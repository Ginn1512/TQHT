# Bộ prompt · Kimetsu no Yaiba: Cây phả hệ các kiểu Hơi thở

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 94 ảnh, 7 đoạn đọc, khoảng 14.7 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (94 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Kimetsu no Yaiba đến hết bộ truyện, gồm cả arc Vô Hạn Thành. Nếu bạn chỉ xem anime…

```text
Wide 16:9 landscape cinematic frame. a dark wooden dojo with a single katana resting on a stand, moonlight through paper doors. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong Kimetsu no Yaiba, con người nhỏ bé chống lại những con quỷ bất tử. Vũ khí của họ không chỉ là thanh kiế…

```text
Wide 16:9 landscape cinematic frame. a small swordsman silhouette facing a towering demon shadow on a moonlit mountain path. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nước, lửa, sấm, gió, đá, hoa, côn trùng, âm thanh, tình yêu... Có rất nhiều kiểu hơi thở. Nhưng chúng không x…

```text
Wide 16:9 landscape cinematic frame. a circle of swirling elemental energies: water, flame, lightning, wind, stone, petals, and sound waves. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Tất cả đều bắt nguồn từ một hơi thở duy nhất, và có thể vẽ thành một cây phả hệ giống như cây gia phả của một…

```text
Wide 16:9 landscape cinematic frame. a giant glowing tree whose roots are a single sun and whose branches are different elements. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ vẽ cây phả hệ hơi thở: gốc rễ ở đâu, các nhánh tách ra thế nào, v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook where a small tree diagram grows from the pages. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ biết vì sao gần như tất cả các kiểu hơi thở đều là phiên bản đơn giản hóa của một kỹ th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a golden sun at the top of a chalkboard family tree. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Hơi thở là gì?

Lời: Trước hết, hơi thở trong truyện là gì? Đó là kỹ thuật thở đặc biệt giúp đưa thật nhiều oxy vào máu, tăng sức…

```text
Wide 16:9 landscape cinematic frame. an anatomical style illustration of lungs glowing with light, energy flowing through blood vessels. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhờ hơi thở, một con người có thể chạy nhanh, chém mạnh và chịu đựng vết thương đủ để đối đầu với quỷ, loài c…

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette leaping impossibly high over a demon, breath visible as a glowing mist. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Cấp độ cao hơn là duy trì hơi thở toàn tập liên tục, kể cả khi ngủ. Người làm được điều này có sức bền tăng v…

```text
Wide 16:9 landscape cinematic frame. a sleeping figure on a futon, faint rhythmic glow of breath around them in the dark. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Luyện hơi thở cực khổ. Học viên phải chạy núi, chịu đựng, tập thở đến mức phổi như muốn nổ tung, trong nhiều…

```text
Wide 16:9 landscape cinematic frame. a young trainee running up a misty mountain path at dawn, exhausted but determined. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Mỗi kiểu hơi thở đi kèm một bộ thế kiếm, thường gọi là thức. Mỗi thức là một cách tận dụng hơi thở theo phong…

```text
Wide 16:9 landscape cinematic frame. a sequence of sword stances drawn like a martial arts manual, each with a flowing elemental trail. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Và thanh kiếm Nhật Luân của mỗi kiếm sĩ đổi màu theo người cầm. Màu kiếm gợi ý kiểu hơi thở phù hợp với họ.

```text
Wide 16:9 landscape cinematic frame. a row of katanas with blades in different colors: blue, red, yellow, green, grey, pink. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hơi thở giống như phong cách võ thuật. Cùng một nền tảng thể lực, nhưng mỗi môn phái có cách ra…

```text
Wide 16:9 landscape cinematic frame. the owl mascot practicing a tiny sword pose with a wooden stick, breathing out a small cloud. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Đối thủ: vì sao phải có hơi thở?

Lời: Để thấy hơi thở quan trọng thế nào, cần hiểu đối thủ. Quỷ trong truyện khỏe hơn người rất nhiều, và gần như k…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette regenerating a severed arm in seconds under moonlight. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Quỷ hồi phục vết thương gần như ngay lập tức. Chặt tay thì tay mọc lại, đâm xuyên thì vết thương liền. Chúng…

```text
Wide 16:9 landscape cinematic frame. a diagram of a demon body with glowing regeneration lines closing wounds. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Điểm yếu thứ nhất là ánh mặt trời. Quỷ tan biến khi bị ánh nắng chiếu trực tiếp. Vì vậy chúng chỉ hoạt động v…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette crumbling into ash as the first rays of sunrise hit it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Điểm yếu thứ hai là bị chém đứt đầu bằng kiếm Nhật Luân, loại kiếm rèn từ quặng hấp thụ ánh mặt trời.

```text
Wide 16:9 landscape cinematic frame. a blacksmith forging a glowing blade from sun-bathed ore on a mountain forge. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhưng cổ của quỷ mạnh cứng như thép. Không có hơi thở, con người không đủ sức và tốc độ để chém đứt nó.

```text
Wide 16:9 landscape cinematic frame. a sword striking a demon's neck and stopping with sparks, the swordsman straining. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nhiều con quỷ còn có Huyết quỷ thuật, năng lực đặc biệt riêng như điều khiển chỉ, tạo ảo ảnh, hay thao túng k…

```text
Wide 16:9 landscape cinematic frame. a demon manipulating razor-sharp threads glowing red across a dark forest. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Hơi thở chính là cây cầu giúp con người vượt qua khoảng cách đó: đủ nhanh để né, đủ mạnh để chém, đủ bền để t…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman standing between a demon and the rising sun, blade ready. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Con đường trở thành kiếm sĩ

Lời: Để học được hơi thở, một người bình thường phải đi qua con đường rất dài. Truyện cho ta thấy khá rõ con đường…

```text
Wide 16:9 landscape cinematic frame. a long mountain path winding through mist, a small traveler with a box on his back walking upward. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Bước đầu là tìm một người thầy. Thường đó là một kiếm sĩ đã giải nghệ, sống ẩn trong núi và chỉ nhận vài học…

```text
Wide 16:9 landscape cinematic frame. an old masked mentor silhouette standing outside a small hut on a misty mountain. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Việc luyện tập kéo dài nhiều tháng tới nhiều năm: chạy núi trong không khí loãng, né bẫy, tập chém, tập thở c…

```text
Wide 16:9 landscape cinematic frame. a trainee running through a forest full of swinging log traps at dawn. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Có những bài kiểm tra tưởng như không thể, như chém đôi một tảng đá khổng lồ. Chỉ khi vượt qua, người thầy mớ…

```text
Wide 16:9 landscape cinematic frame. a young swordsman standing before a massive boulder, blade raised, determined. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Bước tiếp theo là Kỳ tuyển chọn cuối cùng: sống sót bảy ngày trên một ngọn núi đầy quỷ, được bao quanh bởi ho…

```text
Wide 16:9 landscape cinematic frame. a mountain ringed with blooming purple wisteria at night, shadows of demons inside. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Chỉ ai sống sót mới được vào Sát Quỷ Đoàn, nhận kiếm Nhật Luân và một con quạ đưa tin. Nhiều người không bao…

```text
Wide 16:9 landscape cinematic frame. a crow perched on a newly forged sword resting on a stone, morning light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và vào đoàn mới chỉ là khởi đầu. Kiếm sĩ phải tiếp tục luyện, từ cấp thấp nhất, trải qua hàng loạt trận chiến…

```text
Wide 16:9 landscape cinematic frame. a line of new recruits in dark uniforms looking up at a long staircase leading into clouds. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: đây là lý do người xem trân trọng mỗi lần một nhân vật mạnh lên. Mọi bước tiến đều được xây bằ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wiping sweat from its brow after climbing a tiny hill. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Gốc rễ: Hơi thở Mặt Trời

Lời: Ở gốc cây phả hệ là Hơi thở Mặt Trời, hơi thở đầu tiên. Nó được tạo ra bởi một kiếm sĩ huyền thoại từ nhiều t…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman silhouette from a past era standing before a rising sun, earring charms swaying. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Yoriichi được miêu tả là người mạnh nhất trong lịch sử diệt quỷ. Ông sinh ra đã có những khả năng mà người kh…

```text
Wide 16:9 landscape cinematic frame. an ancient scroll painting of a calm swordsman surrounded by fallen demon shadows. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Ông dạy kỹ thuật thở cho những kiếm sĩ khác. Nhưng không ai học được Hơi thở Mặt Trời trọn vẹn như ông.

```text
Wide 16:9 landscape cinematic frame. a group of old-era swordsmen silhouettes watching a single master perform a flowing sun technique. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Vì thế, mỗi người học lấy phần mà họ làm được, rồi kết hợp với phong cách riêng. Từ đó sinh ra năm hơi thở cơ…

```text
Wide 16:9 landscape cinematic frame. a sun splitting into five beams of different colors, each beam landing on a different swordsman. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Đây là ý tưởng rất hay: tất cả những hơi thở ta biết đều là phiên bản rút gọn của một kỹ thuật hoàn hảo đã gầ…

```text
Wide 16:9 landscape cinematic frame. a perfect golden circle fragmenting into smaller imperfect colored arcs. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · 5 nhánh chính

Lời: Năm hơi thở cơ bản, nhánh lớn của cây, là: Nước, Lửa, Sấm, Gió và Đá. Mỗi nhánh có tính cách riêng.

```text
Wide 16:9 landscape cinematic frame. a family tree diagram with five thick branches, each branch colored by its element. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Hơi thở Nước mềm mại và linh hoạt. Thức kiếm như dòng chảy, thích nghi với mọi loại đối thủ. Đây là hơi thở d…

```text
Wide 16:9 landscape cinematic frame. a flowing water dragon spiraling around a swordsman's blade in a forest river. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Hơi thở Lửa mạnh mẽ, dồn lực tấn công trực diện. Nó hợp với người có ý chí rực cháy và dám xông thẳng vào đối…

```text
Wide 16:9 landscape cinematic frame. a blazing flame arc trailing behind a charging sword strike at night. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Hơi thở Sấm tập trung vào tốc độ, dồn lực vào chân để lao đi như tia chớp. Có người chỉ học được đúng một thứ…

```text
Wide 16:9 landscape cinematic frame. a streak of yellow lightning across a dark field, a crouched swordsman at its origin. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Hơi thở Gió dữ dội, những nhát chém như lốc xoáy. Nó hợp với người hung hăng, liều lĩnh.

```text
Wide 16:9 landscape cinematic frame. a violent whirlwind of sharp green wind blades tearing through leaves around a swordsman. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Hơi thở Đá dựa vào sức mạnh thể chất khổng lồ và phòng thủ vững chắc. Người dùng mạnh nhất trong truyện được…

```text
Wide 16:9 landscape cinematic frame. a giant stone-like figure silhouette swinging a spiked flail and axe connected by a chain. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Mỗi nhánh này lại tiếp tục mọc ra những nhánh con khi các kiếm sĩ đời sau cải biên cho hợp với bản thân.

```text
Wide 16:9 landscape cinematic frame. the family tree growing smaller glowing twigs from each main branch, like a time-lapse. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Các nhánh con

Lời: Giờ đi xuống các nhánh con. Từ Nước sinh ra Hơi thở Hoa, mềm mại và đẹp, tập trung vào sự chính xác.

```text
Wide 16:9 landscape cinematic frame. cherry blossom petals swirling around a graceful sword arc, flowing from a water stream. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Từ Hoa lại sinh ra Hơi thở Côn trùng, dành cho người không đủ sức để chém đứt đầu quỷ. Thay vào đó, họ dùng m…

```text
Wide 16:9 landscape cinematic frame. a delicate needle-like blade with a butterfly motif, a drop of glowing poison at the tip. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Đây là ví dụ đẹp về việc hệ thống thích nghi: người yếu về sức vẫn tìm ra cách đánh bại quỷ bằng trí tuệ và y…

```text
Wide 16:9 landscape cinematic frame. a small figure in a plain long coat studying vials in a candlelit clinic, silhouette only. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Cũng từ Nước sinh ra Hơi thở Rắn, với những đường kiếm uốn lượn khó đoán như rắn trườn.

```text
Wide 16:9 landscape cinematic frame. a sinuous serpent-shaped sword trail winding between trees in a dark forest. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Từ Lửa sinh ra Hơi thở Tình yêu, dùng một thanh kiếm mỏng dẻo như roi, kết hợp sự linh hoạt đặc biệt của cơ t…

```text
Wide 16:9 landscape cinematic frame. a thin whip-like pink blade curling through the air in elegant spirals. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Từ Sấm sinh ra Hơi thở Âm thanh, kết hợp tiếng nổ và nhịp điệu. Người dùng đọc nhịp chiến đấu như đọc một bản…

```text
Wide 16:9 landscape cinematic frame. twin cleavers connected by a chain with small explosions like musical notes bursting around them. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Từ Gió sinh ra Hơi thở Sương mù, khó đoán, lúc ẩn lúc hiện, làm đối thủ không bắt được hướng tấn công.

```text
Wide 16:9 landscape cinematic frame. a swordsman fading in and out of a thick mist, only the glint of a blade visible. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Và có một hơi thở tự học: Hơi thở Thú, do một người lớn lên trong núi tự sáng tạo, với lối đánh hoang dã bằng…

```text
Wide 16:9 landscape cinematic frame. a wild figure wearing a boar-like mask silhouette crouching with two jagged blades in a mountain forest. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: cây phả hệ cho thấy mỗi hơi thở mới ra đời để phù hợp với cơ thể và tính cách của một người. Kh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adding a small new twig to a glowing family tree with a brush. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Trụ cột: những bậc thầy hơi thở

Lời: Những người thành thạo hơi thở nhất trong Sát Quỷ Đoàn được gọi là Trụ cột. Mỗi Trụ cột thường đại diện cho m…

```text
Wide 16:9 landscape cinematic frame. nine swordsman silhouettes standing on pillars of different colors in a misty garden. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Sát Quỷ Đoàn có hệ thống cấp bậc từ thấp tới cao. Trụ cột đứng ở đỉnh, ngay dưới người đứng đầu tổ chức.

```text
Wide 16:9 landscape cinematic frame. a vertical rank ladder with ten small emblems and a crowned tier at the top. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Theo truyện, để trở thành Trụ cột, kiếm sĩ phải tiêu diệt khoảng năm mươi con quỷ, hoặc hạ một trong Thập Nhị…

```text
Wide 16:9 landscape cinematic frame. a tally of fifty small marks on a wooden wall next to a single crescent moon symbol. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Mỗi Trụ cột có tính cách gắn với hơi thở của họ: người dùng Lửa nhiệt huyết, người dùng Nước điềm tĩnh, người…

```text
Wide 16:9 landscape cinematic frame. a split portrait of three silhouettes: one with blazing flames, one calm with water, one fierce with wind. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Điều này quay lại ý chính của video: hơi thở không chỉ là kỹ thuật, nó là con người. Người ta tìm ra hơi thở…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a swordsman as a swirl of their own elemental energy. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây giống thuyết tính cách của Nen mà mình từng nhắc. Nhiều bộ truyện đều có chung ý: sức mạnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two small cards, one with a hexagon and one with a flame. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Nhánh bóng tối: Hơi thở Mặt Trăng

Lời: Cây phả hệ này còn một nhánh mà ít ai nhắc tới vì nó thuộc về kẻ thù: Hơi thở Mặt Trăng.

```text
Wide 16:9 landscape cinematic frame. a pale crescent moon casting cold light over a dark branch of the family tree. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Nó được tạo ra bởi anh trai song sinh của Yoriichi. Người này không thể đạt tới Hơi thở Mặt Trời, nên tạo ra…

```text
Wide 16:9 landscape cinematic frame. two sibling silhouettes back to back, one bathed in sunlight, one in moonlight. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Vì khao khát sức mạnh và nỗi sợ cái chết, anh ta đã trở thành quỷ, và sau này là một trong những con quỷ mạnh…

```text
Wide 16:9 landscape cinematic frame. a samurai silhouette with multiple glowing eyes standing under a blood-red moon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hơi thở Mặt Trăng tạo ra những nhát chém có vô số lưỡi trăng nhỏ đi kèm, rất khó đỡ vì chúng thay đổi kích th…

```text
Wide 16:9 landscape cinematic frame. a sword slash surrounded by countless small crescent-shaped blades scattering unpredictably. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Đây là nhánh bi kịch nhất của cây phả hệ: cùng một gốc, nhưng một người trở thành huyền thoại, người kia trở…

```text
Wide 16:9 landscape cinematic frame. a single tree splitting into a bright golden branch and a withered pale branch. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Hơi thở Mặt Trời không thất truyền

Lời: Nếu Hơi thở Mặt Trời không ai học được, sao nó vẫn còn tồn tại? Câu trả lời nằm ở một điệu múa.

```text
Wide 16:9 landscape cinematic frame. a family performing a ritual fire dance on a snowy mountain at night, torches glowing. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Gia đình Kamado truyền lại một điệu múa cầu thần qua nhiều thế hệ, múa suốt đêm vào mỗi dịp đầu năm, cùng đôi…

```text
Wide 16:9 landscape cinematic frame. a pair of hanafuda-style sun earrings on a wooden table beside a torch, snow falling outside. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Điệu múa đó thực chất chính là các thế của Hơi thở Mặt Trời, được giữ gìn dưới dạng nghi lễ, không ai biết đó…

```text
Wide 16:9 landscape cinematic frame. a dance diagram where each graceful movement overlaps with a glowing sword slash. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Tanjiro nhớ lại điệu múa của cha mình trong lúc sinh tử, và dần dần đánh thức lại kỹ thuật tưởng như đã mất.

```text
Wide 16:9 landscape cinematic frame. a young swordsman silhouette remembering a fire dance, flames blooming around his blade. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích chi tiết này: kỹ thuật mạnh nhất không được cất trong sách bí truyền, mà được giữ bởi một gia…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small torch respectfully in a snowy night. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Vượt giới hạn: Ấn, Thế giới trong suốt và kiếm đỏ

Lời: Ở cuối truyện, các kiếm sĩ mạnh nhất phải vượt qua giới hạn con người để đối đầu với những con quỷ hùng mạnh.…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols: a flame-shaped mark, a transparent human outline, and a red-hot blade. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Thứ nhất là Ấn, một hình vẽ xuất hiện trên cơ thể khi kiếm sĩ đạt trạng thái đặc biệt. Người có Ấn tăng sức m…

```text
Wide 16:9 landscape cinematic frame. a flame-like glowing mark appearing across a swordsman's forehead and neck. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Truyện cho biết Ấn xuất hiện khi thân nhiệt vượt khoảng ba mươi chín độ và nhịp tim vượt khoảng hai trăm lần…

```text
Wide 16:9 landscape cinematic frame. a medical style chart with a thermometer and a heart rate line spiking dramatically. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nhưng Ấn có cái giá khủng khiếp: theo truyện, người có Ấn sẽ không sống quá hai mươi lăm tuổi. Chỉ duy nhất Y…

```text
Wide 16:9 landscape cinematic frame. an hourglass with glowing sand draining quickly beside a young swordsman silhouette. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Thứ hai là Thế giới trong suốt, khả năng nhìn xuyên cơ thể đối thủ, thấy cơ bắp, xương và dòng máu. Nhờ đó đọ…

```text
Wide 16:9 landscape cinematic frame. a transparent human figure showing muscles, bones, and flowing blood in glowing lines. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Thứ ba là kiếm đỏ, khi kiếm sĩ nắm chặt thanh kiếm với sức mạnh cực lớn, lưỡi kiếm chuyển đỏ và gây vết thươn…

```text
Wide 16:9 landscape cinematic frame. a katana blade glowing bright red under an intense grip, heat distortion around it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Cả ba đều từng là khả năng tự nhiên của Yoriichi. Những người đời sau chỉ đạt được chúng bằng cách đẩy cơ thể…

```text
Wide 16:9 landscape cinematic frame. a golden silhouette at the top of a staircase while exhausted figures climb toward him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Trắc nghiệm: bạn hợp với hơi thở nào?

Lời: Giờ chơi một trò nhỏ. Dựa trên cách truyện gắn tính cách với hơi thở, hãy xem bạn hợp với nhánh nào nhất. Đây…

```text
Wide 16:9 landscape cinematic frame. a playful quiz card with six elemental icons arranged in a circle. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nếu bạn điềm tĩnh, dễ thích nghi, biết lắng nghe, có thể bạn hợp với Hơi thở Nước.

```text
Wide 16:9 landscape cinematic frame. a calm figure sitting by a quiet river at dawn, water swirling gently around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nếu bạn nhiệt huyết, thích dẫn đầu, luôn tràn năng lượng, Hơi thở Lửa có lẽ là của bạn.

```text
Wide 16:9 landscape cinematic frame. a figure standing in front of a crowd holding a torch high, warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn sợ hãi nhiều thứ nhưng dồn hết vào một điều mình làm tốt nhất, Hơi thở Sấm là lựa chọn hay.

```text
Wide 16:9 landscape cinematic frame. a nervous figure crouching, then a single brilliant flash of lightning. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nếu bạn khéo léo, tinh tế, dùng trí tuệ thay vì sức mạnh, Hơi thở Côn trùng hoặc Hoa có thể hợp với bạn.

```text
Wide 16:9 landscape cinematic frame. a delicate figure surrounded by butterflies and falling petals, holding a thin blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu bạn thích tự mình mày mò, không theo khuôn phép nào, có khi bạn sẽ tự tạo ra một nhánh mới như Hơi thở Th…

```text
Wide 16:9 landscape cinematic frame. a wild figure drawing a brand new branch on the family tree with a stick. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Những hiểu lầm về hơi thở

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về hệ thống hơi thở.

```text
Wide 16:9 landscape cinematic frame. a notice board with four pinned cards marked with question marks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Hiểu lầm một: hơi thở là phép thuật tạo ra nước hay lửa thật. Không phải. Nước, lửa hay sấm chỉ là cách truyệ…

```text
Wide 16:9 landscape cinematic frame. a sword slash drawn half as a stylized water dragon and half as a plain steel arc. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hiểu lầm hai: màu kiếm quyết định hơi thở. Màu kiếm chỉ gợi ý thiên hướng, người dùng vẫn có thể học hơi thở…

```text
Wide 16:9 landscape cinematic frame. a blade glowing one color while its wielder practices a stance of a different element. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Hiểu lầm ba: nhánh con yếu hơn nhánh chính. Thực tế nhiều Trụ cột dùng nhánh con và vẫn thuộc hàng mạnh nhất.

```text
Wide 16:9 landscape cinematic frame. a thin branch of the family tree glowing as brightly as the thick main branches. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hiểu lầm bốn: có Ấn là chắc chắn thắng. Ấn giúp mạnh hơn, nhưng trong những trận cuối, cả những người có Ấn v…

```text
Wide 16:9 landscape cinematic frame. a marked swordsman kneeling exhausted on a battlefield at dawn. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Góc nhìn của Kaku: sức mạnh có giá · **Kaku** (đính kèm ảnh mẫu)

Lời: Điều khiến mình ấn tượng nhất với hệ thống hơi thở là nó luôn nhắc rằng con người có giới hạn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting beside a candle in a quiet dojo, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Quỷ bất tử, hồi phục gần như tức thì. Con người thì mỏi mệt, bị thương, và có tuổi thọ. Hơi thở là cách con n…

```text
Wide 16:9 landscape cinematic frame. a split image: a demon regenerating a lost arm, and a tired human bandaging a wound. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Nhưng thu hẹp khoảng cách luôn có giá: phải luyện tập đến kiệt sức, phải đốt tuổi thọ với Ấn, phải hy sinh đồ…

```text
Wide 16:9 landscape cinematic frame. a row of broken nichirin blades planted in the ground like memorials at sunset. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Đây cũng là điểm khác với Nen hay Chú lực mà mình đã giải thích. Hơi thở không có hệ thống giao ước rõ ràng,…

```text
Wide 16:9 landscape cinematic frame. a glowing hexagon, a dark dome, and a pair of lungs side by side, each with a price tag. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Và cây phả hệ cho thấy một thông điệp đẹp: không ai cần là Yoriichi. Mỗi người tìm ra hơi thở hợp với mình, v…

```text
Wide 16:9 landscape cinematic frame. many swordsman silhouettes of different styles standing together facing the dawn. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Tóm tắt

Lời: Tóm lại: mọi hơi thở đều bắt nguồn từ Hơi thở Mặt Trời. Năm nhánh chính là Nước, Lửa, Sấm, Gió, Đá, rồi từ đó…

```text
Wide 16:9 landscape cinematic frame. a completed glowing family tree with the sun at the root and many colored branches. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Hơi thở Mặt Trăng là nhánh bóng tối, còn Hơi thở Mặt Trời được giữ lại qua điệu múa của một gia đình.

```text
Wide 16:9 landscape cinematic frame. a sun and a crescent moon on opposite sides of the tree, a small torch at its base. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Và ở giới hạn cuối cùng là Ấn, Thế giới trong suốt và kiếm đỏ, những sức mạnh luôn đi kèm cái giá.

```text
Wide 16:9 landscape cinematic frame. three glowing symbols fading into a sunrise over the mountains. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được chọn một kiểu hơi thở, bạn chọn kiểu nào, hay bạn sẽ tự tạo một nhánh mới? Viết xuố…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a paintbrush next to an empty branch on the family tree. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã trái ác quỷ trong One Piece: ba loại, thức tỉn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a strange swirled fruit glowing on a pedestal. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye in a moonlit dojo. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hơi thở là gì?

Khoảng 131 giây · cảnh s01–s13 · 1703 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Kimetsu no Yaiba đến hết bộ truyện, gồm cả arc Vô Hạn Thành. Nếu bạn chỉ xem anime, hãy cân nhắc trước khi xem tiếp nhé.

<short pause> Trong Kimetsu no Yaiba, con người nhỏ bé chống lại những con quỷ bất tử. Vũ khí của họ không chỉ là thanh kiếm, mà là hơi thở.

<short pause> Nước, lửa, sấm, gió, đá, hoa, côn trùng, âm thanh, tình yêu... Có rất nhiều kiểu hơi thở. <short pause> Nhưng chúng không xuất hiện ngẫu nhiên.

<short pause> Tất cả đều bắt nguồn từ một hơi thở duy nhất, và có thể vẽ thành một cây phả hệ giống như cây gia phả của một dòng họ.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ vẽ cây phả hệ hơi thở: gốc rễ ở đâu, các nhánh tách ra thế nào, và cái giá của sức mạnh vượt giới hạn.

<short pause> Xem hết video, bạn sẽ biết vì sao gần như tất cả các kiểu hơi thở đều là phiên bản đơn giản hóa của một kỹ thuật mà không ai học được trọn vẹn.

<short pause> Trước hết, hơi thở trong truyện là gì? Đó là kỹ thuật thở đặc biệt giúp đưa thật nhiều oxy vào máu, tăng sức mạnh và tốc độ vượt xa người thường.

<short pause> Nhờ hơi thở, một con người có thể chạy nhanh, chém mạnh và chịu đựng vết thương đủ để đối đầu với quỷ, loài có sức mạnh và khả năng hồi phục phi thường.

<short pause> Cấp độ cao hơn là duy trì hơi thở toàn tập liên tục, kể cả khi ngủ. Người làm được điều này có sức bền tăng vượt trội.

<short pause> Luyện hơi thở cực khổ. Học viên phải chạy núi, chịu đựng, tập thở đến mức phổi như muốn nổ tung, trong nhiều tháng liền.

<short pause> Mỗi kiểu hơi thở đi kèm một bộ thế kiếm, thường gọi là thức. Mỗi thức là một cách tận dụng hơi thở theo phong cách của nguyên tố đó.

<short pause> Và thanh kiếm Nhật Luân của mỗi kiếm sĩ đổi màu theo người cầm. Màu kiếm gợi ý kiểu hơi thở phù hợp với họ.

<short pause> Kaku ghi chú: hơi thở giống như phong cách võ thuật. Cùng một nền tảng thể lực, nhưng mỗi môn phái có cách ra đòn riêng.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Kimetsu no Yaiba đến hết bộ truyện, gồm cả arc Vô Hạn Thành. Nếu bạn chỉ xem anime, hãy cân nhắc trước khi xem tiếp nhé.

[pause] Trong Kimetsu no Yaiba, con người nhỏ bé chống lại những con quỷ bất tử. Vũ khí của họ không chỉ là thanh kiếm, mà là hơi thở.

[pause] Nước, lửa, sấm, gió, đá, hoa, côn trùng, âm thanh, tình yêu... Có rất nhiều kiểu hơi thở. [pause] Nhưng chúng không xuất hiện ngẫu nhiên.

[pause] Tất cả đều bắt nguồn từ một hơi thở duy nhất, và có thể vẽ thành một cây phả hệ giống như cây gia phả của một dòng họ.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ vẽ cây phả hệ hơi thở: gốc rễ ở đâu, các nhánh tách ra thế nào, và cái giá của sức mạnh vượt giới hạn.

[pause] Xem hết video, bạn sẽ biết vì sao gần như tất cả các kiểu hơi thở đều là phiên bản đơn giản hóa của một kỹ thuật mà không ai học được trọn vẹn.

[pause] [curious] Trước hết, hơi thở trong truyện là gì? Đó là kỹ thuật thở đặc biệt giúp đưa thật nhiều oxy vào máu, tăng sức mạnh và tốc độ vượt xa người thường.

[pause] Nhờ hơi thở, một con người có thể chạy nhanh, chém mạnh và chịu đựng vết thương đủ để đối đầu với quỷ, loài có sức mạnh và khả năng hồi phục phi thường.

[pause] Cấp độ cao hơn là duy trì hơi thở toàn tập liên tục, kể cả khi ngủ. Người làm được điều này có sức bền tăng vượt trội.

[pause] Luyện hơi thở cực khổ. Học viên phải chạy núi, chịu đựng, tập thở đến mức phổi như muốn nổ tung, trong nhiều tháng liền.

[pause] Mỗi kiểu hơi thở đi kèm một bộ thế kiếm, thường gọi là thức. Mỗi thức là một cách tận dụng hơi thở theo phong cách của nguyên tố đó.

[pause] Và thanh kiếm Nhật Luân của mỗi kiếm sĩ đổi màu theo người cầm. Màu kiếm gợi ý kiểu hơi thở phù hợp với họ.

[pause] Kaku ghi chú: hơi thở giống như phong cách võ thuật. Cùng một nền tảng thể lực, nhưng mỗi môn phái có cách ra đòn riêng.
```

### c02 · Đối thủ: vì sao phải có hơi thở? / Con đường trở thành kiếm sĩ

Khoảng 149 giây · cảnh s14–s28 · 1934 ký tự

**Gemini**

```text
Để thấy hơi thở quan trọng thế nào, cần hiểu đối thủ. Quỷ trong truyện khỏe hơn người rất nhiều, và gần như không thể bị giết bằng cách thông thường.

<short pause> Quỷ hồi phục vết thương gần như ngay lập tức. Chặt tay thì tay mọc lại, đâm xuyên thì vết thương liền. Chúng chỉ có hai điểm yếu lớn.

<short pause> Điểm yếu thứ nhất là ánh mặt trời. Quỷ tan biến khi bị ánh nắng chiếu trực tiếp. Vì vậy chúng chỉ hoạt động vào ban đêm.

<short pause> Điểm yếu thứ hai là bị chém đứt đầu bằng kiếm Nhật Luân, loại kiếm rèn từ quặng hấp thụ ánh mặt trời.

<short pause> Nhưng cổ của quỷ mạnh cứng như thép. Không có hơi thở, con người không đủ sức và tốc độ để chém đứt nó.

<short pause> Nhiều con quỷ còn có Huyết quỷ thuật, năng lực đặc biệt riêng như điều khiển chỉ, tạo ảo ảnh, hay thao túng không gian. Cuộc chiến vì thế càng không cân sức.

<short pause> Hơi thở chính là cây cầu giúp con người vượt qua khoảng cách đó: đủ nhanh để né, đủ mạnh để chém, đủ bền để trụ tới bình minh.

<short pause> Để học được hơi thở, một người bình thường phải đi qua con đường rất dài. Truyện cho ta thấy khá rõ con đường đó qua hành trình của Tanjiro.

<short pause> Bước đầu là tìm một người thầy. Thường đó là một kiếm sĩ đã giải nghệ, sống ẩn trong núi và chỉ nhận vài học trò.

<short pause> Việc luyện tập kéo dài nhiều tháng tới nhiều năm: chạy núi trong không khí loãng, né bẫy, tập chém, tập thở cho tới khi cơ thể quen.

<short pause> Có những bài kiểm tra tưởng như không thể, như chém đôi một tảng đá khổng lồ. Chỉ khi vượt qua, người thầy mới cho phép học trò đi tiếp.

<short pause> Bước tiếp theo là Kỳ tuyển chọn cuối cùng: sống sót bảy ngày trên một ngọn núi đầy quỷ, được bao quanh bởi hoa tử đằng mà quỷ sợ.

<short pause> Chỉ ai sống sót mới được vào Sát Quỷ Đoàn, nhận kiếm Nhật Luân và một con quạ đưa tin. Nhiều người không bao giờ trở về từ ngọn núi đó.

<short pause> Và vào đoàn mới chỉ là khởi đầu. Kiếm sĩ phải tiếp tục luyện, từ cấp thấp nhất, trải qua hàng loạt trận chiến để leo lên.

<short pause> <laugh> Kaku nhận xét: đây là lý do người xem trân trọng mỗi lần một nhân vật mạnh lên. Mọi bước tiến đều được xây bằng mồ hôi, không phải may mắn.
```

**ElevenLabs**

```text
Để thấy hơi thở quan trọng thế nào, cần hiểu đối thủ. Quỷ trong truyện khỏe hơn người rất nhiều, và gần như không thể bị giết bằng cách thông thường.

[pause] Quỷ hồi phục vết thương gần như ngay lập tức. Chặt tay thì tay mọc lại, đâm xuyên thì vết thương liền. Chúng chỉ có hai điểm yếu lớn.

[pause] Điểm yếu thứ nhất là ánh mặt trời. Quỷ tan biến khi bị ánh nắng chiếu trực tiếp. Vì vậy chúng chỉ hoạt động vào ban đêm.

[pause] Điểm yếu thứ hai là bị chém đứt đầu bằng kiếm Nhật Luân, loại kiếm rèn từ quặng hấp thụ ánh mặt trời.

[pause] Nhưng cổ của quỷ mạnh cứng như thép. Không có hơi thở, con người không đủ sức và tốc độ để chém đứt nó.

[pause] Nhiều con quỷ còn có Huyết quỷ thuật, năng lực đặc biệt riêng như điều khiển chỉ, tạo ảo ảnh, hay thao túng không gian. Cuộc chiến vì thế càng không cân sức.

[pause] Hơi thở chính là cây cầu giúp con người vượt qua khoảng cách đó: đủ nhanh để né, đủ mạnh để chém, đủ bền để trụ tới bình minh.

[pause] Để học được hơi thở, một người bình thường phải đi qua con đường rất dài. Truyện cho ta thấy khá rõ con đường đó qua hành trình của Tanjiro.

[pause] Bước đầu là tìm một người thầy. Thường đó là một kiếm sĩ đã giải nghệ, sống ẩn trong núi và chỉ nhận vài học trò.

[pause] Việc luyện tập kéo dài nhiều tháng tới nhiều năm: chạy núi trong không khí loãng, né bẫy, tập chém, tập thở cho tới khi cơ thể quen.

[pause] Có những bài kiểm tra tưởng như không thể, như chém đôi một tảng đá khổng lồ. Chỉ khi vượt qua, người thầy mới cho phép học trò đi tiếp.

[pause] Bước tiếp theo là Kỳ tuyển chọn cuối cùng: sống sót bảy ngày trên một ngọn núi đầy quỷ, được bao quanh bởi hoa tử đằng mà quỷ sợ.

[pause] Chỉ ai sống sót mới được vào Sát Quỷ Đoàn, nhận kiếm Nhật Luân và một con quạ đưa tin. Nhiều người không bao giờ trở về từ ngọn núi đó.

[pause] Và vào đoàn mới chỉ là khởi đầu. Kiếm sĩ phải tiếp tục luyện, từ cấp thấp nhất, trải qua hàng loạt trận chiến để leo lên.

[pause] [chuckles] Kaku nhận xét: đây là lý do người xem trân trọng mỗi lần một nhân vật mạnh lên. Mọi bước tiến đều được xây bằng mồ hôi, không phải may mắn.
```

### c03 · Gốc rễ: Hơi thở Mặt Trời / 5 nhánh chính

Khoảng 110 giây · cảnh s29–s40 · 1434 ký tự

**Gemini**

```text
Ở gốc cây phả hệ là Hơi thở Mặt Trời, hơi thở đầu tiên. Nó được tạo ra bởi một kiếm sĩ huyền thoại từ nhiều thế kỷ trước: Tsugikuni Yoriichi.

<short pause> Yoriichi được miêu tả là người mạnh nhất trong lịch sử diệt quỷ. Ông sinh ra đã có những khả năng mà người khác phải cả đời mới chạm tới.

<short pause> Ông dạy kỹ thuật thở cho những kiếm sĩ khác. <short pause> Nhưng không ai học được Hơi thở Mặt Trời trọn vẹn như ông.

<short pause> Vì thế, mỗi người học lấy phần mà họ làm được, rồi kết hợp với phong cách riêng. Từ đó sinh ra năm hơi thở cơ bản.

<short pause> Đây là ý tưởng rất hay: tất cả những hơi thở ta biết đều là phiên bản rút gọn của một kỹ thuật hoàn hảo đã gần như thất truyền.

<short pause> Năm hơi thở cơ bản, nhánh lớn của cây, là: Nước, Lửa, Sấm, Gió và Đá. Mỗi nhánh có tính cách riêng.

<short pause> Hơi thở Nước mềm mại và linh hoạt. Thức kiếm như dòng chảy, thích nghi với mọi loại đối thủ. Đây là hơi thở dễ học và phổ biến nhất.

<short pause> Hơi thở Lửa mạnh mẽ, dồn lực tấn công trực diện. Nó hợp với người có ý chí rực cháy và dám xông thẳng vào đối thủ.

<short pause> Hơi thở Sấm tập trung vào tốc độ, dồn lực vào chân để lao đi như tia chớp. Có người chỉ học được đúng một thức, nhưng luyện nó tới mức hoàn hảo.

<short pause> Hơi thở Gió dữ dội, những nhát chém như lốc xoáy. Nó hợp với người hung hăng, liều lĩnh.

<short pause> Hơi thở Đá dựa vào sức mạnh thể chất khổng lồ và phòng thủ vững chắc. Người dùng mạnh nhất trong truyện được xem là thể lực số một.

<short pause> Mỗi nhánh này lại tiếp tục mọc ra những nhánh con khi các kiếm sĩ đời sau cải biên cho hợp với bản thân.
```

**ElevenLabs**

```text
Ở gốc cây phả hệ là Hơi thở Mặt Trời, hơi thở đầu tiên. Nó được tạo ra bởi một kiếm sĩ huyền thoại từ nhiều thế kỷ trước: Tsugikuni Yoriichi.

[pause] Yoriichi được miêu tả là người mạnh nhất trong lịch sử diệt quỷ. Ông sinh ra đã có những khả năng mà người khác phải cả đời mới chạm tới.

[pause] Ông dạy kỹ thuật thở cho những kiếm sĩ khác. [pause] Nhưng không ai học được Hơi thở Mặt Trời trọn vẹn như ông.

[pause] Vì thế, mỗi người học lấy phần mà họ làm được, rồi kết hợp với phong cách riêng. Từ đó sinh ra năm hơi thở cơ bản.

[pause] Đây là ý tưởng rất hay: tất cả những hơi thở ta biết đều là phiên bản rút gọn của một kỹ thuật hoàn hảo đã gần như thất truyền.

[pause] Năm hơi thở cơ bản, nhánh lớn của cây, là: Nước, Lửa, Sấm, Gió và Đá. Mỗi nhánh có tính cách riêng.

[pause] Hơi thở Nước mềm mại và linh hoạt. Thức kiếm như dòng chảy, thích nghi với mọi loại đối thủ. Đây là hơi thở dễ học và phổ biến nhất.

[pause] Hơi thở Lửa mạnh mẽ, dồn lực tấn công trực diện. Nó hợp với người có ý chí rực cháy và dám xông thẳng vào đối thủ.

[pause] Hơi thở Sấm tập trung vào tốc độ, dồn lực vào chân để lao đi như tia chớp. Có người chỉ học được đúng một thức, nhưng luyện nó tới mức hoàn hảo.

[pause] Hơi thở Gió dữ dội, những nhát chém như lốc xoáy. Nó hợp với người hung hăng, liều lĩnh.

[pause] Hơi thở Đá dựa vào sức mạnh thể chất khổng lồ và phòng thủ vững chắc. Người dùng mạnh nhất trong truyện được xem là thể lực số một.

[pause] Mỗi nhánh này lại tiếp tục mọc ra những nhánh con khi các kiếm sĩ đời sau cải biên cho hợp với bản thân.
```

### c04 · Các nhánh con / Trụ cột: những bậc thầy hơi thở

Khoảng 137 giây · cảnh s41–s55 · 1784 ký tự

**Gemini**

```text
Giờ đi xuống các nhánh con. Từ Nước sinh ra Hơi thở Hoa, mềm mại và đẹp, tập trung vào sự chính xác.

<short pause> Từ Hoa lại sinh ra Hơi thở Côn trùng, dành cho người không đủ sức để chém đứt đầu quỷ. Thay vào đó, họ dùng mũi kiếm tẩm độc.

<short pause> Đây là ví dụ đẹp về việc hệ thống thích nghi: người yếu về sức vẫn tìm ra cách đánh bại quỷ bằng trí tuệ và y học.

<short pause> Cũng từ Nước sinh ra Hơi thở Rắn, với những đường kiếm uốn lượn khó đoán như rắn trườn.

<short pause> Từ Lửa sinh ra Hơi thở Tình yêu, dùng một thanh kiếm mỏng dẻo như roi, kết hợp sự linh hoạt đặc biệt của cơ thể người dùng.

<short pause> Từ Sấm sinh ra Hơi thở Âm thanh, kết hợp tiếng nổ và nhịp điệu. Người dùng đọc nhịp chiến đấu như đọc một bản nhạc.

<short pause> Từ Gió sinh ra Hơi thở Sương mù, khó đoán, lúc ẩn lúc hiện, làm đối thủ không bắt được hướng tấn công.

<short pause> Và có một hơi thở tự học: Hơi thở Thú, do một người lớn lên trong núi tự sáng tạo, với lối đánh hoang dã bằng hai lưỡi kiếm răng cưa.

<short pause> <laugh> Kaku tóm lại: cây phả hệ cho thấy mỗi hơi thở mới ra đời để phù hợp với cơ thể và tính cách của một người. Không ai bắt chước hoàn toàn người đi trước.

<short pause> Những người thành thạo hơi thở nhất trong Sát Quỷ Đoàn được gọi là Trụ cột. Mỗi Trụ cột thường đại diện cho một kiểu hơi thở.

<short pause> Sát Quỷ Đoàn có hệ thống cấp bậc từ thấp tới cao. Trụ cột đứng ở đỉnh, ngay dưới người đứng đầu tổ chức.

<short pause> Theo truyện, để trở thành Trụ cột, kiếm sĩ phải tiêu diệt khoảng năm mươi con quỷ, hoặc hạ một trong Thập Nhị Quỷ Nguyệt.

<short pause> Mỗi Trụ cột có tính cách gắn với hơi thở của họ: người dùng Lửa nhiệt huyết, người dùng Nước điềm tĩnh, người dùng Gió nóng nảy.

<short pause> Điều này quay lại ý chính của video: hơi thở không chỉ là kỹ thuật, nó là con người. Người ta tìm ra hơi thở phản ánh chính mình.

<short pause> Kaku ghi chú: đây giống thuyết tính cách của Nen mà mình từng nhắc. Nhiều bộ truyện đều có chung ý: sức mạnh nói lên bạn là ai.
```

**ElevenLabs**

```text
Giờ đi xuống các nhánh con. Từ Nước sinh ra Hơi thở Hoa, mềm mại và đẹp, tập trung vào sự chính xác.

[pause] Từ Hoa lại sinh ra Hơi thở Côn trùng, dành cho người không đủ sức để chém đứt đầu quỷ. Thay vào đó, họ dùng mũi kiếm tẩm độc.

[pause] Đây là ví dụ đẹp về việc hệ thống thích nghi: người yếu về sức vẫn tìm ra cách đánh bại quỷ bằng trí tuệ và y học.

[pause] Cũng từ Nước sinh ra Hơi thở Rắn, với những đường kiếm uốn lượn khó đoán như rắn trườn.

[pause] Từ Lửa sinh ra Hơi thở Tình yêu, dùng một thanh kiếm mỏng dẻo như roi, kết hợp sự linh hoạt đặc biệt của cơ thể người dùng.

[pause] Từ Sấm sinh ra Hơi thở Âm thanh, kết hợp tiếng nổ và nhịp điệu. Người dùng đọc nhịp chiến đấu như đọc một bản nhạc.

[pause] Từ Gió sinh ra Hơi thở Sương mù, khó đoán, lúc ẩn lúc hiện, làm đối thủ không bắt được hướng tấn công.

[pause] Và có một hơi thở tự học: Hơi thở Thú, do một người lớn lên trong núi tự sáng tạo, với lối đánh hoang dã bằng hai lưỡi kiếm răng cưa.

[pause] [chuckles] Kaku tóm lại: cây phả hệ cho thấy mỗi hơi thở mới ra đời để phù hợp với cơ thể và tính cách của một người. Không ai bắt chước hoàn toàn người đi trước.

[pause] Những người thành thạo hơi thở nhất trong Sát Quỷ Đoàn được gọi là Trụ cột. Mỗi Trụ cột thường đại diện cho một kiểu hơi thở.

[pause] Sát Quỷ Đoàn có hệ thống cấp bậc từ thấp tới cao. Trụ cột đứng ở đỉnh, ngay dưới người đứng đầu tổ chức.

[pause] Theo truyện, để trở thành Trụ cột, kiếm sĩ phải tiêu diệt khoảng năm mươi con quỷ, hoặc hạ một trong Thập Nhị Quỷ Nguyệt.

[pause] Mỗi Trụ cột có tính cách gắn với hơi thở của họ: người dùng Lửa nhiệt huyết, người dùng Nước điềm tĩnh, người dùng Gió nóng nảy.

[pause] Điều này quay lại ý chính của video: hơi thở không chỉ là kỹ thuật, nó là con người. Người ta tìm ra hơi thở phản ánh chính mình.

[pause] Kaku ghi chú: đây giống thuyết tính cách của Nen mà mình từng nhắc. Nhiều bộ truyện đều có chung ý: sức mạnh nói lên bạn là ai.
```

### c05 · Nhánh bóng tối: Hơi thở Mặt Trăng / Hơi thở Mặt Trời không thất truyền

Khoảng 94 giây · cảnh s56–s65 · 1219 ký tự

**Gemini**

```text
Cây phả hệ này còn một nhánh mà ít ai nhắc tới vì nó thuộc về kẻ thù: Hơi thở Mặt Trăng.

<short pause> Nó được tạo ra bởi anh trai song sinh của Yoriichi. Người này không thể đạt tới Hơi thở Mặt Trời, nên tạo ra một phiên bản mang dấu ấn riêng.

<short pause> Vì khao khát sức mạnh và nỗi sợ cái chết, anh ta đã trở thành quỷ, và sau này là một trong những con quỷ mạnh nhất.

<short pause> Hơi thở Mặt Trăng tạo ra những nhát chém có vô số lưỡi trăng nhỏ đi kèm, rất khó đỡ vì chúng thay đổi kích thước và hướng.

<short pause> Đây là nhánh bi kịch nhất của cây phả hệ: cùng một gốc, nhưng một người trở thành huyền thoại, người kia trở thành con quỷ vì ghen tị.

<short pause> Nếu Hơi thở Mặt Trời không ai học được, sao nó vẫn còn tồn tại? Câu trả lời nằm ở một điệu múa.

<short pause> Gia đình Kamado truyền lại một điệu múa cầu thần qua nhiều thế hệ, múa suốt đêm vào mỗi dịp đầu năm, cùng đôi hoa tai hình mặt trời.

<short pause> Điệu múa đó thực chất chính là các thế của Hơi thở Mặt Trời, được giữ gìn dưới dạng nghi lễ, không ai biết đó là kỹ thuật chiến đấu.

<short pause> Tanjiro nhớ lại điệu múa của cha mình trong lúc sinh tử, và dần dần đánh thức lại kỹ thuật tưởng như đã mất.

<short pause> <laugh> Kaku rất thích chi tiết này: kỹ thuật mạnh nhất không được cất trong sách bí truyền, mà được giữ bởi một gia đình bình thường qua tình yêu và thói quen.
```

**ElevenLabs**

```text
Cây phả hệ này còn một nhánh mà ít ai nhắc tới vì nó thuộc về kẻ thù: Hơi thở Mặt Trăng.

[pause] Nó được tạo ra bởi anh trai song sinh của Yoriichi. Người này không thể đạt tới Hơi thở Mặt Trời, nên tạo ra một phiên bản mang dấu ấn riêng.

[pause] Vì khao khát sức mạnh và nỗi sợ cái chết, anh ta đã trở thành quỷ, và sau này là một trong những con quỷ mạnh nhất.

[pause] Hơi thở Mặt Trăng tạo ra những nhát chém có vô số lưỡi trăng nhỏ đi kèm, rất khó đỡ vì chúng thay đổi kích thước và hướng.

[pause] Đây là nhánh bi kịch nhất của cây phả hệ: cùng một gốc, nhưng một người trở thành huyền thoại, người kia trở thành con quỷ vì ghen tị.

[pause] [curious] Nếu Hơi thở Mặt Trời không ai học được, sao nó vẫn còn tồn tại? Câu trả lời nằm ở một điệu múa.

[pause] Gia đình Kamado truyền lại một điệu múa cầu thần qua nhiều thế hệ, múa suốt đêm vào mỗi dịp đầu năm, cùng đôi hoa tai hình mặt trời.

[pause] Điệu múa đó thực chất chính là các thế của Hơi thở Mặt Trời, được giữ gìn dưới dạng nghi lễ, không ai biết đó là kỹ thuật chiến đấu.

[pause] Tanjiro nhớ lại điệu múa của cha mình trong lúc sinh tử, và dần dần đánh thức lại kỹ thuật tưởng như đã mất.

[pause] [chuckles] Kaku rất thích chi tiết này: kỹ thuật mạnh nhất không được cất trong sách bí truyền, mà được giữ bởi một gia đình bình thường qua tình yêu và thói quen.
```

### c06 · Vượt giới hạn: Ấn, Thế giới trong suốt và kiếm đỏ / Trắc nghiệm: bạn hợp với hơi thở nào?

Khoảng 118 giây · cảnh s66–s78 · 1532 ký tự

**Gemini**

```text
Ở cuối truyện, các kiếm sĩ mạnh nhất phải vượt qua giới hạn con người để đối đầu với những con quỷ hùng mạnh. Có ba dạng vượt giới hạn.

<short pause> Thứ nhất là Ấn, một hình vẽ xuất hiện trên cơ thể khi kiếm sĩ đạt trạng thái đặc biệt. Người có Ấn tăng sức mạnh vượt trội.

<short pause> Truyện cho biết Ấn xuất hiện khi thân nhiệt vượt khoảng ba mươi chín độ và nhịp tim vượt khoảng hai trăm lần mỗi phút.

<short pause> Nhưng Ấn có cái giá khủng khiếp: theo truyện, người có Ấn sẽ không sống quá hai mươi lăm tuổi. Chỉ duy nhất Yoriichi là ngoại lệ.

<short pause> Thứ hai là Thế giới trong suốt, khả năng nhìn xuyên cơ thể đối thủ, thấy cơ bắp, xương và dòng máu. Nhờ đó đọc được mọi chuyển động.

<short pause> Thứ ba là kiếm đỏ, khi kiếm sĩ nắm chặt thanh kiếm với sức mạnh cực lớn, lưỡi kiếm chuyển đỏ và gây vết thương khiến quỷ khó hồi phục.

<short pause> Cả ba đều từng là khả năng tự nhiên của Yoriichi. Những người đời sau chỉ đạt được chúng bằng cách đẩy cơ thể tới giới hạn và chấp nhận trả giá.

<short pause> Giờ chơi một trò nhỏ. Dựa trên cách truyện gắn tính cách với hơi thở, hãy xem bạn hợp với nhánh nào nhất. Đây chỉ là trò vui thôi nhé.

<short pause> Nếu bạn điềm tĩnh, dễ thích nghi, biết lắng nghe, có thể bạn hợp với Hơi thở Nước.

<short pause> Nếu bạn nhiệt huyết, thích dẫn đầu, luôn tràn năng lượng, Hơi thở Lửa có lẽ là của bạn.

<short pause> Nếu bạn sợ hãi nhiều thứ nhưng dồn hết vào một điều mình làm tốt nhất, Hơi thở Sấm là lựa chọn hay.

<short pause> Nếu bạn khéo léo, tinh tế, dùng trí tuệ thay vì sức mạnh, Hơi thở Côn trùng hoặc Hoa có thể hợp với bạn.

<short pause> Nếu bạn thích tự mình mày mò, không theo khuôn phép nào, có khi bạn sẽ tự tạo ra một nhánh mới như Hơi thở Thú.
```

**ElevenLabs**

```text
Ở cuối truyện, các kiếm sĩ mạnh nhất phải vượt qua giới hạn con người để đối đầu với những con quỷ hùng mạnh. Có ba dạng vượt giới hạn.

[pause] Thứ nhất là Ấn, một hình vẽ xuất hiện trên cơ thể khi kiếm sĩ đạt trạng thái đặc biệt. Người có Ấn tăng sức mạnh vượt trội.

[pause] Truyện cho biết Ấn xuất hiện khi thân nhiệt vượt khoảng ba mươi chín độ và nhịp tim vượt khoảng hai trăm lần mỗi phút.

[pause] Nhưng Ấn có cái giá khủng khiếp: theo truyện, người có Ấn sẽ không sống quá hai mươi lăm tuổi. Chỉ duy nhất Yoriichi là ngoại lệ.

[pause] Thứ hai là Thế giới trong suốt, khả năng nhìn xuyên cơ thể đối thủ, thấy cơ bắp, xương và dòng máu. Nhờ đó đọc được mọi chuyển động.

[pause] Thứ ba là kiếm đỏ, khi kiếm sĩ nắm chặt thanh kiếm với sức mạnh cực lớn, lưỡi kiếm chuyển đỏ và gây vết thương khiến quỷ khó hồi phục.

[pause] Cả ba đều từng là khả năng tự nhiên của Yoriichi. Những người đời sau chỉ đạt được chúng bằng cách đẩy cơ thể tới giới hạn và chấp nhận trả giá.

[pause] Giờ chơi một trò nhỏ. Dựa trên cách truyện gắn tính cách với hơi thở, hãy xem bạn hợp với nhánh nào nhất. Đây chỉ là trò vui thôi nhé.

[pause] Nếu bạn điềm tĩnh, dễ thích nghi, biết lắng nghe, có thể bạn hợp với Hơi thở Nước.

[pause] Nếu bạn nhiệt huyết, thích dẫn đầu, luôn tràn năng lượng, Hơi thở Lửa có lẽ là của bạn.

[pause] Nếu bạn sợ hãi nhiều thứ nhưng dồn hết vào một điều mình làm tốt nhất, Hơi thở Sấm là lựa chọn hay.

[pause] Nếu bạn khéo léo, tinh tế, dùng trí tuệ thay vì sức mạnh, Hơi thở Côn trùng hoặc Hoa có thể hợp với bạn.

[pause] Nếu bạn thích tự mình mày mò, không theo khuôn phép nào, có khi bạn sẽ tự tạo ra một nhánh mới như Hơi thở Thú.
```

### c07 · Những hiểu lầm về hơi thở / Góc nhìn của Kaku: sức mạnh có giá / Tóm tắt

Khoảng 144 giây · cảnh s79–s94 · 1869 ký tự

**Gemini**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về hệ thống hơi thở.

<short pause> Hiểu lầm một: hơi thở là phép thuật tạo ra nước hay lửa thật. Không phải. Nước, lửa hay sấm chỉ là cách truyện vẽ ra phong cách đòn đánh, không phải nguyên tố thật.

<short pause> Hiểu lầm hai: màu kiếm quyết định hơi thở. Màu kiếm chỉ gợi ý thiên hướng, người dùng vẫn có thể học hơi thở khác.

<short pause> Hiểu lầm ba: nhánh con yếu hơn nhánh chính. Thực tế nhiều Trụ cột dùng nhánh con và vẫn thuộc hàng mạnh nhất.

<short pause> Hiểu lầm bốn: có Ấn là chắc chắn thắng. Ấn giúp mạnh hơn, nhưng trong những trận cuối, cả những người có Ấn vẫn phải trả giá rất đắt.

<short pause> Điều khiến mình ấn tượng nhất với hệ thống hơi thở là nó luôn nhắc rằng con người có giới hạn.

<short pause> Quỷ bất tử, hồi phục gần như tức thì. Con người thì mỏi mệt, bị thương, và có tuổi thọ. Hơi thở là cách con người thu hẹp khoảng cách đó.

<short pause> Nhưng thu hẹp khoảng cách luôn có giá: phải luyện tập đến kiệt sức, phải đốt tuổi thọ với Ấn, phải hy sinh đồng đội.

<short pause> Đây cũng là điểm khác với Nen hay Chú lực mà mình đã giải thích. Hơi thở không có hệ thống giao ước rõ ràng, nhưng cái giá được trả bằng chính cơ thể.

<short pause> Và cây phả hệ cho thấy một thông điệp đẹp: không ai cần là Yoriichi. Mỗi người tìm ra hơi thở hợp với mình, và cùng nhau họ có thể làm được điều một người không làm được.

<short pause> Tóm lại: mọi hơi thở đều bắt nguồn từ Hơi thở Mặt Trời. Năm nhánh chính là Nước, Lửa, Sấm, Gió, Đá, rồi từ đó mọc ra các nhánh con.

<short pause> Hơi thở Mặt Trăng là nhánh bóng tối, còn Hơi thở Mặt Trời được giữ lại qua điệu múa của một gia đình.

<short pause> Và ở giới hạn cuối cùng là Ấn, Thế giới trong suốt và kiếm đỏ, những sức mạnh luôn đi kèm cái giá.

<short pause> Câu hỏi cho bạn: nếu được chọn một kiểu hơi thở, bạn chọn kiểu nào, hay bạn sẽ tự tạo một nhánh mới? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã trái ác quỷ trong One Piece: ba loại, thức tỉnh và điểm yếu.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm hay gặp về hệ thống hơi thở.

[pause] Hiểu lầm một: hơi thở là phép thuật tạo ra nước hay lửa thật. Không phải. Nước, lửa hay sấm chỉ là cách truyện vẽ ra phong cách đòn đánh, không phải nguyên tố thật.

[pause] Hiểu lầm hai: màu kiếm quyết định hơi thở. Màu kiếm chỉ gợi ý thiên hướng, người dùng vẫn có thể học hơi thở khác.

[pause] Hiểu lầm ba: nhánh con yếu hơn nhánh chính. Thực tế nhiều Trụ cột dùng nhánh con và vẫn thuộc hàng mạnh nhất.

[pause] Hiểu lầm bốn: có Ấn là chắc chắn thắng. Ấn giúp mạnh hơn, nhưng trong những trận cuối, cả những người có Ấn vẫn phải trả giá rất đắt.

[pause] Điều khiến mình ấn tượng nhất với hệ thống hơi thở là nó luôn nhắc rằng con người có giới hạn.

[pause] Quỷ bất tử, hồi phục gần như tức thì. Con người thì mỏi mệt, bị thương, và có tuổi thọ. Hơi thở là cách con người thu hẹp khoảng cách đó.

[pause] Nhưng thu hẹp khoảng cách luôn có giá: phải luyện tập đến kiệt sức, phải đốt tuổi thọ với Ấn, phải hy sinh đồng đội.

[pause] Đây cũng là điểm khác với Nen hay Chú lực mà mình đã giải thích. Hơi thở không có hệ thống giao ước rõ ràng, nhưng cái giá được trả bằng chính cơ thể.

[pause] Và cây phả hệ cho thấy một thông điệp đẹp: không ai cần là Yoriichi. Mỗi người tìm ra hơi thở hợp với mình, và cùng nhau họ có thể làm được điều một người không làm được.

[pause] Tóm lại: mọi hơi thở đều bắt nguồn từ Hơi thở Mặt Trời. Năm nhánh chính là Nước, Lửa, Sấm, Gió, Đá, rồi từ đó mọc ra các nhánh con.

[pause] Hơi thở Mặt Trăng là nhánh bóng tối, còn Hơi thở Mặt Trời được giữ lại qua điệu múa của một gia đình.

[pause] Và ở giới hạn cuối cùng là Ấn, Thế giới trong suốt và kiếm đỏ, những sức mạnh luôn đi kèm cái giá.

[pause] [curious] Câu hỏi cho bạn: nếu được chọn một kiểu hơi thở, bạn chọn kiểu nào, hay bạn sẽ tự tạo một nhánh mới? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã trái ác quỷ trong One Piece: ba loại, thức tỉnh và điểm yếu.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
