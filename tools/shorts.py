"""Short dọc 1080×1920 cắt từ video dài: dùng lại ảnh và giọng của một cụm cảnh liền nhau.

    python -m tools.shorts suggest videos/<thư-mục>                     # gợi ý 3 cụm cảnh 35–58 giây
    python -m tools.shorts make videos/<thư-mục> --from s12 --to s17     # render/shorts/s12-s17.mp4
    python -m tools.shorts make videos/<thư-mục> --from s12 --to s17 --title "Vì sao Gon mất Nen?"

Bố cục: nền là chính ảnh cảnh đó phóng to và làm mờ; ảnh 16:9 đặt giữa, có chuyển động nhẹ; dải tên kênh và
tiêu đề ở trên; phụ đề chữ to in thẳng vào hình ở dưới (nhiều người xem Shorts không bật tiếng).
"""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from tools import assemble, config, media, scenes, timing

SIZE = (1080, 1920)
MIN_S, MAX_S = 35.0, 58.0
CHANNEL_TAG = "CÚ KAKU · GIẢI MÃ ANIME"
CTA = "Bản đầy đủ trên kênh"
AMBER = (240, 180, 58, 255)
WHITE = (255, 255, 255, 255)
TWISTS = ("Nhưng", "Thật ra", "Hóa ra", "Và đây mới là", "Khoan đã")


@dataclass
class Pick:
    first: str
    last: str
    seconds: float
    title: str
    score: int


def speech_seconds(board: scenes.Storyboard, video_dir: Path | None = None) -> list[float]:
    """Độ dài giọng mỗi cảnh: đo từ WAV nếu đã có, không thì ước tính theo số ký tự."""
    lang = config.PRIMARY_LANGUAGE
    out = []
    for s in board.scenes:
        wav = Path(video_dir) / "assets" / "audio" / lang / f"{s.id}.wav" if video_dir else None
        out.append(media.wav_duration(wav) if wav and wav.exists() else len(s.narration[lang]) / config.CHARS_PER_SECOND[lang])
    return out


def suggest(board: scenes.Storyboard, speech: list[float], n: int = 3, min_s: float = MIN_S, max_s: float = MAX_S) -> list[Pick]:
    """Mỗi chương cho một cụm cảnh từ đầu chương, dài min_s–max_s. Ưu tiên cụm mở bằng câu hỏi và có điểm bất ngờ."""
    lang = config.PRIMARY_LANGUAGE
    durations = timing.scene_durations(speech)
    picks = []
    for i, s in enumerate(board.scenes):
        if not s.chapter or i == 0:  # bỏ chương mở đầu (cảnh báo spoiler, lời chào)
            continue
        total, j = 0.0, i
        while j < len(board.scenes) and total + durations[j] <= max_s and (j == i or not board.scenes[j].chapter):
            total += durations[j]
            j += 1
        if total < min_s:
            continue
        members = board.scenes[i:j]
        text = " ".join(m.narration[lang] for m in members)
        score = 2 * ("?" in members[0].narration[lang]) + any(t in text for t in TWISTS)
        picks.append(Pick(members[0].id, members[-1].id, round(total, 1), s.chapter, score))
    best = sorted(picks, key=lambda p: -p.score)[:n]
    return sorted(best, key=lambda p: board.scenes.index(next(x for x in board.scenes if x.id == p.first)))


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(assemble.FONT), size)


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        if lines and draw.textlength(f"{lines[-1]} {word}", font=font) <= max_w:
            lines[-1] = f"{lines[-1]} {word}"
        else:
            lines.append(word)
    return lines


def _centered(draw, lines, font, y, w, fill, stroke):
    line_h = int(font.size * 1.25)
    for k, line in enumerate(lines):
        x = (w - draw.textlength(line, font=font)) / 2
        draw.text((x, y + k * line_h), line, font=font, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    return y + len(lines) * line_h


def render_header(title: str, out: Path, size: tuple[int, int]) -> None:
    """Tên kênh + tiêu đề ở trên, lời mời xem bản đầy đủ ở dưới; nền trong suốt."""
    w, h = size
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    tag, head, cta = _font(max(10, int(w * 0.035))), _font(max(12, int(w * 0.068))), _font(max(10, int(w * 0.04)))
    y = _centered(draw, [CHANNEL_TAG], tag, int(h * 0.075), w, AMBER, max(1, w // 360))
    _centered(draw, _wrap(draw, title, head, int(w * 0.88))[:3], head, y + int(h * 0.012), w, WHITE, max(2, w // 200))
    _centered(draw, [CTA], cta, int(h * 0.9), w, AMBER, max(1, w // 360))
    img.save(out)


def render_caption(text: str, out: Path, size: tuple[int, int]) -> None:
    """Phụ đề chữ to, viền đen, đặt dưới ảnh chính."""
    w, h = size
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = _font(max(12, int(w * 0.062)))
    lines = _wrap(draw, text, font, int(w * 0.86))
    _centered(draw, lines, font, int(h * 0.64), w, WHITE, max(2, w // 180))
    img.save(out)


def caption_windows(text: str, speech_s: float, seg_s: float, max_chars: int = 34) -> list[tuple[str, float, float]]:
    """Chia lời thoại thành các dòng ngắn, thời gian tỉ lệ số ký tự; dòng cuối kéo tới hết cảnh."""
    pieces = timing.split_caption(text, max_chars=max_chars)
    total = sum(len(p) for p in pieces) or 1
    out, t = [], 0.0
    for k, p in enumerate(pieces):
        end = seg_s if k == len(pieces) - 1 else t + speech_s * len(p) / total
        out.append((p, round(t, 3), round(end, 3)))
        t = end
    return out


def render_short_segment(
    image: Path, header: Path, captions: list[tuple[Path, float, float]], frames: int, index: int,
    out: Path, size: tuple[int, int], fps: int,
) -> None:
    w, h = size
    fg_w, fg_h = w, int(round(w * 9 / 16 / 2)) * 2
    fg_y = int(h * 0.30)
    dur = frames / fps
    args = ["-loop", "1", "-framerate", str(fps), "-t", f"{dur:.3f}", "-i", str(image), "-i", str(image), "-i", str(header)]
    for png, _, _ in captions:
        args += ["-i", str(png)]
    chain = (
        f"[0:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},boxblur=20:2,eq=brightness=-0.18[bg];"
        f"[1:v]scale={2 * fg_w}:{2 * fg_h},zoompan={assemble.ken_burns(index, frames)}:d={frames}:s={fg_w}x{fg_h}:fps={fps}[fg];"
        f"[bg][fg]overlay=0:{fg_y}[v0];[v0][2:v]overlay=0:0[v1]"
    )
    last = "v1"
    for k, (_, a, b) in enumerate(captions):
        chain += f";[{last}][{k + 3}:v]overlay=0:0:enable='between(t,{a},{b})'[c{k}]"
        last = f"c{k}"
    chain += f";[{last}]format=yuv420p[v]"
    media.run_ffmpeg(
        [*args, "-filter_complex", chain, "-map", "[v]", "-frames:v", str(frames),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(fps), str(out)]
    )


def make(
    video_dir: Path, first: str, last: str, title: str = "", size: tuple[int, int] = SIZE, fps: int = config.FPS,
    draft: bool = False,
) -> Path:
    video_dir = Path(video_dir)
    board = scenes.load(video_dir)
    ids = [s.id for s in board.scenes]
    if first not in ids or last not in ids or ids.index(first) > ids.index(last):
        raise SystemExit(f"cụm cảnh không hợp lệ: {first}–{last}")
    members = board.scenes[ids.index(first) : ids.index(last) + 1]
    lang = config.PRIMARY_LANGUAGE
    assets = video_dir / "assets"
    out_dir = video_dir / "render" / "shorts"
    tmp = out_dir / f"tmp-{first}-{last}"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)

    images = [assets / "images" / f"{s.id}.png" for s in members]
    if draft:
        audio = assemble.silent_wavs(assemble.draft_speech_seconds(scenes.Storyboard("", [lang], members)), [s.id for s in members], tmp)
    else:
        audio = [assets / "audio" / lang / f"{s.id}.wav" for s in members]
    missing = [str(p) for p in images + audio if not p.exists()]
    if missing:
        raise SystemExit("Thiếu file:\n- " + "\n- ".join(missing))

    speech = [media.wav_duration(p) for p in audio]
    durations = timing.scene_durations(speech)
    frames = assemble.frame_counts(durations, fps)
    header = tmp / "header.png"
    render_header(title or members[0].chapter or board.title, header, size)
    segments = []
    for i, (s, img) in enumerate(zip(members, images)):
        caps = []
        for k, (text, a, b) in enumerate(caption_windows(s.narration[lang], speech[i], frames[i] / fps)):
            png = tmp / f"cap_{i:02d}_{k:02d}.png"
            render_caption(text, png, size)
            caps.append((png, a, b))
        seg = tmp / f"seg_{i:02d}.mp4"
        render_short_segment(img, header, caps, frames[i], i, seg, size, fps)
        segments.append(seg)
    concat = tmp / "segments.txt"
    concat.write_text("".join(f"file '{s.name}'\n" for s in segments), encoding="utf-8")
    silent = tmp / "video_only.mp4"
    media.run_ffmpeg(["-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(silent)])
    track = tmp / "track.wav"
    media.concat_wavs_exact(audio, durations, track)
    final = out_dir / f"{first}-{last}.mp4"
    total = round(sum(durations), 3)
    assemble.encode_audio(track, final, total, None, video=silent)
    (out_dir / f"{first}-{last}.json").write_text(
        json.dumps({"scenes": [s.id for s in members], "seconds": total, "title": title or members[0].chapter}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.rmtree(tmp, ignore_errors=True)
    if total > 60:
        print(f"CẢNH BÁO: Short dài {total:.0f} giây, nên dưới 60 giây.")
    return final


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("suggest")
    s.add_argument("video_dir", type=Path)
    s.add_argument("-n", type=int, default=3)
    m = sub.add_parser("make")
    m.add_argument("video_dir", type=Path)
    m.add_argument("--from", dest="first", required=True)
    m.add_argument("--to", dest="last", required=True)
    m.add_argument("--title", default="", help="tiêu đề in trên Short (mặc định: tên chương)")
    m.add_argument("--draft", action="store_true", help="không tiếng, khi chưa có giọng")
    args = p.parse_args()

    if args.cmd == "suggest":
        board = scenes.load(args.video_dir)
        for pick in suggest(board, speech_seconds(board, args.video_dir), args.n):
            print(f"{pick.first}–{pick.last}  {pick.seconds:>4.0f}s  {pick.title}")
        return
    print(make(args.video_dir, args.first, args.last, args.title, draft=args.draft))


if __name__ == "__main__":
    main()
