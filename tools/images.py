"""Tạo ảnh 16:9 cho từng cảnh bằng model ảnh Gemini.

    python -m tools.images videos/<thư-mục>
    python -m tools.images videos/<thư-mục> --only s03,s07   # vẽ lại vài cảnh
    python -m tools.images --test                           # vẽ thử 1 ảnh (~0,03 USD)

Kết quả: videos/<thư-mục>/assets/images/<scene-id>.png (1920×1080)
"""

from __future__ import annotations

import argparse
import io
import re
from pathlib import Path

from PIL import Image, ImageOps

from tools import config, costs, gemini, scenes

# Khuôn prompt 6 lớp: khung → chủ thể (+ linh vật) → máy quay → ánh sáng → nhận diện kênh → cấm.
# Nội dung cảnh đứng đầu vì model ảnh chú ý phần đầu prompt nhiều nhất.
ASPECT_PREFIX = "Wide 16:9 landscape cinematic frame."
# Luôn thêm vào cuối prompt để tránh chữ/logo do AI vẽ (chữ thật được chèn khi dựng video).
GUARD = (
    "No text, no letters, no logos, no watermark, no signature. "
    "Original character designs only, not resembling any existing anime or manga character"
)
# Cho các model nhận negative prompt riêng (Stable Diffusion, Flux, …); Gemini dùng GUARD ở trên.
NEGATIVE = (
    "text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, "
    "low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, "
    "official art, screenshot"
)

_SHOT = re.compile(
    r"\b(close-up|close up|wide shot|medium shot|establishing|low-angle|low angle|high-angle|high angle|"
    r"top-down|overhead|aerial|bird's-eye|macro|over-the-shoulder|side view|front view|split down|split screen|"
    r"split composition)\b",
    re.I,
)
_LIGHT = re.compile(
    r"\b(light|lights|lit|glow|glows|glowing|glint|glinting|sunset|sunrise|dawn|dusk|moon|moonlight|candle|"
    r"candlelight|lantern|lamp|lamplight|neon|fire|flame|flames|shadow|shadows|dark|darkness|dim|bright|sun|"
    r"rain|night|storm|lightning)\b",
    re.I,
)
# (tên nhóm, từ khóa, gợi ý máy quay) — nhóm đầu tiên khớp sẽ được dùng.
_CAMERA_RULES = [
    ("compare", r"\b(two|split|versus|vs|side by side|mirrored|both|left half|right half|panels|triptych)\b",
     "clean side-by-side panel composition, each part equally balanced"),
    ("diagram", r"\b(diagram|chart|graph|gauge|timeline|status window|stat bars?|stat card|scorecard|blueprint|"
     r"family tree|pyramid|flowchart|infographic|icons?|meter|table of|grid of|ranking|tier list|scoreboard)\b",
     "clean centered composition with the diagram as the clear focal point, flat front view, generous negative space"),
    ("figure", r"\b(man|woman|men|women|boy|girl|people|crowd|child|children|(?:figure|silhouette|warrior|swordsman|"
     r"ninja|mage|fighter|hunter|person|soldier|strategist|king|queen|hero|villain|monster|creature|giant|titan|"
     r"demon|sorcerer|witch|pirate|samurai|knight|elf|student|mentor|teenager|brother|sister|reader|diviner|priest|"
     r"monk|gardener|founder|traveler|merchant|scholar|doctor|scientist|guard|chef|captain|detective|trainee)s?)\b",
     "medium shot, expressive body language, strong readable silhouette"),
    ("landscape", r"\b(city|cities|landscape|sea|seas|ocean|mountain|mountains|sky|island|islands|world|kingdom|"
     r"forest|desert|village|ruins|hellscape|void|horizon|valley|castle|space|planet|continents?|coast|harbor)\b",
     "wide establishing shot with deep perspective"),
    ("map", r"\bmaps?\b", "top-down overhead view of the map, slight perspective tilt"),
    ("object", r"\b(book|scroll|key|coin|sword|blade|pen|lantern|seed|card|cup|jar|ring|mask|hand|hands|eye|eyes|"
     r"letter|page|notebook|fruit|stone|crystal|bell|compass|hourglass|feather|gem|orb)\b",
     "close-up detail shot with shallow depth of field"),
]
# Cảnh nhân vật có sức mạnh bùng nổ thì đổi sang góc thấp cho có khí thế.
_POWER = re.compile(r"\b(aura|power|energy|attack|punch|strike|clash|battle|explosion|fist|roar|lightning|unleash\w*)\b", re.I)
_POWER_CAMERA = "dynamic low-angle shot, sense of overwhelming power"
_MASCOT_CAMERA = "medium shot at eye level, the mascot in sharp focus in the foreground"
_DEFAULT_CAMERA = "cinematic medium-wide shot, rule-of-thirds composition"
_CHAPTER_CAMERA = "wide establishing shot with deep perspective"
DEFAULT_LIGHT = "moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light"
DIAGRAM_LIGHT = "diagram lines glowing softly in white and amber, deep navy surroundings"


def camera_kind(scene: scenes.Scene) -> str:
    """Nhóm bố cục của cảnh: mascot, compare, diagram, figure, landscape, map, object, chapter hoặc default.

    Chọn nhóm có từ khóa xuất hiện sớm nhất trong prompt (thường là chủ thể chính của câu).
    """
    if scene.use_mascot:
        return "mascot"
    hits = []
    for order, (kind, pattern, _) in enumerate(_CAMERA_RULES):
        m = re.search(pattern, scene.image_prompt, re.I)
        if m:
            hits.append((m.start(), order, kind))
    if hits:
        return min(hits)[2]
    return "chapter" if scene.chapter else "default"


def camera_hint(scene: scenes.Scene) -> str:
    """Cỡ cảnh / góc máy, chỉ thêm khi image_prompt chưa tự ghi."""
    if _SHOT.search(scene.image_prompt):
        return ""
    kind = camera_kind(scene)
    if kind == "figure" and _POWER.search(scene.image_prompt):
        return _POWER_CAMERA
    hints = {k: h for k, _, h in _CAMERA_RULES}
    hints.update(mascot=_MASCOT_CAMERA, chapter=_CHAPTER_CAMERA, default=_DEFAULT_CAMERA)
    return hints[kind]


def light_hint(scene: scenes.Scene) -> str:
    """Ánh sáng theo bảng màu kênh, chỉ thêm khi image_prompt chưa tự ghi."""
    if _LIGHT.search(scene.image_prompt):
        return ""
    return DIAGRAM_LIGHT if camera_kind(scene) == "diagram" else DEFAULT_LIGHT


def build_prompt(board: scenes.Storyboard, scene: scenes.Scene) -> str:
    parts = [ASPECT_PREFIX, scene.image_prompt]
    if scene.use_mascot:
        parts.append(f"The channel mascot: {board.mascot_prompt}")
    parts += [camera_hint(scene), light_hint(scene), board.style_prompt, GUARD]
    return " ".join(p.strip().rstrip(".") + "." for p in parts if p.strip())


def fit_frame(img: Image.Image, trim: float = 0.0) -> Image.Image:
    """Cắt bỏ `trim` (tỉ lệ) ở mỗi cạnh rồi cắt/co về đúng khung video 1920×1080."""
    img = img.convert("RGB")
    if trim:
        w, h = img.size
        dx, dy = round(w * trim), round(h * trim)
        img = img.crop((dx, dy, w - dx, h - dy))
    return ImageOps.fit(img, (config.WIDTH, config.HEIGHT), Image.Resampling.LANCZOS)


def generate(prompt: str) -> tuple[Path, bool]:
    """Trả về (PNG 1920×1080 trong cache, có gọi API mới hay không)."""
    cached = gemini.cache_path("images", config.IMAGE_MODEL, prompt, suffix=".png")
    if cached.exists():
        return cached, False

    from google.genai import types

    cfg = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="16:9"),
    )
    resp = gemini.with_retry(
        lambda: gemini.client().models.generate_content(model=config.IMAGE_MODEL, contents=prompt, config=cfg)
    )
    data = next(
        (p.inline_data.data for p in resp.candidates[0].content.parts if p.inline_data and p.inline_data.data),
        None,
    )
    if not data:
        raise RuntimeError(f"model không trả về ảnh (có thể bị chặn nội dung) cho prompt: {prompt[:80]}...")
    img = fit_frame(Image.open(io.BytesIO(data)))
    cached.parent.mkdir(parents=True, exist_ok=True)
    img.save(cached)
    return cached, True


def run(video_dir: Path, only: set[str] | None = None) -> None:
    board = scenes.load(video_dir)
    out_dir = Path(video_dir) / "assets" / "images"
    out_dir.mkdir(parents=True, exist_ok=True)
    for scene in board.scenes:
        if only and scene.id not in only:
            continue
        png, fresh = generate(build_prompt(board, scene))
        (out_dir / f"{scene.id}.png").write_bytes(png.read_bytes())
        if fresh:
            costs.add_usage(video_dir, images=1)
        print(f"{scene.id}{'' if fresh else ' (cache)'}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path, nargs="?")
    p.add_argument("--only", help="danh sách id cảnh, cách nhau bằng dấu phẩy")
    p.add_argument("--test", action="store_true")
    args = p.parse_args()

    if args.test:
        png, _ = generate(
            "Anime illustration, dramatic lighting. A lone swordsman silhouette on a cliff at sunset. " + GUARD + "."
        )
        dst = config.CACHE_DIR / "test" / "image.png"
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(png.read_bytes())
        print(dst)
        return
    if not args.video_dir:
        p.error("cần video_dir hoặc --test")
    run(args.video_dir, set(args.only.split(",")) if args.only else None)


if __name__ == "__main__":
    gemini.cli(main)
