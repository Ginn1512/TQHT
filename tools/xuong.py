"""Trang "Xưởng Kaku" của một video: làm ảnh (Gemini app) và giọng (AI Studio, ElevenLabs…) trên điện thoại.

    python -m tools.xuong page videos/<thư-mục> --label "video 2" > xuong-2.html

Đăng file HTML bằng Artifact với capabilities {"assets": {}, "db": {}}. Trang lưu:
- `images/<scene-id>` (và `images/kaku-ref`): {asset, type, size, name, redo, at}
- `audio/<cNN>`: {asset, mime, name, size, seconds, engine, at}. Asset là văn bản base64 có dòng đầu
  "KAKU-AUDIO-B64 1 <mime> <tên>", vì kho tệp của trang không nhận file âm thanh; `tools.app_audio import`
  tự mở gói này.
- `checks/main`: {items: {khóa: true/false}}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools import app_audio, app_images, config, scenes

TEMPLATE = config.ROOT / "tools" / "templates" / "xuong.html"


def page_data(board: scenes.Storyboard, label: str) -> dict:
    images = app_images.export(board)
    for item, scene in zip(images["scenes"], board.scenes):
        item["say"] = scene.narration.get(config.PRIMARY_LANGUAGE, "")
    return {"label": label, "title": board.title, "images": images, "voice": app_audio.export(board)}


def build_page(board: scenes.Storyboard, label: str) -> str:
    payload = json.dumps(page_data(board, label), ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("__LABEL__", label).replace("__DATA__", payload)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    pg = sub.add_parser("page")
    pg.add_argument("video_dir", type=Path)
    pg.add_argument("--label", required=True, help='ví dụ "video 2"')
    args = p.parse_args()
    sys.stdout.write(build_page(scenes.load(args.video_dir), args.label))


if __name__ == "__main__":
    main()
