# Bộ prompt · Naruto: 10 hiểu lầm mà fan lâu năm vẫn tin

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 92 ảnh, 8 đoạn đọc, khoảng 15.3 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (92 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler toàn bộ Naruto và Naruto Shippuden, bao gồm cả cuộc Đại chiến ninja lần thứ tư và…

```text
Wide 16:9 landscape cinematic frame. a ninja village carved into a mountain at sunset, stone faces overlooking rooftops. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Naruto kết thúc đã hơn mười năm, nhưng có những điều sai về nó vẫn được lặp lại mỗi ngày, trong bình luận, tr…

```text
Wide 16:9 landscape cinematic frame. a scroll of comments unrolling endlessly, several lines highlighted in red. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hôm nay Kaku mang theo hai con dấu. Một con dấu ghi SAI. Một con dấu ghi NỬA ĐÚNG. Mỗi hiểu lầm sẽ nhận một p…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up two rubber stamps, one red and one yellow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Luật chơi: trước khi Kaku đóng dấu, bạn hãy tự đoán trong đầu. Cuối video, đếm xe…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a blank scorecard with ten boxes. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Mười hiểu lầm chia làm ba nhóm: về sức mạnh, về thế giới ninja, và về chính nhân vật chính. Hiểu lầm lớn nhất…

```text
Wide 16:9 landscape cinematic frame. three folders labeled with icons: a swirl, a village, and a cloth headband. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Nhóm 1 · Hiểu lầm 1: Sharingan sao chép được mọi thứ

Lời: Nhóm đầu tiên là về sức mạnh. Hiểu lầm một: Sharingan có thể sao chép bất kỳ kỹ thuật nào nó nhìn thấy.

```text
Wide 16:9 landscape cinematic frame. a single glowing red eye reflecting a blur of hand signs. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Phán quyết: nửa đúng.

```text
Wide 16:9 landscape cinematic frame. a yellow stamp slamming down on a paper with the words HALF TRUE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Sharingan đúng là có thể nhìn và ghi nhớ rất nhiều nhẫn thuật, ảo thuật và thể thuật, rồi bắt chước lại. Có n…

```text
Wide 16:9 landscape cinematic frame. a ninja silhouette surrounded by floating scrolls, each representing a copied technique. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Nhưng nó không sao chép được huyết kế giới hạn, những năng lực di truyền theo dòng máu. Nhìn một người dùng m…

```text
Wide 16:9 landscape cinematic frame. a red eye staring at a tree growing from someone's hands, a barrier blocking the copy. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và sao chép rồi cũng phải có đủ chakra và thể chất để thực hiện. Nhìn thấy không có nghĩa là làm được.

```text
Wide 16:9 landscape cinematic frame. a tired ninja trying to perform a massive technique and collapsing halfway. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì những người dùng Sharingan trong truyện thường rất giỏi, khiến ta nghĩ đôi mắt làm được tấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small red eye diagram pinned to its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Giải thích nhanh: huyết kế giới hạn

Lời: Trước khi đi tiếp, cần hiểu huyết kế giới hạn là gì, vì nó xuất hiện trong nhiều hiểu lầm hôm nay.

```text
Wide 16:9 landscape cinematic frame. a family tree with glowing branches, each branch holding a different elemental symbol. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Huyết kế giới hạn là những năng lực được truyền theo dòng máu, người ngoài gia tộc không thể học. Có hai kiểu…

```text
Wide 16:9 landscape cinematic frame. a glowing bloodline passing from parent to child silhouettes like a river of light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Kiểu thứ nhất là kết hợp hai tính chất chakra cùng lúc để tạo ra một tính chất mới. Ví dụ mộc độn là thổ cộng…

```text
Wide 16:9 landscape cinematic frame. two elemental symbols merging into a new one: earth and water becoming a tree, wind and water becoming ice. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Kiểu thứ hai là những đôi mắt đặc biệt, gọi là đồng thuật, như đôi mắt nhìn xuyên vật thể hay đôi mắt đỏ sao…

```text
Wide 16:9 landscape cinematic frame. a row of stylized glowing eyes of different colors on a display shelf. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hiểu điều này rồi, bạn sẽ thấy vì sao có những thứ mà ngay cả thiên tài cũng không thể bắt chước.

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to combine two small elemental orbs and getting only a puff of steam. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Nhóm 1 · Hiểu lầm 2: Rasengan cần nguyên tố

Lời: Hiểu lầm hai: Rasengan là một kỹ thuật hệ gió, hay ít nhất phải có một nguyên tố nào đó mới dùng được.

```text
Wide 16:9 landscape cinematic frame. a spinning sphere of energy in a palm, wind lines swirling around it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Rasengan là kỹ thuật chỉ dùng biến đổi hình dạng của chakra: xoay chakra thật nhanh theo nhiều hướng, rồi nén…

```text
Wide 16:9 landscape cinematic frame. a diagram of chakra spinning in several directions and compressing into a sphere. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Người tạo ra nó, Hokage đệ tứ, thực ra muốn thêm nguyên tố vào, nhưng chưa làm được. Đó mới là bước cuối cùng…

```text
Wide 16:9 landscape cinematic frame. an unfinished blueprint of a sphere with a blank space labeled with a question mark. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Naruto là người làm được điều đó khi thêm tính chất gió vào, tạo ra Phong độn Rasen Shuriken, mạnh tới mức gâ…

```text
Wide 16:9 landscape cinematic frame. a spinning sphere surrounded by a ring of wind blades like a shuriken, a pained arm holding it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Để học Rasengan, Naruto phải đi qua ba bước luyện tập: làm vỡ quả bóng nước bằng cách xoay chakra, làm nổ quả…

```text
Wide 16:9 landscape cinematic frame. three training props on a table: a water balloon, a rubber ball and a thin balloon, each with a small number. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Vì sao dễ nhầm: vì phiên bản nổi tiếng nhất ở Shippuden là phiên bản gió, và nó xuất hiện nhiều tới mức người…

```text
Wide 16:9 landscape cinematic frame. a plain glowing sphere and a wind-wrapped one side by side, labeled before and after. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Nhóm 1 · Hiểu lầm 3: Chakra chỉ để dùng nhẫn thuật

Lời: Hiểu lầm ba: chakra chỉ dùng để phun lửa, tạo nước, gọi thú. Ai không giỏi nhẫn thuật thì chakra cũng vô dụng.

```text
Wide 16:9 landscape cinematic frame. a ninja breathing fire, another summoning a creature, both glowing with energy. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Chakra là sự kết hợp giữa năng lượng thể chất và năng lượng tinh thần. Nó có mặt trong gần như mọi hoạt động…

```text
Wide 16:9 landscape cinematic frame. a ninja walking calmly on a lake surface, ripples forming under each step. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Có một nhân vật không dùng được nhẫn thuật lẫn ảo thuật, nhưng trở thành một trong những bậc thầy thể thuật m…

```text
Wide 16:9 landscape cinematic frame. a young fighter in simple training clothes mid-kick, a faint aura bursting from his body. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Những cửa đó giới hạn dòng chakra để bảo vệ cơ thể. Mở càng nhiều cửa, sức mạnh càng lớn, và cái giá cho cơ t…

```text
Wide 16:9 landscape cinematic frame. a diagram of eight glowing gates along a body, the last ones flickering red. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì phần lớn trận đánh nổi bật trong truyện đều có nhẫn thuật rực rỡ. Nhưng chakra là nền tảng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to walk on water, one foot sinking, a sweat drop on its face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Nhóm 1 · Hiểu lầm 4: Chế độ hiền nhân ai cũng học được

Lời: Hiểu lầm bốn: chế độ hiền nhân chỉ là một kỹ thuật nâng cấp, ai chăm chỉ cũng học được.

```text
Wide 16:9 landscape cinematic frame. a ninja meditating on a rock, green nature energy swirling around him. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Chế độ hiền nhân đòi hỏi hấp thụ năng lượng tự nhiên và cân bằng nó hoàn hảo với chakra của bản thân. Thiếu m…

```text
Wide 16:9 landscape cinematic frame. a balance scale with nature energy on one side and a person's chakra on the other, perfectly level. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Thừa một chút thì còn đáng sợ hơn: người đó sẽ biến thành đá. Truyện cho thấy những bức tượng cóc bằng đá ở v…

```text
Wide 16:9 landscape cinematic frame. a mountain garden filled with stone toad statues, mist drifting between them. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nó cũng cần một lượng chakra khổng lồ và sức bền phi thường. Naruto học được một phần nhờ lượng chakra lớn bấ…

```text
Wide 16:9 landscape cinematic frame. several identical ninja clones sitting still around a lake, gathering energy while the original fights. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Vì sao dễ nhầm: vì Naruto học nó khá nhanh trong một arc ngắn. Nhưng chính truyện nhấn mạnh rằng rất ít người…

```text
Wide 16:9 landscape cinematic frame. a nearly empty hall of fame with only a few portraits on the wall. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Nhóm 2 · Hiểu lầm 5: Vĩ thú là quái vật vô tri

Lời: Nhóm thứ hai là về thế giới ninja. Hiểu lầm năm: vĩ thú chỉ là những quái vật khổng lồ, một nguồn năng lượng…

```text
Wide 16:9 landscape cinematic frame. a colossal nine-tailed silhouette towering over a village at night, red glow in the sky. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Chín vĩ thú được tạo ra khi Lục đạo tiên nhân chia chakra của Thập vĩ thành chín phần. Mỗi con có tên riêng,…

```text
Wide 16:9 landscape cinematic frame. an elderly sage figure surrounded by nine small glowing beasts gathered around him like children. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Suốt nhiều thế hệ, con người chỉ coi chúng là vũ khí. Chính vì bị đối xử như công cụ mà nhiều vĩ thú căm ghét…

```text
Wide 16:9 landscape cinematic frame. a massive creature bound by chains and seals, glaring down at tiny figures. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Một trong những đoạn đẹp nhất truyện là khi Naruto dần hiểu và làm bạn với vĩ thú trong mình, thay vì chỉ cố…

```text
Wide 16:9 landscape cinematic frame. a boy and a giant fox silhouette touching fist to fist inside a vast dark space. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Những người mang vĩ thú trong người, gọi là nhân trụ lực, thường bị dân làng xa lánh và sợ hãi. Cả Naruto lẫn…

```text
Wide 16:9 landscape cinematic frame. a lonely child sitting on a swing in an empty playground while other children walk away. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì phần đầu truyện chỉ thể hiện vĩ thú qua sự phá hủy. Tính cách của chúng chỉ được hé lộ dần…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shaking a giant fox's paw nervously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Nhóm 2 · Hiểu lầm 6: Hokage luôn là người mạnh nhất làng

Lời: Hiểu lầm sáu: Hokage luôn là ninja mạnh nhất làng Lá.

```text
Wide 16:9 landscape cinematic frame. five stone faces carved into a mountain above a village. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Phán quyết: nửa đúng.

```text
Wide 16:9 landscape cinematic frame. a yellow stamp slamming down with the words HALF TRUE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Đúng là nhiều Hokage cực kỳ mạnh, và sức mạnh là một phần quan trọng để được chọn. Nhưng Hokage còn cần sự tí…

```text
Wide 16:9 landscape cinematic frame. a leader addressing a crowd from a rooftop, the villagers listening. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Có những ninja cực mạnh từng được mời làm Hokage nhưng từ chối, như một hiền nhân cóc thích tự do đi khắp nơi…

```text
Wide 16:9 landscape cinematic frame. a tall traveler with a walking staff waving goodbye at the village gate. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Và cũng có Hokage được chọn chủ yếu vì hoàn cảnh và sự tin tưởng của mọi người, không phải vì là người mạnh n…

```text
Wide 16:9 landscape cinematic frame. a ninja reluctantly accepting a leader's wide hat, friends cheering behind him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Hokage đầu tiên còn là người sáng lập làng, và nhiều Hokage về sau hy sinh tính mạng để bảo vệ làng. Với ngườ…

```text
Wide 16:9 landscape cinematic frame. a row of memorial stones with fresh flowers placed before them at dawn. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Vì sao dễ nhầm: vì Naruto luôn nói muốn làm Hokage để được mọi người công nhận. Khán giả gắn Hokage với sức m…

```text
Wide 16:9 landscape cinematic frame. a boy shouting on top of a stone face on the mountain, sunset behind him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Nhóm 2 · Hiểu lầm 7: Itachi diệt tộc vì hắn là kẻ ác

Lời: Hiểu lầm bảy: người anh trai diệt cả gia tộc Uchiha trong một đêm vì hắn là một kẻ tàn độc, muốn thử sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing in a moonlit street of an empty clan district, red eyes glowing. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Sự thật được hé lộ trong Shippuden: gia tộc đang lên kế hoạch đảo chính làng. Các lãnh đạo cấp cao của làng g…

```text
Wide 16:9 landscape cinematic frame. a secret meeting in a dark room, elders issuing an order to a young ninja kneeling before them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Anh chấp nhận làm kẻ phản bội trong mắt mọi người, và tha cho em trai, để em lớn lên với lòng căm thù dành ch…

```text
Wide 16:9 landscape cinematic frame. an older brother walking away from a crying younger brother, his own tears hidden. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Anh gia nhập một tổ chức tội phạm, nhưng thật ra vẫn âm thầm bảo vệ làng từ bên trong.

```text
Wide 16:9 landscape cinematic frame. a cloaked figure standing on a cliff overlooking a village, protective and distant. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì suốt phần đầu, truyện kể hoàn toàn qua ánh mắt của người em trai. Sự thật chỉ được kể lại…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a flipped photograph that shows a different image on the back. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Nhóm 2 · Hiểu lầm 8: Madara là trùm cuối

Lời: Hiểu lầm tám: kẻ thù cuối cùng của cuộc Đại chiến ninja lần thứ tư là Madara Uchiha.

```text
Wide 16:9 landscape cinematic frame. a legendary warrior silhouette standing on a battlefield of craters, a crimson moon above. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Phán quyết: sai.

```text
Wide 16:9 landscape cinematic frame. a red stamp slamming down with the word FALSE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Madara đúng là kẻ đứng sau kế hoạch Nguyệt Nhãn và là đối thủ khủng khiếp nhất của cuộc chiến. Nhưng chính hắ…

```text
Wide 16:9 landscape cinematic frame. a puppet string attached to a powerful warrior's shoulder, leading up into darkness. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Một thực thể đen sống ký sinh đã âm thầm thao túng lịch sử suốt nhiều thế kỷ, để hồi sinh người mẹ của mình:…

```text
Wide 16:9 landscape cinematic frame. a dark shadow figure whispering to generations of warriors across a timeline. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Người phụ nữ đó mới là đối thủ cuối cùng mà Naruto và Sasuke phải đối mặt trong cuộc chiến.

```text
Wide 16:9 landscape cinematic frame. a pale ethereal goddess figure glowing above a shattered landscape. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Chi tiết này được cài cắm từ khá sớm: những bức phù điêu cổ trong đền thờ của gia tộc có ghi lại lịch sử, như…

```text
Wide 16:9 landscape cinematic frame. an ancient stone tablet in a dim shrine, parts of its inscription subtly altered with dark ink. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Vì sao dễ nhầm: vì Madara được xây dựng như một huyền thoại suốt nhiều năm, còn đối thủ thật sự xuất hiện rất…

```text
Wide 16:9 landscape cinematic frame. two groups of fans arguing, one holding a warrior poster, the other a goddess poster. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Nhóm 3 · Hiểu lầm 9: Naruto là học sinh vô dụng

Lời: Nhóm cuối cùng là về chính nhân vật chính. Hiểu lầm chín: Naruto khởi đầu là một học sinh vô dụng, không có c…

```text
Wide 16:9 landscape cinematic frame. a boy in a plain jacket at the back of a classroom, a failing test paper on his desk. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Phán quyết: nửa đúng.

```text
Wide 16:9 landscape cinematic frame. a yellow stamp slamming down with the words HALF TRUE. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Naruto đúng là đứng bét lớp ở học viện, trượt nhiều bài kiểm tra, và không làm nổi kỹ thuật phân thân cơ bản…

```text
Wide 16:9 landscape cinematic frame. a boy trying to make a clone that appears limp and pale, classmates laughing. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nhưng cậu có lượng chakra và sức bền vượt xa người thường. Và chỉ trong một đêm, cậu học được một kỹ thuật cấ…

```text
Wide 16:9 landscape cinematic frame. a boy in a forest at night surrounded by dozens of identical copies of himself, a large scroll open. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Về sau, chính kỹ thuật đó trở thành bí quyết luyện tập của cậu: mỗi phân thân học được gì, bản gốc cũng nhận…

```text
Wide 16:9 landscape cinematic frame. hundreds of clones training at once by a waterfall, the original absorbing glowing light from them. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Chiến thuật thích dùng số đông phân thân cũng thể hiện tính cách của cậu: không có tài năng tinh tế, cậu bù b…

```text
Wide 16:9 landscape cinematic frame. a boy using clones as decoys and springboards in a forest battle, an opponent confused. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Vì sao dễ nhầm: vì truyện cố tình giới thiệu Naruto như một kẻ bị ruồng bỏ. Tài năng của cậu không nằm ở nơi…

```text
Wide 16:9 landscape cinematic frame. a school report card with low grades, and a hidden note in the margin showing a huge energy meter. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Nhóm 3 · Hiểu lầm 10: Naruto thành công nhờ định mệnh

Lời: Và đây là hiểu lầm lớn nhất. Hiểu lầm mười: Naruto thành công vì cậu là người được định mệnh chọn, với dòng m…

```text
Wide 16:9 landscape cinematic frame. a boy standing in a beam of light from the sky, surrounded by symbols of destiny. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Phán quyết: nửa đúng. Và nửa sai của nó chính là thông điệp của cả bộ truyện.

```text
Wide 16:9 landscape cinematic frame. a yellow stamp slamming down, the stamp slightly cracked in the middle. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nửa đúng: cuối truyện tiết lộ Naruto là chuyển thế của một trong hai người con của Lục đạo tiên nhân. Cậu man…

```text
Wide 16:9 landscape cinematic frame. two brothers standing before an elderly sage, one with a sharp gaze and one with a warm smile. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nhưng hãy nhìn lý do người cha chọn người con thứ hai làm người kế thừa. Người anh là thiên tài, dựa vào sức…

```text
Wide 16:9 landscape cinematic frame. the warm-smiling brother surrounded by many friends working together, the other brother alone on a cliff. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nghĩa là ngay cả định mệnh của Naruto cũng là định mệnh của người nỗ lực. Dòng máu cho cậu cơ hội, nhưng khôn…

```text
Wide 16:9 landscape cinematic frame. a boy practicing alone at night under the moon, bruised but smiling. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và hãy nhớ, người anh trong câu chuyện cổ ấy, dù là thiên tài, cũng không sai hoàn toàn. Truyện cho thấy cả h…

```text
Wide 16:9 landscape cinematic frame. two brothers facing each other across a valley, then reaching out their hands toward each other. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Vì sao dễ nhầm: vì những tiết lộ về dòng máu đến rất muộn và rất ồn ào. Chúng làm lu mờ bảy trăm chương về mộ…

```text
Wide 16:9 landscape cinematic frame. a stack of hundreds of chapters with a tiny spotlight only on the last few pages. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Ba hiểu lầm nhanh · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước góc nhìn cuối, Kaku tặng thêm ba hiểu lầm nhỏ, xử lý thật nhanh.

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping three small cards like a card dealer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Một: người thầy đeo mặt nạ lúc nào cũng cầm một cuốn sách là vì lười. Thật ra đó là bộ tiểu thuyết do chính v…

```text
Wide 16:9 landscape cinematic frame. a relaxed ninja leaning on a tree reading a small novel, a sweat drop from a nearby student. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Hai: ninja phải dùng hai tay kết ấn mới dùng được nhẫn thuật. Có mười hai thủ ấn cơ bản, mang tên mười hai co…

```text
Wide 16:9 landscape cinematic frame. a chart of twelve hand seals with small zodiac animal icons, one hand forming a seal alone. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Ba: đôi mắt nhìn xuyên vật thể thấy được ba trăm sáu mươi độ, không có góc chết. Truyện cho thấy nó có một đi…

```text
Wide 16:9 landscape cinematic frame. a circular vision diagram around a head with a tiny dark wedge behind the neck. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn biết cả ba điều này từ trước, Kaku chính thức công nhận bạn là fan Naruto hạng thượng nhẫn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot presenting a small certificate with a leaf-shaped seal. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Góc nhìn của Kaku: nỗ lực hay định mệnh? · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại mười hiểu lầm, Kaku thấy phần lớn chúng xoay quanh một câu hỏi mà Naruto đặt ra từ rất sớm: sức mạnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting between two paths: one lit by a star, one lit by a lantern. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Truyện có những thiên tài như người anh trai tộc Uchiha, và những người chăm chỉ như cậu bé chỉ dùng thể thuậ…

```text
Wide 16:9 landscape cinematic frame. a split image: a gifted ninja effortlessly performing a technique, and a sweaty one training until dawn. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Có một câu nói nổi tiếng trong truyện, từ một thiên tài với đôi mắt trắng: số phận của mỗi người đã được định…

```text
Wide 16:9 landscape cinematic frame. a stern young ninja facing a determined boy in an arena. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Kaku nghĩ câu trả lời của Naruto không phải là định mệnh không tồn tại. Mà là: dù được sinh ra với điều gì, t…

```text
Wide 16:9 landscape cinematic frame. a boy picking up a fallen headband from the ground and tying it on firmly. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và đó là lý do nhiều người lớn lên cùng Naruto vẫn nhớ về cậu. Không phải vì cậu được chọn, mà vì cậu chưa ba…

```text
Wide 16:9 landscape cinematic frame. a grown-up silhouette looking at an old cloth headband on a shelf, smiling. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · Bảng phán quyết

Lời: Tổng kết bảng phán quyết. Nhóm sức mạnh: Sharingan sao chép mọi thứ, nửa đúng. Rasengan cần nguyên tố, sai. C…

```text
Wide 16:9 landscape cinematic frame. a verdict board with four rows stamped red and yellow. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Nhóm thế giới: vĩ thú vô tri, sai. Hokage luôn mạnh nhất, nửa đúng. Người anh diệt tộc vì tàn ác, sai. Madara…

```text
Wide 16:9 landscape cinematic frame. a verdict board with four more rows stamped. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Nhóm nhân vật chính: Naruto là học sinh vô dụng, nửa đúng. Naruto thành công nhờ định mệnh, nửa đúng.

```text
Wide 16:9 landscape cinematic frame. the final two rows stamped yellow, the last stamp glowing. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ đếm điểm: bạn đoán đúng bao nhiêu phán quyết? Từ tám câu trở lên là bạn đã sẵn sàng thi lên trung nhẫn. V…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a scorecard and a small ninja headband as a prize. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · Kết

Lời: Video tới, Kaku mời bạn bước vào một căn phòng mà một ngày bên ngoài bằng một năm bên trong: Phòng Thời Gian…

```text
Wide 16:9 landscape cinematic frame. a vast white void with a small building and an hourglass floating above it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất hai con dấu đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot putting two stamps into a drawer and waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nhóm 1 · Hiểu lầm 1: Sharingan sao chép được mọi thứ

Khoảng 110 giây · cảnh s01–s11 · 1429 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler toàn bộ Naruto và Naruto Shippuden, bao gồm cả cuộc Đại chiến ninja lần thứ tư và trận đấu cuối cùng.

<short pause> Naruto kết thúc đã hơn mười năm, nhưng có những điều sai về nó vẫn được lặp lại mỗi ngày, trong bình luận, trong video, thậm chí trong những cuộc tranh luận của fan lâu năm.

<short pause> <laugh> Hôm nay Kaku mang theo hai con dấu. Một con dấu ghi SAI. Một con dấu ghi NỬA ĐÚNG. Mỗi hiểu lầm sẽ nhận một phán quyết.

<short pause> Mở sổ ra nào! Mình là Kaku. Luật chơi: trước khi Kaku đóng dấu, bạn hãy tự đoán trong đầu. Cuối video, đếm xem bạn đoán đúng bao nhiêu câu.

<short pause> Mười hiểu lầm chia làm ba nhóm: về sức mạnh, về thế giới ninja, và về chính nhân vật chính. Hiểu lầm lớn nhất nằm ở nhóm cuối.

<short pause> Nhóm đầu tiên là về sức mạnh. Hiểu lầm một: Sharingan có thể sao chép bất kỳ kỹ thuật nào nó nhìn thấy.

<short pause> Phán quyết: nửa đúng.

<short pause> Sharingan đúng là có thể nhìn và ghi nhớ rất nhiều nhẫn thuật, ảo thuật và thể thuật, rồi bắt chước lại. Có ninja được mệnh danh là người đã sao chép hơn một nghìn kỹ thuật.

<short pause> Nhưng nó không sao chép được huyết kế giới hạn, những năng lực di truyền theo dòng máu. Nhìn một người dùng mộc độn hay một đôi mắt đặc biệt khác, Sharingan cũng không thể tự làm theo.

<short pause> Và sao chép rồi cũng phải có đủ chakra và thể chất để thực hiện. Nhìn thấy không có nghĩa là làm được.

<short pause> Vì sao dễ nhầm: vì những người dùng Sharingan trong truyện thường rất giỏi, khiến ta nghĩ đôi mắt làm được tất cả. Kaku đã phân tích kỹ Sharingan ở video số tám.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler toàn bộ Naruto và Naruto Shippuden, bao gồm cả cuộc Đại chiến ninja lần thứ tư và trận đấu cuối cùng.

[pause] Naruto kết thúc đã hơn mười năm, nhưng có những điều sai về nó vẫn được lặp lại mỗi ngày, trong bình luận, trong video, thậm chí trong những cuộc tranh luận của fan lâu năm.

[pause] [chuckles] Hôm nay Kaku mang theo hai con dấu. Một con dấu ghi SAI. Một con dấu ghi NỬA ĐÚNG. Mỗi hiểu lầm sẽ nhận một phán quyết.

[pause] Mở sổ ra nào! Mình là Kaku. Luật chơi: trước khi Kaku đóng dấu, bạn hãy tự đoán trong đầu. Cuối video, đếm xem bạn đoán đúng bao nhiêu câu.

[pause] Mười hiểu lầm chia làm ba nhóm: về sức mạnh, về thế giới ninja, và về chính nhân vật chính. Hiểu lầm lớn nhất nằm ở nhóm cuối.

[pause] Nhóm đầu tiên là về sức mạnh. Hiểu lầm một: Sharingan có thể sao chép bất kỳ kỹ thuật nào nó nhìn thấy.

[pause] Phán quyết: nửa đúng.

[pause] Sharingan đúng là có thể nhìn và ghi nhớ rất nhiều nhẫn thuật, ảo thuật và thể thuật, rồi bắt chước lại. Có ninja được mệnh danh là người đã sao chép hơn một nghìn kỹ thuật.

[pause] Nhưng nó không sao chép được huyết kế giới hạn, những năng lực di truyền theo dòng máu. Nhìn một người dùng mộc độn hay một đôi mắt đặc biệt khác, Sharingan cũng không thể tự làm theo.

[pause] Và sao chép rồi cũng phải có đủ chakra và thể chất để thực hiện. Nhìn thấy không có nghĩa là làm được.

[pause] Vì sao dễ nhầm: vì những người dùng Sharingan trong truyện thường rất giỏi, khiến ta nghĩ đôi mắt làm được tất cả. Kaku đã phân tích kỹ Sharingan ở video số tám.
```

### c02 · Giải thích nhanh: huyết kế giới hạn / Nhóm 1 · Hiểu lầm 2: Rasengan cần nguyên tố

Khoảng 115 giây · cảnh s12–s23 · 1495 ký tự

**Gemini**

```text
Trước khi đi tiếp, cần hiểu huyết kế giới hạn là gì, vì nó xuất hiện trong nhiều hiểu lầm hôm nay.

<short pause> Huyết kế giới hạn là những năng lực được truyền theo dòng máu, người ngoài gia tộc không thể học. Có hai kiểu chính.

<short pause> Kiểu thứ nhất là kết hợp hai tính chất chakra cùng lúc để tạo ra một tính chất mới. Ví dụ mộc độn là thổ cộng thủy, băng độn là phong cộng thủy.

<short pause> Kiểu thứ hai là những đôi mắt đặc biệt, gọi là đồng thuật, như đôi mắt nhìn xuyên vật thể hay đôi mắt đỏ sao chép kỹ thuật.

<short pause> Hiểu điều này rồi, bạn sẽ thấy vì sao có những thứ mà ngay cả thiên tài cũng không thể bắt chước.

<short pause> Hiểu lầm hai: Rasengan là một kỹ thuật hệ gió, hay ít nhất phải có một nguyên tố nào đó mới dùng được.

<short pause> Phán quyết: sai.

<short pause> Rasengan là kỹ thuật chỉ dùng biến đổi hình dạng của chakra: xoay chakra thật nhanh theo nhiều hướng, rồi nén nó vào một quả cầu. Không cần bất kỳ nguyên tố nào.

<short pause> Người tạo ra nó, Hokage đệ tứ, thực ra muốn thêm nguyên tố vào, nhưng chưa làm được. Đó mới là bước cuối cùng để hoàn thiện kỹ thuật.

<short pause> Naruto là người làm được điều đó khi thêm tính chất gió vào, tạo ra Phong độn Rasen Shuriken, mạnh tới mức gây tổn thương cho chính cơ thể người dùng lúc đầu.

<short pause> Để học Rasengan, Naruto phải đi qua ba bước luyện tập: làm vỡ quả bóng nước bằng cách xoay chakra, làm nổ quả bóng cao su bằng sức mạnh, rồi giữ tất cả trong một quả cầu mà không để nó tan ra.

<short pause> Vì sao dễ nhầm: vì phiên bản nổi tiếng nhất ở Shippuden là phiên bản gió, và nó xuất hiện nhiều tới mức người ta quên rằng Rasengan gốc không có nguyên tố.
```

**ElevenLabs**

```text
Trước khi đi tiếp, cần hiểu huyết kế giới hạn là gì, vì nó xuất hiện trong nhiều hiểu lầm hôm nay.

[pause] Huyết kế giới hạn là những năng lực được truyền theo dòng máu, người ngoài gia tộc không thể học. Có hai kiểu chính.

[pause] Kiểu thứ nhất là kết hợp hai tính chất chakra cùng lúc để tạo ra một tính chất mới. Ví dụ mộc độn là thổ cộng thủy, băng độn là phong cộng thủy.

[pause] Kiểu thứ hai là những đôi mắt đặc biệt, gọi là đồng thuật, như đôi mắt nhìn xuyên vật thể hay đôi mắt đỏ sao chép kỹ thuật.

[pause] Hiểu điều này rồi, bạn sẽ thấy vì sao có những thứ mà ngay cả thiên tài cũng không thể bắt chước.

[pause] Hiểu lầm hai: Rasengan là một kỹ thuật hệ gió, hay ít nhất phải có một nguyên tố nào đó mới dùng được.

[pause] Phán quyết: sai.

[pause] Rasengan là kỹ thuật chỉ dùng biến đổi hình dạng của chakra: xoay chakra thật nhanh theo nhiều hướng, rồi nén nó vào một quả cầu. Không cần bất kỳ nguyên tố nào.

[pause] Người tạo ra nó, Hokage đệ tứ, thực ra muốn thêm nguyên tố vào, nhưng chưa làm được. Đó mới là bước cuối cùng để hoàn thiện kỹ thuật.

[pause] Naruto là người làm được điều đó khi thêm tính chất gió vào, tạo ra Phong độn Rasen Shuriken, mạnh tới mức gây tổn thương cho chính cơ thể người dùng lúc đầu.

[pause] Để học Rasengan, Naruto phải đi qua ba bước luyện tập: làm vỡ quả bóng nước bằng cách xoay chakra, làm nổ quả bóng cao su bằng sức mạnh, rồi giữ tất cả trong một quả cầu mà không để nó tan ra.

[pause] Vì sao dễ nhầm: vì phiên bản nổi tiếng nhất ở Shippuden là phiên bản gió, và nó xuất hiện nhiều tới mức người ta quên rằng Rasengan gốc không có nguyên tố.
```

### c03 · Nhóm 1 · Hiểu lầm 3: Chakra chỉ để dùng nhẫn thuật / Nhóm 1 · Hiểu lầm 4: Chế độ hiền nhân ai cũng học được

Khoảng 112 giây · cảnh s24–s35 · 1452 ký tự

**Gemini**

```text
Hiểu lầm ba: chakra chỉ dùng để phun lửa, tạo nước, gọi thú. Ai không giỏi nhẫn thuật thì chakra cũng vô dụng.

<short pause> Phán quyết: sai.

<short pause> Chakra là sự kết hợp giữa năng lượng thể chất và năng lượng tinh thần. Nó có mặt trong gần như mọi hoạt động của ninja, từ đi trên mặt nước, leo cây bằng chân, tới chữa thương.

<short pause> Có một nhân vật không dùng được nhẫn thuật lẫn ảo thuật, nhưng trở thành một trong những bậc thầy thể thuật mạnh nhất, nhờ mở các cửa chakra trong cơ thể bằng luyện tập khắc nghiệt.

<short pause> Những cửa đó giới hạn dòng chakra để bảo vệ cơ thể. Mở càng nhiều cửa, sức mạnh càng lớn, và cái giá cho cơ thể càng khủng khiếp.

<short pause> Vì sao dễ nhầm: vì phần lớn trận đánh nổi bật trong truyện đều có nhẫn thuật rực rỡ. <short pause> Nhưng chakra là nền tảng, không chỉ là pháo hoa.

<short pause> Hiểu lầm bốn: chế độ hiền nhân chỉ là một kỹ thuật nâng cấp, ai chăm chỉ cũng học được.

<short pause> Phán quyết: sai.

<short pause> Chế độ hiền nhân đòi hỏi hấp thụ năng lượng tự nhiên và cân bằng nó hoàn hảo với chakra của bản thân. Thiếu một chút thì không có tác dụng.

<short pause> Thừa một chút thì còn đáng sợ hơn: người đó sẽ biến thành đá. Truyện cho thấy những bức tượng cóc bằng đá ở vùng núi của loài cóc chính là những người đã thất bại.

<short pause> Nó cũng cần một lượng chakra khổng lồ và sức bền phi thường. Naruto học được một phần nhờ lượng chakra lớn bất thường và cách dùng phân thân để thu năng lượng thay mình.

<short pause> Vì sao dễ nhầm: vì Naruto học nó khá nhanh trong một arc ngắn. <short pause> Nhưng chính truyện nhấn mạnh rằng rất ít người trong lịch sử làm được.
```

**ElevenLabs**

```text
Hiểu lầm ba: chakra chỉ dùng để phun lửa, tạo nước, gọi thú. Ai không giỏi nhẫn thuật thì chakra cũng vô dụng.

[pause] Phán quyết: sai.

[pause] Chakra là sự kết hợp giữa năng lượng thể chất và năng lượng tinh thần. Nó có mặt trong gần như mọi hoạt động của ninja, từ đi trên mặt nước, leo cây bằng chân, tới chữa thương.

[pause] Có một nhân vật không dùng được nhẫn thuật lẫn ảo thuật, nhưng trở thành một trong những bậc thầy thể thuật mạnh nhất, nhờ mở các cửa chakra trong cơ thể bằng luyện tập khắc nghiệt.

[pause] Những cửa đó giới hạn dòng chakra để bảo vệ cơ thể. Mở càng nhiều cửa, sức mạnh càng lớn, và cái giá cho cơ thể càng khủng khiếp.

[pause] Vì sao dễ nhầm: vì phần lớn trận đánh nổi bật trong truyện đều có nhẫn thuật rực rỡ. [pause] Nhưng chakra là nền tảng, không chỉ là pháo hoa.

[pause] Hiểu lầm bốn: chế độ hiền nhân chỉ là một kỹ thuật nâng cấp, ai chăm chỉ cũng học được.

[pause] Phán quyết: sai.

[pause] Chế độ hiền nhân đòi hỏi hấp thụ năng lượng tự nhiên và cân bằng nó hoàn hảo với chakra của bản thân. Thiếu một chút thì không có tác dụng.

[pause] Thừa một chút thì còn đáng sợ hơn: người đó sẽ biến thành đá. Truyện cho thấy những bức tượng cóc bằng đá ở vùng núi của loài cóc chính là những người đã thất bại.

[pause] Nó cũng cần một lượng chakra khổng lồ và sức bền phi thường. Naruto học được một phần nhờ lượng chakra lớn bất thường và cách dùng phân thân để thu năng lượng thay mình.

[pause] Vì sao dễ nhầm: vì Naruto học nó khá nhanh trong một arc ngắn. [pause] Nhưng chính truyện nhấn mạnh rằng rất ít người trong lịch sử làm được.
```

### c04 · Nhóm 2 · Hiểu lầm 5: Vĩ thú là quái vật vô tri / Nhóm 2 · Hiểu lầm 6: Hokage luôn là người mạnh nhất làng

Khoảng 126 giây · cảnh s36–s49 · 1633 ký tự

**Gemini**

```text
Nhóm thứ hai là về thế giới ninja. Hiểu lầm năm: vĩ thú chỉ là những quái vật khổng lồ, một nguồn năng lượng để các làng phong ấn và sử dụng.

<short pause> Phán quyết: sai.

<short pause> Chín vĩ thú được tạo ra khi Lục đạo tiên nhân chia chakra của Thập vĩ thành chín phần. Mỗi con có tên riêng, tính cách riêng, và được chính ông đặt tên.

<short pause> Suốt nhiều thế hệ, con người chỉ coi chúng là vũ khí. Chính vì bị đối xử như công cụ mà nhiều vĩ thú căm ghét loài người.

<short pause> Một trong những đoạn đẹp nhất truyện là khi Naruto dần hiểu và làm bạn với vĩ thú trong mình, thay vì chỉ cố khống chế nó.

<short pause> Những người mang vĩ thú trong người, gọi là nhân trụ lực, thường bị dân làng xa lánh và sợ hãi. Cả Naruto lẫn nhiều nhân trụ lực khác đều lớn lên trong cô đơn vì điều đó.

<short pause> Vì sao dễ nhầm: vì phần đầu truyện chỉ thể hiện vĩ thú qua sự phá hủy. Tính cách của chúng chỉ được hé lộ dần về sau.

<short pause> Hiểu lầm sáu: Hokage luôn là ninja mạnh nhất làng Lá.

<short pause> Phán quyết: nửa đúng.

<short pause> Đúng là nhiều Hokage cực kỳ mạnh, và sức mạnh là một phần quan trọng để được chọn. <short pause> Nhưng Hokage còn cần sự tín nhiệm và khả năng lãnh đạo.

<short pause> Có những ninja cực mạnh từng được mời làm Hokage nhưng từ chối, như một hiền nhân cóc thích tự do đi khắp nơi hơn là ngồi bàn giấy.

<short pause> Và cũng có Hokage được chọn chủ yếu vì hoàn cảnh và sự tin tưởng của mọi người, không phải vì là người mạnh nhất lúc đó.

<short pause> Hokage đầu tiên còn là người sáng lập làng, và nhiều Hokage về sau hy sinh tính mạng để bảo vệ làng. Với người trong làng, danh hiệu đó gắn với sự hy sinh nhiều hơn là quyền lực.

<short pause> Vì sao dễ nhầm: vì Naruto luôn nói muốn làm Hokage để được mọi người công nhận. Khán giả gắn Hokage với sức mạnh, còn truyện thì gắn nó với sự công nhận.
```

**ElevenLabs**

```text
Nhóm thứ hai là về thế giới ninja. Hiểu lầm năm: vĩ thú chỉ là những quái vật khổng lồ, một nguồn năng lượng để các làng phong ấn và sử dụng.

[pause] Phán quyết: sai.

[pause] Chín vĩ thú được tạo ra khi Lục đạo tiên nhân chia chakra của Thập vĩ thành chín phần. Mỗi con có tên riêng, tính cách riêng, và được chính ông đặt tên.

[pause] Suốt nhiều thế hệ, con người chỉ coi chúng là vũ khí. Chính vì bị đối xử như công cụ mà nhiều vĩ thú căm ghét loài người.

[pause] Một trong những đoạn đẹp nhất truyện là khi Naruto dần hiểu và làm bạn với vĩ thú trong mình, thay vì chỉ cố khống chế nó.

[pause] Những người mang vĩ thú trong người, gọi là nhân trụ lực, thường bị dân làng xa lánh và sợ hãi. Cả Naruto lẫn nhiều nhân trụ lực khác đều lớn lên trong cô đơn vì điều đó.

[pause] Vì sao dễ nhầm: vì phần đầu truyện chỉ thể hiện vĩ thú qua sự phá hủy. Tính cách của chúng chỉ được hé lộ dần về sau.

[pause] Hiểu lầm sáu: Hokage luôn là ninja mạnh nhất làng Lá.

[pause] Phán quyết: nửa đúng.

[pause] Đúng là nhiều Hokage cực kỳ mạnh, và sức mạnh là một phần quan trọng để được chọn. [pause] Nhưng Hokage còn cần sự tín nhiệm và khả năng lãnh đạo.

[pause] Có những ninja cực mạnh từng được mời làm Hokage nhưng từ chối, như một hiền nhân cóc thích tự do đi khắp nơi hơn là ngồi bàn giấy.

[pause] Và cũng có Hokage được chọn chủ yếu vì hoàn cảnh và sự tin tưởng của mọi người, không phải vì là người mạnh nhất lúc đó.

[pause] Hokage đầu tiên còn là người sáng lập làng, và nhiều Hokage về sau hy sinh tính mạng để bảo vệ làng. Với người trong làng, danh hiệu đó gắn với sự hy sinh nhiều hơn là quyền lực.

[pause] Vì sao dễ nhầm: vì Naruto luôn nói muốn làm Hokage để được mọi người công nhận. Khán giả gắn Hokage với sức mạnh, còn truyện thì gắn nó với sự công nhận.
```

### c05 · Nhóm 2 · Hiểu lầm 7: Itachi diệt tộc vì hắn là kẻ ác / Nhóm 2 · Hiểu lầm 8: Madara là trùm cuối

Khoảng 118 giây · cảnh s50–s62 · 1531 ký tự

**Gemini**

```text
Hiểu lầm bảy: người anh trai diệt cả gia tộc Uchiha trong một đêm vì hắn là một kẻ tàn độc, muốn thử sức mạnh của mình.

<short pause> Phán quyết: sai.

<short pause> Sự thật được hé lộ trong Shippuden: gia tộc đang lên kế hoạch đảo chính làng. Các lãnh đạo cấp cao của làng giao cho người anh trai nhiệm vụ ngăn chặn, bằng cái giá khủng khiếp nhất.

<short pause> Anh chấp nhận làm kẻ phản bội trong mắt mọi người, và tha cho em trai, để em lớn lên với lòng căm thù dành cho mình.

<short pause> Anh gia nhập một tổ chức tội phạm, nhưng thật ra vẫn âm thầm bảo vệ làng từ bên trong.

<short pause> Vì sao dễ nhầm: vì suốt phần đầu, truyện kể hoàn toàn qua ánh mắt của người em trai. Sự thật chỉ được kể lại rất muộn, sau khi đã quá muộn.

<short pause> Hiểu lầm tám: kẻ thù cuối cùng của cuộc Đại chiến ninja lần thứ tư là Madara Uchiha.

<short pause> Phán quyết: sai.

<short pause> Madara đúng là kẻ đứng sau kế hoạch Nguyệt Nhãn và là đối thủ khủng khiếp nhất của cuộc chiến. <short pause> Nhưng chính hắn cũng bị lợi dụng.

<short pause> Một thực thể đen sống ký sinh đã âm thầm thao túng lịch sử suốt nhiều thế kỷ, để hồi sinh người mẹ của mình: một nữ thần có sức mạnh vượt xa mọi ninja, là tổ tiên của toàn bộ chakra.

<short pause> Người phụ nữ đó mới là đối thủ cuối cùng mà Naruto và Sasuke phải đối mặt trong cuộc chiến.

<short pause> Chi tiết này được cài cắm từ khá sớm: những bức phù điêu cổ trong đền thờ của gia tộc có ghi lại lịch sử, nhưng bị bóp méo để dẫn dắt những người đọc chúng theo hướng mà kẻ giật dây mong muốn.

<short pause> Vì sao dễ nhầm: vì Madara được xây dựng như một huyền thoại suốt nhiều năm, còn đối thủ thật sự xuất hiện rất muộn. Nhiều người vẫn tranh cãi liệu cú xoay chiều đó có hợp lý không.
```

**ElevenLabs**

```text
Hiểu lầm bảy: người anh trai diệt cả gia tộc Uchiha trong một đêm vì hắn là một kẻ tàn độc, muốn thử sức mạnh của mình.

[pause] Phán quyết: sai.

[pause] Sự thật được hé lộ trong Shippuden: gia tộc đang lên kế hoạch đảo chính làng. Các lãnh đạo cấp cao của làng giao cho người anh trai nhiệm vụ ngăn chặn, bằng cái giá khủng khiếp nhất.

[pause] Anh chấp nhận làm kẻ phản bội trong mắt mọi người, và tha cho em trai, để em lớn lên với lòng căm thù dành cho mình.

[pause] Anh gia nhập một tổ chức tội phạm, nhưng thật ra vẫn âm thầm bảo vệ làng từ bên trong.

[pause] Vì sao dễ nhầm: vì suốt phần đầu, truyện kể hoàn toàn qua ánh mắt của người em trai. Sự thật chỉ được kể lại rất muộn, sau khi đã quá muộn.

[pause] Hiểu lầm tám: kẻ thù cuối cùng của cuộc Đại chiến ninja lần thứ tư là Madara Uchiha.

[pause] Phán quyết: sai.

[pause] Madara đúng là kẻ đứng sau kế hoạch Nguyệt Nhãn và là đối thủ khủng khiếp nhất của cuộc chiến. [pause] Nhưng chính hắn cũng bị lợi dụng.

[pause] Một thực thể đen sống ký sinh đã âm thầm thao túng lịch sử suốt nhiều thế kỷ, để hồi sinh người mẹ của mình: một nữ thần có sức mạnh vượt xa mọi ninja, là tổ tiên của toàn bộ chakra.

[pause] Người phụ nữ đó mới là đối thủ cuối cùng mà Naruto và Sasuke phải đối mặt trong cuộc chiến.

[pause] Chi tiết này được cài cắm từ khá sớm: những bức phù điêu cổ trong đền thờ của gia tộc có ghi lại lịch sử, nhưng bị bóp méo để dẫn dắt những người đọc chúng theo hướng mà kẻ giật dây mong muốn.

[pause] Vì sao dễ nhầm: vì Madara được xây dựng như một huyền thoại suốt nhiều năm, còn đối thủ thật sự xuất hiện rất muộn. Nhiều người vẫn tranh cãi liệu cú xoay chiều đó có hợp lý không.
```

### c06 · Nhóm 3 · Hiểu lầm 9: Naruto là học sinh vô dụng

Khoảng 71 giây · cảnh s63–s69 · 923 ký tự

**Gemini**

```text
Nhóm cuối cùng là về chính nhân vật chính. Hiểu lầm chín: Naruto khởi đầu là một học sinh vô dụng, không có chút tài năng nào.

<short pause> Phán quyết: nửa đúng.

<short pause> Naruto đúng là đứng bét lớp ở học viện, trượt nhiều bài kiểm tra, và không làm nổi kỹ thuật phân thân cơ bản nhất.

<short pause> Nhưng cậu có lượng chakra và sức bền vượt xa người thường. Và chỉ trong một đêm, cậu học được một kỹ thuật cấm: tạo ra rất nhiều phân thân thật từ một cuộn giấy phong ấn.

<short pause> Về sau, chính kỹ thuật đó trở thành bí quyết luyện tập của cậu: mỗi phân thân học được gì, bản gốc cũng nhận lại kinh nghiệm đó. Luyện một ngày bằng cả trăm ngày.

<short pause> Chiến thuật thích dùng số đông phân thân cũng thể hiện tính cách của cậu: không có tài năng tinh tế, cậu bù bằng sự lì lợm và sáng tạo, như dùng phân thân để đánh lạc hướng hay tạo ra những đòn bất ngờ.

<short pause> Vì sao dễ nhầm: vì truyện cố tình giới thiệu Naruto như một kẻ bị ruồng bỏ. Tài năng của cậu không nằm ở nơi trường học đo được.
```

**ElevenLabs**

```text
Nhóm cuối cùng là về chính nhân vật chính. Hiểu lầm chín: Naruto khởi đầu là một học sinh vô dụng, không có chút tài năng nào.

[pause] Phán quyết: nửa đúng.

[pause] Naruto đúng là đứng bét lớp ở học viện, trượt nhiều bài kiểm tra, và không làm nổi kỹ thuật phân thân cơ bản nhất.

[pause] Nhưng cậu có lượng chakra và sức bền vượt xa người thường. Và chỉ trong một đêm, cậu học được một kỹ thuật cấm: tạo ra rất nhiều phân thân thật từ một cuộn giấy phong ấn.

[pause] Về sau, chính kỹ thuật đó trở thành bí quyết luyện tập của cậu: mỗi phân thân học được gì, bản gốc cũng nhận lại kinh nghiệm đó. Luyện một ngày bằng cả trăm ngày.

[pause] Chiến thuật thích dùng số đông phân thân cũng thể hiện tính cách của cậu: không có tài năng tinh tế, cậu bù bằng sự lì lợm và sáng tạo, như dùng phân thân để đánh lạc hướng hay tạo ra những đòn bất ngờ.

[pause] Vì sao dễ nhầm: vì truyện cố tình giới thiệu Naruto như một kẻ bị ruồng bỏ. Tài năng của cậu không nằm ở nơi trường học đo được.
```

### c07 · Nhóm 3 · Hiểu lầm 10: Naruto thành công nhờ định mệnh / Ba hiểu lầm nhanh

Khoảng 143 giây · cảnh s70–s81 · 1855 ký tự

**Gemini**

```text
Và đây là hiểu lầm lớn nhất. Hiểu lầm mười: Naruto thành công vì cậu là người được định mệnh chọn, với dòng máu đặc biệt và vĩ thú mạnh nhất trong người.

<short pause> Phán quyết: nửa đúng. Và nửa sai của nó chính là thông điệp của cả bộ truyện.

<short pause> Nửa đúng: cuối truyện tiết lộ Naruto là chuyển thế của một trong hai người con của Lục đạo tiên nhân. Cậu mang cửu vĩ, là con của Hokage đệ tứ. Nghe rất giống người được chọn.

<short pause> Nhưng hãy nhìn lý do người cha chọn người con thứ hai làm người kế thừa. Người anh là thiên tài, dựa vào sức mạnh của bản thân. Người em không có tài năng nổi bật, nhưng mạnh lên nhờ nỗ lực và nhờ những người đứng bên cạnh mình.

<short pause> Nghĩa là ngay cả định mệnh của Naruto cũng là định mệnh của người nỗ lực. Dòng máu cho cậu cơ hội, nhưng không làm thay cậu những năm bị ruồng bỏ và cố gắng.

<short pause> Và hãy nhớ, người anh trong câu chuyện cổ ấy, dù là thiên tài, cũng không sai hoàn toàn. Truyện cho thấy cả hai cách đều có giá trị, và cuộc chiến giữa hai anh em chỉ kết thúc khi họ hiểu nhau.

<short pause> Vì sao dễ nhầm: vì những tiết lộ về dòng máu đến rất muộn và rất ồn ào. Chúng làm lu mờ bảy trăm chương về một cậu bé cô độc cố gắng để được công nhận.

<short pause> <laugh> Trước góc nhìn cuối, Kaku tặng thêm ba hiểu lầm nhỏ, xử lý thật nhanh.

<short pause> Một: người thầy đeo mặt nạ lúc nào cũng cầm một cuốn sách là vì lười. <short pause> Thật ra đó là bộ tiểu thuyết do chính vị hiền nhân cóc viết, và ông ấy là một fan cuồng thực sự.

<short pause> Hai: ninja phải dùng hai tay kết ấn mới dùng được nhẫn thuật. Có mười hai thủ ấn cơ bản, mang tên mười hai con giáp. <short pause> Nhưng truyện có nhân vật kết ấn chỉ bằng một tay, và những người mạnh nhất có thể không cần ấn.

<short pause> Ba: đôi mắt nhìn xuyên vật thể thấy được ba trăm sáu mươi độ, không có góc chết. Truyện cho thấy nó có một điểm mù nhỏ ở phía sau gáy, và đối thủ đã từng lợi dụng điểm mù đó.

<short pause> Nếu bạn biết cả ba điều này từ trước, Kaku chính thức công nhận bạn là fan Naruto hạng thượng nhẫn.
```

**ElevenLabs**

```text
Và đây là hiểu lầm lớn nhất. Hiểu lầm mười: Naruto thành công vì cậu là người được định mệnh chọn, với dòng máu đặc biệt và vĩ thú mạnh nhất trong người.

[pause] Phán quyết: nửa đúng. Và nửa sai của nó chính là thông điệp của cả bộ truyện.

[pause] Nửa đúng: cuối truyện tiết lộ Naruto là chuyển thế của một trong hai người con của Lục đạo tiên nhân. Cậu mang cửu vĩ, là con của Hokage đệ tứ. Nghe rất giống người được chọn.

[pause] Nhưng hãy nhìn lý do người cha chọn người con thứ hai làm người kế thừa. Người anh là thiên tài, dựa vào sức mạnh của bản thân. Người em không có tài năng nổi bật, nhưng mạnh lên nhờ nỗ lực và nhờ những người đứng bên cạnh mình.

[pause] Nghĩa là ngay cả định mệnh của Naruto cũng là định mệnh của người nỗ lực. Dòng máu cho cậu cơ hội, nhưng không làm thay cậu những năm bị ruồng bỏ và cố gắng.

[pause] Và hãy nhớ, người anh trong câu chuyện cổ ấy, dù là thiên tài, cũng không sai hoàn toàn. Truyện cho thấy cả hai cách đều có giá trị, và cuộc chiến giữa hai anh em chỉ kết thúc khi họ hiểu nhau.

[pause] Vì sao dễ nhầm: vì những tiết lộ về dòng máu đến rất muộn và rất ồn ào. Chúng làm lu mờ bảy trăm chương về một cậu bé cô độc cố gắng để được công nhận.

[pause] [chuckles] Trước góc nhìn cuối, Kaku tặng thêm ba hiểu lầm nhỏ, xử lý thật nhanh.

[pause] Một: người thầy đeo mặt nạ lúc nào cũng cầm một cuốn sách là vì lười. [pause] Thật ra đó là bộ tiểu thuyết do chính vị hiền nhân cóc viết, và ông ấy là một fan cuồng thực sự.

[pause] Hai: ninja phải dùng hai tay kết ấn mới dùng được nhẫn thuật. Có mười hai thủ ấn cơ bản, mang tên mười hai con giáp. [pause] Nhưng truyện có nhân vật kết ấn chỉ bằng một tay, và những người mạnh nhất có thể không cần ấn.

[pause] Ba: đôi mắt nhìn xuyên vật thể thấy được ba trăm sáu mươi độ, không có góc chết. Truyện cho thấy nó có một điểm mù nhỏ ở phía sau gáy, và đối thủ đã từng lợi dụng điểm mù đó.

[pause] Nếu bạn biết cả ba điều này từ trước, Kaku chính thức công nhận bạn là fan Naruto hạng thượng nhẫn.
```

### c08 · Góc nhìn của Kaku: nỗ lực hay định mệnh? / Bảng phán quyết / Kết

Khoảng 123 giây · cảnh s82–s92 · 1601 ký tự

**Gemini**

```text
<laugh> Nhìn lại mười hiểu lầm, Kaku thấy phần lớn chúng xoay quanh một câu hỏi mà Naruto đặt ra từ rất sớm: sức mạnh đến từ tài năng bẩm sinh, hay từ nỗ lực?

<short pause> Truyện có những thiên tài như người anh trai tộc Uchiha, và những người chăm chỉ như cậu bé chỉ dùng thể thuật. Có những đôi mắt đặc biệt, và có những người không có gì ngoài ý chí.

<short pause> Có một câu nói nổi tiếng trong truyện, từ một thiên tài với đôi mắt trắng: số phận của mỗi người đã được định sẵn. Và Naruto là người phản bác lại câu nói ấy.

<short pause> Kaku nghĩ câu trả lời của Naruto không phải là định mệnh không tồn tại. Mà là: dù được sinh ra với điều gì, thứ quyết định bạn trở thành ai vẫn là những gì bạn làm với nó.

<short pause> Và đó là lý do nhiều người lớn lên cùng Naruto vẫn nhớ về cậu. Không phải vì cậu được chọn, mà vì cậu chưa bao giờ bỏ cuộc.

<short pause> Tổng kết bảng phán quyết. Nhóm sức mạnh: Sharingan sao chép mọi thứ, nửa đúng. Rasengan cần nguyên tố, sai. Chakra chỉ cho nhẫn thuật, sai. Chế độ hiền nhân ai cũng học được, sai.

<short pause> Nhóm thế giới: vĩ thú vô tri, sai. Hokage luôn mạnh nhất, nửa đúng. Người anh diệt tộc vì tàn ác, sai. Madara là trùm cuối, sai.

<short pause> Nhóm nhân vật chính: Naruto là học sinh vô dụng, nửa đúng. Naruto thành công nhờ định mệnh, nửa đúng.

<short pause> Giờ đếm điểm: bạn đoán đúng bao nhiêu phán quyết? Từ tám câu trở lên là bạn đã sẵn sàng thi lên trung nhẫn. Viết điểm của bạn vào phần bình luận nhé.

<short pause> Video tới, Kaku mời bạn bước vào một căn phòng mà một ngày bên ngoài bằng một năm bên trong: Phòng Thời Gian Tinh Thần của Dragon Ball. Liệu bạn sống sót và mạnh lên được bao nhiêu?

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất hai con dấu đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Nhìn lại mười hiểu lầm, Kaku thấy phần lớn chúng xoay quanh một câu hỏi mà Naruto đặt ra từ rất sớm: sức mạnh đến từ tài năng bẩm sinh, hay từ nỗ lực?

[pause] Truyện có những thiên tài như người anh trai tộc Uchiha, và những người chăm chỉ như cậu bé chỉ dùng thể thuật. Có những đôi mắt đặc biệt, và có những người không có gì ngoài ý chí.

[pause] Có một câu nói nổi tiếng trong truyện, từ một thiên tài với đôi mắt trắng: số phận của mỗi người đã được định sẵn. Và Naruto là người phản bác lại câu nói ấy.

[pause] Kaku nghĩ câu trả lời của Naruto không phải là định mệnh không tồn tại. Mà là: dù được sinh ra với điều gì, thứ quyết định bạn trở thành ai vẫn là những gì bạn làm với nó.

[pause] Và đó là lý do nhiều người lớn lên cùng Naruto vẫn nhớ về cậu. Không phải vì cậu được chọn, mà vì cậu chưa bao giờ bỏ cuộc.

[pause] Tổng kết bảng phán quyết. Nhóm sức mạnh: Sharingan sao chép mọi thứ, nửa đúng. Rasengan cần nguyên tố, sai. Chakra chỉ cho nhẫn thuật, sai. Chế độ hiền nhân ai cũng học được, sai.

[pause] Nhóm thế giới: vĩ thú vô tri, sai. Hokage luôn mạnh nhất, nửa đúng. Người anh diệt tộc vì tàn ác, sai. Madara là trùm cuối, sai.

[pause] Nhóm nhân vật chính: Naruto là học sinh vô dụng, nửa đúng. Naruto thành công nhờ định mệnh, nửa đúng.

[pause] [curious] Giờ đếm điểm: bạn đoán đúng bao nhiêu phán quyết? Từ tám câu trở lên là bạn đã sẵn sàng thi lên trung nhẫn. Viết điểm của bạn vào phần bình luận nhé.

[pause] Video tới, Kaku mời bạn bước vào một căn phòng mà một ngày bên ngoài bằng một năm bên trong: Phòng Thời Gian Tinh Thần của Dragon Ball. Liệu bạn sống sót và mạnh lên được bao nhiêu?

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất hai con dấu đây, hẹn gặp lại!
```
