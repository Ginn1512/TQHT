"""Test dựng video thật bằng ffmpeg, ở độ phân giải nhỏ cho nhanh."""

import json
import wave

import pytest
from PIL import Image

from tools import assemble, images, media, scenes, thumbnail

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
    assert prompt.startswith("anime illustration. a cliff.")
    assert "a grey cat with a scarf" in prompt
    assert prompt.endswith(images.GUARD)


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
