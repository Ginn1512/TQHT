"""Lấy dữ liệu kênh YouTube qua TranscriptAPI (https://transcriptapi.com).

    python -m tools.yt_research profile @handle          # 1 credit: tên, số người đăng ký, số video
    python -m tools.yt_research outliers @handle         # 1 credit: video phổ biến + điểm vượt trội
    python -m tools.yt_research transcript VIDEO_ID      # 1 credit: transcript có mốc thời gian

Mọi kết quả được cache trong .cache/transcriptapi/, gọi lại không tốn thêm credit.
Cần biến môi trường TRANSCRIPT_API_KEY và tên miền transcriptapi.com được phép truy cập.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from tools import config

BASE = "https://transcriptapi.com/api/v2/youtube"
USER_AGENT = "ClaudeCode/1.0 (TQHT anime channel research)"


class ApiError(RuntimeError):
    pass


def _get(path: str, params: dict, use_cache: bool = True) -> dict:
    query = urllib.parse.urlencode(params)
    cache = config.CACHE_DIR / "transcriptapi" / (hashlib.sha256(f"{path}?{query}".encode()).hexdigest()[:24] + ".json")
    if use_cache and cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))

    key = os.environ.get("TRANSCRIPT_API_KEY")
    if not key:
        raise ApiError(
            "Chưa có biến môi trường TRANSCRIPT_API_KEY. Thêm nó trong cài đặt môi trường cloud "
            "(menu môi trường ở thanh tiêu đề phiên → Edit), rồi mở phiên mới."
        )
    req = urllib.request.Request(
        f"{BASE}/{path}?{query}", headers={"Authorization": f"Bearer {key}", "User-Agent": USER_AGENT}
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code in (408, 429, 503) and attempt < 2:
                time.sleep(int(e.headers.get("Retry-After") or 2 * (attempt + 1)))
                continue
            hint = {401: "key sai", 402: "hết credit", 403: "bị Cloudflare chặn", 404: "không tìm thấy / không có phụ đề"}
            raise ApiError(f"TranscriptAPI {e.code} ({hint.get(e.code, 'lỗi')}): {path}") from e
        except urllib.error.URLError as e:
            raise ApiError(
                f"Không kết nối được transcriptapi.com ({e.reason}). Kiểm tra tên miền đã được thêm vào "
                "Network access của môi trường chưa."
            ) from e
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


_VIEWS = re.compile(r"(\d[\d,]*(?:\.\d+)?)\s*([KMB])?\b", re.IGNORECASE)
_MULT = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}


def parse_views(text: str | int | None) -> int | None:
    """'1.2M views' -> 1200000, '12K views' -> 12000, '1,234 views' -> 1234, 'No views' -> 0."""
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return int(text)
    if re.search(r"\bno views\b", text, re.IGNORECASE):
        return 0
    m = _VIEWS.search(text)
    if not m:
        return None
    number, suffix = m.groups()
    return int(round(float(number.replace(",", "")) * (_MULT[suffix.upper()] if suffix else 1)))


def outlier_scores(videos: list[dict], baseline: float) -> list[dict]:
    """Điểm vượt trội = lượt xem ÷ lượt xem trung vị của các video gần đây."""
    out = []
    for v in videos:
        views = parse_views(v.get("viewCount", v.get("viewCountText")))
        if views is None or baseline <= 0:
            continue
        out.append({**v, "views": views, "outlier": round(views / baseline, 2)})
    return sorted(out, key=lambda v: v["outlier"], reverse=True)


def profile(channel: str) -> dict:
    return _get("channel/info", {"channel": channel})


def latest(channel: str) -> list[dict]:
    data = _get("channel/latest", {"channel": channel})
    return data.get("results") or data.get("videos") or []


def popular(channel: str) -> list[dict]:
    data = _get("channel/videos", {"channel": channel, "sort": "popular"})
    return data.get("results") or data.get("videos") or []


def transcript(video: str) -> dict:
    return _get(
        "transcript",
        {"video_url": video, "format": "text", "include_timestamp": "true", "send_metadata": "true"},
    )


def outliers(channel: str) -> list[dict]:
    recent = [parse_views(v.get("viewCount", v.get("viewCountText"))) for v in latest(channel)]
    recent = [v for v in recent if v]
    baseline = statistics.median(recent) if recent else 0
    return outlier_scores(popular(channel), baseline)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["profile", "outliers", "transcript"])
    p.add_argument("target", help="@handle hoặc video id/url")
    args = p.parse_args()
    try:
        if args.cmd == "profile":
            print(json.dumps(profile(args.target), ensure_ascii=False, indent=2))
        elif args.cmd == "outliers":
            for v in outliers(args.target):
                title = v.get("title", "")
                print(f"{v['outlier']:>7.2f}x  {v['views']:>12,}  {v.get('lengthText', ''):>8}  {v.get('videoId', '')}  {title}")
        else:
            data = transcript(args.target)
            print(json.dumps(data.get("metadata", {}), ensure_ascii=False))
            print(data.get("transcript", ""))
    except ApiError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
