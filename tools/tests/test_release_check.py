import json

import pytest
from PIL import Image

from tools import config, media, release_check

METADATA = """# Metadata

## Tiêu đề
1. Hunter x Hunter: Nen hoạt động thế nào?
2. Hunter x Hunter: Vì sao Gon mất Nen?
Chọn: 1

## Mô tả
Vì sao Gon mất hết Nen? Kaku giải mã từng luật.

0:00 Mở đầu
0:10 Bốn nguyên tắc
0:20 Sáu hệ

Nguồn: https://hunterxhunter.fandom.com/wiki/Nen
Hình minh họa do AI tạo, không phải hình chính thức. Video phân tích của fan.

## Tag
hunter x hunter, nen, gon, killua, hisoka, kurapika, hệ nen, phân tích anime, anime, manga

## Hashtag
#HunterxHunter #Nen #Anime

## Nội dung AI (Altered or synthetic content)
Không tick: tranh cách điệu, không giống người thật.
"""

BRIEF = """# Brief

- **Anime:** Hunter x Hunter

## Sự thật dùng trong kịch bản

| Sự thật | Nguồn / tình trạng |
|---|---|
| 6 hệ | [Hunterpedia](https://hunterxhunter.fandom.com/wiki/Nen) — đã kiểm 2026-10-01 |
"""


def make_video(path, seconds=31, size="1920x1080"):
    media.run_ffmpeg([
        "-f", "lavfi", "-i", f"color=c=navy:s={size}:r=30:d={seconds}",
        "-f", "lavfi", "-i", f"sine=frequency=440:duration={seconds}",
        "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(path),
    ])


@pytest.fixture
def ready(tmp_path, monkeypatch):
    """Một video đủ mọi thứ để đăng (độ dài tối thiểu hạ xuống cho test)."""
    monkeypatch.setattr(config, "MIN_VIDEO_MINUTES", 0.4)
    d = tmp_path / "v"
    render = d / "render"
    (render / "shorts").mkdir(parents=True)
    make_video(render / "video.vi.mp4")
    (render / "subs.vi.srt").write_text(
        "1\n00:00:00,000 --> 00:00:15,000\nMở sổ ra nào!\n\n2\n00:00:15,000 --> 00:00:30,500\nKaku gấp sổ đây.\n", encoding="utf-8"
    )
    (render / "chapters.txt").write_text("0:00 Mở đầu\n0:10 Bốn nguyên tắc\n0:20 Sáu hệ\n", encoding="utf-8")
    Image.new("RGB", (1280, 720), "navy").save(render / "thumbnail.png")
    for i in range(3):
        (render / "shorts" / f"s{i}.mp4").write_bytes(b"x")
    (render / "report.json").write_text(json.dumps({"total_s": 31, "length_problem": "", "languages": {"vi": "ok"}}), encoding="utf-8")
    (d / "metadata.vi.md").write_text(METADATA, encoding="utf-8")
    (d / "brief.md").write_text(BRIEF, encoding="utf-8")
    (d / "cost.json").write_text(json.dumps({"tts_local_seconds": {"vi": 30.0}}), encoding="utf-8")
    return d


def levels(checks):
    return {c.name: c.level for c in checks}


def test_ready_video_has_no_errors(ready):
    checks = release_check.run(ready)
    lv = levels(checks)
    assert release_check.FAIL not in lv.values(), [(c.name, c.detail) for c in checks if c.level == release_check.FAIL]
    assert lv["Khung hình"] == lv["Chương"] == lv["Nguồn (canon)"] == lv["Giấy phép giọng"] == release_check.OK
    assert "Độ to" in lv  # sóng sin mẫu nhỏ hơn -14 LUFS nên chỉ là LƯU Ý


def test_missing_render_and_metadata_are_errors(tmp_path):
    d = tmp_path / "v"
    d.mkdir()
    (d / "brief.md").write_text(BRIEF.replace(" — đã kiểm 2026-10-01", " — cần kiểm lại"), encoding="utf-8")
    lv = levels(release_check.run(d, measure_loudness=False))
    for name in ("Bản render", "Phụ đề", "Chương", "Thumbnail", "Metadata", "Nguồn (canon)"):
        assert lv[name] == release_check.FAIL, name


def test_metadata_rules(ready):
    meta = ready / "metadata.vi.md"
    text = METADATA.replace("1. Hunter x Hunter: Nen hoạt động thế nào?", "1. " + "x" * 101)
    text = text.replace("Hình minh họa do AI tạo", "Hình minh họa").replace("#Anime", " ".join(f"#t{i}" for i in range(15)))
    text = text.replace("## Nội dung AI (Altered or synthetic content)\nKhông tick: tranh cách điệu, không giống người thật.\n", "")
    meta.write_text(text, encoding="utf-8")
    lv = levels(release_check.check_metadata(ready, "vi"))
    assert lv["Tiêu đề"] == lv["Mô tả"] == lv["Hashtag"] == lv["Khai báo AI"] == release_check.FAIL
    assert lv["Tag"] == release_check.OK


def test_chapter_rules(ready):
    (ready / "render" / "chapters.txt").write_text("0:05 Mở đầu\n0:09 Hai\n", encoding="utf-8")
    detail = release_check.check_chapters(ready)[0]
    assert detail.level == release_check.FAIL
    assert "0:00" in detail.detail and "ít nhất 3" in detail.detail and "10 giây" in detail.detail


def test_draft_render_and_wrong_size_fail(ready):
    render = ready / "render"
    (render / "report.json").write_text(json.dumps({"draft": "không tiếng", "length_problem": ""}), encoding="utf-8")
    make_video(render / "video.vi.mp4", seconds=31, size="960x540")
    lv = levels(release_check.check_render(ready, "vi", measure_loudness=False)[0])
    assert lv["report.json"] == lv["Khung hình"] == release_check.FAIL


def test_voice_license_flags_blocked_engine(ready, monkeypatch):
    from tools import voicestudio

    monkeypatch.setattr(voicestudio, "settings", lambda *a: {"engine": "omnivoice"})
    assert release_check.check_voice_license(ready)[0].level == release_check.FAIL


def test_parsers():
    assert release_check.parse_chapters("0:00 A\n1:02:03 B\nkhông phải chương\n") == [(0, "A"), (3723, "B")]
    cues = release_check.parse_srt("1\n00:00:01,500 --> 00:00:02,000\nA\nB\n")
    assert cues == [(1.5, 2.0, ["A", "B"])]
