import json

from PIL import Image

from tools import app_images, config, images, scenes


def board():
    return scenes.parse(
        {
            "languages": ["vi"],
            "style_prompt": "anime style",
            "mascot_prompt": "a small owl",
            "scenes": [
                {"id": "s01", "chapter": "Mở đầu", "narration": {"vi": "a"}, "image_prompt": "a cliff", "use_mascot": True},
                {"id": "s02", "narration": {"vi": "b"}, "image_prompt": "a sea"},
            ],
        }
    )


def test_export_adds_aspect_prefix_and_mascot_flag():
    data = app_images.export(board())
    first, second = data["scenes"]
    assert first["prompt"].startswith(app_images.ASPECT_PREFIX)
    assert "a small owl" in first["prompt"] and first["mascot"] is True and first["chapter"] == "Mở đầu"
    assert second["mascot"] is False and "a small owl" not in second["prompt"]
    assert "a small owl" in data["mascot_reference"]


def test_fit_frame_any_shape_to_video_size():
    for size in [(1024, 1024), (768, 1344), (2048, 1152)]:
        assert images.fit_frame(Image.new("RGB", size)).size == (config.WIDTH, config.HEIGHT)


def test_fit_frame_trim_removes_corner_mark():
    img = Image.new("RGB", (1600, 900), (0, 0, 0))
    img.paste((255, 255, 255), (1540, 850, 1600, 900))  # "watermark" ở góc dưới phải
    out = images.fit_frame(img, trim=0.05)
    assert out.getpixel((config.WIDTH - 5, config.HEIGHT - 5)) == (0, 0, 0)


def test_import_reports_missing_and_records_count(tmp_path):
    video = tmp_path / "v"
    video.mkdir()
    raw = {"languages": ["vi"], "scenes": [{"id": f"s0{i}", "narration": {"vi": "x"}, "image_prompt": "p"} for i in (1, 2, 3)]}
    (video / "scenes.json").write_text(json.dumps(raw), encoding="utf-8")
    src = tmp_path / "in"
    src.mkdir()
    Image.new("RGB", (1024, 1024)).save(src / "s01.png")
    Image.new("RGB", (800, 450)).save(src / "s03.jpg")
    (src / "notes.txt").write_text("bỏ qua")
    done, missing = app_images.import_images(video, src)
    assert done == ["s01", "s03"] and missing == ["s02"]
    assert Image.open(video / "assets" / "images" / "s03.png").size == (config.WIDTH, config.HEIGHT)
    usage = json.loads((video / "cost.json").read_text())
    assert usage["images_app"] == 2 and usage["usd"] == 0


def test_build_page_embeds_label_and_parseable_data():
    b = board()
    html = app_images.build_page(b, "video 9")
    assert "<title>Xưởng ảnh video 9</title>" in html and "__DATA__" not in html
    raw = html.split('<script type="application/json" id="data">', 1)[1].split("</script>", 1)[0]
    data = json.loads(raw)
    assert [s["id"] for s in data["scenes"]] == ["s01", "s02"] and data["scenes"][0]["say"] == "a"
