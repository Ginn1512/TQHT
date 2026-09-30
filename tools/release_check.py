"""Cổng đăng của một video: bản render, phụ đề, chương, thumbnail, metadata, nguồn, quyền tài sản,
độ nguyên bản, khai báo AI và quyết định của người duyệt (audit.md).

    python -m tools.release_check videos/<thư-mục>
    python -m tools.release_check videos/<thư-mục> --no-loudness   # bỏ đo độ to (nhanh hơn)
    python -m tools.release_check videos/<thư-mục> --write-audit   # tạo / cập nhật audit.md cho người duyệt

Mỗi mục có một trong ba mức: ĐẠT, LƯU Ý, LỖI. Còn LỖI thì lệnh trả mã 1 và
chưa được đăng. Cuối cùng là danh sách việc phải tự làm trong YouTube Studio.

audit.md theo khuôn "Pre-publish audit" của tài liệu Policy Safe. Máy điền phần nguồn, quyền,
điểm nguyên bản, rủi ro và gợi ý khai báo AI; người điền đóng góp sáng tạo, người duyệt cuối và
quyết định. Chưa có "Decision: publish" thì chưa được đăng.

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
import datetime as dt
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image

from tools import canon, config, media, originality, rights, scenes, voicestudio

OK, WARN, FAIL = "ĐẠT", "LƯU Ý", "LỖI"
AI_LINE = "Hình minh họa do AI tạo"
TITLE_MAX, TITLE_CHANNEL_MAX = 100, 60
DESC_MAX = 5000
TAGS_MAX = 500
HASHTAG_MAX = 15
THUMB_MAX_BYTES = 2 * 1024 * 1024
LOUDNESS_RANGE = (-16.0, -12.0)  # YouTube chuẩn hóa quanh -14 LUFS
MANUAL = [
    "Quyết định nhãn 'Altered or synthetic content' theo gợi ý trong audit.md và mục Nội dung AI của metadata.",
    "Đặt lịch đăng đúng ngày và giờ trong channel/topics.md (múi giờ GMT+7), chọn thumbnail, gắn phụ đề subs.vi.srt.",
    "Thêm màn hình kết thúc và thẻ tới video liên quan; ghim bình luận câu hỏi cho người xem.",
    "Nếu giọng làm bằng ElevenLabs: chỉ gói trả phí mới được dùng thương mại.",
    "Nếu có nhạc nền: đã thêm dòng music vào rights.csv (tên bài, link, giấy phép).",
    "Tiêu đề và thumbnail không dùng người nổi tiếng, sự kiện hay cảnh không có trong video.",
    "Lời kêu gọi không thao túng: không hứa thưởng, không dọa, không đổi like lấy nội dung.",
    "Không mua view, like, bình luận hay người đăng ký; không dùng bot hay nhóm tương tác chéo.",
    "Sau khi đăng: python -m tools.costs record, cập nhật Notion và channel/topics.md.",
]
# Tiêu đề câu kéo: hứa điều video không có, hoặc la hét bằng chữ hoa.
CLICKBAIT = re.compile(
    r"\bsốc\b|gây sốc|không thể tin|khó tin|100\s?%|chắc chắn 100|bí mật động trời|không ai biết|"
    r"sự thật kinh hoàng|\bshock|!{2,}",
    re.I,
)
CAPS_RATIO = 0.5
SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "shorturl.at", "cutt.ly", "rb.gy", "is.gd", "ow.ly"}
AFFILIATE = re.compile(
    r"[?&](?:ref|aff|affiliate|tag|utm_source)=|amzn\.to|shope\.ee|shopee\.vn|lazada\.vn|tiki\.vn|"
    r"\baffiliate\b|\bsponsor|được tài trợ|nhà tài trợ|mã giảm giá",
    re.I,
)
DISCLOSE_LINE = re.compile(r"(?im)^\s*tiết lộ\s*:")
# Từ chỉ ảnh chân thực trong prompt. "photo" đơn lẻ không tính vì hay là tấm ảnh vẽ trong tranh.
PHOTOREAL = re.compile(
    r"photo-?realis\w*|hyper-?realis\w*|realistic photo|real photograph|live[- ]action|documentary footage|"
    r"news footage|\bdslr\b|35mm film|real (?:person|people)|celebrity|likeness of",
    re.I,
)
REAL_WORLD_FORMATS = {"S": "dạng S nói về người, nơi chốn hay sự kiện có thật"}
AUDIT_NAME = "audit.md"
AUDIT_HUMAN = ("Owner", "Human creative contribution", "Disclosure completed", "Final reviewer", "Decision", "Reasons")
DECISIONS = ("publish", "revise", "reject")


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
    out += check_title_policy(titles)
    out += check_links(desc or "")
    return out


def check_title_policy(titles: list[str]) -> list[Check]:
    """Tiêu đề phản ánh đúng nội dung: không từ câu kéo, không la hét bằng chữ hoa."""
    problems = []
    for title in titles:
        bait = CLICKBAIT.search(title)
        letters = [c for c in title if c.isalpha()]
        caps = sum(c.isupper() for c in letters) / len(letters) if len(letters) >= 10 else 0.0
        if bait:
            problems.append(f"'{title[:40]}' có '{bait.group(0)}'")
        elif caps > CAPS_RATIO:
            problems.append(f"'{title[:40]}' {caps:.0%} chữ hoa")
    if problems:
        return [Check("Tiêu đề câu kéo", WARN, "; ".join(problems[:3]) + " (tiêu đề phải khớp nội dung)")]
    return [Check("Tiêu đề câu kéo", OK, "không có từ câu kéo")]


def check_links(desc: str) -> list[Check]:
    """Link ngoài an toàn và rõ đích; có link tiếp thị liên kết hay tài trợ thì phải có dòng 'Tiết lộ:'."""
    out: list[Check] = []
    urls = re.findall(r"https?://[^\s)>\]]+", desc)
    plain = [u for u in urls if u.startswith("http://")]
    short = [u for u in urls if urlparse(u).netloc.lower().removeprefix("www.") in SHORTENERS]
    problems = []
    if plain:
        problems.append(f"{len(plain)} link không phải https")
    if short:
        problems.append(f"{len(short)} link rút gọn che đích đến")
    out.append(Check("Link ngoài", WARN if problems else OK, "; ".join(problems) or f"{len(urls)} link, đều https"))
    if AFFILIATE.search(desc) and not DISCLOSE_LINE.search(desc):
        out.append(Check("Tiết lộ tài trợ", FAIL, "mô tả có link tiếp thị liên kết hoặc tài trợ nhưng thiếu dòng 'Tiết lộ: …'"))
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


def check_rights(video_dir: Path) -> list[Check]:
    if not (Path(video_dir) / "scenes.json").exists():
        return [Check("Quyền tài sản", FAIL, "thiếu scenes.json nên chưa lập được rights.csv")]
    points, issues = rights.check(video_dir)
    fails = [msg for level, msg in issues if level == rights.FAIL]
    out = [Check("Quyền tài sản", FAIL if fails else OK, "; ".join(fails[:3]) or f"mọi dòng trong {rights.LEDGER_NAME} đã kiểm")]
    out += [Check("Quyền tài sản", WARN, msg) for level, msg in issues if level == rights.WARN]
    return out


def check_originality(video_dir: Path) -> list[Check]:
    if not (Path(video_dir) / "scenes.json").exists():
        return [Check("Độ nguyên bản", FAIL, "thiếu scenes.json")]
    result = originality.evaluate(video_dir)
    pending = [k for k, c in result["criteria"].items() if c["points"] is None]
    head = f"{result['total']}/{result['max']} · {result['verdict']}"
    if result["verdict"] == originality.PASS:
        return [Check("Độ nguyên bản", OK, head)]
    if pending:
        return [Check("Độ nguyên bản", FAIL, f"{head}: chưa chấm {', '.join(pending)} (python -m tools.originality score)")]
    low = [k for k, c in result["criteria"].items() if c["points"] == 0]
    return [Check("Độ nguyên bản", FAIL, f"{head}; tiêu chí 0 điểm: {', '.join(low) or 'không'}")]


def disclosure(video_dir: Path) -> dict:
    """Gợi ý khai báo 'Altered or synthetic content' theo tài liệu Policy Safe (khối YAML ai_disclosure).

    Không cần khai báo: tranh cách điệu rõ ràng, sơ đồ tự dựng, giọng tổng hợp không mạo danh.
    Cần xem xét khai báo: cảnh trông như thật, người thật hay sự kiện thật bị mô phỏng.
    """
    video_dir = Path(video_dir)
    reasons = []
    brief = video_dir / "brief.md"
    code = originality.brief_field(brief.read_text(encoding="utf-8"), "Dạng video")[:1] if brief.exists() else ""
    if code in REAL_WORLD_FORMATS:
        reasons.append(REAL_WORLD_FORMATS[code])
    if (video_dir / "scenes.json").exists():
        board = scenes.load(video_dir)
        prompts = [board.style_prompt] + [f"{s.image_prompt} {s.video_prompt}" for s in board.scenes]
        hits = sorted({m.group(0).lower() for p in prompts for m in PHOTOREAL.finditer(p)})
        if hits:
            reasons.append(f"prompt có từ chỉ ảnh chân thực: {', '.join(hits)}")
    required = bool(reasons)
    return {
        "ai_used": True,
        "realistic_or_meaningfully_altered": required,
        "youtube_studio_altered_content": "yes" if required else "no",
        "reason": "; ".join(reasons) or "tranh minh họa cách điệu kiểu sổ tay, sơ đồ tự dựng, giọng tổng hợp không mạo danh",
        "viewer_note": "Hình minh họa trong video do AI tạo, không phải hình chính thức.",
    }


def check_disclosure(video_dir: Path, lang: str = config.PRIMARY_LANGUAGE) -> list[Check]:
    hint = disclosure(video_dir)
    meta = Path(video_dir) / f"metadata.{lang}.md"
    chosen = _section(metadata_sections(meta.read_text(encoding="utf-8")), "nội dung ai") if meta.exists() else None
    ticked = bool(chosen) and not re.match(r"\s*không", chosen, re.I)
    if hint["realistic_or_meaningfully_altered"] and chosen and not ticked:
        return [Check("Gợi ý khai báo AI", WARN, f"nên tick: {hint['reason']}")]
    return [Check("Gợi ý khai báo AI", OK, ("tick" if hint["realistic_or_meaningfully_altered"] else "không cần tick") + f": {hint['reason']}")]


def cadence(video_dir: Path, topics: Path | None = None) -> int | None:
    """Số video đăng cùng ngày với video này theo channel/topics.md (None nếu không có trong lịch)."""
    numbers = canon.video_numbers(topics or canon.TOPICS)
    if Path(video_dir).name not in numbers:
        return None
    day = numbers[Path(video_dir).name][1]
    return Counter(d for _, d in numbers.values())[day]


def _risk(result: dict, per_day: int | None) -> tuple[str, str, str, str]:
    """(rủi ro nội dung dùng lại, lý do, rủi ro không chân thực, lý do)."""
    total, pending = result["total"], result["verdict"] == originality.PENDING
    if pending or total < originality.GATE:
        reused = ("high", "điểm nguyên bản chưa đủ hoặc chưa chấm đủ")
    elif total < originality.STRONG:
        reused = ("medium", f"điểm nguyên bản {total}/16, dưới {originality.STRONG}")
    else:
        reused = ("low", f"điểm nguyên bản {total}/16, kịch bản và hình do kênh tự làm")
    distinct = result["criteria"]["khac-nhau"]
    if per_day and per_day > 1:
        inauth = ("high", f"nhịp {per_day} video/ngày cùng một khuôn dạng dễ bị xem là sản xuất hàng loạt")
    elif pending or total < originality.STRONG:
        inauth = ("high", f"điểm nguyên bản {total}/16, dưới {originality.STRONG}")
    elif distinct["points"] < 2:
        inauth = ("medium", distinct["evidence"])
    else:
        inauth = ("low", "nhịp tối đa 1 video/ngày, nội dung cốt lõi khác các video khác")
    return reused[0], reused[1], inauth[0], inauth[1]


def parse_audit(text: str) -> dict[str, str]:
    """{khóa: giá trị} của các dòng "- Khóa: giá trị" trong audit.md."""
    out = {}
    for line in text.splitlines():
        m = re.match(r"^- ([A-Za-z][A-Za-z -]+):\s*(.*)$", line)
        if m and m.group(1) not in out:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def write_audit(video_dir: Path, lang: str = config.PRIMARY_LANGUAGE, today: dt.date | None = None) -> Path:
    """Tạo / cập nhật audit.md. Phần máy được viết lại mỗi lần; phần người điền được giữ."""
    video_dir = Path(video_dir)
    if not (video_dir / "scenes.json").exists():
        raise SystemExit(f"Không thấy {video_dir / 'scenes.json'}: chưa tạo được audit.md")
    path = video_dir / AUDIT_NAME
    old = parse_audit(path.read_text(encoding="utf-8")) if path.exists() else {}
    keep = {k: old.get(k, "") for k in AUDIT_HUMAN}
    result = originality.evaluate(video_dir)
    rights_points, rights_issues = rights.check(video_dir)
    hint = disclosure(video_dir)
    per_day = cadence(video_dir)
    reused, reused_why, inauth, inauth_why = _risk(result, per_day)
    claims = canon.parse_brief(video_dir / "brief.md") if (video_dir / "brief.md").exists() else []
    resolved = sum(c.resolved for c in claims)
    links = sum(1 for c in claims if canon.has_link(c.source))
    meta = video_dir / f"metadata.{lang}.md"
    titles = (_section(metadata_sections(meta.read_text(encoding="utf-8")), "tiêu đề") or "") if meta.exists() else ""
    title = next((re.sub(r"^\d+[.)]\s*", "", x).strip() for x in titles.splitlines() if x.strip() and not x.lower().startswith("chọn")), "")
    required = hint["realistic_or_meaningfully_altered"]
    rights_fail = [m for lv, m in rights_issues if lv == rights.FAIL]
    checks = [
        (result["verdict"] == originality.PASS, "Kịch bản là nội dung nguyên bản, có luận điểm riêng (originality.json)."),
        (bool(claims) and resolved == len(claims), f"Nguồn nghiên cứu đã lưu và đã kiểm ({resolved}/{len(claims)} dòng)."),
        (not rights_fail, f"Mọi tài sản đã có quyền sử dụng ({rights.LEDGER_NAME})."),
        (result["criteria"]["khong-paraphrase"]["points"] == 2, "Không dùng nội dung sao chép hoặc chỉ sửa sơ sài."),
        (None, "Không có phát ngôn giả, deepfake, mạo danh hoặc giọng clone trái phép."),
        (None, "Chủ đề sức khỏe, pháp lý, tài chính, chính trị (nếu có) đã kiểm nguồn chính thức."),
        (None, "Tiêu đề và thumbnail không gây hiểu lầm."),
        (None, "Đã bật khai báo nội dung đã chỉnh sửa nếu cần."),
        (result["criteria"]["khac-nhau"]["points"] == 2 and not (per_day and per_day > 1), "Video không phải sản phẩm hàng loạt gần như giống nhau."),
        (None, "Không có bot, traffic ảo hoặc lời kêu gọi thao túng."),
    ]
    lines = [
        "# Pre-publish audit",
        "",
        f"> Tạo bằng `python -m tools.release_check {video_dir} --write-audit`. Máy viết lại các dòng tự động mỗi lần chạy; "
        "các dòng người điền (Owner, Human creative contribution, Disclosure completed, Final reviewer, Decision, Reasons) được giữ.",
        "",
        f"- Video: {video_dir.name}" + (f" · {title}" if title else ""),
        f"- Date: {(today or dt.date.today()).isoformat()}",
        f"- Owner: {keep['Owner']}",
        f"- Human creative contribution: {keep['Human creative contribution']}",
        f"- Research sources: brief.md, {len(claims)} khẳng định, {links} dòng có link, {resolved} dòng đã kiểm",
        f"- Asset rights checked: {'yes' if rights_points == 2 and not rights_fail else 'no'}",
        f"- Reused-content risk: {reused}",
        f"- Inauthentic-content risk: {inauth}",
        f"- AI disclosure required: {'yes' if required else 'no'}",
        f"- Disclosure completed: {keep['Disclosure completed'] or ('no' if required else 'not applicable')}",
        f"- Final reviewer: {keep['Final reviewer']}",
        f"- Decision: {keep['Decision']}",
        f"- Reasons: {keep['Reasons']}",
        "",
        "## Máy ghi",
        "",
        f"- Độ nguyên bản: {result['total']}/{result['max']}, {result['verdict']}.",
    ]
    lines += [f"  - {k}: {'–' if c['points'] is None else c['points']}/2. {c['evidence']}" for k, c in result["criteria"].items()]
    lines += [
        f"- Rủi ro nội dung dùng lại ({reused}): {reused_why}.",
        f"- Rủi ro không chân thực ({inauth}): {inauth_why}.",
        "- Quyền tài sản: " + ("; ".join(rights_fail[:3]) or "mọi dòng đã kiểm") + ".",
        "",
        "```yaml",
        "ai_disclosure:",
        f"  ai_used: {str(hint['ai_used']).lower()}",
        f"  realistic_or_meaningfully_altered: {str(required).lower()}",
        f"  youtube_studio_altered_content: {hint['youtube_studio_altered_content']}",
        f"  reason: \"{hint['reason']}\"",
        f"  viewer_note: \"{hint['viewer_note']}\"",
        "```",
        "",
        "## Checklist trước khi đăng",
        "",
        "Máy đánh dấu các mục kiểm được; mục còn lại người duyệt tự xem và tự đánh dấu.",
        "",
    ]
    lines += [f"- [{'x' if ok else ' '}] {text}" + ("" if ok is not None else " (người kiểm)") for ok, text in checks]
    lines += [
        "",
        "## Người duyệt điền",
        "",
        "- **Human creative contribution:** phần người đã làm (chọn chủ đề, sửa kịch bản, chọn ảnh, duyệt giọng…).",
        "- **Final reviewer:** tên người duyệt cuối.",
        "- **Decision:** `publish`, `revise` hoặc `reject`. Chỉ `publish` mới qua cổng.",
        "- **Reasons:** lý do, nhất là khi rủi ro ghi `high`.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def check_audit(video_dir: Path) -> list[Check]:
    path = Path(video_dir) / AUDIT_NAME
    if not path.exists():
        return [Check("Duyệt của người", FAIL, f"chưa có {AUDIT_NAME}; chạy lại với --write-audit rồi người duyệt điền")]
    fields = parse_audit(path.read_text(encoding="utf-8"))
    decision = fields.get("Decision", "").strip().strip("`").lower()
    missing = [k for k in ("Human creative contribution", "Final reviewer") if not fields.get(k)]
    if decision != "publish":
        what = f"quyết định là '{decision}'" if decision in DECISIONS else "chưa có quyết định"
        return [Check("Duyệt của người", FAIL, f"{what} (cần 'Decision: publish' trong {AUDIT_NAME})")]
    if missing:
        return [Check("Duyệt của người", FAIL, f"{AUDIT_NAME} thiếu: {', '.join(missing)}")]
    note = f"; rủi ro không chân thực: {fields.get('Inauthentic-content risk')}" if fields.get("Inauthentic-content risk") == "high" else ""
    return [Check("Duyệt của người", WARN if note else OK, f"publish, duyệt bởi {fields['Final reviewer']}{note}")]


def check_shorts(video_dir: Path) -> list[Check]:
    n = len(list((video_dir / "render" / "shorts").glob("*.mp4")))
    return [Check("Short", OK if n >= 3 else WARN, f"{n}/3 Short trong render/shorts/")]


def run(
    video_dir: Path, lang: str = config.PRIMARY_LANGUAGE, measure_loudness: bool = True, audit: bool = False
) -> list[Check]:
    video_dir = Path(video_dir)
    checks, duration = check_render(video_dir, lang, measure_loudness)
    checks += check_subs(video_dir, lang, duration)
    checks += check_chapters(video_dir)
    checks += check_thumbnail(video_dir)
    checks += check_shorts(video_dir)
    checks += check_metadata(video_dir, lang)
    checks += check_disclosure(video_dir, lang)
    checks += check_sources(video_dir)
    checks += check_voice_license(video_dir)
    checks += check_rights(video_dir)
    checks += check_originality(video_dir)
    if audit:
        write_audit(video_dir, lang)
    checks += check_audit(video_dir)
    return checks


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path)
    p.add_argument("--lang", default=config.PRIMARY_LANGUAGE, choices=sorted(config.LANGUAGES))
    p.add_argument("--no-loudness", action="store_true", help="bỏ đo độ to")
    p.add_argument("--write-audit", action="store_true", help="tạo / cập nhật audit.md cho người duyệt")
    args = p.parse_args()
    checks = run(args.video_dir, args.lang, not args.no_loudness, args.write_audit)
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
