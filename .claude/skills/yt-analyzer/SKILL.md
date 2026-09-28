---
name: yt-analyzer
description: Phân tích các kênh YouTube mẫu (hồ sơ kênh, video vượt trội, transcript) rồi viết channel/references/<handle>.md và cập nhật channel/profile.md cho kênh anime. Dùng khi người dùng gửi link/handle kênh tham khảo, muốn phân tích đối thủ, hoặc cần tạo/cập nhật hồ sơ kênh.
---

# yt-analyzer: phân tích kênh mẫu → hồ sơ kênh

Mục tiêu: **học công thức, không chép nội dung.** Kết quả là các nhận xét về khuôn mẫu, không phải bản sao.

## 0. Chuẩn bị

```bash
pip install -q -r tools/requirements.txt
python -m tools.yt_research profile @canalmangaq   # kiểm tra key + mạng (1 credit, có cache)
```

Nếu lệnh báo thiếu `TRANSCRIPT_API_KEY` hoặc không kết nối được transcriptapi.com, **dừng lại** và hướng dẫn người dùng:
- Menu môi trường cloud ở thanh tiêu đề phiên → Edit → Network access: thêm `transcriptapi.com`.
- Thêm biến môi trường `TRANSCRIPT_API_KEY` (đăng ký miễn phí ở transcriptapi.com, được 100 credit).
- Mở phiên mới.

Không bao giờ yêu cầu người dùng dán key vào chat.

## 1. Dự trù credit

Mỗi kênh tốn khoảng 10 credit: `profile` 1, `outliers` 1 (danh sách mới nhất miễn phí), transcript 8. Hãy báo tổng dự kiến trước. Nếu vượt 60 credit, hỏi người dùng trước khi chạy. Kết quả được cache trong `.cache/transcriptapi/`, nên chạy lại không tốn thêm.

## 2. Với từng kênh

1. `python -m tools.yt_research profile @handle`: ghi lại tên, số người đăng ký, số video, ngôn ngữ, mô tả kênh.
2. `python -m tools.yt_research outliers @handle`: điểm vượt trội = lượt xem ÷ trung vị lượt xem của các video gần đây. Chọn **khoảng 8 video dài (≥ 4 phút)** có điểm cao nhất.
3. `python -m tools.yt_research transcript VIDEO_ID` cho từng video đã chọn, rồi đọc kỹ. Kênh Brazil nói tiếng Bồ Đào Nha, cứ đọc bình thường và ghi nhận xét bằng tiếng Việt.
4. Viết `channel/references/<handle>.md` theo mẫu:

```markdown
# @handle — <tên kênh>
- Người đăng ký / số video / ngôn ngữ / định dạng (có người dẫn? dùng cảnh phim? ảnh?)
## Video vượt trội
| Tiêu đề | Lượt xem | Điểm | Độ dài |
## 30 giây mở đầu: kiểu câu hỏi, lời hứa, cách giữ chân người xem
## Cấu trúc thân bài: các phần, nhịp, điểm gây bất ngờ, lời kêu gọi hành động
## Giọng văn: xưng hô, độ hài hước, tốc độ
## Công thức tiêu đề (dạng khuôn, ví dụ "X bí mật về Y mà ...")
## Chủ đề ăn khách
## Nên học / Không nên bắt chước (kể cả rủi ro bản quyền nếu kênh dùng cảnh phim)
```

Chỉ được trích tối đa 1–2 câu ngắn làm ví dụ. Transcript thô chỉ nằm trong `.cache/`, không bao giờ chép vào repo.

## 3. Tổng hợp thành `channel/profile.md`

Điền các mục có dấu ⏳. Mục 1 và mục 10 đã chốt, không sửa trừ khi người dùng yêu cầu.
- **Khán giả, cấu trúc chuẩn, công thức tiêu đề, chủ đề ăn khách:** rút từ điểm chung của các kênh, không lấy từ một kênh duy nhất.
- **Góc nhìn riêng:** đề xuất 2–3 phương án, nêu phương án khuyên dùng.
- **Linh vật:** đề xuất 2–3 ý tưởng nhân vật tự thiết kế (tên, tính cách, câu cửa miệng, mô tả ngoại hình bằng tiếng Anh để dùng trong prompt ảnh). Không được giống nhân vật anime có sẵn.
- **`STYLE_PROMPT`:** 1 câu tiếng Anh mô tả phong cách tranh thống nhất cho mọi ảnh.
- **Giọng TTS:** gợi ý chạy `python -m tools.tts --test` (khoảng 0,01 USD) để người dùng nghe thử giọng.

Thêm 10 chủ đề đầu tiên vào `channel/topics.md` và chấm điểm theo 4 tiêu chí trong file.

## 4. Người dùng duyệt

Dùng AskUserQuestion để người dùng chọn **góc nhìn** và **linh vật** (mỗi câu hỏi có các phương án, đánh dấu phương án khuyên dùng). Cập nhật `profile.md` theo lựa chọn, rồi đổi dòng trạng thái đầu file thành:

`> **Trạng thái:** ĐÃ DUYỆT ngày YYYY-MM-DD.`

## 5. Lưu lại

Commit các file `channel/` rồi push lên nhánh đang làm việc. Tóm tắt cho người dùng: điểm chung của các kênh, góc nhìn đã chọn, 3 chủ đề nên làm đầu tiên, và số credit đã dùng.
