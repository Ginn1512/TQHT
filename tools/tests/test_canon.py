import pytest

from tools import canon

BRIEF_2 = """# Brief — thử

- **Anime:** Naruto / Naruto Shippuden (manga của Kishimoto)
- **Dạng video:** E · Hồ sơ bách khoa

## Sự thật dùng trong kịch bản

| Sự thật | Nguồn / tình trạng |
|---|---|
| Chín vĩ thú | [Narutopedia](https://naruto.fandom.com/wiki/Tailed_Beasts) |
| Tên từng con | [Wiki](https://example.com/a) — cần kiểm lại |
| Kurama ghét loài người | Kiến thức chuẩn của truyện — **cần kiểm lại** trước khi tạo giọng |
| Xếp hạng sức mạnh | Ý kiến của kênh |
| Vĩ thú nào mạnh nhất | Lý thuyết của fan, gắn nhãn trong kịch bản |

## Ý tưởng tiêu đề
"""

BRIEF_3 = """# Brief — thử 3 cột

- **Anime:** Hunter x Hunter (manga của Togashi).

## Sự thật dùng trong kịch bản

| Sự thật | Nguồn | Tình trạng |
|---|---|---|
| 4 nguyên tắc | [Screen Rant](https://screenrant.com/x) | Chỉ thấy trong kết quả tìm kiếm, chưa mở trang |
| 6 hệ | [Wiki](https://example.com/b) | Đã mở trang |
"""

TOPICS = """| # | Ngày | Chủ đề | Anime | Dạng | Thư mục | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | 2026-10-06 | Nen | HxH | A · Giải thích | `videos/2026-10-06-hxh/` | Xong |
| 2 | 2026-10-08 | Vĩ thú | Naruto | E · Hồ sơ | `videos/2026-10-08-naruto/` | Xong |
"""


@pytest.fixture
def repo(tmp_path):
    videos = tmp_path / "videos"
    for name, text in (("2026-10-06-hxh", BRIEF_3), ("2026-10-08-naruto", BRIEF_2)):
        (videos / name).mkdir(parents=True)
        (videos / name / "brief.md").write_text(text, encoding="utf-8")
    topics = tmp_path / "topics.md"
    topics.write_text(TOPICS, encoding="utf-8")
    return videos, topics


@pytest.mark.parametrize(
    "cell, status",
    [
        ("[A](https://a.com)", "co-nguon"),
        ("[A](https://a.com) — đã kiểm 2026-10-01", "da-kiem"),
        ("[A](https://a.com) — cần kiểm lại", "can-kiem"),
        ("Kiến thức phổ thông — cần thêm nguồn", "can-kiem"),
        ("Chỉ thấy trong kết quả tìm kiếm, chưa mở trang", "chua-mo"),
        ("Ghi chú của kênh (dạng U)", "y-kien"),
        ("Suy đoán, gắn nhãn trong kịch bản", "y-kien"),
        ("Kiến thức chuẩn của truyện", "khong-ro"),
    ],
)
def test_classify(cell, status):
    assert canon.classify(cell) == status


def test_parse_two_and_three_column_tables(repo):
    videos, _ = repo
    two = canon.parse_brief(videos / "2026-10-08-naruto" / "brief.md")
    assert [c.status for c in two] == ["co-nguon", "can-kiem", "can-kiem", "y-kien", "y-kien"]
    assert two[0].text == "Chín vĩ thú" and two[0].row == 1
    three = canon.parse_brief(videos / "2026-10-06-hxh" / "brief.md")
    assert [c.status for c in three] == ["chua-mo", "co-nguon"]
    assert "Screen Rant" in three[0].source and "chưa mở trang" in three[0].source


def test_anime_names_are_grouped(tmp_path):
    cases = {
        "Naruto / Naruto Shippuden (manga)": "Naruto",
        "Tokyo Revengers, Steins;Gate, Re:Zero": "Tokyo Revengers / Steins;Gate / Re:Zero",
        "Hunter x Hunter (manga của Togashi).": "Hunter x Hunter",
        "JoJo's Bizarre Adventure Part 7: Steel Ball Run": "JoJo",
    }
    for raw, want in cases.items():
        b = tmp_path / "brief.md"
        b.write_text(f"- **Anime:** {raw}\n", encoding="utf-8")
        assert canon.anime_of(b) == want


def test_ledger_counts_and_groups_open_claims_by_anime(repo):
    videos, topics = repo
    text = canon.render_ledger(videos, topics)
    assert "7 khẳng định trong 2 video. **3 chưa kiểm.** 0/2 video sẵn sàng làm giọng." in text
    assert "| 1 | 2026-10-06 | `2026-10-06-hxh` | Hunter x Hunter | 1 | 1 | Chưa |" in text
    assert "### Naruto (2)" in text and "- Video 2, dòng 2 · Cần kiểm lại: Tên từng con" in text
    assert canon.render_ledger(videos, topics) == text  # ổn định, không có ngày giờ


def test_check_and_resolve_two_columns(repo):
    videos, _ = repo
    d = videos / "2026-10-08-naruto"
    assert [c.row for c in canon.check(d)] == [2, 3]
    line = canon.resolve(d, 3, "[Narutopedia: Kurama](https://naruto.fandom.com/wiki/Kurama)", today="2026-10-01")
    assert line == "| Kurama ghét loài người | [Narutopedia: Kurama](https://naruto.fandom.com/wiki/Kurama) — đã kiểm 2026-10-01 |"
    assert [c.row for c in canon.check(d)] == [2]
    assert "## Ý tưởng tiêu đề" in (d / "brief.md").read_text(encoding="utf-8")


def test_resolve_three_columns_and_requires_link(repo):
    videos, _ = repo
    d = videos / "2026-10-06-hxh"
    canon.resolve(d, 1, "[Hunterpedia](https://hunterxhunter.fandom.com/wiki/Nen)", today="2026-10-02")
    claims = canon.parse_brief(d / "brief.md")
    assert claims[0].status == "da-kiem" and canon.check(d) == []
    with pytest.raises(SystemExit):
        canon.resolve(d, 2, "chỉ là chữ, không có link")
    with pytest.raises(SystemExit):
        canon.resolve(d, 9, "[x](https://x.com)")


def test_repo_ledger_is_up_to_date():
    assert canon.LEDGER.read_text(encoding="utf-8") == canon.render_ledger()
