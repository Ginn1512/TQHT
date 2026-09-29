# Bộ prompt · Kaiju No. 8: Bảng chỉ số — tỉ lệ giải phóng sức mạnh và chỉ số quái thú

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 89 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (89 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Kaiju No. 8 tới hết anime mùa hai. Kaku sẽ tránh những diễn biến lớn ở phần cuối m…

```text
Wide 16:9 landscape cinematic frame. a ruined city street at dusk with a colossal monster silhouette on the horizon. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy nhìn thẻ chỉ số này. Tên: Hibino Kafka. Tuổi: ba mươi hai. Nghề nghiệp: dọn xác quái thú. Tỉ lệ giải phón…

```text
Wide 16:9 landscape cinematic frame. a video game style stat card with a tired man's silhouette, one bar completely empty and glowing red at 0%. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Một thẻ chỉ số tệ đến mức buồn cười. Nhưng lật mặt sau ra thì có một dòng khác: chỉ số sức mạnh quái thú, chí…

```text
Wide 16:9 landscape cinematic frame. the stat card flipping over to reveal a monstrous silhouette and a huge glowing number 9.8. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Làm sao một người vừa là con số không, vừa là một trong những con quái thú nguy hiểm nhất từng được đo? Câu t…

```text
Wide 16:9 landscape cinematic frame. a split screen of a tired worker and a towering monster sharing the same shadow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ biến thành màn hình chỉ số. Chúng ta sẽ đọc từng chỉ số, xếp hạng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping a holographic stat screen that pops out of its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và cuối video, bạn sẽ tự làm thẻ chỉ số của chính mình. Chuẩn bị giấy bút nhé!

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a blank stat card with a pencil. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Thế giới quái thú

Lời: Kaiju No. 8 là manga của Matsumoto Naoya, đăng trên Shonen Jump Plus từ năm 2020. Bản anime ra mắt năm 2024 v…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes with a monster claw mark on the cover, beside a small screen. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Trong thế giới này, Nhật Bản là một trong những nơi có quái thú xuất hiện nhiều nhất thế giới. Chúng trồi lên…

```text
Wide 16:9 landscape cinematic frame. a coastal Japanese city with emergency sirens, a giant creature rising from the bay. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Để chống lại chúng có Lực lượng Phòng vệ, những chiến binh mặc bộ giáp đặc biệt và dùng vũ khí chế tạo từ chí…

```text
Wide 16:9 landscape cinematic frame. soldiers in sleek high-tech combat suits standing in formation before a monster. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Sau mỗi trận đánh, còn phải có người dọn dẹp xác quái thú khổng lồ. Đó là công việc của nhân vật chính, một n…

```text
Wide 16:9 landscape cinematic frame. workers in hazmat suits cutting apart a massive monster carcass on a city street. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Kafka từng hứa với người bạn thời thơ ấu rằng cả hai sẽ cùng vào Lực lượng Phòng vệ. Cô ấy giờ đã là đội trưở…

```text
Wide 16:9 landscape cinematic frame. a man in work overalls looking up at a distant woman in a captain's uniform on a stage. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Cho tới một ngày, anh bị một con quái thú nhỏ chui vào miệng, và biến thành một quái thú hình người. Lực lượn…

```text
Wide 16:9 landscape cinematic frame. a small winged creature diving toward a startled man, then a humanoid monster silhouette emerging. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Chỉ số 1: Sức mạnh quái thú

Lời: Chỉ số đầu tiên đo độ nguy hiểm của một con quái thú. Truyện gọi là chỉ số sức mạnh quái thú, và dùng nó để q…

```text
Wide 16:9 landscape cinematic frame. a command center screen with a monster silhouette and a numeric gauge climbing. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Con số càng cao, quái thú càng nguy hiểm. Những con có chỉ số từ tám trở lên được gọi là quái thú lớn, đủ sức…

```text
Wide 16:9 landscape cinematic frame. a gauge with a red zone starting at 8.0, a massive creature casting a shadow over a district. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Chỉ số được đo bằng máy móc khi quái thú xuất hiện, giống như đo cường độ của một trận động đất. Nhờ vậy, tru…

```text
Wide 16:9 landscape cinematic frame. a seismograph-like readout spiking as a monster emerges from the ground. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Khi Kafka biến hình lần đầu, máy đo ghi nhận chỉ số chín phẩy tám, thuộc hàng cao nhất từng thấy. Đó là lý do…

```text
Wide 16:9 landscape cinematic frame. alarms flashing red in a command center as the gauge hits 9.8. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nhưng chỉ số này có một điểm yếu: nó chỉ đo lượng sức mạnh, không đo ý định. Một quái thú không muốn hại ai c…

```text
Wide 16:9 landscape cinematic frame. a monstrous silhouette gently holding a child away from falling debris, alarms still blaring. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Và có một điều đáng sợ hơn: chỉ số có thể thay đổi. Một quái thú có thể mạnh lên sau khi hấp thụ năng lượng h…

```text
Wide 16:9 landscape cinematic frame. a gauge needle suddenly jumping higher as a creature mutates mid-battle, operators gasping. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chỉ số này giống cân nặng. Nó cho biết con quái thú to cỡ nào, chứ không cho biết nó định làm g…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing on a scale that shows a huge number, looking confused. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Chỉ số 2: Tỉ lệ giải phóng sức mạnh

Lời: Chỉ số thứ hai dành cho con người. Bộ giáp chiến đấu có thể khuếch đại sức mạnh của người mặc, nhưng mỗi ngườ…

```text
Wide 16:9 landscape cinematic frame. a combat suit on a rack with glowing power lines running through it, a percentage display on the chest. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Phần đó được đo bằng phần trăm, từ không tới tối đa một trăm. Nó phụ thuộc vào thể lực, tinh thần và mức độ t…

```text
Wide 16:9 landscape cinematic frame. a gauge from 0 to 100 percent with icons for muscle, mind and a puzzle piece. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Người mới vào thường ở mức rất thấp. Những đội trưởng giỏi nhất thì gần chạm mốc tối đa: một đội trưởng ở mức…

```text
Wide 16:9 landscape cinematic frame. a leaderboard showing low percentages for recruits and 96% and 98% glowing at the top. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Còn Kafka ở dạng người? Không phần trăm trong kỳ thi tuyển. Sau khi cố gắng hết sức, anh lên được một phần tr…

```text
Wide 16:9 landscape cinematic frame. a stat screen showing 0% then painfully ticking up to 1%, a man sweating beside it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Chỉ số này rất giống thanh sức mạnh trong game: tăng từ từ qua luyện tập, và một vài phần trăm cũng tạo khác…

```text
Wide 16:9 landscape cinematic frame. a training montage of a recruit's gauge rising slowly, one percent at a time. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Muốn tăng tỉ lệ, không có lối tắt: tập thể lực, rèn tinh thần, và mặc giáp chiến đấu thật nhiều lần để cơ thể…

```text
Wide 16:9 landscape cinematic frame. a recruit training alone at night in a gym, the suit's lines glowing brighter with each rep. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một trăm phần trăm là giới hạn của bộ giáp, không phải giới hạn của con người. Nên muốn mạnh hơ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot squeezing into a tiny combat suit that shows 100% and starts beeping. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Chỉ số 3: Quái thú chính và quái thú phụ

Lời: Quái thú không phải lúc nào cũng đi một mình. Truyện chia chúng thành quái thú chính, là con lớn nhất, và quá…

```text
Wide 16:9 landscape cinematic frame. a giant creature surrounded by a swarm of smaller creatures pouring into a city. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Trong một trận đánh, lực lượng thường chia hai: những người mạnh nhất lo con chính, những người còn lại dọn d…

```text
Wide 16:9 landscape cinematic frame. a tactical map with one big red marker and many small red dots, blue squads assigned to each. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Với tân binh, quái thú phụ là bài kiểm tra thật sự đầu tiên. Không lớn, nhưng rất đông, và chỉ một sai lầm là…

```text
Wide 16:9 landscape cinematic frame. a group of recruits back to back in an alley surrounded by small snarling creatures. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Điểm thú vị: người tiêu diệt được nhiều quái thú phụ nhất không nhất thiết là người có tỉ lệ giải phóng cao n…

```text
Wide 16:9 landscape cinematic frame. a scoreboard of kills where a mid-level recruit tops the chart thanks to teamwork icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: giống game chiến thuật, dọn quái nhỏ tốt thì trận đánh boss mới dễ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sweeping tiny monster figurines off a game board with a small broom. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Chỉ số 4: Số hiệu quái thú

Lời: Có những quái thú nguy hiểm tới mức được đặt số hiệu riêng, như một hồ sơ truy nã. Kafka là số tám, và trước…

```text
Wide 16:9 landscape cinematic frame. a wall of classified files numbered 1 through 9, one file stamped with a large 8. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Được đánh số nghĩa là quái thú đó cực kỳ hiếm và cực kỳ mạnh. Cả lực lượng phải ghi nhớ đặc điểm của từng con.

```text
Wide 16:9 landscape cinematic frame. officers studying glowing monster profiles on a large screen in a briefing room. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trong truyện, có một quái thú mang số hiệu khiến mọi người lo sợ nhất: nó thông minh, biết nói, biết lập kế h…

```text
Wide 16:9 landscape cinematic frame. a shadowy humanoid monster with glowing eyes standing calmly on a rooftop, city lights below. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Sự xuất hiện của quái thú thông minh khiến chỉ số sức mạnh không còn đủ. Một con quái thú biết suy nghĩ nguy…

```text
Wide 16:9 landscape cinematic frame. a chess board where a monster piece moves by itself against surprised human players. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là lúc truyện chuyển từ đánh quái vật sang một cuộc đấu trí. Những con số bắt đầu không còn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a chessboard, sweating. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Chỉ số 5: Vũ khí số hiệu

Lời: Điều gì xảy ra với quái thú mang số hiệu sau khi bị tiêu diệt? Lực lượng Phòng vệ biến cơ thể chúng thành vũ…

```text
Wide 16:9 landscape cinematic frame. a high-tech lab where scientists examine a glowing monster core inside a containment tube. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Những vũ khí này được gọi theo số hiệu của quái thú gốc, và mang một phần năng lực của nó. Ví dụ, một vũ khí…

```text
Wide 16:9 landscape cinematic frame. an officer wearing a sleek visor that shows faint predicted movement lines of an enemy. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Điểm mạnh: chúng đưa sức mạnh của con người vượt xa giới hạn một trăm phần trăm của bộ giáp thường.

```text
Wide 16:9 landscape cinematic frame. a gauge breaking past 100% with a surge of monstrous energy. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điểm yếu: chỉ những người cực kỳ tương thích mới dùng được. Dùng sai người, vũ khí có thể phản chủ, gây tổn t…

```text
Wide 16:9 landscape cinematic frame. a weapon glowing dangerously as it cracks the armor of the person holding it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và có một câu hỏi rùng rợn: nếu vũ khí làm từ quái thú, thì liệu một phần quái thú có còn sống trong đó không…

```text
Wide 16:9 landscape cinematic frame. a dark weapon in a case with a faint eye shape glowing within its surface. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Kỳ thi tuyển: lần đầu bị đo

Lời: Trước khi xếp hạng, hãy xem những con số này được đo lần đầu ở đâu: kỳ thi tuyển của Lực lượng Phòng vệ.

```text
Wide 16:9 landscape cinematic frame. a large exam hall with rows of candidates in training suits and scanners overhead. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Kỳ thi gồm các bài kiểm tra thể lực, rồi một bài thi thực tế: thí sinh mặc giáp và đối đầu với quái thú thật…

```text
Wide 16:9 landscape cinematic frame. candidates in suits entering a fenced ruined district where small creatures lurk. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Ở bài thi đó, có tân binh thể hiện tỉ lệ giải phóng rất cao ngay lần đầu, được mọi người chú ý. Còn Kafka thì…

```text
Wide 16:9 landscape cinematic frame. a young prodigy blasting a creature apart while a man in the background struggles to lift his weapon. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhưng thay vì đánh, anh dùng kinh nghiệm dọn xác để chỉ cho các thí sinh khác chỗ yếu của quái thú. Một đội p…

```text
Wide 16:9 landscape cinematic frame. a man pointing out a weak spot on a creature to a group of surprised candidates, an officer watching from afar. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhờ vậy, anh được nhận vào với tư cách ứng viên dự bị, một cơ hội cuối cùng. Con số nói không, nhưng có người…

```text
Wide 16:9 landscape cinematic frame. a man receiving a provisional badge, his hand trembling, a small smile on his face. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bài học tuyển dụng hay nhất trong anime. Nhìn hồ sơ thì thấy con số, nhìn người thì thấy tiềm n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny glasses, reviewing a resume with a magnifying glass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Bảng xếp hạng tỉ lệ giải phóng

Lời: Giờ ghép các con số lại thành một bảng xếp hạng. Kaku không ghi tên từng người, chỉ ghi vai trò, để bạn thấy…

```text
Wide 16:9 landscape cinematic frame. a tiered leaderboard with silhouettes instead of names, percentage bars glowing. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Tầng thấp nhất: Kafka ở dạng người, không phần trăm rồi một phần trăm. Kỷ lục thấp nhất lịch sử kỳ thi, theo…

```text
Wide 16:9 landscape cinematic frame. the bottom rung of a ladder with a tiny 1% flag and a man hanging on by one hand. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Tầng tân binh: những người vừa đỗ kỳ thi, thường ở mức vài chục phần trăm. Có tân binh thiên tài còn vượt xa…

```text
Wide 16:9 landscape cinematic frame. a group of recruits with bars in the tens of percent, one standing out with a much longer bar. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Tầng đội phó: những chiến binh kỳ cựu, tỉ lệ cao, chỉ huy một đội. Tầng đội trưởng: gần chạm trần, chín mươi…

```text
Wide 16:9 landscape cinematic frame. two higher tiers with veteran silhouettes, bars reaching near the top. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Tầng đỉnh: người đứng đầu lực lượng, chín mươi tám phần trăm, cùng những người dùng vũ khí số hiệu vượt ra ng…

```text
Wide 16:9 landscape cinematic frame. a single silhouette at the peak with a bar at 98%, a glowing weapon beside them breaking the scale. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn bảng này, Kafka có vẻ vô vọng. Nhưng hãy nhớ, thẻ của anh có hai mặt.

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping a card over dramatically. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Kafka: một người, hai thẻ chỉ số

Lời: Ở dạng người, Kafka là người yếu nhất lực lượng. Ở dạng quái thú số tám, anh có thể đấm tan một quái thú lớn…

```text
Wide 16:9 landscape cinematic frame. a split image: a man struggling with a heavy suit, and a humanoid monster shattering a giant creature with one punch. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Vấn đề là anh không thể biến hình công khai. Nếu bị phát hiện, anh sẽ bị coi là quái thú và bị tiêu diệt. Nên…

```text
Wide 16:9 landscape cinematic frame. a man hiding his monstrous shadow behind him as soldiers pass by. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Ban đầu anh cũng chưa kiểm soát được sức mạnh. Có lúc biến hình không theo ý muốn, có lúc suýt mất kiểm soát…

```text
Wide 16:9 landscape cinematic frame. a man clutching his arm as monstrous patterns crawl across his skin. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Đây là cái giá của dạng quái thú: mạnh tuyệt đối, nhưng đổi lại là bí mật, sự nghi ngờ, và nỗi sợ trở thành c…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a man's face on one side and a monster's on the other. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu thẻ chỉ số là game, Kafka giống người chơi có một tài khoản phụ siêu mạnh nhưng bị cấm đăng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a login screen marked BANNED on a glowing monitor. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Giới hạn của những con số

Lời: Giờ tới phần Kaku thích nhất: những con số bỏ sót điều gì?

```text
Wide 16:9 landscape cinematic frame. a stat card with several blank lines labeled with question marks. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Thứ nhất: kinh nghiệm. Nhiều năm dọn xác quái thú giúp Kafka hiểu cấu tạo cơ thể quái thú hơn bất kỳ ai, biết…

```text
Wide 16:9 landscape cinematic frame. a worker's hand pointing to the glowing core inside a monster anatomy diagram. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Kiến thức đó không hiện trên thanh phần trăm nào, nhưng nhiều lần giúp cả đội sống sót khi con số không đủ.

```text
Wide 16:9 landscape cinematic frame. a squad following a man in overalls who points toward a weak spot on a giant creature. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Thứ hai: kỹ năng. Có những chiến binh không có tỉ lệ cao nhất, nhưng kiếm thuật hay chiến thuật của họ khiến…

```text
Wide 16:9 landscape cinematic frame. a lean swordsman slicing through a swarm of small monsters with precise movements. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Thứ ba: tinh thần. Ở tuổi ba mươi hai, sau bao lần bị từ chối, Kafka vẫn thi lại. Sự kiên trì đó không có máy…

```text
Wide 16:9 landscape cinematic frame. a man standing alone at an exam hall entrance, rain falling, determined expression. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và thứ tư: đồng đội. Một con số chỉ đo một người. Nhưng trong truyện, trận thắng quan trọng nào cũng là thắng…

```text
Wide 16:9 landscape cinematic frame. a squad huddled together, each with a different bar, forming one combined glow. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · So với cấp bậc thợ săn

Lời: Nếu bạn đã xem video số bảy của kênh về cấp bậc thợ săn trong Solo Leveling, bạn sẽ thấy hai hệ thống này rất…

```text
Wide 16:9 landscape cinematic frame. two stat systems side by side: letter ranks on one side, percentage gauges on the other. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Hệ thống thợ săn chia theo hạng chữ cái, cố định sau khi thức tỉnh. Hệ thống ở đây là những con số liên tục,…

```text
Wide 16:9 landscape cinematic frame. letter badges E to S frozen in ice beside a gauge that keeps moving. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Một bên đo con người như món đồ được đóng nhãn một lần. Một bên đo như vận động viên, hôm nay có thể giỏi hơn…

```text
Wide 16:9 landscape cinematic frame. a factory label stamp on one side, a runner's stopwatch on the other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và cả hai bộ đều có chung một nhân vật chính bị đánh giá thấp nhất, rồi vượt qua mọi thang đo. Có lẽ khán giả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two broken measuring tapes, grinning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Trò chơi: đoán kết quả trận đánh · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi tới góc nhìn, chơi một trò nhanh. Kaku đưa ra ba tình huống với số liệu tự đặt, bạn đoán xem đội nà…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shuffling three scenario cards on a table. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Tình huống một: năm tân binh, mỗi người ba mươi phần trăm, đối đầu một quái thú phụ nhỏ. Đáp án của Kaku: thắ…

```text
Wide 16:9 landscape cinematic frame. five recruits surrounding a small creature in a coordinated formation. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Tình huống hai: một đội trưởng chín mươi sáu phần trăm, một mình, đối đầu quái thú lớn chỉ số tám phẩy năm. Đ…

```text
Wide 16:9 landscape cinematic frame. a lone captain facing a massive creature while small monsters swarm behind her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Tình huống ba: một người một phần trăm, có kinh nghiệm dọn xác, cùng một đội tân binh, đối đầu quái thú lạ. Đ…

```text
Wide 16:9 landscape cinematic frame. a man in overalls pointing at a creature's weak spot while recruits aim their weapons. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Bạn có đoán giống Kaku không? Nếu không, hãy giải thích lý do của bạn trong phần bình luận, Kaku rất muốn đọc.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a scorecard with question marks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Góc nhìn của Kaku: tuổi ba mươi hai · **Kaku** (đính kèm ảnh mẫu)

Lời: Có một con số trên thẻ chỉ số Kaku muốn nói thêm: tuổi của Kafka, ba mươi hai.

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling the number 32 on a stat card with a red pen. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Phần lớn nhân vật chính trong truyện tranh thiếu niên là học sinh. Kafka là một người đàn ông trung niên, từn…

```text
Wide 16:9 landscape cinematic frame. a middle-aged man eating a convenience store meal alone on a bench after work. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nhưng chính vì vậy, câu chuyện của anh chạm tới nhiều người lớn: những ai cảm thấy mình đã lỡ chuyến tàu của…

```text
Wide 16:9 landscape cinematic frame. a train platform at night, a man watching a train leave, then turning back to walk forward. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Truyện nói rằng chưa bao giờ là quá muộn, và rằng những năm tháng tưởng như lãng phí, như dọn xác quái thú, c…

```text
Wide 16:9 landscape cinematic frame. old work gloves placed beside a new combat helmet on a locker room bench. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Kaku nghĩ đó là chỉ số quan trọng nhất trên thẻ: không phải phần trăm, mà là việc anh vẫn chưa bỏ cuộc.

```text
Wide 16:9 landscape cinematic frame. a stat card with a new line added by hand: NEVER GAVE UP, glowing warmly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Thẻ chỉ số của bạn

Lời: Giờ tới lượt bạn. Lấy giấy bút ra, Kaku sẽ giúp bạn làm thẻ chỉ số. Đây là trò chơi vui, không có đúng sai.

```text
Wide 16:9 landscape cinematic frame. a blank stat card template with five empty bars and a pencil. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Dòng một, sức bền: bạn chạy bộ được bao lâu mà không dừng? Dưới năm phút ghi hai mươi phần trăm, trên ba mươi…

```text
Wide 16:9 landscape cinematic frame. a stat bar labeled stamina filling up beside a small running shoe icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Dòng hai, bình tĩnh: khi gặp chuyện bất ngờ, bạn hoảng loạn hay suy nghĩ trước? Dòng ba, kinh nghiệm: bạn giỏ…

```text
Wide 16:9 landscape cinematic frame. two stat bars labeled calm and experience, small icons of a heartbeat and a toolbox. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Dòng bốn, đồng đội: khi làm việc nhóm, bạn là người dẫn đầu, người hỗ trợ, hay người nghĩ ra kế hoạch? Mỗi va…

```text
Wide 16:9 landscape cinematic frame. three small role icons: a flag, a shield and a lightbulb. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Dòng cuối, không có thang đo: điều gì khiến bạn chưa bỏ cuộc? Viết nó vào thẻ. Đó là dòng quan trọng nhất.

```text
Wide 16:9 landscape cinematic frame. a stat card with a final unmeasured line glowing softly, written by hand. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy chia sẻ dòng cuối của bạn trong phần bình luận. Kaku đọc hết đấy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot reading a long scroll of comments with a warm smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Kết

Lời: Tóm lại: quái thú được đo bằng chỉ số sức mạnh, từ tám trở lên là quái thú lớn. Con người được đo bằng tỉ lệ…

```text
Wide 16:9 landscape cinematic frame. a summary screen showing a monster gauge and a human percentage gauge side by side. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Quái thú mạnh nhất được đánh số, và cơ thể chúng thành vũ khí số hiệu. Còn Kafka mang cả hai thẻ: một phần tr…

```text
Wide 16:9 landscape cinematic frame. two cards overlapping, 1% and 9.8, glowing in contrasting colors. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có thể chọn, bạn muốn làm chiến binh mặc giáp với tỉ lệ cao, hay mang trong mình sức mạn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a helmet in one wing and a monster claw toy in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Video tới, Kaku sẽ leo từng nấc thang tiến hóa của kiếm Zanpakuto trong Bleach, từ Shikai đến Bankai, đúng lú…

```text
Wide 16:9 landscape cinematic frame. a sword silhouette glowing brighter on each step of a staircase. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku tắt màn hình chỉ số đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a holographic stat screen and waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thế giới quái thú

Khoảng 125 giây · cảnh s01–s12 · 1622 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Kaiju No. 8 tới hết anime mùa hai. Kaku sẽ tránh những diễn biến lớn ở phần cuối manga.

<short pause> Hãy nhìn thẻ chỉ số này. Tên: Hibino Kafka. Tuổi: ba mươi hai. Nghề nghiệp: dọn xác quái thú. Tỉ lệ giải phóng sức mạnh: không phần trăm.

<short pause> Một thẻ chỉ số tệ đến mức buồn cười. <short pause> Nhưng lật mặt sau ra thì có một dòng khác: chỉ số sức mạnh quái thú, chín phẩy tám.

<short pause> Làm sao một người vừa là con số không, vừa là một trong những con quái thú nguy hiểm nhất từng được đo? Câu trả lời nằm trong cách thế giới này đo sức mạnh.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ biến thành màn hình chỉ số. Chúng ta sẽ đọc từng chỉ số, xếp hạng, rồi hỏi xem những con số này bỏ sót điều gì.

<short pause> Và cuối video, bạn sẽ tự làm thẻ chỉ số của chính mình. Chuẩn bị giấy bút nhé!

<short pause> Kaiju No. 8 là manga của Matsumoto Naoya, đăng trên Shonen Jump Plus từ năm 2020. Bản anime ra mắt năm 2024 và có mùa hai năm 2025.

<short pause> Trong thế giới này, Nhật Bản là một trong những nơi có quái thú xuất hiện nhiều nhất thế giới. Chúng trồi lên từ lòng đất, từ biển, và tấn công thành phố như thiên tai.

<short pause> Để chống lại chúng có Lực lượng Phòng vệ, những chiến binh mặc bộ giáp đặc biệt và dùng vũ khí chế tạo từ chính cơ thể quái thú.

<short pause> Sau mỗi trận đánh, còn phải có người dọn dẹp xác quái thú khổng lồ. Đó là công việc của nhân vật chính, một nghề bẩn, nguy hiểm và không ai để ý.

<short pause> Kafka từng hứa với người bạn thời thơ ấu rằng cả hai sẽ cùng vào Lực lượng Phòng vệ. Cô ấy giờ đã là đội trưởng. Còn anh vẫn đứng dọn dẹp phía sau.

<short pause> Cho tới một ngày, anh bị một con quái thú nhỏ chui vào miệng, và biến thành một quái thú hình người. Lực lượng Phòng vệ đặt cho nó số hiệu tám.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Kaiju No. 8 tới hết anime mùa hai. Kaku sẽ tránh những diễn biến lớn ở phần cuối manga.

[pause] Hãy nhìn thẻ chỉ số này. Tên: Hibino Kafka. Tuổi: ba mươi hai. Nghề nghiệp: dọn xác quái thú. Tỉ lệ giải phóng sức mạnh: không phần trăm.

[pause] Một thẻ chỉ số tệ đến mức buồn cười. [pause] Nhưng lật mặt sau ra thì có một dòng khác: chỉ số sức mạnh quái thú, chín phẩy tám.

[pause] [curious] Làm sao một người vừa là con số không, vừa là một trong những con quái thú nguy hiểm nhất từng được đo? Câu trả lời nằm trong cách thế giới này đo sức mạnh.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ biến thành màn hình chỉ số. Chúng ta sẽ đọc từng chỉ số, xếp hạng, rồi hỏi xem những con số này bỏ sót điều gì.

[pause] Và cuối video, bạn sẽ tự làm thẻ chỉ số của chính mình. Chuẩn bị giấy bút nhé!

[pause] Kaiju No. 8 là manga của Matsumoto Naoya, đăng trên Shonen Jump Plus từ năm 2020. Bản anime ra mắt năm 2024 và có mùa hai năm 2025.

[pause] Trong thế giới này, Nhật Bản là một trong những nơi có quái thú xuất hiện nhiều nhất thế giới. Chúng trồi lên từ lòng đất, từ biển, và tấn công thành phố như thiên tai.

[pause] Để chống lại chúng có Lực lượng Phòng vệ, những chiến binh mặc bộ giáp đặc biệt và dùng vũ khí chế tạo từ chính cơ thể quái thú.

[pause] Sau mỗi trận đánh, còn phải có người dọn dẹp xác quái thú khổng lồ. Đó là công việc của nhân vật chính, một nghề bẩn, nguy hiểm và không ai để ý.

[pause] Kafka từng hứa với người bạn thời thơ ấu rằng cả hai sẽ cùng vào Lực lượng Phòng vệ. Cô ấy giờ đã là đội trưởng. Còn anh vẫn đứng dọn dẹp phía sau.

[pause] Cho tới một ngày, anh bị một con quái thú nhỏ chui vào miệng, và biến thành một quái thú hình người. Lực lượng Phòng vệ đặt cho nó số hiệu tám.
```

### c02 · Chỉ số 1: Sức mạnh quái thú

Khoảng 79 giây · cảnh s13–s19 · 1022 ký tự

**Gemini**

```text
Chỉ số đầu tiên đo độ nguy hiểm của một con quái thú. Truyện gọi là chỉ số sức mạnh quái thú, và dùng nó để quyết định phải điều bao nhiêu lực lượng.

<short pause> Con số càng cao, quái thú càng nguy hiểm. Những con có chỉ số từ tám trở lên được gọi là quái thú lớn, đủ sức phá hủy cả một khu vực.

<short pause> Chỉ số được đo bằng máy móc khi quái thú xuất hiện, giống như đo cường độ của một trận động đất. Nhờ vậy, trung tâm chỉ huy biết ngay mức độ nguy hiểm.

<short pause> Khi Kafka biến hình lần đầu, máy đo ghi nhận chỉ số chín phẩy tám, thuộc hàng cao nhất từng thấy. Đó là lý do anh được đánh số, và bị truy lùng.

<short pause> Nhưng chỉ số này có một điểm yếu: nó chỉ đo lượng sức mạnh, không đo ý định. Một quái thú không muốn hại ai cũng có thể bị xếp là cực kỳ nguy hiểm.

<short pause> Và có một điều đáng sợ hơn: chỉ số có thể thay đổi. Một quái thú có thể mạnh lên sau khi hấp thụ năng lượng hay tiến hóa, nên con số đo lúc đầu không phải lúc nào cũng đúng tới cuối trận.

<short pause> <laugh> Kaku ghi chú: chỉ số này giống cân nặng. Nó cho biết con quái thú to cỡ nào, chứ không cho biết nó định làm gì.
```

**ElevenLabs**

```text
Chỉ số đầu tiên đo độ nguy hiểm của một con quái thú. Truyện gọi là chỉ số sức mạnh quái thú, và dùng nó để quyết định phải điều bao nhiêu lực lượng.

[pause] Con số càng cao, quái thú càng nguy hiểm. Những con có chỉ số từ tám trở lên được gọi là quái thú lớn, đủ sức phá hủy cả một khu vực.

[pause] Chỉ số được đo bằng máy móc khi quái thú xuất hiện, giống như đo cường độ của một trận động đất. Nhờ vậy, trung tâm chỉ huy biết ngay mức độ nguy hiểm.

[pause] Khi Kafka biến hình lần đầu, máy đo ghi nhận chỉ số chín phẩy tám, thuộc hàng cao nhất từng thấy. Đó là lý do anh được đánh số, và bị truy lùng.

[pause] Nhưng chỉ số này có một điểm yếu: nó chỉ đo lượng sức mạnh, không đo ý định. Một quái thú không muốn hại ai cũng có thể bị xếp là cực kỳ nguy hiểm.

[pause] Và có một điều đáng sợ hơn: chỉ số có thể thay đổi. Một quái thú có thể mạnh lên sau khi hấp thụ năng lượng hay tiến hóa, nên con số đo lúc đầu không phải lúc nào cũng đúng tới cuối trận.

[pause] [chuckles] Kaku ghi chú: chỉ số này giống cân nặng. Nó cho biết con quái thú to cỡ nào, chứ không cho biết nó định làm gì.
```

### c03 · Chỉ số 2: Tỉ lệ giải phóng sức mạnh / Chỉ số 3: Quái thú chính và quái thú phụ

Khoảng 129 giây · cảnh s20–s31 · 1680 ký tự

**Gemini**

```text
Chỉ số thứ hai dành cho con người. Bộ giáp chiến đấu có thể khuếch đại sức mạnh của người mặc, nhưng mỗi người chỉ khai thác được một phần.

<short pause> Phần đó được đo bằng phần trăm, từ không tới tối đa một trăm. Nó phụ thuộc vào thể lực, tinh thần và mức độ tương thích giữa người đó với bộ giáp.

<short pause> Người mới vào thường ở mức rất thấp. Những đội trưởng giỏi nhất thì gần chạm mốc tối đa: một đội trưởng ở mức chín mươi sáu phần trăm, người đứng đầu lực lượng ở mức chín mươi tám.

<short pause> Còn Kafka ở dạng người? Không phần trăm trong kỳ thi tuyển. Sau khi cố gắng hết sức, anh lên được một phần trăm. Đúng vậy, một.

<short pause> Chỉ số này rất giống thanh sức mạnh trong game: tăng từ từ qua luyện tập, và một vài phần trăm cũng tạo khác biệt rất lớn trong trận đánh.

<short pause> Muốn tăng tỉ lệ, không có lối tắt: tập thể lực, rèn tinh thần, và mặc giáp chiến đấu thật nhiều lần để cơ thể quen dần với dòng sức mạnh trong bộ giáp.

<short pause> <laugh> Kaku ghi chú: một trăm phần trăm là giới hạn của bộ giáp, không phải giới hạn của con người. Nên muốn mạnh hơn nữa thì phải có thứ khác ngoài bộ giáp.

<short pause> Quái thú không phải lúc nào cũng đi một mình. Truyện chia chúng thành quái thú chính, là con lớn nhất, và quái thú phụ, là những con nhỏ sinh ra hoặc đi theo nó.

<short pause> Trong một trận đánh, lực lượng thường chia hai: những người mạnh nhất lo con chính, những người còn lại dọn dẹp bầy quái thú phụ.

<short pause> Với tân binh, quái thú phụ là bài kiểm tra thật sự đầu tiên. Không lớn, nhưng rất đông, và chỉ một sai lầm là đủ trả giá.

<short pause> Điểm thú vị: người tiêu diệt được nhiều quái thú phụ nhất không nhất thiết là người có tỉ lệ giải phóng cao nhất, mà là người phối hợp tốt nhất với đồng đội.

<short pause> Kaku ghi chú: giống game chiến thuật, dọn quái nhỏ tốt thì trận đánh boss mới dễ.
```

**ElevenLabs**

```text
Chỉ số thứ hai dành cho con người. Bộ giáp chiến đấu có thể khuếch đại sức mạnh của người mặc, nhưng mỗi người chỉ khai thác được một phần.

[pause] Phần đó được đo bằng phần trăm, từ không tới tối đa một trăm. Nó phụ thuộc vào thể lực, tinh thần và mức độ tương thích giữa người đó với bộ giáp.

[pause] Người mới vào thường ở mức rất thấp. Những đội trưởng giỏi nhất thì gần chạm mốc tối đa: một đội trưởng ở mức chín mươi sáu phần trăm, người đứng đầu lực lượng ở mức chín mươi tám.

[pause] [curious] Còn Kafka ở dạng người? Không phần trăm trong kỳ thi tuyển. Sau khi cố gắng hết sức, anh lên được một phần trăm. Đúng vậy, một.

[pause] Chỉ số này rất giống thanh sức mạnh trong game: tăng từ từ qua luyện tập, và một vài phần trăm cũng tạo khác biệt rất lớn trong trận đánh.

[pause] Muốn tăng tỉ lệ, không có lối tắt: tập thể lực, rèn tinh thần, và mặc giáp chiến đấu thật nhiều lần để cơ thể quen dần với dòng sức mạnh trong bộ giáp.

[pause] [chuckles] Kaku ghi chú: một trăm phần trăm là giới hạn của bộ giáp, không phải giới hạn của con người. Nên muốn mạnh hơn nữa thì phải có thứ khác ngoài bộ giáp.

[pause] Quái thú không phải lúc nào cũng đi một mình. Truyện chia chúng thành quái thú chính, là con lớn nhất, và quái thú phụ, là những con nhỏ sinh ra hoặc đi theo nó.

[pause] Trong một trận đánh, lực lượng thường chia hai: những người mạnh nhất lo con chính, những người còn lại dọn dẹp bầy quái thú phụ.

[pause] Với tân binh, quái thú phụ là bài kiểm tra thật sự đầu tiên. Không lớn, nhưng rất đông, và chỉ một sai lầm là đủ trả giá.

[pause] Điểm thú vị: người tiêu diệt được nhiều quái thú phụ nhất không nhất thiết là người có tỉ lệ giải phóng cao nhất, mà là người phối hợp tốt nhất với đồng đội.

[pause] Kaku ghi chú: giống game chiến thuật, dọn quái nhỏ tốt thì trận đánh boss mới dễ.
```

### c04 · Chỉ số 4: Số hiệu quái thú / Chỉ số 5: Vũ khí số hiệu

Khoảng 102 giây · cảnh s32–s41 · 1330 ký tự

**Gemini**

```text
Có những quái thú nguy hiểm tới mức được đặt số hiệu riêng, như một hồ sơ truy nã. Kafka là số tám, và trước anh còn những con số khác.

<short pause> Được đánh số nghĩa là quái thú đó cực kỳ hiếm và cực kỳ mạnh. Cả lực lượng phải ghi nhớ đặc điểm của từng con.

<short pause> Trong truyện, có một quái thú mang số hiệu khiến mọi người lo sợ nhất: nó thông minh, biết nói, biết lập kế hoạch và còn có thể thay đổi hình dạng.

<short pause> Sự xuất hiện của quái thú thông minh khiến chỉ số sức mạnh không còn đủ. Một con quái thú biết suy nghĩ nguy hiểm hơn nhiều so với con số của nó.

<short pause> <laugh> Kaku ghi chú: đây là lúc truyện chuyển từ đánh quái vật sang một cuộc đấu trí. Những con số bắt đầu không còn nói hết sự thật.

<short pause> Điều gì xảy ra với quái thú mang số hiệu sau khi bị tiêu diệt? Lực lượng Phòng vệ biến cơ thể chúng thành vũ khí.

<short pause> Những vũ khí này được gọi theo số hiệu của quái thú gốc, và mang một phần năng lực của nó. Ví dụ, một vũ khí có thể giúp người dùng đọc trước chuyển động của đối thủ.

<short pause> Điểm mạnh: chúng đưa sức mạnh của con người vượt xa giới hạn một trăm phần trăm của bộ giáp thường.

<short pause> Điểm yếu: chỉ những người cực kỳ tương thích mới dùng được. Dùng sai người, vũ khí có thể phản chủ, gây tổn thương nặng cho chính người mặc.

<short pause> Và có một câu hỏi rùng rợn: nếu vũ khí làm từ quái thú, thì liệu một phần quái thú có còn sống trong đó không? Truyện để câu hỏi này lơ lửng rất lâu.
```

**ElevenLabs**

```text
Có những quái thú nguy hiểm tới mức được đặt số hiệu riêng, như một hồ sơ truy nã. Kafka là số tám, và trước anh còn những con số khác.

[pause] Được đánh số nghĩa là quái thú đó cực kỳ hiếm và cực kỳ mạnh. Cả lực lượng phải ghi nhớ đặc điểm của từng con.

[pause] Trong truyện, có một quái thú mang số hiệu khiến mọi người lo sợ nhất: nó thông minh, biết nói, biết lập kế hoạch và còn có thể thay đổi hình dạng.

[pause] Sự xuất hiện của quái thú thông minh khiến chỉ số sức mạnh không còn đủ. Một con quái thú biết suy nghĩ nguy hiểm hơn nhiều so với con số của nó.

[pause] [chuckles] Kaku ghi chú: đây là lúc truyện chuyển từ đánh quái vật sang một cuộc đấu trí. Những con số bắt đầu không còn nói hết sự thật.

[pause] [curious] Điều gì xảy ra với quái thú mang số hiệu sau khi bị tiêu diệt? Lực lượng Phòng vệ biến cơ thể chúng thành vũ khí.

[pause] Những vũ khí này được gọi theo số hiệu của quái thú gốc, và mang một phần năng lực của nó. Ví dụ, một vũ khí có thể giúp người dùng đọc trước chuyển động của đối thủ.

[pause] Điểm mạnh: chúng đưa sức mạnh của con người vượt xa giới hạn một trăm phần trăm của bộ giáp thường.

[pause] Điểm yếu: chỉ những người cực kỳ tương thích mới dùng được. Dùng sai người, vũ khí có thể phản chủ, gây tổn thương nặng cho chính người mặc.

[pause] Và có một câu hỏi rùng rợn: nếu vũ khí làm từ quái thú, thì liệu một phần quái thú có còn sống trong đó không? Truyện để câu hỏi này lơ lửng rất lâu.
```

### c05 · Kỳ thi tuyển: lần đầu bị đo / Bảng xếp hạng tỉ lệ giải phóng

Khoảng 114 giây · cảnh s42–s53 · 1480 ký tự

**Gemini**

```text
Trước khi xếp hạng, hãy xem những con số này được đo lần đầu ở đâu: kỳ thi tuyển của Lực lượng Phòng vệ.

<short pause> Kỳ thi gồm các bài kiểm tra thể lực, rồi một bài thi thực tế: thí sinh mặc giáp và đối đầu với quái thú thật trong một khu vực được kiểm soát.

<short pause> Ở bài thi đó, có tân binh thể hiện tỉ lệ giải phóng rất cao ngay lần đầu, được mọi người chú ý. Còn Kafka thì gần như không làm được gì với bộ giáp.

<short pause> Nhưng thay vì đánh, anh dùng kinh nghiệm dọn xác để chỉ cho các thí sinh khác chỗ yếu của quái thú. Một đội phó để ý điều đó.

<short pause> Nhờ vậy, anh được nhận vào với tư cách ứng viên dự bị, một cơ hội cuối cùng. Con số nói không, nhưng có người nhìn thấy thứ con số bỏ sót.

<short pause> <laugh> Kaku ghi chú: bài học tuyển dụng hay nhất trong anime. Nhìn hồ sơ thì thấy con số, nhìn người thì thấy tiềm năng.

<short pause> Giờ ghép các con số lại thành một bảng xếp hạng. Kaku không ghi tên từng người, chỉ ghi vai trò, để bạn thấy khoảng cách giữa các tầng.

<short pause> Tầng thấp nhất: Kafka ở dạng người, không phần trăm rồi một phần trăm. Kỷ lục thấp nhất lịch sử kỳ thi, theo đúng nghĩa đen.

<short pause> Tầng tân binh: những người vừa đỗ kỳ thi, thường ở mức vài chục phần trăm. Có tân binh thiên tài còn vượt xa mức đó ngay từ đầu.

<short pause> Tầng đội phó: những chiến binh kỳ cựu, tỉ lệ cao, chỉ huy một đội. Tầng đội trưởng: gần chạm trần, chín mươi phần trăm trở lên.

<short pause> Tầng đỉnh: người đứng đầu lực lượng, chín mươi tám phần trăm, cùng những người dùng vũ khí số hiệu vượt ra ngoài thang đo.

<short pause> Nhìn bảng này, Kafka có vẻ vô vọng. <short pause> Nhưng hãy nhớ, thẻ của anh có hai mặt.
```

**ElevenLabs**

```text
Trước khi xếp hạng, hãy xem những con số này được đo lần đầu ở đâu: kỳ thi tuyển của Lực lượng Phòng vệ.

[pause] Kỳ thi gồm các bài kiểm tra thể lực, rồi một bài thi thực tế: thí sinh mặc giáp và đối đầu với quái thú thật trong một khu vực được kiểm soát.

[pause] Ở bài thi đó, có tân binh thể hiện tỉ lệ giải phóng rất cao ngay lần đầu, được mọi người chú ý. Còn Kafka thì gần như không làm được gì với bộ giáp.

[pause] Nhưng thay vì đánh, anh dùng kinh nghiệm dọn xác để chỉ cho các thí sinh khác chỗ yếu của quái thú. Một đội phó để ý điều đó.

[pause] Nhờ vậy, anh được nhận vào với tư cách ứng viên dự bị, một cơ hội cuối cùng. Con số nói không, nhưng có người nhìn thấy thứ con số bỏ sót.

[pause] [chuckles] Kaku ghi chú: bài học tuyển dụng hay nhất trong anime. Nhìn hồ sơ thì thấy con số, nhìn người thì thấy tiềm năng.

[pause] Giờ ghép các con số lại thành một bảng xếp hạng. Kaku không ghi tên từng người, chỉ ghi vai trò, để bạn thấy khoảng cách giữa các tầng.

[pause] Tầng thấp nhất: Kafka ở dạng người, không phần trăm rồi một phần trăm. Kỷ lục thấp nhất lịch sử kỳ thi, theo đúng nghĩa đen.

[pause] Tầng tân binh: những người vừa đỗ kỳ thi, thường ở mức vài chục phần trăm. Có tân binh thiên tài còn vượt xa mức đó ngay từ đầu.

[pause] Tầng đội phó: những chiến binh kỳ cựu, tỉ lệ cao, chỉ huy một đội. Tầng đội trưởng: gần chạm trần, chín mươi phần trăm trở lên.

[pause] Tầng đỉnh: người đứng đầu lực lượng, chín mươi tám phần trăm, cùng những người dùng vũ khí số hiệu vượt ra ngoài thang đo.

[pause] Nhìn bảng này, Kafka có vẻ vô vọng. [pause] Nhưng hãy nhớ, thẻ của anh có hai mặt.
```

### c06 · Kafka: một người, hai thẻ chỉ số / Giới hạn của những con số / So với cấp bậc thợ săn

Khoảng 144 giây · cảnh s54–s68 · 1869 ký tự

**Gemini**

```text
Ở dạng người, Kafka là người yếu nhất lực lượng. Ở dạng quái thú số tám, anh có thể đấm tan một quái thú lớn chỉ bằng một cú.

<short pause> Vấn đề là anh không thể biến hình công khai. Nếu bị phát hiện, anh sẽ bị coi là quái thú và bị tiêu diệt. Nên anh phải giấu thẻ chỉ số mạnh nhất của mình.

<short pause> Ban đầu anh cũng chưa kiểm soát được sức mạnh. Có lúc biến hình không theo ý muốn, có lúc suýt mất kiểm soát hoàn toàn.

<short pause> Đây là cái giá của dạng quái thú: mạnh tuyệt đối, nhưng đổi lại là bí mật, sự nghi ngờ, và nỗi sợ trở thành chính thứ mình đang chiến đấu.

<short pause> <laugh> Kaku ghi chú: nếu thẻ chỉ số là game, Kafka giống người chơi có một tài khoản phụ siêu mạnh nhưng bị cấm đăng nhập.

<short pause> Giờ tới phần Kaku thích nhất: những con số bỏ sót điều gì?

<short pause> Thứ nhất: kinh nghiệm. Nhiều năm dọn xác quái thú giúp Kafka hiểu cấu tạo cơ thể quái thú hơn bất kỳ ai, biết chỗ nào là điểm yếu, chỗ nào là lõi.

<short pause> Kiến thức đó không hiện trên thanh phần trăm nào, nhưng nhiều lần giúp cả đội sống sót khi con số không đủ.

<short pause> Thứ hai: kỹ năng. Có những chiến binh không có tỉ lệ cao nhất, nhưng kiếm thuật hay chiến thuật của họ khiến quái thú mạnh hơn cũng phải dè chừng.

<short pause> Thứ ba: tinh thần. Ở tuổi ba mươi hai, sau bao lần bị từ chối, Kafka vẫn thi lại. Sự kiên trì đó không có máy nào đo được.

<short pause> Và thứ tư: đồng đội. Một con số chỉ đo một người. <short pause> Nhưng trong truyện, trận thắng quan trọng nào cũng là thắng của cả đội.

<short pause> Nếu bạn đã xem video số bảy của kênh về cấp bậc thợ săn trong Solo Leveling, bạn sẽ thấy hai hệ thống này rất khác nhau.

<short pause> Hệ thống thợ săn chia theo hạng chữ cái, cố định sau khi thức tỉnh. Hệ thống ở đây là những con số liên tục, thay đổi theo luyện tập.

<short pause> Một bên đo con người như món đồ được đóng nhãn một lần. Một bên đo như vận động viên, hôm nay có thể giỏi hơn hôm qua.

<short pause> Và cả hai bộ đều có chung một nhân vật chính bị đánh giá thấp nhất, rồi vượt qua mọi thang đo. Có lẽ khán giả rất thích xem những con số bị phá vỡ.
```

**ElevenLabs**

```text
Ở dạng người, Kafka là người yếu nhất lực lượng. Ở dạng quái thú số tám, anh có thể đấm tan một quái thú lớn chỉ bằng một cú.

[pause] Vấn đề là anh không thể biến hình công khai. Nếu bị phát hiện, anh sẽ bị coi là quái thú và bị tiêu diệt. Nên anh phải giấu thẻ chỉ số mạnh nhất của mình.

[pause] Ban đầu anh cũng chưa kiểm soát được sức mạnh. Có lúc biến hình không theo ý muốn, có lúc suýt mất kiểm soát hoàn toàn.

[pause] Đây là cái giá của dạng quái thú: mạnh tuyệt đối, nhưng đổi lại là bí mật, sự nghi ngờ, và nỗi sợ trở thành chính thứ mình đang chiến đấu.

[pause] [chuckles] Kaku ghi chú: nếu thẻ chỉ số là game, Kafka giống người chơi có một tài khoản phụ siêu mạnh nhưng bị cấm đăng nhập.

[pause] [curious] Giờ tới phần Kaku thích nhất: những con số bỏ sót điều gì?

[pause] Thứ nhất: kinh nghiệm. Nhiều năm dọn xác quái thú giúp Kafka hiểu cấu tạo cơ thể quái thú hơn bất kỳ ai, biết chỗ nào là điểm yếu, chỗ nào là lõi.

[pause] Kiến thức đó không hiện trên thanh phần trăm nào, nhưng nhiều lần giúp cả đội sống sót khi con số không đủ.

[pause] Thứ hai: kỹ năng. Có những chiến binh không có tỉ lệ cao nhất, nhưng kiếm thuật hay chiến thuật của họ khiến quái thú mạnh hơn cũng phải dè chừng.

[pause] Thứ ba: tinh thần. Ở tuổi ba mươi hai, sau bao lần bị từ chối, Kafka vẫn thi lại. Sự kiên trì đó không có máy nào đo được.

[pause] Và thứ tư: đồng đội. Một con số chỉ đo một người. [pause] Nhưng trong truyện, trận thắng quan trọng nào cũng là thắng của cả đội.

[pause] Nếu bạn đã xem video số bảy của kênh về cấp bậc thợ săn trong Solo Leveling, bạn sẽ thấy hai hệ thống này rất khác nhau.

[pause] Hệ thống thợ săn chia theo hạng chữ cái, cố định sau khi thức tỉnh. Hệ thống ở đây là những con số liên tục, thay đổi theo luyện tập.

[pause] Một bên đo con người như món đồ được đóng nhãn một lần. Một bên đo như vận động viên, hôm nay có thể giỏi hơn hôm qua.

[pause] Và cả hai bộ đều có chung một nhân vật chính bị đánh giá thấp nhất, rồi vượt qua mọi thang đo. Có lẽ khán giả rất thích xem những con số bị phá vỡ.
```

### c07 · Trò chơi: đoán kết quả trận đánh / Góc nhìn của Kaku: tuổi ba mươi hai

Khoảng 108 giây · cảnh s69–s78 · 1404 ký tự

**Gemini**

```text
Trước khi tới góc nhìn, chơi một trò nhanh. <laugh> Kaku đưa ra ba tình huống với số liệu tự đặt, bạn đoán xem đội nào thắng. Đây là trò chơi, không phải số liệu trong truyện.

<short pause> Tình huống một: năm tân binh, mỗi người ba mươi phần trăm, đối đầu một quái thú phụ nhỏ. Đáp án của Kaku: thắng, nếu họ phối hợp và không ai hành động một mình.

<short pause> Tình huống hai: một đội trưởng chín mươi sáu phần trăm, một mình, đối đầu quái thú lớn chỉ số tám phẩy năm. Đáp án: có thể thắng, nhưng rất rủi ro nếu không có ai dọn quái thú phụ.

<short pause> Tình huống ba: một người một phần trăm, có kinh nghiệm dọn xác, cùng một đội tân binh, đối đầu quái thú lạ. Đáp án: bất ngờ là cơ hội khá cao, vì biết điểm yếu có khi đáng giá hơn sức mạnh.

<short pause> Bạn có đoán giống Kaku không? Nếu không, hãy giải thích lý do của bạn trong phần bình luận, Kaku rất muốn đọc.

<short pause> Có một con số trên thẻ chỉ số Kaku muốn nói thêm: tuổi của Kafka, ba mươi hai.

<short pause> Phần lớn nhân vật chính trong truyện tranh thiếu niên là học sinh. Kafka là một người đàn ông trung niên, từng bỏ cuộc, đang làm một công việc không ai muốn làm.

<short pause> Nhưng chính vì vậy, câu chuyện của anh chạm tới nhiều người lớn: những ai cảm thấy mình đã lỡ chuyến tàu của ước mơ.

<short pause> Truyện nói rằng chưa bao giờ là quá muộn, và rằng những năm tháng tưởng như lãng phí, như dọn xác quái thú, có thể chính là thứ làm nên bạn.

<short pause> Kaku nghĩ đó là chỉ số quan trọng nhất trên thẻ: không phải phần trăm, mà là việc anh vẫn chưa bỏ cuộc.
```

**ElevenLabs**

```text
Trước khi tới góc nhìn, chơi một trò nhanh. [chuckles] Kaku đưa ra ba tình huống với số liệu tự đặt, bạn đoán xem đội nào thắng. Đây là trò chơi, không phải số liệu trong truyện.

[pause] Tình huống một: năm tân binh, mỗi người ba mươi phần trăm, đối đầu một quái thú phụ nhỏ. Đáp án của Kaku: thắng, nếu họ phối hợp và không ai hành động một mình.

[pause] Tình huống hai: một đội trưởng chín mươi sáu phần trăm, một mình, đối đầu quái thú lớn chỉ số tám phẩy năm. Đáp án: có thể thắng, nhưng rất rủi ro nếu không có ai dọn quái thú phụ.

[pause] Tình huống ba: một người một phần trăm, có kinh nghiệm dọn xác, cùng một đội tân binh, đối đầu quái thú lạ. Đáp án: bất ngờ là cơ hội khá cao, vì biết điểm yếu có khi đáng giá hơn sức mạnh.

[pause] [curious] Bạn có đoán giống Kaku không? Nếu không, hãy giải thích lý do của bạn trong phần bình luận, Kaku rất muốn đọc.

[pause] Có một con số trên thẻ chỉ số Kaku muốn nói thêm: tuổi của Kafka, ba mươi hai.

[pause] Phần lớn nhân vật chính trong truyện tranh thiếu niên là học sinh. Kafka là một người đàn ông trung niên, từng bỏ cuộc, đang làm một công việc không ai muốn làm.

[pause] Nhưng chính vì vậy, câu chuyện của anh chạm tới nhiều người lớn: những ai cảm thấy mình đã lỡ chuyến tàu của ước mơ.

[pause] Truyện nói rằng chưa bao giờ là quá muộn, và rằng những năm tháng tưởng như lãng phí, như dọn xác quái thú, có thể chính là thứ làm nên bạn.

[pause] Kaku nghĩ đó là chỉ số quan trọng nhất trên thẻ: không phải phần trăm, mà là việc anh vẫn chưa bỏ cuộc.
```

### c08 · Thẻ chỉ số của bạn / Kết

Khoảng 104 giây · cảnh s79–s89 · 1349 ký tự

**Gemini**

```text
Giờ tới lượt bạn. Lấy giấy bút ra, Kaku sẽ giúp bạn làm thẻ chỉ số. Đây là trò chơi vui, không có đúng sai.

<short pause> Dòng một, sức bền: bạn chạy bộ được bao lâu mà không dừng? Dưới năm phút ghi hai mươi phần trăm, trên ba mươi phút ghi tám mươi phần trăm.

<short pause> Dòng hai, bình tĩnh: khi gặp chuyện bất ngờ, bạn hoảng loạn hay suy nghĩ trước? Dòng ba, kinh nghiệm: bạn giỏi nhất việc gì mà người khác không để ý?

<short pause> Dòng bốn, đồng đội: khi làm việc nhóm, bạn là người dẫn đầu, người hỗ trợ, hay người nghĩ ra kế hoạch? Mỗi vai trò đều có giá trị riêng.

<short pause> Dòng cuối, không có thang đo: điều gì khiến bạn chưa bỏ cuộc? Viết nó vào thẻ. Đó là dòng quan trọng nhất.

<short pause> Hãy chia sẻ dòng cuối của bạn trong phần bình luận. <laugh> Kaku đọc hết đấy.

<short pause> Tóm lại: quái thú được đo bằng chỉ số sức mạnh, từ tám trở lên là quái thú lớn. Con người được đo bằng tỉ lệ giải phóng sức mạnh, tối đa một trăm phần trăm.

<short pause> Quái thú mạnh nhất được đánh số, và cơ thể chúng thành vũ khí số hiệu. Còn Kafka mang cả hai thẻ: một phần trăm và chín phẩy tám.

<short pause> Câu hỏi cho bạn: nếu có thể chọn, bạn muốn làm chiến binh mặc giáp với tỉ lệ cao, hay mang trong mình sức mạnh quái thú nhưng phải giữ bí mật?

<short pause> Video tới, Kaku sẽ leo từng nấc thang tiến hóa của kiếm Zanpakuto trong Bleach, từ Shikai đến Bankai, đúng lúc bộ anime vừa khép lại.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku tắt màn hình chỉ số đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ tới lượt bạn. Lấy giấy bút ra, Kaku sẽ giúp bạn làm thẻ chỉ số. Đây là trò chơi vui, không có đúng sai.

[pause] [curious] Dòng một, sức bền: bạn chạy bộ được bao lâu mà không dừng? Dưới năm phút ghi hai mươi phần trăm, trên ba mươi phút ghi tám mươi phần trăm.

[pause] Dòng hai, bình tĩnh: khi gặp chuyện bất ngờ, bạn hoảng loạn hay suy nghĩ trước? Dòng ba, kinh nghiệm: bạn giỏi nhất việc gì mà người khác không để ý?

[pause] Dòng bốn, đồng đội: khi làm việc nhóm, bạn là người dẫn đầu, người hỗ trợ, hay người nghĩ ra kế hoạch? Mỗi vai trò đều có giá trị riêng.

[pause] Dòng cuối, không có thang đo: điều gì khiến bạn chưa bỏ cuộc? Viết nó vào thẻ. Đó là dòng quan trọng nhất.

[pause] Hãy chia sẻ dòng cuối của bạn trong phần bình luận. [chuckles] Kaku đọc hết đấy.

[pause] Tóm lại: quái thú được đo bằng chỉ số sức mạnh, từ tám trở lên là quái thú lớn. Con người được đo bằng tỉ lệ giải phóng sức mạnh, tối đa một trăm phần trăm.

[pause] Quái thú mạnh nhất được đánh số, và cơ thể chúng thành vũ khí số hiệu. Còn Kafka mang cả hai thẻ: một phần trăm và chín phẩy tám.

[pause] Câu hỏi cho bạn: nếu có thể chọn, bạn muốn làm chiến binh mặc giáp với tỉ lệ cao, hay mang trong mình sức mạnh quái thú nhưng phải giữ bí mật?

[pause] Video tới, Kaku sẽ leo từng nấc thang tiến hóa của kiếm Zanpakuto trong Bleach, từ Shikai đến Bankai, đúng lúc bộ anime vừa khép lại.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku tắt màn hình chỉ số đây, hẹn gặp lại!
```
