---
name: yt-studio
description: Sản xuất một video YouTube phân tích anime từ chủ đề đến MP4 hoàn chỉnh — nghiên cứu, kịch bản tiếng Việt, chia cảnh, giọng đọc Gemini TTS, ảnh AI, dựng video, thumbnail, tiêu đề/mô tả, và các bản lồng tiếng khác. Dùng khi người dùng muốn làm video mới, làm lại một cảnh, hoặc thêm bản lồng tiếng cho video đã có.
---

# yt-studio: từ chủ đề đến video

Nguồn sự thật duy nhất là `channel/profile.md`. **Không đọc transcript của kênh mẫu** (trong `.cache/` hoặc bất kỳ đâu) khi làm video.

## 0. Chuẩn bị

1. `channel/profile.md` phải có dòng `ĐÃ DUYỆT`. Nếu chưa có, chạy `/yt-analyzer` trước.
2. `pip install -q -r tools/requirements.txt`
3. Kiểm tra `GEMINI_API_KEY` bằng `python -m tools.gemini models`. Nếu thiếu, hướng dẫn người dùng thêm biến môi trường trong cài đặt môi trường cloud rồi mở phiên mới. Không bao giờ yêu cầu dán key vào chat. Nếu model trong `tools/config.py` không còn trong danh sách, đặt `YT_TTS_MODEL` / `YT_IMAGE_MODEL` hoặc sửa `config.py`.
4. Xem profile đang bật những ngôn ngữ nào. Video 1–3 chỉ làm tiếng Việt.

## 1. Nghiên cứu → `videos/<YYYY-MM-DD>-<slug>/brief.md`

- Chủ đề, góc nhìn, câu hỏi mà video trả lời cho người xem.
- Mức spoiler: tới chương hoặc tập nào.
- **Danh sách sự thật kèm URL nguồn** (wiki, nguồn chính thức, phỏng vấn tác giả), tìm bằng WebSearch. Lý thuyết của fan phải ghi rõ là lý thuyết.
- 3 ý tưởng tiêu đề và 1 ý tưởng thumbnail.

## 2. Kịch bản → `script.vi.md`

- **Khoảng 2.600–3.500 từ (≈ 15–20 phút; không được dưới 15 phút)**, theo **Cấu trúc video chuẩn** và **Giọng văn** trong profile.
- 30 giây đầu: đưa ra lời hứa hoặc câu hỏi, không chào hỏi dài dòng. Nếu có spoiler, cảnh báo ngay trong câu đầu.
- Cứ 60–90 giây có một điểm gây bất ngờ. Kêu gọi đăng ký ở gần cuối, không đặt ở đầu video.
- Tự kiểm tra trước khi đi tiếp:
  - [ ] Mọi sự thật có nguồn trong brief.
  - [ ] Không có câu chữ lấy từ kênh khác.
  - [ ] Đúng giọng của linh vật.
  - [ ] Độ dài đạt yêu cầu.

## 3. Chia cảnh → `scenes.json` (cấu trúc xem trong `tools/scenes.py`)

- Mỗi cảnh gồm 1–3 câu, dài 8–15 giây (khoảng 100–190 ký tự tiếng Việt), tổng khoảng 90–110 cảnh. Id đặt theo dạng `s01`, `s02`, …
- Chép `style_prompt` và `mascot_prompt` từ profile vào đầu file.
- `image_prompt` (tiếng Anh):
  - Mô tả một bố cục tự nghĩ ra.
  - **Không ghi tên nhân vật hay tên anime.** Không mô tả lại trang phục hoặc kiểu tóc đặc trưng của nhân vật có bản quyền. Thay vào đó dùng nhân vật kiểu mẫu chung, bóng người, đồ vật tượng trưng, phong cảnh, hoặc cảnh sơ đồ/so sánh.
- `on_screen_text` tối đa 8 từ, ưu tiên tên riêng và con số. Chữ này được in cứng vào hình và **mọi bản lồng tiếng đều thấy**, nên đừng viết câu dài.
- `use_mascot: true` cho mở đầu, chuyển đoạn và kết thúc (khoảng 15% số cảnh).
- `chapter` ở 6–9 cảnh bắt đầu phần mới. Cảnh đầu tiên luôn có chapter.

## 4. Báo chi phí và chờ duyệt

```bash
python -m tools.costs estimate videos/<thư-mục>
```

Dùng AskUserQuestion, kèm tóm tắt: tiêu đề làm việc, độ dài ước tính, số cảnh, chi phí, số tiền đã chi trong tháng. Người dùng chọn: **Tạo video** / **Sửa kịch bản trước**. Chưa được đồng ý thì không gọi API tốn tiền.

## 5. Tạo giọng, ảnh và dựng video

```bash
python -m tools.tts videos/<thư-mục> --lang vi
python -m tools.images videos/<thư-mục>
python -m tools.assemble videos/<thư-mục>        # thêm --music <file> nếu người dùng có nhạc không bản quyền
```

- Dùng Read xem ngẫu nhiên khoảng 5 ảnh. Nếu ảnh có chữ lạ, dị dạng, hoặc quá giống nhân vật có bản quyền, sửa `image_prompt` rồi vẽ lại bằng `python -m tools.images videos/<thư-mục> --only s03,s07`. Ảnh cũ nằm trong cache, không tốn lại.
- Sửa lời thoại một cảnh thì chỉ cảnh đó bị tạo giọng lại.
- Xem `render/report.json` và trích 2–3 khung hình để kiểm tra.

## 6. Thumbnail và thông tin đăng tải

```bash
python -m tools.thumbnail videos/<thư-mục> --text "CHỮ NGẮN 3-6 TỪ" --bg s05
```

Soạn `metadata.vi.md`:
- 3 phương án tiêu đề (≤ 60 ký tự, tên anime đặt ở đầu).
- Mô tả: 2 dòng mở đầu hấp dẫn, danh sách chương lấy từ `render/chapters.txt`, danh sách nguồn tham khảo, và dòng "Hình minh họa do AI tạo, không phải hình chính thức. Video phân tích của fan."
- 10–15 tag và 3 hashtag.
- Khai báo nội dung AI: tranh anime cách điệu rõ ràng không thật thì **không** cần tick "Altered or synthetic content". Nếu có hình giống người thật hoặc sự kiện thật thì phải tick.

## 7. Giao video và duyệt lần cuối

- Gửi `render/video.vi.mp4`, `render/thumbnail.png` và `metadata.vi.md` bằng SendUserFile. Nếu file quá lớn, tải lên Google Drive của người dùng.
- Dùng AskUserQuestion: **Đăng** / **Sửa** (người dùng ghi rõ cần sửa gì).
- Sau khi người dùng đồng ý:
  - chạy `python -m tools.costs record videos/<thư-mục>`
  - cập nhật trạng thái chủ đề trong `channel/topics.md`
  - commit (không commit MP4, vì `assets/` và `render/` đã bị gitignore) rồi push.
- Hướng dẫn đăng video:
  1. App YouTube Studio: tải video lên, dán tiêu đề và mô tả, đặt thumbnail, chọn "Không dành cho trẻ em", hẹn giờ đăng.
  2. YouTube Studio bản web: tải `subs.vi.srt` vào mục Phụ đề.

## 8. Thêm bản lồng tiếng (khi profile đã bật ngôn ngữ đó)

1. Dịch `narration` sang ngôn ngữ mới ngay trong `scenes.json`, thêm mã ngôn ngữ vào `languages`.
   - Dịch tự nhiên, dùng thuật ngữ mà fan ở nước đó hay dùng.
   - Giữ độ dài tương đương bản gốc.
   - Tiếng Trung dùng chữ phồn thể (`zh-TW`).
2. Ước tính chi phí: `python -m tools.costs estimate videos/<thư-mục> --no-images --lang en --lang pt-BR`, rồi chờ người dùng duyệt.
3. `python -m tools.tts videos/<thư-mục> --lang en` (lặp lại cho từng ngôn ngữ), sau đó `python -m tools.assemble videos/<thư-mục>`.
4. Nếu `report.json` báo "cần rút gọn bản dịch", rút ngắn các cảnh được liệt kê rồi chạy lại tts cho ngôn ngữ đó.
5. Soạn `metadata.<lang>.md` (tiêu đề và mô tả đã dịch). Gửi `audio.<lang>.m4a` và `subs.<lang>.srt` cho người dùng. Người dùng thêm chúng trong YouTube Studio bản web → Ngôn ngữ (bản âm thanh, phụ đề, tiêu đề/mô tả dịch).
