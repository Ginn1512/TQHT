# Bộ prompt · Witch Hat Atelier: Nhập môn thế giới nơi phép thuật được vẽ ra

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 96 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (96 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Video này gần như không có spoiler: mình chỉ nói về thế giới, luật phép thuật và những tập đầu tiên của mùa m…

```text
Wide 16:9 landscape cinematic frame. an open wooden door glowing with soft golden light, a quiet fantasy village beyond it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy tưởng tượng một thế giới mà phép thuật không phải thứ bạn sinh ra đã có. Nó là thứ bạn vẽ ra, bằng một câ…

```text
Wide 16:9 landscape cinematic frame. a hand holding a fine dip pen above parchment, glowing ink lines forming a circle. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Chỉ cần vẽ đúng, một vòng tròn trên mặt đất có thể gọi nước, thắp lửa, hay nâng cả một con người bay lên trời.

```text
Wide 16:9 landscape cinematic frame. a glowing circular diagram on a stone floor with a column of water spiraling upward from it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đó là Witch Hat Atelier, bộ anime được gọi là ứng viên anime của năm 2026. Và hôm nay mình sẽ dẫn bạn đi qua…

```text
Wide 16:9 landscape cinematic frame. a tall pointed witch hat resting on a desk beside ink bottles and sketches, morning light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ không phải sổ ghi chép nữa, mà là một cuốn sổ vẽ phép thuật.

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook whose pages glow with circular diagrams. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Cuối video, Kaku sẽ thử tự vẽ một phép theo đúng luật của thế giới này, và gợi ý cho bạn nên bắt đầu xem từ đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny dip pen with a drop of glowing ink on its tip. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Bộ truyện này là gì?

Lời: Witch Hat Atelier là manga của nữ tác giả Shirahama Kamome, bắt đầu đăng từ năm 2016. Tên tiếng Nhật có nghĩa…

```text
Wide 16:9 landscape cinematic frame. a stack of hand-bound sketchbooks tied with ribbon beside a pointed hat on a wooden shelf. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Điều khiến bộ truyện nổi tiếng trước tiên là nét vẽ. Mỗi trang giống như tranh minh họa trong sách truyện cổ,…

```text
Wide 16:9 landscape cinematic frame. an intricate pen-and-ink style fantasy landscape with fine hatching, a castle on a hill. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Bộ truyện đã nhận nhiều giải thưởng truyện tranh quốc tế, và được độc giả phương Tây yêu thích không kém độc…

```text
Wide 16:9 landscape cinematic frame. a small shelf of glowing award medals beside an open illustrated book. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Bản anime do studio Bug Films thực hiện, ra mắt ngày 6 tháng 4 năm 2026 với hai tập liền, và nhanh chóng được…

```text
Wide 16:9 landscape cinematic frame. a calendar page marked with a small star, a film strip unrolling across a desk. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Trước khi phát sóng, nhiều người lo lắng vì studio này từng gặp khó khăn về tiến độ với bộ trước. Nhưng những…

```text
Wide 16:9 landscape cinematic frame. a worried owl silhouette looking at a stack of papers, then a relieved sunrise behind it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là bộ fantasy nhẹ nhàng, không phải kiểu đánh nhau liên tục. Nếu bạn thích Frieren, rất có…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a bookmark between two books glowing with soft magic. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Thế giới của những bí mật

Lời: Trong thế giới này, người thường tin rằng phù thủy là những người sinh ra đã có phép thuật. Họ nghĩ đó là tài…

```text
Wide 16:9 landscape cinematic frame. villagers gazing up in awe at a cloaked figure floating above a market square. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nhưng đó là một lời nói dối được giữ gìn cẩn thận. Sự thật là ai cũng có thể dùng phép, nếu biết cách vẽ và c…

```text
Wide 16:9 landscape cinematic frame. a closed book with a heavy lock, faint glowing lines escaping from between its pages. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Vì sao phải giấu? Trong quá khứ, phép thuật từng bị dùng vào chiến tranh và gây ra thảm họa. Các phù thủy quy…

```text
Wide 16:9 landscape cinematic frame. a ruined ancient battlefield under a dark sky, faded glowing circles scorched into the earth. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Họ lập ra một hiệp ước. Từ đó, phép thuật chỉ được truyền dạy trong giới phù thủy, và mọi hiểu biết về nó bị…

```text
Wide 16:9 landscape cinematic frame. a long table where cloaked figures sign a large scroll by candlelight. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và nếu một người thường vô tình nhìn thấy cách phép được vẽ ra? Theo luật, ký ức đó phải bị xóa.

```text
Wide 16:9 landscape cinematic frame. a figure with a glowing hand hovering near the forehead of a sleeping villager, memories drifting away as light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Đây là nền móng của cả câu chuyện: một thế giới đẹp như tranh, nhưng được xây trên một bí mật mà ai biết được…

```text
Wide 16:9 landscape cinematic frame. a picturesque fantasy town at dusk with a long shadow of a locked keyhole stretching across it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Cô bé muốn trở thành phù thủy

Lời: Nhân vật chính là Coco, một cô bé sống ở làng quê, con gái của một thợ may. Từ nhỏ, cô đã mơ được làm phù thủ…

```text
Wide 16:9 landscape cinematic frame. a young girl with a sketchbook sitting on a hill above a small village, looking at the sky. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng vì tin rằng phép thuật là bẩm sinh, Coco nghĩ giấc mơ đó là không thể. Cô không có phép, nên chỉ biết đ…

```text
Wide 16:9 landscape cinematic frame. a young girl pressing her face to a shop window full of magical trinkets, reflection looking sad. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Khi còn nhỏ, Coco từng nhận được một cuốn sách tranh về phép thuật và một cây bút từ một người lạ đội mũ rộng…

```text
Wide 16:9 landscape cinematic frame. a mysterious figure in a wide-brimmed hat at a night festival handing a small book to a child. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Một ngày, một phù thủy tên là Qifrey ghé qua tiệm may nhà cô. Coco lén nhìn thấy điều không ai được nhìn: anh…

```text
Wide 16:9 landscape cinematic frame. a girl peeking through a door crack as a cloaked figure draws a glowing circle on the floor. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Trong đầu cô bé bừng sáng một ý nghĩ: nếu phép thuật được vẽ ra, thì mình cũng có thể vẽ.

```text
Wide 16:9 landscape cinematic frame. a girl's eyes widening with reflected golden circles, a lightbulb-like spark of ink above her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là khoảnh khắc mở đầu rất hay, vì nó biến một giấc mơ không thể thành một thứ có thể học đư…

```text
Wide 16:9 landscape cinematic frame. the owl mascot with sparkling eyes, holding a tiny pen up like a torch. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Cái giá của một nét vẽ

Lời: Coco mở cuốn sách tranh cũ ra, chép lại một vòng tròn trong đó lên sàn nhà. Cô không biết đó là loại phép gì.

```text
Wide 16:9 landscape cinematic frame. a girl kneeling on a wooden floor at night carefully copying a circle from an old picture book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Phép được kích hoạt, và hậu quả vượt quá sức tưởng tượng: người mẹ của Coco bị bao phủ trong pha lê.

```text
Wide 16:9 landscape cinematic frame. a room frozen in crystal, shards of glowing crystal spreading across the walls, a girl standing in shock. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Hóa ra cuốn sách chứa một loại phép bị cấm. Và người lạ đội mũ rộng vành năm xưa có lẽ đã cố tình trao nó cho…

```text
Wide 16:9 landscape cinematic frame. an old picture book lying open on the floor, its pages glowing a sinister purple. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Qifrey xuất hiện kịp lúc. Theo luật, Coco đã thấy bí mật nên phải bị xóa ký ức. Nhưng anh chọn cách khác: nhậ…

```text
Wide 16:9 landscape cinematic frame. a cloaked figure extending a hand to a crying girl amid crystal shards, soft light behind them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Từ đó, Coco có hai mục tiêu: học thành phù thủy, và tìm cách cứu mẹ mình khỏi lớp pha lê.

```text
Wide 16:9 landscape cinematic frame. a girl walking away from her village with a small bag, a crystal-shaped light in her hand, sunrise ahead. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đây là tất cả spoiler của video hôm nay. Phần còn lại, mình chỉ nói về luật phép thuật và vì sao bộ này đáng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot zipping its beak shut with a tiny zipper, winking. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Luật số 1: Ký hiệu trung tâm

Lời: Giờ tới phần mình thích nhất. Mỗi phép thuật trong Witch Hat Atelier là một hình tròn gồm ba lớp. Lớp đầu tiê…

```text
Wide 16:9 landscape cinematic frame. a large glowing circle diagram with three concentric layers highlighted one by one. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Ký hiệu trung tâm quyết định phép thuật thuộc loại nào. Nó giống như danh từ trong một câu: nói cho thế giới…

```text
Wide 16:9 landscape cinematic frame. a single ornate symbol glowing in the center of an empty circle. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Các phép thường được chia thành năm nhóm lớn theo ký hiệu này: lửa, nước, đất, gió và ánh sáng.

```text
Wide 16:9 landscape cinematic frame. five glowing symbols arranged in a ring: a flame, a droplet, a stone, a swirl of wind, and a star. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Vẽ ký hiệu nước ở giữa thì phép gọi ra nước. Đổi sang ký hiệu lửa thì cùng một vòng tròn đó sẽ thắp lên ngọn…

```text
Wide 16:9 landscape cinematic frame. a split image: the same circle producing water on the left and fire on the right. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy cách này rất giống học chữ. Trước khi viết được câu, bạn phải thuộc bảng chữ cái đã.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a chalkboard of five simple symbols like an alphabet. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Luật số 2: Các dấu điều khiển

Lời: Lớp thứ hai nằm quanh ký hiệu trung tâm, gồm những dấu nhỏ. Nếu ký hiệu trung tâm là danh từ, thì các dấu là…

```text
Wide 16:9 landscape cinematic frame. small glowing marks arranged in a ring around a central symbol, each labeled with a tiny arrow. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Các dấu quyết định phép đi theo hướng nào, mạnh bao nhiêu, kéo dài bao lâu, và có hình dạng ra sao.

```text
Wide 16:9 landscape cinematic frame. four small icons appearing one by one: an arrow, a gauge, an hourglass, and a geometric shape. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Cùng là phép nước, thêm dấu này thì nước phun thẳng lên trời. Đổi dấu khác thì nước chảy thành một dòng suối…

```text
Wide 16:9 landscape cinematic frame. two circles side by side: one spraying water straight up, the other letting a gentle stream flow along the ground. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Vì vậy phù thủy giỏi không phải người biết nhiều ký hiệu nhất, mà là người biết kết hợp các dấu khéo léo nhất.

```text
Wide 16:9 landscape cinematic frame. a skilled hand arranging small glowing marks like puzzle pieces around a circle. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Đây cũng là chỗ bộ truyện cho nhân vật cơ hội sáng tạo. Không có phép nào cố định, chỉ có những cách vẽ khác…

```text
Wide 16:9 landscape cinematic frame. a desk covered in dozens of different circle sketches, some crossed out, some glowing. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Luật số 3: Vòng tròn và mực

Lời: Lớp thứ ba là vòng tròn bao ngoài. Và đây là luật quan trọng nhất: vòng tròn phải khép kín. Hở một chút thôi,…

```text
Wide 16:9 landscape cinematic frame. a glowing circle with a tiny gap, sparks fizzling out at the break. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nghe thì đơn giản, nhưng hãy thử tưởng tượng vẽ một vòng tròn hoàn hảo khi đang rơi từ trên trời xuống, hoặc…

```text
Wide 16:9 landscape cinematic frame. a figure falling through the sky with a pen, desperately drawing a circle on a scrap of paper. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Thứ hai là mực. Phép chỉ hoạt động khi được vẽ bằng một loại mực đặc biệt, không phải mực thường.

```text
Wide 16:9 landscape cinematic frame. a row of small ink bottles glowing faintly silver on a wooden shelf. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Theo các nguồn giới thiệu, loại mực này được làm với sự giúp đỡ của một loại cây bạc rất đặc biệt. Vì vậy mực…

```text
Wide 16:9 landscape cinematic frame. a silver-leafed tree glowing in a misty grove, drops of shining sap falling into a bottle. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chỉ cần hai điều kiện là mực và vòng tròn khép kín, mà cả một thế giới phải giữ bí mật. Vì chún…

```text
Wide 16:9 landscape cinematic frame. the owl mascot guarding a tiny ink bottle with both wings, looking around suspiciously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Những luật nâng cao

Lời: Khi đã hiểu ba lớp, ta có thêm vài luật nâng cao rất thú vị mà bộ truyện dùng để tạo ra những pha xử lý thông…

```text
Wide 16:9 landscape cinematic frame. a notebook page titled with a small star, advanced diagrams sketched in the margins. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Luật đảo chiều: lật ngược hướng của một dấu thì phép cũng đảo ngược. Phép đẩy thành phép kéo, phép bay lên th…

```text
Wide 16:9 landscape cinematic frame. two mirrored circles, one pushing a leaf away and the other pulling it in. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Luật triệt tiêu: hai phép giống hệt nhau nhưng có dấu ngược chiều có thể xóa nhau, giống như hai lực bằng nha…

```text
Wide 16:9 landscape cinematic frame. two opposing glowing circles colliding and dissolving into sparkles. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Luật lồng vòng: một phép có thể được bao trong một vòng tròn khác, để kết hợp hiệu ứng của hai phép, kể cả kh…

```text
Wide 16:9 landscape cinematic frame. a small glowing circle nested inside a larger circle, two different effects merging. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Với những luật này, phép thuật trở thành một câu đố. Người thắng không phải người mạnh nhất, mà là người nghĩ…

```text
Wide 16:9 landscape cinematic frame. a figure solving a glowing puzzle of circles while a larger opponent looks confused. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Ma thuật cấm

Lời: Nếu có luật, thì có những thứ bị cấm. Trong thế giới này, một số loại phép bị các phù thủy cấm tuyệt đối.

```text
Wide 16:9 landscape cinematic frame. a heavy iron gate covered in chains, glowing forbidden symbols behind it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ví dụ nổi bật nhất là vẽ phép trực tiếp lên cơ thể sống. Nó có thể tạo ra sức mạnh lớn, nhưng cái giá thường…

```text
Wide 16:9 landscape cinematic frame. a warning sign showing a crossed-out hand with glowing lines drawn on it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Những người vẫn lén dùng ma thuật cấm được gọi chung là nhóm đội mũ rộng vành. Họ là mối nguy lớn nhất trong…

```text
Wide 16:9 landscape cinematic frame. shadowy figures in wide-brimmed hats standing on a cliff, faces hidden, purple light around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Và để giữ luật, còn có những người chuyên truy bắt kẻ vi phạm. Giữa hai phía đó là những học trò như Coco, cò…

```text
Wide 16:9 landscape cinematic frame. a young girl standing between a line of armored guards and shadowy hatted figures. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Điều thú vị là ma thuật cấm không phải lúc nào cũng xấu về kết quả. Nó có thể chữa lành hoặc giúp người, và c…

```text
Wide 16:9 landscape cinematic frame. a glowing healing light over a wounded hand, but the light has a faint purple edge. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để phần này ngắn thôi, vì càng nói càng spoiler. Chỉ cần biết: ma thuật cấm là sợi dây xuyên suốt cả bộ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quickly closing a book that is leaking purple light. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Xưởng vẽ và các bạn học

Lời: Qifrey đưa Coco về xưởng của mình, nơi anh đang dạy ba học trò khác. Mỗi người là một kiểu tính cách rất khác…

```text
Wide 16:9 landscape cinematic frame. a cozy fantasy atelier with tall windows, drawing tables, hanging herbs and floating lanterns. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Agott là cô gái nghiêm khắc, xuất thân từ một gia đình phù thủy danh giá. Ban đầu cô rất khó chịu với một ngư…

```text
Wide 16:9 landscape cinematic frame. a stern apprentice with arms crossed standing by a window, a precise circle drawn perfectly on her desk. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Tetia vui vẻ, hay cười và muốn dùng phép để làm mọi người hạnh phúc. Richeh thì thích vẽ theo cách riêng, khô…

```text
Wide 16:9 landscape cinematic frame. two apprentices: one cheerful girl waving happily, another lazily doodling tiny creatures on paper. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Qifrey là người thầy dịu dàng, luôn cho học trò tự tìm câu trả lời. Nhưng có vẻ anh cũng mang những bí mật ri…

```text
Wide 16:9 landscape cinematic frame. a gentle teacher smiling while his shadow on the wall looks slightly different, mysterious. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bộ này giống một câu chuyện về trường học hơn là một câu chuyện chiến đấu. Mỗi học trò học cách…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting at a tiny desk among larger drawing tables, raising a wing like a student. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Kaku thử vẽ một phép · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ tới phần thực hành! Kaku sẽ thử thiết kế một phép theo đúng ba lớp. Lưu ý đây là phép Kaku tự nghĩ ra, kh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot spreading a large sheet of paper on a desk, pen in wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Mục tiêu: một phép tưới cây nhẹ nhàng cho vườn. Bước một, chọn ký hiệu trung tâm là nước.

```text
Wide 16:9 landscape cinematic frame. a hand-drawn circle with a water droplet symbol in the center, notes around it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Bước hai, thêm dấu hướng lên để nước bay lên, rồi thêm dấu cường độ nhỏ để nó không phun như vòi cứu hỏa.

```text
Wide 16:9 landscape cinematic frame. small arrow and gauge marks added around the droplet symbol, a note saying gentle. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Bước ba, thêm dấu hình dạng để nước tỏa ra như cơn mưa phùn, thay vì một dòng thẳng.

```text
Wide 16:9 landscape cinematic frame. a gentle fan-shaped mark added, a sketch of drizzle falling over flowers. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Bước cuối, khép kín vòng tròn. Nếu mọi thứ đúng, khu vườn sẽ có một cơn mưa nhỏ riêng.

```text
Wide 16:9 landscape cinematic frame. a completed glowing circle on the ground of a garden, light drizzle falling over blooming flowers. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhưng nếu Kaku lỡ tay vẽ ngược dấu hướng thì sao? Nước sẽ bị hút xuống đất, và cả vườn khô héo. Một nét vẽ, h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring in horror at a dried-up garden, its pen upside down. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Đó chính là tinh thần của bộ truyện: phép thuật là một nghề thủ công, tỉ mỉ và đầy trách nhiệm.

```text
Wide 16:9 landscape cinematic frame. a craftsman's desk with rulers, compasses, ink and a perfect glowing circle. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Vì sao bạn nên xem?

Lời: Tóm gọn lại, có bốn lý do Kaku nghĩ bạn nên cho Witch Hat Atelier một cơ hội.

```text
Wide 16:9 landscape cinematic frame. four glowing cards laid out on a table, each with a simple icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Lý do một: hình ảnh. Anime cố giữ cảm giác tranh minh họa của bản manga, với màu sắc dịu nhẹ như sách truyện…

```text
Wide 16:9 landscape cinematic frame. a painterly fantasy forest with soft watercolor tones and fine ink outlines. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Lý do hai: hệ thống phép thuật có luật rõ ràng. Bạn có thể tự đoán trước một phép sẽ hoạt động thế nào, và th…

```text
Wide 16:9 landscape cinematic frame. a viewer silhouette smiling as a glowing puzzle of circles clicks into place. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Lý do ba: câu chuyện về sự sáng tạo. Coco không phải thiên tài, nhưng cô nhìn phép thuật theo cách của một ng…

```text
Wide 16:9 landscape cinematic frame. a young apprentice drawing an unusual circle while others watch in surprise. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Lý do bốn: bí ẩn. Người đội mũ rộng vành là ai, vì sao họ chọn Coco, và người thầy đang giấu điều gì? Những c…

```text
Wide 16:9 landscape cinematic frame. a mysterious hat floating in darkness with three question marks glowing around it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nếu bạn thích phiêu lưu nhẹ nhàng hơn là đánh nhau dồn dập, đây gần như chắc chắn là bộ dành cho bạn.

```text
Wide 16:9 landscape cinematic frame. a cozy reading nook with a window overlooking a magical valley at sunset. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Góc nhìn của Kaku: khi phép thuật ai cũng học được · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi kết, Kaku muốn chia sẻ một điều khiến bộ này khác hầu hết các bộ fantasy khác.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of books by candlelight, thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Trong nhiều truyện, sức mạnh là bẩm sinh: bạn sinh ra có tài năng hoặc không. Ở đây, sức mạnh là kiến thức. A…

```text
Wide 16:9 landscape cinematic frame. a split image: a glowing figure born with light on one side, a student studying books on the other. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và vì ai cũng dùng được, nên câu hỏi lớn không còn là ai mạnh nhất, mà là ai được phép biết. Đó là câu hỏi về…

```text
Wide 16:9 landscape cinematic frame. a single key hanging over a crowd of reaching hands, soft dramatic lighting. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Các phù thủy giấu phép thuật để bảo vệ thế giới. Nhưng chính bí mật đó cũng khiến người thường phụ thuộc vào…

```text
Wide 16:9 landscape cinematic frame. a high tower of witches above a village, the villagers looking up from far below. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku không nghĩ bộ truyện đưa ra câu trả lời dễ dàng. Và chính việc nó không trả lời vội là lý do nó đáng để…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at two paths in a forest, one bright and one shadowed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Câu hỏi người mới hay hỏi

Lời: Trước khi chốt lộ trình, Kaku gom vài câu hỏi mà người mới hay thắc mắc khi nghe về bộ này.

```text
Wide 16:9 landscape cinematic frame. a wooden board pinned with handwritten question cards, soft lantern light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hỏi: bộ này có hợp với trẻ em không? Đáp: phần lớn nhẹ nhàng, nhưng có vài cảnh khá đáng sợ và căng thẳng, nê…

```text
Wide 16:9 landscape cinematic frame. a family silhouette watching a glowing screen together on a sofa, a small shadowy creature on screen. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Hỏi: không thích truyện nhịp chậm thì sao? Đáp: hãy thử đúng hai tập đầu. Nhịp của bộ này không đổi nhiều về…

```text
Wide 16:9 landscape cinematic frame. an hourglass beside two glowing episode icons, a snail and a rabbit icon on either side. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hỏi: có cần biết gì về phép thuật trước không? Đáp: không. Bạn học luật cùng lúc với Coco, và đó chính là niề…

```text
Wide 16:9 landscape cinematic frame. a beginner student and a small owl side by side reading the same glowing book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Hỏi: có giống Frieren không? Đáp: giống ở không khí yên bình và sự tôn trọng dành cho phép thuật, nhưng Witch…

```text
Wide 16:9 landscape cinematic frame. two books side by side, one with a pen and ink cover, the other with a clock and flower cover. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hỏi: nhân vật nào dễ thương nhất? Đáp: Kaku không dám trả lời, vì sợ bị cả xưởng vẽ giận. Bạn trả lời giúp Ka…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding behind a stack of sketchbooks, peeking out nervously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và câu hỏi cuối: có nên đọc manga trước khi xem anime không? Kaku nghĩ nên xem anime trước, để lần đầu nhìn t…

```text
Wide 16:9 landscape cinematic frame. a glowing screen and an open manga volume side by side on a desk, ink bottle between them. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · Lộ trình xem cho người mới

Lời: Nếu bạn muốn bắt đầu, đây là lộ trình Kaku gợi ý.

```text
Wide 16:9 landscape cinematic frame. a winding path map with small flags leading toward a castle. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Bước một: xem hai tập đầu của anime. Chúng ra mắt cùng lúc, đủ để bạn biết mình có hợp với nhịp chậm và nét v…

```text
Wide 16:9 landscape cinematic frame. a small screen showing two glowing episode icons side by side. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Bước hai: nếu thích, hãy xem hết mùa một, rồi đọc manga để đi tiếp, vì bản gốc vẫn đang được phát hành.

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes next to a glowing television screen. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Bước ba, tùy chọn: xem lại video này sau khi đã xem vài tập. Bạn sẽ thấy các luật ba lớp xuất hiện trong gần…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing circle diagram next to a small screen. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Và hãy nhớ, chỉ xem anime qua các nền tảng có bản quyền, để ủng hộ những người đã làm ra nó.

```text
Wide 16:9 landscape cinematic frame. a heart-shaped glow over a small film reel and a pen. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · Kết

Lời: Tóm lại: trong Witch Hat Atelier, phép thuật là hình tròn ba lớp gồm ký hiệu trung tâm, các dấu điều khiển và…

```text
Wide 16:9 landscape cinematic frame. a summary diagram of a three-layer glowing circle with labels. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93

Lời: Ai cũng học được, nên cả thế giới phải giữ bí mật. Và một cô bé con nhà thợ may đã vô tình mở cánh cửa đó.

```text
Wide 16:9 landscape cinematic frame. a young girl standing before a giant open door filled with swirling glowing circles. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được vẽ một phép trong thế giới này, bạn sẽ vẽ phép gì? Hãy mô tả ký hiệu và các dấu của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank circle template and a pen out toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95

Lời: Video tới sẽ đổi hẳn không khí: Kaku sẽ mang thước và máy tính ra để kiểm tra xem kỹ thuật Xoay trong JoJo St…

```text
Wide 16:9 landscape cinematic frame. a golden spiral drawn over a spinning steel ball, a ruler and calculator beside it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh để không bỏ lỡ. Kaku cất bút đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot capping its pen and waving goodbye from a sunlit atelier window. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Bộ truyện này là gì?

Khoảng 122 giây · cảnh s01–s12 · 1581 ký tự

**Gemini**

```text
Video này gần như không có spoiler: mình chỉ nói về thế giới, luật phép thuật và những tập đầu tiên của mùa một. Nếu bạn chưa xem, đây đúng là video dành cho bạn.

<short pause> Hãy tưởng tượng một thế giới mà phép thuật không phải thứ bạn sinh ra đã có. Nó là thứ bạn vẽ ra, bằng một cây bút và một lọ mực.

<short pause> Chỉ cần vẽ đúng, một vòng tròn trên mặt đất có thể gọi nước, thắp lửa, hay nâng cả một con người bay lên trời.

<short pause> Đó là Witch Hat Atelier, bộ anime được gọi là ứng viên anime của năm 2026. Và hôm nay mình sẽ dẫn bạn đi qua cánh cửa của nó trong khoảng mười lăm phút.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ không phải sổ ghi chép nữa, mà là một cuốn sổ vẽ phép thuật.

<short pause> Cuối video, Kaku sẽ thử tự vẽ một phép theo đúng luật của thế giới này, và gợi ý cho bạn nên bắt đầu xem từ đâu.

<short pause> Witch Hat Atelier là manga của nữ tác giả Shirahama Kamome, bắt đầu đăng từ năm 2016. Tên tiếng Nhật có nghĩa là Xưởng vẽ của chiếc mũ nhọn.

<short pause> Điều khiến bộ truyện nổi tiếng trước tiên là nét vẽ. Mỗi trang giống như tranh minh họa trong sách truyện cổ, với từng đường mực tỉ mỉ.

<short pause> Bộ truyện đã nhận nhiều giải thưởng truyện tranh quốc tế, và được độc giả phương Tây yêu thích không kém độc giả Nhật.

<short pause> Bản anime do studio Bug Films thực hiện, ra mắt ngày 6 tháng 4 năm 2026 với hai tập liền, và nhanh chóng được giới phê bình khen ngợi.

<short pause> Trước khi phát sóng, nhiều người lo lắng vì studio này từng gặp khó khăn về tiến độ với bộ trước. <short pause> Nhưng những tập đầu đã làm phần lớn người xem yên tâm.

<short pause> Kaku ghi chú: đây là bộ fantasy nhẹ nhàng, không phải kiểu đánh nhau liên tục. Nếu bạn thích Frieren, rất có thể bạn sẽ thích bộ này.
```

**ElevenLabs**

```text
Video này gần như không có spoiler: mình chỉ nói về thế giới, luật phép thuật và những tập đầu tiên của mùa một. Nếu bạn chưa xem, đây đúng là video dành cho bạn.

[pause] Hãy tưởng tượng một thế giới mà phép thuật không phải thứ bạn sinh ra đã có. Nó là thứ bạn vẽ ra, bằng một cây bút và một lọ mực.

[pause] Chỉ cần vẽ đúng, một vòng tròn trên mặt đất có thể gọi nước, thắp lửa, hay nâng cả một con người bay lên trời.

[pause] Đó là Witch Hat Atelier, bộ anime được gọi là ứng viên anime của năm 2026. Và hôm nay mình sẽ dẫn bạn đi qua cánh cửa của nó trong khoảng mười lăm phút.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ không phải sổ ghi chép nữa, mà là một cuốn sổ vẽ phép thuật.

[pause] Cuối video, Kaku sẽ thử tự vẽ một phép theo đúng luật của thế giới này, và gợi ý cho bạn nên bắt đầu xem từ đâu.

[pause] Witch Hat Atelier là manga của nữ tác giả Shirahama Kamome, bắt đầu đăng từ năm 2016. Tên tiếng Nhật có nghĩa là Xưởng vẽ của chiếc mũ nhọn.

[pause] Điều khiến bộ truyện nổi tiếng trước tiên là nét vẽ. Mỗi trang giống như tranh minh họa trong sách truyện cổ, với từng đường mực tỉ mỉ.

[pause] Bộ truyện đã nhận nhiều giải thưởng truyện tranh quốc tế, và được độc giả phương Tây yêu thích không kém độc giả Nhật.

[pause] Bản anime do studio Bug Films thực hiện, ra mắt ngày 6 tháng 4 năm 2026 với hai tập liền, và nhanh chóng được giới phê bình khen ngợi.

[pause] Trước khi phát sóng, nhiều người lo lắng vì studio này từng gặp khó khăn về tiến độ với bộ trước. [pause] Nhưng những tập đầu đã làm phần lớn người xem yên tâm.

[pause] Kaku ghi chú: đây là bộ fantasy nhẹ nhàng, không phải kiểu đánh nhau liên tục. Nếu bạn thích Frieren, rất có thể bạn sẽ thích bộ này.
```

### c02 · Thế giới của những bí mật / Cô bé muốn trở thành phù thủy

Khoảng 116 giây · cảnh s13–s24 · 1504 ký tự

**Gemini**

```text
Trong thế giới này, người thường tin rằng phù thủy là những người sinh ra đã có phép thuật. Họ nghĩ đó là tài năng bẩm sinh, không ai học được.

<short pause> Nhưng đó là một lời nói dối được giữ gìn cẩn thận. Sự thật là ai cũng có thể dùng phép, nếu biết cách vẽ và có đúng loại mực.

<short pause> Vì sao phải giấu? Trong quá khứ, phép thuật từng bị dùng vào chiến tranh và gây ra thảm họa. Các phù thủy quyết định rằng người thường không được biết cách phép thuật hoạt động.

<short pause> Họ lập ra một hiệp ước. Từ đó, phép thuật chỉ được truyền dạy trong giới phù thủy, và mọi hiểu biết về nó bị giấu khỏi thế giới bên ngoài.

<short pause> Và nếu một người thường vô tình nhìn thấy cách phép được vẽ ra? Theo luật, ký ức đó phải bị xóa.

<short pause> Đây là nền móng của cả câu chuyện: một thế giới đẹp như tranh, nhưng được xây trên một bí mật mà ai biết được thì đều phải trả giá.

<short pause> Nhân vật chính là Coco, một cô bé sống ở làng quê, con gái của một thợ may. Từ nhỏ, cô đã mơ được làm phù thủy.

<short pause> Nhưng vì tin rằng phép thuật là bẩm sinh, Coco nghĩ giấc mơ đó là không thể. Cô không có phép, nên chỉ biết đứng nhìn.

<short pause> Khi còn nhỏ, Coco từng nhận được một cuốn sách tranh về phép thuật và một cây bút từ một người lạ đội mũ rộng vành ở lễ hội.

<short pause> Một ngày, một phù thủy tên là Qifrey ghé qua tiệm may nhà cô. Coco lén nhìn thấy điều không ai được nhìn: anh ta vẽ phép thuật bằng bút mực.

<short pause> Trong đầu cô bé bừng sáng một ý nghĩ: nếu phép thuật được vẽ ra, thì mình cũng có thể vẽ.

<short pause> <laugh> Kaku ghi chú: đây là khoảnh khắc mở đầu rất hay, vì nó biến một giấc mơ không thể thành một thứ có thể học được.
```

**ElevenLabs**

```text
Trong thế giới này, người thường tin rằng phù thủy là những người sinh ra đã có phép thuật. Họ nghĩ đó là tài năng bẩm sinh, không ai học được.

[pause] Nhưng đó là một lời nói dối được giữ gìn cẩn thận. Sự thật là ai cũng có thể dùng phép, nếu biết cách vẽ và có đúng loại mực.

[pause] [curious] Vì sao phải giấu? Trong quá khứ, phép thuật từng bị dùng vào chiến tranh và gây ra thảm họa. Các phù thủy quyết định rằng người thường không được biết cách phép thuật hoạt động.

[pause] Họ lập ra một hiệp ước. Từ đó, phép thuật chỉ được truyền dạy trong giới phù thủy, và mọi hiểu biết về nó bị giấu khỏi thế giới bên ngoài.

[pause] Và nếu một người thường vô tình nhìn thấy cách phép được vẽ ra? Theo luật, ký ức đó phải bị xóa.

[pause] Đây là nền móng của cả câu chuyện: một thế giới đẹp như tranh, nhưng được xây trên một bí mật mà ai biết được thì đều phải trả giá.

[pause] Nhân vật chính là Coco, một cô bé sống ở làng quê, con gái của một thợ may. Từ nhỏ, cô đã mơ được làm phù thủy.

[pause] Nhưng vì tin rằng phép thuật là bẩm sinh, Coco nghĩ giấc mơ đó là không thể. Cô không có phép, nên chỉ biết đứng nhìn.

[pause] Khi còn nhỏ, Coco từng nhận được một cuốn sách tranh về phép thuật và một cây bút từ một người lạ đội mũ rộng vành ở lễ hội.

[pause] Một ngày, một phù thủy tên là Qifrey ghé qua tiệm may nhà cô. Coco lén nhìn thấy điều không ai được nhìn: anh ta vẽ phép thuật bằng bút mực.

[pause] Trong đầu cô bé bừng sáng một ý nghĩ: nếu phép thuật được vẽ ra, thì mình cũng có thể vẽ.

[pause] [chuckles] Kaku ghi chú: đây là khoảnh khắc mở đầu rất hay, vì nó biến một giấc mơ không thể thành một thứ có thể học được.
```

### c03 · Cái giá của một nét vẽ / Luật số 1: Ký hiệu trung tâm / Luật số 2: Các dấu điều khiển

Khoảng 140 giây · cảnh s25–s40 · 1815 ký tự

**Gemini**

```text
Coco mở cuốn sách tranh cũ ra, chép lại một vòng tròn trong đó lên sàn nhà. Cô không biết đó là loại phép gì.

<short pause> Phép được kích hoạt, và hậu quả vượt quá sức tưởng tượng: người mẹ của Coco bị bao phủ trong pha lê.

<short pause> Hóa ra cuốn sách chứa một loại phép bị cấm. Và người lạ đội mũ rộng vành năm xưa có lẽ đã cố tình trao nó cho cô.

<short pause> Qifrey xuất hiện kịp lúc. Theo luật, Coco đã thấy bí mật nên phải bị xóa ký ức. <short pause> Nhưng anh chọn cách khác: nhận cô làm học trò.

<short pause> Từ đó, Coco có hai mục tiêu: học thành phù thủy, và tìm cách cứu mẹ mình khỏi lớp pha lê.

<short pause> Đây là tất cả spoiler của video hôm nay. Phần còn lại, mình chỉ nói về luật phép thuật và vì sao bộ này đáng xem.

<short pause> Giờ tới phần mình thích nhất. Mỗi phép thuật trong Witch Hat Atelier là một hình tròn gồm ba lớp. Lớp đầu tiên nằm ở chính giữa, gọi là ký hiệu trung tâm.

<short pause> Ký hiệu trung tâm quyết định phép thuật thuộc loại nào. Nó giống như danh từ trong một câu: nói cho thế giới biết bạn đang gọi thứ gì.

<short pause> Các phép thường được chia thành năm nhóm lớn theo ký hiệu này: lửa, nước, đất, gió và ánh sáng.

<short pause> Vẽ ký hiệu nước ở giữa thì phép gọi ra nước. Đổi sang ký hiệu lửa thì cùng một vòng tròn đó sẽ thắp lên ngọn lửa.

<short pause> <laugh> Kaku thấy cách này rất giống học chữ. Trước khi viết được câu, bạn phải thuộc bảng chữ cái đã.

<short pause> Lớp thứ hai nằm quanh ký hiệu trung tâm, gồm những dấu nhỏ. Nếu ký hiệu trung tâm là danh từ, thì các dấu là động từ và trạng từ.

<short pause> Các dấu quyết định phép đi theo hướng nào, mạnh bao nhiêu, kéo dài bao lâu, và có hình dạng ra sao.

<short pause> Cùng là phép nước, thêm dấu này thì nước phun thẳng lên trời. Đổi dấu khác thì nước chảy thành một dòng suối nhỏ dưới chân.

<short pause> Vì vậy phù thủy giỏi không phải người biết nhiều ký hiệu nhất, mà là người biết kết hợp các dấu khéo léo nhất.

<short pause> Đây cũng là chỗ bộ truyện cho nhân vật cơ hội sáng tạo. Không có phép nào cố định, chỉ có những cách vẽ khác nhau.
```

**ElevenLabs**

```text
Coco mở cuốn sách tranh cũ ra, chép lại một vòng tròn trong đó lên sàn nhà. Cô không biết đó là loại phép gì.

[pause] Phép được kích hoạt, và hậu quả vượt quá sức tưởng tượng: người mẹ của Coco bị bao phủ trong pha lê.

[pause] Hóa ra cuốn sách chứa một loại phép bị cấm. Và người lạ đội mũ rộng vành năm xưa có lẽ đã cố tình trao nó cho cô.

[pause] Qifrey xuất hiện kịp lúc. Theo luật, Coco đã thấy bí mật nên phải bị xóa ký ức. [pause] Nhưng anh chọn cách khác: nhận cô làm học trò.

[pause] Từ đó, Coco có hai mục tiêu: học thành phù thủy, và tìm cách cứu mẹ mình khỏi lớp pha lê.

[pause] Đây là tất cả spoiler của video hôm nay. Phần còn lại, mình chỉ nói về luật phép thuật và vì sao bộ này đáng xem.

[pause] Giờ tới phần mình thích nhất. Mỗi phép thuật trong Witch Hat Atelier là một hình tròn gồm ba lớp. Lớp đầu tiên nằm ở chính giữa, gọi là ký hiệu trung tâm.

[pause] Ký hiệu trung tâm quyết định phép thuật thuộc loại nào. Nó giống như danh từ trong một câu: nói cho thế giới biết bạn đang gọi thứ gì.

[pause] Các phép thường được chia thành năm nhóm lớn theo ký hiệu này: lửa, nước, đất, gió và ánh sáng.

[pause] Vẽ ký hiệu nước ở giữa thì phép gọi ra nước. Đổi sang ký hiệu lửa thì cùng một vòng tròn đó sẽ thắp lên ngọn lửa.

[pause] [chuckles] Kaku thấy cách này rất giống học chữ. Trước khi viết được câu, bạn phải thuộc bảng chữ cái đã.

[pause] Lớp thứ hai nằm quanh ký hiệu trung tâm, gồm những dấu nhỏ. Nếu ký hiệu trung tâm là danh từ, thì các dấu là động từ và trạng từ.

[pause] Các dấu quyết định phép đi theo hướng nào, mạnh bao nhiêu, kéo dài bao lâu, và có hình dạng ra sao.

[pause] Cùng là phép nước, thêm dấu này thì nước phun thẳng lên trời. Đổi dấu khác thì nước chảy thành một dòng suối nhỏ dưới chân.

[pause] Vì vậy phù thủy giỏi không phải người biết nhiều ký hiệu nhất, mà là người biết kết hợp các dấu khéo léo nhất.

[pause] Đây cũng là chỗ bộ truyện cho nhân vật cơ hội sáng tạo. Không có phép nào cố định, chỉ có những cách vẽ khác nhau.
```

### c04 · Luật số 3: Vòng tròn và mực / Những luật nâng cao

Khoảng 101 giây · cảnh s41–s50 · 1314 ký tự

**Gemini**

```text
Lớp thứ ba là vòng tròn bao ngoài. Và đây là luật quan trọng nhất: vòng tròn phải khép kín. Hở một chút thôi, phép sẽ không xuất hiện.

<short pause> Nghe thì đơn giản, nhưng hãy thử tưởng tượng vẽ một vòng tròn hoàn hảo khi đang rơi từ trên trời xuống, hoặc khi quái vật đang lao tới.

<short pause> Thứ hai là mực. Phép chỉ hoạt động khi được vẽ bằng một loại mực đặc biệt, không phải mực thường.

<short pause> Theo các nguồn giới thiệu, loại mực này được làm với sự giúp đỡ của một loại cây bạc rất đặc biệt. Vì vậy mực cũng là một thứ được kiểm soát chặt chẽ.

<short pause> <laugh> Kaku ghi chú: chỉ cần hai điều kiện là mực và vòng tròn khép kín, mà cả một thế giới phải giữ bí mật. Vì chúng quá dễ để người khác bắt chước.

<short pause> Khi đã hiểu ba lớp, ta có thêm vài luật nâng cao rất thú vị mà bộ truyện dùng để tạo ra những pha xử lý thông minh.

<short pause> Luật đảo chiều: lật ngược hướng của một dấu thì phép cũng đảo ngược. Phép đẩy thành phép kéo, phép bay lên thành phép rơi xuống.

<short pause> Luật triệt tiêu: hai phép giống hệt nhau nhưng có dấu ngược chiều có thể xóa nhau, giống như hai lực bằng nhau đẩy từ hai phía.

<short pause> Luật lồng vòng: một phép có thể được bao trong một vòng tròn khác, để kết hợp hiệu ứng của hai phép, kể cả khi chúng không được vẽ trên cùng một vật.

<short pause> Với những luật này, phép thuật trở thành một câu đố. Người thắng không phải người mạnh nhất, mà là người nghĩ ra cách vẽ thông minh nhất.
```

**ElevenLabs**

```text
Lớp thứ ba là vòng tròn bao ngoài. Và đây là luật quan trọng nhất: vòng tròn phải khép kín. Hở một chút thôi, phép sẽ không xuất hiện.

[pause] Nghe thì đơn giản, nhưng hãy thử tưởng tượng vẽ một vòng tròn hoàn hảo khi đang rơi từ trên trời xuống, hoặc khi quái vật đang lao tới.

[pause] Thứ hai là mực. Phép chỉ hoạt động khi được vẽ bằng một loại mực đặc biệt, không phải mực thường.

[pause] Theo các nguồn giới thiệu, loại mực này được làm với sự giúp đỡ của một loại cây bạc rất đặc biệt. Vì vậy mực cũng là một thứ được kiểm soát chặt chẽ.

[pause] [chuckles] Kaku ghi chú: chỉ cần hai điều kiện là mực và vòng tròn khép kín, mà cả một thế giới phải giữ bí mật. Vì chúng quá dễ để người khác bắt chước.

[pause] Khi đã hiểu ba lớp, ta có thêm vài luật nâng cao rất thú vị mà bộ truyện dùng để tạo ra những pha xử lý thông minh.

[pause] Luật đảo chiều: lật ngược hướng của một dấu thì phép cũng đảo ngược. Phép đẩy thành phép kéo, phép bay lên thành phép rơi xuống.

[pause] Luật triệt tiêu: hai phép giống hệt nhau nhưng có dấu ngược chiều có thể xóa nhau, giống như hai lực bằng nhau đẩy từ hai phía.

[pause] Luật lồng vòng: một phép có thể được bao trong một vòng tròn khác, để kết hợp hiệu ứng của hai phép, kể cả khi chúng không được vẽ trên cùng một vật.

[pause] Với những luật này, phép thuật trở thành một câu đố. Người thắng không phải người mạnh nhất, mà là người nghĩ ra cách vẽ thông minh nhất.
```

### c05 · Ma thuật cấm / Xưởng vẽ và các bạn học

Khoảng 108 giây · cảnh s51–s61 · 1404 ký tự

**Gemini**

```text
Nếu có luật, thì có những thứ bị cấm. Trong thế giới này, một số loại phép bị các phù thủy cấm tuyệt đối.

<short pause> Ví dụ nổi bật nhất là vẽ phép trực tiếp lên cơ thể sống. Nó có thể tạo ra sức mạnh lớn, nhưng cái giá thường là không thể đảo ngược.

<short pause> Những người vẫn lén dùng ma thuật cấm được gọi chung là nhóm đội mũ rộng vành. Họ là mối nguy lớn nhất trong câu chuyện.

<short pause> Và để giữ luật, còn có những người chuyên truy bắt kẻ vi phạm. Giữa hai phía đó là những học trò như Coco, còn chưa hiểu hết đúng sai.

<short pause> Điều thú vị là ma thuật cấm không phải lúc nào cũng xấu về kết quả. Nó có thể chữa lành hoặc giúp người, và chính điều đó khiến ranh giới đúng sai trở nên mờ.

<short pause> <laugh> Kaku để phần này ngắn thôi, vì càng nói càng spoiler. Chỉ cần biết: ma thuật cấm là sợi dây xuyên suốt cả bộ truyện.

<short pause> Qifrey đưa Coco về xưởng của mình, nơi anh đang dạy ba học trò khác. Mỗi người là một kiểu tính cách rất khác nhau.

<short pause> Agott là cô gái nghiêm khắc, xuất thân từ một gia đình phù thủy danh giá. Ban đầu cô rất khó chịu với một người ngoài như Coco.

<short pause> Tetia vui vẻ, hay cười và muốn dùng phép để làm mọi người hạnh phúc. Richeh thì thích vẽ theo cách riêng, không muốn làm theo khuôn mẫu.

<short pause> Qifrey là người thầy dịu dàng, luôn cho học trò tự tìm câu trả lời. <short pause> Nhưng có vẻ anh cũng mang những bí mật riêng của mình.

<short pause> Kaku ghi chú: bộ này giống một câu chuyện về trường học hơn là một câu chuyện chiến đấu. Mỗi học trò học cách vẽ, và học cả cách làm người.
```

**ElevenLabs**

```text
Nếu có luật, thì có những thứ bị cấm. Trong thế giới này, một số loại phép bị các phù thủy cấm tuyệt đối.

[pause] Ví dụ nổi bật nhất là vẽ phép trực tiếp lên cơ thể sống. Nó có thể tạo ra sức mạnh lớn, nhưng cái giá thường là không thể đảo ngược.

[pause] Những người vẫn lén dùng ma thuật cấm được gọi chung là nhóm đội mũ rộng vành. Họ là mối nguy lớn nhất trong câu chuyện.

[pause] Và để giữ luật, còn có những người chuyên truy bắt kẻ vi phạm. Giữa hai phía đó là những học trò như Coco, còn chưa hiểu hết đúng sai.

[pause] Điều thú vị là ma thuật cấm không phải lúc nào cũng xấu về kết quả. Nó có thể chữa lành hoặc giúp người, và chính điều đó khiến ranh giới đúng sai trở nên mờ.

[pause] [chuckles] Kaku để phần này ngắn thôi, vì càng nói càng spoiler. Chỉ cần biết: ma thuật cấm là sợi dây xuyên suốt cả bộ truyện.

[pause] Qifrey đưa Coco về xưởng của mình, nơi anh đang dạy ba học trò khác. Mỗi người là một kiểu tính cách rất khác nhau.

[pause] Agott là cô gái nghiêm khắc, xuất thân từ một gia đình phù thủy danh giá. Ban đầu cô rất khó chịu với một người ngoài như Coco.

[pause] Tetia vui vẻ, hay cười và muốn dùng phép để làm mọi người hạnh phúc. Richeh thì thích vẽ theo cách riêng, không muốn làm theo khuôn mẫu.

[pause] Qifrey là người thầy dịu dàng, luôn cho học trò tự tìm câu trả lời. [pause] Nhưng có vẻ anh cũng mang những bí mật riêng của mình.

[pause] Kaku ghi chú: bộ này giống một câu chuyện về trường học hơn là một câu chuyện chiến đấu. Mỗi học trò học cách vẽ, và học cả cách làm người.
```

### c06 · Kaku thử vẽ một phép / Vì sao bạn nên xem?

Khoảng 111 giây · cảnh s62–s74 · 1442 ký tự

**Gemini**

```text
Giờ tới phần thực hành! <laugh> Kaku sẽ thử thiết kế một phép theo đúng ba lớp. Lưu ý đây là phép Kaku tự nghĩ ra, không có trong truyện.

<short pause> Mục tiêu: một phép tưới cây nhẹ nhàng cho vườn. Bước một, chọn ký hiệu trung tâm là nước.

<short pause> Bước hai, thêm dấu hướng lên để nước bay lên, rồi thêm dấu cường độ nhỏ để nó không phun như vòi cứu hỏa.

<short pause> Bước ba, thêm dấu hình dạng để nước tỏa ra như cơn mưa phùn, thay vì một dòng thẳng.

<short pause> Bước cuối, khép kín vòng tròn. Nếu mọi thứ đúng, khu vườn sẽ có một cơn mưa nhỏ riêng.

<short pause> Nhưng nếu Kaku lỡ tay vẽ ngược dấu hướng thì sao? Nước sẽ bị hút xuống đất, và cả vườn khô héo. Một nét vẽ, hai kết cục.

<short pause> Đó chính là tinh thần của bộ truyện: phép thuật là một nghề thủ công, tỉ mỉ và đầy trách nhiệm.

<short pause> Tóm gọn lại, có bốn lý do Kaku nghĩ bạn nên cho Witch Hat Atelier một cơ hội.

<short pause> Lý do một: hình ảnh. Anime cố giữ cảm giác tranh minh họa của bản manga, với màu sắc dịu nhẹ như sách truyện cổ.

<short pause> Lý do hai: hệ thống phép thuật có luật rõ ràng. Bạn có thể tự đoán trước một phép sẽ hoạt động thế nào, và thấy thỏa mãn khi nhân vật dùng luật một cách thông minh.

<short pause> Lý do ba: câu chuyện về sự sáng tạo. Coco không phải thiên tài, nhưng cô nhìn phép thuật theo cách của một người ngoài, và điều đó thành lợi thế.

<short pause> Lý do bốn: bí ẩn. Người đội mũ rộng vành là ai, vì sao họ chọn Coco, và người thầy đang giấu điều gì? Những câu hỏi đó kéo bạn đi tiếp.

<short pause> Nếu bạn thích phiêu lưu nhẹ nhàng hơn là đánh nhau dồn dập, đây gần như chắc chắn là bộ dành cho bạn.
```

**ElevenLabs**

```text
Giờ tới phần thực hành! [chuckles] Kaku sẽ thử thiết kế một phép theo đúng ba lớp. Lưu ý đây là phép Kaku tự nghĩ ra, không có trong truyện.

[pause] Mục tiêu: một phép tưới cây nhẹ nhàng cho vườn. Bước một, chọn ký hiệu trung tâm là nước.

[pause] Bước hai, thêm dấu hướng lên để nước bay lên, rồi thêm dấu cường độ nhỏ để nó không phun như vòi cứu hỏa.

[pause] Bước ba, thêm dấu hình dạng để nước tỏa ra như cơn mưa phùn, thay vì một dòng thẳng.

[pause] Bước cuối, khép kín vòng tròn. Nếu mọi thứ đúng, khu vườn sẽ có một cơn mưa nhỏ riêng.

[pause] [curious] Nhưng nếu Kaku lỡ tay vẽ ngược dấu hướng thì sao? Nước sẽ bị hút xuống đất, và cả vườn khô héo. Một nét vẽ, hai kết cục.

[pause] Đó chính là tinh thần của bộ truyện: phép thuật là một nghề thủ công, tỉ mỉ và đầy trách nhiệm.

[pause] Tóm gọn lại, có bốn lý do Kaku nghĩ bạn nên cho Witch Hat Atelier một cơ hội.

[pause] Lý do một: hình ảnh. Anime cố giữ cảm giác tranh minh họa của bản manga, với màu sắc dịu nhẹ như sách truyện cổ.

[pause] Lý do hai: hệ thống phép thuật có luật rõ ràng. Bạn có thể tự đoán trước một phép sẽ hoạt động thế nào, và thấy thỏa mãn khi nhân vật dùng luật một cách thông minh.

[pause] Lý do ba: câu chuyện về sự sáng tạo. Coco không phải thiên tài, nhưng cô nhìn phép thuật theo cách của một người ngoài, và điều đó thành lợi thế.

[pause] Lý do bốn: bí ẩn. Người đội mũ rộng vành là ai, vì sao họ chọn Coco, và người thầy đang giấu điều gì? Những câu hỏi đó kéo bạn đi tiếp.

[pause] Nếu bạn thích phiêu lưu nhẹ nhàng hơn là đánh nhau dồn dập, đây gần như chắc chắn là bộ dành cho bạn.
```

### c07 · Góc nhìn của Kaku: khi phép thuật ai cũng học được / Câu hỏi người mới hay hỏi

Khoảng 128 giây · cảnh s75–s86 · 1668 ký tự

**Gemini**

```text
<laugh> Trước khi kết, Kaku muốn chia sẻ một điều khiến bộ này khác hầu hết các bộ fantasy khác.

<short pause> Trong nhiều truyện, sức mạnh là bẩm sinh: bạn sinh ra có tài năng hoặc không. Ở đây, sức mạnh là kiến thức. Ai học được thì dùng được.

<short pause> Và vì ai cũng dùng được, nên câu hỏi lớn không còn là ai mạnh nhất, mà là ai được phép biết. Đó là câu hỏi về quyền lực và sự tin tưởng.

<short pause> Các phù thủy giấu phép thuật để bảo vệ thế giới. <short pause> Nhưng chính bí mật đó cũng khiến người thường phụ thuộc vào họ, và khiến những đứa trẻ như Coco không có cơ hội.

<short pause> Kaku không nghĩ bộ truyện đưa ra câu trả lời dễ dàng. Và chính việc nó không trả lời vội là lý do nó đáng để suy ngẫm.

<short pause> Trước khi chốt lộ trình, Kaku gom vài câu hỏi mà người mới hay thắc mắc khi nghe về bộ này.

<short pause> Hỏi: bộ này có hợp với trẻ em không? Đáp: phần lớn nhẹ nhàng, nhưng có vài cảnh khá đáng sợ và căng thẳng, nên người lớn nên xem cùng các bạn nhỏ.

<short pause> Hỏi: không thích truyện nhịp chậm thì sao? Đáp: hãy thử đúng hai tập đầu. Nhịp của bộ này không đổi nhiều về sau, nên hai tập đó là bài kiểm tra công bằng.

<short pause> Hỏi: có cần biết gì về phép thuật trước không? Đáp: không. Bạn học luật cùng lúc với Coco, và đó chính là niềm vui của bộ truyện.

<short pause> Hỏi: có giống Frieren không? Đáp: giống ở không khí yên bình và sự tôn trọng dành cho phép thuật, nhưng Witch Hat Atelier tập trung vào việc học và sáng tạo, còn Frieren nói nhiều về thời gian và ký ức.

<short pause> Hỏi: nhân vật nào dễ thương nhất? Đáp: Kaku không dám trả lời, vì sợ bị cả xưởng vẽ giận. Bạn trả lời giúp Kaku ở phần bình luận nhé.

<short pause> Và câu hỏi cuối: có nên đọc manga trước khi xem anime không? Kaku nghĩ nên xem anime trước, để lần đầu nhìn thấy phép thuật chuyển động, rồi đọc manga để ngắm lại từng nét vẽ.
```

**ElevenLabs**

```text
[chuckles] Trước khi kết, Kaku muốn chia sẻ một điều khiến bộ này khác hầu hết các bộ fantasy khác.

[pause] Trong nhiều truyện, sức mạnh là bẩm sinh: bạn sinh ra có tài năng hoặc không. Ở đây, sức mạnh là kiến thức. Ai học được thì dùng được.

[pause] Và vì ai cũng dùng được, nên câu hỏi lớn không còn là ai mạnh nhất, mà là ai được phép biết. Đó là câu hỏi về quyền lực và sự tin tưởng.

[pause] Các phù thủy giấu phép thuật để bảo vệ thế giới. [pause] Nhưng chính bí mật đó cũng khiến người thường phụ thuộc vào họ, và khiến những đứa trẻ như Coco không có cơ hội.

[pause] Kaku không nghĩ bộ truyện đưa ra câu trả lời dễ dàng. Và chính việc nó không trả lời vội là lý do nó đáng để suy ngẫm.

[pause] Trước khi chốt lộ trình, Kaku gom vài câu hỏi mà người mới hay thắc mắc khi nghe về bộ này.

[pause] [curious] Hỏi: bộ này có hợp với trẻ em không? Đáp: phần lớn nhẹ nhàng, nhưng có vài cảnh khá đáng sợ và căng thẳng, nên người lớn nên xem cùng các bạn nhỏ.

[pause] Hỏi: không thích truyện nhịp chậm thì sao? Đáp: hãy thử đúng hai tập đầu. Nhịp của bộ này không đổi nhiều về sau, nên hai tập đó là bài kiểm tra công bằng.

[pause] Hỏi: có cần biết gì về phép thuật trước không? Đáp: không. Bạn học luật cùng lúc với Coco, và đó chính là niềm vui của bộ truyện.

[pause] Hỏi: có giống Frieren không? Đáp: giống ở không khí yên bình và sự tôn trọng dành cho phép thuật, nhưng Witch Hat Atelier tập trung vào việc học và sáng tạo, còn Frieren nói nhiều về thời gian và ký ức.

[pause] Hỏi: nhân vật nào dễ thương nhất? Đáp: Kaku không dám trả lời, vì sợ bị cả xưởng vẽ giận. Bạn trả lời giúp Kaku ở phần bình luận nhé.

[pause] Và câu hỏi cuối: có nên đọc manga trước khi xem anime không? Kaku nghĩ nên xem anime trước, để lần đầu nhìn thấy phép thuật chuyển động, rồi đọc manga để ngắm lại từng nét vẽ.
```

### c08 · Lộ trình xem cho người mới / Kết

Khoảng 88 giây · cảnh s87–s96 · 1139 ký tự

**Gemini**

```text
Nếu bạn muốn bắt đầu, đây là lộ trình Kaku gợi ý.

<short pause> Bước một: xem hai tập đầu của anime. Chúng ra mắt cùng lúc, đủ để bạn biết mình có hợp với nhịp chậm và nét vẽ này hay không.

<short pause> Bước hai: nếu thích, hãy xem hết mùa một, rồi đọc manga để đi tiếp, vì bản gốc vẫn đang được phát hành.

<short pause> Bước ba, tùy chọn: xem lại video này sau khi đã xem vài tập. Bạn sẽ thấy các luật ba lớp xuất hiện trong gần như mọi cảnh phép thuật.

<short pause> Và hãy nhớ, chỉ xem anime qua các nền tảng có bản quyền, để ủng hộ những người đã làm ra nó.

<short pause> Tóm lại: trong Witch Hat Atelier, phép thuật là hình tròn ba lớp gồm ký hiệu trung tâm, các dấu điều khiển và vòng tròn khép kín, vẽ bằng một loại mực đặc biệt.

<short pause> Ai cũng học được, nên cả thế giới phải giữ bí mật. Và một cô bé con nhà thợ may đã vô tình mở cánh cửa đó.

<short pause> Câu hỏi cho bạn: nếu được vẽ một phép trong thế giới này, bạn sẽ vẽ phép gì? Hãy mô tả ký hiệu và các dấu của bạn ở phần bình luận nhé.

<short pause> Video tới sẽ đổi hẳn không khí: Kaku sẽ mang thước và máy tính ra để kiểm tra xem kỹ thuật Xoay trong JoJo Steel Ball Run có đúng với khoa học không.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh để không bỏ lỡ. <laugh> Kaku cất bút đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Nếu bạn muốn bắt đầu, đây là lộ trình Kaku gợi ý.

[pause] Bước một: xem hai tập đầu của anime. Chúng ra mắt cùng lúc, đủ để bạn biết mình có hợp với nhịp chậm và nét vẽ này hay không.

[pause] Bước hai: nếu thích, hãy xem hết mùa một, rồi đọc manga để đi tiếp, vì bản gốc vẫn đang được phát hành.

[pause] Bước ba, tùy chọn: xem lại video này sau khi đã xem vài tập. Bạn sẽ thấy các luật ba lớp xuất hiện trong gần như mọi cảnh phép thuật.

[pause] Và hãy nhớ, chỉ xem anime qua các nền tảng có bản quyền, để ủng hộ những người đã làm ra nó.

[pause] Tóm lại: trong Witch Hat Atelier, phép thuật là hình tròn ba lớp gồm ký hiệu trung tâm, các dấu điều khiển và vòng tròn khép kín, vẽ bằng một loại mực đặc biệt.

[pause] Ai cũng học được, nên cả thế giới phải giữ bí mật. Và một cô bé con nhà thợ may đã vô tình mở cánh cửa đó.

[pause] [curious] Câu hỏi cho bạn: nếu được vẽ một phép trong thế giới này, bạn sẽ vẽ phép gì? Hãy mô tả ký hiệu và các dấu của bạn ở phần bình luận nhé.

[pause] Video tới sẽ đổi hẳn không khí: Kaku sẽ mang thước và máy tính ra để kiểm tra xem kỹ thuật Xoay trong JoJo Steel Ball Run có đúng với khoa học không.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh để không bỏ lỡ. [chuckles] Kaku cất bút đây, hẹn gặp lại!
```
