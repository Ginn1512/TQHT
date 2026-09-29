import json
import math
import struct

from tools import app_audio, config, media, scenes

RATE = config.TTS_SAMPLE_RATE


def board(chapter_sizes=(3, 2, 4), chars=300):
    raw, n = [], 0
    for c, size in enumerate(chapter_sizes):
        for k in range(size):
            n += 1
            scene = {"id": f"s{n:02d}", "narration": {"vi": "x" * chars}, "image_prompt": "p"}
            if k == 0:
                scene["chapter"] = f"Chương {c + 1}"
            raw.append(scene)
    return scenes.parse({"languages": ["vi"], "scenes": raw, "mascot_prompt": "owl"})


def test_chunks_group_whole_chapters_under_limit_in_order():
    b = board(chapter_sizes=(3, 2, 4, 2), chars=300)
    chunks = app_audio.chunk_plan(b, max_chars=1500)
    assert [len(c.scenes) for c in chunks] == [5, 4, 2]  # 900+600 | 1200 (+600 thì quá) | 600
    assert [s.id for c in chunks for s in c.scenes] == [s.id for s in b.scenes]
    assert chunks[0].chapters == ["Chương 1", "Chương 2"] and chunks[0].id == "c01"
    assert all(c.chars <= 1500 for c in chunks)


def voice():
    return app_audio.load_voice()


def talk_board():
    return scenes.parse(
        {
            "languages": ["vi"],
            "mascot_prompt": "owl",
            "scenes": [
                {"id": "s01", "chapter": "Mở đầu", "use_mascot": True,
                 "narration": {"vi": "Mở sổ ra nào! Kaku đã đọc hết thư viện. Vì sao lại thua?"}, "image_prompt": "p"},
                {"id": "s02", "narration": {"vi": "Luật rất đơn giản. Nhưng có một ngoại lệ."}, "image_prompt": "p"},
            ],
        }
    )


def test_perform_uses_each_engine_tags():
    v = voice()
    chunk = app_audio.chunk_plan(talk_board())[0]
    gem = app_audio.perform(chunk, v, "gemini")
    eleven = app_audio.perform(chunk, v, "elevenlabs")
    plain = app_audio.perform(chunk, v, "plain")
    assert "<laugh> Kaku" in gem and "<short pause> Luật" in gem and "<short pause> Nhưng" in gem
    assert "[chuckles] Kaku" in eleven and "[curious] Vì sao" in eleven and "[pause] Nhưng" in eleven
    assert "<" not in plain and "[" not in plain
    assert plain.split("\n\n") == [s.narration["vi"] for s in chunk.scenes]


def test_export_has_notes_and_every_engine():
    data = app_audio.export(talk_board(), voice())
    assert set(data["engines"]) == set(app_audio.ENGINES) and len(data["voices"]) == 3
    assert "AUDIO PROFILE" in data["notes"] and data["chunks"][0]["scenes"] == ["s01", "s02"]
    assert set(data["chunks"][0]["text"]) == set(app_audio.ENGINES)


def test_director_notes_add_accent_of_chosen_voice():
    v = voice()
    v["chosen"] = "nam-nam"
    assert "Saigon" in app_audio.director_notes(v)


def test_split_snaps_to_silences_and_trims_them():
    # 3 cảnh 2s | lặng 0.6s | 4s | lặng 0.6s | 2s, cộng lặng 0.3s ở đầu
    sil = [(0.0, 0.3), (2.3, 2.9), (6.9, 7.5)]
    segs = app_audio.split_segments(9.5, [100, 200, 100], sil)
    assert len(segs) == 3
    assert abs(segs[0][0] - 0.24) < 0.01 and abs(segs[0][1] - 2.36) < 0.01
    assert abs(segs[1][0] - 2.84) < 0.01 and abs(segs[1][1] - 6.96) < 0.01
    assert abs(segs[2][1] - 9.5) < 0.01


def test_split_without_silence_is_proportional():
    segs = app_audio.split_segments(8.0, [100, 300], [])
    assert segs == [(0.0, 2.0), (2.0, 8.0)]


def tone_wav(path, pieces):
    """pieces: [(giây, có tiếng?)] → WAV 16-bit mono."""
    frames = bytearray()
    for secs, loud in pieces:
        for i in range(int(secs * RATE)):
            v = int(8000 * math.sin(2 * math.pi * 330 * i / RATE)) if loud else 0
            frames += struct.pack("<h", v)
    media.pcm_to_wav(bytes(frames), path)


def test_import_cuts_chunk_into_scene_files(tmp_path):
    video = tmp_path / "v"
    video.mkdir()
    raw = {"languages": ["vi"], "scenes": [
        {"id": "s01", "chapter": "A", "narration": {"vi": "x" * 26}, "image_prompt": "p"},
        {"id": "s02", "narration": {"vi": "x" * 52}, "image_prompt": "p"},
        {"id": "s03", "narration": {"vi": "x" * 26}, "image_prompt": "p"},
    ]}
    (video / "scenes.json").write_text(json.dumps(raw), encoding="utf-8")
    src = tmp_path / "in"
    src.mkdir()
    tone_wav(src / "c01.wav", [(2, True), (0.6, False), (4, True), (0.6, False), (2, True)])
    done, missing = app_audio.import_audio(video, src)
    assert done == ["c01"] and missing == []
    lengths = [media.wav_duration(video / "assets" / "audio" / "vi" / f"s0{i}.wav") for i in (1, 2, 3)]
    assert abs(lengths[0] - 2.06) < 0.15 and abs(lengths[1] - 4.12) < 0.15 and abs(lengths[2] - 2.06) < 0.15
    usage = json.loads((video / "cost.json").read_text())
    assert usage["tts_app_seconds"]["vi"] > 9 and usage["usd"] == 0
