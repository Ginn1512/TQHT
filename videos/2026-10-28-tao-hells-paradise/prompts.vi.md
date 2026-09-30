# Bộ prompt · Hell's Paradise: Đạo, ngũ hành và âm dương hoạt động thế nào

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (80 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết anime Hell's Paradise mùa hai. Truyện có nhiều cảnh bạo lực, nhưng Ka…

```text
Wide 16:9 landscape cinematic frame. a closed ancient scroll tied with a red cord lying on a stone step beside strange flowers, spoiler card beside it, close-up, eerie soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một hòn đảo đầy hoa đẹp tới kỳ lạ, những bức tượng Phật khổng lồ, và những sinh vật bất tử. Ai đặt chân lên đ…

```text
Wide 16:9 landscape cinematic frame. a mysterious island covered in vivid flowers and giant stone statues rising from the mist, wide shot, eerie beautiful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Và để sống sót trên hòn đảo đó, con người phải hiểu một khái niệm mà người Việt nghe rất quen: Đạo, ngũ hành…

```text
Wide 16:9 landscape cinematic frame. a circular diagram of five elements drawn in ink with arrows connecting them, parchment close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Một chi tiết vui: tác giả Hell's Paradise tên là Kaku Yuji. Cùng tên với Kaku. Kaku không có họ hàng gì đâu,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly pointing at its own name tag with a tiny smug smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku giải thích Đạo trong Hell's Paradise: luật nền, ngũ hành, âm dương,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a scroll with a five-element circle diagram on it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Bối cảnh: hòn đảo Shinsenkyo

Lời: Hell's Paradise, hay Địa ngục cực lạc, là manga của Kaku Yuji, đăng trên Shonen Jump+ từ tháng một năm 2018 t…

```text
Wide 16:9 landscape cinematic frame. a small stack of manga volumes with flower-patterned spines beside a streaming remote, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Bối cảnh là Nhật Bản thời Edo. Tướng quân nghe tin về một hòn đảo xa, nơi có thuốc trường sinh. Nhưng mọi đoà…

```text
Wide 16:9 landscape cinematic frame. an Edo-period castle town at dusk with a messenger kneeling before a curtained palace hall, wide shot, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Mỗi tử tù là một kẻ nguy hiểm: ninja, samurai, thủ lĩnh cướp, kẻ lừa đảo. Mỗi đao phủ là một kiếm sĩ giỏi. Mộ…

```text
Wide 16:9 landscape cinematic frame. a line of mismatched figures standing on a beach, each paired with a sword-bearing guardian, wide shot, tense grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Vì vậy, tướng quân cử những tử tù ra đảo. Ai mang thuốc trường sinh về sẽ được tha tội. Mỗi tử tù đi cùng một…

```text
Wide 16:9 landscape cinematic frame. a row of small boats rowing away from a dark shore toward a misty island, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nhân vật chính là Gabimaru, một ninja được gọi là kẻ trống rỗng, người tưởng như không có cảm xúc. Nhưng cậu…

```text
Wide 16:9 landscape cinematic frame. a lone figure sitting on a rock by the sea at dusk, holding a small keepsake in his hand, back view, wide shot, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Người đi cùng cậu là Sagiri, một nữ đao phủ trẻ, luôn nghi ngờ chính mình vì phải cầm kiếm lấy mạng người. Ha…

```text
Wide 16:9 landscape cinematic frame. a young swordswoman standing alone in a bamboo grove with her sword sheathed, eyes lowered, medium shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Trên đảo, họ gặp những sinh vật đáng sợ nhất: Tiên nhân, những kẻ gần như bất tử, có thể tái tạo cơ thể. Và m…

```text
Wide 16:9 landscape cinematic frame. several tall elegant silhouettes standing among giant flowers in a misty garden, low-angle shot, eerie divine light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Một hòn đảo sống

Lời: Trước khi vào luật, hãy nhìn hòn đảo. Shinsenkyo đẹp như thiên đường: hoa nở khắp nơi, bướm bay, cây cối rực…

```text
Wide 16:9 landscape cinematic frame. a breathtaking island garden with giant blooming flowers and drifting butterflies, a faint shadow lurking between the petals, wide shot, eerie beautiful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Trên đảo có những sinh vật lạ, mang dáng dấp tượng thần tượng Phật, lai giữa người, thú và côn trùng. Chúng t…

```text
Wide 16:9 landscape cinematic frame. a strange hybrid creature silhouette with a serene stone-like face standing among tall flowers, low-angle shot, unsettling soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và cả những con người biến thành hoa. Kaku không mô tả chi tiết. Chỉ cần biết: thuốc trường sinh trên hòn đảo…

```text
Wide 16:9 landscape cinematic frame. a single enormous pale flower blooming in a dark clearing with mist curling around it, close-up, ominous soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Tất cả những điều kỳ lạ đó đều có chung một gốc: Đạo. Hòn đảo được xây dựng, và vận hành, bằng chính năng lượ…

```text
Wide 16:9 landscape cinematic frame. glowing threads of energy running through roots, flowers and stone statues across the island, symbolic wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là một ý tưởng rất hay. Hệ thống sức mạnh không chỉ để đánh nhau, mà còn giải thích vì sao cả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering nervously at a giant flower through a small magnifying glass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Luật nền: Đạo là gì?

Lời: Trong Hell's Paradise, Đạo là năng lượng sống chảy trong mọi sinh vật: con người, động vật, cây cỏ. Ai cũng c…

```text
Wide 16:9 landscape cinematic frame. a human silhouette with faint flowing lines of energy running through its body like rivers, symbolic diagram, soft glowing light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Luật một: Đạo có thể cảm nhận được. Người luyện tập có thể thấy luồng Đạo của người khác, đoán được họ mạnh h…

```text
Wide 16:9 landscape cinematic frame. a figure with closed eyes sensing faint glowing auras around several shadowy shapes in a dark forest, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Luật hai: Đạo có thể được tập trung để tăng sức mạnh cơ thể, gia cố vũ khí, hoặc chữa lành vết thương nhanh h…

```text
Wide 16:9 landscape cinematic frame. a sword blade glowing faintly as energy flows from the hand into it, dynamic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Trên đảo, những người mạnh thường là những người học được cách thở chậm, giữ bình tĩnh ngay cả khi đối mặt ng…

```text
Wide 16:9 landscape cinematic frame. a figure sitting cross-legged in meditation on a rock while chaos swirls faintly around, medium shot, calm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Luật ba: Đạo có thể bị cạn. Dùng quá nhiều, cơ thể kiệt sức. Đạo cũng dao động theo cảm xúc: sợ hãi, giận dữ…

```text
Wide 16:9 landscape cinematic frame. a candle flame flickering wildly in a draft beside a steady flame protected by a glass, close-up, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Đạo trong truyện giống chakra trong Naruto hay Khí trong Black Clover. Nhưng điểm khác biệt, và th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing three small cards labeled with simple energy icons side by side and tapping the last one. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Ngũ hành: năm thuộc tính

Lời: Mỗi người và mỗi sinh vật có một thuộc tính Đạo, thuộc một trong năm hành: Mộc, Hỏa, Thổ, Kim, Thủy.

```text
Wide 16:9 landscape cinematic frame. five small stones arranged in a circle on dark cloth, each carved with a different symbol: a leaf, a flame, a mountain, a blade, a wave, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Chẳng hạn, nhiều người Việt vẫn nghe ông bà nói người mệnh này hợp màu này, tuổi này hợp tuổi kia. Đó là cách…

```text
Wide 16:9 landscape cinematic frame. a grandmother pointing at a colorful chart on a calendar while a child listens curiously, medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nếu bạn lớn lên ở Việt Nam, rất có thể bạn đã nghe về ngũ hành qua ông bà, qua xem ngày, hay qua đông y. Hell…

```text
Wide 16:9 landscape cinematic frame. an old Vietnamese almanac book lying open on a wooden table beside a cup of tea, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và các hành tác động lẫn nhau theo hai vòng. Vòng thứ nhất là tương sinh: hành này nuôi dưỡng hành kia.

```text
Wide 16:9 landscape cinematic frame. a circle of five element symbols with green arrows flowing clockwise between them, parchment diagram, warm light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Mộc sinh Hỏa: gỗ cháy thành lửa. Hỏa sinh Thổ: lửa để lại tro thành đất. Thổ sinh Kim: trong đất có kim loại.…

```text
Wide 16:9 landscape cinematic frame. five small illustrated vignettes in a row: burning wood, ash on soil, ore in rock, dew on metal, water on a sprout, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Vòng thứ hai là tương khắc: hành này áp chế hành kia. Mộc khắc Thổ, Thổ khắc Thủy, Thủy khắc Hỏa, Hỏa khắc Ki…

```text
Wide 16:9 landscape cinematic frame. the same circle of five element symbols with red arrows forming a star pattern inside, parchment diagram, dramatic light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trong truyện, đây là luật chiến đấu quan trọng nhất. Tấn công bằng hành khắc đối thủ thì hiệu quả hơn nhiều.…

```text
Wide 16:9 landscape cinematic frame. two opposing glowing energies colliding, one clearly overpowering the other, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và ngược lại, ở cạnh một người có hành sinh ra mình, Đạo của bạn sẽ mạnh lên. Chọn đồng đội cũng phải tính th…

```text
Wide 16:9 landscape cinematic frame. two figures standing back to back with complementary glowing auras merging slightly, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Ngũ hành trong chiến đấu

Lời: Hãy thử một ví dụ. Nếu kẻ thù thuộc Mộc, bạn nên tấn công bằng Kim, vì Kim khắc Mộc. Tấn công bằng Thổ thì ng…

```text
Wide 16:9 landscape cinematic frame. a simple battle diagram on parchment with a leaf symbol facing a blade symbol and a mountain symbol, arrows showing advantage, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nhưng nếu đồng đội của bạn thuộc Thủy, và bạn thuộc Mộc, Thủy sinh Mộc, Đạo của bạn sẽ được nuôi thêm khi hai…

```text
Wide 16:9 landscape cinematic frame. two figures side by side with a wave symbol and a leaf symbol glowing between them, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nghĩa là mỗi trận đấu giống một ván cờ ngũ hành: phải đọc hành của đối thủ, chọn đúng người ra trận, và giữ v…

```text
Wide 16:9 landscape cinematic frame. a board game with five-element tokens arranged on a grid, a hand moving one token forward, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và điều thú vị: con người không đổi được hành của mình. Nhưng họ có thể học cách dùng Đạo của đồng đội, hoặc…

```text
Wide 16:9 landscape cinematic frame. a sword and a lantern and a small vial laid on a cloth, each glowing with a different colored aura, still life, soft light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Âm và dương

Lời: Đan xen với ngũ hành là âm và dương. Mọi thứ đều có cả hai mặt: tối và sáng, tĩnh và động, mềm và cứng.

```text
Wide 16:9 landscape cinematic frame. a simple black and white yin-yang symbol drawn in ink on rice paper, close-up, calm balanced light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Trong truyện, cả nam và nữ, người mạnh và người yếu, đều mang cả âm lẫn dương. Không có phía nào hoàn toàn th…

```text
Wide 16:9 landscape cinematic frame. a pair of stones, one dark and one light, placed side by side on a smooth river rock, close-up, soft balanced light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Trong truyện, Đạo mạnh nhất khi âm dương cân bằng. Người quá thiên về một phía thì Đạo sẽ lệch, dễ bị đánh bạ…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a dark stone on one side and a light stone on the other, perfectly level, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Các Tiên nhân thậm chí có thể thay đổi giữa hai dạng âm và dương, và dùng sự kết hợp âm dương để duy trì sức…

```text
Wide 16:9 landscape cinematic frame. a mysterious figure's silhouette half in shadow and half in light standing among flowers, symbolic medium shot, dramatic split light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku để ý: đây là một ý tưởng rất gần với triết học Đạo giáo thật. Không có gì là thuần túy tốt hay thuần túy…

```text
Wide 16:9 landscape cinematic frame. a small pebble balanced perfectly on top of a larger stone beside a calm stream, close-up, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Luật nâng cao: đánh bại kẻ bất tử

Lời: Giờ tới câu hỏi lớn: làm sao đánh bại một Tiên nhân bất tử?

```text
Wide 16:9 landscape cinematic frame. a tall elegant silhouette regenerating from swirling petals while small human figures watch in shock, dramatic wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Luật nâng cao một: Tiên nhân tái tạo cơ thể nhờ Đạo. Muốn đánh bại chúng, phải dùng Đạo để làm rối loạn dòng…

```text
Wide 16:9 landscape cinematic frame. a glowing stream of energy being disrupted by a sharp contrasting beam, symbolic diagram, dramatic light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Luật nâng cao hai: tấn công đúng hành khắc với thuộc tính của Tiên nhân. Mỗi Tiên nhân có một hành, và luôn c…

```text
Wide 16:9 landscape cinematic frame. a five-element wheel with one symbol highlighted and a red arrow pointing to it from its counter, parchment close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Khái niệm đan điền cũng có thật trong võ thuật và khí công truyền thống. Người tập được dạy tập trung hơi thở…

```text
Wide 16:9 landscape cinematic frame. a martial artist practicing slow breathing exercises in a courtyard at dawn, hands resting on the lower abdomen, medium shot, calm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Luật nâng cao ba: tấn công vào nơi tập trung Đạo của cơ thể, gọi là đan điền, nằm ở vùng bụng dưới. Phá được…

```text
Wide 16:9 landscape cinematic frame. an anatomical diagram of a human silhouette with a small glowing point marked below the navel, parchment close-up, amber ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Và luật nâng cao bốn, quan trọng nhất: phối hợp. Một người hiếm khi đủ. Nhóm tử tù và đao phủ phải kết hợp cá…

```text
Wide 16:9 landscape cinematic frame. several small figures surrounding a towering silhouette, each with a different colored glow, wide shot, dramatic teamwork light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhiều cặp tử tù và đao phủ bắt đầu bằng sự nghi ngờ, rồi dần trở thành đồng đội thật. Có cặp chiến đấu vì nha…

```text
Wide 16:9 landscape cinematic frame. two figures standing back to back in a misty forest, weapons drawn, calm expressions, medium shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku thấy luật này là thông điệp của cả bộ truyện: những người ban đầu muốn giết nhau, tử tù và đao phủ, phải…

```text
Wide 16:9 landscape cinematic frame. two hands, one in shackles and one holding a sword hilt, reaching toward each other, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Gabimaru và Đạo của cảm xúc

Lời: Gabimaru xuất thân từ một làng ninja khắc nghiệt, nơi con người bị huấn luyện như vũ khí. Cậu được gọi là kẻ…

```text
Wide 16:9 landscape cinematic frame. a hidden village in a rocky valley shrouded in mist with training grounds carved into the cliffs, wide shot, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Gabimaru là ví dụ đẹp nhất về cách Đạo gắn với con người. Cậu được huấn luyện để trống rỗng, không cảm xúc, n…

```text
Wide 16:9 landscape cinematic frame. an empty clay vessel sitting alone on a dark shelf, close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhưng Đạo của cậu mạnh nhất khi cậu nghĩ về người vợ, về lý do để sống. Cảm xúc mà cậu tưởng mình không có lạ…

```text
Wide 16:9 landscape cinematic frame. a small figure standing in a burning forest with a faint warm glow around their chest, wide shot, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Có một câu hỏi Sagiri tự hỏi suốt truyện: một người cầm kiếm lấy mạng người khác có quyền được sống thanh thả…

```text
Wide 16:9 landscape cinematic frame. a young swordswoman kneeling beside a wounded companion in a misty forest, sword laid down beside her, medium shot, soft compassionate light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Sagiri cũng vậy. Cô học được rằng nghi ngờ bản thân không phải điểm yếu, mà là một phần của âm dương: sự yếu…

```text
Wide 16:9 landscape cinematic frame. a swordswoman standing calmly with her eyes closed as petals drift around her, medium shot, soft balanced light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: trong Hell's Paradise, người mạnh không phải người vô cảm, mà là người hiểu và cân bằng được cảm x…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small yin-yang pendant and looking at it thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Những hiểu lầm về Đạo

Lời: Hiểu lầm một: Đạo là phép thuật. Không. Trong truyện, Đạo là năng lượng sống có sẵn trong mọi thứ. Không ai đ…

```text
Wide 16:9 landscape cinematic frame. a crossed-out magic wand doodle beside a sprouting seed with faint energy lines, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Trong truyện có những trận mà tử tù yếu hơn nhiều vẫn gây thương tích cho Tiên nhân, nhờ đúng hành và đúng th…

```text
Wide 16:9 landscape cinematic frame. a small figure striking at exactly the right moment as a towering shadow staggers, dynamic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Hiểu lầm hai: Đạo mạnh hơn thì luôn thắng. Không. Tương khắc quan trọng hơn độ mạnh. Một người yếu hơn nhưng…

```text
Wide 16:9 landscape cinematic frame. a small figure with a red glow standing confidently before a much larger figure with a blue glow, symbolic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Hiểu lầm ba: chỉ Tiên nhân mới dùng được Đạo. Không. Con người cũng dùng được, và nhiều tử tù học rất nhanh n…

```text
Wide 16:9 landscape cinematic frame. a group of weary human figures practicing breathing exercises together at the edge of a strange forest, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hiểu lầm bốn, lớn nhất: ngũ hành trong truyện là khoa học. Không. Ngũ hành ngoài đời là một hệ thống triết họ…

```text
Wide 16:9 landscape cinematic frame. an old philosophy book open beside a modern science textbook, with a small dividing line drawn between them, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Kaku nhắc thêm: video này nói về truyện, không phải lời khuyên sức khỏe. Nếu bạn quan tâm tới đông y, hãy hỏi…

```text
Wide 16:9 landscape cinematic frame. a small notice card with a simple health cross icon pinned to a board, close-up, soft clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Đạo ngoài đời thật

Lời: Chữ Đạo gắn với Đạo giáo, một trường phái triết học Trung Hoa cổ, thường được gắn với tên Lão Tử và cuốn Đạo…

```text
Wide 16:9 landscape cinematic frame. an old bamboo scroll with brush calligraphy rolled out on a low wooden table beside incense, close-up, warm serene light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Đạo Đức Kinh có một ý rất nổi tiếng: nước là thứ mềm yếu nhất, nhưng lại thắng được những thứ cứng rắn nhất.…

```text
Wide 16:9 landscape cinematic frame. water flowing gently around a large hard rock in a stream, slowly carving it smooth, close-up, calm natural light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Tư tưởng cốt lõi: sống thuận theo tự nhiên, cân bằng, không cưỡng ép. Hell's Paradise lấy cảm hứng từ đó để x…

```text
Wide 16:9 landscape cinematic frame. a quiet mountain stream flowing around rocks through a misty forest, wide shot, peaceful green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và ý tưởng tìm thuốc trường sinh cũng có thật trong lịch sử. Nhiều vị vua xưa đã sai người đi tìm thuốc bất t…

```text
Wide 16:9 landscape cinematic frame. an ancient ship with a large sail heading toward a misty island on the horizon, wide shot, legendary golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Theo truyền thuyết, người được Tần Thủy Hoàng sai đi là Từ Phúc. Ông dẫn một đoàn thuyền ra biển Đông tìm tiê…

```text
Wide 16:9 landscape cinematic frame. a fleet of ancient ships sailing into a misty eastern sea toward a faint mountainous island, wide shot, legendary golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Kaku để ý: chính Tần Thủy Hoàng, người mà Kaku đã nói trong video về Kingdom, cũng được sử sách kể là từng sa…

```text
Wide 16:9 landscape cinematic frame. a small bronze seal resting beside a tiny vial on an old map, close-up, warm historical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Sơ đồ tổng kết một hình

Lời: Và đây là Đạo trong một hình. Ở giữa: Đạo, năng lượng sống. Ba luật nền: cảm nhận được, tăng sức mạnh được, v…

```text
Wide 16:9 landscape cinematic frame. a large circular diagram on parchment with a glowing center labeled with a simple energy symbol, amber ink overhead shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Vòng trong: ngũ hành với hai vòng tương sinh và tương khắc. Bao quanh: âm và dương.

```text
Wide 16:9 landscape cinematic frame. the diagram with the five-element wheel and a yin-yang ring drawn around it, amber and red ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Và ở góc giấy, những chú thích nhỏ: Đạo cần tâm trí vững vàng, và người ta mạnh lên cùng với sự tin tưởng giữ…

```text
Wide 16:9 landscape cinematic frame. small handwritten notes in the margins of the parchment diagram beside tiny doodles of a calm face and two joined hands, extreme close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Vòng ngoài: bốn luật nâng cao để đánh bại Tiên nhân: làm rối dòng Đạo, đúng hành khắc, nhắm vào đan điền, và…

```text
Wide 16:9 landscape cinematic frame. the complete circular diagram with four small icons around its outer edge, amber ink overhead shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và một dòng chữ nhỏ ở mép giấy: cảm xúc không làm Đạo yếu đi, nếu bạn biết cân bằng nó.

```text
Wide 16:9 landscape cinematic frame. a small handwritten note in the corner of the parchment diagram beside a tiny heart, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Trò chơi: bạn thuộc hành nào?

Lời: Giờ tới trò chơi. Nếu bạn là một tử tù trên hòn đảo, Đạo của bạn thuộc hành nào?

```text
Wide 16:9 landscape cinematic frame. five small cards laid face down on a table, each with a faint element symbol showing through, close-up, mysterious warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nếu bạn nóng tính, hành động nhanh, có lẽ bạn thuộc Hỏa. Nếu bạn điềm tĩnh, linh hoạt, có lẽ là Thủy. Nếu bạn…

```text
Wide 16:9 landscape cinematic frame. three small cards turned over showing a flame, a wave and a blade, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nếu bạn thích giúp người khác lớn lên, có lẽ là Mộc. Và nếu bạn là người mà ai cũng muốn dựa vào, có lẽ là Th…

```text
Wide 16:9 landscape cinematic frame. two more cards turned over showing a leaf and a mountain, with a small playful disclaimer tag beside them, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Gợi ý thêm: nếu bạn thuộc Hỏa, đồng đội lý tưởng của bạn thuộc Mộc, vì Mộc sinh Hỏa. Và hãy cẩn thận với ngườ…

```text
Wide 16:9 landscape cinematic frame. a small playful chart showing a leaf and a flame joined by a heart, and a wave with a tiny warning sign, parchment close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tự nhận mình thuộc Mộc, vì Kaku sống trong một cuốn sổ bằng giấy. Còn bạn? Viết vào bình luận, và cho Ka…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a leaf-symbol card with a proud expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Kết

Lời: Và nếu bạn chưa xem, Kaku khuyên bắt đầu từ mùa một. Nó đẹp, đáng sợ, và có những nhân vật mà bạn sẽ nhớ rất…

```text
Wide 16:9 landscape cinematic frame. a small boat drifting away from a beautiful mist-covered island at sunset, wide shot, bittersweet golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Hell's Paradise lấy một hệ thống tư tưởng hàng nghìn năm tuổi, và biến nó thành luật chiến đấu. Nhưng bài học…

```text
Wide 16:9 landscape cinematic frame. a lone flower growing between two stones on a misty island shore at dawn, close-up, peaceful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku đưa bạn vào một trò chơi đáng sợ hơn nhiều: Miền đất hứa. Nếu bạn là một đứa trẻ ở trại…

```text
Wide 16:9 landscape cinematic frame. a peaceful orphanage building surrounded by a tall forest and a high fence in the distance, wide shot, deceptively warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này giúp bạn hiểu Đạo và ngũ hành rõ hơn, hãy đăng ký kênh. Và nhớ tìm đồng đội có hành sinh ra hàn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the five-element scroll and bowing with its wings folded. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu

Khoảng 60 giây · cảnh s01–s05 · 784 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime Hell's Paradise mùa hai. Truyện có nhiều cảnh bạo lực, nhưng Kaku sẽ không mô tả chi tiết. Hôm nay mình chỉ nói về hệ thống sức mạnh.

<short pause> Một hòn đảo đầy hoa đẹp tới kỳ lạ, những bức tượng Phật khổng lồ, và những sinh vật bất tử. Ai đặt chân lên đảo cũng tìm một thứ: thuốc trường sinh.

<short pause> Và để sống sót trên hòn đảo đó, con người phải hiểu một khái niệm mà người Việt nghe rất quen: Đạo, ngũ hành tương sinh tương khắc, và âm dương.

<short pause> <laugh> Một chi tiết vui: tác giả Hell's Paradise tên là Kaku Yuji. Cùng tên với Kaku. Kaku không có họ hàng gì đâu, nhưng rất tự hào.

<short pause> Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku giải thích Đạo trong Hell's Paradise: luật nền, ngũ hành, âm dương, luật nâng cao, và những hiểu lầm. Cuối video là sơ đồ tổng kết trong một hình.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime Hell's Paradise mùa hai. Truyện có nhiều cảnh bạo lực, nhưng Kaku sẽ không mô tả chi tiết. Hôm nay mình chỉ nói về hệ thống sức mạnh.

[pause] Một hòn đảo đầy hoa đẹp tới kỳ lạ, những bức tượng Phật khổng lồ, và những sinh vật bất tử. Ai đặt chân lên đảo cũng tìm một thứ: thuốc trường sinh.

[pause] Và để sống sót trên hòn đảo đó, con người phải hiểu một khái niệm mà người Việt nghe rất quen: Đạo, ngũ hành tương sinh tương khắc, và âm dương.

[pause] [chuckles] Một chi tiết vui: tác giả Hell's Paradise tên là Kaku Yuji. Cùng tên với Kaku. Kaku không có họ hàng gì đâu, nhưng rất tự hào.

[pause] Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku giải thích Đạo trong Hell's Paradise: luật nền, ngũ hành, âm dương, luật nâng cao, và những hiểu lầm. Cuối video là sơ đồ tổng kết trong một hình.
```

### c02 · Bối cảnh: hòn đảo Shinsenkyo / Một hòn đảo sống

Khoảng 152 giây · cảnh s06–s17 · 1971 ký tự

**Gemini**

```text
Hell's Paradise, hay Địa ngục cực lạc, là manga của Kaku Yuji, đăng trên Shonen Jump+ từ tháng một năm 2018 tới tháng một năm 2021. Anime do MAPPA làm, mùa một năm 2023, mùa hai từ tháng một năm 2026.

<short pause> Bối cảnh là Nhật Bản thời Edo. Tướng quân nghe tin về một hòn đảo xa, nơi có thuốc trường sinh. <short pause> Nhưng mọi đoàn thám hiểm cử tới đều không trở về, hoặc trở về trong tình trạng kỳ lạ.

<short pause> Mỗi tử tù là một kẻ nguy hiểm: ninja, samurai, thủ lĩnh cướp, kẻ lừa đảo. Mỗi đao phủ là một kiếm sĩ giỏi. Một tổ hợp kỳ lạ: người canh gác và người bị canh gác phải sống sót cùng nhau.

<short pause> Vì vậy, tướng quân cử những tử tù ra đảo. Ai mang thuốc trường sinh về sẽ được tha tội. Mỗi tử tù đi cùng một người thuộc dòng họ đao phủ Yamada Asaemon, người sẽ chém đầu họ nếu họ bỏ trốn.

<short pause> Nhân vật chính là Gabimaru, một ninja được gọi là kẻ trống rỗng, người tưởng như không có cảm xúc. <short pause> Nhưng cậu có một lý do để sống: người vợ đang chờ ở quê nhà.

<short pause> Người đi cùng cậu là Sagiri, một nữ đao phủ trẻ, luôn nghi ngờ chính mình vì phải cầm kiếm lấy mạng người. Hai con người đầy mâu thuẫn trên một hòn đảo đầy bí ẩn.

<short pause> Trên đảo, họ gặp những sinh vật đáng sợ nhất: Tiên nhân, những kẻ gần như bất tử, có thể tái tạo cơ thể. Và mọi vũ khí thông thường đều vô dụng với chúng. Chỉ có một thứ có tác dụng: Đạo.

<short pause> Trước khi vào luật, hãy nhìn hòn đảo. Shinsenkyo đẹp như thiên đường: hoa nở khắp nơi, bướm bay, cây cối rực rỡ. <short pause> Nhưng mọi vẻ đẹp đó đều che giấu nguy hiểm.

<short pause> Trên đảo có những sinh vật lạ, mang dáng dấp tượng thần tượng Phật, lai giữa người, thú và côn trùng. Chúng tấn công bất kỳ ai đặt chân lên đảo.

<short pause> Và cả những con người biến thành hoa. Kaku không mô tả chi tiết. Chỉ cần biết: thuốc trường sinh trên hòn đảo này có một cái giá rất đen tối.

<short pause> Tất cả những điều kỳ lạ đó đều có chung một gốc: Đạo. Hòn đảo được xây dựng, và vận hành, bằng chính năng lượng sống này.

<short pause> <laugh> Kaku để ý: đây là một ý tưởng rất hay. Hệ thống sức mạnh không chỉ để đánh nhau, mà còn giải thích vì sao cả thế giới trên đảo lại kỳ dị như vậy.
```

**ElevenLabs**

```text
Hell's Paradise, hay Địa ngục cực lạc, là manga của Kaku Yuji, đăng trên Shonen Jump+ từ tháng một năm 2018 tới tháng một năm 2021. Anime do MAPPA làm, mùa một năm 2023, mùa hai từ tháng một năm 2026.

[pause] Bối cảnh là Nhật Bản thời Edo. Tướng quân nghe tin về một hòn đảo xa, nơi có thuốc trường sinh. [pause] Nhưng mọi đoàn thám hiểm cử tới đều không trở về, hoặc trở về trong tình trạng kỳ lạ.

[pause] Mỗi tử tù là một kẻ nguy hiểm: ninja, samurai, thủ lĩnh cướp, kẻ lừa đảo. Mỗi đao phủ là một kiếm sĩ giỏi. Một tổ hợp kỳ lạ: người canh gác và người bị canh gác phải sống sót cùng nhau.

[pause] Vì vậy, tướng quân cử những tử tù ra đảo. Ai mang thuốc trường sinh về sẽ được tha tội. Mỗi tử tù đi cùng một người thuộc dòng họ đao phủ Yamada Asaemon, người sẽ chém đầu họ nếu họ bỏ trốn.

[pause] Nhân vật chính là Gabimaru, một ninja được gọi là kẻ trống rỗng, người tưởng như không có cảm xúc. [pause] Nhưng cậu có một lý do để sống: người vợ đang chờ ở quê nhà.

[pause] Người đi cùng cậu là Sagiri, một nữ đao phủ trẻ, luôn nghi ngờ chính mình vì phải cầm kiếm lấy mạng người. Hai con người đầy mâu thuẫn trên một hòn đảo đầy bí ẩn.

[pause] Trên đảo, họ gặp những sinh vật đáng sợ nhất: Tiên nhân, những kẻ gần như bất tử, có thể tái tạo cơ thể. Và mọi vũ khí thông thường đều vô dụng với chúng. Chỉ có một thứ có tác dụng: Đạo.

[pause] Trước khi vào luật, hãy nhìn hòn đảo. Shinsenkyo đẹp như thiên đường: hoa nở khắp nơi, bướm bay, cây cối rực rỡ. [pause] Nhưng mọi vẻ đẹp đó đều che giấu nguy hiểm.

[pause] Trên đảo có những sinh vật lạ, mang dáng dấp tượng thần tượng Phật, lai giữa người, thú và côn trùng. Chúng tấn công bất kỳ ai đặt chân lên đảo.

[pause] Và cả những con người biến thành hoa. Kaku không mô tả chi tiết. Chỉ cần biết: thuốc trường sinh trên hòn đảo này có một cái giá rất đen tối.

[pause] Tất cả những điều kỳ lạ đó đều có chung một gốc: Đạo. Hòn đảo được xây dựng, và vận hành, bằng chính năng lượng sống này.

[pause] [chuckles] Kaku để ý: đây là một ý tưởng rất hay. Hệ thống sức mạnh không chỉ để đánh nhau, mà còn giải thích vì sao cả thế giới trên đảo lại kỳ dị như vậy.
```

### c03 · Luật nền: Đạo là gì? / Ngũ hành: năm thuộc tính

Khoảng 151 giây · cảnh s18–s31 · 1969 ký tự

**Gemini**

```text
Trong Hell's Paradise, Đạo là năng lượng sống chảy trong mọi sinh vật: con người, động vật, cây cỏ. Ai cũng có Đạo, chỉ là phần lớn không biết cách cảm nhận và điều khiển nó.

<short pause> Luật một: Đạo có thể cảm nhận được. Người luyện tập có thể thấy luồng Đạo của người khác, đoán được họ mạnh hay yếu, và đòn tấn công sẽ tới từ đâu.

<short pause> Luật hai: Đạo có thể được tập trung để tăng sức mạnh cơ thể, gia cố vũ khí, hoặc chữa lành vết thương nhanh hơn.

<short pause> Trên đảo, những người mạnh thường là những người học được cách thở chậm, giữ bình tĩnh ngay cả khi đối mặt nguy hiểm. Đạo đòi hỏi tâm trí vững vàng.

<short pause> Luật ba: Đạo có thể bị cạn. Dùng quá nhiều, cơ thể kiệt sức. Đạo cũng dao động theo cảm xúc: sợ hãi, giận dữ làm luồng Đạo rối loạn.

<short pause> <laugh> Kaku để ý: Đạo trong truyện giống chakra trong Naruto hay Khí trong Black Clover. <short pause> Nhưng điểm khác biệt, và thú vị nhất, là nó được chia theo ngũ hành.

<short pause> Mỗi người và mỗi sinh vật có một thuộc tính Đạo, thuộc một trong năm hành: Mộc, Hỏa, Thổ, Kim, Thủy.

<short pause> Chẳng hạn, nhiều người Việt vẫn nghe ông bà nói người mệnh này hợp màu này, tuổi này hợp tuổi kia. Đó là cách ngũ hành đi vào đời sống văn hóa, dù không phải khoa học.

<short pause> Nếu bạn lớn lên ở Việt Nam, rất có thể bạn đã nghe về ngũ hành qua ông bà, qua xem ngày, hay qua đông y. Hell's Paradise mượn đúng hệ thống đó.

<short pause> Và các hành tác động lẫn nhau theo hai vòng. Vòng thứ nhất là tương sinh: hành này nuôi dưỡng hành kia.

<short pause> Mộc sinh Hỏa: gỗ cháy thành lửa. Hỏa sinh Thổ: lửa để lại tro thành đất. Thổ sinh Kim: trong đất có kim loại. Kim sinh Thủy: kim loại lạnh đọng hơi nước. Thủy sinh Mộc: nước nuôi cây.

<short pause> Vòng thứ hai là tương khắc: hành này áp chế hành kia. Mộc khắc Thổ, Thổ khắc Thủy, Thủy khắc Hỏa, Hỏa khắc Kim, Kim khắc Mộc.

<short pause> Trong truyện, đây là luật chiến đấu quan trọng nhất. Tấn công bằng hành khắc đối thủ thì hiệu quả hơn nhiều. Tấn công bằng hành bị đối thủ khắc thì gần như vô dụng.

<short pause> Và ngược lại, ở cạnh một người có hành sinh ra mình, Đạo của bạn sẽ mạnh lên. Chọn đồng đội cũng phải tính theo ngũ hành.
```

**ElevenLabs**

```text
Trong Hell's Paradise, Đạo là năng lượng sống chảy trong mọi sinh vật: con người, động vật, cây cỏ. Ai cũng có Đạo, chỉ là phần lớn không biết cách cảm nhận và điều khiển nó.

[pause] Luật một: Đạo có thể cảm nhận được. Người luyện tập có thể thấy luồng Đạo của người khác, đoán được họ mạnh hay yếu, và đòn tấn công sẽ tới từ đâu.

[pause] Luật hai: Đạo có thể được tập trung để tăng sức mạnh cơ thể, gia cố vũ khí, hoặc chữa lành vết thương nhanh hơn.

[pause] Trên đảo, những người mạnh thường là những người học được cách thở chậm, giữ bình tĩnh ngay cả khi đối mặt nguy hiểm. Đạo đòi hỏi tâm trí vững vàng.

[pause] Luật ba: Đạo có thể bị cạn. Dùng quá nhiều, cơ thể kiệt sức. Đạo cũng dao động theo cảm xúc: sợ hãi, giận dữ làm luồng Đạo rối loạn.

[pause] [chuckles] Kaku để ý: Đạo trong truyện giống chakra trong Naruto hay Khí trong Black Clover. [pause] Nhưng điểm khác biệt, và thú vị nhất, là nó được chia theo ngũ hành.

[pause] Mỗi người và mỗi sinh vật có một thuộc tính Đạo, thuộc một trong năm hành: Mộc, Hỏa, Thổ, Kim, Thủy.

[pause] Chẳng hạn, nhiều người Việt vẫn nghe ông bà nói người mệnh này hợp màu này, tuổi này hợp tuổi kia. Đó là cách ngũ hành đi vào đời sống văn hóa, dù không phải khoa học.

[pause] Nếu bạn lớn lên ở Việt Nam, rất có thể bạn đã nghe về ngũ hành qua ông bà, qua xem ngày, hay qua đông y. Hell's Paradise mượn đúng hệ thống đó.

[pause] Và các hành tác động lẫn nhau theo hai vòng. Vòng thứ nhất là tương sinh: hành này nuôi dưỡng hành kia.

[pause] Mộc sinh Hỏa: gỗ cháy thành lửa. Hỏa sinh Thổ: lửa để lại tro thành đất. Thổ sinh Kim: trong đất có kim loại. Kim sinh Thủy: kim loại lạnh đọng hơi nước. Thủy sinh Mộc: nước nuôi cây.

[pause] Vòng thứ hai là tương khắc: hành này áp chế hành kia. Mộc khắc Thổ, Thổ khắc Thủy, Thủy khắc Hỏa, Hỏa khắc Kim, Kim khắc Mộc.

[pause] Trong truyện, đây là luật chiến đấu quan trọng nhất. Tấn công bằng hành khắc đối thủ thì hiệu quả hơn nhiều. Tấn công bằng hành bị đối thủ khắc thì gần như vô dụng.

[pause] Và ngược lại, ở cạnh một người có hành sinh ra mình, Đạo của bạn sẽ mạnh lên. Chọn đồng đội cũng phải tính theo ngũ hành.
```

### c04 · Ngũ hành trong chiến đấu / Âm và dương

Khoảng 90 giây · cảnh s32–s40 · 1170 ký tự

**Gemini**

```text
Hãy thử một ví dụ. Nếu kẻ thù thuộc Mộc, bạn nên tấn công bằng Kim, vì Kim khắc Mộc. Tấn công bằng Thổ thì ngược lại, vì Mộc khắc Thổ, đòn của bạn sẽ bị áp chế.

<short pause> Nhưng nếu đồng đội của bạn thuộc Thủy, và bạn thuộc Mộc, Thủy sinh Mộc, Đạo của bạn sẽ được nuôi thêm khi hai người cùng chiến đấu.

<short pause> Nghĩa là mỗi trận đấu giống một ván cờ ngũ hành: phải đọc hành của đối thủ, chọn đúng người ra trận, và giữ vị trí đúng với đồng đội.

<short pause> Và điều thú vị: con người không đổi được hành của mình. <short pause> Nhưng họ có thể học cách dùng Đạo của đồng đội, hoặc dùng vật dụng mang hành khác, để bù đắp.

<short pause> Đan xen với ngũ hành là âm và dương. Mọi thứ đều có cả hai mặt: tối và sáng, tĩnh và động, mềm và cứng.

<short pause> Trong truyện, cả nam và nữ, người mạnh và người yếu, đều mang cả âm lẫn dương. Không có phía nào hoàn toàn thắng thế.

<short pause> Trong truyện, Đạo mạnh nhất khi âm dương cân bằng. Người quá thiên về một phía thì Đạo sẽ lệch, dễ bị đánh bại.

<short pause> Các Tiên nhân thậm chí có thể thay đổi giữa hai dạng âm và dương, và dùng sự kết hợp âm dương để duy trì sức mạnh bất tử của mình.

<short pause> Kaku để ý: đây là một ý tưởng rất gần với triết học Đạo giáo thật. Không có gì là thuần túy tốt hay thuần túy xấu. Mọi thứ cần cân bằng.
```

**ElevenLabs**

```text
Hãy thử một ví dụ. Nếu kẻ thù thuộc Mộc, bạn nên tấn công bằng Kim, vì Kim khắc Mộc. Tấn công bằng Thổ thì ngược lại, vì Mộc khắc Thổ, đòn của bạn sẽ bị áp chế.

[pause] Nhưng nếu đồng đội của bạn thuộc Thủy, và bạn thuộc Mộc, Thủy sinh Mộc, Đạo của bạn sẽ được nuôi thêm khi hai người cùng chiến đấu.

[pause] Nghĩa là mỗi trận đấu giống một ván cờ ngũ hành: phải đọc hành của đối thủ, chọn đúng người ra trận, và giữ vị trí đúng với đồng đội.

[pause] Và điều thú vị: con người không đổi được hành của mình. [pause] Nhưng họ có thể học cách dùng Đạo của đồng đội, hoặc dùng vật dụng mang hành khác, để bù đắp.

[pause] Đan xen với ngũ hành là âm và dương. Mọi thứ đều có cả hai mặt: tối và sáng, tĩnh và động, mềm và cứng.

[pause] Trong truyện, cả nam và nữ, người mạnh và người yếu, đều mang cả âm lẫn dương. Không có phía nào hoàn toàn thắng thế.

[pause] Trong truyện, Đạo mạnh nhất khi âm dương cân bằng. Người quá thiên về một phía thì Đạo sẽ lệch, dễ bị đánh bại.

[pause] Các Tiên nhân thậm chí có thể thay đổi giữa hai dạng âm và dương, và dùng sự kết hợp âm dương để duy trì sức mạnh bất tử của mình.

[pause] Kaku để ý: đây là một ý tưởng rất gần với triết học Đạo giáo thật. Không có gì là thuần túy tốt hay thuần túy xấu. Mọi thứ cần cân bằng.
```

### c05 · Luật nâng cao: đánh bại kẻ bất tử

Khoảng 87 giây · cảnh s41–s48 · 1128 ký tự

**Gemini**

```text
Giờ tới câu hỏi lớn: làm sao đánh bại một Tiên nhân bất tử?

<short pause> Luật nâng cao một: Tiên nhân tái tạo cơ thể nhờ Đạo. Muốn đánh bại chúng, phải dùng Đạo để làm rối loạn dòng Đạo của chúng.

<short pause> Luật nâng cao hai: tấn công đúng hành khắc với thuộc tính của Tiên nhân. Mỗi Tiên nhân có một hành, và luôn có một hành khắc nó.

<short pause> Khái niệm đan điền cũng có thật trong võ thuật và khí công truyền thống. Người tập được dạy tập trung hơi thở vào vùng bụng dưới. <short pause> Nhưng đó là khái niệm truyền thống, không phải một bộ phận giải phẫu.

<short pause> Luật nâng cao ba: tấn công vào nơi tập trung Đạo của cơ thể, gọi là đan điền, nằm ở vùng bụng dưới. Phá được nơi đó, khả năng tái tạo bị chặn lại.

<short pause> Và luật nâng cao bốn, quan trọng nhất: phối hợp. Một người hiếm khi đủ. Nhóm tử tù và đao phủ phải kết hợp các hành khác nhau, người này mở đường, người kia kết thúc.

<short pause> Nhiều cặp tử tù và đao phủ bắt đầu bằng sự nghi ngờ, rồi dần trở thành đồng đội thật. Có cặp chiến đấu vì nhau tới cuối cùng. Đạo của họ mạnh lên cùng với sự tin tưởng.

<short pause> Kaku thấy luật này là thông điệp của cả bộ truyện: những người ban đầu muốn giết nhau, tử tù và đao phủ, phải học cách hợp tác để sống sót.
```

**ElevenLabs**

```text
[curious] Giờ tới câu hỏi lớn: làm sao đánh bại một Tiên nhân bất tử?

[pause] Luật nâng cao một: Tiên nhân tái tạo cơ thể nhờ Đạo. Muốn đánh bại chúng, phải dùng Đạo để làm rối loạn dòng Đạo của chúng.

[pause] Luật nâng cao hai: tấn công đúng hành khắc với thuộc tính của Tiên nhân. Mỗi Tiên nhân có một hành, và luôn có một hành khắc nó.

[pause] Khái niệm đan điền cũng có thật trong võ thuật và khí công truyền thống. Người tập được dạy tập trung hơi thở vào vùng bụng dưới. [pause] Nhưng đó là khái niệm truyền thống, không phải một bộ phận giải phẫu.

[pause] Luật nâng cao ba: tấn công vào nơi tập trung Đạo của cơ thể, gọi là đan điền, nằm ở vùng bụng dưới. Phá được nơi đó, khả năng tái tạo bị chặn lại.

[pause] Và luật nâng cao bốn, quan trọng nhất: phối hợp. Một người hiếm khi đủ. Nhóm tử tù và đao phủ phải kết hợp các hành khác nhau, người này mở đường, người kia kết thúc.

[pause] Nhiều cặp tử tù và đao phủ bắt đầu bằng sự nghi ngờ, rồi dần trở thành đồng đội thật. Có cặp chiến đấu vì nhau tới cuối cùng. Đạo của họ mạnh lên cùng với sự tin tưởng.

[pause] Kaku thấy luật này là thông điệp của cả bộ truyện: những người ban đầu muốn giết nhau, tử tù và đao phủ, phải học cách hợp tác để sống sót.
```

### c06 · Gabimaru và Đạo của cảm xúc / Những hiểu lầm về Đạo

Khoảng 143 giây · cảnh s49–s60 · 1856 ký tự

**Gemini**

```text
Gabimaru xuất thân từ một làng ninja khắc nghiệt, nơi con người bị huấn luyện như vũ khí. Cậu được gọi là kẻ trống rỗng vì không biểu lộ cảm xúc, và vì không gì giết được cậu.

<short pause> Gabimaru là ví dụ đẹp nhất về cách Đạo gắn với con người. Cậu được huấn luyện để trống rỗng, không cảm xúc, như một công cụ giết người.

<short pause> Nhưng Đạo của cậu mạnh nhất khi cậu nghĩ về người vợ, về lý do để sống. Cảm xúc mà cậu tưởng mình không có lại là nguồn sức mạnh lớn nhất.

<short pause> Có một câu hỏi Sagiri tự hỏi suốt truyện: một người cầm kiếm lấy mạng người khác có quyền được sống thanh thản không? Cô tìm ra câu trả lời không phải bằng lý thuyết, mà bằng cách chiến đấu để bảo vệ người khác.

<short pause> Sagiri cũng vậy. Cô học được rằng nghi ngờ bản thân không phải điểm yếu, mà là một phần của âm dương: sự yếu đuối cân bằng với sự cứng rắn.

<short pause> <laugh> Kaku để ý: trong Hell's Paradise, người mạnh không phải người vô cảm, mà là người hiểu và cân bằng được cảm xúc của mình.

<short pause> Hiểu lầm một: Đạo là phép thuật. Không. Trong truyện, Đạo là năng lượng sống có sẵn trong mọi thứ. Không ai được ban cho nó, chỉ là học cách cảm nhận.

<short pause> Trong truyện có những trận mà tử tù yếu hơn nhiều vẫn gây thương tích cho Tiên nhân, nhờ đúng hành và đúng thời điểm. Đó là lúc người xem thấy luật ngũ hành đáng giá thế nào.

<short pause> Hiểu lầm hai: Đạo mạnh hơn thì luôn thắng. Không. Tương khắc quan trọng hơn độ mạnh. Một người yếu hơn nhưng đúng hành vẫn có thể đánh bại người mạnh hơn.

<short pause> Hiểu lầm ba: chỉ Tiên nhân mới dùng được Đạo. Không. Con người cũng dùng được, và nhiều tử tù học rất nhanh ngay trên đảo.

<short pause> Hiểu lầm bốn, lớn nhất: ngũ hành trong truyện là khoa học. Không. Ngũ hành ngoài đời là một hệ thống triết học và văn hóa cổ, dùng trong đông y, phong thủy, xem ngày. Nó không phải một định luật vật lý.

<short pause> Kaku nhắc thêm: video này nói về truyện, không phải lời khuyên sức khỏe. Nếu bạn quan tâm tới đông y, hãy hỏi thầy thuốc có chuyên môn.
```

**ElevenLabs**

```text
Gabimaru xuất thân từ một làng ninja khắc nghiệt, nơi con người bị huấn luyện như vũ khí. Cậu được gọi là kẻ trống rỗng vì không biểu lộ cảm xúc, và vì không gì giết được cậu.

[pause] Gabimaru là ví dụ đẹp nhất về cách Đạo gắn với con người. Cậu được huấn luyện để trống rỗng, không cảm xúc, như một công cụ giết người.

[pause] Nhưng Đạo của cậu mạnh nhất khi cậu nghĩ về người vợ, về lý do để sống. Cảm xúc mà cậu tưởng mình không có lại là nguồn sức mạnh lớn nhất.

[pause] [curious] Có một câu hỏi Sagiri tự hỏi suốt truyện: một người cầm kiếm lấy mạng người khác có quyền được sống thanh thản không? Cô tìm ra câu trả lời không phải bằng lý thuyết, mà bằng cách chiến đấu để bảo vệ người khác.

[pause] Sagiri cũng vậy. Cô học được rằng nghi ngờ bản thân không phải điểm yếu, mà là một phần của âm dương: sự yếu đuối cân bằng với sự cứng rắn.

[pause] [chuckles] Kaku để ý: trong Hell's Paradise, người mạnh không phải người vô cảm, mà là người hiểu và cân bằng được cảm xúc của mình.

[pause] Hiểu lầm một: Đạo là phép thuật. Không. Trong truyện, Đạo là năng lượng sống có sẵn trong mọi thứ. Không ai được ban cho nó, chỉ là học cách cảm nhận.

[pause] Trong truyện có những trận mà tử tù yếu hơn nhiều vẫn gây thương tích cho Tiên nhân, nhờ đúng hành và đúng thời điểm. Đó là lúc người xem thấy luật ngũ hành đáng giá thế nào.

[pause] Hiểu lầm hai: Đạo mạnh hơn thì luôn thắng. Không. Tương khắc quan trọng hơn độ mạnh. Một người yếu hơn nhưng đúng hành vẫn có thể đánh bại người mạnh hơn.

[pause] Hiểu lầm ba: chỉ Tiên nhân mới dùng được Đạo. Không. Con người cũng dùng được, và nhiều tử tù học rất nhanh ngay trên đảo.

[pause] Hiểu lầm bốn, lớn nhất: ngũ hành trong truyện là khoa học. Không. Ngũ hành ngoài đời là một hệ thống triết học và văn hóa cổ, dùng trong đông y, phong thủy, xem ngày. Nó không phải một định luật vật lý.

[pause] Kaku nhắc thêm: video này nói về truyện, không phải lời khuyên sức khỏe. Nếu bạn quan tâm tới đông y, hãy hỏi thầy thuốc có chuyên môn.
```

### c07 · Đạo ngoài đời thật / Sơ đồ tổng kết một hình

Khoảng 115 giây · cảnh s61–s71 · 1494 ký tự

**Gemini**

```text
Chữ Đạo gắn với Đạo giáo, một trường phái triết học Trung Hoa cổ, thường được gắn với tên Lão Tử và cuốn Đạo Đức Kinh.

<short pause> Đạo Đức Kinh có một ý rất nổi tiếng: nước là thứ mềm yếu nhất, nhưng lại thắng được những thứ cứng rắn nhất. Hell's Paradise thể hiện đúng tinh thần đó: người mềm dẻo, biết cân bằng, mới là người sống sót.

<short pause> Tư tưởng cốt lõi: sống thuận theo tự nhiên, cân bằng, không cưỡng ép. Hell's Paradise lấy cảm hứng từ đó để xây hòn đảo và các Tiên nhân.

<short pause> Và ý tưởng tìm thuốc trường sinh cũng có thật trong lịch sử. Nhiều vị vua xưa đã sai người đi tìm thuốc bất tử, và có những người còn tìm tới những hòn đảo huyền thoại ngoài biển.

<short pause> Theo truyền thuyết, người được Tần Thủy Hoàng sai đi là Từ Phúc. Ông dẫn một đoàn thuyền ra biển Đông tìm tiên đảo, và không bao giờ trở về. Có truyền thuyết còn nói ông tới Nhật Bản.

<short pause> Kaku để ý: chính Tần Thủy Hoàng, người mà Kaku đã nói trong video về Kingdom, cũng được sử sách kể là từng sai người đi tìm thuốc trường sinh.

<short pause> Và đây là Đạo trong một hình. Ở giữa: Đạo, năng lượng sống. Ba luật nền: cảm nhận được, tăng sức mạnh được, và có thể cạn.

<short pause> Vòng trong: ngũ hành với hai vòng tương sinh và tương khắc. Bao quanh: âm và dương.

<short pause> Và ở góc giấy, những chú thích nhỏ: Đạo cần tâm trí vững vàng, và người ta mạnh lên cùng với sự tin tưởng giữa đồng đội.

<short pause> Vòng ngoài: bốn luật nâng cao để đánh bại Tiên nhân: làm rối dòng Đạo, đúng hành khắc, nhắm vào đan điền, và phối hợp.

<short pause> Và một dòng chữ nhỏ ở mép giấy: cảm xúc không làm Đạo yếu đi, nếu bạn biết cân bằng nó.
```

**ElevenLabs**

```text
Chữ Đạo gắn với Đạo giáo, một trường phái triết học Trung Hoa cổ, thường được gắn với tên Lão Tử và cuốn Đạo Đức Kinh.

[pause] Đạo Đức Kinh có một ý rất nổi tiếng: nước là thứ mềm yếu nhất, nhưng lại thắng được những thứ cứng rắn nhất. Hell's Paradise thể hiện đúng tinh thần đó: người mềm dẻo, biết cân bằng, mới là người sống sót.

[pause] Tư tưởng cốt lõi: sống thuận theo tự nhiên, cân bằng, không cưỡng ép. Hell's Paradise lấy cảm hứng từ đó để xây hòn đảo và các Tiên nhân.

[pause] Và ý tưởng tìm thuốc trường sinh cũng có thật trong lịch sử. Nhiều vị vua xưa đã sai người đi tìm thuốc bất tử, và có những người còn tìm tới những hòn đảo huyền thoại ngoài biển.

[pause] Theo truyền thuyết, người được Tần Thủy Hoàng sai đi là Từ Phúc. Ông dẫn một đoàn thuyền ra biển Đông tìm tiên đảo, và không bao giờ trở về. Có truyền thuyết còn nói ông tới Nhật Bản.

[pause] Kaku để ý: chính Tần Thủy Hoàng, người mà Kaku đã nói trong video về Kingdom, cũng được sử sách kể là từng sai người đi tìm thuốc trường sinh.

[pause] Và đây là Đạo trong một hình. Ở giữa: Đạo, năng lượng sống. Ba luật nền: cảm nhận được, tăng sức mạnh được, và có thể cạn.

[pause] Vòng trong: ngũ hành với hai vòng tương sinh và tương khắc. Bao quanh: âm và dương.

[pause] Và ở góc giấy, những chú thích nhỏ: Đạo cần tâm trí vững vàng, và người ta mạnh lên cùng với sự tin tưởng giữa đồng đội.

[pause] Vòng ngoài: bốn luật nâng cao để đánh bại Tiên nhân: làm rối dòng Đạo, đúng hành khắc, nhắm vào đan điền, và phối hợp.

[pause] Và một dòng chữ nhỏ ở mép giấy: cảm xúc không làm Đạo yếu đi, nếu bạn biết cân bằng nó.
```

### c08 · Trò chơi: bạn thuộc hành nào? / Kết

Khoảng 106 giây · cảnh s72–s80 · 1376 ký tự

**Gemini**

```text
Giờ tới trò chơi. Nếu bạn là một tử tù trên hòn đảo, Đạo của bạn thuộc hành nào?

<short pause> Nếu bạn nóng tính, hành động nhanh, có lẽ bạn thuộc Hỏa. Nếu bạn điềm tĩnh, linh hoạt, có lẽ là Thủy. Nếu bạn kiên định, cứng rắn, có lẽ là Kim.

<short pause> Nếu bạn thích giúp người khác lớn lên, có lẽ là Mộc. Và nếu bạn là người mà ai cũng muốn dựa vào, có lẽ là Thổ. Đây là trò chơi vui, không phải xem bói nhé.

<short pause> Gợi ý thêm: nếu bạn thuộc Hỏa, đồng đội lý tưởng của bạn thuộc Mộc, vì Mộc sinh Hỏa. Và hãy cẩn thận với người thuộc Thủy trong những ngày căng thẳng. Đùa thôi, nhưng cũng vui phải không?

<short pause> <laugh> Kaku tự nhận mình thuộc Mộc, vì Kaku sống trong một cuốn sổ bằng giấy. Còn bạn? Viết vào bình luận, và cho Kaku biết đồng đội lý tưởng của bạn thuộc hành nào.

<short pause> Và nếu bạn chưa xem, Kaku khuyên bắt đầu từ mùa một. Nó đẹp, đáng sợ, và có những nhân vật mà bạn sẽ nhớ rất lâu, trên một hòn đảo mà bạn sẽ không bao giờ muốn tới.

<short pause> Hell's Paradise lấy một hệ thống tư tưởng hàng nghìn năm tuổi, và biến nó thành luật chiến đấu. <short pause> Nhưng bài học của nó vẫn giữ nguyên: cân bằng, và không ai sống sót một mình.

<short pause> Video tiếp theo, Kaku đưa bạn vào một trò chơi đáng sợ hơn nhiều: Miền đất hứa. Nếu bạn là một đứa trẻ ở trại mồ côi Grace Field, bạn sẽ sống sót bằng cách nào?

<short pause> Nếu video này giúp bạn hiểu Đạo và ngũ hành rõ hơn, hãy đăng ký kênh. Và nhớ tìm đồng đội có hành sinh ra hành của mình nhé. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ tới trò chơi. [curious] Nếu bạn là một tử tù trên hòn đảo, Đạo của bạn thuộc hành nào?

[pause] Nếu bạn nóng tính, hành động nhanh, có lẽ bạn thuộc Hỏa. Nếu bạn điềm tĩnh, linh hoạt, có lẽ là Thủy. Nếu bạn kiên định, cứng rắn, có lẽ là Kim.

[pause] Nếu bạn thích giúp người khác lớn lên, có lẽ là Mộc. Và nếu bạn là người mà ai cũng muốn dựa vào, có lẽ là Thổ. Đây là trò chơi vui, không phải xem bói nhé.

[pause] Gợi ý thêm: nếu bạn thuộc Hỏa, đồng đội lý tưởng của bạn thuộc Mộc, vì Mộc sinh Hỏa. Và hãy cẩn thận với người thuộc Thủy trong những ngày căng thẳng. Đùa thôi, nhưng cũng vui phải không?

[pause] [chuckles] Kaku tự nhận mình thuộc Mộc, vì Kaku sống trong một cuốn sổ bằng giấy. Còn bạn? Viết vào bình luận, và cho Kaku biết đồng đội lý tưởng của bạn thuộc hành nào.

[pause] Và nếu bạn chưa xem, Kaku khuyên bắt đầu từ mùa một. Nó đẹp, đáng sợ, và có những nhân vật mà bạn sẽ nhớ rất lâu, trên một hòn đảo mà bạn sẽ không bao giờ muốn tới.

[pause] Hell's Paradise lấy một hệ thống tư tưởng hàng nghìn năm tuổi, và biến nó thành luật chiến đấu. [pause] Nhưng bài học của nó vẫn giữ nguyên: cân bằng, và không ai sống sót một mình.

[pause] Video tiếp theo, Kaku đưa bạn vào một trò chơi đáng sợ hơn nhiều: Miền đất hứa. Nếu bạn là một đứa trẻ ở trại mồ côi Grace Field, bạn sẽ sống sót bằng cách nào?

[pause] Nếu video này giúp bạn hiểu Đạo và ngũ hành rõ hơn, hãy đăng ký kênh. Và nhớ tìm đồng đội có hành sinh ra hành của mình nhé. Kaku gấp sổ đây, hẹn gặp lại!
```
