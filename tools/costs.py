"""Ước tính và ghi chi phí API (ảnh + giọng đọc).

    python -m tools.costs estimate videos/<thư-mục>            # trước khi tạo
    python -m tools.costs estimate videos/<thư-mục> --lang en  # chỉ tính 1 ngôn ngữ
    python -m tools.costs record videos/<thư-mục>              # sau khi xong, ghi vào channel/costs.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from tools import config, scenes, timing

COST_FILE = "cost.json"


def estimate(board: scenes.Storyboard, languages: list[str] | None = None, images: bool = True) -> dict:
    langs = languages or board.languages
    seconds = {
        lang: round(sum(len(s.narration.get(lang, "")) for s in board.scenes) / config.CHARS_PER_SECOND[lang], 1)
        for lang in langs
    }
    n_images = len(board.scenes) if images else 0
    clip_s = sum(s.clip_seconds for s in board.scenes) if images else 0
    usd = (
        n_images * config.PRICE_PER_IMAGE
        + sum(seconds.values()) * config.PRICE_TTS_PER_SECOND
        + clip_s * config.PRICE_VIDEO_PER_SECOND
    )
    return {"images": n_images, "clip_seconds": clip_s, "tts_seconds": seconds, "usd": round(usd, 3)}


def video_seconds(board: scenes.Storyboard) -> float:
    """Độ dài video ước tính từ lời thoại ngôn ngữ chính (giọng + khoảng lặng mỗi cảnh)."""
    lang = config.PRIMARY_LANGUAGE
    speech = sum(len(s.narration.get(lang, "")) for s in board.scenes)
    return speech / config.CHARS_PER_SECOND[lang] + len(board.scenes) * config.SCENE_PADDING_S


def load_usage(video_dir: Path) -> dict:
    path = Path(video_dir) / COST_FILE
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"images": 0, "tts_seconds": {}}


def add_usage(video_dir: Path, images: int = 0, lang: str | None = None, tts_seconds: float = 0.0) -> None:
    """Cộng dồn lượng dùng thật (chỉ tính các lần gọi API mới, không tính cache)."""
    usage = load_usage(video_dir)
    usage["images"] = usage.get("images", 0) + images
    if lang:
        secs = usage.setdefault("tts_seconds", {})
        secs[lang] = round(secs.get(lang, 0.0) + tts_seconds, 2)
    usage["usd"] = usd_of(usage)
    (Path(video_dir) / COST_FILE).write_text(json.dumps(usage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def usd_of(usage: dict) -> float:
    secs = sum(usage.get("tts_seconds", {}).values())
    return round(usage.get("images", 0) * config.PRICE_PER_IMAGE + secs * config.PRICE_TTS_PER_SECOND, 3)


def record(video_dir: Path, ledger: Path = config.CHANNEL_DIR / "costs.md") -> str:
    usage = load_usage(video_dir)
    month = dt.date.today().strftime("%Y-%m")
    secs = sum(usage.get("tts_seconds", {}).values())
    row = f"| {month} | {Path(video_dir).name} | {usage.get('images', 0)} | {secs:.0f} | {usd_of(usage):.2f} |\n"
    with ledger.open("a", encoding="utf-8") as f:
        f.write(row)
    return row


def month_total(ledger: Path = config.CHANNEL_DIR / "costs.md", month: str | None = None) -> float:
    month = month or dt.date.today().strftime("%Y-%m")
    total = 0.0
    for line in ledger.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0] == month:
            total += float(cells[4])
    return round(total, 2)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("estimate")
    e.add_argument("video_dir", type=Path)
    e.add_argument("--lang", action="append", help="chỉ tính các ngôn ngữ này")
    e.add_argument("--no-images", action="store_true", help="bỏ qua ảnh (ví dụ chỉ thêm bản lồng tiếng)")
    r = sub.add_parser("record")
    r.add_argument("video_dir", type=Path)
    args = p.parse_args()

    if args.cmd == "estimate":
        board = scenes.load(args.video_dir)
        est = estimate(board, args.lang, images=not args.no_images)
        spent = month_total()
        print(f"Ảnh: {est['images']} × {config.PRICE_PER_IMAGE} USD")
        if est["clip_seconds"]:
            n = sum(1 for s in board.scenes if s.clip_seconds)
            print(f"Clip Seedance: {n} clip, {est['clip_seconds']} giây × {config.PRICE_VIDEO_PER_SECOND} USD (qua API; làm trên app thì trừ credit)")
        for lang, s in est["tts_seconds"].items():
            print(f"Giọng {lang}: ~{s / 60:.1f} phút")
        print(f"Ước tính: ~{est['usd']:.2f} USD")
        total_s = video_seconds(board)
        print(f"Độ dài video ước tính: ~{total_s / 60:.1f} phút")
        problem = timing.length_problem(total_s)
        if problem:
            print(f"CẢNH BÁO: {problem}. Sửa kịch bản trước khi tạo.")
        print(f"Đã chi tháng này: {spent:.2f} / {config.MONTHLY_BUDGET_USD:.0f} USD")
        if spent + est["usd"] > config.MONTHLY_BUDGET_USD:
            print("CẢNH BÁO: vượt ngân sách tháng nếu chạy tiếp.")
    else:
        print("Đã ghi:", record(args.video_dir).strip())


if __name__ == "__main__":
    main()
