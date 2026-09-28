"""Đọc và kiểm tra ``scenes.json`` của một video.

Cấu trúc::

    {
      "title": "Tiêu đề làm việc",
      "languages": ["vi"],
      "style_prompt": "anime illustration, ...",      # chép từ channel/profile.md
      "mascot_prompt": "a chubby grey cat ...",       # chép từ channel/profile.md
      "scenes": [
        {
          "id": "s01",
          "chapter": "Mở đầu",                        # tuỳ chọn: cảnh bắt đầu một chương
          "narration": {"vi": "Lời thoại...", "en": "..."},
          "image_prompt": "wide shot of ...",
          "on_screen_text": "Chữ hiện trên màn hình", # tuỳ chọn
          "use_mascot": false                          # tuỳ chọn
        }
      ]
    }
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from tools import config

SCENE_ID = re.compile(r"^[a-z0-9_-]+$")


class ScenesError(ValueError):
    """scenes.json không hợp lệ."""


@dataclass
class Scene:
    id: str
    narration: dict[str, str]
    image_prompt: str
    on_screen_text: str = ""
    chapter: str = ""
    use_mascot: bool = False


@dataclass
class Storyboard:
    title: str
    languages: list[str]
    scenes: list[Scene]
    style_prompt: str = ""
    mascot_prompt: str = ""
    extra: dict = field(default_factory=dict)


def parse(data: dict) -> Storyboard:
    errors: list[str] = []

    languages = data.get("languages") or [config.PRIMARY_LANGUAGE]
    for lang in languages:
        if lang not in config.LANGUAGES:
            errors.append(f"ngôn ngữ không hỗ trợ: {lang}")
    if config.PRIMARY_LANGUAGE not in languages:
        errors.append(f"thiếu ngôn ngữ chính '{config.PRIMARY_LANGUAGE}' trong languages")

    raw_scenes = data.get("scenes") or []
    if not raw_scenes:
        errors.append("không có cảnh nào")

    scenes: list[Scene] = []
    seen: set[str] = set()
    for i, raw in enumerate(raw_scenes):
        sid = str(raw.get("id", ""))
        where = f"cảnh #{i + 1} ({sid or 'không có id'})"
        if not SCENE_ID.match(sid):
            errors.append(f"{where}: id chỉ được dùng chữ thường, số, '-' và '_'")
        elif sid in seen:
            errors.append(f"{where}: id bị trùng")
        seen.add(sid)

        narration = raw.get("narration") or {}
        for lang in languages:
            if not str(narration.get(lang, "")).strip():
                errors.append(f"{where}: thiếu lời thoại '{lang}'")
        if not str(raw.get("image_prompt", "")).strip():
            errors.append(f"{where}: thiếu image_prompt")

        scenes.append(
            Scene(
                id=sid,
                narration={k: str(v).strip() for k, v in narration.items()},
                image_prompt=str(raw.get("image_prompt", "")).strip(),
                on_screen_text=str(raw.get("on_screen_text", "")).strip(),
                chapter=str(raw.get("chapter", "")).strip(),
                use_mascot=bool(raw.get("use_mascot", False)),
            )
        )

    if any(s.use_mascot for s in scenes) and not str(data.get("mascot_prompt", "")).strip():
        errors.append("có cảnh dùng linh vật nhưng thiếu mascot_prompt")

    if errors:
        raise ScenesError("scenes.json không hợp lệ:\n- " + "\n- ".join(errors))

    known = {"title", "languages", "style_prompt", "mascot_prompt", "scenes"}
    return Storyboard(
        title=str(data.get("title", "")),
        languages=list(languages),
        scenes=scenes,
        style_prompt=str(data.get("style_prompt", "")).strip(),
        mascot_prompt=str(data.get("mascot_prompt", "")).strip(),
        extra={k: v for k, v in data.items() if k not in known},
    )


def load(video_dir: Path) -> Storyboard:
    path = Path(video_dir) / "scenes.json"
    if not path.exists():
        raise ScenesError(f"không tìm thấy {path}")
    return parse(json.loads(path.read_text(encoding="utf-8")))
