"""Kiểm một video trước khi đăng: bản render, phụ đề, chương, thumbnail, metadata, nguồn, giấy phép giọng.

    python -m tools.release_check videos/<thư-mục>
    python -m tools.release_check videos/<thư-mục> --no-loudness   # bỏ đo độ to (nhanh hơn)

Mỗi mục có một trong ba mức: ĐẠT, LƯU Ý, LỖI. Còn LỖI thì lệnh trả mã 1 và
chưa được đăng. Cuối cùng là danh sách việc phải tự làm trong YouTube Studio.

Giới hạn của YouTube dùng ở đây:
- tiêu đề tối đa 100 ký tự;
- mô tả tối đa 5.000 ký tự;
- tag tổng cộng tối đa 500 ký tự;
- quá 15 hashtag thì YouTube bỏ qua tất cả;
- thumbnail tối đa 2 MB, nên 1280×720;
- chương: mốc đầu 0:00, ít nhất 3 chương, mỗi chương từ 10 giây.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from tools import canon, config, media, voicestudio

OK, WARN, FAIL = "ĐẠT", "LƯU Ý", "LỖI"
AI_LINE = "Hình minh họa do AI tạo"
TITLE_MAX, TITLE_CHANNEL_MAX = 100, 60
DESC_MAX = 5000
TAGS_MAX = 500
HASHTAG_MAX = 15
THUMB_MAX_BYTES = 2 * 1024 * 1024
LOUDNESS_RANGE = (-16.0, -12.0)  # YouTube chuẩn hóa quanh -14 LUFS
MANUAL = [
    "Quyết định nhãn 'Altered or synthetic content' (xem mục Nội dung AI trong metadata).",
    "Đặt lịch đăng đúng ngày trong channel/topics.md, chọn thumbnail, gắn phụ đề subs.vi.srt.",
    "Thêm màn hình kết thúc và thẻ tới video liên quan; ghim bình luận câu hỏi cho người xem.",
    "Nếu giọng làm bằng ElevenLabs: chỉ gói trả phí mới được dùng thương mại.",
    "Sau khi đăng: python -m tools.costs record, cập nhật Notion và channel/topics.md.",
]


@dataclass
class Check:
    name: str
    level: str
    detail: str


def srt_seconds(ts: str) -> float:
    h, m, rest = ts.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(text: str) -> list[tuple[float, float, list[str]]]:
    cues = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.strip().splitlines()
        if len(lines) >= 2 and "-->" in lines[1]:
            a, b = [x.strip() for x in lines[1].split("-->")]
            cues.append((srt_seconds(a), srt_seconds(b), lines[2:]))
    return cues


def chapter_seconds(ts: str) -> int:
    parts = [int(x) for x in ts.split(":")]
    return sum(v * 60**i for i, v in enumerate(reversed(parts)))


def parse_chapters(text: str) -> list[tuple[int, str]]:
    out = []
    for line in text.splitlines():
        m = re.match(r"^(\d+(?::\d{2}){1,2})\s+(.+)$", line.strip())
        if m:
            out.append((chapter_seconds(m.group(1)), m.group(2)))
    return out


def metadata_sections(text: str) -> dict[str, str]:
    """{tên mục viết thường: nội dung} theo các tiêu đề '## ' trong metadata.<lang>.md."""
    sections: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip().lower()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items()}


def _section(sections: dict[str, str], prefix: str) -> str | None:
    for k, v in sections.items():
        if k.startswith(prefix):
            return v
    return None


def loudness(path: Path) -> float | None:
    """Độ to tích hợp (LUFS) đo bằng bộ lọc ebur128 của ffmpeg."""
    cmd = [media.ffmpeg_exe(), "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af", "ebur128", "-f", "null", "-"]
    text = subprocess.run(cmd, capture_output=True, text=True).stderr
    found = re.findall(r"I:\s+(-?\d+(?:\.\d+)?) LUFS", text)
    return float(found[-1]) if found else None


def check_render(video_dir: Path, lang: str, measure_loudness: bool) -> tuple[list[Check], float | None]:
    render = video_dir / "render"
    out: list[Check] = []
    video = render / f"video.{lang}.mp4"
    if not video.exists():
        draft = render / f"draft.{lang}.mp4"
        hint = " (chỉ có bản nháp không tiếng)" if draft.exists() else ""
        return [Check("Bản render", FAIL, f"thiếu {video.relative_to(video_dir)}{hint}; chạy python -m tools.assemble")], None
    info = media.probe(video)
    minutes = info.duration_s / 60
    lo, hi = config.MIN_VIDEO_MINUTES, config.MAX_VIDEO_MINUTES
    out.append(Check("Độ dài", OK if lo <= minutes <= hi else FAIL, f"{minutes:.1f} phút (cần {lo}–{hi})"))
    desc = info.video[0] if info.video else ""
    size = re.search(r"(\d{3,5})x(\d{3,5})", desc)
    fps = re.search(r"(\d+(?:\.\d+)?) fps", desc)
    if size and (int(size.group(1)), int(size.group(2))) == (config.WIDTH, config.HEIGHT):
        out.append(Check("Khung hình", OK, f"{size.group(1)}×{size.group(2)}"))
    else:
        out.append(Check("Khung hình", FAIL, f"{size.group(0) if size else '?'} (cần {config.WIDTH}×{config.HEIGHT})"))
    if fps and abs(float(fps.group(1)) - config.FPS) > 0.5:
        out.append(Check("Số hình/giây", WARN, f"{fps.group(1)} fps (thường là {config.FPS})"))
    out.append(Check("Âm thanh", OK if info.audio else FAIL, "có" if info.audio else "video không có tiếng"))
    report = render / "report.json"
    if report.exists():
        rep = json.loads(report.read_text(encoding="utf-8"))
        if rep.get("draft"):
            out.append(Check("report.json", FAIL, "lần dựng gần nhất là bản nháp; dựng lại bản đầy đủ"))
        elif rep.get("length_problem"):
            out.append(Check("report.json", FAIL, rep["length_problem"]))
    if measure_loudness and info.audio:
        lufs = loudness(video)
        if lufs is None:
            out.append(Check("Độ to", WARN, "không đo được"))
        else:
            ok = LOUDNESS_RANGE[0] <= lufs <= LOUDNESS_RANGE[1]
            out.append(Check("Độ to", OK if ok else WARN, f"{lufs:.1f} LUFS (nên từ {LOUDNESS_RANGE[0]:.0f} tới {LOUDNESS_RANGE[1]:.0f})"))
    return out, info.duration_s


def check_subs(video_dir: Path, lang: str, duration: float | None) -> list[Check]:
    srt = video_dir / "render" / f"subs.{lang}.srt"
    if not srt.exists():
        return [Check("Phụ đề", FAIL, f"thiếu render/subs.{lang}.srt")]
    cues = parse_srt(srt.read_text(encoding="utf-8"))
    if not cues:
        return [Check("Phụ đề", FAIL, "file phụ đề rỗng")]
    problems = []
    if duration and not (duration - 30 <= cues[-1][1] <= duration + 1):
        problems.append(f"dòng cuối kết thúc ở {cues[-1][1]:.0f}s, video dài {duration:.0f}s")
    long_cues = [i + 1 for i, (_, _, lines) in enumerate(cues) if len(lines) > 2 or any(len(x) > 84 for x in lines)]
    if long_cues:
        problems.append(f"{len(long_cues)} dòng quá dài (ví dụ dòng {long_cues[0]})")
    return [Check("Phụ đề", WARN if problems else OK, "; ".join(problems) or f"{len(cues)} dòng")]


def check_chapters(video_dir: Path) -> list[Check]:
    path = video_dir / "render" / "chapters.txt"
    if not path.exists():
        return [Check("Chương", FAIL, "thiếu render/chapters.txt")]
    chapters = parse_chapters(path.read_text(encoding="utf-8"))
    problems = []
    if not chapters or chapters[0][0] != 0:
        problems.append("mốc đầu phải là 0:00")
    if len(chapters) < 3:
        problems.append(f"chỉ có {len(chapters)} chương (cần ít nhất 3)")
    gaps = [b[1] for a, b in zip(chapters, chapters[1:]) if b[0] - a[0] < 10]
    if gaps:
        problems.append(f"chương ngắn hơn 10 giây trước '{gaps[0]}'")
    return [Check("Chương", FAIL if problems else OK, "; ".join(problems) or f"{len(chapters)} chương")]


def check_thumbnail(video_dir: Path) -> list[Check]:
    path = video_dir / "render" / "thumbnail.png"
    if not path.exists():
        return [Check("Thumbnail", FAIL, "thiếu render/thumbnail.png; chạy python -m tools.thumbnail")]
    with Image.open(path) as im:
        w, h = im.size
    if path.stat().st_size > THUMB_MAX_BYTES:
        return [Check("Thumbnail", FAIL, f"{path.stat().st_size / 1e6:.1f} MB (tối đa 2 MB)")]
    if (w, h) != (1280, 720):
        return [Check("Thumbnail", WARN, f"{w}×{h} (nên 1280×720)")]
    return [Check("Thumbnail", OK, "1280×720")]


def check_metadata(video_dir: Path, lang: str) -> list[Check]:
    path = video_dir / f"metadata.{lang}.md"
    if not path.exists():
        return [Check("Metadata", FAIL, f"thiếu metadata.{lang}.md (khuôn trong skill yt-studio, mục 6)")]
    s = metadata_sections(path.read_text(encoding="utf-8"))
    out: list[Check] = []

    titles = [re.sub(r"^\d+[.)]\s*", "", x).strip() for x in (_section(s, "tiêu đề") or "").splitlines()]
    titles = [t for t in titles if t and not t.lower().startswith("chọn")]
    if not titles:
        out.append(Check("Tiêu đề", FAIL, "mục '## Tiêu đề' trống"))
    else:
        longest = max(len(t) for t in titles)
        level = FAIL if longest > TITLE_MAX else WARN if longest > TITLE_CHANNEL_MAX else OK
        out.append(Check("Tiêu đề", level, f"{len(titles)} phương án, dài nhất {longest} ký tự (kênh ≤ {TITLE_CHANNEL_MAX}, YouTube ≤ {TITLE_MAX})"))

    desc = _section(s, "mô tả")
    if not desc:
        out.append(Check("Mô tả", FAIL, "mục '## Mô tả' trống"))
    else:
        problems, level = [], OK
        if len(desc) > DESC_MAX:
            problems.append(f"{len(desc)} ký tự (tối đa {DESC_MAX})")
            level = FAIL
        if AI_LINE not in desc:
            problems.append(f"thiếu dòng '{AI_LINE}…'")
            level = FAIL
        if "http" not in desc:
            problems.append("thiếu link nguồn tham khảo")
            level = FAIL
        if not re.search(r"(?m)^0:00\s", desc):
            problems.append("chưa dán danh sách chương (dòng bắt đầu bằng 0:00)")
            level = level if level == FAIL else WARN
        out.append(Check("Mô tả", level, "; ".join(problems) or f"{len(desc)} ký tự"))

    tags = [t.strip() for t in re.split(r"[,\n]", _section(s, "tag") or "") if t.strip()]
    tag_chars = sum(len(t) for t in tags) + max(len(tags) - 1, 0)
    if not tags:
        out.append(Check("Tag", WARN, "chưa có tag"))
    else:
        level = FAIL if tag_chars > TAGS_MAX else OK if 10 <= len(tags) <= 15 else WARN
        out.append(Check("Tag", level, f"{len(tags)} tag, {tag_chars} ký tự (tối đa {TAGS_MAX}; kênh dùng 10–15 tag)"))

    hashtags = re.findall(r"#\w+", _section(s, "hashtag") or "")
    if len(hashtags) > HASHTAG_MAX:
        out.append(Check("Hashtag", FAIL, f"{len(hashtags)} hashtag (quá {HASHTAG_MAX} thì YouTube bỏ qua tất cả)"))
    else:
        out.append(Check("Hashtag", OK if len(hashtags) == 3 else WARN, f"{len(hashtags)} hashtag (kênh dùng 3)"))

    ai = _section(s, "nội dung ai")
    out.append(Check("Khai báo AI", OK if ai else FAIL, ai.splitlines()[0][:80] if ai else "thiếu mục '## Nội dung AI' ghi quyết định tick hay không"))
    return out


def check_sources(video_dir: Path) -> list[Check]:
    open_claims = canon.check(video_dir)
    if open_claims:
        return [Check("Nguồn (canon)", FAIL, f"còn {len(open_claims)} khẳng định chưa kiểm; python -m tools.canon check {video_dir}")]
    return [Check("Nguồn (canon)", OK, "mọi khẳng định đã có nguồn")]


def check_voice_license(video_dir: Path) -> list[Check]:
    cost = video_dir / "cost.json"
    usage = json.loads(cost.read_text(encoding="utf-8")) if cost.exists() else {}
    if usage.get("tts_local_seconds"):
        engine = voicestudio.settings()["engine"]
        if engine in voicestudio.LICENSE_OK:
            return [Check("Giấy phép giọng", OK, f"VoiceStudio · {engine}: {voicestudio.LICENSE_OK[engine]}")]
        return [Check("Giấy phép giọng", FAIL, f"VoiceStudio · engine '{engine}' chưa được xác nhận cho kênh kiếm tiền")]
    if usage.get("tts_app_seconds"):
        return [Check("Giấy phép giọng", WARN, "giọng làm tay (AI Studio / ElevenLabs): xác nhận điều khoản thương mại của gói đang dùng")]
    if usage.get("tts_seconds"):
        return [Check("Giấy phép giọng", OK, "Gemini TTS qua API")]
    return [Check("Giấy phép giọng", WARN, "cost.json chưa ghi giọng được tạo bằng gì")]


def check_shorts(video_dir: Path) -> list[Check]:
    n = len(list((video_dir / "render" / "shorts").glob("*.mp4")))
    return [Check("Short", OK if n >= 3 else WARN, f"{n}/3 Short trong render/shorts/")]


def run(video_dir: Path, lang: str = config.PRIMARY_LANGUAGE, measure_loudness: bool = True) -> list[Check]:
    video_dir = Path(video_dir)
    checks, duration = check_render(video_dir, lang, measure_loudness)
    checks += check_subs(video_dir, lang, duration)
    checks += check_chapters(video_dir)
    checks += check_thumbnail(video_dir)
    checks += check_shorts(video_dir)
    checks += check_metadata(video_dir, lang)
    checks += check_sources(video_dir)
    checks += check_voice_license(video_dir)
    return checks


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path)
    p.add_argument("--lang", default=config.PRIMARY_LANGUAGE, choices=sorted(config.LANGUAGES))
    p.add_argument("--no-loudness", action="store_true", help="bỏ đo độ to")
    args = p.parse_args()
    checks = run(args.video_dir, args.lang, not args.no_loudness)
    width = max(len(c.name) for c in checks)
    for c in checks:
        print(f"[{c.level:^6}] {c.name:<{width}}  {c.detail}")
    fails = [c for c in checks if c.level == FAIL]
    print("\nViệc tự làm trong YouTube Studio:")
    for item in MANUAL:
        print(f"  - [ ] {item}")
    if fails:
        print(f"\nCHƯA ĐƯỢC ĐĂNG: còn {len(fails)} lỗi.")
        sys.exit(1)
    print("\nKhông còn lỗi. Gửi video cho người dùng duyệt lần cuối.")


if __name__ == "__main__":
    main()
