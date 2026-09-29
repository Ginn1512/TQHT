---
name: kaku-release-review
description: Kiểm một video trước khi đăng lên YouTube — bản render (độ dài 15–20 phút, 1920×1080, có tiếng, độ to), phụ đề, chương, thumbnail, 3 Short, metadata.vi.md, sổ nguồn và giấy phép giọng — bằng python -m tools.release_check, sửa từng lỗi, xem bằng mắt vài khung hình, rồi mới gửi người dùng duyệt đăng. Dùng khi video đã dựng xong bản đầy đủ, khi người dùng hỏi "đăng được chưa", hoặc trước bước giao video của /yt-studio.
---

# kaku-release-review: cửa kiểm cuối trước khi đăng

Chạy sau `/yt-studio` mục 6 (thumbnail và metadata), trước mục 7 (giao video). **Còn LỖI thì không gửi người dùng đi đăng.**

## 0. Đủ đồ chưa

Trong `videos/<thư-mục>/` phải có:

- `render/video.vi.mp4`: bản đầy đủ, không phải `draft.vi.mp4`;
- `render/subs.vi.srt`, `render/chapters.txt`: do `tools.assemble` tạo;
- `render/thumbnail.png`: do `tools.thumbnail` tạo;
- 3 file `render/shorts/*.mp4`;
- `metadata.vi.md`, theo khuôn ở mục 1;
- `cost.json`: ghi giọng được tạo bằng gì (`tts_local_seconds`, `tts_app_seconds` hoặc `tts_seconds`).

## 1. Khuôn `metadata.vi.md`

Công cụ đọc theo đúng các tiêu đề `##` này:

```markdown
# Metadata — <tiêu đề làm việc>

## Tiêu đề
1. <phương án 1, ≤ 60 ký tự, tên anime ở đầu>
2. <phương án 2>
3. <phương án 3>
Chọn: 1

## Mô tả
<2 dòng mở đầu gây tò mò>

<dán nguyên render/chapters.txt: 0:00 …>

Nguồn tham khảo:
- <link từ brief.md>

Cảnh báo spoiler: <mức spoiler trong brief.md>
Hình minh họa do AI tạo, không phải hình chính thức. Video phân tích của fan.

## Tag
<10–15 tag, cách nhau bằng dấu phẩy>

## Hashtag
#<Anime> #<ChủĐề> #Anime

## Nội dung AI (Altered or synthetic content)
<Tick / Không tick> — <lý do>
```

Luật cho mục Nội dung AI:
- Tranh anime cách điệu rõ ràng thì **không tick**.
- Có hình giống người thật hay sự kiện thật (ví dụ dạng S về lịch sử) thì **tick**.
- Luôn ghi lý do.

## 2. Chạy kiểm tra

```bash
python -m tools.release_check videos/<thư-mục>     # thêm --no-loudness nếu cần nhanh
```

Kết quả có 3 mức: ĐẠT, LƯU Ý, LỖI. Còn LỖI thì lệnh trả mã 1.

| LỖI | Cách sửa |
|---|---|
| Bản render / report.json là bản nháp | `python -m tools.assemble videos/<thư-mục>` (bản đầy đủ, sau khi có đủ giọng) |
| Độ dài ngoài 15–20 phút | Thiếu: thêm cảnh. Thừa: rút gọn. Sửa `scenes.json`, làm lại giọng cảnh đổi, dựng lại. |
| Khung hình, âm thanh | Dựng lại bằng `tools.assemble`, không dùng file từ công cụ khác |
| Phụ đề, chương | Dựng lại. Chương sai luật thì sửa `chapter` trong `scenes.json`: mỗi chương ≥ 10 giây, ít nhất 3 chương. |
| Thumbnail | `python -m tools.thumbnail videos/<thư-mục> --text "…" --bg sNN` (1280×720, dưới 2 MB) |
| Metadata (tiêu đề, mô tả, hashtag, khai báo AI) | Sửa `metadata.vi.md` theo khuôn ở mục 1 |
| Nguồn (canon) | Làm theo `/kaku-canon-ledger` cho video này |
| Giấy phép giọng | VoiceStudio chỉ dùng `voxcpm2` (xem `docs/voicestudio.md`). Làm lại giọng nếu đã dùng engine khác. |

LƯU Ý: không chặn đăng nhưng phải nói với người dùng, ví dụ độ to lệch khỏi khoảng −16 tới −12 LUFS, tag ít hơn 10, thiếu Short, giọng làm tay chưa rõ điều khoản.

## 3. Xem bằng mắt

Công cụ không nhìn được hình. Tự kiểm:

```bash
python - <<'EOF'
from tools import media
for t in (5, 300, 700):
    media.run_ffmpeg(["-ss", str(t), "-i", "videos/<thư-mục>/render/video.vi.mp4", "-frames:v", "1", f"<scratchpad>/frame-{t}.png"])
EOF
```

Dùng Read xem 3 khung hình và `render/thumbnail.png`. Đạt khi:
- chữ trên hình không bị cắt;
- phụ đề không che chữ trên hình;
- ảnh không có chữ lạ và không giống nhân vật có bản quyền;
- chữ trên thumbnail đọc được khi thu nhỏ.

## 4. Gửi người dùng duyệt

- Gửi bằng SendUserFile: `render/video.vi.mp4`, `render/thumbnail.png`, 3 Short và `metadata.vi.md`. File quá lớn thì tải lên Google Drive.
- Kèm bảng kết quả `release_check`: các LƯU Ý còn lại và lý do giữ.
- Kèm danh sách việc tự làm trong YouTube Studio, lấy từ cuối kết quả lệnh.
- Hỏi bằng AskUserQuestion: **Đăng** / **Sửa**. Sau khi người dùng đồng ý đăng, làm tiếp `/yt-studio` mục 7: `costs record`, Notion, `topics.md`, commit.

Không commit MP4: `render/` bị gitignore.
