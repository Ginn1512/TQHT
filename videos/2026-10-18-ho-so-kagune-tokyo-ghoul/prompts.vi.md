# Bộ prompt · Tokyo Ghoul: Hồ sơ 4 loại Kagune và vòng khắc chế

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 87 ảnh, 8 đoạn đọc, khoảng 14.9 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (87 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Tokyo Ghoul tới hết anime mùa một, và nhắc ngắn vài khái niệm xuất hiện sau đó như…

```text
Wide 16:9 landscape cinematic frame. a dim archive room with rows of metal filing cabinets, a single desk lamp lighting a closed notebook, wide establishing shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hồ sơ số ba mươi bảy. Loại tài liệu: vũ khí sinh học. Mức độ nguy hiểm: cao. Nguồn gốc: cơ thể của những sinh…

```text
Wide 16:9 landscape cinematic frame. a thick case file stamped with a red crest being slid across a steel desk, close-up, harsh overhead light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trong Tokyo Ghoul, ngạ quỷ sống lẫn giữa người thường ở Tokyo. Họ đi học, đi làm, uống cà phê. Nhưng khi cần…

```text
Wide 16:9 landscape cinematic frame. a quiet café with ordinary customers, one person's shadow on the wall showing strange flowing shapes rising from the back, medium shot, warm interior light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Thứ vũ khí đó gọi là Kagune. Và không phải Kagune nào cũng giống nhau. Có bốn loại, mỗi loại mọc ra từ một vị…

```text
Wide 16:9 landscape cinematic frame. four silhouettes standing in a row, each with a different abstract glowing shape emerging from a different part of the back, wide shot, crimson and navy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Tokyo Ghoul là manga của tác giả Ishida Sui, ra mắt năm 2011 và được chuyển thể anime từ năm 2014. Nhân vật c…

```text
Wide 16:9 landscape cinematic frame. a shy university student reading a novel on a park bench under autumn trees, a quiet city behind him, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói trước: đây là một bộ truyện u tối. Kaku sẽ giữ video ở mức phân tích hệ thống, không đi vào nhữ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling a small curtain over a dark corner of the notebook page, serious but gentle expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở tủ hồ sơ Kagune. Mỗi hồ sơ ghi theo cùng một thứ tự: tên, vị trí,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny archivist's visor, pulling a folder out of a cabinet with great seriousness. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Cuối video là bảng khắc chế giữa bốn loại, giống như trò oẳn tù tì, và một mục lục để bạn tự đoán Kagune của…

```text
Wide 16:9 landscape cinematic frame. a circular diagram with four icons connected by arrows like a rock paper scissors cycle, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · Ngạ quỷ là ai

Lời: Trước khi mở hồ sơ, cần hiểu cơ thể ngạ quỷ. Họ giống người về ngoại hình, nhưng hệ tiêu hóa không nhận được…

```text
Wide 16:9 landscape cinematic frame. a plate of ordinary food untouched on a table, a person sitting before it looking pale and unwell, medium shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Quán Anteiku trong truyện là nơi trú ẩn của những ngạ quỷ muốn sống yên ổn, không săn người. Họ giúp nhau tồn…

```text
Wide 16:9 landscape cinematic frame. a cozy old café with warm lamps and wooden furniture at night, a few quiet customers and a gentle elderly owner behind the counter, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Có một ngoại lệ dễ thương hiếm hoi: cà phê. Ngạ quỷ uống được cà phê, nên quán cà phê trở thành nơi tụ họp củ…

```text
Wide 16:9 landscape cinematic frame. a steaming cup of black coffee on a wooden café counter, warm soft light, extreme close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Trong cơ thể họ có một loại tế bào đặc biệt gọi là tế bào RC, nhiều hơn người thường rất nhiều. Tế bào này gi…

```text
Wide 16:9 landscape cinematic frame. a stylized microscope view of glowing red cells flowing like liquid, diagram style, crimson and navy. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Da của ngạ quỷ cứng tới mức dao kéo và đạn thường gần như không làm gì được. Vì vậy con người phải dùng tới v…

```text
Wide 16:9 landscape cinematic frame. a broken ordinary knife blade lying next to an unharmed hand, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: CCG còn đặt những cổng kiểm tra ở một số nơi trong thành phố. Cổng đo lượng tế bào RC của người đi qua. Ngạ q…

```text
Wide 16:9 landscape cinematic frame. a security gate at a subway entrance glowing red as a person walks through, alarm light flashing, medium shot, cold fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Tức là trong thế giới này, một con số trong máu có thể quyết định bạn là công dân hay là con mồi.

```text
Wide 16:9 landscape cinematic frame. a blood test result sheet with a single number highlighted in red, extreme close-up, harsh clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Tổ chức săn ngạ quỷ tên là CCG. Họ chế tạo vũ khí gọi là Quinque từ những cơ quan Kagune thu được. Nghĩa là c…

```text
Wide 16:9 landscape cinematic frame. a metal briefcase opening to reveal a strange organic-looking weapon folded inside, medium shot, harsh clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là thế giới mà ranh giới giữa kẻ săn và con mồi rất mờ. Và chính sự mờ nhạt đó là linh hồn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a blurry line between two words on a chalkboard, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Kagune hình thành thế nào

Lời: Tế bào RC được dự trữ trong một cơ quan gọi là Kakuhou. Khi chiến đấu, ngạ quỷ giải phóng tế bào từ cơ quan n…

```text
Wide 16:9 landscape cinematic frame. an anatomical silhouette with a glowing organ near the spine, streams of red liquid flowing out and hardening into solid shapes, diagram style. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nhưng mỗi Kagune lại có hình dạng riêng, như vân tay. Hai người cùng loại Ukaku có thể có đôi cánh rất khác n…

```text
Wide 16:9 landscape cinematic frame. two winged silhouettes side by side, one with small sharp crystal wings and one with wide flowing wings, comparison shot, crimson light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Vị trí của Kakuhou quyết định loại Kagune. Và mỗi ngạ quỷ sinh ra với một loại, không đổi được. Giống như nhó…

```text
Wide 16:9 landscape cinematic frame. a back silhouette with four marked zones: shoulders, shoulder blades, lower back and tailbone, each with a small label icon, parchment diagram. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Khi Kagune xuất hiện, mắt ngạ quỷ cũng đổi màu: lòng trắng chuyển đen, con ngươi chuyển đỏ. Đây là dấu hiệu d…

```text
Wide 16:9 landscape cinematic frame. an extreme close-up of a stylized eye with a dark sclera and a glowing crimson iris, dramatic shadow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kagune rất mạnh, nhưng nó tiêu hao tế bào RC. Dùng càng nhiều, càng phải ăn để bù lại. Nghĩa là sức mạnh của…

```text
Wide 16:9 landscape cinematic frame. an empty glass slowly draining of glowing red liquid, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Giờ ta mở bốn hồ sơ, theo thứ tự từ vai xuống tới đuôi.

```text
Wide 16:9 landscape cinematic frame. four folders fanned out on a desk, each with a small icon: a feather, a shield, a tentacle, a tail, top-down shot, lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Hồ sơ 1: Ukaku

Lời: Hồ sơ số một: Ukaku, nghĩa là loại lông vũ. Vị trí: vùng vai. Hình dạng: như đôi cánh hoặc một chùm lông tỏa…

```text
Wide 16:9 landscape cinematic frame. a figure with glowing translucent feather-like wings spreading from the shoulders, silhouetted against a night sky, low-angle shot, crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Điểm mạnh thứ nhất: tốc độ. Ukaku là loại nhanh nhất trong bốn loại.

```text
Wide 16:9 landscape cinematic frame. a blurred figure dashing across rooftops leaving a trail of light feathers, dynamic wide shot, night city light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Điểm mạnh thứ hai: tấn công từ xa. Người dùng có thể bắn ra những mảnh tinh thể sắc như mưa đạn.

```text
Wide 16:9 landscape cinematic frame. a rain of crystal shards fired from glowing wings toward a distant target, dynamic shot, crimson highlights. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Điểm yếu: sức bền kém. Ukaku tiêu tế bào RC rất nhanh, nên người dùng mệt nhanh. Họ phải thắng nhanh, hoặc kh…

```text
Wide 16:9 landscape cinematic frame. a figure kneeling and panting on a rooftop, wings flickering and fading, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Em trai của cô, Ayato, cũng mang Ukaku. Hai chị em cùng một loại nhưng chọn hai con đường khác nhau: một ngườ…

```text
Wide 16:9 landscape cinematic frame. two young silhouettes with similar wings standing on opposite sides of a dark street, one near a warm café door, the other near a shadowy alley, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Kaku thấy chi tiết này rất đúng tinh thần bộ truyện: Kagune quyết định cách bạn chiến đấu, không quyết định b…

```text
Wide 16:9 landscape cinematic frame. two identical feather icons on a page with two very different paths drawn from them, parchment diagram, amber ink. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Người mang: Kirishima Touka, cô gái làm ở quán cà phê Anteiku. Cô chiến đấu nhanh, dữ dội, và thường muốn kết…

```text
Wide 16:9 landscape cinematic frame. a young woman silhouette in a café apron standing in a dark alley, faint glowing wings forming behind her shoulders, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu Kagune là môn thể thao, Ukaku chính là vận động viên chạy nước rút. Rất nhanh, rất đẹp, như…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a stopwatch at a tiny running track, a feather icon sprinting past. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Hồ sơ 2: Koukaku

Lời: Hồ sơ số hai: Koukaku, nghĩa là loại giáp. Vị trí: ngay dưới xương bả vai. Hình dạng: cứng và nặng, như tấm k…

```text
Wide 16:9 landscape cinematic frame. a figure holding a massive armored organic blade that extends from below the shoulder blade, heavy stance, low-angle shot, crimson and steel light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Điểm mạnh: phòng thủ tốt nhất. Kagune loại này cứng tới mức có thể dùng làm khiên, chặn gần như mọi đòn tấn c…

```text
Wide 16:9 landscape cinematic frame. a large shield-like armored shape blocking a storm of crystal shards, sparks flying off its surface, dynamic close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Điểm yếu: nặng và chậm. Mật độ tế bào dày khiến Kagune khó điều khiển nhanh. Người dùng thường chiến đấu như…

```text
Wide 16:9 landscape cinematic frame. a slow heavy figure lumbering forward while a lighter opponent circles around, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Koukaku còn có thể đổi hình dạng trong trận: lúc thì dựng thành khiên, lúc thì xoắn lại thành mũi khoan. Ngườ…

```text
Wide 16:9 landscape cinematic frame. an armored organic shape shifting from a flat shield into a spiraling drill point, sequential illustration, crimson and steel. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mà có Koukaku thì chắc chỉ dùng làm ô che mưa. Mà ô nặng quá thì cũng thôi, Kaku ở nhà đọc sách.

```text
Wide 16:9 landscape cinematic frame. the owl mascot struggling to hold up a heavy armored umbrella in the rain, comic expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Người mang: Tsukiyama Shuu, quý ông lịch lãm có sở thích ẩm thực kỳ quặc. Kagune của anh có dạng một lưỡi kiế…

```text
Wide 16:9 landscape cinematic frame. an elegant man silhouette in a tailored suit holding a long spiraling organic blade, theatrical pose, spotlight lighting. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Kaku ghi chú: Koukaku là thủ môn của đội. Chạy thì không nhanh, nhưng muốn qua mặt thì rất khó.

```text
Wide 16:9 landscape cinematic frame. a small goalkeeper silhouette with an enormous shield standing in a goal, humorous illustration, parchment style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Hồ sơ 3: Rinkaku

Lời: Hồ sơ số ba: Rinkaku, nghĩa là loại vảy. Vị trí: vùng thắt lưng. Hình dạng: những xúc tu dài, mềm dẻo, có thể…

```text
Wide 16:9 landscape cinematic frame. a silhouette with several long glowing tentacle-like shapes rising from the lower back, curling in the air, low-angle shot, crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điểm mạnh thứ nhất: sức công phá. Mỗi xúc tu có thể đâm xuyên hoặc đập vỡ bê tông.

```text
Wide 16:9 landscape cinematic frame. a tentacle-like shape smashing through a concrete wall, debris flying, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Điểm mạnh thứ hai: hồi phục. Rinkaku có khả năng tái tạo mạnh nhất, nên người dùng thường rất khó bị hạ.

```text
Wide 16:9 landscape cinematic frame. a wound closing rapidly as glowing red cells knit together, extreme close-up, stylized. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Điểm yếu: cấu trúc liên kết yếu, dễ bị cắt đứt. Và người ta hay nói những người mang Rinkaku thường có tâm lý…

```text
Wide 16:9 landscape cinematic frame. a tentacle-like shape cleanly severed and falling apart, beside a small label tag reading fan observation, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Số lượng xúc tu cũng khác nhau ở mỗi người. Kaneki lúc đầu chỉ có một vài xúc tu, và gần như không điều khiển…

```text
Wide 16:9 landscape cinematic frame. a young man clutching his stomach in a dark alley while unstable glowing shapes flicker from his lower back, medium shot, cold streetlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Học cách điều khiển Kagune cũng chính là học cách chấp nhận phần ngạ quỷ trong mình. Và với Kaneki, đó là một…

```text
Wide 16:9 landscape cinematic frame. a young man sitting on the floor of an empty training room, eyes closed, a faint controlled glow around him, medium shot, dim warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Người mang: Kamishiro Rize, ngạ quỷ đã gặp Kaneki Ken trong buổi hẹn định mệnh. Và sau này là chính Kaneki.

```text
Wide 16:9 landscape cinematic frame. a silhouette of a woman with long hair holding a book in a dim library corner, soft ominous light, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Vì sao một con người như Kaneki lại có Kagune? Sau một tai nạn, bác sĩ đã cấy nội tạng của Rize vào người cậu…

```text
Wide 16:9 landscape cinematic frame. a hospital operating room with bright surgical lights and a lone gurney, medium shot, cold clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Kẻ thù đáng sợ trong mùa một, Yamori, cũng mang Rinkaku. Trận đấu giữa hai người mang cùng loại là một trong…

```text
Wide 16:9 landscape cinematic frame. two silhouettes both with tentacle-like shapes facing each other in an empty warehouse, wide shot, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Hồ sơ 4: Bikaku

Lời: Hồ sơ số bốn: Bikaku, nghĩa là loại đuôi. Vị trí: vùng xương cụt. Hình dạng: một cái đuôi dài, đôi khi có nhi…

```text
Wide 16:9 landscape cinematic frame. a silhouette with a long segmented glowing tail extending from the lower spine, crouched in a fighting stance, medium shot, crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Điểm mạnh: cân bằng. Bikaku không nhanh nhất, không cứng nhất, không mạnh nhất, nhưng không có điểm yếu rõ rệ…

```text
Wide 16:9 landscape cinematic frame. a balanced radar chart on parchment with four evenly spread points, amber ink, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Điểm yếu: vì không có gì nổi bật, người dùng Bikaku phải dựa vào kỹ năng chiến đấu nhiều hơn các loại khác.

```text
Wide 16:9 landscape cinematic frame. a fighter practicing precise movements alone in an empty gym at night, the tail curling in controlled arcs, medium shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nishiki có một bạn gái là con người, và cô biết anh là ngạ quỷ. Một chi tiết nhỏ nhưng cho thấy người và ngạ…

```text
Wide 16:9 landscape cinematic frame. a couple sitting on a small apartment balcony at night sharing a blanket, city lights behind them, back view, warm light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Và vì Bikaku cân bằng, Nishiki chiến đấu rất linh hoạt: lúc quật, lúc đâm, lúc cuốn lấy đối thủ.

```text
Wide 16:9 landscape cinematic frame. a segmented tail sweeping in a wide arc, then stabbing forward, then coiling, sequential illustration, crimson highlights. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Người mang: Nishio Nishiki, đàn anh cùng trường của Kaneki. Anh là một trong những kẻ thù đầu tiên của Kaneki…

```text
Wide 16:9 landscape cinematic frame. a young man silhouette in a university hallway, glasses reflecting light, a faint tail shadow on the wall, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Bikaku là học sinh giỏi đều các môn. Không có điểm mười nào, nhưng cũng không có điểm liệt nào.

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding a report card full of identical good grades. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Bảng khắc chế

Lời: Giờ tới phần thú vị nhất. Bốn loại Kagune khắc chế nhau theo một vòng tròn, giống trò oẳn tù tì.

```text
Wide 16:9 landscape cinematic frame. a large circular diagram with four icons: feather, shield, tentacle, tail, connected by arrows in a loop, parchment style, amber and crimson. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Vì sao lại có vòng khắc chế này? Nếu nghĩ theo vật lý, nó khá hợp lý: nhanh thắng cân bằng, cân bằng thắng mạ…

```text
Wide 16:9 landscape cinematic frame. a simple physics-style sketch comparing speed, balance, power and weight with arrows in a loop, parchment style, amber ink. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Ukaku thắng Bikaku: nhờ tốc độ và tầm xa, Ukaku giữ khoảng cách và bắn phá trước khi cái đuôi kịp chạm tới.

```text
Wide 16:9 landscape cinematic frame. an arrow from the feather icon to the tail icon, with a small illustration of shards raining on a tailed silhouette from afar, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Bikaku thắng Rinkaku: cái đuôi cứng và cân bằng hơn, đủ sức cắt đứt những xúc tu dễ gãy.

```text
Wide 16:9 landscape cinematic frame. an arrow from the tail icon to the tentacle icon, with a tail slicing through a tentacle, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Rinkaku thắng Koukaku: sức công phá của xúc tu đủ để đập vỡ lớp giáp nặng, và giáp nặng thì quá chậm để né.

```text
Wide 16:9 landscape cinematic frame. an arrow from the tentacle icon to the shield icon, with a tentacle cracking an armored shape, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Koukaku thắng Ukaku: tấm khiên chặn hết mưa tinh thể, và chờ tới khi người dùng Ukaku kiệt sức.

```text
Wide 16:9 landscape cinematic frame. an arrow from the shield icon back to the feather icon, with a shield blocking shards while the winged figure tires, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ví dụ, một người dùng Ukaku thông minh có thể tránh đánh lâu với Koukaku, chờ đối thủ mệt trước. Luật khắc ch…

```text
Wide 16:9 landscape cinematic frame. a winged figure patiently circling a heavy armored opponent from a safe distance on a rooftop, wide shot, night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và CCG biết rõ điều này. Khi đi săn, họ chọn Quinque phù hợp để khắc chế loại Kagune của mục tiêu.

```text
Wide 16:9 landscape cinematic frame. an investigator choosing a briefcase from a rack labeled with four icons, medium shot, cold armory light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhưng nhớ: đây chỉ là xu hướng. Trong truyện, kinh nghiệm, trí thông minh và lượng tế bào RC có thể lật ngược…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adding a small asterisk beside the cycle diagram with the note tendency, not a rule. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Những trường hợp đặc biệt

Lời: Ngoài bốn loại, Tokyo Ghoul còn có những trường hợp đặc biệt. Đầu tiên là Kakuja: khi một ngạ quỷ ăn thịt đồn…

```text
Wide 16:9 landscape cinematic frame. a figure partially covered in jagged organic armor plates, an eerie mask-like shape forming over the face, dramatic low-angle shot, crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Kaku thấy đây là cơ chế đáng sợ nhất: để mạnh hơn, ngạ quỷ phải làm điều mà chính đồng loại của họ coi là cấm…

```text
Wide 16:9 landscape cinematic frame. a dark doorway with a warning line painted on the floor in front of it, a faint red glow beyond, medium shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Kakuja mạnh hơn nhiều, nhưng cái giá là tâm trí. Người mang dễ mất lý trí, và bộ giáp thường không hoàn chỉnh…

```text
Wide 16:9 landscape cinematic frame. a cracked armored mask with one side broken open, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Chimera rất hiếm, và thường là kết quả của những trường hợp bất thường về tế bào RC. Trong một vòng khắc chế,…

```text
Wide 16:9 landscape cinematic frame. the rock paper scissors cycle diagram with a special figure standing in the middle, touching two icons at once, parchment style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Thứ hai là Chimera: một số ngạ quỷ hiếm hoi có hai loại Kagune cùng lúc. Họ có thể đổi cách chiến đấu tùy đối…

```text
Wide 16:9 landscape cinematic frame. a silhouette with both feather-like wings from the shoulders and a tail from the lower back, balanced stance, medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Thứ ba là những con người được cấy Kakuhou nhân tạo, như Kaneki. Kỹ thuật này về sau được phát triển thành cả…

```text
Wide 16:9 landscape cinematic frame. a sealed laboratory door with a warning sign and a faint red glow from the gap underneath, medium shot, cold clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và cuối cùng là Quinque của CCG. Mỗi Quinque vẫn giữ đặc tính của loại Kagune gốc. Một Quinque làm từ Koukaku…

```text
Wide 16:9 landscape cinematic frame. a row of four metal briefcases each with a different organic weapon inside, labeled with the four icons, still life, harsh light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Góc nhìn của Kaku: vũ khí mọc ra từ con người

Lời: Kaku thấy thiết kế Kagune rất có ý đồ. Vũ khí không nằm trong tay, mà mọc ra từ bên trong cơ thể. Bạn không t…

```text
Wide 16:9 landscape cinematic frame. a figure trying to push a glowing shape back into their own back, struggling, medium shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Có một hình ảnh lặp lại trong truyện: Kaneki muốn giữ lấy phần người của mình, nhưng mỗi lần phải bảo vệ ai đ…

```text
Wide 16:9 landscape cinematic frame. a young man shielding a friend with one arm while a glowing shape rises from his back, torn between two directions, dramatic medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Kagune vì vậy không chỉ là vũ khí. Nó là cái giá phải trả để bảo vệ người khác. Một chủ đề mà Kaku thấy xuất…

```text
Wide 16:9 landscape cinematic frame. a small balance scale with a glowing organic shape on one side and a small heart on the other, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Với Kaneki, Kagune của Rize là một gánh nặng. Mỗi lần nó xuất hiện, cậu nhớ ra rằng mình không còn là người b…

```text
Wide 16:9 landscape cinematic frame. a young man staring into a cracked bathroom mirror, one eye normal and the other darkened, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Còn với CCG, biến Kagune thành Quinque là biến kẻ thù thành công cụ. Nhưng nếu người và ngạ quỷ cùng dùng một…

```text
Wide 16:9 landscape cinematic frame. a split image of an investigator holding a briefcase weapon and a ghoul with the same glowing shape, symmetrical composition, crimson and steel. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Đó là câu hỏi mà Tokyo Ghoul đặt ra suốt cả bộ truyện, và hệ thống Kagune là cách tác giả vẽ nó thành hình.

```text
Wide 16:9 landscape cinematic frame. a single white chrysanthemum lying on a dark café table next to an empty coffee cup, close-up, quiet melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Mục lục hồ sơ · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đóng tủ hồ sơ bằng một bảng mục lục.

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a filing cabinet drawer and pinning an index card on its front. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Thêm một dòng nhỏ cho mục lục: tất cả đều đến từ tế bào RC, tích trong Kakuhou, và tiêu hao theo cơn đói.

```text
Wide 16:9 landscape cinematic frame. a small footnote line written at the bottom of the index card with a cell icon, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Ukaku: vai, như cánh, nhanh và bắn xa, mệt nhanh. Koukaku: bả vai, như giáp, phòng thủ tốt, chậm.

```text
Wide 16:9 landscape cinematic frame. two index cards side by side with a feather icon and a shield icon and short notes, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Rinkaku: thắt lưng, xúc tu, công phá và hồi phục, dễ đứt. Bikaku: xương cụt, đuôi, cân bằng, cần kỹ năng.

```text
Wide 16:9 landscape cinematic frame. two index cards with a tentacle icon and a tail icon and short notes, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và vòng khắc chế: lông vũ thắng đuôi, đuôi thắng xúc tu, xúc tu thắng giáp, giáp thắng lông vũ.

```text
Wide 16:9 landscape cinematic frame. the circular cycle diagram glowing on the final page of the notebook, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và nếu bạn là nhà nghiên cứu CCG, bạn sẽ mang Quinque loại nào khi đi tuần? Câu hỏi này khó hơn bạn nghĩ đấy.

```text
Wide 16:9 landscape cinematic frame. a rack of four sealed weapon briefcases with a single empty slot waiting, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Nếu bạn là ngạ quỷ, bạn muốn Kagune của mình mọc ở đâu? Kaku đoán nhiều bạn chọn đôi cánh cho ngầu. Viết lựa…

```text
Wide 16:9 landscape cinematic frame. four empty checkboxes next to the four icons on a form, a pen resting on it, top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Kết

Lời: Bốn loại Kagune, bốn cách chiến đấu, và một câu hỏi chung: sức mạnh mọc ra từ nỗi đau thì có còn là của mình…

```text
Wide 16:9 landscape cinematic frame. a lone figure sitting on a rooftop at dawn, faint shapes fading from their back as the sun rises over Tokyo, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Tokyo Ghoul có phần tiếp theo tên là Tokyo Ghoul:re, nơi hệ thống này còn được mở rộng thêm nhiều. Nếu bạn mu…

```text
Wide 16:9 landscape cinematic frame. a second filing cabinet next to the first, its drawer labeled with a small question mark, medium shot, lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Video tiếp theo, Kaku chuyển sang một thế giới tươi sáng hơn nhiều: lịch sử các hệ trong Pokémon, từ mười lăm…

```text
Wide 16:9 landscape cinematic frame. a colorful chart of elemental type icons arranged in a grid on a bright desk, close-up, cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích kiểu hồ sơ bách khoa như thế này, hãy đăng ký kênh để Kaku mở thêm nhiều tủ hồ sơ nữa. Kaku gấp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off its archivist visor and waving from beside the filing cabinet. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 96 giây · cảnh s01–s08 · 1247 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Tokyo Ghoul tới hết anime mùa một, và nhắc ngắn vài khái niệm xuất hiện sau đó như Kakuja. Video không mô tả cảnh máu me chi tiết.

<short pause> Hồ sơ số ba mươi bảy. Loại tài liệu: vũ khí sinh học. Mức độ nguy hiểm: cao. Nguồn gốc: cơ thể của những sinh vật trông giống hệt con người.

<short pause> Trong Tokyo Ghoul, ngạ quỷ sống lẫn giữa người thường ở Tokyo. Họ đi học, đi làm, uống cà phê. <short pause> Nhưng khi cần chiến đấu, một thứ vũ khí sống mọc ra từ chính cơ thể họ.

<short pause> Thứ vũ khí đó gọi là Kagune. Và không phải Kagune nào cũng giống nhau. Có bốn loại, mỗi loại mọc ra từ một vị trí khác nhau trên cơ thể, với điểm mạnh và điểm yếu riêng.

<short pause> Tokyo Ghoul là manga của tác giả Ishida Sui, ra mắt năm 2011 và được chuyển thể anime từ năm 2014. Nhân vật chính Kaneki Ken là một sinh viên mê đọc sách, cho tới một buổi hẹn làm thay đổi cả cuộc đời cậu.

<short pause> <laugh> Kaku phải nói trước: đây là một bộ truyện u tối. Kaku sẽ giữ video ở mức phân tích hệ thống, không đi vào những cảnh nặng nề.

<short pause> Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở tủ hồ sơ Kagune. Mỗi hồ sơ ghi theo cùng một thứ tự: tên, vị trí, hình dạng, điểm mạnh, điểm yếu, và một người mang nó.

<short pause> Cuối video là bảng khắc chế giữa bốn loại, giống như trò oẳn tù tì, và một mục lục để bạn tự đoán Kagune của nhân vật mới.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Tokyo Ghoul tới hết anime mùa một, và nhắc ngắn vài khái niệm xuất hiện sau đó như Kakuja. Video không mô tả cảnh máu me chi tiết.

[pause] Hồ sơ số ba mươi bảy. Loại tài liệu: vũ khí sinh học. Mức độ nguy hiểm: cao. Nguồn gốc: cơ thể của những sinh vật trông giống hệt con người.

[pause] Trong Tokyo Ghoul, ngạ quỷ sống lẫn giữa người thường ở Tokyo. Họ đi học, đi làm, uống cà phê. [pause] Nhưng khi cần chiến đấu, một thứ vũ khí sống mọc ra từ chính cơ thể họ.

[pause] Thứ vũ khí đó gọi là Kagune. Và không phải Kagune nào cũng giống nhau. Có bốn loại, mỗi loại mọc ra từ một vị trí khác nhau trên cơ thể, với điểm mạnh và điểm yếu riêng.

[pause] Tokyo Ghoul là manga của tác giả Ishida Sui, ra mắt năm 2011 và được chuyển thể anime từ năm 2014. Nhân vật chính Kaneki Ken là một sinh viên mê đọc sách, cho tới một buổi hẹn làm thay đổi cả cuộc đời cậu.

[pause] [chuckles] Kaku phải nói trước: đây là một bộ truyện u tối. Kaku sẽ giữ video ở mức phân tích hệ thống, không đi vào những cảnh nặng nề.

[pause] Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở tủ hồ sơ Kagune. Mỗi hồ sơ ghi theo cùng một thứ tự: tên, vị trí, hình dạng, điểm mạnh, điểm yếu, và một người mang nó.

[pause] Cuối video là bảng khắc chế giữa bốn loại, giống như trò oẳn tù tì, và một mục lục để bạn tự đoán Kagune của nhân vật mới.
```

### c02 · Ngạ quỷ là ai

Khoảng 104 giây · cảnh s09–s17 · 1358 ký tự

**Gemini**

```text
Trước khi mở hồ sơ, cần hiểu cơ thể ngạ quỷ. Họ giống người về ngoại hình, nhưng hệ tiêu hóa không nhận được thức ăn của người. Thứ duy nhất nuôi sống họ là thịt người.

<short pause> Quán Anteiku trong truyện là nơi trú ẩn của những ngạ quỷ muốn sống yên ổn, không săn người. Họ giúp nhau tồn tại mà không gây hại, và Kaneki được đưa về đây khi không còn chỗ nào để đi.

<short pause> Có một ngoại lệ dễ thương hiếm hoi: cà phê. Ngạ quỷ uống được cà phê, nên quán cà phê trở thành nơi tụ họp của họ trong truyện.

<short pause> Trong cơ thể họ có một loại tế bào đặc biệt gọi là tế bào RC, nhiều hơn người thường rất nhiều. Tế bào này giúp họ hồi phục vết thương cực nhanh.

<short pause> Da của ngạ quỷ cứng tới mức dao kéo và đạn thường gần như không làm gì được. Vì vậy con người phải dùng tới vũ khí làm từ chính Kagune của ngạ quỷ.

<short pause> CCG còn đặt những cổng kiểm tra ở một số nơi trong thành phố. Cổng đo lượng tế bào RC của người đi qua. Ngạ quỷ có lượng tế bào RC cao hơn người thường rất nhiều, nên cổng sẽ báo động.

<short pause> Tức là trong thế giới này, một con số trong máu có thể quyết định bạn là công dân hay là con mồi.

<short pause> Tổ chức săn ngạ quỷ tên là CCG. Họ chế tạo vũ khí gọi là Quinque từ những cơ quan Kagune thu được. Nghĩa là con người chiến đấu với ngạ quỷ bằng chính một phần cơ thể của ngạ quỷ.

<short pause> <laugh> Kaku ghi chú: đây là thế giới mà ranh giới giữa kẻ săn và con mồi rất mờ. Và chính sự mờ nhạt đó là linh hồn của Tokyo Ghoul.
```

**ElevenLabs**

```text
Trước khi mở hồ sơ, cần hiểu cơ thể ngạ quỷ. Họ giống người về ngoại hình, nhưng hệ tiêu hóa không nhận được thức ăn của người. Thứ duy nhất nuôi sống họ là thịt người.

[pause] Quán Anteiku trong truyện là nơi trú ẩn của những ngạ quỷ muốn sống yên ổn, không săn người. Họ giúp nhau tồn tại mà không gây hại, và Kaneki được đưa về đây khi không còn chỗ nào để đi.

[pause] Có một ngoại lệ dễ thương hiếm hoi: cà phê. Ngạ quỷ uống được cà phê, nên quán cà phê trở thành nơi tụ họp của họ trong truyện.

[pause] Trong cơ thể họ có một loại tế bào đặc biệt gọi là tế bào RC, nhiều hơn người thường rất nhiều. Tế bào này giúp họ hồi phục vết thương cực nhanh.

[pause] Da của ngạ quỷ cứng tới mức dao kéo và đạn thường gần như không làm gì được. Vì vậy con người phải dùng tới vũ khí làm từ chính Kagune của ngạ quỷ.

[pause] CCG còn đặt những cổng kiểm tra ở một số nơi trong thành phố. Cổng đo lượng tế bào RC của người đi qua. Ngạ quỷ có lượng tế bào RC cao hơn người thường rất nhiều, nên cổng sẽ báo động.

[pause] Tức là trong thế giới này, một con số trong máu có thể quyết định bạn là công dân hay là con mồi.

[pause] Tổ chức săn ngạ quỷ tên là CCG. Họ chế tạo vũ khí gọi là Quinque từ những cơ quan Kagune thu được. Nghĩa là con người chiến đấu với ngạ quỷ bằng chính một phần cơ thể của ngạ quỷ.

[pause] [chuckles] Kaku ghi chú: đây là thế giới mà ranh giới giữa kẻ săn và con mồi rất mờ. Và chính sự mờ nhạt đó là linh hồn của Tokyo Ghoul.
```

### c03 · Kagune hình thành thế nào / Hồ sơ 1: Ukaku

Khoảng 136 giây · cảnh s18–s31 · 1766 ký tự

**Gemini**

```text
Tế bào RC được dự trữ trong một cơ quan gọi là Kakuhou. Khi chiến đấu, ngạ quỷ giải phóng tế bào từ cơ quan này. Chúng chảy ra như chất lỏng, rồi đông cứng lại thành vũ khí.

<short pause> Nhưng mỗi Kagune lại có hình dạng riêng, như vân tay. Hai người cùng loại Ukaku có thể có đôi cánh rất khác nhau về kích thước, màu sắc và cách tấn công.

<short pause> Vị trí của Kakuhou quyết định loại Kagune. Và mỗi ngạ quỷ sinh ra với một loại, không đổi được. Giống như nhóm máu.

<short pause> Khi Kagune xuất hiện, mắt ngạ quỷ cũng đổi màu: lòng trắng chuyển đen, con ngươi chuyển đỏ. Đây là dấu hiệu dễ nhận biết nhất.

<short pause> Kagune rất mạnh, nhưng nó tiêu hao tế bào RC. Dùng càng nhiều, càng phải ăn để bù lại. Nghĩa là sức mạnh của ngạ quỷ luôn gắn với cơn đói.

<short pause> Giờ ta mở bốn hồ sơ, theo thứ tự từ vai xuống tới đuôi.

<short pause> Hồ sơ số một: Ukaku, nghĩa là loại lông vũ. Vị trí: vùng vai. Hình dạng: như đôi cánh hoặc một chùm lông tỏa ra sau lưng.

<short pause> Điểm mạnh thứ nhất: tốc độ. Ukaku là loại nhanh nhất trong bốn loại.

<short pause> Điểm mạnh thứ hai: tấn công từ xa. Người dùng có thể bắn ra những mảnh tinh thể sắc như mưa đạn.

<short pause> Điểm yếu: sức bền kém. Ukaku tiêu tế bào RC rất nhanh, nên người dùng mệt nhanh. Họ phải thắng nhanh, hoặc không thắng được.

<short pause> Em trai của cô, Ayato, cũng mang Ukaku. Hai chị em cùng một loại nhưng chọn hai con đường khác nhau: một người ở lại với quán cà phê, một người gia nhập nhóm ngạ quỷ hung bạo.

<short pause> Kaku thấy chi tiết này rất đúng tinh thần bộ truyện: Kagune quyết định cách bạn chiến đấu, không quyết định bạn là người thế nào.

<short pause> Người mang: Kirishima Touka, cô gái làm ở quán cà phê Anteiku. Cô chiến đấu nhanh, dữ dội, và thường muốn kết thúc trận đấu trước khi đối thủ kịp phản ứng.

<short pause> <laugh> Kaku ghi chú: nếu Kagune là môn thể thao, Ukaku chính là vận động viên chạy nước rút. Rất nhanh, rất đẹp, nhưng đừng bắt họ chạy marathon.
```

**ElevenLabs**

```text
Tế bào RC được dự trữ trong một cơ quan gọi là Kakuhou. Khi chiến đấu, ngạ quỷ giải phóng tế bào từ cơ quan này. Chúng chảy ra như chất lỏng, rồi đông cứng lại thành vũ khí.

[pause] Nhưng mỗi Kagune lại có hình dạng riêng, như vân tay. Hai người cùng loại Ukaku có thể có đôi cánh rất khác nhau về kích thước, màu sắc và cách tấn công.

[pause] Vị trí của Kakuhou quyết định loại Kagune. Và mỗi ngạ quỷ sinh ra với một loại, không đổi được. Giống như nhóm máu.

[pause] Khi Kagune xuất hiện, mắt ngạ quỷ cũng đổi màu: lòng trắng chuyển đen, con ngươi chuyển đỏ. Đây là dấu hiệu dễ nhận biết nhất.

[pause] Kagune rất mạnh, nhưng nó tiêu hao tế bào RC. Dùng càng nhiều, càng phải ăn để bù lại. Nghĩa là sức mạnh của ngạ quỷ luôn gắn với cơn đói.

[pause] Giờ ta mở bốn hồ sơ, theo thứ tự từ vai xuống tới đuôi.

[pause] Hồ sơ số một: Ukaku, nghĩa là loại lông vũ. Vị trí: vùng vai. Hình dạng: như đôi cánh hoặc một chùm lông tỏa ra sau lưng.

[pause] Điểm mạnh thứ nhất: tốc độ. Ukaku là loại nhanh nhất trong bốn loại.

[pause] Điểm mạnh thứ hai: tấn công từ xa. Người dùng có thể bắn ra những mảnh tinh thể sắc như mưa đạn.

[pause] Điểm yếu: sức bền kém. Ukaku tiêu tế bào RC rất nhanh, nên người dùng mệt nhanh. Họ phải thắng nhanh, hoặc không thắng được.

[pause] Em trai của cô, Ayato, cũng mang Ukaku. Hai chị em cùng một loại nhưng chọn hai con đường khác nhau: một người ở lại với quán cà phê, một người gia nhập nhóm ngạ quỷ hung bạo.

[pause] Kaku thấy chi tiết này rất đúng tinh thần bộ truyện: Kagune quyết định cách bạn chiến đấu, không quyết định bạn là người thế nào.

[pause] Người mang: Kirishima Touka, cô gái làm ở quán cà phê Anteiku. Cô chiến đấu nhanh, dữ dội, và thường muốn kết thúc trận đấu trước khi đối thủ kịp phản ứng.

[pause] [chuckles] Kaku ghi chú: nếu Kagune là môn thể thao, Ukaku chính là vận động viên chạy nước rút. Rất nhanh, rất đẹp, nhưng đừng bắt họ chạy marathon.
```

### c04 · Hồ sơ 2: Koukaku

Khoảng 68 giây · cảnh s32–s38 · 886 ký tự

**Gemini**

```text
Hồ sơ số hai: Koukaku, nghĩa là loại giáp. Vị trí: ngay dưới xương bả vai. Hình dạng: cứng và nặng, như tấm khiên, lưỡi kiếm lớn hoặc mũi khoan.

<short pause> Điểm mạnh: phòng thủ tốt nhất. Kagune loại này cứng tới mức có thể dùng làm khiên, chặn gần như mọi đòn tấn công.

<short pause> Điểm yếu: nặng và chậm. Mật độ tế bào dày khiến Kagune khó điều khiển nhanh. Người dùng thường chiến đấu như một pháo đài di động.

<short pause> Koukaku còn có thể đổi hình dạng trong trận: lúc thì dựng thành khiên, lúc thì xoắn lại thành mũi khoan. Người dùng giỏi biết khi nào nên thủ, khi nào nên đâm.

<short pause> <laugh> Kaku mà có Koukaku thì chắc chỉ dùng làm ô che mưa. Mà ô nặng quá thì cũng thôi, Kaku ở nhà đọc sách.

<short pause> Người mang: Tsukiyama Shuu, quý ông lịch lãm có sở thích ẩm thực kỳ quặc. Kagune của anh có dạng một lưỡi kiếm xoắn, vừa tấn công vừa phòng thủ.

<short pause> Kaku ghi chú: Koukaku là thủ môn của đội. Chạy thì không nhanh, nhưng muốn qua mặt thì rất khó.
```

**ElevenLabs**

```text
Hồ sơ số hai: Koukaku, nghĩa là loại giáp. Vị trí: ngay dưới xương bả vai. Hình dạng: cứng và nặng, như tấm khiên, lưỡi kiếm lớn hoặc mũi khoan.

[pause] Điểm mạnh: phòng thủ tốt nhất. Kagune loại này cứng tới mức có thể dùng làm khiên, chặn gần như mọi đòn tấn công.

[pause] Điểm yếu: nặng và chậm. Mật độ tế bào dày khiến Kagune khó điều khiển nhanh. Người dùng thường chiến đấu như một pháo đài di động.

[pause] Koukaku còn có thể đổi hình dạng trong trận: lúc thì dựng thành khiên, lúc thì xoắn lại thành mũi khoan. Người dùng giỏi biết khi nào nên thủ, khi nào nên đâm.

[pause] [chuckles] Kaku mà có Koukaku thì chắc chỉ dùng làm ô che mưa. Mà ô nặng quá thì cũng thôi, Kaku ở nhà đọc sách.

[pause] Người mang: Tsukiyama Shuu, quý ông lịch lãm có sở thích ẩm thực kỳ quặc. Kagune của anh có dạng một lưỡi kiếm xoắn, vừa tấn công vừa phòng thủ.

[pause] Kaku ghi chú: Koukaku là thủ môn của đội. Chạy thì không nhanh, nhưng muốn qua mặt thì rất khó.
```

### c05 · Hồ sơ 3: Rinkaku

Khoảng 95 giây · cảnh s39–s47 · 1239 ký tự

**Gemini**

```text
Hồ sơ số ba: Rinkaku, nghĩa là loại vảy. Vị trí: vùng thắt lưng. Hình dạng: những xúc tu dài, mềm dẻo, có thể đâm, quật và quấn.

<short pause> Điểm mạnh thứ nhất: sức công phá. Mỗi xúc tu có thể đâm xuyên hoặc đập vỡ bê tông.

<short pause> Điểm mạnh thứ hai: hồi phục. Rinkaku có khả năng tái tạo mạnh nhất, nên người dùng thường rất khó bị hạ.

<short pause> Điểm yếu: cấu trúc liên kết yếu, dễ bị cắt đứt. Và người ta hay nói những người mang Rinkaku thường có tâm lý bất ổn, dễ mất kiểm soát. Kaku gắn nhãn đây là nhận xét của người xem, không phải luật.

<short pause> Số lượng xúc tu cũng khác nhau ở mỗi người. Kaneki lúc đầu chỉ có một vài xúc tu, và gần như không điều khiển được chúng. Chúng xuất hiện khi cậu đói, sợ hãi hoặc giận dữ.

<short pause> Học cách điều khiển Kagune cũng chính là học cách chấp nhận phần ngạ quỷ trong mình. Và với Kaneki, đó là một quá trình rất đau.

<short pause> Người mang: Kamishiro Rize, ngạ quỷ đã gặp Kaneki Ken trong buổi hẹn định mệnh. Và sau này là chính Kaneki.

<short pause> Vì sao một con người như Kaneki lại có Kagune? Sau một tai nạn, bác sĩ đã cấy nội tạng của Rize vào người cậu. Kaneki trở thành nửa người nửa ngạ quỷ, mang Kakuhou loại Rinkaku.

<short pause> Kẻ thù đáng sợ trong mùa một, Yamori, cũng mang Rinkaku. Trận đấu giữa hai người mang cùng loại là một trong những đoạn nặng nề nhất của bộ phim.
```

**ElevenLabs**

```text
Hồ sơ số ba: Rinkaku, nghĩa là loại vảy. Vị trí: vùng thắt lưng. Hình dạng: những xúc tu dài, mềm dẻo, có thể đâm, quật và quấn.

[pause] Điểm mạnh thứ nhất: sức công phá. Mỗi xúc tu có thể đâm xuyên hoặc đập vỡ bê tông.

[pause] Điểm mạnh thứ hai: hồi phục. Rinkaku có khả năng tái tạo mạnh nhất, nên người dùng thường rất khó bị hạ.

[pause] Điểm yếu: cấu trúc liên kết yếu, dễ bị cắt đứt. Và người ta hay nói những người mang Rinkaku thường có tâm lý bất ổn, dễ mất kiểm soát. Kaku gắn nhãn đây là nhận xét của người xem, không phải luật.

[pause] Số lượng xúc tu cũng khác nhau ở mỗi người. Kaneki lúc đầu chỉ có một vài xúc tu, và gần như không điều khiển được chúng. Chúng xuất hiện khi cậu đói, sợ hãi hoặc giận dữ.

[pause] Học cách điều khiển Kagune cũng chính là học cách chấp nhận phần ngạ quỷ trong mình. Và với Kaneki, đó là một quá trình rất đau.

[pause] Người mang: Kamishiro Rize, ngạ quỷ đã gặp Kaneki Ken trong buổi hẹn định mệnh. Và sau này là chính Kaneki.

[pause] [curious] Vì sao một con người như Kaneki lại có Kagune? Sau một tai nạn, bác sĩ đã cấy nội tạng của Rize vào người cậu. Kaneki trở thành nửa người nửa ngạ quỷ, mang Kakuhou loại Rinkaku.

[pause] Kẻ thù đáng sợ trong mùa một, Yamori, cũng mang Rinkaku. Trận đấu giữa hai người mang cùng loại là một trong những đoạn nặng nề nhất của bộ phim.
```

### c06 · Hồ sơ 4: Bikaku / Bảng khắc chế

Khoảng 148 giây · cảnh s48–s63 · 1923 ký tự

**Gemini**

```text
Hồ sơ số bốn: Bikaku, nghĩa là loại đuôi. Vị trí: vùng xương cụt. Hình dạng: một cái đuôi dài, đôi khi có nhiều đốt.

<short pause> Điểm mạnh: cân bằng. Bikaku không nhanh nhất, không cứng nhất, không mạnh nhất, nhưng không có điểm yếu rõ rệt. Tầm đánh trung bình, tốc độ khá, độ bền khá.

<short pause> Điểm yếu: vì không có gì nổi bật, người dùng Bikaku phải dựa vào kỹ năng chiến đấu nhiều hơn các loại khác.

<short pause> Nishiki có một bạn gái là con người, và cô biết anh là ngạ quỷ. Một chi tiết nhỏ nhưng cho thấy người và ngạ quỷ vẫn có thể thương nhau, bất chấp mọi luật lệ.

<short pause> Và vì Bikaku cân bằng, Nishiki chiến đấu rất linh hoạt: lúc quật, lúc đâm, lúc cuốn lấy đối thủ.

<short pause> Người mang: Nishio Nishiki, đàn anh cùng trường của Kaneki. Anh là một trong những kẻ thù đầu tiên của Kaneki, và sau này lại trở thành đồng minh.

<short pause> <laugh> Kaku ghi chú: Bikaku là học sinh giỏi đều các môn. Không có điểm mười nào, nhưng cũng không có điểm liệt nào.

<short pause> Giờ tới phần thú vị nhất. Bốn loại Kagune khắc chế nhau theo một vòng tròn, giống trò oẳn tù tì.

<short pause> Vì sao lại có vòng khắc chế này? Nếu nghĩ theo vật lý, nó khá hợp lý: nhanh thắng cân bằng, cân bằng thắng mạnh mà dễ gãy, mạnh thắng nặng mà chậm, nặng thắng nhanh mà yếu sức bền.

<short pause> Ukaku thắng Bikaku: nhờ tốc độ và tầm xa, Ukaku giữ khoảng cách và bắn phá trước khi cái đuôi kịp chạm tới.

<short pause> Bikaku thắng Rinkaku: cái đuôi cứng và cân bằng hơn, đủ sức cắt đứt những xúc tu dễ gãy.

<short pause> Rinkaku thắng Koukaku: sức công phá của xúc tu đủ để đập vỡ lớp giáp nặng, và giáp nặng thì quá chậm để né.

<short pause> Koukaku thắng Ukaku: tấm khiên chặn hết mưa tinh thể, và chờ tới khi người dùng Ukaku kiệt sức.

<short pause> Ví dụ, một người dùng Ukaku thông minh có thể tránh đánh lâu với Koukaku, chờ đối thủ mệt trước. Luật khắc chế chỉ đúng khi hai bên ngang sức.

<short pause> Và CCG biết rõ điều này. Khi đi săn, họ chọn Quinque phù hợp để khắc chế loại Kagune của mục tiêu.

<short pause> Nhưng nhớ: đây chỉ là xu hướng. Trong truyện, kinh nghiệm, trí thông minh và lượng tế bào RC có thể lật ngược mọi lợi thế.
```

**ElevenLabs**

```text
Hồ sơ số bốn: Bikaku, nghĩa là loại đuôi. Vị trí: vùng xương cụt. Hình dạng: một cái đuôi dài, đôi khi có nhiều đốt.

[pause] Điểm mạnh: cân bằng. Bikaku không nhanh nhất, không cứng nhất, không mạnh nhất, nhưng không có điểm yếu rõ rệt. Tầm đánh trung bình, tốc độ khá, độ bền khá.

[pause] Điểm yếu: vì không có gì nổi bật, người dùng Bikaku phải dựa vào kỹ năng chiến đấu nhiều hơn các loại khác.

[pause] Nishiki có một bạn gái là con người, và cô biết anh là ngạ quỷ. Một chi tiết nhỏ nhưng cho thấy người và ngạ quỷ vẫn có thể thương nhau, bất chấp mọi luật lệ.

[pause] Và vì Bikaku cân bằng, Nishiki chiến đấu rất linh hoạt: lúc quật, lúc đâm, lúc cuốn lấy đối thủ.

[pause] Người mang: Nishio Nishiki, đàn anh cùng trường của Kaneki. Anh là một trong những kẻ thù đầu tiên của Kaneki, và sau này lại trở thành đồng minh.

[pause] [chuckles] Kaku ghi chú: Bikaku là học sinh giỏi đều các môn. Không có điểm mười nào, nhưng cũng không có điểm liệt nào.

[pause] Giờ tới phần thú vị nhất. Bốn loại Kagune khắc chế nhau theo một vòng tròn, giống trò oẳn tù tì.

[pause] [curious] Vì sao lại có vòng khắc chế này? Nếu nghĩ theo vật lý, nó khá hợp lý: nhanh thắng cân bằng, cân bằng thắng mạnh mà dễ gãy, mạnh thắng nặng mà chậm, nặng thắng nhanh mà yếu sức bền.

[pause] Ukaku thắng Bikaku: nhờ tốc độ và tầm xa, Ukaku giữ khoảng cách và bắn phá trước khi cái đuôi kịp chạm tới.

[pause] Bikaku thắng Rinkaku: cái đuôi cứng và cân bằng hơn, đủ sức cắt đứt những xúc tu dễ gãy.

[pause] Rinkaku thắng Koukaku: sức công phá của xúc tu đủ để đập vỡ lớp giáp nặng, và giáp nặng thì quá chậm để né.

[pause] Koukaku thắng Ukaku: tấm khiên chặn hết mưa tinh thể, và chờ tới khi người dùng Ukaku kiệt sức.

[pause] Ví dụ, một người dùng Ukaku thông minh có thể tránh đánh lâu với Koukaku, chờ đối thủ mệt trước. Luật khắc chế chỉ đúng khi hai bên ngang sức.

[pause] Và CCG biết rõ điều này. Khi đi săn, họ chọn Quinque phù hợp để khắc chế loại Kagune của mục tiêu.

[pause] Nhưng nhớ: đây chỉ là xu hướng. Trong truyện, kinh nghiệm, trí thông minh và lượng tế bào RC có thể lật ngược mọi lợi thế.
```

### c07 · Những trường hợp đặc biệt / Góc nhìn của Kaku: vũ khí mọc ra từ con người

Khoảng 149 giây · cảnh s64–s76 · 1936 ký tự

**Gemini**

```text
Ngoài bốn loại, Tokyo Ghoul còn có những trường hợp đặc biệt. Đầu tiên là Kakuja: khi một ngạ quỷ ăn thịt đồng loại nhiều lần, tế bào RC biến đổi, tạo thành lớp giáp phủ khắp cơ thể.

<short pause> Kaku thấy đây là cơ chế đáng sợ nhất: để mạnh hơn, ngạ quỷ phải làm điều mà chính đồng loại của họ coi là cấm kỵ. Sức mạnh lớn nhất nằm sau ranh giới đạo đức lớn nhất.

<short pause> Kakuja mạnh hơn nhiều, nhưng cái giá là tâm trí. Người mang dễ mất lý trí, và bộ giáp thường không hoàn chỉnh, có chỗ hở.

<short pause> Chimera rất hiếm, và thường là kết quả của những trường hợp bất thường về tế bào RC. Trong một vòng khắc chế, người có hai loại gần như không bị khắc chế hoàn toàn.

<short pause> Thứ hai là Chimera: một số ngạ quỷ hiếm hoi có hai loại Kagune cùng lúc. Họ có thể đổi cách chiến đấu tùy đối thủ.

<short pause> Thứ ba là những con người được cấy Kakuhou nhân tạo, như Kaneki. Kỹ thuật này về sau được phát triển thành cả một chương trình, nhưng Kaku sẽ không spoiler thêm.

<short pause> Và cuối cùng là Quinque của CCG. Mỗi Quinque vẫn giữ đặc tính của loại Kagune gốc. Một Quinque làm từ Koukaku sẽ nặng và bền, từ Ukaku thì bắn xa. Vũ khí của con người cũng chơi oẳn tù tì.

<short pause> Kaku thấy thiết kế Kagune rất có ý đồ. Vũ khí không nằm trong tay, mà mọc ra từ bên trong cơ thể. Bạn không thể đặt nó xuống. Nó là một phần của bạn.

<short pause> Có một hình ảnh lặp lại trong truyện: Kaneki muốn giữ lấy phần người của mình, nhưng mỗi lần phải bảo vệ ai đó, cậu lại phải dùng tới phần ngạ quỷ.

<short pause> Kagune vì vậy không chỉ là vũ khí. Nó là cái giá phải trả để bảo vệ người khác. Một chủ đề mà Kaku thấy xuất hiện ở rất nhiều bộ anime, từ Edgerunners tới Tokyo Ghoul.

<short pause> Với Kaneki, Kagune của Rize là một gánh nặng. Mỗi lần nó xuất hiện, cậu nhớ ra rằng mình không còn là người bình thường nữa.

<short pause> Còn với CCG, biến Kagune thành Quinque là biến kẻ thù thành công cụ. <short pause> Nhưng nếu người và ngạ quỷ cùng dùng một thứ vũ khí, thì ai mới là quái vật?

<short pause> Đó là câu hỏi mà Tokyo Ghoul đặt ra suốt cả bộ truyện, và hệ thống Kagune là cách tác giả vẽ nó thành hình.
```

**ElevenLabs**

```text
Ngoài bốn loại, Tokyo Ghoul còn có những trường hợp đặc biệt. Đầu tiên là Kakuja: khi một ngạ quỷ ăn thịt đồng loại nhiều lần, tế bào RC biến đổi, tạo thành lớp giáp phủ khắp cơ thể.

[pause] Kaku thấy đây là cơ chế đáng sợ nhất: để mạnh hơn, ngạ quỷ phải làm điều mà chính đồng loại của họ coi là cấm kỵ. Sức mạnh lớn nhất nằm sau ranh giới đạo đức lớn nhất.

[pause] Kakuja mạnh hơn nhiều, nhưng cái giá là tâm trí. Người mang dễ mất lý trí, và bộ giáp thường không hoàn chỉnh, có chỗ hở.

[pause] Chimera rất hiếm, và thường là kết quả của những trường hợp bất thường về tế bào RC. Trong một vòng khắc chế, người có hai loại gần như không bị khắc chế hoàn toàn.

[pause] Thứ hai là Chimera: một số ngạ quỷ hiếm hoi có hai loại Kagune cùng lúc. Họ có thể đổi cách chiến đấu tùy đối thủ.

[pause] Thứ ba là những con người được cấy Kakuhou nhân tạo, như Kaneki. Kỹ thuật này về sau được phát triển thành cả một chương trình, nhưng Kaku sẽ không spoiler thêm.

[pause] Và cuối cùng là Quinque của CCG. Mỗi Quinque vẫn giữ đặc tính của loại Kagune gốc. Một Quinque làm từ Koukaku sẽ nặng và bền, từ Ukaku thì bắn xa. Vũ khí của con người cũng chơi oẳn tù tì.

[pause] Kaku thấy thiết kế Kagune rất có ý đồ. Vũ khí không nằm trong tay, mà mọc ra từ bên trong cơ thể. Bạn không thể đặt nó xuống. Nó là một phần của bạn.

[pause] Có một hình ảnh lặp lại trong truyện: Kaneki muốn giữ lấy phần người của mình, nhưng mỗi lần phải bảo vệ ai đó, cậu lại phải dùng tới phần ngạ quỷ.

[pause] Kagune vì vậy không chỉ là vũ khí. Nó là cái giá phải trả để bảo vệ người khác. Một chủ đề mà Kaku thấy xuất hiện ở rất nhiều bộ anime, từ Edgerunners tới Tokyo Ghoul.

[pause] Với Kaneki, Kagune của Rize là một gánh nặng. Mỗi lần nó xuất hiện, cậu nhớ ra rằng mình không còn là người bình thường nữa.

[pause] Còn với CCG, biến Kagune thành Quinque là biến kẻ thù thành công cụ. [pause] [curious] Nhưng nếu người và ngạ quỷ cùng dùng một thứ vũ khí, thì ai mới là quái vật?

[pause] Đó là câu hỏi mà Tokyo Ghoul đặt ra suốt cả bộ truyện, và hệ thống Kagune là cách tác giả vẽ nó thành hình.
```

### c08 · Mục lục hồ sơ / Kết

Khoảng 101 giây · cảnh s77–s87 · 1313 ký tự

**Gemini**

```text
<laugh> Kaku đóng tủ hồ sơ bằng một bảng mục lục.

<short pause> Thêm một dòng nhỏ cho mục lục: tất cả đều đến từ tế bào RC, tích trong Kakuhou, và tiêu hao theo cơn đói.

<short pause> Ukaku: vai, như cánh, nhanh và bắn xa, mệt nhanh. Koukaku: bả vai, như giáp, phòng thủ tốt, chậm.

<short pause> Rinkaku: thắt lưng, xúc tu, công phá và hồi phục, dễ đứt. Bikaku: xương cụt, đuôi, cân bằng, cần kỹ năng.

<short pause> Và vòng khắc chế: lông vũ thắng đuôi, đuôi thắng xúc tu, xúc tu thắng giáp, giáp thắng lông vũ.

<short pause> Và nếu bạn là nhà nghiên cứu CCG, bạn sẽ mang Quinque loại nào khi đi tuần? Câu hỏi này khó hơn bạn nghĩ đấy.

<short pause> Nếu bạn là ngạ quỷ, bạn muốn Kagune của mình mọc ở đâu? Kaku đoán nhiều bạn chọn đôi cánh cho ngầu. Viết lựa chọn và lý do của bạn vào bình luận nhé.

<short pause> Bốn loại Kagune, bốn cách chiến đấu, và một câu hỏi chung: sức mạnh mọc ra từ nỗi đau thì có còn là của mình không?

<short pause> Tokyo Ghoul có phần tiếp theo tên là Tokyo Ghoul:re, nơi hệ thống này còn được mở rộng thêm nhiều. Nếu bạn muốn Kaku làm hồ sơ phần hai, hãy nói trong bình luận.

<short pause> Video tiếp theo, Kaku chuyển sang một thế giới tươi sáng hơn nhiều: lịch sử các hệ trong Pokémon, từ mười lăm hệ ban đầu tới mười tám hệ hôm nay. Có một hệ được thêm vào chỉ để cân bằng lại một hệ quá mạnh.

<short pause> Nếu bạn thích kiểu hồ sơ bách khoa như thế này, hãy đăng ký kênh để Kaku mở thêm nhiều tủ hồ sơ nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Kaku đóng tủ hồ sơ bằng một bảng mục lục.

[pause] Thêm một dòng nhỏ cho mục lục: tất cả đều đến từ tế bào RC, tích trong Kakuhou, và tiêu hao theo cơn đói.

[pause] Ukaku: vai, như cánh, nhanh và bắn xa, mệt nhanh. Koukaku: bả vai, như giáp, phòng thủ tốt, chậm.

[pause] Rinkaku: thắt lưng, xúc tu, công phá và hồi phục, dễ đứt. Bikaku: xương cụt, đuôi, cân bằng, cần kỹ năng.

[pause] Và vòng khắc chế: lông vũ thắng đuôi, đuôi thắng xúc tu, xúc tu thắng giáp, giáp thắng lông vũ.

[pause] [curious] Và nếu bạn là nhà nghiên cứu CCG, bạn sẽ mang Quinque loại nào khi đi tuần? Câu hỏi này khó hơn bạn nghĩ đấy.

[pause] Nếu bạn là ngạ quỷ, bạn muốn Kagune của mình mọc ở đâu? Kaku đoán nhiều bạn chọn đôi cánh cho ngầu. Viết lựa chọn và lý do của bạn vào bình luận nhé.

[pause] Bốn loại Kagune, bốn cách chiến đấu, và một câu hỏi chung: sức mạnh mọc ra từ nỗi đau thì có còn là của mình không?

[pause] Tokyo Ghoul có phần tiếp theo tên là Tokyo Ghoul:re, nơi hệ thống này còn được mở rộng thêm nhiều. Nếu bạn muốn Kaku làm hồ sơ phần hai, hãy nói trong bình luận.

[pause] Video tiếp theo, Kaku chuyển sang một thế giới tươi sáng hơn nhiều: lịch sử các hệ trong Pokémon, từ mười lăm hệ ban đầu tới mười tám hệ hôm nay. Có một hệ được thêm vào chỉ để cân bằng lại một hệ quá mạnh.

[pause] Nếu bạn thích kiểu hồ sơ bách khoa như thế này, hãy đăng ký kênh để Kaku mở thêm nhiều tủ hồ sơ nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
