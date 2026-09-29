import io
import json
import threading
import wave
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from tools import config, media, voicestudio


def wav_bytes(seconds: float, rate: int = 48_000) -> bytes:
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(b"\x00\x00" * int(seconds * rate))
    return buf.getvalue()


class FakeStudio:
    """Máy chủ giả, trả lời như API tương thích OpenAI của VoiceStudio."""

    def __init__(self):
        self.requests: list[dict] = []
        self.fail_next: list[int] = []  # mã lỗi trả cho các lần gọi /speech tiếp theo
        studio = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _json(self, code, obj):
                data = json.dumps(obj).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def do_GET(self):
                if self.path == "/health":
                    self._json(200, {"status": "ok", "device": "cuda:0"})
                elif self.path == "/v1/models":
                    self._json(200, {"object": "list", "data": [
                        {"id": "tts-1", "voicestudio": {"kind": "tts", "alias_for_active_engine": True}},
                        {"id": "omnivoice", "voicestudio": {"kind": "tts"}},
                        {"id": "voxcpm2", "voicestudio": {"kind": "tts"}},
                    ]})
                elif self.path == "/v1/audio/voices":
                    self._json(200, {"voices": [
                        {"voice_id": "alloy", "type": "openai_alias"},
                        {"voice_id": "kaku-123", "name": "Kaku", "type": "profile", "language": "vi"},
                    ]})
                else:
                    self._json(404, {"error": {"message": "not found"}})

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                studio.requests.append(body)
                if studio.fail_next:
                    code = studio.fail_next.pop(0)
                    self._json(code, {"error": {"message": f"lỗi giả {code}", "type": "server_error"}})
                    return
                data = wav_bytes(0.05 * len(body["input"]))
                self.send_response(200)
                self.send_header("Content-Type", "audio/wav")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


@pytest.fixture
def studio(monkeypatch, tmp_path):
    s = FakeStudio()
    monkeypatch.setenv("VOICESTUDIO_URL", s.url)
    monkeypatch.setattr(config, "CACHE_DIR", tmp_path / "cache")
    yield s
    s.close()


def video(tmp_path, n=3):
    d = tmp_path / "videos" / "v"
    d.mkdir(parents=True)
    raw = {
        "languages": ["vi"],
        "mascot_prompt": "owl",
        "scenes": [{"id": f"s{i:02d}", "narration": {"vi": f"Câu thứ {i} của Kaku."}, "image_prompt": "p"} for i in range(1, n + 1)],
    }
    (d / "scenes.json").write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    return d


def cfg(**kw):
    return voicestudio.settings({"voicestudio": {"voice_id": "kaku-123", "_ghi_chu": "x", **kw}})


def test_settings_defaults_and_overrides():
    s = voicestudio.settings({})
    assert s["engine"] == "voxcpm2" and s["voice_id"] is None and s["language"] == "vi"
    s = cfg(speed=1.1)
    assert s["voice_id"] == "kaku-123" and s["speed"] == 1.1 and "_ghi_chu" not in s


def test_repo_voice_file_has_voicestudio_section():
    s = voicestudio.settings()
    assert s["engine"] == "voxcpm2"


def test_license_guard():
    assert "Apache" in voicestudio.check_license("voxcpm2")
    for bad in ("omnivoice", "tts-1"):
        with pytest.raises(voicestudio.StudioError):
            voicestudio.check_license(bad)
    with pytest.raises(voicestudio.StudioError):
        voicestudio.check_license("cosyvoice")
    assert voicestudio.check_license("cosyvoice", license_ok=True)


def test_run_writes_24k_mono_wav_per_scene_and_records_seconds(studio, tmp_path):
    d = video(tmp_path)
    made = voicestudio.run(d, cfg())
    assert made == ["s01", "s02", "s03"]
    body = studio.requests[0]
    assert body["model"] == "voxcpm2" and body["voice"] == "kaku-123"
    assert body["language"] == "vi" and body["response_format"] == "wav" and body["input"] == "Câu thứ 1 của Kaku."
    wav = d / "assets" / "audio" / "vi" / "s01.wav"
    with wave.open(str(wav)) as w:
        assert w.getframerate() == config.TTS_SAMPLE_RATE and w.getnchannels() == 1 and w.getsampwidth() == 2
    assert media.wav_duration(wav) == pytest.approx(0.05 * len("Câu thứ 1 của Kaku."), abs=0.02)
    usage = json.loads((d / "cost.json").read_text(encoding="utf-8"))
    assert usage["tts_local_seconds"]["vi"] > 0 and usage["usd"] == 0


def test_run_skips_existing_uses_only_and_cache(studio, tmp_path):
    d = video(tmp_path)
    voicestudio.run(d, cfg(), only={"s02"})
    assert [r["input"] for r in studio.requests] == ["Câu thứ 2 của Kaku."]
    voicestudio.run(d, cfg())  # s02 đã có: chỉ làm s01, s03
    assert len(studio.requests) == 3
    voicestudio.run(d, cfg(), force=True)  # làm lại từ cache, không gọi app
    assert len(studio.requests) == 3


def test_run_needs_voice_profile(studio, tmp_path):
    with pytest.raises(voicestudio.StudioError, match="hồ sơ giọng"):
        voicestudio.run(video(tmp_path), voicestudio.settings({}))


def test_speech_retries_server_errors_but_not_client_errors(studio):
    studio.fail_next = [500]
    assert voicestudio.speech("xin chào", cfg(), wait=0)[:4] == b"RIFF"
    assert len(studio.requests) == 2
    studio.fail_next = [400]
    with pytest.raises(voicestudio.StudioError, match="lỗi giả 400"):
        voicestudio.speech("xin chào", cfg(), wait=0)


def test_offline_gives_clear_message(monkeypatch):
    monkeypatch.setenv("VOICESTUDIO_URL", "http://127.0.0.1:9")
    with pytest.raises(voicestudio.StudioError, match="Không kết nối") as e:
        voicestudio.get_json("/health")
    assert e.value.network


def test_check_lists_engines_licenses_and_profiles(studio, capsys):
    voicestudio.check()
    out = capsys.readouterr().out
    assert "voxcpm2: dùng được" in out and "omnivoice: KHÔNG" in out and "kaku-123" in out


def test_pack_then_unpack_on_another_machine(studio, tmp_path):
    d = video(tmp_path)
    with pytest.raises(voicestudio.StudioError, match="Còn thiếu"):
        voicestudio.pack(d)
    voicestudio.run(d, cfg())
    archive = voicestudio.pack(d)
    assert archive.name == "giong-vi.zip"
    other = tmp_path / "may-khac"
    other.mkdir()
    (other / "scenes.json").write_text((d / "scenes.json").read_text(encoding="utf-8"), encoding="utf-8")
    got, missing = voicestudio.unpack(other, archive)
    assert got == ["s01", "s02", "s03"] and missing == []
    assert (other / "assets" / "audio" / "vi" / "s02.wav").read_bytes() == (d / "assets" / "audio" / "vi" / "s02.wav").read_bytes()
