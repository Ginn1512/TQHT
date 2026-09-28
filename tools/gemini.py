"""Kết nối Gemini API (giọng đọc + ảnh) và cache kết quả theo hash.

    python -m tools.gemini models   # liệt kê model TTS và ảnh đang có cho key này
"""

from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path
from typing import Callable, TypeVar

from tools import config

T = TypeVar("T")


class MissingKey(RuntimeError):
    pass


def client():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise MissingKey(
            "Chưa có biến môi trường GEMINI_API_KEY. Thêm nó trong cài đặt môi trường cloud "
            "(menu môi trường ở thanh tiêu đề phiên → Edit), rồi mở phiên mới."
        )
    from google import genai

    return genai.Client(api_key=key)


def cli(main: Callable[[], None]) -> None:
    """Chạy lệnh; thiếu key thì in hướng dẫn thay vì traceback."""
    try:
        main()
    except MissingKey as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        sys.exit(1)


def with_retry(fn: Callable[[], T], attempts: int = 4, base_delay: float = 2.0) -> T:
    """Thử lại khi bị giới hạn tốc độ (429) hoặc lỗi máy chủ (5xx)."""
    from google.genai import errors

    for i in range(attempts):
        try:
            return fn()
        except errors.APIError as e:
            retryable = e.code == 429 or (e.code or 0) >= 500
            if not retryable or i == attempts - 1:
                raise
            time.sleep(base_delay * 2**i)
    raise AssertionError("unreachable")


def cache_path(kind: str, *parts: str, suffix: str) -> Path:
    digest = hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()[:24]
    return config.CACHE_DIR / kind / f"{digest}{suffix}"


def list_models() -> list[tuple[str, str]]:
    out = []
    for m in client().models.list():
        name = m.name.removeprefix("models/")
        if "tts" in name or "image" in name or "imagen" in name:
            out.append((name, m.display_name or ""))
    return sorted(out)


def main() -> None:
    if sys.argv[1:] != ["models"]:
        print(__doc__)
        sys.exit(2)
    print(f"Đang cấu hình: TTS={config.TTS_MODEL}  IMAGE={config.IMAGE_MODEL}\n")
    for name, display in list_models():
        mark = " <- đang dùng" if name in (config.TTS_MODEL, config.IMAGE_MODEL) else ""
        print(f"{name:45s} {display}{mark}")


if __name__ == "__main__":
    cli(main)
