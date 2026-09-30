# Bộ prompt · Chakra vs Nen vs Chú lực: Hệ thống sức mạnh nào chặt chẽ nhất?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 93 ảnh, 7 đoạn đọc, khoảng 14.8 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (93 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Naruto đến hết Đại chiến Ninja lần thứ tư, Hunter x Hunter đến arc Kiến Chimera, v…

```text
Wide 16:9 landscape cinematic frame. three closed books on a desk, each with a different glowing emblem on the cover, candlelight. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Ba bộ truyện, ba hệ thống sức mạnh được fan tranh luận nhiều nhất: Chakra của Naruto, Nen của Hunter x Hunter…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols in a triangle: a swirling blue orb, a golden hexagon, and a dark purple flame. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Câu hỏi hôm nay không phải hệ nào mạnh nhất, vì nhân vật mạnh hay yếu tùy tác giả. Câu hỏi là: hệ thống nào đ…

```text
Wide 16:9 landscape cinematic frame. a scale with three pans, each holding a different glowing symbol, perfectly balanced. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Để trả lời, mình sẽ chấm ba hệ thống theo sáu tiêu chí, từ nguồn năng lượng tới cái giá phải trả, rồi cộng đi…

```text
Wide 16:9 landscape cinematic frame. a scorecard grid with six rows and three columns, empty cells glowing faintly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ biến thành bàn giám khảo, và Kaku sẽ cố gắng công bằng nhất có th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting behind a judge's desk with a tiny gavel and three name plates. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn chưa xem video giải thích Nen và lãnh địa của kênh, cũng không sao. Mình sẽ nhắc lại những gì cần biế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing to two small thumbnails pinned on a board: a hexagon and a dark dome. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Tiêu chí chấm điểm

Lời: Trước khi chấm, cần thống nhất tiêu chí. Mình chọn sáu tiêu chí mà một hệ thống sức mạnh tốt nên có.

```text
Wide 16:9 landscape cinematic frame. a list of six glowing icons on a scroll: a spring, a gate, a rulebook, a price tag, a chess piece, and a paintbrush. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Một, nguồn năng lượng rõ ràng: sức mạnh đến từ đâu. Hai, ai dùng được: có công bằng hay chỉ dành cho người đư…

```text
Wide 16:9 landscape cinematic frame. a spring of glowing water and an open gate with people walking through. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ba, luật và giới hạn: có quy tắc rõ để người xem hiểu. Bốn, cái giá: dùng sức mạnh có phải trả gì không.

```text
Wide 16:9 landscape cinematic frame. a rulebook with glowing clauses and a price tag hanging from a chain. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Năm, chiều sâu chiến thuật: trận đấu có giống đấu trí không. Sáu, không gian sáng tạo: nhân vật có thể tạo ra…

```text
Wide 16:9 landscape cinematic frame. a chessboard with glowing pieces and a paintbrush painting a new symbol in the air. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mỗi tiêu chí chấm từ một đến năm điểm. Đây là đánh giá của Kaku, bạn hoàn toàn có thể không đồng ý, và mình r…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up five fingers of feathers, smiling. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Ba hệ thống trong một phút

Lời: Nhắc nhanh ba hệ thống. Chakra là năng lượng tạo từ thể chất và tinh thần. Ninja dùng nó cho nhẫn thuật, ảo t…

```text
Wide 16:9 landscape cinematic frame. a ninja silhouette forming hand seals with blue energy flowing through the body. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nen là kỹ năng điều khiển khí, năng lượng sống. Nó có bốn nguyên tắc cơ bản, sáu hệ trên hình lục giác, và lu…

```text
Wide 16:9 landscape cinematic frame. a golden hexagon with six glowing vertices floating above an open palm. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Chú lực là năng lượng sinh ra từ cảm xúc tiêu cực. Chú thuật sư dùng nó để kích hoạt thuật thức bẩm sinh, và…

```text
Wide 16:9 landscape cinematic frame. dark purple energy rising from a figure, forming a dome in the background. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Ba hệ nghe giống nhau ở chỗ đều là năng lượng bên trong cơ thể. Nhưng cách chúng được tổ chức thì khác nhau r…

```text
Wide 16:9 landscape cinematic frame. three energy streams of blue, gold, and purple flowing from three silhouettes into three different shaped containers. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Tiêu chí 1: nguồn năng lượng

Lời: Tiêu chí đầu tiên: nguồn năng lượng có rõ ràng không, và nó có ý nghĩa gì với câu chuyện?

```text
Wide 16:9 landscape cinematic frame. three wellsprings side by side: blue, gold, and purple. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Chakra đến từ thể chất và tinh thần. Rõ ràng, dễ hiểu, nhưng khá trung tính, nó không nói gì nhiều về cảm xúc…

```text
Wide 16:9 landscape cinematic frame. a simple diagram of body energy and mind energy merging into a blue orb. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nen đến từ sức sống. Ai cũng có, chỉ cần đánh thức. Nó gắn với sự sống và ý chí, và được giải thích rất kỹ qu…

```text
Wide 16:9 landscape cinematic frame. a human silhouette with glowing aura nodes across the body, light leaking gently. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Chú lực đến từ cảm xúc tiêu cực. Đây là lựa chọn rất đậm chất chủ đề: thế giới Jujutsu Kaisen được xây trên n…

```text
Wide 16:9 landscape cinematic frame. a crowd of silhouettes emitting dark purple wisps that gather into curse shapes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Kaku chấm: Chakra ba điểm, Nen bốn điểm, Chú lực năm điểm. Chú lực thắng vì nguồn năng lượng gắn chặt nhất vớ…

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 4, 5 appearing under three icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Tiêu chí 2: ai dùng được?

Lời: Tiêu chí thứ hai: sức mạnh có công bằng không? Người bình thường có thể mạnh lên, hay chỉ người được chọn?

```text
Wide 16:9 landscape cinematic frame. an open gate with many people walking toward it, some blocked, some passing. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Với Chakra, ai cũng có, ai chịu tập cũng dùng được. Nhưng truyện dần nghiêng về dòng máu: gia tộc, huyết kế g…

```text
Wide 16:9 landscape cinematic frame. a family tree with glowing lineages at the top and ordinary figures at the bottom looking up. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Với Nen, ai cũng có khí, và ai được dạy đúng cách cũng học được. Tài năng có ảnh hưởng, nhưng nỗ lực và sự kh…

```text
Wide 16:9 landscape cinematic frame. diverse figures of all ages training together on a grassy field, each with a faint aura. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Với Chú lực, ai cũng có chú lực, nhưng thuật thức là bẩm sinh. Không có thuật thức thì rất khó trở thành chú…

```text
Wide 16:9 landscape cinematic frame. a crowd with faint purple wisps, only a few with bright unique emblems glowing on their chests. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực ba điểm. Nen công bằng nhất, vì nó cho người bình thường nhi…

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 5, 3. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Tiêu chí 3: luật và giới hạn

Lời: Tiêu chí thứ ba: hệ thống có luật rõ ràng không? Người xem có tự đoán được điều gì làm được, điều gì không?

```text
Wide 16:9 landscape cinematic frame. a thick rulebook with glowing numbered clauses on a wooden table. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Chakra có các nguyên tố và nhóm nhẫn thuật, nhưng giới hạn khá linh hoạt. Nhiều năng lực mới xuất hiện ở cuối…

```text
Wide 16:9 landscape cinematic frame. a rulebook whose later pages are scribbled over with new glowing symbols. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nen có luật chi tiết: bốn nguyên tắc, bảy kỹ năng nâng cao, sáu hệ với tỉ lệ phần trăm, và giao ước. Người xe…

```text
Wide 16:9 landscape cinematic frame. a precise technical diagram of a hexagon with percentages and arrows. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Chú lực cũng có luật rõ: thuật thức, đảo ngược thuật thức, lãnh địa, giản dị lãnh địa, và các giao ước ràng b…

```text
Wide 16:9 landscape cinematic frame. a layered diagram of techniques stacked like floors of a tower. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng vì luật vừa chặt vừa ít khái niệm hơn.

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 5, 4. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Tiêu chí 4: cái giá

Lời: Tiêu chí thứ tư: dùng sức mạnh có phải trả giá không? Một hệ thống có cái giá thường tạo ra kịch tính và lựa…

```text
Wide 16:9 landscape cinematic frame. three price tags hanging on chains over three glowing symbols. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Với Chakra, cái giá chủ yếu là cạn chakra. Có những thuật cấm và đôi mắt đặc biệt đòi giá đắt, nhưng phần lớn…

```text
Wide 16:9 landscape cinematic frame. a tired ninja kneeling after a big technique, faint blue energy fading, a red eye glowing in the corner. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Với Nen, cái giá được đưa vào tận luật chơi: giới hạn và giao ước. Tự đặt điều kiện càng khắt khe, sức mạnh c…

```text
Wide 16:9 landscape cinematic frame. a sealed contract glowing with a chain, an hourglass draining beside it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Với Chú lực, cũng có giao ước ràng buộc, và lãnh địa làm thuật thức bị cháy sau khi dùng. Cái giá xuất hiện ở…

```text
Wide 16:9 landscape cinematic frame. a burnt-out engine glowing red inside a collapsing dome. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Hai hệ sau hòa nhau, vì cái giá là một phần cốt lõ…

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 5, 5. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Tiêu chí 5: chiều sâu chiến thuật

Lời: Tiêu chí thứ năm: trận đấu có giống đấu trí không, hay chủ yếu là ai có năng lượng nhiều hơn?

```text
Wide 16:9 landscape cinematic frame. a chessboard with glowing pieces shaped like the three symbols. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Chakra có những trận đấu chiến thuật rất hay, nhất là ở nửa đầu truyện. Về sau, nhiều trận lớn nghiêng về lượ…

```text
Wide 16:9 landscape cinematic frame. an early small-scale ninja duel in a forest, then a giant clash of colossal energy figures in the sky. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nen được xây cho đấu trí: che giấu năng lực, dùng In để giấu khí, dùng Gyo để nhìn thấu, và khai thác điều ki…

```text
Wide 16:9 landscape cinematic frame. two figures at a card table, one hiding a transparent weapon, the other with glowing eyes. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Chú lực cũng rất chiến thuật, đặc biệt với lãnh địa và cách chống lãnh địa. Việc tiết lộ thuật thức cho đối t…

```text
Wide 16:9 landscape cinematic frame. a figure explaining their technique aloud to an opponent while their energy grows brighter. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Cả Nen và Chú lực đều biến trận đấu thành ván cờ.

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 5, 5. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Tiêu chí 6: không gian sáng tạo

Lời: Tiêu chí cuối: hệ thống có cho phép nhân vật sáng tạo ra năng lực mới, độc đáo, mà vẫn hợp luật không?

```text
Wide 16:9 landscape cinematic frame. a paintbrush painting a brand-new glowing symbol in the air above three emblems. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chakra có nhiều biến thể nguyên tố và nhẫn thuật riêng, nhưng nhiều năng lực mạnh nhất lại đến từ dòng máu ho…

```text
Wide 16:9 landscape cinematic frame. a ninja experimenting with a new swirling technique in a training field. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Nen có Hatsu, năng lực riêng do mỗi người tự thiết kế theo hệ và tính cách. Đây là không gian sáng tạo cực lớ…

```text
Wide 16:9 landscape cinematic frame. a drafting table with blueprints of strange glowing abilities, a hexagon compass beside them. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Chú lực có thuật thức bẩm sinh, nhưng cách mỗi người mở rộng và kết hợp thuật thức, cùng lãnh địa phản ánh tâ…

```text
Wide 16:9 landscape cinematic frame. a gallery of surreal domain landscapes, each different from the next. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng nhờ Hatsu, nơi giới hạn duy nhất là trí…

```text
Wide 16:9 landscape cinematic frame. a scorecard with glowing numbers 3, 5, 4. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Kết quả chung cuộc

Lời: Giờ cộng điểm. Chakra được ba cộng ba cộng ba cộng ba cộng ba cộng ba, tổng mười tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scoreboard with a blue orb and the number 18 glowing. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nen được bốn cộng năm cộng năm cộng năm cộng năm cộng năm, tổng hai mươi chín điểm.

```text
Wide 16:9 landscape cinematic frame. a scoreboard with a golden hexagon and the number 29 glowing brightly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Chú lực được năm cộng ba cộng bốn cộng năm cộng năm cộng bốn, tổng hai mươi sáu điểm.

```text
Wide 16:9 landscape cinematic frame. a scoreboard with a purple flame and the number 26 glowing. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Theo bảng chấm của Kaku, Nen là hệ thống chặt chẽ nhất, Chú lực đứng thứ hai rất sát, và Chakra đứng thứ ba.

```text
Wide 16:9 landscape cinematic frame. a podium with a golden hexagon on top, a purple flame second, and a blue orb third. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhưng nhớ nhé: chặt chẽ không có nghĩa là hay hơn. Chakra thua về luật, nhưng lại thắng ở cảm xúc và độ phổ b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small trophy but pointing to a crowd cheering for the blue orb. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Thử nghiệm: một trận đấu, ba hệ thống

Lời: Để thấy sự khác nhau rõ hơn, hãy tưởng tượng cùng một tình huống xảy ra trong ba thế giới: một người yếu hơn…

```text
Wide 16:9 landscape cinematic frame. a small figure facing a towering opponent on a bridge, three colored filters overlaid. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Trong thế giới Chakra, người yếu thường thắng nhờ một cú bộc phát cảm xúc, một nhẫn thuật mới học được đúng l…

```text
Wide 16:9 landscape cinematic frame. a small ninja surrounded by bursting blue energy and friends arriving behind him. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Trong thế giới Nen, người yếu thắng nhờ thông tin và giao ước: giấu năng lực, đặt điều kiện khắt khe cho một…

```text
Wide 16:9 landscape cinematic frame. a small figure hiding a glowing hand behind their back while the opponent laughs, a contract glowing. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Trong thế giới Chú lực, người yếu thắng nhờ hiểu thuật thức của đối thủ, dùng giản dị lãnh địa để sống sót, v…

```text
Wide 16:9 landscape cinematic frame. a small figure inside a circle of calm light while a collapsing dome fades around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Cùng một câu chuyện, nhưng ba cách giải quyết rất khác nhau. Đó chính là dấu ấn của từng hệ thống.

```text
Wide 16:9 landscape cinematic frame. three short film strips side by side, each ending with the small figure standing. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: nhìn cách kẻ yếu chiến thắng là cách nhanh nhất để hiểu một hệ thống sức mạnh được thiết kế ra…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over the small figure in the film strip. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Những hệ thống khác trên kênh

Lời: Ba hệ thống hôm nay không phải là tất cả. Trên kênh, Kaku đã giải mã thêm vài hệ thống khác, và mỗi hệ có một…

```text
Wide 16:9 landscape cinematic frame. a bookshelf with glowing spines, each with a different small emblem. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Haki của One Piece gắn với ý chí, và cân bằng giữa số phận với nỗ lực.

```text
Wide 16:9 landscape cinematic frame. a black lightning fist emblem glowing on a book spine. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hơi thở của Kimetsu no Yaiba có một cây phả hệ rõ ràng, và cái giá được trả bằng chính cơ thể.

```text
Wide 16:9 landscape cinematic frame. a book spine with a flowing family tree emblem of water and fire. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Ma thuật trong Frieren có lịch sử và tiến hóa như khoa học, nơi phép mạnh nhất hôm nay có thể là bài học vỡ l…

```text
Wide 16:9 landscape cinematic frame. a book spine with a violet beam emblem turning into a textbook icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Và ác quỷ trong Chainsaw Man có sức mạnh đến từ nỗi sợ của cả loài người.

```text
Wide 16:9 landscape cinematic frame. a book spine with a shadowy crowd emblem. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu chấm theo sáu tiêu chí hôm nay, bạn nghĩ hệ thống nào trong số đó sẽ đứng đầu? Kaku có thể làm một bảng x…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a long blank ranking scroll unrolling to the floor. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Nếu trộn ba hệ thống

Lời: Một câu hỏi vui để khép lại phần phân tích: nếu một nhân vật có cả Chakra, Nen và Chú lực, điều gì sẽ xảy ra?

```text
Wide 16:9 landscape cinematic frame. a figure with three colored auras swirling around them: blue, gold, and purple. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Có lẽ họ sẽ dùng kết ấn để tung nhẫn thuật, đặt giao ước Nen để tăng sức mạnh, và mở lãnh địa để đòn đánh tất…

```text
Wide 16:9 landscape cinematic frame. a chaotic storm of three energies clashing inside a single figure, cracks forming. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Vì mỗi hệ thống được thiết kế cho câu chuyện riêng của nó. Trộn lẫn thì luật bị chồng chéo, và giới hạn, thứ…

```text
Wide 16:9 landscape cinematic frame. three puzzle sets whose pieces do not fit together, scattered on a table. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Đây cũng là lý do các tác giả giỏi thường giữ hệ thống của mình gọn gàng: ít khái niệm, luật rõ, và cái giá t…

```text
Wide 16:9 landscape cinematic frame. a single clean glowing emblem inside a simple frame, calm and balanced. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Vì sao Chakra vẫn được yêu thích nhất?

Lời: Nếu Chakra đứng cuối bảng, vì sao Naruto vẫn là một trong những bộ truyện được yêu thích nhất mọi thời đại?

```text
Wide 16:9 landscape cinematic frame. a massive crowd of fans holding up headbands, glowing blue energy rising above them. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Lý do một: Chakra rất dễ hiểu. Một đứa trẻ xem lần đầu cũng hiểu ngay: tập trung năng lượng, kết ấn, tung chi…

```text
Wide 16:9 landscape cinematic frame. a child copying hand seals in front of a TV screen, eyes shining. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Lý do hai: Naruto tập trung vào cảm xúc và mối quan hệ hơn là luật chơi. Trận đấu hay vì ta quan tâm tới nhân…

```text
Wide 16:9 landscape cinematic frame. two rivals facing each other at a waterfall, rain falling, emotions more than energy visible. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Lý do ba: Chakra ra đời sớm hơn và mở đường cho nhiều bộ sau. Nhiều hệ thống hiện đại học hỏi từ những gì Nar…

```text
Wide 16:9 landscape cinematic frame. a road with footprints leading from an old path into many newer branching paths. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ: một hệ thống không cần hoàn hảo để làm nên một câu chuyện tuyệt vời. Luật là công cụ, còn cảm xúc…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a rulebook down and picking up a small heart-shaped lantern. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Điểm chung của ba hệ thống

Lời: Dù khác nhau, cả ba hệ thống chia sẻ một vài ý tưởng chung, và những ý tưởng này có lẽ là công thức của một h…

```text
Wide 16:9 landscape cinematic frame. three overlapping circles of blue, gold, and purple with a glowing intersection. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Một, sức mạnh đến từ bên trong con người, không phải từ vũ khí hay công nghệ. Người mạnh là người hiểu và làm…

```text
Wide 16:9 landscape cinematic frame. a figure meditating with energy of three colors swirling inside their chest. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hai, sức mạnh phản ánh tính cách. Năng lực của nhân vật nói lên họ là ai: hệ Nen, thuật thức, hay phong cách…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting different figures as different glowing emblems. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Ba, sức mạnh có giới hạn và cái giá. Không có năng lực nào vô hạn, và chính giới hạn tạo ra kịch tính.

```text
Wide 16:9 landscape cinematic frame. a glowing power source inside a cage made of chains, stable and contained. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bốn, sức mạnh có thể rèn luyện. Dù tài năng quan trọng, cả ba bộ đều có những nhân vật đi lên nhờ nỗ lực.

```text
Wide 16:9 landscape cinematic frame. a figure climbing a staircase with sweat drops, three colored lights at the top. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Hệ thống sức mạnh lý tưởng

Lời: Nếu được tự thiết kế một hệ thống sức mạnh từ những gì học được hôm nay, Kaku sẽ lấy mỗi hệ một điểm mạnh.

```text
Wide 16:9 landscape cinematic frame. a blank blueprint on a drafting table with three colored pencils beside it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Từ Chú lực, mình lấy nguồn năng lượng gắn với chủ đề câu chuyện. Nếu truyện nói về lòng dũng cảm, năng lượng…

```text
Wide 16:9 landscape cinematic frame. a purple pencil drawing a wellspring connected to a heart icon on the blueprint. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Từ Nen, mình lấy luật rõ ràng, sự công bằng và không gian để mỗi nhân vật tự thiết kế năng lực.

```text
Wide 16:9 landscape cinematic frame. a gold pencil drawing a clean hexagon rulebook and a blank emblem slot. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Từ Chakra, mình lấy sự dễ hiểu và cảm xúc. Một đứa trẻ xem lần đầu cũng phải hiểu ngay và thấy phấn khích.

```text
Wide 16:9 landscape cinematic frame. a blue pencil drawing a simple glowing hand seal and a smiling child. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và cuối cùng, một cái giá thật cho mọi sức mạnh lớn, để mỗi lựa chọn của nhân vật đều có ý nghĩa.

```text
Wide 16:9 landscape cinematic frame. a finished blueprint with a small price tag drawn at the center, glowing softly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn cũng đang viết truyện hay làm game, hy vọng bảng tiêu chí này giúp ích. Và nếu bạn thiết kế được một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the blueprint and tying it with its red scarf. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Ý kiến trái chiều

Lời: Để công bằng, đây là vài ý kiến trái chiều mà Kaku thấy fan hay đưa ra, và mình nghĩ chúng đều có lý.

```text
Wide 16:9 landscape cinematic frame. a debate stage with several podiums, speech bubbles without text above them. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Có người cho rằng Nen chặt chẽ nhưng tác giả đôi khi vẫn phá luật khi cần, nên không thể cho gần tuyệt đối. Đ…

```text
Wide 16:9 landscape cinematic frame. a precise hexagon diagram with a single small crack glowing at one corner. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Có người cho rằng Chú lực mới là chặt nhất vì có nhiều tầng khái niệm hơn. Nhưng nhiều khái niệm cũng làm ngư…

```text
Wide 16:9 landscape cinematic frame. a very tall tower of stacked technique diagrams with a small confused figure at its base. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và có người cho rằng không nên so sánh vì mỗi bộ có mục đích khác nhau. Điều này cũng đúng, và là lý do Kaku…

```text
Wide 16:9 landscape cinematic frame. three different-shaped keys each fitting a different lock. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn chấm khác Kaku, hãy viết điểm của bạn cho sáu tiêu chí xuống phần bình luận. Kaku sẽ đọc hết.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank scorecard and a pencil, looking at the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · Tóm tắt

Lời: Tóm lại: theo sáu tiêu chí, Nen đạt hai mươi chín điểm, Chú lực hai mươi sáu, và Chakra mười tám.

```text
Wide 16:9 landscape cinematic frame. a final scoreboard showing 29, 26, and 18 under the three symbols. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Nen thắng về luật, sự công bằng và sáng tạo. Chú lực thắng về nguồn năng lượng gắn với chủ đề. Chakra thắng v…

```text
Wide 16:9 landscape cinematic frame. three small trophies each with a different label icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Và bài học chung: một hệ thống sức mạnh hay cần nguồn gốc rõ ràng, luật dễ hiểu, cái giá thật, và chỗ cho nhâ…

```text
Wide 16:9 landscape cinematic frame. a blueprint of an ideal power system with four glowing pillars. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: hệ thống sức mạnh yêu thích của bạn là gì, kể cả ngoài ba hệ này? Viết xuống phần bình luận…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a suggestion box with a slot on top. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ xếp hạng các dạng Super Saiyan trong Dragon Ball, theo…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing golden aura with spiky hair silhouette. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye behind a judge's desk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Tiêu chí chấm điểm / Ba hệ thống trong một phút

Khoảng 149 giây · cảnh s01–s15 · 1933 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Naruto đến hết Đại chiến Ninja lần thứ tư, Hunter x Hunter đến arc Kiến Chimera, và Jujutsu Kaisen đến arc Trò chơi tử thần.

<short pause> Ba bộ truyện, ba hệ thống sức mạnh được fan tranh luận nhiều nhất: Chakra của Naruto, Nen của Hunter x Hunter, và Chú lực của Jujutsu Kaisen.

<short pause> Câu hỏi hôm nay không phải hệ nào mạnh nhất, vì nhân vật mạnh hay yếu tùy tác giả. Câu hỏi là: hệ thống nào được thiết kế chặt chẽ nhất?

<short pause> Để trả lời, mình sẽ chấm ba hệ thống theo sáu tiêu chí, từ nguồn năng lượng tới cái giá phải trả, rồi cộng điểm cuối cùng.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ biến thành bàn giám khảo, và Kaku sẽ cố gắng công bằng nhất có thể.

<short pause> Nếu bạn chưa xem video giải thích Nen và lãnh địa của kênh, cũng không sao. Mình sẽ nhắc lại những gì cần biết ngay trong video này.

<short pause> Trước khi chấm, cần thống nhất tiêu chí. Mình chọn sáu tiêu chí mà một hệ thống sức mạnh tốt nên có.

<short pause> Một, nguồn năng lượng rõ ràng: sức mạnh đến từ đâu. Hai, ai dùng được: có công bằng hay chỉ dành cho người được chọn.

<short pause> Ba, luật và giới hạn: có quy tắc rõ để người xem hiểu. Bốn, cái giá: dùng sức mạnh có phải trả gì không.

<short pause> Năm, chiều sâu chiến thuật: trận đấu có giống đấu trí không. Sáu, không gian sáng tạo: nhân vật có thể tạo ra năng lực mới không.

<short pause> Mỗi tiêu chí chấm từ một đến năm điểm. Đây là đánh giá của Kaku, bạn hoàn toàn có thể không đồng ý, và mình rất muốn nghe ý kiến của bạn.

<short pause> Nhắc nhanh ba hệ thống. Chakra là năng lượng tạo từ thể chất và tinh thần. Ninja dùng nó cho nhẫn thuật, ảo thuật và thể thuật, thường thông qua kết ấn tay.

<short pause> Nen là kỹ năng điều khiển khí, năng lượng sống. Nó có bốn nguyên tắc cơ bản, sáu hệ trên hình lục giác, và luật giới hạn cùng giao ước.

<short pause> Chú lực là năng lượng sinh ra từ cảm xúc tiêu cực. Chú thuật sư dùng nó để kích hoạt thuật thức bẩm sinh, và ở đỉnh cao là bành trướng lãnh địa.

<short pause> Ba hệ nghe giống nhau ở chỗ đều là năng lượng bên trong cơ thể. <short pause> Nhưng cách chúng được tổ chức thì khác nhau rất nhiều.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Naruto đến hết Đại chiến Ninja lần thứ tư, Hunter x Hunter đến arc Kiến Chimera, và Jujutsu Kaisen đến arc Trò chơi tử thần.

[pause] Ba bộ truyện, ba hệ thống sức mạnh được fan tranh luận nhiều nhất: Chakra của Naruto, Nen của Hunter x Hunter, và Chú lực của Jujutsu Kaisen.

[pause] Câu hỏi hôm nay không phải hệ nào mạnh nhất, vì nhân vật mạnh hay yếu tùy tác giả. [curious] Câu hỏi là: hệ thống nào được thiết kế chặt chẽ nhất?

[pause] Để trả lời, mình sẽ chấm ba hệ thống theo sáu tiêu chí, từ nguồn năng lượng tới cái giá phải trả, rồi cộng điểm cuối cùng.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ biến thành bàn giám khảo, và Kaku sẽ cố gắng công bằng nhất có thể.

[pause] Nếu bạn chưa xem video giải thích Nen và lãnh địa của kênh, cũng không sao. Mình sẽ nhắc lại những gì cần biết ngay trong video này.

[pause] Trước khi chấm, cần thống nhất tiêu chí. Mình chọn sáu tiêu chí mà một hệ thống sức mạnh tốt nên có.

[pause] Một, nguồn năng lượng rõ ràng: sức mạnh đến từ đâu. Hai, ai dùng được: có công bằng hay chỉ dành cho người được chọn.

[pause] Ba, luật và giới hạn: có quy tắc rõ để người xem hiểu. Bốn, cái giá: dùng sức mạnh có phải trả gì không.

[pause] Năm, chiều sâu chiến thuật: trận đấu có giống đấu trí không. Sáu, không gian sáng tạo: nhân vật có thể tạo ra năng lực mới không.

[pause] Mỗi tiêu chí chấm từ một đến năm điểm. Đây là đánh giá của Kaku, bạn hoàn toàn có thể không đồng ý, và mình rất muốn nghe ý kiến của bạn.

[pause] Nhắc nhanh ba hệ thống. Chakra là năng lượng tạo từ thể chất và tinh thần. Ninja dùng nó cho nhẫn thuật, ảo thuật và thể thuật, thường thông qua kết ấn tay.

[pause] Nen là kỹ năng điều khiển khí, năng lượng sống. Nó có bốn nguyên tắc cơ bản, sáu hệ trên hình lục giác, và luật giới hạn cùng giao ước.

[pause] Chú lực là năng lượng sinh ra từ cảm xúc tiêu cực. Chú thuật sư dùng nó để kích hoạt thuật thức bẩm sinh, và ở đỉnh cao là bành trướng lãnh địa.

[pause] Ba hệ nghe giống nhau ở chỗ đều là năng lượng bên trong cơ thể. [pause] Nhưng cách chúng được tổ chức thì khác nhau rất nhiều.
```

### c02 · Tiêu chí 1: nguồn năng lượng / Tiêu chí 2: ai dùng được? / Tiêu chí 3: luật và giới hạn

Khoảng 150 giây · cảnh s16–s30 · 1948 ký tự

**Gemini**

```text
Tiêu chí đầu tiên: nguồn năng lượng có rõ ràng không, và nó có ý nghĩa gì với câu chuyện?

<short pause> Chakra đến từ thể chất và tinh thần. Rõ ràng, dễ hiểu, nhưng khá trung tính, nó không nói gì nhiều về cảm xúc của nhân vật.

<short pause> Nen đến từ sức sống. Ai cũng có, chỉ cần đánh thức. Nó gắn với sự sống và ý chí, và được giải thích rất kỹ qua các lỗ khí.

<short pause> Chú lực đến từ cảm xúc tiêu cực. Đây là lựa chọn rất đậm chất chủ đề: thế giới Jujutsu Kaisen được xây trên nỗi sợ, oán hận và cái chết.

<short pause> Kaku chấm: Chakra ba điểm, Nen bốn điểm, Chú lực năm điểm. Chú lực thắng vì nguồn năng lượng gắn chặt nhất với câu chuyện.

<short pause> Tiêu chí thứ hai: sức mạnh có công bằng không? Người bình thường có thể mạnh lên, hay chỉ người được chọn?

<short pause> Với Chakra, ai cũng có, ai chịu tập cũng dùng được. <short pause> Nhưng truyện dần nghiêng về dòng máu: gia tộc, huyết kế giới hạn, và hậu duệ của những nhân vật huyền thoại.

<short pause> Với Nen, ai cũng có khí, và ai được dạy đúng cách cũng học được. Tài năng có ảnh hưởng, nhưng nỗ lực và sự khéo léo vẫn quyết định rất nhiều.

<short pause> Với Chú lực, ai cũng có chú lực, nhưng thuật thức là bẩm sinh. Không có thuật thức thì rất khó trở thành chú thuật sư mạnh, dù vẫn có ngoại lệ đáng nể.

<short pause> Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực ba điểm. Nen công bằng nhất, vì nó cho người bình thường nhiều đường để mạnh lên.

<short pause> Tiêu chí thứ ba: hệ thống có luật rõ ràng không? Người xem có tự đoán được điều gì làm được, điều gì không?

<short pause> Chakra có các nguyên tố và nhóm nhẫn thuật, nhưng giới hạn khá linh hoạt. Nhiều năng lực mới xuất hiện ở cuối truyện mà không theo luật cũ.

<short pause> Nen có luật chi tiết: bốn nguyên tắc, bảy kỹ năng nâng cao, sáu hệ với tỉ lệ phần trăm, và giao ước. Người xem gần như có thể tự tính toán trận đấu.

<short pause> Chú lực cũng có luật rõ: thuật thức, đảo ngược thuật thức, lãnh địa, giản dị lãnh địa, và các giao ước ràng buộc. Hệ thống rất chặt, nhưng có nhiều khái niệm phải nhớ.

<short pause> Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng vì luật vừa chặt vừa ít khái niệm hơn.
```

**ElevenLabs**

```text
[curious] Tiêu chí đầu tiên: nguồn năng lượng có rõ ràng không, và nó có ý nghĩa gì với câu chuyện?

[pause] Chakra đến từ thể chất và tinh thần. Rõ ràng, dễ hiểu, nhưng khá trung tính, nó không nói gì nhiều về cảm xúc của nhân vật.

[pause] Nen đến từ sức sống. Ai cũng có, chỉ cần đánh thức. Nó gắn với sự sống và ý chí, và được giải thích rất kỹ qua các lỗ khí.

[pause] Chú lực đến từ cảm xúc tiêu cực. Đây là lựa chọn rất đậm chất chủ đề: thế giới Jujutsu Kaisen được xây trên nỗi sợ, oán hận và cái chết.

[pause] Kaku chấm: Chakra ba điểm, Nen bốn điểm, Chú lực năm điểm. Chú lực thắng vì nguồn năng lượng gắn chặt nhất với câu chuyện.

[pause] Tiêu chí thứ hai: sức mạnh có công bằng không? Người bình thường có thể mạnh lên, hay chỉ người được chọn?

[pause] Với Chakra, ai cũng có, ai chịu tập cũng dùng được. [pause] Nhưng truyện dần nghiêng về dòng máu: gia tộc, huyết kế giới hạn, và hậu duệ của những nhân vật huyền thoại.

[pause] Với Nen, ai cũng có khí, và ai được dạy đúng cách cũng học được. Tài năng có ảnh hưởng, nhưng nỗ lực và sự khéo léo vẫn quyết định rất nhiều.

[pause] Với Chú lực, ai cũng có chú lực, nhưng thuật thức là bẩm sinh. Không có thuật thức thì rất khó trở thành chú thuật sư mạnh, dù vẫn có ngoại lệ đáng nể.

[pause] Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực ba điểm. Nen công bằng nhất, vì nó cho người bình thường nhiều đường để mạnh lên.

[pause] Tiêu chí thứ ba: hệ thống có luật rõ ràng không? Người xem có tự đoán được điều gì làm được, điều gì không?

[pause] Chakra có các nguyên tố và nhóm nhẫn thuật, nhưng giới hạn khá linh hoạt. Nhiều năng lực mới xuất hiện ở cuối truyện mà không theo luật cũ.

[pause] Nen có luật chi tiết: bốn nguyên tắc, bảy kỹ năng nâng cao, sáu hệ với tỉ lệ phần trăm, và giao ước. Người xem gần như có thể tự tính toán trận đấu.

[pause] Chú lực cũng có luật rõ: thuật thức, đảo ngược thuật thức, lãnh địa, giản dị lãnh địa, và các giao ước ràng buộc. Hệ thống rất chặt, nhưng có nhiều khái niệm phải nhớ.

[pause] Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng vì luật vừa chặt vừa ít khái niệm hơn.
```

### c03 · Tiêu chí 4: cái giá / Tiêu chí 5: chiều sâu chiến thuật

Khoảng 102 giây · cảnh s31–s40 · 1329 ký tự

**Gemini**

```text
Tiêu chí thứ tư: dùng sức mạnh có phải trả giá không? Một hệ thống có cái giá thường tạo ra kịch tính và lựa chọn khó khăn.

<short pause> Với Chakra, cái giá chủ yếu là cạn chakra. Có những thuật cấm và đôi mắt đặc biệt đòi giá đắt, nhưng phần lớn nhẫn thuật chỉ tốn sức.

<short pause> Với Nen, cái giá được đưa vào tận luật chơi: giới hạn và giao ước. Tự đặt điều kiện càng khắt khe, sức mạnh càng lớn, có khi đổi bằng cả tuổi thọ hay tương lai.

<short pause> Với Chú lực, cũng có giao ước ràng buộc, và lãnh địa làm thuật thức bị cháy sau khi dùng. Cái giá xuất hiện ở hầu hết những kỹ thuật mạnh.

<short pause> Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Hai hệ sau hòa nhau, vì cái giá là một phần cốt lõi của luật.

<short pause> Tiêu chí thứ năm: trận đấu có giống đấu trí không, hay chủ yếu là ai có năng lượng nhiều hơn?

<short pause> Chakra có những trận đấu chiến thuật rất hay, nhất là ở nửa đầu truyện. Về sau, nhiều trận lớn nghiêng về lượng chakra khổng lồ và những năng lực mang tính thần thoại.

<short pause> Nen được xây cho đấu trí: che giấu năng lực, dùng In để giấu khí, dùng Gyo để nhìn thấu, và khai thác điều kiện của đối thủ.

<short pause> Chú lực cũng rất chiến thuật, đặc biệt với lãnh địa và cách chống lãnh địa. Việc tiết lộ thuật thức cho đối thủ thậm chí có thể làm nó mạnh hơn, tạo thêm lựa chọn.

<short pause> Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Cả Nen và Chú lực đều biến trận đấu thành ván cờ.
```

**ElevenLabs**

```text
[curious] Tiêu chí thứ tư: dùng sức mạnh có phải trả giá không? Một hệ thống có cái giá thường tạo ra kịch tính và lựa chọn khó khăn.

[pause] Với Chakra, cái giá chủ yếu là cạn chakra. Có những thuật cấm và đôi mắt đặc biệt đòi giá đắt, nhưng phần lớn nhẫn thuật chỉ tốn sức.

[pause] Với Nen, cái giá được đưa vào tận luật chơi: giới hạn và giao ước. Tự đặt điều kiện càng khắt khe, sức mạnh càng lớn, có khi đổi bằng cả tuổi thọ hay tương lai.

[pause] Với Chú lực, cũng có giao ước ràng buộc, và lãnh địa làm thuật thức bị cháy sau khi dùng. Cái giá xuất hiện ở hầu hết những kỹ thuật mạnh.

[pause] Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Hai hệ sau hòa nhau, vì cái giá là một phần cốt lõi của luật.

[pause] Tiêu chí thứ năm: trận đấu có giống đấu trí không, hay chủ yếu là ai có năng lượng nhiều hơn?

[pause] Chakra có những trận đấu chiến thuật rất hay, nhất là ở nửa đầu truyện. Về sau, nhiều trận lớn nghiêng về lượng chakra khổng lồ và những năng lực mang tính thần thoại.

[pause] Nen được xây cho đấu trí: che giấu năng lực, dùng In để giấu khí, dùng Gyo để nhìn thấu, và khai thác điều kiện của đối thủ.

[pause] Chú lực cũng rất chiến thuật, đặc biệt với lãnh địa và cách chống lãnh địa. Việc tiết lộ thuật thức cho đối thủ thậm chí có thể làm nó mạnh hơn, tạo thêm lựa chọn.

[pause] Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực năm điểm. Cả Nen và Chú lực đều biến trận đấu thành ván cờ.
```

### c04 · Tiêu chí 6: không gian sáng tạo / Kết quả chung cuộc / Thử nghiệm: một trận đấu, ba hệ thống

Khoảng 151 giây · cảnh s41–s56 · 1967 ký tự

**Gemini**

```text
Tiêu chí cuối: hệ thống có cho phép nhân vật sáng tạo ra năng lực mới, độc đáo, mà vẫn hợp luật không?

<short pause> Chakra có nhiều biến thể nguyên tố và nhẫn thuật riêng, nhưng nhiều năng lực mạnh nhất lại đến từ dòng máu hoặc sức mạnh thần thoại, ít do nhân vật tự sáng tạo.

<short pause> Nen có Hatsu, năng lực riêng do mỗi người tự thiết kế theo hệ và tính cách. Đây là không gian sáng tạo cực lớn, có thể tạo ra những năng lực kỳ lạ nhất.

<short pause> Chú lực có thuật thức bẩm sinh, nhưng cách mỗi người mở rộng và kết hợp thuật thức, cùng lãnh địa phản ánh tâm hồn, cũng rất sáng tạo.

<short pause> Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng nhờ Hatsu, nơi giới hạn duy nhất là trí tưởng tượng và luật.

<short pause> Giờ cộng điểm. Chakra được ba cộng ba cộng ba cộng ba cộng ba cộng ba, tổng mười tám điểm.

<short pause> Nen được bốn cộng năm cộng năm cộng năm cộng năm cộng năm, tổng hai mươi chín điểm.

<short pause> Chú lực được năm cộng ba cộng bốn cộng năm cộng năm cộng bốn, tổng hai mươi sáu điểm.

<short pause> Theo bảng chấm của Kaku, Nen là hệ thống chặt chẽ nhất, Chú lực đứng thứ hai rất sát, và Chakra đứng thứ ba.

<short pause> Nhưng nhớ nhé: chặt chẽ không có nghĩa là hay hơn. Chakra thua về luật, nhưng lại thắng ở cảm xúc và độ phổ biến.

<short pause> Để thấy sự khác nhau rõ hơn, hãy tưởng tượng cùng một tình huống xảy ra trong ba thế giới: một người yếu hơn phải đánh bại một người mạnh hơn nhiều.

<short pause> Trong thế giới Chakra, người yếu thường thắng nhờ một cú bộc phát cảm xúc, một nhẫn thuật mới học được đúng lúc, hoặc sự giúp đỡ của đồng đội.

<short pause> Trong thế giới Nen, người yếu thắng nhờ thông tin và giao ước: giấu năng lực, đặt điều kiện khắt khe cho một đòn duy nhất, và đánh đúng lúc đối thủ chủ quan.

<short pause> Trong thế giới Chú lực, người yếu thắng nhờ hiểu thuật thức của đối thủ, dùng giản dị lãnh địa để sống sót, và phản công khi thuật thức đối thủ bị cháy.

<short pause> Cùng một câu chuyện, nhưng ba cách giải quyết rất khác nhau. Đó chính là dấu ấn của từng hệ thống.

<short pause> <laugh> Kaku nhận xét: nhìn cách kẻ yếu chiến thắng là cách nhanh nhất để hiểu một hệ thống sức mạnh được thiết kế ra sao.
```

**ElevenLabs**

```text
[curious] Tiêu chí cuối: hệ thống có cho phép nhân vật sáng tạo ra năng lực mới, độc đáo, mà vẫn hợp luật không?

[pause] Chakra có nhiều biến thể nguyên tố và nhẫn thuật riêng, nhưng nhiều năng lực mạnh nhất lại đến từ dòng máu hoặc sức mạnh thần thoại, ít do nhân vật tự sáng tạo.

[pause] Nen có Hatsu, năng lực riêng do mỗi người tự thiết kế theo hệ và tính cách. Đây là không gian sáng tạo cực lớn, có thể tạo ra những năng lực kỳ lạ nhất.

[pause] Chú lực có thuật thức bẩm sinh, nhưng cách mỗi người mở rộng và kết hợp thuật thức, cùng lãnh địa phản ánh tâm hồn, cũng rất sáng tạo.

[pause] Kaku chấm: Chakra ba điểm, Nen năm điểm, Chú lực bốn điểm. Nen thắng nhờ Hatsu, nơi giới hạn duy nhất là trí tưởng tượng và luật.

[pause] Giờ cộng điểm. Chakra được ba cộng ba cộng ba cộng ba cộng ba cộng ba, tổng mười tám điểm.

[pause] Nen được bốn cộng năm cộng năm cộng năm cộng năm cộng năm, tổng hai mươi chín điểm.

[pause] Chú lực được năm cộng ba cộng bốn cộng năm cộng năm cộng bốn, tổng hai mươi sáu điểm.

[pause] Theo bảng chấm của Kaku, Nen là hệ thống chặt chẽ nhất, Chú lực đứng thứ hai rất sát, và Chakra đứng thứ ba.

[pause] Nhưng nhớ nhé: chặt chẽ không có nghĩa là hay hơn. Chakra thua về luật, nhưng lại thắng ở cảm xúc và độ phổ biến.

[pause] Để thấy sự khác nhau rõ hơn, hãy tưởng tượng cùng một tình huống xảy ra trong ba thế giới: một người yếu hơn phải đánh bại một người mạnh hơn nhiều.

[pause] Trong thế giới Chakra, người yếu thường thắng nhờ một cú bộc phát cảm xúc, một nhẫn thuật mới học được đúng lúc, hoặc sự giúp đỡ của đồng đội.

[pause] Trong thế giới Nen, người yếu thắng nhờ thông tin và giao ước: giấu năng lực, đặt điều kiện khắt khe cho một đòn duy nhất, và đánh đúng lúc đối thủ chủ quan.

[pause] Trong thế giới Chú lực, người yếu thắng nhờ hiểu thuật thức của đối thủ, dùng giản dị lãnh địa để sống sót, và phản công khi thuật thức đối thủ bị cháy.

[pause] Cùng một câu chuyện, nhưng ba cách giải quyết rất khác nhau. Đó chính là dấu ấn của từng hệ thống.

[pause] [chuckles] Kaku nhận xét: nhìn cách kẻ yếu chiến thắng là cách nhanh nhất để hiểu một hệ thống sức mạnh được thiết kế ra sao.
```

### c05 · Những hệ thống khác trên kênh / Nếu trộn ba hệ thống / Vì sao Chakra vẫn được yêu thích nhất?

Khoảng 135 giây · cảnh s57–s71 · 1757 ký tự

**Gemini**

```text
Ba hệ thống hôm nay không phải là tất cả. Trên kênh, Kaku đã giải mã thêm vài hệ thống khác, và mỗi hệ có một điểm mạnh riêng.

<short pause> Haki của One Piece gắn với ý chí, và cân bằng giữa số phận với nỗ lực.

<short pause> Hơi thở của Kimetsu no Yaiba có một cây phả hệ rõ ràng, và cái giá được trả bằng chính cơ thể.

<short pause> Ma thuật trong Frieren có lịch sử và tiến hóa như khoa học, nơi phép mạnh nhất hôm nay có thể là bài học vỡ lòng ngày mai.

<short pause> Và ác quỷ trong Chainsaw Man có sức mạnh đến từ nỗi sợ của cả loài người.

<short pause> Nếu chấm theo sáu tiêu chí hôm nay, bạn nghĩ hệ thống nào trong số đó sẽ đứng đầu? <laugh> Kaku có thể làm một bảng xếp hạng lớn nếu bạn muốn.

<short pause> Một câu hỏi vui để khép lại phần phân tích: nếu một nhân vật có cả Chakra, Nen và Chú lực, điều gì sẽ xảy ra?

<short pause> Có lẽ họ sẽ dùng kết ấn để tung nhẫn thuật, đặt giao ước Nen để tăng sức mạnh, và mở lãnh địa để đòn đánh tất trúng. Nghe thì đáng sợ, nhưng rất khó kể thành chuyện.

<short pause> Vì mỗi hệ thống được thiết kế cho câu chuyện riêng của nó. Trộn lẫn thì luật bị chồng chéo, và giới hạn, thứ làm trận đấu hay, sẽ biến mất.

<short pause> Đây cũng là lý do các tác giả giỏi thường giữ hệ thống của mình gọn gàng: ít khái niệm, luật rõ, và cái giá thật.

<short pause> Nếu Chakra đứng cuối bảng, vì sao Naruto vẫn là một trong những bộ truyện được yêu thích nhất mọi thời đại?

<short pause> Lý do một: Chakra rất dễ hiểu. Một đứa trẻ xem lần đầu cũng hiểu ngay: tập trung năng lượng, kết ấn, tung chiêu.

<short pause> Lý do hai: Naruto tập trung vào cảm xúc và mối quan hệ hơn là luật chơi. Trận đấu hay vì ta quan tâm tới nhân vật, không phải vì ta hiểu hết cơ chế.

<short pause> Lý do ba: Chakra ra đời sớm hơn và mở đường cho nhiều bộ sau. Nhiều hệ thống hiện đại học hỏi từ những gì Naruto đã làm.

<short pause> Kaku nghĩ: một hệ thống không cần hoàn hảo để làm nên một câu chuyện tuyệt vời. Luật là công cụ, còn cảm xúc mới là đích đến.
```

**ElevenLabs**

```text
Ba hệ thống hôm nay không phải là tất cả. Trên kênh, Kaku đã giải mã thêm vài hệ thống khác, và mỗi hệ có một điểm mạnh riêng.

[pause] Haki của One Piece gắn với ý chí, và cân bằng giữa số phận với nỗ lực.

[pause] Hơi thở của Kimetsu no Yaiba có một cây phả hệ rõ ràng, và cái giá được trả bằng chính cơ thể.

[pause] Ma thuật trong Frieren có lịch sử và tiến hóa như khoa học, nơi phép mạnh nhất hôm nay có thể là bài học vỡ lòng ngày mai.

[pause] Và ác quỷ trong Chainsaw Man có sức mạnh đến từ nỗi sợ của cả loài người.

[pause] [curious] Nếu chấm theo sáu tiêu chí hôm nay, bạn nghĩ hệ thống nào trong số đó sẽ đứng đầu? [chuckles] Kaku có thể làm một bảng xếp hạng lớn nếu bạn muốn.

[pause] Một câu hỏi vui để khép lại phần phân tích: nếu một nhân vật có cả Chakra, Nen và Chú lực, điều gì sẽ xảy ra?

[pause] Có lẽ họ sẽ dùng kết ấn để tung nhẫn thuật, đặt giao ước Nen để tăng sức mạnh, và mở lãnh địa để đòn đánh tất trúng. Nghe thì đáng sợ, nhưng rất khó kể thành chuyện.

[pause] Vì mỗi hệ thống được thiết kế cho câu chuyện riêng của nó. Trộn lẫn thì luật bị chồng chéo, và giới hạn, thứ làm trận đấu hay, sẽ biến mất.

[pause] Đây cũng là lý do các tác giả giỏi thường giữ hệ thống của mình gọn gàng: ít khái niệm, luật rõ, và cái giá thật.

[pause] Nếu Chakra đứng cuối bảng, vì sao Naruto vẫn là một trong những bộ truyện được yêu thích nhất mọi thời đại?

[pause] Lý do một: Chakra rất dễ hiểu. Một đứa trẻ xem lần đầu cũng hiểu ngay: tập trung năng lượng, kết ấn, tung chiêu.

[pause] Lý do hai: Naruto tập trung vào cảm xúc và mối quan hệ hơn là luật chơi. Trận đấu hay vì ta quan tâm tới nhân vật, không phải vì ta hiểu hết cơ chế.

[pause] Lý do ba: Chakra ra đời sớm hơn và mở đường cho nhiều bộ sau. Nhiều hệ thống hiện đại học hỏi từ những gì Naruto đã làm.

[pause] Kaku nghĩ: một hệ thống không cần hoàn hảo để làm nên một câu chuyện tuyệt vời. Luật là công cụ, còn cảm xúc mới là đích đến.
```

### c06 · Điểm chung của ba hệ thống / Hệ thống sức mạnh lý tưởng / Ý kiến trái chiều

Khoảng 149 giây · cảnh s72–s87 · 1934 ký tự

**Gemini**

```text
Dù khác nhau, cả ba hệ thống chia sẻ một vài ý tưởng chung, và những ý tưởng này có lẽ là công thức của một hệ thống sức mạnh hay.

<short pause> Một, sức mạnh đến từ bên trong con người, không phải từ vũ khí hay công nghệ. Người mạnh là người hiểu và làm chủ chính mình.

<short pause> Hai, sức mạnh phản ánh tính cách. Năng lực của nhân vật nói lên họ là ai: hệ Nen, thuật thức, hay phong cách chiến đấu đều gắn với con người họ.

<short pause> Ba, sức mạnh có giới hạn và cái giá. Không có năng lực nào vô hạn, và chính giới hạn tạo ra kịch tính.

<short pause> Bốn, sức mạnh có thể rèn luyện. Dù tài năng quan trọng, cả ba bộ đều có những nhân vật đi lên nhờ nỗ lực.

<short pause> Nếu được tự thiết kế một hệ thống sức mạnh từ những gì học được hôm nay, Kaku sẽ lấy mỗi hệ một điểm mạnh.

<short pause> Từ Chú lực, mình lấy nguồn năng lượng gắn với chủ đề câu chuyện. Nếu truyện nói về lòng dũng cảm, năng lượng nên đến từ lòng dũng cảm.

<short pause> Từ Nen, mình lấy luật rõ ràng, sự công bằng và không gian để mỗi nhân vật tự thiết kế năng lực.

<short pause> Từ Chakra, mình lấy sự dễ hiểu và cảm xúc. Một đứa trẻ xem lần đầu cũng phải hiểu ngay và thấy phấn khích.

<short pause> Và cuối cùng, một cái giá thật cho mọi sức mạnh lớn, để mỗi lựa chọn của nhân vật đều có ý nghĩa.

<short pause> Nếu bạn cũng đang viết truyện hay làm game, hy vọng bảng tiêu chí này giúp ích. <laugh> Và nếu bạn thiết kế được một hệ thống hay, hãy kể cho Kaku nghe nhé.

<short pause> Để công bằng, đây là vài ý kiến trái chiều mà Kaku thấy fan hay đưa ra, và mình nghĩ chúng đều có lý.

<short pause> Có người cho rằng Nen chặt chẽ nhưng tác giả đôi khi vẫn phá luật khi cần, nên không thể cho gần tuyệt đối. Điều này hợp lý, không hệ thống nào hoàn hảo.

<short pause> Có người cho rằng Chú lực mới là chặt nhất vì có nhiều tầng khái niệm hơn. <short pause> Nhưng nhiều khái niệm cũng làm người xem mới khó theo.

<short pause> Và có người cho rằng không nên so sánh vì mỗi bộ có mục đích khác nhau. Điều này cũng đúng, và là lý do Kaku chỉ chấm theo tiêu chí, không nói bộ nào hay hơn.

<short pause> Nếu bạn chấm khác Kaku, hãy viết điểm của bạn cho sáu tiêu chí xuống phần bình luận. Kaku sẽ đọc hết.
```

**ElevenLabs**

```text
Dù khác nhau, cả ba hệ thống chia sẻ một vài ý tưởng chung, và những ý tưởng này có lẽ là công thức của một hệ thống sức mạnh hay.

[pause] Một, sức mạnh đến từ bên trong con người, không phải từ vũ khí hay công nghệ. Người mạnh là người hiểu và làm chủ chính mình.

[pause] Hai, sức mạnh phản ánh tính cách. Năng lực của nhân vật nói lên họ là ai: hệ Nen, thuật thức, hay phong cách chiến đấu đều gắn với con người họ.

[pause] Ba, sức mạnh có giới hạn và cái giá. Không có năng lực nào vô hạn, và chính giới hạn tạo ra kịch tính.

[pause] Bốn, sức mạnh có thể rèn luyện. Dù tài năng quan trọng, cả ba bộ đều có những nhân vật đi lên nhờ nỗ lực.

[pause] Nếu được tự thiết kế một hệ thống sức mạnh từ những gì học được hôm nay, Kaku sẽ lấy mỗi hệ một điểm mạnh.

[pause] Từ Chú lực, mình lấy nguồn năng lượng gắn với chủ đề câu chuyện. Nếu truyện nói về lòng dũng cảm, năng lượng nên đến từ lòng dũng cảm.

[pause] Từ Nen, mình lấy luật rõ ràng, sự công bằng và không gian để mỗi nhân vật tự thiết kế năng lực.

[pause] Từ Chakra, mình lấy sự dễ hiểu và cảm xúc. Một đứa trẻ xem lần đầu cũng phải hiểu ngay và thấy phấn khích.

[pause] Và cuối cùng, một cái giá thật cho mọi sức mạnh lớn, để mỗi lựa chọn của nhân vật đều có ý nghĩa.

[pause] Nếu bạn cũng đang viết truyện hay làm game, hy vọng bảng tiêu chí này giúp ích. [chuckles] Và nếu bạn thiết kế được một hệ thống hay, hãy kể cho Kaku nghe nhé.

[pause] Để công bằng, đây là vài ý kiến trái chiều mà Kaku thấy fan hay đưa ra, và mình nghĩ chúng đều có lý.

[pause] Có người cho rằng Nen chặt chẽ nhưng tác giả đôi khi vẫn phá luật khi cần, nên không thể cho gần tuyệt đối. Điều này hợp lý, không hệ thống nào hoàn hảo.

[pause] Có người cho rằng Chú lực mới là chặt nhất vì có nhiều tầng khái niệm hơn. [pause] Nhưng nhiều khái niệm cũng làm người xem mới khó theo.

[pause] Và có người cho rằng không nên so sánh vì mỗi bộ có mục đích khác nhau. Điều này cũng đúng, và là lý do Kaku chỉ chấm theo tiêu chí, không nói bộ nào hay hơn.

[pause] Nếu bạn chấm khác Kaku, hãy viết điểm của bạn cho sáu tiêu chí xuống phần bình luận. Kaku sẽ đọc hết.
```

### c07 · Tóm tắt

Khoảng 52 giây · cảnh s88–s93 · 670 ký tự

**Gemini**

```text
Tóm lại: theo sáu tiêu chí, Nen đạt hai mươi chín điểm, Chú lực hai mươi sáu, và Chakra mười tám.

<short pause> Nen thắng về luật, sự công bằng và sáng tạo. Chú lực thắng về nguồn năng lượng gắn với chủ đề. Chakra thắng về sự dễ hiểu và cảm xúc.

<short pause> Và bài học chung: một hệ thống sức mạnh hay cần nguồn gốc rõ ràng, luật dễ hiểu, cái giá thật, và chỗ cho nhân vật tỏa sáng theo cách riêng.

<short pause> Câu hỏi cho bạn: hệ thống sức mạnh yêu thích của bạn là gì, kể cả ngoài ba hệ này? <laugh> Viết xuống phần bình luận để Kaku làm video tiếp theo nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ xếp hạng các dạng Super Saiyan trong Dragon Ball, theo sức mạnh và cái giá.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: theo sáu tiêu chí, Nen đạt hai mươi chín điểm, Chú lực hai mươi sáu, và Chakra mười tám.

[pause] Nen thắng về luật, sự công bằng và sáng tạo. Chú lực thắng về nguồn năng lượng gắn với chủ đề. Chakra thắng về sự dễ hiểu và cảm xúc.

[pause] Và bài học chung: một hệ thống sức mạnh hay cần nguồn gốc rõ ràng, luật dễ hiểu, cái giá thật, và chỗ cho nhân vật tỏa sáng theo cách riêng.

[pause] [curious] Câu hỏi cho bạn: hệ thống sức mạnh yêu thích của bạn là gì, kể cả ngoài ba hệ này? [chuckles] Viết xuống phần bình luận để Kaku làm video tiếp theo nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ xếp hạng các dạng Super Saiyan trong Dragon Ball, theo sức mạnh và cái giá.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
