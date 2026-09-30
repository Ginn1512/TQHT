"""Hook trong .claude/hooks/ và định nghĩa subagent trong .claude/agents/."""

import datetime as dt
import json
import os
import subprocess
import sys

import pytest
import yaml

from tools import config

HOOKS = config.ROOT / ".claude" / "hooks"
AGENTS = config.ROOT / ".claude" / "agents"
SKILLS = config.ROOT / ".claude" / "skills"


def run_hook(script, payload, *args, env=None):
    p = subprocess.run(
        [sys.executable, str(HOOKS / script), *args],
        input=json.dumps(payload).encode("utf-8"),
        capture_output=True,
        env={**os.environ, "CLAUDE_PROJECT_DIR": str(config.ROOT), **(env or {})},
        timeout=120,
    )
    assert p.returncode == 0, p.stderr.decode()
    out = p.stdout.decode().strip()
    return json.loads(out)["hookSpecificOutput"] if out else None


def decision(payload, *args, env=None):
    out = run_hook("guard.py", payload, *args, env=env)
    return out and out["permissionDecision"]


def bash(command):
    return {"tool_name": "Bash", "tool_input": {"command": command}}


@pytest.mark.parametrize(
    "command, expected",
    [
        ("ls -la && python -m tools.plan_check", None),
        ("python -m tools.costs estimate videos/x", None),
        ("python -m tools.images videos/x --only s03", "ask"),
        ("echo $GEMINI_API_KEY", "deny"),
        ("printenv | grep KEY", "deny"),
        ("env", "deny"),
        ("cat .env", "deny"),
        ("git push -u origin claude/planning-strategy-98xh5l", None),
        ("git push -u origin claude/x 2>&1 | tail -2", None),
        ("git push origin claude/x > push.log 2>/dev/null", None),
        ("git push origin main 2>&1", "deny"),
        ("git push --force-with-lease origin claude/x", None),
        ("git push origin main", "deny"),
        ("git push --force origin claude/x", "deny"),
        ("git push origin +claude/x", "deny"),
        ("git add videos/a/brief.md videos/a/rights.csv", None),
        ("git add -f videos/a/render/video.vi.mp4", "deny"),
        ("sed -i 's/- Decision: $/- Decision: publish/' videos/a/audit.md", "ask"),
    ],
)
def test_guard_bash(command, expected):
    assert decision(bash(command)) == expected


def test_paid_api_denied_for_text_agents_and_over_budget(tmp_path):
    assert decision(bash("python -m tools.tts videos/x"), "--deny-paid") == "deny"
    ledger = tmp_path / "costs.md"
    month = dt.date.today().strftime("%Y-%m")
    ledger.write_text(f"| Tháng | Video | Ảnh | Giây | USD |\n|---|---|---|---|---|\n| {month} | x | 1 | 0 | {config.MONTHLY_BUDGET_USD + 1} |\n", encoding="utf-8")
    out = run_hook("guard.py", bash("python -m tools.images videos/x"), env={"KAKU_COSTS_FILE": str(ledger)})
    assert out["permissionDecision"] == "deny" and "trần" in out["permissionDecisionReason"]


def test_publish_decision_needs_human():
    edit = {"tool_name": "Edit", "tool_input": {"file_path": "videos/a/audit.md", "old_string": "- Decision: ", "new_string": "- Decision: publish"}}
    assert decision(edit) == "ask"
    other = {"tool_name": "Write", "tool_input": {"file_path": "videos/a/notes.md", "content": "- Decision: publish"}}
    assert decision(other) is None
    revise = {"tool_name": "Write", "tool_input": {"file_path": "videos/a/audit.md", "content": "- Decision: revise"}}
    assert decision(revise) is None


def test_notion_human_statuses_need_confirmation():
    def notion(status):
        return {"tool_name": "mcp__Notion__notion-update-page", "tool_input": {"properties": {"Trạng thái": status}}}

    assert decision(notion("Duyệt đăng")) == "ask"
    assert decision(notion("Sửa")) == "ask"
    assert decision(notion("Đang kiểm nguồn")) is None
    assert decision({"tool_name": "mcp__Notion__notion-update-page", "tool_input": {"properties": {"Loại sửa": "ảnh"}}}) is None


def test_after_edit_regenerates_prompts_for_scenes_only():
    video = next(p.parent for p in sorted((config.ROOT / "videos").glob("*/scenes.json")))
    rel = video.relative_to(config.ROOT).as_posix()
    out = run_hook("after_edit.py", {"tool_name": "Edit", "tool_input": {"file_path": f"{rel}/scenes.json"}})
    assert "prompt_pack đạt" in out["additionalContext"] and "prompt_check đạt" in out["additionalContext"]
    assert run_hook("after_edit.py", {"tool_name": "Edit", "tool_input": {"file_path": "tools/config.py"}}) is None


def test_settings_register_both_hooks():
    settings = json.loads((config.ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
    pre = {g["matcher"] for g in settings["hooks"]["PreToolUse"]}
    assert {"Bash", "Edit|Write|MultiEdit"} <= pre
    args = [h["args"][0] for e in settings["hooks"].values() for g in e for h in g["hooks"]]
    assert all((config.ROOT / a.replace("${CLAUDE_PROJECT_DIR}/", "")).exists() for a in args)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path.name
    return yaml.safe_load(text.split("---\n", 2)[1])


@pytest.mark.parametrize("path", sorted(AGENTS.glob("*.md")), ids=lambda p: p.stem)
def test_agent_definitions(path):
    meta = frontmatter(path)
    assert meta["name"] == path.stem
    assert meta["description"] and meta["model"] in ("sonnet", "opus", "haiku", "inherit")
    tools = [t.strip() for t in meta["tools"].split(",")]
    for skill in meta.get("skills", []):
        assert (SKILLS / skill / "SKILL.md").exists(), skill
    if path.stem in ("fact-checker", "release-qa", "art-director", "producer"):
        assert "Edit" not in tools and "Write" not in tools
    for groups in (meta.get("hooks") or {}).values():
        for group in groups:
            for hook in group["hooks"]:
                script = hook["args"][0].replace("${CLAUDE_PROJECT_DIR}/", "")
                assert (config.ROOT / script).exists()


def test_six_agents_exist():
    assert {p.stem for p in AGENTS.glob("*.md")} == {"strategist", "writer", "fact-checker", "art-director", "producer", "release-qa"}
