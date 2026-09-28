"""Cấu hình chung: đường dẫn, model, giá, thông số video.

Giá lấy từ bảng giá Gemini API tháng 9/2026 (nguồn thứ ba). Kiểm tra lại trên
trang giá chính thức và sửa ở đây nếu thay đổi. Model có thể đổi bằng biến môi
trường mà không cần sửa code.
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cache"
CHANNEL_DIR = ROOT / "channel"
FONTS_DIR = ROOT / "assets" / "fonts"

# --- Model (đổi bằng biến môi trường nếu Google đổi tên) ---
# Xem danh sách model hiện có: python -m tools.gemini models
TTS_MODEL = os.environ.get("YT_TTS_MODEL", "gemini-3.8-flash-lite-tts")
IMAGE_MODEL = os.environ.get("YT_IMAGE_MODEL", "gemini-3.1-flash-lite-image")

# --- Giá (USD) ---
PRICE_PER_IMAGE = 0.0336
# TTS tính theo token âm thanh đầu ra: 6 USD / 1 triệu token, 25 token mỗi giây.
PRICE_TTS_PER_SECOND = 6.0 / 1_000_000 * 25
# Seedance 2.5, 720p, không có video đầu vào. Replicate khoảng 0,23 USD/giây, fal khoảng 0,47.
# Làm thủ công trên app Dreamina/CapCut thì trả bằng credit của gói, không qua API.
PRICE_VIDEO_PER_SECOND = 0.23
MONTHLY_BUDGET_USD = 38.0

# --- Ngôn ngữ ---
# Mã ngôn ngữ dùng trong scenes.json -> mã BCP-47 gửi cho TTS và giọng đọc mặc định.
LANGUAGES = {
    "vi": {"name": "Tiếng Việt", "tts_code": "vi-VN", "voice": "Kore"},
    "en": {"name": "English", "tts_code": "en-US", "voice": "Kore"},
    "pt-BR": {"name": "Português (Brasil)", "tts_code": "pt-BR", "voice": "Kore"},
    "hi": {"name": "हिन्दी", "tts_code": "hi-IN", "voice": "Kore"},
    "zh-TW": {"name": "繁體中文", "tts_code": "cmn-TW", "voice": "Kore"},
}
PRIMARY_LANGUAGE = "vi"
# Tốc độ đọc ước tính (ký tự/giây) để dự trù chi phí trước khi tạo giọng.
CHARS_PER_SECOND = {"vi": 13.0, "en": 14.0, "pt-BR": 14.0, "hi": 12.0, "zh-TW": 4.5}

# --- Video ---
WIDTH, HEIGHT = 1920, 1080
FPS = 30
MIN_VIDEO_MINUTES = 15  # yêu cầu của kênh: video dài 15–20 phút
MAX_VIDEO_MINUTES = 20
SCENE_PADDING_S = 0.4  # khoảng lặng sau mỗi câu thoại
MAX_TEMPO = 1.2  # tăng tốc tối đa khi khớp bản lồng tiếng vào độ dài cảnh
MUSIC_VOLUME = 0.08
TTS_SAMPLE_RATE = 24_000  # Gemini TTS trả về PCM 16-bit mono 24 kHz
