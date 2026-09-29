# Bộ prompt · The One Piece: Những chi tiết cài cắm trong 50 chương đầu

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói về năm mươi chương đầu One Piece, và những chỗ các chi tiết đó được trả lời v…

```text
Wide 16:9 landscape cinematic frame. an old leather-bound logbook lying open on a ship's deck with a spoiler warning card tucked between the pages, close-up, warm dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Câu trả lời đã có từ tập đầu tiên. Đó là cảm giác của rất nhiều người khi đọc lại One Piece sau hai mươi năm.

```text
Wide 16:9 landscape cinematic frame. a first page of a manga chapter sketched on paper with a tiny glowing mark hidden in the corner, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đầu năm 2027, Netflix ra mắt The One Piece, bản anime làm lại từ đầu do studio WIT thực hiện, bắt đầu từ biển…

```text
Wide 16:9 landscape cinematic frame. a small ship setting sail from a peaceful harbor at sunrise, gulls circling above, wide shot, fresh morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và năm mươi chương đầu đó chứa những chi tiết mà Oda đã cài từ năm 1997, và phải mất mười, hai mươi, thậm chí…

```text
Wide 16:9 landscape cinematic frame. a seed planted in the soil beside a tall old tree whose roots reach toward it, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đặt hai khung cạnh nhau cho mỗi chi tiết: lần đầu xuất hiện, và ý ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two picture frames side by side, one empty and one with a question mark. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Năm mươi chương đầu gồm: chương một ở làng Foosha, gặp Zoro ở căn cứ Hải quân, băng Buggy, làng Syrup với Uso…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn map of a calm sea with a dotted route connecting five small islands, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Chi tiết 1: tên của Vua Hải Tặc

Lời: Trang đầu tiên của One Piece mở bằng một cuộc hành quyết. Vua Hải Tặc bị xử tử, và trước khi chết, ông nói vớ…

```text
Wide 16:9 landscape cinematic frame. a wooden execution platform in a crowded town square under a bright sky, a tall figure standing calmly at its center, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Ở những bản dịch và phiên bản đầu, ông được gọi là Gold Roger. Nghe như một cái tên bình thường, liên quan tớ…

```text
Wide 16:9 landscape cinematic frame. a wanted poster nailed to a wooden post with a name printed in bold letters, the ink slightly faded, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Về sau truyện tiết lộ: tên thật của ông là Gol D. Roger. Chữ D bị Chính phủ Thế giới cố tình giấu đi, vì nhữn…

```text
Wide 16:9 landscape cinematic frame. a government document with one letter carefully blacked out in a name, extreme close-up, cold official light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và Luffy, nhân vật chính, tên đầy đủ là Monkey D. Luffy. Chữ D đã nằm trong tên cậu ngay từ chương một, chỉ l…

```text
Wide 16:9 landscape cinematic frame. a name written on a small ship's registry card with the middle initial circled in pencil, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Và câu nói cuối cùng của Roger trên đoạn đầu đài đã mở ra cả Kỷ nguyên Hải tặc. Hàng nghìn người ra khơi chỉ…

```text
Wide 16:9 landscape cinematic frame. hundreds of small ships setting sail at once from a crowded harbor toward the open sea, wide shot, bright adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: một chữ cái nhỏ, cài từ trang đầu, tới giờ vẫn là một trong những bí ẩn lớn nhất của truyện. Ý chí…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering through a magnifying glass at a single letter printed on a page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Chi tiết 2: chiếc mũ và cánh tay

Lời: Chương một: Shanks, thuyền trưởng tóc đỏ, đặt chiếc mũ rơm lên đầu cậu bé Luffy, và dặn cậu trả lại khi đã tr…

```text
Wide 16:9 landscape cinematic frame. an old wide-brimmed hat being placed on a small child's head at a harbor dock at sunset, close-up of hands and hat, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Cùng chương đó, Shanks mất một cánh tay khi cứu Luffy khỏi một con quái vật biển. Ông nói, đại ý, rằng ông đã…

```text
Wide 16:9 landscape cinematic frame. a sea monster's shadow rising beneath a small rowboat on dark water, a figure leaning over the side to shield a child, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Về sau ta biết chiếc mũ vốn thuộc về Roger. Shanks từng là cậu bé tập sự trên tàu Roger, được trao chiếc mũ,…

```text
Wide 16:9 landscape cinematic frame. three hands of different ages passing an old wide-brimmed hat along a line, symbolic close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Nghĩa là ngay từ chương một, Shanks đã nhìn thấy ở Luffy thứ gì đó giống Roger. Cánh tay và chiếc mũ không ph…

```text
Wide 16:9 landscape cinematic frame. an old captain's portrait on a cabin wall beside a small child's drawing of a ship, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và lời hẹn trả mũ vẫn chưa được thực hiện. Luffy và Shanks chưa gặp lại nhau kể từ chương một. Hơn một nghìn…

```text
Wide 16:9 landscape cinematic frame. an old wide-brimmed hat hanging on a hook beside an empty chair in a ship's cabin, close-up, quiet waiting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Kaku rất thích chữ thời đại mới. Nó được nói ở chương một, và cả truyện về sau chính là thời đại mới đó thành…

```text
Wide 16:9 landscape cinematic frame. a sunrise breaking over a vast ocean horizon with a tiny ship sailing toward it, wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Chi tiết 3: vết sẹo trên mắt Shanks

Lời: Cũng ở chương một, Shanks có ba vết sẹo trên mắt trái. Không ai giải thích. Người đọc năm 1997 chỉ nghĩ đó là…

```text
Wide 16:9 landscape cinematic frame. three parallel scratch marks carved into an old wooden mast, extreme close-up, warm sunlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Phải tới chương 434, gần mười năm sau, Shanks mới nói ra: vết sẹo đó do Râu Đen, Marshall D. Teach, gây ra.

```text
Wide 16:9 landscape cinematic frame. a dark silhouette laughing on a stormy cliff with jagged lightning behind it, dramatic low-angle shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Một người đã khiến Shanks, một trong những hải tặc mạnh nhất thế giới, bị thương. Chỉ một chi tiết nhỏ ở chươ…

```text
Wide 16:9 landscape cinematic frame. a chess board with a single black piece lurking at the far edge while the other pieces face the opposite direction, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kaku để ý: Râu Đen là người mang chữ D. Shanks thì không. Hai chi tiết nhỏ từ hai thời điểm khác nhau, nhưng…

```text
Wide 16:9 landscape cinematic frame. two name cards side by side on a table, one with a circled middle initial and one without, close-up, dim mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Và hai người đó, Shanks và Râu Đen, cho tới giờ vẫn là hai thế lực mà người đọc chờ đợi được thấy đối mặt nha…

```text
Wide 16:9 landscape cinematic frame. two ships approaching each other from opposite horizons under a heavy sky, wide shot, tense grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Chi tiết 4: trái ác quỷ trong rương

Lời: Chương một: trong một bữa tiệc, Luffy vô tình ăn trái ác quỷ mà băng Shanks mang về. Cậu trở thành người cao…

```text
Wide 16:9 landscape cinematic frame. a strange swirling fruit resting inside an open wooden treasure chest on a tavern table, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Suốt hơn một nghìn chương, trái đó được gọi là trái cao su, một trái Paramecia bình thường.

```text
Wide 16:9 landscape cinematic frame. a small label tied to a fruit with a simple word written on it, extreme close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Chương 1044 tiết lộ: tên thật là Hito Hito no Mi, mô hình Nika, một trái Zoan thần thoại mà Chính phủ Thế giớ…

```text
Wide 16:9 landscape cinematic frame. an ancient mural of a laughing sun god painted on weathered stone, close-up, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và chương 1054 cho thấy: băng Shanks đã cướp trái này từ một con tàu của Chính phủ. Nghĩa là trái ác quỷ tron…

```text
Wide 16:9 landscape cinematic frame. a government transport ship on open sea with smoke rising from its deck and a small pirate ship sailing away, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Câu hỏi còn lại mà fan vẫn tranh luận: Shanks có biết trái đó là gì khi để nó trong rương không? Truyện chưa…

```text
Wide 16:9 landscape cinematic frame. a closed treasure chest with a small question mark tag hanging from its lock, close-up, mysterious warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là cú lật tuyệt vời. Một trái cây nằm trong rương ở trang mười mấy của chương một, hóa ra là th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a small fruit on a plate with wide shocked eyes and its beak open. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Chi tiết 5: người bắn súng trên tàu Shanks

Lời: Chương một, trong băng Shanks có một người bắn súng tên Yasopp. Anh chỉ xuất hiện vài khung hình, khoe về đứa…

```text
Wide 16:9 landscape cinematic frame. a sharpshooter's rifle leaning against a barrel on a tavern floor beside a mug, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Khoảng hai mươi chương sau, ở làng Syrup, Luffy gặp Usopp, một cậu bé hay nói dối, có tài bắn ná. Và Usopp ch…

```text
Wide 16:9 landscape cinematic frame. a slingshot and a small pouch of pebbles resting on a wooden fence overlooking a quiet village, close-up, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Luffy nhận ra ngay, và kể cho Usopp nghe về người cha đang ở trên biển. Đó là lần đầu một chi tiết cài cắm đư…

```text
Wide 16:9 landscape cinematic frame. two young figures sitting on a hilltop overlooking the sea at sunset, one gesturing excitedly toward the horizon, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Trong phim One Piece Film: Red, Usopp lần đầu cảm nhận được sự hiện diện của cha mình qua Haki quan sát. Một…

```text
Wide 16:9 landscape cinematic frame. two distant figures on separate ships sensing each other across a wide sea, faint glowing lines between them, wide shot, soft blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và mối liên hệ đó chưa dừng lại. Hai cha con, một người trên tàu Shanks, một người trên tàu Luffy, là một sợi…

```text
Wide 16:9 landscape cinematic frame. two ships on the horizon connected by a faint glowing thread across the water, symbolic wide shot, soft dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Chi tiết 6: cậu bé muốn làm Hải quân

Lời: Chương hai: Luffy gặp Coby, một cậu bé nhút nhát làm việc vặt cho một nữ hải tặc. Coby mơ trở thành Hải quân.

```text
Wide 16:9 landscape cinematic frame. a timid boy carrying a heavy mop and bucket across a ship's deck, medium shot, harsh daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Luffy khuyến khích Coby theo đuổi giấc mơ. Coby rời đi, gia nhập Hải quân, trở thành người đầu tiên được Luff…

```text
Wide 16:9 landscape cinematic frame. a boy saluting at the gate of a naval base with the sea sparkling behind him, wide shot, bright hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Hơn một nghìn chương sau, Coby trở thành một anh hùng của Hải quân, nổi tiếng khắp thế giới. Cậu bé nhút nhát…

```text
Wide 16:9 landscape cinematic frame. a young naval officer standing confidently on a dock while a crowd cheers in the background, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Và cùng thời điểm đó còn có Helmeppo, cậu con trai hống hách của một viên chỉ huy Hải quân. Về sau cậu cũng t…

```text
Wide 16:9 landscape cinematic frame. two young naval recruits scrubbing a deck side by side, one grumbling and one smiling, humorous medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kaku thấy Coby là chi tiết cài cắm dễ thương nhất. Nó nói rằng tầm ảnh hưởng của Luffy không chỉ nằm ở những…

```text
Wide 16:9 landscape cinematic frame. two paths diverging on a map, one toward a pirate flag and one toward a naval flag, both starting from the same small dot, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Chi tiết 7: gã hề và người bạn cũ

Lời: Chương tám tới hai mươi mốt: băng hải tặc Buggy, một gã hề nổ tung được thành nhiều mảnh. Nhìn thì như một ph…

```text
Wide 16:9 landscape cinematic frame. a circus tent pitched on a small island with colorful flags and a cannon pointing out of it, wide shot, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nhưng trong arc này, Buggy nhắc tới Shanks như một người quen cũ. Hai người từng là cậu bé tập sự trên cùng m…

```text
Wide 16:9 landscape cinematic frame. two small boys sweeping the deck of a large ship side by side, sepia flashback style, soft light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Về sau, Buggy trốn thoát từ nhà tù, lập một tổ chức mới, và ở chương 1058 trở thành một trong Tứ Hoàng. Gã hề…

```text
Wide 16:9 landscape cinematic frame. a clownish silhouette sitting nervously on a giant throne with a huge bounty poster behind him, humorous wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và điều buồn cười là Buggy được lên Tứ Hoàng một phần nhờ danh tiếng được thổi phồng: người ta tin gã là bạn…

```text
Wide 16:9 landscape cinematic frame. a newspaper with a large headline and a clown silhouette on the front page, crumpled slightly, close-up, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kaku thích nhất ở Buggy: không ai tin gã sẽ đi xa như vậy, kể cả chính gã. Một nhân vật phụ được cài từ chươn…

```text
Wide 16:9 landscape cinematic frame. a small toy clown figurine placed on a shelf among much larger statues of warriors, close-up, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Chi tiết 8: lời hứa của kiếm sĩ

Lời: Chương năm: hồi ức của Zoro về Kuina, người bạn thời nhỏ. Hai đứa hứa với nhau rằng một trong hai sẽ trở thàn…

```text
Wide 16:9 landscape cinematic frame. two small wooden practice swords crossed on the floor of a quiet dojo at dusk, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Kuina mất sớm. Zoro mang theo thanh kiếm của cô, và lời hứa trở thành mục tiêu cả đời.

```text
Wide 16:9 landscape cinematic frame. a single white-handled sword resting on a small memorial shelf with a candle beside it, close-up, soft somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Chương bốn mươi chín tới năm mươi hai: Zoro gặp Mihawk, kiếm sĩ mạnh nhất thế giới, và thua một cách tuyệt đố…

```text
Wide 16:9 landscape cinematic frame. a swordsman standing tall on a floating wreck facing a lone figure in a small boat, the sea glowing at sunset, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Về sau, sau hai năm cách biệt, chính Mihawk lại là người huấn luyện Zoro. Kẻ đánh bại cậu ở chương năm mươi t…

```text
Wide 16:9 landscape cinematic frame. a quiet castle courtyard on a misty island with two sword silhouettes sparring, wide shot, soft grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Và Mihawk, lúc xuất hiện, là một thành viên Thất Vũ Hải. Hệ thống đó được giới thiệu ngay trong năm mươi chươ…

```text
Wide 16:9 landscape cinematic frame. seven small official seals lined up on a desk with one seal highlighted, close-up, cold official light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: cảnh Zoro thua Mihawk là lần đầu tiên One Piece cho thấy biển cả rộng tới mức nào. Năm mươi chương…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up at a vast horizon from the edge of a tiny island with awe. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Chi tiết thêm: cô trộm ghét hải tặc

Lời: Chương tám: Nami xuất hiện, một cô trộm chuyên ăn cắp của hải tặc. Cô nói rõ rằng mình ghét hải tặc, và chỉ đ…

```text
Wide 16:9 landscape cinematic frame. a small bag of stolen coins and a folded sea chart hidden inside a cloak pocket, close-up, sly warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Trong năm mươi chương đầu, Nami có vài khoảnh khắc lạ: buồn bã khi nhìn biển, nói về một khoản tiền cần gom đ…

```text
Wide 16:9 landscape cinematic frame. a young woman sitting alone on a ship's railing at night looking at the sea with a troubled expression, back view, soft moonlight. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Về sau, ở arc Arlong, ta biết lý do: làng của Nami bị một băng hải tặc người cá cai trị, và cô gom tiền để mu…

```text
Wide 16:9 landscape cinematic frame. a small seaside village with orange trees in the foreground and a menacing fortress on the horizon, wide shot, heavy overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Và giấc mơ vẽ bản đồ toàn thế giới của cô, được nhắc từ rất sớm, cũng có gốc từ chính quá khứ đó.

```text
Wide 16:9 landscape cinematic frame. a half-finished hand-drawn world map pinned to a wooden desk with drawing tools around it, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Chi tiết thêm: lời nói dối thành sự thật

Lời: Làng Syrup: Usopp nổi tiếng vì mỗi sáng chạy khắp làng hô hải tặc tới rồi. Chẳng ai tin cậu nữa.

```text
Wide 16:9 landscape cinematic frame. a boy running down a village road at dawn waving his arms and shouting while villagers roll their eyes, humorous wide shot, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Rồi một ngày, hải tặc tới thật. Và lời nói dối của Usopp, trong một thoáng, trở thành lời cảnh báo mà cả làng…

```text
Wide 16:9 landscape cinematic frame. a dark pirate ship silhouette appearing on a misty horizon beyond a sleepy village, wide shot, ominous dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Kaku thấy đây là mô-típ của Usopp suốt cả truyện: những lời khoác lác của cậu dần trở thành sự thật. Cậu nói…

```text
Wide 16:9 landscape cinematic frame. a small handwritten boast on a scrap of paper slowly turning into a real medal pinned beside it, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Chi tiết 9: con tàu Going Merry

Lời: Chương bốn mươi mốt: Kaya, cô tiểu thư ở làng Syrup, tặng cả nhóm con tàu Going Merry, có chiếc đầu cừu dễ th…

```text
Wide 16:9 landscape cinematic frame. a small cozy caravel with a sheep-shaped figurehead moored at a quiet village dock, wide shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Ở năm mươi chương đầu, Merry chỉ là một phương tiện di chuyển. Nhưng Oda cho nó rất nhiều khung hình, rất nhi…

```text
Wide 16:9 landscape cinematic frame. a lively ship's deck with laundry hanging, a fishing rod leaning on the rail, and a small table set for a meal, wide shot, sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Về sau, ở chương 430, Merry hỏng nặng không thể sửa. Cả nhóm tiễn con tàu bằng một đám tang trên biển, và Mer…

```text
Wide 16:9 landscape cinematic frame. a small ship burning gently on a calm sea at night, sparks rising into a starry sky, wide shot, bittersweet orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nhiều người đọc nói đó là một trong những cảnh khiến họ khóc nhiều nhất. Và nó chỉ có sức nặng vì năm mươi ch…

```text
Wide 16:9 landscape cinematic frame. a small wooden sheep figurine resting on a windowsill beside a folded map, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Chi tiết 10: giấc mơ của đầu bếp

Lời: Từ chương bốn mươi ba: nhà hàng Baratie trên biển, và đầu bếp Sanji. Cậu kể về All Blue, một vùng biển huyền…

```text
Wide 16:9 landscape cinematic frame. a floating restaurant shaped like a large fish anchored on a calm sea, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Cậu học giấc mơ đó từ Zeff, người chủ nhà hàng, một cựu hải tặc đã mất một chân. Hai người từng suýt chết đói…

```text
Wide 16:9 landscape cinematic frame. a small rocky island in the middle of an empty sea with a single wooden crutch planted on top, wide shot, harsh bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: All Blue tới giờ vẫn chưa được tìm thấy. Nó là một trong những lời hứa được cài từ năm mươi chương đầu mà ngư…

```text
Wide 16:9 landscape cinematic frame. a sea chart with a single blue circle drawn in the middle of blank ocean, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Cảnh Sanji rời Baratie, quỳ xuống cảm ơn Zeff, nằm ngay sau năm mươi chương đầu. Nhưng toàn bộ sức nặng của c…

```text
Wide 16:9 landscape cinematic frame. a young cook kneeling on the deck of a floating restaurant bowing deeply toward an older man with a wooden leg, wide shot, emotional warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và Kaku để ý: ngay từ năm mươi chương đầu, mỗi thành viên đều có một giấc mơ cụ thể: Vua Hải Tặc, kiếm sĩ mạn…

```text
Wide 16:9 landscape cinematic frame. a row of small handwritten dream cards pinned to a ship's mast, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Chi tiết cài cắm hay nhất

Lời: Và giờ, chi tiết cài cắm Kaku thấy hay nhất. Hãy quay lại trang đầu tiên của chương một.

```text
Wide 16:9 landscape cinematic frame. the very first page of an old book slowly turning in a beam of light, close-up, warm dust-filled light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Roger, trên đoạn đầu đài, trước khi chết, mỉm cười. Ông không sợ hãi, không hối hận. Ông cười.

```text
Wide 16:9 landscape cinematic frame. a tall silhouette on a wooden platform facing a vast crowd, head tilted upward with a faint smile, wide shot, bright dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Hơn chín trăm chương sau, ở chương 967, ta biết: khi Roger tới hòn đảo cuối cùng và thấy kho báu, ông cười lớ…

```text
Wide 16:9 landscape cinematic frame. a group of old sailors laughing on a beach at night under a sky full of stars, wide shot, warm firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và Nika, vị thần trong trái ác quỷ của Luffy, là vị thần của tiếng cười và sự giải phóng. Nụ cười của Roger,…

```text
Wide 16:9 landscape cinematic frame. three small smiling faces drawn in a row on parchment and connected by a single golden line, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và ở Loguetown, ngay sau biển Đông, Luffy suýt bị xử tử trên chính đoạn đầu đài của Roger. Và cậu cũng mỉm cư…

```text
Wide 16:9 landscape cinematic frame. a young figure on an old wooden execution platform grinning in the rain as lightning strikes nearby, wide shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là chi tiết đẹp nhất: One Piece bắt đầu bằng một người đàn ông mỉm cười khi đối diện cái chết.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently closing the first page of a book and smiling softly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Bảng trước và sau

Lời: Tổng kết mười một chi tiết trên hai khung trước và sau. Tên Gold Roger thành Gol D. Roger. Chiếc mũ của Shank…

```text
Wide 16:9 landscape cinematic frame. a two-column chart on parchment with small before-and-after sketches for the first three items, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Trái cao su thành trái thần Nika bị cướp từ tàu Chính phủ. Người bắn súng thành cha của Usopp. Cậu bé nhút nh…

```text
Wide 16:9 landscape cinematic frame. the chart with the next four items sketched on both sides, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Lời hứa với Kuina và Mihawk. Con tàu Going Merry. Giấc mơ All Blue. Và nụ cười của Roger.

```text
Wide 16:9 landscape cinematic frame. the completed chart with a gold star next to the final item, amber ink close-up, warm triumphant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Cộng thêm hai chi tiết tặng kèm: cô trộm ghét hải tặc mang một vết thương thật, và lời nói dối của Usopp dần…

```text
Wide 16:9 landscape cinematic frame. two small bonus cards clipped to the corner of the chart with an orange doodle and a slingshot doodle, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Khi xem bản làm lại, bạn hãy thử để ý những chi tiết này. Bạn sẽ thấy năm mươi chương đầu không chỉ là phần m…

```text
Wide 16:9 landscape cinematic frame. a treasure map with many small hidden marks glowing faintly across its surface, close-up, warm adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Kết

Lời: Bạn có biết chi tiết cài cắm nào khác trong năm mươi chương đầu mà Kaku chưa nhắc? Viết vào bình luận nhé, Ka…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny ship doodle and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku mở bảng xếp hạng anh hùng của One Punch Man, từ hạng C tới hạng S, và cả những cấp độ t…

```text
Wide 16:9 landscape cinematic frame. a stat card sheet with letter grades from C to S and small hero silhouettes, close-up, bright game-style light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn sắp ra khơi cùng bản làm lại, hãy đăng ký kênh. Kaku sẽ đi cùng bạn qua từng hòn đảo, và chỉ cho bạn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving from the bow of a tiny paper boat as it drifts toward the sunrise. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Chi tiết 1: tên của Vua Hải Tặc

Khoảng 145 giây · cảnh s01–s12 · 1889 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói về năm mươi chương đầu One Piece, và những chỗ các chi tiết đó được trả lời về sau, có cái tận arc Wano và Egghead. Nếu bạn định xem bản làm lại mà không muốn biết trước, hãy lưu video lại.

<short pause> Câu trả lời đã có từ tập đầu tiên. Đó là cảm giác của rất nhiều người khi đọc lại One Piece sau hai mươi năm.

<short pause> Đầu năm 2027, Netflix ra mắt The One Piece, bản anime làm lại từ đầu do studio WIT thực hiện, bắt đầu từ biển Đông. Hàng triệu người sẽ xem lại năm mươi chương đầu.

<short pause> Và năm mươi chương đầu đó chứa những chi tiết mà Oda đã cài từ năm 1997, và phải mất mười, hai mươi, thậm chí hai mươi lăm năm mới được trả lời.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đặt hai khung cạnh nhau cho mỗi chi tiết: lần đầu xuất hiện, và ý nghĩa về sau. Cuối video là chi tiết cài cắm Kaku thấy hay nhất.

<short pause> Năm mươi chương đầu gồm: chương một ở làng Foosha, gặp Zoro ở căn cứ Hải quân, băng Buggy, làng Syrup với Usopp, và bắt đầu nhà hàng trên biển Baratie.

<short pause> Trang đầu tiên của One Piece mở bằng một cuộc hành quyết. Vua Hải Tặc bị xử tử, và trước khi chết, ông nói với đám đông rằng kho báu của ông đang chờ ai đó tới tìm.

<short pause> Ở những bản dịch và phiên bản đầu, ông được gọi là Gold Roger. Nghe như một cái tên bình thường, liên quan tới vàng.

<short pause> Về sau truyện tiết lộ: tên thật của ông là Gol D. Roger. Chữ D bị Chính phủ Thế giới cố tình giấu đi, vì những người mang chữ D liên quan tới một bí mật mà Chính phủ muốn chôn vùi.

<short pause> Và Luffy, nhân vật chính, tên đầy đủ là Monkey D. Luffy. Chữ D đã nằm trong tên cậu ngay từ chương một, chỉ là ta chưa biết nó có nghĩa gì.

<short pause> Và câu nói cuối cùng của Roger trên đoạn đầu đài đã mở ra cả Kỷ nguyên Hải tặc. Hàng nghìn người ra khơi chỉ vì một câu nói. Chính Chính phủ đã tự tạo ra cơn sóng mà họ muốn dập tắt.

<short pause> Kaku để ý: một chữ cái nhỏ, cài từ trang đầu, tới giờ vẫn là một trong những bí ẩn lớn nhất của truyện. Ý chí của chữ D là gì, Oda vẫn chưa nói hết.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói về năm mươi chương đầu One Piece, và những chỗ các chi tiết đó được trả lời về sau, có cái tận arc Wano và Egghead. Nếu bạn định xem bản làm lại mà không muốn biết trước, hãy lưu video lại.

[pause] Câu trả lời đã có từ tập đầu tiên. Đó là cảm giác của rất nhiều người khi đọc lại One Piece sau hai mươi năm.

[pause] Đầu năm 2027, Netflix ra mắt The One Piece, bản anime làm lại từ đầu do studio WIT thực hiện, bắt đầu từ biển Đông. Hàng triệu người sẽ xem lại năm mươi chương đầu.

[pause] Và năm mươi chương đầu đó chứa những chi tiết mà Oda đã cài từ năm 1997, và phải mất mười, hai mươi, thậm chí hai mươi lăm năm mới được trả lời.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đặt hai khung cạnh nhau cho mỗi chi tiết: lần đầu xuất hiện, và ý nghĩa về sau. Cuối video là chi tiết cài cắm Kaku thấy hay nhất.

[pause] Năm mươi chương đầu gồm: chương một ở làng Foosha, gặp Zoro ở căn cứ Hải quân, băng Buggy, làng Syrup với Usopp, và bắt đầu nhà hàng trên biển Baratie.

[pause] Trang đầu tiên của One Piece mở bằng một cuộc hành quyết. Vua Hải Tặc bị xử tử, và trước khi chết, ông nói với đám đông rằng kho báu của ông đang chờ ai đó tới tìm.

[pause] Ở những bản dịch và phiên bản đầu, ông được gọi là Gold Roger. Nghe như một cái tên bình thường, liên quan tới vàng.

[pause] Về sau truyện tiết lộ: tên thật của ông là Gol D. Roger. Chữ D bị Chính phủ Thế giới cố tình giấu đi, vì những người mang chữ D liên quan tới một bí mật mà Chính phủ muốn chôn vùi.

[pause] Và Luffy, nhân vật chính, tên đầy đủ là Monkey D. Luffy. Chữ D đã nằm trong tên cậu ngay từ chương một, chỉ là ta chưa biết nó có nghĩa gì.

[pause] Và câu nói cuối cùng của Roger trên đoạn đầu đài đã mở ra cả Kỷ nguyên Hải tặc. Hàng nghìn người ra khơi chỉ vì một câu nói. Chính Chính phủ đã tự tạo ra cơn sóng mà họ muốn dập tắt.

[pause] Kaku để ý: một chữ cái nhỏ, cài từ trang đầu, tới giờ vẫn là một trong những bí ẩn lớn nhất của truyện. Ý chí của chữ D là gì, Oda vẫn chưa nói hết.
```

### c02 · Chi tiết 2: chiếc mũ và cánh tay / Chi tiết 3: vết sẹo trên mắt Shanks

Khoảng 120 giây · cảnh s13–s23 · 1558 ký tự

**Gemini**

```text
Chương một: Shanks, thuyền trưởng tóc đỏ, đặt chiếc mũ rơm lên đầu cậu bé Luffy, và dặn cậu trả lại khi đã trở thành một hải tặc vĩ đại.

<short pause> Cùng chương đó, Shanks mất một cánh tay khi cứu Luffy khỏi một con quái vật biển. Ông nói, đại ý, rằng ông đã đặt cược cánh tay vào thời đại mới.

<short pause> Về sau ta biết chiếc mũ vốn thuộc về Roger. Shanks từng là cậu bé tập sự trên tàu Roger, được trao chiếc mũ, rồi trao lại cho Luffy.

<short pause> Nghĩa là ngay từ chương một, Shanks đã nhìn thấy ở Luffy thứ gì đó giống Roger. Cánh tay và chiếc mũ không phải là quà cho một đứa trẻ, mà là một khoản đầu tư cho tương lai.

<short pause> Và lời hẹn trả mũ vẫn chưa được thực hiện. Luffy và Shanks chưa gặp lại nhau kể từ chương một. Hơn một nghìn chương, và người đọc vẫn chờ khoảnh khắc đó.

<short pause> Kaku rất thích chữ thời đại mới. Nó được nói ở chương một, và cả truyện về sau chính là thời đại mới đó thành hình.

<short pause> Cũng ở chương một, Shanks có ba vết sẹo trên mắt trái. Không ai giải thích. Người đọc năm 1997 chỉ nghĩ đó là một chi tiết tạo dáng ngầu cho nhân vật.

<short pause> Phải tới chương 434, gần mười năm sau, Shanks mới nói ra: vết sẹo đó do Râu Đen, Marshall D. Teach, gây ra.

<short pause> Một người đã khiến Shanks, một trong những hải tặc mạnh nhất thế giới, bị thương. Chỉ một chi tiết nhỏ ở chương một đã báo trước sự nguy hiểm của phản diện lớn nhất truyện.

<short pause> Kaku để ý: Râu Đen là người mang chữ D. Shanks thì không. Hai chi tiết nhỏ từ hai thời điểm khác nhau, nhưng đặt cạnh nhau lại gợi ra rất nhiều câu hỏi.

<short pause> Và hai người đó, Shanks và Râu Đen, cho tới giờ vẫn là hai thế lực mà người đọc chờ đợi được thấy đối mặt nhau một lần nữa.
```

**ElevenLabs**

```text
Chương một: Shanks, thuyền trưởng tóc đỏ, đặt chiếc mũ rơm lên đầu cậu bé Luffy, và dặn cậu trả lại khi đã trở thành một hải tặc vĩ đại.

[pause] Cùng chương đó, Shanks mất một cánh tay khi cứu Luffy khỏi một con quái vật biển. Ông nói, đại ý, rằng ông đã đặt cược cánh tay vào thời đại mới.

[pause] Về sau ta biết chiếc mũ vốn thuộc về Roger. Shanks từng là cậu bé tập sự trên tàu Roger, được trao chiếc mũ, rồi trao lại cho Luffy.

[pause] Nghĩa là ngay từ chương một, Shanks đã nhìn thấy ở Luffy thứ gì đó giống Roger. Cánh tay và chiếc mũ không phải là quà cho một đứa trẻ, mà là một khoản đầu tư cho tương lai.

[pause] Và lời hẹn trả mũ vẫn chưa được thực hiện. Luffy và Shanks chưa gặp lại nhau kể từ chương một. Hơn một nghìn chương, và người đọc vẫn chờ khoảnh khắc đó.

[pause] Kaku rất thích chữ thời đại mới. Nó được nói ở chương một, và cả truyện về sau chính là thời đại mới đó thành hình.

[pause] Cũng ở chương một, Shanks có ba vết sẹo trên mắt trái. Không ai giải thích. Người đọc năm 1997 chỉ nghĩ đó là một chi tiết tạo dáng ngầu cho nhân vật.

[pause] Phải tới chương 434, gần mười năm sau, Shanks mới nói ra: vết sẹo đó do Râu Đen, Marshall D. Teach, gây ra.

[pause] Một người đã khiến Shanks, một trong những hải tặc mạnh nhất thế giới, bị thương. Chỉ một chi tiết nhỏ ở chương một đã báo trước sự nguy hiểm của phản diện lớn nhất truyện.

[pause] Kaku để ý: Râu Đen là người mang chữ D. Shanks thì không. Hai chi tiết nhỏ từ hai thời điểm khác nhau, nhưng đặt cạnh nhau lại gợi ra rất nhiều câu hỏi.

[pause] Và hai người đó, Shanks và Râu Đen, cho tới giờ vẫn là hai thế lực mà người đọc chờ đợi được thấy đối mặt nhau một lần nữa.
```

### c03 · Chi tiết 4: trái ác quỷ trong rương / Chi tiết 5: người bắn súng trên tàu Shanks

Khoảng 117 giây · cảnh s24–s34 · 1517 ký tự

**Gemini**

```text
Chương một: trong một bữa tiệc, Luffy vô tình ăn trái ác quỷ mà băng Shanks mang về. Cậu trở thành người cao su. Shanks nổi giận, nhưng đã quá muộn.

<short pause> Suốt hơn một nghìn chương, trái đó được gọi là trái cao su, một trái Paramecia bình thường.

<short pause> Chương 1044 tiết lộ: tên thật là Hito Hito no Mi, mô hình Nika, một trái Zoan thần thoại mà Chính phủ Thế giới đã săn lùng suốt tám trăm năm.

<short pause> Và chương 1054 cho thấy: băng Shanks đã cướp trái này từ một con tàu của Chính phủ. Nghĩa là trái ác quỷ trong rương ở chương một không phải là tình cờ.

<short pause> Câu hỏi còn lại mà fan vẫn tranh luận: Shanks có biết trái đó là gì khi để nó trong rương không? Truyện chưa nói rõ. Đây là vùng lý thuyết.

<short pause> <laugh> Kaku thấy đây là cú lật tuyệt vời. Một trái cây nằm trong rương ở trang mười mấy của chương một, hóa ra là thứ mà cả thế giới săn đuổi.

<short pause> Chương một, trong băng Shanks có một người bắn súng tên Yasopp. Anh chỉ xuất hiện vài khung hình, khoe về đứa con trai ở quê nhà.

<short pause> Khoảng hai mươi chương sau, ở làng Syrup, Luffy gặp Usopp, một cậu bé hay nói dối, có tài bắn ná. Và Usopp chính là con trai của Yasopp.

<short pause> Luffy nhận ra ngay, và kể cho Usopp nghe về người cha đang ở trên biển. Đó là lần đầu một chi tiết cài cắm được trả lời ngay trong năm mươi chương đầu.

<short pause> Trong phim One Piece Film: Red, Usopp lần đầu cảm nhận được sự hiện diện của cha mình qua Haki quan sát. Một cuộc gặp không lời, sau hơn hai mươi năm cài cắm.

<short pause> Và mối liên hệ đó chưa dừng lại. Hai cha con, một người trên tàu Shanks, một người trên tàu Luffy, là một sợi dây nối hai thế hệ hải tặc.
```

**ElevenLabs**

```text
Chương một: trong một bữa tiệc, Luffy vô tình ăn trái ác quỷ mà băng Shanks mang về. Cậu trở thành người cao su. Shanks nổi giận, nhưng đã quá muộn.

[pause] Suốt hơn một nghìn chương, trái đó được gọi là trái cao su, một trái Paramecia bình thường.

[pause] Chương 1044 tiết lộ: tên thật là Hito Hito no Mi, mô hình Nika, một trái Zoan thần thoại mà Chính phủ Thế giới đã săn lùng suốt tám trăm năm.

[pause] Và chương 1054 cho thấy: băng Shanks đã cướp trái này từ một con tàu của Chính phủ. Nghĩa là trái ác quỷ trong rương ở chương một không phải là tình cờ.

[pause] [curious] Câu hỏi còn lại mà fan vẫn tranh luận: Shanks có biết trái đó là gì khi để nó trong rương không? Truyện chưa nói rõ. Đây là vùng lý thuyết.

[pause] [chuckles] Kaku thấy đây là cú lật tuyệt vời. Một trái cây nằm trong rương ở trang mười mấy của chương một, hóa ra là thứ mà cả thế giới săn đuổi.

[pause] Chương một, trong băng Shanks có một người bắn súng tên Yasopp. Anh chỉ xuất hiện vài khung hình, khoe về đứa con trai ở quê nhà.

[pause] Khoảng hai mươi chương sau, ở làng Syrup, Luffy gặp Usopp, một cậu bé hay nói dối, có tài bắn ná. Và Usopp chính là con trai của Yasopp.

[pause] Luffy nhận ra ngay, và kể cho Usopp nghe về người cha đang ở trên biển. Đó là lần đầu một chi tiết cài cắm được trả lời ngay trong năm mươi chương đầu.

[pause] Trong phim One Piece Film: Red, Usopp lần đầu cảm nhận được sự hiện diện của cha mình qua Haki quan sát. Một cuộc gặp không lời, sau hơn hai mươi năm cài cắm.

[pause] Và mối liên hệ đó chưa dừng lại. Hai cha con, một người trên tàu Shanks, một người trên tàu Luffy, là một sợi dây nối hai thế hệ hải tặc.
```

### c04 · Chi tiết 6: cậu bé muốn làm Hải quân / Chi tiết 7: gã hề và người bạn cũ

Khoảng 120 giây · cảnh s35–s44 · 1556 ký tự

**Gemini**

```text
Chương hai: Luffy gặp Coby, một cậu bé nhút nhát làm việc vặt cho một nữ hải tặc. Coby mơ trở thành Hải quân.

<short pause> Luffy khuyến khích Coby theo đuổi giấc mơ. Coby rời đi, gia nhập Hải quân, trở thành người đầu tiên được Luffy truyền cảm hứng.

<short pause> Hơn một nghìn chương sau, Coby trở thành một anh hùng của Hải quân, nổi tiếng khắp thế giới. Cậu bé nhút nhát ở chương hai đã thật sự làm được.

<short pause> Và cùng thời điểm đó còn có Helmeppo, cậu con trai hống hách của một viên chỉ huy Hải quân. Về sau cậu cũng thay đổi, trở thành người đồng hành trung thành của Coby. Oda không bỏ quên cả những nhân vật tưởng như chỉ để làm nền.

<short pause> Kaku thấy Coby là chi tiết cài cắm dễ thương nhất. Nó nói rằng tầm ảnh hưởng của Luffy không chỉ nằm ở những người đi cùng cậu, mà cả ở những người đứng phía bên kia.

<short pause> Chương tám tới hai mươi mốt: băng hải tặc Buggy, một gã hề nổ tung được thành nhiều mảnh. Nhìn thì như một phản diện hài, đánh xong là quên.

<short pause> Nhưng trong arc này, Buggy nhắc tới Shanks như một người quen cũ. Hai người từng là cậu bé tập sự trên cùng một con tàu: tàu của Roger.

<short pause> Về sau, Buggy trốn thoát từ nhà tù, lập một tổ chức mới, và ở chương 1058 trở thành một trong Tứ Hoàng. Gã hề của chương tám đứng ngang hàng với Shanks.

<short pause> Và điều buồn cười là Buggy được lên Tứ Hoàng một phần nhờ danh tiếng được thổi phồng: người ta tin gã là bạn cũ, đối thủ ngang hàng của Shanks. Một chi tiết từ chương tám quay lại theo cách không ai ngờ.

<short pause> Kaku thích nhất ở Buggy: không ai tin gã sẽ đi xa như vậy, kể cả chính gã. Một nhân vật phụ được cài từ chương tám, và được Oda giữ lại suốt hai mươi năm.
```

**ElevenLabs**

```text
Chương hai: Luffy gặp Coby, một cậu bé nhút nhát làm việc vặt cho một nữ hải tặc. Coby mơ trở thành Hải quân.

[pause] Luffy khuyến khích Coby theo đuổi giấc mơ. Coby rời đi, gia nhập Hải quân, trở thành người đầu tiên được Luffy truyền cảm hứng.

[pause] Hơn một nghìn chương sau, Coby trở thành một anh hùng của Hải quân, nổi tiếng khắp thế giới. Cậu bé nhút nhát ở chương hai đã thật sự làm được.

[pause] Và cùng thời điểm đó còn có Helmeppo, cậu con trai hống hách của một viên chỉ huy Hải quân. Về sau cậu cũng thay đổi, trở thành người đồng hành trung thành của Coby. Oda không bỏ quên cả những nhân vật tưởng như chỉ để làm nền.

[pause] Kaku thấy Coby là chi tiết cài cắm dễ thương nhất. Nó nói rằng tầm ảnh hưởng của Luffy không chỉ nằm ở những người đi cùng cậu, mà cả ở những người đứng phía bên kia.

[pause] Chương tám tới hai mươi mốt: băng hải tặc Buggy, một gã hề nổ tung được thành nhiều mảnh. Nhìn thì như một phản diện hài, đánh xong là quên.

[pause] Nhưng trong arc này, Buggy nhắc tới Shanks như một người quen cũ. Hai người từng là cậu bé tập sự trên cùng một con tàu: tàu của Roger.

[pause] Về sau, Buggy trốn thoát từ nhà tù, lập một tổ chức mới, và ở chương 1058 trở thành một trong Tứ Hoàng. Gã hề của chương tám đứng ngang hàng với Shanks.

[pause] Và điều buồn cười là Buggy được lên Tứ Hoàng một phần nhờ danh tiếng được thổi phồng: người ta tin gã là bạn cũ, đối thủ ngang hàng của Shanks. Một chi tiết từ chương tám quay lại theo cách không ai ngờ.

[pause] Kaku thích nhất ở Buggy: không ai tin gã sẽ đi xa như vậy, kể cả chính gã. Một nhân vật phụ được cài từ chương tám, và được Oda giữ lại suốt hai mươi năm.
```

### c05 · Chi tiết 8: lời hứa của kiếm sĩ / Chi tiết thêm: cô trộm ghét hải tặc / Chi tiết thêm: lời nói dối thành sự thật

Khoảng 138 giây · cảnh s45–s57 · 1799 ký tự

**Gemini**

```text
Chương năm: hồi ức của Zoro về Kuina, người bạn thời nhỏ. Hai đứa hứa với nhau rằng một trong hai sẽ trở thành kiếm sĩ mạnh nhất thế giới.

<short pause> Kuina mất sớm. Zoro mang theo thanh kiếm của cô, và lời hứa trở thành mục tiêu cả đời.

<short pause> Chương bốn mươi chín tới năm mươi hai: Zoro gặp Mihawk, kiếm sĩ mạnh nhất thế giới, và thua một cách tuyệt đối. Zoro quay người lại, không để vết chém rơi vào lưng, và thề sẽ không bao giờ thua nữa.

<short pause> Về sau, sau hai năm cách biệt, chính Mihawk lại là người huấn luyện Zoro. Kẻ đánh bại cậu ở chương năm mươi trở thành người thầy.

<short pause> Và Mihawk, lúc xuất hiện, là một thành viên Thất Vũ Hải. Hệ thống đó được giới thiệu ngay trong năm mươi chương đầu, và bị bãi bỏ ở chương 956.

<short pause> <laugh> Kaku để ý: cảnh Zoro thua Mihawk là lần đầu tiên One Piece cho thấy biển cả rộng tới mức nào. Năm mươi chương đầu, và thế giới đã mở ra một cánh cửa rất lớn.

<short pause> Chương tám: Nami xuất hiện, một cô trộm chuyên ăn cắp của hải tặc. Cô nói rõ rằng mình ghét hải tặc, và chỉ đi cùng Luffy vì lợi ích.

<short pause> Trong năm mươi chương đầu, Nami có vài khoảnh khắc lạ: buồn bã khi nhìn biển, nói về một khoản tiền cần gom đủ. Người đọc khi đó chưa hiểu.

<short pause> Về sau, ở arc Arlong, ta biết lý do: làng của Nami bị một băng hải tặc người cá cai trị, và cô gom tiền để mua lại tự do cho cả làng. Cô ghét hải tặc vì một vết thương rất thật.

<short pause> Và giấc mơ vẽ bản đồ toàn thế giới của cô, được nhắc từ rất sớm, cũng có gốc từ chính quá khứ đó.

<short pause> Làng Syrup: Usopp nổi tiếng vì mỗi sáng chạy khắp làng hô hải tặc tới rồi. Chẳng ai tin cậu nữa.

<short pause> Rồi một ngày, hải tặc tới thật. Và lời nói dối của Usopp, trong một thoáng, trở thành lời cảnh báo mà cả làng không nghe.

<short pause> Kaku thấy đây là mô-típ của Usopp suốt cả truyện: những lời khoác lác của cậu dần trở thành sự thật. Cậu nói mình là chiến binh dũng cảm của biển cả trước khi thật sự trở thành như vậy.
```

**ElevenLabs**

```text
Chương năm: hồi ức của Zoro về Kuina, người bạn thời nhỏ. Hai đứa hứa với nhau rằng một trong hai sẽ trở thành kiếm sĩ mạnh nhất thế giới.

[pause] Kuina mất sớm. Zoro mang theo thanh kiếm của cô, và lời hứa trở thành mục tiêu cả đời.

[pause] Chương bốn mươi chín tới năm mươi hai: Zoro gặp Mihawk, kiếm sĩ mạnh nhất thế giới, và thua một cách tuyệt đối. Zoro quay người lại, không để vết chém rơi vào lưng, và thề sẽ không bao giờ thua nữa.

[pause] Về sau, sau hai năm cách biệt, chính Mihawk lại là người huấn luyện Zoro. Kẻ đánh bại cậu ở chương năm mươi trở thành người thầy.

[pause] Và Mihawk, lúc xuất hiện, là một thành viên Thất Vũ Hải. Hệ thống đó được giới thiệu ngay trong năm mươi chương đầu, và bị bãi bỏ ở chương 956.

[pause] [chuckles] Kaku để ý: cảnh Zoro thua Mihawk là lần đầu tiên One Piece cho thấy biển cả rộng tới mức nào. Năm mươi chương đầu, và thế giới đã mở ra một cánh cửa rất lớn.

[pause] Chương tám: Nami xuất hiện, một cô trộm chuyên ăn cắp của hải tặc. Cô nói rõ rằng mình ghét hải tặc, và chỉ đi cùng Luffy vì lợi ích.

[pause] Trong năm mươi chương đầu, Nami có vài khoảnh khắc lạ: buồn bã khi nhìn biển, nói về một khoản tiền cần gom đủ. Người đọc khi đó chưa hiểu.

[pause] Về sau, ở arc Arlong, ta biết lý do: làng của Nami bị một băng hải tặc người cá cai trị, và cô gom tiền để mua lại tự do cho cả làng. Cô ghét hải tặc vì một vết thương rất thật.

[pause] Và giấc mơ vẽ bản đồ toàn thế giới của cô, được nhắc từ rất sớm, cũng có gốc từ chính quá khứ đó.

[pause] Làng Syrup: Usopp nổi tiếng vì mỗi sáng chạy khắp làng hô hải tặc tới rồi. Chẳng ai tin cậu nữa.

[pause] Rồi một ngày, hải tặc tới thật. Và lời nói dối của Usopp, trong một thoáng, trở thành lời cảnh báo mà cả làng không nghe.

[pause] Kaku thấy đây là mô-típ của Usopp suốt cả truyện: những lời khoác lác của cậu dần trở thành sự thật. Cậu nói mình là chiến binh dũng cảm của biển cả trước khi thật sự trở thành như vậy.
```

### c06 · Chi tiết 9: con tàu Going Merry / Chi tiết 10: giấc mơ của đầu bếp

Khoảng 107 giây · cảnh s58–s66 · 1397 ký tự

**Gemini**

```text
Chương bốn mươi mốt: Kaya, cô tiểu thư ở làng Syrup, tặng cả nhóm con tàu Going Merry, có chiếc đầu cừu dễ thương ở mũi tàu.

<short pause> Ở năm mươi chương đầu, Merry chỉ là một phương tiện di chuyển. <short pause> Nhưng Oda cho nó rất nhiều khung hình, rất nhiều khoảnh khắc cả nhóm vui đùa trên boong.

<short pause> Về sau, ở chương 430, Merry hỏng nặng không thể sửa. Cả nhóm tiễn con tàu bằng một đám tang trên biển, và Merry cất tiếng cảm ơn họ.

<short pause> Nhiều người đọc nói đó là một trong những cảnh khiến họ khóc nhiều nhất. Và nó chỉ có sức nặng vì năm mươi chương đầu đã cho ta sống cùng con tàu.

<short pause> Từ chương bốn mươi ba: nhà hàng Baratie trên biển, và đầu bếp Sanji. Cậu kể về All Blue, một vùng biển huyền thoại nơi mọi loài cá trên thế giới cùng sinh sống.

<short pause> Cậu học giấc mơ đó từ Zeff, người chủ nhà hàng, một cựu hải tặc đã mất một chân. Hai người từng suýt chết đói cùng nhau trên một hòn đảo đá.

<short pause> All Blue tới giờ vẫn chưa được tìm thấy. Nó là một trong những lời hứa được cài từ năm mươi chương đầu mà người đọc vẫn đang chờ được trả lời.

<short pause> Cảnh Sanji rời Baratie, quỳ xuống cảm ơn Zeff, nằm ngay sau năm mươi chương đầu. <short pause> Nhưng toàn bộ sức nặng của cảnh đó được xây từ những chương trước, khi hai người cãi nhau mỗi ngày.

<short pause> Và Kaku để ý: ngay từ năm mươi chương đầu, mỗi thành viên đều có một giấc mơ cụ thể: Vua Hải Tặc, kiếm sĩ mạnh nhất, chiến binh dũng cảm của biển cả, bản đồ thế giới, All Blue. Cả truyện là hành trình của những giấc mơ đó.
```

**ElevenLabs**

```text
Chương bốn mươi mốt: Kaya, cô tiểu thư ở làng Syrup, tặng cả nhóm con tàu Going Merry, có chiếc đầu cừu dễ thương ở mũi tàu.

[pause] Ở năm mươi chương đầu, Merry chỉ là một phương tiện di chuyển. [pause] Nhưng Oda cho nó rất nhiều khung hình, rất nhiều khoảnh khắc cả nhóm vui đùa trên boong.

[pause] Về sau, ở chương 430, Merry hỏng nặng không thể sửa. Cả nhóm tiễn con tàu bằng một đám tang trên biển, và Merry cất tiếng cảm ơn họ.

[pause] Nhiều người đọc nói đó là một trong những cảnh khiến họ khóc nhiều nhất. Và nó chỉ có sức nặng vì năm mươi chương đầu đã cho ta sống cùng con tàu.

[pause] Từ chương bốn mươi ba: nhà hàng Baratie trên biển, và đầu bếp Sanji. Cậu kể về All Blue, một vùng biển huyền thoại nơi mọi loài cá trên thế giới cùng sinh sống.

[pause] Cậu học giấc mơ đó từ Zeff, người chủ nhà hàng, một cựu hải tặc đã mất một chân. Hai người từng suýt chết đói cùng nhau trên một hòn đảo đá.

[pause] All Blue tới giờ vẫn chưa được tìm thấy. Nó là một trong những lời hứa được cài từ năm mươi chương đầu mà người đọc vẫn đang chờ được trả lời.

[pause] Cảnh Sanji rời Baratie, quỳ xuống cảm ơn Zeff, nằm ngay sau năm mươi chương đầu. [pause] Nhưng toàn bộ sức nặng của cảnh đó được xây từ những chương trước, khi hai người cãi nhau mỗi ngày.

[pause] Và Kaku để ý: ngay từ năm mươi chương đầu, mỗi thành viên đều có một giấc mơ cụ thể: Vua Hải Tặc, kiếm sĩ mạnh nhất, chiến binh dũng cảm của biển cả, bản đồ thế giới, All Blue. Cả truyện là hành trình của những giấc mơ đó.
```

### c07 · Chi tiết cài cắm hay nhất / Bảng trước và sau

Khoảng 121 giây · cảnh s67–s77 · 1576 ký tự

**Gemini**

```text
Và giờ, chi tiết cài cắm Kaku thấy hay nhất. Hãy quay lại trang đầu tiên của chương một.

<short pause> Roger, trên đoạn đầu đài, trước khi chết, mỉm cười. Ông không sợ hãi, không hối hận. Ông cười.

<short pause> Hơn chín trăm chương sau, ở chương 967, ta biết: khi Roger tới hòn đảo cuối cùng và thấy kho báu, ông cười lớn tới mức đặt tên hòn đảo là Laugh Tale, câu chuyện của tiếng cười.

<short pause> Và Nika, vị thần trong trái ác quỷ của Luffy, là vị thần của tiếng cười và sự giải phóng. Nụ cười của Roger, tiếng cười ở Laugh Tale, và nụ cười của Luffy, có lẽ là cùng một câu trả lời.

<short pause> Và ở Loguetown, ngay sau biển Đông, Luffy suýt bị xử tử trên chính đoạn đầu đài của Roger. Và cậu cũng mỉm cười. Oda lặp lại hình ảnh chương một, như một lời nhắc: người thừa kế đã tới.

<short pause> <laugh> Kaku thấy đây là chi tiết đẹp nhất: One Piece bắt đầu bằng một người đàn ông mỉm cười khi đối diện cái chết. Và cả bộ truyện đang đi tìm lý do cho nụ cười đó.

<short pause> Tổng kết mười một chi tiết trên hai khung trước và sau. Tên Gold Roger thành Gol D. Roger. Chiếc mũ của Shanks thành mũ của Roger. Ba vết sẹo thành dấu vết của Râu Đen.

<short pause> Trái cao su thành trái thần Nika bị cướp từ tàu Chính phủ. Người bắn súng thành cha của Usopp. Cậu bé nhút nhát thành anh hùng Hải quân. Gã hề thành Tứ Hoàng.

<short pause> Lời hứa với Kuina và Mihawk. Con tàu Going Merry. Giấc mơ All Blue. Và nụ cười của Roger.

<short pause> Cộng thêm hai chi tiết tặng kèm: cô trộm ghét hải tặc mang một vết thương thật, và lời nói dối của Usopp dần trở thành sự thật.

<short pause> Khi xem bản làm lại, bạn hãy thử để ý những chi tiết này. Bạn sẽ thấy năm mươi chương đầu không chỉ là phần mở đầu, mà là bản đồ của cả hành trình.
```

**ElevenLabs**

```text
Và giờ, chi tiết cài cắm Kaku thấy hay nhất. Hãy quay lại trang đầu tiên của chương một.

[pause] Roger, trên đoạn đầu đài, trước khi chết, mỉm cười. Ông không sợ hãi, không hối hận. Ông cười.

[pause] Hơn chín trăm chương sau, ở chương 967, ta biết: khi Roger tới hòn đảo cuối cùng và thấy kho báu, ông cười lớn tới mức đặt tên hòn đảo là Laugh Tale, câu chuyện của tiếng cười.

[pause] Và Nika, vị thần trong trái ác quỷ của Luffy, là vị thần của tiếng cười và sự giải phóng. Nụ cười của Roger, tiếng cười ở Laugh Tale, và nụ cười của Luffy, có lẽ là cùng một câu trả lời.

[pause] Và ở Loguetown, ngay sau biển Đông, Luffy suýt bị xử tử trên chính đoạn đầu đài của Roger. Và cậu cũng mỉm cười. Oda lặp lại hình ảnh chương một, như một lời nhắc: người thừa kế đã tới.

[pause] [chuckles] Kaku thấy đây là chi tiết đẹp nhất: One Piece bắt đầu bằng một người đàn ông mỉm cười khi đối diện cái chết. Và cả bộ truyện đang đi tìm lý do cho nụ cười đó.

[pause] Tổng kết mười một chi tiết trên hai khung trước và sau. Tên Gold Roger thành Gol D. Roger. Chiếc mũ của Shanks thành mũ của Roger. Ba vết sẹo thành dấu vết của Râu Đen.

[pause] Trái cao su thành trái thần Nika bị cướp từ tàu Chính phủ. Người bắn súng thành cha của Usopp. Cậu bé nhút nhát thành anh hùng Hải quân. Gã hề thành Tứ Hoàng.

[pause] Lời hứa với Kuina và Mihawk. Con tàu Going Merry. Giấc mơ All Blue. Và nụ cười của Roger.

[pause] Cộng thêm hai chi tiết tặng kèm: cô trộm ghét hải tặc mang một vết thương thật, và lời nói dối của Usopp dần trở thành sự thật.

[pause] Khi xem bản làm lại, bạn hãy thử để ý những chi tiết này. Bạn sẽ thấy năm mươi chương đầu không chỉ là phần mở đầu, mà là bản đồ của cả hành trình.
```

### c08 · Kết

Khoảng 36 giây · cảnh s78–s80 · 467 ký tự

**Gemini**

```text
Bạn có biết chi tiết cài cắm nào khác trong năm mươi chương đầu mà Kaku chưa nhắc? Viết vào bình luận nhé, Kaku sẽ gom lại cho một phần hai.

<short pause> Video tiếp theo, Kaku mở bảng xếp hạng anh hùng của One Punch Man, từ hạng C tới hạng S, và cả những cấp độ thảm họa. Theo kiểu thẻ chỉ số game.

<short pause> Nếu bạn sắp ra khơi cùng bản làm lại, hãy đăng ký kênh. <laugh> Kaku sẽ đi cùng bạn qua từng hòn đảo, và chỉ cho bạn những viên sỏi nhỏ mà Oda đã rải trên đường. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Bạn có biết chi tiết cài cắm nào khác trong năm mươi chương đầu mà Kaku chưa nhắc? Viết vào bình luận nhé, Kaku sẽ gom lại cho một phần hai.

[pause] Video tiếp theo, Kaku mở bảng xếp hạng anh hùng của One Punch Man, từ hạng C tới hạng S, và cả những cấp độ thảm họa. Theo kiểu thẻ chỉ số game.

[pause] Nếu bạn sắp ra khơi cùng bản làm lại, hãy đăng ký kênh. [chuckles] Kaku sẽ đi cùng bạn qua từng hòn đảo, và chỉ cho bạn những viên sỏi nhỏ mà Oda đã rải trên đường. Kaku gấp sổ đây, hẹn gặp lại!
```
