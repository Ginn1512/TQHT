# Bộ prompt · Tougen Anki: Truyền thuyết Momotaro thật và vì sao anh hùng thành kẻ săn quỷ

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 10 đoạn đọc, khoảng 15.9 phút giọng.
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

Lời: Cảnh báo: video có spoiler nhẹ tiền đề của Tougen Anki, tương đương vài tập đầu của anime. Phần lớn video nói…

```text
Wide 16:9 landscape cinematic frame. an old wooden storybook shelf in a quiet room with a single paper lantern glowing beside a closed notebook, wide establishing shot, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Câu chuyện này có thật hơn bạn nghĩ. Một quả đào khổng lồ trôi trên sông. Một bà cụ vớt nó lên. Bên trong là…

```text
Wide 16:9 landscape cinematic frame. a giant peach floating down a gentle river past reeds, an elderly woman kneeling at the bank with a washing basket, wide shot, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Cậu lớn lên, mang theo bánh kê, rủ một con chó, một con khỉ và một con chim trĩ, rồi vượt biển tới đảo Quỷ để…

```text
Wide 16:9 landscape cinematic frame. a young hero silhouette walking on a coastal path with a dog, a monkey and a pheasant following, a distant dark island on the horizon, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Trẻ con Nhật Bản lớn lên với câu chuyện Momotaro, cậu bé quả đào. Anh hùng là Momotaro, còn quỷ là kẻ xấu. Đơ…

```text
Wide 16:9 landscape cinematic frame. a classroom of young children sitting on the floor listening to a teacher holding up a picture scroll, back view, warm afternoon light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Nhưng trong Tougen Anki, hậu duệ của Momotaro lại là những kẻ đi săn, còn hậu duệ của quỷ là những người bị t…

```text
Wide 16:9 landscape cinematic frame. a split composition: an elegant hunter silhouette in a dark suit on the left, a frightened young man with faint glowing horns on the right, dramatic red and navy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Nghe như một bộ anime nổi loạn cố tình đi ngược. Nhưng nếu đọc kỹ lịch sử của truyện cổ tích này, bạn sẽ thấy…

```text
Wide 16:9 landscape cinematic frame. a stack of different book covers of the same folktale from many eras fanned out on a table, top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình lần ngược về truyện Momotaro thật: phiên bản cũ nhất, gốc gác ở đâu,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening an ancient picture scroll on a low wooden table, a small peach resting beside it, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Tougen Anki trong một phút

Lời: Trước hết, tiền đề của Tougen Anki. Ichinose Shiki là một cậu thiếu niên sống bình thường cùng cha nuôi, cho…

```text
Wide 16:9 landscape cinematic frame. a rebellious teenager silhouette and an older man running through a dark suburban street at night, a menacing figure following, wide shot, cold streetlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Từ đó Shiki bước vào một thế giới khác: có trường học dành riêng cho những người trẻ mang máu quỷ, nơi họ học…

```text
Wide 16:9 landscape cinematic frame. a hidden academy building among dark forested hills, a group of young students with faint horn shadows walking through its gate, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Trong khi đó phía Momotaro hoạt động như một cơ quan có tổ chức, có cấp bậc, và coi việc săn quỷ là nhiệm vụ…

```text
Wide 16:9 landscape cinematic frame. an orderly briefing room with silhouettes seated in rows before a large screen displaying a map with red markers, medium shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Kẻ tấn công thuộc về một tổ chức của hậu duệ Momotaro. Và Shiki biết được sự thật: trong người cậu chảy dòng…

```text
Wide 16:9 landscape cinematic frame. a drop of blood falling onto a white floor and blooming into a faint horned shape, extreme close-up, crimson accent. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Điều làm Kaku thấy thú vị nhất là người cha nuôi. Ông mang dòng máu Momotaro, tức là đáng lẽ phải săn quỷ. Nh…

```text
Wide 16:9 landscape cinematic frame. a man holding a sleeping infant in his arms in a dim room, a hunter's weapon leaning forgotten against the wall behind him, medium shot, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Trong thế giới này, quỷ dùng chính máu của mình làm vũ khí: làm nó cứng lại, tạo hình, bắn ra ngoài. Còn phía…

```text
Wide 16:9 landscape cinematic frame. crimson blood forming into a sharp weapon shape above an open palm, opposite a row of disciplined silhouettes in dark uniforms, split composition, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây chỉ là khung câu chuyện. Arc mới đang phát từ tháng mười, và Kaku sẽ không kể nội dung của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a small book with a peach sticker on the cover and putting it aside politely. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Momotaro mà ai cũng biết

Lời: Giờ ta mở truyện cổ tích ra. Phiên bản phổ biến ngày nay bắt đầu với hai ông bà già không có con. Ông lên núi…

```text
Wide 16:9 landscape cinematic frame. a thatched-roof farmhouse at the foot of a mountain, an old man carrying firewood up a path, an old woman walking toward a river, wide shot, peaceful morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Bà thấy một quả đào khổng lồ trôi tới, mang về nhà. Khi hai ông bà định bổ đào, một cậu bé bước ra. Họ đặt tê…

```text
Wide 16:9 landscape cinematic frame. a giant peach split open on a wooden floor, a tiny baby sitting inside it, an elderly couple staring in amazement, medium shot, warm hearth light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Cậu lớn nhanh và khỏe mạnh khác thường. Một ngày, cậu quyết định tới đảo Quỷ, nơi lũ quỷ vẫn hay sang cướp ph…

```text
Wide 16:9 landscape cinematic frame. a strong young man kneeling respectfully before the elderly couple, a small travel bundle beside him, medium shot, soft lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Bà làm cho cậu những chiếc bánh kê. Trên đường đi, cậu chia bánh cho một con chó, một con khỉ và một con chim…

```text
Wide 16:9 landscape cinematic frame. a hand offering small round millet dumplings to a dog, a monkey and a pheasant on a forest path, close-up, dappled sunlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Đây là phiên bản mà gần như mọi người Nhật đều thuộc lòng. Có cả một bài hát thiếu nhi về Momotaro xin bánh k…

```text
Wide 16:9 landscape cinematic frame. a kindergarten classroom with children singing together around a small piano, a picture of a peach on the wall, medium shot, cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng thử đọc lại với con mắt người lớn: Momotaro chưa hề bị quỷ làm hại. Cậu chủ động tới đảo, đánh bại chủ…

```text
Wide 16:9 landscape cinematic frame. a treasure chest overflowing with gold being carried away from a dark island, a small crying shadow watching from a cave entrance, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Cả nhóm vượt biển, đánh bại lũ quỷ, và mang châu báu về làng. Hết truyện. Mọi người sống hạnh phúc.

```text
Wide 16:9 landscape cinematic frame. a small boat returning to a village harbor loaded with treasure chests, villagers cheering on the shore, wide shot, bright victorious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải khen chú chim trĩ. Trong đội có một con chó, một con khỉ, và một con chim chuyên đi mổ mắt quỷ. Nhỏ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot puffing its chest proudly beside a small pheasant, both looking heroic. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Phiên bản cũ hơn: ông bà hóa trẻ

Lời: Nhưng đây mới là phiên bản được chuẩn hóa về sau. Trong phần lớn các văn bản thời Edo, Momotaro không chui ra…

```text
Wide 16:9 landscape cinematic frame. a stack of old woodblock-printed books with worn covers on a scholar's desk, close-up, candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Hai ông bà ăn quả đào, và trẻ lại như thời thanh xuân. Rồi họ sinh ra một đứa con theo cách bình thường. Đứa…

```text
Wide 16:9 landscape cinematic frame. an elderly couple sharing slices of a glowing peach, their silhouettes gradually becoming young again, before-and-after composition, soft golden light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Ở một số vùng, truyện dân gian còn có những phiên bản khác nữa: có nơi kể Momotaro lúc nhỏ rất lười, chỉ chịu…

```text
Wide 16:9 landscape cinematic frame. a lazy young man napping under a tree while villagers stand around him with their hands on their hips, humorous medium shot, afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thích phiên bản này nhất, vì nó cho Kaku hy vọng rằng anh hùng cũng từng ngủ nướng.

```text
Wide 16:9 landscape cinematic frame. the owl mascot yawning under a blanket with a peach-shaped pillow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Vì sao câu chuyện đổi đi? Khi truyện được đưa vào sách giáo khoa luân lý thời Minh Trị, chi tiết hóa trẻ và m…

```text
Wide 16:9 landscape cinematic frame. a Meiji-era classroom with desks in rows and a standardized textbook open on a desk, close-up, cool daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Kaku thấy chi tiết này rất đáng suy nghĩ. Một truyện cổ tích không phải là thứ đứng yên. Nó được kể lại, sửa…

```text
Wide 16:9 landscape cinematic frame. a pair of scissors trimming a paper scroll, small cut-off fragments drifting away, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và nếu truyện đã từng được sửa để phục vụ giáo dục, thì một tác giả hiện đại sửa nó thêm lần nữa cũng là tiếp…

```text
Wide 16:9 landscape cinematic frame. a long line of hands passing the same scroll from one era to the next, each hand dressed differently, horizontal composition, amber light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Gốc Okayama: hoàng tử và quỷ Ura

Lời: Truyện Momotaro gắn với nhiều vùng ở Nhật, nhưng nổi tiếng nhất là tỉnh Okayama. Ở đó có một truyền thuyết cổ…

```text
Wide 16:9 landscape cinematic frame. a misty rural landscape with rice fields and low mountains, an old shrine roof visible among trees, wide establishing shot, soft morning fog. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Theo truyền thuyết, vùng Kibi xưa có một con quỷ tên Ura sống trong một thành đá trên núi, đi cướp phá làng m…

```text
Wide 16:9 landscape cinematic frame. a stone fortress on a mountain ridge under dark clouds, a small army of ancient warriors approaching along a valley road, wide shot, stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Ngày nay ở Okayama vẫn còn di tích một thành cổ trên núi, và người ta gọi nó là Kinojo, nghĩa là thành của qu…

```text
Wide 16:9 landscape cinematic frame. ancient stone fortress walls winding along a misty mountain ridge, a rebuilt wooden gate at the top, wide establishing shot, soft morning fog. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Và ở Okayama có đền Kibitsu, nơi thờ chính vị hoàng tử diệt quỷ. Một truyền thuyết tới giờ vẫn có đền, có thà…

```text
Wide 16:9 landscape cinematic frame. a long covered wooden corridor of an old shrine stretching into the distance under red autumn leaves, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nhiều người tin đây chính là hình mẫu gốc của Momotaro. Ngày nay Okayama vẫn tự gọi mình là quê hương của cậu…

```text
Wide 16:9 landscape cinematic frame. a small bronze statue of a boy with animal companions in front of a modern train station, tourists taking photos, medium shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Nhưng có một chi tiết làm Kaku dừng lại. Vùng Kibi xưa nổi tiếng về luyện sắt. Một số cách diễn giải cho rằng…

```text
Wide 16:9 landscape cinematic frame. an ancient iron smelting furnace glowing in a mountain village, workers silhouetted against the fire, medium shot, orange firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói rõ: đây là cách diễn giải của một số nhà nghiên cứu và câu chuyện địa phương, không phải sự thậ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a paper tag reading interpretation on a string, eyebrows raised seriously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhưng nó mở ra một câu hỏi rất lớn, đúng thứ mà Tougen Anki đặt ra: khi người thắng kể lại câu chuyện, kẻ thu…

```text
Wide 16:9 landscape cinematic frame. a victorious scribe writing on a scroll while a defeated figure's shadow on the wall grows horns, medium shot, dramatic candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Quỷ trong văn hóa Nhật

Lời: Vậy quỷ, hay oni, trong văn hóa Nhật là gì? Hình ảnh quen thuộc nhất là sừng trên đầu, khố bằng da hổ, và cây…

```text
Wide 16:9 landscape cinematic frame. a traditional theatrical demon mask with two horns hanging on a wooden wall beside a spiked iron club, still life, dramatic side light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Có một cách giải thích rất thú vị cho hình ảnh này. Hướng đông bắc được coi là quỷ môn, cửa của quỷ. Trong mư…

```text
Wide 16:9 landscape cinematic frame. an old compass diagram on parchment with the northeast direction highlighted, small ox and tiger icons at that position, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Và giờ tới chi tiết Kaku thích nhất. Hướng ngược lại với quỷ môn là tây nam, ứng với ba con giáp Thân, Dậu, T…

```text
Wide 16:9 landscape cinematic frame. the same compass diagram with the southwest direction now highlighted in gold, small monkey, rooster and dog icons at that position, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Khỉ, một con chim, và chó. Chính là ba người bạn đồng hành của Momotaro. Theo cách giải thích này, đội hình c…

```text
Wide 16:9 landscape cinematic frame. a monkey, a pheasant and a dog standing in formation facing a horned shadow across the compass diagram, parchment illustration, warm light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói rõ: đây là cách giải thích phổ biến, được nhắc nhiều ở Nhật, nhưng không ai chắc người kể truyệ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a small star sticker labeled popular theory next to the compass diagram. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Sừng trâu và da hổ. Quỷ được vẽ theo đúng hướng mà nó được cho là đi vào. Kaku không biết có đúng hoàn toàn k…

```text
Wide 16:9 landscape cinematic frame. an ox horn and a tiger-striped cloth placed side by side under a single spotlight, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Có cả những hòn đảo thật tự nhận là đảo Quỷ. Một hòn đảo nhỏ ở biển nội địa Seto có hang động lớn, và người t…

```text
Wide 16:9 landscape cinematic frame. a small green island in a calm inland sea with a dark cave entrance on its hillside, tourists walking on a path toward it, wide shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Mỗi năm vào dịp tiết Phân, người Nhật ném đậu ra cửa và hô quỷ ra ngoài, phúc vào nhà. Quỷ là thứ bị đẩy ra n…

```text
Wide 16:9 landscape cinematic frame. a family tossing roasted beans out of an open door at dusk, a small shadow of horns fleeing outside, medium shot, warm interior light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Và đó là chìa khóa: trong nhiều câu chuyện, quỷ đại diện cho những gì ở bên ngoài: người lạ, kẻ nổi loạn, ngư…

```text
Wide 16:9 landscape cinematic frame. a door half open, warm light inside with a family, a lonely silhouette with faint horns standing in the cold outside, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng văn hóa Nhật cũng có những câu chuyện về quỷ tốt bụng, quỷ khóc vì bị hiểu lầm. Quỷ không phải lúc nào…

```text
Wide 16:9 landscape cinematic frame. a large gentle demon silhouette sitting alone on a hillside, a small flower in its giant hand, wide shot, melancholic sunset. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Akutagawa: người lật ngược đầu tiên

Lời: Năm 1924, nhà văn Akutagawa Ryunosuke, người mà giải văn học lớn nhất Nhật Bản mang tên, đăng một truyện ngắn…

```text
Wide 16:9 landscape cinematic frame. a 1920s writer's desk with a fountain pen, ink bottle and newspaper pages, a small peach sketch in the margin, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Ông viết rằng lũ quỷ ở đó chơi đàn, múa hát, và kể cho nhau nghe chuyện về con người như kể chuyện ma. Con ng…

```text
Wide 16:9 landscape cinematic frame. a group of gentle horned figures sitting around a campfire telling scary stories, one shaping a human silhouette with its hands in the smoke, medium shot, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Trong truyện của Akutagawa, đảo Quỷ là một hòn đảo yên bình. Lũ quỷ sống hiền hòa, yêu âm nhạc, yêu gia đình.

```text
Wide 16:9 landscape cinematic frame. a peaceful tropical island village with gentle horned figures playing music and children playing on the beach, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Truyện kết thúc không có đoạn sống hạnh phúc mãi mãi. Những con quỷ sống sót ôm hận, và mối thù ấy được hứa h…

```text
Wide 16:9 landscape cinematic frame. a small horned child silhouette standing on a ruined beach looking at a departing boat on the horizon, wide shot, cold grey dusk. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Momotaro tới xâm chiếm hòn đảo đó, không vì lý do chính đáng nào, và những con vật đi theo cậu chỉ vì được tr…

```text
Wide 16:9 landscape cinematic frame. a dark silhouette with three animal shadows arriving on a beach at night with torches, frightened villagers watching from the trees, wide shot, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Đây là một truyện châm biếm tinh thần chiến tranh và bành trướng lúc bấy giờ. Akutagawa dùng chính câu chuyện…

```text
Wide 16:9 landscape cinematic frame. a newspaper page with a satirical ink cartoon of a boy marching with a flag, close-up, sepia tones. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kaku thấy tác giả Tougen Anki đi cùng một hướng. Có thể không phải bắt chước, nhưng rõ ràng câu hỏi ấy đã nằm…

```text
Wide 16:9 landscape cinematic frame. two books side by side, one old and worn, one modern, both with a peach symbol on the cover, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Momotaro ra trận

Lời: Rồi có một mặt ngược lại. Trong Thế chiến thứ hai, Momotaro được dùng làm biểu tượng tuyên truyền. Quỷ trở th…

```text
Wide 16:9 landscape cinematic frame. a faded wartime poster style illustration of a boy hero leading animal soldiers, rendered in muted sepia, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Trong phim, Momotaro chỉ huy những con vật đáng yêu trong vai binh lính. Lũ quỷ đại diện cho kẻ thù ngoại quố…

```text
Wide 16:9 landscape cinematic frame. a row of cute animal silhouettes in sailor caps marching in line under a flag, rendered as a faded vintage cartoon still, wide shot, sepia tones. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Năm 1945, bộ phim hoạt hình dài đầu tiên của Nhật ra đời, tên là Momotaro: Thần binh trên biển. Đó là một bộ…

```text
Wide 16:9 landscape cinematic frame. an old film projector casting light onto a screen in a dark cinema, rows of empty wooden seats, wide shot, flickering light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Nghĩa là lịch sử anime có một điểm khởi đầu rất lạ: phim hoạt hình dài đầu tiên của Nhật kể về Momotaro và nh…

```text
Wide 16:9 landscape cinematic frame. a single frame of old film strip glowing against darkness, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cùng một câu chuyện, một người dùng để cổ vũ chiến tranh, một người dùng để phê phán chiến tran…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two identical scrolls, one tied with a red ribbon and one with a white ribbon, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Tougen Anki lật ngược những gì

Lời: Giờ quay lại Tougen Anki. Thứ nhất, tác giả biến Momotaro từ một người anh hùng thành cả một dòng máu, một tổ…

```text
Wide 16:9 landscape cinematic frame. a sleek corporate building lobby with a subtle peach emblem on the wall, rows of disciplined silhouettes in dark suits, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nghĩa là không còn đảo Quỷ ở xa ngoài biển nữa. Ranh giới giữa bên trong và bên ngoài cánh cửa giờ nằm ngay t…

```text
Wide 16:9 landscape cinematic frame. a modern apartment building at night, one window glowing red among many warm yellow windows, wide shot, quiet urban light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Thứ hai, quỷ không còn là con quái vật ngoài đảo. Họ là người sống lẫn trong xã hội, nhiều người không hề biế…

```text
Wide 16:9 landscape cinematic frame. an ordinary city crosswalk crowd, one person in the middle with faint translucent horns only visible in their reflection on a shop window, medium shot, daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Thứ ba, trong truyện gốc quỷ bị đánh và bị cướp châu báu. Trong Tougen Anki, hậu duệ quỷ bị truy đuổi chỉ vì…

```text
Wide 16:9 landscape cinematic frame. a young person running through rain at night, their shadow on the wall showing horns while their own figure looks completely ordinary, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và phía Momotaro cũng không phải ai cũng giống ai. Truyện cho thấy trong mỗi phe đều có người tàn nhẫn và ngư…

```text
Wide 16:9 landscape cinematic frame. two groups of silhouettes facing each other, a few individuals on each side stepping slightly forward with open hands, wide shot, balanced warm and cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Thứ tư, và đây là chỗ tinh tế nhất: dòng máu không quyết định tất cả. Người cha nuôi mang máu Momotaro nhưng…

```text
Wide 16:9 landscape cinematic frame. a large hand and a small hand holding each other, one with a faint peach-pink glow and one with a faint crimson glow, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và tên truyện, Tougen Anki, có chữ Đào Nguyên, nghĩa là vườn đào tiên, chốn thiên đường. Nhưng đi kèm với nó…

```text
Wide 16:9 landscape cinematic frame. a beautiful peach orchard in full bloom with a single dark horned shadow standing between the trees, wide shot, pink and navy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku để ý thêm một điều: năng lực của quỷ trong truyện đến từ chính dòng máu. Như thể thứ khiến họ bị săn đuổ…

```text
Wide 16:9 landscape cinematic frame. a single drop of crimson blood suspended above a palm, glowing and forming a small shield shape, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Vì sao phải lật ngược · **Kaku** (đính kèm ảnh mẫu)

Lời: Tại sao tác giả hiện đại lại thích lật ngược truyện cổ tích? Kaku nghĩ có ba lý do.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up three fingers in front of a chalkboard with a peach drawn upside down. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Một: người đọc hôm nay không còn chấp nhận câu chuyện có kẻ xấu chỉ vì họ trông khác. Chúng ta muốn biết lý d…

```text
Wide 16:9 landscape cinematic frame. two people sitting across a table in conversation, one with faint horns, both listening intently, medium shot, warm café light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hai: truyện cổ tích quá quen, nên lật ngược nó là cách nhanh nhất để gây bất ngờ. Người Nhật nghe tên Momotar…

```text
Wide 16:9 landscape cinematic frame. a familiar picture book cover being turned around on a table to reveal a darker version on the back, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Kaku nghĩ đây cũng là lý do truyện được yêu thích ngoài Nhật Bản: câu chuyện về người bị ghét chỉ vì nguồn gố…

```text
Wide 16:9 landscape cinematic frame. readers from different backgrounds holding the same book on a crowded train, each absorbed in reading, medium shot, soft daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Ba: câu hỏi ai là quỷ vẫn luôn đúng với thời nào cũng vậy. Mỗi xã hội đều có những người bị coi là quỷ chỉ vì…

```text
Wide 16:9 landscape cinematic frame. a line drawn on the ground separating a crowd from a small group of outsiders, both sides looking wary, top-down wide shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và đây là lý do dạng video này tồn tại trên kênh: hiểu câu chuyện gốc, bạn sẽ thấy anime hay hơn nhiều, vì bạ…

```text
Wide 16:9 landscape cinematic frame. a reader holding a modern manga in one hand and an old folktale book in the other, reading both, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Bản đồ thật và hư cấu

Lời: Kaku gom lại thành một tấm bản đồ. Cột bên trái là những gì có thật trong văn hóa và lịch sử.

```text
Wide 16:9 landscape cinematic frame. a large parchment map divided into two columns, the left side illustrated with a shrine, a scroll and an iron furnace, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Cũng ở cột có thật: di tích thành cổ ở Okayama gắn với truyền thuyết quỷ Ura, và cách giải thích chó, khỉ, ch…

```text
Wide 16:9 landscape cinematic frame. a small fortress wall icon and a compass icon on the left column of the map, one with a tiny label tag, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Có thật: truyện Momotaro với chó, khỉ, chim trĩ và bánh kê. Phiên bản cũ ông bà hóa trẻ. Truyền thuyết Kibits…

```text
Wide 16:9 landscape cinematic frame. small icons on the left column of the map: a peach, three animals, a shrine and a handful of beans, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Cũng có thật: truyện châm biếm năm 1924 của Akutagawa, và bộ phim hoạt hình tuyên truyền năm 1945.

```text
Wide 16:9 landscape cinematic frame. a newspaper and a film reel drawn on the left column of the map, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Cột bên phải là sáng tạo của Tougen Anki: hai dòng máu Momotaro và quỷ di truyền tới ngày nay, năng lực điều…

```text
Wide 16:9 landscape cinematic frame. the right column of the map illustrated with a blood drop, a corporate emblem and two clasped hands, close-up, crimson and navy. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và ở giữa hai cột, Kaku vẽ một mũi tên: câu hỏi ai mới thật sự là quỷ. Câu hỏi đó đi từ truyền thuyết cổ, qua…

```text
Wide 16:9 landscape cinematic frame. a glowing arrow crossing from the left column to the right column of the map with a question mark at its center, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Kết

Lời: Một quả đào trôi trên sông đã đi một hành trình dài hơn bất kỳ ai tưởng: từ truyền thuyết địa phương, vào sác…

```text
Wide 16:9 landscape cinematic frame. a giant peach floating down a river that flows through different eras: ancient villages, a Meiji town, a modern city at night, wide panoramic shot, warm to cool light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hãy nhớ lần sau nghe ai đó kể một câu chuyện có anh hùng và quỷ: thử hỏi xem ai đang cầm bút, và câu chuyện đ…

```text
Wide 16:9 landscape cinematic frame. a brush pen resting on an unfinished scroll where a hero and a demon are drawn side by side, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Nếu bạn là người kể lại truyện Momotaro, bạn sẽ đứng về phía ai? Viết phiên bản một câu của bạn vào bình luận…

```text
Wide 16:9 landscape cinematic frame. an empty scroll and a brush waiting on a low table beside a peach, top-down shot, inviting warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tiếp theo, Kaku quay lại với một trận đấu kinh điển: Ichigo đối đầu Byakuya. Kaku sẽ chia trận đấu thàn…

```text
Wide 16:9 landscape cinematic frame. two sword-wielding silhouettes facing each other on a tall white tower under a storm of falling cherry blossom petals, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video đào ngược về nguồn gốc thật như thế này, hãy đăng ký kênh để không bỏ lỡ. Kaku gấp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the ancient scroll, placing a peach on top, and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 81 giây · cảnh s01–s07 · 1052 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler nhẹ tiền đề của Tougen Anki, tương đương vài tập đầu của anime. Phần lớn video nói về truyện cổ tích thật, nên ai chưa xem vẫn theo được.

<short pause> Câu chuyện này có thật hơn bạn nghĩ. Một quả đào khổng lồ trôi trên sông. Một bà cụ vớt nó lên. Bên trong là một cậu bé.

<short pause> Cậu lớn lên, mang theo bánh kê, rủ một con chó, một con khỉ và một con chim trĩ, rồi vượt biển tới đảo Quỷ để diệt lũ quỷ và mang châu báu về làng.

<short pause> Trẻ con Nhật Bản lớn lên với câu chuyện Momotaro, cậu bé quả đào. Anh hùng là Momotaro, còn quỷ là kẻ xấu. Đơn giản vậy thôi.

<short pause> Nhưng trong Tougen Anki, hậu duệ của Momotaro lại là những kẻ đi săn, còn hậu duệ của quỷ là những người bị truy đuổi. Tác giả lật ngược cả truyện cổ tích.

<short pause> Nghe như một bộ anime nổi loạn cố tình đi ngược. <short pause> Nhưng nếu đọc kỹ lịch sử của truyện cổ tích này, bạn sẽ thấy nó từng bị kể lại theo đủ mọi hướng.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình lần ngược về truyện Momotaro thật: phiên bản cũ nhất, gốc gác ở đâu, quỷ là ai. Và bạn sẽ thấy tác giả Tougen Anki không phải người đầu tiên lật ngược nó.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler nhẹ tiền đề của Tougen Anki, tương đương vài tập đầu của anime. Phần lớn video nói về truyện cổ tích thật, nên ai chưa xem vẫn theo được.

[pause] Câu chuyện này có thật hơn bạn nghĩ. Một quả đào khổng lồ trôi trên sông. Một bà cụ vớt nó lên. Bên trong là một cậu bé.

[pause] Cậu lớn lên, mang theo bánh kê, rủ một con chó, một con khỉ và một con chim trĩ, rồi vượt biển tới đảo Quỷ để diệt lũ quỷ và mang châu báu về làng.

[pause] Trẻ con Nhật Bản lớn lên với câu chuyện Momotaro, cậu bé quả đào. Anh hùng là Momotaro, còn quỷ là kẻ xấu. Đơn giản vậy thôi.

[pause] Nhưng trong Tougen Anki, hậu duệ của Momotaro lại là những kẻ đi săn, còn hậu duệ của quỷ là những người bị truy đuổi. Tác giả lật ngược cả truyện cổ tích.

[pause] Nghe như một bộ anime nổi loạn cố tình đi ngược. [pause] Nhưng nếu đọc kỹ lịch sử của truyện cổ tích này, bạn sẽ thấy nó từng bị kể lại theo đủ mọi hướng.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình lần ngược về truyện Momotaro thật: phiên bản cũ nhất, gốc gác ở đâu, quỷ là ai. Và bạn sẽ thấy tác giả Tougen Anki không phải người đầu tiên lật ngược nó.
```

### c02 · Tougen Anki trong một phút

Khoảng 77 giây · cảnh s08–s14 · 1006 ký tự

**Gemini**

```text
Trước hết, tiền đề của Tougen Anki. Ichinose Shiki là một cậu thiếu niên sống bình thường cùng cha nuôi, cho tới ngày bị một người đàn ông bí ẩn tấn công.

<short pause> Từ đó Shiki bước vào một thế giới khác: có trường học dành riêng cho những người trẻ mang máu quỷ, nơi họ học cách sống sót và chiến đấu.

<short pause> Trong khi đó phía Momotaro hoạt động như một cơ quan có tổ chức, có cấp bậc, và coi việc săn quỷ là nhiệm vụ bảo vệ xã hội.

<short pause> Kẻ tấn công thuộc về một tổ chức của hậu duệ Momotaro. Và Shiki biết được sự thật: trong người cậu chảy dòng máu của quỷ.

<short pause> Điều làm Kaku thấy thú vị nhất là người cha nuôi. Ông mang dòng máu Momotaro, tức là đáng lẽ phải săn quỷ. <short pause> Nhưng ông đã không giết đứa trẻ sơ sinh ấy, mà nhận nuôi và yêu thương cậu.

<short pause> Trong thế giới này, quỷ dùng chính máu của mình làm vũ khí: làm nó cứng lại, tạo hình, bắn ra ngoài. Còn phía Momotaro có năng lực riêng và cả một tổ chức lớn, có kỷ luật.

<short pause> <laugh> Kaku ghi chú: đây chỉ là khung câu chuyện. Arc mới đang phát từ tháng mười, và Kaku sẽ không kể nội dung của nó ở đây.
```

**ElevenLabs**

```text
Trước hết, tiền đề của Tougen Anki. Ichinose Shiki là một cậu thiếu niên sống bình thường cùng cha nuôi, cho tới ngày bị một người đàn ông bí ẩn tấn công.

[pause] Từ đó Shiki bước vào một thế giới khác: có trường học dành riêng cho những người trẻ mang máu quỷ, nơi họ học cách sống sót và chiến đấu.

[pause] Trong khi đó phía Momotaro hoạt động như một cơ quan có tổ chức, có cấp bậc, và coi việc săn quỷ là nhiệm vụ bảo vệ xã hội.

[pause] Kẻ tấn công thuộc về một tổ chức của hậu duệ Momotaro. Và Shiki biết được sự thật: trong người cậu chảy dòng máu của quỷ.

[pause] Điều làm Kaku thấy thú vị nhất là người cha nuôi. Ông mang dòng máu Momotaro, tức là đáng lẽ phải săn quỷ. [pause] Nhưng ông đã không giết đứa trẻ sơ sinh ấy, mà nhận nuôi và yêu thương cậu.

[pause] Trong thế giới này, quỷ dùng chính máu của mình làm vũ khí: làm nó cứng lại, tạo hình, bắn ra ngoài. Còn phía Momotaro có năng lực riêng và cả một tổ chức lớn, có kỷ luật.

[pause] [chuckles] Kaku ghi chú: đây chỉ là khung câu chuyện. Arc mới đang phát từ tháng mười, và Kaku sẽ không kể nội dung của nó ở đây.
```

### c03 · Momotaro mà ai cũng biết

Khoảng 86 giây · cảnh s15–s22 · 1124 ký tự

**Gemini**

```text
Giờ ta mở truyện cổ tích ra. Phiên bản phổ biến ngày nay bắt đầu với hai ông bà già không có con. Ông lên núi đốn củi, bà ra sông giặt đồ.

<short pause> Bà thấy một quả đào khổng lồ trôi tới, mang về nhà. Khi hai ông bà định bổ đào, một cậu bé bước ra. Họ đặt tên là Momotaro, nghĩa là cậu con trai quả đào.

<short pause> Cậu lớn nhanh và khỏe mạnh khác thường. Một ngày, cậu quyết định tới đảo Quỷ, nơi lũ quỷ vẫn hay sang cướp phá làng.

<short pause> Bà làm cho cậu những chiếc bánh kê. Trên đường đi, cậu chia bánh cho một con chó, một con khỉ và một con chim trĩ, đổi lấy việc chúng đi theo cậu.

<short pause> Đây là phiên bản mà gần như mọi người Nhật đều thuộc lòng. Có cả một bài hát thiếu nhi về Momotaro xin bánh kê, mà trẻ con hát từ thời mẫu giáo.

<short pause> Nhưng thử đọc lại với con mắt người lớn: Momotaro chưa hề bị quỷ làm hại. Cậu chủ động tới đảo, đánh bại chủ đảo, và mang của cải về. Chính chi tiết này sau này sẽ bị lật ngược.

<short pause> Cả nhóm vượt biển, đánh bại lũ quỷ, và mang châu báu về làng. Hết truyện. Mọi người sống hạnh phúc.

<short pause> <laugh> Kaku phải khen chú chim trĩ. Trong đội có một con chó, một con khỉ, và một con chim chuyên đi mổ mắt quỷ. Nhỏ mà có võ, giống Kaku lúc bị hỏi bài khó.
```

**ElevenLabs**

```text
Giờ ta mở truyện cổ tích ra. Phiên bản phổ biến ngày nay bắt đầu với hai ông bà già không có con. Ông lên núi đốn củi, bà ra sông giặt đồ.

[pause] Bà thấy một quả đào khổng lồ trôi tới, mang về nhà. Khi hai ông bà định bổ đào, một cậu bé bước ra. Họ đặt tên là Momotaro, nghĩa là cậu con trai quả đào.

[pause] Cậu lớn nhanh và khỏe mạnh khác thường. Một ngày, cậu quyết định tới đảo Quỷ, nơi lũ quỷ vẫn hay sang cướp phá làng.

[pause] Bà làm cho cậu những chiếc bánh kê. Trên đường đi, cậu chia bánh cho một con chó, một con khỉ và một con chim trĩ, đổi lấy việc chúng đi theo cậu.

[pause] Đây là phiên bản mà gần như mọi người Nhật đều thuộc lòng. Có cả một bài hát thiếu nhi về Momotaro xin bánh kê, mà trẻ con hát từ thời mẫu giáo.

[pause] Nhưng thử đọc lại với con mắt người lớn: Momotaro chưa hề bị quỷ làm hại. Cậu chủ động tới đảo, đánh bại chủ đảo, và mang của cải về. Chính chi tiết này sau này sẽ bị lật ngược.

[pause] Cả nhóm vượt biển, đánh bại lũ quỷ, và mang châu báu về làng. Hết truyện. Mọi người sống hạnh phúc.

[pause] [chuckles] Kaku phải khen chú chim trĩ. Trong đội có một con chó, một con khỉ, và một con chim chuyên đi mổ mắt quỷ. Nhỏ mà có võ, giống Kaku lúc bị hỏi bài khó.
```

### c04 · Phiên bản cũ hơn: ông bà hóa trẻ

Khoảng 76 giây · cảnh s23–s29 · 992 ký tự

**Gemini**

```text
Nhưng đây mới là phiên bản được chuẩn hóa về sau. Trong phần lớn các văn bản thời Edo, Momotaro không chui ra từ quả đào.

<short pause> Hai ông bà ăn quả đào, và trẻ lại như thời thanh xuân. Rồi họ sinh ra một đứa con theo cách bình thường. Đứa con ấy là Momotaro.

<short pause> Ở một số vùng, truyện dân gian còn có những phiên bản khác nữa: có nơi kể Momotaro lúc nhỏ rất lười, chỉ chịu ra khỏi nhà khi bị cả làng thúc giục.

<short pause> <laugh> Kaku thích phiên bản này nhất, vì nó cho Kaku hy vọng rằng anh hùng cũng từng ngủ nướng.

<short pause> Vì sao câu chuyện đổi đi? Khi truyện được đưa vào sách giáo khoa luân lý thời Minh Trị, chi tiết hóa trẻ và mang thai bị coi là không phù hợp với trẻ em. Phiên bản sinh ra từ quả đào trở thành bản chính thức.

<short pause> Kaku thấy chi tiết này rất đáng suy nghĩ. Một truyện cổ tích không phải là thứ đứng yên. Nó được kể lại, sửa lại, và cắt gọt theo điều người lớn muốn trẻ con tin.

<short pause> Và nếu truyện đã từng được sửa để phục vụ giáo dục, thì một tác giả hiện đại sửa nó thêm lần nữa cũng là tiếp nối một truyền thống rất cũ.
```

**ElevenLabs**

```text
Nhưng đây mới là phiên bản được chuẩn hóa về sau. Trong phần lớn các văn bản thời Edo, Momotaro không chui ra từ quả đào.

[pause] Hai ông bà ăn quả đào, và trẻ lại như thời thanh xuân. Rồi họ sinh ra một đứa con theo cách bình thường. Đứa con ấy là Momotaro.

[pause] Ở một số vùng, truyện dân gian còn có những phiên bản khác nữa: có nơi kể Momotaro lúc nhỏ rất lười, chỉ chịu ra khỏi nhà khi bị cả làng thúc giục.

[pause] [chuckles] Kaku thích phiên bản này nhất, vì nó cho Kaku hy vọng rằng anh hùng cũng từng ngủ nướng.

[pause] [curious] Vì sao câu chuyện đổi đi? Khi truyện được đưa vào sách giáo khoa luân lý thời Minh Trị, chi tiết hóa trẻ và mang thai bị coi là không phù hợp với trẻ em. Phiên bản sinh ra từ quả đào trở thành bản chính thức.

[pause] Kaku thấy chi tiết này rất đáng suy nghĩ. Một truyện cổ tích không phải là thứ đứng yên. Nó được kể lại, sửa lại, và cắt gọt theo điều người lớn muốn trẻ con tin.

[pause] Và nếu truyện đã từng được sửa để phục vụ giáo dục, thì một tác giả hiện đại sửa nó thêm lần nữa cũng là tiếp nối một truyền thống rất cũ.
```

### c05 · Gốc Okayama: hoàng tử và quỷ Ura

Khoảng 97 giây · cảnh s30–s37 · 1265 ký tự

**Gemini**

```text
Truyện Momotaro gắn với nhiều vùng ở Nhật, nhưng nổi tiếng nhất là tỉnh Okayama. Ở đó có một truyền thuyết cổ hơn nhiều về một vị hoàng tử tên Kibitsuhiko.

<short pause> Theo truyền thuyết, vùng Kibi xưa có một con quỷ tên Ura sống trong một thành đá trên núi, đi cướp phá làng mạc. Triều đình Yamato cử hoàng tử Kibitsuhiko tới diệt quỷ.

<short pause> Ngày nay ở Okayama vẫn còn di tích một thành cổ trên núi, và người ta gọi nó là Kinojo, nghĩa là thành của quỷ. Truyền thuyết nói đó chính là nơi quỷ Ura từng sống.

<short pause> Và ở Okayama có đền Kibitsu, nơi thờ chính vị hoàng tử diệt quỷ. Một truyền thuyết tới giờ vẫn có đền, có thành, có lễ hội.

<short pause> Nhiều người tin đây chính là hình mẫu gốc của Momotaro. Ngày nay Okayama vẫn tự gọi mình là quê hương của cậu bé quả đào, có tượng, có lễ hội, và bánh kê là đặc sản.

<short pause> Nhưng có một chi tiết làm Kaku dừng lại. Vùng Kibi xưa nổi tiếng về luyện sắt. Một số cách diễn giải cho rằng những kẻ bị gọi là quỷ có thể là những người từ nơi khác đến, mang theo kỹ thuật và quyền lực riêng.

<short pause> <laugh> Kaku phải nói rõ: đây là cách diễn giải của một số nhà nghiên cứu và câu chuyện địa phương, không phải sự thật lịch sử đã được chứng minh.

<short pause> Nhưng nó mở ra một câu hỏi rất lớn, đúng thứ mà Tougen Anki đặt ra: khi người thắng kể lại câu chuyện, kẻ thua sẽ trở thành gì trong trang sử?
```

**ElevenLabs**

```text
Truyện Momotaro gắn với nhiều vùng ở Nhật, nhưng nổi tiếng nhất là tỉnh Okayama. Ở đó có một truyền thuyết cổ hơn nhiều về một vị hoàng tử tên Kibitsuhiko.

[pause] Theo truyền thuyết, vùng Kibi xưa có một con quỷ tên Ura sống trong một thành đá trên núi, đi cướp phá làng mạc. Triều đình Yamato cử hoàng tử Kibitsuhiko tới diệt quỷ.

[pause] Ngày nay ở Okayama vẫn còn di tích một thành cổ trên núi, và người ta gọi nó là Kinojo, nghĩa là thành của quỷ. Truyền thuyết nói đó chính là nơi quỷ Ura từng sống.

[pause] Và ở Okayama có đền Kibitsu, nơi thờ chính vị hoàng tử diệt quỷ. Một truyền thuyết tới giờ vẫn có đền, có thành, có lễ hội.

[pause] Nhiều người tin đây chính là hình mẫu gốc của Momotaro. Ngày nay Okayama vẫn tự gọi mình là quê hương của cậu bé quả đào, có tượng, có lễ hội, và bánh kê là đặc sản.

[pause] Nhưng có một chi tiết làm Kaku dừng lại. Vùng Kibi xưa nổi tiếng về luyện sắt. Một số cách diễn giải cho rằng những kẻ bị gọi là quỷ có thể là những người từ nơi khác đến, mang theo kỹ thuật và quyền lực riêng.

[pause] [chuckles] Kaku phải nói rõ: đây là cách diễn giải của một số nhà nghiên cứu và câu chuyện địa phương, không phải sự thật lịch sử đã được chứng minh.

[pause] [curious] Nhưng nó mở ra một câu hỏi rất lớn, đúng thứ mà Tougen Anki đặt ra: khi người thắng kể lại câu chuyện, kẻ thua sẽ trở thành gì trong trang sử?
```

### c06 · Quỷ trong văn hóa Nhật

Khoảng 116 giây · cảnh s38–s47 · 1509 ký tự

**Gemini**

```text
Vậy quỷ, hay oni, trong văn hóa Nhật là gì? Hình ảnh quen thuộc nhất là sừng trên đầu, khố bằng da hổ, và cây gậy sắt có gai.

<short pause> Có một cách giải thích rất thú vị cho hình ảnh này. Hướng đông bắc được coi là quỷ môn, cửa của quỷ. Trong mười hai con giáp, hướng đó là giữa Sửu và Dần, tức là trâu và hổ.

<short pause> Và giờ tới chi tiết Kaku thích nhất. Hướng ngược lại với quỷ môn là tây nam, ứng với ba con giáp Thân, Dậu, Tuất: khỉ, gà, chó.

<short pause> Khỉ, một con chim, và chó. Chính là ba người bạn đồng hành của Momotaro. Theo cách giải thích này, đội hình của cậu bé quả đào được chọn từ hướng khắc chế quỷ.

<short pause> <laugh> Kaku phải nói rõ: đây là cách giải thích phổ biến, được nhắc nhiều ở Nhật, nhưng không ai chắc người kể truyện đầu tiên đã nghĩ như vậy. Dù sao thì nó quá đẹp để không kể.

<short pause> Sừng trâu và da hổ. Quỷ được vẽ theo đúng hướng mà nó được cho là đi vào. Kaku không biết có đúng hoàn toàn không, nhưng đây là cách giải thích phổ biến ở Nhật.

<short pause> Có cả những hòn đảo thật tự nhận là đảo Quỷ. Một hòn đảo nhỏ ở biển nội địa Seto có hang động lớn, và người ta đón khách du lịch tới xem hang của quỷ.

<short pause> Mỗi năm vào dịp tiết Phân, người Nhật ném đậu ra cửa và hô quỷ ra ngoài, phúc vào nhà. Quỷ là thứ bị đẩy ra ngoài ranh giới.

<short pause> Và đó là chìa khóa: trong nhiều câu chuyện, quỷ đại diện cho những gì ở bên ngoài: người lạ, kẻ nổi loạn, người bị gạt ra lề. Ai được gọi là quỷ phụ thuộc vào ai đứng bên trong cánh cửa.

<short pause> Nhưng văn hóa Nhật cũng có những câu chuyện về quỷ tốt bụng, quỷ khóc vì bị hiểu lầm. Quỷ không phải lúc nào cũng là cái ác thuần túy.
```

**ElevenLabs**

```text
[curious] Vậy quỷ, hay oni, trong văn hóa Nhật là gì? Hình ảnh quen thuộc nhất là sừng trên đầu, khố bằng da hổ, và cây gậy sắt có gai.

[pause] Có một cách giải thích rất thú vị cho hình ảnh này. Hướng đông bắc được coi là quỷ môn, cửa của quỷ. Trong mười hai con giáp, hướng đó là giữa Sửu và Dần, tức là trâu và hổ.

[pause] Và giờ tới chi tiết Kaku thích nhất. Hướng ngược lại với quỷ môn là tây nam, ứng với ba con giáp Thân, Dậu, Tuất: khỉ, gà, chó.

[pause] Khỉ, một con chim, và chó. Chính là ba người bạn đồng hành của Momotaro. Theo cách giải thích này, đội hình của cậu bé quả đào được chọn từ hướng khắc chế quỷ.

[pause] [chuckles] Kaku phải nói rõ: đây là cách giải thích phổ biến, được nhắc nhiều ở Nhật, nhưng không ai chắc người kể truyện đầu tiên đã nghĩ như vậy. Dù sao thì nó quá đẹp để không kể.

[pause] Sừng trâu và da hổ. Quỷ được vẽ theo đúng hướng mà nó được cho là đi vào. Kaku không biết có đúng hoàn toàn không, nhưng đây là cách giải thích phổ biến ở Nhật.

[pause] Có cả những hòn đảo thật tự nhận là đảo Quỷ. Một hòn đảo nhỏ ở biển nội địa Seto có hang động lớn, và người ta đón khách du lịch tới xem hang của quỷ.

[pause] Mỗi năm vào dịp tiết Phân, người Nhật ném đậu ra cửa và hô quỷ ra ngoài, phúc vào nhà. Quỷ là thứ bị đẩy ra ngoài ranh giới.

[pause] Và đó là chìa khóa: trong nhiều câu chuyện, quỷ đại diện cho những gì ở bên ngoài: người lạ, kẻ nổi loạn, người bị gạt ra lề. Ai được gọi là quỷ phụ thuộc vào ai đứng bên trong cánh cửa.

[pause] Nhưng văn hóa Nhật cũng có những câu chuyện về quỷ tốt bụng, quỷ khóc vì bị hiểu lầm. Quỷ không phải lúc nào cũng là cái ác thuần túy.
```

### c07 · Akutagawa: người lật ngược đầu tiên / Momotaro ra trận

Khoảng 138 giây · cảnh s48–s59 · 1788 ký tự

**Gemini**

```text
Năm 1924, nhà văn Akutagawa Ryunosuke, người mà giải văn học lớn nhất Nhật Bản mang tên, đăng một truyện ngắn tên là Momotaro. Và ông đã làm đúng điều Tougen Anki làm, trước gần một trăm năm.

<short pause> Ông viết rằng lũ quỷ ở đó chơi đàn, múa hát, và kể cho nhau nghe chuyện về con người như kể chuyện ma. Con người mới là thứ đáng sợ trong mắt quỷ.

<short pause> Trong truyện của Akutagawa, đảo Quỷ là một hòn đảo yên bình. Lũ quỷ sống hiền hòa, yêu âm nhạc, yêu gia đình.

<short pause> Truyện kết thúc không có đoạn sống hạnh phúc mãi mãi. Những con quỷ sống sót ôm hận, và mối thù ấy được hứa hẹn sẽ còn tiếp diễn.

<short pause> Momotaro tới xâm chiếm hòn đảo đó, không vì lý do chính đáng nào, và những con vật đi theo cậu chỉ vì được trả công. Người anh hùng bị kể lại như một kẻ xâm lược.

<short pause> Đây là một truyện châm biếm tinh thần chiến tranh và bành trướng lúc bấy giờ. Akutagawa dùng chính câu chuyện mà ai cũng yêu để đặt ra câu hỏi: có thật kẻ thắng luôn đúng?

<short pause> Kaku thấy tác giả Tougen Anki đi cùng một hướng. Có thể không phải bắt chước, nhưng rõ ràng câu hỏi ấy đã nằm trong truyện cổ tích từ rất lâu.

<short pause> Rồi có một mặt ngược lại. Trong Thế chiến thứ hai, Momotaro được dùng làm biểu tượng tuyên truyền. Quỷ trở thành hình ảnh của kẻ thù bên ngoài.

<short pause> Trong phim, Momotaro chỉ huy những con vật đáng yêu trong vai binh lính. Lũ quỷ đại diện cho kẻ thù ngoại quốc. Truyện cổ tích bị biến thành một công cụ chính trị.

<short pause> Năm 1945, bộ phim hoạt hình dài đầu tiên của Nhật ra đời, tên là Momotaro: Thần binh trên biển. Đó là một bộ phim tuyên truyền do hải quân đặt làm.

<short pause> Nghĩa là lịch sử anime có một điểm khởi đầu rất lạ: phim hoạt hình dài đầu tiên của Nhật kể về Momotaro và những con quỷ.

<short pause> <laugh> Kaku ghi chú: cùng một câu chuyện, một người dùng để cổ vũ chiến tranh, một người dùng để phê phán chiến tranh. Truyện cổ tích không có lập trường. Người kể mới có.
```

**ElevenLabs**

```text
Năm 1924, nhà văn Akutagawa Ryunosuke, người mà giải văn học lớn nhất Nhật Bản mang tên, đăng một truyện ngắn tên là Momotaro. Và ông đã làm đúng điều Tougen Anki làm, trước gần một trăm năm.

[pause] Ông viết rằng lũ quỷ ở đó chơi đàn, múa hát, và kể cho nhau nghe chuyện về con người như kể chuyện ma. Con người mới là thứ đáng sợ trong mắt quỷ.

[pause] Trong truyện của Akutagawa, đảo Quỷ là một hòn đảo yên bình. Lũ quỷ sống hiền hòa, yêu âm nhạc, yêu gia đình.

[pause] Truyện kết thúc không có đoạn sống hạnh phúc mãi mãi. Những con quỷ sống sót ôm hận, và mối thù ấy được hứa hẹn sẽ còn tiếp diễn.

[pause] Momotaro tới xâm chiếm hòn đảo đó, không vì lý do chính đáng nào, và những con vật đi theo cậu chỉ vì được trả công. Người anh hùng bị kể lại như một kẻ xâm lược.

[pause] Đây là một truyện châm biếm tinh thần chiến tranh và bành trướng lúc bấy giờ. [curious] Akutagawa dùng chính câu chuyện mà ai cũng yêu để đặt ra câu hỏi: có thật kẻ thắng luôn đúng?

[pause] Kaku thấy tác giả Tougen Anki đi cùng một hướng. Có thể không phải bắt chước, nhưng rõ ràng câu hỏi ấy đã nằm trong truyện cổ tích từ rất lâu.

[pause] Rồi có một mặt ngược lại. Trong Thế chiến thứ hai, Momotaro được dùng làm biểu tượng tuyên truyền. Quỷ trở thành hình ảnh của kẻ thù bên ngoài.

[pause] Trong phim, Momotaro chỉ huy những con vật đáng yêu trong vai binh lính. Lũ quỷ đại diện cho kẻ thù ngoại quốc. Truyện cổ tích bị biến thành một công cụ chính trị.

[pause] Năm 1945, bộ phim hoạt hình dài đầu tiên của Nhật ra đời, tên là Momotaro: Thần binh trên biển. Đó là một bộ phim tuyên truyền do hải quân đặt làm.

[pause] Nghĩa là lịch sử anime có một điểm khởi đầu rất lạ: phim hoạt hình dài đầu tiên của Nhật kể về Momotaro và những con quỷ.

[pause] [chuckles] Kaku ghi chú: cùng một câu chuyện, một người dùng để cổ vũ chiến tranh, một người dùng để phê phán chiến tranh. Truyện cổ tích không có lập trường. Người kể mới có.
```

### c08 · Tougen Anki lật ngược những gì

Khoảng 95 giây · cảnh s60–s67 · 1241 ký tự

**Gemini**

```text
Giờ quay lại Tougen Anki. Thứ nhất, tác giả biến Momotaro từ một người anh hùng thành cả một dòng máu, một tổ chức có quy củ, có quyền lực, có cả vỏ bọc hợp pháp.

<short pause> Nghĩa là không còn đảo Quỷ ở xa ngoài biển nữa. Ranh giới giữa bên trong và bên ngoài cánh cửa giờ nằm ngay trong một thành phố, thậm chí trong một gia đình.

<short pause> Thứ hai, quỷ không còn là con quái vật ngoài đảo. Họ là người sống lẫn trong xã hội, nhiều người không hề biết mình mang dòng máu ấy cho tới khi thức tỉnh.

<short pause> Thứ ba, trong truyện gốc quỷ bị đánh và bị cướp châu báu. Trong Tougen Anki, hậu duệ quỷ bị truy đuổi chỉ vì dòng máu, không cần biết họ đã làm gì.

<short pause> Và phía Momotaro cũng không phải ai cũng giống ai. Truyện cho thấy trong mỗi phe đều có người tàn nhẫn và người tử tế. Dòng máu chỉ là điểm xuất phát.

<short pause> Thứ tư, và đây là chỗ tinh tế nhất: dòng máu không quyết định tất cả. Người cha nuôi mang máu Momotaro nhưng chọn yêu thương một đứa trẻ quỷ. Lựa chọn quan trọng hơn nguồn gốc.

<short pause> Và tên truyện, Tougen Anki, có chữ Đào Nguyên, nghĩa là vườn đào tiên, chốn thiên đường. <short pause> Nhưng đi kèm với nó là chữ quỷ. Một thiên đường có quỷ ẩn bên trong.

<short pause> Kaku để ý thêm một điều: năng lực của quỷ trong truyện đến từ chính dòng máu. Như thể thứ khiến họ bị săn đuổi cũng là thứ giúp họ tự vệ.
```

**ElevenLabs**

```text
Giờ quay lại Tougen Anki. Thứ nhất, tác giả biến Momotaro từ một người anh hùng thành cả một dòng máu, một tổ chức có quy củ, có quyền lực, có cả vỏ bọc hợp pháp.

[pause] Nghĩa là không còn đảo Quỷ ở xa ngoài biển nữa. Ranh giới giữa bên trong và bên ngoài cánh cửa giờ nằm ngay trong một thành phố, thậm chí trong một gia đình.

[pause] Thứ hai, quỷ không còn là con quái vật ngoài đảo. Họ là người sống lẫn trong xã hội, nhiều người không hề biết mình mang dòng máu ấy cho tới khi thức tỉnh.

[pause] Thứ ba, trong truyện gốc quỷ bị đánh và bị cướp châu báu. Trong Tougen Anki, hậu duệ quỷ bị truy đuổi chỉ vì dòng máu, không cần biết họ đã làm gì.

[pause] Và phía Momotaro cũng không phải ai cũng giống ai. Truyện cho thấy trong mỗi phe đều có người tàn nhẫn và người tử tế. Dòng máu chỉ là điểm xuất phát.

[pause] Thứ tư, và đây là chỗ tinh tế nhất: dòng máu không quyết định tất cả. Người cha nuôi mang máu Momotaro nhưng chọn yêu thương một đứa trẻ quỷ. Lựa chọn quan trọng hơn nguồn gốc.

[pause] Và tên truyện, Tougen Anki, có chữ Đào Nguyên, nghĩa là vườn đào tiên, chốn thiên đường. [pause] Nhưng đi kèm với nó là chữ quỷ. Một thiên đường có quỷ ẩn bên trong.

[pause] Kaku để ý thêm một điều: năng lực của quỷ trong truyện đến từ chính dòng máu. Như thể thứ khiến họ bị săn đuổi cũng là thứ giúp họ tự vệ.
```

### c09 · Vì sao phải lật ngược / Bản đồ thật và hư cấu

Khoảng 131 giây · cảnh s68–s79 · 1697 ký tự

**Gemini**

```text
Tại sao tác giả hiện đại lại thích lật ngược truyện cổ tích? <laugh> Kaku nghĩ có ba lý do.

<short pause> Một: người đọc hôm nay không còn chấp nhận câu chuyện có kẻ xấu chỉ vì họ trông khác. Chúng ta muốn biết lý do, muốn nghe cả phía bên kia.

<short pause> Hai: truyện cổ tích quá quen, nên lật ngược nó là cách nhanh nhất để gây bất ngờ. Người Nhật nghe tên Momotaro là đã có sẵn hình ảnh trong đầu, và tác giả chỉ cần xoay nó lại.

<short pause> Kaku nghĩ đây cũng là lý do truyện được yêu thích ngoài Nhật Bản: câu chuyện về người bị ghét chỉ vì nguồn gốc là câu chuyện mà ai cũng có thể hiểu.

<short pause> Ba: câu hỏi ai là quỷ vẫn luôn đúng với thời nào cũng vậy. Mỗi xã hội đều có những người bị coi là quỷ chỉ vì họ đến từ bên ngoài.

<short pause> Và đây là lý do dạng video này tồn tại trên kênh: hiểu câu chuyện gốc, bạn sẽ thấy anime hay hơn nhiều, vì bạn biết tác giả đang đối thoại với ai.

<short pause> Kaku gom lại thành một tấm bản đồ. Cột bên trái là những gì có thật trong văn hóa và lịch sử.

<short pause> Cũng ở cột có thật: di tích thành cổ ở Okayama gắn với truyền thuyết quỷ Ura, và cách giải thích chó, khỉ, chim là các con giáp ngược hướng quỷ môn, với nhãn là giả thuyết phổ biến.

<short pause> Có thật: truyện Momotaro với chó, khỉ, chim trĩ và bánh kê. Phiên bản cũ ông bà hóa trẻ. Truyền thuyết Kibitsuhiko và quỷ Ura ở Okayama. Tục ném đậu đuổi quỷ.

<short pause> Cũng có thật: truyện châm biếm năm 1924 của Akutagawa, và bộ phim hoạt hình tuyên truyền năm 1945.

<short pause> Cột bên phải là sáng tạo của Tougen Anki: hai dòng máu Momotaro và quỷ di truyền tới ngày nay, năng lực điều khiển máu, tổ chức săn quỷ hiện đại, và người cha nuôi chọn tình thương thay vì dòng máu.

<short pause> Và ở giữa hai cột, Kaku vẽ một mũi tên: câu hỏi ai mới thật sự là quỷ. Câu hỏi đó đi từ truyền thuyết cổ, qua Akutagawa, tới tận Tougen Anki hôm nay.
```

**ElevenLabs**

```text
[curious] Tại sao tác giả hiện đại lại thích lật ngược truyện cổ tích? [chuckles] Kaku nghĩ có ba lý do.

[pause] Một: người đọc hôm nay không còn chấp nhận câu chuyện có kẻ xấu chỉ vì họ trông khác. Chúng ta muốn biết lý do, muốn nghe cả phía bên kia.

[pause] Hai: truyện cổ tích quá quen, nên lật ngược nó là cách nhanh nhất để gây bất ngờ. Người Nhật nghe tên Momotaro là đã có sẵn hình ảnh trong đầu, và tác giả chỉ cần xoay nó lại.

[pause] Kaku nghĩ đây cũng là lý do truyện được yêu thích ngoài Nhật Bản: câu chuyện về người bị ghét chỉ vì nguồn gốc là câu chuyện mà ai cũng có thể hiểu.

[pause] Ba: câu hỏi ai là quỷ vẫn luôn đúng với thời nào cũng vậy. Mỗi xã hội đều có những người bị coi là quỷ chỉ vì họ đến từ bên ngoài.

[pause] Và đây là lý do dạng video này tồn tại trên kênh: hiểu câu chuyện gốc, bạn sẽ thấy anime hay hơn nhiều, vì bạn biết tác giả đang đối thoại với ai.

[pause] Kaku gom lại thành một tấm bản đồ. Cột bên trái là những gì có thật trong văn hóa và lịch sử.

[pause] Cũng ở cột có thật: di tích thành cổ ở Okayama gắn với truyền thuyết quỷ Ura, và cách giải thích chó, khỉ, chim là các con giáp ngược hướng quỷ môn, với nhãn là giả thuyết phổ biến.

[pause] Có thật: truyện Momotaro với chó, khỉ, chim trĩ và bánh kê. Phiên bản cũ ông bà hóa trẻ. Truyền thuyết Kibitsuhiko và quỷ Ura ở Okayama. Tục ném đậu đuổi quỷ.

[pause] Cũng có thật: truyện châm biếm năm 1924 của Akutagawa, và bộ phim hoạt hình tuyên truyền năm 1945.

[pause] Cột bên phải là sáng tạo của Tougen Anki: hai dòng máu Momotaro và quỷ di truyền tới ngày nay, năng lực điều khiển máu, tổ chức săn quỷ hiện đại, và người cha nuôi chọn tình thương thay vì dòng máu.

[pause] Và ở giữa hai cột, Kaku vẽ một mũi tên: câu hỏi ai mới thật sự là quỷ. Câu hỏi đó đi từ truyền thuyết cổ, qua Akutagawa, tới tận Tougen Anki hôm nay.
```

### c10 · Kết

Khoảng 59 giây · cảnh s80–s84 · 761 ký tự

**Gemini**

```text
Một quả đào trôi trên sông đã đi một hành trình dài hơn bất kỳ ai tưởng: từ truyền thuyết địa phương, vào sách giáo khoa, lên màn ảnh chiến tranh, rồi thành một bộ anime về những con người bị săn đuổi.

<short pause> Hãy nhớ lần sau nghe ai đó kể một câu chuyện có anh hùng và quỷ: thử hỏi xem ai đang cầm bút, và câu chuyện đã được sửa bao nhiêu lần.

<short pause> Nếu bạn là người kể lại truyện Momotaro, bạn sẽ đứng về phía ai? Viết phiên bản một câu của bạn vào bình luận nhé, Kaku sẽ đọc từng câu.

<short pause> Video tiếp theo, Kaku quay lại với một trận đấu kinh điển: Ichigo đối đầu Byakuya. Kaku sẽ chia trận đấu thành từng hiệp, xem mỗi người đã chọn gì và trả giá gì.

<short pause> Nếu bạn thích những video đào ngược về nguồn gốc thật như thế này, hãy đăng ký kênh để không bỏ lỡ. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Một quả đào trôi trên sông đã đi một hành trình dài hơn bất kỳ ai tưởng: từ truyền thuyết địa phương, vào sách giáo khoa, lên màn ảnh chiến tranh, rồi thành một bộ anime về những con người bị săn đuổi.

[pause] Hãy nhớ lần sau nghe ai đó kể một câu chuyện có anh hùng và quỷ: thử hỏi xem ai đang cầm bút, và câu chuyện đã được sửa bao nhiêu lần.

[pause] [curious] Nếu bạn là người kể lại truyện Momotaro, bạn sẽ đứng về phía ai? Viết phiên bản một câu của bạn vào bình luận nhé, Kaku sẽ đọc từng câu.

[pause] Video tiếp theo, Kaku quay lại với một trận đấu kinh điển: Ichigo đối đầu Byakuya. Kaku sẽ chia trận đấu thành từng hiệp, xem mỗi người đã chọn gì và trả giá gì.

[pause] Nếu bạn thích những video đào ngược về nguồn gốc thật như thế này, hãy đăng ký kênh để không bỏ lỡ. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
