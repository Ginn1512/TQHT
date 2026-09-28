"""Kiểm tra tts/images với client Gemini giả (không gọi mạng, không cần key)."""

import io
import json
from types import SimpleNamespace

import pytest
from PIL import Image

from tools import config, gemini, images, media, tts


class FakeModels:
    def __init__(self, blob):
        self.blob = blob
        self.calls = 0

    def generate_content(self, model, contents, config):
        self.calls += 1
        part = SimpleNamespace(inline_data=self.blob)
        return SimpleNamespace(candidates=[SimpleNamespace(content=SimpleNamespace(parts=[part]))])


@pytest.fixture
def fake_client(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "CACHE_DIR", tmp_path / "cache")

    def install(blob):
        models = FakeModels(blob)
        monkeypatch.setattr(gemini, "client", lambda: SimpleNamespace(models=models))
        return models

    return install


def test_tts_writes_wav_uses_rate_and_caches(fake_client, tmp_path):
    one_second_16k = b"\x00\x00" * 16_000
    models = fake_client(SimpleNamespace(data=one_second_16k, mime_type="audio/L16;codec=pcm;rate=16000"))

    wav, fresh = tts.synthesize("Xin chào", "vi")
    assert fresh and media.wav_duration(wav) == pytest.approx(1.0)
    _, fresh_again = tts.synthesize("Xin chào", "vi")
    assert not fresh_again and models.calls == 1


def test_tts_run_records_usage(fake_client, tmp_path):
    fake_client(SimpleNamespace(data=b"\x00\x00" * 24_000 * 2, mime_type="audio/L16;rate=24000"))
    video = tmp_path / "video"
    video.mkdir()
    (video / "scenes.json").write_text(
        json.dumps({"scenes": [{"id": "s01", "narration": {"vi": "Một"}, "image_prompt": "p"}]}), encoding="utf-8"
    )
    tts.run(video, "vi")
    assert (video / "assets" / "audio" / "vi" / "s01.wav").exists()
    assert json.loads((video / "cost.json").read_text())["tts_seconds"]["vi"] == pytest.approx(2.0)


def test_images_resized_to_1080p_and_cached(fake_client):
    buf = io.BytesIO()
    Image.new("RGB", (1344, 768), (200, 50, 50)).save(buf, format="PNG")
    models = fake_client(SimpleNamespace(data=buf.getvalue(), mime_type="image/png"))

    png, fresh = images.generate("a cliff")
    assert fresh and Image.open(png).size == (config.WIDTH, config.HEIGHT)
    images.generate("a cliff")
    assert models.calls == 1


def test_empty_response_raises(fake_client):
    fake_client(SimpleNamespace(data=b"", mime_type="image/png"))
    with pytest.raises(RuntimeError, match="không trả về ảnh"):
        images.generate("blocked prompt")
