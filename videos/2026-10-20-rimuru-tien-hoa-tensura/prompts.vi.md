# Bộ prompt · Tensura: Bậc thang tiến hóa của Rimuru — từ slime tới Ma vương

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 81 ảnh, 8 đoạn đọc, khoảng 15.5 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (81 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Tensura, Chuyển sinh thành slime, tới hết anime mùa hai, và nhắc ngắn bối cảnh các…

```text
Wide 16:9 landscape cinematic frame. a damp glowing cave with crystals on the walls, a closed notebook resting on a rock, wide establishing shot, soft blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Nấc thang đầu tiên: một khối thạch nhỏ màu xanh nằm trong hang tối. Không có mắt, không có tay chân, không có…

```text
Wide 16:9 landscape cinematic frame. a small translucent blue gelatinous blob sitting alone on a cave floor lit by glowing crystals, close-up, soft magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nấc thang cuối cùng, tính tới mùa hai: một Ma vương đứng ngang hàng với những sinh vật mạnh nhất thế giới, ca…

```text
Wide 16:9 landscape cinematic frame. a calm figure standing on a balcony overlooking a thriving city of monsters and humans at dusk, a faint dark aura around them, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Giữa hai nấc đó là cả một bậc thang. Mỗi bậc có điều kiện để bước lên, có sức mạnh nhận được, và có cái giá p…

```text
Wide 16:9 landscape cinematic frame. a spiral staircase rising out of a cave toward a starry sky, each step glowing a different color, low-angle wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Tensura bắt đầu là một tiểu thuyết đăng trên mạng của tác giả Fuse, rồi thành light novel, manga và anime từ…

```text
Wide 16:9 landscape cinematic frame. a light novel volume, a manga volume and a tablet showing an anime still arranged on a desk, close-up, cozy warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Và năm 2026, mùa bốn đã lên sóng với một kế hoạch rất dài. Đây là lúc tốt để nhìn lại con đường Rimuru đã đi.

```text
Wide 16:9 landscape cinematic frame. a long winding road drawn on a map from a cave to a castle, with a small marker at the far end, parchment style, amber ink. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku leo bậc thang tiến hóa của Rimuru Tempest, từ slime tới Ma vương, từ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at the bottom of a glowing staircase holding a tiny blue blob in its wings, cheerful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Nấc 0: một người đàn ông ba mươi bảy tuổi

Lời: Trước khi là slime, Rimuru là Mikami Satoru, một nhân viên văn phòng ba mươi bảy tuổi ở Tokyo. Một buổi tối,…

```text
Wide 16:9 landscape cinematic frame. a businessman silhouette lying on a rainy Tokyo sidewalk under neon signs, umbrella fallen beside him, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Trong những giây cuối, anh nghĩ vẩn vơ: giá mà mình có thể phân tích mọi thứ, giá mà mình không phải chịu đau…

```text
Wide 16:9 landscape cinematic frame. faint glowing thought fragments floating up from a fallen figure into the rainy night sky, close-up, melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Mỗi khi có kỹ năng mới, một giọng nói vang lên thông báo, gọi là Tiếng nói Thế giới. Nó giống như hệ thống th…

```text
Wide 16:9 landscape cinematic frame. a glowing translucent notification panel appearing in the air above a cave floor, close-up, soft cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Kaku thấy chi tiết này rất hợp với dòng isekai: thế giới mới vận hành như một trò chơi có luật rõ ràng, và ng…

```text
Wide 16:9 landscape cinematic frame. a rulebook floating open in the air above a fantasy landscape, pages glowing, wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Và trong thế giới mới, những suy nghĩ đó trở thành kỹ năng. Đây là luật đầu tiên của Tensura: mong muốn lúc l…

```text
Wide 16:9 landscape cinematic frame. glowing thought fragments transforming into small shining skill icons as they drift into another world's sky, wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu luật này áp dụng cho Kaku, chắc Kaku sẽ chuyển sinh thành một cuốn từ điển biết bay.

```text
Wide 16:9 landscape cinematic frame. the owl mascot imagining itself as a small flying dictionary with wings, thought bubble above its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Nấc 1: slime với hai kỹ năng

Lời: Nấc đầu tiên. Điều kiện: chết và chuyển sinh. Sức mạnh: hai kỹ năng đặc biệt. Cái giá: một cơ thể yếu ớt, khô…

```text
Wide 16:9 landscape cinematic frame. a small blue slime bumping clumsily into a cave wall, tiny sparkles around it, humorous close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Kỹ năng thứ nhất là Đại hiền giả: một giọng nói trong đầu có thể phân tích mọi thứ, tính toán, trả lời câu hỏ…

```text
Wide 16:9 landscape cinematic frame. a glowing geometric orb floating beside a small slime, projecting data diagrams into the air, close-up, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Đại hiền giả còn có tính cách riêng. Nó trả lời ngắn gọn, chính xác, đôi khi hơi lạnh lùng. Nhiều fan coi nó…

```text
Wide 16:9 landscape cinematic frame. a calm glowing orb projecting a single short answer line in the air beside a surprised slime, humorous close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Kỹ năng thứ hai là Kẻ săn mồi: slime có thể nuốt mọi thứ vào cơ thể, phân tích, lưu trữ, và sao chép khả năng…

```text
Wide 16:9 landscape cinematic frame. a small slime engulfing a glowing crystal whole, the crystal's pattern appearing on its surface, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Ngay trong hang, Rimuru nuốt những con quái vật đầu tiên: một con rắn, một con nhện, một con dơi. Mỗi con cho…

```text
Wide 16:9 landscape cinematic frame. three small cave creatures — a serpent, a spider and a bat — each dissolving into a small slime, three skill icons glowing above it, parchment storyboard style. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Thậm chí nuốt nước cũng thành kỹ năng: anh phun nước ra với áp lực cực mạnh, cắt được cả đá. Đòn tấn công đầu…

```text
Wide 16:9 landscape cinematic frame. a thin high-pressure jet of water slicing cleanly through a boulder in a cave, dynamic close-up, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Hai kỹ năng này hợp lại thành một cỗ máy tiến hóa: ăn một thứ gì đó, Đại hiền giả phân tích, rồi Rimuru có th…

```text
Wide 16:9 landscape cinematic frame. a circular diagram on parchment: an eating icon, an analysis icon and a new skill icon connected by arrows, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Trong hang, Rimuru gặp Veldora, con rồng Bão Tố bị phong ấn suốt ba trăm năm. Hai người trở thành bạn, và đặt…

```text
Wide 16:9 landscape cinematic frame. a colossal dragon silhouette trapped inside a glowing magical prison in a cave, a tiny slime sitting in front of it chatting, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Rồi Rimuru làm một việc táo bạo: nuốt luôn con rồng vào trong cơ thể, để phân tích phong ấn từ bên trong và g…

```text
Wide 16:9 landscape cinematic frame. a tiny slime swallowing a huge swirling vortex of dragon-shaped energy, dramatic close-up, cyan and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Kaku phải thừa nhận: đây là tình bạn kỳ lạ nhất trong anime. Nhưng từ đây, trong người Rimuru chứa một nguồn…

```text
Wide 16:9 landscape cinematic frame. a small slime glowing faintly from within with a coiled dragon silhouette visible inside, close-up, soft magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Nấc 2: sức mạnh của cái tên

Lời: Nấc thứ hai không đến từ việc ăn, mà từ việc cho đi. Trong thế giới này, đặt tên cho một quái vật sẽ khiến nó…

```text
Wide 16:9 landscape cinematic frame. a small slime placing a glowing name tag on a goblin's head, sparkles transforming the goblin, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Rimuru ra khỏi hang và gặp một làng yêu tinh nghèo khó. Anh đặt tên cho từng con. Yêu tinh tiến hóa thành yêu…

```text
Wide 16:9 landscape cinematic frame. a small poor goblin village being transformed as its inhabitants grow taller and stronger in a wave of light, wide shot, warm sunrise. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Già làng yêu tinh được đặt tên Rigurd, và từ một ông lão gầy yếu, ông trở thành một người đàn ông cơ bắp, khỏ…

```text
Wide 16:9 landscape cinematic frame. a frail old goblin transforming into a tall muscular figure in a burst of light while villagers gasp, before-and-after composition, humorous warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Bầy sói từng tấn công làng cũng được đặt tên, và trở thành bầy sói Bão Tố trung thành, những con sói mang tên…

```text
Wide 16:9 landscape cinematic frame. a pack of large dark wolves bowing their heads before a small slime, faint storm energy crackling around them, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Con sói đầu đàn được đặt tên Ranga. Từ kẻ thù, nó trở thành người bạn trung thành nhất, và thích được Rimuru…

```text
Wide 16:9 landscape cinematic frame. a huge dark wolf happily wagging its tail as a small figure pats its head, humorous medium shot, soft sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Trong thế giới Tensura, quái vật có tên được gọi là quái vật mang tên, và chúng mạnh hơn hẳn đồng loại. Đó là…

```text
Wide 16:9 landscape cinematic frame. a small glowing name tag resting on a velvet cushion like a precious jewel, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Điều kiện của nấc này: có người để đặt tên, và đủ năng lượng ma thuật. Sức mạnh nhận được: cả một cộng đồng t…

```text
Wide 16:9 landscape cinematic frame. a notebook page listing names with small monster doodles beside each, one after another, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Cái giá: đặt tên tiêu tốn năng lượng ma thuật của người đặt. Đặt quá nhiều tên một lúc, Rimuru kiệt sức tới m…

```text
Wide 16:9 landscape cinematic frame. a small slime flattened and sleeping on a bed of leaves with tiny zzz marks, humorous close-up, soft moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là nấc đẹp nhất của bậc thang: sức mạnh của Rimuru tăng lên không phải vì anh lấy đi của người…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing names on small cards and handing them to a line of tiny creatures. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Nấc 3: hình dạng con người

Lời: Nấc thứ ba đến từ một cuộc gặp buồn. Rimuru gặp Shizu, một người phụ nữ cũng đến từ Nhật Bản, bị triệu hồi sa…

```text
Wide 16:9 landscape cinematic frame. a woman in a traveler's cloak and a mask resting on her hat, sitting by a campfire at night, a small slime beside her, medium shot, warm firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trong người Shizu có một tinh linh lửa, Ifrit, bị gắn vào cô từ khi còn nhỏ. Nó mất kiểm soát và gây nguy hiể…

```text
Wide 16:9 landscape cinematic frame. a roaring fire spirit silhouette bursting out of a cloaked woman, a small slime leaping toward it, dramatic wide shot, orange flames. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Trước khi mất, Shizu nhờ Rimuru nuốt mình vào cơ thể, để cô được yên nghỉ trong một người đồng hương. Rimuru…

```text
Wide 16:9 landscape cinematic frame. a small slime gently glowing beside a fading figure lying on flowers under a starry sky, close-up, soft melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Sức mạnh nhận được: hình dạng con người, dựa trên dáng vẻ của Shizu thời trẻ, cùng khả năng sử dụng lửa. Từ đ…

```text
Wide 16:9 landscape cinematic frame. a young androgynous figure in a simple traveler's cloak standing in a meadow, looking at their own hands for the first time, medium shot, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Lời hứa đó dẫn Rimuru tới năm đứa trẻ bị triệu hồi, những học trò cuối cùng của Shizu. Anh trở thành thầy giá…

```text
Wide 16:9 landscape cinematic frame. a young teacher figure standing in front of five small children in a sunny classroom, back view, warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Cái giá: một ký ức và một nỗi buồn mà Rimuru mang theo mãi. Và một lời hứa với Shizu về những đứa trẻ bị triệ…

```text
Wide 16:9 landscape cinematic frame. a folded mask lying on a small stone memorial in a quiet meadow, extreme close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kaku ghi chú: đây là nấc đầu tiên mà sức mạnh gắn liền với tình cảm. Rimuru không chỉ học được một hình dạng,…

```text
Wide 16:9 landscape cinematic frame. a glowing thread connecting a small slime to a faint figure in the stars, parchment illustration, amber ink. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Nấc 4: vua của một quốc gia

Lời: Kaku nghĩ nhiều người xem Tensura vì nấc này hơn cả các trận đánh: xem một thị trấn nhỏ lớn dần thành thành p…

```text
Wide 16:9 landscape cinematic frame. a cozy hot spring bathhouse steaming in a forest town at dusk, lanterns glowing, monsters relaxing, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nấc thứ tư không phải tiến hóa của cơ thể, mà là tiến hóa của vị trí. Rimuru lập ra một quốc gia của quái vật…

```text
Wide 16:9 landscape cinematic frame. a thriving forest city with wooden houses, markets and roads full of goblins, wolves and ogres working together, wide aerial shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Anh đặt tên cho những con quỷ cao lớn, và họ tiến hóa thành các kijin, những chiến binh mạnh mẽ: một người đi…

```text
Wide 16:9 landscape cinematic frame. four imposing warrior silhouettes standing in a row behind a smaller figure: one with dark flames, one holding a huge sword, one masked in shadow, one elderly with a katana, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Rimuru còn tới vương quốc của người lùn, gặp vua Gazel, và mở đường cho liên minh đầu tiên giữa quốc gia quái…

```text
Wide 16:9 landscape cinematic frame. a grand underground dwarven city carved into a mountain with glowing forges, a small visitor standing at the gate, wide shot, warm firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và có những nhân vật hài hước như Gabiru, chàng thằn lằn tự tin quá mức, người luôn chen vào những lúc không…

```text
Wide 16:9 landscape cinematic frame. a flamboyant lizard warrior striking a dramatic pose on a rock while others sigh in the background, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Anh còn nuốt cả Chúa tể Orc, và đưa đội quân orc đói khát về với đất nước của mình. Sức mạnh của Kẻ săn mồi d…

```text
Wide 16:9 landscape cinematic frame. a massive orc army kneeling in a muddy field under clearing skies, a small figure standing before them, wide shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Điều kiện của nấc này: niềm tin của những người đi theo. Sức mạnh: một quốc gia, quân đội, thương mại, liên m…

```text
Wide 16:9 landscape cinematic frame. a map on parchment with a small nation in a forest connected by trade routes to neighboring kingdoms, amber ink. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: ở nấc này, Rimuru không còn mạnh lên một mình. Mỗi người trong quốc gia mạnh lên thì quốc gia m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a web of connected small figures around a central slime, looking impressed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Cái giá: trách nhiệm. Mỗi quyết định của Rimuru giờ ảnh hưởng tới hàng nghìn người. Và một quốc gia quái vật…

```text
Wide 16:9 landscape cinematic frame. a figure sitting alone at a desk late at night with piles of documents and a map, a single candle burning, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Nấc 5: Chân Ma vương

Lời: Và rồi đến nấc đau đớn nhất. Khi Rimuru đi vắng, vương quốc loài người Falmuth tấn công Tempest. Nhiều người…

```text
Wide 16:9 landscape cinematic frame. a burning forest city at night seen from a hill, a lone figure standing frozen at the edge, wide shot, red and cold contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Truyện nói rõ đây không chỉ là nghi lễ sức mạnh. Để có cơ hội hồi sinh những người đã mất, Rimuru phải trở th…

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand running out placed beside a sleeping figure on a stone bed, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Để hồi sinh họ, Rimuru cần tiến hóa thành Chân Ma vương. Và điều kiện để tiến hóa là thu hoạch một vạn linh h…

```text
Wide 16:9 landscape cinematic frame. a stark diagram on parchment with a single number ten thousand written beside a small crown icon, crimson ink, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Rimuru đưa ra một quyết định mà không mùa nào trong anime nặng nề bằng: anh một mình đối đầu với toàn bộ quân…

```text
Wide 16:9 landscape cinematic frame. a small figure standing alone on a hill facing a vast army camp under a dark stormy sky, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Quá trình tiến hóa diễn ra trong lúc Rimuru ngủ, và những người được Rimuru đặt tên cũng nhận được một phần s…

```text
Wide 16:9 landscape cinematic frame. a whole city of monsters glowing softly at night as a wave of light spreads outward from a central palace, wide aerial shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Sức mạnh nhận được là khổng lồ. Cơ thể tiến hóa thành Ma slime. Đại hiền giả tiến hóa thành Trí tuệ vương Rap…

```text
Wide 16:9 landscape cinematic frame. a glowing geometric orb transforming into a larger radiant crystal form, a dark swirling aura expanding around a figure, dramatic close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Và với sức mạnh mới, Rimuru hồi sinh được Shion cùng những người đã mất. Mục đích của nấc thang này đạt được.

```text
Wide 16:9 landscape cinematic frame. a woman opening her eyes surrounded by friends crying with joy in a sunlit room, medium shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Sau nấc này, Rimuru cũng hiểu rằng con đường chung sống giữa quái vật và con người sẽ không hề dễ dàng. Giấc…

```text
Wide 16:9 landscape cinematic frame. a beautiful painted mural of monsters and humans holding hands, a fine crack running through its center, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Nhưng cái giá là lớn nhất từ trước tới nay: Rimuru đã giết rất nhiều người để có được nó. Truyện không né trá…

```text
Wide 16:9 landscape cinematic frame. a figure sitting alone on the edge of a cliff at dawn, looking at their own hands, wide shot, grey-gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là nấc duy nhất mà sức mạnh đến từ việc lấy đi mạng sống. Và Kaku nghĩ tác giả cố ý đặt nó…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quietly closing a dark page of the notebook with a serious expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Nấc 6: Ma vương được công nhận

Lời: Tiến hóa xong vẫn chưa đủ. Trong thế giới này, có một nhóm Ma vương mạnh nhất, và muốn được gọi là Ma vương,…

```text
Wide 16:9 landscape cinematic frame. a grand dark banquet hall with a long table and several empty ornate thrones, candles flickering, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Ở Walpurgis có Milim, Ma vương mạnh nhất, trông như một cô bé hiếu động nhưng có sức hủy diệt khủng khiếp. Cô…

```text
Wide 16:9 landscape cinematic frame. a small energetic girl silhouette sitting on a giant throne swinging her legs, a crater visible out the window behind her, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Tại buổi yến tiệc Walpurgis, Rimuru đối đầu với Ma vương Clayman, kẻ đứng sau nhiều âm mưu nhắm vào Tempest,…

```text
Wide 16:9 landscape cinematic frame. two figures facing each other across a long banquet table while other powerful silhouettes watch from their thrones, tense wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Tám Ma vương sau đó được gọi chung bằng một cái tên mới, và theo truyện, cái tên đó do chính Rimuru đề xuất.…

```text
Wide 16:9 landscape cinematic frame. eight crowns arranged in a circle on a dark table with a small name tag placed in the center, close-up, dramatic candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Rimuru trở thành một trong tám Ma vương, và được gọi là Ma vương mới. Đồng thời, anh cuối cùng cũng giải phón…

```text
Wide 16:9 landscape cinematic frame. a colossal dragon bursting free from a small figure into the sky, joyful storm clouds swirling, wide shot, bright dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Từ nấc này trở đi, các mùa sau của anime xoay quanh chính trị, ngoại giao và những cuộc đối đầu với các thế l…

```text
Wide 16:9 landscape cinematic frame. a long diplomatic table with flags of many nations and a small monster nation's flag among them, medium shot, formal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Điều kiện: chiến thắng và uy tín. Sức mạnh: vị thế ngang hàng với những sinh vật mạnh nhất. Cái giá: giờ Rimu…

```text
Wide 16:9 landscape cinematic frame. a map of the world with eight crown icons, one of them newly placed and surrounded by small arrows from all directions, parchment style. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Quy luật của bậc thang

Lời: Nhìn lại cả bậc thang, Kaku thấy một quy luật. Sức mạnh của Rimuru đến từ hai hướng: ăn vào và cho đi.

```text
Wide 16:9 landscape cinematic frame. a diagram with two arrows: one pointing inward labeled with a mouth icon, one pointing outward labeled with a name tag icon, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý rằng Rimuru chưa bao giờ ăn ai chỉ để mạnh lên. Mỗi lần nuốt đều có lý do: cứu một người bạn, giữ m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot checking items off a list titled with a small heart icon beside each swallowed thing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Ăn vào là Kẻ săn mồi: nuốt rồng, nuốt Shizu, nuốt Chúa tể Orc. Mỗi lần ăn là một lần học.

```text
Wide 16:9 landscape cinematic frame. three small icons in a row: a dragon, a mask and an orc head, each flowing into a small slime, parchment illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Kaku thấy đây là thiết kế rất tinh tế: một hệ thống sức mạnh có cả hai chiều. Nếu chỉ có ăn vào, Rimuru sẽ là…

```text
Wide 16:9 landscape cinematic frame. a balanced scale with a small mouth icon on one side and a name tag icon on the other, parchment illustration, amber light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Cho đi là đặt tên: yêu tinh, sói, kijin, và cả một quốc gia. Mỗi cái tên là một phần năng lượng của Rimuru ch…

```text
Wide 16:9 landscape cinematic frame. many small glowing name tags floating outward from a central figure to a crowd of creatures, then small hearts flowing back, parchment illustration. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và nấc Chân Ma vương là nơi hai hướng này va chạm: Rimuru phải lấy đi một thứ rất lớn để trả lại những người…

```text
Wide 16:9 landscape cinematic frame. two arrows colliding in the center of the diagram with a crack of crimson light, close-up, dramatic amber and crimson. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Toàn bộ bậc thang

Lời: Kaku vẽ lại toàn bộ bậc thang. Nấc không: một người đàn ông chết trong mưa. Nấc một: slime với hai kỹ năng, v…

```text
Wide 16:9 landscape cinematic frame. the bottom steps of the glowing staircase: a rainy street and a small cave slime with a dragon shadow, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nấc hai: sức mạnh của cái tên. Nấc ba: hình người và lời hứa với Shizu. Nấc bốn: vua của một quốc gia.

```text
Wide 16:9 landscape cinematic frame. the middle steps: name tags, a mask on a memorial, a forest city, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nhìn từ xa, bậc thang này đi lên đều đặn, nhưng không đều về màu sắc: những nấc đầu sáng và ấm, nấc năm tối h…

```text
Wide 16:9 landscape cinematic frame. the full glowing staircase seen from a distance, one step noticeably darker than the rest, wide shot, dramatic contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nấc năm: Chân Ma vương, với cái giá nặng nhất. Nấc sáu: được công nhận, và giải phóng người bạn đầu tiên.

```text
Wide 16:9 landscape cinematic frame. the top steps: a dark crown and a dragon flying free into a bright sky, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Và nếu bước lên, bạn sẽ đặt tên cho ai đầu tiên? Kaku thì chắc sẽ đặt tên cho chiếc bàn học, để nó tự dọn dẹp.

```text
Wide 16:9 landscape cinematic frame. a messy desk with a small glowing name tag placed on it, books starting to rearrange themselves, humorous close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nếu bạn là Rimuru, bạn có bước lên nấc thứ năm không? Đây là câu hỏi Kaku nghĩ mãi mà chưa có câu trả lời. Vi…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing at the foot of a dark glowing step, one foot raised, hesitating, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Kết

Lời: Và có lẽ đó là lý do người xem yêu Rimuru: anh mạnh lên rất nhanh, nhưng chưa bao giờ quên mình từng là một n…

```text
Wide 16:9 landscape cinematic frame. a small slime sitting on an office desk beside a framed photo of a rainy Tokyo street, gentle nostalgic light, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Từ một khối thạch trong hang tới một Ma vương, bậc thang của Rimuru là câu chuyện về việc sức mạnh có thể đến…

```text
Wide 16:9 landscape cinematic frame. a small blue slime sitting peacefully on a hill overlooking a bright city at sunset, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Video tiếp theo, Kaku vẽ một cây phả hệ đặc biệt: chín người đã lần lượt nắm giữ One For All trong My Hero Ac…

```text
Wide 16:9 landscape cinematic frame. a tree of glowing silhouettes passing a single light from hand to hand across generations, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những bậc thang tiến hóa như thế này, hãy đăng ký kênh để leo thêm nhiều bậc thang nữa cùng Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving from the top of the glowing staircase with a tiny slime on its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nấc 0: một người đàn ông ba mươi bảy tuổi

Khoảng 142 giây · cảnh s01–s13 · 1842 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Tensura, Chuyển sinh thành slime, tới hết anime mùa hai, và nhắc ngắn bối cảnh các mùa sau. Không có spoiler phần tiểu thuyết chưa chiếu.

<short pause> Nấc thang đầu tiên: một khối thạch nhỏ màu xanh nằm trong hang tối. Không có mắt, không có tay chân, không có gì ngoài hai kỹ năng lạ.

<short pause> Nấc thang cuối cùng, tính tới mùa hai: một Ma vương đứng ngang hàng với những sinh vật mạnh nhất thế giới, cai trị cả một quốc gia của quái vật.

<short pause> Giữa hai nấc đó là cả một bậc thang. Mỗi bậc có điều kiện để bước lên, có sức mạnh nhận được, và có cái giá phải trả.

<short pause> Tensura bắt đầu là một tiểu thuyết đăng trên mạng của tác giả Fuse, rồi thành light novel, manga và anime từ năm 2018. Ở Việt Nam, nhiều người biết bộ này qua cái tên Chuyển sinh thành slime.

<short pause> Và năm 2026, mùa bốn đã lên sóng với một kế hoạch rất dài. Đây là lúc tốt để nhìn lại con đường Rimuru đã đi.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku leo bậc thang tiến hóa của Rimuru Tempest, từ slime tới Ma vương, từng nấc một.

<short pause> Trước khi là slime, Rimuru là Mikami Satoru, một nhân viên văn phòng ba mươi bảy tuổi ở Tokyo. Một buổi tối, anh bị đâm khi đang bảo vệ đồng nghiệp.

<short pause> Trong những giây cuối, anh nghĩ vẩn vơ: giá mà mình có thể phân tích mọi thứ, giá mà mình không phải chịu đau, giá mà mình có thể ăn được mọi thứ.

<short pause> Mỗi khi có kỹ năng mới, một giọng nói vang lên thông báo, gọi là Tiếng nói Thế giới. Nó giống như hệ thống thông báo của một trò chơi, nhưng là luật của cả thế giới.

<short pause> Kaku thấy chi tiết này rất hợp với dòng isekai: thế giới mới vận hành như một trò chơi có luật rõ ràng, và người chuyển sinh đọc được luật đó.

<short pause> Và trong thế giới mới, những suy nghĩ đó trở thành kỹ năng. Đây là luật đầu tiên của Tensura: mong muốn lúc lâm chung có thể định hình năng lực khi chuyển sinh.

<short pause> Kaku ghi chú: nếu luật này áp dụng cho Kaku, chắc Kaku sẽ chuyển sinh thành một cuốn từ điển biết bay.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Tensura, Chuyển sinh thành slime, tới hết anime mùa hai, và nhắc ngắn bối cảnh các mùa sau. Không có spoiler phần tiểu thuyết chưa chiếu.

[pause] Nấc thang đầu tiên: một khối thạch nhỏ màu xanh nằm trong hang tối. Không có mắt, không có tay chân, không có gì ngoài hai kỹ năng lạ.

[pause] Nấc thang cuối cùng, tính tới mùa hai: một Ma vương đứng ngang hàng với những sinh vật mạnh nhất thế giới, cai trị cả một quốc gia của quái vật.

[pause] Giữa hai nấc đó là cả một bậc thang. Mỗi bậc có điều kiện để bước lên, có sức mạnh nhận được, và có cái giá phải trả.

[pause] Tensura bắt đầu là một tiểu thuyết đăng trên mạng của tác giả Fuse, rồi thành light novel, manga và anime từ năm 2018. Ở Việt Nam, nhiều người biết bộ này qua cái tên Chuyển sinh thành slime.

[pause] Và năm 2026, mùa bốn đã lên sóng với một kế hoạch rất dài. Đây là lúc tốt để nhìn lại con đường Rimuru đã đi.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku leo bậc thang tiến hóa của Rimuru Tempest, từ slime tới Ma vương, từng nấc một.

[pause] Trước khi là slime, Rimuru là Mikami Satoru, một nhân viên văn phòng ba mươi bảy tuổi ở Tokyo. Một buổi tối, anh bị đâm khi đang bảo vệ đồng nghiệp.

[pause] Trong những giây cuối, anh nghĩ vẩn vơ: giá mà mình có thể phân tích mọi thứ, giá mà mình không phải chịu đau, giá mà mình có thể ăn được mọi thứ.

[pause] Mỗi khi có kỹ năng mới, một giọng nói vang lên thông báo, gọi là Tiếng nói Thế giới. Nó giống như hệ thống thông báo của một trò chơi, nhưng là luật của cả thế giới.

[pause] Kaku thấy chi tiết này rất hợp với dòng isekai: thế giới mới vận hành như một trò chơi có luật rõ ràng, và người chuyển sinh đọc được luật đó.

[pause] Và trong thế giới mới, những suy nghĩ đó trở thành kỹ năng. Đây là luật đầu tiên của Tensura: mong muốn lúc lâm chung có thể định hình năng lực khi chuyển sinh.

[pause] Kaku ghi chú: nếu luật này áp dụng cho Kaku, chắc Kaku sẽ chuyển sinh thành một cuốn từ điển biết bay.
```

### c02 · Nấc 1: slime với hai kỹ năng

Khoảng 118 giây · cảnh s14–s23 · 1528 ký tự

**Gemini**

```text
Nấc đầu tiên. Điều kiện: chết và chuyển sinh. Sức mạnh: hai kỹ năng đặc biệt. Cái giá: một cơ thể yếu ớt, không nhìn thấy gì lúc ban đầu.

<short pause> Kỹ năng thứ nhất là Đại hiền giả: một giọng nói trong đầu có thể phân tích mọi thứ, tính toán, trả lời câu hỏi. Nó giống như có một bộ não thứ hai cực kỳ thông minh.

<short pause> Đại hiền giả còn có tính cách riêng. Nó trả lời ngắn gọn, chính xác, đôi khi hơi lạnh lùng. Nhiều fan coi nó là nhân vật được yêu thích nhất bộ truyện dù nó chỉ là một giọng nói.

<short pause> Kỹ năng thứ hai là Kẻ săn mồi: slime có thể nuốt mọi thứ vào cơ thể, phân tích, lưu trữ, và sao chép khả năng của thứ bị nuốt.

<short pause> Ngay trong hang, Rimuru nuốt những con quái vật đầu tiên: một con rắn, một con nhện, một con dơi. Mỗi con cho anh một kỹ năng: phun độc, nhả tơ dính, phát sóng âm để nói chuyện.

<short pause> Thậm chí nuốt nước cũng thành kỹ năng: anh phun nước ra với áp lực cực mạnh, cắt được cả đá. Đòn tấn công đầu tiên của Rimuru là một lưỡi dao bằng nước.

<short pause> Hai kỹ năng này hợp lại thành một cỗ máy tiến hóa: ăn một thứ gì đó, Đại hiền giả phân tích, rồi Rimuru có thêm năng lực mới. Toàn bộ bậc thang phía sau đều dựa trên vòng lặp này.

<short pause> Trong hang, Rimuru gặp Veldora, con rồng Bão Tố bị phong ấn suốt ba trăm năm. Hai người trở thành bạn, và đặt tên họ cho nhau. Slime nhận họ Tempest.

<short pause> Rồi Rimuru làm một việc táo bạo: nuốt luôn con rồng vào trong cơ thể, để phân tích phong ấn từ bên trong và giải thoát bạn mình sau này.

<short pause> Kaku phải thừa nhận: đây là tình bạn kỳ lạ nhất trong anime. <short pause> Nhưng từ đây, trong người Rimuru chứa một nguồn năng lượng khổng lồ.
```

**ElevenLabs**

```text
Nấc đầu tiên. Điều kiện: chết và chuyển sinh. Sức mạnh: hai kỹ năng đặc biệt. Cái giá: một cơ thể yếu ớt, không nhìn thấy gì lúc ban đầu.

[pause] Kỹ năng thứ nhất là Đại hiền giả: một giọng nói trong đầu có thể phân tích mọi thứ, tính toán, trả lời câu hỏi. Nó giống như có một bộ não thứ hai cực kỳ thông minh.

[pause] Đại hiền giả còn có tính cách riêng. Nó trả lời ngắn gọn, chính xác, đôi khi hơi lạnh lùng. Nhiều fan coi nó là nhân vật được yêu thích nhất bộ truyện dù nó chỉ là một giọng nói.

[pause] Kỹ năng thứ hai là Kẻ săn mồi: slime có thể nuốt mọi thứ vào cơ thể, phân tích, lưu trữ, và sao chép khả năng của thứ bị nuốt.

[pause] Ngay trong hang, Rimuru nuốt những con quái vật đầu tiên: một con rắn, một con nhện, một con dơi. Mỗi con cho anh một kỹ năng: phun độc, nhả tơ dính, phát sóng âm để nói chuyện.

[pause] Thậm chí nuốt nước cũng thành kỹ năng: anh phun nước ra với áp lực cực mạnh, cắt được cả đá. Đòn tấn công đầu tiên của Rimuru là một lưỡi dao bằng nước.

[pause] Hai kỹ năng này hợp lại thành một cỗ máy tiến hóa: ăn một thứ gì đó, Đại hiền giả phân tích, rồi Rimuru có thêm năng lực mới. Toàn bộ bậc thang phía sau đều dựa trên vòng lặp này.

[pause] Trong hang, Rimuru gặp Veldora, con rồng Bão Tố bị phong ấn suốt ba trăm năm. Hai người trở thành bạn, và đặt tên họ cho nhau. Slime nhận họ Tempest.

[pause] Rồi Rimuru làm một việc táo bạo: nuốt luôn con rồng vào trong cơ thể, để phân tích phong ấn từ bên trong và giải thoát bạn mình sau này.

[pause] Kaku phải thừa nhận: đây là tình bạn kỳ lạ nhất trong anime. [pause] Nhưng từ đây, trong người Rimuru chứa một nguồn năng lượng khổng lồ.
```

### c03 · Nấc 2: sức mạnh của cái tên

Khoảng 101 giây · cảnh s24–s32 · 1317 ký tự

**Gemini**

```text
Nấc thứ hai không đến từ việc ăn, mà từ việc cho đi. Trong thế giới này, đặt tên cho một quái vật sẽ khiến nó tiến hóa.

<short pause> Rimuru ra khỏi hang và gặp một làng yêu tinh nghèo khó. Anh đặt tên cho từng con. Yêu tinh tiến hóa thành yêu tinh lớn hơn, khỏe hơn, thông minh hơn.

<short pause> Già làng yêu tinh được đặt tên Rigurd, và từ một ông lão gầy yếu, ông trở thành một người đàn ông cơ bắp, khỏe mạnh. Cả làng không nhận ra nhau sau một đêm.

<short pause> Bầy sói từng tấn công làng cũng được đặt tên, và trở thành bầy sói Bão Tố trung thành, những con sói mang tên của chính Veldora.

<short pause> Con sói đầu đàn được đặt tên Ranga. Từ kẻ thù, nó trở thành người bạn trung thành nhất, và thích được Rimuru xoa đầu như một chú chó lớn.

<short pause> Trong thế giới Tensura, quái vật có tên được gọi là quái vật mang tên, và chúng mạnh hơn hẳn đồng loại. Đó là lý do một cái tên là món quà quý nhất một chủ nhân có thể trao.

<short pause> Điều kiện của nấc này: có người để đặt tên, và đủ năng lượng ma thuật. Sức mạnh nhận được: cả một cộng đồng trung thành và mạnh lên.

<short pause> Cái giá: đặt tên tiêu tốn năng lượng ma thuật của người đặt. Đặt quá nhiều tên một lúc, Rimuru kiệt sức tới mức phải chuyển vào trạng thái ngủ để hồi phục.

<short pause> <laugh> Kaku thấy đây là nấc đẹp nhất của bậc thang: sức mạnh của Rimuru tăng lên không phải vì anh lấy đi của người khác, mà vì anh cho đi thứ đầu tiên anh có, là một cái tên.
```

**ElevenLabs**

```text
Nấc thứ hai không đến từ việc ăn, mà từ việc cho đi. Trong thế giới này, đặt tên cho một quái vật sẽ khiến nó tiến hóa.

[pause] Rimuru ra khỏi hang và gặp một làng yêu tinh nghèo khó. Anh đặt tên cho từng con. Yêu tinh tiến hóa thành yêu tinh lớn hơn, khỏe hơn, thông minh hơn.

[pause] Già làng yêu tinh được đặt tên Rigurd, và từ một ông lão gầy yếu, ông trở thành một người đàn ông cơ bắp, khỏe mạnh. Cả làng không nhận ra nhau sau một đêm.

[pause] Bầy sói từng tấn công làng cũng được đặt tên, và trở thành bầy sói Bão Tố trung thành, những con sói mang tên của chính Veldora.

[pause] Con sói đầu đàn được đặt tên Ranga. Từ kẻ thù, nó trở thành người bạn trung thành nhất, và thích được Rimuru xoa đầu như một chú chó lớn.

[pause] Trong thế giới Tensura, quái vật có tên được gọi là quái vật mang tên, và chúng mạnh hơn hẳn đồng loại. Đó là lý do một cái tên là món quà quý nhất một chủ nhân có thể trao.

[pause] Điều kiện của nấc này: có người để đặt tên, và đủ năng lượng ma thuật. Sức mạnh nhận được: cả một cộng đồng trung thành và mạnh lên.

[pause] Cái giá: đặt tên tiêu tốn năng lượng ma thuật của người đặt. Đặt quá nhiều tên một lúc, Rimuru kiệt sức tới mức phải chuyển vào trạng thái ngủ để hồi phục.

[pause] [chuckles] Kaku thấy đây là nấc đẹp nhất của bậc thang: sức mạnh của Rimuru tăng lên không phải vì anh lấy đi của người khác, mà vì anh cho đi thứ đầu tiên anh có, là một cái tên.
```

### c04 · Nấc 3: hình dạng con người

Khoảng 81 giây · cảnh s33–s39 · 1055 ký tự

**Gemini**

```text
Nấc thứ ba đến từ một cuộc gặp buồn. Rimuru gặp Shizu, một người phụ nữ cũng đến từ Nhật Bản, bị triệu hồi sang thế giới này từ khi còn nhỏ và mang trong mình một linh hồn lửa.

<short pause> Trong người Shizu có một tinh linh lửa, Ifrit, bị gắn vào cô từ khi còn nhỏ. Nó mất kiểm soát và gây nguy hiểm cho mọi người xung quanh. Rimuru nuốt luôn tinh linh đó.

<short pause> Trước khi mất, Shizu nhờ Rimuru nuốt mình vào cơ thể, để cô được yên nghỉ trong một người đồng hương. Rimuru nhận lấy lời nhờ đó.

<short pause> Sức mạnh nhận được: hình dạng con người, dựa trên dáng vẻ của Shizu thời trẻ, cùng khả năng sử dụng lửa. Từ đây Rimuru có thể nói, đi lại, và sống giữa con người.

<short pause> Lời hứa đó dẫn Rimuru tới năm đứa trẻ bị triệu hồi, những học trò cuối cùng của Shizu. Anh trở thành thầy giáo của chúng, và cứu chúng khỏi số phận của chính Shizu.

<short pause> Cái giá: một ký ức và một nỗi buồn mà Rimuru mang theo mãi. Và một lời hứa với Shizu về những đứa trẻ bị triệu hồi khác.

<short pause> Kaku ghi chú: đây là nấc đầu tiên mà sức mạnh gắn liền với tình cảm. Rimuru không chỉ học được một hình dạng, mà học được cả trách nhiệm.
```

**ElevenLabs**

```text
Nấc thứ ba đến từ một cuộc gặp buồn. Rimuru gặp Shizu, một người phụ nữ cũng đến từ Nhật Bản, bị triệu hồi sang thế giới này từ khi còn nhỏ và mang trong mình một linh hồn lửa.

[pause] Trong người Shizu có một tinh linh lửa, Ifrit, bị gắn vào cô từ khi còn nhỏ. Nó mất kiểm soát và gây nguy hiểm cho mọi người xung quanh. Rimuru nuốt luôn tinh linh đó.

[pause] Trước khi mất, Shizu nhờ Rimuru nuốt mình vào cơ thể, để cô được yên nghỉ trong một người đồng hương. Rimuru nhận lấy lời nhờ đó.

[pause] Sức mạnh nhận được: hình dạng con người, dựa trên dáng vẻ của Shizu thời trẻ, cùng khả năng sử dụng lửa. Từ đây Rimuru có thể nói, đi lại, và sống giữa con người.

[pause] Lời hứa đó dẫn Rimuru tới năm đứa trẻ bị triệu hồi, những học trò cuối cùng của Shizu. Anh trở thành thầy giáo của chúng, và cứu chúng khỏi số phận của chính Shizu.

[pause] Cái giá: một ký ức và một nỗi buồn mà Rimuru mang theo mãi. Và một lời hứa với Shizu về những đứa trẻ bị triệu hồi khác.

[pause] Kaku ghi chú: đây là nấc đầu tiên mà sức mạnh gắn liền với tình cảm. Rimuru không chỉ học được một hình dạng, mà học được cả trách nhiệm.
```

### c05 · Nấc 4: vua của một quốc gia

Khoảng 110 giây · cảnh s40–s48 · 1435 ký tự

**Gemini**

```text
Kaku nghĩ nhiều người xem Tensura vì nấc này hơn cả các trận đánh: xem một thị trấn nhỏ lớn dần thành thành phố, có đường xá, có nhà tắm suối nước nóng, có cả món ăn Nhật.

<short pause> Nấc thứ tư không phải tiến hóa của cơ thể, mà là tiến hóa của vị trí. Rimuru lập ra một quốc gia của quái vật: Liên bang Jura Tempest.

<short pause> Anh đặt tên cho những con quỷ cao lớn, và họ tiến hóa thành các kijin, những chiến binh mạnh mẽ: một người điều khiển lửa đen, một nữ thư ký khỏe khủng khiếp, một ninja im lặng, một kiếm sĩ già.

<short pause> Rimuru còn tới vương quốc của người lùn, gặp vua Gazel, và mở đường cho liên minh đầu tiên giữa quốc gia quái vật và một vương quốc của các chủng tộc khác.

<short pause> Và có những nhân vật hài hước như Gabiru, chàng thằn lằn tự tin quá mức, người luôn chen vào những lúc không ai mời. Tensura luôn cân bằng những trận chiến lớn bằng những khoảnh khắc buồn cười.

<short pause> Anh còn nuốt cả Chúa tể Orc, và đưa đội quân orc đói khát về với đất nước của mình. Sức mạnh của Kẻ săn mồi dùng để kết thúc một thảm họa, không phải để tàn sát.

<short pause> Điều kiện của nấc này: niềm tin của những người đi theo. Sức mạnh: một quốc gia, quân đội, thương mại, liên minh với các nước láng giềng.

<short pause> <laugh> Kaku ghi chú: ở nấc này, Rimuru không còn mạnh lên một mình. Mỗi người trong quốc gia mạnh lên thì quốc gia mạnh lên, và Rimuru cũng mạnh lên theo.

<short pause> Cái giá: trách nhiệm. Mỗi quyết định của Rimuru giờ ảnh hưởng tới hàng nghìn người. Và một quốc gia quái vật lớn mạnh sẽ khiến con người lo sợ.
```

**ElevenLabs**

```text
Kaku nghĩ nhiều người xem Tensura vì nấc này hơn cả các trận đánh: xem một thị trấn nhỏ lớn dần thành thành phố, có đường xá, có nhà tắm suối nước nóng, có cả món ăn Nhật.

[pause] Nấc thứ tư không phải tiến hóa của cơ thể, mà là tiến hóa của vị trí. Rimuru lập ra một quốc gia của quái vật: Liên bang Jura Tempest.

[pause] Anh đặt tên cho những con quỷ cao lớn, và họ tiến hóa thành các kijin, những chiến binh mạnh mẽ: một người điều khiển lửa đen, một nữ thư ký khỏe khủng khiếp, một ninja im lặng, một kiếm sĩ già.

[pause] Rimuru còn tới vương quốc của người lùn, gặp vua Gazel, và mở đường cho liên minh đầu tiên giữa quốc gia quái vật và một vương quốc của các chủng tộc khác.

[pause] Và có những nhân vật hài hước như Gabiru, chàng thằn lằn tự tin quá mức, người luôn chen vào những lúc không ai mời. Tensura luôn cân bằng những trận chiến lớn bằng những khoảnh khắc buồn cười.

[pause] Anh còn nuốt cả Chúa tể Orc, và đưa đội quân orc đói khát về với đất nước của mình. Sức mạnh của Kẻ săn mồi dùng để kết thúc một thảm họa, không phải để tàn sát.

[pause] Điều kiện của nấc này: niềm tin của những người đi theo. Sức mạnh: một quốc gia, quân đội, thương mại, liên minh với các nước láng giềng.

[pause] [chuckles] Kaku ghi chú: ở nấc này, Rimuru không còn mạnh lên một mình. Mỗi người trong quốc gia mạnh lên thì quốc gia mạnh lên, và Rimuru cũng mạnh lên theo.

[pause] Cái giá: trách nhiệm. Mỗi quyết định của Rimuru giờ ảnh hưởng tới hàng nghìn người. Và một quốc gia quái vật lớn mạnh sẽ khiến con người lo sợ.
```

### c06 · Nấc 5: Chân Ma vương

Khoảng 122 giây · cảnh s49–s58 · 1589 ký tự

**Gemini**

```text
Và rồi đến nấc đau đớn nhất. Khi Rimuru đi vắng, vương quốc loài người Falmuth tấn công Tempest. Nhiều người dân chết, trong đó có Shion, nữ thư ký trung thành.

<short pause> Truyện nói rõ đây không chỉ là nghi lễ sức mạnh. Để có cơ hội hồi sinh những người đã mất, Rimuru phải trở thành một thứ vượt trên giới hạn cũ của mình, và phải làm điều đó thật nhanh.

<short pause> Để hồi sinh họ, Rimuru cần tiến hóa thành Chân Ma vương. Và điều kiện để tiến hóa là thu hoạch một vạn linh hồn người.

<short pause> Rimuru đưa ra một quyết định mà không mùa nào trong anime nặng nề bằng: anh một mình đối đầu với toàn bộ quân đội xâm lược. Kaku sẽ không mô tả chi tiết cảnh đó.

<short pause> Quá trình tiến hóa diễn ra trong lúc Rimuru ngủ, và những người được Rimuru đặt tên cũng nhận được một phần sức mạnh, gọi là món quà. Cả quốc gia cùng tiến hóa theo vị vua của mình.

<short pause> Sức mạnh nhận được là khổng lồ. Cơ thể tiến hóa thành Ma slime. Đại hiền giả tiến hóa thành Trí tuệ vương Raphael, còn Kẻ săn mồi thành Bạo thực chi vương.

<short pause> Và với sức mạnh mới, Rimuru hồi sinh được Shion cùng những người đã mất. Mục đích của nấc thang này đạt được.

<short pause> Sau nấc này, Rimuru cũng hiểu rằng con đường chung sống giữa quái vật và con người sẽ không hề dễ dàng. Giấc mơ của anh giờ có thêm một vết nứt không thể xóa.

<short pause> Nhưng cái giá là lớn nhất từ trước tới nay: Rimuru đã giết rất nhiều người để có được nó. Truyện không né tránh điều đó, và chính Rimuru cũng không quên.

<short pause> <laugh> Kaku ghi chú: đây là nấc duy nhất mà sức mạnh đến từ việc lấy đi mạng sống. Và Kaku nghĩ tác giả cố ý đặt nó ngay sau những nấc đẹp nhất, để ta thấy một người tốt có thể đi tới đâu khi mất đi người mình thương.
```

**ElevenLabs**

```text
Và rồi đến nấc đau đớn nhất. Khi Rimuru đi vắng, vương quốc loài người Falmuth tấn công Tempest. Nhiều người dân chết, trong đó có Shion, nữ thư ký trung thành.

[pause] Truyện nói rõ đây không chỉ là nghi lễ sức mạnh. Để có cơ hội hồi sinh những người đã mất, Rimuru phải trở thành một thứ vượt trên giới hạn cũ của mình, và phải làm điều đó thật nhanh.

[pause] Để hồi sinh họ, Rimuru cần tiến hóa thành Chân Ma vương. Và điều kiện để tiến hóa là thu hoạch một vạn linh hồn người.

[pause] Rimuru đưa ra một quyết định mà không mùa nào trong anime nặng nề bằng: anh một mình đối đầu với toàn bộ quân đội xâm lược. Kaku sẽ không mô tả chi tiết cảnh đó.

[pause] Quá trình tiến hóa diễn ra trong lúc Rimuru ngủ, và những người được Rimuru đặt tên cũng nhận được một phần sức mạnh, gọi là món quà. Cả quốc gia cùng tiến hóa theo vị vua của mình.

[pause] Sức mạnh nhận được là khổng lồ. Cơ thể tiến hóa thành Ma slime. Đại hiền giả tiến hóa thành Trí tuệ vương Raphael, còn Kẻ săn mồi thành Bạo thực chi vương.

[pause] Và với sức mạnh mới, Rimuru hồi sinh được Shion cùng những người đã mất. Mục đích của nấc thang này đạt được.

[pause] Sau nấc này, Rimuru cũng hiểu rằng con đường chung sống giữa quái vật và con người sẽ không hề dễ dàng. Giấc mơ của anh giờ có thêm một vết nứt không thể xóa.

[pause] Nhưng cái giá là lớn nhất từ trước tới nay: Rimuru đã giết rất nhiều người để có được nó. Truyện không né tránh điều đó, và chính Rimuru cũng không quên.

[pause] [chuckles] Kaku ghi chú: đây là nấc duy nhất mà sức mạnh đến từ việc lấy đi mạng sống. Và Kaku nghĩ tác giả cố ý đặt nó ngay sau những nấc đẹp nhất, để ta thấy một người tốt có thể đi tới đâu khi mất đi người mình thương.
```

### c07 · Nấc 6: Ma vương được công nhận / Quy luật của bậc thang

Khoảng 147 giây · cảnh s59–s71 · 1915 ký tự

**Gemini**

```text
Tiến hóa xong vẫn chưa đủ. Trong thế giới này, có một nhóm Ma vương mạnh nhất, và muốn được gọi là Ma vương, Rimuru phải được họ công nhận.

<short pause> Ở Walpurgis có Milim, Ma vương mạnh nhất, trông như một cô bé hiếu động nhưng có sức hủy diệt khủng khiếp. Cô coi Rimuru là bạn thân, một tình bạn mà cả thế giới phải dè chừng.

<short pause> Tại buổi yến tiệc Walpurgis, Rimuru đối đầu với Ma vương Clayman, kẻ đứng sau nhiều âm mưu nhắm vào Tempest, và đánh bại hắn.

<short pause> Tám Ma vương sau đó được gọi chung bằng một cái tên mới, và theo truyện, cái tên đó do chính Rimuru đề xuất. Một slime từng không có tên, giờ đặt tên cho cả nhóm Ma vương.

<short pause> Rimuru trở thành một trong tám Ma vương, và được gọi là Ma vương mới. Đồng thời, anh cuối cùng cũng giải phóng được Veldora khỏi cơ thể mình, giữ đúng lời hứa từ nấc đầu tiên.

<short pause> Từ nấc này trở đi, các mùa sau của anime xoay quanh chính trị, ngoại giao và những cuộc đối đầu với các thế lực lớn hơn. Kaku sẽ dành chúng cho một video khác.

<short pause> Điều kiện: chiến thắng và uy tín. Sức mạnh: vị thế ngang hàng với những sinh vật mạnh nhất. Cái giá: giờ Rimuru là mục tiêu của mọi thế lực muốn lật đổ Ma vương.

<short pause> Nhìn lại cả bậc thang, Kaku thấy một quy luật. Sức mạnh của Rimuru đến từ hai hướng: ăn vào và cho đi.

<short pause> <laugh> Kaku để ý rằng Rimuru chưa bao giờ ăn ai chỉ để mạnh lên. Mỗi lần nuốt đều có lý do: cứu một người bạn, giữ một lời hứa, chấm dứt một thảm họa.

<short pause> Ăn vào là Kẻ săn mồi: nuốt rồng, nuốt Shizu, nuốt Chúa tể Orc. Mỗi lần ăn là một lần học.

<short pause> Kaku thấy đây là thiết kế rất tinh tế: một hệ thống sức mạnh có cả hai chiều. Nếu chỉ có ăn vào, Rimuru sẽ là một con quái vật tham lam. Nếu chỉ có cho đi, anh sẽ không bảo vệ được ai.

<short pause> Cho đi là đặt tên: yêu tinh, sói, kijin, và cả một quốc gia. Mỗi cái tên là một phần năng lượng của Rimuru chuyển sang người khác, và quay lại thành lòng trung thành.

<short pause> Và nấc Chân Ma vương là nơi hai hướng này va chạm: Rimuru phải lấy đi một thứ rất lớn để trả lại những người mình yêu thương.
```

**ElevenLabs**

```text
Tiến hóa xong vẫn chưa đủ. Trong thế giới này, có một nhóm Ma vương mạnh nhất, và muốn được gọi là Ma vương, Rimuru phải được họ công nhận.

[pause] Ở Walpurgis có Milim, Ma vương mạnh nhất, trông như một cô bé hiếu động nhưng có sức hủy diệt khủng khiếp. Cô coi Rimuru là bạn thân, một tình bạn mà cả thế giới phải dè chừng.

[pause] Tại buổi yến tiệc Walpurgis, Rimuru đối đầu với Ma vương Clayman, kẻ đứng sau nhiều âm mưu nhắm vào Tempest, và đánh bại hắn.

[pause] Tám Ma vương sau đó được gọi chung bằng một cái tên mới, và theo truyện, cái tên đó do chính Rimuru đề xuất. Một slime từng không có tên, giờ đặt tên cho cả nhóm Ma vương.

[pause] Rimuru trở thành một trong tám Ma vương, và được gọi là Ma vương mới. Đồng thời, anh cuối cùng cũng giải phóng được Veldora khỏi cơ thể mình, giữ đúng lời hứa từ nấc đầu tiên.

[pause] Từ nấc này trở đi, các mùa sau của anime xoay quanh chính trị, ngoại giao và những cuộc đối đầu với các thế lực lớn hơn. Kaku sẽ dành chúng cho một video khác.

[pause] Điều kiện: chiến thắng và uy tín. Sức mạnh: vị thế ngang hàng với những sinh vật mạnh nhất. Cái giá: giờ Rimuru là mục tiêu của mọi thế lực muốn lật đổ Ma vương.

[pause] Nhìn lại cả bậc thang, Kaku thấy một quy luật. Sức mạnh của Rimuru đến từ hai hướng: ăn vào và cho đi.

[pause] [chuckles] Kaku để ý rằng Rimuru chưa bao giờ ăn ai chỉ để mạnh lên. Mỗi lần nuốt đều có lý do: cứu một người bạn, giữ một lời hứa, chấm dứt một thảm họa.

[pause] Ăn vào là Kẻ săn mồi: nuốt rồng, nuốt Shizu, nuốt Chúa tể Orc. Mỗi lần ăn là một lần học.

[pause] Kaku thấy đây là thiết kế rất tinh tế: một hệ thống sức mạnh có cả hai chiều. Nếu chỉ có ăn vào, Rimuru sẽ là một con quái vật tham lam. Nếu chỉ có cho đi, anh sẽ không bảo vệ được ai.

[pause] Cho đi là đặt tên: yêu tinh, sói, kijin, và cả một quốc gia. Mỗi cái tên là một phần năng lượng của Rimuru chuyển sang người khác, và quay lại thành lòng trung thành.

[pause] Và nấc Chân Ma vương là nơi hai hướng này va chạm: Rimuru phải lấy đi một thứ rất lớn để trả lại những người mình yêu thương.
```

### c08 · Toàn bộ bậc thang / Kết

Khoảng 107 giây · cảnh s72–s81 · 1386 ký tự

**Gemini**

```text
Kaku vẽ lại toàn bộ bậc thang. Nấc không: một người đàn ông chết trong mưa. Nấc một: slime với hai kỹ năng, và một người bạn là rồng.

<short pause> Nấc hai: sức mạnh của cái tên. Nấc ba: hình người và lời hứa với Shizu. Nấc bốn: vua của một quốc gia.

<short pause> Nhìn từ xa, bậc thang này đi lên đều đặn, nhưng không đều về màu sắc: những nấc đầu sáng và ấm, nấc năm tối hẳn, rồi nấc sáu sáng trở lại.

<short pause> Nấc năm: Chân Ma vương, với cái giá nặng nhất. Nấc sáu: được công nhận, và giải phóng người bạn đầu tiên.

<short pause> Và nếu bước lên, bạn sẽ đặt tên cho ai đầu tiên? Kaku thì chắc sẽ đặt tên cho chiếc bàn học, để nó tự dọn dẹp.

<short pause> Nếu bạn là Rimuru, bạn có bước lên nấc thứ năm không? Đây là câu hỏi Kaku nghĩ mãi mà chưa có câu trả lời. Viết suy nghĩ của bạn vào bình luận nhé.

<short pause> Và có lẽ đó là lý do người xem yêu Rimuru: anh mạnh lên rất nhanh, nhưng chưa bao giờ quên mình từng là một nhân viên văn phòng bình thường, chết trong mưa vì bảo vệ người khác.

<short pause> Từ một khối thạch trong hang tới một Ma vương, bậc thang của Rimuru là câu chuyện về việc sức mạnh có thể đến từ sự tử tế, và cũng có thể đòi hỏi những lựa chọn tàn nhẫn nhất.

<short pause> Video tiếp theo, Kaku vẽ một cây phả hệ đặc biệt: chín người đã lần lượt nắm giữ One For All trong My Hero Academia, và mỗi người để lại gì cho người kế tiếp.

<short pause> <laugh> Nếu bạn thích những bậc thang tiến hóa như thế này, hãy đăng ký kênh để leo thêm nhiều bậc thang nữa cùng Kaku. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Kaku vẽ lại toàn bộ bậc thang. Nấc không: một người đàn ông chết trong mưa. Nấc một: slime với hai kỹ năng, và một người bạn là rồng.

[pause] Nấc hai: sức mạnh của cái tên. Nấc ba: hình người và lời hứa với Shizu. Nấc bốn: vua của một quốc gia.

[pause] Nhìn từ xa, bậc thang này đi lên đều đặn, nhưng không đều về màu sắc: những nấc đầu sáng và ấm, nấc năm tối hẳn, rồi nấc sáu sáng trở lại.

[pause] Nấc năm: Chân Ma vương, với cái giá nặng nhất. Nấc sáu: được công nhận, và giải phóng người bạn đầu tiên.

[pause] [curious] Và nếu bước lên, bạn sẽ đặt tên cho ai đầu tiên? Kaku thì chắc sẽ đặt tên cho chiếc bàn học, để nó tự dọn dẹp.

[pause] Nếu bạn là Rimuru, bạn có bước lên nấc thứ năm không? Đây là câu hỏi Kaku nghĩ mãi mà chưa có câu trả lời. Viết suy nghĩ của bạn vào bình luận nhé.

[pause] Và có lẽ đó là lý do người xem yêu Rimuru: anh mạnh lên rất nhanh, nhưng chưa bao giờ quên mình từng là một nhân viên văn phòng bình thường, chết trong mưa vì bảo vệ người khác.

[pause] Từ một khối thạch trong hang tới một Ma vương, bậc thang của Rimuru là câu chuyện về việc sức mạnh có thể đến từ sự tử tế, và cũng có thể đòi hỏi những lựa chọn tàn nhẫn nhất.

[pause] Video tiếp theo, Kaku vẽ một cây phả hệ đặc biệt: chín người đã lần lượt nắm giữ One For All trong My Hero Academia, và mỗi người để lại gì cho người kế tiếp.

[pause] [chuckles] Nếu bạn thích những bậc thang tiến hóa như thế này, hãy đăng ký kênh để leo thêm nhiều bậc thang nữa cùng Kaku. Kaku gấp sổ đây, hẹn gặp lại!
```
