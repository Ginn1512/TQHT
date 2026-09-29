# Bộ prompt · Attack on Titan: Dòng thời gian 2.000 năm, từ Ymir tới Cuộc dậm nát

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 78 ảnh, 7 đoạn đọc, khoảng 14.9 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (78 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này đi qua toàn bộ Attack on Titan, từ khởi đầu hai nghìn năm trước tới tận phần kết.…

```text
Wide 16:9 landscape cinematic frame. a very long closed scroll tied with a red cord lying on a stone floor beside a spoiler card, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Năm 845 theo lịch trong truyện, một người khổng lồ cao hơn cả bức tường năm mươi mét xuất hiện, và đá thủng c…

```text
Wide 16:9 landscape cinematic frame. a massive wall with a gaping hole in its gate, dust and debris rising into an orange sky, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng câu chuyện không bắt đầu từ năm 845. Nó bắt đầu từ khoảng hai nghìn năm trước, với một cô gái nô lệ chạ…

```text
Wide 16:9 landscape cinematic frame. a lone small figure running barefoot through an ancient dark forest, wide shot, cold misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Câu hỏi hôm nay: điều gì đã xảy ra trong hai nghìn năm đó? Vì sao có những bức tường, vì sao có người khổng l…

```text
Wide 16:9 landscape cinematic frame. a long timeline scroll partially unrolled with ink marks spaced far apart, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku trải dòng thời gian hai nghìn năm của Attack on Titan. Mỗi mốc có mứ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling an extremely long scroll that stretches off the edge of the table. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Anime do WIT Studio rồi MAPPA thực hi…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a small model of a tall stone wall on a shelf, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Cách đọc dòng thời gian

Lời: Trước khi đi, một lưu ý quan trọng. Những năm như 845 hay 854 là lịch dùng trong những bức tường. Còn khoảng…

```text
Wide 16:9 landscape cinematic frame. two different calendars pinned side by side on a wall, one with year numbers and one with a large ancient symbol, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Một lưu ý nữa: phần lớn lịch sử trong truyện được kể lại bởi những người có lý do để bóp méo nó. Người Marley…

```text
Wide 16:9 landscape cinematic frame. two history books with different covers telling the same story, one with bright heroic imagery and one with dark imagery, close-up, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Và vì truyện có một năng lực liên quan tới ký ức và thời gian, có những mốc mà ngay cả nhân vật cũng không ch…

```text
Wide 16:9 landscape cinematic frame. a tangled thread with knots at various points, laid across an old map, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · Khoảng 2.000 năm trước: Ymir

Lời: Khoảng hai nghìn năm trước, trong vương quốc Eldia của vua Fritz, có một cô gái nô lệ tên Ymir. Cô bị đổ tội…

```text
Wide 16:9 landscape cinematic frame. a group of hunters with torches and dogs chasing a small figure through a dark forest at night, wide shot, ominous firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Chạy trốn trong rừng, Ymir ngã vào hốc một cái cây cổ thụ khổng lồ. Ở đó, cô chạm vào một thứ mà truyện gọi l…

```text
Wide 16:9 landscape cinematic frame. the hollow of an enormous ancient tree with a strange glowing presence deep inside, dramatic close-up, eerie green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Đây là mốc số không của cả câu chuyện. Truyện không nói rõ cái cây là gì, hay thứ bên trong nó từ đâu tới. Ka…

```text
Wide 16:9 landscape cinematic frame. a question mark carved into the bark of an ancient tree beside a faint glowing crack, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Cô trở thành người khổng lồ đầu tiên.

```text
Wide 16:9 landscape cinematic frame. a gigantic silhouette rising slowly out of a forest, trees bending around it, wide shot, awe-inspiring dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nhưng thay vì được tự do, Ymir tiếp tục phục vụ vua Fritz. Cô xây cầu, mở đường, và giúp Eldia chinh phục nhữ…

```text
Wide 16:9 landscape cinematic frame. a giant silhouette carrying enormous stones to build a bridge over a river while tiny soldiers watch, wide shot, warm hazy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Ymir sống khoảng mười ba năm sau khi có sức mạnh. Cô chết khi đỡ một ngọn giáo nhắm vào nhà vua. Mười ba năm,…

```text
Wide 16:9 landscape cinematic frame. a single spear lying on a stone throne-room floor beside a fallen crown, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: truyện cho thấy Ymir không chỉ là nạn nhân của nhà vua, mà còn là tù nhân của chính tình cảm trung…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small broken chain in its wings and looking at it sadly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Chín người khổng lồ

Lời: Sau khi Ymir chết, sức mạnh của cô được chia cho ba người con gái: Maria, Rose và Sina. Sức mạnh cứ thế truyề…

```text
Wide 16:9 landscape cinematic frame. three small candles lit from one larger candle, their flames splitting into nine smaller flames, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Mỗi người khổng lồ có năng lực riêng: người khổng lồ Đại hình, Thiết giáp, Nữ, Hàm, Xe, Quái thú, Chiến chùy,…

```text
Wide 16:9 landscape cinematic frame. a row of nine distinct tall silhouettes of different shapes standing on a ridge against a dramatic sky, wide shot, epic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Và mọi người thừa hưởng sức mạnh đều chịu lời nguyền của Ymir: chỉ sống thêm mười ba năm.

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand marked in thirteen sections, close-up, cold somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Tên ba người con gái, Maria, Rose, Sina, về sau được dùng để đặt tên cho ba bức tường. Một chi tiết nhỏ cho t…

```text
Wide 16:9 landscape cinematic frame. three concentric stone walls drawn on an old map, each labeled with an elegant hand-lettered name, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Gần 1.700 năm: Đế quốc Eldia

Lời: Trong khoảng một nghìn bảy trăm năm tiếp theo, Đế quốc Eldia dùng sức mạnh người khổng lồ để thống trị thế gi…

```text
Wide 16:9 landscape cinematic frame. a vast ancient empire map with a single dominant color spreading across continents, parchment close-up, dramatic red ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Theo lời kể của người Marley, Eldia đã gây ra vô số tội ác với các dân tộc khác. Theo lời kể của một số người…

```text
Wide 16:9 landscape cinematic frame. a scale with two scrolls of different colors on each side, slightly unbalanced, close-up, dim dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Và mọi người khổng lồ của Eldia đều có chung một điểm yếu: chỉ người mang dòng máu hoàng gia mới dùng được to…

```text
Wide 16:9 landscape cinematic frame. a crown resting on a velvet cushion with a single drop of red ink beside it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Trong lòng đế quốc, chín gia tộc nắm giữ chín người khổng lồ cũng tranh giành quyền lực với nhau. Đế quốc mạn…

```text
Wide 16:9 landscape cinematic frame. nine noble crests painted on a crumbling palace wall with cracks spreading between them, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Năm 743: Đại chiến người khổng lồ và những bức tường

Lời: Khoảng năm 743 theo lịch tường, vị vua thứ một trăm bốn mươi lăm của Eldia là Karl Fritz. Ông ghê sợ lịch sử…

```text
Wide 16:9 landscape cinematic frame. a lonely king's silhouette standing at a tall palace window looking at a war-torn city, back view, wide shot, melancholy dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Ông bí mật liên kết với gia tộc Tybur để chấm dứt đế quốc. Người Marley giành lại quyền lực, và câu chuyện đư…

```text
Wide 16:9 landscape cinematic frame. a heroic statue in a public square with a small hidden figure behind its pedestal whispering to another, wide shot, deceptive golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Karl Fritz đưa một phần người Eldia tới đảo Paradis. Ông dùng hàng triệu người khổng lồ Đại hình để xây ba bứ…

```text
Wide 16:9 landscape cinematic frame. three massive concentric stone walls under construction on an island seen from above, colossal figures standing inside the wall's structure, aerial wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Rồi ông dùng sức mạnh người khổng lồ Thủy tổ để xóa ký ức của người dân trong tường. Họ tin rằng thế giới bên…

```text
Wide 16:9 landscape cinematic frame. a crowd of people with blank expressions looking up at a glowing sky as faint memories drift away like smoke, symbolic wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Ông còn tạo ra một lời thề từ bỏ chiến tranh, gắn vào sức mạnh Thủy tổ: người kế thừa dòng máu hoàng gia sẽ b…

```text
Wide 16:9 landscape cinematic frame. an ancient oath scroll sealed with wax and a small crown symbol, close-up, cold solemn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Kaku thấy đây là một trong những quyết định gây tranh cãi nhất truyện: một vị vua chọn giam dân tộc mình tron…

```text
Wide 16:9 landscape cinematic frame. a vast walled island seen from the sea at dusk with warships silhouetted on the horizon, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · 100 năm trong tường

Lời: Trong một trăm năm tiếp theo, người dân trong tường sống yên bình, nhưng không biết gì về thế giới bên ngoài.…

```text
Wide 16:9 landscape cinematic frame. a quiet town street inside a massive wall with people going about daily life, the wall towering in the background, wide shot, soft calm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Ở Marley, người Eldia bị dồn vào khu cách ly, phải đeo băng tay để phân biệt. Những đứa trẻ Eldia được huấn l…

```text
Wide 16:9 landscape cinematic frame. a fenced district with plain grey buildings and a single child's armband lying on the ground, wide shot, cold oppressive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Trong khu cách ly, có một bác sĩ tên Grisha Yeager, người tham gia phong trào phục quốc Eldia. Về sau, ông tr…

```text
Wide 16:9 landscape cinematic frame. a doctor's leather bag and a small key on a chain lying on a wooden table, close-up, warm secretive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trước đó, Grisha từng có một gia đình khác ở Marley, và một người con trai lớn tên Zeke. Hai anh em cùng cha,…

```text
Wide 16:9 landscape cinematic frame. two old family photographs placed side by side on a desk, one from a foreign city and one from a small walled town, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Grisha lập gia đình trong tường, có con trai là Eren. Và ông để lại một tầng hầm khóa kín, cùng chiếc chìa kh…

```text
Wide 16:9 landscape cinematic frame. a closed wooden basement door with a heavy lock in a quiet house, close-up, dim mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Những người không bị xóa ký ức

Lời: Có một chi tiết thú vị: không phải ai trong tường cũng bị xóa ký ức. Gia tộc Ackerman, những người từng làm c…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing unaffected in a crowd of people with blank expressions, as faint smoke of memories drifts past them, symbolic wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Vì vậy họ bị nhà vua trong tường săn đuổi và đàn áp. Levi và Mikasa, hai chiến binh mạnh nhất phe loài người…

```text
Wide 16:9 landscape cinematic frame. two blades crossed on a worn wooden table beside a family name carved into the wood, close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Mẹ của Mikasa còn thuộc một dòng họ đến từ phương Đông, liên quan tới đất nước Hizuru. Chi tiết nhỏ này về sa…

```text
Wide 16:9 landscape cinematic frame. a small embroidered family crest on a piece of cloth tucked inside a wooden box, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ngay trong những bức tường, lịch sử cũng không đồng nhất. Có những người mang ký ức mà người khác…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small candle in a dark room where other figures stand in shadow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Bên kia biển: Marley và thế giới

Lời: Trong khi người trong tường sống yên bình, Marley dùng những người khổng lồ Eldia để đánh chiếm các nước khác…

```text
Wide 16:9 landscape cinematic frame. a military parade in a foreign city with giant silhouettes marching behind rows of soldiers, wide shot, cold imperial light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nhưng thời thế đổi thay. Tàu chiến, đại bác và máy bay ngày càng mạnh. Người khổng lồ không còn là vũ khí bất…

```text
Wide 16:9 landscape cinematic frame. a massive naval gun on a warship deck pointing toward a distant silhouette on the shore, wide shot, grey industrial light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Vì vậy Marley cần sức mạnh Thủy tổ, thứ đang nằm trên đảo Paradis. Đó là lý do năm 845, bốn chiến binh trẻ đư…

```text
Wide 16:9 landscape cinematic frame. four small figures standing on a ship's deck looking toward a distant island with a massive wall, back view, wide shot, cold dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Những đứa trẻ này lớn lên trong khu cách ly, được dạy rằng người trên đảo là quỷ dữ. Khi sống giữa họ, chúng…

```text
Wide 16:9 landscape cinematic frame. a young soldier sitting at a crowded barracks dinner table, looking at laughing comrades with a troubled expression, medium shot, warm conflicted light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Năm 845: bức tường sụp đổ

Lời: Năm 845, người khổng lồ Đại hình và người khổng lồ Thiết giáp phá thủng tường Maria. Họ là Bertholdt và Reine…

```text
Wide 16:9 landscape cinematic frame. a colossal silhouette looming over a wall gate as debris flies in every direction, low-angle shot, fiery dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhiều năm sau, người đọc mới biết một sự thật đau lòng liên quan tới ngày hôm đó và vai trò của chính sức mạn…

```text
Wide 16:9 landscape cinematic frame. a sealed envelope resting on the rubble of a destroyed house, close-up, somber dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Mẹ của Eren mất trong ngày đó. Eren thề sẽ tiêu diệt tất cả người khổng lồ. Cùng Mikasa và Armin, cậu gia nhậ…

```text
Wide 16:9 landscape cinematic frame. three small silhouettes standing on a hill looking at a ruined town behind a broken wall, back view, wide shot, somber sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Cũng trong đêm đó, Grisha tiêm cho Eren để truyền lại người khổng lồ Tiến công, và cả sức mạnh Thủy tổ mà ông…

```text
Wide 16:9 landscape cinematic frame. a syringe glinting on a forest floor at night beside a dropped key, close-up, cold eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Năm 850 tới 854: sự thật

Lời: Cũng trong những năm này, người dân trong tường phát hiện ra chính nhà vua của họ là giả, và hoàng gia thật đ…

```text
Wide 16:9 landscape cinematic frame. a small crown being placed on a young girl's head in a quiet stone hall, close-up, warm solemn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Năm 850, trận Trost, Eren lần đầu biến thành người khổng lồ. Những bí mật dần lộ ra: có người khổng lồ là ngư…

```text
Wide 16:9 landscape cinematic frame. a titan silhouette standing among ruined city rooftops as soldiers on wires look on in shock, wide shot, dramatic smoky light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Sau những trận chiến giành lại tường Maria, Eren, Mikasa và Armin cuối cùng mở được tầng hầm. Bên trong là nh…

```text
Wide 16:9 landscape cinematic frame. an open basement with dusty books and old photographs spread on a table under a single hanging bulb, close-up, warm revealing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhật ký của Grisha cũng tiết lộ bí mật của chính người khổng lồ Tiến công: người thừa kế có thể nhìn thấy ký…

```text
Wide 16:9 landscape cinematic frame. an open journal with pages that seem to blur into overlapping images of different eras, symbolic close-up, eerie warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nhân loại không bị diệt vong. Thế giới bên ngoài vẫn tồn tại, và họ, người Eldia trên đảo, bị cả thế giới coi…

```text
Wide 16:9 landscape cinematic frame. a vast ocean at sunrise seen from a beach with small figures standing at the water's edge, wide shot, awe-struck light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Khi lần đầu tới bờ biển, Eren chỉ tay ra phía xa và hỏi: nếu giết hết kẻ thù bên kia biển, chúng ta sẽ được t…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing ankle-deep in the sea pointing toward the horizon while others watch from the shore, back view, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Trước đó, Marley vừa kết thúc một cuộc chiến dài với liên minh các nước phía đông, và thấy rõ người khổng lồ…

```text
Wide 16:9 landscape cinematic frame. a battered fortress on a cliff overlooking the sea with smoke rising and damaged warships in the bay, wide shot, grey dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Năm 854, Eren tấn công khu Liberio ở Marley. Chiến tranh giữa đảo Paradis và thế giới chính thức bắt đầu.

```text
Wide 16:9 landscape cinematic frame. a festival stage at night in a foreign city with lights suddenly disrupted and smoke rising, wide shot, chaotic dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Năm 854: Cuộc dậm nát

Lời: Để làm được điều đó, Eren cần tiếp xúc với một người mang dòng máu hoàng gia. Người đó là Zeke, anh trai cậu,…

```text
Wide 16:9 landscape cinematic frame. two figures standing apart in a vast luminous desert, one reaching toward the other, wide shot, ethereal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Eren chạm được tới Con đường, nơi không gian và thời gian gặp nhau, và gặp Ymir. Cậu thuyết phục cô cho cậu d…

```text
Wide 16:9 landscape cinematic frame. an endless sandy expanse under a starry sky with a giant glowing tree of light rising from the horizon, wide shot, ethereal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Và Eren kích hoạt Cuộc dậm nát: hàng triệu người khổng lồ trong ba bức tường thức dậy, bước ra ngoài, và tiến…

```text
Wide 16:9 landscape cinematic frame. an endless line of colossal silhouettes marching across a flat landscape toward the horizon under a burning sky, aerial wide shot, apocalyptic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Theo truyện, khoảng tám mươi phần trăm nhân loại bên ngoài đảo mất đi. Kaku không mô tả chi tiết. Đây là sự k…

```text
Wide 16:9 landscape cinematic frame. a silent empty city under a dust-filled orange sky, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Cả Armin, người bạn thân nhất, và Reiner, kẻ từng phá tường năm 845, cùng đứng trong liên minh đó. Hai nghìn…

```text
Wide 16:9 landscape cinematic frame. two figures in different uniforms standing side by side on a cliff facing a distant storm, back view, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Những người từng là bạn của Eren, cùng những người từng là kẻ thù, liên minh với nhau để ngăn cậu lại.

```text
Wide 16:9 landscape cinematic frame. a small airship flying through a dark sky toward a massive silhouette, with figures from different uniforms standing together on its deck, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Cuối cùng, Mikasa là người kết thúc cuộc chiến. Eren mất, và sức mạnh người khổng lồ biến mất khỏi thế giới.

```text
Wide 16:9 landscape cinematic frame. a single red scarf-like cloth drifting in the wind above a quiet battlefield at dawn, close-up, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Và có một chi tiết quan trọng: Ymir, sau hai nghìn năm, cuối cùng được giải thoát. Truyện gợi ý rằng cô chờ đ…

```text
Wide 16:9 landscape cinematic frame. a small figure of a girl standing peacefully under a vast tree at sunset, then fading into light, symbolic wide shot, gentle golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Sau đó: vòng lặp chưa kết thúc

Lời: Armin trở thành đại sứ hòa bình, cố gắng nói chuyện với thế giới. Những người sống sót mang theo câu hỏi: làm…

```text
Wide 16:9 landscape cinematic frame. a small ship carrying a few figures sailing toward a distant foreign harbor under a clearing sky, wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Phần kết của manga cho thấy thời gian trôi qua sau Cuộc dậm nát. Đảo Paradis tiếp tục tồn tại, và thế giới kh…

```text
Wide 16:9 landscape cinematic frame. a small island seen from far away with a distant city skyline growing over the years, time-lapse style wide shot, changing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và ở cuối cùng, trên đồi nơi Eren được chôn, một cái cây lớn mọc lên. Một cậu bé tìm tới cái cây đó. Truyện đ…

```text
Wide 16:9 landscape cinematic frame. a lone child walking toward a massive tree with a dark hollow at its base on a grassy hill, wide shot, ominous soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: dòng thời gian bắt đầu bằng một cô gái chạm vào cây, và kết thúc bằng một cậu bé tìm tới cây. Hai…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a large circle on a scroll connecting the first and last points of a timeline. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Độ chắc chắn của từng mốc

Lời: Tổng kết độ chắc chắn. Chắc chắn: Ymir có sức mạnh, chín người khổng lồ, lời nguyền mười ba năm, Karl Fritz x…

```text
Wide 16:9 landscape cinematic frame. a checklist on parchment with many items marked by solid circles, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Là lời kể của một phía: chi tiết những tội ác của đế quốc Eldia, và câu chuyện anh hùng Helos. Truyện cho thấ…

```text
Wide 16:9 landscape cinematic frame. the same checklist with two items marked by half circles and small quote marks, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Để ngỏ: bản chất của nguồn gốc sự sống trong cái cây, và ý nghĩa cuối cùng của cái kết. Người đọc vẫn tranh l…

```text
Wide 16:9 landscape cinematic frame. the same checklist with two items marked by dotted circles and a question mark, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Toàn bộ dòng thời gian

Lời: Và đây là cả dòng thời gian trong một hình. Khoảng hai nghìn năm trước: Ymir chạm vào cây, trở thành người kh…

```text
Wide 16:9 landscape cinematic frame. a long timeline scroll with the first section illuminated showing a tree icon and nine small figures, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Gần một nghìn bảy trăm năm: Đế quốc Eldia. Năm 743: Karl Fritz, đại chiến người khổng lồ, ba bức tường, xóa k…

```text
Wide 16:9 landscape cinematic frame. the middle section of the scroll with an empire icon and three concentric wall circles illuminated, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Một trăm năm trong tường. Năm 845: tường Maria sụp đổ. Năm 850: Trost và những bí mật. Tầng hầm được mở.

```text
Wide 16:9 landscape cinematic frame. the later section of the scroll with a broken wall icon and a small key icon illuminated, parchment close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Năm 854: Liberio, Con đường, Cuộc dậm nát, sức mạnh người khổng lồ biến mất. Và sau đó: một cái cây, một cậu…

```text
Wide 16:9 landscape cinematic frame. the full timeline scroll unrolled with the final section showing a tree icon mirroring the first, wide overhead shot, radiant bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Kết

Lời: Attack on Titan là câu chuyện hai nghìn năm về tự do: một cô gái nô lệ không được tự do, một dân tộc bị nhốt…

```text
Wide 16:9 landscape cinematic frame. a bird flying freely over a massive stone wall toward an open sky at dawn, wide shot, hopeful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bạn nghĩ vòng lặp ở cuối truyện có bắt đầu lại không? Và mốc nào trong dòng thời gian khiến bạn bất ngờ nhất?…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny tree doodle and a looping arrow, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Video tiếp theo, Kaku chuyển sang một câu chuyện dịu dàng hơn nhiều: Frieren, và những chi tiết cài cắm về Hi…

```text
Wide 16:9 landscape cinematic frame. a small bouquet of blue flowers resting on a stone bench in a quiet field at sunset, close-up, gentle nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những dòng thời gian dài như thế này, hãy đăng ký kênh. Kaku sẽ tiếp tục trải những cuộn sổ dài…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the enormous scroll with great effort and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc dòng thời gian

Khoảng 116 giây · cảnh s01–s09 · 1502 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này đi qua toàn bộ Attack on Titan, từ khởi đầu hai nghìn năm trước tới tận phần kết. Nếu bạn chưa xem hết, hãy lưu video lại.

<short pause> Năm 845 theo lịch trong truyện, một người khổng lồ cao hơn cả bức tường năm mươi mét xuất hiện, và đá thủng cổng thị trấn Shiganshina. Một trăm năm hòa bình kết thúc trong một buổi chiều.

<short pause> Nhưng câu chuyện không bắt đầu từ năm 845. Nó bắt đầu từ khoảng hai nghìn năm trước, với một cô gái nô lệ chạy trốn trong một khu rừng.

<short pause> Câu hỏi hôm nay: điều gì đã xảy ra trong hai nghìn năm đó? Vì sao có những bức tường, vì sao có người khổng lồ, và vì sao tất cả dẫn tới một cậu bé tên Eren?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku trải dòng thời gian hai nghìn năm của Attack on Titan. Mỗi mốc có mức độ chắc chắn, và cuối video là cả dòng thời gian trong một hình.

<short pause> Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Anime do WIT Studio rồi MAPPA thực hiện, kết thúc năm 2023.

<short pause> Trước khi đi, một lưu ý quan trọng. Những năm như 845 hay 854 là lịch dùng trong những bức tường. Còn khoảng hai nghìn năm là con số truyện dùng để chỉ thời gian từ khi sức mạnh người khổng lồ xuất hiện.

<short pause> Một lưu ý nữa: phần lớn lịch sử trong truyện được kể lại bởi những người có lý do để bóp méo nó. Người Marley kể một kiểu, người Eldia kể một kiểu. Kaku sẽ đánh dấu mốc nào chắc chắn, mốc nào là lời kể.

<short pause> Và vì truyện có một năng lực liên quan tới ký ức và thời gian, có những mốc mà ngay cả nhân vật cũng không chắc. Đây là một dòng thời gian được xây dựng rất khéo.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này đi qua toàn bộ Attack on Titan, từ khởi đầu hai nghìn năm trước tới tận phần kết. Nếu bạn chưa xem hết, hãy lưu video lại.

[pause] Năm 845 theo lịch trong truyện, một người khổng lồ cao hơn cả bức tường năm mươi mét xuất hiện, và đá thủng cổng thị trấn Shiganshina. Một trăm năm hòa bình kết thúc trong một buổi chiều.

[pause] Nhưng câu chuyện không bắt đầu từ năm 845. Nó bắt đầu từ khoảng hai nghìn năm trước, với một cô gái nô lệ chạy trốn trong một khu rừng.

[pause] [curious] Câu hỏi hôm nay: điều gì đã xảy ra trong hai nghìn năm đó? Vì sao có những bức tường, vì sao có người khổng lồ, và vì sao tất cả dẫn tới một cậu bé tên Eren?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku trải dòng thời gian hai nghìn năm của Attack on Titan. Mỗi mốc có mức độ chắc chắn, và cuối video là cả dòng thời gian trong một hình.

[pause] Attack on Titan là manga của Isayama Hajime, đăng từ năm 2009 tới 2021. Anime do WIT Studio rồi MAPPA thực hiện, kết thúc năm 2023.

[pause] Trước khi đi, một lưu ý quan trọng. Những năm như 845 hay 854 là lịch dùng trong những bức tường. Còn khoảng hai nghìn năm là con số truyện dùng để chỉ thời gian từ khi sức mạnh người khổng lồ xuất hiện.

[pause] Một lưu ý nữa: phần lớn lịch sử trong truyện được kể lại bởi những người có lý do để bóp méo nó. Người Marley kể một kiểu, người Eldia kể một kiểu. Kaku sẽ đánh dấu mốc nào chắc chắn, mốc nào là lời kể.

[pause] Và vì truyện có một năng lực liên quan tới ký ức và thời gian, có những mốc mà ngay cả nhân vật cũng không chắc. Đây là một dòng thời gian được xây dựng rất khéo.
```

### c02 · Khoảng 2.000 năm trước: Ymir / Chín người khổng lồ

Khoảng 114 giây · cảnh s10–s20 · 1484 ký tự

**Gemini**

```text
Khoảng hai nghìn năm trước, trong vương quốc Eldia của vua Fritz, có một cô gái nô lệ tên Ymir. Cô bị đổ tội làm thả những con lợn của nhà vua, và bị săn đuổi như một con thú.

<short pause> Chạy trốn trong rừng, Ymir ngã vào hốc một cái cây cổ thụ khổng lồ. Ở đó, cô chạm vào một thứ mà truyện gọi là nguồn gốc của mọi sự sống.

<short pause> Đây là mốc số không của cả câu chuyện. Truyện không nói rõ cái cây là gì, hay thứ bên trong nó từ đâu tới. Kaku ghi nó ở mức để ngỏ.

<short pause> Cô trở thành người khổng lồ đầu tiên.

<short pause> Nhưng thay vì được tự do, Ymir tiếp tục phục vụ vua Fritz. Cô xây cầu, mở đường, và giúp Eldia chinh phục những vùng đất xung quanh, trong đó có Marley.

<short pause> Ymir sống khoảng mười ba năm sau khi có sức mạnh. Cô chết khi đỡ một ngọn giáo nhắm vào nhà vua. Mười ba năm, con số này sẽ trở thành lời nguyền của cả dòng máu cô.

<short pause> <laugh> Kaku để ý: truyện cho thấy Ymir không chỉ là nạn nhân của nhà vua, mà còn là tù nhân của chính tình cảm trung thành của mình. Chìa khóa của cả câu chuyện nằm ở đây.

<short pause> Sau khi Ymir chết, sức mạnh của cô được chia cho ba người con gái: Maria, Rose và Sina. Sức mạnh cứ thế truyền đi, và chia thành chín người khổng lồ.

<short pause> Mỗi người khổng lồ có năng lực riêng: người khổng lồ Đại hình, Thiết giáp, Nữ, Hàm, Xe, Quái thú, Chiến chùy, Tiến công, và Thủy tổ.

<short pause> Và mọi người thừa hưởng sức mạnh đều chịu lời nguyền của Ymir: chỉ sống thêm mười ba năm.

<short pause> Tên ba người con gái, Maria, Rose, Sina, về sau được dùng để đặt tên cho ba bức tường. Một chi tiết nhỏ cho thấy người xây tường biết rất rõ lịch sử này.
```

**ElevenLabs**

```text
Khoảng hai nghìn năm trước, trong vương quốc Eldia của vua Fritz, có một cô gái nô lệ tên Ymir. Cô bị đổ tội làm thả những con lợn của nhà vua, và bị săn đuổi như một con thú.

[pause] Chạy trốn trong rừng, Ymir ngã vào hốc một cái cây cổ thụ khổng lồ. Ở đó, cô chạm vào một thứ mà truyện gọi là nguồn gốc của mọi sự sống.

[pause] Đây là mốc số không của cả câu chuyện. Truyện không nói rõ cái cây là gì, hay thứ bên trong nó từ đâu tới. Kaku ghi nó ở mức để ngỏ.

[pause] Cô trở thành người khổng lồ đầu tiên.

[pause] Nhưng thay vì được tự do, Ymir tiếp tục phục vụ vua Fritz. Cô xây cầu, mở đường, và giúp Eldia chinh phục những vùng đất xung quanh, trong đó có Marley.

[pause] Ymir sống khoảng mười ba năm sau khi có sức mạnh. Cô chết khi đỡ một ngọn giáo nhắm vào nhà vua. Mười ba năm, con số này sẽ trở thành lời nguyền của cả dòng máu cô.

[pause] [chuckles] Kaku để ý: truyện cho thấy Ymir không chỉ là nạn nhân của nhà vua, mà còn là tù nhân của chính tình cảm trung thành của mình. Chìa khóa của cả câu chuyện nằm ở đây.

[pause] Sau khi Ymir chết, sức mạnh của cô được chia cho ba người con gái: Maria, Rose và Sina. Sức mạnh cứ thế truyền đi, và chia thành chín người khổng lồ.

[pause] Mỗi người khổng lồ có năng lực riêng: người khổng lồ Đại hình, Thiết giáp, Nữ, Hàm, Xe, Quái thú, Chiến chùy, Tiến công, và Thủy tổ.

[pause] Và mọi người thừa hưởng sức mạnh đều chịu lời nguyền của Ymir: chỉ sống thêm mười ba năm.

[pause] Tên ba người con gái, Maria, Rose, Sina, về sau được dùng để đặt tên cho ba bức tường. Một chi tiết nhỏ cho thấy người xây tường biết rất rõ lịch sử này.
```

### c03 · Gần 1.700 năm: Đế quốc Eldia / Năm 743: Đại chiến người khổng lồ và những bức tường

Khoảng 120 giây · cảnh s21–s30 · 1560 ký tự

**Gemini**

```text
Trong khoảng một nghìn bảy trăm năm tiếp theo, Đế quốc Eldia dùng sức mạnh người khổng lồ để thống trị thế giới.

<short pause> Theo lời kể của người Marley, Eldia đã gây ra vô số tội ác với các dân tộc khác. Theo lời kể của một số người Eldia, Eldia đã mang lại phát triển. Sự thật có lẽ nằm ở giữa, nhưng truyện cho thấy bạo lực là có thật.

<short pause> Và mọi người khổng lồ của Eldia đều có chung một điểm yếu: chỉ người mang dòng máu hoàng gia mới dùng được toàn bộ sức mạnh Thủy tổ. Chi tiết này sẽ quyết định cả cái kết.

<short pause> Trong lòng đế quốc, chín gia tộc nắm giữ chín người khổng lồ cũng tranh giành quyền lực với nhau. Đế quốc mạnh nhất thế giới dần mục ruỗng từ bên trong.

<short pause> Khoảng năm 743 theo lịch tường, vị vua thứ một trăm bốn mươi lăm của Eldia là Karl Fritz. Ông ghê sợ lịch sử tàn bạo của dân tộc mình.

<short pause> Ông bí mật liên kết với gia tộc Tybur để chấm dứt đế quốc. Người Marley giành lại quyền lực, và câu chuyện được kể rằng một anh hùng tên Helos đã cứu Marley.

<short pause> Karl Fritz đưa một phần người Eldia tới đảo Paradis. Ông dùng hàng triệu người khổng lồ Đại hình để xây ba bức tường khổng lồ.

<short pause> Rồi ông dùng sức mạnh người khổng lồ Thủy tổ để xóa ký ức của người dân trong tường. Họ tin rằng thế giới bên ngoài đã bị người khổng lồ hủy diệt, và họ là những người cuối cùng.

<short pause> Ông còn tạo ra một lời thề từ bỏ chiến tranh, gắn vào sức mạnh Thủy tổ: người kế thừa dòng máu hoàng gia sẽ bị ý chí của ông ràng buộc, không muốn chống lại thế giới.

<short pause> Kaku thấy đây là một trong những quyết định gây tranh cãi nhất truyện: một vị vua chọn giam dân tộc mình trong lồng, để chờ ngày thế giới đến trả thù.
```

**ElevenLabs**

```text
Trong khoảng một nghìn bảy trăm năm tiếp theo, Đế quốc Eldia dùng sức mạnh người khổng lồ để thống trị thế giới.

[pause] Theo lời kể của người Marley, Eldia đã gây ra vô số tội ác với các dân tộc khác. Theo lời kể của một số người Eldia, Eldia đã mang lại phát triển. Sự thật có lẽ nằm ở giữa, nhưng truyện cho thấy bạo lực là có thật.

[pause] Và mọi người khổng lồ của Eldia đều có chung một điểm yếu: chỉ người mang dòng máu hoàng gia mới dùng được toàn bộ sức mạnh Thủy tổ. Chi tiết này sẽ quyết định cả cái kết.

[pause] Trong lòng đế quốc, chín gia tộc nắm giữ chín người khổng lồ cũng tranh giành quyền lực với nhau. Đế quốc mạnh nhất thế giới dần mục ruỗng từ bên trong.

[pause] Khoảng năm 743 theo lịch tường, vị vua thứ một trăm bốn mươi lăm của Eldia là Karl Fritz. Ông ghê sợ lịch sử tàn bạo của dân tộc mình.

[pause] Ông bí mật liên kết với gia tộc Tybur để chấm dứt đế quốc. Người Marley giành lại quyền lực, và câu chuyện được kể rằng một anh hùng tên Helos đã cứu Marley.

[pause] Karl Fritz đưa một phần người Eldia tới đảo Paradis. Ông dùng hàng triệu người khổng lồ Đại hình để xây ba bức tường khổng lồ.

[pause] Rồi ông dùng sức mạnh người khổng lồ Thủy tổ để xóa ký ức của người dân trong tường. Họ tin rằng thế giới bên ngoài đã bị người khổng lồ hủy diệt, và họ là những người cuối cùng.

[pause] Ông còn tạo ra một lời thề từ bỏ chiến tranh, gắn vào sức mạnh Thủy tổ: người kế thừa dòng máu hoàng gia sẽ bị ý chí của ông ràng buộc, không muốn chống lại thế giới.

[pause] Kaku thấy đây là một trong những quyết định gây tranh cãi nhất truyện: một vị vua chọn giam dân tộc mình trong lồng, để chờ ngày thế giới đến trả thù.
```

### c04 · 100 năm trong tường / Những người không bị xóa ký ức / Bên kia biển: Marley và thế giới

Khoảng 153 giây · cảnh s31–s43 · 1992 ký tự

**Gemini**

```text
Trong một trăm năm tiếp theo, người dân trong tường sống yên bình, nhưng không biết gì về thế giới bên ngoài. Lịch sử bị cấm. Ai hỏi quá nhiều thì biến mất.

<short pause> Ở Marley, người Eldia bị dồn vào khu cách ly, phải đeo băng tay để phân biệt. Những đứa trẻ Eldia được huấn luyện làm chiến binh, để thừa kế người khổng lồ và phục vụ Marley.

<short pause> Trong khu cách ly, có một bác sĩ tên Grisha Yeager, người tham gia phong trào phục quốc Eldia. Về sau, ông trốn tới đảo Paradis, mang theo người khổng lồ Tiến công.

<short pause> Trước đó, Grisha từng có một gia đình khác ở Marley, và một người con trai lớn tên Zeke. Hai anh em cùng cha, Zeke và Eren, sẽ gặp nhau ở trung tâm của cuộc chiến cuối cùng.

<short pause> Grisha lập gia đình trong tường, có con trai là Eren. Và ông để lại một tầng hầm khóa kín, cùng chiếc chìa khóa mà Eren mang trên cổ.

<short pause> Có một chi tiết thú vị: không phải ai trong tường cũng bị xóa ký ức. Gia tộc Ackerman, những người từng làm cận vệ cho hoàng gia, không bị sức mạnh Thủy tổ ảnh hưởng.

<short pause> Vì vậy họ bị nhà vua trong tường săn đuổi và đàn áp. Levi và Mikasa, hai chiến binh mạnh nhất phe loài người trong truyện, đều mang dòng máu này.

<short pause> Mẹ của Mikasa còn thuộc một dòng họ đến từ phương Đông, liên quan tới đất nước Hizuru. Chi tiết nhỏ này về sau trở thành mối liên hệ ngoại giao quan trọng.

<short pause> <laugh> Kaku để ý: ngay trong những bức tường, lịch sử cũng không đồng nhất. Có những người mang ký ức mà người khác không có, và họ phải trả giá cho điều đó.

<short pause> Trong khi người trong tường sống yên bình, Marley dùng những người khổng lồ Eldia để đánh chiếm các nước khác, và trở thành cường quốc.

<short pause> Nhưng thời thế đổi thay. Tàu chiến, đại bác và máy bay ngày càng mạnh. Người khổng lồ không còn là vũ khí bất khả chiến bại.

<short pause> Vì vậy Marley cần sức mạnh Thủy tổ, thứ đang nằm trên đảo Paradis. Đó là lý do năm 845, bốn chiến binh trẻ được cử tới đảo: Reiner, Bertholdt, Annie và Marcel.

<short pause> Những đứa trẻ này lớn lên trong khu cách ly, được dạy rằng người trên đảo là quỷ dữ. Khi sống giữa họ, chúng dần nhận ra những người đó cũng chỉ là con người.
```

**ElevenLabs**

```text
Trong một trăm năm tiếp theo, người dân trong tường sống yên bình, nhưng không biết gì về thế giới bên ngoài. Lịch sử bị cấm. Ai hỏi quá nhiều thì biến mất.

[pause] Ở Marley, người Eldia bị dồn vào khu cách ly, phải đeo băng tay để phân biệt. Những đứa trẻ Eldia được huấn luyện làm chiến binh, để thừa kế người khổng lồ và phục vụ Marley.

[pause] Trong khu cách ly, có một bác sĩ tên Grisha Yeager, người tham gia phong trào phục quốc Eldia. Về sau, ông trốn tới đảo Paradis, mang theo người khổng lồ Tiến công.

[pause] Trước đó, Grisha từng có một gia đình khác ở Marley, và một người con trai lớn tên Zeke. Hai anh em cùng cha, Zeke và Eren, sẽ gặp nhau ở trung tâm của cuộc chiến cuối cùng.

[pause] Grisha lập gia đình trong tường, có con trai là Eren. Và ông để lại một tầng hầm khóa kín, cùng chiếc chìa khóa mà Eren mang trên cổ.

[pause] Có một chi tiết thú vị: không phải ai trong tường cũng bị xóa ký ức. Gia tộc Ackerman, những người từng làm cận vệ cho hoàng gia, không bị sức mạnh Thủy tổ ảnh hưởng.

[pause] Vì vậy họ bị nhà vua trong tường săn đuổi và đàn áp. Levi và Mikasa, hai chiến binh mạnh nhất phe loài người trong truyện, đều mang dòng máu này.

[pause] Mẹ của Mikasa còn thuộc một dòng họ đến từ phương Đông, liên quan tới đất nước Hizuru. Chi tiết nhỏ này về sau trở thành mối liên hệ ngoại giao quan trọng.

[pause] [chuckles] Kaku để ý: ngay trong những bức tường, lịch sử cũng không đồng nhất. Có những người mang ký ức mà người khác không có, và họ phải trả giá cho điều đó.

[pause] Trong khi người trong tường sống yên bình, Marley dùng những người khổng lồ Eldia để đánh chiếm các nước khác, và trở thành cường quốc.

[pause] Nhưng thời thế đổi thay. Tàu chiến, đại bác và máy bay ngày càng mạnh. Người khổng lồ không còn là vũ khí bất khả chiến bại.

[pause] Vì vậy Marley cần sức mạnh Thủy tổ, thứ đang nằm trên đảo Paradis. Đó là lý do năm 845, bốn chiến binh trẻ được cử tới đảo: Reiner, Bertholdt, Annie và Marcel.

[pause] Những đứa trẻ này lớn lên trong khu cách ly, được dạy rằng người trên đảo là quỷ dữ. Khi sống giữa họ, chúng dần nhận ra những người đó cũng chỉ là con người.
```

### c05 · Năm 845: bức tường sụp đổ / Năm 850 tới 854: sự thật

Khoảng 141 giây · cảnh s44–s55 · 1835 ký tự

**Gemini**

```text
Năm 845, người khổng lồ Đại hình và người khổng lồ Thiết giáp phá thủng tường Maria. Họ là Bertholdt và Reiner, những chiến binh Marley được cử tới đảo.

<short pause> Nhiều năm sau, người đọc mới biết một sự thật đau lòng liên quan tới ngày hôm đó và vai trò của chính sức mạnh người khổng lồ Tiến công. Kaku không nói chi tiết, để bạn tự cảm nhận khi xem.

<short pause> Mẹ của Eren mất trong ngày đó. Eren thề sẽ tiêu diệt tất cả người khổng lồ. Cùng Mikasa và Armin, cậu gia nhập quân đội.

<short pause> Cũng trong đêm đó, Grisha tiêm cho Eren để truyền lại người khổng lồ Tiến công, và cả sức mạnh Thủy tổ mà ông đã giành được. Eren không nhớ gì.

<short pause> Cũng trong những năm này, người dân trong tường phát hiện ra chính nhà vua của họ là giả, và hoàng gia thật đã giấu sự thật suốt một trăm năm. Historia, người mang dòng máu hoàng gia, lên làm nữ hoàng.

<short pause> Năm 850, trận Trost, Eren lần đầu biến thành người khổng lồ. Những bí mật dần lộ ra: có người khổng lồ là người, và có kẻ thù đang ở ngay trong quân đội.

<short pause> Sau những trận chiến giành lại tường Maria, Eren, Mikasa và Armin cuối cùng mở được tầng hầm. Bên trong là những cuốn nhật ký của Grisha, và sự thật về thế giới bên ngoài.

<short pause> Nhật ký của Grisha cũng tiết lộ bí mật của chính người khổng lồ Tiến công: người thừa kế có thể nhìn thấy ký ức của những người thừa kế trước, và cả sau mình.

<short pause> Nhân loại không bị diệt vong. Thế giới bên ngoài vẫn tồn tại, và họ, người Eldia trên đảo, bị cả thế giới coi là quỷ dữ.

<short pause> Khi lần đầu tới bờ biển, Eren chỉ tay ra phía xa và hỏi: nếu giết hết kẻ thù bên kia biển, chúng ta sẽ được tự do chứ? Câu hỏi đó báo trước cái kết.

<short pause> Trước đó, Marley vừa kết thúc một cuộc chiến dài với liên minh các nước phía đông, và thấy rõ người khổng lồ đã không còn đủ mạnh. Thế giới đang chuẩn bị tấn công đảo Paradis.

<short pause> Năm 854, Eren tấn công khu Liberio ở Marley. Chiến tranh giữa đảo Paradis và thế giới chính thức bắt đầu.
```

**ElevenLabs**

```text
Năm 845, người khổng lồ Đại hình và người khổng lồ Thiết giáp phá thủng tường Maria. Họ là Bertholdt và Reiner, những chiến binh Marley được cử tới đảo.

[pause] Nhiều năm sau, người đọc mới biết một sự thật đau lòng liên quan tới ngày hôm đó và vai trò của chính sức mạnh người khổng lồ Tiến công. Kaku không nói chi tiết, để bạn tự cảm nhận khi xem.

[pause] Mẹ của Eren mất trong ngày đó. Eren thề sẽ tiêu diệt tất cả người khổng lồ. Cùng Mikasa và Armin, cậu gia nhập quân đội.

[pause] Cũng trong đêm đó, Grisha tiêm cho Eren để truyền lại người khổng lồ Tiến công, và cả sức mạnh Thủy tổ mà ông đã giành được. Eren không nhớ gì.

[pause] Cũng trong những năm này, người dân trong tường phát hiện ra chính nhà vua của họ là giả, và hoàng gia thật đã giấu sự thật suốt một trăm năm. Historia, người mang dòng máu hoàng gia, lên làm nữ hoàng.

[pause] Năm 850, trận Trost, Eren lần đầu biến thành người khổng lồ. Những bí mật dần lộ ra: có người khổng lồ là người, và có kẻ thù đang ở ngay trong quân đội.

[pause] Sau những trận chiến giành lại tường Maria, Eren, Mikasa và Armin cuối cùng mở được tầng hầm. Bên trong là những cuốn nhật ký của Grisha, và sự thật về thế giới bên ngoài.

[pause] Nhật ký của Grisha cũng tiết lộ bí mật của chính người khổng lồ Tiến công: người thừa kế có thể nhìn thấy ký ức của những người thừa kế trước, và cả sau mình.

[pause] Nhân loại không bị diệt vong. Thế giới bên ngoài vẫn tồn tại, và họ, người Eldia trên đảo, bị cả thế giới coi là quỷ dữ.

[pause] [curious] Khi lần đầu tới bờ biển, Eren chỉ tay ra phía xa và hỏi: nếu giết hết kẻ thù bên kia biển, chúng ta sẽ được tự do chứ? Câu hỏi đó báo trước cái kết.

[pause] Trước đó, Marley vừa kết thúc một cuộc chiến dài với liên minh các nước phía đông, và thấy rõ người khổng lồ đã không còn đủ mạnh. Thế giới đang chuẩn bị tấn công đảo Paradis.

[pause] Năm 854, Eren tấn công khu Liberio ở Marley. Chiến tranh giữa đảo Paradis và thế giới chính thức bắt đầu.
```

### c06 · Năm 854: Cuộc dậm nát / Sau đó: vòng lặp chưa kết thúc

Khoảng 131 giây · cảnh s56–s67 · 1709 ký tự

**Gemini**

```text
Để làm được điều đó, Eren cần tiếp xúc với một người mang dòng máu hoàng gia. Người đó là Zeke, anh trai cậu, người có kế hoạch riêng của mình.

<short pause> Eren chạm được tới Con đường, nơi không gian và thời gian gặp nhau, và gặp Ymir. Cậu thuyết phục cô cho cậu dùng toàn bộ sức mạnh Thủy tổ.

<short pause> Và Eren kích hoạt Cuộc dậm nát: hàng triệu người khổng lồ trong ba bức tường thức dậy, bước ra ngoài, và tiến về phía thế giới.

<short pause> Theo truyện, khoảng tám mươi phần trăm nhân loại bên ngoài đảo mất đi. Kaku không mô tả chi tiết. Đây là sự kiện tàn khốc nhất của cả dòng thời gian.

<short pause> Cả Armin, người bạn thân nhất, và Reiner, kẻ từng phá tường năm 845, cùng đứng trong liên minh đó. Hai nghìn năm hận thù, và những kẻ thù cũ cuối cùng chiến đấu cạnh nhau.

<short pause> Những người từng là bạn của Eren, cùng những người từng là kẻ thù, liên minh với nhau để ngăn cậu lại.

<short pause> Cuối cùng, Mikasa là người kết thúc cuộc chiến. Eren mất, và sức mạnh người khổng lồ biến mất khỏi thế giới.

<short pause> Và có một chi tiết quan trọng: Ymir, sau hai nghìn năm, cuối cùng được giải thoát. Truyện gợi ý rằng cô chờ đợi một người có thể yêu mà không bị ràng buộc, và cô tìm thấy điều đó qua Mikasa.

<short pause> Armin trở thành đại sứ hòa bình, cố gắng nói chuyện với thế giới. Những người sống sót mang theo câu hỏi: làm sao để không lặp lại hai nghìn năm vừa qua?

<short pause> Phần kết của manga cho thấy thời gian trôi qua sau Cuộc dậm nát. Đảo Paradis tiếp tục tồn tại, và thế giới không hề hết chiến tranh.

<short pause> Và ở cuối cùng, trên đồi nơi Eren được chôn, một cái cây lớn mọc lên. Một cậu bé tìm tới cái cây đó. Truyện để người đọc tự hiểu: vòng lặp có thể bắt đầu lại.

<short pause> <laugh> Kaku để ý: dòng thời gian bắt đầu bằng một cô gái chạm vào cây, và kết thúc bằng một cậu bé tìm tới cây. Hai nghìn năm, như một vòng tròn.
```

**ElevenLabs**

```text
Để làm được điều đó, Eren cần tiếp xúc với một người mang dòng máu hoàng gia. Người đó là Zeke, anh trai cậu, người có kế hoạch riêng của mình.

[pause] Eren chạm được tới Con đường, nơi không gian và thời gian gặp nhau, và gặp Ymir. Cậu thuyết phục cô cho cậu dùng toàn bộ sức mạnh Thủy tổ.

[pause] Và Eren kích hoạt Cuộc dậm nát: hàng triệu người khổng lồ trong ba bức tường thức dậy, bước ra ngoài, và tiến về phía thế giới.

[pause] Theo truyện, khoảng tám mươi phần trăm nhân loại bên ngoài đảo mất đi. Kaku không mô tả chi tiết. Đây là sự kiện tàn khốc nhất của cả dòng thời gian.

[pause] Cả Armin, người bạn thân nhất, và Reiner, kẻ từng phá tường năm 845, cùng đứng trong liên minh đó. Hai nghìn năm hận thù, và những kẻ thù cũ cuối cùng chiến đấu cạnh nhau.

[pause] Những người từng là bạn của Eren, cùng những người từng là kẻ thù, liên minh với nhau để ngăn cậu lại.

[pause] Cuối cùng, Mikasa là người kết thúc cuộc chiến. Eren mất, và sức mạnh người khổng lồ biến mất khỏi thế giới.

[pause] Và có một chi tiết quan trọng: Ymir, sau hai nghìn năm, cuối cùng được giải thoát. Truyện gợi ý rằng cô chờ đợi một người có thể yêu mà không bị ràng buộc, và cô tìm thấy điều đó qua Mikasa.

[pause] Armin trở thành đại sứ hòa bình, cố gắng nói chuyện với thế giới. [curious] Những người sống sót mang theo câu hỏi: làm sao để không lặp lại hai nghìn năm vừa qua?

[pause] Phần kết của manga cho thấy thời gian trôi qua sau Cuộc dậm nát. Đảo Paradis tiếp tục tồn tại, và thế giới không hề hết chiến tranh.

[pause] Và ở cuối cùng, trên đồi nơi Eren được chôn, một cái cây lớn mọc lên. Một cậu bé tìm tới cái cây đó. Truyện để người đọc tự hiểu: vòng lặp có thể bắt đầu lại.

[pause] [chuckles] Kaku để ý: dòng thời gian bắt đầu bằng một cô gái chạm vào cây, và kết thúc bằng một cậu bé tìm tới cây. Hai nghìn năm, như một vòng tròn.
```

### c07 · Độ chắc chắn của từng mốc / Toàn bộ dòng thời gian / Kết

Khoảng 122 giây · cảnh s68–s78 · 1586 ký tự

**Gemini**

```text
Tổng kết độ chắc chắn. Chắc chắn: Ymir có sức mạnh, chín người khổng lồ, lời nguyền mười ba năm, Karl Fritz xây tường, năm 845, năm 850, năm 854 và Cuộc dậm nát.

<short pause> Là lời kể của một phía: chi tiết những tội ác của đế quốc Eldia, và câu chuyện anh hùng Helos. Truyện cho thấy cả hai phía đều bóp méo lịch sử.

<short pause> Để ngỏ: bản chất của nguồn gốc sự sống trong cái cây, và ý nghĩa cuối cùng của cái kết. Người đọc vẫn tranh luận tới hôm nay.

<short pause> Và đây là cả dòng thời gian trong một hình. Khoảng hai nghìn năm trước: Ymir chạm vào cây, trở thành người khổng lồ đầu tiên, sống mười ba năm, sức mạnh chia làm chín.

<short pause> Gần một nghìn bảy trăm năm: Đế quốc Eldia. Năm 743: Karl Fritz, đại chiến người khổng lồ, ba bức tường, xóa ký ức, lời thề.

<short pause> Một trăm năm trong tường. Năm 845: tường Maria sụp đổ. Năm 850: Trost và những bí mật. Tầng hầm được mở.

<short pause> Năm 854: Liberio, Con đường, Cuộc dậm nát, sức mạnh người khổng lồ biến mất. Và sau đó: một cái cây, một cậu bé, và một câu hỏi.

<short pause> Attack on Titan là câu chuyện hai nghìn năm về tự do: một cô gái nô lệ không được tự do, một dân tộc bị nhốt trong tường, và một cậu bé muốn tự do tới mức sẵn sàng hủy diệt thế giới.

<short pause> Bạn nghĩ vòng lặp ở cuối truyện có bắt đầu lại không? Và mốc nào trong dòng thời gian khiến bạn bất ngờ nhất? Viết vào bình luận nhé.

<short pause> Video tiếp theo, Kaku chuyển sang một câu chuyện dịu dàng hơn nhiều: Frieren, và những chi tiết cài cắm về Himmel, người anh hùng mà cả thế giới dần quên, trừ một người.

<short pause> Nếu bạn thích những dòng thời gian dài như thế này, hãy đăng ký kênh. <laugh> Kaku sẽ tiếp tục trải những cuộn sổ dài nhất anime. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tổng kết độ chắc chắn. Chắc chắn: Ymir có sức mạnh, chín người khổng lồ, lời nguyền mười ba năm, Karl Fritz xây tường, năm 845, năm 850, năm 854 và Cuộc dậm nát.

[pause] Là lời kể của một phía: chi tiết những tội ác của đế quốc Eldia, và câu chuyện anh hùng Helos. Truyện cho thấy cả hai phía đều bóp méo lịch sử.

[pause] Để ngỏ: bản chất của nguồn gốc sự sống trong cái cây, và ý nghĩa cuối cùng của cái kết. Người đọc vẫn tranh luận tới hôm nay.

[pause] Và đây là cả dòng thời gian trong một hình. Khoảng hai nghìn năm trước: Ymir chạm vào cây, trở thành người khổng lồ đầu tiên, sống mười ba năm, sức mạnh chia làm chín.

[pause] Gần một nghìn bảy trăm năm: Đế quốc Eldia. Năm 743: Karl Fritz, đại chiến người khổng lồ, ba bức tường, xóa ký ức, lời thề.

[pause] Một trăm năm trong tường. Năm 845: tường Maria sụp đổ. Năm 850: Trost và những bí mật. Tầng hầm được mở.

[pause] Năm 854: Liberio, Con đường, Cuộc dậm nát, sức mạnh người khổng lồ biến mất. Và sau đó: một cái cây, một cậu bé, và một câu hỏi.

[pause] Attack on Titan là câu chuyện hai nghìn năm về tự do: một cô gái nô lệ không được tự do, một dân tộc bị nhốt trong tường, và một cậu bé muốn tự do tới mức sẵn sàng hủy diệt thế giới.

[pause] [curious] Bạn nghĩ vòng lặp ở cuối truyện có bắt đầu lại không? Và mốc nào trong dòng thời gian khiến bạn bất ngờ nhất? Viết vào bình luận nhé.

[pause] Video tiếp theo, Kaku chuyển sang một câu chuyện dịu dàng hơn nhiều: Frieren, và những chi tiết cài cắm về Himmel, người anh hùng mà cả thế giới dần quên, trừ một người.

[pause] Nếu bạn thích những dòng thời gian dài như thế này, hãy đăng ký kênh. [chuckles] Kaku sẽ tiếp tục trải những cuộn sổ dài nhất anime. Kaku gấp sổ đây, hẹn gặp lại!
```
