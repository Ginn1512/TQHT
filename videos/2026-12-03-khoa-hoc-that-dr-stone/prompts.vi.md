# Bộ prompt · Dr. Stone: Phát minh nào của Senku làm được ngoài đời thật?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
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

Lời: Cảnh báo: video có spoiler Dr. Stone tới hết anime, kể cả mùa cuối phát năm 2026. Và một cảnh báo quan trọng…

```text
Wide 16:9 landscape cinematic frame. a stone-age workshop with glass flasks and a large warning sign painted on a wooden board. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy tưởng tượng bạn tỉnh dậy sau ba nghìn bảy trăm năm. Mọi thành phố đã thành rừng. Không điện, không thuốc,…

```text
Wide 16:9 landscape cinematic frame. a figure breaking free from a stone shell in a lush overgrown forest where a city once stood. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đó là tình cảnh của Senku, nhân vật chính của Dr. Stone. Và cậu quyết định xây lại toàn bộ nền văn minh, từ c…

```text
Wide 16:9 landscape cinematic frame. a young scientist silhouette standing on a hill, looking at a vast untouched wilderness with determination. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku, và hôm nay Kaku hỏi một câu thôi: những phát minh của Senku, ngoài đời thật có là…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing safety goggles, opening a notebook beside a rustic lab bench. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Cuối video, Kaku sẽ xếp tất cả lên một bảng khả thi, từ dễ như nấu ăn tới khó như lên Mặt Trăng.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a long chart on a wooden wall, from a campfire icon to a rocket icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Thế giới đá

Lời: Dr. Stone là manga do Inagaki Riichiro viết, Boichi vẽ, đăng từ năm 2017 tới 2022. Bản anime kết thúc năm 202…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a small model rocket and a glass flask. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Một ngày, một luồng sáng xanh bí ẩn quét qua Trái Đất và biến toàn bộ loài người thành đá. Senku giữ được ý t…

```text
Wide 16:9 landscape cinematic frame. a wave of green light sweeping across a modern city, people frozen mid-step as stone statues. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Khi tỉnh dậy, cậu biết chính xác mình đã ở trong đá bao lâu. Và cậu bắt đầu làm những việc đầu tiên: tìm nước…

```text
Wide 16:9 landscape cinematic frame. a young scientist carving tally marks on a cave wall, a small campfire burning beside him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Câu cửa miệng của Senku là mười tỉ phần trăm, dùng mỗi khi cậu chắc chắn về một điều gì đó bằng khoa học.

```text
Wide 16:9 landscape cinematic frame. a big glowing number 10,000,000,000 percent written on a stone wall in chalk. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: điểm hay nhất của bộ này là mỗi phát minh đều dựa trên một phát minh trước đó. Không có gì từ t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot stacking small blocks labeled with simple icons into a staircase. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Thang đo của Kaku

Lời: Với mỗi phát minh, Kaku chấm ba thứ. Thứ nhất: khả thi hay không, với ba mức: làm được, làm được nhưng rất kh…

```text
Wide 16:9 landscape cinematic frame. three colored badges: green, yellow and red, each with a small icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Thứ hai: ngoài đời, loài người đã mất bao lâu để phát minh ra nó lần đầu tiên. Thứ ba: độ nguy hiểm nếu một n…

```text
Wide 16:9 landscape cinematic frame. an hourglass and a warning triangle placed next to the three badges. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhắc lại một lần nữa: Kaku sẽ không nói cách làm chi tiết. Nhiều phát minh dùng hóa chất và nhiệt độ có thể g…

```text
Wide 16:9 landscape cinematic frame. a locked cabinet of chemical bottles with a bold do-not-try sign on the door. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và thuốc thì tuyệt đối không tự chế. Thuốc thật cần được kiểm định bởi các chuyên gia và cơ quan y tế, không…

```text
Wide 16:9 landscape cinematic frame. a medicine bottle behind glass in a pharmacy, a stamp of approval on its label. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Phát minh 1: dung dịch hồi sinh

Lời: Phát minh đầu tiên của Senku là dung dịch phá lớp đá hóa. Trong truyện, nó được pha từ axit nitric và cồn.

```text
Wide 16:9 landscape cinematic frame. a small clay pot with a glowing liquid dripping onto a stone statue's crack. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Điều thú vị là hỗn hợp axit nitric pha trong cồn có thật ngoài đời. Nó được dùng trong ngành luyện kim để ăn…

```text
Wide 16:9 landscape cinematic frame. a metallurgy lab with a polished metal sample under a microscope, grain patterns visible. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Để có axit nitric, Senku phải tìm nguồn nitrat trong tự nhiên, như trong hang có nhiều phân dơi, rồi chế biến…

```text
Wide 16:9 landscape cinematic frame. a dark cave with bats hanging from the ceiling, a torch lighting the entrance. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhưng tất nhiên, ngoài đời không có lớp đá hóa nào để phá. Việc hóa đá con người và hồi sinh bằng dung dịch l…

```text
Wide 16:9 landscape cinematic frame. a stone statue in a park with a question mark hovering above it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Chấm điểm: khả thi, không thực tế, vì hiện tượng hóa đá không tồn tại. Độ nguy hiểm: rất cao, axit nitric có…

```text
Wide 16:9 landscape cinematic frame. a red badge and a large warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Phát minh 2: vôi từ vỏ sò

Lời: Tiếp theo là những phát minh cơ bản hơn, nhưng quan trọng không kém. Senku nung vỏ sò để tạo ra vôi.

```text
Wide 16:9 landscape cinematic frame. a pile of seashells beside a stone kiln glowing with heat. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Khoa học: vỏ sò chứa nhiều canxi cacbonat. Khi nung ở nhiệt độ cao, nó biến thành vôi sống. Vôi được dùng làm…

```text
Wide 16:9 landscape cinematic frame. a simple diagram of a shell turning into white powder in a kiln, arrows showing heat. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Ngoài đời, con người đã làm vôi từ hàng nghìn năm trước. Nhiều công trình cổ đại dùng vữa vôi và vẫn còn đứng…

```text
Wide 16:9 landscape cinematic frame. an ancient stone aqueduct standing tall under a blue sky. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Chấm điểm: làm được. Đây là công nghệ cổ xưa. Độ nguy hiểm: trung bình, vì vôi sống gây bỏng khi dính nước và…

```text
Wide 16:9 landscape cinematic frame. a green badge and a yellow warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Trong truyện, vôi còn là bước đệm để làm ra những thứ khác. Nhiều phản ứng hóa học quan trọng cần một chất ki…

```text
Wide 16:9 landscape cinematic frame. a row of clay jars labeled with simple icons, a bowl of white lime powder in the center. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nghe có vẻ tầm thường, nhưng không có vôi thì không có vữa, không có nhà vững, và không có nhiề…

```text
Wide 16:9 landscape cinematic frame. the owl mascot building a tiny stone wall with a little trowel. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Phát minh 3: xà phòng

Lời: Phát minh thứ ba giúp cả làng sống khỏe hơn: xà phòng.

```text
Wide 16:9 landscape cinematic frame. a bar of rough handmade soap on a wooden ledge beside a stream. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Khoa học: xà phòng được tạo ra khi chất béo phản ứng với một chất kiềm. Phản ứng này có tên là xà phòng hóa.…

```text
Wide 16:9 landscape cinematic frame. a diagram of fat droplets and ash combining into soap molecules, labeled simply. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Ngoài đời, có những bằng chứng về việc làm chất giống xà phòng từ gần năm nghìn năm trước ở vùng Lưỡng Hà cổ…

```text
Wide 16:9 landscape cinematic frame. an ancient clay tablet with carved symbols beside a small clay pot. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Xà phòng quan trọng hơn ta tưởng: rửa tay bằng xà phòng giúp giảm mạnh việc lây lan nhiều bệnh truyền nhiễm.…

```text
Wide 16:9 landscape cinematic frame. hands being washed with soap under running water, bubbles glowing softly. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Chấm điểm: làm được. Độ nguy hiểm: trung bình, vì dung dịch kiềm đậm đặc có thể gây bỏng da. Ngày nay mua xà…

```text
Wide 16:9 landscape cinematic frame. a green badge and a yellow warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Phát minh 4: thủy tinh

Lời: Muốn làm thí nghiệm hóa học thì phải có dụng cụ. Nên Senku làm thủy tinh.

```text
Wide 16:9 landscape cinematic frame. a glowing blob of molten glass on the end of a long pipe in a stone furnace. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Khoa học: thủy tinh thường được làm từ cát, một chất trợ chảy giúp hạ nhiệt độ nóng chảy, và vôi để thủy tinh…

```text
Wide 16:9 landscape cinematic frame. three small piles labeled sand, flux and lime beside a roaring furnace. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Để đạt nhiệt độ đó, cần một lò nung tốt và ống thổi để đưa thêm không khí vào lửa. Trong truyện, cả làng phải…

```text
Wide 16:9 landscape cinematic frame. several villagers pumping bellows in rhythm beside a glowing furnace. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Ngoài đời, thủy tinh đã được làm từ hơn bốn nghìn năm trước ở vùng Lưỡng Hà và Ai Cập cổ đại.

```text
Wide 16:9 landscape cinematic frame. ancient colorful glass beads and small vessels displayed in a museum case. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Chấm điểm: làm được nhưng rất khó, vì cần kiểm soát nhiệt độ rất cao. Độ nguy hiểm: cao, bỏng nhiệt và mảnh v…

```text
Wide 16:9 landscape cinematic frame. a yellow badge and a red warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một cái cốc thủy tinh bình thường trên bàn bạn là kết quả của bốn nghìn năm kinh nghiệm.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a glass cup up to the light, admiring it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Phát minh 5: thuốc kháng khuẩn

Lời: Đây là phát minh cảm động nhất ở mùa một: Senku chế thuốc kháng khuẩn để cứu một người đang bệnh nặng trong l…

```text
Wide 16:9 landscape cinematic frame. a village hut at night, a figure lying ill while others wait anxiously outside. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Trong truyện, đó là một loại thuốc thuộc nhóm sulfa. Ngoài đời, đây là nhóm thuốc kháng khuẩn tổng hợp đầu ti…

```text
Wide 16:9 landscape cinematic frame. an old pharmacy shelf from the 1930s with glass bottles and handwritten labels. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhà khoa học tìm ra hiệu quả của loại thuốc đầu tiên trong nhóm này được trao giải Nobel năm 1939. Trước đó,…

```text
Wide 16:9 landscape cinematic frame. a vintage award medal on a velvet cushion beside a stack of research notes. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Để làm ra nó, Senku phải đi qua cả một chuỗi dài: tạo ra nhiều hóa chất trung gian, từng bước một. Truyện cho…

```text
Wide 16:9 landscape cinematic frame. a long chain of glass flasks connected by tubes, villagers carrying materials along it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Chấm điểm: không thực tế với một người tự làm. Thuốc thật phải được sản xuất trong điều kiện kiểm soát, đúng…

```text
Wide 16:9 landscape cinematic frame. a red badge and a red warning triangle, and a doctor figure behind a pharmacy counter. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cảnh này cho thấy vì sao khoa học đáng quý. Một viên thuốc ngày nay ta mua dễ dàng là kết quả c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a small pill with great respect. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Phát minh 6: điện

Lời: Bước tiếp theo đưa làng đá vào một kỷ nguyên mới: điện.

```text
Wide 16:9 landscape cinematic frame. a simple hand-cranked generator with copper coils and a magnet on a wooden stand. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Khoa học: khi một nam châm chuyển động gần một cuộn dây đồng, dòng điện xuất hiện trong cuộn dây. Hiện tượng…

```text
Wide 16:9 landscape cinematic frame. a magnet moving through a coil of wire, small sparks of current shown flowing. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Trong truyện, cái khó nhất không phải nguyên lý, mà là làm ra dây đồng đủ dài và đủ mảnh, và làm ra nam châm…

```text
Wide 16:9 landscape cinematic frame. villagers pulling a thin copper wire through a hole in a metal plate, coils of wire stacked nearby. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Ngoài đời, từ lúc biết điện tới lúc có máy phát điện thực dụng mất hàng chục năm. Senku rút ngắn điều đó nhờ…

```text
Wide 16:9 landscape cinematic frame. a timeline of early electrical devices from a simple coil to a large generator. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Chấm điểm: làm được nhưng rất khó. Độ nguy hiểm: cao, điện giật và cháy. Kaku nhắc: dòng điện trong nhà bạn đ…

```text
Wide 16:9 landscape cinematic frame. a yellow badge and a red warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Phát minh 7: bóng đèn tre

Lời: Có điện rồi thì làm đèn. Và Senku chọn một nguyên liệu bất ngờ cho dây tóc bóng đèn: tre.

```text
Wide 16:9 landscape cinematic frame. a glass bulb glowing warmly with a thin carbonized bamboo filament inside. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Đây là một chi tiết lịch sử có thật. Những năm 1880, xưởng của Thomas Edison đã thử hàng nghìn vật liệu, và d…

```text
Wide 16:9 landscape cinematic frame. a vintage laboratory with rows of experimental bulbs and bundles of bamboo on a shelf. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Khoa học: dây tóc phải phát sáng khi nóng mà không cháy. Muốn vậy, bên trong bóng đèn phải gần như không có k…

```text
Wide 16:9 landscape cinematic frame. a cross-section of a bulb showing an empty vacuum inside and a glowing filament. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Chấm điểm: làm được nhưng rất khó, cái khó nhất là hút chân không. Độ nguy hiểm: trung bình, thủy tinh có thể…

```text
Wide 16:9 landscape cinematic frame. a yellow badge and a yellow warning triangle on a scorecard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ngày nay, bóng đèn dây tóc đã gần như được thay bằng đèn LED, tiết kiệm điện hơn rất nhiều. Nhưng nguyên lý đ…

```text
Wide 16:9 landscape cinematic frame. an old filament bulb beside a modern LED bulb on a table, both glowing. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: ánh sáng đầu tiên trong đêm của một thế giới đá. Cảnh đó trong anime khiến Kaku nổi da gà.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up at a single light bulb glowing in a dark forest village. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Phát minh 8: điện thoại và radio

Lời: Tiếp theo là liên lạc từ xa: điện thoại, rồi radio. Đây là những phát minh giúp vương quốc khoa học thắng đượ…

```text
Wide 16:9 landscape cinematic frame. two tin-can style telephones connected by a long wire across a forest. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Khoa học: điện thoại biến âm thanh thành tín hiệu điện rồi biến ngược lại. Radio đi xa hơn: truyền tín hiệu q…

```text
Wide 16:9 landscape cinematic frame. a diagram of sound waves turning into electrical signals and radio waves spreading from a tower. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Để làm radio, Senku cần những linh kiện rất khó như ống chân không, nam châm, dây dẫn và cả những tinh thể đặ…

```text
Wide 16:9 landscape cinematic frame. a wooden workbench cluttered with glass tubes, coils and crystals under lamplight. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Ngoài đời, từ điện thoại đầu tiên cuối thế kỷ mười chín tới radio phát sóng rộng rãi đầu thế kỷ hai mươi mất…

```text
Wide 16:9 landscape cinematic frame. a timeline with a vintage telephone on the left and an old radio set on the right. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Chấm điểm: làm được nhưng cực khó với một nhóm nhỏ. Độ nguy hiểm: trung bình. Kaku ghi chú: trong truyện, lời…

```text
Wide 16:9 landscape cinematic frame. the owl mascot speaking into an old microphone, sound waves spreading out. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Phát minh 9: tên lửa lên Mặt Trăng

Lời: Và phát minh cuối cùng, tham vọng nhất: một tên lửa đưa người lên Mặt Trăng, để tìm hiểu nguồn gốc của luồng…

```text
Wide 16:9 landscape cinematic frame. a tall rocket on a wooden launch tower at dawn, the moon faint in the sky. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Khoa học: tên lửa bay nhờ đẩy khí ra phía sau với tốc độ cực lớn, theo định luật ba của Newton. Nhưng để thoá…

```text
Wide 16:9 landscape cinematic frame. a diagram of exhaust pushing down and a rocket pushing up, with a small Newton's third law label. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ngoài đời, chương trình đưa người lên Mặt Trăng của Mỹ cần tới khoảng bốn trăm nghìn người làm việc cùng nhau…

```text
Wide 16:9 landscape cinematic frame. a huge crowd of engineers and workers silhouetted before a giant rocket. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Chấm điểm: không thực tế nếu bắt đầu từ con số không trong vài năm. Đây là phần khoa học viễn tưởng, nhưng là…

```text
Wide 16:9 landscape cinematic frame. a red badge on a scorecard beside a small moon icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: truyện rất thông minh khi để việc lên Mặt Trăng là cái đích cuối cùng. Nó cho thấy mọi thứ trướ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at the top of a staircase of small inventions, looking at the moon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Cây công nghệ: vì sao thứ tự quan trọng

Lời: Trước khi xếp bảng, hãy nhìn các phát minh như một cây công nghệ trong game chiến thuật. Mỗi ô chỉ mở được kh…

```text
Wide 16:9 landscape cinematic frame. a game-style technology tree drawn on parchment, glowing nodes connected by lines. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Có lửa thì mới nung được vôi và thủy tinh. Có thủy tinh thì mới có dụng cụ để làm hóa học. Có hóa học thì mới…

```text
Wide 16:9 landscape cinematic frame. the first branches of the tree lighting up: flame, shell, glass, flask. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Có kim loại và nam châm thì mới có điện. Có điện thì mới có đèn, điện thoại và radio. Và có tất cả những thứ…

```text
Wide 16:9 landscape cinematic frame. the upper branches lighting up: magnet, bulb, radio, and at the top a small rocket. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Senku luôn biết mình đang ở ô nào và ô tiếp theo cần gì. Đó là lý do cậu không bao giờ cố làm radio khi còn c…

```text
Wide 16:9 landscape cinematic frame. a young scientist pointing at the next node on a glowing tree while villagers watch. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây cũng là cách học rất tốt ngoài đời. Muốn giỏi một thứ khó, hãy tìm xem nó đứng trên những t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot climbing a small tree of glowing nodes, branch by branch. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Thời gian thật và thời gian trong truyện

Lời: Loài người thật mất bao lâu để đi từ lửa tới tên lửa? Hàng chục nghìn năm, nếu tính từ những đống lửa đầu tiê…

```text
Wide 16:9 landscape cinematic frame. a very long timeline scroll next to a tiny calendar with only a few pages. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Có ba lý do khiến truyện nhanh như vậy. Một: Senku đã biết câu trả lời, không phải thử sai hàng nghìn lần như…

```text
Wide 16:9 landscape cinematic frame. a scientist walking straight through a maze while others wander its paths. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hai: cậu có rất nhiều người giúp, và những người đó học rất nhanh. Ba: truyện cần nhịp nhanh để hấp dẫn, nên…

```text
Wide 16:9 landscape cinematic frame. a busy workshop montage with villagers learning new skills at a rapid pace. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nhưng cũng có những thứ Senku không thể rút ngắn: chờ nguyên liệu, chờ lò đủ nóng, chờ người bệnh hồi phục. T…

```text
Wide 16:9 landscape cinematic frame. an hourglass placed next to a slowly heating furnace and a sleeping patient. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: biết trước câu trả lời giúp đi nhanh gấp trăm lần. Đó là sức mạnh thật sự của giáo dục.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a textbook like a treasure map. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Bảng khả thi

Lời: Giờ xếp tất cả lên bảng. Làm được: vôi từ vỏ sò, xà phòng. Đây là công nghệ hàng nghìn năm tuổi.

```text
Wide 16:9 landscape cinematic frame. a chart with green badges next to a seashell and a soap bar. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Làm được nhưng rất khó: thủy tinh, điện, bóng đèn tre, điện thoại và radio. Nguyên lý đơn giản, nhưng làm ra…

```text
Wide 16:9 landscape cinematic frame. yellow badges next to a glass cup, a coil, a bulb and a radio. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Không thực tế: dung dịch phá đá hóa, vì hiện tượng không có thật, thuốc tự chế, vì quá nguy hiểm, và tên lửa…

```text
Wide 16:9 landscape cinematic frame. red badges next to a stone statue, a pill bottle and a rocket. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Vậy Dr. Stone có thật không? Kaku chấm: phần lớn nguyên lý là thật, còn tốc độ thì được đẩy nhanh hơn thực tế…

```text
Wide 16:9 landscape cinematic frame. a large stamp reading REAL PRINCIPLES, FAST FORWARD on the chart. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Góc nhìn của Kaku: khoa học là cầu thang · **Kaku** (đính kèm ảnh mẫu)

Lời: Có một câu nói nổi tiếng của Isaac Newton: nếu tôi nhìn được xa hơn, đó là nhờ tôi đứng trên vai những người…

```text
Wide 16:9 landscape cinematic frame. a small figure standing on the shoulders of a towering statue, looking far into the distance. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Senku làm được mọi thứ vì cậu mang trong đầu kiến thức của hàng nghìn năm loài người. Cậu không phát minh lại…

```text
Wide 16:9 landscape cinematic frame. a glowing path of footprints stretching back through history behind a young scientist. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Và truyện cũng cho thấy một mình Senku không làm được gì. Cần người thợ làm dây, người thổi lửa, người đi tìm…

```text
Wide 16:9 landscape cinematic frame. a whole village working together at different stations of a rustic workshop. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Kaku nghĩ đó là thông điệp đẹp nhất: mọi thứ ta dùng mỗi ngày, từ cốc thủy tinh tới bóng đèn, là món quà của…

```text
Wide 16:9 landscape cinematic frame. a modern kitchen with a glass cup, a light bulb and a bar of soap, softly lit. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và muốn đi tiếp, ta chỉ cần làm điều Senku làm: tò mò, kiên nhẫn, và đi từng bậc một.

```text
Wide 16:9 landscape cinematic frame. a single step of a staircase glowing in the dark, ready to be climbed. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Tóm lại: nhiều phát minh trong Dr. Stone dựa trên khoa học và lịch sử có thật, từ vôi, xà phòng, thủy tinh ch…

```text
Wide 16:9 landscape cinematic frame. a summary board of inventions from a seashell to a rocket, connected by arrows. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu tỉnh dậy sau ba nghìn bảy trăm năm, thứ đầu tiên bạn muốn làm lại là gì? Kaku thì chọn x…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a bar of soap proudly, bubbles floating around. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tới, Kaku đổi sang một thế giới khác hẳn: hậu cung, thuốc men và những vụ bí ẩn trong Dược sư tự sự, bộ…

```text
Wide 16:9 landscape cinematic frame. an elegant palace courtyard at night with lanterns and a small herb basket on a bench. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Kaku tháo kính bảo hộ đây. Mười tỉ phần trăm hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off safety goggles and waving in a rustic lab. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thế giới đá

Khoảng 112 giây · cảnh s01–s10 · 1459 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Dr. Stone tới hết anime, kể cả mùa cuối phát năm 2026. Và một cảnh báo quan trọng hơn: video chỉ nói nguyên lý khoa học, không phải hướng dẫn. Nhiều thứ trong video rất nguy hiểm nếu tự làm.

<short pause> Hãy tưởng tượng bạn tỉnh dậy sau ba nghìn bảy trăm năm. Mọi thành phố đã thành rừng. Không điện, không thuốc, không cả một cục xà phòng. Chỉ có bạn và những gì bạn nhớ trong đầu.

<short pause> Đó là tình cảnh của Senku, nhân vật chính của Dr. Stone. Và cậu quyết định xây lại toàn bộ nền văn minh, từ con số không, chỉ bằng khoa học.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku, và hôm nay Kaku hỏi một câu thôi: những phát minh của Senku, ngoài đời thật có làm được không, và mất bao lâu?

<short pause> Cuối video, Kaku sẽ xếp tất cả lên một bảng khả thi, từ dễ như nấu ăn tới khó như lên Mặt Trăng.

<short pause> Dr. Stone là manga do Inagaki Riichiro viết, Boichi vẽ, đăng từ năm 2017 tới 2022. Bản anime kết thúc năm 2026 với mùa cuối có tên Science Future.

<short pause> Một ngày, một luồng sáng xanh bí ẩn quét qua Trái Đất và biến toàn bộ loài người thành đá. Senku giữ được ý thức bằng cách đếm từng giây, suốt hàng nghìn năm.

<short pause> Khi tỉnh dậy, cậu biết chính xác mình đã ở trong đá bao lâu. Và cậu bắt đầu làm những việc đầu tiên: tìm nước, tìm lửa, rồi tìm cách hồi sinh người khác.

<short pause> Câu cửa miệng của Senku là mười tỉ phần trăm, dùng mỗi khi cậu chắc chắn về một điều gì đó bằng khoa học.

<short pause> Kaku ghi chú: điểm hay nhất của bộ này là mỗi phát minh đều dựa trên một phát minh trước đó. Không có gì từ trên trời rơi xuống.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Dr. Stone tới hết anime, kể cả mùa cuối phát năm 2026. Và một cảnh báo quan trọng hơn: video chỉ nói nguyên lý khoa học, không phải hướng dẫn. Nhiều thứ trong video rất nguy hiểm nếu tự làm.

[pause] Hãy tưởng tượng bạn tỉnh dậy sau ba nghìn bảy trăm năm. Mọi thành phố đã thành rừng. Không điện, không thuốc, không cả một cục xà phòng. Chỉ có bạn và những gì bạn nhớ trong đầu.

[pause] Đó là tình cảnh của Senku, nhân vật chính của Dr. Stone. Và cậu quyết định xây lại toàn bộ nền văn minh, từ con số không, chỉ bằng khoa học.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku, và hôm nay Kaku hỏi một câu thôi: những phát minh của Senku, ngoài đời thật có làm được không, và mất bao lâu?

[pause] Cuối video, Kaku sẽ xếp tất cả lên một bảng khả thi, từ dễ như nấu ăn tới khó như lên Mặt Trăng.

[pause] Dr. Stone là manga do Inagaki Riichiro viết, Boichi vẽ, đăng từ năm 2017 tới 2022. Bản anime kết thúc năm 2026 với mùa cuối có tên Science Future.

[pause] Một ngày, một luồng sáng xanh bí ẩn quét qua Trái Đất và biến toàn bộ loài người thành đá. Senku giữ được ý thức bằng cách đếm từng giây, suốt hàng nghìn năm.

[pause] Khi tỉnh dậy, cậu biết chính xác mình đã ở trong đá bao lâu. Và cậu bắt đầu làm những việc đầu tiên: tìm nước, tìm lửa, rồi tìm cách hồi sinh người khác.

[pause] Câu cửa miệng của Senku là mười tỉ phần trăm, dùng mỗi khi cậu chắc chắn về một điều gì đó bằng khoa học.

[pause] Kaku ghi chú: điểm hay nhất của bộ này là mỗi phát minh đều dựa trên một phát minh trước đó. Không có gì từ trên trời rơi xuống.
```

### c02 · Thang đo của Kaku / Phát minh 1: dung dịch hồi sinh

Khoảng 97 giây · cảnh s11–s19 · 1267 ký tự

**Gemini**

```text
Với mỗi phát minh, Kaku chấm ba thứ. Thứ nhất: khả thi hay không, với ba mức: làm được, làm được nhưng rất khó, và không thực tế.

<short pause> Thứ hai: ngoài đời, loài người đã mất bao lâu để phát minh ra nó lần đầu tiên. Thứ ba: độ nguy hiểm nếu một người bình thường tự làm.

<short pause> Nhắc lại một lần nữa: Kaku sẽ không nói cách làm chi tiết. Nhiều phát minh dùng hóa chất và nhiệt độ có thể gây bỏng, ngộ độc hay cháy nổ.

<short pause> Và thuốc thì tuyệt đối không tự chế. Thuốc thật cần được kiểm định bởi các chuyên gia và cơ quan y tế, không phải bởi một người trong phim hoạt hình.

<short pause> Phát minh đầu tiên của Senku là dung dịch phá lớp đá hóa. Trong truyện, nó được pha từ axit nitric và cồn.

<short pause> Điều thú vị là hỗn hợp axit nitric pha trong cồn có thật ngoài đời. Nó được dùng trong ngành luyện kim để ăn mòn nhẹ bề mặt kim loại, giúp soi rõ cấu trúc bên trong dưới kính hiển vi.

<short pause> Để có axit nitric, Senku phải tìm nguồn nitrat trong tự nhiên, như trong hang có nhiều phân dơi, rồi chế biến qua nhiều bước.

<short pause> Nhưng tất nhiên, ngoài đời không có lớp đá hóa nào để phá. Việc hóa đá con người và hồi sinh bằng dung dịch là phần khoa học viễn tưởng của truyện.

<short pause> Chấm điểm: khả thi, không thực tế, vì hiện tượng hóa đá không tồn tại. Độ nguy hiểm: rất cao, axit nitric có thể gây bỏng nặng. Kaku khuyên bạn đứng thật xa.
```

**ElevenLabs**

```text
Với mỗi phát minh, Kaku chấm ba thứ. Thứ nhất: khả thi hay không, với ba mức: làm được, làm được nhưng rất khó, và không thực tế.

[pause] Thứ hai: ngoài đời, loài người đã mất bao lâu để phát minh ra nó lần đầu tiên. Thứ ba: độ nguy hiểm nếu một người bình thường tự làm.

[pause] Nhắc lại một lần nữa: Kaku sẽ không nói cách làm chi tiết. Nhiều phát minh dùng hóa chất và nhiệt độ có thể gây bỏng, ngộ độc hay cháy nổ.

[pause] Và thuốc thì tuyệt đối không tự chế. Thuốc thật cần được kiểm định bởi các chuyên gia và cơ quan y tế, không phải bởi một người trong phim hoạt hình.

[pause] Phát minh đầu tiên của Senku là dung dịch phá lớp đá hóa. Trong truyện, nó được pha từ axit nitric và cồn.

[pause] Điều thú vị là hỗn hợp axit nitric pha trong cồn có thật ngoài đời. Nó được dùng trong ngành luyện kim để ăn mòn nhẹ bề mặt kim loại, giúp soi rõ cấu trúc bên trong dưới kính hiển vi.

[pause] Để có axit nitric, Senku phải tìm nguồn nitrat trong tự nhiên, như trong hang có nhiều phân dơi, rồi chế biến qua nhiều bước.

[pause] Nhưng tất nhiên, ngoài đời không có lớp đá hóa nào để phá. Việc hóa đá con người và hồi sinh bằng dung dịch là phần khoa học viễn tưởng của truyện.

[pause] Chấm điểm: khả thi, không thực tế, vì hiện tượng hóa đá không tồn tại. Độ nguy hiểm: rất cao, axit nitric có thể gây bỏng nặng. Kaku khuyên bạn đứng thật xa.
```

### c03 · Phát minh 2: vôi từ vỏ sò / Phát minh 3: xà phòng

Khoảng 112 giây · cảnh s20–s30 · 1460 ký tự

**Gemini**

```text
Tiếp theo là những phát minh cơ bản hơn, nhưng quan trọng không kém. Senku nung vỏ sò để tạo ra vôi.

<short pause> Khoa học: vỏ sò chứa nhiều canxi cacbonat. Khi nung ở nhiệt độ cao, nó biến thành vôi sống. Vôi được dùng làm vữa xây, quét tường, và làm nguyên liệu cho nhiều phản ứng khác.

<short pause> Ngoài đời, con người đã làm vôi từ hàng nghìn năm trước. Nhiều công trình cổ đại dùng vữa vôi và vẫn còn đứng tới ngày nay.

<short pause> Chấm điểm: làm được. Đây là công nghệ cổ xưa. Độ nguy hiểm: trung bình, vì vôi sống gây bỏng khi dính nước và có thể làm tổn thương mắt.

<short pause> Trong truyện, vôi còn là bước đệm để làm ra những thứ khác. Nhiều phản ứng hóa học quan trọng cần một chất kiềm, và vôi là chất kiềm dễ kiếm nhất ở một thế giới đá.

<short pause> <laugh> Kaku ghi chú: nghe có vẻ tầm thường, nhưng không có vôi thì không có vữa, không có nhà vững, và không có nhiều phản ứng hóa học sau này.

<short pause> Phát minh thứ ba giúp cả làng sống khỏe hơn: xà phòng.

<short pause> Khoa học: xà phòng được tạo ra khi chất béo phản ứng với một chất kiềm. Phản ứng này có tên là xà phòng hóa. Ngày xưa, người ta lấy chất kiềm từ tro gỗ.

<short pause> Ngoài đời, có những bằng chứng về việc làm chất giống xà phòng từ gần năm nghìn năm trước ở vùng Lưỡng Hà cổ đại.

<short pause> Xà phòng quan trọng hơn ta tưởng: rửa tay bằng xà phòng giúp giảm mạnh việc lây lan nhiều bệnh truyền nhiễm. Ở một thế giới không có thuốc, nó là tấm khiên đầu tiên.

<short pause> Chấm điểm: làm được. Độ nguy hiểm: trung bình, vì dung dịch kiềm đậm đặc có thể gây bỏng da. Ngày nay mua xà phòng vẫn an toàn và rẻ hơn nhiều.
```

**ElevenLabs**

```text
Tiếp theo là những phát minh cơ bản hơn, nhưng quan trọng không kém. Senku nung vỏ sò để tạo ra vôi.

[pause] Khoa học: vỏ sò chứa nhiều canxi cacbonat. Khi nung ở nhiệt độ cao, nó biến thành vôi sống. Vôi được dùng làm vữa xây, quét tường, và làm nguyên liệu cho nhiều phản ứng khác.

[pause] Ngoài đời, con người đã làm vôi từ hàng nghìn năm trước. Nhiều công trình cổ đại dùng vữa vôi và vẫn còn đứng tới ngày nay.

[pause] Chấm điểm: làm được. Đây là công nghệ cổ xưa. Độ nguy hiểm: trung bình, vì vôi sống gây bỏng khi dính nước và có thể làm tổn thương mắt.

[pause] Trong truyện, vôi còn là bước đệm để làm ra những thứ khác. Nhiều phản ứng hóa học quan trọng cần một chất kiềm, và vôi là chất kiềm dễ kiếm nhất ở một thế giới đá.

[pause] [chuckles] Kaku ghi chú: nghe có vẻ tầm thường, nhưng không có vôi thì không có vữa, không có nhà vững, và không có nhiều phản ứng hóa học sau này.

[pause] Phát minh thứ ba giúp cả làng sống khỏe hơn: xà phòng.

[pause] Khoa học: xà phòng được tạo ra khi chất béo phản ứng với một chất kiềm. Phản ứng này có tên là xà phòng hóa. Ngày xưa, người ta lấy chất kiềm từ tro gỗ.

[pause] Ngoài đời, có những bằng chứng về việc làm chất giống xà phòng từ gần năm nghìn năm trước ở vùng Lưỡng Hà cổ đại.

[pause] Xà phòng quan trọng hơn ta tưởng: rửa tay bằng xà phòng giúp giảm mạnh việc lây lan nhiều bệnh truyền nhiễm. Ở một thế giới không có thuốc, nó là tấm khiên đầu tiên.

[pause] Chấm điểm: làm được. Độ nguy hiểm: trung bình, vì dung dịch kiềm đậm đặc có thể gây bỏng da. Ngày nay mua xà phòng vẫn an toàn và rẻ hơn nhiều.
```

### c04 · Phát minh 4: thủy tinh / Phát minh 5: thuốc kháng khuẩn

Khoảng 122 giây · cảnh s31–s42 · 1586 ký tự

**Gemini**

```text
Muốn làm thí nghiệm hóa học thì phải có dụng cụ. Nên Senku làm thủy tinh.

<short pause> Khoa học: thủy tinh thường được làm từ cát, một chất trợ chảy giúp hạ nhiệt độ nóng chảy, và vôi để thủy tinh bền hơn. Tất cả được nung tới nhiệt độ hơn một nghìn độ C.

<short pause> Để đạt nhiệt độ đó, cần một lò nung tốt và ống thổi để đưa thêm không khí vào lửa. Trong truyện, cả làng phải thay nhau thổi.

<short pause> Ngoài đời, thủy tinh đã được làm từ hơn bốn nghìn năm trước ở vùng Lưỡng Hà và Ai Cập cổ đại.

<short pause> Chấm điểm: làm được nhưng rất khó, vì cần kiểm soát nhiệt độ rất cao. Độ nguy hiểm: cao, bỏng nhiệt và mảnh vỡ sắc.

<short pause> <laugh> Kaku ghi chú: một cái cốc thủy tinh bình thường trên bàn bạn là kết quả của bốn nghìn năm kinh nghiệm.

<short pause> Đây là phát minh cảm động nhất ở mùa một: Senku chế thuốc kháng khuẩn để cứu một người đang bệnh nặng trong làng.

<short pause> Trong truyện, đó là một loại thuốc thuộc nhóm sulfa. Ngoài đời, đây là nhóm thuốc kháng khuẩn tổng hợp đầu tiên được dùng rộng rãi, xuất hiện vào những năm 1930.

<short pause> Nhà khoa học tìm ra hiệu quả của loại thuốc đầu tiên trong nhóm này được trao giải Nobel năm 1939. Trước đó, một vết nhiễm trùng nhỏ cũng có thể gây chết người.

<short pause> Để làm ra nó, Senku phải đi qua cả một chuỗi dài: tạo ra nhiều hóa chất trung gian, từng bước một. Truyện cho thấy cả làng phải góp sức rất lâu.

<short pause> Chấm điểm: không thực tế với một người tự làm. Thuốc thật phải được sản xuất trong điều kiện kiểm soát, đúng liều, đúng độ tinh khiết. Độ nguy hiểm: cực cao. Nhắc lại: không bao giờ tự chế thuốc.

<short pause> Kaku ghi chú: cảnh này cho thấy vì sao khoa học đáng quý. Một viên thuốc ngày nay ta mua dễ dàng là kết quả của hàng chục năm nghiên cứu.
```

**ElevenLabs**

```text
Muốn làm thí nghiệm hóa học thì phải có dụng cụ. Nên Senku làm thủy tinh.

[pause] Khoa học: thủy tinh thường được làm từ cát, một chất trợ chảy giúp hạ nhiệt độ nóng chảy, và vôi để thủy tinh bền hơn. Tất cả được nung tới nhiệt độ hơn một nghìn độ C.

[pause] Để đạt nhiệt độ đó, cần một lò nung tốt và ống thổi để đưa thêm không khí vào lửa. Trong truyện, cả làng phải thay nhau thổi.

[pause] Ngoài đời, thủy tinh đã được làm từ hơn bốn nghìn năm trước ở vùng Lưỡng Hà và Ai Cập cổ đại.

[pause] Chấm điểm: làm được nhưng rất khó, vì cần kiểm soát nhiệt độ rất cao. Độ nguy hiểm: cao, bỏng nhiệt và mảnh vỡ sắc.

[pause] [chuckles] Kaku ghi chú: một cái cốc thủy tinh bình thường trên bàn bạn là kết quả của bốn nghìn năm kinh nghiệm.

[pause] Đây là phát minh cảm động nhất ở mùa một: Senku chế thuốc kháng khuẩn để cứu một người đang bệnh nặng trong làng.

[pause] Trong truyện, đó là một loại thuốc thuộc nhóm sulfa. Ngoài đời, đây là nhóm thuốc kháng khuẩn tổng hợp đầu tiên được dùng rộng rãi, xuất hiện vào những năm 1930.

[pause] Nhà khoa học tìm ra hiệu quả của loại thuốc đầu tiên trong nhóm này được trao giải Nobel năm 1939. Trước đó, một vết nhiễm trùng nhỏ cũng có thể gây chết người.

[pause] Để làm ra nó, Senku phải đi qua cả một chuỗi dài: tạo ra nhiều hóa chất trung gian, từng bước một. Truyện cho thấy cả làng phải góp sức rất lâu.

[pause] Chấm điểm: không thực tế với một người tự làm. Thuốc thật phải được sản xuất trong điều kiện kiểm soát, đúng liều, đúng độ tinh khiết. Độ nguy hiểm: cực cao. Nhắc lại: không bao giờ tự chế thuốc.

[pause] Kaku ghi chú: cảnh này cho thấy vì sao khoa học đáng quý. Một viên thuốc ngày nay ta mua dễ dàng là kết quả của hàng chục năm nghiên cứu.
```

### c05 · Phát minh 6: điện / Phát minh 7: bóng đèn tre

Khoảng 115 giây · cảnh s43–s53 · 1500 ký tự

**Gemini**

```text
Bước tiếp theo đưa làng đá vào một kỷ nguyên mới: điện.

<short pause> Khoa học: khi một nam châm chuyển động gần một cuộn dây đồng, dòng điện xuất hiện trong cuộn dây. Hiện tượng này gọi là cảm ứng điện từ, được Faraday phát hiện năm 1831.

<short pause> Trong truyện, cái khó nhất không phải nguyên lý, mà là làm ra dây đồng đủ dài và đủ mảnh, và làm ra nam châm đủ mạnh.

<short pause> Ngoài đời, từ lúc biết điện tới lúc có máy phát điện thực dụng mất hàng chục năm. Senku rút ngắn điều đó nhờ biết trước câu trả lời.

<short pause> Chấm điểm: làm được nhưng rất khó. Độ nguy hiểm: cao, điện giật và cháy. Kaku nhắc: dòng điện trong nhà bạn đủ mạnh để gây chết người.

<short pause> Có điện rồi thì làm đèn. Và Senku chọn một nguyên liệu bất ngờ cho dây tóc bóng đèn: tre.

<short pause> Đây là một chi tiết lịch sử có thật. Những năm 1880, xưởng của Thomas Edison đã thử hàng nghìn vật liệu, và dùng sợi tre cacbon hóa từ Nhật Bản làm dây tóc, cho bóng đèn sáng hơn một nghìn giờ.

<short pause> Khoa học: dây tóc phải phát sáng khi nóng mà không cháy. Muốn vậy, bên trong bóng đèn phải gần như không có không khí, vì không có khí oxy thì dây tóc không bị đốt cháy.

<short pause> Chấm điểm: làm được nhưng rất khó, cái khó nhất là hút chân không. Độ nguy hiểm: trung bình, thủy tinh có thể vỡ và điện có thể gây giật.

<short pause> Ngày nay, bóng đèn dây tóc đã gần như được thay bằng đèn LED, tiết kiệm điện hơn rất nhiều. <short pause> Nhưng nguyên lý đầu tiên, làm một sợi dây phát sáng khi nóng, vẫn là cột mốc đưa loài người ra khỏi bóng tối.

<short pause> <laugh> Kaku ghi chú: ánh sáng đầu tiên trong đêm của một thế giới đá. Cảnh đó trong anime khiến Kaku nổi da gà.
```

**ElevenLabs**

```text
Bước tiếp theo đưa làng đá vào một kỷ nguyên mới: điện.

[pause] Khoa học: khi một nam châm chuyển động gần một cuộn dây đồng, dòng điện xuất hiện trong cuộn dây. Hiện tượng này gọi là cảm ứng điện từ, được Faraday phát hiện năm 1831.

[pause] Trong truyện, cái khó nhất không phải nguyên lý, mà là làm ra dây đồng đủ dài và đủ mảnh, và làm ra nam châm đủ mạnh.

[pause] Ngoài đời, từ lúc biết điện tới lúc có máy phát điện thực dụng mất hàng chục năm. Senku rút ngắn điều đó nhờ biết trước câu trả lời.

[pause] Chấm điểm: làm được nhưng rất khó. Độ nguy hiểm: cao, điện giật và cháy. Kaku nhắc: dòng điện trong nhà bạn đủ mạnh để gây chết người.

[pause] Có điện rồi thì làm đèn. Và Senku chọn một nguyên liệu bất ngờ cho dây tóc bóng đèn: tre.

[pause] Đây là một chi tiết lịch sử có thật. Những năm 1880, xưởng của Thomas Edison đã thử hàng nghìn vật liệu, và dùng sợi tre cacbon hóa từ Nhật Bản làm dây tóc, cho bóng đèn sáng hơn một nghìn giờ.

[pause] Khoa học: dây tóc phải phát sáng khi nóng mà không cháy. Muốn vậy, bên trong bóng đèn phải gần như không có không khí, vì không có khí oxy thì dây tóc không bị đốt cháy.

[pause] Chấm điểm: làm được nhưng rất khó, cái khó nhất là hút chân không. Độ nguy hiểm: trung bình, thủy tinh có thể vỡ và điện có thể gây giật.

[pause] Ngày nay, bóng đèn dây tóc đã gần như được thay bằng đèn LED, tiết kiệm điện hơn rất nhiều. [pause] Nhưng nguyên lý đầu tiên, làm một sợi dây phát sáng khi nóng, vẫn là cột mốc đưa loài người ra khỏi bóng tối.

[pause] [chuckles] Kaku ghi chú: ánh sáng đầu tiên trong đêm của một thế giới đá. Cảnh đó trong anime khiến Kaku nổi da gà.
```

### c06 · Phát minh 8: điện thoại và radio / Phát minh 9: tên lửa lên Mặt Trăng

Khoảng 120 giây · cảnh s54–s63 · 1561 ký tự

**Gemini**

```text
Tiếp theo là liên lạc từ xa: điện thoại, rồi radio. Đây là những phát minh giúp vương quốc khoa học thắng được một cuộc chiến mà không cần sức mạnh cơ bắp.

<short pause> Khoa học: điện thoại biến âm thanh thành tín hiệu điện rồi biến ngược lại. Radio đi xa hơn: truyền tín hiệu qua sóng vô tuyến, không cần dây.

<short pause> Để làm radio, Senku cần những linh kiện rất khó như ống chân không, nam châm, dây dẫn và cả những tinh thể đặc biệt. Mỗi thứ là một phát minh riêng.

<short pause> Ngoài đời, từ điện thoại đầu tiên cuối thế kỷ mười chín tới radio phát sóng rộng rãi đầu thế kỷ hai mươi mất vài chục năm, với rất nhiều nhà phát minh.

<short pause> Chấm điểm: làm được nhưng cực khó với một nhóm nhỏ. Độ nguy hiểm: trung bình. <laugh> Kaku ghi chú: trong truyện, lời nói qua radio có lúc mạnh hơn cả vũ khí.

<short pause> Và phát minh cuối cùng, tham vọng nhất: một tên lửa đưa người lên Mặt Trăng, để tìm hiểu nguồn gốc của luồng sáng hóa đá.

<short pause> Khoa học: tên lửa bay nhờ đẩy khí ra phía sau với tốc độ cực lớn, theo định luật ba của Newton. <short pause> Nhưng để thoát khỏi lực hút Trái Đất, cần năng lượng khổng lồ và vật liệu cực bền.

<short pause> Ngoài đời, chương trình đưa người lên Mặt Trăng của Mỹ cần tới khoảng bốn trăm nghìn người làm việc cùng nhau trong nhiều năm, với nền công nghiệp của cả một quốc gia.

<short pause> Chấm điểm: không thực tế nếu bắt đầu từ con số không trong vài năm. Đây là phần khoa học viễn tưởng, nhưng là viễn tưởng dựa trên đúng con đường mà loài người thật đã đi.

<short pause> Kaku ghi chú: truyện rất thông minh khi để việc lên Mặt Trăng là cái đích cuối cùng. Nó cho thấy mọi thứ trước đó, từ vôi, xà phòng, thủy tinh, tất cả đều là bậc thang dẫn tới đây.
```

**ElevenLabs**

```text
Tiếp theo là liên lạc từ xa: điện thoại, rồi radio. Đây là những phát minh giúp vương quốc khoa học thắng được một cuộc chiến mà không cần sức mạnh cơ bắp.

[pause] Khoa học: điện thoại biến âm thanh thành tín hiệu điện rồi biến ngược lại. Radio đi xa hơn: truyền tín hiệu qua sóng vô tuyến, không cần dây.

[pause] Để làm radio, Senku cần những linh kiện rất khó như ống chân không, nam châm, dây dẫn và cả những tinh thể đặc biệt. Mỗi thứ là một phát minh riêng.

[pause] Ngoài đời, từ điện thoại đầu tiên cuối thế kỷ mười chín tới radio phát sóng rộng rãi đầu thế kỷ hai mươi mất vài chục năm, với rất nhiều nhà phát minh.

[pause] Chấm điểm: làm được nhưng cực khó với một nhóm nhỏ. Độ nguy hiểm: trung bình. [chuckles] Kaku ghi chú: trong truyện, lời nói qua radio có lúc mạnh hơn cả vũ khí.

[pause] Và phát minh cuối cùng, tham vọng nhất: một tên lửa đưa người lên Mặt Trăng, để tìm hiểu nguồn gốc của luồng sáng hóa đá.

[pause] Khoa học: tên lửa bay nhờ đẩy khí ra phía sau với tốc độ cực lớn, theo định luật ba của Newton. [pause] Nhưng để thoát khỏi lực hút Trái Đất, cần năng lượng khổng lồ và vật liệu cực bền.

[pause] Ngoài đời, chương trình đưa người lên Mặt Trăng của Mỹ cần tới khoảng bốn trăm nghìn người làm việc cùng nhau trong nhiều năm, với nền công nghiệp của cả một quốc gia.

[pause] Chấm điểm: không thực tế nếu bắt đầu từ con số không trong vài năm. Đây là phần khoa học viễn tưởng, nhưng là viễn tưởng dựa trên đúng con đường mà loài người thật đã đi.

[pause] Kaku ghi chú: truyện rất thông minh khi để việc lên Mặt Trăng là cái đích cuối cùng. Nó cho thấy mọi thứ trước đó, từ vôi, xà phòng, thủy tinh, tất cả đều là bậc thang dẫn tới đây.
```

### c07 · Cây công nghệ: vì sao thứ tự quan trọng / Thời gian thật và thời gian trong truyện / Bảng khả thi

Khoảng 142 giây · cảnh s64–s77 · 1846 ký tự

**Gemini**

```text
Trước khi xếp bảng, hãy nhìn các phát minh như một cây công nghệ trong game chiến thuật. Mỗi ô chỉ mở được khi ô trước đã mở.

<short pause> Có lửa thì mới nung được vôi và thủy tinh. Có thủy tinh thì mới có dụng cụ để làm hóa học. Có hóa học thì mới có thuốc và vật liệu mới.

<short pause> Có kim loại và nam châm thì mới có điện. Có điện thì mới có đèn, điện thoại và radio. Và có tất cả những thứ đó, cộng với nhiên liệu và máy móc, mới nghĩ tới chuyện lên trời.

<short pause> Senku luôn biết mình đang ở ô nào và ô tiếp theo cần gì. Đó là lý do cậu không bao giờ cố làm radio khi còn chưa có thủy tinh.

<short pause> <laugh> Kaku ghi chú: đây cũng là cách học rất tốt ngoài đời. Muốn giỏi một thứ khó, hãy tìm xem nó đứng trên những thứ dễ hơn nào.

<short pause> Loài người thật mất bao lâu để đi từ lửa tới tên lửa? Hàng chục nghìn năm, nếu tính từ những đống lửa đầu tiên. Còn Senku chỉ mất vài năm.

<short pause> Có ba lý do khiến truyện nhanh như vậy. Một: Senku đã biết câu trả lời, không phải thử sai hàng nghìn lần như những nhà phát minh thật.

<short pause> Hai: cậu có rất nhiều người giúp, và những người đó học rất nhanh. Ba: truyện cần nhịp nhanh để hấp dẫn, nên nhiều bước bị lược đi.

<short pause> Nhưng cũng có những thứ Senku không thể rút ngắn: chờ nguyên liệu, chờ lò đủ nóng, chờ người bệnh hồi phục. Truyện vẫn tôn trọng những giới hạn đó.

<short pause> Kaku ghi chú: biết trước câu trả lời giúp đi nhanh gấp trăm lần. Đó là sức mạnh thật sự của giáo dục.

<short pause> Giờ xếp tất cả lên bảng. Làm được: vôi từ vỏ sò, xà phòng. Đây là công nghệ hàng nghìn năm tuổi.

<short pause> Làm được nhưng rất khó: thủy tinh, điện, bóng đèn tre, điện thoại và radio. Nguyên lý đơn giản, nhưng làm ra thì cần kỹ năng, dụng cụ và rất nhiều người.

<short pause> Không thực tế: dung dịch phá đá hóa, vì hiện tượng không có thật, thuốc tự chế, vì quá nguy hiểm, và tên lửa lên Mặt Trăng trong vài năm.

<short pause> Vậy Dr. Stone có thật không? Kaku chấm: phần lớn nguyên lý là thật, còn tốc độ thì được đẩy nhanh hơn thực tế rất, rất nhiều.
```

**ElevenLabs**

```text
Trước khi xếp bảng, hãy nhìn các phát minh như một cây công nghệ trong game chiến thuật. Mỗi ô chỉ mở được khi ô trước đã mở.

[pause] Có lửa thì mới nung được vôi và thủy tinh. Có thủy tinh thì mới có dụng cụ để làm hóa học. Có hóa học thì mới có thuốc và vật liệu mới.

[pause] Có kim loại và nam châm thì mới có điện. Có điện thì mới có đèn, điện thoại và radio. Và có tất cả những thứ đó, cộng với nhiên liệu và máy móc, mới nghĩ tới chuyện lên trời.

[pause] Senku luôn biết mình đang ở ô nào và ô tiếp theo cần gì. Đó là lý do cậu không bao giờ cố làm radio khi còn chưa có thủy tinh.

[pause] [chuckles] Kaku ghi chú: đây cũng là cách học rất tốt ngoài đời. Muốn giỏi một thứ khó, hãy tìm xem nó đứng trên những thứ dễ hơn nào.

[pause] [curious] Loài người thật mất bao lâu để đi từ lửa tới tên lửa? Hàng chục nghìn năm, nếu tính từ những đống lửa đầu tiên. Còn Senku chỉ mất vài năm.

[pause] Có ba lý do khiến truyện nhanh như vậy. Một: Senku đã biết câu trả lời, không phải thử sai hàng nghìn lần như những nhà phát minh thật.

[pause] Hai: cậu có rất nhiều người giúp, và những người đó học rất nhanh. Ba: truyện cần nhịp nhanh để hấp dẫn, nên nhiều bước bị lược đi.

[pause] Nhưng cũng có những thứ Senku không thể rút ngắn: chờ nguyên liệu, chờ lò đủ nóng, chờ người bệnh hồi phục. Truyện vẫn tôn trọng những giới hạn đó.

[pause] Kaku ghi chú: biết trước câu trả lời giúp đi nhanh gấp trăm lần. Đó là sức mạnh thật sự của giáo dục.

[pause] Giờ xếp tất cả lên bảng. Làm được: vôi từ vỏ sò, xà phòng. Đây là công nghệ hàng nghìn năm tuổi.

[pause] Làm được nhưng rất khó: thủy tinh, điện, bóng đèn tre, điện thoại và radio. Nguyên lý đơn giản, nhưng làm ra thì cần kỹ năng, dụng cụ và rất nhiều người.

[pause] Không thực tế: dung dịch phá đá hóa, vì hiện tượng không có thật, thuốc tự chế, vì quá nguy hiểm, và tên lửa lên Mặt Trăng trong vài năm.

[pause] Vậy Dr. Stone có thật không? Kaku chấm: phần lớn nguyên lý là thật, còn tốc độ thì được đẩy nhanh hơn thực tế rất, rất nhiều.
```

### c08 · Góc nhìn của Kaku: khoa học là cầu thang / Kết

Khoảng 95 giây · cảnh s78–s86 · 1239 ký tự

**Gemini**

```text
Có một câu nói nổi tiếng của Isaac Newton: nếu tôi nhìn được xa hơn, đó là nhờ tôi đứng trên vai những người khổng lồ.

<short pause> Senku làm được mọi thứ vì cậu mang trong đầu kiến thức của hàng nghìn năm loài người. Cậu không phát minh lại từ đầu, cậu nhớ lại con đường mà người khác đã mở.

<short pause> Và truyện cũng cho thấy một mình Senku không làm được gì. Cần người thợ làm dây, người thổi lửa, người đi tìm nguyên liệu. Khoa học là việc của cả một cộng đồng.

<short pause> Kaku nghĩ đó là thông điệp đẹp nhất: mọi thứ ta dùng mỗi ngày, từ cốc thủy tinh tới bóng đèn, là món quà của hàng triệu người ta không biết tên.

<short pause> Và muốn đi tiếp, ta chỉ cần làm điều Senku làm: tò mò, kiên nhẫn, và đi từng bậc một.

<short pause> Tóm lại: nhiều phát minh trong Dr. Stone dựa trên khoa học và lịch sử có thật, từ vôi, xà phòng, thủy tinh cho tới dây tóc bằng tre. Phần khó tin nhất là tốc độ, và hiện tượng hóa đá.

<short pause> Câu hỏi cho bạn: nếu tỉnh dậy sau ba nghìn bảy trăm năm, thứ đầu tiên bạn muốn làm lại là gì? <laugh> Kaku thì chọn xà phòng, vì Kaku rất sợ bẩn.

<short pause> Video tới, Kaku đổi sang một thế giới khác hẳn: hậu cung, thuốc men và những vụ bí ẩn trong Dược sư tự sự, bộ đang phát mùa ba. Một video nhập môn cho người mới.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. Kaku tháo kính bảo hộ đây. Mười tỉ phần trăm hẹn gặp lại!
```

**ElevenLabs**

```text
Có một câu nói nổi tiếng của Isaac Newton: nếu tôi nhìn được xa hơn, đó là nhờ tôi đứng trên vai những người khổng lồ.

[pause] Senku làm được mọi thứ vì cậu mang trong đầu kiến thức của hàng nghìn năm loài người. Cậu không phát minh lại từ đầu, cậu nhớ lại con đường mà người khác đã mở.

[pause] Và truyện cũng cho thấy một mình Senku không làm được gì. Cần người thợ làm dây, người thổi lửa, người đi tìm nguyên liệu. Khoa học là việc của cả một cộng đồng.

[pause] Kaku nghĩ đó là thông điệp đẹp nhất: mọi thứ ta dùng mỗi ngày, từ cốc thủy tinh tới bóng đèn, là món quà của hàng triệu người ta không biết tên.

[pause] Và muốn đi tiếp, ta chỉ cần làm điều Senku làm: tò mò, kiên nhẫn, và đi từng bậc một.

[pause] Tóm lại: nhiều phát minh trong Dr. Stone dựa trên khoa học và lịch sử có thật, từ vôi, xà phòng, thủy tinh cho tới dây tóc bằng tre. Phần khó tin nhất là tốc độ, và hiện tượng hóa đá.

[pause] [curious] Câu hỏi cho bạn: nếu tỉnh dậy sau ba nghìn bảy trăm năm, thứ đầu tiên bạn muốn làm lại là gì? [chuckles] Kaku thì chọn xà phòng, vì Kaku rất sợ bẩn.

[pause] Video tới, Kaku đổi sang một thế giới khác hẳn: hậu cung, thuốc men và những vụ bí ẩn trong Dược sư tự sự, bộ đang phát mùa ba. Một video nhập môn cho người mới.

[pause] Đăng ký kênh để không bỏ lỡ nhé. Kaku tháo kính bảo hộ đây. Mười tỉ phần trăm hẹn gặp lại!
```
