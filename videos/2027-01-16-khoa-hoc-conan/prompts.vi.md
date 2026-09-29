# Bộ prompt · Thám tử lừng danh Conan: APTX 4869 và đồ của tiến sĩ Agasa — khoa học thật tới đâu?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 9 đoạn đọc, khoảng 15.6 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (80 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Video này có spoiler nhẹ về bí mật của Conan và Haibara, những điều ai xem vài tập đầu cũng biết. Và một lưu…

```text
Wide 16:9 landscape cinematic frame. a cozy detective's study with a magnifying glass and a closed notebook on a wooden desk, wide establishing shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong đời thật, liệu một viên thuốc có thể làm một chàng trai mười bảy tuổi teo nhỏ thành một cậu bé bảy tuổi…

```text
Wide 16:9 landscape cinematic frame. a small unmarked capsule resting on a velvet cloth under a single spotlight, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Liệu một chiếc nơ có thể giả giọng bất kỳ ai? Một chiếc đồng hồ có thể bắn kim làm người ta ngủ ngay lập tức?…

```text
Wide 16:9 landscape cinematic frame. a tiny collar-mounted voice gadget, a wristwatch and a pair of sneakers displayed on a workbench like museum pieces, still life, warm light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Hơn ba mươi năm qua, Thám tử lừng danh Conan đã là một phần tuổi thơ của rất nhiều người Việt. Và câu hỏi kho…

```text
Wide 16:9 landscape cinematic frame. a stack of well-worn manga volumes on a bedroom shelf beside a childhood photo, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Manga Conan của tác giả Aoyama Gosho bắt đầu từ năm 1994, anime từ năm 1996, và tới nay đã có hơn một nghìn t…

```text
Wide 16:9 landscape cinematic frame. a very long bookshelf filled with numbered manga volumes stretching into the distance, wide shot, warm library light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Ở Việt Nam, truyện được xuất bản từ những năm chín mươi, và nhiều thế hệ đã lớn lên cùng những chuyến đi thuê…

```text
Wide 16:9 landscape cinematic frame. a small neighborhood book rental shop with stacks of comics and a child browsing, medium shot, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở phòng thí nghiệm của Conan: mỗi món đồ, Kaku xem truyện nói gì, k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny safety goggles in a home laboratory, holding a clipboard with a score column. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Bối cảnh trong một phút

Lời: Kudo Shinichi là một thám tử học sinh cấp ba thiên tài. Một buổi tối ở công viên giải trí, anh bí mật theo dõ…

```text
Wide 16:9 landscape cinematic frame. a teenage detective silhouette hiding behind a roller coaster pillar at night, watching two tall figures in dark coats, wide shot, neon amusement park light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Hai gã mặc đồ đen thuộc về một tổ chức tội phạm bí ẩn mà fan gọi là Tổ chức Áo đen. Họ tin Shinichi đã chết,…

```text
Wide 16:9 landscape cinematic frame. two tall silhouettes in long dark coats and hats walking away down a rainy street at night, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Anh bị đánh từ phía sau và bị ép uống một viên thuốc độc thử nghiệm. Nhưng thay vì chết, cơ thể anh teo nhỏ l…

```text
Wide 16:9 landscape cinematic frame. a small child figure waking up inside an oversized school uniform on the ground of an empty park at night, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Tên Edogawa lấy từ nhà văn trinh thám Nhật Edogawa Ranpo, còn Conan lấy từ Arthur Conan Doyle, cha đẻ của She…

```text
Wide 16:9 landscape cinematic frame. two classic detective novels with worn covers placed side by side on a shelf, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Anh lấy tên Edogawa Conan, sống nhờ nhà cô bạn thân Ran, và bí mật phá án bằng những món đồ do nhà phát minh…

```text
Wide 16:9 landscape cinematic frame. a kindly round elderly inventor with a white lab coat handing a small gadget to a young boy in a cluttered garage lab, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Haibara bỏ trốn khỏi tổ chức, và từ đó trở thành người đồng hành của Conan, vừa là nhà khoa học duy nhất có t…

```text
Wide 16:9 landscape cinematic frame. a young girl silhouette running through a rainy alley at night clutching a small case, wide shot, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Về sau, người tạo ra viên thuốc, nhà khoa học Miyano Shiho, cũng uống chính loại thuốc đó, teo nhỏ, và trở th…

```text
Wide 16:9 landscape cinematic frame. a young girl with a cool expression sitting at a laboratory desk with test tubes, looking out a window, medium shot, soft cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Món 1: viên thuốc APTX 4869

Lời: Trong truyện, tên thuốc APTX là viết tắt của Apoptoxin, một chất độc gây ra quá trình tự chết của tế bào, rồi…

```text
Wide 16:9 landscape cinematic frame. a stylized textbook diagram of a cell gently dissolving into small fragments, clean scientific illustration, soft light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Phần này có một nửa là khoa học thật. Apoptosis, hay chết tế bào theo chương trình, là một quá trình có thật…

```text
Wide 16:9 landscape cinematic frame. a microscope on a lab bench beside an open biology textbook, close-up, clean white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Mỗi ngày, cơ thể bạn loại bỏ hàng tỉ tế bào cũ hoặc hỏng theo cách này, như một đội dọn dẹp tự động. Ngón tay…

```text
Wide 16:9 landscape cinematic frame. a gentle diagram of a developing hand shape with the webbing between fingers fading away, scientific illustration style, soft light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Truyện còn nói chất độc không để lại dấu vết. Ngoài đời, khoa học pháp y ngày nay phát hiện được rất nhiều lo…

```text
Wide 16:9 landscape cinematic frame. a forensic laboratory with sample vials and a mass spectrometer machine, a scientist silhouette analyzing results, medium shot, clean white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Truyện còn nói thuốc có thành phần liên quan tới telomerase, một loại enzyme giúp kéo dài phần đầu mút của nh…

```text
Wide 16:9 landscape cinematic frame. a stylized chromosome with glowing caps at its ends, clean scientific illustration, cool blue light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Trong truyện, Haibara từng chế được những viên thuốc giải tạm thời, giúp Conan trở lại dạng Shinichi trong mộ…

```text
Wide 16:9 landscape cinematic frame. a young man gripping his chest in pain on the floor of a dim room as a faint glow fades from his body, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Nhưng tới phần teo nhỏ thì truyện phóng tay rất xa. Cơ thể một người mười bảy tuổi không thể thu lại thành cơ…

```text
Wide 16:9 landscape cinematic frame. a skeleton diagram of a teenager next to a much smaller child skeleton, with a large crossed-out arrow between them, parchment diagram, crimson ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và quan trọng nhất: đây là một chất độc trong truyện. Ngoài đời, không có loại thuốc nào biến người lớn thành…

```text
Wide 16:9 landscape cinematic frame. a suspicious bottle with a flashy miracle label and a big warning stamp across it, close-up, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Manga của Aoyama Gosho từ 1994, anime từ 1996, hơn 1.000 tập, phim điện ảnh hằng năm; tên Edogawa (Ranpo) + C…

```text
Wide 16:9 landscape cinematic frame. cần kiểm lại. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Điểm độ thật của viên thuốc: ba trên mười. Có khái niệm khoa học thật làm nền, nhưng hiệu ứng chính là hư cấu…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 3 out of 10 next to a capsule icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Món 2: nơ đổi giọng

Lời: Nhưng giả giọng chỉ là một nửa. Conan còn phải giả cả cách nói chuyện của ông Mori: từ ngữ, nhịp điệu, cả nhữ…

```text
Wide 16:9 landscape cinematic frame. a young boy hiding behind a sofa whispering into a small device while a sleeping man sits in the armchair in front, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử giả giọng của một giáo sư đọc sách rất chán. Kết quả là Kaku tự ngủ trước.

```text
Wide 16:9 landscape cinematic frame. the owl mascot asleep on top of an open book, a tiny microphone slipping from its wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Chiếc nơ đổi giọng là món đồ nổi tiếng nhất của Conan. Cậu vặn núm, nói vào nơ, và giọng phát ra giống hệt gi…

```text
Wide 16:9 landscape cinematic frame. a tiny collar-mounted voice gadget with small dials on its side resting on a desk beside a microphone, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Khoa học thật: thiết bị đổi giọng đã có từ lâu. Chúng thay đổi cao độ và âm sắc, biến giọng trầm thành bổng h…

```text
Wide 16:9 landscape cinematic frame. a vintage voice-changer device next to a modern audio waveform on a laptop screen, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và ngày nay, trí tuệ nhân tạo đã có thể bắt chước giọng của một người cụ thể chỉ từ vài đoạn ghi âm. Nghĩa là…

```text
Wide 16:9 landscape cinematic frame. a sound waveform on a screen transforming into another person's silhouette icon, clean digital illustration, cyan light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nhưng điều này cũng có mặt tối: kẻ gian dùng giọng giả để lừa đảo qua điện thoại. Kaku nhắc bạn: nếu người th…

```text
Wide 16:9 landscape cinematic frame. a phone showing an incoming call next to a small shield icon and a checklist, close-up, cautionary light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Chỗ truyện phóng tay: một chiếc nơ nhỏ như vậy mà giả được mọi giọng tức thì, không cần mẫu ghi âm, là chưa c…

```text
Wide 16:9 landscape cinematic frame. a tiny collar-mounted voice gadget next to a large computer server rack, humorous size comparison, parchment illustration. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Điểm độ thật của chiếc nơ: bảy trên mười. Món đồ gần hiện thực nhất trong phòng thí nghiệm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 7 out of 10 next to a small microphone icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Món 3: đồng hồ bắn kim gây mê

Lời: Chiếc đồng hồ đeo tay có nắp bật lên, ngắm qua một ô kính nhỏ, và bắn ra một cây kim tẩm thuốc mê. Người trún…

```text
Wide 16:9 landscape cinematic frame. a sleek wristwatch with its cover flipped open revealing a tiny aiming lens, extreme close-up, dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Thời gian thuốc tác dụng phụ thuộc vào vị trí trúng kim, cân nặng, và loại thuốc. Không có công thức nào vừa…

```text
Wide 16:9 landscape cinematic frame. a veterinarian's clipboard with a weight chart and a clock sketched on it, close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Khoa học thật: súng bắn phi tiêu gây mê có thật, dùng để bắt động vật hoang dã. Nhưng thuốc mê không bao giờ…

```text
Wide 16:9 landscape cinematic frame. a wildlife veterinarian silhouette kneeling beside a sleeping large animal in tall grass, wide shot, golden afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Và gây mê là việc cực kỳ nguy hiểm. Sai liều có thể làm người ta ngừng thở. Trong bệnh viện, luôn có bác sĩ g…

```text
Wide 16:9 landscape cinematic frame. a hospital monitor showing heart and breathing lines beside an anesthesia machine, close-up, clean clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Chiếc đồng hồ còn có đèn pin và chỉ mang theo một cây kim mỗi lần. Giới hạn một cây kim là chi tiết khéo của…

```text
Wide 16:9 landscape cinematic frame. a wristwatch with a small beam of flashlight in a dark room, a single tiny needle visible in its chamber, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Chỗ truyện phóng tay: ngủ ngay lập tức, rồi tỉnh dậy khỏe mạnh vài chục phút sau, lần nào cũng như vậy. Nếu n…

```text
Wide 16:9 landscape cinematic frame. a man slumped comically on a chair with a tiny needle in his neck, a question mark above him, humorous illustration, parchment style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc lại: đây không phải hướng dẫn. Đừng bao giờ thử dùng thuốc gây mê với bất kỳ ai.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a large stop sign with a serious expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điểm độ thật của đồng hồ: bốn trên mười. Thiết bị bắn kim có thật, nhưng hiệu ứng tức thì và an toàn là hư cấ…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 4 out of 10 next to a watch icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Món 4: giày tăng lực

Lời: Đôi giày tăng lực có núm vặn bên hông. Khi bật, nó kích thích chân để Conan đá với lực của một vận động viên,…

```text
Wide 16:9 landscape cinematic frame. a pair of children's sneakers with a small dial on the side glowing faintly, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Trong truyện, giày hoạt động bằng cách kích thích huyệt đạo và dùng điện, từ trường. Khoa học thật có một thứ…

```text
Wide 16:9 landscape cinematic frame. a physical therapy session with small electrode pads on a leg connected to a device, medium shot, soft clinic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Nhưng xung điện chỉ làm cơ co lại, không biến cơ của một cậu bé bảy tuổi thành cơ của vận động viên. Và cú đá…

```text
Wide 16:9 landscape cinematic frame. a diagram comparing a small child's leg bone and a strong adult's leg bone with force arrows, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Shinichi vốn là cầu thủ bóng đá giỏi hồi cấp hai, nên đá bóng là kỹ năng sẵn có. Tiến sĩ Agasa chỉ chế thiết…

```text
Wide 16:9 landscape cinematic frame. a teenage boy practicing soccer kicks alone on a school field at sunset, the ball curving into the goal, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Kết hợp với thắt lưng bắn bóng, Conan có cả một hệ thống vũ khí dựa trên bóng đá. Kaku nghĩ tác giả chắc là n…

```text
Wide 16:9 landscape cinematic frame. a soccer ball inflating from a small belt buckle mid-air, a small figure winding up for a kick, dynamic illustration, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Điểm độ thật của đôi giày: hai trên mười. Có khái niệm thật, nhưng hiệu quả là hư cấu hoàn toàn.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 2 out of 10 next to a sneaker icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Món 5: kính truy tìm

Lời: Kính còn có chức năng phóng to như ống nhòm, và về sau được nâng cấp thêm nhiều thứ. Nó giống một chiếc điện…

```text
Wide 16:9 landscape cinematic frame. a small boy peering through glasses with a zoom reticle overlay at a distant building, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Cặp kính của Conan có ăng-ten ẩn, màn hình radar hiện ngay trên mắt kính, và có thể dò tìm một thiết bị định…

```text
Wide 16:9 landscape cinematic frame. a pair of glasses with a faint green radar grid reflected on one lens, extreme close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Khoa học thật: thiết bị định vị nhỏ gọn đã rất phổ biến, từ thẻ định vị chìa khóa tới vòng đeo cổ thú cưng. V…

```text
Wide 16:9 landscape cinematic frame. a small modern tracking tag beside a pair of sleek smart glasses on a table, still life, soft daylight. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Kaku ghi chú: năm 1994, khi truyện ra đời, những thứ này là khoa học viễn tưởng. Ba mươi năm sau, nhiều thứ đ…

```text
Wide 16:9 landscape cinematic frame. a split image of a 1990s bulky mobile phone and a modern slim smartphone, symmetrical composition, soft light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Chỗ truyện phóng tay: kính nhỏ vậy mà có ăng-ten mạnh, pin dùng mãi không hết, và bắt sóng qua cả tòa nhà. Nh…

```text
Wide 16:9 landscape cinematic frame. a tiny battery icon next to a big question mark on a parchment note, humorous close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kaku phải nói thêm: định vị và nghe lén người khác mà không được phép là vi phạm quyền riêng tư. Trong truyện…

```text
Wide 16:9 landscape cinematic frame. a small privacy lock icon glowing over a map with a tracking dot, clean illustration, cool light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Điểm độ thật của cặp kính: tám trên mười. Món đồ gần hiện thực nhất sau chiếc nơ, thậm chí có mặt còn vượt qu…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 out of 10 next to a glasses icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Món 6: ván trượt năng lượng mặt trời

Lời: Ván trượt thường xuất hiện ở những cảnh rượt đuổi hay nhất, khi Conan phải đuổi theo xe hơi của hung thủ. Đó…

```text
Wide 16:9 landscape cinematic frame. a small boy crouching low on a speeding skateboard chasing a car through city traffic, dynamic wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Chiếc ván trượt của Conan chạy bằng năng lượng mặt trời, tăng tốc đuổi kịp cả ô tô trên đường cao tốc.

```text
Wide 16:9 landscape cinematic frame. a sleek skateboard with small solar panels on its deck speeding along a highway at sunset, dynamic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Kaku làm một phép tính nhanh: tấm pin mặt trời bằng cỡ mặt ván chỉ cho công suất nhỏ, đủ sạc chậm cho một chi…

```text
Wide 16:9 landscape cinematic frame. a small solar panel connected to a phone charging slowly, a racing car drawn beside it with a crossed-out arrow, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Khoa học thật: ván trượt điện đã có thật và khá phổ biến. Tấm pin mặt trời cũng có thật. Nhưng tấm pin nhỏ tr…

```text
Wide 16:9 landscape cinematic frame. a modern electric skateboard parked beside a small solar panel, still life, bright daylight. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Chạy nhanh như vậy mà không có mũ bảo hiểm thì cực kỳ nguy hiểm. Kaku nhắc: đi ván điện ngoài đời phải có đồ…

```text
Wide 16:9 landscape cinematic frame. a helmet, knee pads and elbow pads neatly arranged next to a skateboard, close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Điểm độ thật của ván trượt: năm trên mười.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 5 out of 10 next to a skateboard icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Món 7: huy hiệu thám tử

Lời: Đội thám tử nhí, những người bạn cùng lớp của Conan, mỗi người có một chiếc huy hiệu. Nó vừa là bộ đàm để nói…

```text
Wide 16:9 landscape cinematic frame. three small children proudly showing their shiny detective badges in a schoolyard, medium shot, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Khoa học thật: bộ đàm và thiết bị định vị cho trẻ em đã có thật, như đồng hồ định vị mà nhiều phụ huynh mua c…

```text
Wide 16:9 landscape cinematic frame. a child's smartwatch with a small map on its screen beside a pair of walkie-talkies on a table, still life, soft daylight. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Chỗ truyện phóng tay rất ít: chủ yếu là kích thước nhỏ gọn và pin lâu. Nhiều vụ án được cứu chỉ nhờ một đứa t…

```text
Wide 16:9 landscape cinematic frame. a small hand pressing a badge button in a dark storage room, a faint signal wave emanating from it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Điểm độ thật của huy hiệu: chín trên mười. Món đồ thật nhất trong cả video.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 9 out of 10 next to a badge icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Bảng điểm độ thật

Lời: Nhưng đừng quên còn một món nữa, không nằm trong phòng thí nghiệm: những chiếc huy hiệu của Đội thám tử nhí.

```text
Wide 16:9 landscape cinematic frame. a small shiny detective badge resting on a child's palm, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Kaku gom lại bảng điểm. Cao nhất là huy hiệu thám tử, chín điểm, rồi cặp kính truy tìm, tám điểm, và chiếc nơ…

```text
Wide 16:9 landscape cinematic frame. a ranked chart on parchment with glasses and microphone icons at the top, amber ink, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Ở giữa là ván trượt, năm điểm, và đồng hồ gây mê, bốn điểm. Cuối bảng là viên thuốc, ba điểm, và đôi giày tăn…

```text
Wide 16:9 landscape cinematic frame. the lower part of the ranked chart with skateboard, watch, capsule and sneaker icons, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku để ý thêm: những món đồ gần hiện thực nhất đều là thứ giúp giao tiếp và tìm kiếm. Conan thật ra là một b…

```text
Wide 16:9 landscape cinematic frame. a web of communication lines connecting small icons of people, a magnifying glass at the center, parchment illustration, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Có một quy luật thú vị: những món đồ về thông tin, như giọng nói và định vị, thì gần hiện thực nhất. Những mó…

```text
Wide 16:9 landscape cinematic frame. a two-column diagram: information gadgets on a bright side, body-changing gadgets on a dim side, parchment illustration. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ điều này phản ánh đúng khoa học ngoài đời: máy móc và điện tử tiến rất nhanh, còn cơ thể người thì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny circuit board in one wing and a biology textbook in the other, weighing them thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Góc nhìn của Kaku: khoa học phục vụ suy luận

Lời: Nhưng Kaku muốn nói thêm một điều. Trong Conan, tất cả những món đồ này không bao giờ là thứ giải quyết vụ án…

```text
Wide 16:9 landscape cinematic frame. a boy detective pointing confidently at a pinned evidence board full of clues and red strings, medium shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Rất nhiều vụ án trong Conan xoay quanh những kiến thức có thật: tính chất hóa học, thời gian đông cứng của vậ…

```text
Wide 16:9 landscape cinematic frame. a notebook page with small sketches of a chemistry flask, an ice cube melting, a beam of light and a thinking face, parchment style, amber ink. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Kaku có một bài tập nhỏ: hôm nay, hãy thử quan sát một người quen thật kỹ, rồi đoán xem họ vừa làm gì trước k…

```text
Wide 16:9 landscape cinematic frame. a person at a café table observing a friend's muddy shoes and a train ticket sticking out of a pocket, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Thứ phá án luôn là quan sát, logic, và kiến thức. Và kiến thức trong Conan, từ hóa học, vật lý tới tâm lý, ph…

```text
Wide 16:9 landscape cinematic frame. a desk covered with a chemistry book, a physics diagram and a psychology notebook, a magnifying glass on top, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất muốn biết: vụ án nào trong Conan khiến bạn nhớ nhất vì một chi tiết khoa học bất ngờ? Kể cho Kaku ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny magnifying glass over a comment box drawn on parchment. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Kaku nghĩ đó là lý do Conan sống được hơn ba mươi năm và vẫn được yêu thích: truyện dạy người xem cách quan s…

```text
Wide 16:9 landscape cinematic frame. a child looking carefully through a magnifying glass at a small leaf in a garden, close-up, bright natural light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu được chọn một món đồ của tiến sĩ Agasa để mang về nhà, bạn chọn món nào, và để làm gì? Kaku đoán nhiều bạ…

```text
Wide 16:9 landscape cinematic frame. a small wish list on a notepad with gadget icons and checkboxes, a pencil beside it, top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Kết

Lời: Và nếu một ngày ai đó nói với bạn họ đã chế ra thuốc trẻ hóa, hãy nhớ bảng điểm của Kaku: những gì thay đổi c…

```text
Wide 16:9 landscape cinematic frame. a skeptical eyebrow raised in front of a flashy advertisement for a miracle youth pill, close-up, humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Thuốc teo nhỏ thì còn là giấc mơ của tiểu thuyết. Nhưng nơ đổi giọng và kính định vị thì đã ở trong túi chúng…

```text
Wide 16:9 landscape cinematic frame. a kindly elderly inventor silhouette looking at a modern smartphone with delighted surprise, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku quay lại Jujutsu Kaisen với một trò chơi sinh tử: Tử Diệt Hồi Du. Luật chơi là gì, và l…

```text
Wide 16:9 landscape cinematic frame. a game board drawn over a city map with glowing point markers and barrier lines, top-down shot, eerie violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích kiểu video tách bạch thật và hư cấu, hãy đăng ký kênh để Kaku mở thêm nhiều phòng thí nghiệm nữ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off its safety goggles and waving goodbye from the laboratory doorway. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 85 giây · cảnh s01–s07 · 1104 ký tự

**Gemini**

```text
Video này có spoiler nhẹ về bí mật của Conan và Haibara, những điều ai xem vài tập đầu cũng biết. Và một lưu ý quan trọng: đây là nội dung giải trí, không phải hướng dẫn hay lời khuyên y tế.

<short pause> Trong đời thật, liệu một viên thuốc có thể làm một chàng trai mười bảy tuổi teo nhỏ thành một cậu bé bảy tuổi không?

<short pause> Liệu một chiếc nơ có thể giả giọng bất kỳ ai? Một chiếc đồng hồ có thể bắn kim làm người ta ngủ ngay lập tức? Một đôi giày có thể giúp trẻ con đá bay cả xe máy?

<short pause> Hơn ba mươi năm qua, Thám tử lừng danh Conan đã là một phần tuổi thơ của rất nhiều người Việt. Và câu hỏi khoa học thật tới đâu thì ai cũng từng tự hỏi.

<short pause> Manga Conan của tác giả Aoyama Gosho bắt đầu từ năm 1994, anime từ năm 1996, và tới nay đã có hơn một nghìn tập phim cùng một bộ phim điện ảnh mỗi năm.

<short pause> Ở Việt Nam, truyện được xuất bản từ những năm chín mươi, và nhiều thế hệ đã lớn lên cùng những chuyến đi thuê truyện, đợi tập mới ra.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở phòng thí nghiệm của Conan: mỗi món đồ, Kaku xem truyện nói gì, khoa học thật nói gì, và truyện phóng tay ở đâu. Cuối mỗi món là điểm độ thật từ một tới mười.
```

**ElevenLabs**

```text
Video này có spoiler nhẹ về bí mật của Conan và Haibara, những điều ai xem vài tập đầu cũng biết. Và một lưu ý quan trọng: đây là nội dung giải trí, không phải hướng dẫn hay lời khuyên y tế.

[pause] [curious] Trong đời thật, liệu một viên thuốc có thể làm một chàng trai mười bảy tuổi teo nhỏ thành một cậu bé bảy tuổi không?

[pause] Liệu một chiếc nơ có thể giả giọng bất kỳ ai? Một chiếc đồng hồ có thể bắn kim làm người ta ngủ ngay lập tức? Một đôi giày có thể giúp trẻ con đá bay cả xe máy?

[pause] Hơn ba mươi năm qua, Thám tử lừng danh Conan đã là một phần tuổi thơ của rất nhiều người Việt. Và câu hỏi khoa học thật tới đâu thì ai cũng từng tự hỏi.

[pause] Manga Conan của tác giả Aoyama Gosho bắt đầu từ năm 1994, anime từ năm 1996, và tới nay đã có hơn một nghìn tập phim cùng một bộ phim điện ảnh mỗi năm.

[pause] Ở Việt Nam, truyện được xuất bản từ những năm chín mươi, và nhiều thế hệ đã lớn lên cùng những chuyến đi thuê truyện, đợi tập mới ra.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở phòng thí nghiệm của Conan: mỗi món đồ, Kaku xem truyện nói gì, khoa học thật nói gì, và truyện phóng tay ở đâu. Cuối mỗi món là điểm độ thật từ một tới mười.
```

### c02 · Bối cảnh trong một phút

Khoảng 84 giây · cảnh s08–s14 · 1089 ký tự

**Gemini**

```text
Kudo Shinichi là một thám tử học sinh cấp ba thiên tài. Một buổi tối ở công viên giải trí, anh bí mật theo dõi hai gã đàn ông mặc đồ đen.

<short pause> Hai gã mặc đồ đen thuộc về một tổ chức tội phạm bí ẩn mà fan gọi là Tổ chức Áo đen. Họ tin Shinichi đã chết, và Conan phải giấu thân phận để không ai quanh mình gặp nguy hiểm.

<short pause> Anh bị đánh từ phía sau và bị ép uống một viên thuốc độc thử nghiệm. <short pause> Nhưng thay vì chết, cơ thể anh teo nhỏ lại thành một cậu bé.

<short pause> Tên Edogawa lấy từ nhà văn trinh thám Nhật Edogawa Ranpo, còn Conan lấy từ Arthur Conan Doyle, cha đẻ của Sherlock Holmes. Chỉ một cái tên đã là một lời tri ân dòng truyện trinh thám.

<short pause> Anh lấy tên Edogawa Conan, sống nhờ nhà cô bạn thân Ran, và bí mật phá án bằng những món đồ do nhà phát minh hàng xóm, tiến sĩ Agasa, chế tạo.

<short pause> Haibara bỏ trốn khỏi tổ chức, và từ đó trở thành người đồng hành của Conan, vừa là nhà khoa học duy nhất có thể chế ra thuốc giải, vừa là người hiểu rõ nhất sự nguy hiểm của chính phát minh ấy.

<short pause> Về sau, người tạo ra viên thuốc, nhà khoa học Miyano Shiho, cũng uống chính loại thuốc đó, teo nhỏ, và trở thành cô bé Haibara Ai.
```

**ElevenLabs**

```text
Kudo Shinichi là một thám tử học sinh cấp ba thiên tài. Một buổi tối ở công viên giải trí, anh bí mật theo dõi hai gã đàn ông mặc đồ đen.

[pause] Hai gã mặc đồ đen thuộc về một tổ chức tội phạm bí ẩn mà fan gọi là Tổ chức Áo đen. Họ tin Shinichi đã chết, và Conan phải giấu thân phận để không ai quanh mình gặp nguy hiểm.

[pause] Anh bị đánh từ phía sau và bị ép uống một viên thuốc độc thử nghiệm. [pause] Nhưng thay vì chết, cơ thể anh teo nhỏ lại thành một cậu bé.

[pause] Tên Edogawa lấy từ nhà văn trinh thám Nhật Edogawa Ranpo, còn Conan lấy từ Arthur Conan Doyle, cha đẻ của Sherlock Holmes. Chỉ một cái tên đã là một lời tri ân dòng truyện trinh thám.

[pause] Anh lấy tên Edogawa Conan, sống nhờ nhà cô bạn thân Ran, và bí mật phá án bằng những món đồ do nhà phát minh hàng xóm, tiến sĩ Agasa, chế tạo.

[pause] Haibara bỏ trốn khỏi tổ chức, và từ đó trở thành người đồng hành của Conan, vừa là nhà khoa học duy nhất có thể chế ra thuốc giải, vừa là người hiểu rõ nhất sự nguy hiểm của chính phát minh ấy.

[pause] Về sau, người tạo ra viên thuốc, nhà khoa học Miyano Shiho, cũng uống chính loại thuốc đó, teo nhỏ, và trở thành cô bé Haibara Ai.
```

### c03 · Món 1: viên thuốc APTX 4869

Khoảng 139 giây · cảnh s15–s24 · 1801 ký tự

**Gemini**

```text
Trong truyện, tên thuốc APTX là viết tắt của Apoptoxin, một chất độc gây ra quá trình tự chết của tế bào, rồi không để lại dấu vết.

<short pause> Phần này có một nửa là khoa học thật. Apoptosis, hay chết tế bào theo chương trình, là một quá trình có thật và rất bình thường trong cơ thể người.

<short pause> Mỗi ngày, cơ thể bạn loại bỏ hàng tỉ tế bào cũ hoặc hỏng theo cách này, như một đội dọn dẹp tự động. Ngón tay của thai nhi tách ra được cũng là nhờ các tế bào giữa các ngón tự chết đi.

<short pause> Truyện còn nói chất độc không để lại dấu vết. Ngoài đời, khoa học pháp y ngày nay phát hiện được rất nhiều loại chất lạ trong cơ thể. Chất độc hoàn hảo không dấu vết gần như chỉ có trong tiểu thuyết.

<short pause> Truyện còn nói thuốc có thành phần liên quan tới telomerase, một loại enzyme giúp kéo dài phần đầu mút của nhiễm sắc thể. Telomerase cũng là thứ có thật, và các nhà khoa học vẫn nghiên cứu nó trong chuyện lão hóa.

<short pause> Trong truyện, Haibara từng chế được những viên thuốc giải tạm thời, giúp Conan trở lại dạng Shinichi trong một thời gian ngắn. <short pause> Nhưng mỗi lần như vậy đều kèm những cơn đau dữ dội.

<short pause> Nhưng tới phần teo nhỏ thì truyện phóng tay rất xa. Cơ thể một người mười bảy tuổi không thể thu lại thành cơ thể bảy tuổi. Xương đã dài ra thì không co lại, và khối lượng cơ thể không thể tự nhiên biến mất.

<short pause> Và quan trọng nhất: đây là một chất độc trong truyện. Ngoài đời, không có loại thuốc nào biến người lớn thành trẻ con, và mọi thứ gọi là thuốc trẻ hóa thần kỳ đều đáng nghi ngờ.

<short pause> Manga của Aoyama Gosho từ 1994, anime từ 1996, hơn 1.000 tập, phim điện ảnh hằng năm; tên Edogawa (Ranpo) + Conan (Doyle); Tổ chức Áo đen; Haibara chế thuốc giải tạm thời; Shinichi từng chơi bóng đá; huy hiệu Đội thám tử nhí có bộ đàm và định vị

<short pause> Điểm độ thật của viên thuốc: ba trên mười. Có khái niệm khoa học thật làm nền, nhưng hiệu ứng chính là hư cấu hoàn toàn.
```

**ElevenLabs**

```text
Trong truyện, tên thuốc APTX là viết tắt của Apoptoxin, một chất độc gây ra quá trình tự chết của tế bào, rồi không để lại dấu vết.

[pause] Phần này có một nửa là khoa học thật. Apoptosis, hay chết tế bào theo chương trình, là một quá trình có thật và rất bình thường trong cơ thể người.

[pause] Mỗi ngày, cơ thể bạn loại bỏ hàng tỉ tế bào cũ hoặc hỏng theo cách này, như một đội dọn dẹp tự động. Ngón tay của thai nhi tách ra được cũng là nhờ các tế bào giữa các ngón tự chết đi.

[pause] Truyện còn nói chất độc không để lại dấu vết. Ngoài đời, khoa học pháp y ngày nay phát hiện được rất nhiều loại chất lạ trong cơ thể. Chất độc hoàn hảo không dấu vết gần như chỉ có trong tiểu thuyết.

[pause] Truyện còn nói thuốc có thành phần liên quan tới telomerase, một loại enzyme giúp kéo dài phần đầu mút của nhiễm sắc thể. Telomerase cũng là thứ có thật, và các nhà khoa học vẫn nghiên cứu nó trong chuyện lão hóa.

[pause] Trong truyện, Haibara từng chế được những viên thuốc giải tạm thời, giúp Conan trở lại dạng Shinichi trong một thời gian ngắn. [pause] Nhưng mỗi lần như vậy đều kèm những cơn đau dữ dội.

[pause] Nhưng tới phần teo nhỏ thì truyện phóng tay rất xa. Cơ thể một người mười bảy tuổi không thể thu lại thành cơ thể bảy tuổi. Xương đã dài ra thì không co lại, và khối lượng cơ thể không thể tự nhiên biến mất.

[pause] Và quan trọng nhất: đây là một chất độc trong truyện. Ngoài đời, không có loại thuốc nào biến người lớn thành trẻ con, và mọi thứ gọi là thuốc trẻ hóa thần kỳ đều đáng nghi ngờ.

[pause] Manga của Aoyama Gosho từ 1994, anime từ 1996, hơn 1.000 tập, phim điện ảnh hằng năm; tên Edogawa (Ranpo) + Conan (Doyle); Tổ chức Áo đen; Haibara chế thuốc giải tạm thời; Shinichi từng chơi bóng đá; huy hiệu Đội thám tử nhí có bộ đàm và định vị

[pause] Điểm độ thật của viên thuốc: ba trên mười. Có khái niệm khoa học thật làm nền, nhưng hiệu ứng chính là hư cấu hoàn toàn.
```

### c04 · Món 2: nơ đổi giọng

Khoảng 87 giây · cảnh s25–s32 · 1133 ký tự

**Gemini**

```text
Nhưng giả giọng chỉ là một nửa. Conan còn phải giả cả cách nói chuyện của ông Mori: từ ngữ, nhịp điệu, cả những câu cửa miệng. Đó là kỹ năng diễn xuất, không phải của máy.

<short pause> <laugh> Kaku thử giả giọng của một giáo sư đọc sách rất chán. Kết quả là Kaku tự ngủ trước.

<short pause> Chiếc nơ đổi giọng là món đồ nổi tiếng nhất của Conan. Cậu vặn núm, nói vào nơ, và giọng phát ra giống hệt giọng người khác, thường là ông Mori, để suy luận thay ông.

<short pause> Khoa học thật: thiết bị đổi giọng đã có từ lâu. Chúng thay đổi cao độ và âm sắc, biến giọng trầm thành bổng hoặc ngược lại.

<short pause> Và ngày nay, trí tuệ nhân tạo đã có thể bắt chước giọng của một người cụ thể chỉ từ vài đoạn ghi âm. Nghĩa là về mặt kỹ thuật, chiếc nơ của Conan gần với hiện thực hơn bao giờ hết.

<short pause> Nhưng điều này cũng có mặt tối: kẻ gian dùng giọng giả để lừa đảo qua điện thoại. Kaku nhắc bạn: nếu người thân gọi tới xin tiền gấp, hãy gọi lại bằng số quen để kiểm tra.

<short pause> Chỗ truyện phóng tay: một chiếc nơ nhỏ như vậy mà giả được mọi giọng tức thì, không cần mẫu ghi âm, là chưa có thật. <short pause> Nhưng khoảng cách đang hẹp dần.

<short pause> Điểm độ thật của chiếc nơ: bảy trên mười. Món đồ gần hiện thực nhất trong phòng thí nghiệm.
```

**ElevenLabs**

```text
Nhưng giả giọng chỉ là một nửa. Conan còn phải giả cả cách nói chuyện của ông Mori: từ ngữ, nhịp điệu, cả những câu cửa miệng. Đó là kỹ năng diễn xuất, không phải của máy.

[pause] [chuckles] Kaku thử giả giọng của một giáo sư đọc sách rất chán. Kết quả là Kaku tự ngủ trước.

[pause] Chiếc nơ đổi giọng là món đồ nổi tiếng nhất của Conan. Cậu vặn núm, nói vào nơ, và giọng phát ra giống hệt giọng người khác, thường là ông Mori, để suy luận thay ông.

[pause] Khoa học thật: thiết bị đổi giọng đã có từ lâu. Chúng thay đổi cao độ và âm sắc, biến giọng trầm thành bổng hoặc ngược lại.

[pause] Và ngày nay, trí tuệ nhân tạo đã có thể bắt chước giọng của một người cụ thể chỉ từ vài đoạn ghi âm. Nghĩa là về mặt kỹ thuật, chiếc nơ của Conan gần với hiện thực hơn bao giờ hết.

[pause] Nhưng điều này cũng có mặt tối: kẻ gian dùng giọng giả để lừa đảo qua điện thoại. Kaku nhắc bạn: nếu người thân gọi tới xin tiền gấp, hãy gọi lại bằng số quen để kiểm tra.

[pause] Chỗ truyện phóng tay: một chiếc nơ nhỏ như vậy mà giả được mọi giọng tức thì, không cần mẫu ghi âm, là chưa có thật. [pause] Nhưng khoảng cách đang hẹp dần.

[pause] Điểm độ thật của chiếc nơ: bảy trên mười. Món đồ gần hiện thực nhất trong phòng thí nghiệm.
```

### c05 · Món 3: đồng hồ bắn kim gây mê

Khoảng 90 giây · cảnh s33–s40 · 1174 ký tự

**Gemini**

```text
Chiếc đồng hồ đeo tay có nắp bật lên, ngắm qua một ô kính nhỏ, và bắn ra một cây kim tẩm thuốc mê. Người trúng kim ngủ ngay lập tức, thường là ông Mori tội nghiệp.

<short pause> Thời gian thuốc tác dụng phụ thuộc vào vị trí trúng kim, cân nặng, và loại thuốc. Không có công thức nào vừa nhanh tức thì vừa an toàn cho mọi người.

<short pause> Khoa học thật: súng bắn phi tiêu gây mê có thật, dùng để bắt động vật hoang dã. <short pause> Nhưng thuốc mê không bao giờ tác dụng ngay. Con vật thường mất vài phút mới ngủ, và liều phải tính theo cân nặng.

<short pause> Và gây mê là việc cực kỳ nguy hiểm. Sai liều có thể làm người ta ngừng thở. Trong bệnh viện, luôn có bác sĩ gây mê theo dõi từng chỉ số.

<short pause> Chiếc đồng hồ còn có đèn pin và chỉ mang theo một cây kim mỗi lần. Giới hạn một cây kim là chi tiết khéo của tác giả: Conan phải chọn đúng thời điểm, không thể bắn bừa.

<short pause> Chỗ truyện phóng tay: ngủ ngay lập tức, rồi tỉnh dậy khỏe mạnh vài chục phút sau, lần nào cũng như vậy. Nếu ngoài đời, ông Mori chắc đã phải vào viện rất nhiều lần.

<short pause> <laugh> Kaku nhắc lại: đây không phải hướng dẫn. Đừng bao giờ thử dùng thuốc gây mê với bất kỳ ai.

<short pause> Điểm độ thật của đồng hồ: bốn trên mười. Thiết bị bắn kim có thật, nhưng hiệu ứng tức thì và an toàn là hư cấu.
```

**ElevenLabs**

```text
Chiếc đồng hồ đeo tay có nắp bật lên, ngắm qua một ô kính nhỏ, và bắn ra một cây kim tẩm thuốc mê. Người trúng kim ngủ ngay lập tức, thường là ông Mori tội nghiệp.

[pause] Thời gian thuốc tác dụng phụ thuộc vào vị trí trúng kim, cân nặng, và loại thuốc. Không có công thức nào vừa nhanh tức thì vừa an toàn cho mọi người.

[pause] Khoa học thật: súng bắn phi tiêu gây mê có thật, dùng để bắt động vật hoang dã. [pause] Nhưng thuốc mê không bao giờ tác dụng ngay. Con vật thường mất vài phút mới ngủ, và liều phải tính theo cân nặng.

[pause] Và gây mê là việc cực kỳ nguy hiểm. Sai liều có thể làm người ta ngừng thở. Trong bệnh viện, luôn có bác sĩ gây mê theo dõi từng chỉ số.

[pause] Chiếc đồng hồ còn có đèn pin và chỉ mang theo một cây kim mỗi lần. Giới hạn một cây kim là chi tiết khéo của tác giả: Conan phải chọn đúng thời điểm, không thể bắn bừa.

[pause] Chỗ truyện phóng tay: ngủ ngay lập tức, rồi tỉnh dậy khỏe mạnh vài chục phút sau, lần nào cũng như vậy. Nếu ngoài đời, ông Mori chắc đã phải vào viện rất nhiều lần.

[pause] [chuckles] Kaku nhắc lại: đây không phải hướng dẫn. Đừng bao giờ thử dùng thuốc gây mê với bất kỳ ai.

[pause] Điểm độ thật của đồng hồ: bốn trên mười. Thiết bị bắn kim có thật, nhưng hiệu ứng tức thì và an toàn là hư cấu.
```

### c06 · Món 4: giày tăng lực / Món 5: kính truy tìm

Khoảng 153 giây · cảnh s41–s53 · 1984 ký tự

**Gemini**

```text
Đôi giày tăng lực có núm vặn bên hông. Khi bật, nó kích thích chân để Conan đá với lực của một vận động viên, thậm chí làm vỡ kính, hạ gục kẻ xấu từ xa.

<short pause> Trong truyện, giày hoạt động bằng cách kích thích huyệt đạo và dùng điện, từ trường. Khoa học thật có một thứ gần giống: kích thích cơ bằng xung điện, dùng trong vật lý trị liệu và tập luyện.

<short pause> Nhưng xung điện chỉ làm cơ co lại, không biến cơ của một cậu bé bảy tuổi thành cơ của vận động viên. Và cú đá quá mạnh sẽ làm chính chân người đá bị thương trước.

<short pause> Shinichi vốn là cầu thủ bóng đá giỏi hồi cấp hai, nên đá bóng là kỹ năng sẵn có. Tiến sĩ Agasa chỉ chế thiết bị để phóng đại kỹ năng ấy.

<short pause> Kết hợp với thắt lưng bắn bóng, Conan có cả một hệ thống vũ khí dựa trên bóng đá. Kaku nghĩ tác giả chắc là người rất mê bóng đá.

<short pause> Điểm độ thật của đôi giày: hai trên mười. Có khái niệm thật, nhưng hiệu quả là hư cấu hoàn toàn.

<short pause> Kính còn có chức năng phóng to như ống nhòm, và về sau được nâng cấp thêm nhiều thứ. Nó giống một chiếc điện thoại thông minh đeo trên mặt, từ trước khi điện thoại thông minh ra đời.

<short pause> Cặp kính của Conan có ăng-ten ẩn, màn hình radar hiện ngay trên mắt kính, và có thể dò tìm một thiết bị định vị cách xa hàng chục cây số, kèm chức năng nghe lén.

<short pause> Khoa học thật: thiết bị định vị nhỏ gọn đã rất phổ biến, từ thẻ định vị chìa khóa tới vòng đeo cổ thú cưng. Và kính thông minh có màn hình hiển thị cũng đã được bán ngoài thị trường.

<short pause> Kaku ghi chú: năm 1994, khi truyện ra đời, những thứ này là khoa học viễn tưởng. Ba mươi năm sau, nhiều thứ đã thành đồ dùng hằng ngày. Truyện trinh thám đôi khi đoán trước tương lai.

<short pause> Chỗ truyện phóng tay: kính nhỏ vậy mà có ăng-ten mạnh, pin dùng mãi không hết, và bắt sóng qua cả tòa nhà. <short pause> Nhưng ý tưởng thì rất gần hiện thực.

<short pause> Kaku phải nói thêm: định vị và nghe lén người khác mà không được phép là vi phạm quyền riêng tư. Trong truyện Conan dùng để phá án, ngoài đời thì không nên.

<short pause> Điểm độ thật của cặp kính: tám trên mười. Món đồ gần hiện thực nhất sau chiếc nơ, thậm chí có mặt còn vượt qua.
```

**ElevenLabs**

```text
Đôi giày tăng lực có núm vặn bên hông. Khi bật, nó kích thích chân để Conan đá với lực của một vận động viên, thậm chí làm vỡ kính, hạ gục kẻ xấu từ xa.

[pause] Trong truyện, giày hoạt động bằng cách kích thích huyệt đạo và dùng điện, từ trường. Khoa học thật có một thứ gần giống: kích thích cơ bằng xung điện, dùng trong vật lý trị liệu và tập luyện.

[pause] Nhưng xung điện chỉ làm cơ co lại, không biến cơ của một cậu bé bảy tuổi thành cơ của vận động viên. Và cú đá quá mạnh sẽ làm chính chân người đá bị thương trước.

[pause] Shinichi vốn là cầu thủ bóng đá giỏi hồi cấp hai, nên đá bóng là kỹ năng sẵn có. Tiến sĩ Agasa chỉ chế thiết bị để phóng đại kỹ năng ấy.

[pause] Kết hợp với thắt lưng bắn bóng, Conan có cả một hệ thống vũ khí dựa trên bóng đá. Kaku nghĩ tác giả chắc là người rất mê bóng đá.

[pause] Điểm độ thật của đôi giày: hai trên mười. Có khái niệm thật, nhưng hiệu quả là hư cấu hoàn toàn.

[pause] Kính còn có chức năng phóng to như ống nhòm, và về sau được nâng cấp thêm nhiều thứ. Nó giống một chiếc điện thoại thông minh đeo trên mặt, từ trước khi điện thoại thông minh ra đời.

[pause] Cặp kính của Conan có ăng-ten ẩn, màn hình radar hiện ngay trên mắt kính, và có thể dò tìm một thiết bị định vị cách xa hàng chục cây số, kèm chức năng nghe lén.

[pause] Khoa học thật: thiết bị định vị nhỏ gọn đã rất phổ biến, từ thẻ định vị chìa khóa tới vòng đeo cổ thú cưng. Và kính thông minh có màn hình hiển thị cũng đã được bán ngoài thị trường.

[pause] Kaku ghi chú: năm 1994, khi truyện ra đời, những thứ này là khoa học viễn tưởng. Ba mươi năm sau, nhiều thứ đã thành đồ dùng hằng ngày. Truyện trinh thám đôi khi đoán trước tương lai.

[pause] Chỗ truyện phóng tay: kính nhỏ vậy mà có ăng-ten mạnh, pin dùng mãi không hết, và bắt sóng qua cả tòa nhà. [pause] Nhưng ý tưởng thì rất gần hiện thực.

[pause] Kaku phải nói thêm: định vị và nghe lén người khác mà không được phép là vi phạm quyền riêng tư. Trong truyện Conan dùng để phá án, ngoài đời thì không nên.

[pause] Điểm độ thật của cặp kính: tám trên mười. Món đồ gần hiện thực nhất sau chiếc nơ, thậm chí có mặt còn vượt qua.
```

### c07 · Món 6: ván trượt năng lượng mặt trời / Món 7: huy hiệu thám tử

Khoảng 99 giây · cảnh s54–s63 · 1287 ký tự

**Gemini**

```text
Ván trượt thường xuất hiện ở những cảnh rượt đuổi hay nhất, khi Conan phải đuổi theo xe hơi của hung thủ. Đó là món đồ cho những pha hành động của một thám tử không biết lái xe.

<short pause> Chiếc ván trượt của Conan chạy bằng năng lượng mặt trời, tăng tốc đuổi kịp cả ô tô trên đường cao tốc.

<short pause> Kaku làm một phép tính nhanh: tấm pin mặt trời bằng cỡ mặt ván chỉ cho công suất nhỏ, đủ sạc chậm cho một chiếc điện thoại, chứ không đủ đẩy một người đi với tốc độ ô tô.

<short pause> Khoa học thật: ván trượt điện đã có thật và khá phổ biến. Tấm pin mặt trời cũng có thật. <short pause> Nhưng tấm pin nhỏ trên mặt ván không thể cung cấp đủ năng lượng để chạy nhanh như ô tô.

<short pause> Chạy nhanh như vậy mà không có mũ bảo hiểm thì cực kỳ nguy hiểm. Kaku nhắc: đi ván điện ngoài đời phải có đồ bảo hộ và đúng nơi cho phép.

<short pause> Điểm độ thật của ván trượt: năm trên mười.

<short pause> Đội thám tử nhí, những người bạn cùng lớp của Conan, mỗi người có một chiếc huy hiệu. Nó vừa là bộ đàm để nói chuyện, vừa có thiết bị định vị để tìm nhau.

<short pause> Khoa học thật: bộ đàm và thiết bị định vị cho trẻ em đã có thật, như đồng hồ định vị mà nhiều phụ huynh mua cho con.

<short pause> Chỗ truyện phóng tay rất ít: chủ yếu là kích thước nhỏ gọn và pin lâu. Nhiều vụ án được cứu chỉ nhờ một đứa trẻ bấm nút huy hiệu đúng lúc.

<short pause> Điểm độ thật của huy hiệu: chín trên mười. Món đồ thật nhất trong cả video.
```

**ElevenLabs**

```text
Ván trượt thường xuất hiện ở những cảnh rượt đuổi hay nhất, khi Conan phải đuổi theo xe hơi của hung thủ. Đó là món đồ cho những pha hành động của một thám tử không biết lái xe.

[pause] Chiếc ván trượt của Conan chạy bằng năng lượng mặt trời, tăng tốc đuổi kịp cả ô tô trên đường cao tốc.

[pause] Kaku làm một phép tính nhanh: tấm pin mặt trời bằng cỡ mặt ván chỉ cho công suất nhỏ, đủ sạc chậm cho một chiếc điện thoại, chứ không đủ đẩy một người đi với tốc độ ô tô.

[pause] Khoa học thật: ván trượt điện đã có thật và khá phổ biến. Tấm pin mặt trời cũng có thật. [pause] Nhưng tấm pin nhỏ trên mặt ván không thể cung cấp đủ năng lượng để chạy nhanh như ô tô.

[pause] Chạy nhanh như vậy mà không có mũ bảo hiểm thì cực kỳ nguy hiểm. Kaku nhắc: đi ván điện ngoài đời phải có đồ bảo hộ và đúng nơi cho phép.

[pause] Điểm độ thật của ván trượt: năm trên mười.

[pause] Đội thám tử nhí, những người bạn cùng lớp của Conan, mỗi người có một chiếc huy hiệu. Nó vừa là bộ đàm để nói chuyện, vừa có thiết bị định vị để tìm nhau.

[pause] Khoa học thật: bộ đàm và thiết bị định vị cho trẻ em đã có thật, như đồng hồ định vị mà nhiều phụ huynh mua cho con.

[pause] Chỗ truyện phóng tay rất ít: chủ yếu là kích thước nhỏ gọn và pin lâu. Nhiều vụ án được cứu chỉ nhờ một đứa trẻ bấm nút huy hiệu đúng lúc.

[pause] Điểm độ thật của huy hiệu: chín trên mười. Món đồ thật nhất trong cả video.
```

### c08 · Bảng điểm độ thật / Góc nhìn của Kaku: khoa học phục vụ suy luận

Khoảng 152 giây · cảnh s64–s76 · 1979 ký tự

**Gemini**

```text
Nhưng đừng quên còn một món nữa, không nằm trong phòng thí nghiệm: những chiếc huy hiệu của Đội thám tử nhí.

<short pause> Kaku gom lại bảng điểm. Cao nhất là huy hiệu thám tử, chín điểm, rồi cặp kính truy tìm, tám điểm, và chiếc nơ đổi giọng, bảy điểm. Ba món này ngày nay gần như đã có thật.

<short pause> Ở giữa là ván trượt, năm điểm, và đồng hồ gây mê, bốn điểm. Cuối bảng là viên thuốc, ba điểm, và đôi giày tăng lực, hai điểm.

<short pause> Kaku để ý thêm: những món đồ gần hiện thực nhất đều là thứ giúp giao tiếp và tìm kiếm. Conan thật ra là một bộ truyện về thông tin, và ai có thông tin đúng lúc thì thắng.

<short pause> Có một quy luật thú vị: những món đồ về thông tin, như giọng nói và định vị, thì gần hiện thực nhất. Những món đồ thay đổi cơ thể người thì xa hiện thực nhất.

<short pause> <laugh> Kaku nghĩ điều này phản ánh đúng khoa học ngoài đời: máy móc và điện tử tiến rất nhanh, còn cơ thể người thì phức tạp hơn nhiều so với những gì truyện tranh muốn.

<short pause> Nhưng Kaku muốn nói thêm một điều. Trong Conan, tất cả những món đồ này không bao giờ là thứ giải quyết vụ án. Chúng chỉ giúp Conan nói ra được suy luận của mình.

<short pause> Rất nhiều vụ án trong Conan xoay quanh những kiến thức có thật: tính chất hóa học, thời gian đông cứng của vật liệu, đặc điểm của ánh sáng, thậm chí thói quen tâm lý của con người.

<short pause> Kaku có một bài tập nhỏ: hôm nay, hãy thử quan sát một người quen thật kỹ, rồi đoán xem họ vừa làm gì trước khi gặp bạn. Không cần đồ nghề, chỉ cần để ý.

<short pause> Thứ phá án luôn là quan sát, logic, và kiến thức. Và kiến thức trong Conan, từ hóa học, vật lý tới tâm lý, phần lớn là có thật.

<short pause> Kaku rất muốn biết: vụ án nào trong Conan khiến bạn nhớ nhất vì một chi tiết khoa học bất ngờ? Kể cho Kaku nghe trong phần bình luận nhé.

<short pause> Kaku nghĩ đó là lý do Conan sống được hơn ba mươi năm và vẫn được yêu thích: truyện dạy người xem cách quan sát và suy luận, những thứ không cần phát minh nào cả.

<short pause> Nếu được chọn một món đồ của tiến sĩ Agasa để mang về nhà, bạn chọn món nào, và để làm gì? Kaku đoán nhiều bạn sẽ chọn chiếc nơ để… giả giọng xin nghỉ học. Đừng nhé.
```

**ElevenLabs**

```text
Nhưng đừng quên còn một món nữa, không nằm trong phòng thí nghiệm: những chiếc huy hiệu của Đội thám tử nhí.

[pause] Kaku gom lại bảng điểm. Cao nhất là huy hiệu thám tử, chín điểm, rồi cặp kính truy tìm, tám điểm, và chiếc nơ đổi giọng, bảy điểm. Ba món này ngày nay gần như đã có thật.

[pause] Ở giữa là ván trượt, năm điểm, và đồng hồ gây mê, bốn điểm. Cuối bảng là viên thuốc, ba điểm, và đôi giày tăng lực, hai điểm.

[pause] Kaku để ý thêm: những món đồ gần hiện thực nhất đều là thứ giúp giao tiếp và tìm kiếm. Conan thật ra là một bộ truyện về thông tin, và ai có thông tin đúng lúc thì thắng.

[pause] Có một quy luật thú vị: những món đồ về thông tin, như giọng nói và định vị, thì gần hiện thực nhất. Những món đồ thay đổi cơ thể người thì xa hiện thực nhất.

[pause] [chuckles] Kaku nghĩ điều này phản ánh đúng khoa học ngoài đời: máy móc và điện tử tiến rất nhanh, còn cơ thể người thì phức tạp hơn nhiều so với những gì truyện tranh muốn.

[pause] Nhưng Kaku muốn nói thêm một điều. Trong Conan, tất cả những món đồ này không bao giờ là thứ giải quyết vụ án. Chúng chỉ giúp Conan nói ra được suy luận của mình.

[pause] Rất nhiều vụ án trong Conan xoay quanh những kiến thức có thật: tính chất hóa học, thời gian đông cứng của vật liệu, đặc điểm của ánh sáng, thậm chí thói quen tâm lý của con người.

[pause] Kaku có một bài tập nhỏ: hôm nay, hãy thử quan sát một người quen thật kỹ, rồi đoán xem họ vừa làm gì trước khi gặp bạn. Không cần đồ nghề, chỉ cần để ý.

[pause] Thứ phá án luôn là quan sát, logic, và kiến thức. Và kiến thức trong Conan, từ hóa học, vật lý tới tâm lý, phần lớn là có thật.

[pause] [curious] Kaku rất muốn biết: vụ án nào trong Conan khiến bạn nhớ nhất vì một chi tiết khoa học bất ngờ? Kể cho Kaku nghe trong phần bình luận nhé.

[pause] Kaku nghĩ đó là lý do Conan sống được hơn ba mươi năm và vẫn được yêu thích: truyện dạy người xem cách quan sát và suy luận, những thứ không cần phát minh nào cả.

[pause] Nếu được chọn một món đồ của tiến sĩ Agasa để mang về nhà, bạn chọn món nào, và để làm gì? Kaku đoán nhiều bạn sẽ chọn chiếc nơ để… giả giọng xin nghỉ học. Đừng nhé.
```

### c09 · Kết

Khoảng 45 giây · cảnh s77–s80 · 582 ký tự

**Gemini**

```text
Và nếu một ngày ai đó nói với bạn họ đã chế ra thuốc trẻ hóa, hãy nhớ bảng điểm của Kaku: những gì thay đổi cơ thể người luôn là thứ khó tin nhất.

<short pause> Thuốc teo nhỏ thì còn là giấc mơ của tiểu thuyết. <short pause> Nhưng nơ đổi giọng và kính định vị thì đã ở trong túi chúng ta. Có lẽ tiến sĩ Agasa đi trước thời đại chỉ vài chục năm.

<short pause> Video tiếp theo, Kaku quay lại Jujutsu Kaisen với một trò chơi sinh tử: Tử Diệt Hồi Du. Luật chơi là gì, và làm sao để phá nó?

<short pause> <laugh> Nếu bạn thích kiểu video tách bạch thật và hư cấu, hãy đăng ký kênh để Kaku mở thêm nhiều phòng thí nghiệm nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và nếu một ngày ai đó nói với bạn họ đã chế ra thuốc trẻ hóa, hãy nhớ bảng điểm của Kaku: những gì thay đổi cơ thể người luôn là thứ khó tin nhất.

[pause] Thuốc teo nhỏ thì còn là giấc mơ của tiểu thuyết. [pause] Nhưng nơ đổi giọng và kính định vị thì đã ở trong túi chúng ta. Có lẽ tiến sĩ Agasa đi trước thời đại chỉ vài chục năm.

[pause] Video tiếp theo, Kaku quay lại Jujutsu Kaisen với một trò chơi sinh tử: Tử Diệt Hồi Du. [curious] Luật chơi là gì, và làm sao để phá nó?

[pause] [chuckles] Nếu bạn thích kiểu video tách bạch thật và hư cấu, hãy đăng ký kênh để Kaku mở thêm nhiều phòng thí nghiệm nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
