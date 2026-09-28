"""Quét image_prompt / video_prompt tìm tên riêng và chi tiết thiết kế đặc trưng bị cấm.

    python -m tools.prompt_check videos/<thư-mục> [videos/<thư-mục> ...]
    python -m tools.prompt_check --all

Danh sách từ cấm: `channel/prompt-blocklist.txt`. Thoát mã 1 nếu còn vi phạm.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from tools import config

BLOCKLIST = config.CHANNEL_DIR / "prompt-blocklist.txt"
FIELDS = ("image_prompt", "video_prompt")


def load_patterns(text: str) -> list[re.Pattern]:
    patterns = []
    for line in text.splitlines():
        term = line.strip()
        if not term or term.startswith("#"):
            continue
        flags = 0
        if term.startswith("i:"):
            term, flags = term[2:].strip(), re.IGNORECASE
        patterns.append(re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", flags))
    return patterns


def violations(board: dict, patterns: list[re.Pattern]) -> list[tuple[str, str, str]]:
    """Trả về (id cảnh, trường, từ khớp) cho mọi prompt vi phạm."""
    found = []
    for scene in board.get("scenes", []):
        for field in FIELDS:
            text = scene.get(field, "")
            for pat in patterns:
                m = pat.search(text)
                if m:
                    found.append((scene.get("id", "?"), field, m.group(0)))
    return found


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dirs", nargs="*", type=Path)
    p.add_argument("--all", action="store_true", help="quét mọi thư mục trong videos/")
    args = p.parse_args()
    dirs = sorted((config.ROOT / "videos").glob("*/")) if args.all else args.video_dirs
    if not dirs:
        p.error("cần ít nhất một thư mục video hoặc --all")
    patterns = load_patterns(BLOCKLIST.read_text(encoding="utf-8"))
    total = 0
    for d in dirs:
        board = json.loads((Path(d) / "scenes.json").read_text(encoding="utf-8"))
        for sid, field, term in violations(board, patterns):
            print(f"{Path(d).name} {sid} {field}: '{term}'")
            total += 1
    print(f"{len(dirs)} video, {total} vi phạm." if total else f"{len(dirs)} video, không có vi phạm.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
