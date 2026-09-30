"""Hook PostToolUse của kênh Cú Kaku: giữ các file tạo tự động khớp với file gốc.

    python .claude/hooks/after_edit.py   # đọc JSON của Claude Code từ stdin

- Sửa videos/<x>/scenes.json: chạy lại tools.prompt_pack (prompts.vi.md) và tools.prompt_check cho video đó.
- Sửa videos/<x>/brief.md: chạy lại tools.canon build (channel/canon-ledger.md).

Kết quả được báo lại cho Claude qua additionalContext. Hook không bao giờ chặn: lỗi chỉ được báo.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])


def run(*args: str) -> tuple[bool, str]:
    p = subprocess.run([sys.executable, "-m", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=300)
    text = (p.stdout + p.stderr).strip().splitlines()
    return p.returncode == 0, " / ".join(text[-3:])


def video_file(path: str) -> tuple[Path, str] | None:
    """(thư mục video, tên file) nếu path là file nằm ngay trong videos/<x>/."""
    p = Path(path)
    p = (ROOT / p) if not p.is_absolute() else p
    try:
        rel = p.resolve().relative_to((ROOT / "videos").resolve())
    except ValueError:
        return None
    return ((ROOT / "videos" / rel.parts[0]), rel.parts[1]) if len(rel.parts) == 2 else None


def main() -> None:
    data = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
    hit = video_file(str((data.get("tool_input") or {}).get("file_path", "")))
    if not hit:
        return
    video_dir, name = hit
    rel = video_dir.relative_to(ROOT).as_posix()
    notes = []
    if name == "scenes.json":
        ok, out = run("tools.prompt_pack", rel)
        notes.append(f"prompt_pack {'đạt' if ok else 'LỖI'}: {out}")
        if ok:
            ok, out = run("tools.prompt_check", rel)
            notes.append(f"prompt_check {'đạt' if ok else 'LỖI'}: {out}")
    elif name == "brief.md":
        ok, out = run("tools.canon", "build")
        notes.append(f"canon build {'đạt' if ok else 'LỖI'}: {out}")
    if notes:
        context = f"Hook after_edit ({rel}/{name}): " + " | ".join(notes)
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": context}}))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 — hook hỏng không được chặn công việc
        print(f"after_edit: lỗi hook, bỏ qua: {e}", file=sys.stderr)
        sys.exit(1)
