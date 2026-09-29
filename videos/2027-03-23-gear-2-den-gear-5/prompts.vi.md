# Bộ prompt · One Piece: Từ Gear 2 tới Gear 5 — bậc thang sức mạnh của Luffy

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 88 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Cảnh báo spoiler: video này đi tới Gear 5 và arc Egghead của manga One Piece. Nếu bạn đang xem bản làm lại từ…

```text
Wide 16:9 landscape cinematic frame. an old wooden ship's logbook closed on a deck beside a spoiler warning card, close-up, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một cơ thể cao su. Nghe thì buồn cười. Bị đấm không đau, bị bắn đạn nảy ngược lại. Nhưng làm sao một cơ thể c…

```text
Wide 16:9 landscape cinematic frame. a rubbery arm stretching absurdly long across a harbor to grab a distant ship's mast, humorous wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Câu trả lời của Luffy là các Gear, tức các cấp số. Giống như sang số trên xe: mỗi cấp nhanh hơn, mạnh hơn, và…

```text
Wide 16:9 landscape cinematic frame. a vintage car gearshift lever with numbered positions glowing one after another, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku leo bậc thang Gear của Luffy: từ Gear 2 tới Gear 5. Mỗi nấc có điều…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at the bottom of a staircase with glowing numbered steps, rolling up its sleeves. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và Kaku nhắc trước: Luffy không có sức mạnh nào miễn phí. Mỗi Gear đều được sinh ra từ một trận thua, hoặc mộ…

```text
Wide 16:9 landscape cinematic frame. a torn flag with a simple smiling face emblem fluttering in the wind over a battered ship, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Nấc 0: cơ thể cao su

Lời: Nấc đầu tiên là Gear 1, tức Luffy bình thường, sau khi ăn trái Gomu Gomu. Cơ thể co giãn, kéo dài tay chân để…

```text
Wide 16:9 landscape cinematic frame. a stretched rubbery fist flying forward with a long arm trailing behind it, dynamic close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Điểm mạnh: miễn nhiễm với đòn đánh cùn và điện, vì cao su không dẫn điện. Luffy từng thắng Enel, kẻ tự xưng l…

```text
Wide 16:9 landscape cinematic frame. a bolt of lightning striking a rubbery silhouette and bouncing off harmlessly, dynamic wide shot, bright electric light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Điểm yếu: dao kiếm vẫn cắt được, và như mọi người ăn trái ác quỷ, Luffy không biết bơi.

```text
Wide 16:9 landscape cinematic frame. a figure sinking slowly into deep blue water with a limp hand reaching upward, close-up, cold underwater light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Điều kiện: ăn trái ác quỷ. Cái giá: mất khả năng bơi, với một người muốn làm Vua Hải Tặc.

```text
Wide 16:9 landscape cinematic frame. a small index card with three lines: condition, power, cost, each with a tiny doodle, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Luffy ăn trái ác quỷ khi còn nhỏ, vì tưởng đó chỉ là một món ăn lạ. Một sức mạnh định mệnh bắt đầu từ một lần…

```text
Wide 16:9 landscape cinematic frame. a small bowl holding a strange swirled fruit on a tavern counter, a child's hand sneaking toward it, humorous close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Kaku để ý: cơ thể cao su của Luffy lúc đầu chỉ là một cơ thể bị động, chịu đòn tốt. Mọi Gear về sau là cách c…

```text
Wide 16:9 landscape cinematic frame. a rubber band stretched between two fingers about to be released, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Nấc 1: Gear 2

Lời: Hoàn cảnh ra đời: trước arc Enies Lobby, Luffy thua thảm một kẻ thù rất nhanh. Cậu nhận ra mình cần tốc độ và…

```text
Wide 16:9 landscape cinematic frame. a battered figure lying on the ground in the rain looking up at a distant silhouette walking away, wide shot, grey somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Cách hoạt động: Luffy dùng cơ thể cao su để bơm máu đi khắp người nhanh hơn bình thường, như một cái bơm. Cơ…

```text
Wide 16:9 landscape cinematic frame. a figure crouching low with steam rising from their skin in a stone courtyard, dramatic close-up, warm red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Lần đầu xuất hiện ở chương 387, trong arc Enies Lobby. Tốc độ và sức mạnh tăng vọt, tới mức đối thủ không kịp…

```text
Wide 16:9 landscape cinematic frame. a blur of motion streaking across a courtyard with a trail of steam, dynamic wide shot, bright dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Cái giá: cơ thể chịu áp lực cực lớn. Trong truyện, có người cảnh báo rằng nó có thể làm hao mòn cơ thể, và Lu…

```text
Wide 16:9 landscape cinematic frame. a figure kneeling and breathing heavily with faint steam fading from their shoulders, medium shot, exhausted grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Luffy nói với đối thủ, đại ý, rằng cậu cần sức mạnh này để không để mất bất kỳ người bạn nào. Gear 2 là lời h…

```text
Wide 16:9 landscape cinematic frame. a hand clenched into a fist beside a small torn piece of a crew flag, extreme close-up, determined warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Nấc 2: Gear 3

Lời: Cách hoạt động: Luffy thổi hơi vào xương của mình. Vì xương cũng là cao su, tay hoặc chân phồng lên khổng lồ…

```text
Wide 16:9 landscape cinematic frame. a figure biting their thumb and blowing into it as their arm swells to enormous size, humorous dynamic close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Sức mạnh: một cú đấm khổng lồ, có sức nặng và sức tàn phá của một vật cực lớn. Đủ để phá tường thành hay đánh…

```text
Wide 16:9 landscape cinematic frame. a gigantic inflated fist smashing into a stone fortress wall and cracking it apart, dramatic wide shot, dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Cái giá lúc đầu rất buồn cười: sau khi xả hơi, Luffy bị teo nhỏ lại như một đứa bé tí hon trong một lúc.

```text
Wide 16:9 landscape cinematic frame. a tiny figure standing on a stone ledge looking up in surprise at normal-sized companions, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Gear 2 là tốc độ, Gear 3 là khối lượng. Luffy bắt đầu kết hợp chúng: đánh nhanh bằng Gear 2, kết thúc bằng Ge…

```text
Wide 16:9 landscape cinematic frame. a diagram on parchment with a lightning bolt icon and a heavy weight icon connected by a plus sign, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: cả Gear 2 lẫn Gear 3 đều ra đời trong cùng một arc, để giải cứu Robin. Luffy phát minh cả hai chỉ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny inflated balloon in one wing and a steaming kettle in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Tên đòn: nhật ký sức mạnh

Lời: Luffy có một thói quen: hô tên đòn trước khi đánh. Cú đấm cơ bản gọi là Pistol, tức súng lục. Cú đá quét gọi…

```text
Wide 16:9 landscape cinematic frame. a notebook page of hand-drawn attack names with small doodles of a pistol and a whip beside each, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Khi lên Gear 2, tên đòn có thêm chữ Jet, tức phản lực: Jet Pistol, Jet Bazooka. Đòn nhanh tới mức nắm tay đến…

```text
Wide 16:9 landscape cinematic frame. a fist leaving a long vapor trail like a jet engine, dynamic extreme close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Khi lên Gear 3, tên đòn có thêm chữ Gigant, tức khổng lồ. Sang Gear 4, tên đòn mượn tên thú lớn: Kong, Leo là…

```text
Wide 16:9 landscape cinematic frame. a row of hand-drawn animal silhouettes, a great ape, a lion, a rhino and a cobra, parchment close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: tên đòn chính là cuốn nhật ký sức mạnh của Luffy. Chỉ cần nghe tiếng hô, người đọc biết ngay cậu đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a notebook with labels written in bigger and bigger letters down the page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Gear 2 và 3 trên đường đi

Lời: Sau Enies Lobby, Gear 2 và Gear 3 trở thành vũ khí chính của Luffy trước những kẻ thù lớn hơn cậu rất nhiều,…

```text
Wide 16:9 landscape cinematic frame. a small figure facing a towering shadowy giant in a misty graveyard island, dramatic wide shot, eerie moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Nhưng ở quần đảo Sabaody, cả băng gặp một Đô đốc Hải quân. Gear 2 và 3 gần như vô dụng: đối thủ quá nhanh, qu…

```text
Wide 16:9 landscape cinematic frame. small silhouettes scattered by a blinding beam of light across a grove of giant mangrove trees, dramatic wide shot, harsh bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Ở Marineford, Luffy dùng Gear 2 và 3 liên tục để lao tới cứu anh trai. Cơ thể cậu bị đẩy quá giới hạn, và dù…

```text
Wide 16:9 landscape cinematic frame. a lone figure charging across a frozen battlefield toward a distant execution platform, steam trailing behind, wide shot, harsh cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là lúc Luffy hiểu rằng thêm một cấp số nữa là không đủ. Cậu không cần sang số nhanh hơn, cậu c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering under the hood of a tiny old car with a worried face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Hai năm luyện tập và Haki

Lời: Sau cuộc chiến Marineford và cái chết của Ace, Luffy thua đau nhất đời. Cậu chọn tạm dừng hai năm để luyện tậ…

```text
Wide 16:9 landscape cinematic frame. a lone figure sitting on a rocky shore at dusk staring at the sea, a single broken bead necklace in hand, back view, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Cậu học Haki từ Rayleigh, cánh tay phải của Vua Hải Tặc. Haki vũ trang cho phép phủ một lớp năng lượng cứng n…

```text
Wide 16:9 landscape cinematic frame. a forearm coated in a dark glossy sheen like polished steel on a jungle training ground, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Haki là chìa khóa mở ra Gear 4. Nó giải quyết một vấn đề cũ: cao su mềm thì khó gây sát thương thật cho kẻ mạ…

```text
Wide 16:9 landscape cinematic frame. a soft rubber ball beside a steel-coated ball on a table, both on scale pans, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Luffy được dạy về cả ba loại Haki: vũ trang để phủ giáp, quan sát để cảm nhận đối thủ, và bá vương, loại Haki…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols on parchment, a shield, an eye and a crown, arranged in a triangle, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Luffy luyện tập hai năm trên một hòn đảo đầy thú dữ. Khi trở lại, cậu mạnh hơn hẳn, nhưng vẫn giữ Gear 4 như…

```text
Wide 16:9 landscape cinematic frame. a wild jungle island with enormous beasts silhouetted against the sunrise, wide shot, adventurous golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Nấc 3: Gear 4

Lời: Gear 4 lần đầu xuất hiện ở chương 784, trong trận với Doflamingo ở Dressrosa. Luffy thổi phồng cơ bắp, rồi ph…

```text
Wide 16:9 landscape cinematic frame. a massively bulked silhouette with dark hardened arms bouncing in midair above a ruined city, dramatic low-angle shot, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Dạng đầu tiên là Boundman: cơ thể nảy liên tục như quả bóng, và những cú đấm nén lại rồi bật ra với lực khủng…

```text
Wide 16:9 landscape cinematic frame. a figure bouncing rhythmically in place with a shockwave ring under their feet, dynamic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Về sau có thêm Tankman, một cơ thể phình to để hấp thụ đòn đánh, và Snakeman, thon gọn hơn, với những cú đấm…

```text
Wide 16:9 landscape cinematic frame. two contrasting silhouettes side by side, one wide and round, one lean with sinuous arm trails, parchment illustration style, dramatic light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Cái giá của Gear 4 rất rõ ràng: nó chỉ kéo dài một thời gian ngắn. Khi hết, Luffy không dùng được Haki trong…

```text
Wide 16:9 landscape cinematic frame. a large clock with ten minutes shaded in red beside an exhausted figure sitting on the ground, close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Để vào Gear 4, Luffy cắn vào cánh tay và thổi phồng cơ bắp giống cách làm Gear 3, nhưng lần này là cả thân tr…

```text
Wide 16:9 landscape cinematic frame. a figure biting their forearm as their upper body swells and darkens with a glossy steel-like sheen, dramatic close-up, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Gear 4 là lần đầu tiên Luffy kết hợp trái ác quỷ với một kỹ năng học được. Sức mạnh không còn chỉ là bẩm sinh…

```text
Wide 16:9 landscape cinematic frame. a pair of hands with rubber-band stretch lines on one and steel coating on the other, clasped together, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Gear 4 trong thực chiến

Lời: Ở Dressrosa, Boundman đủ sức áp đảo Doflamingo. Nhưng khi hết thời gian, Luffy nằm bất động, và cả hòn đảo ph…

```text
Wide 16:9 landscape cinematic frame. citizens of a ruined city forming a desperate barrier around a motionless figure lying on the ground, wide shot, tense dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Ở Whole Cake Island, Luffy gặp một đối thủ tạo ra vô số lính bánh quy. Cậu ăn chúng tới mức bụng căng tròn, r…

```text
Wide 16:9 landscape cinematic frame. a comically round bloated silhouette sitting among crumbled biscuit soldiers, humorous wide shot, warm bakery light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Tankman hấp thụ đòn đánh bằng cơ thể phình to, rồi dồn toàn bộ lực bắn ngược lại. Đây là dạng thiên về phòng…

```text
Wide 16:9 landscape cinematic frame. a huge round belly compressing under a heavy blow and about to launch it back, dynamic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Rồi tới đối thủ khó nhất arc: một chỉ huy có thể nhìn thấy tương lai gần bằng Haki quan sát. Mọi cú đấm của L…

```text
Wide 16:9 landscape cinematic frame. a calm tall silhouette in a mirrored room sidestepping a fist, eyes glowing faintly, dramatic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Snakeman ra đời ở chương 894 để giải bài toán ấy: nắm tay lượn vòng, đổi hướng giữa chừng, nhanh tới mức dù đ…

```text
Wide 16:9 landscape cinematic frame. a fist trailing a long winding path like a snake around mirrored pillars, dynamic wide shot, dark dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Và trong trận ấy, Luffy tự học được cách nhìn thấy tương lai, giống đối thủ. Kaku để ý: đối thủ mạnh nhất lại…

```text
Wide 16:9 landscape cinematic frame. a figure with closed eyes sensing faint ghostly outlines of upcoming movements in the air, close-up, mystical blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Wano: Haki cấp cao

Lời: Ở Wano, Luffy bị Kaido hạ chỉ bằng một đòn, dù đang ở Gear 4. Cậu bị ném vào một nhà tù khai thác mỏ.

```text
Wide 16:9 landscape cinematic frame. a figure in shackles pushing a heavy cart inside a dim mining prison, wide shot, grim torchlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ở đó, một ông lão tù nhân dạy cậu một cách dùng Haki vũ trang mới: đẩy lực vào bên trong đối thủ thay vì chỉ…

```text
Wide 16:9 landscape cinematic frame. an elderly figure demonstrating a palm strike that sends a ripple through a stone wall without touching it, dramatic close-up, dim prison light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Rồi trong trận quyết chiến, Luffy học được cách phủ Haki bá vương lên đòn đánh. Chỉ những kẻ mạnh nhất thế gi…

```text
Wide 16:9 landscape cinematic frame. two clashing fists crackling with black and red lightning above a castle roof, dramatic close-up, intense stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: trước khi thức tỉnh Gear 5, Luffy đã chạm tới đỉnh Haki. Gear 5 không đến với một người yếu, mà đế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing an arrow that climbs to the top of a mountain marked with a small flame. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Bí mật của trái ác quỷ

Lời: Rồi tới Wano. Trong trận với Kaido, Luffy thua, ngã xuống, và tim cậu gần như ngừng đập.

```text
Wide 16:9 landscape cinematic frame. a figure falling from a great height through storm clouds over a mountainous land, wide shot, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Và ở chương 1044, sự thật được tiết lộ: trái của Luffy không phải trái cao su. Tên thật của nó là Hito Hito n…

```text
Wide 16:9 landscape cinematic frame. an ancient stone mural of a laughing sun deity with swirling clouds, close-up, radiant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Chính phủ Thế giới đã đổi tên trái này suốt nhiều thế kỷ để giấu nó. Và trái Zoan có ý chí riêng: nó đã chọn…

```text
Wide 16:9 landscape cinematic frame. a thick government ledger with an entry scratched out and a faint sun symbol glowing through, extreme close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Luffy thức tỉnh trái ác quỷ. Và điều đầu tiên cậu làm, là cười.

```text
Wide 16:9 landscape cinematic frame. a silhouette rising from rubble with head thrown back in joyful laughter as a drumbeat ripples through the air, dramatic wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Kaku đã nói về chi tiết này trong video mười hiểu lầm One Piece. Hôm nay ta nhìn nó như nấc cuối c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at the top step of a staircase that glows brightly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Nấc 4: Gear 5

Lời: Gear 5 là trạng thái thức tỉnh. Cơ thể Luffy trở nên tự do như trong phim hoạt hình: mắt trố ra, cơ thể biến…

```text
Wide 16:9 landscape cinematic frame. a whimsical silhouette stretching a whole landscape like rubber, with ground and clouds bending around it, cartoonish dynamic wide shot, bright white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Luffy túm lấy tia sét. Kéo mặt đất như kéo một tấm vải. Và biến những đòn đánh nghiêm túc nhất thành những tr…

```text
Wide 16:9 landscape cinematic frame. a hand grabbing a lightning bolt like a rope and swinging it, humorous dynamic close-up, bright electric light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Tính cách của Nika là tiếng cười và sự giải phóng. Và Gear 5 là sức mạnh chỉ bị giới hạn bởi trí tưởng tượng…

```text
Wide 16:9 landscape cinematic frame. a joyful figure dancing on clouds with musical notes and drum icons floating around, symbolic wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cái giá: Gear 5 tiêu hao sức lực khủng khiếp. Sau khi dùng, Luffy kiệt sức tới mức cơ thể teo lại, trông như…

```text
Wide 16:9 landscape cinematic frame. a frail exhausted figure sitting slumped against a rock while companions rush toward them, wide shot, dim tired light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Với Gear 5, Luffy kết thúc trận chiến với Kaido và giải phóng Wano. Nhịp tim của cậu vang lên như tiếng trống…

```text
Wide 16:9 landscape cinematic frame. a giant drum beating in the sky over a mountainous land at dawn, symbolic wide shot, radiant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nhưng ở Egghead, ta thấy Gear 5 có giới hạn thời gian. Khi hết, Luffy phải nghỉ để hồi sức, đôi khi vào đúng…

```text
Wide 16:9 landscape cinematic frame. an hourglass running out on a futuristic laboratory island, close-up, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nghĩa là dù ở nấc cao nhất, luật cũ vẫn đúng: không có sức mạnh nào miễn phí. Gear 5 chỉ đẩy cái giá lên cao…

```text
Wide 16:9 landscape cinematic frame. a price tag with a sun symbol hanging from a golden key, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Kaku để ý: Gear 5 là nấc duy nhất không đến từ việc luyện tập hay một trận thua. Nó đến từ việc chính trái ác…

```text
Wide 16:9 landscape cinematic frame. a golden key floating down into an open hand from a bright sky, symbolic close-up, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Điều kiện và cái giá của từng nấc

Lời: Tổng kết điều kiện và cái giá. Gear 1: ăn trái ác quỷ, đổi lại mất khả năng bơi.

```text
Wide 16:9 landscape cinematic frame. a ladder drawn on parchment with the first step labeled with a fruit icon and a wave icon crossed out, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Gear 2: một trận thua và nhu cầu tốc độ; đổi lại áp lực lớn lên cơ thể. Gear 3: sự sáng tạo với xương cao su;…

```text
Wide 16:9 landscape cinematic frame. the next two steps of the ladder labeled with a steam icon and a balloon icon, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Gear 4: hai năm luyện Haki; đổi lại mười phút không Haki. Gear 5: được trái ác quỷ thức tỉnh; đổi lại kiệt sứ…

```text
Wide 16:9 landscape cinematic frame. the top steps of the ladder labeled with a steel fist icon and a sun icon, amber ink close-up, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nếu vẽ thành biểu đồ, sức mạnh đi lên như bậc thang, còn cái giá đi lên theo cùng một nhịp. Không nấc nào đượ…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn chart with two lines climbing side by side like stairs, one gold and one red, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Và có một điều không đổi ở mọi nấc: mỗi lần Luffy lên một Gear mới, đều là vì một người bạn đang gặp nguy hiể…

```text
Wide 16:9 landscape cinematic frame. a small group of silhouettes standing behind a figure on each step of the ladder, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Ba quy luật của bậc thang · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại toàn bộ, Kaku thấy bậc thang Gear tuân theo ba quy luật.

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a big number three on a chalkboard with a flourish. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Quy luật một: mỗi nấc sửa một điểm yếu của nấc trước. Gear 1 thiếu tốc độ, Gear 2 thêm tốc độ. Gear 2 thiếu s…

```text
Wide 16:9 landscape cinematic frame. a chain of linked boxes on parchment, each with an arrow pointing at a crossed-out weakness, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Gear 3 chậm và để lộ sơ hở, Gear 4 gộp cả tốc độ lẫn sức nặng. Gear 4 bị kẻ mạnh hơn đè bẹp, Gear 5 phá luôn…

```text
Wide 16:9 landscape cinematic frame. the last links of the chain glowing brighter, the final link shaped like a sun, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Quy luật hai: cái giá tăng theo sức mạnh. Từ vài hơi thở gấp, tới teo nhỏ, tới mười phút mất Haki, rồi tới ki…

```text
Wide 16:9 landscape cinematic frame. a staircase of iron weights getting heavier on each step, symbolic close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Quy luật ba: mỗi nấc là câu trả lời cho những con người cụ thể. Robin ở Enies Lobby. Nỗi đau mất Ace sau Mari…

```text
Wide 16:9 landscape cinematic frame. three small symbolic objects on a table, a book, a bead necklace and a cherry blossom branch, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kaku nghĩ đó là lý do bậc thang này hấp dẫn: nó không chỉ là danh sách sức mạnh, mà là một cuốn tiểu sử viết…

```text
Wide 16:9 landscape cinematic frame. an open biography book whose pages show small fight silhouettes instead of text, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Vì sao Gear 5 gây tranh cãi

Lời: Khi Gear 5 lên anime, người xem chia làm hai phe. Một phe thấy hụt hẫng: trận đấu nghiêm túc nhất bỗng hóa th…

```text
Wide 16:9 landscape cinematic frame. a split crowd of tiny silhouettes, half frowning with crossed arms, half cheering, symbolic wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Phe kia cho rằng Gear 5 đã được cài từ đầu: Luffy luôn là nhân vật cười nhiều nhất, và giấc mơ của cậu là đượ…

```text
Wide 16:9 landscape cinematic frame. an old sketchbook opened to an early page showing a small laughing face drawn in simple lines, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nhiều người còn để ý: ngay từ những chương đầu, Luffy vốn đã co giãn như nhân vật hoạt hình cổ điển. Gear 5 c…

```text
Wide 16:9 landscape cinematic frame. a vintage black and white cartoon style doodle of a bouncing rubbery figure on old film strip, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku không đứng về phe nào. Nhưng một sức mạnh khiến người xem cãi nhau tới vậy chắc chắn là một sức mạnh đán…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a fence between two groups, shrugging with a smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Góc nhìn của Kaku

Lời: Kaku nghĩ bậc thang Gear kể câu chuyện về cách Luffy lớn lên. Gear 2 và 3: một cậu thiếu niên liều mình vì bạ…

```text
Wide 16:9 landscape cinematic frame. three portraits of the same silhouette at different ages hanging side by side on a ship's cabin wall, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Và Gear 5: một người trở thành biểu tượng tự do cho người khác. Không còn là sức mạnh của một cá nhân, mà là…

```text
Wide 16:9 landscape cinematic frame. a crowd of people in a dark town looking up at a bright laughing silhouette on a rooftop, wide shot, hopeful radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và thú vị nhất: nấc mạnh nhất lại là nấc vui nhộn nhất. One Piece nói rằng sức mạnh thật không đến từ sự nghi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot doing a silly stretchy dance with a big grin. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Trò chơi: bạn muốn Gear nào?

Lời: Nếu bạn có cơ thể cao su, bạn muốn dùng Gear nào trong đời thường? Gear 2 để chạy kịp xe buýt? Gear 3 để với…

```text
Wide 16:9 landscape cinematic frame. a humorous doodle of a figure stretching an arm to reach a high kitchen shelf while steam rises from another figure running to a bus, parchment close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hay Gear 4 Tankman để ăn hết một bàn buffet mà không thấy no? Còn Gear 5, bạn sẽ biến thứ gì quanh mình thành…

```text
Wide 16:9 landscape cinematic frame. a humorous doodle of a round bloated figure beside an empty buffet table, parchment close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn Gear 5, nhưng chỉ để biến bàn học thành cao su, cho cú ngã từ ghế đỡ đau. Viết lựa chọn của bạn vào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bouncing happily on a rubbery desk that bends like a trampoline. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Kết

Lời: Từ một cơ thể cao su bị coi là trò đùa, tới một vị thần của tiếng cười. Bậc thang Gear của Luffy là bậc thang…

```text
Wide 16:9 landscape cinematic frame. a long stretching arm reaching toward a sunrise over the ocean from the deck of a small ship, wide shot, radiant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và bậc thang ấy chưa kết thúc. Manga vẫn đang tiếp tục, và biết đâu Luffy còn một nấc nữa mà chưa ai đoán đượ…

```text
Wide 16:9 landscape cinematic frame. a staircase continuing upward into bright clouds beyond the last visible step, symbolic wide shot, radiant hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Video tiếp theo, Kaku phân tích một trận đấu kinh điển: Hunter x Hunter, Netero đấu với vua kiến Meruem. Một…

```text
Wide 16:9 landscape cinematic frame. a quiet desert at dusk with two silhouettes facing each other, one elderly and one tall and slender, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem Kaku leo những bậc thang sức mạnh, hãy đăng ký kênh. Và nhớ: nấc cao nhất đôi khi lại là nấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at the top of a glowing staircase, waving goodbye with a big laugh. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nấc 0: cơ thể cao su

Khoảng 112 giây · cảnh s01–s11 · 1462 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này đi tới Gear 5 và arc Egghead của manga One Piece. Nếu bạn đang xem bản làm lại từ đầu, hãy lưu video lại cho sau này.

<short pause> Một cơ thể cao su. Nghe thì buồn cười. Bị đấm không đau, bị bắn đạn nảy ngược lại. <short pause> Nhưng làm sao một cơ thể cao su có thể đánh bại những kẻ mạnh nhất thế giới?

<short pause> Câu trả lời của Luffy là các Gear, tức các cấp số. Giống như sang số trên xe: mỗi cấp nhanh hơn, mạnh hơn, và tốn nhiều sức hơn.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku leo bậc thang Gear của Luffy: từ Gear 2 tới Gear 5. Mỗi nấc có điều kiện, sức mạnh, và cái giá. Cuối video là cả bậc thang trong một hình.

<short pause> Và Kaku nhắc trước: Luffy không có sức mạnh nào miễn phí. Mỗi Gear đều được sinh ra từ một trận thua, hoặc một lần suýt mất đồng đội.

<short pause> Nấc đầu tiên là Gear 1, tức Luffy bình thường, sau khi ăn trái Gomu Gomu. Cơ thể co giãn, kéo dài tay chân để tung những cú đấm từ xa.

<short pause> Điểm mạnh: miễn nhiễm với đòn đánh cùn và điện, vì cao su không dẫn điện. Luffy từng thắng Enel, kẻ tự xưng là thần sấm, chính nhờ điều này.

<short pause> Điểm yếu: dao kiếm vẫn cắt được, và như mọi người ăn trái ác quỷ, Luffy không biết bơi.

<short pause> Điều kiện: ăn trái ác quỷ. Cái giá: mất khả năng bơi, với một người muốn làm Vua Hải Tặc.

<short pause> Luffy ăn trái ác quỷ khi còn nhỏ, vì tưởng đó chỉ là một món ăn lạ. Một sức mạnh định mệnh bắt đầu từ một lần ăn vụng.

<short pause> Kaku để ý: cơ thể cao su của Luffy lúc đầu chỉ là một cơ thể bị động, chịu đòn tốt. Mọi Gear về sau là cách cậu biến sự co giãn thành vũ khí chủ động.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này đi tới Gear 5 và arc Egghead của manga One Piece. Nếu bạn đang xem bản làm lại từ đầu, hãy lưu video lại cho sau này.

[pause] Một cơ thể cao su. Nghe thì buồn cười. Bị đấm không đau, bị bắn đạn nảy ngược lại. [pause] [curious] Nhưng làm sao một cơ thể cao su có thể đánh bại những kẻ mạnh nhất thế giới?

[pause] Câu trả lời của Luffy là các Gear, tức các cấp số. Giống như sang số trên xe: mỗi cấp nhanh hơn, mạnh hơn, và tốn nhiều sức hơn.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku leo bậc thang Gear của Luffy: từ Gear 2 tới Gear 5. Mỗi nấc có điều kiện, sức mạnh, và cái giá. Cuối video là cả bậc thang trong một hình.

[pause] Và Kaku nhắc trước: Luffy không có sức mạnh nào miễn phí. Mỗi Gear đều được sinh ra từ một trận thua, hoặc một lần suýt mất đồng đội.

[pause] Nấc đầu tiên là Gear 1, tức Luffy bình thường, sau khi ăn trái Gomu Gomu. Cơ thể co giãn, kéo dài tay chân để tung những cú đấm từ xa.

[pause] Điểm mạnh: miễn nhiễm với đòn đánh cùn và điện, vì cao su không dẫn điện. Luffy từng thắng Enel, kẻ tự xưng là thần sấm, chính nhờ điều này.

[pause] Điểm yếu: dao kiếm vẫn cắt được, và như mọi người ăn trái ác quỷ, Luffy không biết bơi.

[pause] Điều kiện: ăn trái ác quỷ. Cái giá: mất khả năng bơi, với một người muốn làm Vua Hải Tặc.

[pause] Luffy ăn trái ác quỷ khi còn nhỏ, vì tưởng đó chỉ là một món ăn lạ. Một sức mạnh định mệnh bắt đầu từ một lần ăn vụng.

[pause] Kaku để ý: cơ thể cao su của Luffy lúc đầu chỉ là một cơ thể bị động, chịu đòn tốt. Mọi Gear về sau là cách cậu biến sự co giãn thành vũ khí chủ động.
```

### c02 · Nấc 1: Gear 2 / Nấc 2: Gear 3 / Tên đòn: nhật ký sức mạnh

Khoảng 143 giây · cảnh s12–s25 · 1865 ký tự

**Gemini**

```text
Hoàn cảnh ra đời: trước arc Enies Lobby, Luffy thua thảm một kẻ thù rất nhanh. Cậu nhận ra mình cần tốc độ và sức mạnh vượt trội để bảo vệ đồng đội.

<short pause> Cách hoạt động: Luffy dùng cơ thể cao su để bơm máu đi khắp người nhanh hơn bình thường, như một cái bơm. Cơ thể nóng lên, bốc hơi, da đỏ hồng.

<short pause> Lần đầu xuất hiện ở chương 387, trong arc Enies Lobby. Tốc độ và sức mạnh tăng vọt, tới mức đối thủ không kịp nhìn thấy.

<short pause> Cái giá: cơ thể chịu áp lực cực lớn. Trong truyện, có người cảnh báo rằng nó có thể làm hao mòn cơ thể, và Luffy kiệt sức rất nhanh sau khi dùng.

<short pause> Luffy nói với đối thủ, đại ý, rằng cậu cần sức mạnh này để không để mất bất kỳ người bạn nào. Gear 2 là lời hứa với đồng đội.

<short pause> Cách hoạt động: Luffy thổi hơi vào xương của mình. Vì xương cũng là cao su, tay hoặc chân phồng lên khổng lồ như một quả bóng.

<short pause> Sức mạnh: một cú đấm khổng lồ, có sức nặng và sức tàn phá của một vật cực lớn. Đủ để phá tường thành hay đánh bay người khổng lồ.

<short pause> Cái giá lúc đầu rất buồn cười: sau khi xả hơi, Luffy bị teo nhỏ lại như một đứa bé tí hon trong một lúc.

<short pause> Gear 2 là tốc độ, Gear 3 là khối lượng. Luffy bắt đầu kết hợp chúng: đánh nhanh bằng Gear 2, kết thúc bằng Gear 3.

<short pause> <laugh> Kaku để ý: cả Gear 2 lẫn Gear 3 đều ra đời trong cùng một arc, để giải cứu Robin. Luffy phát minh cả hai chỉ vì không muốn mất một người bạn.

<short pause> Luffy có một thói quen: hô tên đòn trước khi đánh. Cú đấm cơ bản gọi là Pistol, tức súng lục. Cú đá quét gọi là Whip, tức roi quất.

<short pause> Khi lên Gear 2, tên đòn có thêm chữ Jet, tức phản lực: Jet Pistol, Jet Bazooka. Đòn nhanh tới mức nắm tay đến trước cả tiếng hô.

<short pause> Khi lên Gear 3, tên đòn có thêm chữ Gigant, tức khổng lồ. Sang Gear 4, tên đòn mượn tên thú lớn: Kong, Leo là sư tử, Rhino là tê giác, rồi tới những loài rắn như Black Mamba và King Cobra.

<short pause> Kaku để ý: tên đòn chính là cuốn nhật ký sức mạnh của Luffy. Chỉ cần nghe tiếng hô, người đọc biết ngay cậu đang ở nấc nào.
```

**ElevenLabs**

```text
Hoàn cảnh ra đời: trước arc Enies Lobby, Luffy thua thảm một kẻ thù rất nhanh. Cậu nhận ra mình cần tốc độ và sức mạnh vượt trội để bảo vệ đồng đội.

[pause] Cách hoạt động: Luffy dùng cơ thể cao su để bơm máu đi khắp người nhanh hơn bình thường, như một cái bơm. Cơ thể nóng lên, bốc hơi, da đỏ hồng.

[pause] Lần đầu xuất hiện ở chương 387, trong arc Enies Lobby. Tốc độ và sức mạnh tăng vọt, tới mức đối thủ không kịp nhìn thấy.

[pause] Cái giá: cơ thể chịu áp lực cực lớn. Trong truyện, có người cảnh báo rằng nó có thể làm hao mòn cơ thể, và Luffy kiệt sức rất nhanh sau khi dùng.

[pause] Luffy nói với đối thủ, đại ý, rằng cậu cần sức mạnh này để không để mất bất kỳ người bạn nào. Gear 2 là lời hứa với đồng đội.

[pause] Cách hoạt động: Luffy thổi hơi vào xương của mình. Vì xương cũng là cao su, tay hoặc chân phồng lên khổng lồ như một quả bóng.

[pause] Sức mạnh: một cú đấm khổng lồ, có sức nặng và sức tàn phá của một vật cực lớn. Đủ để phá tường thành hay đánh bay người khổng lồ.

[pause] Cái giá lúc đầu rất buồn cười: sau khi xả hơi, Luffy bị teo nhỏ lại như một đứa bé tí hon trong một lúc.

[pause] Gear 2 là tốc độ, Gear 3 là khối lượng. Luffy bắt đầu kết hợp chúng: đánh nhanh bằng Gear 2, kết thúc bằng Gear 3.

[pause] [chuckles] Kaku để ý: cả Gear 2 lẫn Gear 3 đều ra đời trong cùng một arc, để giải cứu Robin. Luffy phát minh cả hai chỉ vì không muốn mất một người bạn.

[pause] Luffy có một thói quen: hô tên đòn trước khi đánh. Cú đấm cơ bản gọi là Pistol, tức súng lục. Cú đá quét gọi là Whip, tức roi quất.

[pause] Khi lên Gear 2, tên đòn có thêm chữ Jet, tức phản lực: Jet Pistol, Jet Bazooka. Đòn nhanh tới mức nắm tay đến trước cả tiếng hô.

[pause] Khi lên Gear 3, tên đòn có thêm chữ Gigant, tức khổng lồ. Sang Gear 4, tên đòn mượn tên thú lớn: Kong, Leo là sư tử, Rhino là tê giác, rồi tới những loài rắn như Black Mamba và King Cobra.

[pause] Kaku để ý: tên đòn chính là cuốn nhật ký sức mạnh của Luffy. Chỉ cần nghe tiếng hô, người đọc biết ngay cậu đang ở nấc nào.
```

### c03 · Gear 2 và 3 trên đường đi / Hai năm luyện tập và Haki

Khoảng 95 giây · cảnh s26–s34 · 1239 ký tự

**Gemini**

```text
Sau Enies Lobby, Gear 2 và Gear 3 trở thành vũ khí chính của Luffy trước những kẻ thù lớn hơn cậu rất nhiều, kể cả trên một hòn đảo ma đầy xác sống.

<short pause> Nhưng ở quần đảo Sabaody, cả băng gặp một Đô đốc Hải quân. Gear 2 và 3 gần như vô dụng: đối thủ quá nhanh, quá mạnh. Cả băng bị tách ra, mỗi người văng một nơi.

<short pause> Ở Marineford, Luffy dùng Gear 2 và 3 liên tục để lao tới cứu anh trai. Cơ thể cậu bị đẩy quá giới hạn, và dù vậy, cậu vẫn không kịp.

<short pause> <laugh> Kaku để ý: đây là lúc Luffy hiểu rằng thêm một cấp số nữa là không đủ. Cậu không cần sang số nhanh hơn, cậu cần một cái động cơ khác.

<short pause> Sau cuộc chiến Marineford và cái chết của Ace, Luffy thua đau nhất đời. Cậu chọn tạm dừng hai năm để luyện tập.

<short pause> Cậu học Haki từ Rayleigh, cánh tay phải của Vua Hải Tặc. Haki vũ trang cho phép phủ một lớp năng lượng cứng như thép lên cơ thể. Kaku đã nói kỹ về Haki trong một video riêng.

<short pause> Haki là chìa khóa mở ra Gear 4. Nó giải quyết một vấn đề cũ: cao su mềm thì khó gây sát thương thật cho kẻ mạnh.

<short pause> Luffy được dạy về cả ba loại Haki: vũ trang để phủ giáp, quan sát để cảm nhận đối thủ, và bá vương, loại Haki chỉ một số ít người sinh ra đã có.

<short pause> Luffy luyện tập hai năm trên một hòn đảo đầy thú dữ. Khi trở lại, cậu mạnh hơn hẳn, nhưng vẫn giữ Gear 4 như một con bài tẩy.
```

**ElevenLabs**

```text
Sau Enies Lobby, Gear 2 và Gear 3 trở thành vũ khí chính của Luffy trước những kẻ thù lớn hơn cậu rất nhiều, kể cả trên một hòn đảo ma đầy xác sống.

[pause] Nhưng ở quần đảo Sabaody, cả băng gặp một Đô đốc Hải quân. Gear 2 và 3 gần như vô dụng: đối thủ quá nhanh, quá mạnh. Cả băng bị tách ra, mỗi người văng một nơi.

[pause] Ở Marineford, Luffy dùng Gear 2 và 3 liên tục để lao tới cứu anh trai. Cơ thể cậu bị đẩy quá giới hạn, và dù vậy, cậu vẫn không kịp.

[pause] [chuckles] Kaku để ý: đây là lúc Luffy hiểu rằng thêm một cấp số nữa là không đủ. Cậu không cần sang số nhanh hơn, cậu cần một cái động cơ khác.

[pause] Sau cuộc chiến Marineford và cái chết của Ace, Luffy thua đau nhất đời. Cậu chọn tạm dừng hai năm để luyện tập.

[pause] Cậu học Haki từ Rayleigh, cánh tay phải của Vua Hải Tặc. Haki vũ trang cho phép phủ một lớp năng lượng cứng như thép lên cơ thể. Kaku đã nói kỹ về Haki trong một video riêng.

[pause] Haki là chìa khóa mở ra Gear 4. Nó giải quyết một vấn đề cũ: cao su mềm thì khó gây sát thương thật cho kẻ mạnh.

[pause] Luffy được dạy về cả ba loại Haki: vũ trang để phủ giáp, quan sát để cảm nhận đối thủ, và bá vương, loại Haki chỉ một số ít người sinh ra đã có.

[pause] Luffy luyện tập hai năm trên một hòn đảo đầy thú dữ. Khi trở lại, cậu mạnh hơn hẳn, nhưng vẫn giữ Gear 4 như một con bài tẩy.
```

### c04 · Nấc 3: Gear 4 / Gear 4 trong thực chiến

Khoảng 135 giây · cảnh s35–s46 · 1751 ký tự

**Gemini**

```text
Gear 4 lần đầu xuất hiện ở chương 784, trong trận với Doflamingo ở Dressrosa. Luffy thổi phồng cơ bắp, rồi phủ Haki vũ trang lên, biến cơ thể thành một khối cao su cứng và đàn hồi.

<short pause> Dạng đầu tiên là Boundman: cơ thể nảy liên tục như quả bóng, và những cú đấm nén lại rồi bật ra với lực khủng khiếp.

<short pause> Về sau có thêm Tankman, một cơ thể phình to để hấp thụ đòn đánh, và Snakeman, thon gọn hơn, với những cú đấm uốn lượn, đổi hướng liên tục, nhanh hơn Boundman.

<short pause> Cái giá của Gear 4 rất rõ ràng: nó chỉ kéo dài một thời gian ngắn. Khi hết, Luffy không dùng được Haki trong khoảng mười phút. Trong một trận đấu, mười phút là vô cùng dài.

<short pause> Để vào Gear 4, Luffy cắn vào cánh tay và thổi phồng cơ bắp giống cách làm Gear 3, nhưng lần này là cả thân trên. Rồi Haki phủ lên, đen bóng như thép.

<short pause> Gear 4 là lần đầu tiên Luffy kết hợp trái ác quỷ với một kỹ năng học được. Sức mạnh không còn chỉ là bẩm sinh, mà là thứ luyện ra.

<short pause> Ở Dressrosa, Boundman đủ sức áp đảo Doflamingo. <short pause> Nhưng khi hết thời gian, Luffy nằm bất động, và cả hòn đảo phải liều mạng câu giờ cho cậu hồi sức.

<short pause> Ở Whole Cake Island, Luffy gặp một đối thủ tạo ra vô số lính bánh quy. Cậu ăn chúng tới mức bụng căng tròn, rồi dùng Gear 4 để biến lượng đồ ăn ấy thành dạng Tankman.

<short pause> Tankman hấp thụ đòn đánh bằng cơ thể phình to, rồi dồn toàn bộ lực bắn ngược lại. Đây là dạng thiên về phòng thủ nhất trong bậc thang Gear.

<short pause> Rồi tới đối thủ khó nhất arc: một chỉ huy có thể nhìn thấy tương lai gần bằng Haki quan sát. Mọi cú đấm của Luffy đều bị đoán trước.

<short pause> Snakeman ra đời ở chương 894 để giải bài toán ấy: nắm tay lượn vòng, đổi hướng giữa chừng, nhanh tới mức dù đoán trước vẫn khó né.

<short pause> Và trong trận ấy, Luffy tự học được cách nhìn thấy tương lai, giống đối thủ. Kaku để ý: đối thủ mạnh nhất lại là người thầy tốt nhất.
```

**ElevenLabs**

```text
Gear 4 lần đầu xuất hiện ở chương 784, trong trận với Doflamingo ở Dressrosa. Luffy thổi phồng cơ bắp, rồi phủ Haki vũ trang lên, biến cơ thể thành một khối cao su cứng và đàn hồi.

[pause] Dạng đầu tiên là Boundman: cơ thể nảy liên tục như quả bóng, và những cú đấm nén lại rồi bật ra với lực khủng khiếp.

[pause] Về sau có thêm Tankman, một cơ thể phình to để hấp thụ đòn đánh, và Snakeman, thon gọn hơn, với những cú đấm uốn lượn, đổi hướng liên tục, nhanh hơn Boundman.

[pause] Cái giá của Gear 4 rất rõ ràng: nó chỉ kéo dài một thời gian ngắn. Khi hết, Luffy không dùng được Haki trong khoảng mười phút. Trong một trận đấu, mười phút là vô cùng dài.

[pause] Để vào Gear 4, Luffy cắn vào cánh tay và thổi phồng cơ bắp giống cách làm Gear 3, nhưng lần này là cả thân trên. Rồi Haki phủ lên, đen bóng như thép.

[pause] Gear 4 là lần đầu tiên Luffy kết hợp trái ác quỷ với một kỹ năng học được. Sức mạnh không còn chỉ là bẩm sinh, mà là thứ luyện ra.

[pause] Ở Dressrosa, Boundman đủ sức áp đảo Doflamingo. [pause] Nhưng khi hết thời gian, Luffy nằm bất động, và cả hòn đảo phải liều mạng câu giờ cho cậu hồi sức.

[pause] Ở Whole Cake Island, Luffy gặp một đối thủ tạo ra vô số lính bánh quy. Cậu ăn chúng tới mức bụng căng tròn, rồi dùng Gear 4 để biến lượng đồ ăn ấy thành dạng Tankman.

[pause] Tankman hấp thụ đòn đánh bằng cơ thể phình to, rồi dồn toàn bộ lực bắn ngược lại. Đây là dạng thiên về phòng thủ nhất trong bậc thang Gear.

[pause] Rồi tới đối thủ khó nhất arc: một chỉ huy có thể nhìn thấy tương lai gần bằng Haki quan sát. Mọi cú đấm của Luffy đều bị đoán trước.

[pause] Snakeman ra đời ở chương 894 để giải bài toán ấy: nắm tay lượn vòng, đổi hướng giữa chừng, nhanh tới mức dù đoán trước vẫn khó né.

[pause] Và trong trận ấy, Luffy tự học được cách nhìn thấy tương lai, giống đối thủ. Kaku để ý: đối thủ mạnh nhất lại là người thầy tốt nhất.
```

### c05 · Wano: Haki cấp cao / Bí mật của trái ác quỷ

Khoảng 84 giây · cảnh s47–s55 · 1095 ký tự

**Gemini**

```text
Ở Wano, Luffy bị Kaido hạ chỉ bằng một đòn, dù đang ở Gear 4. Cậu bị ném vào một nhà tù khai thác mỏ.

<short pause> Ở đó, một ông lão tù nhân dạy cậu một cách dùng Haki vũ trang mới: đẩy lực vào bên trong đối thủ thay vì chỉ phủ lớp giáp bên ngoài, thậm chí đánh mà không cần chạm.

<short pause> Rồi trong trận quyết chiến, Luffy học được cách phủ Haki bá vương lên đòn đánh. Chỉ những kẻ mạnh nhất thế giới mới làm được điều này.

<short pause> <laugh> Kaku để ý: trước khi thức tỉnh Gear 5, Luffy đã chạm tới đỉnh Haki. Gear 5 không đến với một người yếu, mà đến đúng lúc cậu đã dốc cạn mọi thứ.

<short pause> Rồi tới Wano. Trong trận với Kaido, Luffy thua, ngã xuống, và tim cậu gần như ngừng đập.

<short pause> Và ở chương 1044, sự thật được tiết lộ: trái của Luffy không phải trái cao su. Tên thật của nó là Hito Hito no Mi, mô hình Nika, một trái Zoan thần thoại.

<short pause> Chính phủ Thế giới đã đổi tên trái này suốt nhiều thế kỷ để giấu nó. Và trái Zoan có ý chí riêng: nó đã chọn Luffy.

<short pause> Luffy thức tỉnh trái ác quỷ. Và điều đầu tiên cậu làm, là cười.

<short pause> Kaku để ý: Kaku đã nói về chi tiết này trong video mười hiểu lầm One Piece. Hôm nay ta nhìn nó như nấc cuối cùng của bậc thang Gear.
```

**ElevenLabs**

```text
Ở Wano, Luffy bị Kaido hạ chỉ bằng một đòn, dù đang ở Gear 4. Cậu bị ném vào một nhà tù khai thác mỏ.

[pause] Ở đó, một ông lão tù nhân dạy cậu một cách dùng Haki vũ trang mới: đẩy lực vào bên trong đối thủ thay vì chỉ phủ lớp giáp bên ngoài, thậm chí đánh mà không cần chạm.

[pause] Rồi trong trận quyết chiến, Luffy học được cách phủ Haki bá vương lên đòn đánh. Chỉ những kẻ mạnh nhất thế giới mới làm được điều này.

[pause] [chuckles] Kaku để ý: trước khi thức tỉnh Gear 5, Luffy đã chạm tới đỉnh Haki. Gear 5 không đến với một người yếu, mà đến đúng lúc cậu đã dốc cạn mọi thứ.

[pause] Rồi tới Wano. Trong trận với Kaido, Luffy thua, ngã xuống, và tim cậu gần như ngừng đập.

[pause] Và ở chương 1044, sự thật được tiết lộ: trái của Luffy không phải trái cao su. Tên thật của nó là Hito Hito no Mi, mô hình Nika, một trái Zoan thần thoại.

[pause] Chính phủ Thế giới đã đổi tên trái này suốt nhiều thế kỷ để giấu nó. Và trái Zoan có ý chí riêng: nó đã chọn Luffy.

[pause] Luffy thức tỉnh trái ác quỷ. Và điều đầu tiên cậu làm, là cười.

[pause] Kaku để ý: Kaku đã nói về chi tiết này trong video mười hiểu lầm One Piece. Hôm nay ta nhìn nó như nấc cuối cùng của bậc thang Gear.
```

### c06 · Nấc 4: Gear 5 / Điều kiện và cái giá của từng nấc

Khoảng 125 giây · cảnh s56–s68 · 1624 ký tự

**Gemini**

```text
Gear 5 là trạng thái thức tỉnh. Cơ thể Luffy trở nên tự do như trong phim hoạt hình: mắt trố ra, cơ thể biến dạng theo ý muốn, và cậu có thể biến cả môi trường xung quanh thành cao su.

<short pause> Luffy túm lấy tia sét. Kéo mặt đất như kéo một tấm vải. Và biến những đòn đánh nghiêm túc nhất thành những trò đùa.

<short pause> Tính cách của Nika là tiếng cười và sự giải phóng. Và Gear 5 là sức mạnh chỉ bị giới hạn bởi trí tưởng tượng của Luffy.

<short pause> Cái giá: Gear 5 tiêu hao sức lực khủng khiếp. Sau khi dùng, Luffy kiệt sức tới mức cơ thể teo lại, trông như già đi trong một lúc.

<short pause> Với Gear 5, Luffy kết thúc trận chiến với Kaido và giải phóng Wano. Nhịp tim của cậu vang lên như tiếng trống, được gọi là trống giải phóng.

<short pause> Nhưng ở Egghead, ta thấy Gear 5 có giới hạn thời gian. Khi hết, Luffy phải nghỉ để hồi sức, đôi khi vào đúng lúc nguy hiểm nhất.

<short pause> Nghĩa là dù ở nấc cao nhất, luật cũ vẫn đúng: không có sức mạnh nào miễn phí. Gear 5 chỉ đẩy cái giá lên cao hơn.

<short pause> Kaku để ý: Gear 5 là nấc duy nhất không đến từ việc luyện tập hay một trận thua. Nó đến từ việc chính trái ác quỷ công nhận Luffy.

<short pause> Tổng kết điều kiện và cái giá. Gear 1: ăn trái ác quỷ, đổi lại mất khả năng bơi.

<short pause> Gear 2: một trận thua và nhu cầu tốc độ; đổi lại áp lực lớn lên cơ thể. Gear 3: sự sáng tạo với xương cao su; đổi lại tạm thời teo nhỏ.

<short pause> Gear 4: hai năm luyện Haki; đổi lại mười phút không Haki. Gear 5: được trái ác quỷ thức tỉnh; đổi lại kiệt sức hoàn toàn.

<short pause> Nếu vẽ thành biểu đồ, sức mạnh đi lên như bậc thang, còn cái giá đi lên theo cùng một nhịp. Không nấc nào được ưu đãi.

<short pause> Và có một điều không đổi ở mọi nấc: mỗi lần Luffy lên một Gear mới, đều là vì một người bạn đang gặp nguy hiểm.
```

**ElevenLabs**

```text
Gear 5 là trạng thái thức tỉnh. Cơ thể Luffy trở nên tự do như trong phim hoạt hình: mắt trố ra, cơ thể biến dạng theo ý muốn, và cậu có thể biến cả môi trường xung quanh thành cao su.

[pause] Luffy túm lấy tia sét. Kéo mặt đất như kéo một tấm vải. Và biến những đòn đánh nghiêm túc nhất thành những trò đùa.

[pause] Tính cách của Nika là tiếng cười và sự giải phóng. Và Gear 5 là sức mạnh chỉ bị giới hạn bởi trí tưởng tượng của Luffy.

[pause] Cái giá: Gear 5 tiêu hao sức lực khủng khiếp. Sau khi dùng, Luffy kiệt sức tới mức cơ thể teo lại, trông như già đi trong một lúc.

[pause] Với Gear 5, Luffy kết thúc trận chiến với Kaido và giải phóng Wano. Nhịp tim của cậu vang lên như tiếng trống, được gọi là trống giải phóng.

[pause] Nhưng ở Egghead, ta thấy Gear 5 có giới hạn thời gian. Khi hết, Luffy phải nghỉ để hồi sức, đôi khi vào đúng lúc nguy hiểm nhất.

[pause] Nghĩa là dù ở nấc cao nhất, luật cũ vẫn đúng: không có sức mạnh nào miễn phí. Gear 5 chỉ đẩy cái giá lên cao hơn.

[pause] Kaku để ý: Gear 5 là nấc duy nhất không đến từ việc luyện tập hay một trận thua. Nó đến từ việc chính trái ác quỷ công nhận Luffy.

[pause] Tổng kết điều kiện và cái giá. Gear 1: ăn trái ác quỷ, đổi lại mất khả năng bơi.

[pause] Gear 2: một trận thua và nhu cầu tốc độ; đổi lại áp lực lớn lên cơ thể. Gear 3: sự sáng tạo với xương cao su; đổi lại tạm thời teo nhỏ.

[pause] Gear 4: hai năm luyện Haki; đổi lại mười phút không Haki. Gear 5: được trái ác quỷ thức tỉnh; đổi lại kiệt sức hoàn toàn.

[pause] Nếu vẽ thành biểu đồ, sức mạnh đi lên như bậc thang, còn cái giá đi lên theo cùng một nhịp. Không nấc nào được ưu đãi.

[pause] Và có một điều không đổi ở mọi nấc: mỗi lần Luffy lên một Gear mới, đều là vì một người bạn đang gặp nguy hiểm.
```

### c07 · Ba quy luật của bậc thang / Vì sao Gear 5 gây tranh cãi / Góc nhìn của Kaku

Khoảng 134 giây · cảnh s69–s81 · 1742 ký tự

**Gemini**

```text
<laugh> Nhìn lại toàn bộ, Kaku thấy bậc thang Gear tuân theo ba quy luật.

<short pause> Quy luật một: mỗi nấc sửa một điểm yếu của nấc trước. Gear 1 thiếu tốc độ, Gear 2 thêm tốc độ. Gear 2 thiếu sức nặng, Gear 3 thêm khối lượng.

<short pause> Gear 3 chậm và để lộ sơ hở, Gear 4 gộp cả tốc độ lẫn sức nặng. Gear 4 bị kẻ mạnh hơn đè bẹp, Gear 5 phá luôn cả luật vật lý.

<short pause> Quy luật hai: cái giá tăng theo sức mạnh. Từ vài hơi thở gấp, tới teo nhỏ, tới mười phút mất Haki, rồi tới kiệt sức hoàn toàn.

<short pause> Quy luật ba: mỗi nấc là câu trả lời cho những con người cụ thể. Robin ở Enies Lobby. Nỗi đau mất Ace sau Marineford. Cả đất nước Wano bị áp bức.

<short pause> Kaku nghĩ đó là lý do bậc thang này hấp dẫn: nó không chỉ là danh sách sức mạnh, mà là một cuốn tiểu sử viết bằng những trận đấu.

<short pause> Khi Gear 5 lên anime, người xem chia làm hai phe. Một phe thấy hụt hẫng: trận đấu nghiêm túc nhất bỗng hóa thành phim hoạt hình vui nhộn.

<short pause> Phe kia cho rằng Gear 5 đã được cài từ đầu: Luffy luôn là nhân vật cười nhiều nhất, và giấc mơ của cậu là được tự do nhất trên biển.

<short pause> Nhiều người còn để ý: ngay từ những chương đầu, Luffy vốn đã co giãn như nhân vật hoạt hình cổ điển. Gear 5 chỉ đẩy phong cách ấy tới tận cùng.

<short pause> Kaku không đứng về phe nào. <short pause> Nhưng một sức mạnh khiến người xem cãi nhau tới vậy chắc chắn là một sức mạnh đáng nhớ. Bạn thuộc phe nào?

<short pause> Kaku nghĩ bậc thang Gear kể câu chuyện về cách Luffy lớn lên. Gear 2 và 3: một cậu thiếu niên liều mình vì bạn. Gear 4: một người chấp nhận học hỏi sau thất bại lớn nhất đời.

<short pause> Và Gear 5: một người trở thành biểu tượng tự do cho người khác. Không còn là sức mạnh của một cá nhân, mà là niềm hy vọng của những người bị áp bức.

<short pause> Và thú vị nhất: nấc mạnh nhất lại là nấc vui nhộn nhất. One Piece nói rằng sức mạnh thật không đến từ sự nghiêm trọng, mà từ tự do và tiếng cười.
```

**ElevenLabs**

```text
[chuckles] Nhìn lại toàn bộ, Kaku thấy bậc thang Gear tuân theo ba quy luật.

[pause] Quy luật một: mỗi nấc sửa một điểm yếu của nấc trước. Gear 1 thiếu tốc độ, Gear 2 thêm tốc độ. Gear 2 thiếu sức nặng, Gear 3 thêm khối lượng.

[pause] Gear 3 chậm và để lộ sơ hở, Gear 4 gộp cả tốc độ lẫn sức nặng. Gear 4 bị kẻ mạnh hơn đè bẹp, Gear 5 phá luôn cả luật vật lý.

[pause] Quy luật hai: cái giá tăng theo sức mạnh. Từ vài hơi thở gấp, tới teo nhỏ, tới mười phút mất Haki, rồi tới kiệt sức hoàn toàn.

[pause] Quy luật ba: mỗi nấc là câu trả lời cho những con người cụ thể. Robin ở Enies Lobby. Nỗi đau mất Ace sau Marineford. Cả đất nước Wano bị áp bức.

[pause] Kaku nghĩ đó là lý do bậc thang này hấp dẫn: nó không chỉ là danh sách sức mạnh, mà là một cuốn tiểu sử viết bằng những trận đấu.

[pause] Khi Gear 5 lên anime, người xem chia làm hai phe. Một phe thấy hụt hẫng: trận đấu nghiêm túc nhất bỗng hóa thành phim hoạt hình vui nhộn.

[pause] Phe kia cho rằng Gear 5 đã được cài từ đầu: Luffy luôn là nhân vật cười nhiều nhất, và giấc mơ của cậu là được tự do nhất trên biển.

[pause] Nhiều người còn để ý: ngay từ những chương đầu, Luffy vốn đã co giãn như nhân vật hoạt hình cổ điển. Gear 5 chỉ đẩy phong cách ấy tới tận cùng.

[pause] Kaku không đứng về phe nào. [pause] Nhưng một sức mạnh khiến người xem cãi nhau tới vậy chắc chắn là một sức mạnh đáng nhớ. [curious] Bạn thuộc phe nào?

[pause] Kaku nghĩ bậc thang Gear kể câu chuyện về cách Luffy lớn lên. Gear 2 và 3: một cậu thiếu niên liều mình vì bạn. Gear 4: một người chấp nhận học hỏi sau thất bại lớn nhất đời.

[pause] Và Gear 5: một người trở thành biểu tượng tự do cho người khác. Không còn là sức mạnh của một cá nhân, mà là niềm hy vọng của những người bị áp bức.

[pause] Và thú vị nhất: nấc mạnh nhất lại là nấc vui nhộn nhất. One Piece nói rằng sức mạnh thật không đến từ sự nghiêm trọng, mà từ tự do và tiếng cười.
```

### c08 · Trò chơi: bạn muốn Gear nào? / Kết

Khoảng 78 giây · cảnh s82–s88 · 1012 ký tự

**Gemini**

```text
Nếu bạn có cơ thể cao su, bạn muốn dùng Gear nào trong đời thường? Gear 2 để chạy kịp xe buýt? Gear 3 để với đồ trên nóc tủ?

<short pause> Hay Gear 4 Tankman để ăn hết một bàn buffet mà không thấy no? Còn Gear 5, bạn sẽ biến thứ gì quanh mình thành cao su?

<short pause> <laugh> Kaku chọn Gear 5, nhưng chỉ để biến bàn học thành cao su, cho cú ngã từ ghế đỡ đau. Viết lựa chọn của bạn vào bình luận nhé.

<short pause> Từ một cơ thể cao su bị coi là trò đùa, tới một vị thần của tiếng cười. Bậc thang Gear của Luffy là bậc thang của một người chưa bao giờ ngừng vươn xa hơn, như chính cánh tay của cậu.

<short pause> Và bậc thang ấy chưa kết thúc. Manga vẫn đang tiếp tục, và biết đâu Luffy còn một nấc nữa mà chưa ai đoán được.

<short pause> Video tiếp theo, Kaku phân tích một trận đấu kinh điển: Hunter x Hunter, Netero đấu với vua kiến Meruem. Một trận đấu giữa đỉnh cao của con người và một sinh vật sinh ra để vượt qua con người.

<short pause> Nếu bạn thích xem Kaku leo những bậc thang sức mạnh, hãy đăng ký kênh. Và nhớ: nấc cao nhất đôi khi lại là nấc bạn cười nhiều nhất. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Nếu bạn có cơ thể cao su, bạn muốn dùng Gear nào trong đời thường? Gear 2 để chạy kịp xe buýt? Gear 3 để với đồ trên nóc tủ?

[pause] Hay Gear 4 Tankman để ăn hết một bàn buffet mà không thấy no? Còn Gear 5, bạn sẽ biến thứ gì quanh mình thành cao su?

[pause] [chuckles] Kaku chọn Gear 5, nhưng chỉ để biến bàn học thành cao su, cho cú ngã từ ghế đỡ đau. Viết lựa chọn của bạn vào bình luận nhé.

[pause] Từ một cơ thể cao su bị coi là trò đùa, tới một vị thần của tiếng cười. Bậc thang Gear của Luffy là bậc thang của một người chưa bao giờ ngừng vươn xa hơn, như chính cánh tay của cậu.

[pause] Và bậc thang ấy chưa kết thúc. Manga vẫn đang tiếp tục, và biết đâu Luffy còn một nấc nữa mà chưa ai đoán được.

[pause] Video tiếp theo, Kaku phân tích một trận đấu kinh điển: Hunter x Hunter, Netero đấu với vua kiến Meruem. Một trận đấu giữa đỉnh cao của con người và một sinh vật sinh ra để vượt qua con người.

[pause] Nếu bạn thích xem Kaku leo những bậc thang sức mạnh, hãy đăng ký kênh. Và nhớ: nấc cao nhất đôi khi lại là nấc bạn cười nhiều nhất. Kaku gấp sổ đây, hẹn gặp lại!
```
