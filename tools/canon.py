"""Sổ khẳng định về anime: gom bảng "Sự thật dùng trong kịch bản" của mọi brief.md.

    python -m tools.canon build            # ghi channel/canon-ledger.md (tạo tự động, không sửa tay)
    python -m tools.canon build --check    # báo nếu sổ cũ hơn các brief.md
    python -m tools.canon check videos/<thư-mục>     # dừng (mã 1) nếu còn dòng chưa kiểm
    python -m tools.canon resolve videos/<thư-mục> 3 --source "[Tên trang](https://…)"

brief.md là nguồn gốc. Muốn đổi trạng thái một dòng thì sửa brief.md (hoặc dùng
`resolve`), rồi chạy lại `build`.

Mức chắc chắn của mỗi dòng (đọc từ ô nguồn / tình trạng):
- da-kiem      có "đã kiểm YYYY-MM-DD": đã mở trang nguồn và đối chiếu.
- co-nguon     có link nguồn, không kèm lời dè dặt.
- y-kien       ý kiến, ghi chú, trò chơi của kênh hoặc lý thuyết đã gắn nhãn trong kịch bản: không cần nguồn.
- chua-mo      "chỉ thấy trong kết quả tìm kiếm, chưa mở trang".
- can-kiem     "cần kiểm lại" hoặc "cần thêm nguồn".
- khong-ro     không có link, không có nhãn nào ở trên.
Ba mức cuối là CHƯA KIỂM: `check` báo lỗi và bước làm giọng phải chờ.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from tools import config

VIDEOS_DIR = config.ROOT / "videos"
TOPICS = config.CHANNEL_DIR / "topics.md"
LEDGER = config.CHANNEL_DIR / "canon-ledger.md"

RESOLVED = ("da-kiem", "co-nguon", "y-kien")
UNRESOLVED = ("chua-mo", "can-kiem", "khong-ro")
LABELS = {
    "da-kiem": "Đã kiểm",
    "co-nguon": "Có nguồn",
    "y-kien": "Ý kiến / lý thuyết đã gắn nhãn",
    "chua-mo": "Chưa mở trang",
    "can-kiem": "Cần kiểm lại",
    "khong-ro": "Không rõ nguồn",
}

_OPINION = ("của kênh", "ý kiến", "lý thuyết", "suy đoán", "suy luận", "gắn nhãn", "diễn giải")
# Tên khác nhau của cùng một bộ, để gom việc kiểm theo bộ.
ALIASES = {
    "Naruto Shippuden": "Naruto",
    "Sousou no Frieren": "Frieren",
    "Dragon Ball Z": "Dragon Ball",
    "Dragon Ball Super": "Dragon Ball",
    "JoJo's Bizarre Adventure": "JoJo",
    "JoJo's Bizarre Adventure Part 7: Steel Ball Run": "JoJo",
    "Mashle: Magic and Muscles": "Mashle",
    "The Apothecary Diaries": "Dược sư tự sự",
    "Cyberpunk: Edgerunners": "Cyberpunk Edgerunners",
}
_LINK = re.compile(r"\[[^\]]*\]\(https?://[^)\s]+\)|https?://\S+")
_CHECKED = re.compile(r"đã kiểm\s+(\d{4}-\d{2}-\d{2})", re.I)


@dataclass(frozen=True)
class Claim:
    video: str  # tên thư mục
    row: int  # thứ tự dòng trong bảng, từ 1
    text: str
    source: str  # ô nguồn và tình trạng, gộp lại
    status: str

    @property
    def resolved(self) -> bool:
        return self.status in RESOLVED


def has_link(source: str) -> bool:
    """Ô nguồn có link (dạng Markdown hoặc URL trần)."""
    return bool(_LINK.search(source))


def classify(source: str) -> str:
    low = source.lower()
    if _CHECKED.search(source):
        return "da-kiem"
    if "cần kiểm lại" in low or "cần thêm nguồn" in low:
        return "can-kiem"
    if "chưa mở trang" in low or "kết quả tìm kiếm" in low:
        return "chua-mo"
    if any(k in low for k in _OPINION):
        return "y-kien"
    if has_link(source):
        return "co-nguon"
    return "khong-ro"


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _table(lines: list[str]) -> tuple[int, list[str], list[int]]:
    """Tìm bảng sự thật. Trả về (chỉ số dòng tiêu đề, các cột, chỉ số các dòng dữ liệu)."""
    in_section = False
    for i, line in enumerate(lines):
        if line.startswith("## "):
            in_section = line.startswith("## Sự thật")
            continue
        if in_section and line.startswith("|"):
            header = _cells(line)
            rows = []
            for j in range(i + 1, len(lines)):
                if not lines[j].startswith("|"):
                    break
                if set("".join(_cells(lines[j]))) <= set("-: "):
                    continue
                rows.append(j)
            return i, header, rows
    return -1, [], []


def parse_brief(path: Path) -> list[Claim]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    _, header, rows = _table(lines)
    video = Path(path).parent.name
    claims = []
    for n, j in enumerate(rows, 1):
        cells = _cells(lines[j])
        if len(cells) < 2:
            continue
        source = " — ".join(c for c in cells[1:] if c)
        claims.append(Claim(video, n, cells[0], source, classify(source)))
    return claims


def anime_of(brief: Path) -> str:
    m = re.search(r"^- \*\*Anime:\*\*\s*(.+)$", Path(brief).read_text(encoding="utf-8"), re.M)
    if not m:
        return "?"
    raw = re.split(r"\s+\(|;\s", m.group(1).strip().rstrip("."))[0].strip()
    names: list[str] = []
    for part in re.split(r"\s*/\s*|,\s+", raw):
        name = ALIASES.get(part.strip(), part.strip())
        if name and name not in names:
            names.append(name)
    return " / ".join(names) or "?"


def video_numbers(topics: Path = TOPICS) -> dict[str, tuple[int, str]]:
    """{thư mục: (số video, ngày)} lấy từ channel/topics.md."""
    out = {}
    if not topics.exists():
        return out
    for line in topics.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (\d+) \| (\d{4}-\d{2}-\d{2}) \|.*`videos/([^`/]+)/?`", line)
        if m:
            out[m.group(3)] = (int(m.group(1)), m.group(2))
    return out


def all_claims(videos_dir: Path = VIDEOS_DIR) -> dict[str, list[Claim]]:
    return {b.parent.name: parse_brief(b) for b in sorted(Path(videos_dir).glob("*/brief.md"))}


def render_ledger(videos_dir: Path = VIDEOS_DIR, topics: Path = TOPICS) -> str:
    claims = all_claims(videos_dir)
    numbers = video_numbers(topics)
    animes = {v: anime_of(Path(videos_dir) / v / "brief.md") for v in claims}
    total = Counter(c.status for cs in claims.values() for c in cs)
    n_claims = sum(total.values())
    n_open = sum(total[s] for s in UNRESOLVED)
    ready = sum(1 for cs in claims.values() if all(c.resolved for c in cs))

    out = [
        "# Sổ khẳng định (canon ledger)",
        "",
        "> Tạo tự động bằng `python -m tools.canon build` từ bảng sự thật trong `videos/*/brief.md`. **Không sửa tay**: sửa `brief.md` (hoặc `python -m tools.canon resolve`), rồi chạy lại `build`.",
        "",
        f"{n_claims} khẳng định trong {len(claims)} video. **{n_open} chưa kiểm.** {ready}/{len(claims)} video sẵn sàng làm giọng.",
        "",
        "| Mức | Số dòng |",
        "|---|---|",
    ]
    out += [f"| {LABELS[s]} | {total[s]} |" for s in (*RESOLVED, *UNRESOLVED)]
    out += ["", "## Theo video", "", "| # | Ngày | Video | Anime | Đã kiểm / có nguồn | Chưa kiểm | Sẵn sàng làm giọng |", "|---|---|---|---|---|---|---|"]
    order = sorted(claims, key=lambda v: (numbers.get(v, (10**6, ""))[0], v))
    for v in order:
        cs = claims[v]
        num, date = numbers.get(v, ("?", "?"))
        ok = sum(c.resolved for c in cs)
        out.append(f"| {num} | {date} | `{v}` | {animes[v]} | {ok} | {len(cs) - ok} | {'Có' if cs and ok == len(cs) else 'Chưa'} |")

    out += ["", "## Chưa kiểm, gom theo bộ", "", "Kiểm cả nhóm một lần: cùng một chi tiết thường xuất hiện ở nhiều video của cùng bộ.", ""]
    by_anime: dict[str, list[Claim]] = defaultdict(list)
    for v in order:
        by_anime[animes[v]] += [c for c in claims[v] if not c.resolved]
    for anime in sorted(by_anime, key=lambda a: (-len(by_anime[a]), a)):
        items = by_anime[anime]
        if not items:
            continue
        out += [f"### {anime} ({len(items)})", ""]
        for c in items:
            num = numbers.get(c.video, ("?",))[0]
            out.append(f"- Video {num}, dòng {c.row} · {LABELS[c.status]}: {c.text}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def check(video_dir: Path) -> list[Claim]:
    """Các dòng chưa kiểm của một video."""
    brief = Path(video_dir) / "brief.md"
    if not brief.exists():
        raise SystemExit(f"Không thấy {brief}")
    return [c for c in parse_brief(brief) if not c.resolved]


def resolve(video_dir: Path, row: int, source: str, today: str | None = None) -> str:
    """Ghi nguồn đã mở và ngày kiểm vào dòng `row` của bảng sự thật. Trả về dòng mới."""
    if not _LINK.search(source):
        raise SystemExit("--source phải có link, ví dụ \"[Tên trang](https://…)\"")
    today = today or dt.date.today().isoformat()
    brief = Path(video_dir) / "brief.md"
    lines = brief.read_text(encoding="utf-8").splitlines()
    _, header, rows = _table(lines)
    if not 1 <= row <= len(rows):
        raise SystemExit(f"Bảng chỉ có {len(rows)} dòng")
    j = rows[row - 1]
    cells = _cells(lines[j])
    stamp = f"đã kiểm {today}"
    if len(header) >= 3:
        cells = [cells[0], source, stamp] + [""] * (len(header) - 3)
    else:
        cells = [cells[0], f"{source} — {stamp}"]
    lines[j] = "| " + " | ".join(cells) + " |"
    brief.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return lines[j]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--check", action="store_true", help="chỉ kiểm sổ có khớp các brief.md không")
    c = sub.add_parser("check")
    c.add_argument("video_dir", type=Path)
    r = sub.add_parser("resolve")
    r.add_argument("video_dir", type=Path)
    r.add_argument("row", type=int, help="thứ tự dòng trong bảng sự thật, từ 1")
    r.add_argument("--source", required=True, help='link đã mở, dạng "[Tên](https://…)"')
    args = p.parse_args()

    if args.cmd == "build":
        text = render_ledger()
        if args.check:
            if not LEDGER.exists() or LEDGER.read_text(encoding="utf-8") != text:
                print(f"{LEDGER.relative_to(config.ROOT)} cần tạo lại: python -m tools.canon build")
                sys.exit(1)
            print("Sổ khẳng định khớp các brief.md.")
            return
        LEDGER.write_text(text, encoding="utf-8")
        print(text.splitlines()[4])
        return
    if args.cmd == "check":
        open_claims = check(args.video_dir)
        if not open_claims:
            print("Mọi khẳng định đều đã có nguồn. Làm giọng được.")
            return
        print(f"Còn {len(open_claims)} khẳng định chưa kiểm (chưa nên làm giọng):")
        for cl in open_claims:
            print(f"  dòng {cl.row} · {LABELS[cl.status]}: {cl.text}")
        sys.exit(1)
    print(resolve(args.video_dir, args.row, args.source))
    print("Nhớ chạy lại: python -m tools.canon build")


if __name__ == "__main__":
    main()
