import copy

import pytest

from tools import scenes

VALID = {
    "title": "Thử",
    "languages": ["vi", "en"],
    "style_prompt": "anime illustration",
    "mascot_prompt": "a grey cat",
    "scenes": [
        {"id": "s01", "narration": {"vi": "Xin chào", "en": "Hello"}, "image_prompt": "a cliff"},
        {
            "id": "s02",
            "chapter": "Phần 1",
            "narration": {"vi": "Tiếp", "en": "Next"},
            "image_prompt": "a sword",
            "on_screen_text": "Chữ",
            "use_mascot": True,
        },
    ],
}


def test_parse_valid_storyboard():
    board = scenes.parse(VALID)
    assert [s.id for s in board.scenes] == ["s01", "s02"]
    assert board.scenes[1].use_mascot and board.scenes[1].chapter == "Phần 1"
    assert board.languages == ["vi", "en"]


def test_defaults_to_primary_language():
    data = {"scenes": [{"id": "a", "narration": {"vi": "x"}, "image_prompt": "y"}]}
    assert scenes.parse(data).languages == ["vi"]


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda d: d["scenes"][0]["narration"].pop("en"), "thiếu lời thoại 'en'"),
        (lambda d: d["scenes"][1].update(id="s01"), "id bị trùng"),
        (lambda d: d["scenes"][0].update(id="Cảnh 1"), "id chỉ được dùng"),
        (lambda d: d["languages"].append("fr"), "ngôn ngữ không hỗ trợ: fr"),
        (lambda d: d.update(languages=["en"]), "thiếu ngôn ngữ chính"),
        (lambda d: d.update(mascot_prompt=""), "thiếu mascot_prompt"),
        (lambda d: d["scenes"][0].update(image_prompt=" "), "thiếu image_prompt"),
        (lambda d: d.update(scenes=[]), "không có cảnh nào"),
    ],
)
def test_parse_reports_errors(mutate, message):
    data = copy.deepcopy(VALID)
    mutate(data)
    with pytest.raises(scenes.ScenesError, match=message):
        scenes.parse(data)
