"""Tạo thumbnail 1280×720: ảnh nền + chữ lớn có viền.

    python -m tools.thumbnail videos/<thư-mục> --text "BÍ MẬT CỦA HASHIRA" --bg s05
    python -m tools.thumbnail videos/<thư-mục> --text "..." --prompt "anime illustration of ..."   # vẽ nền mới (~0,03 USD)

--bg nhận id cảnh (dùng assets/images/<id>.png) hoặc đường dẫn ảnh.
Kết quả: videos/<thư-mục>/render/thumbnail.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from tools import config

SIZE = (1280, 720)
FONT = config.FONTS_DIR / "BeVietnamPro-ExtraBold.ttf"
ACCENT = (255, 214, 0)


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        if lines and draw.textlength(f"{lines[-1]} {word}", font=font) <= max_w:
            lines[-1] = f"{lines[-1]} {word}"
        else:
            lines.append(word)
    return lines


def compose(background: Path, text: str, out: Path) -> Path:
    w, h = SIZE
    img = ImageOps.fit(Image.open(background).convert("RGB"), SIZE, Image.Resampling.LANCZOS)

    # Làm tối dần nửa trái để chữ luôn dễ đọc.
    shade = Image.new("L", SIZE)
    ImageDraw.Draw(shade).rectangle((0, 0, w, h), fill=0)
    for x in range(int(w * 0.7)):
        ImageDraw.Draw(shade).line([(x, 0), (x, h)], fill=int(170 * (1 - x / (w * 0.7))))
    img = Image.composite(Image.new("RGB", SIZE, (0, 0, 0)), img, shade)

    draw = ImageDraw.Draw(img)
    max_w = int(w * 0.62)
    size = 120
    while size > 48:  # giảm cỡ chữ cho đến khi vừa tối đa 3 dòng
        font = ImageFont.truetype(str(FONT), size)
        lines = wrap(draw, text.upper(), font, max_w)
        if len(lines) <= 3 and all(draw.textlength(line, font=font) <= max_w for line in lines):
            break
        size -= 6
    line_h = int(size * 1.15)
    y = (h - line_h * len(lines)) // 2
    for i, line in enumerate(lines):
        fill = ACCENT if i == len(lines) - 1 else (255, 255, 255)
        draw.text((60, y + i * line_h), line, font=font, fill=fill, stroke_width=max(4, size // 14), stroke_fill=(0, 0, 0))

    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True)
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path)
    p.add_argument("--text", required=True)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--bg", help="id cảnh hoặc đường dẫn ảnh nền")
    src.add_argument("--prompt", help="vẽ ảnh nền mới bằng AI")
    args = p.parse_args()

    if args.prompt:
        from tools import costs, images

        bg, fresh = images.generate(f"{args.prompt} {images.GUARD}")
        if fresh:
            costs.add_usage(args.video_dir, images=1)
    else:
        candidate = args.video_dir / "assets" / "images" / f"{args.bg}.png"
        bg = candidate if candidate.exists() else Path(args.bg)
    out = compose(bg, args.text, args.video_dir / "render" / "thumbnail.png")
    print(out)


if __name__ == "__main__":
    from tools import gemini

    gemini.cli(main)
