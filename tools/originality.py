"""Chấm độ nguyên bản của một video, trước khi làm ảnh và giọng.

    python -m tools.originality check videos/<thư-mục>     # chấm phần máy, ghi originality.json; mã 1 nếu chưa đạt
    python -m tools.originality score videos/<thư-mục> vi-du-moi 2 --evidence "s40: phép tính tốc độ riêng của kênh"
    python -m tools.originality scan                       # câu lặp và cặp video giống nhau nhất toàn kênh

8 tiêu chí của tài liệu "Policy Safe", mỗi tiêu chí 0–2 điểm, tổng 16:

| Khóa             | Tiêu chí                                              | Ai chấm |
|------------------|-------------------------------------------------------|---------|
| cau-hoi          | Có câu hỏi hoặc luận điểm riêng                       | máy     |
| nguon            | Có nghiên cứu và nguồn được ghi lại                   | máy     |
| binh-luan        | Có bình luận hoặc phân tích của người làm kênh        | máy     |
| vi-du-moi        | Có ví dụ hoặc dữ liệu mới                             | Claude  |
| hinh-co-quyen    | Hình minh họa tự tạo hoặc có giấy phép                | máy     |
| khong-paraphrase | Không phải bản dịch hay paraphrase gần nguyên bản     | Claude  |
| khac-nhau        | Nội dung cốt lõi khác các video khác của kênh         | máy     |
| gia-tri          | Người xem nhận được giá trị rõ ràng                   | Claude  |

Kết luận:
- chưa chấm đủ 8 tiêu chí: "chưa chấm đủ";
- "khong-paraphrase" được 0 (chỉ đọc lại bài viết, transcript hay tin tức): "từ chối";
- tổng dưới 12: "viết lại";
- còn lại: "đạt".
Người xác nhận điểm Claude chấm bằng quyết định trong audit.md (xem tools/release_check.py).
Câu cửa miệng của kênh ("Mở sổ ra nào!"…) không tính là khuôn mẫu khi đo độ trùng.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path

from tools import canon, config, rights, scenes

VIDEOS_DIR = config.ROOT / "videos"
RESULT_NAME = "originality.json"
CRITERIA = {
    "cau-hoi": ("Có câu hỏi hoặc luận điểm riêng", "máy"),
    "nguon": ("Có nghiên cứu và nguồn được ghi lại", "máy"),
    "binh-luan": ("Có bình luận hoặc phân tích của người làm kênh", "máy"),
    "vi-du-moi": ("Có ví dụ hoặc dữ liệu mới", "claude"),
    "hinh-co-quyen": ("Hình minh họa tự tạo hoặc có giấy phép", "máy"),
    "khong-paraphrase": ("Không phải bản dịch hay paraphrase gần nguyên bản", "claude"),
    "khac-nhau": ("Nội dung cốt lõi khác các video khác của kênh", "máy"),
    "gia-tri": ("Người xem nhận được giá trị giáo dục hoặc giải trí rõ ràng", "claude"),
}
MANUAL = tuple(k for k, (_, by) in CRITERIA.items() if by == "claude")
MAX_POINTS = 2 * len(CRITERIA)
GATE = 12  # dưới mức này là viết lại
STRONG = 14  # dưới mức này, audit.md ghi rủi ro "không chân thực" là cao
PASS, REWRITE, REJECT, PENDING = "đạt", "viết lại", "từ chối", "chưa chấm đủ"

# Câu cửa miệng của thương hiệu (channel/profile.md), được phép lặp ở mọi video.
CATCHPHRASES = ("Mở sổ ra nào!", "Mình là Kaku.", "Kaku gấp sổ đây, hẹn gặp lại!")
NGRAM = 5
DISTINCT_OK, DISTINCT_WARN = 0.10, 0.25  # tỉ lệ 5-gram trùng với một video khác

_COMMENT = re.compile(
    r"\b(?:kaku|mình) (?:ghi chú|nghĩ|đoán|để ý|thấy|cho rằng|tin|thích|nhận ra|ngờ)\b"
    r"|\btheo (?:mình|kaku)\b|\bgóc nhìn\b|\blý thuyết\b|\bgiả thuyết\b|\bý kiến\b",
    re.I,
)
_OPINION_CHAPTER = re.compile(
    r"góc nhìn|kaku|bài học|vì sao|tại sao|hiểu lầm|thử nghiệm|nếu|giả thuyết|lý thuyết|ý kiến|đánh giá|xếp hạng|so sánh",
    re.I,
)
_SENTENCE = re.compile(r"(?<=[.!?…])\s+")


def brief_field(text: str, *names: str) -> str:
    """Giá trị của dòng "- **Tên:** …" hoặc nội dung mục "## Tên…" trong brief.md."""
    for name in names:
        m = re.search(rf"^- \*\*{re.escape(name)}[^*\n]*:\*\*\s*(\S.*)$", text, re.M)
        if m:
            return m.group(1).strip()
        m = re.search(rf"^## {re.escape(name)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        if m and m.group(1).strip():
            return m.group(1).strip()
    return ""


def narration(board: scenes.Storyboard, lang: str = config.PRIMARY_LANGUAGE) -> str:
    """Lời thoại cả video, đã bỏ câu cửa miệng."""
    text = " ".join(s.narration.get(lang, "") for s in board.scenes)
    for phrase in CATCHPHRASES:
        text = text.replace(phrase, " ")
    return text


def shingles(text: str, n: int = NGRAM) -> set[tuple[str, ...]]:
    words = re.findall(r"\w+", text.lower())
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def score_question(brief_text: str) -> tuple[int, str]:
    question = brief_field(brief_text, "Câu hỏi video trả lời", "Câu hỏi trung tâm")
    thesis = brief_field(brief_text, "Luận điểm riêng", "Góc nhìn")
    if question and thesis:
        return 2, f"có câu hỏi và luận điểm: {thesis[:90]}"
    if question:
        return 1, "có câu hỏi, chưa có dòng 'Luận điểm riêng' trong brief.md"
    return 0, "brief.md thiếu 'Câu hỏi video trả lời'"


def score_sources(brief: Path) -> tuple[int, str]:
    claims = canon.parse_brief(brief)
    if not claims:
        return 0, "bảng 'Sự thật dùng trong kịch bản' trống"
    resolved = sum(c.resolved for c in claims)
    linked = sum(1 for c in claims if c.resolved or canon.has_link(c.source))
    detail = f"{resolved}/{len(claims)} dòng đã kiểm, {linked}/{len(claims)} dòng có link hoặc đã kiểm"
    if resolved == len(claims):
        return 2, detail
    return (1 if linked * 2 >= len(claims) else 0), detail


def score_commentary(board: scenes.Storyboard) -> tuple[int, str]:
    marks = sum(len(_COMMENT.findall(s.narration.get(config.PRIMARY_LANGUAGE, ""))) for s in board.scenes)
    chapter = next((s.chapter for s in board.scenes if s.chapter and _OPINION_CHAPTER.search(s.chapter)), "")
    detail = f"{marks} cụm bình luận của kênh" + (f"; chương '{chapter}'" if chapter else "; chưa có chương góc nhìn")
    if marks >= 5 and chapter:
        return 2, detail
    return (1 if marks >= 2 or chapter else 0), detail


def score_rights(video_dir: Path) -> tuple[int, str]:
    points, issues = rights.check(video_dir)
    fails = [msg for level, msg in issues if level == rights.FAIL and "chưa có" not in msg]
    return points, "; ".join(fails[:2]) or "mọi tài sản có nguồn và giấy phép đã kiểm"


def build_corpus(videos_dir: Path | None = None) -> dict[str, set]:
    videos = sorted(Path(videos_dir or VIDEOS_DIR).glob("*/scenes.json"))
    return {p.parent.name: shingles(narration(scenes.load(p.parent))) for p in videos}


def nearest(name: str, corpus: dict[str, set]) -> tuple[float, str]:
    """(tỉ lệ 5-gram của video trùng với một video khác, tên video đó), lấy cặp trùng nhiều nhất."""
    mine = corpus.get(name) or set()
    if not mine:
        return 0.0, ""
    return max(((len(mine & other) / len(mine), o) for o, other in corpus.items() if o != name), default=(0.0, ""))


def score_distinct(name: str, corpus: dict[str, set]) -> tuple[int, str]:
    if not corpus.get(name):
        return 0, "không có lời thoại"
    share, other = nearest(name, corpus)
    points = 2 if share < DISTINCT_OK else 1 if share < DISTINCT_WARN else 0
    return points, f"trùng nhiều nhất {share:.1%} cụm 5 từ với {other or 'không video nào'}"


def load_result(video_dir: Path) -> dict | None:
    path = Path(video_dir) / RESULT_NAME
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def verdict(criteria: dict) -> tuple[int, str]:
    points = [c["points"] for c in criteria.values()]
    total = sum(p for p in points if p is not None)
    if any(p is None for p in points):
        return total, PENDING
    if criteria["khong-paraphrase"]["points"] == 0:
        return total, REJECT
    return total, REWRITE if total < GATE else PASS


def evaluate(video_dir: Path, videos_dir: Path | None = None, corpus: dict[str, set] | None = None) -> dict:
    """Chấm lại phần máy, giữ điểm Claude đã ghi trong originality.json. Không ghi file."""
    video_dir = Path(video_dir)
    brief = video_dir / "brief.md"
    board = scenes.load(video_dir)
    corpus = dict(corpus) if corpus is not None else build_corpus(videos_dir)
    corpus[video_dir.name] = shingles(narration(board))
    brief_text = brief.read_text(encoding="utf-8") if brief.exists() else ""
    auto = {
        "cau-hoi": score_question(brief_text),
        "nguon": score_sources(brief) if brief.exists() else (0, "thiếu brief.md"),
        "binh-luan": score_commentary(board),
        "hinh-co-quyen": score_rights(video_dir),
        "khac-nhau": score_distinct(video_dir.name, corpus),
    }
    old = (load_result(video_dir) or {}).get("criteria", {})
    criteria = {}
    for key, (label, by) in CRITERIA.items():
        if key in auto:
            points, evidence = auto[key]
            criteria[key] = {"label": label, "by": "máy", "points": points, "evidence": evidence}
        else:
            prev = old.get(key) or {}
            criteria[key] = {
                "label": label,
                "by": prev.get("by") or "claude",
                "points": prev.get("points"),
                "evidence": prev.get("evidence", ""),
            }
    total, result = verdict(criteria)
    return {
        "video": video_dir.name,
        "updated": dt.date.today().isoformat(),
        "criteria": criteria,
        "total": total,
        "max": MAX_POINTS,
        "verdict": result,
    }


def save(video_dir: Path, result: dict) -> None:
    (Path(video_dir) / RESULT_NAME).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def set_score(video_dir: Path, key: str, points: int, evidence: str, by: str = "claude", **kw) -> dict:
    """Ghi điểm một tiêu chí do Claude (hoặc người) chấm, rồi chấm lại và lưu."""
    if key not in MANUAL:
        raise SystemExit(f"'{key}' do máy chấm. Chỉ chấm tay: {', '.join(MANUAL)}")
    if points not in (0, 1, 2):
        raise SystemExit("điểm phải là 0, 1 hoặc 2")
    if not evidence.strip():
        raise SystemExit("--evidence bắt buộc: dẫn cảnh (sNN) hoặc câu cụ thể trong kịch bản")
    old = load_result(video_dir) or {"criteria": {}}
    old["criteria"][key] = {"by": by, "points": points, "evidence": evidence.strip()}
    save(video_dir, old)
    result = evaluate(video_dir, **kw)
    save(video_dir, result)
    return result


def report(result: dict) -> str:
    lines = []
    for key, c in result["criteria"].items():
        pts = "–" if c["points"] is None else c["points"]
        lines.append(f"  {pts}/2  {key:<17} {c['label']} [{c['by']}]" + (f"\n        {c['evidence']}" if c["evidence"] else ""))
    lines.append(f"\nTổng {result['total']}/{result['max']} · kết luận: {result['verdict'].upper()}")
    return "\n".join(lines)


def _sentences(text: str) -> set[str]:
    out = set()
    for s in _SENTENCE.split(text):
        s = re.sub(r"\s+", " ", s).strip().lower()
        if len(s.split()) >= 4:
            out.add(s)
    return out


def scan(videos_dir: Path | None = None, top: int = 10) -> str:
    videos = sorted(p.parent for p in Path(videos_dir or VIDEOS_DIR).glob("*/scenes.json"))
    boards = {v.name: scenes.load(v) for v in videos}
    corpus = {name: shingles(narration(b)) for name, b in boards.items()}
    pairs = sorted(((*nearest(name, corpus), name) for name in corpus), reverse=True)
    counts = Counter(s for b in boards.values() for s in _sentences(narration(b)))
    grades = Counter(score_distinct(name, corpus)[0] for name in corpus)

    out = [f"{len(videos)} video. Tiêu chí 'khác nhau': {grades[2]} video 2 điểm, {grades[1]} video 1 điểm, {grades[0]} video 0 điểm.", ""]
    out.append(f"Cặp giống nhau nhất (tỉ lệ cụm {NGRAM} từ trùng, đã bỏ câu cửa miệng):")
    out += [f"  {share:5.1%}  {name} ~ {other}" for share, other, name in pairs[:top]]
    out += ["", "Câu lặp ở nhiều video nhất (đã bỏ câu cửa miệng):"]
    repeated = [(n, s) for s, n in counts.most_common(top) if n >= 3]
    out += [f"  {n:>3} video: {s}" for n, s in repeated] or ["  không có câu nào lặp ở từ 3 video trở lên"]
    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("video_dir", type=Path)
    s = sub.add_parser("score")
    s.add_argument("video_dir", type=Path)
    s.add_argument("criterion", choices=MANUAL)
    s.add_argument("points", type=int, choices=(0, 1, 2))
    s.add_argument("--evidence", required=True, help="dẫn chứng: cảnh sNN hoặc câu cụ thể")
    s.add_argument("--by", default="claude", help="ai chấm (mặc định claude)")
    sub.add_parser("scan")
    args = p.parse_args()

    if args.cmd == "scan":
        print(scan())
        return
    if args.cmd == "score":
        result = set_score(args.video_dir, args.criterion, args.points, args.evidence, args.by)
    else:
        result = evaluate(args.video_dir)
        save(args.video_dir, result)
    print(report(result))
    if result["verdict"] != PASS:
        sys.exit(1)


if __name__ == "__main__":
    main()
