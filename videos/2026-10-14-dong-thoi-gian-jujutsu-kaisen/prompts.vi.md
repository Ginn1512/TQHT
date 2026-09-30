# Bộ prompt · Jujutsu Kaisen: Dòng thời gian 1.000 năm, từ thời Heian đến Shibuya

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 7 đoạn đọc, khoảng 15.4 phút giọng.
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

Lời: Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya, phim Jujutsu Kaisen số 0, và phần mở đầu Trò c…

```text
Wide 16:9 landscape cinematic frame. an ancient Japanese capital at night lit by paper lanterns, a modern skyline faintly visible behind it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một đêm năm 2018, ở giữa Tokyo, một kế hoạch được chuẩn bị suốt một nghìn năm bắt đầu vận hành.

```text
Wide 16:9 landscape cinematic frame. a crowded modern city street on a festival night, a faint dark dome forming over the skyline. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Để hiểu đêm đó, ta phải quay về rất xa: về thời Heian, khi kinh đô Nhật Bản còn thắp đèn lồng, và thế giới ch…

```text
Wide 16:9 landscape cinematic frame. a lantern-lit wooden palace in an ancient capital, robed figures crossing a bridge under the moon. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku thắp từng chiếc đèn lồng cho mỗi thời đại, và kéo một sợi chỉ đỏ đi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot lighting a row of paper lanterns, a red thread running through them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và vì thời Heian là một thời kỳ có thật trong lịch sử Nhật Bản, Kaku sẽ đặt lịch sử thật và lịch sử trong tru…

```text
Wide 16:9 landscape cinematic frame. two parallel timelines on a scroll, one labeled with a history book icon and one with a manga icon. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Thời Heian ngoài đời thật

Lời: Trước tiên là lịch sử thật. Thời Heian kéo dài từ năm 794 tới khoảng năm 1185. Kinh đô là Heian-kyō, nay là t…

```text
Wide 16:9 landscape cinematic frame. an aerial view of an ancient grid-planned capital with a grand palace at its northern end. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Đó là thời kỳ văn hóa cung đình phát triển rực rỡ, với thơ ca, tiểu thuyết và nghi lễ. Nhưng cũng là thời kỳ…

```text
Wide 16:9 landscape cinematic frame. courtiers writing poetry by candlelight while shadows of spirits lurk outside the paper screens. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Có hẳn những người làm nghề âm dương sư, chuyên xem điềm, trừ tà và tính ngày lành tháng tốt cho triều đình.…

```text
Wide 16:9 landscape cinematic frame. a robed diviner arranging talismans and a star chart on a low wooden table. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Người ta còn tin những người chết oan có thể biến thành oán linh. Một quan đại thần có thật tên là Sugawara n…

```text
Wide 16:9 landscape cinematic frame. an old shrine with plum blossoms, students leaving prayer plaques at the gate. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và đây là điểm nối thú vị: trong Jujutsu Kaisen, hai nhân vật mạnh nhất thời hiện đại được nói là hậu duệ xa…

```text
Wide 16:9 landscape cinematic frame. a family tree growing from an ancient shrine to two modern silhouettes. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Truyện còn mượn nhiều thứ khác từ văn hóa thật, như những vị thần, những câu chuyện ma quỷ dân gian và các ng…

```text
Wide 16:9 landscape cinematic frame. a collection of old folk art prints of spirits and demons pinned on a wall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: vậy nên khi truyện nói thời Heian là thời hoàng kim của chú thuật, nó dựa trên một nền văn hóa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a real history book open beside a manga volume. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Thời Heian trong truyện: thời hoàng kim

Lời: Giờ sang lịch sử trong truyện. Khoảng một nghìn năm trước, thế giới chú thuật mạnh hơn bây giờ rất nhiều. Chú…

```text
Wide 16:9 landscape cinematic frame. a night battle in an ancient capital, bursts of cursed energy lighting up pagodas. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và kẻ đứng trên đỉnh tất cả là Sukuna, vua nguyền rủa. Như Kaku đã nói trong video mười hiểu lầm, hắn là con…

```text
Wide 16:9 landscape cinematic frame. a shadowy figure seated on a throne of ruins, an ancient city burning below. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Các chú thuật sư thời đó hợp sức cũng không đánh bại được hắn. Sau khi hắn chết, hai mươi ngón tay trở thành…

```text
Wide 16:9 landscape cinematic frame. twenty sealed wooden boxes scattered across a map of ancient Japan. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Hắn có một người hầu trung thành, cũng sống từ thời đó tới tận hiện đại, chờ đợi ngày chủ nhân trở lại.

```text
Wide 16:9 landscape cinematic frame. a pale servant figure bowing in the snow outside an ancient gate, centuries passing behind them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và cũng trong thời Heian, có một chú thuật sư khác bắt đầu một kế hoạch dài nhất lịch sử. Đó là đầu sợi chỉ đ…

```text
Wide 16:9 landscape cinematic frame. a red thread emerging from an ancient lantern and stretching off into the darkness. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: thời Heian trong truyện giống một kỷ nguyên của những quái vật, và hiện tại chỉ là cái bóng yếu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small lantern against a looming ancient shadow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Thiên Nguyên và những kết giới

Lời: Chiếc đèn lồng tiếp theo thuộc về một nhân vật đặc biệt: Thiên Nguyên, một chú thuật sư đã sống hơn một nghìn…

```text
Wide 16:9 landscape cinematic frame. a mysterious presence behind layered barrier walls deep beneath a temple. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Thiên Nguyên duy trì những kết giới bảo vệ khắp Nhật Bản và che giấu các cơ sở của giới chú thuật. Có thể nói…

```text
Wide 16:9 landscape cinematic frame. a map of Japan covered in faint glowing barrier lines connected to a single central point. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Nhưng bất tử có một cái giá: nếu không làm gì, cơ thể Thiên Nguyên sẽ tiến hóa thành một thứ không còn là con…

```text
Wide 16:9 landscape cinematic frame. a silhouette slowly transforming into an abstract shape of light, a warning glow around it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Để ngăn điều đó, cứ khoảng năm trăm năm một lần, Thiên Nguyên phải hợp nhất với một người đặc biệt, gọi là vậ…

```text
Wide 16:9 landscape cinematic frame. a young girl standing before an ancient gate, a cycle of five hundred years drawn around her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Người được chọn làm vật chứa thường không hề biết cuộc đời mình được định sẵn cho việc đó cho tới khi đủ lớn.…

```text
Wide 16:9 landscape cinematic frame. a young girl in a school uniform looking at a starry sky, unaware of shadows watching from rooftops. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hãy nhớ con số năm trăm năm. Vì một trong những lần hợp nhất ấy sẽ bị phá hỏng, và dòng thời gi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling the number 500 in red on its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Khoảng 400 năm trước: hai gia chủ

Lời: Nhảy tới khoảng bốn trăm năm trước, thời Keichō, đầu thời Edo. Chiếc đèn lồng này thắp sáng một trận đấu mà a…

```text
Wide 16:9 landscape cinematic frame. a castle town at the start of a new era, samurai silhouettes in the streets. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Trong thế giới chú thuật có ba gia tộc lớn: Gojo, Zenin và Kamo. Họ nắm giữ quyền lực và những thuật thức mạn…

```text
Wide 16:9 landscape cinematic frame. three family crests carved on three great gates of old estates. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Thời đó, gia chủ nhà Gojo, người có cả Lục nhãn lẫn Vô hạ hạn, đấu với gia chủ nhà Zenin, người mang Thập chủ…

```text
Wide 16:9 landscape cinematic frame. two sorcerers striking each other simultaneously in a burning shrine, shadows and light colliding. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Trận đấu này được nhắc lại nhiều lần trong truyện, như một bằng chứng rằng thuật thức của Megumi có thể sánh…

```text
Wide 16:9 landscape cinematic frame. a young boy's shadow overlapping with an ancient warrior's shadow on a wall. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: mối thù và sự cạnh tranh giữa các gia tộc kéo dài hàng trăm năm. Nó là một phần lý do vì sao gi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing between three quarreling crests, sighing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Thời Minh Trị: chú thuật sư tồi tệ nhất lịch sử

Lời: Chiếc đèn lồng tiếp theo cháy trong thời Minh Trị, khoảng một trăm rưỡi năm trước, khi Nhật Bản mở cửa và hiệ…

```text
Wide 16:9 landscape cinematic frame. a Meiji-era street with gas lamps, western-style buildings and rickshaws. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Thời đó có một người của nhà Kamo, về sau bị gọi là chú thuật sư tồi tệ nhất lịch sử. Ông ta tiến hành những…

```text
Wide 16:9 landscape cinematic frame. a dim laboratory with jars on shelves and a shadowy figure in a Meiji-era coat. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Kết quả là chín chú vật được gọi là Cửu tướng đồ, những sinh mệnh nửa người nửa chú linh. Một số trong đó sẽ…

```text
Wide 16:9 landscape cinematic frame. nine glass jars in a row, faint silhouettes floating inside, numbered with small tags. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Và đây là chỗ sợi chỉ đỏ lộ ra: người nhà Kamo đó không thật sự là người nhà Kamo. Cơ thể ông ta đã bị một kẻ…

```text
Wide 16:9 landscape cinematic frame. a red thread wrapping around the Meiji-era figure's silhouette, pulling tight. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một người anh trong số chín sinh mệnh ấy, khi gặp lại kẻ này ở hiện tại, đã nhận ra ngay khuôn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at an old photograph that seems to look back. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Sợi chỉ đỏ: Kenjaku

Lời: Đã đến lúc gọi tên sợi chỉ đỏ: Kenjaku. Một chú thuật sư từ thời Heian, có thuật thức cho phép chiếm cơ thể n…

```text
Wide 16:9 landscape cinematic frame. a red thread running through lanterns of three different eras, connecting three silhouettes. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Dấu hiệu nhận biết là một đường khâu chạy ngang trán của cơ thể bị chiếm. Nhờ đó, kẻ này sống qua hết thời đạ…

```text
Wide 16:9 landscape cinematic frame. a close-up of a line of stitches across a forehead, softly lit, the face in shadow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Thời Heian, thời Minh Trị, và ở hiện tại, hắn mang cơ thể của một chú thuật sư đặc cấp đã chết, người bạn thâ…

```text
Wide 16:9 landscape cinematic frame. three portraits side by side from different eras, each with the same line of stitches. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Mục đích của hắn? Hắn muốn đẩy loài người tới một bước tiến hóa mới bằng chú lực, dù phải hy sinh bao nhiêu m…

```text
Wide 16:9 landscape cinematic frame. a vast crowd silhouetted under a sky filling with cursed energy, a single figure watching from above. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Điều đáng sợ nhất ở Kenjaku là sự kiên nhẫn. Hắn không vội. Hắn chờ đợi hàng trăm năm, thu thập từng mảnh ghé…

```text
Wide 16:9 landscape cinematic frame. a figure calmly placing pieces on a giant board game spanning centuries, candles burning low. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một nghìn năm, nhiều khuôn mặt, một kế hoạch. Hắn là lý do vì sao dòng thời gian này có một sợi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling on a long red thread that goes back through many lanterns. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · 2006: chuyến hộ tống

Lời: Nhảy tới thời hiện đại. Năm 2006, chiếc đèn lồng thứ năm trăm năm lại được thắp: đã tới lúc Thiên Nguyên hợp…

```text
Wide 16:9 landscape cinematic frame. a modern Tokyo skyline in 2006, a single paper lantern glowing on a rooftop. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Hai học sinh năm hai của trường chú thuật Tokyo được giao nhiệm vụ hộ tống cô gái làm vật chứa. Hai cậu là bộ…

```text
Wide 16:9 landscape cinematic frame. two confident teenage students in dark uniforms walking beside a young schoolgirl. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Nhưng một sát thủ không có chú lực, được thuê để giết cô gái, đã phá hỏng tất cả. Cô gái chết, và lần hợp nhấ…

```text
Wide 16:9 landscape cinematic frame. a lone assassin silhouette standing in a dark underground corridor, a dropped school bag nearby. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Trong trận chiến đó, một trong hai học sinh suýt chết, rồi thức tỉnh sức mạnh vượt bậc, trở thành người mạnh…

```text
Wide 16:9 landscape cinematic frame. one figure rising with a blinding aura, the other standing in shadow looking at his hands. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Sau lần đó, người học sinh suýt chết ấy trở thành chú thuật sư mà mọi người gọi là mạnh nhất. Người bạn của a…

```text
Wide 16:9 landscape cinematic frame. a lone student sitting on a rooftop at night, looking down at a busy city of ordinary people. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là điểm rẽ quan trọng nhất của thời hiện đại. Một người trở nên mạnh nhất, một người bắt đầ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a path splitting into two directions. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · 2007 đến 2017: kẻ phản bội và bách quỷ dạ hành

Lời: Năm 2007, người học sinh lạc lối ấy rời bỏ giới chú thuật, sau khi gây ra một vụ thảm sát ở một ngôi làng. An…

```text
Wide 16:9 landscape cinematic frame. a lone figure walking away from a quiet mountain village at dawn, smoke rising behind. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Mười năm sau, vào đêm Giáng sinh năm 2017, anh tổ chức một cuộc tấn công lớn gọi là Bách quỷ dạ hành, thả hàn…

```text
Wide 16:9 landscape cinematic frame. a night sky over two cities filled with swarms of shadowy curses, snow falling. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Đó là câu chuyện của phim Jujutsu Kaisen số 0, với nhân vật chính là một cậu học sinh bị một linh hồn nguyền…

```text
Wide 16:9 landscape cinematic frame. a timid student with a sword case, a massive protective spirit looming behind him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Cuối trận, người bạn thân năm xưa, giờ là người mạnh nhất, tự tay kết liễu kẻ phản bội. Cái chết đó tưởng như…

```text
Wide 16:9 landscape cinematic frame. two old friends facing each other in a snowy alley, one leaning against a wall. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhưng cơ thể của kẻ phản bội đã không được xử lý đúng cách. Và ai đó, với một đường khâu mới trên trán, đã lấ…

```text
Wide 16:9 landscape cinematic frame. a line of stitches glowing faintly on a forehead in a dark room. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · 2018: năm mọi thứ sụp đổ

Lời: Năm 2018. Tháng sáu, một học sinh cấp ba bình thường tên là Yuji nuốt một ngón tay của Sukuna để cứu bạn mình…

```text
Wide 16:9 landscape cinematic frame. a high school rooftop at night, a teenager holding a small withered finger, friends in danger. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Cậu được tha án tử với một điều kiện: ăn hết hai mươi ngón tay, rồi chết cùng Sukuna. Đó là khởi đầu của câu…

```text
Wide 16:9 landscape cinematic frame. a contract scroll with twenty small boxes, several already checked off. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Ngày 31 tháng 10 năm 2018, đêm Halloween, ở khu Shibuya, kẻ mang cơ thể của người phản bội thực hiện một bước…

```text
Wide 16:9 landscape cinematic frame. a crowded Halloween night at a famous scramble crossing, a dark barrier sealing the district. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Người mạnh nhất bị dụ vào một cái bẫy và bị phong ấn trong một chú vật gọi là Ngục môn cương. Không có anh, c…

```text
Wide 16:9 landscape cinematic frame. a small ornate cube floating in darkness, faint light leaking from its seams. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Và Sukuna được giải phóng trong chốc lát giữa Shibuya, gây ra thảm họa khủng khiếp. Đêm đó thay đổi hoàn toàn…

```text
Wide 16:9 landscape cinematic frame. a devastated city district at night, fires burning, a lone figure standing amid the ruins. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Trong đêm đó, nhiều nhân vật quan trọng ngã xuống, và những người sống sót không còn là con người cũ. Truyện…

```text
Wide 16:9 landscape cinematic frame. a quiet morning after a disaster, survivors sitting among rubble as the sun rises. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một nghìn năm chuẩn bị, và tất cả dồn vào một đêm lễ hội. Đó là lý do arc Shibuya được xem là m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a Halloween lantern with a worried expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Sau Shibuya: Trò chơi tử diệt

Lời: Sau Shibuya, kẻ mang đường khâu công bố bước tiếp theo: một trò chơi sinh tử trên khắp Nhật Bản, gọi là Trò c…

```text
Wide 16:9 landscape cinematic frame. a map of Japan with several glowing colonies marked by barrier domes. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Hắn đánh thức sức mạnh ở nhiều người, và còn đưa những chú thuật sư từ nhiều thời đại quá khứ trở lại trong c…

```text
Wide 16:9 landscape cinematic frame. ancient warrior silhouettes emerging from modern people like ghosts, standing in a ruined city. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Đây là phần mùa ba của anime, bắt đầu phát từ tháng một năm 2026. Phần tiếp theo sẽ là mùa bốn.

```text
Wide 16:9 landscape cinematic frame. a calendar page for January 2026 with a small barrier dome icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku dừng dòng thời gian ở đây để tránh spoiler. Chỉ cần biết: đây là lúc những chiếc đèn lồng từ mọi thời đạ…

```text
Wide 16:9 landscape cinematic frame. all the paper lanterns from every era glowing together in one street. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Bản đồ những nơi quan trọng

Lời: Trước khi tổng kết, hãy đặt các sự kiện lên bản đồ. Dòng thời gian này không chỉ trải dài theo năm, mà còn tr…

```text
Wide 16:9 landscape cinematic frame. a stylized map of Japan with small lantern icons placed on several cities. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Kyoto, kinh đô thời Heian, là nơi mọi thứ bắt đầu. Ngày nay, ở đó có một trong hai trường chú thuật của Nhật…

```text
Wide 16:9 landscape cinematic frame. a traditional school gate in an old city with temple roofs in the background. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Tokyo có trường chú thuật còn lại, nơi Yuji và bạn bè theo học. Sâu bên dưới trường là nơi ở của Thiên Nguyên…

```text
Wide 16:9 landscape cinematic frame. a quiet school on a wooded hill with a deep glowing chamber drawn beneath it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Shibuya, khu phố đông đúc bậc nhất Tokyo, trở thành chiến trường của đêm Halloween năm 2018.

```text
Wide 16:9 landscape cinematic frame. a famous busy crossing at night marked with a red lantern on the map. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Và sau Shibuya, Trò chơi tử diệt biến nhiều khu vực trên khắp Nhật Bản thành những vùng kết giới khép kín, nơ…

```text
Wide 16:9 landscape cinematic frame. several glowing domes scattered across the map, each with a small warning icon. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một kế hoạch bắt đầu ở kinh đô cổ, và kết thúc bằng việc biến cả đất nước thành sân chơi. Kenja…

```text
Wide 16:9 landscape cinematic frame. the owl mascot stretching a red thread from one end of the map to the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Những khoảng trống trên dòng thời gian

Lời: Dòng thời gian của Kaku vẫn còn những khoảng trống. Ở mức spoiler của video này, có vài câu hỏi truyện chưa t…

```text
Wide 16:9 landscape cinematic frame. a lantern-lit scroll with a few gaps where lanterns are missing. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Một: Sukuna đã sống thế nào ở thời Heian, và vì sao hắn trở thành con người đáng sợ nhất thời đại? Truyện chỉ…

```text
Wide 16:9 landscape cinematic frame. an empty lantern hook above an ancient ruined throne. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hai: người hầu trung thành của Sukuna thật sự là ai, và vì sao lại trung thành suốt một nghìn năm? Ba: kế hoạ…

```text
Wide 16:9 landscape cinematic frame. two question-mark lanterns hanging over a snowy gate and a long red thread. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · **Kaku** (đính kèm ảnh mẫu)

Lời: Bạn nào đã đọc manga tới cuối chắc biết thêm một vài câu trả lời. Nhưng hãy giúp người khác, đừng spoiler tro…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a finger to its beak with a gentle shush. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Toàn bộ dòng thời gian

Lời: Tổng kết cả dãy đèn lồng. Thời Heian, khoảng một nghìn năm trước: Sukuna thống trị, Kenjaku bắt đầu kế hoạch,…

```text
Wide 16:9 landscape cinematic frame. the first lanterns lighting up with small icons of a throne, a red thread and a barrier. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Khoảng bốn trăm năm trước: hai gia chủ Gojo và Zenin cùng gục ngã. Thời Minh Trị: người nhà Kamo bị chiếm xác…

```text
Wide 16:9 landscape cinematic frame. the middle lanterns lighting up with two crossed swords and nine small jars. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: 2006: lần hợp nhất năm trăm năm thất bại. 2007: kẻ phản bội rời đi. 2017: Bách quỷ dạ hành.

```text
Wide 16:9 landscape cinematic frame. modern lanterns lighting up with a school bag, a lone path and a snowy night. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: 2018: Yuji nuốt ngón tay, sự kiện Shibuya, người mạnh nhất bị phong ấn, và Trò chơi tử diệt bắt đầu.

```text
Wide 16:9 landscape cinematic frame. the final lanterns blazing brightly over a modern city. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku: những kẻ không chịu chết · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn cả dãy đèn lồng, Kaku nhận ra một điều: những nhân vật nguy hiểm nhất đều là những kẻ không chịu chết.

```text
Wide 16:9 landscape cinematic frame. the owl mascot walking along the line of lanterns, looking at each one carefully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Thiên Nguyên sống hơn một nghìn năm nhờ bất tử. Sukuna sống tiếp qua hai mươi ngón tay. Người hầu của hắn chờ…

```text
Wide 16:9 landscape cinematic frame. four shadowy figures standing apart from each other across a long timeline. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Trong khi đó, những nhân vật chính lại là những người trẻ, biết mình có thể chết bất cứ lúc nào. Truyện luôn…

```text
Wide 16:9 landscape cinematic frame. a group of young students sitting on school steps at sunset, laughing together. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Kaku nghĩ đó là câu hỏi lớn của Jujutsu Kaisen: sống mãi mà không thay đổi, hay sống ngắn nhưng trọn vẹn? Một…

```text
Wide 16:9 landscape cinematic frame. a withered ancient tree beside a young sapling in bright sunlight. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và có lẽ vì thế mà kẻ thù lớn nhất của truyện không phải một con quái vật, mà là một nghìn năm lịch sử không…

```text
Wide 16:9 landscape cinematic frame. an old red thread finally snapping in the wind, drifting away. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được sống qua một nghìn năm như Kenjaku, bạn muốn chứng kiến thời đại nào nhất? Viết vào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a lantern with a question mark painted on it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tới, Kaku mang bảng tuần hoàn và kính bảo hộ ra lần nữa, để kiểm tra những phát minh của Senku trong Dr…

```text
Wide 16:9 landscape cinematic frame. a rustic stone-age laboratory with glass flasks, a periodic table pinned to a wooden wall. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Kaku thổi tắt từng chiếc đèn lồng đây. Hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot blowing out a paper lantern, a thin trail of smoke rising. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thời Heian ngoài đời thật

Khoảng 139 giây · cảnh s01–s12 · 1812 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya, phim Jujutsu Kaisen số 0, và phần mở đầu Trò chơi tử diệt trong mùa ba.

<short pause> Một đêm năm 2018, ở giữa Tokyo, một kế hoạch được chuẩn bị suốt một nghìn năm bắt đầu vận hành.

<short pause> Để hiểu đêm đó, ta phải quay về rất xa: về thời Heian, khi kinh đô Nhật Bản còn thắp đèn lồng, và thế giới chú thuật ở thời hoàng kim.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku thắp từng chiếc đèn lồng cho mỗi thời đại, và kéo một sợi chỉ đỏ đi xuyên qua tất cả. Sợi chỉ đó là một nhân vật đã sống suốt một nghìn năm.

<short pause> Và vì thời Heian là một thời kỳ có thật trong lịch sử Nhật Bản, Kaku sẽ đặt lịch sử thật và lịch sử trong truyện cạnh nhau, để bạn thấy tác giả đã mượn gì từ đời thật.

<short pause> Trước tiên là lịch sử thật. Thời Heian kéo dài từ năm 794 tới khoảng năm 1185. Kinh đô là Heian-kyō, nay là thành phố Kyoto.

<short pause> Đó là thời kỳ văn hóa cung đình phát triển rực rỡ, với thơ ca, tiểu thuyết và nghi lễ. <short pause> Nhưng cũng là thời kỳ con người rất sợ ma quỷ và lời nguyền.

<short pause> Có hẳn những người làm nghề âm dương sư, chuyên xem điềm, trừ tà và tính ngày lành tháng tốt cho triều đình. Họ là hình mẫu ngoài đời gần nhất với chú thuật sư.

<short pause> Người ta còn tin những người chết oan có thể biến thành oán linh. Một quan đại thần có thật tên là Sugawara no Michizane, sau khi chết trong oan ức, được cho là đã gây ra tai họa, rồi được thờ phụng như vị thần học vấn.

<short pause> Và đây là điểm nối thú vị: trong Jujutsu Kaisen, hai nhân vật mạnh nhất thời hiện đại được nói là hậu duệ xa của chính ông.

<short pause> Truyện còn mượn nhiều thứ khác từ văn hóa thật, như những vị thần, những câu chuyện ma quỷ dân gian và các nghi lễ cổ. Đó là lý do thế giới chú thuật có cảm giác vừa hư cấu vừa quen thuộc.

<short pause> Kaku ghi chú: vậy nên khi truyện nói thời Heian là thời hoàng kim của chú thuật, nó dựa trên một nền văn hóa thật sự rất tin vào lời nguyền.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya, phim Jujutsu Kaisen số 0, và phần mở đầu Trò chơi tử diệt trong mùa ba.

[pause] Một đêm năm 2018, ở giữa Tokyo, một kế hoạch được chuẩn bị suốt một nghìn năm bắt đầu vận hành.

[pause] Để hiểu đêm đó, ta phải quay về rất xa: về thời Heian, khi kinh đô Nhật Bản còn thắp đèn lồng, và thế giới chú thuật ở thời hoàng kim.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku thắp từng chiếc đèn lồng cho mỗi thời đại, và kéo một sợi chỉ đỏ đi xuyên qua tất cả. Sợi chỉ đó là một nhân vật đã sống suốt một nghìn năm.

[pause] Và vì thời Heian là một thời kỳ có thật trong lịch sử Nhật Bản, Kaku sẽ đặt lịch sử thật và lịch sử trong truyện cạnh nhau, để bạn thấy tác giả đã mượn gì từ đời thật.

[pause] Trước tiên là lịch sử thật. Thời Heian kéo dài từ năm 794 tới khoảng năm 1185. Kinh đô là Heian-kyō, nay là thành phố Kyoto.

[pause] Đó là thời kỳ văn hóa cung đình phát triển rực rỡ, với thơ ca, tiểu thuyết và nghi lễ. [pause] Nhưng cũng là thời kỳ con người rất sợ ma quỷ và lời nguyền.

[pause] Có hẳn những người làm nghề âm dương sư, chuyên xem điềm, trừ tà và tính ngày lành tháng tốt cho triều đình. Họ là hình mẫu ngoài đời gần nhất với chú thuật sư.

[pause] Người ta còn tin những người chết oan có thể biến thành oán linh. Một quan đại thần có thật tên là Sugawara no Michizane, sau khi chết trong oan ức, được cho là đã gây ra tai họa, rồi được thờ phụng như vị thần học vấn.

[pause] Và đây là điểm nối thú vị: trong Jujutsu Kaisen, hai nhân vật mạnh nhất thời hiện đại được nói là hậu duệ xa của chính ông.

[pause] Truyện còn mượn nhiều thứ khác từ văn hóa thật, như những vị thần, những câu chuyện ma quỷ dân gian và các nghi lễ cổ. Đó là lý do thế giới chú thuật có cảm giác vừa hư cấu vừa quen thuộc.

[pause] Kaku ghi chú: vậy nên khi truyện nói thời Heian là thời hoàng kim của chú thuật, nó dựa trên một nền văn hóa thật sự rất tin vào lời nguyền.
```

### c02 · Thời Heian trong truyện: thời hoàng kim / Thiên Nguyên và những kết giới

Khoảng 137 giây · cảnh s13–s24 · 1784 ký tự

**Gemini**

```text
Giờ sang lịch sử trong truyện. Khoảng một nghìn năm trước, thế giới chú thuật mạnh hơn bây giờ rất nhiều. Chú thuật sư và chú linh đều ở đỉnh cao.

<short pause> Và kẻ đứng trên đỉnh tất cả là Sukuna, vua nguyền rủa. Như Kaku đã nói trong video mười hiểu lầm, hắn là con người, một chú thuật sư, chứ không phải quỷ.

<short pause> Các chú thuật sư thời đó hợp sức cũng không đánh bại được hắn. Sau khi hắn chết, hai mươi ngón tay trở thành những chú vật không thể phá hủy, rải rác khắp nơi.

<short pause> Hắn có một người hầu trung thành, cũng sống từ thời đó tới tận hiện đại, chờ đợi ngày chủ nhân trở lại.

<short pause> Và cũng trong thời Heian, có một chú thuật sư khác bắt đầu một kế hoạch dài nhất lịch sử. Đó là đầu sợi chỉ đỏ của Kaku.

<short pause> <laugh> Kaku ghi chú: thời Heian trong truyện giống một kỷ nguyên của những quái vật, và hiện tại chỉ là cái bóng yếu hơn của nó. Đó là lý do mọi thứ từ thời Heian đều đáng sợ.

<short pause> Chiếc đèn lồng tiếp theo thuộc về một nhân vật đặc biệt: Thiên Nguyên, một chú thuật sư đã sống hơn một nghìn năm nhờ một thuật thức bất tử.

<short pause> Thiên Nguyên duy trì những kết giới bảo vệ khắp Nhật Bản và che giấu các cơ sở của giới chú thuật. Có thể nói, toàn bộ hệ thống chú thuật hiện đại đứng trên vai người này.

<short pause> Nhưng bất tử có một cái giá: nếu không làm gì, cơ thể Thiên Nguyên sẽ tiến hóa thành một thứ không còn là con người, và có thể trở nên nguy hiểm.

<short pause> Để ngăn điều đó, cứ khoảng năm trăm năm một lần, Thiên Nguyên phải hợp nhất với một người đặc biệt, gọi là vật chứa Tinh Tương, để làm mới cơ thể.

<short pause> Người được chọn làm vật chứa thường không hề biết cuộc đời mình được định sẵn cho việc đó cho tới khi đủ lớn. Và có những kẻ muốn phá lần hợp nhất ấy vì đủ loại lý do, từ tín ngưỡng tới tiền bạc.

<short pause> Kaku ghi chú: hãy nhớ con số năm trăm năm. Vì một trong những lần hợp nhất ấy sẽ bị phá hỏng, và dòng thời gian sẽ rẽ sang một hướng khác.
```

**ElevenLabs**

```text
Giờ sang lịch sử trong truyện. Khoảng một nghìn năm trước, thế giới chú thuật mạnh hơn bây giờ rất nhiều. Chú thuật sư và chú linh đều ở đỉnh cao.

[pause] Và kẻ đứng trên đỉnh tất cả là Sukuna, vua nguyền rủa. Như Kaku đã nói trong video mười hiểu lầm, hắn là con người, một chú thuật sư, chứ không phải quỷ.

[pause] Các chú thuật sư thời đó hợp sức cũng không đánh bại được hắn. Sau khi hắn chết, hai mươi ngón tay trở thành những chú vật không thể phá hủy, rải rác khắp nơi.

[pause] Hắn có một người hầu trung thành, cũng sống từ thời đó tới tận hiện đại, chờ đợi ngày chủ nhân trở lại.

[pause] Và cũng trong thời Heian, có một chú thuật sư khác bắt đầu một kế hoạch dài nhất lịch sử. Đó là đầu sợi chỉ đỏ của Kaku.

[pause] [chuckles] Kaku ghi chú: thời Heian trong truyện giống một kỷ nguyên của những quái vật, và hiện tại chỉ là cái bóng yếu hơn của nó. Đó là lý do mọi thứ từ thời Heian đều đáng sợ.

[pause] Chiếc đèn lồng tiếp theo thuộc về một nhân vật đặc biệt: Thiên Nguyên, một chú thuật sư đã sống hơn một nghìn năm nhờ một thuật thức bất tử.

[pause] Thiên Nguyên duy trì những kết giới bảo vệ khắp Nhật Bản và che giấu các cơ sở của giới chú thuật. Có thể nói, toàn bộ hệ thống chú thuật hiện đại đứng trên vai người này.

[pause] Nhưng bất tử có một cái giá: nếu không làm gì, cơ thể Thiên Nguyên sẽ tiến hóa thành một thứ không còn là con người, và có thể trở nên nguy hiểm.

[pause] Để ngăn điều đó, cứ khoảng năm trăm năm một lần, Thiên Nguyên phải hợp nhất với một người đặc biệt, gọi là vật chứa Tinh Tương, để làm mới cơ thể.

[pause] Người được chọn làm vật chứa thường không hề biết cuộc đời mình được định sẵn cho việc đó cho tới khi đủ lớn. Và có những kẻ muốn phá lần hợp nhất ấy vì đủ loại lý do, từ tín ngưỡng tới tiền bạc.

[pause] Kaku ghi chú: hãy nhớ con số năm trăm năm. Vì một trong những lần hợp nhất ấy sẽ bị phá hỏng, và dòng thời gian sẽ rẽ sang một hướng khác.
```

### c03 · Khoảng 400 năm trước: hai gia chủ / Thời Minh Trị: chú thuật sư tồi tệ nhất lịch sử

Khoảng 110 giây · cảnh s25–s34 · 1424 ký tự

**Gemini**

```text
Nhảy tới khoảng bốn trăm năm trước, thời Keichō, đầu thời Edo. Chiếc đèn lồng này thắp sáng một trận đấu mà ai cũng nhắc tới.

<short pause> Trong thế giới chú thuật có ba gia tộc lớn: Gojo, Zenin và Kamo. Họ nắm giữ quyền lực và những thuật thức mạnh nhất, truyền qua nhiều thế hệ.

<short pause> Thời đó, gia chủ nhà Gojo, người có cả Lục nhãn lẫn Vô hạ hạn, đấu với gia chủ nhà Zenin, người mang Thập chủng ảnh pháp. Cả hai cùng chết trong trận đấu ấy.

<short pause> Trận đấu này được nhắc lại nhiều lần trong truyện, như một bằng chứng rằng thuật thức của Megumi có thể sánh ngang sức mạnh mạnh nhất.

<short pause> <laugh> Kaku ghi chú: mối thù và sự cạnh tranh giữa các gia tộc kéo dài hàng trăm năm. Nó là một phần lý do vì sao giới chú thuật hiện đại bảo thủ và chia rẽ đến vậy.

<short pause> Chiếc đèn lồng tiếp theo cháy trong thời Minh Trị, khoảng một trăm rưỡi năm trước, khi Nhật Bản mở cửa và hiện đại hóa.

<short pause> Thời đó có một người của nhà Kamo, về sau bị gọi là chú thuật sư tồi tệ nhất lịch sử. Ông ta tiến hành những thí nghiệm khủng khiếp với một người phụ nữ có thể mang thai con của chú linh.

<short pause> Kết quả là chín chú vật được gọi là Cửu tướng đồ, những sinh mệnh nửa người nửa chú linh. Một số trong đó sẽ thức tỉnh và xuất hiện ở hiện tại.

<short pause> Và đây là chỗ sợi chỉ đỏ lộ ra: người nhà Kamo đó không thật sự là người nhà Kamo. Cơ thể ông ta đã bị một kẻ khác chiếm lấy.

<short pause> Kaku ghi chú: một người anh trong số chín sinh mệnh ấy, khi gặp lại kẻ này ở hiện tại, đã nhận ra ngay khuôn mặt của kẻ đã tạo ra mình.
```

**ElevenLabs**

```text
Nhảy tới khoảng bốn trăm năm trước, thời Keichō, đầu thời Edo. Chiếc đèn lồng này thắp sáng một trận đấu mà ai cũng nhắc tới.

[pause] Trong thế giới chú thuật có ba gia tộc lớn: Gojo, Zenin và Kamo. Họ nắm giữ quyền lực và những thuật thức mạnh nhất, truyền qua nhiều thế hệ.

[pause] Thời đó, gia chủ nhà Gojo, người có cả Lục nhãn lẫn Vô hạ hạn, đấu với gia chủ nhà Zenin, người mang Thập chủng ảnh pháp. Cả hai cùng chết trong trận đấu ấy.

[pause] Trận đấu này được nhắc lại nhiều lần trong truyện, như một bằng chứng rằng thuật thức của Megumi có thể sánh ngang sức mạnh mạnh nhất.

[pause] [chuckles] Kaku ghi chú: mối thù và sự cạnh tranh giữa các gia tộc kéo dài hàng trăm năm. Nó là một phần lý do vì sao giới chú thuật hiện đại bảo thủ và chia rẽ đến vậy.

[pause] Chiếc đèn lồng tiếp theo cháy trong thời Minh Trị, khoảng một trăm rưỡi năm trước, khi Nhật Bản mở cửa và hiện đại hóa.

[pause] Thời đó có một người của nhà Kamo, về sau bị gọi là chú thuật sư tồi tệ nhất lịch sử. Ông ta tiến hành những thí nghiệm khủng khiếp với một người phụ nữ có thể mang thai con của chú linh.

[pause] Kết quả là chín chú vật được gọi là Cửu tướng đồ, những sinh mệnh nửa người nửa chú linh. Một số trong đó sẽ thức tỉnh và xuất hiện ở hiện tại.

[pause] Và đây là chỗ sợi chỉ đỏ lộ ra: người nhà Kamo đó không thật sự là người nhà Kamo. Cơ thể ông ta đã bị một kẻ khác chiếm lấy.

[pause] Kaku ghi chú: một người anh trong số chín sinh mệnh ấy, khi gặp lại kẻ này ở hiện tại, đã nhận ra ngay khuôn mặt của kẻ đã tạo ra mình.
```

### c04 · Sợi chỉ đỏ: Kenjaku / 2006: chuyến hộ tống

Khoảng 140 giây · cảnh s35–s46 · 1816 ký tự

**Gemini**

```text
Đã đến lúc gọi tên sợi chỉ đỏ: Kenjaku. Một chú thuật sư từ thời Heian, có thuật thức cho phép chiếm cơ thể người khác bằng cách thay bộ não.

<short pause> Dấu hiệu nhận biết là một đường khâu chạy ngang trán của cơ thể bị chiếm. Nhờ đó, kẻ này sống qua hết thời đại này tới thời đại khác, dưới nhiều khuôn mặt khác nhau.

<short pause> Thời Heian, thời Minh Trị, và ở hiện tại, hắn mang cơ thể của một chú thuật sư đặc cấp đã chết, người bạn thân nhất ngày xưa của người mạnh nhất.

<short pause> Mục đích của hắn? Hắn muốn đẩy loài người tới một bước tiến hóa mới bằng chú lực, dù phải hy sinh bao nhiêu mạng sống.

<short pause> Điều đáng sợ nhất ở Kenjaku là sự kiên nhẫn. Hắn không vội. Hắn chờ đợi hàng trăm năm, thu thập từng mảnh ghép, và chỉ ra tay khi mọi thứ đã sẵn sàng.

<short pause> <laugh> Kaku ghi chú: một nghìn năm, nhiều khuôn mặt, một kế hoạch. Hắn là lý do vì sao dòng thời gian này có một sợi chỉ xuyên suốt.

<short pause> Nhảy tới thời hiện đại. Năm 2006, chiếc đèn lồng thứ năm trăm năm lại được thắp: đã tới lúc Thiên Nguyên hợp nhất với vật chứa Tinh Tương mới.

<short pause> Hai học sinh năm hai của trường chú thuật Tokyo được giao nhiệm vụ hộ tống cô gái làm vật chứa. Hai cậu là bộ đôi mạnh nhất thế hệ, và là bạn thân của nhau.

<short pause> Nhưng một sát thủ không có chú lực, được thuê để giết cô gái, đã phá hỏng tất cả. Cô gái chết, và lần hợp nhất năm trăm năm thất bại.

<short pause> Trong trận chiến đó, một trong hai học sinh suýt chết, rồi thức tỉnh sức mạnh vượt bậc, trở thành người mạnh nhất. Người còn lại bắt đầu nghi ngờ tất cả những gì mình tin.

<short pause> Sau lần đó, người học sinh suýt chết ấy trở thành chú thuật sư mà mọi người gọi là mạnh nhất. Người bạn của anh thì mang theo một câu hỏi không lời đáp: bảo vệ những người không có chú lực để làm gì?

<short pause> Kaku ghi chú: đây là điểm rẽ quan trọng nhất của thời hiện đại. Một người trở nên mạnh nhất, một người bắt đầu lạc lối. Và kẻ mang đường khâu trên trán sẽ tận dụng cả hai.
```

**ElevenLabs**

```text
Đã đến lúc gọi tên sợi chỉ đỏ: Kenjaku. Một chú thuật sư từ thời Heian, có thuật thức cho phép chiếm cơ thể người khác bằng cách thay bộ não.

[pause] Dấu hiệu nhận biết là một đường khâu chạy ngang trán của cơ thể bị chiếm. Nhờ đó, kẻ này sống qua hết thời đại này tới thời đại khác, dưới nhiều khuôn mặt khác nhau.

[pause] Thời Heian, thời Minh Trị, và ở hiện tại, hắn mang cơ thể của một chú thuật sư đặc cấp đã chết, người bạn thân nhất ngày xưa của người mạnh nhất.

[pause] [curious] Mục đích của hắn? Hắn muốn đẩy loài người tới một bước tiến hóa mới bằng chú lực, dù phải hy sinh bao nhiêu mạng sống.

[pause] Điều đáng sợ nhất ở Kenjaku là sự kiên nhẫn. Hắn không vội. Hắn chờ đợi hàng trăm năm, thu thập từng mảnh ghép, và chỉ ra tay khi mọi thứ đã sẵn sàng.

[pause] [chuckles] Kaku ghi chú: một nghìn năm, nhiều khuôn mặt, một kế hoạch. Hắn là lý do vì sao dòng thời gian này có một sợi chỉ xuyên suốt.

[pause] Nhảy tới thời hiện đại. Năm 2006, chiếc đèn lồng thứ năm trăm năm lại được thắp: đã tới lúc Thiên Nguyên hợp nhất với vật chứa Tinh Tương mới.

[pause] Hai học sinh năm hai của trường chú thuật Tokyo được giao nhiệm vụ hộ tống cô gái làm vật chứa. Hai cậu là bộ đôi mạnh nhất thế hệ, và là bạn thân của nhau.

[pause] Nhưng một sát thủ không có chú lực, được thuê để giết cô gái, đã phá hỏng tất cả. Cô gái chết, và lần hợp nhất năm trăm năm thất bại.

[pause] Trong trận chiến đó, một trong hai học sinh suýt chết, rồi thức tỉnh sức mạnh vượt bậc, trở thành người mạnh nhất. Người còn lại bắt đầu nghi ngờ tất cả những gì mình tin.

[pause] Sau lần đó, người học sinh suýt chết ấy trở thành chú thuật sư mà mọi người gọi là mạnh nhất. Người bạn của anh thì mang theo một câu hỏi không lời đáp: bảo vệ những người không có chú lực để làm gì?

[pause] Kaku ghi chú: đây là điểm rẽ quan trọng nhất của thời hiện đại. Một người trở nên mạnh nhất, một người bắt đầu lạc lối. Và kẻ mang đường khâu trên trán sẽ tận dụng cả hai.
```

### c05 · 2007 đến 2017: kẻ phản bội và bách quỷ dạ hành / 2018: năm mọi thứ sụp đổ

Khoảng 130 giây · cảnh s47–s58 · 1693 ký tự

**Gemini**

```text
Năm 2007, người học sinh lạc lối ấy rời bỏ giới chú thuật, sau khi gây ra một vụ thảm sát ở một ngôi làng. Anh tin rằng người không có chú lực là nguồn gốc của mọi chú linh.

<short pause> Mười năm sau, vào đêm Giáng sinh năm 2017, anh tổ chức một cuộc tấn công lớn gọi là Bách quỷ dạ hành, thả hàng nghìn chú linh xuống Tokyo và Kyoto.

<short pause> Đó là câu chuyện của phim Jujutsu Kaisen số 0, với nhân vật chính là một cậu học sinh bị một linh hồn nguyền rủa cực mạnh đi theo.

<short pause> Cuối trận, người bạn thân năm xưa, giờ là người mạnh nhất, tự tay kết liễu kẻ phản bội. Cái chết đó tưởng như khép lại một chương.

<short pause> Nhưng cơ thể của kẻ phản bội đã không được xử lý đúng cách. Và ai đó, với một đường khâu mới trên trán, đã lấy nó đi.

<short pause> Năm 2018. Tháng sáu, một học sinh cấp ba bình thường tên là Yuji nuốt một ngón tay của Sukuna để cứu bạn mình, và trở thành vật chứa của vua nguyền rủa.

<short pause> Cậu được tha án tử với một điều kiện: ăn hết hai mươi ngón tay, rồi chết cùng Sukuna. Đó là khởi đầu của câu chuyện mà ta biết.

<short pause> Ngày 31 tháng 10 năm 2018, đêm Halloween, ở khu Shibuya, kẻ mang cơ thể của người phản bội thực hiện một bước quan trọng nhất của kế hoạch một nghìn năm.

<short pause> Người mạnh nhất bị dụ vào một cái bẫy và bị phong ấn trong một chú vật gọi là Ngục môn cương. Không có anh, cán cân quyền lực sụp đổ.

<short pause> Và Sukuna được giải phóng trong chốc lát giữa Shibuya, gây ra thảm họa khủng khiếp. Đêm đó thay đổi hoàn toàn thế giới chú thuật.

<short pause> Trong đêm đó, nhiều nhân vật quan trọng ngã xuống, và những người sống sót không còn là con người cũ. Truyện không cho ai đi qua Shibuya mà không trả giá.

<short pause> <laugh> Kaku ghi chú: một nghìn năm chuẩn bị, và tất cả dồn vào một đêm lễ hội. Đó là lý do arc Shibuya được xem là một trong những arc hay nhất của truyện.
```

**ElevenLabs**

```text
Năm 2007, người học sinh lạc lối ấy rời bỏ giới chú thuật, sau khi gây ra một vụ thảm sát ở một ngôi làng. Anh tin rằng người không có chú lực là nguồn gốc của mọi chú linh.

[pause] Mười năm sau, vào đêm Giáng sinh năm 2017, anh tổ chức một cuộc tấn công lớn gọi là Bách quỷ dạ hành, thả hàng nghìn chú linh xuống Tokyo và Kyoto.

[pause] Đó là câu chuyện của phim Jujutsu Kaisen số 0, với nhân vật chính là một cậu học sinh bị một linh hồn nguyền rủa cực mạnh đi theo.

[pause] Cuối trận, người bạn thân năm xưa, giờ là người mạnh nhất, tự tay kết liễu kẻ phản bội. Cái chết đó tưởng như khép lại một chương.

[pause] Nhưng cơ thể của kẻ phản bội đã không được xử lý đúng cách. Và ai đó, với một đường khâu mới trên trán, đã lấy nó đi.

[pause] Năm 2018. Tháng sáu, một học sinh cấp ba bình thường tên là Yuji nuốt một ngón tay của Sukuna để cứu bạn mình, và trở thành vật chứa của vua nguyền rủa.

[pause] Cậu được tha án tử với một điều kiện: ăn hết hai mươi ngón tay, rồi chết cùng Sukuna. Đó là khởi đầu của câu chuyện mà ta biết.

[pause] Ngày 31 tháng 10 năm 2018, đêm Halloween, ở khu Shibuya, kẻ mang cơ thể của người phản bội thực hiện một bước quan trọng nhất của kế hoạch một nghìn năm.

[pause] Người mạnh nhất bị dụ vào một cái bẫy và bị phong ấn trong một chú vật gọi là Ngục môn cương. Không có anh, cán cân quyền lực sụp đổ.

[pause] Và Sukuna được giải phóng trong chốc lát giữa Shibuya, gây ra thảm họa khủng khiếp. Đêm đó thay đổi hoàn toàn thế giới chú thuật.

[pause] Trong đêm đó, nhiều nhân vật quan trọng ngã xuống, và những người sống sót không còn là con người cũ. Truyện không cho ai đi qua Shibuya mà không trả giá.

[pause] [chuckles] Kaku ghi chú: một nghìn năm chuẩn bị, và tất cả dồn vào một đêm lễ hội. Đó là lý do arc Shibuya được xem là một trong những arc hay nhất của truyện.
```

### c06 · Sau Shibuya: Trò chơi tử diệt / Bản đồ những nơi quan trọng / Những khoảng trống trên dòng thời gian

Khoảng 146 giây · cảnh s59–s72 · 1892 ký tự

**Gemini**

```text
Sau Shibuya, kẻ mang đường khâu công bố bước tiếp theo: một trò chơi sinh tử trên khắp Nhật Bản, gọi là Trò chơi tử diệt.

<short pause> Hắn đánh thức sức mạnh ở nhiều người, và còn đưa những chú thuật sư từ nhiều thời đại quá khứ trở lại trong cơ thể người hiện đại, buộc tất cả chiến đấu với nhau.

<short pause> Đây là phần mùa ba của anime, bắt đầu phát từ tháng một năm 2026. Phần tiếp theo sẽ là mùa bốn.

<short pause> <laugh> Kaku dừng dòng thời gian ở đây để tránh spoiler. Chỉ cần biết: đây là lúc những chiếc đèn lồng từ mọi thời đại bị thắp lên cùng một lúc.

<short pause> Trước khi tổng kết, hãy đặt các sự kiện lên bản đồ. Dòng thời gian này không chỉ trải dài theo năm, mà còn trải khắp nước Nhật.

<short pause> Kyoto, kinh đô thời Heian, là nơi mọi thứ bắt đầu. Ngày nay, ở đó có một trong hai trường chú thuật của Nhật Bản, nổi tiếng bảo thủ và gắn chặt với các gia tộc cũ.

<short pause> Tokyo có trường chú thuật còn lại, nơi Yuji và bạn bè theo học. Sâu bên dưới trường là nơi ở của Thiên Nguyên, trung tâm của mọi kết giới.

<short pause> Shibuya, khu phố đông đúc bậc nhất Tokyo, trở thành chiến trường của đêm Halloween năm 2018.

<short pause> Và sau Shibuya, Trò chơi tử diệt biến nhiều khu vực trên khắp Nhật Bản thành những vùng kết giới khép kín, nơi người chơi buộc phải chiến đấu.

<short pause> Kaku ghi chú: một kế hoạch bắt đầu ở kinh đô cổ, và kết thúc bằng việc biến cả đất nước thành sân chơi. Kenjaku thật sự nghĩ rất xa.

<short pause> Dòng thời gian của Kaku vẫn còn những khoảng trống. Ở mức spoiler của video này, có vài câu hỏi truyện chưa trả lời trọn vẹn.

<short pause> Một: Sukuna đã sống thế nào ở thời Heian, và vì sao hắn trở thành con người đáng sợ nhất thời đại? Truyện chỉ hé lộ từng mảnh nhỏ.

<short pause> Hai: người hầu trung thành của Sukuna thật sự là ai, và vì sao lại trung thành suốt một nghìn năm? Ba: kế hoạch của Kenjaku bắt đầu từ khi nào, và hắn đã chiếm bao nhiêu cơ thể khác mà ta chưa biết?

<short pause> Bạn nào đã đọc manga tới cuối chắc biết thêm một vài câu trả lời. <short pause> Nhưng hãy giúp người khác, đừng spoiler trong phần bình luận nhé.
```

**ElevenLabs**

```text
Sau Shibuya, kẻ mang đường khâu công bố bước tiếp theo: một trò chơi sinh tử trên khắp Nhật Bản, gọi là Trò chơi tử diệt.

[pause] Hắn đánh thức sức mạnh ở nhiều người, và còn đưa những chú thuật sư từ nhiều thời đại quá khứ trở lại trong cơ thể người hiện đại, buộc tất cả chiến đấu với nhau.

[pause] Đây là phần mùa ba của anime, bắt đầu phát từ tháng một năm 2026. Phần tiếp theo sẽ là mùa bốn.

[pause] [chuckles] Kaku dừng dòng thời gian ở đây để tránh spoiler. Chỉ cần biết: đây là lúc những chiếc đèn lồng từ mọi thời đại bị thắp lên cùng một lúc.

[pause] Trước khi tổng kết, hãy đặt các sự kiện lên bản đồ. Dòng thời gian này không chỉ trải dài theo năm, mà còn trải khắp nước Nhật.

[pause] Kyoto, kinh đô thời Heian, là nơi mọi thứ bắt đầu. Ngày nay, ở đó có một trong hai trường chú thuật của Nhật Bản, nổi tiếng bảo thủ và gắn chặt với các gia tộc cũ.

[pause] Tokyo có trường chú thuật còn lại, nơi Yuji và bạn bè theo học. Sâu bên dưới trường là nơi ở của Thiên Nguyên, trung tâm của mọi kết giới.

[pause] Shibuya, khu phố đông đúc bậc nhất Tokyo, trở thành chiến trường của đêm Halloween năm 2018.

[pause] Và sau Shibuya, Trò chơi tử diệt biến nhiều khu vực trên khắp Nhật Bản thành những vùng kết giới khép kín, nơi người chơi buộc phải chiến đấu.

[pause] Kaku ghi chú: một kế hoạch bắt đầu ở kinh đô cổ, và kết thúc bằng việc biến cả đất nước thành sân chơi. Kenjaku thật sự nghĩ rất xa.

[pause] Dòng thời gian của Kaku vẫn còn những khoảng trống. Ở mức spoiler của video này, có vài câu hỏi truyện chưa trả lời trọn vẹn.

[pause] [curious] Một: Sukuna đã sống thế nào ở thời Heian, và vì sao hắn trở thành con người đáng sợ nhất thời đại? Truyện chỉ hé lộ từng mảnh nhỏ.

[pause] Hai: người hầu trung thành của Sukuna thật sự là ai, và vì sao lại trung thành suốt một nghìn năm? Ba: kế hoạch của Kenjaku bắt đầu từ khi nào, và hắn đã chiếm bao nhiêu cơ thể khác mà ta chưa biết?

[pause] Bạn nào đã đọc manga tới cuối chắc biết thêm một vài câu trả lời. [pause] Nhưng hãy giúp người khác, đừng spoiler trong phần bình luận nhé.
```

### c07 · Toàn bộ dòng thời gian / Góc nhìn của Kaku: những kẻ không chịu chết / Kết

Khoảng 120 giây · cảnh s73–s84 · 1563 ký tự

**Gemini**

```text
Tổng kết cả dãy đèn lồng. Thời Heian, khoảng một nghìn năm trước: Sukuna thống trị, Kenjaku bắt đầu kế hoạch, Thiên Nguyên đã tồn tại.

<short pause> Khoảng bốn trăm năm trước: hai gia chủ Gojo và Zenin cùng gục ngã. Thời Minh Trị: người nhà Kamo bị chiếm xác tạo ra Cửu tướng đồ.

<short pause> 2006: lần hợp nhất năm trăm năm thất bại. 2007: kẻ phản bội rời đi. 2017: Bách quỷ dạ hành.

<short pause> 2018: Yuji nuốt ngón tay, sự kiện Shibuya, người mạnh nhất bị phong ấn, và Trò chơi tử diệt bắt đầu.

<short pause> <laugh> Nhìn cả dãy đèn lồng, Kaku nhận ra một điều: những nhân vật nguy hiểm nhất đều là những kẻ không chịu chết.

<short pause> Thiên Nguyên sống hơn một nghìn năm nhờ bất tử. Sukuna sống tiếp qua hai mươi ngón tay. Người hầu của hắn chờ đợi suốt nhiều thế kỷ. Kenjaku nhảy từ cơ thể này sang cơ thể khác.

<short pause> Trong khi đó, những nhân vật chính lại là những người trẻ, biết mình có thể chết bất cứ lúc nào. Truyện luôn nhắc về việc chết sao cho không hối tiếc.

<short pause> Kaku nghĩ đó là câu hỏi lớn của Jujutsu Kaisen: sống mãi mà không thay đổi, hay sống ngắn nhưng trọn vẹn? Một bên là những kẻ bám lấy quá khứ, một bên là những người sống cho hiện tại.

<short pause> Và có lẽ vì thế mà kẻ thù lớn nhất của truyện không phải một con quái vật, mà là một nghìn năm lịch sử không chịu buông tay.

<short pause> Câu hỏi cho bạn: nếu được sống qua một nghìn năm như Kenjaku, bạn muốn chứng kiến thời đại nào nhất? Viết vào phần bình luận nhé.

<short pause> Video tới, Kaku mang bảng tuần hoàn và kính bảo hộ ra lần nữa, để kiểm tra những phát minh của Senku trong Dr. Stone có thật sự làm được ngoài đời không.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. Kaku thổi tắt từng chiếc đèn lồng đây. Hẹn gặp lại!
```

**ElevenLabs**

```text
Tổng kết cả dãy đèn lồng. Thời Heian, khoảng một nghìn năm trước: Sukuna thống trị, Kenjaku bắt đầu kế hoạch, Thiên Nguyên đã tồn tại.

[pause] Khoảng bốn trăm năm trước: hai gia chủ Gojo và Zenin cùng gục ngã. Thời Minh Trị: người nhà Kamo bị chiếm xác tạo ra Cửu tướng đồ.

[pause] 2006: lần hợp nhất năm trăm năm thất bại. 2007: kẻ phản bội rời đi. 2017: Bách quỷ dạ hành.

[pause] 2018: Yuji nuốt ngón tay, sự kiện Shibuya, người mạnh nhất bị phong ấn, và Trò chơi tử diệt bắt đầu.

[pause] [chuckles] Nhìn cả dãy đèn lồng, Kaku nhận ra một điều: những nhân vật nguy hiểm nhất đều là những kẻ không chịu chết.

[pause] Thiên Nguyên sống hơn một nghìn năm nhờ bất tử. Sukuna sống tiếp qua hai mươi ngón tay. Người hầu của hắn chờ đợi suốt nhiều thế kỷ. Kenjaku nhảy từ cơ thể này sang cơ thể khác.

[pause] Trong khi đó, những nhân vật chính lại là những người trẻ, biết mình có thể chết bất cứ lúc nào. Truyện luôn nhắc về việc chết sao cho không hối tiếc.

[pause] [curious] Kaku nghĩ đó là câu hỏi lớn của Jujutsu Kaisen: sống mãi mà không thay đổi, hay sống ngắn nhưng trọn vẹn? Một bên là những kẻ bám lấy quá khứ, một bên là những người sống cho hiện tại.

[pause] Và có lẽ vì thế mà kẻ thù lớn nhất của truyện không phải một con quái vật, mà là một nghìn năm lịch sử không chịu buông tay.

[pause] Câu hỏi cho bạn: nếu được sống qua một nghìn năm như Kenjaku, bạn muốn chứng kiến thời đại nào nhất? Viết vào phần bình luận nhé.

[pause] Video tới, Kaku mang bảng tuần hoàn và kính bảo hộ ra lần nữa, để kiểm tra những phát minh của Senku trong Dr. Stone có thật sự làm được ngoài đời không.

[pause] Đăng ký kênh để không bỏ lỡ nhé. Kaku thổi tắt từng chiếc đèn lồng đây. Hẹn gặp lại!
```
