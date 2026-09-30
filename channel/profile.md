# Hồ sơ kênh (profile)

> **Trạng thái:** ĐÃ DUYỆT SƠ BỘ ngày 2026-09-28 (người dùng chọn góc nhìn và linh vật).
> Các mục 2, 5–7, 9 là suy luận từ tìm kiếm web và kinh nghiệm chung của thể loại, **chưa có lời thoại kênh mẫu**. Khi có `TRANSCRIPT_API_KEY`, chạy `/yt-analyzer` để đối chiếu và sửa (xem `channel/references/so-bo-web.md`).
> Skill `yt-studio` chỉ đọc file này, không đọc transcript của kênh mẫu.

## 1. Định vị (đã chốt)

- **Ngách:** phân tích / giải thích anime: sức mạnh, bí ẩn, lý thuyết, top 10, so sánh.
- **Mục tiêu:** đủ điều kiện kiếm tiền (YPP) trong 1–3 tháng, làm tay trước (xem `docs/lo-trinh.md`).
- **Định dạng:** video dài **15–20 phút** (bắt buộc, không làm ngắn hơn 15 phút), 3 video/ngày lúc 06:00, 14:00, 22:00. Mỗi ngày 1 Short dọc lúc 18:00, cắt từ video 06:00 cùng ngày (`tools/shorts.py`): dài 35–58 giây, là một cụm cảnh ở đầu một chương, có phụ đề chữ to.
- **Hình ảnh:** tranh AI tự vẽ theo phong cách anime, cộng chữ trên màn hình và sơ đồ. **Không dùng cảnh phim, ảnh chụp màn hình, trang manga hay art chính thức.**
- **Ngôn ngữ:** tiếng Việt là chính. Lồng tiếng thêm theo lộ trình:
  - video 1–3: chỉ tiếng Việt (`vi`)
  - tiếp theo: thêm `en` và `pt-BR`
  - sau cùng: thêm `hi` và `zh-TW`
- **Ngân sách:** trần khoảng 38 USD/tháng. Khi làm tay (ảnh bằng Gemini app, giọng bằng AI Studio hoặc ElevenLabs) thì gần như 0 USD.

## 2. Khán giả (sơ bộ)

- Fan anime Việt 15–30 tuổi, đã xem các bộ shounen dài kỳ (One Piece, Naruto, Hunter x Hunter, Jujutsu Kaisen, Kimetsu no Yaiba) và isekai/manhwa phổ biến (Solo Leveling).
- Biết tên nhân vật và sự kiện chính, nhưng muốn hiểu **luật vận hành** phía sau: vì sao ai đó mạnh, giới hạn của sức mạnh, các chi tiết cài cắm.
- Xem trên điện thoại, thường tìm bằng từ khóa "giải thích", "là gì", "mạnh nhất".

## 3. Góc nhìn riêng (đã chọn)

**"Giải mã hệ thống sức mạnh & lore"** — mỗi video trả lời một câu hỏi "vận hành thế nào / vì sao" về luật của một thế giới anime, bằng sơ đồ và tranh tự vẽ, có nguồn rõ ràng. Khác kênh mẫu: không phản ứng theo chương, không tóm tắt phim, không cần cảnh gốc.

## 4. Linh vật dẫn chuyện (đã chọn)

- **Tên:** Cú Kaku.
- **Tính cách:** học giả thông thái nhưng hài hước, hay tự nhận "đã đọc hết thư viện" rồi bị chính fan sửa sai; mê vẽ sơ đồ.
- **Câu cửa miệng:** "Mở sổ ra nào!" (đầu video) và "Kaku gấp sổ đây, hẹn gặp lại!" (cuối video).
- **Ngoại hình (dán nguyên vào `mascot_prompt`):**
  `a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design`

## 5. Giọng văn (sơ bộ)

- Xưng "mình", gọi khán giả "các bạn". Thân mật, rõ ràng, không la hét câu view.
- Câu ngắn; thuật ngữ gốc (Nen, Haki…) giữ nguyên, giải thích bằng tiếng Việt ngay lần đầu xuất hiện.
- Hài hước nhẹ qua lời Kaku, không mỉa mai nhân vật hay fan.
- **Giọng Kaku** (cấu hình trong `channel/giong-kaku.json`):
  - 3 bản mô tả cho Voice Design: nam giọng Bắc, nam giọng Nam, nữ giọng Bắc. Bạn nghe thử rồi chọn một; mã giọng đã chọn ghi vào `chosen`.
  - Ghi chú đạo diễn cố định: giọng ấm, tò mò, tự tin; khoảng 13 ký tự/giây; dừng ngắn trước mỗi điểm bất ngờ; không la hét.
  - Bảng thẻ cho từng công cụ: Gemini `<short pause>` `<laugh>`; ElevenLabs `[pause]` `[chuckles]` `[curious]`; bản thường không có thẻ.
- **Làm giọng:** mặc định làm tay trên AI Studio hoặc ElevenLabs, dùng các đoạn đọc soạn sẵn trong trang Xưởng hoặc `prompts.vi.md`. Qua API (`tools/tts.py`, giọng mặc định `Kore`) chỉ là dự phòng, hoặc dùng sau khi tự động hóa.

## 6. Cấu trúc video chuẩn (sơ bộ)

- **0–30 giây:** một câu hỏi cụ thể + lời hứa trả lời ("Vì sao Gon mất hết Nen? Hết video này bạn sẽ hiểu luật Nen đủ để tự đoán."). Cảnh báo spoiler nếu có. Kaku chào bằng câu cửa miệng.
- **30–90 giây:** bối cảnh tối thiểu, chỉ những gì cần cho câu hỏi.
- **Thân bài 5–7 phần** (mỗi phần 2–3 phút), mỗi phần là một chương, mở bằng một câu hỏi con và khép bằng một điểm bất ngờ hoặc một sơ đồ tổng kết.
- **Kết:** tóm tắt bằng một sơ đồ; câu hỏi cho phần bình luận; kêu gọi đăng ký nằm ở đây, không đặt ở đầu.
- **Nhịp:** đổi hình mỗi 8–15 giây; cứ 60–90 giây có một điểm gây bất ngờ.

## 7. Công thức tiêu đề và thumbnail (sơ bộ)

Tiêu đề ≤ 60 ký tự, tên anime đặt ở đầu, hứa đúng thứ video trả lời:
- `[Anime]: [Hệ thống] hoạt động thế nào? (Giải thích dễ hiểu)`
- `[Anime]: Vì sao [nhân vật] lại [điều bất ngờ]?`
- `[Anime]: [N] luật của [hệ thống] mà nhiều fan hiểu sai`
- `[Anime]: Xếp hạng [N] [loại sức mạnh] từ yếu đến mạnh`

Thumbnail: 3–5 từ chữ lớn (dòng cuối màu vàng), Kaku hoặc một biểu tượng sức mạnh, nền tối có một điểm sáng. Không dùng art chính thức.

## 8. Phong cách hình ảnh: "Sổ tay Kaku"

Nét riêng của kênh: mọi ảnh trông như một trang trong sổ tay của học giả cú. Tranh anime cel-shading, nét sạch; vệt phác thảo mực mờ và vân giấy da ở mép khung; bảng màu cố định gồm bóng navy, điểm sáng vàng hổ phách và **một** điểm nhấn đỏ son (trùng màu khăn Kaku, thumbnail và sơ đồ).

- `STYLE_PROMPT` (chép vào `style_prompt` của `scenes.json`):
  `Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only`
- **Khuôn prompt 6 lớp** (`tools/images.build_prompt`, dùng chung cho Gemini app và API):
  1. khung 16:9;
  2. chủ thể và hành động (`image_prompt`), cộng mô tả Kaku nếu cảnh có linh vật;
  3. cỡ cảnh / góc máy;
  4. ánh sáng;
  5. `STYLE_PROMPT`;
  6. cấm (`GUARD`).

  Lớp 3 và 4 được tự thêm theo nội dung cảnh nếu `image_prompt` chưa ghi. Kịch bản mới nên tự ghi cả hai để kiểm soát tốt hơn.
- **Negative prompt** (cho model có ô riêng): `images.NEGATIVE`.
- **Ảnh mẫu Kaku** dùng cho cả kênh: tạo một lần bằng prompt "model sheet", lưu ở `channel/brand/kaku-ref.png`, đính kèm làm ảnh tham chiếu cho mọi cảnh có Kaku.
- Chữ trên màn hình: font Be Vietnam Pro ExtraBold (`assets/fonts/`), hộp tối bán trong suốt, tối đa 8 từ.
- Sơ đồ: nền tối, đường trắng, một màu nhấn vàng.

## 9. Chủ đề ăn khách (sơ bộ)

- Giải thích hệ thống sức mạnh của các bộ dài kỳ đang được bàn nhiều (xem `channel/topics.md`).
- Lý thuyết về bí ẩn chưa được giải đáp (ghi rõ là lý thuyết).
- Xếp hạng trong một hệ thống (cấp bậc, loại năng lực).
- Sẽ kiểm chứng bằng video vượt trội của kênh mẫu khi có dữ liệu.

## 10. Danh sách CẤM

- Không chép câu chữ, cấu trúc câu đặc trưng, câu cửa miệng hay tiêu đề của kênh mẫu.
- Không dùng cảnh phim, ảnh chụp, trang manga, art chính thức hay nhạc có bản quyền.
- Không vẽ lại chính xác nhân vật có bản quyền. Dùng dáng người, bóng, biểu tượng hoặc cảnh gợi ý.
- Không đưa thông tin không có nguồn. Tin đồn, leak, lý thuyết phải nói rõ là lý thuyết.
- Không spoil chương hoặc tập mới mà không cảnh báo trước ở đầu video.
- Không giả làm chuyên gia (bác sĩ, luật sư, nhà khoa học…). Kaku là cú kể chuyện, nói rõ khi nào là ý kiến của kênh.
- Không tạo lời phát biểu giả cho người thật (tác giả, diễn viên lồng tiếng, nhân vật lịch sử). Trích lời thì phải có nguồn.
- Không dùng giọng clone hay khuôn mặt của người thật. Giọng Kaku là giọng thiết kế bằng mô tả (`channel/giong-kaku.json`).
- Không dùng bot, mua view, like, bình luận hay người đăng ký. Không dùng lời kêu gọi thao túng (hứa thưởng, dọa, đổi like lấy nội dung).
- Tiêu đề và thumbnail không dùng người nổi tiếng, sự kiện hay cảnh không có trong video, không hứa điều video không có.
- Không làm hàng loạt video gần như giống nhau chỉ thay tên anime. Mỗi video một luận điểm riêng (`python -m tools.originality`).
- Thiếu nguồn, giấy phép hay độ chính xác thì ghi UNKNOWN và không đăng. Xem `docs/chinh-sach-noi-dung.md`.
