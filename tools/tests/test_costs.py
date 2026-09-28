import json

import pytest

from tools import config, costs, scenes


def board(chars_vi: int, n: int = 2) -> scenes.Storyboard:
    return scenes.parse(
        {
            "languages": ["vi"],
            "scenes": [
                {"id": f"s{i}", "narration": {"vi": "a" * chars_vi}, "image_prompt": "p"} for i in range(n)
            ],
        }
    )


def test_estimate_counts_images_and_speech():
    est = costs.estimate(board(chars_vi=130, n=2))
    assert est["images"] == 2
    assert est["tts_seconds"]["vi"] == pytest.approx(260 / config.CHARS_PER_SECOND["vi"], abs=0.1)
    expected = 2 * config.PRICE_PER_IMAGE + est["tts_seconds"]["vi"] * config.PRICE_TTS_PER_SECOND
    assert est["usd"] == pytest.approx(expected, abs=0.001)


def test_estimate_without_images():
    assert costs.estimate(board(10), images=False)["images"] == 0


def test_add_usage_accumulates(tmp_path):
    costs.add_usage(tmp_path, images=3)
    costs.add_usage(tmp_path, lang="vi", tts_seconds=60)
    costs.add_usage(tmp_path, lang="vi", tts_seconds=30)
    usage = json.loads((tmp_path / "cost.json").read_text())
    assert usage["images"] == 3
    assert usage["tts_seconds"] == {"vi": 90}
    assert usage["usd"] == pytest.approx(3 * config.PRICE_PER_IMAGE + 90 * config.PRICE_TTS_PER_SECOND, abs=0.001)


def test_record_and_month_total(tmp_path):
    ledger = tmp_path / "costs.md"
    ledger.write_text("| Tháng | Video | Ảnh | Giây giọng đọc | Chi phí (USD) |\n|---|---|---|---|---|\n")
    video = tmp_path / "2026-10-01-thu"
    video.mkdir()
    costs.add_usage(video, images=10)
    costs.record(video, ledger)
    costs.record(video, ledger)
    import datetime as dt

    month = dt.date.today().strftime("%Y-%m")
    assert costs.month_total(ledger, month) == pytest.approx(2 * 10 * config.PRICE_PER_IMAGE, abs=0.01)
    assert costs.month_total(ledger, "1999-01") == 0
