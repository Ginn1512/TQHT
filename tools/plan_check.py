"""Kiểm tra kế hoạch nội dung theo luật trong `channel/formats.md`.

    python -m tools.plan_check

- Không có 2 video liền nhau cùng dạng.
- Trong mỗi 30 video liên tiếp, một dạng xuất hiện tối đa 2 lần.
- Mỗi thư mục video đã có kịch bản phải dài 15–20 phút (ước tính từ lời thoại).

Đọc bảng trong `channel/topics.md`; cần các cột "#", "Dạng" và "Thư mục".
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from tools import config, costs, scenes, timing

WINDOW = 30
MAX_PER_WINDOW = 2


@dataclass(frozen=True)
class Planned:
    number: int
    fmt: str  # mã dạng, ví dụ "A"
    folder: str  # tên thư mục trong videos/, rỗng nếu chưa có


def parse_topics(text: str) -> list[Planned]:
    """Lấy các dòng của bảng markdown có cột "#", "Dạng" và "Thư mục"."""
    header: list[str] | None = None
    rows: list[Planned] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if not {"#", "Dạng", "Thư mục"} <= set(header) or len(cells) != len(header):
            continue
        row = dict(zip(header, cells))
        if not row["#"].isdigit():
            continue
        code = re.match(r"[A-Z]", row["Dạng"])
        folder = row["Thư mục"].strip("`").rstrip("/").split("/")[-1]
        rows.append(Planned(int(row["#"]), code.group(0) if code else "?", folder))
    return sorted(rows, key=lambda p: p.number)


def format_problems(plan: list[Planned], window: int = WINDOW, max_per: int = MAX_PER_WINDOW) -> list[str]:
    problems = []
    for a, b in zip(plan, plan[1:]):
        if a.fmt == b.fmt:
            problems.append(f"video {a.number} và {b.number} liền nhau cùng dạng {a.fmt}")
    reported = set()
    for i in range(max(1, len(plan) - window + 1)):
        for fmt, n in Counter(p.fmt for p in plan[i : i + window]).items():
            if n > max_per and fmt not in reported:
                reported.add(fmt)
                problems.append(f"dạng {fmt} xuất hiện {n} lần trong {window} video liên tiếp (tối đa {max_per})")
    return problems


def length_problems(plan: list[Planned], videos_dir: Path) -> tuple[list[str], dict[int, float]]:
    problems, minutes = [], {}
    for p in plan:
        folder = videos_dir / p.folder if p.folder else None
        if not folder or not (folder / "scenes.json").exists():
            continue
        total_s = costs.video_seconds(scenes.load(folder))
        minutes[p.number] = round(total_s / 60, 1)
        problem = timing.length_problem(total_s)
        if problem:
            problems.append(f"video {p.number} ({p.folder}): {problem}")
    return problems, minutes


def main() -> int:
    plan = parse_topics((config.CHANNEL_DIR / "topics.md").read_text(encoding="utf-8"))
    if not plan:
        print("Không đọc được bảng chủ đề (cần các cột #, Dạng, Thư mục).")
        return 1
    problems = format_problems(plan)
    length, minutes = length_problems(plan, config.ROOT / "videos")
    problems += length
    for p in plan:
        mins = f"{minutes[p.number]:.1f} phút" if p.number in minutes else "chưa có kịch bản"
        print(f"{p.number:>3}  {p.fmt}  {mins:<17} {p.folder}")
    print(f"\n{len(plan)} video, {len(minutes)} đã có kịch bản, dạng dùng: {dict(sorted(Counter(p.fmt for p in plan).items()))}")
    for msg in problems:
        print("LỖI:", msg)
    if not problems:
        print("Đạt: không có dạng lặp liền nhau, không dạng nào quá giới hạn, độ dài đều trong 15–20 phút.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
