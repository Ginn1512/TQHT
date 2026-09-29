# Bộ prompt · Naruto: Sharingan tiến hóa thế nào? Từ 1 tomoe đến Rinnegan

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 95 ảnh, 7 đoạn đọc, khoảng 14.8 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (95 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Naruto và Naruto Shippuden đến hết cuộc Đại chiến Ninja lần thứ tư. Nếu chưa xem h…

```text
Wide 16:9 landscape cinematic frame. a dark scroll unrolling on a wooden floor, a single red glowing eye symbol drawn on it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong Naruto, có một đôi mắt được cả thế giới ninja vừa thèm muốn vừa sợ hãi. Nó sao chép được nhẫn thuật, nh…

```text
Wide 16:9 landscape cinematic frame. close-up of a crimson eye with three dark comma-shaped marks glowing in the dark, rain reflections. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng đôi mắt ấy có một bí mật đau đớn: nó càng mạnh khi chủ nhân càng đau khổ.

```text
Wide 16:9 landscape cinematic frame. a figure standing alone in the rain before a graveyard, eyes glowing red. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đó là Sharingan. Và hôm nay mình sẽ đi theo từng nấc tiến hóa của nó, từ một dấu phẩy nhỏ tới con mắt của thầ…

```text
Wide 16:9 landscape cinematic frame. a staircase of glowing eye symbols evolving from simple to complex, rising into clouds. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ sẽ vẽ một bậc thang tiến hóa: mỗi nấc có sức mạnh gì, và phải trả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook, its round glasses reflecting a red light. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao lịch sử của đôi mắt này cũng là lịch sử của thù hận trong thế giới ninja.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking serious, holding a small red lantern. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Nền tảng: chakra và nhẫn thuật

Lời: Trước khi leo bậc thang, cần hiểu nền tảng của thế giới Naruto: chakra, năng lượng mà mọi ninja dùng để thực…

```text
Wide 16:9 landscape cinematic frame. a ninja silhouette with glowing blue energy lines flowing through the body like veins. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Chakra được tạo ra từ hai phần: năng lượng thể chất trong từng tế bào và năng lượng tinh thần từ sự rèn luyện…

```text
Wide 16:9 landscape cinematic frame. two streams of light, one warm and physical, one calm and mental, merging into a glowing blue orb. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ninja dùng chakra theo ba nhóm chính: nhẫn thuật như cầu lửa hay phân thân, ảo thuật đánh lừa giác quan, và t…

```text
Wide 16:9 landscape cinematic frame. three panels: a fireball, a swirling illusion, a flying kick. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Hầu hết nhẫn thuật cần kết ấn tay để điều khiển chakra. Người càng giỏi, kết ấn càng nhanh, có người rút gọn…

```text
Wide 16:9 landscape cinematic frame. a blur of hands forming seals at incredible speed, motion trails behind each finger. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Sharingan đặc biệt vì nó can thiệp vào cả ba nhóm: nhìn thấu nhẫn thuật, tạo và phá ảo thuật, và đọc trước th…

```text
Wide 16:9 landscape cinematic frame. a red eye at the center of a triangle connecting the three technique types. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đó là lý do một đôi mắt lại có thể thay đổi cục diện trận đấu. Nó không thêm một chiêu mới, mà…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering through a red-tinted magnifying glass at a scroll. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Nấc 0: đôi mắt của một gia tộc

Lời: Sharingan là huyết kế giới hạn, một năng lực di truyền, chỉ xuất hiện ở gia tộc Uchiha. Người ngoài gia tộc k…

```text
Wide 16:9 landscape cinematic frame. a village compound with a red-and-white fan emblem painted on the walls at dusk. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nhưng không phải thành viên Uchiha nào cũng có. Sharingan chỉ thức tỉnh khi người đó trải qua cảm xúc cực mạn…

```text
Wide 16:9 landscape cinematic frame. a young ninja silhouette protecting a friend in battle, eyes suddenly flashing red. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Truyện giải thích rằng Uchiha là gia tộc có tình yêu rất sâu. Khi tình yêu đó bị tổn thương, nó biến thành nỗ…

```text
Wide 16:9 landscape cinematic frame. a warm family silhouette under a lantern, then the same scene shattered like glass with a red glow. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Đây là nền tảng của mọi thứ phía sau: Sharingan không chỉ là năng lực, mà là tấm gương phản chiếu trái tim củ…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a heart that glows red, cracks spreading across the glass. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hãy nhớ quy luật này nhé. Ở mỗi nấc tiếp theo, cái giá luôn lớn hơn nấc trước.

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a single rule on a chalkboard with a red chalk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Nấc 1: Sharingan một, hai, ba dấu phẩy

Lời: Khi mới thức tỉnh, Sharingan thường có một dấu phẩy quanh con ngươi. Dấu phẩy này được gọi là tomoe.

```text
Wide 16:9 landscape cinematic frame. a crimson eye with a single black comma mark, close-up, soft glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Theo thời gian và kinh nghiệm chiến đấu, số tomoe tăng lên hai, rồi ba. Mỗi dấu phẩy thêm vào là khả năng nhì…

```text
Wide 16:9 landscape cinematic frame. a sequence of three eyes side by side showing one, two, and three comma marks. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Năng lực thứ nhất: nhìn thấy dòng chakra. Người dùng phân biệt được nhẫn thuật thật và ảo ảnh, thấy được chak…

```text
Wide 16:9 landscape cinematic frame. a figure seen through a red filter, glowing chakra lines flowing through their body. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Năng lực thứ hai: đọc chuyển động. Sharingan thấy đòn đánh tới trước khi nó chạm, giúp né và phản công gần nh…

```text
Wide 16:9 landscape cinematic frame. a ninja dodging a kunai by a hair's breadth, ghost trails showing its predicted path. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Năng lực thứ ba, nổi tiếng nhất: sao chép. Người dùng nhìn một nhẫn thuật và có thể học lại nó, miễn là cơ th…

```text
Wide 16:9 landscape cinematic frame. a ninja mirroring another ninja's hand signs perfectly, glowing lines linking their hands. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Tuy nhiên, Sharingan không sao chép được huyết kế giới hạn của gia tộc khác, vì đó là năng lực gắn với cơ thể…

```text
Wide 16:9 landscape cinematic frame. a copy diagram with a red cross over a unique bloodline symbol. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Năng lực thứ tư: ảo thuật. Chỉ cần đối thủ nhìn vào mắt, người dùng có thể kéo họ vào ảo ảnh.

```text
Wide 16:9 landscape cinematic frame. two ninjas locking eyes, the background dissolving into swirling red illusion. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: nấc một là đôi mắt của một thiên tài chiến đấu. Nhìn thấu, đọc trước, sao chép và đánh lừa.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a small red monocle, peering at a scroll. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Người ngoài dùng Sharingan: trường hợp Kakashi

Lời: Có một ngoại lệ nổi tiếng: Kakashi, không phải Uchiha nhưng có một mắt Sharingan được cấy ghép từ người bạn t…

```text
Wide 16:9 landscape cinematic frame. a masked ninja silhouette with one eye covered by a headband, a faint red glow beneath it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Vì không mang dòng máu Uchiha, cơ thể Kakashi không hợp với Sharingan. Anh không thể tắt nó, nên phải che mắt…

```text
Wide 16:9 landscape cinematic frame. a headband being pulled down over a glowing red eye. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Mỗi lần dùng, Sharingan tiêu hao chakra của anh rất nhanh. Dùng quá sức, anh có thể ngã quỵ sau trận đấu.

```text
Wide 16:9 landscape cinematic frame. an exhausted ninja collapsing onto one knee, steam rising from his body. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Dù vậy, Kakashi vẫn được gọi là Ninja Sao Chép, với hàng nghìn nhẫn thuật đã học được. Đây là minh chứng cho…

```text
Wide 16:9 landscape cinematic frame. a library of countless glowing scrolls behind a relaxed masked ninja reading a book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Nấc 2: Mangekyo Sharingan

Lời: Nấc tiến hóa thứ hai là Mangekyo Sharingan, và cái giá để có nó khủng khiếp hơn nhiều.

```text
Wide 16:9 landscape cinematic frame. a crimson eye with an intricate pinwheel-like pattern replacing the comma marks. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Theo truyện, Mangekyo thức tỉnh khi người dùng trải qua nỗi đau cực độ, thường là mất đi người thân yêu nhất,…

```text
Wide 16:9 landscape cinematic frame. a figure kneeling in shock before a fallen silhouette, their eyes transforming into a new pattern. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Mỗi Mangekyo có hoa văn riêng, và mỗi người nhận được những năng lực riêng. Không có hai Mangekyo nào giống h…

```text
Wide 16:9 landscape cinematic frame. a grid of six unique abstract pinwheel eye patterns, each glowing differently. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Có năng lực tạo ra ảo thuật thời gian, nơi vài giây ngoài đời bằng nhiều ngày tra tấn trong ảo ảnh.

```text
Wide 16:9 landscape cinematic frame. a red moonlit illusion world where a clock spins wildly while a figure is bound. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Có năng lực tạo ra ngọn lửa đen không thể dập tắt, đốt cháy mọi thứ mà người dùng nhìn vào.

```text
Wide 16:9 landscape cinematic frame. black flames erupting on a target and spreading unstoppably across a stone wall. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Có năng lực dịch chuyển đồ vật hoặc chính mình sang một không gian khác, khiến đòn đánh xuyên qua người dùng…

```text
Wide 16:9 landscape cinematic frame. a swirling vortex warping space around a masked figure as attacks pass through him. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Và khi thức tỉnh Mangekyo ở cả hai mắt, người dùng có thể gọi ra một chiến binh khổng lồ bằng chakra bao quan…

```text
Wide 16:9 landscape cinematic frame. a colossal translucent armored warrior of glowing chakra surrounding a small ninja silhouette. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là lúc Sharingan đi từ đôi mắt của thiên tài thành vũ khí có thể thay đổi cả một cuộc chiến.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up in awe at a giant glowing warrior silhouette. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Cái giá của Mangekyo

Lời: Nhưng Mangekyo có một cái giá tàn nhẫn: mỗi lần sử dụng, thị lực người dùng giảm dần. Dùng càng nhiều, càng t…

```text
Wide 16:9 landscape cinematic frame. an eye with a faint crack spreading across it, vision blurring into darkness. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Những năng lực mạnh nhất còn khiến mắt chảy máu, cơ thể kiệt quệ ngay sau khi dùng.

```text
Wide 16:9 landscape cinematic frame. a ninja clutching one bleeding eye, the other still glowing red, kneeling in the rain. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điều này tạo ra một bi kịch: đôi mắt được sinh ra từ nỗi đau mất người thân, rồi lại lấy đi ánh sáng của chín…

```text
Wide 16:9 landscape cinematic frame. a figure alone in a darkening room, a single candle slowly going out. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và nó giải thích vì sao trong truyện, những người có Mangekyo luôn tìm cách vượt qua giới hạn đó, dù cái giá…

```text
Wide 16:9 landscape cinematic frame. a staircase continuing downward into shadows beyond a red-lit landing. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Nấc 3: Mangekyo vĩnh hằng

Lời: Cách để thoát khỏi mù lòa là nấc thứ ba: Mangekyo vĩnh hằng. Và cách đạt được nó khiến người ta rùng mình.

```text
Wide 16:9 landscape cinematic frame. an eye with a pattern merged from two different pinwheel designs, glowing steadily. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Người dùng phải cấy ghép đôi mắt Mangekyo của một người ruột thịt, thường là anh em. Hai hoa văn hòa vào nhau…

```text
Wide 16:9 landscape cinematic frame. two pinwheel eye patterns overlapping and merging into a new combined design. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kết quả: người dùng không còn bị mù dần nữa, và sức mạnh của Mangekyo tăng lên rõ rệt.

```text
Wide 16:9 landscape cinematic frame. a figure opening newly clear eyes, a stronger and brighter chakra warrior forming around them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Trong lịch sử truyện, chỉ vài người đạt được nấc này, và mỗi lần đều gắn với một câu chuyện anh em đầy đau đớ…

```text
Wide 16:9 landscape cinematic frame. two brother silhouettes back to back on a cliff at sunset, one fading like smoke. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đến đây, bạn có thể thấy quy luật: mỗi nấc tiến hóa đều được trả bằng thứ quý giá hơn. Mắt của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a staircase of price tags getting larger with each step. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Những thuật cấm: Izanagi và Izanami

Lời: Bên cạnh các nấc tiến hóa, Sharingan còn có những thuật cấm, mạnh đến mức gia tộc Uchiha phải hạn chế sử dụng.

```text
Wide 16:9 landscape cinematic frame. an old locked chest sealed with red talismans in a dark clan shrine. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Izanagi cho phép người dùng viết lại thực tại trong một thời gian ngắn: những gì bất lợi xảy ra với họ có thể…

```text
Wide 16:9 landscape cinematic frame. a scene rewinding like a film strip, a fatal wound disappearing as if it never happened. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Cái giá: con mắt dùng Izanagi sẽ vĩnh viễn mất ánh sáng. Một con mắt đổi lấy vài giây như một vị thần.

```text
Wide 16:9 landscape cinematic frame. a single eye closing permanently, turning grey, while the figure stands unharmed. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Izanami được tạo ra như thuật để chấm dứt Izanagi: nó giam đối thủ trong một vòng lặp cho tới khi họ chấp nhậ…

```text
Wide 16:9 landscape cinematic frame. a figure trapped in a repeating loop of the same moment, drawn as a circular film strip. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Hai thuật này cho thấy một ý tưởng sâu sắc của truyện: sức mạnh lớn nhất không phải trốn tránh thực tại, mà l…

```text
Wide 16:9 landscape cinematic frame. a figure stepping out of a circular loop into a calm sunrise. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Những người sở hữu tiêu biểu

Lời: Mỗi nấc tiến hóa gắn với những nhân vật cụ thể. Hãy điểm qua vài người để thấy mỗi người dùng Sharingan theo…

```text
Wide 16:9 landscape cinematic frame. a row of six silhouettes with glowing red eyes standing on a misty hill. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Itachi được biết đến với ảo thuật cực mạnh và tài năng từ nhỏ. Anh dùng Sharingan không để phô diễn mà để kết…

```text
Wide 16:9 landscape cinematic frame. a calm ninja silhouette in a cloak with crows scattering around him under a red moon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Sasuke là người đi hết gần như toàn bộ bậc thang: từ một dấu phẩy, tới Mangekyo, Mangekyo vĩnh hằng, rồi Rinn…

```text
Wide 16:9 landscape cinematic frame. a young ninja silhouette climbing a long staircase of glowing eyes, darkness below and light above. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Madara là huyền thoại của gia tộc, người đầu tiên đạt Mangekyo vĩnh hằng được biết đến và sau này là Rinnegan…

```text
Wide 16:9 landscape cinematic frame. a legendary warrior silhouette with long wild hair standing on a colossal chakra warrior over a battlefield. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Shisui được nhắc tới với một ảo thuật có thể thay đổi suy nghĩ của người khác mà họ không hề hay biết, được x…

```text
Wide 16:9 landscape cinematic frame. a gentle ninja silhouette on a cliff, an eye glowing with a unique pattern, soft light around a village below. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Obito cho thấy mặt tối của Sharingan: một người từng muốn trở thành Hokage, nhưng mất mát đã đẩy anh vào con…

```text
Wide 16:9 landscape cinematic frame. a masked figure standing in front of a swirling vortex, a broken goggle lying on the ground. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: cùng một đôi mắt, nhưng mỗi người dùng nó theo cách phản ánh con người họ. Lại là quy luật sức…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at six small portraits pinned on a wall. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Sharingan so với các đôi mắt khác

Lời: Sharingan không phải đôi mắt đặc biệt duy nhất. Trong Naruto còn có những huyết kế giới hạn liên quan tới mắt…

```text
Wide 16:9 landscape cinematic frame. two eye symbols side by side: a red eye with comma marks and a pale white eye with visible veins. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Byakugan của gia tộc Hyuga cho tầm nhìn gần như ba trăm sáu mươi độ, nhìn xuyên vật cản, và thấy rõ hệ thống…

```text
Wide 16:9 landscape cinematic frame. a pale-eyed ninja seeing through walls, a glowing network of chakra points visible inside a target. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nếu Sharingan là đôi mắt của sao chép và ảo thuật, thì Byakugan là đôi mắt của nhìn thấu và đánh chính xác và…

```text
Wide 16:9 landscape cinematic frame. a split image: a red eye copying a hand seal, a pale eye targeting glowing points on a body. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Điểm khác lớn: Byakugan không có bậc thang tiến hóa đau đớn như Sharingan. Nó ổn định hơn, nhưng cũng ít biến…

```text
Wide 16:9 landscape cinematic frame. a flat stable line next to a dramatic staircase, both glowing. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Sự khác biệt này phản ánh hai gia tộc: một bên bị cuốn vào cảm xúc mãnh liệt, một bên đề cao truyền thống và…

```text
Wide 16:9 landscape cinematic frame. two family crests on banners, one red fan, one pale symbol, fluttering in wind. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Nấc cuối: Rinnegan

Lời: Ở đỉnh bậc thang tiến hóa là Rinnegan, con mắt được xem là huyền thoại, gắn với vị tổ của thế giới ninja.

```text
Wide 16:9 landscape cinematic frame. a pale purple eye with concentric rings glowing softly against a starry background. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Theo truyện, Rinnegan thức tỉnh khi Sharingan kết hợp với sức mạnh của gia tộc Senju, hai dòng máu vốn cùng m…

```text
Wide 16:9 landscape cinematic frame. two ancient energies, one red and one green, spiraling together and forming concentric rings. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Người có Rinnegan dùng được nhiều loại năng lực khác nhau: điều khiển lực hút và lực đẩy, và cả những năng lự…

```text
Wide 16:9 landscape cinematic frame. a figure pushing away debris with an invisible force while pulling another object toward them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Ở giai đoạn cuối cuộc chiến, còn xuất hiện một dạng Rinnegan có cả dấu phẩy của Sharingan, với sức mạnh ở tầm…

```text
Wide 16:9 landscape cinematic frame. a glowing eye symbol with concentric rings floating above a moonlit battlefield. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: ở nấc này, truyện chuyển từ chuyện gia tộc sang chuyện nguồn gốc của cả thế giới. Đôi mắt trở t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small key shaped like a ringed eye in front of an ancient door. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Những hiểu lầm về Sharingan

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về Sharingan.

```text
Wide 16:9 landscape cinematic frame. a notice board with four pinned cards with red question marks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hiểu lầm một: Sharingan sao chép được mọi thứ. Nó không sao chép được huyết kế giới hạn, và người dùng vẫn cầ…

```text
Wide 16:9 landscape cinematic frame. a copy diagram with a large red cross over a unique bloodline icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hiểu lầm hai: Uchiha nào cũng có Mangekyo. Thực tế rất ít người đạt được nó, vì nó đòi hỏi một nỗi đau mà khô…

```text
Wide 16:9 landscape cinematic frame. a crowd of silhouettes with ordinary red eyes and only one with a pinwheel pattern. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Hiểu lầm ba: Sharingan là thứ mạnh nhất trong Naruto. Nhiều nhân vật không có nó vẫn đứng ở hàng mạnh nhất nh…

```text
Wide 16:9 landscape cinematic frame. a ninja with no special eyes standing confidently with swirling orange energy around him. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Hiểu lầm bốn: cấy mắt là cách dễ để mạnh lên. Người không hợp dòng máu bị tiêu hao chakra nặng, và việc cấy g…

```text
Wide 16:9 landscape cinematic frame. a tired ninja clutching a covered eye, surrounded by shadows. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Trắc nghiệm: nếu bạn sinh ra trong gia tộc Uchiha

Lời: Giờ một trò vui: nếu bạn sinh ra trong gia tộc Uchiha, bạn sẽ đi tới nấc nào? Đây chỉ là trò chơi thôi nhé.

```text
Wide 16:9 landscape cinematic frame. a quiz card with a staircase of eye symbols and a small figure at the bottom. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nếu bạn sống bình yên và may mắn không mất ai, có lẽ bạn sẽ dừng ở một đến ba dấu phẩy. Và thành thật mà nói,…

```text
Wide 16:9 landscape cinematic frame. a peaceful figure with a gentle red glow in their eyes sitting under a cherry tree. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn trải qua mất mát lớn, Mangekyo có thể thức tỉnh. Nhưng bạn sẽ phải chọn: dùng nó và mất dần ánh sáng,…

```text
Wide 16:9 landscape cinematic frame. a figure standing at a fork between a dark path and a gentle path, eyes glowing with a new pattern. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và nếu bạn bị cuốn vào vòng thù hận, bạn có thể leo cao hơn nữa. Nhưng như truyện đã cho thấy, mỗi bậc thang…

```text
Wide 16:9 landscape cinematic frame. a figure climbing a staircase into darkness, leaving pieces of light behind on each step. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn ở lại nấc đầu, uống trà và đọc sách. Còn bạn thì sao?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sipping tea with a small red glint in its glasses, smiling. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Nhìn lại bậc thang

Lời: Trước khi đi tiếp, hãy nhìn lại toàn bộ bậc thang một lượt, như một bảng tóm tắt nhanh.

```text
Wide 16:9 landscape cinematic frame. a vertical infographic of five glowing eye stages from bottom to top on a dark scroll. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Nấc một, một đến ba dấu phẩy: đổi bằng một khoảnh khắc cảm xúc mạnh. Đây là nấc duy nhất mà cái giá vẫn còn n…

```text
Wide 16:9 landscape cinematic frame. the bottom step glowing softly with a single comma-marked eye and a small heart icon. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Nấc hai, Mangekyo: đổi bằng mất mát người thân và ánh sáng của chính đôi mắt mình.

```text
Wide 16:9 landscape cinematic frame. the second step with a pinwheel eye and a cracked heart icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Nấc ba, Mangekyo vĩnh hằng: đổi bằng đôi mắt của anh em ruột, cái giá mà nhiều người không bao giờ tha thứ ch…

```text
Wide 16:9 landscape cinematic frame. the third step with a merged eye pattern and two linked silhouettes fading. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Nấc cuối, Rinnegan: đổi bằng sự hòa trộn hai dòng máu cổ xưa, thường đi kèm những biến cố làm rung chuyển cả…

```text
Wide 16:9 landscape cinematic frame. the top step glowing purple with concentric rings above a trembling world map. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Nhìn như vậy, bạn sẽ thấy Sharingan không phải món quà, mà là một khoản vay. Và thế giới ninja luôn bắt người…

```text
Wide 16:9 landscape cinematic frame. a ledger book with red entries, a quill resting on the open page. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Góc nhìn của Kaku: lời nguyền của thù hận · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn toàn bộ bậc thang, ta thấy một điều đáng sợ: mỗi nấc sức mạnh đều được mua bằng mất mát.

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at the bottom of a red staircase lined with fading lanterns. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Truyện gọi đây là lời nguyền của thù hận. Tình yêu sâu sắc biến thành nỗi đau, nỗi đau biến thành sức mạnh, v…

```text
Wide 16:9 landscape cinematic frame. a circular diagram with three arrows: a heart, a broken heart, and a glowing eye, looping endlessly. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Đó là lý do nhiều thế hệ Uchiha rơi vào bi kịch. Gia tộc mạnh nhất cũng là gia tộc chịu nhiều mất mát nhất.

```text
Wide 16:9 landscape cinematic frame. a quiet abandoned compound with fan emblems fading on the walls under a grey sky. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Nhưng truyện cũng cho thấy lối thoát: những nhân vật chọn tin tưởng và tha thứ thay vì thù hận đã phá được vò…

```text
Wide 16:9 landscape cinematic frame. two hands reaching out to each other across a broken bridge at sunrise. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: So với Nen hay hơi thở trong Kimetsu mà mình từng giải thích, Sharingan là hệ thống gắn chặt nhất với cảm xúc…

```text
Wide 16:9 landscape cinematic frame. three symbols side by side: a hexagon, a pair of lungs, and a red eye, each glowing. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · Tóm tắt

Lời: Tóm lại: Sharingan thức tỉnh từ cảm xúc mạnh, tăng từ một tới ba dấu phẩy, giúp nhìn chakra, đọc chuyển động,…

```text
Wide 16:9 landscape cinematic frame. a summary ladder of eye symbols from one comma to three. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Mangekyo đến từ mất mát lớn, cho năng lực riêng nhưng làm mù dần. Mangekyo vĩnh hằng đổi bằng đôi mắt của ngư…

```text
Wide 16:9 landscape cinematic frame. two eye patterns merging above a small price tag. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92

Lời: Và ở đỉnh là Rinnegan, con mắt nối Sharingan với nguồn gốc của thế giới ninja.

```text
Wide 16:9 landscape cinematic frame. a ringed purple eye at the top of the staircase glowing softly. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có Mangekyo, bạn muốn năng lực gì, và bạn có chấp nhận cái giá đi kèm không? Viết xuống…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a red lantern and a small scale, thinking. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã luật ác quỷ và nỗi sợ trong Chainsaw Man.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a shadowy figure with a chainsaw motif made of abstract shapes. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye under a moonlit sky. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nền tảng: chakra và nhẫn thuật

Khoảng 117 giây · cảnh s01–s12 · 1517 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Naruto và Naruto Shippuden đến hết cuộc Đại chiến Ninja lần thứ tư. Nếu chưa xem hết, hãy lưu video lại nhé.

<short pause> Trong Naruto, có một đôi mắt được cả thế giới ninja vừa thèm muốn vừa sợ hãi. Nó sao chép được nhẫn thuật, nhìn thấu chuyển động, và giam người khác trong ảo ảnh.

<short pause> Nhưng đôi mắt ấy có một bí mật đau đớn: nó càng mạnh khi chủ nhân càng đau khổ.

<short pause> Đó là Sharingan. Và hôm nay mình sẽ đi theo từng nấc tiến hóa của nó, từ một dấu phẩy nhỏ tới con mắt của thần.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ sẽ vẽ một bậc thang tiến hóa: mỗi nấc có sức mạnh gì, và phải trả cái giá gì.

<short pause> Xem hết video, bạn sẽ hiểu vì sao lịch sử của đôi mắt này cũng là lịch sử của thù hận trong thế giới ninja.

<short pause> Trước khi leo bậc thang, cần hiểu nền tảng của thế giới Naruto: chakra, năng lượng mà mọi ninja dùng để thực hiện nhẫn thuật.

<short pause> Chakra được tạo ra từ hai phần: năng lượng thể chất trong từng tế bào và năng lượng tinh thần từ sự rèn luyện. Hai phần hòa vào nhau thành chakra.

<short pause> Ninja dùng chakra theo ba nhóm chính: nhẫn thuật như cầu lửa hay phân thân, ảo thuật đánh lừa giác quan, và thể thuật dùng cơ thể chiến đấu.

<short pause> Hầu hết nhẫn thuật cần kết ấn tay để điều khiển chakra. Người càng giỏi, kết ấn càng nhanh, có người rút gọn tới mức gần như không cần ấn.

<short pause> Sharingan đặc biệt vì nó can thiệp vào cả ba nhóm: nhìn thấu nhẫn thuật, tạo và phá ảo thuật, và đọc trước thể thuật.

<short pause> Kaku ghi chú: đó là lý do một đôi mắt lại có thể thay đổi cục diện trận đấu. Nó không thêm một chiêu mới, mà nâng mọi chiêu lên một tầm.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Naruto và Naruto Shippuden đến hết cuộc Đại chiến Ninja lần thứ tư. Nếu chưa xem hết, hãy lưu video lại nhé.

[pause] Trong Naruto, có một đôi mắt được cả thế giới ninja vừa thèm muốn vừa sợ hãi. Nó sao chép được nhẫn thuật, nhìn thấu chuyển động, và giam người khác trong ảo ảnh.

[pause] Nhưng đôi mắt ấy có một bí mật đau đớn: nó càng mạnh khi chủ nhân càng đau khổ.

[pause] Đó là Sharingan. Và hôm nay mình sẽ đi theo từng nấc tiến hóa của nó, từ một dấu phẩy nhỏ tới con mắt của thần.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ sẽ vẽ một bậc thang tiến hóa: mỗi nấc có sức mạnh gì, và phải trả cái giá gì.

[pause] Xem hết video, bạn sẽ hiểu vì sao lịch sử của đôi mắt này cũng là lịch sử của thù hận trong thế giới ninja.

[pause] Trước khi leo bậc thang, cần hiểu nền tảng của thế giới Naruto: chakra, năng lượng mà mọi ninja dùng để thực hiện nhẫn thuật.

[pause] Chakra được tạo ra từ hai phần: năng lượng thể chất trong từng tế bào và năng lượng tinh thần từ sự rèn luyện. Hai phần hòa vào nhau thành chakra.

[pause] Ninja dùng chakra theo ba nhóm chính: nhẫn thuật như cầu lửa hay phân thân, ảo thuật đánh lừa giác quan, và thể thuật dùng cơ thể chiến đấu.

[pause] Hầu hết nhẫn thuật cần kết ấn tay để điều khiển chakra. Người càng giỏi, kết ấn càng nhanh, có người rút gọn tới mức gần như không cần ấn.

[pause] Sharingan đặc biệt vì nó can thiệp vào cả ba nhóm: nhìn thấu nhẫn thuật, tạo và phá ảo thuật, và đọc trước thể thuật.

[pause] Kaku ghi chú: đó là lý do một đôi mắt lại có thể thay đổi cục diện trận đấu. Nó không thêm một chiêu mới, mà nâng mọi chiêu lên một tầm.
```

### c02 · Nấc 0: đôi mắt của một gia tộc / Nấc 1: Sharingan một, hai, ba dấu phẩy

Khoảng 122 giây · cảnh s13–s25 · 1588 ký tự

**Gemini**

```text
Sharingan là huyết kế giới hạn, một năng lực di truyền, chỉ xuất hiện ở gia tộc Uchiha. Người ngoài gia tộc không thể tự thức tỉnh nó.

<short pause> Nhưng không phải thành viên Uchiha nào cũng có. Sharingan chỉ thức tỉnh khi người đó trải qua cảm xúc cực mạnh, thường là trong nguy hiểm hoặc mất mát.

<short pause> Truyện giải thích rằng Uchiha là gia tộc có tình yêu rất sâu. Khi tình yêu đó bị tổn thương, nó biến thành nỗi đau, và nỗi đau đánh thức đôi mắt.

<short pause> Đây là nền tảng của mọi thứ phía sau: Sharingan không chỉ là năng lực, mà là tấm gương phản chiếu trái tim của người sở hữu.

<short pause> <laugh> Kaku ghi chú: hãy nhớ quy luật này nhé. Ở mỗi nấc tiếp theo, cái giá luôn lớn hơn nấc trước.

<short pause> Khi mới thức tỉnh, Sharingan thường có một dấu phẩy quanh con ngươi. Dấu phẩy này được gọi là tomoe.

<short pause> Theo thời gian và kinh nghiệm chiến đấu, số tomoe tăng lên hai, rồi ba. Mỗi dấu phẩy thêm vào là khả năng nhìn rõ hơn, nhanh hơn.

<short pause> Năng lực thứ nhất: nhìn thấy dòng chakra. Người dùng phân biệt được nhẫn thuật thật và ảo ảnh, thấy được chakra đang dồn về đâu.

<short pause> Năng lực thứ hai: đọc chuyển động. Sharingan thấy đòn đánh tới trước khi nó chạm, giúp né và phản công gần như hoàn hảo.

<short pause> Năng lực thứ ba, nổi tiếng nhất: sao chép. Người dùng nhìn một nhẫn thuật và có thể học lại nó, miễn là cơ thể đủ khả năng thực hiện.

<short pause> Tuy nhiên, Sharingan không sao chép được huyết kế giới hạn của gia tộc khác, vì đó là năng lực gắn với cơ thể chứ không phải kỹ thuật.

<short pause> Năng lực thứ tư: ảo thuật. Chỉ cần đối thủ nhìn vào mắt, người dùng có thể kéo họ vào ảo ảnh.

<short pause> Kaku tóm lại: nấc một là đôi mắt của một thiên tài chiến đấu. Nhìn thấu, đọc trước, sao chép và đánh lừa.
```

**ElevenLabs**

```text
Sharingan là huyết kế giới hạn, một năng lực di truyền, chỉ xuất hiện ở gia tộc Uchiha. Người ngoài gia tộc không thể tự thức tỉnh nó.

[pause] Nhưng không phải thành viên Uchiha nào cũng có. Sharingan chỉ thức tỉnh khi người đó trải qua cảm xúc cực mạnh, thường là trong nguy hiểm hoặc mất mát.

[pause] Truyện giải thích rằng Uchiha là gia tộc có tình yêu rất sâu. Khi tình yêu đó bị tổn thương, nó biến thành nỗi đau, và nỗi đau đánh thức đôi mắt.

[pause] Đây là nền tảng của mọi thứ phía sau: Sharingan không chỉ là năng lực, mà là tấm gương phản chiếu trái tim của người sở hữu.

[pause] [chuckles] Kaku ghi chú: hãy nhớ quy luật này nhé. Ở mỗi nấc tiếp theo, cái giá luôn lớn hơn nấc trước.

[pause] Khi mới thức tỉnh, Sharingan thường có một dấu phẩy quanh con ngươi. Dấu phẩy này được gọi là tomoe.

[pause] Theo thời gian và kinh nghiệm chiến đấu, số tomoe tăng lên hai, rồi ba. Mỗi dấu phẩy thêm vào là khả năng nhìn rõ hơn, nhanh hơn.

[pause] Năng lực thứ nhất: nhìn thấy dòng chakra. Người dùng phân biệt được nhẫn thuật thật và ảo ảnh, thấy được chakra đang dồn về đâu.

[pause] Năng lực thứ hai: đọc chuyển động. Sharingan thấy đòn đánh tới trước khi nó chạm, giúp né và phản công gần như hoàn hảo.

[pause] Năng lực thứ ba, nổi tiếng nhất: sao chép. Người dùng nhìn một nhẫn thuật và có thể học lại nó, miễn là cơ thể đủ khả năng thực hiện.

[pause] Tuy nhiên, Sharingan không sao chép được huyết kế giới hạn của gia tộc khác, vì đó là năng lực gắn với cơ thể chứ không phải kỹ thuật.

[pause] Năng lực thứ tư: ảo thuật. Chỉ cần đối thủ nhìn vào mắt, người dùng có thể kéo họ vào ảo ảnh.

[pause] Kaku tóm lại: nấc một là đôi mắt của một thiên tài chiến đấu. Nhìn thấu, đọc trước, sao chép và đánh lừa.
```

### c03 · Người ngoài dùng Sharingan: trường hợp Kakashi / Nấc 2: Mangekyo Sharingan / Cái giá của Mangekyo

Khoảng 145 giây · cảnh s26–s41 · 1879 ký tự

**Gemini**

```text
Có một ngoại lệ nổi tiếng: Kakashi, không phải Uchiha nhưng có một mắt Sharingan được cấy ghép từ người bạn thân Obito.

<short pause> Vì không mang dòng máu Uchiha, cơ thể Kakashi không hợp với Sharingan. Anh không thể tắt nó, nên phải che mắt bằng băng trán.

<short pause> Mỗi lần dùng, Sharingan tiêu hao chakra của anh rất nhanh. Dùng quá sức, anh có thể ngã quỵ sau trận đấu.

<short pause> Dù vậy, Kakashi vẫn được gọi là Ninja Sao Chép, với hàng nghìn nhẫn thuật đã học được. Đây là minh chứng cho việc nỗ lực có thể bù đắp dòng máu.

<short pause> Nấc tiến hóa thứ hai là Mangekyo Sharingan, và cái giá để có nó khủng khiếp hơn nhiều.

<short pause> Theo truyện, Mangekyo thức tỉnh khi người dùng trải qua nỗi đau cực độ, thường là mất đi người thân yêu nhất, có khi là chính tay mình gây ra.

<short pause> Mỗi Mangekyo có hoa văn riêng, và mỗi người nhận được những năng lực riêng. Không có hai Mangekyo nào giống hệt nhau.

<short pause> Có năng lực tạo ra ảo thuật thời gian, nơi vài giây ngoài đời bằng nhiều ngày tra tấn trong ảo ảnh.

<short pause> Có năng lực tạo ra ngọn lửa đen không thể dập tắt, đốt cháy mọi thứ mà người dùng nhìn vào.

<short pause> Có năng lực dịch chuyển đồ vật hoặc chính mình sang một không gian khác, khiến đòn đánh xuyên qua người dùng như không có gì.

<short pause> Và khi thức tỉnh Mangekyo ở cả hai mắt, người dùng có thể gọi ra một chiến binh khổng lồ bằng chakra bao quanh cơ thể, vừa là khiên vừa là vũ khí.

<short pause> <laugh> Kaku ghi chú: đây là lúc Sharingan đi từ đôi mắt của thiên tài thành vũ khí có thể thay đổi cả một cuộc chiến.

<short pause> Nhưng Mangekyo có một cái giá tàn nhẫn: mỗi lần sử dụng, thị lực người dùng giảm dần. Dùng càng nhiều, càng tiến gần tới mù lòa.

<short pause> Những năng lực mạnh nhất còn khiến mắt chảy máu, cơ thể kiệt quệ ngay sau khi dùng.

<short pause> Điều này tạo ra một bi kịch: đôi mắt được sinh ra từ nỗi đau mất người thân, rồi lại lấy đi ánh sáng của chính người sở hữu.

<short pause> Và nó giải thích vì sao trong truyện, những người có Mangekyo luôn tìm cách vượt qua giới hạn đó, dù cái giá tiếp theo còn đen tối hơn.
```

**ElevenLabs**

```text
Có một ngoại lệ nổi tiếng: Kakashi, không phải Uchiha nhưng có một mắt Sharingan được cấy ghép từ người bạn thân Obito.

[pause] Vì không mang dòng máu Uchiha, cơ thể Kakashi không hợp với Sharingan. Anh không thể tắt nó, nên phải che mắt bằng băng trán.

[pause] Mỗi lần dùng, Sharingan tiêu hao chakra của anh rất nhanh. Dùng quá sức, anh có thể ngã quỵ sau trận đấu.

[pause] Dù vậy, Kakashi vẫn được gọi là Ninja Sao Chép, với hàng nghìn nhẫn thuật đã học được. Đây là minh chứng cho việc nỗ lực có thể bù đắp dòng máu.

[pause] Nấc tiến hóa thứ hai là Mangekyo Sharingan, và cái giá để có nó khủng khiếp hơn nhiều.

[pause] Theo truyện, Mangekyo thức tỉnh khi người dùng trải qua nỗi đau cực độ, thường là mất đi người thân yêu nhất, có khi là chính tay mình gây ra.

[pause] Mỗi Mangekyo có hoa văn riêng, và mỗi người nhận được những năng lực riêng. Không có hai Mangekyo nào giống hệt nhau.

[pause] Có năng lực tạo ra ảo thuật thời gian, nơi vài giây ngoài đời bằng nhiều ngày tra tấn trong ảo ảnh.

[pause] Có năng lực tạo ra ngọn lửa đen không thể dập tắt, đốt cháy mọi thứ mà người dùng nhìn vào.

[pause] Có năng lực dịch chuyển đồ vật hoặc chính mình sang một không gian khác, khiến đòn đánh xuyên qua người dùng như không có gì.

[pause] Và khi thức tỉnh Mangekyo ở cả hai mắt, người dùng có thể gọi ra một chiến binh khổng lồ bằng chakra bao quanh cơ thể, vừa là khiên vừa là vũ khí.

[pause] [chuckles] Kaku ghi chú: đây là lúc Sharingan đi từ đôi mắt của thiên tài thành vũ khí có thể thay đổi cả một cuộc chiến.

[pause] Nhưng Mangekyo có một cái giá tàn nhẫn: mỗi lần sử dụng, thị lực người dùng giảm dần. Dùng càng nhiều, càng tiến gần tới mù lòa.

[pause] Những năng lực mạnh nhất còn khiến mắt chảy máu, cơ thể kiệt quệ ngay sau khi dùng.

[pause] Điều này tạo ra một bi kịch: đôi mắt được sinh ra từ nỗi đau mất người thân, rồi lại lấy đi ánh sáng của chính người sở hữu.

[pause] Và nó giải thích vì sao trong truyện, những người có Mangekyo luôn tìm cách vượt qua giới hạn đó, dù cái giá tiếp theo còn đen tối hơn.
```

### c04 · Nấc 3: Mangekyo vĩnh hằng / Những thuật cấm: Izanagi và Izanami

Khoảng 91 giây · cảnh s42–s51 · 1182 ký tự

**Gemini**

```text
Cách để thoát khỏi mù lòa là nấc thứ ba: Mangekyo vĩnh hằng. Và cách đạt được nó khiến người ta rùng mình.

<short pause> Người dùng phải cấy ghép đôi mắt Mangekyo của một người ruột thịt, thường là anh em. Hai hoa văn hòa vào nhau thành một hoa văn mới.

<short pause> Kết quả: người dùng không còn bị mù dần nữa, và sức mạnh của Mangekyo tăng lên rõ rệt.

<short pause> Trong lịch sử truyện, chỉ vài người đạt được nấc này, và mỗi lần đều gắn với một câu chuyện anh em đầy đau đớn.

<short pause> <laugh> Kaku ghi chú: đến đây, bạn có thể thấy quy luật: mỗi nấc tiến hóa đều được trả bằng thứ quý giá hơn. Mắt của mình, rồi mắt của người thân.

<short pause> Bên cạnh các nấc tiến hóa, Sharingan còn có những thuật cấm, mạnh đến mức gia tộc Uchiha phải hạn chế sử dụng.

<short pause> Izanagi cho phép người dùng viết lại thực tại trong một thời gian ngắn: những gì bất lợi xảy ra với họ có thể biến thành như chưa từng xảy ra.

<short pause> Cái giá: con mắt dùng Izanagi sẽ vĩnh viễn mất ánh sáng. Một con mắt đổi lấy vài giây như một vị thần.

<short pause> Izanami được tạo ra như thuật để chấm dứt Izanagi: nó giam đối thủ trong một vòng lặp cho tới khi họ chấp nhận sự thật về bản thân.

<short pause> Hai thuật này cho thấy một ý tưởng sâu sắc của truyện: sức mạnh lớn nhất không phải trốn tránh thực tại, mà là chấp nhận nó.
```

**ElevenLabs**

```text
Cách để thoát khỏi mù lòa là nấc thứ ba: Mangekyo vĩnh hằng. Và cách đạt được nó khiến người ta rùng mình.

[pause] Người dùng phải cấy ghép đôi mắt Mangekyo của một người ruột thịt, thường là anh em. Hai hoa văn hòa vào nhau thành một hoa văn mới.

[pause] Kết quả: người dùng không còn bị mù dần nữa, và sức mạnh của Mangekyo tăng lên rõ rệt.

[pause] Trong lịch sử truyện, chỉ vài người đạt được nấc này, và mỗi lần đều gắn với một câu chuyện anh em đầy đau đớn.

[pause] [chuckles] Kaku ghi chú: đến đây, bạn có thể thấy quy luật: mỗi nấc tiến hóa đều được trả bằng thứ quý giá hơn. Mắt của mình, rồi mắt của người thân.

[pause] Bên cạnh các nấc tiến hóa, Sharingan còn có những thuật cấm, mạnh đến mức gia tộc Uchiha phải hạn chế sử dụng.

[pause] Izanagi cho phép người dùng viết lại thực tại trong một thời gian ngắn: những gì bất lợi xảy ra với họ có thể biến thành như chưa từng xảy ra.

[pause] Cái giá: con mắt dùng Izanagi sẽ vĩnh viễn mất ánh sáng. Một con mắt đổi lấy vài giây như một vị thần.

[pause] Izanami được tạo ra như thuật để chấm dứt Izanagi: nó giam đối thủ trong một vòng lặp cho tới khi họ chấp nhận sự thật về bản thân.

[pause] Hai thuật này cho thấy một ý tưởng sâu sắc của truyện: sức mạnh lớn nhất không phải trốn tránh thực tại, mà là chấp nhận nó.
```

### c05 · Những người sở hữu tiêu biểu / Sharingan so với các đôi mắt khác

Khoảng 127 giây · cảnh s52–s63 · 1647 ký tự

**Gemini**

```text
Mỗi nấc tiến hóa gắn với những nhân vật cụ thể. Hãy điểm qua vài người để thấy mỗi người dùng Sharingan theo một cách rất riêng.

<short pause> Itachi được biết đến với ảo thuật cực mạnh và tài năng từ nhỏ. Anh dùng Sharingan không để phô diễn mà để kết thúc trận đấu nhanh nhất có thể.

<short pause> Sasuke là người đi hết gần như toàn bộ bậc thang: từ một dấu phẩy, tới Mangekyo, Mangekyo vĩnh hằng, rồi Rinnegan. Hành trình của anh cũng là hành trình của thù hận và chuộc lỗi.

<short pause> Madara là huyền thoại của gia tộc, người đầu tiên đạt Mangekyo vĩnh hằng được biết đến và sau này là Rinnegan. Sức mạnh của ông định hình cả lịch sử làng Lá.

<short pause> Shisui được nhắc tới với một ảo thuật có thể thay đổi suy nghĩ của người khác mà họ không hề hay biết, được xem là một trong những ảo thuật mạnh nhất.

<short pause> Obito cho thấy mặt tối của Sharingan: một người từng muốn trở thành Hokage, nhưng mất mát đã đẩy anh vào con đường khác hẳn.

<short pause> <laugh> Kaku nhận xét: cùng một đôi mắt, nhưng mỗi người dùng nó theo cách phản ánh con người họ. Lại là quy luật sức mạnh gắn với tính cách.

<short pause> Sharingan không phải đôi mắt đặc biệt duy nhất. Trong Naruto còn có những huyết kế giới hạn liên quan tới mắt khác, nổi bật nhất là Byakugan.

<short pause> Byakugan của gia tộc Hyuga cho tầm nhìn gần như ba trăm sáu mươi độ, nhìn xuyên vật cản, và thấy rõ hệ thống kinh mạch chakra trong cơ thể.

<short pause> Nếu Sharingan là đôi mắt của sao chép và ảo thuật, thì Byakugan là đôi mắt của nhìn thấu và đánh chính xác vào điểm yếu.

<short pause> Điểm khác lớn: Byakugan không có bậc thang tiến hóa đau đớn như Sharingan. Nó ổn định hơn, nhưng cũng ít biến đổi hơn.

<short pause> Sự khác biệt này phản ánh hai gia tộc: một bên bị cuốn vào cảm xúc mãnh liệt, một bên đề cao truyền thống và kỷ luật.
```

**ElevenLabs**

```text
Mỗi nấc tiến hóa gắn với những nhân vật cụ thể. Hãy điểm qua vài người để thấy mỗi người dùng Sharingan theo một cách rất riêng.

[pause] Itachi được biết đến với ảo thuật cực mạnh và tài năng từ nhỏ. Anh dùng Sharingan không để phô diễn mà để kết thúc trận đấu nhanh nhất có thể.

[pause] Sasuke là người đi hết gần như toàn bộ bậc thang: từ một dấu phẩy, tới Mangekyo, Mangekyo vĩnh hằng, rồi Rinnegan. Hành trình của anh cũng là hành trình của thù hận và chuộc lỗi.

[pause] Madara là huyền thoại của gia tộc, người đầu tiên đạt Mangekyo vĩnh hằng được biết đến và sau này là Rinnegan. Sức mạnh của ông định hình cả lịch sử làng Lá.

[pause] Shisui được nhắc tới với một ảo thuật có thể thay đổi suy nghĩ của người khác mà họ không hề hay biết, được xem là một trong những ảo thuật mạnh nhất.

[pause] Obito cho thấy mặt tối của Sharingan: một người từng muốn trở thành Hokage, nhưng mất mát đã đẩy anh vào con đường khác hẳn.

[pause] [chuckles] Kaku nhận xét: cùng một đôi mắt, nhưng mỗi người dùng nó theo cách phản ánh con người họ. Lại là quy luật sức mạnh gắn với tính cách.

[pause] Sharingan không phải đôi mắt đặc biệt duy nhất. Trong Naruto còn có những huyết kế giới hạn liên quan tới mắt khác, nổi bật nhất là Byakugan.

[pause] Byakugan của gia tộc Hyuga cho tầm nhìn gần như ba trăm sáu mươi độ, nhìn xuyên vật cản, và thấy rõ hệ thống kinh mạch chakra trong cơ thể.

[pause] Nếu Sharingan là đôi mắt của sao chép và ảo thuật, thì Byakugan là đôi mắt của nhìn thấu và đánh chính xác vào điểm yếu.

[pause] Điểm khác lớn: Byakugan không có bậc thang tiến hóa đau đớn như Sharingan. Nó ổn định hơn, nhưng cũng ít biến đổi hơn.

[pause] Sự khác biệt này phản ánh hai gia tộc: một bên bị cuốn vào cảm xúc mãnh liệt, một bên đề cao truyền thống và kỷ luật.
```

### c06 · Nấc cuối: Rinnegan / Những hiểu lầm về Sharingan / Trắc nghiệm: nếu bạn sinh ra trong gia tộc Uchiha

Khoảng 142 giây · cảnh s64–s78 · 1847 ký tự

**Gemini**

```text
Ở đỉnh bậc thang tiến hóa là Rinnegan, con mắt được xem là huyền thoại, gắn với vị tổ của thế giới ninja.

<short pause> Theo truyện, Rinnegan thức tỉnh khi Sharingan kết hợp với sức mạnh của gia tộc Senju, hai dòng máu vốn cùng một nguồn gốc xa xưa.

<short pause> Người có Rinnegan dùng được nhiều loại năng lực khác nhau: điều khiển lực hút và lực đẩy, và cả những năng lực liên quan đến sự sống và cái chết.

<short pause> Ở giai đoạn cuối cuộc chiến, còn xuất hiện một dạng Rinnegan có cả dấu phẩy của Sharingan, với sức mạnh ở tầm thần thoại.

<short pause> <laugh> Kaku ghi chú: ở nấc này, truyện chuyển từ chuyện gia tộc sang chuyện nguồn gốc của cả thế giới. Đôi mắt trở thành chìa khóa của lịch sử.

<short pause> Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về Sharingan.

<short pause> Hiểu lầm một: Sharingan sao chép được mọi thứ. Nó không sao chép được huyết kế giới hạn, và người dùng vẫn cần đủ chakra và thể lực để làm lại nhẫn thuật.

<short pause> Hiểu lầm hai: Uchiha nào cũng có Mangekyo. Thực tế rất ít người đạt được nó, vì nó đòi hỏi một nỗi đau mà không ai muốn trải qua.

<short pause> Hiểu lầm ba: Sharingan là thứ mạnh nhất trong Naruto. Nhiều nhân vật không có nó vẫn đứng ở hàng mạnh nhất nhờ chakra, kỹ năng và ý chí.

<short pause> Hiểu lầm bốn: cấy mắt là cách dễ để mạnh lên. Người không hợp dòng máu bị tiêu hao chakra nặng, và việc cấy ghép luôn kèm theo những câu chuyện đau lòng.

<short pause> Giờ một trò vui: nếu bạn sinh ra trong gia tộc Uchiha, bạn sẽ đi tới nấc nào? Đây chỉ là trò chơi thôi nhé.

<short pause> Nếu bạn sống bình yên và may mắn không mất ai, có lẽ bạn sẽ dừng ở một đến ba dấu phẩy. Và thành thật mà nói, đó là cái kết hạnh phúc nhất.

<short pause> Nếu bạn trải qua mất mát lớn, Mangekyo có thể thức tỉnh. <short pause> Nhưng bạn sẽ phải chọn: dùng nó và mất dần ánh sáng, hay cất nó đi.

<short pause> Và nếu bạn bị cuốn vào vòng thù hận, bạn có thể leo cao hơn nữa. <short pause> Nhưng như truyện đã cho thấy, mỗi bậc thang đó đều trả bằng một phần trái tim.

<short pause> Kaku chọn ở lại nấc đầu, uống trà và đọc sách. Còn bạn thì sao?
```

**ElevenLabs**

```text
Ở đỉnh bậc thang tiến hóa là Rinnegan, con mắt được xem là huyền thoại, gắn với vị tổ của thế giới ninja.

[pause] Theo truyện, Rinnegan thức tỉnh khi Sharingan kết hợp với sức mạnh của gia tộc Senju, hai dòng máu vốn cùng một nguồn gốc xa xưa.

[pause] Người có Rinnegan dùng được nhiều loại năng lực khác nhau: điều khiển lực hút và lực đẩy, và cả những năng lực liên quan đến sự sống và cái chết.

[pause] Ở giai đoạn cuối cuộc chiến, còn xuất hiện một dạng Rinnegan có cả dấu phẩy của Sharingan, với sức mạnh ở tầm thần thoại.

[pause] [chuckles] Kaku ghi chú: ở nấc này, truyện chuyển từ chuyện gia tộc sang chuyện nguồn gốc của cả thế giới. Đôi mắt trở thành chìa khóa của lịch sử.

[pause] Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về Sharingan.

[pause] Hiểu lầm một: Sharingan sao chép được mọi thứ. Nó không sao chép được huyết kế giới hạn, và người dùng vẫn cần đủ chakra và thể lực để làm lại nhẫn thuật.

[pause] Hiểu lầm hai: Uchiha nào cũng có Mangekyo. Thực tế rất ít người đạt được nó, vì nó đòi hỏi một nỗi đau mà không ai muốn trải qua.

[pause] Hiểu lầm ba: Sharingan là thứ mạnh nhất trong Naruto. Nhiều nhân vật không có nó vẫn đứng ở hàng mạnh nhất nhờ chakra, kỹ năng và ý chí.

[pause] Hiểu lầm bốn: cấy mắt là cách dễ để mạnh lên. Người không hợp dòng máu bị tiêu hao chakra nặng, và việc cấy ghép luôn kèm theo những câu chuyện đau lòng.

[pause] [curious] Giờ một trò vui: nếu bạn sinh ra trong gia tộc Uchiha, bạn sẽ đi tới nấc nào? Đây chỉ là trò chơi thôi nhé.

[pause] Nếu bạn sống bình yên và may mắn không mất ai, có lẽ bạn sẽ dừng ở một đến ba dấu phẩy. Và thành thật mà nói, đó là cái kết hạnh phúc nhất.

[pause] Nếu bạn trải qua mất mát lớn, Mangekyo có thể thức tỉnh. [pause] Nhưng bạn sẽ phải chọn: dùng nó và mất dần ánh sáng, hay cất nó đi.

[pause] Và nếu bạn bị cuốn vào vòng thù hận, bạn có thể leo cao hơn nữa. [pause] Nhưng như truyện đã cho thấy, mỗi bậc thang đó đều trả bằng một phần trái tim.

[pause] Kaku chọn ở lại nấc đầu, uống trà và đọc sách. Còn bạn thì sao?
```

### c07 · Nhìn lại bậc thang / Góc nhìn của Kaku: lời nguyền của thù hận / Tóm tắt

Khoảng 143 giây · cảnh s79–s95 · 1856 ký tự

**Gemini**

```text
Trước khi đi tiếp, hãy nhìn lại toàn bộ bậc thang một lượt, như một bảng tóm tắt nhanh.

<short pause> Nấc một, một đến ba dấu phẩy: đổi bằng một khoảnh khắc cảm xúc mạnh. Đây là nấc duy nhất mà cái giá vẫn còn nhẹ.

<short pause> Nấc hai, Mangekyo: đổi bằng mất mát người thân và ánh sáng của chính đôi mắt mình.

<short pause> Nấc ba, Mangekyo vĩnh hằng: đổi bằng đôi mắt của anh em ruột, cái giá mà nhiều người không bao giờ tha thứ cho bản thân.

<short pause> Nấc cuối, Rinnegan: đổi bằng sự hòa trộn hai dòng máu cổ xưa, thường đi kèm những biến cố làm rung chuyển cả thế giới.

<short pause> Nhìn như vậy, bạn sẽ thấy Sharingan không phải món quà, mà là một khoản vay. Và thế giới ninja luôn bắt người vay trả lại.

<short pause> Nhìn toàn bộ bậc thang, ta thấy một điều đáng sợ: mỗi nấc sức mạnh đều được mua bằng mất mát.

<short pause> Truyện gọi đây là lời nguyền của thù hận. Tình yêu sâu sắc biến thành nỗi đau, nỗi đau biến thành sức mạnh, và sức mạnh lại gây ra thêm nỗi đau.

<short pause> Đó là lý do nhiều thế hệ Uchiha rơi vào bi kịch. Gia tộc mạnh nhất cũng là gia tộc chịu nhiều mất mát nhất.

<short pause> Nhưng truyện cũng cho thấy lối thoát: những nhân vật chọn tin tưởng và tha thứ thay vì thù hận đã phá được vòng lặp đó.

<short pause> So với Nen hay hơi thở trong Kimetsu mà mình từng giải thích, Sharingan là hệ thống gắn chặt nhất với cảm xúc. Sức mạnh là câu chuyện, và câu chuyện là sức mạnh.

<short pause> Tóm lại: Sharingan thức tỉnh từ cảm xúc mạnh, tăng từ một tới ba dấu phẩy, giúp nhìn chakra, đọc chuyển động, sao chép và tạo ảo thuật.

<short pause> Mangekyo đến từ mất mát lớn, cho năng lực riêng nhưng làm mù dần. Mangekyo vĩnh hằng đổi bằng đôi mắt của người thân.

<short pause> Và ở đỉnh là Rinnegan, con mắt nối Sharingan với nguồn gốc của thế giới ninja.

<short pause> Câu hỏi cho bạn: nếu có Mangekyo, bạn muốn năng lực gì, và bạn có chấp nhận cái giá đi kèm không? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã luật ác quỷ và nỗi sợ trong Chainsaw Man.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi đi tiếp, hãy nhìn lại toàn bộ bậc thang một lượt, như một bảng tóm tắt nhanh.

[pause] Nấc một, một đến ba dấu phẩy: đổi bằng một khoảnh khắc cảm xúc mạnh. Đây là nấc duy nhất mà cái giá vẫn còn nhẹ.

[pause] Nấc hai, Mangekyo: đổi bằng mất mát người thân và ánh sáng của chính đôi mắt mình.

[pause] Nấc ba, Mangekyo vĩnh hằng: đổi bằng đôi mắt của anh em ruột, cái giá mà nhiều người không bao giờ tha thứ cho bản thân.

[pause] Nấc cuối, Rinnegan: đổi bằng sự hòa trộn hai dòng máu cổ xưa, thường đi kèm những biến cố làm rung chuyển cả thế giới.

[pause] Nhìn như vậy, bạn sẽ thấy Sharingan không phải món quà, mà là một khoản vay. Và thế giới ninja luôn bắt người vay trả lại.

[pause] Nhìn toàn bộ bậc thang, ta thấy một điều đáng sợ: mỗi nấc sức mạnh đều được mua bằng mất mát.

[pause] Truyện gọi đây là lời nguyền của thù hận. Tình yêu sâu sắc biến thành nỗi đau, nỗi đau biến thành sức mạnh, và sức mạnh lại gây ra thêm nỗi đau.

[pause] Đó là lý do nhiều thế hệ Uchiha rơi vào bi kịch. Gia tộc mạnh nhất cũng là gia tộc chịu nhiều mất mát nhất.

[pause] Nhưng truyện cũng cho thấy lối thoát: những nhân vật chọn tin tưởng và tha thứ thay vì thù hận đã phá được vòng lặp đó.

[pause] So với Nen hay hơi thở trong Kimetsu mà mình từng giải thích, Sharingan là hệ thống gắn chặt nhất với cảm xúc. Sức mạnh là câu chuyện, và câu chuyện là sức mạnh.

[pause] Tóm lại: Sharingan thức tỉnh từ cảm xúc mạnh, tăng từ một tới ba dấu phẩy, giúp nhìn chakra, đọc chuyển động, sao chép và tạo ảo thuật.

[pause] Mangekyo đến từ mất mát lớn, cho năng lực riêng nhưng làm mù dần. Mangekyo vĩnh hằng đổi bằng đôi mắt của người thân.

[pause] Và ở đỉnh là Rinnegan, con mắt nối Sharingan với nguồn gốc của thế giới ninja.

[pause] [curious] Câu hỏi cho bạn: nếu có Mangekyo, bạn muốn năng lực gì, và bạn có chấp nhận cái giá đi kèm không? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã luật ác quỷ và nỗi sợ trong Chainsaw Man.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
