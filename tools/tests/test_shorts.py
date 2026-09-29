from tools import assemble, media, scenes, shorts


def test_suggest_picks_chapter_runs_within_limits():
    raw = {"languages": ["vi"], "scenes": []}
    n = 0
    for c in range(4):
        for k in range(6):
            n += 1
            text = ("Vì sao lại thế? " if k == 0 and c == 2 else "") + "x" * 110
            scene = {"id": f"s{n:02d}", "narration": {"vi": text}, "image_prompt": "p"}
            if k == 0:
                scene["chapter"] = f"Chương {c + 1}"
            raw["scenes"].append(scene)
    board = scenes.parse(raw)
    speech = [9.0] * len(board.scenes)
    picks = shorts.suggest(board, speech, n=2)
    assert len(picks) == 2
    assert all(35 <= p.seconds <= 58 for p in picks)
    assert "Chương 1" not in [p.title for p in picks]  # bỏ chương mở đầu
    assert picks[0].title == "Chương 3" or picks[1].title == "Chương 3"  # cụm mở bằng câu hỏi được ưu tiên


def test_caption_windows_cover_the_scene():
    wins = shorts.caption_windows("Câu một khá ngắn. Câu hai thì dài hơn một chút nữa.", 4.0, 4.4)
    assert wins[0][1] == 0 and wins[-1][2] == 4.4
    assert all(a < b for _, a, b in wins)


def test_make_renders_vertical_short(tmp_path):
    video = assemble.make_demo(tmp_path / "demo", size=(320, 180))
    out = shorts.make(video, "s01", "s03", title="Thử Short", size=(180, 320), fps=10)
    info = media.probe(out)
    assert any("180x320" in v for v in info.video) and info.audio
    assert abs(info.duration_s - (5.4 + 6.4 + 4.9)) < 0.3
