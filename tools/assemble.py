"""Dựng video: ảnh + chuyển động nhẹ + chữ trên màn hình + giọng đọc + nhạc nền.

    python -m tools.assemble videos/<thư-mục>
    python -m tools.assemble videos/<thư-mục> --music assets/music/nhac.mp3
    python -m tools.assemble --demo            # clip thử bằng dữ liệu giả, không cần API key
    python -m tools.assemble videos/<thư-mục> --draft   # bản nháp KHÔNG TIẾNG 960×540 khi chưa có giọng đọc

Cần có: assets/images/<id>.png và assets/audio/<lang>/<id>.wav cho mọi cảnh.
Độ dài mỗi cảnh do giọng tiếng Việt quyết định; các bản lồng tiếng khác được khớp theo.

Kết quả trong render/:
- video.vi.mp4             video chính (H.264 + AAC) để tải lên YouTube
- audio.<lang>.m4a         bản âm thanh phụ, tải lên mục Ngôn ngữ trong YouTube Studio
- subs.<lang>.srt          phụ đề cho từng ngôn ngữ
- chapters.txt             mốc chương để dán vào phần mô tả
- draft.<lang>.mp4         (chế độ --draft) bản nháp để duyệt hình, độ dài cảnh ước tính theo lời thoại
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import sys
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from tools import config, media, scenes, timing

FONT = config.FONTS_DIR / "BeVietnamPro-ExtraBold.ttf"


def render_overlay(text: str, out: Path, size: tuple[int, int]) -> None:
    """Chữ trắng trên hộp tối ở góc dưới, nền trong suốt."""
    w, h = size
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(FONT), max(12, int(h * 0.055)))
    max_w = int(w * 0.8)

    lines: list[str] = []
    for word in text.split():
        if lines and draw.textlength(f"{lines[-1]} {word}", font=font) <= max_w:
            lines[-1] = f"{lines[-1]} {word}"
        else:
            lines.append(word)
    line_h = int(font.size * 1.3)
    pad = int(font.size * 0.6)
    box_w = int(max(draw.textlength(line, font=font) for line in lines)) + 2 * pad
    box_h = line_h * len(lines) + 2 * pad
    x0, y0 = int(w * 0.06), int(h * 0.94) - box_h
    draw.rounded_rectangle((x0, y0, x0 + box_w, y0 + box_h), radius=pad, fill=(10, 10, 20, 190))
    for i, line in enumerate(lines):
        draw.text((x0 + pad, y0 + pad + i * line_h), line, font=font, fill=(255, 255, 255, 255))
    img.save(out)


def ken_burns(index: int, frames: int) -> str:
    """Luân phiên: phóng to, thu nhỏ, lia ngang. Trả về biểu thức zoompan (chưa có d/s/fps)."""
    n = max(frames - 1, 1)
    center = "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    kind = index % 3
    if kind == 0:
        return f"z='1+0.08*on/{n}':{center}"
    if kind == 1:
        return f"z='1.08-0.08*on/{n}':{center}"
    return f"z='1.08':x='(iw-iw/zoom)*on/{n}':y='ih/2-(ih/zoom/2)'"


def frame_counts(durations: list[float], fps: int) -> list[int]:
    """Số khung hình mỗi cảnh, làm tròn theo mốc cộng dồn để hình không lệch tiếng dần về cuối."""
    counts, prev, t = [], 0, 0.0
    for d in durations:
        t += d
        end = round(t * fps)
        counts.append(max(1, end - prev))
        prev = end
    return counts


def render_segment(
    image: Path,
    overlay: Path | None,
    frames: int,
    index: int,
    out: Path,
    size: tuple[int, int],
    fps: int,
    crf: int = 20,
) -> None:
    w, h = size
    zoom = ken_burns(index, frames)
    # Phóng ảnh lên gấp đôi trước khi zoompan để chuyển động mượt, không bị rung.
    chain = f"[0:v]scale={2 * w}:{2 * h},zoompan={zoom}:d={frames}:s={w}x{h}:fps={fps}"
    args = ["-i", str(image)]
    if overlay:
        args += ["-i", str(overlay)]
        chain += "[bg];[bg][1:v]overlay=0:0"
    chain += ",format=yuv420p[v]"
    media.run_ffmpeg(
        [
            *args,
            "-filter_complex", chain,
            "-map", "[v]",
            "-frames:v", str(frames),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-r", str(fps),
            str(out),
        ]
    )


def render_clip_segment(
    clip: Path, overlay: Path | None, frames: int, out: Path, size: tuple[int, int], fps: int
) -> None:
    """Cảnh dùng clip AI (Seedance): cắt/lặp cho đủ độ dài cảnh, bỏ tiếng, phủ chữ nếu có."""
    w, h = size
    chain = f"[0:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={fps},setsar=1"
    args = ["-stream_loop", "-1", "-i", str(clip)]
    if overlay:
        args += ["-i", str(overlay)]
        chain += "[bg];[bg][1:v]overlay=0:0"
    chain += ",format=yuv420p[v]"
    media.run_ffmpeg(
        [
            *args,
            "-filter_complex", chain,
            "-map", "[v]", "-an",
            "-frames:v", str(frames),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(fps),
            str(out),
        ]
    )


def encode_audio(track_wav: Path, out: Path, total_s: float, music: Path | None, video: Path | None = None) -> None:
    """Mã hoá AAC, trộn nhạc nền (lặp lại cho đủ dài). Nếu có video thì ghép luôn thành MP4."""
    args: list[str] = []
    if video:
        args += ["-i", str(video)]
    a = 1 if video else 0
    args += ["-i", str(track_wav)]
    if music:
        args += ["-stream_loop", "-1", "-i", str(music)]
        mix = (
            f"[{a + 1}:a]volume={config.MUSIC_VOLUME}[m];"
            f"[{a}:a][m]amix=inputs=2:duration=first:normalize=0[a]"
        )
        args += ["-filter_complex", mix, "-map", "[a]"]
    else:
        args += ["-map", f"{a}:a"]
    if video:
        args += ["-map", "0:v", "-c:v", "copy", "-movflags", "+faststart"]
    args += ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-t", f"{total_s:.3f}", str(out)]
    media.run_ffmpeg(args)


def fit_language(parts: list[Path], durations: list[float], tmp: Path) -> tuple[list[Path], list[float]]:
    """Khớp từng đoạn giọng vào độ dài cảnh. Trả về (các WAV đã khớp, độ dài giọng thực)."""
    fitted, spoken, problems = [], [], []
    for i, (part, scene_s) in enumerate(zip(parts, durations)):
        speech = media.wav_duration(part)
        try:
            fit = timing.fit_to_scene(speech, scene_s)
        except timing.NeedsShorterTranslation as e:
            problems.append(f"{part.stem}: {e}")
            continue
        if fit.tempo != 1.0:
            sped = tmp / f"{part.stem}.tempo.wav"
            media.run_ffmpeg(["-i", str(part), "-filter:a", f"atempo={fit.tempo}", str(sped)])
            fitted.append(sped)
            spoken.append(speech / fit.tempo)
        else:
            fitted.append(part)
            spoken.append(speech)
    if problems:
        raise timing.NeedsShorterTranslation("cần rút gọn bản dịch ở các cảnh:\n- " + "\n- ".join(problems))
    return fitted, spoken


def write_chapters(board: scenes.Storyboard, starts: list[float], out: Path) -> None:
    rows = [(t, s.chapter) for t, s in zip(starts, board.scenes) if s.chapter]
    if rows and rows[0][0] > 0:
        rows.insert(0, (0.0, "Mở đầu"))
    lines = [f"{timing.chapter_timestamp(t)} {title}" for t, title in rows]
    if len(lines) < 3:
        lines.append("(YouTube cần ít nhất 3 chương, mỗi chương ≥ 10 giây, để hiện mốc chương)")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def draft_speech_seconds(board: scenes.Storyboard, lang: str = config.PRIMARY_LANGUAGE) -> list[float]:
    """Độ dài giọng ước tính mỗi cảnh (số ký tự ÷ tốc độ đọc), dùng cho bản nháp chưa có giọng."""
    return [round(len(s.narration.get(lang, "")) / config.CHARS_PER_SECOND[lang], 3) for s in board.scenes]


def silent_wavs(seconds: list[float], ids: list[str], folder: Path, rate: int = config.TTS_SAMPLE_RATE) -> list[Path]:
    paths = []
    for sid, sec in zip(ids, seconds):
        path = folder / f"silent_{sid}.wav"
        media.pcm_to_wav(b"\x00\x00" * int(round(sec * rate)), path, rate=rate)
        paths.append(path)
    return paths


DRAFT_SIZE = (960, 540)
DRAFT_FPS = 24
DRAFT_CRF = 26


def run(
    video_dir: Path,
    music: Path | None = None,
    size: tuple[int, int] = (config.WIDTH, config.HEIGHT),
    fps: int = config.FPS,
    draft: bool = False,
    crf: int = 20,
) -> Path:
    video_dir = Path(video_dir)
    board = scenes.load(video_dir)
    primary = config.PRIMARY_LANGUAGE
    assets, render = video_dir / "assets", video_dir / "render"
    tmp = render / "tmp"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)

    images = [assets / "images" / f"{s.id}.png" for s in board.scenes]
    if draft:
        main_audio = silent_wavs(draft_speech_seconds(board), [s.id for s in board.scenes], tmp)
    else:
        main_audio = [assets / "audio" / primary / f"{s.id}.wav" for s in board.scenes]
    clips = [assets / "clips" / f"{s.id}.mp4" for s in board.scenes]
    missing = [str(img) for img, clip in zip(images, clips) if not img.exists() and not clip.exists()]
    missing += [str(p) for p in main_audio if not p.exists()]
    if missing:
        raise SystemExit("Thiếu file, hãy chạy tools.images / tools.tts trước:\n- " + "\n- ".join(missing))

    speech = [media.wav_duration(p) for p in main_audio]
    durations = timing.scene_durations(speech)
    starts = timing.starts(durations)
    total = round(sum(durations), 3)

    # 1. Dựng từng cảnh rồi nối lại (cùng thông số mã hoá nên nối không cần mã hoá lại).
    segments = []
    frames = frame_counts(durations, fps)
    for i, (scene, image, dur) in enumerate(zip(board.scenes, images, durations)):
        overlay = None
        if scene.on_screen_text:
            overlay = tmp / f"overlay_{scene.id}.png"
            render_overlay(scene.on_screen_text, overlay, size)
        seg = tmp / f"seg_{i:03d}.mp4"
        if clips[i].exists():
            render_clip_segment(clips[i], overlay, frames[i], seg, size, fps)
        else:
            render_segment(image, overlay, frames[i], i, seg, size, fps, crf)
        segments.append(seg)
        print(f"Cảnh {i + 1}/{len(board.scenes)} ({scene.id}, {dur:.1f}s)", flush=True)
    concat_list = tmp / "segments.txt"
    concat_list.write_text("".join(f"file '{s.name}'\n" for s in segments), encoding="utf-8")
    silent = tmp / "video_only.mp4"
    media.run_ffmpeg(["-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(silent)])

    # 2. Giọng ngôn ngữ chính + ghép thành video hoàn chỉnh.
    main_track = tmp / f"track.{primary}.wav"
    media.concat_wavs_exact(main_audio, durations, main_track)
    final = render / f"{'draft' if draft else 'video'}.{primary}.mp4"
    encode_audio(main_track, final, total, music, video=silent)
    subs = {primary: [s.narration[primary] for s in board.scenes]}
    (render / f"subs.{primary}.srt").write_text(
        timing.build_srt(subs[primary], starts, speech), encoding="utf-8"
    )

    # 3. Các bản lồng tiếng khác (nếu đã tạo giọng).
    report = {"total_s": total, "length_problem": timing.length_problem(total), "languages": {primary: "ok"}}
    if draft:
        report["draft"] = "không tiếng, độ dài cảnh ước tính theo lời thoại"
    for lang in board.languages:
        if lang == primary or draft:
            continue
        parts = [assets / "audio" / lang / f"{s.id}.wav" for s in board.scenes]
        if not all(p.exists() for p in parts):
            report["languages"][lang] = "chưa có giọng (chạy tools.tts --lang %s)" % lang
            continue
        try:
            fitted, spoken = fit_language(parts, durations, tmp)
        except timing.NeedsShorterTranslation as e:
            report["languages"][lang] = str(e)
            print(f"[{lang}] {e}", file=sys.stderr)
            continue
        track = tmp / f"track.{lang}.wav"
        media.concat_wavs_exact(fitted, durations, track)
        encode_audio(track, render / f"audio.{lang}.m4a", total, music)
        texts = [s.narration[lang] for s in board.scenes]
        (render / f"subs.{lang}.srt").write_text(timing.build_srt(texts, starts, spoken), encoding="utf-8")
        report["languages"][lang] = "ok"

    write_chapters(board, starts, render / "chapters.txt")
    (render / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    return final


def make_demo(root: Path, size: tuple[int, int] = (config.WIDTH, config.HEIGHT)) -> Path:
    """Tạo một thư mục video giả: 3 cảnh, ảnh vẽ bằng Pillow, âm thanh là tiếng bíp."""
    shutil.rmtree(root, ignore_errors=True)
    colors = [((40, 20, 80), (230, 90, 60)), ((10, 60, 90), (240, 200, 80)), ((60, 10, 30), (120, 200, 255))]
    board = {
        "title": "Demo",
        "languages": ["vi", "en"],
        "scenes": [
            {
                "id": f"s0{i + 1}",
                "chapter": ["Mở đầu", "Phân tích", "Kết luận"][i],
                "narration": {
                    "vi": ["Đây là cảnh mở đầu thử nghiệm.", "Cảnh thứ hai có chữ trên màn hình.", "Hết demo!"][i],
                    "en": ["This is the test opening scene.", "Scene two has on-screen text.", "End of demo!"][i],
                },
                "image_prompt": "demo",
                "on_screen_text": ["", "Chữ tiếng Việt có dấu: Sức mạnh thật sự", "Cảm ơn đã xem"][i],
            }
            for i in range(3)
        ],
    }
    (root / "assets" / "images").mkdir(parents=True)
    (root / "scenes.json").write_text(json.dumps(board, ensure_ascii=False, indent=2), encoding="utf-8")

    w, h = size
    for i, (c1, c2) in enumerate(colors):
        img = Image.new("RGB", size)
        draw = ImageDraw.Draw(img)
        for y in range(h):  # nền chuyển màu dọc
            t = y / h
            draw.line([(0, y), (w, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(c1, c2)))
        r = h // 4
        draw.ellipse((w // 2 - r, h // 2 - r, w // 2 + r, h // 2 + r), outline=(255, 255, 255), width=max(2, h // 90))
        img.save(root / "assets" / "images" / f"s0{i + 1}.png")

    # vi quyết định độ dài cảnh; en: cảnh 1 dài hơn (phải tăng tốc), cảnh 2 ngắn hơn (đệm lặng).
    lengths = {"vi": [5.0, 6.0, 4.5], "en": [5.6, 5.0, 4.9]}
    for lang, secs in lengths.items():
        for i, s in enumerate(secs):
            _beep(root / "assets" / "audio" / lang / f"s0{i + 1}.wav", s, 440 if lang == "vi" else 660)
    return root


def _beep(path: Path, seconds: float, freq: int, rate: int = config.TTS_SAMPLE_RATE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = int(seconds * rate)
    samples = bytearray()
    for k in range(n):
        on = (k // (rate // 4)) % 2 == 0  # bíp 0,25s rồi nghỉ 0,25s
        v = int(8000 * math.sin(2 * math.pi * freq * k / rate)) if on else 0
        samples += v.to_bytes(2, "little", signed=True)
    with wave.open(str(path), "wb") as wv:
        wv.setnchannels(1)
        wv.setsampwidth(2)
        wv.setframerate(rate)
        wv.writeframes(bytes(samples))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path, nargs="?")
    p.add_argument("--music", type=Path, help="nhạc nền không bản quyền (ví dụ từ YouTube Audio Library)")
    p.add_argument("--demo", action="store_true")
    p.add_argument("--draft", action="store_true", help="bản nháp không tiếng 960×540 khi chưa có giọng đọc")
    args = p.parse_args()

    video_dir = make_demo(config.CACHE_DIR / "demo") if args.demo else args.video_dir
    if not video_dir:
        p.error("cần video_dir hoặc --demo")
    if args.draft:
        final = run(video_dir, music=args.music, size=DRAFT_SIZE, fps=DRAFT_FPS, draft=True, crf=DRAFT_CRF)
    else:
        final = run(video_dir, music=args.music)
    info = media.probe(final)
    print(f"\nXong: {final} ({info.duration_s:.1f}s)")
    report = json.loads((final.parent / "report.json").read_text(encoding="utf-8"))
    print(report["languages"])
    if report["length_problem"] and not args.demo:
        print(f"CẢNH BÁO: {report['length_problem']}")


if __name__ == "__main__":
    main()
