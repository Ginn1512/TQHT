# Bộ prompt · Dragon Ball: Nếu bạn tập một năm trong Phòng Thời Gian Tinh Thần

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (83 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Dragon Ball Z, arc Cell và arc Buu. Không có spoiler Dragon Ball Super.

```text
Wide 16:9 landscape cinematic frame. a vast glowing white void with a small domed building floating in the middle. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một ngày bên ngoài, một năm bên trong. Nếu bạn có một căn phòng như vậy, bạn sẽ làm gì với ba trăm sáu mươi l…

```text
Wide 16:9 landscape cinematic frame. a door standing alone in white emptiness, an hourglass beside it with sand flowing upward. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đó là Phòng Thời Gian Tinh Thần trong Dragon Ball. Hôm nay, người bước qua cánh cửa đó là bạn.

```text
Wide 16:9 landscape cinematic frame. a viewer silhouette stepping through a doorway into blinding white light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku, và hôm nay cuốn sổ là nhật ký tập luyện của bạn. Bạn bắt đầu với ba chỉ số: sức m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a training diary with three bars drawn on the first page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mỗi ba tháng trong phòng, bạn sẽ gặp một thử thách và phải chọn. Cuối năm, Kaku sẽ tính xem bạn mạnh lên bao…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a calendar with four seasons circled, a pencil behind its ear. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Căn phòng này là gì?

Lời: Phòng Thời Gian Tinh Thần nằm trong thần điện trên bầu trời, nơi ở của vị thần hộ mệnh Trái Đất. Chỉ những ng…

```text
Wide 16:9 landscape cinematic frame. a floating sky palace above the clouds, a small building on its edge with a single door. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Luật đầu tiên: thời gian bên trong trôi nhanh hơn bên ngoài rất nhiều. Một ngày ở thế giới bên ngoài bằng một…

```text
Wide 16:9 landscape cinematic frame. two clocks side by side, one barely moving and one spinning rapidly. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Luật thứ hai: mỗi lần chỉ nên có tối đa hai người trong phòng. Và mỗi người chỉ được dùng căn phòng tổng cộng…

```text
Wide 16:9 landscape cinematic frame. a door fading into nothing while a figure reaches for it too late. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Bên trong có một ngôi nhà nhỏ với giường, nhà tắm và kho đồ ăn. Bên ngoài ngôi nhà là một khoảng trắng mênh m…

```text
Wide 16:9 landscape cinematic frame. a small cozy building on the edge of endless white emptiness, footprints leading away into nothing. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong truyện, những người mạnh nhất đã dùng căn phòng này trước các trận đấu sinh tử. Nhưng họ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking nervously through the door into the white void. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Trước khi vào: mang theo gì?

Lời: Trước khi bước qua cánh cửa, hãy chuẩn bị hành lý. Bạn chỉ có một lần vào, nên đừng quên thứ gì quan trọng.

```text
Wide 16:9 landscape cinematic frame. an open backpack on the floor of a sky palace, items laid out neatly beside it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Đồ ăn thì không cần lo quá nhiều: trong phòng có kho thực phẩm, nhưng truyện cho thấy chúng khá đơn giản và n…

```text
Wide 16:9 landscape cinematic frame. a plain storeroom with sacks and jars, a tiny bottle of spice being slipped into a bag. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Quần áo cho cả hai thái cực: đồ mỏng cho lúc nóng năm mươi độ, và đồ thật dày cho lúc lạnh âm bốn mươi độ.

```text
Wide 16:9 landscape cinematic frame. a light shirt and a thick fur coat hanging side by side on hooks. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Một chiếc đồng hồ. Trong phòng không có ngày và đêm, nên không có đồng hồ, bạn sẽ mất cảm giác thời gian rất…

```text
Wide 16:9 landscape cinematic frame. a simple wristwatch lying on white ground, its ticking the only sign of time. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và một cuốn sổ. Ghi lại mỗi ngày mình đã tập gì và cảm thấy thế nào. Đó là cách để biết mình có đang tiến bộ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot tucking a notebook into the backpack carefully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Ngày đầu tiên: trọng lực

Lời: Bạn bước vào. Ngay lập tức, cơ thể nặng trĩu như bị đè xuống. Trọng lực trong phòng mạnh gấp mười lần Trái Đấ…

```text
Wide 16:9 landscape cinematic frame. a figure collapsing to one knee, the floor cracking slightly, heavy air distortion around them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nếu bạn nặng năm mươi ký, ở đây bạn sẽ cảm thấy như đang nặng năm trăm ký. Chỉ đứng dậy thôi cũng là một bài…

```text
Wide 16:9 landscape cinematic frame. a scale showing 50 kilograms turning into 500 kilograms with a dramatic crack. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Lựa chọn: A, lao vào tập nặng ngay từ ngày đầu để tận dụng thời gian. B, dành cả tháng đầu chỉ để làm quen: đ…

```text
Wide 16:9 landscape cinematic frame. two cards: a figure lifting a huge boulder, and a figure slowly walking with careful steps. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nếu chọn A: bạn bị chấn thương trong tuần đầu. Sức khỏe trừ ba mươi, sức mạnh chỉ cộng một chút. Nếu chọn B:…

```text
Wide 16:9 landscape cinematic frame. two diary entries: one with a bandaged arm and a small arrow, one with a steady rising arrow. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong truyện, ngay cả những chiến binh mạnh nhất cũng phải mất thời gian để di chuyển bình thườ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to take a step and flattening onto the floor like a pancake. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Tháng 1 đến 3: nóng, lạnh và không khí loãng

Lời: Qua được tuần đầu, bạn phát hiện thêm vài điều kinh khủng. Nhiệt độ trong phòng thay đổi dữ dội, từ nóng khoả…

```text
Wide 16:9 landscape cinematic frame. a split view of the white void: one side shimmering with heat haze, the other covered in frost. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Càng đi xa khỏi ngôi nhà, không khí càng loãng, giống như leo lên đỉnh một ngọn núi rất cao. Thở thôi cũng kh…

```text
Wide 16:9 landscape cinematic frame. a figure walking away from the small building, breath visible, the air getting visibly thinner. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Lựa chọn: A, tập luyện ngay trong điều kiện khắc nghiệt nhất, xa ngôi nhà. B, tập gần ngôi nhà, nơi nhiệt độ…

```text
Wide 16:9 landscape cinematic frame. two cards: a figure training alone far out in the frozen void, and one training near the building. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Nếu chọn A: tinh thần trừ hai mươi, sức khỏe trừ hai mươi, nhưng sức mạnh nhân thêm một phẩy năm lần. Nếu chọ…

```text
Wide 16:9 landscape cinematic frame. diary bars updating: one set dropping in health but rising in strength, another steady. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Trong truyện, chính các nhân vật mạnh nhất cũng phải nghỉ trong ngôi nhà để hồi sức sau những đợt tập ngoài k…

```text
Wide 16:9 landscape cinematic frame. a battered warrior resting on a simple bed inside the small building, bandages on his arms. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: khắc nghiệt hơn chưa chắc là tốt hơn. Nó chỉ tốt khi bạn còn đủ sức để đi hết cả năm.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wrapped in a blanket, sipping hot tea near a small window. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Tháng 4 đến 6: sự cô đơn

Lời: Giữa năm, thứ đáng sợ nhất không còn là trọng lực, mà là sự trống rỗng. Chỉ có màu trắng, không ngày, không đ…

```text
Wide 16:9 landscape cinematic frame. a tiny figure sitting alone in an endless white void, no horizon, no shadows. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Trong truyện, các nhân vật thường vào phòng theo cặp. Và có lý do: một người tập cùng giúp bạn giữ tinh thần,…

```text
Wide 16:9 landscape cinematic frame. two figures sparring in the white void, their shadows the only color around them. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Lựa chọn: A, vào một mình để tập trung tuyệt đối. B, rủ một người bạn vào cùng, dù sẽ phải chia thời gian và…

```text
Wide 16:9 landscape cinematic frame. two cards: a lone meditating figure, and two figures sharing a simple meal. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nếu chọn A: tinh thần trừ bốn mươi. Bạn bắt đầu nói chuyện với chính mình. Nếu chọn B: tinh thần cộng mười, v…

```text
Wide 16:9 landscape cinematic frame. diary bars: one showing a cracked mind icon, another showing two small smiling icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Có một cách khác để giữ tinh thần nếu vào một mình: tự đặt mục tiêu nhỏ mỗi tuần, và viết nhật ký như đang nó…

```text
Wide 16:9 landscape cinematic frame. a lone figure writing a letter in a notebook by lamplight in the white void. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong một thí nghiệm có thật tên là Mars-500, sáu người đã sống cách ly năm trăm hai mươi ngày…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small model of a sealed capsule labeled with a mission patch. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Tháng 7 đến 9: bức tường

Lời: Bước sang quý ba, bạn chạm vào bức tường mà mọi người tập luyện đều gặp: tiến bộ chậm lại, dù tập nhiều hơn.

```text
Wide 16:9 landscape cinematic frame. a figure punching a transparent wall in the white void, ripples but no cracks. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Trong truyện, ở arc Cell, có một cách giải bài toán này. Thay vì cố tạo ra dạng mạnh hơn, cha con Goku ở tron…

```text
Wide 16:9 landscape cinematic frame. a father and son figure with golden auras calmly eating a meal together in the void. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Trong khi đó, có người chọn hướng ngược lại: làm cơ bắp phình to để tăng sức mạnh thô. Dạng đó mạnh hơn, nhưn…

```text
Wide 16:9 landscape cinematic frame. a massively muscled figure swinging slowly while a smaller one dodges easily. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Lựa chọn: A, làm cơ bắp to hơn. B, luyện kiểm soát, để giữ sức mạnh hiện có mà tốn ít năng lượng nhất.

```text
Wide 16:9 landscape cinematic frame. two cards: a bulging muscular arm, and a calm steady hand with a small flame. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nếu chọn A: sức mạnh nhân một phẩy năm lần nhưng mất tốc độ, cuối năm bị chia đôi hiệu quả. Nếu chọn B: sức m…

```text
Wide 16:9 landscape cinematic frame. diary bars: a muscular icon with a slow snail, and a calm icon with a lightning bolt. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bài học này Kaku đã nhắc trong video xếp hạng Super Saiyan. Sức mạnh mà không dùng được thì khô…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small ranking ladder pinned to its diary. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Một ngày trong phòng của bạn

Lời: Trước khi tới quý cuối, hãy thử lên lịch một ngày lý tưởng trong phòng. Vì không có mặt trời, bạn phải tự tạo…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn daily schedule pinned to the wall of the small building. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Sáng: khởi động thật kỹ trong trọng lực gấp mười. Một cú trẹo chân ở đây có thể mất cả tháng để hồi phục.

```text
Wide 16:9 landscape cinematic frame. a figure stretching carefully on the white floor, a watch showing morning. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Trưa: tập nặng gần ngôi nhà, rồi thử đi xa hơn một chút mỗi ngày để làm quen với không khí loãng.

```text
Wide 16:9 landscape cinematic frame. footprints extending a little farther into the void each day, marked with small flags. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chiều: đấu tập với bạn đồng hành, và cùng ghi lại tiến bộ. Tối: ăn, trò chuyện, và ngủ đủ giấc, dù bên ngoài…

```text
Wide 16:9 landscape cinematic frame. two figures sharing a meal at a small table, a lamp glowing warmly in the white void. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nghe thì chán, nhưng lịch đều đặn chính là thứ giúp bạn không bị khoảng trắng nuốt mất.

```text
Wide 16:9 landscape cinematic frame. the owl mascot ticking boxes on a checklist with a pencil. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Tháng 10 đến 12: cánh cửa

Lời: Quý cuối cùng. Bạn đã mạnh hơn nhiều. Và một ý nghĩ nguy hiểm xuất hiện: nếu ở lại thêm vài tháng nữa thì sao?

```text
Wide 16:9 landscape cinematic frame. a figure standing in front of the only door, hand hesitating on the handle. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhớ luật: mỗi người chỉ được dùng căn phòng tổng cộng hai ngày trong đời. Bạn đã dùng một. Ở quá giới hạn, cá…

```text
Wide 16:9 landscape cinematic frame. a door with a small counter above it showing one day used out of two. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Lựa chọn: A, ra đúng hạn một năm. B, liều ở thêm, chấp nhận nguy cơ.

```text
Wide 16:9 landscape cinematic frame. two cards: an open door with daylight, and a door slowly fading. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nếu chọn A: bạn bước ra, thế giới bên ngoài mới chỉ qua một ngày. Nếu chọn B: bạn được thêm chút sức mạnh, nh…

```text
Wide 16:9 landscape cinematic frame. a figure stepping out into sunlight, and another pounding on a vanishing door in the void. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong arc Buu, căn phòng từng bị phá lối ra khi có người ở bên trong. Có kẻ thoát được bằng các…

```text
Wide 16:9 landscape cinematic frame. a crack of darkness ripping through the white void, a small figure covering its ears. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Kết quả của bạn

Lời: Giờ tính kết quả. Nhân các hệ số sức mạnh của bạn lại với nhau, và cộng trừ tinh thần, sức khỏe.

```text
Wide 16:9 landscape cinematic frame. a diary page full of calculations, arrows and small multiplier signs. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử chọn cẩn thận: làm quen trước, tập gần nhà, rủ bạn vào cùng, luyện kiểm soát, ra đúng hạn. Sức mạnh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly showing a diary page with a result of about 3.7 times. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Tinh thần của Kaku còn một trăm hai mươi, sức khỏe chín mươi. Không phải người mạnh nhất, nhưng bước ra khỏi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot stepping out of the door into sunlight, stretching happily. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nếu bạn chọn toàn phương án liều lĩnh, sức mạnh có thể cao hơn trên giấy, nhưng tinh thần và sức khỏe gần như…

```text
Wide 16:9 landscape cinematic frame. a figure staggering out of the door, exhausted, a huge number above their head flickering. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Còn một kiểu kết quả nữa: nếu bạn chọn vào một mình và ở quá hạn, tinh thần có thể xuống dưới không. Trong tr…

```text
Wide 16:9 landscape cinematic frame. an empty doorway in the white void, a lone figure sitting far away with its back turned. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kết quả của bạn là bao nhiêu? Viết ba chỉ số cuối năm của bạn vào phần bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. a blank diary page with three bars waiting to be filled in. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Ba hiểu lầm về căn phòng

Lời: Trước khi nói về khoa học, gỡ nhanh ba hiểu lầm về căn phòng này.

```text
Wide 16:9 landscape cinematic frame. three sticky notes on the door of the chamber, each with a red question mark. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Hiểu lầm một: người trong phòng không già đi. Sai. Họ vẫn sống trọn một năm, nên già đi một năm thật. Trong t…

```text
Wide 16:9 landscape cinematic frame. a young swordsman stepping out of the door with noticeably longer hair, friends staring. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Hiểu lầm hai: có thể vào bao nhiêu lần cũng được. Sai. Mỗi người chỉ có tổng cộng hai ngày trong đời, và đó l…

```text
Wide 16:9 landscape cinematic frame. a door with a counter showing a strict limit of two. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Hiểu lầm ba: căn phòng chỉ nhỏ như một phòng tập. Sai. Ngoài ngôi nhà nhỏ là một khoảng không trắng mênh mông…

```text
Wide 16:9 landscape cinematic frame. a figure walking endlessly into white emptiness, the building shrinking to a dot behind them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cả ba điều cho thấy căn phòng không phải phép màu miễn phí. Nó chỉ đổi thời gian lấy thời gian.

```text
Wide 16:9 landscape cinematic frame. the owl mascot exchanging a small hourglass for another identical one, shrugging. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Khoa học: nếu điều này là thật

Lời: Giờ đặt căn phòng này cạnh khoa học thật. Có ba điều thú vị.

```text
Wide 16:9 landscape cinematic frame. a lab notebook with three sticky notes, a small model of a white room on the desk. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Một: trọng lực gấp mười lần là không thể chịu nổi với người thường. Phi công chiến đấu, với bộ đồ đặc biệt, c…

```text
Wide 16:9 landscape cinematic frame. a fighter pilot in a special suit inside a centrifuge, a gauge showing about 9 G. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Hai: thời gian trôi khác nhau là có thật trong vật lý. Đồng hồ trên vệ tinh định vị chạy nhanh hơn đồng hồ tr…

```text
Wide 16:9 landscape cinematic frame. a satellite orbiting Earth with a tiny clock ticking slightly faster than one on the ground. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nhưng chênh lệch thật rất nhỏ, còn một ngày bằng một năm thì chỉ có trong truyện. Và trong vật lý, muốn thời…

```text
Wide 16:9 landscape cinematic frame. a black hole bending light around it, a tiny clock nearby barely ticking. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Ba: tập luyện thật cần nghỉ ngơi. Cơ bắp phát triển trong lúc hồi phục, không phải trong lúc tập. Tập liên tụ…

```text
Wide 16:9 landscape cinematic frame. a sleeping athlete with a glowing muscle diagram showing repair during rest. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Một điều nữa: ở trọng lực cao lâu ngày, tim và xương phải làm việc vất vả hơn nhiều. Ngược lại, phi hành gia…

```text
Wide 16:9 landscape cinematic frame. an astronaut floating in a space station exercising on a machine, a bone density chart beside them. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nên nếu ngoài đời có căn phòng này, lịch tập tốt nhất có lẽ là tập, ăn, ngủ, và nói chuyện với…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sleeping on a tiny bed with a dumbbell under its pillow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Những người từng bước vào

Lời: Cùng nhìn lại những lần căn phòng thay đổi câu chuyện Dragon Ball.

```text
Wide 16:9 landscape cinematic frame. a guest book with several signatures on a pedestal beside the door. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Trước trận đấu với Cell, Goku và con trai Gohan dùng căn phòng để làm quen với sức mạnh Super Saiyan. Chính t…

```text
Wide 16:9 landscape cinematic frame. a father and son sparring in the white void, golden auras flickering. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Vegeta và con trai đến từ tương lai cũng vào phòng, và mỗi người đi theo một hướng mạnh lên khác nhau, như ta…

```text
Wide 16:9 landscape cinematic frame. a proud warrior and a young swordsman training at opposite ends of the white void. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Ở arc Buu, căn phòng được dùng như một cái bẫy, với hy vọng nhốt kẻ thù bên trong. Nhưng kế hoạch không diễn…

```text
Wide 16:9 landscape cinematic frame. a pink smoke trail swirling inside the white void, a door crumbling behind it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và ở arc Buu, hai đứa trẻ cũng vào phòng, luyện tập trong dạng hợp thể, khi hai người nhập làm một chiến binh…

```text
Wide 16:9 landscape cinematic frame. two small children practicing a synchronized dance-like pose in the white void. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: căn phòng không tự làm ai mạnh lên. Nó chỉ cho bạn thêm thời gian. Ai dùng thời gian đó thế nào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small hourglass up to the light. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Góc nhìn của Kaku: thứ đắt nhất là thời gian · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu phải chọn một bài học từ căn phòng này, Kaku chọn điều này: thời gian là thứ đắt nhất, và ngay cả trong t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of calendars, looking at a single hourglass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hai ngày trong cả đời, tức hai năm. Luật đó khiến căn phòng không phải phép màu vô hạn, mà là một nguồn tài n…

```text
Wide 16:9 landscape cinematic frame. two glowing coins labeled with a day each, held carefully in a palm. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Các nhân vật không dùng nó để lười biếng. Họ vào khi thật sự cần, với một mục tiêu rõ ràng, và ra ngay khi đủ.

```text
Wide 16:9 landscape cinematic frame. a figure walking out of the door with a determined look, sunrise ahead. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Ngoài đời, ta không có căn phòng nào như vậy. Nhưng mỗi năm ta vẫn có ba trăm sáu mươi lăm ngày. Chỉ là không…

```text
Wide 16:9 landscape cinematic frame. a real-life desk with a calendar, a notebook and a cup of tea, sunlight through the window. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và giống như trong phòng, một năm ngoài đời cũng trôi qua nhanh hơn ta tưởng nếu không có mục tiêu. Ngày nào…

```text
Wide 16:9 landscape cinematic frame. a stack of identical calendar pages blurring together into a single sheet. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Kaku nghĩ, nếu coi mỗi năm như một lần vào phòng, có lẽ ta sẽ biết mình muốn mạnh lên ở điều gì.

```text
Wide 16:9 landscape cinematic frame. a diary with a new year's first page open, a pen waiting beside it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Kết

Lời: Tóm lại: một ngày bên ngoài bằng một năm bên trong, trọng lực gấp mười, nhiệt độ từ năm mươi tới âm bốn mươi…

```text
Wide 16:9 landscape cinematic frame. a summary board of the chamber's rules with small icons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Và người mạnh lên nhiều nhất không phải người liều nhất, mà là người biết làm quen, biết kiểm soát, có bạn đồ…

```text
Wide 16:9 landscape cinematic frame. a figure and a friend stepping out of the door together into sunlight. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có một năm trong căn phòng này, bạn sẽ dùng nó để luyện kỹ năng gì ngoài đời thật? Học m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a guitar, a language book and a pen, looking undecided. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tới, Kaku lại trải cuộn giấy thời gian, lần này là một nghìn năm lịch sử chú thuật của Jujutsu Kaisen,…

```text
Wide 16:9 landscape cinematic frame. an ancient scroll with a lantern-lit capital at one end and a modern city at the other. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Kaku bước ra khỏi phòng đây. Bên ngoài mới qua một ngày thôi. Hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving from the doorway, a single sun rising outside. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Căn phòng này là gì?

Khoảng 109 giây · cảnh s01–s10 · 1416 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Dragon Ball Z, arc Cell và arc Buu. Không có spoiler Dragon Ball Super.

<short pause> Một ngày bên ngoài, một năm bên trong. Nếu bạn có một căn phòng như vậy, bạn sẽ làm gì với ba trăm sáu mươi lăm ngày mà thế giới không hề biết?

<short pause> Đó là Phòng Thời Gian Tinh Thần trong Dragon Ball. Hôm nay, người bước qua cánh cửa đó là bạn.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku, và hôm nay cuốn sổ là nhật ký tập luyện của bạn. Bạn bắt đầu với ba chỉ số: sức mạnh gấp một lần, tinh thần một trăm, sức khỏe một trăm.

<short pause> Mỗi ba tháng trong phòng, bạn sẽ gặp một thử thách và phải chọn. Cuối năm, Kaku sẽ tính xem bạn mạnh lên bao nhiêu, và có còn đủ tỉnh táo để bước ra không.

<short pause> Phòng Thời Gian Tinh Thần nằm trong thần điện trên bầu trời, nơi ở của vị thần hộ mệnh Trái Đất. Chỉ những người được phép mới có thể bước vào.

<short pause> Luật đầu tiên: thời gian bên trong trôi nhanh hơn bên ngoài rất nhiều. Một ngày ở thế giới bên ngoài bằng một năm bên trong.

<short pause> Luật thứ hai: mỗi lần chỉ nên có tối đa hai người trong phòng. Và mỗi người chỉ được dùng căn phòng tổng cộng hai ngày trong cả đời. Vượt quá, cánh cửa sẽ biến mất và người đó bị kẹt vĩnh viễn.

<short pause> Bên trong có một ngôi nhà nhỏ với giường, nhà tắm và kho đồ ăn. Bên ngoài ngôi nhà là một khoảng trắng mênh mông, trông như không có giới hạn.

<short pause> Kaku ghi chú: trong truyện, những người mạnh nhất đã dùng căn phòng này trước các trận đấu sinh tử. <short pause> Nhưng họ cũng nói rằng ở trong đó không hề dễ chịu chút nào.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Dragon Ball Z, arc Cell và arc Buu. Không có spoiler Dragon Ball Super.

[pause] Một ngày bên ngoài, một năm bên trong. [curious] Nếu bạn có một căn phòng như vậy, bạn sẽ làm gì với ba trăm sáu mươi lăm ngày mà thế giới không hề biết?

[pause] Đó là Phòng Thời Gian Tinh Thần trong Dragon Ball. Hôm nay, người bước qua cánh cửa đó là bạn.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku, và hôm nay cuốn sổ là nhật ký tập luyện của bạn. Bạn bắt đầu với ba chỉ số: sức mạnh gấp một lần, tinh thần một trăm, sức khỏe một trăm.

[pause] Mỗi ba tháng trong phòng, bạn sẽ gặp một thử thách và phải chọn. Cuối năm, Kaku sẽ tính xem bạn mạnh lên bao nhiêu, và có còn đủ tỉnh táo để bước ra không.

[pause] Phòng Thời Gian Tinh Thần nằm trong thần điện trên bầu trời, nơi ở của vị thần hộ mệnh Trái Đất. Chỉ những người được phép mới có thể bước vào.

[pause] Luật đầu tiên: thời gian bên trong trôi nhanh hơn bên ngoài rất nhiều. Một ngày ở thế giới bên ngoài bằng một năm bên trong.

[pause] Luật thứ hai: mỗi lần chỉ nên có tối đa hai người trong phòng. Và mỗi người chỉ được dùng căn phòng tổng cộng hai ngày trong cả đời. Vượt quá, cánh cửa sẽ biến mất và người đó bị kẹt vĩnh viễn.

[pause] Bên trong có một ngôi nhà nhỏ với giường, nhà tắm và kho đồ ăn. Bên ngoài ngôi nhà là một khoảng trắng mênh mông, trông như không có giới hạn.

[pause] Kaku ghi chú: trong truyện, những người mạnh nhất đã dùng căn phòng này trước các trận đấu sinh tử. [pause] Nhưng họ cũng nói rằng ở trong đó không hề dễ chịu chút nào.
```

### c02 · Trước khi vào: mang theo gì? / Ngày đầu tiên: trọng lực

Khoảng 101 giây · cảnh s11–s20 · 1314 ký tự

**Gemini**

```text
Trước khi bước qua cánh cửa, hãy chuẩn bị hành lý. Bạn chỉ có một lần vào, nên đừng quên thứ gì quan trọng.

<short pause> Đồ ăn thì không cần lo quá nhiều: trong phòng có kho thực phẩm, nhưng truyện cho thấy chúng khá đơn giản và nhạt nhẽo. Mang thêm chút gia vị có lẽ là ý hay.

<short pause> Quần áo cho cả hai thái cực: đồ mỏng cho lúc nóng năm mươi độ, và đồ thật dày cho lúc lạnh âm bốn mươi độ.

<short pause> Một chiếc đồng hồ. Trong phòng không có ngày và đêm, nên không có đồng hồ, bạn sẽ mất cảm giác thời gian rất nhanh.

<short pause> Và một cuốn sổ. Ghi lại mỗi ngày mình đã tập gì và cảm thấy thế nào. Đó là cách để biết mình có đang tiến bộ không.

<short pause> Bạn bước vào. Ngay lập tức, cơ thể nặng trĩu như bị đè xuống. Trọng lực trong phòng mạnh gấp mười lần Trái Đất.

<short pause> Nếu bạn nặng năm mươi ký, ở đây bạn sẽ cảm thấy như đang nặng năm trăm ký. Chỉ đứng dậy thôi cũng là một bài tập.

<short pause> Lựa chọn: A, lao vào tập nặng ngay từ ngày đầu để tận dụng thời gian. B, dành cả tháng đầu chỉ để làm quen: đứng, đi, thở trong trọng lực mới.

<short pause> Nếu chọn A: bạn bị chấn thương trong tuần đầu. Sức khỏe trừ ba mươi, sức mạnh chỉ cộng một chút. Nếu chọn B: sức khỏe trừ mười, nhưng cơ thể thích nghi dần, và sức mạnh tăng lên gấp hai lần.

<short pause> <laugh> Kaku ghi chú: trong truyện, ngay cả những chiến binh mạnh nhất cũng phải mất thời gian để di chuyển bình thường trong căn phòng. Vội vàng ở đây là tự hại mình.
```

**ElevenLabs**

```text
Trước khi bước qua cánh cửa, hãy chuẩn bị hành lý. Bạn chỉ có một lần vào, nên đừng quên thứ gì quan trọng.

[pause] Đồ ăn thì không cần lo quá nhiều: trong phòng có kho thực phẩm, nhưng truyện cho thấy chúng khá đơn giản và nhạt nhẽo. Mang thêm chút gia vị có lẽ là ý hay.

[pause] Quần áo cho cả hai thái cực: đồ mỏng cho lúc nóng năm mươi độ, và đồ thật dày cho lúc lạnh âm bốn mươi độ.

[pause] Một chiếc đồng hồ. Trong phòng không có ngày và đêm, nên không có đồng hồ, bạn sẽ mất cảm giác thời gian rất nhanh.

[pause] Và một cuốn sổ. Ghi lại mỗi ngày mình đã tập gì và cảm thấy thế nào. Đó là cách để biết mình có đang tiến bộ không.

[pause] Bạn bước vào. Ngay lập tức, cơ thể nặng trĩu như bị đè xuống. Trọng lực trong phòng mạnh gấp mười lần Trái Đất.

[pause] Nếu bạn nặng năm mươi ký, ở đây bạn sẽ cảm thấy như đang nặng năm trăm ký. Chỉ đứng dậy thôi cũng là một bài tập.

[pause] Lựa chọn: A, lao vào tập nặng ngay từ ngày đầu để tận dụng thời gian. B, dành cả tháng đầu chỉ để làm quen: đứng, đi, thở trong trọng lực mới.

[pause] Nếu chọn A: bạn bị chấn thương trong tuần đầu. Sức khỏe trừ ba mươi, sức mạnh chỉ cộng một chút. Nếu chọn B: sức khỏe trừ mười, nhưng cơ thể thích nghi dần, và sức mạnh tăng lên gấp hai lần.

[pause] [chuckles] Kaku ghi chú: trong truyện, ngay cả những chiến binh mạnh nhất cũng phải mất thời gian để di chuyển bình thường trong căn phòng. Vội vàng ở đây là tự hại mình.
```

### c03 · Tháng 1 đến 3: nóng, lạnh và không khí loãng / Tháng 4 đến 6: sự cô đơn

Khoảng 140 giây · cảnh s21–s32 · 1819 ký tự

**Gemini**

```text
Qua được tuần đầu, bạn phát hiện thêm vài điều kinh khủng. Nhiệt độ trong phòng thay đổi dữ dội, từ nóng khoảng năm mươi độ C tới lạnh khoảng âm bốn mươi độ C.

<short pause> Càng đi xa khỏi ngôi nhà, không khí càng loãng, giống như leo lên đỉnh một ngọn núi rất cao. Thở thôi cũng khó.

<short pause> Lựa chọn: A, tập luyện ngay trong điều kiện khắc nghiệt nhất, xa ngôi nhà. B, tập gần ngôi nhà, nơi nhiệt độ và không khí dễ chịu hơn.

<short pause> Nếu chọn A: tinh thần trừ hai mươi, sức khỏe trừ hai mươi, nhưng sức mạnh nhân thêm một phẩy năm lần. Nếu chọn B: sức mạnh nhân một phẩy hai lần, tinh thần và sức khỏe giữ nguyên.

<short pause> Trong truyện, chính các nhân vật mạnh nhất cũng phải nghỉ trong ngôi nhà để hồi sức sau những đợt tập ngoài khoảng trắng. Không ai ở ngoài đó liên tục được.

<short pause> <laugh> Kaku ghi chú: khắc nghiệt hơn chưa chắc là tốt hơn. Nó chỉ tốt khi bạn còn đủ sức để đi hết cả năm.

<short pause> Giữa năm, thứ đáng sợ nhất không còn là trọng lực, mà là sự trống rỗng. Chỉ có màu trắng, không ngày, không đêm, không tiếng động.

<short pause> Trong truyện, các nhân vật thường vào phòng theo cặp. Và có lý do: một người tập cùng giúp bạn giữ tinh thần, cũng như giúp bạn biết mình đang tiến bộ hay đi lùi.

<short pause> Lựa chọn: A, vào một mình để tập trung tuyệt đối. B, rủ một người bạn vào cùng, dù sẽ phải chia thời gian và đồ ăn.

<short pause> Nếu chọn A: tinh thần trừ bốn mươi. Bạn bắt đầu nói chuyện với chính mình. Nếu chọn B: tinh thần cộng mười, và sức mạnh nhân thêm một phẩy hai lần nhờ có người đấu tập.

<short pause> Có một cách khác để giữ tinh thần nếu vào một mình: tự đặt mục tiêu nhỏ mỗi tuần, và viết nhật ký như đang nói chuyện với người mình quý. <short pause> Nhưng nó vẫn không thay được một người bạn thật.

<short pause> Kaku ghi chú: trong một thí nghiệm có thật tên là Mars-500, sáu người đã sống cách ly năm trăm hai mươi ngày để mô phỏng chuyến bay tới sao Hỏa. Giấc ngủ và tâm trạng của họ bị ảnh hưởng rõ rệt. Cô đơn là kẻ thù thật sự.
```

**ElevenLabs**

```text
Qua được tuần đầu, bạn phát hiện thêm vài điều kinh khủng. Nhiệt độ trong phòng thay đổi dữ dội, từ nóng khoảng năm mươi độ C tới lạnh khoảng âm bốn mươi độ C.

[pause] Càng đi xa khỏi ngôi nhà, không khí càng loãng, giống như leo lên đỉnh một ngọn núi rất cao. Thở thôi cũng khó.

[pause] Lựa chọn: A, tập luyện ngay trong điều kiện khắc nghiệt nhất, xa ngôi nhà. B, tập gần ngôi nhà, nơi nhiệt độ và không khí dễ chịu hơn.

[pause] Nếu chọn A: tinh thần trừ hai mươi, sức khỏe trừ hai mươi, nhưng sức mạnh nhân thêm một phẩy năm lần. Nếu chọn B: sức mạnh nhân một phẩy hai lần, tinh thần và sức khỏe giữ nguyên.

[pause] Trong truyện, chính các nhân vật mạnh nhất cũng phải nghỉ trong ngôi nhà để hồi sức sau những đợt tập ngoài khoảng trắng. Không ai ở ngoài đó liên tục được.

[pause] [chuckles] Kaku ghi chú: khắc nghiệt hơn chưa chắc là tốt hơn. Nó chỉ tốt khi bạn còn đủ sức để đi hết cả năm.

[pause] Giữa năm, thứ đáng sợ nhất không còn là trọng lực, mà là sự trống rỗng. Chỉ có màu trắng, không ngày, không đêm, không tiếng động.

[pause] Trong truyện, các nhân vật thường vào phòng theo cặp. Và có lý do: một người tập cùng giúp bạn giữ tinh thần, cũng như giúp bạn biết mình đang tiến bộ hay đi lùi.

[pause] Lựa chọn: A, vào một mình để tập trung tuyệt đối. B, rủ một người bạn vào cùng, dù sẽ phải chia thời gian và đồ ăn.

[pause] Nếu chọn A: tinh thần trừ bốn mươi. Bạn bắt đầu nói chuyện với chính mình. Nếu chọn B: tinh thần cộng mười, và sức mạnh nhân thêm một phẩy hai lần nhờ có người đấu tập.

[pause] Có một cách khác để giữ tinh thần nếu vào một mình: tự đặt mục tiêu nhỏ mỗi tuần, và viết nhật ký như đang nói chuyện với người mình quý. [pause] Nhưng nó vẫn không thay được một người bạn thật.

[pause] Kaku ghi chú: trong một thí nghiệm có thật tên là Mars-500, sáu người đã sống cách ly năm trăm hai mươi ngày để mô phỏng chuyến bay tới sao Hỏa. Giấc ngủ và tâm trạng của họ bị ảnh hưởng rõ rệt. Cô đơn là kẻ thù thật sự.
```

### c04 · Tháng 7 đến 9: bức tường / Một ngày trong phòng của bạn

Khoảng 112 giây · cảnh s33–s43 · 1450 ký tự

**Gemini**

```text
Bước sang quý ba, bạn chạm vào bức tường mà mọi người tập luyện đều gặp: tiến bộ chậm lại, dù tập nhiều hơn.

<short pause> Trong truyện, ở arc Cell, có một cách giải bài toán này. Thay vì cố tạo ra dạng mạnh hơn, cha con Goku ở trong trạng thái Super Saiyan suốt cả ngày, kể cả khi ăn và ngủ, để cơ thể quen hoàn toàn với nó.

<short pause> Trong khi đó, có người chọn hướng ngược lại: làm cơ bắp phình to để tăng sức mạnh thô. Dạng đó mạnh hơn, nhưng chậm tới mức không đánh trúng ai.

<short pause> Lựa chọn: A, làm cơ bắp to hơn. B, luyện kiểm soát, để giữ sức mạnh hiện có mà tốn ít năng lượng nhất.

<short pause> Nếu chọn A: sức mạnh nhân một phẩy năm lần nhưng mất tốc độ, cuối năm bị chia đôi hiệu quả. Nếu chọn B: sức mạnh nhân một phẩy ba lần, và tinh thần cộng mười vì bạn thấy mình làm chủ được cơ thể.

<short pause> <laugh> Kaku ghi chú: bài học này Kaku đã nhắc trong video xếp hạng Super Saiyan. Sức mạnh mà không dùng được thì không phải sức mạnh.

<short pause> Trước khi tới quý cuối, hãy thử lên lịch một ngày lý tưởng trong phòng. Vì không có mặt trời, bạn phải tự tạo nhịp sống cho mình.

<short pause> Sáng: khởi động thật kỹ trong trọng lực gấp mười. Một cú trẹo chân ở đây có thể mất cả tháng để hồi phục.

<short pause> Trưa: tập nặng gần ngôi nhà, rồi thử đi xa hơn một chút mỗi ngày để làm quen với không khí loãng.

<short pause> Chiều: đấu tập với bạn đồng hành, và cùng ghi lại tiến bộ. Tối: ăn, trò chuyện, và ngủ đủ giấc, dù bên ngoài cửa sổ vẫn chỉ là một màu trắng.

<short pause> Kaku ghi chú: nghe thì chán, nhưng lịch đều đặn chính là thứ giúp bạn không bị khoảng trắng nuốt mất.
```

**ElevenLabs**

```text
Bước sang quý ba, bạn chạm vào bức tường mà mọi người tập luyện đều gặp: tiến bộ chậm lại, dù tập nhiều hơn.

[pause] Trong truyện, ở arc Cell, có một cách giải bài toán này. Thay vì cố tạo ra dạng mạnh hơn, cha con Goku ở trong trạng thái Super Saiyan suốt cả ngày, kể cả khi ăn và ngủ, để cơ thể quen hoàn toàn với nó.

[pause] Trong khi đó, có người chọn hướng ngược lại: làm cơ bắp phình to để tăng sức mạnh thô. Dạng đó mạnh hơn, nhưng chậm tới mức không đánh trúng ai.

[pause] Lựa chọn: A, làm cơ bắp to hơn. B, luyện kiểm soát, để giữ sức mạnh hiện có mà tốn ít năng lượng nhất.

[pause] Nếu chọn A: sức mạnh nhân một phẩy năm lần nhưng mất tốc độ, cuối năm bị chia đôi hiệu quả. Nếu chọn B: sức mạnh nhân một phẩy ba lần, và tinh thần cộng mười vì bạn thấy mình làm chủ được cơ thể.

[pause] [chuckles] Kaku ghi chú: bài học này Kaku đã nhắc trong video xếp hạng Super Saiyan. Sức mạnh mà không dùng được thì không phải sức mạnh.

[pause] Trước khi tới quý cuối, hãy thử lên lịch một ngày lý tưởng trong phòng. Vì không có mặt trời, bạn phải tự tạo nhịp sống cho mình.

[pause] Sáng: khởi động thật kỹ trong trọng lực gấp mười. Một cú trẹo chân ở đây có thể mất cả tháng để hồi phục.

[pause] Trưa: tập nặng gần ngôi nhà, rồi thử đi xa hơn một chút mỗi ngày để làm quen với không khí loãng.

[pause] Chiều: đấu tập với bạn đồng hành, và cùng ghi lại tiến bộ. Tối: ăn, trò chuyện, và ngủ đủ giấc, dù bên ngoài cửa sổ vẫn chỉ là một màu trắng.

[pause] Kaku ghi chú: nghe thì chán, nhưng lịch đều đặn chính là thứ giúp bạn không bị khoảng trắng nuốt mất.
```

### c05 · Tháng 10 đến 12: cánh cửa / Kết quả của bạn

Khoảng 121 giây · cảnh s44–s54 · 1567 ký tự

**Gemini**

```text
Quý cuối cùng. Bạn đã mạnh hơn nhiều. Và một ý nghĩ nguy hiểm xuất hiện: nếu ở lại thêm vài tháng nữa thì sao?

<short pause> Nhớ luật: mỗi người chỉ được dùng căn phòng tổng cộng hai ngày trong đời. Bạn đã dùng một. Ở quá giới hạn, cánh cửa biến mất.

<short pause> Lựa chọn: A, ra đúng hạn một năm. B, liều ở thêm, chấp nhận nguy cơ.

<short pause> Nếu chọn A: bạn bước ra, thế giới bên ngoài mới chỉ qua một ngày. Nếu chọn B: bạn được thêm chút sức mạnh, nhưng tiêu hết giới hạn cả đời, và mạo hiểm bị kẹt mãi mãi. Kaku tính như tinh thần trừ năm mươi.

<short pause> <laugh> Kaku ghi chú: trong arc Buu, căn phòng từng bị phá lối ra khi có người ở bên trong. Có kẻ thoát được bằng cách hét tới mức xé toạc không gian. Bạn thì chắc không làm được đâu.

<short pause> Giờ tính kết quả. Nhân các hệ số sức mạnh của bạn lại với nhau, và cộng trừ tinh thần, sức khỏe.

<short pause> Kaku thử chọn cẩn thận: làm quen trước, tập gần nhà, rủ bạn vào cùng, luyện kiểm soát, ra đúng hạn. Sức mạnh gấp hai, nhân một phẩy hai, nhân một phẩy hai, nhân một phẩy ba, tức khoảng gấp ba phẩy bảy lần.

<short pause> Tinh thần của Kaku còn một trăm hai mươi, sức khỏe chín mươi. Không phải người mạnh nhất, nhưng bước ra khỏi phòng vẫn là chính mình.

<short pause> Nếu bạn chọn toàn phương án liều lĩnh, sức mạnh có thể cao hơn trên giấy, nhưng tinh thần và sức khỏe gần như cạn kiệt. Kaku khuyên bạn đọc lại luật về cánh cửa.

<short pause> Còn một kiểu kết quả nữa: nếu bạn chọn vào một mình và ở quá hạn, tinh thần có thể xuống dưới không. Trong trò chơi của Kaku, như vậy nghĩa là bạn không còn muốn bước ra nữa, và đó là kết cục đáng sợ nhất.

<short pause> Kết quả của bạn là bao nhiêu? Viết ba chỉ số cuối năm của bạn vào phần bình luận nhé.
```

**ElevenLabs**

```text
Quý cuối cùng. Bạn đã mạnh hơn nhiều. [curious] Và một ý nghĩ nguy hiểm xuất hiện: nếu ở lại thêm vài tháng nữa thì sao?

[pause] Nhớ luật: mỗi người chỉ được dùng căn phòng tổng cộng hai ngày trong đời. Bạn đã dùng một. Ở quá giới hạn, cánh cửa biến mất.

[pause] Lựa chọn: A, ra đúng hạn một năm. B, liều ở thêm, chấp nhận nguy cơ.

[pause] Nếu chọn A: bạn bước ra, thế giới bên ngoài mới chỉ qua một ngày. Nếu chọn B: bạn được thêm chút sức mạnh, nhưng tiêu hết giới hạn cả đời, và mạo hiểm bị kẹt mãi mãi. Kaku tính như tinh thần trừ năm mươi.

[pause] [chuckles] Kaku ghi chú: trong arc Buu, căn phòng từng bị phá lối ra khi có người ở bên trong. Có kẻ thoát được bằng cách hét tới mức xé toạc không gian. Bạn thì chắc không làm được đâu.

[pause] Giờ tính kết quả. Nhân các hệ số sức mạnh của bạn lại với nhau, và cộng trừ tinh thần, sức khỏe.

[pause] Kaku thử chọn cẩn thận: làm quen trước, tập gần nhà, rủ bạn vào cùng, luyện kiểm soát, ra đúng hạn. Sức mạnh gấp hai, nhân một phẩy hai, nhân một phẩy hai, nhân một phẩy ba, tức khoảng gấp ba phẩy bảy lần.

[pause] Tinh thần của Kaku còn một trăm hai mươi, sức khỏe chín mươi. Không phải người mạnh nhất, nhưng bước ra khỏi phòng vẫn là chính mình.

[pause] Nếu bạn chọn toàn phương án liều lĩnh, sức mạnh có thể cao hơn trên giấy, nhưng tinh thần và sức khỏe gần như cạn kiệt. Kaku khuyên bạn đọc lại luật về cánh cửa.

[pause] Còn một kiểu kết quả nữa: nếu bạn chọn vào một mình và ở quá hạn, tinh thần có thể xuống dưới không. Trong trò chơi của Kaku, như vậy nghĩa là bạn không còn muốn bước ra nữa, và đó là kết cục đáng sợ nhất.

[pause] Kết quả của bạn là bao nhiêu? Viết ba chỉ số cuối năm của bạn vào phần bình luận nhé.
```

### c06 · Ba hiểu lầm về căn phòng / Khoa học: nếu điều này là thật

Khoảng 148 giây · cảnh s55–s66 · 1922 ký tự

**Gemini**

```text
Trước khi nói về khoa học, gỡ nhanh ba hiểu lầm về căn phòng này.

<short pause> Hiểu lầm một: người trong phòng không già đi. Sai. Họ vẫn sống trọn một năm, nên già đi một năm thật. Trong truyện, có người bước ra với mái tóc dài hẳn ra.

<short pause> Hiểu lầm hai: có thể vào bao nhiêu lần cũng được. Sai. Mỗi người chỉ có tổng cộng hai ngày trong đời, và đó là lý do các nhân vật dùng nó rất dè dặt.

<short pause> Hiểu lầm ba: căn phòng chỉ nhỏ như một phòng tập. Sai. Ngoài ngôi nhà nhỏ là một khoảng không trắng mênh mông, rộng tới mức đi mãi cũng không thấy tường.

<short pause> <laugh> Kaku ghi chú: cả ba điều cho thấy căn phòng không phải phép màu miễn phí. Nó chỉ đổi thời gian lấy thời gian.

<short pause> Giờ đặt căn phòng này cạnh khoa học thật. Có ba điều thú vị.

<short pause> Một: trọng lực gấp mười lần là không thể chịu nổi với người thường. Phi công chiến đấu, với bộ đồ đặc biệt, chỉ chịu được khoảng chín lần trọng lực trong vài giây. Chịu gấp mười suốt một năm thì cơ thể người thật không thể tồn tại.

<short pause> Hai: thời gian trôi khác nhau là có thật trong vật lý. Đồng hồ trên vệ tinh định vị chạy nhanh hơn đồng hồ trên mặt đất khoảng ba mươi tám phần triệu giây mỗi ngày, và kỹ sư phải tính tới điều đó.

<short pause> Nhưng chênh lệch thật rất nhỏ, còn một ngày bằng một năm thì chỉ có trong truyện. Và trong vật lý, muốn thời gian trôi chậm hơn, ta phải ở gần một vật cực nặng như lỗ đen, chứ không phải bước qua một cánh cửa.

<short pause> Ba: tập luyện thật cần nghỉ ngơi. Cơ bắp phát triển trong lúc hồi phục, không phải trong lúc tập. Tập liên tục không nghỉ suốt một năm thường dẫn tới chấn thương, không phải sức mạnh.

<short pause> Một điều nữa: ở trọng lực cao lâu ngày, tim và xương phải làm việc vất vả hơn nhiều. Ngược lại, phi hành gia sống lâu ngoài không gian với trọng lực gần bằng không thì bị mất khối lượng xương và cơ. Cơ thể người được thiết kế cho đúng trọng lực Trái Đất.

<short pause> Kaku ghi chú: nên nếu ngoài đời có căn phòng này, lịch tập tốt nhất có lẽ là tập, ăn, ngủ, và nói chuyện với bạn tập. Giống hệt những gì các nhân vật đã làm.
```

**ElevenLabs**

```text
Trước khi nói về khoa học, gỡ nhanh ba hiểu lầm về căn phòng này.

[pause] Hiểu lầm một: người trong phòng không già đi. Sai. Họ vẫn sống trọn một năm, nên già đi một năm thật. Trong truyện, có người bước ra với mái tóc dài hẳn ra.

[pause] Hiểu lầm hai: có thể vào bao nhiêu lần cũng được. Sai. Mỗi người chỉ có tổng cộng hai ngày trong đời, và đó là lý do các nhân vật dùng nó rất dè dặt.

[pause] Hiểu lầm ba: căn phòng chỉ nhỏ như một phòng tập. Sai. Ngoài ngôi nhà nhỏ là một khoảng không trắng mênh mông, rộng tới mức đi mãi cũng không thấy tường.

[pause] [chuckles] Kaku ghi chú: cả ba điều cho thấy căn phòng không phải phép màu miễn phí. Nó chỉ đổi thời gian lấy thời gian.

[pause] Giờ đặt căn phòng này cạnh khoa học thật. Có ba điều thú vị.

[pause] Một: trọng lực gấp mười lần là không thể chịu nổi với người thường. Phi công chiến đấu, với bộ đồ đặc biệt, chỉ chịu được khoảng chín lần trọng lực trong vài giây. Chịu gấp mười suốt một năm thì cơ thể người thật không thể tồn tại.

[pause] Hai: thời gian trôi khác nhau là có thật trong vật lý. Đồng hồ trên vệ tinh định vị chạy nhanh hơn đồng hồ trên mặt đất khoảng ba mươi tám phần triệu giây mỗi ngày, và kỹ sư phải tính tới điều đó.

[pause] Nhưng chênh lệch thật rất nhỏ, còn một ngày bằng một năm thì chỉ có trong truyện. Và trong vật lý, muốn thời gian trôi chậm hơn, ta phải ở gần một vật cực nặng như lỗ đen, chứ không phải bước qua một cánh cửa.

[pause] Ba: tập luyện thật cần nghỉ ngơi. Cơ bắp phát triển trong lúc hồi phục, không phải trong lúc tập. Tập liên tục không nghỉ suốt một năm thường dẫn tới chấn thương, không phải sức mạnh.

[pause] Một điều nữa: ở trọng lực cao lâu ngày, tim và xương phải làm việc vất vả hơn nhiều. Ngược lại, phi hành gia sống lâu ngoài không gian với trọng lực gần bằng không thì bị mất khối lượng xương và cơ. Cơ thể người được thiết kế cho đúng trọng lực Trái Đất.

[pause] Kaku ghi chú: nên nếu ngoài đời có căn phòng này, lịch tập tốt nhất có lẽ là tập, ăn, ngủ, và nói chuyện với bạn tập. Giống hệt những gì các nhân vật đã làm.
```

### c07 · Những người từng bước vào / Góc nhìn của Kaku: thứ đắt nhất là thời gian

Khoảng 125 giây · cảnh s67–s78 · 1620 ký tự

**Gemini**

```text
Cùng nhìn lại những lần căn phòng thay đổi câu chuyện Dragon Ball.

<short pause> Trước trận đấu với Cell, Goku và con trai Gohan dùng căn phòng để làm quen với sức mạnh Super Saiyan. Chính thời gian đó giúp Gohan sau này vượt qua giới hạn của mình.

<short pause> Vegeta và con trai đến từ tương lai cũng vào phòng, và mỗi người đi theo một hướng mạnh lên khác nhau, như ta đã nói ở quý ba.

<short pause> Ở arc Buu, căn phòng được dùng như một cái bẫy, với hy vọng nhốt kẻ thù bên trong. <short pause> Nhưng kế hoạch không diễn ra như mong đợi.

<short pause> Và ở arc Buu, hai đứa trẻ cũng vào phòng, luyện tập trong dạng hợp thể, khi hai người nhập làm một chiến binh mạnh hơn nhiều, để kịp đối đầu với kẻ thù. Căn phòng không chỉ dành cho người lớn.

<short pause> <laugh> Kaku ghi chú: căn phòng không tự làm ai mạnh lên. Nó chỉ cho bạn thêm thời gian. Ai dùng thời gian đó thế nào mới là điều quyết định.

<short pause> Nếu phải chọn một bài học từ căn phòng này, Kaku chọn điều này: thời gian là thứ đắt nhất, và ngay cả trong truyện, nó cũng có giới hạn.

<short pause> Hai ngày trong cả đời, tức hai năm. Luật đó khiến căn phòng không phải phép màu vô hạn, mà là một nguồn tài nguyên quý giá phải cân nhắc khi dùng.

<short pause> Các nhân vật không dùng nó để lười biếng. Họ vào khi thật sự cần, với một mục tiêu rõ ràng, và ra ngay khi đủ.

<short pause> Ngoài đời, ta không có căn phòng nào như vậy. <short pause> Nhưng mỗi năm ta vẫn có ba trăm sáu mươi lăm ngày. Chỉ là không ai đếm hộ ta, và cánh cửa thì không bao giờ mở lại.

<short pause> Và giống như trong phòng, một năm ngoài đời cũng trôi qua nhanh hơn ta tưởng nếu không có mục tiêu. Ngày nào cũng giống ngày nào thì cả năm cũng chỉ như một ngày.

<short pause> Kaku nghĩ, nếu coi mỗi năm như một lần vào phòng, có lẽ ta sẽ biết mình muốn mạnh lên ở điều gì.
```

**ElevenLabs**

```text
Cùng nhìn lại những lần căn phòng thay đổi câu chuyện Dragon Ball.

[pause] Trước trận đấu với Cell, Goku và con trai Gohan dùng căn phòng để làm quen với sức mạnh Super Saiyan. Chính thời gian đó giúp Gohan sau này vượt qua giới hạn của mình.

[pause] Vegeta và con trai đến từ tương lai cũng vào phòng, và mỗi người đi theo một hướng mạnh lên khác nhau, như ta đã nói ở quý ba.

[pause] Ở arc Buu, căn phòng được dùng như một cái bẫy, với hy vọng nhốt kẻ thù bên trong. [pause] Nhưng kế hoạch không diễn ra như mong đợi.

[pause] Và ở arc Buu, hai đứa trẻ cũng vào phòng, luyện tập trong dạng hợp thể, khi hai người nhập làm một chiến binh mạnh hơn nhiều, để kịp đối đầu với kẻ thù. Căn phòng không chỉ dành cho người lớn.

[pause] [chuckles] Kaku ghi chú: căn phòng không tự làm ai mạnh lên. Nó chỉ cho bạn thêm thời gian. Ai dùng thời gian đó thế nào mới là điều quyết định.

[pause] Nếu phải chọn một bài học từ căn phòng này, Kaku chọn điều này: thời gian là thứ đắt nhất, và ngay cả trong truyện, nó cũng có giới hạn.

[pause] Hai ngày trong cả đời, tức hai năm. Luật đó khiến căn phòng không phải phép màu vô hạn, mà là một nguồn tài nguyên quý giá phải cân nhắc khi dùng.

[pause] Các nhân vật không dùng nó để lười biếng. Họ vào khi thật sự cần, với một mục tiêu rõ ràng, và ra ngay khi đủ.

[pause] Ngoài đời, ta không có căn phòng nào như vậy. [pause] Nhưng mỗi năm ta vẫn có ba trăm sáu mươi lăm ngày. Chỉ là không ai đếm hộ ta, và cánh cửa thì không bao giờ mở lại.

[pause] Và giống như trong phòng, một năm ngoài đời cũng trôi qua nhanh hơn ta tưởng nếu không có mục tiêu. Ngày nào cũng giống ngày nào thì cả năm cũng chỉ như một ngày.

[pause] Kaku nghĩ, nếu coi mỗi năm như một lần vào phòng, có lẽ ta sẽ biết mình muốn mạnh lên ở điều gì.
```

### c08 · Kết

Khoảng 55 giây · cảnh s79–s83 · 711 ký tự

**Gemini**

```text
Tóm lại: một ngày bên ngoài bằng một năm bên trong, trọng lực gấp mười, nhiệt độ từ năm mươi tới âm bốn mươi độ, không khí loãng, tối đa hai ngày trong cả đời.

<short pause> Và người mạnh lên nhiều nhất không phải người liều nhất, mà là người biết làm quen, biết kiểm soát, có bạn đồng hành, và biết lúc nào nên bước ra.

<short pause> Câu hỏi cho bạn: nếu có một năm trong căn phòng này, bạn sẽ dùng nó để luyện kỹ năng gì ngoài đời thật? Học một ngôn ngữ, chơi một nhạc cụ, hay viết một cuốn sách?

<short pause> Video tới, Kaku lại trải cuộn giấy thời gian, lần này là một nghìn năm lịch sử chú thuật của Jujutsu Kaisen, từ thời Heian tới hiện tại.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. <laugh> Kaku bước ra khỏi phòng đây. Bên ngoài mới qua một ngày thôi. Hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: một ngày bên ngoài bằng một năm bên trong, trọng lực gấp mười, nhiệt độ từ năm mươi tới âm bốn mươi độ, không khí loãng, tối đa hai ngày trong cả đời.

[pause] Và người mạnh lên nhiều nhất không phải người liều nhất, mà là người biết làm quen, biết kiểm soát, có bạn đồng hành, và biết lúc nào nên bước ra.

[pause] [curious] Câu hỏi cho bạn: nếu có một năm trong căn phòng này, bạn sẽ dùng nó để luyện kỹ năng gì ngoài đời thật? Học một ngôn ngữ, chơi một nhạc cụ, hay viết một cuốn sách?

[pause] Video tới, Kaku lại trải cuộn giấy thời gian, lần này là một nghìn năm lịch sử chú thuật của Jujutsu Kaisen, từ thời Heian tới hiện tại.

[pause] Đăng ký kênh để không bỏ lỡ nhé. [chuckles] Kaku bước ra khỏi phòng đây. Bên ngoài mới qua một ngày thôi. Hẹn gặp lại!
```
