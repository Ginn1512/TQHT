# Bộ prompt · One Piece: Haki hoạt động thế nào? 3 loại và bí mật bá vương

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 96 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Cảnh báo: video có spoiler One Piece đến hết arc Wano. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

```text
Wide 16:9 landscape cinematic frame. a pirate ship silhouette at sea under a stormy sky with a single ray of light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong One Piece, có những người ăn trái ác quỷ để trở nên mạnh, có những người luyện kiếm cả đời. Nhưng ở tần…

```text
Wide 16:9 landscape cinematic frame. a group of pirate silhouettes standing on a cliff, each with a different weapon, facing the horizon. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Thứ đó là Haki, sức mạnh của ý chí. Không có Haki, bạn gần như không có cửa ở Tân Thế Giới.

```text
Wide 16:9 landscape cinematic frame. a clenched fist surrounded by crackling black lightning over a turbulent sea. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng Haki thực chất là gì? Vì sao có ba loại? Và vì sao chỉ một số rất ít người trên thế giới có Haki bá vươ…

```text
Wide 16:9 landscape cinematic frame. three glowing emblems floating above an ocean: an eye, a black fist, and a crown. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã Haki: ba loại, các cấp độ nâng cao, và bí mật của Haki bá…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook on the deck of a small ship, sea breeze. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao một cú đấm có Haki có thể chạm tới người mà nắm đấm thường không bao giờ ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a diagram of a fist passing through smoke and hitting a hidden figure. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Haki là gì?

Lời: Theo truyện, Haki là sức mạnh tiềm ẩn trong mọi sinh vật sống. Ai cũng có, nhưng phần lớn người ta sống cả đờ…

```text
Wide 16:9 landscape cinematic frame. a busy harbor town where every person has a faint invisible glow only visible as a subtle shimmer. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Haki gắn với ý chí, sự tập trung và quyết tâm. Người càng vững vàng về tinh thần, Haki càng mạnh.

```text
Wide 16:9 landscape cinematic frame. a lone figure standing firm against a raging wind on a rocky shore, cloak whipping. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Có thể hiểu Haki giống cơ bắp của tinh thần. Không tập thì nó vẫn ở đó nhưng yếu ớt. Tập đúng cách thì nó trở…

```text
Wide 16:9 landscape cinematic frame. a weight-lifting montage where the weights are glowing spheres of will energy. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Để đánh thức Haki, có hai con đường: rèn luyện khắc nghiệt dưới sự hướng dẫn của người giỏi, hoặc bộc phát tr…

```text
Wide 16:9 landscape cinematic frame. a split image: a teacher and student training on a remote island, and a figure screaming in a burning battlefield. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Luffy trải qua cả hai. Cậu bộc phát vô thức ở những lúc cảm xúc lên đến đỉnh, rồi sau đó luyện tập hai năm để…

```text
Wide 16:9 landscape cinematic frame. a young pirate silhouette training alone on a jungle island, a mentor watching from a rock. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong One Piece, trái ác quỷ cho bạn sức mạnh ngay lập tức, còn Haki thì phải tự kiếm từng chút…

```text
Wide 16:9 landscape cinematic frame. the owl mascot comparing a strange fruit in one wing and a dumbbell in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Vì sao Haki xuất hiện muộn trong truyện?

Lời: Một điều thú vị: suốt nửa đầu One Piece, Haki gần như không được nhắc tên. Vậy mà sau đó nó trở thành nền tản…

```text
Wide 16:9 landscape cinematic frame. an old logbook with early pages blank and later pages filled with glowing black-fist symbols. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nếu đọc lại, bạn sẽ thấy những dấu hiệu từ rất sớm: những người mạnh làm đối thủ ngất chỉ bằng ánh mắt, những…

```text
Wide 16:9 landscape cinematic frame. a figure glaring and a line of enemies fainting behind them, drawn in an old sketchbook style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Haki được giải thích rõ ràng khi băng Mũ Rơm tới quần đảo trước Tân Thế Giới và gặp một người thầy từng đi cù…

```text
Wide 16:9 landscape cinematic frame. an old man silhouette with glasses sitting in a bar by a giant mangrove tree, a young crew listening. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Cách làm này rất khéo: người đọc được làm quen với thế giới trước, rồi mới được trao chìa khóa để hiểu tầng s…

```text
Wide 16:9 landscape cinematic frame. a key being handed from an old hand to a young hand, glowing softly. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nó cũng khớp với hành trình của Luffy: khi còn yếu, cậu không biết Haki tồn tại. Khi đủ lớn để ra Tân Thế Giớ…

```text
Wide 16:9 landscape cinematic frame. a small boat sailing from calm blue waters into a massive stormy sea where lightning strikes. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là cách mở rộng hệ thống sức mạnh mà không làm hỏng phần trước. Những gì đã xảy ra vẫn hợp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping back through an old notebook and nodding with approval. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Loại 1: Haki quan sát

Lời: Loại thứ nhất là Haki quan sát. Nó giúp bạn cảm nhận sự hiện diện, cảm xúc và ý định của những sinh vật xung…

```text
Wide 16:9 landscape cinematic frame. a figure with closed eyes in a dark forest, faint glowing silhouettes of hidden people visible around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Ở mức cơ bản, người dùng biết có bao nhiêu người đang ở gần, họ ở đâu, dù không nhìn thấy.

```text
Wide 16:9 landscape cinematic frame. a top-down map of a ship where glowing dots represent people behind walls. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Ở mức cao hơn, người dùng đọc được đòn tấn công trước khi nó đến. Né đòn trở nên dễ dàng vì bạn biết đối thủ…

```text
Wide 16:9 landscape cinematic frame. a fighter leaning away a split second before a blade passes, ghost trails showing the predicted path. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Ở mức cao nhất trong truyện, người dùng nhìn thấy một đoạn ngắn của tương lai. Đây là trình độ cực hiếm.

```text
Wide 16:9 landscape cinematic frame. a pair of glowing eyes with a faint translucent future scene reflected inside them. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Trận đấu nổi tiếng thể hiện điều này là trận Luffy với Katakuri. Katakuri nhìn thấy tương lai, và Luffy phải…

```text
Wide 16:9 landscape cinematic frame. two silhouettes clashing inside a dreamlike world of mochi-like soft shapes, time trails behind them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Haki quan sát còn có những dạng lạ: có người nghe được tiếng nói của vạn vật, có người cảm nhận từ khoảng các…

```text
Wide 16:9 landscape cinematic frame. a figure listening with eyes closed as faint sound waves ripple from trees, stones, and the sea. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Điểm yếu của Haki quan sát: nó bị ảnh hưởng bởi cảm xúc. Khi hoảng loạn hay giận dữ, khả năng đọc đòn giảm đi…

```text
Wide 16:9 landscape cinematic frame. a fighter's vision blurring and cracking like glass while their heartbeat pounds visibly. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: Haki quan sát là đôi mắt thứ hai. Không mạnh thêm cú đấm nào, nhưng giúp bạn không bao giờ bị b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a second pair of glowing glasses on its forehead. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Loại 2: Haki vũ trang

Lời: Loại thứ hai là Haki vũ trang. Người dùng biến ý chí thành một lớp giáp vô hình bao quanh cơ thể hoặc vũ khí.

```text
Wide 16:9 landscape cinematic frame. a fighter's arm wrapped in a faint shimmering layer of energy, a sword blade similarly coated. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Khi tập trung đủ mạnh, lớp giáp này chuyển sang màu đen bóng, gọi là cứng hóa. Đòn đánh vừa mạnh hơn, vừa bền…

```text
Wide 16:9 landscape cinematic frame. a fist and forearm turning glossy black like polished obsidian, faint lightning at the edges. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Điều quan trọng nhất: Haki vũ trang chạm được vào thực thể của người dùng trái ác quỷ hệ Logia, những người c…

```text
Wide 16:9 landscape cinematic frame. a black-coated fist striking through a cloud of smoke and hitting a hidden solid figure inside. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trước Haki, người Logia gần như bất khả xâm phạm. Đạn xuyên qua, kiếm chém qua. Haki là thứ biến họ thành ngư…

```text
Wide 16:9 landscape cinematic frame. bullets passing harmlessly through a figure made of sand, then a black fist landing solidly. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Haki vũ trang cũng bọc được lên vũ khí. Những kiếm sĩ mạnh nhất có thể phủ Haki lên lưỡi kiếm để chém những t…

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette with a black-coated blade slicing a massive boulder in half. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Ở Wano, Luffy học một cấp cao hơn: phát Haki ra bên ngoài, không chạm vào bề mặt mà đẩy lực xuyên vào bên tro…

```text
Wide 16:9 landscape cinematic frame. a punch stopping just before a target, a shockwave of energy passing through and cracking the target from within. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Kỹ thuật này cho phép đánh xuyên qua lớp phòng thủ cứng nhất, vì lực không dừng lại ở bề mặt.

```text
Wide 16:9 landscape cinematic frame. a diagram showing energy waves passing through an armor plate and exploding behind it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nó cũng giải thích vì sao có người đánh bay đối thủ mà không cần chạm vào. Haki được đẩy ra khỏi cơ thể như m…

```text
Wide 16:9 landscape cinematic frame. a fighter punching the air, a visible ring of force knocking down a line of enemies at a distance. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: Haki vũ trang là áo giáp và vũ khí làm từ ý chí. Cấp thấp là giáp, cấp cao là phá xuyên từ bên…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny black helmet and holding a tiny black hammer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Loại 3: Haki bá vương

Lời: Loại thứ ba là Haki bá vương, và đây là loại đặc biệt nhất. Theo truyện, chỉ khoảng một trong vài triệu người…

```text
Wide 16:9 landscape cinematic frame. a crown of dark energy hovering above a lone figure standing on a hill, tiny crowd far below. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Haki bá vương không luyện ra được nếu bạn không sinh ra đã có. Người có nó được xem là mang tố chất của một v…

```text
Wide 16:9 landscape cinematic frame. a newborn light glowing inside a small crown symbol, surrounded by darkness. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Tác dụng cơ bản: áp đảo ý chí của người khác. Những người có tinh thần yếu hơn sẽ ngất xỉu chỉ vì đứng gần.

```text
Wide 16:9 landscape cinematic frame. a wave of dark red energy sweeping across a crowd, many silhouettes collapsing while a few remain standing. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Người mạnh thì không ngất, nhưng vẫn cảm nhận được áp lực. Khi hai người có Haki bá vương va chạm, bầu trời n…

```text
Wide 16:9 landscape cinematic frame. two figures clashing weapons as black lightning splits the sky above them. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Haki bá vương cũng có thể kiểm soát được. Người dùng giỏi chọn ai bị ảnh hưởng, ai không, thay vì làm tất cả…

```text
Wide 16:9 landscape cinematic frame. a figure releasing a controlled wave that passes harmlessly over allies but knocks down enemies. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Thú vị hơn, Haki bá vương còn ảnh hưởng đến động vật. Những con thú hung dữ có thể phục tùng người mang khí c…

```text
Wide 16:9 landscape cinematic frame. a giant beast bowing its head before a small figure on a jungle path. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là loại Haki duy nhất gắn với số phận. Hai loại kia là chăm chỉ, loại này là được chọn. Mìn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up thoughtfully at a floating crown. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Haki bá vương phủ lên đòn đánh

Lời: Ở Wano, truyện tiết lộ cấp độ cao nhất của Haki bá vương: phủ nó lên đòn đánh, giống như phủ Haki vũ trang.

```text
Wide 16:9 landscape cinematic frame. a fist crackling with both black armor and red-black lightning, sparks dancing above it. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Khi làm được điều này, đòn đánh có thể chạm vào đối thủ mà không cần tiếp xúc trực tiếp, và mạnh hơn hẳn Haki…

```text
Wide 16:9 landscape cinematic frame. a punch surrounded by a halo of black lightning striking a giant figure from a small distance. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Trong truyện, kỹ thuật này được nói là chỉ một số rất ít người mạnh nhất thế giới làm được. Đó là ranh giới g…

```text
Wide 16:9 landscape cinematic frame. a small group of towering silhouettes on a mountain peak with black lightning around them. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Luffy học được nó ngay trong trận quyết chiến ở Wano. Đó là khoảnh khắc cho thấy cậu đã bước vào hàng ngũ nhữ…

```text
Wide 16:9 landscape cinematic frame. a straw-hat silhouette standing on a rooftop at night, black lightning crackling around his fists, back view. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Điều này cũng giải thích vì sao khi những người mạnh nhất va chạm, không khí xung quanh nổ ra từng tia sét đe…

```text
Wide 16:9 landscape cinematic frame. two giant silhouettes clashing mid-air above an island, black lightning bolts radiating outward. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Những người dùng Haki tiêu biểu

Lời: Để dễ hình dung, hãy điểm qua vài nhân vật mà Haki là phần quan trọng trong cách họ chiến đấu.

```text
Wide 16:9 landscape cinematic frame. a gallery wall with six framed silhouettes, each with a small glowing emblem. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Rayleigh, người thầy của Luffy, là hình mẫu của người thành thạo cả ba loại Haki dù đã lớn tuổi. Ông chứng mi…

```text
Wide 16:9 landscape cinematic frame. an old swordsman silhouette with glasses casually blocking a massive strike with one hand. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Zoro là ví dụ của Haki vũ trang phủ lên kiếm. Với kiếm sĩ, Haki biến lưỡi kiếm thường thành thứ chém được cả…

```text
Wide 16:9 landscape cinematic frame. a three-sword stance silhouette with black-coated blades slicing through a stone pillar. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Koby là ví dụ thú vị của Haki quan sát. Cậu nghe được tiếng nói, tiếng kêu cứu của những người xung quanh, mộ…

```text
Wide 16:9 landscape cinematic frame. a young marine silhouette with eyes closed amid a battlefield, faint voices shown as glowing ripples. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Katakuri là ví dụ của Haki quan sát ở đỉnh cao: nhìn thấy tương lai. Anh ta gần như không bao giờ bị đánh trú…

```text
Wide 16:9 landscape cinematic frame. a tall figure effortlessly dodging countless blows, ghostly future images around him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và những Tứ Hoàng như Shanks là ví dụ của Haki bá vương ở mức khiến cả một đội quân ngừng thở. Chỉ sự hiện di…

```text
Wide 16:9 landscape cinematic frame. a calm captain silhouette stepping onto a ship deck as a wave of pressure bends the sails. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Điểm chung: mỗi người dùng Haki theo cách hợp với bản thân. Không có một cách dùng đúng duy nhất, giống như k…

```text
Wide 16:9 landscape cinematic frame. a collage of different fighting stances, each with a unique flow of black energy. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Thử nghiệm: nếu bạn là hải tặc mới

Lời: Giờ thử tưởng tượng bạn là một hải tặc mới, muốn tiến vào Tân Thế Giới. Bạn nên luyện Haki theo thứ tự nào?

```text
Wide 16:9 landscape cinematic frame. a small raft sailing toward a towering red wall of cliffs splitting the ocean. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Bước một: Haki quan sát. Ở biển cả, biết trước nguy hiểm quan trọng hơn đánh mạnh. Né được một đòn chí mạng l…

```text
Wide 16:9 landscape cinematic frame. a lookout silhouette on a mast with eyes closed, sensing a hidden ship behind fog. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Bước hai: Haki vũ trang. Bạn cần nó để đối đầu với người có trái ác quỷ, đặc biệt là Logia. Không có nó, bạn…

```text
Wide 16:9 landscape cinematic frame. a fighter punching through a swirling column of smoke and connecting with a solid figure. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Bước ba: kiểm tra xem mình có Haki bá vương hay không. Phần lớn người không có, và điều đó hoàn toàn bình thư…

```text
Wide 16:9 landscape cinematic frame. a figure looking at their open palm with a question mark glowing above it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Bước bốn: luyện kỹ thuật phá từ bên trong. Đây là thứ giúp bạn đánh bại những đối thủ có phòng thủ cứng hơn m…

```text
Wide 16:9 landscape cinematic frame. a fist stopping short of an armored giant while cracks spread across the giant's armor from within. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nghe thì dễ, nhưng Luffy mất hai năm luyện tập cộng với nhiều trận sinh tử mới đi hết con đường đó. Tân Thế G…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a long winding sea route drawn on a map, whistling softly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Haki và trái ác quỷ

Lời: Một câu hỏi fan hay đặt ra: Haki và trái ác quỷ, cái nào mạnh hơn? Câu trả lời là chúng bổ sung cho nhau, khô…

```text
Wide 16:9 landscape cinematic frame. a scale balancing a strange swirled fruit and a glowing black fist. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Trái ác quỷ cho năng lực đặc biệt, Haki quyết định bạn dùng năng lực đó mạnh tới đâu và có chạm được đối thủ…

```text
Wide 16:9 landscape cinematic frame. a diagram of a strange fruit powering a machine, with a glowing will core controlling the output. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Một người Logia không biết Haki vẫn có thể bị đánh bại bởi người có Haki vũ trang. Ngược lại, người không có…

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette with no powers standing victorious over a figure made of flames. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Nhiều nhân vật mạnh nhất trong truyện là người có Haki cực mạnh, bất kể họ có ăn trái ác quỷ hay không.

```text
Wide 16:9 landscape cinematic frame. a lineup of powerful silhouettes, some with strange energy, some with only swords, all surrounded by black lightning. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rút ra: ở One Piece, năng lực là món quà, còn Haki là thứ bạn tự rèn. Và cuối cùng, ý chí mới quyết định…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing firmly on a rock in a stormy sea, scarf blowing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Cách luyện Haki trong truyện

Lời: Vậy luyện Haki thế nào? Truyện không đưa ra giáo trình chi tiết, nhưng qua các lần huấn luyện, ta thấy vài ng…

```text
Wide 16:9 landscape cinematic frame. an old training scroll with abstract diagrams of eyes, fists, and crowns. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nguyên tắc một: cần môi trường nguy hiểm thật sự. Luffy luyện trên một hòn đảo đầy thú dữ, nơi sai một bước l…

```text
Wide 16:9 landscape cinematic frame. a dense jungle island with huge beasts lurking, a small figure standing alert in a clearing. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Nguyên tắc hai: cần người thầy hiểu Haki. Người thầy không chỉ dạy kỹ thuật mà còn tạo áp lực đúng mức để học…

```text
Wide 16:9 landscape cinematic frame. an old mentor silhouette with glasses watching a student from a high branch, arms crossed. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nguyên tắc ba: luyện Haki quan sát bằng cách bịt mắt và né đòn. Không nhìn được, bạn buộc phải cảm nhận.

```text
Wide 16:9 landscape cinematic frame. a blindfolded fighter dodging falling stones and swinging logs in a training ground. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nguyên tắc bốn: luyện Haki vũ trang bằng cách va chạm liên tục với thứ cứng hơn mình, cho tới khi ý chí trở n…

```text
Wide 16:9 landscape cinematic frame. a fighter punching a massive iron pillar repeatedly, knuckles glowing darker with each strike. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và ở Wano, Luffy còn luyện trong nhà tù, nơi một người già dạy cậu dùng Haki mà không cần chạm vào đối thủ. Đ…

```text
Wide 16:9 landscape cinematic frame. a small old man silhouette teaching a young prisoner in a dark stone cell, a single shaft of light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Ý chí được truyền lại

Lời: Có một lý do sâu hơn khiến Haki quan trọng trong One Piece: cả bộ truyện xoay quanh chủ đề ý chí.

```text
Wide 16:9 landscape cinematic frame. a lantern being passed from one hand to another across generations on a dark shore. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Truyện nhiều lần nhắc tới những thứ không thể ngăn cản: ý chí được truyền lại, giấc mơ của con người, và thời…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols in the night sky above the sea: a torch, a dream cloud, and a turning wheel. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Haki là cách truyện biến chủ đề đó thành sức mạnh cụ thể. Người có ý chí mạnh thì đứng vững, người yếu ý chí…

```text
Wide 16:9 landscape cinematic frame. a line of figures facing a storm, the ones with glowing cores standing firm, others bending. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Vì vậy khi Luffy dùng Haki bá vương, đó không chỉ là một chiêu thức. Nó thể hiện ý chí không chịu khuất phục…

```text
Wide 16:9 landscape cinematic frame. a weathered pirate flag resting on a rock at sunrise, faint black lightning fading around it. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là điểm hay của One Piece: hệ thống sức mạnh và chủ đề câu chuyện là một. Hiểu Haki là hiểu tin…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small pirate flag respectfully, looking at the sea. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku: số phận hay nỗ lực? · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ tới câu hỏi lớn mà Haki đặt ra: trong One Piece, sức mạnh đến từ nỗ lực hay từ số phận?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting at a crossroads sign with two arrows pointing in different directions. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Haki quan sát và Haki vũ trang cho thấy nỗ lực được đền đáp. Ai chịu luyện cũng có thể giỏi, dù xuất phát điể…

```text
Wide 16:9 landscape cinematic frame. a staircase of many steps with small figures climbing steadily upward. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Nhưng Haki bá vương thì khác. Bạn phải sinh ra đã có nó. Điều này làm nhiều fan tranh luận về việc truyện có…

```text
Wide 16:9 landscape cinematic frame. a golden crown glowing at the top of a mountain that only a few chosen figures can approach. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Mình nghĩ Oda cân bằng khá khéo: có Haki bá vương chỉ là tiềm năng. Người không rèn luyện thì cũng chỉ làm ng…

```text
Wide 16:9 landscape cinematic frame. a figure with a faint crown symbol above their head who has not trained, standing uncertainly. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và rất nhiều người không có Haki bá vương vẫn đứng ở đỉnh cao nhờ Haki vũ trang và kỹ thuật cực tốt. Nỗ lực v…

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette with a black blade standing alone on a mountain peak at sunrise. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Đây là điểm hay của Haki so với nhiều hệ thống khác: nó vừa có phần được chọn, vừa có phần tự kiếm. Giống như…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a small crown on one side and a stack of training weights on the other, perfectly level. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Nếu so với Nen, Haki ít luật hơn nhiều. Nen có sáu hệ và giao ước rõ ràng, còn Haki dựa nhiều vào ý chí và cả…

```text
Wide 16:9 landscape cinematic frame. a glowing hexagon on the left and a black lightning fist on the right, side by side. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · 5 hiểu lầm phổ biến về Haki

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm mà mình thấy fan hay nhắc về Haki.

```text
Wide 16:9 landscape cinematic frame. a notice board with five pinned cards, each with a red question mark. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Hiểu lầm một: Haki chỉ dành cho nhân vật chính. Thực ra nhiều lính hải quân và hải tặc bình thường ở Tân Thế…

```text
Wide 16:9 landscape cinematic frame. rows of ordinary marine and pirate silhouettes with faint black-coated fists. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Hiểu lầm hai: Haki bá vương là loại mạnh nhất nên ai có nó sẽ thắng. Không đúng, vì không biết dùng hai loại…

```text
Wide 16:9 landscape cinematic frame. a figure with a faint crown symbol losing a duel to a disciplined swordsman. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Hiểu lầm ba: Haki vũ trang màu đen mới là Haki. Thật ra lớp giáp vô hình không màu cũng là Haki, màu đen chỉ…

```text
Wide 16:9 landscape cinematic frame. two fists side by side: one with a faint clear shimmer, one glossy black. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Hiểu lầm bốn: Haki quan sát giúp né được mọi thứ. Nó bị giới hạn bởi cảm xúc, sự mệt mỏi và tốc độ của đối th…

```text
Wide 16:9 landscape cinematic frame. a tired fighter failing to dodge a blindingly fast strike despite glowing eyes. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Hiểu lầm năm: Haki thay thế trái ác quỷ. Như mình đã nói, chúng bổ sung cho nhau, và người mạnh nhất thường g…

```text
Wide 16:9 landscape cinematic frame. a strange swirled fruit and a black fist fitting together like puzzle pieces. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: những điểm trên dựa trên các trận đấu đã xuất hiện trong truyện tới Wano. Truyện vẫn đang tiếp diễ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a small open book with a question mark bookmark. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · Tóm tắt

Lời: Tóm lại: Haki là sức mạnh ý chí có trong mọi người, nhưng phải đánh thức và rèn luyện mới dùng được.

```text
Wide 16:9 landscape cinematic frame. a summary diagram: a faint glow evolving into a strong aura through three stages. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92

Lời: Haki quan sát để cảm nhận và nhìn trước. Haki vũ trang để phòng thủ, tấn công và chạm vào Logia. Haki bá vươn…

```text
Wide 16:9 landscape cinematic frame. three emblems in a row: an eye, a black fist, and a crown, each glowing. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93

Lời: Và ở đỉnh cao, người mạnh nhất phủ Haki bá vương lên đòn đánh, tạo ra những tia sét đen khi va chạm.

```text
Wide 16:9 landscape cinematic frame. a final image of black lightning crackling around a raised fist against a red sky. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu chỉ được chọn một loại Haki, bạn chọn loại nào và vì sao? Viết xuống phần bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up three cards with an eye, a fist, and a crown. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ vẽ cây phả hệ các kiểu Hơi thở trong Kimetsu no Yaiba.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing family tree diagram made of flowing water and fire lines. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye on the deck of a ship at sunset. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Haki là gì?

Khoảng 113 giây · cảnh s01–s12 · 1467 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler One Piece đến hết arc Wano. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Trong One Piece, có những người ăn trái ác quỷ để trở nên mạnh, có những người luyện kiếm cả đời. <short pause> Nhưng ở tầng cao nhất, tất cả đều phải biết một thứ.

<short pause> Thứ đó là Haki, sức mạnh của ý chí. Không có Haki, bạn gần như không có cửa ở Tân Thế Giới.

<short pause> Nhưng Haki thực chất là gì? Vì sao có ba loại? Và vì sao chỉ một số rất ít người trên thế giới có Haki bá vương?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã Haki: ba loại, các cấp độ nâng cao, và bí mật của Haki bá vương phủ lên đòn đánh.

<short pause> Xem hết video, bạn sẽ hiểu vì sao một cú đấm có Haki có thể chạm tới người mà nắm đấm thường không bao giờ chạm được.

<short pause> Theo truyện, Haki là sức mạnh tiềm ẩn trong mọi sinh vật sống. Ai cũng có, nhưng phần lớn người ta sống cả đời mà không bao giờ đánh thức nó.

<short pause> Haki gắn với ý chí, sự tập trung và quyết tâm. Người càng vững vàng về tinh thần, Haki càng mạnh.

<short pause> Có thể hiểu Haki giống cơ bắp của tinh thần. Không tập thì nó vẫn ở đó nhưng yếu ớt. Tập đúng cách thì nó trở thành vũ khí.

<short pause> Để đánh thức Haki, có hai con đường: rèn luyện khắc nghiệt dưới sự hướng dẫn của người giỏi, hoặc bộc phát trong những khoảnh khắc sinh tử.

<short pause> Luffy trải qua cả hai. Cậu bộc phát vô thức ở những lúc cảm xúc lên đến đỉnh, rồi sau đó luyện tập hai năm để kiểm soát nó.

<short pause> Kaku ghi chú: trong One Piece, trái ác quỷ cho bạn sức mạnh ngay lập tức, còn Haki thì phải tự kiếm từng chút một. Đó là lý do nó đáng giá.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler One Piece đến hết arc Wano. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

[pause] Trong One Piece, có những người ăn trái ác quỷ để trở nên mạnh, có những người luyện kiếm cả đời. [pause] Nhưng ở tầng cao nhất, tất cả đều phải biết một thứ.

[pause] Thứ đó là Haki, sức mạnh của ý chí. Không có Haki, bạn gần như không có cửa ở Tân Thế Giới.

[pause] [curious] Nhưng Haki thực chất là gì? Vì sao có ba loại? Và vì sao chỉ một số rất ít người trên thế giới có Haki bá vương?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã Haki: ba loại, các cấp độ nâng cao, và bí mật của Haki bá vương phủ lên đòn đánh.

[pause] Xem hết video, bạn sẽ hiểu vì sao một cú đấm có Haki có thể chạm tới người mà nắm đấm thường không bao giờ chạm được.

[pause] Theo truyện, Haki là sức mạnh tiềm ẩn trong mọi sinh vật sống. Ai cũng có, nhưng phần lớn người ta sống cả đời mà không bao giờ đánh thức nó.

[pause] Haki gắn với ý chí, sự tập trung và quyết tâm. Người càng vững vàng về tinh thần, Haki càng mạnh.

[pause] Có thể hiểu Haki giống cơ bắp của tinh thần. Không tập thì nó vẫn ở đó nhưng yếu ớt. Tập đúng cách thì nó trở thành vũ khí.

[pause] Để đánh thức Haki, có hai con đường: rèn luyện khắc nghiệt dưới sự hướng dẫn của người giỏi, hoặc bộc phát trong những khoảnh khắc sinh tử.

[pause] Luffy trải qua cả hai. Cậu bộc phát vô thức ở những lúc cảm xúc lên đến đỉnh, rồi sau đó luyện tập hai năm để kiểm soát nó.

[pause] Kaku ghi chú: trong One Piece, trái ác quỷ cho bạn sức mạnh ngay lập tức, còn Haki thì phải tự kiếm từng chút một. Đó là lý do nó đáng giá.
```

### c02 · Vì sao Haki xuất hiện muộn trong truyện? / Loại 1: Haki quan sát

Khoảng 133 giây · cảnh s13–s26 · 1732 ký tự

**Gemini**

```text
Một điều thú vị: suốt nửa đầu One Piece, Haki gần như không được nhắc tên. Vậy mà sau đó nó trở thành nền tảng của mọi trận đấu lớn.

<short pause> Nếu đọc lại, bạn sẽ thấy những dấu hiệu từ rất sớm: những người mạnh làm đối thủ ngất chỉ bằng ánh mắt, những cú đánh chạm được người tưởng như không thể chạm.

<short pause> Haki được giải thích rõ ràng khi băng Mũ Rơm tới quần đảo trước Tân Thế Giới và gặp một người thầy từng đi cùng Vua Hải Tặc.

<short pause> Cách làm này rất khéo: người đọc được làm quen với thế giới trước, rồi mới được trao chìa khóa để hiểu tầng sâu hơn của sức mạnh.

<short pause> Nó cũng khớp với hành trình của Luffy: khi còn yếu, cậu không biết Haki tồn tại. Khi đủ lớn để ra Tân Thế Giới, cậu buộc phải học nó.

<short pause> <laugh> Kaku ghi chú: đây là cách mở rộng hệ thống sức mạnh mà không làm hỏng phần trước. Những gì đã xảy ra vẫn hợp lý khi nhìn lại.

<short pause> Loại thứ nhất là Haki quan sát. Nó giúp bạn cảm nhận sự hiện diện, cảm xúc và ý định của những sinh vật xung quanh.

<short pause> Ở mức cơ bản, người dùng biết có bao nhiêu người đang ở gần, họ ở đâu, dù không nhìn thấy.

<short pause> Ở mức cao hơn, người dùng đọc được đòn tấn công trước khi nó đến. Né đòn trở nên dễ dàng vì bạn biết đối thủ định làm gì.

<short pause> Ở mức cao nhất trong truyện, người dùng nhìn thấy một đoạn ngắn của tương lai. Đây là trình độ cực hiếm.

<short pause> Trận đấu nổi tiếng thể hiện điều này là trận Luffy với Katakuri. Katakuri nhìn thấy tương lai, và Luffy phải học được điều đó ngay trong trận đấu.

<short pause> Haki quan sát còn có những dạng lạ: có người nghe được tiếng nói của vạn vật, có người cảm nhận từ khoảng cách rất xa.

<short pause> Điểm yếu của Haki quan sát: nó bị ảnh hưởng bởi cảm xúc. Khi hoảng loạn hay giận dữ, khả năng đọc đòn giảm đi rất nhiều.

<short pause> Kaku tóm lại: Haki quan sát là đôi mắt thứ hai. Không mạnh thêm cú đấm nào, nhưng giúp bạn không bao giờ bị bất ngờ.
```

**ElevenLabs**

```text
Một điều thú vị: suốt nửa đầu One Piece, Haki gần như không được nhắc tên. Vậy mà sau đó nó trở thành nền tảng của mọi trận đấu lớn.

[pause] Nếu đọc lại, bạn sẽ thấy những dấu hiệu từ rất sớm: những người mạnh làm đối thủ ngất chỉ bằng ánh mắt, những cú đánh chạm được người tưởng như không thể chạm.

[pause] Haki được giải thích rõ ràng khi băng Mũ Rơm tới quần đảo trước Tân Thế Giới và gặp một người thầy từng đi cùng Vua Hải Tặc.

[pause] Cách làm này rất khéo: người đọc được làm quen với thế giới trước, rồi mới được trao chìa khóa để hiểu tầng sâu hơn của sức mạnh.

[pause] Nó cũng khớp với hành trình của Luffy: khi còn yếu, cậu không biết Haki tồn tại. Khi đủ lớn để ra Tân Thế Giới, cậu buộc phải học nó.

[pause] [chuckles] Kaku ghi chú: đây là cách mở rộng hệ thống sức mạnh mà không làm hỏng phần trước. Những gì đã xảy ra vẫn hợp lý khi nhìn lại.

[pause] Loại thứ nhất là Haki quan sát. Nó giúp bạn cảm nhận sự hiện diện, cảm xúc và ý định của những sinh vật xung quanh.

[pause] Ở mức cơ bản, người dùng biết có bao nhiêu người đang ở gần, họ ở đâu, dù không nhìn thấy.

[pause] Ở mức cao hơn, người dùng đọc được đòn tấn công trước khi nó đến. Né đòn trở nên dễ dàng vì bạn biết đối thủ định làm gì.

[pause] Ở mức cao nhất trong truyện, người dùng nhìn thấy một đoạn ngắn của tương lai. Đây là trình độ cực hiếm.

[pause] Trận đấu nổi tiếng thể hiện điều này là trận Luffy với Katakuri. Katakuri nhìn thấy tương lai, và Luffy phải học được điều đó ngay trong trận đấu.

[pause] Haki quan sát còn có những dạng lạ: có người nghe được tiếng nói của vạn vật, có người cảm nhận từ khoảng cách rất xa.

[pause] Điểm yếu của Haki quan sát: nó bị ảnh hưởng bởi cảm xúc. Khi hoảng loạn hay giận dữ, khả năng đọc đòn giảm đi rất nhiều.

[pause] Kaku tóm lại: Haki quan sát là đôi mắt thứ hai. Không mạnh thêm cú đấm nào, nhưng giúp bạn không bao giờ bị bất ngờ.
```

### c03 · Loại 2: Haki vũ trang / Loại 3: Haki bá vương

Khoảng 150 giây · cảnh s27–s42 · 1944 ký tự

**Gemini**

```text
Loại thứ hai là Haki vũ trang. Người dùng biến ý chí thành một lớp giáp vô hình bao quanh cơ thể hoặc vũ khí.

<short pause> Khi tập trung đủ mạnh, lớp giáp này chuyển sang màu đen bóng, gọi là cứng hóa. Đòn đánh vừa mạnh hơn, vừa bền hơn.

<short pause> Điều quan trọng nhất: Haki vũ trang chạm được vào thực thể của người dùng trái ác quỷ hệ Logia, những người có thể biến thành khói, lửa hay sét.

<short pause> Trước Haki, người Logia gần như bất khả xâm phạm. Đạn xuyên qua, kiếm chém qua. Haki là thứ biến họ thành người có thể bị đánh bại.

<short pause> Haki vũ trang cũng bọc được lên vũ khí. Những kiếm sĩ mạnh nhất có thể phủ Haki lên lưỡi kiếm để chém những thứ tưởng như không thể chém.

<short pause> Ở Wano, Luffy học một cấp cao hơn: phát Haki ra bên ngoài, không chạm vào bề mặt mà đẩy lực xuyên vào bên trong đối thủ.

<short pause> Kỹ thuật này cho phép đánh xuyên qua lớp phòng thủ cứng nhất, vì lực không dừng lại ở bề mặt.

<short pause> Nó cũng giải thích vì sao có người đánh bay đối thủ mà không cần chạm vào. Haki được đẩy ra khỏi cơ thể như một làn sóng.

<short pause> <laugh> Kaku tóm lại: Haki vũ trang là áo giáp và vũ khí làm từ ý chí. Cấp thấp là giáp, cấp cao là phá xuyên từ bên trong.

<short pause> Loại thứ ba là Haki bá vương, và đây là loại đặc biệt nhất. Theo truyện, chỉ khoảng một trong vài triệu người sinh ra đã có nó.

<short pause> Haki bá vương không luyện ra được nếu bạn không sinh ra đã có. Người có nó được xem là mang tố chất của một vị vua.

<short pause> Tác dụng cơ bản: áp đảo ý chí của người khác. Những người có tinh thần yếu hơn sẽ ngất xỉu chỉ vì đứng gần.

<short pause> Người mạnh thì không ngất, nhưng vẫn cảm nhận được áp lực. Khi hai người có Haki bá vương va chạm, bầu trời như bị xé toạc.

<short pause> Haki bá vương cũng có thể kiểm soát được. Người dùng giỏi chọn ai bị ảnh hưởng, ai không, thay vì làm tất cả xung quanh ngất xỉu.

<short pause> Thú vị hơn, Haki bá vương còn ảnh hưởng đến động vật. Những con thú hung dữ có thể phục tùng người mang khí chất vua.

<short pause> Kaku ghi chú: đây là loại Haki duy nhất gắn với số phận. Hai loại kia là chăm chỉ, loại này là được chọn. Mình sẽ bàn điều đó ở phần góc nhìn.
```

**ElevenLabs**

```text
Loại thứ hai là Haki vũ trang. Người dùng biến ý chí thành một lớp giáp vô hình bao quanh cơ thể hoặc vũ khí.

[pause] Khi tập trung đủ mạnh, lớp giáp này chuyển sang màu đen bóng, gọi là cứng hóa. Đòn đánh vừa mạnh hơn, vừa bền hơn.

[pause] Điều quan trọng nhất: Haki vũ trang chạm được vào thực thể của người dùng trái ác quỷ hệ Logia, những người có thể biến thành khói, lửa hay sét.

[pause] Trước Haki, người Logia gần như bất khả xâm phạm. Đạn xuyên qua, kiếm chém qua. Haki là thứ biến họ thành người có thể bị đánh bại.

[pause] Haki vũ trang cũng bọc được lên vũ khí. Những kiếm sĩ mạnh nhất có thể phủ Haki lên lưỡi kiếm để chém những thứ tưởng như không thể chém.

[pause] Ở Wano, Luffy học một cấp cao hơn: phát Haki ra bên ngoài, không chạm vào bề mặt mà đẩy lực xuyên vào bên trong đối thủ.

[pause] Kỹ thuật này cho phép đánh xuyên qua lớp phòng thủ cứng nhất, vì lực không dừng lại ở bề mặt.

[pause] Nó cũng giải thích vì sao có người đánh bay đối thủ mà không cần chạm vào. Haki được đẩy ra khỏi cơ thể như một làn sóng.

[pause] [chuckles] Kaku tóm lại: Haki vũ trang là áo giáp và vũ khí làm từ ý chí. Cấp thấp là giáp, cấp cao là phá xuyên từ bên trong.

[pause] Loại thứ ba là Haki bá vương, và đây là loại đặc biệt nhất. Theo truyện, chỉ khoảng một trong vài triệu người sinh ra đã có nó.

[pause] Haki bá vương không luyện ra được nếu bạn không sinh ra đã có. Người có nó được xem là mang tố chất của một vị vua.

[pause] Tác dụng cơ bản: áp đảo ý chí của người khác. Những người có tinh thần yếu hơn sẽ ngất xỉu chỉ vì đứng gần.

[pause] Người mạnh thì không ngất, nhưng vẫn cảm nhận được áp lực. Khi hai người có Haki bá vương va chạm, bầu trời như bị xé toạc.

[pause] Haki bá vương cũng có thể kiểm soát được. Người dùng giỏi chọn ai bị ảnh hưởng, ai không, thay vì làm tất cả xung quanh ngất xỉu.

[pause] Thú vị hơn, Haki bá vương còn ảnh hưởng đến động vật. Những con thú hung dữ có thể phục tùng người mang khí chất vua.

[pause] Kaku ghi chú: đây là loại Haki duy nhất gắn với số phận. Hai loại kia là chăm chỉ, loại này là được chọn. Mình sẽ bàn điều đó ở phần góc nhìn.
```

### c04 · Haki bá vương phủ lên đòn đánh / Những người dùng Haki tiêu biểu

Khoảng 119 giây · cảnh s43–s54 · 1549 ký tự

**Gemini**

```text
Ở Wano, truyện tiết lộ cấp độ cao nhất của Haki bá vương: phủ nó lên đòn đánh, giống như phủ Haki vũ trang.

<short pause> Khi làm được điều này, đòn đánh có thể chạm vào đối thủ mà không cần tiếp xúc trực tiếp, và mạnh hơn hẳn Haki vũ trang thông thường.

<short pause> Trong truyện, kỹ thuật này được nói là chỉ một số rất ít người mạnh nhất thế giới làm được. Đó là ranh giới giữa mạnh và cực mạnh.

<short pause> Luffy học được nó ngay trong trận quyết chiến ở Wano. Đó là khoảnh khắc cho thấy cậu đã bước vào hàng ngũ những người đứng trên đỉnh.

<short pause> Điều này cũng giải thích vì sao khi những người mạnh nhất va chạm, không khí xung quanh nổ ra từng tia sét đen. Đó là Haki bá vương phủ lên từng đòn.

<short pause> Để dễ hình dung, hãy điểm qua vài nhân vật mà Haki là phần quan trọng trong cách họ chiến đấu.

<short pause> Rayleigh, người thầy của Luffy, là hình mẫu của người thành thạo cả ba loại Haki dù đã lớn tuổi. Ông chứng minh kinh nghiệm có thể bù cho sức trẻ.

<short pause> Zoro là ví dụ của Haki vũ trang phủ lên kiếm. Với kiếm sĩ, Haki biến lưỡi kiếm thường thành thứ chém được cả thép và đá.

<short pause> Koby là ví dụ thú vị của Haki quan sát. Cậu nghe được tiếng nói, tiếng kêu cứu của những người xung quanh, một dạng cảm nhận rất nhạy.

<short pause> Katakuri là ví dụ của Haki quan sát ở đỉnh cao: nhìn thấy tương lai. Anh ta gần như không bao giờ bị đánh trúng cho tới khi gặp Luffy.

<short pause> Và những Tứ Hoàng như Shanks là ví dụ của Haki bá vương ở mức khiến cả một đội quân ngừng thở. Chỉ sự hiện diện của họ đã là vũ khí.

<short pause> Điểm chung: mỗi người dùng Haki theo cách hợp với bản thân. Không có một cách dùng đúng duy nhất, giống như không có một kiểu võ duy nhất.
```

**ElevenLabs**

```text
Ở Wano, truyện tiết lộ cấp độ cao nhất của Haki bá vương: phủ nó lên đòn đánh, giống như phủ Haki vũ trang.

[pause] Khi làm được điều này, đòn đánh có thể chạm vào đối thủ mà không cần tiếp xúc trực tiếp, và mạnh hơn hẳn Haki vũ trang thông thường.

[pause] Trong truyện, kỹ thuật này được nói là chỉ một số rất ít người mạnh nhất thế giới làm được. Đó là ranh giới giữa mạnh và cực mạnh.

[pause] Luffy học được nó ngay trong trận quyết chiến ở Wano. Đó là khoảnh khắc cho thấy cậu đã bước vào hàng ngũ những người đứng trên đỉnh.

[pause] Điều này cũng giải thích vì sao khi những người mạnh nhất va chạm, không khí xung quanh nổ ra từng tia sét đen. Đó là Haki bá vương phủ lên từng đòn.

[pause] Để dễ hình dung, hãy điểm qua vài nhân vật mà Haki là phần quan trọng trong cách họ chiến đấu.

[pause] Rayleigh, người thầy của Luffy, là hình mẫu của người thành thạo cả ba loại Haki dù đã lớn tuổi. Ông chứng minh kinh nghiệm có thể bù cho sức trẻ.

[pause] Zoro là ví dụ của Haki vũ trang phủ lên kiếm. Với kiếm sĩ, Haki biến lưỡi kiếm thường thành thứ chém được cả thép và đá.

[pause] Koby là ví dụ thú vị của Haki quan sát. Cậu nghe được tiếng nói, tiếng kêu cứu của những người xung quanh, một dạng cảm nhận rất nhạy.

[pause] Katakuri là ví dụ của Haki quan sát ở đỉnh cao: nhìn thấy tương lai. Anh ta gần như không bao giờ bị đánh trúng cho tới khi gặp Luffy.

[pause] Và những Tứ Hoàng như Shanks là ví dụ của Haki bá vương ở mức khiến cả một đội quân ngừng thở. Chỉ sự hiện diện của họ đã là vũ khí.

[pause] Điểm chung: mỗi người dùng Haki theo cách hợp với bản thân. Không có một cách dùng đúng duy nhất, giống như không có một kiểu võ duy nhất.
```

### c05 · Thử nghiệm: nếu bạn là hải tặc mới / Haki và trái ác quỷ

Khoảng 105 giây · cảnh s55–s65 · 1371 ký tự

**Gemini**

```text
Giờ thử tưởng tượng bạn là một hải tặc mới, muốn tiến vào Tân Thế Giới. Bạn nên luyện Haki theo thứ tự nào?

<short pause> Bước một: Haki quan sát. Ở biển cả, biết trước nguy hiểm quan trọng hơn đánh mạnh. Né được một đòn chí mạng là sống thêm một ngày.

<short pause> Bước hai: Haki vũ trang. Bạn cần nó để đối đầu với người có trái ác quỷ, đặc biệt là Logia. Không có nó, bạn đánh vào không khí.

<short pause> Bước ba: kiểm tra xem mình có Haki bá vương hay không. Phần lớn người không có, và điều đó hoàn toàn bình thường.

<short pause> Bước bốn: luyện kỹ thuật phá từ bên trong. Đây là thứ giúp bạn đánh bại những đối thủ có phòng thủ cứng hơn mình rất nhiều.

<short pause> Nghe thì dễ, nhưng Luffy mất hai năm luyện tập cộng với nhiều trận sinh tử mới đi hết con đường đó. Tân Thế Giới không dành cho người vội vàng.

<short pause> Một câu hỏi fan hay đặt ra: Haki và trái ác quỷ, cái nào mạnh hơn? Câu trả lời là chúng bổ sung cho nhau, không thay thế nhau.

<short pause> Trái ác quỷ cho năng lực đặc biệt, Haki quyết định bạn dùng năng lực đó mạnh tới đâu và có chạm được đối thủ hay không.

<short pause> Một người Logia không biết Haki vẫn có thể bị đánh bại bởi người có Haki vũ trang. Ngược lại, người không có trái ác quỷ vẫn có thể đứng trên đỉnh nhờ Haki.

<short pause> Nhiều nhân vật mạnh nhất trong truyện là người có Haki cực mạnh, bất kể họ có ăn trái ác quỷ hay không.

<short pause> <laugh> Kaku rút ra: ở One Piece, năng lực là món quà, còn Haki là thứ bạn tự rèn. Và cuối cùng, ý chí mới quyết định ai đứng vững.
```

**ElevenLabs**

```text
Giờ thử tưởng tượng bạn là một hải tặc mới, muốn tiến vào Tân Thế Giới. [curious] Bạn nên luyện Haki theo thứ tự nào?

[pause] Bước một: Haki quan sát. Ở biển cả, biết trước nguy hiểm quan trọng hơn đánh mạnh. Né được một đòn chí mạng là sống thêm một ngày.

[pause] Bước hai: Haki vũ trang. Bạn cần nó để đối đầu với người có trái ác quỷ, đặc biệt là Logia. Không có nó, bạn đánh vào không khí.

[pause] Bước ba: kiểm tra xem mình có Haki bá vương hay không. Phần lớn người không có, và điều đó hoàn toàn bình thường.

[pause] Bước bốn: luyện kỹ thuật phá từ bên trong. Đây là thứ giúp bạn đánh bại những đối thủ có phòng thủ cứng hơn mình rất nhiều.

[pause] Nghe thì dễ, nhưng Luffy mất hai năm luyện tập cộng với nhiều trận sinh tử mới đi hết con đường đó. Tân Thế Giới không dành cho người vội vàng.

[pause] Một câu hỏi fan hay đặt ra: Haki và trái ác quỷ, cái nào mạnh hơn? Câu trả lời là chúng bổ sung cho nhau, không thay thế nhau.

[pause] Trái ác quỷ cho năng lực đặc biệt, Haki quyết định bạn dùng năng lực đó mạnh tới đâu và có chạm được đối thủ hay không.

[pause] Một người Logia không biết Haki vẫn có thể bị đánh bại bởi người có Haki vũ trang. Ngược lại, người không có trái ác quỷ vẫn có thể đứng trên đỉnh nhờ Haki.

[pause] Nhiều nhân vật mạnh nhất trong truyện là người có Haki cực mạnh, bất kể họ có ăn trái ác quỷ hay không.

[pause] [chuckles] Kaku rút ra: ở One Piece, năng lực là món quà, còn Haki là thứ bạn tự rèn. Và cuối cùng, ý chí mới quyết định ai đứng vững.
```

### c06 · Cách luyện Haki trong truyện / Ý chí được truyền lại

Khoảng 105 giây · cảnh s66–s76 · 1368 ký tự

**Gemini**

```text
Vậy luyện Haki thế nào? Truyện không đưa ra giáo trình chi tiết, nhưng qua các lần huấn luyện, ta thấy vài nguyên tắc chung.

<short pause> Nguyên tắc một: cần môi trường nguy hiểm thật sự. Luffy luyện trên một hòn đảo đầy thú dữ, nơi sai một bước là mất mạng.

<short pause> Nguyên tắc hai: cần người thầy hiểu Haki. Người thầy không chỉ dạy kỹ thuật mà còn tạo áp lực đúng mức để học trò vượt giới hạn.

<short pause> Nguyên tắc ba: luyện Haki quan sát bằng cách bịt mắt và né đòn. Không nhìn được, bạn buộc phải cảm nhận.

<short pause> Nguyên tắc bốn: luyện Haki vũ trang bằng cách va chạm liên tục với thứ cứng hơn mình, cho tới khi ý chí trở nên cứng như thép.

<short pause> Và ở Wano, Luffy còn luyện trong nhà tù, nơi một người già dạy cậu dùng Haki mà không cần chạm vào đối thủ. Đôi khi thầy giỏi xuất hiện ở nơi không ngờ nhất.

<short pause> Có một lý do sâu hơn khiến Haki quan trọng trong One Piece: cả bộ truyện xoay quanh chủ đề ý chí.

<short pause> Truyện nhiều lần nhắc tới những thứ không thể ngăn cản: ý chí được truyền lại, giấc mơ của con người, và thời đại luôn thay đổi.

<short pause> Haki là cách truyện biến chủ đề đó thành sức mạnh cụ thể. Người có ý chí mạnh thì đứng vững, người yếu ý chí thì gục ngã trước áp lực.

<short pause> Vì vậy khi Luffy dùng Haki bá vương, đó không chỉ là một chiêu thức. Nó thể hiện ý chí không chịu khuất phục của cậu.

<short pause> <laugh> Kaku thấy đây là điểm hay của One Piece: hệ thống sức mạnh và chủ đề câu chuyện là một. Hiểu Haki là hiểu tinh thần của cả bộ truyện.
```

**ElevenLabs**

```text
[curious] Vậy luyện Haki thế nào? Truyện không đưa ra giáo trình chi tiết, nhưng qua các lần huấn luyện, ta thấy vài nguyên tắc chung.

[pause] Nguyên tắc một: cần môi trường nguy hiểm thật sự. Luffy luyện trên một hòn đảo đầy thú dữ, nơi sai một bước là mất mạng.

[pause] Nguyên tắc hai: cần người thầy hiểu Haki. Người thầy không chỉ dạy kỹ thuật mà còn tạo áp lực đúng mức để học trò vượt giới hạn.

[pause] Nguyên tắc ba: luyện Haki quan sát bằng cách bịt mắt và né đòn. Không nhìn được, bạn buộc phải cảm nhận.

[pause] Nguyên tắc bốn: luyện Haki vũ trang bằng cách va chạm liên tục với thứ cứng hơn mình, cho tới khi ý chí trở nên cứng như thép.

[pause] Và ở Wano, Luffy còn luyện trong nhà tù, nơi một người già dạy cậu dùng Haki mà không cần chạm vào đối thủ. Đôi khi thầy giỏi xuất hiện ở nơi không ngờ nhất.

[pause] Có một lý do sâu hơn khiến Haki quan trọng trong One Piece: cả bộ truyện xoay quanh chủ đề ý chí.

[pause] Truyện nhiều lần nhắc tới những thứ không thể ngăn cản: ý chí được truyền lại, giấc mơ của con người, và thời đại luôn thay đổi.

[pause] Haki là cách truyện biến chủ đề đó thành sức mạnh cụ thể. Người có ý chí mạnh thì đứng vững, người yếu ý chí thì gục ngã trước áp lực.

[pause] Vì vậy khi Luffy dùng Haki bá vương, đó không chỉ là một chiêu thức. Nó thể hiện ý chí không chịu khuất phục của cậu.

[pause] [chuckles] Kaku thấy đây là điểm hay của One Piece: hệ thống sức mạnh và chủ đề câu chuyện là một. Hiểu Haki là hiểu tinh thần của cả bộ truyện.
```

### c07 · Góc nhìn của Kaku: số phận hay nỗ lực? / 5 hiểu lầm phổ biến về Haki

Khoảng 137 giây · cảnh s77–s90 · 1775 ký tự

**Gemini**

```text
Giờ tới câu hỏi lớn mà Haki đặt ra: trong One Piece, sức mạnh đến từ nỗ lực hay từ số phận?

<short pause> Haki quan sát và Haki vũ trang cho thấy nỗ lực được đền đáp. Ai chịu luyện cũng có thể giỏi, dù xuất phát điểm thấp.

<short pause> Nhưng Haki bá vương thì khác. Bạn phải sinh ra đã có nó. Điều này làm nhiều fan tranh luận về việc truyện có đề cao số phận quá không.

<short pause> Mình nghĩ Oda cân bằng khá khéo: có Haki bá vương chỉ là tiềm năng. Người không rèn luyện thì cũng chỉ làm người yếu ngất xỉu mà thôi.

<short pause> Và rất nhiều người không có Haki bá vương vẫn đứng ở đỉnh cao nhờ Haki vũ trang và kỹ thuật cực tốt. Nỗ lực vẫn có chỗ đứng.

<short pause> Đây là điểm hay của Haki so với nhiều hệ thống khác: nó vừa có phần được chọn, vừa có phần tự kiếm. Giống như tài năng và chăm chỉ ngoài đời.

<short pause> Nếu so với Nen, Haki ít luật hơn nhiều. Nen có sáu hệ và giao ước rõ ràng, còn Haki dựa nhiều vào ý chí và cảm xúc. Mỗi kiểu có cái hay riêng.

<short pause> Trước khi tổng kết, cùng gỡ vài hiểu lầm mà mình thấy fan hay nhắc về Haki.

<short pause> Hiểu lầm một: Haki chỉ dành cho nhân vật chính. Thực ra nhiều lính hải quân và hải tặc bình thường ở Tân Thế Giới cũng dùng Haki cơ bản.

<short pause> Hiểu lầm hai: Haki bá vương là loại mạnh nhất nên ai có nó sẽ thắng. Không đúng, vì không biết dùng hai loại kia thì vẫn thua người rèn luyện kỹ.

<short pause> Hiểu lầm ba: Haki vũ trang màu đen mới là Haki. <short pause> Thật ra lớp giáp vô hình không màu cũng là Haki, màu đen chỉ là mức tập trung cao hơn.

<short pause> Hiểu lầm bốn: Haki quan sát giúp né được mọi thứ. Nó bị giới hạn bởi cảm xúc, sự mệt mỏi và tốc độ của đối thủ. Người nhanh hơn vẫn đánh trúng được.

<short pause> Hiểu lầm năm: Haki thay thế trái ác quỷ. Như mình đã nói, chúng bổ sung cho nhau, và người mạnh nhất thường giỏi cả hai.

<short pause> <laugh> Kaku nhắc: những điểm trên dựa trên các trận đấu đã xuất hiện trong truyện tới Wano. Truyện vẫn đang tiếp diễn, nên có thể còn bất ngờ.
```

**ElevenLabs**

```text
[curious] Giờ tới câu hỏi lớn mà Haki đặt ra: trong One Piece, sức mạnh đến từ nỗ lực hay từ số phận?

[pause] Haki quan sát và Haki vũ trang cho thấy nỗ lực được đền đáp. Ai chịu luyện cũng có thể giỏi, dù xuất phát điểm thấp.

[pause] Nhưng Haki bá vương thì khác. Bạn phải sinh ra đã có nó. Điều này làm nhiều fan tranh luận về việc truyện có đề cao số phận quá không.

[pause] Mình nghĩ Oda cân bằng khá khéo: có Haki bá vương chỉ là tiềm năng. Người không rèn luyện thì cũng chỉ làm người yếu ngất xỉu mà thôi.

[pause] Và rất nhiều người không có Haki bá vương vẫn đứng ở đỉnh cao nhờ Haki vũ trang và kỹ thuật cực tốt. Nỗ lực vẫn có chỗ đứng.

[pause] Đây là điểm hay của Haki so với nhiều hệ thống khác: nó vừa có phần được chọn, vừa có phần tự kiếm. Giống như tài năng và chăm chỉ ngoài đời.

[pause] Nếu so với Nen, Haki ít luật hơn nhiều. Nen có sáu hệ và giao ước rõ ràng, còn Haki dựa nhiều vào ý chí và cảm xúc. Mỗi kiểu có cái hay riêng.

[pause] Trước khi tổng kết, cùng gỡ vài hiểu lầm mà mình thấy fan hay nhắc về Haki.

[pause] Hiểu lầm một: Haki chỉ dành cho nhân vật chính. Thực ra nhiều lính hải quân và hải tặc bình thường ở Tân Thế Giới cũng dùng Haki cơ bản.

[pause] Hiểu lầm hai: Haki bá vương là loại mạnh nhất nên ai có nó sẽ thắng. Không đúng, vì không biết dùng hai loại kia thì vẫn thua người rèn luyện kỹ.

[pause] Hiểu lầm ba: Haki vũ trang màu đen mới là Haki. [pause] Thật ra lớp giáp vô hình không màu cũng là Haki, màu đen chỉ là mức tập trung cao hơn.

[pause] Hiểu lầm bốn: Haki quan sát giúp né được mọi thứ. Nó bị giới hạn bởi cảm xúc, sự mệt mỏi và tốc độ của đối thủ. Người nhanh hơn vẫn đánh trúng được.

[pause] Hiểu lầm năm: Haki thay thế trái ác quỷ. Như mình đã nói, chúng bổ sung cho nhau, và người mạnh nhất thường giỏi cả hai.

[pause] [chuckles] Kaku nhắc: những điểm trên dựa trên các trận đấu đã xuất hiện trong truyện tới Wano. Truyện vẫn đang tiếp diễn, nên có thể còn bất ngờ.
```

### c08 · Tóm tắt

Khoảng 45 giây · cảnh s91–s96 · 585 ký tự

**Gemini**

```text
Tóm lại: Haki là sức mạnh ý chí có trong mọi người, nhưng phải đánh thức và rèn luyện mới dùng được.

<short pause> Haki quan sát để cảm nhận và nhìn trước. Haki vũ trang để phòng thủ, tấn công và chạm vào Logia. Haki bá vương để áp đảo ý chí người khác.

<short pause> Và ở đỉnh cao, người mạnh nhất phủ Haki bá vương lên đòn đánh, tạo ra những tia sét đen khi va chạm.

<short pause> Câu hỏi cho bạn: nếu chỉ được chọn một loại Haki, bạn chọn loại nào và vì sao? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ vẽ cây phả hệ các kiểu Hơi thở trong Kimetsu no Yaiba.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: Haki là sức mạnh ý chí có trong mọi người, nhưng phải đánh thức và rèn luyện mới dùng được.

[pause] Haki quan sát để cảm nhận và nhìn trước. Haki vũ trang để phòng thủ, tấn công và chạm vào Logia. Haki bá vương để áp đảo ý chí người khác.

[pause] Và ở đỉnh cao, người mạnh nhất phủ Haki bá vương lên đòn đánh, tạo ra những tia sét đen khi va chạm.

[pause] [curious] Câu hỏi cho bạn: nếu chỉ được chọn một loại Haki, bạn chọn loại nào và vì sao? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ vẽ cây phả hệ các kiểu Hơi thở trong Kimetsu no Yaiba.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
