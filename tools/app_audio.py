"""Giọng đọc làm tay (AI Studio, ElevenLabs, công cụ khác hoặc tự thu): xuất đoạn đọc và nhập file giọng.

    python -m tools.app_audio export videos/<thư-mục> --engine gemini       # đoạn đọc c01, c02… (JSON)
    python -m tools.app_audio import videos/<thư-mục> --from <folder>       # c01.wav, c02.mp3… → giọng từng cảnh

Mỗi đoạn đọc gồm vài chương liền nhau (tối đa khoảng 2.000 ký tự, khoảng 2,5 phút). Khi nhập, mỗi
đoạn được cắt thành từng cảnh tại khoảng lặng gần nhất với chỗ cắt dự kiến (tỉ lệ theo số ký tự), rồi
lưu vào assets/audio/<lang>/<scene-id>.wav để `tools.assemble` dựng như giọng tạo bằng API.
Cấu hình giọng, ghi chú đạo diễn và thẻ của từng công cụ: channel/giong-kaku.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from tools import config, costs, media, scenes

VOICE_FILE = config.CHANNEL_DIR / "giong-kaku.json"
ENGINES = ("gemini", "elevenlabs", "plain")
AUDIO_EXTS = {".wav", ".mp3", ".m4a", ".aac", ".ogg", ".opus", ".flac", ".webm"}
_SENTENCE = re.compile(r"(?<=[.!?…])\s+")


def load_voice(path: Path = VOICE_FILE) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


@dataclass
class Chunk:
    id: str
    chapters: list[str]
    scenes: list[scenes.Scene]

    @property
    def chars(self) -> int:
        return sum(len(s.narration[config.PRIMARY_LANGUAGE]) for s in self.scenes)


def chunk_plan(board: scenes.Storyboard, max_chars: int = 2000) -> list[Chunk]:
    """Gộp các chương liền nhau thành đoạn đọc, mỗi đoạn không quá max_chars (trừ khi một chương đã dài hơn)."""
    lang = config.PRIMARY_LANGUAGE
    chapters: list[tuple[str, list[scenes.Scene]]] = []
    for s in board.scenes:
        if s.chapter or not chapters:
            chapters.append((s.chapter, []))
        chapters[-1][1].append(s)
    chunks: list[Chunk] = []
    for title, members in chapters:
        size = sum(len(s.narration[lang]) for s in members)
        if chunks and chunks[-1].chars + size <= max_chars:
            chunks[-1].chapters.append(title)
            chunks[-1].scenes.extend(members)
        else:
            chunks.append(Chunk(id=f"c{len(chunks) + 1:02d}", chapters=[title], scenes=list(members)))
    return chunks


def director_notes(voice: dict) -> str:
    """Ghi chú đạo diễn (dán vào ô chỉ đạo / style instructions), kèm giọng vùng miền của giọng đã chọn."""
    notes = voice["director_notes"]
    chosen = next((v for v in voice["voices"] if v["id"] == voice.get("chosen")), None)
    lines = [notes["profile"], notes["scene"], "DIRECTOR'S NOTES:"]
    lines += [f"- {d}" for d in notes["direction"]]
    if chosen:
        lines.append(f"- Accent: {chosen['accent']}.")
    return "\n".join(lines)


def _tag(tag: str, text: str) -> str:
    return f"{tag} {text}" if tag else text


def perform(chunk: Chunk, voice: dict, engine: str) -> str:
    """Lời đọc của một đoạn cho một công cụ: mỗi cảnh một đoạn văn, thẻ dừng/cười/tò mò theo công cụ."""
    tags = voice["engines"][engine]
    twists = tuple(voice.get("twist_starts", []))
    smiled = asked = False
    paragraphs = []
    for i, s in enumerate(chunk.scenes):
        sentences = _SENTENCE.split(s.narration[config.PRIMARY_LANGUAGE].strip())
        out = []
        for j, sent in enumerate(sentences):
            # dừng giữa hai cảnh và trước câu mở ra điểm bất ngờ
            pause = (i > 0 and j == 0) or (j > 0 and sent.startswith(twists))
            if tags["smile"] and not smiled and s.use_mascot and "Kaku" in sent:
                sent, smiled = _tag(tags["smile"], sent), True
            elif tags["question"] and not asked and sent.endswith("?"):
                sent, asked = _tag(tags["question"], sent), True
            if pause:
                sent = _tag(tags["pause"], sent)
            out.append(sent)
        paragraphs.append(" ".join(out))
    return "\n\n".join(paragraphs)


def export(board: scenes.Storyboard, voice: dict | None = None) -> dict:
    """Mọi thứ cần để làm giọng bằng tay, cho cả 3 công cụ (dùng cho trang Xưởng và prompts.vi.md)."""
    voice = voice or load_voice()
    rate = config.CHARS_PER_SECOND[config.PRIMARY_LANGUAGE]
    return {
        "chosen": voice.get("chosen"),
        "voices": voice["voices"],
        "sample": voice["sample"],
        "notes": director_notes(voice),
        "engines": {k: {"label": v["label"], "how": v["how"]} for k, v in voice["engines"].items()},
        "chunks": [
            {
                "id": c.id,
                "chapters": [t for t in c.chapters if t],
                "scenes": [s.id for s in c.scenes],
                "chars": c.chars,
                "seconds": round(c.chars / rate),
                "text": {e: perform(c, voice, e) for e in ENGINES},
            }
            for c in chunk_plan(board, voice.get("max_chunk_chars", 2000))
        ],
    }


def split_segments(
    total: float, weights: list[int], silences: list[tuple[float, float]], window: float = 1.5, keep: float = 0.06
) -> list[tuple[float, float]]:
    """Chia một đoạn giọng dài `total` giây thành len(weights) đoạn (bắt đầu, kết thúc).

    Chỗ cắt dự kiến tỉ lệ với số ký tự còn lại, rồi dời về khoảng lặng gần nhất trong cửa sổ (ưu tiên
    khoảng lặng dài). Phần lặng ở chỗ cắt, đầu và cuối được bỏ đi (giữ `keep` giây), vì khi dựng đã
    có khoảng nghỉ cố định giữa các cảnh. Không có khoảng lặng phù hợp thì cắt đúng chỗ dự kiến.
    """
    sil = sorted(silences)
    start, end = 0.0, total
    if sil and sil[0][0] <= keep:
        start = max(0.0, sil[0][1] - keep)
    if sil and sil[-1][1] >= total - keep:
        end = min(total, sil[-1][0] + keep)
    segments = []
    pos = start
    for i in range(len(weights) - 1):
        remaining_w = sum(weights[i:])
        expected = pos + (end - pos) * weights[i] / remaining_w
        win = max(window, 0.2 * (expected - pos))
        best, best_score = None, None
        for a, b in sil:
            mid = (a + b) / 2
            if a <= pos + 0.3 or b >= end or abs(mid - expected) > win:
                continue
            score = abs(mid - expected) - 1.5 * min(b - a, 1.0)
            if best_score is None or score < best_score:
                best, best_score = (a, b), score
        if best:
            segments.append((pos, min(best[0] + keep, best[1])))
            pos = max(best[1] - keep, best[0])
        else:
            segments.append((pos, expected))
            pos = expected
    segments.append((pos, end))
    return segments


def find_sources(folder: Path) -> dict[str, Path]:
    """{chunk id: file} theo tên file (c01.wav, c02.mp3, …). Bỏ qua file không phải âm thanh."""
    return {p.stem.lower(): p for p in sorted(Path(folder).iterdir()) if p.suffix.lower() in AUDIO_EXTS}


def import_audio(video_dir: Path, folder: Path, lang: str = config.PRIMARY_LANGUAGE) -> tuple[list[str], list[str]]:
    """Cắt từng file đoạn đọc thành giọng từng cảnh. Trả về (id đoạn đã nhập, id đoạn còn thiếu)."""
    board = scenes.load(video_dir)
    voice = load_voice()
    sources = find_sources(folder)
    out_dir = Path(video_dir) / "assets" / "audio" / lang
    done, missing = [], []
    seconds = 0.0
    with tempfile.TemporaryDirectory() as tmp:
        for chunk in chunk_plan(board, voice.get("max_chunk_chars", 2000)):
            src = sources.get(chunk.id)
            if not src:
                missing.append(chunk.id)
                continue
            wav = Path(tmp) / f"{chunk.id}.wav"
            media.run_ffmpeg(["-i", str(src), "-ac", "1", "-ar", str(config.TTS_SAMPLE_RATE), "-sample_fmt", "s16", str(wav)])
            total = media.wav_duration(wav)
            weights = [len(s.narration[lang]) for s in chunk.scenes]
            segments = split_segments(total, weights, media.silences(wav))
            media.cut_wav(wav, segments, [out_dir / f"{s.id}.wav" for s in chunk.scenes])
            seconds += total
            done.append(chunk.id)
    usage = costs.load_usage(video_dir)
    app = usage.setdefault("tts_app_seconds", {})
    app[lang] = round(app.get(lang, 0.0) + seconds, 1)
    usage["usd"] = costs.usd_of(usage)
    (Path(video_dir) / costs.COST_FILE).write_text(json.dumps(usage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return done, missing


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("video_dir", type=Path)
    i = sub.add_parser("import")
    i.add_argument("video_dir", type=Path)
    i.add_argument("--from", dest="folder", type=Path, required=True)
    args = p.parse_args()

    if args.cmd == "export":
        json.dump(export(scenes.load(args.video_dir)), sys.stdout, ensure_ascii=False, indent=1)
        print()
        return
    done, missing = import_audio(args.video_dir, args.folder)
    print(f"Đã nhập {len(done)} đoạn giọng.")
    if missing:
        print(f"Còn thiếu {len(missing)} đoạn: {', '.join(missing)}")


if __name__ == "__main__":
    main()
