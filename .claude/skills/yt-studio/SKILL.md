---
name: yt-studio
description: Sản xuất một video YouTube phân tích anime từ chủ đề đến MP4 hoàn chỉnh — nghiên cứu, kịch bản tiếng Việt, chia cảnh, bộ prompt ảnh + giọng, trang Xưởng Kaku để người dùng làm tay (Gemini app, AI Studio, ElevenLabs), nhập ảnh/giọng, dựng video, 3 Short, thumbnail, tiêu đề/mô tả, và các bản lồng tiếng khác. Dùng khi người dùng muốn làm video mới, báo "xong ảnh + giọng", làm lại một cảnh, hoặc thêm bản lồng tiếng.
---

# yt-studio: từ chủ đề đến video

Nguồn sự thật duy nhất là `channel/profile.md`. **Không đọc transcript của kênh mẫu** (trong `.cache/` hoặc bất kỳ đâu) khi làm video.

## 0. Chuẩn bị

1. `channel/profile.md` phải có dòng `ĐÃ DUYỆT`. Nếu chưa có, chạy `/yt-analyzer` trước.
2. `pip install -q -r tools/requirements.txt`
3. Chỉ khi sẽ dùng API (ảnh hoặc giọng): kiểm tra `GEMINI_API_KEY` bằng `python -m tools.gemini models`. Làm tay thì không cần key. Nếu thiếu, hướng dẫn người dùng thêm biến môi trường trong cài đặt môi trường cloud rồi mở phiên mới. Không bao giờ yêu cầu dán key vào chat. Nếu model trong `tools/config.py` không còn trong danh sách, đặt `YT_TTS_MODEL` / `YT_IMAGE_MODEL` hoặc sửa `config.py`.
4. Xem profile đang bật những ngôn ngữ nào. Video 1–3 chỉ làm tiếng Việt.

## 1. Nghiên cứu → `videos/<YYYY-MM-DD>-<slug>/brief.md`

- Nếu mục mới nhất trong `channel/references/nhat-ky-hoc-hoi.md` đã quá 2 tuần, hoặc bộ anime chưa từng làm: chạy skill `/yt-research` trước.
- Chọn dạng video trong `channel/formats.md` theo `channel/topics.md` và **theo đúng khung của dạng đó** (mở đầu, chương đặc thù, cách kết). Không lặp khung của video trước.
- Đầu `brief.md` là các dòng mà `tools.canon` và `tools.originality` đọc:
  ```markdown
  - **Anime:** …
  - **Dạng video:** <mã> · <tên dạng>
  - **Câu hỏi video trả lời:** câu hỏi người xem cần giải quyết.
  - **Luận điểm riêng:** một câu, điều kênh khẳng định mà wiki không viết sẵn.
  - **Mức spoiler:** tới chương hoặc tập nào.
  - **Độ dài mục tiêu:** 15–20 phút.
  ```
- **Bảng "Sự thật dùng trong kịch bản" kèm URL nguồn** (wiki, nguồn chính thức, phỏng vấn tác giả), tìm bằng WebSearch. Chủ đề cần dữ kiện thật thì có ít nhất 3 nguồn. Phân biệt dữ kiện, suy luận và ý kiến; lý thuyết của fan phải ghi rõ là lý thuyết. Ô tình trạng theo các mức trong `/kaku-canon-ledger`.
- `## Điều chưa chắc chắn`: chi tiết còn tranh cãi hoặc chưa kiểm được, và cách kịch bản nói về chúng.
- `## Rủi ro bản quyền/chính sách`: người thật, sự kiện thật, chủ đề nhạy cảm (sức khỏe, pháp lý, tài chính, chính trị), nguy cơ vẽ giống nhân vật có bản quyền. Không có thì ghi "không".
- 3 ý tưởng tiêu đề không gây hiểu lầm và 1 ý tưởng thumbnail.

## 2. Kịch bản → `script.vi.md`

- **Khoảng 2.600–3.500 từ (≈ 15–20 phút; không được dưới 15 phút)**, theo **Cấu trúc video chuẩn** và **Giọng văn** trong profile.
- 30 giây đầu: đưa ra lời hứa hoặc câu hỏi, không chào hỏi dài dòng. Nếu có spoiler, cảnh báo ngay trong câu đầu.
- Cứ 60–90 giây có một điểm gây bất ngờ. Kêu gọi đăng ký ở gần cuối, không đặt ở đầu video.
- Tự kiểm tra trước khi đi tiếp:
  - [ ] Mọi sự thật có nguồn trong brief.
  - [ ] Không có câu chữ lấy từ kênh khác, không dịch hay viết lại gần nguyên văn một bài viết.
  - [ ] Có luận điểm riêng, ví dụ hoặc phép so sánh riêng, và nói rõ giới hạn hay điểm chưa chắc chắn.
  - [ ] Không giả làm chuyên gia, không bịa lời phát biểu của người thật (tác giả, diễn viên lồng tiếng…).
  - [ ] Lời kêu gọi không thao túng: không hứa thưởng, không dọa, không đổi like lấy nội dung.
  - [ ] Đúng giọng của linh vật.
  - [ ] Độ dài đạt yêu cầu.

## 3. Chia cảnh → `scenes.json` (cấu trúc xem trong `tools/scenes.py`)

- Mỗi cảnh gồm 1–3 câu, dài 8–15 giây (khoảng 100–190 ký tự tiếng Việt), tổng khoảng 90–110 cảnh. Id đặt theo dạng `s01`, `s02`, …
- Chép `style_prompt` và `mascot_prompt` từ profile vào đầu file.
- `image_prompt` (tiếng Anh):
  - Mô tả một bố cục tự nghĩ ra: chủ thể + hành động + bối cảnh, **kèm cỡ cảnh / góc máy và ánh sáng** (ví dụ "close-up", "wide establishing shot", "lit by a single desk lamp"). Nếu thiếu, `images.build_prompt` sẽ tự thêm theo quy tắc, nhưng tự ghi thì kiểm soát tốt hơn.
  - **Không ghi tên nhân vật hay tên anime.** Không mô tả lại trang phục hoặc kiểu tóc đặc trưng của nhân vật có bản quyền. Thay vào đó dùng nhân vật kiểu mẫu chung, bóng người, đồ vật tượng trưng, phong cảnh, hoặc cảnh sơ đồ/so sánh.
  - Không yêu cầu chữ trong ảnh. Chữ được chèn khi dựng.
- Chạy `python -m tools.prompt_check videos/<thư-mục>`: phải báo "không có vi phạm". Gặp tên hoặc chi tiết đặc trưng mới thì thêm vào `channel/prompt-blocklist.txt`.
- Chạy `python -m tools.prompt_pack videos/<thư-mục>` để tạo `prompts.vi.md` (prompt ảnh 6 lớp + các đoạn đọc cho Gemini và ElevenLabs). Mỗi lần sửa `scenes.json` thì chạy lại.
- `on_screen_text` tối đa 8 từ, ưu tiên tên riêng và con số. Chữ này được in cứng vào hình và **mọi bản lồng tiếng đều thấy**, nên đừng viết câu dài.
- `use_mascot: true` cho mở đầu, chuyển đoạn và kết thúc (khoảng 15% số cảnh).
- `chapter` ở 6–9 cảnh bắt đầu phần mới. Cảnh đầu tiên luôn có chapter.

## 4. Báo chi phí và chờ duyệt

```bash
python -m tools.costs estimate videos/<thư-mục> --no-images --no-tts   # làm tay cả ảnh lẫn giọng (mặc định): 0 USD
python -m tools.costs estimate videos/<thư-mục> --no-images            # nếu tạo giọng bằng API
python -m tools.costs estimate videos/<thư-mục>                        # nếu tạo cả ảnh bằng API
```

Dùng AskUserQuestion, kèm tóm tắt: tiêu đề làm việc, độ dài ước tính, số cảnh, chi phí, số tiền đã chi trong tháng. Người dùng chọn: **Tạo video** / **Sửa kịch bản trước**. Chưa được đồng ý thì không gọi API tốn tiền. Khi làm tay hoàn toàn (0 USD) thì chỉ cần người dùng duyệt kịch bản.

## 5. Ảnh, giọng và dựng video

**Trước khi làm ảnh và giọng:** `python -m tools.originality check videos/<thư-mục>` phải ra "đạt" (xem `/kaku-originality-check`). Dưới 12/16 thì viết lại kịch bản trước.

**Trước khi làm giọng:** `python -m tools.canon check videos/<thư-mục>` phải đạt. Còn dòng chưa kiểm thì làm theo `/kaku-canon-ledger` trước, vì sửa kịch bản sau khi có giọng là phải làm lại giọng. Ảnh thì làm song song được.

**Sau khi nhập ảnh và giọng:** `python -m tools.rights build videos/<thư-mục>` để ghi công cụ thật vào `rights.csv` (xem `/kaku-rights-audit`).

**Cách mặc định: người dùng làm tay trên trang "Xưởng Kaku"** (ảnh bằng Gemini app, giọng bằng AI Studio hoặc ElevenLabs; hướng dẫn trong `docs/huong-dan-lam-tay.md`):

1. `python -m tools.xuong page videos/<thư-mục> --label "video N" > <scratchpad>/xuong-N.html`, rồi đăng bằng Artifact với `capabilities: {"assets": {}, "db": {}}`. Mỗi video một trang (video 1: https://claude.ai/artifact/JZThW5cMae5U9pbrvRsYSr). Ghi link vào cột "Link Xưởng" của video trong bảng Notion "Video dài" (data source `80099179-a3b2-4816-8862-0a4d1d3db805`) và đổi Trạng thái sang "Đang làm ảnh".
2. Gửi link cho người dùng. Trang có 3 tab:
   - **Ảnh:** sao chép prompt → Gemini → tải ảnh lên. Cảnh có Kaku thì đính kèm ảnh mẫu Kaku.
   - **Giọng:** chọn công cụ, dán ghi chú đạo diễn, dán từng đoạn đọc `c01`… rồi tải file lên.
   - **Kiểm tra:** danh sách tiêu chí, và báo "Sẵn sàng dựng" khi đủ.
3. Khi người dùng báo "xong ảnh + giọng video N":
   - `ArtifactData list` các collection `images` và `audio` (`query.limit` 200) để lấy asset id.
   - Tải từng asset bằng `Artifact read` với `path=<asset id>`, lưu vào thư mục tạm:
     - ảnh đặt tên `<scene-id>.<đuôi>`;
     - giọng đặt tên `<cNN>.txt`. Đây là gói base64 có dòng đầu `KAKU-AUDIO-B64`, vì kho tệp của trang không nhận file âm thanh.
   - Ảnh có `redo: true` thì báo lại cho người dùng, chưa nhập.
   - `python -m tools.app_images import videos/<thư-mục> --from <tạm>` (thêm `--trim 0.05` nếu ảnh có watermark ở góc).
   - `python -m tools.app_audio import videos/<thư-mục> --from <tạm> --engine gemini` (hoặc `elevenlabs`, theo công cụ người dùng đã chọn trên trang): mỗi đoạn tự được cắt thành giọng từng cảnh tại các khoảng lặng. Thiếu `--engine` thì sổ quyền ghi giọng là UNKNOWN và chặn đăng.
   - Nếu ảnh mẫu Kaku (`images/kaku-ref`) chưa có trong `channel/brand/kaku-ref.png` thì lưu vào đó.
4. Cảnh hoặc đoạn nào thiếu hay hỏng thì báo số cảnh / số đoạn để người dùng làm lại trên trang.

**Giọng bằng VoiceStudio trên PC của người dùng** (0 USD, xem `docs/voicestudio.md`):
- Người dùng tự chạy `python -m tools.voicestudio run videos/<thư-mục>` trên PC. Lệnh không chạy được trong phiên cloud vì không với tới `localhost:3900`.
- Chỉ dùng engine `voxcpm2` (Apache-2.0). Không dùng `omnivoice` (CC-BY-NC 4.0, phi thương mại); công cụ tự chặn.
- Nếu người dùng gửi `giong-vi.zip` (tải từ Google Drive): `python -m tools.voicestudio unpack videos/<thư-mục> --from <zip>`, rồi dựng như bình thường.

Chỉ khi người dùng yêu cầu mới dùng API: `python -m tools.images videos/<thư-mục>` (khoảng 0,034 USD/ảnh), `python -m tools.tts videos/<thư-mục> --lang vi` (khoảng 0,14 USD/video).

```bash
python -m tools.assemble videos/<thư-mục> --draft   # bản nháp không tiếng, 960×540, để duyệt hình khi chưa có giọng
python -m tools.assemble videos/<thư-mục>           # thêm --music <file> nếu người dùng có nhạc không bản quyền
python -m tools.shorts suggest videos/<thư-mục>     # 3 cụm cảnh 35–58 giây
python -m tools.shorts make videos/<thư-mục> --from s19 --to s24 --title "Câu hỏi ngắn gây tò mò"
```

- Muốn có clip chuyển động thật cho vài cảnh "đinh": làm theo skill `/yt-seedance` trước khi chạy `tools.assemble` (tối đa 6 clip × 5 giây).

- Dùng Read xem ngẫu nhiên khoảng 5 ảnh. Nếu ảnh có chữ lạ, dị dạng, hoặc quá giống nhân vật có bản quyền, sửa `image_prompt` rồi vẽ lại bằng `python -m tools.images videos/<thư-mục> --only s03,s07`. Ảnh cũ nằm trong cache, không tốn lại.
- Sửa lời thoại một cảnh thì chỉ cảnh đó bị tạo giọng lại.
- Xem `render/report.json` và trích 2–3 khung hình để kiểm tra.
- **Short:** làm 3 cái mỗi video, tiêu đề là một câu hỏi ngắn (tối đa 8 từ). Đăng 1 Short mỗi ngày giữa hai video dài. Mô tả Short gắn link video dài (dùng tính năng "Video liên quan" của YouTube).

## 6. Thumbnail và thông tin đăng tải

```bash
python -m tools.thumbnail videos/<thư-mục> --text "CHỮ NGẮN 3-6 TỪ" --bg s05
```

Soạn `metadata.vi.md` **đúng khuôn trong `/kaku-release-review` mục 1**, vì `tools.release_check` đọc theo các tiêu đề `##` của khuôn đó:
- 3 phương án tiêu đề (≤ 60 ký tự, tên anime đặt ở đầu).
- Mô tả: 2 dòng mở đầu hấp dẫn, danh sách chương lấy từ `render/chapters.txt`, danh sách nguồn tham khảo, và dòng "Hình minh họa do AI tạo, không phải hình chính thức. Video phân tích của fan."
- 10–15 tag và 3 hashtag.
- Khai báo nội dung AI: tranh anime cách điệu rõ ràng không thật thì **không** cần tick "Altered or synthetic content". Nếu có hình giống người thật hoặc sự kiện thật thì phải tick. `release_check` đưa ra gợi ý và báo LƯU Ý nếu lệch.
- Có link tiếp thị liên kết hay tài trợ thì thêm dòng `Tiết lộ: …` trong mô tả. Link ngoài dùng `https`, không dùng link rút gọn.

## 7. Giao video và duyệt lần cuối

- Làm `/kaku-release-review` trước: `python -m tools.release_check videos/<thư-mục> --write-audit`, rồi người dùng điền `audit.md` và ghi `Decision: publish`. Lệnh không còn LỖI mới được đăng.
- Gửi `render/video.vi.mp4`, `render/thumbnail.png`, 3 file `render/shorts/*.mp4` và `metadata.vi.md` bằng SendUserFile. Nếu file quá lớn, tải lên Google Drive của người dùng.
- Dùng AskUserQuestion: **Đăng** / **Sửa** (người dùng ghi rõ cần sửa gì).
- Sau khi người dùng đồng ý:
  - chạy `python -m tools.costs record videos/<thư-mục>`
  - cập nhật trạng thái chủ đề trong `channel/topics.md`
  - cập nhật Notion (trang "Cú Kaku anime", cấu trúc trong `docs/tu-dong-hoa.md`):
    - dòng của video trong "Video dài": Trạng thái, Link YouTube, Phút, Chi phí USD, Giờ làm tay;
    - thêm 3 dòng vào "Shorts" (`f057bfe8-e21f-4b2a-8518-87b1b891dd1c`), liên kết tới video gốc.
  - commit `rights.csv`, `originality.json`, `audit.md` cùng các file khác (không commit MP4, vì `assets/` và `render/` đã bị gitignore) rồi push.
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
