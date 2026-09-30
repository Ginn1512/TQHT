# Bộ prompt · Doraemon: 10 bảo bối, cái nào làm được ngoài đời thật?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 81 ảnh, 7 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Video này gần như không có spoiler, chỉ nói về các bảo bối quen thuộc. Và Kaku nhắc trước: đây là video khoa…

```text
Wide 16:9 landscape cinematic frame. a child's desk with a science notebook, a small toy propeller and a warning card that says do not try, close-up, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Nếu được chọn một bảo bối của Doraemon, bạn chọn gì? Chong chóng tre để bay đi học? Cánh cửa thần kỳ để khỏi…

```text
Wide 16:9 landscape cinematic frame. a round white pocket-like pouch doodle on paper with small sketches of a propeller, a door and a slice of bread spilling out, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trẻ em Việt Nam hỏi câu này suốt hơn ba mươi năm, từ khi truyện Đôrêmon đến Việt Nam năm 1992. Hôm nay Kaku h…

```text
Wide 16:9 landscape cinematic frame. a worn old comic book on a wooden school desk beside a modern smartphone, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và đúng dịp này, ngày năm tháng ba năm 2027, bộ phim Doraemon mới ra rạp ở Nhật. Một thời điểm hoàn hảo để mở…

```text
Wide 16:9 landscape cinematic frame. a cinema ticket and a small blue bell charm resting on a table, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku chấm mười bảo bối theo thang điểm độ thật từ không tới mười: trong t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny lab goggles, holding a clipboard with a score scale from zero to ten. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Doraemon là manga của Fujiko F. Fujio, xuất hiện lần đầu vào tháng mười hai năm 1969, cùng lúc trên sáu tạp c…

```text
Wide 16:9 landscape cinematic frame. an old calendar page from the late nineteen sixties pinned beside a futuristic calendar page from the twenty second century, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Doraemon ở Việt Nam

Lời: Trước khi mở túi, một chút lịch sử. Mùa đông năm 1992, Nhà xuất bản Kim Đồng phát hành truyện Đôrêmon ở Việt…

```text
Wide 16:9 landscape cinematic frame. a small stack of early nineteen nineties comic books tied with string on a street vendor's table, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Những bản đầu tiên ra đời khi chưa có bản quyền chính thức. Về sau, Kim Đồng làm việc với nhà xuất bản Nhật đ…

```text
Wide 16:9 landscape cinematic frame. an old comic book beside a newer edition with a small official seal on the cover, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Người Việt còn nhớ những cái tên được Việt hóa: Nobita, Xuka, Chaien, Xêkô. Với nhiều người, đó là những ngườ…

```text
Wide 16:9 landscape cinematic frame. four small name tags pinned to a corkboard beside a child's drawing of friends, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: gần như mọi bảo bối trong video này, bạn đều đã từng ước có ít nhất một lần. Hôm nay, ta thử hỏi k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small wish list written in childlike handwriting. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Bảo bối 1: Chong chóng tre

Lời: Bảo bối nổi tiếng nhất: chong chóng tre. Gắn lên đầu, chong chóng quay, và bạn bay lên. Nobita, Xuka, Chaien,…

```text
Wide 16:9 landscape cinematic frame. a small bamboo-style propeller hovering above a child's head in a blue sky over rooftops, wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Ngoài đời, con người đã bay bằng cánh quạt: trực thăng, và gần đây là những chiếc drone chở người. Nguyên lý…

```text
Wide 16:9 landscape cinematic frame. a small passenger drone with multiple rotors hovering above a test field, wide shot, clear daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhưng có hai vấn đề. Một: để nâng một người, cánh quạt phải rất lớn và rất mạnh, không thể nhỏ như chiếc chon…

```text
Wide 16:9 landscape cinematic frame. a diagram comparing a tiny propeller to a huge helicopter rotor with a human silhouette for scale, infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Hai: khi cánh quạt quay, nó đẩy ngược lại thứ gắn với nó. Đó là lý do trực thăng cần cánh quạt đuôi. Không có…

```text
Wide 16:9 landscape cinematic frame. a humorous sketch of a stick figure spinning in circles under a propeller with motion lines, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và thêm một vấn đề nữa: lực kéo toàn bộ cơ thể treo vào đỉnh đầu. Cổ của bạn sẽ không vui chút nào.

```text
Wide 16:9 landscape cinematic frame. a small doodle of a neck with a worried face and an upward arrow, parchment close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Hãy tưởng tượng tiếng ồn nữa. Một cánh quạt đủ mạnh để nâng người sẽ kêu to như máy cắt cỏ ngay trên đầu bạn.…

```text
Wide 16:9 landscape cinematic frame. a humorous doodle of a child covering their ears under a loud buzzing propeller, parchment close-up, playful amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Điểm độ thật của chong chóng tre: ba trên mười. Bay cá nhân là có thật, nhưng không nhỏ gọn, không êm như vậy.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing three out of ten beside a propeller icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Bảo bối 2: Cánh cửa thần kỳ

Lời: Cánh cửa thần kỳ: mở ra là tới bất cứ nơi nào bạn muốn. Không máy bay, không tắc đường.

```text
Wide 16:9 landscape cinematic frame. a single pink-framed door standing alone in a grassy field, slightly open with a beach scene visible through it, wide shot, bright magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Khoa học thật có một thứ nghe giống: dịch chuyển lượng tử. Các nhà khoa học đã truyền được trạng thái của nhữ…

```text
Wide 16:9 landscape cinematic frame. a laboratory table with lasers and optical equipment and two glowing points connected by a faint line, close-up, cool scientific light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nghiên cứu về hiện tượng rối lượng tử, nền tảng của nó, đã được trao giải Nobel Vật lý năm 2022.

```text
Wide 16:9 landscape cinematic frame. a gold medal resting on a stack of physics papers, close-up, warm prestigious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và còn một câu hỏi triết học: nếu một người được tách ra ở chỗ này và tạo lại ở chỗ khác, người ở đầu kia có…

```text
Wide 16:9 landscape cinematic frame. a person hesitating before an open glowing doorway, hand on the frame, back view, medium shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Nhưng thứ được dịch chuyển là thông tin về trạng thái của hạt, không phải bản thân vật chất. Và từ vài hạt tớ…

```text
Wide 16:9 landscape cinematic frame. a single tiny glowing particle beside an enormous silhouette made of countless dots, symbolic comparison, cool light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Điểm độ thật của cánh cửa thần kỳ: một trên mười. Có một hiện tượng khoa học thật mang cùng tên, nhưng còn rấ…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing one out of ten beside a door icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Bảo bối 3: Thạch phiên dịch

Lời: Thạch phiên dịch: ăn một miếng, bạn hiểu và nói được mọi ngôn ngữ, kể cả tiếng của động vật trong vài tập.

```text
Wide 16:9 landscape cinematic frame. a small wobbly jelly block on a plate with tiny speech bubbles in different scripts floating above it, close-up, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Đây là bảo bối gần với đời thật nhất. Ngày nay, điện thoại có thể dịch lời nói gần như tức thời, và có cả tai…

```text
Wide 16:9 landscape cinematic frame. two people from different countries talking with a smartphone between them displaying translated text, medium shot, warm café light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Trí tuệ nhân tạo đã làm cho việc dịch tự động tiến bộ rất nhanh trong vài năm gần đây. Với những câu thông th…

```text
Wide 16:9 landscape cinematic frame. a laptop screen showing a sentence being translated into several languages side by side, close-up, cool screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và dịch máy vẫn có lúc sai với tiếng lóng, câu đùa, hay những từ mang nhiều tầng nghĩa. Thạch phiên dịch tron…

```text
Wide 16:9 landscape cinematic frame. a phone screen showing a funny mistranslation with a confused emoji beside it, close-up, humorous bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Chỗ truyện phóng tay: không cần thiết bị, chỉ cần ăn. Và dịch được cả tiếng động vật. Khoa học chưa hiểu tiến…

```text
Wide 16:9 landscape cinematic frame. a whale surfacing near a small research boat with sound wave graphics drawn above the water, wide shot, soft ocean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Điểm độ thật của thạch phiên dịch: tám trên mười. Chúng ta đã có bảo bối này, chỉ là nó nằm trong điện thoại…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing eight out of ten beside a jelly icon and a phone icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Bảo bối 4: Bánh mì trí nhớ

Lời: Bánh mì trí nhớ: in trang sách lên bánh mì, ăn vào là nhớ. Giấc mơ của mọi học sinh trước kỳ thi.

```text
Wide 16:9 landscape cinematic frame. a slice of bread with tiny printed text on its surface resting on an open textbook, close-up, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Nhưng trong truyện có một chi tiết rất hay: Nobita ăn quá nhiều, bị đau bụng, và mọi thứ vừa nhớ đều mất khi…

```text
Wide 16:9 landscape cinematic frame. a humorous doodle of a stomach with a worried face surrounded by tiny floating letters, parchment close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Ngoài đời, trí nhớ không nằm trong dạ dày. Nó được hình thành bằng cách các tế bào thần kinh trong não tạo và…

```text
Wide 16:9 landscape cinematic frame. a glowing network of neurons with connections lighting up between them, scientific illustration, cool blue light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Mẹo thật mà các nhà khoa học khuyên: học rải ra nhiều ngày, tự kiểm tra bằng cách nhớ lại, và ngủ đủ. Nghe kh…

```text
Wide 16:9 landscape cinematic frame. a study planner with short sessions spread across a week and a small moon icon for sleep, close-up, calm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Có những nghiên cứu về kích thích não để hỗ trợ ghi nhớ, nhưng vẫn còn ở giai đoạn thí nghiệm. Chưa có món ăn…

```text
Wide 16:9 landscape cinematic frame. a laboratory model of a brain with small sensor wires and a notebook of experimental data, close-up, clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Điểm độ thật: một trên mười. Cách thật duy nhất để nhớ là học, ôn lại, và ngủ đủ giấc. Kaku biết, nghe chán h…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing one out of ten beside a bread icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Bảo bối 5: Đèn pin thu nhỏ

Lời: Đèn pin thu nhỏ: chiếu vào đâu, thứ đó nhỏ lại. Nhóm bạn dùng nó để đi phiêu lưu trong những thế giới tí hon.

```text
Wide 16:9 landscape cinematic frame. a flashlight beam shining on a toy car that is shrinking, with sparkles along the beam, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Khoa học có một định luật khiến việc thu nhỏ rất khó: định luật bình phương, lập phương. Khi một vật nhỏ lại,…

```text
Wide 16:9 landscape cinematic frame. a diagram of a large cube and a small cube with their surface areas and volumes labeled, infographic style, clean light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Một người tí hon sẽ mất nhiệt rất nhanh, như những con vật nhỏ phải ăn liên tục để giữ ấm. Và nếu số nguyên t…

```text
Wide 16:9 landscape cinematic frame. a tiny figure shivering on a leaf next to a small mouse eating a seed, humorous close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Khoa học thì làm theo hướng ngược lại: không thu nhỏ người, mà làm những cỗ máy siêu nhỏ, như robot tí hon ha…

```text
Wide 16:9 landscape cinematic frame. a tiny medical capsule device beside a coin for scale on a laboratory tray, extreme close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nếu số nguyên tử giảm đi, thì bộ não tí hon cũng mất bớt tế bào. Bạn sẽ không còn là bạn nữa.

```text
Wide 16:9 landscape cinematic frame. a tiny brain model beside a normal-sized one with a question mark between them, close-up, scientific light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Điểm độ thật: một trên mười. Khoa học có thể làm những cỗ máy rất nhỏ, nhưng không thể thu nhỏ một con người.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing one out of ten beside a flashlight icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Bảo bối 6: Cỗ máy thời gian

Lời: Cỗ máy thời gian nằm trong ngăn kéo bàn học của Nobita. Chui vào ngăn kéo, và bạn có thể đi tới quá khứ hay t…

```text
Wide 16:9 landscape cinematic frame. an open desk drawer with a swirling colorful tunnel of light inside, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Ngoài đời, đi tới tương lai theo một cách nào đó là có thật. Theo thuyết tương đối của Einstein, thời gian tr…

```text
Wide 16:9 landscape cinematic frame. two clocks side by side, one on a fast-moving rocket and one on the ground, showing slightly different times, infographic style, cool light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Bằng chứng nằm ngay trong điện thoại của bạn. Đồng hồ trên vệ tinh GPS chạy nhanh hơn đồng hồ dưới mặt đất kh…

```text
Wide 16:9 landscape cinematic frame. a satellite orbiting Earth with a small clock icon beside it and a map pin on the ground below, wide shot, cool space light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Phi hành gia sống lâu ngày trên trạm vũ trụ cũng già đi chậm hơn người dưới đất một chút xíu, nhỏ tới mức phả…

```text
Wide 16:9 landscape cinematic frame. a space station orbiting above Earth with a tiny clock icon beside it, wide shot, cool space light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhưng mức chênh lệch đó rất nhỏ. Và đi về quá khứ thì khoa học chưa tìm ra cách nào, lại còn gặp rất nhiều ng…

```text
Wide 16:9 landscape cinematic frame. a loop of arrows drawn on parchment with a small crossed-out figure at the center, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Điểm độ thật: hai trên mười. Tương lai thì có một chút, quá khứ thì không.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing two out of ten beside a drawer icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Bảo bối 7: Áo choàng tàng hình

Lời: Áo choàng tàng hình: khoác vào là không ai nhìn thấy. Bảo bối yêu thích của những ai muốn trốn học, hay trốn…

```text
Wide 16:9 landscape cinematic frame. an empty cloak floating in a school hallway with footprints appearing on the floor below it, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Năm 2006, các nhà khoa học ở Đại học Duke giới thiệu áo choàng tàng hình đầu tiên, làm từ siêu vật liệu. Nó b…

```text
Wide 16:9 landscape cinematic frame. a small cylindrical device made of patterned rings on a lab bench with wave lines bending around it, close-up, cool scientific light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nhưng thiết bị chỉ hoạt động với sóng vi ba, không phải ánh sáng nhìn thấy. Và rất khó làm cho nó hoạt động v…

```text
Wide 16:9 landscape cinematic frame. a rainbow spectrum diagram with only a small section highlighted, infographic style, clean light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Quân đội và các nhà khoa học còn phát triển vật liệu giấu nhiệt, để không bị camera hồng ngoại phát hiện. Tàn…

```text
Wide 16:9 landscape cinematic frame. a thermal camera image showing a bright landscape with one area strangely cool and blank, close-up, false-color light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Có những vật liệu ngụy trang thật, như tấm bẻ ánh sáng để làm mờ vật phía sau. Nhưng chúng giống kính đặc biệ…

```text
Wide 16:9 landscape cinematic frame. a sheet of ribbed transparent material in front of a tree making it look blurred and partially hidden, close-up, outdoor daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Điểm độ thật: bốn trên mười. Tàng hình có thật trong phòng thí nghiệm, với vài loại sóng, trong vài điều kiện.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing four out of ten beside a cloak icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Bảo bối 8: Túi thần kỳ

Lời: Và chiếc túi trước bụng Doraemon, túi bốn chiều, chứa được vô số bảo bối, lớn tới đâu cũng vừa.

```text
Wide 16:9 landscape cinematic frame. a small white half-moon pouch with a swirling starry space visible inside it, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Chữ bốn chiều gợi tới toán học: nếu có thêm một chiều không gian, một cái túi có thể chứa nhiều hơn vẻ ngoài…

```text
Wide 16:9 landscape cinematic frame. a flat sheet of paper beside a cardboard box with a ball inside it, infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Các nhà vật lý có bàn tới những chiều không gian thêm trong một số lý thuyết. Nhưng chưa có bằng chứng nào, v…

```text
Wide 16:9 landscape cinematic frame. a chalkboard filled with physics equations and a small doodle of a pouch in the corner, close-up, classroom light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Điểm độ thật: không trên mười. Nhưng Kaku cho thêm một điểm phụ, vì chiếc ba lô đi học của Kaku cũng chứa đượ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling an impossibly long scarf out of a tiny backpack. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Bảo bối 9: Khăn trùm thời gian

Lời: Khăn trùm thời gian: trùm lên một vật, nó trở về trạng thái mới tinh. Trùm lâu hơn, nó quay về trạng thái trư…

```text
Wide 16:9 landscape cinematic frame. a colorful cloth draped over an old broken toy, with sparkles suggesting it is becoming new again, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Ngoài đời, ta có những kỹ thuật phục chế đồ cũ rất giỏi, và khoa học vật liệu làm được những lớp phủ tự lành…

```text
Wide 16:9 landscape cinematic frame. a craftsman carefully restoring an antique wooden chair in a workshop, medium shot, warm workshop light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nhưng đảo ngược quá trình lão hóa của vật chất hay của cơ thể thì vẫn là một thách thức rất lớn. Có nhiều ngh…

```text
Wide 16:9 landscape cinematic frame. a flashy miracle product advertisement with a large red warning stamp across it, close-up, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Điểm độ thật: hai trên mười. Sửa được, làm mới được bề mặt, nhưng không quay ngược thời gian.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing two out of ten beside a cloth icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Bảo bối 10: chính Doraemon

Lời: Và bảo bối cuối cùng, cũng là bảo bối lớn nhất: chính Doraemon. Một chú mèo máy biết nói, biết buồn, biết giậ…

```text
Wide 16:9 landscape cinematic frame. a round friendly robot cat silhouette sitting beside a sleeping child in a cozy bedroom at night, wide shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Ngày nay, chúng ta đã có robot đi lại được, robot trò chuyện được, và những trợ lý trí tuệ nhân tạo có thể nó…

```text
Wide 16:9 landscape cinematic frame. a humanoid robot walking in a bright laboratory beside a tablet displaying a chat interface, wide shot, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Nhật Bản còn có những robot chăm sóc người già, robot thú cưng, và cả robot đồng hành cho trẻ em. Giấc mơ về…

```text
Wide 16:9 landscape cinematic frame. a small robot pet sitting on the lap of an elderly person in a cozy living room, medium shot, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nhưng một người bạn máy thật sự hiểu và quan tâm tới bạn như Doraemon, có cảm xúc thật, thì vẫn là câu hỏi mà…

```text
Wide 16:9 landscape cinematic frame. a robot hand and a child's hand almost touching, with a question mark drawn in the space between, symbolic close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Điểm độ thật: năm trên mười. Phần thân máy và giọng nói đang tới gần. Phần trái tim thì còn rất xa.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing five out of ten beside a small robot icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Hai bảo bối tặng thêm

Lời: Kaku tặng thêm hai bảo bối nhanh. Bảo bối mười một: cây bút chì tự làm bài. Cầm bút, nó tự viết đáp án đúng.

```text
Wide 16:9 landscape cinematic frame. a pencil writing on its own across a homework sheet with small sparkles along the tip, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Ngày nay, trí tuệ nhân tạo có thể giải rất nhiều bài tập. Về kỹ thuật, bảo bối này gần thành thật rồi: bảy tr…

```text
Wide 16:9 landscape cinematic frame. a tablet showing a solved math problem beside an untouched textbook gathering dust, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Bảo bối mười hai: điều khiển thời tiết. Muốn mưa là mưa, muốn nắng là nắng.

```text
Wide 16:9 landscape cinematic frame. a small control panel with sun, cloud and rain buttons floating in front of a changing sky, wide shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Ngoài đời có kỹ thuật gieo mây: rải những hạt nhỏ như bạc iodua vào mây để kích thích mưa. Nó chỉ tăng khả nă…

```text
Wide 16:9 landscape cinematic frame. a small aircraft flying through grey clouds releasing a faint trail of particles, wide shot, overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Bảng điểm độ thật

Lời: Tổng kết bảng điểm. Thạch phiên dịch: tám. Chính Doraemon: năm. Áo choàng tàng hình: bốn. Chong chóng tre: ba.

```text
Wide 16:9 landscape cinematic frame. a ranked scoreboard on parchment with small gadget icons and their scores, top half filled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Cỗ máy thời gian và khăn trùm thời gian: hai. Cánh cửa thần kỳ, bánh mì trí nhớ, đèn pin thu nhỏ: một. Túi bố…

```text
Wide 16:9 landscape cinematic frame. the completed scoreboard with the bottom half filled and a small smiley sticker beside the last entry, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Hai bảo bối tặng thêm: bút chì tự làm bài bảy điểm, điều khiển thời tiết ba điểm. Nghĩa là bảo bối thật nhất…

```text
Wide 16:9 landscape cinematic frame. two small bonus entries added to the bottom of the scoreboard in a different ink color, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Điều thú vị: bảo bối thật nhất là bảo bối giúp con người hiểu nhau, còn những bảo bối kém thật nhất là những…

```text
Wide 16:9 landscape cinematic frame. two paths drawn on a map, a short shortcut path crossed out and a longer winding path with footprints, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Góc nhìn của Kaku

Lời: Nhiều tập truyện kết thúc bằng cảnh bảo bối gây họa, và Nobita phải tự sửa sai. Tác giả đã dùng những món đồ…

```text
Wide 16:9 landscape cinematic frame. a small broken gadget on a desk beside a child's handwritten apology note, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Kaku nghĩ đó chính là bài học của Doraemon. Bảo bối nào cũng giúp Nobita thoát khỏi rắc rối, nhưng rồi cũng t…

```text
Wide 16:9 landscape cinematic frame. a child's small shoes beside a pair of adult shoes at a doorway, symbolic close-up, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và có lẽ vì vậy mà Doraemon vẫn được yêu hơn năm mươi năm. Không phải vì chiếc túi, mà vì người bạn luôn ở bê…

```text
Wide 16:9 landscape cinematic frame. a robot cat silhouette and a child sitting together on a grassy hill watching the sunset, back view, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu được chọn một bảo bối có thật trong tương lai, bạn muốn các nhà khoa học làm ra cái nào trước? Viết vào b…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny pouch doodle and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Kết

Lời: Và nếu bạn là người lớn, hãy thử kể cho một đứa trẻ nghe về Doraemon. Có thể bạn sẽ là người truyền lại chiếc…

```text
Wide 16:9 landscape cinematic frame. an adult and a child sitting together reading an old comic book on a sofa, medium shot, warm cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Video tiếp theo, Kaku vẽ một cây phả hệ đầy ngôi sao: dòng họ Joestar trong JoJo, và vết bớt hình ngôi sao tr…

```text
Wide 16:9 landscape cinematic frame. an old family tree drawing with small star marks beside each name, parchment close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video khoa học vui như thế này, hãy đăng ký kênh. Kaku không có túi thần kỳ, nhưng có một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing its notebook and tucking it into a tiny pouch with a satisfied smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Doraemon ở Việt Nam

Khoảng 125 giây · cảnh s01–s10 · 1620 ký tự

**Gemini**

```text
Video này gần như không có spoiler, chỉ nói về các bảo bối quen thuộc. Và Kaku nhắc trước: đây là video khoa học vui, không phải hướng dẫn chế tạo. Đừng thử bay bằng quạt nhé.

<short pause> Nếu được chọn một bảo bối của Doraemon, bạn chọn gì? Chong chóng tre để bay đi học? Cánh cửa thần kỳ để khỏi tắc đường? Hay bánh mì trí nhớ trước ngày thi?

<short pause> Trẻ em Việt Nam hỏi câu này suốt hơn ba mươi năm, từ khi truyện Đôrêmon đến Việt Nam năm 1992. Hôm nay Kaku hỏi một câu khác: bảo bối nào có thể làm được ngoài đời thật?

<short pause> Và đúng dịp này, ngày năm tháng ba năm 2027, bộ phim Doraemon mới ra rạp ở Nhật. Một thời điểm hoàn hảo để mở túi thần kỳ ra xem.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku chấm mười bảo bối theo thang điểm độ thật từ không tới mười: trong truyện làm gì, khoa học thật tới đâu, và truyện phóng tay ở chỗ nào.

<short pause> Doraemon là manga của Fujiko F. Fujio, xuất hiện lần đầu vào tháng mười hai năm 1969, cùng lúc trên sáu tạp chí. Chú mèo máy trong truyện sinh ngày ba tháng chín năm 2112.

<short pause> Trước khi mở túi, một chút lịch sử. Mùa đông năm 1992, Nhà xuất bản Kim Đồng phát hành truyện Đôrêmon ở Việt Nam. Chỉ sau một tuần, bốn tập đầu bán được bốn mươi nghìn bản.

<short pause> Những bản đầu tiên ra đời khi chưa có bản quyền chính thức. Về sau, Kim Đồng làm việc với nhà xuất bản Nhật để phát hành chính thức, và truyện gắn với tuổi thơ của nhiều thế hệ.

<short pause> Người Việt còn nhớ những cái tên được Việt hóa: Nobita, Xuka, Chaien, Xêkô. Với nhiều người, đó là những người bạn đầu tiên trong thế giới truyện tranh.

<short pause> Kaku để ý: gần như mọi bảo bối trong video này, bạn đều đã từng ước có ít nhất một lần. Hôm nay, ta thử hỏi khoa học xem điều ước đó xa tới đâu.
```

**ElevenLabs**

```text
Video này gần như không có spoiler, chỉ nói về các bảo bối quen thuộc. Và Kaku nhắc trước: đây là video khoa học vui, không phải hướng dẫn chế tạo. Đừng thử bay bằng quạt nhé.

[pause] [curious] Nếu được chọn một bảo bối của Doraemon, bạn chọn gì? Chong chóng tre để bay đi học? Cánh cửa thần kỳ để khỏi tắc đường? Hay bánh mì trí nhớ trước ngày thi?

[pause] Trẻ em Việt Nam hỏi câu này suốt hơn ba mươi năm, từ khi truyện Đôrêmon đến Việt Nam năm 1992. Hôm nay Kaku hỏi một câu khác: bảo bối nào có thể làm được ngoài đời thật?

[pause] Và đúng dịp này, ngày năm tháng ba năm 2027, bộ phim Doraemon mới ra rạp ở Nhật. Một thời điểm hoàn hảo để mở túi thần kỳ ra xem.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku chấm mười bảo bối theo thang điểm độ thật từ không tới mười: trong truyện làm gì, khoa học thật tới đâu, và truyện phóng tay ở chỗ nào.

[pause] Doraemon là manga của Fujiko F. Fujio, xuất hiện lần đầu vào tháng mười hai năm 1969, cùng lúc trên sáu tạp chí. Chú mèo máy trong truyện sinh ngày ba tháng chín năm 2112.

[pause] Trước khi mở túi, một chút lịch sử. Mùa đông năm 1992, Nhà xuất bản Kim Đồng phát hành truyện Đôrêmon ở Việt Nam. Chỉ sau một tuần, bốn tập đầu bán được bốn mươi nghìn bản.

[pause] Những bản đầu tiên ra đời khi chưa có bản quyền chính thức. Về sau, Kim Đồng làm việc với nhà xuất bản Nhật để phát hành chính thức, và truyện gắn với tuổi thơ của nhiều thế hệ.

[pause] Người Việt còn nhớ những cái tên được Việt hóa: Nobita, Xuka, Chaien, Xêkô. Với nhiều người, đó là những người bạn đầu tiên trong thế giới truyện tranh.

[pause] Kaku để ý: gần như mọi bảo bối trong video này, bạn đều đã từng ước có ít nhất một lần. Hôm nay, ta thử hỏi khoa học xem điều ước đó xa tới đâu.
```

### c02 · Bảo bối 1: Chong chóng tre / Bảo bối 2: Cánh cửa thần kỳ

Khoảng 135 giây · cảnh s11–s23 · 1756 ký tự

**Gemini**

```text
Bảo bối nổi tiếng nhất: chong chóng tre. Gắn lên đầu, chong chóng quay, và bạn bay lên. Nobita, Xuka, Chaien, Xêkô đều dùng nó để đi chơi.

<short pause> Ngoài đời, con người đã bay bằng cánh quạt: trực thăng, và gần đây là những chiếc drone chở người. Nguyên lý giống nhau: cánh quạt đẩy không khí xuống, không khí đẩy máy lên.

<short pause> Nhưng có hai vấn đề. Một: để nâng một người, cánh quạt phải rất lớn và rất mạnh, không thể nhỏ như chiếc chong chóng trên đầu.

<short pause> Hai: khi cánh quạt quay, nó đẩy ngược lại thứ gắn với nó. Đó là lý do trực thăng cần cánh quạt đuôi. Không có nó, người đội chong chóng sẽ tự xoay tít như con quay.

<short pause> Và thêm một vấn đề nữa: lực kéo toàn bộ cơ thể treo vào đỉnh đầu. Cổ của bạn sẽ không vui chút nào.

<short pause> Hãy tưởng tượng tiếng ồn nữa. Một cánh quạt đủ mạnh để nâng người sẽ kêu to như máy cắt cỏ ngay trên đầu bạn. Trong truyện, chong chóng tre bay êm ru.

<short pause> Điểm độ thật của chong chóng tre: ba trên mười. Bay cá nhân là có thật, nhưng không nhỏ gọn, không êm như vậy.

<short pause> Cánh cửa thần kỳ: mở ra là tới bất cứ nơi nào bạn muốn. Không máy bay, không tắc đường.

<short pause> Khoa học thật có một thứ nghe giống: dịch chuyển lượng tử. Các nhà khoa học đã truyền được trạng thái của những hạt rất nhỏ từ nơi này sang nơi khác.

<short pause> Nghiên cứu về hiện tượng rối lượng tử, nền tảng của nó, đã được trao giải Nobel Vật lý năm 2022.

<short pause> Và còn một câu hỏi triết học: nếu một người được tách ra ở chỗ này và tạo lại ở chỗ khác, người ở đầu kia có còn là bạn không? Nhiều người sẽ ngại bước qua cánh cửa đó.

<short pause> Nhưng thứ được dịch chuyển là thông tin về trạng thái của hạt, không phải bản thân vật chất. Và từ vài hạt tới một con người gồm hàng tỉ tỉ nguyên tử là một khoảng cách không tưởng.

<short pause> Điểm độ thật của cánh cửa thần kỳ: một trên mười. Có một hiện tượng khoa học thật mang cùng tên, nhưng còn rất xa.
```

**ElevenLabs**

```text
Bảo bối nổi tiếng nhất: chong chóng tre. Gắn lên đầu, chong chóng quay, và bạn bay lên. Nobita, Xuka, Chaien, Xêkô đều dùng nó để đi chơi.

[pause] Ngoài đời, con người đã bay bằng cánh quạt: trực thăng, và gần đây là những chiếc drone chở người. Nguyên lý giống nhau: cánh quạt đẩy không khí xuống, không khí đẩy máy lên.

[pause] Nhưng có hai vấn đề. Một: để nâng một người, cánh quạt phải rất lớn và rất mạnh, không thể nhỏ như chiếc chong chóng trên đầu.

[pause] Hai: khi cánh quạt quay, nó đẩy ngược lại thứ gắn với nó. Đó là lý do trực thăng cần cánh quạt đuôi. Không có nó, người đội chong chóng sẽ tự xoay tít như con quay.

[pause] Và thêm một vấn đề nữa: lực kéo toàn bộ cơ thể treo vào đỉnh đầu. Cổ của bạn sẽ không vui chút nào.

[pause] Hãy tưởng tượng tiếng ồn nữa. Một cánh quạt đủ mạnh để nâng người sẽ kêu to như máy cắt cỏ ngay trên đầu bạn. Trong truyện, chong chóng tre bay êm ru.

[pause] Điểm độ thật của chong chóng tre: ba trên mười. Bay cá nhân là có thật, nhưng không nhỏ gọn, không êm như vậy.

[pause] Cánh cửa thần kỳ: mở ra là tới bất cứ nơi nào bạn muốn. Không máy bay, không tắc đường.

[pause] Khoa học thật có một thứ nghe giống: dịch chuyển lượng tử. Các nhà khoa học đã truyền được trạng thái của những hạt rất nhỏ từ nơi này sang nơi khác.

[pause] Nghiên cứu về hiện tượng rối lượng tử, nền tảng của nó, đã được trao giải Nobel Vật lý năm 2022.

[pause] [curious] Và còn một câu hỏi triết học: nếu một người được tách ra ở chỗ này và tạo lại ở chỗ khác, người ở đầu kia có còn là bạn không? Nhiều người sẽ ngại bước qua cánh cửa đó.

[pause] Nhưng thứ được dịch chuyển là thông tin về trạng thái của hạt, không phải bản thân vật chất. Và từ vài hạt tới một con người gồm hàng tỉ tỉ nguyên tử là một khoảng cách không tưởng.

[pause] Điểm độ thật của cánh cửa thần kỳ: một trên mười. Có một hiện tượng khoa học thật mang cùng tên, nhưng còn rất xa.
```

### c03 · Bảo bối 3: Thạch phiên dịch / Bảo bối 4: Bánh mì trí nhớ

Khoảng 131 giây · cảnh s24–s35 · 1708 ký tự

**Gemini**

```text
Thạch phiên dịch: ăn một miếng, bạn hiểu và nói được mọi ngôn ngữ, kể cả tiếng của động vật trong vài tập.

<short pause> Đây là bảo bối gần với đời thật nhất. Ngày nay, điện thoại có thể dịch lời nói gần như tức thời, và có cả tai nghe dịch trực tiếp cuộc hội thoại.

<short pause> Trí tuệ nhân tạo đã làm cho việc dịch tự động tiến bộ rất nhanh trong vài năm gần đây. Với những câu thông thường, bản dịch đã khá tự nhiên.

<short pause> Và dịch máy vẫn có lúc sai với tiếng lóng, câu đùa, hay những từ mang nhiều tầng nghĩa. Thạch phiên dịch trong truyện thì không bao giờ sai.

<short pause> Chỗ truyện phóng tay: không cần thiết bị, chỉ cần ăn. Và dịch được cả tiếng động vật. Khoa học chưa hiểu tiếng động vật tới mức đó, dù đã có nghiên cứu về cách cá voi hay chim giao tiếp.

<short pause> Điểm độ thật của thạch phiên dịch: tám trên mười. Chúng ta đã có bảo bối này, chỉ là nó nằm trong điện thoại chứ không nằm trong đĩa thạch.

<short pause> Bánh mì trí nhớ: in trang sách lên bánh mì, ăn vào là nhớ. Giấc mơ của mọi học sinh trước kỳ thi.

<short pause> Nhưng trong truyện có một chi tiết rất hay: Nobita ăn quá nhiều, bị đau bụng, và mọi thứ vừa nhớ đều mất khi cậu đi vệ sinh. Truyện tự chế giễu chính bảo bối của mình.

<short pause> Ngoài đời, trí nhớ không nằm trong dạ dày. Nó được hình thành bằng cách các tế bào thần kinh trong não tạo và củng cố kết nối, và giấc ngủ đóng vai trò rất quan trọng.

<short pause> Mẹo thật mà các nhà khoa học khuyên: học rải ra nhiều ngày, tự kiểm tra bằng cách nhớ lại, và ngủ đủ. Nghe không thần kỳ, nhưng hiệu quả hơn nhồi nhét cả đêm.

<short pause> Có những nghiên cứu về kích thích não để hỗ trợ ghi nhớ, nhưng vẫn còn ở giai đoạn thí nghiệm. Chưa có món ăn nào giúp bạn học thuộc bài.

<short pause> Điểm độ thật: một trên mười. Cách thật duy nhất để nhớ là học, ôn lại, và ngủ đủ giấc. Kaku biết, nghe chán hơn bánh mì nhiều.
```

**ElevenLabs**

```text
Thạch phiên dịch: ăn một miếng, bạn hiểu và nói được mọi ngôn ngữ, kể cả tiếng của động vật trong vài tập.

[pause] Đây là bảo bối gần với đời thật nhất. Ngày nay, điện thoại có thể dịch lời nói gần như tức thời, và có cả tai nghe dịch trực tiếp cuộc hội thoại.

[pause] Trí tuệ nhân tạo đã làm cho việc dịch tự động tiến bộ rất nhanh trong vài năm gần đây. Với những câu thông thường, bản dịch đã khá tự nhiên.

[pause] Và dịch máy vẫn có lúc sai với tiếng lóng, câu đùa, hay những từ mang nhiều tầng nghĩa. Thạch phiên dịch trong truyện thì không bao giờ sai.

[pause] Chỗ truyện phóng tay: không cần thiết bị, chỉ cần ăn. Và dịch được cả tiếng động vật. Khoa học chưa hiểu tiếng động vật tới mức đó, dù đã có nghiên cứu về cách cá voi hay chim giao tiếp.

[pause] Điểm độ thật của thạch phiên dịch: tám trên mười. Chúng ta đã có bảo bối này, chỉ là nó nằm trong điện thoại chứ không nằm trong đĩa thạch.

[pause] Bánh mì trí nhớ: in trang sách lên bánh mì, ăn vào là nhớ. Giấc mơ của mọi học sinh trước kỳ thi.

[pause] Nhưng trong truyện có một chi tiết rất hay: Nobita ăn quá nhiều, bị đau bụng, và mọi thứ vừa nhớ đều mất khi cậu đi vệ sinh. Truyện tự chế giễu chính bảo bối của mình.

[pause] Ngoài đời, trí nhớ không nằm trong dạ dày. Nó được hình thành bằng cách các tế bào thần kinh trong não tạo và củng cố kết nối, và giấc ngủ đóng vai trò rất quan trọng.

[pause] Mẹo thật mà các nhà khoa học khuyên: học rải ra nhiều ngày, tự kiểm tra bằng cách nhớ lại, và ngủ đủ. Nghe không thần kỳ, nhưng hiệu quả hơn nhồi nhét cả đêm.

[pause] Có những nghiên cứu về kích thích não để hỗ trợ ghi nhớ, nhưng vẫn còn ở giai đoạn thí nghiệm. Chưa có món ăn nào giúp bạn học thuộc bài.

[pause] Điểm độ thật: một trên mười. Cách thật duy nhất để nhớ là học, ôn lại, và ngủ đủ giấc. Kaku biết, nghe chán hơn bánh mì nhiều.
```

### c04 · Bảo bối 5: Đèn pin thu nhỏ / Bảo bối 6: Cỗ máy thời gian

Khoảng 134 giây · cảnh s36–s47 · 1740 ký tự

**Gemini**

```text
Đèn pin thu nhỏ: chiếu vào đâu, thứ đó nhỏ lại. Nhóm bạn dùng nó để đi phiêu lưu trong những thế giới tí hon.

<short pause> Khoa học có một định luật khiến việc thu nhỏ rất khó: định luật bình phương, lập phương. Khi một vật nhỏ lại, thể tích giảm nhanh hơn diện tích bề mặt rất nhiều.

<short pause> Một người tí hon sẽ mất nhiệt rất nhanh, như những con vật nhỏ phải ăn liên tục để giữ ấm. Và nếu số nguyên tử giữ nguyên, người tí hon vẫn nặng như cũ.

<short pause> Khoa học thì làm theo hướng ngược lại: không thu nhỏ người, mà làm những cỗ máy siêu nhỏ, như robot tí hon hay thiết bị y tế có thể đi vào cơ thể. Chuyến phiêu lưu tí hon, nhưng không có người ngồi trong.

<short pause> Nếu số nguyên tử giảm đi, thì bộ não tí hon cũng mất bớt tế bào. Bạn sẽ không còn là bạn nữa.

<short pause> Điểm độ thật: một trên mười. Khoa học có thể làm những cỗ máy rất nhỏ, nhưng không thể thu nhỏ một con người.

<short pause> Cỗ máy thời gian nằm trong ngăn kéo bàn học của Nobita. Chui vào ngăn kéo, và bạn có thể đi tới quá khứ hay tương lai.

<short pause> Ngoài đời, đi tới tương lai theo một cách nào đó là có thật. Theo thuyết tương đối của Einstein, thời gian trôi chậm hơn khi bạn di chuyển rất nhanh, hoặc ở gần một vật rất nặng.

<short pause> Bằng chứng nằm ngay trong điện thoại của bạn. Đồng hồ trên vệ tinh GPS chạy nhanh hơn đồng hồ dưới mặt đất khoảng ba mươi tám micro giây mỗi ngày. Nếu không hiệu chỉnh, định vị sẽ lệch khoảng mười cây số mỗi ngày.

<short pause> Phi hành gia sống lâu ngày trên trạm vũ trụ cũng già đi chậm hơn người dưới đất một chút xíu, nhỏ tới mức phải đo bằng những đồng hồ cực kỳ chính xác. Du hành tới tương lai có thật, nhưng chỉ vài phần nghìn giây.

<short pause> Nhưng mức chênh lệch đó rất nhỏ. Và đi về quá khứ thì khoa học chưa tìm ra cách nào, lại còn gặp rất nhiều nghịch lý.

<short pause> Điểm độ thật: hai trên mười. Tương lai thì có một chút, quá khứ thì không.
```

**ElevenLabs**

```text
Đèn pin thu nhỏ: chiếu vào đâu, thứ đó nhỏ lại. Nhóm bạn dùng nó để đi phiêu lưu trong những thế giới tí hon.

[pause] Khoa học có một định luật khiến việc thu nhỏ rất khó: định luật bình phương, lập phương. Khi một vật nhỏ lại, thể tích giảm nhanh hơn diện tích bề mặt rất nhiều.

[pause] Một người tí hon sẽ mất nhiệt rất nhanh, như những con vật nhỏ phải ăn liên tục để giữ ấm. Và nếu số nguyên tử giữ nguyên, người tí hon vẫn nặng như cũ.

[pause] Khoa học thì làm theo hướng ngược lại: không thu nhỏ người, mà làm những cỗ máy siêu nhỏ, như robot tí hon hay thiết bị y tế có thể đi vào cơ thể. Chuyến phiêu lưu tí hon, nhưng không có người ngồi trong.

[pause] Nếu số nguyên tử giảm đi, thì bộ não tí hon cũng mất bớt tế bào. Bạn sẽ không còn là bạn nữa.

[pause] Điểm độ thật: một trên mười. Khoa học có thể làm những cỗ máy rất nhỏ, nhưng không thể thu nhỏ một con người.

[pause] Cỗ máy thời gian nằm trong ngăn kéo bàn học của Nobita. Chui vào ngăn kéo, và bạn có thể đi tới quá khứ hay tương lai.

[pause] Ngoài đời, đi tới tương lai theo một cách nào đó là có thật. Theo thuyết tương đối của Einstein, thời gian trôi chậm hơn khi bạn di chuyển rất nhanh, hoặc ở gần một vật rất nặng.

[pause] Bằng chứng nằm ngay trong điện thoại của bạn. Đồng hồ trên vệ tinh GPS chạy nhanh hơn đồng hồ dưới mặt đất khoảng ba mươi tám micro giây mỗi ngày. Nếu không hiệu chỉnh, định vị sẽ lệch khoảng mười cây số mỗi ngày.

[pause] Phi hành gia sống lâu ngày trên trạm vũ trụ cũng già đi chậm hơn người dưới đất một chút xíu, nhỏ tới mức phải đo bằng những đồng hồ cực kỳ chính xác. Du hành tới tương lai có thật, nhưng chỉ vài phần nghìn giây.

[pause] Nhưng mức chênh lệch đó rất nhỏ. Và đi về quá khứ thì khoa học chưa tìm ra cách nào, lại còn gặp rất nhiều nghịch lý.

[pause] Điểm độ thật: hai trên mười. Tương lai thì có một chút, quá khứ thì không.
```

### c05 · Bảo bối 7: Áo choàng tàng hình / Bảo bối 8: Túi thần kỳ

Khoảng 114 giây · cảnh s48–s57 · 1488 ký tự

**Gemini**

```text
Áo choàng tàng hình: khoác vào là không ai nhìn thấy. Bảo bối yêu thích của những ai muốn trốn học, hay trốn Chaien.

<short pause> Năm 2006, các nhà khoa học ở Đại học Duke giới thiệu áo choàng tàng hình đầu tiên, làm từ siêu vật liệu. Nó bẻ cong sóng vi ba đi vòng qua một vật, như thể vật đó không có ở đó.

<short pause> Nhưng thiết bị chỉ hoạt động với sóng vi ba, không phải ánh sáng nhìn thấy. Và rất khó làm cho nó hoạt động với mọi màu, mọi góc nhìn cùng lúc.

<short pause> Quân đội và các nhà khoa học còn phát triển vật liệu giấu nhiệt, để không bị camera hồng ngoại phát hiện. Tàng hình không nhất thiết là biến mất trước mắt, mà là không bị cảm biến nhìn thấy.

<short pause> Có những vật liệu ngụy trang thật, như tấm bẻ ánh sáng để làm mờ vật phía sau. <short pause> Nhưng chúng giống kính đặc biệt hơn là một chiếc áo biến mất hoàn toàn.

<short pause> Điểm độ thật: bốn trên mười. Tàng hình có thật trong phòng thí nghiệm, với vài loại sóng, trong vài điều kiện.

<short pause> Và chiếc túi trước bụng Doraemon, túi bốn chiều, chứa được vô số bảo bối, lớn tới đâu cũng vừa.

<short pause> Chữ bốn chiều gợi tới toán học: nếu có thêm một chiều không gian, một cái túi có thể chứa nhiều hơn vẻ ngoài của nó. Giống như một tờ giấy phẳng không thể chứa một quả bóng, nhưng một chiếc hộp thì có thể.

<short pause> Các nhà vật lý có bàn tới những chiều không gian thêm trong một số lý thuyết. <short pause> Nhưng chưa có bằng chứng nào, và càng chưa có cách nào tạo ra một cái túi dẫn vào đó.

<short pause> Điểm độ thật: không trên mười. <short pause> <laugh> Nhưng Kaku cho thêm một điểm phụ, vì chiếc ba lô đi học của Kaku cũng chứa được nhiều thứ một cách khó hiểu.
```

**ElevenLabs**

```text
Áo choàng tàng hình: khoác vào là không ai nhìn thấy. Bảo bối yêu thích của những ai muốn trốn học, hay trốn Chaien.

[pause] Năm 2006, các nhà khoa học ở Đại học Duke giới thiệu áo choàng tàng hình đầu tiên, làm từ siêu vật liệu. Nó bẻ cong sóng vi ba đi vòng qua một vật, như thể vật đó không có ở đó.

[pause] Nhưng thiết bị chỉ hoạt động với sóng vi ba, không phải ánh sáng nhìn thấy. Và rất khó làm cho nó hoạt động với mọi màu, mọi góc nhìn cùng lúc.

[pause] Quân đội và các nhà khoa học còn phát triển vật liệu giấu nhiệt, để không bị camera hồng ngoại phát hiện. Tàng hình không nhất thiết là biến mất trước mắt, mà là không bị cảm biến nhìn thấy.

[pause] Có những vật liệu ngụy trang thật, như tấm bẻ ánh sáng để làm mờ vật phía sau. [pause] Nhưng chúng giống kính đặc biệt hơn là một chiếc áo biến mất hoàn toàn.

[pause] Điểm độ thật: bốn trên mười. Tàng hình có thật trong phòng thí nghiệm, với vài loại sóng, trong vài điều kiện.

[pause] Và chiếc túi trước bụng Doraemon, túi bốn chiều, chứa được vô số bảo bối, lớn tới đâu cũng vừa.

[pause] Chữ bốn chiều gợi tới toán học: nếu có thêm một chiều không gian, một cái túi có thể chứa nhiều hơn vẻ ngoài của nó. Giống như một tờ giấy phẳng không thể chứa một quả bóng, nhưng một chiếc hộp thì có thể.

[pause] Các nhà vật lý có bàn tới những chiều không gian thêm trong một số lý thuyết. [pause] Nhưng chưa có bằng chứng nào, và càng chưa có cách nào tạo ra một cái túi dẫn vào đó.

[pause] Điểm độ thật: không trên mười. [pause] [chuckles] Nhưng Kaku cho thêm một điểm phụ, vì chiếc ba lô đi học của Kaku cũng chứa được nhiều thứ một cách khó hiểu.
```

### c06 · Bảo bối 9: Khăn trùm thời gian / Bảo bối 10: chính Doraemon / Hai bảo bối tặng thêm

Khoảng 140 giây · cảnh s58–s70 · 1818 ký tự

**Gemini**

```text
Khăn trùm thời gian: trùm lên một vật, nó trở về trạng thái mới tinh. Trùm lâu hơn, nó quay về trạng thái trước khi được làm ra. Đổi mặt khăn, vật cũ đi.

<short pause> Ngoài đời, ta có những kỹ thuật phục chế đồ cũ rất giỏi, và khoa học vật liệu làm được những lớp phủ tự lành vết xước.

<short pause> Nhưng đảo ngược quá trình lão hóa của vật chất hay của cơ thể thì vẫn là một thách thức rất lớn. Có nhiều nghiên cứu về lão hóa, nhưng mọi quảng cáo trẻ hóa thần kỳ đều đáng nghi ngờ.

<short pause> Điểm độ thật: hai trên mười. Sửa được, làm mới được bề mặt, nhưng không quay ngược thời gian.

<short pause> Và bảo bối cuối cùng, cũng là bảo bối lớn nhất: chính Doraemon. Một chú mèo máy biết nói, biết buồn, biết giận, biết chăm sóc một cậu bé vụng về.

<short pause> Ngày nay, chúng ta đã có robot đi lại được, robot trò chuyện được, và những trợ lý trí tuệ nhân tạo có thể nói chuyện khá tự nhiên.

<short pause> Nhật Bản còn có những robot chăm sóc người già, robot thú cưng, và cả robot đồng hành cho trẻ em. Giấc mơ về một Doraemon đã truyền cảm hứng cho không ít kỹ sư robot Nhật.

<short pause> Nhưng một người bạn máy thật sự hiểu và quan tâm tới bạn như Doraemon, có cảm xúc thật, thì vẫn là câu hỏi mà các nhà khoa học và triết học còn tranh luận.

<short pause> Điểm độ thật: năm trên mười. Phần thân máy và giọng nói đang tới gần. Phần trái tim thì còn rất xa.

<short pause> Kaku tặng thêm hai bảo bối nhanh. Bảo bối mười một: cây bút chì tự làm bài. Cầm bút, nó tự viết đáp án đúng.

<short pause> Ngày nay, trí tuệ nhân tạo có thể giải rất nhiều bài tập. Về kỹ thuật, bảo bối này gần thành thật rồi: bảy trên mười. <short pause> Nhưng giống như trong truyện, nếu để bút làm hết, bạn sẽ không học được gì.

<short pause> Bảo bối mười hai: điều khiển thời tiết. Muốn mưa là mưa, muốn nắng là nắng.

<short pause> Ngoài đời có kỹ thuật gieo mây: rải những hạt nhỏ như bạc iodua vào mây để kích thích mưa. Nó chỉ tăng khả năng mưa khi đã có mây phù hợp, không tạo mưa từ bầu trời trong. Độ thật: ba trên mười.
```

**ElevenLabs**

```text
Khăn trùm thời gian: trùm lên một vật, nó trở về trạng thái mới tinh. Trùm lâu hơn, nó quay về trạng thái trước khi được làm ra. Đổi mặt khăn, vật cũ đi.

[pause] Ngoài đời, ta có những kỹ thuật phục chế đồ cũ rất giỏi, và khoa học vật liệu làm được những lớp phủ tự lành vết xước.

[pause] Nhưng đảo ngược quá trình lão hóa của vật chất hay của cơ thể thì vẫn là một thách thức rất lớn. Có nhiều nghiên cứu về lão hóa, nhưng mọi quảng cáo trẻ hóa thần kỳ đều đáng nghi ngờ.

[pause] Điểm độ thật: hai trên mười. Sửa được, làm mới được bề mặt, nhưng không quay ngược thời gian.

[pause] Và bảo bối cuối cùng, cũng là bảo bối lớn nhất: chính Doraemon. Một chú mèo máy biết nói, biết buồn, biết giận, biết chăm sóc một cậu bé vụng về.

[pause] Ngày nay, chúng ta đã có robot đi lại được, robot trò chuyện được, và những trợ lý trí tuệ nhân tạo có thể nói chuyện khá tự nhiên.

[pause] Nhật Bản còn có những robot chăm sóc người già, robot thú cưng, và cả robot đồng hành cho trẻ em. Giấc mơ về một Doraemon đã truyền cảm hứng cho không ít kỹ sư robot Nhật.

[pause] Nhưng một người bạn máy thật sự hiểu và quan tâm tới bạn như Doraemon, có cảm xúc thật, thì vẫn là câu hỏi mà các nhà khoa học và triết học còn tranh luận.

[pause] Điểm độ thật: năm trên mười. Phần thân máy và giọng nói đang tới gần. Phần trái tim thì còn rất xa.

[pause] Kaku tặng thêm hai bảo bối nhanh. Bảo bối mười một: cây bút chì tự làm bài. Cầm bút, nó tự viết đáp án đúng.

[pause] Ngày nay, trí tuệ nhân tạo có thể giải rất nhiều bài tập. Về kỹ thuật, bảo bối này gần thành thật rồi: bảy trên mười. [pause] Nhưng giống như trong truyện, nếu để bút làm hết, bạn sẽ không học được gì.

[pause] Bảo bối mười hai: điều khiển thời tiết. Muốn mưa là mưa, muốn nắng là nắng.

[pause] Ngoài đời có kỹ thuật gieo mây: rải những hạt nhỏ như bạc iodua vào mây để kích thích mưa. Nó chỉ tăng khả năng mưa khi đã có mây phù hợp, không tạo mưa từ bầu trời trong. Độ thật: ba trên mười.
```

### c07 · Bảng điểm độ thật / Góc nhìn của Kaku / Kết

Khoảng 126 giây · cảnh s71–s81 · 1634 ký tự

**Gemini**

```text
Tổng kết bảng điểm. Thạch phiên dịch: tám. Chính Doraemon: năm. Áo choàng tàng hình: bốn. Chong chóng tre: ba.

<short pause> Cỗ máy thời gian và khăn trùm thời gian: hai. Cánh cửa thần kỳ, bánh mì trí nhớ, đèn pin thu nhỏ: một. Túi bốn chiều: không, cộng một điểm của Kaku.

<short pause> Hai bảo bối tặng thêm: bút chì tự làm bài bảy điểm, điều khiển thời tiết ba điểm. Nghĩa là bảo bối thật nhất lại là thứ mà Doraemon luôn dặn Nobita đừng lạm dụng.

<short pause> Điều thú vị: bảo bối thật nhất là bảo bối giúp con người hiểu nhau, còn những bảo bối kém thật nhất là những thứ giúp ta đi đường tắt: học không cần học, đi không cần đi.

<short pause> Nhiều tập truyện kết thúc bằng cảnh bảo bối gây họa, và Nobita phải tự sửa sai. Tác giả đã dùng những món đồ tương lai để dạy trẻ em những bài học rất bình thường.

<short pause> Kaku nghĩ đó chính là bài học của Doraemon. Bảo bối nào cũng giúp Nobita thoát khỏi rắc rối, nhưng rồi cũng tạo ra rắc rối mới. Cuối cùng, Nobita vẫn phải tự lớn lên.

<short pause> Và có lẽ vì vậy mà Doraemon vẫn được yêu hơn năm mươi năm. Không phải vì chiếc túi, mà vì người bạn luôn ở bên, kể cả khi bạn thất bại.

<short pause> Nếu được chọn một bảo bối có thật trong tương lai, bạn muốn các nhà khoa học làm ra cái nào trước? Viết vào bình luận nhé.

<short pause> Và nếu bạn là người lớn, hãy thử kể cho một đứa trẻ nghe về Doraemon. Có thể bạn sẽ là người truyền lại chiếc túi thần kỳ cho thế hệ tiếp theo.

<short pause> Video tiếp theo, Kaku vẽ một cây phả hệ đầy ngôi sao: dòng họ Joestar trong JoJo, và vết bớt hình ngôi sao truyền qua nhiều thế hệ.

<short pause> Nếu bạn thích những video khoa học vui như thế này, hãy đăng ký kênh. <laugh> Kaku không có túi thần kỳ, nhưng có một cuốn sổ, và cuốn sổ này còn rất nhiều trang. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tổng kết bảng điểm. Thạch phiên dịch: tám. Chính Doraemon: năm. Áo choàng tàng hình: bốn. Chong chóng tre: ba.

[pause] Cỗ máy thời gian và khăn trùm thời gian: hai. Cánh cửa thần kỳ, bánh mì trí nhớ, đèn pin thu nhỏ: một. Túi bốn chiều: không, cộng một điểm của Kaku.

[pause] Hai bảo bối tặng thêm: bút chì tự làm bài bảy điểm, điều khiển thời tiết ba điểm. Nghĩa là bảo bối thật nhất lại là thứ mà Doraemon luôn dặn Nobita đừng lạm dụng.

[pause] Điều thú vị: bảo bối thật nhất là bảo bối giúp con người hiểu nhau, còn những bảo bối kém thật nhất là những thứ giúp ta đi đường tắt: học không cần học, đi không cần đi.

[pause] Nhiều tập truyện kết thúc bằng cảnh bảo bối gây họa, và Nobita phải tự sửa sai. Tác giả đã dùng những món đồ tương lai để dạy trẻ em những bài học rất bình thường.

[pause] Kaku nghĩ đó chính là bài học của Doraemon. Bảo bối nào cũng giúp Nobita thoát khỏi rắc rối, nhưng rồi cũng tạo ra rắc rối mới. Cuối cùng, Nobita vẫn phải tự lớn lên.

[pause] Và có lẽ vì vậy mà Doraemon vẫn được yêu hơn năm mươi năm. Không phải vì chiếc túi, mà vì người bạn luôn ở bên, kể cả khi bạn thất bại.

[pause] [curious] Nếu được chọn một bảo bối có thật trong tương lai, bạn muốn các nhà khoa học làm ra cái nào trước? Viết vào bình luận nhé.

[pause] Và nếu bạn là người lớn, hãy thử kể cho một đứa trẻ nghe về Doraemon. Có thể bạn sẽ là người truyền lại chiếc túi thần kỳ cho thế hệ tiếp theo.

[pause] Video tiếp theo, Kaku vẽ một cây phả hệ đầy ngôi sao: dòng họ Joestar trong JoJo, và vết bớt hình ngôi sao truyền qua nhiều thế hệ.

[pause] Nếu bạn thích những video khoa học vui như thế này, hãy đăng ký kênh. [chuckles] Kaku không có túi thần kỳ, nhưng có một cuốn sổ, và cuốn sổ này còn rất nhiều trang. Kaku gấp sổ đây, hẹn gặp lại!
```
