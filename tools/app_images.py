"""Ảnh tạo thủ công bằng Gemini app (gói Gemini Plus): xuất prompt và nhập ảnh vào video.

    python -m tools.app_images export videos/<thư-mục>                  # JSON prompt (trang Xưởng: tools.xuong)
    python -m tools.app_images import videos/<thư-mục> --from <folder>   # ảnh <scene-id>.* → assets/images
    python -m tools.app_images import videos/<thư-mục> --from <folder> --trim 0.05   # cắt viền (watermark góc)

Ảnh từ app không tốn tiền API; chỉ ghi số lượng vào cost.json (`images_app`).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

from tools import costs, images, scenes

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def mascot_reference_prompt(board: scenes.Storyboard) -> str:
    """Prompt tạo ảnh mẫu linh vật (dùng cho cả kênh), làm ảnh tham chiếu cho mọi cảnh có linh vật."""
    return (
        f"{images.ASPECT_PREFIX} Character model sheet of the channel mascot on a plain warm parchment background: "
        f"front view, three-quarter view and side view, full body, identical proportions and colors in every view: "
        f"{board.mascot_prompt}. Even soft studio lighting. {board.style_prompt}. {images.GUARD}."
    )


def export(board: scenes.Storyboard) -> dict:
    """Prompt ảnh cho mọi công cụ: Gemini app lúc làm tay, API hay model khác sau này (kèm negative)."""
    return {
        "title": board.title,
        "mascot_reference": mascot_reference_prompt(board),
        "negative": images.NEGATIVE,
        "scenes": [
            {"id": s.id, "chapter": s.chapter, "mascot": s.use_mascot, "prompt": images.build_prompt(board, s)}
            for s in board.scenes
        ],
    }


def find_sources(folder: Path) -> dict[str, Path]:
    """{scene id: file} theo tên file (s01.png, s01.jpg, …). Bỏ qua file không phải ảnh."""
    return {p.stem: p for p in sorted(Path(folder).iterdir()) if p.suffix.lower() in IMAGE_EXTS}


def import_images(video_dir: Path, folder: Path, trim: float = 0.0) -> tuple[list[str], list[str]]:
    """Chuẩn hoá ảnh về 1920×1080 vào assets/images. Trả về (id đã nhập, id còn thiếu)."""
    board = scenes.load(video_dir)
    sources = find_sources(folder)
    out_dir = Path(video_dir) / "assets" / "images"
    out_dir.mkdir(parents=True, exist_ok=True)
    done, missing = [], []
    for s in board.scenes:
        src = sources.get(s.id)
        if not src:
            missing.append(s.id)
            continue
        with Image.open(src) as img:
            images.fit_frame(img, trim).save(out_dir / f"{s.id}.png")
        done.append(s.id)
    usage = costs.load_usage(video_dir)
    usage["images_app"] = len(list(out_dir.glob("*.png")))
    usage["usd"] = costs.usd_of(usage)
    (Path(video_dir) / costs.COST_FILE).write_text(json.dumps(usage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return done, missing


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("video_dir", type=Path)
    i = sub.add_parser("import")
    i.add_argument("video_dir", type=Path)
    i.add_argument("--from", dest="folder", type=Path, required=True)
    i.add_argument("--trim", type=float, default=0.0, help="tỉ lệ cắt bỏ ở mỗi cạnh, ví dụ 0.05")
    args = p.parse_args()

    if args.cmd == "export":
        json.dump(export(scenes.load(args.video_dir)), sys.stdout, ensure_ascii=False, indent=1)
        print()
        return
    done, missing = import_images(args.video_dir, args.folder, args.trim)
    print(f"Đã nhập {len(done)} ảnh.")
    if missing:
        print(f"Còn thiếu {len(missing)} cảnh: {', '.join(missing)}")


if __name__ == "__main__":
    main()
