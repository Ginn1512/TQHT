# Bộ prompt · Attack on Titan: 9 chi tiết cài cắm có từ tập đầu tiên

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (84 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo cực mạnh: video có spoiler toàn bộ Attack on Titan, kể cả cái kết. Nếu chưa xem hết, hãy dừng ở đây.…

```text
Wide 16:9 landscape cinematic frame. a massive stone wall under a stormy sky, a single warning sign nailed to it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Có những bộ truyện viết tới đâu nghĩ tới đó. Và có những bộ mà câu trả lời cuối cùng đã nằm sẵn ở ngay trang…

```text
Wide 16:9 landscape cinematic frame. the very first page of an old book glowing faintly, tiny details highlighted in gold. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Attack on Titan là bộ thứ hai. Rất nhiều chi tiết ở tập một, chương một, tưởng như vô nghĩa, hóa ra là chìa k…

```text
Wide 16:9 landscape cinematic frame. a key hidden in the corner of a first-page illustration, glinting. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hôm nay Kaku sẽ đặt từng chi tiết cạnh nhau: bên trái là lần đầu nó xuất hiện, bên phải là ý nghĩa thật của n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning two photographs side by side on a board labeled BEFORE and AFTER. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Có chín chi tiết chính, thêm vài món tặng kèm, và Kaku để dành chi tiết khiến Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook with nine numbered bookmarks sticking out. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Một bộ truyện được lên kế hoạch

Lời: Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Bản anime kéo dài từ 2013 tới tận năm…

```text
Wide 16:9 landscape cinematic frame. a long shelf of manga volumes ending in a final volume with a small bird on the spine. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Câu chuyện bắt đầu rất đơn giản: loài người sống sau những bức tường cao năm mươi mét để trốn những người khổ…

```text
Wide 16:9 landscape cinematic frame. a walled city seen from above, towering walls in concentric rings, giant silhouettes outside. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhưng càng đi, câu chuyện càng lật ngược: titan là gì, ai xây tường, bên ngoài tường có gì. Mỗi câu trả lời l…

```text
Wide 16:9 landscape cinematic frame. a map that keeps unfolding outward, revealing larger and larger worlds beyond the walls. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Điều làm fan kinh ngạc là nhiều câu trả lời đó được cài sẵn từ những chương đầu tiên. Đó là lý do bộ này được…

```text
Wide 16:9 landscape cinematic frame. a reader flipping back to the first chapter with a shocked expression, notes scattered around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Tác giả từng chia sẻ trong các buổi phỏng vấn rằng ông đã hình dung những nét chính của cái kết từ khá sớm, d…

```text
Wide 16:9 landscape cinematic frame. a gardener planting seeds in the first row of a long field, tall trees already visible at the far end. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: xem lại Attack on Titan giống như xem một bộ khác hoàn toàn. Bạn sẽ thấy nhân vật nói những câu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing two pairs of glasses stacked, reading intensely. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Chi tiết 1: Chìa khóa trên cổ

Lời: Lần đầu xuất hiện: ở tập đầu tiên, cha của Eren đưa cho cậu một chiếc chìa khóa, và dặn một ngày nào đó hãy x…

```text
Wide 16:9 landscape cinematic frame. a small old key on a string hanging around a boy's neck, glinting in candlelight. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Suốt ba mùa anime, chiếc chìa khóa ấy luôn ở trên cổ Eren. Tầng hầm trở thành mục tiêu của cả đoàn trinh sát.…

```text
Wide 16:9 landscape cinematic frame. a boy clutching the key at his chest while soldiers on horseback ride toward a distant ruined town. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Ý nghĩa về sau: tầng hầm không chứa vũ khí hay cách tiêu diệt titan. Nó chứa những cuốn sổ và một tấm ảnh chụ…

```text
Wide 16:9 landscape cinematic frame. an open drawer in a dusty basement revealing old journals and a photograph. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và thế giới đó coi những người trong tường là kẻ thù. Chiếc chìa khóa nhỏ mở ra một cánh cửa lớn hơn nhiều so…

```text
Wide 16:9 landscape cinematic frame. a small key turning in a lock as a huge world map unfolds behind the door. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Trong những cuốn sổ đó, người cha còn viết về quá khứ của mình, về một gia đình, một đứa con khác và một thế…

```text
Wide 16:9 landscape cinematic frame. an open journal with handwritten pages and a small faded family photo tucked inside. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một chiếc chìa khóa được giữ suốt nhiều năm để mở ra một sự thật không ai muốn nghe. Đây là cài…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny key up to the light, eyes wide. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Chi tiết 2: Titan không cần ăn

Lời: Lần đầu xuất hiện: ở mùa một, một nhà nghiên cứu phát hiện titan không có cơ quan tiêu hóa. Chúng ăn người, n…

```text
Wide 16:9 landscape cinematic frame. a scientist's sketch of a giant's anatomy with the digestive system crossed out, notes in the margin. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Chúng không cần ăn để sống. Chúng cũng không tấn công động vật, chỉ nhắm vào con người. Lần đầu xem, đây giốn…

```text
Wide 16:9 landscape cinematic frame. a giant ignoring a herd of deer to stare at a distant human village. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Ý nghĩa về sau: titan vốn là con người. Họ bị biến thành titan không có ý thức, và bản năng khiến họ tìm tới…

```text
Wide 16:9 landscape cinematic frame. a human silhouette slowly morphing into a giant's silhouette, an empty expression on its face. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Chi tiết này khiến mọi trận đánh trước đó trở nên nặng nề hơn. Những con quái vật mà các nhân vật chém hạ từn…

```text
Wide 16:9 landscape cinematic frame. a battlefield at dusk with steam rising from fallen giants, a soldier looking down in silence. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cài cắm hay nhất không phải lúc nào cũng là lời thoại. Đôi khi nó nằm trong một chi tiết sinh h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering at a textbook diagram through a magnifying glass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Chi tiết 3: Khuôn mặt trong bức tường

Lời: Lần đầu xuất hiện: cuối mùa một, sau một trận đánh làm vỡ một phần bức tường, lộ ra bên trong là khuôn mặt củ…

```text
Wide 16:9 landscape cinematic frame. a crack in a massive stone wall revealing a giant eye staring out from within. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Một vị mục sư biết rõ bí mật này, và hoảng loạn yêu cầu phải che nó lại khỏi ánh mặt trời. Người xem lúc đó c…

```text
Wide 16:9 landscape cinematic frame. a panicked robed figure shouting at soldiers to cover a crack in the wall with cloth. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Ý nghĩa về sau: những bức tường được tạo thành từ vô số titan khổng lồ đứng sát cạnh nhau, cứng hóa lại. Thứ…

```text
Wide 16:9 landscape cinematic frame. a cross-section of a wall showing countless colossal figures standing shoulder to shoulder inside. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Ở cuối truyện, những titan trong tường được đánh thức và bước ra, tạo nên một thảm họa có tên là Địa Minh. Cả…

```text
Wide 16:9 landscape cinematic frame. a horizon of colossal silhouettes marching across the land, dust clouds rising to the sky. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bức tường là biểu tượng của sự an toàn trong mùa một, và là biểu tượng của sự hủy diệt ở mùa cu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding behind a small wall that suddenly opens one eye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Chi tiết 4: Titan nằm trên mái nhà

Lời: Lần đầu xuất hiện: ở mùa hai, một người lính trẻ về thăm làng quê của mình và thấy một titan nằm ngửa trên nó…

```text
Wide 16:9 landscape cinematic frame. a small village house crushed under a giant lying face up on its roof. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Titan đó nhìn cậu và thều thào một câu nghe như lời chào đón về nhà. Ngôi làng không có một vết máu nào, nhưn…

```text
Wide 16:9 landscape cinematic frame. an empty village with no destruction, doors left open, laundry still hanging. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Ý nghĩa về sau: dân làng không bị ăn thịt. Chính họ đã bị biến thành titan. Và titan trên mái nhà là mẹ của c…

```text
Wide 16:9 landscape cinematic frame. a mother's silhouette overlapped with the giant's silhouette on the rooftop. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Đây là lần đầu truyện gần như nói thẳng rằng titan là con người, sớm hơn nhiều so với lời giải thích chính th…

```text
Wide 16:9 landscape cinematic frame. a single tear sliding down the face of a giant lying still under the moon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chi tiết này nhỏ, nhưng là một trong những khoảnh khắc buồn nhất cả bộ. Nó biến nỗi sợ thành nỗ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small candle in silence. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Chi tiết 5: Titan mỉm cười

Lời: Lần đầu xuất hiện: tập một, titan ăn thịt mẹ của Eren có gương mặt mỉm cười, trông gần như hiền lành. Đó là h…

```text
Wide 16:9 landscape cinematic frame. a smiling giant's silhouette looming over a collapsed house, dust in the air. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Ở mùa ba, ta biết titan đó từng là vợ trước của cha Eren. Một người phụ nữ bị biến thành titan và thả vào tro…

```text
Wide 16:9 landscape cinematic frame. a faded photograph of a woman with a gentle smile, the same smile echoed in a giant's face. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và ở mùa cuối, một sự thật còn đáng sợ hơn được hé lộ: hướng đi của titan đó hôm ấy có liên quan tới chính sứ…

```text
Wide 16:9 landscape cinematic frame. a looping arrow drawn from an adult's silhouette back to a childhood scene of a destroyed house. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Nói cách khác, Eren đã chứng kiến bi kịch lớn nhất đời mình, và bi kịch ấy lại gắn với chính cậu. Đây là lúc…

```text
Wide 16:9 landscape cinematic frame. a circular path of footprints that ends where it began, a single house in the middle. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Kaku vẫn chưa hết rùng mình mỗi khi nghĩ lại chi tiết này.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wrapped tightly in its scarf, shivering. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Chi tiết 6: Cuộc trò chuyện về quê nhà

Lời: Lần đầu xuất hiện: ở mùa một và mùa hai, hai học viên thân thiết thỉnh thoảng nhắc về việc trở về quê nhà, nh…

```text
Wide 16:9 landscape cinematic frame. two young soldiers sitting on a wall at night, looking toward the distant horizon. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Một người trong số họ luôn đóng vai người anh cả đáng tin cậy, chăm sóc mọi người trong nhóm. Không ai nghi n…

```text
Wide 16:9 landscape cinematic frame. a tall reliable young man helping a fellow trainee up after a fall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Ý nghĩa về sau: quê nhà của họ ở bên ngoài tường. Họ là chiến binh được gửi tới để lấy sức mạnh của titan thủ…

```text
Wide 16:9 landscape cinematic frame. two silhouettes standing on a wall revealed as giant shadows loom behind them. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Lần xem lại, mỗi lần họ nhắc về quê nhà, về nhiệm vụ, về việc phải trở về, đều mang một nghĩa hoàn toàn khác.

```text
Wide 16:9 landscape cinematic frame. a replayed memory with subtitles changing meaning, highlighted words glowing. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Thậm chí có lúc, một trong hai người thú nhận thẳng thân phận của mình giữa một cuộc trò chuyện bình thường,…

```text
Wide 16:9 landscape cinematic frame. two soldiers talking casually on a wall in daylight while a third listens in stunned silence. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: tác giả để những nhân vật này nói gần như sự thật ngay trước mặt khán giả. Chính vì quá thật nê…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a speech bubble with a hidden meaning in invisible ink. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Chi tiết 7: Giấc mơ về biển

Lời: Lần đầu xuất hiện: từ những tập đầu, Armin kể cho Eren nghe về đại dương, một vùng nước mặn mênh mông mà sách…

```text
Wide 16:9 landscape cinematic frame. two boys reading a forbidden book under a tree, an illustration of a vast ocean on its pages. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Suốt nhiều mùa, biển là biểu tượng của tự do, của thế giới rộng lớn bên ngoài bức tường.

```text
Wide 16:9 landscape cinematic frame. a wall with a painted ocean on its inner side, children looking at it with longing. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Ý nghĩa về sau: khi đến được biển, họ nhận ra bên kia đại dương là những người coi họ là kẻ thù. Biển không p…

```text
Wide 16:9 landscape cinematic frame. a group of young soldiers standing on a beach, one pointing across the water at an unseen enemy. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Câu hỏi của Eren khi đứng trước biển gần như là câu hỏi của cả bộ truyện: nếu giết hết kẻ thù bên kia biển, l…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing at the water's edge, looking out, waves touching his boots. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là cài cắm đau lòng nhất. Giấc mơ tuổi thơ đẹp nhất trở thành nơi giấc mơ tan vỡ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a seashell to its ear, looking sad. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Chi tiết 8: Những cánh chim

Lời: Lần đầu xuất hiện: ngay từ những cảnh đầu tiên, Eren nhìn lên những đàn chim bay qua bức tường. Biểu tượng củ…

```text
Wide 16:9 landscape cinematic frame. a boy on a riverbank looking up at birds flying over a towering wall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Với Eren, chim là tự do: chúng bay qua tường mà không cần xin phép ai. Cậu muốn được như chúng.

```text
Wide 16:9 landscape cinematic frame. a flock of birds soaring freely above a walled city at sunset. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Ý nghĩa về sau: ở cảnh cuối cùng của truyện, một chú chim xuất hiện bên cạnh người đã luôn ở bên Eren, và quấ…

```text
Wide 16:9 landscape cinematic frame. a small bird gently tugging a red scarf around someone's neck on a quiet hill. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nhiều người hiểu chú chim đó như hình ảnh của Eren, cuối cùng được tự do. Truyện để người đọc tự cảm nhận.

```text
Wide 16:9 landscape cinematic frame. a single bird flying away from a large tree into an open sky. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chữ tự do được nhắc tới rất nhiều lần trong truyện, nhưng nó được nói rõ nhất bằng một hình ảnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot watching a bird fly away, a small smile on its face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Những câu thoại đổi nghĩa khi xem lại

Lời: Không chỉ đồ vật và hình ảnh, cả lời thoại trong Attack on Titan cũng đổi nghĩa hoàn toàn khi xem lại.

```text
Wide 16:9 landscape cinematic frame. an old script page with certain lines glowing red after being reread. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Ở tập một, sau khi mất mẹ, cậu bé Eren hét lên rằng sẽ tiêu diệt hết bọn chúng, không chừa một con nào. Lần đ…

```text
Wide 16:9 landscape cinematic frame. a boy screaming with clenched fists on a ruined street, smoke rising behind him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Xem lại sau khi biết cái kết, câu nói ấy nghe hoàn toàn khác. Vì về sau, thứ Eren muốn tiêu diệt không còn là…

```text
Wide 16:9 landscape cinematic frame. the same boy's shadow stretching across a map of the entire world. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Một câu khác của Armin: người không thể hy sinh bất cứ điều gì thì không thể thay đổi được gì. Lúc đầu nghe n…

```text
Wide 16:9 landscape cinematic frame. a young strategist looking at a chessboard where every piece has a human face. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Kaku khuyên bạn xem lại tập một sau khi xem hết. Gần như câu nào cũng có tầng nghĩa thứ hai.

```text
Wide 16:9 landscape cinematic frame. the owl mascot rewinding a tiny film reel with a knowing look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Chi tiết tặng kèm: Cơn đau đầu

Lời: Chi tiết tặng kèm trước khi tới chi tiết cuối. Lần đầu xuất hiện: nhiều lần trong truyện, Mikasa bỗng ôm đầu…

```text
Wide 16:9 landscape cinematic frame. a young woman clutching her head in pain on a battlefield, a faint glow behind her eyes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Lần đầu xem, người ta nghĩ đó là di chứng từ chấn thương, hoặc chỉ là cách thể hiện căng thẳng. Không ai để ý…

```text
Wide 16:9 landscape cinematic frame. a medical chart with question marks next to a small head icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ý nghĩa về sau: cái kết gợi ý rằng những cơn đau đó liên quan tới cô gái đầu tiên có sức mạnh titan, người đã…

```text
Wide 16:9 landscape cinematic frame. a ghostly girl silhouette standing far behind a young woman, watching silently. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và lựa chọn cuối cùng của Mikasa được xem là chìa khóa để giải thoát cô gái ấy khỏi hai nghìn năm ràng buộc.…

```text
Wide 16:9 landscape cinematic frame. chains dissolving around a ghostly girl as a single tear falls from her eye. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là chi tiết mà rất nhiều người chỉ nhận ra sau khi đọc chương cuối. Kaku cũng vậy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot rubbing its head with a sheepish smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Cách nhận ra một chi tiết cài cắm

Lời: Trước chi tiết cuối cùng, Kaku chia sẻ cách tự nhận ra cài cắm khi xem bất kỳ bộ truyện nào.

```text
Wide 16:9 landscape cinematic frame. a checklist on a notepad with three items and a magnifying glass beside it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Một: để ý những chi tiết được nhắc lại mà không có lý do rõ ràng. Một đồ vật, một câu nói, một hình ảnh lặp l…

```text
Wide 16:9 landscape cinematic frame. a recurring symbol appearing in three different scenes, circled in red. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Hai: để ý những câu trả lời quá hoàn hảo hoặc quá mơ hồ. Khi nhân vật nói một câu mà bạn thấy hơi lạ, hãy ghi…

```text
Wide 16:9 landscape cinematic frame. a speech bubble with a strange sentence highlighted, a sticky note attached. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Ba: để ý tên chương hay tên tập. Tác giả thường giấu manh mối ở những chỗ ít người đọc kỹ nhất.

```text
Wide 16:9 landscape cinematic frame. a table of contents with one chapter title glowing faintly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và chi tiết cuối cùng của Kaku hôm nay chính là một tên chương.

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping on a chapter title with its wing, eyebrows raised. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Chi tiết 9: Gửi em, hai nghìn năm sau

Lời: Lần đầu xuất hiện: tên của chương một, cũng là tên tập một của anime, là Gửi em, hai nghìn năm sau. Một cái t…

```text
Wide 16:9 landscape cinematic frame. a title card on old paper reading like a letter, with a faint number 2000 watermarked. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và ở trang đầu tiên của chương một, có một cảnh rất lạ: một cô gái nói với Eren câu tạm biệt, hẹn gặp lại, tr…

```text
Wide 16:9 landscape cinematic frame. a boy waking up under a large tree with tears on his cheeks, a girl looking at him with concern. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Ý nghĩa về sau: gần cuối truyện có một chương mang tên đối xứng hoàn hảo: Từ em, hai nghìn năm trước. Chương…

```text
Wide 16:9 landscape cinematic frame. two title cards side by side, mirrored, one reading TO and the other reading FROM. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Còn cảnh ở trang đầu tiên, cô gái nói lời tạm biệt, hóa ra là một cảnh từ tương lai, gần với cái kết của cả c…

```text
Wide 16:9 landscape cinematic frame. a looping ribbon connecting the first page of a book to its last page. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nghĩa là ngay từ trang đầu tiên, câu chuyện đã được viết như một vòng tròn. Hai nghìn năm lịch sử, mười hai n…

```text
Wide 16:9 landscape cinematic frame. a vast circle drawn across a timeline of two thousand years, both ends meeting under a tree. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là chi tiết khiến Kaku nổi da gà nhất. Lần đầu đọc, bạn không thể hiểu. Lần cuối đọc, bạn k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a letter to its chest, eyes closed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Góc nhìn của Kaku: vòng lặp và tự do · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao Isayama lại cài cắm nhiều đến vậy? Kaku nghĩ nó gắn chặt với chủ đề của bộ truyện.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a wall at dusk, looking at a circle drawn in the sky. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Attack on Titan nói về tự do. Nhưng nhân vật chính càng chạy tới tự do, càng như bị cuốn vào một vòng lặp đã…

```text
Wide 16:9 landscape cinematic frame. a runner sprinting along a path that curves back into itself, birds flying overhead. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Những chi tiết cài cắm chính là bằng chứng của vòng lặp đó: mọi thứ ở cuối đã có mặt ở đầu. Câu chuyện không…

```text
Wide 16:9 landscape cinematic frame. the first and last pages of a book stitched together into a ring. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Và vì vậy, câu hỏi mà bộ truyện để lại cho người xem là: tự do thật sự là gì, nếu ta không thể thay đổi những…

```text
Wide 16:9 landscape cinematic frame. a single bird sitting on top of a broken wall, looking at the open sky. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Có người thấy cái kết đẹp, có người thấy nó gây tranh cãi. Nhưng gần như ai cũng đồng ý rằng những cài cắm từ…

```text
Wide 16:9 landscape cinematic frame. two groups of readers debating around a table, a single book in the middle. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Kaku không có câu trả lời. Nhưng Kaku nghĩ đó là lý do bộ truyện này vẫn được bàn luận, dù đã kết thúc nhiều…

```text
Wide 16:9 landscape cinematic frame. a group of silhouettes sitting around a campfire at night, deep in discussion. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Tóm lại, chín chi tiết cài cắm: chiếc chìa khóa, titan không cần ăn, khuôn mặt trong tường, titan trên mái nh…

```text
Wide 16:9 landscape cinematic frame. a board with nine before-and-after photo pairs, connected by threads. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: chi tiết nào khiến bạn sốc nhất khi nhận ra? Hoặc bạn còn biết chi tiết cài cắm nào mà Kaku…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a blank photo frame labeled 10. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tới, Kaku quay lại với một bộ truyện quen thuộc để gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Narut…

```text
Wide 16:9 landscape cinematic frame. a notice board with ten pinned notes and a small leaf-shaped pin. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Và nếu xem lại Attack on Titan, hãy nhớ để ý trang đầu tiên. Kaku g…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sealing a letter with a small red wax stamp and waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Một bộ truyện được lên kế hoạch

Khoảng 126 giây · cảnh s01–s11 · 1640 ký tự

**Gemini**

```text
Cảnh báo cực mạnh: video có spoiler toàn bộ Attack on Titan, kể cả cái kết. Nếu chưa xem hết, hãy dừng ở đây. Video này sẽ phá hỏng những cú sốc lớn nhất của bộ truyện.

<short pause> Có những bộ truyện viết tới đâu nghĩ tới đó. Và có những bộ mà câu trả lời cuối cùng đã nằm sẵn ở ngay trang đầu tiên, chờ bạn quay lại để nhìn thấy.

<short pause> Attack on Titan là bộ thứ hai. Rất nhiều chi tiết ở tập một, chương một, tưởng như vô nghĩa, hóa ra là chìa khóa của cả câu chuyện.

<short pause> <laugh> Hôm nay Kaku sẽ đặt từng chi tiết cạnh nhau: bên trái là lần đầu nó xuất hiện, bên phải là ý nghĩa thật của nó về sau.

<short pause> Mở sổ ra nào! Mình là Kaku. Có chín chi tiết chính, thêm vài món tặng kèm, và Kaku để dành chi tiết khiến Kaku nổi da gà nhất cho tới cuối cùng.

<short pause> Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Bản anime kéo dài từ 2013 tới tận năm 2023 mới kết thúc.

<short pause> Câu chuyện bắt đầu rất đơn giản: loài người sống sau những bức tường cao năm mươi mét để trốn những người khổng lồ ăn thịt người, gọi là titan.

<short pause> Nhưng càng đi, câu chuyện càng lật ngược: titan là gì, ai xây tường, bên ngoài tường có gì. Mỗi câu trả lời lại làm thay đổi ý nghĩa của những gì ta đã xem.

<short pause> Điều làm fan kinh ngạc là nhiều câu trả lời đó được cài sẵn từ những chương đầu tiên. Đó là lý do bộ này được xem lại nhiều đến vậy.

<short pause> Tác giả từng chia sẻ trong các buổi phỏng vấn rằng ông đã hình dung những nét chính của cái kết từ khá sớm, dù nhiều chi tiết thay đổi trong quá trình vẽ. Nhờ vậy, những hạt giống từ đầu có đất để nảy mầm về sau.

<short pause> Kaku ghi chú: xem lại Attack on Titan giống như xem một bộ khác hoàn toàn. Bạn sẽ thấy nhân vật nói những câu mà lần đầu bạn không hiểu họ thật sự đang nói gì.
```

**ElevenLabs**

```text
Cảnh báo cực mạnh: video có spoiler toàn bộ Attack on Titan, kể cả cái kết. Nếu chưa xem hết, hãy dừng ở đây. Video này sẽ phá hỏng những cú sốc lớn nhất của bộ truyện.

[pause] Có những bộ truyện viết tới đâu nghĩ tới đó. Và có những bộ mà câu trả lời cuối cùng đã nằm sẵn ở ngay trang đầu tiên, chờ bạn quay lại để nhìn thấy.

[pause] Attack on Titan là bộ thứ hai. Rất nhiều chi tiết ở tập một, chương một, tưởng như vô nghĩa, hóa ra là chìa khóa của cả câu chuyện.

[pause] [chuckles] Hôm nay Kaku sẽ đặt từng chi tiết cạnh nhau: bên trái là lần đầu nó xuất hiện, bên phải là ý nghĩa thật của nó về sau.

[pause] Mở sổ ra nào! Mình là Kaku. Có chín chi tiết chính, thêm vài món tặng kèm, và Kaku để dành chi tiết khiến Kaku nổi da gà nhất cho tới cuối cùng.

[pause] Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Bản anime kéo dài từ 2013 tới tận năm 2023 mới kết thúc.

[pause] Câu chuyện bắt đầu rất đơn giản: loài người sống sau những bức tường cao năm mươi mét để trốn những người khổng lồ ăn thịt người, gọi là titan.

[pause] Nhưng càng đi, câu chuyện càng lật ngược: titan là gì, ai xây tường, bên ngoài tường có gì. Mỗi câu trả lời lại làm thay đổi ý nghĩa của những gì ta đã xem.

[pause] Điều làm fan kinh ngạc là nhiều câu trả lời đó được cài sẵn từ những chương đầu tiên. Đó là lý do bộ này được xem lại nhiều đến vậy.

[pause] Tác giả từng chia sẻ trong các buổi phỏng vấn rằng ông đã hình dung những nét chính của cái kết từ khá sớm, dù nhiều chi tiết thay đổi trong quá trình vẽ. Nhờ vậy, những hạt giống từ đầu có đất để nảy mầm về sau.

[pause] Kaku ghi chú: xem lại Attack on Titan giống như xem một bộ khác hoàn toàn. Bạn sẽ thấy nhân vật nói những câu mà lần đầu bạn không hiểu họ thật sự đang nói gì.
```

### c02 · Chi tiết 1: Chìa khóa trên cổ / Chi tiết 2: Titan không cần ăn

Khoảng 129 giây · cảnh s12–s22 · 1681 ký tự

**Gemini**

```text
Lần đầu xuất hiện: ở tập đầu tiên, cha của Eren đưa cho cậu một chiếc chìa khóa, và dặn một ngày nào đó hãy xuống tầng hầm của nhà mình.

<short pause> Suốt ba mùa anime, chiếc chìa khóa ấy luôn ở trên cổ Eren. Tầng hầm trở thành mục tiêu của cả đoàn trinh sát. Người ta tin rằng trong đó có bí mật về titan.

<short pause> Ý nghĩa về sau: tầng hầm không chứa vũ khí hay cách tiêu diệt titan. Nó chứa những cuốn sổ và một tấm ảnh chụp, bằng chứng rằng bên ngoài tường có cả một thế giới loài người.

<short pause> Và thế giới đó coi những người trong tường là kẻ thù. Chiếc chìa khóa nhỏ mở ra một cánh cửa lớn hơn nhiều so với một căn hầm.

<short pause> Trong những cuốn sổ đó, người cha còn viết về quá khứ của mình, về một gia đình, một đứa con khác và một thế giới mà ông đã rời bỏ. Mỗi trang là một câu trả lời, và cũng là một câu hỏi mới.

<short pause> <laugh> Kaku ghi chú: một chiếc chìa khóa được giữ suốt nhiều năm để mở ra một sự thật không ai muốn nghe. Đây là cài cắm kiểu kinh điển, nhưng làm rất trọn vẹn.

<short pause> Lần đầu xuất hiện: ở mùa một, một nhà nghiên cứu phát hiện titan không có cơ quan tiêu hóa. Chúng ăn người, nhưng không tiêu hóa gì cả, và nôn ra khi đã đầy.

<short pause> Chúng không cần ăn để sống. Chúng cũng không tấn công động vật, chỉ nhắm vào con người. Lần đầu xem, đây giống một chi tiết kỳ lạ để làm titan thêm đáng sợ.

<short pause> Ý nghĩa về sau: titan vốn là con người. Họ bị biến thành titan không có ý thức, và bản năng khiến họ tìm tới con người để ăn, với hy vọng lấy lại được thân phận người.

<short pause> Chi tiết này khiến mọi trận đánh trước đó trở nên nặng nề hơn. Những con quái vật mà các nhân vật chém hạ từng là những người bình thường.

<short pause> Kaku ghi chú: cài cắm hay nhất không phải lúc nào cũng là lời thoại. Đôi khi nó nằm trong một chi tiết sinh học tưởng như vô hại.
```

**ElevenLabs**

```text
Lần đầu xuất hiện: ở tập đầu tiên, cha của Eren đưa cho cậu một chiếc chìa khóa, và dặn một ngày nào đó hãy xuống tầng hầm của nhà mình.

[pause] Suốt ba mùa anime, chiếc chìa khóa ấy luôn ở trên cổ Eren. Tầng hầm trở thành mục tiêu của cả đoàn trinh sát. Người ta tin rằng trong đó có bí mật về titan.

[pause] Ý nghĩa về sau: tầng hầm không chứa vũ khí hay cách tiêu diệt titan. Nó chứa những cuốn sổ và một tấm ảnh chụp, bằng chứng rằng bên ngoài tường có cả một thế giới loài người.

[pause] Và thế giới đó coi những người trong tường là kẻ thù. Chiếc chìa khóa nhỏ mở ra một cánh cửa lớn hơn nhiều so với một căn hầm.

[pause] Trong những cuốn sổ đó, người cha còn viết về quá khứ của mình, về một gia đình, một đứa con khác và một thế giới mà ông đã rời bỏ. Mỗi trang là một câu trả lời, và cũng là một câu hỏi mới.

[pause] [chuckles] Kaku ghi chú: một chiếc chìa khóa được giữ suốt nhiều năm để mở ra một sự thật không ai muốn nghe. Đây là cài cắm kiểu kinh điển, nhưng làm rất trọn vẹn.

[pause] Lần đầu xuất hiện: ở mùa một, một nhà nghiên cứu phát hiện titan không có cơ quan tiêu hóa. Chúng ăn người, nhưng không tiêu hóa gì cả, và nôn ra khi đã đầy.

[pause] Chúng không cần ăn để sống. Chúng cũng không tấn công động vật, chỉ nhắm vào con người. Lần đầu xem, đây giống một chi tiết kỳ lạ để làm titan thêm đáng sợ.

[pause] Ý nghĩa về sau: titan vốn là con người. Họ bị biến thành titan không có ý thức, và bản năng khiến họ tìm tới con người để ăn, với hy vọng lấy lại được thân phận người.

[pause] Chi tiết này khiến mọi trận đánh trước đó trở nên nặng nề hơn. Những con quái vật mà các nhân vật chém hạ từng là những người bình thường.

[pause] Kaku ghi chú: cài cắm hay nhất không phải lúc nào cũng là lời thoại. Đôi khi nó nằm trong một chi tiết sinh học tưởng như vô hại.
```

### c03 · Chi tiết 3: Khuôn mặt trong bức tường / Chi tiết 4: Titan nằm trên mái nhà / Chi tiết 5: Titan mỉm cười

Khoảng 152 giây · cảnh s23–s37 · 1971 ký tự

**Gemini**

```text
Lần đầu xuất hiện: cuối mùa một, sau một trận đánh làm vỡ một phần bức tường, lộ ra bên trong là khuôn mặt của một titan khổng lồ.

<short pause> Một vị mục sư biết rõ bí mật này, và hoảng loạn yêu cầu phải che nó lại khỏi ánh mặt trời. Người xem lúc đó chỉ biết thắc mắc.

<short pause> Ý nghĩa về sau: những bức tường được tạo thành từ vô số titan khổng lồ đứng sát cạnh nhau, cứng hóa lại. Thứ bảo vệ loài người cũng là thứ có thể hủy diệt họ.

<short pause> Ở cuối truyện, những titan trong tường được đánh thức và bước ra, tạo nên một thảm họa có tên là Địa Minh. Cả thế giới rung chuyển dưới bước chân của chúng.

<short pause> <laugh> Kaku ghi chú: bức tường là biểu tượng của sự an toàn trong mùa một, và là biểu tượng của sự hủy diệt ở mùa cuối. Cùng một vật, hai ý nghĩa đối lập.

<short pause> Lần đầu xuất hiện: ở mùa hai, một người lính trẻ về thăm làng quê của mình và thấy một titan nằm ngửa trên nóc nhà mình, không thể cử động.

<short pause> Titan đó nhìn cậu và thều thào một câu nghe như lời chào đón về nhà. Ngôi làng không có một vết máu nào, nhưng không còn ai.

<short pause> Ý nghĩa về sau: dân làng không bị ăn thịt. Chính họ đã bị biến thành titan. Và titan trên mái nhà là mẹ của cậu lính trẻ.

<short pause> Đây là lần đầu truyện gần như nói thẳng rằng titan là con người, sớm hơn nhiều so với lời giải thích chính thức.

<short pause> Kaku ghi chú: chi tiết này nhỏ, nhưng là một trong những khoảnh khắc buồn nhất cả bộ. Nó biến nỗi sợ thành nỗi đau.

<short pause> Lần đầu xuất hiện: tập một, titan ăn thịt mẹ của Eren có gương mặt mỉm cười, trông gần như hiền lành. Đó là hình ảnh ám ảnh cả tuổi thơ của Eren và của khán giả.

<short pause> Ở mùa ba, ta biết titan đó từng là vợ trước của cha Eren. Một người phụ nữ bị biến thành titan và thả vào trong tường.

<short pause> Và ở mùa cuối, một sự thật còn đáng sợ hơn được hé lộ: hướng đi của titan đó hôm ấy có liên quan tới chính sức mạnh của Eren, từ tương lai.

<short pause> Nói cách khác, Eren đã chứng kiến bi kịch lớn nhất đời mình, và bi kịch ấy lại gắn với chính cậu. Đây là lúc câu chuyện trở thành một vòng tròn khép kín.

<short pause> Kaku ghi chú: Kaku vẫn chưa hết rùng mình mỗi khi nghĩ lại chi tiết này.
```

**ElevenLabs**

```text
Lần đầu xuất hiện: cuối mùa một, sau một trận đánh làm vỡ một phần bức tường, lộ ra bên trong là khuôn mặt của một titan khổng lồ.

[pause] Một vị mục sư biết rõ bí mật này, và hoảng loạn yêu cầu phải che nó lại khỏi ánh mặt trời. Người xem lúc đó chỉ biết thắc mắc.

[pause] Ý nghĩa về sau: những bức tường được tạo thành từ vô số titan khổng lồ đứng sát cạnh nhau, cứng hóa lại. Thứ bảo vệ loài người cũng là thứ có thể hủy diệt họ.

[pause] Ở cuối truyện, những titan trong tường được đánh thức và bước ra, tạo nên một thảm họa có tên là Địa Minh. Cả thế giới rung chuyển dưới bước chân của chúng.

[pause] [chuckles] Kaku ghi chú: bức tường là biểu tượng của sự an toàn trong mùa một, và là biểu tượng của sự hủy diệt ở mùa cuối. Cùng một vật, hai ý nghĩa đối lập.

[pause] Lần đầu xuất hiện: ở mùa hai, một người lính trẻ về thăm làng quê của mình và thấy một titan nằm ngửa trên nóc nhà mình, không thể cử động.

[pause] Titan đó nhìn cậu và thều thào một câu nghe như lời chào đón về nhà. Ngôi làng không có một vết máu nào, nhưng không còn ai.

[pause] Ý nghĩa về sau: dân làng không bị ăn thịt. Chính họ đã bị biến thành titan. Và titan trên mái nhà là mẹ của cậu lính trẻ.

[pause] Đây là lần đầu truyện gần như nói thẳng rằng titan là con người, sớm hơn nhiều so với lời giải thích chính thức.

[pause] Kaku ghi chú: chi tiết này nhỏ, nhưng là một trong những khoảnh khắc buồn nhất cả bộ. Nó biến nỗi sợ thành nỗi đau.

[pause] Lần đầu xuất hiện: tập một, titan ăn thịt mẹ của Eren có gương mặt mỉm cười, trông gần như hiền lành. Đó là hình ảnh ám ảnh cả tuổi thơ của Eren và của khán giả.

[pause] Ở mùa ba, ta biết titan đó từng là vợ trước của cha Eren. Một người phụ nữ bị biến thành titan và thả vào trong tường.

[pause] Và ở mùa cuối, một sự thật còn đáng sợ hơn được hé lộ: hướng đi của titan đó hôm ấy có liên quan tới chính sức mạnh của Eren, từ tương lai.

[pause] Nói cách khác, Eren đã chứng kiến bi kịch lớn nhất đời mình, và bi kịch ấy lại gắn với chính cậu. Đây là lúc câu chuyện trở thành một vòng tròn khép kín.

[pause] Kaku ghi chú: Kaku vẫn chưa hết rùng mình mỗi khi nghĩ lại chi tiết này.
```

### c04 · Chi tiết 6: Cuộc trò chuyện về quê nhà / Chi tiết 7: Giấc mơ về biển

Khoảng 116 giây · cảnh s38–s48 · 1514 ký tự

**Gemini**

```text
Lần đầu xuất hiện: ở mùa một và mùa hai, hai học viên thân thiết thỉnh thoảng nhắc về việc trở về quê nhà, như bất kỳ người lính xa nhà nào.

<short pause> Một người trong số họ luôn đóng vai người anh cả đáng tin cậy, chăm sóc mọi người trong nhóm. Không ai nghi ngờ gì.

<short pause> Ý nghĩa về sau: quê nhà của họ ở bên ngoài tường. Họ là chiến binh được gửi tới để lấy sức mạnh của titan thủy tổ. Và chính họ đã phá cánh cổng trong ngày đầu tiên của câu chuyện.

<short pause> Lần xem lại, mỗi lần họ nhắc về quê nhà, về nhiệm vụ, về việc phải trở về, đều mang một nghĩa hoàn toàn khác.

<short pause> Thậm chí có lúc, một trong hai người thú nhận thẳng thân phận của mình giữa một cuộc trò chuyện bình thường, với giọng điệu như đang nói chuyện thời tiết. Cảnh đó khiến rất nhiều khán giả phải tua lại.

<short pause> <laugh> Kaku ghi chú: tác giả để những nhân vật này nói gần như sự thật ngay trước mặt khán giả. Chính vì quá thật nên không ai nghi ngờ.

<short pause> Lần đầu xuất hiện: từ những tập đầu, Armin kể cho Eren nghe về đại dương, một vùng nước mặn mênh mông mà sách cấm nói tới. Hai cậu bé hứa một ngày sẽ nhìn thấy nó.

<short pause> Suốt nhiều mùa, biển là biểu tượng của tự do, của thế giới rộng lớn bên ngoài bức tường.

<short pause> Ý nghĩa về sau: khi đến được biển, họ nhận ra bên kia đại dương là những người coi họ là kẻ thù. Biển không phải là tự do, mà là đường ranh giới tiếp theo.

<short pause> Câu hỏi của Eren khi đứng trước biển gần như là câu hỏi của cả bộ truyện: nếu giết hết kẻ thù bên kia biển, liệu ta có được tự do không?

<short pause> Kaku ghi chú: đây là cài cắm đau lòng nhất. Giấc mơ tuổi thơ đẹp nhất trở thành nơi giấc mơ tan vỡ.
```

**ElevenLabs**

```text
Lần đầu xuất hiện: ở mùa một và mùa hai, hai học viên thân thiết thỉnh thoảng nhắc về việc trở về quê nhà, như bất kỳ người lính xa nhà nào.

[pause] Một người trong số họ luôn đóng vai người anh cả đáng tin cậy, chăm sóc mọi người trong nhóm. Không ai nghi ngờ gì.

[pause] Ý nghĩa về sau: quê nhà của họ ở bên ngoài tường. Họ là chiến binh được gửi tới để lấy sức mạnh của titan thủy tổ. Và chính họ đã phá cánh cổng trong ngày đầu tiên của câu chuyện.

[pause] Lần xem lại, mỗi lần họ nhắc về quê nhà, về nhiệm vụ, về việc phải trở về, đều mang một nghĩa hoàn toàn khác.

[pause] Thậm chí có lúc, một trong hai người thú nhận thẳng thân phận của mình giữa một cuộc trò chuyện bình thường, với giọng điệu như đang nói chuyện thời tiết. Cảnh đó khiến rất nhiều khán giả phải tua lại.

[pause] [chuckles] Kaku ghi chú: tác giả để những nhân vật này nói gần như sự thật ngay trước mặt khán giả. Chính vì quá thật nên không ai nghi ngờ.

[pause] Lần đầu xuất hiện: từ những tập đầu, Armin kể cho Eren nghe về đại dương, một vùng nước mặn mênh mông mà sách cấm nói tới. Hai cậu bé hứa một ngày sẽ nhìn thấy nó.

[pause] Suốt nhiều mùa, biển là biểu tượng của tự do, của thế giới rộng lớn bên ngoài bức tường.

[pause] Ý nghĩa về sau: khi đến được biển, họ nhận ra bên kia đại dương là những người coi họ là kẻ thù. Biển không phải là tự do, mà là đường ranh giới tiếp theo.

[pause] [curious] Câu hỏi của Eren khi đứng trước biển gần như là câu hỏi của cả bộ truyện: nếu giết hết kẻ thù bên kia biển, liệu ta có được tự do không?

[pause] Kaku ghi chú: đây là cài cắm đau lòng nhất. Giấc mơ tuổi thơ đẹp nhất trở thành nơi giấc mơ tan vỡ.
```

### c05 · Chi tiết 8: Những cánh chim / Những câu thoại đổi nghĩa khi xem lại

Khoảng 102 giây · cảnh s49–s58 · 1327 ký tự

**Gemini**

```text
Lần đầu xuất hiện: ngay từ những cảnh đầu tiên, Eren nhìn lên những đàn chim bay qua bức tường. Biểu tượng của đoàn trinh sát cũng là đôi cánh.

<short pause> Với Eren, chim là tự do: chúng bay qua tường mà không cần xin phép ai. Cậu muốn được như chúng.

<short pause> Ý nghĩa về sau: ở cảnh cuối cùng của truyện, một chú chim xuất hiện bên cạnh người đã luôn ở bên Eren, và quấn lại chiếc khăn quàng cho cô.

<short pause> Nhiều người hiểu chú chim đó như hình ảnh của Eren, cuối cùng được tự do. Truyện để người đọc tự cảm nhận.

<short pause> <laugh> Kaku ghi chú: chữ tự do được nhắc tới rất nhiều lần trong truyện, nhưng nó được nói rõ nhất bằng một hình ảnh không có lời.

<short pause> Không chỉ đồ vật và hình ảnh, cả lời thoại trong Attack on Titan cũng đổi nghĩa hoàn toàn khi xem lại.

<short pause> Ở tập một, sau khi mất mẹ, cậu bé Eren hét lên rằng sẽ tiêu diệt hết bọn chúng, không chừa một con nào. Lần đầu xem, ta hiểu đó là lời thề của một đứa trẻ đau khổ với loài titan.

<short pause> Xem lại sau khi biết cái kết, câu nói ấy nghe hoàn toàn khác. Vì về sau, thứ Eren muốn tiêu diệt không còn là titan, mà là cả thế giới bên kia bức tường.

<short pause> Một câu khác của Armin: người không thể hy sinh bất cứ điều gì thì không thể thay đổi được gì. Lúc đầu nghe như một lời khuyên chiến thuật, về sau nó trở thành gánh nặng của cả nhóm.

<short pause> Kaku ghi chú: Kaku khuyên bạn xem lại tập một sau khi xem hết. Gần như câu nào cũng có tầng nghĩa thứ hai.
```

**ElevenLabs**

```text
Lần đầu xuất hiện: ngay từ những cảnh đầu tiên, Eren nhìn lên những đàn chim bay qua bức tường. Biểu tượng của đoàn trinh sát cũng là đôi cánh.

[pause] Với Eren, chim là tự do: chúng bay qua tường mà không cần xin phép ai. Cậu muốn được như chúng.

[pause] Ý nghĩa về sau: ở cảnh cuối cùng của truyện, một chú chim xuất hiện bên cạnh người đã luôn ở bên Eren, và quấn lại chiếc khăn quàng cho cô.

[pause] Nhiều người hiểu chú chim đó như hình ảnh của Eren, cuối cùng được tự do. Truyện để người đọc tự cảm nhận.

[pause] [chuckles] Kaku ghi chú: chữ tự do được nhắc tới rất nhiều lần trong truyện, nhưng nó được nói rõ nhất bằng một hình ảnh không có lời.

[pause] Không chỉ đồ vật và hình ảnh, cả lời thoại trong Attack on Titan cũng đổi nghĩa hoàn toàn khi xem lại.

[pause] Ở tập một, sau khi mất mẹ, cậu bé Eren hét lên rằng sẽ tiêu diệt hết bọn chúng, không chừa một con nào. Lần đầu xem, ta hiểu đó là lời thề của một đứa trẻ đau khổ với loài titan.

[pause] Xem lại sau khi biết cái kết, câu nói ấy nghe hoàn toàn khác. Vì về sau, thứ Eren muốn tiêu diệt không còn là titan, mà là cả thế giới bên kia bức tường.

[pause] Một câu khác của Armin: người không thể hy sinh bất cứ điều gì thì không thể thay đổi được gì. Lúc đầu nghe như một lời khuyên chiến thuật, về sau nó trở thành gánh nặng của cả nhóm.

[pause] Kaku ghi chú: Kaku khuyên bạn xem lại tập một sau khi xem hết. Gần như câu nào cũng có tầng nghĩa thứ hai.
```

### c06 · Chi tiết tặng kèm: Cơn đau đầu / Cách nhận ra một chi tiết cài cắm

Khoảng 93 giây · cảnh s59–s68 · 1212 ký tự

**Gemini**

```text
Chi tiết tặng kèm trước khi tới chi tiết cuối. Lần đầu xuất hiện: nhiều lần trong truyện, Mikasa bỗng ôm đầu vì một cơn đau đột ngột, thường vào những khoảnh khắc liên quan tới Eren.

<short pause> Lần đầu xem, người ta nghĩ đó là di chứng từ chấn thương, hoặc chỉ là cách thể hiện căng thẳng. Không ai để ý nhiều.

<short pause> Ý nghĩa về sau: cái kết gợi ý rằng những cơn đau đó liên quan tới cô gái đầu tiên có sức mạnh titan, người đã dõi theo lựa chọn của Mikasa suốt cả câu chuyện.

<short pause> Và lựa chọn cuối cùng của Mikasa được xem là chìa khóa để giải thoát cô gái ấy khỏi hai nghìn năm ràng buộc. Chi tiết nhỏ bé nhất lại gắn với cái kết lớn nhất.

<short pause> <laugh> Kaku ghi chú: đây là chi tiết mà rất nhiều người chỉ nhận ra sau khi đọc chương cuối. Kaku cũng vậy.

<short pause> Trước chi tiết cuối cùng, Kaku chia sẻ cách tự nhận ra cài cắm khi xem bất kỳ bộ truyện nào.

<short pause> Một: để ý những chi tiết được nhắc lại mà không có lý do rõ ràng. Một đồ vật, một câu nói, một hình ảnh lặp lại thường có ý nghĩa.

<short pause> Hai: để ý những câu trả lời quá hoàn hảo hoặc quá mơ hồ. Khi nhân vật nói một câu mà bạn thấy hơi lạ, hãy ghi nó lại.

<short pause> Ba: để ý tên chương hay tên tập. Tác giả thường giấu manh mối ở những chỗ ít người đọc kỹ nhất.

<short pause> Và chi tiết cuối cùng của Kaku hôm nay chính là một tên chương.
```

**ElevenLabs**

```text
Chi tiết tặng kèm trước khi tới chi tiết cuối. Lần đầu xuất hiện: nhiều lần trong truyện, Mikasa bỗng ôm đầu vì một cơn đau đột ngột, thường vào những khoảnh khắc liên quan tới Eren.

[pause] Lần đầu xem, người ta nghĩ đó là di chứng từ chấn thương, hoặc chỉ là cách thể hiện căng thẳng. Không ai để ý nhiều.

[pause] Ý nghĩa về sau: cái kết gợi ý rằng những cơn đau đó liên quan tới cô gái đầu tiên có sức mạnh titan, người đã dõi theo lựa chọn của Mikasa suốt cả câu chuyện.

[pause] Và lựa chọn cuối cùng của Mikasa được xem là chìa khóa để giải thoát cô gái ấy khỏi hai nghìn năm ràng buộc. Chi tiết nhỏ bé nhất lại gắn với cái kết lớn nhất.

[pause] [chuckles] Kaku ghi chú: đây là chi tiết mà rất nhiều người chỉ nhận ra sau khi đọc chương cuối. Kaku cũng vậy.

[pause] Trước chi tiết cuối cùng, Kaku chia sẻ cách tự nhận ra cài cắm khi xem bất kỳ bộ truyện nào.

[pause] Một: để ý những chi tiết được nhắc lại mà không có lý do rõ ràng. Một đồ vật, một câu nói, một hình ảnh lặp lại thường có ý nghĩa.

[pause] Hai: để ý những câu trả lời quá hoàn hảo hoặc quá mơ hồ. Khi nhân vật nói một câu mà bạn thấy hơi lạ, hãy ghi nó lại.

[pause] Ba: để ý tên chương hay tên tập. Tác giả thường giấu manh mối ở những chỗ ít người đọc kỹ nhất.

[pause] Và chi tiết cuối cùng của Kaku hôm nay chính là một tên chương.
```

### c07 · Chi tiết 9: Gửi em, hai nghìn năm sau / Góc nhìn của Kaku: vòng lặp và tự do

Khoảng 141 giây · cảnh s69–s80 · 1830 ký tự

**Gemini**

```text
Lần đầu xuất hiện: tên của chương một, cũng là tên tập một của anime, là Gửi em, hai nghìn năm sau. Một cái tên đẹp nhưng khó hiểu, không ai biết em là ai và vì sao là hai nghìn năm.

<short pause> Và ở trang đầu tiên của chương một, có một cảnh rất lạ: một cô gái nói với Eren câu tạm biệt, hẹn gặp lại, trước khi cậu tỉnh dậy dưới gốc cây, nước mắt chảy dài mà không biết vì sao.

<short pause> Ý nghĩa về sau: gần cuối truyện có một chương mang tên đối xứng hoàn hảo: Từ em, hai nghìn năm trước. Chương đó kể về cô gái đầu tiên có sức mạnh titan, hai nghìn năm trước câu chuyện.

<short pause> Còn cảnh ở trang đầu tiên, cô gái nói lời tạm biệt, hóa ra là một cảnh từ tương lai, gần với cái kết của cả câu chuyện. Nước mắt của cậu bé Eren là vì cậu đã thoáng thấy điều đó.

<short pause> Nghĩa là ngay từ trang đầu tiên, câu chuyện đã được viết như một vòng tròn. Hai nghìn năm lịch sử, mười hai năm đăng truyện, và kết thúc quay về đúng chỗ bắt đầu.

<short pause> <laugh> Kaku ghi chú: đây là chi tiết khiến Kaku nổi da gà nhất. Lần đầu đọc, bạn không thể hiểu. Lần cuối đọc, bạn không thể quên.

<short pause> Vì sao Isayama lại cài cắm nhiều đến vậy? Kaku nghĩ nó gắn chặt với chủ đề của bộ truyện.

<short pause> Attack on Titan nói về tự do. <short pause> Nhưng nhân vật chính càng chạy tới tự do, càng như bị cuốn vào một vòng lặp đã được định sẵn, nơi tương lai và quá khứ ảnh hưởng lẫn nhau.

<short pause> Những chi tiết cài cắm chính là bằng chứng của vòng lặp đó: mọi thứ ở cuối đã có mặt ở đầu. Câu chuyện không để ai, kể cả nhân vật chính, thoát khỏi nó dễ dàng.

<short pause> Và vì vậy, câu hỏi mà bộ truyện để lại cho người xem là: tự do thật sự là gì, nếu ta không thể thay đổi những gì đã được định sẵn?

<short pause> Có người thấy cái kết đẹp, có người thấy nó gây tranh cãi. <short pause> Nhưng gần như ai cũng đồng ý rằng những cài cắm từ đầu cho thấy câu chuyện có một hướng đi rõ ràng.

<short pause> Kaku không có câu trả lời. <short pause> Nhưng Kaku nghĩ đó là lý do bộ truyện này vẫn được bàn luận, dù đã kết thúc nhiều năm.
```

**ElevenLabs**

```text
Lần đầu xuất hiện: tên của chương một, cũng là tên tập một của anime, là Gửi em, hai nghìn năm sau. Một cái tên đẹp nhưng khó hiểu, không ai biết em là ai và vì sao là hai nghìn năm.

[pause] Và ở trang đầu tiên của chương một, có một cảnh rất lạ: một cô gái nói với Eren câu tạm biệt, hẹn gặp lại, trước khi cậu tỉnh dậy dưới gốc cây, nước mắt chảy dài mà không biết vì sao.

[pause] Ý nghĩa về sau: gần cuối truyện có một chương mang tên đối xứng hoàn hảo: Từ em, hai nghìn năm trước. Chương đó kể về cô gái đầu tiên có sức mạnh titan, hai nghìn năm trước câu chuyện.

[pause] Còn cảnh ở trang đầu tiên, cô gái nói lời tạm biệt, hóa ra là một cảnh từ tương lai, gần với cái kết của cả câu chuyện. Nước mắt của cậu bé Eren là vì cậu đã thoáng thấy điều đó.

[pause] Nghĩa là ngay từ trang đầu tiên, câu chuyện đã được viết như một vòng tròn. Hai nghìn năm lịch sử, mười hai năm đăng truyện, và kết thúc quay về đúng chỗ bắt đầu.

[pause] [chuckles] Kaku ghi chú: đây là chi tiết khiến Kaku nổi da gà nhất. Lần đầu đọc, bạn không thể hiểu. Lần cuối đọc, bạn không thể quên.

[pause] [curious] Vì sao Isayama lại cài cắm nhiều đến vậy? Kaku nghĩ nó gắn chặt với chủ đề của bộ truyện.

[pause] Attack on Titan nói về tự do. [pause] Nhưng nhân vật chính càng chạy tới tự do, càng như bị cuốn vào một vòng lặp đã được định sẵn, nơi tương lai và quá khứ ảnh hưởng lẫn nhau.

[pause] Những chi tiết cài cắm chính là bằng chứng của vòng lặp đó: mọi thứ ở cuối đã có mặt ở đầu. Câu chuyện không để ai, kể cả nhân vật chính, thoát khỏi nó dễ dàng.

[pause] Và vì vậy, câu hỏi mà bộ truyện để lại cho người xem là: tự do thật sự là gì, nếu ta không thể thay đổi những gì đã được định sẵn?

[pause] Có người thấy cái kết đẹp, có người thấy nó gây tranh cãi. [pause] Nhưng gần như ai cũng đồng ý rằng những cài cắm từ đầu cho thấy câu chuyện có một hướng đi rõ ràng.

[pause] Kaku không có câu trả lời. [pause] Nhưng Kaku nghĩ đó là lý do bộ truyện này vẫn được bàn luận, dù đã kết thúc nhiều năm.
```

### c08 · Kết

Khoảng 44 giây · cảnh s81–s84 · 576 ký tự

**Gemini**

```text
Tóm lại, chín chi tiết cài cắm: chiếc chìa khóa, titan không cần ăn, khuôn mặt trong tường, titan trên mái nhà, titan mỉm cười, cuộc trò chuyện về quê nhà, giấc mơ về biển, những cánh chim, và tên chương đầu tiên.

<short pause> Câu hỏi cho bạn: chi tiết nào khiến bạn sốc nhất khi nhận ra? <laugh> Hoặc bạn còn biết chi tiết cài cắm nào mà Kaku chưa nhắc tới?

<short pause> Video tới, Kaku quay lại với một bộ truyện quen thuộc để gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Naruto.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. Và nếu xem lại Attack on Titan, hãy nhớ để ý trang đầu tiên. Kaku gửi bạn, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại, chín chi tiết cài cắm: chiếc chìa khóa, titan không cần ăn, khuôn mặt trong tường, titan trên mái nhà, titan mỉm cười, cuộc trò chuyện về quê nhà, giấc mơ về biển, những cánh chim, và tên chương đầu tiên.

[pause] [curious] Câu hỏi cho bạn: chi tiết nào khiến bạn sốc nhất khi nhận ra? [chuckles] Hoặc bạn còn biết chi tiết cài cắm nào mà Kaku chưa nhắc tới?

[pause] Video tới, Kaku quay lại với một bộ truyện quen thuộc để gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Naruto.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. Và nếu xem lại Attack on Titan, hãy nhớ để ý trang đầu tiên. Kaku gửi bạn, hẹn gặp lại!
```
