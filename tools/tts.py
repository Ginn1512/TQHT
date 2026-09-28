"""Tạo giọng đọc cho từng cảnh bằng Gemini TTS.

    python -m tools.tts videos/<thư-mục> --lang vi
    python -m tools.tts --test                      # đọc thử 1 câu mỗi ngôn ngữ (~0,01 USD)

Kết quả: videos/<thư-mục>/assets/audio/<lang>/<scene-id>.wav
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from tools import config, costs, gemini, media, scenes

TEST_SENTENCES = {
    "vi": "Xin chào, đây là giọng đọc thử cho kênh phân tích anime.",
    "en": "Hello, this is a test voice for the anime analysis channel.",
    "pt-BR": "Olá, esta é uma voz de teste para o canal de análise de anime.",
    "hi": "नमस्ते, यह एनीमे विश्लेषण चैनल के लिए एक परीक्षण आवाज़ है।",
    "zh-TW": "你好，這是動漫分析頻道的測試語音。",
}


def synthesize(text: str, lang: str, voice: str | None = None) -> tuple[Path, bool]:
    """Trả về (đường dẫn WAV trong cache, có gọi API mới hay không)."""
    info = config.LANGUAGES[lang]
    voice = voice or info["voice"]
    cached = gemini.cache_path("tts", config.TTS_MODEL, lang, voice, text, suffix=".wav")
    if cached.exists():
        return cached, False

    from google.genai import types

    cfg = types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            language_code=info["tts_code"],
            voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)),
        ),
    )
    resp = gemini.with_retry(
        lambda: gemini.client().models.generate_content(model=config.TTS_MODEL, contents=text, config=cfg)
    )
    blobs = [p.inline_data for p in resp.candidates[0].content.parts if p.inline_data and p.inline_data.data]
    if not blobs:
        raise RuntimeError(f"TTS không trả về âm thanh cho: {text[:60]}...")
    # mime_type dạng "audio/L16;codec=pcm;rate=24000"
    rate = re.search(r"rate=(\d+)", blobs[0].mime_type or "")
    media.pcm_to_wav(
        b"".join(b.data for b in blobs), cached, rate=int(rate.group(1)) if rate else config.TTS_SAMPLE_RATE
    )
    return cached, True


def run(video_dir: Path, lang: str) -> list[Path]:
    board = scenes.load(video_dir)
    if lang not in board.languages:
        raise SystemExit(f"'{lang}' chưa có trong languages của scenes.json")
    out_dir = Path(video_dir) / "assets" / "audio" / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for scene in board.scenes:
        wav, fresh = synthesize(scene.narration[lang], lang)
        dst = out_dir / f"{scene.id}.wav"
        shutil.copyfile(wav, dst)
        secs = media.wav_duration(dst)
        if fresh:
            costs.add_usage(video_dir, lang=lang, tts_seconds=secs)
        print(f"{scene.id} [{lang}] {secs:.1f}s{'' if fresh else ' (cache)'}")
        outputs.append(dst)
    return outputs


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path, nargs="?")
    p.add_argument("--lang", default=config.PRIMARY_LANGUAGE, choices=sorted(config.LANGUAGES))
    p.add_argument("--test", action="store_true")
    args = p.parse_args()

    if args.test:
        out = config.CACHE_DIR / "test"
        out.mkdir(parents=True, exist_ok=True)
        for lang, text in TEST_SENTENCES.items():
            wav, _ = synthesize(text, lang)
            dst = out / f"tts-{lang}.wav"
            shutil.copyfile(wav, dst)
            print(f"{lang}: {dst} ({media.wav_duration(dst):.1f}s)")
        return
    if not args.video_dir:
        p.error("cần video_dir hoặc --test")
    run(args.video_dir, args.lang)


if __name__ == "__main__":
    gemini.cli(main)
