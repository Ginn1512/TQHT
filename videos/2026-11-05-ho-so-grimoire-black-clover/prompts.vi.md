# Bộ prompt · Black Clover: Hồ sơ grimoire ba lá, bốn lá, năm lá và phản ma thuật

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 90 ảnh, 7 đoạn đọc, khoảng 14.9 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (90 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Black Clover tới hết phần anime mùa đầu, một trăm bảy mươi tập, cùng một số chi ti…

```text
Wide 16:9 landscape cinematic frame. a massive library door with a clover emblem, slightly ajar, warm light spilling out. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Ở vương quốc Cỏ Ba Lá, năm mười lăm tuổi, mỗi đứa trẻ bước vào một tòa tháp cổ. Một cuốn sách bay xuống từ tr…

```text
Wide 16:9 landscape cinematic frame. a towering stone library interior with hundreds of books floating in the air, a teenager looking up in awe. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Những cuốn sách đó gọi là grimoire, sách phép. Và biểu tượng trên bìa, ba lá, bốn lá hay năm lá, nói lên rất…

```text
Wide 16:9 landscape cinematic frame. three grimoire covers side by side with glowing three-leaf, four-leaf and five-leaf clover emblems. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku, và hôm nay Kaku làm thủ thư. Mỗi chương là một thẻ thư viện, ghi bốn dòng: tên, l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at a library desk stamping a small index card, round glasses glinting. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Black Clover mùa hai vừa quay lại từ ngày 3 tháng 10 năm 2026, sau nhiều năm chờ đợi. Đây là lúc tốt nhất để…

```text
Wide 16:9 landscape cinematic frame. a calendar on a stone wall with October circled, a clover-shaped bookmark hanging from it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Thẻ số 1: Grimoire

Lời: Thẻ đầu tiên là chính cuốn grimoire. Tên: sách phép. Loại: vật phẩm gắn với một người duy nhất trong suốt cuộ…

```text
Wide 16:9 landscape cinematic frame. an index card reading GRIMOIRE with four blank lines, a glowing book resting on top of it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Cách hoạt động: grimoire lưu các phép thuật của chủ nhân. Khi người đó trưởng thành hoặc hiểu mình hơn, những…

```text
Wide 16:9 landscape cinematic frame. a floating book whose blank pages fill with glowing script one by one. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Điểm mạnh: nó giúp phép thuật mạnh hơn và ổn định hơn nhiều so với dùng ma lực trần. Trong thế giới này, pháp…

```text
Wide 16:9 landscape cinematic frame. two figures casting spells, one with a book producing a huge stable blast, the other a small flicker. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Điểm yếu: nếu mất grimoire hoặc bị đánh rơi giữa trận, pháp sư sẽ yếu đi rất nhiều. Và grimoire chỉ nhận đúng…

```text
Wide 16:9 landscape cinematic frame. a grimoire falling from a hand mid-battle, its owner reaching desperately. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: grimoire xuất hiện theo độ tuổi, không theo tài năng. Nghĩa là cơ hội đến với mọi người cùng lú…

```text
Wide 16:9 landscape cinematic frame. the owl mascot lining up small books of different colors on a shelf. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Thẻ số 2: Ma lực

Lời: Trước khi tới các loại lá, cần biết nguồn năng lượng. Tên: ma lực. Loại: năng lượng tồn tại trong cơ thể con…

```text
Wide 16:9 landscape cinematic frame. an index card reading MANA with a soft blue glow swirling around it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Ở vương quốc này, gần như ai cũng có ma lực. Nông dân dùng nó để làm ruộng, người bán hàng dùng để nấu ăn. Ph…

```text
Wide 16:9 landscape cinematic frame. a village scene where farmers float water buckets and a baker lights an oven with a small spell. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Mỗi người có một thuộc tính riêng: lửa, nước, gió, ánh sáng, bóng tối, và rất nhiều thuộc tính hiếm như thời…

```text
Wide 16:9 landscape cinematic frame. a ring of glowing elemental symbols around a clover: flame, droplet, swirl, sun, crescent, clock, portal. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Điểm mạnh: người có ma lực lớn có thể làm những điều phi thường. Điểm yếu: địa vị trong xã hội gắn chặt với l…

```text
Wide 16:9 landscape cinematic frame. a class pyramid: nobles with bright auras on top, commoners with faint glows at the bottom. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và rồi có một cậu bé sinh ra với ma lực bằng không. Không phải ít, mà là hoàn toàn không có. Hãy nhớ chi tiết…

```text
Wide 16:9 landscape cinematic frame. a small boy standing alone in a crowd of glowing people, no aura at all around him. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Thẻ số 3: Grimoire ba lá

Lời: Thẻ số ba là loại phổ biến nhất. Tên: grimoire ba lá. Loại: sách phép tiêu chuẩn của vương quốc.

```text
Wide 16:9 landscape cinematic frame. an index card reading THREE-LEAF, a green three-leaf clover emblem on a book cover. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Theo truyền thuyết của vương quốc, ba chiếc lá tượng trưng cho ba phẩm chất: sự chân thành, hy vọng, và tình…

```text
Wide 16:9 landscape cinematic frame. three glowing leaves each with a small icon: an open hand, a sunrise, and a heart. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Điểm mạnh: phần lớn các pháp sư mạnh nhất vương quốc, kể cả nhiều đội trưởng hiệp sĩ ma pháp, đều dùng grimoi…

```text
Wide 16:9 landscape cinematic frame. a row of powerful knight silhouettes in capes, each holding a three-leaf grimoire. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Điểm yếu: không có sức mạnh đặc biệt đi kèm. Mọi thứ phụ thuộc vào ma lực và sự luyện tập của chủ nhân.

```text
Wide 16:9 landscape cinematic frame. a figure training alone at night, sweat dripping, a plain three-leaf book beside them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: truyện rất khéo khi để sức mạnh đến từ con người, không phải từ số lá. Grimoire ba lá là bằng c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a three-leaf clover proudly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Thẻ số 4: Grimoire bốn lá

Lời: Tên: grimoire bốn lá. Loại: cực hiếm, được xem là dấu hiệu của số mệnh lớn.

```text
Wide 16:9 landscape cinematic frame. an index card reading FOUR-LEAF, a radiant four-leaf clover emblem glowing gold. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Lá thứ tư tượng trưng cho may mắn. Theo truyền thuyết, pháp vương đầu tiên của vương quốc cũng sở hữu một cuố…

```text
Wide 16:9 landscape cinematic frame. an ancient mural of a crowned figure holding a glowing four-leaf grimoire above a cheering crowd. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Trong truyện, Yuno, bạn thân và đối thủ của nhân vật chính, nhận được grimoire bốn lá. Cuốn sách còn thu hút…

```text
Wide 16:9 landscape cinematic frame. a calm young mage with a four-leaf grimoire, a tiny wind spirit swirling around his shoulder. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Điểm mạnh: phép thuật mạnh và đa dạng, được giới quý tộc và các hội hiệp sĩ săn đón ngay từ ngày nhận sách.

```text
Wide 16:9 landscape cinematic frame. several knight captains reaching out invitations toward a young mage holding a glowing book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Điểm yếu: áp lực. Mọi người coi người sở hữu là thiên tài được chọn, nên mọi thất bại đều bị soi xét gấp đôi.

```text
Wide 16:9 landscape cinematic frame. a young mage standing under a spotlight while dozens of eyes watch from the dark. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: có một ý thú vị. Bốn lá là may mắn, nhưng Yuno lại là người luyện tập chăm chỉ nhất truyện. May…

```text
Wide 16:9 landscape cinematic frame. the owl mascot jogging with a tiny four-leaf clover pinned to its scarf. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Thẻ số 5: Grimoire năm lá

Lời: Và giờ là thẻ bí ẩn nhất. Tên: grimoire năm lá. Loại: truyền thuyết đen tối, gần như không ai muốn nhận.

```text
Wide 16:9 landscape cinematic frame. an index card reading FIVE-LEAF, stained and torn at the edges, a black five-leaf clover emblem. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Theo truyền thuyết, lá thứ năm là nơi trú ngụ của ác quỷ. Người sở hữu grimoire năm lá được cho là mang theo…

```text
Wide 16:9 landscape cinematic frame. a dark grimoire with a shadowy horned silhouette faintly visible inside the fifth leaf. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Nhân vật chính Asta, cậu bé không có ma lực, ban đầu không nhận được sách. Sau đó một cuốn sách cũ nát, phủ đ…

```text
Wide 16:9 landscape cinematic frame. a dusty tattered black grimoire drifting down toward a determined boy in a dark alley. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Điểm mạnh: thay vì chứa phép, cuốn sách chứa những thanh kiếm, và một sức mạnh gọi là phản ma thuật, thứ ta s…

```text
Wide 16:9 landscape cinematic frame. a massive black sword emerging from the pages of a tattered grimoire. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Điểm yếu: mang tiếng xấu. Và về sau, truyện cho thấy trong cuốn sách của Asta thực sự có một ác quỷ. Vì sao n…

```text
Wide 16:9 landscape cinematic frame. a boy looking at his grimoire as a pair of red eyes open inside the fifth leaf. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: năm lá là sự đảo ngược của bốn lá. Một bên là may mắn trời cho, một bên là lời nguyền. Và truyệ…

```text
Wide 16:9 landscape cinematic frame. two boys back to back, one holding a glowing four-leaf book, the other a black five-leaf book. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Thẻ số 6: Phản ma thuật

Lời: Tên: phản ma thuật. Loại: sức mạnh vô hiệu hóa ma thuật, cực kỳ hiếm trong thế giới này.

```text
Wide 16:9 landscape cinematic frame. an index card reading ANTI-MAGIC, black mist curling off its edges. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Phản ma thuật không tạo ra phép. Nó xóa phép. Một đòn chém có phản ma thuật có thể cắt đôi quả cầu lửa, phá v…

```text
Wide 16:9 landscape cinematic frame. a black blade slicing a giant fireball in half, the flames dissolving into black mist. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và đây là điều trùng hợp tuyệt vời: sức mạnh này hợp nhất với một người không có chút ma lực nào, vì chính cơ…

```text
Wide 16:9 landscape cinematic frame. a boy with no aura calmly holding a sword wreathed in black mist, while mages nearby flinch away. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Điểm mạnh: gần như là khắc tinh của mọi pháp sư. Trong một thế giới nơi ai cũng dùng phép, người phá được phé…

```text
Wide 16:9 landscape cinematic frame. a row of spell circles shattering one after another as a black blade sweeps through them. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Điểm yếu: Asta không dùng được phép thường. Không bay được, không chữa thương được, không bắn từ xa được như…

```text
Wide 16:9 landscape cinematic frame. a boy running across rooftops while other mages fly overhead on brooms. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là thiết kế thông minh. Nhân vật yếu nhất theo luật của thế giới lại có sức mạnh phá chính…

```text
Wide 16:9 landscape cinematic frame. the owl mascot cutting a rulebook in half with tiny scissors. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Thẻ số 7: Những thanh kiếm

Lời: Tên: các thanh kiếm của grimoire năm lá. Loại: vũ khí chứa phản ma thuật, mỗi thanh có một công dụng riêng.

```text
Wide 16:9 landscape cinematic frame. an index card reading SWORDS with three sword silhouettes drawn on it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Thanh thứ nhất là Kiếm Diệt Quỷ: to, nặng, trông như một tấm sắt khổng lồ. Nó chém tan phép thuật chạm vào lư…

```text
Wide 16:9 landscape cinematic frame. a huge heavy black sword like a slab of iron, a muscular boy swinging it with effort. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Thanh thứ hai là Kiếm Trú Quỷ: mảnh hơn, có thể hấp thụ phép thuật của đối thủ rồi phóng trả lại bằng một nhá…

```text
Wide 16:9 landscape cinematic frame. a slimmer black sword absorbing a stream of light, then releasing it as a glowing slash. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Thanh thứ ba là Kiếm Hủy Quỷ: có thể hóa giải những hiệu ứng phép đang tác động lên người hay vật, như gỡ bỏ…

```text
Wide 16:9 landscape cinematic frame. a black sword touching glowing chains around a figure, the chains dissolving into mist. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Điểm mạnh: ba thanh kiếm cho Asta ba cách đối phó phép thuật: chém tan, hấp thụ và hóa giải. Điểm yếu: đều là…

```text
Wide 16:9 landscape cinematic frame. three swords arranged in a fan with small icons: slash, absorb, dispel. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · **Kaku** (đính kèm ảnh mẫu)

Lời: Về sau Asta còn có thêm vũ khí khác, nhưng Kaku dừng ở ba thanh này để tránh spoiler mùa hai.

```text
Wide 16:9 landscape cinematic frame. the owl mascot putting a cloth over a fourth sword shape on a rack. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Thẻ số 8: Dạng Đen

Lời: Tên: Dạng Đen. Loại: trạng thái khi phản ma thuật từ cuốn sách bao phủ cơ thể Asta.

```text
Wide 16:9 landscape cinematic frame. an index card reading BLACK FORM, a jagged black wing sketched in the corner. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Khi dùng, một bên tay Asta phủ màu đen, trên lưng mọc ra một cánh đen lởm chởm, và tốc độ lẫn sức mạnh tăng v…

```text
Wide 16:9 landscape cinematic frame. a boy with one arm covered in black, a single tattered black wing on his back, black mist swirling. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Điểm mạnh: Asta có thể di chuyển nhanh và chém mạnh hơn nhiều lần, đủ để đối đầu những đối thủ vượt xa mình.

```text
Wide 16:9 landscape cinematic frame. a black-winged figure dashing with speed lines past a stunned opponent. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Điểm yếu: ban đầu thời gian duy trì rất ngắn và cơ thể kiệt sức nhanh. Còn việc sức mạnh đến từ ác quỷ khiến…

```text
Wide 16:9 landscape cinematic frame. a boy collapsing to one knee, the black mist fading, onlookers watching with suspicion. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Dạng Đen là lần đầu truyện nói thẳng rằng sức mạnh của Asta có một cái giá. Mạnh hơn, nhưng bị…

```text
Wide 16:9 landscape cinematic frame. the owl mascot with one wing dipped in black ink, looking at it thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Thẻ số 9: Các hội hiệp sĩ ma pháp

Lời: Tên: các hội hiệp sĩ ma pháp. Loại: lực lượng bảo vệ vương quốc, chia thành chín hội, mỗi hội có đội trưởng v…

```text
Wide 16:9 landscape cinematic frame. an index card reading MAGIC KNIGHTS, nine small cape icons in different colors. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Mỗi năm, những người đã có grimoire tham gia kỳ thi tuyển. Các đội trưởng quan sát và giơ tay chọn người mình…

```text
Wide 16:9 landscape cinematic frame. an arena where candidates show their spells while nine captains watch from a high balcony. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Asta được hội Bò Tót Đen nhận, hội bị coi là tệ nhất, gồm toàn những người lập dị. Yuno vào hội Bình Minh Vàn…

```text
Wide 16:9 landscape cinematic frame. a messy rowdy hideout with a black bull emblem on one side, a pristine golden hall on the other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Điểm mạnh của hệ thống: người tài có đường tiến thân, kể cả thường dân. Điểm yếu: định kiến về xuất thân vẫn…

```text
Wide 16:9 landscape cinematic frame. a ladder with some rungs glowing for nobles and others cracked for commoners. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Trên đỉnh tất cả là pháp vương, người mạnh nhất và là biểu tượng của vương quốc. Và cả Asta lẫn Yuno đều có c…

```text
Wide 16:9 landscape cinematic frame. a tall throne-like seat atop a tower above the clouds, two small figures climbing toward it. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Thẻ số 10: Khí

Lời: Tên: khí. Loại: kỹ năng không dùng ma lực, bắt nguồn từ một đất nước ở phương Đông.

```text
Wide 16:9 landscape cinematic frame. an index card reading KI, a faint white outline of a person drawn on it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Khí là khả năng cảm nhận sự hiện diện và ý định của sinh vật sống, giống như đọc được chuyển động của đối thủ…

```text
Wide 16:9 landscape cinematic frame. a figure with eyes closed sensing faint white outlines of hidden enemies around a forest. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Vì Asta không có ma lực, cậu không cảm nhận được phép như người khác. Đội trưởng của hội Bò Tót Đen dạy cậu c…

```text
Wide 16:9 landscape cinematic frame. a tall captain with a sword over his shoulder teaching a young knight to close his eyes and feel. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Điểm mạnh: đọc được đòn tấn công kể cả khi không nhìn thấy, và không bị phép ẩn thân đánh lừa. Điểm yếu: cần…

```text
Wide 16:9 landscape cinematic frame. a boy dodging an invisible attack with eyes closed, a faint white silhouette revealing the attacker. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là chi tiết Kaku thích. Người không có phép không chờ phép đến với mình, mà tìm một con đườ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot meditating with eyes closed while tiny white outlines of butterflies flutter around. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Thẻ số 11: Tinh linh

Lời: Tên: tinh linh. Loại: những thực thể mang sức mạnh của tự nhiên, chỉ chọn những người đặc biệt để đi theo.

```text
Wide 16:9 landscape cinematic frame. an index card reading SPIRITS with four tiny elemental symbols in the corners. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Truyện nhắc tới bốn tinh linh lớn gắn với bốn nguyên tố: gió, lửa, nước và đất.

```text
Wide 16:9 landscape cinematic frame. four small glowing spirit silhouettes: a swirl of wind, a flame, a droplet, and a stone. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Tinh linh gió là tinh linh đi theo Yuno, và giúp phép gió của cậu mạnh hơn rất nhiều khi cả hai hợp sức.

```text
Wide 16:9 landscape cinematic frame. a young mage surrounded by a storm of wind, a small spirit glowing at the center of the vortex. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Điểm mạnh: người được tinh linh chọn có thể đạt đến những dạng sức mạnh vượt xa pháp sư thường. Điểm yếu: tin…

```text
Wide 16:9 landscape cinematic frame. a spirit turning its back on a demanding mage, crossing its tiny arms. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: tinh linh và ác quỷ là hai mặt đối lập. Một bên đi cùng người được tự nhiên chọn, bên kia trú t…

```text
Wide 16:9 landscape cinematic frame. a glowing wind spirit and a shadowy horned silhouette facing each other across a clover. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Ba hiểu lầm về số lá

Lời: Trước khi chơi trò chơi, Kaku muốn gỡ ba hiểu lầm rất hay gặp về grimoire.

```text
Wide 16:9 landscape cinematic frame. three sticky notes pinned to a library board, each with a red question mark. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Hiểu lầm một: càng nhiều lá càng mạnh. Không đúng. Rất nhiều nhân vật mạnh nhất truyện dùng sách ba lá. Số lá…

```text
Wide 16:9 landscape cinematic frame. a three-leaf book beating a four-leaf book in an arm wrestling match, a small crowd cheering. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Hiểu lầm hai: năm lá nghĩa là người xấu. Cũng không đúng. Asta là một trong những người tốt bụng nhất truyện.…

```text
Wide 16:9 landscape cinematic frame. a boy with a black grimoire helping a crying child stand up in a village street. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Hiểu lầm ba: cuốn sách quyết định bạn dùng phép gì. Thực ra thuộc tính phép thuộc về chính con người. Grimoir…

```text
Wide 16:9 landscape cinematic frame. a mage's hand glowing with fire before touching the book, the book then filling with fire spells. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cả ba hiểu lầm đều chung một gốc: tin rằng thứ bên ngoài quyết định giá trị con người. Và đó ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot crossing out three notes with a big red marker, looking satisfied. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Nếu bạn nhận grimoire hôm nay · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ tới trò chơi của thủ thư Kaku: nếu bạn bước vào tòa tháp hôm nay, cuốn sách nào sẽ chọn bạn? Chỉ để vui t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a floating stack of books with a question mark. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nếu bạn chăm chỉ, sống chân thành và đặt người khác lên trước, cuốn ba lá là của bạn. Đó cũng là cuốn của hầu…

```text
Wide 16:9 landscape cinematic frame. a warm glowing three-leaf book floating down toward an outstretched hand. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu bạn luôn thấy mình có vận may kỳ lạ và thích tự đặt mục tiêu thật cao, có khi lá thứ tư đang chờ bạn.

```text
Wide 16:9 landscape cinematic frame. a four-leaf book shining through a stained glass window onto a surprised reader. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Còn nếu cả thế giới bảo bạn không làm được, và bạn vẫn không bỏ cuộc, thì có lẽ một cuốn sách năm lá đầy bụi…

```text
Wide 16:9 landscape cinematic frame. a dusty black book drifting through an empty hall toward a lone determined silhouette. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thì chắc chắn nhận được một cuốn sổ ghi chép. Không có phép, nhưng ghi được mọi thứ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot hugging a plain notebook happily while fancy grimoires float past. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Góc nhìn của Kaku: sức mạnh của người không có gì · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại toàn bộ hồ sơ, Kaku thấy Black Clover kể một câu chuyện rất rõ ràng qua hệ thống grimoire.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a ladder in the library, looking over a wall of filing cards. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Thế giới này đo giá trị con người bằng ma lực và số lá trên bìa sách. Người sinh ra có nhiều thì được tôn trọ…

```text
Wide 16:9 landscape cinematic frame. a crowd sorting people by the brightness of their auras, dim figures pushed to the side. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Asta là câu trả lời ngược lại. Cậu không có ma lực, nhận cuốn sách bị nguyền rủa, vào hội bị coi thường nhất.…

```text
Wide 16:9 landscape cinematic frame. a boy standing at the bottom of a towering chart where every bar is empty for him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nhưng chính vì không có gì, cậu mới dùng được thứ sức mạnh xóa bỏ các luật cũ. Truyện đang nói rằng hệ thống…

```text
Wide 16:9 landscape cinematic frame. a black sword cutting through a giant ranking chart, pieces falling like paper. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Đó là lý do câu cửa miệng của Asta, không bao giờ bỏ cuộc, nghe có vẻ đơn giản nhưng lại hợp với cả hệ thống…

```text
Wide 16:9 landscape cinematic frame. a battered boy standing up again in the rain, sword planted in the ground. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Mùa hai: cần nhớ gì?

Lời: Nếu bạn chuẩn bị xem mùa hai, đây là vài điều nên nhớ.

```text
Wide 16:9 landscape cinematic frame. a checklist pinned to a library board with three items. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Một: mùa hai do Studio Pierrot thực hiện, có hai mươi bốn tập, phát trên Crunchyroll song song với Nhật Bản.

```text
Wide 16:9 landscape cinematic frame. a small screen with a clover emblem and a counter showing 24 episodes. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Hai: mối quan hệ giữa Asta và ác quỷ trong cuốn sách của cậu sẽ ngày càng quan trọng. Hãy để ý mỗi lần cuốn s…

```text
Wide 16:9 landscape cinematic frame. a black grimoire trembling on a table, faint red light leaking from its pages. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Ba: thẻ số sáu về phản ma thuật chưa phải là tất cả. Luật của nó sẽ còn được mở rộng, và có thể bạn sẽ muốn q…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adding a blank card to the ANTI-MAGIC file, marked with a question mark. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Mục lục hồ sơ

Lời: Đóng hồ sơ lại, đây là mục lục của thủ thư Kaku.

```text
Wide 16:9 landscape cinematic frame. a neatly organized card catalog drawer being pulled open. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Grimoire là cuốn sách phép nhận năm mười lăm tuổi. Ma lực là năng lượng của mọi người và cũng là thước đo địa…

```text
Wide 16:9 landscape cinematic frame. two index cards lit up: GRIMOIRE and MANA. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Ba lá là chân thành, hy vọng, tình yêu. Bốn lá là may mắn. Năm lá là nơi ác quỷ trú ngụ.

```text
Wide 16:9 landscape cinematic frame. three index cards lit up with three-leaf, four-leaf and five-leaf emblems. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Phản ma thuật xóa phép, đi qua ba thanh kiếm và Dạng Đen, trong tay cậu bé không có chút ma lực nào.

```text
Wide 16:9 landscape cinematic frame. index cards for ANTI-MAGIC, SWORDS and BLACK FORM lit up in black and silver. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được chọn, bạn muốn nhận cuốn sách mấy lá, và thuộc tính phép của bạn là gì? Viết vào ph…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank index card and a quill toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Video tới, Kaku rời thư viện để làm việc khác: gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Jujutsu Kaisen.

```text
Wide 16:9 landscape cinematic frame. a notice board with ten pinned notes, several crossed out in red. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để thẻ thư viện của bạn luôn được gia hạn. Thủ thư Kaku đóng cửa đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot turning off a desk lamp and waving from a quiet library. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Thẻ số 1: Grimoire

Khoảng 112 giây · cảnh s01–s10 · 1462 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Black Clover tới hết phần anime mùa đầu, một trăm bảy mươi tập, cùng một số chi tiết trong manga. Nếu bạn định xem mùa hai mà chưa xem mùa một, hãy cân nhắc nhé.

<short pause> Ở vương quốc Cỏ Ba Lá, năm mười lăm tuổi, mỗi đứa trẻ bước vào một tòa tháp cổ. Một cuốn sách bay xuống từ trên cao và chọn lấy nó. Cuốn sách đó sẽ đi theo nó suốt cuộc đời.

<short pause> Những cuốn sách đó gọi là grimoire, sách phép. Và biểu tượng trên bìa, ba lá, bốn lá hay năm lá, nói lên rất nhiều điều về người được chọn.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku, và hôm nay Kaku làm thủ thư. Mỗi chương là một thẻ thư viện, ghi bốn dòng: tên, loại, điểm mạnh, điểm yếu.

<short pause> Black Clover mùa hai vừa quay lại từ ngày 3 tháng 10 năm 2026, sau nhiều năm chờ đợi. Đây là lúc tốt nhất để ôn lại toàn bộ hệ thống sách phép.

<short pause> Thẻ đầu tiên là chính cuốn grimoire. Tên: sách phép. Loại: vật phẩm gắn với một người duy nhất trong suốt cuộc đời.

<short pause> Cách hoạt động: grimoire lưu các phép thuật của chủ nhân. Khi người đó trưởng thành hoặc hiểu mình hơn, những trang mới xuất hiện với phép mới.

<short pause> Điểm mạnh: nó giúp phép thuật mạnh hơn và ổn định hơn nhiều so với dùng ma lực trần. Trong thế giới này, pháp sư có grimoire mạnh hơn hẳn pháp sư không có.

<short pause> Điểm yếu: nếu mất grimoire hoặc bị đánh rơi giữa trận, pháp sư sẽ yếu đi rất nhiều. Và grimoire chỉ nhận đúng một chủ.

<short pause> Kaku ghi chú: grimoire xuất hiện theo độ tuổi, không theo tài năng. Nghĩa là cơ hội đến với mọi người cùng lúc, nhưng thứ nhận được thì không ai giống ai.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Black Clover tới hết phần anime mùa đầu, một trăm bảy mươi tập, cùng một số chi tiết trong manga. Nếu bạn định xem mùa hai mà chưa xem mùa một, hãy cân nhắc nhé.

[pause] Ở vương quốc Cỏ Ba Lá, năm mười lăm tuổi, mỗi đứa trẻ bước vào một tòa tháp cổ. Một cuốn sách bay xuống từ trên cao và chọn lấy nó. Cuốn sách đó sẽ đi theo nó suốt cuộc đời.

[pause] Những cuốn sách đó gọi là grimoire, sách phép. Và biểu tượng trên bìa, ba lá, bốn lá hay năm lá, nói lên rất nhiều điều về người được chọn.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku, và hôm nay Kaku làm thủ thư. Mỗi chương là một thẻ thư viện, ghi bốn dòng: tên, loại, điểm mạnh, điểm yếu.

[pause] Black Clover mùa hai vừa quay lại từ ngày 3 tháng 10 năm 2026, sau nhiều năm chờ đợi. Đây là lúc tốt nhất để ôn lại toàn bộ hệ thống sách phép.

[pause] Thẻ đầu tiên là chính cuốn grimoire. Tên: sách phép. Loại: vật phẩm gắn với một người duy nhất trong suốt cuộc đời.

[pause] Cách hoạt động: grimoire lưu các phép thuật của chủ nhân. Khi người đó trưởng thành hoặc hiểu mình hơn, những trang mới xuất hiện với phép mới.

[pause] Điểm mạnh: nó giúp phép thuật mạnh hơn và ổn định hơn nhiều so với dùng ma lực trần. Trong thế giới này, pháp sư có grimoire mạnh hơn hẳn pháp sư không có.

[pause] Điểm yếu: nếu mất grimoire hoặc bị đánh rơi giữa trận, pháp sư sẽ yếu đi rất nhiều. Và grimoire chỉ nhận đúng một chủ.

[pause] Kaku ghi chú: grimoire xuất hiện theo độ tuổi, không theo tài năng. Nghĩa là cơ hội đến với mọi người cùng lúc, nhưng thứ nhận được thì không ai giống ai.
```

### c02 · Thẻ số 2: Ma lực / Thẻ số 3: Grimoire ba lá

Khoảng 103 giây · cảnh s11–s20 · 1337 ký tự

**Gemini**

```text
Trước khi tới các loại lá, cần biết nguồn năng lượng. Tên: ma lực. Loại: năng lượng tồn tại trong cơ thể con người và khắp thế giới tự nhiên.

<short pause> Ở vương quốc này, gần như ai cũng có ma lực. Nông dân dùng nó để làm ruộng, người bán hàng dùng để nấu ăn. Phép thuật là một phần của đời sống thường ngày.

<short pause> Mỗi người có một thuộc tính riêng: lửa, nước, gió, ánh sáng, bóng tối, và rất nhiều thuộc tính hiếm như thời gian hay không gian.

<short pause> Điểm mạnh: người có ma lực lớn có thể làm những điều phi thường. Điểm yếu: địa vị trong xã hội gắn chặt với lượng ma lực, và người ít ma lực bị coi thường.

<short pause> Và rồi có một cậu bé sinh ra với ma lực bằng không. Không phải ít, mà là hoàn toàn không có. Hãy nhớ chi tiết này, vì nó là chìa khóa của thẻ số năm.

<short pause> Thẻ số ba là loại phổ biến nhất. Tên: grimoire ba lá. Loại: sách phép tiêu chuẩn của vương quốc.

<short pause> Theo truyền thuyết của vương quốc, ba chiếc lá tượng trưng cho ba phẩm chất: sự chân thành, hy vọng, và tình yêu.

<short pause> Điểm mạnh: phần lớn các pháp sư mạnh nhất vương quốc, kể cả nhiều đội trưởng hiệp sĩ ma pháp, đều dùng grimoire ba lá. Ba lá không có nghĩa là yếu.

<short pause> Điểm yếu: không có sức mạnh đặc biệt đi kèm. Mọi thứ phụ thuộc vào ma lực và sự luyện tập của chủ nhân.

<short pause> <laugh> Kaku ghi chú: truyện rất khéo khi để sức mạnh đến từ con người, không phải từ số lá. Grimoire ba lá là bằng chứng rằng nỗ lực vẫn là con đường chính.
```

**ElevenLabs**

```text
Trước khi tới các loại lá, cần biết nguồn năng lượng. Tên: ma lực. Loại: năng lượng tồn tại trong cơ thể con người và khắp thế giới tự nhiên.

[pause] Ở vương quốc này, gần như ai cũng có ma lực. Nông dân dùng nó để làm ruộng, người bán hàng dùng để nấu ăn. Phép thuật là một phần của đời sống thường ngày.

[pause] Mỗi người có một thuộc tính riêng: lửa, nước, gió, ánh sáng, bóng tối, và rất nhiều thuộc tính hiếm như thời gian hay không gian.

[pause] Điểm mạnh: người có ma lực lớn có thể làm những điều phi thường. Điểm yếu: địa vị trong xã hội gắn chặt với lượng ma lực, và người ít ma lực bị coi thường.

[pause] Và rồi có một cậu bé sinh ra với ma lực bằng không. Không phải ít, mà là hoàn toàn không có. Hãy nhớ chi tiết này, vì nó là chìa khóa của thẻ số năm.

[pause] Thẻ số ba là loại phổ biến nhất. Tên: grimoire ba lá. Loại: sách phép tiêu chuẩn của vương quốc.

[pause] Theo truyền thuyết của vương quốc, ba chiếc lá tượng trưng cho ba phẩm chất: sự chân thành, hy vọng, và tình yêu.

[pause] Điểm mạnh: phần lớn các pháp sư mạnh nhất vương quốc, kể cả nhiều đội trưởng hiệp sĩ ma pháp, đều dùng grimoire ba lá. Ba lá không có nghĩa là yếu.

[pause] Điểm yếu: không có sức mạnh đặc biệt đi kèm. Mọi thứ phụ thuộc vào ma lực và sự luyện tập của chủ nhân.

[pause] [chuckles] Kaku ghi chú: truyện rất khéo khi để sức mạnh đến từ con người, không phải từ số lá. Grimoire ba lá là bằng chứng rằng nỗ lực vẫn là con đường chính.
```

### c03 · Thẻ số 4: Grimoire bốn lá / Thẻ số 5: Grimoire năm lá

Khoảng 120 giây · cảnh s21–s32 · 1561 ký tự

**Gemini**

```text
Tên: grimoire bốn lá. Loại: cực hiếm, được xem là dấu hiệu của số mệnh lớn.

<short pause> Lá thứ tư tượng trưng cho may mắn. Theo truyền thuyết, pháp vương đầu tiên của vương quốc cũng sở hữu một cuốn grimoire bốn lá.

<short pause> Trong truyện, Yuno, bạn thân và đối thủ của nhân vật chính, nhận được grimoire bốn lá. Cuốn sách còn thu hút một tinh linh gió đi theo cậu.

<short pause> Điểm mạnh: phép thuật mạnh và đa dạng, được giới quý tộc và các hội hiệp sĩ săn đón ngay từ ngày nhận sách.

<short pause> Điểm yếu: áp lực. Mọi người coi người sở hữu là thiên tài được chọn, nên mọi thất bại đều bị soi xét gấp đôi.

<short pause> <laugh> Kaku ghi chú: có một ý thú vị. Bốn lá là may mắn, nhưng Yuno lại là người luyện tập chăm chỉ nhất truyện. May mắn chỉ là điểm xuất phát.

<short pause> Và giờ là thẻ bí ẩn nhất. Tên: grimoire năm lá. Loại: truyền thuyết đen tối, gần như không ai muốn nhận.

<short pause> Theo truyền thuyết, lá thứ năm là nơi trú ngụ của ác quỷ. Người sở hữu grimoire năm lá được cho là mang theo một ác quỷ bên mình.

<short pause> Nhân vật chính Asta, cậu bé không có ma lực, ban đầu không nhận được sách. Sau đó một cuốn sách cũ nát, phủ đầy bụi, tự tìm đến cậu. Trên bìa là cỏ năm lá màu đen.

<short pause> Điểm mạnh: thay vì chứa phép, cuốn sách chứa những thanh kiếm, và một sức mạnh gọi là phản ma thuật, thứ ta sẽ mở ở thẻ tiếp theo.

<short pause> Điểm yếu: mang tiếng xấu. Và về sau, truyện cho thấy trong cuốn sách của Asta thực sự có một ác quỷ. Vì sao nó ở đó và muốn gì là một trong những bí ẩn lớn của bộ truyện.

<short pause> Kaku ghi chú: năm lá là sự đảo ngược của bốn lá. Một bên là may mắn trời cho, một bên là lời nguyền. Và truyện đặt hai cuốn sách đó vào tay hai người bạn lớn lên cùng nhau.
```

**ElevenLabs**

```text
Tên: grimoire bốn lá. Loại: cực hiếm, được xem là dấu hiệu của số mệnh lớn.

[pause] Lá thứ tư tượng trưng cho may mắn. Theo truyền thuyết, pháp vương đầu tiên của vương quốc cũng sở hữu một cuốn grimoire bốn lá.

[pause] Trong truyện, Yuno, bạn thân và đối thủ của nhân vật chính, nhận được grimoire bốn lá. Cuốn sách còn thu hút một tinh linh gió đi theo cậu.

[pause] Điểm mạnh: phép thuật mạnh và đa dạng, được giới quý tộc và các hội hiệp sĩ săn đón ngay từ ngày nhận sách.

[pause] Điểm yếu: áp lực. Mọi người coi người sở hữu là thiên tài được chọn, nên mọi thất bại đều bị soi xét gấp đôi.

[pause] [chuckles] Kaku ghi chú: có một ý thú vị. Bốn lá là may mắn, nhưng Yuno lại là người luyện tập chăm chỉ nhất truyện. May mắn chỉ là điểm xuất phát.

[pause] Và giờ là thẻ bí ẩn nhất. Tên: grimoire năm lá. Loại: truyền thuyết đen tối, gần như không ai muốn nhận.

[pause] Theo truyền thuyết, lá thứ năm là nơi trú ngụ của ác quỷ. Người sở hữu grimoire năm lá được cho là mang theo một ác quỷ bên mình.

[pause] Nhân vật chính Asta, cậu bé không có ma lực, ban đầu không nhận được sách. Sau đó một cuốn sách cũ nát, phủ đầy bụi, tự tìm đến cậu. Trên bìa là cỏ năm lá màu đen.

[pause] Điểm mạnh: thay vì chứa phép, cuốn sách chứa những thanh kiếm, và một sức mạnh gọi là phản ma thuật, thứ ta sẽ mở ở thẻ tiếp theo.

[pause] Điểm yếu: mang tiếng xấu. Và về sau, truyện cho thấy trong cuốn sách của Asta thực sự có một ác quỷ. Vì sao nó ở đó và muốn gì là một trong những bí ẩn lớn của bộ truyện.

[pause] Kaku ghi chú: năm lá là sự đảo ngược của bốn lá. Một bên là may mắn trời cho, một bên là lời nguyền. Và truyện đặt hai cuốn sách đó vào tay hai người bạn lớn lên cùng nhau.
```

### c04 · Thẻ số 6: Phản ma thuật / Thẻ số 7: Những thanh kiếm

Khoảng 121 giây · cảnh s33–s44 · 1569 ký tự

**Gemini**

```text
Tên: phản ma thuật. Loại: sức mạnh vô hiệu hóa ma thuật, cực kỳ hiếm trong thế giới này.

<short pause> Phản ma thuật không tạo ra phép. Nó xóa phép. Một đòn chém có phản ma thuật có thể cắt đôi quả cầu lửa, phá vỡ lá chắn phép, hay vô hiệu hóa lời nguyền.

<short pause> Và đây là điều trùng hợp tuyệt vời: sức mạnh này hợp nhất với một người không có chút ma lực nào, vì chính cơ thể cậu không bị nó bài xích.

<short pause> Điểm mạnh: gần như là khắc tinh của mọi pháp sư. Trong một thế giới nơi ai cũng dùng phép, người phá được phép là mối đe dọa lớn nhất.

<short pause> Điểm yếu: Asta không dùng được phép thường. Không bay được, không chữa thương được, không bắn từ xa được như người khác. Mọi thứ phải bù bằng cơ thể và kiếm.

<short pause> <laugh> Kaku ghi chú: đây là thiết kế thông minh. Nhân vật yếu nhất theo luật của thế giới lại có sức mạnh phá chính cái luật đó.

<short pause> Tên: các thanh kiếm của grimoire năm lá. Loại: vũ khí chứa phản ma thuật, mỗi thanh có một công dụng riêng.

<short pause> Thanh thứ nhất là Kiếm Diệt Quỷ: to, nặng, trông như một tấm sắt khổng lồ. Nó chém tan phép thuật chạm vào lưỡi kiếm. Asta phải luyện cơ bắp cả đời mới vung nổi nó.

<short pause> Thanh thứ hai là Kiếm Trú Quỷ: mảnh hơn, có thể hấp thụ phép thuật của đối thủ rồi phóng trả lại bằng một nhát chém.

<short pause> Thanh thứ ba là Kiếm Hủy Quỷ: có thể hóa giải những hiệu ứng phép đang tác động lên người hay vật, như gỡ bỏ một phép đang trói buộc ai đó.

<short pause> Điểm mạnh: ba thanh kiếm cho Asta ba cách đối phó phép thuật: chém tan, hấp thụ và hóa giải. Điểm yếu: đều là vũ khí cận chiến, phải lao vào gần mới dùng được.

<short pause> Về sau Asta còn có thêm vũ khí khác, nhưng Kaku dừng ở ba thanh này để tránh spoiler mùa hai.
```

**ElevenLabs**

```text
Tên: phản ma thuật. Loại: sức mạnh vô hiệu hóa ma thuật, cực kỳ hiếm trong thế giới này.

[pause] Phản ma thuật không tạo ra phép. Nó xóa phép. Một đòn chém có phản ma thuật có thể cắt đôi quả cầu lửa, phá vỡ lá chắn phép, hay vô hiệu hóa lời nguyền.

[pause] Và đây là điều trùng hợp tuyệt vời: sức mạnh này hợp nhất với một người không có chút ma lực nào, vì chính cơ thể cậu không bị nó bài xích.

[pause] Điểm mạnh: gần như là khắc tinh của mọi pháp sư. Trong một thế giới nơi ai cũng dùng phép, người phá được phép là mối đe dọa lớn nhất.

[pause] Điểm yếu: Asta không dùng được phép thường. Không bay được, không chữa thương được, không bắn từ xa được như người khác. Mọi thứ phải bù bằng cơ thể và kiếm.

[pause] [chuckles] Kaku ghi chú: đây là thiết kế thông minh. Nhân vật yếu nhất theo luật của thế giới lại có sức mạnh phá chính cái luật đó.

[pause] Tên: các thanh kiếm của grimoire năm lá. Loại: vũ khí chứa phản ma thuật, mỗi thanh có một công dụng riêng.

[pause] Thanh thứ nhất là Kiếm Diệt Quỷ: to, nặng, trông như một tấm sắt khổng lồ. Nó chém tan phép thuật chạm vào lưỡi kiếm. Asta phải luyện cơ bắp cả đời mới vung nổi nó.

[pause] Thanh thứ hai là Kiếm Trú Quỷ: mảnh hơn, có thể hấp thụ phép thuật của đối thủ rồi phóng trả lại bằng một nhát chém.

[pause] Thanh thứ ba là Kiếm Hủy Quỷ: có thể hóa giải những hiệu ứng phép đang tác động lên người hay vật, như gỡ bỏ một phép đang trói buộc ai đó.

[pause] Điểm mạnh: ba thanh kiếm cho Asta ba cách đối phó phép thuật: chém tan, hấp thụ và hóa giải. Điểm yếu: đều là vũ khí cận chiến, phải lao vào gần mới dùng được.

[pause] Về sau Asta còn có thêm vũ khí khác, nhưng Kaku dừng ở ba thanh này để tránh spoiler mùa hai.
```

### c05 · Thẻ số 8: Dạng Đen / Thẻ số 9: Các hội hiệp sĩ ma pháp / Thẻ số 10: Khí

Khoảng 149 giây · cảnh s45–s59 · 1935 ký tự

**Gemini**

```text
Tên: Dạng Đen. Loại: trạng thái khi phản ma thuật từ cuốn sách bao phủ cơ thể Asta.

<short pause> Khi dùng, một bên tay Asta phủ màu đen, trên lưng mọc ra một cánh đen lởm chởm, và tốc độ lẫn sức mạnh tăng vọt.

<short pause> Điểm mạnh: Asta có thể di chuyển nhanh và chém mạnh hơn nhiều lần, đủ để đối đầu những đối thủ vượt xa mình.

<short pause> Điểm yếu: ban đầu thời gian duy trì rất ngắn và cơ thể kiệt sức nhanh. Còn việc sức mạnh đến từ ác quỷ khiến người khác lo sợ, nghi ngờ cậu.

<short pause> <laugh> Kaku ghi chú: Dạng Đen là lần đầu truyện nói thẳng rằng sức mạnh của Asta có một cái giá. Mạnh hơn, nhưng bị nhìn bằng ánh mắt khác.

<short pause> Tên: các hội hiệp sĩ ma pháp. Loại: lực lượng bảo vệ vương quốc, chia thành chín hội, mỗi hội có đội trưởng và màu áo choàng riêng.

<short pause> Mỗi năm, những người đã có grimoire tham gia kỳ thi tuyển. Các đội trưởng quan sát và giơ tay chọn người mình muốn.

<short pause> Asta được hội Bò Tót Đen nhận, hội bị coi là tệ nhất, gồm toàn những người lập dị. Yuno vào hội Bình Minh Vàng, hội được đánh giá cao nhất.

<short pause> Điểm mạnh của hệ thống: người tài có đường tiến thân, kể cả thường dân. Điểm yếu: định kiến về xuất thân vẫn ảnh hưởng tới việc ai được chọn và ai được thăng tiến.

<short pause> Trên đỉnh tất cả là pháp vương, người mạnh nhất và là biểu tượng của vương quốc. Và cả Asta lẫn Yuno đều có chung một ước mơ: trở thành pháp vương.

<short pause> Tên: khí. Loại: kỹ năng không dùng ma lực, bắt nguồn từ một đất nước ở phương Đông.

<short pause> Khí là khả năng cảm nhận sự hiện diện và ý định của sinh vật sống, giống như đọc được chuyển động của đối thủ trước khi chúng xảy ra.

<short pause> Vì Asta không có ma lực, cậu không cảm nhận được phép như người khác. Đội trưởng của hội Bò Tót Đen dạy cậu cách đọc khí để bù lại điểm yếu đó.

<short pause> Điểm mạnh: đọc được đòn tấn công kể cả khi không nhìn thấy, và không bị phép ẩn thân đánh lừa. Điểm yếu: cần luyện tập rất lâu, và đối thủ không có ý định rõ ràng thì khó đọc hơn.

<short pause> Kaku ghi chú: đây là chi tiết Kaku thích. Người không có phép không chờ phép đến với mình, mà tìm một con đường khác hoàn toàn.
```

**ElevenLabs**

```text
Tên: Dạng Đen. Loại: trạng thái khi phản ma thuật từ cuốn sách bao phủ cơ thể Asta.

[pause] Khi dùng, một bên tay Asta phủ màu đen, trên lưng mọc ra một cánh đen lởm chởm, và tốc độ lẫn sức mạnh tăng vọt.

[pause] Điểm mạnh: Asta có thể di chuyển nhanh và chém mạnh hơn nhiều lần, đủ để đối đầu những đối thủ vượt xa mình.

[pause] Điểm yếu: ban đầu thời gian duy trì rất ngắn và cơ thể kiệt sức nhanh. Còn việc sức mạnh đến từ ác quỷ khiến người khác lo sợ, nghi ngờ cậu.

[pause] [chuckles] Kaku ghi chú: Dạng Đen là lần đầu truyện nói thẳng rằng sức mạnh của Asta có một cái giá. Mạnh hơn, nhưng bị nhìn bằng ánh mắt khác.

[pause] Tên: các hội hiệp sĩ ma pháp. Loại: lực lượng bảo vệ vương quốc, chia thành chín hội, mỗi hội có đội trưởng và màu áo choàng riêng.

[pause] Mỗi năm, những người đã có grimoire tham gia kỳ thi tuyển. Các đội trưởng quan sát và giơ tay chọn người mình muốn.

[pause] Asta được hội Bò Tót Đen nhận, hội bị coi là tệ nhất, gồm toàn những người lập dị. Yuno vào hội Bình Minh Vàng, hội được đánh giá cao nhất.

[pause] Điểm mạnh của hệ thống: người tài có đường tiến thân, kể cả thường dân. Điểm yếu: định kiến về xuất thân vẫn ảnh hưởng tới việc ai được chọn và ai được thăng tiến.

[pause] Trên đỉnh tất cả là pháp vương, người mạnh nhất và là biểu tượng của vương quốc. Và cả Asta lẫn Yuno đều có chung một ước mơ: trở thành pháp vương.

[pause] Tên: khí. Loại: kỹ năng không dùng ma lực, bắt nguồn từ một đất nước ở phương Đông.

[pause] Khí là khả năng cảm nhận sự hiện diện và ý định của sinh vật sống, giống như đọc được chuyển động của đối thủ trước khi chúng xảy ra.

[pause] Vì Asta không có ma lực, cậu không cảm nhận được phép như người khác. Đội trưởng của hội Bò Tót Đen dạy cậu cách đọc khí để bù lại điểm yếu đó.

[pause] Điểm mạnh: đọc được đòn tấn công kể cả khi không nhìn thấy, và không bị phép ẩn thân đánh lừa. Điểm yếu: cần luyện tập rất lâu, và đối thủ không có ý định rõ ràng thì khó đọc hơn.

[pause] Kaku ghi chú: đây là chi tiết Kaku thích. Người không có phép không chờ phép đến với mình, mà tìm một con đường khác hoàn toàn.
```

### c06 · Thẻ số 11: Tinh linh / Ba hiểu lầm về số lá / Nếu bạn nhận grimoire hôm nay

Khoảng 148 giây · cảnh s60–s74 · 1930 ký tự

**Gemini**

```text
Tên: tinh linh. Loại: những thực thể mang sức mạnh của tự nhiên, chỉ chọn những người đặc biệt để đi theo.

<short pause> Truyện nhắc tới bốn tinh linh lớn gắn với bốn nguyên tố: gió, lửa, nước và đất.

<short pause> Tinh linh gió là tinh linh đi theo Yuno, và giúp phép gió của cậu mạnh hơn rất nhiều khi cả hai hợp sức.

<short pause> Điểm mạnh: người được tinh linh chọn có thể đạt đến những dạng sức mạnh vượt xa pháp sư thường. Điểm yếu: tinh linh có ý chí riêng, không phải công cụ muốn dùng lúc nào cũng được.

<short pause> <laugh> Kaku ghi chú: tinh linh và ác quỷ là hai mặt đối lập. Một bên đi cùng người được tự nhiên chọn, bên kia trú trong cuốn sách của cậu bé bị cả thế giới gạt ra ngoài.

<short pause> Trước khi chơi trò chơi, Kaku muốn gỡ ba hiểu lầm rất hay gặp về grimoire.

<short pause> Hiểu lầm một: càng nhiều lá càng mạnh. Không đúng. Rất nhiều nhân vật mạnh nhất truyện dùng sách ba lá. Số lá nói về loại sức mạnh, không nói về độ mạnh.

<short pause> Hiểu lầm hai: năm lá nghĩa là người xấu. Cũng không đúng. Asta là một trong những người tốt bụng nhất truyện. Cuốn sách mang tiếng xấu, nhưng người cầm nó thì không.

<short pause> Hiểu lầm ba: cuốn sách quyết định bạn dùng phép gì. Thực ra thuộc tính phép thuộc về chính con người. Grimoire giống một cuốn sổ ghi lại và khuếch đại những gì người đó vốn có.

<short pause> Kaku ghi chú: cả ba hiểu lầm đều chung một gốc: tin rằng thứ bên ngoài quyết định giá trị con người. Và đó chính là điều Black Clover muốn phản bác.

<short pause> Giờ tới trò chơi của thủ thư Kaku: nếu bạn bước vào tòa tháp hôm nay, cuốn sách nào sẽ chọn bạn? Chỉ để vui thôi nhé.

<short pause> Nếu bạn chăm chỉ, sống chân thành và đặt người khác lên trước, cuốn ba lá là của bạn. Đó cũng là cuốn của hầu hết những người mạnh nhất.

<short pause> Nếu bạn luôn thấy mình có vận may kỳ lạ và thích tự đặt mục tiêu thật cao, có khi lá thứ tư đang chờ bạn.

<short pause> Còn nếu cả thế giới bảo bạn không làm được, và bạn vẫn không bỏ cuộc, thì có lẽ một cuốn sách năm lá đầy bụi đang tìm đường đến với bạn.

<short pause> Kaku thì chắc chắn nhận được một cuốn sổ ghi chép. Không có phép, nhưng ghi được mọi thứ.
```

**ElevenLabs**

```text
Tên: tinh linh. Loại: những thực thể mang sức mạnh của tự nhiên, chỉ chọn những người đặc biệt để đi theo.

[pause] Truyện nhắc tới bốn tinh linh lớn gắn với bốn nguyên tố: gió, lửa, nước và đất.

[pause] Tinh linh gió là tinh linh đi theo Yuno, và giúp phép gió của cậu mạnh hơn rất nhiều khi cả hai hợp sức.

[pause] Điểm mạnh: người được tinh linh chọn có thể đạt đến những dạng sức mạnh vượt xa pháp sư thường. Điểm yếu: tinh linh có ý chí riêng, không phải công cụ muốn dùng lúc nào cũng được.

[pause] [chuckles] Kaku ghi chú: tinh linh và ác quỷ là hai mặt đối lập. Một bên đi cùng người được tự nhiên chọn, bên kia trú trong cuốn sách của cậu bé bị cả thế giới gạt ra ngoài.

[pause] Trước khi chơi trò chơi, Kaku muốn gỡ ba hiểu lầm rất hay gặp về grimoire.

[pause] Hiểu lầm một: càng nhiều lá càng mạnh. Không đúng. Rất nhiều nhân vật mạnh nhất truyện dùng sách ba lá. Số lá nói về loại sức mạnh, không nói về độ mạnh.

[pause] Hiểu lầm hai: năm lá nghĩa là người xấu. Cũng không đúng. Asta là một trong những người tốt bụng nhất truyện. Cuốn sách mang tiếng xấu, nhưng người cầm nó thì không.

[pause] Hiểu lầm ba: cuốn sách quyết định bạn dùng phép gì. Thực ra thuộc tính phép thuộc về chính con người. Grimoire giống một cuốn sổ ghi lại và khuếch đại những gì người đó vốn có.

[pause] Kaku ghi chú: cả ba hiểu lầm đều chung một gốc: tin rằng thứ bên ngoài quyết định giá trị con người. Và đó chính là điều Black Clover muốn phản bác.

[pause] [curious] Giờ tới trò chơi của thủ thư Kaku: nếu bạn bước vào tòa tháp hôm nay, cuốn sách nào sẽ chọn bạn? Chỉ để vui thôi nhé.

[pause] Nếu bạn chăm chỉ, sống chân thành và đặt người khác lên trước, cuốn ba lá là của bạn. Đó cũng là cuốn của hầu hết những người mạnh nhất.

[pause] Nếu bạn luôn thấy mình có vận may kỳ lạ và thích tự đặt mục tiêu thật cao, có khi lá thứ tư đang chờ bạn.

[pause] Còn nếu cả thế giới bảo bạn không làm được, và bạn vẫn không bỏ cuộc, thì có lẽ một cuốn sách năm lá đầy bụi đang tìm đường đến với bạn.

[pause] Kaku thì chắc chắn nhận được một cuốn sổ ghi chép. Không có phép, nhưng ghi được mọi thứ.
```

### c07 · Góc nhìn của Kaku: sức mạnh của người không có gì / Mùa hai: cần nhớ gì? / Mục lục hồ sơ

Khoảng 139 giây · cảnh s75–s90 · 1807 ký tự

**Gemini**

```text
<laugh> Nhìn lại toàn bộ hồ sơ, Kaku thấy Black Clover kể một câu chuyện rất rõ ràng qua hệ thống grimoire.

<short pause> Thế giới này đo giá trị con người bằng ma lực và số lá trên bìa sách. Người sinh ra có nhiều thì được tôn trọng, người sinh ra có ít thì bị coi thường.

<short pause> Asta là câu trả lời ngược lại. Cậu không có ma lực, nhận cuốn sách bị nguyền rủa, vào hội bị coi thường nhất. Mọi chỉ số đều nói cậu sẽ thất bại.

<short pause> Nhưng chính vì không có gì, cậu mới dùng được thứ sức mạnh xóa bỏ các luật cũ. Truyện đang nói rằng hệ thống xếp hạng con người không phải lúc nào cũng đúng.

<short pause> Đó là lý do câu cửa miệng của Asta, không bao giờ bỏ cuộc, nghe có vẻ đơn giản nhưng lại hợp với cả hệ thống sức mạnh đến vậy.

<short pause> Nếu bạn chuẩn bị xem mùa hai, đây là vài điều nên nhớ.

<short pause> Một: mùa hai do Studio Pierrot thực hiện, có hai mươi bốn tập, phát trên Crunchyroll song song với Nhật Bản.

<short pause> Hai: mối quan hệ giữa Asta và ác quỷ trong cuốn sách của cậu sẽ ngày càng quan trọng. Hãy để ý mỗi lần cuốn sách phản ứng.

<short pause> Ba: thẻ số sáu về phản ma thuật chưa phải là tất cả. Luật của nó sẽ còn được mở rộng, và có thể bạn sẽ muốn quay lại xem video này để so sánh.

<short pause> Đóng hồ sơ lại, đây là mục lục của thủ thư Kaku.

<short pause> Grimoire là cuốn sách phép nhận năm mười lăm tuổi. Ma lực là năng lượng của mọi người và cũng là thước đo địa vị.

<short pause> Ba lá là chân thành, hy vọng, tình yêu. Bốn lá là may mắn. Năm lá là nơi ác quỷ trú ngụ.

<short pause> Phản ma thuật xóa phép, đi qua ba thanh kiếm và Dạng Đen, trong tay cậu bé không có chút ma lực nào.

<short pause> Câu hỏi cho bạn: nếu được chọn, bạn muốn nhận cuốn sách mấy lá, và thuộc tính phép của bạn là gì? Viết vào phần bình luận để Kaku lập thẻ cho bạn nhé.

<short pause> Video tới, Kaku rời thư viện để làm việc khác: gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Jujutsu Kaisen.

<short pause> Đăng ký kênh để thẻ thư viện của bạn luôn được gia hạn. Thủ thư Kaku đóng cửa đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Nhìn lại toàn bộ hồ sơ, Kaku thấy Black Clover kể một câu chuyện rất rõ ràng qua hệ thống grimoire.

[pause] Thế giới này đo giá trị con người bằng ma lực và số lá trên bìa sách. Người sinh ra có nhiều thì được tôn trọng, người sinh ra có ít thì bị coi thường.

[pause] Asta là câu trả lời ngược lại. Cậu không có ma lực, nhận cuốn sách bị nguyền rủa, vào hội bị coi thường nhất. Mọi chỉ số đều nói cậu sẽ thất bại.

[pause] Nhưng chính vì không có gì, cậu mới dùng được thứ sức mạnh xóa bỏ các luật cũ. Truyện đang nói rằng hệ thống xếp hạng con người không phải lúc nào cũng đúng.

[pause] Đó là lý do câu cửa miệng của Asta, không bao giờ bỏ cuộc, nghe có vẻ đơn giản nhưng lại hợp với cả hệ thống sức mạnh đến vậy.

[pause] Nếu bạn chuẩn bị xem mùa hai, đây là vài điều nên nhớ.

[pause] Một: mùa hai do Studio Pierrot thực hiện, có hai mươi bốn tập, phát trên Crunchyroll song song với Nhật Bản.

[pause] Hai: mối quan hệ giữa Asta và ác quỷ trong cuốn sách của cậu sẽ ngày càng quan trọng. Hãy để ý mỗi lần cuốn sách phản ứng.

[pause] Ba: thẻ số sáu về phản ma thuật chưa phải là tất cả. Luật của nó sẽ còn được mở rộng, và có thể bạn sẽ muốn quay lại xem video này để so sánh.

[pause] Đóng hồ sơ lại, đây là mục lục của thủ thư Kaku.

[pause] Grimoire là cuốn sách phép nhận năm mười lăm tuổi. Ma lực là năng lượng của mọi người và cũng là thước đo địa vị.

[pause] Ba lá là chân thành, hy vọng, tình yêu. Bốn lá là may mắn. Năm lá là nơi ác quỷ trú ngụ.

[pause] Phản ma thuật xóa phép, đi qua ba thanh kiếm và Dạng Đen, trong tay cậu bé không có chút ma lực nào.

[pause] [curious] Câu hỏi cho bạn: nếu được chọn, bạn muốn nhận cuốn sách mấy lá, và thuộc tính phép của bạn là gì? Viết vào phần bình luận để Kaku lập thẻ cho bạn nhé.

[pause] Video tới, Kaku rời thư viện để làm việc khác: gỡ mười hiểu lầm mà rất nhiều người vẫn tin về Jujutsu Kaisen.

[pause] Đăng ký kênh để thẻ thư viện của bạn luôn được gia hạn. Thủ thư Kaku đóng cửa đây, hẹn gặp lại!
```
