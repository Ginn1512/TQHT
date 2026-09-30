"""Sổ quyền tài sản: mọi ảnh, clip, giọng, font và nhạc trong video phải có nguồn và giấy phép.

    python -m tools.rights build videos/<thư-mục>     # tạo / cập nhật videos/<x>/rights.csv
    python -m tools.rights build --all                # mọi video
    python -m tools.rights check videos/<thư-mục>     # dừng (mã 1) nếu còn dòng UNKNOWN hay mục chưa kiểm
    python -m tools.rights registry                   # trạng thái các mục trong channel/rights-registry.json

rights.csv theo cột của tài liệu "Policy Safe": asset_id, filename, type, creator,
source_url, license, permission_proof, attribution_required, expiry, notes.

- Dòng do máy tạo có permission_proof dạng "registry:<khóa>". Giấy phép và trạng thái kiểm
  nằm trong channel/rights-registry.json, nên kiểm điều khoản một lần là dùng cho mọi video.
- Dòng người tự thêm (ví dụ nhạc nền), hoặc dòng có permission_proof không bắt đầu bằng
  "registry:", được giữ nguyên khi chạy lại build. Ô expiry và notes người đã điền cũng được giữ.
- Công cụ ảnh và giọng đọc lấy từ cost.json. Chưa làm thì ghi theo kế hoạch sản xuất
  (ảnh Gemini API, giọng VoxCPM2) và ghi chú "dự kiến".
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import sys
from collections import defaultdict
from pathlib import Path

from tools import config, costs, scenes, voicestudio

VIDEOS_DIR = config.ROOT / "videos"
REGISTRY = config.CHANNEL_DIR / "rights-registry.json"
LEDGER_NAME = "rights.csv"
COLUMNS = [
    "asset_id",
    "filename",
    "type",
    "creator",
    "source_url",
    "license",
    "permission_proof",
    "attribution_required",
    "expiry",
    "notes",
]
PROOF_PREFIX = "registry:"
UNKNOWN = "UNKNOWN"
CHECKED = "da-kiem"
AUTO_NOTE = "Tự ghi:"  # ghi chú do máy viết; ghi chú khác là của người và được giữ
FAIL, WARN = "LỖI", "LƯU Ý"
FONT_KEY = "font-be-vietnam-pro"
FONT_FILE = "assets/fonts/BeVietnamPro-ExtraBold.ttf"
PLANNED_IMAGE = "gemini-image-api"
PLANNED_VOICE = "voxcpm2"
APP_VOICE = {"gemini": "ai-studio-tts", "elevenlabs": "elevenlabs"}
CLIP_TOOL = "seedance-dreamina"


def load_registry(path: Path | None = None) -> dict[str, dict]:
    return json.loads(Path(path or REGISTRY).read_text(encoding="utf-8"))["items"]


def proof_keys(proof: str) -> list[str]:
    """Các khóa sổ trong ô permission_proof, ví dụ "registry:a; registry:b" -> ["a", "b"]."""
    return [p.strip()[len(PROOF_PREFIX):] for p in proof.split(";") if p.strip().startswith(PROOF_PREFIX)]


def _auto_row(asset_id: str, filename: str, type_: str, keys: list[str], registry: dict, note: str = "") -> dict:
    items = [registry.get(k) for k in keys]
    row = dict.fromkeys(COLUMNS, "")
    row.update(asset_id=asset_id, filename=filename, type=type_)
    row["permission_proof"] = "; ".join(PROOF_PREFIX + k for k in keys)
    if any(i is None for i in items):
        row.update(creator=UNKNOWN, source_url=UNKNOWN, license=UNKNOWN, attribution_required=UNKNOWN)
    else:

        def join(field: str, sep: str = "; ") -> str:
            return sep.join(dict.fromkeys(i.get(field, "") for i in items))

        row.update(
            creator=join("creator"),
            source_url=join("source_url", " "),
            license=join("license"),
            attribution_required=join("attribution_required", "/"),
        )
    if note:
        row["notes"] = f"{AUTO_NOTE} {note}"
    return row


def image_tools(usage: dict) -> tuple[list[str], str]:
    keys = []
    if usage.get("images"):
        keys.append("gemini-image-api")
    if usage.get("images_app"):
        keys.append("gemini-image-app")
    if keys:
        note = "video dùng cả ảnh API lẫn ảnh làm tay; từng cảnh là một trong hai" if len(keys) > 1 else ""
        return keys, note
    return [PLANNED_IMAGE], "dự kiến theo kế hoạch (ảnh qua API); chạy lại build sau khi có ảnh"


def voice_tool(usage: dict, lang: str) -> tuple[str, str]:
    if (usage.get("tts_local_seconds") or {}).get(lang):
        engine = voicestudio.settings()["engine"]
        return engine, f"VoiceStudio, engine {engine}"
    if (usage.get("tts_seconds") or {}).get(lang):
        return "gemini-tts-api", ""
    if (usage.get("tts_app_seconds") or {}).get(lang):
        engine = usage.get("tts_app_engine")
        if engine in APP_VOICE:
            return APP_VOICE[engine], ""
        return UNKNOWN, "giọng làm tay nhưng không rõ công cụ; nhập lại bằng app_audio import --engine gemini|elevenlabs"
    return PLANNED_VOICE, "dự kiến theo kế hoạch (VoxCPM2); chạy lại build sau khi có giọng"


def planned_rows(video_dir: Path, registry: dict | None = None) -> list[dict]:
    """Các dòng máy tạo được từ scenes.json, cost.json và các file trong assets/."""
    video_dir = Path(video_dir)
    registry = registry if registry is not None else load_registry()
    board = scenes.load(video_dir)
    usage = costs.load_usage(video_dir)
    img_keys, img_note = image_tools(usage)
    rows = [
        _auto_row(s.id, f"assets/images/{s.id}.png", "image", img_keys, registry, img_note)
        for s in board.scenes
    ]
    for s in board.scenes:
        if (video_dir / "assets" / "clips" / f"{s.id}.mp4").exists():
            rows.append(_auto_row(f"clip-{s.id}", f"assets/clips/{s.id}.mp4", "clip", [CLIP_TOOL], registry))
    for lang in board.languages:
        key, note = voice_tool(usage, lang)
        rows.append(_auto_row(f"voice-{lang}", f"assets/audio/{lang}/*.wav", "voice", [key], registry, note))
    rows.append(_auto_row("font", FONT_FILE, "font", [FONT_KEY], registry))
    rows.append(_auto_row("thumbnail", "render/thumbnail.png", "thumbnail", img_keys + [FONT_KEY], registry,
                          "ảnh nền lấy từ một cảnh của video, chữ bằng font của kênh"))
    return rows


def read_ledger(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return [{c: (r.get(c) or "").strip() for c in COLUMNS} for r in csv.DictReader(f)]


def to_csv(rows: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def _is_manual(row: dict) -> bool:
    return not row["permission_proof"].startswith(PROOF_PREFIX)


def merge(generated: list[dict], existing: list[dict]) -> list[dict]:
    """Ghép dòng máy tạo với sổ cũ: giữ dòng của người và các ô expiry, notes người đã điền."""
    old = {r["asset_id"]: r for r in existing}
    out = []
    for row in generated:
        prev = old.get(row["asset_id"])
        if prev and _is_manual(prev):
            out.append(prev)
            continue
        row = dict(row)
        if prev:
            if prev["expiry"]:
                row["expiry"] = prev["expiry"]
            if prev["notes"] and not prev["notes"].startswith(AUTO_NOTE):
                row["notes"] = prev["notes"]
        out.append(row)
    ids = {r["asset_id"] for r in generated}
    out += [r for r in existing if r["asset_id"] not in ids and _is_manual(r)]
    return out


def build(video_dir: Path, registry: dict | None = None, write: bool = True) -> list[dict]:
    path = Path(video_dir) / LEDGER_NAME
    rows = merge(planned_rows(video_dir, registry), read_ledger(path))
    if write:
        path.write_text(to_csv(rows), encoding="utf-8")
    return rows


def audit(rows: list[dict], registry: dict, today: dt.date | None = None) -> tuple[int, list[tuple[str, str]]]:
    """Chấm sổ quyền: (điểm 0–2 cho tiêu chí "hình có quyền", danh sách (mức, lời)).

    2: mọi dòng đủ nguồn và giấy phép, mọi mục trong sổ đã kiểm.
    1: còn mục trong sổ ở mức can-kiem.
    0: có ô UNKNOWN hoặc trống, mục bị cấm, mục không có trong sổ, hoặc giấy phép hết hạn.
    """
    today = today or dt.date.today()
    issues: list[tuple[str, str]] = []
    worst = 2
    if not rows:
        return 0, [(FAIL, "sổ quyền trống")]
    missing = [r["asset_id"] for r in rows if any(r[c] in ("", UNKNOWN) for c in ("creator", "source_url", "license"))]
    if missing:
        worst = 0
        issues.append((FAIL, f"{len(missing)} dòng thiếu nguồn hoặc giấy phép (UNKNOWN): {', '.join(missing[:6])}"))
    by_key: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        for k in proof_keys(r["permission_proof"]):
            by_key[k].append(r["asset_id"])
    for key, ids in by_key.items():
        item = registry.get(key)
        status = item.get("status") if item else None
        if status == CHECKED:
            continue
        if status == "can-kiem":
            worst = min(worst, 1)
            what = f"{item['label']} ({key}): chưa kiểm điều khoản"
        elif status == "cam":
            worst = 0
            what = f"{item['label']} ({key}): bị cấm cho kênh kiếm tiền ({item.get('license', '')})"
        elif item is None and key != UNKNOWN:
            worst = 0
            what = f"'{key}' không có trong channel/rights-registry.json"
        elif item is None:
            continue  # dòng UNKNOWN đã báo ở trên
        else:
            worst = 0
            what = f"{item['label']} ({key}): trạng thái {status}"
        issues.append((FAIL, f"{len(ids)} dòng dùng {what}"))
    for r in rows:
        try:
            expired = r["expiry"] and dt.date.fromisoformat(r["expiry"]) < today
        except ValueError:
            expired = False
            issues.append((WARN, f"{r['asset_id']}: ô expiry '{r['expiry']}' không phải ngày YYYY-MM-DD"))
        if expired:
            worst = 0
            issues.append((FAIL, f"{r['asset_id']}: giấy phép hết hạn {r['expiry']}"))
    credit = [r["asset_id"] for r in rows if r["attribution_required"].lower() in ("yes", "có")]
    if credit:
        issues.append((WARN, f"{len(credit)} dòng bắt buộc ghi công, nhớ ghi trong mô tả: {', '.join(credit[:6])}"))
    return worst, issues


def check(video_dir: Path, registry: dict | None = None, today: dt.date | None = None) -> tuple[int, list[tuple[str, str]]]:
    """Kiểm rights.csv của một video. Chưa có file thì chấm theo dòng dự kiến và báo LỖI."""
    registry = registry if registry is not None else load_registry()
    path = Path(video_dir) / LEDGER_NAME
    if not path.exists():
        points, issues = audit(build(video_dir, registry, write=False), registry, today)
        return points, [(FAIL, f"chưa có {LEDGER_NAME}; chạy python -m tools.rights build {video_dir}")] + issues
    rows = read_ledger(path)
    points, issues = audit(rows, registry, today)
    if to_csv(rows) != to_csv(build(video_dir, registry, write=False)):
        issues.insert(0, (WARN, f"{LEDGER_NAME} chưa khớp scenes.json / cost.json; chạy lại python -m tools.rights build"))
    return points, issues


def all_videos(videos_dir: Path | None = None) -> list[Path]:
    return sorted(p.parent for p in Path(videos_dir or VIDEOS_DIR).glob("*/scenes.json"))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("video_dir", type=Path, nargs="?")
    b.add_argument("--all", action="store_true", help="mọi video có scenes.json")
    c = sub.add_parser("check")
    c.add_argument("video_dir", type=Path)
    sub.add_parser("registry")
    args = p.parse_args()

    if args.cmd == "registry":
        for key, item in load_registry().items():
            print(f"{item['status']:<9} {key:<22} {item['license'] or '(chưa ghi)'}  {item.get('checked') or ''}")
        return
    if args.cmd == "build":
        targets = all_videos() if args.all else [args.video_dir] if args.video_dir else []
        if not targets:
            p.error("cần video_dir hoặc --all")
        for v in targets:
            rows = build(v)
            print(f"{v.name}: {len(rows)} dòng")
        return
    points, issues = check(args.video_dir)
    for level, msg in issues:
        print(f"[{level}] {msg}")
    if any(level == FAIL for level, _ in issues):
        print(f"\nCHƯA ĐƯỢC ĐĂNG (điểm 'hình có quyền': {points}/2).")
        sys.exit(1)
    print(f"Mọi tài sản đã có nguồn và giấy phép đã kiểm (điểm {points}/2).")


if __name__ == "__main__":
    main()
