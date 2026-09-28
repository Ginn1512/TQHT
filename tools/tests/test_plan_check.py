import json

from tools import plan_check

TABLE = """# Chủ đề

| # | Chủ đề | Dạng | Thư mục |
|---|---|---|---|
| 2 | B | B · Luật chơi | `videos/v2/` |
| 1 | A | A · Giải thích | `videos/v1/` |
| 3 | C | A · Giải thích | — |

Chữ thường ở ngoài bảng.

| Khác | bảng |
|---|---|
| 1 | x |
"""


def test_parse_topics_reads_code_and_folder_sorted():
    plan = plan_check.parse_topics(TABLE)
    assert [(p.number, p.fmt, p.folder) for p in plan] == [(1, "A", "v1"), (2, "B", "v2"), (3, "A", "—")]


def test_consecutive_same_format_is_reported():
    plan = [plan_check.Planned(1, "A", ""), plan_check.Planned(2, "A", "")]
    assert "liền nhau" in plan_check.format_problems(plan)[0]


def test_format_limit_per_window():
    plan = [plan_check.Planned(i, "AB"[i % 2] if i < 5 else "C", "") for i in range(1, 6)]
    plan[4] = plan_check.Planned(5, "A", "")
    # A xuất hiện ở 2, 4, 5 → liền nhau (4, 5) và quá 2 lần trong cửa sổ.
    problems = plan_check.format_problems(plan, window=5, max_per=2)
    assert any("liền nhau" in p for p in problems)
    assert any("dạng A xuất hiện 3 lần" in p for p in problems)


def test_valid_plan_has_no_problems():
    plan = [plan_check.Planned(i, "ABC"[i % 3], "") for i in range(6)]
    assert plan_check.format_problems(plan, window=6, max_per=2) == []


def test_length_problems_flags_short_video(tmp_path):
    folder = tmp_path / "v1"
    folder.mkdir()
    board = {"languages": ["vi"], "scenes": [{"id": "s1", "narration": {"vi": "ngắn"}, "image_prompt": "p"}]}
    (folder / "scenes.json").write_text(json.dumps(board), encoding="utf-8")
    problems, minutes = plan_check.length_problems([plan_check.Planned(1, "A", "v1")], tmp_path)
    assert minutes[1] == 0.0
    assert "ngắn hơn tối thiểu" in problems[0]
