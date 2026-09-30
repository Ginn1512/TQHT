# Bộ prompt · Dược sư tự sự: Nhập môn thế giới hậu cung, thuốc và độc

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 7 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (86 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Video này gần như không có spoiler: Kaku chỉ nói về thế giới, nhân vật và vụ án đầu tiên ở những tập đầu mùa…

```text
Wide 16:9 landscape cinematic frame. an elegant palace gate at dusk with red lanterns, the doors slightly open. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02 · **Kaku** (đính kèm ảnh mẫu)

Lời: Ở một kênh chuyên giải mã hệ thống sức mạnh, hôm nay Kaku giới thiệu một bộ không có phép thuật, không có siê…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at an empty power-system chart with a puzzled face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Vũ khí duy nhất của nhân vật chính là một thứ: kiến thức về thuốc và độc. Và trong một hoàng cung đầy âm mưu,…

```text
Wide 16:9 landscape cinematic frame. a small herb basket and a silver needle resting on a lacquered table in a palace room. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đó là Dược sư tự sự, bộ anime đang phát mùa ba từ tháng mười năm 2026. Mở sổ ra nào! Mình là Kaku, và đây là…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook with pressed herbs between its pages. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Một lưu ý quan trọng: video có nhắc tới thuốc và chất độc trong bối cảnh truyện. Đây không phải lời khuyên y…

```text
Wide 16:9 landscape cinematic frame. a warning note pinned beside a jar of dried herbs, a doctor icon on it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Bộ truyện này là gì?

Lời: Dược sư tự sự khởi đầu là một tiểu thuyết đăng trên mạng của tác giả Hyūganatsu, rồi được xuất bản thành ligh…

```text
Wide 16:9 landscape cinematic frame. a stack of light novels and two different manga volumes side by side on a wooden shelf. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Bản anime ra mắt tháng mười năm 2023 và nhanh chóng trở thành một trong những bộ được yêu thích nhất. Mùa hai…

```text
Wide 16:9 landscape cinematic frame. three calendar pages with small herb-shaped bookmarks: 2023, 2025, 2026. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Tại lễ trao giải anime của Crunchyroll năm 2026, bộ này nhận mười bảy đề cử, chỉ sau Dandadan. Mùa ba sẽ chia…

```text
Wide 16:9 landscape cinematic frame. a trophy shelf with seventeen small glowing stars beside a herb basket. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ngoài ra còn có một bộ phim điện ảnh với câu chuyện hoàn toàn mới của tác giả, ra rạp ở Nhật ngày 11 tháng 12…

```text
Wide 16:9 landscape cinematic frame. a cinema marquee at night with a lantern-shaped poster, snow lightly falling. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Tên tiếng Nhật của bộ này có nghĩa là những lời lẩm bẩm của một dược sư. Và đúng vậy, phần lớn thời gian nhân…

```text
Wide 16:9 landscape cinematic frame. a young woman with a deadpan expression, small thought bubbles full of blunt comments floating above her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là bộ hiếm hoi vừa là trinh thám, vừa là cung đấu, vừa là hài lãng mạn. Và cả ba thể loại đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot juggling a magnifying glass, a hairpin and a small heart. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Thế giới: hậu cung

Lời: Câu chuyện diễn ra ở một đế quốc hư cấu, lấy cảm hứng từ các triều đại phong kiến Trung Hoa. Trung tâm của mọ…

```text
Wide 16:9 landscape cinematic frame. a vast palace complex with many courtyards and pavilions seen from above. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Hậu cung là nơi ở của các phi tần, cung nữ và những người phục vụ, với hàng nghìn người sống sau những bức tư…

```text
Wide 16:9 landscape cinematic frame. high palace walls with many small figures of court ladies walking inside, guards at the gate. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Ở đỉnh là bốn phi tần cao nhất, mỗi người có cung điện riêng, người hầu riêng, và phe cánh riêng. Họ đẹp, quy…

```text
Wide 16:9 landscape cinematic frame. four elegant pavilions in different colors arranged around a central garden. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Vì sao nguy hiểm? Vì sinh được người thừa kế cho hoàng đế là chuyện quyền lực của cả một gia tộc. Trong hậu c…

```text
Wide 16:9 landscape cinematic frame. a teacup on a tray with a faint dark swirl in the tea, soft ominous lighting. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Ngoài phi tần và cung nữ, hậu cung còn có các quan lại, thị vệ, thầy thuốc và rất nhiều quy tắc nghiêm ngặt v…

```text
Wide 16:9 landscape cinematic frame. a long corridor with guards at every door and a scroll of rules pinned on the wall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hãy tưởng tượng một cái trường học nội trú khổng lồ, nhưng thay vì thi cử là tranh giành ngai v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking nervously at a lunch tray with a magnifying glass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Bảng thuật ngữ cho người mới

Lời: Trước khi đi tiếp, Kaku lập một bảng thuật ngữ nhỏ, vì bộ này có khá nhiều từ cung đình.

```text
Wide 16:9 landscape cinematic frame. a scroll glossary with small illustrated icons next to each term. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Phi tần là vợ của hoàng đế, có nhiều thứ bậc. Cung nữ là những người phục vụ trong hậu cung, phần lớn là con…

```text
Wide 16:9 landscape cinematic frame. two small icons: an ornate hairpin for a consort and a simple broom for a court lady. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Thái giám là những người đàn ông đã bị thiến để được phép phục vụ trong hậu cung. Họ lo việc quản lý, canh gá…

```text
Wide 16:9 landscape cinematic frame. a robed official carrying scrolls through a palace corridor. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Người thử độc là người nếm thức ăn trước phi tần, để nếu có độc thì chính họ bị trước. Đây là công việc mà nh…

```text
Wide 16:9 landscape cinematic frame. a small bowl and spoon on a tray with a single tasting spoon set apart. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và dược sư là người bào chế thuốc từ thảo dược. Ở thời đó, ranh giới giữa thuốc và độc đôi khi chỉ là liều lư…

```text
Wide 16:9 landscape cinematic frame. a wooden medicine cabinet with many small drawers and a balance scale on top. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Nhân vật chính: Maomao

Lời: Nhân vật chính là Maomao, một cô gái mười bảy tuổi, lớn lên ở khu phố đèn đỏ của kinh thành, nơi cô làm dược…

```text
Wide 16:9 landscape cinematic frame. a young woman with a plain dress grinding herbs in a small shop in a lantern-lit alley. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Người cha nuôi của cô là một dược sư rất giỏi, và dạy cô gần như mọi thứ về thảo dược, bệnh tật và cách quan…

```text
Wide 16:9 landscape cinematic frame. an elderly gentle apothecary teaching a young girl to identify plants in a garden. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Một ngày, cô bị bắt cóc và bán vào hậu cung làm cung nữ hạ đẳng. Kế hoạch của cô rất đơn giản: sống thật lặng…

```text
Wide 16:9 landscape cinematic frame. a young woman scrubbing floors in a palace corridor, keeping her head down. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Điều đặc biệt nhất ở Maomao là cô yêu độc dược. Không phải để hại người, mà vì tò mò khoa học. Cô còn tự thử…

```text
Wide 16:9 landscape cinematic frame. a young woman looking at an unusual mushroom with sparkling eyes of pure fascination. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Nhắc lại lần nữa: đây là nhân vật hư cấu. Ngoài đời, thử độc trên cơ thể là cực kỳ nguy hiểm và có thể gây ch…

```text
Wide 16:9 landscape cinematic frame. a red warning sign over a crossed-out hand reaching toward a mushroom. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Cô còn có một tài năng khác: nhận ra mùi, vị và dấu hiệu nhỏ trên cơ thể người khác mà người thường bỏ qua, n…

```text
Wide 16:9 landscape cinematic frame. a close-up of a young woman observing another person's hands carefully under lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Maomao là kiểu nhân vật hiếm có: thông minh tuyệt đỉnh, nhưng chỉ muốn được yên thân. Chính sự…

```text
Wide 16:9 landscape cinematic frame. the owl mascot yawning next to a giant pile of palace drama, completely uninterested. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Vụ án đầu tiên: bệnh của những đứa trẻ

Lời: Maomao không muốn dính vào chuyện gì. Nhưng rồi cô nghe tin những đứa con nhỏ của hoàng đế liên tục đổ bệnh,…

```text
Wide 16:9 landscape cinematic frame. an empty cradle in a quiet palace room with a single candle burning. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Người ta đồn đó là một lời nguyền. Maomao thì không tin lời nguyền. Cô tin vào triệu chứng.

```text
Wide 16:9 landscape cinematic frame. court ladies whispering behind fans while a young woman listens quietly in the background. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Cô quan sát và nhận ra nguyên nhân: phấn trang điểm mà các phi tần dùng có chứa chì. Chất độc đi vào cơ thể n…

```text
Wide 16:9 landscape cinematic frame. a small open jar of white face powder with a faint warning glow around it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Không muốn bị chú ý, cô viết một lời cảnh báo nặc danh và để lại cho các phi tần. Một người tin và bỏ phấn, đ…

```text
Wide 16:9 landscape cinematic frame. a small anonymous note tied to a branch outside a pavilion window at night. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nhưng lời cảnh báo nặc danh lại lọt vào mắt một người rất để ý. Và cuộc sống lặng lẽ của Maomao chính thức kế…

```text
Wide 16:9 landscape cinematic frame. a tall elegant figure holding the anonymous note, smiling knowingly in lantern light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đó là toàn bộ spoiler của video hôm nay. Phần còn lại, Kaku chỉ nói về thế giới và lý do nên xem.

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a book and tying it with a ribbon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Khoa học thật: chì trong mỹ phẩm

Lời: Vụ án đầu tiên dựa trên một chuyện có thật trong lịch sử. Chì từng được dùng trong phấn trắng ở nhiều nền văn…

```text
Wide 16:9 landscape cinematic frame. an antique cosmetics box with porcelain jars and a hand mirror in a museum case. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Ở châu Âu thế kỷ mười sáu, nhiều quý tộc dùng loại phấn trắng làm từ chì. Ở Nhật Bản, phấn trắng có chì cũng…

```text
Wide 16:9 landscape cinematic frame. a split image: a European noblewoman portrait and a traditional Japanese stage performer's makeup set. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Chì là chất độc tích tụ trong cơ thể. Nó đặc biệt nguy hiểm với trẻ em, ảnh hưởng tới não bộ và sự phát triển…

```text
Wide 16:9 landscape cinematic frame. a simple diagram of a child silhouette with a highlighted brain and a warning icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Ngày nay, chì trong mỹ phẩm bị kiểm soát chặt ở nhiều nước. Nhưng vụ án này cho thấy tác giả đã dựa vào khoa…

```text
Wide 16:9 landscape cinematic frame. a modern cosmetics lab with a safety inspector checking a label. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Và chì không phải chất độc duy nhất từng có trong mỹ phẩm. Trong lịch sử, người ta còn dùng thủy ngân và thạc…

```text
Wide 16:9 landscape cinematic frame. an old apothecary shelf with antique cosmetic jars, each with a small faded warning label. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là điều Kaku thích nhất ở bộ này. Mọi bí ẩn đều có lời giải hợp lý. Không có ma, chỉ có hóa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over a jar, with a satisfied nod. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Những người trong cung

Lời: Người phát hiện ra Maomao là Jinshi, một thái giám quản lý hậu cung, đẹp tới mức khiến cả phi tần lẫn cung nữ…

```text
Wide 16:9 landscape cinematic frame. a tall graceful figure in elegant robes walking through a courtyard as court ladies blush. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Anh đưa Maomao về làm người thử độc cho một phi tần hiền hậu, người vừa được cứu đứa con nhờ lời cảnh báo của…

```text
Wide 16:9 landscape cinematic frame. a kind consort holding a healthy baby, a young woman standing respectfully beside her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Điều buồn cười là trong khi mọi người đều bị vẻ đẹp của Jinshi mê hoặc, thì Maomao nhìn anh như nhìn một con…

```text
Wide 16:9 landscape cinematic frame. a young woman giving a flat unimpressed look while a handsome figure smiles brightly at her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Jinshi thì ngày càng tò mò về cô, và liên tục giao cho cô những vụ án khó trong cung. Mối quan hệ giữa hai ng…

```text
Wide 16:9 landscape cinematic frame. the handsome figure leaning in with a new case scroll, the young woman sighing. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Ngoài ra còn có nhiều nhân vật đáng nhớ khác: những phi tần mỗi người một tính cách, những cung nữ trung thàn…

```text
Wide 16:9 landscape cinematic frame. a group portrait of varied palace figures in soft lantern light, each with a different expression. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và Jinshi còn mang một bí mật về thân phận thật của mình. Kaku không nói ra đâu, bạn tự xem nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot zipping its beak shut and winking. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Khoa học thật: bạc có phát hiện được độc không?

Lời: Trong phim cung đình, ta hay thấy người ta dùng kim bạc hoặc đũa bạc để thử độc. Nếu bạc đổi màu đen thì có đ…

```text
Wide 16:9 landscape cinematic frame. a silver needle dipped into a bowl of soup on a lacquered tray. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Khoa học nói: bạc bị xỉn đen khi gặp các hợp chất chứa lưu huỳnh. Ngày xưa, thạch tín thường lẫn tạp chất lưu…

```text
Wide 16:9 landscape cinematic frame. a silver spoon slowly tarnishing black beside a small pile of yellow mineral. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nhưng thạch tín tinh khiết thì không làm bạc đổi màu. Và nhiều loại độc khác, như độc từ cây cỏ, cũng không p…

```text
Wide 16:9 landscape cinematic frame. a clean silver needle beside a bowl labeled with a question mark, and a boiled egg next to a tarnished spoon. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nên bạc chỉ là một cách thử rất không đáng tin. Đó là lý do trong truyện, người thử độc vẫn phải có kiến thức…

```text
Wide 16:9 landscape cinematic frame. a young woman confidently examining a dish while a silver needle lies unused beside it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ngày nay, để phát hiện chất độc, các phòng thí nghiệm dùng những máy phân tích hiện đại, có thể tìm ra một lư…

```text
Wide 16:9 landscape cinematic frame. a modern laboratory with analysis machines and a technician in a white coat. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một lần nữa, đây là kiến thức để hiểu truyện, không phải cách kiểm tra thức ăn ngoài đời. Ngoài…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a phone with an emergency icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Kaku thử suy luận · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ tới phần vui. Kaku thử suy luận như Maomao với một vụ án nhỏ do Kaku tự nghĩ ra, hoàn toàn vô hại.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny apron, standing before a vase of wilted flowers. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Vụ án: trong một phòng khách, hoa cắm trong bình luôn héo chỉ sau hai ngày, trong khi hoa ở phòng bên cạnh tư…

```text
Wide 16:9 landscape cinematic frame. two rooms side by side: one with wilted flowers, the other with fresh ones. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Quan sát: nước trong hai bình như nhau, ánh sáng như nhau. Điểm khác duy nhất: phòng hoa héo có một đĩa trái…

```text
Wide 16:9 landscape cinematic frame. a close-up of a bowl of ripe fruit sitting right next to a vase of drooping flowers. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Suy luận: trái cây chín tỏa ra một loại khí tên là ethylene. Khí này thúc đẩy trái cây chín nhanh hơn, và cũn…

```text
Wide 16:9 landscape cinematic frame. invisible gas lines drawn curling from ripe fruit toward flowers, labeled with a simple molecule icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Lời giải: không có ma. Chỉ cần dời đĩa trái cây ra xa là hoa tươi lâu hơn. Đây là khoa học có thật, và bạn có…

```text
Wide 16:9 landscape cinematic frame. the same room with the fruit bowl moved to another table and the flowers standing fresh. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đó là tinh thần của Maomao. Khi người ta nói lời nguyền, cô hỏi: đâu là thứ khác biệt?

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping its temple thoughtfully with a wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Vì sao bạn nên xem?

Lời: Tóm lại, có bốn lý do Kaku nghĩ bạn nên thử Dược sư tự sự.

```text
Wide 16:9 landscape cinematic frame. four hanging lanterns, each with a small icon painted on it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Một: mỗi tập thường có một bí ẩn nhỏ, được giải bằng kiến thức và quan sát, rất thỏa mãn. Hai: nhân vật chính…

```text
Wide 16:9 landscape cinematic frame. a small solved-case scroll and a young woman with a smug grin. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Ba: thế giới cung đình được xây dựng tỉ mỉ, đẹp và đầy âm mưu. Bốn: bên dưới những vụ án là một câu chuyện lớ…

```text
Wide 16:9 landscape cinematic frame. an ornate palace garden at night, a few women standing apart in quiet conversation. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nếu bạn thích trinh thám kiểu Sherlock Holmes, thích lịch sử và cung đình, hoặc đơn giản muốn nghỉ một chút k…

```text
Wide 16:9 landscape cinematic frame. a cozy reading corner with a detective novel, a cup of tea and a small herb pot. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Maomao và những thám tử nổi tiếng

Lời: Nếu phải xếp Maomao vào một nhóm, Kaku sẽ xếp cô cạnh những thám tử nổi tiếng nhất trong văn học và anime.

```text
Wide 16:9 landscape cinematic frame. a shelf of detective novels with a small herb pouch placed among them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Sherlock Holmes, nhân vật của nhà văn Arthur Conan Doyle, xuất hiện lần đầu năm 1887. Ông nổi tiếng vì quan s…

```text
Wide 16:9 landscape cinematic frame. a Victorian-era study with a violin, chemistry glassware and a long coat on a hook. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Thám tử lừng danh Conan, bắt đầu từ năm 1994, là bộ trinh thám anime quen thuộc nhất với khán giả Việt Nam, v…

```text
Wide 16:9 landscape cinematic frame. a stack of detective manga volumes beside a magnifying glass and a small notebook. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Điểm chung của họ với Maomao: không có siêu năng lực, chỉ có quan sát, kiến thức và lý luận. Điểm khác: Maoma…

```text
Wide 16:9 landscape cinematic frame. a young woman reluctantly holding a magnifying glass while longingly looking at an herb garden. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: có lẽ đó là lý do cô được yêu thích. Một thiên tài bất đắc dĩ, luôn bị kéo vào rắc rối, và luôn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sighing dramatically while holding a solved case file. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Ba bài học quan sát từ Maomao

Lời: Trước khi kết, Kaku rút ra ba bài học quan sát từ cách Maomao giải án, những bài học dùng được cả ngoài đời.

```text
Wide 16:9 landscape cinematic frame. a notebook page with three numbered notes and a pressed flower. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Một: tìm điểm khác biệt. Khi hai tình huống gần giống nhau mà kết quả khác nhau, câu trả lời thường nằm ở chỗ…

```text
Wide 16:9 landscape cinematic frame. two nearly identical rooms side by side with one small difference circled in red. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hai: đừng tin lời đồn vội. Khi mọi người nói đó là lời nguyền hay ma quỷ, hãy hỏi xem có lời giải thích nào đ…

```text
Wide 16:9 landscape cinematic frame. a group whispering about a ghost while a calm figure examines footprints on the floor. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Ba: kiến thức từ sách chỉ mạnh khi đi kèm kinh nghiệm thực tế. Maomao giỏi vì cô vừa học từ cha nuôi, vừa làm…

```text
Wide 16:9 landscape cinematic frame. a young woman reading a thick book by lamplight, then tending to a patient in a small shop. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: ba bài học này không cần phải vào hậu cung mới dùng được. Chúng hữu ích cả khi bạn tìm chìa khó…

```text
Wide 16:9 landscape cinematic frame. the owl mascot finding a small key under a cushion, looking triumphant. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Góc nhìn của Kaku: kiến thức là sức mạnh · **Kaku** (đính kèm ảnh mẫu)

Lời: Kênh của Kaku thường nói về những hệ thống sức mạnh: Nen, chú lực, Haki. Vậy Dược sư tự sự có hệ thống sức mạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a chart of power systems with one empty slot. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Kaku nghĩ là có. Chỉ là sức mạnh ở đây không nằm trong cơ thể, mà nằm trong đầu. Người biết nhiều hơn thì kiể…

```text
Wide 16:9 landscape cinematic frame. a glowing brain icon placed into the empty slot on the power chart. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Trong một thế giới mà một cung nữ không có quyền gì, kiến thức là thứ duy nhất giúp Maomao được lắng nghe, đư…

```text
Wide 16:9 landscape cinematic frame. a young woman speaking calmly while powerful officials listen intently. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và giống mọi sức mạnh, nó cũng có cái giá: càng biết nhiều, cô càng bị cuốn vào những bí mật nguy hiểm mà cô…

```text
Wide 16:9 landscape cinematic frame. a young woman surrounded by floating secret scrolls, looking tired. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Kaku thấy đây là bài học rất thật: trong đời thật, không có phép thuật, nhưng kiến thức luôn là sức mạnh mà a…

```text
Wide 16:9 landscape cinematic frame. a stack of books with a small sprout growing out of the top one. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Lộ trình xem cho người mới

Lời: Nếu muốn bắt đầu, đây là lộ trình Kaku gợi ý.

```text
Wide 16:9 landscape cinematic frame. a winding path through a palace garden with small signposts. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Bước một: xem mùa một từ đầu, hai mươi bốn tập. Ba tập đầu đủ để bạn biết mình có thích nhịp của bộ này hay k…

```text
Wide 16:9 landscape cinematic frame. a small screen showing three glowing episode icons at the start of a long row. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Bước hai: xem tiếp mùa hai, rồi theo dõi mùa ba đang phát. Nếu thích, bộ phim điện ảnh tháng mười hai là một…

```text
Wide 16:9 landscape cinematic frame. a timeline of three seasons and a small film reel at the end. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và như mọi khi, hãy xem qua các nền tảng có bản quyền để ủng hộ những người làm ra bộ phim.

```text
Wide 16:9 landscape cinematic frame. a heart-shaped glow over a small film reel and a herb leaf. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Tóm lại: Dược sư tự sự là câu chuyện về một cô gái mê độc dược bị bán vào hậu cung, và dùng kiến thức về thuố…

```text
Wide 16:9 landscape cinematic frame. a young woman standing in a palace courtyard at dawn holding a small herb bundle. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được sống trong hậu cung, bạn muốn làm phi tần, cung nữ, thái giám hay người thử độc? Ka…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sniffing a bundle of herbs happily. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tới quay lại với thế giới sức mạnh: Kaku kể lịch sử của JoJo, từ kỹ thuật thở Hamon cho tới những Stand…

```text
Wide 16:9 landscape cinematic frame. a sunrise glowing behind a spiral of breath and a shadowy guardian silhouette. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Kaku cất giỏ thảo dược đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a small herb basket and waving from a palace garden. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 3. Giọng đọc

### Chọn giọng Kaku (làm 1 lần)

Tạo cả 3 giọng bằng Voice Design (AI Studio hoặc ElevenLabs), cho mỗi giọng đọc đoạn thử bên dưới, rồi báo mình giọng bạn chọn.

**Nam · giọng Bắc**: Nam khoảng 25 tuổi, giọng Hà Nội, ấm và sáng, như một anh gia sư mê kể chuyện.

```text
A young Vietnamese man in his mid-20s speaking with a clear Northern (Hanoi) accent. Warm, bright mid-range voice with a gentle smile in it; articulate and precise like a friendly university tutor who loves telling stories. Curious and playful, confident but never shouting. Close-mic, clean studio recording, no background noise.
```

**Nam · giọng Nam**: Nam khoảng 25 tuổi, giọng Sài Gòn, thân thiện và có năng lượng, như một người bạn giải thích anime lúc khuya.

```text
A young Vietnamese man around 25 speaking with a natural Southern (Saigon) accent. Friendly, energetic mid-range voice, relaxed and approachable, like an older friend explaining anime lore late at night. Playful humor, clear diction, never shouting. Close-mic, clean studio recording, no background noise.
```

**Nữ · giọng Bắc**: Nữ khoảng 25 tuổi, giọng Hà Nội, trong và tự tin, hơi khàn nhẹ, như một MC gameshow thầm mê anime.

```text
A young Vietnamese woman in her mid-20s speaking with a clear Northern (Hanoi) accent. Bright, confident voice with a slight husky texture and a playful smile; sharp and articulate like a quiz-show host who secretly loves anime. Never shrill, never shouting. Close-mic, clean studio recording, no background noise.
```

Đoạn đọc thử:

```text
Mở sổ ra nào! Mình là Kaku, một con cú tự nhận đã đọc hết thư viện, rồi bị chính các bạn sửa sai trong phần bình luận. Hôm nay mình sẽ giải mã một hệ thống sức mạnh mà ai cũng tưởng là hiểu rồi. Nhưng khoan đã. Nếu luật chơi đơn giản như vậy, thì tại sao nhân vật mạnh nhất lại thua? Câu trả lời nằm ở một dòng chữ nhỏ mà rất ít người để ý.
```

### Ghi chú đạo diễn (dán 1 lần, ô Style instructions)

```text
AUDIO PROFILE: Kaku, a witty owl scholar who narrates a Vietnamese anime-lore channel. Young adult narrator, warm and bright, with a knowing smile.
THE SCENE: Late evening in a cozy library lit by a desk lamp. Kaku leans toward the microphone and shares a secret he has just decoded in his notebook with a close friend.
DIRECTOR'S NOTES:
- Speak Vietnamese naturally, like a real storyteller; never robotic, never news-anchor stiff.
- Pace: steady and unhurried, about 150 words per minute; slow down slightly on key terms and numbers.
- Tone: curious and confident; light humor with a smile in the voice on jokes; never shout.
- Take a short breath-pause before every reveal (sentences starting with 'Nhưng', 'Thật ra', 'Hóa ra').
- Say Japanese and English terms (Nen, Haki, Bankai...) the way Vietnamese fans say them, clearly articulated.
- Keep exactly the same voice, energy and loudness in every segment so the pieces join seamlessly.
```

- **Gemini (AI Studio / API):** AI Studio → Generate speech (Gemini TTS). Chọn giọng Kaku đã tạo bằng Voice Design, dán Ghi chú đạo diễn vào ô Style instructions, dán từng đoạn đọc vào ô văn bản, bấm Run rồi tải file về, đặt tên c01, c02…
- **ElevenLabs (Eleven v3):** ElevenLabs → Voices → Voice Design: dán Mô tả giọng, lưu giọng Kaku. Text to Speech → model Eleven v3 → chọn giọng Kaku → dán từng đoạn đọc (đã có thẻ [..]) → Generate → tải file về, đặt tên c01, c02… ElevenLabs không có ô chỉ đạo: cảm xúc nằm trong thẻ.

Bản không có thẻ (công cụ khác hoặc tự thu âm): mỗi cảnh một đoạn, xem `script.vi.md`.

### c01 · Mở đầu / Bộ truyện này là gì?

Khoảng 129 giây · cảnh s01–s11 · 1676 ký tự

**Gemini**

```text
Video này gần như không có spoiler: Kaku chỉ nói về thế giới, nhân vật và vụ án đầu tiên ở những tập đầu mùa một. Nếu bạn chưa xem, đây là video dành cho bạn.

<short pause> <laugh> Ở một kênh chuyên giải mã hệ thống sức mạnh, hôm nay Kaku giới thiệu một bộ không có phép thuật, không có siêu năng lực, không có ai bắn chưởng.

<short pause> Vũ khí duy nhất của nhân vật chính là một thứ: kiến thức về thuốc và độc. Và trong một hoàng cung đầy âm mưu, thứ đó đáng sợ hơn bất kỳ phép thuật nào.

<short pause> Đó là Dược sư tự sự, bộ anime đang phát mùa ba từ tháng mười năm 2026. Mở sổ ra nào! Mình là Kaku, và đây là mười lăm phút nhập môn của bạn.

<short pause> Một lưu ý quan trọng: video có nhắc tới thuốc và chất độc trong bối cảnh truyện. Đây không phải lời khuyên y tế, và tuyệt đối đừng thử bất cứ điều gì ở nhà.

<short pause> Dược sư tự sự khởi đầu là một tiểu thuyết đăng trên mạng của tác giả Hyūganatsu, rồi được xuất bản thành light novel, và có tới hai bản chuyển thể manga khác nhau.

<short pause> Bản anime ra mắt tháng mười năm 2023 và nhanh chóng trở thành một trong những bộ được yêu thích nhất. Mùa hai phát năm 2025, và mùa ba bắt đầu ngày 2 tháng 10 năm 2026.

<short pause> Tại lễ trao giải anime của Crunchyroll năm 2026, bộ này nhận mười bảy đề cử, chỉ sau Dandadan. Mùa ba sẽ chia làm hai phần, phần hai phát tháng tư năm 2027.

<short pause> Ngoài ra còn có một bộ phim điện ảnh với câu chuyện hoàn toàn mới của tác giả, ra rạp ở Nhật ngày 11 tháng 12 năm 2026.

<short pause> Tên tiếng Nhật của bộ này có nghĩa là những lời lẩm bẩm của một dược sư. Và đúng vậy, phần lớn thời gian nhân vật chính chỉ lẩm bẩm trong đầu những suy nghĩ rất thẳng thắn về mọi người xung quanh.

<short pause> Kaku ghi chú: đây là bộ hiếm hoi vừa là trinh thám, vừa là cung đấu, vừa là hài lãng mạn. Và cả ba thể loại đều được làm tốt.
```

**ElevenLabs**

```text
Video này gần như không có spoiler: Kaku chỉ nói về thế giới, nhân vật và vụ án đầu tiên ở những tập đầu mùa một. Nếu bạn chưa xem, đây là video dành cho bạn.

[pause] [chuckles] Ở một kênh chuyên giải mã hệ thống sức mạnh, hôm nay Kaku giới thiệu một bộ không có phép thuật, không có siêu năng lực, không có ai bắn chưởng.

[pause] Vũ khí duy nhất của nhân vật chính là một thứ: kiến thức về thuốc và độc. Và trong một hoàng cung đầy âm mưu, thứ đó đáng sợ hơn bất kỳ phép thuật nào.

[pause] Đó là Dược sư tự sự, bộ anime đang phát mùa ba từ tháng mười năm 2026. Mở sổ ra nào! Mình là Kaku, và đây là mười lăm phút nhập môn của bạn.

[pause] Một lưu ý quan trọng: video có nhắc tới thuốc và chất độc trong bối cảnh truyện. Đây không phải lời khuyên y tế, và tuyệt đối đừng thử bất cứ điều gì ở nhà.

[pause] Dược sư tự sự khởi đầu là một tiểu thuyết đăng trên mạng của tác giả Hyūganatsu, rồi được xuất bản thành light novel, và có tới hai bản chuyển thể manga khác nhau.

[pause] Bản anime ra mắt tháng mười năm 2023 và nhanh chóng trở thành một trong những bộ được yêu thích nhất. Mùa hai phát năm 2025, và mùa ba bắt đầu ngày 2 tháng 10 năm 2026.

[pause] Tại lễ trao giải anime của Crunchyroll năm 2026, bộ này nhận mười bảy đề cử, chỉ sau Dandadan. Mùa ba sẽ chia làm hai phần, phần hai phát tháng tư năm 2027.

[pause] Ngoài ra còn có một bộ phim điện ảnh với câu chuyện hoàn toàn mới của tác giả, ra rạp ở Nhật ngày 11 tháng 12 năm 2026.

[pause] Tên tiếng Nhật của bộ này có nghĩa là những lời lẩm bẩm của một dược sư. Và đúng vậy, phần lớn thời gian nhân vật chính chỉ lẩm bẩm trong đầu những suy nghĩ rất thẳng thắn về mọi người xung quanh.

[pause] Kaku ghi chú: đây là bộ hiếm hoi vừa là trinh thám, vừa là cung đấu, vừa là hài lãng mạn. Và cả ba thể loại đều được làm tốt.
```

### c02 · Thế giới: hậu cung / Bảng thuật ngữ cho người mới

Khoảng 115 giây · cảnh s12–s22 · 1497 ký tự

**Gemini**

```text
Câu chuyện diễn ra ở một đế quốc hư cấu, lấy cảm hứng từ các triều đại phong kiến Trung Hoa. Trung tâm của mọi thứ là hậu cung của hoàng đế.

<short pause> Hậu cung là nơi ở của các phi tần, cung nữ và những người phục vụ, với hàng nghìn người sống sau những bức tường cao. Đàn ông bình thường không được vào.

<short pause> Ở đỉnh là bốn phi tần cao nhất, mỗi người có cung điện riêng, người hầu riêng, và phe cánh riêng. Họ đẹp, quyền lực, và luôn gặp nguy hiểm.

<short pause> Vì sao nguy hiểm? Vì sinh được người thừa kế cho hoàng đế là chuyện quyền lực của cả một gia tộc. Trong hậu cung, độc dược là vũ khí im lặng nhất.

<short pause> Ngoài phi tần và cung nữ, hậu cung còn có các quan lại, thị vệ, thầy thuốc và rất nhiều quy tắc nghiêm ngặt về việc ai được đi đâu, nói gì, gặp ai. Một sai sót nhỏ có thể phải trả giá rất đắt.

<short pause> <laugh> Kaku ghi chú: hãy tưởng tượng một cái trường học nội trú khổng lồ, nhưng thay vì thi cử là tranh giành ngai vàng. Và căng tin thì có thể có độc.

<short pause> Trước khi đi tiếp, Kaku lập một bảng thuật ngữ nhỏ, vì bộ này có khá nhiều từ cung đình.

<short pause> Phi tần là vợ của hoàng đế, có nhiều thứ bậc. Cung nữ là những người phục vụ trong hậu cung, phần lớn là con gái nhà thường dân.

<short pause> Thái giám là những người đàn ông đã bị thiến để được phép phục vụ trong hậu cung. Họ lo việc quản lý, canh gác và truyền tin.

<short pause> Người thử độc là người nếm thức ăn trước phi tần, để nếu có độc thì chính họ bị trước. Đây là công việc mà nhân vật chính sẽ làm.

<short pause> Và dược sư là người bào chế thuốc từ thảo dược. Ở thời đó, ranh giới giữa thuốc và độc đôi khi chỉ là liều lượng.
```

**ElevenLabs**

```text
Câu chuyện diễn ra ở một đế quốc hư cấu, lấy cảm hứng từ các triều đại phong kiến Trung Hoa. Trung tâm của mọi thứ là hậu cung của hoàng đế.

[pause] Hậu cung là nơi ở của các phi tần, cung nữ và những người phục vụ, với hàng nghìn người sống sau những bức tường cao. Đàn ông bình thường không được vào.

[pause] Ở đỉnh là bốn phi tần cao nhất, mỗi người có cung điện riêng, người hầu riêng, và phe cánh riêng. Họ đẹp, quyền lực, và luôn gặp nguy hiểm.

[pause] [curious] Vì sao nguy hiểm? Vì sinh được người thừa kế cho hoàng đế là chuyện quyền lực của cả một gia tộc. Trong hậu cung, độc dược là vũ khí im lặng nhất.

[pause] Ngoài phi tần và cung nữ, hậu cung còn có các quan lại, thị vệ, thầy thuốc và rất nhiều quy tắc nghiêm ngặt về việc ai được đi đâu, nói gì, gặp ai. Một sai sót nhỏ có thể phải trả giá rất đắt.

[pause] [chuckles] Kaku ghi chú: hãy tưởng tượng một cái trường học nội trú khổng lồ, nhưng thay vì thi cử là tranh giành ngai vàng. Và căng tin thì có thể có độc.

[pause] Trước khi đi tiếp, Kaku lập một bảng thuật ngữ nhỏ, vì bộ này có khá nhiều từ cung đình.

[pause] Phi tần là vợ của hoàng đế, có nhiều thứ bậc. Cung nữ là những người phục vụ trong hậu cung, phần lớn là con gái nhà thường dân.

[pause] Thái giám là những người đàn ông đã bị thiến để được phép phục vụ trong hậu cung. Họ lo việc quản lý, canh gác và truyền tin.

[pause] Người thử độc là người nếm thức ăn trước phi tần, để nếu có độc thì chính họ bị trước. Đây là công việc mà nhân vật chính sẽ làm.

[pause] Và dược sư là người bào chế thuốc từ thảo dược. Ở thời đó, ranh giới giữa thuốc và độc đôi khi chỉ là liều lượng.
```

### c03 · Nhân vật chính: Maomao / Vụ án đầu tiên: bệnh của những đứa trẻ

Khoảng 128 giây · cảnh s23–s35 · 1660 ký tự

**Gemini**

```text
Nhân vật chính là Maomao, một cô gái mười bảy tuổi, lớn lên ở khu phố đèn đỏ của kinh thành, nơi cô làm dược sư cùng người cha nuôi.

<short pause> Người cha nuôi của cô là một dược sư rất giỏi, và dạy cô gần như mọi thứ về thảo dược, bệnh tật và cách quan sát cơ thể con người.

<short pause> Một ngày, cô bị bắt cóc và bán vào hậu cung làm cung nữ hạ đẳng. Kế hoạch của cô rất đơn giản: sống thật lặng lẽ, làm hết hạn, rồi về nhà.

<short pause> Điều đặc biệt nhất ở Maomao là cô yêu độc dược. Không phải để hại người, mà vì tò mò khoa học. Cô còn tự thử độc trên cánh tay mình để hiểu tác dụng.

<short pause> Nhắc lại lần nữa: đây là nhân vật hư cấu. Ngoài đời, thử độc trên cơ thể là cực kỳ nguy hiểm và có thể gây chết người.

<short pause> Cô còn có một tài năng khác: nhận ra mùi, vị và dấu hiệu nhỏ trên cơ thể người khác mà người thường bỏ qua, như màu móng tay, làn da hay hơi thở.

<short pause> <laugh> Kaku ghi chú: Maomao là kiểu nhân vật hiếm có: thông minh tuyệt đỉnh, nhưng chỉ muốn được yên thân. Chính sự thờ ơ đó khiến cô rất buồn cười.

<short pause> Maomao không muốn dính vào chuyện gì. <short pause> Nhưng rồi cô nghe tin những đứa con nhỏ của hoàng đế liên tục đổ bệnh, và có đứa đã qua đời.

<short pause> Người ta đồn đó là một lời nguyền. Maomao thì không tin lời nguyền. Cô tin vào triệu chứng.

<short pause> Cô quan sát và nhận ra nguyên nhân: phấn trang điểm mà các phi tần dùng có chứa chì. Chất độc đi vào cơ thể những đứa trẻ qua người mẹ.

<short pause> Không muốn bị chú ý, cô viết một lời cảnh báo nặc danh và để lại cho các phi tần. Một người tin và bỏ phấn, đứa con của người đó khỏe lại.

<short pause> Nhưng lời cảnh báo nặc danh lại lọt vào mắt một người rất để ý. Và cuộc sống lặng lẽ của Maomao chính thức kết thúc.

<short pause> Đó là toàn bộ spoiler của video hôm nay. Phần còn lại, Kaku chỉ nói về thế giới và lý do nên xem.
```

**ElevenLabs**

```text
Nhân vật chính là Maomao, một cô gái mười bảy tuổi, lớn lên ở khu phố đèn đỏ của kinh thành, nơi cô làm dược sư cùng người cha nuôi.

[pause] Người cha nuôi của cô là một dược sư rất giỏi, và dạy cô gần như mọi thứ về thảo dược, bệnh tật và cách quan sát cơ thể con người.

[pause] Một ngày, cô bị bắt cóc và bán vào hậu cung làm cung nữ hạ đẳng. Kế hoạch của cô rất đơn giản: sống thật lặng lẽ, làm hết hạn, rồi về nhà.

[pause] Điều đặc biệt nhất ở Maomao là cô yêu độc dược. Không phải để hại người, mà vì tò mò khoa học. Cô còn tự thử độc trên cánh tay mình để hiểu tác dụng.

[pause] Nhắc lại lần nữa: đây là nhân vật hư cấu. Ngoài đời, thử độc trên cơ thể là cực kỳ nguy hiểm và có thể gây chết người.

[pause] Cô còn có một tài năng khác: nhận ra mùi, vị và dấu hiệu nhỏ trên cơ thể người khác mà người thường bỏ qua, như màu móng tay, làn da hay hơi thở.

[pause] [chuckles] Kaku ghi chú: Maomao là kiểu nhân vật hiếm có: thông minh tuyệt đỉnh, nhưng chỉ muốn được yên thân. Chính sự thờ ơ đó khiến cô rất buồn cười.

[pause] Maomao không muốn dính vào chuyện gì. [pause] Nhưng rồi cô nghe tin những đứa con nhỏ của hoàng đế liên tục đổ bệnh, và có đứa đã qua đời.

[pause] Người ta đồn đó là một lời nguyền. Maomao thì không tin lời nguyền. Cô tin vào triệu chứng.

[pause] Cô quan sát và nhận ra nguyên nhân: phấn trang điểm mà các phi tần dùng có chứa chì. Chất độc đi vào cơ thể những đứa trẻ qua người mẹ.

[pause] Không muốn bị chú ý, cô viết một lời cảnh báo nặc danh và để lại cho các phi tần. Một người tin và bỏ phấn, đứa con của người đó khỏe lại.

[pause] Nhưng lời cảnh báo nặc danh lại lọt vào mắt một người rất để ý. Và cuộc sống lặng lẽ của Maomao chính thức kết thúc.

[pause] Đó là toàn bộ spoiler của video hôm nay. Phần còn lại, Kaku chỉ nói về thế giới và lý do nên xem.
```

### c04 · Khoa học thật: chì trong mỹ phẩm / Những người trong cung

Khoảng 133 giây · cảnh s36–s47 · 1724 ký tự

**Gemini**

```text
Vụ án đầu tiên dựa trên một chuyện có thật trong lịch sử. Chì từng được dùng trong phấn trắng ở nhiều nền văn hóa, vì nó làm da trông trắng mịn.

<short pause> Ở châu Âu thế kỷ mười sáu, nhiều quý tộc dùng loại phấn trắng làm từ chì. Ở Nhật Bản, phấn trắng có chì cũng được dùng rộng rãi trong nhiều thế kỷ.

<short pause> Chì là chất độc tích tụ trong cơ thể. Nó đặc biệt nguy hiểm với trẻ em, ảnh hưởng tới não bộ và sự phát triển. Tổ chức Y tế Thế giới nói không có mức phơi nhiễm chì nào được coi là an toàn.

<short pause> Ngày nay, chì trong mỹ phẩm bị kiểm soát chặt ở nhiều nước. <short pause> Nhưng vụ án này cho thấy tác giả đã dựa vào khoa học và lịch sử thật, không phải một lời nguyền tưởng tượng.

<short pause> Và chì không phải chất độc duy nhất từng có trong mỹ phẩm. Trong lịch sử, người ta còn dùng thủy ngân và thạch tín để làm đẹp, trước khi hiểu được tác hại của chúng.

<short pause> <laugh> Kaku ghi chú: đây là điều Kaku thích nhất ở bộ này. Mọi bí ẩn đều có lời giải hợp lý. Không có ma, chỉ có hóa học.

<short pause> Người phát hiện ra Maomao là Jinshi, một thái giám quản lý hậu cung, đẹp tới mức khiến cả phi tần lẫn cung nữ phải xao xuyến.

<short pause> Anh đưa Maomao về làm người thử độc cho một phi tần hiền hậu, người vừa được cứu đứa con nhờ lời cảnh báo của cô.

<short pause> Điều buồn cười là trong khi mọi người đều bị vẻ đẹp của Jinshi mê hoặc, thì Maomao nhìn anh như nhìn một con sâu. Cô chỉ quan tâm tới thảo dược.

<short pause> Jinshi thì ngày càng tò mò về cô, và liên tục giao cho cô những vụ án khó trong cung. Mối quan hệ giữa hai người là một nửa niềm vui của bộ truyện.

<short pause> Ngoài ra còn có nhiều nhân vật đáng nhớ khác: những phi tần mỗi người một tính cách, những cung nữ trung thành, và người cha nuôi hiền lành mà Maomao kính trọng hơn ai hết.

<short pause> Và Jinshi còn mang một bí mật về thân phận thật của mình. Kaku không nói ra đâu, bạn tự xem nhé.
```

**ElevenLabs**

```text
Vụ án đầu tiên dựa trên một chuyện có thật trong lịch sử. Chì từng được dùng trong phấn trắng ở nhiều nền văn hóa, vì nó làm da trông trắng mịn.

[pause] Ở châu Âu thế kỷ mười sáu, nhiều quý tộc dùng loại phấn trắng làm từ chì. Ở Nhật Bản, phấn trắng có chì cũng được dùng rộng rãi trong nhiều thế kỷ.

[pause] Chì là chất độc tích tụ trong cơ thể. Nó đặc biệt nguy hiểm với trẻ em, ảnh hưởng tới não bộ và sự phát triển. Tổ chức Y tế Thế giới nói không có mức phơi nhiễm chì nào được coi là an toàn.

[pause] Ngày nay, chì trong mỹ phẩm bị kiểm soát chặt ở nhiều nước. [pause] Nhưng vụ án này cho thấy tác giả đã dựa vào khoa học và lịch sử thật, không phải một lời nguyền tưởng tượng.

[pause] Và chì không phải chất độc duy nhất từng có trong mỹ phẩm. Trong lịch sử, người ta còn dùng thủy ngân và thạch tín để làm đẹp, trước khi hiểu được tác hại của chúng.

[pause] [chuckles] Kaku ghi chú: đây là điều Kaku thích nhất ở bộ này. Mọi bí ẩn đều có lời giải hợp lý. Không có ma, chỉ có hóa học.

[pause] Người phát hiện ra Maomao là Jinshi, một thái giám quản lý hậu cung, đẹp tới mức khiến cả phi tần lẫn cung nữ phải xao xuyến.

[pause] Anh đưa Maomao về làm người thử độc cho một phi tần hiền hậu, người vừa được cứu đứa con nhờ lời cảnh báo của cô.

[pause] Điều buồn cười là trong khi mọi người đều bị vẻ đẹp của Jinshi mê hoặc, thì Maomao nhìn anh như nhìn một con sâu. Cô chỉ quan tâm tới thảo dược.

[pause] Jinshi thì ngày càng tò mò về cô, và liên tục giao cho cô những vụ án khó trong cung. Mối quan hệ giữa hai người là một nửa niềm vui của bộ truyện.

[pause] Ngoài ra còn có nhiều nhân vật đáng nhớ khác: những phi tần mỗi người một tính cách, những cung nữ trung thành, và người cha nuôi hiền lành mà Maomao kính trọng hơn ai hết.

[pause] Và Jinshi còn mang một bí mật về thân phận thật của mình. Kaku không nói ra đâu, bạn tự xem nhé.
```

### c05 · Khoa học thật: bạc có phát hiện được độc không? / Kaku thử suy luận

Khoảng 133 giây · cảnh s48–s59 · 1726 ký tự

**Gemini**

```text
Trong phim cung đình, ta hay thấy người ta dùng kim bạc hoặc đũa bạc để thử độc. Nếu bạc đổi màu đen thì có độc. Liệu có đúng không?

<short pause> Khoa học nói: bạc bị xỉn đen khi gặp các hợp chất chứa lưu huỳnh. Ngày xưa, thạch tín thường lẫn tạp chất lưu huỳnh, nên bạc có lúc đổi màu thật.

<short pause> Nhưng thạch tín tinh khiết thì không làm bạc đổi màu. Và nhiều loại độc khác, như độc từ cây cỏ, cũng không phản ứng với bạc. Trứng hay tỏi lại có thể làm bạc xỉn dù hoàn toàn vô hại.

<short pause> Nên bạc chỉ là một cách thử rất không đáng tin. Đó là lý do trong truyện, người thử độc vẫn phải có kiến thức thật, và Maomao giỏi hơn một cây kim bạc rất nhiều.

<short pause> Ngày nay, để phát hiện chất độc, các phòng thí nghiệm dùng những máy phân tích hiện đại, có thể tìm ra một lượng chất cực nhỏ. Không có cây kim bạc nào làm được như vậy.

<short pause> <laugh> Kaku ghi chú: một lần nữa, đây là kiến thức để hiểu truyện, không phải cách kiểm tra thức ăn ngoài đời. Ngoài đời, nghi ngờ ngộ độc thì gọi cấp cứu ngay.

<short pause> Giờ tới phần vui. Kaku thử suy luận như Maomao với một vụ án nhỏ do Kaku tự nghĩ ra, hoàn toàn vô hại.

<short pause> Vụ án: trong một phòng khách, hoa cắm trong bình luôn héo chỉ sau hai ngày, trong khi hoa ở phòng bên cạnh tươi cả tuần. Người hầu đồn phòng đó bị ám.

<short pause> Quan sát: nước trong hai bình như nhau, ánh sáng như nhau. Điểm khác duy nhất: phòng hoa héo có một đĩa trái cây chín đặt ngay bên cạnh bình hoa.

<short pause> Suy luận: trái cây chín tỏa ra một loại khí tên là ethylene. Khí này thúc đẩy trái cây chín nhanh hơn, và cũng làm hoa cắm héo nhanh hơn.

<short pause> Lời giải: không có ma. Chỉ cần dời đĩa trái cây ra xa là hoa tươi lâu hơn. Đây là khoa học có thật, và bạn có thể tự quan sát ở nhà một cách an toàn.

<short pause> Kaku ghi chú: đó là tinh thần của Maomao. Khi người ta nói lời nguyền, cô hỏi: đâu là thứ khác biệt?
```

**ElevenLabs**

```text
Trong phim cung đình, ta hay thấy người ta dùng kim bạc hoặc đũa bạc để thử độc. Nếu bạc đổi màu đen thì có độc. [curious] Liệu có đúng không?

[pause] Khoa học nói: bạc bị xỉn đen khi gặp các hợp chất chứa lưu huỳnh. Ngày xưa, thạch tín thường lẫn tạp chất lưu huỳnh, nên bạc có lúc đổi màu thật.

[pause] Nhưng thạch tín tinh khiết thì không làm bạc đổi màu. Và nhiều loại độc khác, như độc từ cây cỏ, cũng không phản ứng với bạc. Trứng hay tỏi lại có thể làm bạc xỉn dù hoàn toàn vô hại.

[pause] Nên bạc chỉ là một cách thử rất không đáng tin. Đó là lý do trong truyện, người thử độc vẫn phải có kiến thức thật, và Maomao giỏi hơn một cây kim bạc rất nhiều.

[pause] Ngày nay, để phát hiện chất độc, các phòng thí nghiệm dùng những máy phân tích hiện đại, có thể tìm ra một lượng chất cực nhỏ. Không có cây kim bạc nào làm được như vậy.

[pause] [chuckles] Kaku ghi chú: một lần nữa, đây là kiến thức để hiểu truyện, không phải cách kiểm tra thức ăn ngoài đời. Ngoài đời, nghi ngờ ngộ độc thì gọi cấp cứu ngay.

[pause] Giờ tới phần vui. Kaku thử suy luận như Maomao với một vụ án nhỏ do Kaku tự nghĩ ra, hoàn toàn vô hại.

[pause] Vụ án: trong một phòng khách, hoa cắm trong bình luôn héo chỉ sau hai ngày, trong khi hoa ở phòng bên cạnh tươi cả tuần. Người hầu đồn phòng đó bị ám.

[pause] Quan sát: nước trong hai bình như nhau, ánh sáng như nhau. Điểm khác duy nhất: phòng hoa héo có một đĩa trái cây chín đặt ngay bên cạnh bình hoa.

[pause] Suy luận: trái cây chín tỏa ra một loại khí tên là ethylene. Khí này thúc đẩy trái cây chín nhanh hơn, và cũng làm hoa cắm héo nhanh hơn.

[pause] Lời giải: không có ma. Chỉ cần dời đĩa trái cây ra xa là hoa tươi lâu hơn. Đây là khoa học có thật, và bạn có thể tự quan sát ở nhà một cách an toàn.

[pause] Kaku ghi chú: đó là tinh thần của Maomao. Khi người ta nói lời nguyền, cô hỏi: đâu là thứ khác biệt?
```

### c06 · Vì sao bạn nên xem? / Maomao và những thám tử nổi tiếng / Ba bài học quan sát từ Maomao

Khoảng 150 giây · cảnh s60–s73 · 1951 ký tự

**Gemini**

```text
Tóm lại, có bốn lý do Kaku nghĩ bạn nên thử Dược sư tự sự.

<short pause> Một: mỗi tập thường có một bí ẩn nhỏ, được giải bằng kiến thức và quan sát, rất thỏa mãn. Hai: nhân vật chính cực kỳ cá tính, vừa thông minh vừa buồn cười.

<short pause> Ba: thế giới cung đình được xây dựng tỉ mỉ, đẹp và đầy âm mưu. Bốn: bên dưới những vụ án là một câu chuyện lớn hơn về những người phụ nữ sống trong một thế giới đầy luật lệ khắt khe.

<short pause> Nếu bạn thích trinh thám kiểu Sherlock Holmes, thích lịch sử và cung đình, hoặc đơn giản muốn nghỉ một chút khỏi những trận đánh, đây là lựa chọn hoàn hảo.

<short pause> Nếu phải xếp Maomao vào một nhóm, Kaku sẽ xếp cô cạnh những thám tử nổi tiếng nhất trong văn học và anime.

<short pause> Sherlock Holmes, nhân vật của nhà văn Arthur Conan Doyle, xuất hiện lần đầu năm 1887. Ông nổi tiếng vì quan sát những chi tiết nhỏ nhất, và còn là một người mê làm thí nghiệm hóa học.

<short pause> Thám tử lừng danh Conan, bắt đầu từ năm 1994, là bộ trinh thám anime quen thuộc nhất với khán giả Việt Nam, với hàng nghìn vụ án được giải bằng logic.

<short pause> Điểm chung của họ với Maomao: không có siêu năng lực, chỉ có quan sát, kiến thức và lý luận. Điểm khác: Maomao không muốn làm thám tử. Cô chỉ muốn được nghiên cứu thảo dược trong yên bình.

<short pause> <laugh> Kaku ghi chú: có lẽ đó là lý do cô được yêu thích. Một thiên tài bất đắc dĩ, luôn bị kéo vào rắc rối, và luôn giải quyết xong với vẻ mặt chán chường.

<short pause> Trước khi kết, Kaku rút ra ba bài học quan sát từ cách Maomao giải án, những bài học dùng được cả ngoài đời.

<short pause> Một: tìm điểm khác biệt. Khi hai tình huống gần giống nhau mà kết quả khác nhau, câu trả lời thường nằm ở chỗ khác nhau duy nhất.

<short pause> Hai: đừng tin lời đồn vội. Khi mọi người nói đó là lời nguyền hay ma quỷ, hãy hỏi xem có lời giải thích nào đơn giản hơn không.

<short pause> Ba: kiến thức từ sách chỉ mạnh khi đi kèm kinh nghiệm thực tế. Maomao giỏi vì cô vừa học từ cha nuôi, vừa làm việc với bệnh nhân thật mỗi ngày.

<short pause> Kaku ghi chú: ba bài học này không cần phải vào hậu cung mới dùng được. Chúng hữu ích cả khi bạn tìm chìa khóa bị mất.
```

**ElevenLabs**

```text
Tóm lại, có bốn lý do Kaku nghĩ bạn nên thử Dược sư tự sự.

[pause] Một: mỗi tập thường có một bí ẩn nhỏ, được giải bằng kiến thức và quan sát, rất thỏa mãn. Hai: nhân vật chính cực kỳ cá tính, vừa thông minh vừa buồn cười.

[pause] Ba: thế giới cung đình được xây dựng tỉ mỉ, đẹp và đầy âm mưu. Bốn: bên dưới những vụ án là một câu chuyện lớn hơn về những người phụ nữ sống trong một thế giới đầy luật lệ khắt khe.

[pause] Nếu bạn thích trinh thám kiểu Sherlock Holmes, thích lịch sử và cung đình, hoặc đơn giản muốn nghỉ một chút khỏi những trận đánh, đây là lựa chọn hoàn hảo.

[pause] Nếu phải xếp Maomao vào một nhóm, Kaku sẽ xếp cô cạnh những thám tử nổi tiếng nhất trong văn học và anime.

[pause] Sherlock Holmes, nhân vật của nhà văn Arthur Conan Doyle, xuất hiện lần đầu năm 1887. Ông nổi tiếng vì quan sát những chi tiết nhỏ nhất, và còn là một người mê làm thí nghiệm hóa học.

[pause] Thám tử lừng danh Conan, bắt đầu từ năm 1994, là bộ trinh thám anime quen thuộc nhất với khán giả Việt Nam, với hàng nghìn vụ án được giải bằng logic.

[pause] Điểm chung của họ với Maomao: không có siêu năng lực, chỉ có quan sát, kiến thức và lý luận. Điểm khác: Maomao không muốn làm thám tử. Cô chỉ muốn được nghiên cứu thảo dược trong yên bình.

[pause] [chuckles] Kaku ghi chú: có lẽ đó là lý do cô được yêu thích. Một thiên tài bất đắc dĩ, luôn bị kéo vào rắc rối, và luôn giải quyết xong với vẻ mặt chán chường.

[pause] Trước khi kết, Kaku rút ra ba bài học quan sát từ cách Maomao giải án, những bài học dùng được cả ngoài đời.

[pause] Một: tìm điểm khác biệt. Khi hai tình huống gần giống nhau mà kết quả khác nhau, câu trả lời thường nằm ở chỗ khác nhau duy nhất.

[pause] Hai: đừng tin lời đồn vội. Khi mọi người nói đó là lời nguyền hay ma quỷ, hãy hỏi xem có lời giải thích nào đơn giản hơn không.

[pause] Ba: kiến thức từ sách chỉ mạnh khi đi kèm kinh nghiệm thực tế. Maomao giỏi vì cô vừa học từ cha nuôi, vừa làm việc với bệnh nhân thật mỗi ngày.

[pause] Kaku ghi chú: ba bài học này không cần phải vào hậu cung mới dùng được. Chúng hữu ích cả khi bạn tìm chìa khóa bị mất.
```

### c07 · Góc nhìn của Kaku: kiến thức là sức mạnh / Lộ trình xem cho người mới / Kết

Khoảng 120 giây · cảnh s74–s86 · 1565 ký tự

**Gemini**

```text
<laugh> Kênh của Kaku thường nói về những hệ thống sức mạnh: Nen, chú lực, Haki. Vậy Dược sư tự sự có hệ thống sức mạnh không?

<short pause> Kaku nghĩ là có. Chỉ là sức mạnh ở đây không nằm trong cơ thể, mà nằm trong đầu. Người biết nhiều hơn thì kiểm soát được nhiều hơn.

<short pause> Trong một thế giới mà một cung nữ không có quyền gì, kiến thức là thứ duy nhất giúp Maomao được lắng nghe, được bảo vệ, và cứu được người khác.

<short pause> Và giống mọi sức mạnh, nó cũng có cái giá: càng biết nhiều, cô càng bị cuốn vào những bí mật nguy hiểm mà cô chỉ muốn tránh xa.

<short pause> Kaku thấy đây là bài học rất thật: trong đời thật, không có phép thuật, nhưng kiến thức luôn là sức mạnh mà ai cũng có thể luyện được.

<short pause> Nếu muốn bắt đầu, đây là lộ trình Kaku gợi ý.

<short pause> Bước một: xem mùa một từ đầu, hai mươi bốn tập. Ba tập đầu đủ để bạn biết mình có thích nhịp của bộ này hay không.

<short pause> Bước hai: xem tiếp mùa hai, rồi theo dõi mùa ba đang phát. Nếu thích, bộ phim điện ảnh tháng mười hai là một câu chuyện riêng, rất đáng chờ.

<short pause> Và như mọi khi, hãy xem qua các nền tảng có bản quyền để ủng hộ những người làm ra bộ phim.

<short pause> Tóm lại: Dược sư tự sự là câu chuyện về một cô gái mê độc dược bị bán vào hậu cung, và dùng kiến thức về thuốc để giải những bí ẩn mà người khác gọi là lời nguyền.

<short pause> Câu hỏi cho bạn: nếu được sống trong hậu cung, bạn muốn làm phi tần, cung nữ, thái giám hay người thử độc? Kaku thì chọn làm dược sư, vì được ngửi thảo dược cả ngày.

<short pause> Video tới quay lại với thế giới sức mạnh: Kaku kể lịch sử của JoJo, từ kỹ thuật thở Hamon cho tới những Stand kỳ lạ nhất.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. Kaku cất giỏ thảo dược đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Kênh của Kaku thường nói về những hệ thống sức mạnh: Nen, chú lực, Haki. [curious] Vậy Dược sư tự sự có hệ thống sức mạnh không?

[pause] Kaku nghĩ là có. Chỉ là sức mạnh ở đây không nằm trong cơ thể, mà nằm trong đầu. Người biết nhiều hơn thì kiểm soát được nhiều hơn.

[pause] Trong một thế giới mà một cung nữ không có quyền gì, kiến thức là thứ duy nhất giúp Maomao được lắng nghe, được bảo vệ, và cứu được người khác.

[pause] Và giống mọi sức mạnh, nó cũng có cái giá: càng biết nhiều, cô càng bị cuốn vào những bí mật nguy hiểm mà cô chỉ muốn tránh xa.

[pause] Kaku thấy đây là bài học rất thật: trong đời thật, không có phép thuật, nhưng kiến thức luôn là sức mạnh mà ai cũng có thể luyện được.

[pause] Nếu muốn bắt đầu, đây là lộ trình Kaku gợi ý.

[pause] Bước một: xem mùa một từ đầu, hai mươi bốn tập. Ba tập đầu đủ để bạn biết mình có thích nhịp của bộ này hay không.

[pause] Bước hai: xem tiếp mùa hai, rồi theo dõi mùa ba đang phát. Nếu thích, bộ phim điện ảnh tháng mười hai là một câu chuyện riêng, rất đáng chờ.

[pause] Và như mọi khi, hãy xem qua các nền tảng có bản quyền để ủng hộ những người làm ra bộ phim.

[pause] Tóm lại: Dược sư tự sự là câu chuyện về một cô gái mê độc dược bị bán vào hậu cung, và dùng kiến thức về thuốc để giải những bí ẩn mà người khác gọi là lời nguyền.

[pause] Câu hỏi cho bạn: nếu được sống trong hậu cung, bạn muốn làm phi tần, cung nữ, thái giám hay người thử độc? Kaku thì chọn làm dược sư, vì được ngửi thảo dược cả ngày.

[pause] Video tới quay lại với thế giới sức mạnh: Kaku kể lịch sử của JoJo, từ kỹ thuật thở Hamon cho tới những Stand kỳ lạ nhất.

[pause] Đăng ký kênh để không bỏ lỡ nhé. Kaku cất giỏ thảo dược đây, hẹn gặp lại!
```
