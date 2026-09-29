import json

from tools import scenes, xuong


def board():
    return scenes.parse(
        {
            "title": "Thử",
            "languages": ["vi"],
            "style_prompt": "anime style",
            "mascot_prompt": "a small owl",
            "scenes": [
                {"id": "s01", "chapter": "Mở đầu", "narration": {"vi": "a </script> b"}, "image_prompt": "a cliff", "use_mascot": True},
                {"id": "s02", "narration": {"vi": "Nhưng c"}, "image_prompt": "a sea"},
            ],
        }
    )


def test_page_embeds_label_images_and_voice_data():
    html = xuong.build_page(board(), "video 9")
    assert "<title>Xưởng Kaku video 9</title>" in html and "__DATA__" not in html and "__LABEL__" not in html
    raw = html.split('<script type="application/json" id="data">', 1)[1].split("</script>", 1)[0]
    data = json.loads(raw)
    assert [s["id"] for s in data["images"]["scenes"]] == ["s01", "s02"]
    assert data["images"]["scenes"][0]["say"] == "a </script> b"
    chunk = data["voice"]["chunks"][0]
    assert chunk["scenes"] == ["s01", "s02"] and set(chunk["text"]) == {"gemini", "elevenlabs", "plain"}
    assert data["voice"]["notes"].startswith("AUDIO PROFILE")
