# Bộ prompt · Vinland Saga: Người Viking thật và Thorfinn thật là ai?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 78 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (78 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết anime Vinland Saga mùa hai, và nhắc nhẹ hướng đi của manga, đã kết th…

```text
Wide 16:9 landscape cinematic frame. an old leather-bound saga manuscript lying closed on a wooden table beside a spoiler warning card, close-up, cold northern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Câu chuyện này có thật hơn bạn nghĩ. Khoảng năm 1010, một người Iceland tên Thorfinn dẫn ba con tàu vượt biển…

```text
Wide 16:9 landscape cinematic frame. three Norse longships with square sails crossing a grey stormy ocean toward a distant forested coastline, wide shot, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Gần năm trăm năm trước Columbus. Và tên của ông, Thorfinn, chính là cái tên mà tác giả Yukimura Makoto chọn c…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn Atlantic map with a dotted route from Iceland to Greenland to a green coastline, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Câu hỏi hôm nay: trong Vinland Saga, bao nhiêu là thật? Thorfinn thật là ai? Người Viking thật sống thế nào?…

```text
Wide 16:9 landscape cinematic frame. a large parchment divided into two columns, one marked with a rune and one with a question mark, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đặt Vinland Saga cạnh những bộ sử thi Iceland. Cuối video là bản đồ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny fur cloak, unrolling an old map on a wooden table by candlelight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Như mọi video dạng này, Kaku không vẽ chân dung người thật. Kaku dùng tàu, cổ vật, bản đồ, và những bóng ngườ…

```text
Wide 16:9 landscape cinematic frame. a museum display of a Viking-age iron sword, a brooch and a comb under soft spotlight, close-up, museum light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Vinland Saga là gì?

Lời: Vinland Saga là manga của Yukimura Makoto, đăng từ năm 2005 và kết thúc với chương hai trăm hai mươi vào thán…

```text
Wide 16:9 landscape cinematic frame. a long row of manga volumes on a wooden shelf with a small carved longship bookend, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Anime mùa một do WIT Studio làm năm 2019, mùa hai do MAPPA làm năm 2023. Hai mùa rất khác nhau: mùa một là ch…

```text
Wide 16:9 landscape cinematic frame. a split image: a battlefield with shields and smoke on the left, a quiet farm field with a wooden house on the right, symmetrical composition. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Câu chuyện theo Thorfinn, cậu bé chứng kiến cha mình bị giết, rồi lớn lên trong băng lính đánh thuê của kẻ th…

```text
Wide 16:9 landscape cinematic frame. a young boy sitting alone on a ship's deck clutching a short knife, staring at the sea, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nhiều người xem thích Vinland Saga vì nó dám thay đổi thể loại giữa chừng: từ một bộ hành động về chiến binh,…

```text
Wide 16:9 landscape cinematic frame. a battle axe lying abandoned on a field where small green shoots are starting to grow around it, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Rồi, sau tất cả, cậu bỏ kiếm, và mơ đưa mọi người tới một vùng đất không có chiến tranh, không có nô lệ: Vinl…

```text
Wide 16:9 landscape cinematic frame. a wooden sword laid down on the grass beside a plow in a sunny green field, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Người Viking thật

Lời: Trước hết, người Viking thật là ai? Viking không phải một dân tộc, mà là cách gọi những người Bắc Âu đi biển…

```text
Wide 16:9 landscape cinematic frame. a Norse longship pulled up on a pebble beach beside a trading post with barrels and furs, wide shot, cold morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Phần lớn thời gian, họ là nông dân, thợ thủ công, thương nhân. Đi biển cướp bóc chỉ là một phần, dù là phần n…

```text
Wide 16:9 landscape cinematic frame. a turf-roofed longhouse with smoke rising from its chimney, sheep grazing nearby, wide shot, soft overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Một hiểu lầm lớn: mũ sừng. Chưa có bằng chứng khảo cổ nào cho thấy chiến binh Viking đội mũ có sừng. Hình ảnh…

```text
Wide 16:9 landscape cinematic frame. a plain rounded iron helmet on a museum stand beside a crossed-out horned helmet doodle, close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Tàu Viking cũng là một kỳ quan kỹ thuật: đáy nông để vào được sông, thân ghép ván chồng lên nhau cho mềm dẻo,…

```text
Wide 16:9 landscape cinematic frame. a restored ancient longship displayed in a museum hall with its curved prow and overlapping planks visible, wide shot, soft museum light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Vinland Saga không cho nhân vật đội mũ sừng. Tác giả đã nghiên cứu rất kỹ trang phục, vũ khí và tà…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying on a tiny horned helmet, then taking it off with an embarrassed look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Người Viking cũng buôn bán nô lệ, gọi là thrall. Tù binh từ các cuộc cướp bóc bị bán qua nhiều vùng. Mùa hai…

```text
Wide 16:9 landscape cinematic frame. a heavy iron shackle lying on a rough wooden floor of a farm storehouse, close-up, somber cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Thế giới Bắc Âu năm 1000

Lời: Để hiểu Thorfinn thật, hãy nhìn thế giới của ông. Người Bắc Âu định cư ở Iceland từ cuối thế kỷ chín, trên mộ…

```text
Wide 16:9 landscape cinematic frame. a volcanic Icelandic landscape with a small turf farmstead beside a river, wide shot, soft misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Năm 930, họ lập ra Althing, một hội nghị nơi các thủ lĩnh gặp nhau hằng năm để làm luật và xử án. Nhiều người…

```text
Wide 16:9 landscape cinematic frame. a gathering of cloaked figures in a rocky valley beside a large flat stone under an open sky, wide shot, cold clear light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Khoảng năm 985, Erik Đỏ, bị trục xuất khỏi Iceland, đi về phía tây và lập khu định cư ở Greenland. Ông đặt tê…

```text
Wide 16:9 landscape cinematic frame. a rugged fjord with icebergs and a thin strip of green grass along the shore where a few houses stand, wide shot, cold bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và khoảng năm 1000, Iceland chính thức chuyển sang Kitô giáo qua một quyết định tại Althing. Thế giới của Tho…

```text
Wide 16:9 landscape cinematic frame. a small wooden church beside an old rune stone on a grassy hill, wide shot, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Vinland Saga cũng là một câu chuyện về thời đại chuyển giao. Giữa thần cũ và thần mới, giữa cướp b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at a fork in a path with a rune stone on one side and a small church on the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Leif Erikson và Vinland đầu tiên

Lời: Người đầu tiên tới Vinland theo sử thi là Leif Erikson, con trai của Erik Đỏ, khoảng năm 1000.

```text
Wide 16:9 landscape cinematic frame. a single longship approaching a misty forested coast with a lone figure standing at the bow, wide shot, cold dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Leif đặt tên cho ba vùng đất: Helluland, vùng đá phẳng; Markland, vùng rừng; và Vinland. Các nhà nghiên cứu c…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn coastline map with three regions labeled by small icons: flat stones, a forest, and a vine, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Vinland thường được hiểu là vùng đất nho, vì sử thi kể họ tìm thấy nho mọc hoang. Có học giả hiểu khác, nhưng…

```text
Wide 16:9 landscape cinematic frame. a cluster of wild grapes growing on a vine in a sunlit forest clearing, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Thorfinn Karlsefni đi sau Leif vài năm, với ý định không chỉ khám phá, mà định cư lâu dài: mang theo người, g…

```text
Wide 16:9 landscape cinematic frame. a longship loaded with livestock, barrels and families sailing on calm water, wide shot, hopeful morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Thorfinn thật

Lời: Thorfinn thật tên đầy đủ là Thorfinn Karlsefni. Karlsefni nghĩa là người có tố chất của một người đàn ông thự…

```text
Wide 16:9 landscape cinematic frame. a Norse trader's scale and a pouch of silver pieces on a wooden table beside a rune-carved stick, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Chuyện của ông được ghi lại trong hai bộ sử thi Iceland: Sử thi về Erik Đỏ, và Sử thi về người Greenland. Cả…

```text
Wide 16:9 landscape cinematic frame. two old manuscript pages side by side with Old Norse script and small illuminated initials, close-up, warm parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Theo sử thi, Thorfinn dẫn ba con tàu từ Greenland đi về phía tây, theo con đường mà Leif Erikson đã mở ra kho…

```text
Wide 16:9 landscape cinematic frame. three longships sailing past icy cliffs along a rugged coastline at dawn, wide shot, cold clear light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Vợ ông là Gudrid, một người phụ nữ phi thường, đã đi qua gần hết thế giới Bắc Âu thời đó. Và con trai họ, Sno…

```text
Wide 16:9 landscape cinematic frame. a small wooden cradle inside a turf house with a woven blanket and light coming through a doorway, close-up, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Sử thi kể về những lần trao đổi hàng hóa với người bản địa, rồi những hiểu lầm và xung đột. Người Bắc Âu ít n…

```text
Wide 16:9 landscape cinematic frame. a small pile of trade goods, cloth and furs, placed on a rock between two groups on a beach, wide shot, tense cautious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Sau khoảng ba năm, nhóm của Thorfinn rời Vinland. Sử thi kể về những xung đột với cư dân bản địa. Người Bắc Â…

```text
Wide 16:9 landscape cinematic frame. a longship sailing away from a forested coast at dusk with a distant campfire on the shore, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Và Thorfinn thật không phải một chiến binh trả thù. Ông là thương nhân, người đi tìm vùng đất mới để làm ăn v…

```text
Wide 16:9 landscape cinematic frame. a merchant's ledger and a map lying beside a sheathed knife on a table, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Chỗ tác giả thay đổi: Thorfinn trong truyện

Lời: Vậy Yukimura đã lấy gì và đổi gì? Ông lấy cái tên, và điểm đến: Vinland. Nhưng gần như toàn bộ tuổi thơ và tu…

```text
Wide 16:9 landscape cinematic frame. a blank page with a single name and a destination written at the top, the rest empty, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Sử thi gần như không kể gì về thời trẻ của Thorfinn Karlsefni. Và cũng như Kingdom, khoảng trống đó là món qu…

```text
Wide 16:9 landscape cinematic frame. an old manuscript with a large blank section between two dense blocks of text, close-up, parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Cha của Thorfinn trong truyện là Thors, một chiến binh huyền thoại đã bỏ kiếm. Cha thật của Thorfinn Karlsefn…

```text
Wide 16:9 landscape cinematic frame. a sheathed sword hung on a wall above a family hearth, gathering dust, close-up, warm quiet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Câu nói nổi tiếng của Thors, đại ý: con không có kẻ thù nào cả, không ai có kẻ thù cả. Câu đó trở thành trái…

```text
Wide 16:9 landscape cinematic frame. a father's large hand resting on a child's head beside a calm fjord at dusk, close-up, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Ở cuối manga, Thorfinn trong truyện thật sự đi tới Vinland, như Thorfinn thật. Hai cuộc đời khác nhau hội tụ…

```text
Wide 16:9 landscape cinematic frame. two paths drawn on a map, one straight and one winding, meeting at the same small coastal point, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kaku thấy tác giả chọn một thương nhân có thật làm khung, rồi lấp vào đó hành trình từ trả thù tới hòa bình.…

```text
Wide 16:9 landscape cinematic frame. a map with a fixed destination marked in ink and a winding pencil path leading to it, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Chiến tranh ở nước Anh

Lời: Phần đầu Vinland Saga diễn ra trong những cuộc chiến của người Đan Mạch ở Anh. Bối cảnh này cũng có thật.

```text
Wide 16:9 landscape cinematic frame. a misty English countryside with a burned village on a hill and longships moored in a river below, wide shot, grey somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Để mua bình yên, nước Anh nhiều lần phải trả cho người Viking những khoản tiền cống nạp lớn bằng bạc, sau này…

```text
Wide 16:9 landscape cinematic frame. heavy chests of silver coins being loaded onto a longship at a riverside dock, close-up, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Năm 1002, vua Anh Æthelred ra lệnh giết những người Đan Mạch sống ở Anh, sự kiện gọi là vụ thảm sát ngày thán…

```text
Wide 16:9 landscape cinematic frame. an old English church door at night with a single candle burning before it, close-up, somber cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Chính những vòng lặp trả thù đó là nền cho câu hỏi của Vinland Saga. Tác giả không phải bịa ra một thế giới b…

```text
Wide 16:9 landscape cinematic frame. a circle of arrows drawn on parchment looping endlessly around a small map of the North Sea, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Những người có thật khác

Lời: Nhiều nhân vật khác trong Vinland Saga cũng có thật. Thorkell Cao lớn là một thủ lĩnh Viking có thật, từng đá…

```text
Wide 16:9 landscape cinematic frame. a massive Norse war camp on an English riverbank with many longships moored, wide shot, misty morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Thorkell thật từng đổi phe nhiều lần: đánh nước Anh, rồi phục vụ vua Anh Æthelred, rồi theo vua Cnut. Cnut ph…

```text
Wide 16:9 landscape cinematic frame. a banner being lowered from one side of a wall and a different banner raised on the other, symbolic wide shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Trong manga, Thorkell là một chiến binh cuồng nhiệt, chỉ muốn đánh nhau với người mạnh. Tính đổi phe trong sử…

```text
Wide 16:9 landscape cinematic frame. a giant silhouette laughing on a battlefield with a broken spear in each hand, dramatic low-angle shot, warm stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Cnut, hay Canute, là vua có thật: vua Anh từ năm 1016, vua Đan Mạch, rồi cả Na Uy. Ông lập nên một đế chế qua…

```text
Wide 16:9 landscape cinematic frame. a map of the North Sea with England, Denmark and Norway shaded in the same color, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Cha của Cnut, vua Sweyn Râu Chẻ, cũng có thật. Ông chiếm được nước Anh năm 1013 và mất vào đầu năm 1014.

```text
Wide 16:9 landscape cinematic frame. an old royal seal pressed into red wax beside a crown resting on a cushion, close-up, cold regal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Có một giai thoại nổi tiếng về Cnut thật: ông ngồi bên bờ biển và ra lệnh cho sóng lùi lại, để cho các cận th…

```text
Wide 16:9 landscape cinematic frame. an empty wooden throne placed on a sandy beach as waves wash around its legs, wide shot, grey dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Trong manga, Cnut thay đổi từ một hoàng tử nhút nhát thành một vị vua lạnh lùng, quyết tâm xây thiên đường tr…

```text
Wide 16:9 landscape cinematic frame. a young silhouette standing on a cliff overlooking a vast sea at dawn, back view, wide shot, cold majestic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Những gì hư cấu

Lời: Askeladd, thủ lĩnh lính đánh thuê, người giết cha Thorfinn và nuôi Thorfinn lớn, là nhân vật hư cấu. Tên của…

```text
Wide 16:9 landscape cinematic frame. an old Norwegian folk tale book opened to an illustration of a young lad by a fireplace, close-up, warm storybook light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Trong truyện, Askeladd tự nhận là hậu duệ của một vị tướng La Mã gắn với truyền thuyết vua Arthur. Đó là một…

```text
Wide 16:9 landscape cinematic frame. a weathered Roman-era stone carving of a warrior beside an old book of Arthurian legends, close-up, misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Mùa hai được nhiều người xem đánh giá là một trong những phần hay nhất của anime, dù không có trận chiến lớn…

```text
Wide 16:9 landscape cinematic frame. a pair of calloused hands planting seeds in a furrowed field at dawn, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nông trại của Ketil ở mùa hai, và những nô lệ như Einar, cũng là sáng tạo. Nhưng cuộc sống của nô lệ Bắc Âu t…

```text
Wide 16:9 landscape cinematic frame. a sprawling Danish farm with wheat fields and a large wooden hall under a wide sky, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Jomsviking, đội chiến binh xuất hiện trong truyện, có trong sử thi. Nhưng các nhà sử học vẫn tranh luận họ có…

```text
Wide 16:9 landscape cinematic frame. a legendary fortress on a misty coast drawn in an old manuscript style, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Vinland có thật: L'Anse aux Meadows

Lời: Và đây là phần Kaku thích nhất. Vinland không chỉ có trong sử thi. Năm 1960, các nhà nghiên cứu Na Uy tìm thấ…

```text
Wide 16:9 landscape cinematic frame. grassy mounds of reconstructed turf houses on a windswept coastal meadow, wide shot, soft overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Đây là bằng chứng khảo cổ đầu tiên và rõ ràng nhất cho thấy người Bắc Âu đã tới châu Mỹ trước Columbus.

```text
Wide 16:9 landscape cinematic frame. an archaeologist's hand brushing soil from an iron rivet at a dig site, extreme close-up, natural daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Năm 2021, một nghiên cứu đăng trên tạp chí Nature dùng vòng gỗ để xác định chính xác: người Bắc Âu đã chặt câ…

```text
Wide 16:9 landscape cinematic frame. a cross-section of an old tree trunk with rings highlighted and a small marker at one ring, close-up, clean scientific light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Bí quyết: năm 993 có một cơn bão tia vũ trụ hiếm gặp, để lại dấu vết trong vòng cây trên toàn thế giới. Đếm t…

```text
Wide 16:9 landscape cinematic frame. a diagram of tree rings with one bright highlighted ring and a count of rings to the outer edge, infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là một trong những khám phá khoa học đẹp nhất: một cơn bão từ vũ trụ giúp ta biết năm chính xác…

```text
Wide 16:9 landscape cinematic frame. the owl mascot counting tree rings on a stump with a tiny pointer, wide-eyed with delight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ngày nay, L'Anse aux Meadows là Di sản Thế giới UNESCO, với những ngôi nhà mái cỏ được dựng lại. Bạn có thể t…

```text
Wide 16:9 landscape cinematic frame. visitors walking along a wooden path toward reconstructed turf houses on a windy coastal meadow, wide shot, soft overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nhưng chưa ai chắc L'Anse aux Meadows có phải chính là Vinland trong sử thi hay không, hay chỉ là một trạm tr…

```text
Wide 16:9 landscape cinematic frame. a coastal map of northeastern North America with a question mark hovering over the southern coast, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Chỗ tác giả thay đổi và vì sao

Lời: Trước đó, hãy nhớ rằng chính các sử thi Iceland cũng không phải ghi chép chính xác từng chữ. Chúng được truyề…

```text
Wide 16:9 landscape cinematic frame. an elder telling a story by a longhouse fire to a group of listeners, wide shot, warm flickering light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Vậy vì sao Yukimura thay đổi lịch sử? Kaku thấy có ba lý do.

```text
Wide 16:9 landscape cinematic frame. a notebook page with three numbered empty lines, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Một: lấp khoảng trống. Sử thi chỉ kể chuyến đi, không kể con người trước chuyến đi. Tác giả tạo nên cả một tu…

```text
Wide 16:9 landscape cinematic frame. a crumbling wall with fresh bricks filling in the gaps, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Hai: đặt câu hỏi cho thời đại. Người Viking thường được tô vẽ là chiến binh oai hùng. Vinland Saga hỏi ngược…

```text
Wide 16:9 landscape cinematic frame. a romantic painting of a heroic warrior hanging on a wall, with a small realistic sketch of a grieving farmer pinned beside it, close-up, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Và tác giả chọn những chi tiết thật một cách rất tinh tế: tên người, tên tàu, tên vùng đất. Người đọc tò mò c…

```text
Wide 16:9 landscape cinematic frame. a manga volume open beside a history encyclopedia with sticky notes connecting pages, close-up, cozy lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Ba: một hành trình của chính tác giả. Yukimura từng chia sẻ rằng ông muốn viết về cách con người vượt qua bạo…

```text
Wide 16:9 landscape cinematic frame. a writer's desk with an open notebook, a stack of history books and a small wooden longship model, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Kaku nghĩ đây là cách dùng lịch sử rất đẹp: không bóp méo những gì đã xảy ra, mà dùng khoảng trống để nói điề…

```text
Wide 16:9 landscape cinematic frame. a gentle hand writing in the margin of an old history book with a quill, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Bản đồ thật và hư cấu

Lời: Và đây là bản đồ trong một hình. Cột thật: Thorfinn Karlsefni, Gudrid, Snorri, Leif Erikson, Thorkell Cao lớn…

```text
Wide 16:9 landscape cinematic frame. a two-column chart on parchment with the left column filled with small rune stamps, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Cột tên thật nhưng đời khác: Thorfinn trong truyện, một chiến binh trả thù rồi bỏ kiếm, và tính cách của Thor…

```text
Wide 16:9 landscape cinematic frame. the middle section of the chart with half-filled circle icons, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Cột hư cấu: Thors, Askeladd, nông trại Ketil, Einar. Và cột còn tranh luận: Jomsviking, và vị trí chính xác c…

```text
Wide 16:9 landscape cinematic frame. the right side of the chart with dotted circle icons and a small question mark note pinned at the edge, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Góc nhìn của Kaku

Lời: Và có lẽ đó là điểm chung sâu nhất: cả hai Thorfinn đều là người dám đi xa khỏi vùng đất quen thuộc, để tìm m…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing on the prow of a ship looking toward a distant unknown coastline, back view, wide shot, golden dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Thorfinn thật đi tìm đất mới để buôn bán. Thorfinn trong truyện đi tìm đất mới để không ai phải cầm kiếm nữa.…

```text
Wide 16:9 landscape cinematic frame. two longships sailing side by side toward the same horizon, one loaded with trade goods and one with farming tools, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và câu hỏi của Thors vẫn còn đó cho chúng ta: nếu không ai có kẻ thù, thì ta đang chiến đấu với ai? Viết suy…

```text
Wide 16:9 landscape cinematic frame. a quiet fjord at dawn with a single empty boat resting on still water, wide shot, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Kết

Lời: Vinland Saga là câu chuyện về một cái tên có thật trong sử thi, được tác giả trao cho một cuộc đời mới, để hỏ…

```text
Wide 16:9 landscape cinematic frame. an old saga manuscript lying open beside a modern manga volume on a wooden table, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Video tiếp theo, Kaku mở một hệ thống sức mạnh kỳ lạ: Hell's Paradise, và khái niệm Đạo, cân bằng âm dương, t…

```text
Wide 16:9 landscape cinematic frame. a mysterious island covered in strange flowers under a misty sky, a small boat approaching the shore, wide shot, eerie beautiful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video đặt anime cạnh lịch sử thật, hãy đăng ký kênh. Kaku sẽ tiếp tục đi tìm những câu ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the old map and waving from the bow of a tiny longship. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Vinland Saga là gì?

Khoảng 125 giây · cảnh s01–s11 · 1623 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime Vinland Saga mùa hai, và nhắc nhẹ hướng đi của manga, đã kết thúc năm 2025. Phần lịch sử thật thì không phải spoiler, nó đã xảy ra từ một nghìn năm trước.

<short pause> Câu chuyện này có thật hơn bạn nghĩ. Khoảng năm 1010, một người Iceland tên Thorfinn dẫn ba con tàu vượt biển Bắc Đại Tây Dương, tới một vùng đất mà người châu Âu chưa từng sống: châu Mỹ.

<short pause> Gần năm trăm năm trước Columbus. Và tên của ông, Thorfinn, chính là cái tên mà tác giả Yukimura Makoto chọn cho nhân vật chính của Vinland Saga.

<short pause> Câu hỏi hôm nay: trong Vinland Saga, bao nhiêu là thật? Thorfinn thật là ai? Người Viking thật sống thế nào? Và tác giả đã thay đổi những gì, vì sao?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đặt Vinland Saga cạnh những bộ sử thi Iceland. Cuối video là bản đồ thật và hư cấu trong một hình.

<short pause> Như mọi video dạng này, Kaku không vẽ chân dung người thật. Kaku dùng tàu, cổ vật, bản đồ, và những bóng người.

<short pause> Vinland Saga là manga của Yukimura Makoto, đăng từ năm 2005 và kết thúc với chương hai trăm hai mươi vào tháng bảy năm 2025, sau đúng hai mươi năm.

<short pause> Anime mùa một do WIT Studio làm năm 2019, mùa hai do MAPPA làm năm 2023. Hai mùa rất khác nhau: mùa một là chiến tranh, mùa hai là một nông trại.

<short pause> Câu chuyện theo Thorfinn, cậu bé chứng kiến cha mình bị giết, rồi lớn lên trong băng lính đánh thuê của kẻ thù, chỉ sống để trả thù.

<short pause> Nhiều người xem thích Vinland Saga vì nó dám thay đổi thể loại giữa chừng: từ một bộ hành động về chiến binh, thành một câu chuyện về chuộc lỗi và hòa bình.

<short pause> Rồi, sau tất cả, cậu bỏ kiếm, và mơ đưa mọi người tới một vùng đất không có chiến tranh, không có nô lệ: Vinland.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime Vinland Saga mùa hai, và nhắc nhẹ hướng đi của manga, đã kết thúc năm 2025. Phần lịch sử thật thì không phải spoiler, nó đã xảy ra từ một nghìn năm trước.

[pause] Câu chuyện này có thật hơn bạn nghĩ. Khoảng năm 1010, một người Iceland tên Thorfinn dẫn ba con tàu vượt biển Bắc Đại Tây Dương, tới một vùng đất mà người châu Âu chưa từng sống: châu Mỹ.

[pause] Gần năm trăm năm trước Columbus. Và tên của ông, Thorfinn, chính là cái tên mà tác giả Yukimura Makoto chọn cho nhân vật chính của Vinland Saga.

[pause] [curious] Câu hỏi hôm nay: trong Vinland Saga, bao nhiêu là thật? Thorfinn thật là ai? Người Viking thật sống thế nào? Và tác giả đã thay đổi những gì, vì sao?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đặt Vinland Saga cạnh những bộ sử thi Iceland. Cuối video là bản đồ thật và hư cấu trong một hình.

[pause] Như mọi video dạng này, Kaku không vẽ chân dung người thật. Kaku dùng tàu, cổ vật, bản đồ, và những bóng người.

[pause] Vinland Saga là manga của Yukimura Makoto, đăng từ năm 2005 và kết thúc với chương hai trăm hai mươi vào tháng bảy năm 2025, sau đúng hai mươi năm.

[pause] Anime mùa một do WIT Studio làm năm 2019, mùa hai do MAPPA làm năm 2023. Hai mùa rất khác nhau: mùa một là chiến tranh, mùa hai là một nông trại.

[pause] Câu chuyện theo Thorfinn, cậu bé chứng kiến cha mình bị giết, rồi lớn lên trong băng lính đánh thuê của kẻ thù, chỉ sống để trả thù.

[pause] Nhiều người xem thích Vinland Saga vì nó dám thay đổi thể loại giữa chừng: từ một bộ hành động về chiến binh, thành một câu chuyện về chuộc lỗi và hòa bình.

[pause] Rồi, sau tất cả, cậu bỏ kiếm, và mơ đưa mọi người tới một vùng đất không có chiến tranh, không có nô lệ: Vinland.
```

### c02 · Người Viking thật / Thế giới Bắc Âu năm 1000

Khoảng 138 giây · cảnh s12–s22 · 1789 ký tự

**Gemini**

```text
Trước hết, người Viking thật là ai? Viking không phải một dân tộc, mà là cách gọi những người Bắc Âu đi biển để buôn bán, cướp bóc, hay định cư, khoảng từ cuối thế kỷ tám tới thế kỷ mười một.

<short pause> Phần lớn thời gian, họ là nông dân, thợ thủ công, thương nhân. Đi biển cướp bóc chỉ là một phần, dù là phần nổi tiếng nhất.

<short pause> Một hiểu lầm lớn: mũ sừng. Chưa có bằng chứng khảo cổ nào cho thấy chiến binh Viking đội mũ có sừng. Hình ảnh đó phổ biến từ trang phục sân khấu ở châu Âu thế kỷ mười chín.

<short pause> Tàu Viking cũng là một kỳ quan kỹ thuật: đáy nông để vào được sông, thân ghép ván chồng lên nhau cho mềm dẻo, vừa có buồm vừa có mái chèo. Những con tàu như tàu Gokstad ở Na Uy vẫn còn tới ngày nay.

<short pause> <laugh> Kaku để ý: Vinland Saga không cho nhân vật đội mũ sừng. Tác giả đã nghiên cứu rất kỹ trang phục, vũ khí và tàu thuyền thời đó.

<short pause> Người Viking cũng buôn bán nô lệ, gọi là thrall. Tù binh từ các cuộc cướp bóc bị bán qua nhiều vùng. Mùa hai của Vinland Saga, với Thorfinn làm nô lệ ở nông trại, dựa trên sự thật tàn khốc này.

<short pause> Để hiểu Thorfinn thật, hãy nhìn thế giới của ông. Người Bắc Âu định cư ở Iceland từ cuối thế kỷ chín, trên một hòn đảo núi lửa gần như không người.

<short pause> Năm 930, họ lập ra Althing, một hội nghị nơi các thủ lĩnh gặp nhau hằng năm để làm luật và xử án. Nhiều người gọi đó là một trong những nghị viện lâu đời nhất thế giới.

<short pause> Khoảng năm 985, Erik Đỏ, bị trục xuất khỏi Iceland, đi về phía tây và lập khu định cư ở Greenland. Ông đặt tên Greenland, vùng đất xanh, để thu hút người tới ở.

<short pause> Và khoảng năm 1000, Iceland chính thức chuyển sang Kitô giáo qua một quyết định tại Althing. Thế giới của Thorfinn là một thế giới đang thay đổi rất nhanh.

<short pause> Kaku để ý: Vinland Saga cũng là một câu chuyện về thời đại chuyển giao. Giữa thần cũ và thần mới, giữa cướp bóc và làm ruộng, con người phải chọn cách sống.
```

**ElevenLabs**

```text
[curious] Trước hết, người Viking thật là ai? Viking không phải một dân tộc, mà là cách gọi những người Bắc Âu đi biển để buôn bán, cướp bóc, hay định cư, khoảng từ cuối thế kỷ tám tới thế kỷ mười một.

[pause] Phần lớn thời gian, họ là nông dân, thợ thủ công, thương nhân. Đi biển cướp bóc chỉ là một phần, dù là phần nổi tiếng nhất.

[pause] Một hiểu lầm lớn: mũ sừng. Chưa có bằng chứng khảo cổ nào cho thấy chiến binh Viking đội mũ có sừng. Hình ảnh đó phổ biến từ trang phục sân khấu ở châu Âu thế kỷ mười chín.

[pause] Tàu Viking cũng là một kỳ quan kỹ thuật: đáy nông để vào được sông, thân ghép ván chồng lên nhau cho mềm dẻo, vừa có buồm vừa có mái chèo. Những con tàu như tàu Gokstad ở Na Uy vẫn còn tới ngày nay.

[pause] [chuckles] Kaku để ý: Vinland Saga không cho nhân vật đội mũ sừng. Tác giả đã nghiên cứu rất kỹ trang phục, vũ khí và tàu thuyền thời đó.

[pause] Người Viking cũng buôn bán nô lệ, gọi là thrall. Tù binh từ các cuộc cướp bóc bị bán qua nhiều vùng. Mùa hai của Vinland Saga, với Thorfinn làm nô lệ ở nông trại, dựa trên sự thật tàn khốc này.

[pause] Để hiểu Thorfinn thật, hãy nhìn thế giới của ông. Người Bắc Âu định cư ở Iceland từ cuối thế kỷ chín, trên một hòn đảo núi lửa gần như không người.

[pause] Năm 930, họ lập ra Althing, một hội nghị nơi các thủ lĩnh gặp nhau hằng năm để làm luật và xử án. Nhiều người gọi đó là một trong những nghị viện lâu đời nhất thế giới.

[pause] Khoảng năm 985, Erik Đỏ, bị trục xuất khỏi Iceland, đi về phía tây và lập khu định cư ở Greenland. Ông đặt tên Greenland, vùng đất xanh, để thu hút người tới ở.

[pause] Và khoảng năm 1000, Iceland chính thức chuyển sang Kitô giáo qua một quyết định tại Althing. Thế giới của Thorfinn là một thế giới đang thay đổi rất nhanh.

[pause] Kaku để ý: Vinland Saga cũng là một câu chuyện về thời đại chuyển giao. Giữa thần cũ và thần mới, giữa cướp bóc và làm ruộng, con người phải chọn cách sống.
```

### c03 · Leif Erikson và Vinland đầu tiên / Thorfinn thật

Khoảng 126 giây · cảnh s23–s33 · 1642 ký tự

**Gemini**

```text
Người đầu tiên tới Vinland theo sử thi là Leif Erikson, con trai của Erik Đỏ, khoảng năm 1000.

<short pause> Leif đặt tên cho ba vùng đất: Helluland, vùng đá phẳng; Markland, vùng rừng; và Vinland. Các nhà nghiên cứu cho rằng chúng tương ứng với những vùng bờ biển đông bắc Bắc Mỹ ngày nay.

<short pause> Vinland thường được hiểu là vùng đất nho, vì sử thi kể họ tìm thấy nho mọc hoang. Có học giả hiểu khác, nhưng cách hiểu vùng đất nho là phổ biến nhất.

<short pause> Thorfinn Karlsefni đi sau Leif vài năm, với ý định không chỉ khám phá, mà định cư lâu dài: mang theo người, gia súc, và cả phụ nữ.

<short pause> Thorfinn thật tên đầy đủ là Thorfinn Karlsefni. Karlsefni nghĩa là người có tố chất của một người đàn ông thực thụ. Ông là một thương nhân Iceland.

<short pause> Chuyện của ông được ghi lại trong hai bộ sử thi Iceland: Sử thi về Erik Đỏ, và Sử thi về người Greenland. Cả hai được viết lại nhiều thế kỷ sau sự kiện.

<short pause> Theo sử thi, Thorfinn dẫn ba con tàu từ Greenland đi về phía tây, theo con đường mà Leif Erikson đã mở ra khoảng bảy năm trước. Họ tới vùng đất mà người Bắc Âu gọi là Vinland.

<short pause> Vợ ông là Gudrid, một người phụ nữ phi thường, đã đi qua gần hết thế giới Bắc Âu thời đó. Và con trai họ, Snorri, được cho là đứa trẻ châu Âu đầu tiên sinh ra ở Bắc Mỹ.

<short pause> Sử thi kể về những lần trao đổi hàng hóa với người bản địa, rồi những hiểu lầm và xung đột. Người Bắc Âu ít người, ở quá xa quê nhà, và không thể ở lại.

<short pause> Sau khoảng ba năm, nhóm của Thorfinn rời Vinland. Sử thi kể về những xung đột với cư dân bản địa. Người Bắc Âu không ở lại lâu dài.

<short pause> Và Thorfinn thật không phải một chiến binh trả thù. Ông là thương nhân, người đi tìm vùng đất mới để làm ăn và định cư. Nhân vật trong manga có cuộc đời rất khác.
```

**ElevenLabs**

```text
Người đầu tiên tới Vinland theo sử thi là Leif Erikson, con trai của Erik Đỏ, khoảng năm 1000.

[pause] Leif đặt tên cho ba vùng đất: Helluland, vùng đá phẳng; Markland, vùng rừng; và Vinland. Các nhà nghiên cứu cho rằng chúng tương ứng với những vùng bờ biển đông bắc Bắc Mỹ ngày nay.

[pause] Vinland thường được hiểu là vùng đất nho, vì sử thi kể họ tìm thấy nho mọc hoang. Có học giả hiểu khác, nhưng cách hiểu vùng đất nho là phổ biến nhất.

[pause] Thorfinn Karlsefni đi sau Leif vài năm, với ý định không chỉ khám phá, mà định cư lâu dài: mang theo người, gia súc, và cả phụ nữ.

[pause] Thorfinn thật tên đầy đủ là Thorfinn Karlsefni. Karlsefni nghĩa là người có tố chất của một người đàn ông thực thụ. Ông là một thương nhân Iceland.

[pause] Chuyện của ông được ghi lại trong hai bộ sử thi Iceland: Sử thi về Erik Đỏ, và Sử thi về người Greenland. Cả hai được viết lại nhiều thế kỷ sau sự kiện.

[pause] Theo sử thi, Thorfinn dẫn ba con tàu từ Greenland đi về phía tây, theo con đường mà Leif Erikson đã mở ra khoảng bảy năm trước. Họ tới vùng đất mà người Bắc Âu gọi là Vinland.

[pause] Vợ ông là Gudrid, một người phụ nữ phi thường, đã đi qua gần hết thế giới Bắc Âu thời đó. Và con trai họ, Snorri, được cho là đứa trẻ châu Âu đầu tiên sinh ra ở Bắc Mỹ.

[pause] Sử thi kể về những lần trao đổi hàng hóa với người bản địa, rồi những hiểu lầm và xung đột. Người Bắc Âu ít người, ở quá xa quê nhà, và không thể ở lại.

[pause] Sau khoảng ba năm, nhóm của Thorfinn rời Vinland. Sử thi kể về những xung đột với cư dân bản địa. Người Bắc Âu không ở lại lâu dài.

[pause] Và Thorfinn thật không phải một chiến binh trả thù. Ông là thương nhân, người đi tìm vùng đất mới để làm ăn và định cư. Nhân vật trong manga có cuộc đời rất khác.
```

### c04 · Chỗ tác giả thay đổi: Thorfinn trong truyện / Chiến tranh ở nước Anh

Khoảng 114 giây · cảnh s34–s43 · 1484 ký tự

**Gemini**

```text
Vậy Yukimura đã lấy gì và đổi gì? Ông lấy cái tên, và điểm đến: Vinland. <short pause> Nhưng gần như toàn bộ tuổi thơ và tuổi trẻ của Thorfinn trong truyện là sáng tạo.

<short pause> Sử thi gần như không kể gì về thời trẻ của Thorfinn Karlsefni. Và cũng như Kingdom, khoảng trống đó là món quà cho tác giả.

<short pause> Cha của Thorfinn trong truyện là Thors, một chiến binh huyền thoại đã bỏ kiếm. Cha thật của Thorfinn Karlsefni, theo sử thi, là một người khác. Tác giả tạo ra Thors để đặt câu hỏi về bạo lực.

<short pause> Câu nói nổi tiếng của Thors, đại ý: con không có kẻ thù nào cả, không ai có kẻ thù cả. Câu đó trở thành trái tim của cả bộ truyện.

<short pause> Ở cuối manga, Thorfinn trong truyện thật sự đi tới Vinland, như Thorfinn thật. Hai cuộc đời khác nhau hội tụ ở cùng một điểm đến. Kaku sẽ không kể thêm.

<short pause> Kaku thấy tác giả chọn một thương nhân có thật làm khung, rồi lấp vào đó hành trình từ trả thù tới hòa bình. Lịch sử cho đích đến, còn con đường là của nhà văn.

<short pause> Phần đầu Vinland Saga diễn ra trong những cuộc chiến của người Đan Mạch ở Anh. Bối cảnh này cũng có thật.

<short pause> Để mua bình yên, nước Anh nhiều lần phải trả cho người Viking những khoản tiền cống nạp lớn bằng bạc, sau này được gọi là Danegeld.

<short pause> Năm 1002, vua Anh Æthelred ra lệnh giết những người Đan Mạch sống ở Anh, sự kiện gọi là vụ thảm sát ngày thánh Brice. Nhiều sử gia cho rằng nó góp phần khiến người Đan Mạch trả thù dữ dội hơn.

<short pause> Chính những vòng lặp trả thù đó là nền cho câu hỏi của Vinland Saga. Tác giả không phải bịa ra một thế giới bạo lực. Ông chỉ cần nhìn vào lịch sử.
```

**ElevenLabs**

```text
[curious] Vậy Yukimura đã lấy gì và đổi gì? Ông lấy cái tên, và điểm đến: Vinland. [pause] Nhưng gần như toàn bộ tuổi thơ và tuổi trẻ của Thorfinn trong truyện là sáng tạo.

[pause] Sử thi gần như không kể gì về thời trẻ của Thorfinn Karlsefni. Và cũng như Kingdom, khoảng trống đó là món quà cho tác giả.

[pause] Cha của Thorfinn trong truyện là Thors, một chiến binh huyền thoại đã bỏ kiếm. Cha thật của Thorfinn Karlsefni, theo sử thi, là một người khác. Tác giả tạo ra Thors để đặt câu hỏi về bạo lực.

[pause] Câu nói nổi tiếng của Thors, đại ý: con không có kẻ thù nào cả, không ai có kẻ thù cả. Câu đó trở thành trái tim của cả bộ truyện.

[pause] Ở cuối manga, Thorfinn trong truyện thật sự đi tới Vinland, như Thorfinn thật. Hai cuộc đời khác nhau hội tụ ở cùng một điểm đến. Kaku sẽ không kể thêm.

[pause] Kaku thấy tác giả chọn một thương nhân có thật làm khung, rồi lấp vào đó hành trình từ trả thù tới hòa bình. Lịch sử cho đích đến, còn con đường là của nhà văn.

[pause] Phần đầu Vinland Saga diễn ra trong những cuộc chiến của người Đan Mạch ở Anh. Bối cảnh này cũng có thật.

[pause] Để mua bình yên, nước Anh nhiều lần phải trả cho người Viking những khoản tiền cống nạp lớn bằng bạc, sau này được gọi là Danegeld.

[pause] Năm 1002, vua Anh Æthelred ra lệnh giết những người Đan Mạch sống ở Anh, sự kiện gọi là vụ thảm sát ngày thánh Brice. Nhiều sử gia cho rằng nó góp phần khiến người Đan Mạch trả thù dữ dội hơn.

[pause] Chính những vòng lặp trả thù đó là nền cho câu hỏi của Vinland Saga. Tác giả không phải bịa ra một thế giới bạo lực. Ông chỉ cần nhìn vào lịch sử.
```

### c05 · Những người có thật khác / Những gì hư cấu

Khoảng 146 giây · cảnh s44–s55 · 1900 ký tự

**Gemini**

```text
Nhiều nhân vật khác trong Vinland Saga cũng có thật. Thorkell Cao lớn là một thủ lĩnh Viking có thật, từng đánh ở Anh đầu thế kỷ mười một.

<short pause> Thorkell thật từng đổi phe nhiều lần: đánh nước Anh, rồi phục vụ vua Anh Æthelred, rồi theo vua Cnut. Cnut phong ông làm bá tước vùng Đông Anglia năm 1017.

<short pause> Trong manga, Thorkell là một chiến binh cuồng nhiệt, chỉ muốn đánh nhau với người mạnh. Tính đổi phe trong sử thật được tác giả diễn giải thành một người chỉ đi theo trận đấu hay nhất.

<short pause> Cnut, hay Canute, là vua có thật: vua Anh từ năm 1016, vua Đan Mạch, rồi cả Na Uy. Ông lập nên một đế chế quanh biển Bắc.

<short pause> Cha của Cnut, vua Sweyn Râu Chẻ, cũng có thật. Ông chiếm được nước Anh năm 1013 và mất vào đầu năm 1014.

<short pause> Có một giai thoại nổi tiếng về Cnut thật: ông ngồi bên bờ biển và ra lệnh cho sóng lùi lại, để cho các cận thần thấy rằng quyền lực của vua cũng có giới hạn. Đây là giai thoại được kể lại, không chắc đã xảy ra.

<short pause> Trong manga, Cnut thay đổi từ một hoàng tử nhút nhát thành một vị vua lạnh lùng, quyết tâm xây thiên đường trên mặt đất bằng mọi giá. Sự thay đổi đó là sáng tạo, nhưng đế chế thì có thật.

<short pause> Askeladd, thủ lĩnh lính đánh thuê, người giết cha Thorfinn và nuôi Thorfinn lớn, là nhân vật hư cấu. Tên của ông lấy từ một nhân vật trong truyện cổ tích Na Uy, cậu bé Askeladden.

<short pause> Trong truyện, Askeladd tự nhận là hậu duệ của một vị tướng La Mã gắn với truyền thuyết vua Arthur. Đó là một lớp truyền thuyết chồng lên hư cấu.

<short pause> Mùa hai được nhiều người xem đánh giá là một trong những phần hay nhất của anime, dù không có trận chiến lớn nào. Nó cho thấy một chiến binh học lại cách làm người, bằng tay trồng lúa mì.

<short pause> Nông trại của Ketil ở mùa hai, và những nô lệ như Einar, cũng là sáng tạo. <short pause> Nhưng cuộc sống của nô lệ Bắc Âu thời đó thì dựa trên tư liệu thật.

<short pause> Jomsviking, đội chiến binh xuất hiện trong truyện, có trong sử thi. <short pause> Nhưng các nhà sử học vẫn tranh luận họ có thật như lời kể hay chỉ là huyền thoại.
```

**ElevenLabs**

```text
Nhiều nhân vật khác trong Vinland Saga cũng có thật. Thorkell Cao lớn là một thủ lĩnh Viking có thật, từng đánh ở Anh đầu thế kỷ mười một.

[pause] Thorkell thật từng đổi phe nhiều lần: đánh nước Anh, rồi phục vụ vua Anh Æthelred, rồi theo vua Cnut. Cnut phong ông làm bá tước vùng Đông Anglia năm 1017.

[pause] Trong manga, Thorkell là một chiến binh cuồng nhiệt, chỉ muốn đánh nhau với người mạnh. Tính đổi phe trong sử thật được tác giả diễn giải thành một người chỉ đi theo trận đấu hay nhất.

[pause] Cnut, hay Canute, là vua có thật: vua Anh từ năm 1016, vua Đan Mạch, rồi cả Na Uy. Ông lập nên một đế chế quanh biển Bắc.

[pause] Cha của Cnut, vua Sweyn Râu Chẻ, cũng có thật. Ông chiếm được nước Anh năm 1013 và mất vào đầu năm 1014.

[pause] Có một giai thoại nổi tiếng về Cnut thật: ông ngồi bên bờ biển và ra lệnh cho sóng lùi lại, để cho các cận thần thấy rằng quyền lực của vua cũng có giới hạn. Đây là giai thoại được kể lại, không chắc đã xảy ra.

[pause] Trong manga, Cnut thay đổi từ một hoàng tử nhút nhát thành một vị vua lạnh lùng, quyết tâm xây thiên đường trên mặt đất bằng mọi giá. Sự thay đổi đó là sáng tạo, nhưng đế chế thì có thật.

[pause] Askeladd, thủ lĩnh lính đánh thuê, người giết cha Thorfinn và nuôi Thorfinn lớn, là nhân vật hư cấu. Tên của ông lấy từ một nhân vật trong truyện cổ tích Na Uy, cậu bé Askeladden.

[pause] Trong truyện, Askeladd tự nhận là hậu duệ của một vị tướng La Mã gắn với truyền thuyết vua Arthur. Đó là một lớp truyền thuyết chồng lên hư cấu.

[pause] Mùa hai được nhiều người xem đánh giá là một trong những phần hay nhất của anime, dù không có trận chiến lớn nào. Nó cho thấy một chiến binh học lại cách làm người, bằng tay trồng lúa mì.

[pause] Nông trại của Ketil ở mùa hai, và những nô lệ như Einar, cũng là sáng tạo. [pause] Nhưng cuộc sống của nô lệ Bắc Âu thời đó thì dựa trên tư liệu thật.

[pause] Jomsviking, đội chiến binh xuất hiện trong truyện, có trong sử thi. [pause] Nhưng các nhà sử học vẫn tranh luận họ có thật như lời kể hay chỉ là huyền thoại.
```

### c06 · Vinland có thật: L'Anse aux Meadows

Khoảng 84 giây · cảnh s56–s62 · 1090 ký tự

**Gemini**

```text
Và đây là phần Kaku thích nhất. Vinland không chỉ có trong sử thi. Năm 1960, các nhà nghiên cứu Na Uy tìm thấy dấu vết một khu định cư Bắc Âu ở Newfoundland, Canada, tại một nơi tên L'Anse aux Meadows.

<short pause> Đây là bằng chứng khảo cổ đầu tiên và rõ ràng nhất cho thấy người Bắc Âu đã tới châu Mỹ trước Columbus.

<short pause> Năm 2021, một nghiên cứu đăng trên tạp chí Nature dùng vòng gỗ để xác định chính xác: người Bắc Âu đã chặt cây ở đây vào năm 1021.

<short pause> Bí quyết: năm 993 có một cơn bão tia vũ trụ hiếm gặp, để lại dấu vết trong vòng cây trên toàn thế giới. Đếm từ vòng đó ra tới vỏ cây là hai mươi tám vòng. 993 cộng 28 là 1021.

<short pause> <laugh> Kaku thấy đây là một trong những khám phá khoa học đẹp nhất: một cơn bão từ vũ trụ giúp ta biết năm chính xác người Viking cầm rìu ở châu Mỹ.

<short pause> Ngày nay, L'Anse aux Meadows là Di sản Thế giới UNESCO, với những ngôi nhà mái cỏ được dựng lại. Bạn có thể tới đó và đứng đúng nơi người Bắc Âu từng đứng một nghìn năm trước.

<short pause> Nhưng chưa ai chắc L'Anse aux Meadows có phải chính là Vinland trong sử thi hay không, hay chỉ là một trạm trung chuyển. Vinland có thể rộng hơn, xa hơn về phía nam.
```

**ElevenLabs**

```text
Và đây là phần Kaku thích nhất. Vinland không chỉ có trong sử thi. Năm 1960, các nhà nghiên cứu Na Uy tìm thấy dấu vết một khu định cư Bắc Âu ở Newfoundland, Canada, tại một nơi tên L'Anse aux Meadows.

[pause] Đây là bằng chứng khảo cổ đầu tiên và rõ ràng nhất cho thấy người Bắc Âu đã tới châu Mỹ trước Columbus.

[pause] Năm 2021, một nghiên cứu đăng trên tạp chí Nature dùng vòng gỗ để xác định chính xác: người Bắc Âu đã chặt cây ở đây vào năm 1021.

[pause] Bí quyết: năm 993 có một cơn bão tia vũ trụ hiếm gặp, để lại dấu vết trong vòng cây trên toàn thế giới. Đếm từ vòng đó ra tới vỏ cây là hai mươi tám vòng. 993 cộng 28 là 1021.

[pause] [chuckles] Kaku thấy đây là một trong những khám phá khoa học đẹp nhất: một cơn bão từ vũ trụ giúp ta biết năm chính xác người Viking cầm rìu ở châu Mỹ.

[pause] Ngày nay, L'Anse aux Meadows là Di sản Thế giới UNESCO, với những ngôi nhà mái cỏ được dựng lại. Bạn có thể tới đó và đứng đúng nơi người Bắc Âu từng đứng một nghìn năm trước.

[pause] Nhưng chưa ai chắc L'Anse aux Meadows có phải chính là Vinland trong sử thi hay không, hay chỉ là một trạm trung chuyển. Vinland có thể rộng hơn, xa hơn về phía nam.
```

### c07 · Chỗ tác giả thay đổi và vì sao / Bản đồ thật và hư cấu / Góc nhìn của Kaku

Khoảng 141 giây · cảnh s63–s75 · 1829 ký tự

**Gemini**

```text
Trước đó, hãy nhớ rằng chính các sử thi Iceland cũng không phải ghi chép chính xác từng chữ. Chúng được truyền miệng qua nhiều thế hệ rồi mới được viết lại. Lịch sử của người Viking vốn đã là một câu chuyện được kể.

<short pause> Vậy vì sao Yukimura thay đổi lịch sử? Kaku thấy có ba lý do.

<short pause> Một: lấp khoảng trống. Sử thi chỉ kể chuyến đi, không kể con người trước chuyến đi. Tác giả tạo nên cả một tuổi trẻ đầy máu và hối hận.

<short pause> Hai: đặt câu hỏi cho thời đại. Người Viking thường được tô vẽ là chiến binh oai hùng. Vinland Saga hỏi ngược lại: bạo lực đó có ý nghĩa gì với người bị cướp, bị bán làm nô lệ?

<short pause> Và tác giả chọn những chi tiết thật một cách rất tinh tế: tên người, tên tàu, tên vùng đất. Người đọc tò mò có thể tự tra, và sẽ thấy lịch sử hiện ra sau từng trang.

<short pause> Ba: một hành trình của chính tác giả. Yukimura từng chia sẻ rằng ông muốn viết về cách con người vượt qua bạo lực. Thorfinn là câu trả lời của ông.

<short pause> Kaku nghĩ đây là cách dùng lịch sử rất đẹp: không bóp méo những gì đã xảy ra, mà dùng khoảng trống để nói điều mình tin.

<short pause> Và đây là bản đồ trong một hình. Cột thật: Thorfinn Karlsefni, Gudrid, Snorri, Leif Erikson, Thorkell Cao lớn, Cnut, Sweyn, chuyến đi tới Vinland, và L'Anse aux Meadows năm 1021.

<short pause> Cột tên thật nhưng đời khác: Thorfinn trong truyện, một chiến binh trả thù rồi bỏ kiếm, và tính cách của Thorkell, Cnut.

<short pause> Cột hư cấu: Thors, Askeladd, nông trại Ketil, Einar. Và cột còn tranh luận: Jomsviking, và vị trí chính xác của Vinland.

<short pause> Và có lẽ đó là điểm chung sâu nhất: cả hai Thorfinn đều là người dám đi xa khỏi vùng đất quen thuộc, để tìm một cách sống mới.

<short pause> Thorfinn thật đi tìm đất mới để buôn bán. Thorfinn trong truyện đi tìm đất mới để không ai phải cầm kiếm nữa. Kaku thích cả hai.

<short pause> Và câu hỏi của Thors vẫn còn đó cho chúng ta: nếu không ai có kẻ thù, thì ta đang chiến đấu với ai? Viết suy nghĩ của bạn vào bình luận nhé.
```

**ElevenLabs**

```text
Trước đó, hãy nhớ rằng chính các sử thi Iceland cũng không phải ghi chép chính xác từng chữ. Chúng được truyền miệng qua nhiều thế hệ rồi mới được viết lại. Lịch sử của người Viking vốn đã là một câu chuyện được kể.

[pause] [curious] Vậy vì sao Yukimura thay đổi lịch sử? Kaku thấy có ba lý do.

[pause] Một: lấp khoảng trống. Sử thi chỉ kể chuyến đi, không kể con người trước chuyến đi. Tác giả tạo nên cả một tuổi trẻ đầy máu và hối hận.

[pause] Hai: đặt câu hỏi cho thời đại. Người Viking thường được tô vẽ là chiến binh oai hùng. Vinland Saga hỏi ngược lại: bạo lực đó có ý nghĩa gì với người bị cướp, bị bán làm nô lệ?

[pause] Và tác giả chọn những chi tiết thật một cách rất tinh tế: tên người, tên tàu, tên vùng đất. Người đọc tò mò có thể tự tra, và sẽ thấy lịch sử hiện ra sau từng trang.

[pause] Ba: một hành trình của chính tác giả. Yukimura từng chia sẻ rằng ông muốn viết về cách con người vượt qua bạo lực. Thorfinn là câu trả lời của ông.

[pause] Kaku nghĩ đây là cách dùng lịch sử rất đẹp: không bóp méo những gì đã xảy ra, mà dùng khoảng trống để nói điều mình tin.

[pause] Và đây là bản đồ trong một hình. Cột thật: Thorfinn Karlsefni, Gudrid, Snorri, Leif Erikson, Thorkell Cao lớn, Cnut, Sweyn, chuyến đi tới Vinland, và L'Anse aux Meadows năm 1021.

[pause] Cột tên thật nhưng đời khác: Thorfinn trong truyện, một chiến binh trả thù rồi bỏ kiếm, và tính cách của Thorkell, Cnut.

[pause] Cột hư cấu: Thors, Askeladd, nông trại Ketil, Einar. Và cột còn tranh luận: Jomsviking, và vị trí chính xác của Vinland.

[pause] Và có lẽ đó là điểm chung sâu nhất: cả hai Thorfinn đều là người dám đi xa khỏi vùng đất quen thuộc, để tìm một cách sống mới.

[pause] Thorfinn thật đi tìm đất mới để buôn bán. Thorfinn trong truyện đi tìm đất mới để không ai phải cầm kiếm nữa. Kaku thích cả hai.

[pause] Và câu hỏi của Thors vẫn còn đó cho chúng ta: nếu không ai có kẻ thù, thì ta đang chiến đấu với ai? Viết suy nghĩ của bạn vào bình luận nhé.
```

### c08 · Kết

Khoảng 38 giây · cảnh s76–s78 · 495 ký tự

**Gemini**

```text
Vinland Saga là câu chuyện về một cái tên có thật trong sử thi, được tác giả trao cho một cuộc đời mới, để hỏi một câu hỏi rất cũ: làm sao để sống mà không cần kẻ thù.

<short pause> Video tiếp theo, Kaku mở một hệ thống sức mạnh kỳ lạ: Hell's Paradise, và khái niệm Đạo, cân bằng âm dương, trên một hòn đảo mà ai cũng muốn tìm thuốc trường sinh.

<short pause> Nếu bạn thích những video đặt anime cạnh lịch sử thật, hãy đăng ký kênh. <laugh> Kaku sẽ tiếp tục đi tìm những câu chuyện có thật hơn bạn nghĩ. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Vinland Saga là câu chuyện về một cái tên có thật trong sử thi, được tác giả trao cho một cuộc đời mới, để hỏi một câu hỏi rất cũ: làm sao để sống mà không cần kẻ thù.

[pause] Video tiếp theo, Kaku mở một hệ thống sức mạnh kỳ lạ: Hell's Paradise, và khái niệm Đạo, cân bằng âm dương, trên một hòn đảo mà ai cũng muốn tìm thuốc trường sinh.

[pause] Nếu bạn thích những video đặt anime cạnh lịch sử thật, hãy đăng ký kênh. [chuckles] Kaku sẽ tiếp tục đi tìm những câu chuyện có thật hơn bạn nghĩ. Kaku gấp sổ đây, hẹn gặp lại!
```
