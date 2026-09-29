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
    assert first["prompt"].startswith(images.ASPECT_PREFIX)
    assert "a small owl" in first["prompt"] and first["mascot"] is True and first["chapter"] == "Mở đầu"
    assert second["mascot"] is False and "a small owl" not in second["prompt"]
    assert "a small owl" in data["mascot_reference"] and data["negative"] == images.NEGATIVE


def scene(prompt, **kw):
    return scenes.Scene(id="s01", narration={"vi": "x"}, image_prompt=prompt, **kw)


def test_build_prompt_has_six_layers_in_order():
    b = board()
    s = scene("a lone swordsman on a cliff")
    p = images.build_prompt(b, s)
    order = [images.ASPECT_PREFIX[:-1], "a lone swordsman", images.camera_hint(s), images.DEFAULT_LIGHT, "anime style", "No text"]
    positions = [p.index(part) for part in order]
    assert positions == sorted(positions)


def test_mascot_description_follows_subject():
    b = board()
    p = images.build_prompt(b, b.scenes[0])
    assert p.index("a cliff") < p.index("a small owl") < p.index("anime style")
    assert images.camera_kind(b.scenes[0]) == "mascot"


def test_camera_hint_picks_earliest_subject():
    assert images.camera_kind(scene("a pie chart with a glowing slice")) == "diagram"
    assert images.camera_kind(scene("two mirrored circles pushing a leaf")) == "compare"
    assert images.camera_kind(scene("a vast frozen sea with a single figure on it")) == "landscape"
    assert images.camera_kind(scene("a young pirate silhouette on a ship at sea")) == "figure"
    assert images.camera_kind(scene("an old key on a string")) == "object"
    assert images.camera_kind(scene("ancient beads in a museum case", chapter="Mở đầu")) == "chapter"
    assert images.camera_kind(scene("ancient beads in a museum case")) == "default"


def test_power_scenes_get_low_angle_quiet_ones_do_not():
    assert images.camera_hint(scene("a warrior silhouette with a flaming aura")) == images._POWER_CAMERA
    assert "low-angle" not in images.camera_hint(scene("a small boy sitting alone on a hospital bed"))


def test_hints_skip_when_prompt_already_has_them():
    s = scene("close-up of a sword glowing in candlelight")
    assert images.camera_hint(s) == "" and images.light_hint(s) == ""
    assert images.light_hint(scene("a pie chart")) == images.DIAGRAM_LIGHT
    assert images.light_hint(scene("a swordsman on a cliff")) == images.DEFAULT_LIGHT


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
