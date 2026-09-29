# Bộ prompt · Jujutsu Kaisen: Bành trướng lãnh địa hoạt động thế nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 93 ảnh, 8 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo: video có spoiler Jujutsu Kaisen đến arc Trò chơi tử thần, đúng phần anime đang chiếu. Chưa xem tới…

```text
Wide 16:9 landscape cinematic frame. a dark stage with a single spotlight on a sealed shrine door covered in glowing talismans. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong Jujutsu Kaisen, có một kỹ thuật mà khi được tung ra, trận đấu gần như kết thúc ngay lập tức. Đối thủ kh…

```text
Wide 16:9 landscape cinematic frame. a sorcerer silhouette forming a hand sign while a dark sphere of space closes around a battlefield. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Kỹ thuật đó là Bành trướng lãnh địa. Nhưng nếu nó mạnh tới vậy, tại sao không phải ai cũng dùng, và tại sao v…

```text
Wide 16:9 landscape cinematic frame. a glowing dome barrier swallowing a ruined city block at night, dramatic scale. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã lãnh địa: nó được tạo ra thế nào, luật tất trúng, cách ph…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook, a small dome diagram floating above the pages. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao một trận đấu lãnh địa giống ván cờ hơn là màn so ai đấm mạnh.

```text
Wide 16:9 landscape cinematic frame. the owl mascot moving a chess piece shaped like a tiny dome across a glowing board. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Chú lực và thuật thức

Lời: Muốn hiểu lãnh địa, trước hết cần hai khái niệm. Thứ nhất là chú lực: năng lượng sinh ra từ cảm xúc tiêu cực…

```text
Wide 16:9 landscape cinematic frame. a crowd silhouette emitting dark purple wisps of energy rising into a stormy sky. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Người thường rò rỉ chú lực mà không biết, và chính phần rò rỉ đó sinh ra chú linh, những thứ quái vật các chú…

```text
Wide 16:9 landscape cinematic frame. dark energy gathering in a school hallway corner and forming a grotesque shadow creature. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Thứ hai là thuật thức: năng lực bẩm sinh khắc sẵn trong cơ thể một người. Chú lực là nhiên liệu, thuật thức l…

```text
Wide 16:9 landscape cinematic frame. a glowing engine diagram where purple fuel flows into an ornate mechanism. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Phần lớn thuật thức chỉ có vậy: một năng lực, dùng khi cần. Nhưng ở đỉnh cao của chú thuật, người ta có thể l…

```text
Wide 16:9 landscape cinematic frame. a staircase of glowing steps leading up to a closed temple gate at the top. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Đỉnh cao đó là biến thuật thức của mình thành một thế giới thu nhỏ, nơi luật của mình là luật duy nhất.

```text
Wide 16:9 landscape cinematic frame. a miniature floating world inside a glass sphere held in an open palm. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Lãnh địa là gì?

Lời: Bành trướng lãnh địa là dùng chú lực dựng lên một kết giới, rồi lấp đầy bên trong bằng thế giới nội tâm của n…

```text
Wide 16:9 landscape cinematic frame. a barrier forming like ink spreading across the sky, revealing a surreal inner world inside. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Mỗi lãnh địa trông khác nhau vì nó phản ánh tâm hồn người tạo ra nó: có nơi là biển cát, có nơi là không gian…

```text
Wide 16:9 landscape cinematic frame. a triptych of surreal landscapes: an endless beach, a starry void, a courtroom floating in darkness. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Để triển khai, người dùng thường kết một thủ ấn bằng tay. Thủ ấn giúp tập trung, giống như chìa khóa mở cánh…

```text
Wide 16:9 landscape cinematic frame. close-up of two hands forming an intricate sign, faint glowing lines tracing the fingers. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Bên trong lãnh địa, người dùng được tăng sức mạnh, còn thuật thức của họ được nạp sẵn vào không gian. Đây là…

```text
Wide 16:9 landscape cinematic frame. a sorcerer silhouette at the center of a domain, glowing symbols embedded into every surface around. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Nạp sẵn nghĩa là gì? Nghĩa là đòn đánh không cần bay tới mục tiêu nữa. Nó đã ở đó, ở mọi nơi trong lãnh địa.

```text
Wide 16:9 landscape cinematic frame. countless glowing symbols floating everywhere in a dark space, all pointed inward at a small figure. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Luật tất trúng

Lời: Đây là luật làm lãnh địa đáng sợ: đòn tấn công bằng thuật thức bên trong lãnh địa sẽ tất trúng. Không có khái…

```text
Wide 16:9 landscape cinematic frame. a small figure trying to run inside a dome while glowing marks appear on them from every direction. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Với một người mạnh, chỉ cần một đòn trúng chắc chắn là đủ. Vì vậy trong truyện, lãnh địa được gọi là đỉnh cao…

```text
Wide 16:9 landscape cinematic frame. a single glowing strike landing with a shockwave ring inside a dark dome. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Hãy tưởng tượng một ván cờ mà đối thủ được đi liên tục, còn bạn không được di chuyển. Đó là cảm giác bị kéo v…

```text
Wide 16:9 landscape cinematic frame. a chessboard where one side's pieces glow and move while the other side's pieces are frozen in ice. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nhưng tất trúng cũng có điều kiện: đòn đánh phải là thuật thức được nạp vào lãnh địa. Nắm đấm thường thì vẫn…

```text
Wide 16:9 landscape cinematic frame. a split diagram: glowing technique arrows that cannot be blocked versus a plain fist being blocked by a raised arm. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Và lãnh địa rất tốn chú lực. Dựng nó lên một lần đã là cả gánh nặng, duy trì lâu còn nặng hơn.

```text
Wide 16:9 landscape cinematic frame. a sorcerer silhouette kneeling and breathing hard as the dome around them flickers. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ví von: lãnh địa giống một chiêu tất tay trong bài. Tung đúng lúc thì thắng, tung sai lúc thì mình cạn s…

```text
Wide 16:9 landscape cinematic frame. the owl mascot slamming a glowing card on a table, surprised expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Cách chống lại lãnh địa

Lời: Nếu lãnh địa mạnh như vậy, làm sao sống sót? Trong truyện có vài cách, và mỗi cách đều có cái giá riêng.

```text
Wide 16:9 landscape cinematic frame. a lone figure standing inside an enemy dome, looking around calmly, several glowing options floating. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Cách thứ nhất: dựng lãnh địa của mình. Khi hai lãnh địa va nhau, bên nào tinh xảo hơn sẽ lấn át bên kia. Đây…

```text
Wide 16:9 landscape cinematic frame. two domes colliding in the sky, their surfaces grinding against each other with sparks. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Tranh chấp không đo ai nhiều chú lực hơn, mà đo lãnh địa nào được xây chặt chẽ hơn. Người tinh tế có thể thắn…

```text
Wide 16:9 landscape cinematic frame. two glowing blueprints overlapping, one intricate and detailed, one rough and simple, the intricate one glowing brighter. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Cách thứ hai: giản dị lãnh địa. Đây là một vùng nhỏ bao quanh người dùng, không tấn công ai, chỉ để vô hiệu h…

```text
Wide 16:9 landscape cinematic frame. a small circle of calm light around a sword stance figure, dark symbols dissolving at its edge. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Giản dị lãnh địa được xem là kỹ thuật của kẻ yếu, vì nó giúp người không dựng được lãnh địa vẫn có cơ hội sốn…

```text
Wide 16:9 landscape cinematic frame. a humble dojo scroll being passed from a teacher silhouette to a student silhouette. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Cách thứ ba: các kỹ thuật bí truyền của những gia tộc lớn, dùng để phản đòn tất trúng ngay khi nó chạm vào ng…

```text
Wide 16:9 landscape cinematic frame. petals of light bursting from a figure's body to counter incoming dark marks. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Cách thứ tư: khuếch đại lãnh địa. Người dùng bọc cơ thể trong một lớp lãnh địa mỏng, vô hiệu hóa thuật thức n…

```text
Wide 16:9 landscape cinematic frame. a figure wrapped in a thin shimmering film of liquid-like energy, incoming techniques dissolving on contact. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Cái giá là: trong lúc khuếch đại, người dùng không thể dùng thuật thức của chính mình. Được phòng thủ thì mất…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a shield on one side and a crossed-out sword on the other. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Cách thứ năm, cách thô bạo nhất: phá kết giới từ bên ngoài. Kết giới lãnh địa thường được thiết kế để giữ ngư…

```text
Wide 16:9 landscape cinematic frame. a giant fist of energy cracking a dome surface from outside, light leaking through cracks. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: đánh lại bằng lãnh địa, che mình bằng giản dị lãnh địa, phản đòn bằng bí truyền, bọc mình bằng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a neat chart of five glowing icons on a chalkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Cái giá: thuật thức bị cháy

Lời: Sau khi lãnh địa kết thúc, người dùng thường không thể dùng thuật thức trong một khoảng thời gian. Fan gọi hi…

```text
Wide 16:9 landscape cinematic frame. a burnt-out engine glowing faintly red, smoke rising, inside a dim workshop. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Đây là lý do lãnh địa không phải chiêu mở màn. Tung ra mà không kết liễu được đối thủ thì người dùng rơi vào…

```text
Wide 16:9 landscape cinematic frame. a sorcerer silhouette standing in a collapsing dome while the enemy rises from the dust. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trong truyện có nhân vật dùng sức mạnh hồi phục để chữa lại phần não bị cháy, rút ngắn thời gian chờ. Nhưng đ…

```text
Wide 16:9 landscape cinematic frame. a glowing brain diagram with warm healing light repairing charred lines. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Vì thế các trận đấu lãnh địa luôn có nhịp: ai dựng trước, ai chịu được lâu hơn, ai còn sức khi cả hai lãnh đị…

```text
Wide 16:9 landscape cinematic frame. a timeline diagram of two glowing bars rising and collapsing at different moments. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Lãnh địa không hoàn chỉnh và lãnh địa mở

Lời: Không phải lãnh địa nào cũng hoàn hảo. Có những lãnh địa chưa hoàn chỉnh: dựng được không gian nhưng chưa có…

```text
Wide 16:9 landscape cinematic frame. a half-built dome with missing panels, shadows pouring in through gaps. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Lãnh địa chưa hoàn chỉnh vẫn hữu ích, nhất là khi dùng để tranh chấp, nhưng nó không phải chiêu kết liễu.

```text
Wide 16:9 landscape cinematic frame. an unfinished barrier holding back a larger dome, cracks spreading on both. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Ở chiều ngược lại là thứ gần như không tưởng: lãnh địa không có kết giới. Người dùng vẽ thế giới của mình thẳ…

```text
Wide 16:9 landscape cinematic frame. an artist silhouette painting a dark shrine directly onto the sky without any canvas frame. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Trong truyện, kỹ thuật này được ví như vẽ tranh lên không khí thay vì lên giấy. Chỉ kẻ ở đẳng cấp cao nhất mớ…

```text
Wide 16:9 landscape cinematic frame. a brush stroke of glowing ink floating in mid-air over a city, forming a giant temple silhouette. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Vì không có kết giới giam giữ, lãnh địa này có thể phủ cả một vùng rộng. Đổi lại, người dùng để lại cho đối t…

```text
Wide 16:9 landscape cinematic frame. an aerial view of a city with a vast circle of destruction, a single escape path glowing at its edge. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Để lại đường thoát không phải vì tử tế. Đó là một giao ước: chấp nhận bất lợi nhỏ để đổi lấy sức mạnh lớn hơn…

```text
Wide 16:9 landscape cinematic frame. a contract scroll with a small door symbol drawn on it, glowing seal. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Những lãnh địa trong Trò chơi tử thần

Lời: Arc Trò chơi tử thần mang tới những lãnh địa rất lạ, cho thấy lãnh địa không nhất thiết là để giết ngay.

```text
Wide 16:9 landscape cinematic frame. a surreal casino hall and a floating courtroom side by side in a dark void. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Có một lãnh địa vận hành như một tòa án. Bên trong, không ai được dùng bạo lực. Mọi thứ được quyết định bằng…

```text
Wide 16:9 landscape cinematic frame. a floating courtroom with a giant judge silhouette, both parties standing in glowing boxes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Nếu bị kết tội, bị cáo có thể bị tịch thu thuật thức. Với một chú thuật sư, mất thuật thức còn đáng sợ hơn bị…

```text
Wide 16:9 landscape cinematic frame. a glowing emblem being pulled out of a figure's chest by a chain into a judge's hand. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Lãnh địa tòa án cho thấy tất trúng không phải là tất sát. Hiệu ứng chắc chắn xảy ra là phiên tòa, còn kết quả…

```text
Wide 16:9 landscape cinematic frame. a scale of justice glowing inside a dome, two possible outcomes floating on each side. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Một lãnh địa khác lại giống máy chơi may rủi. Người dùng quay số, và nếu trúng lớn, họ nhận được sức mạnh gần…

```text
Wide 16:9 landscape cinematic frame. a giant glowing slot machine inside a dome, reels spinning, lights flashing. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nghe có vẻ tùy hứng, nhưng chính yếu tố may rủi là một phần luật. Đối thủ bị buộc phải chơi cùng, dù họ có mu…

```text
Wide 16:9 landscape cinematic frame. a reluctant opponent silhouette forced to watch spinning reels, chains around their feet. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Những lãnh địa này chứng minh một điều: lãnh địa phản ánh con người. Người mê công lý dựng tòa án, người mê m…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a person as a courtroom on one side and a casino on the other. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: phần này dựa trên những gì anime và truyện đã kể tới arc Trò chơi tử thần. Chi tiết nào chưa rõ, m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a small warning sign with a spoiler icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Hai lãnh địa nổi tiếng nhất

Lời: Nói về lãnh địa thì không thể bỏ qua hai lãnh địa được nhắc nhiều nhất trong truyện. Chúng đại diện cho hai t…

```text
Wide 16:9 landscape cinematic frame. two contrasting domes side by side: one filled with infinite stars, one with a dark shrine and blades. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Lãnh địa thứ nhất là Vô lượng không xứ. Bên trong là một không gian vô tận, và đối thủ bị ép tiếp nhận một lư…

```text
Wide 16:9 landscape cinematic frame. a vast cosmic void with endless streams of light pouring into a tiny frozen figure. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kết quả là đối thủ đứng im. Không phải vì bị trói, mà vì não không xử lý kịp. Họ nhìn thấy mọi thứ, nên không…

```text
Wide 16:9 landscape cinematic frame. close-up of wide frozen eyes reflecting countless stars and symbols, stillness. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Đó là kiểu lãnh địa vô hiệu hóa: không cần chém, chỉ cần làm đối thủ tê liệt, rồi người dùng muốn làm gì cũng…

```text
Wide 16:9 landscape cinematic frame. a calm silhouette walking slowly toward a frozen opponent inside a starry void. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Lãnh địa thứ hai là Phục ma ngự trù tử. Đây chính là lãnh địa không kết giới mà mình vừa nói. Bên trong là mộ…

```text
Wide 16:9 landscape cinematic frame. a dark ornate shrine rising from a ruined landscape, endless thin slashes cutting through the air. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Mọi thứ trong phạm vi đều bị chém không ngừng cho tới khi tan thành từng mảnh. Đây là kiểu lãnh địa hủy diệt…

```text
Wide 16:9 landscape cinematic frame. buildings being sliced into countless clean pieces by invisible blades, debris suspended in air. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Hai lãnh địa này cho thấy hai con đường: một bên khóa đối thủ bằng thông tin, một bên xóa sổ bằng sức hủy diệ…

```text
Wide 16:9 landscape cinematic frame. a split composition: a frozen figure in starlight on the left, a storm of blades on the right. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: khi hai lãnh địa kiểu này đối đầu, câu hỏi không còn là ai mạnh hơn, mà là lãnh địa của ai được…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing two overlapping circles on a chalkboard with a question mark in the middle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Vì sao không phải ai cũng dựng được lãnh địa?

Lời: Nếu lãnh địa mạnh như vậy, sao không phải chú thuật sư nào cũng học nó? Câu trả lời: vì nó đòi hỏi ba thứ cùn…

```text
Wide 16:9 landscape cinematic frame. three locked gates standing in a row on a misty mountain path. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Thứ nhất là lượng chú lực khổng lồ. Dựng cả một thế giới tốn hơn rất nhiều so với tung vài đòn thuật thức.

```text
Wide 16:9 landscape cinematic frame. a massive reservoir of purple energy draining rapidly into a growing dome. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Thứ hai là khả năng kiểm soát cực kỳ chính xác. Kết giới phải kín, thế giới bên trong phải ổn định, và thuật…

```text
Wide 16:9 landscape cinematic frame. a craftsman silhouette assembling a delicate glass sphere with tiny glowing tools. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Thứ ba là hiểu rõ bản thân. Vì lãnh địa là thế giới nội tâm, người không hiểu mình sẽ không thể hình dung ra…

```text
Wide 16:9 landscape cinematic frame. a figure standing before a mirror that shows a blurry, unfinished landscape. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Đó là lý do trong truyện, người dựng được lãnh địa hoàn chỉnh được xem là thuộc hàng mạnh nhất, dù họ là ngườ…

```text
Wide 16:9 landscape cinematic frame. a small group of powerful silhouettes standing on a high cliff above a crowd. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Và cũng vì thế, một nhân vật mới học được lãnh địa thường là bước ngoặt lớn của câu chuyện. Nó cho thấy họ đã…

```text
Wide 16:9 landscape cinematic frame. a young sorcerer silhouette opening their eyes as a new dome forms around them for the first time. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Một trận tranh chấp lãnh địa diễn ra thế nào

Lời: Để dễ hình dung, hãy tua chậm một trận tranh chấp lãnh địa theo từng giây, dựa trên cách truyện thường miêu t…

```text
Wide 16:9 landscape cinematic frame. a film strip unrolling with frames showing two figures and two growing domes. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Giây đầu tiên: cả hai kết thủ ấn gần như cùng lúc. Hai kết giới bắt đầu mọc lên và chồng lên nhau trong cùng…

```text
Wide 16:9 landscape cinematic frame. two figures forming hand signs simultaneously, two translucent domes beginning to overlap. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Những giây tiếp theo: hai thế giới nội tâm giành nhau từng mét. Chỗ nào lãnh địa tinh xảo hơn thì bắt đầu lấn…

```text
Wide 16:9 landscape cinematic frame. a boundary line between two textures, stars and blades, shifting as one side pushes forward. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nếu một bên bị lấn hoàn toàn, lãnh địa của họ vỡ. Hiệu ứng tất trúng của bên thắng lập tức có hiệu lực.

```text
Wide 16:9 landscape cinematic frame. one dome shattering like glass while the other expands to fill the whole space. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Nếu không ai lấn được ai, cả hai cùng hao chú lực rất nhanh. Người cạn trước sẽ phải bỏ lãnh địa và chịu thuậ…

```text
Wide 16:9 landscape cinematic frame. two exhausted figures kneeling as both domes flicker and fade at the same time. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Vì vậy ngay cả khi thua tranh chấp, người thông minh vẫn có thể cố tình kéo dài để đối thủ cũng cạn sức theo…

```text
Wide 16:9 landscape cinematic frame. a figure smiling faintly while holding a cracked barrier, the opponent sweating. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Lịch sử: kỹ thuật chống lãnh địa cổ xưa

Lời: Lãnh địa không phải phát minh mới. Trong truyện, các chú thuật sư từ thời xa xưa đã biết tới nó, và cũng đã n…

```text
Wide 16:9 landscape cinematic frame. an ancient scroll painting of robed sorcerers facing a dark dome under a full moon. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Có một kỹ thuật cổ gọi là Không bát, tạo ra một chiếc giỏ đan quanh người dùng, giúp trung hòa hiệu ứng tất t…

```text
Wide 16:9 landscape cinematic frame. a glowing woven basket pattern of light forming around a meditating figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Giản dị lãnh địa ngày nay được xem như phiên bản dễ học hơn của những kỹ thuật cổ này, để nhiều chú thuật sư…

```text
Wide 16:9 landscape cinematic frame. an old scroll transforming into a modern notebook, the same circle diagram on both. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Điểm chung của các kỹ thuật phòng thủ: chúng không đánh bại lãnh địa. Chúng chỉ giúp bạn sống đủ lâu để lãnh…

```text
Wide 16:9 landscape cinematic frame. an hourglass inside a dome, a small shielded figure waiting as the sand runs low. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Đây là chi tiết rất đời: trong chiến đấu thật, sống sót đôi khi quan trọng hơn chiến thắng.

```text
Wide 16:9 landscape cinematic frame. a lone survivor silhouette walking out of dust at sunrise. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Thử nghiệm: nếu bạn bị kéo vào lãnh địa

Lời: Giờ thử đặt mình vào vị trí một chú thuật sư bình thường. Bạn bị kéo vào lãnh địa của một đối thủ mạnh hơn. B…

```text
Wide 16:9 landscape cinematic frame. a first-person view looking up as a dark dome closes overhead, hands raised. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bước một: đừng hoảng. Xác định đây là lãnh địa hoàn chỉnh hay chưa. Nếu chưa có tất trúng, bạn vẫn còn đánh đ…

```text
Wide 16:9 landscape cinematic frame. a checklist floating in the air with the first item glowing, a calm figure reading it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bước hai: nếu bạn biết giản dị lãnh địa, dựng nó ngay. Mục tiêu không phải thắng, mà là không để đòn tất trún…

```text
Wide 16:9 landscape cinematic frame. a figure dropping into a low stance as a small circle of light forms around their feet. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Bước ba: tính thời gian. Lãnh địa rất tốn sức, đối thủ không duy trì mãi được. Sau khi nó sụp, thuật thức của…

```text
Wide 16:9 landscape cinematic frame. a countdown timer glowing above a trembling dome, cracks forming. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Bước bốn: tận dụng khoảnh khắc đó. Đối thủ vừa mất thuật thức tạm thời, đây là cơ hội duy nhất để phản công.

```text
Wide 16:9 landscape cinematic frame. a figure dashing forward through dissolving dome fragments toward an exhausted opponent. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nghe đơn giản, nhưng trong truyện, rất ít người làm được đủ cả bốn bước. Phần lớn đã thua ở bước một vì không…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shaking its head slowly, holding the checklist. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Góc nhìn của Kaku: vì sao lãnh địa hay · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ tới phần mình thích nhất: vì sao lãnh địa là một ý tưởng hay trong thiết kế hệ thống sức mạnh?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of books, several dome diagrams floating around, thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Lý do thứ nhất: nó tạo ra kịch tính có luật. Người xem biết khi lãnh địa mở, có người sắp gặp nguy. Căng thẳn…

```text
Wide 16:9 landscape cinematic frame. a clock counting down inside a dark dome, figures bracing themselves. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Lý do thứ hai: có phản đòn rõ ràng. Mạnh cỡ nào cũng có cách chống. Nhờ vậy nhân vật yếu hơn vẫn có đường sốn…

```text
Wide 16:9 landscape cinematic frame. a small figure holding a glowing circle of calm light against a towering dome. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Lý do thứ ba: có cái giá. Thuật thức bị cháy sau khi dùng khiến mỗi lần mở lãnh địa là một quyết định lớn, kh…

```text
Wide 16:9 landscape cinematic frame. a burning candle next to a closed dome, the candle almost gone. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Lý do thứ tư: lãnh địa kể chuyện về nhân vật. Nhìn lãnh địa của ai đó, bạn hiểu họ nghĩ gì về thế giới.

```text
Wide 16:9 landscape cinematic frame. a gallery of framed surreal landscapes, each labeled only with a small icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Nhưng cũng có điểm yếu: khi quá nhiều nhân vật có lãnh địa, cảm giác đặc biệt có thể giảm đi. Đây là thách th…

```text
Wide 16:9 landscape cinematic frame. rows of many identical domes on a landscape, the viewer feeling less impressed. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Nếu so với Nen mà mình đã giải thích ở video trước, lãnh địa giống một dạng giao ước cực lớn: đổi thật nhiều…

```text
Wide 16:9 landscape cinematic frame. a split diagram: a glowing hexagon on one side and a dark dome on the other, a chain connecting them. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · Tóm tắt

Lời: Tóm lại: chú lực là nhiên liệu, thuật thức là cỗ máy, và lãnh địa là biến cả thế giới xung quanh thành cỗ máy…

```text
Wide 16:9 landscape cinematic frame. a summary diagram: fuel, engine, and a world-sized dome, arranged left to right. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Bên trong lãnh địa, thuật thức tất trúng. Để sống sót, bạn cần lãnh địa của riêng mình, giản dị lãnh địa, bí…

```text
Wide 16:9 landscape cinematic frame. five small glowing icons arranged around a dome in a circle. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Và mọi lãnh địa đều có giá: tốn chú lực, thuật thức bị cháy, hoặc phải chừa đường thoát cho đối thủ.

```text
Wide 16:9 landscape cinematic frame. three price tags hanging from a dark dome, glowing softly. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có lãnh địa riêng, thế giới nội tâm của bạn sẽ trông như thế nào? Viết xuống phần bình l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking curiously at a small glowing snow globe containing an unknown world. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã ma thuật trong Frieren, nơi phép thuật có cả l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at an ancient spellbook glowing on a lectern. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye in a warm library at night. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Chú lực và thuật thức / Lãnh địa là gì?

Khoảng 148 giây · cảnh s01–s15 · 1925 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen đến arc Trò chơi tử thần, đúng phần anime đang chiếu. Chưa xem tới đó thì bạn lưu video lại nhé.

<short pause> Trong Jujutsu Kaisen, có một kỹ thuật mà khi được tung ra, trận đấu gần như kết thúc ngay lập tức. Đối thủ không thể né, không thể chạy.

<short pause> Kỹ thuật đó là Bành trướng lãnh địa. <short pause> Nhưng nếu nó mạnh tới vậy, tại sao không phải ai cũng dùng, và tại sao vẫn có người thoát được?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã lãnh địa: nó được tạo ra thế nào, luật tất trúng, cách phá, và cái giá phải trả.

<short pause> Xem hết video, bạn sẽ hiểu vì sao một trận đấu lãnh địa giống ván cờ hơn là màn so ai đấm mạnh.

<short pause> Muốn hiểu lãnh địa, trước hết cần hai khái niệm. Thứ nhất là chú lực: năng lượng sinh ra từ cảm xúc tiêu cực như sợ hãi, giận dữ, oán hận.

<short pause> Người thường rò rỉ chú lực mà không biết, và chính phần rò rỉ đó sinh ra chú linh, những thứ quái vật các chú thuật sư phải tiêu diệt.

<short pause> Thứ hai là thuật thức: năng lực bẩm sinh khắc sẵn trong cơ thể một người. Chú lực là nhiên liệu, thuật thức là cỗ máy dùng nhiên liệu đó.

<short pause> Phần lớn thuật thức chỉ có vậy: một năng lực, dùng khi cần. <short pause> Nhưng ở đỉnh cao của chú thuật, người ta có thể làm nhiều hơn thế.

<short pause> Đỉnh cao đó là biến thuật thức của mình thành một thế giới thu nhỏ, nơi luật của mình là luật duy nhất.

<short pause> Bành trướng lãnh địa là dùng chú lực dựng lên một kết giới, rồi lấp đầy bên trong bằng thế giới nội tâm của người dùng, gọi là sinh đắc lãnh vực.

<short pause> Mỗi lãnh địa trông khác nhau vì nó phản ánh tâm hồn người tạo ra nó: có nơi là biển cát, có nơi là không gian vô tận, có nơi là một tòa án.

<short pause> Để triển khai, người dùng thường kết một thủ ấn bằng tay. Thủ ấn giúp tập trung, giống như chìa khóa mở cánh cửa thế giới bên trong.

<short pause> Bên trong lãnh địa, người dùng được tăng sức mạnh, còn thuật thức của họ được nạp sẵn vào không gian. Đây là điều quan trọng nhất.

<short pause> Nạp sẵn nghĩa là gì? Nghĩa là đòn đánh không cần bay tới mục tiêu nữa. Nó đã ở đó, ở mọi nơi trong lãnh địa.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen đến arc Trò chơi tử thần, đúng phần anime đang chiếu. Chưa xem tới đó thì bạn lưu video lại nhé.

[pause] Trong Jujutsu Kaisen, có một kỹ thuật mà khi được tung ra, trận đấu gần như kết thúc ngay lập tức. Đối thủ không thể né, không thể chạy.

[pause] Kỹ thuật đó là Bành trướng lãnh địa. [pause] [curious] Nhưng nếu nó mạnh tới vậy, tại sao không phải ai cũng dùng, và tại sao vẫn có người thoát được?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã lãnh địa: nó được tạo ra thế nào, luật tất trúng, cách phá, và cái giá phải trả.

[pause] Xem hết video, bạn sẽ hiểu vì sao một trận đấu lãnh địa giống ván cờ hơn là màn so ai đấm mạnh.

[pause] Muốn hiểu lãnh địa, trước hết cần hai khái niệm. Thứ nhất là chú lực: năng lượng sinh ra từ cảm xúc tiêu cực như sợ hãi, giận dữ, oán hận.

[pause] Người thường rò rỉ chú lực mà không biết, và chính phần rò rỉ đó sinh ra chú linh, những thứ quái vật các chú thuật sư phải tiêu diệt.

[pause] Thứ hai là thuật thức: năng lực bẩm sinh khắc sẵn trong cơ thể một người. Chú lực là nhiên liệu, thuật thức là cỗ máy dùng nhiên liệu đó.

[pause] Phần lớn thuật thức chỉ có vậy: một năng lực, dùng khi cần. [pause] Nhưng ở đỉnh cao của chú thuật, người ta có thể làm nhiều hơn thế.

[pause] Đỉnh cao đó là biến thuật thức của mình thành một thế giới thu nhỏ, nơi luật của mình là luật duy nhất.

[pause] Bành trướng lãnh địa là dùng chú lực dựng lên một kết giới, rồi lấp đầy bên trong bằng thế giới nội tâm của người dùng, gọi là sinh đắc lãnh vực.

[pause] Mỗi lãnh địa trông khác nhau vì nó phản ánh tâm hồn người tạo ra nó: có nơi là biển cát, có nơi là không gian vô tận, có nơi là một tòa án.

[pause] Để triển khai, người dùng thường kết một thủ ấn bằng tay. Thủ ấn giúp tập trung, giống như chìa khóa mở cánh cửa thế giới bên trong.

[pause] Bên trong lãnh địa, người dùng được tăng sức mạnh, còn thuật thức của họ được nạp sẵn vào không gian. Đây là điều quan trọng nhất.

[pause] Nạp sẵn nghĩa là gì? Nghĩa là đòn đánh không cần bay tới mục tiêu nữa. Nó đã ở đó, ở mọi nơi trong lãnh địa.
```

### c02 · Luật tất trúng / Cách chống lại lãnh địa

Khoảng 152 giây · cảnh s16–s31 · 1980 ký tự

**Gemini**

```text
Đây là luật làm lãnh địa đáng sợ: đòn tấn công bằng thuật thức bên trong lãnh địa sẽ tất trúng. Không có khái niệm né.

<short pause> Với một người mạnh, chỉ cần một đòn trúng chắc chắn là đủ. Vì vậy trong truyện, lãnh địa được gọi là đỉnh cao của chú thuật.

<short pause> Hãy tưởng tượng một ván cờ mà đối thủ được đi liên tục, còn bạn không được di chuyển. Đó là cảm giác bị kéo vào lãnh địa.

<short pause> Nhưng tất trúng cũng có điều kiện: đòn đánh phải là thuật thức được nạp vào lãnh địa. Nắm đấm thường thì vẫn có thể bị đỡ.

<short pause> Và lãnh địa rất tốn chú lực. Dựng nó lên một lần đã là cả gánh nặng, duy trì lâu còn nặng hơn.

<short pause> <laugh> Kaku ví von: lãnh địa giống một chiêu tất tay trong bài. Tung đúng lúc thì thắng, tung sai lúc thì mình cạn sạch lực.

<short pause> Nếu lãnh địa mạnh như vậy, làm sao sống sót? Trong truyện có vài cách, và mỗi cách đều có cái giá riêng.

<short pause> Cách thứ nhất: dựng lãnh địa của mình. Khi hai lãnh địa va nhau, bên nào tinh xảo hơn sẽ lấn át bên kia. Đây gọi là tranh chấp lãnh địa.

<short pause> Tranh chấp không đo ai nhiều chú lực hơn, mà đo lãnh địa nào được xây chặt chẽ hơn. Người tinh tế có thể thắng người mạnh hơn.

<short pause> Cách thứ hai: giản dị lãnh địa. Đây là một vùng nhỏ bao quanh người dùng, không tấn công ai, chỉ để vô hiệu hóa hiệu ứng tất trúng khi chạm vào.

<short pause> Giản dị lãnh địa được xem là kỹ thuật của kẻ yếu, vì nó giúp người không dựng được lãnh địa vẫn có cơ hội sống sót.

<short pause> Cách thứ ba: các kỹ thuật bí truyền của những gia tộc lớn, dùng để phản đòn tất trúng ngay khi nó chạm vào người.

<short pause> Cách thứ tư: khuếch đại lãnh địa. Người dùng bọc cơ thể trong một lớp lãnh địa mỏng, vô hiệu hóa thuật thức nào chạm vào mình.

<short pause> Cái giá là: trong lúc khuếch đại, người dùng không thể dùng thuật thức của chính mình. Được phòng thủ thì mất tấn công.

<short pause> Cách thứ năm, cách thô bạo nhất: phá kết giới từ bên ngoài. Kết giới lãnh địa thường được thiết kế để giữ người ở trong, nên từ ngoài phá vào dễ hơn.

<short pause> Kaku tóm lại: đánh lại bằng lãnh địa, che mình bằng giản dị lãnh địa, phản đòn bằng bí truyền, bọc mình bằng khuếch đại, hoặc nhờ đồng đội phá từ ngoài.
```

**ElevenLabs**

```text
Đây là luật làm lãnh địa đáng sợ: đòn tấn công bằng thuật thức bên trong lãnh địa sẽ tất trúng. Không có khái niệm né.

[pause] Với một người mạnh, chỉ cần một đòn trúng chắc chắn là đủ. Vì vậy trong truyện, lãnh địa được gọi là đỉnh cao của chú thuật.

[pause] Hãy tưởng tượng một ván cờ mà đối thủ được đi liên tục, còn bạn không được di chuyển. Đó là cảm giác bị kéo vào lãnh địa.

[pause] Nhưng tất trúng cũng có điều kiện: đòn đánh phải là thuật thức được nạp vào lãnh địa. Nắm đấm thường thì vẫn có thể bị đỡ.

[pause] Và lãnh địa rất tốn chú lực. Dựng nó lên một lần đã là cả gánh nặng, duy trì lâu còn nặng hơn.

[pause] [chuckles] Kaku ví von: lãnh địa giống một chiêu tất tay trong bài. Tung đúng lúc thì thắng, tung sai lúc thì mình cạn sạch lực.

[pause] [curious] Nếu lãnh địa mạnh như vậy, làm sao sống sót? Trong truyện có vài cách, và mỗi cách đều có cái giá riêng.

[pause] Cách thứ nhất: dựng lãnh địa của mình. Khi hai lãnh địa va nhau, bên nào tinh xảo hơn sẽ lấn át bên kia. Đây gọi là tranh chấp lãnh địa.

[pause] Tranh chấp không đo ai nhiều chú lực hơn, mà đo lãnh địa nào được xây chặt chẽ hơn. Người tinh tế có thể thắng người mạnh hơn.

[pause] Cách thứ hai: giản dị lãnh địa. Đây là một vùng nhỏ bao quanh người dùng, không tấn công ai, chỉ để vô hiệu hóa hiệu ứng tất trúng khi chạm vào.

[pause] Giản dị lãnh địa được xem là kỹ thuật của kẻ yếu, vì nó giúp người không dựng được lãnh địa vẫn có cơ hội sống sót.

[pause] Cách thứ ba: các kỹ thuật bí truyền của những gia tộc lớn, dùng để phản đòn tất trúng ngay khi nó chạm vào người.

[pause] Cách thứ tư: khuếch đại lãnh địa. Người dùng bọc cơ thể trong một lớp lãnh địa mỏng, vô hiệu hóa thuật thức nào chạm vào mình.

[pause] Cái giá là: trong lúc khuếch đại, người dùng không thể dùng thuật thức của chính mình. Được phòng thủ thì mất tấn công.

[pause] Cách thứ năm, cách thô bạo nhất: phá kết giới từ bên ngoài. Kết giới lãnh địa thường được thiết kế để giữ người ở trong, nên từ ngoài phá vào dễ hơn.

[pause] Kaku tóm lại: đánh lại bằng lãnh địa, che mình bằng giản dị lãnh địa, phản đòn bằng bí truyền, bọc mình bằng khuếch đại, hoặc nhờ đồng đội phá từ ngoài.
```

### c03 · Cái giá: thuật thức bị cháy / Lãnh địa không hoàn chỉnh và lãnh địa mở

Khoảng 97 giây · cảnh s32–s41 · 1264 ký tự

**Gemini**

```text
Sau khi lãnh địa kết thúc, người dùng thường không thể dùng thuật thức trong một khoảng thời gian. Fan gọi hiện tượng này là thuật thức bị cháy.

<short pause> Đây là lý do lãnh địa không phải chiêu mở màn. Tung ra mà không kết liễu được đối thủ thì người dùng rơi vào thế cực kỳ nguy hiểm.

<short pause> Trong truyện có nhân vật dùng sức mạnh hồi phục để chữa lại phần não bị cháy, rút ngắn thời gian chờ. <short pause> Nhưng đó là kỹ năng cực hiếm.

<short pause> Vì thế các trận đấu lãnh địa luôn có nhịp: ai dựng trước, ai chịu được lâu hơn, ai còn sức khi cả hai lãnh địa sụp đổ.

<short pause> Không phải lãnh địa nào cũng hoàn hảo. Có những lãnh địa chưa hoàn chỉnh: dựng được không gian nhưng chưa có hiệu ứng tất trúng.

<short pause> Lãnh địa chưa hoàn chỉnh vẫn hữu ích, nhất là khi dùng để tranh chấp, nhưng nó không phải chiêu kết liễu.

<short pause> Ở chiều ngược lại là thứ gần như không tưởng: lãnh địa không có kết giới. Người dùng vẽ thế giới của mình thẳng lên thực tại mà không cần khung.

<short pause> Trong truyện, kỹ thuật này được ví như vẽ tranh lên không khí thay vì lên giấy. Chỉ kẻ ở đẳng cấp cao nhất mới làm được.

<short pause> Vì không có kết giới giam giữ, lãnh địa này có thể phủ cả một vùng rộng. Đổi lại, người dùng để lại cho đối thủ một đường thoát.

<short pause> Để lại đường thoát không phải vì tử tế. Đó là một giao ước: chấp nhận bất lợi nhỏ để đổi lấy sức mạnh lớn hơn nhiều.
```

**ElevenLabs**

```text
Sau khi lãnh địa kết thúc, người dùng thường không thể dùng thuật thức trong một khoảng thời gian. Fan gọi hiện tượng này là thuật thức bị cháy.

[pause] Đây là lý do lãnh địa không phải chiêu mở màn. Tung ra mà không kết liễu được đối thủ thì người dùng rơi vào thế cực kỳ nguy hiểm.

[pause] Trong truyện có nhân vật dùng sức mạnh hồi phục để chữa lại phần não bị cháy, rút ngắn thời gian chờ. [pause] Nhưng đó là kỹ năng cực hiếm.

[pause] Vì thế các trận đấu lãnh địa luôn có nhịp: ai dựng trước, ai chịu được lâu hơn, ai còn sức khi cả hai lãnh địa sụp đổ.

[pause] Không phải lãnh địa nào cũng hoàn hảo. Có những lãnh địa chưa hoàn chỉnh: dựng được không gian nhưng chưa có hiệu ứng tất trúng.

[pause] Lãnh địa chưa hoàn chỉnh vẫn hữu ích, nhất là khi dùng để tranh chấp, nhưng nó không phải chiêu kết liễu.

[pause] Ở chiều ngược lại là thứ gần như không tưởng: lãnh địa không có kết giới. Người dùng vẽ thế giới của mình thẳng lên thực tại mà không cần khung.

[pause] Trong truyện, kỹ thuật này được ví như vẽ tranh lên không khí thay vì lên giấy. Chỉ kẻ ở đẳng cấp cao nhất mới làm được.

[pause] Vì không có kết giới giam giữ, lãnh địa này có thể phủ cả một vùng rộng. Đổi lại, người dùng để lại cho đối thủ một đường thoát.

[pause] Để lại đường thoát không phải vì tử tế. Đó là một giao ước: chấp nhận bất lợi nhỏ để đổi lấy sức mạnh lớn hơn nhiều.
```

### c04 · Những lãnh địa trong Trò chơi tử thần

Khoảng 77 giây · cảnh s42–s49 · 1007 ký tự

**Gemini**

```text
Arc Trò chơi tử thần mang tới những lãnh địa rất lạ, cho thấy lãnh địa không nhất thiết là để giết ngay.

<short pause> Có một lãnh địa vận hành như một tòa án. Bên trong, không ai được dùng bạo lực. Mọi thứ được quyết định bằng một phiên xét xử.

<short pause> Nếu bị kết tội, bị cáo có thể bị tịch thu thuật thức. Với một chú thuật sư, mất thuật thức còn đáng sợ hơn bị thương.

<short pause> Lãnh địa tòa án cho thấy tất trúng không phải là tất sát. Hiệu ứng chắc chắn xảy ra là phiên tòa, còn kết quả phụ thuộc vào luật chơi.

<short pause> Một lãnh địa khác lại giống máy chơi may rủi. Người dùng quay số, và nếu trúng lớn, họ nhận được sức mạnh gần như bất tử trong vài phút.

<short pause> Nghe có vẻ tùy hứng, nhưng chính yếu tố may rủi là một phần luật. Đối thủ bị buộc phải chơi cùng, dù họ có muốn hay không.

<short pause> Những lãnh địa này chứng minh một điều: lãnh địa phản ánh con người. Người mê công lý dựng tòa án, người mê may rủi dựng sòng bạc.

<short pause> <laugh> Kaku nhắc: phần này dựa trên những gì anime và truyện đã kể tới arc Trò chơi tử thần. Chi tiết nào chưa rõ, mình sẽ nói rõ đó là suy đoán.
```

**ElevenLabs**

```text
Arc Trò chơi tử thần mang tới những lãnh địa rất lạ, cho thấy lãnh địa không nhất thiết là để giết ngay.

[pause] Có một lãnh địa vận hành như một tòa án. Bên trong, không ai được dùng bạo lực. Mọi thứ được quyết định bằng một phiên xét xử.

[pause] Nếu bị kết tội, bị cáo có thể bị tịch thu thuật thức. Với một chú thuật sư, mất thuật thức còn đáng sợ hơn bị thương.

[pause] Lãnh địa tòa án cho thấy tất trúng không phải là tất sát. Hiệu ứng chắc chắn xảy ra là phiên tòa, còn kết quả phụ thuộc vào luật chơi.

[pause] Một lãnh địa khác lại giống máy chơi may rủi. Người dùng quay số, và nếu trúng lớn, họ nhận được sức mạnh gần như bất tử trong vài phút.

[pause] Nghe có vẻ tùy hứng, nhưng chính yếu tố may rủi là một phần luật. Đối thủ bị buộc phải chơi cùng, dù họ có muốn hay không.

[pause] Những lãnh địa này chứng minh một điều: lãnh địa phản ánh con người. Người mê công lý dựng tòa án, người mê may rủi dựng sòng bạc.

[pause] [chuckles] Kaku nhắc: phần này dựa trên những gì anime và truyện đã kể tới arc Trò chơi tử thần. Chi tiết nào chưa rõ, mình sẽ nói rõ đó là suy đoán.
```

### c05 · Hai lãnh địa nổi tiếng nhất / Vì sao không phải ai cũng dựng được lãnh địa?

Khoảng 143 giây · cảnh s50–s63 · 1859 ký tự

**Gemini**

```text
Nói về lãnh địa thì không thể bỏ qua hai lãnh địa được nhắc nhiều nhất trong truyện. Chúng đại diện cho hai triết lý hoàn toàn khác nhau.

<short pause> Lãnh địa thứ nhất là Vô lượng không xứ. Bên trong là một không gian vô tận, và đối thủ bị ép tiếp nhận một lượng thông tin không bao giờ kết thúc.

<short pause> Kết quả là đối thủ đứng im. Không phải vì bị trói, mà vì não không xử lý kịp. Họ nhìn thấy mọi thứ, nên không làm được gì.

<short pause> Đó là kiểu lãnh địa vô hiệu hóa: không cần chém, chỉ cần làm đối thủ tê liệt, rồi người dùng muốn làm gì cũng được.

<short pause> Lãnh địa thứ hai là Phục ma ngự trù tử. Đây chính là lãnh địa không kết giới mà mình vừa nói. Bên trong là một ngôi đền và những nhát chém liên tục.

<short pause> Mọi thứ trong phạm vi đều bị chém không ngừng cho tới khi tan thành từng mảnh. Đây là kiểu lãnh địa hủy diệt thuần túy.

<short pause> Hai lãnh địa này cho thấy hai con đường: một bên khóa đối thủ bằng thông tin, một bên xóa sổ bằng sức hủy diệt. Cả hai đều cực kỳ khó vượt qua.

<short pause> <laugh> Kaku ghi chú: khi hai lãnh địa kiểu này đối đầu, câu hỏi không còn là ai mạnh hơn, mà là lãnh địa của ai được xây tinh xảo hơn và ai trụ được lâu hơn.

<short pause> Nếu lãnh địa mạnh như vậy, sao không phải chú thuật sư nào cũng học nó? Câu trả lời: vì nó đòi hỏi ba thứ cùng lúc, và thiếu một thứ là thất bại.

<short pause> Thứ nhất là lượng chú lực khổng lồ. Dựng cả một thế giới tốn hơn rất nhiều so với tung vài đòn thuật thức.

<short pause> Thứ hai là khả năng kiểm soát cực kỳ chính xác. Kết giới phải kín, thế giới bên trong phải ổn định, và thuật thức phải được nạp vào đúng cách.

<short pause> Thứ ba là hiểu rõ bản thân. Vì lãnh địa là thế giới nội tâm, người không hiểu mình sẽ không thể hình dung ra nó cho rõ ràng.

<short pause> Đó là lý do trong truyện, người dựng được lãnh địa hoàn chỉnh được xem là thuộc hàng mạnh nhất, dù họ là người hay chú linh.

<short pause> Và cũng vì thế, một nhân vật mới học được lãnh địa thường là bước ngoặt lớn của câu chuyện. Nó cho thấy họ đã bước sang một đẳng cấp khác.
```

**ElevenLabs**

```text
Nói về lãnh địa thì không thể bỏ qua hai lãnh địa được nhắc nhiều nhất trong truyện. Chúng đại diện cho hai triết lý hoàn toàn khác nhau.

[pause] Lãnh địa thứ nhất là Vô lượng không xứ. Bên trong là một không gian vô tận, và đối thủ bị ép tiếp nhận một lượng thông tin không bao giờ kết thúc.

[pause] Kết quả là đối thủ đứng im. Không phải vì bị trói, mà vì não không xử lý kịp. Họ nhìn thấy mọi thứ, nên không làm được gì.

[pause] Đó là kiểu lãnh địa vô hiệu hóa: không cần chém, chỉ cần làm đối thủ tê liệt, rồi người dùng muốn làm gì cũng được.

[pause] Lãnh địa thứ hai là Phục ma ngự trù tử. Đây chính là lãnh địa không kết giới mà mình vừa nói. Bên trong là một ngôi đền và những nhát chém liên tục.

[pause] Mọi thứ trong phạm vi đều bị chém không ngừng cho tới khi tan thành từng mảnh. Đây là kiểu lãnh địa hủy diệt thuần túy.

[pause] Hai lãnh địa này cho thấy hai con đường: một bên khóa đối thủ bằng thông tin, một bên xóa sổ bằng sức hủy diệt. Cả hai đều cực kỳ khó vượt qua.

[pause] [chuckles] Kaku ghi chú: khi hai lãnh địa kiểu này đối đầu, câu hỏi không còn là ai mạnh hơn, mà là lãnh địa của ai được xây tinh xảo hơn và ai trụ được lâu hơn.

[pause] [curious] Nếu lãnh địa mạnh như vậy, sao không phải chú thuật sư nào cũng học nó? Câu trả lời: vì nó đòi hỏi ba thứ cùng lúc, và thiếu một thứ là thất bại.

[pause] Thứ nhất là lượng chú lực khổng lồ. Dựng cả một thế giới tốn hơn rất nhiều so với tung vài đòn thuật thức.

[pause] Thứ hai là khả năng kiểm soát cực kỳ chính xác. Kết giới phải kín, thế giới bên trong phải ổn định, và thuật thức phải được nạp vào đúng cách.

[pause] Thứ ba là hiểu rõ bản thân. Vì lãnh địa là thế giới nội tâm, người không hiểu mình sẽ không thể hình dung ra nó cho rõ ràng.

[pause] Đó là lý do trong truyện, người dựng được lãnh địa hoàn chỉnh được xem là thuộc hàng mạnh nhất, dù họ là người hay chú linh.

[pause] Và cũng vì thế, một nhân vật mới học được lãnh địa thường là bước ngoặt lớn của câu chuyện. Nó cho thấy họ đã bước sang một đẳng cấp khác.
```

### c06 · Một trận tranh chấp lãnh địa diễn ra thế nào / Lịch sử: kỹ thuật chống lãnh địa cổ xưa

Khoảng 101 giây · cảnh s64–s74 · 1307 ký tự

**Gemini**

```text
Để dễ hình dung, hãy tua chậm một trận tranh chấp lãnh địa theo từng giây, dựa trên cách truyện thường miêu tả.

<short pause> Giây đầu tiên: cả hai kết thủ ấn gần như cùng lúc. Hai kết giới bắt đầu mọc lên và chồng lên nhau trong cùng một không gian.

<short pause> Những giây tiếp theo: hai thế giới nội tâm giành nhau từng mét. Chỗ nào lãnh địa tinh xảo hơn thì bắt đầu lấn chiếm.

<short pause> Nếu một bên bị lấn hoàn toàn, lãnh địa của họ vỡ. Hiệu ứng tất trúng của bên thắng lập tức có hiệu lực.

<short pause> Nếu không ai lấn được ai, cả hai cùng hao chú lực rất nhanh. Người cạn trước sẽ phải bỏ lãnh địa và chịu thuật thức bị cháy.

<short pause> Vì vậy ngay cả khi thua tranh chấp, người thông minh vẫn có thể cố tình kéo dài để đối thủ cũng cạn sức theo mình.

<short pause> Lãnh địa không phải phát minh mới. Trong truyện, các chú thuật sư từ thời xa xưa đã biết tới nó, và cũng đã nghĩ ra cách chống lại nó.

<short pause> Có một kỹ thuật cổ gọi là Không bát, tạo ra một chiếc giỏ đan quanh người dùng, giúp trung hòa hiệu ứng tất trúng.

<short pause> Giản dị lãnh địa ngày nay được xem như phiên bản dễ học hơn của những kỹ thuật cổ này, để nhiều chú thuật sư có thể tự bảo vệ mình.

<short pause> Điểm chung của các kỹ thuật phòng thủ: chúng không đánh bại lãnh địa. Chúng chỉ giúp bạn sống đủ lâu để lãnh địa tự sụp, hoặc để đồng đội phá nó.

<short pause> Đây là chi tiết rất đời: trong chiến đấu thật, sống sót đôi khi quan trọng hơn chiến thắng.
```

**ElevenLabs**

```text
Để dễ hình dung, hãy tua chậm một trận tranh chấp lãnh địa theo từng giây, dựa trên cách truyện thường miêu tả.

[pause] Giây đầu tiên: cả hai kết thủ ấn gần như cùng lúc. Hai kết giới bắt đầu mọc lên và chồng lên nhau trong cùng một không gian.

[pause] Những giây tiếp theo: hai thế giới nội tâm giành nhau từng mét. Chỗ nào lãnh địa tinh xảo hơn thì bắt đầu lấn chiếm.

[pause] Nếu một bên bị lấn hoàn toàn, lãnh địa của họ vỡ. Hiệu ứng tất trúng của bên thắng lập tức có hiệu lực.

[pause] Nếu không ai lấn được ai, cả hai cùng hao chú lực rất nhanh. Người cạn trước sẽ phải bỏ lãnh địa và chịu thuật thức bị cháy.

[pause] Vì vậy ngay cả khi thua tranh chấp, người thông minh vẫn có thể cố tình kéo dài để đối thủ cũng cạn sức theo mình.

[pause] Lãnh địa không phải phát minh mới. Trong truyện, các chú thuật sư từ thời xa xưa đã biết tới nó, và cũng đã nghĩ ra cách chống lại nó.

[pause] Có một kỹ thuật cổ gọi là Không bát, tạo ra một chiếc giỏ đan quanh người dùng, giúp trung hòa hiệu ứng tất trúng.

[pause] Giản dị lãnh địa ngày nay được xem như phiên bản dễ học hơn của những kỹ thuật cổ này, để nhiều chú thuật sư có thể tự bảo vệ mình.

[pause] Điểm chung của các kỹ thuật phòng thủ: chúng không đánh bại lãnh địa. Chúng chỉ giúp bạn sống đủ lâu để lãnh địa tự sụp, hoặc để đồng đội phá nó.

[pause] Đây là chi tiết rất đời: trong chiến đấu thật, sống sót đôi khi quan trọng hơn chiến thắng.
```

### c07 · Thử nghiệm: nếu bạn bị kéo vào lãnh địa / Góc nhìn của Kaku: vì sao lãnh địa hay

Khoảng 126 giây · cảnh s75–s87 · 1638 ký tự

**Gemini**

```text
Giờ thử đặt mình vào vị trí một chú thuật sư bình thường. Bạn bị kéo vào lãnh địa của một đối thủ mạnh hơn. Bạn sẽ làm gì?

<short pause> Bước một: đừng hoảng. Xác định đây là lãnh địa hoàn chỉnh hay chưa. Nếu chưa có tất trúng, bạn vẫn còn đánh được như bình thường.

<short pause> Bước hai: nếu bạn biết giản dị lãnh địa, dựng nó ngay. Mục tiêu không phải thắng, mà là không để đòn tất trúng chạm vào mình.

<short pause> Bước ba: tính thời gian. Lãnh địa rất tốn sức, đối thủ không duy trì mãi được. Sau khi nó sụp, thuật thức của họ còn bị cháy.

<short pause> Bước bốn: tận dụng khoảnh khắc đó. Đối thủ vừa mất thuật thức tạm thời, đây là cơ hội duy nhất để phản công.

<short pause> Nghe đơn giản, nhưng trong truyện, rất ít người làm được đủ cả bốn bước. Phần lớn đã thua ở bước một vì không kịp phản ứng.

<short pause> Giờ tới phần mình thích nhất: vì sao lãnh địa là một ý tưởng hay trong thiết kế hệ thống sức mạnh?

<short pause> Lý do thứ nhất: nó tạo ra kịch tính có luật. Người xem biết khi lãnh địa mở, có người sắp gặp nguy. Căng thẳng đến từ luật chứ không từ may mắn.

<short pause> Lý do thứ hai: có phản đòn rõ ràng. Mạnh cỡ nào cũng có cách chống. Nhờ vậy nhân vật yếu hơn vẫn có đường sống nếu đủ thông minh.

<short pause> Lý do thứ ba: có cái giá. Thuật thức bị cháy sau khi dùng khiến mỗi lần mở lãnh địa là một quyết định lớn, không phải chiêu spam.

<short pause> Lý do thứ tư: lãnh địa kể chuyện về nhân vật. Nhìn lãnh địa của ai đó, bạn hiểu họ nghĩ gì về thế giới.

<short pause> Nhưng cũng có điểm yếu: khi quá nhiều nhân vật có lãnh địa, cảm giác đặc biệt có thể giảm đi. Đây là thách thức của mọi hệ thống sức mạnh khi truyện kéo dài.

<short pause> Nếu so với Nen mà mình đã giải thích ở video trước, lãnh địa giống một dạng giao ước cực lớn: đổi thật nhiều chú lực lấy một không gian tất trúng.
```

**ElevenLabs**

```text
Giờ thử đặt mình vào vị trí một chú thuật sư bình thường. Bạn bị kéo vào lãnh địa của một đối thủ mạnh hơn. [curious] Bạn sẽ làm gì?

[pause] Bước một: đừng hoảng. Xác định đây là lãnh địa hoàn chỉnh hay chưa. Nếu chưa có tất trúng, bạn vẫn còn đánh được như bình thường.

[pause] Bước hai: nếu bạn biết giản dị lãnh địa, dựng nó ngay. Mục tiêu không phải thắng, mà là không để đòn tất trúng chạm vào mình.

[pause] Bước ba: tính thời gian. Lãnh địa rất tốn sức, đối thủ không duy trì mãi được. Sau khi nó sụp, thuật thức của họ còn bị cháy.

[pause] Bước bốn: tận dụng khoảnh khắc đó. Đối thủ vừa mất thuật thức tạm thời, đây là cơ hội duy nhất để phản công.

[pause] Nghe đơn giản, nhưng trong truyện, rất ít người làm được đủ cả bốn bước. Phần lớn đã thua ở bước một vì không kịp phản ứng.

[pause] Giờ tới phần mình thích nhất: vì sao lãnh địa là một ý tưởng hay trong thiết kế hệ thống sức mạnh?

[pause] Lý do thứ nhất: nó tạo ra kịch tính có luật. Người xem biết khi lãnh địa mở, có người sắp gặp nguy. Căng thẳng đến từ luật chứ không từ may mắn.

[pause] Lý do thứ hai: có phản đòn rõ ràng. Mạnh cỡ nào cũng có cách chống. Nhờ vậy nhân vật yếu hơn vẫn có đường sống nếu đủ thông minh.

[pause] Lý do thứ ba: có cái giá. Thuật thức bị cháy sau khi dùng khiến mỗi lần mở lãnh địa là một quyết định lớn, không phải chiêu spam.

[pause] Lý do thứ tư: lãnh địa kể chuyện về nhân vật. Nhìn lãnh địa của ai đó, bạn hiểu họ nghĩ gì về thế giới.

[pause] Nhưng cũng có điểm yếu: khi quá nhiều nhân vật có lãnh địa, cảm giác đặc biệt có thể giảm đi. Đây là thách thức của mọi hệ thống sức mạnh khi truyện kéo dài.

[pause] Nếu so với Nen mà mình đã giải thích ở video trước, lãnh địa giống một dạng giao ước cực lớn: đổi thật nhiều chú lực lấy một không gian tất trúng.
```

### c08 · Tóm tắt

Khoảng 49 giây · cảnh s88–s93 · 635 ký tự

**Gemini**

```text
Tóm lại: chú lực là nhiên liệu, thuật thức là cỗ máy, và lãnh địa là biến cả thế giới xung quanh thành cỗ máy của mình.

<short pause> Bên trong lãnh địa, thuật thức tất trúng. Để sống sót, bạn cần lãnh địa của riêng mình, giản dị lãnh địa, bí truyền, khuếch đại, hoặc phá từ ngoài.

<short pause> Và mọi lãnh địa đều có giá: tốn chú lực, thuật thức bị cháy, hoặc phải chừa đường thoát cho đối thủ.

<short pause> Câu hỏi cho bạn: nếu có lãnh địa riêng, thế giới nội tâm của bạn sẽ trông như thế nào? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã ma thuật trong Frieren, nơi phép thuật có cả lịch sử của nó.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: chú lực là nhiên liệu, thuật thức là cỗ máy, và lãnh địa là biến cả thế giới xung quanh thành cỗ máy của mình.

[pause] Bên trong lãnh địa, thuật thức tất trúng. Để sống sót, bạn cần lãnh địa của riêng mình, giản dị lãnh địa, bí truyền, khuếch đại, hoặc phá từ ngoài.

[pause] Và mọi lãnh địa đều có giá: tốn chú lực, thuật thức bị cháy, hoặc phải chừa đường thoát cho đối thủ.

[pause] [curious] Câu hỏi cho bạn: nếu có lãnh địa riêng, thế giới nội tâm của bạn sẽ trông như thế nào? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã ma thuật trong Frieren, nơi phép thuật có cả lịch sử của nó.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
