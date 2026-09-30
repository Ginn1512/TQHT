import json

import pytest
from PIL import Image

from tools import config, media, originality, release_check, rights
from tools.tests.test_originality import LINES
from tools.tests.test_rights import REGISTRY

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
- **Dạng video:** A · Giải thích hệ thống
- **Câu hỏi video trả lời:** Vì sao Gon mất Nen?
- **Luận điểm riêng:** Nen đổi rủi ro lấy sức mạnh, và Gon trả giá bằng chính luật đó.

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


def fill_audit(d, **fields):
    """Điền các dòng người duyệt trong audit.md."""
    path = d / release_check.AUDIT_NAME
    text = path.read_text(encoding="utf-8")
    for key, value in fields.items():
        name = key.replace("_", " ").capitalize()
        text = text.replace(f"- {name}: \n", f"- {name}: {value}\n", 1)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def ready(tmp_path, monkeypatch):
    """Một video đủ mọi thứ để đăng (độ dài tối thiểu hạ xuống cho test)."""
    monkeypatch.setattr(config, "MIN_VIDEO_MINUTES", 0.4)
    monkeypatch.setattr(rights, "load_registry", lambda *a: REGISTRY)
    monkeypatch.setattr(originality, "VIDEOS_DIR", tmp_path)
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
    raw = [{"id": f"s{i:02d}", "narration": {"vi": x}, "image_prompt": "a paper notebook sketch"} for i, x in enumerate(LINES, 1)]
    raw[1]["chapter"] = "Góc nhìn của Kaku"
    (d / "scenes.json").write_text(json.dumps({"languages": ["vi"], "scenes": raw}), encoding="utf-8")
    rights.build(d)
    for key in originality.MANUAL:
        originality.set_score(d, key, 2, "s03: so sánh riêng của kênh")
    release_check.write_audit(d)
    fill_audit(d, human_creative_contribution="chọn chủ đề, sửa kịch bản, duyệt ảnh", final_reviewer="Thắng", decision="publish")
    return d


def levels(checks):
    return {c.name: c.level for c in checks}


def test_ready_video_has_no_errors(ready):
    checks = release_check.run(ready)
    lv = levels(checks)
    assert release_check.FAIL not in lv.values(), [(c.name, c.detail) for c in checks if c.level == release_check.FAIL]
    assert lv["Khung hình"] == lv["Chương"] == lv["Nguồn (canon)"] == lv["Giấy phép giọng"] == release_check.OK
    assert lv["Quyền tài sản"] == lv["Độ nguyên bản"] == lv["Duyệt của người"] == lv["Gợi ý khai báo AI"] == release_check.OK
    assert "Độ to" in lv  # sóng sin mẫu nhỏ hơn -14 LUFS nên chỉ là LƯU Ý


def test_missing_render_and_metadata_are_errors(tmp_path):
    d = tmp_path / "v"
    d.mkdir()
    (d / "brief.md").write_text(BRIEF.replace(" — đã kiểm 2026-10-01", " — cần kiểm lại"), encoding="utf-8")
    lv = levels(release_check.run(d, measure_loudness=False))
    for name in ("Bản render", "Phụ đề", "Chương", "Thumbnail", "Metadata", "Nguồn (canon)", "Quyền tài sản", "Độ nguyên bản", "Duyệt của người"):
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


def test_audit_needs_human_decision_and_keeps_it(ready):
    audit = ready / release_check.AUDIT_NAME
    text = audit.read_text(encoding="utf-8")
    assert text.startswith("# Pre-publish audit") and "ai_disclosure:" in text and "- Asset rights checked: yes" in text
    # chạy lại --write-audit giữ phần người điền
    release_check.write_audit(ready)
    fields = release_check.parse_audit(audit.read_text(encoding="utf-8"))
    assert fields["Decision"] == "publish" and fields["Final reviewer"] == "Thắng"
    assert fields["Reused-content risk"] == "low" and fields["Inauthentic-content risk"] == "low"
    audit.write_text(audit.read_text(encoding="utf-8").replace("- Decision: publish", "- Decision: revise"), encoding="utf-8")
    check = release_check.check_audit(ready)[0]
    assert check.level == release_check.FAIL and "revise" in check.detail
    audit.unlink()
    assert release_check.check_audit(ready)[0].level == release_check.FAIL


def test_three_videos_a_day_is_high_inauthentic_risk(ready, tmp_path):
    topics = tmp_path / "topics.md"
    rows = [f"| {n} | 2026-10-06 | 06:00 | x | `videos/{name}/` |" for n, name in enumerate(("v", "b", "c"), 1)]
    topics.write_text("\n".join(rows) + "\n", encoding="utf-8")
    assert release_check.cadence(ready, topics) == 3
    result = originality.evaluate(ready)
    assert release_check._risk(result, 3)[2] == "high"
    assert release_check._risk(result, 1)[2] == "low"


def test_originality_and_rights_gate(ready, monkeypatch):
    originality.set_score(ready, "khong-paraphrase", 0, "s02: dịch gần nguyên văn wiki")
    check = release_check.check_originality(ready)[0]
    assert check.level == release_check.FAIL and "từ chối" in check.detail
    reg = {k: dict(v) for k, v in REGISTRY.items()}
    reg["gemini-image-api"]["status"] = "can-kiem"
    monkeypatch.setattr(rights, "load_registry", lambda *a: reg)
    assert release_check.check_rights(ready)[0].level == release_check.FAIL


def test_disclosure_hint_for_real_world_or_photoreal(ready):
    assert release_check.disclosure(ready)["youtube_studio_altered_content"] == "no"
    brief = ready / "brief.md"
    brief.write_text(brief.read_text(encoding="utf-8").replace("A · Giải thích hệ thống", "S · Nguồn gốc ngoài đời thật"), encoding="utf-8")
    hint = release_check.disclosure(ready)
    assert hint["realistic_or_meaningfully_altered"] and "dạng S" in hint["reason"]
    # metadata ghi "Không tick" trong khi nên tick: LƯU Ý
    assert release_check.check_disclosure(ready)[0].level == release_check.WARN
    scenes_json = ready / "scenes.json"
    brief.write_text(BRIEF, encoding="utf-8")
    scenes_json.write_text(scenes_json.read_text(encoding="utf-8").replace("a paper notebook sketch", "photorealistic street, DSLR", 1), encoding="utf-8")
    assert "photorealistic" in release_check.disclosure(ready)["reason"]


def test_title_link_and_sponsor_policy(ready):
    meta = ready / "metadata.vi.md"
    text = METADATA.replace("2. Hunter x Hunter: Vì sao Gon mất Nen?", "2. SỐC: GON MẤT NEN VÌ AI?")
    text = text.replace("Nguồn: https://hunterxhunter.fandom.com/wiki/Nen", "Nguồn: http://hunterxhunter.fandom.com/wiki/Nen\nMua truyện: https://shopee.vn/x?aff=kaku")
    meta.write_text(text, encoding="utf-8")
    lv = levels(release_check.check_metadata(ready, "vi"))
    assert lv["Tiêu đề câu kéo"] == lv["Link ngoài"] == release_check.WARN
    assert lv["Tiết lộ tài trợ"] == release_check.FAIL
    meta.write_text(text.replace("Mua truyện:", "Tiết lộ: link dưới là link tiếp thị liên kết, kênh nhận hoa hồng.\nMua truyện:"), encoding="utf-8")
    assert "Tiết lộ tài trợ" not in levels(release_check.check_metadata(ready, "vi"))
