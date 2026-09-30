# Bộ prompt · JoJo Steel Ball Run: Kỹ thuật Xoay và tỉ lệ vàng — khoa học có thật không?

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

Lời: Cảnh báo: video có spoiler nhẹ JoJo Steel Ball Run, tới khoảng chặng thứ ba của cuộc đua. Các cấp độ sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a dusty desert trail at sunrise with hoofprints leading toward the horizon. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một quả cầu thép xoay trong lòng bàn tay. Nó không phát sáng, không có năng lượng thần bí, chỉ xoay. Nhưng kh…

```text
Wide 16:9 landscape cinematic frame. a polished steel ball spinning rapidly on a gloved palm, wind swirling around it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Và bí quyết của nó, theo truyện, là một con số: một phẩy sáu một tám. Tỉ lệ vàng.

```text
Wide 16:9 landscape cinematic frame. the number 1.618 glowing in golden light above a spiral drawn in the sand. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hôm nay Kaku không giải thích như mọi khi. Kaku sẽ mang thước kẻ, máy tính và sách vật lý ra, để hỏi một câu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny safety goggles, surrounded by a ruler, calculator and physics book. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Mỗi chương hôm nay sẽ có ba bước: truyện nói gì, khoa học nói gì, và truyện đã ph…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook to a page with three columns and a score box. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Bối cảnh: cuộc đua xuyên nước Mỹ

Lời: Steel Ball Run là phần thứ bảy của loạt JoJo, do Araki Hirohiko sáng tác. Câu chuyện bắt đầu năm 1890 với một…

```text
Wide 16:9 landscape cinematic frame. a vintage poster-style illustration of horses racing across a vast American plain, 1890 aesthetic. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Hàng nghìn tay đua xuất phát từ bờ biển phía tây, đích đến là New York, cách khoảng sáu nghìn cây số. Người t…

```text
Wide 16:9 landscape cinematic frame. a map of a continent with a dotted route from the west coast to the east coast, a trophy at the end. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Trong số đó có hai nhân vật chính: Gyro, một người đàn ông đến từ nước Ý với hai quả cầu thép, và Johnny, một…

```text
Wide 16:9 landscape cinematic frame. two riders silhouetted at dawn, one with steel balls on his belt, the other in a wheelchair beside a horse. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Trong tập đầu, Johnny vô tình chạm vào quả cầu đang xoay của Gyro, và đôi chân đã liệt của anh bỗng cử động t…

```text
Wide 16:9 landscape cinematic frame. a hand touching a spinning steel ball as faint golden ripples travel down toward motionless legs. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là bộ JoJo mà nhiều fan đánh giá cao nhất. Bản anime phát tập đầu trên Netflix tháng 3 năm…

```text
Wide 16:9 landscape cinematic frame. the owl mascot riding a tiny toy horse across a map on a desk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Kỹ thuật Xoay là gì?

Lời: Theo truyện, Xoay là kỹ thuật được truyền lại trong gia tộc của Gyro qua nhiều thế hệ. Nó được dùng trong y t…

```text
Wide 16:9 landscape cinematic frame. an old family crest on a stone wall, a pair of steel balls resting on a velvet cloth below it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Người dùng xoay một vật, thường là quả cầu thép, với độ chính xác cực cao. Khi chạm vào mục tiêu, lực xoay tr…

```text
Wide 16:9 landscape cinematic frame. a steel ball striking a stone wall, spiral ripples spreading outward across the surface. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nó có thể làm vỡ vật cứng, làm cơ bắp co giật, làm da chuyển động, và thậm chí điều khiển cơ thể người khác t…

```text
Wide 16:9 landscape cinematic frame. four small panels: a cracked stone, a twitching arm, rippling skin, and a puppet-like pose. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nhưng Xoay chỉ mạnh khi đủ hoàn hảo. Và theo truyện, thước đo của sự hoàn hảo đó là hình chữ nhật vàng.

```text
Wide 16:9 landscape cinematic frame. a golden rectangle drawn over a spinning ball, the spiral inside it glowing brightly. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vậy để kiểm tra Xoay, trước hết ta phải hiểu tỉ lệ vàng là gì. Đi thôi!

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling a golden measuring tape out of its scarf. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Tỉ lệ vàng là gì?

Lời: Tỉ lệ vàng là một con số, xấp xỉ một phẩy sáu một tám. Người ta thường viết nó bằng chữ cái Hy Lạp phi.

```text
Wide 16:9 landscape cinematic frame. the Greek letter phi glowing in gold on a chalkboard, 1.618 written beneath it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Định nghĩa rất gọn: chia một đoạn thẳng thành hai phần, sao cho cả đoạn chia cho phần dài bằng đúng phần dài…

```text
Wide 16:9 landscape cinematic frame. a line segment split into two parts with arcs showing the matching ratio. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Hình chữ nhật vàng là hình chữ nhật có cạnh dài gấp phi lần cạnh ngắn. Nó có một tính chất kỳ diệu: cắt đi mộ…

```text
Wide 16:9 landscape cinematic frame. a golden rectangle with a square removed, revealing a smaller golden rectangle inside. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Cứ cắt mãi như vậy, bạn được vô số hình vuông nhỏ dần. Nối các góc của chúng bằng những cung tròn, ta có xoắn…

```text
Wide 16:9 landscape cinematic frame. nested squares shrinking inward with a golden spiral curving through them endlessly. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Đây là chỗ truyện lấy ý tưởng: một vòng xoay đi theo xoắn ốc vô tận thì cũng có thể tạo ra năng lượng vô tận.…

```text
Wide 16:9 landscape cinematic frame. a steel ball tracing a golden spiral path, an infinity symbol glowing faintly above it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: phần toán học ở trên là hoàn toàn đúng. Tỉ lệ vàng và xoắn ốc vàng là kiến thức toán học thật,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a neat spiral with a compass on graph paper. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Kiểm tra 1: Tỉ lệ vàng có mặt khắp tự nhiên?

Lời: Truyện nói: tỉ lệ vàng có mặt trong tự nhiên, và người dùng Xoay học theo tự nhiên để xoay hoàn hảo hơn. Đây…

```text
Wide 16:9 landscape cinematic frame. a collage of a sunflower, a seashell, a pinecone and a classical statue, each overlaid with a spiral. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Khoa học nói: có những chỗ đúng thật. Hạt hướng dương và vảy quả thông xếp theo các đường xoắn, và số đường x…

```text
Wide 16:9 landscape cinematic frame. a close-up of a sunflower head with two sets of spirals highlighted in different colors, numbers 34 and 55. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Lý do là mỗi hạt mới mọc lệch hạt trước một góc khoảng một trăm ba mươi bảy phẩy năm độ, gọi là góc vàng. Góc…

```text
Wide 16:9 landscape cinematic frame. a diagram of seeds placed one by one at a rotating angle, forming a tight spiral pattern. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nhưng cũng có nhiều chỗ bị thổi phồng. Vỏ ốc anh vũ là một đường xoắn ốc thật, nhưng các phép đo cho thấy tỉ…

```text
Wide 16:9 landscape cinematic frame. a spiral seashell with a measuring tape, a small red cross next to the number 1.618. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Tương tự, những khẳng định kiểu khuôn mặt đẹp hay công trình cổ được xây theo đúng tỉ lệ vàng thường thiếu bằ…

```text
Wide 16:9 landscape cinematic frame. a classical temple facade with golden rectangles drawn over it, several question marks floating nearby. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Điểm độ thật cho kiểm tra này: sáu trên mười. Tỉ lệ vàng có mặt trong tự nhiên thật, nhưng không có mặt ở khắ…

```text
Wide 16:9 landscape cinematic frame. a score card showing 6 out of 10 with a golden sunflower icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Kiểm tra 2: Vật xoay có ổn định hơn?

Lời: Truyện nói: quả cầu xoay càng chuẩn thì càng mạnh và càng khó bị chặn lại. Hãy thử kiểm tra phần đầu: xoay có…

```text
Wide 16:9 landscape cinematic frame. a steel ball flying straight through the air with a perfect spiral trail behind it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Khoa học nói: có, và rất rõ ràng. Một vật đang xoay có mô men động lượng, và nó chống lại việc bị đổi hướng t…

```text
Wide 16:9 landscape cinematic frame. a spinning top balancing upright beside a stopped top lying on its side. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nòng súng trường có rãnh xoắn để làm viên đạn xoay khi bay ra, giúp nó bay thẳng và ổn định hơn. Người ném bó…

```text
Wide 16:9 landscape cinematic frame. a cross-section of a rifled barrel with spiral grooves, a spinning projectile leaving it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Xoay còn làm đường bay cong đi. Trái bóng xoáy trong bóng đá bẻ cong quỹ đạo nhờ hiệu ứng Magnus, khi không k…

```text
Wide 16:9 landscape cinematic frame. a soccer ball curving around a wall of players, air flow lines bending around it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Trong truyện, Gyro thường ném quả cầu theo những quỹ đạo cong khó đoán. Về nguyên lý, điều này hoàn toàn có c…

```text
Wide 16:9 landscape cinematic frame. a steel ball arcing around a rock in a curved path, dust trail following it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Điểm độ thật: chín trên mười. Xoay giúp vật ổn định và bay cong là vật lý chuẩn. Chỉ có mức độ chính xác tron…

```text
Wide 16:9 landscape cinematic frame. a score card showing 9 out of 10 with a spinning top icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Kiểm tra 3: Năng lượng xoay vô hạn?

Lời: Đây là tuyên bố lớn nhất: vòng xoay đi theo xoắn ốc vàng có thể tạo ra năng lượng gần như vô tận.

```text
Wide 16:9 landscape cinematic frame. a glowing golden spiral spinning into infinity, sparks of energy flowing outward. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Khoa học nói: một vật đang xoay đúng là tích trữ năng lượng. Năng lượng đó phụ thuộc vào khối lượng, cách phâ…

```text
Wide 16:9 landscape cinematic frame. a heavy flywheel spinning in a lab with an energy meter beside it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Người ta còn dùng bánh đà, một khối nặng xoay rất nhanh, để trữ năng lượng trong một số hệ thống điện và máy…

```text
Wide 16:9 landscape cinematic frame. a cutaway of a modern flywheel energy storage unit glowing softly. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhưng năng lượng vô hạn thì không. Định luật bảo toàn năng lượng nói rằng năng lượng không tự sinh ra. Và ma…

```text
Wide 16:9 landscape cinematic frame. a spinning ball slowly losing speed, heat waves and air swirls stealing energy from it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Một đường xoắn ốc vô tận trên giấy chỉ là hình học. Hình dạng của chuyển động không thể tự tạo ra năng lượng.…

```text
Wide 16:9 landscape cinematic frame. a crossed-out sketch of a perpetual motion machine on an old blueprint. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Điểm độ thật: một trên mười. Một điểm cho ý tưởng vật xoay tích trữ năng lượng. Phần vô hạn là trí tưởng tượn…

```text
Wide 16:9 landscape cinematic frame. a score card showing 1 out of 10 with an infinity symbol icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đừng buồn nhé. Chính truyện cũng coi vòng xoay vô tận là thứ gần như không thể đạt được, và điề…

```text
Wide 16:9 landscape cinematic frame. the owl mascot patting a small crying infinity symbol on the head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Kiểm tra 4: Xoay truyền qua cơ thể

Lời: Truyện nói: lực xoay có thể truyền qua da và cơ bắp, làm cơ co giật hay khiến cơ thể cử động ngoài ý muốn.

```text
Wide 16:9 landscape cinematic frame. a glowing spiral ripple traveling along an arm, muscles tensing beneath the skin. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Khoa học nói: rung động có thể lan truyền qua cơ thể thật. Y học dùng rung động và sóng âm trong nhiều việc,…

```text
Wide 16:9 landscape cinematic frame. a medical ultrasound probe with sound waves drawn entering a stylized body outline. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Cộng hưởng là một hiện tượng có thật khác: khi rung đúng tần số tự nhiên, một vật có thể dao động rất mạnh. V…

```text
Wide 16:9 landscape cinematic frame. a wine glass shattering as a sound wave of matching frequency hits it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Nhưng để điều khiển chính xác từng nhóm cơ của người khác chỉ bằng một quả cầu xoay thì hoàn toàn nằm ngoài k…

```text
Wide 16:9 landscape cinematic frame. a diagram of nerves sending electric signals to muscles, a spinning ball marked with a question mark. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Điểm độ thật: ba trên mười. Rung động và cộng hưởng là thật. Điều khiển cơ thể người khác là phần truyện phón…

```text
Wide 16:9 landscape cinematic frame. a score card showing 3 out of 10 with a vibrating wave icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Kiểm tra 5: Con ngựa và nhịp chạy hoàn hảo

Lời: Đây là chi tiết Kaku thích nhất. Truyện nói có một kỹ thuật nâng cao gọi là Xoay vàng: để con ngựa chạy đúng…

```text
Wide 16:9 landscape cinematic frame. a horse galloping at sunset with golden spiral patterns trailing from its hooves. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Theo truyện, năng lượng đó truyền qua bàn đạp yên ngựa lên cơ thể người cưỡi, rồi vào cánh tay và quả cầu thé…

```text
Wide 16:9 landscape cinematic frame. a diagram of energy flowing from a horse's stride up through the stirrups into a rider's arm. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Khoa học nói: điều bất ngờ là phần đầu có cơ sở thật. Ngựa có các dáng chạy khác nhau như đi bộ, chạy nước ki…

```text
Wide 16:9 landscape cinematic frame. three horse silhouettes showing walking, trotting and galloping gaits side by side. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Các nhà khoa học đã đo và thấy rằng trong mỗi dáng chạy, ngựa tự chọn một tốc độ tốn ít năng lượng nhất trên…

```text
Wide 16:9 landscape cinematic frame. a graph with three U-shaped curves, each with a glowing lowest point marked by a small horse icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Về lịch sử, bàn đạp yên ngựa đúng là một phát minh quan trọng, giúp người cưỡi đứng vững hơn khi chiến đấu tr…

```text
Wide 16:9 landscape cinematic frame. an antique iron stirrup on display in a museum case, soft spotlight. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Điểm độ thật: năm trên mười. Nhịp chạy tối ưu là thật, bàn đạp là thật. Nhưng biến bước chạy của ngựa thành l…

```text
Wide 16:9 landscape cinematic frame. a score card showing 5 out of 10 with a horseshoe icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Kiểm tra 6: Quả cầu thép có đủ sức?

Lời: Kiểm tra cuối: một quả cầu thép cỡ quả bóng tennis ném bằng tay có đủ sức làm vỡ đá hay xuyên qua vật cứng kh…

```text
Wide 16:9 landscape cinematic frame. a steel ball the size of a tennis ball next to a cracked boulder, a ruler for scale. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Khoa học nói: thép đặc nặng gần gấp tám lần nước, nên một quả cầu thép cỡ đó nặng hơn một ký, khoảng một phẩy…

```text
Wide 16:9 landscape cinematic frame. a scale weighing a steel ball, a small note showing about 1.2 kilograms. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nhưng làm vỡ đá cứng hay xuyên qua tường dày thì cần năng lượng lớn hơn nhiều. Cánh tay người khó ném một vật…

```text
Wide 16:9 landscape cinematic frame. a figure throwing a heavy ball with visible strain, the ball bouncing off a thick stone wall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Ở đây, truyện dùng lực xoay để bù vào phần thiếu. Và như ta đã thấy ở kiểm tra ba, xoay không tự tạo thêm năn…

```text
Wide 16:9 landscape cinematic frame. an energy bar chart comparing a throw, a spin, and the energy needed to break stone. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Điểm độ thật: bốn trên mười. Quả cầu thép là vũ khí nguy hiểm thật, nhưng những pha phá đá trong truyện đã đư…

```text
Wide 16:9 landscape cinematic frame. a score card showing 4 out of 10 with a steel ball icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Nếu Gyro là vận động viên thật

Lời: Thử một câu hỏi vui: nếu đưa Gyro vào thể thao thật, anh ấy sẽ đứng ở đâu?

```text
Wide 16:9 landscape cinematic frame. a steel ball resting on a modern sports field beside a baseball and a bowling ball. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Kỷ lục ném bóng chày nhanh nhất vào khoảng một trăm bảy mươi cây số một giờ, với quả bóng chỉ nặng khoảng một…

```text
Wide 16:9 landscape cinematic frame. a baseball blurring through the air with a speed gauge showing about 170 km/h. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Quả cầu thép của Gyro nặng gấp khoảng tám lần. Với cùng sức tay, vật càng nặng thì càng khó ném nhanh, nên tố…

```text
Wide 16:9 landscape cinematic frame. a balance scale with one baseball on one side and a steel ball outweighing eight baseballs on the other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nhưng về độ xoáy, người thật cũng rất đáng nể. Một cú ném bóng chày xoáy của vận động viên chuyên nghiệp có t…

```text
Wide 16:9 landscape cinematic frame. a curveball spinning with motion lines, a counter showing about 2500 rpm. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Và cũng như Gyro, những vận động viên đó không dựa vào sức mạnh thô. Họ luyện hàng nghìn giờ để kiểm soát từn…

```text
Wide 16:9 landscape cinematic frame. close-up of fingers gripping a ball along its seams, chalk dust in the air. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nên nếu hỏi Kaku, Gyro sẽ là một vận động viên ném bóng xoáy xuất sắc. Hoặc một cao thủ bowling mà không ai m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at a bowling alley holding a tiny steel ball, all pins already knocked down. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Điểm chung giữa truyện và đời thật là đây: độ xoáy là kỹ năng luyện được, không phải phép màu.

```text
Wide 16:9 landscape cinematic frame. a training ground at dusk with rows of practice balls and worn gloves. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Còn Stand thì sao?

Lời: Có thể bạn hỏi: JoJo nổi tiếng với Stand, vậy khoa học nói gì về Stand?

```text
Wide 16:9 landscape cinematic frame. a shadowy guardian spirit silhouette rising behind a person, glowing faintly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Câu trả lời ngắn: Stand là năng lực siêu nhiên, là hình ảnh của tinh thần con người. Nó không có cơ chế vật l…

```text
Wide 16:9 landscape cinematic frame. a translucent spirit figure with a big question mark where its engine would be. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Điều thú vị là Steel Ball Run đặt hai thứ cạnh nhau: Stand là sức mạnh của tinh thần, còn Xoay là sức mạnh củ…

```text
Wide 16:9 landscape cinematic frame. a split image: a glowing spirit on one side, a pair of hands training with steel balls on the other. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và theo truyện, hai thứ này có thể kết hợp với nhau. Chi tiết đó Kaku để dành, vì nó thuộc về những chặng đua…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding a glowing envelope behind its back, winking. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Bảng điểm độ thật

Lời: Giờ hãy đặt tất cả lên bảng điểm.

```text
Wide 16:9 landscape cinematic frame. a chalkboard with six rows and a score column, chalk dust in the air. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Xoay giúp vật ổn định và bay cong: chín điểm. Tỉ lệ vàng trong tự nhiên: sáu điểm. Nhịp chạy hoàn hảo của ngự…

```text
Wide 16:9 landscape cinematic frame. the top three rows of the chalkboard lighting up: 9, 6, 5. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Sức phá của quả cầu thép: bốn điểm. Xoay điều khiển cơ thể: ba điểm. Năng lượng vô hạn: một điểm.

```text
Wide 16:9 landscape cinematic frame. the bottom three rows lighting up: 4, 3, 1. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Trung bình khoảng bốn phẩy sáu trên mười. Với một bộ truyện có Stand và thánh tích bí ẩn, đây là con số rất đ…

```text
Wide 16:9 landscape cinematic frame. a large score of 4.6 out of 10 glowing at the bottom of the board with a small medal. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Điều đáng khen là tác giả không bịa ra một khái niệm hoàn toàn mới, mà lấy kiến thức thật làm nền rồi mới phó…

```text
Wide 16:9 landscape cinematic frame. a sturdy stone foundation with a fantastical tower rising on top of it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Góc nhìn của Kaku: vì sao lại là tỉ lệ vàng? · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao Araki chọn tỉ lệ vàng, chứ không phải một nguồn năng lượng thần bí nào đó?

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a golden spiral on a canvas in an art studio. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Araki là một họa sĩ rất yêu điêu khắc và hội họa cổ điển châu Âu. Tỉ lệ vàng từ lâu gắn với những cuộc bàn lu…

```text
Wide 16:9 landscape cinematic frame. a sculptor's studio with classical statues and sketches of proportions pinned to the wall. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nên trong Steel Ball Run, sức mạnh lớn nhất không đến từ cơn giận hay dòng máu, mà đến từ sự hài hòa với tự n…

```text
Wide 16:9 landscape cinematic frame. a rider and horse moving in perfect harmony through a golden meadow, spiral patterns in the grass. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Kỹ thuật Xoay cũng đòi hỏi luyện tập và quan sát, không có lối tắt. Nhân vật phải học cách nhìn thế giới trướ…

```text
Wide 16:9 landscape cinematic frame. a student carefully studying the curve of a leaf with a magnifying glass, a steel ball beside them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đó là thông điệp đẹp nhất của phần này: sự hoàn hảo không nằm ở sức mạnh, mà nằm ở cách ta quan sát…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting quietly in a meadow, watching a sunflower turn toward the sun. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Thử nghiệm tại nhà (an toàn)

Lời: Muốn tự thấy tỉ lệ vàng? Đây là hai thử nghiệm an toàn bạn làm được ngay.

```text
Wide 16:9 landscape cinematic frame. a desk with a sunflower, a ruler, a sheet of paper and colored pencils. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Thứ nhất: lấy một bông hướng dương hoặc một quả thông, đếm số đường xoắn theo chiều kim đồng hồ và ngược chiề…

```text
Wide 16:9 landscape cinematic frame. hands counting spirals on a pinecone, small numbers written on sticky notes. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Thứ hai: trên giấy kẻ ô, vẽ hai hình vuông cạnh một ô, rồi hình vuông cạnh hai, ba, năm, tám. Nối các góc bằn…

```text
Wide 16:9 landscape cinematic frame. graph paper with squares of sizes 1, 1, 2, 3, 5, 8 and a spiral drawn through them. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Còn ném cầu thép thì làm ơn đừng thử nhé. Kaku không muốn nhận bình luận về cửa kính nhà bạn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a sign with a crossed-out steel ball and a cracked window. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Tóm lại: tỉ lệ vàng và xoắn ốc vàng là toán học thật. Xoay giúp vật bay ổn định và bay cong là vật lý thật. N…

```text
Wide 16:9 landscape cinematic frame. a summary board with three green check marks next to small icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Còn năng lượng vô hạn và điều khiển cơ thể người khác là phần JoJo, nơi khoa học dừng lại và trí tưởng tượng…

```text
Wide 16:9 landscape cinematic frame. a road where solid pavement ends and a glowing golden spiral path continues into the sky. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: còn chi tiết nào trong anime mà bạn muốn Kaku mang thước và máy tính ra kiểm tra? Viết vào p…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a ruler and a calculator like a detective. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tới quay về thế giới phép thuật: Kaku sẽ mở hồ sơ các cuốn sách phép trong Black Clover, từ ba lá, bốn…

```text
Wide 16:9 landscape cinematic frame. an old grimoire with a glowing clover emblem on its cover, resting on a stone pedestal. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy đăng ký kênh nếu bạn thấy video thú vị. Kaku tháo kính bảo hộ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off tiny safety goggles and waving in a sunny lab. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Bối cảnh: cuộc đua xuyên nước Mỹ

Khoảng 113 giây · cảnh s01–s10 · 1467 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler nhẹ JoJo Steel Ball Run, tới khoảng chặng thứ ba của cuộc đua. Các cấp độ sức mạnh về sau, Kaku sẽ không nhắc tới.

<short pause> Một quả cầu thép xoay trong lòng bàn tay. Nó không phát sáng, không có năng lượng thần bí, chỉ xoay. <short pause> Nhưng khi ném ra, nó có thể làm những điều mà phép thuật cũng phải ghen tị.

<short pause> Và bí quyết của nó, theo truyện, là một con số: một phẩy sáu một tám. Tỉ lệ vàng.

<short pause> <laugh> Hôm nay Kaku không giải thích như mọi khi. Kaku sẽ mang thước kẻ, máy tính và sách vật lý ra, để hỏi một câu thôi: điều này có thật không?

<short pause> Mở sổ ra nào! Mình là Kaku. Mỗi chương hôm nay sẽ có ba bước: truyện nói gì, khoa học nói gì, và truyện đã phóng tay tới đâu. Cuối mỗi chương là điểm độ thật, từ không tới mười.

<short pause> Steel Ball Run là phần thứ bảy của loạt JoJo, do Araki Hirohiko sáng tác. Câu chuyện bắt đầu năm 1890 với một cuộc đua ngựa xuyên nước Mỹ.

<short pause> Hàng nghìn tay đua xuất phát từ bờ biển phía tây, đích đến là New York, cách khoảng sáu nghìn cây số. Người thắng nhận giải thưởng khổng lồ.

<short pause> Trong số đó có hai nhân vật chính: Gyro, một người đàn ông đến từ nước Ý với hai quả cầu thép, và Johnny, một cựu nài ngựa bị liệt đôi chân.

<short pause> Trong tập đầu, Johnny vô tình chạm vào quả cầu đang xoay của Gyro, và đôi chân đã liệt của anh bỗng cử động trong giây lát. Từ đó anh quyết theo Gyro để tìm hiểu bí mật của kỹ thuật Xoay.

<short pause> Kaku ghi chú: đây là bộ JoJo mà nhiều fan đánh giá cao nhất. Bản anime phát tập đầu trên Netflix tháng 3 năm 2026, và phát hằng tuần từ cuối tháng 9.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler nhẹ JoJo Steel Ball Run, tới khoảng chặng thứ ba của cuộc đua. Các cấp độ sức mạnh về sau, Kaku sẽ không nhắc tới.

[pause] Một quả cầu thép xoay trong lòng bàn tay. Nó không phát sáng, không có năng lượng thần bí, chỉ xoay. [pause] Nhưng khi ném ra, nó có thể làm những điều mà phép thuật cũng phải ghen tị.

[pause] Và bí quyết của nó, theo truyện, là một con số: một phẩy sáu một tám. Tỉ lệ vàng.

[pause] [chuckles] Hôm nay Kaku không giải thích như mọi khi. [curious] Kaku sẽ mang thước kẻ, máy tính và sách vật lý ra, để hỏi một câu thôi: điều này có thật không?

[pause] Mở sổ ra nào! Mình là Kaku. Mỗi chương hôm nay sẽ có ba bước: truyện nói gì, khoa học nói gì, và truyện đã phóng tay tới đâu. Cuối mỗi chương là điểm độ thật, từ không tới mười.

[pause] Steel Ball Run là phần thứ bảy của loạt JoJo, do Araki Hirohiko sáng tác. Câu chuyện bắt đầu năm 1890 với một cuộc đua ngựa xuyên nước Mỹ.

[pause] Hàng nghìn tay đua xuất phát từ bờ biển phía tây, đích đến là New York, cách khoảng sáu nghìn cây số. Người thắng nhận giải thưởng khổng lồ.

[pause] Trong số đó có hai nhân vật chính: Gyro, một người đàn ông đến từ nước Ý với hai quả cầu thép, và Johnny, một cựu nài ngựa bị liệt đôi chân.

[pause] Trong tập đầu, Johnny vô tình chạm vào quả cầu đang xoay của Gyro, và đôi chân đã liệt của anh bỗng cử động trong giây lát. Từ đó anh quyết theo Gyro để tìm hiểu bí mật của kỹ thuật Xoay.

[pause] Kaku ghi chú: đây là bộ JoJo mà nhiều fan đánh giá cao nhất. Bản anime phát tập đầu trên Netflix tháng 3 năm 2026, và phát hằng tuần từ cuối tháng 9.
```

### c02 · Kỹ thuật Xoay là gì? / Tỉ lệ vàng là gì?

Khoảng 116 giây · cảnh s11–s21 · 1504 ký tự

**Gemini**

```text
Theo truyện, Xoay là kỹ thuật được truyền lại trong gia tộc của Gyro qua nhiều thế hệ. Nó được dùng trong y thuật, và cả trong nghề hành hình của gia tộc.

<short pause> Người dùng xoay một vật, thường là quả cầu thép, với độ chính xác cực cao. Khi chạm vào mục tiêu, lực xoay truyền vào và gây ra đủ loại hiệu ứng.

<short pause> Nó có thể làm vỡ vật cứng, làm cơ bắp co giật, làm da chuyển động, và thậm chí điều khiển cơ thể người khác trong thời gian ngắn.

<short pause> Nhưng Xoay chỉ mạnh khi đủ hoàn hảo. Và theo truyện, thước đo của sự hoàn hảo đó là hình chữ nhật vàng.

<short pause> Vậy để kiểm tra Xoay, trước hết ta phải hiểu tỉ lệ vàng là gì. Đi thôi!

<short pause> Tỉ lệ vàng là một con số, xấp xỉ một phẩy sáu một tám. Người ta thường viết nó bằng chữ cái Hy Lạp phi.

<short pause> Định nghĩa rất gọn: chia một đoạn thẳng thành hai phần, sao cho cả đoạn chia cho phần dài bằng đúng phần dài chia cho phần ngắn. Tỉ số đó chính là phi.

<short pause> Hình chữ nhật vàng là hình chữ nhật có cạnh dài gấp phi lần cạnh ngắn. Nó có một tính chất kỳ diệu: cắt đi một hình vuông, phần còn lại lại là một hình chữ nhật vàng nhỏ hơn.

<short pause> Cứ cắt mãi như vậy, bạn được vô số hình vuông nhỏ dần. Nối các góc của chúng bằng những cung tròn, ta có xoắn ốc vàng, một đường xoắn không bao giờ kết thúc về mặt toán học.

<short pause> Đây là chỗ truyện lấy ý tưởng: một vòng xoay đi theo xoắn ốc vô tận thì cũng có thể tạo ra năng lượng vô tận. Nghe rất hay. <short pause> Nhưng khoa học có đồng ý không?

<short pause> <laugh> Kaku ghi chú: phần toán học ở trên là hoàn toàn đúng. Tỉ lệ vàng và xoắn ốc vàng là kiến thức toán học thật, học sinh phổ thông cũng có thể tự vẽ.
```

**ElevenLabs**

```text
Theo truyện, Xoay là kỹ thuật được truyền lại trong gia tộc của Gyro qua nhiều thế hệ. Nó được dùng trong y thuật, và cả trong nghề hành hình của gia tộc.

[pause] Người dùng xoay một vật, thường là quả cầu thép, với độ chính xác cực cao. Khi chạm vào mục tiêu, lực xoay truyền vào và gây ra đủ loại hiệu ứng.

[pause] Nó có thể làm vỡ vật cứng, làm cơ bắp co giật, làm da chuyển động, và thậm chí điều khiển cơ thể người khác trong thời gian ngắn.

[pause] Nhưng Xoay chỉ mạnh khi đủ hoàn hảo. Và theo truyện, thước đo của sự hoàn hảo đó là hình chữ nhật vàng.

[pause] Vậy để kiểm tra Xoay, trước hết ta phải hiểu tỉ lệ vàng là gì. Đi thôi!

[pause] Tỉ lệ vàng là một con số, xấp xỉ một phẩy sáu một tám. Người ta thường viết nó bằng chữ cái Hy Lạp phi.

[pause] Định nghĩa rất gọn: chia một đoạn thẳng thành hai phần, sao cho cả đoạn chia cho phần dài bằng đúng phần dài chia cho phần ngắn. Tỉ số đó chính là phi.

[pause] Hình chữ nhật vàng là hình chữ nhật có cạnh dài gấp phi lần cạnh ngắn. Nó có một tính chất kỳ diệu: cắt đi một hình vuông, phần còn lại lại là một hình chữ nhật vàng nhỏ hơn.

[pause] Cứ cắt mãi như vậy, bạn được vô số hình vuông nhỏ dần. Nối các góc của chúng bằng những cung tròn, ta có xoắn ốc vàng, một đường xoắn không bao giờ kết thúc về mặt toán học.

[pause] Đây là chỗ truyện lấy ý tưởng: một vòng xoay đi theo xoắn ốc vô tận thì cũng có thể tạo ra năng lượng vô tận. Nghe rất hay. [pause] [curious] Nhưng khoa học có đồng ý không?

[pause] [chuckles] Kaku ghi chú: phần toán học ở trên là hoàn toàn đúng. Tỉ lệ vàng và xoắn ốc vàng là kiến thức toán học thật, học sinh phổ thông cũng có thể tự vẽ.
```

### c03 · Kiểm tra 1: Tỉ lệ vàng có mặt khắp tự nhiên? / Kiểm tra 2: Vật xoay có ổn định hơn?

Khoảng 137 giây · cảnh s22–s33 · 1787 ký tự

**Gemini**

```text
Truyện nói: tỉ lệ vàng có mặt trong tự nhiên, và người dùng Xoay học theo tự nhiên để xoay hoàn hảo hơn. Đây là một ý tưởng rất phổ biến, cả ngoài đời lẫn trên mạng.

<short pause> Khoa học nói: có những chỗ đúng thật. Hạt hướng dương và vảy quả thông xếp theo các đường xoắn, và số đường xoắn thường là các số Fibonacci liền nhau, như ba mươi bốn và năm mươi lăm.

<short pause> Lý do là mỗi hạt mới mọc lệch hạt trước một góc khoảng một trăm ba mươi bảy phẩy năm độ, gọi là góc vàng. Góc này giúp hạt xếp khít nhất mà không chồng lên nhau.

<short pause> Nhưng cũng có nhiều chỗ bị thổi phồng. Vỏ ốc anh vũ là một đường xoắn ốc thật, nhưng các phép đo cho thấy tỉ lệ của nó thường không phải tỉ lệ vàng.

<short pause> Tương tự, những khẳng định kiểu khuôn mặt đẹp hay công trình cổ được xây theo đúng tỉ lệ vàng thường thiếu bằng chứng chặt chẽ.

<short pause> Điểm độ thật cho kiểm tra này: sáu trên mười. Tỉ lệ vàng có mặt trong tự nhiên thật, nhưng không có mặt ở khắp nơi như người ta thường nói.

<short pause> Truyện nói: quả cầu xoay càng chuẩn thì càng mạnh và càng khó bị chặn lại. Hãy thử kiểm tra phần đầu: xoay có làm vật ổn định hơn không?

<short pause> Khoa học nói: có, và rất rõ ràng. Một vật đang xoay có mô men động lượng, và nó chống lại việc bị đổi hướng trục xoay. Đó là lý do con quay đứng vững khi xoay, nhưng đổ ngay khi dừng.

<short pause> Nòng súng trường có rãnh xoắn để làm viên đạn xoay khi bay ra, giúp nó bay thẳng và ổn định hơn. Người ném bóng bầu dục cũng xoáy bóng vì lý do tương tự.

<short pause> Xoay còn làm đường bay cong đi. Trái bóng xoáy trong bóng đá bẻ cong quỹ đạo nhờ hiệu ứng Magnus, khi không khí bị kéo lệch ở hai bên quả bóng.

<short pause> Trong truyện, Gyro thường ném quả cầu theo những quỹ đạo cong khó đoán. Về nguyên lý, điều này hoàn toàn có cơ sở.

<short pause> Điểm độ thật: chín trên mười. Xoay giúp vật ổn định và bay cong là vật lý chuẩn. Chỉ có mức độ chính xác trong truyện là hơi siêu phàm.
```

**ElevenLabs**

```text
Truyện nói: tỉ lệ vàng có mặt trong tự nhiên, và người dùng Xoay học theo tự nhiên để xoay hoàn hảo hơn. Đây là một ý tưởng rất phổ biến, cả ngoài đời lẫn trên mạng.

[pause] Khoa học nói: có những chỗ đúng thật. Hạt hướng dương và vảy quả thông xếp theo các đường xoắn, và số đường xoắn thường là các số Fibonacci liền nhau, như ba mươi bốn và năm mươi lăm.

[pause] Lý do là mỗi hạt mới mọc lệch hạt trước một góc khoảng một trăm ba mươi bảy phẩy năm độ, gọi là góc vàng. Góc này giúp hạt xếp khít nhất mà không chồng lên nhau.

[pause] Nhưng cũng có nhiều chỗ bị thổi phồng. Vỏ ốc anh vũ là một đường xoắn ốc thật, nhưng các phép đo cho thấy tỉ lệ của nó thường không phải tỉ lệ vàng.

[pause] Tương tự, những khẳng định kiểu khuôn mặt đẹp hay công trình cổ được xây theo đúng tỉ lệ vàng thường thiếu bằng chứng chặt chẽ.

[pause] Điểm độ thật cho kiểm tra này: sáu trên mười. Tỉ lệ vàng có mặt trong tự nhiên thật, nhưng không có mặt ở khắp nơi như người ta thường nói.

[pause] Truyện nói: quả cầu xoay càng chuẩn thì càng mạnh và càng khó bị chặn lại. [curious] Hãy thử kiểm tra phần đầu: xoay có làm vật ổn định hơn không?

[pause] Khoa học nói: có, và rất rõ ràng. Một vật đang xoay có mô men động lượng, và nó chống lại việc bị đổi hướng trục xoay. Đó là lý do con quay đứng vững khi xoay, nhưng đổ ngay khi dừng.

[pause] Nòng súng trường có rãnh xoắn để làm viên đạn xoay khi bay ra, giúp nó bay thẳng và ổn định hơn. Người ném bóng bầu dục cũng xoáy bóng vì lý do tương tự.

[pause] Xoay còn làm đường bay cong đi. Trái bóng xoáy trong bóng đá bẻ cong quỹ đạo nhờ hiệu ứng Magnus, khi không khí bị kéo lệch ở hai bên quả bóng.

[pause] Trong truyện, Gyro thường ném quả cầu theo những quỹ đạo cong khó đoán. Về nguyên lý, điều này hoàn toàn có cơ sở.

[pause] Điểm độ thật: chín trên mười. Xoay giúp vật ổn định và bay cong là vật lý chuẩn. Chỉ có mức độ chính xác trong truyện là hơi siêu phàm.
```

### c04 · Kiểm tra 3: Năng lượng xoay vô hạn? / Kiểm tra 4: Xoay truyền qua cơ thể

Khoảng 140 giây · cảnh s34–s45 · 1814 ký tự

**Gemini**

```text
Đây là tuyên bố lớn nhất: vòng xoay đi theo xoắn ốc vàng có thể tạo ra năng lượng gần như vô tận.

<short pause> Khoa học nói: một vật đang xoay đúng là tích trữ năng lượng. Năng lượng đó phụ thuộc vào khối lượng, cách phân bố khối lượng và tốc độ xoay.

<short pause> Người ta còn dùng bánh đà, một khối nặng xoay rất nhanh, để trữ năng lượng trong một số hệ thống điện và máy móc. Nên ý tưởng quả cầu xoay mang năng lượng là có thật.

<short pause> Nhưng năng lượng vô hạn thì không. Định luật bảo toàn năng lượng nói rằng năng lượng không tự sinh ra. Và ma sát, sức cản không khí luôn lấy dần năng lượng của vật xoay.

<short pause> Một đường xoắn ốc vô tận trên giấy chỉ là hình học. Hình dạng của chuyển động không thể tự tạo ra năng lượng. Nếu làm được, con người đã có máy chuyển động vĩnh cửu từ lâu.

<short pause> Điểm độ thật: một trên mười. Một điểm cho ý tưởng vật xoay tích trữ năng lượng. Phần vô hạn là trí tưởng tượng thuần túy, nhưng là trí tưởng tượng rất đẹp.

<short pause> <laugh> Kaku ghi chú: đừng buồn nhé. Chính truyện cũng coi vòng xoay vô tận là thứ gần như không thể đạt được, và điều đó làm nó quý giá.

<short pause> Truyện nói: lực xoay có thể truyền qua da và cơ bắp, làm cơ co giật hay khiến cơ thể cử động ngoài ý muốn.

<short pause> Khoa học nói: rung động có thể lan truyền qua cơ thể thật. Y học dùng rung động và sóng âm trong nhiều việc, như siêu âm để chụp hình bên trong cơ thể, hay máy rung để thư giãn cơ.

<short pause> Cộng hưởng là một hiện tượng có thật khác: khi rung đúng tần số tự nhiên, một vật có thể dao động rất mạnh. Ví dụ quen thuộc là ly thủy tinh bị vỡ bởi âm thanh đúng tần số.

<short pause> Nhưng để điều khiển chính xác từng nhóm cơ của người khác chỉ bằng một quả cầu xoay thì hoàn toàn nằm ngoài khoa học hiện nay. Cơ bắp được điều khiển bằng tín hiệu thần kinh, không phải bằng lực xoay từ bên ngoài.

<short pause> Điểm độ thật: ba trên mười. Rung động và cộng hưởng là thật. Điều khiển cơ thể người khác là phần truyện phóng tay.
```

**ElevenLabs**

```text
Đây là tuyên bố lớn nhất: vòng xoay đi theo xoắn ốc vàng có thể tạo ra năng lượng gần như vô tận.

[pause] Khoa học nói: một vật đang xoay đúng là tích trữ năng lượng. Năng lượng đó phụ thuộc vào khối lượng, cách phân bố khối lượng và tốc độ xoay.

[pause] Người ta còn dùng bánh đà, một khối nặng xoay rất nhanh, để trữ năng lượng trong một số hệ thống điện và máy móc. Nên ý tưởng quả cầu xoay mang năng lượng là có thật.

[pause] Nhưng năng lượng vô hạn thì không. Định luật bảo toàn năng lượng nói rằng năng lượng không tự sinh ra. Và ma sát, sức cản không khí luôn lấy dần năng lượng của vật xoay.

[pause] Một đường xoắn ốc vô tận trên giấy chỉ là hình học. Hình dạng của chuyển động không thể tự tạo ra năng lượng. Nếu làm được, con người đã có máy chuyển động vĩnh cửu từ lâu.

[pause] Điểm độ thật: một trên mười. Một điểm cho ý tưởng vật xoay tích trữ năng lượng. Phần vô hạn là trí tưởng tượng thuần túy, nhưng là trí tưởng tượng rất đẹp.

[pause] [chuckles] Kaku ghi chú: đừng buồn nhé. Chính truyện cũng coi vòng xoay vô tận là thứ gần như không thể đạt được, và điều đó làm nó quý giá.

[pause] Truyện nói: lực xoay có thể truyền qua da và cơ bắp, làm cơ co giật hay khiến cơ thể cử động ngoài ý muốn.

[pause] Khoa học nói: rung động có thể lan truyền qua cơ thể thật. Y học dùng rung động và sóng âm trong nhiều việc, như siêu âm để chụp hình bên trong cơ thể, hay máy rung để thư giãn cơ.

[pause] Cộng hưởng là một hiện tượng có thật khác: khi rung đúng tần số tự nhiên, một vật có thể dao động rất mạnh. Ví dụ quen thuộc là ly thủy tinh bị vỡ bởi âm thanh đúng tần số.

[pause] Nhưng để điều khiển chính xác từng nhóm cơ của người khác chỉ bằng một quả cầu xoay thì hoàn toàn nằm ngoài khoa học hiện nay. Cơ bắp được điều khiển bằng tín hiệu thần kinh, không phải bằng lực xoay từ bên ngoài.

[pause] Điểm độ thật: ba trên mười. Rung động và cộng hưởng là thật. Điều khiển cơ thể người khác là phần truyện phóng tay.
```

### c05 · Kiểm tra 5: Con ngựa và nhịp chạy hoàn hảo / Kiểm tra 6: Quả cầu thép có đủ sức?

Khoảng 127 giây · cảnh s46–s56 · 1646 ký tự

**Gemini**

```text
Đây là chi tiết Kaku thích nhất. Truyện nói có một kỹ thuật nâng cao gọi là Xoay vàng: để con ngựa chạy đúng nhịp tự nhiên nhất của nó, năng lượng từ bước chạy sẽ tạo ra lực xoay hoàn hảo.

<short pause> Theo truyện, năng lượng đó truyền qua bàn đạp yên ngựa lên cơ thể người cưỡi, rồi vào cánh tay và quả cầu thép.

<short pause> Khoa học nói: điều bất ngờ là phần đầu có cơ sở thật. Ngựa có các dáng chạy khác nhau như đi bộ, chạy nước kiệu và phi nước đại.

<short pause> Các nhà khoa học đã đo và thấy rằng trong mỗi dáng chạy, ngựa tự chọn một tốc độ tốn ít năng lượng nhất trên mỗi mét đường. Tức là thật sự có một nhịp chạy tự nhiên hiệu quả nhất.

<short pause> Về lịch sử, bàn đạp yên ngựa đúng là một phát minh quan trọng, giúp người cưỡi đứng vững hơn khi chiến đấu trên lưng ngựa. Còn chuyện kỹ thuật Xoay được phát minh cùng bàn đạp chỉ là lịch sử trong truyện.

<short pause> Điểm độ thật: năm trên mười. Nhịp chạy tối ưu là thật, bàn đạp là thật. <short pause> Nhưng biến bước chạy của ngựa thành lực xoay ném ra từ tay thì là JoJo.

<short pause> Kiểm tra cuối: một quả cầu thép cỡ quả bóng tennis ném bằng tay có đủ sức làm vỡ đá hay xuyên qua vật cứng không?

<short pause> Khoa học nói: thép đặc nặng gần gấp tám lần nước, nên một quả cầu thép cỡ đó nặng hơn một ký, khoảng một phẩy hai ký. Ném mạnh, nó mang động năng đáng kể, đủ gây sát thương nghiêm trọng.

<short pause> Nhưng làm vỡ đá cứng hay xuyên qua tường dày thì cần năng lượng lớn hơn nhiều. Cánh tay người khó ném một vật hơn một ký đủ nhanh để làm điều đó.

<short pause> Ở đây, truyện dùng lực xoay để bù vào phần thiếu. Và như ta đã thấy ở kiểm tra ba, xoay không tự tạo thêm năng lượng.

<short pause> Điểm độ thật: bốn trên mười. Quả cầu thép là vũ khí nguy hiểm thật, nhưng những pha phá đá trong truyện đã được phóng đại nhiều lần.
```

**ElevenLabs**

```text
Đây là chi tiết Kaku thích nhất. Truyện nói có một kỹ thuật nâng cao gọi là Xoay vàng: để con ngựa chạy đúng nhịp tự nhiên nhất của nó, năng lượng từ bước chạy sẽ tạo ra lực xoay hoàn hảo.

[pause] Theo truyện, năng lượng đó truyền qua bàn đạp yên ngựa lên cơ thể người cưỡi, rồi vào cánh tay và quả cầu thép.

[pause] Khoa học nói: điều bất ngờ là phần đầu có cơ sở thật. Ngựa có các dáng chạy khác nhau như đi bộ, chạy nước kiệu và phi nước đại.

[pause] Các nhà khoa học đã đo và thấy rằng trong mỗi dáng chạy, ngựa tự chọn một tốc độ tốn ít năng lượng nhất trên mỗi mét đường. Tức là thật sự có một nhịp chạy tự nhiên hiệu quả nhất.

[pause] Về lịch sử, bàn đạp yên ngựa đúng là một phát minh quan trọng, giúp người cưỡi đứng vững hơn khi chiến đấu trên lưng ngựa. Còn chuyện kỹ thuật Xoay được phát minh cùng bàn đạp chỉ là lịch sử trong truyện.

[pause] Điểm độ thật: năm trên mười. Nhịp chạy tối ưu là thật, bàn đạp là thật. [pause] Nhưng biến bước chạy của ngựa thành lực xoay ném ra từ tay thì là JoJo.

[pause] [curious] Kiểm tra cuối: một quả cầu thép cỡ quả bóng tennis ném bằng tay có đủ sức làm vỡ đá hay xuyên qua vật cứng không?

[pause] Khoa học nói: thép đặc nặng gần gấp tám lần nước, nên một quả cầu thép cỡ đó nặng hơn một ký, khoảng một phẩy hai ký. Ném mạnh, nó mang động năng đáng kể, đủ gây sát thương nghiêm trọng.

[pause] Nhưng làm vỡ đá cứng hay xuyên qua tường dày thì cần năng lượng lớn hơn nhiều. Cánh tay người khó ném một vật hơn một ký đủ nhanh để làm điều đó.

[pause] Ở đây, truyện dùng lực xoay để bù vào phần thiếu. Và như ta đã thấy ở kiểm tra ba, xoay không tự tạo thêm năng lượng.

[pause] Điểm độ thật: bốn trên mười. Quả cầu thép là vũ khí nguy hiểm thật, nhưng những pha phá đá trong truyện đã được phóng đại nhiều lần.
```

### c06 · Nếu Gyro là vận động viên thật / Còn Stand thì sao? / Bảng điểm độ thật

Khoảng 138 giây · cảnh s57–s72 · 1788 ký tự

**Gemini**

```text
Thử một câu hỏi vui: nếu đưa Gyro vào thể thao thật, anh ấy sẽ đứng ở đâu?

<short pause> Kỷ lục ném bóng chày nhanh nhất vào khoảng một trăm bảy mươi cây số một giờ, với quả bóng chỉ nặng khoảng một trăm bốn mươi lăm gram.

<short pause> Quả cầu thép của Gyro nặng gấp khoảng tám lần. Với cùng sức tay, vật càng nặng thì càng khó ném nhanh, nên tốc độ thật của nó sẽ thấp hơn nhiều.

<short pause> Nhưng về độ xoáy, người thật cũng rất đáng nể. Một cú ném bóng chày xoáy của vận động viên chuyên nghiệp có thể đạt khoảng hai nghìn năm trăm vòng mỗi phút.

<short pause> Và cũng như Gyro, những vận động viên đó không dựa vào sức mạnh thô. Họ luyện hàng nghìn giờ để kiểm soát từng ngón tay khi thả bóng.

<short pause> <laugh> Nên nếu hỏi Kaku, Gyro sẽ là một vận động viên ném bóng xoáy xuất sắc. Hoặc một cao thủ bowling mà không ai muốn đấu cùng.

<short pause> Điểm chung giữa truyện và đời thật là đây: độ xoáy là kỹ năng luyện được, không phải phép màu.

<short pause> Có thể bạn hỏi: JoJo nổi tiếng với Stand, vậy khoa học nói gì về Stand?

<short pause> Câu trả lời ngắn: Stand là năng lực siêu nhiên, là hình ảnh của tinh thần con người. Nó không có cơ chế vật lý nào để kiểm tra.

<short pause> Điều thú vị là Steel Ball Run đặt hai thứ cạnh nhau: Stand là sức mạnh của tinh thần, còn Xoay là sức mạnh của kỹ thuật và luyện tập.

<short pause> Và theo truyện, hai thứ này có thể kết hợp với nhau. Chi tiết đó Kaku để dành, vì nó thuộc về những chặng đua sau.

<short pause> Giờ hãy đặt tất cả lên bảng điểm.

<short pause> Xoay giúp vật ổn định và bay cong: chín điểm. Tỉ lệ vàng trong tự nhiên: sáu điểm. Nhịp chạy hoàn hảo của ngựa: năm điểm.

<short pause> Sức phá của quả cầu thép: bốn điểm. Xoay điều khiển cơ thể: ba điểm. Năng lượng vô hạn: một điểm.

<short pause> Trung bình khoảng bốn phẩy sáu trên mười. Với một bộ truyện có Stand và thánh tích bí ẩn, đây là con số rất đáng nể.

<short pause> Điều đáng khen là tác giả không bịa ra một khái niệm hoàn toàn mới, mà lấy kiến thức thật làm nền rồi mới phóng đại lên.
```

**ElevenLabs**

```text
[curious] Thử một câu hỏi vui: nếu đưa Gyro vào thể thao thật, anh ấy sẽ đứng ở đâu?

[pause] Kỷ lục ném bóng chày nhanh nhất vào khoảng một trăm bảy mươi cây số một giờ, với quả bóng chỉ nặng khoảng một trăm bốn mươi lăm gram.

[pause] Quả cầu thép của Gyro nặng gấp khoảng tám lần. Với cùng sức tay, vật càng nặng thì càng khó ném nhanh, nên tốc độ thật của nó sẽ thấp hơn nhiều.

[pause] Nhưng về độ xoáy, người thật cũng rất đáng nể. Một cú ném bóng chày xoáy của vận động viên chuyên nghiệp có thể đạt khoảng hai nghìn năm trăm vòng mỗi phút.

[pause] Và cũng như Gyro, những vận động viên đó không dựa vào sức mạnh thô. Họ luyện hàng nghìn giờ để kiểm soát từng ngón tay khi thả bóng.

[pause] [chuckles] Nên nếu hỏi Kaku, Gyro sẽ là một vận động viên ném bóng xoáy xuất sắc. Hoặc một cao thủ bowling mà không ai muốn đấu cùng.

[pause] Điểm chung giữa truyện và đời thật là đây: độ xoáy là kỹ năng luyện được, không phải phép màu.

[pause] Có thể bạn hỏi: JoJo nổi tiếng với Stand, vậy khoa học nói gì về Stand?

[pause] Câu trả lời ngắn: Stand là năng lực siêu nhiên, là hình ảnh của tinh thần con người. Nó không có cơ chế vật lý nào để kiểm tra.

[pause] Điều thú vị là Steel Ball Run đặt hai thứ cạnh nhau: Stand là sức mạnh của tinh thần, còn Xoay là sức mạnh của kỹ thuật và luyện tập.

[pause] Và theo truyện, hai thứ này có thể kết hợp với nhau. Chi tiết đó Kaku để dành, vì nó thuộc về những chặng đua sau.

[pause] Giờ hãy đặt tất cả lên bảng điểm.

[pause] Xoay giúp vật ổn định và bay cong: chín điểm. Tỉ lệ vàng trong tự nhiên: sáu điểm. Nhịp chạy hoàn hảo của ngựa: năm điểm.

[pause] Sức phá của quả cầu thép: bốn điểm. Xoay điều khiển cơ thể: ba điểm. Năng lượng vô hạn: một điểm.

[pause] Trung bình khoảng bốn phẩy sáu trên mười. Với một bộ truyện có Stand và thánh tích bí ẩn, đây là con số rất đáng nể.

[pause] Điều đáng khen là tác giả không bịa ra một khái niệm hoàn toàn mới, mà lấy kiến thức thật làm nền rồi mới phóng đại lên.
```

### c07 · Góc nhìn của Kaku: vì sao lại là tỉ lệ vàng? / Thử nghiệm tại nhà (an toàn) / Kết

Khoảng 134 giây · cảnh s73–s86 · 1748 ký tự

**Gemini**

```text
Vì sao Araki chọn tỉ lệ vàng, chứ không phải một nguồn năng lượng thần bí nào đó?

<short pause> Araki là một họa sĩ rất yêu điêu khắc và hội họa cổ điển châu Âu. Tỉ lệ vàng từ lâu gắn với những cuộc bàn luận về vẻ đẹp và sự cân đối trong nghệ thuật.

<short pause> Nên trong Steel Ball Run, sức mạnh lớn nhất không đến từ cơn giận hay dòng máu, mà đến từ sự hài hòa với tự nhiên, như một họa sĩ tìm ra tỉ lệ đẹp nhất.

<short pause> Kỹ thuật Xoay cũng đòi hỏi luyện tập và quan sát, không có lối tắt. Nhân vật phải học cách nhìn thế giới trước, rồi mới xoay được.

<short pause> <laugh> Kaku nghĩ đó là thông điệp đẹp nhất của phần này: sự hoàn hảo không nằm ở sức mạnh, mà nằm ở cách ta quan sát và hòa hợp với thế giới.

<short pause> Muốn tự thấy tỉ lệ vàng? Đây là hai thử nghiệm an toàn bạn làm được ngay.

<short pause> Thứ nhất: lấy một bông hướng dương hoặc một quả thông, đếm số đường xoắn theo chiều kim đồng hồ và ngược chiều. Rất có thể bạn sẽ được hai số Fibonacci liền nhau.

<short pause> Thứ hai: trên giấy kẻ ô, vẽ hai hình vuông cạnh một ô, rồi hình vuông cạnh hai, ba, năm, tám. Nối các góc bằng cung tròn, bạn sẽ có một xoắn ốc rất gần xoắn ốc vàng.

<short pause> Còn ném cầu thép thì làm ơn đừng thử nhé. Kaku không muốn nhận bình luận về cửa kính nhà bạn.

<short pause> Tóm lại: tỉ lệ vàng và xoắn ốc vàng là toán học thật. Xoay giúp vật bay ổn định và bay cong là vật lý thật. Ngựa có nhịp chạy tối ưu cũng là khoa học thật.

<short pause> Còn năng lượng vô hạn và điều khiển cơ thể người khác là phần JoJo, nơi khoa học dừng lại và trí tưởng tượng bắt đầu.

<short pause> Câu hỏi cho bạn: còn chi tiết nào trong anime mà bạn muốn Kaku mang thước và máy tính ra kiểm tra? Viết vào phần bình luận nhé.

<short pause> Video tới quay về thế giới phép thuật: Kaku sẽ mở hồ sơ các cuốn sách phép trong Black Clover, từ ba lá, bốn lá đến năm lá.

<short pause> Hãy đăng ký kênh nếu bạn thấy video thú vị. Kaku tháo kính bảo hộ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Vì sao Araki chọn tỉ lệ vàng, chứ không phải một nguồn năng lượng thần bí nào đó?

[pause] Araki là một họa sĩ rất yêu điêu khắc và hội họa cổ điển châu Âu. Tỉ lệ vàng từ lâu gắn với những cuộc bàn luận về vẻ đẹp và sự cân đối trong nghệ thuật.

[pause] Nên trong Steel Ball Run, sức mạnh lớn nhất không đến từ cơn giận hay dòng máu, mà đến từ sự hài hòa với tự nhiên, như một họa sĩ tìm ra tỉ lệ đẹp nhất.

[pause] Kỹ thuật Xoay cũng đòi hỏi luyện tập và quan sát, không có lối tắt. Nhân vật phải học cách nhìn thế giới trước, rồi mới xoay được.

[pause] [chuckles] Kaku nghĩ đó là thông điệp đẹp nhất của phần này: sự hoàn hảo không nằm ở sức mạnh, mà nằm ở cách ta quan sát và hòa hợp với thế giới.

[pause] Muốn tự thấy tỉ lệ vàng? Đây là hai thử nghiệm an toàn bạn làm được ngay.

[pause] Thứ nhất: lấy một bông hướng dương hoặc một quả thông, đếm số đường xoắn theo chiều kim đồng hồ và ngược chiều. Rất có thể bạn sẽ được hai số Fibonacci liền nhau.

[pause] Thứ hai: trên giấy kẻ ô, vẽ hai hình vuông cạnh một ô, rồi hình vuông cạnh hai, ba, năm, tám. Nối các góc bằng cung tròn, bạn sẽ có một xoắn ốc rất gần xoắn ốc vàng.

[pause] Còn ném cầu thép thì làm ơn đừng thử nhé. Kaku không muốn nhận bình luận về cửa kính nhà bạn.

[pause] Tóm lại: tỉ lệ vàng và xoắn ốc vàng là toán học thật. Xoay giúp vật bay ổn định và bay cong là vật lý thật. Ngựa có nhịp chạy tối ưu cũng là khoa học thật.

[pause] Còn năng lượng vô hạn và điều khiển cơ thể người khác là phần JoJo, nơi khoa học dừng lại và trí tưởng tượng bắt đầu.

[pause] Câu hỏi cho bạn: còn chi tiết nào trong anime mà bạn muốn Kaku mang thước và máy tính ra kiểm tra? Viết vào phần bình luận nhé.

[pause] Video tới quay về thế giới phép thuật: Kaku sẽ mở hồ sơ các cuốn sách phép trong Black Clover, từ ba lá, bốn lá đến năm lá.

[pause] Hãy đăng ký kênh nếu bạn thấy video thú vị. Kaku tháo kính bảo hộ đây, hẹn gặp lại!
```
