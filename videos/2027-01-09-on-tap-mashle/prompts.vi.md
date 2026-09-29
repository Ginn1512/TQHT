# Bộ prompt · Mashle: Ôn tập mọi thứ cần nhớ trước mùa 3

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 81 ảnh, 9 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (81 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Mashle tới hết anime mùa hai, arc kỳ thi ứng viên Thần giác giả. Không có nội dung…

```text
Wide 16:9 landscape cinematic frame. a grand magic academy castle at dusk with glowing windows, a closed notebook on a stone bench in the foreground, wide establishing shot, warm magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Mùa ba của Mashle trở lại trong tháng một, sau gần ba năm chờ đợi. Nếu bạn đã quên ai là ai và vì sao một cậu…

```text
Wide 16:9 landscape cinematic frame. a wall calendar showing January with a small cream puff doodle drawn on a date, close-up, bright morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Mashle là manga của tác giả Komoto Hajime, đăng trên Shonen Jump từ năm 2020 tới 2023. Anime mùa một ra mắt n…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes next to headphones and a phone playing an upbeat song, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đây là một bộ truyện hài nhại lại các câu chuyện học viện phép thuật nổi tiếng. Nhưng càng về sau, nó càng có…

```text
Wide 16:9 landscape cinematic frame. a classic magic school book cover next to a parody version with a muscular silhouette bursting through, side by side, humorous still life. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Kaku sẽ nhắc lại thế giới của Mashle, luật sức mạnh, những người bạn, các phe, và những nút thắt còn mở. Cuối…

```text
Wide 16:9 landscape cinematic frame. five small index cards on a desk with icons: a castle, a rulebook, a group of friends, a chessboard and a knot, top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Nếu bạn chưa xem Mashle, video này vẫn giúp bạn hiểu đủ để bắt đầu. Nhưng nhớ là có spoiler mùa một và mùa ha…

```text
Wide 16:9 landscape cinematic frame. a friendly signpost at a crossroads pointing toward a castle, with a small warning ribbon tied to it, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku phát bài ôn tập kèm một chiếc bánh su kem, vì thiếu bánh su kem thì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny cream puff on a plate beside a stack of study notes, cheerful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Thế giới: phép thuật là địa vị

Lời: Trong thế giới Mashle, phép thuật không chỉ là năng lực. Nó là địa vị, là giai cấp, là giấy thông hành để đượ…

```text
Wide 16:9 landscape cinematic frame. a society pyramid diagram on parchment with glowing wand icons at the top and a small crossed-out figure at the bottom, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Phép thuật dùng cho mọi việc trong đời sống: nấu ăn, dọn nhà, đi lại. Một người không có phép thuật sẽ không…

```text
Wide 16:9 landscape cinematic frame. a bustling magical town where brooms sweep by themselves and pots stir on their own, one person struggling to open a magically locked door, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và những gia đình có nhiều người sở hữu phép mạnh thì sống ở những khu cao cấp, học ở những trường danh giá,…

```text
Wide 16:9 landscape cinematic frame. an elegant upper district of a city on a hill with tall spires, a poorer district in the valley below, wide shot, contrasting warm and cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Mỗi người có những vạch trên mặt, gọi là dấu ấn phép thuật. Số vạch cho biết người đó dùng được bao nhiêu loạ…

```text
Wide 16:9 landscape cinematic frame. three stylized face silhouettes side by side with one, two and three glowing lines on their cheeks, clean diagram style, soft light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Kaku thấy đây là một câu chuyện rất quen: một xã hội đánh giá con người bằng một thứ họ không tự chọn được kh…

```text
Wide 16:9 landscape cinematic frame. a birth certificate style document with a single glowing mark stamp deciding a person's future, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu có một thế giới xếp hạng theo khả năng đọc sách, Kaku chắc chắn lên ngôi. Tiếc là thế giới Mashle xếp the…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a paper crown made of book pages, sighing at a wand it cannot use. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Còn người không có phép thuật thì sao? Họ bị coi là khiếm khuyết của xã hội, và có thể bị thanh trừng. Không…

```text
Wide 16:9 landscape cinematic frame. a dark notice board with a sealed decree pinned on it, a small shadowy figure hiding behind a corner, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và nhân vật chính của chúng ta, Mash Burnedead, không có một chút phép thuật nào.

```text
Wide 16:9 landscape cinematic frame. a quiet young man sitting on a tree stump in a forest clearing, holding a cream puff, no marks on his face, medium shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Mash không oán hận ai. Cậu điềm tĩnh, ít nói, thẳng thắn tới mức ngây ngô, và chỉ muốn được sống yên ổn với ô…

```text
Wide 16:9 landscape cinematic frame. a calm young man and an old man sharing cream puffs on a wooden porch at sunset, medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nhưng một ngày, người ta phát hiện ra cậu. Và để bảo vệ ông, Mash quyết định bước vào chính cái thế giới đã m…

```text
Wide 16:9 landscape cinematic frame. a young man walking out of a forest toward a distant city of spires, looking back once at a small cabin, wide shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Mash được một ông lão tên Regro nhặt về nuôi trong rừng. Để bảo vệ cậu, ông giấu cậu khỏi xã hội. Và Mash thì…

```text
Wide 16:9 landscape cinematic frame. an old man watching fondly from a small cabin porch as a young man does one-armed handstand push-ups on a boulder, wide shot, warm forest light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Tình hình hiện tại: từ học viện tới án tử

Lời: Để cha nuôi được sống yên ổn, Mash vào học viện phép thuật Easton với một mục tiêu duy nhất: trở thành Thần g…

```text
Wide 16:9 landscape cinematic frame. a young man standing at the enormous gates of a magic academy, looking up at the towers, back view, wide shot, bright hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Ngay trong kỳ thi đầu vào, Mash đã gây chấn động. Những bài thi cần phép thuật, cậu giải bằng sức mạnh và sự…

```text
Wide 16:9 landscape cinematic frame. a bewildered examiner holding a clipboard while a young man stands beside a completely shattered magical test apparatus, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Cậu được xếp vào ký túc xá Adler. Và từ ngày đầu, những học sinh quý tộc đã coi cậu là cái gai trong mắt.

```text
Wide 16:9 landscape cinematic frame. a group of arrogant students with wands glaring at a calm young man in a dormitory hallway, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Cậu vượt qua kỳ thi đầu vào, rồi mọi thử thách trong học viện, bằng cơ bắp nhưng giả vờ như đó là phép thuật.…

```text
Wide 16:9 landscape cinematic frame. a young man jumping so high he appears to be flying past astonished students holding wands, humorous wide shot, bright sky. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Đồng xu được trao cho những thành tích đặc biệt: đánh bại kẻ thù nguy hiểm, cứu người, hoàn thành nhiệm vụ kh…

```text
Wide 16:9 landscape cinematic frame. a gold coin being placed into a young man's large palm by an old teacher's hand, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Trong học viện, học sinh thu thập những đồng xu vàng. Ai có đủ số đồng xu sẽ trở thành ứng viên Thần giác giả.

```text
Wide 16:9 landscape cinematic frame. a small velvet pouch spilling shiny gold coins with a crest onto a wooden desk, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Trong những trận đấu đó, Mash lần đầu gặp những đối thủ thật sự nguy hiểm, những người sẵn sàng làm tổn thươn…

```text
Wide 16:9 landscape cinematic frame. a smug noble student holding a wand toward a fallen friend while a calm young man steps between them, medium shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Mùa một kết thúc với những trận đấu giữa ký túc xá Adler của Mash và ký túc xá Lang, cùng sự xuất hiện của mộ…

```text
Wide 16:9 landscape cinematic frame. two dormitory banners with different crests hanging opposite each other in a great hall, a dark insignia faintly visible in the shadows above, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Thầy hiệu trưởng Wahlberg là người đứng ra bảo vệ cậu. Ông đưa ra điều kiện: nếu Mash trở thành ứng viên Thần…

```text
Wide 16:9 landscape cinematic frame. a very old headmaster standing calmly between a young man and a group of stern officials, back view, dramatic hall light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Kỳ thi ứng viên giống một giải đấu thật sự: những trận đấu một chọi một, những thử thách đồng đội, và những đ…

```text
Wide 16:9 landscape cinematic frame. a tournament bracket carved on a stone wall with glowing names, a young man studying it with arms crossed, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Sang mùa hai, bí mật của Mash bị lộ. Cậu bị kết án, và cách duy nhất để thoát là trở thành ứng viên Thần giác…

```text
Wide 16:9 landscape cinematic frame. a courtroom-like hall with stern mages seated high above a calm young man standing alone, dramatic low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Mash cùng các bạn đánh bại nhóm Magia Lupus, giành được đồng xu của ký túc xá Lang, và tiến thêm một bước gần…

```text
Wide 16:9 landscape cinematic frame. a group of students celebrating in a ruined arena, a young man calmly eating a cream puff among them, wide shot, triumphant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Luật sức mạnh cần nhớ

Lời: Pháp sư dùng đũa để tập trung và giải phóng phép. Họ đọc thần chú, vung đũa, và phép thuật xuất hiện. Mash th…

```text
Wide 16:9 landscape cinematic frame. a row of students raising glowing wands, one young man at the end raising only his bare fist, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Luật thứ nhất: phép thuật trong Mashle mỗi người thường có một thuộc tính chính. Có người điều khiển trọng lự…

```text
Wide 16:9 landscape cinematic frame. three mages demonstrating different magic: one pressing the air down with gravity, one making a small explosion, one swapping two teacups, triptych composition. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Có những người mang một dấu ấn đặc biệt, và càng về sau truyện càng cho thấy dấu ấn không chỉ nói lên sức mạn…

```text
Wide 16:9 landscape cinematic frame. a mysterious double mark glowing on an ancient portrait's cheek in a dim gallery, close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Luật thứ hai: số vạch trên mặt nói lên tiềm năng. Hai vạch là rất giỏi. Ba vạch là cực hiếm, và những Thần gi…

```text
Wide 16:9 landscape cinematic frame. a close-up of a stylized face with three bright magic lines glowing on the cheek, dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Có lần Mash chặn một phép tấn công bằng cách xoay tay thật nhanh tới mức tạo ra luồng gió. Có lần cậu bơi tro…

```text
Wide 16:9 landscape cinematic frame. a young man spinning his arms so fast they blur into a whirlwind that deflects a glowing spell, humorous dynamic shot, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Luật thứ ba, luật của riêng Mash: cơ bắp thắng phép thuật, nếu đủ mạnh. Cậu chặn phép bằng tay không, phá kết…

```text
Wide 16:9 landscape cinematic frame. a young man punching straight through a glowing magical barrier, shards of light flying, dynamic low-angle shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhưng nhại lại không có nghĩa là không có luật. Mashle giữ một luật rất chặt: Mash không bao giờ tự nhiên có…

```text
Wide 16:9 landscape cinematic frame. a training log notebook filled with endless tally marks of push-ups and squats, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nghe thì vô lý, nhưng Mashle là một bộ truyện nhại lại chính các bộ truyện phép thuật. Luật thứ ba tồn tại để…

```text
Wide 16:9 landscape cinematic frame. a spell book with a big muscular arm bursting through its cover, humorous still life, bright light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Và cậu có một cách giải quyết mâu thuẫn rất riêng: nói thẳng. Nhiều kẻ thù bị bất ngờ không phải vì cú đấm, m…

```text
Wide 16:9 landscape cinematic frame. a young man calmly speaking to a startled arrogant noble student, the noble's wand drooping, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Luật thứ tư: Mash không bao giờ nói dối vì ác ý. Cậu chỉ giấu chuyện không có phép để được sống. Và cậu sẵn s…

```text
Wide 16:9 landscape cinematic frame. a young man standing protectively in front of his friends facing a powerful dark mage, back view, dramatic light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu bạn muốn biết một trận đấu trong Mashle sẽ kết thúc thế nào, hãy nhìn xem Mash đã ăn bánh s…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small cream puff icon drawn at the top of a battle diagram. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Những người bạn

Lời: Finn Ames, người bạn cùng phòng nhút nhát, có phép hoán đổi vị trí. Cậu yếu về chiến đấu nhưng thông minh và…

```text
Wide 16:9 landscape cinematic frame. a small nervous student holding a wand with two glowing swap arrows above it, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Lúc đầu Lance coi Mash là đối thủ. Nhưng sau khi chứng kiến Mash chiến đấu vì người khác, anh trở thành một t…

```text
Wide 16:9 landscape cinematic frame. two young men standing side by side on a bridge at night, one with gravity magic swirling around his hand, back view, soft moonlight. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Lance Crown, thiên tài hai vạch điều khiển trọng lực, lạnh lùng nhưng cực kỳ thương em gái.

```text
Wide 16:9 landscape cinematic frame. a cool student with two magic lines on his cheek pressing the air downward with his palm, a small locket in his other hand, medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhưng ở những trận quan trọng, Dot chứng minh mình là người đáng tin cậy nhất: đứng dậy dù đã kiệt sức, chỉ v…

```text
Wide 16:9 landscape cinematic frame. a battered student rising from rubble with small sparks flickering in his hand, determined face, dramatic low-angle shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Dot Barrett, chuyên phép nổ, ồn ào, nóng tính, và luôn thất bại trong chuyện tình cảm. Kaku không bình luận t…

```text
Wide 16:9 landscape cinematic frame. a loud student surrounded by small colorful explosions striking a dramatic pose, humorous medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Lemon Irvine, cô bạn học đã phải lòng Mash và tự xưng là vợ tương lai của cậu. Mash thì không hiểu chuyện gì…

```text
Wide 16:9 landscape cinematic frame. a cheerful girl clasping her hands with heart shapes floating around her, a confused young man eating a cream puff beside her, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku để ý: mỗi người bạn của Mash đều từng bị coi thường vì một lý do nào đó. Finn bị coi là yếu, Dot bị coi…

```text
Wide 16:9 landscape cinematic frame. four small portraits pinned on a corkboard, each with a crossed-out unfair label beneath it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Anh trai của Finn là Rayne Ames, một Thần giác giả trẻ tuổi, nổi tiếng lạnh lùng và cực mạnh. Mối quan hệ giữ…

```text
Wide 16:9 landscape cinematic frame. a tall stern young mage in a long coat standing at the top of a staircase, a smaller student looking up at him from below, low-angle shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nhóm bạn này là lý do Mash tiếp tục. Mỗi người có phép thuật, nhưng đều chọn đứng về phía một người không có…

```text
Wide 16:9 landscape cinematic frame. a group of students standing in a row on a castle bridge at sunset, arms around each other's shoulders, back view, warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Các phe

Lời: Phe thứ nhất: học viện Easton và thầy hiệu trưởng Wahlberg, người biết Mash không có phép thuật nhưng vẫn tin…

```text
Wide 16:9 landscape cinematic frame. a very old kind headmaster with a long beard smiling behind a desk piled with books, medium shot, warm office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Và bản thân các Thần giác giả cũng không giống nhau. Có người tin vào luật thanh trừng, có người âm thầm nghi…

```text
Wide 16:9 landscape cinematic frame. a council of powerful mages seated in a semicircle, some with arms crossed, some glancing at each other uneasily, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Phe thứ hai: giới cầm quyền pháp sư, những người coi luật thanh trừng là trật tự tự nhiên. Họ là lý do Mash b…

```text
Wide 16:9 landscape cinematic frame. a row of stern officials in dark robes seated at a long elevated bench, looking down, low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Ở mùa hai, một tay sai của Innocent Zero tên Cell War đã đột nhập học viện. Sau trận đấu đó, tin đồn về việc…

```text
Wide 16:9 landscape cinematic frame. a sinister figure in a long coat walking away from a damaged academy corridor, students whispering in the background, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Phe thứ ba: tổ chức Innocent Zero, kẻ thù lớn nhất. Họ cài người vào học viện, và dường như có mục tiêu liên…

```text
Wide 16:9 landscape cinematic frame. a shadowy organization emblem glowing on a dark stone wall behind hooded figures, wide shot, ominous violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mà là Mash thì sẽ lo lắng lắm. Nhưng Mash thì chắc chỉ lo cửa hàng bánh su kem hôm nay có mở không.

```text
Wide 16:9 landscape cinematic frame. the owl mascot biting its nails nervously next to a calm silhouette reading a bakery's opening hours sign. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hãy để ý rằng Innocent Zero có vẻ quan tâm tới Mash nhiều hơn mức bình thường. Kaku không spoil…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a small question mark on an organization chart next to a cream puff icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Nút thắt còn mở

Lời: Những đối thủ trong kỳ thi cuối đều là những người giỏi nhất thế hệ. Mash không chỉ phải thắng họ, mà còn phả…

```text
Wide 16:9 landscape cinematic frame. a packed arena crowd booing and cheering at the same time, one calm young man standing in the center, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Nút thắt thứ nhất: kỳ thi cuối cùng để chọn Thần giác giả sẽ diễn ra thế nào, và Mash có thể thắng mà không b…

```text
Wide 16:9 landscape cinematic frame. an enormous arena carved into a mountain with floating platforms, crowds of spectators, wide epic shot, dramatic sky. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Có một chi tiết Kaku rất muốn bạn để ý: tổ chức này có vẻ quan tâm tới thể chất và dòng máu hơn là phép thuật…

```text
Wide 16:9 landscape cinematic frame. a vial of glowing liquid on a dark laboratory table beside an old family tree scroll, close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nút thắt thứ hai: Innocent Zero muốn gì? Tổ chức này đã tấn công học viện, nhưng mục tiêu thật sự vẫn còn tro…

```text
Wide 16:9 landscape cinematic frame. a chessboard in shadow with most pieces hidden under a dark cloth, one visible piece shaped like a crown, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nếu Mash thắng, cả hệ thống xã hội dựa trên phép thuật sẽ bị đặt dấu hỏi. Đó là lý do nhiều người quyền lực m…

```text
Wide 16:9 landscape cinematic frame. a tall pyramid of glowing wand icons with a single crack starting at its base, parchment illustration, dramatic light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nút thắt thứ ba, và là câu hỏi lớn của cả bộ truyện: nếu một người không có phép thuật trở thành Thần giác gi…

```text
Wide 16:9 landscape cinematic frame. a decree scroll with the word purge being crossed out by a single muscular hand, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Ông Regro chưa bao giờ kể nhiều về ngày tìm thấy Mash. Và trong một bộ truyện nhại như Mashle, những gì không…

```text
Wide 16:9 landscape cinematic frame. an old man sitting alone by a fireplace looking at a small worn blanket in his hands, medium shot, warm flickering light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nút thắt nhỏ hơn nhưng quan trọng: Mash đến từ đâu? Vì sao một đứa trẻ bị bỏ rơi trong rừng lại có một thể ch…

```text
Wide 16:9 landscape cinematic frame. a small basket left at the edge of a dark forest under a full moon, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Ba điều nên để ý ở mùa mới · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku có một trò chơi nhỏ cho bạn: mỗi lần đối thủ tung một phép mới, hãy dừng video và đoán xem Mash sẽ phá n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pausing a video with a remote, scribbling guesses on a sticky note. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Một: để ý cách Mash giải quyết từng phép thuật. Đa số các trận, cậu không thắng bằng sức mạnh thô, mà bằng mộ…

```text
Wide 16:9 landscape cinematic frame. a diagram showing a spinning spell being stopped by a simple lever action, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Đặc biệt là hiệu trưởng Wahlberg và những Thần giác giả. Một cái gật đầu hay một cái nhíu mày của họ đôi khi…

```text
Wide 16:9 landscape cinematic frame. a close-up of an old headmaster's eyes narrowing slightly behind round spectacles, warm dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Hai: để ý những người lớn xung quanh Mash. Trong kỳ thi cuối, ai đứng về phía cậu và ai không sẽ cho bạn biết…

```text
Wide 16:9 landscape cinematic frame. several adult mage silhouettes in the audience of an arena, some leaning forward in support, others with arms crossed, medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nếu một nhân vật khác chia bánh su kem với Mash, hãy coi đó là dấu hiệu họ đã trở thành bạn thật sự. Trong Ma…

```text
Wide 16:9 landscape cinematic frame. two hands sharing a single cream puff split in half over a table, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Ba: để ý bánh su kem. Kaku không đùa đâu. Trong Mashle, bánh su kem xuất hiện ở những khoảnh khắc quan trọng…

```text
Wide 16:9 landscape cinematic frame. a single cream puff sitting on a stone windowsill overlooking a vast arena, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Góc nhìn của Kaku: vì sao Mashle hài mà sâu

Lời: Nhìn lại hai mùa, Kaku thấy Mashle làm một việc rất khéo: dùng tiếng cười để đưa người xem tới gần một câu hỏ…

```text
Wide 16:9 landscape cinematic frame. a jester's mask and a judge's gavel lying side by side on a velvet cloth, still life, warm dramatic light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Mỗi lần Mash đấm vỡ một phép thuật, ta cười. Nhưng đồng thời, ta cũng thấy một hệ thống xã hội bị đấm vỡ theo.

```text
Wide 16:9 landscape cinematic frame. a magical barrier shattering into pieces that look like fragments of an official decree, dynamic close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Và Mash không bao giờ muốn làm cách mạng. Cậu chỉ muốn được sống. Chính sự đơn giản đó khiến cậu trở thành ng…

```text
Wide 16:9 landscape cinematic frame. a calm young man eating a cream puff on a castle wall while alarms and flying messengers swirl chaotically around him, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Kaku nghĩ đây là lý do Mashle hợp với thời đại: người xem ngày nay thích những nhân vật chiến thắng bằng sự k…

```text
Wide 16:9 landscape cinematic frame. a young person training alone in an empty gym at dawn, a small poster of a muscular silhouette on the wall, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Và câu hỏi Kaku muốn để lại cho bạn: nếu bạn sống trong thế giới Mashle, bạn sẽ có mấy vạch trên mặt? Và bạn…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a face with an empty space where magic marks would be, a question mark drawn in the mist on the glass, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Kết

Lời: Mashle là một câu chuyện nghe rất ngớ ngẩn: một cậu bé dùng cơ bắp giả làm phép thuật. Nhưng bên dưới tiếng c…

```text
Wide 16:9 landscape cinematic frame. a young man standing alone on a castle rooftop at sunset looking at the academy below, a cream puff in hand, wide shot, bittersweet warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Và nếu bạn chưa xem hai mùa trước, đây là thời điểm tốt nhất để cày lại. Hai mùa chỉ khoảng hai mươi lăm tập,…

```text
Wide 16:9 landscape cinematic frame. a cozy couch with a blanket, a bowl of cream puffs and a remote, evening light through a window, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Mùa ba sẽ trả lời câu hỏi đó. Xem xong vài tập, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không nhé.

```text
Wide 16:9 landscape cinematic frame. a small note pinned to the notebook reading come back later with a tiny clock drawn beside it, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Video tiếp theo, Kaku kể chuyện một con slime nhỏ trở thành Ma vương: bậc thang tiến hóa của Rimuru trong Ten…

```text
Wide 16:9 landscape cinematic frame. a small blue gelatinous blob sitting at the bottom of a tall glowing staircase that leads to a throne, wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bài ôn tập này hữu ích, hãy đăng ký kênh để Kaku ôn tập thêm cho các bộ sắp trở lại. Kaku gấp sổ đây, hẹn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot finishing the cream puff and waving goodbye with a tiny crumb on its beak. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 82 giây · cảnh s01–s07 · 1065 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Mashle tới hết anime mùa hai, arc kỳ thi ứng viên Thần giác giả. Không có nội dung của mùa ba.

<short pause> Mùa ba của Mashle trở lại trong tháng một, sau gần ba năm chờ đợi. Nếu bạn đã quên ai là ai và vì sao một cậu bé không có phép thuật lại đang tranh danh hiệu cao quý nhất giới pháp sư, đây là bài ôn tập của bạn.

<short pause> Mashle là manga của tác giả Komoto Hajime, đăng trên Shonen Jump từ năm 2020 tới 2023. Anime mùa một ra mắt năm 2023 và nổi tiếng khắp thế giới với bài hát mở đầu mà ai nghe cũng muốn nhún nhảy.

<short pause> Đây là một bộ truyện hài nhại lại các câu chuyện học viện phép thuật nổi tiếng. <short pause> Nhưng càng về sau, nó càng có những câu hỏi rất nghiêm túc về xã hội.

<short pause> Kaku sẽ nhắc lại thế giới của Mashle, luật sức mạnh, những người bạn, các phe, và những nút thắt còn mở. Cuối video là ba điều nên để ý ở mùa mới.

<short pause> Nếu bạn chưa xem Mashle, video này vẫn giúp bạn hiểu đủ để bắt đầu. <short pause> Nhưng nhớ là có spoiler mùa một và mùa hai.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku phát bài ôn tập kèm một chiếc bánh su kem, vì thiếu bánh su kem thì không thể nói về Mashle.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Mashle tới hết anime mùa hai, arc kỳ thi ứng viên Thần giác giả. Không có nội dung của mùa ba.

[pause] Mùa ba của Mashle trở lại trong tháng một, sau gần ba năm chờ đợi. Nếu bạn đã quên ai là ai và vì sao một cậu bé không có phép thuật lại đang tranh danh hiệu cao quý nhất giới pháp sư, đây là bài ôn tập của bạn.

[pause] Mashle là manga của tác giả Komoto Hajime, đăng trên Shonen Jump từ năm 2020 tới 2023. Anime mùa một ra mắt năm 2023 và nổi tiếng khắp thế giới với bài hát mở đầu mà ai nghe cũng muốn nhún nhảy.

[pause] Đây là một bộ truyện hài nhại lại các câu chuyện học viện phép thuật nổi tiếng. [pause] Nhưng càng về sau, nó càng có những câu hỏi rất nghiêm túc về xã hội.

[pause] Kaku sẽ nhắc lại thế giới của Mashle, luật sức mạnh, những người bạn, các phe, và những nút thắt còn mở. Cuối video là ba điều nên để ý ở mùa mới.

[pause] Nếu bạn chưa xem Mashle, video này vẫn giúp bạn hiểu đủ để bắt đầu. [pause] Nhưng nhớ là có spoiler mùa một và mùa hai.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku phát bài ôn tập kèm một chiếc bánh su kem, vì thiếu bánh su kem thì không thể nói về Mashle.
```

### c02 · Thế giới: phép thuật là địa vị

Khoảng 112 giây · cảnh s08–s18 · 1457 ký tự

**Gemini**

```text
Trong thế giới Mashle, phép thuật không chỉ là năng lực. Nó là địa vị, là giai cấp, là giấy thông hành để được sống.

<short pause> Phép thuật dùng cho mọi việc trong đời sống: nấu ăn, dọn nhà, đi lại. Một người không có phép thuật sẽ không làm được những việc tưởng như đơn giản nhất.

<short pause> Và những gia đình có nhiều người sở hữu phép mạnh thì sống ở những khu cao cấp, học ở những trường danh giá, nắm giữ những vị trí quyền lực.

<short pause> Mỗi người có những vạch trên mặt, gọi là dấu ấn phép thuật. Số vạch cho biết người đó dùng được bao nhiêu loại phép. Càng nhiều vạch, càng được kính trọng.

<short pause> Kaku thấy đây là một câu chuyện rất quen: một xã hội đánh giá con người bằng một thứ họ không tự chọn được khi sinh ra.

<short pause> <laugh> Nếu có một thế giới xếp hạng theo khả năng đọc sách, Kaku chắc chắn lên ngôi. Tiếc là thế giới Mashle xếp theo phép thuật.

<short pause> Còn người không có phép thuật thì sao? Họ bị coi là khiếm khuyết của xã hội, và có thể bị thanh trừng. Không có phép thuật là một tội.

<short pause> Và nhân vật chính của chúng ta, Mash Burnedead, không có một chút phép thuật nào.

<short pause> Mash không oán hận ai. Cậu điềm tĩnh, ít nói, thẳng thắn tới mức ngây ngô, và chỉ muốn được sống yên ổn với ông và những chiếc bánh su kem.

<short pause> Nhưng một ngày, người ta phát hiện ra cậu. Và để bảo vệ ông, Mash quyết định bước vào chính cái thế giới đã muốn loại bỏ mình.

<short pause> Mash được một ông lão tên Regro nhặt về nuôi trong rừng. Để bảo vệ cậu, ông giấu cậu khỏi xã hội. Và Mash thì tập luyện cơ bắp mỗi ngày, tới mức vượt xa giới hạn con người.
```

**ElevenLabs**

```text
Trong thế giới Mashle, phép thuật không chỉ là năng lực. Nó là địa vị, là giai cấp, là giấy thông hành để được sống.

[pause] Phép thuật dùng cho mọi việc trong đời sống: nấu ăn, dọn nhà, đi lại. Một người không có phép thuật sẽ không làm được những việc tưởng như đơn giản nhất.

[pause] Và những gia đình có nhiều người sở hữu phép mạnh thì sống ở những khu cao cấp, học ở những trường danh giá, nắm giữ những vị trí quyền lực.

[pause] Mỗi người có những vạch trên mặt, gọi là dấu ấn phép thuật. Số vạch cho biết người đó dùng được bao nhiêu loại phép. Càng nhiều vạch, càng được kính trọng.

[pause] Kaku thấy đây là một câu chuyện rất quen: một xã hội đánh giá con người bằng một thứ họ không tự chọn được khi sinh ra.

[pause] [chuckles] Nếu có một thế giới xếp hạng theo khả năng đọc sách, Kaku chắc chắn lên ngôi. Tiếc là thế giới Mashle xếp theo phép thuật.

[pause] [curious] Còn người không có phép thuật thì sao? Họ bị coi là khiếm khuyết của xã hội, và có thể bị thanh trừng. Không có phép thuật là một tội.

[pause] Và nhân vật chính của chúng ta, Mash Burnedead, không có một chút phép thuật nào.

[pause] Mash không oán hận ai. Cậu điềm tĩnh, ít nói, thẳng thắn tới mức ngây ngô, và chỉ muốn được sống yên ổn với ông và những chiếc bánh su kem.

[pause] Nhưng một ngày, người ta phát hiện ra cậu. Và để bảo vệ ông, Mash quyết định bước vào chính cái thế giới đã muốn loại bỏ mình.

[pause] Mash được một ông lão tên Regro nhặt về nuôi trong rừng. Để bảo vệ cậu, ông giấu cậu khỏi xã hội. Và Mash thì tập luyện cơ bắp mỗi ngày, tới mức vượt xa giới hạn con người.
```

### c03 · Tình hình hiện tại: từ học viện tới án tử

Khoảng 146 giây · cảnh s19–s30 · 1894 ký tự

**Gemini**

```text
Để cha nuôi được sống yên ổn, Mash vào học viện phép thuật Easton với một mục tiêu duy nhất: trở thành Thần giác giả, danh hiệu cao quý nhất giới pháp sư. Một Thần giác giả có quyền lực đủ để bảo vệ gia đình mình.

<short pause> Ngay trong kỳ thi đầu vào, Mash đã gây chấn động. Những bài thi cần phép thuật, cậu giải bằng sức mạnh và sự lì lợm, khiến giám khảo không biết nên cho điểm thế nào.

<short pause> Cậu được xếp vào ký túc xá Adler. Và từ ngày đầu, những học sinh quý tộc đã coi cậu là cái gai trong mắt.

<short pause> Cậu vượt qua kỳ thi đầu vào, rồi mọi thử thách trong học viện, bằng cơ bắp nhưng giả vờ như đó là phép thuật. Đập vỡ quả cầu, bay bằng cách nhảy, bẻ cong luật bằng sức mạnh.

<short pause> Đồng xu được trao cho những thành tích đặc biệt: đánh bại kẻ thù nguy hiểm, cứu người, hoàn thành nhiệm vụ khó. Với Mash, mỗi đồng xu là thêm một bước gần tới sự an toàn cho gia đình.

<short pause> Trong học viện, học sinh thu thập những đồng xu vàng. Ai có đủ số đồng xu sẽ trở thành ứng viên Thần giác giả.

<short pause> Trong những trận đấu đó, Mash lần đầu gặp những đối thủ thật sự nguy hiểm, những người sẵn sàng làm tổn thương bạn bè cậu chỉ để chứng minh đẳng cấp.

<short pause> Mùa một kết thúc với những trận đấu giữa ký túc xá Adler của Mash và ký túc xá Lang, cùng sự xuất hiện của một tổ chức bí ẩn tên là Innocent Zero.

<short pause> Thầy hiệu trưởng Wahlberg là người đứng ra bảo vệ cậu. Ông đưa ra điều kiện: nếu Mash trở thành ứng viên Thần giác giả, cậu sẽ có đủ vị thế để không ai động tới được.

<short pause> Kỳ thi ứng viên giống một giải đấu thật sự: những trận đấu một chọi một, những thử thách đồng đội, và những đối thủ đều là thiên tài của thế hệ.

<short pause> Sang mùa hai, bí mật của Mash bị lộ. Cậu bị kết án, và cách duy nhất để thoát là trở thành ứng viên Thần giác giả trước khi hết năm. Thế là cậu bước vào kỳ thi dành cho những pháp sư ưu tú nhất.

<short pause> Mash cùng các bạn đánh bại nhóm Magia Lupus, giành được đồng xu của ký túc xá Lang, và tiến thêm một bước gần danh hiệu. Đó là nơi mùa ba bắt đầu.
```

**ElevenLabs**

```text
Để cha nuôi được sống yên ổn, Mash vào học viện phép thuật Easton với một mục tiêu duy nhất: trở thành Thần giác giả, danh hiệu cao quý nhất giới pháp sư. Một Thần giác giả có quyền lực đủ để bảo vệ gia đình mình.

[pause] Ngay trong kỳ thi đầu vào, Mash đã gây chấn động. Những bài thi cần phép thuật, cậu giải bằng sức mạnh và sự lì lợm, khiến giám khảo không biết nên cho điểm thế nào.

[pause] Cậu được xếp vào ký túc xá Adler. Và từ ngày đầu, những học sinh quý tộc đã coi cậu là cái gai trong mắt.

[pause] Cậu vượt qua kỳ thi đầu vào, rồi mọi thử thách trong học viện, bằng cơ bắp nhưng giả vờ như đó là phép thuật. Đập vỡ quả cầu, bay bằng cách nhảy, bẻ cong luật bằng sức mạnh.

[pause] Đồng xu được trao cho những thành tích đặc biệt: đánh bại kẻ thù nguy hiểm, cứu người, hoàn thành nhiệm vụ khó. Với Mash, mỗi đồng xu là thêm một bước gần tới sự an toàn cho gia đình.

[pause] Trong học viện, học sinh thu thập những đồng xu vàng. Ai có đủ số đồng xu sẽ trở thành ứng viên Thần giác giả.

[pause] Trong những trận đấu đó, Mash lần đầu gặp những đối thủ thật sự nguy hiểm, những người sẵn sàng làm tổn thương bạn bè cậu chỉ để chứng minh đẳng cấp.

[pause] Mùa một kết thúc với những trận đấu giữa ký túc xá Adler của Mash và ký túc xá Lang, cùng sự xuất hiện của một tổ chức bí ẩn tên là Innocent Zero.

[pause] Thầy hiệu trưởng Wahlberg là người đứng ra bảo vệ cậu. Ông đưa ra điều kiện: nếu Mash trở thành ứng viên Thần giác giả, cậu sẽ có đủ vị thế để không ai động tới được.

[pause] Kỳ thi ứng viên giống một giải đấu thật sự: những trận đấu một chọi một, những thử thách đồng đội, và những đối thủ đều là thiên tài của thế hệ.

[pause] Sang mùa hai, bí mật của Mash bị lộ. Cậu bị kết án, và cách duy nhất để thoát là trở thành ứng viên Thần giác giả trước khi hết năm. Thế là cậu bước vào kỳ thi dành cho những pháp sư ưu tú nhất.

[pause] Mash cùng các bạn đánh bại nhóm Magia Lupus, giành được đồng xu của ký túc xá Lang, và tiến thêm một bước gần danh hiệu. Đó là nơi mùa ba bắt đầu.
```

### c04 · Luật sức mạnh cần nhớ

Khoảng 137 giây · cảnh s31–s41 · 1780 ký tự

**Gemini**

```text
Pháp sư dùng đũa để tập trung và giải phóng phép. Họ đọc thần chú, vung đũa, và phép thuật xuất hiện. Mash thì không có đũa nào hoạt động, nên cậu dùng… tay.

<short pause> Luật thứ nhất: phép thuật trong Mashle mỗi người thường có một thuộc tính chính. Có người điều khiển trọng lực, có người tạo vụ nổ, có người hoán đổi vị trí các vật.

<short pause> Có những người mang một dấu ấn đặc biệt, và càng về sau truyện càng cho thấy dấu ấn không chỉ nói lên sức mạnh, mà còn có thể nói lên dòng dõi. Kaku dừng ở đây để không spoiler.

<short pause> Luật thứ hai: số vạch trên mặt nói lên tiềm năng. Hai vạch là rất giỏi. Ba vạch là cực hiếm, và những Thần giác giả thường ở mức đó.

<short pause> Có lần Mash chặn một phép tấn công bằng cách xoay tay thật nhanh tới mức tạo ra luồng gió. Có lần cậu bơi trong không khí. Truyện không cần giải thích, chỉ cần bạn cười.

<short pause> Luật thứ ba, luật của riêng Mash: cơ bắp thắng phép thuật, nếu đủ mạnh. Cậu chặn phép bằng tay không, phá kết giới bằng cú đấm, và dùng tốc độ để né mọi thứ.

<short pause> Nhưng nhại lại không có nghĩa là không có luật. Mashle giữ một luật rất chặt: Mash không bao giờ tự nhiên có phép thuật. Cậu mạnh lên chỉ bằng tập luyện. Đó là lời hứa của tác giả với người đọc.

<short pause> Nghe thì vô lý, nhưng Mashle là một bộ truyện nhại lại chính các bộ truyện phép thuật. Luật thứ ba tồn tại để chế giễu một thế giới coi phép thuật là tất cả.

<short pause> Và cậu có một cách giải quyết mâu thuẫn rất riêng: nói thẳng. Nhiều kẻ thù bị bất ngờ không phải vì cú đấm, mà vì Mash nói ra đúng điều họ không muốn nghe.

<short pause> Luật thứ tư: Mash không bao giờ nói dối vì ác ý. Cậu chỉ giấu chuyện không có phép để được sống. Và cậu sẵn sàng liều mạng vì bạn bè ngay khi họ gặp nguy.

<short pause> <laugh> Kaku ghi chú: nếu bạn muốn biết một trận đấu trong Mashle sẽ kết thúc thế nào, hãy nhìn xem Mash đã ăn bánh su kem chưa. Ăn rồi thì đối thủ nên chuẩn bị tinh thần.
```

**ElevenLabs**

```text
Pháp sư dùng đũa để tập trung và giải phóng phép. Họ đọc thần chú, vung đũa, và phép thuật xuất hiện. Mash thì không có đũa nào hoạt động, nên cậu dùng… tay.

[pause] Luật thứ nhất: phép thuật trong Mashle mỗi người thường có một thuộc tính chính. Có người điều khiển trọng lực, có người tạo vụ nổ, có người hoán đổi vị trí các vật.

[pause] Có những người mang một dấu ấn đặc biệt, và càng về sau truyện càng cho thấy dấu ấn không chỉ nói lên sức mạnh, mà còn có thể nói lên dòng dõi. Kaku dừng ở đây để không spoiler.

[pause] Luật thứ hai: số vạch trên mặt nói lên tiềm năng. Hai vạch là rất giỏi. Ba vạch là cực hiếm, và những Thần giác giả thường ở mức đó.

[pause] Có lần Mash chặn một phép tấn công bằng cách xoay tay thật nhanh tới mức tạo ra luồng gió. Có lần cậu bơi trong không khí. Truyện không cần giải thích, chỉ cần bạn cười.

[pause] Luật thứ ba, luật của riêng Mash: cơ bắp thắng phép thuật, nếu đủ mạnh. Cậu chặn phép bằng tay không, phá kết giới bằng cú đấm, và dùng tốc độ để né mọi thứ.

[pause] Nhưng nhại lại không có nghĩa là không có luật. Mashle giữ một luật rất chặt: Mash không bao giờ tự nhiên có phép thuật. Cậu mạnh lên chỉ bằng tập luyện. Đó là lời hứa của tác giả với người đọc.

[pause] Nghe thì vô lý, nhưng Mashle là một bộ truyện nhại lại chính các bộ truyện phép thuật. Luật thứ ba tồn tại để chế giễu một thế giới coi phép thuật là tất cả.

[pause] Và cậu có một cách giải quyết mâu thuẫn rất riêng: nói thẳng. Nhiều kẻ thù bị bất ngờ không phải vì cú đấm, mà vì Mash nói ra đúng điều họ không muốn nghe.

[pause] Luật thứ tư: Mash không bao giờ nói dối vì ác ý. Cậu chỉ giấu chuyện không có phép để được sống. Và cậu sẵn sàng liều mạng vì bạn bè ngay khi họ gặp nguy.

[pause] [chuckles] Kaku ghi chú: nếu bạn muốn biết một trận đấu trong Mashle sẽ kết thúc thế nào, hãy nhìn xem Mash đã ăn bánh su kem chưa. Ăn rồi thì đối thủ nên chuẩn bị tinh thần.
```

### c05 · Những người bạn

Khoảng 94 giây · cảnh s42–s50 · 1224 ký tự

**Gemini**

```text
Finn Ames, người bạn cùng phòng nhút nhát, có phép hoán đổi vị trí. Cậu yếu về chiến đấu nhưng thông minh và luôn đi theo Mash.

<short pause> Lúc đầu Lance coi Mash là đối thủ. <short pause> Nhưng sau khi chứng kiến Mash chiến đấu vì người khác, anh trở thành một trong những đồng minh đáng tin nhất.

<short pause> Lance Crown, thiên tài hai vạch điều khiển trọng lực, lạnh lùng nhưng cực kỳ thương em gái.

<short pause> Nhưng ở những trận quan trọng, Dot chứng minh mình là người đáng tin cậy nhất: đứng dậy dù đã kiệt sức, chỉ vì không muốn bạn mình phải chiến đấu một mình.

<short pause> Dot Barrett, chuyên phép nổ, ồn ào, nóng tính, và luôn thất bại trong chuyện tình cảm. Kaku không bình luận thêm.

<short pause> Lemon Irvine, cô bạn học đã phải lòng Mash và tự xưng là vợ tương lai của cậu. Mash thì không hiểu chuyện gì đang xảy ra.

<short pause> Kaku để ý: mỗi người bạn của Mash đều từng bị coi thường vì một lý do nào đó. Finn bị coi là yếu, Dot bị coi là ồn ào, Lance bị coi là lạnh lùng. Họ hiểu cảm giác bị đánh giá sai.

<short pause> Anh trai của Finn là Rayne Ames, một Thần giác giả trẻ tuổi, nổi tiếng lạnh lùng và cực mạnh. Mối quan hệ giữa hai anh em là một trong những mạch truyện cảm động của mùa hai.

<short pause> Nhóm bạn này là lý do Mash tiếp tục. Mỗi người có phép thuật, nhưng đều chọn đứng về phía một người không có phép thuật.
```

**ElevenLabs**

```text
Finn Ames, người bạn cùng phòng nhút nhát, có phép hoán đổi vị trí. Cậu yếu về chiến đấu nhưng thông minh và luôn đi theo Mash.

[pause] Lúc đầu Lance coi Mash là đối thủ. [pause] Nhưng sau khi chứng kiến Mash chiến đấu vì người khác, anh trở thành một trong những đồng minh đáng tin nhất.

[pause] Lance Crown, thiên tài hai vạch điều khiển trọng lực, lạnh lùng nhưng cực kỳ thương em gái.

[pause] Nhưng ở những trận quan trọng, Dot chứng minh mình là người đáng tin cậy nhất: đứng dậy dù đã kiệt sức, chỉ vì không muốn bạn mình phải chiến đấu một mình.

[pause] Dot Barrett, chuyên phép nổ, ồn ào, nóng tính, và luôn thất bại trong chuyện tình cảm. Kaku không bình luận thêm.

[pause] Lemon Irvine, cô bạn học đã phải lòng Mash và tự xưng là vợ tương lai của cậu. Mash thì không hiểu chuyện gì đang xảy ra.

[pause] Kaku để ý: mỗi người bạn của Mash đều từng bị coi thường vì một lý do nào đó. Finn bị coi là yếu, Dot bị coi là ồn ào, Lance bị coi là lạnh lùng. Họ hiểu cảm giác bị đánh giá sai.

[pause] Anh trai của Finn là Rayne Ames, một Thần giác giả trẻ tuổi, nổi tiếng lạnh lùng và cực mạnh. Mối quan hệ giữa hai anh em là một trong những mạch truyện cảm động của mùa hai.

[pause] Nhóm bạn này là lý do Mash tiếp tục. Mỗi người có phép thuật, nhưng đều chọn đứng về phía một người không có phép thuật.
```

### c06 · Các phe

Khoảng 73 giây · cảnh s51–s57 · 955 ký tự

**Gemini**

```text
Phe thứ nhất: học viện Easton và thầy hiệu trưởng Wahlberg, người biết Mash không có phép thuật nhưng vẫn tin vào cậu.

<short pause> Và bản thân các Thần giác giả cũng không giống nhau. Có người tin vào luật thanh trừng, có người âm thầm nghi ngờ nó. Kỳ thi cuối sẽ cho ta thấy họ đứng ở đâu.

<short pause> Phe thứ hai: giới cầm quyền pháp sư, những người coi luật thanh trừng là trật tự tự nhiên. Họ là lý do Mash bị kết án.

<short pause> Ở mùa hai, một tay sai của Innocent Zero tên Cell War đã đột nhập học viện. Sau trận đấu đó, tin đồn về việc Mash không có phép thuật bắt đầu lan ra khắp trường.

<short pause> Phe thứ ba: tổ chức Innocent Zero, kẻ thù lớn nhất. Họ cài người vào học viện, và dường như có mục tiêu liên quan tới chính những học sinh có tiềm năng đặc biệt.

<short pause> <laugh> Kaku mà là Mash thì sẽ lo lắng lắm. <short pause> Nhưng Mash thì chắc chỉ lo cửa hàng bánh su kem hôm nay có mở không.

<short pause> Kaku ghi chú: hãy để ý rằng Innocent Zero có vẻ quan tâm tới Mash nhiều hơn mức bình thường. Kaku không spoiler, chỉ khuyên bạn chú ý.
```

**ElevenLabs**

```text
Phe thứ nhất: học viện Easton và thầy hiệu trưởng Wahlberg, người biết Mash không có phép thuật nhưng vẫn tin vào cậu.

[pause] Và bản thân các Thần giác giả cũng không giống nhau. Có người tin vào luật thanh trừng, có người âm thầm nghi ngờ nó. Kỳ thi cuối sẽ cho ta thấy họ đứng ở đâu.

[pause] Phe thứ hai: giới cầm quyền pháp sư, những người coi luật thanh trừng là trật tự tự nhiên. Họ là lý do Mash bị kết án.

[pause] Ở mùa hai, một tay sai của Innocent Zero tên Cell War đã đột nhập học viện. Sau trận đấu đó, tin đồn về việc Mash không có phép thuật bắt đầu lan ra khắp trường.

[pause] Phe thứ ba: tổ chức Innocent Zero, kẻ thù lớn nhất. Họ cài người vào học viện, và dường như có mục tiêu liên quan tới chính những học sinh có tiềm năng đặc biệt.

[pause] [chuckles] Kaku mà là Mash thì sẽ lo lắng lắm. [pause] Nhưng Mash thì chắc chỉ lo cửa hàng bánh su kem hôm nay có mở không.

[pause] Kaku ghi chú: hãy để ý rằng Innocent Zero có vẻ quan tâm tới Mash nhiều hơn mức bình thường. Kaku không spoiler, chỉ khuyên bạn chú ý.
```

### c07 · Nút thắt còn mở

Khoảng 86 giây · cảnh s58–s65 · 1123 ký tự

**Gemini**

```text
Những đối thủ trong kỳ thi cuối đều là những người giỏi nhất thế hệ. Mash không chỉ phải thắng họ, mà còn phải thắng định kiến của cả khán đài.

<short pause> Nút thắt thứ nhất: kỳ thi cuối cùng để chọn Thần giác giả sẽ diễn ra thế nào, và Mash có thể thắng mà không bị lộ, hoặc không cần giấu nữa?

<short pause> Có một chi tiết Kaku rất muốn bạn để ý: tổ chức này có vẻ quan tâm tới thể chất và dòng máu hơn là phép thuật. Tại sao? Mùa ba sẽ trả lời.

<short pause> Nút thắt thứ hai: Innocent Zero muốn gì? Tổ chức này đã tấn công học viện, nhưng mục tiêu thật sự vẫn còn trong bóng tối.

<short pause> Nếu Mash thắng, cả hệ thống xã hội dựa trên phép thuật sẽ bị đặt dấu hỏi. Đó là lý do nhiều người quyền lực muốn cậu thua, bất kể cậu tốt hay xấu.

<short pause> Nút thắt thứ ba, và là câu hỏi lớn của cả bộ truyện: nếu một người không có phép thuật trở thành Thần giác giả, thì luật thanh trừng còn ý nghĩa gì?

<short pause> Ông Regro chưa bao giờ kể nhiều về ngày tìm thấy Mash. Và trong một bộ truyện nhại như Mashle, những gì không được nói ra thường là những gì quan trọng nhất.

<short pause> Nút thắt nhỏ hơn nhưng quan trọng: Mash đến từ đâu? Vì sao một đứa trẻ bị bỏ rơi trong rừng lại có một thể chất phi thường như vậy?
```

**ElevenLabs**

```text
Những đối thủ trong kỳ thi cuối đều là những người giỏi nhất thế hệ. Mash không chỉ phải thắng họ, mà còn phải thắng định kiến của cả khán đài.

[pause] [curious] Nút thắt thứ nhất: kỳ thi cuối cùng để chọn Thần giác giả sẽ diễn ra thế nào, và Mash có thể thắng mà không bị lộ, hoặc không cần giấu nữa?

[pause] Có một chi tiết Kaku rất muốn bạn để ý: tổ chức này có vẻ quan tâm tới thể chất và dòng máu hơn là phép thuật. Tại sao? Mùa ba sẽ trả lời.

[pause] Nút thắt thứ hai: Innocent Zero muốn gì? Tổ chức này đã tấn công học viện, nhưng mục tiêu thật sự vẫn còn trong bóng tối.

[pause] Nếu Mash thắng, cả hệ thống xã hội dựa trên phép thuật sẽ bị đặt dấu hỏi. Đó là lý do nhiều người quyền lực muốn cậu thua, bất kể cậu tốt hay xấu.

[pause] Nút thắt thứ ba, và là câu hỏi lớn của cả bộ truyện: nếu một người không có phép thuật trở thành Thần giác giả, thì luật thanh trừng còn ý nghĩa gì?

[pause] Ông Regro chưa bao giờ kể nhiều về ngày tìm thấy Mash. Và trong một bộ truyện nhại như Mashle, những gì không được nói ra thường là những gì quan trọng nhất.

[pause] Nút thắt nhỏ hơn nhưng quan trọng: Mash đến từ đâu? Vì sao một đứa trẻ bị bỏ rơi trong rừng lại có một thể chất phi thường như vậy?
```

### c08 · Ba điều nên để ý ở mùa mới / Góc nhìn của Kaku: vì sao Mashle hài mà sâu

Khoảng 127 giây · cảnh s66–s76 · 1655 ký tự

**Gemini**

```text
<laugh> Kaku có một trò chơi nhỏ cho bạn: mỗi lần đối thủ tung một phép mới, hãy dừng video và đoán xem Mash sẽ phá nó bằng cách nào. Kaku đoán đúng khoảng một nửa.

<short pause> Một: để ý cách Mash giải quyết từng phép thuật. Đa số các trận, cậu không thắng bằng sức mạnh thô, mà bằng một ý tưởng vật lý đơn giản tới mức buồn cười.

<short pause> Đặc biệt là hiệu trưởng Wahlberg và những Thần giác giả. Một cái gật đầu hay một cái nhíu mày của họ đôi khi nói nhiều hơn cả trận đấu.

<short pause> Hai: để ý những người lớn xung quanh Mash. Trong kỳ thi cuối, ai đứng về phía cậu và ai không sẽ cho bạn biết thế giới này sắp thay đổi theo hướng nào.

<short pause> Nếu một nhân vật khác chia bánh su kem với Mash, hãy coi đó là dấu hiệu họ đã trở thành bạn thật sự. Trong Mashle, đó là nghi thức kết nghĩa.

<short pause> Ba: để ý bánh su kem. Kaku không đùa đâu. Trong Mashle, bánh su kem xuất hiện ở những khoảnh khắc quan trọng nhất, như một lời nhắc về những niềm vui giản dị mà Mash chiến đấu để giữ.

<short pause> Nhìn lại hai mùa, Kaku thấy Mashle làm một việc rất khéo: dùng tiếng cười để đưa người xem tới gần một câu hỏi khó mà không thấy nặng nề.

<short pause> Mỗi lần Mash đấm vỡ một phép thuật, ta cười. <short pause> Nhưng đồng thời, ta cũng thấy một hệ thống xã hội bị đấm vỡ theo.

<short pause> Và Mash không bao giờ muốn làm cách mạng. Cậu chỉ muốn được sống. Chính sự đơn giản đó khiến cậu trở thành người thách thức lớn nhất của cả hệ thống.

<short pause> Kaku nghĩ đây là lý do Mashle hợp với thời đại: người xem ngày nay thích những nhân vật chiến thắng bằng sự kiên trì của bản thân, không phải bằng dòng máu hay năng lực trời cho.

<short pause> Và câu hỏi Kaku muốn để lại cho bạn: nếu bạn sống trong thế giới Mashle, bạn sẽ có mấy vạch trên mặt? Và bạn có dám kết bạn với một người không có vạch nào không?
```

**ElevenLabs**

```text
[chuckles] Kaku có một trò chơi nhỏ cho bạn: mỗi lần đối thủ tung một phép mới, hãy dừng video và đoán xem Mash sẽ phá nó bằng cách nào. Kaku đoán đúng khoảng một nửa.

[pause] Một: để ý cách Mash giải quyết từng phép thuật. Đa số các trận, cậu không thắng bằng sức mạnh thô, mà bằng một ý tưởng vật lý đơn giản tới mức buồn cười.

[pause] Đặc biệt là hiệu trưởng Wahlberg và những Thần giác giả. Một cái gật đầu hay một cái nhíu mày của họ đôi khi nói nhiều hơn cả trận đấu.

[pause] Hai: để ý những người lớn xung quanh Mash. Trong kỳ thi cuối, ai đứng về phía cậu và ai không sẽ cho bạn biết thế giới này sắp thay đổi theo hướng nào.

[pause] Nếu một nhân vật khác chia bánh su kem với Mash, hãy coi đó là dấu hiệu họ đã trở thành bạn thật sự. Trong Mashle, đó là nghi thức kết nghĩa.

[pause] Ba: để ý bánh su kem. Kaku không đùa đâu. Trong Mashle, bánh su kem xuất hiện ở những khoảnh khắc quan trọng nhất, như một lời nhắc về những niềm vui giản dị mà Mash chiến đấu để giữ.

[pause] Nhìn lại hai mùa, Kaku thấy Mashle làm một việc rất khéo: dùng tiếng cười để đưa người xem tới gần một câu hỏi khó mà không thấy nặng nề.

[pause] Mỗi lần Mash đấm vỡ một phép thuật, ta cười. [pause] Nhưng đồng thời, ta cũng thấy một hệ thống xã hội bị đấm vỡ theo.

[pause] Và Mash không bao giờ muốn làm cách mạng. Cậu chỉ muốn được sống. Chính sự đơn giản đó khiến cậu trở thành người thách thức lớn nhất của cả hệ thống.

[pause] Kaku nghĩ đây là lý do Mashle hợp với thời đại: người xem ngày nay thích những nhân vật chiến thắng bằng sự kiên trì của bản thân, không phải bằng dòng máu hay năng lực trời cho.

[pause] [curious] Và câu hỏi Kaku muốn để lại cho bạn: nếu bạn sống trong thế giới Mashle, bạn sẽ có mấy vạch trên mặt? Và bạn có dám kết bạn với một người không có vạch nào không?
```

### c09 · Kết

Khoảng 54 giây · cảnh s77–s81 · 702 ký tự

**Gemini**

```text
Mashle là một câu chuyện nghe rất ngớ ngẩn: một cậu bé dùng cơ bắp giả làm phép thuật. <short pause> Nhưng bên dưới tiếng cười là một câu hỏi nghiêm túc: xã hội có quyền quyết định ai đáng được sống chỉ vì một năng lực bẩm sinh không?

<short pause> Và nếu bạn chưa xem hai mùa trước, đây là thời điểm tốt nhất để cày lại. Hai mùa chỉ khoảng hai mươi lăm tập, đủ cho vài buổi tối.

<short pause> Mùa ba sẽ trả lời câu hỏi đó. Xem xong vài tập, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không nhé.

<short pause> Video tiếp theo, Kaku kể chuyện một con slime nhỏ trở thành Ma vương: bậc thang tiến hóa của Rimuru trong Tensura, từng nấc một.

<short pause> <laugh> Nếu bài ôn tập này hữu ích, hãy đăng ký kênh để Kaku ôn tập thêm cho các bộ sắp trở lại. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Mashle là một câu chuyện nghe rất ngớ ngẩn: một cậu bé dùng cơ bắp giả làm phép thuật. [pause] [curious] Nhưng bên dưới tiếng cười là một câu hỏi nghiêm túc: xã hội có quyền quyết định ai đáng được sống chỉ vì một năng lực bẩm sinh không?

[pause] Và nếu bạn chưa xem hai mùa trước, đây là thời điểm tốt nhất để cày lại. Hai mùa chỉ khoảng hai mươi lăm tập, đủ cho vài buổi tối.

[pause] Mùa ba sẽ trả lời câu hỏi đó. Xem xong vài tập, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không nhé.

[pause] Video tiếp theo, Kaku kể chuyện một con slime nhỏ trở thành Ma vương: bậc thang tiến hóa của Rimuru trong Tensura, từng nấc một.

[pause] [chuckles] Nếu bài ôn tập này hữu ích, hãy đăng ký kênh để Kaku ôn tập thêm cho các bộ sắp trở lại. Kaku gấp sổ đây, hẹn gặp lại!
```
