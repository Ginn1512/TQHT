# Bộ prompt · Dungeon Meshi: Hồ sơ quái vật hầm ngục — và con nào ăn được?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói tới hết anime Dungeon Meshi mùa một, hai mươi bốn tập. Kaku không nói gì về p…

```text
Wide 16:9 landscape cinematic frame. a closed leather field journal with a small fork and spoon tied to its strap, resting on a stone dungeon floor, close-up, warm torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Bạn đang ở tầng sâu của một hầm ngục. Hết tiền, hết lương thực, và đồng đội của bạn vừa bị một con rồng nuốt…

```text
Wide 16:9 landscape cinematic frame. a small adventuring party sitting exhausted around an empty cooking pot in a dark stone corridor, wide shot, dim torchlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Câu trả lời của Dungeon Meshi rất đơn giản: ăn quái vật.

```text
Wide 16:9 landscape cinematic frame. a cooking pot bubbling over a campfire with a strange tentacle poking out over the rim, humorous close-up, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và từ ý tưởng tưởng như đùa đó, tác giả Kui Ryoko xây nên một trong những thế giới giả tưởng chi tiết nhất Ka…

```text
Wide 16:9 landscape cinematic frame. an illustrated naturalist's notebook with detailed anatomical sketches of fantasy creatures and handwritten notes, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Hôm nay Kaku mở một hồ sơ đặc biệt: hồ sơ quái vật hầm ngục. Mỗi con một thẻ: tên, loại, điểm mạnh, điểm yếu,…

```text
Wide 16:9 landscape cinematic frame. a stack of index cards with creature sketches and a small spoon icon rating on each, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku vừa là nhà sinh vật học, vừa là đầu bếp, và hơi đói bụng một chút.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny chef's apron, holding a notebook in one wing and a ladle in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Cách đọc hồ sơ

Lời: Mỗi thẻ hồ sơ có sáu dòng. Tên và loại. Điểm mạnh, tức là cách nó gây nguy hiểm. Điểm yếu, tức là cách đánh b…

```text
Wide 16:9 landscape cinematic frame. a blank index card template drawn on parchment with six labeled lines, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Kaku chấm thêm độ ngon theo thang năm cái muỗng, dựa trên phản ứng của nhân vật trong truyện. Đây là cảm nhận…

```text
Wide 16:9 landscape cinematic frame. five small spoons lined up on a wooden table, three of them polished and two dull, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Và Kaku nói rõ trước: đây là quái vật giả tưởng. Ngoài đời, đừng bao giờ ăn nấm dại, côn trùng lạ hay động vậ…

```text
Wide 16:9 landscape cinematic frame. a warning card with a crossed-out wild mushroom drawing pinned to a kitchen corkboard, close-up, clear light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Hồ sơ chia làm bốn nhóm: quái vật tầng nông, kẻ giả dạng, sinh vật kỳ lạ, và cuối cùng là con rồng.

```text
Wide 16:9 landscape cinematic frame. four colored folder tabs sticking out of a thick case file on a stone table, close-up, warm torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Bối cảnh: Dungeon Meshi là gì?

Lời: Dungeon Meshi là manga của Kui Ryoko, đăng trên tạp chí Harta từ năm 2014 tới 2023, gồm mười bốn tập. Anime d…

```text
Wide 16:9 landscape cinematic frame. a neat stack of fourteen manga volumes beside a streaming remote on a cozy table, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Câu chuyện theo Laios, một chiến binh mê quái vật tới mức kỳ quặc. Em gái anh, Falin, bị một con rồng đỏ nuốt…

```text
Wide 16:9 landscape cinematic frame. a huge red dragon silhouette looming in a dark underground cavern with a tiny figure standing defiantly before it, wide shot, fiery red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Trong thế giới này, người chết trong hầm ngục có thể được hồi sinh bằng phép thuật, nếu thi thể còn nguyên vẹ…

```text
Wide 16:9 landscape cinematic frame. an hourglass with red sand running quickly placed on a map of a deep dungeon, close-up, tense torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Không đủ tiền mua lương thực, Laios đề xuất một ý điên rồ: vừa đi vừa ăn quái vật. Cả nhóm phản đối, trừ chín…

```text
Wide 16:9 landscape cinematic frame. a tall adventurer excitedly holding up a monster cookbook while two companions look horrified, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Rồi họ gặp một người lùn đã sống trong hầm ngục nhiều năm, chuyên nấu quái vật. Người đó tên Senshi, và ông t…

```text
Wide 16:9 landscape cinematic frame. a stout bearded cook stirring a large pot over a fire in a stone alcove, his back to the viewer, medium shot, warm cozy firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích cách bộ truyện xem hầm ngục như một hệ sinh thái thật. Quái vật ăn gì, sống ở đâu, sinh sản th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering through a tiny magnifying glass at a mushroom growing between dungeon stones. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Bốn người trong bếp

Lời: Trước khi mở hồ sơ, hãy làm quen với bốn thực khách, vì mỗi người phản ứng với món quái vật một kiểu, và đó l…

```text
Wide 16:9 landscape cinematic frame. four empty wooden bowls of different sizes placed around a campfire on a stone floor, close-up, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Laios, trưởng nhóm, mê quái vật từ nhỏ. Với anh, được ăn quái vật là một giấc mơ. Anh thường là người háo hức…

```text
Wide 16:9 landscape cinematic frame. a tall adventurer leaning eagerly over a bubbling pot with shining eyes, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Marcille, pháp sư tộc elf, là người phản đối dữ nhất. Cô kêu la, từ chối, rồi cuối cùng vẫn ăn, và thường là…

```text
Wide 16:9 landscape cinematic frame. a slender mage covering her mouth in disgust at a strange dish, then a second small panel of her happily eating, humorous split illustration. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Chilchuck, thợ mở khóa tộc người nhỏ, là người thực tế nhất. Anh không quan tâm quái vật ngon hay không, chỉ…

```text
Wide 16:9 landscape cinematic frame. a small figure with lockpicks and a skeptical expression inspecting a spoonful of stew, close-up, dry humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và Senshi, người nấu, xem mỗi bữa ăn như một cách tôn trọng hầm ngục. Bốn người, bốn thái độ, và mỗi món ăn t…

```text
Wide 16:9 landscape cinematic frame. a stout bearded cook carefully tasting broth from a wooden ladle, his back to the viewer, medium shot, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Nhóm A: quái vật tầng nông

Lời: Hồ sơ số một: Bọ cạp khổng lồ. Loại: côn trùng hầm ngục. Điểm mạnh: càng khỏe và đuôi độc. Điểm yếu: phần khớ…

```text
Wide 16:9 landscape cinematic frame. a giant scorpion with a glossy segmented shell crouched on a rocky dungeon floor, low-angle shot, dramatic torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Hồ sơ số hai: Nấm biết đi. Loại: nấm có chân, di chuyển được. Điểm mạnh: bào tử. Điểm yếu: chậm, và chân dễ b…

```text
Wide 16:9 landscape cinematic frame. a large mushroom with stubby legs waddling across a mossy dungeon corridor, humorous medium shot, soft glowing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Senshi còn chỉ ra một điều: phần ngon nhất của nấm biết đi lại là phần chân, chỗ cơ bắp chắc nhất. Món đầu ti…

```text
Wide 16:9 landscape cinematic frame. sliced mushroom stems arranged neatly on a wooden cutting board beside a small knife, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Món ăn: lẩu bọ cạp và nấm biết đi, món đầu tiên trong truyện. Senshi luộc bọ cạp như luộc cua, và nhóm bất ng…

```text
Wide 16:9 landscape cinematic frame. a steaming hot pot with a red crab-like shell and sliced mushrooms floating in broth over a campfire, close-up, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Hồ sơ số ba: Slime. Loại: sinh vật không xương dạng keo. Điểm mạnh: bịt kín miệng mũi con mồi. Điểm yếu: dễ b…

```text
Wide 16:9 landscape cinematic frame. a translucent jelly-like blob sliding across a damp stone floor, glistening in torchlight, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Món ăn: slime phơi khô. Senshi lấy phần cơ quan bên trong, phơi khô, dùng như một nguyên liệu cao cấp. Kaku c…

```text
Wide 16:9 landscape cinematic frame. thin translucent sheets drying on a small wooden rack beside a dungeon campfire, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Một mẹo của Senshi mà Kaku rất thích: nếu không chắc một quái vật có ăn được không, hãy xem những sinh vật kh…

```text
Wide 16:9 landscape cinematic frame. a small bird pecking at a mushroom on a dungeon floor while a cook watches from behind a rock, humorous medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Hồ sơ số bốn: Basilisk. Loại: nửa gà trống, nửa rắn. Điểm mạnh: nọc độc và đuôi rắn. Điểm yếu: phần thân gà v…

```text
Wide 16:9 landscape cinematic frame. a large rooster-like creature with a long serpent tail coiled behind it, standing in a ruined dungeon hall, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Món ăn: basilisk quay và trứng ốp la. Thịt gà mềm, phần đuôi rắn ngon như thịt trắng. Kaku chấm năm muỗng. Đâ…

```text
Wide 16:9 landscape cinematic frame. a golden roasted bird with crispy skin on a wooden board beside a fluffy omelette in a small pan, close-up, appetizing warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Hồ sơ số năm: Mandrake. Loại: cây có rễ hình người. Điểm mạnh: tiếng hét khi bị nhổ lên, có thể làm người ngh…

```text
Wide 16:9 landscape cinematic frame. a strange root with a vaguely human shape half pulled from dark soil, close-up, eerie greenish light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Trong Dungeon Meshi, Senshi có cách nhổ mandrake an toàn, và dùng củ của nó như một loại rau củ trong món trứ…

```text
Wide 16:9 landscape cinematic frame. a pale root vegetable being sliced into a sizzling pan of eggs, close-up, appetizing warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Kaku thích mandrake vì đây là quái vật có gốc thật trong truyền thuyết châu Âu. Người xưa tin rằng ai nhổ man…

```text
Wide 16:9 landscape cinematic frame. an old European herbal manuscript page with an illustration of a human-shaped root, close-up, aged parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Nhóm B: kẻ giả dạng

Lời: Nhóm thứ hai khiến Kaku thích nhất: những kẻ giả dạng. Nhìn một đằng, bên trong một nẻo.

```text
Wide 16:9 landscape cinematic frame. a folder tab labeled with a small mask icon opened on a stone table, close-up, warm torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Hồ sơ số sáu: Giáp sống. Loại: một bộ giáp tự di chuyển, cầm kiếm tấn công. Điểm mạnh: cứng, và không có đầu…

```text
Wide 16:9 landscape cinematic frame. an empty suit of plate armor walking stiffly down a dark dungeon corridor holding a sword, low-angle shot, ominous torchlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Và đây là phát hiện tuyệt vời nhất của Laios: bên trong bộ giáp không có linh hồn nào. Chỉ có một đàn sinh vậ…

```text
Wide 16:9 landscape cinematic frame. the inside of an opened armor breastplate revealing clusters of small shellfish-like creatures clinging to the metal, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Món ăn: giáp sống xào kiểu người lùn. Senshi nấu chúng như hải sản. Kaku chấm bốn muỗng, và thêm một điểm cho…

```text
Wide 16:9 landscape cinematic frame. a sizzling pan of stir-fried shellfish with herbs over a campfire, close-up, appetizing warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Hồ sơ số bảy: Mimic, rương báu giả. Loại: sinh vật sống trong rương. Điểm mạnh: kẹp chặt tay kẻ tham lam mở r…

```text
Wide 16:9 landscape cinematic frame. an old wooden treasure chest slightly open with a pair of crustacean claws peeking out from the gap, close-up, suspenseful torchlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Trong Dungeon Meshi, mimic giống một loài giáp xác, như tôm hay cua ẩn sĩ, sống trong rương như cua ẩn sĩ sốn…

```text
Wide 16:9 landscape cinematic frame. a pot of boiled crustacean legs steaming on a stone slab beside an empty treasure chest, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Hồ sơ số tám: Golem. Loại: người đá khổng lồ, bảo vệ một khu vực. Điểm mạnh: to, nặng, gần như không biết đau…

```text
Wide 16:9 landscape cinematic frame. a massive stone golem with moss growing on its shoulders standing guard in an underground cavern, low-angle shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và Senshi làm một việc không ai nghĩ tới: ông dùng lưng golem làm vườn rau. Đất trên lưng golem màu mỡ, lại đ…

```text
Wide 16:9 landscape cinematic frame. vegetables and leafy greens growing neatly in soil on the back of a sleeping stone giant, wide shot, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Có một chi tiết hài hước: khi cả nhóm cần đánh golem, Senshi lại lo cho vườn rau của mình hơn. Với ông, golem…

```text
Wide 16:9 landscape cinematic frame. a stout cook shielding a row of vegetables with his arms while a stone giant stirs behind him, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy chi tiết golem là linh hồn của Dungeon Meshi. Quái vật không chỉ là kẻ thù hay thức ăn. Nó là một p…

```text
Wide 16:9 landscape cinematic frame. the owl mascot happily harvesting a small carrot from a mossy stone surface. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Nhóm C: sinh vật kỳ lạ

Lời: Hồ sơ số chín: Hồn ma. Loại: linh hồn không thể chạm. Điểm mạnh: kéo nhiệt độ xuống rất thấp, làm con người l…

```text
Wide 16:9 landscape cinematic frame. a pale translucent ghostly shape drifting through a frosty stone chamber, frost patterns spreading on the walls, medium shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Senshi không ăn được hồn ma. Nhưng ông lợi dụng nó. Ông làm một loại nước thánh ngọt, rồi để hồn ma làm đông…

```text
Wide 16:9 landscape cinematic frame. a small bowl of pale shaved ice dessert with frost crystals on a stone table in a cold chamber, close-up, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Chi tiết thú vị: Senshi coi việc trừ tà và làm kem là cùng một việc. Hồn ma được siêu thoát, cả nhóm có món t…

```text
Wide 16:9 landscape cinematic frame. a faint ghostly shape rising peacefully toward a soft light above a small bowl of frozen dessert, symbolic close-up, gentle blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Kaku chấm bốn muỗng, và cho thêm một huy chương cho món có tên hay nhất cả hồ sơ.

```text
Wide 16:9 landscape cinematic frame. a tiny gold medal placed next to a bowl of frosty dessert, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Hồ sơ số mười: Bọ châu báu. Loại: côn trùng giả làm đồ trang sức. Điểm mạnh: lừa kẻ tham lam nhặt lên. Điểm y…

```text
Wide 16:9 landscape cinematic frame. a small pile of what looks like gemstones and gold rings on a stone floor, some of them sprouting tiny insect legs, close-up, sparkling light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Kaku để ý: trong hầm ngục, những kẻ tham lam thường là người chết sớm nhất. Mimic, bọ châu báu, đều là cái bẫ…

```text
Wide 16:9 landscape cinematic frame. a skeleton hand still clutching a fake jewel beside an open chest in a dusty corner, close-up, eerie dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Một bài học nho nhỏ của hầm ngục: không phải thứ gì lấp lánh cũng là báu vật. Và đôi khi, báu vật lại ngọt, v…

```text
Wide 16:9 landscape cinematic frame. a jeweled ring beside a small spoon of glossy dessert, still life, sparkling warm light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Hồ sơ số mười một: Vòng nấm tiên. Loại: một vòng nấm mọc tròn, nơi các sinh vật tí hon sống. Điểm mạnh: ai bư…

```text
Wide 16:9 landscape cinematic frame. a perfect ring of pale mushrooms growing on a mossy dungeon floor, tiny glowing lights hovering above it, wide shot, magical soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kaku thấy chương vòng nấm là cách tác giả cho các nhân vật thử sống trong thân thể người khác. Và họ hiểu nha…

```text
Wide 16:9 landscape cinematic frame. four pairs of different-sized boots placed swapped in front of four different-sized sleeping bags, whimsical close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Ở cuối mùa một, cả nhóm bị hoán đổi chủng tộc sau khi bước vào vòng nấm. Người lùn thành người cao, người cao…

```text
Wide 16:9 landscape cinematic frame. a plate of steamed dumplings on a flat stone beside a ring of mushrooms, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Nhóm D: Rồng đỏ

Lời: Và hồ sơ cuối cùng, hồ sơ số mười hai: Rồng đỏ. Loại: rồng. Điểm mạnh: lửa, sức mạnh, và vảy gần như không th…

```text
Wide 16:9 landscape cinematic frame. a colossal red dragon rearing up in a vast underground chamber, flames curling from its jaws, dramatic low-angle wide shot, intense red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Điểm yếu: như mọi sinh vật, rồng có phần cổ và vảy ngược. Laios, người mê quái vật, biết rõ cơ thể rồng hơn a…

```text
Wide 16:9 landscape cinematic frame. an anatomical sketch of a dragon's neck with a single circled scale drawn in red ink, parchment close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Kaku không kể chi tiết trận đánh để bạn tự xem. Nhưng nó là một trong những trận hay nhất của anime năm 2024,…

```text
Wide 16:9 landscape cinematic frame. a small group of shadows standing firm before a giant red silhouette in a firelit cavern, wide shot, dramatic contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Và sau trận đánh là câu hỏi không thể tránh: ăn rồng thế nào? Senshi làm cả một bữa tiệc: thịt nướng, giăm bô…

```text
Wide 16:9 landscape cinematic frame. a feast spread on a huge stone slab with roasted meat, hams hanging from a rack, and bowls of broth, wide shot, warm celebratory firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Mùa một khép lại ở đây, với những câu hỏi còn bỏ ngỏ về Falin và bí mật sâu hơn của hầm ngục. Mùa hai sẽ trả…

```text
Wide 16:9 landscape cinematic frame. a dark staircase leading deeper into a dungeon with a faint glow at the bottom, wide shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Nhưng Kaku muốn nói rõ: bữa tiệc rồng không hoàn toàn vui vẻ. Vì cả nhóm biết rằng trong bụng rồng là Falin.…

```text
Wide 16:9 landscape cinematic frame. a quiet campfire scene after a feast with the party sitting in silence, bones and empty bowls around them, wide shot, somber warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là lúc Dungeon Meshi cho thấy chiều sâu thật sự. Ăn không chỉ là để sống. Ăn là chấp nhận rằng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small bowl with both wings and bowing its head quietly before eating. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Luật ẩm thực hầm ngục của Senshi

Lời: Qua cả mùa một, Senshi dạy cả nhóm vài luật ăn uống rất giản dị. Kaku ghi lại năm luật.

```text
Wide 16:9 landscape cinematic frame. a small handwritten recipe card with five numbered lines pinned to a wooden board, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Luật một: ăn uống cân bằng. Dù ở hầm ngục, vẫn phải có rau, thịt, tinh bột. Đó là lý do ông trồng rau trên lư…

```text
Wide 16:9 landscape cinematic frame. a rustic plate with a balanced portion of vegetables, meat and bread on a stone table, close-up, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Luật hai: không lãng phí. Đã giết một sinh vật thì phải dùng hết những gì có thể dùng.

```text
Wide 16:9 landscape cinematic frame. neatly separated piles of bones, meat and hide on a clean butcher's board, still life, soft light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Luật ba: tôn trọng hệ sinh thái. Nếu ăn quá nhiều một loài, cả hầm ngục sẽ mất cân bằng.

```text
Wide 16:9 landscape cinematic frame. a simple food chain diagram drawn on parchment with arrows connecting mushrooms, insects, birds and a dragon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Luật bốn: nấu cho đúng. Nhiều quái vật có độc nếu ăn sai cách. Senshi luôn biết phần nào ăn được, phần nào ph…

```text
Wide 16:9 landscape cinematic frame. a cook's knife carefully separating a dark gland from pale meat on a board, extreme close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Luật năm, luật Kaku thích nhất: ăn cùng nhau. Những bữa ăn chung là lúc nhóm hiểu nhau hơn, cãi nhau, làm hòa…

```text
Wide 16:9 landscape cinematic frame. a small group sitting close together around a campfire sharing food from one pot, back view, wide shot, warm golden firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku thêm luật thứ sáu của riêng mình, không có trong truyện: rửa nồi ngay sau khi ăn. Vì trong hầm ngục, mùi…

```text
Wide 16:9 landscape cinematic frame. a cook scrubbing a pot in an underground stream while glowing eyes watch curiously from the darkness nearby, humorous wide shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Quái vật và đời thật

Lời: Nhiều quái vật trong Dungeon Meshi có gốc từ truyền thuyết châu Âu. Basilisk trong truyền thuyết là vua của l…

```text
Wide 16:9 landscape cinematic frame. an old bestiary illustration of a crowned serpent with a rooster's head, aged parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nhưng Kui Ryoko làm một việc thú vị: bà lấy quái vật truyền thuyết rồi hỏi, nếu nó có thật thì cơ thể nó hoạt…

```text
Wide 16:9 landscape cinematic frame. a split page: on the left a fantasy creature drawing, on the right a detailed anatomical cross-section of the same creature, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Giáp sống thành trai hến. Mimic thành cua ẩn sĩ. Đây là cách biến truyền thuyết thành sinh học giả tưởng rất…

```text
Wide 16:9 landscape cinematic frame. a real hermit crab peeking out of a shell on wet sand beside a tiny toy treasure chest, close-up, bright beach light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và Kaku nhắc lại một lần nữa: ngoài đời, nấm dại có thể gây chết người, và nhiều loài vật hoang dã mang mầm b…

```text
Wide 16:9 landscape cinematic frame. a basket of wild mushrooms with a red warning sign beside it on a forest floor, close-up, clear daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Nếu bạn là đầu bếp hầm ngục

Lời: Giờ tới trò chơi nhỏ. Bạn là đầu bếp của một nhóm phiêu lưu, và trước mặt bạn là ba con quái vật: một slime,…

```text
Wide 16:9 landscape cinematic frame. three small creature sketches on a parchment menu card with empty checkboxes beside them, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn mimic, luộc với chút muối và thảo mộc, vì Kaku tin mọi thứ giống cua đều ngon. Và vì Kaku muốn trả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding up a boiled crab-like claw on a tiny plate, looking triumphant. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Còn bạn? Bạn chọn con nào, nấu món gì, và đặt tên món là gì? Tên hay nhất sẽ được Kaku vẽ lên một thẻ hồ sơ đ…

```text
Wide 16:9 landscape cinematic frame. a blank recipe card and a pencil resting on a stone table beside a small campfire, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Gợi ý của Senshi mà Kaku rất thích: món ngon nhất không phải món cầu kỳ nhất, mà là món làm cả nhóm ngồi lại…

```text
Wide 16:9 landscape cinematic frame. a group of hands reaching into a shared pot with ladles and bowls, close-up, warm cozy firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Mục lục hồ sơ

Lời: Và đây là mục lục hồ sơ quái vật. Nhóm A, tầng nông: bọ cạp khổng lồ, nấm biết đi, slime, basilisk, mandrake.

```text
Wide 16:9 landscape cinematic frame. an index page of a field journal listing entries with small creature doodles beside each, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nhóm B, kẻ giả dạng: giáp sống, mimic, golem. Nhóm C, sinh vật kỳ lạ: hồn ma, bọ châu báu, vòng nấm tiên. Và…

```text
Wide 16:9 landscape cinematic frame. the second half of the index page with more doodles and a large dragon sketch at the bottom, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Giải món ngon nhất theo Kaku: đồng hạng năm muỗng, basilisk quay và tiệc rồng. Giải món sáng tạo nhất: giáp s…

```text
Wide 16:9 landscape cinematic frame. three small ribbons pinned beside three dish sketches on a journal page, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Còn bạn? Bạn muốn thử món nào nhất, và món nào bạn nhất quyết không ăn? Viết vào bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a fork and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Góc nhìn của Kaku

Lời: Kaku nghĩ Dungeon Meshi là một bộ truyện về sự tò mò. Laios nhìn quái vật không bằng sợ hãi, mà bằng câu hỏi:…

```text
Wide 16:9 landscape cinematic frame. a curious adventurer crouching to observe a small creature on the dungeon floor with a notebook in hand, medium shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và khi bạn tò mò về một thứ, bạn bắt đầu hiểu nó, rồi tôn trọng nó. Kể cả khi thứ đó muốn ăn bạn.

```text
Wide 16:9 landscape cinematic frame. a small figure and a large gentle creature sitting side by side at the edge of an underground lake, back view, wide shot, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Dungeon Meshi dạy ta rằng mọi thứ trong hầm ngục đều nối với nhau, qua một thứ rất bình thường: bữa ăn.

```text
Wide 16:9 landscape cinematic frame. a single cooking pot over a small fire in a vast dark cavern, a thin wisp of steam rising toward faint light above, wide shot, warm and cold contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tiếp theo, Kaku phân tích một trong những trận đấu được tìm nhiều nhất của Naruto: Naruto đấu với Pain,…

```text
Wide 16:9 landscape cinematic frame. a crater in the middle of a destroyed village with two small figures facing each other, wide shot, dramatic overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu hồ sơ này làm bạn đói bụng, Kaku xin lỗi. Hãy đăng ký kênh, rồi đi ăn một bữa thật ngon với người bạn thư…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting at a tiny table with a napkin tucked in, raising a spoon in farewell. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc hồ sơ

Khoảng 102 giây · cảnh s01–s10 · 1332 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime Dungeon Meshi mùa một, hai mươi bốn tập. Kaku không nói gì về phần sau trong manga.

<short pause> Bạn đang ở tầng sâu của một hầm ngục. Hết tiền, hết lương thực, và đồng đội của bạn vừa bị một con rồng nuốt mất. Bạn sẽ làm gì?

<short pause> Câu trả lời của Dungeon Meshi rất đơn giản: ăn quái vật.

<short pause> Và từ ý tưởng tưởng như đùa đó, tác giả Kui Ryoko xây nên một trong những thế giới giả tưởng chi tiết nhất Kaku từng đọc. Mỗi con quái vật đều có cơ thể, tập tính, và mùi vị.

<short pause> Hôm nay Kaku mở một hồ sơ đặc biệt: hồ sơ quái vật hầm ngục. Mỗi con một thẻ: tên, loại, điểm mạnh, điểm yếu, và câu hỏi quan trọng nhất, ăn được không?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku vừa là nhà sinh vật học, vừa là đầu bếp, và hơi đói bụng một chút.

<short pause> Mỗi thẻ hồ sơ có sáu dòng. Tên và loại. Điểm mạnh, tức là cách nó gây nguy hiểm. Điểm yếu, tức là cách đánh bại nó. Và cuối cùng là món ăn mà nhóm đã nấu từ nó.

<short pause> Kaku chấm thêm độ ngon theo thang năm cái muỗng, dựa trên phản ứng của nhân vật trong truyện. Đây là cảm nhận của Kaku, không phải con số chính thức.

<short pause> Và Kaku nói rõ trước: đây là quái vật giả tưởng. Ngoài đời, đừng bao giờ ăn nấm dại, côn trùng lạ hay động vật hoang dã chưa rõ nguồn gốc. Video này không phải hướng dẫn ăn uống.

<short pause> Hồ sơ chia làm bốn nhóm: quái vật tầng nông, kẻ giả dạng, sinh vật kỳ lạ, và cuối cùng là con rồng.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime Dungeon Meshi mùa một, hai mươi bốn tập. Kaku không nói gì về phần sau trong manga.

[pause] Bạn đang ở tầng sâu của một hầm ngục. Hết tiền, hết lương thực, và đồng đội của bạn vừa bị một con rồng nuốt mất. [curious] Bạn sẽ làm gì?

[pause] Câu trả lời của Dungeon Meshi rất đơn giản: ăn quái vật.

[pause] Và từ ý tưởng tưởng như đùa đó, tác giả Kui Ryoko xây nên một trong những thế giới giả tưởng chi tiết nhất Kaku từng đọc. Mỗi con quái vật đều có cơ thể, tập tính, và mùi vị.

[pause] Hôm nay Kaku mở một hồ sơ đặc biệt: hồ sơ quái vật hầm ngục. Mỗi con một thẻ: tên, loại, điểm mạnh, điểm yếu, và câu hỏi quan trọng nhất, ăn được không?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku vừa là nhà sinh vật học, vừa là đầu bếp, và hơi đói bụng một chút.

[pause] Mỗi thẻ hồ sơ có sáu dòng. Tên và loại. Điểm mạnh, tức là cách nó gây nguy hiểm. Điểm yếu, tức là cách đánh bại nó. Và cuối cùng là món ăn mà nhóm đã nấu từ nó.

[pause] Kaku chấm thêm độ ngon theo thang năm cái muỗng, dựa trên phản ứng của nhân vật trong truyện. Đây là cảm nhận của Kaku, không phải con số chính thức.

[pause] Và Kaku nói rõ trước: đây là quái vật giả tưởng. Ngoài đời, đừng bao giờ ăn nấm dại, côn trùng lạ hay động vật hoang dã chưa rõ nguồn gốc. Video này không phải hướng dẫn ăn uống.

[pause] Hồ sơ chia làm bốn nhóm: quái vật tầng nông, kẻ giả dạng, sinh vật kỳ lạ, và cuối cùng là con rồng.
```

### c02 · Bối cảnh: Dungeon Meshi là gì? / Bốn người trong bếp

Khoảng 121 giây · cảnh s11–s21 · 1570 ký tự

**Gemini**

```text
Dungeon Meshi là manga của Kui Ryoko, đăng trên tạp chí Harta từ năm 2014 tới 2023, gồm mười bốn tập. Anime do studio Trigger làm, phát năm 2024, và mùa hai đã được công bố.

<short pause> Câu chuyện theo Laios, một chiến binh mê quái vật tới mức kỳ quặc. Em gái anh, Falin, bị một con rồng đỏ nuốt chửng trong khi cứu cả nhóm thoát ra.

<short pause> Trong thế giới này, người chết trong hầm ngục có thể được hồi sinh bằng phép thuật, nếu thi thể còn nguyên vẹn. Nên nhóm phải xuống cứu Falin trước khi con rồng tiêu hóa xong.

<short pause> Không đủ tiền mua lương thực, Laios đề xuất một ý điên rồ: vừa đi vừa ăn quái vật. Cả nhóm phản đối, trừ chính anh.

<short pause> Rồi họ gặp một người lùn đã sống trong hầm ngục nhiều năm, chuyên nấu quái vật. Người đó tên Senshi, và ông trở thành đầu bếp của cả nhóm.

<short pause> <laugh> Kaku rất thích cách bộ truyện xem hầm ngục như một hệ sinh thái thật. Quái vật ăn gì, sống ở đâu, sinh sản thế nào, và tất nhiên, nấu thế nào cho ngon.

<short pause> Trước khi mở hồ sơ, hãy làm quen với bốn thực khách, vì mỗi người phản ứng với món quái vật một kiểu, và đó là nửa niềm vui của bộ truyện.

<short pause> Laios, trưởng nhóm, mê quái vật từ nhỏ. Với anh, được ăn quái vật là một giấc mơ. Anh thường là người háo hức nhất bên nồi.

<short pause> Marcille, pháp sư tộc elf, là người phản đối dữ nhất. Cô kêu la, từ chối, rồi cuối cùng vẫn ăn, và thường là người khen ngon đầu tiên.

<short pause> Chilchuck, thợ mở khóa tộc người nhỏ, là người thực tế nhất. Anh không quan tâm quái vật ngon hay không, chỉ quan tâm có an toàn và có tính công không.

<short pause> Và Senshi, người nấu, xem mỗi bữa ăn như một cách tôn trọng hầm ngục. Bốn người, bốn thái độ, và mỗi món ăn thử thách cả bốn.
```

**ElevenLabs**

```text
Dungeon Meshi là manga của Kui Ryoko, đăng trên tạp chí Harta từ năm 2014 tới 2023, gồm mười bốn tập. Anime do studio Trigger làm, phát năm 2024, và mùa hai đã được công bố.

[pause] Câu chuyện theo Laios, một chiến binh mê quái vật tới mức kỳ quặc. Em gái anh, Falin, bị một con rồng đỏ nuốt chửng trong khi cứu cả nhóm thoát ra.

[pause] Trong thế giới này, người chết trong hầm ngục có thể được hồi sinh bằng phép thuật, nếu thi thể còn nguyên vẹn. Nên nhóm phải xuống cứu Falin trước khi con rồng tiêu hóa xong.

[pause] Không đủ tiền mua lương thực, Laios đề xuất một ý điên rồ: vừa đi vừa ăn quái vật. Cả nhóm phản đối, trừ chính anh.

[pause] Rồi họ gặp một người lùn đã sống trong hầm ngục nhiều năm, chuyên nấu quái vật. Người đó tên Senshi, và ông trở thành đầu bếp của cả nhóm.

[pause] [chuckles] Kaku rất thích cách bộ truyện xem hầm ngục như một hệ sinh thái thật. Quái vật ăn gì, sống ở đâu, sinh sản thế nào, và tất nhiên, nấu thế nào cho ngon.

[pause] Trước khi mở hồ sơ, hãy làm quen với bốn thực khách, vì mỗi người phản ứng với món quái vật một kiểu, và đó là nửa niềm vui của bộ truyện.

[pause] Laios, trưởng nhóm, mê quái vật từ nhỏ. Với anh, được ăn quái vật là một giấc mơ. Anh thường là người háo hức nhất bên nồi.

[pause] Marcille, pháp sư tộc elf, là người phản đối dữ nhất. Cô kêu la, từ chối, rồi cuối cùng vẫn ăn, và thường là người khen ngon đầu tiên.

[pause] Chilchuck, thợ mở khóa tộc người nhỏ, là người thực tế nhất. Anh không quan tâm quái vật ngon hay không, chỉ quan tâm có an toàn và có tính công không.

[pause] Và Senshi, người nấu, xem mỗi bữa ăn như một cách tôn trọng hầm ngục. Bốn người, bốn thái độ, và mỗi món ăn thử thách cả bốn.
```

### c03 · Nhóm A: quái vật tầng nông

Khoảng 140 giây · cảnh s22–s33 · 1826 ký tự

**Gemini**

```text
Hồ sơ số một: Bọ cạp khổng lồ. Loại: côn trùng hầm ngục. Điểm mạnh: càng khỏe và đuôi độc. Điểm yếu: phần khớp mềm giữa các lớp vỏ.

<short pause> Hồ sơ số hai: Nấm biết đi. Loại: nấm có chân, di chuyển được. Điểm mạnh: bào tử. Điểm yếu: chậm, và chân dễ bị chặt.

<short pause> Senshi còn chỉ ra một điều: phần ngon nhất của nấm biết đi lại là phần chân, chỗ cơ bắp chắc nhất. Món đầu tiên đã nói rõ phong cách của bộ truyện: quái vật cũng là sinh vật có thịt, có cơ.

<short pause> Món ăn: lẩu bọ cạp và nấm biết đi, món đầu tiên trong truyện. Senshi luộc bọ cạp như luộc cua, và nhóm bất ngờ vì nó ngon. Kaku chấm bốn muỗng.

<short pause> Hồ sơ số ba: Slime. Loại: sinh vật không xương dạng keo. Điểm mạnh: bịt kín miệng mũi con mồi. Điểm yếu: dễ bị tách ra nếu biết chỗ.

<short pause> Món ăn: slime phơi khô. Senshi lấy phần cơ quan bên trong, phơi khô, dùng như một nguyên liệu cao cấp. Kaku chấm ba muỗng, vì nghe thì ghê nhưng hóa ra rất tinh tế.

<short pause> Một mẹo của Senshi mà Kaku rất thích: nếu không chắc một quái vật có ăn được không, hãy xem những sinh vật khác trong hầm ngục có ăn nó không. Thiên nhiên thường đã thử trước bạn.

<short pause> Hồ sơ số bốn: Basilisk. Loại: nửa gà trống, nửa rắn. Điểm mạnh: nọc độc và đuôi rắn. Điểm yếu: phần thân gà vẫn là gà.

<short pause> Món ăn: basilisk quay và trứng ốp la. Thịt gà mềm, phần đuôi rắn ngon như thịt trắng. Kaku chấm năm muỗng. Đây là món khiến cả nhóm bắt đầu tin vào Senshi.

<short pause> Hồ sơ số năm: Mandrake. Loại: cây có rễ hình người. Điểm mạnh: tiếng hét khi bị nhổ lên, có thể làm người nghe mất trí. Điểm yếu: nếu biết cách nhổ an toàn, nó chỉ là một củ rau.

<short pause> Trong Dungeon Meshi, Senshi có cách nhổ mandrake an toàn, và dùng củ của nó như một loại rau củ trong món trứng. Truyền thuyết đáng sợ, trong tay đầu bếp, thành nguyên liệu.

<short pause> Kaku thích mandrake vì đây là quái vật có gốc thật trong truyền thuyết châu Âu. Người xưa tin rằng ai nhổ mandrake và nghe tiếng hét của nó sẽ chết.
```

**ElevenLabs**

```text
Hồ sơ số một: Bọ cạp khổng lồ. Loại: côn trùng hầm ngục. Điểm mạnh: càng khỏe và đuôi độc. Điểm yếu: phần khớp mềm giữa các lớp vỏ.

[pause] Hồ sơ số hai: Nấm biết đi. Loại: nấm có chân, di chuyển được. Điểm mạnh: bào tử. Điểm yếu: chậm, và chân dễ bị chặt.

[pause] Senshi còn chỉ ra một điều: phần ngon nhất của nấm biết đi lại là phần chân, chỗ cơ bắp chắc nhất. Món đầu tiên đã nói rõ phong cách của bộ truyện: quái vật cũng là sinh vật có thịt, có cơ.

[pause] Món ăn: lẩu bọ cạp và nấm biết đi, món đầu tiên trong truyện. Senshi luộc bọ cạp như luộc cua, và nhóm bất ngờ vì nó ngon. Kaku chấm bốn muỗng.

[pause] Hồ sơ số ba: Slime. Loại: sinh vật không xương dạng keo. Điểm mạnh: bịt kín miệng mũi con mồi. Điểm yếu: dễ bị tách ra nếu biết chỗ.

[pause] Món ăn: slime phơi khô. Senshi lấy phần cơ quan bên trong, phơi khô, dùng như một nguyên liệu cao cấp. Kaku chấm ba muỗng, vì nghe thì ghê nhưng hóa ra rất tinh tế.

[pause] Một mẹo của Senshi mà Kaku rất thích: nếu không chắc một quái vật có ăn được không, hãy xem những sinh vật khác trong hầm ngục có ăn nó không. Thiên nhiên thường đã thử trước bạn.

[pause] Hồ sơ số bốn: Basilisk. Loại: nửa gà trống, nửa rắn. Điểm mạnh: nọc độc và đuôi rắn. Điểm yếu: phần thân gà vẫn là gà.

[pause] Món ăn: basilisk quay và trứng ốp la. Thịt gà mềm, phần đuôi rắn ngon như thịt trắng. Kaku chấm năm muỗng. Đây là món khiến cả nhóm bắt đầu tin vào Senshi.

[pause] Hồ sơ số năm: Mandrake. Loại: cây có rễ hình người. Điểm mạnh: tiếng hét khi bị nhổ lên, có thể làm người nghe mất trí. Điểm yếu: nếu biết cách nhổ an toàn, nó chỉ là một củ rau.

[pause] Trong Dungeon Meshi, Senshi có cách nhổ mandrake an toàn, và dùng củ của nó như một loại rau củ trong món trứng. Truyền thuyết đáng sợ, trong tay đầu bếp, thành nguyên liệu.

[pause] Kaku thích mandrake vì đây là quái vật có gốc thật trong truyền thuyết châu Âu. Người xưa tin rằng ai nhổ mandrake và nghe tiếng hét của nó sẽ chết.
```

### c04 · Nhóm B: kẻ giả dạng

Khoảng 115 giây · cảnh s34–s43 · 1491 ký tự

**Gemini**

```text
Nhóm thứ hai khiến Kaku thích nhất: những kẻ giả dạng. Nhìn một đằng, bên trong một nẻo.

<short pause> Hồ sơ số sáu: Giáp sống. Loại: một bộ giáp tự di chuyển, cầm kiếm tấn công. Điểm mạnh: cứng, và không có đầu để chém. Điểm yếu: những khe hở giữa các tấm giáp.

<short pause> Và đây là phát hiện tuyệt vời nhất của Laios: bên trong bộ giáp không có linh hồn nào. Chỉ có một đàn sinh vật thân mềm, giống trai hay hến, sống bám vào mặt trong của giáp và điều khiển nó như một cơ thể.

<short pause> Món ăn: giáp sống xào kiểu người lùn. Senshi nấu chúng như hải sản. Kaku chấm bốn muỗng, và thêm một điểm cho sự sáng tạo khoa học.

<short pause> Hồ sơ số bảy: Mimic, rương báu giả. Loại: sinh vật sống trong rương. Điểm mạnh: kẹp chặt tay kẻ tham lam mở rương. Điểm yếu: rời khỏi vỏ thì yếu ớt.

<short pause> Trong Dungeon Meshi, mimic giống một loài giáp xác, như tôm hay cua ẩn sĩ, sống trong rương như cua ẩn sĩ sống trong vỏ ốc. Món ăn: mimic luộc. Kaku chấm bốn muỗng.

<short pause> Hồ sơ số tám: Golem. Loại: người đá khổng lồ, bảo vệ một khu vực. Điểm mạnh: to, nặng, gần như không biết đau. Điểm yếu: có một điểm yếu trên thân.

<short pause> Và Senshi làm một việc không ai nghĩ tới: ông dùng lưng golem làm vườn rau. Đất trên lưng golem màu mỡ, lại được chính golem bảo vệ khỏi kẻ trộm.

<short pause> Có một chi tiết hài hước: khi cả nhóm cần đánh golem, Senshi lại lo cho vườn rau của mình hơn. Với ông, golem là đồng nghiệp, không phải kẻ thù.

<short pause> <laugh> Kaku thấy chi tiết golem là linh hồn của Dungeon Meshi. Quái vật không chỉ là kẻ thù hay thức ăn. Nó là một phần của hệ sinh thái mà con người có thể sống cùng.
```

**ElevenLabs**

```text
Nhóm thứ hai khiến Kaku thích nhất: những kẻ giả dạng. Nhìn một đằng, bên trong một nẻo.

[pause] Hồ sơ số sáu: Giáp sống. Loại: một bộ giáp tự di chuyển, cầm kiếm tấn công. Điểm mạnh: cứng, và không có đầu để chém. Điểm yếu: những khe hở giữa các tấm giáp.

[pause] Và đây là phát hiện tuyệt vời nhất của Laios: bên trong bộ giáp không có linh hồn nào. Chỉ có một đàn sinh vật thân mềm, giống trai hay hến, sống bám vào mặt trong của giáp và điều khiển nó như một cơ thể.

[pause] Món ăn: giáp sống xào kiểu người lùn. Senshi nấu chúng như hải sản. Kaku chấm bốn muỗng, và thêm một điểm cho sự sáng tạo khoa học.

[pause] Hồ sơ số bảy: Mimic, rương báu giả. Loại: sinh vật sống trong rương. Điểm mạnh: kẹp chặt tay kẻ tham lam mở rương. Điểm yếu: rời khỏi vỏ thì yếu ớt.

[pause] Trong Dungeon Meshi, mimic giống một loài giáp xác, như tôm hay cua ẩn sĩ, sống trong rương như cua ẩn sĩ sống trong vỏ ốc. Món ăn: mimic luộc. Kaku chấm bốn muỗng.

[pause] Hồ sơ số tám: Golem. Loại: người đá khổng lồ, bảo vệ một khu vực. Điểm mạnh: to, nặng, gần như không biết đau. Điểm yếu: có một điểm yếu trên thân.

[pause] Và Senshi làm một việc không ai nghĩ tới: ông dùng lưng golem làm vườn rau. Đất trên lưng golem màu mỡ, lại được chính golem bảo vệ khỏi kẻ trộm.

[pause] Có một chi tiết hài hước: khi cả nhóm cần đánh golem, Senshi lại lo cho vườn rau của mình hơn. Với ông, golem là đồng nghiệp, không phải kẻ thù.

[pause] [chuckles] Kaku thấy chi tiết golem là linh hồn của Dungeon Meshi. Quái vật không chỉ là kẻ thù hay thức ăn. Nó là một phần của hệ sinh thái mà con người có thể sống cùng.
```

### c05 · Nhóm C: sinh vật kỳ lạ

Khoảng 114 giây · cảnh s44–s53 · 1478 ký tự

**Gemini**

```text
Hồ sơ số chín: Hồn ma. Loại: linh hồn không thể chạm. Điểm mạnh: kéo nhiệt độ xuống rất thấp, làm con người lạnh cóng. Điểm yếu: nước thánh.

<short pause> Senshi không ăn được hồn ma. <short pause> Nhưng ông lợi dụng nó. Ông làm một loại nước thánh ngọt, rồi để hồn ma làm đông lạnh, tạo thành một món kem mà ông gọi là kem trừ tà.

<short pause> Chi tiết thú vị: Senshi coi việc trừ tà và làm kem là cùng một việc. Hồn ma được siêu thoát, cả nhóm có món tráng miệng. Không ai bị thiệt.

<short pause> Kaku chấm bốn muỗng, và cho thêm một huy chương cho món có tên hay nhất cả hồ sơ.

<short pause> Hồ sơ số mười: Bọ châu báu. Loại: côn trùng giả làm đồ trang sức. Điểm mạnh: lừa kẻ tham lam nhặt lên. Điểm yếu: không có nhiều sức tấn công.

<short pause> Kaku để ý: trong hầm ngục, những kẻ tham lam thường là người chết sớm nhất. Mimic, bọ châu báu, đều là cái bẫy dành cho người chỉ nhìn thấy tiền.

<short pause> Một bài học nho nhỏ của hầm ngục: không phải thứ gì lấp lánh cũng là báu vật. Và đôi khi, báu vật lại ngọt, vì Senshi dùng chúng làm nguyên liệu cho món kem.

<short pause> Hồ sơ số mười một: Vòng nấm tiên. Loại: một vòng nấm mọc tròn, nơi các sinh vật tí hon sống. Điểm mạnh: ai bước vào có thể bị hoán đổi chủng tộc. Điểm yếu: tránh bước vào là được.

<short pause> Kaku thấy chương vòng nấm là cách tác giả cho các nhân vật thử sống trong thân thể người khác. Và họ hiểu nhau hơn nhờ đó, dù chỉ trong một bữa ăn.

<short pause> Ở cuối mùa một, cả nhóm bị hoán đổi chủng tộc sau khi bước vào vòng nấm. Người lùn thành người cao, người cao thành người tí hon. Và Senshi, dĩ nhiên, vẫn nấu ăn, lần này là món bánh bao.
```

**ElevenLabs**

```text
Hồ sơ số chín: Hồn ma. Loại: linh hồn không thể chạm. Điểm mạnh: kéo nhiệt độ xuống rất thấp, làm con người lạnh cóng. Điểm yếu: nước thánh.

[pause] Senshi không ăn được hồn ma. [pause] Nhưng ông lợi dụng nó. Ông làm một loại nước thánh ngọt, rồi để hồn ma làm đông lạnh, tạo thành một món kem mà ông gọi là kem trừ tà.

[pause] Chi tiết thú vị: Senshi coi việc trừ tà và làm kem là cùng một việc. Hồn ma được siêu thoát, cả nhóm có món tráng miệng. Không ai bị thiệt.

[pause] Kaku chấm bốn muỗng, và cho thêm một huy chương cho món có tên hay nhất cả hồ sơ.

[pause] Hồ sơ số mười: Bọ châu báu. Loại: côn trùng giả làm đồ trang sức. Điểm mạnh: lừa kẻ tham lam nhặt lên. Điểm yếu: không có nhiều sức tấn công.

[pause] Kaku để ý: trong hầm ngục, những kẻ tham lam thường là người chết sớm nhất. Mimic, bọ châu báu, đều là cái bẫy dành cho người chỉ nhìn thấy tiền.

[pause] Một bài học nho nhỏ của hầm ngục: không phải thứ gì lấp lánh cũng là báu vật. Và đôi khi, báu vật lại ngọt, vì Senshi dùng chúng làm nguyên liệu cho món kem.

[pause] Hồ sơ số mười một: Vòng nấm tiên. Loại: một vòng nấm mọc tròn, nơi các sinh vật tí hon sống. Điểm mạnh: ai bước vào có thể bị hoán đổi chủng tộc. Điểm yếu: tránh bước vào là được.

[pause] Kaku thấy chương vòng nấm là cách tác giả cho các nhân vật thử sống trong thân thể người khác. Và họ hiểu nhau hơn nhờ đó, dù chỉ trong một bữa ăn.

[pause] Ở cuối mùa một, cả nhóm bị hoán đổi chủng tộc sau khi bước vào vòng nấm. Người lùn thành người cao, người cao thành người tí hon. Và Senshi, dĩ nhiên, vẫn nấu ăn, lần này là món bánh bao.
```

### c06 · Nhóm D: Rồng đỏ / Luật ẩm thực hầm ngục của Senshi

Khoảng 143 giây · cảnh s54–s67 · 1864 ký tự

**Gemini**

```text
Và hồ sơ cuối cùng, hồ sơ số mười hai: Rồng đỏ. Loại: rồng. Điểm mạnh: lửa, sức mạnh, và vảy gần như không thể xuyên thủng.

<short pause> Điểm yếu: như mọi sinh vật, rồng có phần cổ và vảy ngược. Laios, người mê quái vật, biết rõ cơ thể rồng hơn ai hết, và chính kiến thức đó giúp nhóm tìm ra cách đánh.

<short pause> Kaku không kể chi tiết trận đánh để bạn tự xem. <short pause> Nhưng nó là một trong những trận hay nhất của anime năm 2024, và nó thắng không phải bằng sức mạnh mà bằng hiểu biết.

<short pause> Và sau trận đánh là câu hỏi không thể tránh: ăn rồng thế nào? Senshi làm cả một bữa tiệc: thịt nướng, giăm bông, và nhiều món khác từ một con vật khổng lồ.

<short pause> Mùa một khép lại ở đây, với những câu hỏi còn bỏ ngỏ về Falin và bí mật sâu hơn của hầm ngục. Mùa hai sẽ trả lời, và Kaku hứa sẽ mở tiếp hồ sơ khi đó.

<short pause> Nhưng Kaku muốn nói rõ: bữa tiệc rồng không hoàn toàn vui vẻ. Vì cả nhóm biết rằng trong bụng rồng là Falin. Ăn và cứu, sống và chết, được đặt cạnh nhau một cách rất nặng nề.

<short pause> <laugh> Kaku thấy đây là lúc Dungeon Meshi cho thấy chiều sâu thật sự. Ăn không chỉ là để sống. Ăn là chấp nhận rằng mọi sự sống đều nối với nhau.

<short pause> Qua cả mùa một, Senshi dạy cả nhóm vài luật ăn uống rất giản dị. Kaku ghi lại năm luật.

<short pause> Luật một: ăn uống cân bằng. Dù ở hầm ngục, vẫn phải có rau, thịt, tinh bột. Đó là lý do ông trồng rau trên lưng golem.

<short pause> Luật hai: không lãng phí. Đã giết một sinh vật thì phải dùng hết những gì có thể dùng.

<short pause> Luật ba: tôn trọng hệ sinh thái. Nếu ăn quá nhiều một loài, cả hầm ngục sẽ mất cân bằng.

<short pause> Luật bốn: nấu cho đúng. Nhiều quái vật có độc nếu ăn sai cách. Senshi luôn biết phần nào ăn được, phần nào phải bỏ.

<short pause> Luật năm, luật Kaku thích nhất: ăn cùng nhau. Những bữa ăn chung là lúc nhóm hiểu nhau hơn, cãi nhau, làm hòa, và trở thành một đội thật sự.

<short pause> Kaku thêm luật thứ sáu của riêng mình, không có trong truyện: rửa nồi ngay sau khi ăn. Vì trong hầm ngục, mùi thức ăn là lời mời gọi cho con quái vật tiếp theo.
```

**ElevenLabs**

```text
Và hồ sơ cuối cùng, hồ sơ số mười hai: Rồng đỏ. Loại: rồng. Điểm mạnh: lửa, sức mạnh, và vảy gần như không thể xuyên thủng.

[pause] Điểm yếu: như mọi sinh vật, rồng có phần cổ và vảy ngược. Laios, người mê quái vật, biết rõ cơ thể rồng hơn ai hết, và chính kiến thức đó giúp nhóm tìm ra cách đánh.

[pause] Kaku không kể chi tiết trận đánh để bạn tự xem. [pause] Nhưng nó là một trong những trận hay nhất của anime năm 2024, và nó thắng không phải bằng sức mạnh mà bằng hiểu biết.

[pause] [curious] Và sau trận đánh là câu hỏi không thể tránh: ăn rồng thế nào? Senshi làm cả một bữa tiệc: thịt nướng, giăm bông, và nhiều món khác từ một con vật khổng lồ.

[pause] Mùa một khép lại ở đây, với những câu hỏi còn bỏ ngỏ về Falin và bí mật sâu hơn của hầm ngục. Mùa hai sẽ trả lời, và Kaku hứa sẽ mở tiếp hồ sơ khi đó.

[pause] Nhưng Kaku muốn nói rõ: bữa tiệc rồng không hoàn toàn vui vẻ. Vì cả nhóm biết rằng trong bụng rồng là Falin. Ăn và cứu, sống và chết, được đặt cạnh nhau một cách rất nặng nề.

[pause] [chuckles] Kaku thấy đây là lúc Dungeon Meshi cho thấy chiều sâu thật sự. Ăn không chỉ là để sống. Ăn là chấp nhận rằng mọi sự sống đều nối với nhau.

[pause] Qua cả mùa một, Senshi dạy cả nhóm vài luật ăn uống rất giản dị. Kaku ghi lại năm luật.

[pause] Luật một: ăn uống cân bằng. Dù ở hầm ngục, vẫn phải có rau, thịt, tinh bột. Đó là lý do ông trồng rau trên lưng golem.

[pause] Luật hai: không lãng phí. Đã giết một sinh vật thì phải dùng hết những gì có thể dùng.

[pause] Luật ba: tôn trọng hệ sinh thái. Nếu ăn quá nhiều một loài, cả hầm ngục sẽ mất cân bằng.

[pause] Luật bốn: nấu cho đúng. Nhiều quái vật có độc nếu ăn sai cách. Senshi luôn biết phần nào ăn được, phần nào phải bỏ.

[pause] Luật năm, luật Kaku thích nhất: ăn cùng nhau. Những bữa ăn chung là lúc nhóm hiểu nhau hơn, cãi nhau, làm hòa, và trở thành một đội thật sự.

[pause] Kaku thêm luật thứ sáu của riêng mình, không có trong truyện: rửa nồi ngay sau khi ăn. Vì trong hầm ngục, mùi thức ăn là lời mời gọi cho con quái vật tiếp theo.
```

### c07 · Quái vật và đời thật / Nếu bạn là đầu bếp hầm ngục / Mục lục hồ sơ / Góc nhìn của Kaku

Khoảng 140 giây · cảnh s68–s81 · 1824 ký tự

**Gemini**

```text
Nhiều quái vật trong Dungeon Meshi có gốc từ truyền thuyết châu Âu. Basilisk trong truyền thuyết là vua của loài rắn, được cho là có ánh mắt giết người.

<short pause> Nhưng Kui Ryoko làm một việc thú vị: bà lấy quái vật truyền thuyết rồi hỏi, nếu nó có thật thì cơ thể nó hoạt động thế nào, và thịt nó có vị gì?

<short pause> Giáp sống thành trai hến. Mimic thành cua ẩn sĩ. Đây là cách biến truyền thuyết thành sinh học giả tưởng rất đáng tin.

<short pause> Và Kaku nhắc lại một lần nữa: ngoài đời, nấm dại có thể gây chết người, và nhiều loài vật hoang dã mang mầm bệnh. Hãy để việc ăn quái vật ở lại trong truyện.

<short pause> Giờ tới trò chơi nhỏ. Bạn là đầu bếp của một nhóm phiêu lưu, và trước mặt bạn là ba con quái vật: một slime, một mimic, và một con nấm biết đi. Bạn chỉ được nấu một món.

<short pause> <laugh> Kaku chọn mimic, luộc với chút muối và thảo mộc, vì Kaku tin mọi thứ giống cua đều ngon. Và vì Kaku muốn trả thù những chiếc rương từng kẹp tay mình.

<short pause> Còn bạn? Bạn chọn con nào, nấu món gì, và đặt tên món là gì? Tên hay nhất sẽ được Kaku vẽ lên một thẻ hồ sơ đặc biệt.

<short pause> Gợi ý của Senshi mà Kaku rất thích: món ngon nhất không phải món cầu kỳ nhất, mà là món làm cả nhóm ngồi lại với nhau.

<short pause> Và đây là mục lục hồ sơ quái vật. Nhóm A, tầng nông: bọ cạp khổng lồ, nấm biết đi, slime, basilisk, mandrake.

<short pause> Nhóm B, kẻ giả dạng: giáp sống, mimic, golem. Nhóm C, sinh vật kỳ lạ: hồn ma, bọ châu báu, vòng nấm tiên. Và nhóm D: rồng đỏ.

<short pause> Giải món ngon nhất theo Kaku: đồng hạng năm muỗng, basilisk quay và tiệc rồng. Giải món sáng tạo nhất: giáp sống xào. Giải tên hay nhất: kem trừ tà.

<short pause> Còn bạn? Bạn muốn thử món nào nhất, và món nào bạn nhất quyết không ăn? Viết vào bình luận nhé.

<short pause> Kaku nghĩ Dungeon Meshi là một bộ truyện về sự tò mò. Laios nhìn quái vật không bằng sợ hãi, mà bằng câu hỏi: nó sống thế nào?

<short pause> Và khi bạn tò mò về một thứ, bạn bắt đầu hiểu nó, rồi tôn trọng nó. Kể cả khi thứ đó muốn ăn bạn.
```

**ElevenLabs**

```text
Nhiều quái vật trong Dungeon Meshi có gốc từ truyền thuyết châu Âu. Basilisk trong truyền thuyết là vua của loài rắn, được cho là có ánh mắt giết người.

[pause] [curious] Nhưng Kui Ryoko làm một việc thú vị: bà lấy quái vật truyền thuyết rồi hỏi, nếu nó có thật thì cơ thể nó hoạt động thế nào, và thịt nó có vị gì?

[pause] Giáp sống thành trai hến. Mimic thành cua ẩn sĩ. Đây là cách biến truyền thuyết thành sinh học giả tưởng rất đáng tin.

[pause] Và Kaku nhắc lại một lần nữa: ngoài đời, nấm dại có thể gây chết người, và nhiều loài vật hoang dã mang mầm bệnh. Hãy để việc ăn quái vật ở lại trong truyện.

[pause] Giờ tới trò chơi nhỏ. Bạn là đầu bếp của một nhóm phiêu lưu, và trước mặt bạn là ba con quái vật: một slime, một mimic, và một con nấm biết đi. Bạn chỉ được nấu một món.

[pause] [chuckles] Kaku chọn mimic, luộc với chút muối và thảo mộc, vì Kaku tin mọi thứ giống cua đều ngon. Và vì Kaku muốn trả thù những chiếc rương từng kẹp tay mình.

[pause] Còn bạn? Bạn chọn con nào, nấu món gì, và đặt tên món là gì? Tên hay nhất sẽ được Kaku vẽ lên một thẻ hồ sơ đặc biệt.

[pause] Gợi ý của Senshi mà Kaku rất thích: món ngon nhất không phải món cầu kỳ nhất, mà là món làm cả nhóm ngồi lại với nhau.

[pause] Và đây là mục lục hồ sơ quái vật. Nhóm A, tầng nông: bọ cạp khổng lồ, nấm biết đi, slime, basilisk, mandrake.

[pause] Nhóm B, kẻ giả dạng: giáp sống, mimic, golem. Nhóm C, sinh vật kỳ lạ: hồn ma, bọ châu báu, vòng nấm tiên. Và nhóm D: rồng đỏ.

[pause] Giải món ngon nhất theo Kaku: đồng hạng năm muỗng, basilisk quay và tiệc rồng. Giải món sáng tạo nhất: giáp sống xào. Giải tên hay nhất: kem trừ tà.

[pause] Còn bạn? Bạn muốn thử món nào nhất, và món nào bạn nhất quyết không ăn? Viết vào bình luận nhé.

[pause] Kaku nghĩ Dungeon Meshi là một bộ truyện về sự tò mò. Laios nhìn quái vật không bằng sợ hãi, mà bằng câu hỏi: nó sống thế nào?

[pause] Và khi bạn tò mò về một thứ, bạn bắt đầu hiểu nó, rồi tôn trọng nó. Kể cả khi thứ đó muốn ăn bạn.
```

### c08 · Kết

Khoảng 31 giây · cảnh s82–s84 · 402 ký tự

**Gemini**

```text
Dungeon Meshi dạy ta rằng mọi thứ trong hầm ngục đều nối với nhau, qua một thứ rất bình thường: bữa ăn.

<short pause> Video tiếp theo, Kaku phân tích một trong những trận đấu được tìm nhiều nhất của Naruto: Naruto đấu với Pain, từng hiệp một, và câu hỏi về vòng lặp hận thù.

<short pause> <laugh> Nếu hồ sơ này làm bạn đói bụng, Kaku xin lỗi. Hãy đăng ký kênh, rồi đi ăn một bữa thật ngon với người bạn thương. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Dungeon Meshi dạy ta rằng mọi thứ trong hầm ngục đều nối với nhau, qua một thứ rất bình thường: bữa ăn.

[pause] Video tiếp theo, Kaku phân tích một trong những trận đấu được tìm nhiều nhất của Naruto: Naruto đấu với Pain, từng hiệp một, và câu hỏi về vòng lặp hận thù.

[pause] [chuckles] Nếu hồ sơ này làm bạn đói bụng, Kaku xin lỗi. Hãy đăng ký kênh, rồi đi ăn một bữa thật ngon với người bạn thương. Kaku gấp sổ đây, hẹn gặp lại!
```
