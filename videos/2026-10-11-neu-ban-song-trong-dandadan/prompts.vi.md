# Bộ prompt · Dandadan: Nếu bạn sống trong thế giới có cả ma lẫn người ngoài hành tinh

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 9 đoạn đọc, khoảng 15.2 phút giọng.
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

Lời: Cảnh báo: video có spoiler Dandadan tới hết anime mùa một và một phần mùa hai. Kaku sẽ không nói về những gì…

```text
Wide 16:9 landscape cinematic frame. a quiet Japanese suburban street at night under a flickering streetlight. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Giả sử sáng mai bạn tỉnh dậy ở một thị trấn nhỏ của Nhật Bản. Mọi thứ trông bình thường, cho tới khi bạn biết…

```text
Wide 16:9 landscape cinematic frame. a teenager waking up in a small bedroom, a ghostly hand on the window and a UFO light in the sky outside. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đây là thế giới của Dandadan. Và hôm nay, người bước vào thế giới đó không phải nhân vật chính, mà là bạn.

```text
Wide 16:9 landscape cinematic frame. a silhouette of the viewer standing at a crossroads, one path lit purple and one lit green. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku, và hôm nay Kaku làm người dẫn trò. Bạn sẽ sống qua năm đêm, mỗi đêm có một lựa ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot as a game master behind a small screen, a health bar showing 100. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy ghi lại lựa chọn của mình, rồi so với kết quả. Cuối video, Kaku sẽ nói bạn sống sót được bao lâu. Đừng gi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot handing a small pencil and score sheet toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Thế giới này là gì?

Lời: Dandadan là manga của Tatsu Yukinobu, đăng trên nền tảng Shonen Jump Plus từ năm 2021. Trước đó, tác giả từng…

```text
Wide 16:9 landscape cinematic frame. a cluttered manga artist desk at night with sketches of ghosts and flying saucers. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Bản anime do Science Saru thực hiện, mùa một ra năm 2024, mùa hai năm 2025, và mùa ba đã được xác nhận cho nă…

```text
Wide 16:9 landscape cinematic frame. three film reels labeled with years, the last one wrapped in a ribbon. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Tại lễ trao giải anime của Crunchyroll năm 2026, Dandadan là bộ có nhiều đề cử nhất, tới hai mươi đề cử.

```text
Wide 16:9 landscape cinematic frame. a glowing trophy shelf with twenty small stars around it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Câu chuyện bắt đầu với hai học sinh cá cược với nhau. Cô gái tin có ma nhưng không tin người ngoài hành tinh.…

```text
Wide 16:9 landscape cinematic frame. two teenagers arguing on a school rooftop, one holding a ghost charm, the other an alien magazine. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Mỗi người đến nơi mà người kia tin là có chuyện lạ, để chứng minh mình đúng. Và cả hai đều đúng. Đó là lúc mọ…

```text
Wide 16:9 landscape cinematic frame. a split scene: a girl under a UFO beam on a hill, a boy in a dark tunnel with a ghostly figure behind him. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Tên truyện cũng rất vui tai. Nhiều người đọc nó như một tiếng động mạnh, giống tiếng trống hay tiếng bước châ…

```text
Wide 16:9 landscape cinematic frame. a big drum being struck with bold comic-style sound effect shapes bursting out. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Dandadan pha trộn kinh dị, hành động, hài và cả lãng mạn tuổi học trò, với tốc độ nhanh đến chó…

```text
Wide 16:9 landscape cinematic frame. the owl mascot spinning dizzily with tiny ghosts and UFOs orbiting its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Đêm 1: Cuộc cá cược

Lời: Đêm đầu tiên. Một người bạn cùng lớp thách bạn chứng minh niềm tin của mình. Bạn có hai lựa chọn.

```text
Wide 16:9 landscape cinematic frame. a school hallway at dusk, a classmate pointing a challenging finger at the viewer. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Lựa chọn A: đi vào một đường hầm bỏ hoang, nơi người ta đồn có một bà lão chạy nhanh hơn cả xe hơi. Lựa chọn…

```text
Wide 16:9 landscape cinematic frame. two cards on a table: a dark tunnel entrance and a lonely hill under a strange light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Nếu bạn chọn A: bà lão trong đường hầm là một yêu quái đuổi theo nạn nhân với tốc độ khủng khiếp. Không ai ch…

```text
Wide 16:9 landscape cinematic frame. a ghostly old woman sprinting at impossible speed through a dark tunnel, motion lines behind her. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Trong truyện, bà ta còn lấy đi của nạn nhân một thứ rất quan trọng, và muốn lấy lại thì phải đi một hành trìn…

```text
Wide 16:9 landscape cinematic frame. a small glowing object floating away into darkness, a health bar dropping. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nếu bạn chọn B: một nhóm người ngoài hành tinh sẽ bắt cóc bạn lên đĩa bay. Họ có những mục đích rất đáng lo n…

```text
Wide 16:9 landscape cinematic frame. a teenager floating up in a beam of light toward a saucer, tall grey figures waiting inside. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhưng trong truyện, chính cú sốc khi bị bắt cóc đã đánh thức năng lực siêu linh của cô gái. Nếu bạn may mắn n…

```text
Wide 16:9 landscape cinematic frame. a girl's eyes glowing as translucent energy hands burst out around her inside a spaceship. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Còn nếu bạn không đi đâu cả và ở nhà ngủ? Trong thế giới này, chuyện lạ vẫn sẽ tự tìm đến. Kaku tính như chọn…

```text
Wide 16:9 landscape cinematic frame. a teenager sleeping in bed while a strange light and a ghostly shadow both appear at the window. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: không có lựa chọn an toàn. Trong thế giới này, cứ tò mò là trả giá. Nhưng không tò mò thì chẳng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking nervously around a corner with a flashlight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Đêm 2: Sức mạnh thức tỉnh

Lời: Sống sót qua đêm đầu, bạn nhận ra mình đã thay đổi. Trong Dandadan, con người có thể có sức mạnh theo vài con…

```text
Wide 16:9 landscape cinematic frame. a teenager looking at their glowing hands in a bathroom mirror at night. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Con đường thứ nhất: năng lực siêu linh. Người có năng lực này có thể di chuyển đồ vật, trói đối thủ, thậm chí…

```text
Wide 16:9 landscape cinematic frame. translucent glowing hands lifting a car off the ground in a parking lot. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Con đường thứ hai: mang một yêu quái trong người. Cậu bạn trong truyện bị bà lão yêu quái nhập, và nhờ đó có…

```text
Wide 16:9 landscape cinematic frame. a boy whose silhouette flickers with a ghostly aura, his hair standing up, speed lines around him. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Lựa chọn của bạn: A, chấp nhận để một yêu quái sống trong cơ thể, nhận sức mạnh ngay lập tức. B, tự luyện năn…

```text
Wide 16:9 landscape cinematic frame. two doors: one with a ghostly face on it, the other with a glowing hand symbol. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nếu chọn A: bạn nhanh và mạnh ngay, nhưng có một cái giá. Truyện cho thấy sức mạnh đó không thể dùng quá nhiề…

```text
Wide 16:9 landscape cinematic frame. a boy collapsing after a burst of speed, cracks of light across his arms. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nếu chọn B: bạn yếu hơn trong vài trận đầu và phải dựa vào người khác. Trừ mười lăm điểm. Nhưng sức mạnh đó h…

```text
Wide 16:9 landscape cinematic frame. a teenager practicing lifting pebbles with a faint glowing hand in a backyard. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và còn một con đường thứ ba: dòng máu. Có những gia đình đời đời làm nghề trừ tà, và sức mạnh cảm nhận ma quỷ…

```text
Wide 16:9 landscape cinematic frame. an old family shrine with generations of photographs and a glowing protective charm. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu Kaku có một yêu quái trong người, chắc nó sẽ bắt Kaku chạy bộ mỗi sáng. Kaku chọn B.

```text
Wide 16:9 landscape cinematic frame. the owl mascot jogging with a sweatband, a tiny ghost yelling at it from behind. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Đêm 3: Truyền thuyết đô thị

Lời: Đêm thứ ba, thị trấn xôn xao vì một tin đồn: có người phụ nữ cao lớn, tóc dài, mặc váy đỏ, nhảy qua các mái n…

```text
Wide 16:9 landscape cinematic frame. a tall figure with long hair in a red dress leaping between rooftops under a full moon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Yêu quái trong Dandadan thường lấy cảm hứng từ những truyền thuyết đô thị có thật của Nhật Bản. Người phụ nữ…

```text
Wide 16:9 landscape cinematic frame. an old internet forum page on a glowing monitor, a blurry photo of a figure on a rooftop. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Lựa chọn của bạn: A, lao vào đánh ngay vì đó là yêu quái. B, tìm hiểu vì sao cô ta xuất hiện ở thị trấn này.

```text
Wide 16:9 landscape cinematic frame. a teenager on a rooftop at night deciding between a raised fist and an open hand. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nếu chọn A: bạn có thể thắng, nhưng bạn sẽ bỏ lỡ điều quan trọng nhất. Trừ hai mươi điểm, vì yêu quái này rất…

```text
Wide 16:9 landscape cinematic frame. a violent clash on a rooftop, tiles flying, a health bar dropping. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nếu chọn B: bạn sẽ biết rằng đằng sau yêu quái là câu chuyện đau lòng của một người mẹ, gắn với một người mà…

```text
Wide 16:9 landscape cinematic frame. a faded photograph of a mother holding a small child, soft light on a rooftop. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Đây là arc được nhiều người xem nhắc tới nhất ở mùa một, vì nó biến một con quái vật đáng sợ thành một câu ch…

```text
Wide 16:9 landscape cinematic frame. a single red ribbon drifting down from a rooftop into morning light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong Dandadan, hiểu kẻ thù nhiều khi quan trọng hơn đánh bại kẻ thù. Bài học này đúng cả ngoài…

```text
Wide 16:9 landscape cinematic frame. the owl mascot offering a small tissue to a tiny sad ghost. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Đêm 4: Thị trấn bị tấn công

Lời: Đêm thứ tư, bầu trời thị trấn đầy những ánh sáng lạ. Người ngoài hành tinh quay lại, và lần này họ không đến…

```text
Wide 16:9 landscape cinematic frame. a sky full of strange lights over a small town, silhouettes of odd creatures descending. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Người ngoài hành tinh trong Dandadan có đủ loại hình dạng, từ những dáng người xám quen thuộc tới những sinh…

```text
Wide 16:9 landscape cinematic frame. a lineup of alien silhouettes: a tall grey figure, a hulking beast, and a tiny floating creature. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Lựa chọn của bạn: A, trốn trong nhà và chờ sáng. B, chạy thật xa khỏi thị trấn. C, gọi bạn bè có năng lực đến…

```text
Wide 16:9 landscape cinematic frame. three cards: a locked door, a running shoe, and a phone glowing with contacts. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nếu chọn A: trong thế giới này, cửa khóa không cản được thứ gì. Trừ ba mươi điểm. Nếu chọn B: bạn sống sót, n…

```text
Wide 16:9 landscape cinematic frame. a door melting open under an eerie light, and a lone figure running on an empty highway. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nếu chọn C: bạn không phải đối mặt một mình. Trong truyện, hầu như mọi trận đánh lớn đều được giải quyết nhờ…

```text
Wide 16:9 landscape cinematic frame. a small group of teenagers standing back to back under a sky full of lights, glowing hands raised. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Chi tiết thú vị: trận đánh trong truyện thường vừa kinh dị vừa buồn cười, như người ngoài hành tinh vừa đánh…

```text
Wide 16:9 landscape cinematic frame. a chaotic battle scene where an alien and a teenager are arguing mid-fight, sweat drops flying. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là đêm quyết định. Những ai tự xoay xở một mình thường mất nhiều điểm nhất. Dandadan là câu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding hands with a tiny ghost and a tiny alien in a circle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Đêm 5: Chọn đồng đội

Lời: Đêm cuối cùng. Bạn được chọn một đồng đội để cùng đối mặt thử thách lớn nhất. Đây là ba ứng viên.

```text
Wide 16:9 landscape cinematic frame. three silhouettes standing in fog, each with a different glowing aura. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Ứng viên một: một bà đồng lớn tuổi, nóng tính nhưng hiểu biết sâu về ma quỷ, có thể dựng kết giới và nói chuy…

```text
Wide 16:9 landscape cinematic frame. an elderly woman with a stern face holding prayer beads, a glowing barrier around a house. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Ứng viên hai: một bạn học có sức mạnh từ yêu quái, rất mạnh trong chiến đấu nhưng khó đoán và hay tự ái.

```text
Wide 16:9 landscape cinematic frame. a proud teenager with a flickering supernatural aura, arms crossed on a rooftop. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Ứng viên ba: một cậu bạn mê khoa học viễn tưởng, không có sức mạnh gì nhưng rất giỏi máy móc và luôn có một k…

```text
Wide 16:9 landscape cinematic frame. a nerdy teenager with goggles tinkering with a strange homemade device in a garage. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Kết quả: chọn bà đồng thì trừ năm điểm, vì kinh nghiệm cứu bạn khỏi những cái bẫy mà bạn không biết. Chọn ngư…

```text
Wide 16:9 landscape cinematic frame. a health bar with small deductions labeled by icons of prayer beads and a ghostly aura. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Chọn người mê máy móc thì trừ mười lăm điểm, nhưng bạn có những khoảnh khắc buồn cười nhất đêm đó. Trong Dand…

```text
Wide 16:9 landscape cinematic frame. a ridiculous homemade robot collapsing in a heap while teenagers laugh. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Đêm thưởng: Con mèo may mắn

Lời: Khoan đã, còn một đêm thưởng mà Kaku giấu từ đầu. Sau khi mọi chuyện lắng xuống, bạn nhận được một món quà kỳ…

```text
Wide 16:9 landscape cinematic frame. a small ceramic lucky cat figurine with a raised paw sitting on a windowsill at night. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Trong truyện, sau trận đấu trong đường hầm, linh hồn bà lão yêu quái bị nhốt vào một bức tượng mèo may mắn, v…

```text
Wide 16:9 landscape cinematic frame. a lucky cat figurine with a faint ghostly grumpy face glowing inside it, on a kitchen shelf. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Bà ta vẫn cáu kỉnh, vẫn đòi hỏi, nhưng dần dần trở thành một thành viên kỳ quặc của nhóm. Có nguồn còn nói bà…

```text
Wide 16:9 landscape cinematic frame. a grumpy lucky cat figurine sitting at a family dinner table among laughing teenagers. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Lựa chọn của bạn: A, giữ bức tượng trong nhà. B, vứt nó ra bãi rác thật xa.

```text
Wide 16:9 landscape cinematic frame. two cards: a cozy shelf and a garbage bin on a dark street. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nếu chọn A: cộng mười điểm. Một yêu quái từng muốn hại bạn giờ trở thành đồng minh, dù hơi khó chịu. Nếu chọn…

```text
Wide 16:9 landscape cinematic frame. a health bar rising with a small cat icon, and a small angry ghost climbing out of a trash bin. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là một điểm rất Dandadan. Kẻ thù hôm qua có thể là người nhà hôm nay, miễn là bạn đủ kiên n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sharing a cup of tea with a grumpy lucky cat figurine. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Bảng điểm sống sót

Lời: Giờ hãy cộng điểm. Bạn bắt đầu với một trăm, trừ đi điểm của năm đêm, rồi cộng hoặc trừ điểm của đêm thưởng.…

```text
Wide 16:9 landscape cinematic frame. a scoreboard with five rows and a total at the bottom, chalk in the owl mascot's wing. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Từ năm mươi điểm trở lên: bạn là một thành viên thực thụ của nhóm, đủ bản lĩnh để sống sót tới cuối mùa và cò…

```text
Wide 16:9 landscape cinematic frame. a confident teenager standing with friends at sunrise over the town. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Từ hai mươi lăm đến bốn mươi chín điểm: bạn sống sót, nhưng với vài vết sẹo và một nỗi sợ đường hầm suốt đời.

```text
Wide 16:9 landscape cinematic frame. a teenager with bandages avoiding a tunnel entrance on the way to school. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Dưới hai mươi lăm điểm: bạn đã trở thành một truyền thuyết đô thị mới của thị trấn. Chúc mừng, theo một cách…

```text
Wide 16:9 landscape cinematic frame. a new rumor posted on a school bulletin board with a blurry silhouette photo. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử chơi và được năm mươi lăm điểm: lên ngọn đồi, tự luyện năng lực, tìm hiểu yêu quái, gọi bạn bè, chọn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding a score sheet showing 55 points. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Nếu bạn là người ngoài hành tinh

Lời: Giờ hãy đảo ngược trò chơi. Nếu bạn là một người ngoài hành tinh vừa hạ cánh xuống thị trấn đó thì sao?

```text
Wide 16:9 landscape cinematic frame. a small saucer landing in a rice field at night, a curious alien peeking out of the hatch. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Bạn đến với công nghệ vượt xa loài người, tàu bay, tia sáng, và những thiết bị có thể biến đổi cơ thể. Theo m…

```text
Wide 16:9 landscape cinematic frame. an alien control room with glowing panels and holographic maps of the town. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nhưng bạn không biết rằng hành tinh này còn có ma. Những thứ mà máy quét của bạn không đo được, và vũ khí của…

```text
Wide 16:9 landscape cinematic frame. an alien scanner screen showing nothing while a ghost floats right behind the alien. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Trong Dandadan, nhiều người ngoài hành tinh đánh giá thấp loài người, rồi bất ngờ trước năng lực siêu linh và…

```text
Wide 16:9 landscape cinematic frame. a smug alien laughing, then shocked as glowing hands grab its ship. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: dù bạn là người hay người ngoài hành tinh, luật của thế giới này vẫn giống nhau: đừng coi thườn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny foil hat, nodding wisely. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Truyền thuyết thật đằng sau

Lời: Điều làm Dandadan đặc biệt là rất nhiều yêu quái và người ngoài hành tinh trong truyện đến từ những câu chuyệ…

```text
Wide 16:9 landscape cinematic frame. a scrapbook of newspaper clippings about ghost sightings and UFOs, pinned with thumbtacks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Bà lão chạy siêu tốc là một truyền thuyết đô thị nổi tiếng ở Nhật Bản. Người ta đồn về một bà lão chạy song s…

```text
Wide 16:9 landscape cinematic frame. a mountain road at night, headlights of a car and a small hunched figure running alongside it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Người phụ nữ nhào lộn váy đỏ cũng là một câu chuyện lan truyền trên các diễn đàn mạng Nhật Bản, với những lần…

```text
Wide 16:9 landscape cinematic frame. a glowing computer screen at night showing a forum thread with a blurry rooftop figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Còn những người ngoài hành tinh xám, mắt to, đầu lớn, bắt cóc người để nghiên cứu là hình ảnh quen thuộc tron…

```text
Wide 16:9 landscape cinematic frame. a vintage magazine cover with a grey alien illustration and bold retro typography. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Tên của nhóm người ngoài hành tinh đầu tiên trong truyện còn gợi nhớ một câu chuyện trên mạng về chương trình…

```text
Wide 16:9 landscape cinematic frame. a stack of fake classified documents with a question mark stamp on top. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là cách xây thế giới rất thông minh: lấy những câu chuyện người ta kể trong đêm khuya, rồi hỏi,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot telling a spooky story with a flashlight under its chin to a circle of tiny listeners. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Góc nhìn của Kaku: vì sao ma và người ngoài hành tinh? · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao tác giả đặt ma và người ngoài hành tinh vào cùng một câu chuyện? Kaku có một giả thuyết.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a Venn diagram with a ghost on one side and a UFO on the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Cả hai đều là những thứ người lớn thường bảo là không có thật. Nhưng hai nhân vật chính mỗi người tin một nửa…

```text
Wide 16:9 landscape cinematic frame. two teenagers each covering one eye, looking at a single sky full of both ghosts and UFOs. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Câu chuyện bắt đầu khi cả hai phải thừa nhận mình đã sai một nửa. Đó là cách hai con người khác biệt bắt đầu…

```text
Wide 16:9 landscape cinematic frame. two teenagers finally standing side by side, looking at the same strange sky together. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nên dù có quái vật, có đĩa bay, có những cảnh hài vô lý, Dandadan về cơ bản là câu chuyện về việc mở lòng với…

```text
Wide 16:9 landscape cinematic frame. a door opening in a dark room, light pouring in with small ghost and alien silhouettes in it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Kaku cũng thích cách truyện đối xử với những người bị coi là kỳ quặc. Cậu bạn mê người ngoài hành tinh bị cả…

```text
Wide 16:9 landscape cinematic frame. a lonely boy with an alien magazine at the back of a classroom, then the same boy shielding his friends. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Và có lẽ đó là lý do nó hợp với tuổi học trò đến vậy: ai cũng từng chắc chắn mình đúng, cho tới khi gặp một n…

```text
Wide 16:9 landscape cinematic frame. a school rooftop at sunset with two bags side by side and a small UFO keychain. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · 5 mẹo sống sót của Kaku

Lời: Nếu một ngày bạn thật sự tỉnh dậy trong thế giới đó, đây là năm mẹo sống sót Kaku rút ra từ trò chơi hôm nay.

```text
Wide 16:9 landscape cinematic frame. a handwritten survival checklist taped to a bedroom door. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Một: đừng bao giờ đi vào đường hầm bỏ hoang vào ban đêm, dù bạn có tin ma hay không. Hai: nếu bị bắt cóc, hãy…

```text
Wide 16:9 landscape cinematic frame. a tunnel entrance with a do-not-enter sign and a calm figure floating in a UFO beam. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Ba: trước khi đánh một yêu quái, hãy hỏi vì sao nó ở đó. Bốn: luôn có bạn bè ở bên, vì cả nhóm mạnh hơn bất k…

```text
Wide 16:9 landscape cinematic frame. a teenager kneeling to talk with a small sad spirit, friends standing behind. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Năm: hãy tìm một bà đồng giỏi và đối xử tốt với bà ấy. Thật đấy.

```text
Wide 16:9 landscape cinematic frame. an elderly woman with prayer beads nodding approvingly, a cup of tea in front of her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và một mẹo tặng thêm: đừng bao giờ cá cược về những thứ bạn không tin. Cả câu chuyện Dandadan bắt đầu từ một…

```text
Wide 16:9 landscape cinematic frame. two hands shaking on a bet as a ghost and an alien silently watch from behind. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Tóm lại: trong thế giới Dandadan, cả ma lẫn người ngoài hành tinh đều có thật. Sức mạnh đến từ năng lực siêu…

```text
Wide 16:9 landscape cinematic frame. a summary board with ghost and UFO icons, two paths leading to glowing hands and a ghostly aura. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Và người sống sót lâu nhất không phải người mạnh nhất, mà là người chịu tìm hiểu và không đi một mình.

```text
Wide 16:9 landscape cinematic frame. a group of friends walking home at dawn, long shadows behind them. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: bạn tin vào ma, vào người ngoài hành tinh, hay cả hai? Và bạn còn lại bao nhiêu điểm sống só…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a ghost plush in one wing and a UFO toy in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tới, Kaku đổi sang một thế giới có số liệu rõ ràng hơn nhiều: bảng chỉ số của Kaiju No. 8, nơi sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a futuristic stat screen with a percentage gauge and a giant monster silhouette behind it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Người dẫn trò Kaku xin rút lui, trước khi bà lão trong đường hầm tìm tới. Hẹ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot running away comically down a street as a tiny ghostly granny chases it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thế giới này là gì?

Khoảng 125 giây · cảnh s01–s12 · 1625 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Dandadan tới hết anime mùa một và một phần mùa hai. Kaku sẽ không nói về những gì xảy ra sau đó trong manga.

<short pause> Giả sử sáng mai bạn tỉnh dậy ở một thị trấn nhỏ của Nhật Bản. Mọi thứ trông bình thường, cho tới khi bạn biết một sự thật: ma có thật, và người ngoài hành tinh cũng có thật.

<short pause> Đây là thế giới của Dandadan. Và hôm nay, người bước vào thế giới đó không phải nhân vật chính, mà là bạn.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku, và hôm nay Kaku làm người dẫn trò. Bạn sẽ sống qua năm đêm, mỗi đêm có một lựa chọn. Bạn bắt đầu với một trăm điểm sống sót.

<short pause> Hãy ghi lại lựa chọn của mình, rồi so với kết quả. Cuối video, Kaku sẽ nói bạn sống sót được bao lâu. Đừng gian lận nhé!

<short pause> Dandadan là manga của Tatsu Yukinobu, đăng trên nền tảng Shonen Jump Plus từ năm 2021. Trước đó, tác giả từng làm trợ lý cho những bộ truyện rất nổi tiếng.

<short pause> Bản anime do Science Saru thực hiện, mùa một ra năm 2024, mùa hai năm 2025, và mùa ba đã được xác nhận cho năm 2027.

<short pause> Tại lễ trao giải anime của Crunchyroll năm 2026, Dandadan là bộ có nhiều đề cử nhất, tới hai mươi đề cử.

<short pause> Câu chuyện bắt đầu với hai học sinh cá cược với nhau. Cô gái tin có ma nhưng không tin người ngoài hành tinh. Cậu bạn thì ngược lại.

<short pause> Mỗi người đến nơi mà người kia tin là có chuyện lạ, để chứng minh mình đúng. Và cả hai đều đúng. Đó là lúc mọi thứ bắt đầu hỗn loạn.

<short pause> Tên truyện cũng rất vui tai. Nhiều người đọc nó như một tiếng động mạnh, giống tiếng trống hay tiếng bước chân dồn dập, hợp với nhịp truyện lúc nào cũng hối hả.

<short pause> Kaku ghi chú: Dandadan pha trộn kinh dị, hành động, hài và cả lãng mạn tuổi học trò, với tốc độ nhanh đến chóng mặt. Chuẩn bị tinh thần nhé!
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Dandadan tới hết anime mùa một và một phần mùa hai. Kaku sẽ không nói về những gì xảy ra sau đó trong manga.

[pause] Giả sử sáng mai bạn tỉnh dậy ở một thị trấn nhỏ của Nhật Bản. Mọi thứ trông bình thường, cho tới khi bạn biết một sự thật: ma có thật, và người ngoài hành tinh cũng có thật.

[pause] Đây là thế giới của Dandadan. Và hôm nay, người bước vào thế giới đó không phải nhân vật chính, mà là bạn.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku, và hôm nay Kaku làm người dẫn trò. Bạn sẽ sống qua năm đêm, mỗi đêm có một lựa chọn. Bạn bắt đầu với một trăm điểm sống sót.

[pause] Hãy ghi lại lựa chọn của mình, rồi so với kết quả. Cuối video, Kaku sẽ nói bạn sống sót được bao lâu. Đừng gian lận nhé!

[pause] Dandadan là manga của Tatsu Yukinobu, đăng trên nền tảng Shonen Jump Plus từ năm 2021. Trước đó, tác giả từng làm trợ lý cho những bộ truyện rất nổi tiếng.

[pause] Bản anime do Science Saru thực hiện, mùa một ra năm 2024, mùa hai năm 2025, và mùa ba đã được xác nhận cho năm 2027.

[pause] Tại lễ trao giải anime của Crunchyroll năm 2026, Dandadan là bộ có nhiều đề cử nhất, tới hai mươi đề cử.

[pause] Câu chuyện bắt đầu với hai học sinh cá cược với nhau. Cô gái tin có ma nhưng không tin người ngoài hành tinh. Cậu bạn thì ngược lại.

[pause] Mỗi người đến nơi mà người kia tin là có chuyện lạ, để chứng minh mình đúng. Và cả hai đều đúng. Đó là lúc mọi thứ bắt đầu hỗn loạn.

[pause] Tên truyện cũng rất vui tai. Nhiều người đọc nó như một tiếng động mạnh, giống tiếng trống hay tiếng bước chân dồn dập, hợp với nhịp truyện lúc nào cũng hối hả.

[pause] Kaku ghi chú: Dandadan pha trộn kinh dị, hành động, hài và cả lãng mạn tuổi học trò, với tốc độ nhanh đến chóng mặt. Chuẩn bị tinh thần nhé!
```

### c02 · Đêm 1: Cuộc cá cược

Khoảng 84 giây · cảnh s13–s20 · 1091 ký tự

**Gemini**

```text
Đêm đầu tiên. Một người bạn cùng lớp thách bạn chứng minh niềm tin của mình. Bạn có hai lựa chọn.

<short pause> Lựa chọn A: đi vào một đường hầm bỏ hoang, nơi người ta đồn có một bà lão chạy nhanh hơn cả xe hơi. Lựa chọn B: lên một ngọn đồi vắng, nơi hay có ánh sáng lạ trên trời.

<short pause> Nếu bạn chọn A: bà lão trong đường hầm là một yêu quái đuổi theo nạn nhân với tốc độ khủng khiếp. Không ai chạy bộ thoát được bà ta.

<short pause> Trong truyện, bà ta còn lấy đi của nạn nhân một thứ rất quan trọng, và muốn lấy lại thì phải đi một hành trình dài và kỳ quặc. Trừ bốn mươi điểm.

<short pause> Nếu bạn chọn B: một nhóm người ngoài hành tinh sẽ bắt cóc bạn lên đĩa bay. Họ có những mục đích rất đáng lo ngại, và nói chuyện một cách vô cùng lịch sự.

<short pause> Nhưng trong truyện, chính cú sốc khi bị bắt cóc đã đánh thức năng lực siêu linh của cô gái. Nếu bạn may mắn như vậy, chỉ trừ hai mươi điểm.

<short pause> Còn nếu bạn không đi đâu cả và ở nhà ngủ? Trong thế giới này, chuyện lạ vẫn sẽ tự tìm đến. Kaku tính như chọn A cho công bằng.

<short pause> <laugh> Kaku ghi chú: không có lựa chọn an toàn. Trong thế giới này, cứ tò mò là trả giá. <short pause> Nhưng không tò mò thì chẳng có câu chuyện nào cả.
```

**ElevenLabs**

```text
Đêm đầu tiên. Một người bạn cùng lớp thách bạn chứng minh niềm tin của mình. Bạn có hai lựa chọn.

[pause] Lựa chọn A: đi vào một đường hầm bỏ hoang, nơi người ta đồn có một bà lão chạy nhanh hơn cả xe hơi. Lựa chọn B: lên một ngọn đồi vắng, nơi hay có ánh sáng lạ trên trời.

[pause] Nếu bạn chọn A: bà lão trong đường hầm là một yêu quái đuổi theo nạn nhân với tốc độ khủng khiếp. Không ai chạy bộ thoát được bà ta.

[pause] Trong truyện, bà ta còn lấy đi của nạn nhân một thứ rất quan trọng, và muốn lấy lại thì phải đi một hành trình dài và kỳ quặc. Trừ bốn mươi điểm.

[pause] Nếu bạn chọn B: một nhóm người ngoài hành tinh sẽ bắt cóc bạn lên đĩa bay. Họ có những mục đích rất đáng lo ngại, và nói chuyện một cách vô cùng lịch sự.

[pause] Nhưng trong truyện, chính cú sốc khi bị bắt cóc đã đánh thức năng lực siêu linh của cô gái. Nếu bạn may mắn như vậy, chỉ trừ hai mươi điểm.

[pause] [curious] Còn nếu bạn không đi đâu cả và ở nhà ngủ? Trong thế giới này, chuyện lạ vẫn sẽ tự tìm đến. Kaku tính như chọn A cho công bằng.

[pause] [chuckles] Kaku ghi chú: không có lựa chọn an toàn. Trong thế giới này, cứ tò mò là trả giá. [pause] Nhưng không tò mò thì chẳng có câu chuyện nào cả.
```

### c03 · Đêm 2: Sức mạnh thức tỉnh

Khoảng 90 giây · cảnh s21–s28 · 1165 ký tự

**Gemini**

```text
Sống sót qua đêm đầu, bạn nhận ra mình đã thay đổi. Trong Dandadan, con người có thể có sức mạnh theo vài con đường khác nhau.

<short pause> Con đường thứ nhất: năng lực siêu linh. Người có năng lực này có thể di chuyển đồ vật, trói đối thủ, thậm chí nhấc cả người lên bằng những bàn tay năng lượng vô hình.

<short pause> Con đường thứ hai: mang một yêu quái trong người. Cậu bạn trong truyện bị bà lão yêu quái nhập, và nhờ đó có được tốc độ và sức mạnh của bà ta.

<short pause> Lựa chọn của bạn: A, chấp nhận để một yêu quái sống trong cơ thể, nhận sức mạnh ngay lập tức. B, tự luyện năng lực siêu linh, chậm hơn nhưng là của chính mình.

<short pause> Nếu chọn A: bạn nhanh và mạnh ngay, nhưng có một cái giá. Truyện cho thấy sức mạnh đó không thể dùng quá nhiều lần liền, nếu không cơ thể sẽ bị tổn thương. Trừ mười điểm.

<short pause> Nếu chọn B: bạn yếu hơn trong vài trận đầu và phải dựa vào người khác. Trừ mười lăm điểm. <short pause> Nhưng sức mạnh đó hoàn toàn thuộc về bạn và sẽ không phản bội bạn.

<short pause> Và còn một con đường thứ ba: dòng máu. Có những gia đình đời đời làm nghề trừ tà, và sức mạnh cảm nhận ma quỷ được truyền lại qua nhiều thế hệ.

<short pause> <laugh> Kaku ghi chú: nếu Kaku có một yêu quái trong người, chắc nó sẽ bắt Kaku chạy bộ mỗi sáng. Kaku chọn B.
```

**ElevenLabs**

```text
Sống sót qua đêm đầu, bạn nhận ra mình đã thay đổi. Trong Dandadan, con người có thể có sức mạnh theo vài con đường khác nhau.

[pause] Con đường thứ nhất: năng lực siêu linh. Người có năng lực này có thể di chuyển đồ vật, trói đối thủ, thậm chí nhấc cả người lên bằng những bàn tay năng lượng vô hình.

[pause] Con đường thứ hai: mang một yêu quái trong người. Cậu bạn trong truyện bị bà lão yêu quái nhập, và nhờ đó có được tốc độ và sức mạnh của bà ta.

[pause] Lựa chọn của bạn: A, chấp nhận để một yêu quái sống trong cơ thể, nhận sức mạnh ngay lập tức. B, tự luyện năng lực siêu linh, chậm hơn nhưng là của chính mình.

[pause] Nếu chọn A: bạn nhanh và mạnh ngay, nhưng có một cái giá. Truyện cho thấy sức mạnh đó không thể dùng quá nhiều lần liền, nếu không cơ thể sẽ bị tổn thương. Trừ mười điểm.

[pause] Nếu chọn B: bạn yếu hơn trong vài trận đầu và phải dựa vào người khác. Trừ mười lăm điểm. [pause] Nhưng sức mạnh đó hoàn toàn thuộc về bạn và sẽ không phản bội bạn.

[pause] Và còn một con đường thứ ba: dòng máu. Có những gia đình đời đời làm nghề trừ tà, và sức mạnh cảm nhận ma quỷ được truyền lại qua nhiều thế hệ.

[pause] [chuckles] Kaku ghi chú: nếu Kaku có một yêu quái trong người, chắc nó sẽ bắt Kaku chạy bộ mỗi sáng. Kaku chọn B.
```

### c04 · Đêm 3: Truyền thuyết đô thị

Khoảng 75 giây · cảnh s29–s35 · 975 ký tự

**Gemini**

```text
Đêm thứ ba, thị trấn xôn xao vì một tin đồn: có người phụ nữ cao lớn, tóc dài, mặc váy đỏ, nhảy qua các mái nhà như một nghệ sĩ nhào lộn.

<short pause> Yêu quái trong Dandadan thường lấy cảm hứng từ những truyền thuyết đô thị có thật của Nhật Bản. Người phụ nữ này là một truyền thuyết lan truyền trên mạng từ nhiều năm trước.

<short pause> Lựa chọn của bạn: A, lao vào đánh ngay vì đó là yêu quái. B, tìm hiểu vì sao cô ta xuất hiện ở thị trấn này.

<short pause> Nếu chọn A: bạn có thể thắng, nhưng bạn sẽ bỏ lỡ điều quan trọng nhất. Trừ hai mươi điểm, vì yêu quái này rất mạnh và rất nhanh.

<short pause> Nếu chọn B: bạn sẽ biết rằng đằng sau yêu quái là câu chuyện đau lòng của một người mẹ, gắn với một người mà bạn quen. Chỉ trừ năm điểm, và bạn có thêm một đồng minh.

<short pause> Đây là arc được nhiều người xem nhắc tới nhất ở mùa một, vì nó biến một con quái vật đáng sợ thành một câu chuyện khiến người xem rơi nước mắt.

<short pause> <laugh> Kaku ghi chú: trong Dandadan, hiểu kẻ thù nhiều khi quan trọng hơn đánh bại kẻ thù. Bài học này đúng cả ngoài đời thật.
```

**ElevenLabs**

```text
Đêm thứ ba, thị trấn xôn xao vì một tin đồn: có người phụ nữ cao lớn, tóc dài, mặc váy đỏ, nhảy qua các mái nhà như một nghệ sĩ nhào lộn.

[pause] Yêu quái trong Dandadan thường lấy cảm hứng từ những truyền thuyết đô thị có thật của Nhật Bản. Người phụ nữ này là một truyền thuyết lan truyền trên mạng từ nhiều năm trước.

[pause] Lựa chọn của bạn: A, lao vào đánh ngay vì đó là yêu quái. B, tìm hiểu vì sao cô ta xuất hiện ở thị trấn này.

[pause] Nếu chọn A: bạn có thể thắng, nhưng bạn sẽ bỏ lỡ điều quan trọng nhất. Trừ hai mươi điểm, vì yêu quái này rất mạnh và rất nhanh.

[pause] Nếu chọn B: bạn sẽ biết rằng đằng sau yêu quái là câu chuyện đau lòng của một người mẹ, gắn với một người mà bạn quen. Chỉ trừ năm điểm, và bạn có thêm một đồng minh.

[pause] Đây là arc được nhiều người xem nhắc tới nhất ở mùa một, vì nó biến một con quái vật đáng sợ thành một câu chuyện khiến người xem rơi nước mắt.

[pause] [chuckles] Kaku ghi chú: trong Dandadan, hiểu kẻ thù nhiều khi quan trọng hơn đánh bại kẻ thù. Bài học này đúng cả ngoài đời thật.
```

### c05 · Đêm 4: Thị trấn bị tấn công / Đêm 5: Chọn đồng đội

Khoảng 139 giây · cảnh s36–s48 · 1813 ký tự

**Gemini**

```text
Đêm thứ tư, bầu trời thị trấn đầy những ánh sáng lạ. Người ngoài hành tinh quay lại, và lần này họ không đến một mình.

<short pause> Người ngoài hành tinh trong Dandadan có đủ loại hình dạng, từ những dáng người xám quen thuộc tới những sinh vật khổng lồ như quái vật trong phim.

<short pause> Lựa chọn của bạn: A, trốn trong nhà và chờ sáng. B, chạy thật xa khỏi thị trấn. C, gọi bạn bè có năng lực đến giúp.

<short pause> Nếu chọn A: trong thế giới này, cửa khóa không cản được thứ gì. Trừ ba mươi điểm. Nếu chọn B: bạn sống sót, nhưng thị trấn thì không. Trừ hai mươi điểm và mất luôn đồng minh.

<short pause> Nếu chọn C: bạn không phải đối mặt một mình. Trong truyện, hầu như mọi trận đánh lớn đều được giải quyết nhờ cả nhóm. Chỉ trừ mười điểm.

<short pause> Chi tiết thú vị: trận đánh trong truyện thường vừa kinh dị vừa buồn cười, như người ngoài hành tinh vừa đánh vừa cãi nhau, hay nhân vật chính hét những câu rất ngớ ngẩn giữa lúc nguy hiểm.

<short pause> <laugh> Kaku ghi chú: đây là đêm quyết định. Những ai tự xoay xở một mình thường mất nhiều điểm nhất. Dandadan là câu chuyện về một nhóm bạn, không phải một người hùng.

<short pause> Đêm cuối cùng. Bạn được chọn một đồng đội để cùng đối mặt thử thách lớn nhất. Đây là ba ứng viên.

<short pause> Ứng viên một: một bà đồng lớn tuổi, nóng tính nhưng hiểu biết sâu về ma quỷ, có thể dựng kết giới và nói chuyện với yêu quái.

<short pause> Ứng viên hai: một bạn học có sức mạnh từ yêu quái, rất mạnh trong chiến đấu nhưng khó đoán và hay tự ái.

<short pause> Ứng viên ba: một cậu bạn mê khoa học viễn tưởng, không có sức mạnh gì nhưng rất giỏi máy móc và luôn có một kế hoạch điên rồ.

<short pause> Kết quả: chọn bà đồng thì trừ năm điểm, vì kinh nghiệm cứu bạn khỏi những cái bẫy mà bạn không biết. Chọn người có yêu quái thì trừ mười điểm, vì sức mạnh đi kèm rắc rối.

<short pause> Chọn người mê máy móc thì trừ mười lăm điểm, nhưng bạn có những khoảnh khắc buồn cười nhất đêm đó. Trong Dandadan, tiếng cười cũng là một cách để sống sót.
```

**ElevenLabs**

```text
Đêm thứ tư, bầu trời thị trấn đầy những ánh sáng lạ. Người ngoài hành tinh quay lại, và lần này họ không đến một mình.

[pause] Người ngoài hành tinh trong Dandadan có đủ loại hình dạng, từ những dáng người xám quen thuộc tới những sinh vật khổng lồ như quái vật trong phim.

[pause] Lựa chọn của bạn: A, trốn trong nhà và chờ sáng. B, chạy thật xa khỏi thị trấn. C, gọi bạn bè có năng lực đến giúp.

[pause] Nếu chọn A: trong thế giới này, cửa khóa không cản được thứ gì. Trừ ba mươi điểm. Nếu chọn B: bạn sống sót, nhưng thị trấn thì không. Trừ hai mươi điểm và mất luôn đồng minh.

[pause] Nếu chọn C: bạn không phải đối mặt một mình. Trong truyện, hầu như mọi trận đánh lớn đều được giải quyết nhờ cả nhóm. Chỉ trừ mười điểm.

[pause] Chi tiết thú vị: trận đánh trong truyện thường vừa kinh dị vừa buồn cười, như người ngoài hành tinh vừa đánh vừa cãi nhau, hay nhân vật chính hét những câu rất ngớ ngẩn giữa lúc nguy hiểm.

[pause] [chuckles] Kaku ghi chú: đây là đêm quyết định. Những ai tự xoay xở một mình thường mất nhiều điểm nhất. Dandadan là câu chuyện về một nhóm bạn, không phải một người hùng.

[pause] Đêm cuối cùng. Bạn được chọn một đồng đội để cùng đối mặt thử thách lớn nhất. Đây là ba ứng viên.

[pause] Ứng viên một: một bà đồng lớn tuổi, nóng tính nhưng hiểu biết sâu về ma quỷ, có thể dựng kết giới và nói chuyện với yêu quái.

[pause] Ứng viên hai: một bạn học có sức mạnh từ yêu quái, rất mạnh trong chiến đấu nhưng khó đoán và hay tự ái.

[pause] Ứng viên ba: một cậu bạn mê khoa học viễn tưởng, không có sức mạnh gì nhưng rất giỏi máy móc và luôn có một kế hoạch điên rồ.

[pause] Kết quả: chọn bà đồng thì trừ năm điểm, vì kinh nghiệm cứu bạn khỏi những cái bẫy mà bạn không biết. Chọn người có yêu quái thì trừ mười điểm, vì sức mạnh đi kèm rắc rối.

[pause] Chọn người mê máy móc thì trừ mười lăm điểm, nhưng bạn có những khoảnh khắc buồn cười nhất đêm đó. Trong Dandadan, tiếng cười cũng là một cách để sống sót.
```

### c06 · Đêm thưởng: Con mèo may mắn / Bảng điểm sống sót

Khoảng 116 giây · cảnh s49–s59 · 1512 ký tự

**Gemini**

```text
Khoan đã, còn một đêm thưởng mà Kaku giấu từ đầu. Sau khi mọi chuyện lắng xuống, bạn nhận được một món quà kỳ lạ: một bức tượng mèo may mắn.

<short pause> Trong truyện, sau trận đấu trong đường hầm, linh hồn bà lão yêu quái bị nhốt vào một bức tượng mèo may mắn, và từ đó sống luôn trong nhà của cô gái.

<short pause> Bà ta vẫn cáu kỉnh, vẫn đòi hỏi, nhưng dần dần trở thành một thành viên kỳ quặc của nhóm. Có nguồn còn nói bà ta mang lại may mắn cho người giữ mình.

<short pause> Lựa chọn của bạn: A, giữ bức tượng trong nhà. B, vứt nó ra bãi rác thật xa.

<short pause> Nếu chọn A: cộng mười điểm. Một yêu quái từng muốn hại bạn giờ trở thành đồng minh, dù hơi khó chịu. Nếu chọn B: trừ năm điểm, vì yêu quái thì không thích bị vứt đi chút nào.

<short pause> <laugh> Kaku ghi chú: đây là một điểm rất Dandadan. Kẻ thù hôm qua có thể là người nhà hôm nay, miễn là bạn đủ kiên nhẫn chịu đựng tính khí của họ.

<short pause> Giờ hãy cộng điểm. Bạn bắt đầu với một trăm, trừ đi điểm của năm đêm, rồi cộng hoặc trừ điểm của đêm thưởng. Bạn còn lại bao nhiêu?

<short pause> Từ năm mươi điểm trở lên: bạn là một thành viên thực thụ của nhóm, đủ bản lĩnh để sống sót tới cuối mùa và còn kể chuyện lại cho người khác.

<short pause> Từ hai mươi lăm đến bốn mươi chín điểm: bạn sống sót, nhưng với vài vết sẹo và một nỗi sợ đường hầm suốt đời.

<short pause> Dưới hai mươi lăm điểm: bạn đã trở thành một truyền thuyết đô thị mới của thị trấn. Chúc mừng, theo một cách nào đó.

<short pause> Kaku thử chơi và được năm mươi lăm điểm: lên ngọn đồi, tự luyện năng lực, tìm hiểu yêu quái, gọi bạn bè, chọn bà đồng, và giữ lại con mèo. Còn bạn được bao nhiêu? Viết vào phần bình luận nhé!
```

**ElevenLabs**

```text
Khoan đã, còn một đêm thưởng mà Kaku giấu từ đầu. Sau khi mọi chuyện lắng xuống, bạn nhận được một món quà kỳ lạ: một bức tượng mèo may mắn.

[pause] Trong truyện, sau trận đấu trong đường hầm, linh hồn bà lão yêu quái bị nhốt vào một bức tượng mèo may mắn, và từ đó sống luôn trong nhà của cô gái.

[pause] Bà ta vẫn cáu kỉnh, vẫn đòi hỏi, nhưng dần dần trở thành một thành viên kỳ quặc của nhóm. Có nguồn còn nói bà ta mang lại may mắn cho người giữ mình.

[pause] Lựa chọn của bạn: A, giữ bức tượng trong nhà. B, vứt nó ra bãi rác thật xa.

[pause] Nếu chọn A: cộng mười điểm. Một yêu quái từng muốn hại bạn giờ trở thành đồng minh, dù hơi khó chịu. Nếu chọn B: trừ năm điểm, vì yêu quái thì không thích bị vứt đi chút nào.

[pause] [chuckles] Kaku ghi chú: đây là một điểm rất Dandadan. Kẻ thù hôm qua có thể là người nhà hôm nay, miễn là bạn đủ kiên nhẫn chịu đựng tính khí của họ.

[pause] Giờ hãy cộng điểm. Bạn bắt đầu với một trăm, trừ đi điểm của năm đêm, rồi cộng hoặc trừ điểm của đêm thưởng. [curious] Bạn còn lại bao nhiêu?

[pause] Từ năm mươi điểm trở lên: bạn là một thành viên thực thụ của nhóm, đủ bản lĩnh để sống sót tới cuối mùa và còn kể chuyện lại cho người khác.

[pause] Từ hai mươi lăm đến bốn mươi chín điểm: bạn sống sót, nhưng với vài vết sẹo và một nỗi sợ đường hầm suốt đời.

[pause] Dưới hai mươi lăm điểm: bạn đã trở thành một truyền thuyết đô thị mới của thị trấn. Chúc mừng, theo một cách nào đó.

[pause] Kaku thử chơi và được năm mươi lăm điểm: lên ngọn đồi, tự luyện năng lực, tìm hiểu yêu quái, gọi bạn bè, chọn bà đồng, và giữ lại con mèo. Còn bạn được bao nhiêu? Viết vào phần bình luận nhé!
```

### c07 · Nếu bạn là người ngoài hành tinh / Truyền thuyết thật đằng sau

Khoảng 124 giây · cảnh s60–s70 · 1611 ký tự

**Gemini**

```text
Giờ hãy đảo ngược trò chơi. Nếu bạn là một người ngoài hành tinh vừa hạ cánh xuống thị trấn đó thì sao?

<short pause> Bạn đến với công nghệ vượt xa loài người, tàu bay, tia sáng, và những thiết bị có thể biến đổi cơ thể. Theo mọi logic, bạn phải thắng dễ dàng.

<short pause> Nhưng bạn không biết rằng hành tinh này còn có ma. Những thứ mà máy quét của bạn không đo được, và vũ khí của bạn không bắn trúng.

<short pause> Trong Dandadan, nhiều người ngoài hành tinh đánh giá thấp loài người, rồi bất ngờ trước năng lực siêu linh và yêu quái. Sự tự tin thái quá là điểm yếu lớn nhất của họ.

<short pause> <laugh> Kaku ghi chú: dù bạn là người hay người ngoài hành tinh, luật của thế giới này vẫn giống nhau: đừng coi thường những thứ bạn chưa hiểu.

<short pause> Điều làm Dandadan đặc biệt là rất nhiều yêu quái và người ngoài hành tinh trong truyện đến từ những câu chuyện có thật ngoài đời, dù là chuyện đồn.

<short pause> Bà lão chạy siêu tốc là một truyền thuyết đô thị nổi tiếng ở Nhật Bản. Người ta đồn về một bà lão chạy song song với xe hơi trên những con đường đèo vào ban đêm.

<short pause> Người phụ nữ nhào lộn váy đỏ cũng là một câu chuyện lan truyền trên các diễn đàn mạng Nhật Bản, với những lần kể lại khác nhau.

<short pause> Còn những người ngoài hành tinh xám, mắt to, đầu lớn, bắt cóc người để nghiên cứu là hình ảnh quen thuộc trong văn hóa UFO của phương Tây từ nhiều thập kỷ.

<short pause> Tên của nhóm người ngoài hành tinh đầu tiên trong truyện còn gợi nhớ một câu chuyện trên mạng về chương trình trao đổi bí mật giữa con người và người ngoài hành tinh, mà hầu hết mọi người coi là bịa đặt.

<short pause> Kaku thấy đây là cách xây thế giới rất thông minh: lấy những câu chuyện người ta kể trong đêm khuya, rồi hỏi, nếu tất cả đều là thật thì sao?
```

**ElevenLabs**

```text
Giờ hãy đảo ngược trò chơi. [curious] Nếu bạn là một người ngoài hành tinh vừa hạ cánh xuống thị trấn đó thì sao?

[pause] Bạn đến với công nghệ vượt xa loài người, tàu bay, tia sáng, và những thiết bị có thể biến đổi cơ thể. Theo mọi logic, bạn phải thắng dễ dàng.

[pause] Nhưng bạn không biết rằng hành tinh này còn có ma. Những thứ mà máy quét của bạn không đo được, và vũ khí của bạn không bắn trúng.

[pause] Trong Dandadan, nhiều người ngoài hành tinh đánh giá thấp loài người, rồi bất ngờ trước năng lực siêu linh và yêu quái. Sự tự tin thái quá là điểm yếu lớn nhất của họ.

[pause] [chuckles] Kaku ghi chú: dù bạn là người hay người ngoài hành tinh, luật của thế giới này vẫn giống nhau: đừng coi thường những thứ bạn chưa hiểu.

[pause] Điều làm Dandadan đặc biệt là rất nhiều yêu quái và người ngoài hành tinh trong truyện đến từ những câu chuyện có thật ngoài đời, dù là chuyện đồn.

[pause] Bà lão chạy siêu tốc là một truyền thuyết đô thị nổi tiếng ở Nhật Bản. Người ta đồn về một bà lão chạy song song với xe hơi trên những con đường đèo vào ban đêm.

[pause] Người phụ nữ nhào lộn váy đỏ cũng là một câu chuyện lan truyền trên các diễn đàn mạng Nhật Bản, với những lần kể lại khác nhau.

[pause] Còn những người ngoài hành tinh xám, mắt to, đầu lớn, bắt cóc người để nghiên cứu là hình ảnh quen thuộc trong văn hóa UFO của phương Tây từ nhiều thập kỷ.

[pause] Tên của nhóm người ngoài hành tinh đầu tiên trong truyện còn gợi nhớ một câu chuyện trên mạng về chương trình trao đổi bí mật giữa con người và người ngoài hành tinh, mà hầu hết mọi người coi là bịa đặt.

[pause] Kaku thấy đây là cách xây thế giới rất thông minh: lấy những câu chuyện người ta kể trong đêm khuya, rồi hỏi, nếu tất cả đều là thật thì sao?
```

### c08 · Góc nhìn của Kaku: vì sao ma và người ngoài hành tinh? / 5 mẹo sống sót của Kaku

Khoảng 108 giây · cảnh s71–s81 · 1399 ký tự

**Gemini**

```text
Vì sao tác giả đặt ma và người ngoài hành tinh vào cùng một câu chuyện? <laugh> Kaku có một giả thuyết.

<short pause> Cả hai đều là những thứ người lớn thường bảo là không có thật. <short pause> Nhưng hai nhân vật chính mỗi người tin một nửa, và coi thường nửa còn lại.

<short pause> Câu chuyện bắt đầu khi cả hai phải thừa nhận mình đã sai một nửa. Đó là cách hai con người khác biệt bắt đầu hiểu nhau.

<short pause> Nên dù có quái vật, có đĩa bay, có những cảnh hài vô lý, Dandadan về cơ bản là câu chuyện về việc mở lòng với những điều mình không tin.

<short pause> Kaku cũng thích cách truyện đối xử với những người bị coi là kỳ quặc. Cậu bạn mê người ngoài hành tinh bị cả lớp xa lánh, nhưng chính sự kỳ quặc đó cứu cả nhóm nhiều lần.

<short pause> Và có lẽ đó là lý do nó hợp với tuổi học trò đến vậy: ai cũng từng chắc chắn mình đúng, cho tới khi gặp một người khiến mình phải nghĩ lại.

<short pause> Nếu một ngày bạn thật sự tỉnh dậy trong thế giới đó, đây là năm mẹo sống sót Kaku rút ra từ trò chơi hôm nay.

<short pause> Một: đừng bao giờ đi vào đường hầm bỏ hoang vào ban đêm, dù bạn có tin ma hay không. Hai: nếu bị bắt cóc, hãy giữ bình tĩnh, vì hoảng loạn chưa bao giờ giúp ai trong truyện.

<short pause> Ba: trước khi đánh một yêu quái, hãy hỏi vì sao nó ở đó. Bốn: luôn có bạn bè ở bên, vì cả nhóm mạnh hơn bất kỳ ai đứng một mình.

<short pause> Năm: hãy tìm một bà đồng giỏi và đối xử tốt với bà ấy. Thật đấy.

<short pause> Và một mẹo tặng thêm: đừng bao giờ cá cược về những thứ bạn không tin. Cả câu chuyện Dandadan bắt đầu từ một lần cá cược như vậy.
```

**ElevenLabs**

```text
[curious] Vì sao tác giả đặt ma và người ngoài hành tinh vào cùng một câu chuyện? [chuckles] Kaku có một giả thuyết.

[pause] Cả hai đều là những thứ người lớn thường bảo là không có thật. [pause] Nhưng hai nhân vật chính mỗi người tin một nửa, và coi thường nửa còn lại.

[pause] Câu chuyện bắt đầu khi cả hai phải thừa nhận mình đã sai một nửa. Đó là cách hai con người khác biệt bắt đầu hiểu nhau.

[pause] Nên dù có quái vật, có đĩa bay, có những cảnh hài vô lý, Dandadan về cơ bản là câu chuyện về việc mở lòng với những điều mình không tin.

[pause] Kaku cũng thích cách truyện đối xử với những người bị coi là kỳ quặc. Cậu bạn mê người ngoài hành tinh bị cả lớp xa lánh, nhưng chính sự kỳ quặc đó cứu cả nhóm nhiều lần.

[pause] Và có lẽ đó là lý do nó hợp với tuổi học trò đến vậy: ai cũng từng chắc chắn mình đúng, cho tới khi gặp một người khiến mình phải nghĩ lại.

[pause] Nếu một ngày bạn thật sự tỉnh dậy trong thế giới đó, đây là năm mẹo sống sót Kaku rút ra từ trò chơi hôm nay.

[pause] Một: đừng bao giờ đi vào đường hầm bỏ hoang vào ban đêm, dù bạn có tin ma hay không. Hai: nếu bị bắt cóc, hãy giữ bình tĩnh, vì hoảng loạn chưa bao giờ giúp ai trong truyện.

[pause] Ba: trước khi đánh một yêu quái, hãy hỏi vì sao nó ở đó. Bốn: luôn có bạn bè ở bên, vì cả nhóm mạnh hơn bất kỳ ai đứng một mình.

[pause] Năm: hãy tìm một bà đồng giỏi và đối xử tốt với bà ấy. Thật đấy.

[pause] Và một mẹo tặng thêm: đừng bao giờ cá cược về những thứ bạn không tin. Cả câu chuyện Dandadan bắt đầu từ một lần cá cược như vậy.
```

### c09 · Kết

Khoảng 49 giây · cảnh s82–s86 · 641 ký tự

**Gemini**

```text
Tóm lại: trong thế giới Dandadan, cả ma lẫn người ngoài hành tinh đều có thật. Sức mạnh đến từ năng lực siêu linh hoặc từ yêu quái trong người, và mỗi con đường đều có cái giá.

<short pause> Và người sống sót lâu nhất không phải người mạnh nhất, mà là người chịu tìm hiểu và không đi một mình.

<short pause> Câu hỏi cho bạn: bạn tin vào ma, vào người ngoài hành tinh, hay cả hai? Và bạn còn lại bao nhiêu điểm sống sót?

<short pause> Video tới, Kaku đổi sang một thế giới có số liệu rõ ràng hơn nhiều: bảng chỉ số của Kaiju No. 8, nơi sức mạnh được đo bằng phần trăm.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. <laugh> Người dẫn trò Kaku xin rút lui, trước khi bà lão trong đường hầm tìm tới. Hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: trong thế giới Dandadan, cả ma lẫn người ngoài hành tinh đều có thật. Sức mạnh đến từ năng lực siêu linh hoặc từ yêu quái trong người, và mỗi con đường đều có cái giá.

[pause] Và người sống sót lâu nhất không phải người mạnh nhất, mà là người chịu tìm hiểu và không đi một mình.

[pause] [curious] Câu hỏi cho bạn: bạn tin vào ma, vào người ngoài hành tinh, hay cả hai? Và bạn còn lại bao nhiêu điểm sống sót?

[pause] Video tới, Kaku đổi sang một thế giới có số liệu rõ ràng hơn nhiều: bảng chỉ số của Kaiju No. 8, nơi sức mạnh được đo bằng phần trăm.

[pause] Đăng ký kênh để không bỏ lỡ nhé. [chuckles] Người dẫn trò Kaku xin rút lui, trước khi bà lão trong đường hầm tìm tới. Hẹn gặp lại!
```
