# Bộ prompt · Solo Leveling: Hệ thống cấp bậc thợ săn và cổng hoạt động thế nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 98 ảnh, 7 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (98 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Solo Leveling đến hết phần anime mùa hai, gồm cả arc đảo Jeju. Nếu chưa xem tới đó…

```text
Wide 16:9 landscape cinematic frame. a glowing blue portal floating over a quiet city street at night, sealed off by barriers. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy tưởng tượng một thế giới mà cánh cổng tới hầm ngục có thể mở ra giữa ngã tư đường phố bất cứ lúc nào. Và…

```text
Wide 16:9 landscape cinematic frame. a swirling blue gate appearing above a busy intersection, pedestrians looking up in shock. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trong thế giới đó, con người được xếp hạng như trong một trò chơi: E, D, C, B, A, S. Hạng của bạn quyết định…

```text
Wide 16:9 landscape cinematic frame. a vertical ladder of glowing letters E D C B A S floating in the dark. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và ở đáy bậc thang ấy có một người được gọi là thợ săn yếu nhất nhân loại. Rồi một ngày, anh ta bắt đầu lên c…

```text
Wide 16:9 landscape cinematic frame. a lone young hunter silhouette at the bottom of a giant staircase, a faint blue screen glowing in front of him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã hệ thống của Solo Leveling: cổng, cấp bậc thợ săn, và vì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook as a small blue status window pops up above it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, hạng của thợ săn gần như là số phận, và chỉ một người t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a single upward arrow breaking through a ceiling of letters. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Cổng và hầm ngục

Lời: Theo truyện, khoảng mười năm trước câu chuyện chính, những cánh cổng bắt đầu xuất hiện khắp thế giới, nối tới…

```text
Wide 16:9 landscape cinematic frame. a world map with glowing portals appearing across continents like scattered stars. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Bên trong hầm ngục là quái vật. Cách duy nhất để đóng cổng là vào trong và tiêu diệt con trùm ở tầng sâu nhất.

```text
Wide 16:9 landscape cinematic frame. a dark cavern with a massive boss silhouette at the end of a long corridor, torches along the walls. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Nếu không ai vào dọn, sau một khoảng thời gian, quái vật sẽ tràn ra ngoài thế giới thực. Hiện tượng này gọi l…

```text
Wide 16:9 landscape cinematic frame. monsters pouring out of a shattered portal into a city street, people running. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Vì vậy việc dọn cổng không chỉ là kiếm tiền. Nó là trách nhiệm bảo vệ thành phố. Mỗi cổng bị bỏ quên là một t…

```text
Wide 16:9 landscape cinematic frame. a countdown clock projected above a glowing gate in an empty parking lot. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Cổng cũng được xếp hạng từ E đến S, dựa trên lượng ma lực nó tỏa ra. Cổng càng cao hạng, quái vật bên trong c…

```text
Wide 16:9 landscape cinematic frame. a row of gates of increasing size and glow, from a small faint portal to a huge blazing one. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Có một loại cổng đặc biệt nguy hiểm: cổng đỏ. Khi vào trong, không ai thoát ra được cho tới khi diệt xong trù…

```text
Wide 16:9 landscape cinematic frame. a crimson portal pulsing ominously in a snowy forest, hunters hesitating at its edge. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hệ thống cổng biến thế giới thành một trò chơi sinh tồn thật. Ai cũng biết luật, nhưng sai một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing nervously at the edge of a small glowing portal, holding a tiny sword. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Thợ săn và thức tỉnh

Lời: Cùng lúc cổng xuất hiện, một số người bắt đầu thức tỉnh sức mạnh. Họ được gọi là thợ săn.

```text
Wide 16:9 landscape cinematic frame. a person on a hospital bed suddenly surrounded by a faint glowing aura, doctors stepping back. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Khi thức tỉnh, cơ thể thợ săn có ma lực, giúp họ chiến đấu với quái vật mà vũ khí thông thường không làm được…

```text
Wide 16:9 landscape cinematic frame. a hunter swinging a glowing blade at a monster while bullets bounce off it harmlessly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Mỗi thợ săn được đo lượng ma lực khi thức tỉnh, và từ đó được xếp hạng từ E đến S bởi Hiệp hội thợ săn.

```text
Wide 16:9 landscape cinematic frame. a futuristic measuring device scanning a person's hand, a rank letter appearing on a screen. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Điều quan trọng nhất: theo truyện, hạng này gần như không đổi suốt đời. Sinh ra hạng E thì phần lớn sẽ mãi là…

```text
Wide 16:9 landscape cinematic frame. a rank card stamped with a large E, sealed in a glass frame. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Có hiện tượng tái thức tỉnh giúp thợ săn tăng hạng, nhưng nó cực hiếm. Với đa số, hạng là số phận.

```text
Wide 16:9 landscape cinematic frame. a rare shooting star over a crowd of hunters, only one looking up. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Thợ săn cũng chia theo vai trò: cận chiến, pháp sư, hồi phục, đỡ đòn, sát thủ, tầm xa. Một đội đi cổng cần đủ…

```text
Wide 16:9 landscape cinematic frame. a party of six silhouettes in a line: a tank with a shield, a mage, a healer, an assassin, a fighter, an archer. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Bậc thang cấp bậc

Lời: Giờ cùng đi từ đáy lên đỉnh bậc thang cấp bậc để thấy khoảng cách giữa các hạng lớn tới đâu.

```text
Wide 16:9 landscape cinematic frame. a tall staircase of glowing tiers rising into clouds, each tier labeled with a letter. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Hạng E là thấp nhất. Sức mạnh chỉ nhỉnh hơn người thường một chút, thường chỉ dọn được những cổng dễ nhất, và…

```text
Wide 16:9 landscape cinematic frame. a nervous low-rank hunter holding a dagger at the entrance of a small dim cave. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Hạng D và C là lực lượng đông đảo. Họ đi thành nhóm để dọn các cổng trung bình, kiếm sống bằng nghề thợ săn.

```text
Wide 16:9 landscape cinematic frame. a group of mid-rank hunters walking together toward a medium-sized portal. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Hạng B và A là tinh anh. Các hội thợ săn lớn tranh giành họ, trả những khoản tiền rất lớn để có họ trong đội.

```text
Wide 16:9 landscape cinematic frame. elite hunters in sleek gear being greeted by guild representatives in a modern lobby. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Hạng S là hàng hiếm hoi mạnh nhất. Mỗi quốc gia chỉ có vài người, và sức mạnh của họ được xem như tài sản quố…

```text
Wide 16:9 landscape cinematic frame. a single S-rank hunter silhouette standing on a rooftop, the city skyline below. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Và vượt trên cả hạng S là những thợ săn cấp quốc gia, những người mạnh đến mức một mình họ đủ thay đổi cán câ…

```text
Wide 16:9 landscape cinematic frame. a few towering silhouettes above a globe, each standing over a different region. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Khoảng cách giữa các hạng không phải là cộng thêm một chút. Một hạng S có thể mạnh hơn cả trăm hạng thấp cộng…

```text
Wide 16:9 landscape cinematic frame. a balance scale with one glowing figure on one side outweighing a crowd on the other. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: bậc thang này giống một xã hội phân tầng. Hạng không chỉ là sức mạnh, mà còn là tiền bạc, địa v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing on the lowest step looking up at a very long staircase. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Hội thợ săn và kinh tế

Lời: Vì cổng xuất hiện liên tục, thợ săn trở thành một nghề, và hội thợ săn trở thành những công ty khổng lồ.

```text
Wide 16:9 landscape cinematic frame. a modern skyscraper with a guild emblem glowing at the top, hunters walking in and out. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Các hội nhận hợp đồng dọn cổng, thu thập đá ma lực từ quái vật và bán lại. Đá ma lực là nguồn năng lượng quý…

```text
Wide 16:9 landscape cinematic frame. a pile of glowing crystals being loaded into armored trucks outside a portal. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Thợ săn hạng thấp thường làm thuê cho các hội, nhận phần tiền nhỏ và gánh rủi ro lớn. Đó là thực tế khắc nghi…

```text
Wide 16:9 landscape cinematic frame. tired low-rank hunters receiving small envelopes from a manager at a folding table. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Hiệp hội thợ săn quản lý và kiểm soát tất cả, xếp hạng thợ săn, phân loại cổng, và can thiệp khi có thảm họa.

```text
Wide 16:9 landscape cinematic frame. an official command center with screens showing gate locations across a city map. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Chi tiết kinh tế này làm thế giới Solo Leveling giống một xã hội thật. Sức mạnh gắn liền với tiền, và tiền gắ…

```text
Wide 16:9 landscape cinematic frame. a split image: a luxurious penthouse and a cramped apartment, both lit by the glow of distant portals. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Người thay đổi luật chơi: Hệ thống

Lời: Và giờ tới lý do cả bộ truyện tồn tại: Sung Jinwoo, thợ săn hạng E được gọi là yếu nhất nhân loại.

```text
Wide 16:9 landscape cinematic frame. a young hunter in worn gear with bandages, standing alone at the back of a group. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trong một hầm ngục kép bí ẩn, gần như cả đội bị giết. Jinwoo sống sót, và một màn hình xanh xuất hiện trước m…

```text
Wide 16:9 landscape cinematic frame. a dark temple chamber with giant statues, a single blue translucent window glowing in front of a wounded figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Đó là Hệ thống, thứ biến cuộc đời anh thành một trò chơi thật sự: có nhiệm vụ, có cấp độ, có chỉ số, có phần…

```text
Wide 16:9 landscape cinematic frame. a floating game-like status window with bars and numbers glowing blue, no readable text. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Mỗi ngày, Hệ thống giao nhiệm vụ tập luyện: chống đẩy, gập bụng, squat và chạy bộ. Không hoàn thành thì bị ph…

```text
Wide 16:9 landscape cinematic frame. a young man doing push-ups at night in a small room while a blue window counts beside him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhờ Hệ thống, Jinwoo làm được điều mà thế giới cho là không thể: lên cấp. Anh mạnh dần lên, không có giới hạn.

```text
Wide 16:9 landscape cinematic frame. a level bar filling repeatedly while a silhouette grows taller and stronger with each level. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Đây chính là cú phá luật của Solo Leveling. Trong khi mọi thợ săn khác bị khóa trong hạng của mình, Jinwoo là…

```text
Wide 16:9 landscape cinematic frame. a figure climbing a staircase that extends upward while all others stand frozen on their steps. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: sức hấp dẫn của Solo Leveling nằm ở đây. Ai cũng từng cảm thấy mình yếu, và ai cũng mơ có một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot doing a tiny push-up with a small blue window cheering it on. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Chỉ số và kỹ năng của Hệ thống

Lời: Hệ thống của Jinwoo vận hành giống hệt một trò chơi nhập vai, với các chỉ số mà người chơi game nào cũng quen.

```text
Wide 16:9 landscape cinematic frame. a glowing status window with five stat bars and small icons, no readable text. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Có sức mạnh cho những cú đánh nặng, nhanh nhẹn cho tốc độ, thể lực cho độ bền, trí tuệ cho ma lực, và giác qu…

```text
Wide 16:9 landscape cinematic frame. five icons in a row: a fist, a running shoe, a heart, a brain, and an eye, each glowing blue. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Mỗi lần lên cấp, Jinwoo nhận điểm để tự phân bổ vào chỉ số. Anh quyết định mình sẽ mạnh lên theo hướng nào.

```text
Wide 16:9 landscape cinematic frame. a hand dragging glowing points into different stat bars on a floating screen. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Hệ thống còn cho kỹ năng: lao nhanh, ẩn thân, và sau này là những kỹ năng dùng ma lực điều khiển vật từ xa.

```text
Wide 16:9 landscape cinematic frame. a figure blurring forward in a dash, another fading into invisibility, a third lifting objects with an invisible force. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Có cả cửa hàng và vật phẩm: bình hồi máu, vũ khí rơi ra từ trùm, trang bị tăng chỉ số. Jinwoo chuẩn bị cho mỗ…

```text
Wide 16:9 landscape cinematic frame. an inventory grid with glowing potions, a curved dagger, and a pair of boots. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: điều đặc biệt là chỉ Jinwoo nhìn thấy Hệ thống. Với người khác, anh chỉ đơn giản là mạnh lên mộ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a blue window while other characters around it see nothing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Những cổng đáng nhớ

Lời: Hành trình của Jinwoo được đánh dấu bằng những cổng đáng nhớ, mỗi cổng là một bước ngoặt.

```text
Wide 16:9 landscape cinematic frame. a timeline of five portals of different colors along a winding road. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Hầm ngục kép là nơi mọi chuyện bắt đầu: một ngôi đền với những bức tượng giết người theo luật lệ bí ẩn. Sống…

```text
Wide 16:9 landscape cinematic frame. a vast temple with towering statues holding weapons, candles in a circle on the floor. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Nhiệm vụ đổi nghề là lúc Jinwoo đối đầu một hiệp sĩ bóng tối mạnh mẽ, và sau khi thắng, hiệp sĩ đó trở thành…

```text
Wide 16:9 landscape cinematic frame. a lone figure facing a crimson-plumed dark knight in an empty throne room. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Cổng đỏ là nơi cả đội bị mắc kẹt trong một thế giới băng giá, và thời gian bên trong kéo dài hơn bên ngoài rấ…

```text
Wide 16:9 landscape cinematic frame. a snowy wasteland under a red sky, a small group of hunters huddled together. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Lâu đài quỷ là một hầm ngục đặc biệt nhiều tầng mà Jinwoo leo lên để tìm thứ có thể cứu mẹ mình. Đây là động…

```text
Wide 16:9 landscape cinematic frame. a towering dark castle with many floors, a lone figure climbing toward the top. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Và arc đảo Jeju là trận chiến quy mô quốc gia, nơi thế giới lần đầu thấy sức mạnh thật sự của người từng được…

```text
Wide 16:9 landscape cinematic frame. a volcanic island under a stormy sky, a lone figure leading a shadow army against giant insects. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Chủ nhân bóng tối

Lời: Khi đủ cấp, Jinwoo được chọn một nghề mới. Anh trở thành Thuật sĩ bóng tối, với năng lực đặc biệt nhất truyện…

```text
Wide 16:9 landscape cinematic frame. a dark figure raising a hand as shadows gather into humanoid shapes around him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Với năng lực này, Jinwoo có thể lấy bóng của quái vật hay chiến binh đã bị đánh bại, biến chúng thành binh lí…

```text
Wide 16:9 landscape cinematic frame. shadow soldiers rising from the ground of a battlefield, kneeling before a lone figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Đội quân bóng tối lớn dần theo mỗi trận chiến. Có hiệp sĩ, có sát thủ, có cả những sinh vật khổng lồ từng là…

```text
Wide 16:9 landscape cinematic frame. an army of dark silhouettes with glowing purple eyes lined up behind their commander. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Bóng binh không chết theo cách thông thường. Bị tiêu diệt, chúng có thể được triệu hồi lại khi chủ nhân còn đ…

```text
Wide 16:9 landscape cinematic frame. a shadow soldier dissolving into smoke and reforming a moment later beside its master. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Ở arc đảo Jeju, Jinwoo đối đầu với đàn kiến khổng lồ, và một trong số đó sau này trở thành binh lính bóng tối…

```text
Wide 16:9 landscape cinematic frame. a giant insect-like creature with wings kneeling in shadow form beside a lone figure on a volcanic island. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: năng lực này cực kỳ mạnh vì nó cộng dồn. Mỗi trận thắng không chỉ làm anh mạnh hơn, mà còn cho…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adding small shadow figures to a growing line on a chalkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Vì sao hạng S cũng phải dè chừng

Lời: Có một cảnh làm fan nhớ mãi: khi các thợ săn hạng S bắt đầu nhận ra một người từng hạng E giờ mạnh hơn cả họ.

```text
Wide 16:9 landscape cinematic frame. a group of elite hunters looking stunned at a calm figure walking past them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Khi Jinwoo tái đánh giá, thiết bị đo cho thấy anh đã vượt lên hạng S. Nhưng thực tế, sức mạnh của anh còn tăn…

```text
Wide 16:9 landscape cinematic frame. a measuring device overloading with sparks as a figure places his hand on it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Điều này làm lộ ra lỗ hổng của hệ thống xếp hạng: nó chỉ đo được ma lực tại một thời điểm, không đo được khả…

```text
Wide 16:9 landscape cinematic frame. a ruler trying to measure a growing tree that keeps extending past its end. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nói cách khác, hệ thống xếp hạng hợp với một thế giới đứng yên. Còn Jinwoo là thứ duy nhất trong thế giới đó…

```text
Wide 16:9 landscape cinematic frame. a still photograph of a crowd with one figure blurred in motion walking forward. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Thử nghiệm: bạn thức tỉnh ở hạng nào?

Lời: Thử tưởng tượng bạn thức tỉnh trong thế giới Solo Leveling. Mỗi hạng sẽ cho bạn một cuộc sống rất khác.

```text
Wide 16:9 landscape cinematic frame. a person standing before a measuring device, six possible letters floating around them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nếu bạn hạng E hoặc D, có lẽ an toàn nhất là làm hậu cần cho hội thợ săn, hoặc chỉ nhận các cổng dễ. Đừng liề…

```text
Wide 16:9 landscape cinematic frame. a low-rank hunter carrying supplies and smiling safely outside a portal. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Nếu bạn hạng C hoặc B, bạn có thể sống tốt bằng nghề thợ săn, miễn là chọn đội tốt và biết rút lui khi cổng q…

```text
Wide 16:9 landscape cinematic frame. a mid-rank party carefully retreating from a portal that glows too brightly. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nếu bạn hạng A hoặc S, các hội lớn sẽ tranh nhau mời bạn. Nhưng bạn cũng sẽ bị gọi vào những thảm họa lớn nhấ…

```text
Wide 16:9 landscape cinematic frame. an elite hunter receiving multiple glowing contract offers while an alarm flashes in the distance. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · **Kaku** (đính kèm ảnh mẫu)

Lời: Còn nếu một màn hình xanh xuất hiện trước mắt bạn, thì chúc mừng, bạn là nhân vật chính. Nhưng nhớ làm đủ nhi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a small blue window with a push-up icon, looking tired. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Những hiểu lầm về hệ thống

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về thế giới Solo Leveling.

```text
Wide 16:9 landscape cinematic frame. a notice board with four pinned cards marked with question marks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Hiểu lầm một: thợ săn nào cũng có Hệ thống như Jinwoo. Không, trong truyện anh là trường hợp duy nhất được bi…

```text
Wide 16:9 landscape cinematic frame. a single glowing blue window above one figure among a crowd of hunters without any. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Hiểu lầm hai: hạng S là giới hạn cao nhất. Trên hạng S còn có thợ săn cấp quốc gia, và sau đó còn những thế l…

```text
Wide 16:9 landscape cinematic frame. a staircase continuing above the S tier into darker clouds. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hiểu lầm ba: cổng hạng thấp thì an toàn. Hầm ngục kép ban đầu được xếp hạng thấp, nhưng suýt giết cả đội.

```text
Wide 16:9 landscape cinematic frame. a small harmless-looking portal with a massive shadow looming behind it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hiểu lầm bốn: Jinwoo mạnh chỉ nhờ may mắn. Hệ thống cho cơ hội, nhưng anh phải hoàn thành nhiệm vụ mỗi ngày v…

```text
Wide 16:9 landscape cinematic frame. a young man training alone in the rain at night, determined expression, blue window beside him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Bài học đời thực: nhiệm vụ hằng ngày

Lời: Có một lý do khác khiến fan yêu Solo Leveling, và nó nằm ngoài màn hình: nhiệm vụ hằng ngày.

```text
Wide 16:9 landscape cinematic frame. a phone screen showing a simple daily checklist next to running shoes by a door at dawn. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Rất nhiều người xem đã tự tạo nhiệm vụ hằng ngày của riêng mình: chống đẩy, chạy bộ, đọc sách, học ngoại ngữ,…

```text
Wide 16:9 landscape cinematic frame. a montage of everyday people doing push-ups, jogging, reading, and studying at sunrise. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Thông điệp ở đây rất đơn giản: những việc nhỏ lặp lại mỗi ngày sẽ cộng dồn thành thay đổi lớn. Lên cấp không…

```text
Wide 16:9 landscape cinematic frame. a stack of small glowing blocks building up into a tall tower over many days. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Tất nhiên ngoài đời không có màn hình xanh báo điểm. Nhưng bạn có thể tự ghi lại tiến bộ của mình, và cảm giá…

```text
Wide 16:9 landscape cinematic frame. a notebook with daily check marks filling page after page. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử làm nhiệm vụ hằng ngày: mỗi ngày đọc một chương sách. Đến giờ, cuốn sổ của Kaku đã dày lên đáng kể.

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding a thick notebook with many bookmarks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku: vì sao hệ thống này cuốn hút · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao hệ thống của Solo Leveling lại cuốn hút hàng triệu người, dù ý tưởng cổng và xếp hạng không quá mới?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of game controllers and books, thinking. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Lý do một: nó rất dễ hiểu. Chữ cái từ E đến S ai nhìn cũng biết ngay ai mạnh, ai yếu. Người xem không cần học…

```text
Wide 16:9 landscape cinematic frame. a simple glowing letter scale that anyone can read at a glance. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Lý do hai: nó biến cảm giác chơi game thành truyện. Lên cấp, tăng chỉ số, nhận phần thưởng đều tạo cảm giác t…

```text
Wide 16:9 landscape cinematic frame. a level-up burst of blue light with numbers rising, a figure grinning. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Lý do ba: nó có kẻ yếu vươn lên. Một thế giới cứng nhắc làm cho sự vươn lên của một người trở nên đặc biệt.

```text
Wide 16:9 landscape cinematic frame. a small figure breaking through a glass ceiling marked with letters. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Nhưng cũng có điểm yếu: khi nhân vật chính mạnh vượt xa mọi người, các trận đấu dễ mất căng thẳng. Truyện bù…

```text
Wide 16:9 landscape cinematic frame. a lone powerful figure standing among defeated enemies, a larger shadow looming on the horizon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: So với Nen, nơi luật và giao ước quyết định trận đấu, Solo Leveling đơn giản hơn nhiều. Nhưng sự đơn giản đó…

```text
Wide 16:9 landscape cinematic frame. a complex glowing hexagon beside a simple blue level bar, both glowing equally bright. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Vì sao cổng xuất hiện?

Lời: Một câu hỏi lớn mà người xem mới hay đặt ra: vì sao cổng lại xuất hiện? Ai hay cái gì đứng sau chúng?

```text
Wide 16:9 landscape cinematic frame. a night sky filled with faint portal outlines, a question mark formed by stars. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Trong phần đầu câu chuyện, không ai biết. Con người chỉ biết cách sống chung với cổng: đo, phân loại, dọn dẹp…

```text
Wide 16:9 landscape cinematic frame. scientists and hunters studying a portal with instruments, taking notes in the dark. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Dần dần, truyện hé lộ rằng cổng và Hệ thống có liên quan tới những thế lực lớn hơn loài người rất nhiều. Mình…

```text
Wide 16:9 landscape cinematic frame. vast shadowy figures looming beyond the clouds, watching the world below. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Điều đáng chú ý là cách truyện dẫn dắt: bắt đầu từ góc nhìn của một thợ săn yếu nhất, rồi mở rộng dần ra nhữn…

```text
Wide 16:9 landscape cinematic frame. a camera-like view zooming out from a single hunter to a city, to a country, to the whole planet. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Nhờ vậy, mỗi lần Jinwoo mạnh lên, người xem cũng được thấy thêm một phần sự thật. Sức mạnh và bí ẩn lớn lên c…

```text
Wide 16:9 landscape cinematic frame. a figure climbing a staircase where each new step reveals a larger view of a mysterious sky. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: nếu bạn muốn một video riêng về bí ẩn của cổng và những thế lực đứng sau, có spoiler đầy đủ, hãy b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a sealed envelope with a spoiler stamp. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Nếu Solo Leveling có phần tiếp theo trong đời bạn

Lời: Trước khi tổng kết, Kaku muốn bàn một câu hỏi nhỏ: vì sao câu chuyện về một người lên cấp lại khiến nhiều ngư…

```text
Wide 16:9 landscape cinematic frame. a young person looking at their reflection in a window at night, a faint blue glow on the glass. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Có lẽ vì Solo Leveling nói điều mà ai cũng muốn nghe: vị trí xuất phát không quyết định vị trí kết thúc.

```text
Wide 16:9 landscape cinematic frame. a runner at the very back of a starting line, a long glowing road ahead. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Trong truyện, người khác bị khóa ở hạng của mình. Ngoài đời, may mắn là chúng ta không bị khóa như vậy. Ai cũ…

```text
Wide 16:9 landscape cinematic frame. a staircase with no labels where many different people climb at their own pace. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và đó là lý do Kaku nghĩ nhiệm vụ hằng ngày là bài học hay nhất của bộ truyện, hay hơn cả những trận đấu hoàn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot ticking off a small daily checklist with a feather pen. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · Tóm tắt

Lời: Tóm lại: cổng mở ra hầm ngục, không dọn kịp thì quái vật tràn ra. Cổng và thợ săn đều được xếp hạng từ E đến…

```text
Wide 16:9 landscape cinematic frame. a summary card with a portal, a monster icon, and a ladder of letters. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94

Lời: Hạng thợ săn gần như cố định suốt đời, và nó quyết định tiền bạc, địa vị và sự an toàn của họ.

```text
Wide 16:9 landscape cinematic frame. a rank card sealed in glass next to a stack of coins. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95

Lời: Jinwoo phá vỡ luật đó nhờ Hệ thống, rồi trở thành chủ nhân của một đội quân bóng tối ngày càng lớn.

```text
Wide 16:9 landscape cinematic frame. a lone figure at the top of a staircase with an army of shadows behind him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu thức tỉnh, bạn muốn đóng vai trò nào trong đội: đỡ đòn, pháp sư, hồi phục hay sát thủ? V…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up four small role cards: a shield, a staff, a cross, a dagger. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s97 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã sự tiến hóa của Sharingan trong Naruto.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing red eye symbol with three marks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s98 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye beside a softly glowing blue portal. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cổng và hầm ngục

Khoảng 131 giây · cảnh s01–s13 · 1705 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Solo Leveling đến hết phần anime mùa hai, gồm cả arc đảo Jeju. Nếu chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Hãy tưởng tượng một thế giới mà cánh cổng tới hầm ngục có thể mở ra giữa ngã tư đường phố bất cứ lúc nào. Và bên trong là quái vật.

<short pause> Trong thế giới đó, con người được xếp hạng như trong một trò chơi: E, D, C, B, A, S. Hạng của bạn quyết định bạn sống hay chết.

<short pause> Và ở đáy bậc thang ấy có một người được gọi là thợ săn yếu nhất nhân loại. Rồi một ngày, anh ta bắt đầu lên cấp.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã hệ thống của Solo Leveling: cổng, cấp bậc thợ săn, và vì sao Hệ thống của Jinwoo phá vỡ mọi quy tắc.

<short pause> Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, hạng của thợ săn gần như là số phận, và chỉ một người thoát khỏi số phận đó.

<short pause> Theo truyện, khoảng mười năm trước câu chuyện chính, những cánh cổng bắt đầu xuất hiện khắp thế giới, nối tới những không gian gọi là hầm ngục.

<short pause> Bên trong hầm ngục là quái vật. Cách duy nhất để đóng cổng là vào trong và tiêu diệt con trùm ở tầng sâu nhất.

<short pause> Nếu không ai vào dọn, sau một khoảng thời gian, quái vật sẽ tràn ra ngoài thế giới thực. Hiện tượng này gọi là vỡ hầm ngục.

<short pause> Vì vậy việc dọn cổng không chỉ là kiếm tiền. Nó là trách nhiệm bảo vệ thành phố. Mỗi cổng bị bỏ quên là một thảm họa đang đếm ngược.

<short pause> Cổng cũng được xếp hạng từ E đến S, dựa trên lượng ma lực nó tỏa ra. Cổng càng cao hạng, quái vật bên trong càng mạnh.

<short pause> Có một loại cổng đặc biệt nguy hiểm: cổng đỏ. Khi vào trong, không ai thoát ra được cho tới khi diệt xong trùm, và thời gian bên trong trôi khác bên ngoài.

<short pause> Kaku ghi chú: hệ thống cổng biến thế giới thành một trò chơi sinh tồn thật. Ai cũng biết luật, nhưng sai một bước là không có nút chơi lại.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Solo Leveling đến hết phần anime mùa hai, gồm cả arc đảo Jeju. Nếu chưa xem tới đó, hãy lưu video lại nhé.

[pause] Hãy tưởng tượng một thế giới mà cánh cổng tới hầm ngục có thể mở ra giữa ngã tư đường phố bất cứ lúc nào. Và bên trong là quái vật.

[pause] Trong thế giới đó, con người được xếp hạng như trong một trò chơi: E, D, C, B, A, S. Hạng của bạn quyết định bạn sống hay chết.

[pause] Và ở đáy bậc thang ấy có một người được gọi là thợ săn yếu nhất nhân loại. Rồi một ngày, anh ta bắt đầu lên cấp.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã hệ thống của Solo Leveling: cổng, cấp bậc thợ săn, và vì sao Hệ thống của Jinwoo phá vỡ mọi quy tắc.

[pause] Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, hạng của thợ săn gần như là số phận, và chỉ một người thoát khỏi số phận đó.

[pause] Theo truyện, khoảng mười năm trước câu chuyện chính, những cánh cổng bắt đầu xuất hiện khắp thế giới, nối tới những không gian gọi là hầm ngục.

[pause] Bên trong hầm ngục là quái vật. Cách duy nhất để đóng cổng là vào trong và tiêu diệt con trùm ở tầng sâu nhất.

[pause] Nếu không ai vào dọn, sau một khoảng thời gian, quái vật sẽ tràn ra ngoài thế giới thực. Hiện tượng này gọi là vỡ hầm ngục.

[pause] Vì vậy việc dọn cổng không chỉ là kiếm tiền. Nó là trách nhiệm bảo vệ thành phố. Mỗi cổng bị bỏ quên là một thảm họa đang đếm ngược.

[pause] Cổng cũng được xếp hạng từ E đến S, dựa trên lượng ma lực nó tỏa ra. Cổng càng cao hạng, quái vật bên trong càng mạnh.

[pause] Có một loại cổng đặc biệt nguy hiểm: cổng đỏ. Khi vào trong, không ai thoát ra được cho tới khi diệt xong trùm, và thời gian bên trong trôi khác bên ngoài.

[pause] Kaku ghi chú: hệ thống cổng biến thế giới thành một trò chơi sinh tồn thật. Ai cũng biết luật, nhưng sai một bước là không có nút chơi lại.
```

### c02 · Thợ săn và thức tỉnh / Bậc thang cấp bậc

Khoảng 123 giây · cảnh s14–s27 · 1599 ký tự

**Gemini**

```text
Cùng lúc cổng xuất hiện, một số người bắt đầu thức tỉnh sức mạnh. Họ được gọi là thợ săn.

<short pause> Khi thức tỉnh, cơ thể thợ săn có ma lực, giúp họ chiến đấu với quái vật mà vũ khí thông thường không làm được gì.

<short pause> Mỗi thợ săn được đo lượng ma lực khi thức tỉnh, và từ đó được xếp hạng từ E đến S bởi Hiệp hội thợ săn.

<short pause> Điều quan trọng nhất: theo truyện, hạng này gần như không đổi suốt đời. Sinh ra hạng E thì phần lớn sẽ mãi là hạng E.

<short pause> Có hiện tượng tái thức tỉnh giúp thợ săn tăng hạng, nhưng nó cực hiếm. Với đa số, hạng là số phận.

<short pause> Thợ săn cũng chia theo vai trò: cận chiến, pháp sư, hồi phục, đỡ đòn, sát thủ, tầm xa. Một đội đi cổng cần đủ các vai trò để sống sót.

<short pause> Giờ cùng đi từ đáy lên đỉnh bậc thang cấp bậc để thấy khoảng cách giữa các hạng lớn tới đâu.

<short pause> Hạng E là thấp nhất. Sức mạnh chỉ nhỉnh hơn người thường một chút, thường chỉ dọn được những cổng dễ nhất, và vẫn có thể chết nếu xui.

<short pause> Hạng D và C là lực lượng đông đảo. Họ đi thành nhóm để dọn các cổng trung bình, kiếm sống bằng nghề thợ săn.

<short pause> Hạng B và A là tinh anh. Các hội thợ săn lớn tranh giành họ, trả những khoản tiền rất lớn để có họ trong đội.

<short pause> Hạng S là hàng hiếm hoi mạnh nhất. Mỗi quốc gia chỉ có vài người, và sức mạnh của họ được xem như tài sản quốc gia.

<short pause> Và vượt trên cả hạng S là những thợ săn cấp quốc gia, những người mạnh đến mức một mình họ đủ thay đổi cán cân quyền lực giữa các nước.

<short pause> Khoảng cách giữa các hạng không phải là cộng thêm một chút. Một hạng S có thể mạnh hơn cả trăm hạng thấp cộng lại.

<short pause> <laugh> Kaku tóm lại: bậc thang này giống một xã hội phân tầng. Hạng không chỉ là sức mạnh, mà còn là tiền bạc, địa vị và quyền được sống an toàn.
```

**ElevenLabs**

```text
Cùng lúc cổng xuất hiện, một số người bắt đầu thức tỉnh sức mạnh. Họ được gọi là thợ săn.

[pause] Khi thức tỉnh, cơ thể thợ săn có ma lực, giúp họ chiến đấu với quái vật mà vũ khí thông thường không làm được gì.

[pause] Mỗi thợ săn được đo lượng ma lực khi thức tỉnh, và từ đó được xếp hạng từ E đến S bởi Hiệp hội thợ săn.

[pause] Điều quan trọng nhất: theo truyện, hạng này gần như không đổi suốt đời. Sinh ra hạng E thì phần lớn sẽ mãi là hạng E.

[pause] Có hiện tượng tái thức tỉnh giúp thợ săn tăng hạng, nhưng nó cực hiếm. Với đa số, hạng là số phận.

[pause] Thợ săn cũng chia theo vai trò: cận chiến, pháp sư, hồi phục, đỡ đòn, sát thủ, tầm xa. Một đội đi cổng cần đủ các vai trò để sống sót.

[pause] Giờ cùng đi từ đáy lên đỉnh bậc thang cấp bậc để thấy khoảng cách giữa các hạng lớn tới đâu.

[pause] Hạng E là thấp nhất. Sức mạnh chỉ nhỉnh hơn người thường một chút, thường chỉ dọn được những cổng dễ nhất, và vẫn có thể chết nếu xui.

[pause] Hạng D và C là lực lượng đông đảo. Họ đi thành nhóm để dọn các cổng trung bình, kiếm sống bằng nghề thợ săn.

[pause] Hạng B và A là tinh anh. Các hội thợ săn lớn tranh giành họ, trả những khoản tiền rất lớn để có họ trong đội.

[pause] Hạng S là hàng hiếm hoi mạnh nhất. Mỗi quốc gia chỉ có vài người, và sức mạnh của họ được xem như tài sản quốc gia.

[pause] Và vượt trên cả hạng S là những thợ săn cấp quốc gia, những người mạnh đến mức một mình họ đủ thay đổi cán cân quyền lực giữa các nước.

[pause] Khoảng cách giữa các hạng không phải là cộng thêm một chút. Một hạng S có thể mạnh hơn cả trăm hạng thấp cộng lại.

[pause] [chuckles] Kaku tóm lại: bậc thang này giống một xã hội phân tầng. Hạng không chỉ là sức mạnh, mà còn là tiền bạc, địa vị và quyền được sống an toàn.
```

### c03 · Hội thợ săn và kinh tế / Người thay đổi luật chơi: Hệ thống

Khoảng 113 giây · cảnh s28–s39 · 1463 ký tự

**Gemini**

```text
Vì cổng xuất hiện liên tục, thợ săn trở thành một nghề, và hội thợ săn trở thành những công ty khổng lồ.

<short pause> Các hội nhận hợp đồng dọn cổng, thu thập đá ma lực từ quái vật và bán lại. Đá ma lực là nguồn năng lượng quý của thế giới này.

<short pause> Thợ săn hạng thấp thường làm thuê cho các hội, nhận phần tiền nhỏ và gánh rủi ro lớn. Đó là thực tế khắc nghiệt ở đáy bậc thang.

<short pause> Hiệp hội thợ săn quản lý và kiểm soát tất cả, xếp hạng thợ săn, phân loại cổng, và can thiệp khi có thảm họa.

<short pause> Chi tiết kinh tế này làm thế giới Solo Leveling giống một xã hội thật. Sức mạnh gắn liền với tiền, và tiền gắn liền với quyền lực.

<short pause> Và giờ tới lý do cả bộ truyện tồn tại: Sung Jinwoo, thợ săn hạng E được gọi là yếu nhất nhân loại.

<short pause> Trong một hầm ngục kép bí ẩn, gần như cả đội bị giết. Jinwoo sống sót, và một màn hình xanh xuất hiện trước mắt anh.

<short pause> Đó là Hệ thống, thứ biến cuộc đời anh thành một trò chơi thật sự: có nhiệm vụ, có cấp độ, có chỉ số, có phần thưởng.

<short pause> Mỗi ngày, Hệ thống giao nhiệm vụ tập luyện: chống đẩy, gập bụng, squat và chạy bộ. Không hoàn thành thì bị phạt trong một vùng đất nguy hiểm.

<short pause> Nhờ Hệ thống, Jinwoo làm được điều mà thế giới cho là không thể: lên cấp. Anh mạnh dần lên, không có giới hạn.

<short pause> Đây chính là cú phá luật của Solo Leveling. Trong khi mọi thợ săn khác bị khóa trong hạng của mình, Jinwoo là người duy nhất có thể leo lên.

<short pause> <laugh> Kaku nhận xét: sức hấp dẫn của Solo Leveling nằm ở đây. Ai cũng từng cảm thấy mình yếu, và ai cũng mơ có một hệ thống giúp mình lên cấp mỗi ngày.
```

**ElevenLabs**

```text
Vì cổng xuất hiện liên tục, thợ săn trở thành một nghề, và hội thợ săn trở thành những công ty khổng lồ.

[pause] Các hội nhận hợp đồng dọn cổng, thu thập đá ma lực từ quái vật và bán lại. Đá ma lực là nguồn năng lượng quý của thế giới này.

[pause] Thợ săn hạng thấp thường làm thuê cho các hội, nhận phần tiền nhỏ và gánh rủi ro lớn. Đó là thực tế khắc nghiệt ở đáy bậc thang.

[pause] Hiệp hội thợ săn quản lý và kiểm soát tất cả, xếp hạng thợ săn, phân loại cổng, và can thiệp khi có thảm họa.

[pause] Chi tiết kinh tế này làm thế giới Solo Leveling giống một xã hội thật. Sức mạnh gắn liền với tiền, và tiền gắn liền với quyền lực.

[pause] Và giờ tới lý do cả bộ truyện tồn tại: Sung Jinwoo, thợ săn hạng E được gọi là yếu nhất nhân loại.

[pause] Trong một hầm ngục kép bí ẩn, gần như cả đội bị giết. Jinwoo sống sót, và một màn hình xanh xuất hiện trước mắt anh.

[pause] Đó là Hệ thống, thứ biến cuộc đời anh thành một trò chơi thật sự: có nhiệm vụ, có cấp độ, có chỉ số, có phần thưởng.

[pause] Mỗi ngày, Hệ thống giao nhiệm vụ tập luyện: chống đẩy, gập bụng, squat và chạy bộ. Không hoàn thành thì bị phạt trong một vùng đất nguy hiểm.

[pause] Nhờ Hệ thống, Jinwoo làm được điều mà thế giới cho là không thể: lên cấp. Anh mạnh dần lên, không có giới hạn.

[pause] Đây chính là cú phá luật của Solo Leveling. Trong khi mọi thợ săn khác bị khóa trong hạng của mình, Jinwoo là người duy nhất có thể leo lên.

[pause] [chuckles] Kaku nhận xét: sức hấp dẫn của Solo Leveling nằm ở đây. Ai cũng từng cảm thấy mình yếu, và ai cũng mơ có một hệ thống giúp mình lên cấp mỗi ngày.
```

### c04 · Chỉ số và kỹ năng của Hệ thống / Những cổng đáng nhớ

Khoảng 113 giây · cảnh s40–s51 · 1470 ký tự

**Gemini**

```text
Hệ thống của Jinwoo vận hành giống hệt một trò chơi nhập vai, với các chỉ số mà người chơi game nào cũng quen.

<short pause> Có sức mạnh cho những cú đánh nặng, nhanh nhẹn cho tốc độ, thể lực cho độ bền, trí tuệ cho ma lực, và giác quan để cảm nhận nguy hiểm.

<short pause> Mỗi lần lên cấp, Jinwoo nhận điểm để tự phân bổ vào chỉ số. Anh quyết định mình sẽ mạnh lên theo hướng nào.

<short pause> Hệ thống còn cho kỹ năng: lao nhanh, ẩn thân, và sau này là những kỹ năng dùng ma lực điều khiển vật từ xa.

<short pause> Có cả cửa hàng và vật phẩm: bình hồi máu, vũ khí rơi ra từ trùm, trang bị tăng chỉ số. Jinwoo chuẩn bị cho mỗi trận như một game thủ.

<short pause> <laugh> Kaku ghi chú: điều đặc biệt là chỉ Jinwoo nhìn thấy Hệ thống. Với người khác, anh chỉ đơn giản là mạnh lên một cách khó hiểu.

<short pause> Hành trình của Jinwoo được đánh dấu bằng những cổng đáng nhớ, mỗi cổng là một bước ngoặt.

<short pause> Hầm ngục kép là nơi mọi chuyện bắt đầu: một ngôi đền với những bức tượng giết người theo luật lệ bí ẩn. Sống sót ở đó là điều kiện để nhận Hệ thống.

<short pause> Nhiệm vụ đổi nghề là lúc Jinwoo đối đầu một hiệp sĩ bóng tối mạnh mẽ, và sau khi thắng, hiệp sĩ đó trở thành bóng binh đầu tiên của anh.

<short pause> Cổng đỏ là nơi cả đội bị mắc kẹt trong một thế giới băng giá, và thời gian bên trong kéo dài hơn bên ngoài rất nhiều.

<short pause> Lâu đài quỷ là một hầm ngục đặc biệt nhiều tầng mà Jinwoo leo lên để tìm thứ có thể cứu mẹ mình. Đây là động lực cảm xúc lớn nhất của anh.

<short pause> Và arc đảo Jeju là trận chiến quy mô quốc gia, nơi thế giới lần đầu thấy sức mạnh thật sự của người từng được gọi là yếu nhất.
```

**ElevenLabs**

```text
Hệ thống của Jinwoo vận hành giống hệt một trò chơi nhập vai, với các chỉ số mà người chơi game nào cũng quen.

[pause] Có sức mạnh cho những cú đánh nặng, nhanh nhẹn cho tốc độ, thể lực cho độ bền, trí tuệ cho ma lực, và giác quan để cảm nhận nguy hiểm.

[pause] Mỗi lần lên cấp, Jinwoo nhận điểm để tự phân bổ vào chỉ số. Anh quyết định mình sẽ mạnh lên theo hướng nào.

[pause] Hệ thống còn cho kỹ năng: lao nhanh, ẩn thân, và sau này là những kỹ năng dùng ma lực điều khiển vật từ xa.

[pause] Có cả cửa hàng và vật phẩm: bình hồi máu, vũ khí rơi ra từ trùm, trang bị tăng chỉ số. Jinwoo chuẩn bị cho mỗi trận như một game thủ.

[pause] [chuckles] Kaku ghi chú: điều đặc biệt là chỉ Jinwoo nhìn thấy Hệ thống. Với người khác, anh chỉ đơn giản là mạnh lên một cách khó hiểu.

[pause] Hành trình của Jinwoo được đánh dấu bằng những cổng đáng nhớ, mỗi cổng là một bước ngoặt.

[pause] Hầm ngục kép là nơi mọi chuyện bắt đầu: một ngôi đền với những bức tượng giết người theo luật lệ bí ẩn. Sống sót ở đó là điều kiện để nhận Hệ thống.

[pause] Nhiệm vụ đổi nghề là lúc Jinwoo đối đầu một hiệp sĩ bóng tối mạnh mẽ, và sau khi thắng, hiệp sĩ đó trở thành bóng binh đầu tiên của anh.

[pause] Cổng đỏ là nơi cả đội bị mắc kẹt trong một thế giới băng giá, và thời gian bên trong kéo dài hơn bên ngoài rất nhiều.

[pause] Lâu đài quỷ là một hầm ngục đặc biệt nhiều tầng mà Jinwoo leo lên để tìm thứ có thể cứu mẹ mình. Đây là động lực cảm xúc lớn nhất của anh.

[pause] Và arc đảo Jeju là trận chiến quy mô quốc gia, nơi thế giới lần đầu thấy sức mạnh thật sự của người từng được gọi là yếu nhất.
```

### c05 · Chủ nhân bóng tối / Vì sao hạng S cũng phải dè chừng / Thử nghiệm: bạn thức tỉnh ở hạng nào?

Khoảng 139 giây · cảnh s52–s66 · 1801 ký tự

**Gemini**

```text
Khi đủ cấp, Jinwoo được chọn một nghề mới. Anh trở thành Thuật sĩ bóng tối, với năng lực đặc biệt nhất truyện: trỗi dậy.

<short pause> Với năng lực này, Jinwoo có thể lấy bóng của quái vật hay chiến binh đã bị đánh bại, biến chúng thành binh lính trung thành với anh.

<short pause> Đội quân bóng tối lớn dần theo mỗi trận chiến. Có hiệp sĩ, có sát thủ, có cả những sinh vật khổng lồ từng là kẻ thù.

<short pause> Bóng binh không chết theo cách thông thường. Bị tiêu diệt, chúng có thể được triệu hồi lại khi chủ nhân còn đủ ma lực.

<short pause> Ở arc đảo Jeju, Jinwoo đối đầu với đàn kiến khổng lồ, và một trong số đó sau này trở thành binh lính bóng tối mạnh nhất của anh.

<short pause> <laugh> Kaku ghi chú: năng lực này cực kỳ mạnh vì nó cộng dồn. Mỗi trận thắng không chỉ làm anh mạnh hơn, mà còn cho anh thêm binh lính.

<short pause> Có một cảnh làm fan nhớ mãi: khi các thợ săn hạng S bắt đầu nhận ra một người từng hạng E giờ mạnh hơn cả họ.

<short pause> Khi Jinwoo tái đánh giá, thiết bị đo cho thấy anh đã vượt lên hạng S. <short pause> Nhưng thực tế, sức mạnh của anh còn tăng tiếp sau đó.

<short pause> Điều này làm lộ ra lỗ hổng của hệ thống xếp hạng: nó chỉ đo được ma lực tại một thời điểm, không đo được khả năng phát triển.

<short pause> Nói cách khác, hệ thống xếp hạng hợp với một thế giới đứng yên. Còn Jinwoo là thứ duy nhất trong thế giới đó đang chuyển động.

<short pause> Thử tưởng tượng bạn thức tỉnh trong thế giới Solo Leveling. Mỗi hạng sẽ cho bạn một cuộc sống rất khác.

<short pause> Nếu bạn hạng E hoặc D, có lẽ an toàn nhất là làm hậu cần cho hội thợ săn, hoặc chỉ nhận các cổng dễ. Đừng liều.

<short pause> Nếu bạn hạng C hoặc B, bạn có thể sống tốt bằng nghề thợ săn, miễn là chọn đội tốt và biết rút lui khi cổng quá nguy hiểm.

<short pause> Nếu bạn hạng A hoặc S, các hội lớn sẽ tranh nhau mời bạn. <short pause> Nhưng bạn cũng sẽ bị gọi vào những thảm họa lớn nhất.

<short pause> Còn nếu một màn hình xanh xuất hiện trước mắt bạn, thì chúc mừng, bạn là nhân vật chính. <short pause> Nhưng nhớ làm đủ nhiệm vụ hằng ngày nhé.
```

**ElevenLabs**

```text
Khi đủ cấp, Jinwoo được chọn một nghề mới. Anh trở thành Thuật sĩ bóng tối, với năng lực đặc biệt nhất truyện: trỗi dậy.

[pause] Với năng lực này, Jinwoo có thể lấy bóng của quái vật hay chiến binh đã bị đánh bại, biến chúng thành binh lính trung thành với anh.

[pause] Đội quân bóng tối lớn dần theo mỗi trận chiến. Có hiệp sĩ, có sát thủ, có cả những sinh vật khổng lồ từng là kẻ thù.

[pause] Bóng binh không chết theo cách thông thường. Bị tiêu diệt, chúng có thể được triệu hồi lại khi chủ nhân còn đủ ma lực.

[pause] Ở arc đảo Jeju, Jinwoo đối đầu với đàn kiến khổng lồ, và một trong số đó sau này trở thành binh lính bóng tối mạnh nhất của anh.

[pause] [chuckles] Kaku ghi chú: năng lực này cực kỳ mạnh vì nó cộng dồn. Mỗi trận thắng không chỉ làm anh mạnh hơn, mà còn cho anh thêm binh lính.

[pause] Có một cảnh làm fan nhớ mãi: khi các thợ săn hạng S bắt đầu nhận ra một người từng hạng E giờ mạnh hơn cả họ.

[pause] Khi Jinwoo tái đánh giá, thiết bị đo cho thấy anh đã vượt lên hạng S. [pause] Nhưng thực tế, sức mạnh của anh còn tăng tiếp sau đó.

[pause] Điều này làm lộ ra lỗ hổng của hệ thống xếp hạng: nó chỉ đo được ma lực tại một thời điểm, không đo được khả năng phát triển.

[pause] Nói cách khác, hệ thống xếp hạng hợp với một thế giới đứng yên. Còn Jinwoo là thứ duy nhất trong thế giới đó đang chuyển động.

[pause] Thử tưởng tượng bạn thức tỉnh trong thế giới Solo Leveling. Mỗi hạng sẽ cho bạn một cuộc sống rất khác.

[pause] Nếu bạn hạng E hoặc D, có lẽ an toàn nhất là làm hậu cần cho hội thợ săn, hoặc chỉ nhận các cổng dễ. Đừng liều.

[pause] Nếu bạn hạng C hoặc B, bạn có thể sống tốt bằng nghề thợ săn, miễn là chọn đội tốt và biết rút lui khi cổng quá nguy hiểm.

[pause] Nếu bạn hạng A hoặc S, các hội lớn sẽ tranh nhau mời bạn. [pause] Nhưng bạn cũng sẽ bị gọi vào những thảm họa lớn nhất.

[pause] Còn nếu một màn hình xanh xuất hiện trước mắt bạn, thì chúc mừng, bạn là nhân vật chính. [pause] Nhưng nhớ làm đủ nhiệm vụ hằng ngày nhé.
```

### c06 · Những hiểu lầm về hệ thống / Bài học đời thực: nhiệm vụ hằng ngày / Góc nhìn của Kaku: vì sao hệ thống này cuốn hút

Khoảng 147 giây · cảnh s67–s82 · 1917 ký tự

**Gemini**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về thế giới Solo Leveling.

<short pause> Hiểu lầm một: thợ săn nào cũng có Hệ thống như Jinwoo. Không, trong truyện anh là trường hợp duy nhất được biết đến.

<short pause> Hiểu lầm hai: hạng S là giới hạn cao nhất. Trên hạng S còn có thợ săn cấp quốc gia, và sau đó còn những thế lực vượt xa con người.

<short pause> Hiểu lầm ba: cổng hạng thấp thì an toàn. Hầm ngục kép ban đầu được xếp hạng thấp, nhưng suýt giết cả đội.

<short pause> Hiểu lầm bốn: Jinwoo mạnh chỉ nhờ may mắn. Hệ thống cho cơ hội, nhưng anh phải hoàn thành nhiệm vụ mỗi ngày và liều mạng trong từng trận.

<short pause> Có một lý do khác khiến fan yêu Solo Leveling, và nó nằm ngoài màn hình: nhiệm vụ hằng ngày.

<short pause> Rất nhiều người xem đã tự tạo nhiệm vụ hằng ngày của riêng mình: chống đẩy, chạy bộ, đọc sách, học ngoại ngữ, đúng như cách Hệ thống giao cho Jinwoo.

<short pause> Thông điệp ở đây rất đơn giản: những việc nhỏ lặp lại mỗi ngày sẽ cộng dồn thành thay đổi lớn. Lên cấp không đến từ một lần bùng nổ.

<short pause> Tất nhiên ngoài đời không có màn hình xanh báo điểm. <short pause> Nhưng bạn có thể tự ghi lại tiến bộ của mình, và cảm giác lên cấp là có thật.

<short pause> <laugh> Kaku thử làm nhiệm vụ hằng ngày: mỗi ngày đọc một chương sách. Đến giờ, cuốn sổ của Kaku đã dày lên đáng kể.

<short pause> Vì sao hệ thống của Solo Leveling lại cuốn hút hàng triệu người, dù ý tưởng cổng và xếp hạng không quá mới?

<short pause> Lý do một: nó rất dễ hiểu. Chữ cái từ E đến S ai nhìn cũng biết ngay ai mạnh, ai yếu. Người xem không cần học luật phức tạp.

<short pause> Lý do hai: nó biến cảm giác chơi game thành truyện. Lên cấp, tăng chỉ số, nhận phần thưởng đều tạo cảm giác thỏa mãn liên tục.

<short pause> Lý do ba: nó có kẻ yếu vươn lên. Một thế giới cứng nhắc làm cho sự vươn lên của một người trở nên đặc biệt.

<short pause> Nhưng cũng có điểm yếu: khi nhân vật chính mạnh vượt xa mọi người, các trận đấu dễ mất căng thẳng. Truyện bù lại bằng những kẻ thù ở tầm cao hơn.

<short pause> So với Nen, nơi luật và giao ước quyết định trận đấu, Solo Leveling đơn giản hơn nhiều. <short pause> Nhưng sự đơn giản đó chính là sức mạnh của nó.
```

**ElevenLabs**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về thế giới Solo Leveling.

[pause] Hiểu lầm một: thợ săn nào cũng có Hệ thống như Jinwoo. Không, trong truyện anh là trường hợp duy nhất được biết đến.

[pause] Hiểu lầm hai: hạng S là giới hạn cao nhất. Trên hạng S còn có thợ săn cấp quốc gia, và sau đó còn những thế lực vượt xa con người.

[pause] Hiểu lầm ba: cổng hạng thấp thì an toàn. Hầm ngục kép ban đầu được xếp hạng thấp, nhưng suýt giết cả đội.

[pause] Hiểu lầm bốn: Jinwoo mạnh chỉ nhờ may mắn. Hệ thống cho cơ hội, nhưng anh phải hoàn thành nhiệm vụ mỗi ngày và liều mạng trong từng trận.

[pause] Có một lý do khác khiến fan yêu Solo Leveling, và nó nằm ngoài màn hình: nhiệm vụ hằng ngày.

[pause] Rất nhiều người xem đã tự tạo nhiệm vụ hằng ngày của riêng mình: chống đẩy, chạy bộ, đọc sách, học ngoại ngữ, đúng như cách Hệ thống giao cho Jinwoo.

[pause] Thông điệp ở đây rất đơn giản: những việc nhỏ lặp lại mỗi ngày sẽ cộng dồn thành thay đổi lớn. Lên cấp không đến từ một lần bùng nổ.

[pause] Tất nhiên ngoài đời không có màn hình xanh báo điểm. [pause] Nhưng bạn có thể tự ghi lại tiến bộ của mình, và cảm giác lên cấp là có thật.

[pause] [chuckles] Kaku thử làm nhiệm vụ hằng ngày: mỗi ngày đọc một chương sách. Đến giờ, cuốn sổ của Kaku đã dày lên đáng kể.

[pause] [curious] Vì sao hệ thống của Solo Leveling lại cuốn hút hàng triệu người, dù ý tưởng cổng và xếp hạng không quá mới?

[pause] Lý do một: nó rất dễ hiểu. Chữ cái từ E đến S ai nhìn cũng biết ngay ai mạnh, ai yếu. Người xem không cần học luật phức tạp.

[pause] Lý do hai: nó biến cảm giác chơi game thành truyện. Lên cấp, tăng chỉ số, nhận phần thưởng đều tạo cảm giác thỏa mãn liên tục.

[pause] Lý do ba: nó có kẻ yếu vươn lên. Một thế giới cứng nhắc làm cho sự vươn lên của một người trở nên đặc biệt.

[pause] Nhưng cũng có điểm yếu: khi nhân vật chính mạnh vượt xa mọi người, các trận đấu dễ mất căng thẳng. Truyện bù lại bằng những kẻ thù ở tầm cao hơn.

[pause] So với Nen, nơi luật và giao ước quyết định trận đấu, Solo Leveling đơn giản hơn nhiều. [pause] Nhưng sự đơn giản đó chính là sức mạnh của nó.
```

### c07 · Vì sao cổng xuất hiện? / Nếu Solo Leveling có phần tiếp theo trong đời bạn / Tóm tắt

Khoảng 145 giây · cảnh s83–s98 · 1881 ký tự

**Gemini**

```text
Một câu hỏi lớn mà người xem mới hay đặt ra: vì sao cổng lại xuất hiện? Ai hay cái gì đứng sau chúng?

<short pause> Trong phần đầu câu chuyện, không ai biết. Con người chỉ biết cách sống chung với cổng: đo, phân loại, dọn dẹp, và kiếm tiền từ nó.

<short pause> Dần dần, truyện hé lộ rằng cổng và Hệ thống có liên quan tới những thế lực lớn hơn loài người rất nhiều. Mình sẽ không nói sâu để tránh spoiler phần sau.

<short pause> Điều đáng chú ý là cách truyện dẫn dắt: bắt đầu từ góc nhìn của một thợ săn yếu nhất, rồi mở rộng dần ra những bí ẩn của cả thế giới.

<short pause> Nhờ vậy, mỗi lần Jinwoo mạnh lên, người xem cũng được thấy thêm một phần sự thật. Sức mạnh và bí ẩn lớn lên cùng nhau.

<short pause> <laugh> Kaku nhắc: nếu bạn muốn một video riêng về bí ẩn của cổng và những thế lực đứng sau, có spoiler đầy đủ, hãy bình luận để mình biết nhé.

<short pause> Trước khi tổng kết, Kaku muốn bàn một câu hỏi nhỏ: vì sao câu chuyện về một người lên cấp lại khiến nhiều người muốn thay đổi bản thân đến vậy?

<short pause> Có lẽ vì Solo Leveling nói điều mà ai cũng muốn nghe: vị trí xuất phát không quyết định vị trí kết thúc.

<short pause> Trong truyện, người khác bị khóa ở hạng của mình. Ngoài đời, may mắn là chúng ta không bị khóa như vậy. Ai cũng có thể lên cấp, chỉ là chậm hơn và không có màn hình báo điểm.

<short pause> Và đó là lý do Kaku nghĩ nhiệm vụ hằng ngày là bài học hay nhất của bộ truyện, hay hơn cả những trận đấu hoành tráng.

<short pause> Tóm lại: cổng mở ra hầm ngục, không dọn kịp thì quái vật tràn ra. Cổng và thợ săn đều được xếp hạng từ E đến S.

<short pause> Hạng thợ săn gần như cố định suốt đời, và nó quyết định tiền bạc, địa vị và sự an toàn của họ.

<short pause> Jinwoo phá vỡ luật đó nhờ Hệ thống, rồi trở thành chủ nhân của một đội quân bóng tối ngày càng lớn.

<short pause> Câu hỏi cho bạn: nếu thức tỉnh, bạn muốn đóng vai trò nào trong đội: đỡ đòn, pháp sư, hồi phục hay sát thủ? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã sự tiến hóa của Sharingan trong Naruto.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Một câu hỏi lớn mà người xem mới hay đặt ra: vì sao cổng lại xuất hiện? Ai hay cái gì đứng sau chúng?

[pause] Trong phần đầu câu chuyện, không ai biết. Con người chỉ biết cách sống chung với cổng: đo, phân loại, dọn dẹp, và kiếm tiền từ nó.

[pause] Dần dần, truyện hé lộ rằng cổng và Hệ thống có liên quan tới những thế lực lớn hơn loài người rất nhiều. Mình sẽ không nói sâu để tránh spoiler phần sau.

[pause] Điều đáng chú ý là cách truyện dẫn dắt: bắt đầu từ góc nhìn của một thợ săn yếu nhất, rồi mở rộng dần ra những bí ẩn của cả thế giới.

[pause] Nhờ vậy, mỗi lần Jinwoo mạnh lên, người xem cũng được thấy thêm một phần sự thật. Sức mạnh và bí ẩn lớn lên cùng nhau.

[pause] [chuckles] Kaku nhắc: nếu bạn muốn một video riêng về bí ẩn của cổng và những thế lực đứng sau, có spoiler đầy đủ, hãy bình luận để mình biết nhé.

[pause] Trước khi tổng kết, Kaku muốn bàn một câu hỏi nhỏ: vì sao câu chuyện về một người lên cấp lại khiến nhiều người muốn thay đổi bản thân đến vậy?

[pause] Có lẽ vì Solo Leveling nói điều mà ai cũng muốn nghe: vị trí xuất phát không quyết định vị trí kết thúc.

[pause] Trong truyện, người khác bị khóa ở hạng của mình. Ngoài đời, may mắn là chúng ta không bị khóa như vậy. Ai cũng có thể lên cấp, chỉ là chậm hơn và không có màn hình báo điểm.

[pause] Và đó là lý do Kaku nghĩ nhiệm vụ hằng ngày là bài học hay nhất của bộ truyện, hay hơn cả những trận đấu hoành tráng.

[pause] Tóm lại: cổng mở ra hầm ngục, không dọn kịp thì quái vật tràn ra. Cổng và thợ săn đều được xếp hạng từ E đến S.

[pause] Hạng thợ săn gần như cố định suốt đời, và nó quyết định tiền bạc, địa vị và sự an toàn của họ.

[pause] Jinwoo phá vỡ luật đó nhờ Hệ thống, rồi trở thành chủ nhân của một đội quân bóng tối ngày càng lớn.

[pause] Câu hỏi cho bạn: nếu thức tỉnh, bạn muốn đóng vai trò nào trong đội: đỡ đòn, pháp sư, hồi phục hay sát thủ? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã sự tiến hóa của Sharingan trong Naruto.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
