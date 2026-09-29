import json
import re

from tools import app_audio, prompt_pack


def make_video(tmp_path):
    video = tmp_path / "v"
    video.mkdir()
    raw = {
        "title": "Thử",
        "languages": ["vi"],
        "style_prompt": "anime style",
        "mascot_prompt": "a small owl",
        "scenes": [
            {"id": "s01", "chapter": "Mở đầu", "use_mascot": True, "narration": {"vi": "Mở sổ ra nào! Kaku đây."}, "image_prompt": "a cliff"},
            {"id": "s02", "narration": {"vi": "Nhưng luật có ngoại lệ."}, "image_prompt": "a sea"},
            {"id": "s03", "chapter": "Phần hai", "narration": {"vi": "x" * 2100}, "image_prompt": "a book"},
        ],
    }
    (video / "scenes.json").write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    return video


def test_pack_has_three_parts_and_every_scene_and_chunk_once(tmp_path):
    text = prompt_pack.render(make_video(tmp_path))
    assert "## 1. Ảnh mẫu Kaku" in text and "## 2. Ảnh (3 cảnh)" in text and "## 3. Giọng đọc" in text
    for sid in ("s01", "s02", "s03"):
        assert len(re.findall(rf"^### {sid}\b", text, re.M)) == 1
    assert len(re.findall(r"^### c01 ", text, re.M)) == 1 and len(re.findall(r"^### c02 ", text, re.M)) == 1
    assert "<short pause> Nhưng" in text and "[pause] Nhưng" in text
    assert "a small owl" in text and "### Chọn giọng Kaku" in text  # chưa chọn giọng thì hiện 3 bản mô tả
    assert text.count("```text") == text.count("```") // 2


def test_pack_shows_only_chosen_voice(tmp_path, monkeypatch):
    voice = app_audio.load_voice()
    voice["chosen"] = "nu-bac"
    monkeypatch.setattr(app_audio, "load_voice", lambda *a, **k: voice)
    text = prompt_pack.render(make_video(tmp_path))
    assert "Giọng đã chọn: **Nữ · giọng Bắc**" in text and "### Chọn giọng Kaku" not in text
    assert "Hanoi" in text
