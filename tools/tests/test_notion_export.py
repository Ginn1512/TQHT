from tools import config, notion_export

VIDEO = config.ROOT / "videos" / "2026-10-06-nen-hunter-x-hunter"


def test_render_strips_file_header_and_adds_note():
    text = notion_export.render(VIDEO)
    first, second = text.splitlines()[:2]
    assert first.startswith("> Bản chép từ `script.vi.md` (commit ")
    assert "https://github.com/Ginn1512/TQHT/blob/HEAD/videos/2026-10-06-nen-hunter-x-hunter/script.vi.md" in first
    assert "Đừng sửa thẳng" in second
    assert "# Kịch bản" not in text and "Sinh từ `scenes.json`" not in text
    assert "## Mở đầu" in text and "**s01** —" in text


def test_body_keeps_everything_after_header():
    script = "# Kịch bản — X\n\n> Sinh từ scenes.json\n\n## Mở đầu\n\n**s01** — A.\n"
    assert notion_export.body(script) == "## Mở đầu\n\n**s01** — A.\n"


def test_folders_by_number():
    got = notion_export.folders("1-3,9")
    assert got[0] == "videos/2026-10-06-nen-hunter-x-hunter" and len(got) == 4
