"""Cảnh "đinh" làm bằng clip Seedance: kiểm tra dữ liệu, chi phí, prompt và dựng video."""

import json

import pytest

from tools import assemble, config, costs, media, scenes, seedance

BASE = {
    "style_prompt": "anime illustration",
    "mascot_prompt": "a small owl with glasses",
    "scenes": [
        {"id": "s01", "narration": {"vi": "a" * 26}, "image_prompt": "a cliff"},
        {"id": "s02", "narration": {"vi": "b" * 26}, "image_prompt": "a storm", "video_prompt": "slow push-in",
         "clip_seconds": 6, "use_mascot": True},
    ],
}


def test_video_prompt_defaults_to_5_seconds_and_validates_range():
    data = json.loads(json.dumps(BASE))
    del data["scenes"][1]["clip_seconds"]
    assert scenes.parse(data).scenes[1].clip_seconds == 5
    data["scenes"][1]["clip_seconds"] = 30
    with pytest.raises(scenes.ScenesError, match="clip_seconds"):
        scenes.parse(data)


def test_estimate_includes_clip_seconds():
    est = costs.estimate(scenes.parse(BASE))
    assert est["clip_seconds"] == 6
    assert est["usd"] >= 6 * config.PRICE_VIDEO_PER_SECOND
    assert costs.estimate(scenes.parse(BASE), images=False)["clip_seconds"] == 0


def test_prompt_keeps_style_mascot_motion_and_guard():
    board = scenes.parse(BASE)
    prompt = seedance.build_prompt(board, board.scenes[1])
    assert prompt.startswith("6-second cinematic anime shot")
    assert "a small owl with glasses" in prompt and "slow push-in" in prompt
    assert prompt.endswith(seedance.GUARD)


def test_export_lists_only_hero_scenes(tmp_path):
    (tmp_path / "scenes.json").write_text(json.dumps(BASE), encoding="utf-8")
    text = seedance.export(tmp_path).read_text(encoding="utf-8")
    assert "## s02" in text and "## s01" not in text


def test_assemble_uses_clip_when_present(tmp_path):
    size, fps = (320, 180), 10
    video_dir = assemble.make_demo(tmp_path / "demo", size=size)
    clip = video_dir / "assets" / "clips" / "s02.mp4"
    clip.parent.mkdir(parents=True)
    media.run_ffmpeg(["-f", "lavfi", "-i", "testsrc=size=640x360:rate=24:duration=2", "-pix_fmt", "yuv420p", str(clip)])
    (video_dir / "assets" / "images" / "s02.png").unlink()  # có clip thì không cần ảnh

    final = assemble.run(video_dir, size=size, fps=fps)
    assert media.probe(final).duration_s == pytest.approx(5.4 + 6.4 + 4.9, abs=0.15)
