"""Bộ prompt làm tay cho một video: ảnh (Gemini app hay model khác) và giọng (AI Studio, ElevenLabs…).

    python -m tools.prompt_pack videos/<thư-mục>     # ghi videos/<thư-mục>/prompts.vi.md
    python -m tools.prompt_pack --all                # cả 30 video
    python -m tools.prompt_pack --all --check        # chỉ kiểm tra file nào đã cũ so với scenes.json

File được tạo tự động từ scenes.json + channel/giong-kaku.json, không sửa tay. Mở trên điện thoại qua
app GitHub: mỗi prompt nằm trong một khối code có nút sao chép.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools import app_audio, app_images, config, scenes

PACK_FILE = "prompts.vi.md"
VIDEOS_DIR = config.ROOT / "videos"


def _block(text: str) -> str:
    return f"```text\n{text.strip()}\n```"


def _short(text: str, n: int = 110) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def render(video_dir: Path) -> str:
    board = scenes.load(video_dir)
    img = app_images.export(board)
    voice = app_audio.export(board)
    lang = config.PRIMARY_LANGUAGE
    minutes = sum(c["seconds"] for c in voice["chunks"]) / 60
    out = [
        f"# Bộ prompt · {board.title or Path(video_dir).name}",
        "",
        "> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. "
        "**Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.",
        "> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.",
        "",
        f"- {len(board.scenes)} ảnh, {len(voice['chunks'])} đoạn đọc, khoảng {minutes:.1f} phút giọng.",
        "- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).",
        "- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).",
        "",
        "## 1. Ảnh mẫu Kaku (một lần cho cả kênh)",
        "",
        "Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.",
        "",
        _block(img["mascot_reference"]),
        "",
        f"## 2. Ảnh ({len(img['scenes'])} cảnh)",
        "",
        "Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):",
        "",
        _block(img["negative"]),
        "",
    ]
    for item, scene in zip(img["scenes"], board.scenes):
        tags = [item["id"]]
        if item["chapter"]:
            tags.append(item["chapter"])
        if item["mascot"]:
            tags.append("**Kaku** (đính kèm ảnh mẫu)")
        out += [f"### {' · '.join(tags)}", "", f"Lời: {_short(scene.narration[lang])}", "", _block(item["prompt"]), ""]

    out += ["## 3. Giọng đọc", ""]
    chosen = next((v for v in voice["voices"] if v["id"] == voice["chosen"]), None)
    if chosen:
        out += [f"Giọng đã chọn: **{chosen['label']}**. Mô tả để tạo lại khi cần:", "", _block(chosen["design_prompt"]), ""]
    else:
        out += [
            "### Chọn giọng Kaku (làm 1 lần)",
            "",
            "Tạo cả 3 giọng bằng Voice Design (AI Studio hoặc ElevenLabs), cho mỗi giọng đọc đoạn thử bên dưới, "
            "rồi báo mình giọng bạn chọn.",
            "",
        ]
        for v in voice["voices"]:
            out += [f"**{v['label']}**: {v['summary']}", "", _block(v["design_prompt"]), ""]
        out += ["Đoạn đọc thử:", "", _block(voice["sample"]), ""]
    out += ["### Ghi chú đạo diễn (dán 1 lần, ô Style instructions)", "", _block(voice["notes"]), ""]
    for key in ("gemini", "elevenlabs"):
        eng = voice["engines"][key]
        out += [f"- **{eng['label']}:** {eng['how']}"]
    out += ["", "Bản không có thẻ (công cụ khác hoặc tự thu âm): mỗi cảnh một đoạn, xem `script.vi.md`.", ""]
    for c in voice["chunks"]:
        title = " / ".join(c["chapters"]) or "(tiếp)"
        out += [
            f"### {c['id']} · {title}",
            "",
            f"Khoảng {c['seconds']} giây · cảnh {c['scenes'][0]}–{c['scenes'][-1]} · {c['chars']} ký tự",
            "",
            "**Gemini**",
            "",
            _block(c["text"]["gemini"]),
            "",
            "**ElevenLabs**",
            "",
            _block(c["text"]["elevenlabs"]),
            "",
        ]
    return "\n".join(out).rstrip() + "\n"


def video_dirs() -> list[Path]:
    return sorted(p for p in VIDEOS_DIR.iterdir() if (p / "scenes.json").exists())


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path, nargs="?")
    p.add_argument("--all", action="store_true", help="mọi video trong videos/")
    p.add_argument("--check", action="store_true", help="không ghi, chỉ báo file nào đã cũ")
    args = p.parse_args()
    if not args.all and not args.video_dir:
        p.error("cần video_dir hoặc --all")

    stale = []
    for d in video_dirs() if args.all else [args.video_dir]:
        text = render(d)
        path = Path(d) / PACK_FILE
        if path.exists() and path.read_text(encoding="utf-8") == text:
            continue
        stale.append(path)
        if not args.check:
            path.write_text(text, encoding="utf-8")
    verb = "cần tạo lại" if args.check else "đã ghi"
    print(f"{len(stale)} file {verb}." + ("" if not stale else " " + ", ".join(str(s) for s in stale[:5])))
    if args.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
