import copy
import datetime as dt
import json

import pytest

from tools import rights

REGISTRY = {
    "gemini-image-api": {"label": "Ảnh API", "creator": "Kênh", "license": "Điều khoản API", "source_url": "https://x/terms",
                         "attribution_required": "no", "status": "da-kiem"},
    "gemini-image-app": {"label": "Ảnh app", "creator": "Kênh", "license": "Điều khoản app", "source_url": "https://y/terms",
                         "attribution_required": "no", "status": "can-kiem"},
    "voxcpm2": {"label": "VoxCPM2", "creator": "Kênh", "license": "Apache-2.0", "source_url": "https://github.com/OpenBMB/VoxCPM",
                "attribution_required": "no", "status": "da-kiem"},
    "omnivoice": {"label": "OmniVoice", "creator": "k2-fsa", "license": "CC-BY-NC 4.0", "source_url": "https://hf/omni",
                  "attribution_required": "yes", "status": "cam"},
    "font-be-vietnam-pro": {"label": "Font", "creator": "Tác giả font", "license": "OFL-1.1", "source_url": "https://f",
                            "attribution_required": "no", "status": "da-kiem"},
    "seedance-dreamina": {"label": "Clip", "creator": "Kênh", "license": "", "source_url": "", "attribution_required": "chưa rõ",
                          "status": "can-kiem"},
}


@pytest.fixture
def video(tmp_path):
    d = tmp_path / "v"
    d.mkdir()
    board = {"languages": ["vi"], "scenes": [{"id": f"s0{i}", "narration": {"vi": "Lời."}, "image_prompt": "p"} for i in (1, 2)]}
    (d / "scenes.json").write_text(json.dumps(board), encoding="utf-8")
    (d / "cost.json").write_text(json.dumps({"images": 2, "tts_local_seconds": {"vi": 30.0}}), encoding="utf-8")
    return d


@pytest.fixture
def reg():
    return copy.deepcopy(REGISTRY)


def test_build_writes_document_columns_and_rows(video, reg):
    rows = rights.build(video, reg)
    text = (video / "rights.csv").read_text(encoding="utf-8")
    assert text.splitlines()[0] == ",".join(rights.COLUMNS)
    assert [r["asset_id"] for r in rows] == ["s01", "s02", "voice-vi", "font", "thumbnail"]
    assert rows[0]["permission_proof"] == "registry:gemini-image-api" and rows[0]["license"] == "Điều khoản API"
    assert rows[2]["license"] == "Apache-2.0"  # VoiceStudio mặc định dùng voxcpm2
    assert rows[-1]["permission_proof"] == "registry:gemini-image-api; registry:font-be-vietnam-pro"
    assert rights.check(video, reg) == (2, [])


def test_rebuild_keeps_manual_rows_and_human_cells(video, reg):
    rights.build(video, reg)
    rows = rights.read_ledger(video / "rights.csv")
    rows[0]["notes"] = "ảnh làm lại ngày 05/10"
    rows[1].update(creator="Tự vẽ", source_url="https://drive/x", license="Tác phẩm của kênh", permission_proof="file gốc trên Drive")
    music = dict.fromkeys(rights.COLUMNS, "")
    music.update(asset_id="music", type="music", creator="Tác giả", source_url="https://yt/audiolibrary/1",
                 license="Không cần ghi công", permission_proof="Thư viện âm thanh YouTube")
    (video / "rights.csv").write_text(rights.to_csv(rows + [music]), encoding="utf-8")
    again = {r["asset_id"]: r for r in rights.build(video, reg)}
    assert again["s01"]["notes"] == "ảnh làm lại ngày 05/10"
    assert again["s02"]["creator"] == "Tự vẽ" and again["music"]["license"] == "Không cần ghi công"
    assert rights.check(video, reg)[0] == 2


def test_unknown_and_unchecked_block_publishing(video, reg):
    (video / "cost.json").write_text(json.dumps({"images_app": 2, "tts_app_seconds": {"vi": 30.0}}), encoding="utf-8")
    rows = {r["asset_id"]: r for r in rights.build(video, reg)}
    assert rows["voice-vi"]["license"] == rights.UNKNOWN  # giọng làm tay chưa rõ công cụ
    points, issues = rights.check(video, reg)
    assert points == 0
    messages = " ".join(m for lv, m in issues if lv == rights.FAIL)
    assert "UNKNOWN" in messages and "chưa kiểm điều khoản" in messages


def test_planned_rows_when_nothing_made_yet(video, reg):
    (video / "cost.json").unlink()
    rows = {r["asset_id"]: r for r in rights.build(video, reg, write=False)}
    assert rows["s01"]["permission_proof"] == f"registry:{rights.PLANNED_IMAGE}"
    assert rows["voice-vi"]["notes"].startswith(rights.AUTO_NOTE) and "dự kiến" in rows["voice-vi"]["notes"]
    points, issues = rights.check(video, reg)
    assert points == 2 and issues[0][0] == rights.FAIL and "chưa có rights.csv" in issues[0][1]


def test_banned_engine_expired_licence_and_attribution(video, reg, monkeypatch):
    monkeypatch.setattr(rights.voicestudio, "settings", lambda *a: {"engine": "omnivoice"})
    rights.build(video, reg)
    points, issues = rights.check(video, reg)
    assert points == 0 and any("bị cấm" in m for _, m in issues)
    assert any(lv == rights.WARN and "ghi công" in m for lv, m in issues)

    monkeypatch.setattr(rights.voicestudio, "settings", lambda *a: {"engine": "voxcpm2"})
    rows = rights.build(video, reg)
    rows[0]["expiry"] = "2026-01-01"
    points, issues = rights.audit(rows, reg, today=dt.date(2026, 10, 1))
    assert points == 0 and any("hết hạn" in m for _, m in issues)


def test_clip_rows_and_can_kiem_gives_one_point(video, reg):
    (video / "assets" / "clips").mkdir(parents=True)
    (video / "assets" / "clips" / "s02.mp4").write_bytes(b"x")
    rows = rights.build(video, reg)
    assert "clip-s02" in [r["asset_id"] for r in rows]
    points, issues = rights.check(video, reg)
    assert points == 0  # clip chưa có giấy phép trong sổ: ô trống tính là UNKNOWN
    reg["seedance-dreamina"].update(license="Điều khoản Dreamina", source_url="https://dreamina/terms")
    rights.build(video, reg)
    assert rights.check(video, reg)[0] == 1


def test_stale_ledger_is_flagged(video, reg):
    rights.build(video, reg)
    (video / "cost.json").write_text(json.dumps({"images_app": 2, "tts_local_seconds": {"vi": 30.0}}), encoding="utf-8")
    _, issues = rights.check(video, reg)
    assert issues[0][0] == rights.WARN and "chưa khớp" in issues[0][1]


def test_repo_registry_is_honest():
    reg = rights.load_registry()
    for key, item in reg.items():
        assert item["status"] in ("da-kiem", "can-kiem", "UNKNOWN", "cam"), key
        if item["status"] == "da-kiem":
            assert item["checked"] and item["license"] and item["source_url"], key
    assert reg["gemini-image-api"]["status"] != "da-kiem" or reg["gemini-image-api"]["checked"]
