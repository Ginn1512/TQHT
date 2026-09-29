# Bộ prompt · Naruto vs Pain: Phân tích từng hiệp — thông tin, năm giây và lựa chọn cuối cùng

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 85 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (85 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói trọn arc Pain tấn công làng Lá, tức manga chương 413 tới 453, và Naruto Shipp…

```text
Wide 16:9 landscape cinematic frame. a closed scroll tied with a red cord lying on a stone ledge overlooking a ruined village, close-up, overcast grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một ngôi làng bị san phẳng chỉ trong một đòn. Không còn nhà, không còn tường, chỉ còn một hố sâu khổng lồ ở c…

```text
Wide 16:9 landscape cinematic frame. an enormous circular crater where a village used to be, debris scattered at its rim, a single figure standing at the center, aerial wide shot, dramatic grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Rồi một tiếng động vang lên. Một làn khói bốc lên ở rìa hố. Người anh hùng của làng vừa trở về, cưỡi trên lưn…

```text
Wide 16:9 landscape cinematic frame. a thick plume of smoke rising at the edge of a crater with giant silhouettes of toads emerging from it, wide shot, dramatic backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đây là Naruto đấu với Pain, một trong những trận được người xem tìm kiếm nhiều nhất của cả loạt Naruto. Nhưng…

```text
Wide 16:9 landscape cinematic frame. two silhouettes facing each other across a vast crater under a heavy sky, wide shot, tense dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Vì đây là một trận đấu chiến thuật: thông tin, chuẩn bị, và cả kiểm soát cảm xúc. Và nó kết thúc theo một các…

```text
Wide 16:9 landscape cinematic frame. a strategy board with pieces arranged around a central crater drawing, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku phân tích trận Naruto đấu Pain, từng hiệp một: mục tiêu, lựa chọn, v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny referee headband, standing beside a tactical board with arrows and circles. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Trước trận: tỉ số trên giấy

Lời: Trước trận, gần như mọi thứ đều nghiêng về phía Pain. Hãy xem hồ sơ hai bên.

```text
Wide 16:9 landscape cinematic frame. a scale drawn on parchment tipping heavily to one side, amber ink close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Pain: thủ lĩnh Akatsuki, sở hữu đôi mắt Luân Hồi Nhãn. Hắn điều khiển sáu thân xác cùng lúc, mỗi thân xác một…

```text
Wide 16:9 landscape cinematic frame. six cloaked silhouettes standing in a row on a rooftop in the rain, each with a slightly different posture, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Hắn vừa giết Jiraiya, thầy của Naruto và là một trong ba Ninja huyền thoại. Hắn vừa san phẳng cả làng Lá bằng…

```text
Wide 16:9 landscape cinematic frame. a broken writing brush and an open notebook lying in shallow water at the bottom of a misty lake, close-up, somber blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Naruto: vừa hoàn thành khóa luyện tập Hiền nhân ở núi Myoboku. Cậu có một sức mạnh mới, nhưng chưa từng dùng…

```text
Wide 16:9 landscape cinematic frame. a young figure meditating on a stone pillar above a misty mountain valley with large toads watching nearby, wide shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Nếu hỏi người trong làng lúc đó, gần như ai cũng sẽ đặt cược vào Pain. Và Kaku cũng vậy, nếu chỉ nhìn trên gi…

```text
Wide 16:9 landscape cinematic frame. a betting board drawn on parchment with most tally marks under one column, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Nhưng Naruto có một thứ Pain không biết: một manh mối từ người thầy đã chết.

```text
Wide 16:9 landscape cinematic frame. a coded message tattooed in small symbols on the back of an old toad's shell, extreme close-up, mysterious warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Hồ sơ sáu thân xác

Lời: Trước khi vào trận, Kaku mở nhanh hồ sơ sáu thân xác của Pain, vì mỗi thân là một bài toán riêng mà Naruto ph…

```text
Wide 16:9 landscape cinematic frame. six small index cards laid out in a row on a stone table, each with a different symbol, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Thiên Đạo: điều khiển lực đẩy và lực hút. Đây là thân xác mạnh nhất, và cũng là bộ mặt mà cả thế giới biết tớ…

```text
Wide 16:9 landscape cinematic frame. a card with a symbol of outward-pointing arrows around a circle, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Tu La Đạo: thân xác như một cỗ máy, gắn vũ khí khắp người, bắn tên lửa và lưỡi dao. Súc Sinh Đạo: triệu hồi n…

```text
Wide 16:9 landscape cinematic frame. two cards side by side, one with a gear symbol and one with a paw print symbol, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Nhân Đạo: đọc ký ức và rút linh hồn chỉ bằng một cái chạm. Ngạ Quỷ Đạo: hút mọi loại chakra và thuật nhẫn.

```text
Wide 16:9 landscape cinematic frame. two cards side by side, one with a hand symbol and one with an open mouth symbol, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Địa Ngục Đạo: triệu hồi một thực thể có thể hồi phục các thân xác khác. Đây là lý do phải hạ nó, nếu không cá…

```text
Wide 16:9 landscape cinematic frame. a card with a symbol of a gate with a crown above it, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Sáu thân xác, sáu năng lực, và chúng thấy những gì nhau thấy. Đánh một chọi sáu mà sáu cùng một bộ não, đó là…

```text
Wide 16:9 landscape cinematic frame. six connected dots forming a network on parchment with lines linking every dot to every other, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Làng Lá trước khi Naruto về

Lời: Trước khi Naruto trở về, làng Lá đã chiến đấu. Kakashi đấu với nhiều thân xác cùng lúc, và chính trong trận đ…

```text
Wide 16:9 landscape cinematic frame. a lone silver-haired silhouette crouched on a rooftop facing several cloaked figures in the distance, wide shot, tense grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Hokage Tsunade dùng rất nhiều năng lượng của mình để cùng Katsuyu, con sên triệu hồi, chia nhỏ thân mình bao…

```text
Wide 16:9 landscape cinematic frame. countless tiny glowing slug-like creatures clinging protectively to villagers amid collapsing buildings, wide shot, soft healing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Nhờ vậy, dù cả làng bị san phẳng, rất nhiều người vẫn sống sót. Kaku thấy đây là một chi tiết hay bị bỏ qua:…

```text
Wide 16:9 landscape cinematic frame. villagers huddled together in the rubble looking up toward the sky with hope, wide shot, dusty warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Hiệp 0: manh mối của Jiraiya

Lời: Trước khi chết, Jiraiya đã chiến đấu với Pain và phát hiện ra một bí mật. Ông không kịp nói ra, nên để lại mộ…

```text
Wide 16:9 landscape cinematic frame. an old sage fighting alone in a rain-soaked village of towers, silhouetted against lightning, wide shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Mật mã được giải: người thật không nằm trong số đó. Nghĩa là sáu thân xác không phải Pain thật. Có một người…

```text
Wide 16:9 landscape cinematic frame. a decoded note on parchment with six crossed-out silhouettes and an arrow pointing to an empty space outside the frame, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Đây là hiệp quan trọng nhất, dù không có cú đấm nào. Nhờ Jiraiya, Naruto biết rằng đánh bại sáu thân xác chưa…

```text
Wide 16:9 landscape cinematic frame. a chess board where six pieces surround a king piece, but a hand is reaching in from off the board, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Jiraiya dùng cả mạng sống của mình để đổi lấy một câu. Và câu đó quyết định cả trận đấu. Thông tin…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a single small note card very carefully with both wings, eyes serious. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Hiệp 1: Hiền nhân xuất hiện

Lời: Mục tiêu của Naruto ở hiệp một: hạ từng thân xác một, trước khi chúng phối hợp được với nhau.

```text
Wide 16:9 landscape cinematic frame. a tactical diagram on parchment with six dots scattered around a crater and one arrow picking them off one by one, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Chế độ Hiền nhân cho Naruto sức mạnh thể chất lớn hơn, cảm nhận được xung quanh, và một thứ đặc biệt: đòn đán…

```text
Wide 16:9 landscape cinematic frame. a fist striking the air with a wide shimmering ripple of natural energy around it, dynamic close-up, green-gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Naruto hạ được thân xác Tu La Đạo, thân xác máy móc với vũ khí gắn khắp người, bằng một đòn Rasengan khổng lồ.

```text
Wide 16:9 landscape cinematic frame. a huge spinning sphere of energy slamming into a mechanical silhouette on the ground, dust exploding outward, dynamic wide shot, blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Rồi tới Ngạ Quỷ Đạo, thân xác có thể hút mọi loại chakra. Nó tóm lấy Naruto để hút năng lượng.

```text
Wide 16:9 landscape cinematic frame. a cloaked silhouette gripping another figure's arm with glowing energy being drawn into its palm, close-up, eerie purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nhưng năng lượng Hiền nhân là năng lượng tự nhiên, và cơ thể người thường không chịu nổi. Ngạ Quỷ Đạo hút vào…

```text
Wide 16:9 landscape cinematic frame. a stone statue with a frog-like shape frozen mid-motion in the middle of a ruined street, close-up, grey dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Kaku rất thích chi tiết này. Naruto không cần đánh. Chính luật của năng lượng tự nhiên đánh bại đối thủ. Đây…

```text
Wide 16:9 landscape cinematic frame. a small toad sitting calmly on top of a stone statue, close-up, soft ironic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Những con cóc khổng lồ cũng không đứng ngoài. Chúng chiến đấu cùng Naruto, và các lão cóc Hiền nhân ngồi trên…

```text
Wide 16:9 landscape cinematic frame. two small elderly toads perched on a figure's shoulders in the middle of a battlefield, close-up, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Hiệp một thuộc về Naruto. Nhưng Pain vẫn còn bốn thân xác, và hắn bắt đầu hiểu sức mạnh mới của đối thủ.

```text
Wide 16:9 landscape cinematic frame. four remaining cloaked silhouettes regrouping on a ridge above the crater, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Hiệp 2: điểm yếu của Hiền nhân

Lời: Nhưng chế độ Hiền nhân có một điểm yếu chí mạng: nó không kéo dài lâu. Muốn nạp lại năng lượng tự nhiên, Naru…

```text
Wide 16:9 landscape cinematic frame. a meditating figure sitting perfectly still while an enemy silhouette approaches from behind, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và ngồi yên giữa chiến trường với sáu kẻ thù thì gần như tự sát. Đây là vấn đề mà cả người thầy Jiraiya cũng…

```text
Wide 16:9 landscape cinematic frame. a lone meditating silhouette in the center of a crater surrounded by shadowy approaching figures, aerial wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Giải pháp của Naruto rất thông minh: cậu để các phân thân bóng ngồi yên ở núi Myoboku, gom năng lượng tự nhiê…

```text
Wide 16:9 landscape cinematic frame. several identical meditating figures sitting in a row on a distant mountain ledge, one of them vanishing in a puff of smoke, wide shot, green mist light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhưng chỉ có một số lượng phân thân giới hạn. Mỗi lần dùng một cái là một lần nạp. Naruto phải tính toán rất…

```text
Wide 16:9 landscape cinematic frame. a row of small glass vials on a shelf, some empty and some full of glowing green liquid, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Với năng lượng được nạp, Naruto dùng Phong độn Rasen Shuriken, lần này có thể ném đi, hạ hai thân xác Nhân Đạ…

```text
Wide 16:9 landscape cinematic frame. a spinning disc of wind energy with a glowing core flying through the air toward two silhouettes, dynamic wide shot, bright white-blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Địa Ngục Đạo, thân xác có thể hồi sinh các thân khác, cũng không trụ được. Naruto đã đi qua năm trên sáu thân…

```text
Wide 16:9 landscape cinematic frame. five fallen cloaked silhouettes lying on the rubble of a crater, one silhouette still standing in the distance, wide shot, dust-filled light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku đánh giá: hiệp hai là chiến thắng của sự chuẩn bị. Naruto thua Jiraiya về kinh nghiệm, nhưng hơn ở chỗ b…

```text
Wide 16:9 landscape cinematic frame. a patch sewn carefully over a hole in a cloth banner, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Hiệp 3: Thiên Đạo và cái bẫy

Lời: Chỉ còn lại Thiên Đạo, thân xác mạnh nhất. Năng lực của nó: đẩy mọi thứ ra xa, hoặc kéo mọi thứ lại gần.

```text
Wide 16:9 landscape cinematic frame. a lone cloaked figure standing calmly as rubble and dust are pushed outward in a perfect circle around him, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chính năng lực đẩy này, Thần La Thiên Chinh, đã san phẳng cả làng Lá. Ở quy mô nhỏ, nó biến Thiên Đạo thành g…

```text
Wide 16:9 landscape cinematic frame. a shockwave ring visibly bending the air around a figure, stones frozen mid-flight at its edge, dynamic close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Nhưng có một thông tin quý giá. Trước đó, Kakashi đã phát hiện ra: giữa hai lần dùng Thần La Thiên Chinh, Thi…

```text
Wide 16:9 landscape cinematic frame. a stopwatch lying in the dust with its hand frozen at five seconds, close-up, dramatic grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kakashi đã ngã xuống trong trận trước đó, nhưng thông tin ông tìm được vẫn được truyền đi. Lại một lần nữa, m…

```text
Wide 16:9 landscape cinematic frame. a torn headband lying on rubble beside a small handwritten note weighted down by a stone, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhưng Pain cũng không đứng yên. Hắn ghim Naruto xuống đất bằng những thanh kim loại truyền chakra, khiến cậu…

```text
Wide 16:9 landscape cinematic frame. a figure pinned to the ground by several dark metal rods in the middle of a crater, overhead shot, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Những thanh kim loại đó chính là thứ Nagato dùng để truyền chakra điều khiển sáu thân xác. Bị ghim bằng chúng…

```text
Wide 16:9 landscape cinematic frame. a close-up of a dark metal rod with small ridges glowing faintly at the tip, embedded in the ground, extreme close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Hiệp ba thuộc về Pain. Naruto bị bắt, và có vẻ như mọi chuẩn bị đã không đủ.

```text
Wide 16:9 landscape cinematic frame. the tactical board with most arrows erased and a single dark circle drawn over the center, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Hiệp 4: cơn giận và cánh cửa

Lời: Và rồi Hinata xuất hiện. Cô bé nhút nhát, người luôn dõi theo Naruto từ xa, bước ra một mình để bảo vệ cậu.

```text
Wide 16:9 landscape cinematic frame. a small figure standing alone between a pinned figure and a towering cloaked silhouette, wide shot, dramatic backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Hinata nói ra điều cô giữ trong lòng suốt nhiều năm: cô thích Naruto. Rồi cô chiến đấu, dù biết mình không có…

```text
Wide 16:9 landscape cinematic frame. a close-up of determined eyes reflecting a distant looming shadow, dramatic soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Pain hạ gục Hinata. Kaku không mô tả chi tiết. Chỉ cần biết: Naruto nhìn thấy, và trong cậu có thứ gì đó vỡ r…

```text
Wide 16:9 landscape cinematic frame. a small figure lying still on rubble in the distance, out of focus, while a pinned figure in the foreground clenches a fist, wide shot, heavy grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Cơn giận làm Cửu Vĩ bên trong Naruto trỗi dậy. Sáu đuôi, rồi tám đuôi. Cậu mất dần kiểm soát, và sức mạnh hủy…

```text
Wide 16:9 landscape cinematic frame. a swirling storm of red-orange energy erupting from a crater with multiple tail-like streams lashing outward, wide shot, fierce red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Pain đáp trả bằng Địa Bạo Thiên Tinh: hắn tạo ra một khối cầu khổng lồ, kéo đất đá xung quanh vào, định giam…

```text
Wide 16:9 landscape cinematic frame. a colossal sphere of rock and earth forming in the sky as debris is pulled upward from the ground, wide shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và ở tận sâu trong tâm trí Naruto, khi cậu gần mở phong ấn cuối cùng, một người xuất hiện: cha của cậu, Minat…

```text
Wide 16:9 landscape cinematic frame. a tall figure appearing in a dim flooded corridor inside a mind, reaching out to stop a hand from pulling off a seal, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Minato đã cài sẵn một phần chakra của mình vào phong ấn, để xuất hiện đúng lúc con trai cần. Ông sửa lại phon…

```text
Wide 16:9 landscape cinematic frame. two silhouettes of a father and son standing face to face in a quiet glowing space, symbolic wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Minato cũng nói với Naruto rằng ông tin con trai mình sẽ tìm ra câu trả lời mà thế hệ của ông chưa tìm được.…

```text
Wide 16:9 landscape cinematic frame. a large hand resting gently on a younger figure's head in a glowing quiet space, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy hiệp bốn là trận thua lớn nhất của Naruto, không phải vì Pain, mà vì cơn giận của chính cậu. Và nó…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting quietly with a hand on a small closed box, eyes soft and serious. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Hiệp 5: năm giây

Lời: Naruto trở lại, bình tĩnh hơn, với phân thân cuối cùng trong chế độ Hiền nhân. Mục tiêu của hiệp cuối: tận dụ…

```text
Wide 16:9 landscape cinematic frame. a calm figure standing up from the rubble with a steady gaze, wide shot, clearing sky light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Naruto tung một phân thân tấn công trước. Thiên Đạo dùng Thần La Thiên Chinh để đẩy nó đi. Và đồng hồ bắt đầu…

```text
Wide 16:9 landscape cinematic frame. a decoy figure being blasted backward by a shockwave while a second figure waits hidden behind rubble, dynamic wide shot, dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Đây chính là cách thông tin của Kakashi được biến thành chiến thuật. Biết đối thủ có năm giây trống là một ch…

```text
Wide 16:9 landscape cinematic frame. a hand pressing the start button of a stopwatch while a second hand draws an arrow on a tactical map, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Trong năm giây đó, Naruto thật lao tới từ một hướng khác. Thiên Đạo không thể đẩy nữa, và buộc phải đỡ đòn tr…

```text
Wide 16:9 landscape cinematic frame. a figure dashing across the crater at incredible speed with a trail of dust, dynamic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Rasengan trúng đích. Thân xác cuối cùng ngã xuống. Hiệp năm, và trận đấu trên chiến trường, thuộc về Naruto.

```text
Wide 16:9 landscape cinematic frame. a sphere of spinning energy impacting a figure at close range, a bright ring of light bursting outward, dynamic close-up, brilliant blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và hãy nhớ, lúc này Naruto đã không còn nhiều phân thân dự trữ. Nếu đòn này hụt, trận đấu có thể đã kết thúc…

```text
Wide 16:9 landscape cinematic frame. a single remaining glowing vial on an otherwise empty shelf, close-up, tense dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Kaku để ý: đòn quyết định không phải là đòn mạnh nhất. Nó là một đòn Rasengan cơ bản, thứ Naruto đã học từ rấ…

```text
Wide 16:9 landscape cinematic frame. a simple wooden practice target with a single perfect mark at its center, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Sau trận: người thật

Lời: Nhưng nhớ lại mật mã của Jiraiya: người thật không nằm trong số đó. Naruto quyết định đi tìm người điều khiển…

```text
Wide 16:9 landscape cinematic frame. a lone figure walking through a forest toward a distant tree with a strange tower-like structure growing from it, back view, wide shot, quiet grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Người thật là Nagato, một người từng là học trò của Jiraiya, giống như Naruto. Cơ thể ông gầy yếu, bị gắn vào…

```text
Wide 16:9 landscape cinematic frame. a frail silhouette sitting inside a mechanical frame with dark rods protruding from it, dimly lit inside a hollow tree, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nagato kể quá khứ của mình: chiến tranh đã cướp đi cha mẹ, bạn bè, và cả hy vọng của ông. Ông tin rằng chỉ có…

```text
Wide 16:9 landscape cinematic frame. a faded memory scene of three children huddled together under a single umbrella in the rain amid a war-torn landscape, sepia tone, melancholy light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nagato hỏi Naruto một câu: vậy cậu sẽ làm gì để mang lại hòa bình? Và Naruto thừa nhận: cậu chưa có câu trả l…

```text
Wide 16:9 landscape cinematic frame. two figures facing each other in a dim hollow tree, one seated and frail, one standing with an open posture, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Đây là lúc Naruto phải lựa chọn khó nhất trận. Người trước mặt đã giết thầy cậu, phá hủy làng cậu. Cậu có thể…

```text
Wide 16:9 landscape cinematic frame. a figure standing before a frail seated silhouette, fist clenched at his side, medium shot, tense dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nhưng Naruto chọn không giết. Cậu nói rằng nếu cậu trả thù, vòng lặp hận thù sẽ tiếp tục. Cậu tin vào điều mà…

```text
Wide 16:9 landscape cinematic frame. an unclenched open hand extended forward in a dim room, symbolic close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nagato bị thuyết phục. Ông dùng hết sức lực cuối cùng để thi triển một thuật hồi sinh, đưa những người đã chế…

```text
Wide 16:9 landscape cinematic frame. a gentle rain of soft light falling over a ruined village as figures begin to stir and rise from the rubble, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Konan, người bạn đồng hành của Nagato, tin vào lựa chọn của Naruto. Cô mang thi thể của bạn mình đi, và để lạ…

```text
Wide 16:9 landscape cinematic frame. a bouquet of delicate paper flowers resting on a stone step, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Naruto trở về làng không phải như một chiến binh thắng trận, mà như một người hùng được cả làng chào đón. Cậu…

```text
Wide 16:9 landscape cinematic frame. a crowd of villagers cheering and lifting a young figure onto their shoulders amid ruins at sunset, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Sơ đồ chiến thuật

Lời: Tổng kết trận đấu trên một sơ đồ. Hiệp không: thông tin từ Jiraiya. Hiệp một: Hiền nhân và Ngạ Quỷ Đạo hóa đá…

```text
Wide 16:9 landscape cinematic frame. a tactical board with the first three rounds marked with small icons: a note, a statue, and a spinning disc, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hiệp ba: Pain ghim Naruto. Hiệp bốn: Hinata, Cửu Vĩ, và Minato. Hiệp năm: năm giây và một Rasengan. Sau trận:…

```text
Wide 16:9 landscape cinematic frame. the tactical board completed with icons of a pinned figure, a flame, a stopwatch, and an open hand, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Điểm số theo hiệp: Naruto thắng hiệp không, một, hai, năm. Pain thắng hiệp ba và gần như thắng hiệp bốn. Nhưn…

```text
Wide 16:9 landscape cinematic frame. a scoreboard on parchment with round-by-round marks and a large final column labeled with a heart icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Ba bài học chiến thuật

Lời: Bài học một: thông tin thắng sức mạnh. Mật mã của Jiraiya và năm giây của Kakashi quyết định trận đấu nhiều h…

```text
Wide 16:9 landscape cinematic frame. a small note card placed on top of a heavy sword on a table, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bài học hai: dùng thế mạnh của mình để vá điểm yếu. Naruto không sửa được điểm yếu của chế độ Hiền nhân, nhưn…

```text
Wide 16:9 landscape cinematic frame. a puzzle piece fitting perfectly into a gap in another puzzle, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Và điều đáng nói: Naruto không giỏi kiểm soát cảm xúc một mình. Cậu được cứu bởi người cha. Kiểm soát cảm xúc…

```text
Wide 16:9 landscape cinematic frame. a steady hand resting on a trembling shoulder in a quiet room, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Bài học ba: kiểm soát cảm xúc. Khoảnh khắc Naruto gần thua nhất không phải khi bị ghim, mà khi cơn giận chiếm…

```text
Wide 16:9 landscape cinematic frame. a calm still lake reflecting a storm cloud above it, symbolic wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Bài học phụ: người thầy vẫn ở trong học trò. Nagato và Naruto là hai học trò của cùng một người thầy. Một ngư…

```text
Wide 16:9 landscape cinematic frame. two small books with identical covers side by side, one faded and torn, one intact and glowing faintly, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và một bài học không thuộc về chiến thuật: đôi khi chiến thắng lớn nhất là không đánh đòn cuối cùng.

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently placing a chess king piece back upright instead of knocking it over. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Trận Naruto đấu Pain bắt đầu bằng một ngôi làng bị san phẳng, và kết thúc bằng một ngôi làng được hồi sinh. G…

```text
Wide 16:9 landscape cinematic frame. a village being rebuilt at dawn with scaffolding and people working together, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Bạn nghĩ sao về lựa chọn của Naruto? Nếu là bạn, bạn có tha cho Nagato không? Viết vào bình luận nhé, Kaku rấ…

```text
Wide 16:9 landscape cinematic frame. a comment card on parchment with a small open hand doodle and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Và đúng câu hỏi đó sẽ trở lại trong video tiếp theo: Kaku mở một phiên tòa, bị cáo là Lelouch của Code Geass.…

```text
Wide 16:9 landscape cinematic frame. a courtroom gavel resting on a chess board with a black king piece, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video phân tích trận đấu như thế này, hãy đăng ký kênh. Kaku sẽ tiếp tục mổ xẻ từng hiệp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up a tactical map and bowing respectfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 126 giây · cảnh s01–s12 · 1642 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói trọn arc Pain tấn công làng Lá, tức manga chương 413 tới 453, và Naruto Shippuden khoảng tập 152 tới 175. Kể cả quá khứ của Nagato.

<short pause> Một ngôi làng bị san phẳng chỉ trong một đòn. Không còn nhà, không còn tường, chỉ còn một hố sâu khổng lồ ở chính giữa. Và giữa hố là một người đàn ông đứng một mình.

<short pause> Rồi một tiếng động vang lên. Một làn khói bốc lên ở rìa hố. Người anh hùng của làng vừa trở về, cưỡi trên lưng những con cóc khổng lồ.

<short pause> Đây là Naruto đấu với Pain, một trong những trận được người xem tìm kiếm nhiều nhất của cả loạt Naruto. <short pause> Nhưng nếu chỉ nhớ nó là một trận đánh đẹp, bạn đang bỏ lỡ một nửa.

<short pause> Vì đây là một trận đấu chiến thuật: thông tin, chuẩn bị, và cả kiểm soát cảm xúc. Và nó kết thúc theo một cách mà không trận shounen nào trước đó dám làm.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku phân tích trận Naruto đấu Pain, từng hiệp một: mục tiêu, lựa chọn, và cái giá. Cuối video là ba bài học chiến thuật.

<short pause> Trước trận, gần như mọi thứ đều nghiêng về phía Pain. Hãy xem hồ sơ hai bên.

<short pause> Pain: thủ lĩnh Akatsuki, sở hữu đôi mắt Luân Hồi Nhãn. Hắn điều khiển sáu thân xác cùng lúc, mỗi thân xác một năng lực khác nhau, và cả sáu nhìn thấy những gì các thân khác thấy.

<short pause> Hắn vừa giết Jiraiya, thầy của Naruto và là một trong ba Ninja huyền thoại. Hắn vừa san phẳng cả làng Lá bằng một đòn duy nhất.

<short pause> Naruto: vừa hoàn thành khóa luyện tập Hiền nhân ở núi Myoboku. Cậu có một sức mạnh mới, nhưng chưa từng dùng trong một trận thật.

<short pause> Nếu hỏi người trong làng lúc đó, gần như ai cũng sẽ đặt cược vào Pain. Và Kaku cũng vậy, nếu chỉ nhìn trên giấy.

<short pause> Nhưng Naruto có một thứ Pain không biết: một manh mối từ người thầy đã chết.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói trọn arc Pain tấn công làng Lá, tức manga chương 413 tới 453, và Naruto Shippuden khoảng tập 152 tới 175. Kể cả quá khứ của Nagato.

[pause] Một ngôi làng bị san phẳng chỉ trong một đòn. Không còn nhà, không còn tường, chỉ còn một hố sâu khổng lồ ở chính giữa. Và giữa hố là một người đàn ông đứng một mình.

[pause] Rồi một tiếng động vang lên. Một làn khói bốc lên ở rìa hố. Người anh hùng của làng vừa trở về, cưỡi trên lưng những con cóc khổng lồ.

[pause] Đây là Naruto đấu với Pain, một trong những trận được người xem tìm kiếm nhiều nhất của cả loạt Naruto. [pause] Nhưng nếu chỉ nhớ nó là một trận đánh đẹp, bạn đang bỏ lỡ một nửa.

[pause] Vì đây là một trận đấu chiến thuật: thông tin, chuẩn bị, và cả kiểm soát cảm xúc. Và nó kết thúc theo một cách mà không trận shounen nào trước đó dám làm.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku phân tích trận Naruto đấu Pain, từng hiệp một: mục tiêu, lựa chọn, và cái giá. Cuối video là ba bài học chiến thuật.

[pause] Trước trận, gần như mọi thứ đều nghiêng về phía Pain. Hãy xem hồ sơ hai bên.

[pause] Pain: thủ lĩnh Akatsuki, sở hữu đôi mắt Luân Hồi Nhãn. Hắn điều khiển sáu thân xác cùng lúc, mỗi thân xác một năng lực khác nhau, và cả sáu nhìn thấy những gì các thân khác thấy.

[pause] Hắn vừa giết Jiraiya, thầy của Naruto và là một trong ba Ninja huyền thoại. Hắn vừa san phẳng cả làng Lá bằng một đòn duy nhất.

[pause] Naruto: vừa hoàn thành khóa luyện tập Hiền nhân ở núi Myoboku. Cậu có một sức mạnh mới, nhưng chưa từng dùng trong một trận thật.

[pause] Nếu hỏi người trong làng lúc đó, gần như ai cũng sẽ đặt cược vào Pain. Và Kaku cũng vậy, nếu chỉ nhìn trên giấy.

[pause] Nhưng Naruto có một thứ Pain không biết: một manh mối từ người thầy đã chết.
```

### c02 · Hồ sơ sáu thân xác / Làng Lá trước khi Naruto về / Hiệp 0: manh mối của Jiraiya

Khoảng 139 giây · cảnh s13–s25 · 1810 ký tự

**Gemini**

```text
Trước khi vào trận, Kaku mở nhanh hồ sơ sáu thân xác của Pain, vì mỗi thân là một bài toán riêng mà Naruto phải giải.

<short pause> Thiên Đạo: điều khiển lực đẩy và lực hút. Đây là thân xác mạnh nhất, và cũng là bộ mặt mà cả thế giới biết tới dưới cái tên Pain.

<short pause> Tu La Đạo: thân xác như một cỗ máy, gắn vũ khí khắp người, bắn tên lửa và lưỡi dao. Súc Sinh Đạo: triệu hồi những con thú khổng lồ.

<short pause> Nhân Đạo: đọc ký ức và rút linh hồn chỉ bằng một cái chạm. Ngạ Quỷ Đạo: hút mọi loại chakra và thuật nhẫn.

<short pause> Địa Ngục Đạo: triệu hồi một thực thể có thể hồi phục các thân xác khác. Đây là lý do phải hạ nó, nếu không các thân khác sẽ đứng dậy mãi.

<short pause> Sáu thân xác, sáu năng lực, và chúng thấy những gì nhau thấy. Đánh một chọi sáu mà sáu cùng một bộ não, đó là bài toán Naruto phải giải.

<short pause> Trước khi Naruto trở về, làng Lá đã chiến đấu. Kakashi đấu với nhiều thân xác cùng lúc, và chính trong trận đó ông phát hiện ra khoảng nghỉ năm giây.

<short pause> Hokage Tsunade dùng rất nhiều năng lượng của mình để cùng Katsuyu, con sên triệu hồi, chia nhỏ thân mình bao bọc và chữa trị cho dân làng khi làng bị san phẳng.

<short pause> Nhờ vậy, dù cả làng bị san phẳng, rất nhiều người vẫn sống sót. Kaku thấy đây là một chi tiết hay bị bỏ qua: trận của Naruto chỉ có thể xảy ra vì những người khác đã giữ làng tới lúc cậu về.

<short pause> Trước khi chết, Jiraiya đã chiến đấu với Pain và phát hiện ra một bí mật. Ông không kịp nói ra, nên để lại một mật mã trên lưng một con cóc.

<short pause> Mật mã được giải: người thật không nằm trong số đó. Nghĩa là sáu thân xác không phải Pain thật. Có một người đang điều khiển chúng từ nơi khác.

<short pause> Đây là hiệp quan trọng nhất, dù không có cú đấm nào. Nhờ Jiraiya, Naruto biết rằng đánh bại sáu thân xác chưa phải là kết thúc.

<short pause> <laugh> Kaku để ý: Jiraiya dùng cả mạng sống của mình để đổi lấy một câu. Và câu đó quyết định cả trận đấu. Thông tin là vũ khí mạnh nhất trong trận này.
```

**ElevenLabs**

```text
Trước khi vào trận, Kaku mở nhanh hồ sơ sáu thân xác của Pain, vì mỗi thân là một bài toán riêng mà Naruto phải giải.

[pause] Thiên Đạo: điều khiển lực đẩy và lực hút. Đây là thân xác mạnh nhất, và cũng là bộ mặt mà cả thế giới biết tới dưới cái tên Pain.

[pause] Tu La Đạo: thân xác như một cỗ máy, gắn vũ khí khắp người, bắn tên lửa và lưỡi dao. Súc Sinh Đạo: triệu hồi những con thú khổng lồ.

[pause] Nhân Đạo: đọc ký ức và rút linh hồn chỉ bằng một cái chạm. Ngạ Quỷ Đạo: hút mọi loại chakra và thuật nhẫn.

[pause] Địa Ngục Đạo: triệu hồi một thực thể có thể hồi phục các thân xác khác. Đây là lý do phải hạ nó, nếu không các thân khác sẽ đứng dậy mãi.

[pause] Sáu thân xác, sáu năng lực, và chúng thấy những gì nhau thấy. Đánh một chọi sáu mà sáu cùng một bộ não, đó là bài toán Naruto phải giải.

[pause] Trước khi Naruto trở về, làng Lá đã chiến đấu. Kakashi đấu với nhiều thân xác cùng lúc, và chính trong trận đó ông phát hiện ra khoảng nghỉ năm giây.

[pause] Hokage Tsunade dùng rất nhiều năng lượng của mình để cùng Katsuyu, con sên triệu hồi, chia nhỏ thân mình bao bọc và chữa trị cho dân làng khi làng bị san phẳng.

[pause] Nhờ vậy, dù cả làng bị san phẳng, rất nhiều người vẫn sống sót. Kaku thấy đây là một chi tiết hay bị bỏ qua: trận của Naruto chỉ có thể xảy ra vì những người khác đã giữ làng tới lúc cậu về.

[pause] Trước khi chết, Jiraiya đã chiến đấu với Pain và phát hiện ra một bí mật. Ông không kịp nói ra, nên để lại một mật mã trên lưng một con cóc.

[pause] Mật mã được giải: người thật không nằm trong số đó. Nghĩa là sáu thân xác không phải Pain thật. Có một người đang điều khiển chúng từ nơi khác.

[pause] Đây là hiệp quan trọng nhất, dù không có cú đấm nào. Nhờ Jiraiya, Naruto biết rằng đánh bại sáu thân xác chưa phải là kết thúc.

[pause] [chuckles] Kaku để ý: Jiraiya dùng cả mạng sống của mình để đổi lấy một câu. Và câu đó quyết định cả trận đấu. Thông tin là vũ khí mạnh nhất trong trận này.
```

### c03 · Hiệp 1: Hiền nhân xuất hiện / Hiệp 2: điểm yếu của Hiền nhân

Khoảng 154 giây · cảnh s26–s40 · 1997 ký tự

**Gemini**

```text
Mục tiêu của Naruto ở hiệp một: hạ từng thân xác một, trước khi chúng phối hợp được với nhau.

<short pause> Chế độ Hiền nhân cho Naruto sức mạnh thể chất lớn hơn, cảm nhận được xung quanh, và một thứ đặc biệt: đòn đánh của cậu có một vùng ảnh hưởng rộng hơn cả nắm tay.

<short pause> Naruto hạ được thân xác Tu La Đạo, thân xác máy móc với vũ khí gắn khắp người, bằng một đòn Rasengan khổng lồ.

<short pause> Rồi tới Ngạ Quỷ Đạo, thân xác có thể hút mọi loại chakra. Nó tóm lấy Naruto để hút năng lượng.

<short pause> Nhưng năng lượng Hiền nhân là năng lượng tự nhiên, và cơ thể người thường không chịu nổi. Ngạ Quỷ Đạo hút vào, rồi hóa đá thành một bức tượng cóc.

<short pause> Kaku rất thích chi tiết này. Naruto không cần đánh. Chính luật của năng lượng tự nhiên đánh bại đối thủ. Đây là thắng bằng hiểu biết, không phải bằng sức mạnh.

<short pause> Những con cóc khổng lồ cũng không đứng ngoài. Chúng chiến đấu cùng Naruto, và các lão cóc Hiền nhân ngồi trên vai cậu, giúp cậu hợp nhất năng lượng tự nhiên.

<short pause> Hiệp một thuộc về Naruto. <short pause> Nhưng Pain vẫn còn bốn thân xác, và hắn bắt đầu hiểu sức mạnh mới của đối thủ.

<short pause> Nhưng chế độ Hiền nhân có một điểm yếu chí mạng: nó không kéo dài lâu. Muốn nạp lại năng lượng tự nhiên, Naruto phải ngồi yên hoàn toàn.

<short pause> Và ngồi yên giữa chiến trường với sáu kẻ thù thì gần như tự sát. Đây là vấn đề mà cả người thầy Jiraiya cũng chưa giải quyết được.

<short pause> Giải pháp của Naruto rất thông minh: cậu để các phân thân bóng ngồi yên ở núi Myoboku, gom năng lượng tự nhiên. Khi bản thể cần, cậu hủy một phân thân, và năng lượng chuyển về.

<short pause> Nhưng chỉ có một số lượng phân thân giới hạn. Mỗi lần dùng một cái là một lần nạp. Naruto phải tính toán rất kỹ.

<short pause> Với năng lượng được nạp, Naruto dùng Phong độn Rasen Shuriken, lần này có thể ném đi, hạ hai thân xác Nhân Đạo và Súc Sinh Đạo cùng lúc.

<short pause> Địa Ngục Đạo, thân xác có thể hồi sinh các thân khác, cũng không trụ được. Naruto đã đi qua năm trên sáu thân xác.

<short pause> Kaku đánh giá: hiệp hai là chiến thắng của sự chuẩn bị. Naruto thua Jiraiya về kinh nghiệm, nhưng hơn ở chỗ biết dùng thế mạnh riêng của mình, phân thân, để vá điểm yếu.
```

**ElevenLabs**

```text
Mục tiêu của Naruto ở hiệp một: hạ từng thân xác một, trước khi chúng phối hợp được với nhau.

[pause] Chế độ Hiền nhân cho Naruto sức mạnh thể chất lớn hơn, cảm nhận được xung quanh, và một thứ đặc biệt: đòn đánh của cậu có một vùng ảnh hưởng rộng hơn cả nắm tay.

[pause] Naruto hạ được thân xác Tu La Đạo, thân xác máy móc với vũ khí gắn khắp người, bằng một đòn Rasengan khổng lồ.

[pause] Rồi tới Ngạ Quỷ Đạo, thân xác có thể hút mọi loại chakra. Nó tóm lấy Naruto để hút năng lượng.

[pause] Nhưng năng lượng Hiền nhân là năng lượng tự nhiên, và cơ thể người thường không chịu nổi. Ngạ Quỷ Đạo hút vào, rồi hóa đá thành một bức tượng cóc.

[pause] Kaku rất thích chi tiết này. Naruto không cần đánh. Chính luật của năng lượng tự nhiên đánh bại đối thủ. Đây là thắng bằng hiểu biết, không phải bằng sức mạnh.

[pause] Những con cóc khổng lồ cũng không đứng ngoài. Chúng chiến đấu cùng Naruto, và các lão cóc Hiền nhân ngồi trên vai cậu, giúp cậu hợp nhất năng lượng tự nhiên.

[pause] Hiệp một thuộc về Naruto. [pause] Nhưng Pain vẫn còn bốn thân xác, và hắn bắt đầu hiểu sức mạnh mới của đối thủ.

[pause] Nhưng chế độ Hiền nhân có một điểm yếu chí mạng: nó không kéo dài lâu. Muốn nạp lại năng lượng tự nhiên, Naruto phải ngồi yên hoàn toàn.

[pause] Và ngồi yên giữa chiến trường với sáu kẻ thù thì gần như tự sát. Đây là vấn đề mà cả người thầy Jiraiya cũng chưa giải quyết được.

[pause] Giải pháp của Naruto rất thông minh: cậu để các phân thân bóng ngồi yên ở núi Myoboku, gom năng lượng tự nhiên. Khi bản thể cần, cậu hủy một phân thân, và năng lượng chuyển về.

[pause] Nhưng chỉ có một số lượng phân thân giới hạn. Mỗi lần dùng một cái là một lần nạp. Naruto phải tính toán rất kỹ.

[pause] Với năng lượng được nạp, Naruto dùng Phong độn Rasen Shuriken, lần này có thể ném đi, hạ hai thân xác Nhân Đạo và Súc Sinh Đạo cùng lúc.

[pause] Địa Ngục Đạo, thân xác có thể hồi sinh các thân khác, cũng không trụ được. Naruto đã đi qua năm trên sáu thân xác.

[pause] Kaku đánh giá: hiệp hai là chiến thắng của sự chuẩn bị. Naruto thua Jiraiya về kinh nghiệm, nhưng hơn ở chỗ biết dùng thế mạnh riêng của mình, phân thân, để vá điểm yếu.
```

### c04 · Hiệp 3: Thiên Đạo và cái bẫy

Khoảng 70 giây · cảnh s41–s47 · 911 ký tự

**Gemini**

```text
Chỉ còn lại Thiên Đạo, thân xác mạnh nhất. Năng lực của nó: đẩy mọi thứ ra xa, hoặc kéo mọi thứ lại gần.

<short pause> Chính năng lực đẩy này, Thần La Thiên Chinh, đã san phẳng cả làng Lá. Ở quy mô nhỏ, nó biến Thiên Đạo thành gần như bất khả xâm phạm.

<short pause> Nhưng có một thông tin quý giá. Trước đó, Kakashi đã phát hiện ra: giữa hai lần dùng Thần La Thiên Chinh, Thiên Đạo cần khoảng năm giây để hồi.

<short pause> Kakashi đã ngã xuống trong trận trước đó, nhưng thông tin ông tìm được vẫn được truyền đi. Lại một lần nữa, một người đã mất để lại vũ khí cho người còn sống.

<short pause> Nhưng Pain cũng không đứng yên. Hắn ghim Naruto xuống đất bằng những thanh kim loại truyền chakra, khiến cậu không cử động được.

<short pause> Những thanh kim loại đó chính là thứ Nagato dùng để truyền chakra điều khiển sáu thân xác. Bị ghim bằng chúng, Naruto không chỉ bị trói, mà còn bị nhiễu loạn năng lượng.

<short pause> Hiệp ba thuộc về Pain. Naruto bị bắt, và có vẻ như mọi chuẩn bị đã không đủ.
```

**ElevenLabs**

```text
Chỉ còn lại Thiên Đạo, thân xác mạnh nhất. Năng lực của nó: đẩy mọi thứ ra xa, hoặc kéo mọi thứ lại gần.

[pause] Chính năng lực đẩy này, Thần La Thiên Chinh, đã san phẳng cả làng Lá. Ở quy mô nhỏ, nó biến Thiên Đạo thành gần như bất khả xâm phạm.

[pause] Nhưng có một thông tin quý giá. Trước đó, Kakashi đã phát hiện ra: giữa hai lần dùng Thần La Thiên Chinh, Thiên Đạo cần khoảng năm giây để hồi.

[pause] Kakashi đã ngã xuống trong trận trước đó, nhưng thông tin ông tìm được vẫn được truyền đi. Lại một lần nữa, một người đã mất để lại vũ khí cho người còn sống.

[pause] Nhưng Pain cũng không đứng yên. Hắn ghim Naruto xuống đất bằng những thanh kim loại truyền chakra, khiến cậu không cử động được.

[pause] Những thanh kim loại đó chính là thứ Nagato dùng để truyền chakra điều khiển sáu thân xác. Bị ghim bằng chúng, Naruto không chỉ bị trói, mà còn bị nhiễu loạn năng lượng.

[pause] Hiệp ba thuộc về Pain. Naruto bị bắt, và có vẻ như mọi chuẩn bị đã không đủ.
```

### c05 · Hiệp 4: cơn giận và cánh cửa

Khoảng 92 giây · cảnh s48–s56 · 1193 ký tự

**Gemini**

```text
Và rồi Hinata xuất hiện. Cô bé nhút nhát, người luôn dõi theo Naruto từ xa, bước ra một mình để bảo vệ cậu.

<short pause> Hinata nói ra điều cô giữ trong lòng suốt nhiều năm: cô thích Naruto. Rồi cô chiến đấu, dù biết mình không có cơ hội thắng.

<short pause> Pain hạ gục Hinata. Kaku không mô tả chi tiết. Chỉ cần biết: Naruto nhìn thấy, và trong cậu có thứ gì đó vỡ ra.

<short pause> Cơn giận làm Cửu Vĩ bên trong Naruto trỗi dậy. Sáu đuôi, rồi tám đuôi. Cậu mất dần kiểm soát, và sức mạnh hủy diệt tràn ra.

<short pause> Pain đáp trả bằng Địa Bạo Thiên Tinh: hắn tạo ra một khối cầu khổng lồ, kéo đất đá xung quanh vào, định giam cầm cả sinh vật bên trong.

<short pause> Và ở tận sâu trong tâm trí Naruto, khi cậu gần mở phong ấn cuối cùng, một người xuất hiện: cha của cậu, Minato, Hokage đệ tứ.

<short pause> Minato đã cài sẵn một phần chakra của mình vào phong ấn, để xuất hiện đúng lúc con trai cần. Ông sửa lại phong ấn, và lần đầu tiên hai cha con nói chuyện với nhau.

<short pause> Minato cũng nói với Naruto rằng ông tin con trai mình sẽ tìm ra câu trả lời mà thế hệ của ông chưa tìm được. Một lời tin tưởng, không phải một mệnh lệnh.

<short pause> <laugh> Kaku thấy hiệp bốn là trận thua lớn nhất của Naruto, không phải vì Pain, mà vì cơn giận của chính cậu. Và nó được cứu bởi người cha mà cậu chưa từng gặp.
```

**ElevenLabs**

```text
Và rồi Hinata xuất hiện. Cô bé nhút nhát, người luôn dõi theo Naruto từ xa, bước ra một mình để bảo vệ cậu.

[pause] Hinata nói ra điều cô giữ trong lòng suốt nhiều năm: cô thích Naruto. Rồi cô chiến đấu, dù biết mình không có cơ hội thắng.

[pause] Pain hạ gục Hinata. Kaku không mô tả chi tiết. Chỉ cần biết: Naruto nhìn thấy, và trong cậu có thứ gì đó vỡ ra.

[pause] Cơn giận làm Cửu Vĩ bên trong Naruto trỗi dậy. Sáu đuôi, rồi tám đuôi. Cậu mất dần kiểm soát, và sức mạnh hủy diệt tràn ra.

[pause] Pain đáp trả bằng Địa Bạo Thiên Tinh: hắn tạo ra một khối cầu khổng lồ, kéo đất đá xung quanh vào, định giam cầm cả sinh vật bên trong.

[pause] Và ở tận sâu trong tâm trí Naruto, khi cậu gần mở phong ấn cuối cùng, một người xuất hiện: cha của cậu, Minato, Hokage đệ tứ.

[pause] Minato đã cài sẵn một phần chakra của mình vào phong ấn, để xuất hiện đúng lúc con trai cần. Ông sửa lại phong ấn, và lần đầu tiên hai cha con nói chuyện với nhau.

[pause] Minato cũng nói với Naruto rằng ông tin con trai mình sẽ tìm ra câu trả lời mà thế hệ của ông chưa tìm được. Một lời tin tưởng, không phải một mệnh lệnh.

[pause] [chuckles] Kaku thấy hiệp bốn là trận thua lớn nhất của Naruto, không phải vì Pain, mà vì cơn giận của chính cậu. Và nó được cứu bởi người cha mà cậu chưa từng gặp.
```

### c06 · Hiệp 5: năm giây

Khoảng 70 giây · cảnh s57–s63 · 905 ký tự

**Gemini**

```text
Naruto trở lại, bình tĩnh hơn, với phân thân cuối cùng trong chế độ Hiền nhân. Mục tiêu của hiệp cuối: tận dụng đúng năm giây.

<short pause> Naruto tung một phân thân tấn công trước. Thiên Đạo dùng Thần La Thiên Chinh để đẩy nó đi. Và đồng hồ bắt đầu đếm.

<short pause> Đây chính là cách thông tin của Kakashi được biến thành chiến thuật. Biết đối thủ có năm giây trống là một chuyện. Tạo ra năm giây đó đúng lúc mình cần là chuyện khác.

<short pause> Trong năm giây đó, Naruto thật lao tới từ một hướng khác. Thiên Đạo không thể đẩy nữa, và buộc phải đỡ đòn trực diện.

<short pause> Rasengan trúng đích. Thân xác cuối cùng ngã xuống. Hiệp năm, và trận đấu trên chiến trường, thuộc về Naruto.

<short pause> Và hãy nhớ, lúc này Naruto đã không còn nhiều phân thân dự trữ. Nếu đòn này hụt, trận đấu có thể đã kết thúc theo cách khác.

<short pause> Kaku để ý: đòn quyết định không phải là đòn mạnh nhất. Nó là một đòn Rasengan cơ bản, thứ Naruto đã học từ rất lâu. Đúng thời điểm đánh bại sức mạnh.
```

**ElevenLabs**

```text
Naruto trở lại, bình tĩnh hơn, với phân thân cuối cùng trong chế độ Hiền nhân. Mục tiêu của hiệp cuối: tận dụng đúng năm giây.

[pause] Naruto tung một phân thân tấn công trước. Thiên Đạo dùng Thần La Thiên Chinh để đẩy nó đi. Và đồng hồ bắt đầu đếm.

[pause] Đây chính là cách thông tin của Kakashi được biến thành chiến thuật. Biết đối thủ có năm giây trống là một chuyện. Tạo ra năm giây đó đúng lúc mình cần là chuyện khác.

[pause] Trong năm giây đó, Naruto thật lao tới từ một hướng khác. Thiên Đạo không thể đẩy nữa, và buộc phải đỡ đòn trực diện.

[pause] Rasengan trúng đích. Thân xác cuối cùng ngã xuống. Hiệp năm, và trận đấu trên chiến trường, thuộc về Naruto.

[pause] Và hãy nhớ, lúc này Naruto đã không còn nhiều phân thân dự trữ. Nếu đòn này hụt, trận đấu có thể đã kết thúc theo cách khác.

[pause] Kaku để ý: đòn quyết định không phải là đòn mạnh nhất. Nó là một đòn Rasengan cơ bản, thứ Naruto đã học từ rất lâu. Đúng thời điểm đánh bại sức mạnh.
```

### c07 · Sau trận: người thật / Sơ đồ chiến thuật

Khoảng 139 giây · cảnh s64–s75 · 1810 ký tự

**Gemini**

```text
Nhưng nhớ lại mật mã của Jiraiya: người thật không nằm trong số đó. Naruto quyết định đi tìm người điều khiển sáu thân xác. Một mình.

<short pause> Người thật là Nagato, một người từng là học trò của Jiraiya, giống như Naruto. Cơ thể ông gầy yếu, bị gắn vào một cỗ máy, điều khiển sáu thân xác từ xa.

<short pause> Nagato kể quá khứ của mình: chiến tranh đã cướp đi cha mẹ, bạn bè, và cả hy vọng của ông. Ông tin rằng chỉ có nỗi đau mới khiến con người hiểu nhau.

<short pause> Nagato hỏi Naruto một câu: vậy cậu sẽ làm gì để mang lại hòa bình? Và Naruto thừa nhận: cậu chưa có câu trả lời. <short pause> Nhưng cậu sẽ tìm, và sẽ không từ bỏ.

<short pause> Đây là lúc Naruto phải lựa chọn khó nhất trận. Người trước mặt đã giết thầy cậu, phá hủy làng cậu. Cậu có thể kết thúc mọi thứ ngay bây giờ.

<short pause> Nhưng Naruto chọn không giết. Cậu nói rằng nếu cậu trả thù, vòng lặp hận thù sẽ tiếp tục. Cậu tin vào điều mà Jiraiya từng tin: một ngày nào đó, con người sẽ hiểu nhau.

<short pause> Nagato bị thuyết phục. Ông dùng hết sức lực cuối cùng để thi triển một thuật hồi sinh, đưa những người đã chết ở làng Lá trở lại. Rồi ông ra đi.

<short pause> Konan, người bạn đồng hành của Nagato, tin vào lựa chọn của Naruto. Cô mang thi thể của bạn mình đi, và để lại cho Naruto một bó hoa giấy như lời chúc.

<short pause> Naruto trở về làng không phải như một chiến binh thắng trận, mà như một người hùng được cả làng chào đón. Cậu bé từng bị cả làng xa lánh, giờ được cả làng tung hô.

<short pause> Tổng kết trận đấu trên một sơ đồ. Hiệp không: thông tin từ Jiraiya. Hiệp một: Hiền nhân và Ngạ Quỷ Đạo hóa đá. Hiệp hai: phân thân dự trữ, Rasen Shuriken.

<short pause> Hiệp ba: Pain ghim Naruto. Hiệp bốn: Hinata, Cửu Vĩ, và Minato. Hiệp năm: năm giây và một Rasengan. Sau trận: một cuộc nói chuyện thay vì một đòn đánh.

<short pause> Điểm số theo hiệp: Naruto thắng hiệp không, một, hai, năm. Pain thắng hiệp ba và gần như thắng hiệp bốn. <short pause> Nhưng trận thật sự được quyết định sau tiếng chuông.
```

**ElevenLabs**

```text
Nhưng nhớ lại mật mã của Jiraiya: người thật không nằm trong số đó. Naruto quyết định đi tìm người điều khiển sáu thân xác. Một mình.

[pause] Người thật là Nagato, một người từng là học trò của Jiraiya, giống như Naruto. Cơ thể ông gầy yếu, bị gắn vào một cỗ máy, điều khiển sáu thân xác từ xa.

[pause] Nagato kể quá khứ của mình: chiến tranh đã cướp đi cha mẹ, bạn bè, và cả hy vọng của ông. Ông tin rằng chỉ có nỗi đau mới khiến con người hiểu nhau.

[pause] [curious] Nagato hỏi Naruto một câu: vậy cậu sẽ làm gì để mang lại hòa bình? Và Naruto thừa nhận: cậu chưa có câu trả lời. [pause] Nhưng cậu sẽ tìm, và sẽ không từ bỏ.

[pause] Đây là lúc Naruto phải lựa chọn khó nhất trận. Người trước mặt đã giết thầy cậu, phá hủy làng cậu. Cậu có thể kết thúc mọi thứ ngay bây giờ.

[pause] Nhưng Naruto chọn không giết. Cậu nói rằng nếu cậu trả thù, vòng lặp hận thù sẽ tiếp tục. Cậu tin vào điều mà Jiraiya từng tin: một ngày nào đó, con người sẽ hiểu nhau.

[pause] Nagato bị thuyết phục. Ông dùng hết sức lực cuối cùng để thi triển một thuật hồi sinh, đưa những người đã chết ở làng Lá trở lại. Rồi ông ra đi.

[pause] Konan, người bạn đồng hành của Nagato, tin vào lựa chọn của Naruto. Cô mang thi thể của bạn mình đi, và để lại cho Naruto một bó hoa giấy như lời chúc.

[pause] Naruto trở về làng không phải như một chiến binh thắng trận, mà như một người hùng được cả làng chào đón. Cậu bé từng bị cả làng xa lánh, giờ được cả làng tung hô.

[pause] Tổng kết trận đấu trên một sơ đồ. Hiệp không: thông tin từ Jiraiya. Hiệp một: Hiền nhân và Ngạ Quỷ Đạo hóa đá. Hiệp hai: phân thân dự trữ, Rasen Shuriken.

[pause] Hiệp ba: Pain ghim Naruto. Hiệp bốn: Hinata, Cửu Vĩ, và Minato. Hiệp năm: năm giây và một Rasengan. Sau trận: một cuộc nói chuyện thay vì một đòn đánh.

[pause] Điểm số theo hiệp: Naruto thắng hiệp không, một, hai, năm. Pain thắng hiệp ba và gần như thắng hiệp bốn. [pause] Nhưng trận thật sự được quyết định sau tiếng chuông.
```

### c08 · Ba bài học chiến thuật / Kết

Khoảng 113 giây · cảnh s76–s85 · 1467 ký tự

**Gemini**

```text
Bài học một: thông tin thắng sức mạnh. Mật mã của Jiraiya và năm giây của Kakashi quyết định trận đấu nhiều hơn bất kỳ kỹ thuật nào.

<short pause> Bài học hai: dùng thế mạnh của mình để vá điểm yếu. Naruto không sửa được điểm yếu của chế độ Hiền nhân, nhưng cậu dùng phân thân, thứ cậu giỏi nhất, để bù vào.

<short pause> Và điều đáng nói: Naruto không giỏi kiểm soát cảm xúc một mình. Cậu được cứu bởi người cha. Kiểm soát cảm xúc đôi khi cũng cần có người bên cạnh.

<short pause> Bài học ba: kiểm soát cảm xúc. Khoảnh khắc Naruto gần thua nhất không phải khi bị ghim, mà khi cơn giận chiếm lấy cậu.

<short pause> Bài học phụ: người thầy vẫn ở trong học trò. Nagato và Naruto là hai học trò của cùng một người thầy. Một người mất niềm tin, một người giữ được. Và người giữ được đã nhắc lại cho người kia.

<short pause> Và một bài học không thuộc về chiến thuật: đôi khi chiến thắng lớn nhất là không đánh đòn cuối cùng.

<short pause> Trận Naruto đấu Pain bắt đầu bằng một ngôi làng bị san phẳng, và kết thúc bằng một ngôi làng được hồi sinh. Giữa hai điều đó là một cậu bé học cách phá vỡ vòng lặp hận thù.

<short pause> Bạn nghĩ sao về lựa chọn của Naruto? Nếu là bạn, bạn có tha cho Nagato không? Viết vào bình luận nhé, Kaku rất muốn đọc.

<short pause> Và đúng câu hỏi đó sẽ trở lại trong video tiếp theo: Kaku mở một phiên tòa, bị cáo là Lelouch của Code Geass. Người muốn thay đổi thế giới có được phép dùng mọi cách?

<short pause> Nếu bạn thích những video phân tích trận đấu như thế này, hãy đăng ký kênh. <laugh> Kaku sẽ tiếp tục mổ xẻ từng hiệp của những trận kinh điển. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Bài học một: thông tin thắng sức mạnh. Mật mã của Jiraiya và năm giây của Kakashi quyết định trận đấu nhiều hơn bất kỳ kỹ thuật nào.

[pause] Bài học hai: dùng thế mạnh của mình để vá điểm yếu. Naruto không sửa được điểm yếu của chế độ Hiền nhân, nhưng cậu dùng phân thân, thứ cậu giỏi nhất, để bù vào.

[pause] Và điều đáng nói: Naruto không giỏi kiểm soát cảm xúc một mình. Cậu được cứu bởi người cha. Kiểm soát cảm xúc đôi khi cũng cần có người bên cạnh.

[pause] Bài học ba: kiểm soát cảm xúc. Khoảnh khắc Naruto gần thua nhất không phải khi bị ghim, mà khi cơn giận chiếm lấy cậu.

[pause] Bài học phụ: người thầy vẫn ở trong học trò. Nagato và Naruto là hai học trò của cùng một người thầy. Một người mất niềm tin, một người giữ được. Và người giữ được đã nhắc lại cho người kia.

[pause] Và một bài học không thuộc về chiến thuật: đôi khi chiến thắng lớn nhất là không đánh đòn cuối cùng.

[pause] Trận Naruto đấu Pain bắt đầu bằng một ngôi làng bị san phẳng, và kết thúc bằng một ngôi làng được hồi sinh. Giữa hai điều đó là một cậu bé học cách phá vỡ vòng lặp hận thù.

[pause] [curious] Bạn nghĩ sao về lựa chọn của Naruto? Nếu là bạn, bạn có tha cho Nagato không? Viết vào bình luận nhé, Kaku rất muốn đọc.

[pause] Và đúng câu hỏi đó sẽ trở lại trong video tiếp theo: Kaku mở một phiên tòa, bị cáo là Lelouch của Code Geass. Người muốn thay đổi thế giới có được phép dùng mọi cách?

[pause] Nếu bạn thích những video phân tích trận đấu như thế này, hãy đăng ký kênh. [chuckles] Kaku sẽ tiếp tục mổ xẻ từng hiệp của những trận kinh điển. Kaku gấp sổ đây, hẹn gặp lại!
```
