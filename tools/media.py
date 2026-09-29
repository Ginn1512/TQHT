"""Tiện ích âm thanh/video dùng chung: gọi ffmpeg, đọc/ghi WAV, dò thông tin file."""

from __future__ import annotations

import re
import subprocess
import wave
from dataclasses import dataclass
from pathlib import Path

import imageio_ffmpeg

from tools import config


def ffmpeg_exe() -> str:
    return imageio_ffmpeg.get_ffmpeg_exe()


def run_ffmpeg(args: list[str]) -> None:
    cmd = [ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", *args]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg lỗi ({result.returncode}): {result.stderr.strip()[-2000:]}")


def pcm_to_wav(pcm: bytes, path: Path, rate: int = config.TTS_SAMPLE_RATE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(pcm)


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / w.getframerate()


def concat_wavs_exact(parts: list[Path], durations: list[float], out: Path) -> None:
    """Nối các WAV cùng định dạng, mỗi đoạn được đệm lặng hoặc cắt cho đúng độ dài cảnh."""
    out.parent.mkdir(parents=True, exist_ok=True)
    params = None
    with wave.open(str(out), "wb") as dst:
        for part, dur in zip(parts, durations):
            with wave.open(str(part), "rb") as src:
                if params is None:
                    params = (src.getnchannels(), src.getsampwidth(), src.getframerate())
                    dst.setnchannels(params[0])
                    dst.setsampwidth(params[1])
                    dst.setframerate(params[2])
                elif (src.getnchannels(), src.getsampwidth(), src.getframerate()) != params:
                    raise ValueError(f"{part} khác định dạng với các đoạn trước")
                frame_bytes = params[0] * params[1]
                want = int(round(dur * params[2]))
                data = src.readframes(min(src.getnframes(), want))
                have = len(data) // frame_bytes
                dst.writeframes(data + b"\x00" * frame_bytes * (want - have))


_SIL_START = re.compile(r"silence_start: (-?\d+(?:\.\d+)?)")
_SIL_END = re.compile(r"silence_end: (\d+(?:\.\d+)?)")


def silences(path: Path, noise_db: float = -35.0, min_s: float = 0.2) -> list[tuple[float, float]]:
    """Các khoảng lặng (bắt đầu, kết thúc) tính bằng giây, dò bằng bộ lọc silencedetect của ffmpeg."""
    cmd = [ffmpeg_exe(), "-hide_banner", "-nostats", "-i", str(path),
           "-af", f"silencedetect=noise={noise_db}dB:d={min_s}", "-f", "null", "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg lỗi ({result.returncode}): {result.stderr.strip()[-2000:]}")
    starts = [max(0.0, float(x)) for x in _SIL_START.findall(result.stderr)]
    ends = [float(x) for x in _SIL_END.findall(result.stderr)]
    if len(ends) < len(starts):  # khoảng lặng kéo tới hết file
        ends.append(wav_duration(path) if Path(path).suffix.lower() == ".wav" else probe(path).duration_s)
    return list(zip(starts, ends))


def cut_wav(src: Path, segments: list[tuple[float, float]], outs: list[Path]) -> None:
    """Cắt một WAV thành nhiều file theo các đoạn (bắt đầu, kết thúc) tính bằng giây."""
    with wave.open(str(src), "rb") as w:
        params = w.getparams()
        data = w.readframes(w.getnframes())
    frame_bytes = params.nchannels * params.sampwidth
    for (start, end), out in zip(segments, outs):
        a, b = int(round(start * params.framerate)), int(round(end * params.framerate))
        out.parent.mkdir(parents=True, exist_ok=True)
        with wave.open(str(out), "wb") as dst:
            dst.setnchannels(params.nchannels)
            dst.setsampwidth(params.sampwidth)
            dst.setframerate(params.framerate)
            dst.writeframes(data[a * frame_bytes : b * frame_bytes])


@dataclass
class MediaInfo:
    duration_s: float
    video: list[str]
    audio: list[str]


_DURATION = re.compile(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)")
_STREAM = re.compile(r"Stream #\S+.*?: (Video|Audio): (.+)")


def probe(path: Path) -> MediaInfo:
    """Đọc thời lượng và các luồng video/audio (imageio-ffmpeg không kèm ffprobe)."""
    result = subprocess.run([ffmpeg_exe(), "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    text = result.stderr
    m = _DURATION.search(text)
    if not m:
        raise RuntimeError(f"không đọc được {path}: {text.strip()[-500:]}")
    h, mnt, s = m.groups()
    info = MediaInfo(duration_s=int(h) * 3600 + int(mnt) * 60 + float(s), video=[], audio=[])
    for kind, desc in _STREAM.findall(text):
        (info.video if kind == "Video" else info.audio).append(desc.strip())
    return info
