---
name: kaku-release-review
description: Cổng đăng của một video trước khi lên YouTube — bản render (độ dài 15–20 phút, 1920×1080, có tiếng, độ to), phụ đề, chương, thumbnail, 3 Short, metadata.vi.md (tiêu đề câu kéo, link, tiết lộ tài trợ), sổ nguồn, giấy phép giọng, sổ quyền tài sản, điểm nguyên bản, gợi ý khai báo AI và audit.md có quyết định của người duyệt — bằng python -m tools.release_check, sửa từng lỗi, xem bằng mắt vài khung hình, rồi mới gửi người dùng duyệt đăng. Dùng khi video đã dựng xong bản đầy đủ, khi người dùng hỏi "đăng được chưa", hoặc trước bước giao video của /yt-studio.
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
- `cost.json`: ghi giọng được tạo bằng gì (`tts_local_seconds`, `tts_app_seconds` + `tts_app_engine`, hoặc `tts_seconds`).
- `rights.csv`: đã chạy lại `python -m tools.rights build` sau khi nhập ảnh và giọng (`/kaku-rights-audit`).
- `originality.json`: đủ 8 tiêu chí, kết luận "đạt" (`/kaku-originality-check`).
- `audit.md`: tạo ở mục 3 bên dưới.

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
<chỉ khi có link tiếp thị liên kết hay tài trợ> Tiết lộ: <quan hệ tài trợ / hoa hồng>.

## Tag
<10–15 tag, cách nhau bằng dấu phẩy>

## Hashtag
#<Anime> #<ChủĐề> #Anime

## Nội dung AI (Altered or synthetic content)
<Tick / Không tick> — <lý do>
```

Luật cho mục Nội dung AI (theo tài liệu Policy Safe, mục ai-disclosure-check):
- Không cần khai báo: tranh anime cách điệu rõ ràng, sơ đồ tự dựng, giọng tổng hợp không mạo danh, AI chỉ hỗ trợ kịch bản.
- Cần xem xét tick: hình trông như thật, người thật hay sự kiện thật được mô phỏng (ví dụ dạng S về lịch sử), giọng hay hình của người khác được mô phỏng.
- Luôn ghi lý do. `release_check` gợi ý tick khi video thuộc dạng S hoặc prompt có từ chỉ ảnh chân thực, và báo LƯU Ý nếu metadata ghi "Không tick".
- Khai báo AI **không thay thế** bản quyền, kiểm nguồn hay độ nguyên bản.

Luật cho tiêu đề, mô tả và link:
- Tiêu đề phản ánh đúng nội dung; không dùng từ câu kéo ("SỐC", "không thể tin", "100%"…) hay viết hoa quá nửa. Công cụ báo LƯU Ý.
- Link ngoài dùng `https`, không dùng link rút gọn, và phải liên quan tới video.
- Có link tiếp thị liên kết hay tài trợ thì bắt buộc có dòng `Tiết lộ:`. Thiếu là LỖI.

## 2. Chạy kiểm tra

```bash
python -m tools.release_check videos/<thư-mục> --write-audit     # thêm --no-loudness nếu cần nhanh
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
| Quyền tài sản | Làm theo `/kaku-rights-audit`: chạy lại `build`, thêm dòng nhạc, kiểm điều khoản công cụ còn `can-kiem` |
| Độ nguyên bản | Làm theo `/kaku-originality-check`: chấm đủ 3 tiêu chí của Claude, hoặc sửa kịch bản nếu dưới 12/16 |
| Tiết lộ tài trợ | Thêm dòng `Tiết lộ: …` vào mô tả |
| Duyệt của người | Người dùng điền `audit.md` (mục 3) |

LƯU Ý: không chặn đăng nhưng phải nói với người dùng, ví dụ:
- độ to lệch khỏi khoảng −16 tới −12 LUFS;
- tag ít hơn 10, thiếu Short;
- tiêu đề câu kéo, link không phải https;
- gợi ý khai báo AI khác với metadata;
- `audit.md` ghi rủi ro "inauthentic" là high.

## 3. `audit.md`: người duyệt quyết định

`--write-audit` tạo `videos/<thư-mục>/audit.md` theo khuôn "Pre-publish audit" của tài liệu Policy Safe:

- **Máy điền:**
  - nguồn, quyền tài sản, điểm nguyên bản;
  - rủi ro "reused" và "inauthentic";
  - gợi ý khai báo AI (khối YAML `ai_disclosure`);
  - checklist 10 mục, đánh dấu sẵn những mục máy kiểm được.
- **Rủi ro "inauthentic" là high** khi nhịp đăng hơn 1 video/ngày (đọc từ `channel/topics.md`) hoặc điểm nguyên bản dưới 14. Không che giấu điều này: nói rõ với người dùng.
- **Người dùng điền:**
  - `Owner`;
  - `Human creative contribution`: phần người đã làm;
  - `Disclosure completed`;
  - `Final reviewer`;
  - `Decision`: `publish` / `revise` / `reject`;
  - `Reasons`.
- Chạy lại `--write-audit` thì phần máy được viết lại, phần người điền được giữ.
- **Chưa có `Decision: publish` thì lệnh báo LỖI.** Claude không tự điền quyết định thay người dùng.

Các mục "(người kiểm)" trong checklist cần người dùng tự xem:
- không phát ngôn giả, deepfake, mạo danh hay giọng clone trái phép;
- chủ đề sức khỏe, pháp lý, tài chính, chính trị đã kiểm nguồn chính thức;
- tiêu đề và thumbnail không gây hiểu lầm;
- đã bật khai báo nếu cần;
- không bot, không traffic ảo, không lời kêu gọi thao túng.

## 4. Xem bằng mắt

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

## Lỗi hay gặp

- Chạy `release_check` trước khi chạy lại `rights build` sau khi nhập ảnh và giọng thì báo "rights.csv chưa khớp".
- Claude **không** tự ghi `Decision: publish`. Hook `guard.py` sẽ hỏi lại người dùng nếu Claude thử ghi.
- Video dạng S (người, sự kiện thật): `release_check` gợi ý tick khai báo AI. Metadata ghi "Không tick" thì bị báo LƯU Ý.
- Đăng hơn 1 video/ngày thì `audit.md` ghi rủi ro "inauthentic" là high. Không sửa tay cho thấp đi; nói thật với người dùng.

## 5. Gửi người dùng duyệt

- Gửi bằng SendUserFile: `render/video.vi.mp4`, `render/thumbnail.png`, 3 Short, `metadata.vi.md` và `audit.md`. File quá lớn thì tải lên Google Drive.
- Kèm bảng kết quả `release_check`: các LƯU Ý còn lại và lý do giữ.
- Kèm danh sách việc tự làm trong YouTube Studio, lấy từ cuối kết quả lệnh.
- Hỏi bằng AskUserQuestion: **Đăng** / **Sửa** / **Bỏ**. Ghi câu trả lời, tên người duyệt và phần người đã làm vào `audit.md` đúng như người dùng nói, rồi chạy lại `release_check`. Chỉ khi không còn LỖI mới làm tiếp `/yt-studio` mục 7: `costs record`, Notion, `topics.md`, commit (kèm `rights.csv`, `originality.json`, `audit.md`).

Không commit MP4: `render/` bị gitignore.
