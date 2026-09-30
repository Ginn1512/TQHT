# Bộ prompt · One Punch Man: Bảng xếp hạng anh hùng và cấp thảm họa — vì sao người mạnh nhất lại hạng C?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 88 ảnh, 8 đoạn đọc, khoảng 14.9 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (88 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết anime One Punch Man mùa hai và phần đầu mùa ba. Kaku không nói về nhữ…

```text
Wide 16:9 landscape cinematic frame. a hero's ID card lying on a desk beside a spoiler warning note, close-up, bright office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Thẻ chỉ số của một anh hùng. Tên: Saitama. Điểm thi: bảy mươi mốt. Hạng: C. Thứ hạng trong hạng C: gần bốn tr…

```text
Wide 16:9 landscape cinematic frame. a game-style stat card with a plain silhouette, a low letter grade and a large rank number, close-up, bright game UI light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Câu trả lời: người mạnh nhất thế giới. Anh hạ mọi đối thủ bằng đúng một cú đấm.

```text
Wide 16:9 landscape cinematic frame. a single fist punching forward with a massive shockwave splitting clouds in the sky behind it, dynamic wide shot, dramatic bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đó là trò đùa lớn nhất của One Punch Man, và cũng là chủ đề của video hôm nay: một hệ thống xếp hạng anh hùng…

```text
Wide 16:9 landscape cinematic frame. a large ranking board with many names and numbers, one name at the very bottom glowing brightly, wide shot, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Ban đầu, One Punch Man là một truyện tranh mạng ONE tự vẽ bằng nét rất đơn giản. Nó nổi tiếng tới mức được vẽ…

```text
Wide 16:9 landscape cinematic frame. a simple rough webcomic sketch on a laptop screen next to a polished detailed manga page on a desk, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: One Punch Man là truyện của ONE, được Murata Yusuke vẽ lại thành manga. Anime mùa một do Madhouse làm năm 201…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a TV remote and a hero's cape folded neatly on a shelf, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đọc thẻ chỉ số của thế giới One Punch Man: hạng anh hùng, cấp thảm h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny game headphones holding up a blank stat card. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Thế giới của những anh hùng có hạng

Lời: Trong thế giới One Punch Man, quái vật xuất hiện liên tục. Để đối phó, một tổ chức được lập ra: Hiệp hội Anh…

```text
Wide 16:9 landscape cinematic frame. a gleaming headquarters tower with a large emblem in the center of a bustling city, wide shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Hiệp hội tuyển anh hùng qua một kỳ thi, rồi xếp họ vào bốn hạng: C, B, A, và S. Mỗi hạng lại có thứ hạng từ m…

```text
Wide 16:9 landscape cinematic frame. a pyramid diagram with four tiers labeled C, B, A and S from bottom to top, clean infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Anh hùng làm việc được trả lương, được xếp hạng dựa trên thành tích, và được người dân theo dõi như những ngô…

```text
Wide 16:9 landscape cinematic frame. a smartphone screen showing a leaderboard app with small hero icons and trending arrows, close-up, bright screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Khi một quái vật xuất hiện, Hiệp hội đánh giá cấp thảm họa, rồi cử anh hùng có hạng phù hợp. Về lý thuyết, đâ…

```text
Wide 16:9 landscape cinematic frame. an emergency dispatch screen showing a monster alert with a level tag and a list of assigned hero ranks, close-up, red alert light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Và quái vật cũng có hạng riêng, gọi là cấp thảm họa, từ Sói tới Thần. Hai hệ thống này ghép lại thành một bản…

```text
Wide 16:9 landscape cinematic frame. two parallel ladders drawn on a whiteboard, one with hero letters and one with animal icons, connected by dotted lines, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là một ý tưởng rất hiện đại. Anh hùng không chỉ cứu người, mà còn phải cạnh tranh thứ hạng, giữ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot anxiously refreshing a leaderboard on a tiny laptop. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Chỉ số 1: hạng anh hùng

Lời: Nghe thì dễ, nhưng hạng C có hàng trăm người, và ai cũng muốn lập thành tích. Có anh hùng hạng C tranh nhau t…

```text
Wide 16:9 landscape cinematic frame. several small hero silhouettes racing toward a single fleeing purse snatcher on a busy street, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Hạng C là hạng thấp nhất. Anh hùng hạng C phải lập ít nhất một thành tích mỗi tuần. Nếu không, họ bị loại khỏ…

```text
Wide 16:9 landscape cinematic frame. a weekly calendar with a single checkbox per week, several boxes empty and marked with red warnings, close-up, office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Hạng B không còn chỉ tiêu hằng tuần. Anh hùng hạng B được kỳ vọng tự đánh bại quái vật cấp Sói.

```text
Wide 16:9 landscape cinematic frame. a hero's silhouette standing over a defeated wolf-shaped shadow in an alley, medium shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Hạng A là những anh hùng nổi tiếng, đủ sức đánh bại quái vật cấp Hổ một mình. Họ có người hâm mộ, có hình trê…

```text
Wide 16:9 landscape cinematic frame. a billboard in a busy street showing a heroic silhouette posing, with a crowd taking photos below, wide shot, bright commercial light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Hạng S là tầng cao nhất, dành cho những người có thể một mình hạ quái vật cấp Quỷ. Số người trong hạng S rất…

```text
Wide 16:9 landscape cinematic frame. a small elite gathering of shadowy figures around a long conference table in a high tower, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Muốn lên hạng, anh hùng phải leo tới vị trí số một trong hạng hiện tại, rồi chọn lên hạng trên và bắt đầu lại…

```text
Wide 16:9 landscape cinematic frame. a small figure climbing to the top of one staircase and stepping onto the bottom of a taller staircase, symbolic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nghĩa là số một hạng C và người cuối cùng hạng B cách nhau chỉ một bước. Có người chọn ở lại làm số một hạng…

```text
Wide 16:9 landscape cinematic frame. a gold medal on a small podium beside a bronze medal on a much taller podium, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kaku để ý: hệ thống này đo thành tích và sức mạnh, nhưng không đo tính cách. Và đó là chỗ nó bắt đầu sai.

```text
Wide 16:9 landscape cinematic frame. a measuring tape wrapped around a heart-shaped object with the numbers unreadable, symbolic close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Chỉ số 2: cấp thảm họa

Lời: Giờ tới phía quái vật. Hiệp hội chia mối đe dọa làm năm cấp thảm họa, theo quy mô tàn phá.

```text
Wide 16:9 landscape cinematic frame. a five-level warning scale drawn like a thermometer with icons at each level, clean infographic, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Cấp Sói: một mối đe dọa chưa rõ mức độ, có thể gây nguy hiểm cho người. Phần lớn quái vật đường phố thuộc cấp…

```text
Wide 16:9 landscape cinematic frame. a small wolf icon on a warning card beside a quiet street at night, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Cấp Hổ: đe dọa một số lượng lớn người. Cấp Quỷ: đe dọa cả một thành phố.

```text
Wide 16:9 landscape cinematic frame. two warning cards side by side, one with a tiger icon and one with a horned demon icon, close-up, orange warning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Cấp Rồng: đe dọa nhiều thành phố. Cấp Thần: đe dọa sự tồn vong của cả loài người.

```text
Wide 16:9 landscape cinematic frame. two warning cards with a dragon icon and a radiant crown icon, glowing ominously, close-up, red and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Và rồi Saitama tới, trong mưa, và hạ nó bằng một cú đấm. Một mối đe dọa cấp Quỷ, đã đánh bại nhiều anh hùng,…

```text
Wide 16:9 landscape cinematic frame. a single fist impact in heavy rain sending a shockwave through falling water droplets, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Ví dụ: vua biển sâu, con quái vật tấn công thành phố trong mùa một, được xếp cấp Quỷ. Nó đánh bại liên tiếp n…

```text
Wide 16:9 landscape cinematic frame. a towering sea creature emerging from a flooded city street in heavy rain, wide shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Thiên thạch lao về thành phố Z cũng được xếp cấp Rồng. Và Saitama phá nó bằng một cú nhảy và một cú đấm.

```text
Wide 16:9 landscape cinematic frame. a massive flaming meteor descending over a city skyline while a tiny figure leaps up toward it, wide shot, blazing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và cấp Thần? Trong phần anime tới giờ, gần như chưa có mối đe dọa nào được xếp chính thức ở cấp này. Nó giống…

```text
Wide 16:9 landscape cinematic frame. a warning scale with the top level glowing faintly but empty, a question mark hovering beside it, close-up, eerie gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Theo bảng, cấp Rồng cần nhiều anh hùng hạng S. Theo thực tế, chỉ cần một người hạng C đi mua đồ giảm giá về.

```text
Wide 16:9 landscape cinematic frame. a plastic grocery bag with a discount sticker resting on a rooftop beside a crater, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Chỉ số 3: điểm thi

Lời: Kỳ thi anh hùng có hai phần: kiểm tra thể lực và bài viết. Điểm tổng quyết định hạng khởi đầu.

```text
Wide 16:9 landscape cinematic frame. a test paper and a stopwatch side by side on a desk in an exam hall, close-up, bright fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Saitama làm phần thể lực hoàn hảo, phá mọi kỷ lục. Nhưng phần viết thì gần như trượt. Tổng điểm bảy mươi mốt,…

```text
Wide 16:9 landscape cinematic frame. a scoreboard showing a perfect physical score next to a barely passing written score, close-up, humorous bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Trong khi đó Genos, học trò của Saitama, cậu người máy, được điểm tuyệt đối, và được xếp thẳng vào hạng S.

```text
Wide 16:9 landscape cinematic frame. a perfect score certificate with a small gear emblem pinned to a wall beside a mirror, close-up, clean bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Saitama sau đó vẫn leo hạng, lên hạng B rồi hạng A theo thời gian. Nhưng tốc độ leo hạng của anh rất chậm so…

```text
Wide 16:9 landscape cinematic frame. a slow snail climbing a tall staircase of rank numbers, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Nghĩa là thầy ở hạng C, trò ở hạng S. Và trò vẫn gọi thầy là thầy, đi theo học mỗi ngày.

```text
Wide 16:9 landscape cinematic frame. a small apartment with two cups of tea on a low table, one seat humble and one seat eager, wide shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy phần thi viết là lời châm biếm rất hay. Một anh hùng có thể mạnh vô địch nhưng không trả lời được c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot chewing on a pencil and staring at a blank exam paper with a sweat drop. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Vì sao Saitama mạnh?

Lời: Trước khi sang chỉ số tiếp theo, một câu hỏi ai cũng muốn biết: Saitama luyện tập thế nào mà mạnh như vậy?

```text
Wide 16:9 landscape cinematic frame. a worn pair of running shoes beside a simple exercise mat in a small apartment, close-up, morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Theo lời anh kể: một trăm lần hít đất, một trăm lần gập bụng, một trăm lần ngồi xổm, và chạy mười cây số. Mỗi…

```text
Wide 16:9 landscape cinematic frame. a daily checklist pinned to a wall with four exercise icons and hundreds of checkmarks, close-up, bright morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kèm theo những điều kiện rất lạ: không bật điều hòa mùa hè, không sưởi mùa đông, ăn uống đầy đủ. Cái giá duy…

```text
Wide 16:9 landscape cinematic frame. a single strand of hair floating down onto an exercise mat, humorous extreme close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Genos, và cả người đọc, đều nghĩ phải có bí mật gì đó. Nhưng truyện không bao giờ đưa ra một lời giải thích n…

```text
Wide 16:9 landscape cinematic frame. a thick notebook of scientific formulas with the last page containing only a small doodle of a push-up, close-up, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là lời châm biếm tuyệt vời nhắm vào thể loại shounen: những bộ truyện khác cần cả chục chương g…

```text
Wide 16:9 landscape cinematic frame. the owl mascot doing a tiny push-up on a notebook with a determined face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Hồ sơ vài anh hùng hạng S

Lời: Để thấy bảng xếp hạng hoạt động thế nào khi nó đúng, hãy xem nhanh vài anh hùng hạng S.

```text
Wide 16:9 landscape cinematic frame. a row of seven sealed dossiers on a long table, each stamped with a large letter S, close-up, dramatic office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Số một là Blast, một anh hùng bí ẩn hiếm khi xuất hiện. Gần như không ai biết anh trông thế nào, và đó là lý…

```text
Wide 16:9 landscape cinematic frame. a single dossier with only a shadowy silhouette photo and mostly blank pages, close-up, mysterious dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Số ba là Bang, một võ sư già dạy võ trên núi. Sức mạnh của ông đến từ cả đời luyện tập, không có siêu năng lự…

```text
Wide 16:9 landscape cinematic frame. an old martial arts dojo on a mountainside with a single elderly silhouette practicing slow forms at dawn, wide shot, misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Có cả một cậu bé thiên tài dùng phát minh để chiến đấu, một samurai kiếm thuật đỉnh cao, và một anh hùng dùng…

```text
Wide 16:9 landscape cinematic frame. a table with a small robotic gadget, a sheathed katana, and a metal baseball bat laid side by side, still life, bright light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhưng ngay trong hạng S, vẫn có người như King, và vẫn có những người tính cách rất khó chịu. Hạng S là hạng…

```text
Wide 16:9 landscape cinematic frame. a conference table where some chairs are turned away from each other, symbolic wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Chỉ số 4: độ nổi tiếng

Lời: Chỉ số ẩn quan trọng nhất trong hệ thống: độ nổi tiếng. Thứ hạng không chỉ dựa vào sức mạnh, mà còn dựa vào v…

```text
Wide 16:9 landscape cinematic frame. a popularity meter with fan icons filling up beside a hero silhouette, clean infographic, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Và Saitama gần như luôn thất bại ở chỉ số này. Anh thường xuất hiện khi mọi thứ gần kết thúc, đấm một cái, rồ…

```text
Wide 16:9 landscape cinematic frame. a lone figure walking home down an empty street at sunset carrying a grocery bag, back view, wide shot, quiet golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Có lúc anh cứu cả thành phố khỏi thiên thạch, và người dân lại trách anh vì mảnh vỡ làm hỏng nhà cửa.

```text
Wide 16:9 landscape cinematic frame. angry citizens pointing at a small figure amid scattered rubble on a street, humorous wide shot, harsh daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Có lúc anh hạ vua biển sâu, rồi cố ý nói rằng các anh hùng khác đã làm quái vật yếu đi, để họ không bị coi th…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing in the rain with his back to a crowd, while other heroes are helped up in the background, wide shot, grey rainy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Và Saitama cũng không thật sự quan tâm. Anh muốn được công nhận, nhưng không muốn nổi tiếng bằng cách nói dối…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing at the edge of a rooftop at dusk looking out at the city lights, back view, wide shot, quiet golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kaku để ý: độ nổi tiếng trong truyện không đo ai làm tốt nhất, mà đo ai được nhìn thấy nhiều nhất. Nghe có qu…

```text
Wide 16:9 landscape cinematic frame. a phone screen with a viral post counter rising rapidly beside a small quiet photo with no likes, close-up, bright screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Xếp hạng: những ca đặc biệt

Lời: Giờ tới những ca khiến bảng xếp hạng trở nên thú vị nhất.

```text
Wide 16:9 landscape cinematic frame. a ranking board with several entries highlighted in different colors, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Ca một: King, anh hùng hạng S thứ bảy, được gọi là người mạnh nhất Trái Đất. Sự thật: anh không có sức mạnh g…

```text
Wide 16:9 landscape cinematic frame. a tall imposing silhouette with a calm face sitting in a small room playing a video game, humorous medium shot, dim screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Tiếng tim đập của King khi sợ hãi vang to tới mức kẻ thù nghe thấy, và tưởng đó là âm thanh của một chiến bin…

```text
Wide 16:9 landscape cinematic frame. a heart-shaped sound wave icon pulsing loudly beside a nervous silhouette, humorous infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Ca hai: Mumen Rider, anh hùng số một hạng C, đi xe đạp. Anh yếu, và anh biết mình yếu.

```text
Wide 16:9 landscape cinematic frame. a simple bicycle leaning against a lamppost with a helmet hanging from the handlebar, close-up, soft afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Nhưng khi vua biển sâu tấn công, Mumen Rider vẫn lao tới, dù biết mình không có cơ hội thắng. Anh nói, đại ý:…

```text
Wide 16:9 landscape cinematic frame. a small figure standing alone in heavy rain before a towering sea creature, fists raised, wide shot, dramatic grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Và đám đông, những người đã trách mọi anh hùng, lại cổ vũ Mumen Rider. Vì họ thấy lòng dũng cảm thật.

```text
Wide 16:9 landscape cinematic frame. a crowd under umbrellas cheering toward a small injured figure in the rain, wide shot, emotional warm light breaking through grey. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Ca ba: Tatsumaki, hạng S thứ hai, một nhà ngoại cảm cực mạnh, có thể nâng cả những khối đá khổng lồ. Cô mạnh…

```text
Wide 16:9 landscape cinematic frame. massive chunks of rock floating in the sky above a city, held by an invisible force, wide shot, green-tinted dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nghĩa là bảng xếp hạng đôi khi đúng, đôi khi sai, và đôi khi sai theo cả hai chiều: đánh giá thấp người mạnh,…

```text
Wide 16:9 landscape cinematic frame. a crooked ranking board with some names too high and some too low, arrows pointing to correct them, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Anh hùng săn anh hùng

Lời: Có một nhân vật lật ngược cả hệ thống: Garou, kẻ tự gọi mình là thợ săn anh hùng. Hắn đi đánh bại từng anh hù…

```text
Wide 16:9 landscape cinematic frame. a lone martial artist standing on a rooftop at night surrounded by defeated silhouettes, wide shot, cold moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Garou không tin vào bảng xếp hạng. Hắn nghĩ những anh hùng chỉ là kẻ mạnh bắt nạt kẻ yếu, và quái vật mới là…

```text
Wide 16:9 landscape cinematic frame. a crumpled hero ranking poster lying on wet pavement under a flickering street lamp, close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Điều thú vị là Garou từng là học trò của võ sư Bang, người đứng hạng S thứ ba. Một người được bảng xếp hạng v…

```text
Wide 16:9 landscape cinematic frame. two pairs of training shoes at the entrance of a mountain dojo, one neatly placed and one kicked aside, close-up, misty morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Hắn cũng là một câu hỏi cho chính hệ thống: nếu anh hùng được đánh giá bằng sức mạnh và danh tiếng, thì ai đư…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a hero's silhouette as a monster's silhouette, symbolic close-up, dramatic split light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Arc của Garou kéo dài sang mùa ba, và Kaku sẽ không nói trước kết quả. Chỉ biết rằng hắn là một trong những n…

```text
Wide 16:9 landscape cinematic frame. a martial artist's worn wrist wraps lying on a stone step, close-up, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Khi quái vật cũng có tổ chức

Lời: Ở mùa hai và mùa ba, thế giới One Punch Man có thêm một hệ thống thứ ba: Hiệp hội Quái vật, một tổ chức của c…

```text
Wide 16:9 landscape cinematic frame. a dark underground lair with a large throne and many shadowy monstrous silhouettes gathered below, wide shot, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nhiều cán bộ của tổ chức này được xếp cấp Rồng. Nghĩa là cùng lúc có nhiều mối đe dọa cấp Rồng, thứ mà bảng x…

```text
Wide 16:9 landscape cinematic frame. a warning board with many dragon icons pinned at once and a flashing alarm light, close-up, tense red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Cuộc đối đầu giữa hai hiệp hội là phép thử lớn nhất cho bảng xếp hạng. Ai thật sự mạnh, ai chỉ có danh tiếng,…

```text
Wide 16:9 landscape cinematic frame. two large emblems facing each other on opposite walls of a ruined hall, dramatic wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Kaku sẽ không nói trước diễn biến, vì mùa ba vẫn đang kể phần này. Nhưng nếu bạn thích bảng xếp hạng, arc này…

```text
Wide 16:9 landscape cinematic frame. a ranking board with several cracks spreading across it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Giới hạn của những con số

Lời: Vậy những con số trong One Punch Man cho ta biết gì? Kaku thấy có ba giới hạn.

```text
Wide 16:9 landscape cinematic frame. a notebook page titled with three numbered lines, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nói cách khác, Hiệp hội chấm điểm theo bằng chứng. Mà Saitama thì luôn đi về trước khi có người tới chụp ảnh.

```text
Wide 16:9 landscape cinematic frame. an empty street with a large crater and a news camera crew arriving too late, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Giới hạn một: con số đo cái được nhìn thấy, không đo cái thật. Saitama mạnh nhất nhưng ở hạng thấp, vì không…

```text
Wide 16:9 landscape cinematic frame. an iceberg drawing with a small visible tip above water and a massive hidden body below, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Giới hạn hai: con số không đo được lòng dũng cảm. Mumen Rider yếu, nhưng dũng cảm hơn nhiều anh hùng mạnh hơn…

```text
Wide 16:9 landscape cinematic frame. a small heart icon on a stat card with the value field showing an infinity symbol, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Giới hạn ba: con số có thể bị lừa. King ở hạng S chỉ vì danh tiếng. Một hệ thống dựa vào tin đồn sẽ luôn có n…

```text
Wide 16:9 landscape cinematic frame. a stat card with a large fake gold sticker stuck over the real numbers, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và có một giới hạn cuối, rất buồn: Saitama đã mạnh tới mức không còn thấy hứng thú khi chiến đấu. Mọi trận đề…

```text
Wide 16:9 landscape cinematic frame. a lone figure sitting on a rooftop staring at the sky with an empty expression, a single cloud drifting by, wide shot, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Có lẽ vì vậy mà Saitama không quan tâm tới thứ hạng. Thứ anh muốn không phải con số, mà là một đối thủ khiến…

```text
Wide 16:9 landscape cinematic frame. a single boxing glove hanging from a hook in an empty gym, dust drifting in a beam of light, close-up, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nghĩa là con số cao nhất cũng có giá. Khi bạn không còn ai để thử thách, sức mạnh trở thành một sự cô đơn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting alone on top of a very tall stack of trophies, looking a bit lonely. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Trò chơi: thẻ chỉ số của bạn

Lời: Giờ tới lượt bạn. Hãy tự điền thẻ chỉ số anh hùng của mình.

```text
Wide 16:9 landscape cinematic frame. a blank hero stat card with empty fields and a pencil resting on it, close-up, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Một: bạn sẽ đậu kỳ thi với bao nhiêu điểm? Thể lực bao nhiêu, bài viết bao nhiêu?

```text
Wide 16:9 landscape cinematic frame. a small exam form with two score boxes, one with a running shoe icon and one with a pencil icon, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Hai: bạn thuộc hạng nào, và bạn chọn làm số một hạng dưới, hay người cuối hạng trên?

```text
Wide 16:9 landscape cinematic frame. two podiums of different heights with a small question mark on each, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Ba: bạn đủ sức đối đầu với quái vật cấp nào? Và nếu gặp một con cấp Quỷ, bạn có lao lên như Mumen Rider không?

```text
Wide 16:9 landscape cinematic frame. a small figure standing at the start of a road leading toward a distant silhouette of a giant monster, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Năm: nếu bạn giỏi hơn người ở hạng trên mà vẫn bị xếp hạng thấp, bạn sẽ tức giận, hay cứ tiếp tục làm việc củ…

```text
Wide 16:9 landscape cinematic frame. a small calm figure continuing to jog past a ranking board without looking at it, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Bốn, chỉ số ẩn: nếu bạn cứu cả thành phố mà không ai biết, bạn có còn làm không?

```text
Wide 16:9 landscape cinematic frame. a small anonymous thank-you note left on a doorstep with no name signed, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Thẻ của Kaku: thể lực hai điểm, bài viết mười điểm, hạng C, cấp Sói cũng hơi run. Nhưng chỉ số ẩn thì Kaku tự…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding up its own stat card showing low numbers and a big heart sticker. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Kết

Lời: One Punch Man là một bộ truyện giả vờ nói về sức mạnh, nhưng thật ra nói về việc con người đánh giá nhau thế…

```text
Wide 16:9 landscape cinematic frame. a ranking board slowly fading while a small figure walks away carrying groceries in the foreground, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và lần tới bạn nhìn thấy một bảng xếp hạng, dù ở trường, ở công ty, hay trên mạng, hãy nhớ tới Saitama: con s…

```text
Wide 16:9 landscape cinematic frame. a school notice board with ranked names pinned to it, a small smiling doodle drawn in the corner, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Video tiếp theo, Kaku mở một cuốn sử hoài niệm: Yu-Gi-Oh! và lịch sử luật bài, từ Fusion, Ritual, tới Synchro…

```text
Wide 16:9 landscape cinematic frame. a small stack of trading cards fanned out on a table with an old game mat, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem Kaku đọc thẻ chỉ số, hãy đăng ký kênh. Thứ hạng của Kaku có thể thấp, nhưng Kaku sẽ tiếp tụ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot riding a tiny bicycle and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thế giới của những anh hùng có hạng

Khoảng 152 giây · cảnh s01–s13 · 1971 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime One Punch Man mùa hai và phần đầu mùa ba. Kaku không nói về những gì chỉ có trong manga.

<short pause> Thẻ chỉ số của một anh hùng. Tên: Saitama. Điểm thi: bảy mươi mốt. Hạng: C. Thứ hạng trong hạng C: gần bốn trăm. Nhìn thẻ này, bạn nghĩ anh ta mạnh cỡ nào?

<short pause> Câu trả lời: người mạnh nhất thế giới. Anh hạ mọi đối thủ bằng đúng một cú đấm.

<short pause> Đó là trò đùa lớn nhất của One Punch Man, và cũng là chủ đề của video hôm nay: một hệ thống xếp hạng anh hùng rất chi tiết, và vì sao những con số của nó lại sai một cách hài hước.

<short pause> Ban đầu, One Punch Man là một truyện tranh mạng ONE tự vẽ bằng nét rất đơn giản. Nó nổi tiếng tới mức được vẽ lại thành manga chuyên nghiệp. Chính câu chuyện ra đời của nó cũng giống Saitama: bắt đầu ở hạng thấp nhất.

<short pause> One Punch Man là truyện của ONE, được Murata Yusuke vẽ lại thành manga. Anime mùa một do Madhouse làm năm 2015, mùa hai và ba do J.C. Staff, mùa ba ra mắt tháng mười năm 2025.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đọc thẻ chỉ số của thế giới One Punch Man: hạng anh hùng, cấp thảm họa, điểm thi, và giới hạn của những con số. Cuối video là thẻ chỉ số của chính bạn.

<short pause> Trong thế giới One Punch Man, quái vật xuất hiện liên tục. Để đối phó, một tổ chức được lập ra: Hiệp hội Anh hùng.

<short pause> Hiệp hội tuyển anh hùng qua một kỳ thi, rồi xếp họ vào bốn hạng: C, B, A, và S. Mỗi hạng lại có thứ hạng từ một trở xuống.

<short pause> Anh hùng làm việc được trả lương, được xếp hạng dựa trên thành tích, và được người dân theo dõi như những ngôi sao. Giống một bảng xếp hạng game online.

<short pause> Khi một quái vật xuất hiện, Hiệp hội đánh giá cấp thảm họa, rồi cử anh hùng có hạng phù hợp. Về lý thuyết, đây là một hệ thống rất hợp lý.

<short pause> Và quái vật cũng có hạng riêng, gọi là cấp thảm họa, từ Sói tới Thần. Hai hệ thống này ghép lại thành một bảng: anh hùng hạng nào đánh được quái vật cấp nào.

<short pause> Kaku thấy đây là một ý tưởng rất hiện đại. Anh hùng không chỉ cứu người, mà còn phải cạnh tranh thứ hạng, giữ độ nổi tiếng, và chịu áp lực từ bảng xếp hạng.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime One Punch Man mùa hai và phần đầu mùa ba. Kaku không nói về những gì chỉ có trong manga.

[pause] Thẻ chỉ số của một anh hùng. Tên: Saitama. Điểm thi: bảy mươi mốt. Hạng: C. Thứ hạng trong hạng C: gần bốn trăm. [curious] Nhìn thẻ này, bạn nghĩ anh ta mạnh cỡ nào?

[pause] Câu trả lời: người mạnh nhất thế giới. Anh hạ mọi đối thủ bằng đúng một cú đấm.

[pause] Đó là trò đùa lớn nhất của One Punch Man, và cũng là chủ đề của video hôm nay: một hệ thống xếp hạng anh hùng rất chi tiết, và vì sao những con số của nó lại sai một cách hài hước.

[pause] Ban đầu, One Punch Man là một truyện tranh mạng ONE tự vẽ bằng nét rất đơn giản. Nó nổi tiếng tới mức được vẽ lại thành manga chuyên nghiệp. Chính câu chuyện ra đời của nó cũng giống Saitama: bắt đầu ở hạng thấp nhất.

[pause] One Punch Man là truyện của ONE, được Murata Yusuke vẽ lại thành manga. Anime mùa một do Madhouse làm năm 2015, mùa hai và ba do J.C. Staff, mùa ba ra mắt tháng mười năm 2025.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đọc thẻ chỉ số của thế giới One Punch Man: hạng anh hùng, cấp thảm họa, điểm thi, và giới hạn của những con số. Cuối video là thẻ chỉ số của chính bạn.

[pause] Trong thế giới One Punch Man, quái vật xuất hiện liên tục. Để đối phó, một tổ chức được lập ra: Hiệp hội Anh hùng.

[pause] Hiệp hội tuyển anh hùng qua một kỳ thi, rồi xếp họ vào bốn hạng: C, B, A, và S. Mỗi hạng lại có thứ hạng từ một trở xuống.

[pause] Anh hùng làm việc được trả lương, được xếp hạng dựa trên thành tích, và được người dân theo dõi như những ngôi sao. Giống một bảng xếp hạng game online.

[pause] Khi một quái vật xuất hiện, Hiệp hội đánh giá cấp thảm họa, rồi cử anh hùng có hạng phù hợp. Về lý thuyết, đây là một hệ thống rất hợp lý.

[pause] Và quái vật cũng có hạng riêng, gọi là cấp thảm họa, từ Sói tới Thần. Hai hệ thống này ghép lại thành một bảng: anh hùng hạng nào đánh được quái vật cấp nào.

[pause] Kaku thấy đây là một ý tưởng rất hiện đại. Anh hùng không chỉ cứu người, mà còn phải cạnh tranh thứ hạng, giữ độ nổi tiếng, và chịu áp lực từ bảng xếp hạng.
```

### c02 · Chỉ số 1: hạng anh hùng

Khoảng 78 giây · cảnh s14–s21 · 1013 ký tự

**Gemini**

```text
Nghe thì dễ, nhưng hạng C có hàng trăm người, và ai cũng muốn lập thành tích. Có anh hùng hạng C tranh nhau từng vụ trộm vặt để giữ chỉ tiêu.

<short pause> Hạng C là hạng thấp nhất. Anh hùng hạng C phải lập ít nhất một thành tích mỗi tuần. Nếu không, họ bị loại khỏi hiệp hội.

<short pause> Hạng B không còn chỉ tiêu hằng tuần. Anh hùng hạng B được kỳ vọng tự đánh bại quái vật cấp Sói.

<short pause> Hạng A là những anh hùng nổi tiếng, đủ sức đánh bại quái vật cấp Hổ một mình. Họ có người hâm mộ, có hình trên quảng cáo.

<short pause> Hạng S là tầng cao nhất, dành cho những người có thể một mình hạ quái vật cấp Quỷ. Số người trong hạng S rất ít, và mỗi người gần như là một siêu anh hùng thật.

<short pause> Muốn lên hạng, anh hùng phải leo tới vị trí số một trong hạng hiện tại, rồi chọn lên hạng trên và bắt đầu lại từ dưới cùng.

<short pause> Nghĩa là số một hạng C và người cuối cùng hạng B cách nhau chỉ một bước. Có người chọn ở lại làm số một hạng dưới, thay vì làm người cuối hạng trên.

<short pause> Kaku để ý: hệ thống này đo thành tích và sức mạnh, nhưng không đo tính cách. Và đó là chỗ nó bắt đầu sai.
```

**ElevenLabs**

```text
Nghe thì dễ, nhưng hạng C có hàng trăm người, và ai cũng muốn lập thành tích. Có anh hùng hạng C tranh nhau từng vụ trộm vặt để giữ chỉ tiêu.

[pause] Hạng C là hạng thấp nhất. Anh hùng hạng C phải lập ít nhất một thành tích mỗi tuần. Nếu không, họ bị loại khỏi hiệp hội.

[pause] Hạng B không còn chỉ tiêu hằng tuần. Anh hùng hạng B được kỳ vọng tự đánh bại quái vật cấp Sói.

[pause] Hạng A là những anh hùng nổi tiếng, đủ sức đánh bại quái vật cấp Hổ một mình. Họ có người hâm mộ, có hình trên quảng cáo.

[pause] Hạng S là tầng cao nhất, dành cho những người có thể một mình hạ quái vật cấp Quỷ. Số người trong hạng S rất ít, và mỗi người gần như là một siêu anh hùng thật.

[pause] Muốn lên hạng, anh hùng phải leo tới vị trí số một trong hạng hiện tại, rồi chọn lên hạng trên và bắt đầu lại từ dưới cùng.

[pause] Nghĩa là số một hạng C và người cuối cùng hạng B cách nhau chỉ một bước. Có người chọn ở lại làm số một hạng dưới, thay vì làm người cuối hạng trên.

[pause] Kaku để ý: hệ thống này đo thành tích và sức mạnh, nhưng không đo tính cách. Và đó là chỗ nó bắt đầu sai.
```

### c03 · Chỉ số 2: cấp thảm họa / Chỉ số 3: điểm thi

Khoảng 134 giây · cảnh s22–s36 · 1743 ký tự

**Gemini**

```text
Giờ tới phía quái vật. Hiệp hội chia mối đe dọa làm năm cấp thảm họa, theo quy mô tàn phá.

<short pause> Cấp Sói: một mối đe dọa chưa rõ mức độ, có thể gây nguy hiểm cho người. Phần lớn quái vật đường phố thuộc cấp này.

<short pause> Cấp Hổ: đe dọa một số lượng lớn người. Cấp Quỷ: đe dọa cả một thành phố.

<short pause> Cấp Rồng: đe dọa nhiều thành phố. Cấp Thần: đe dọa sự tồn vong của cả loài người.

<short pause> Và rồi Saitama tới, trong mưa, và hạ nó bằng một cú đấm. Một mối đe dọa cấp Quỷ, đã đánh bại nhiều anh hùng, kết thúc trong một giây.

<short pause> Ví dụ: vua biển sâu, con quái vật tấn công thành phố trong mùa một, được xếp cấp Quỷ. Nó đánh bại liên tiếp nhiều anh hùng hạng B, hạng A, và cả một anh hùng hạng S.

<short pause> Thiên thạch lao về thành phố Z cũng được xếp cấp Rồng. Và Saitama phá nó bằng một cú nhảy và một cú đấm.

<short pause> Và cấp Thần? Trong phần anime tới giờ, gần như chưa có mối đe dọa nào được xếp chính thức ở cấp này. Nó giống như một ô trống trên bảng, chờ một ngày được điền vào.

<short pause> Theo bảng, cấp Rồng cần nhiều anh hùng hạng S. Theo thực tế, chỉ cần một người hạng C đi mua đồ giảm giá về.

<short pause> Kỳ thi anh hùng có hai phần: kiểm tra thể lực và bài viết. Điểm tổng quyết định hạng khởi đầu.

<short pause> Saitama làm phần thể lực hoàn hảo, phá mọi kỷ lục. <short pause> Nhưng phần viết thì gần như trượt. Tổng điểm bảy mươi mốt, vừa đủ đậu, xếp hạng C.

<short pause> Trong khi đó Genos, học trò của Saitama, cậu người máy, được điểm tuyệt đối, và được xếp thẳng vào hạng S.

<short pause> Saitama sau đó vẫn leo hạng, lên hạng B rồi hạng A theo thời gian. <short pause> Nhưng tốc độ leo hạng của anh rất chậm so với sức mạnh thật.

<short pause> Nghĩa là thầy ở hạng C, trò ở hạng S. Và trò vẫn gọi thầy là thầy, đi theo học mỗi ngày.

<short pause> <laugh> Kaku thấy phần thi viết là lời châm biếm rất hay. Một anh hùng có thể mạnh vô địch nhưng không trả lời được câu hỏi trên giấy. Và hệ thống lại coi trọng tờ giấy đó.
```

**ElevenLabs**

```text
Giờ tới phía quái vật. Hiệp hội chia mối đe dọa làm năm cấp thảm họa, theo quy mô tàn phá.

[pause] Cấp Sói: một mối đe dọa chưa rõ mức độ, có thể gây nguy hiểm cho người. Phần lớn quái vật đường phố thuộc cấp này.

[pause] Cấp Hổ: đe dọa một số lượng lớn người. Cấp Quỷ: đe dọa cả một thành phố.

[pause] Cấp Rồng: đe dọa nhiều thành phố. Cấp Thần: đe dọa sự tồn vong của cả loài người.

[pause] Và rồi Saitama tới, trong mưa, và hạ nó bằng một cú đấm. Một mối đe dọa cấp Quỷ, đã đánh bại nhiều anh hùng, kết thúc trong một giây.

[pause] Ví dụ: vua biển sâu, con quái vật tấn công thành phố trong mùa một, được xếp cấp Quỷ. Nó đánh bại liên tiếp nhiều anh hùng hạng B, hạng A, và cả một anh hùng hạng S.

[pause] Thiên thạch lao về thành phố Z cũng được xếp cấp Rồng. Và Saitama phá nó bằng một cú nhảy và một cú đấm.

[pause] [curious] Và cấp Thần? Trong phần anime tới giờ, gần như chưa có mối đe dọa nào được xếp chính thức ở cấp này. Nó giống như một ô trống trên bảng, chờ một ngày được điền vào.

[pause] Theo bảng, cấp Rồng cần nhiều anh hùng hạng S. Theo thực tế, chỉ cần một người hạng C đi mua đồ giảm giá về.

[pause] Kỳ thi anh hùng có hai phần: kiểm tra thể lực và bài viết. Điểm tổng quyết định hạng khởi đầu.

[pause] Saitama làm phần thể lực hoàn hảo, phá mọi kỷ lục. [pause] Nhưng phần viết thì gần như trượt. Tổng điểm bảy mươi mốt, vừa đủ đậu, xếp hạng C.

[pause] Trong khi đó Genos, học trò của Saitama, cậu người máy, được điểm tuyệt đối, và được xếp thẳng vào hạng S.

[pause] Saitama sau đó vẫn leo hạng, lên hạng B rồi hạng A theo thời gian. [pause] Nhưng tốc độ leo hạng của anh rất chậm so với sức mạnh thật.

[pause] Nghĩa là thầy ở hạng C, trò ở hạng S. Và trò vẫn gọi thầy là thầy, đi theo học mỗi ngày.

[pause] [chuckles] Kaku thấy phần thi viết là lời châm biếm rất hay. Một anh hùng có thể mạnh vô địch nhưng không trả lời được câu hỏi trên giấy. Và hệ thống lại coi trọng tờ giấy đó.
```

### c04 · Vì sao Saitama mạnh? / Hồ sơ vài anh hùng hạng S

Khoảng 109 giây · cảnh s37–s46 · 1415 ký tự

**Gemini**

```text
Trước khi sang chỉ số tiếp theo, một câu hỏi ai cũng muốn biết: Saitama luyện tập thế nào mà mạnh như vậy?

<short pause> Theo lời anh kể: một trăm lần hít đất, một trăm lần gập bụng, một trăm lần ngồi xổm, và chạy mười cây số. Mỗi ngày. Suốt ba năm. Không bỏ một ngày nào.

<short pause> Kèm theo những điều kiện rất lạ: không bật điều hòa mùa hè, không sưởi mùa đông, ăn uống đầy đủ. Cái giá duy nhất anh nhắc tới: tóc anh rụng hết.

<short pause> Genos, và cả người đọc, đều nghĩ phải có bí mật gì đó. <short pause> Nhưng truyện không bao giờ đưa ra một lời giải thích nghiêm túc. Và đó chính là trò đùa.

<short pause> <laugh> Kaku thấy đây là lời châm biếm tuyệt vời nhắm vào thể loại shounen: những bộ truyện khác cần cả chục chương giải thích hệ thống sức mạnh. One Punch Man trả lời bằng một bài tập thể dục ai cũng biết.

<short pause> Để thấy bảng xếp hạng hoạt động thế nào khi nó đúng, hãy xem nhanh vài anh hùng hạng S.

<short pause> Số một là Blast, một anh hùng bí ẩn hiếm khi xuất hiện. Gần như không ai biết anh trông thế nào, và đó là lý do anh trở thành huyền thoại.

<short pause> Số ba là Bang, một võ sư già dạy võ trên núi. Sức mạnh của ông đến từ cả đời luyện tập, không có siêu năng lực.

<short pause> Có cả một cậu bé thiên tài dùng phát minh để chiến đấu, một samurai kiếm thuật đỉnh cao, và một anh hùng dùng gậy bóng chày. Mỗi người một phong cách, và đa số xứng đáng với thứ hạng.

<short pause> Nhưng ngay trong hạng S, vẫn có người như King, và vẫn có những người tính cách rất khó chịu. Hạng S là hạng của sức mạnh, không phải hạng của nhân cách.
```

**ElevenLabs**

```text
[curious] Trước khi sang chỉ số tiếp theo, một câu hỏi ai cũng muốn biết: Saitama luyện tập thế nào mà mạnh như vậy?

[pause] Theo lời anh kể: một trăm lần hít đất, một trăm lần gập bụng, một trăm lần ngồi xổm, và chạy mười cây số. Mỗi ngày. Suốt ba năm. Không bỏ một ngày nào.

[pause] Kèm theo những điều kiện rất lạ: không bật điều hòa mùa hè, không sưởi mùa đông, ăn uống đầy đủ. Cái giá duy nhất anh nhắc tới: tóc anh rụng hết.

[pause] Genos, và cả người đọc, đều nghĩ phải có bí mật gì đó. [pause] Nhưng truyện không bao giờ đưa ra một lời giải thích nghiêm túc. Và đó chính là trò đùa.

[pause] [chuckles] Kaku thấy đây là lời châm biếm tuyệt vời nhắm vào thể loại shounen: những bộ truyện khác cần cả chục chương giải thích hệ thống sức mạnh. One Punch Man trả lời bằng một bài tập thể dục ai cũng biết.

[pause] Để thấy bảng xếp hạng hoạt động thế nào khi nó đúng, hãy xem nhanh vài anh hùng hạng S.

[pause] Số một là Blast, một anh hùng bí ẩn hiếm khi xuất hiện. Gần như không ai biết anh trông thế nào, và đó là lý do anh trở thành huyền thoại.

[pause] Số ba là Bang, một võ sư già dạy võ trên núi. Sức mạnh của ông đến từ cả đời luyện tập, không có siêu năng lực.

[pause] Có cả một cậu bé thiên tài dùng phát minh để chiến đấu, một samurai kiếm thuật đỉnh cao, và một anh hùng dùng gậy bóng chày. Mỗi người một phong cách, và đa số xứng đáng với thứ hạng.

[pause] Nhưng ngay trong hạng S, vẫn có người như King, và vẫn có những người tính cách rất khó chịu. Hạng S là hạng của sức mạnh, không phải hạng của nhân cách.
```

### c05 · Chỉ số 4: độ nổi tiếng / Xếp hạng: những ca đặc biệt

Khoảng 144 giây · cảnh s47–s60 · 1876 ký tự

**Gemini**

```text
Chỉ số ẩn quan trọng nhất trong hệ thống: độ nổi tiếng. Thứ hạng không chỉ dựa vào sức mạnh, mà còn dựa vào việc người ta biết bạn đã làm gì.

<short pause> Và Saitama gần như luôn thất bại ở chỉ số này. Anh thường xuất hiện khi mọi thứ gần kết thúc, đấm một cái, rồi về. Không ai thấy.

<short pause> Có lúc anh cứu cả thành phố khỏi thiên thạch, và người dân lại trách anh vì mảnh vỡ làm hỏng nhà cửa.

<short pause> Có lúc anh hạ vua biển sâu, rồi cố ý nói rằng các anh hùng khác đã làm quái vật yếu đi, để họ không bị coi thường. Anh nhận tiếng xấu thay cho họ.

<short pause> Và Saitama cũng không thật sự quan tâm. Anh muốn được công nhận, nhưng không muốn nổi tiếng bằng cách nói dối. Anh chỉ muốn một trận đấu làm tim mình đập nhanh trở lại.

<short pause> Kaku để ý: độ nổi tiếng trong truyện không đo ai làm tốt nhất, mà đo ai được nhìn thấy nhiều nhất. Nghe có quen với mạng xã hội ngày nay không?

<short pause> Giờ tới những ca khiến bảng xếp hạng trở nên thú vị nhất.

<short pause> Ca một: King, anh hùng hạng S thứ bảy, được gọi là người mạnh nhất Trái Đất. Sự thật: anh không có sức mạnh gì cả. Mọi chiến công của anh thật ra là do Saitama làm, và người ta nhầm là King.

<short pause> Tiếng tim đập của King khi sợ hãi vang to tới mức kẻ thù nghe thấy, và tưởng đó là âm thanh của một chiến binh sắp ra đòn. Anh thắng nhiều trận chỉ bằng danh tiếng.

<short pause> Ca hai: Mumen Rider, anh hùng số một hạng C, đi xe đạp. Anh yếu, và anh biết mình yếu.

<short pause> Nhưng khi vua biển sâu tấn công, Mumen Rider vẫn lao tới, dù biết mình không có cơ hội thắng. Anh nói, đại ý: tôi biết mình không thắng được, nhưng tôi vẫn phải chiến đấu.

<short pause> Và đám đông, những người đã trách mọi anh hùng, lại cổ vũ Mumen Rider. Vì họ thấy lòng dũng cảm thật.

<short pause> Ca ba: Tatsumaki, hạng S thứ hai, một nhà ngoại cảm cực mạnh, có thể nâng cả những khối đá khổng lồ. Cô mạnh thật, và danh tiếng của cô xứng đáng.

<short pause> Nghĩa là bảng xếp hạng đôi khi đúng, đôi khi sai, và đôi khi sai theo cả hai chiều: đánh giá thấp người mạnh, đánh giá cao người yếu.
```

**ElevenLabs**

```text
Chỉ số ẩn quan trọng nhất trong hệ thống: độ nổi tiếng. Thứ hạng không chỉ dựa vào sức mạnh, mà còn dựa vào việc người ta biết bạn đã làm gì.

[pause] Và Saitama gần như luôn thất bại ở chỉ số này. Anh thường xuất hiện khi mọi thứ gần kết thúc, đấm một cái, rồi về. Không ai thấy.

[pause] Có lúc anh cứu cả thành phố khỏi thiên thạch, và người dân lại trách anh vì mảnh vỡ làm hỏng nhà cửa.

[pause] Có lúc anh hạ vua biển sâu, rồi cố ý nói rằng các anh hùng khác đã làm quái vật yếu đi, để họ không bị coi thường. Anh nhận tiếng xấu thay cho họ.

[pause] Và Saitama cũng không thật sự quan tâm. Anh muốn được công nhận, nhưng không muốn nổi tiếng bằng cách nói dối. Anh chỉ muốn một trận đấu làm tim mình đập nhanh trở lại.

[pause] Kaku để ý: độ nổi tiếng trong truyện không đo ai làm tốt nhất, mà đo ai được nhìn thấy nhiều nhất. [curious] Nghe có quen với mạng xã hội ngày nay không?

[pause] Giờ tới những ca khiến bảng xếp hạng trở nên thú vị nhất.

[pause] Ca một: King, anh hùng hạng S thứ bảy, được gọi là người mạnh nhất Trái Đất. Sự thật: anh không có sức mạnh gì cả. Mọi chiến công của anh thật ra là do Saitama làm, và người ta nhầm là King.

[pause] Tiếng tim đập của King khi sợ hãi vang to tới mức kẻ thù nghe thấy, và tưởng đó là âm thanh của một chiến binh sắp ra đòn. Anh thắng nhiều trận chỉ bằng danh tiếng.

[pause] Ca hai: Mumen Rider, anh hùng số một hạng C, đi xe đạp. Anh yếu, và anh biết mình yếu.

[pause] Nhưng khi vua biển sâu tấn công, Mumen Rider vẫn lao tới, dù biết mình không có cơ hội thắng. Anh nói, đại ý: tôi biết mình không thắng được, nhưng tôi vẫn phải chiến đấu.

[pause] Và đám đông, những người đã trách mọi anh hùng, lại cổ vũ Mumen Rider. Vì họ thấy lòng dũng cảm thật.

[pause] Ca ba: Tatsumaki, hạng S thứ hai, một nhà ngoại cảm cực mạnh, có thể nâng cả những khối đá khổng lồ. Cô mạnh thật, và danh tiếng của cô xứng đáng.

[pause] Nghĩa là bảng xếp hạng đôi khi đúng, đôi khi sai, và đôi khi sai theo cả hai chiều: đánh giá thấp người mạnh, đánh giá cao người yếu.
```

### c06 · Anh hùng săn anh hùng / Khi quái vật cũng có tổ chức

Khoảng 99 giây · cảnh s61–s69 · 1284 ký tự

**Gemini**

```text
Có một nhân vật lật ngược cả hệ thống: Garou, kẻ tự gọi mình là thợ săn anh hùng. Hắn đi đánh bại từng anh hùng một.

<short pause> Garou không tin vào bảng xếp hạng. Hắn nghĩ những anh hùng chỉ là kẻ mạnh bắt nạt kẻ yếu, và quái vật mới là phe bị đối xử bất công.

<short pause> Điều thú vị là Garou từng là học trò của võ sư Bang, người đứng hạng S thứ ba. Một người được bảng xếp hạng vinh danh, và một người quay lưng với nó, xuất phát từ cùng một võ đường.

<short pause> Hắn cũng là một câu hỏi cho chính hệ thống: nếu anh hùng được đánh giá bằng sức mạnh và danh tiếng, thì ai được coi là người tốt thật sự?

<short pause> Arc của Garou kéo dài sang mùa ba, và Kaku sẽ không nói trước kết quả. Chỉ biết rằng hắn là một trong những nhân vật được yêu thích nhất truyện.

<short pause> Ở mùa hai và mùa ba, thế giới One Punch Man có thêm một hệ thống thứ ba: Hiệp hội Quái vật, một tổ chức của chính các quái vật, với thủ lĩnh và cán bộ riêng.

<short pause> Nhiều cán bộ của tổ chức này được xếp cấp Rồng. Nghĩa là cùng lúc có nhiều mối đe dọa cấp Rồng, thứ mà bảng xếp hạng chưa từng tính tới.

<short pause> Cuộc đối đầu giữa hai hiệp hội là phép thử lớn nhất cho bảng xếp hạng. Ai thật sự mạnh, ai chỉ có danh tiếng, sẽ lộ ra khi áp lực đủ lớn.

<short pause> Kaku sẽ không nói trước diễn biến, vì mùa ba vẫn đang kể phần này. <short pause> Nhưng nếu bạn thích bảng xếp hạng, arc này là nơi nó bị thử thách nhiều nhất.
```

**ElevenLabs**

```text
Có một nhân vật lật ngược cả hệ thống: Garou, kẻ tự gọi mình là thợ săn anh hùng. Hắn đi đánh bại từng anh hùng một.

[pause] Garou không tin vào bảng xếp hạng. Hắn nghĩ những anh hùng chỉ là kẻ mạnh bắt nạt kẻ yếu, và quái vật mới là phe bị đối xử bất công.

[pause] Điều thú vị là Garou từng là học trò của võ sư Bang, người đứng hạng S thứ ba. Một người được bảng xếp hạng vinh danh, và một người quay lưng với nó, xuất phát từ cùng một võ đường.

[pause] [curious] Hắn cũng là một câu hỏi cho chính hệ thống: nếu anh hùng được đánh giá bằng sức mạnh và danh tiếng, thì ai được coi là người tốt thật sự?

[pause] Arc của Garou kéo dài sang mùa ba, và Kaku sẽ không nói trước kết quả. Chỉ biết rằng hắn là một trong những nhân vật được yêu thích nhất truyện.

[pause] Ở mùa hai và mùa ba, thế giới One Punch Man có thêm một hệ thống thứ ba: Hiệp hội Quái vật, một tổ chức của chính các quái vật, với thủ lĩnh và cán bộ riêng.

[pause] Nhiều cán bộ của tổ chức này được xếp cấp Rồng. Nghĩa là cùng lúc có nhiều mối đe dọa cấp Rồng, thứ mà bảng xếp hạng chưa từng tính tới.

[pause] Cuộc đối đầu giữa hai hiệp hội là phép thử lớn nhất cho bảng xếp hạng. Ai thật sự mạnh, ai chỉ có danh tiếng, sẽ lộ ra khi áp lực đủ lớn.

[pause] Kaku sẽ không nói trước diễn biến, vì mùa ba vẫn đang kể phần này. [pause] Nhưng nếu bạn thích bảng xếp hạng, arc này là nơi nó bị thử thách nhiều nhất.
```

### c07 · Giới hạn của những con số / Trò chơi: thẻ chỉ số của bạn

Khoảng 127 giây · cảnh s70–s84 · 1650 ký tự

**Gemini**

```text
Vậy những con số trong One Punch Man cho ta biết gì? Kaku thấy có ba giới hạn.

<short pause> Nói cách khác, Hiệp hội chấm điểm theo bằng chứng. Mà Saitama thì luôn đi về trước khi có người tới chụp ảnh.

<short pause> Giới hạn một: con số đo cái được nhìn thấy, không đo cái thật. Saitama mạnh nhất nhưng ở hạng thấp, vì không ai thấy anh làm gì.

<short pause> Giới hạn hai: con số không đo được lòng dũng cảm. Mumen Rider yếu, nhưng dũng cảm hơn nhiều anh hùng mạnh hơn anh.

<short pause> Giới hạn ba: con số có thể bị lừa. King ở hạng S chỉ vì danh tiếng. Một hệ thống dựa vào tin đồn sẽ luôn có những King.

<short pause> Và có một giới hạn cuối, rất buồn: Saitama đã mạnh tới mức không còn thấy hứng thú khi chiến đấu. Mọi trận đều kết thúc bằng một cú đấm. Anh mất đi cảm giác hồi hộp.

<short pause> Có lẽ vì vậy mà Saitama không quan tâm tới thứ hạng. Thứ anh muốn không phải con số, mà là một đối thủ khiến anh cảm thấy mình đang sống.

<short pause> Nghĩa là con số cao nhất cũng có giá. Khi bạn không còn ai để thử thách, sức mạnh trở thành một sự cô đơn.

<short pause> Giờ tới lượt bạn. Hãy tự điền thẻ chỉ số anh hùng của mình.

<short pause> Một: bạn sẽ đậu kỳ thi với bao nhiêu điểm? Thể lực bao nhiêu, bài viết bao nhiêu?

<short pause> Hai: bạn thuộc hạng nào, và bạn chọn làm số một hạng dưới, hay người cuối hạng trên?

<short pause> Ba: bạn đủ sức đối đầu với quái vật cấp nào? Và nếu gặp một con cấp Quỷ, bạn có lao lên như Mumen Rider không?

<short pause> Năm: nếu bạn giỏi hơn người ở hạng trên mà vẫn bị xếp hạng thấp, bạn sẽ tức giận, hay cứ tiếp tục làm việc của mình như Saitama?

<short pause> Bốn, chỉ số ẩn: nếu bạn cứu cả thành phố mà không ai biết, bạn có còn làm không?

<short pause> <laugh> Thẻ của Kaku: thể lực hai điểm, bài viết mười điểm, hạng C, cấp Sói cũng hơi run. <short pause> Nhưng chỉ số ẩn thì Kaku tự chấm cao. Còn bạn? Viết vào bình luận nhé.
```

**ElevenLabs**

```text
[curious] Vậy những con số trong One Punch Man cho ta biết gì? Kaku thấy có ba giới hạn.

[pause] Nói cách khác, Hiệp hội chấm điểm theo bằng chứng. Mà Saitama thì luôn đi về trước khi có người tới chụp ảnh.

[pause] Giới hạn một: con số đo cái được nhìn thấy, không đo cái thật. Saitama mạnh nhất nhưng ở hạng thấp, vì không ai thấy anh làm gì.

[pause] Giới hạn hai: con số không đo được lòng dũng cảm. Mumen Rider yếu, nhưng dũng cảm hơn nhiều anh hùng mạnh hơn anh.

[pause] Giới hạn ba: con số có thể bị lừa. King ở hạng S chỉ vì danh tiếng. Một hệ thống dựa vào tin đồn sẽ luôn có những King.

[pause] Và có một giới hạn cuối, rất buồn: Saitama đã mạnh tới mức không còn thấy hứng thú khi chiến đấu. Mọi trận đều kết thúc bằng một cú đấm. Anh mất đi cảm giác hồi hộp.

[pause] Có lẽ vì vậy mà Saitama không quan tâm tới thứ hạng. Thứ anh muốn không phải con số, mà là một đối thủ khiến anh cảm thấy mình đang sống.

[pause] Nghĩa là con số cao nhất cũng có giá. Khi bạn không còn ai để thử thách, sức mạnh trở thành một sự cô đơn.

[pause] Giờ tới lượt bạn. Hãy tự điền thẻ chỉ số anh hùng của mình.

[pause] Một: bạn sẽ đậu kỳ thi với bao nhiêu điểm? Thể lực bao nhiêu, bài viết bao nhiêu?

[pause] Hai: bạn thuộc hạng nào, và bạn chọn làm số một hạng dưới, hay người cuối hạng trên?

[pause] Ba: bạn đủ sức đối đầu với quái vật cấp nào? Và nếu gặp một con cấp Quỷ, bạn có lao lên như Mumen Rider không?

[pause] Năm: nếu bạn giỏi hơn người ở hạng trên mà vẫn bị xếp hạng thấp, bạn sẽ tức giận, hay cứ tiếp tục làm việc của mình như Saitama?

[pause] Bốn, chỉ số ẩn: nếu bạn cứu cả thành phố mà không ai biết, bạn có còn làm không?

[pause] [chuckles] Thẻ của Kaku: thể lực hai điểm, bài viết mười điểm, hạng C, cấp Sói cũng hơi run. [pause] Nhưng chỉ số ẩn thì Kaku tự chấm cao. Còn bạn? Viết vào bình luận nhé.
```

### c08 · Kết

Khoảng 50 giây · cảnh s85–s88 · 653 ký tự

**Gemini**

```text
One Punch Man là một bộ truyện giả vờ nói về sức mạnh, nhưng thật ra nói về việc con người đánh giá nhau thế nào. Và những con số trên bảng xếp hạng không bao giờ kể hết câu chuyện.

<short pause> Và lần tới bạn nhìn thấy một bảng xếp hạng, dù ở trường, ở công ty, hay trên mạng, hãy nhớ tới Saitama: con số chỉ là một phần của câu chuyện.

<short pause> Video tiếp theo, Kaku mở một cuốn sử hoài niệm: Yu-Gi-Oh! và lịch sử luật bài, từ Fusion, Ritual, tới Synchro, Xyz, Pendulum và Link.

<short pause> <laugh> Nếu bạn thích xem Kaku đọc thẻ chỉ số, hãy đăng ký kênh. Thứ hạng của Kaku có thể thấp, nhưng Kaku sẽ tiếp tục ra một video mỗi tuần, như một anh hùng hạng C chăm chỉ. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
One Punch Man là một bộ truyện giả vờ nói về sức mạnh, nhưng thật ra nói về việc con người đánh giá nhau thế nào. Và những con số trên bảng xếp hạng không bao giờ kể hết câu chuyện.

[pause] Và lần tới bạn nhìn thấy một bảng xếp hạng, dù ở trường, ở công ty, hay trên mạng, hãy nhớ tới Saitama: con số chỉ là một phần của câu chuyện.

[pause] Video tiếp theo, Kaku mở một cuốn sử hoài niệm: Yu-Gi-Oh! và lịch sử luật bài, từ Fusion, Ritual, tới Synchro, Xyz, Pendulum và Link.

[pause] [chuckles] Nếu bạn thích xem Kaku đọc thẻ chỉ số, hãy đăng ký kênh. Thứ hạng của Kaku có thể thấp, nhưng Kaku sẽ tiếp tục ra một video mỗi tuần, như một anh hùng hạng C chăm chỉ. Kaku gấp sổ đây, hẹn gặp lại!
```
