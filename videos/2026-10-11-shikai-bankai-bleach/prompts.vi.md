# Bộ prompt · Bleach: Từ thanh kiếm không tên đến Bankai — bậc thang tiến hóa của trảm phách đao

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

Lời: Cảnh báo: video có spoiler Bleach tới hết anime Huyết chiến ngàn năm, kể cả phần cuối vừa phát xong năm 2026.…

```text
Wide 16:9 landscape cinematic frame. a lone katana stuck in the ground on a hill under a pale moon, wind blowing through tall grass. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một thanh kiếm Nhật bình thường. Không phát sáng, không có hoa văn đặc biệt. Nhưng nếu bạn gọi đúng tên nó, n…

```text
Wide 16:9 landscape cinematic frame. an ordinary katana resting on a wooden stand in a dark room, a faint breath of wind stirring dust around it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trong Bleach, mỗi thanh kiếm của tử thần có một linh hồn riêng. Và sức mạnh của người cầm kiếm tăng theo mức…

```text
Wide 16:9 landscape cinematic frame. a warrior kneeling before a translucent spirit that rises from a sword, the two facing each other in silence. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku vẽ một bậc thang sáu nấc, từ thanh kiếm không tên cho tới Bankai. Mỗ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a staircase with six steps in its notebook, each step with three small icons. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Bộ anime Huyết chiến ngàn năm vừa khép lại vào tháng 10 năm 2026, sau gần bốn năm. Đây là lúc tốt nhất để nhì…

```text
Wide 16:9 landscape cinematic frame. a final film reel being placed into a box beside a sheathed katana, soft evening light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Tử thần và thanh kiếm

Lời: Trước khi leo thang, cần biết tử thần là ai. Trong Bleach, tử thần là những linh hồn chiến binh, dẫn dắt linh…

```text
Wide 16:9 landscape cinematic frame. a black-robed warrior standing on a rooftop at night, watching over a quiet city. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Vũ khí của họ là trảm phách đao, thanh kiếm có thể chém cả linh hồn. Nó không phải đồ rèn sẵn để phát cho ai…

```text
Wide 16:9 landscape cinematic frame. a row of swords on a rack, each casting a different shaped shadow on the wall behind it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Vì vậy không có hai thanh trảm phách đao nào giống nhau. Có thanh mang lửa, có thanh mang băng, có thanh biến…

```text
Wide 16:9 landscape cinematic frame. a fan of glowing blade silhouettes: one wreathed in fire, one in ice, one dissolving into petals, one casting a beast shadow. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Bleach là manga của Kubo Tite, đăng từ năm 2001 tới 2016. Phần cuối của truyện được chuyển thể thành bộ anime…

```text
Wide 16:9 landscape cinematic frame. a long bookshelf of manga volumes ending in a dramatic final volume glowing faintly. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Bleach nổi tiếng với cách đặt tên và câu gọi kiếm rất đẹp. Mỗi lần giải phóng là một câu thơ ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot practicing a dramatic pose with a tiny wooden sword. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Nấc 0: Thanh kiếm không tên

Lời: Nấc đầu tiên của bậc thang thật ra là con số không. Phần cuối truyện tiết lộ rằng mọi tử thần đều bắt đầu với…

```text
Wide 16:9 landscape cinematic frame. a row of identical plain nameless swords in a training academy armory. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Điều kiện: vào học viện đào tạo tử thần và nhận kiếm. Thanh kiếm lúc này không có linh hồn riêng, giống như m…

```text
Wide 16:9 landscape cinematic frame. a young trainee receiving a plain sword from an instructor in a stone courtyard. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Sức mạnh: chỉ là một thanh kiếm chém được linh hồn. Người cầm dùng nó bằng kiếm thuật thuần túy.

```text
Wide 16:9 landscape cinematic frame. a trainee practicing basic sword forms at dawn, the plain blade reflecting light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Cái giá: chưa có. Nhưng khi chủ nhân chiến đấu, rèn luyện và sống cùng thanh kiếm, linh hồn của họ dần in dấu…

```text
Wide 16:9 landscape cinematic frame. a faint glow slowly spreading from a trainee's hands into the blade over many seasons. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Điều đó cũng giải thích vì sao thanh kiếm của một người không thể đem cho người khác dùng như của mình. Nó đã…

```text
Wide 16:9 landscape cinematic frame. two warriors trying to swap swords, the blades flickering and refusing to respond in the wrong hands. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là chi tiết rất đẹp. Thanh kiếm không có sẵn tính cách. Nó lớn lên cùng bạn.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pressing its wing print onto a blank sword like a stamp. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Nấc 1: Trạng thái niêm phong

Lời: Nấc một là trạng thái mà ta thấy thường xuyên nhất: thanh kiếm đã có linh hồn riêng, nhưng đang ngủ, trông nh…

```text
Wide 16:9 landscape cinematic frame. a sheathed katana with a unique guard design resting on a warrior's hip. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Điều kiện: thanh kiếm đã mang linh hồn của chủ nhân. Mỗi thanh có một chuôi, một đốc kiếm khác nhau, như dấu…

```text
Wide 16:9 landscape cinematic frame. close-up of several different sword guards: a square one, a flower-shaped one, a star-shaped one. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Sức mạnh: vẫn chỉ là kiếm thuật cộng với sức mạnh tâm linh của người dùng. Nhưng với những người rất mạnh, ch…

```text
Wide 16:9 landscape cinematic frame. a warrior slicing a boulder cleanly in half with a single unreleased stroke. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Cái giá: không có gì, ngoài việc bạn chưa khai thác được sức mạnh thật của nó. Nhiều tử thần cả đời chỉ ở nấc…

```text
Wide 16:9 landscape cinematic frame. a crowd of ordinary black-robed warriors walking in formation, swords still sealed. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Thú vị là có vài nhân vật giữ kiếm ở trạng thái giải phóng suốt, vì sức mạnh tâm linh quá lớn khiến thanh kiế…

```text
Wide 16:9 landscape cinematic frame. an oversized cleaver-like blade with no guard, wrapped in cloth, strapped to a young warrior's back. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Nấc 2: Biết tên thanh kiếm

Lời: Nấc hai là bước ngoặt đầu tiên: nghe được tên của thanh kiếm. Không phải tự đặt tên, mà là nghe linh hồn tron…

```text
Wide 16:9 landscape cinematic frame. a warrior meditating with a sword across their knees, a faint whisper visualized as glowing characters in the air. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Điều kiện: đối thoại với linh hồn trong kiếm, thường qua thiền định, hoặc trong những khoảnh khắc sinh tử. Li…

```text
Wide 16:9 landscape cinematic frame. a surreal inner world: a skyscraper city tilted sideways, a cloaked figure standing on a building's side. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Thế giới nội tâm này phản chiếu tâm trạng của người đó. Khi họ buồn, trong đó có thể đổ mưa. Khi họ quyết tâm…

```text
Wide 16:9 landscape cinematic frame. a sideways city under heavy rain, then the same city under a clear sky, split down the middle. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Sức mạnh: chưa tăng ngay, nhưng đây là chìa khóa để mở nấc tiếp theo. Cái giá: không phải ai cũng nghe được.…

```text
Wide 16:9 landscape cinematic frame. a warrior straining to listen in silence, years passing as seasons change behind them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: để mạnh hơn, trước tiên phải biết lắng nghe. Kaku thấy câu này đúng cả với việc học hành.

```text
Wide 16:9 landscape cinematic frame. the owl mascot cupping a wing to its ear, listening to a tiny book. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Nấc 3: Shikai

Lời: Nấc ba là Shikai, lần giải phóng đầu tiên. Người dùng hô một câu lệnh, rồi gọi tên thanh kiếm. Thanh kiếm biế…

```text
Wide 16:9 landscape cinematic frame. a katana transforming mid-swing, its blade reshaping as a burst of spiritual energy erupts. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Điều kiện: biết tên kiếm và có đủ sức mạnh tâm linh. Câu lệnh thường là một động từ ngắn, như rơi xuống, gầm…

```text
Wide 16:9 landscape cinematic frame. a warrior raising a sword as calligraphy characters of a command swirl around the blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Sức mạnh: rất đa dạng. Có thanh kiếm tan thành hàng nghìn lưỡi dao nhỏ như cánh hoa anh đào. Có thanh biến th…

```text
Wide 16:9 landscape cinematic frame. three panels: a blade dissolving into cherry blossom-like shards, an ice dragon coiling, a segmented whip-sword. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Cái giá: tiêu hao sức mạnh tâm linh, và tiết lộ năng lực cho đối thủ. Trong Bleach, biết năng lực của kiếm đố…

```text
Wide 16:9 landscape cinematic frame. an opponent smirking as they study the shape of a newly released blade. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Hầu hết các đội phó và nhiều tử thần mạnh đều đạt tới Shikai. Đây là nấc phân biệt người lính thường với một…

```text
Wide 16:9 landscape cinematic frame. a line of officers with released swords of many shapes standing behind their commanders. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: có một điều kỳ lạ là có những nhân vật rất mạnh mà mãi tới phần cuối truyện mới biết tên thanh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot scratching its head at a sword that refuses to say its name. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Những câu lệnh giải phóng đẹp nhất

Lời: Trước khi nói về cái giá, Kaku muốn dừng lại ở thứ khiến Shikai trong Bleach đáng nhớ: những câu lệnh giải ph…

```text
Wide 16:9 landscape cinematic frame. calligraphy brush strokes floating in the air around a raised sword. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Mỗi câu lệnh là một động từ ngắn trong tiếng Nhật, và nó thường gợi tả đúng năng lực của thanh kiếm.

```text
Wide 16:9 landscape cinematic frame. a scroll with several short brushed verbs, each glowing with a different color. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Thanh kiếm tan thành cánh hoa được gọi bằng lệnh rơi rụng. Thanh kiếm hình rắn được gọi bằng lệnh gầm lên. Th…

```text
Wide 16:9 landscape cinematic frame. three sword silhouettes: one scattering petals, one roaring like a serpent, one surrounded by frost. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Có lệnh là nhảy múa, có lệnh là gầm gừ, có lệnh là vươn dài. Nghe tên câu lệnh, người xem gần như đoán được t…

```text
Wide 16:9 landscape cinematic frame. a small gallery of sword spirits each posing according to its verb: dancing, growling, stretching. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Đây là một cách xây dựng nhân vật rất tiết kiệm: chỉ một câu ngắn, mà nói lên cả một con người.

```text
Wide 16:9 landscape cinematic frame. a single brushstroke on paper that forms the silhouette of a warrior. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu bạn học tiếng Nhật, các câu lệnh này là cách học động từ vui nhất quả đất.

```text
Wide 16:9 landscape cinematic frame. the owl mascot with a tiny headband practicing brush calligraphy. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Nấc 4: Cụ hiện hóa

Lời: Giữa Shikai và Bankai có một nấc mà nhiều người quên: cụ hiện hóa, tức là kéo linh hồn thanh kiếm ra khỏi thế…

```text
Wide 16:9 landscape cinematic frame. a translucent spirit stepping out of a sword into the real world, standing face to face with its owner. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điều kiện: sức mạnh tâm linh và sự hòa hợp đủ lớn để linh hồn kiếm có hình dạng thật. Việc này thường mất rất…

```text
Wide 16:9 landscape cinematic frame. a warrior and a spirit meditating opposite each other across seasons, snow falling then melting. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Sức mạnh: chưa tăng, nhưng người dùng giờ có thể đối mặt trực tiếp với linh hồn kiếm. Và bước tiếp theo đòi h…

```text
Wide 16:9 landscape cinematic frame. a warrior drawing their sword against their own sword's spirit in an empty training ground. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Cái giá: thời gian và nguy hiểm. Linh hồn kiếm không phải lúc nào cũng thân thiện. Có linh hồn kiêu ngạo, có…

```text
Wide 16:9 landscape cinematic frame. a fierce beast-like spirit roaring at a warrior who stands firm, sword raised. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · Nấc 5: Bankai

Lời: Nấc cao nhất là Bankai, lần giải phóng cuối cùng. Để đạt được, người dùng phải cụ hiện hóa linh hồn kiếm, rồi…

```text
Wide 16:9 landscape cinematic frame. a warrior standing victorious over a kneeling sword spirit, both glowing with power. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Điều kiện: theo truyện, ngay cả người có tài năng cũng cần khoảng mười năm hoặc hơn để thành thạo Bankai. Đó…

```text
Wide 16:9 landscape cinematic frame. a calendar spiraling through ten years behind a warrior training under a waterfall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhân vật chính là ngoại lệ nổi tiếng: nhờ một phương pháp luyện đặc biệt và đặt cược cả mạng sống, cậu đạt Ba…

```text
Wide 16:9 landscape cinematic frame. a young warrior exhausted in a vast underground training cavern, a glowing figure fading beside him. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Sức mạnh: truyện nói Bankai mạnh hơn Shikai khoảng năm đến mười lần. Hình dạng thay đổi hoàn toàn, có khi thà…

```text
Wide 16:9 landscape cinematic frame. a colossal armored giant rising behind a warrior, sword raised in unison. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Có Bankai thì gần như đủ điều kiện làm đội trưởng. Trong mười ba đội của lực lượng tử thần, gần như tất cả độ…

```text
Wide 16:9 landscape cinematic frame. thirteen captain silhouettes in white coats standing in a grand hall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Mỗi Bankai cũng có tên riêng, thường dài hơn tên kiếm ở Shikai, như thể thanh kiếm được gọi bằng tên đầy đủ k…

```text
Wide 16:9 landscape cinematic frame. a long ceremonial name written vertically on a banner above a warrior with a transformed blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: không phải Bankai nào cũng to lớn. Bankai của nhân vật chính lại thu nhỏ thành một thanh kiếm đ…

```text
Wide 16:9 landscape cinematic frame. a slim black katana held low by a warrior in a long black coat, speed lines behind him. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Cái giá của Bankai

Lời: Bankai mạnh nhất, nhưng cũng là nấc có cái giá đáng sợ nhất. Và cái giá đó không chỉ là thể lực.

```text
Wide 16:9 landscape cinematic frame. a cracked sword lying on stone, a faint crack also glowing on the owner's hand. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Truyện nói Bankai bị gãy thì không bao giờ phục hồi hoàn toàn như cũ. Với nhiều người, mất Bankai giống như m…

```text
Wide 16:9 landscape cinematic frame. shards of a broken blade scattered on the ground, a warrior kneeling over them in the rain. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Có Bankai gắn chặt với cơ thể chủ nhân đến mức vết thương của Bankai truyền thẳng sang người dùng. Bankai càn…

```text
Wide 16:9 landscape cinematic frame. a giant armored figure wounded on its arm, and the small warrior behind it clutching the same arm. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và trong Huyết chiến ngàn năm, xuất hiện một mối đe dọa chưa từng có: kẻ thù có thể cướp Bankai, rồi dùng chí…

```text
Wide 16:9 landscape cinematic frame. a mysterious medallion glowing as a sword's power is pulled away from its horrified owner. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nhiều đội trưởng mất Bankai trong đợt tấn công đầu tiên. Đó là lúc cả lực lượng nhận ra nấc cao nhất cũng là…

```text
Wide 16:9 landscape cinematic frame. captains standing in a ruined courtyard, empty hilts in their hands, smoke rising. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là thiết kế rất thông minh. Kẻ địch mạnh nhất không cần mạnh hơn bạn. Chỉ cần lấy đi thứ bạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot clutching its notebook tightly while a shadowy hand reaches for it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Ba hiểu lầm về Bankai

Lời: Có ba hiểu lầm về Bankai mà Kaku hay thấy trong bình luận, gỡ nhanh trước khi tới bí mật lớn nhất.

```text
Wide 16:9 landscape cinematic frame. three sticky notes on a sword rack, each with a red question mark. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Hiểu lầm một: Bankai luôn mạnh hơn mọi Shikai. Không hẳn. Bankai của một người luôn mạnh hơn Shikai của chính…

```text
Wide 16:9 landscape cinematic frame. a small released blade defeating a much larger giant form, the giant toppling. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Hiểu lầm hai: ai có Bankai cũng muốn khoe. Thực ra có nhân vật cố tình giấu Bankai của mình, vì nếu lộ ra sẽ…

```text
Wide 16:9 landscape cinematic frame. a bald warrior hiding a glowing blade behind his back, grinning at his captain in the distance. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hiểu lầm ba: Bankai là giới hạn cuối cùng. Truyện cho thấy có những sức mạnh vượt cả Bankai. Nhưng một trong…

```text
Wide 16:9 landscape cinematic frame. a warrior engulfed in black flames, his sword dissolving into the fire as his power fades. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cả ba hiểu lầm cho thấy một điều: trong Bleach, sức mạnh không phải là một con số, mà là một lự…

```text
Wide 16:9 landscape cinematic frame. the owl mascot balancing a sword on one wing and a scale on the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Bí mật của thanh kiếm nhân vật chính

Lời: Bây giờ là spoiler lớn nhất video. Nếu chưa xem hết Huyết chiến ngàn năm, bạn có thể tua qua chương này.

```text
Wide 16:9 landscape cinematic frame. a warning sign on a closed door with a sword emblem. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Suốt nhiều năm, nhân vật chính tưởng linh hồn thanh kiếm của mình là một ông già mặc áo choàng đen. Cậu gọi ô…

```text
Wide 16:9 landscape cinematic frame. a tall old man in a tattered black cloak standing on the side of a skyscraper in an inner world. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nhưng phần cuối truyện tiết lộ: ông già đó thật ra là hiện thân của một dòng sức mạnh khác trong dòng máu của…

```text
Wide 16:9 landscape cinematic frame. a split image: the cloaked old man on one side, a pale mirror-like double with dark eyes on the other. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Vì vậy thanh kiếm của cậu phải được rèn lại, lần này thành hai thanh, phản ánh đúng hai nửa sức mạnh trong cậ…

```text
Wide 16:9 landscape cinematic frame. a blacksmith's forge with two blades glowing on the anvil, one large and one small. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chi tiết này khiến cả bậc thang có ý nghĩa mới. Biết tên kiếm chưa đủ. Phải biết thật sự mình l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking into a mirror that shows a slightly different owl. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Những bậc thang song song

Lời: Bleach không chỉ có một bậc thang. Các chủng tộc khác cũng có con đường tiến hóa riêng, và nhìn chúng cạnh nh…

```text
Wide 16:9 landscape cinematic frame. three staircases side by side in a vast void, each a different color. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Những kẻ phản bội từ phe ác linh có dạng giải phóng riêng: họ niêm phong sức mạnh ác linh vào hình dạng một t…

```text
Wide 16:9 landscape cinematic frame. a warrior-like figure with a bone mask fragment releasing a sword into a monstrous armored form. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Còn những cung thủ thuộc tộc người đối lập với tử thần có dạng giải phóng hoàn toàn, với đôi cánh ánh sáng và…

```text
Wide 16:9 landscape cinematic frame. an archer figure with glowing wings of light and a halo, arrows of energy hovering around them. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Điểm chung của cả ba: sức mạnh tối thượng luôn đến từ việc chấp nhận bản chất thật của mình, dù bản chất đó l…

```text
Wide 16:9 landscape cinematic frame. three figures on top of three staircases, each facing a mirror of themselves. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Góc nhìn của Kaku: kiếm là chính mình · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại cả bậc thang, Kaku thấy Bleach đang kể một câu chuyện về sự thấu hiểu bản thân, không phải về sức mạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting at the top of a small staircase, looking back down it thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nấc không là một trang giấy trắng. Nấc một là khi linh hồn bạn in dấu vào kiếm. Nấc hai là khi bạn chịu lắng…

```text
Wide 16:9 landscape cinematic frame. the first four steps lighting up one by one with small icons: blank page, fingerprint, ear, voice. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nấc bốn là khi bạn đối mặt với linh hồn đó. Và nấc năm là khi bạn khuất phục nó, không phải bằng cách tiêu di…

```text
Wide 16:9 landscape cinematic frame. the top steps lighting up: two faces meeting, then a hand resting on a kneeling spirit's shoulder. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nói cách khác: thanh kiếm mạnh nhất là thanh kiếm hiểu bạn nhất, và bạn hiểu nó nhất. Người chưa biết mình là…

```text
Wide 16:9 landscape cinematic frame. a warrior and their sword spirit standing side by side at the peak, looking at the same horizon. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kaku nghĩ đó là lý do các cảnh giải phóng kiếm trong Bleach luôn xúc động. Đó không chỉ là tăng sức mạnh, mà…

```text
Wide 16:9 landscape cinematic frame. a single cherry blossom petal landing on a sheathed blade in soft morning light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Trò chơi: đặt tên thanh kiếm của bạn · **Kaku** (đính kèm ảnh mẫu)

Lời: Trò chơi cuối: hãy tự đặt tên cho trảm phách đao của bạn, theo đúng luật của Bleach. Tất nhiên đây là trò vui…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank sword tag and a brush. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bước một: nghĩ về tính cách của bạn. Nóng nảy thì có thể là lửa. Điềm tĩnh thì có thể là nước hay băng. Hay t…

```text
Wide 16:9 landscape cinematic frame. four small elemental icons around a thoughtful silhouette: fire, water, ice and wind. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bước hai: chọn một động từ làm câu lệnh, như bùng cháy, đóng băng, hay thức dậy. Bước ba: đặt tên kiếm, thườn…

```text
Wide 16:9 landscape cinematic frame. calligraphy practice sheet with verbs and names written in brush strokes. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử trước: câu lệnh là lật trang, tên kiếm là Mực Đêm. Năng lực: biến mọi dòng chữ thành những con chim…

```text
Wide 16:9 landscape cinematic frame. the owl mascot raising a pen like a sword as ink birds burst out of its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Giờ tới bạn. Hãy viết câu lệnh, tên kiếm và năng lực vào phần bình luận. Kaku sẽ chọn vài cái hay nhất để vẽ…

```text
Wide 16:9 landscape cinematic frame. a blank comment card with three lines and a small sword doodle. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Kết

Lời: Tóm lại: bậc thang của trảm phách đao đi từ thanh kiếm không tên, qua trạng thái niêm phong, biết tên kiếm, S…

```text
Wide 16:9 landscape cinematic frame. a summary staircase with six glowing steps and small labels. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Mỗi nấc cao hơn cần hiểu linh hồn kiếm sâu hơn, mạnh hơn nhiều lần, và mang cái giá lớn hơn: Bankai gãy thì k…

```text
Wide 16:9 landscape cinematic frame. a staircase where each higher step casts a longer, darker shadow. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có Bankai, bạn muốn nó khổng lồ như một đội quân, hay nhỏ gọn và nhanh như một tia chớp?

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a giant toy sword in one wing and a tiny dagger in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tới, Kaku sẽ trải một cuộn giấy dài tám trăm năm, để xếp lại dòng thời gian của thế giới One Piece và b…

```text
Wide 16:9 landscape cinematic frame. a very long scroll unrolling across a wooden floor with a faded map and dates. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy đăng ký kênh nếu bạn thích video. Kaku tra bút vào vỏ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot sliding a pen into a tiny sheath at its side and bowing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Tử thần và thanh kiếm

Khoảng 120 giây · cảnh s01–s10 · 1554 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Bleach tới hết anime Huyết chiến ngàn năm, kể cả phần cuối vừa phát xong năm 2026. Nếu bạn chưa xem hết, hãy lưu video lại nhé.

<short pause> Một thanh kiếm Nhật bình thường. Không phát sáng, không có hoa văn đặc biệt. <short pause> Nhưng nếu bạn gọi đúng tên nó, nó sẽ trả lời.

<short pause> Trong Bleach, mỗi thanh kiếm của tử thần có một linh hồn riêng. Và sức mạnh của người cầm kiếm tăng theo mức độ họ hiểu linh hồn đó.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku vẽ một bậc thang sáu nấc, từ thanh kiếm không tên cho tới Bankai. Mỗi nấc có ba dòng: điều kiện, sức mạnh, và cái giá.

<short pause> Bộ anime Huyết chiến ngàn năm vừa khép lại vào tháng 10 năm 2026, sau gần bốn năm. Đây là lúc tốt nhất để nhìn lại toàn bộ con đường của thanh kiếm.

<short pause> Trước khi leo thang, cần biết tử thần là ai. Trong Bleach, tử thần là những linh hồn chiến binh, dẫn dắt linh hồn người chết sang thế giới bên kia và chiến đấu với ác linh.

<short pause> Vũ khí của họ là trảm phách đao, thanh kiếm có thể chém cả linh hồn. Nó không phải đồ rèn sẵn để phát cho ai cũng như ai, mà phản chiếu linh hồn của chính người cầm.

<short pause> Vì vậy không có hai thanh trảm phách đao nào giống nhau. Có thanh mang lửa, có thanh mang băng, có thanh biến thành cánh hoa, có thanh biến thành một con thú khổng lồ.

<short pause> Bleach là manga của Kubo Tite, đăng từ năm 2001 tới 2016. Phần cuối của truyện được chuyển thể thành bộ anime Huyết chiến ngàn năm, phát từ năm 2022.

<short pause> Kaku ghi chú: Bleach nổi tiếng với cách đặt tên và câu gọi kiếm rất đẹp. Mỗi lần giải phóng là một câu thơ ngắn. Kaku sẽ dùng tên tiếng Nhật cho các nấc, vì dịch ra nghe không ngầu bằng.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Bleach tới hết anime Huyết chiến ngàn năm, kể cả phần cuối vừa phát xong năm 2026. Nếu bạn chưa xem hết, hãy lưu video lại nhé.

[pause] Một thanh kiếm Nhật bình thường. Không phát sáng, không có hoa văn đặc biệt. [pause] Nhưng nếu bạn gọi đúng tên nó, nó sẽ trả lời.

[pause] Trong Bleach, mỗi thanh kiếm của tử thần có một linh hồn riêng. Và sức mạnh của người cầm kiếm tăng theo mức độ họ hiểu linh hồn đó.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku vẽ một bậc thang sáu nấc, từ thanh kiếm không tên cho tới Bankai. Mỗi nấc có ba dòng: điều kiện, sức mạnh, và cái giá.

[pause] Bộ anime Huyết chiến ngàn năm vừa khép lại vào tháng 10 năm 2026, sau gần bốn năm. Đây là lúc tốt nhất để nhìn lại toàn bộ con đường của thanh kiếm.

[pause] Trước khi leo thang, cần biết tử thần là ai. Trong Bleach, tử thần là những linh hồn chiến binh, dẫn dắt linh hồn người chết sang thế giới bên kia và chiến đấu với ác linh.

[pause] Vũ khí của họ là trảm phách đao, thanh kiếm có thể chém cả linh hồn. Nó không phải đồ rèn sẵn để phát cho ai cũng như ai, mà phản chiếu linh hồn của chính người cầm.

[pause] Vì vậy không có hai thanh trảm phách đao nào giống nhau. Có thanh mang lửa, có thanh mang băng, có thanh biến thành cánh hoa, có thanh biến thành một con thú khổng lồ.

[pause] Bleach là manga của Kubo Tite, đăng từ năm 2001 tới 2016. Phần cuối của truyện được chuyển thể thành bộ anime Huyết chiến ngàn năm, phát từ năm 2022.

[pause] Kaku ghi chú: Bleach nổi tiếng với cách đặt tên và câu gọi kiếm rất đẹp. Mỗi lần giải phóng là một câu thơ ngắn. Kaku sẽ dùng tên tiếng Nhật cho các nấc, vì dịch ra nghe không ngầu bằng.
```

### c02 · Nấc 0: Thanh kiếm không tên / Nấc 1: Trạng thái niêm phong

Khoảng 115 giây · cảnh s11–s21 · 1498 ký tự

**Gemini**

```text
Nấc đầu tiên của bậc thang thật ra là con số không. Phần cuối truyện tiết lộ rằng mọi tử thần đều bắt đầu với một thanh kiếm không tên gọi là Asauchi.

<short pause> Điều kiện: vào học viện đào tạo tử thần và nhận kiếm. Thanh kiếm lúc này không có linh hồn riêng, giống như một trang giấy trắng.

<short pause> Sức mạnh: chỉ là một thanh kiếm chém được linh hồn. Người cầm dùng nó bằng kiếm thuật thuần túy.

<short pause> Cái giá: chưa có. <short pause> Nhưng khi chủ nhân chiến đấu, rèn luyện và sống cùng thanh kiếm, linh hồn của họ dần in dấu vào nó. Thanh kiếm bắt đầu trở thành của riêng họ.

<short pause> Điều đó cũng giải thích vì sao thanh kiếm của một người không thể đem cho người khác dùng như của mình. Nó đã mang hình dạng linh hồn của đúng một người.

<short pause> <laugh> Kaku ghi chú: đây là chi tiết rất đẹp. Thanh kiếm không có sẵn tính cách. Nó lớn lên cùng bạn.

<short pause> Nấc một là trạng thái mà ta thấy thường xuyên nhất: thanh kiếm đã có linh hồn riêng, nhưng đang ngủ, trông như một thanh katana bình thường.

<short pause> Điều kiện: thanh kiếm đã mang linh hồn của chủ nhân. Mỗi thanh có một chuôi, một đốc kiếm khác nhau, như dấu vân tay.

<short pause> Sức mạnh: vẫn chỉ là kiếm thuật cộng với sức mạnh tâm linh của người dùng. <short pause> Nhưng với những người rất mạnh, chỉ một nhát chém ở trạng thái này cũng đã đủ nguy hiểm.

<short pause> Cái giá: không có gì, ngoài việc bạn chưa khai thác được sức mạnh thật của nó. Nhiều tử thần cả đời chỉ ở nấc này.

<short pause> Thú vị là có vài nhân vật giữ kiếm ở trạng thái giải phóng suốt, vì sức mạnh tâm linh quá lớn khiến thanh kiếm không thể quay về hình dạng thường. Nhân vật chính Ichigo là một ví dụ.
```

**ElevenLabs**

```text
Nấc đầu tiên của bậc thang thật ra là con số không. Phần cuối truyện tiết lộ rằng mọi tử thần đều bắt đầu với một thanh kiếm không tên gọi là Asauchi.

[pause] Điều kiện: vào học viện đào tạo tử thần và nhận kiếm. Thanh kiếm lúc này không có linh hồn riêng, giống như một trang giấy trắng.

[pause] Sức mạnh: chỉ là một thanh kiếm chém được linh hồn. Người cầm dùng nó bằng kiếm thuật thuần túy.

[pause] Cái giá: chưa có. [pause] Nhưng khi chủ nhân chiến đấu, rèn luyện và sống cùng thanh kiếm, linh hồn của họ dần in dấu vào nó. Thanh kiếm bắt đầu trở thành của riêng họ.

[pause] Điều đó cũng giải thích vì sao thanh kiếm của một người không thể đem cho người khác dùng như của mình. Nó đã mang hình dạng linh hồn của đúng một người.

[pause] [chuckles] Kaku ghi chú: đây là chi tiết rất đẹp. Thanh kiếm không có sẵn tính cách. Nó lớn lên cùng bạn.

[pause] Nấc một là trạng thái mà ta thấy thường xuyên nhất: thanh kiếm đã có linh hồn riêng, nhưng đang ngủ, trông như một thanh katana bình thường.

[pause] Điều kiện: thanh kiếm đã mang linh hồn của chủ nhân. Mỗi thanh có một chuôi, một đốc kiếm khác nhau, như dấu vân tay.

[pause] Sức mạnh: vẫn chỉ là kiếm thuật cộng với sức mạnh tâm linh của người dùng. [pause] Nhưng với những người rất mạnh, chỉ một nhát chém ở trạng thái này cũng đã đủ nguy hiểm.

[pause] Cái giá: không có gì, ngoài việc bạn chưa khai thác được sức mạnh thật của nó. Nhiều tử thần cả đời chỉ ở nấc này.

[pause] Thú vị là có vài nhân vật giữ kiếm ở trạng thái giải phóng suốt, vì sức mạnh tâm linh quá lớn khiến thanh kiếm không thể quay về hình dạng thường. Nhân vật chính Ichigo là một ví dụ.
```

### c03 · Nấc 2: Biết tên thanh kiếm / Nấc 3: Shikai

Khoảng 123 giây · cảnh s22–s32 · 1603 ký tự

**Gemini**

```text
Nấc hai là bước ngoặt đầu tiên: nghe được tên của thanh kiếm. Không phải tự đặt tên, mà là nghe linh hồn trong kiếm nói tên của nó.

<short pause> Điều kiện: đối thoại với linh hồn trong kiếm, thường qua thiền định, hoặc trong những khoảnh khắc sinh tử. Linh hồn kiếm sống trong thế giới nội tâm của chủ nhân.

<short pause> Thế giới nội tâm này phản chiếu tâm trạng của người đó. Khi họ buồn, trong đó có thể đổ mưa. Khi họ quyết tâm, bầu trời trong đó trong xanh.

<short pause> Sức mạnh: chưa tăng ngay, nhưng đây là chìa khóa để mở nấc tiếp theo. Cái giá: không phải ai cũng nghe được. Có người mất hàng chục năm, có người không bao giờ nghe thấy.

<short pause> <laugh> Kaku ghi chú: để mạnh hơn, trước tiên phải biết lắng nghe. Kaku thấy câu này đúng cả với việc học hành.

<short pause> Nấc ba là Shikai, lần giải phóng đầu tiên. Người dùng hô một câu lệnh, rồi gọi tên thanh kiếm. Thanh kiếm biến đổi hình dạng và thức tỉnh năng lực.

<short pause> Điều kiện: biết tên kiếm và có đủ sức mạnh tâm linh. Câu lệnh thường là một động từ ngắn, như rơi xuống, gầm lên, hay tan ra, rồi tới tên kiếm.

<short pause> Sức mạnh: rất đa dạng. Có thanh kiếm tan thành hàng nghìn lưỡi dao nhỏ như cánh hoa anh đào. Có thanh biến thành một con rồng băng. Có thanh kéo dài và uốn như một con rắn.

<short pause> Cái giá: tiêu hao sức mạnh tâm linh, và tiết lộ năng lực cho đối thủ. Trong Bleach, biết năng lực của kiếm đối phương là lợi thế cực lớn.

<short pause> Hầu hết các đội phó và nhiều tử thần mạnh đều đạt tới Shikai. Đây là nấc phân biệt người lính thường với một chiến binh thật sự.

<short pause> Kaku ghi chú: có một điều kỳ lạ là có những nhân vật rất mạnh mà mãi tới phần cuối truyện mới biết tên thanh kiếm của mình. Sức mạnh thô đôi khi đi trước cả sự thấu hiểu.
```

**ElevenLabs**

```text
Nấc hai là bước ngoặt đầu tiên: nghe được tên của thanh kiếm. Không phải tự đặt tên, mà là nghe linh hồn trong kiếm nói tên của nó.

[pause] Điều kiện: đối thoại với linh hồn trong kiếm, thường qua thiền định, hoặc trong những khoảnh khắc sinh tử. Linh hồn kiếm sống trong thế giới nội tâm của chủ nhân.

[pause] Thế giới nội tâm này phản chiếu tâm trạng của người đó. Khi họ buồn, trong đó có thể đổ mưa. Khi họ quyết tâm, bầu trời trong đó trong xanh.

[pause] Sức mạnh: chưa tăng ngay, nhưng đây là chìa khóa để mở nấc tiếp theo. Cái giá: không phải ai cũng nghe được. Có người mất hàng chục năm, có người không bao giờ nghe thấy.

[pause] [chuckles] Kaku ghi chú: để mạnh hơn, trước tiên phải biết lắng nghe. Kaku thấy câu này đúng cả với việc học hành.

[pause] Nấc ba là Shikai, lần giải phóng đầu tiên. Người dùng hô một câu lệnh, rồi gọi tên thanh kiếm. Thanh kiếm biến đổi hình dạng và thức tỉnh năng lực.

[pause] Điều kiện: biết tên kiếm và có đủ sức mạnh tâm linh. Câu lệnh thường là một động từ ngắn, như rơi xuống, gầm lên, hay tan ra, rồi tới tên kiếm.

[pause] Sức mạnh: rất đa dạng. Có thanh kiếm tan thành hàng nghìn lưỡi dao nhỏ như cánh hoa anh đào. Có thanh biến thành một con rồng băng. Có thanh kéo dài và uốn như một con rắn.

[pause] Cái giá: tiêu hao sức mạnh tâm linh, và tiết lộ năng lực cho đối thủ. Trong Bleach, biết năng lực của kiếm đối phương là lợi thế cực lớn.

[pause] Hầu hết các đội phó và nhiều tử thần mạnh đều đạt tới Shikai. Đây là nấc phân biệt người lính thường với một chiến binh thật sự.

[pause] Kaku ghi chú: có một điều kỳ lạ là có những nhân vật rất mạnh mà mãi tới phần cuối truyện mới biết tên thanh kiếm của mình. Sức mạnh thô đôi khi đi trước cả sự thấu hiểu.
```

### c04 · Những câu lệnh giải phóng đẹp nhất / Nấc 4: Cụ hiện hóa

Khoảng 101 giây · cảnh s33–s42 · 1313 ký tự

**Gemini**

```text
Trước khi nói về cái giá, Kaku muốn dừng lại ở thứ khiến Shikai trong Bleach đáng nhớ: những câu lệnh giải phóng.

<short pause> Mỗi câu lệnh là một động từ ngắn trong tiếng Nhật, và nó thường gợi tả đúng năng lực của thanh kiếm.

<short pause> Thanh kiếm tan thành cánh hoa được gọi bằng lệnh rơi rụng. Thanh kiếm hình rắn được gọi bằng lệnh gầm lên. Thanh kiếm băng được gọi bằng một câu dài hơn: ngự trên bầu trời băng giá.

<short pause> Có lệnh là nhảy múa, có lệnh là gầm gừ, có lệnh là vươn dài. Nghe tên câu lệnh, người xem gần như đoán được tính cách của cả thanh kiếm lẫn chủ nhân.

<short pause> Đây là một cách xây dựng nhân vật rất tiết kiệm: chỉ một câu ngắn, mà nói lên cả một con người.

<short pause> <laugh> Kaku ghi chú: nếu bạn học tiếng Nhật, các câu lệnh này là cách học động từ vui nhất quả đất.

<short pause> Giữa Shikai và Bankai có một nấc mà nhiều người quên: cụ hiện hóa, tức là kéo linh hồn thanh kiếm ra khỏi thế giới nội tâm, đưa nó xuất hiện trong thế giới thực.

<short pause> Điều kiện: sức mạnh tâm linh và sự hòa hợp đủ lớn để linh hồn kiếm có hình dạng thật. Việc này thường mất rất nhiều năm.

<short pause> Sức mạnh: chưa tăng, nhưng người dùng giờ có thể đối mặt trực tiếp với linh hồn kiếm. Và bước tiếp theo đòi hỏi chính điều đó.

<short pause> Cái giá: thời gian và nguy hiểm. Linh hồn kiếm không phải lúc nào cũng thân thiện. Có linh hồn kiêu ngạo, có linh hồn hung dữ, có linh hồn thử thách chủ nhân bằng cả mạng sống.
```

**ElevenLabs**

```text
Trước khi nói về cái giá, Kaku muốn dừng lại ở thứ khiến Shikai trong Bleach đáng nhớ: những câu lệnh giải phóng.

[pause] Mỗi câu lệnh là một động từ ngắn trong tiếng Nhật, và nó thường gợi tả đúng năng lực của thanh kiếm.

[pause] Thanh kiếm tan thành cánh hoa được gọi bằng lệnh rơi rụng. Thanh kiếm hình rắn được gọi bằng lệnh gầm lên. Thanh kiếm băng được gọi bằng một câu dài hơn: ngự trên bầu trời băng giá.

[pause] Có lệnh là nhảy múa, có lệnh là gầm gừ, có lệnh là vươn dài. Nghe tên câu lệnh, người xem gần như đoán được tính cách của cả thanh kiếm lẫn chủ nhân.

[pause] Đây là một cách xây dựng nhân vật rất tiết kiệm: chỉ một câu ngắn, mà nói lên cả một con người.

[pause] [chuckles] Kaku ghi chú: nếu bạn học tiếng Nhật, các câu lệnh này là cách học động từ vui nhất quả đất.

[pause] Giữa Shikai và Bankai có một nấc mà nhiều người quên: cụ hiện hóa, tức là kéo linh hồn thanh kiếm ra khỏi thế giới nội tâm, đưa nó xuất hiện trong thế giới thực.

[pause] Điều kiện: sức mạnh tâm linh và sự hòa hợp đủ lớn để linh hồn kiếm có hình dạng thật. Việc này thường mất rất nhiều năm.

[pause] Sức mạnh: chưa tăng, nhưng người dùng giờ có thể đối mặt trực tiếp với linh hồn kiếm. Và bước tiếp theo đòi hỏi chính điều đó.

[pause] Cái giá: thời gian và nguy hiểm. Linh hồn kiếm không phải lúc nào cũng thân thiện. Có linh hồn kiêu ngạo, có linh hồn hung dữ, có linh hồn thử thách chủ nhân bằng cả mạng sống.
```

### c05 · Nấc 5: Bankai / Cái giá của Bankai

Khoảng 137 giây · cảnh s43–s55 · 1777 ký tự

**Gemini**

```text
Nấc cao nhất là Bankai, lần giải phóng cuối cùng. Để đạt được, người dùng phải cụ hiện hóa linh hồn kiếm, rồi khuất phục nó, thường là trong một trận đấu.

<short pause> Điều kiện: theo truyện, ngay cả người có tài năng cũng cần khoảng mười năm hoặc hơn để thành thạo Bankai. Đó là lý do nó hiếm đến vậy.

<short pause> Nhân vật chính là ngoại lệ nổi tiếng: nhờ một phương pháp luyện đặc biệt và đặt cược cả mạng sống, cậu đạt Bankai chỉ trong khoảng ba ngày.

<short pause> Sức mạnh: truyện nói Bankai mạnh hơn Shikai khoảng năm đến mười lần. Hình dạng thay đổi hoàn toàn, có khi thành cả một chiến trường hay một sinh vật khổng lồ.

<short pause> Có Bankai thì gần như đủ điều kiện làm đội trưởng. Trong mười ba đội của lực lượng tử thần, gần như tất cả đội trưởng đều có Bankai.

<short pause> Mỗi Bankai cũng có tên riêng, thường dài hơn tên kiếm ở Shikai, như thể thanh kiếm được gọi bằng tên đầy đủ khi đã trưởng thành hoàn toàn.

<short pause> <laugh> Kaku ghi chú: không phải Bankai nào cũng to lớn. Bankai của nhân vật chính lại thu nhỏ thành một thanh kiếm đen mảnh, dồn toàn bộ sức mạnh vào tốc độ.

<short pause> Bankai mạnh nhất, nhưng cũng là nấc có cái giá đáng sợ nhất. Và cái giá đó không chỉ là thể lực.

<short pause> Truyện nói Bankai bị gãy thì không bao giờ phục hồi hoàn toàn như cũ. Với nhiều người, mất Bankai giống như mất một phần linh hồn.

<short pause> Có Bankai gắn chặt với cơ thể chủ nhân đến mức vết thương của Bankai truyền thẳng sang người dùng. Bankai càng lớn, rủi ro càng lớn.

<short pause> Và trong Huyết chiến ngàn năm, xuất hiện một mối đe dọa chưa từng có: kẻ thù có thể cướp Bankai, rồi dùng chính sức mạnh đó chống lại chủ nhân.

<short pause> Nhiều đội trưởng mất Bankai trong đợt tấn công đầu tiên. Đó là lúc cả lực lượng nhận ra nấc cao nhất cũng là điểm yếu lớn nhất nếu bị lấy đi.

<short pause> Kaku ghi chú: đây là thiết kế rất thông minh. Kẻ địch mạnh nhất không cần mạnh hơn bạn. Chỉ cần lấy đi thứ bạn dựa vào nhiều nhất.
```

**ElevenLabs**

```text
Nấc cao nhất là Bankai, lần giải phóng cuối cùng. Để đạt được, người dùng phải cụ hiện hóa linh hồn kiếm, rồi khuất phục nó, thường là trong một trận đấu.

[pause] Điều kiện: theo truyện, ngay cả người có tài năng cũng cần khoảng mười năm hoặc hơn để thành thạo Bankai. Đó là lý do nó hiếm đến vậy.

[pause] Nhân vật chính là ngoại lệ nổi tiếng: nhờ một phương pháp luyện đặc biệt và đặt cược cả mạng sống, cậu đạt Bankai chỉ trong khoảng ba ngày.

[pause] Sức mạnh: truyện nói Bankai mạnh hơn Shikai khoảng năm đến mười lần. Hình dạng thay đổi hoàn toàn, có khi thành cả một chiến trường hay một sinh vật khổng lồ.

[pause] Có Bankai thì gần như đủ điều kiện làm đội trưởng. Trong mười ba đội của lực lượng tử thần, gần như tất cả đội trưởng đều có Bankai.

[pause] Mỗi Bankai cũng có tên riêng, thường dài hơn tên kiếm ở Shikai, như thể thanh kiếm được gọi bằng tên đầy đủ khi đã trưởng thành hoàn toàn.

[pause] [chuckles] Kaku ghi chú: không phải Bankai nào cũng to lớn. Bankai của nhân vật chính lại thu nhỏ thành một thanh kiếm đen mảnh, dồn toàn bộ sức mạnh vào tốc độ.

[pause] Bankai mạnh nhất, nhưng cũng là nấc có cái giá đáng sợ nhất. Và cái giá đó không chỉ là thể lực.

[pause] Truyện nói Bankai bị gãy thì không bao giờ phục hồi hoàn toàn như cũ. Với nhiều người, mất Bankai giống như mất một phần linh hồn.

[pause] Có Bankai gắn chặt với cơ thể chủ nhân đến mức vết thương của Bankai truyền thẳng sang người dùng. Bankai càng lớn, rủi ro càng lớn.

[pause] Và trong Huyết chiến ngàn năm, xuất hiện một mối đe dọa chưa từng có: kẻ thù có thể cướp Bankai, rồi dùng chính sức mạnh đó chống lại chủ nhân.

[pause] Nhiều đội trưởng mất Bankai trong đợt tấn công đầu tiên. Đó là lúc cả lực lượng nhận ra nấc cao nhất cũng là điểm yếu lớn nhất nếu bị lấy đi.

[pause] Kaku ghi chú: đây là thiết kế rất thông minh. Kẻ địch mạnh nhất không cần mạnh hơn bạn. Chỉ cần lấy đi thứ bạn dựa vào nhiều nhất.
```

### c06 · Ba hiểu lầm về Bankai / Bí mật của thanh kiếm nhân vật chính

Khoảng 116 giây · cảnh s56–s65 · 1513 ký tự

**Gemini**

```text
Có ba hiểu lầm về Bankai mà Kaku hay thấy trong bình luận, gỡ nhanh trước khi tới bí mật lớn nhất.

<short pause> Hiểu lầm một: Bankai luôn mạnh hơn mọi Shikai. Không hẳn. Bankai của một người luôn mạnh hơn Shikai của chính họ, nhưng có những Shikai đặc biệt nguy hiểm hơn Bankai của người khác.

<short pause> Hiểu lầm hai: ai có Bankai cũng muốn khoe. Thực ra có nhân vật cố tình giấu Bankai của mình, vì nếu lộ ra sẽ bị điều lên làm đội trưởng ở nơi khác, trong khi anh chỉ muốn chiến đấu dưới trướng đội trưởng của mình.

<short pause> Hiểu lầm ba: Bankai là giới hạn cuối cùng. Truyện cho thấy có những sức mạnh vượt cả Bankai. <short pause> Nhưng một trong số đó đòi hỏi nhân vật chính trả bằng toàn bộ sức mạnh tử thần của mình sau khi dùng.

<short pause> <laugh> Kaku ghi chú: cả ba hiểu lầm cho thấy một điều: trong Bleach, sức mạnh không phải là một con số, mà là một lựa chọn, và lựa chọn nào cũng có hậu quả.

<short pause> Bây giờ là spoiler lớn nhất video. Nếu chưa xem hết Huyết chiến ngàn năm, bạn có thể tua qua chương này.

<short pause> Suốt nhiều năm, nhân vật chính tưởng linh hồn thanh kiếm của mình là một ông già mặc áo choàng đen. Cậu gọi ông bằng tên thanh kiếm và coi ông là thầy.

<short pause> Nhưng phần cuối truyện tiết lộ: ông già đó thật ra là hiện thân của một dòng sức mạnh khác trong dòng máu của cậu. Còn linh hồn thật của thanh kiếm lại là thứ cậu vẫn tưởng là kẻ thù bên trong mình.

<short pause> Vì vậy thanh kiếm của cậu phải được rèn lại, lần này thành hai thanh, phản ánh đúng hai nửa sức mạnh trong cậu.

<short pause> Kaku ghi chú: chi tiết này khiến cả bậc thang có ý nghĩa mới. Biết tên kiếm chưa đủ. Phải biết thật sự mình là ai.
```

**ElevenLabs**

```text
Có ba hiểu lầm về Bankai mà Kaku hay thấy trong bình luận, gỡ nhanh trước khi tới bí mật lớn nhất.

[pause] Hiểu lầm một: Bankai luôn mạnh hơn mọi Shikai. Không hẳn. Bankai của một người luôn mạnh hơn Shikai của chính họ, nhưng có những Shikai đặc biệt nguy hiểm hơn Bankai của người khác.

[pause] Hiểu lầm hai: ai có Bankai cũng muốn khoe. Thực ra có nhân vật cố tình giấu Bankai của mình, vì nếu lộ ra sẽ bị điều lên làm đội trưởng ở nơi khác, trong khi anh chỉ muốn chiến đấu dưới trướng đội trưởng của mình.

[pause] Hiểu lầm ba: Bankai là giới hạn cuối cùng. Truyện cho thấy có những sức mạnh vượt cả Bankai. [pause] Nhưng một trong số đó đòi hỏi nhân vật chính trả bằng toàn bộ sức mạnh tử thần của mình sau khi dùng.

[pause] [chuckles] Kaku ghi chú: cả ba hiểu lầm cho thấy một điều: trong Bleach, sức mạnh không phải là một con số, mà là một lựa chọn, và lựa chọn nào cũng có hậu quả.

[pause] Bây giờ là spoiler lớn nhất video. Nếu chưa xem hết Huyết chiến ngàn năm, bạn có thể tua qua chương này.

[pause] Suốt nhiều năm, nhân vật chính tưởng linh hồn thanh kiếm của mình là một ông già mặc áo choàng đen. Cậu gọi ông bằng tên thanh kiếm và coi ông là thầy.

[pause] Nhưng phần cuối truyện tiết lộ: ông già đó thật ra là hiện thân của một dòng sức mạnh khác trong dòng máu của cậu. Còn linh hồn thật của thanh kiếm lại là thứ cậu vẫn tưởng là kẻ thù bên trong mình.

[pause] Vì vậy thanh kiếm của cậu phải được rèn lại, lần này thành hai thanh, phản ánh đúng hai nửa sức mạnh trong cậu.

[pause] Kaku ghi chú: chi tiết này khiến cả bậc thang có ý nghĩa mới. Biết tên kiếm chưa đủ. Phải biết thật sự mình là ai.
```

### c07 · Những bậc thang song song / Góc nhìn của Kaku: kiếm là chính mình / Trò chơi: đặt tên thanh kiếm của bạn

Khoảng 147 giây · cảnh s66–s79 · 1911 ký tự

**Gemini**

```text
Bleach không chỉ có một bậc thang. Các chủng tộc khác cũng có con đường tiến hóa riêng, và nhìn chúng cạnh nhau rất thú vị.

<short pause> Những kẻ phản bội từ phe ác linh có dạng giải phóng riêng: họ niêm phong sức mạnh ác linh vào hình dạng một thanh kiếm, và khi giải phóng thì trở về dạng thật.

<short pause> Còn những cung thủ thuộc tộc người đối lập với tử thần có dạng giải phóng hoàn toàn, với đôi cánh ánh sáng và vầng hào quang trên đầu.

<short pause> Điểm chung của cả ba: sức mạnh tối thượng luôn đến từ việc chấp nhận bản chất thật của mình, dù bản chất đó là gì.

<short pause> <laugh> Nhìn lại cả bậc thang, Kaku thấy Bleach đang kể một câu chuyện về sự thấu hiểu bản thân, không phải về sức mạnh.

<short pause> Nấc không là một trang giấy trắng. Nấc một là khi linh hồn bạn in dấu vào kiếm. Nấc hai là khi bạn chịu lắng nghe. Nấc ba là khi bạn gọi đúng tên.

<short pause> Nấc bốn là khi bạn đối mặt với linh hồn đó. Và nấc năm là khi bạn khuất phục nó, không phải bằng cách tiêu diệt, mà bằng cách chứng minh mình xứng đáng.

<short pause> Nói cách khác: thanh kiếm mạnh nhất là thanh kiếm hiểu bạn nhất, và bạn hiểu nó nhất. Người chưa biết mình là ai thì không thể leo tới đỉnh.

<short pause> Kaku nghĩ đó là lý do các cảnh giải phóng kiếm trong Bleach luôn xúc động. Đó không chỉ là tăng sức mạnh, mà là một người vừa hiểu thêm về chính mình.

<short pause> Trò chơi cuối: hãy tự đặt tên cho trảm phách đao của bạn, theo đúng luật của Bleach. Tất nhiên đây là trò vui, tên do bạn tự nghĩ.

<short pause> Bước một: nghĩ về tính cách của bạn. Nóng nảy thì có thể là lửa. Điềm tĩnh thì có thể là nước hay băng. Hay thay đổi thì có thể là gió.

<short pause> Bước hai: chọn một động từ làm câu lệnh, như bùng cháy, đóng băng, hay thức dậy. Bước ba: đặt tên kiếm, thường là tên một hiện tượng hay sinh vật.

<short pause> Kaku thử trước: câu lệnh là lật trang, tên kiếm là Mực Đêm. Năng lực: biến mọi dòng chữ thành những con chim mực bay ra khỏi trang giấy.

<short pause> Giờ tới bạn. Hãy viết câu lệnh, tên kiếm và năng lực vào phần bình luận. Kaku sẽ chọn vài cái hay nhất để vẽ minh họa trong video sau.
```

**ElevenLabs**

```text
Bleach không chỉ có một bậc thang. Các chủng tộc khác cũng có con đường tiến hóa riêng, và nhìn chúng cạnh nhau rất thú vị.

[pause] Những kẻ phản bội từ phe ác linh có dạng giải phóng riêng: họ niêm phong sức mạnh ác linh vào hình dạng một thanh kiếm, và khi giải phóng thì trở về dạng thật.

[pause] Còn những cung thủ thuộc tộc người đối lập với tử thần có dạng giải phóng hoàn toàn, với đôi cánh ánh sáng và vầng hào quang trên đầu.

[pause] Điểm chung của cả ba: sức mạnh tối thượng luôn đến từ việc chấp nhận bản chất thật của mình, dù bản chất đó là gì.

[pause] [chuckles] Nhìn lại cả bậc thang, Kaku thấy Bleach đang kể một câu chuyện về sự thấu hiểu bản thân, không phải về sức mạnh.

[pause] Nấc không là một trang giấy trắng. Nấc một là khi linh hồn bạn in dấu vào kiếm. Nấc hai là khi bạn chịu lắng nghe. Nấc ba là khi bạn gọi đúng tên.

[pause] Nấc bốn là khi bạn đối mặt với linh hồn đó. Và nấc năm là khi bạn khuất phục nó, không phải bằng cách tiêu diệt, mà bằng cách chứng minh mình xứng đáng.

[pause] Nói cách khác: thanh kiếm mạnh nhất là thanh kiếm hiểu bạn nhất, và bạn hiểu nó nhất. Người chưa biết mình là ai thì không thể leo tới đỉnh.

[pause] Kaku nghĩ đó là lý do các cảnh giải phóng kiếm trong Bleach luôn xúc động. Đó không chỉ là tăng sức mạnh, mà là một người vừa hiểu thêm về chính mình.

[pause] Trò chơi cuối: hãy tự đặt tên cho trảm phách đao của bạn, theo đúng luật của Bleach. Tất nhiên đây là trò vui, tên do bạn tự nghĩ.

[pause] Bước một: nghĩ về tính cách của bạn. Nóng nảy thì có thể là lửa. Điềm tĩnh thì có thể là nước hay băng. Hay thay đổi thì có thể là gió.

[pause] Bước hai: chọn một động từ làm câu lệnh, như bùng cháy, đóng băng, hay thức dậy. Bước ba: đặt tên kiếm, thường là tên một hiện tượng hay sinh vật.

[pause] Kaku thử trước: câu lệnh là lật trang, tên kiếm là Mực Đêm. Năng lực: biến mọi dòng chữ thành những con chim mực bay ra khỏi trang giấy.

[pause] Giờ tới bạn. Hãy viết câu lệnh, tên kiếm và năng lực vào phần bình luận. Kaku sẽ chọn vài cái hay nhất để vẽ minh họa trong video sau.
```

### c08 · Kết

Khoảng 47 giây · cảnh s80–s84 · 611 ký tự

**Gemini**

```text
Tóm lại: bậc thang của trảm phách đao đi từ thanh kiếm không tên, qua trạng thái niêm phong, biết tên kiếm, Shikai, cụ hiện hóa, cho tới Bankai.

<short pause> Mỗi nấc cao hơn cần hiểu linh hồn kiếm sâu hơn, mạnh hơn nhiều lần, và mang cái giá lớn hơn: Bankai gãy thì không phục hồi như cũ, và có thể bị cướp đi.

<short pause> Câu hỏi cho bạn: nếu có Bankai, bạn muốn nó khổng lồ như một đội quân, hay nhỏ gọn và nhanh như một tia chớp?

<short pause> Video tới, Kaku sẽ trải một cuộn giấy dài tám trăm năm, để xếp lại dòng thời gian của thế giới One Piece và bí ẩn của Thế kỷ trống.

<short pause> Hãy đăng ký kênh nếu bạn thích video. <laugh> Kaku tra bút vào vỏ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: bậc thang của trảm phách đao đi từ thanh kiếm không tên, qua trạng thái niêm phong, biết tên kiếm, Shikai, cụ hiện hóa, cho tới Bankai.

[pause] Mỗi nấc cao hơn cần hiểu linh hồn kiếm sâu hơn, mạnh hơn nhiều lần, và mang cái giá lớn hơn: Bankai gãy thì không phục hồi như cũ, và có thể bị cướp đi.

[pause] [curious] Câu hỏi cho bạn: nếu có Bankai, bạn muốn nó khổng lồ như một đội quân, hay nhỏ gọn và nhanh như một tia chớp?

[pause] Video tới, Kaku sẽ trải một cuộn giấy dài tám trăm năm, để xếp lại dòng thời gian của thế giới One Piece và bí ẩn của Thế kỷ trống.

[pause] Hãy đăng ký kênh nếu bạn thích video. [chuckles] Kaku tra bút vào vỏ đây, hẹn gặp lại!
```
