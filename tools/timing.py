"""Tính thời lượng cảnh, khớp bản lồng tiếng và tạo phụ đề SRT (hàm thuần, dễ test)."""

from __future__ import annotations

import re
from dataclasses import dataclass

from tools import config


class NeedsShorterTranslation(ValueError):
    """Bản dịch đọc quá dài, không khớp được vào độ dài cảnh kể cả khi tăng tốc tối đa."""


@dataclass(frozen=True)
class Fit:
    tempo: float  # >1 là đọc nhanh hơn, 1.0 là giữ nguyên
    pad_s: float  # khoảng lặng thêm vào cuối cảnh


def scene_durations(speech_s: list[float], padding_s: float = config.SCENE_PADDING_S) -> list[float]:
    """Độ dài mỗi cảnh = độ dài giọng ngôn ngữ chính + khoảng lặng."""
    return [round(s + padding_s, 3) for s in speech_s]


def fit_to_scene(speech_s: float, scene_s: float, max_tempo: float = config.MAX_TEMPO) -> Fit:
    """Khớp một đoạn giọng (ngôn ngữ phụ) vào đúng độ dài cảnh.

    Ưu tiên giữ tốc độ tự nhiên và chèn khoảng lặng. Chỉ tăng tốc khi giọng dài hơn
    cảnh, và không quá ``max_tempo``.
    """
    if speech_s <= scene_s:
        return Fit(tempo=1.0, pad_s=round(scene_s - speech_s, 3))
    tempo = speech_s / scene_s
    if tempo > max_tempo:
        raise NeedsShorterTranslation(
            f"giọng dài {speech_s:.2f}s, cảnh chỉ {scene_s:.2f}s (cần tăng tốc {tempo:.2f}x > {max_tempo}x)"
        )
    return Fit(tempo=round(tempo, 4), pad_s=0.0)


def starts(durations: list[float]) -> list[float]:
    out, t = [], 0.0
    for d in durations:
        out.append(round(t, 3))
        t += d
    return out


def srt_timestamp(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def chapter_timestamp(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


_SENTENCE_END = re.compile(r"(?<=[.!?…。！？])\s+")


def split_caption(text: str, max_chars: int = 84) -> list[str]:
    """Chia lời thoại thành các dòng phụ đề ngắn, ưu tiên cắt ở cuối câu rồi mới cắt theo từ."""
    chunks: list[str] = []
    for sentence in _SENTENCE_END.split(text.strip()):
        sentence = sentence.strip()
        if not sentence:
            continue
        if len(sentence) <= max_chars:
            chunks.append(sentence)
            continue
        words = sentence.split()
        if len(words) == 1:  # ngôn ngữ không có dấu cách (tiếng Trung)
            chunks.extend(sentence[i : i + max_chars] for i in range(0, len(sentence), max_chars))
            continue
        line = ""
        for w in words:
            candidate = f"{line} {w}".strip()
            if len(candidate) > max_chars and line:
                chunks.append(line)
                line = w
            else:
                line = candidate
        if line:
            chunks.append(line)
    return chunks


def build_srt(texts: list[str], scene_starts: list[float], speech_s: list[float]) -> str:
    """Tạo SRT: thời gian mỗi dòng chia theo tỷ lệ số ký tự trong phần có giọng của cảnh."""
    entries: list[str] = []
    n = 1
    for text, start, dur in zip(texts, scene_starts, speech_s):
        chunks = split_caption(text)
        total = sum(len(c) for c in chunks) or 1
        t = start
        for c in chunks:
            d = dur * len(c) / total
            entries.append(f"{n}\n{srt_timestamp(t)} --> {srt_timestamp(t + d)}\n{c}\n")
            n += 1
            t += d
    return "\n".join(entries)
