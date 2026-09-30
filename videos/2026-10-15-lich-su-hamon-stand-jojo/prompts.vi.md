# Bộ prompt · JoJo: Lịch sử sức mạnh từ Hamon đến Stand

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

Lời: Cảnh báo: video có spoiler JoJo phần một tới phần năm, và nhắc nhẹ phần sáu. Phần bảy Steel Ball Run chỉ được…

```text
Wide 16:9 landscape cinematic frame. a Victorian mansion at dusk on one side and a modern Italian city on the other, split by a line of light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Năm 1880, ở nước Anh, một chàng trai quý tộc học cách thở. Chỉ thở thôi, nhưng hơi thở của anh tạo ra năng lư…

```text
Wide 16:9 landscape cinematic frame. a young gentleman breathing deeply on a misty English moor, golden ripples of light around his hands. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Hơn một trăm năm sau, cháu chắt của anh chiến đấu bằng một thứ hoàn toàn khác: một chiến binh vô hình đứng sa…

```text
Wide 16:9 landscape cinematic frame. a stoic young man in a modern city with a translucent guardian figure standing behind him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Từ hơi thở đến chiến binh vô hình, sức mạnh trong JoJo đã thay đổi thế nào, và vì sao? Hôm nay Kaku kể lại lị…

```text
Wide 16:9 landscape cinematic frame. a long corridor of portraits from Victorian to modern times, each with a different glowing aura. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Mỗi thời kỳ hôm nay sẽ có một phát minh sức mạnh mới, và một lý do vì sao cái cũ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook with a timeline sketched from a gas lamp to a neon sign. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Một bộ truyện kéo dài qua nhiều thế hệ

Lời: JoJo's Bizarre Adventure là manga của Araki Hirohiko, bắt đầu từ năm 1987. Điều đặc biệt là truyện chia thành…

```text
Wide 16:9 landscape cinematic frame. a long shelf of manga volumes in many different colors, one section for each part. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Các nhân vật chính đều thuộc cùng một dòng họ, và đều có biệt danh là JoJo. Câu chuyện trải dài từ thế kỷ mườ…

```text
Wide 16:9 landscape cinematic frame. a family tree spanning generations, each branch holding a small glowing mark icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Bản anime do David Production thực hiện từ năm 2012, đã chuyển thể sáu phần đầu. Phần bảy đang phát trên Netf…

```text
Wide 16:9 landscape cinematic frame. a row of film reels with a streaming screen at the end showing a desert horse race. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: vì truyện trải qua hơn một thế kỷ trong câu chuyện, và gần bốn mươi năm ngoài đời, nó là nơi ho…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over a family tree. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · Thời kỳ 1 · 1880: Mặt nạ đá và Hamon

Lời: Thời kỳ đầu tiên là nước Anh thời Victoria. Kẻ thù là ma cà rồng, sinh ra từ một chiếc mặt nạ đá cổ có thể bi…

```text
Wide 16:9 landscape cinematic frame. an ancient stone mask on a pedestal in a candlelit study, tiny spikes along its edges. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Để chống lại chúng, con người có một kỹ thuật cổ gọi là Hamon, hay còn gọi là sóng gợn. Người luyện Hamon dùn…

```text
Wide 16:9 landscape cinematic frame. a figure breathing in a controlled rhythm, golden ripples spreading across the surface of a pond. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Hamon có thể truyền qua nước, qua vật dẫn, qua cả một bông hoa hay một ly rượu. Nó chữa được vết thương nhỏ,…

```text
Wide 16:9 landscape cinematic frame. golden ripples traveling through a glass of wine and up a flower stem into a vampire's shadow. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Phát minh của thời kỳ này là hơi thở. Sức mạnh đến từ kỷ luật và luyện tập, ai chăm chỉ cũng có thể học, như…

```text
Wide 16:9 landscape cinematic frame. a young gentleman training under a stern older mentor by a river. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Giới hạn của nó: Hamon rất khó thể hiện bằng hình ảnh, vì đó là một năng lượng vô hình chạy trong cơ thể. Hãy…

```text
Wide 16:9 landscape cinematic frame. an artist at a desk struggling to draw invisible energy, crumpled papers around. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Hamon cũng có tác dụng ngoài chiến đấu: người luyện lâu năm có thể giữ được sức khỏe và vẻ trẻ trung lâu hơn…

```text
Wide 16:9 landscape cinematic frame. an elegant woman on a balcony who looks young, with an old photograph beside her showing the same face decades earlier. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu bạn đã xem video số năm về các kiểu hơi thở trong Kimetsu no Yaiba, bạn sẽ thấy ý tưởng dùn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at two small breathing diagrams pinned side by side. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Thời kỳ 2 · 1938: Những người đá cổ đại

Lời: Thời kỳ thứ hai nhảy tới năm 1938. Nhân vật chính mới là cháu của Jonathan, một chàng trai tên Joseph, láu cá…

```text
Wide 16:9 landscape cinematic frame. a cocky young man in 1930s clothing grinning on a New York street. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Kẻ thù mới là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá, gọi là những Người Cột. Chúng mạnh hơn ma cà r…

```text
Wide 16:9 landscape cinematic frame. towering ancient beings emerging from a stone pillar deep beneath a Roman ruin. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Hamon được đẩy lên đỉnh cao. Joseph học dưới tay một bậc thầy Hamon, luyện thở hàng tháng trời, kể cả trong l…

```text
Wide 16:9 landscape cinematic frame. a young man training on a tall pillar surrounded by oil, a mentor watching from a balcony. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng phát minh thật sự của thời kỳ này không phải là Hamon mạnh hơn, mà là trí thông minh. Joseph thắng nhờ…

```text
Wide 16:9 landscape cinematic frame. a young man pointing dramatically at an astonished opponent, a speech bubble completed before the opponent speaks. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kết thúc thời kỳ này, kẻ thù mạnh nhất đạt tới dạng sinh vật tối thượng, và không bị đánh bại bằng sức mạnh,…

```text
Wide 16:9 landscape cinematic frame. a volcanic eruption launching a small figure into a starry sky, the figure frozen in the vacuum of space. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Thời kỳ này cũng thêm những vật phẩm quan trọng, như một viên đá đỏ cổ đại có thể khuếch đại ánh sáng. Đó là…

```text
Wide 16:9 landscape cinematic frame. a glowing red gemstone on an ancient altar, beams of light refracting from it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đến đây, Hamon đã chạm tới giới hạn của nó. Những kẻ thù mạnh hơn cần một kiểu sức mạnh mới.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a cracked breathing gauge. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Bước ngoặt: vì sao cần một phát minh mới?

Lời: Trước khi sang thời kỳ ba, hãy dừng lại ở một câu hỏi: vì sao tác giả lại bỏ Hamon, thứ đã làm nên hai phần đ…

```text
Wide 16:9 landscape cinematic frame. a crossroads in the story timeline with a signpost pointing two directions. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Araki từng chia sẻ rằng năng lượng vô hình như Hamon rất khó thể hiện bằng tranh. Đánh nhau bằng tia sáng và…

```text
Wide 16:9 landscape cinematic frame. two fighters exchanging similar golden ripples, the viewer unable to tell them apart. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Ông muốn biến siêu năng lực thành một thứ có hình dạng, để người đọc nhìn thấy được. Ý tưởng về một linh hồn…

```text
Wide 16:9 landscape cinematic frame. a traditional painting of a guardian spirit standing behind a person, soft ink wash style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Kết quả là một phát minh làm thay đổi cả thể loại truyện tranh chiến đấu Nhật Bản: Stand.

```text
Wide 16:9 landscape cinematic frame. a translucent guardian figure bursting from a person's back in a dramatic pose, light rays around it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Thời kỳ 3 · 1989: Stand ra đời

Lời: Thời kỳ thứ ba, năm 1989. Kẻ thù từ phần một, ma cà rồng Dio, trở lại sau một trăm năm dưới đáy biển. Và sự t…

```text
Wide 16:9 landscape cinematic frame. a coffin rising from the seabed, bubbles streaming upward, a faint shadow inside. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Stand là hình ảnh cụ thể của năng lượng sống bên trong một người. Nó xuất hiện như một thực thể đứng cạnh ngư…

```text
Wide 16:9 landscape cinematic frame. a young man standing calmly as a muscular translucent spirit appears behind him, arms crossed. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Cái tên Stand đến từ chính ý nghĩa của nó: thứ đứng bên cạnh bạn. Nhiều Stand trong phần ba được đặt tên theo…

```text
Wide 16:9 landscape cinematic frame. a spread of tarot cards on a table, each card glowing with a different shadowy silhouette. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Phần ba cũng là một chuyến hành trình từ Nhật Bản tới Ai Cập, và mỗi chặng đường là một trận đấu Stand mới vớ…

```text
Wide 16:9 landscape cinematic frame. a map with a dotted route from Japan across Asia to Egypt, small battle icons along the way. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Phát minh của thời kỳ này là hình dạng. Sức mạnh giờ có thể nhìn thấy, có cá tính, có luật riêng, và mỗi trận…

```text
Wide 16:9 landscape cinematic frame. a chessboard where each piece is a different glowing guardian spirit. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Một điểm thú vị: người trong dòng họ Joestar thức tỉnh Stand gần như cùng lúc, vì sự trở lại của kẻ thù cũ đá…

```text
Wide 16:9 landscape cinematic frame. a family gathered around a sick woman in bed, faint vines of spirit energy wrapping around her. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: từ đây, các trận đánh trong JoJo không còn là ai mạnh hơn, mà là ai hiểu luật Stand của đối thủ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot studying a small rulebook with a tiny guardian spirit behind it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Luật cơ bản của Stand

Lời: Để hiểu vì sao Stand thay đổi cách đánh nhau, hãy xem vài luật cơ bản.

```text
Wide 16:9 landscape cinematic frame. a notice board with five pinned rule cards, each with a simple icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Một: mỗi người thường chỉ có một Stand. Hai: chỉ người dùng Stand mới nhìn thấy Stand. Người thường chỉ thấy…

```text
Wide 16:9 landscape cinematic frame. ordinary people staring in confusion at a floating teacup, a faint spirit visible only to one person. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Ba: Stand bị thương thì người dùng cũng bị thương ở cùng chỗ. Đánh vào Stand cũng là đánh vào người.

```text
Wide 16:9 landscape cinematic frame. a spirit's arm cracking and the user's arm bleeding in the same spot. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Bốn: Stand càng mạnh ở cận chiến thì phạm vi hoạt động càng ngắn. Stand đi xa được thì thường yếu hơn. Đây là…

```text
Wide 16:9 landscape cinematic frame. a diagram with a strong spirit on a short leash and a weaker one on a very long leash. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Năm: năng lực của Stand thường phản ánh tính cách người dùng. Người nóng nảy có Stand thô bạo, người tỉ mỉ có…

```text
Wide 16:9 landscape cinematic frame. three people with spirits that visibly mirror their personalities: fiery, precise, gentle. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: với những luật này, một Stand yếu vẫn có thể thắng một Stand mạnh nếu người dùng thông minh hơn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot moving a tiny pawn to checkmate a much bigger piece. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Các kiểu Stand

Lời: Khi Stand ngày càng nhiều, fan và các tài liệu tham khảo bắt đầu chia chúng thành vài kiểu lớn. Hiểu các kiểu…

```text
Wide 16:9 landscape cinematic frame. a museum hall with display cases, each holding a different kind of glowing spirit. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Kiểu cận chiến: mạnh, nhanh, chính xác, nhưng chỉ hoạt động trong vài mét quanh người dùng. Đây là kiểu của n…

```text
Wide 16:9 landscape cinematic frame. a powerful spirit throwing a flurry of punches within a small circle around its user. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Kiểu tầm xa: có thể đi rất xa người dùng để do thám hay tấn công lén, đổi lại sức mạnh yếu hơn. Kiểu tự động:…

```text
Wide 16:9 landscape cinematic frame. a small spirit flying far across a city while its user sits calmly in a café. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và còn những kiểu đặc biệt hơn: Stand là cả một bầy sinh vật nhỏ, Stand gắn vào một đồ vật, thậm chí có Stand…

```text
Wide 16:9 landscape cinematic frame. a swarm of tiny spirits, a sword glowing with a spirit inside, and a ghostly ship on the sea. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: sự đa dạng này là lý do trận đấu Stand hiếm khi lặp lại. Mỗi kiểu mở ra một cách chơi khác nhau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sorting small spirit figurines into labeled boxes. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Hamon và Stand: bảng so sánh

Lời: Trước khi nói về ảnh hưởng, hãy đặt hai hệ thống lên bàn cân.

```text
Wide 16:9 landscape cinematic frame. a balance scale with golden ripples on one side and a guardian spirit on the other. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Về cách có được: Hamon là kỹ thuật, ai chăm chỉ và có thầy giỏi đều có thể học. Stand là tài năng hoặc được đ…

```text
Wide 16:9 landscape cinematic frame. a student training breath with a mentor on one side, a person struck by a glowing arrow on the other. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Về hình ảnh: Hamon là năng lượng vô hình. Stand có hình dạng, có tính cách, và mỗi cái mỗi khác.

```text
Wide 16:9 landscape cinematic frame. invisible ripples on one side, a colorful distinct spirit on the other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Về đối thủ: Hamon sinh ra để diệt ma cà rồng và sinh vật cổ đại. Stand thì dùng được với mọi đối thủ, kể cả c…

```text
Wide 16:9 landscape cinematic frame. a vampire shadow recoiling from golden light, and two ordinary people facing off with spirits. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Về chiến thuật: Hamon thắng bằng kỷ luật và mưu trí. Stand thắng bằng việc hiểu luật và tìm kẽ hở trong năng…

```text
Wide 16:9 landscape cinematic frame. a disciplined fighter meditating, and a clever fighter studying a rulebook. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: không có hệ thống nào tốt hơn tuyệt đối. Chúng chỉ phù hợp với những câu chuyện khác nhau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a ripple in one wing and a tiny spirit in the other, smiling. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Thời kỳ 4 · 1999: Stand trong đời thường

Lời: Thời kỳ thứ tư, năm 1999, ở một thị trấn nhỏ yên bình của Nhật Bản. Không còn hành trình vòng quanh thế giới,…

```text
Wide 16:9 landscape cinematic frame. a quiet Japanese suburban town with small shops and a train station on a sunny day. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Phát minh của thời kỳ này là mũi tên. Truyện tiết lộ những mũi tên đặc biệt có thể đánh thức Stand ở người bị…

```text
Wide 16:9 landscape cinematic frame. an ornate ancient arrowhead glowing faintly on a velvet cloth. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nhờ vậy, Stand không còn chỉ là sức mạnh của dòng máu đặc biệt. Người bình thường trong thị trấn cũng có thể…

```text
Wide 16:9 landscape cinematic frame. an ordinary chef, a manga artist and a student each with a small spirit beside them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Stand ở đây thường có năng lực rất đời thường và kỳ quặc: chữa bệnh bằng đồ ăn, biến người thành cuốn sách, h…

```text
Wide 16:9 landscape cinematic frame. a plate of food glowing with healing light and a person's face opening like the pages of a book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Và kẻ thù đáng sợ nhất lại là một người đàn ông bình thường chỉ muốn sống yên ổn, nhưng thực ra là một kẻ giế…

```text
Wide 16:9 landscape cinematic frame. a neatly dressed office worker walking home at dusk, his long shadow looking sinister. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Và người dùng Stand có xu hướng bị thu hút về phía nhau, như có một sợi dây vô hình kéo họ lại. Truyện dùng đ…

```text
Wide 16:9 landscape cinematic frame. invisible threads drawing several people with small spirits toward the same street corner. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: phần bốn chứng minh Stand không cần những trận chiến thế giới. Chỉ một thị trấn nhỏ cũng đủ chứ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting in a small café, a tiny spirit stirring its coffee. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Thời kỳ 5 · 2001: vượt qua giới hạn của Stand

Lời: Thời kỳ thứ năm, năm 2001, ở nước Ý. Thế giới của các băng đảng, nơi Stand là vũ khí của những người sống ngo…

```text
Wide 16:9 landscape cinematic frame. a sunlit Italian coastal city with narrow streets, a group of stylish silhouettes walking together. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nhân vật chính là một thiếu niên có Stand ban cho sự sống, biến đồ vật thành sinh vật. Cậu có một ước mơ kỳ l…

```text
Wide 16:9 landscape cinematic frame. a young man touching a stone that sprouts into a living tree full of birds. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Phát minh của thời kỳ này là vượt qua giới hạn. Khi mũi tên đâm vào chính một Stand, Stand đó tiến hóa lên mộ…

```text
Wide 16:9 landscape cinematic frame. a spirit pierced by a glowing arrow, transforming into a brighter, more intricate form. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Kẻ thù của phần này có năng lực xóa đi một khoảng thời gian và chỉ mình hắn nhớ chuyện gì đã xảy ra. Để thắng…

```text
Wide 16:9 landscape cinematic frame. a clock with a missing section of its face, the hands jumping over the gap. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Phần năm còn nổi tiếng với phong cách thời trang và tạo dáng đặc trưng. Những tư thế kỳ lạ của nhân vật đã tr…

```text
Wide 16:9 landscape cinematic frame. a group of silhouettes striking dramatic twisting poses on an Italian street, fans copying them in the background. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đến đây, Stand không chỉ là nắm đấm có hình dạng nữa. Nó có thể chạm vào thời gian, số phận và…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a clock that skips seconds, blinking in confusion. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Sau đó: vòng tròn khép lại và mở lại

Lời: Ở phần sáu, câu chuyện đi tới một kết thúc rất lớn, lớn tới mức thế giới của các phần trước khép lại theo một…

```text
Wide 16:9 landscape cinematic frame. a spiral galaxy slowly closing into a circle of light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và từ phần bảy, Steel Ball Run, JoJo mở ra một thế giới mới, với những nhân vật mới mang tên quen thuộc. Ở đó…

```text
Wide 16:9 landscape cinematic frame. a desert trail at sunrise with a spinning steel ball tracing a golden spiral. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku đã phân tích khoa học đằng sau kỹ thuật Xoay ở video số mười ba. Điều thú vị là JoJo đi một vòng: từ kỹ…

```text
Wide 16:9 landscape cinematic frame. a circular diagram with breath, spirit and spin connected by arrows. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: rất ít bộ truyện dám tự làm mới hệ thống sức mạnh của chính mình nhiều lần như vậy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot applauding a wheel of power icons turning slowly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Ảnh hưởng của Stand

Lời: Stand không chỉ thay đổi JoJo. Nó ảnh hưởng tới rất nhiều bộ truyện tranh chiến đấu ra đời sau đó.

```text
Wide 16:9 landscape cinematic frame. a family tree of many manga-style silhouettes all branching from a single guardian spirit. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Ý tưởng một năng lực có luật riêng, có điểm yếu riêng, và trận đấu được thắng bằng cách hiểu luật của đối thủ…

```text
Wide 16:9 landscape cinematic frame. a chalkboard comparing several rulebooks side by side, with similar headings. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nhiều fan cho rằng những hệ thống như Nen trong Hunter x Hunter hay lời nguyền trong Jujutsu Kaisen đều có ch…

```text
Wide 16:9 landscape cinematic frame. a hexagon, a dark dome and a guardian spirit arranged in a triangle with dotted lines. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và cụm từ này là Stand à, đã trở thành một câu đùa quen thuộc trong cộng đồng anime, mỗi khi ai đó có một năn…

```text
Wide 16:9 landscape cinematic frame. a group of friends laughing as one of them points at a strangely floating object. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Góc nhìn của Kaku: sức mạnh thay đổi theo thời đại · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại cả lịch sử, Kaku thấy mỗi phát minh sức mạnh trong JoJo đều khớp với thời đại mà nó xuất hiện.

```text
Wide 16:9 landscape cinematic frame. the owl mascot walking through a gallery where each room represents a different era. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nước Anh thời Victoria có Hamon: kỷ luật, lễ nghi, và hơi thở của một quý ông. Năm 1938 có mưu trí: thời của…

```text
Wide 16:9 landscape cinematic frame. a Victorian gentleman bowing politely, then a 1930s adventurer winking with a grin. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Năm 1989 có Stand: sức mạnh cá nhân, mỗi người một kiểu. Năm 1999 có Stand đời thường: phép màu trong một thị…

```text
Wide 16:9 landscape cinematic frame. three rooms showing a traveler with a spirit, a small town with quirky spirits, and a clock without hands. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Kaku nghĩ điều đó cho thấy Araki không chỉ tạo ra sức mạnh, mà dùng sức mạnh để kể về thời đại và con người c…

```text
Wide 16:9 landscape cinematic frame. a painter's easel with a portrait that changes era each time it is looked at. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và có một thứ không bao giờ đổi qua mọi thời kỳ: dòng họ JoJo luôn chiến đấu vì người khác, bằng lòng dũng cả…

```text
Wide 16:9 landscape cinematic frame. a line of silhouettes from different eras standing side by side, each with a faint glowing mark. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Dòng thời gian thu gọn

Lời: Tóm tắt dòng thời gian. Năm 1880: mặt nạ đá và Hamon, phát minh là hơi thở. Năm 1938: những Người Cột, phát m…

```text
Wide 16:9 landscape cinematic frame. a compact timeline with a stone mask icon and a grinning face icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Năm 1989: Stand ra đời, phát minh là hình dạng. Năm 1999: mũi tên, Stand trong đời thường.

```text
Wide 16:9 landscape cinematic frame. the timeline continuing with a guardian spirit icon and an arrowhead icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Năm 2001: Stand tiến hóa, vượt qua giới hạn. Rồi một vòng tròn khép lại, và thế giới mới mở ra với kỹ thuật X…

```text
Wide 16:9 landscape cinematic frame. the timeline ending with a clock icon and a spinning golden spiral. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu có Stand, bạn muốn nó có năng lực gì, và tên của nó sẽ là gì? Theo truyền thống từ phần…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank card and a small music note. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Video tới, Kaku sẽ vẽ một cây phả hệ thật lớn cho thế giới Naruto: Otsutsuki, Uchiha, Senju, và Uzumaki, để x…

```text
Wide 16:9 landscape cinematic frame. a giant glowing tree with roots in the moon and four large branches. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku thở một hơi thật sâu đây. Hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking a deep breath with golden ripples around it, then waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Một bộ truyện kéo dài qua nhiều thế hệ

Khoảng 99 giây · cảnh s01–s09 · 1289 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler JoJo phần một tới phần năm, và nhắc nhẹ phần sáu. Phần bảy Steel Ball Run chỉ được nhắc lại từ video số mười ba.

<short pause> Năm 1880, ở nước Anh, một chàng trai quý tộc học cách thở. Chỉ thở thôi, nhưng hơi thở của anh tạo ra năng lượng giống như ánh mặt trời, đủ để tiêu diệt ma cà rồng.

<short pause> Hơn một trăm năm sau, cháu chắt của anh chiến đấu bằng một thứ hoàn toàn khác: một chiến binh vô hình đứng sau lưng, mà người thường không nhìn thấy.

<short pause> Từ hơi thở đến chiến binh vô hình, sức mạnh trong JoJo đã thay đổi thế nào, và vì sao? Hôm nay Kaku kể lại lịch sử đó, từng thời kỳ một.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Mỗi thời kỳ hôm nay sẽ có một phát minh sức mạnh mới, và một lý do vì sao cái cũ không còn đủ.

<short pause> JoJo's Bizarre Adventure là manga của Araki Hirohiko, bắt đầu từ năm 1987. Điều đặc biệt là truyện chia thành nhiều phần, mỗi phần có một nhân vật chính khác nhau.

<short pause> Các nhân vật chính đều thuộc cùng một dòng họ, và đều có biệt danh là JoJo. Câu chuyện trải dài từ thế kỷ mười chín tới thế kỷ hai mươi mốt.

<short pause> Bản anime do David Production thực hiện từ năm 2012, đã chuyển thể sáu phần đầu. Phần bảy đang phát trên Netflix năm 2026.

<short pause> Kaku ghi chú: vì truyện trải qua hơn một thế kỷ trong câu chuyện, và gần bốn mươi năm ngoài đời, nó là nơi hoàn hảo để xem một hệ thống sức mạnh tiến hóa.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler JoJo phần một tới phần năm, và nhắc nhẹ phần sáu. Phần bảy Steel Ball Run chỉ được nhắc lại từ video số mười ba.

[pause] Năm 1880, ở nước Anh, một chàng trai quý tộc học cách thở. Chỉ thở thôi, nhưng hơi thở của anh tạo ra năng lượng giống như ánh mặt trời, đủ để tiêu diệt ma cà rồng.

[pause] Hơn một trăm năm sau, cháu chắt của anh chiến đấu bằng một thứ hoàn toàn khác: một chiến binh vô hình đứng sau lưng, mà người thường không nhìn thấy.

[pause] [curious] Từ hơi thở đến chiến binh vô hình, sức mạnh trong JoJo đã thay đổi thế nào, và vì sao? Hôm nay Kaku kể lại lịch sử đó, từng thời kỳ một.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Mỗi thời kỳ hôm nay sẽ có một phát minh sức mạnh mới, và một lý do vì sao cái cũ không còn đủ.

[pause] JoJo's Bizarre Adventure là manga của Araki Hirohiko, bắt đầu từ năm 1987. Điều đặc biệt là truyện chia thành nhiều phần, mỗi phần có một nhân vật chính khác nhau.

[pause] Các nhân vật chính đều thuộc cùng một dòng họ, và đều có biệt danh là JoJo. Câu chuyện trải dài từ thế kỷ mười chín tới thế kỷ hai mươi mốt.

[pause] Bản anime do David Production thực hiện từ năm 2012, đã chuyển thể sáu phần đầu. Phần bảy đang phát trên Netflix năm 2026.

[pause] Kaku ghi chú: vì truyện trải qua hơn một thế kỷ trong câu chuyện, và gần bốn mươi năm ngoài đời, nó là nơi hoàn hảo để xem một hệ thống sức mạnh tiến hóa.
```

### c02 · Thời kỳ 1 · 1880: Mặt nạ đá và Hamon

Khoảng 90 giây · cảnh s10–s16 · 1164 ký tự

**Gemini**

```text
Thời kỳ đầu tiên là nước Anh thời Victoria. Kẻ thù là ma cà rồng, sinh ra từ một chiếc mặt nạ đá cổ có thể biến người đội thành sinh vật bất tử, mạnh vô song, chỉ sợ ánh mặt trời.

<short pause> Để chống lại chúng, con người có một kỹ thuật cổ gọi là Hamon, hay còn gọi là sóng gợn. Người luyện Hamon dùng nhịp thở đặc biệt để tạo năng lượng giống ánh mặt trời trong cơ thể.

<short pause> Hamon có thể truyền qua nước, qua vật dẫn, qua cả một bông hoa hay một ly rượu. Nó chữa được vết thương nhỏ, và là vũ khí chí mạng với ma cà rồng.

<short pause> Phát minh của thời kỳ này là hơi thở. Sức mạnh đến từ kỷ luật và luyện tập, ai chăm chỉ cũng có thể học, như Jonathan học từ người thầy của mình.

<short pause> Giới hạn của nó: Hamon rất khó thể hiện bằng hình ảnh, vì đó là một năng lượng vô hình chạy trong cơ thể. Hãy nhớ giới hạn này, vì nó sẽ dẫn tới một phát minh sau.

<short pause> Hamon cũng có tác dụng ngoài chiến đấu: người luyện lâu năm có thể giữ được sức khỏe và vẻ trẻ trung lâu hơn người thường. Có bậc thầy Hamon trông trẻ hơn rất nhiều so với tuổi thật.

<short pause> <laugh> Kaku ghi chú: nếu bạn đã xem video số năm về các kiểu hơi thở trong Kimetsu no Yaiba, bạn sẽ thấy ý tưởng dùng hơi thở chống lại quỷ đã có từ rất lâu trước đó trong JoJo.
```

**ElevenLabs**

```text
Thời kỳ đầu tiên là nước Anh thời Victoria. Kẻ thù là ma cà rồng, sinh ra từ một chiếc mặt nạ đá cổ có thể biến người đội thành sinh vật bất tử, mạnh vô song, chỉ sợ ánh mặt trời.

[pause] Để chống lại chúng, con người có một kỹ thuật cổ gọi là Hamon, hay còn gọi là sóng gợn. Người luyện Hamon dùng nhịp thở đặc biệt để tạo năng lượng giống ánh mặt trời trong cơ thể.

[pause] Hamon có thể truyền qua nước, qua vật dẫn, qua cả một bông hoa hay một ly rượu. Nó chữa được vết thương nhỏ, và là vũ khí chí mạng với ma cà rồng.

[pause] Phát minh của thời kỳ này là hơi thở. Sức mạnh đến từ kỷ luật và luyện tập, ai chăm chỉ cũng có thể học, như Jonathan học từ người thầy của mình.

[pause] Giới hạn của nó: Hamon rất khó thể hiện bằng hình ảnh, vì đó là một năng lượng vô hình chạy trong cơ thể. Hãy nhớ giới hạn này, vì nó sẽ dẫn tới một phát minh sau.

[pause] Hamon cũng có tác dụng ngoài chiến đấu: người luyện lâu năm có thể giữ được sức khỏe và vẻ trẻ trung lâu hơn người thường. Có bậc thầy Hamon trông trẻ hơn rất nhiều so với tuổi thật.

[pause] [chuckles] Kaku ghi chú: nếu bạn đã xem video số năm về các kiểu hơi thở trong Kimetsu no Yaiba, bạn sẽ thấy ý tưởng dùng hơi thở chống lại quỷ đã có từ rất lâu trước đó trong JoJo.
```

### c03 · Thời kỳ 2 · 1938: Những người đá cổ đại / Bước ngoặt: vì sao cần một phát minh mới?

Khoảng 122 giây · cảnh s17–s27 · 1583 ký tự

**Gemini**

```text
Thời kỳ thứ hai nhảy tới năm 1938. Nhân vật chính mới là cháu của Jonathan, một chàng trai tên Joseph, láu cá và thích lừa đối thủ.

<short pause> Kẻ thù mới là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá, gọi là những Người Cột. Chúng mạnh hơn ma cà rồng rất nhiều, và ăn thịt cả ma cà rồng.

<short pause> Hamon được đẩy lên đỉnh cao. Joseph học dưới tay một bậc thầy Hamon, luyện thở hàng tháng trời, kể cả trong lúc ngủ.

<short pause> Nhưng phát minh thật sự của thời kỳ này không phải là Hamon mạnh hơn, mà là trí thông minh. Joseph thắng nhờ mưu mẹo, đoán trước câu tiếp theo đối thủ sẽ nói, và biến mọi thứ xung quanh thành vũ khí.

<short pause> Kết thúc thời kỳ này, kẻ thù mạnh nhất đạt tới dạng sinh vật tối thượng, và không bị đánh bại bằng sức mạnh, mà bị đẩy lên vũ trụ bằng một vụ phun trào núi lửa.

<short pause> Thời kỳ này cũng thêm những vật phẩm quan trọng, như một viên đá đỏ cổ đại có thể khuếch đại ánh sáng. Đó là thứ mà những Người Cột khao khát để vượt qua điểm yếu của mình.

<short pause> <laugh> Kaku ghi chú: đến đây, Hamon đã chạm tới giới hạn của nó. Những kẻ thù mạnh hơn cần một kiểu sức mạnh mới.

<short pause> Trước khi sang thời kỳ ba, hãy dừng lại ở một câu hỏi: vì sao tác giả lại bỏ Hamon, thứ đã làm nên hai phần đầu?

<short pause> Araki từng chia sẻ rằng năng lượng vô hình như Hamon rất khó thể hiện bằng tranh. Đánh nhau bằng tia sáng và sóng gợn mãi thì người đọc khó phân biệt ai đang làm gì.

<short pause> Ông muốn biến siêu năng lực thành một thứ có hình dạng, để người đọc nhìn thấy được. Ý tưởng về một linh hồn hộ mệnh đứng sau lưng con người trong văn hóa Nhật đã gợi cảm hứng cho ông.

<short pause> Kết quả là một phát minh làm thay đổi cả thể loại truyện tranh chiến đấu Nhật Bản: Stand.
```

**ElevenLabs**

```text
Thời kỳ thứ hai nhảy tới năm 1938. Nhân vật chính mới là cháu của Jonathan, một chàng trai tên Joseph, láu cá và thích lừa đối thủ.

[pause] Kẻ thù mới là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá, gọi là những Người Cột. Chúng mạnh hơn ma cà rồng rất nhiều, và ăn thịt cả ma cà rồng.

[pause] Hamon được đẩy lên đỉnh cao. Joseph học dưới tay một bậc thầy Hamon, luyện thở hàng tháng trời, kể cả trong lúc ngủ.

[pause] Nhưng phát minh thật sự của thời kỳ này không phải là Hamon mạnh hơn, mà là trí thông minh. Joseph thắng nhờ mưu mẹo, đoán trước câu tiếp theo đối thủ sẽ nói, và biến mọi thứ xung quanh thành vũ khí.

[pause] Kết thúc thời kỳ này, kẻ thù mạnh nhất đạt tới dạng sinh vật tối thượng, và không bị đánh bại bằng sức mạnh, mà bị đẩy lên vũ trụ bằng một vụ phun trào núi lửa.

[pause] Thời kỳ này cũng thêm những vật phẩm quan trọng, như một viên đá đỏ cổ đại có thể khuếch đại ánh sáng. Đó là thứ mà những Người Cột khao khát để vượt qua điểm yếu của mình.

[pause] [chuckles] Kaku ghi chú: đến đây, Hamon đã chạm tới giới hạn của nó. Những kẻ thù mạnh hơn cần một kiểu sức mạnh mới.

[pause] [curious] Trước khi sang thời kỳ ba, hãy dừng lại ở một câu hỏi: vì sao tác giả lại bỏ Hamon, thứ đã làm nên hai phần đầu?

[pause] Araki từng chia sẻ rằng năng lượng vô hình như Hamon rất khó thể hiện bằng tranh. Đánh nhau bằng tia sáng và sóng gợn mãi thì người đọc khó phân biệt ai đang làm gì.

[pause] Ông muốn biến siêu năng lực thành một thứ có hình dạng, để người đọc nhìn thấy được. Ý tưởng về một linh hồn hộ mệnh đứng sau lưng con người trong văn hóa Nhật đã gợi cảm hứng cho ông.

[pause] Kết quả là một phát minh làm thay đổi cả thể loại truyện tranh chiến đấu Nhật Bản: Stand.
```

### c04 · Thời kỳ 3 · 1989: Stand ra đời / Luật cơ bản của Stand

Khoảng 139 giây · cảnh s28–s40 · 1803 ký tự

**Gemini**

```text
Thời kỳ thứ ba, năm 1989. Kẻ thù từ phần một, ma cà rồng Dio, trở lại sau một trăm năm dưới đáy biển. Và sự trở lại của hắn đánh thức một sức mạnh mới trong dòng họ Joestar.

<short pause> Stand là hình ảnh cụ thể của năng lượng sống bên trong một người. Nó xuất hiện như một thực thể đứng cạnh người dùng, và mỗi Stand có một năng lực riêng.

<short pause> Cái tên Stand đến từ chính ý nghĩa của nó: thứ đứng bên cạnh bạn. Nhiều Stand trong phần ba được đặt tên theo các lá bài Tarot.

<short pause> Phần ba cũng là một chuyến hành trình từ Nhật Bản tới Ai Cập, và mỗi chặng đường là một trận đấu Stand mới với năng lực kỳ lạ khác nhau.

<short pause> Phát minh của thời kỳ này là hình dạng. Sức mạnh giờ có thể nhìn thấy, có cá tính, có luật riêng, và mỗi trận đấu trở thành một câu đố.

<short pause> Một điểm thú vị: người trong dòng họ Joestar thức tỉnh Stand gần như cùng lúc, vì sự trở lại của kẻ thù cũ đánh thức sức mạnh trong dòng máu. Có người không chịu nổi Stand của mình và đổ bệnh, tạo ra lý do cho cả chuyến hành trình.

<short pause> <laugh> Kaku ghi chú: từ đây, các trận đánh trong JoJo không còn là ai mạnh hơn, mà là ai hiểu luật Stand của đối thủ trước.

<short pause> Để hiểu vì sao Stand thay đổi cách đánh nhau, hãy xem vài luật cơ bản.

<short pause> Một: mỗi người thường chỉ có một Stand. Hai: chỉ người dùng Stand mới nhìn thấy Stand. Người thường chỉ thấy hậu quả, như đồ vật tự bay hay vết thương tự xuất hiện.

<short pause> Ba: Stand bị thương thì người dùng cũng bị thương ở cùng chỗ. Đánh vào Stand cũng là đánh vào người.

<short pause> Bốn: Stand càng mạnh ở cận chiến thì phạm vi hoạt động càng ngắn. Stand đi xa được thì thường yếu hơn. Đây là luật cân bằng rất quan trọng.

<short pause> Năm: năng lực của Stand thường phản ánh tính cách người dùng. Người nóng nảy có Stand thô bạo, người tỉ mỉ có Stand tinh xảo.

<short pause> Kaku ghi chú: với những luật này, một Stand yếu vẫn có thể thắng một Stand mạnh nếu người dùng thông minh hơn. Đó là cái hay của JoJo.
```

**ElevenLabs**

```text
Thời kỳ thứ ba, năm 1989. Kẻ thù từ phần một, ma cà rồng Dio, trở lại sau một trăm năm dưới đáy biển. Và sự trở lại của hắn đánh thức một sức mạnh mới trong dòng họ Joestar.

[pause] Stand là hình ảnh cụ thể của năng lượng sống bên trong một người. Nó xuất hiện như một thực thể đứng cạnh người dùng, và mỗi Stand có một năng lực riêng.

[pause] Cái tên Stand đến từ chính ý nghĩa của nó: thứ đứng bên cạnh bạn. Nhiều Stand trong phần ba được đặt tên theo các lá bài Tarot.

[pause] Phần ba cũng là một chuyến hành trình từ Nhật Bản tới Ai Cập, và mỗi chặng đường là một trận đấu Stand mới với năng lực kỳ lạ khác nhau.

[pause] Phát minh của thời kỳ này là hình dạng. Sức mạnh giờ có thể nhìn thấy, có cá tính, có luật riêng, và mỗi trận đấu trở thành một câu đố.

[pause] Một điểm thú vị: người trong dòng họ Joestar thức tỉnh Stand gần như cùng lúc, vì sự trở lại của kẻ thù cũ đánh thức sức mạnh trong dòng máu. Có người không chịu nổi Stand của mình và đổ bệnh, tạo ra lý do cho cả chuyến hành trình.

[pause] [chuckles] Kaku ghi chú: từ đây, các trận đánh trong JoJo không còn là ai mạnh hơn, mà là ai hiểu luật Stand của đối thủ trước.

[pause] Để hiểu vì sao Stand thay đổi cách đánh nhau, hãy xem vài luật cơ bản.

[pause] Một: mỗi người thường chỉ có một Stand. Hai: chỉ người dùng Stand mới nhìn thấy Stand. Người thường chỉ thấy hậu quả, như đồ vật tự bay hay vết thương tự xuất hiện.

[pause] Ba: Stand bị thương thì người dùng cũng bị thương ở cùng chỗ. Đánh vào Stand cũng là đánh vào người.

[pause] Bốn: Stand càng mạnh ở cận chiến thì phạm vi hoạt động càng ngắn. Stand đi xa được thì thường yếu hơn. Đây là luật cân bằng rất quan trọng.

[pause] Năm: năng lực của Stand thường phản ánh tính cách người dùng. Người nóng nảy có Stand thô bạo, người tỉ mỉ có Stand tinh xảo.

[pause] Kaku ghi chú: với những luật này, một Stand yếu vẫn có thể thắng một Stand mạnh nếu người dùng thông minh hơn. Đó là cái hay của JoJo.
```

### c05 · Các kiểu Stand / Hamon và Stand: bảng so sánh

Khoảng 106 giây · cảnh s41–s51 · 1384 ký tự

**Gemini**

```text
Khi Stand ngày càng nhiều, fan và các tài liệu tham khảo bắt đầu chia chúng thành vài kiểu lớn. Hiểu các kiểu này, bạn sẽ đoán được trận đấu sẽ diễn ra thế nào.

<short pause> Kiểu cận chiến: mạnh, nhanh, chính xác, nhưng chỉ hoạt động trong vài mét quanh người dùng. Đây là kiểu của nhiều nhân vật chính.

<short pause> Kiểu tầm xa: có thể đi rất xa người dùng để do thám hay tấn công lén, đổi lại sức mạnh yếu hơn. Kiểu tự động: tự hành động theo một luật đơn giản, như tấn công bất kỳ thứ gì nóng nhất.

<short pause> Và còn những kiểu đặc biệt hơn: Stand là cả một bầy sinh vật nhỏ, Stand gắn vào một đồ vật, thậm chí có Stand là một con tàu hay một thanh kiếm.

<short pause> <laugh> Kaku ghi chú: sự đa dạng này là lý do trận đấu Stand hiếm khi lặp lại. Mỗi kiểu mở ra một cách chơi khác nhau.

<short pause> Trước khi nói về ảnh hưởng, hãy đặt hai hệ thống lên bàn cân.

<short pause> Về cách có được: Hamon là kỹ thuật, ai chăm chỉ và có thầy giỏi đều có thể học. Stand là tài năng hoặc được đánh thức, không phải ai cũng có.

<short pause> Về hình ảnh: Hamon là năng lượng vô hình. Stand có hình dạng, có tính cách, và mỗi cái mỗi khác.

<short pause> Về đối thủ: Hamon sinh ra để diệt ma cà rồng và sinh vật cổ đại. Stand thì dùng được với mọi đối thủ, kể cả con người bình thường.

<short pause> Về chiến thuật: Hamon thắng bằng kỷ luật và mưu trí. Stand thắng bằng việc hiểu luật và tìm kẽ hở trong năng lực của đối thủ.

<short pause> Kaku ghi chú: không có hệ thống nào tốt hơn tuyệt đối. Chúng chỉ phù hợp với những câu chuyện khác nhau.
```

**ElevenLabs**

```text
Khi Stand ngày càng nhiều, fan và các tài liệu tham khảo bắt đầu chia chúng thành vài kiểu lớn. Hiểu các kiểu này, bạn sẽ đoán được trận đấu sẽ diễn ra thế nào.

[pause] Kiểu cận chiến: mạnh, nhanh, chính xác, nhưng chỉ hoạt động trong vài mét quanh người dùng. Đây là kiểu của nhiều nhân vật chính.

[pause] Kiểu tầm xa: có thể đi rất xa người dùng để do thám hay tấn công lén, đổi lại sức mạnh yếu hơn. Kiểu tự động: tự hành động theo một luật đơn giản, như tấn công bất kỳ thứ gì nóng nhất.

[pause] Và còn những kiểu đặc biệt hơn: Stand là cả một bầy sinh vật nhỏ, Stand gắn vào một đồ vật, thậm chí có Stand là một con tàu hay một thanh kiếm.

[pause] [chuckles] Kaku ghi chú: sự đa dạng này là lý do trận đấu Stand hiếm khi lặp lại. Mỗi kiểu mở ra một cách chơi khác nhau.

[pause] Trước khi nói về ảnh hưởng, hãy đặt hai hệ thống lên bàn cân.

[pause] Về cách có được: Hamon là kỹ thuật, ai chăm chỉ và có thầy giỏi đều có thể học. Stand là tài năng hoặc được đánh thức, không phải ai cũng có.

[pause] Về hình ảnh: Hamon là năng lượng vô hình. Stand có hình dạng, có tính cách, và mỗi cái mỗi khác.

[pause] Về đối thủ: Hamon sinh ra để diệt ma cà rồng và sinh vật cổ đại. Stand thì dùng được với mọi đối thủ, kể cả con người bình thường.

[pause] Về chiến thuật: Hamon thắng bằng kỷ luật và mưu trí. Stand thắng bằng việc hiểu luật và tìm kẽ hở trong năng lực của đối thủ.

[pause] Kaku ghi chú: không có hệ thống nào tốt hơn tuyệt đối. Chúng chỉ phù hợp với những câu chuyện khác nhau.
```

### c06 · Thời kỳ 4 · 1999: Stand trong đời thường / Thời kỳ 5 · 2001: vượt qua giới hạn của Stand

Khoảng 153 giây · cảnh s52–s64 · 1992 ký tự

**Gemini**

```text
Thời kỳ thứ tư, năm 1999, ở một thị trấn nhỏ yên bình của Nhật Bản. Không còn hành trình vòng quanh thế giới, câu chuyện ở lại một nơi.

<short pause> Phát minh của thời kỳ này là mũi tên. Truyện tiết lộ những mũi tên đặc biệt có thể đánh thức Stand ở người bị bắn trúng, nếu người đó đủ mạnh để sống sót.

<short pause> Nhờ vậy, Stand không còn chỉ là sức mạnh của dòng máu đặc biệt. Người bình thường trong thị trấn cũng có thể có Stand: một đầu bếp, một họa sĩ truyện tranh, một học sinh.

<short pause> Stand ở đây thường có năng lực rất đời thường và kỳ quặc: chữa bệnh bằng đồ ăn, biến người thành cuốn sách, hay sửa mọi thứ trở lại như cũ.

<short pause> Và kẻ thù đáng sợ nhất lại là một người đàn ông bình thường chỉ muốn sống yên ổn, nhưng thực ra là một kẻ giết người hàng loạt.

<short pause> Và người dùng Stand có xu hướng bị thu hút về phía nhau, như có một sợi dây vô hình kéo họ lại. Truyện dùng điều này để giải thích vì sao một thị trấn nhỏ lại có nhiều người dùng Stand đến vậy.

<short pause> <laugh> Kaku ghi chú: phần bốn chứng minh Stand không cần những trận chiến thế giới. Chỉ một thị trấn nhỏ cũng đủ chứa cả trăm câu chuyện kỳ lạ.

<short pause> Thời kỳ thứ năm, năm 2001, ở nước Ý. Thế giới của các băng đảng, nơi Stand là vũ khí của những người sống ngoài vòng pháp luật.

<short pause> Nhân vật chính là một thiếu niên có Stand ban cho sự sống, biến đồ vật thành sinh vật. Cậu có một ước mơ kỳ lạ: trở thành trùm băng đảng để thay đổi nó từ bên trong.

<short pause> Phát minh của thời kỳ này là vượt qua giới hạn. Khi mũi tên đâm vào chính một Stand, Stand đó tiến hóa lên một dạng cao hơn, với năng lực vượt ra ngoài luật thông thường.

<short pause> Kẻ thù của phần này có năng lực xóa đi một khoảng thời gian và chỉ mình hắn nhớ chuyện gì đã xảy ra. Để thắng hắn, cần một sức mạnh có thể xoay chuyển cả quy luật nhân quả.

<short pause> Phần năm còn nổi tiếng với phong cách thời trang và tạo dáng đặc trưng. Những tư thế kỳ lạ của nhân vật đã trở thành biểu tượng văn hóa đại chúng, được fan khắp thế giới bắt chước.

<short pause> Kaku ghi chú: đến đây, Stand không chỉ là nắm đấm có hình dạng nữa. Nó có thể chạm vào thời gian, số phận và chính thực tại.
```

**ElevenLabs**

```text
Thời kỳ thứ tư, năm 1999, ở một thị trấn nhỏ yên bình của Nhật Bản. Không còn hành trình vòng quanh thế giới, câu chuyện ở lại một nơi.

[pause] Phát minh của thời kỳ này là mũi tên. Truyện tiết lộ những mũi tên đặc biệt có thể đánh thức Stand ở người bị bắn trúng, nếu người đó đủ mạnh để sống sót.

[pause] Nhờ vậy, Stand không còn chỉ là sức mạnh của dòng máu đặc biệt. Người bình thường trong thị trấn cũng có thể có Stand: một đầu bếp, một họa sĩ truyện tranh, một học sinh.

[pause] Stand ở đây thường có năng lực rất đời thường và kỳ quặc: chữa bệnh bằng đồ ăn, biến người thành cuốn sách, hay sửa mọi thứ trở lại như cũ.

[pause] Và kẻ thù đáng sợ nhất lại là một người đàn ông bình thường chỉ muốn sống yên ổn, nhưng thực ra là một kẻ giết người hàng loạt.

[pause] Và người dùng Stand có xu hướng bị thu hút về phía nhau, như có một sợi dây vô hình kéo họ lại. Truyện dùng điều này để giải thích vì sao một thị trấn nhỏ lại có nhiều người dùng Stand đến vậy.

[pause] [chuckles] Kaku ghi chú: phần bốn chứng minh Stand không cần những trận chiến thế giới. Chỉ một thị trấn nhỏ cũng đủ chứa cả trăm câu chuyện kỳ lạ.

[pause] Thời kỳ thứ năm, năm 2001, ở nước Ý. Thế giới của các băng đảng, nơi Stand là vũ khí của những người sống ngoài vòng pháp luật.

[pause] Nhân vật chính là một thiếu niên có Stand ban cho sự sống, biến đồ vật thành sinh vật. Cậu có một ước mơ kỳ lạ: trở thành trùm băng đảng để thay đổi nó từ bên trong.

[pause] Phát minh của thời kỳ này là vượt qua giới hạn. Khi mũi tên đâm vào chính một Stand, Stand đó tiến hóa lên một dạng cao hơn, với năng lực vượt ra ngoài luật thông thường.

[pause] Kẻ thù của phần này có năng lực xóa đi một khoảng thời gian và chỉ mình hắn nhớ chuyện gì đã xảy ra. Để thắng hắn, cần một sức mạnh có thể xoay chuyển cả quy luật nhân quả.

[pause] Phần năm còn nổi tiếng với phong cách thời trang và tạo dáng đặc trưng. Những tư thế kỳ lạ của nhân vật đã trở thành biểu tượng văn hóa đại chúng, được fan khắp thế giới bắt chước.

[pause] Kaku ghi chú: đến đây, Stand không chỉ là nắm đấm có hình dạng nữa. Nó có thể chạm vào thời gian, số phận và chính thực tại.
```

### c07 · Sau đó: vòng tròn khép lại và mở lại / Ảnh hưởng của Stand / Góc nhìn của Kaku: sức mạnh thay đổi theo thời đại

Khoảng 146 giây · cảnh s65–s77 · 1898 ký tự

**Gemini**

```text
Ở phần sáu, câu chuyện đi tới một kết thúc rất lớn, lớn tới mức thế giới của các phần trước khép lại theo một cách mà Kaku sẽ không nói ra.

<short pause> Và từ phần bảy, Steel Ball Run, JoJo mở ra một thế giới mới, với những nhân vật mới mang tên quen thuộc. Ở đó, Hamon không còn, nhưng một kỹ thuật dựa trên hơi thở và tự nhiên lại trở về dưới dạng Xoay.

<short pause> Kaku đã phân tích khoa học đằng sau kỹ thuật Xoay ở video số mười ba. Điều thú vị là JoJo đi một vòng: từ kỹ thuật cơ thể, sang Stand, rồi quay lại kỹ thuật cơ thể, và kết hợp cả hai.

<short pause> <laugh> Kaku ghi chú: rất ít bộ truyện dám tự làm mới hệ thống sức mạnh của chính mình nhiều lần như vậy.

<short pause> Stand không chỉ thay đổi JoJo. Nó ảnh hưởng tới rất nhiều bộ truyện tranh chiến đấu ra đời sau đó.

<short pause> Ý tưởng một năng lực có luật riêng, có điểm yếu riêng, và trận đấu được thắng bằng cách hiểu luật của đối thủ, có thể thấy ở nhiều hệ thống sức mạnh nổi tiếng về sau.

<short pause> Nhiều fan cho rằng những hệ thống như Nen trong Hunter x Hunter hay lời nguyền trong Jujutsu Kaisen đều có chung tinh thần đó. Đây là nhận xét của fan, tác giả các bộ đó không nói là lấy cảm hứng trực tiếp.

<short pause> Và cụm từ này là Stand à, đã trở thành một câu đùa quen thuộc trong cộng đồng anime, mỗi khi ai đó có một năng lực kỳ lạ.

<short pause> Nhìn lại cả lịch sử, Kaku thấy mỗi phát minh sức mạnh trong JoJo đều khớp với thời đại mà nó xuất hiện.

<short pause> Nước Anh thời Victoria có Hamon: kỷ luật, lễ nghi, và hơi thở của một quý ông. Năm 1938 có mưu trí: thời của phiêu lưu và những kẻ láu cá.

<short pause> Năm 1989 có Stand: sức mạnh cá nhân, mỗi người một kiểu. Năm 1999 có Stand đời thường: phép màu trong một thị trấn bình thường. Năm 2001 có Stand vượt giới hạn: câu hỏi về số phận.

<short pause> Kaku nghĩ điều đó cho thấy Araki không chỉ tạo ra sức mạnh, mà dùng sức mạnh để kể về thời đại và con người của từng thời kỳ.

<short pause> Và có một thứ không bao giờ đổi qua mọi thời kỳ: dòng họ JoJo luôn chiến đấu vì người khác, bằng lòng dũng cảm, chứ không chỉ bằng sức mạnh.
```

**ElevenLabs**

```text
Ở phần sáu, câu chuyện đi tới một kết thúc rất lớn, lớn tới mức thế giới của các phần trước khép lại theo một cách mà Kaku sẽ không nói ra.

[pause] Và từ phần bảy, Steel Ball Run, JoJo mở ra một thế giới mới, với những nhân vật mới mang tên quen thuộc. Ở đó, Hamon không còn, nhưng một kỹ thuật dựa trên hơi thở và tự nhiên lại trở về dưới dạng Xoay.

[pause] Kaku đã phân tích khoa học đằng sau kỹ thuật Xoay ở video số mười ba. Điều thú vị là JoJo đi một vòng: từ kỹ thuật cơ thể, sang Stand, rồi quay lại kỹ thuật cơ thể, và kết hợp cả hai.

[pause] [chuckles] Kaku ghi chú: rất ít bộ truyện dám tự làm mới hệ thống sức mạnh của chính mình nhiều lần như vậy.

[pause] Stand không chỉ thay đổi JoJo. Nó ảnh hưởng tới rất nhiều bộ truyện tranh chiến đấu ra đời sau đó.

[pause] Ý tưởng một năng lực có luật riêng, có điểm yếu riêng, và trận đấu được thắng bằng cách hiểu luật của đối thủ, có thể thấy ở nhiều hệ thống sức mạnh nổi tiếng về sau.

[pause] Nhiều fan cho rằng những hệ thống như Nen trong Hunter x Hunter hay lời nguyền trong Jujutsu Kaisen đều có chung tinh thần đó. Đây là nhận xét của fan, tác giả các bộ đó không nói là lấy cảm hứng trực tiếp.

[pause] Và cụm từ này là Stand à, đã trở thành một câu đùa quen thuộc trong cộng đồng anime, mỗi khi ai đó có một năng lực kỳ lạ.

[pause] Nhìn lại cả lịch sử, Kaku thấy mỗi phát minh sức mạnh trong JoJo đều khớp với thời đại mà nó xuất hiện.

[pause] Nước Anh thời Victoria có Hamon: kỷ luật, lễ nghi, và hơi thở của một quý ông. Năm 1938 có mưu trí: thời của phiêu lưu và những kẻ láu cá.

[pause] Năm 1989 có Stand: sức mạnh cá nhân, mỗi người một kiểu. Năm 1999 có Stand đời thường: phép màu trong một thị trấn bình thường. Năm 2001 có Stand vượt giới hạn: câu hỏi về số phận.

[pause] Kaku nghĩ điều đó cho thấy Araki không chỉ tạo ra sức mạnh, mà dùng sức mạnh để kể về thời đại và con người của từng thời kỳ.

[pause] Và có một thứ không bao giờ đổi qua mọi thời kỳ: dòng họ JoJo luôn chiến đấu vì người khác, bằng lòng dũng cảm, chứ không chỉ bằng sức mạnh.
```

### c08 · Dòng thời gian thu gọn / Kết

Khoảng 55 giây · cảnh s78–s83 · 721 ký tự

**Gemini**

```text
Tóm tắt dòng thời gian. Năm 1880: mặt nạ đá và Hamon, phát minh là hơi thở. Năm 1938: những Người Cột, phát minh là mưu trí.

<short pause> Năm 1989: Stand ra đời, phát minh là hình dạng. Năm 1999: mũi tên, Stand trong đời thường.

<short pause> Năm 2001: Stand tiến hóa, vượt qua giới hạn. Rồi một vòng tròn khép lại, và thế giới mới mở ra với kỹ thuật Xoay.

<short pause> Câu hỏi cho bạn: nếu có Stand, bạn muốn nó có năng lực gì, và tên của nó sẽ là gì? Theo truyền thống từ phần bốn, nhiều Stand được đặt theo tên một bài hát hay ban nhạc.

<short pause> Video tới, Kaku sẽ vẽ một cây phả hệ thật lớn cho thế giới Naruto: Otsutsuki, Uchiha, Senju, và Uzumaki, để xem tất cả nối với nhau thế nào.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. <laugh> Kaku thở một hơi thật sâu đây. Hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm tắt dòng thời gian. Năm 1880: mặt nạ đá và Hamon, phát minh là hơi thở. Năm 1938: những Người Cột, phát minh là mưu trí.

[pause] Năm 1989: Stand ra đời, phát minh là hình dạng. Năm 1999: mũi tên, Stand trong đời thường.

[pause] Năm 2001: Stand tiến hóa, vượt qua giới hạn. Rồi một vòng tròn khép lại, và thế giới mới mở ra với kỹ thuật Xoay.

[pause] [curious] Câu hỏi cho bạn: nếu có Stand, bạn muốn nó có năng lực gì, và tên của nó sẽ là gì? Theo truyền thống từ phần bốn, nhiều Stand được đặt theo tên một bài hát hay ban nhạc.

[pause] Video tới, Kaku sẽ vẽ một cây phả hệ thật lớn cho thế giới Naruto: Otsutsuki, Uchiha, Senju, và Uzumaki, để xem tất cả nối với nhau thế nào.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. [chuckles] Kaku thở một hơi thật sâu đây. Hẹn gặp lại!
```
