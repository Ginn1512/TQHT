"""Chuẩn bị kịch bản để chép vào trang Notion của video (bảng "Video dài").

    python -m tools.notion_export videos/<thư-mục>    # in Markdown để dán vào trang Notion
    python -m tools.notion_export --numbers 1-9       # thư mục của video 1–9 theo channel/topics.md

Notion chỉ là **bản đọc**. Bản gốc là scenes.json (script.vi.md tạo từ đó). Mỗi bản chép ghi
commit của script.vi.md lúc chép. Nếu `git log -1 -- videos/<x>/script.vi.md` ra commit khác,
bản trên Notion đã cũ và cần chép lại. Người dùng góp ý bằng bình luận trên Notion; không sửa
thẳng trên trang, vì lần chép sau sẽ ghi đè.

Cột "Kịch bản" của bảng là công thức dẫn tới bản mới nhất trên GitHub, nên không cần chép
mới đọc được.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from tools import canon, config

REPO_URL = "https://github.com/Ginn1512/TQHT"


def script_url(video_dir: Path) -> str:
    rel = (Path(video_dir).resolve() / "script.vi.md").relative_to(config.ROOT).as_posix()
    return f"{REPO_URL}/blob/HEAD/{rel}"


def last_commit(path: Path) -> tuple[str, str]:
    """(commit rút gọn, ngày) của lần cuối file được commit; ("chưa commit", "") nếu chưa có."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%h %cs", "--", str(path)], cwd=config.ROOT, capture_output=True, text=True
    ).stdout.split()
    return (out[0], out[1]) if len(out) == 2 else ("chưa commit", "")


def body(script: str) -> str:
    """Bỏ tiêu đề "# Kịch bản — …" và dòng ghi chú "> Sinh từ scenes.json…" ở đầu file."""
    lines = script.splitlines()
    while lines and (lines[0].startswith("# ") or lines[0].startswith(">") or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines).strip() + "\n"


def render(video_dir: Path) -> str:
    video_dir = Path(video_dir)
    script = video_dir / "script.vi.md"
    commit, date = last_commit(script)
    stamp = f"commit {commit}, {date}" if date else commit
    note = (
        f"> Bản chép từ `script.vi.md` ({stamp}). Bản mới nhất: [GitHub]({script_url(video_dir)}).\n"
        "> Muốn sửa: bình luận trên trang này hoặc nhắn Claude. Đừng sửa thẳng ở đây, vì lần chép sau sẽ ghi đè.\n\n"
    )
    return note + body(script.read_text(encoding="utf-8"))


def folders(numbers: str) -> list[str]:
    """Thư mục của các video theo số trong channel/topics.md, ví dụ "1-9" hoặc "1,4,7"."""
    wanted: set[int] = set()
    for part in numbers.split(","):
        a, _, b = part.partition("-")
        wanted.update(range(int(a), int(b or a) + 1))
    by_number = {num: folder for folder, (num, _) in canon.video_numbers().items()}
    return [f"videos/{by_number[n]}" for n in sorted(wanted) if n in by_number]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path, nargs="?")
    p.add_argument("--numbers", help='số video, ví dụ "1-9"; in danh sách thư mục')
    args = p.parse_args()
    if args.numbers:
        print("\n".join(folders(args.numbers)))
        return
    if not args.video_dir:
        p.error("cần video_dir hoặc --numbers")
    print(render(args.video_dir), end="")


if __name__ == "__main__":
    main()
