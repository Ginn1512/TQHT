"""Test dựng video thật bằng ffmpeg, ở độ phân giải nhỏ cho nhanh."""

import json
import shutil
import wave

import pytest
from PIL import Image

from tools import assemble, config, images, media, scenes, thumbnail

SMALL = (320, 180)
FPS = 10


def test_frame_counts_do_not_drift():
    durations = [1.37] * 50
    counts = assemble.frame_counts(durations, fps=30)
    assert sum(counts) == round(sum(durations) * 30)


def test_build_prompt_includes_style_mascot_and_guard():
    board = scenes.parse(
        {
            "style_prompt": "anime illustration",
            "mascot_prompt": "a grey cat with a scarf",
            "scenes": [{"id": "a", "narration": {"vi": "x"}, "image_prompt": "a cliff", "use_mascot": True}],
        }
    )
    prompt = images.build_prompt(board, board.scenes[0])
    assert prompt.startswith(f"{images.ASPECT_PREFIX} a cliff.")
    assert "a grey cat with a scarf" in prompt and "anime illustration." in prompt
    assert prompt.endswith(images.GUARD + ".")


def test_demo_renders_video_audio_tracks_and_subtitles(tmp_path):
    video_dir = assemble.make_demo(tmp_path / "demo", size=SMALL)
    final = assemble.run(video_dir, size=SMALL, fps=FPS)

    info = media.probe(final)
    expected = 5.4 + 6.4 + 4.9
    assert info.duration_s == pytest.approx(expected, abs=0.15)
    assert "320x180" in info.video[0] and "h264" in info.video[0]
    assert "aac" in info.audio[0]

    render = video_dir / "render"
    en = media.probe(render / "audio.en.m4a")
    assert en.duration_s == pytest.approx(expected, abs=0.15)
    assert json.loads((render / "report.json").read_text())["languages"] == {"vi": "ok", "en": "ok"}
    assert (render / "chapters.txt").read_text().splitlines()[0] == "0:00 Mở đầu"
    assert "Scene two has on-screen text." in (render / "subs.en.srt").read_text()
    assert not (render / "tmp").exists()


def test_too_long_translation_is_reported(tmp_path):
    video_dir = assemble.make_demo(tmp_path / "demo", size=SMALL)
    long_wav = video_dir / "assets" / "audio" / "en" / "s03.wav"
    with wave.open(str(long_wav), "wb") as w:  # 8s cho cảnh chỉ dài 4.9s
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(24_000)
        w.writeframes(b"\x00\x00" * 24_000 * 8)

    assemble.run(video_dir, size=SMALL, fps=FPS)
    report = json.loads((video_dir / "render" / "report.json").read_text())
    assert "s03" in report["languages"]["en"]
    assert not (video_dir / "render" / "audio.en.m4a").exists()


def test_thumbnail_is_1280x720(tmp_path):
    bg = tmp_path / "bg.png"
    Image.new("RGB", (800, 600), (30, 60, 90)).save(bg)
    out = thumbnail.compose(bg, "Bí mật sức mạnh thật sự của Hashira", tmp_path / "thumb.png")
    assert Image.open(out).size == (1280, 720)


def test_draft_speech_seconds_follow_reading_speed():
    board = scenes.parse(
        {"languages": ["vi"], "scenes": [{"id": "s1", "narration": {"vi": "a" * 130}, "image_prompt": "p"}]}
    )
    assert assemble.draft_speech_seconds(board) == [round(130 / config.CHARS_PER_SECOND["vi"], 3)]


def test_draft_renders_without_any_audio_files(tmp_path):
    video_dir = assemble.make_demo(tmp_path / "demo", size=SMALL)
    shutil.rmtree(video_dir / "assets" / "audio")
    final = assemble.run(video_dir, size=SMALL, fps=FPS, draft=True, crf=assemble.DRAFT_CRF)
    assert final.name == "draft.vi.mp4"
    board = scenes.load(video_dir)
    expected = sum(assemble.draft_speech_seconds(board)) + len(board.scenes) * config.SCENE_PADDING_S
    assert abs(media.probe(final).duration_s - expected) < 0.3
    report = json.loads((final.parent / "report.json").read_text(encoding="utf-8"))
    assert "draft" in report and "en" not in report["languages"]
    assert (final.parent / "subs.vi.srt").exists()
