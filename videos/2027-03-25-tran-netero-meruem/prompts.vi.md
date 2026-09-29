# Bộ prompt · Netero vs Meruem: Phân tích từng hiệp — lời cầu nguyện, số không và bông hồng

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 7 đoạn đọc, khoảng 14.8 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (84 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói trọn trận Netero đấu Meruem và cái kết của arc Kiến Chimera trong Hunter x Hu…

```text
Wide 16:9 landscape cinematic frame. a closed old notebook on a stone floor beside a spoiler warning card, close-up, dim dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một ông lão hơn trăm tuổi. Đối diện là một sinh vật mới ra đời chưa được bao lâu, nhưng được sinh ra để đứng…

```text
Wide 16:9 landscape cinematic frame. an elderly silhouette and a tall slender armored silhouette facing each other across a vast empty desert at dusk, wide shot, dramatic amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhiều người gọi đây là trận đấu hay nhất anime. Nhưng điều thú vị là trận này không kết thúc bằng một cú đấm.…

```text
Wide 16:9 landscape cinematic frame. a single rose lying on cracked stone ground in a ruined arena, extreme close-up, somber golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku phân tích trận Netero đấu Meruem theo từng hiệp: mỗi bên muốn gì, ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at a desk with a chess board and a stopwatch, opening a notebook with a serious face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Kaku nhắc trước: trận này có những khoảnh khắc rất nặng nề. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiết đau đ…

```text
Wide 16:9 landscape cinematic frame. a small candle burning steadily on a stone ledge in a dark hall, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Trước trận: tỉ số trên giấy

Lời: Bên trái sàn đấu: Isaac Netero, Chủ tịch Hiệp hội Hunter, được xem là người sử dụng Niệm mạnh nhất thế giới l…

```text
Wide 16:9 landscape cinematic frame. an elderly figure in simple loose clothing sitting cross-legged in meditation on a mountain ledge, back view, wide shot, calm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Bên phải sàn đấu: Meruem, Vua Kiến Chimera. Sinh ra đã mạnh hơn mọi thuộc hạ, và mỗi lần ăn một người có Niệm…

```text
Wide 16:9 landscape cinematic frame. a tall slender armored silhouette standing on a palace balcony above a kneeling crowd of shadowy guards, low-angle shot, cold regal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Trên giấy, tỉ số nghiêng hẳn về Meruem. Tốc độ, sức mạnh, độ bền, khả năng học: Vua vượt trội ở gần như mọi c…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn comparison chart on parchment with two columns of bars, one column much taller than the other, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Netero chỉ có hai thứ: kinh nghiệm, và một kỹ thuật đã mài giũa suốt cả đời. Câu hỏi của trận đấu là: hai thứ…

```text
Wide 16:9 landscape cinematic frame. an old weathered hand resting beside a single well-worn training glove on a wooden floor, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và cả hai bên đều biết: nếu Vua thắng, loài người có thể mất vị trí trên đỉnh thế giới. Đây không chỉ là một…

```text
Wide 16:9 landscape cinematic frame. a globe on a desk with a crack spreading across it, close-up, tense dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Hồ sơ hai đấu thủ

Lời: Năm bốn mươi sáu tuổi, Netero cảm thấy võ công của mình đã chạm giới hạn. Ông lên núi, và bắt đầu một bài tập…

```text
Wide 16:9 landscape cinematic frame. an elderly figure climbing a narrow mountain path alone with a small bundle on their back, wide shot, misty dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Trước mỗi cú đấm, ông chắp tay cầu nguyện, tỏ lòng biết ơn với võ đạo. Lúc đầu, một vạn cú đấm mất mười tám t…

```text
Wide 16:9 landscape cinematic frame. two hands pressed together in prayer in front of a rising sun on a mountain peak, close-up, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhiều năm sau, ông đấm xong một vạn cú trong chưa tới một tiếng, và cú đấm nhanh hơn cả tiếng động của nó. Kh…

```text
Wide 16:9 landscape cinematic frame. a blur of countless fists in the air around a praying figure on a mountaintop, dynamic wide shot, radiant morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Từ đó sinh ra năng lực Bách Thức Quan Âm: một pho tượng khổng lồ bằng Niệm, với vô số bàn tay, ra đòn ngay kh…

```text
Wide 16:9 landscape cinematic frame. a colossal translucent golden figure with countless hands rising behind a small praying silhouette, dramatic low-angle shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Còn Meruem thì ngược lại hoàn toàn. Không cần luyện tập, chỉ cần quan sát là học được. Vua học một trò chơi m…

```text
Wide 16:9 landscape cinematic frame. a board game table with scattered pieces and several defeated shadowy opponents slumped around it, wide shot, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Nhưng có một người Vua không thắng nổi: Komugi, một cô gái mù vô địch môn cờ quân sự gọi là Gungi. Và những v…

```text
Wide 16:9 landscape cinematic frame. a small hand placing a game piece on a wooden board with calm precision, a larger clawed hand hesitating opposite, extreme close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: hai đấu thủ đại diện cho hai kiểu mạnh. Một người mạnh nhờ lặp lại một điều suốt nửa đời. Một kẻ m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a worn training glove in one wing and a fresh open book in the other, weighing them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Hiệp 0: đưa Vua ra khỏi cung điện

Lời: Mục tiêu đầu tiên của Netero: tách Vua khỏi ba cận vệ Hoàng gia. Ở cung điện, Vua có người bảo vệ. Ở nơi hoan…

```text
Wide 16:9 landscape cinematic frame. a map on parchment showing a palace with three guard icons and an arrow leading far away to an empty region, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Kế hoạch được chuẩn bị kỹ: một cuộc tấn công từ trên trời làm cả cung điện rối loạn, trong khi các Hunter khá…

```text
Wide 16:9 landscape cinematic frame. a rain of glowing dragon-shaped energy falling from the night sky onto a distant palace, dramatic wide shot, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Và điều bất ngờ nhất: Netero không phải lôi Vua đi. Vua tự nguyện đi theo ông, tới một vùng đất trống cách xa…

```text
Wide 16:9 landscape cinematic frame. two small silhouettes flying side by side over a moonlit wasteland, wide shot, cold silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Vì sao? Meruem khi đó đã tò mò về loài người, và muốn nói chuyện với người mạnh nhất của họ. Vua không coi Ne…

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette with head tilted in curiosity, facing a small old figure, medium shot, soft moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kaku ghi vào sổ: hiệp 0 là của Netero. Ông có được thứ ông muốn nhất, là một trận tay đôi, mà không mất một g…

```text
Wide 16:9 landscape cinematic frame. a small scorecard with a tick in the first box under the elderly figure icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Hiệp 1: lời đề nghị và lời từ chối

Lời: Tới nơi, Meruem đưa ra một đề nghị: hai bên nói chuyện, không cần đánh. Vua muốn hiểu loài người, và muốn biế…

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette extending an open hand toward an elderly figure across a stone floor, medium shot, dim dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Netero từ chối. Với ông, đây là nhiệm vụ: loài Kiến Chimera là mối đe dọa với loài người, và Vua phải bị ngăn…

```text
Wide 16:9 landscape cinematic frame. an elderly figure shaking their head calmly with hands tucked in wide sleeves, close-up, stern dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nhưng có một lý do sâu hơn. Netero đã già, và từ lâu ông không còn tìm được đối thủ xứng tầm. Đứng trước Vua,…

```text
Wide 16:9 landscape cinematic frame. an elderly face with a faint hungry smile and sharp eyes, extreme close-up, dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Meruem đưa ra một điều kiện: nếu Netero đánh trúng được Vua một lần, Vua sẽ nghe ông. Vua tự tin tới mức cho…

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette standing with arms relaxed, inviting an attack, low-angle shot, cold confident light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Netero nhận lời ngay. Với một võ sĩ, được ra đòn trước là món quà lớn nhất mà đối thủ có thể tặng.

```text
Wide 16:9 landscape cinematic frame. an elderly figure slowly raising both hands toward a prayer position, close-up, focused golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là sai lầm chiến thuật đầu tiên của Vua. Coi thường đối thủ không phải là kiêu ngạo, mà là chư…

```text
Wide 16:9 landscape cinematic frame. the owl mascot scribbling a big question mark next to a crown doodle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Hiệp 2: Bách Thức Quan Âm áp đảo

Lời: Netero chắp tay. Pho tượng Quan Âm hiện ra sau lưng ông, và bàn tay khổng lồ giáng xuống trước khi Vua kịp nh…

```text
Wide 16:9 landscape cinematic frame. a colossal golden hand of light slamming down onto a tall slender silhouette, dynamic wide shot, blinding golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Bí mật nằm ở lời cầu nguyện. Nhờ một vạn cú đấm mỗi ngày trong nhiều năm, động tác chắp tay của Netero nhanh…

```text
Wide 16:9 landscape cinematic frame. two hands snapping together so fast they leave afterimages, extreme close-up, bright motion blur light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và mỗi tư thế tay lại ứng với một đòn khác nhau. Tay này là cú đập, tay kia là cú tát ngang, tay kia nữa là c…

```text
Wide 16:9 landscape cinematic frame. a diagram on parchment of several hand gestures, each linked by an arrow to a different attack symbol, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Vua bị đánh văng hết lần này tới lần khác. Hàng trăm, rồi hàng nghìn đòn. Một cỗ máy chiến đấu không có bất k…

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette flung repeatedly through the air by countless golden hands in a dusty stone arena, dynamic wide shot, intense golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nhưng có một vấn đề. Mỗi đòn đều trúng, mà Vua gần như không bị thương. Lớp vỏ của Meruem quá cứng. Netero đa…

```text
Wide 16:9 landscape cinematic frame. a single hairline crack on an otherwise flawless dark armored shoulder, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi vào sổ: hiệp 2 vẫn là của Netero, nhưng đồng hồ đang chạy ngược lại ông. Mỗi đòn đánh tiêu hao sức c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking anxiously at an hourglass while tallying marks on a scorecard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Hiệp 3: Vua học

Lời: Trong lúc bị đánh, Meruem làm điều Vua giỏi nhất: quan sát. Đòn nào tới trước, tay nào theo sau, nhịp chắp ta…

```text
Wide 16:9 landscape cinematic frame. a pair of calm focused eyes reflecting countless golden hands, extreme close-up, cold analytical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Vua nhận ra một điều: mọi đòn của Quan Âm đều bắt đầu từ lời cầu nguyện. Nếu ngăn được Netero chắp tay, pho t…

```text
Wide 16:9 landscape cinematic frame. a diagram on parchment showing praying hands with an arrow to a giant statue and a big red cross over the hands, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Cùng lúc, Netero bắt đầu chậm lại. Không nhiều, chỉ một chút. Nhưng với một đối thủ như Vua, một chút là đủ.

```text
Wide 16:9 landscape cinematic frame. an elderly figure breathing hard with a single bead of sweat on their brow, close-up, harsh dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Và trong một khoảnh khắc, Vua hành động. Netero mất một chân, rồi mất một cánh tay. Kaku không đi vào chi tiế…

```text
Wide 16:9 landscape cinematic frame. a single torn sleeve drifting down through dusty air in a ruined stone hall, symbolic close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhưng Netero vẫn đứng đó, và vẫn mỉm cười. Còn Vua lại hỏi một câu lạ: Vua muốn biết tên của ông.

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette standing over a kneeling elderly figure, both still, wide shot, dusty golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là lúc Vua thay đổi. Kẻ sinh ra để coi loài người là thức ăn, giờ muốn nhớ tên một con người.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a name tag with great care, holding it up gently. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Kaku ghi vào sổ: hiệp 3 là của Meruem. Vua tìm ra điểm yếu duy nhất của một kỹ thuật không có khe hở, và khai…

```text
Wide 16:9 landscape cinematic frame. a scorecard with a tick in the third box under the crown icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Hiệp 4: Linh Thủ, lòng bàn tay số không

Lời: Netero còn một con bài: đòn cuối cùng của Bách Thức Quan Âm, gọi là Linh Thủ, lòng bàn tay số không. Đòn này…

```text
Wide 16:9 landscape cinematic frame. a colossal golden figure with all its hands closing into a single embrace around a tiny silhouette, dramatic wide shot, blinding golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Pho tượng ôm lấy Vua, và bắn ra một luồng sáng khổng lồ. Cả khu vực rung chuyển, mặt đất bị xé toạc.

```text
Wide 16:9 landscape cinematic frame. a pillar of blinding light erupting into the sky from a desert and shaking the ground in a wide shockwave, dramatic wide shot, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Khi khói bụi tan, Netero không còn là ông lão khỏe mạnh lúc đầu. Dồn hết Niệm, cơ thể ông như già thêm chục n…

```text
Wide 16:9 landscape cinematic frame. a frail elderly figure kneeling in settling dust, visibly thinner and more worn, wide shot, pale fading light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Còn Vua? Vẫn đứng. Bị thương, nhưng đứng. Đòn mạnh nhất của người mạnh nhất loài người không đủ để hạ gục Vua…

```text
Wide 16:9 landscape cinematic frame. a tall slender armored silhouette standing in a crater with scorched but intact armor, low-angle shot, cold light through dust. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Linh Thủ không thất bại vì Netero yếu. Nó thất bại vì con số trên giấy từ đầu đã đúng. Về sức mạnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quietly closing a chart of bar graphs with a sad nod. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Kaku ghi vào sổ: hiệp 4 thuộc về Meruem. Và nếu trận đấu chỉ là sức mạnh, đây là lúc nó kết thúc.

```text
Wide 16:9 landscape cinematic frame. a scorecard with a tick in the fourth box under the crown icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Hiệp 5: bông hồng của kẻ nghèo

Lời: Nhưng Netero đã tính trước điều này. Ngay từ đầu, ông biết mình có thể không thắng bằng võ công. Ông mang the…

```text
Wide 16:9 landscape cinematic frame. an elderly figure with eyes closed and a calm faint smile in the settling dust, close-up, soft dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Trong cơ thể Netero có một quả bom thu nhỏ, tên là Bông Hồng Của Kẻ Nghèo. Nó được nối với nhịp tim của ông,…

```text
Wide 16:9 landscape cinematic frame. a small glowing rose-shaped mechanism resting inside a clockwork heart diagram on parchment, symbolic close-up, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Trước khi kích hoạt, Netero nói với Vua, đại ý: ngươi không hiểu gì về loài người cả. Ác ý của con người là k…

```text
Wide 16:9 landscape cinematic frame. an elderly figure looking up with a piercing calm stare at a tall silhouette, extreme close-up, dramatic red side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Và theo lời người kể chuyện, đó là lần đầu tiên Meruem cảm thấy sợ hãi.

```text
Wide 16:9 landscape cinematic frame. a tall slender silhouette taking a single step backward, its shadow trembling on the stone wall, medium shot, dim red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Netero chọn hy sinh chính mình. Bông hồng nở ra thành một vụ nổ khổng lồ, hình dáng như một đóa hồng lửa trên…

```text
Wide 16:9 landscape cinematic frame. a giant rose-shaped blossom of fire blooming over a distant desert at dusk, seen from very far away, wide shot, eerie orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nhiều người đọc thấy quả bom này như một phép ẩn dụ cho vũ khí hủy diệt của loài người ngoài đời thật. Tác gi…

```text
Wide 16:9 landscape cinematic frame. a withered rose lying on a historical-style map of the world with faint shadows over it, symbolic close-up, grey somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kaku ghi vào sổ: hiệp 5 là của Netero, nhưng không phải chiến thắng của ông. Đó là chiến thắng của thứ ông ma…

```text
Wide 16:9 landscape cinematic frame. a scorecard with the fifth box ticked in a faded grey ink under a small rose icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Sau trận: người thắng thật sự

Lời: Meruem sống sót qua vụ nổ. Cận vệ Hoàng gia tìm thấy và chữa trị cho Vua. Nhưng bông hồng còn một thứ nữa: ch…

```text
Wide 16:9 landscape cinematic frame. a faint violet mist drifting across a scorched desert under a pale sky, wide shot, eerie cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Chất độc lan dần trong cơ thể Vua, và cả những ai ở gần. Không thuốc giải. Người thắng trận đấu, thật ra đã t…

```text
Wide 16:9 landscape cinematic frame. a small hourglass with violet sand draining slowly on a stone table, close-up, dim violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Biết mình sắp chết, Meruem chọn làm gì? Không trả thù, không chinh phục. Vua chỉ muốn quay lại chơi cờ với Ko…

```text
Wide 16:9 landscape cinematic frame. a small wooden game board set up on a quiet table in a dim room, two cushions facing each other, close-up, soft lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Sau vụ nổ, Vua mới biết tên của chính mình, cái tên mà Nữ hoàng đã đặt trước khi qua đời: Meruem, nghĩa là án…

```text
Wide 16:9 landscape cinematic frame. a faint name written in golden light on an old scroll unrolled on a stone floor, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hai người chơi những ván cuối cùng trong một căn phòng yên tĩnh. Komugi biết mình cũng bị nhiễm độc, nhưng ch…

```text
Wide 16:9 landscape cinematic frame. two silhouettes sitting across a small game board in a dim quiet room, a single lamp between them, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku không kể thêm. Nhưng Kaku muốn bạn để ý: kẻ sinh ra để thay thế loài người, trong những giờ cuối, lại số…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting quietly with its hat off, looking at a small lamp. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Vì sao trận này được nhớ mãi

Lời: Arc Kiến Chimera nổi tiếng với giọng người kể chuyện. Những suy nghĩ chỉ diễn ra trong vài giây được kể thành…

```text
Wide 16:9 landscape cinematic frame. a pocket watch with its second hand frozen mid-tick, surrounded by floating lines of handwritten text, extreme close-up, dim golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Trong trận này, người kể chuyện cho ta vào đầu cả hai bên. Ta biết Netero đang tính gì, và cũng biết Vua đang…

```text
Wide 16:9 landscape cinematic frame. two thought bubbles drawn on parchment above two facing silhouettes, each filled with tiny diagrams, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Không có ai cổ vũ. Không có đồng đội xông vào giúp. Chỉ có hai bên, một vùng đất trống, và một câu hỏi: loài…

```text
Wide 16:9 landscape cinematic frame. a vast empty desert with only two tiny silhouettes far apart under a huge sky, extreme wide shot, lonely dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Bản anime 2011 dựng trận này với nhiều khoảng lặng và lời kể, thay vì chỉ có tiếng đòn đánh. Chính khoảng lặn…

```text
Wide 16:9 landscape cinematic frame. a single drop of water falling in slow motion onto a still stone floor, extreme close-up, quiet cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: một trận đấu hay không cần nhiều chiêu thức. Nó cần hai người có lý do thật để đứng đó, và một cái…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up two fingers and then pointing at a small rose on the desk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Sơ đồ chiến thuật

Lời: Tổng kết bằng một trang. Hiệp 0: Netero tách Vua ra một mình. Hiệp 1: Vua coi thường đối thủ và cho ra đòn tr…

```text
Wide 16:9 landscape cinematic frame. a strategy diagram on parchment with numbered boxes and arrows between a small old figure icon and a crown icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Hiệp 2: Quan Âm áp đảo nhưng không gây sát thương thật. Hiệp 3: Vua tìm ra điểm yếu, lời cầu nguyện.

```text
Wide 16:9 landscape cinematic frame. the middle boxes of the strategy diagram glowing, one with praying hands icon crossed out, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Hiệp 4: Linh Thủ dồn hết sức nhưng thất bại. Hiệp 5: bông hồng, phương án được chuẩn bị từ trước khi trận đấu…

```text
Wide 16:9 landscape cinematic frame. the final boxes of the diagram with a burst icon and a rose icon, amber ink close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Và mũi tên quan trọng nhất trên sơ đồ không nằm trong trận đấu. Nó nối từ bàn cờ Gungi tới câu hỏi tên của Vu…

```text
Wide 16:9 landscape cinematic frame. a long red arrow on the diagram leading from a small game board icon to a speech bubble with a question mark, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Ba bài học chiến thuật

Lời: Bài học một: chọn chiến trường. Netero thắng hiệp đầu tiên trước khi tung ra cú đấm nào, chỉ bằng việc đưa Vu…

```text
Wide 16:9 landscape cinematic frame. a chess piece being moved from a crowded board corner to an empty open square, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Bài học hai: kỹ thuật không có khe hở vẫn có điểm bắt đầu. Quan Âm không có lỗ hổng trong đòn đánh, nhưng lời…

```text
Wide 16:9 landscape cinematic frame. a fortress with perfect walls except a single gate glowing faintly, parchment illustration style, amber light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Bài học ba: phương án cuối cùng luôn có cái giá. Bông hồng thắng được Vua, nhưng cái giá là mạng sống của Net…

```text
Wide 16:9 landscape cinematic frame. a scale with a rose on one pan and a pile of small silhouettes on the other, symbolic close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và thêm một bài học không phải chiến thuật: đôi khi, thứ thay đổi một trận đấu lớn nhất lại đến từ một ván cờ…

```text
Wide 16:9 landscape cinematic frame. a single game piece standing alone on a board in a quiet sunlit room, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Nếu Netero trẻ hơn năm mươi tuổi?

Lời: Có một câu hỏi fan tranh luận mãi: nếu Netero đấu Vua ở thời sung sức nhất, ông có thắng không?

```text
Wide 16:9 landscape cinematic frame. an old framed photograph of a younger vigorous silhouette beside a current photo of an elderly one, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Phe nói có cho rằng lúc sung sức, ông nhanh hơn, bền hơn, và đủ sức giữ nhịp Quan Âm lâu hơn, đủ để Vua không…

```text
Wide 16:9 landscape cinematic frame. a younger silhouette surrounded by countless golden hands moving at dazzling speed, dynamic wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Phe nói không thì chỉ ra: vấn đề chưa bao giờ là tốc độ. Hàng nghìn đòn trúng mà Vua gần như không bị thương.…

```text
Wide 16:9 landscape cinematic frame. a fist of light bouncing off a flawless dark armored plate, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghiêng về một ý khác: câu hỏi ấy có lẽ không quan trọng với tác giả. Trận đấu được viết để cho thấy võ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently closing a photo album with a thoughtful look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Góc nhìn của Kaku

Lời: Kaku nghĩ trận này hay không phải vì đòn đánh đẹp. Nó hay vì cả hai đều thay đổi trong lúc đánh. Netero bắt đ…

```text
Wide 16:9 landscape cinematic frame. a split image of the same elderly silhouette, one half praying on a mountain, one half standing in a dark ruin, symbolic close-up, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Còn Meruem bắt đầu như một vị vua coi loài người là thức ăn, và kết thúc như một người chỉ muốn chơi thêm một…

```text
Wide 16:9 landscape cinematic frame. a crown lying beside a small game board on a quiet table, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi Kaku muốn để lại: ai là con người hơn trong trận này? Người đã mang theo bông hồng, hay kẻ đã hỏi tên…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at two small figurines on a desk, one elderly and one tall and slender, thinking deeply. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Kaku không có câu trả lời. Hãy viết câu trả lời của bạn vào bình luận. Kaku đọc hết.

```text
Wide 16:9 landscape cinematic frame. an open notebook with two blank columns labeled with a rose icon and a game piece icon, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Một vạn cú đấm mỗi ngày. Một lời cầu nguyện nhanh hơn phản xạ của Vua. Và một bông hồng mà chính người mang n…

```text
Wide 16:9 landscape cinematic frame. a single rose resting on two praying hands carved in stone at sunset, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tiếp theo, Kaku đổi hẳn không khí: Blue Lock, và bảng xếp hạng vũ khí của các tiền đạo. Ai có vũ khí đá…

```text
Wide 16:9 landscape cinematic frame. a football on a pitch under stadium lights with a glowing goal in the background, dramatic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem Kaku mổ xẻ từng hiệp đấu, hãy đăng ký kênh. Và lần tới bạn chắp tay cảm ơn một điều gì đó,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pressing its wings together in a small thankful bow, then waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Trước trận: tỉ số trên giấy

Khoảng 119 giây · cảnh s01–s10 · 1543 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói trọn trận Netero đấu Meruem và cái kết của arc Kiến Chimera trong Hunter x Hunter. Nếu bạn chưa xem tới tập 126 bản 2011, hãy lưu video lại cho sau này.

<short pause> Một ông lão hơn trăm tuổi. Đối diện là một sinh vật mới ra đời chưa được bao lâu, nhưng được sinh ra để đứng trên đỉnh chuỗi thức ăn. Người mạnh nhất loài người, đấu với kẻ sinh ra để thay thế loài người.

<short pause> Nhiều người gọi đây là trận đấu hay nhất anime. <short pause> Nhưng điều thú vị là trận này không kết thúc bằng một cú đấm. Nó kết thúc bằng một lựa chọn mà người thắng lại là kẻ đã thua.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku phân tích trận Netero đấu Meruem theo từng hiệp: mỗi bên muốn gì, chọn gì, và trả giá gì. Cuối video là sơ đồ chiến thuật cả trận trong một trang.

<short pause> Kaku nhắc trước: trận này có những khoảnh khắc rất nặng nề. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiết đau đớn, nhưng không né tránh ý nghĩa của nó.

<short pause> Bên trái sàn đấu: Isaac Netero, Chủ tịch Hiệp hội Hunter, được xem là người sử dụng Niệm mạnh nhất thế giới loài người. Kinh nghiệm hơn một thế kỷ.

<short pause> Bên phải sàn đấu: Meruem, Vua Kiến Chimera. Sinh ra đã mạnh hơn mọi thuộc hạ, và mỗi lần ăn một người có Niệm mạnh, nó lại mạnh thêm.

<short pause> Trên giấy, tỉ số nghiêng hẳn về Meruem. Tốc độ, sức mạnh, độ bền, khả năng học: Vua vượt trội ở gần như mọi chỉ số.

<short pause> Netero chỉ có hai thứ: kinh nghiệm, và một kỹ thuật đã mài giũa suốt cả đời. Câu hỏi của trận đấu là: hai thứ đó có đủ không?

<short pause> Và cả hai bên đều biết: nếu Vua thắng, loài người có thể mất vị trí trên đỉnh thế giới. Đây không chỉ là một trận đấu tay đôi.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói trọn trận Netero đấu Meruem và cái kết của arc Kiến Chimera trong Hunter x Hunter. Nếu bạn chưa xem tới tập 126 bản 2011, hãy lưu video lại cho sau này.

[pause] Một ông lão hơn trăm tuổi. Đối diện là một sinh vật mới ra đời chưa được bao lâu, nhưng được sinh ra để đứng trên đỉnh chuỗi thức ăn. Người mạnh nhất loài người, đấu với kẻ sinh ra để thay thế loài người.

[pause] Nhiều người gọi đây là trận đấu hay nhất anime. [pause] Nhưng điều thú vị là trận này không kết thúc bằng một cú đấm. Nó kết thúc bằng một lựa chọn mà người thắng lại là kẻ đã thua.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku phân tích trận Netero đấu Meruem theo từng hiệp: mỗi bên muốn gì, chọn gì, và trả giá gì. Cuối video là sơ đồ chiến thuật cả trận trong một trang.

[pause] Kaku nhắc trước: trận này có những khoảnh khắc rất nặng nề. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiết đau đớn, nhưng không né tránh ý nghĩa của nó.

[pause] Bên trái sàn đấu: Isaac Netero, Chủ tịch Hiệp hội Hunter, được xem là người sử dụng Niệm mạnh nhất thế giới loài người. Kinh nghiệm hơn một thế kỷ.

[pause] Bên phải sàn đấu: Meruem, Vua Kiến Chimera. Sinh ra đã mạnh hơn mọi thuộc hạ, và mỗi lần ăn một người có Niệm mạnh, nó lại mạnh thêm.

[pause] Trên giấy, tỉ số nghiêng hẳn về Meruem. Tốc độ, sức mạnh, độ bền, khả năng học: Vua vượt trội ở gần như mọi chỉ số.

[pause] Netero chỉ có hai thứ: kinh nghiệm, và một kỹ thuật đã mài giũa suốt cả đời. [curious] Câu hỏi của trận đấu là: hai thứ đó có đủ không?

[pause] Và cả hai bên đều biết: nếu Vua thắng, loài người có thể mất vị trí trên đỉnh thế giới. Đây không chỉ là một trận đấu tay đôi.
```

### c02 · Hồ sơ hai đấu thủ / Hiệp 0: đưa Vua ra khỏi cung điện

Khoảng 133 giây · cảnh s11–s22 · 1725 ký tự

**Gemini**

```text
Năm bốn mươi sáu tuổi, Netero cảm thấy võ công của mình đã chạm giới hạn. Ông lên núi, và bắt đầu một bài tập kỳ lạ: mỗi ngày một vạn cú đấm cảm tạ.

<short pause> Trước mỗi cú đấm, ông chắp tay cầu nguyện, tỏ lòng biết ơn với võ đạo. Lúc đầu, một vạn cú đấm mất mười tám tiếng. Ông kiệt sức, ngủ gục, rồi hôm sau lại tiếp tục.

<short pause> Nhiều năm sau, ông đấm xong một vạn cú trong chưa tới một tiếng, và cú đấm nhanh hơn cả tiếng động của nó. Khi xuống núi, ông đã thành một người khác.

<short pause> Từ đó sinh ra năng lực Bách Thức Quan Âm: một pho tượng khổng lồ bằng Niệm, với vô số bàn tay, ra đòn ngay khi ông chắp tay cầu nguyện.

<short pause> Còn Meruem thì ngược lại hoàn toàn. Không cần luyện tập, chỉ cần quan sát là học được. Vua học một trò chơi mới, và chỉ sau vài ván đã thắng những kỳ thủ giỏi nhất.

<short pause> Nhưng có một người Vua không thắng nổi: Komugi, một cô gái mù vô địch môn cờ quân sự gọi là Gungi. Và những ván cờ ấy đang thay đổi Vua từ bên trong.

<short pause> <laugh> Kaku để ý: hai đấu thủ đại diện cho hai kiểu mạnh. Một người mạnh nhờ lặp lại một điều suốt nửa đời. Một kẻ mạnh nhờ học mọi thứ gần như ngay lập tức.

<short pause> Mục tiêu đầu tiên của Netero: tách Vua khỏi ba cận vệ Hoàng gia. Ở cung điện, Vua có người bảo vệ. Ở nơi hoang vắng, Vua chỉ có một mình.

<short pause> Kế hoạch được chuẩn bị kỹ: một cuộc tấn công từ trên trời làm cả cung điện rối loạn, trong khi các Hunter khác kéo từng cận vệ ra xa.

<short pause> Và điều bất ngờ nhất: Netero không phải lôi Vua đi. Vua tự nguyện đi theo ông, tới một vùng đất trống cách xa cung điện.

<short pause> Vì sao? Meruem khi đó đã tò mò về loài người, và muốn nói chuyện với người mạnh nhất của họ. Vua không coi Netero là mối đe dọa, mà là một người đối thoại.

<short pause> Kaku ghi vào sổ: hiệp 0 là của Netero. Ông có được thứ ông muốn nhất, là một trận tay đôi, mà không mất một giọt sức nào.
```

**ElevenLabs**

```text
Năm bốn mươi sáu tuổi, Netero cảm thấy võ công của mình đã chạm giới hạn. Ông lên núi, và bắt đầu một bài tập kỳ lạ: mỗi ngày một vạn cú đấm cảm tạ.

[pause] Trước mỗi cú đấm, ông chắp tay cầu nguyện, tỏ lòng biết ơn với võ đạo. Lúc đầu, một vạn cú đấm mất mười tám tiếng. Ông kiệt sức, ngủ gục, rồi hôm sau lại tiếp tục.

[pause] Nhiều năm sau, ông đấm xong một vạn cú trong chưa tới một tiếng, và cú đấm nhanh hơn cả tiếng động của nó. Khi xuống núi, ông đã thành một người khác.

[pause] Từ đó sinh ra năng lực Bách Thức Quan Âm: một pho tượng khổng lồ bằng Niệm, với vô số bàn tay, ra đòn ngay khi ông chắp tay cầu nguyện.

[pause] Còn Meruem thì ngược lại hoàn toàn. Không cần luyện tập, chỉ cần quan sát là học được. Vua học một trò chơi mới, và chỉ sau vài ván đã thắng những kỳ thủ giỏi nhất.

[pause] Nhưng có một người Vua không thắng nổi: Komugi, một cô gái mù vô địch môn cờ quân sự gọi là Gungi. Và những ván cờ ấy đang thay đổi Vua từ bên trong.

[pause] [chuckles] Kaku để ý: hai đấu thủ đại diện cho hai kiểu mạnh. Một người mạnh nhờ lặp lại một điều suốt nửa đời. Một kẻ mạnh nhờ học mọi thứ gần như ngay lập tức.

[pause] Mục tiêu đầu tiên của Netero: tách Vua khỏi ba cận vệ Hoàng gia. Ở cung điện, Vua có người bảo vệ. Ở nơi hoang vắng, Vua chỉ có một mình.

[pause] Kế hoạch được chuẩn bị kỹ: một cuộc tấn công từ trên trời làm cả cung điện rối loạn, trong khi các Hunter khác kéo từng cận vệ ra xa.

[pause] Và điều bất ngờ nhất: Netero không phải lôi Vua đi. Vua tự nguyện đi theo ông, tới một vùng đất trống cách xa cung điện.

[pause] [curious] Vì sao? Meruem khi đó đã tò mò về loài người, và muốn nói chuyện với người mạnh nhất của họ. Vua không coi Netero là mối đe dọa, mà là một người đối thoại.

[pause] Kaku ghi vào sổ: hiệp 0 là của Netero. Ông có được thứ ông muốn nhất, là một trận tay đôi, mà không mất một giọt sức nào.
```

### c03 · Hiệp 1: lời đề nghị và lời từ chối / Hiệp 2: Bách Thức Quan Âm áp đảo

Khoảng 126 giây · cảnh s23–s34 · 1633 ký tự

**Gemini**

```text
Tới nơi, Meruem đưa ra một đề nghị: hai bên nói chuyện, không cần đánh. Vua muốn hiểu loài người, và muốn biết Netero có thể chấp nhận điều kiện gì.

<short pause> Netero từ chối. Với ông, đây là nhiệm vụ: loài Kiến Chimera là mối đe dọa với loài người, và Vua phải bị ngăn lại.

<short pause> Nhưng có một lý do sâu hơn. Netero đã già, và từ lâu ông không còn tìm được đối thủ xứng tầm. Đứng trước Vua, ông lại cảm thấy mình là kẻ thách đấu.

<short pause> Meruem đưa ra một điều kiện: nếu Netero đánh trúng được Vua một lần, Vua sẽ nghe ông. Vua tự tin tới mức cho đối thủ ra đòn trước.

<short pause> Netero nhận lời ngay. Với một võ sĩ, được ra đòn trước là món quà lớn nhất mà đối thủ có thể tặng.

<short pause> <laugh> Kaku để ý: đây là sai lầm chiến thuật đầu tiên của Vua. Coi thường đối thủ không phải là kiêu ngạo, mà là chưa có đủ dữ liệu. Và Vua sắp có rất nhiều dữ liệu.

<short pause> Netero chắp tay. Pho tượng Quan Âm hiện ra sau lưng ông, và bàn tay khổng lồ giáng xuống trước khi Vua kịp nhìn thấy.

<short pause> Bí mật nằm ở lời cầu nguyện. Nhờ một vạn cú đấm mỗi ngày trong nhiều năm, động tác chắp tay của Netero nhanh tới mức nhanh hơn cả phản xạ của Vua.

<short pause> Và mỗi tư thế tay lại ứng với một đòn khác nhau. Tay này là cú đập, tay kia là cú tát ngang, tay kia nữa là cú chụp. Vua không đoán được đòn tiếp theo.

<short pause> Vua bị đánh văng hết lần này tới lần khác. Hàng trăm, rồi hàng nghìn đòn. Một cỗ máy chiến đấu không có bất kỳ khe hở nào.

<short pause> Nhưng có một vấn đề. Mỗi đòn đều trúng, mà Vua gần như không bị thương. Lớp vỏ của Meruem quá cứng. Netero đang thắng trên điểm số, nhưng không thể hạ gục đối thủ.

<short pause> Kaku ghi vào sổ: hiệp 2 vẫn là của Netero, nhưng đồng hồ đang chạy ngược lại ông. Mỗi đòn đánh tiêu hao sức của một ông lão hơn trăm tuổi.
```

**ElevenLabs**

```text
Tới nơi, Meruem đưa ra một đề nghị: hai bên nói chuyện, không cần đánh. Vua muốn hiểu loài người, và muốn biết Netero có thể chấp nhận điều kiện gì.

[pause] Netero từ chối. Với ông, đây là nhiệm vụ: loài Kiến Chimera là mối đe dọa với loài người, và Vua phải bị ngăn lại.

[pause] Nhưng có một lý do sâu hơn. Netero đã già, và từ lâu ông không còn tìm được đối thủ xứng tầm. Đứng trước Vua, ông lại cảm thấy mình là kẻ thách đấu.

[pause] Meruem đưa ra một điều kiện: nếu Netero đánh trúng được Vua một lần, Vua sẽ nghe ông. Vua tự tin tới mức cho đối thủ ra đòn trước.

[pause] Netero nhận lời ngay. Với một võ sĩ, được ra đòn trước là món quà lớn nhất mà đối thủ có thể tặng.

[pause] [chuckles] Kaku để ý: đây là sai lầm chiến thuật đầu tiên của Vua. Coi thường đối thủ không phải là kiêu ngạo, mà là chưa có đủ dữ liệu. Và Vua sắp có rất nhiều dữ liệu.

[pause] Netero chắp tay. Pho tượng Quan Âm hiện ra sau lưng ông, và bàn tay khổng lồ giáng xuống trước khi Vua kịp nhìn thấy.

[pause] Bí mật nằm ở lời cầu nguyện. Nhờ một vạn cú đấm mỗi ngày trong nhiều năm, động tác chắp tay của Netero nhanh tới mức nhanh hơn cả phản xạ của Vua.

[pause] Và mỗi tư thế tay lại ứng với một đòn khác nhau. Tay này là cú đập, tay kia là cú tát ngang, tay kia nữa là cú chụp. Vua không đoán được đòn tiếp theo.

[pause] Vua bị đánh văng hết lần này tới lần khác. Hàng trăm, rồi hàng nghìn đòn. Một cỗ máy chiến đấu không có bất kỳ khe hở nào.

[pause] Nhưng có một vấn đề. Mỗi đòn đều trúng, mà Vua gần như không bị thương. Lớp vỏ của Meruem quá cứng. Netero đang thắng trên điểm số, nhưng không thể hạ gục đối thủ.

[pause] Kaku ghi vào sổ: hiệp 2 vẫn là của Netero, nhưng đồng hồ đang chạy ngược lại ông. Mỗi đòn đánh tiêu hao sức của một ông lão hơn trăm tuổi.
```

### c04 · Hiệp 3: Vua học / Hiệp 4: Linh Thủ, lòng bàn tay số không

Khoảng 127 giây · cảnh s35–s47 · 1652 ký tự

**Gemini**

```text
Trong lúc bị đánh, Meruem làm điều Vua giỏi nhất: quan sát. Đòn nào tới trước, tay nào theo sau, nhịp chắp tay dài bao lâu.

<short pause> Vua nhận ra một điều: mọi đòn của Quan Âm đều bắt đầu từ lời cầu nguyện. Nếu ngăn được Netero chắp tay, pho tượng không thể ra đòn.

<short pause> Cùng lúc, Netero bắt đầu chậm lại. Không nhiều, chỉ một chút. <short pause> Nhưng với một đối thủ như Vua, một chút là đủ.

<short pause> Và trong một khoảnh khắc, Vua hành động. Netero mất một chân, rồi mất một cánh tay. Kaku không đi vào chi tiết: điều quan trọng là, ông không còn chắp tay theo cách cũ được nữa.

<short pause> Nhưng Netero vẫn đứng đó, và vẫn mỉm cười. Còn Vua lại hỏi một câu lạ: Vua muốn biết tên của ông.

<short pause> <laugh> Kaku để ý: đây là lúc Vua thay đổi. Kẻ sinh ra để coi loài người là thức ăn, giờ muốn nhớ tên một con người. Những ván cờ với Komugi đang lên tiếng.

<short pause> Kaku ghi vào sổ: hiệp 3 là của Meruem. Vua tìm ra điểm yếu duy nhất của một kỹ thuật không có khe hở, và khai thác nó.

<short pause> Netero còn một con bài: đòn cuối cùng của Bách Thức Quan Âm, gọi là Linh Thủ, lòng bàn tay số không. Đòn này dồn toàn bộ Niệm còn lại vào một phát duy nhất.

<short pause> Pho tượng ôm lấy Vua, và bắn ra một luồng sáng khổng lồ. Cả khu vực rung chuyển, mặt đất bị xé toạc.

<short pause> Khi khói bụi tan, Netero không còn là ông lão khỏe mạnh lúc đầu. Dồn hết Niệm, cơ thể ông như già thêm chục năm trong một khoảnh khắc.

<short pause> Còn Vua? Vẫn đứng. Bị thương, nhưng đứng. Đòn mạnh nhất của người mạnh nhất loài người không đủ để hạ gục Vua Kiến.

<short pause> Kaku để ý: Linh Thủ không thất bại vì Netero yếu. Nó thất bại vì con số trên giấy từ đầu đã đúng. Về sức mạnh thuần túy, loài người không thể thắng.

<short pause> Kaku ghi vào sổ: hiệp 4 thuộc về Meruem. Và nếu trận đấu chỉ là sức mạnh, đây là lúc nó kết thúc.
```

**ElevenLabs**

```text
Trong lúc bị đánh, Meruem làm điều Vua giỏi nhất: quan sát. Đòn nào tới trước, tay nào theo sau, nhịp chắp tay dài bao lâu.

[pause] Vua nhận ra một điều: mọi đòn của Quan Âm đều bắt đầu từ lời cầu nguyện. Nếu ngăn được Netero chắp tay, pho tượng không thể ra đòn.

[pause] Cùng lúc, Netero bắt đầu chậm lại. Không nhiều, chỉ một chút. [pause] Nhưng với một đối thủ như Vua, một chút là đủ.

[pause] Và trong một khoảnh khắc, Vua hành động. Netero mất một chân, rồi mất một cánh tay. Kaku không đi vào chi tiết: điều quan trọng là, ông không còn chắp tay theo cách cũ được nữa.

[pause] Nhưng Netero vẫn đứng đó, và vẫn mỉm cười. Còn Vua lại hỏi một câu lạ: Vua muốn biết tên của ông.

[pause] [chuckles] Kaku để ý: đây là lúc Vua thay đổi. Kẻ sinh ra để coi loài người là thức ăn, giờ muốn nhớ tên một con người. Những ván cờ với Komugi đang lên tiếng.

[pause] Kaku ghi vào sổ: hiệp 3 là của Meruem. Vua tìm ra điểm yếu duy nhất của một kỹ thuật không có khe hở, và khai thác nó.

[pause] Netero còn một con bài: đòn cuối cùng của Bách Thức Quan Âm, gọi là Linh Thủ, lòng bàn tay số không. Đòn này dồn toàn bộ Niệm còn lại vào một phát duy nhất.

[pause] Pho tượng ôm lấy Vua, và bắn ra một luồng sáng khổng lồ. Cả khu vực rung chuyển, mặt đất bị xé toạc.

[pause] Khi khói bụi tan, Netero không còn là ông lão khỏe mạnh lúc đầu. Dồn hết Niệm, cơ thể ông như già thêm chục năm trong một khoảnh khắc.

[pause] [curious] Còn Vua? Vẫn đứng. Bị thương, nhưng đứng. Đòn mạnh nhất của người mạnh nhất loài người không đủ để hạ gục Vua Kiến.

[pause] Kaku để ý: Linh Thủ không thất bại vì Netero yếu. Nó thất bại vì con số trên giấy từ đầu đã đúng. Về sức mạnh thuần túy, loài người không thể thắng.

[pause] Kaku ghi vào sổ: hiệp 4 thuộc về Meruem. Và nếu trận đấu chỉ là sức mạnh, đây là lúc nó kết thúc.
```

### c05 · Hiệp 5: bông hồng của kẻ nghèo / Sau trận: người thắng thật sự

Khoảng 130 giây · cảnh s48–s60 · 1692 ký tự

**Gemini**

```text
Nhưng Netero đã tính trước điều này. Ngay từ đầu, ông biết mình có thể không thắng bằng võ công. Ông mang theo phương án cuối cùng.

<short pause> Trong cơ thể Netero có một quả bom thu nhỏ, tên là Bông Hồng Của Kẻ Nghèo. Nó được nối với nhịp tim của ông, và chỉ kích hoạt khi tim ông ngừng đập.

<short pause> Trước khi kích hoạt, Netero nói với Vua, đại ý: ngươi không hiểu gì về loài người cả. Ác ý của con người là không có đáy.

<short pause> Và theo lời người kể chuyện, đó là lần đầu tiên Meruem cảm thấy sợ hãi.

<short pause> Netero chọn hy sinh chính mình. Bông hồng nở ra thành một vụ nổ khổng lồ, hình dáng như một đóa hồng lửa trên sa mạc.

<short pause> Nhiều người đọc thấy quả bom này như một phép ẩn dụ cho vũ khí hủy diệt của loài người ngoài đời thật. Tác giả đặt nó vào tay người anh hùng, và điều đó khiến trận đấu trở nên rất khó chịu.

<short pause> Kaku ghi vào sổ: hiệp 5 là của Netero, nhưng không phải chiến thắng của ông. Đó là chiến thắng của thứ ông mang theo, thứ mà chính ông cũng không tự hào.

<short pause> Meruem sống sót qua vụ nổ. Cận vệ Hoàng gia tìm thấy và chữa trị cho Vua. <short pause> Nhưng bông hồng còn một thứ nữa: chất độc.

<short pause> Chất độc lan dần trong cơ thể Vua, và cả những ai ở gần. Không thuốc giải. Người thắng trận đấu, thật ra đã thua từ khoảnh khắc bông hồng nở.

<short pause> Biết mình sắp chết, Meruem chọn làm gì? Không trả thù, không chinh phục. Vua chỉ muốn quay lại chơi cờ với Komugi.

<short pause> Sau vụ nổ, Vua mới biết tên của chính mình, cái tên mà Nữ hoàng đã đặt trước khi qua đời: Meruem, nghĩa là ánh sáng soi rọi mọi thứ.

<short pause> Hai người chơi những ván cuối cùng trong một căn phòng yên tĩnh. Komugi biết mình cũng bị nhiễm độc, nhưng chọn ở lại.

<short pause> <laugh> Kaku không kể thêm. <short pause> Nhưng Kaku muốn bạn để ý: kẻ sinh ra để thay thế loài người, trong những giờ cuối, lại sống như một con người hơn ai hết.
```

**ElevenLabs**

```text
Nhưng Netero đã tính trước điều này. Ngay từ đầu, ông biết mình có thể không thắng bằng võ công. Ông mang theo phương án cuối cùng.

[pause] Trong cơ thể Netero có một quả bom thu nhỏ, tên là Bông Hồng Của Kẻ Nghèo. Nó được nối với nhịp tim của ông, và chỉ kích hoạt khi tim ông ngừng đập.

[pause] Trước khi kích hoạt, Netero nói với Vua, đại ý: ngươi không hiểu gì về loài người cả. Ác ý của con người là không có đáy.

[pause] Và theo lời người kể chuyện, đó là lần đầu tiên Meruem cảm thấy sợ hãi.

[pause] Netero chọn hy sinh chính mình. Bông hồng nở ra thành một vụ nổ khổng lồ, hình dáng như một đóa hồng lửa trên sa mạc.

[pause] Nhiều người đọc thấy quả bom này như một phép ẩn dụ cho vũ khí hủy diệt của loài người ngoài đời thật. Tác giả đặt nó vào tay người anh hùng, và điều đó khiến trận đấu trở nên rất khó chịu.

[pause] Kaku ghi vào sổ: hiệp 5 là của Netero, nhưng không phải chiến thắng của ông. Đó là chiến thắng của thứ ông mang theo, thứ mà chính ông cũng không tự hào.

[pause] Meruem sống sót qua vụ nổ. Cận vệ Hoàng gia tìm thấy và chữa trị cho Vua. [pause] Nhưng bông hồng còn một thứ nữa: chất độc.

[pause] Chất độc lan dần trong cơ thể Vua, và cả những ai ở gần. Không thuốc giải. Người thắng trận đấu, thật ra đã thua từ khoảnh khắc bông hồng nở.

[pause] [curious] Biết mình sắp chết, Meruem chọn làm gì? Không trả thù, không chinh phục. Vua chỉ muốn quay lại chơi cờ với Komugi.

[pause] Sau vụ nổ, Vua mới biết tên của chính mình, cái tên mà Nữ hoàng đã đặt trước khi qua đời: Meruem, nghĩa là ánh sáng soi rọi mọi thứ.

[pause] Hai người chơi những ván cuối cùng trong một căn phòng yên tĩnh. Komugi biết mình cũng bị nhiễm độc, nhưng chọn ở lại.

[pause] [chuckles] Kaku không kể thêm. [pause] Nhưng Kaku muốn bạn để ý: kẻ sinh ra để thay thế loài người, trong những giờ cuối, lại sống như một con người hơn ai hết.
```

### c06 · Vì sao trận này được nhớ mãi / Sơ đồ chiến thuật / Ba bài học chiến thuật

Khoảng 134 giây · cảnh s61–s73 · 1748 ký tự

**Gemini**

```text
Arc Kiến Chimera nổi tiếng với giọng người kể chuyện. Những suy nghĩ chỉ diễn ra trong vài giây được kể thành những đoạn dài, như thời gian bị kéo chậm lại.

<short pause> Trong trận này, người kể chuyện cho ta vào đầu cả hai bên. Ta biết Netero đang tính gì, và cũng biết Vua đang học gì. Không ai là phản diện đơn giản.

<short pause> Không có ai cổ vũ. Không có đồng đội xông vào giúp. Chỉ có hai bên, một vùng đất trống, và một câu hỏi: loài người có thể thắng thứ sinh ra để vượt qua mình không?

<short pause> Bản anime 2011 dựng trận này với nhiều khoảng lặng và lời kể, thay vì chỉ có tiếng đòn đánh. Chính khoảng lặng làm các đòn đánh nặng hơn.

<short pause> <laugh> Kaku để ý: một trận đấu hay không cần nhiều chiêu thức. Nó cần hai người có lý do thật để đứng đó, và một cái kết không ai muốn.

<short pause> Tổng kết bằng một trang. Hiệp 0: Netero tách Vua ra một mình. Hiệp 1: Vua coi thường đối thủ và cho ra đòn trước.

<short pause> Hiệp 2: Quan Âm áp đảo nhưng không gây sát thương thật. Hiệp 3: Vua tìm ra điểm yếu, lời cầu nguyện.

<short pause> Hiệp 4: Linh Thủ dồn hết sức nhưng thất bại. Hiệp 5: bông hồng, phương án được chuẩn bị từ trước khi trận đấu bắt đầu.

<short pause> Và mũi tên quan trọng nhất trên sơ đồ không nằm trong trận đấu. Nó nối từ bàn cờ Gungi tới câu hỏi tên của Vua.

<short pause> Bài học một: chọn chiến trường. Netero thắng hiệp đầu tiên trước khi tung ra cú đấm nào, chỉ bằng việc đưa Vua ra khỏi cung điện.

<short pause> Bài học hai: kỹ thuật không có khe hở vẫn có điểm bắt đầu. Quan Âm không có lỗ hổng trong đòn đánh, nhưng lời cầu nguyện là cái cổng mà mọi đòn phải đi qua.

<short pause> Bài học ba: phương án cuối cùng luôn có cái giá. Bông hồng thắng được Vua, nhưng cái giá là mạng sống của Netero, và cả những người vô tội bị nhiễm độc.

<short pause> Và thêm một bài học không phải chiến thuật: đôi khi, thứ thay đổi một trận đấu lớn nhất lại đến từ một ván cờ nhỏ, cách xa chiến trường.
```

**ElevenLabs**

```text
Arc Kiến Chimera nổi tiếng với giọng người kể chuyện. Những suy nghĩ chỉ diễn ra trong vài giây được kể thành những đoạn dài, như thời gian bị kéo chậm lại.

[pause] Trong trận này, người kể chuyện cho ta vào đầu cả hai bên. Ta biết Netero đang tính gì, và cũng biết Vua đang học gì. Không ai là phản diện đơn giản.

[pause] Không có ai cổ vũ. Không có đồng đội xông vào giúp. [curious] Chỉ có hai bên, một vùng đất trống, và một câu hỏi: loài người có thể thắng thứ sinh ra để vượt qua mình không?

[pause] Bản anime 2011 dựng trận này với nhiều khoảng lặng và lời kể, thay vì chỉ có tiếng đòn đánh. Chính khoảng lặng làm các đòn đánh nặng hơn.

[pause] [chuckles] Kaku để ý: một trận đấu hay không cần nhiều chiêu thức. Nó cần hai người có lý do thật để đứng đó, và một cái kết không ai muốn.

[pause] Tổng kết bằng một trang. Hiệp 0: Netero tách Vua ra một mình. Hiệp 1: Vua coi thường đối thủ và cho ra đòn trước.

[pause] Hiệp 2: Quan Âm áp đảo nhưng không gây sát thương thật. Hiệp 3: Vua tìm ra điểm yếu, lời cầu nguyện.

[pause] Hiệp 4: Linh Thủ dồn hết sức nhưng thất bại. Hiệp 5: bông hồng, phương án được chuẩn bị từ trước khi trận đấu bắt đầu.

[pause] Và mũi tên quan trọng nhất trên sơ đồ không nằm trong trận đấu. Nó nối từ bàn cờ Gungi tới câu hỏi tên của Vua.

[pause] Bài học một: chọn chiến trường. Netero thắng hiệp đầu tiên trước khi tung ra cú đấm nào, chỉ bằng việc đưa Vua ra khỏi cung điện.

[pause] Bài học hai: kỹ thuật không có khe hở vẫn có điểm bắt đầu. Quan Âm không có lỗ hổng trong đòn đánh, nhưng lời cầu nguyện là cái cổng mà mọi đòn phải đi qua.

[pause] Bài học ba: phương án cuối cùng luôn có cái giá. Bông hồng thắng được Vua, nhưng cái giá là mạng sống của Netero, và cả những người vô tội bị nhiễm độc.

[pause] Và thêm một bài học không phải chiến thuật: đôi khi, thứ thay đổi một trận đấu lớn nhất lại đến từ một ván cờ nhỏ, cách xa chiến trường.
```

### c07 · Nếu Netero trẻ hơn năm mươi tuổi? / Góc nhìn của Kaku / Kết

Khoảng 119 giây · cảnh s74–s84 · 1543 ký tự

**Gemini**

```text
Có một câu hỏi fan tranh luận mãi: nếu Netero đấu Vua ở thời sung sức nhất, ông có thắng không?

<short pause> Phe nói có cho rằng lúc sung sức, ông nhanh hơn, bền hơn, và đủ sức giữ nhịp Quan Âm lâu hơn, đủ để Vua không kịp học.

<short pause> Phe nói không thì chỉ ra: vấn đề chưa bao giờ là tốc độ. Hàng nghìn đòn trúng mà Vua gần như không bị thương. Nhanh hơn cũng không phá được lớp vỏ ấy.

<short pause> <laugh> Kaku nghiêng về một ý khác: câu hỏi ấy có lẽ không quan trọng với tác giả. Trận đấu được viết để cho thấy võ công của một người, dù đỉnh cao tới đâu, cũng có giới hạn.

<short pause> Kaku nghĩ trận này hay không phải vì đòn đánh đẹp. Nó hay vì cả hai đều thay đổi trong lúc đánh. Netero bắt đầu như một võ sĩ, và kết thúc như một vũ khí.

<short pause> Còn Meruem bắt đầu như một vị vua coi loài người là thức ăn, và kết thúc như một người chỉ muốn chơi thêm một ván cờ.

<short pause> Câu hỏi Kaku muốn để lại: ai là con người hơn trong trận này? Người đã mang theo bông hồng, hay kẻ đã hỏi tên đối thủ?

<short pause> Kaku không có câu trả lời. Hãy viết câu trả lời của bạn vào bình luận. Kaku đọc hết.

<short pause> Một vạn cú đấm mỗi ngày. Một lời cầu nguyện nhanh hơn phản xạ của Vua. Và một bông hồng mà chính người mang nó cũng muốn quên. Trận Netero đấu Meruem là câu chuyện về sức mạnh, và về cái giá của việc phải thắng bằng mọi giá.

<short pause> Video tiếp theo, Kaku đổi hẳn không khí: Blue Lock, và bảng xếp hạng vũ khí của các tiền đạo. Ai có vũ khí đáng sợ nhất trong khung thành?

<short pause> Nếu bạn thích xem Kaku mổ xẻ từng hiệp đấu, hãy đăng ký kênh. Và lần tới bạn chắp tay cảm ơn một điều gì đó, hãy nhớ tới ông lão với một vạn cú đấm. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Có một câu hỏi fan tranh luận mãi: nếu Netero đấu Vua ở thời sung sức nhất, ông có thắng không?

[pause] Phe nói có cho rằng lúc sung sức, ông nhanh hơn, bền hơn, và đủ sức giữ nhịp Quan Âm lâu hơn, đủ để Vua không kịp học.

[pause] Phe nói không thì chỉ ra: vấn đề chưa bao giờ là tốc độ. Hàng nghìn đòn trúng mà Vua gần như không bị thương. Nhanh hơn cũng không phá được lớp vỏ ấy.

[pause] [chuckles] Kaku nghiêng về một ý khác: câu hỏi ấy có lẽ không quan trọng với tác giả. Trận đấu được viết để cho thấy võ công của một người, dù đỉnh cao tới đâu, cũng có giới hạn.

[pause] Kaku nghĩ trận này hay không phải vì đòn đánh đẹp. Nó hay vì cả hai đều thay đổi trong lúc đánh. Netero bắt đầu như một võ sĩ, và kết thúc như một vũ khí.

[pause] Còn Meruem bắt đầu như một vị vua coi loài người là thức ăn, và kết thúc như một người chỉ muốn chơi thêm một ván cờ.

[pause] Câu hỏi Kaku muốn để lại: ai là con người hơn trong trận này? Người đã mang theo bông hồng, hay kẻ đã hỏi tên đối thủ?

[pause] Kaku không có câu trả lời. Hãy viết câu trả lời của bạn vào bình luận. Kaku đọc hết.

[pause] Một vạn cú đấm mỗi ngày. Một lời cầu nguyện nhanh hơn phản xạ của Vua. Và một bông hồng mà chính người mang nó cũng muốn quên. Trận Netero đấu Meruem là câu chuyện về sức mạnh, và về cái giá của việc phải thắng bằng mọi giá.

[pause] Video tiếp theo, Kaku đổi hẳn không khí: Blue Lock, và bảng xếp hạng vũ khí của các tiền đạo. Ai có vũ khí đáng sợ nhất trong khung thành?

[pause] Nếu bạn thích xem Kaku mổ xẻ từng hiệp đấu, hãy đăng ký kênh. Và lần tới bạn chắp tay cảm ơn một điều gì đó, hãy nhớ tới ông lão với một vạn cú đấm. Kaku gấp sổ đây, hẹn gặp lại!
```
