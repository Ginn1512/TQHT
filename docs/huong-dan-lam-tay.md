# Hướng dẫn làm tay: ảnh và giọng Kaku

Giai đoạn đầu, ảnh và giọng đều làm tay nên **không tốn tiền API**. Mỗi video có sẵn hai chỗ để lấy prompt:

- **Trang "Xưởng Kaku"** của video (khuyên dùng trên điện thoại): mỗi prompt có nút sao chép, có nút tải ảnh và file giọng lên, có tiến độ và danh sách kiểm tra.
- **File `videos/<thư-mục>/prompts.vi.md`**: nội dung giống hệt, mở bằng app GitHub. Mỗi prompt nằm trong một khối có nút sao chép.

Khi được bật kiếm tiền, cùng các prompt này sẽ chạy qua API (Gemini, ElevenLabs hoặc model khác) mà không phải soạn lại (xem `docs/tu-dong-hoa.md`).

## 0. Làm một lần cho cả kênh

### Ảnh mẫu Kaku

1. Dán prompt "Ảnh mẫu Kaku" (phần 1) vào Gemini app, tạo 2–4 lần.
2. Chọn ảnh đúng mẫu nhất: kính tròn vàng, khăn len đỏ, cuộn giấy, lông nâu kem, dáng chibi.
3. Lưu vào album "Kaku" trên điện thoại, rồi tải lên thẻ **REF** trên trang Xưởng. Mình sẽ lưu ảnh đó vào `channel/brand/kaku-ref.png` để dùng lại sau này.

### Giọng Kaku (chọn 1 trong 3)

Trên trang Xưởng, tab **Giọng**, có 3 bản mô tả giọng (nam giọng Bắc, nam giọng Nam, nữ giọng Bắc) và một đoạn đọc thử.

- **Google AI Studio** (miễn phí, cùng tài khoản Google): vào aistudio.google.com, mở phần tạo giọng nói, dùng **Voice Design**. Dán mô tả giọng, đọc thử đoạn mẫu, lưu giọng.
- **ElevenLabs**: vào Voices → Voice Design, dán mô tả giọng, nghe thử với đoạn mẫu, rồi Save.

Nghe cả 3 giọng rồi nhắn mình, ví dụ "chọn giọng nam-bac". Mình sẽ ghi vào `channel/giong-kaku.json`. Từ đó mọi video dùng đúng một giọng này.

## 1. Ảnh cho mỗi video (khoảng 1,5–2 giờ, chia làm nhiều lần được)

1. Mở tab **Ảnh** trên trang Xưởng.
2. Với mỗi cảnh:
   1. Bấm **Sao chép prompt**.
   2. Mở Gemini app và dán prompt. Nếu cảnh có nhãn **Kaku**, đính kèm ảnh mẫu Kaku trước khi gửi.
   3. Bấm nút tải ảnh gốc về máy. **Không chụp màn hình**, vì ảnh chụp màn hình bị mờ và dính khung giao diện.
   4. Quay lại trang Xưởng, bấm **Tải ảnh lên** ở đúng cảnh.
3. Mẹo để ảnh đồng đều:
   - Làm từng chương trong cùng một cuộc trò chuyện.
   - Ảnh lệch phong cách thì gửi thêm câu "Same style as the previous image" rồi tạo lại.
4. Tạo lại ngay (hoặc bấm **Cần làm lại**) nếu ảnh có một trong các lỗi sau:
   - chữ lạ;
   - tay hoặc mặt dị dạng;
   - giống một nhân vật anime có thật;
   - sai bảng màu (không có tông navy và vàng hổ phách);
   - Kaku không giống ảnh mẫu.

## 2. Giọng cho mỗi video (khoảng 30–45 phút)

Mỗi video chia thành khoảng 7–9 **đoạn đọc** (`c01`, `c02`…), mỗi đoạn khoảng 2 phút.

- **Nếu dùng AI Studio:**
  1. Chọn giọng Kaku đã lưu.
  2. Dán **Ghi chú đạo diễn** vào ô hướng dẫn phong cách (Style instructions). Chỉ cần dán một lần.
  3. Dán **bản Gemini** của đoạn `c01` vào ô văn bản rồi chạy.
  4. Nghe lại, rồi tải file về.
- **Nếu dùng ElevenLabs:**
  1. Chọn model **Eleven v3** và giọng Kaku.
  2. Dán **bản ElevenLabs** của đoạn (đã có sẵn các thẻ `[pause]`, `[chuckles]`, `[curious]`).
  3. Bấm Generate rồi tải file về.
- **Sau khi có file:** tải lên đúng thẻ đoạn trên trang Xưởng. Trang sẽ báo nếu thời lượng lệch hơn 20% so với dự kiến.
- **Lưu ý:**
  - Cả video phải dùng **một công cụ và một giọng**, để các đoạn nối vào nhau liền mạch.
  - Nếu thẻ trong ngoặc bị đọc thành chữ, chuyển sang **bản thường** (tab Giọng → Bản thường).
  - Nếu tên riêng bị đọc sai, chỉ sửa cách viết ngay trong ô của công cụ (ví dụ viết kiểu phiên âm). Không sửa kịch bản.

## 3. Báo mình

Nhắn **"xong ảnh + giọng video N"**. Mình sẽ:

1. Nhập ảnh (`tools.app_images import`) và giọng (`tools.app_audio import`). Giọng được tự cắt thành từng cảnh tại các khoảng lặng.
2. Dựng video, rồi gửi MP4, thumbnail, thông tin đăng tải và 3 Short (`tools.shorts`).
3. Cập nhật trạng thái video trong Notion (trang "Cú Kaku anime") và trong `channel/topics.md`.

Nếu không dùng được trang Xưởng, bạn có thể bỏ ảnh (tên `s01.png`…) và file giọng (tên `c01.wav`…) vào một thư mục Google Drive rồi gửi link cho mình.
