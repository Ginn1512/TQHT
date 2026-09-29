# Bộ prompt · Hunter x Hunter: Nen hoạt động thế nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 104 ảnh, 9 đoạn đọc, khoảng 15.5 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (104 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Hunter x Hunter đến hết arc Kiến Chimera, và nhắc ngắn một chi tiết ở arc Thừa kế.…

```text
Wide 16:9 landscape cinematic frame. a dark theater stage with a single spotlight on a closed ancient book with a glowing hexagon on its cover. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Có một cậu bé mười bốn tuổi, trong cơn giận, đã biến mình thành một chiến binh trưởng thành mạnh tới mức kẻ t…

```text
Wide 16:9 landscape cinematic frame. silhouette of a tall adult warrior with long wild hair standing in a ruined forest, overwhelming dark orange aura rising like flames, back view. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng cái giá của khoảnh khắc đó là mọi thứ. Sau trận đấu, cậu không còn dùng được, thậm chí không còn nhìn t…

```text
Wide 16:9 landscape cinematic frame. a small boy silhouette sitting alone on a hospital bed by a window at dawn, faint fading aura particles drifting away. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Vì sao lại như vậy? Câu trả lời nằm trong một hệ thống sức mạnh được xem là chặt chẽ bậc nhất anime: Nen.

```text
Wide 16:9 landscape cinematic frame. a glowing golden hexagon diagram floating above an open ancient book in a dark library. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã Nen từ con số không: khí là gì, bốn nguyên tắc, sáu hệ, v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a big glowing notebook on a wooden desk in a cozy library, waving to the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ tự trả lời được vì sao Gon mất Nen, và tự đoán được một nhân vật thuộc hệ nào chỉ qua c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a chalkboard showing a question mark inside a hexagon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Nen là gì?

Lời: Trong Hunter x Hunter, mọi sinh vật sống đều tỏa ra một dòng năng lượng sống, gọi là khí, hay aura.

```text
Wide 16:9 landscape cinematic frame. a calm city street crowd where every person is surrounded by a faint translucent glow, soft watercolor light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Với người thường, khí chỉ rò rỉ ra ngoài một cách vô thức qua các lỗ khí trên cơ thể, rồi tan đi, không để là…

```text
Wide 16:9 landscape cinematic frame. anatomical style anime illustration of a human silhouette with small glowing points across the body leaking thin wisps of light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Nen là kỹ năng kiểm soát dòng khí đó: giữ nó lại, dồn nó đi, và biến nó thành sức mạnh.

```text
Wide 16:9 landscape cinematic frame. a martial artist silhouette in meditation, glowing aura gathering into a controlled sphere around the body. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Tên gọi Nen có nghĩa là niệm, ý niệm. Người dùng được gọi là người dùng Nen, và phần lớn thợ săn chuyên nghiệ…

```text
Wide 16:9 landscape cinematic frame. an old scroll unrolling with an elegant brush-stroke symbol glowing gold, calligraphy style, no readable text. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Có một chi tiết thú vị: lúc đầu, thầy Wing không dạy Gon và Killua Nen thật. Thầy dạy một phiên bản khác, chỉ…

```text
Wide 16:9 landscape cinematic frame. a gentle martial arts teacher silhouette with glasses in a small apartment, two children sitting on the floor listening. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Lý do rất đơn giản: Nen thật nguy hiểm. Mở lỗ khí sai cách, hoặc bị kẻ xấu tấn công bằng khí khi chưa phòng t…

```text
Wide 16:9 landscape cinematic frame. a warning sign made of glowing red aura cracks on a dark wall, ominous atmosphere. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Có hai cách để đánh thức Nen. Cách chậm là thiền định, mở từng lỗ khí một cách tự nhiên. Cách này an toàn như…

```text
Wide 16:9 landscape cinematic frame. a lone student meditating under a waterfall at sunrise, slow gentle glow appearing around the body. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Cách nhanh là để một người đã thành thạo truyền khí vào cơ thể bạn, ép tất cả lỗ khí bật mở cùng lúc.

```text
Wide 16:9 landscape cinematic frame. a teacher's glowing palm near a student's back, a burst of light forcing open glowing points across the body. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Cách này được xem là cấm kỵ, vì người không đủ tố chất có thể kiệt sức hoặc chết. Gon và Killua sống sót, như…

```text
Wide 16:9 landscape cinematic frame. two small silhouettes standing inside a raging vortex of released aura, both holding their ground. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Khí không phải phép thuật từ bên ngoài, mà là sức sống của chính cơ thể. Vì thế người kiệt sức hay bị thương…

```text
Wide 16:9 landscape cinematic frame. a tired traveler silhouette with a dim flickering aura resting against a tree at dusk. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và vì khí gắn với sự sống, bị tấn công bằng khí khi không phòng thủ có thể gây thương tổn nặng hơn nhiều so v…

```text
Wide 16:9 landscape cinematic frame. a glowing strike hitting an unprotected silhouette, shockwave rings, dramatic impact frame. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Nen giống như học bơi. Ai cũng có khí, nhưng chỉ người học mới biết giữ mình không chìm, rồi mớ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny swimming goggles, floating in a pool of glowing aura with a notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Bốn nguyên tắc

Lời: Mọi kỹ năng Nen đều xây trên bốn nguyên tắc cơ bản: Ten, Zetsu, Ren và Hatsu. Hãy đi lần lượt từng cái.

```text
Wide 16:9 landscape cinematic frame. four glowing stone pillars in a row inside a temple, each carved with a different abstract symbol. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Ten, hay Triền, là giữ các lỗ khí mở nhưng không cho khí trôi đi. Khí bao quanh cơ thể như một lớp áo mỏng.

```text
Wide 16:9 landscape cinematic frame. a person silhouette wrapped in a smooth, even, thin layer of blue glowing aura, calm pose. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Lớp áo này giúp chống lại đòn tấn công bằng khí, và theo lời trong truyện, còn giúp cơ thể chậm già đi.

```text
Wide 16:9 landscape cinematic frame. a glowing aura shield deflecting dark sparks around a calm figure. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Zetsu, hay Tuyệt, thì ngược lại: đóng toàn bộ lỗ khí. Khí gần như biến mất, người khác khó cảm nhận được bạn.

```text
Wide 16:9 landscape cinematic frame. a figure fading into the shadows of a dark alley, no aura visible, only faint outline. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Zetsu rất hợp để ẩn nấp và hồi sức. Nhưng khi đã tắt khí, bạn cũng không còn lớp áo phòng thủ, trúng một đòn…

```text
Wide 16:9 landscape cinematic frame. a hidden figure behind a tree while a glowing fist of aura strikes the ground nearby, tension. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Ren, hay Luyện, là đẩy khí ra mạnh hơn bình thường, để tăng sức mạnh và độ bền của cơ thể.

```text
Wide 16:9 landscape cinematic frame. a fighter flaring a large burst of aura outward, dust and wind blowing around, dramatic low angle. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Người dùng Ren lâu, giữ được lượng khí lớn trong thời gian dài, sẽ có lợi thế rất rõ trong chiến đấu kéo dài.

```text
Wide 16:9 landscape cinematic frame. a progress bar made of glowing aura energy filling up inside a stylized training dojo. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Hatsu, hay Phát, là bước cuối: dùng khí để tạo ra một năng lực riêng. Đây là phần mà mỗi người Nen khác nhau…

```text
Wide 16:9 landscape cinematic frame. a hand releasing a unique glowing shape of energy, like a signature, sparks forming an abstract emblem. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu Ten, Zetsu và Ren là bảng chữ cái, thì Hatsu là bài thơ bạn tự viết ra bằng bảng chữ cái đó.

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a glowing poem with a quill, letters of light floating from the page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Kỹ năng nâng cao

Lời: Từ bốn nguyên tắc, người dùng Nen kết hợp chúng thành những kỹ năng nâng cao. Có bảy cái hay được nhắc tới nh…

```text
Wide 16:9 landscape cinematic frame. seven glowing orbs arranged in a circle on a dark background, each a different color. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Gyo, hay Ngưng, là dồn khí vào một bộ phận, thường là mắt. Nhờ vậy bạn nhìn thấy những khí bị giấu đi.

```text
Wide 16:9 landscape cinematic frame. close-up of a glowing eye with aura concentrated around it, revealing hidden ghostly threads in the air. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: In, hay Ẩn, là phiên bản cao cấp của Zetsu: giấu khí của đòn tấn công để đối phương không nhìn thấy nó, trừ k…

```text
Wide 16:9 landscape cinematic frame. an invisible blade shimmering faintly in the air, almost transparent, a figure unaware of it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Chính vì thế In và Gyo là cặp đấu trí: một người giấu, một người soi. Ai lơ là Gyo sẽ trúng đòn mà không biết…

```text
Wide 16:9 landscape cinematic frame. two figures facing each other, one hiding a transparent weapon, the other with glowing eyes scanning. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: En, hay Viên, là mở rộng lớp Ten ra xa, thành một vùng cảm nhận. Bất cứ thứ gì bước vào vùng đó, bạn đều biết.

```text
Wide 16:9 landscape cinematic frame. a fighter at the center of a huge translucent dome of aura covering a forest, small creatures detected inside. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Vùng En càng rộng càng khó giữ. Người bình thường chỉ duy trì được vài mét, còn những kẻ quái vật có thể trải…

```text
Wide 16:9 landscape cinematic frame. a comparison diagram of a small aura circle and an enormous aura circle over a landscape, map style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Shu, hay Chu, là bọc khí lên đồ vật, như bọc lên cây gậy hay lá bài, biến món đồ thường thành vũ khí nguy hiể…

```text
Wide 16:9 landscape cinematic frame. an ordinary playing card and a wooden stick wrapped in sharp glowing aura, cutting through a metal pipe. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Ko, hay Ngạnh, là dồn toàn bộ khí vào một điểm, phần còn lại của cơ thể dùng Zetsu. Sức công phá cực lớn, như…

```text
Wide 16:9 landscape cinematic frame. a fist glowing with blinding concentrated aura while the rest of the body is dark, dramatic contrast. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Ken, hay Kiên, là giữ Ren quanh toàn thân trong thời gian dài, như một bộ giáp để đỡ đòn từ mọi phía.

```text
Wide 16:9 landscape cinematic frame. a fighter surrounded by a thick sphere-shaped armor of aura, arrows of energy bouncing off. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Ryu, hay Lưu, là chia khí trong từng khoảnh khắc: dồn bảy phần vào tay khi đánh, rồi chuyển sang tay kia khi…

```text
Wide 16:9 landscape cinematic frame. a percentage diagram over a fighter's body showing seventy percent aura in the right fist and thirty percent spread over the body. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Trong truyện, Gon và Killua tập Ryu bằng cách đấu tay đôi, vừa đánh vừa chuyển khí liên tục. Đó là bài tập nề…

```text
Wide 16:9 landscape cinematic frame. two young silhouettes sparring on a rocky field, glowing aura shifting between their hands and legs. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: Gyo để thấy, In để giấu, En để cảm nhận, Shu để bọc đồ, Ko để tất tay, Ken để thủ, Ryu để chia…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a neat chart of seven glowing icons on a chalkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Sáu hệ và hình lục giác

Lời: Giờ tới phần nổi tiếng nhất: sáu hệ Nen. Ai sinh ra cũng thuộc sẵn một hệ, và hệ đó quyết định bạn giỏi loại…

```text
Wide 16:9 landscape cinematic frame. a large glowing hexagon floating in a starry void, six vertices each with a distinct color. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Hệ thứ nhất là Cường hóa: tăng sức mạnh cho chính cơ thể hoặc đồ vật. Đơn giản, bền bỉ, rất hợp chiến đấu trự…

```text
Wide 16:9 landscape cinematic frame. a muscular fist punching a boulder into pieces, orange aura bursting outward. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Gon là người Cường hóa. Chiêu Oẳn tù tì của cậu, dồn khí vào nắm đấm rồi tung ra, chính là Cường hóa ở dạng t…

```text
Wide 16:9 landscape cinematic frame. a small fighter silhouette crouching low with one fist glowing brighter and brighter, energy gathering. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Hệ thứ hai là Biến hóa: thay đổi tính chất của khí, biến nó thành điện, thành thứ dính như kẹo cao su.

```text
Wide 16:9 landscape cinematic frame. a hand with aura transforming into crackling blue lightning on one side and stretchy pink elastic on the other. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Killua biến khí thành điện, còn Hisoka biến khí thành thứ vừa dính như kẹo cao su vừa đàn hồi. Cả hai đều là…

```text
Wide 16:9 landscape cinematic frame. split image: blue lightning arcing between fingers, and a stretchy pink elastic thread connecting two cards. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Hệ thứ ba là Phóng xuất: tách khí khỏi cơ thể và bắn đi, như đạn khí hay quả cầu năng lượng.

```text
Wide 16:9 landscape cinematic frame. a figure firing glowing spheres of aura from their palms across a field, trails of light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Hệ thứ tư là Cụ hiện hóa: dùng khí tạo ra đồ vật hữu hình. Kurapika tạo ra những sợi xích, mỗi sợi mang một n…

```text
Wide 16:9 landscape cinematic frame. glowing chains materializing from thin air around an outstretched hand, each chain tip a different shape. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Hệ thứ năm là Thao tác: điều khiển vật hoặc sinh vật khác, như điều khiển người bằng kim cắm vào cơ thể.

```text
Wide 16:9 landscape cinematic frame. puppet strings of glowing aura connected to a wooden mannequin that moves on its own. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Hệ thứ sáu là Đặc chất: những năng lực không xếp được vào năm hệ còn lại, như đọc tương lai hay đánh cắp năng…

```text
Wide 16:9 landscape cinematic frame. a mysterious floating book and a glowing eye above it, abstract swirling symbols, purple tones. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Sáu hệ được xếp thành một hình lục giác. Thứ tự vòng quanh là: Cường hóa, Biến hóa, Cụ hiện hóa, Đặc chất, Th…

```text
Wide 16:9 landscape cinematic frame. clean infographic style hexagon with six colored nodes connected by glowing lines, no text. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Hình lục giác cho biết bạn học được hệ khác tốt tới đâu. Hệ của chính mình: một trăm phần trăm.

```text
Wide 16:9 landscape cinematic frame. a single hexagon node glowing brightly at full intensity, the others dim. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Hai hệ đứng cạnh: khoảng tám mươi phần trăm. Hai hệ cách một ô: khoảng sáu mươi. Hệ đối diện: chỉ khoảng bốn…

```text
Wide 16:9 landscape cinematic frame. hexagon diagram where node brightness fades step by step from one vertex to the opposite vertex. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Vì thế Gon, một người Cường hóa, học Biến hóa và Phóng xuất khá tốt, nhưng rất yếu với Đặc chất nằm ở phía đố…

```text
Wide 16:9 landscape cinematic frame. a small fighter silhouette at one vertex of a glowing hexagon, a distant dim vertex across from them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Riêng hệ Đặc chất có một điều lạ: nó thường không có từ đầu, mà xuất hiện sau, do hoàn cảnh hoặc do tính cách…

```text
Wide 16:9 landscape cinematic frame. a purple vertex of the hexagon flickering into existence out of mist. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mẹo nhỏ: khi xem một trận đấu, hãy hỏi 'người này đang làm gì với khí?'. Mạnh thêm, đổi chất, bắn đi, tạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over a hexagon diagram, curious expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Bói nước và tính cách

Lời: Vậy làm sao biết mình thuộc hệ nào? Trong truyện có một bài kiểm tra rất gọn: bói nước.

```text
Wide 16:9 landscape cinematic frame. a clear glass of water on a wooden table with a single green leaf floating on top, soft window light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Bạn đặt một chiếc lá lên cốc nước đầy, rồi đặt hai tay quanh cốc và dùng Ren. Cách cốc nước thay đổi sẽ cho b…

```text
Wide 16:9 landscape cinematic frame. two hands cupped around a glass of water with a leaf, aura glowing gently into the water. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Nước dâng lên nhiều hơn là Cường hóa. Khi Gon thử, nước trào ra khỏi cốc.

```text
Wide 16:9 landscape cinematic frame. a glass of water overflowing onto a table, leaf riding the rising water. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Vị nước thay đổi là Biến hóa. Killua nếm thử và thấy nước có vị ngọt.

```text
Wide 16:9 landscape cinematic frame. a glass of water with sparkling sweet-looking shimmer, a small tongue-taste icon floating beside it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Màu nước đổi là Phóng xuất. Nước xuất hiện cặn lạ là Cụ hiện hóa. Chiếc lá tự chuyển động là Thao tác.

```text
Wide 16:9 landscape cinematic frame. three glasses side by side: one with changed color water, one with tiny crystals appearing, one with a leaf spinning. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Còn nếu có một thay đổi khác hẳn, không giống năm kiểu trên, thì đó là Đặc chất.

```text
Wide 16:9 landscape cinematic frame. a glass of water where the leaf withers and glows with strange purple runes, mysterious. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ngoài ra, Hisoka có một thuyết vui về tính cách: người Cường hóa đơn giản và quyết đoán, người Biến hóa thất…

```text
Wide 16:9 landscape cinematic frame. a playing card spread fanned out on a table, each card showing an abstract personality icon, playful mood. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Người Phóng xuất nóng tính, người Cụ hiện hóa hay căng thẳng, người Thao tác lý trí và thích lý lẽ, còn người…

```text
Wide 16:9 landscape cinematic frame. six small chibi silhouettes in different moods: determined, sly, angry, nervous, thoughtful, aloof. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Chính Hisoka nói đây chỉ là kiểu xem nhóm máu đoán tính cách. Đừng coi là luật, nhưng nó giải thích vì sao nh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shrugging with a small smile, a question mark floating above a personality chart. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Hatsu: năng lực riêng

Lời: Biết hệ của mình rồi, bước tiếp theo là thiết kế Hatsu, năng lực riêng. Và đây là chỗ nhiều người dùng Nen tự…

```text
Wide 16:9 landscape cinematic frame. a blueprint style drawing of a glowing energy weapon being designed on a drafting table. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nguyên tắc vàng: năng lực nên hợp với hệ của mình. Người Cường hóa nên làm năng lực đánh mạnh, không nên cố t…

```text
Wide 16:9 landscape cinematic frame. a signpost with two paths, one bright path toward a glowing fist icon, one dim path toward a complex machine icon. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Trong truyện có một ví dụ đau lòng: một võ sĩ tên Kastro, rất tài năng, nhưng chọn một năng lực nằm xa hệ tự…

```text
Wide 16:9 landscape cinematic frame. a proud martial artist silhouette in a tournament arena, a transparent double of himself standing beside him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Hisoka gọi đó là tràn bộ nhớ: dồn quá nhiều công sức vào một năng lực không hợp, nên không còn chỗ để tiến xa…

```text
Wide 16:9 landscape cinematic frame. an overflowing cup of glowing energy spilling over a small container, metaphor for capacity. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kết quả là Kastro thua. Bài học rất rõ: năng lực mạnh nhất chưa chắc là năng lực ngầu nhất, mà là năng lực hợ…

```text
Wide 16:9 landscape cinematic frame. a fallen fighter's silhouette in an empty arena, dramatic spotlight, falling petals. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Năng lực tốt thường có ba điều: hợp hệ, hợp tính cách, và có một ý tưởng rõ ràng mà người dùng tin tuyệt đối.

```text
Wide 16:9 landscape cinematic frame. three glowing check marks stacked vertically beside a small energy emblem. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chấm điểm: nếu năng lực của bạn cần giải thích quá ba câu, có lẽ nó đang dùng nhiều khí hơn mức cần thiế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a scorecard with three stars, sitting on a stack of books. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Giới hạn và giao ước

Lời: Và giờ, phần quan trọng nhất để hiểu chuyện của Gon: giới hạn và giao ước.

```text
Wide 16:9 landscape cinematic frame. an ancient contract scroll sealed with a glowing wax seal shaped like a chain link. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Luật rất đơn giản: tự đặt ra điều kiện càng khắt khe cho năng lực của mình, năng lực đó càng mạnh.

```text
Wide 16:9 landscape cinematic frame. a balance scale with a heavy glowing chain on one side and a burst of power on the other, rising. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Điều kiện có thể là 'chỉ dùng được với một loại kẻ thù', 'chỉ dùng khi đứng yên', hay 'nếu phá luật, ta sẽ ch…

```text
Wide 16:9 landscape cinematic frame. three floating glowing contract clauses shown as abstract icons: a target, a standing figure, a skull. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kurapika là ví dụ kinh điển. Cậu tự thề sợi xích mạnh nhất chỉ được dùng với băng Ảo Ảnh, nếu dùng với người…

```text
Wide 16:9 landscape cinematic frame. a glowing chain wrapped around a heart-shaped light, with a spider-shaped silhouette target far away. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nhờ giao ước khắc nghiệt đó, sợi xích đủ mạnh để trói những kẻ vượt xa cậu về kinh nghiệm.

```text
Wide 16:9 landscape cinematic frame. a glowing chain binding a large shadowy figure against a stone wall. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Về sau, truyện cho thấy năng lực Emperor Time của Kurapika còn phải trả giá bằng chính tuổi thọ của cậu mỗi k…

```text
Wide 16:9 landscape cinematic frame. an hourglass with glowing sand draining quickly, a chain wrapped around it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Giao ước không chỉ là luật chơi. Nó là cái giá mà người dùng Nen chấp nhận trả để đổi lấy sức mạnh.

```text
Wide 16:9 landscape cinematic frame. a merchant-style balance weighing a glowing gem of power against a fading candle of life. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: giao ước càng đổi lấy thứ quý giá, sức mạnh càng lớn. Và không có thứ gì quý giá hơn tương lai của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking serious, holding a small glowing hourglass carefully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Vì sao Gon mất Nen?

Lời: Giờ quay lại câu hỏi ban đầu. Trong arc Kiến Chimera, Gon biết người thầy Kite của mình không thể cứu được nữ…

```text
Wide 16:9 landscape cinematic frame. a boy silhouette kneeling in a dark forest clearing, rain falling, distant fallen figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Cơn giận và tuyệt vọng đẩy Gon đến một giao ước chưa từng có: đổi tất cả những gì mình có để có đủ sức mạnh n…

```text
Wide 16:9 landscape cinematic frame. a small figure with a dark aura spiraling upward like a storm, cracks forming in the ground. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Cậu ép cơ thể lớn vượt tuổi, đạt tới sức mạnh mà lẽ ra phải cả đời tu luyện mới có, và đánh bại kẻ thù.

```text
Wide 16:9 landscape cinematic frame. a tall adult silhouette with overwhelming aura towering above a smaller shadowy creature, back view. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Nhưng thứ bị đem ra đổi chính là tương lai: toàn bộ tiềm năng và Nen mà Gon lẽ ra sẽ có trong suốt cuộc đời.

```text
Wide 16:9 landscape cinematic frame. a glowing path into the future crumbling into pieces behind a figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Gon suýt chết. Sau khi được cứu, cậu còn sống, nhưng khi nói chuyện với cha là Ging, Gon cho biết mình không…

```text
Wide 16:9 landscape cinematic frame. a boy silhouette holding a phone at a sunny hilltop, a faint aura around him that he cannot see. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Chi tiết đáng chú ý: Ging vẫn thấy khí quanh Gon. Nghĩa là Gon không mất khí, mà mất khả năng cảm nhận và điề…

```text
Wide 16:9 landscape cinematic frame. a diagram: a figure with a soft aura glow, but the eyes of the figure are covered by a gentle mist. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Theo luật giao ước, chuyện này hoàn toàn hợp lý: Gon đã trả trước toàn bộ tương lai, nên hiện tại không còn g…

```text
Wide 16:9 landscape cinematic frame. a balance scale fully tilted, one side holding a burst of past power, the other side empty. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Liệu Gon có lấy lại được Nen không? Truyện chưa trả lời chắc chắn. Nhiều fan tin là có, nhưng hiện tại đó vẫn…

```text
Wide 16:9 landscape cinematic frame. a single green sprout growing from cracked ground at dawn, hopeful light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · Vì sao Nen được yêu thích? · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi tổng kết, Kaku muốn bàn thêm một câu hỏi: vì sao rất nhiều fan xem Nen là hệ thống sức mạnh hay nhấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a pile of books with several other power-system symbols floating around, thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Lý do đầu tiên: Nen có luật rõ ràng. Người xem hiểu được giới hạn của từng nhân vật, nên khi ai đó thắng, chi…

```text
Wide 16:9 landscape cinematic frame. a clean rulebook with glowing pages opened on a stone table, rays of light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Ở nhiều bộ khác, nhân vật chính mạnh lên nhờ một cơn giận hay một cú bộc phát khó giải thích. Trong Hunter x…

```text
Wide 16:9 landscape cinematic frame. a comparison of two paths: a chaotic explosion of energy versus a neat glowing contract with a price tag. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Lý do thứ hai: thông tin là vũ khí. Biết năng lực và điều kiện của đối phương quan trọng không kém sức mạnh t…

```text
Wide 16:9 landscape cinematic frame. a detective style board with glowing threads connecting clue cards, dark room. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Vì thế nhiều trận đấu giống một ván bài lật ngửa dần: ai giấu được lá bài của mình lâu hơn, người đó có lợi t…

```text
Wide 16:9 landscape cinematic frame. a table with face-down glowing playing cards being slowly turned over one by one. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92

Lời: Lý do thứ ba: người yếu hơn vẫn có thể thắng. Một năng lực nhỏ nhưng thông minh, cộng với giao ước đúng, có t…

```text
Wide 16:9 landscape cinematic frame. a small figure standing confidently before a giant shadow, holding a tiny glowing chain. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93

Lời: Điều này làm mỗi trận đấu khó đoán. Bạn không thể chỉ so ai có nhiều khí hơn, mà phải xem ai dùng khí thông m…

```text
Wide 16:9 landscape cinematic frame. two balance scales side by side, one weighing raw energy and one weighing a lightbulb of ideas. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94

Lời: Lý do thứ tư: Nen phản ánh tính cách. Năng lực của mỗi người nói lên họ là ai, họ mong muốn gì, và họ sẵn sàn…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a person's silhouette as a glowing emblem shaped like their inner self. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95

Lời: Kurapika sống vì trả thù, nên năng lực của cậu là những sợi xích trói buộc và đổi bằng mạng sống. Gon sống th…

```text
Wide 16:9 landscape cinematic frame. split image: a coiled glowing chain on one side, a single glowing fist on the other, symmetric composition. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96

Lời: Khi năng lực gắn với tính cách, trận đấu cũng là câu chuyện. Người xem không chỉ hỏi ai mạnh hơn, mà hỏi ai s…

```text
Wide 16:9 landscape cinematic frame. a dramatic stage with two silhouettes facing each other under a single spotlight, falling feathers. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s97

Lời: Và cuối cùng, Nen có giá. Không có sức mạnh nào miễn phí. Chính điều đó làm khoảnh khắc Gon biến đổi vừa đẹp,…

```text
Wide 16:9 landscape cinematic frame. a single glowing flower blooming from cracked dark stone, bittersweet mood. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s98 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là bài học lớn nhất của Nen: mọi thứ mạnh mẽ đều cần kỷ luật, lựa chọn đúng, và sẵn sàng trả gi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing its eyes calmly, a tiny glowing hexagon floating above its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s99 · Tóm tắt

Lời: Tóm lại: khí là năng lượng sống. Bốn nguyên tắc để giữ, tắt, dồn và phát khí. Bảy kỹ năng nâng cao để chiến đ…

```text
Wide 16:9 landscape cinematic frame. a summary infographic with glowing icons arranged in rows on a dark background, no text. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s100

Lời: Sáu hệ trên hình lục giác quyết định bạn giỏi gì. Và giới hạn cùng giao ước cho phép đổi cái giá lấy sức mạnh.

```text
Wide 16:9 landscape cinematic frame. a glowing hexagon connected by a chain to a sealed contract scroll, symmetric composition. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s101

Lời: Chính vì mọi sức mạnh đều có luật và có giá, các trận đấu trong Hunter x Hunter mới căng thẳng như một ván cờ.

```text
Wide 16:9 landscape cinematic frame. two figures facing each other on a giant chessboard made of glowing tiles, strategic mood. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s102 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu tự làm bói nước, bạn nghĩ mình thuộc hệ nào, và bạn sẽ đặt giao ước gì cho năng lực của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a glass of water with a leaf, looking at the viewer with curiosity. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s103 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video giúp bạn hiểu Nen rõ hơn, hãy đăng ký kênh. Video sau Kaku sẽ giải mã Haki trong One Piece.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing subscribe-style button shape without any text, stack of books behind. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s104 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a big glowing notebook and waving goodbye in a warm library at night. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 60 giây · cảnh s01–s06 · 776 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Hunter x Hunter đến hết arc Kiến Chimera, và nhắc ngắn một chi tiết ở arc Thừa kế. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Có một cậu bé mười bốn tuổi, trong cơn giận, đã biến mình thành một chiến binh trưởng thành mạnh tới mức kẻ thù phải run sợ.

<short pause> Nhưng cái giá của khoảnh khắc đó là mọi thứ. Sau trận đấu, cậu không còn dùng được, thậm chí không còn nhìn thấy sức mạnh từng là của mình.

<short pause> Vì sao lại như vậy? Câu trả lời nằm trong một hệ thống sức mạnh được xem là chặt chẽ bậc nhất anime: Nen.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã Nen từ con số không: khí là gì, bốn nguyên tắc, sáu hệ, và luật giao ước.

<short pause> Xem hết video, bạn sẽ tự trả lời được vì sao Gon mất Nen, và tự đoán được một nhân vật thuộc hệ nào chỉ qua cách họ chiến đấu.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Hunter x Hunter đến hết arc Kiến Chimera, và nhắc ngắn một chi tiết ở arc Thừa kế. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

[pause] Có một cậu bé mười bốn tuổi, trong cơn giận, đã biến mình thành một chiến binh trưởng thành mạnh tới mức kẻ thù phải run sợ.

[pause] Nhưng cái giá của khoảnh khắc đó là mọi thứ. Sau trận đấu, cậu không còn dùng được, thậm chí không còn nhìn thấy sức mạnh từng là của mình.

[pause] [curious] Vì sao lại như vậy? Câu trả lời nằm trong một hệ thống sức mạnh được xem là chặt chẽ bậc nhất anime: Nen.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã Nen từ con số không: khí là gì, bốn nguyên tắc, sáu hệ, và luật giao ước.

[pause] Xem hết video, bạn sẽ tự trả lời được vì sao Gon mất Nen, và tự đoán được một nhân vật thuộc hệ nào chỉ qua cách họ chiến đấu.
```

### c02 · Nen là gì?

Khoảng 111 giây · cảnh s07–s18 · 1449 ký tự

**Gemini**

```text
Trong Hunter x Hunter, mọi sinh vật sống đều tỏa ra một dòng năng lượng sống, gọi là khí, hay aura.

<short pause> Với người thường, khí chỉ rò rỉ ra ngoài một cách vô thức qua các lỗ khí trên cơ thể, rồi tan đi, không để làm gì.

<short pause> Nen là kỹ năng kiểm soát dòng khí đó: giữ nó lại, dồn nó đi, và biến nó thành sức mạnh.

<short pause> Tên gọi Nen có nghĩa là niệm, ý niệm. Người dùng được gọi là người dùng Nen, và phần lớn thợ săn chuyên nghiệp đều phải thành thạo nó.

<short pause> Có một chi tiết thú vị: lúc đầu, thầy Wing không dạy Gon và Killua Nen thật. Thầy dạy một phiên bản khác, chỉ nói về ý chí.

<short pause> Lý do rất đơn giản: Nen thật nguy hiểm. Mở lỗ khí sai cách, hoặc bị kẻ xấu tấn công bằng khí khi chưa phòng thủ, có thể chết.

<short pause> Có hai cách để đánh thức Nen. Cách chậm là thiền định, mở từng lỗ khí một cách tự nhiên. Cách này an toàn nhưng rất lâu.

<short pause> Cách nhanh là để một người đã thành thạo truyền khí vào cơ thể bạn, ép tất cả lỗ khí bật mở cùng lúc.

<short pause> Cách này được xem là cấm kỵ, vì người không đủ tố chất có thể kiệt sức hoặc chết. Gon và Killua sống sót, nhưng không phải ai cũng may mắn như vậy.

<short pause> Khí không phải phép thuật từ bên ngoài, mà là sức sống của chính cơ thể. Vì thế người kiệt sức hay bị thương nặng cũng sẽ có dòng khí yếu đi.

<short pause> Và vì khí gắn với sự sống, bị tấn công bằng khí khi không phòng thủ có thể gây thương tổn nặng hơn nhiều so với một đòn đánh thường.

<short pause> <laugh> Kaku ghi chú: Nen giống như học bơi. Ai cũng có khí, nhưng chỉ người học mới biết giữ mình không chìm, rồi mới bơi nhanh được.
```

**ElevenLabs**

```text
Trong Hunter x Hunter, mọi sinh vật sống đều tỏa ra một dòng năng lượng sống, gọi là khí, hay aura.

[pause] Với người thường, khí chỉ rò rỉ ra ngoài một cách vô thức qua các lỗ khí trên cơ thể, rồi tan đi, không để làm gì.

[pause] Nen là kỹ năng kiểm soát dòng khí đó: giữ nó lại, dồn nó đi, và biến nó thành sức mạnh.

[pause] Tên gọi Nen có nghĩa là niệm, ý niệm. Người dùng được gọi là người dùng Nen, và phần lớn thợ săn chuyên nghiệp đều phải thành thạo nó.

[pause] Có một chi tiết thú vị: lúc đầu, thầy Wing không dạy Gon và Killua Nen thật. Thầy dạy một phiên bản khác, chỉ nói về ý chí.

[pause] Lý do rất đơn giản: Nen thật nguy hiểm. Mở lỗ khí sai cách, hoặc bị kẻ xấu tấn công bằng khí khi chưa phòng thủ, có thể chết.

[pause] Có hai cách để đánh thức Nen. Cách chậm là thiền định, mở từng lỗ khí một cách tự nhiên. Cách này an toàn nhưng rất lâu.

[pause] Cách nhanh là để một người đã thành thạo truyền khí vào cơ thể bạn, ép tất cả lỗ khí bật mở cùng lúc.

[pause] Cách này được xem là cấm kỵ, vì người không đủ tố chất có thể kiệt sức hoặc chết. Gon và Killua sống sót, nhưng không phải ai cũng may mắn như vậy.

[pause] Khí không phải phép thuật từ bên ngoài, mà là sức sống của chính cơ thể. Vì thế người kiệt sức hay bị thương nặng cũng sẽ có dòng khí yếu đi.

[pause] Và vì khí gắn với sự sống, bị tấn công bằng khí khi không phòng thủ có thể gây thương tổn nặng hơn nhiều so với một đòn đánh thường.

[pause] [chuckles] Kaku ghi chú: Nen giống như học bơi. Ai cũng có khí, nhưng chỉ người học mới biết giữ mình không chìm, rồi mới bơi nhanh được.
```

### c03 · Bốn nguyên tắc

Khoảng 75 giây · cảnh s19–s27 · 969 ký tự

**Gemini**

```text
Mọi kỹ năng Nen đều xây trên bốn nguyên tắc cơ bản: Ten, Zetsu, Ren và Hatsu. Hãy đi lần lượt từng cái.

<short pause> Ten, hay Triền, là giữ các lỗ khí mở nhưng không cho khí trôi đi. Khí bao quanh cơ thể như một lớp áo mỏng.

<short pause> Lớp áo này giúp chống lại đòn tấn công bằng khí, và theo lời trong truyện, còn giúp cơ thể chậm già đi.

<short pause> Zetsu, hay Tuyệt, thì ngược lại: đóng toàn bộ lỗ khí. Khí gần như biến mất, người khác khó cảm nhận được bạn.

<short pause> Zetsu rất hợp để ẩn nấp và hồi sức. <short pause> Nhưng khi đã tắt khí, bạn cũng không còn lớp áo phòng thủ, trúng một đòn Nen là cực kỳ nguy hiểm.

<short pause> Ren, hay Luyện, là đẩy khí ra mạnh hơn bình thường, để tăng sức mạnh và độ bền của cơ thể.

<short pause> Người dùng Ren lâu, giữ được lượng khí lớn trong thời gian dài, sẽ có lợi thế rất rõ trong chiến đấu kéo dài.

<short pause> Hatsu, hay Phát, là bước cuối: dùng khí để tạo ra một năng lực riêng. Đây là phần mà mỗi người Nen khác nhau hoàn toàn.

<short pause> Nếu Ten, Zetsu và Ren là bảng chữ cái, thì Hatsu là bài thơ bạn tự viết ra bằng bảng chữ cái đó.
```

**ElevenLabs**

```text
Mọi kỹ năng Nen đều xây trên bốn nguyên tắc cơ bản: Ten, Zetsu, Ren và Hatsu. Hãy đi lần lượt từng cái.

[pause] Ten, hay Triền, là giữ các lỗ khí mở nhưng không cho khí trôi đi. Khí bao quanh cơ thể như một lớp áo mỏng.

[pause] Lớp áo này giúp chống lại đòn tấn công bằng khí, và theo lời trong truyện, còn giúp cơ thể chậm già đi.

[pause] Zetsu, hay Tuyệt, thì ngược lại: đóng toàn bộ lỗ khí. Khí gần như biến mất, người khác khó cảm nhận được bạn.

[pause] Zetsu rất hợp để ẩn nấp và hồi sức. [pause] Nhưng khi đã tắt khí, bạn cũng không còn lớp áo phòng thủ, trúng một đòn Nen là cực kỳ nguy hiểm.

[pause] Ren, hay Luyện, là đẩy khí ra mạnh hơn bình thường, để tăng sức mạnh và độ bền của cơ thể.

[pause] Người dùng Ren lâu, giữ được lượng khí lớn trong thời gian dài, sẽ có lợi thế rất rõ trong chiến đấu kéo dài.

[pause] Hatsu, hay Phát, là bước cuối: dùng khí để tạo ra một năng lực riêng. Đây là phần mà mỗi người Nen khác nhau hoàn toàn.

[pause] Nếu Ten, Zetsu và Ren là bảng chữ cái, thì Hatsu là bài thơ bạn tự viết ra bằng bảng chữ cái đó.
```

### c04 · Kỹ năng nâng cao

Khoảng 109 giây · cảnh s28–s39 · 1413 ký tự

**Gemini**

```text
Từ bốn nguyên tắc, người dùng Nen kết hợp chúng thành những kỹ năng nâng cao. Có bảy cái hay được nhắc tới nhất.

<short pause> Gyo, hay Ngưng, là dồn khí vào một bộ phận, thường là mắt. Nhờ vậy bạn nhìn thấy những khí bị giấu đi.

<short pause> In, hay Ẩn, là phiên bản cao cấp của Zetsu: giấu khí của đòn tấn công để đối phương không nhìn thấy nó, trừ khi họ dùng Gyo.

<short pause> Chính vì thế In và Gyo là cặp đấu trí: một người giấu, một người soi. Ai lơ là Gyo sẽ trúng đòn mà không biết đòn đến từ đâu.

<short pause> En, hay Viên, là mở rộng lớp Ten ra xa, thành một vùng cảm nhận. Bất cứ thứ gì bước vào vùng đó, bạn đều biết.

<short pause> Vùng En càng rộng càng khó giữ. Người bình thường chỉ duy trì được vài mét, còn những kẻ quái vật có thể trải En rất rộng.

<short pause> Shu, hay Chu, là bọc khí lên đồ vật, như bọc lên cây gậy hay lá bài, biến món đồ thường thành vũ khí nguy hiểm.

<short pause> Ko, hay Ngạnh, là dồn toàn bộ khí vào một điểm, phần còn lại của cơ thể dùng Zetsu. Sức công phá cực lớn, nhưng chỗ khác gần như không được bảo vệ.

<short pause> Ken, hay Kiên, là giữ Ren quanh toàn thân trong thời gian dài, như một bộ giáp để đỡ đòn từ mọi phía.

<short pause> Ryu, hay Lưu, là chia khí trong từng khoảnh khắc: dồn bảy phần vào tay khi đánh, rồi chuyển sang tay kia khi đỡ.

<short pause> Trong truyện, Gon và Killua tập Ryu bằng cách đấu tay đôi, vừa đánh vừa chuyển khí liên tục. Đó là bài tập nền tảng của chiến đấu Nen.

<short pause> <laugh> Kaku tóm lại: Gyo để thấy, In để giấu, En để cảm nhận, Shu để bọc đồ, Ko để tất tay, Ken để thủ, Ryu để chia khí.
```

**ElevenLabs**

```text
Từ bốn nguyên tắc, người dùng Nen kết hợp chúng thành những kỹ năng nâng cao. Có bảy cái hay được nhắc tới nhất.

[pause] Gyo, hay Ngưng, là dồn khí vào một bộ phận, thường là mắt. Nhờ vậy bạn nhìn thấy những khí bị giấu đi.

[pause] In, hay Ẩn, là phiên bản cao cấp của Zetsu: giấu khí của đòn tấn công để đối phương không nhìn thấy nó, trừ khi họ dùng Gyo.

[pause] Chính vì thế In và Gyo là cặp đấu trí: một người giấu, một người soi. Ai lơ là Gyo sẽ trúng đòn mà không biết đòn đến từ đâu.

[pause] En, hay Viên, là mở rộng lớp Ten ra xa, thành một vùng cảm nhận. Bất cứ thứ gì bước vào vùng đó, bạn đều biết.

[pause] Vùng En càng rộng càng khó giữ. Người bình thường chỉ duy trì được vài mét, còn những kẻ quái vật có thể trải En rất rộng.

[pause] Shu, hay Chu, là bọc khí lên đồ vật, như bọc lên cây gậy hay lá bài, biến món đồ thường thành vũ khí nguy hiểm.

[pause] Ko, hay Ngạnh, là dồn toàn bộ khí vào một điểm, phần còn lại của cơ thể dùng Zetsu. Sức công phá cực lớn, nhưng chỗ khác gần như không được bảo vệ.

[pause] Ken, hay Kiên, là giữ Ren quanh toàn thân trong thời gian dài, như một bộ giáp để đỡ đòn từ mọi phía.

[pause] Ryu, hay Lưu, là chia khí trong từng khoảnh khắc: dồn bảy phần vào tay khi đánh, rồi chuyển sang tay kia khi đỡ.

[pause] Trong truyện, Gon và Killua tập Ryu bằng cách đấu tay đôi, vừa đánh vừa chuyển khí liên tục. Đó là bài tập nền tảng của chiến đấu Nen.

[pause] [chuckles] Kaku tóm lại: Gyo để thấy, In để giấu, En để cảm nhận, Shu để bọc đồ, Ko để tất tay, Ken để thủ, Ryu để chia khí.
```

### c05 · Sáu hệ và hình lục giác

Khoảng 134 giây · cảnh s40–s54 · 1741 ký tự

**Gemini**

```text
Giờ tới phần nổi tiếng nhất: sáu hệ Nen. Ai sinh ra cũng thuộc sẵn một hệ, và hệ đó quyết định bạn giỏi loại năng lực nào.

<short pause> Hệ thứ nhất là Cường hóa: tăng sức mạnh cho chính cơ thể hoặc đồ vật. Đơn giản, bền bỉ, rất hợp chiến đấu trực diện.

<short pause> Gon là người Cường hóa. Chiêu Oẳn tù tì của cậu, dồn khí vào nắm đấm rồi tung ra, chính là Cường hóa ở dạng thuần nhất.

<short pause> Hệ thứ hai là Biến hóa: thay đổi tính chất của khí, biến nó thành điện, thành thứ dính như kẹo cao su.

<short pause> Killua biến khí thành điện, còn Hisoka biến khí thành thứ vừa dính như kẹo cao su vừa đàn hồi. Cả hai đều là Biến hóa.

<short pause> Hệ thứ ba là Phóng xuất: tách khí khỏi cơ thể và bắn đi, như đạn khí hay quả cầu năng lượng.

<short pause> Hệ thứ tư là Cụ hiện hóa: dùng khí tạo ra đồ vật hữu hình. Kurapika tạo ra những sợi xích, mỗi sợi mang một năng lực.

<short pause> Hệ thứ năm là Thao tác: điều khiển vật hoặc sinh vật khác, như điều khiển người bằng kim cắm vào cơ thể.

<short pause> Hệ thứ sáu là Đặc chất: những năng lực không xếp được vào năm hệ còn lại, như đọc tương lai hay đánh cắp năng lực người khác.

<short pause> Sáu hệ được xếp thành một hình lục giác. Thứ tự vòng quanh là: Cường hóa, Biến hóa, Cụ hiện hóa, Đặc chất, Thao tác, Phóng xuất.

<short pause> Hình lục giác cho biết bạn học được hệ khác tốt tới đâu. Hệ của chính mình: một trăm phần trăm.

<short pause> Hai hệ đứng cạnh: khoảng tám mươi phần trăm. Hai hệ cách một ô: khoảng sáu mươi. Hệ đối diện: chỉ khoảng bốn mươi.

<short pause> Vì thế Gon, một người Cường hóa, học Biến hóa và Phóng xuất khá tốt, nhưng rất yếu với Đặc chất nằm ở phía đối diện.

<short pause> Riêng hệ Đặc chất có một điều lạ: nó thường không có từ đầu, mà xuất hiện sau, do hoàn cảnh hoặc do tính cách người đó.

<short pause> <laugh> Kaku mẹo nhỏ: khi xem một trận đấu, hãy hỏi 'người này đang làm gì với khí?'. Mạnh thêm, đổi chất, bắn đi, tạo đồ, điều khiển, hay kỳ lạ. Đó là hệ của họ.
```

**ElevenLabs**

```text
Giờ tới phần nổi tiếng nhất: sáu hệ Nen. Ai sinh ra cũng thuộc sẵn một hệ, và hệ đó quyết định bạn giỏi loại năng lực nào.

[pause] Hệ thứ nhất là Cường hóa: tăng sức mạnh cho chính cơ thể hoặc đồ vật. Đơn giản, bền bỉ, rất hợp chiến đấu trực diện.

[pause] Gon là người Cường hóa. Chiêu Oẳn tù tì của cậu, dồn khí vào nắm đấm rồi tung ra, chính là Cường hóa ở dạng thuần nhất.

[pause] Hệ thứ hai là Biến hóa: thay đổi tính chất của khí, biến nó thành điện, thành thứ dính như kẹo cao su.

[pause] Killua biến khí thành điện, còn Hisoka biến khí thành thứ vừa dính như kẹo cao su vừa đàn hồi. Cả hai đều là Biến hóa.

[pause] Hệ thứ ba là Phóng xuất: tách khí khỏi cơ thể và bắn đi, như đạn khí hay quả cầu năng lượng.

[pause] Hệ thứ tư là Cụ hiện hóa: dùng khí tạo ra đồ vật hữu hình. Kurapika tạo ra những sợi xích, mỗi sợi mang một năng lực.

[pause] Hệ thứ năm là Thao tác: điều khiển vật hoặc sinh vật khác, như điều khiển người bằng kim cắm vào cơ thể.

[pause] Hệ thứ sáu là Đặc chất: những năng lực không xếp được vào năm hệ còn lại, như đọc tương lai hay đánh cắp năng lực người khác.

[pause] Sáu hệ được xếp thành một hình lục giác. Thứ tự vòng quanh là: Cường hóa, Biến hóa, Cụ hiện hóa, Đặc chất, Thao tác, Phóng xuất.

[pause] Hình lục giác cho biết bạn học được hệ khác tốt tới đâu. Hệ của chính mình: một trăm phần trăm.

[pause] Hai hệ đứng cạnh: khoảng tám mươi phần trăm. Hai hệ cách một ô: khoảng sáu mươi. Hệ đối diện: chỉ khoảng bốn mươi.

[pause] Vì thế Gon, một người Cường hóa, học Biến hóa và Phóng xuất khá tốt, nhưng rất yếu với Đặc chất nằm ở phía đối diện.

[pause] Riêng hệ Đặc chất có một điều lạ: nó thường không có từ đầu, mà xuất hiện sau, do hoàn cảnh hoặc do tính cách người đó.

[pause] [chuckles] Kaku mẹo nhỏ: khi xem một trận đấu, hãy hỏi 'người này đang làm gì với khí?'. Mạnh thêm, đổi chất, bắn đi, tạo đồ, điều khiển, hay kỳ lạ. Đó là hệ của họ.
```

### c06 · Bói nước và tính cách / Hatsu: năng lực riêng

Khoảng 138 giây · cảnh s55–s70 · 1789 ký tự

**Gemini**

```text
Vậy làm sao biết mình thuộc hệ nào? Trong truyện có một bài kiểm tra rất gọn: bói nước.

<short pause> Bạn đặt một chiếc lá lên cốc nước đầy, rồi đặt hai tay quanh cốc và dùng Ren. Cách cốc nước thay đổi sẽ cho biết hệ của bạn.

<short pause> Nước dâng lên nhiều hơn là Cường hóa. Khi Gon thử, nước trào ra khỏi cốc.

<short pause> Vị nước thay đổi là Biến hóa. Killua nếm thử và thấy nước có vị ngọt.

<short pause> Màu nước đổi là Phóng xuất. Nước xuất hiện cặn lạ là Cụ hiện hóa. Chiếc lá tự chuyển động là Thao tác.

<short pause> Còn nếu có một thay đổi khác hẳn, không giống năm kiểu trên, thì đó là Đặc chất.

<short pause> Ngoài ra, Hisoka có một thuyết vui về tính cách: người Cường hóa đơn giản và quyết đoán, người Biến hóa thất thường và hay nói dối.

<short pause> Người Phóng xuất nóng tính, người Cụ hiện hóa hay căng thẳng, người Thao tác lý trí và thích lý lẽ, còn người Đặc chất thì cá tính riêng biệt.

<short pause> Chính Hisoka nói đây chỉ là kiểu xem nhóm máu đoán tính cách. Đừng coi là luật, nhưng nó giải thích vì sao nhân vật cùng hệ lại hay giống nhau.

<short pause> Biết hệ của mình rồi, bước tiếp theo là thiết kế Hatsu, năng lực riêng. Và đây là chỗ nhiều người dùng Nen tự làm hỏng mình.

<short pause> Nguyên tắc vàng: năng lực nên hợp với hệ của mình. Người Cường hóa nên làm năng lực đánh mạnh, không nên cố tạo ra đồ vật phức tạp.

<short pause> Trong truyện có một ví dụ đau lòng: một võ sĩ tên Kastro, rất tài năng, nhưng chọn một năng lực nằm xa hệ tự nhiên của mình.

<short pause> Hisoka gọi đó là tràn bộ nhớ: dồn quá nhiều công sức vào một năng lực không hợp, nên không còn chỗ để tiến xa hơn.

<short pause> Kết quả là Kastro thua. Bài học rất rõ: năng lực mạnh nhất chưa chắc là năng lực ngầu nhất, mà là năng lực hợp với mình nhất.

<short pause> Năng lực tốt thường có ba điều: hợp hệ, hợp tính cách, và có một ý tưởng rõ ràng mà người dùng tin tuyệt đối.

<short pause> <laugh> Kaku chấm điểm: nếu năng lực của bạn cần giải thích quá ba câu, có lẽ nó đang dùng nhiều khí hơn mức cần thiết.
```

**ElevenLabs**

```text
[curious] Vậy làm sao biết mình thuộc hệ nào? Trong truyện có một bài kiểm tra rất gọn: bói nước.

[pause] Bạn đặt một chiếc lá lên cốc nước đầy, rồi đặt hai tay quanh cốc và dùng Ren. Cách cốc nước thay đổi sẽ cho biết hệ của bạn.

[pause] Nước dâng lên nhiều hơn là Cường hóa. Khi Gon thử, nước trào ra khỏi cốc.

[pause] Vị nước thay đổi là Biến hóa. Killua nếm thử và thấy nước có vị ngọt.

[pause] Màu nước đổi là Phóng xuất. Nước xuất hiện cặn lạ là Cụ hiện hóa. Chiếc lá tự chuyển động là Thao tác.

[pause] Còn nếu có một thay đổi khác hẳn, không giống năm kiểu trên, thì đó là Đặc chất.

[pause] Ngoài ra, Hisoka có một thuyết vui về tính cách: người Cường hóa đơn giản và quyết đoán, người Biến hóa thất thường và hay nói dối.

[pause] Người Phóng xuất nóng tính, người Cụ hiện hóa hay căng thẳng, người Thao tác lý trí và thích lý lẽ, còn người Đặc chất thì cá tính riêng biệt.

[pause] Chính Hisoka nói đây chỉ là kiểu xem nhóm máu đoán tính cách. Đừng coi là luật, nhưng nó giải thích vì sao nhân vật cùng hệ lại hay giống nhau.

[pause] Biết hệ của mình rồi, bước tiếp theo là thiết kế Hatsu, năng lực riêng. Và đây là chỗ nhiều người dùng Nen tự làm hỏng mình.

[pause] Nguyên tắc vàng: năng lực nên hợp với hệ của mình. Người Cường hóa nên làm năng lực đánh mạnh, không nên cố tạo ra đồ vật phức tạp.

[pause] Trong truyện có một ví dụ đau lòng: một võ sĩ tên Kastro, rất tài năng, nhưng chọn một năng lực nằm xa hệ tự nhiên của mình.

[pause] Hisoka gọi đó là tràn bộ nhớ: dồn quá nhiều công sức vào một năng lực không hợp, nên không còn chỗ để tiến xa hơn.

[pause] Kết quả là Kastro thua. Bài học rất rõ: năng lực mạnh nhất chưa chắc là năng lực ngầu nhất, mà là năng lực hợp với mình nhất.

[pause] Năng lực tốt thường có ba điều: hợp hệ, hợp tính cách, và có một ý tưởng rõ ràng mà người dùng tin tuyệt đối.

[pause] [chuckles] Kaku chấm điểm: nếu năng lực của bạn cần giải thích quá ba câu, có lẽ nó đang dùng nhiều khí hơn mức cần thiết.
```

### c07 · Giới hạn và giao ước / Vì sao Gon mất Nen?

Khoảng 137 giây · cảnh s71–s86 · 1780 ký tự

**Gemini**

```text
Và giờ, phần quan trọng nhất để hiểu chuyện của Gon: giới hạn và giao ước.

<short pause> Luật rất đơn giản: tự đặt ra điều kiện càng khắt khe cho năng lực của mình, năng lực đó càng mạnh.

<short pause> Điều kiện có thể là 'chỉ dùng được với một loại kẻ thù', 'chỉ dùng khi đứng yên', hay 'nếu phá luật, ta sẽ chết'.

<short pause> Kurapika là ví dụ kinh điển. Cậu tự thề sợi xích mạnh nhất chỉ được dùng với băng Ảo Ảnh, nếu dùng với người khác, chính cậu sẽ chết.

<short pause> Nhờ giao ước khắc nghiệt đó, sợi xích đủ mạnh để trói những kẻ vượt xa cậu về kinh nghiệm.

<short pause> Về sau, truyện cho thấy năng lực Emperor Time của Kurapika còn phải trả giá bằng chính tuổi thọ của cậu mỗi khi dùng.

<short pause> Giao ước không chỉ là luật chơi. Nó là cái giá mà người dùng Nen chấp nhận trả để đổi lấy sức mạnh.

<short pause> <laugh> Kaku nhắc: giao ước càng đổi lấy thứ quý giá, sức mạnh càng lớn. Và không có thứ gì quý giá hơn tương lai của chính mình.

<short pause> Giờ quay lại câu hỏi ban đầu. Trong arc Kiến Chimera, Gon biết người thầy Kite của mình không thể cứu được nữa.

<short pause> Cơn giận và tuyệt vọng đẩy Gon đến một giao ước chưa từng có: đổi tất cả những gì mình có để có đủ sức mạnh ngay lúc đó.

<short pause> Cậu ép cơ thể lớn vượt tuổi, đạt tới sức mạnh mà lẽ ra phải cả đời tu luyện mới có, và đánh bại kẻ thù.

<short pause> Nhưng thứ bị đem ra đổi chính là tương lai: toàn bộ tiềm năng và Nen mà Gon lẽ ra sẽ có trong suốt cuộc đời.

<short pause> Gon suýt chết. Sau khi được cứu, cậu còn sống, nhưng khi nói chuyện với cha là Ging, Gon cho biết mình không dùng được Nen nữa.

<short pause> Chi tiết đáng chú ý: Ging vẫn thấy khí quanh Gon. Nghĩa là Gon không mất khí, mà mất khả năng cảm nhận và điều khiển nó.

<short pause> Theo luật giao ước, chuyện này hoàn toàn hợp lý: Gon đã trả trước toàn bộ tương lai, nên hiện tại không còn gì để dùng.

<short pause> Liệu Gon có lấy lại được Nen không? Truyện chưa trả lời chắc chắn. Nhiều fan tin là có, nhưng hiện tại đó vẫn chỉ là lý thuyết.
```

**ElevenLabs**

```text
Và giờ, phần quan trọng nhất để hiểu chuyện của Gon: giới hạn và giao ước.

[pause] Luật rất đơn giản: tự đặt ra điều kiện càng khắt khe cho năng lực của mình, năng lực đó càng mạnh.

[pause] Điều kiện có thể là 'chỉ dùng được với một loại kẻ thù', 'chỉ dùng khi đứng yên', hay 'nếu phá luật, ta sẽ chết'.

[pause] Kurapika là ví dụ kinh điển. Cậu tự thề sợi xích mạnh nhất chỉ được dùng với băng Ảo Ảnh, nếu dùng với người khác, chính cậu sẽ chết.

[pause] Nhờ giao ước khắc nghiệt đó, sợi xích đủ mạnh để trói những kẻ vượt xa cậu về kinh nghiệm.

[pause] Về sau, truyện cho thấy năng lực Emperor Time của Kurapika còn phải trả giá bằng chính tuổi thọ của cậu mỗi khi dùng.

[pause] Giao ước không chỉ là luật chơi. Nó là cái giá mà người dùng Nen chấp nhận trả để đổi lấy sức mạnh.

[pause] [chuckles] Kaku nhắc: giao ước càng đổi lấy thứ quý giá, sức mạnh càng lớn. Và không có thứ gì quý giá hơn tương lai của chính mình.

[pause] Giờ quay lại câu hỏi ban đầu. Trong arc Kiến Chimera, Gon biết người thầy Kite của mình không thể cứu được nữa.

[pause] Cơn giận và tuyệt vọng đẩy Gon đến một giao ước chưa từng có: đổi tất cả những gì mình có để có đủ sức mạnh ngay lúc đó.

[pause] Cậu ép cơ thể lớn vượt tuổi, đạt tới sức mạnh mà lẽ ra phải cả đời tu luyện mới có, và đánh bại kẻ thù.

[pause] Nhưng thứ bị đem ra đổi chính là tương lai: toàn bộ tiềm năng và Nen mà Gon lẽ ra sẽ có trong suốt cuộc đời.

[pause] Gon suýt chết. Sau khi được cứu, cậu còn sống, nhưng khi nói chuyện với cha là Ging, Gon cho biết mình không dùng được Nen nữa.

[pause] Chi tiết đáng chú ý: Ging vẫn thấy khí quanh Gon. Nghĩa là Gon không mất khí, mà mất khả năng cảm nhận và điều khiển nó.

[pause] Theo luật giao ước, chuyện này hoàn toàn hợp lý: Gon đã trả trước toàn bộ tương lai, nên hiện tại không còn gì để dùng.

[pause] [curious] Liệu Gon có lấy lại được Nen không? Truyện chưa trả lời chắc chắn. Nhiều fan tin là có, nhưng hiện tại đó vẫn chỉ là lý thuyết.
```

### c08 · Vì sao Nen được yêu thích?

Khoảng 119 giây · cảnh s87–s98 · 1543 ký tự

**Gemini**

```text
<laugh> Trước khi tổng kết, Kaku muốn bàn thêm một câu hỏi: vì sao rất nhiều fan xem Nen là hệ thống sức mạnh hay nhất trong anime?

<short pause> Lý do đầu tiên: Nen có luật rõ ràng. Người xem hiểu được giới hạn của từng nhân vật, nên khi ai đó thắng, chiến thắng đó có lý do.

<short pause> Ở nhiều bộ khác, nhân vật chính mạnh lên nhờ một cơn giận hay một cú bộc phát khó giải thích. Trong Hunter x Hunter, ngay cả cơn giận của Gon cũng phải trả giá theo luật.

<short pause> Lý do thứ hai: thông tin là vũ khí. Biết năng lực và điều kiện của đối phương quan trọng không kém sức mạnh thô.

<short pause> Vì thế nhiều trận đấu giống một ván bài lật ngửa dần: ai giấu được lá bài của mình lâu hơn, người đó có lợi thế.

<short pause> Lý do thứ ba: người yếu hơn vẫn có thể thắng. Một năng lực nhỏ nhưng thông minh, cộng với giao ước đúng, có thể lật đổ kẻ mạnh hơn nhiều.

<short pause> Điều này làm mỗi trận đấu khó đoán. Bạn không thể chỉ so ai có nhiều khí hơn, mà phải xem ai dùng khí thông minh hơn.

<short pause> Lý do thứ tư: Nen phản ánh tính cách. Năng lực của mỗi người nói lên họ là ai, họ mong muốn gì, và họ sẵn sàng hy sinh điều gì.

<short pause> Kurapika sống vì trả thù, nên năng lực của cậu là những sợi xích trói buộc và đổi bằng mạng sống. Gon sống thẳng thắn, nên năng lực của cậu là một cú đấm.

<short pause> Khi năng lực gắn với tính cách, trận đấu cũng là câu chuyện. Người xem không chỉ hỏi ai mạnh hơn, mà hỏi ai sẽ phải hy sinh điều gì.

<short pause> Và cuối cùng, Nen có giá. Không có sức mạnh nào miễn phí. Chính điều đó làm khoảnh khắc Gon biến đổi vừa đẹp, vừa đau.

<short pause> Kaku nghĩ đây là bài học lớn nhất của Nen: mọi thứ mạnh mẽ đều cần kỷ luật, lựa chọn đúng, và sẵn sàng trả giá.
```

**ElevenLabs**

```text
[chuckles] Trước khi tổng kết, Kaku muốn bàn thêm một câu hỏi: vì sao rất nhiều fan xem Nen là hệ thống sức mạnh hay nhất trong anime?

[pause] Lý do đầu tiên: Nen có luật rõ ràng. Người xem hiểu được giới hạn của từng nhân vật, nên khi ai đó thắng, chiến thắng đó có lý do.

[pause] Ở nhiều bộ khác, nhân vật chính mạnh lên nhờ một cơn giận hay một cú bộc phát khó giải thích. Trong Hunter x Hunter, ngay cả cơn giận của Gon cũng phải trả giá theo luật.

[pause] Lý do thứ hai: thông tin là vũ khí. Biết năng lực và điều kiện của đối phương quan trọng không kém sức mạnh thô.

[pause] Vì thế nhiều trận đấu giống một ván bài lật ngửa dần: ai giấu được lá bài của mình lâu hơn, người đó có lợi thế.

[pause] Lý do thứ ba: người yếu hơn vẫn có thể thắng. Một năng lực nhỏ nhưng thông minh, cộng với giao ước đúng, có thể lật đổ kẻ mạnh hơn nhiều.

[pause] Điều này làm mỗi trận đấu khó đoán. Bạn không thể chỉ so ai có nhiều khí hơn, mà phải xem ai dùng khí thông minh hơn.

[pause] Lý do thứ tư: Nen phản ánh tính cách. Năng lực của mỗi người nói lên họ là ai, họ mong muốn gì, và họ sẵn sàng hy sinh điều gì.

[pause] Kurapika sống vì trả thù, nên năng lực của cậu là những sợi xích trói buộc và đổi bằng mạng sống. Gon sống thẳng thắn, nên năng lực của cậu là một cú đấm.

[pause] Khi năng lực gắn với tính cách, trận đấu cũng là câu chuyện. Người xem không chỉ hỏi ai mạnh hơn, mà hỏi ai sẽ phải hy sinh điều gì.

[pause] Và cuối cùng, Nen có giá. Không có sức mạnh nào miễn phí. Chính điều đó làm khoảnh khắc Gon biến đổi vừa đẹp, vừa đau.

[pause] Kaku nghĩ đây là bài học lớn nhất của Nen: mọi thứ mạnh mẽ đều cần kỷ luật, lựa chọn đúng, và sẵn sàng trả giá.
```

### c09 · Tóm tắt

Khoảng 47 giây · cảnh s99–s104 · 607 ký tự

**Gemini**

```text
Tóm lại: khí là năng lượng sống. Bốn nguyên tắc để giữ, tắt, dồn và phát khí. Bảy kỹ năng nâng cao để chiến đấu.

<short pause> Sáu hệ trên hình lục giác quyết định bạn giỏi gì. Và giới hạn cùng giao ước cho phép đổi cái giá lấy sức mạnh.

<short pause> Chính vì mọi sức mạnh đều có luật và có giá, các trận đấu trong Hunter x Hunter mới căng thẳng như một ván cờ.

<short pause> Câu hỏi cho bạn: nếu tự làm bói nước, bạn nghĩ mình thuộc hệ nào, và bạn sẽ đặt giao ước gì cho năng lực của mình? Viết xuống phần bình luận nhé.

<short pause> Nếu video giúp bạn hiểu Nen rõ hơn, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã Haki trong One Piece.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: khí là năng lượng sống. Bốn nguyên tắc để giữ, tắt, dồn và phát khí. Bảy kỹ năng nâng cao để chiến đấu.

[pause] Sáu hệ trên hình lục giác quyết định bạn giỏi gì. Và giới hạn cùng giao ước cho phép đổi cái giá lấy sức mạnh.

[pause] Chính vì mọi sức mạnh đều có luật và có giá, các trận đấu trong Hunter x Hunter mới căng thẳng như một ván cờ.

[pause] [curious] Câu hỏi cho bạn: nếu tự làm bói nước, bạn nghĩ mình thuộc hệ nào, và bạn sẽ đặt giao ước gì cho năng lực của mình? Viết xuống phần bình luận nhé.

[pause] Nếu video giúp bạn hiểu Nen rõ hơn, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã Haki trong One Piece.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
