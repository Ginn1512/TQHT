"""Hook PreToolUse của kênh Cú Kaku: chặn (deny) hoặc hỏi lại người dùng (ask) trước thao tác rủi ro.

    python .claude/hooks/guard.py              # khai báo trong .claude/settings.json (phiên trên PC)
    python .claude/hooks/guard.py --deny-paid  # khai báo trong frontmatter của writer, fact-checker (chạy cả trong cloud)

Đọc JSON của Claude Code từ stdin. Không in gì nghĩa là để luồng quyền bình thường quyết định.

| Thao tác                                                        | Quyết định |
|-----------------------------------------------------------------|------------|
| python -m tools.images / tools.tts (gọi API tốn tiền)            | deny nếu tháng đã chi tới trần, ngược lại ask; --deny-paid: luôn deny |
| ghi "Decision: publish" vào audit.md                             | ask: chỉ người dùng được quyết định đăng |
| đặt trạng thái của người trên Notion (Đã chọn, Duyệt đăng, …)     | ask |
| in biến môi trường chứa key (printenv, env, echo $…KEY, cat .env) | deny |
| git push --force, push lên nhánh không phải claude/*             | deny |
| git add file MP4, assets/ hoặc render/                           | deny |

Lỗi bên trong hook không chặn công việc: in ra stderr và thoát mã 1 (lỗi không chặn).
"""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
COSTS_FILE = Path(os.environ.get("KAKU_COSTS_FILE") or ROOT / "channel" / "costs.md")

PAID = re.compile(r"-m\s+tools\.(images|tts)\b")
PUBLISH = re.compile(r"(?mi)^\s*-\s*Decision:\s*`?publish\b")  # dòng trong audit.md
PUBLISH_ANY = re.compile(r"(?i)Decision:\s*`?publish\b")  # trong lệnh shell (sed, echo…)
HUMAN_STATUSES = ("Đã chọn", "Kịch bản đã duyệt", "Duyệt đăng", "Sửa", "Tạm dừng")
SECRET_ECHO = re.compile(r"\b(?:echo|printf|print)\b[^|;&\n]*\$\{?\w*(?:KEY|TOKEN|SECRET|PASSWORD)", re.I)
SECRET_CMDS = re.compile(
    r"\bprintenv\b|(?:^|[;&|(]\s*)env\s*(?:$|[;&|)])|\bset\s*\||\bexport\s+-p\b|\bdeclare\s+-[px]\b"
    r"|\b(?:cat|less|more|head|tail|type)\s+[^|;&\n]*\.env\b"
)
MEDIA_PATH = re.compile(r"\.mp4$|(?:^|/)(?:assets|render)(?:/|$)", re.I)
FORCE_FLAG = re.compile(r"(?<![\w-])(?:-f|--force)(?![\w-])")


def decide(decision: str, reason: str) -> None:
    out = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision, "permissionDecisionReason": reason}}
    print(json.dumps(out))
    sys.exit(0)


REDIRECT = re.compile(r"^(?:\d*|&)(?:>>?|<)(?:&\d+|&-)?$")  # 2>&1, >, >>, 2>, &>, < (tên file ở từ sau)
REDIRECT_JOINED = re.compile(r"^(?:\d*|&)(?:>>?|<)\S+$")  # 2>/dev/null, >out.txt


def strip_redirects(words: list[str]) -> list[str]:
    """Bỏ phần chuyển hướng (2>&1, > file, 2>/dev/null) khỏi danh sách từ của một lệnh."""
    out, skip = [], False
    for w in words:
        if skip:
            skip = False
            continue
        if REDIRECT.match(w):
            skip = not re.search(r"&\d+$|&-$", w)  # "2>&1" không kèm tên file
            continue
        if REDIRECT_JOINED.match(w):
            continue
        out.append(w)
    return out


def segments(command: str) -> list[list[str]]:
    """Tách lệnh shell thành từng lệnh con (theo &&, ||, ;, |, xuống dòng), mỗi lệnh là danh sách từ."""
    out = []
    for part in re.split(r"&&|\|\||[;|\n]", command):
        try:
            words = shlex.split(part)
        except ValueError:
            words = part.split()
        words = strip_redirects(words)
        if words:
            out.append(words)
    return out


def current_branch() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT, capture_output=True, text=True, timeout=10
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def check_push(words: list[str]) -> None:
    args = words[2:]
    if any(FORCE_FLAG.fullmatch(a) for a in args) or any(a in ("--all", "--mirror") for a in args):
        decide("deny", "Không push --force, --all hay --mirror. Chỉ push nhánh claude/* bằng git push -u origin <nhánh>.")
    positional = [a for a in args if not a.startswith("-")]
    refspecs = positional[1:]
    for spec in refspecs:
        if spec.startswith("+"):
            decide("deny", f"Refspec '{spec}' là force push. Không được force push.")
        dst = spec.split(":")[-1].removeprefix("refs/heads/")
        if dst and dst != "HEAD" and not dst.startswith("claude/"):
            decide("deny", f"Chỉ được push lên nhánh claude/*, không phải '{dst}'.")
    if not refspecs:
        branch = current_branch()
        if branch and not branch.startswith("claude/"):
            decide("deny", f"Nhánh hiện tại là '{branch}'. Chỉ được push nhánh claude/*.")


def check_bash(command: str, deny_paid: bool) -> None:
    if SECRET_ECHO.search(command) or SECRET_CMDS.search(command):
        decide("deny", "Lệnh có thể in key hoặc biến môi trường ra màn hình. Key chỉ đọc trong code, không in ra.")
    if PAID.search(command):
        check_paid(deny_paid)
    if "audit.md" in command and PUBLISH_ANY.search(command):
        decide("ask", "Chỉ người dùng được ghi 'Decision: publish' vào audit.md. Người dùng xác nhận đã duyệt video này?")
    for words in segments(command):
        if words[:2] == ["git", "push"]:
            check_push(words)
        if words[:2] == ["git", "add"]:
            media = [w for w in words[2:] if not w.startswith("-") and MEDIA_PATH.search(w.replace("\\", "/"))]
            if media:
                decide("deny", f"Không commit video hay file dựng ({', '.join(media[:3])}). MP4 gửi bằng SendUserFile.")


def check_paid(deny_paid: bool) -> None:
    if deny_paid:
        decide("deny", "Agent này không được gọi API tốn tiền (tools.images, tools.tts). Việc đó thuộc art-director/producer trên PC.")
    spent, budget = None, None
    try:
        sys.path.insert(0, str(ROOT))
        from tools import config, costs

        budget = config.MONTHLY_BUDGET_USD
        spent = costs.month_total(COSTS_FILE)
    except Exception as e:  # noqa: BLE001 — không đọc được sổ thì vẫn hỏi người dùng
        print(f"guard: không đọc được sổ chi phí: {e}", file=sys.stderr)
    if spent is not None and budget is not None and spent >= budget:
        decide("deny", f"Tháng này đã chi {spent:.2f}/{budget:.0f} USD, chạm trần. Không gọi thêm API tốn tiền.")
    so_far = f" Tháng này đã chi {spent:.2f}/{budget:.0f} USD." if spent is not None else ""
    decide("ask", "Lệnh gọi API tốn tiền. Đã báo ước tính (python -m tools.costs estimate) và người dùng đã đồng ý chưa?" + so_far)


def edited_text(tool_input: dict) -> str:
    parts = [tool_input.get(k, "") for k in ("content", "file_text", "new_string")]
    parts += [e.get("new_string", "") for e in tool_input.get("edits") or [] if isinstance(e, dict)]
    return "\n".join(p for p in parts if isinstance(p, str))


def check_notion(tool_input: dict) -> None:
    payload = unicodedata.normalize("NFC", json.dumps(tool_input, ensure_ascii=False))
    if "Trạng thái" not in payload:
        return
    for status in HUMAN_STATUSES:
        if re.search(rf"(?<![\wÀ-ỹ]){re.escape(status)}(?![\wÀ-ỹ])", payload):
            decide("ask", f"Trạng thái '{status}' là quyết định của người. Người dùng đã yêu cầu đặt trạng thái này chưa?")


def main() -> None:
    deny_paid = "--deny-paid" in sys.argv[1:]
    data = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
    tool, tool_input = data.get("tool_name", ""), data.get("tool_input") or {}
    if tool == "Bash":
        check_bash(tool_input.get("command", ""), deny_paid)
    elif tool in ("Edit", "Write", "MultiEdit"):
        path = str(tool_input.get("file_path", "")).replace("\\", "/")
        if path.endswith("audit.md") and PUBLISH.search(edited_text(tool_input)):
            decide("ask", "Chỉ người dùng được ghi 'Decision: publish' vào audit.md. Người dùng xác nhận đã duyệt video này?")
    elif re.search(r"notion", tool, re.I):
        check_notion(tool_input)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001 — hook hỏng không được chặn công việc
        print(f"guard: lỗi hook, bỏ qua: {e}", file=sys.stderr)
        sys.exit(1)
