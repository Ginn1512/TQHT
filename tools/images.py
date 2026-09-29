"""Tạo ảnh 16:9 cho từng cảnh bằng model ảnh Gemini.

    python -m tools.images videos/<thư-mục>
    python -m tools.images videos/<thư-mục> --only s03,s07   # vẽ lại vài cảnh
    python -m tools.images --test                           # vẽ thử 1 ảnh (~0,03 USD)

Kết quả: videos/<thư-mục>/assets/images/<scene-id>.png (1920×1080)
"""

from __future__ import annotations

import argparse
import io
from pathlib import Path

from PIL import Image, ImageOps

from tools import config, costs, gemini, scenes

# Luôn thêm vào cuối prompt để tránh chữ/logo do AI vẽ (chữ thật được chèn khi dựng video).
GUARD = "No text, no letters, no logos, no watermark. Original character designs only."


def build_prompt(board: scenes.Storyboard, scene: scenes.Scene) -> str:
    parts = [board.style_prompt, scene.image_prompt]
    if scene.use_mascot:
        parts.append(f"Featuring the channel mascot: {board.mascot_prompt}")
    parts.append(GUARD)
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
            "Anime illustration, dramatic lighting. A lone swordsman silhouette on a cliff at sunset. " + GUARD
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
