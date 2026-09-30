# Bộ prompt · Dược sư tự sự: Bí ẩn thân thế Jinshi — 5 manh mối, 1 giả thuyết (lý thuyết có gắn nhãn)

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 7 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo spoiler: video này dùng manh mối trong anime Dược sư tự sự tới mùa ba phần một. Gần cuối có một vùng…

```text
Wide 16:9 landscape cinematic frame. a folded palace letter sealed with wax beside a spoiler warning card on a lacquered table, close-up, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một người đàn ông đẹp tới mức cả hậu cung xôn xao. Anh tự nhận là một hoạn quan, quản lý hậu cung của Hoàng đ…

```text
Wide 16:9 landscape cinematic frame. a long palace corridor with red pillars and a single elegant silhouette in flowing robes walking away, back view, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Câu hỏi của hôm nay: Jinshi thật sự là con của ai? Và vì sao câu trả lời ấy có thể làm rung chuyển cả hoàng c…

```text
Wide 16:9 landscape cinematic frame. an old imperial family tree scroll with one branch blotted out by ink, extreme close-up, dim lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku làm thám tử cung đình: gom manh mối có thật trong anime, dựng giả th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny scholar's hat and holding a magnifying glass over a scroll. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và Kaku nhắc: Dược sư tự sự nói nhiều về thuốc và độc. Những gì Kaku kể là để hiểu truyện, không phải lời khu…

```text
Wide 16:9 landscape cinematic frame. a row of small porcelain medicine jars on a wooden shelf with a warning tag hanging from one, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Hồ sơ công khai của Jinshi

Lời: Bắt đầu từ những gì ai cũng thấy. Jinshi xuất hiện như một hoạn quan trẻ, được giao quản lý hậu cung. Anh thô…

```text
Wide 16:9 landscape cinematic frame. a group of court ladies peeking from behind a folding screen at a distant elegant figure, humorous wide shot, warm palace light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Anh là người phát hiện ra tài năng của Maomao, một cô gái bán thuốc bị bắt vào cung làm cung nữ, và kéo cô và…

```text
Wide 16:9 landscape cinematic frame. a young woman sniffing a small herb bundle at a workbench while a shadowy tall figure watches from the doorway, medium shot, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhưng dần dần, anime cho thấy Jinshi không phải hoạn quan. Đó là một vỏ bọc. Thân phận thật của anh là Hoàng…

```text
Wide 16:9 landscape cinematic frame. an elegant robe hanging on a stand with a hidden imperial seal visible beneath its folded sleeve, extreme close-up, dramatic lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Theo hồ sơ chính thức, cha của Jinshi là vị Hoàng đế trước, và mẹ là Thái hậu An Thị. Vì Hoàng đế hiện tại ch…

```text
Wide 16:9 landscape cinematic frame. a formal genealogy chart on silk with three names connected by gold lines, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Jinshi còn có một người hầu cận luôn đi theo, điềm tĩnh, trung thành, và dường như biết nhiều hơn những gì an…

```text
Wide 16:9 landscape cinematic frame. a composed tall attendant silhouette standing a step behind a younger figure in a palace hallway, medium shot, calm warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Vậy tại sao một Hoàng đệ lại phải đóng giả hoạn quan? Đó là câu hỏi đầu tiên, và cũng là manh mối đầu tiên rằ…

```text
Wide 16:9 landscape cinematic frame. a mask resting on a palace desk beside a sheathed ceremonial dagger, close-up, low candle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Jinshi là người đầy bí mật, nhưng lại luôn nhờ Maomao giải bí mật của người khác. Người điều tra h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering into a mirror and seeing a question mark reflected back. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Hậu cung vận hành thế nào?

Lời: Để hiểu bí ẩn này, cần hiểu hậu cung trong truyện. Đó là một thành phố thu nhỏ bên trong hoàng cung, với hàng…

```text
Wide 16:9 landscape cinematic frame. an aerial view of a walled inner palace city with many courtyards and pavilions at dawn, extreme wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Đứng đầu là bốn phi tần cấp cao nhất. Mỗi người có cung điện riêng, người hầu riêng, và gia tộc đứng sau. Ai…

```text
Wide 16:9 landscape cinematic frame. four ornate pavilions arranged around a central courtyard, each with a different colored banner, wide shot, warm palace light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Ah-Duo từng là một trong bốn người ấy, và là người ở bên Hoàng đế lâu nhất, từ khi ông còn là Thái tử.

```text
Wide 16:9 landscape cinematic frame. a tall elegant silhouette standing alone in an emptied pavilion with packed chests, medium shot, bittersweet warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Vì vậy, mỗi đứa trẻ ra đời trong hậu cung không chỉ là một đứa trẻ. Đó là một quân cờ trong ván cờ quyền lực,…

```text
Wide 16:9 landscape cinematic frame. a tiny cradle placed in the middle of a giant game board with pieces surrounding it, symbolic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: trong một nơi mà đứa trẻ là quân cờ, việc đổi hai quân cờ cho nhau có thể là cách duy nhất để bảo…

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently moving two small pieces on a board with a worried face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Hậu cung ngoài lịch sử thật

Lời: Thế giới của Dược sư tự sự là một đất nước hư cấu, nhưng lấy cảm hứng rõ ràng từ các triều đại Trung Hoa thời…

```text
Wide 16:9 landscape cinematic frame. a traditional East Asian palace roofline with curved eaves against a misty morning sky, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Trong lịch sử, hậu cung của các hoàng đế Trung Hoa thường có hệ thống cấp bậc phi tần rất chặt, và hoạn quan…

```text
Wide 16:9 landscape cinematic frame. an old ledger with rows of rank titles written in neat columns beside a brush and ink stone, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Cuộc tranh giành ngôi thái tử trong lịch sử cũng rất khốc liệt. Vì vậy, nỗi lo về một đứa trẻ bị đánh tráo ha…

```text
Wide 16:9 landscape cinematic frame. a faded scroll painting of a quiet palace courtyard at night with a single lantern, close-up, aged golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: Kaku không nói Dược sư tự sự dựa trên một sự kiện lịch sử cụ thể nào. Truyện chỉ mượn không khí và…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a history book in one wing and a novel in the other, balancing them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Manh mối 1: hai đứa trẻ cùng ra đời

Lời: Manh mối đầu tiên nằm ở quá khứ. Gần hai mươi năm trước, hai người phụ nữ trong cung sinh con gần như cùng lú…

```text
Wide 16:9 landscape cinematic frame. two small cradles side by side in a dim palace chamber, one draped in finer silk than the other, wide shot, soft candle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Một người là An Thị, khi ấy là phi tần của Hoàng đế trước, sau này là Thái hậu. Người kia là Ah-Duo, phi tần…

```text
Wide 16:9 landscape cinematic frame. two silk fans laid on a table, one ornate with a phoenix pattern, one simple and elegant, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Vì thứ bậc trong cung, An Thị được các thầy thuốc giỏi nhất chăm sóc. Còn Ah-Duo bị bỏ lại, sinh con trong đi…

```text
Wide 16:9 landscape cinematic frame. a crowd of physicians hurrying toward one lit doorway while another doorway down the corridor stays dark, wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Hậu quả: Ah-Duo không thể có con thêm nữa. Và về sau, cô rời khỏi hậu cung.

```text
Wide 16:9 landscape cinematic frame. an empty palace chamber with a single hairpin left on a dressing table, close-up, pale melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Chi tiết ấy cho thấy một điều lạnh lùng: trong hậu cung, ai được cứu, ai bị bỏ mặc, phụ thuộc vào thứ bậc hơn…

```text
Wide 16:9 landscape cinematic frame. a ladder of rank plaques on a palace wall with a single candle lit only at the top, symbolic close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Kaku ghi vào sổ: manh mối một là có thật trong anime. Hai đứa trẻ, cùng thời điểm, trong hai hoàn cảnh chênh…

```text
Wide 16:9 landscape cinematic frame. a notebook page with two small cradle doodles and a checkmark labeled clue one, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Manh mối 2: mật ong

Lời: Theo anime, con của Ah-Duo không sống được lâu. Đứa bé mất khi còn rất nhỏ.

```text
Wide 16:9 landscape cinematic frame. a tiny embroidered baby shoe resting alone on a windowsill in the rain, extreme close-up, grey soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và Maomao, với đầu óc của một dược sư, lần ra nguyên nhân có thể: mật ong. Mật ong nguy hiểm với trẻ sơ sinh.

```text
Wide 16:9 landscape cinematic frame. a small ceramic honey jar with a wooden dipper on a palace table, a warning red ribbon tied around it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Đây là chi tiết có thật ngoài đời. Các cơ quan y tế khuyên không cho trẻ dưới mười hai tháng tuổi ăn mật ong,…

```text
Wide 16:9 landscape cinematic frame. a simple health information card with a crossed-out honey jar icon and a baby rattle icon, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Nhưng câu hỏi quan trọng là: đứa trẻ đã mất là con của ai? Nếu có ai đó chăm sóc nhầm một đứa bé, trong một đ…

```text
Wide 16:9 landscape cinematic frame. two identical swaddling cloths folded side by side on a shelf, extreme close-up, dim uncertain light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Với Maomao, một hũ mật ong không chỉ là đồ ngọt. Cùng một thứ, với người lớn là món ăn, với trẻ sơ sinh lại c…

```text
Wide 16:9 landscape cinematic frame. a honey jar placed on a balance scale opposite a small medicine vial, symbolic close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: mỗi khi Maomao nhắc tới độc hay mật ong, hãy nhìn nét mặt những cung nữ lớn tuổi trong cảnh. Nhiều…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small group of elderly silhouettes whose faces are turned away. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Manh mối 3: gương mặt và dáng người

Lời: Manh mối ba mang tính hình ảnh. Ah-Duo được miêu tả là một người có vẻ đẹp phóng khoáng, cao ráo, đôi khi mặc…

```text
Wide 16:9 landscape cinematic frame. a tall elegant silhouette in a simple men's style robe standing on a palace balcony in the wind, wide shot, soft moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Còn Jinshi thì có vẻ đẹp khiến người ta không phân biệt nổi là nam hay nữ. Nhiều người xem để ý rằng hai ngườ…

```text
Wide 16:9 landscape cinematic frame. two silhouettes facing each other in profile across a moonlit courtyard, symmetrical composition, soft silver light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Trong khi đó, Jinshi không có nhiều nét giống An Thị, người được cho là mẹ ruột của anh.

```text
Wide 16:9 landscape cinematic frame. a portrait frame on a wall left intentionally blank beside a mirror reflecting a different face, symbolic close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Cả hai còn có một phong thái giống nhau: điềm tĩnh, hơi xa cách, và rất giỏi che giấu cảm xúc sau một nụ cười.

```text
Wide 16:9 landscape cinematic frame. two folding fans half covering two smiling mouths side by side, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Kaku nhắc: gương mặt là manh mối yếu nhất. Trong truyện hay ngoài đời, con cái không phải lúc nào cũng giống…

```text
Wide 16:9 landscape cinematic frame. a notebook with a clue written in pencil and a small question mark beside it, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Manh mối 4: cách người lớn đối xử với Jinshi

Lời: Manh mối bốn nằm ở hành vi. Thái hậu An Thị, người mẹ chính thức, đối xử với Jinshi khá xa cách. Không lạnh l…

```text
Wide 16:9 landscape cinematic frame. an older noble silhouette seated on a throne-like chair turning her face slightly away from a kneeling figure, medium shot, cool distant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Trong khi đó, Hoàng đế đối xử với Jinshi rất thân thiết, đôi khi như một người cha trêu con hơn là một người…

```text
Wide 16:9 landscape cinematic frame. a broad-shouldered bearded silhouette laughing and patting the shoulder of a younger slender figure in a garden, medium shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và Ah-Duo, khi xuất hiện cùng Jinshi, có một sự dịu dàng khó giải thích, như thể cô biết điều gì đó mà anh kh…

```text
Wide 16:9 landscape cinematic frame. a tall silhouette watching a younger figure from a distance with a gentle smile under a lantern, wide shot, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi vào sổ: manh mối bốn là cách người lớn nhìn Jinshi. Và thú vị thay, chính Jinshi dường như không hiể…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing three small faces with arrows pointing toward one figure in the center. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Maomao: cô thám tử dược sư

Lời: Người sẽ giải bí ẩn này, nếu có ai giải được, là Maomao. Cô lớn lên ở khu phố đèn đỏ, được một người cha nuôi…

```text
Wide 16:9 landscape cinematic frame. a small apothecary shop at night in a lantern-lit district with dried herbs hanging in the window, wide shot, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Cô có khứu giác cực nhạy, trí nhớ về thảo dược đáng kinh ngạc, và một niềm đam mê kỳ lạ với độc chất.

```text
Wide 16:9 landscape cinematic frame. a hand holding a sprig of herbs close to the nose with small labeled jars in the background, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Cô còn thử độc trên chính cơ thể mình để hiểu chúng. Kaku nhắc rõ: đây là chi tiết hư cấu, tuyệt đối không ph…

```text
Wide 16:9 landscape cinematic frame. a warning sign with a crossed-out hand next to a small bottle on a shelf, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Điều làm Maomao trở thành thám tử giỏi là cô chỉ tin vào bằng chứng. Cô không kết luận khi chưa đủ dữ kiện, v…

```text
Wide 16:9 landscape cinematic frame. a notebook with neat observations and one sentence deliberately left blank, close-up, soft lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Manh mối 5: vì sao phải giả làm hoạn quan?

Lời: Quay lại câu hỏi đầu tiên. Một Hoàng đệ có quyền kế vị, tại sao phải sống dưới vỏ bọc hoạn quan?

```text
Wide 16:9 landscape cinematic frame. a heavy palace door half open revealing a long corridor with a single figure in plain robes, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Một cách hiểu: Jinshi muốn thoát khỏi vị trí người kế vị. Anh muốn Hoàng đế sớm có con trai, để mình không bị…

```text
Wide 16:9 landscape cinematic frame. a crown resting on a cushion with a hand pushing it slightly away, extreme close-up, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Vỏ bọc hoạn quan giúp anh vào hậu cung, quan sát các phi tần, và âm thầm bảo vệ những người có thể sinh ra ng…

```text
Wide 16:9 landscape cinematic frame. a figure moving quietly through a night garden past several lit pavilion windows, wide shot, moonlit light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Anh cũng dùng chính vẻ đẹp của mình như một công cụ, để người khác mất cảnh giác và nói nhiều hơn họ định.

```text
Wide 16:9 landscape cinematic frame. a group of court officials leaning in and chatting eagerly toward a serene figure holding a teacup, medium shot, warm palace light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhưng nếu Jinshi là con ruột của Hoàng đế, thì vị trí của anh còn nhạy cảm hơn nhiều. Anh không chỉ là em tra…

```text
Wide 16:9 landscape cinematic frame. a chess board with a single piece standing apart from its row, lit by a spotlight, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Giả thuyết: hai đứa trẻ bị hoán đổi

Lời: LÝ THUYẾT. Gom năm manh mối lại, ta có giả thuyết phổ biến nhất: đêm ấy, hai đứa trẻ đã bị hoán đổi.

```text
Wide 16:9 landscape cinematic frame. a large red stamp reading THEORY pressed onto a sheet of parchment beside two cradle doodles, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Theo giả thuyết này, đứa bé khỏe mạnh của Ah-Duo được đưa sang làm con của An Thị. Đứa bé ấy chính là Jinshi.

```text
Wide 16:9 landscape cinematic frame. two pairs of hands gently passing a swaddled bundle between two dimly lit rooms, close-up, soft candle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Còn đứa con của An Thị, được Ah-Duo nuôi như con mình, và chính đứa bé ấy đã mất khi còn nhỏ.

```text
Wide 16:9 landscape cinematic frame. a single cradle in a quiet room with a candle burning low beside it, wide shot, somber warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Nếu đúng, thì Jinshi là con ruột của Hoàng đế hiện tại và Ah-Duo. Người anh anh vẫn gọi, thật ra là cha anh.

```text
Wide 16:9 landscape cinematic frame. a family tree diagram on parchment being redrawn with a new line connecting a crown icon directly to a young figure icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc lại: đây là LÝ THUYẾT dựa trên manh mối trong anime. Kaku chưa khẳng định. Phần tiếp theo, Kaku sẽ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a sign with the word theory and a small warning triangle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Những khả năng khác

Lời: Trước khi phản biện, Kaku liệt kê những khả năng khác về mặt logic, để giả thuyết hoán đổi không phải lựa chọ…

```text
Wide 16:9 landscape cinematic frame. a notebook page with three branching arrows from a single question mark, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: LÝ THUYẾT A: Jinshi đúng là con của Hoàng đế trước và An Thị, và mọi manh mối chỉ là sự trùng hợp. Đây là các…

```text
Wide 16:9 landscape cinematic frame. a straight single line drawn between two points on parchment, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: LÝ THUYẾT B: có hoán đổi, nhưng không ai trong hai người mẹ chủ động làm. Đó là một sự nhầm lẫn trong đêm hỗn…

```text
Wide 16:9 landscape cinematic frame. two lanterns placed on the wrong doorsteps in a dark corridor, symbolic close-up, uncertain dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: LÝ THUYẾT C: hoán đổi có chủ đích, do hai người mẹ đồng ý với nhau. Đây là giả thuyết khớp nhất, và là giả th…

```text
Wide 16:9 landscape cinematic frame. two hands meeting in a quiet agreement over a small table with a single candle, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Phản biện

Lời: Phản biện một: hoán đổi con trong hoàng cung là tội cực nặng. Ai dám làm, và làm sao giữ bí mật suốt gần hai…

```text
Wide 16:9 landscape cinematic frame. a heavy iron lock on an old palace door with a faint crack in the wood beside it, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Trả lời thử: chỉ cần hai người mẹ đồng ý, và vài cung nữ trung thành. Mà theo anime, đêm ấy cả hoàng cung đan…

```text
Wide 16:9 landscape cinematic frame. a narrow servants' corridor with only two lanterns lit while the main hall glows brightly far away, wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Phản biện hai: vì sao An Thị lại đồng ý? Một người mẹ có thể đổi con mình lấy con người khác sao?

```text
Wide 16:9 landscape cinematic frame. a single hand resting hesitantly on the edge of a cradle, extreme close-up, uncertain dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Đây là chỗ các tóm tắt từ tiểu thuyết cho thấy câu chuyện của An Thị rất đau lòng, với những hoàn cảnh cô khô…

```text
Wide 16:9 landscape cinematic frame. a withered flower pressed between the pages of an old closed book, close-up, somber soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Phản biện ba: nếu mọi thứ chỉ là gương mặt và thái độ, thì có thể Jinshi đơn giản là em trai Hoàng đế, và mọi…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a handful of small clue cards on one side and an official seal on the other, symbolic close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là điểm yếu thật của giả thuyết. Phần lớn manh mối là gián tiếp. Chỉ riêng manh mối mật ong là…

```text
Wide 16:9 landscape cinematic frame. the owl mascot crossing out one clue and circling another in a notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Vùng spoiler tiểu thuyết

Lời: Từ đây là vùng spoiler tiểu thuyết. Nếu bạn chỉ muốn xem anime, hãy tua tới chương tiếp theo, khi thấy chữ Hế…

```text
Wide 16:9 landscape cinematic frame. a red rope barrier across a palace corridor with a hanging sign showing a warning symbol, wide shot, dramatic lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Theo nhiều trang tổng hợp về bộ truyện, tiểu thuyết gốc đã xác nhận giả thuyết hoán đổi: Jinshi là con ruột c…

```text
Wide 16:9 landscape cinematic frame. an old book opening to reveal a single glowing line of text highlighted in gold, symbolic close-up, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Và theo các tóm tắt ấy, chính Jinshi không được cho biết sự thật từ nhỏ. Thân phận thật trở thành gánh nặng m…

```text
Wide 16:9 landscape cinematic frame. a figure standing alone before a tall mirror in an empty hall at dusk, back view, wide shot, somber golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku vẫn giữ nhãn lý thuyết cho người chỉ xem anime, vì anime có thể kể theo cách riêng. Hết vùng spoiler.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling the red rope barrier aside with a relieved smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Điều này thay đổi gì?

Lời: Nếu Jinshi là con của Hoàng đế, cuộc tranh ngôi trong hoàng cung trở nên nguy hiểm hơn nhiều. Mỗi đứa trẻ ra…

```text
Wide 16:9 landscape cinematic frame. several small candles in a dark palace hall, some flickering in a draft, symbolic wide shot, tense warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nó cũng giải thích vì sao Jinshi quá quan tâm tới sự an toàn của các phi tần và những đứa trẻ. Có thể anh hiể…

```text
Wide 16:9 landscape cinematic frame. a figure gently straightening a small blanket over an empty cradle in a quiet nursery, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và nó làm mối quan hệ giữa Jinshi và Maomao phức tạp hơn. Maomao muốn một cuộc sống bình thường với thảo dược…

```text
Wide 16:9 landscape cinematic frame. two silhouettes standing on either side of a garden gate, one holding an herb basket, one in formal robes, wide shot, bittersweet dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Còn với Hoàng đế, nếu giả thuyết đúng, việc giữ im lặng cũng là một cách bảo vệ con mình khỏi những kẻ muốn l…

```text
Wide 16:9 landscape cinematic frame. a broad-shouldered silhouette standing alone on a palace terrace at night looking down at a lit pavilion, wide shot, somber moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Maomao là người giỏi nhất cung trong việc tìm sự thật. Nhưng với sự thật này, cô có vẻ chọn không…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a scroll gently and tying it with a ribbon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Bảng manh mối tổng kết

Lời: Tổng kết bằng một trang. Manh mối một: hai đứa trẻ cùng ra đời, trong hai hoàn cảnh chênh lệch. Độ tin cậy: c…

```text
Wide 16:9 landscape cinematic frame. a clue board on parchment with a first card showing two cradles and three filled stars, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Manh mối hai: mật ong và đứa trẻ đã mất. Độ tin cậy: cao. Manh mối ba: gương mặt. Độ tin cậy: thấp.

```text
Wide 16:9 landscape cinematic frame. the next two cards on the clue board, a honey jar with three stars and a face outline with one star, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Manh mối bốn: thái độ của người lớn. Độ tin cậy: trung bình. Manh mối năm: vỏ bọc hoạn quan. Độ tin cậy: trun…

```text
Wide 16:9 landscape cinematic frame. the last two cards on the clue board, three small faces and a mask, each with two stars, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Kết luận của Kaku: giả thuyết hoán đổi là cách giải thích khớp nhất với mọi manh mối. Nhưng với người chỉ xem…

```text
Wide 16:9 landscape cinematic frame. the complete clue board with a red string connecting all five cards to a central theory card, amber ink close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Câu hỏi mở cho bạn

Lời: Giờ tới lượt bạn. Nếu bạn là Jinshi và biết được sự thật, bạn sẽ làm gì? Giữ im lặng để bảo vệ mọi người, hay…

```text
Wide 16:9 landscape cinematic frame. a figure standing at a crossroads in a palace garden with two lantern-lit paths leading in different directions, wide shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và nếu bạn là Maomao, bạn có hỏi thẳng Jinshi không? Hay chọn giả vờ không biết?

```text
Wide 16:9 landscape cinematic frame. a small herb basket resting beside a folded unopened letter on a wooden bench, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy viết câu trả lời vào bình luận. Kaku muốn đọc xem ai là người chọn sự thật, và ai là người chọn sự bình y…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a quill pen over a blank scroll, looking expectantly at the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Một hoạn quan không phải hoạn quan. Một người em có thể là con. Và một hũ mật ong nhỏ giữ bí mật của cả hoàng…

```text
Wide 16:9 landscape cinematic frame. a small honey jar and a porcelain medicine cup side by side on a palace table at dusk, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Khi phần hai của mùa ba lên sóng vào tháng tư, hãy xem lại những cảnh có Ah-Duo và Thái hậu. Bạn sẽ thấy nhiề…

```text
Wide 16:9 landscape cinematic frame. a calendar page for April with a small lantern doodle beside a circled date, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tiếp theo, Kaku đặt ba hệ kiếm thuật lên cùng một bàn: Hơi thở của Kimetsu, kiếm Haki của One Piece, và…

```text
Wide 16:9 landscape cinematic frame. three different swords laid side by side on a long table, each with a different glow, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những cuộc điều tra có gắn nhãn rõ ràng, hãy đăng ký kênh. Và nhớ: đừng cho trẻ nhỏ ăn mật ong,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot putting a lid firmly on a honey jar and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hồ sơ công khai của Jinshi

Khoảng 141 giây · cảnh s01–s12 · 1827 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này dùng manh mối trong anime Dược sư tự sự tới mùa ba phần một. Gần cuối có một vùng spoiler tiểu thuyết, Kaku sẽ báo trước để bạn tua qua nếu muốn.

<short pause> Một người đàn ông đẹp tới mức cả hậu cung xôn xao. Anh tự nhận là một hoạn quan, quản lý hậu cung của Hoàng đế. <short pause> Nhưng càng xem, ta càng thấy anh không phải người như anh nói.

<short pause> Câu hỏi của hôm nay: Jinshi thật sự là con của ai? Và vì sao câu trả lời ấy có thể làm rung chuyển cả hoàng cung?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku làm thám tử cung đình: gom manh mối có thật trong anime, dựng giả thuyết, rồi tự phản biện. Mọi giả thuyết đều được gắn nhãn LÝ THUYẾT rõ ràng.

<short pause> Và Kaku nhắc: Dược sư tự sự nói nhiều về thuốc và độc. Những gì Kaku kể là để hiểu truyện, không phải lời khuyên y tế.

<short pause> Bắt đầu từ những gì ai cũng thấy. Jinshi xuất hiện như một hoạn quan trẻ, được giao quản lý hậu cung. Anh thông minh, lịch thiệp, và đẹp tới mức các phi tần phải ngẩn ngơ.

<short pause> Anh là người phát hiện ra tài năng của Maomao, một cô gái bán thuốc bị bắt vào cung làm cung nữ, và kéo cô vào những vụ án trong hậu cung.

<short pause> Nhưng dần dần, anime cho thấy Jinshi không phải hoạn quan. Đó là một vỏ bọc. Thân phận thật của anh là Hoàng đệ, em trai của Hoàng đế, tên thật là Ka Zuigetsu.

<short pause> Theo hồ sơ chính thức, cha của Jinshi là vị Hoàng đế trước, và mẹ là Thái hậu An Thị. Vì Hoàng đế hiện tại chưa có con trai nối ngôi vững chắc, Jinshi có một vị trí rất nhạy cảm.

<short pause> Jinshi còn có một người hầu cận luôn đi theo, điềm tĩnh, trung thành, và dường như biết nhiều hơn những gì anh ta nói ra.

<short pause> Vậy tại sao một Hoàng đệ lại phải đóng giả hoạn quan? Đó là câu hỏi đầu tiên, và cũng là manh mối đầu tiên rằng thân phận của anh còn phức tạp hơn thế.

<short pause> Kaku để ý: Jinshi là người đầy bí mật, nhưng lại luôn nhờ Maomao giải bí mật của người khác. Người điều tra hậu cung, hóa ra lại là vụ án lớn nhất.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này dùng manh mối trong anime Dược sư tự sự tới mùa ba phần một. Gần cuối có một vùng spoiler tiểu thuyết, Kaku sẽ báo trước để bạn tua qua nếu muốn.

[pause] Một người đàn ông đẹp tới mức cả hậu cung xôn xao. Anh tự nhận là một hoạn quan, quản lý hậu cung của Hoàng đế. [pause] Nhưng càng xem, ta càng thấy anh không phải người như anh nói.

[pause] [curious] Câu hỏi của hôm nay: Jinshi thật sự là con của ai? Và vì sao câu trả lời ấy có thể làm rung chuyển cả hoàng cung?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku làm thám tử cung đình: gom manh mối có thật trong anime, dựng giả thuyết, rồi tự phản biện. Mọi giả thuyết đều được gắn nhãn LÝ THUYẾT rõ ràng.

[pause] Và Kaku nhắc: Dược sư tự sự nói nhiều về thuốc và độc. Những gì Kaku kể là để hiểu truyện, không phải lời khuyên y tế.

[pause] Bắt đầu từ những gì ai cũng thấy. Jinshi xuất hiện như một hoạn quan trẻ, được giao quản lý hậu cung. Anh thông minh, lịch thiệp, và đẹp tới mức các phi tần phải ngẩn ngơ.

[pause] Anh là người phát hiện ra tài năng của Maomao, một cô gái bán thuốc bị bắt vào cung làm cung nữ, và kéo cô vào những vụ án trong hậu cung.

[pause] Nhưng dần dần, anime cho thấy Jinshi không phải hoạn quan. Đó là một vỏ bọc. Thân phận thật của anh là Hoàng đệ, em trai của Hoàng đế, tên thật là Ka Zuigetsu.

[pause] Theo hồ sơ chính thức, cha của Jinshi là vị Hoàng đế trước, và mẹ là Thái hậu An Thị. Vì Hoàng đế hiện tại chưa có con trai nối ngôi vững chắc, Jinshi có một vị trí rất nhạy cảm.

[pause] Jinshi còn có một người hầu cận luôn đi theo, điềm tĩnh, trung thành, và dường như biết nhiều hơn những gì anh ta nói ra.

[pause] Vậy tại sao một Hoàng đệ lại phải đóng giả hoạn quan? Đó là câu hỏi đầu tiên, và cũng là manh mối đầu tiên rằng thân phận của anh còn phức tạp hơn thế.

[pause] Kaku để ý: Jinshi là người đầy bí mật, nhưng lại luôn nhờ Maomao giải bí mật của người khác. Người điều tra hậu cung, hóa ra lại là vụ án lớn nhất.
```

### c02 · Hậu cung vận hành thế nào? / Hậu cung ngoài lịch sử thật / Manh mối 1: hai đứa trẻ cùng ra đời

Khoảng 152 giây · cảnh s13–s27 · 1980 ký tự

**Gemini**

```text
Để hiểu bí ẩn này, cần hiểu hậu cung trong truyện. Đó là một thành phố thu nhỏ bên trong hoàng cung, với hàng nghìn cung nữ, hoạn quan, và các phi tần của Hoàng đế.

<short pause> Đứng đầu là bốn phi tần cấp cao nhất. Mỗi người có cung điện riêng, người hầu riêng, và gia tộc đứng sau. Ai sinh được con trai cho Hoàng đế, người đó và gia tộc của họ có thể thay đổi vận mệnh.

<short pause> Ah-Duo từng là một trong bốn người ấy, và là người ở bên Hoàng đế lâu nhất, từ khi ông còn là Thái tử.

<short pause> Vì vậy, mỗi đứa trẻ ra đời trong hậu cung không chỉ là một đứa trẻ. Đó là một quân cờ trong ván cờ quyền lực, dù đứa bé chẳng hề biết gì.

<short pause> <laugh> Kaku để ý: trong một nơi mà đứa trẻ là quân cờ, việc đổi hai quân cờ cho nhau có thể là cách duy nhất để bảo vệ chúng.

<short pause> Thế giới của Dược sư tự sự là một đất nước hư cấu, nhưng lấy cảm hứng rõ ràng từ các triều đại Trung Hoa thời xưa.

<short pause> Trong lịch sử, hậu cung của các hoàng đế Trung Hoa thường có hệ thống cấp bậc phi tần rất chặt, và hoạn quan là những người được phép làm việc bên trong.

<short pause> Cuộc tranh giành ngôi thái tử trong lịch sử cũng rất khốc liệt. Vì vậy, nỗi lo về một đứa trẻ bị đánh tráo hay bị hại không phải chuyện hoàn toàn xa lạ với người xưa.

<short pause> Kaku nhắc: Kaku không nói Dược sư tự sự dựa trên một sự kiện lịch sử cụ thể nào. Truyện chỉ mượn không khí và luật chơi của hậu cung xưa.

<short pause> Manh mối đầu tiên nằm ở quá khứ. Gần hai mươi năm trước, hai người phụ nữ trong cung sinh con gần như cùng lúc.

<short pause> Một người là An Thị, khi ấy là phi tần của Hoàng đế trước, sau này là Thái hậu. Người kia là Ah-Duo, phi tần của Thái tử, tức Hoàng đế hiện tại.

<short pause> Vì thứ bậc trong cung, An Thị được các thầy thuốc giỏi nhất chăm sóc. Còn Ah-Duo bị bỏ lại, sinh con trong điều kiện thiếu thốn.

<short pause> Hậu quả: Ah-Duo không thể có con thêm nữa. Và về sau, cô rời khỏi hậu cung.

<short pause> Chi tiết ấy cho thấy một điều lạnh lùng: trong hậu cung, ai được cứu, ai bị bỏ mặc, phụ thuộc vào thứ bậc hơn là tính mạng.

<short pause> Kaku ghi vào sổ: manh mối một là có thật trong anime. Hai đứa trẻ, cùng thời điểm, trong hai hoàn cảnh chênh lệch.
```

**ElevenLabs**

```text
Để hiểu bí ẩn này, cần hiểu hậu cung trong truyện. Đó là một thành phố thu nhỏ bên trong hoàng cung, với hàng nghìn cung nữ, hoạn quan, và các phi tần của Hoàng đế.

[pause] Đứng đầu là bốn phi tần cấp cao nhất. Mỗi người có cung điện riêng, người hầu riêng, và gia tộc đứng sau. Ai sinh được con trai cho Hoàng đế, người đó và gia tộc của họ có thể thay đổi vận mệnh.

[pause] Ah-Duo từng là một trong bốn người ấy, và là người ở bên Hoàng đế lâu nhất, từ khi ông còn là Thái tử.

[pause] Vì vậy, mỗi đứa trẻ ra đời trong hậu cung không chỉ là một đứa trẻ. Đó là một quân cờ trong ván cờ quyền lực, dù đứa bé chẳng hề biết gì.

[pause] [chuckles] Kaku để ý: trong một nơi mà đứa trẻ là quân cờ, việc đổi hai quân cờ cho nhau có thể là cách duy nhất để bảo vệ chúng.

[pause] Thế giới của Dược sư tự sự là một đất nước hư cấu, nhưng lấy cảm hứng rõ ràng từ các triều đại Trung Hoa thời xưa.

[pause] Trong lịch sử, hậu cung của các hoàng đế Trung Hoa thường có hệ thống cấp bậc phi tần rất chặt, và hoạn quan là những người được phép làm việc bên trong.

[pause] Cuộc tranh giành ngôi thái tử trong lịch sử cũng rất khốc liệt. Vì vậy, nỗi lo về một đứa trẻ bị đánh tráo hay bị hại không phải chuyện hoàn toàn xa lạ với người xưa.

[pause] Kaku nhắc: Kaku không nói Dược sư tự sự dựa trên một sự kiện lịch sử cụ thể nào. Truyện chỉ mượn không khí và luật chơi của hậu cung xưa.

[pause] Manh mối đầu tiên nằm ở quá khứ. Gần hai mươi năm trước, hai người phụ nữ trong cung sinh con gần như cùng lúc.

[pause] Một người là An Thị, khi ấy là phi tần của Hoàng đế trước, sau này là Thái hậu. Người kia là Ah-Duo, phi tần của Thái tử, tức Hoàng đế hiện tại.

[pause] Vì thứ bậc trong cung, An Thị được các thầy thuốc giỏi nhất chăm sóc. Còn Ah-Duo bị bỏ lại, sinh con trong điều kiện thiếu thốn.

[pause] Hậu quả: Ah-Duo không thể có con thêm nữa. Và về sau, cô rời khỏi hậu cung.

[pause] Chi tiết ấy cho thấy một điều lạnh lùng: trong hậu cung, ai được cứu, ai bị bỏ mặc, phụ thuộc vào thứ bậc hơn là tính mạng.

[pause] Kaku ghi vào sổ: manh mối một là có thật trong anime. Hai đứa trẻ, cùng thời điểm, trong hai hoàn cảnh chênh lệch.
```

### c03 · Manh mối 2: mật ong / Manh mối 3: gương mặt và dáng người

Khoảng 117 giây · cảnh s28–s38 · 1517 ký tự

**Gemini**

```text
Theo anime, con của Ah-Duo không sống được lâu. Đứa bé mất khi còn rất nhỏ.

<short pause> Và Maomao, với đầu óc của một dược sư, lần ra nguyên nhân có thể: mật ong. Mật ong nguy hiểm với trẻ sơ sinh.

<short pause> Đây là chi tiết có thật ngoài đời. Các cơ quan y tế khuyên không cho trẻ dưới mười hai tháng tuổi ăn mật ong, vì nguy cơ ngộ độc botulinum ở trẻ nhỏ. Đây là thông tin chung, không phải lời khuyên y tế thay bác sĩ.

<short pause> Nhưng câu hỏi quan trọng là: đứa trẻ đã mất là con của ai? Nếu có ai đó chăm sóc nhầm một đứa bé, trong một đêm hỗn loạn của hoàng cung, mọi thứ có thể đã khác.

<short pause> Với Maomao, một hũ mật ong không chỉ là đồ ngọt. Cùng một thứ, với người lớn là món ăn, với trẻ sơ sinh lại có thể là độc. Đó cũng là tinh thần của cả bộ truyện.

<short pause> <laugh> Kaku để ý: mỗi khi Maomao nhắc tới độc hay mật ong, hãy nhìn nét mặt những cung nữ lớn tuổi trong cảnh. Nhiều người xem cho rằng quá khứ hiện rõ trên mặt họ.

<short pause> Manh mối ba mang tính hình ảnh. Ah-Duo được miêu tả là một người có vẻ đẹp phóng khoáng, cao ráo, đôi khi mặc đồ nam và được so với một chàng trai.

<short pause> Còn Jinshi thì có vẻ đẹp khiến người ta không phân biệt nổi là nam hay nữ. Nhiều người xem để ý rằng hai người có nét gì đó rất giống nhau.

<short pause> Trong khi đó, Jinshi không có nhiều nét giống An Thị, người được cho là mẹ ruột của anh.

<short pause> Cả hai còn có một phong thái giống nhau: điềm tĩnh, hơi xa cách, và rất giỏi che giấu cảm xúc sau một nụ cười.

<short pause> Kaku nhắc: gương mặt là manh mối yếu nhất. Trong truyện hay ngoài đời, con cái không phải lúc nào cũng giống cha mẹ. Kaku chỉ ghi nó vào sổ, không dựa vào nó.
```

**ElevenLabs**

```text
Theo anime, con của Ah-Duo không sống được lâu. Đứa bé mất khi còn rất nhỏ.

[pause] Và Maomao, với đầu óc của một dược sư, lần ra nguyên nhân có thể: mật ong. Mật ong nguy hiểm với trẻ sơ sinh.

[pause] Đây là chi tiết có thật ngoài đời. Các cơ quan y tế khuyên không cho trẻ dưới mười hai tháng tuổi ăn mật ong, vì nguy cơ ngộ độc botulinum ở trẻ nhỏ. Đây là thông tin chung, không phải lời khuyên y tế thay bác sĩ.

[pause] [curious] Nhưng câu hỏi quan trọng là: đứa trẻ đã mất là con của ai? Nếu có ai đó chăm sóc nhầm một đứa bé, trong một đêm hỗn loạn của hoàng cung, mọi thứ có thể đã khác.

[pause] Với Maomao, một hũ mật ong không chỉ là đồ ngọt. Cùng một thứ, với người lớn là món ăn, với trẻ sơ sinh lại có thể là độc. Đó cũng là tinh thần của cả bộ truyện.

[pause] [chuckles] Kaku để ý: mỗi khi Maomao nhắc tới độc hay mật ong, hãy nhìn nét mặt những cung nữ lớn tuổi trong cảnh. Nhiều người xem cho rằng quá khứ hiện rõ trên mặt họ.

[pause] Manh mối ba mang tính hình ảnh. Ah-Duo được miêu tả là một người có vẻ đẹp phóng khoáng, cao ráo, đôi khi mặc đồ nam và được so với một chàng trai.

[pause] Còn Jinshi thì có vẻ đẹp khiến người ta không phân biệt nổi là nam hay nữ. Nhiều người xem để ý rằng hai người có nét gì đó rất giống nhau.

[pause] Trong khi đó, Jinshi không có nhiều nét giống An Thị, người được cho là mẹ ruột của anh.

[pause] Cả hai còn có một phong thái giống nhau: điềm tĩnh, hơi xa cách, và rất giỏi che giấu cảm xúc sau một nụ cười.

[pause] Kaku nhắc: gương mặt là manh mối yếu nhất. Trong truyện hay ngoài đời, con cái không phải lúc nào cũng giống cha mẹ. Kaku chỉ ghi nó vào sổ, không dựa vào nó.
```

### c04 · Manh mối 4: cách người lớn đối xử với Jinshi / Maomao: cô thám tử dược sư / Manh mối 5: vì sao phải giả làm hoạn quan?

Khoảng 127 giây · cảnh s39–s51 · 1654 ký tự

**Gemini**

```text
Manh mối bốn nằm ở hành vi. Thái hậu An Thị, người mẹ chính thức, đối xử với Jinshi khá xa cách. Không lạnh lùng, nhưng cũng không giống một người mẹ với con trai út.

<short pause> Trong khi đó, Hoàng đế đối xử với Jinshi rất thân thiết, đôi khi như một người cha trêu con hơn là một người anh.

<short pause> Và Ah-Duo, khi xuất hiện cùng Jinshi, có một sự dịu dàng khó giải thích, như thể cô biết điều gì đó mà anh không biết.

<short pause> <laugh> Kaku ghi vào sổ: manh mối bốn là cách người lớn nhìn Jinshi. Và thú vị thay, chính Jinshi dường như không hiểu vì sao.

<short pause> Người sẽ giải bí ẩn này, nếu có ai giải được, là Maomao. Cô lớn lên ở khu phố đèn đỏ, được một người cha nuôi làm thầy thuốc dạy về thuốc men.

<short pause> Cô có khứu giác cực nhạy, trí nhớ về thảo dược đáng kinh ngạc, và một niềm đam mê kỳ lạ với độc chất.

<short pause> Cô còn thử độc trên chính cơ thể mình để hiểu chúng. Kaku nhắc rõ: đây là chi tiết hư cấu, tuyệt đối không phải điều nên làm theo.

<short pause> Điều làm Maomao trở thành thám tử giỏi là cô chỉ tin vào bằng chứng. Cô không kết luận khi chưa đủ dữ kiện, và thường chọn không nói ra khi sự thật có thể hại người.

<short pause> Quay lại câu hỏi đầu tiên. Một Hoàng đệ có quyền kế vị, tại sao phải sống dưới vỏ bọc hoạn quan?

<short pause> Một cách hiểu: Jinshi muốn thoát khỏi vị trí người kế vị. Anh muốn Hoàng đế sớm có con trai, để mình không bị cuốn vào cuộc tranh ngôi.

<short pause> Vỏ bọc hoạn quan giúp anh vào hậu cung, quan sát các phi tần, và âm thầm bảo vệ những người có thể sinh ra người nối ngôi.

<short pause> Anh cũng dùng chính vẻ đẹp của mình như một công cụ, để người khác mất cảnh giác và nói nhiều hơn họ định.

<short pause> Nhưng nếu Jinshi là con ruột của Hoàng đế, thì vị trí của anh còn nhạy cảm hơn nhiều. Anh không chỉ là em trai. Anh có thể là con trai trưởng.
```

**ElevenLabs**

```text
Manh mối bốn nằm ở hành vi. Thái hậu An Thị, người mẹ chính thức, đối xử với Jinshi khá xa cách. Không lạnh lùng, nhưng cũng không giống một người mẹ với con trai út.

[pause] Trong khi đó, Hoàng đế đối xử với Jinshi rất thân thiết, đôi khi như một người cha trêu con hơn là một người anh.

[pause] Và Ah-Duo, khi xuất hiện cùng Jinshi, có một sự dịu dàng khó giải thích, như thể cô biết điều gì đó mà anh không biết.

[pause] [chuckles] Kaku ghi vào sổ: manh mối bốn là cách người lớn nhìn Jinshi. Và thú vị thay, chính Jinshi dường như không hiểu vì sao.

[pause] Người sẽ giải bí ẩn này, nếu có ai giải được, là Maomao. Cô lớn lên ở khu phố đèn đỏ, được một người cha nuôi làm thầy thuốc dạy về thuốc men.

[pause] Cô có khứu giác cực nhạy, trí nhớ về thảo dược đáng kinh ngạc, và một niềm đam mê kỳ lạ với độc chất.

[pause] Cô còn thử độc trên chính cơ thể mình để hiểu chúng. Kaku nhắc rõ: đây là chi tiết hư cấu, tuyệt đối không phải điều nên làm theo.

[pause] Điều làm Maomao trở thành thám tử giỏi là cô chỉ tin vào bằng chứng. Cô không kết luận khi chưa đủ dữ kiện, và thường chọn không nói ra khi sự thật có thể hại người.

[pause] Quay lại câu hỏi đầu tiên. [curious] Một Hoàng đệ có quyền kế vị, tại sao phải sống dưới vỏ bọc hoạn quan?

[pause] Một cách hiểu: Jinshi muốn thoát khỏi vị trí người kế vị. Anh muốn Hoàng đế sớm có con trai, để mình không bị cuốn vào cuộc tranh ngôi.

[pause] Vỏ bọc hoạn quan giúp anh vào hậu cung, quan sát các phi tần, và âm thầm bảo vệ những người có thể sinh ra người nối ngôi.

[pause] Anh cũng dùng chính vẻ đẹp của mình như một công cụ, để người khác mất cảnh giác và nói nhiều hơn họ định.

[pause] Nhưng nếu Jinshi là con ruột của Hoàng đế, thì vị trí của anh còn nhạy cảm hơn nhiều. Anh không chỉ là em trai. Anh có thể là con trai trưởng.
```

### c05 · Giả thuyết: hai đứa trẻ bị hoán đổi / Những khả năng khác / Phản biện

Khoảng 143 giây · cảnh s52–s66 · 1856 ký tự

**Gemini**

```text
LÝ THUYẾT. Gom năm manh mối lại, ta có giả thuyết phổ biến nhất: đêm ấy, hai đứa trẻ đã bị hoán đổi.

<short pause> Theo giả thuyết này, đứa bé khỏe mạnh của Ah-Duo được đưa sang làm con của An Thị. Đứa bé ấy chính là Jinshi.

<short pause> Còn đứa con của An Thị, được Ah-Duo nuôi như con mình, và chính đứa bé ấy đã mất khi còn nhỏ.

<short pause> Nếu đúng, thì Jinshi là con ruột của Hoàng đế hiện tại và Ah-Duo. Người anh anh vẫn gọi, thật ra là cha anh.

<short pause> <laugh> Kaku nhắc lại: đây là LÝ THUYẾT dựa trên manh mối trong anime. Kaku chưa khẳng định. Phần tiếp theo, Kaku sẽ tự phản biện nó.

<short pause> Trước khi phản biện, Kaku liệt kê những khả năng khác về mặt logic, để giả thuyết hoán đổi không phải lựa chọn duy nhất.

<short pause> LÝ THUYẾT A: Jinshi đúng là con của Hoàng đế trước và An Thị, và mọi manh mối chỉ là sự trùng hợp. Đây là cách đọc đơn giản nhất.

<short pause> LÝ THUYẾT B: có hoán đổi, nhưng không ai trong hai người mẹ chủ động làm. Đó là một sự nhầm lẫn trong đêm hỗn loạn, và người ta chọn im lặng.

<short pause> LÝ THUYẾT C: hoán đổi có chủ đích, do hai người mẹ đồng ý với nhau. Đây là giả thuyết khớp nhất, và là giả thuyết Kaku đặt lên bàn phản biện.

<short pause> Phản biện một: hoán đổi con trong hoàng cung là tội cực nặng. Ai dám làm, và làm sao giữ bí mật suốt gần hai mươi năm?

<short pause> Trả lời thử: chỉ cần hai người mẹ đồng ý, và vài cung nữ trung thành. Mà theo anime, đêm ấy cả hoàng cung đang dồn mọi sự chú ý vào một phía.

<short pause> Phản biện hai: vì sao An Thị lại đồng ý? Một người mẹ có thể đổi con mình lấy con người khác sao?

<short pause> Đây là chỗ các tóm tắt từ tiểu thuyết cho thấy câu chuyện của An Thị rất đau lòng, với những hoàn cảnh cô không được chọn. Kaku sẽ không kể chi tiết.

<short pause> Phản biện ba: nếu mọi thứ chỉ là gương mặt và thái độ, thì có thể Jinshi đơn giản là em trai Hoàng đế, và mọi người chỉ có lý do riêng để đối xử với anh như vậy.

<short pause> Kaku để ý: đây là điểm yếu thật của giả thuyết. Phần lớn manh mối là gián tiếp. Chỉ riêng manh mối mật ong là có cơ sở vững.
```

**ElevenLabs**

```text
LÝ THUYẾT. Gom năm manh mối lại, ta có giả thuyết phổ biến nhất: đêm ấy, hai đứa trẻ đã bị hoán đổi.

[pause] Theo giả thuyết này, đứa bé khỏe mạnh của Ah-Duo được đưa sang làm con của An Thị. Đứa bé ấy chính là Jinshi.

[pause] Còn đứa con của An Thị, được Ah-Duo nuôi như con mình, và chính đứa bé ấy đã mất khi còn nhỏ.

[pause] Nếu đúng, thì Jinshi là con ruột của Hoàng đế hiện tại và Ah-Duo. Người anh anh vẫn gọi, thật ra là cha anh.

[pause] [chuckles] Kaku nhắc lại: đây là LÝ THUYẾT dựa trên manh mối trong anime. Kaku chưa khẳng định. Phần tiếp theo, Kaku sẽ tự phản biện nó.

[pause] Trước khi phản biện, Kaku liệt kê những khả năng khác về mặt logic, để giả thuyết hoán đổi không phải lựa chọn duy nhất.

[pause] LÝ THUYẾT A: Jinshi đúng là con của Hoàng đế trước và An Thị, và mọi manh mối chỉ là sự trùng hợp. Đây là cách đọc đơn giản nhất.

[pause] LÝ THUYẾT B: có hoán đổi, nhưng không ai trong hai người mẹ chủ động làm. Đó là một sự nhầm lẫn trong đêm hỗn loạn, và người ta chọn im lặng.

[pause] LÝ THUYẾT C: hoán đổi có chủ đích, do hai người mẹ đồng ý với nhau. Đây là giả thuyết khớp nhất, và là giả thuyết Kaku đặt lên bàn phản biện.

[pause] Phản biện một: hoán đổi con trong hoàng cung là tội cực nặng. [curious] Ai dám làm, và làm sao giữ bí mật suốt gần hai mươi năm?

[pause] Trả lời thử: chỉ cần hai người mẹ đồng ý, và vài cung nữ trung thành. Mà theo anime, đêm ấy cả hoàng cung đang dồn mọi sự chú ý vào một phía.

[pause] Phản biện hai: vì sao An Thị lại đồng ý? Một người mẹ có thể đổi con mình lấy con người khác sao?

[pause] Đây là chỗ các tóm tắt từ tiểu thuyết cho thấy câu chuyện của An Thị rất đau lòng, với những hoàn cảnh cô không được chọn. Kaku sẽ không kể chi tiết.

[pause] Phản biện ba: nếu mọi thứ chỉ là gương mặt và thái độ, thì có thể Jinshi đơn giản là em trai Hoàng đế, và mọi người chỉ có lý do riêng để đối xử với anh như vậy.

[pause] Kaku để ý: đây là điểm yếu thật của giả thuyết. Phần lớn manh mối là gián tiếp. Chỉ riêng manh mối mật ong là có cơ sở vững.
```

### c06 · Vùng spoiler tiểu thuyết / Điều này thay đổi gì? / Bảng manh mối tổng kết

Khoảng 139 giây · cảnh s67–s79 · 1805 ký tự

**Gemini**

```text
Từ đây là vùng spoiler tiểu thuyết. Nếu bạn chỉ muốn xem anime, hãy tua tới chương tiếp theo, khi thấy chữ Hết vùng spoiler.

<short pause> Theo nhiều trang tổng hợp về bộ truyện, tiểu thuyết gốc đã xác nhận giả thuyết hoán đổi: Jinshi là con ruột của Hoàng đế và Ah-Duo.

<short pause> Và theo các tóm tắt ấy, chính Jinshi không được cho biết sự thật từ nhỏ. Thân phận thật trở thành gánh nặng mà anh phải tự đối diện.

<short pause> <laugh> Kaku vẫn giữ nhãn lý thuyết cho người chỉ xem anime, vì anime có thể kể theo cách riêng. Hết vùng spoiler.

<short pause> Nếu Jinshi là con của Hoàng đế, cuộc tranh ngôi trong hoàng cung trở nên nguy hiểm hơn nhiều. Mỗi đứa trẻ ra đời trong hậu cung đều liên quan tới vị trí của anh.

<short pause> Nó cũng giải thích vì sao Jinshi quá quan tâm tới sự an toàn của các phi tần và những đứa trẻ. Có thể anh hiểu, sâu trong lòng, rằng một đứa trẻ trong cung mong manh tới mức nào.

<short pause> Và nó làm mối quan hệ giữa Jinshi và Maomao phức tạp hơn. Maomao muốn một cuộc sống bình thường với thảo dược và thuốc men. Còn Jinshi, càng gần ngai vàng, càng khó có một cuộc sống bình thường.

<short pause> Còn với Hoàng đế, nếu giả thuyết đúng, việc giữ im lặng cũng là một cách bảo vệ con mình khỏi những kẻ muốn lợi dụng thân phận ấy.

<short pause> Kaku để ý: Maomao là người giỏi nhất cung trong việc tìm sự thật. <short pause> Nhưng với sự thật này, cô có vẻ chọn không hỏi thêm. Có những sự thật, biết rồi là không quay lại được.

<short pause> Tổng kết bằng một trang. Manh mối một: hai đứa trẻ cùng ra đời, trong hai hoàn cảnh chênh lệch. Độ tin cậy: cao, vì anime kể rõ.

<short pause> Manh mối hai: mật ong và đứa trẻ đã mất. Độ tin cậy: cao. Manh mối ba: gương mặt. Độ tin cậy: thấp.

<short pause> Manh mối bốn: thái độ của người lớn. Độ tin cậy: trung bình. Manh mối năm: vỏ bọc hoạn quan. Độ tin cậy: trung bình.

<short pause> Kết luận của Kaku: giả thuyết hoán đổi là cách giải thích khớp nhất với mọi manh mối. <short pause> Nhưng với người chỉ xem anime, nó vẫn là LÝ THUYẾT.
```

**ElevenLabs**

```text
Từ đây là vùng spoiler tiểu thuyết. Nếu bạn chỉ muốn xem anime, hãy tua tới chương tiếp theo, khi thấy chữ Hết vùng spoiler.

[pause] Theo nhiều trang tổng hợp về bộ truyện, tiểu thuyết gốc đã xác nhận giả thuyết hoán đổi: Jinshi là con ruột của Hoàng đế và Ah-Duo.

[pause] Và theo các tóm tắt ấy, chính Jinshi không được cho biết sự thật từ nhỏ. Thân phận thật trở thành gánh nặng mà anh phải tự đối diện.

[pause] [chuckles] Kaku vẫn giữ nhãn lý thuyết cho người chỉ xem anime, vì anime có thể kể theo cách riêng. Hết vùng spoiler.

[pause] Nếu Jinshi là con của Hoàng đế, cuộc tranh ngôi trong hoàng cung trở nên nguy hiểm hơn nhiều. Mỗi đứa trẻ ra đời trong hậu cung đều liên quan tới vị trí của anh.

[pause] Nó cũng giải thích vì sao Jinshi quá quan tâm tới sự an toàn của các phi tần và những đứa trẻ. Có thể anh hiểu, sâu trong lòng, rằng một đứa trẻ trong cung mong manh tới mức nào.

[pause] Và nó làm mối quan hệ giữa Jinshi và Maomao phức tạp hơn. Maomao muốn một cuộc sống bình thường với thảo dược và thuốc men. Còn Jinshi, càng gần ngai vàng, càng khó có một cuộc sống bình thường.

[pause] Còn với Hoàng đế, nếu giả thuyết đúng, việc giữ im lặng cũng là một cách bảo vệ con mình khỏi những kẻ muốn lợi dụng thân phận ấy.

[pause] Kaku để ý: Maomao là người giỏi nhất cung trong việc tìm sự thật. [pause] Nhưng với sự thật này, cô có vẻ chọn không hỏi thêm. Có những sự thật, biết rồi là không quay lại được.

[pause] Tổng kết bằng một trang. Manh mối một: hai đứa trẻ cùng ra đời, trong hai hoàn cảnh chênh lệch. Độ tin cậy: cao, vì anime kể rõ.

[pause] Manh mối hai: mật ong và đứa trẻ đã mất. Độ tin cậy: cao. Manh mối ba: gương mặt. Độ tin cậy: thấp.

[pause] Manh mối bốn: thái độ của người lớn. Độ tin cậy: trung bình. Manh mối năm: vỏ bọc hoạn quan. Độ tin cậy: trung bình.

[pause] Kết luận của Kaku: giả thuyết hoán đổi là cách giải thích khớp nhất với mọi manh mối. [pause] Nhưng với người chỉ xem anime, nó vẫn là LÝ THUYẾT.
```

### c07 · Câu hỏi mở cho bạn / Kết

Khoảng 77 giây · cảnh s80–s86 · 1007 ký tự

**Gemini**

```text
Giờ tới lượt bạn. Nếu bạn là Jinshi và biết được sự thật, bạn sẽ làm gì? Giữ im lặng để bảo vệ mọi người, hay đòi lại vị trí của mình?

<short pause> Và nếu bạn là Maomao, bạn có hỏi thẳng Jinshi không? Hay chọn giả vờ không biết?

<short pause> Hãy viết câu trả lời vào bình luận. <laugh> Kaku muốn đọc xem ai là người chọn sự thật, và ai là người chọn sự bình yên.

<short pause> Một hoạn quan không phải hoạn quan. Một người em có thể là con. Và một hũ mật ong nhỏ giữ bí mật của cả hoàng cung. Dược sư tự sự là câu chuyện mà mỗi chi tiết nhỏ đều có thể là một liều thuốc, hoặc một liều độc.

<short pause> Khi phần hai của mùa ba lên sóng vào tháng tư, hãy xem lại những cảnh có Ah-Duo và Thái hậu. Bạn sẽ thấy nhiều ánh mắt mang nghĩa khác đi.

<short pause> Video tiếp theo, Kaku đặt ba hệ kiếm thuật lên cùng một bàn: Hơi thở của Kimetsu, kiếm Haki của One Piece, và yêu đao của Kagurabachi. Hệ nào mạnh nhất?

<short pause> Nếu bạn thích những cuộc điều tra có gắn nhãn rõ ràng, hãy đăng ký kênh. Và nhớ: đừng cho trẻ nhỏ ăn mật ong, kể cả khi bạn không ở trong hoàng cung. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ tới lượt bạn. [curious] Nếu bạn là Jinshi và biết được sự thật, bạn sẽ làm gì? Giữ im lặng để bảo vệ mọi người, hay đòi lại vị trí của mình?

[pause] Và nếu bạn là Maomao, bạn có hỏi thẳng Jinshi không? Hay chọn giả vờ không biết?

[pause] Hãy viết câu trả lời vào bình luận. [chuckles] Kaku muốn đọc xem ai là người chọn sự thật, và ai là người chọn sự bình yên.

[pause] Một hoạn quan không phải hoạn quan. Một người em có thể là con. Và một hũ mật ong nhỏ giữ bí mật của cả hoàng cung. Dược sư tự sự là câu chuyện mà mỗi chi tiết nhỏ đều có thể là một liều thuốc, hoặc một liều độc.

[pause] Khi phần hai của mùa ba lên sóng vào tháng tư, hãy xem lại những cảnh có Ah-Duo và Thái hậu. Bạn sẽ thấy nhiều ánh mắt mang nghĩa khác đi.

[pause] Video tiếp theo, Kaku đặt ba hệ kiếm thuật lên cùng một bàn: Hơi thở của Kimetsu, kiếm Haki của One Piece, và yêu đao của Kagurabachi. Hệ nào mạnh nhất?

[pause] Nếu bạn thích những cuộc điều tra có gắn nhãn rõ ràng, hãy đăng ký kênh. Và nhớ: đừng cho trẻ nhỏ ăn mật ong, kể cả khi bạn không ở trong hoàng cung. Kaku gấp sổ đây, hẹn gặp lại!
```
