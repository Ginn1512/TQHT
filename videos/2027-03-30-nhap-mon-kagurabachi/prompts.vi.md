# Bộ prompt · Kagurabachi: Nhập môn thế giới yêu đao trong 15 phút, trước khi anime ra mắt

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 8 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Video này gần như không có spoiler. Kaku chỉ nói tới tiền đề và vài chương đầu của Kagurabachi, đúng những gì…

```text
Wide 16:9 landscape cinematic frame. a closed notebook with a small green safe-to-read stamp on its cover resting on a wooden workbench, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Nếu bạn chưa đọc Kagurabachi, đây là mười lăm phút bạn cần. Một cậu con trai của thợ rèn kiếm. Một thanh kiếm…

```text
Wide 16:9 landscape cinematic frame. a sheathed katana resting on a blacksmith's anvil in a dark forge with embers glowing, dramatic close-up, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đây là bộ truyện từng bị cả internet đem ra làm trò đùa, trước khi chương một kịp ra mắt. Và rồi nó làm tất c…

```text
Wide 16:9 landscape cinematic frame. a wall of scrolling social media speech bubbles slowly fading into silence, symbolic wide shot, cool screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở cánh cửa vào thế giới Kagurabachi: thế giới trông ra sao, nhân vậ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pushing open a heavy wooden door with light spilling out, looking excited. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Kaku nhắc trước: đây là truyện hành động với nhiều cảnh đánh nhau. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiế…

```text
Wide 16:9 landscape cinematic frame. a katana blade reflecting a soft lantern light in a quiet dark room, extreme close-up, calm warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Hiện tượng Kagurabachi

Lời: Kagurabachi là manga của tác giả Takeru Hokazono, đăng trên tuần san Shonen Jump từ tháng chín năm 2023. Đây…

```text
Wide 16:9 landscape cinematic frame. a stack of weekly manga magazines on a newsstand counter with a single copy slightly pulled out, close-up, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Ngay khi truyện vừa ra mắt, cộng đồng mạng nước ngoài biến nó thành một trò đùa: người ta khen nó quá mức ở k…

```text
Wide 16:9 landscape cinematic frame. a crowd of tiny cartoon speech bubbles all shouting the same exclamation mark, humorous wide shot, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhưng trò đùa ấy kéo rất nhiều người tới đọc thật. Và họ ở lại. Nhiều người nói, đại ý, rằng họ tới để cười,…

```text
Wide 16:9 landscape cinematic frame. a reader sitting under a lamp, completely absorbed in a book late at night, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Năm 2024, Kagurabachi giành hạng nhất giải Next Manga Award ở hạng mục truyện in, với hơn một trăm nghìn điểm…

```text
Wide 16:9 landscape cinematic frame. a small golden trophy on a table beside a tally sheet with a very long column of marks, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và tháng tư năm 2027, anime Kagurabachi ra mắt, do studio Cypic thực hiện. Trước đó, hai mươi phút đầu của tậ…

```text
Wide 16:9 landscape cinematic frame. a cinema screen glowing in a dark theater with rows of silhouetted audience members, wide shot, blue projector light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ít bộ truyện nào đi từ một câu đùa trên mạng tới một bản anime chỉ trong khoảng ba năm rưỡi. Kagur…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny meme poster in one wing and a trophy in the other, surprised. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Thế giới: Nhật Bản hiện đại và thuật sư

Lời: Kagurabachi lấy bối cảnh Nhật Bản hiện đại. Có điện thoại, có xe hơi, có những con phố đêm đầy đèn neon.

```text
Wide 16:9 landscape cinematic frame. a rain-soaked modern Japanese alley at night with glowing neon signs and a vending machine, wide shot, moody neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhưng dưới lớp vỏ ấy là một thế giới ngầm. Có những thuật sư, những người dùng năng lực siêu nhiên. Có những…

```text
Wide 16:9 landscape cinematic frame. a shadowy back room with figures in suits gathered around a table under a single hanging bulb, medium shot, dim smoky light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Trong quá khứ của thế giới này có một cuộc chiến lớn, gọi là Chiến tranh Seitei. Cuộc chiến ấy kết thúc nhờ m…

```text
Wide 16:9 landscape cinematic frame. an old war painting on a folding screen showing distant armies and a few bright points of light on a battlefield, close-up, aged golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Có sáu thanh yêu đao, do một thợ rèn tên Rokuhira Kunishige tạo ra. Sáu người cầm sáu thanh kiếm ấy đã chấm d…

```text
Wide 16:9 landscape cinematic frame. six katanas resting on a long wooden rack in a dim shrine hall, each with a faint different glow, wide shot, solemn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Sau chiến tranh, sáu thanh kiếm bị cất giấu và canh giữ cẩn mật. Người thợ rèn, người tạo ra chúng, không hề…

```text
Wide 16:9 landscape cinematic frame. a heavy sealed wooden chest wrapped in ropes and paper charms in a dark storehouse, close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Chính phủ có một tổ chức thuật sư riêng, tên là Kamunabi, lo việc giữ trật tự trong thế giới phép thuật và bả…

```text
Wide 16:9 landscape cinematic frame. a formal building entrance at night with guards in dark uniforms standing beneath a simple emblem, wide shot, cold institutional light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Điều thú vị là thế giới phép thuật và thế giới bình thường sống sát cạnh nhau. Người thường có thể đi ngang q…

```text
Wide 16:9 landscape cinematic frame. ordinary pedestrians with umbrellas walking past a narrow alley where faint glowing sparks flicker, wide shot, rainy neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: thế giới này giống như một bộ phim yakuza pha với truyện kiếm hiệp. Kiếm và phép thuật, nhưng giữa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny fedora and holding a wooden practice sword under a neon sign. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Nhân vật chính: con trai người thợ rèn

Lời: Nhân vật chính là Rokuhira Chihiro, con trai của người thợ rèn huyền thoại. Cậu mơ trở thành thợ rèn kiếm giố…

```text
Wide 16:9 landscape cinematic frame. a teenager kneeling beside a forge carefully watching an older figure hammer glowing steel, medium shot, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Những ngày đầu của truyện rất ấm áp. Hai cha con làm việc, ăn cơm, trêu nhau. Người cha là một người vui tính…

```text
Wide 16:9 landscape cinematic frame. two bowls of rice and a small teapot on a low table in a cozy workshop kitchen, close-up, soft warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và trong nhà có những con cá vàng. Một chi tiết nhỏ, nhưng hãy nhớ nó, vì cá vàng sẽ quay lại theo một cách r…

```text
Wide 16:9 landscape cinematic frame. a round glass bowl with goldfish swimming slowly on a wooden windowsill, extreme close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Rồi một ngày, một nhóm thuật sư bí ẩn tấn công ngôi nhà. Người cha bị giết. Sáu thanh yêu đao bị cướp đi. Và…

```text
Wide 16:9 landscape cinematic frame. a workshop doorway with a broken sliding door and scattered tools on the floor under cold moonlight, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Nhóm thuật sư ấy có tên là Hishaku. Họ lấy yêu đao để làm gì, lúc đầu không ai biết.

```text
Wide 16:9 landscape cinematic frame. a single black ladle-shaped emblem drawn on an old paper talisman pinned to a wall, extreme close-up, eerie dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Vài năm sau, Chihiro trở lại với một thanh kiếm bên hông. Cậu ít nói, lạnh lùng, và chỉ có một mục tiêu: tìm…

```text
Wide 16:9 landscape cinematic frame. a lone young figure in a dark coat walking down a rainy street at night with a sheathed sword at their side, back view, wide shot, cold neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Người cha từng nói với Chihiro, đại ý, rằng một thợ rèn phải hiểu thanh kiếm của mình sẽ được dùng để làm gì.…

```text
Wide 16:9 landscape cinematic frame. an older blacksmith pointing at a blade while a teenager listens intently beside the forge, medium shot, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Chihiro không phải kiểu nhân vật chính hét to và cười lớn. Cậu im lặng, nhưng sự im lặng ấy cho ta…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting quietly beside a goldfish bowl, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Nghề rèn kiếm Nhật ngoài đời thật

Lời: Trước khi nói về yêu đao, Kaku kể một chút về nghề của cha Chihiro ngoài đời thật. Rèn kiếm Nhật là một nghề…

```text
Wide 16:9 landscape cinematic frame. a traditional Japanese forge interior with a charcoal fire, a hammer and tongs on a wooden stand, wide shot, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Nguyên liệu truyền thống là một loại thép gọi là tamahagane, luyện từ cát sắt trong một lò đất lớn. Người thợ…

```text
Wide 16:9 landscape cinematic frame. a glowing bar of steel being folded over on an anvil with sparks flying, extreme close-up, bright orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trước khi tôi, người thợ phủ lên lưỡi kiếm một lớp đất sét, dày ở sống và mỏng ở lưỡi. Nhờ vậy lưỡi kiếm cứng…

```text
Wide 16:9 landscape cinematic frame. a blade coated with uneven grey clay resting on a wooden board beside a water trough, close-up, warm workshop light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Ở Nhật hiện nay, thợ rèn kiếm phải có giấy phép, sau nhiều năm học việc dưới một thợ cả. Luật còn giới hạn mỗ…

```text
Wide 16:9 landscape cinematic frame. a calendar page with only two small sword icons marked on it, pinned above a workbench, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Giới hạn ấy nhằm giữ chất lượng thay vì số lượng. Mỗi thanh kiếm là nhiều tuần làm việc của một người.

```text
Wide 16:9 landscape cinematic frame. an old craftsman's hands carefully polishing a blade under a single lamp, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: đây chỉ là giới thiệu văn hóa, không phải hướng dẫn. Kaku để ý: biết điều này, bạn sẽ hiểu vì sao…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing respectfully in front of a small sword stand. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Yêu đao hoạt động thế nào?

Lời: Yêu đao không phải thanh kiếm bình thường. Mỗi thanh chứa một sức mạnh phép thuật, và chỉ trở nên đáng sợ tro…

```text
Wide 16:9 landscape cinematic frame. a katana blade with faint swirling patterns of light moving beneath the steel surface, extreme close-up, mystical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Sáu thanh yêu đao là vũ khí chiến tranh. Sức mạnh của chúng đủ để thay đổi số phận cả một đất nước. Vì vậy, a…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn map of a country with six small sword icons scattered across it and arrows between them, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Nhưng Chihiro không cầm một trong sáu thanh ấy. Cậu cầm thanh thứ bảy, tên là Enten, một thanh kiếm cha cậu r…

```text
Wide 16:9 landscape cinematic frame. a seventh katana resting alone on a separate stand, set apart from an empty six-slot rack, dramatic close-up, cold moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Khác với sáu thanh kia, Enten không được rèn để đánh trận. Nó được rèn để đối đầu với chính sáu thanh kiếm cũ…

```text
Wide 16:9 landscape cinematic frame. an old blacksmith's hands wrapping the hilt of a new sword by lamplight, extreme close-up, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Và sức mạnh của Enten mang hình dáng những con cá vàng. Đúng rồi: những con cá vàng trong nhà Chihiro.

```text
Wide 16:9 landscape cinematic frame. ghostly goldfish shapes swimming in the air around a drawn katana in a dark room, symbolic close-up, glowing orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kỹ thuật Kuro, tức cá vàng đen, phủ một lớp chất lỏng màu đen lên cánh tay và lưỡi kiếm, rồi tung ra những nh…

```text
Wide 16:9 landscape cinematic frame. a black liquid swirl shaped like a goldfish coiling around a blade and launching a long dark arc through the air, dynamic wide shot, dramatic night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kỹ thuật Nishiki, tức cá vàng ba màu, trở thành một lớp áo năng lượng quanh cơ thể, giúp Chihiro nhanh hơn và…

```text
Wide 16:9 landscape cinematic frame. a figure wrapped in a shimmering cloak of white, orange and black light shaped like flowing fins, dynamic close-up, vivid light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Còn kỹ thuật Aka, tức cá vàng đỏ, hấp thụ đòn đánh mà lưỡi kiếm chạm vào, rồi có thể dùng lại đòn ấy ở một mứ…

```text
Wide 16:9 landscape cinematic frame. a red goldfish shape swallowing a bolt of energy along a blade's edge, extreme close-up, glowing red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Ba kỹ thuật, ba cách dùng: Kuro để đánh xa, Nishiki để tăng tốc, Aka để phản đòn. Chihiro phải chọn đúng kỹ t…

```text
Wide 16:9 landscape cinematic frame. three goldfish icons in black, tri-color and red arranged like game pieces on a board, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: sức mạnh của Chihiro mang hình ảnh ký ức ấm áp nhất của cậu. Mỗi nhát kiếm trả thù lại được vẽ bằn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small goldfish bowl gently in both wings. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Kẻ thù và đồng minh

Lời: Kẻ thù chính là Hishaku, nhóm thuật sư đã cướp yêu đao. Họ đông, có tổ chức, và sẵn sàng hợp tác với cả thế g…

```text
Wide 16:9 landscape cinematic frame. a line of faceless figures in dark coats standing in the rain at the end of a long street, wide shot, ominous cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Sáu thanh yêu đao rơi vào tay những kẻ khác nhau. Nghĩa là mỗi lần Chihiro tìm lại một thanh, cậu phải đối mặ…

```text
Wide 16:9 landscape cinematic frame. six empty sword silhouettes drawn on a wanted poster wall with some crossed out, close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhưng Chihiro không đi một mình. Có một thuật sư là bạn cũ của cha cậu, người luôn đứng sau giúp đỡ, và thỉnh…

```text
Wide 16:9 landscape cinematic frame. an older figure with sunglasses leaning casually against a wall beside a young swordsman, medium shot, soft street light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Trên đường đi, Chihiro còn gặp những người cũng bị tổn thương bởi yêu đao, và dần có thêm những người bạn đồn…

```text
Wide 16:9 landscape cinematic frame. a small group of silhouettes sharing a meal around a low table in a hidden room, wide shot, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Và giữa hai phe còn có Kamunabi, tổ chức của chính phủ. Họ muốn thu hồi yêu đao, nhưng không phải lúc nào cũn…

```text
Wide 16:9 landscape cinematic frame. a line of uniformed figures watching from a rooftop as a lone swordsman walks below, wide shot, cold night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là câu chuyện trả thù, nhưng không phải câu chuyện cô độc. Chihiro càng đi xa, càng có thêm ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a small circle of stick figures holding hands in a notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Những biểu tượng cần để ý

Lời: Khi đọc hay xem Kagurabachi, hãy để ý vài hình ảnh lặp lại. Chúng giúp bạn đọc được cảm xúc mà nhân vật không…

```text
Wide 16:9 landscape cinematic frame. a notebook page with four small doodles, a goldfish, a hammer, a raindrop and a closed mouth, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Cá vàng: ký ức về ngôi nhà và người cha. Mỗi khi cá vàng xuất hiện, đó là lúc Chihiro chiến đấu bằng chính qu…

```text
Wide 16:9 landscape cinematic frame. a goldfish swimming alone in a dark space with a faint warm glow around it, symbolic close-up, soft orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Lò rèn và cái búa: di sản. Chihiro không chỉ là kiếm sĩ, cậu vẫn là người học nghề của cha.

```text
Wide 16:9 landscape cinematic frame. a small hammer hanging on a hook in an empty workshop with the forge fire still faintly glowing, close-up, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và sự im lặng: truyện thường để những khung hình không có lời thoại, ngay trước hoặc sau một nhát kiếm. Chính…

```text
Wide 16:9 landscape cinematic frame. a wide empty frame of a rainy street with a single figure standing still, no motion at all, cinematic wide shot, cold quiet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Vì sao nên xem?

Lời: Lý do một: phong cách như phim điện ảnh. Truyện dùng nhiều khung hình rộng, nhiều khoảng lặng, và những pha h…

```text
Wide 16:9 landscape cinematic frame. a film strip with wide cinematic frames showing a lone swordsman in different quiet poses, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Và các trận đấu thường là những trận đấu trí: năng lực nào cũng có điều kiện, và người thắng là người đọc đượ…

```text
Wide 16:9 landscape cinematic frame. a chess-like diagram of two sword icons with arrows and small condition notes, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Lý do hai: nhịp nhanh. Truyện không vòng vo. Chương một đã đưa bạn vào thẳng mạch truyện, và mỗi arc đều gọn…

```text
Wide 16:9 landscape cinematic frame. a stopwatch beside a short neat stack of manga volumes, close-up, crisp bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Lý do ba: một thế giới pha trộn độc đáo. Kiếm Nhật, phép thuật, yakuza, và những con phố hiện đại. Ít bộ truy…

```text
Wide 16:9 landscape cinematic frame. a split composition showing a katana, a glowing talisman, a neon street sign and a business suit arranged together on a table, close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Lý do bốn: một nhân vật chính có chiều sâu. Chihiro không nói nhiều, nhưng mỗi quyết định của cậu cho thấy cậ…

```text
Wide 16:9 landscape cinematic frame. a young swordsman kneeling to hand a small goldfish bowl to a frightened child in a ruined street, medium shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Lý do năm: câu chuyện về cha và con. Mỗi thanh kiếm là một phần di sản của người cha. Tìm lại chúng cũng là c…

```text
Wide 16:9 landscape cinematic frame. an old blacksmith's hammer resting beside a young swordsman's hand on a workbench, extreme close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Và lý do sáu: bạn có thể bắt kịp nhanh. Vì truyện bắt đầu từ năm 2023, số chương chưa quá nhiều như những bộ…

```text
Wide 16:9 landscape cinematic frame. a short neat bookshelf row next to a very long overflowing bookshelf row, humorous wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Ba câu hỏi lớn của truyện · **Kaku** (đính kèm ảnh mẫu)

Lời: Không cần spoiler, Kaku vẫn có thể cho bạn ba câu hỏi lớn để mang theo khi xem.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up three fingers with a magnifying glass in the other wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Câu hỏi một: Hishaku muốn sáu thanh yêu đao để làm gì? Chúng là vũ khí chiến tranh, vậy ai đó đang chuẩn bị c…

```text
Wide 16:9 landscape cinematic frame. six sword silhouettes drawn in a circle around a question mark on a map, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Câu hỏi hai: chuyện gì thật sự đã xảy ra trong Chiến tranh Seitei, và vì sao người thợ rèn lại hối hận về chí…

```text
Wide 16:9 landscape cinematic frame. a faded war scroll partially burned at the edges with a smith's hammer resting on it, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Câu hỏi ba: Enten, thanh kiếm thứ bảy, còn giấu điều gì mà người cha chưa kịp nói với con mình?

```text
Wide 16:9 landscape cinematic frame. a single sword on a stand with a folded unopened letter tucked beneath its hilt, extreme close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Nên chuẩn bị tinh thần điều gì?

Lời: Kagurabachi có nhiều cảnh chiến đấu và có những cái chết. Truyện không nhẹ nhàng như một số bộ shonen vui vẻ…

```text
Wide 16:9 landscape cinematic frame. a single fallen katana lying on a wet street under a flickering streetlight, close-up, somber cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nhân vật chính ít nói, nên nếu bạn thích kiểu nhân vật hài hước, ồn ào, bạn cần vài chương để quen với Chihir…

```text
Wide 16:9 landscape cinematic frame. a quiet swordsman sitting apart from a loudly laughing group at a table, medium shot, warm and cool contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Thế giới được tiết lộ từ từ. Nhiều câu hỏi về Chiến tranh Seitei và mục đích của Hishaku sẽ chưa có lời đáp t…

```text
Wide 16:9 landscape cinematic frame. an old map with several regions left blank and marked with question marks, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: nếu bạn chịu được một chút u tối, phần thưởng là một câu chuyện có trái tim rất ấm.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small lantern in a dark corridor, smiling reassuringly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Nếu bạn thích những bộ này

Lời: Nếu bạn thích Kimetsu no Yaiba, bạn sẽ thấy quen: một cậu bé mất gia đình, cầm kiếm lên đường, và vẫn giữ lòn…

```text
Wide 16:9 landscape cinematic frame. a pair of katanas crossed gently over a family photo frame on a wooden shelf, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nếu bạn thích Jujutsu Kaisen, bạn sẽ thấy quen với thế giới thuật sư ẩn sau thành phố hiện đại, và những trận…

```text
Wide 16:9 landscape cinematic frame. a modern city skyline at night with faint glowing sigils hidden among the buildings, wide shot, eerie blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và nếu bạn thích phim hành động kiểu điện ảnh, với những nhân vật ít lời và ánh mắt nói thay, Kagurabachi sẽ…

```text
Wide 16:9 landscape cinematic frame. a single silhouette standing in a long empty corridor lit by one overhead light, cinematic wide shot, dramatic contrast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu bạn thích những bộ phim kiếm hiệp cổ về người con lên đường báo thù cho cha, bạn cũng sẽ thấy một mạch cả…

```text
Wide 16:9 landscape cinematic frame. an old wuxia-style film poster aesthetic of a lone swordsman on a misty mountain path, close-up, faded warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nhưng Kagurabachi không phải bản sao. Hình ảnh cá vàng, câu chuyện của người thợ rèn, và không khí yakuza là…

```text
Wide 16:9 landscape cinematic frame. a goldfish bowl placed on a blacksmith's anvil under a neon glow, symbolic close-up, mixed warm and cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Từ vựng cần nhớ

Lời: Trước khi xem, đây là năm từ bạn sẽ gặp liên tục. Một: yêu đao, những thanh kiếm có phép do cha Chihiro rèn.

```text
Wide 16:9 landscape cinematic frame. a small vocabulary card with a sword icon and a handwritten label, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Hai: Enten, thanh kiếm thứ bảy mà Chihiro mang theo, với sức mạnh hình cá vàng.

```text
Wide 16:9 landscape cinematic frame. a vocabulary card with a goldfish icon beside a sword, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Ba: Hishaku, nhóm thuật sư đã cướp sáu thanh yêu đao. Bốn: Kamunabi, tổ chức thuật sư của chính phủ.

```text
Wide 16:9 landscape cinematic frame. two vocabulary cards side by side, one with a dark ladle emblem and one with a formal badge, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Năm: Chiến tranh Seitei, cuộc chiến trong quá khứ mà sáu thanh yêu đao đã chấm dứt. Nhớ năm từ này, bạn sẽ th…

```text
Wide 16:9 landscape cinematic frame. a fifth vocabulary card with a faded battlefield icon, the full set of five fanned out on a desk, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Lộ trình xem cho người mới

Lời: Lộ trình của Kaku. Cách một: đợi anime tháng tư năm 2027, xem từ tập một. Đây là cách nhẹ nhàng nhất.

```text
Wide 16:9 landscape cinematic frame. a calendar page for April with the first day circled and a small sword doodle beside it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Cách hai: đọc manga từ chương một, trên các nền tảng phát hành chính thức. Bạn sẽ đi trước anime và hiểu thế…

```text
Wide 16:9 landscape cinematic frame. a phone screen and a printed volume side by side on a desk, both opened to a first page with no visible artwork, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Cách ba, cách Kaku thích nhất: đọc vài chương đầu để quen thế giới, rồi dừng lại và xem anime, để những cảnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a bookmark in one wing and a TV remote in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Mẹo nhỏ của Kaku: đừng tra cứu tên nhân vật trên mạng trước khi xem. Kagurabachi có những bất ngờ mà bạn nên…

```text
Wide 16:9 landscape cinematic frame. a phone lying face down on a table beside an unopened book, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và dù chọn cách nào, hãy ủng hộ bản chính thức. Đó là cách để tác giả tiếp tục vẽ.

```text
Wide 16:9 landscape cinematic frame. a small hand placing a coin into a jar labeled with a pen and brush icon, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Một cậu con trai thợ rèn, một thanh kiếm thứ bảy, và những con cá vàng bơi trong không khí. Kagurabachi là câ…

```text
Wide 16:9 landscape cinematic frame. a goldfish bowl on a windowsill at dawn beside a sheathed sword, close-up, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Nếu bạn muốn Kaku làm video sâu hơn về từng thanh yêu đao sau khi anime ra mắt, hãy bình luận để Kaku biết th…

```text
Wide 16:9 landscape cinematic frame. six small sword sketches pinned on a corkboard with one circled in red, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tiếp theo, Kaku đổi sang một bí ẩn cung đình: Dược sư tự sự, và thân thế thật của Jinshi. Một video lý…

```text
Wide 16:9 landscape cinematic frame. an ornate palace corridor with hanging lanterns and a single folded letter on the floor, wide shot, warm mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này mở được cánh cửa cho bạn, hãy đăng ký kênh. Và nếu nhà bạn có nuôi cá vàng, hôm nay hãy cho chú…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sprinkling fish food into a small goldfish bowl, waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hiện tượng Kagurabachi

Khoảng 131 giây · cảnh s01–s11 · 1701 ký tự

**Gemini**

```text
Video này gần như không có spoiler. Kaku chỉ nói tới tiền đề và vài chương đầu của Kagurabachi, đúng những gì anime tháng tư sẽ kể. Bạn có thể xem thoải mái.

<short pause> Nếu bạn chưa đọc Kagurabachi, đây là mười lăm phút bạn cần. Một cậu con trai của thợ rèn kiếm. Một thanh kiếm có phép. Và một cuộc truy lùng những kẻ đã lấy đi tất cả của cậu.

<short pause> Đây là bộ truyện từng bị cả internet đem ra làm trò đùa, trước khi chương một kịp ra mắt. Và rồi nó làm tất cả những người đùa phải im lặng.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở cánh cửa vào thế giới Kagurabachi: thế giới trông ra sao, nhân vật chính là ai, yêu đao hoạt động thế nào, và vì sao bạn nên xem. Cuối video là lộ trình xem cho người mới.

<short pause> Kaku nhắc trước: đây là truyện hành động với nhiều cảnh đánh nhau. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiết bạo lực.

<short pause> Kagurabachi là manga của tác giả Takeru Hokazono, đăng trên tuần san Shonen Jump từ tháng chín năm 2023. Đây là bộ truyện dài kỳ đầu tiên của ông.

<short pause> Ngay khi truyện vừa ra mắt, cộng đồng mạng nước ngoài biến nó thành một trò đùa: người ta khen nó quá mức ở khắp nơi, như một câu nói đùa lặp đi lặp lại.

<short pause> Nhưng trò đùa ấy kéo rất nhiều người tới đọc thật. Và họ ở lại. Nhiều người nói, đại ý, rằng họ tới để cười, nhưng ở lại vì truyện hay thật.

<short pause> Năm 2024, Kagurabachi giành hạng nhất giải Next Manga Award ở hạng mục truyện in, với hơn một trăm nghìn điểm bình chọn.

<short pause> Và tháng tư năm 2027, anime Kagurabachi ra mắt, do studio Cypic thực hiện. Trước đó, hai mươi phút đầu của tập một đã được chiếu trong một chuyến lưu diễn vòng quanh thế giới.

<short pause> Kaku để ý: ít bộ truyện nào đi từ một câu đùa trên mạng tới một bản anime chỉ trong khoảng ba năm rưỡi. Kagurabachi làm được, vì nó có thứ để giữ chân người đọc.
```

**ElevenLabs**

```text
Video này gần như không có spoiler. Kaku chỉ nói tới tiền đề và vài chương đầu của Kagurabachi, đúng những gì anime tháng tư sẽ kể. Bạn có thể xem thoải mái.

[pause] Nếu bạn chưa đọc Kagurabachi, đây là mười lăm phút bạn cần. Một cậu con trai của thợ rèn kiếm. Một thanh kiếm có phép. Và một cuộc truy lùng những kẻ đã lấy đi tất cả của cậu.

[pause] Đây là bộ truyện từng bị cả internet đem ra làm trò đùa, trước khi chương một kịp ra mắt. Và rồi nó làm tất cả những người đùa phải im lặng.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở cánh cửa vào thế giới Kagurabachi: thế giới trông ra sao, nhân vật chính là ai, yêu đao hoạt động thế nào, và vì sao bạn nên xem. Cuối video là lộ trình xem cho người mới.

[pause] Kaku nhắc trước: đây là truyện hành động với nhiều cảnh đánh nhau. Kaku sẽ kể nhẹ nhàng, không đi vào chi tiết bạo lực.

[pause] Kagurabachi là manga của tác giả Takeru Hokazono, đăng trên tuần san Shonen Jump từ tháng chín năm 2023. Đây là bộ truyện dài kỳ đầu tiên của ông.

[pause] Ngay khi truyện vừa ra mắt, cộng đồng mạng nước ngoài biến nó thành một trò đùa: người ta khen nó quá mức ở khắp nơi, như một câu nói đùa lặp đi lặp lại.

[pause] Nhưng trò đùa ấy kéo rất nhiều người tới đọc thật. Và họ ở lại. Nhiều người nói, đại ý, rằng họ tới để cười, nhưng ở lại vì truyện hay thật.

[pause] Năm 2024, Kagurabachi giành hạng nhất giải Next Manga Award ở hạng mục truyện in, với hơn một trăm nghìn điểm bình chọn.

[pause] Và tháng tư năm 2027, anime Kagurabachi ra mắt, do studio Cypic thực hiện. Trước đó, hai mươi phút đầu của tập một đã được chiếu trong một chuyến lưu diễn vòng quanh thế giới.

[pause] Kaku để ý: ít bộ truyện nào đi từ một câu đùa trên mạng tới một bản anime chỉ trong khoảng ba năm rưỡi. Kagurabachi làm được, vì nó có thứ để giữ chân người đọc.
```

### c02 · Thế giới: Nhật Bản hiện đại và thuật sư

Khoảng 84 giây · cảnh s12–s19 · 1087 ký tự

**Gemini**

```text
Kagurabachi lấy bối cảnh Nhật Bản hiện đại. Có điện thoại, có xe hơi, có những con phố đêm đầy đèn neon.

<short pause> Nhưng dưới lớp vỏ ấy là một thế giới ngầm. Có những thuật sư, những người dùng năng lực siêu nhiên. Có những băng đảng yakuza sẵn sàng mua bán bất cứ thứ gì.

<short pause> Trong quá khứ của thế giới này có một cuộc chiến lớn, gọi là Chiến tranh Seitei. Cuộc chiến ấy kết thúc nhờ một thứ vũ khí đặc biệt: yêu đao.

<short pause> Có sáu thanh yêu đao, do một thợ rèn tên Rokuhira Kunishige tạo ra. Sáu người cầm sáu thanh kiếm ấy đã chấm dứt chiến tranh.

<short pause> Sau chiến tranh, sáu thanh kiếm bị cất giấu và canh giữ cẩn mật. Người thợ rèn, người tạo ra chúng, không hề tự hào về điều đó.

<short pause> Chính phủ có một tổ chức thuật sư riêng, tên là Kamunabi, lo việc giữ trật tự trong thế giới phép thuật và bảo vệ những bí mật như yêu đao.

<short pause> Điều thú vị là thế giới phép thuật và thế giới bình thường sống sát cạnh nhau. Người thường có thể đi ngang qua một trận chiến mà không hiểu chuyện gì đang xảy ra.

<short pause> <laugh> Kaku để ý: thế giới này giống như một bộ phim yakuza pha với truyện kiếm hiệp. Kiếm và phép thuật, nhưng giữa những tòa nhà bê tông.
```

**ElevenLabs**

```text
Kagurabachi lấy bối cảnh Nhật Bản hiện đại. Có điện thoại, có xe hơi, có những con phố đêm đầy đèn neon.

[pause] Nhưng dưới lớp vỏ ấy là một thế giới ngầm. Có những thuật sư, những người dùng năng lực siêu nhiên. Có những băng đảng yakuza sẵn sàng mua bán bất cứ thứ gì.

[pause] Trong quá khứ của thế giới này có một cuộc chiến lớn, gọi là Chiến tranh Seitei. Cuộc chiến ấy kết thúc nhờ một thứ vũ khí đặc biệt: yêu đao.

[pause] Có sáu thanh yêu đao, do một thợ rèn tên Rokuhira Kunishige tạo ra. Sáu người cầm sáu thanh kiếm ấy đã chấm dứt chiến tranh.

[pause] Sau chiến tranh, sáu thanh kiếm bị cất giấu và canh giữ cẩn mật. Người thợ rèn, người tạo ra chúng, không hề tự hào về điều đó.

[pause] Chính phủ có một tổ chức thuật sư riêng, tên là Kamunabi, lo việc giữ trật tự trong thế giới phép thuật và bảo vệ những bí mật như yêu đao.

[pause] Điều thú vị là thế giới phép thuật và thế giới bình thường sống sát cạnh nhau. Người thường có thể đi ngang qua một trận chiến mà không hiểu chuyện gì đang xảy ra.

[pause] [chuckles] Kaku để ý: thế giới này giống như một bộ phim yakuza pha với truyện kiếm hiệp. Kiếm và phép thuật, nhưng giữa những tòa nhà bê tông.
```

### c03 · Nhân vật chính: con trai người thợ rèn / Nghề rèn kiếm Nhật ngoài đời thật

Khoảng 153 giây · cảnh s20–s33 · 1994 ký tự

**Gemini**

```text
Nhân vật chính là Rokuhira Chihiro, con trai của người thợ rèn huyền thoại. Cậu mơ trở thành thợ rèn kiếm giống cha.

<short pause> Những ngày đầu của truyện rất ấm áp. Hai cha con làm việc, ăn cơm, trêu nhau. Người cha là một người vui tính, hay đùa, và yêu con.

<short pause> Và trong nhà có những con cá vàng. Một chi tiết nhỏ, nhưng hãy nhớ nó, vì cá vàng sẽ quay lại theo một cách rất đặc biệt.

<short pause> Rồi một ngày, một nhóm thuật sư bí ẩn tấn công ngôi nhà. Người cha bị giết. Sáu thanh yêu đao bị cướp đi. Và cuộc sống êm đềm của Chihiro vỡ tan.

<short pause> Nhóm thuật sư ấy có tên là Hishaku. Họ lấy yêu đao để làm gì, lúc đầu không ai biết.

<short pause> Vài năm sau, Chihiro trở lại với một thanh kiếm bên hông. Cậu ít nói, lạnh lùng, và chỉ có một mục tiêu: tìm lại sáu thanh yêu đao, và tìm ra những kẻ đã giết cha mình.

<short pause> Người cha từng nói với Chihiro, đại ý, rằng một thợ rèn phải hiểu thanh kiếm của mình sẽ được dùng để làm gì. Câu nói ấy theo Chihiro suốt hành trình.

<short pause> <laugh> Kaku để ý: Chihiro không phải kiểu nhân vật chính hét to và cười lớn. Cậu im lặng, nhưng sự im lặng ấy cho ta biết cậu đã mất nhiều thế nào.

<short pause> Trước khi nói về yêu đao, Kaku kể một chút về nghề của cha Chihiro ngoài đời thật. Rèn kiếm Nhật là một nghề thủ công có từ hàng trăm năm, và tới nay vẫn còn người làm.

<short pause> Nguyên liệu truyền thống là một loại thép gọi là tamahagane, luyện từ cát sắt trong một lò đất lớn. Người thợ gấp và đập thép nhiều lần để loại bớt tạp chất.

<short pause> Trước khi tôi, người thợ phủ lên lưỡi kiếm một lớp đất sét, dày ở sống và mỏng ở lưỡi. Nhờ vậy lưỡi kiếm cứng, còn sống kiếm dẻo, và một đường vân gọi là hamon hiện ra.

<short pause> Ở Nhật hiện nay, thợ rèn kiếm phải có giấy phép, sau nhiều năm học việc dưới một thợ cả. Luật còn giới hạn mỗi thợ chỉ được làm khoảng hai thanh kiếm dài mỗi tháng.

<short pause> Giới hạn ấy nhằm giữ chất lượng thay vì số lượng. Mỗi thanh kiếm là nhiều tuần làm việc của một người.

<short pause> Kaku nhắc: đây chỉ là giới thiệu văn hóa, không phải hướng dẫn. Kaku để ý: biết điều này, bạn sẽ hiểu vì sao trong truyện, mỗi thanh kiếm của người cha đều mang cả tâm hồn của ông.
```

**ElevenLabs**

```text
Nhân vật chính là Rokuhira Chihiro, con trai của người thợ rèn huyền thoại. Cậu mơ trở thành thợ rèn kiếm giống cha.

[pause] Những ngày đầu của truyện rất ấm áp. Hai cha con làm việc, ăn cơm, trêu nhau. Người cha là một người vui tính, hay đùa, và yêu con.

[pause] Và trong nhà có những con cá vàng. Một chi tiết nhỏ, nhưng hãy nhớ nó, vì cá vàng sẽ quay lại theo một cách rất đặc biệt.

[pause] Rồi một ngày, một nhóm thuật sư bí ẩn tấn công ngôi nhà. Người cha bị giết. Sáu thanh yêu đao bị cướp đi. Và cuộc sống êm đềm của Chihiro vỡ tan.

[pause] Nhóm thuật sư ấy có tên là Hishaku. Họ lấy yêu đao để làm gì, lúc đầu không ai biết.

[pause] Vài năm sau, Chihiro trở lại với một thanh kiếm bên hông. Cậu ít nói, lạnh lùng, và chỉ có một mục tiêu: tìm lại sáu thanh yêu đao, và tìm ra những kẻ đã giết cha mình.

[pause] Người cha từng nói với Chihiro, đại ý, rằng một thợ rèn phải hiểu thanh kiếm của mình sẽ được dùng để làm gì. Câu nói ấy theo Chihiro suốt hành trình.

[pause] [chuckles] Kaku để ý: Chihiro không phải kiểu nhân vật chính hét to và cười lớn. Cậu im lặng, nhưng sự im lặng ấy cho ta biết cậu đã mất nhiều thế nào.

[pause] Trước khi nói về yêu đao, Kaku kể một chút về nghề của cha Chihiro ngoài đời thật. Rèn kiếm Nhật là một nghề thủ công có từ hàng trăm năm, và tới nay vẫn còn người làm.

[pause] Nguyên liệu truyền thống là một loại thép gọi là tamahagane, luyện từ cát sắt trong một lò đất lớn. Người thợ gấp và đập thép nhiều lần để loại bớt tạp chất.

[pause] Trước khi tôi, người thợ phủ lên lưỡi kiếm một lớp đất sét, dày ở sống và mỏng ở lưỡi. Nhờ vậy lưỡi kiếm cứng, còn sống kiếm dẻo, và một đường vân gọi là hamon hiện ra.

[pause] Ở Nhật hiện nay, thợ rèn kiếm phải có giấy phép, sau nhiều năm học việc dưới một thợ cả. Luật còn giới hạn mỗi thợ chỉ được làm khoảng hai thanh kiếm dài mỗi tháng.

[pause] Giới hạn ấy nhằm giữ chất lượng thay vì số lượng. Mỗi thanh kiếm là nhiều tuần làm việc của một người.

[pause] Kaku nhắc: đây chỉ là giới thiệu văn hóa, không phải hướng dẫn. Kaku để ý: biết điều này, bạn sẽ hiểu vì sao trong truyện, mỗi thanh kiếm của người cha đều mang cả tâm hồn của ông.
```

### c04 · Yêu đao hoạt động thế nào?

Khoảng 108 giây · cảnh s34–s43 · 1399 ký tự

**Gemini**

```text
Yêu đao không phải thanh kiếm bình thường. Mỗi thanh chứa một sức mạnh phép thuật, và chỉ trở nên đáng sợ trong tay một người có thể dùng nó.

<short pause> Sáu thanh yêu đao là vũ khí chiến tranh. Sức mạnh của chúng đủ để thay đổi số phận cả một đất nước. Vì vậy, ai giữ chúng thì người đó nắm quyền lực rất lớn.

<short pause> Nhưng Chihiro không cầm một trong sáu thanh ấy. Cậu cầm thanh thứ bảy, tên là Enten, một thanh kiếm cha cậu rèn sau chiến tranh.

<short pause> Khác với sáu thanh kia, Enten không được rèn để đánh trận. Nó được rèn để đối đầu với chính sáu thanh kiếm cũ, để người thợ rèn đối mặt với quá khứ của mình.

<short pause> Và sức mạnh của Enten mang hình dáng những con cá vàng. Đúng rồi: những con cá vàng trong nhà Chihiro.

<short pause> Kỹ thuật Kuro, tức cá vàng đen, phủ một lớp chất lỏng màu đen lên cánh tay và lưỡi kiếm, rồi tung ra những nhát chém bay xa, kéo dài tầm đánh của thanh kiếm.

<short pause> Kỹ thuật Nishiki, tức cá vàng ba màu, trở thành một lớp áo năng lượng quanh cơ thể, giúp Chihiro nhanh hơn và nhanh nhẹn hơn rất nhiều.

<short pause> Còn kỹ thuật Aka, tức cá vàng đỏ, hấp thụ đòn đánh mà lưỡi kiếm chạm vào, rồi có thể dùng lại đòn ấy ở một mức độ nhất định.

<short pause> Ba kỹ thuật, ba cách dùng: Kuro để đánh xa, Nishiki để tăng tốc, Aka để phản đòn. Chihiro phải chọn đúng kỹ thuật cho từng tình huống, như chọn quân cờ.

<short pause> <laugh> Kaku để ý: sức mạnh của Chihiro mang hình ảnh ký ức ấm áp nhất của cậu. Mỗi nhát kiếm trả thù lại được vẽ bằng những con cá vàng trong ngôi nhà cũ.
```

**ElevenLabs**

```text
Yêu đao không phải thanh kiếm bình thường. Mỗi thanh chứa một sức mạnh phép thuật, và chỉ trở nên đáng sợ trong tay một người có thể dùng nó.

[pause] Sáu thanh yêu đao là vũ khí chiến tranh. Sức mạnh của chúng đủ để thay đổi số phận cả một đất nước. Vì vậy, ai giữ chúng thì người đó nắm quyền lực rất lớn.

[pause] Nhưng Chihiro không cầm một trong sáu thanh ấy. Cậu cầm thanh thứ bảy, tên là Enten, một thanh kiếm cha cậu rèn sau chiến tranh.

[pause] Khác với sáu thanh kia, Enten không được rèn để đánh trận. Nó được rèn để đối đầu với chính sáu thanh kiếm cũ, để người thợ rèn đối mặt với quá khứ của mình.

[pause] Và sức mạnh của Enten mang hình dáng những con cá vàng. Đúng rồi: những con cá vàng trong nhà Chihiro.

[pause] Kỹ thuật Kuro, tức cá vàng đen, phủ một lớp chất lỏng màu đen lên cánh tay và lưỡi kiếm, rồi tung ra những nhát chém bay xa, kéo dài tầm đánh của thanh kiếm.

[pause] Kỹ thuật Nishiki, tức cá vàng ba màu, trở thành một lớp áo năng lượng quanh cơ thể, giúp Chihiro nhanh hơn và nhanh nhẹn hơn rất nhiều.

[pause] Còn kỹ thuật Aka, tức cá vàng đỏ, hấp thụ đòn đánh mà lưỡi kiếm chạm vào, rồi có thể dùng lại đòn ấy ở một mức độ nhất định.

[pause] Ba kỹ thuật, ba cách dùng: Kuro để đánh xa, Nishiki để tăng tốc, Aka để phản đòn. Chihiro phải chọn đúng kỹ thuật cho từng tình huống, như chọn quân cờ.

[pause] [chuckles] Kaku để ý: sức mạnh của Chihiro mang hình ảnh ký ức ấm áp nhất của cậu. Mỗi nhát kiếm trả thù lại được vẽ bằng những con cá vàng trong ngôi nhà cũ.
```

### c05 · Kẻ thù và đồng minh / Những biểu tượng cần để ý

Khoảng 99 giây · cảnh s44–s53 · 1292 ký tự

**Gemini**

```text
Kẻ thù chính là Hishaku, nhóm thuật sư đã cướp yêu đao. Họ đông, có tổ chức, và sẵn sàng hợp tác với cả thế giới ngầm để đạt mục đích.

<short pause> Sáu thanh yêu đao rơi vào tay những kẻ khác nhau. Nghĩa là mỗi lần Chihiro tìm lại một thanh, cậu phải đối mặt với một người đang cầm nó.

<short pause> Nhưng Chihiro không đi một mình. Có một thuật sư là bạn cũ của cha cậu, người luôn đứng sau giúp đỡ, và thỉnh thoảng làm không khí bớt nặng nề bằng những câu đùa.

<short pause> Trên đường đi, Chihiro còn gặp những người cũng bị tổn thương bởi yêu đao, và dần có thêm những người bạn đồng hành.

<short pause> Và giữa hai phe còn có Kamunabi, tổ chức của chính phủ. Họ muốn thu hồi yêu đao, nhưng không phải lúc nào cũng đứng cùng phía với Chihiro.

<short pause> <laugh> Kaku để ý: đây là câu chuyện trả thù, nhưng không phải câu chuyện cô độc. Chihiro càng đi xa, càng có thêm người để bảo vệ.

<short pause> Khi đọc hay xem Kagurabachi, hãy để ý vài hình ảnh lặp lại. Chúng giúp bạn đọc được cảm xúc mà nhân vật không nói ra.

<short pause> Cá vàng: ký ức về ngôi nhà và người cha. Mỗi khi cá vàng xuất hiện, đó là lúc Chihiro chiến đấu bằng chính quá khứ của mình.

<short pause> Lò rèn và cái búa: di sản. Chihiro không chỉ là kiếm sĩ, cậu vẫn là người học nghề của cha.

<short pause> Và sự im lặng: truyện thường để những khung hình không có lời thoại, ngay trước hoặc sau một nhát kiếm. Chính khoảng lặng ấy khiến hành động nặng hơn.
```

**ElevenLabs**

```text
Kẻ thù chính là Hishaku, nhóm thuật sư đã cướp yêu đao. Họ đông, có tổ chức, và sẵn sàng hợp tác với cả thế giới ngầm để đạt mục đích.

[pause] Sáu thanh yêu đao rơi vào tay những kẻ khác nhau. Nghĩa là mỗi lần Chihiro tìm lại một thanh, cậu phải đối mặt với một người đang cầm nó.

[pause] Nhưng Chihiro không đi một mình. Có một thuật sư là bạn cũ của cha cậu, người luôn đứng sau giúp đỡ, và thỉnh thoảng làm không khí bớt nặng nề bằng những câu đùa.

[pause] Trên đường đi, Chihiro còn gặp những người cũng bị tổn thương bởi yêu đao, và dần có thêm những người bạn đồng hành.

[pause] Và giữa hai phe còn có Kamunabi, tổ chức của chính phủ. Họ muốn thu hồi yêu đao, nhưng không phải lúc nào cũng đứng cùng phía với Chihiro.

[pause] [chuckles] Kaku để ý: đây là câu chuyện trả thù, nhưng không phải câu chuyện cô độc. Chihiro càng đi xa, càng có thêm người để bảo vệ.

[pause] Khi đọc hay xem Kagurabachi, hãy để ý vài hình ảnh lặp lại. Chúng giúp bạn đọc được cảm xúc mà nhân vật không nói ra.

[pause] Cá vàng: ký ức về ngôi nhà và người cha. Mỗi khi cá vàng xuất hiện, đó là lúc Chihiro chiến đấu bằng chính quá khứ của mình.

[pause] Lò rèn và cái búa: di sản. Chihiro không chỉ là kiếm sĩ, cậu vẫn là người học nghề của cha.

[pause] Và sự im lặng: truyện thường để những khung hình không có lời thoại, ngay trước hoặc sau một nhát kiếm. Chính khoảng lặng ấy khiến hành động nặng hơn.
```

### c06 · Vì sao nên xem? / Ba câu hỏi lớn của truyện / Nên chuẩn bị tinh thần điều gì?

Khoảng 145 giây · cảnh s54–s68 · 1881 ký tự

**Gemini**

```text
Lý do một: phong cách như phim điện ảnh. Truyện dùng nhiều khung hình rộng, nhiều khoảng lặng, và những pha hành động được dựng như cảnh quay chậm.

<short pause> Và các trận đấu thường là những trận đấu trí: năng lực nào cũng có điều kiện, và người thắng là người đọc được điều kiện của đối phương trước.

<short pause> Lý do hai: nhịp nhanh. Truyện không vòng vo. Chương một đã đưa bạn vào thẳng mạch truyện, và mỗi arc đều gọn gàng.

<short pause> Lý do ba: một thế giới pha trộn độc đáo. Kiếm Nhật, phép thuật, yakuza, và những con phố hiện đại. Ít bộ truyện nào đặt tất cả những thứ đó cạnh nhau.

<short pause> Lý do bốn: một nhân vật chính có chiều sâu. Chihiro không nói nhiều, nhưng mỗi quyết định của cậu cho thấy cậu vẫn là cậu con trai hiền lành ngày xưa.

<short pause> Lý do năm: câu chuyện về cha và con. Mỗi thanh kiếm là một phần di sản của người cha. Tìm lại chúng cũng là cách Chihiro hiểu cha mình hơn.

<short pause> Và lý do sáu: bạn có thể bắt kịp nhanh. Vì truyện bắt đầu từ năm 2023, số chương chưa quá nhiều như những bộ truyện dài hàng chục năm.

<short pause> <laugh> Không cần spoiler, Kaku vẫn có thể cho bạn ba câu hỏi lớn để mang theo khi xem.

<short pause> Câu hỏi một: Hishaku muốn sáu thanh yêu đao để làm gì? Chúng là vũ khí chiến tranh, vậy ai đó đang chuẩn bị cho một cuộc chiến mới?

<short pause> Câu hỏi hai: chuyện gì thật sự đã xảy ra trong Chiến tranh Seitei, và vì sao người thợ rèn lại hối hận về chính những thanh kiếm đã chấm dứt chiến tranh?

<short pause> Câu hỏi ba: Enten, thanh kiếm thứ bảy, còn giấu điều gì mà người cha chưa kịp nói với con mình?

<short pause> Kagurabachi có nhiều cảnh chiến đấu và có những cái chết. Truyện không nhẹ nhàng như một số bộ shonen vui vẻ khác.

<short pause> Nhân vật chính ít nói, nên nếu bạn thích kiểu nhân vật hài hước, ồn ào, bạn cần vài chương để quen với Chihiro.

<short pause> Thế giới được tiết lộ từ từ. Nhiều câu hỏi về Chiến tranh Seitei và mục đích của Hishaku sẽ chưa có lời đáp trong mùa anime đầu.

<short pause> Kaku để ý: nếu bạn chịu được một chút u tối, phần thưởng là một câu chuyện có trái tim rất ấm.
```

**ElevenLabs**

```text
Lý do một: phong cách như phim điện ảnh. Truyện dùng nhiều khung hình rộng, nhiều khoảng lặng, và những pha hành động được dựng như cảnh quay chậm.

[pause] Và các trận đấu thường là những trận đấu trí: năng lực nào cũng có điều kiện, và người thắng là người đọc được điều kiện của đối phương trước.

[pause] Lý do hai: nhịp nhanh. Truyện không vòng vo. Chương một đã đưa bạn vào thẳng mạch truyện, và mỗi arc đều gọn gàng.

[pause] Lý do ba: một thế giới pha trộn độc đáo. Kiếm Nhật, phép thuật, yakuza, và những con phố hiện đại. Ít bộ truyện nào đặt tất cả những thứ đó cạnh nhau.

[pause] Lý do bốn: một nhân vật chính có chiều sâu. Chihiro không nói nhiều, nhưng mỗi quyết định của cậu cho thấy cậu vẫn là cậu con trai hiền lành ngày xưa.

[pause] Lý do năm: câu chuyện về cha và con. Mỗi thanh kiếm là một phần di sản của người cha. Tìm lại chúng cũng là cách Chihiro hiểu cha mình hơn.

[pause] Và lý do sáu: bạn có thể bắt kịp nhanh. Vì truyện bắt đầu từ năm 2023, số chương chưa quá nhiều như những bộ truyện dài hàng chục năm.

[pause] [chuckles] Không cần spoiler, Kaku vẫn có thể cho bạn ba câu hỏi lớn để mang theo khi xem.

[pause] [curious] Câu hỏi một: Hishaku muốn sáu thanh yêu đao để làm gì? Chúng là vũ khí chiến tranh, vậy ai đó đang chuẩn bị cho một cuộc chiến mới?

[pause] Câu hỏi hai: chuyện gì thật sự đã xảy ra trong Chiến tranh Seitei, và vì sao người thợ rèn lại hối hận về chính những thanh kiếm đã chấm dứt chiến tranh?

[pause] Câu hỏi ba: Enten, thanh kiếm thứ bảy, còn giấu điều gì mà người cha chưa kịp nói với con mình?

[pause] Kagurabachi có nhiều cảnh chiến đấu và có những cái chết. Truyện không nhẹ nhàng như một số bộ shonen vui vẻ khác.

[pause] Nhân vật chính ít nói, nên nếu bạn thích kiểu nhân vật hài hước, ồn ào, bạn cần vài chương để quen với Chihiro.

[pause] Thế giới được tiết lộ từ từ. Nhiều câu hỏi về Chiến tranh Seitei và mục đích của Hishaku sẽ chưa có lời đáp trong mùa anime đầu.

[pause] Kaku để ý: nếu bạn chịu được một chút u tối, phần thưởng là một câu chuyện có trái tim rất ấm.
```

### c07 · Nếu bạn thích những bộ này / Từ vựng cần nhớ / Lộ trình xem cho người mới

Khoảng 127 giây · cảnh s69–s82 · 1657 ký tự

**Gemini**

```text
Nếu bạn thích Kimetsu no Yaiba, bạn sẽ thấy quen: một cậu bé mất gia đình, cầm kiếm lên đường, và vẫn giữ lòng tốt.

<short pause> Nếu bạn thích Jujutsu Kaisen, bạn sẽ thấy quen với thế giới thuật sư ẩn sau thành phố hiện đại, và những trận đấu dựa trên luật của năng lực.

<short pause> Và nếu bạn thích phim hành động kiểu điện ảnh, với những nhân vật ít lời và ánh mắt nói thay, Kagurabachi sẽ rất hợp với bạn.

<short pause> Nếu bạn thích những bộ phim kiếm hiệp cổ về người con lên đường báo thù cho cha, bạn cũng sẽ thấy một mạch cảm xúc rất quen thuộc.

<short pause> Nhưng Kagurabachi không phải bản sao. Hình ảnh cá vàng, câu chuyện của người thợ rèn, và không khí yakuza là những thứ chỉ bộ này có.

<short pause> Trước khi xem, đây là năm từ bạn sẽ gặp liên tục. Một: yêu đao, những thanh kiếm có phép do cha Chihiro rèn.

<short pause> Hai: Enten, thanh kiếm thứ bảy mà Chihiro mang theo, với sức mạnh hình cá vàng.

<short pause> Ba: Hishaku, nhóm thuật sư đã cướp sáu thanh yêu đao. Bốn: Kamunabi, tổ chức thuật sư của chính phủ.

<short pause> Năm: Chiến tranh Seitei, cuộc chiến trong quá khứ mà sáu thanh yêu đao đã chấm dứt. Nhớ năm từ này, bạn sẽ theo kịp truyện ngay từ tập đầu.

<short pause> Lộ trình của Kaku. Cách một: đợi anime tháng tư năm 2027, xem từ tập một. Đây là cách nhẹ nhàng nhất.

<short pause> Cách hai: đọc manga từ chương một, trên các nền tảng phát hành chính thức. Bạn sẽ đi trước anime và hiểu thế giới sâu hơn.

<short pause> <laugh> Cách ba, cách Kaku thích nhất: đọc vài chương đầu để quen thế giới, rồi dừng lại và xem anime, để những cảnh hành động đầu tiên được sống lại bằng hình ảnh động.

<short pause> Mẹo nhỏ của Kaku: đừng tra cứu tên nhân vật trên mạng trước khi xem. Kagurabachi có những bất ngờ mà bạn nên tự mình gặp.

<short pause> Và dù chọn cách nào, hãy ủng hộ bản chính thức. Đó là cách để tác giả tiếp tục vẽ.
```

**ElevenLabs**

```text
Nếu bạn thích Kimetsu no Yaiba, bạn sẽ thấy quen: một cậu bé mất gia đình, cầm kiếm lên đường, và vẫn giữ lòng tốt.

[pause] Nếu bạn thích Jujutsu Kaisen, bạn sẽ thấy quen với thế giới thuật sư ẩn sau thành phố hiện đại, và những trận đấu dựa trên luật của năng lực.

[pause] Và nếu bạn thích phim hành động kiểu điện ảnh, với những nhân vật ít lời và ánh mắt nói thay, Kagurabachi sẽ rất hợp với bạn.

[pause] Nếu bạn thích những bộ phim kiếm hiệp cổ về người con lên đường báo thù cho cha, bạn cũng sẽ thấy một mạch cảm xúc rất quen thuộc.

[pause] Nhưng Kagurabachi không phải bản sao. Hình ảnh cá vàng, câu chuyện của người thợ rèn, và không khí yakuza là những thứ chỉ bộ này có.

[pause] Trước khi xem, đây là năm từ bạn sẽ gặp liên tục. Một: yêu đao, những thanh kiếm có phép do cha Chihiro rèn.

[pause] Hai: Enten, thanh kiếm thứ bảy mà Chihiro mang theo, với sức mạnh hình cá vàng.

[pause] Ba: Hishaku, nhóm thuật sư đã cướp sáu thanh yêu đao. Bốn: Kamunabi, tổ chức thuật sư của chính phủ.

[pause] Năm: Chiến tranh Seitei, cuộc chiến trong quá khứ mà sáu thanh yêu đao đã chấm dứt. Nhớ năm từ này, bạn sẽ theo kịp truyện ngay từ tập đầu.

[pause] Lộ trình của Kaku. Cách một: đợi anime tháng tư năm 2027, xem từ tập một. Đây là cách nhẹ nhàng nhất.

[pause] Cách hai: đọc manga từ chương một, trên các nền tảng phát hành chính thức. Bạn sẽ đi trước anime và hiểu thế giới sâu hơn.

[pause] [chuckles] Cách ba, cách Kaku thích nhất: đọc vài chương đầu để quen thế giới, rồi dừng lại và xem anime, để những cảnh hành động đầu tiên được sống lại bằng hình ảnh động.

[pause] Mẹo nhỏ của Kaku: đừng tra cứu tên nhân vật trên mạng trước khi xem. Kagurabachi có những bất ngờ mà bạn nên tự mình gặp.

[pause] Và dù chọn cách nào, hãy ủng hộ bản chính thức. Đó là cách để tác giả tiếp tục vẽ.
```

### c08 · Kết

Khoảng 48 giây · cảnh s83–s86 · 618 ký tự

**Gemini**

```text
Một cậu con trai thợ rèn, một thanh kiếm thứ bảy, và những con cá vàng bơi trong không khí. Kagurabachi là câu chuyện trả thù, nhưng thứ đọng lại lâu nhất lại là tình yêu của một người cha.

<short pause> Nếu bạn muốn Kaku làm video sâu hơn về từng thanh yêu đao sau khi anime ra mắt, hãy bình luận để Kaku biết thanh kiếm bạn tò mò nhất.

<short pause> Video tiếp theo, Kaku đổi sang một bí ẩn cung đình: Dược sư tự sự, và thân thế thật của Jinshi. Một video lý thuyết, có gắn nhãn rõ ràng.

<short pause> Nếu video này mở được cánh cửa cho bạn, hãy đăng ký kênh. Và nếu nhà bạn có nuôi cá vàng, hôm nay hãy cho chúng ăn thêm một chút. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Một cậu con trai thợ rèn, một thanh kiếm thứ bảy, và những con cá vàng bơi trong không khí. Kagurabachi là câu chuyện trả thù, nhưng thứ đọng lại lâu nhất lại là tình yêu của một người cha.

[pause] Nếu bạn muốn Kaku làm video sâu hơn về từng thanh yêu đao sau khi anime ra mắt, hãy bình luận để Kaku biết thanh kiếm bạn tò mò nhất.

[pause] Video tiếp theo, Kaku đổi sang một bí ẩn cung đình: Dược sư tự sự, và thân thế thật của Jinshi. Một video lý thuyết, có gắn nhãn rõ ràng.

[pause] Nếu video này mở được cánh cửa cho bạn, hãy đăng ký kênh. Và nếu nhà bạn có nuôi cá vàng, hôm nay hãy cho chúng ăn thêm một chút. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
