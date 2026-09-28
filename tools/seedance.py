"""Xuất prompt Seedance 2.5 cho các cảnh "đinh" (cảnh có video_prompt trong scenes.json).

    python -m tools.seedance videos/<thư-mục>

Kết quả: videos/<thư-mục>/seedance.md — mỗi cảnh một khối: ảnh tham chiếu, độ dài, prompt.
Dùng thủ công trên app Dreamina/CapCut (chế độ ảnh → video): tải ảnh assets/images/<id>.png làm
khung đầu, dán prompt, chọn 16:9, tắt âm thanh. Tải clip về, đặt vào assets/clips/<id>.mp4 rồi
chạy lại tools.assemble — cảnh đó sẽ dùng clip thay cho ảnh tĩnh.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools import config, scenes

# Luôn ghép vào cuối prompt: giữ bản quyền an toàn và để giọng đọc riêng của kênh.
GUARD = (
    "Keep the exact art style, colors and characters of the reference image. "
    "No text, no logos, no watermark, no dialogue, no lip-sync. "
    "Original characters only, do not depict any existing anime character."
)


def build_prompt(board: scenes.Storyboard, scene: scenes.Scene) -> str:
    parts = [
        f"{scene.clip_seconds}-second cinematic anime shot, 16:9.",
        board.style_prompt,
        f"Scene: {scene.image_prompt}",
    ]
    if scene.use_mascot:
        parts.append(f"The channel mascot: {board.mascot_prompt}")
    parts += [f"Motion and camera: {scene.video_prompt}", GUARD]
    return " ".join(p.strip().rstrip(".") + "." for p in parts if p.strip())


def export(video_dir: Path) -> Path:
    board = scenes.load(video_dir)
    hero = [s for s in board.scenes if s.video_prompt]
    total = sum(s.clip_seconds for s in hero)
    lines = [
        f"# Prompt Seedance 2.5 — {board.title}",
        "",
        f"{len(hero)} clip, tổng {total} giây. Qua API khoảng {total * config.PRICE_VIDEO_PER_SECOND:.2f} USD "
        "(720p); làm trên app Dreamina/CapCut thì trừ credit của gói.",
        "",
        "Cách làm cho mỗi clip: chọn ảnh → video, tải ảnh tham chiếu làm khung đầu, dán prompt, "
        "tỉ lệ 16:9, độ dài như ghi, tắt âm thanh. Lưu clip thành `assets/clips/<id>.mp4`.",
        "",
    ]
    for s in hero:
        lines += [
            f"## {s.id} — {s.clip_seconds} giây",
            "",
            f"- Ảnh tham chiếu: `assets/images/{s.id}.png`",
            f"- Lời thoại cảnh này: {s.narration.get(config.PRIMARY_LANGUAGE, '')}",
            "",
            "```text",
            build_prompt(board, s),
            "```",
            "",
        ]
    out = Path(video_dir) / "seedance.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_dir", type=Path)
    args = p.parse_args()
    print(export(args.video_dir))


if __name__ == "__main__":
    main()
