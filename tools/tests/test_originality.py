import json

import pytest

from tools import originality, rights, scenes
from tools.tests.test_rights import REGISTRY

BRIEF = """# Brief

- **Anime:** Hunter x Hunter
- **Dạng video:** A · Giải thích hệ thống
- **Câu hỏi video trả lời:** Vì sao Gon mất Nen?
- **Luận điểm riêng:** Nen là hệ thống đổi rủi ro lấy sức mạnh, và Gon trả giá bằng chính luật đó.

## Sự thật dùng trong kịch bản

| Sự thật | Nguồn / tình trạng |
|---|---|
| 6 hệ | [Hunterpedia](https://hunterxhunter.fandom.com/wiki/Nen) — đã kiểm 2026-10-01 |
| Gon mất Nen | [Hunterpedia](https://hunterxhunter.fandom.com/wiki/Gon) — đã kiểm 2026-10-01 |
"""

LINES = [
    "Mở sổ ra nào! Mình là Kaku. Hôm nay ta mở trang về luật Nen và cái giá của sức mạnh.",
    "Kaku ghi chú: sáu hệ không phải sáu ngăn kéo tách rời, chúng là một vòng tròn liền nhau.",
    "Theo mình, giao ước là phát minh thông minh nhất của Togashi, vì nó biến điểm yếu thành sức mạnh.",
    "Mình nghĩ Gon không thua vì yếu, mà vì cậu đặt cược cả tương lai vào một khoảnh khắc.",
    "Kaku đoán nhiều bạn sẽ phản đối, nhưng hãy nhìn bảng phần trăm trên màn hình trước đã.",
    "Kaku để ý rằng mỗi lần luật được nói ra, một nhân vật khác lại dùng nó để phá luật.",
    "Kaku gấp sổ đây, hẹn gặp lại!",
]


def write_video(root, name, lines, chapter="Góc nhìn của Kaku", brief=BRIEF):
    d = root / name
    d.mkdir(parents=True)
    raw = [{"id": f"s{i:02d}", "narration": {"vi": text}, "image_prompt": "p"} for i, text in enumerate(lines, 1)]
    raw[1]["chapter"] = chapter
    (d / "scenes.json").write_text(json.dumps({"languages": ["vi"], "scenes": raw}), encoding="utf-8")
    (d / "brief.md").write_text(brief, encoding="utf-8")
    (d / "cost.json").write_text(json.dumps({"images": len(lines), "tts_local_seconds": {"vi": 60.0}}), encoding="utf-8")
    return d


@pytest.fixture
def channel(tmp_path, monkeypatch):
    monkeypatch.setattr(rights, "load_registry", lambda *a: REGISTRY)
    other = ["Một câu chuyện hoàn toàn khác về hải tặc, trái ác quỷ và giấc mơ tìm kho báu cuối cùng."] * 3
    write_video(tmp_path, "b", other)
    v = write_video(tmp_path, "a", LINES)
    rights.build(v)
    return tmp_path, v


def test_auto_criteria_score_full_marks(channel):
    root, v = channel
    result = originality.evaluate(v, videos_dir=root)
    pts = {k: c["points"] for k, c in result["criteria"].items()}
    assert pts == {"cau-hoi": 2, "nguon": 2, "binh-luan": 2, "vi-du-moi": None, "hinh-co-quyen": 2,
                   "khong-paraphrase": None, "khac-nhau": 2, "gia-tri": None}
    assert result["verdict"] == originality.PENDING and result["total"] == 10


def test_manual_scores_gate_and_persist(channel):
    root, v = channel
    for key in originality.MANUAL:
        result = originality.set_score(v, key, 2, "s03: phép so sánh riêng của kênh", videos_dir=root)
    assert result["verdict"] == originality.PASS and result["total"] == 16
    saved = json.loads((v / originality.RESULT_NAME).read_text(encoding="utf-8"))
    assert saved["criteria"]["gia-tri"] == {"label": originality.CRITERIA["gia-tri"][0], "by": "claude", "points": 2,
                                            "evidence": "s03: phép so sánh riêng của kênh"}
    # chấm lại phần máy vẫn giữ điểm tay
    assert originality.evaluate(v, videos_dir=root)["total"] == 16
    # chỉ đọc lại nguồn: từ chối dù tổng điểm cao
    result = originality.set_score(v, "khong-paraphrase", 0, "s02–s05 dịch gần nguyên văn một bài wiki", videos_dir=root)
    assert result["verdict"] == originality.REJECT


def test_set_score_rejects_auto_criteria_and_missing_evidence(channel):
    _, v = channel
    with pytest.raises(SystemExit):
        originality.set_score(v, "nguon", 2, "tự cho điểm")
    with pytest.raises(SystemExit):
        originality.set_score(v, "gia-tri", 2, "  ")


def test_weak_brief_and_commentary_lower_scores(tmp_path, monkeypatch):
    monkeypatch.setattr(rights, "load_registry", lambda *a: REGISTRY)
    brief = BRIEF.replace("- **Luận điểm riêng:** Nen là hệ thống đổi rủi ro lấy sức mạnh, và Gon trả giá bằng chính luật đó.\n", "")
    brief = brief.replace("[Hunterpedia](https://hunterxhunter.fandom.com/wiki/Nen) — đã kiểm 2026-10-01", "Kiến thức chuẩn — cần kiểm lại")
    brief = brief.replace("[Hunterpedia](https://hunterxhunter.fandom.com/wiki/Gon) — đã kiểm 2026-10-01", "Kiến thức chuẩn — cần kiểm lại")
    v = write_video(tmp_path, "a", ["Nen có sáu hệ và bốn nguyên tắc cơ bản mà ai cũng cần biết."] * 4, chapter="Sáu hệ", brief=brief)
    result = originality.evaluate(v, videos_dir=tmp_path)
    pts = {k: c["points"] for k, c in result["criteria"].items()}
    assert pts["cau-hoi"] == 1 and pts["nguon"] == 0 and pts["binh-luan"] == 0
    # chưa có rights.csv: chấm theo các dòng dự kiến (ảnh API, VoxCPM2), đều đã kiểm trong sổ thử
    assert pts["hinh-co-quyen"] == 2


def test_near_copy_between_videos_is_caught(channel):
    root, v = channel
    write_video(root, "c", LINES[:-1] + ["Một câu kết khác hẳn để không trùng tuyệt đối với video kia."])
    result = originality.evaluate(v, videos_dir=root)
    assert result["criteria"]["khac-nhau"]["points"] == 0 and "c" in result["criteria"]["khac-nhau"]["evidence"]


def test_catchphrases_do_not_count_as_template():
    board = scenes.parse({"languages": ["vi"], "scenes": [{"id": "s1", "narration": {"vi": LINES[0] + " " + LINES[-1]}, "image_prompt": "p"}]})
    text = originality.narration(board)
    assert all(p not in text for p in originality.CATCHPHRASES)


def test_scan_reports_pairs_and_repeated_sentences(channel):
    root, _ = channel
    write_video(root, "c", ["Nếu video hữu ích, hãy đăng ký kênh nhé bạn."] * 2)
    write_video(root, "d", ["Nếu video hữu ích, hãy đăng ký kênh nhé bạn."] * 2)
    write_video(root, "e", ["Nếu video hữu ích, hãy đăng ký kênh nhé bạn."] * 2)
    report = originality.scan(root)
    assert "5 video" in report and "3 video: nếu video hữu ích, hãy đăng ký kênh nhé bạn." in report


def test_brief_field_reads_bullets_and_sections():
    text = "- **Câu hỏi video trả lời:** Vì sao?\n\n## Luận điểm riêng của kênh\n\nLuận điểm A.\n\n## Khác\n"
    assert originality.brief_field(text, "Câu hỏi video trả lời") == "Vì sao?"
    assert originality.brief_field(text, "Luận điểm riêng") == "Luận điểm A."
    assert originality.brief_field(text, "Không có") == ""
