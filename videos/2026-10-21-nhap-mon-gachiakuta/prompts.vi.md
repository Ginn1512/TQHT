# Bộ prompt · Gachiakuta: Nhập môn — thế giới nơi rác thành vũ khí

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 9 đoạn đọc, khoảng 15.3 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (82 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Video này gần như không có spoiler. Kaku chỉ nói tới khoảng tập ba, tập bốn của anime mùa một. Nếu bạn chưa x…

```text
Wide 16:9 landscape cinematic frame. a towering mountain of discarded objects under a grey sky, a closed notebook resting on a broken chair at its base, wide establishing shot, muted light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy nhìn quanh phòng bạn. Có món đồ nào bạn giữ rất lâu, dù nó đã cũ, đã hỏng? Một chiếc áo của người thân, m…

```text
Wide 16:9 landscape cinematic frame. a cozy bedroom shelf with an old worn plush toy, a faded jacket and a scratched pen, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trong Gachiakuta, những món đồ như vậy có linh hồn. Và nếu bạn đủ trân trọng chúng, chúng có thể trở thành vũ…

```text
Wide 16:9 landscape cinematic frame. an old umbrella glowing faintly with a soft light in the hands of a young fighter, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Gachiakuta là manga của tác giả Urana Kei, và anime do studio Bones sản xuất, ra mắt năm 2025. Nó được nhiều…

```text
Wide 16:9 landscape cinematic frame. a stylized manga volume with graffiti-style lettering next to a TV screen glowing with bold colors, close-up, vibrant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Tên truyện ghép từ hai từ tiếng Nhật: gachi, nghĩa là thật sự, nghiêm túc, và akuta, nghĩa là rác, đồ bỏ đi.…

```text
Wide 16:9 landscape cinematic frame. two Japanese-style brush stroke characters drawn on paper side by side with small icons of a serious face and a crumpled paper ball, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở cửa nhập môn cho Gachiakuta: thế giới, nhân vật chính, cách sức m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at a creaky gate made of scrap metal, holding it open and gesturing welcomingly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Thế giới: tầng trên và hố rác

Lời: Thế giới của Gachiakuta được chia làm hai tầng. Ở trên là một thành phố giàu có, nơi người ta vứt bỏ mọi thứ…

```text
Wide 16:9 landscape cinematic frame. a gleaming wealthy city on a floating plateau with clean streets and elegant buildings, residents tossing items carelessly over a railing, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Mọi thứ bị vứt đi đều rơi xuống một vực sâu khổng lồ gọi là Hố. Không ai ở trên biết dưới đó có gì, và không…

```text
Wide 16:9 landscape cinematic frame. an enormous chasm at the edge of a city with trash falling into dark clouds below, dramatic high-angle shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Người dân tầng trên sống sạch sẽ, tiện nghi, và chưa từng tự hỏi rác của mình đi đâu. Đối với họ, vứt xuống H…

```text
Wide 16:9 landscape cinematic frame. a well-dressed family casually dropping a bag over a railing without looking, the chasm below hidden in clouds, medium shot, bright indifferent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nhưng Hố không chỉ nhận rác. Nó còn là hình phạt. Tội phạm bị ném xuống Hố, và người ta tin rằng không ai rơi…

```text
Wide 16:9 landscape cinematic frame. a silhouette being pushed toward the edge of the chasm by guards, a crowd watching from behind a fence, wide shot, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Những người ở khu ổ chuột mang một dấu hiệu trên người, cho biết họ là hậu duệ của tội phạm. Họ chưa làm gì s…

```text
Wide 16:9 landscape cinematic frame. a young person pulling a sleeve down to hide a small mark on their arm as passersby glance suspiciously, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Kaku để ý: đây là một chủ đề lặp lại trong nhiều bộ anime Kaku làm gần đây. Tougen Anki với dòng máu quỷ, Mas…

```text
Wide 16:9 landscape cinematic frame. three small book spines side by side, each with an icon: a horn, a cream puff, and a crumpled paper ball, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Ở rìa thành phố có một khu ổ chuột, nơi sống những người mang dấu vết của tổ tiên phạm tội. Họ bị kỳ thị chỉ…

```text
Wide 16:9 landscape cinematic frame. a cramped slum district built from scrap metal at the edge of the floating city, children playing in narrow alleys, wide shot, warm dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ngay từ thiết kế thế giới, Gachiakuta đã nói về một câu hỏi rất thời sự: cái gì bị coi là rác, và…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up an old shoe and looking at it thoughtfully, as if deciding whether it is trash. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Nhân vật chính: Rudo

Lời: Nhân vật chính là Rudo, một cậu thiếu niên sống ở khu ổ chuột. Cậu có một thói quen mà mọi người chê cười: nh…

```text
Wide 16:9 landscape cinematic frame. a rebellious teenage boy with a determined face digging through a pile of discarded objects, holding up a broken gadget with a grin, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Nhưng Rudo vẫn nhặt, vẫn sửa. Căn nhà nhỏ của hai cha con đầy những món đồ được cứu khỏi thùng rác, mỗi món đ…

```text
Wide 16:9 landscape cinematic frame. a small cozy shack filled with repaired lamps, clocks and gadgets, all glowing softly, wide shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Cậu được nuôi bởi một người cha nuôi tên Regto, người nhiều lần nhắc cậu đừng nhặt rác, vì ở thành phố này, n…

```text
Wide 16:9 landscape cinematic frame. a gentle older man with a scarred face standing in a small doorway, watching a boy carry scrap home, medium shot, soft evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Rudo luôn đeo một đôi găng tay, món đồ cậu không bao giờ rời. Đôi găng này sẽ trở thành chìa khóa của cả câu…

```text
Wide 16:9 landscape cinematic frame. a pair of worn fingerless gloves resting on a wooden table beside a small toolkit, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Không ai tin Rudo. Chỉ vì cậu sống ở khu ổ chuột, chỉ vì cậu mang dấu hiệu của tổ tiên tội phạm. Bằng chứng k…

```text
Wide 16:9 landscape cinematic frame. a crowd of accusing faces surrounding a boy in a town square, fingers pointing, dramatic low-angle shot, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Rồi một ngày, Regto bị một kẻ lạ mặt sát hại. Rudo bị vu oan là hung thủ, bị bắt, và bị ném xuống Hố.

```text
Wide 16:9 landscape cinematic frame. a boy falling into a dark cloud-filled chasm, reaching upward toward a shrinking circle of light, dramatic low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kaku phải nói: tập một của Gachiakuta là một trong những tập mở đầu mạnh nhất Kaku từng xem gần đây. Nếu bạn…

```text
Wide 16:9 landscape cinematic frame. a TV screen glowing in a dark room with a single remote on the couch, a sticky note reading episode one, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Đó là tập một. Và từ đây, câu chuyện thật sự bắt đầu: một cậu bé bị thế giới vứt bỏ, rơi xuống nơi chứa đựng…

```text
Wide 16:9 landscape cinematic frame. a boy lying on top of a vast landscape of trash at the bottom of the chasm, looking up at a distant sky, wide shot, muted grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Dưới đáy Hố

Lời: Nơi đây ngập trong khói độc và mùi rác thối. Người dưới Hố phải đeo mặt nạ để thở, và học cách sống giữa nhữn…

```text
Wide 16:9 landscape cinematic frame. people wearing improvised breathing masks walking through a hazy landscape of trash, wide shot, muted green haze. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Dưới đáy Hố không phải là chết chóc tuyệt đối như người trên cao nghĩ. Có người sống ở đó, có cả những thị tr…

```text
Wide 16:9 landscape cinematic frame. a surprising settlement built from scrap metal and old vehicles on a landscape of trash, smoke rising from chimneys, wide shot, warm hazy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nhưng rác ở đây cũng sinh ra quái vật: những sinh vật khổng lồ được tạo thành từ rác thải, gọi là Quái vật rá…

```text
Wide 16:9 landscape cinematic frame. a towering monster formed from piles of discarded junk, glowing eyes in its scrap body, looming over a small figure, low-angle shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Và có một nhóm người chuyên chiến đấu với chúng, gọi là Cleaners, những người dọn dẹp. Họ không dùng súng hay…

```text
Wide 16:9 landscape cinematic frame. a group of stylish fighters with graffiti-painted jackets standing on a trash hill, each holding a different everyday object, wide shot, dramatic backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Enjin có vẻ lười biếng và hay đùa, nhưng khi chiến đấu thì rất đáng tin. Anh là kiểu người thầy mà shounen nà…

```text
Wide 16:9 landscape cinematic frame. a laid-back man lounging on a trash hill with an umbrella over his shoulder, grinning at a frustrated boy, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Rudo gặp một người đàn ông tên Enjin, một Cleaner dùng chiếc ô làm vũ khí. Anh cứu Rudo khỏi quái vật, và đưa…

```text
Wide 16:9 landscape cinematic frame. a tall laid-back man holding an open umbrella that deflects a monster's strike, a boy on the ground behind him, dynamic medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Sức mạnh: Jinki và Giver

Lời: Giờ tới hệ thống sức mạnh. Gachiakuta có một khái niệm gọi là Jinki, tạm dịch là bảo khí: những món đồ được n…

```text
Wide 16:9 landscape cinematic frame. an old everyday object glowing with soft threads of light connecting it to a person's heart, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Năng lượng trong Jinki không phải phép thuật từ trên trời rơi xuống. Nó đến từ chính con người: từ suy nghĩ,…

```text
Wide 16:9 landscape cinematic frame. a translucent memory of a smiling person faintly visible inside a glowing old object, symbolic close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Người có thể đánh thức sức mạnh của những món đồ đó gọi là Giver. Không phải ai cũng làm được. Giver là người…

```text
Wide 16:9 landscape cinematic frame. a young person holding an old tool with both hands as it begins to glow brighter, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Mỗi Jinki là duy nhất, vì mỗi mối gắn bó là duy nhất. Chiếc ô của Enjin, cây gậy của một Cleaner khác, mỗi mó…

```text
Wide 16:9 landscape cinematic frame. a row of different glowing objects laid out on a workbench: an umbrella, a stick, a pair of gloves, a small toy, each with a different colored glow, still life. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nghĩa là trong một thế giới đầy rác, Rudo có một kho vũ khí vô tận. Chỉ cần cậu chạm vào và thấy được giá trị…

```text
Wide 16:9 landscape cinematic frame. a boy standing in the middle of an endless trash landscape, faint glowing outlines appearing around nearby objects as he looks at them, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và Rudo phát hiện ra mình là một Giver. Đôi găng tay của cậu là Jinki. Nhưng điều đặc biệt là: với đôi găng,…

```text
Wide 16:9 landscape cinematic frame. a boy wearing glowing gloves touching a pile of junk that rises and reshapes into a makeshift weapon, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích chi tiết này: người từng bị chê cười vì nhặt rác lại có năng lực biến rác thành sức mạnh. Tác…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a broken teacup that glows faintly, looking delighted. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Luật của Jinki

Lời: Trước khi đi vào luật, Kaku nhắc lại một điều: những gì Kaku nói sau đây chỉ tới khoảng tập bốn, nên bạn yên…

```text
Wide 16:9 landscape cinematic frame. a notebook page with a small padlock doodle beside a list of three numbered rules, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Luật một: sức mạnh của Jinki đến từ sự gắn bó. Một món đồ mới mua hôm qua sẽ không có sức mạnh. Một món đồ đư…

```text
Wide 16:9 landscape cinematic frame. two objects side by side: a shiny new pen in its packaging and an old worn pen with tape repairs glowing softly, comparison still life, warm light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Luật hai: Jinki phản ánh người dùng. Năng lực của nó thường liên quan tới ý nghĩa món đồ đó với chủ nhân.

```text
Wide 16:9 landscape cinematic frame. a small handwritten note tied to an old object, the note's words glowing faintly, extreme close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kaku rất thích hình ảnh các Cleaner sửa Jinki sau mỗi trận. Giống như một người lính lau súng, nhưng ở đây họ…

```text
Wide 16:9 landscape cinematic frame. several fighters sitting together at dusk mending their various objects with glue, thread and tape, wide shot, warm quiet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Luật ba: nếu Jinki bị phá hủy, Giver mất vũ khí, và phải xây dựng lại mối gắn bó từ đầu. Vì vậy các Cleaner c…

```text
Wide 16:9 landscape cinematic frame. a fighter carefully repairing a cracked umbrella handle with tools by lamplight, close-up, warm quiet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và nó khiến hệ thống sức mạnh này rất gần với người xem. Ai trong chúng ta cũng có một món đồ như vậy. Ai tro…

```text
Wide 16:9 landscape cinematic frame. a diverse group of people each holding a small cherished object that glows faintly, arranged in a warm circle, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Kaku ghi chú: đây là một hệ thống sức mạnh hiếm hoi mà cách mạnh lên không phải là luyện tập hay chiến đấu, m…

```text
Wide 16:9 landscape cinematic frame. a timeline drawn on parchment showing an object gaining a brighter glow over many years of care, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Gốc văn hóa: đồ vật có linh hồn

Lời: Ý tưởng đồ vật có linh hồn không phải do Gachiakuta nghĩ ra. Nó có gốc rất sâu trong văn hóa Nhật Bản.

```text
Wide 16:9 landscape cinematic frame. an old Japanese picture scroll unrolled on a low table showing whimsical drawings of household objects with faces, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Trong dân gian Nhật có khái niệm tsukumogami: những đồ vật dùng lâu tới một trăm năm sẽ có linh hồn. Một chiế…

```text
Wide 16:9 landscape cinematic frame. a moonlit room where an old paper umbrella, a lantern and a pair of wooden sandals come to life with playful expressions, whimsical wide shot, soft blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Theo truyền thuyết, những đồ vật bị vứt bỏ một cách vô ơn có thể trở nên giận dữ và báo thù. Những câu chuyện…

```text
Wide 16:9 landscape cinematic frame. a pile of discarded old objects in an alley at night with faint angry glowing eyes, eerie but whimsical, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nghe có quen không? Quái vật rác trong Gachiakuta được sinh ra từ đống đồ bị vứt đi. Còn Jinki là đồ vật được…

```text
Wide 16:9 landscape cinematic frame. a split illustration: an angry junk monster on one side and a softly glowing cherished object on the other, symmetrical composition, parchment and neon. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Người Nhật còn có một từ rất đặc biệt: mottainai, nghĩa là thật đáng tiếc khi một thứ bị lãng phí mà chưa đượ…

```text
Wide 16:9 landscape cinematic frame. a grandmother carefully folding a used gift wrapping paper to reuse it, close-up, warm kitchen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Và có cả nghệ thuật kintsugi: hàn gắn đồ gốm bị vỡ bằng sơn mài trộn bột vàng. Vết nứt không bị giấu đi mà đư…

```text
Wide 16:9 landscape cinematic frame. a ceramic bowl repaired with glowing golden seams along its cracks, resting on a dark wooden table, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là chìa khóa để hiểu Rudo. Cậu không nhặt rác vì nghèo. Cậu nhặt vì cậu thấy giá trị ở nơi ngườ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a golden-repaired teacup and nodding solemnly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Nếu bạn là một Giver

Lời: Giờ đến một trò chơi nhỏ. Nếu bạn là một Giver, món đồ nào của bạn sẽ trở thành Jinki?

```text
Wide 16:9 landscape cinematic frame. a desk drawer pulled open revealing a collection of personal keepsakes: a keychain, an old watch, a worn notebook, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Hãy nghĩ tới món đồ bạn giữ lâu nhất, sửa nhiều nhất, và buồn nhất nếu mất nó. Đó là Jinki của bạn.

```text
Wide 16:9 landscape cinematic frame. a hand holding a small repaired keychain with tape around it, extreme close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Rồi thử đoán năng lực của nó. Một chiếc đồng hồ cũ của ông có thể làm chậm thời gian. Một quyển sổ ghi chép c…

```text
Wide 16:9 landscape cinematic frame. three small panels: an old watch with glowing slowed clock hands, a notebook with glowing annotations, a bicycle with light trails, parchment storyboard. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Jinki của Kaku chắc chắn là cuốn sổ này. Năng lực: mở ra là kẻ thù phải nghe giảng mười lăm phút. Rất đáng sợ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding its glowing notebook up like a shield while a monster yawns in front of it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Viết tên Jinki và năng lực của bạn vào bình luận nhé. Kaku sẽ chọn những Jinki sáng tạo nhất để vẽ vào một vi…

```text
Wide 16:9 landscape cinematic frame. a comment box drawn on parchment with small doodles of glowing everyday objects, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Vì sao nên xem: phong cách

Lời: Những nét graffiti xuất hiện cả trên quần áo, trên tường, trên vũ khí. Nó cho thế giới dưới Hố một cá tính đư…

```text
Wide 16:9 landscape cinematic frame. a split composition: sterile white city walls above, vibrant graffiti-covered scrap walls below, wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Lý do đầu tiên để xem Gachiakuta: phong cách hình ảnh. Bộ truyện có những hình vẽ graffiti mạnh mẽ, và anime…

```text
Wide 16:9 landscape cinematic frame. a large colorful graffiti mural on a scrap metal wall with bold abstract shapes, wide shot, vibrant urban light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Chính tác giả Urana Kei từng là trợ lý của tác giả Fire Force, và bạn sẽ thấy chất năng lượng, chuyển động rấ…

```text
Wide 16:9 landscape cinematic frame. a manga page layout with dynamic diagonal panels and speed lines sketched on a drawing desk, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Nhạc nền của anime cũng rất đáng chú ý, mạnh mẽ, có chất hip hop đường phố, hợp với thế giới graffiti. Kaku k…

```text
Wide 16:9 landscape cinematic frame. a pair of headphones resting on a spray paint can beside a small speaker, close-up, vibrant urban light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Studio Bones, nơi từng làm My Hero Academia, mang tới những cảnh hành động rất mãn nhãn. Kaku không dùng cảnh…

```text
Wide 16:9 landscape cinematic frame. an animation desk with layered sketches of an action pose and a lightbox glowing underneath, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Vì sao nên xem: câu chuyện

Lời: Câu hỏi lớn của bộ truyện là: nếu bạn bị cả thế giới vứt bỏ, bạn sẽ đập phá nó, hay tìm cách làm nó tốt hơn?…

```text
Wide 16:9 landscape cinematic frame. a boy standing at a crossroads in the trash landscape, one path leading toward the city above, one toward a group of people below, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Lý do thứ hai: câu chuyện về bất công. Rudo bị vu oan, bị vứt bỏ, và muốn trả thù những kẻ ở tầng trên. Nhưng…

```text
Wide 16:9 landscape cinematic frame. a boy standing at the bottom of the chasm looking up at the distant city lights with clenched fists, wide shot, dramatic contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Kaku thích cách bộ truyện không vẽ tầng dưới là người tốt hết, tầng trên là người xấu hết. Dưới Hố cũng có kẻ…

```text
Wide 16:9 landscape cinematic frame. a split scene of a kind face in the clean city and a greedy face in the trash landscape, symmetrical composition, muted grey light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Lý do thứ ba: những nhân vật phụ có cá tính. Các Cleaner mỗi người một vẻ, và mỗi Jinki kể một câu chuyện riê…

```text
Wide 16:9 landscape cinematic frame. a group of eccentric fighters sitting around a campfire on a trash hill, laughing and repairing their tools, wide shot, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Theo nhiều báo cáo, con người thải ra hàng tỉ tấn rác mỗi năm. Gachiakuta không giảng đạo lý, nhưng khiến bạn…

```text
Wide 16:9 landscape cinematic frame. an overflowing city trash bin at night with a single discarded toy on top, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Và lý do thứ tư, Kaku thích nhất: thông điệp về đồ vật. Trong thời đại ai cũng vứt đi rất dễ dàng, một bộ ani…

```text
Wide 16:9 landscape cinematic frame. a child handing an old repaired toy to a younger child in a quiet street, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Nếu bạn thích bộ này, bạn sẽ thích Gachiakuta

Lời: Nếu bạn còn phân vân, đây là cách Kaku gợi ý nhanh. Nếu bạn thích Fire Force, bạn sẽ thích nhịp hành động và…

```text
Wide 16:9 landscape cinematic frame. two manga volumes side by side on a shelf, one with flame motifs and one with graffiti motifs, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Nếu bạn thích Dr. Stone, bạn sẽ thích cảm giác biến những thứ tưởng như vô dụng thành công cụ hữu ích.

```text
Wide 16:9 landscape cinematic frame. a makeshift workshop where junk parts are assembled into a working machine, close-up, warm inventive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Nếu bạn thích Chainsaw Man, bạn sẽ thích thế giới u ám, bẩn thỉu nhưng đầy cá tính của tầng dưới.

```text
Wide 16:9 landscape cinematic frame. a gritty alley at night with flickering signs and graffiti, a lone figure walking through, wide shot, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Và nếu bạn chưa thích bộ nào kể trên, Gachiakuta vẫn là một cửa vào dễ chịu cho thể loại shounen hiện đại: nh…

```text
Wide 16:9 landscape cinematic frame. an open door made of scrap metal leading into a colorful graffiti world, a curious newcomer stepping through, wide shot, inviting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nói nhỏ: Kaku đã giới thiệu bộ này cho một người bạn chỉ xem anime lãng mạn. Người đó xem hết mùa một tr…

```text
Wide 16:9 landscape cinematic frame. the owl mascot whispering behind its wing with a small heart and a trash bag icon floating nearby, playful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Lộ trình xem cho người mới

Lời: Nếu bạn thích đọc hơn, manga Gachiakuta đăng trên tạp chí Shonen Magazine từ năm 2022, và có rất nhiều trang…

```text
Wide 16:9 landscape cinematic frame. a manga magazine lying open on a café table with a bold graffiti-style splash page, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu bạn quyết định xem, đây là lộ trình Kaku gợi ý. Tập một tới tập ba: làm quen thế giới và lý do Rudo rơi x…

```text
Wide 16:9 landscape cinematic frame. a simple roadmap drawn on parchment with three early stops marked by small icons: a city, a fall, a trash landscape, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Tập bốn tới tập tám: Rudo gia nhập Cleaners và học về Jinki. Đây là lúc hệ thống sức mạnh được giải thích rõ…

```text
Wide 16:9 landscape cinematic frame. the roadmap's middle section with an umbrella icon and a pair of glove icons, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Sau đó: những nhiệm vụ lớn hơn và những bí mật về Hố. Kaku sẽ không nói thêm.

```text
Wide 16:9 landscape cinematic frame. the roadmap fading into fog with a question mark at the end, parchment close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Mẹo nhỏ của Kaku: xem xong mỗi tập, hãy để ý xem Jinki của từng nhân vật nói gì về quá khứ của họ. Đó là cách…

```text
Wide 16:9 landscape cinematic frame. a notebook page with small doodles of different objects and short notes beside each, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn xem cùng bạn bè, hãy thử trò này: mỗi người đoán năng lực của một Jinki trước khi nó được tiết lộ. Ai…

```text
Wide 16:9 landscape cinematic frame. a group of friends on a couch pointing at a TV and laughing, snack bowls on the table, medium shot, cozy evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Mùa một có khoảng hai mươi bốn tập. Nếu bạn xem mỗi tối hai tập, bạn sẽ kịp xem hết trước khi mùa hai ra mắt.

```text
Wide 16:9 landscape cinematic frame. a calendar with small checkmarks on each evening and a TV icon, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Kết

Lời: Tóm lại trong một câu: Gachiakuta là shounen hành động có graffiti, có hệ thống sức mạnh dễ hiểu, và có một t…

```text
Wide 16:9 landscape cinematic frame. a single summary card pinned to a corkboard with three small icons: a spray can, a glowing glove, a heart, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và lần tới bạn định vứt một món đồ cũ, hãy dừng lại một giây và nghĩ: nó đã ở bên bạn bao lâu rồi?

```text
Wide 16:9 landscape cinematic frame. a hand hesitating over a trash bin while holding an old worn keychain, close-up, soft reflective light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Gachiakuta là câu chuyện về một cậu bé bị coi là rác, rơi xuống nơi chứa mọi thứ bị coi là rác, và phát hiện…

```text
Wide 16:9 landscape cinematic frame. a boy standing on a trash hill at dawn holding up a glowing pair of gloves, the chasm walls lit by the rising sun, wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo, Kaku đặt ba bộ du hành thời gian lên cùng một bàn cân: Tokyo Revengers, Steins;Gate và Re:Ze…

```text
Wide 16:9 landscape cinematic frame. three different clocks placed on a round table under a spotlight, each with a different style, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video nhập môn này giúp bạn quyết định xem Gachiakuta, hãy đăng ký kênh để Kaku mở thêm nhiều cánh cửa nữ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing the scrap metal gate gently and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 74 giây · cảnh s01–s06 · 958 ký tự

**Gemini**

```text
Video này gần như không có spoiler. Kaku chỉ nói tới khoảng tập ba, tập bốn của anime mùa một. Nếu bạn chưa xem Gachiakuta, đây là mười lăm phút bạn cần.

<short pause> Hãy nhìn quanh phòng bạn. Có món đồ nào bạn giữ rất lâu, dù nó đã cũ, đã hỏng? Một chiếc áo của người thân, một cây bút từ hồi đi học, một món quà nhỏ?

<short pause> Trong Gachiakuta, những món đồ như vậy có linh hồn. Và nếu bạn đủ trân trọng chúng, chúng có thể trở thành vũ khí.

<short pause> Gachiakuta là manga của tác giả Urana Kei, và anime do studio Bones sản xuất, ra mắt năm 2025. Nó được nhiều người gọi là một trong những bộ shounen mới nổi bật nhất năm đó, và mùa hai đã được công bố.

<short pause> Tên truyện ghép từ hai từ tiếng Nhật: gachi, nghĩa là thật sự, nghiêm túc, và akuta, nghĩa là rác, đồ bỏ đi. Có thể hiểu là rác thật sự, hay rác nghiêm túc.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở cửa nhập môn cho Gachiakuta: thế giới, nhân vật chính, cách sức mạnh vận hành, và vì sao nên xem. Cuối video là lộ trình xem cho người mới.
```

**ElevenLabs**

```text
Video này gần như không có spoiler. Kaku chỉ nói tới khoảng tập ba, tập bốn của anime mùa một. Nếu bạn chưa xem Gachiakuta, đây là mười lăm phút bạn cần.

[pause] Hãy nhìn quanh phòng bạn. [curious] Có món đồ nào bạn giữ rất lâu, dù nó đã cũ, đã hỏng? Một chiếc áo của người thân, một cây bút từ hồi đi học, một món quà nhỏ?

[pause] Trong Gachiakuta, những món đồ như vậy có linh hồn. Và nếu bạn đủ trân trọng chúng, chúng có thể trở thành vũ khí.

[pause] Gachiakuta là manga của tác giả Urana Kei, và anime do studio Bones sản xuất, ra mắt năm 2025. Nó được nhiều người gọi là một trong những bộ shounen mới nổi bật nhất năm đó, và mùa hai đã được công bố.

[pause] Tên truyện ghép từ hai từ tiếng Nhật: gachi, nghĩa là thật sự, nghiêm túc, và akuta, nghĩa là rác, đồ bỏ đi. Có thể hiểu là rác thật sự, hay rác nghiêm túc.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở cửa nhập môn cho Gachiakuta: thế giới, nhân vật chính, cách sức mạnh vận hành, và vì sao nên xem. Cuối video là lộ trình xem cho người mới.
```

### c02 · Thế giới: tầng trên và hố rác

Khoảng 88 giây · cảnh s07–s14 · 1147 ký tự

**Gemini**

```text
Thế giới của Gachiakuta được chia làm hai tầng. Ở trên là một thành phố giàu có, nơi người ta vứt bỏ mọi thứ mà không cần suy nghĩ.

<short pause> Mọi thứ bị vứt đi đều rơi xuống một vực sâu khổng lồ gọi là Hố. Không ai ở trên biết dưới đó có gì, và không ai quan tâm.

<short pause> Người dân tầng trên sống sạch sẽ, tiện nghi, và chưa từng tự hỏi rác của mình đi đâu. Đối với họ, vứt xuống Hố là biến mất vĩnh viễn.

<short pause> Nhưng Hố không chỉ nhận rác. Nó còn là hình phạt. Tội phạm bị ném xuống Hố, và người ta tin rằng không ai rơi xuống mà còn sống trở về.

<short pause> Những người ở khu ổ chuột mang một dấu hiệu trên người, cho biết họ là hậu duệ của tội phạm. Họ chưa làm gì sai, nhưng bị đối xử như đã có tội từ lúc sinh ra.

<short pause> Kaku để ý: đây là một chủ đề lặp lại trong nhiều bộ anime Kaku làm gần đây. Tougen Anki với dòng máu quỷ, Mashle với người không có phép. Có vẻ những năm gần đây anime rất quan tâm tới những người bị xã hội gạt ra lề.

<short pause> Ở rìa thành phố có một khu ổ chuột, nơi sống những người mang dấu vết của tổ tiên phạm tội. Họ bị kỳ thị chỉ vì dòng dõi.

<short pause> <laugh> Kaku để ý: ngay từ thiết kế thế giới, Gachiakuta đã nói về một câu hỏi rất thời sự: cái gì bị coi là rác, và ai quyết định điều đó.
```

**ElevenLabs**

```text
Thế giới của Gachiakuta được chia làm hai tầng. Ở trên là một thành phố giàu có, nơi người ta vứt bỏ mọi thứ mà không cần suy nghĩ.

[pause] Mọi thứ bị vứt đi đều rơi xuống một vực sâu khổng lồ gọi là Hố. Không ai ở trên biết dưới đó có gì, và không ai quan tâm.

[pause] Người dân tầng trên sống sạch sẽ, tiện nghi, và chưa từng tự hỏi rác của mình đi đâu. Đối với họ, vứt xuống Hố là biến mất vĩnh viễn.

[pause] Nhưng Hố không chỉ nhận rác. Nó còn là hình phạt. Tội phạm bị ném xuống Hố, và người ta tin rằng không ai rơi xuống mà còn sống trở về.

[pause] Những người ở khu ổ chuột mang một dấu hiệu trên người, cho biết họ là hậu duệ của tội phạm. Họ chưa làm gì sai, nhưng bị đối xử như đã có tội từ lúc sinh ra.

[pause] Kaku để ý: đây là một chủ đề lặp lại trong nhiều bộ anime Kaku làm gần đây. Tougen Anki với dòng máu quỷ, Mashle với người không có phép. Có vẻ những năm gần đây anime rất quan tâm tới những người bị xã hội gạt ra lề.

[pause] Ở rìa thành phố có một khu ổ chuột, nơi sống những người mang dấu vết của tổ tiên phạm tội. Họ bị kỳ thị chỉ vì dòng dõi.

[pause] [chuckles] Kaku để ý: ngay từ thiết kế thế giới, Gachiakuta đã nói về một câu hỏi rất thời sự: cái gì bị coi là rác, và ai quyết định điều đó.
```

### c03 · Nhân vật chính: Rudo / Dưới đáy Hố

Khoảng 152 giây · cảnh s15–s28 · 1972 ký tự

**Gemini**

```text
Nhân vật chính là Rudo, một cậu thiếu niên sống ở khu ổ chuột. Cậu có một thói quen mà mọi người chê cười: nhặt lại những món đồ người khác vứt đi, sửa chữa và giữ chúng.

<short pause> Nhưng Rudo vẫn nhặt, vẫn sửa. Căn nhà nhỏ của hai cha con đầy những món đồ được cứu khỏi thùng rác, mỗi món đều hoạt động lại.

<short pause> Cậu được nuôi bởi một người cha nuôi tên Regto, người nhiều lần nhắc cậu đừng nhặt rác, vì ở thành phố này, người nhặt rác sẽ bị coi như rác.

<short pause> Rudo luôn đeo một đôi găng tay, món đồ cậu không bao giờ rời. Đôi găng này sẽ trở thành chìa khóa của cả câu chuyện.

<short pause> Không ai tin Rudo. Chỉ vì cậu sống ở khu ổ chuột, chỉ vì cậu mang dấu hiệu của tổ tiên tội phạm. Bằng chứng không quan trọng, định kiến mới quan trọng.

<short pause> Rồi một ngày, Regto bị một kẻ lạ mặt sát hại. Rudo bị vu oan là hung thủ, bị bắt, và bị ném xuống Hố.

<short pause> Kaku phải nói: tập một của Gachiakuta là một trong những tập mở đầu mạnh nhất Kaku từng xem gần đây. Nếu bạn chỉ có hai mươi phút, hãy xem tập một để quyết định.

<short pause> Đó là tập một. Và từ đây, câu chuyện thật sự bắt đầu: một cậu bé bị thế giới vứt bỏ, rơi xuống nơi chứa đựng mọi thứ bị vứt bỏ.

<short pause> Nơi đây ngập trong khói độc và mùi rác thối. Người dưới Hố phải đeo mặt nạ để thở, và học cách sống giữa những thứ người trên cao vứt bỏ.

<short pause> Dưới đáy Hố không phải là chết chóc tuyệt đối như người trên cao nghĩ. Có người sống ở đó, có cả những thị trấn được dựng lên từ rác.

<short pause> Nhưng rác ở đây cũng sinh ra quái vật: những sinh vật khổng lồ được tạo thành từ rác thải, gọi là Quái vật rác. Chúng tấn công bất cứ thứ gì sống.

<short pause> Và có một nhóm người chuyên chiến đấu với chúng, gọi là Cleaners, những người dọn dẹp. Họ không dùng súng hay phép thuật. Họ dùng đồ vật.

<short pause> Enjin có vẻ lười biếng và hay đùa, nhưng khi chiến đấu thì rất đáng tin. Anh là kiểu người thầy mà shounen nào cũng cần, và Kaku đoán bạn sẽ thích anh ngay từ tập đầu gặp mặt.

<short pause> Rudo gặp một người đàn ông tên Enjin, một Cleaner dùng chiếc ô làm vũ khí. Anh cứu Rudo khỏi quái vật, và đưa cậu vào thế giới của những người dọn dẹp.
```

**ElevenLabs**

```text
Nhân vật chính là Rudo, một cậu thiếu niên sống ở khu ổ chuột. Cậu có một thói quen mà mọi người chê cười: nhặt lại những món đồ người khác vứt đi, sửa chữa và giữ chúng.

[pause] Nhưng Rudo vẫn nhặt, vẫn sửa. Căn nhà nhỏ của hai cha con đầy những món đồ được cứu khỏi thùng rác, mỗi món đều hoạt động lại.

[pause] Cậu được nuôi bởi một người cha nuôi tên Regto, người nhiều lần nhắc cậu đừng nhặt rác, vì ở thành phố này, người nhặt rác sẽ bị coi như rác.

[pause] Rudo luôn đeo một đôi găng tay, món đồ cậu không bao giờ rời. Đôi găng này sẽ trở thành chìa khóa của cả câu chuyện.

[pause] Không ai tin Rudo. Chỉ vì cậu sống ở khu ổ chuột, chỉ vì cậu mang dấu hiệu của tổ tiên tội phạm. Bằng chứng không quan trọng, định kiến mới quan trọng.

[pause] Rồi một ngày, Regto bị một kẻ lạ mặt sát hại. Rudo bị vu oan là hung thủ, bị bắt, và bị ném xuống Hố.

[pause] Kaku phải nói: tập một của Gachiakuta là một trong những tập mở đầu mạnh nhất Kaku từng xem gần đây. Nếu bạn chỉ có hai mươi phút, hãy xem tập một để quyết định.

[pause] Đó là tập một. Và từ đây, câu chuyện thật sự bắt đầu: một cậu bé bị thế giới vứt bỏ, rơi xuống nơi chứa đựng mọi thứ bị vứt bỏ.

[pause] Nơi đây ngập trong khói độc và mùi rác thối. Người dưới Hố phải đeo mặt nạ để thở, và học cách sống giữa những thứ người trên cao vứt bỏ.

[pause] Dưới đáy Hố không phải là chết chóc tuyệt đối như người trên cao nghĩ. Có người sống ở đó, có cả những thị trấn được dựng lên từ rác.

[pause] Nhưng rác ở đây cũng sinh ra quái vật: những sinh vật khổng lồ được tạo thành từ rác thải, gọi là Quái vật rác. Chúng tấn công bất cứ thứ gì sống.

[pause] Và có một nhóm người chuyên chiến đấu với chúng, gọi là Cleaners, những người dọn dẹp. Họ không dùng súng hay phép thuật. Họ dùng đồ vật.

[pause] Enjin có vẻ lười biếng và hay đùa, nhưng khi chiến đấu thì rất đáng tin. Anh là kiểu người thầy mà shounen nào cũng cần, và Kaku đoán bạn sẽ thích anh ngay từ tập đầu gặp mặt.

[pause] Rudo gặp một người đàn ông tên Enjin, một Cleaner dùng chiếc ô làm vũ khí. Anh cứu Rudo khỏi quái vật, và đưa cậu vào thế giới của những người dọn dẹp.
```

### c04 · Sức mạnh: Jinki và Giver

Khoảng 86 giây · cảnh s29–s35 · 1124 ký tự

**Gemini**

```text
Giờ tới hệ thống sức mạnh. Gachiakuta có một khái niệm gọi là Jinki, tạm dịch là bảo khí: những món đồ được người dùng gắn bó sâu sắc, tới mức chúng thấm đẫm năng lượng từ cảm xúc và suy nghĩ của con người.

<short pause> Năng lượng trong Jinki không phải phép thuật từ trên trời rơi xuống. Nó đến từ chính con người: từ suy nghĩ, cảm xúc, ký ức gắn với món đồ.

<short pause> Người có thể đánh thức sức mạnh của những món đồ đó gọi là Giver. Không phải ai cũng làm được. Giver là người có khả năng truyền năng lượng vào đồ vật mình trân trọng.

<short pause> Mỗi Jinki là duy nhất, vì mỗi mối gắn bó là duy nhất. Chiếc ô của Enjin, cây gậy của một Cleaner khác, mỗi món có năng lực riêng phản ánh người dùng nó.

<short pause> Nghĩa là trong một thế giới đầy rác, Rudo có một kho vũ khí vô tận. Chỉ cần cậu chạm vào và thấy được giá trị của món đồ.

<short pause> Và Rudo phát hiện ra mình là một Giver. Đôi găng tay của cậu là Jinki. <short pause> Nhưng điều đặc biệt là: với đôi găng, cậu có thể đánh thức cả những món rác xung quanh, biến chúng thành vũ khí.

<short pause> <laugh> Kaku rất thích chi tiết này: người từng bị chê cười vì nhặt rác lại có năng lực biến rác thành sức mạnh. Tác giả biến điểm yếu của nhân vật thành điểm mạnh.
```

**ElevenLabs**

```text
Giờ tới hệ thống sức mạnh. Gachiakuta có một khái niệm gọi là Jinki, tạm dịch là bảo khí: những món đồ được người dùng gắn bó sâu sắc, tới mức chúng thấm đẫm năng lượng từ cảm xúc và suy nghĩ của con người.

[pause] Năng lượng trong Jinki không phải phép thuật từ trên trời rơi xuống. Nó đến từ chính con người: từ suy nghĩ, cảm xúc, ký ức gắn với món đồ.

[pause] Người có thể đánh thức sức mạnh của những món đồ đó gọi là Giver. Không phải ai cũng làm được. Giver là người có khả năng truyền năng lượng vào đồ vật mình trân trọng.

[pause] Mỗi Jinki là duy nhất, vì mỗi mối gắn bó là duy nhất. Chiếc ô của Enjin, cây gậy của một Cleaner khác, mỗi món có năng lực riêng phản ánh người dùng nó.

[pause] Nghĩa là trong một thế giới đầy rác, Rudo có một kho vũ khí vô tận. Chỉ cần cậu chạm vào và thấy được giá trị của món đồ.

[pause] Và Rudo phát hiện ra mình là một Giver. Đôi găng tay của cậu là Jinki. [pause] Nhưng điều đặc biệt là: với đôi găng, cậu có thể đánh thức cả những món rác xung quanh, biến chúng thành vũ khí.

[pause] [chuckles] Kaku rất thích chi tiết này: người từng bị chê cười vì nhặt rác lại có năng lực biến rác thành sức mạnh. Tác giả biến điểm yếu của nhân vật thành điểm mạnh.
```

### c05 · Luật của Jinki

Khoảng 79 giây · cảnh s36–s42 · 1027 ký tự

**Gemini**

```text
Trước khi đi vào luật, Kaku nhắc lại một điều: những gì Kaku nói sau đây chỉ tới khoảng tập bốn, nên bạn yên tâm, không có bí mật lớn nào bị lộ.

<short pause> Luật một: sức mạnh của Jinki đến từ sự gắn bó. Một món đồ mới mua hôm qua sẽ không có sức mạnh. Một món đồ được giữ gìn, sửa chữa, yêu quý qua nhiều năm thì có.

<short pause> Luật hai: Jinki phản ánh người dùng. Năng lực của nó thường liên quan tới ý nghĩa món đồ đó với chủ nhân.

<short pause> Kaku rất thích hình ảnh các Cleaner sửa Jinki sau mỗi trận. Giống như một người lính lau súng, nhưng ở đây họ đang chăm sóc một người bạn.

<short pause> Luật ba: nếu Jinki bị phá hủy, Giver mất vũ khí, và phải xây dựng lại mối gắn bó từ đầu. Vì vậy các Cleaner chăm sóc Jinki của mình như chăm sóc một người bạn.

<short pause> Và nó khiến hệ thống sức mạnh này rất gần với người xem. Ai trong chúng ta cũng có một món đồ như vậy. Ai trong chúng ta cũng có thể là một Giver, ít nhất là trong tưởng tượng.

<short pause> Kaku ghi chú: đây là một hệ thống sức mạnh hiếm hoi mà cách mạnh lên không phải là luyện tập hay chiến đấu, mà là yêu quý một thứ gì đó thật lâu.
```

**ElevenLabs**

```text
Trước khi đi vào luật, Kaku nhắc lại một điều: những gì Kaku nói sau đây chỉ tới khoảng tập bốn, nên bạn yên tâm, không có bí mật lớn nào bị lộ.

[pause] Luật một: sức mạnh của Jinki đến từ sự gắn bó. Một món đồ mới mua hôm qua sẽ không có sức mạnh. Một món đồ được giữ gìn, sửa chữa, yêu quý qua nhiều năm thì có.

[pause] Luật hai: Jinki phản ánh người dùng. Năng lực của nó thường liên quan tới ý nghĩa món đồ đó với chủ nhân.

[pause] Kaku rất thích hình ảnh các Cleaner sửa Jinki sau mỗi trận. Giống như một người lính lau súng, nhưng ở đây họ đang chăm sóc một người bạn.

[pause] Luật ba: nếu Jinki bị phá hủy, Giver mất vũ khí, và phải xây dựng lại mối gắn bó từ đầu. Vì vậy các Cleaner chăm sóc Jinki của mình như chăm sóc một người bạn.

[pause] Và nó khiến hệ thống sức mạnh này rất gần với người xem. Ai trong chúng ta cũng có một món đồ như vậy. Ai trong chúng ta cũng có thể là một Giver, ít nhất là trong tưởng tượng.

[pause] Kaku ghi chú: đây là một hệ thống sức mạnh hiếm hoi mà cách mạnh lên không phải là luyện tập hay chiến đấu, mà là yêu quý một thứ gì đó thật lâu.
```

### c06 · Gốc văn hóa: đồ vật có linh hồn / Nếu bạn là một Giver

Khoảng 131 giây · cảnh s43–s54 · 1707 ký tự

**Gemini**

```text
Ý tưởng đồ vật có linh hồn không phải do Gachiakuta nghĩ ra. Nó có gốc rất sâu trong văn hóa Nhật Bản.

<short pause> Trong dân gian Nhật có khái niệm tsukumogami: những đồ vật dùng lâu tới một trăm năm sẽ có linh hồn. Một chiếc ô, một chiếc đèn lồng, một đôi guốc có thể thức dậy vào ban đêm.

<short pause> Theo truyền thuyết, những đồ vật bị vứt bỏ một cách vô ơn có thể trở nên giận dữ và báo thù. Những câu chuyện này dạy người ta tôn trọng những thứ đã phục vụ mình.

<short pause> Nghe có quen không? Quái vật rác trong Gachiakuta được sinh ra từ đống đồ bị vứt đi. Còn Jinki là đồ vật được yêu quý. Hai mặt của cùng một truyền thuyết.

<short pause> Người Nhật còn có một từ rất đặc biệt: mottainai, nghĩa là thật đáng tiếc khi một thứ bị lãng phí mà chưa được dùng hết giá trị. Nó không chỉ là tiết kiệm, mà là tôn trọng đồ vật.

<short pause> Và có cả nghệ thuật kintsugi: hàn gắn đồ gốm bị vỡ bằng sơn mài trộn bột vàng. Vết nứt không bị giấu đi mà được làm nổi bật, như một phần câu chuyện của món đồ.

<short pause> <laugh> Kaku thấy đây là chìa khóa để hiểu Rudo. Cậu không nhặt rác vì nghèo. Cậu nhặt vì cậu thấy giá trị ở nơi người khác chỉ thấy đồ bỏ đi. Cậu là một tinh thần mottainai biết đi.

<short pause> Giờ đến một trò chơi nhỏ. Nếu bạn là một Giver, món đồ nào của bạn sẽ trở thành Jinki?

<short pause> Hãy nghĩ tới món đồ bạn giữ lâu nhất, sửa nhiều nhất, và buồn nhất nếu mất nó. Đó là Jinki của bạn.

<short pause> Rồi thử đoán năng lực của nó. Một chiếc đồng hồ cũ của ông có thể làm chậm thời gian. Một quyển sổ ghi chép có thể ghi nhớ đòn đánh của đối thủ. Một chiếc xe đạp có thể đưa bạn đi thật xa.

<short pause> Jinki của Kaku chắc chắn là cuốn sổ này. Năng lực: mở ra là kẻ thù phải nghe giảng mười lăm phút. Rất đáng sợ.

<short pause> Viết tên Jinki và năng lực của bạn vào bình luận nhé. Kaku sẽ chọn những Jinki sáng tạo nhất để vẽ vào một video sau.
```

**ElevenLabs**

```text
Ý tưởng đồ vật có linh hồn không phải do Gachiakuta nghĩ ra. Nó có gốc rất sâu trong văn hóa Nhật Bản.

[pause] Trong dân gian Nhật có khái niệm tsukumogami: những đồ vật dùng lâu tới một trăm năm sẽ có linh hồn. Một chiếc ô, một chiếc đèn lồng, một đôi guốc có thể thức dậy vào ban đêm.

[pause] Theo truyền thuyết, những đồ vật bị vứt bỏ một cách vô ơn có thể trở nên giận dữ và báo thù. Những câu chuyện này dạy người ta tôn trọng những thứ đã phục vụ mình.

[pause] [curious] Nghe có quen không? Quái vật rác trong Gachiakuta được sinh ra từ đống đồ bị vứt đi. Còn Jinki là đồ vật được yêu quý. Hai mặt của cùng một truyền thuyết.

[pause] Người Nhật còn có một từ rất đặc biệt: mottainai, nghĩa là thật đáng tiếc khi một thứ bị lãng phí mà chưa được dùng hết giá trị. Nó không chỉ là tiết kiệm, mà là tôn trọng đồ vật.

[pause] Và có cả nghệ thuật kintsugi: hàn gắn đồ gốm bị vỡ bằng sơn mài trộn bột vàng. Vết nứt không bị giấu đi mà được làm nổi bật, như một phần câu chuyện của món đồ.

[pause] [chuckles] Kaku thấy đây là chìa khóa để hiểu Rudo. Cậu không nhặt rác vì nghèo. Cậu nhặt vì cậu thấy giá trị ở nơi người khác chỉ thấy đồ bỏ đi. Cậu là một tinh thần mottainai biết đi.

[pause] Giờ đến một trò chơi nhỏ. Nếu bạn là một Giver, món đồ nào của bạn sẽ trở thành Jinki?

[pause] Hãy nghĩ tới món đồ bạn giữ lâu nhất, sửa nhiều nhất, và buồn nhất nếu mất nó. Đó là Jinki của bạn.

[pause] Rồi thử đoán năng lực của nó. Một chiếc đồng hồ cũ của ông có thể làm chậm thời gian. Một quyển sổ ghi chép có thể ghi nhớ đòn đánh của đối thủ. Một chiếc xe đạp có thể đưa bạn đi thật xa.

[pause] Jinki của Kaku chắc chắn là cuốn sổ này. Năng lực: mở ra là kẻ thù phải nghe giảng mười lăm phút. Rất đáng sợ.

[pause] Viết tên Jinki và năng lực của bạn vào bình luận nhé. Kaku sẽ chọn những Jinki sáng tạo nhất để vẽ vào một video sau.
```

### c07 · Vì sao nên xem: phong cách / Vì sao nên xem: câu chuyện

Khoảng 131 giây · cảnh s55–s65 · 1698 ký tự

**Gemini**

```text
Những nét graffiti xuất hiện cả trên quần áo, trên tường, trên vũ khí. Nó cho thế giới dưới Hố một cá tính đường phố rất riêng, khác hẳn vẻ sạch sẽ lạnh lùng của tầng trên.

<short pause> Lý do đầu tiên để xem Gachiakuta: phong cách hình ảnh. Bộ truyện có những hình vẽ graffiti mạnh mẽ, và anime có hẳn một nghệ sĩ thiết kế graffiti riêng.

<short pause> Chính tác giả Urana Kei từng là trợ lý của tác giả Fire Force, và bạn sẽ thấy chất năng lượng, chuyển động rất mạnh trong từng trang.

<short pause> Nhạc nền của anime cũng rất đáng chú ý, mạnh mẽ, có chất hip hop đường phố, hợp với thế giới graffiti. Kaku khuyên đeo tai nghe khi xem.

<short pause> Studio Bones, nơi từng làm My Hero Academia, mang tới những cảnh hành động rất mãn nhãn. Kaku không dùng cảnh gốc ở đây, nên bạn phải tự xem để thấy.

<short pause> Câu hỏi lớn của bộ truyện là: nếu bạn bị cả thế giới vứt bỏ, bạn sẽ đập phá nó, hay tìm cách làm nó tốt hơn? Rudo phải chọn, và lựa chọn đó không dễ.

<short pause> Lý do thứ hai: câu chuyện về bất công. Rudo bị vu oan, bị vứt bỏ, và muốn trả thù những kẻ ở tầng trên. <short pause> Nhưng dưới Hố, cậu dần học được rằng thế giới phức tạp hơn nhiều.

<short pause> Kaku thích cách bộ truyện không vẽ tầng dưới là người tốt hết, tầng trên là người xấu hết. Dưới Hố cũng có kẻ tham lam, trên cao cũng có người tử tế. Thế giới xám, không trắng đen.

<short pause> Lý do thứ ba: những nhân vật phụ có cá tính. Các Cleaner mỗi người một vẻ, và mỗi Jinki kể một câu chuyện riêng về chủ nhân.

<short pause> Theo nhiều báo cáo, con người thải ra hàng tỉ tấn rác mỗi năm. Gachiakuta không giảng đạo lý, nhưng khiến bạn nhìn lại thùng rác của mình với một chút áy náy.

<short pause> Và lý do thứ tư, Kaku thích nhất: thông điệp về đồ vật. Trong thời đại ai cũng vứt đi rất dễ dàng, một bộ anime nhắc ta rằng những thứ cũ vẫn có giá trị nếu ta biết trân trọng.
```

**ElevenLabs**

```text
Những nét graffiti xuất hiện cả trên quần áo, trên tường, trên vũ khí. Nó cho thế giới dưới Hố một cá tính đường phố rất riêng, khác hẳn vẻ sạch sẽ lạnh lùng của tầng trên.

[pause] Lý do đầu tiên để xem Gachiakuta: phong cách hình ảnh. Bộ truyện có những hình vẽ graffiti mạnh mẽ, và anime có hẳn một nghệ sĩ thiết kế graffiti riêng.

[pause] Chính tác giả Urana Kei từng là trợ lý của tác giả Fire Force, và bạn sẽ thấy chất năng lượng, chuyển động rất mạnh trong từng trang.

[pause] Nhạc nền của anime cũng rất đáng chú ý, mạnh mẽ, có chất hip hop đường phố, hợp với thế giới graffiti. Kaku khuyên đeo tai nghe khi xem.

[pause] Studio Bones, nơi từng làm My Hero Academia, mang tới những cảnh hành động rất mãn nhãn. Kaku không dùng cảnh gốc ở đây, nên bạn phải tự xem để thấy.

[pause] [curious] Câu hỏi lớn của bộ truyện là: nếu bạn bị cả thế giới vứt bỏ, bạn sẽ đập phá nó, hay tìm cách làm nó tốt hơn? Rudo phải chọn, và lựa chọn đó không dễ.

[pause] Lý do thứ hai: câu chuyện về bất công. Rudo bị vu oan, bị vứt bỏ, và muốn trả thù những kẻ ở tầng trên. [pause] Nhưng dưới Hố, cậu dần học được rằng thế giới phức tạp hơn nhiều.

[pause] Kaku thích cách bộ truyện không vẽ tầng dưới là người tốt hết, tầng trên là người xấu hết. Dưới Hố cũng có kẻ tham lam, trên cao cũng có người tử tế. Thế giới xám, không trắng đen.

[pause] Lý do thứ ba: những nhân vật phụ có cá tính. Các Cleaner mỗi người một vẻ, và mỗi Jinki kể một câu chuyện riêng về chủ nhân.

[pause] Theo nhiều báo cáo, con người thải ra hàng tỉ tấn rác mỗi năm. Gachiakuta không giảng đạo lý, nhưng khiến bạn nhìn lại thùng rác của mình với một chút áy náy.

[pause] Và lý do thứ tư, Kaku thích nhất: thông điệp về đồ vật. Trong thời đại ai cũng vứt đi rất dễ dàng, một bộ anime nhắc ta rằng những thứ cũ vẫn có giá trị nếu ta biết trân trọng.
```

### c08 · Nếu bạn thích bộ này, bạn sẽ thích Gachiakuta / Lộ trình xem cho người mới

Khoảng 122 giây · cảnh s66–s77 · 1591 ký tự

**Gemini**

```text
Nếu bạn còn phân vân, đây là cách Kaku gợi ý nhanh. Nếu bạn thích Fire Force, bạn sẽ thích nhịp hành động và cách vẽ đầy năng lượng của Gachiakuta.

<short pause> Nếu bạn thích Dr. Stone, bạn sẽ thích cảm giác biến những thứ tưởng như vô dụng thành công cụ hữu ích.

<short pause> Nếu bạn thích Chainsaw Man, bạn sẽ thích thế giới u ám, bẩn thỉu nhưng đầy cá tính của tầng dưới.

<short pause> Và nếu bạn chưa thích bộ nào kể trên, Gachiakuta vẫn là một cửa vào dễ chịu cho thể loại shounen hiện đại: nhân vật chính rõ ràng, thế giới dễ hiểu, và hệ thống sức mạnh gắn với cảm xúc.

<short pause> <laugh> Kaku nói nhỏ: Kaku đã giới thiệu bộ này cho một người bạn chỉ xem anime lãng mạn. Người đó xem hết mùa một trong ba ngày.

<short pause> Nếu bạn thích đọc hơn, manga Gachiakuta đăng trên tạp chí Shonen Magazine từ năm 2022, và có rất nhiều trang graffiti chi tiết mà anime khó truyền tải hết.

<short pause> Nếu bạn quyết định xem, đây là lộ trình Kaku gợi ý. Tập một tới tập ba: làm quen thế giới và lý do Rudo rơi xuống Hố. Đừng bỏ qua tập một, vì mọi chi tiết đều quan trọng về sau.

<short pause> Tập bốn tới tập tám: Rudo gia nhập Cleaners và học về Jinki. Đây là lúc hệ thống sức mạnh được giải thích rõ nhất.

<short pause> Sau đó: những nhiệm vụ lớn hơn và những bí mật về Hố. Kaku sẽ không nói thêm.

<short pause> Mẹo nhỏ của Kaku: xem xong mỗi tập, hãy để ý xem Jinki của từng nhân vật nói gì về quá khứ của họ. Đó là cách bộ truyện kể chuyện mà không cần lời.

<short pause> Nếu bạn xem cùng bạn bè, hãy thử trò này: mỗi người đoán năng lực của một Jinki trước khi nó được tiết lộ. Ai đoán đúng nhiều nhất thì được chọn tập tiếp theo.

<short pause> Mùa một có khoảng hai mươi bốn tập. Nếu bạn xem mỗi tối hai tập, bạn sẽ kịp xem hết trước khi mùa hai ra mắt.
```

**ElevenLabs**

```text
Nếu bạn còn phân vân, đây là cách Kaku gợi ý nhanh. Nếu bạn thích Fire Force, bạn sẽ thích nhịp hành động và cách vẽ đầy năng lượng của Gachiakuta.

[pause] Nếu bạn thích Dr. Stone, bạn sẽ thích cảm giác biến những thứ tưởng như vô dụng thành công cụ hữu ích.

[pause] Nếu bạn thích Chainsaw Man, bạn sẽ thích thế giới u ám, bẩn thỉu nhưng đầy cá tính của tầng dưới.

[pause] Và nếu bạn chưa thích bộ nào kể trên, Gachiakuta vẫn là một cửa vào dễ chịu cho thể loại shounen hiện đại: nhân vật chính rõ ràng, thế giới dễ hiểu, và hệ thống sức mạnh gắn với cảm xúc.

[pause] [chuckles] Kaku nói nhỏ: Kaku đã giới thiệu bộ này cho một người bạn chỉ xem anime lãng mạn. Người đó xem hết mùa một trong ba ngày.

[pause] Nếu bạn thích đọc hơn, manga Gachiakuta đăng trên tạp chí Shonen Magazine từ năm 2022, và có rất nhiều trang graffiti chi tiết mà anime khó truyền tải hết.

[pause] Nếu bạn quyết định xem, đây là lộ trình Kaku gợi ý. Tập một tới tập ba: làm quen thế giới và lý do Rudo rơi xuống Hố. Đừng bỏ qua tập một, vì mọi chi tiết đều quan trọng về sau.

[pause] Tập bốn tới tập tám: Rudo gia nhập Cleaners và học về Jinki. Đây là lúc hệ thống sức mạnh được giải thích rõ nhất.

[pause] Sau đó: những nhiệm vụ lớn hơn và những bí mật về Hố. Kaku sẽ không nói thêm.

[pause] Mẹo nhỏ của Kaku: xem xong mỗi tập, hãy để ý xem Jinki của từng nhân vật nói gì về quá khứ của họ. Đó là cách bộ truyện kể chuyện mà không cần lời.

[pause] Nếu bạn xem cùng bạn bè, hãy thử trò này: mỗi người đoán năng lực của một Jinki trước khi nó được tiết lộ. Ai đoán đúng nhiều nhất thì được chọn tập tiếp theo.

[pause] Mùa một có khoảng hai mươi bốn tập. Nếu bạn xem mỗi tối hai tập, bạn sẽ kịp xem hết trước khi mùa hai ra mắt.
```

### c09 · Kết

Khoảng 55 giây · cảnh s78–s82 · 715 ký tự

**Gemini**

```text
Tóm lại trong một câu: Gachiakuta là shounen hành động có graffiti, có hệ thống sức mạnh dễ hiểu, và có một thông điệp mà bạn mang theo được sau khi tắt màn hình.

<short pause> Và lần tới bạn định vứt một món đồ cũ, hãy dừng lại một giây và nghĩ: nó đã ở bên bạn bao lâu rồi?

<short pause> Gachiakuta là câu chuyện về một cậu bé bị coi là rác, rơi xuống nơi chứa mọi thứ bị coi là rác, và phát hiện ra rằng rác có thể trở thành sức mạnh nếu có người trân trọng.

<short pause> Video tiếp theo, Kaku đặt ba bộ du hành thời gian lên cùng một bàn cân: Tokyo Revengers, Steins;Gate và Re:Zero. Luật của bộ nào chặt chẽ nhất?

<short pause> <laugh> Nếu video nhập môn này giúp bạn quyết định xem Gachiakuta, hãy đăng ký kênh để Kaku mở thêm nhiều cánh cửa nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại trong một câu: Gachiakuta là shounen hành động có graffiti, có hệ thống sức mạnh dễ hiểu, và có một thông điệp mà bạn mang theo được sau khi tắt màn hình.

[pause] [curious] Và lần tới bạn định vứt một món đồ cũ, hãy dừng lại một giây và nghĩ: nó đã ở bên bạn bao lâu rồi?

[pause] Gachiakuta là câu chuyện về một cậu bé bị coi là rác, rơi xuống nơi chứa mọi thứ bị coi là rác, và phát hiện ra rằng rác có thể trở thành sức mạnh nếu có người trân trọng.

[pause] Video tiếp theo, Kaku đặt ba bộ du hành thời gian lên cùng một bàn cân: Tokyo Revengers, Steins;Gate và Re:Zero. Luật của bộ nào chặt chẽ nhất?

[pause] [chuckles] Nếu video nhập môn này giúp bạn quyết định xem Gachiakuta, hãy đăng ký kênh để Kaku mở thêm nhiều cánh cửa nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
