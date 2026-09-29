# Bộ prompt · Dragon Ball: Xếp hạng các dạng Super Saiyan theo sức mạnh và cái giá

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 96 ảnh, 7 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (96 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Dragon Ball Z, Dragon Ball Super đến arc Kẻ sống sót trên hành tinh và phim Super…

```text
Wide 16:9 landscape cinematic frame. a rocky wasteland at dusk with a single glowing golden light on the horizon. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Có lẽ không có biến hình nào nổi tiếng hơn khoảnh khắc mái tóc chuyển sang màu vàng, đôi mắt xanh lạnh lùng,…

```text
Wide 16:9 landscape cinematic frame. a silhouette with spiky hair turning golden, a blazing golden aura exploding upward against a dark sky. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đó là Super Saiyan. Nhưng từ lần đầu tiên xuất hiện tới nay, nó đã có hàng loạt phiên bản mới: tóc dài hơn, m…

```text
Wide 16:9 landscape cinematic frame. a lineup of silhouettes with auras of different colors: gold, red, blue, silver. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Hôm nay mình sẽ xếp hạng các dạng đó theo ba tiêu chí: sức mạnh, điều kiện kích hoạt, và cái giá phải trả. Kh…

```text
Wide 16:9 landscape cinematic frame. a ranking board with three columns labeled by icons: a fist, a key, and a price tag. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ sẽ thành một bảng xếp hạng, và mình sẽ đi từ dưới lên trên.

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook as its feathers flare slightly golden. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao dạng mạnh nhất chưa chắc là dạng tốt nhất, và vì sao có những dạng mà chính…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small scale balancing a golden flame and a price tag. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Nền tảng: người Saiyan và khí

Lời: Trước hết, người Saiyan là một tộc chiến binh ngoài hành tinh, sinh ra để chiến đấu. Họ mạnh lên sau mỗi trận…

```text
Wide 16:9 landscape cinematic frame. a warrior race silhouette with a tail standing on a cliff under a red planet sky. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Sức mạnh trong Dragon Ball được đo bằng khí, năng lượng bên trong cơ thể. Khí có thể dùng để bay, bắn chưởng,…

```text
Wide 16:9 landscape cinematic frame. a figure flying above clouds, a sphere of glowing energy forming in their hands. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Biến hình là cách người Saiyan nhân sức mạnh của mình lên nhiều lần trong một thời gian ngắn. Mỗi dạng biến h…

```text
Wide 16:9 landscape cinematic frame. a staircase where each step multiplies in size, glowing brighter as it rises. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nhưng biến hình không miễn phí. Nó tiêu hao thể lực, và càng lên cao, cơ thể càng phải chịu áp lực lớn hơn.

```text
Wide 16:9 landscape cinematic frame. a figure breathing heavily with a flickering aura, sweat dripping, cracks in the ground around them. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Dragon Ball ít luật chi tiết hơn Nen hay Chú lực, nên bảng xếp hạng này dựa trên những gì truyệ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adjusting its glasses and holding up a notebook labeled with a small star. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Hạng 10: Super Saiyan

Lời: Đứng ở nền móng là dạng kinh điển: Super Saiyan. Tóc dựng đứng màu vàng, mắt xanh, hào quang vàng rực.

```text
Wide 16:9 landscape cinematic frame. a spiky-haired silhouette with golden hair and a steady golden aura, rocky battlefield. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Điều kiện kích hoạt lần đầu: một cơn giận dữ cực độ, thường là khi mất đi người thân yêu. Goku biến hình lần…

```text
Wide 16:9 landscape cinematic frame. a kneeling figure screaming as lightning strikes around them and their hair begins to turn gold. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Theo các sách hướng dẫn chính thức, Super Saiyan tăng sức mạnh lên khoảng năm mươi lần so với trạng thái thườ…

```text
Wide 16:9 landscape cinematic frame. a multiplier gauge jumping dramatically, a glowing x50 symbol. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Cái giá: ban đầu, dạng này tiêu hao nhiều thể lực và làm người dùng hung hăng hơn. Về sau, Goku và Gohan luyệ…

```text
Wide 16:9 landscape cinematic frame. two figures relaxing with golden hair at home, eating calmly, aura barely visible. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh thấp nhất bảng, điều kiện khó ở lần đầu, nhưng cái giá rẻ khi đã quen. Đây là nền tảng ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a golden card at the bottom of a ranking ladder. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Hạng 9: các cấp trung gian

Lời: Ngay sau Super Saiyan là những cấp trung gian mà nhiều fan hay quên: dạng cơ bắp phình to lên để tăng sức mạn…

```text
Wide 16:9 landscape cinematic frame. a golden-haired silhouette with visibly bulked muscles, aura dense and heavy. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Dạng này tăng sức mạnh, nhưng cơ bắp quá lớn khiến tốc độ giảm mạnh. Trong trận đấu thực tế, người dùng chậm…

```text
Wide 16:9 landscape cinematic frame. a massive muscular figure swinging slowly while a faster opponent dodges easily. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Đây là một bài học được chính truyện đưa ra: sức mạnh lớn hơn chưa chắc là tốt hơn, nếu đánh đổi mất thứ quan…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a huge muscle icon on one side and a lightning bolt icon on the other, tipping wrong. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh nhỉnh hơn một chút, nhưng cái giá là tốc độ, rất đắt trong chiến đấu. Vì vậy nó đứng thấp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to lift a giant dumbbell and toppling over. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Hạng 8: Super Saiyan 2

Lời: Super Saiyan 2 trông gần giống dạng đầu, nhưng tóc dựng hơn, hào quang có những tia điện xanh lóe lên.

```text
Wide 16:9 landscape cinematic frame. a golden-haired silhouette with sharper spikes and crackling blue electric sparks in the aura. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Lần xuất hiện nổi tiếng nhất là khi Gohan, còn là một cậu bé, bùng nổ trong trận đấu Cell Games sau khi chịu…

```text
Wide 16:9 landscape cinematic frame. a young fighter with electric sparks around him standing calmly over a battlefield, his aura crackling. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Theo sách hướng dẫn, Super Saiyan 2 mạnh gấp đôi Super Saiyan, tức khoảng một trăm lần trạng thái thường.

```text
Wide 16:9 landscape cinematic frame. a multiplier gauge showing a glowing x100 symbol. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Cái giá: tiêu hao thể lực nhiều hơn dạng đầu, và cần luyện tập hoặc một cú bộc phát cảm xúc rất lớn mới đạt đ…

```text
Wide 16:9 landscape cinematic frame. a tired figure kneeling with fading sparks, breathing hard. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là dạng cân bằng rất tốt. Mạnh hơn nhiều nhưng không đánh mất tốc độ như các cấp trung gian.

```text
Wide 16:9 landscape cinematic frame. the owl mascot giving a thumbs up with a small electric spark on its feather. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Hạng 7: Super Saiyan 3

Lời: Super Saiyan 3 là dạng dễ nhận ra nhất: tóc dài tới tận thắt lưng, lông mày biến mất, và hào quang cực lớn.

```text
Wide 16:9 landscape cinematic frame. a silhouette with extremely long golden hair reaching the waist, no eyebrows, massive aura. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Theo sách hướng dẫn, dạng này mạnh khoảng bốn trăm lần trạng thái thường, gấp bốn lần Super Saiyan 2.

```text
Wide 16:9 landscape cinematic frame. a multiplier gauge exploding upward to a glowing x400 symbol. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nhưng cái giá rất đắt: nó tiêu hao năng lượng cực nhanh. Truyện cho thấy Goku không duy trì được lâu, và việc…

```text
Wide 16:9 landscape cinematic frame. a figure whose long golden hair flickers as an energy bar drains rapidly beside them. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Có chi tiết thú vị: khi Goku dùng Super Saiyan 3 trong lúc chỉ còn ở dạng linh hồn, thời gian còn lại ở thế g…

```text
Wide 16:9 landscape cinematic frame. a spectral figure with a halo above his head and long golden hair, an hourglass emptying beside him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh cao, nhưng cái giá khiến nó ít hữu dụng trong trận đấu dài. Đây là ví dụ rõ nhất cho việc…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking worried at a rapidly draining battery icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Ngoại truyện: Super Saiyan 4

Lời: Trước khi đi tiếp, cần nhắc Super Saiyan 4, dạng xuất hiện trong Dragon Ball GT, với bộ lông đỏ và mái tóc đe…

```text
Wide 16:9 landscape cinematic frame. a silhouette with dark long hair and red fur on the upper body, a monkey tail, red aura. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Dạng này gắn với sức mạnh của khỉ đột khổng lồ nguyên thủy, và cần có đuôi để đạt được.

```text
Wide 16:9 landscape cinematic frame. a colossal golden ape silhouette under a full moon transforming into a smaller warrior form. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Vì Dragon Ball GT không nằm trong mạch truyện chính của Dragon Ball Super, Kaku để Super Saiyan 4 ở mục riêng…

```text
Wide 16:9 landscape cinematic frame. a separate display case holding a red-furred silhouette, apart from the main ranking ladder. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Dù vậy, rất nhiều fan coi đây là thiết kế đẹp nhất trong lịch sử Dragon Ball. Nếu bạn cũng vậy, hãy bình luận…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny red fur scarf, admiring its reflection. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Những dạng đặc biệt khác

Lời: Ngoài bảng xếp hạng chính, Dragon Ball còn có vài dạng đặc biệt chỉ xuất hiện ở một nhân vật, và mỗi dạng kể…

```text
Wide 16:9 landscape cinematic frame. a side gallery with three glowing silhouettes in display cases: green-gold, blue-gold, and red. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Super Saiyan huyền thoại là dạng của một chiến binh sinh ra với sức mạnh bẩm sinh khổng lồ, hào quang xanh lụ…

```text
Wide 16:9 landscape cinematic frame. a towering muscular silhouette with a green-gold aura roaring on a frozen battlefield. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Super Saiyan cuồng nộ là dạng xuất hiện khi một người trẻ tuổi dồn toàn bộ cơn giận và nỗi đau mất mát để bảo…

```text
Wide 16:9 landscape cinematic frame. a young swordsman silhouette with a blue-gold aura crackling violently in a ruined future city. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Và có một kỹ thuật không phải biến hình nhưng hay đi kèm: nhân sức mạnh lên nhiều lần bằng cách ép khí, đổi l…

```text
Wide 16:9 landscape cinematic frame. a figure wrapped in a violent red aura, veins glowing, the ground cracking beneath. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Những dạng này cho thấy một điều quen thuộc: mọi biến hình đều sinh ra từ một cảm xúc hoặc hoàn cảnh cụ thể,…

```text
Wide 16:9 landscape cinematic frame. three silhouettes in a row, each casting a long shadow shaped like a different emotion. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Hạng 6: Super Saiyan God

Lời: Bước sang Dragon Ball Super, biến hình không còn chỉ dựa vào cơn giận nữa. Super Saiyan God là dạng đầu tiên…

```text
Wide 16:9 landscape cinematic frame. a slimmer silhouette with crimson hair and a flickering red-orange aura, calm expression. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Điều kiện kích hoạt rất đặc biệt: cần một nghi lễ với năm người Saiyan có trái tim trong sáng truyền năng lượ…

```text
Wide 16:9 landscape cinematic frame. six figures in a circle holding hands, a column of light rising into the one at the center. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Dạng này không tăng cơ bắp, mà giúp người dùng cảm nhận và dùng khí thần, một loại năng lượng mà người thường…

```text
Wide 16:9 landscape cinematic frame. a figure surrounded by a subtle shimmering aura, while ordinary fighters around them look confused. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Cái giá: sức mạnh ban đầu chỉ tạm thời. Nhưng sau khi trải qua nó, cơ thể người dùng tiếp thu một phần khí th…

```text
Wide 16:9 landscape cinematic frame. a fading red aura leaving behind a faint glow inside a figure's chest. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: điều kiện khó nhất bảng vì cần năm người khác. Nhưng nó mở ra một tầng sức mạnh mới hoàn toàn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding hands with five small birds in a circle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Hạng 5: Super Saiyan Blue

Lời: Super Saiyan Blue kết hợp khí thần của dạng God với biến hình Super Saiyan. Tóc và hào quang chuyển sang màu…

```text
Wide 16:9 landscape cinematic frame. a silhouette with vivid blue spiky hair and a calm but intense blue aura, cosmic background. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Dạng này mạnh hơn hẳn các dạng trước, và giúp Goku và Vegeta đứng ngang hàng với những đối thủ cấp thần.

```text
Wide 16:9 landscape cinematic frame. two silhouettes with blue auras standing side by side facing a towering godlike figure. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Cái giá: nó đòi hỏi kiểm soát khí cực tốt và tiêu hao nhiều năng lượng. Mất bình tĩnh là lãng phí sức mạnh.

```text
Wide 16:9 landscape cinematic frame. a blue aura flickering unstably as a figure loses focus mid-battle. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Có một biến thể liều lĩnh: kết hợp Blue với kỹ thuật tăng sức mạnh gấp nhiều lần, đổi lại cơ thể chịu tổn thư…

```text
Wide 16:9 landscape cinematic frame. a blue aura wrapped in a violent red outer layer, veins glowing, cracks in the ground. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh rất cao, điều kiện là luyện tập nghiêm túc, cái giá vừa phải nếu biết kiểm soát. Đây là d…

```text
Wide 16:9 landscape cinematic frame. the owl mascot meditating calmly with a faint blue glow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Hạng 4: Bản năng vô cực

Lời: Bản năng vô cực không phải dạng Super Saiyan. Nó là một kỹ thuật của các thiên thần, nơi cơ thể tự phản ứng m…

```text
Wide 16:9 landscape cinematic frame. a silhouette with silver hair and a calm silver aura, moving effortlessly between incoming attacks. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Ở dạng này, người dùng né đòn và phản công theo bản năng, nhanh hơn cả ý nghĩ của đối thủ.

```text
Wide 16:9 landscape cinematic frame. a figure dodging a flurry of attacks with eyes closed, ghostly motion trails all around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Điều kiện: phải tách được cảm xúc khỏi chuyển động của cơ thể, điều mà ngay cả thần hủy diệt cũng thấy khó. G…

```text
Wide 16:9 landscape cinematic frame. a figure meditating in a quiet void, emotions drawn as fading shapes drifting away. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Cái giá: lúc đầu, cơ thể không chịu nổi và kiệt sức ngay sau khi dùng. Chỉ khi luyện đủ lâu mới duy trì được.

```text
Wide 16:9 landscape cinematic frame. a silver aura fading as a figure collapses exhausted onto a floating stone. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là dạng thú vị nhất về triết lý. Trong khi Super Saiyan dựa vào cơn giận, Bản năng vô cực l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting perfectly still as leaves swirl around it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Hạng 3: Bản ngã tối thượng

Lời: Nếu Goku chọn con đường của thiên thần, Vegeta chọn con đường của thần hủy diệt: Bản ngã tối thượng.

```text
Wide 16:9 landscape cinematic frame. a silhouette with dark purple hair and a violet aura, fierce expression, cosmic destruction energy. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Dạng này dựa trên niềm kiêu hãnh và bản năng chiến đấu. Người dùng càng chịu đòn, càng mạnh lên, và càng thíc…

```text
Wide 16:9 landscape cinematic frame. a battered figure grinning as their violet aura grows larger with each hit they take. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Đây là đối lập hoàn hảo với Bản năng vô cực: một bên né mọi đòn, một bên lao vào nhận đòn để mạnh hơn.

```text
Wide 16:9 landscape cinematic frame. a split image: a silver figure dodging gracefully and a violet figure charging headfirst. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Cái giá: cơ thể phải chịu tổn thương thật. Người dùng không tránh đòn, nên luôn đi trên ranh giới giữa sức mạ…

```text
Wide 16:9 landscape cinematic frame. a figure standing unsteadily covered in wounds, violet aura blazing brighter than ever. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh cực cao trong trận dài, nhưng cái giá là chính cơ thể. Nó hợp hoàn hảo với tính cách của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot flexing a tiny wing with a small purple flame, looking proud. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Hạng 2: Beast

Lời: Gohan, người từng là thiên tài mạnh nhất thế hệ trẻ, trở lại với một dạng mới trong phim Super Hero: Beast.

```text
Wide 16:9 landscape cinematic frame. a silhouette with tall spiky silver-white hair and glowing red eyes, a crimson-purple aura. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Dạng này thức tỉnh khi Gohan bùng nổ cảm xúc để bảo vệ người thân, giống như lần đầu cậu đạt Super Saiyan 2 n…

```text
Wide 16:9 landscape cinematic frame. a protective figure shielding a small child as their aura explodes and their hair turns silver-white. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nó được xem là giải phóng hoàn toàn tiềm năng bị ngủ quên của Gohan, thứ mà nhiều nhân vật đã nhắc tới từ rất…

```text
Wide 16:9 landscape cinematic frame. a locked door breaking open with blinding light pouring out. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Vì đây là dạng mới, truyện chưa cho biết nhiều về cái giá. Kaku sẽ không suy đoán quá nhiều, và chờ những gì…

```text
Wide 16:9 landscape cinematic frame. a question mark glowing next to a silver-haired silhouette. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: fan tranh cãi rất nhiều về việc Beast, Bản năng vô cực và Bản ngã tối thượng dạng nào mạnh hơn.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shrugging between three glowing silhouettes of silver, violet, and white. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Hạng 1: dạng hoàn thiện của Bản năng vô cực

Lời: Đứng đầu bảng của Kaku là dạng hoàn thiện của Bản năng vô cực, khi Goku làm chủ được kỹ thuật này và giữ được…

```text
Wide 16:9 landscape cinematic frame. a calm silver-haired silhouette standing in a vast arena, an overwhelming but serene silver aura. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Ở dạng hoàn thiện, cơ thể tự né và tự tấn công, cả phòng thủ lẫn tấn công đều vượt ngoài suy nghĩ.

```text
Wide 16:9 landscape cinematic frame. a figure landing a precise strike while dodging three attacks simultaneously, motion trails everywhere. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nó từng giúp Goku đứng ngang hàng với những đối thủ mạnh nhất vũ trụ trong Giải đấu sức mạnh.

```text
Wide 16:9 landscape cinematic frame. a crumbling floating arena in space, a single silver figure standing among falling debris. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Cái giá: điều kiện gần như không thể với người thường, cần sự bình tĩnh tuyệt đối và cơ thể được rèn luyện ở…

```text
Wide 16:9 landscape cinematic frame. a staircase of light stretching into infinity with a single figure near the top. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm: sức mạnh cao nhất bảng, điều kiện khó nhất, và cái giá là cả một hành trình. Đây là đỉnh cao của t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting perfectly still at the top of a tiny staircase, eyes closed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Những hiểu lầm về biến hình

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về các dạng biến hình.

```text
Wide 16:9 landscape cinematic frame. a notice board with four pinned cards marked with red question marks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hiểu lầm một: dạng sau luôn mạnh hơn dạng trước trong mọi tình huống. Không đúng. Dạng mạnh nhưng tiêu hao nh…

```text
Wide 16:9 landscape cinematic frame. a strong but exhausted figure losing to a calmer opponent who paced themselves. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Hiểu lầm hai: chỉ cần giận là biến hình được. Cơn giận chỉ là cánh cửa đầu tiên. Những dạng cao hơn cần luyện…

```text
Wide 16:9 landscape cinematic frame. a figure screaming in frustration while nothing happens, a training ground in the background. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Hiểu lầm ba: Bản năng vô cực là một dạng Super Saiyan. Thực ra nó là kỹ thuật của thiên thần, không gắn với d…

```text
Wide 16:9 landscape cinematic frame. a silver-haired figure beside a serene angel silhouette, both in the same calm stance. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hiểu lầm bốn: hệ số sức mạnh là con số chính thức mọi lúc. Những con số năm mươi, một trăm, bốn trăm lần đến…

```text
Wide 16:9 landscape cinematic frame. an old guidebook with faded numbers next to a new book with no numbers at all. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Trắc nghiệm: bạn hợp với dạng nào?

Lời: Giờ một trò vui: dựa trên tính cách, bạn hợp với dạng biến hình nào nhất? Chỉ là trò chơi thôi nhé.

```text
Wide 16:9 landscape cinematic frame. a quiz card with five glowing aura colors arranged in a circle. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn bùng nổ khi thấy bất công và luôn đứng ra bảo vệ người khác, Super Saiyan cổ điển là của bạn.

```text
Wide 16:9 landscape cinematic frame. a figure stepping in front of a smaller person as a golden aura flares. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nếu bạn điềm tĩnh, ít nói và thích làm chủ bản thân, Bản năng vô cực có lẽ hợp với bạn.

```text
Wide 16:9 landscape cinematic frame. a quiet figure meditating by a still lake, a faint silver glow. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu bạn kiêu hãnh, thích thử thách và càng bị dồn vào đường cùng càng hăng, Bản ngã tối thượng là lựa chọn.

```text
Wide 16:9 landscape cinematic frame. a proud figure grinning while surrounded by opponents, violet aura blazing. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Nếu bạn hiền lành nhưng sẽ không bao giờ để ai làm hại gia đình mình, có khi Beast đang ngủ yên trong bạn.

```text
Wide 16:9 landscape cinematic frame. a gentle figure reading a book to a child, a faint silver-white glow hidden behind them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thì chọn Super Saiyan cổ điển, vì màu vàng hợp với cặp kính của Kaku.

```text
Wide 16:9 landscape cinematic frame. the owl mascot with golden spiky feathers, admiring its reflection in a mirror. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Góc nhìn của Kaku: từ cơn giận đến sự bình tĩnh · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn toàn bộ bảng xếp hạng, có một câu chuyện thú vị mà Dragon Ball kể qua các dạng biến hình.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a long ranking ladder glowing from gold to silver. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Ở thời Dragon Ball Z, sức mạnh đến từ cơn giận: mất người thân, gào thét, tóc chuyển vàng. Cảm xúc càng mãnh…

```text
Wide 16:9 landscape cinematic frame. a screaming golden-haired figure with lightning and debris flying, raw emotion. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Ở Dragon Ball Super, sức mạnh cao nhất lại đến từ sự bình tĩnh và kỹ thuật. Người mạnh nhất không phải người…

```text
Wide 16:9 landscape cinematic frame. a calm silver-haired figure with closed eyes as chaos swirls harmlessly around them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Đây là sự trưởng thành của cả bộ truyện: từ một cậu bé chiến đấu bằng cảm xúc, thành một võ sĩ hiểu rằng kiểm…

```text
Wide 16:9 landscape cinematic frame. a timeline from an angry young fighter to a calm mature fighter meditating. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: So với các hệ thống mình từng giải thích, Dragon Ball ít luật nhất, nhưng có một thông điệp rõ ràng: vượt qua…

```text
Wide 16:9 landscape cinematic frame. a hexagon, a dark dome, a red eye, and a golden flame side by side, the golden flame reaching upward. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · Điều gì làm nên một biến hình hay?

Lời: Trước khi tổng kết, cùng nghĩ xem điều gì khiến một dạng biến hình trở nên đáng nhớ, không chỉ trong Dragon B…

```text
Wide 16:9 landscape cinematic frame. a sketchbook page with several transformation silhouettes and notes in the margins. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Thứ nhất là khoảnh khắc: biến hình đáng nhớ nhất luôn xuất hiện đúng lúc cảm xúc câu chuyện lên đỉnh điểm, kh…

```text
Wide 16:9 landscape cinematic frame. a dramatic moment frozen in time, a figure mid-transformation as friends watch in tears. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Thứ hai là thiết kế dễ nhận ra: chỉ cần nhìn bóng dáng hay màu tóc, người xem biết ngay đó là dạng nào.

```text
Wide 16:9 landscape cinematic frame. five silhouettes in a row distinguishable only by hair shape and aura color. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Thứ ba là cái giá: biến hình có giới hạn thì mỗi lần dùng đều căng thẳng. Biến hình vô hạn thì nhanh chóng tr…

```text
Wide 16:9 landscape cinematic frame. an hourglass placed next to a glowing aura, sand running out. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ Super Saiyan đầu tiên là ví dụ hoàn hảo cho cả ba điều. Đó là lý do nó vẫn là biểu tượng sau bao nh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot saluting a golden silhouette on a distant cliff at sunset. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · Tóm tắt

Lời: Tóm lại: từ Super Saiyan tới Super Saiyan 3, sức mạnh tăng khoảng năm mươi, một trăm, rồi bốn trăm lần, nhưng…

```text
Wide 16:9 landscape cinematic frame. a summary ladder of golden forms with multiplier icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92

Lời: Super Saiyan God và Blue đưa sức mạnh lên tầm thần. Bản năng vô cực và Bản ngã tối thượng là hai con đường đố…

```text
Wide 16:9 landscape cinematic frame. a split image of silver and violet auras facing each other. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93

Lời: Và theo bảng của Kaku, đứng đầu là dạng hoàn thiện của Bản năng vô cực, đỉnh cao của sự bình tĩnh.

```text
Wide 16:9 landscape cinematic frame. a single silver figure at the top of the ranking ladder glowing softly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: bạn xếp hạng các dạng này thế nào, và dạng biến hình yêu thích của bạn là gì? Viết xuống phầ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank ranking card and a pencil. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Hãy bình luận hệ thống sức mạnh bạn muốn Kaku giải mã tiếp theo.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a suggestion box glowing on a desk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye on a rocky cliff at sunset. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nền tảng: người Saiyan và khí

Khoảng 120 giây · cảnh s01–s11 · 1555 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Dragon Ball Z, Dragon Ball Super đến arc Kẻ sống sót trên hành tinh và phim Super Hero. Nếu chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Có lẽ không có biến hình nào nổi tiếng hơn khoảnh khắc mái tóc chuyển sang màu vàng, đôi mắt xanh lạnh lùng, và hào quang bùng lên như ngọn lửa.

<short pause> Đó là Super Saiyan. <short pause> Nhưng từ lần đầu tiên xuất hiện tới nay, nó đã có hàng loạt phiên bản mới: tóc dài hơn, màu đỏ, màu xanh, rồi cả những dạng không còn gọi là Super Saiyan nữa.

<short pause> Hôm nay mình sẽ xếp hạng các dạng đó theo ba tiêu chí: sức mạnh, điều kiện kích hoạt, và cái giá phải trả. Không chỉ ai mạnh hơn, mà còn đắt hơn.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ sẽ thành một bảng xếp hạng, và mình sẽ đi từ dưới lên trên.

<short pause> Xem hết video, bạn sẽ hiểu vì sao dạng mạnh nhất chưa chắc là dạng tốt nhất, và vì sao có những dạng mà chính nhân vật cũng hạn chế dùng.

<short pause> Trước hết, người Saiyan là một tộc chiến binh ngoài hành tinh, sinh ra để chiến đấu. Họ mạnh lên sau mỗi trận chiến, đặc biệt là sau khi hồi phục từ vết thương nặng.

<short pause> Sức mạnh trong Dragon Ball được đo bằng khí, năng lượng bên trong cơ thể. Khí có thể dùng để bay, bắn chưởng, và cảm nhận đối thủ.

<short pause> Biến hình là cách người Saiyan nhân sức mạnh của mình lên nhiều lần trong một thời gian ngắn. Mỗi dạng biến hình là một bước nhảy vọt.

<short pause> Nhưng biến hình không miễn phí. Nó tiêu hao thể lực, và càng lên cao, cơ thể càng phải chịu áp lực lớn hơn.

<short pause> Kaku ghi chú: Dragon Ball ít luật chi tiết hơn Nen hay Chú lực, nên bảng xếp hạng này dựa trên những gì truyện và phim thể hiện, cộng với ý kiến của Kaku.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Dragon Ball Z, Dragon Ball Super đến arc Kẻ sống sót trên hành tinh và phim Super Hero. Nếu chưa xem tới đó, hãy lưu video lại nhé.

[pause] Có lẽ không có biến hình nào nổi tiếng hơn khoảnh khắc mái tóc chuyển sang màu vàng, đôi mắt xanh lạnh lùng, và hào quang bùng lên như ngọn lửa.

[pause] Đó là Super Saiyan. [pause] Nhưng từ lần đầu tiên xuất hiện tới nay, nó đã có hàng loạt phiên bản mới: tóc dài hơn, màu đỏ, màu xanh, rồi cả những dạng không còn gọi là Super Saiyan nữa.

[pause] Hôm nay mình sẽ xếp hạng các dạng đó theo ba tiêu chí: sức mạnh, điều kiện kích hoạt, và cái giá phải trả. Không chỉ ai mạnh hơn, mà còn đắt hơn.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ sẽ thành một bảng xếp hạng, và mình sẽ đi từ dưới lên trên.

[pause] Xem hết video, bạn sẽ hiểu vì sao dạng mạnh nhất chưa chắc là dạng tốt nhất, và vì sao có những dạng mà chính nhân vật cũng hạn chế dùng.

[pause] Trước hết, người Saiyan là một tộc chiến binh ngoài hành tinh, sinh ra để chiến đấu. Họ mạnh lên sau mỗi trận chiến, đặc biệt là sau khi hồi phục từ vết thương nặng.

[pause] Sức mạnh trong Dragon Ball được đo bằng khí, năng lượng bên trong cơ thể. Khí có thể dùng để bay, bắn chưởng, và cảm nhận đối thủ.

[pause] Biến hình là cách người Saiyan nhân sức mạnh của mình lên nhiều lần trong một thời gian ngắn. Mỗi dạng biến hình là một bước nhảy vọt.

[pause] Nhưng biến hình không miễn phí. Nó tiêu hao thể lực, và càng lên cao, cơ thể càng phải chịu áp lực lớn hơn.

[pause] Kaku ghi chú: Dragon Ball ít luật chi tiết hơn Nen hay Chú lực, nên bảng xếp hạng này dựa trên những gì truyện và phim thể hiện, cộng với ý kiến của Kaku.
```

### c02 · Hạng 10: Super Saiyan / Hạng 9: các cấp trung gian / Hạng 8: Super Saiyan 2

Khoảng 133 giây · cảnh s12–s25 · 1729 ký tự

**Gemini**

```text
Đứng ở nền móng là dạng kinh điển: Super Saiyan. Tóc dựng đứng màu vàng, mắt xanh, hào quang vàng rực.

<short pause> Điều kiện kích hoạt lần đầu: một cơn giận dữ cực độ, thường là khi mất đi người thân yêu. Goku biến hình lần đầu trên hành tinh Namek khi chứng kiến bạn thân bị giết.

<short pause> Theo các sách hướng dẫn chính thức, Super Saiyan tăng sức mạnh lên khoảng năm mươi lần so với trạng thái thường.

<short pause> Cái giá: ban đầu, dạng này tiêu hao nhiều thể lực và làm người dùng hung hăng hơn. Về sau, Goku và Gohan luyện để giữ trạng thái này liên tục mà không mệt.

<short pause> <laugh> Kaku chấm: sức mạnh thấp nhất bảng, điều kiện khó ở lần đầu, nhưng cái giá rẻ khi đã quen. Đây là nền tảng cho mọi dạng phía sau.

<short pause> Ngay sau Super Saiyan là những cấp trung gian mà nhiều fan hay quên: dạng cơ bắp phình to lên để tăng sức mạnh thô.

<short pause> Dạng này tăng sức mạnh, nhưng cơ bắp quá lớn khiến tốc độ giảm mạnh. Trong trận đấu thực tế, người dùng chậm tới mức không đánh trúng ai.

<short pause> Đây là một bài học được chính truyện đưa ra: sức mạnh lớn hơn chưa chắc là tốt hơn, nếu đánh đổi mất thứ quan trọng khác.

<short pause> Kaku chấm: sức mạnh nhỉnh hơn một chút, nhưng cái giá là tốc độ, rất đắt trong chiến đấu. Vì vậy nó đứng thấp trong bảng của Kaku.

<short pause> Super Saiyan 2 trông gần giống dạng đầu, nhưng tóc dựng hơn, hào quang có những tia điện xanh lóe lên.

<short pause> Lần xuất hiện nổi tiếng nhất là khi Gohan, còn là một cậu bé, bùng nổ trong trận đấu Cell Games sau khi chịu đựng quá nhiều đau đớn.

<short pause> Theo sách hướng dẫn, Super Saiyan 2 mạnh gấp đôi Super Saiyan, tức khoảng một trăm lần trạng thái thường.

<short pause> Cái giá: tiêu hao thể lực nhiều hơn dạng đầu, và cần luyện tập hoặc một cú bộc phát cảm xúc rất lớn mới đạt được.

<short pause> Kaku ghi chú: đây là dạng cân bằng rất tốt. Mạnh hơn nhiều nhưng không đánh mất tốc độ như các cấp trung gian.
```

**ElevenLabs**

```text
Đứng ở nền móng là dạng kinh điển: Super Saiyan. Tóc dựng đứng màu vàng, mắt xanh, hào quang vàng rực.

[pause] Điều kiện kích hoạt lần đầu: một cơn giận dữ cực độ, thường là khi mất đi người thân yêu. Goku biến hình lần đầu trên hành tinh Namek khi chứng kiến bạn thân bị giết.

[pause] Theo các sách hướng dẫn chính thức, Super Saiyan tăng sức mạnh lên khoảng năm mươi lần so với trạng thái thường.

[pause] Cái giá: ban đầu, dạng này tiêu hao nhiều thể lực và làm người dùng hung hăng hơn. Về sau, Goku và Gohan luyện để giữ trạng thái này liên tục mà không mệt.

[pause] [chuckles] Kaku chấm: sức mạnh thấp nhất bảng, điều kiện khó ở lần đầu, nhưng cái giá rẻ khi đã quen. Đây là nền tảng cho mọi dạng phía sau.

[pause] Ngay sau Super Saiyan là những cấp trung gian mà nhiều fan hay quên: dạng cơ bắp phình to lên để tăng sức mạnh thô.

[pause] Dạng này tăng sức mạnh, nhưng cơ bắp quá lớn khiến tốc độ giảm mạnh. Trong trận đấu thực tế, người dùng chậm tới mức không đánh trúng ai.

[pause] Đây là một bài học được chính truyện đưa ra: sức mạnh lớn hơn chưa chắc là tốt hơn, nếu đánh đổi mất thứ quan trọng khác.

[pause] Kaku chấm: sức mạnh nhỉnh hơn một chút, nhưng cái giá là tốc độ, rất đắt trong chiến đấu. Vì vậy nó đứng thấp trong bảng của Kaku.

[pause] Super Saiyan 2 trông gần giống dạng đầu, nhưng tóc dựng hơn, hào quang có những tia điện xanh lóe lên.

[pause] Lần xuất hiện nổi tiếng nhất là khi Gohan, còn là một cậu bé, bùng nổ trong trận đấu Cell Games sau khi chịu đựng quá nhiều đau đớn.

[pause] Theo sách hướng dẫn, Super Saiyan 2 mạnh gấp đôi Super Saiyan, tức khoảng một trăm lần trạng thái thường.

[pause] Cái giá: tiêu hao thể lực nhiều hơn dạng đầu, và cần luyện tập hoặc một cú bộc phát cảm xúc rất lớn mới đạt được.

[pause] Kaku ghi chú: đây là dạng cân bằng rất tốt. Mạnh hơn nhiều nhưng không đánh mất tốc độ như các cấp trung gian.
```

### c03 · Hạng 7: Super Saiyan 3 / Ngoại truyện: Super Saiyan 4 / Những dạng đặc biệt khác

Khoảng 137 giây · cảnh s26–s39 · 1780 ký tự

**Gemini**

```text
Super Saiyan 3 là dạng dễ nhận ra nhất: tóc dài tới tận thắt lưng, lông mày biến mất, và hào quang cực lớn.

<short pause> Theo sách hướng dẫn, dạng này mạnh khoảng bốn trăm lần trạng thái thường, gấp bốn lần Super Saiyan 2.

<short pause> Nhưng cái giá rất đắt: nó tiêu hao năng lượng cực nhanh. Truyện cho thấy Goku không duy trì được lâu, và việc biến hình còn mất thời gian.

<short pause> Có chi tiết thú vị: khi Goku dùng Super Saiyan 3 trong lúc chỉ còn ở dạng linh hồn, thời gian còn lại ở thế giới người sống bị rút ngắn.

<short pause> <laugh> Kaku chấm: sức mạnh cao, nhưng cái giá khiến nó ít hữu dụng trong trận đấu dài. Đây là ví dụ rõ nhất cho việc mạnh chưa chắc là tốt.

<short pause> Trước khi đi tiếp, cần nhắc Super Saiyan 4, dạng xuất hiện trong Dragon Ball GT, với bộ lông đỏ và mái tóc đen dài.

<short pause> Dạng này gắn với sức mạnh của khỉ đột khổng lồ nguyên thủy, và cần có đuôi để đạt được.

<short pause> Vì Dragon Ball GT không nằm trong mạch truyện chính của Dragon Ball Super, Kaku để Super Saiyan 4 ở mục riêng, không xếp chung bảng.

<short pause> Dù vậy, rất nhiều fan coi đây là thiết kế đẹp nhất trong lịch sử Dragon Ball. Nếu bạn cũng vậy, hãy bình luận để Kaku biết nhé.

<short pause> Ngoài bảng xếp hạng chính, Dragon Ball còn có vài dạng đặc biệt chỉ xuất hiện ở một nhân vật, và mỗi dạng kể một câu chuyện riêng.

<short pause> Super Saiyan huyền thoại là dạng của một chiến binh sinh ra với sức mạnh bẩm sinh khổng lồ, hào quang xanh lục và cơ thể phình to vì cơn thịnh nộ không kiểm soát.

<short pause> Super Saiyan cuồng nộ là dạng xuất hiện khi một người trẻ tuổi dồn toàn bộ cơn giận và nỗi đau mất mát để bảo vệ những gì còn lại.

<short pause> Và có một kỹ thuật không phải biến hình nhưng hay đi kèm: nhân sức mạnh lên nhiều lần bằng cách ép khí, đổi lại cơ thể phải chịu áp lực khủng khiếp.

<short pause> Những dạng này cho thấy một điều quen thuộc: mọi biến hình đều sinh ra từ một cảm xúc hoặc hoàn cảnh cụ thể, và đều có mặt trái của nó.
```

**ElevenLabs**

```text
Super Saiyan 3 là dạng dễ nhận ra nhất: tóc dài tới tận thắt lưng, lông mày biến mất, và hào quang cực lớn.

[pause] Theo sách hướng dẫn, dạng này mạnh khoảng bốn trăm lần trạng thái thường, gấp bốn lần Super Saiyan 2.

[pause] Nhưng cái giá rất đắt: nó tiêu hao năng lượng cực nhanh. Truyện cho thấy Goku không duy trì được lâu, và việc biến hình còn mất thời gian.

[pause] Có chi tiết thú vị: khi Goku dùng Super Saiyan 3 trong lúc chỉ còn ở dạng linh hồn, thời gian còn lại ở thế giới người sống bị rút ngắn.

[pause] [chuckles] Kaku chấm: sức mạnh cao, nhưng cái giá khiến nó ít hữu dụng trong trận đấu dài. Đây là ví dụ rõ nhất cho việc mạnh chưa chắc là tốt.

[pause] Trước khi đi tiếp, cần nhắc Super Saiyan 4, dạng xuất hiện trong Dragon Ball GT, với bộ lông đỏ và mái tóc đen dài.

[pause] Dạng này gắn với sức mạnh của khỉ đột khổng lồ nguyên thủy, và cần có đuôi để đạt được.

[pause] Vì Dragon Ball GT không nằm trong mạch truyện chính của Dragon Ball Super, Kaku để Super Saiyan 4 ở mục riêng, không xếp chung bảng.

[pause] Dù vậy, rất nhiều fan coi đây là thiết kế đẹp nhất trong lịch sử Dragon Ball. Nếu bạn cũng vậy, hãy bình luận để Kaku biết nhé.

[pause] Ngoài bảng xếp hạng chính, Dragon Ball còn có vài dạng đặc biệt chỉ xuất hiện ở một nhân vật, và mỗi dạng kể một câu chuyện riêng.

[pause] Super Saiyan huyền thoại là dạng của một chiến binh sinh ra với sức mạnh bẩm sinh khổng lồ, hào quang xanh lục và cơ thể phình to vì cơn thịnh nộ không kiểm soát.

[pause] Super Saiyan cuồng nộ là dạng xuất hiện khi một người trẻ tuổi dồn toàn bộ cơn giận và nỗi đau mất mát để bảo vệ những gì còn lại.

[pause] Và có một kỹ thuật không phải biến hình nhưng hay đi kèm: nhân sức mạnh lên nhiều lần bằng cách ép khí, đổi lại cơ thể phải chịu áp lực khủng khiếp.

[pause] Những dạng này cho thấy một điều quen thuộc: mọi biến hình đều sinh ra từ một cảm xúc hoặc hoàn cảnh cụ thể, và đều có mặt trái của nó.
```

### c04 · Hạng 6: Super Saiyan God / Hạng 5: Super Saiyan Blue / Hạng 4: Bản năng vô cực

Khoảng 142 giây · cảnh s40–s54 · 1851 ký tự

**Gemini**

```text
Bước sang Dragon Ball Super, biến hình không còn chỉ dựa vào cơn giận nữa. Super Saiyan God là dạng đầu tiên mang sức mạnh của thần.

<short pause> Điều kiện kích hoạt rất đặc biệt: cần một nghi lễ với năm người Saiyan có trái tim trong sáng truyền năng lượng cho người thứ sáu.

<short pause> Dạng này không tăng cơ bắp, mà giúp người dùng cảm nhận và dùng khí thần, một loại năng lượng mà người thường không cảm nhận được.

<short pause> Cái giá: sức mạnh ban đầu chỉ tạm thời. <short pause> Nhưng sau khi trải qua nó, cơ thể người dùng tiếp thu một phần khí thần, nền tảng cho các dạng tiếp theo.

<short pause> <laugh> Kaku chấm: điều kiện khó nhất bảng vì cần năm người khác. <short pause> Nhưng nó mở ra một tầng sức mạnh mới hoàn toàn.

<short pause> Super Saiyan Blue kết hợp khí thần của dạng God với biến hình Super Saiyan. Tóc và hào quang chuyển sang màu xanh.

<short pause> Dạng này mạnh hơn hẳn các dạng trước, và giúp Goku và Vegeta đứng ngang hàng với những đối thủ cấp thần.

<short pause> Cái giá: nó đòi hỏi kiểm soát khí cực tốt và tiêu hao nhiều năng lượng. Mất bình tĩnh là lãng phí sức mạnh.

<short pause> Có một biến thể liều lĩnh: kết hợp Blue với kỹ thuật tăng sức mạnh gấp nhiều lần, đổi lại cơ thể chịu tổn thương nặng nếu kéo dài.

<short pause> Kaku chấm: sức mạnh rất cao, điều kiện là luyện tập nghiêm túc, cái giá vừa phải nếu biết kiểm soát. Đây là dạng cân bằng nhất ở tầng thần.

<short pause> Bản năng vô cực không phải dạng Super Saiyan. Nó là một kỹ thuật của các thiên thần, nơi cơ thể tự phản ứng mà không cần suy nghĩ.

<short pause> Ở dạng này, người dùng né đòn và phản công theo bản năng, nhanh hơn cả ý nghĩ của đối thủ.

<short pause> Điều kiện: phải tách được cảm xúc khỏi chuyển động của cơ thể, điều mà ngay cả thần hủy diệt cũng thấy khó. Goku mất rất lâu mới làm chủ được.

<short pause> Cái giá: lúc đầu, cơ thể không chịu nổi và kiệt sức ngay sau khi dùng. Chỉ khi luyện đủ lâu mới duy trì được.

<short pause> Kaku ghi chú: đây là dạng thú vị nhất về triết lý. Trong khi Super Saiyan dựa vào cơn giận, Bản năng vô cực lại mạnh nhờ sự bình tĩnh tuyệt đối.
```

**ElevenLabs**

```text
Bước sang Dragon Ball Super, biến hình không còn chỉ dựa vào cơn giận nữa. Super Saiyan God là dạng đầu tiên mang sức mạnh của thần.

[pause] Điều kiện kích hoạt rất đặc biệt: cần một nghi lễ với năm người Saiyan có trái tim trong sáng truyền năng lượng cho người thứ sáu.

[pause] Dạng này không tăng cơ bắp, mà giúp người dùng cảm nhận và dùng khí thần, một loại năng lượng mà người thường không cảm nhận được.

[pause] Cái giá: sức mạnh ban đầu chỉ tạm thời. [pause] Nhưng sau khi trải qua nó, cơ thể người dùng tiếp thu một phần khí thần, nền tảng cho các dạng tiếp theo.

[pause] [chuckles] Kaku chấm: điều kiện khó nhất bảng vì cần năm người khác. [pause] Nhưng nó mở ra một tầng sức mạnh mới hoàn toàn.

[pause] Super Saiyan Blue kết hợp khí thần của dạng God với biến hình Super Saiyan. Tóc và hào quang chuyển sang màu xanh.

[pause] Dạng này mạnh hơn hẳn các dạng trước, và giúp Goku và Vegeta đứng ngang hàng với những đối thủ cấp thần.

[pause] Cái giá: nó đòi hỏi kiểm soát khí cực tốt và tiêu hao nhiều năng lượng. Mất bình tĩnh là lãng phí sức mạnh.

[pause] Có một biến thể liều lĩnh: kết hợp Blue với kỹ thuật tăng sức mạnh gấp nhiều lần, đổi lại cơ thể chịu tổn thương nặng nếu kéo dài.

[pause] Kaku chấm: sức mạnh rất cao, điều kiện là luyện tập nghiêm túc, cái giá vừa phải nếu biết kiểm soát. Đây là dạng cân bằng nhất ở tầng thần.

[pause] Bản năng vô cực không phải dạng Super Saiyan. Nó là một kỹ thuật của các thiên thần, nơi cơ thể tự phản ứng mà không cần suy nghĩ.

[pause] Ở dạng này, người dùng né đòn và phản công theo bản năng, nhanh hơn cả ý nghĩ của đối thủ.

[pause] Điều kiện: phải tách được cảm xúc khỏi chuyển động của cơ thể, điều mà ngay cả thần hủy diệt cũng thấy khó. Goku mất rất lâu mới làm chủ được.

[pause] Cái giá: lúc đầu, cơ thể không chịu nổi và kiệt sức ngay sau khi dùng. Chỉ khi luyện đủ lâu mới duy trì được.

[pause] Kaku ghi chú: đây là dạng thú vị nhất về triết lý. Trong khi Super Saiyan dựa vào cơn giận, Bản năng vô cực lại mạnh nhờ sự bình tĩnh tuyệt đối.
```

### c05 · Hạng 3: Bản ngã tối thượng / Hạng 2: Beast / Hạng 1: dạng hoàn thiện của Bản năng vô cực

Khoảng 138 giây · cảnh s55–s69 · 1788 ký tự

**Gemini**

```text
Nếu Goku chọn con đường của thiên thần, Vegeta chọn con đường của thần hủy diệt: Bản ngã tối thượng.

<short pause> Dạng này dựa trên niềm kiêu hãnh và bản năng chiến đấu. Người dùng càng chịu đòn, càng mạnh lên, và càng thích thú với trận đấu.

<short pause> Đây là đối lập hoàn hảo với Bản năng vô cực: một bên né mọi đòn, một bên lao vào nhận đòn để mạnh hơn.

<short pause> Cái giá: cơ thể phải chịu tổn thương thật. Người dùng không tránh đòn, nên luôn đi trên ranh giới giữa sức mạnh và gục ngã.

<short pause> <laugh> Kaku chấm: sức mạnh cực cao trong trận dài, nhưng cái giá là chính cơ thể. Nó hợp hoàn hảo với tính cách của Vegeta.

<short pause> Gohan, người từng là thiên tài mạnh nhất thế hệ trẻ, trở lại với một dạng mới trong phim Super Hero: Beast.

<short pause> Dạng này thức tỉnh khi Gohan bùng nổ cảm xúc để bảo vệ người thân, giống như lần đầu cậu đạt Super Saiyan 2 nhiều năm trước.

<short pause> Nó được xem là giải phóng hoàn toàn tiềm năng bị ngủ quên của Gohan, thứ mà nhiều nhân vật đã nhắc tới từ rất lâu.

<short pause> Vì đây là dạng mới, truyện chưa cho biết nhiều về cái giá. Kaku sẽ không suy đoán quá nhiều, và chờ những gì truyện kể tiếp.

<short pause> Kaku ghi chú: fan tranh cãi rất nhiều về việc Beast, Bản năng vô cực và Bản ngã tối thượng dạng nào mạnh hơn. Thứ tự ở đây là ý kiến của Kaku, không phải kết luận chính thức.

<short pause> Đứng đầu bảng của Kaku là dạng hoàn thiện của Bản năng vô cực, khi Goku làm chủ được kỹ thuật này và giữ được nó trong chiến đấu thật.

<short pause> Ở dạng hoàn thiện, cơ thể tự né và tự tấn công, cả phòng thủ lẫn tấn công đều vượt ngoài suy nghĩ.

<short pause> Nó từng giúp Goku đứng ngang hàng với những đối thủ mạnh nhất vũ trụ trong Giải đấu sức mạnh.

<short pause> Cái giá: điều kiện gần như không thể với người thường, cần sự bình tĩnh tuyệt đối và cơ thể được rèn luyện ở tầm thiên thần.

<short pause> Kaku chấm: sức mạnh cao nhất bảng, điều kiện khó nhất, và cái giá là cả một hành trình. Đây là đỉnh cao của triết lý bình tĩnh.
```

**ElevenLabs**

```text
Nếu Goku chọn con đường của thiên thần, Vegeta chọn con đường của thần hủy diệt: Bản ngã tối thượng.

[pause] Dạng này dựa trên niềm kiêu hãnh và bản năng chiến đấu. Người dùng càng chịu đòn, càng mạnh lên, và càng thích thú với trận đấu.

[pause] Đây là đối lập hoàn hảo với Bản năng vô cực: một bên né mọi đòn, một bên lao vào nhận đòn để mạnh hơn.

[pause] Cái giá: cơ thể phải chịu tổn thương thật. Người dùng không tránh đòn, nên luôn đi trên ranh giới giữa sức mạnh và gục ngã.

[pause] [chuckles] Kaku chấm: sức mạnh cực cao trong trận dài, nhưng cái giá là chính cơ thể. Nó hợp hoàn hảo với tính cách của Vegeta.

[pause] Gohan, người từng là thiên tài mạnh nhất thế hệ trẻ, trở lại với một dạng mới trong phim Super Hero: Beast.

[pause] Dạng này thức tỉnh khi Gohan bùng nổ cảm xúc để bảo vệ người thân, giống như lần đầu cậu đạt Super Saiyan 2 nhiều năm trước.

[pause] Nó được xem là giải phóng hoàn toàn tiềm năng bị ngủ quên của Gohan, thứ mà nhiều nhân vật đã nhắc tới từ rất lâu.

[pause] Vì đây là dạng mới, truyện chưa cho biết nhiều về cái giá. Kaku sẽ không suy đoán quá nhiều, và chờ những gì truyện kể tiếp.

[pause] Kaku ghi chú: fan tranh cãi rất nhiều về việc Beast, Bản năng vô cực và Bản ngã tối thượng dạng nào mạnh hơn. Thứ tự ở đây là ý kiến của Kaku, không phải kết luận chính thức.

[pause] Đứng đầu bảng của Kaku là dạng hoàn thiện của Bản năng vô cực, khi Goku làm chủ được kỹ thuật này và giữ được nó trong chiến đấu thật.

[pause] Ở dạng hoàn thiện, cơ thể tự né và tự tấn công, cả phòng thủ lẫn tấn công đều vượt ngoài suy nghĩ.

[pause] Nó từng giúp Goku đứng ngang hàng với những đối thủ mạnh nhất vũ trụ trong Giải đấu sức mạnh.

[pause] Cái giá: điều kiện gần như không thể với người thường, cần sự bình tĩnh tuyệt đối và cơ thể được rèn luyện ở tầm thiên thần.

[pause] Kaku chấm: sức mạnh cao nhất bảng, điều kiện khó nhất, và cái giá là cả một hành trình. Đây là đỉnh cao của triết lý bình tĩnh.
```

### c06 · Những hiểu lầm về biến hình / Trắc nghiệm: bạn hợp với dạng nào? / Góc nhìn của Kaku: từ cơn giận đến sự bình tĩnh

Khoảng 148 giây · cảnh s70–s85 · 1930 ký tự

**Gemini**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về các dạng biến hình.

<short pause> Hiểu lầm một: dạng sau luôn mạnh hơn dạng trước trong mọi tình huống. Không đúng. Dạng mạnh nhưng tiêu hao nhanh có thể thua trong một trận đánh dài.

<short pause> Hiểu lầm hai: chỉ cần giận là biến hình được. Cơn giận chỉ là cánh cửa đầu tiên. Những dạng cao hơn cần luyện tập, kiểm soát và cả điều kiện đặc biệt.

<short pause> Hiểu lầm ba: Bản năng vô cực là một dạng Super Saiyan. Thực ra nó là kỹ thuật của thiên thần, không gắn với dòng máu Saiyan.

<short pause> Hiểu lầm bốn: hệ số sức mạnh là con số chính thức mọi lúc. Những con số năm mươi, một trăm, bốn trăm lần đến từ sách hướng dẫn, và về sau truyện không còn dùng chúng nữa.

<short pause> Giờ một trò vui: dựa trên tính cách, bạn hợp với dạng biến hình nào nhất? Chỉ là trò chơi thôi nhé.

<short pause> Nếu bạn bùng nổ khi thấy bất công và luôn đứng ra bảo vệ người khác, Super Saiyan cổ điển là của bạn.

<short pause> Nếu bạn điềm tĩnh, ít nói và thích làm chủ bản thân, Bản năng vô cực có lẽ hợp với bạn.

<short pause> Nếu bạn kiêu hãnh, thích thử thách và càng bị dồn vào đường cùng càng hăng, Bản ngã tối thượng là lựa chọn.

<short pause> Nếu bạn hiền lành nhưng sẽ không bao giờ để ai làm hại gia đình mình, có khi Beast đang ngủ yên trong bạn.

<short pause> <laugh> Kaku thì chọn Super Saiyan cổ điển, vì màu vàng hợp với cặp kính của Kaku.

<short pause> Nhìn toàn bộ bảng xếp hạng, có một câu chuyện thú vị mà Dragon Ball kể qua các dạng biến hình.

<short pause> Ở thời Dragon Ball Z, sức mạnh đến từ cơn giận: mất người thân, gào thét, tóc chuyển vàng. Cảm xúc càng mãnh liệt, sức mạnh càng lớn.

<short pause> Ở Dragon Ball Super, sức mạnh cao nhất lại đến từ sự bình tĩnh và kỹ thuật. Người mạnh nhất không phải người giận dữ nhất, mà là người điềm tĩnh nhất.

<short pause> Đây là sự trưởng thành của cả bộ truyện: từ một cậu bé chiến đấu bằng cảm xúc, thành một võ sĩ hiểu rằng kiểm soát bản thân mới là sức mạnh thật.

<short pause> So với các hệ thống mình từng giải thích, Dragon Ball ít luật nhất, nhưng có một thông điệp rõ ràng: vượt qua giới hạn của chính mình là con đường không bao giờ kết thúc.
```

**ElevenLabs**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về các dạng biến hình.

[pause] Hiểu lầm một: dạng sau luôn mạnh hơn dạng trước trong mọi tình huống. Không đúng. Dạng mạnh nhưng tiêu hao nhanh có thể thua trong một trận đánh dài.

[pause] Hiểu lầm hai: chỉ cần giận là biến hình được. Cơn giận chỉ là cánh cửa đầu tiên. Những dạng cao hơn cần luyện tập, kiểm soát và cả điều kiện đặc biệt.

[pause] Hiểu lầm ba: Bản năng vô cực là một dạng Super Saiyan. Thực ra nó là kỹ thuật của thiên thần, không gắn với dòng máu Saiyan.

[pause] Hiểu lầm bốn: hệ số sức mạnh là con số chính thức mọi lúc. Những con số năm mươi, một trăm, bốn trăm lần đến từ sách hướng dẫn, và về sau truyện không còn dùng chúng nữa.

[pause] [curious] Giờ một trò vui: dựa trên tính cách, bạn hợp với dạng biến hình nào nhất? Chỉ là trò chơi thôi nhé.

[pause] Nếu bạn bùng nổ khi thấy bất công và luôn đứng ra bảo vệ người khác, Super Saiyan cổ điển là của bạn.

[pause] Nếu bạn điềm tĩnh, ít nói và thích làm chủ bản thân, Bản năng vô cực có lẽ hợp với bạn.

[pause] Nếu bạn kiêu hãnh, thích thử thách và càng bị dồn vào đường cùng càng hăng, Bản ngã tối thượng là lựa chọn.

[pause] Nếu bạn hiền lành nhưng sẽ không bao giờ để ai làm hại gia đình mình, có khi Beast đang ngủ yên trong bạn.

[pause] [chuckles] Kaku thì chọn Super Saiyan cổ điển, vì màu vàng hợp với cặp kính của Kaku.

[pause] Nhìn toàn bộ bảng xếp hạng, có một câu chuyện thú vị mà Dragon Ball kể qua các dạng biến hình.

[pause] Ở thời Dragon Ball Z, sức mạnh đến từ cơn giận: mất người thân, gào thét, tóc chuyển vàng. Cảm xúc càng mãnh liệt, sức mạnh càng lớn.

[pause] Ở Dragon Ball Super, sức mạnh cao nhất lại đến từ sự bình tĩnh và kỹ thuật. Người mạnh nhất không phải người giận dữ nhất, mà là người điềm tĩnh nhất.

[pause] Đây là sự trưởng thành của cả bộ truyện: từ một cậu bé chiến đấu bằng cảm xúc, thành một võ sĩ hiểu rằng kiểm soát bản thân mới là sức mạnh thật.

[pause] So với các hệ thống mình từng giải thích, Dragon Ball ít luật nhất, nhưng có một thông điệp rõ ràng: vượt qua giới hạn của chính mình là con đường không bao giờ kết thúc.
```

### c07 · Điều gì làm nên một biến hình hay? / Tóm tắt

Khoảng 96 giây · cảnh s86–s96 · 1254 ký tự

**Gemini**

```text
Trước khi tổng kết, cùng nghĩ xem điều gì khiến một dạng biến hình trở nên đáng nhớ, không chỉ trong Dragon Ball mà trong mọi bộ truyện.

<short pause> Thứ nhất là khoảnh khắc: biến hình đáng nhớ nhất luôn xuất hiện đúng lúc cảm xúc câu chuyện lên đỉnh điểm, không phải lúc ngẫu nhiên.

<short pause> Thứ hai là thiết kế dễ nhận ra: chỉ cần nhìn bóng dáng hay màu tóc, người xem biết ngay đó là dạng nào.

<short pause> Thứ ba là cái giá: biến hình có giới hạn thì mỗi lần dùng đều căng thẳng. Biến hình vô hạn thì nhanh chóng trở nên nhàm chán.

<short pause> <laugh> Kaku nghĩ Super Saiyan đầu tiên là ví dụ hoàn hảo cho cả ba điều. Đó là lý do nó vẫn là biểu tượng sau bao nhiêu năm.

<short pause> Tóm lại: từ Super Saiyan tới Super Saiyan 3, sức mạnh tăng khoảng năm mươi, một trăm, rồi bốn trăm lần, nhưng cái giá về thể lực cũng tăng theo.

<short pause> Super Saiyan God và Blue đưa sức mạnh lên tầm thần. Bản năng vô cực và Bản ngã tối thượng là hai con đường đối lập: né mọi đòn và nhận mọi đòn.

<short pause> Và theo bảng của Kaku, đứng đầu là dạng hoàn thiện của Bản năng vô cực, đỉnh cao của sự bình tĩnh.

<short pause> Câu hỏi cho bạn: bạn xếp hạng các dạng này thế nào, và dạng biến hình yêu thích của bạn là gì? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. Hãy bình luận hệ thống sức mạnh bạn muốn Kaku giải mã tiếp theo.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi tổng kết, cùng nghĩ xem điều gì khiến một dạng biến hình trở nên đáng nhớ, không chỉ trong Dragon Ball mà trong mọi bộ truyện.

[pause] Thứ nhất là khoảnh khắc: biến hình đáng nhớ nhất luôn xuất hiện đúng lúc cảm xúc câu chuyện lên đỉnh điểm, không phải lúc ngẫu nhiên.

[pause] Thứ hai là thiết kế dễ nhận ra: chỉ cần nhìn bóng dáng hay màu tóc, người xem biết ngay đó là dạng nào.

[pause] Thứ ba là cái giá: biến hình có giới hạn thì mỗi lần dùng đều căng thẳng. Biến hình vô hạn thì nhanh chóng trở nên nhàm chán.

[pause] [chuckles] Kaku nghĩ Super Saiyan đầu tiên là ví dụ hoàn hảo cho cả ba điều. Đó là lý do nó vẫn là biểu tượng sau bao nhiêu năm.

[pause] Tóm lại: từ Super Saiyan tới Super Saiyan 3, sức mạnh tăng khoảng năm mươi, một trăm, rồi bốn trăm lần, nhưng cái giá về thể lực cũng tăng theo.

[pause] Super Saiyan God và Blue đưa sức mạnh lên tầm thần. Bản năng vô cực và Bản ngã tối thượng là hai con đường đối lập: né mọi đòn và nhận mọi đòn.

[pause] Và theo bảng của Kaku, đứng đầu là dạng hoàn thiện của Bản năng vô cực, đỉnh cao của sự bình tĩnh.

[pause] [curious] Câu hỏi cho bạn: bạn xếp hạng các dạng này thế nào, và dạng biến hình yêu thích của bạn là gì? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. Hãy bình luận hệ thống sức mạnh bạn muốn Kaku giải mã tiếp theo.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
