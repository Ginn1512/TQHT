"""Tạo giọng Kaku bằng VoiceStudio chạy trên máy tính của bạn (miễn phí, không cần API key).

VoiceStudio (https://github.com/debpalash/VoiceStudio) là app desktop, mở API ở
http://localhost:3900. Lệnh này phải chạy trên CHÍNH máy đang mở VoiceStudio: phiên
Claude trên cloud không với tới localhost của bạn. Hướng dẫn cài: docs/voicestudio.md.

    python -m tools.voicestudio check                              # app chạy chưa, có engine và hồ sơ giọng nào
    python -m tools.voicestudio design                             # đọc thử câu mẫu bằng 3 mô tả giọng Kaku
    python -m tools.voicestudio test                               # đọc thử câu mẫu bằng hồ sơ giọng đã chọn
    python -m tools.voicestudio run videos/<thư-mục> [--only s01,s02] [--force]
    python -m tools.voicestudio pack videos/<thư-mục>              # gói giọng thành render/giong-vi.zip để gửi đi
    python -m tools.voicestudio unpack videos/<thư-mục> --from giong-vi.zip   # nhận gói giọng ở máy khác

Mặc định dùng engine VoxCPM2 (giấy phép Apache-2.0, có tiếng Việt). Lệnh từ chối
engine OmniVoice (mặc định của app): trọng số của nó theo CC-BY-NC 4.0, không dùng
được cho video bật kiếm tiền.

Kết quả: videos/<thư-mục>/assets/audio/<lang>/<scene-id>.wav, đúng chỗ tools.assemble đọc.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from tools import config, costs, media, scenes

DEFAULT_URL = "http://localhost:3900"
DEFAULT_ENGINE = "voxcpm2"
VOICE_FILE = config.CHANNEL_DIR / "giong-kaku.json"

# Giấy phép TRỌNG SỐ mô hình, không phải giấy phép của app (app là AGPL-3.0).
# Chỉ engine trong LICENSE_OK được dùng mặc định cho kênh bật kiếm tiền.
LICENSE_OK = {"voxcpm2": "Apache-2.0 (OpenBMB VoxCPM2)"}
LICENSE_BLOCKED = {"omnivoice": "CC-BY-NC 4.0 (k2-fsa/OmniVoice), phi thương mại"}
# Tên kiểu OpenAI (tts-1…) chuyển tới engine đang bật trong app, thường là OmniVoice.
OPENAI_ALIASES = {"tts-1", "tts-1-hd", "gpt-4o-mini-tts"}


class StudioError(RuntimeError):
    def __init__(self, message: str, status: int | None = None, network: bool = False):
        super().__init__(message)
        self.status = status
        self.network = network

    @property
    def retryable(self) -> bool:
        return self.network or (self.status or 0) >= 500


def settings(voice: dict | None = None) -> dict:
    """Mục "voicestudio" trong giong-kaku.json, cộng giá trị mặc định."""
    voice = voice if voice is not None else json.loads(VOICE_FILE.read_text(encoding="utf-8"))
    s = {"engine": DEFAULT_ENGINE, "voice_id": None, "speed": 1.0, "seed": 1234, "language": "vi"}
    s.update({k: v for k, v in (voice.get("voicestudio") or {}).items() if not k.startswith("_")})
    return s


def base_url() -> str:
    return os.environ.get("VOICESTUDIO_URL", DEFAULT_URL).rstrip("/")


def check_license(engine: str, license_ok: bool = False) -> str:
    """Trả về giấy phép của engine, hoặc dừng nếu không dùng được cho kênh kiếm tiền."""
    if engine in LICENSE_BLOCKED:
        raise StudioError(
            f"Engine '{engine}' dùng trọng số {LICENSE_BLOCKED[engine]}. "
            f"Kênh sẽ bật kiếm tiền nên không dùng engine này. Hãy dùng '{DEFAULT_ENGINE}'."
        )
    if engine in OPENAI_ALIASES:
        raise StudioError(
            f"'{engine}' chuyển tới engine đang bật trong app (thường là OmniVoice, phi thương mại). "
            f"Hãy ghi rõ engine, ví dụ --engine {DEFAULT_ENGINE}."
        )
    if engine in LICENSE_OK:
        return LICENSE_OK[engine]
    if license_ok:
        return "đã được bạn tự kiểm (--license-ok)"
    raise StudioError(
        f"Chưa kiểm giấy phép trọng số của engine '{engine}'. Đọc giấy phép của mô hình, ghi vào "
        "docs/voicestudio.md, rồi chạy lại với --license-ok."
    )


def _request(method: str, path: str, body: dict | None = None, timeout: float = 30.0) -> tuple[bytes, str]:
    url = base_url() + path
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(), resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            err = json.loads(raw)
            msg = (err.get("error") or {}).get("message") or err.get("detail") or raw.decode("utf-8", "replace")
        except ValueError:
            msg = raw.decode("utf-8", "replace")
        raise StudioError(f"VoiceStudio trả lỗi {e.code} ở {path}: {str(msg)[:300]}", status=e.code) from e
    except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
        raise StudioError(
            f"Không kết nối được VoiceStudio ở {base_url()} ({e}). Mở app VoiceStudio trên máy này trước. "
            "Lệnh phải chạy trên chính máy đó, không chạy trong phiên Claude trên cloud.",
            network=True,
        ) from e


def get_json(path: str) -> dict:
    raw, _ = _request("GET", path)
    return json.loads(raw)


def speech(
    text: str, s: dict, voice: str | None = None, description: str | None = None, retries: int = 2, wait: float = 3.0
) -> bytes:
    """Gọi POST /v1/audio/speech, trả về byte WAV. Lần đầu có thể chậm vì app nạp mô hình."""
    body = {
        "model": s["engine"],
        "input": text,
        "voice": voice or s.get("voice_id") or "default",
        "response_format": "wav",
        "speed": s.get("speed", 1.0),
        "language": s.get("language", "vi"),
    }
    if s.get("seed") is not None:
        body["seed"] = s["seed"]
    if description:
        body["description"] = description
    attempt = 0
    while True:
        try:
            raw, ctype = _request("POST", "/v1/audio/speech", body, timeout=600.0)
            break
        except StudioError as e:
            if not e.retryable or attempt >= retries:
                raise
            attempt += 1
            time.sleep(wait * attempt)
    if raw[:4] != b"RIFF":
        raise StudioError(f"VoiceStudio không trả về WAV (Content-Type: {ctype or '?'}).")
    return raw


def cache_file(text: str, s: dict, voice: str | None, description: str | None) -> Path:
    key = "\x1f".join(
        [s["engine"], voice or str(s.get("voice_id")), str(s.get("speed")), str(s.get("seed")), s.get("language", "vi"), description or "", text]
    )
    return config.CACHE_DIR / "voicestudio" / f"{hashlib.sha256(key.encode('utf-8')).hexdigest()[:24]}.wav"


def synthesize(text: str, s: dict, out: Path, voice: str | None = None, description: str | None = None) -> bool:
    """Ghi WAV mono 16-bit 24 kHz (cùng chuẩn với tools.tts) vào out. Trả về True nếu vừa gọi app."""
    cached = cache_file(text, s, voice, description)
    fresh = not cached.exists()
    if fresh:
        raw = speech(text, s, voice=voice, description=description)
        cached.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "raw.wav"
            src.write_bytes(raw)
            media.run_ffmpeg(["-i", str(src), "-ac", "1", "-ar", str(config.TTS_SAMPLE_RATE), "-sample_fmt", "s16", str(cached)])
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cached, out)
    return fresh


def record_seconds(video_dir: Path, lang: str, seconds: float) -> None:
    """Ghi thời lượng giọng tạo tại máy vào cost.json (0 USD, chỉ để theo dõi)."""
    usage = costs.load_usage(video_dir)
    local = usage.setdefault("tts_local_seconds", {})
    local[lang] = round(local.get(lang, 0.0) + seconds, 1)
    usage["usd"] = costs.usd_of(usage)
    (Path(video_dir) / costs.COST_FILE).write_text(json.dumps(usage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(video_dir: Path, s: dict, lang: str = config.PRIMARY_LANGUAGE, only: set[str] | None = None, force: bool = False) -> list[str]:
    if not s.get("voice_id"):
        raise StudioError(
            "Chưa có hồ sơ giọng Kaku. Tạo giọng trong VoiceStudio (docs/voicestudio.md), rồi ghi id vào "
            "mục voicestudio.voice_id của channel/giong-kaku.json hoặc truyền --voice <id>."
        )
    board = scenes.load(video_dir)
    if lang not in board.languages:
        raise SystemExit(f"'{lang}' chưa có trong languages của scenes.json")
    out_dir = Path(video_dir) / "assets" / "audio" / lang
    made, seconds = [], 0.0
    for scene in board.scenes:
        if only and scene.id not in only:
            continue
        dst = out_dir / f"{scene.id}.wav"
        if dst.exists() and not force:
            print(f"{scene.id} đã có, bỏ qua (dùng --force để làm lại)")
            continue
        fresh = synthesize(scene.narration[lang], s, dst)
        secs = media.wav_duration(dst)
        if fresh:
            seconds += secs
        print(f"{scene.id} [{lang}] {secs:.1f}s{'' if fresh else ' (cache)'}")
        made.append(scene.id)
    if seconds:
        record_seconds(video_dir, lang, seconds)
    return made


def pack(video_dir: Path, lang: str = config.PRIMARY_LANGUAGE) -> Path:
    """Gói giọng các cảnh thành render/giong-<lang>.zip. Dừng nếu còn thiếu cảnh."""
    board = scenes.load(video_dir)
    src = Path(video_dir) / "assets" / "audio" / lang
    missing = [s.id for s in board.scenes if not (src / f"{s.id}.wav").exists()]
    if missing:
        raise StudioError(f"Còn thiếu giọng {len(missing)} cảnh: {', '.join(missing[:10])}")
    out = Path(video_dir) / "render" / f"giong-{lang}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for s in board.scenes:
            z.write(src / f"{s.id}.wav", f"{s.id}.wav")
    return out


def unpack(video_dir: Path, archive: Path, lang: str = config.PRIMARY_LANGUAGE) -> tuple[list[str], list[str]]:
    """Giải nén gói giọng vào assets/audio/<lang>/. Chỉ nhận file <scene-id>.wav có trong scenes.json."""
    board = scenes.load(video_dir)
    ids = {s.id for s in board.scenes}
    out_dir = Path(video_dir) / "assets" / "audio" / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    got = []
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            stem = Path(name).stem
            if Path(name).suffix.lower() == ".wav" and stem in ids:
                (out_dir / f"{stem}.wav").write_bytes(z.read(name))
                got.append(stem)
    return sorted(got), [s.id for s in board.scenes if s.id not in got]


def check() -> None:
    health = get_json("/health")
    print(f"VoiceStudio ở {base_url()}: {json.dumps(health, ensure_ascii=False)[:200]}")
    models = [m.get("id") for m in get_json("/v1/models").get("data", []) if (m.get("voicestudio") or {}).get("kind") == "tts"]
    print("Engine đọc (TTS) đã cài:", ", ".join(m for m in models if m) or "(không thấy)")
    for m in models:
        if m in LICENSE_OK:
            print(f"  {m}: dùng được cho kênh kiếm tiền ({LICENSE_OK[m]})")
        elif m in LICENSE_BLOCKED:
            print(f"  {m}: KHÔNG dùng cho video kiếm tiền ({LICENSE_BLOCKED[m]})")
    if DEFAULT_ENGINE not in models:
        print(f"Chưa thấy engine {DEFAULT_ENGINE}. Cài nó trong app VoiceStudio (docs/voicestudio.md, bước 2).")
    profiles = [v for v in get_json("/v1/audio/voices").get("voices", []) if v.get("type") == "profile"]
    print(f"Hồ sơ giọng: {len(profiles)}")
    for v in profiles:
        print(f"  {v.get('voice_id')}  {v.get('name', '')}  {v.get('language', '')}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--engine", help=f"engine VoiceStudio (mặc định lấy từ giong-kaku.json, hoặc {DEFAULT_ENGINE})")
    p.add_argument("--voice", help="id hồ sơ giọng Kaku trong VoiceStudio (mặc định lấy từ giong-kaku.json)")
    p.add_argument("--license-ok", action="store_true", help="đã tự kiểm giấy phép của engine không có trong danh sách")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("design")
    sub.add_parser("test")
    for name in ("pack", "unpack"):
        k = sub.add_parser(name)
        k.add_argument("video_dir", type=Path)
        k.add_argument("--lang", default=config.PRIMARY_LANGUAGE, choices=sorted(config.LANGUAGES))
        if name == "unpack":
            k.add_argument("--from", dest="archive", type=Path, required=True)
    r = sub.add_parser("run")
    r.add_argument("video_dir", type=Path)
    r.add_argument("--lang", default=config.PRIMARY_LANGUAGE, choices=sorted(config.LANGUAGES))
    r.add_argument("--only", help="chỉ làm các cảnh này, ví dụ s01,s07")
    r.add_argument("--force", action="store_true", help="làm lại cả cảnh đã có file")
    args = p.parse_args()

    voice_cfg = json.loads(VOICE_FILE.read_text(encoding="utf-8"))
    s = settings(voice_cfg)
    if args.engine:
        s["engine"] = args.engine
    if args.voice:
        s["voice_id"] = args.voice
    try:
        if args.cmd == "check":
            check()
            return
        if args.cmd == "pack":
            print(f"Đã gói: {pack(args.video_dir, args.lang)}")
            return
        if args.cmd == "unpack":
            got, missing = unpack(args.video_dir, args.archive, args.lang)
            print(f"Đã nhận giọng {len(got)} cảnh." + (f" Còn thiếu {len(missing)}: {', '.join(missing[:10])}" if missing else ""))
            return
        print(f"Engine {s['engine']}: {check_license(s['engine'], args.license_ok)}")
        out = config.CACHE_DIR / "voicestudio-test"
        if args.cmd == "design":
            for v in voice_cfg["voices"]:
                dst = out / f"design-{v['id']}.wav"
                synthesize(voice_cfg["sample"], s, dst, voice="default", description=v["design_prompt"])
                print(f"{v['label']}: {dst} ({media.wav_duration(dst):.1f}s)")
            print("Nghe 3 file, chọn giọng hợp nhất, rồi lưu thành hồ sơ giọng trong app (docs/voicestudio.md, bước 3).")
            return
        if args.cmd == "test":
            if not s.get("voice_id"):
                raise StudioError("Chưa có voice_id. Chạy 'design' rồi làm bước 3 trong docs/voicestudio.md.")
            dst = out / "kaku-test.wav"
            synthesize(voice_cfg["sample"], s, dst)
            print(f"Đã đọc thử: {dst} ({media.wav_duration(dst):.1f}s)")
            return
        only = set(args.only.split(",")) if args.only else None
        made = run(args.video_dir, s, args.lang, only, args.force)
        print(f"Xong {len(made)} cảnh. Kiểm tra: python -m tools.assemble {args.video_dir} --draft")
    except StudioError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
