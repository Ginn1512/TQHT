# Bộ prompt · Blue Lock: Xếp hạng 10 vũ khí của các tiền đạo — ba tiêu chí, một luật hòa

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 88 ảnh, 7 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói về vũ khí của các tiền đạo Blue Lock tới hết giải U-20 và phần Neo Egoist Lea…

```text
Wide 16:9 landscape cinematic frame. a football resting on a locker room bench beside a spoiler warning card, close-up, cool fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Ba trăm tiền đạo trẻ bị nhốt vào một cơ sở huấn luyện. Chỉ một người được bước ra làm tiền đạo số một của Nhậ…

```text
Wide 16:9 landscape cinematic frame. a massive futuristic training facility at night with rows of lit windows and a single door glowing at the end, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Vũ khí ở đây không phải dao kiếm. Đó là một kỹ năng mà chỉ bạn có, và đủ sắc để ghi bàn ở bất kỳ trận đấu nào.

```text
Wide 16:9 landscape cinematic frame. a football boot placed on a velvet cushion like a treasured sword in a display case, dramatic close-up, spotlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku xếp hạng mười vũ khí của các tiền đạo Blue Lock, từ hạng mười lên hạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot in a referee shirt holding a clipboard with a whistle around its neck. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và Kaku nói trước: bảng này xếp hạng vũ khí, không xếp hạng người. Một cầu thủ có vũ khí hạng thấp vẫn có thể…

```text
Wide 16:9 landscape cinematic frame. a row of ten small numbered trophies on a shelf, some plain and some ornate, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Blue Lock là gì?

Lời: Trong truyện, sau khi đội tuyển Nhật Bản bị loại ở World Cup 2018, Liên đoàn bóng đá mở một dự án đặc biệt tê…

```text
Wide 16:9 landscape cinematic frame. an empty stadium at night with a scoreboard showing a loss and confetti swept into a corner, wide shot, melancholy stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Nhân vật chính Isagi bước vào Blue Lock sau một trận đấu ở trường: ở khoảnh khắc quyết định, cậu chuyền bóng…

```text
Wide 16:9 landscape cinematic frame. a high school pitch with a ball rolling past a post and a figure staring at their own feet, wide shot, grey overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Người đứng đầu dự án là Ego Jinpachi, một huấn luyện viên kỳ quặc với một triết lý: Nhật Bản thiếu một tiền đ…

```text
Wide 16:9 landscape cinematic frame. a thin shadowy silhouette with glasses glinting behind a bank of monitors in a dark control room, medium shot, cold screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ego nói, đại ý, rằng mỗi tiền đạo phải tìm ra vũ khí của mình, rồi tìm công thức để ghi bàn bằng vũ khí đó. V…

```text
Wide 16:9 landscape cinematic frame. a chalkboard with a simple equation: a sword icon plus a gear icon equals a football in a net, amber chalk close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Luật chơi rất khắc nghiệt: ai thua sẽ bị loại, và theo luật dự án, không bao giờ được khoác áo đội tuyển quốc…

```text
Wide 16:9 landscape cinematic frame. a locker being slowly closed with a name tag removed from its door, close-up, harsh fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Blue Lock biến bóng đá thành một trò chơi sinh tồn. Và trong trò chơi sinh tồn, thứ quý nhất chính…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking nervously out of a locker holding a football. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Ba tiêu chí chấm điểm

Lời: Tiêu chí một: sát thương. Vũ khí này trực tiếp tạo ra bàn thắng tới mức nào? Chấm từ một tới năm.

```text
Wide 16:9 landscape cinematic frame. a scorecard on parchment with a first row labeled with a football-in-net icon and five empty stars, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Tiêu chí hai: độc nhất. Người khác có dễ học theo, dễ sao chép không? Càng khó sao chép, điểm càng cao.

```text
Wide 16:9 landscape cinematic frame. a fingerprint drawn in ink beside a crossed-out photocopier icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Tiêu chí ba: tiến hóa. Vũ khí này còn lớn lên được không, hay đã chạm trần? Blue Lock là câu chuyện về tiến h…

```text
Wide 16:9 landscape cinematic frame. a small seedling growing into a tall tree drawn in stages across the page, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Tổng điểm tối đa là mười lăm. Và luật hòa: nếu hai vũ khí bằng điểm, vũ khí có điểm tiến hóa cao hơn xếp trên.

```text
Wide 16:9 landscape cinematic frame. a small balance scale with a seedling tipping one side down, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Điểm là cảm nhận của Kaku, dựa trên những gì truyện cho thấy. Bạn hoàn toàn có thể chấm khác, và Kaku muốn ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a pencil with a playful wink beside a blank scorecard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Hạng 10: cơ thể dẻo như cao su

Lời: Hạng mười thuộc về Gagamaru, thành viên đội Z. Vũ khí của cậu là một cơ thể dẻo khác thường, có thể vươn tới…

```text
Wide 16:9 landscape cinematic frame. a lanky figure twisting into an impossible stretching pose to reach a flying football, dynamic wide shot, bright stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Trong những trận đầu, Gagamaru thậm chí đứng khung thành cho cả đội, vì phản xạ và độ dẻo của cậu hợp với vị…

```text
Wide 16:9 landscape cinematic frame. a figure diving across a goal mouth with limbs stretched in an odd angle, dynamic close-up, harsh floodlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Sát thương: hai điểm. Cơ thể dẻo giúp chạm bóng, nhưng bản thân nó không ghi bàn. Độc nhất: bốn điểm, vì khôn…

```text
Wide 16:9 landscape cinematic frame. a scorecard with two stars in the first row and four stars in the second row, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Tiến hóa: một điểm. Truyện chưa cho thấy vũ khí này phát triển thêm. Tổng: bảy điểm.

```text
Wide 16:9 landscape cinematic frame. the third row of the scorecard with a single star and a total of seven circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kaku để ý: một vũ khí độc nhất nhưng không lớn lên được, cuối cùng sẽ bị bỏ lại trong một nơi mà ai cũng tiến…

```text
Wide 16:9 landscape cinematic frame. a single old trophy gathering dust on a shelf while newer ones shine beside it, close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Hạng 9: tắc kè hoa

Lời: Hạng chín là Mikage Reo. Cậu xuất thân từ gia đình giàu có, và vũ khí cậu tìm ra là khả năng sao chép: quan s…

```text
Wide 16:9 landscape cinematic frame. a chameleon on a branch changing its colors to match different patterned cards around it, extreme close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Lúc đầu Reo không có vũ khí riêng. Cậu chỉ là cộng sự của một thiên tài. Chính việc bị bỏ lại đã buộc cậu tìm…

```text
Wide 16:9 landscape cinematic frame. a figure standing alone on an empty training pitch watching a distant partner walk away, wide shot, grey overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Sát thương: hai điểm. Bản sao thường yếu hơn bản gốc. Độc nhất: ba điểm. Sao chép thì ai cũng có thể thử, như…

```text
Wide 16:9 landscape cinematic frame. a scorecard with two stars and three stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Tiến hóa: ba điểm. Mỗi người mới cậu gặp là một vũ khí mới cậu có thể học. Tổng: tám điểm.

```text
Wide 16:9 landscape cinematic frame. the scorecard total of eight circled with a small chameleon doodle beside it, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: vũ khí của Reo là chiếc gương của cả Blue Lock. Nó cho thấy ai là người đáng học nhất.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking into a hand mirror that reflects several different football poses. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Hạng 8: tốc độ

Lời: Hạng tám là Chigiri Hyoma, và vũ khí đơn giản nhất: tốc độ. Khi có khoảng trống, không ai đuổi kịp cậu.

```text
Wide 16:9 landscape cinematic frame. a blur of a runner with long hair streaming behind sprinting along the sideline, dynamic wide shot, bright stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nhưng Chigiri từng bị chấn thương đầu gối nặng, và cậu sợ phải chạy hết sức một lần nữa. Vũ khí mạnh nhất của…

```text
Wide 16:9 landscape cinematic frame. a knee brace lying on a bench in an empty locker room, close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Khoảnh khắc Chigiri quyết định chạy hết sức, dù biết có thể lại đau, là một trong những cảnh đáng nhớ nhất củ…

```text
Wide 16:9 landscape cinematic frame. a runner bursting forward with a determined face as the pitch streaks past, dramatic low-angle shot, golden stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Sát thương: ba điểm. Độc nhất: ba điểm, vì tốc độ là thứ nhiều cầu thủ có. Tiến hóa: ba điểm, khi cậu học các…

```text
Wide 16:9 landscape cinematic frame. a scorecard with three rows of three stars each and nine circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Ngoài đời, tốc độ cũng là vũ khí được săn đón nhất của các cầu thủ chạy cánh. Nhưng tốc độ chỉ có giá khi có…

```text
Wide 16:9 landscape cinematic frame. a top-down tactical board with an arrow racing into a wide open space along the wing, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Hạng 7: chân trái đại bác

Lời: Hạng bảy là Kunigami Rensuke, với cú sút chân trái uy lực từ ngoài vòng cấm. Khi cậu có khoảng trống để sút,…

```text
Wide 16:9 landscape cinematic frame. a powerful left-footed kick sending a ball rocketing toward a goal from long range, dynamic wide shot, bright floodlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Kunigami muốn trở thành một anh hùng, một tiền đạo chơi đẹp và chính trực. Nhưng Blue Lock liên tục thử thách…

```text
Wide 16:9 landscape cinematic frame. a figure standing tall with a hand on their chest in an empty stadium at dawn, heroic low-angle shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Sát thương: bốn điểm. Sút xa là cách ghi bàn trực tiếp. Độc nhất: hai điểm, vì sút mạnh là kỹ năng cơ bản mà…

```text
Wide 16:9 landscape cinematic frame. a scorecard with four stars and two stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Tiến hóa: bốn điểm. Qua các giai đoạn, Kunigami trở lại với thể lực và cú sút được mài giũa hơn. Tổng: mười đ…

```text
Wide 16:9 landscape cinematic frame. the scorecard total of ten circled with a small cannon doodle, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: vũ khí đơn giản không có nghĩa là yếu. Nó chỉ có nghĩa là bạn phải mài nó sắc hơn mọi người.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sharpening a tiny pencil with great concentration. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Hạng 6: khống chế bóng thiên tài

Lời: Hạng sáu là Nagi Seishiro. Cậu mới chơi bóng chưa lâu, nhưng có một khả năng khống chế bóng gần như phi lý: b…

```text
Wide 16:9 landscape cinematic frame. a ball dropping from high in the air and landing perfectly dead on a foot, extreme close-up, bright soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Vì khống chế hoàn hảo, Nagi có thể làm những động tác mà người khác không dám nghĩ tới, như giả vờ sút rồi đổ…

```text
Wide 16:9 landscape cinematic frame. a figure in midair twisting with the ball glued to their foot, surprised defenders frozen below, dynamic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Sát thương: bốn điểm. Độc nhất: năm điểm, vì cảm giác bóng ấy là bẩm sinh, không ai tập ra được.

```text
Wide 16:9 landscape cinematic frame. a scorecard with four stars and five stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nhưng tiến hóa: chỉ hai điểm. Nagi từng rất lười, và truyện cho thấy cậu gặp khó khi phải thật sự khao khát.…

```text
Wide 16:9 landscape cinematic frame. a figure lying on a couch playing a handheld game with a football forgotten on the floor, humorous close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Nagi là bài học đắt nhất bảng xếp hạng. Tài năng bẩm sinh cao nhất không đảm bảo hạng cao nhất, nế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a shiny golden football with a slightly worried face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Hạng 5: rê bóng cùng con quái vật

Lời: Hạng năm là Bachira Meguru. Vũ khí của cậu là rê bóng: những đường lắc léo không theo bất kỳ quy luật nào, nh…

```text
Wide 16:9 landscape cinematic frame. a figure dancing past defenders with the ball in a swirling path, dynamic wide shot, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Bachira kể rằng trong mình có một con quái vật, một người bạn tưởng tượng từ thuở nhỏ, luôn rê bóng cùng cậu…

```text
Wide 16:9 landscape cinematic frame. a child kicking a ball alone in a park beside a faint friendly shadow shaped like a playful creature, wide shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Sát thương: ba điểm. Rê bóng mở đường, nhưng không phải lúc nào cũng kết thúc bằng bàn thắng. Độc nhất: bốn đ…

```text
Wide 16:9 landscape cinematic frame. a scorecard with three stars and four stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Tiến hóa: năm điểm. Bachira học được cách để con quái vật bên trong là chính mình, không cần ai khác nữa. Tổn…

```text
Wide 16:9 landscape cinematic frame. a figure dribbling alone confidently with the friendly shadow now merged into their own shadow, wide shot, bright warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: vũ khí của Bachira lớn lên khi cậu thôi dựa vào người khác. Đó là một câu chuyện trưởng thành đặt…

```text
Wide 16:9 landscape cinematic frame. the owl mascot doing a clumsy little dance step with a football. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Hạng 4: sút ở mọi tư thế

Lời: Hạng bốn là Shidou Ryusei, người được gọi là con quỷ. Vũ khí của cậu là khả năng sút ở mọi tư thế: đang lộn n…

```text
Wide 16:9 landscape cinematic frame. a figure flipping upside down in midair and striking a ball with explosive force, dynamic wide shot, intense floodlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Shidou đọc được chỗ bóng sẽ bùng nổ, như một khoảnh khắc vụ nổ lớn, và luôn có mặt ở đó để dứt điểm.

```text
Wide 16:9 landscape cinematic frame. a small starburst of light where a ball is about to be struck in the penalty area, symbolic close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Sát thương: năm điểm. Độc nhất: năm điểm. Không ai sút được từ những góc kỳ quặc như vậy.

```text
Wide 16:9 landscape cinematic frame. a scorecard with five stars and five stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Ngoài đời, những pha móc bóng hay xe đạp chổng ngược vẫn thỉnh thoảng xuất hiện. Nhưng sút như vậy thường xuy…

```text
Wide 16:9 landscape cinematic frame. a single bicycle-kick silhouette frozen against stadium floodlights, dramatic low-angle shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Tiến hóa: ba điểm. Shidou gần như đã hoàn thiện ngay từ đầu, và thứ cậu cần học là phối hợp, không phải thêm…

```text
Wide 16:9 landscape cinematic frame. the scorecard total of thirteen circled with a small lightning doodle, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Shidou là minh chứng rằng vũ khí hoàn hảo cũng có giới hạn, nếu chủ nhân không học cách chơi cùng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to juggle a football alone and fumbling it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Hạng 3: nhà vua

Lời: Hạng ba là Barou Shoei, tự xưng là nhà vua. Vũ khí của cậu là sự kết hợp giữa rê bóng mạnh mẽ và cú dứt điểm…

```text
Wide 16:9 landscape cinematic frame. a powerful figure charging through defenders with a crown-shaped shadow on the ground, dynamic low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Barou tin rằng cả sân bóng là vương quốc của mình, và đồng đội chỉ là người hầu. Cái tôi ấy khiến cậu khó chị…

```text
Wide 16:9 landscape cinematic frame. a figure standing alone at the center circle with arms crossed while teammates keep their distance, wide shot, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Nhưng điểm đáng nể nhất của Barou không phải cú sút. Đó là cách cậu thua. Barou từng bị Isagi cướp vai trò, v…

```text
Wide 16:9 landscape cinematic frame. a figure kneeling on the pitch after a loss, then rising with clenched fists, split-moment wide shot, rainy stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Sát thương: năm điểm. Độc nhất: ba điểm, vì rê và sút mạnh thì nhiều người có, chỉ là không ai tự tin như Bar…

```text
Wide 16:9 landscape cinematic frame. a scorecard with five stars and three stars filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Tiến hóa: năm điểm. Mỗi thất bại lại biến Barou thành một phiên bản khác. Tổng: mười ba điểm, bằng Shidou, nh…

```text
Wide 16:9 landscape cinematic frame. the scorecard total of thirteen circled with a seedling icon tipping the balance, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là lý do Kaku đặt luật hòa là tiến hóa. Trong Blue Lock, người biết thua đúng cách thường đi x…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a small paper crown on a scuffed old football. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Hạng 2: chính xác và phá hủy

Lời: Hạng hai là Itoshi Rin, người đứng đầu bảng xếp hạng Blue Lock suốt một thời gian dài. Vũ khí của cậu là sự c…

```text
Wide 16:9 landscape cinematic frame. a ball threading a perfect path through a narrow gap between defenders into the top corner, dynamic wide shot, cold precise light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Rin có một người anh trai là thiên tài bóng đá, Itoshi Sae. Cả hành trình của Rin là cuộc đuổi theo, rồi cố v…

```text
Wide 16:9 landscape cinematic frame. two long shadows on a pitch at sunset, one ahead and one chasing, symbolic wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Trong trận với đội U-20, Rin bộc lộ một mặt khác: lối chơi hủy diệt, bất chấp đồng đội, chỉ để thắng.

```text
Wide 16:9 landscape cinematic frame. a fierce figure tearing through a defensive line with shards of light scattering around, dramatic close-up, harsh red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Sát thương: năm điểm. Độc nhất: năm điểm. Tiến hóa: bốn điểm, vì cậu vẫn đang lớn, nhưng bị trói buộc bởi cái…

```text
Wide 16:9 landscape cinematic frame. a scorecard with five, five and four stars filled and fourteen circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Rin mạnh nhất khi quên đi người anh. Nhưng câu hỏi cậu chưa trả lời được là: nếu không phải để vượ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up at a long shadow cast across a pitch, thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Hạng 1: tầm nhìn nuốt chửng

Lời: Và hạng một: Isagi Yoichi, nhân vật chính. Vũ khí của cậu không phải cú sút mạnh nhất hay tốc độ nhanh nhất.…

```text
Wide 16:9 landscape cinematic frame. a figure standing still in the middle of a busy pitch while everyone else blurs around them, dramatic wide shot, focused light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Ban đầu, Isagi có khả năng nhìn không gian: đọc vị trí của mọi người để tìm ra điểm trống. Rồi cậu phát triển…

```text
Wide 16:9 landscape cinematic frame. a tactical overlay of lines and circles projected over a pitch from a player's point of view, amber ink style close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Rồi tầm nhìn ấy lớn tới mức được gọi là Metavision: cậu nhìn trận đấu như từ trên cao, thấy trước cả ý định c…

```text
Wide 16:9 landscape cinematic frame. a translucent bird's-eye view of a football pitch floating above a player's head with arrows showing everyone's intentions, symbolic wide shot, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Ở Neo Egoist League, Isagi còn luyện được khả năng sút bằng cả hai chân, xóa đi điểm mù của chính mình.

```text
Wide 16:9 landscape cinematic frame. two football boots side by side, both glowing equally, extreme close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Và điều đáng sợ nhất: Isagi nuốt chửng vũ khí của người khác. Cậu học từ Bachira, từ Rin, từ Barou, và biến c…

```text
Wide 16:9 landscape cinematic frame. a figure at the center of a web of glowing lines connected to several faceless player silhouettes, symbolic wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Sát thương: bốn điểm, vì cú sút của cậu không phải mạnh nhất. Độc nhất: năm điểm. Tiến hóa: năm điểm, vì chín…

```text
Wide 16:9 landscape cinematic frame. a scorecard with four, five and five stars filled and fourteen circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Mười bốn điểm, bằng Rin. Nhưng theo luật hòa, Isagi xếp trên. Vì vũ khí của cậu không có trần.

```text
Wide 16:9 landscape cinematic frame. a balance scale tipping toward a small glowing seedling that keeps growing, symbolic close-up, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: vũ khí mạnh nhất Blue Lock không phải là một kỹ năng, mà là khả năng biến điểm mạnh của người khác…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing oversized glasses and looking at a football pitch from a high stand. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Đề cử danh dự

Lời: Có vài vũ khí không vào được top mười của Kaku, vì chủ nhân không phải tiền đạo Blue Lock hoặc truyện chưa kể…

```text
Wide 16:9 landscape cinematic frame. a small side table with a few ribbons labeled honorable mention, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Cú sút tốc độ của Michael Kaiser, ngôi sao người Đức ở Neo Egoist League. Nhanh tới mức thủ môn không kịp phả…

```text
Wide 16:9 landscape cinematic frame. a blurred ball tearing through the air leaving a sharp streak of light toward a goal, dynamic wide shot, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Và những đường chuyền của Itoshi Sae, người anh của Rin. Một tiền vệ thiên tài, nên không nằm trong bảng dành…

```text
Wide 16:9 landscape cinematic frame. a perfect curving pass drawn as a golden line across a tactical board, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Vũ khí ngoài sân cỏ thật

Lời: Blue Lock phóng đại mọi thứ, nhưng nhiều vũ khí có bóng dáng ngoài đời thật. Tốc độ là vũ khí của cầu thủ chạ…

```text
Wide 16:9 landscape cinematic frame. a tactical board with small icons of real football roles, a winger arrow, a target striker circle, a playmaker eye, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Còn tầm nhìn kiểu Isagi thì ngoài đời thường thuộc về các tiền vệ kiến thiết, những người nhìn thấy đường chu…

```text
Wide 16:9 landscape cinematic frame. a midfielder silhouette with head up scanning the pitch while others look at the ball, wide shot, bright stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nhưng có một chỗ Blue Lock khác hẳn: bóng đá thật là môn đồng đội. Một tiền đạo chỉ biết ích kỷ sẽ khó đứng v…

```text
Wide 16:9 landscape cinematic frame. eleven small silhouettes linked by a single glowing line across a pitch at dusk, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: điều thú vị là chính Blue Lock cũng dần thừa nhận điều đó. Những tiền đạo mạnh nhất là người biết…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a football in one wing and giving a high five with the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Bảng xếp hạng đầy đủ

Lời: Toàn bộ bảng xếp hạng. Hạng mười: cơ thể dẻo, bảy điểm. Hạng chín: sao chép, tám điểm. Hạng tám: tốc độ, chín…

```text
Wide 16:9 landscape cinematic frame. a ranking board on parchment with the bottom three rows filled in with small icons, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Hạng bảy: chân trái, mười điểm. Hạng sáu: khống chế bóng, mười một điểm. Hạng năm: rê bóng, mười hai điểm.

```text
Wide 16:9 landscape cinematic frame. the middle rows of the ranking board filled with icons, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hạng bốn: sút mọi tư thế, mười ba điểm. Hạng ba: nhà vua, mười ba điểm. Hạng hai: chính xác, mười bốn điểm. H…

```text
Wide 16:9 landscape cinematic frame. the top rows of the ranking board glowing, the first row crowned with a small eye icon, amber ink close-up, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Để ý một điều: bốn hạng đầu đều cách nhau rất ít. Và thứ quyết định thứ tự không phải sức mạnh, mà là khả năn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling the top four rows of the board with a red pencil. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Bạn xếp lại thế nào?

Lời: Giờ tới lượt bạn. Nếu bạn chấm sát thương cao hơn tiến hóa, Rin hoặc Shidou có thể lên hạng một. Nếu bạn chấm…

```text
Wide 16:9 landscape cinematic frame. a blank ranking board with numbered empty rows and a pencil resting on it, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Hãy viết top ba của bạn vào bình luận, kèm một câu lý do. Kaku sẽ tổng hợp những bảng xếp hạng thú vị nhất tr…

```text
Wide 16:9 landscape cinematic frame. a stack of handwritten ranking cards on a desk, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và nếu bạn là một tiền đạo trong Blue Lock, vũ khí của bạn là gì? Kaku đoán vũ khí của Kaku là nói nhiều tới…

```text
Wide 16:9 landscape cinematic frame. the owl mascot chattering at a bored defender figure who is yawning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · Kết

Lời: Ba trăm tiền đạo, mười vũ khí, và một bài học chung: vũ khí mạnh nhất không phải thứ bạn sinh ra đã có, mà là…

```text
Wide 16:9 landscape cinematic frame. a football on the center spot of a vast empty stadium at dawn, wide shot, hopeful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Video tiếp theo, Kaku mở cửa một thế giới mới: Kagurabachi, bộ truyện về yêu đao sắp lên anime. Nếu bạn chưa…

```text
Wide 16:9 landscape cinematic frame. a sheathed sword resting on a wooden stand in a quiet workshop, dramatic close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những bảng xếp hạng có luật rõ ràng, hãy đăng ký kênh. Và nhớ tìm vũ khí của riêng mình, kể cả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot kicking a small football toward the camera and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Blue Lock là gì?

Khoảng 124 giây · cảnh s01–s11 · 1606 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói về vũ khí của các tiền đạo Blue Lock tới hết giải U-20 và phần Neo Egoist League trong manga. Nếu bạn chỉ xem anime, hãy cẩn thận ở hạng 1.

<short pause> Ba trăm tiền đạo trẻ bị nhốt vào một cơ sở huấn luyện. Chỉ một người được bước ra làm tiền đạo số một của Nhật Bản. Và để sống sót, mỗi người cần một thứ: vũ khí.

<short pause> Vũ khí ở đây không phải dao kiếm. Đó là một kỹ năng mà chỉ bạn có, và đủ sắc để ghi bàn ở bất kỳ trận đấu nào.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku xếp hạng mười vũ khí của các tiền đạo Blue Lock, từ hạng mười lên hạng một, bằng ba tiêu chí công bố ngay từ đầu. Cuối video là bảng xếp hạng đầy đủ.

<short pause> Và Kaku nói trước: bảng này xếp hạng vũ khí, không xếp hạng người. Một cầu thủ có vũ khí hạng thấp vẫn có thể là người thú vị nhất bộ truyện.

<short pause> Trong truyện, sau khi đội tuyển Nhật Bản bị loại ở World Cup 2018, Liên đoàn bóng đá mở một dự án đặc biệt tên là Blue Lock.

<short pause> Nhân vật chính Isagi bước vào Blue Lock sau một trận đấu ở trường: ở khoảnh khắc quyết định, cậu chuyền bóng thay vì tự sút. Đồng đội sút hỏng, và đội cậu thua.

<short pause> Người đứng đầu dự án là Ego Jinpachi, một huấn luyện viên kỳ quặc với một triết lý: Nhật Bản thiếu một tiền đạo ích kỷ, một người muốn ghi bàn hơn mọi thứ khác.

<short pause> Ego nói, đại ý, rằng mỗi tiền đạo phải tìm ra vũ khí của mình, rồi tìm công thức để ghi bàn bằng vũ khí đó. Vũ khí cộng với công thức, bằng bàn thắng.

<short pause> Luật chơi rất khắc nghiệt: ai thua sẽ bị loại, và theo luật dự án, không bao giờ được khoác áo đội tuyển quốc gia nữa.

<short pause> Kaku để ý: Blue Lock biến bóng đá thành một trò chơi sinh tồn. Và trong trò chơi sinh tồn, thứ quý nhất chính là vũ khí.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói về vũ khí của các tiền đạo Blue Lock tới hết giải U-20 và phần Neo Egoist League trong manga. Nếu bạn chỉ xem anime, hãy cẩn thận ở hạng 1.

[pause] Ba trăm tiền đạo trẻ bị nhốt vào một cơ sở huấn luyện. Chỉ một người được bước ra làm tiền đạo số một của Nhật Bản. Và để sống sót, mỗi người cần một thứ: vũ khí.

[pause] Vũ khí ở đây không phải dao kiếm. Đó là một kỹ năng mà chỉ bạn có, và đủ sắc để ghi bàn ở bất kỳ trận đấu nào.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku xếp hạng mười vũ khí của các tiền đạo Blue Lock, từ hạng mười lên hạng một, bằng ba tiêu chí công bố ngay từ đầu. Cuối video là bảng xếp hạng đầy đủ.

[pause] Và Kaku nói trước: bảng này xếp hạng vũ khí, không xếp hạng người. Một cầu thủ có vũ khí hạng thấp vẫn có thể là người thú vị nhất bộ truyện.

[pause] Trong truyện, sau khi đội tuyển Nhật Bản bị loại ở World Cup 2018, Liên đoàn bóng đá mở một dự án đặc biệt tên là Blue Lock.

[pause] Nhân vật chính Isagi bước vào Blue Lock sau một trận đấu ở trường: ở khoảnh khắc quyết định, cậu chuyền bóng thay vì tự sút. Đồng đội sút hỏng, và đội cậu thua.

[pause] Người đứng đầu dự án là Ego Jinpachi, một huấn luyện viên kỳ quặc với một triết lý: Nhật Bản thiếu một tiền đạo ích kỷ, một người muốn ghi bàn hơn mọi thứ khác.

[pause] Ego nói, đại ý, rằng mỗi tiền đạo phải tìm ra vũ khí của mình, rồi tìm công thức để ghi bàn bằng vũ khí đó. Vũ khí cộng với công thức, bằng bàn thắng.

[pause] Luật chơi rất khắc nghiệt: ai thua sẽ bị loại, và theo luật dự án, không bao giờ được khoác áo đội tuyển quốc gia nữa.

[pause] Kaku để ý: Blue Lock biến bóng đá thành một trò chơi sinh tồn. Và trong trò chơi sinh tồn, thứ quý nhất chính là vũ khí.
```

### c02 · Ba tiêu chí chấm điểm / Hạng 10: cơ thể dẻo như cao su / Hạng 9: tắc kè hoa

Khoảng 139 giây · cảnh s12–s26 · 1811 ký tự

**Gemini**

```text
Tiêu chí một: sát thương. Vũ khí này trực tiếp tạo ra bàn thắng tới mức nào? Chấm từ một tới năm.

<short pause> Tiêu chí hai: độc nhất. Người khác có dễ học theo, dễ sao chép không? Càng khó sao chép, điểm càng cao.

<short pause> Tiêu chí ba: tiến hóa. Vũ khí này còn lớn lên được không, hay đã chạm trần? Blue Lock là câu chuyện về tiến hóa, nên tiêu chí này rất quan trọng.

<short pause> Tổng điểm tối đa là mười lăm. Và luật hòa: nếu hai vũ khí bằng điểm, vũ khí có điểm tiến hóa cao hơn xếp trên.

<short pause> <laugh> Điểm là cảm nhận của Kaku, dựa trên những gì truyện cho thấy. Bạn hoàn toàn có thể chấm khác, và Kaku muốn nghe bạn chấm.

<short pause> Hạng mười thuộc về Gagamaru, thành viên đội Z. Vũ khí của cậu là một cơ thể dẻo khác thường, có thể vươn tới những góc bóng mà người khác không với tới.

<short pause> Trong những trận đầu, Gagamaru thậm chí đứng khung thành cho cả đội, vì phản xạ và độ dẻo của cậu hợp với vị trí đó hơn.

<short pause> Sát thương: hai điểm. Cơ thể dẻo giúp chạm bóng, nhưng bản thân nó không ghi bàn. Độc nhất: bốn điểm, vì không ai tập được sự kỳ quặc ấy.

<short pause> Tiến hóa: một điểm. Truyện chưa cho thấy vũ khí này phát triển thêm. Tổng: bảy điểm.

<short pause> Kaku để ý: một vũ khí độc nhất nhưng không lớn lên được, cuối cùng sẽ bị bỏ lại trong một nơi mà ai cũng tiến hóa từng ngày.

<short pause> Hạng chín là Mikage Reo. Cậu xuất thân từ gia đình giàu có, và vũ khí cậu tìm ra là khả năng sao chép: quan sát kỹ năng của người khác rồi làm lại gần như y hệt.

<short pause> Lúc đầu Reo không có vũ khí riêng. Cậu chỉ là cộng sự của một thiên tài. Chính việc bị bỏ lại đã buộc cậu tìm ra thứ của mình.

<short pause> Sát thương: hai điểm. Bản sao thường yếu hơn bản gốc. Độc nhất: ba điểm. Sao chép thì ai cũng có thể thử, nhưng sao chép nhanh như Reo thì hiếm.

<short pause> Tiến hóa: ba điểm. Mỗi người mới cậu gặp là một vũ khí mới cậu có thể học. Tổng: tám điểm.

<short pause> Kaku để ý: vũ khí của Reo là chiếc gương của cả Blue Lock. Nó cho thấy ai là người đáng học nhất.
```

**ElevenLabs**

```text
Tiêu chí một: sát thương. [curious] Vũ khí này trực tiếp tạo ra bàn thắng tới mức nào? Chấm từ một tới năm.

[pause] Tiêu chí hai: độc nhất. Người khác có dễ học theo, dễ sao chép không? Càng khó sao chép, điểm càng cao.

[pause] Tiêu chí ba: tiến hóa. Vũ khí này còn lớn lên được không, hay đã chạm trần? Blue Lock là câu chuyện về tiến hóa, nên tiêu chí này rất quan trọng.

[pause] Tổng điểm tối đa là mười lăm. Và luật hòa: nếu hai vũ khí bằng điểm, vũ khí có điểm tiến hóa cao hơn xếp trên.

[pause] [chuckles] Điểm là cảm nhận của Kaku, dựa trên những gì truyện cho thấy. Bạn hoàn toàn có thể chấm khác, và Kaku muốn nghe bạn chấm.

[pause] Hạng mười thuộc về Gagamaru, thành viên đội Z. Vũ khí của cậu là một cơ thể dẻo khác thường, có thể vươn tới những góc bóng mà người khác không với tới.

[pause] Trong những trận đầu, Gagamaru thậm chí đứng khung thành cho cả đội, vì phản xạ và độ dẻo của cậu hợp với vị trí đó hơn.

[pause] Sát thương: hai điểm. Cơ thể dẻo giúp chạm bóng, nhưng bản thân nó không ghi bàn. Độc nhất: bốn điểm, vì không ai tập được sự kỳ quặc ấy.

[pause] Tiến hóa: một điểm. Truyện chưa cho thấy vũ khí này phát triển thêm. Tổng: bảy điểm.

[pause] Kaku để ý: một vũ khí độc nhất nhưng không lớn lên được, cuối cùng sẽ bị bỏ lại trong một nơi mà ai cũng tiến hóa từng ngày.

[pause] Hạng chín là Mikage Reo. Cậu xuất thân từ gia đình giàu có, và vũ khí cậu tìm ra là khả năng sao chép: quan sát kỹ năng của người khác rồi làm lại gần như y hệt.

[pause] Lúc đầu Reo không có vũ khí riêng. Cậu chỉ là cộng sự của một thiên tài. Chính việc bị bỏ lại đã buộc cậu tìm ra thứ của mình.

[pause] Sát thương: hai điểm. Bản sao thường yếu hơn bản gốc. Độc nhất: ba điểm. Sao chép thì ai cũng có thể thử, nhưng sao chép nhanh như Reo thì hiếm.

[pause] Tiến hóa: ba điểm. Mỗi người mới cậu gặp là một vũ khí mới cậu có thể học. Tổng: tám điểm.

[pause] Kaku để ý: vũ khí của Reo là chiếc gương của cả Blue Lock. Nó cho thấy ai là người đáng học nhất.
```

### c03 · Hạng 8: tốc độ / Hạng 7: chân trái đại bác / Hạng 6: khống chế bóng thiên tài

Khoảng 145 giây · cảnh s27–s41 · 1888 ký tự

**Gemini**

```text
Hạng tám là Chigiri Hyoma, và vũ khí đơn giản nhất: tốc độ. Khi có khoảng trống, không ai đuổi kịp cậu.

<short pause> Nhưng Chigiri từng bị chấn thương đầu gối nặng, và cậu sợ phải chạy hết sức một lần nữa. Vũ khí mạnh nhất của cậu cũng là nỗi sợ lớn nhất.

<short pause> Khoảnh khắc Chigiri quyết định chạy hết sức, dù biết có thể lại đau, là một trong những cảnh đáng nhớ nhất của đội Z.

<short pause> Sát thương: ba điểm. Độc nhất: ba điểm, vì tốc độ là thứ nhiều cầu thủ có. Tiến hóa: ba điểm, khi cậu học cách dùng tốc độ thông minh hơn. Tổng: chín điểm.

<short pause> Ngoài đời, tốc độ cũng là vũ khí được săn đón nhất của các cầu thủ chạy cánh. <short pause> Nhưng tốc độ chỉ có giá khi có khoảng trống để chạy.

<short pause> Hạng bảy là Kunigami Rensuke, với cú sút chân trái uy lực từ ngoài vòng cấm. Khi cậu có khoảng trống để sút, thủ môn chỉ có thể đoán hướng.

<short pause> Kunigami muốn trở thành một anh hùng, một tiền đạo chơi đẹp và chính trực. <short pause> Nhưng Blue Lock liên tục thử thách lý tưởng ấy.

<short pause> Sát thương: bốn điểm. Sút xa là cách ghi bàn trực tiếp. Độc nhất: hai điểm, vì sút mạnh là kỹ năng cơ bản mà nhiều người luyện được.

<short pause> Tiến hóa: bốn điểm. Qua các giai đoạn, Kunigami trở lại với thể lực và cú sút được mài giũa hơn. Tổng: mười điểm.

<short pause> <laugh> Kaku để ý: vũ khí đơn giản không có nghĩa là yếu. Nó chỉ có nghĩa là bạn phải mài nó sắc hơn mọi người.

<short pause> Hạng sáu là Nagi Seishiro. Cậu mới chơi bóng chưa lâu, nhưng có một khả năng khống chế bóng gần như phi lý: bóng tới từ góc nào, cậu cũng dập được gọn gàng.

<short pause> Vì khống chế hoàn hảo, Nagi có thể làm những động tác mà người khác không dám nghĩ tới, như giả vờ sút rồi đổi ý giữa không trung.

<short pause> Sát thương: bốn điểm. Độc nhất: năm điểm, vì cảm giác bóng ấy là bẩm sinh, không ai tập ra được.

<short pause> Nhưng tiến hóa: chỉ hai điểm. Nagi từng rất lười, và truyện cho thấy cậu gặp khó khi phải thật sự khao khát. Tổng: mười một điểm.

<short pause> Kaku để ý: Nagi là bài học đắt nhất bảng xếp hạng. Tài năng bẩm sinh cao nhất không đảm bảo hạng cao nhất, nếu thiếu cái đói.
```

**ElevenLabs**

```text
Hạng tám là Chigiri Hyoma, và vũ khí đơn giản nhất: tốc độ. Khi có khoảng trống, không ai đuổi kịp cậu.

[pause] Nhưng Chigiri từng bị chấn thương đầu gối nặng, và cậu sợ phải chạy hết sức một lần nữa. Vũ khí mạnh nhất của cậu cũng là nỗi sợ lớn nhất.

[pause] Khoảnh khắc Chigiri quyết định chạy hết sức, dù biết có thể lại đau, là một trong những cảnh đáng nhớ nhất của đội Z.

[pause] Sát thương: ba điểm. Độc nhất: ba điểm, vì tốc độ là thứ nhiều cầu thủ có. Tiến hóa: ba điểm, khi cậu học cách dùng tốc độ thông minh hơn. Tổng: chín điểm.

[pause] Ngoài đời, tốc độ cũng là vũ khí được săn đón nhất của các cầu thủ chạy cánh. [pause] Nhưng tốc độ chỉ có giá khi có khoảng trống để chạy.

[pause] Hạng bảy là Kunigami Rensuke, với cú sút chân trái uy lực từ ngoài vòng cấm. Khi cậu có khoảng trống để sút, thủ môn chỉ có thể đoán hướng.

[pause] Kunigami muốn trở thành một anh hùng, một tiền đạo chơi đẹp và chính trực. [pause] Nhưng Blue Lock liên tục thử thách lý tưởng ấy.

[pause] Sát thương: bốn điểm. Sút xa là cách ghi bàn trực tiếp. Độc nhất: hai điểm, vì sút mạnh là kỹ năng cơ bản mà nhiều người luyện được.

[pause] Tiến hóa: bốn điểm. Qua các giai đoạn, Kunigami trở lại với thể lực và cú sút được mài giũa hơn. Tổng: mười điểm.

[pause] [chuckles] Kaku để ý: vũ khí đơn giản không có nghĩa là yếu. Nó chỉ có nghĩa là bạn phải mài nó sắc hơn mọi người.

[pause] Hạng sáu là Nagi Seishiro. Cậu mới chơi bóng chưa lâu, nhưng có một khả năng khống chế bóng gần như phi lý: bóng tới từ góc nào, cậu cũng dập được gọn gàng.

[pause] Vì khống chế hoàn hảo, Nagi có thể làm những động tác mà người khác không dám nghĩ tới, như giả vờ sút rồi đổi ý giữa không trung.

[pause] Sát thương: bốn điểm. Độc nhất: năm điểm, vì cảm giác bóng ấy là bẩm sinh, không ai tập ra được.

[pause] Nhưng tiến hóa: chỉ hai điểm. Nagi từng rất lười, và truyện cho thấy cậu gặp khó khi phải thật sự khao khát. Tổng: mười một điểm.

[pause] Kaku để ý: Nagi là bài học đắt nhất bảng xếp hạng. Tài năng bẩm sinh cao nhất không đảm bảo hạng cao nhất, nếu thiếu cái đói.
```

### c04 · Hạng 5: rê bóng cùng con quái vật / Hạng 4: sút ở mọi tư thế

Khoảng 107 giây · cảnh s42–s52 · 1388 ký tự

**Gemini**

```text
Hạng năm là Bachira Meguru. Vũ khí của cậu là rê bóng: những đường lắc léo không theo bất kỳ quy luật nào, như đang nhảy múa.

<short pause> Bachira kể rằng trong mình có một con quái vật, một người bạn tưởng tượng từ thuở nhỏ, luôn rê bóng cùng cậu và chỉ đường cho cậu.

<short pause> Sát thương: ba điểm. Rê bóng mở đường, nhưng không phải lúc nào cũng kết thúc bằng bàn thắng. Độc nhất: bốn điểm, vì nhịp rê bóng ấy rất khó đoán.

<short pause> Tiến hóa: năm điểm. Bachira học được cách để con quái vật bên trong là chính mình, không cần ai khác nữa. Tổng: mười hai điểm.

<short pause> <laugh> Kaku để ý: vũ khí của Bachira lớn lên khi cậu thôi dựa vào người khác. Đó là một câu chuyện trưởng thành đặt trong một pha rê bóng.

<short pause> Hạng bốn là Shidou Ryusei, người được gọi là con quỷ. Vũ khí của cậu là khả năng sút ở mọi tư thế: đang lộn nhào, đang ngã, đang bay.

<short pause> Shidou đọc được chỗ bóng sẽ bùng nổ, như một khoảnh khắc vụ nổ lớn, và luôn có mặt ở đó để dứt điểm.

<short pause> Sát thương: năm điểm. Độc nhất: năm điểm. Không ai sút được từ những góc kỳ quặc như vậy.

<short pause> Ngoài đời, những pha móc bóng hay xe đạp chổng ngược vẫn thỉnh thoảng xuất hiện. <short pause> Nhưng sút như vậy thường xuyên, như Shidou, là thứ chỉ có trong truyện.

<short pause> Tiến hóa: ba điểm. Shidou gần như đã hoàn thiện ngay từ đầu, và thứ cậu cần học là phối hợp, không phải thêm vũ khí. Tổng: mười ba điểm.

<short pause> Kaku để ý: Shidou là minh chứng rằng vũ khí hoàn hảo cũng có giới hạn, nếu chủ nhân không học cách chơi cùng người khác.
```

**ElevenLabs**

```text
Hạng năm là Bachira Meguru. Vũ khí của cậu là rê bóng: những đường lắc léo không theo bất kỳ quy luật nào, như đang nhảy múa.

[pause] Bachira kể rằng trong mình có một con quái vật, một người bạn tưởng tượng từ thuở nhỏ, luôn rê bóng cùng cậu và chỉ đường cho cậu.

[pause] Sát thương: ba điểm. Rê bóng mở đường, nhưng không phải lúc nào cũng kết thúc bằng bàn thắng. Độc nhất: bốn điểm, vì nhịp rê bóng ấy rất khó đoán.

[pause] Tiến hóa: năm điểm. Bachira học được cách để con quái vật bên trong là chính mình, không cần ai khác nữa. Tổng: mười hai điểm.

[pause] [chuckles] Kaku để ý: vũ khí của Bachira lớn lên khi cậu thôi dựa vào người khác. Đó là một câu chuyện trưởng thành đặt trong một pha rê bóng.

[pause] Hạng bốn là Shidou Ryusei, người được gọi là con quỷ. Vũ khí của cậu là khả năng sút ở mọi tư thế: đang lộn nhào, đang ngã, đang bay.

[pause] Shidou đọc được chỗ bóng sẽ bùng nổ, như một khoảnh khắc vụ nổ lớn, và luôn có mặt ở đó để dứt điểm.

[pause] Sát thương: năm điểm. Độc nhất: năm điểm. Không ai sút được từ những góc kỳ quặc như vậy.

[pause] Ngoài đời, những pha móc bóng hay xe đạp chổng ngược vẫn thỉnh thoảng xuất hiện. [pause] Nhưng sút như vậy thường xuyên, như Shidou, là thứ chỉ có trong truyện.

[pause] Tiến hóa: ba điểm. Shidou gần như đã hoàn thiện ngay từ đầu, và thứ cậu cần học là phối hợp, không phải thêm vũ khí. Tổng: mười ba điểm.

[pause] Kaku để ý: Shidou là minh chứng rằng vũ khí hoàn hảo cũng có giới hạn, nếu chủ nhân không học cách chơi cùng người khác.
```

### c05 · Hạng 3: nhà vua / Hạng 2: chính xác và phá hủy

Khoảng 117 giây · cảnh s53–s63 · 1519 ký tự

**Gemini**

```text
Hạng ba là Barou Shoei, tự xưng là nhà vua. Vũ khí của cậu là sự kết hợp giữa rê bóng mạnh mẽ và cú dứt điểm đầy uy lực.

<short pause> Barou tin rằng cả sân bóng là vương quốc của mình, và đồng đội chỉ là người hầu. Cái tôi ấy khiến cậu khó chịu, nhưng cũng khiến cậu dứt điểm không chút do dự.

<short pause> Nhưng điểm đáng nể nhất của Barou không phải cú sút. Đó là cách cậu thua. Barou từng bị Isagi cướp vai trò, và thay vì gục ngã, cậu tìm một cách ghi bàn mới.

<short pause> Sát thương: năm điểm. Độc nhất: ba điểm, vì rê và sút mạnh thì nhiều người có, chỉ là không ai tự tin như Barou.

<short pause> Tiến hóa: năm điểm. Mỗi thất bại lại biến Barou thành một phiên bản khác. Tổng: mười ba điểm, bằng Shidou, nhưng xếp trên nhờ luật hòa.

<short pause> <laugh> Kaku để ý: đây là lý do Kaku đặt luật hòa là tiến hóa. Trong Blue Lock, người biết thua đúng cách thường đi xa hơn người chưa bao giờ thua.

<short pause> Hạng hai là Itoshi Rin, người đứng đầu bảng xếp hạng Blue Lock suốt một thời gian dài. Vũ khí của cậu là sự chính xác: sút, chuyền, chọn vị trí, gần như không sai.

<short pause> Rin có một người anh trai là thiên tài bóng đá, Itoshi Sae. Cả hành trình của Rin là cuộc đuổi theo, rồi cố vượt qua cái bóng của anh mình.

<short pause> Trong trận với đội U-20, Rin bộc lộ một mặt khác: lối chơi hủy diệt, bất chấp đồng đội, chỉ để thắng.

<short pause> Sát thương: năm điểm. Độc nhất: năm điểm. Tiến hóa: bốn điểm, vì cậu vẫn đang lớn, nhưng bị trói buộc bởi cái bóng của anh trai. Tổng: mười bốn điểm.

<short pause> Kaku để ý: Rin mạnh nhất khi quên đi người anh. <short pause> Nhưng câu hỏi cậu chưa trả lời được là: nếu không phải để vượt qua anh, cậu chơi bóng vì điều gì?
```

**ElevenLabs**

```text
Hạng ba là Barou Shoei, tự xưng là nhà vua. Vũ khí của cậu là sự kết hợp giữa rê bóng mạnh mẽ và cú dứt điểm đầy uy lực.

[pause] Barou tin rằng cả sân bóng là vương quốc của mình, và đồng đội chỉ là người hầu. Cái tôi ấy khiến cậu khó chịu, nhưng cũng khiến cậu dứt điểm không chút do dự.

[pause] Nhưng điểm đáng nể nhất của Barou không phải cú sút. Đó là cách cậu thua. Barou từng bị Isagi cướp vai trò, và thay vì gục ngã, cậu tìm một cách ghi bàn mới.

[pause] Sát thương: năm điểm. Độc nhất: ba điểm, vì rê và sút mạnh thì nhiều người có, chỉ là không ai tự tin như Barou.

[pause] Tiến hóa: năm điểm. Mỗi thất bại lại biến Barou thành một phiên bản khác. Tổng: mười ba điểm, bằng Shidou, nhưng xếp trên nhờ luật hòa.

[pause] [chuckles] Kaku để ý: đây là lý do Kaku đặt luật hòa là tiến hóa. Trong Blue Lock, người biết thua đúng cách thường đi xa hơn người chưa bao giờ thua.

[pause] Hạng hai là Itoshi Rin, người đứng đầu bảng xếp hạng Blue Lock suốt một thời gian dài. Vũ khí của cậu là sự chính xác: sút, chuyền, chọn vị trí, gần như không sai.

[pause] Rin có một người anh trai là thiên tài bóng đá, Itoshi Sae. Cả hành trình của Rin là cuộc đuổi theo, rồi cố vượt qua cái bóng của anh mình.

[pause] Trong trận với đội U-20, Rin bộc lộ một mặt khác: lối chơi hủy diệt, bất chấp đồng đội, chỉ để thắng.

[pause] Sát thương: năm điểm. Độc nhất: năm điểm. Tiến hóa: bốn điểm, vì cậu vẫn đang lớn, nhưng bị trói buộc bởi cái bóng của anh trai. Tổng: mười bốn điểm.

[pause] Kaku để ý: Rin mạnh nhất khi quên đi người anh. [pause] [curious] Nhưng câu hỏi cậu chưa trả lời được là: nếu không phải để vượt qua anh, cậu chơi bóng vì điều gì?
```

### c06 · Hạng 1: tầm nhìn nuốt chửng / Đề cử danh dự

Khoảng 112 giây · cảnh s64–s74 · 1452 ký tự

**Gemini**

```text
Và hạng một: Isagi Yoichi, nhân vật chính. Vũ khí của cậu không phải cú sút mạnh nhất hay tốc độ nhanh nhất. Đó là tầm nhìn.

<short pause> Ban đầu, Isagi có khả năng nhìn không gian: đọc vị trí của mọi người để tìm ra điểm trống. Rồi cậu phát triển cú sút một chạm, dứt điểm ngay khi bóng tới.

<short pause> Rồi tầm nhìn ấy lớn tới mức được gọi là Metavision: cậu nhìn trận đấu như từ trên cao, thấy trước cả ý định của đồng đội lẫn đối thủ.

<short pause> Ở Neo Egoist League, Isagi còn luyện được khả năng sút bằng cả hai chân, xóa đi điểm mù của chính mình.

<short pause> Và điều đáng sợ nhất: Isagi nuốt chửng vũ khí của người khác. Cậu học từ Bachira, từ Rin, từ Barou, và biến chúng thành một phần công thức của mình.

<short pause> Sát thương: bốn điểm, vì cú sút của cậu không phải mạnh nhất. Độc nhất: năm điểm. Tiến hóa: năm điểm, vì chính tiến hóa là vũ khí của Isagi. Tổng: mười bốn điểm.

<short pause> Mười bốn điểm, bằng Rin. <short pause> Nhưng theo luật hòa, Isagi xếp trên. Vì vũ khí của cậu không có trần.

<short pause> <laugh> Kaku để ý: vũ khí mạnh nhất Blue Lock không phải là một kỹ năng, mà là khả năng biến điểm mạnh của người khác thành của mình.

<short pause> Có vài vũ khí không vào được top mười của Kaku, vì chủ nhân không phải tiền đạo Blue Lock hoặc truyện chưa kể đủ.

<short pause> Cú sút tốc độ của Michael Kaiser, ngôi sao người Đức ở Neo Egoist League. Nhanh tới mức thủ môn không kịp phản ứng. <short pause> Nhưng đây là vũ khí của đối thủ, không phải của Blue Lock.

<short pause> Và những đường chuyền của Itoshi Sae, người anh của Rin. Một tiền vệ thiên tài, nên không nằm trong bảng dành cho tiền đạo.
```

**ElevenLabs**

```text
Và hạng một: Isagi Yoichi, nhân vật chính. Vũ khí của cậu không phải cú sút mạnh nhất hay tốc độ nhanh nhất. Đó là tầm nhìn.

[pause] Ban đầu, Isagi có khả năng nhìn không gian: đọc vị trí của mọi người để tìm ra điểm trống. Rồi cậu phát triển cú sút một chạm, dứt điểm ngay khi bóng tới.

[pause] Rồi tầm nhìn ấy lớn tới mức được gọi là Metavision: cậu nhìn trận đấu như từ trên cao, thấy trước cả ý định của đồng đội lẫn đối thủ.

[pause] Ở Neo Egoist League, Isagi còn luyện được khả năng sút bằng cả hai chân, xóa đi điểm mù của chính mình.

[pause] Và điều đáng sợ nhất: Isagi nuốt chửng vũ khí của người khác. Cậu học từ Bachira, từ Rin, từ Barou, và biến chúng thành một phần công thức của mình.

[pause] Sát thương: bốn điểm, vì cú sút của cậu không phải mạnh nhất. Độc nhất: năm điểm. Tiến hóa: năm điểm, vì chính tiến hóa là vũ khí của Isagi. Tổng: mười bốn điểm.

[pause] Mười bốn điểm, bằng Rin. [pause] Nhưng theo luật hòa, Isagi xếp trên. Vì vũ khí của cậu không có trần.

[pause] [chuckles] Kaku để ý: vũ khí mạnh nhất Blue Lock không phải là một kỹ năng, mà là khả năng biến điểm mạnh của người khác thành của mình.

[pause] Có vài vũ khí không vào được top mười của Kaku, vì chủ nhân không phải tiền đạo Blue Lock hoặc truyện chưa kể đủ.

[pause] Cú sút tốc độ của Michael Kaiser, ngôi sao người Đức ở Neo Egoist League. Nhanh tới mức thủ môn không kịp phản ứng. [pause] Nhưng đây là vũ khí của đối thủ, không phải của Blue Lock.

[pause] Và những đường chuyền của Itoshi Sae, người anh của Rin. Một tiền vệ thiên tài, nên không nằm trong bảng dành cho tiền đạo.
```

### c07 · Vũ khí ngoài sân cỏ thật / Bảng xếp hạng đầy đủ / Bạn xếp lại thế nào? / Kết

Khoảng 150 giây · cảnh s75–s88 · 1945 ký tự

**Gemini**

```text
Blue Lock phóng đại mọi thứ, nhưng nhiều vũ khí có bóng dáng ngoài đời thật. Tốc độ là vũ khí của cầu thủ chạy cánh. Khống chế bóng là vũ khí của những tiền đạo cắm giỏi giữ bóng.

<short pause> Còn tầm nhìn kiểu Isagi thì ngoài đời thường thuộc về các tiền vệ kiến thiết, những người nhìn thấy đường chuyền trước khi nó xuất hiện.

<short pause> Nhưng có một chỗ Blue Lock khác hẳn: bóng đá thật là môn đồng đội. Một tiền đạo chỉ biết ích kỷ sẽ khó đứng vững trong một đội bóng thật.

<short pause> <laugh> Kaku để ý: điều thú vị là chính Blue Lock cũng dần thừa nhận điều đó. Những tiền đạo mạnh nhất là người biết dùng đồng đội để phục vụ cái tôi của mình.

<short pause> Toàn bộ bảng xếp hạng. Hạng mười: cơ thể dẻo, bảy điểm. Hạng chín: sao chép, tám điểm. Hạng tám: tốc độ, chín điểm.

<short pause> Hạng bảy: chân trái, mười điểm. Hạng sáu: khống chế bóng, mười một điểm. Hạng năm: rê bóng, mười hai điểm.

<short pause> Hạng bốn: sút mọi tư thế, mười ba điểm. Hạng ba: nhà vua, mười ba điểm. Hạng hai: chính xác, mười bốn điểm. Hạng một: tầm nhìn, mười bốn điểm.

<short pause> Để ý một điều: bốn hạng đầu đều cách nhau rất ít. Và thứ quyết định thứ tự không phải sức mạnh, mà là khả năng lớn lên.

<short pause> Giờ tới lượt bạn. Nếu bạn chấm sát thương cao hơn tiến hóa, Rin hoặc Shidou có thể lên hạng một. Nếu bạn chấm độc nhất cao nhất, Nagi có thể leo lên rất xa.

<short pause> Hãy viết top ba của bạn vào bình luận, kèm một câu lý do. Kaku sẽ tổng hợp những bảng xếp hạng thú vị nhất trong một video sau.

<short pause> Và nếu bạn là một tiền đạo trong Blue Lock, vũ khí của bạn là gì? Kaku đoán vũ khí của Kaku là nói nhiều tới mức hậu vệ mất tập trung.

<short pause> Ba trăm tiền đạo, mười vũ khí, và một bài học chung: vũ khí mạnh nhất không phải thứ bạn sinh ra đã có, mà là thứ bạn không ngừng làm cho nó lớn lên.

<short pause> Video tiếp theo, Kaku mở cửa một thế giới mới: Kagurabachi, bộ truyện về yêu đao sắp lên anime. Nếu bạn chưa đọc, đó là mười lăm phút bạn cần.

<short pause> Nếu bạn thích những bảng xếp hạng có luật rõ ràng, hãy đăng ký kênh. Và nhớ tìm vũ khí của riêng mình, kể cả ngoài sân cỏ. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Blue Lock phóng đại mọi thứ, nhưng nhiều vũ khí có bóng dáng ngoài đời thật. Tốc độ là vũ khí của cầu thủ chạy cánh. Khống chế bóng là vũ khí của những tiền đạo cắm giỏi giữ bóng.

[pause] Còn tầm nhìn kiểu Isagi thì ngoài đời thường thuộc về các tiền vệ kiến thiết, những người nhìn thấy đường chuyền trước khi nó xuất hiện.

[pause] Nhưng có một chỗ Blue Lock khác hẳn: bóng đá thật là môn đồng đội. Một tiền đạo chỉ biết ích kỷ sẽ khó đứng vững trong một đội bóng thật.

[pause] [chuckles] Kaku để ý: điều thú vị là chính Blue Lock cũng dần thừa nhận điều đó. Những tiền đạo mạnh nhất là người biết dùng đồng đội để phục vụ cái tôi của mình.

[pause] Toàn bộ bảng xếp hạng. Hạng mười: cơ thể dẻo, bảy điểm. Hạng chín: sao chép, tám điểm. Hạng tám: tốc độ, chín điểm.

[pause] Hạng bảy: chân trái, mười điểm. Hạng sáu: khống chế bóng, mười một điểm. Hạng năm: rê bóng, mười hai điểm.

[pause] Hạng bốn: sút mọi tư thế, mười ba điểm. Hạng ba: nhà vua, mười ba điểm. Hạng hai: chính xác, mười bốn điểm. Hạng một: tầm nhìn, mười bốn điểm.

[pause] Để ý một điều: bốn hạng đầu đều cách nhau rất ít. Và thứ quyết định thứ tự không phải sức mạnh, mà là khả năng lớn lên.

[pause] Giờ tới lượt bạn. Nếu bạn chấm sát thương cao hơn tiến hóa, Rin hoặc Shidou có thể lên hạng một. Nếu bạn chấm độc nhất cao nhất, Nagi có thể leo lên rất xa.

[pause] Hãy viết top ba của bạn vào bình luận, kèm một câu lý do. Kaku sẽ tổng hợp những bảng xếp hạng thú vị nhất trong một video sau.

[pause] [curious] Và nếu bạn là một tiền đạo trong Blue Lock, vũ khí của bạn là gì? Kaku đoán vũ khí của Kaku là nói nhiều tới mức hậu vệ mất tập trung.

[pause] Ba trăm tiền đạo, mười vũ khí, và một bài học chung: vũ khí mạnh nhất không phải thứ bạn sinh ra đã có, mà là thứ bạn không ngừng làm cho nó lớn lên.

[pause] Video tiếp theo, Kaku mở cửa một thế giới mới: Kagurabachi, bộ truyện về yêu đao sắp lên anime. Nếu bạn chưa đọc, đó là mười lăm phút bạn cần.

[pause] Nếu bạn thích những bảng xếp hạng có luật rõ ràng, hãy đăng ký kênh. Và nhớ tìm vũ khí của riêng mình, kể cả ngoài sân cỏ. Kaku gấp sổ đây, hẹn gặp lại!
```
