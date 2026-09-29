# Bộ prompt · One Piece: Dòng thời gian 800 năm và bí ẩn Thế kỷ trống

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

Lời: Cảnh báo: video có spoiler One Piece tới hết arc Egghead trong anime. Arc Elbaph đang phát năm 2026 chỉ được…

```text
Wide 16:9 landscape cinematic frame. an ancient stone tablet half-buried in sand, glowing faintly under a stormy sky. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Tám trăm năm trước, hai mươi vị vua đứng trên đỉnh một bức tường đá khổng lồ chia đôi thế giới. Họ vừa thắng…

```text
Wide 16:9 landscape cinematic frame. twenty regal silhouettes standing atop a colossal red cliff wall at sunset, banners snapping in the wind. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Một trăm năm lịch sử trước đó bị xóa sạch. Ai tìm hiểu về nó thì bị coi là tội phạm. Người ta gọi khoảng thời…

```text
Wide 16:9 landscape cinematic frame. a thick history book with a hundred blank pages in the middle, torn edges glowing. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Hôm nay Kaku trải một cuộn giấy thật dài, và xếp lại mọi mốc thời gian mà One Piece đã hé lộ, từ trước Thế kỷ…

```text
Wide 16:9 landscape cinematic frame. a very long scroll unrolling across a wooden floor, dates and small drawings along its length. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Mỗi chương hôm nay là một mốc thời gian. Những gì truyện đã xác nhận, Kaku nói là…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning two labels onto the scroll: a solid pin and a dotted question-mark pin. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Cách đọc dòng thời gian

Lời: One Piece thường tính thời gian theo kiểu bao nhiêu năm trước hiện tại. Hiện tại là thời điểm nhân vật chính…

```text
Wide 16:9 landscape cinematic frame. a timeline arrow with a glowing marker labeled NOW at the right end. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Thế kỷ trống kéo dài một trăm năm, từ khoảng chín trăm năm trước tới tám trăm năm trước. Sau đó là tám thế kỷ…

```text
Wide 16:9 landscape cinematic frame. a timeline with a dark gap between 900 and 800 years ago, then a long lighter segment to the present. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nguồn thông tin về quá khứ rất ít: những phiến đá cổ khắc chữ không ai đọc được, lời kể của vài người sống só…

```text
Wide 16:9 landscape cinematic frame. a desk with a stone rubbing, an old diary and a crackling radio transmitter. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì vậy, dòng thời gian này giống một bức tranh ghép còn thiếu rất nhiều mảnh. Kaku sẽ chỉ ghép những mảnh đã…

```text
Wide 16:9 landscape cinematic frame. a jigsaw puzzle of a world map with many missing pieces, a few pieces in the owl mascot's wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · Bản đồ thế giới hôm nay

Lời: Trước khi đi ngược thời gian, hãy nhìn bản đồ thế giới One Piece ở hiện tại, vì chính bản đồ này là kết quả c…

```text
Wide 16:9 landscape cinematic frame. a stylized world map mostly ocean, split by a red vertical wall and a blue horizontal band. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Thế giới bị chia làm bốn phần bởi hai đường lớn. Đường thẳng đứng là Red Line, một bức tường đá đỏ khổng lồ c…

```text
Wide 16:9 landscape cinematic frame. the red rock wall and the dangerous sea route crossing each other in a giant cross shape. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Hai bên Grand Line là hai vùng biển lặng không có gió, nơi những con thủy quái khổng lồ sinh sống. Tàu thường…

```text
Wide 16:9 landscape cinematic frame. a windless sea with a small becalmed ship and enormous sea monster shadows beneath it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Bốn phần còn lại là bốn vùng biển, Đông, Tây, Nam, Bắc. Nhân vật chính xuất phát từ biển Đông, được xem là vù…

```text
Wide 16:9 landscape cinematic frame. four quadrants of ocean labeled with compass icons, a tiny boat setting out from one of them. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và thủ đô của Chính phủ Thế giới nằm ngay trên đỉnh bức tường đá đỏ. Nghĩa là những người cai trị đứng, theo…

```text
Wide 16:9 landscape cinematic frame. a palace glittering on top of the red wall, far above clouds and tiny ships. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nhớ bản đồ này nhé, vì lát nữa ở mốc biển dâng, bạn sẽ nhìn nó theo một cách hoàn toàn khác.

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping the map with a wing, a small wave icon hovering above. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Trước Thế kỷ trống

Lời: Điểm xa nhất: trước khi Thế kỷ trống bắt đầu. Truyện gần như không kể gì về thời kỳ này, ngoài vài dấu vết kỳ…

```text
Wide 16:9 landscape cinematic frame. a misty ancient landscape with ruins of strange architecture, too advanced for its era. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Dấu vết lớn nhất là công nghệ. Trên hòn đảo khoa học ở arc Egghead, người ta tìm thấy những thứ cho thấy thời…

```text
Wide 16:9 landscape cinematic frame. a futuristic lab discovering an ancient machine part covered in moss, scientists staring in awe. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhà khoa học thiên tài nhất thế giới hiện tại từng thừa nhận: nhiều phát minh của ông chỉ là tái tạo lại nhữn…

```text
Wide 16:9 landscape cinematic frame. a scientist silhouette comparing his blueprint to an ancient carved diagram that looks nearly identical. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Một người máy khổng lồ cổ đại, được tìm thấy trong trạng thái ngủ, là bằng chứng rõ ràng nhất cho nền văn min…

```text
Wide 16:9 landscape cinematic frame. a colossal ancient robot slumped over and covered in vines, birds nesting on its shoulders. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một thế giới có công nghệ cao, rồi tụt lùi về thời thuyền buồm. Chuyện gì đã xảy ra? Câu trả lờ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding an ancient gear in one wing and a wooden ship wheel in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Thế kỷ trống: 900 đến 800 năm trước

Lời: Bước vào Thế kỷ trống. Truyện xác nhận rằng trong thời kỳ này có một vương quốc lớn, được gọi là Vương quốc V…

```text
Wide 16:9 landscape cinematic frame. a radiant ancient city with towering spires, bathed in golden light, its name hidden by fog. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Vương quốc này có một tư tưởng mà Chính phủ Thế giới sau này coi là mối đe dọa. Tư tưởng đó là gì, truyện vẫn…

```text
Wide 16:9 landscape cinematic frame. a glowing idea symbol above an ancient city, dark hands reaching toward it from the edges. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Trong thời kỳ này có một người tên Joy Boy, được xem là hải tặc đầu tiên. Ông để lại những lời hứa với nhiều…

```text
Wide 16:9 landscape cinematic frame. a lone laughing silhouette at the bow of a ship under a blazing sun. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Ở hòn đảo người cá dưới đáy biển, có một phiến đá cổ chứa lời xin lỗi của Joy Boy vì đã không thể giữ lời hứa…

```text
Wide 16:9 landscape cinematic frame. an ancient stone tablet deep under the sea, surrounded by glowing coral and curious fish. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Cũng trong thời kỳ này, những phiến đá cổ gọi là poneglyph được khắc ra. Chúng không thể bị phá hủy, và chứa…

```text
Wide 16:9 landscape cinematic frame. a massive cube of indestructible stone carved with ancient glyphs, cracks of light along the text. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: người ta khắc lịch sử vào đá không thể phá hủy, vì họ biết có người sẽ cố xóa nó. Đó là một hàn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot carefully carving a tiny symbol into a small stone with a chisel. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · 800 năm trước: ngày thành lập Chính phủ Thế giới

Lời: Tám trăm năm trước, cuộc chiến kết thúc. Một liên minh hai mươi vị vua đánh bại Vương quốc Vĩ đại và lập ra C…

```text
Wide 16:9 landscape cinematic frame. twenty crowns placed in a circle on a great stone table, a treaty scroll in the middle. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Mười chín gia tộc hoàng gia chuyển tới sống trên đỉnh bức tường đá đỏ chạy vòng quanh thế giới. Hậu duệ của h…

```text
Wide 16:9 landscape cinematic frame. a gleaming palace city atop a red rock wall that circles the world, clouds below it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Nhưng có một gia tộc từ chối. Họ ở lại vương quốc sa mạc của mình và sống như những người bình thường. Chi ti…

```text
Wide 16:9 landscape cinematic frame. a single royal family silhouette walking back toward a desert kingdom while the others ascend. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trong thánh địa trên đỉnh tường đá có một chiếc ngai được gọi là ngai trống, tượng trưng cho việc không ai đứ…

```text
Wide 16:9 landscape cinematic frame. an empty throne under a beam of light in a vast hall, twenty swords planted around it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Nhưng truyện đã cho thấy: chiếc ngai đó không hề trống. Có một nhân vật bí ẩn ngồi trên nó, và người đó dường…

```text
Wide 16:9 landscape cinematic frame. a shadowy figure seated on the empty throne, only a pair of glowing eyes visible. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một chính phủ dựng lên biểu tượng bình đẳng, nhưng sau biểu tượng đó là một người cai trị giấu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking behind a curtain and gasping. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Cũng 800 năm trước: biển dâng

Lời: Ở arc Egghead, nhà khoa học thiên tài phát đi một thông điệp cho cả thế giới, và tiết lộ một sự thật gây sốc…

```text
Wide 16:9 landscape cinematic frame. a giant holographic broadcast screen floating over the ocean, crowds on islands looking up. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Theo thông điệp đó, trong cuộc chiến cổ đại, vũ khí cổ đại đã được sử dụng, và mực nước biển trên toàn thế gi…

```text
Wide 16:9 landscape cinematic frame. a cross-section of ancient cities being swallowed by rising water, a measuring line showing 200 meters. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Điều đó có nghĩa là rất nhiều vùng đất của thế giới cũ đang nằm dưới đáy biển. Thế giới đầy đảo mà ta thấy hô…

```text
Wide 16:9 landscape cinematic frame. a map morphing from large continents into scattered islands as water rises. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Và ông cảnh báo rằng thế giới có thể chìm thêm nữa. Vũ khí cổ đại không chỉ là truyền thuyết, mà là thứ đã đị…

```text
Wide 16:9 landscape cinematic frame. a coastal city with water creeping up its streets, people looking worried. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: tự nhiên cái tên Grand Line, những vùng biển kỳ lạ, những hòn đảo trên trời, tất cả đều có thể…

```text
Wide 16:9 landscape cinematic frame. the owl mascot redrawing a map with a pencil, erasing coastlines. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Tám thế kỷ im lặng

Lời: Sau khi thành lập, Chính phủ Thế giới cấm tuyệt đối việc nghiên cứu Thế kỷ trống và đọc poneglyph. Vi phạm là…

```text
Wide 16:9 landscape cinematic frame. a notice board with an official decree nailed to it, a skull stamp at the bottom. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Các poneglyph bị phân tán khắp thế giới. Có phiến chứa thông tin về vũ khí cổ đại, có phiến chỉ đường tới hòn…

```text
Wide 16:9 landscape cinematic frame. a world map with scattered glowing stone icons of different colors. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Có một đất nước khép kín biên giới suốt nhiều thế kỷ. Gia tộc cai trị ở đó nắm giữ kỹ thuật khắc đá, và có li…

```text
Wide 16:9 landscape cinematic frame. a mountainous island nation surrounded by towering cliffs and waterfalls, a closed gate at its harbor. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Trong tám trăm năm, lịch sử thật chỉ còn sống trong những phiến đá im lặng, và trong ký ức của những người kh…

```text
Wide 16:9 landscape cinematic frame. a quiet stone monument covered in moss, a single candle burning before it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · 38 năm trước: thời của những huyền thoại

Lời: Nhảy tới gần hiện tại hơn. Khoảng ba mươi tám năm trước, ở một hòn đảo tên là Thung lũng Thần, xảy ra một sự…

```text
Wide 16:9 landscape cinematic frame. an island being erased from a map by a giant eraser, smoke rising where it once was. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Tại đó, một băng hải tặc khổng lồ bị đánh bại bởi sự hợp sức bất ngờ của một hải quân huyền thoại và một hải…

```text
Wide 16:9 landscape cinematic frame. a navy hero and a young pirate standing back to back against a massive pirate fleet silhouette. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Chi tiết về sự kiện này vẫn đang được hé lộ dần. Kaku chỉ ghi lại điều chắc chắn: đó là khởi đầu cho thời đại…

```text
Wide 16:9 landscape cinematic frame. a dusty history page with only a few lines legible, the rest smudged. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Chính phủ có thói quen xóa những hòn đảo khỏi bản đồ khi có điều gì bất lợi xảy ra. Thế kỷ trốn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a map with several islands cut out as holes. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · 25 năm trước: hòn đảo cuối cùng

Lời: Khoảng hai mươi lăm năm trước, băng hải tặc của Gol D. Roger đến được hòn đảo cuối cùng của Grand Line, nơi c…

```text
Wide 16:9 landscape cinematic frame. a weathered pirate ship approaching a mysterious island under a golden sky. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Theo truyện, khi biết được sự thật ở đó, ông bật cười, và đặt tên cho hòn đảo là Laugh Tale, câu chuyện khiến…

```text
Wide 16:9 landscape cinematic frame. a crew silhouette laughing on a beach, tears of laughter shining in the light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ông cũng nói rằng họ đến quá sớm. Nghĩa là thứ họ tìm thấy cần một thời điểm khác, và có thể một người khác,…

```text
Wide 16:9 landscape cinematic frame. a hand placing an hourglass on a treasure chest, sand still flowing. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Để đến được hòn đảo, cần đọc bốn phiến đá chỉ đường. Và trong băng của ông có một người đọc được chữ trên đá,…

```text
Wide 16:9 landscape cinematic frame. four red stone cubes placed on a map, lines connecting them to a hidden point. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cái tên Laugh Tale có lẽ là manh mối lớn nhất. Vì sao sự thật cuối cùng lại khiến người ta cười?

```text
Wide 16:9 landscape cinematic frame. the owl mascot chuckling nervously at a closed treasure chest. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · 24 năm trước: cái chết mở ra một kỷ nguyên

Lời: Hai mươi bốn năm trước, Vua Hải Tặc bị hành quyết trước đám đông. Nhưng trước khi chết, ông nói một câu làm t…

```text
Wide 16:9 landscape cinematic frame. a crowd gathered in a town square before an execution platform, a man smiling calmly. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ông nói kho báu của ông đang ở đó, ai muốn thì cứ việc đi tìm. Hàng nghìn người ra khơi. Kỷ nguyên hải tặc vĩ…

```text
Wide 16:9 landscape cinematic frame. hundreds of ships setting sail from a harbor at dawn, flags of every design flying. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Chính phủ muốn buổi hành quyết là lời cảnh cáo. Kết quả lại ngược lại: nó trở thành lời mời gọi lớn nhất lịch…

```text
Wide 16:9 landscape cinematic frame. a warning poster being torn apart by the wind and turning into a treasure map. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cũng giống như Thế kỷ trống, càng cố cấm người ta tìm hiểu, người ta càng muốn biết.

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to hold a door shut as light and curious faces push through. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · 22 năm trước: Ohara

Lời: Hai mươi hai năm trước, trên đảo Ohara, có những học giả lén nghiên cứu poneglyph suốt nhiều năm. Họ đã đọc đ…

```text
Wide 16:9 landscape cinematic frame. a giant ancient tree housing a library, scholars working by lamplight among towering bookshelves. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Chính phủ phát hiện ra. Họ ra lệnh tấn công bằng lực lượng hủy diệt, bắn phá hòn đảo cho tới khi không còn gì.

```text
Wide 16:9 landscape cinematic frame. warships surrounding a small island, cannon fire lighting up the night sky. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Các học giả ném sách xuống hồ để cứu lấy tri thức, dù biết mình không thể thoát. Một người trong số họ còn cố…

```text
Wide 16:9 landscape cinematic frame. scholars forming a chain to throw books into a lake as the great tree burns behind them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Chỉ có một cô bé tám tuổi sống sót. Cô đọc được chữ trên đá, và trở thành người duy nhất còn lại có thể đọc p…

```text
Wide 16:9 landscape cinematic frame. a small girl on a tiny boat drifting away from a burning island, clutching a book. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cô bé ấy bị truy nã từ năm tám tuổi, không phải vì đã làm gì, mà vì những gì cô có thể đọc được.

```text
Wide 16:9 landscape cinematic frame. a wanted poster with a child's silhouette pinned to a harbor wall in the rain. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là mốc thời gian buồn nhất trên cuộn giấy của Kaku. Tri thức bị coi là tội ác.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a single rescued book close to its chest. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Hiện tại: thế giới rung chuyển

Lời: Và giờ là hiện tại. Một chàng trai mang trái ác quỷ gắn với truyền thuyết thần mặt trời, vị thần giải phóng n…

```text
Wide 16:9 landscape cinematic frame. a young pirate silhouette on a ship's figurehead, sun rising behind him, laughter shaped clouds. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Thông điệp từ Egghead đã đến tai cả thế giới. Người dân bắt đầu hỏi những câu hỏi mà tám trăm năm nay không a…

```text
Wide 16:9 landscape cinematic frame. crowds in many towns gathered around radio snails and screens, whispering to each other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Ở arc Elbaph đang phát năm 2026, băng hải tặc đến vùng đất của người khổng lồ, nơi có những câu chuyện rất cổ…

```text
Wide 16:9 landscape cinematic frame. a colossal tree towering above clouds in a land of giants, a small ship approaching. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Có thể nói, lần đầu tiên sau tám trăm năm, Thế kỷ trống đang dần có chữ trở lại.

```text
Wide 16:9 landscape cinematic frame. blank pages of a history book slowly filling with glowing ink. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Lý thuyết: Vương quốc Vĩ đại muốn gì?

Lời: Tới phần lý thuyết. Kaku nhắc lại: phần này là suy đoán của fan và của Kaku, không phải sự thật đã được xác n…

```text
Wide 16:9 landscape cinematic frame. a big dotted question-mark pin placed on the scroll, a THEORY stamp next to it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Lý thuyết một: Vương quốc Vĩ đại muốn một thế giới không có tường ngăn cách, cả nghĩa đen lẫn nghĩa bóng. Và…

```text
Wide 16:9 landscape cinematic frame. a red wall splitting the world, with ancient figures trying to build a bridge across it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Lý thuyết hai: chữ D bí ẩn trong tên của nhiều nhân vật có liên quan tới những người thuộc phe thua cuộc tám…

```text
Wide 16:9 landscape cinematic frame. a single glowing letter D carved into ancient stone, surrounded by faded names. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Lý thuyết ba: Laugh Tale khiến người ta cười vì sự thật ở đó vừa vĩ đại vừa giản dị đến mức buồn cười, như mộ…

```text
Wide 16:9 landscape cinematic frame. a treasure chest opening to reveal warm light and a simple drawing, people laughing around it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Bạn tin lý thuyết nào? Hay bạn có lý thuyết riêng? Đây là lúc tuyệt vời nhất để đoán, vì câu trả lời có thể k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding three theory cards fanned out like a magician. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Góc nhìn của Kaku: ai viết lịch sử? · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn toàn bộ cuộn giấy, Kaku thấy One Piece đang kể một câu chuyện rất cũ: lịch sử luôn do người thắng viết.

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at the end of the long scroll, looking back along it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hai mươi vị vua thắng, nên họ xóa một trăm năm. Chính phủ sợ tri thức, nên họ đốt Ohara. Mỗi lần có sự thật b…

```text
Wide 16:9 landscape cinematic frame. a victorious hand holding a pen, erasing lines from a history book while ashes fall. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nhưng những người thua cũng không im lặng. Họ khắc sự thật vào đá. Họ ném sách xuống hồ. Họ truyền lại lời hứ…

```text
Wide 16:9 landscape cinematic frame. a montage of hands: one carving stone, one throwing a book into water, one passing a small keepsake to another hand. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và câu chuyện về một nhóm hải tặc tìm kho báu hóa ra lại là câu chuyện về việc tìm lại sự thật đã bị chôn vùi.

```text
Wide 16:9 landscape cinematic frame. a pirate crew standing before an ancient stone tablet at sunrise, reading it together. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kaku nghĩ đó là lý do One Piece có thể kéo dài gần ba mươi năm mà người ta vẫn chờ đợi: ai cũng muốn biết tra…

```text
Wide 16:9 landscape cinematic frame. blank pages fluttering in the wind over the sea, a few words beginning to appear. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Độ chắc chắn của từng mốc

Lời: Trước khi tổng kết, Kaku chấm độ chắc chắn của từng mốc, để bạn biết đâu là nền móng vững, đâu là cát lún.

```text
Wide 16:9 landscape cinematic frame. a scroll with small colored flags: green, yellow and red, pinned along its length. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Màu xanh, chắc chắn: việc thành lập Chính phủ Thế giới tám trăm năm trước, lệnh cấm nghiên cứu, cuộc tấn công…

```text
Wide 16:9 landscape cinematic frame. green flags on the government founding, the ban, the burning tree and the execution platform. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Màu vàng, đã xác nhận nhưng còn thiếu chi tiết: Vương quốc Vĩ đại, Joy Boy, nước biển dâng hai trăm mét, và s…

```text
Wide 16:9 landscape cinematic frame. yellow flags on the ancient city, the laughing silhouette, rising water and an erased island. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Màu đỏ, gần như chưa biết: tư tưởng của Vương quốc Vĩ đại, nội dung đầy đủ của Laugh Tale, và danh tính thật…

```text
Wide 16:9 landscape cinematic frame. red flags on a glowing idea symbol, a closed treasure chest and a shadowy throne. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: thú vị là những câu hỏi lớn nhất đều nằm ở màu đỏ. One Piece giữ những bí mật quan trọng nhất c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot guarding a small pile of red flags, looking excited. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Toàn bộ dòng thời gian

Lời: Tổng kết cả cuộn giấy. Hơn chín trăm năm trước: một nền văn minh có công nghệ vượt xa hiện tại.

```text
Wide 16:9 landscape cinematic frame. the scroll's leftmost section lighting up with an ancient machine drawing. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Chín trăm tới tám trăm năm trước: Thế kỷ trống, Vương quốc Vĩ đại, Joy Boy và các poneglyph. Tám trăm năm trư…

```text
Wide 16:9 landscape cinematic frame. the middle sections of the scroll lighting up with crowns, stones and rising water. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Ba mươi tám năm trước: Thung lũng Thần. Hai mươi lăm năm trước: Laugh Tale. Hai mươi bốn năm trước: Vua Hải T…

```text
Wide 16:9 landscape cinematic frame. the recent sections of the scroll lighting up with an island, a laughing crew, an execution and a burning tree. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Và hiện tại: thông điệp từ Egghead, và một con tàu đang tiến dần tới hòn đảo cuối cùng.

```text
Wide 16:9 landscape cinematic frame. the rightmost end of the scroll glowing with a small ship icon pointing forward. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được đọc một poneglyph duy nhất, bạn muốn nó kể về điều gì? Viết vào phần bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank stone tablet and a pencil toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Kết

Lời: Video tới sẽ đổi hướng: Kaku cầm kính lúp lên, điều tra một bí ẩn khác chưa có lời giải, Lục địa Đen trong Hu…

```text
Wide 16:9 landscape cinematic frame. a magnifying glass over a dark unexplored map edge, a compass spinning wildly. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cuộn giấy lại đây. Tám trăm năm, gói gọn trong mười lăm phút.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the long scroll and tying it with a red ribbon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc dòng thời gian

Khoảng 100 giây · cảnh s01–s09 · 1298 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler One Piece tới hết arc Egghead trong anime. Arc Elbaph đang phát năm 2026 chỉ được nhắc rất nhẹ.

<short pause> Tám trăm năm trước, hai mươi vị vua đứng trên đỉnh một bức tường đá khổng lồ chia đôi thế giới. Họ vừa thắng một cuộc chiến, và quyết định rằng thế giới sẽ quên đi những gì đã xảy ra.

<short pause> Một trăm năm lịch sử trước đó bị xóa sạch. Ai tìm hiểu về nó thì bị coi là tội phạm. Người ta gọi khoảng thời gian đó là Thế kỷ trống.

<short pause> Hôm nay Kaku trải một cuộn giấy thật dài, và xếp lại mọi mốc thời gian mà One Piece đã hé lộ, từ trước Thế kỷ trống cho tới hiện tại.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Mỗi chương hôm nay là một mốc thời gian. Những gì truyện đã xác nhận, Kaku nói là sự thật. Những gì còn là suy đoán, Kaku gắn nhãn lý thuyết thật rõ.

<short pause> One Piece thường tính thời gian theo kiểu bao nhiêu năm trước hiện tại. Hiện tại là thời điểm nhân vật chính đang ra khơi.

<short pause> Thế kỷ trống kéo dài một trăm năm, từ khoảng chín trăm năm trước tới tám trăm năm trước. Sau đó là tám thế kỷ dưới sự cai trị của Chính phủ Thế giới.

<short pause> Nguồn thông tin về quá khứ rất ít: những phiến đá cổ khắc chữ không ai đọc được, lời kể của vài người sống sót, và vài lời tiết lộ gây sốc ở những arc gần đây.

<short pause> Vì vậy, dòng thời gian này giống một bức tranh ghép còn thiếu rất nhiều mảnh. Kaku sẽ chỉ ghép những mảnh đã chắc chắn.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler One Piece tới hết arc Egghead trong anime. Arc Elbaph đang phát năm 2026 chỉ được nhắc rất nhẹ.

[pause] Tám trăm năm trước, hai mươi vị vua đứng trên đỉnh một bức tường đá khổng lồ chia đôi thế giới. Họ vừa thắng một cuộc chiến, và quyết định rằng thế giới sẽ quên đi những gì đã xảy ra.

[pause] Một trăm năm lịch sử trước đó bị xóa sạch. Ai tìm hiểu về nó thì bị coi là tội phạm. Người ta gọi khoảng thời gian đó là Thế kỷ trống.

[pause] Hôm nay Kaku trải một cuộn giấy thật dài, và xếp lại mọi mốc thời gian mà One Piece đã hé lộ, từ trước Thế kỷ trống cho tới hiện tại.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Mỗi chương hôm nay là một mốc thời gian. Những gì truyện đã xác nhận, Kaku nói là sự thật. Những gì còn là suy đoán, Kaku gắn nhãn lý thuyết thật rõ.

[pause] One Piece thường tính thời gian theo kiểu bao nhiêu năm trước hiện tại. Hiện tại là thời điểm nhân vật chính đang ra khơi.

[pause] Thế kỷ trống kéo dài một trăm năm, từ khoảng chín trăm năm trước tới tám trăm năm trước. Sau đó là tám thế kỷ dưới sự cai trị của Chính phủ Thế giới.

[pause] Nguồn thông tin về quá khứ rất ít: những phiến đá cổ khắc chữ không ai đọc được, lời kể của vài người sống sót, và vài lời tiết lộ gây sốc ở những arc gần đây.

[pause] Vì vậy, dòng thời gian này giống một bức tranh ghép còn thiếu rất nhiều mảnh. Kaku sẽ chỉ ghép những mảnh đã chắc chắn.
```

### c02 · Bản đồ thế giới hôm nay / Trước Thế kỷ trống

Khoảng 115 giây · cảnh s10–s20 · 1494 ký tự

**Gemini**

```text
Trước khi đi ngược thời gian, hãy nhìn bản đồ thế giới One Piece ở hiện tại, vì chính bản đồ này là kết quả của tám trăm năm lịch sử.

<short pause> Thế giới bị chia làm bốn phần bởi hai đường lớn. Đường thẳng đứng là Red Line, một bức tường đá đỏ khổng lồ chạy vòng quanh hành tinh. Đường nằm ngang là Grand Line, vùng biển nguy hiểm nhất.

<short pause> Hai bên Grand Line là hai vùng biển lặng không có gió, nơi những con thủy quái khổng lồ sinh sống. Tàu thường gần như không thể băng qua.

<short pause> Bốn phần còn lại là bốn vùng biển, Đông, Tây, Nam, Bắc. Nhân vật chính xuất phát từ biển Đông, được xem là vùng biển yên bình nhất.

<short pause> Và thủ đô của Chính phủ Thế giới nằm ngay trên đỉnh bức tường đá đỏ. Nghĩa là những người cai trị đứng, theo đúng nghĩa đen, trên đỉnh thế giới.

<short pause> <laugh> Kaku ghi chú: nhớ bản đồ này nhé, vì lát nữa ở mốc biển dâng, bạn sẽ nhìn nó theo một cách hoàn toàn khác.

<short pause> Điểm xa nhất: trước khi Thế kỷ trống bắt đầu. Truyện gần như không kể gì về thời kỳ này, ngoài vài dấu vết kỳ lạ.

<short pause> Dấu vết lớn nhất là công nghệ. Trên hòn đảo khoa học ở arc Egghead, người ta tìm thấy những thứ cho thấy thời cổ đại từng có công nghệ vượt xa hiện tại.

<short pause> Nhà khoa học thiên tài nhất thế giới hiện tại từng thừa nhận: nhiều phát minh của ông chỉ là tái tạo lại những gì người xưa đã làm được.

<short pause> Một người máy khổng lồ cổ đại, được tìm thấy trong trạng thái ngủ, là bằng chứng rõ ràng nhất cho nền văn minh đó.

<short pause> Kaku ghi chú: một thế giới có công nghệ cao, rồi tụt lùi về thời thuyền buồm. Chuyện gì đã xảy ra? Câu trả lời nằm trong trăm năm bị xóa.
```

**ElevenLabs**

```text
Trước khi đi ngược thời gian, hãy nhìn bản đồ thế giới One Piece ở hiện tại, vì chính bản đồ này là kết quả của tám trăm năm lịch sử.

[pause] Thế giới bị chia làm bốn phần bởi hai đường lớn. Đường thẳng đứng là Red Line, một bức tường đá đỏ khổng lồ chạy vòng quanh hành tinh. Đường nằm ngang là Grand Line, vùng biển nguy hiểm nhất.

[pause] Hai bên Grand Line là hai vùng biển lặng không có gió, nơi những con thủy quái khổng lồ sinh sống. Tàu thường gần như không thể băng qua.

[pause] Bốn phần còn lại là bốn vùng biển, Đông, Tây, Nam, Bắc. Nhân vật chính xuất phát từ biển Đông, được xem là vùng biển yên bình nhất.

[pause] Và thủ đô của Chính phủ Thế giới nằm ngay trên đỉnh bức tường đá đỏ. Nghĩa là những người cai trị đứng, theo đúng nghĩa đen, trên đỉnh thế giới.

[pause] [chuckles] Kaku ghi chú: nhớ bản đồ này nhé, vì lát nữa ở mốc biển dâng, bạn sẽ nhìn nó theo một cách hoàn toàn khác.

[pause] Điểm xa nhất: trước khi Thế kỷ trống bắt đầu. Truyện gần như không kể gì về thời kỳ này, ngoài vài dấu vết kỳ lạ.

[pause] Dấu vết lớn nhất là công nghệ. Trên hòn đảo khoa học ở arc Egghead, người ta tìm thấy những thứ cho thấy thời cổ đại từng có công nghệ vượt xa hiện tại.

[pause] Nhà khoa học thiên tài nhất thế giới hiện tại từng thừa nhận: nhiều phát minh của ông chỉ là tái tạo lại những gì người xưa đã làm được.

[pause] Một người máy khổng lồ cổ đại, được tìm thấy trong trạng thái ngủ, là bằng chứng rõ ràng nhất cho nền văn minh đó.

[pause] Kaku ghi chú: một thế giới có công nghệ cao, rồi tụt lùi về thời thuyền buồm. [curious] Chuyện gì đã xảy ra? Câu trả lời nằm trong trăm năm bị xóa.
```

### c03 · Thế kỷ trống: 900 đến 800 năm trước / 800 năm trước: ngày thành lập Chính phủ Thế giới

Khoảng 130 giây · cảnh s21–s32 · 1684 ký tự

**Gemini**

```text
Bước vào Thế kỷ trống. Truyện xác nhận rằng trong thời kỳ này có một vương quốc lớn, được gọi là Vương quốc Vĩ đại.

<short pause> Vương quốc này có một tư tưởng mà Chính phủ Thế giới sau này coi là mối đe dọa. Tư tưởng đó là gì, truyện vẫn chưa nói rõ.

<short pause> Trong thời kỳ này có một người tên Joy Boy, được xem là hải tặc đầu tiên. Ông để lại những lời hứa với nhiều nơi trên thế giới, và không phải lời hứa nào cũng được giữ.

<short pause> Ở hòn đảo người cá dưới đáy biển, có một phiến đá cổ chứa lời xin lỗi của Joy Boy vì đã không thể giữ lời hứa với họ.

<short pause> Cũng trong thời kỳ này, những phiến đá cổ gọi là poneglyph được khắc ra. Chúng không thể bị phá hủy, và chứa những thông tin mà kẻ chiến thắng muốn xóa đi.

<short pause> <laugh> Kaku ghi chú: người ta khắc lịch sử vào đá không thể phá hủy, vì họ biết có người sẽ cố xóa nó. Đó là một hành động rất can đảm.

<short pause> Tám trăm năm trước, cuộc chiến kết thúc. Một liên minh hai mươi vị vua đánh bại Vương quốc Vĩ đại và lập ra Chính phủ Thế giới.

<short pause> Mười chín gia tộc hoàng gia chuyển tới sống trên đỉnh bức tường đá đỏ chạy vòng quanh thế giới. Hậu duệ của họ trở thành tầng lớp cao nhất, đứng trên mọi luật lệ.

<short pause> Nhưng có một gia tộc từ chối. Họ ở lại vương quốc sa mạc của mình và sống như những người bình thường. Chi tiết này sẽ trở nên rất quan trọng.

<short pause> Trong thánh địa trên đỉnh tường đá có một chiếc ngai được gọi là ngai trống, tượng trưng cho việc không ai đứng trên ai trong số các vị vua.

<short pause> Nhưng truyện đã cho thấy: chiếc ngai đó không hề trống. Có một nhân vật bí ẩn ngồi trên nó, và người đó dường như đã tồn tại rất, rất lâu.

<short pause> Kaku ghi chú: một chính phủ dựng lên biểu tượng bình đẳng, nhưng sau biểu tượng đó là một người cai trị giấu mặt. Đây là một trong những hình ảnh mạnh nhất của One Piece.
```

**ElevenLabs**

```text
Bước vào Thế kỷ trống. Truyện xác nhận rằng trong thời kỳ này có một vương quốc lớn, được gọi là Vương quốc Vĩ đại.

[pause] Vương quốc này có một tư tưởng mà Chính phủ Thế giới sau này coi là mối đe dọa. Tư tưởng đó là gì, truyện vẫn chưa nói rõ.

[pause] Trong thời kỳ này có một người tên Joy Boy, được xem là hải tặc đầu tiên. Ông để lại những lời hứa với nhiều nơi trên thế giới, và không phải lời hứa nào cũng được giữ.

[pause] Ở hòn đảo người cá dưới đáy biển, có một phiến đá cổ chứa lời xin lỗi của Joy Boy vì đã không thể giữ lời hứa với họ.

[pause] Cũng trong thời kỳ này, những phiến đá cổ gọi là poneglyph được khắc ra. Chúng không thể bị phá hủy, và chứa những thông tin mà kẻ chiến thắng muốn xóa đi.

[pause] [chuckles] Kaku ghi chú: người ta khắc lịch sử vào đá không thể phá hủy, vì họ biết có người sẽ cố xóa nó. Đó là một hành động rất can đảm.

[pause] Tám trăm năm trước, cuộc chiến kết thúc. Một liên minh hai mươi vị vua đánh bại Vương quốc Vĩ đại và lập ra Chính phủ Thế giới.

[pause] Mười chín gia tộc hoàng gia chuyển tới sống trên đỉnh bức tường đá đỏ chạy vòng quanh thế giới. Hậu duệ của họ trở thành tầng lớp cao nhất, đứng trên mọi luật lệ.

[pause] Nhưng có một gia tộc từ chối. Họ ở lại vương quốc sa mạc của mình và sống như những người bình thường. Chi tiết này sẽ trở nên rất quan trọng.

[pause] Trong thánh địa trên đỉnh tường đá có một chiếc ngai được gọi là ngai trống, tượng trưng cho việc không ai đứng trên ai trong số các vị vua.

[pause] Nhưng truyện đã cho thấy: chiếc ngai đó không hề trống. Có một nhân vật bí ẩn ngồi trên nó, và người đó dường như đã tồn tại rất, rất lâu.

[pause] Kaku ghi chú: một chính phủ dựng lên biểu tượng bình đẳng, nhưng sau biểu tượng đó là một người cai trị giấu mặt. Đây là một trong những hình ảnh mạnh nhất của One Piece.
```

### c04 · Cũng 800 năm trước: biển dâng / Tám thế kỷ im lặng / 38 năm trước: thời của những huyền thoại

Khoảng 142 giây · cảnh s33–s45 · 1844 ký tự

**Gemini**

```text
Ở arc Egghead, nhà khoa học thiên tài phát đi một thông điệp cho cả thế giới, và tiết lộ một sự thật gây sốc về tám trăm năm trước.

<short pause> Theo thông điệp đó, trong cuộc chiến cổ đại, vũ khí cổ đại đã được sử dụng, và mực nước biển trên toàn thế giới đã dâng lên khoảng hai trăm mét.

<short pause> Điều đó có nghĩa là rất nhiều vùng đất của thế giới cũ đang nằm dưới đáy biển. Thế giới đầy đảo mà ta thấy hôm nay có thể là kết quả của một thảm họa.

<short pause> Và ông cảnh báo rằng thế giới có thể chìm thêm nữa. Vũ khí cổ đại không chỉ là truyền thuyết, mà là thứ đã định hình lại cả hành tinh.

<short pause> <laugh> Kaku ghi chú: tự nhiên cái tên Grand Line, những vùng biển kỳ lạ, những hòn đảo trên trời, tất cả đều có thể có lời giải thích mới.

<short pause> Sau khi thành lập, Chính phủ Thế giới cấm tuyệt đối việc nghiên cứu Thế kỷ trống và đọc poneglyph. Vi phạm là tội chết.

<short pause> Các poneglyph bị phân tán khắp thế giới. Có phiến chứa thông tin về vũ khí cổ đại, có phiến chỉ đường tới hòn đảo cuối cùng, có phiến kể lại lịch sử thật.

<short pause> Có một đất nước khép kín biên giới suốt nhiều thế kỷ. Gia tộc cai trị ở đó nắm giữ kỹ thuật khắc đá, và có liên quan mật thiết tới những phiến đá cổ.

<short pause> Trong tám trăm năm, lịch sử thật chỉ còn sống trong những phiến đá im lặng, và trong ký ức của những người không bao giờ được phép nói ra.

<short pause> Nhảy tới gần hiện tại hơn. Khoảng ba mươi tám năm trước, ở một hòn đảo tên là Thung lũng Thần, xảy ra một sự kiện lớn mà Chính phủ Thế giới cố xóa khỏi bản đồ.

<short pause> Tại đó, một băng hải tặc khổng lồ bị đánh bại bởi sự hợp sức bất ngờ của một hải quân huyền thoại và một hải tặc trẻ tuổi, người sau này trở thành Vua Hải Tặc.

<short pause> Chi tiết về sự kiện này vẫn đang được hé lộ dần. Kaku chỉ ghi lại điều chắc chắn: đó là khởi đầu cho thời đại của những nhân vật huyền thoại.

<short pause> Kaku ghi chú: Chính phủ có thói quen xóa những hòn đảo khỏi bản đồ khi có điều gì bất lợi xảy ra. Thế kỷ trống không phải lần duy nhất.
```

**ElevenLabs**

```text
Ở arc Egghead, nhà khoa học thiên tài phát đi một thông điệp cho cả thế giới, và tiết lộ một sự thật gây sốc về tám trăm năm trước.

[pause] Theo thông điệp đó, trong cuộc chiến cổ đại, vũ khí cổ đại đã được sử dụng, và mực nước biển trên toàn thế giới đã dâng lên khoảng hai trăm mét.

[pause] Điều đó có nghĩa là rất nhiều vùng đất của thế giới cũ đang nằm dưới đáy biển. Thế giới đầy đảo mà ta thấy hôm nay có thể là kết quả của một thảm họa.

[pause] Và ông cảnh báo rằng thế giới có thể chìm thêm nữa. Vũ khí cổ đại không chỉ là truyền thuyết, mà là thứ đã định hình lại cả hành tinh.

[pause] [chuckles] Kaku ghi chú: tự nhiên cái tên Grand Line, những vùng biển kỳ lạ, những hòn đảo trên trời, tất cả đều có thể có lời giải thích mới.

[pause] Sau khi thành lập, Chính phủ Thế giới cấm tuyệt đối việc nghiên cứu Thế kỷ trống và đọc poneglyph. Vi phạm là tội chết.

[pause] Các poneglyph bị phân tán khắp thế giới. Có phiến chứa thông tin về vũ khí cổ đại, có phiến chỉ đường tới hòn đảo cuối cùng, có phiến kể lại lịch sử thật.

[pause] Có một đất nước khép kín biên giới suốt nhiều thế kỷ. Gia tộc cai trị ở đó nắm giữ kỹ thuật khắc đá, và có liên quan mật thiết tới những phiến đá cổ.

[pause] Trong tám trăm năm, lịch sử thật chỉ còn sống trong những phiến đá im lặng, và trong ký ức của những người không bao giờ được phép nói ra.

[pause] Nhảy tới gần hiện tại hơn. Khoảng ba mươi tám năm trước, ở một hòn đảo tên là Thung lũng Thần, xảy ra một sự kiện lớn mà Chính phủ Thế giới cố xóa khỏi bản đồ.

[pause] Tại đó, một băng hải tặc khổng lồ bị đánh bại bởi sự hợp sức bất ngờ của một hải quân huyền thoại và một hải tặc trẻ tuổi, người sau này trở thành Vua Hải Tặc.

[pause] Chi tiết về sự kiện này vẫn đang được hé lộ dần. Kaku chỉ ghi lại điều chắc chắn: đó là khởi đầu cho thời đại của những nhân vật huyền thoại.

[pause] Kaku ghi chú: Chính phủ có thói quen xóa những hòn đảo khỏi bản đồ khi có điều gì bất lợi xảy ra. Thế kỷ trống không phải lần duy nhất.
```

### c05 · 25 năm trước: hòn đảo cuối cùng / 24 năm trước: cái chết mở ra một kỷ nguyên / 22 năm trước: Ohara

Khoảng 139 giây · cảnh s46–s60 · 1810 ký tự

**Gemini**

```text
Khoảng hai mươi lăm năm trước, băng hải tặc của Gol D. Roger đến được hòn đảo cuối cùng của Grand Line, nơi chưa ai từng đặt chân tới.

<short pause> Theo truyện, khi biết được sự thật ở đó, ông bật cười, và đặt tên cho hòn đảo là Laugh Tale, câu chuyện khiến người ta bật cười.

<short pause> Ông cũng nói rằng họ đến quá sớm. Nghĩa là thứ họ tìm thấy cần một thời điểm khác, và có thể một người khác, để hoàn thành.

<short pause> Để đến được hòn đảo, cần đọc bốn phiến đá chỉ đường. Và trong băng của ông có một người đọc được chữ trên đá, người đến từ đất nước khép kín kia.

<short pause> <laugh> Kaku ghi chú: cái tên Laugh Tale có lẽ là manh mối lớn nhất. Vì sao sự thật cuối cùng lại khiến người ta cười?

<short pause> Hai mươi bốn năm trước, Vua Hải Tặc bị hành quyết trước đám đông. <short pause> Nhưng trước khi chết, ông nói một câu làm thay đổi cả thế giới.

<short pause> Ông nói kho báu của ông đang ở đó, ai muốn thì cứ việc đi tìm. Hàng nghìn người ra khơi. Kỷ nguyên hải tặc vĩ đại bắt đầu.

<short pause> Chính phủ muốn buổi hành quyết là lời cảnh cáo. Kết quả lại ngược lại: nó trở thành lời mời gọi lớn nhất lịch sử.

<short pause> Kaku ghi chú: cũng giống như Thế kỷ trống, càng cố cấm người ta tìm hiểu, người ta càng muốn biết.

<short pause> Hai mươi hai năm trước, trên đảo Ohara, có những học giả lén nghiên cứu poneglyph suốt nhiều năm. Họ đã đọc được một phần lịch sử bị cấm.

<short pause> Chính phủ phát hiện ra. Họ ra lệnh tấn công bằng lực lượng hủy diệt, bắn phá hòn đảo cho tới khi không còn gì.

<short pause> Các học giả ném sách xuống hồ để cứu lấy tri thức, dù biết mình không thể thoát. Một người trong số họ còn cố nói to những gì đã biết trước khi bị bắn.

<short pause> Chỉ có một cô bé tám tuổi sống sót. Cô đọc được chữ trên đá, và trở thành người duy nhất còn lại có thể đọc poneglyph.

<short pause> Cô bé ấy bị truy nã từ năm tám tuổi, không phải vì đã làm gì, mà vì những gì cô có thể đọc được.

<short pause> Kaku ghi chú: đây là mốc thời gian buồn nhất trên cuộn giấy của Kaku. Tri thức bị coi là tội ác.
```

**ElevenLabs**

```text
Khoảng hai mươi lăm năm trước, băng hải tặc của Gol D. Roger đến được hòn đảo cuối cùng của Grand Line, nơi chưa ai từng đặt chân tới.

[pause] Theo truyện, khi biết được sự thật ở đó, ông bật cười, và đặt tên cho hòn đảo là Laugh Tale, câu chuyện khiến người ta bật cười.

[pause] Ông cũng nói rằng họ đến quá sớm. Nghĩa là thứ họ tìm thấy cần một thời điểm khác, và có thể một người khác, để hoàn thành.

[pause] Để đến được hòn đảo, cần đọc bốn phiến đá chỉ đường. Và trong băng của ông có một người đọc được chữ trên đá, người đến từ đất nước khép kín kia.

[pause] [chuckles] Kaku ghi chú: cái tên Laugh Tale có lẽ là manh mối lớn nhất. [curious] Vì sao sự thật cuối cùng lại khiến người ta cười?

[pause] Hai mươi bốn năm trước, Vua Hải Tặc bị hành quyết trước đám đông. [pause] Nhưng trước khi chết, ông nói một câu làm thay đổi cả thế giới.

[pause] Ông nói kho báu của ông đang ở đó, ai muốn thì cứ việc đi tìm. Hàng nghìn người ra khơi. Kỷ nguyên hải tặc vĩ đại bắt đầu.

[pause] Chính phủ muốn buổi hành quyết là lời cảnh cáo. Kết quả lại ngược lại: nó trở thành lời mời gọi lớn nhất lịch sử.

[pause] Kaku ghi chú: cũng giống như Thế kỷ trống, càng cố cấm người ta tìm hiểu, người ta càng muốn biết.

[pause] Hai mươi hai năm trước, trên đảo Ohara, có những học giả lén nghiên cứu poneglyph suốt nhiều năm. Họ đã đọc được một phần lịch sử bị cấm.

[pause] Chính phủ phát hiện ra. Họ ra lệnh tấn công bằng lực lượng hủy diệt, bắn phá hòn đảo cho tới khi không còn gì.

[pause] Các học giả ném sách xuống hồ để cứu lấy tri thức, dù biết mình không thể thoát. Một người trong số họ còn cố nói to những gì đã biết trước khi bị bắn.

[pause] Chỉ có một cô bé tám tuổi sống sót. Cô đọc được chữ trên đá, và trở thành người duy nhất còn lại có thể đọc poneglyph.

[pause] Cô bé ấy bị truy nã từ năm tám tuổi, không phải vì đã làm gì, mà vì những gì cô có thể đọc được.

[pause] Kaku ghi chú: đây là mốc thời gian buồn nhất trên cuộn giấy của Kaku. Tri thức bị coi là tội ác.
```

### c06 · Hiện tại: thế giới rung chuyển / Lý thuyết: Vương quốc Vĩ đại muốn gì? / Góc nhìn của Kaku: ai viết lịch sử?

Khoảng 146 giây · cảnh s61–s74 · 1892 ký tự

**Gemini**

```text
Và giờ là hiện tại. Một chàng trai mang trái ác quỷ gắn với truyền thuyết thần mặt trời, vị thần giải phóng người khác bằng tiếng cười, đang tiến gần hòn đảo cuối cùng.

<short pause> Thông điệp từ Egghead đã đến tai cả thế giới. Người dân bắt đầu hỏi những câu hỏi mà tám trăm năm nay không ai dám hỏi.

<short pause> Ở arc Elbaph đang phát năm 2026, băng hải tặc đến vùng đất của người khổng lồ, nơi có những câu chuyện rất cổ xưa. Kaku sẽ dừng ở đây để không spoiler.

<short pause> Có thể nói, lần đầu tiên sau tám trăm năm, Thế kỷ trống đang dần có chữ trở lại.

<short pause> Tới phần lý thuyết. Kaku nhắc lại: phần này là suy đoán của fan và của Kaku, không phải sự thật đã được xác nhận.

<short pause> Lý thuyết một: Vương quốc Vĩ đại muốn một thế giới không có tường ngăn cách, cả nghĩa đen lẫn nghĩa bóng. Và bức tường đá đỏ cùng các vùng biển chia cắt chính là thứ họ chống lại.

<short pause> Lý thuyết hai: chữ D bí ẩn trong tên của nhiều nhân vật có liên quan tới những người thuộc phe thua cuộc tám trăm năm trước. Kẻ thù tự nhiên của những người ngồi trên đỉnh tường.

<short pause> Lý thuyết ba: Laugh Tale khiến người ta cười vì sự thật ở đó vừa vĩ đại vừa giản dị đến mức buồn cười, như một câu chuyện mà ai cũng đáng được biết.

<short pause> Bạn tin lý thuyết nào? Hay bạn có lý thuyết riêng? Đây là lúc tuyệt vời nhất để đoán, vì câu trả lời có thể không còn xa nữa.

<short pause> <laugh> Nhìn toàn bộ cuộn giấy, Kaku thấy One Piece đang kể một câu chuyện rất cũ: lịch sử luôn do người thắng viết.

<short pause> Hai mươi vị vua thắng, nên họ xóa một trăm năm. Chính phủ sợ tri thức, nên họ đốt Ohara. Mỗi lần có sự thật bất lợi, một hòn đảo biến mất khỏi bản đồ.

<short pause> Nhưng những người thua cũng không im lặng. Họ khắc sự thật vào đá. Họ ném sách xuống hồ. Họ truyền lại lời hứa qua tám trăm năm.

<short pause> Và câu chuyện về một nhóm hải tặc tìm kho báu hóa ra lại là câu chuyện về việc tìm lại sự thật đã bị chôn vùi.

<short pause> Kaku nghĩ đó là lý do One Piece có thể kéo dài gần ba mươi năm mà người ta vẫn chờ đợi: ai cũng muốn biết trang giấy trắng kia viết gì.
```

**ElevenLabs**

```text
Và giờ là hiện tại. Một chàng trai mang trái ác quỷ gắn với truyền thuyết thần mặt trời, vị thần giải phóng người khác bằng tiếng cười, đang tiến gần hòn đảo cuối cùng.

[pause] Thông điệp từ Egghead đã đến tai cả thế giới. Người dân bắt đầu hỏi những câu hỏi mà tám trăm năm nay không ai dám hỏi.

[pause] Ở arc Elbaph đang phát năm 2026, băng hải tặc đến vùng đất của người khổng lồ, nơi có những câu chuyện rất cổ xưa. Kaku sẽ dừng ở đây để không spoiler.

[pause] Có thể nói, lần đầu tiên sau tám trăm năm, Thế kỷ trống đang dần có chữ trở lại.

[pause] Tới phần lý thuyết. Kaku nhắc lại: phần này là suy đoán của fan và của Kaku, không phải sự thật đã được xác nhận.

[pause] Lý thuyết một: Vương quốc Vĩ đại muốn một thế giới không có tường ngăn cách, cả nghĩa đen lẫn nghĩa bóng. Và bức tường đá đỏ cùng các vùng biển chia cắt chính là thứ họ chống lại.

[pause] Lý thuyết hai: chữ D bí ẩn trong tên của nhiều nhân vật có liên quan tới những người thuộc phe thua cuộc tám trăm năm trước. Kẻ thù tự nhiên của những người ngồi trên đỉnh tường.

[pause] Lý thuyết ba: Laugh Tale khiến người ta cười vì sự thật ở đó vừa vĩ đại vừa giản dị đến mức buồn cười, như một câu chuyện mà ai cũng đáng được biết.

[pause] [curious] Bạn tin lý thuyết nào? Hay bạn có lý thuyết riêng? Đây là lúc tuyệt vời nhất để đoán, vì câu trả lời có thể không còn xa nữa.

[pause] [chuckles] Nhìn toàn bộ cuộn giấy, Kaku thấy One Piece đang kể một câu chuyện rất cũ: lịch sử luôn do người thắng viết.

[pause] Hai mươi vị vua thắng, nên họ xóa một trăm năm. Chính phủ sợ tri thức, nên họ đốt Ohara. Mỗi lần có sự thật bất lợi, một hòn đảo biến mất khỏi bản đồ.

[pause] Nhưng những người thua cũng không im lặng. Họ khắc sự thật vào đá. Họ ném sách xuống hồ. Họ truyền lại lời hứa qua tám trăm năm.

[pause] Và câu chuyện về một nhóm hải tặc tìm kho báu hóa ra lại là câu chuyện về việc tìm lại sự thật đã bị chôn vùi.

[pause] Kaku nghĩ đó là lý do One Piece có thể kéo dài gần ba mươi năm mà người ta vẫn chờ đợi: ai cũng muốn biết trang giấy trắng kia viết gì.
```

### c07 · Độ chắc chắn của từng mốc / Toàn bộ dòng thời gian / Kết

Khoảng 124 giây · cảnh s75–s86 · 1609 ký tự

**Gemini**

```text
Trước khi tổng kết, Kaku chấm độ chắc chắn của từng mốc, để bạn biết đâu là nền móng vững, đâu là cát lún.

<short pause> Màu xanh, chắc chắn: việc thành lập Chính phủ Thế giới tám trăm năm trước, lệnh cấm nghiên cứu, cuộc tấn công Ohara, và buổi hành quyết Vua Hải Tặc. Truyện nói rõ nhiều lần.

<short pause> Màu vàng, đã xác nhận nhưng còn thiếu chi tiết: Vương quốc Vĩ đại, Joy Boy, nước biển dâng hai trăm mét, và sự kiện Thung lũng Thần. Ta biết chúng có thật, nhưng chưa biết đầy đủ.

<short pause> Màu đỏ, gần như chưa biết: tư tưởng của Vương quốc Vĩ đại, nội dung đầy đủ của Laugh Tale, và danh tính thật của người ngồi trên ngai trống.

<short pause> <laugh> Kaku ghi chú: thú vị là những câu hỏi lớn nhất đều nằm ở màu đỏ. One Piece giữ những bí mật quan trọng nhất cho tới cuối cùng.

<short pause> Tổng kết cả cuộn giấy. Hơn chín trăm năm trước: một nền văn minh có công nghệ vượt xa hiện tại.

<short pause> Chín trăm tới tám trăm năm trước: Thế kỷ trống, Vương quốc Vĩ đại, Joy Boy và các poneglyph. Tám trăm năm trước: hai mươi vị vua thắng, lập Chính phủ Thế giới, và biển dâng khoảng hai trăm mét.

<short pause> Ba mươi tám năm trước: Thung lũng Thần. Hai mươi lăm năm trước: Laugh Tale. Hai mươi bốn năm trước: Vua Hải Tặc bị hành quyết. Hai mươi hai năm trước: Ohara.

<short pause> Và hiện tại: thông điệp từ Egghead, và một con tàu đang tiến dần tới hòn đảo cuối cùng.

<short pause> Câu hỏi cho bạn: nếu được đọc một poneglyph duy nhất, bạn muốn nó kể về điều gì? Viết vào phần bình luận nhé.

<short pause> Video tới sẽ đổi hướng: Kaku cầm kính lúp lên, điều tra một bí ẩn khác chưa có lời giải, Lục địa Đen trong Hunter x Hunter.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cuộn giấy lại đây. Tám trăm năm, gói gọn trong mười lăm phút. Hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi tổng kết, Kaku chấm độ chắc chắn của từng mốc, để bạn biết đâu là nền móng vững, đâu là cát lún.

[pause] Màu xanh, chắc chắn: việc thành lập Chính phủ Thế giới tám trăm năm trước, lệnh cấm nghiên cứu, cuộc tấn công Ohara, và buổi hành quyết Vua Hải Tặc. Truyện nói rõ nhiều lần.

[pause] Màu vàng, đã xác nhận nhưng còn thiếu chi tiết: Vương quốc Vĩ đại, Joy Boy, nước biển dâng hai trăm mét, và sự kiện Thung lũng Thần. Ta biết chúng có thật, nhưng chưa biết đầy đủ.

[pause] Màu đỏ, gần như chưa biết: tư tưởng của Vương quốc Vĩ đại, nội dung đầy đủ của Laugh Tale, và danh tính thật của người ngồi trên ngai trống.

[pause] [chuckles] Kaku ghi chú: thú vị là những câu hỏi lớn nhất đều nằm ở màu đỏ. One Piece giữ những bí mật quan trọng nhất cho tới cuối cùng.

[pause] Tổng kết cả cuộn giấy. Hơn chín trăm năm trước: một nền văn minh có công nghệ vượt xa hiện tại.

[pause] Chín trăm tới tám trăm năm trước: Thế kỷ trống, Vương quốc Vĩ đại, Joy Boy và các poneglyph. Tám trăm năm trước: hai mươi vị vua thắng, lập Chính phủ Thế giới, và biển dâng khoảng hai trăm mét.

[pause] Ba mươi tám năm trước: Thung lũng Thần. Hai mươi lăm năm trước: Laugh Tale. Hai mươi bốn năm trước: Vua Hải Tặc bị hành quyết. Hai mươi hai năm trước: Ohara.

[pause] Và hiện tại: thông điệp từ Egghead, và một con tàu đang tiến dần tới hòn đảo cuối cùng.

[pause] [curious] Câu hỏi cho bạn: nếu được đọc một poneglyph duy nhất, bạn muốn nó kể về điều gì? Viết vào phần bình luận nhé.

[pause] Video tới sẽ đổi hướng: Kaku cầm kính lúp lên, điều tra một bí ẩn khác chưa có lời giải, Lục địa Đen trong Hunter x Hunter.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cuộn giấy lại đây. Tám trăm năm, gói gọn trong mười lăm phút. Hẹn gặp lại!
```
