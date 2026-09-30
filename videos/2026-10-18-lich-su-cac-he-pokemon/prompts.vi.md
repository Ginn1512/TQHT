# Bộ prompt · Pokémon: Lịch sử các hệ từ 15 lên 18 — vì sao phải thêm Bóng tối, Thép và Tiên?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 9 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (86 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Video này không có spoiler cốt truyện. Kaku chỉ nói về luật chơi, chủ yếu trong các phiên bản trò chơi chính,…

```text
Wide 16:9 landscape cinematic frame. a cozy bedroom desk with an old handheld game console, a notebook and a small lamp, wide establishing shot, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Năm 1996, một trò chơi trên máy cầm tay ra mắt ở Nhật Bản với mười lăm hệ. Lửa, Nước, Cỏ, Điện, và mười một h…

```text
Wide 16:9 landscape cinematic frame. a vintage handheld console with a small greenish screen showing a simple grid of fifteen icons, close-up, soft nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Ba mươi năm sau, con số đó là mười tám. Bảng tương khắc có ba trăm hai mươi bốn ô, và mỗi ô là một luật nhỏ q…

```text
Wide 16:9 landscape cinematic frame. a large modern type chart grid of 18 by 18 colorful cells glowing on a screen, wide shot, vibrant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng ba hệ mới không được thêm vào cho vui. Mỗi hệ ra đời để sửa một vấn đề của bảng cũ. Và có một hệ từng m…

```text
Wide 16:9 landscape cinematic frame. a single glowing violet icon sitting on top of a pile of defeated icons, dramatic spotlight, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Ở Việt Nam, nhiều thế hệ biết tới Pokémon qua truyện tranh, phim hoạt hình trên truyền hình và những tấm thẻ…

```text
Wide 16:9 landscape cinematic frame. a group of kids trading colorful cards on the steps outside a school gate in the afternoon, medium shot, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Và câu trả lời cho cuộc tranh cãi đó đã thay đổi nhiều lần trong ba mươi năm. Đó chính là nội dung hôm nay.

```text
Wide 16:9 landscape cinematic frame. an old notebook page with a childish drawing of a ranking of elemental icons, several names crossed out and rewritten, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Nhân dịp Pokémon vừa tròn ba mươi tuổi, hôm nay Kaku kể lại lịch sử các hệ: từng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook with a big birthday cake drawing on one page and a type grid on the other, cheerful warm light. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Hệ là gì

Lời: Trước khi đi vào lịch sử, nhắc lại luật cơ bản. Mỗi sinh vật trong Pokémon có một hoặc hai hệ. Mỗi chiêu thức…

```text
Wide 16:9 landscape cinematic frame. a simple diagram of a creature silhouette with two small elemental badges beside it, and a move card with one badge, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Khi một chiêu đánh trúng, trò chơi so hệ của chiêu với hệ của mục tiêu. Có thể gây gấp đôi sát thương, một nử…

```text
Wide 16:9 landscape cinematic frame. three result cards: a bold x2, a faded x0.5 and an empty x0, arranged in a row on a desk, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nước dập Lửa, Lửa đốt Cỏ, Cỏ hút Nước. Đây là vòng tròn đầu tiên mà mọi người chơi đều học, giống như oẳn tù…

```text
Wide 16:9 landscape cinematic frame. a circular diagram with a water drop, a flame and a leaf connected by arrows, parchment style, blue red green accents. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Có cả những ô số không, tức miễn nhiễm hoàn toàn. Hệ Đất không bị chiêu Điện làm gì cả. Hệ Ma thì không bị ch…

```text
Wide 16:9 landscape cinematic frame. an electric bolt fizzling out against a mound of earth, and a fist passing through a ghostly wisp, two small panels, parchment illustration. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Thêm một luật nhỏ: nếu sinh vật dùng chiêu cùng hệ với mình, sức mạnh chiêu được tăng thêm một nửa. Vì vậy mộ…

```text
Wide 16:9 landscape cinematic frame. a flame-themed silhouette casting a large flame with a small plus fifty percent badge glowing beside it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Và nếu sinh vật có hai hệ, các hệ số nhân với nhau. Một chiêu có thể gây gấp bốn sát thương, hoặc chỉ một phầ…

```text
Wide 16:9 landscape cinematic frame. a calculation drawn on a chalkboard: two small multiplier cards combining into a large x4, amber chalk, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nếu so với các bộ Kaku đã phân tích như Nen hay Haki, đây là hệ thống sức mạnh minh bạch nhất: mọi luật đều đ…

```text
Wide 16:9 landscape cinematic frame. a clear glass box containing neatly labeled gears and numbers, next to a mysterious glowing orb, comparison still life, soft light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Bảng tương khắc chính là hệ thống sức mạnh của Pokémon. Không có năng lượng bí ẩn nào cả, chỉ có một cái bảng…

```text
Wide 16:9 landscape cinematic frame. an old paper chart with many hand-written corrections and crossed-out cells, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải thú nhận: hồi nhỏ Kaku từng thuộc lòng bảng này, và quên sạch bảng cửu chương. Mỗi người một ưu tiê…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly holding a type chart while a multiplication table lies forgotten on the floor. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Thời kỳ 1 (1996): bảng mười lăm hệ

Lời: Thời kỳ đầu tiên bắt đầu với hai phiên bản Đỏ và Xanh lá ở Nhật năm 1996. Phát minh của thời kỳ này chính là…

```text
Wide 16:9 landscape cinematic frame. two old game cartridges, one red and one green, lying side by side on a wooden desk, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Mười lăm hệ gồm: Thường, Lửa, Nước, Cỏ, Điện, Băng, Giác đấu, Độc, Đất, Bay, Siêu linh, Côn trùng, Đá, Ma, và…

```text
Wide 16:9 landscape cinematic frame. a grid of fifteen simple elemental icons drawn on parchment: a circle, flame, drop, leaf, bolt, snowflake, fist, skull, mound, wing, eye, beetle, rock, ghost wisp, dragon head, top-down shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Bảng thời kỳ đầu còn có vài luật lạ mà ít người nhớ. Ví dụ, Côn trùng và Độc từng khắc chế lẫn nhau, cùng gây…

```text
Wide 16:9 landscape cinematic frame. a beetle icon and a skull icon punching each other with matching x2 badges, humorous parchment illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Và Băng lúc đó không bị Lửa kháng. Những chi tiết này đều bị sửa ở thời kỳ sau. Kaku gắn nhãn cần kiểm lại ch…

```text
Wide 16:9 landscape cinematic frame. an old strategy guide book with sticky notes and corrections scribbled in the margins, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Ý tưởng rất hay: không có hệ nào tuyệt đối mạnh. Muốn thắng, người chơi phải xây một đội đa dạng, và đổi sinh…

```text
Wide 16:9 landscape cinematic frame. a small team of six silhouettes of different shapes standing together on a grassy hill, back view, bright adventurous light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Nhưng lý thuyết là một chuyện, thực tế lại là chuyện khác. Và thực tế của thời kỳ này có tên là hệ Siêu linh.

```text
Wide 16:9 landscape cinematic frame. a calm psychic silhouette levitating with glowing violet eyes in a dark room, other silhouettes backing away, dramatic low-angle shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Vấn đề của thời kỳ 1: Siêu linh quá mạnh

Lời: Trên giấy, Siêu linh có hai điểm yếu: Côn trùng và Ma. Nhưng thời đó, gần như không có chiêu Côn trùng nào đủ…

```text
Wide 16:9 landscape cinematic frame. a tiny beetle icon throwing a weak punch at a large violet eye icon, humorous diagram on parchment. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Còn Ma thì sao? Chiêu Ma lẽ ra phải gây gấp đôi sát thương. Nhưng một lỗi trong trò chơi khiến chiêu Ma hoàn…

```text
Wide 16:9 landscape cinematic frame. a ghostly wisp bouncing harmlessly off a violet shield with a small error symbol blinking above, close-up, glitchy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nghĩa là hệ mạnh nhất trò chơi gần như không có điểm yếu thật sự. Trong khi đó, nó lại khắc chế hệ Giác đấu v…

```text
Wide 16:9 landscape cinematic frame. a violet eye icon standing tall on a podium while fist and skull icons lie defeated below, parchment illustration. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Hệ Rồng thì có vấn đề ngược lại: cả trò chơi chỉ có một chiêu hệ Rồng, và nó luôn gây đúng bốn mươi điểm sát…

```text
Wide 16:9 landscape cinematic frame. a single lonely dragon move card on an otherwise empty shelf, a fixed number 40 stamped on it, close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Ngay cả sinh vật huyền thoại mạnh nhất phiên bản đầu, Mewtwo, cũng là hệ Siêu linh. Hệ mạnh nhất lại có đại d…

```text
Wide 16:9 landscape cinematic frame. a tall mysterious psychic silhouette hovering in a dark cave surrounded by glowing violet energy, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku hồi đó cũng có một đội toàn Siêu linh. Không phải vì Kaku giỏi, mà vì Kaku không biết gì hơn. Giờ nghĩ l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding its face behind an old team roster full of eye icons, embarrassed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Những năm đó chưa có mạng internet phổ biến như bây giờ. Người chơi phát hiện lỗi hệ Ma bằng cách tự thử, rồi…

```text
Wide 16:9 landscape cinematic frame. two kids connecting two old handheld consoles with a cable on a bedroom floor, a gaming magazine open beside them, medium shot, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Kết quả là trong các trận đấu giữa người chơi, đội nào cũng có ít nhất một sinh vật Siêu linh. Sự đa dạng mà…

```text
Wide 16:9 landscape cinematic frame. several team rosters pinned on a board, each with the same violet eye icon circled in red, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Vậy các nhà làm game đã sửa thế nào? Câu trả lời đến sau ba năm.

```text
Wide 16:9 landscape cinematic frame. a calendar with pages flipping from 1996 to 1999, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là bài học đầu tiên về thiết kế hệ thống sức mạnh. Một luật hay trên giấy vẫn có thể hỏng n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling a crack in a beautifully drawn chart with a red pencil. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Thời kỳ 2 (1999): Bóng tối và Thép

Lời: Cùng với hai hệ mới là những sinh vật mới mang hệ đó, và cả những sinh vật cũ được đổi hệ. Một số sinh vật hệ…

```text
Wide 16:9 landscape cinematic frame. a small magnet-like floating silhouette receiving a new steel badge beside its electric badge, parchment illustration, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Năm 1999, phiên bản Vàng và Bạc ra mắt với lời giải: hai hệ mới, Bóng tối và Thép. Bảng tăng lên mười bảy hệ.

```text
Wide 16:9 landscape cinematic frame. two new icons, a crescent moon and a steel gear, being added to an old parchment chart with fresh ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Phát minh thứ nhất: hệ Bóng tối miễn nhiễm hoàn toàn với chiêu Siêu linh. Lần đầu tiên, Siêu linh có một khắc…

```text
Wide 16:9 landscape cinematic frame. a dark shadowy silhouette calmly standing as violet psychic waves pass through it without effect, dramatic medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Tính ra, Thép chống chịu được mười hệ khác nhau ở thời kỳ này, và miễn nhiễm hoàn toàn với Độc. Không hệ nào…

```text
Wide 16:9 landscape cinematic frame. a steel gear icon at the center of a chart with ten arrows bouncing off it, one arrow vanishing entirely, parchment diagram. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Phát minh thứ hai: hệ Thép chống chịu rất nhiều hệ, trong đó có Siêu linh. Nó là bức tường mới của bảng tương…

```text
Wide 16:9 landscape cinematic frame. a heavy steel shield icon deflecting arrows from many elemental icons, parchment diagram, amber and steel tones. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Lỗi hệ Ma cũng được sửa. Chiêu Ma giờ gây gấp đôi sát thương lên Siêu linh đúng như thiết kế ban đầu.

```text
Wide 16:9 landscape cinematic frame. a small repair wrench fixing a cracked line between a ghost wisp icon and an eye icon on the chart, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Và có thêm một thay đổi lớn: chỉ số Đặc biệt được tách thành hai: tấn công đặc biệt và phòng thủ đặc biệt. Si…

```text
Wide 16:9 landscape cinematic frame. a single stat bar splitting into two separate bars labeled with a sword icon and a shield icon, diagram style, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nhưng hai hệ mới cũng tạo ra những kẻ thống trị mới. Một số sinh vật mang cả hệ Đá và Bóng tối, hay Thép và C…

```text
Wide 16:9 landscape cinematic frame. a racetrack loop with several elemental icons chasing each other endlessly, humorous parchment illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Kaku thấy cách sửa này rất khéo: không giảm sức mạnh của Siêu linh một cách thô bạo, mà thêm công cụ cho ngườ…

```text
Wide 16:9 landscape cinematic frame. a scale being balanced by adding a new weight on one side rather than removing one from the other, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Thời kỳ 3 (2006): vật lý và đặc biệt

Lời: Trước đó một chút, năm 2002, phiên bản Hồng ngọc và Lam ngọc đã thêm một lớp mới: đặc tính. Mỗi sinh vật có m…

```text
Wide 16:9 landscape cinematic frame. two gem-shaped cartridges, one red and one blue, beside a small card showing a passive ability icon, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Ví dụ đặc tính Bay lơ lửng giúp sinh vật miễn nhiễm hoàn toàn chiêu Đất, dù hệ của nó không phải hệ Bay. Bảng…

```text
Wide 16:9 landscape cinematic frame. a floating round silhouette hovering calmly above cracks in the ground from an earthquake, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Thời kỳ thứ ba không thêm hệ nào, nhưng thay đổi cách mọi hệ hoạt động. Phát minh của phiên bản Kim cương và…

```text
Wide 16:9 landscape cinematic frame. two game cartridges with diamond and pearl symbols resting on a desk beside a notebook, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Trước đó, một chiêu dùng sức tấn công thường hay tấn công đặc biệt là do hệ của nó quyết định. Mọi chiêu Lửa…

```text
Wide 16:9 landscape cinematic frame. a sorting chart where every flame icon goes into one box and every fist icon goes into another, rigid rules, parchment style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Điều này tạo ra những chuyện rất vô lý. Một cú đấm lửa lại tính theo sức mạnh đặc biệt, dù rõ ràng là một cú…

```text
Wide 16:9 landscape cinematic frame. a flaming fist punch labeled with a magic sparkle icon, a confused question mark floating above, humorous illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Những sinh vật có sức tấn công vật lý cao nhưng mang hệ vốn là đặc biệt, như Lửa hay Nước, cuối cùng cũng có…

```text
Wide 16:9 landscape cinematic frame. a muscular fire-themed silhouette finally throwing a powerful flaming punch, triumphant pose, dramatic warm light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Từ năm 2006, mỗi chiêu tự có loại riêng. Cú đấm lửa thành vật lý, luồng lửa thổi ra thành đặc biệt. Bỗng nhiê…

```text
Wide 16:9 landscape cinematic frame. a flaming fist and a stream of fire sorted into two different boxes now, several previously ignored silhouettes stepping forward, parchment diagram. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đôi khi thay đổi lớn nhất không phải là thêm thứ mới, mà là sửa cách chia những thứ cũ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot rearranging books on a shelf into a new order, looking satisfied. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Thời kỳ 4 (2013): hệ Tiên

Lời: Những sinh vật Rồng thời này thường là át chủ bài trong đội: hiếm, mạnh, và gần như ai có cũng mang ra trận.…

```text
Wide 16:9 landscape cinematic frame. a tournament bracket board filled with dragon head icons across most slots, close-up, dramatic stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Sau Siêu linh, tới lượt hệ Rồng thống trị. Tới thời kỳ này, Rồng có nhiều chiêu mạnh, chỉ số cao, và chỉ yếu…

```text
Wide 16:9 landscape cinematic frame. a large dragon silhouette perched atop a mountain of defeated icons, wings spread, dramatic sunset light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Hệ Tiên còn khắc chế Giác đấu và Bóng tối, hai hệ đang rất mạnh lúc đó. Một hệ mới, cùng lúc kiềm chế ba kẻ t…

```text
Wide 16:9 landscape cinematic frame. a sparkling star icon with three arrows pointing outward at a dragon head, a fist and a crescent moon, parchment diagram. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Năm 2013, phiên bản X và Y thêm hệ thứ mười tám: Tiên. Đây là hệ mới đầu tiên sau hơn mười hai năm.

```text
Wide 16:9 landscape cinematic frame. a delicate glowing pink star icon being added to the chart with a sparkle, close-up, soft magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Phát minh của hệ Tiên: miễn nhiễm hoàn toàn với chiêu Rồng, và đánh Rồng gấp đôi. Kẻ thống trị lần đầu gặp kh…

```text
Wide 16:9 landscape cinematic frame. a small sparkling fairy silhouette standing unharmed as a dragon's breath passes around it, wide shot, pink and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Để Tiên không trở thành hệ quá mạnh tiếp theo, nó yếu trước Độc và Thép. Hai hệ vốn ít được dùng để tấn công…

```text
Wide 16:9 landscape cinematic frame. a fairy icon with two arrows pointing at it from a skull icon and a gear icon, parchment diagram, balanced composition. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Nhiều sinh vật mang hình dáng dễ thương hay mang yếu tố thần tiên được xếp lại vào hệ mới. Có những sinh vật…

```text
Wide 16:9 landscape cinematic frame. a graceful psychic silhouette gaining a new sparkling badge, a surprised dragon silhouette stepping back, wide shot, pink and violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Một số sinh vật cũ còn được đổi hệ sang Tiên. Những sinh vật bao nhiêu năm là hệ Thường bỗng có danh tính mới.

```text
Wide 16:9 landscape cinematic frame. an old identity card being restamped with a new sparkling badge, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Và hệ Thép bị giảm nhẹ: mất khả năng chống chịu chiêu Ma và Bóng tối. Mười hai năm làm bức tường, giờ tường c…

```text
Wide 16:9 landscape cinematic frame. a steel wall with two small new windows cut into it, a ghost wisp and a crescent moon peeking through, humorous illustration. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Thời kỳ 5 (2022): đổi hệ ngay trong trận

Lời: Thời kỳ gần nhất không thêm hệ, nhưng cho phép một điều trước đây không thể: đổi hệ ngay giữa trận đấu. Cơ ch…

```text
Wide 16:9 landscape cinematic frame. a creature silhouette encased in a glowing crystal shell, a new elemental crown floating above its head, dramatic close-up, prismatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Về sau còn có một hệ Tera đặc biệt tên là Tinh tú, xuất hiện trong phần mở rộng. Kaku ghi cần kiểm lại cho ch…

```text
Wide 16:9 landscape cinematic frame. a prismatic star-shaped crystal glowing with all colors at once, extreme close-up, rainbow light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Mỗi sinh vật có một hệ Tera riêng. Khi kích hoạt, nó mang hệ đó, bất kể hệ gốc là gì. Một sinh vật hệ Lửa có…

```text
Wide 16:9 landscape cinematic frame. a fire-themed silhouette cracking into a crystal form with water drop symbols glowing inside, sequential illustration, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nghĩa là bảng tương khắc giờ có thêm một lớp đoán ý đối thủ. Bạn không chỉ nhìn hệ trước mặt, mà phải đoán hệ…

```text
Wide 16:9 landscape cinematic frame. two players across a table, one holding a hidden card close to the chest, the other studying them intently, medium shot, tense warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nhưng nhìn theo lịch sử, Terastal vẫn theo đúng nguyên tắc cũ: không bỏ bảng tương khắc, mà thêm công cụ để n…

```text
Wide 16:9 landscape cinematic frame. an old chart pinned on the wall with a new crystal tool hanging beside it on a hook, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thật: cơ chế này khiến nhiều người chơi lâu năm vừa thích vừa đau đầu. Ba mươi năm học thuộc bả…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a chart where the icons keep changing places, holding its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Anime và trò chơi: hai luật khác nhau

Lời: Có cả những trận mà nhân vật chính thắng bằng cách đảo ngược bảng tương khắc: dùng điểm yếu của mình làm điểm…

```text
Wide 16:9 landscape cinematic frame. a small creature using a river in the arena to redirect an attack, clever tactical diagram overlay, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Còn trong anime thì sao? Anime Pokémon dùng bảng tương khắc lỏng hơn nhiều. Một sinh vật hệ Điện có thể thắng…

```text
Wide 16:9 landscape cinematic frame. a small determined electric creature silhouette standing victorious in front of a large collapsed rock-like opponent, dramatic arena light, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku nghĩ đây là lựa chọn có chủ đích. Trò chơi cần luật chặt để công bằng. Phim thì cần kịch tính, và kịch t…

```text
Wide 16:9 landscape cinematic frame. a split image: a neat rulebook on one side, a dramatic comeback moment on the other, symmetrical composition, warm and cool light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kaku để ý thấy những trận hay nhất trong anime thường là trận mà bảng tương khắc bất lợi cho nhân vật chính.…

```text
Wide 16:9 landscape cinematic frame. a young trainer and a small creature standing together against a much larger opponent, backlit by stadium lights, low-angle shot, inspiring light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nhưng anime vẫn dùng bảng làm nền. Khi nhân vật chính đổi sinh vật đúng hệ để thắng, người xem thấy mình hiểu…

```text
Wide 16:9 landscape cinematic frame. a young trainer silhouette pointing forward confidently, a type chart faintly glowing in the sky above the arena, low-angle shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và ba mươi năm qua, cậu bé Satoshi cùng chú chuột điện của mình đã dạy cả một thế hệ thuộc lòng bảng tương kh…

```text
Wide 16:9 landscape cinematic frame. a vintage television in a living room glowing with a bright cartoon scene, children sitting on the floor watching, back view, nostalgic warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Góc nhìn của Kaku: một hệ thống sống

Lời: Hầu hết hệ thống sức mạnh trong anime được viết một lần rồi giữ nguyên. Bảng tương khắc Pokémon thì khác: nó…

```text
Wide 16:9 landscape cinematic frame. a living tree whose branches are shaped like a growing type chart, new leaves sprouting at the edges, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và mỗi thời kỳ đều để lại những hệ từng mạnh rồi yếu, từng bị quên rồi được nhớ lại. Côn trùng từng vô dụng,…

```text
Wide 16:9 landscape cinematic frame. a wheel of elemental icons slowly rotating, some rising into light and others dipping into shadow, parchment illustration, warm light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Mỗi lần sửa đều theo một nguyên tắc giống nhau: khi một hệ quá mạnh, không cấm nó, mà thêm khắc tinh. Siêu li…

```text
Wide 16:9 landscape cinematic frame. two pairs of icons facing each other: an eye versus a crescent moon, a dragon head versus a sparkling star, parchment diagram. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kaku thấy đây là cách cân bằng rất đáng học, không chỉ trong trò chơi. Khi một thứ trở nên quá áp đảo, đôi kh…

```text
Wide 16:9 landscape cinematic frame. a crowded single-lane road turning into a multi-lane road with new paths opening, top-down diagram, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Kaku để một gợi ý: hãy nhìn xem hệ nào xuất hiện nhiều nhất trong các đội thi đấu hiện nay. Lịch sử cho thấy…

```text
Wide 16:9 landscape cinematic frame. a pie chart on parchment with one slice much larger than the others, a small question mark beside it, top-down shot, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thì chỉ mong có một hệ Cú. Mạnh trước Côn trùng, yếu trước… bài kiểm tra buổi sáng.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sketching a tiny owl-shaped type icon in the empty nineteenth slot, grinning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Theo bạn, hệ nào hiện đang quá mạnh và cần một khắc tinh mới? Và nếu được đặt tên hệ thứ mười chín, bạn chọn…

```text
Wide 16:9 landscape cinematic frame. an empty nineteenth slot at the edge of the type chart with a question mark and a pencil beside it, close-up, inviting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Đường thời gian thu gọn · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thu gọn ba mươi năm vào một đường thời gian.

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a long timeline banner across a table, markers at five points. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Năm 1996: mười lăm hệ và ý tưởng bảng tương khắc. Siêu linh thống trị vì lỗi hệ Ma và chiêu Côn trùng quá yếu.

```text
Wide 16:9 landscape cinematic frame. the first marker on the timeline with an eye icon and a small bug symbol, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Năm 2002: đặc tính, những ngoại lệ gắn với từng sinh vật.

```text
Wide 16:9 landscape cinematic frame. a small marker on the timeline with a passive ability icon between the 1999 and 2006 markers, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Năm 1999: thêm Bóng tối và Thép, sửa lỗi hệ Ma, tách chỉ số Đặc biệt. Năm 2006: tách chiêu vật lý và đặc biệt.

```text
Wide 16:9 landscape cinematic frame. the second and third markers with a crescent moon, a gear and a split stat icon, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Năm 2013: thêm hệ Tiên để khắc chế Rồng. Năm 2022: đổi hệ ngay trong trận. Và năm 2026: Pokémon tròn ba mươi…

```text
Wide 16:9 landscape cinematic frame. the last markers with a sparkling star, a crystal icon and a small birthday cake, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Và có lẽ đó là lý do Pokémon sống được ba mươi năm: mỗi lần người chơi tìm ra cách phá, trò chơi lại tìm ra c…

```text
Wide 16:9 landscape cinematic frame. a grown-up player and a child sitting side by side playing handheld games on a couch, warm evening light, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Từ mười lăm lên mười tám hệ, ba mươi năm của bảng tương khắc là câu chuyện về việc sửa sai, cân bằng và mở rộ…

```text
Wide 16:9 landscape cinematic frame. a big hand-drawn type chart on parchment, covered with notes from many different pens and eras, wide shot, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tiếp theo, Kaku mở một phiên tòa. Bị cáo là Eren Yeager. Kaku sẽ trình bày cáo trạng, lời bào chữa và c…

```text
Wide 16:9 landscape cinematic frame. an empty wooden courtroom with a single spotlight on the defendant's chair, a gavel resting on the judge's bench, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn lớn lên cùng bảng tương khắc này, hãy đăng ký kênh và chia sẻ video cho người bạn từng đấu với bạn hồ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving goodbye beside an old handheld console and a tiny birthday cake. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 76 giây · cảnh s01–s07 · 991 ký tự

**Gemini**

```text
Video này không có spoiler cốt truyện. Kaku chỉ nói về luật chơi, chủ yếu trong các phiên bản trò chơi chính, và một chút về anime.

<short pause> Năm 1996, một trò chơi trên máy cầm tay ra mắt ở Nhật Bản với mười lăm hệ. Lửa, Nước, Cỏ, Điện, và mười một hệ khác.

<short pause> Ba mươi năm sau, con số đó là mười tám. Bảng tương khắc có ba trăm hai mươi bốn ô, và mỗi ô là một luật nhỏ quyết định trận đấu.

<short pause> Nhưng ba hệ mới không được thêm vào cho vui. Mỗi hệ ra đời để sửa một vấn đề của bảng cũ. Và có một hệ từng mạnh tới mức gần như không ai đánh bại được.

<short pause> Ở Việt Nam, nhiều thế hệ biết tới Pokémon qua truyện tranh, phim hoạt hình trên truyền hình và những tấm thẻ bài đổi nhau ở cổng trường. Ai cũng từng tranh cãi xem hệ nào mạnh nhất.

<short pause> Và câu trả lời cho cuộc tranh cãi đó đã thay đổi nhiều lần trong ba mươi năm. Đó chính là nội dung hôm nay.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Nhân dịp Pokémon vừa tròn ba mươi tuổi, hôm nay Kaku kể lại lịch sử các hệ: từng thời kỳ, mỗi thời kỳ một phát minh, và lý do đằng sau mỗi thay đổi.
```

**ElevenLabs**

```text
Video này không có spoiler cốt truyện. Kaku chỉ nói về luật chơi, chủ yếu trong các phiên bản trò chơi chính, và một chút về anime.

[pause] Năm 1996, một trò chơi trên máy cầm tay ra mắt ở Nhật Bản với mười lăm hệ. Lửa, Nước, Cỏ, Điện, và mười một hệ khác.

[pause] Ba mươi năm sau, con số đó là mười tám. Bảng tương khắc có ba trăm hai mươi bốn ô, và mỗi ô là một luật nhỏ quyết định trận đấu.

[pause] Nhưng ba hệ mới không được thêm vào cho vui. Mỗi hệ ra đời để sửa một vấn đề của bảng cũ. Và có một hệ từng mạnh tới mức gần như không ai đánh bại được.

[pause] Ở Việt Nam, nhiều thế hệ biết tới Pokémon qua truyện tranh, phim hoạt hình trên truyền hình và những tấm thẻ bài đổi nhau ở cổng trường. Ai cũng từng tranh cãi xem hệ nào mạnh nhất.

[pause] Và câu trả lời cho cuộc tranh cãi đó đã thay đổi nhiều lần trong ba mươi năm. Đó chính là nội dung hôm nay.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Nhân dịp Pokémon vừa tròn ba mươi tuổi, hôm nay Kaku kể lại lịch sử các hệ: từng thời kỳ, mỗi thời kỳ một phát minh, và lý do đằng sau mỗi thay đổi.
```

### c02 · Hệ là gì

Khoảng 94 giây · cảnh s08–s16 · 1221 ký tự

**Gemini**

```text
Trước khi đi vào lịch sử, nhắc lại luật cơ bản. Mỗi sinh vật trong Pokémon có một hoặc hai hệ. Mỗi chiêu thức cũng thuộc một hệ.

<short pause> Khi một chiêu đánh trúng, trò chơi so hệ của chiêu với hệ của mục tiêu. Có thể gây gấp đôi sát thương, một nửa, hoặc không có tác dụng gì.

<short pause> Nước dập Lửa, Lửa đốt Cỏ, Cỏ hút Nước. Đây là vòng tròn đầu tiên mà mọi người chơi đều học, giống như oẳn tù tì.

<short pause> Có cả những ô số không, tức miễn nhiễm hoàn toàn. Hệ Đất không bị chiêu Điện làm gì cả. Hệ Ma thì không bị chiêu Thường và Giác đấu chạm tới.

<short pause> Thêm một luật nhỏ: nếu sinh vật dùng chiêu cùng hệ với mình, sức mạnh chiêu được tăng thêm một nửa. Vì vậy một sinh vật Lửa dùng chiêu Lửa luôn mạnh hơn dùng chiêu hệ khác.

<short pause> Và nếu sinh vật có hai hệ, các hệ số nhân với nhau. Một chiêu có thể gây gấp bốn sát thương, hoặc chỉ một phần tư.

<short pause> Nếu so với các bộ Kaku đã phân tích như Nen hay Haki, đây là hệ thống sức mạnh minh bạch nhất: mọi luật đều được viết thành số, ai cũng tra được.

<short pause> Bảng tương khắc chính là hệ thống sức mạnh của Pokémon. Không có năng lượng bí ẩn nào cả, chỉ có một cái bảng. <short pause> Nhưng cái bảng đó đã thay đổi nhiều hơn bạn nghĩ.

<short pause> <laugh> Kaku phải thú nhận: hồi nhỏ Kaku từng thuộc lòng bảng này, và quên sạch bảng cửu chương. Mỗi người một ưu tiên.
```

**ElevenLabs**

```text
Trước khi đi vào lịch sử, nhắc lại luật cơ bản. Mỗi sinh vật trong Pokémon có một hoặc hai hệ. Mỗi chiêu thức cũng thuộc một hệ.

[pause] Khi một chiêu đánh trúng, trò chơi so hệ của chiêu với hệ của mục tiêu. Có thể gây gấp đôi sát thương, một nửa, hoặc không có tác dụng gì.

[pause] Nước dập Lửa, Lửa đốt Cỏ, Cỏ hút Nước. Đây là vòng tròn đầu tiên mà mọi người chơi đều học, giống như oẳn tù tì.

[pause] Có cả những ô số không, tức miễn nhiễm hoàn toàn. Hệ Đất không bị chiêu Điện làm gì cả. Hệ Ma thì không bị chiêu Thường và Giác đấu chạm tới.

[pause] Thêm một luật nhỏ: nếu sinh vật dùng chiêu cùng hệ với mình, sức mạnh chiêu được tăng thêm một nửa. Vì vậy một sinh vật Lửa dùng chiêu Lửa luôn mạnh hơn dùng chiêu hệ khác.

[pause] Và nếu sinh vật có hai hệ, các hệ số nhân với nhau. Một chiêu có thể gây gấp bốn sát thương, hoặc chỉ một phần tư.

[pause] Nếu so với các bộ Kaku đã phân tích như Nen hay Haki, đây là hệ thống sức mạnh minh bạch nhất: mọi luật đều được viết thành số, ai cũng tra được.

[pause] Bảng tương khắc chính là hệ thống sức mạnh của Pokémon. Không có năng lượng bí ẩn nào cả, chỉ có một cái bảng. [pause] Nhưng cái bảng đó đã thay đổi nhiều hơn bạn nghĩ.

[pause] [chuckles] Kaku phải thú nhận: hồi nhỏ Kaku từng thuộc lòng bảng này, và quên sạch bảng cửu chương. Mỗi người một ưu tiên.
```

### c03 · Thời kỳ 1 (1996): bảng mười lăm hệ

Khoảng 62 giây · cảnh s17–s22 · 801 ký tự

**Gemini**

```text
Thời kỳ đầu tiên bắt đầu với hai phiên bản Đỏ và Xanh lá ở Nhật năm 1996. Phát minh của thời kỳ này chính là ý tưởng về bảng tương khắc.

<short pause> Mười lăm hệ gồm: Thường, Lửa, Nước, Cỏ, Điện, Băng, Giác đấu, Độc, Đất, Bay, Siêu linh, Côn trùng, Đá, Ma, và Rồng.

<short pause> Bảng thời kỳ đầu còn có vài luật lạ mà ít người nhớ. Ví dụ, Côn trùng và Độc từng khắc chế lẫn nhau, cùng gây gấp đôi sát thương cho nhau.

<short pause> Và Băng lúc đó không bị Lửa kháng. Những chi tiết này đều bị sửa ở thời kỳ sau. Kaku gắn nhãn cần kiểm lại cho từng chi tiết nhỏ, vì sách hướng dẫn thời đó cũng không ghi đúng hết.

<short pause> Ý tưởng rất hay: không có hệ nào tuyệt đối mạnh. Muốn thắng, người chơi phải xây một đội đa dạng, và đổi sinh vật đúng lúc.

<short pause> Nhưng lý thuyết là một chuyện, thực tế lại là chuyện khác. Và thực tế của thời kỳ này có tên là hệ Siêu linh.
```

**ElevenLabs**

```text
Thời kỳ đầu tiên bắt đầu với hai phiên bản Đỏ và Xanh lá ở Nhật năm 1996. Phát minh của thời kỳ này chính là ý tưởng về bảng tương khắc.

[pause] Mười lăm hệ gồm: Thường, Lửa, Nước, Cỏ, Điện, Băng, Giác đấu, Độc, Đất, Bay, Siêu linh, Côn trùng, Đá, Ma, và Rồng.

[pause] Bảng thời kỳ đầu còn có vài luật lạ mà ít người nhớ. Ví dụ, Côn trùng và Độc từng khắc chế lẫn nhau, cùng gây gấp đôi sát thương cho nhau.

[pause] Và Băng lúc đó không bị Lửa kháng. Những chi tiết này đều bị sửa ở thời kỳ sau. Kaku gắn nhãn cần kiểm lại cho từng chi tiết nhỏ, vì sách hướng dẫn thời đó cũng không ghi đúng hết.

[pause] Ý tưởng rất hay: không có hệ nào tuyệt đối mạnh. Muốn thắng, người chơi phải xây một đội đa dạng, và đổi sinh vật đúng lúc.

[pause] Nhưng lý thuyết là một chuyện, thực tế lại là chuyện khác. Và thực tế của thời kỳ này có tên là hệ Siêu linh.
```

### c04 · Vấn đề của thời kỳ 1: Siêu linh quá mạnh

Khoảng 100 giây · cảnh s23–s32 · 1301 ký tự

**Gemini**

```text
Trên giấy, Siêu linh có hai điểm yếu: Côn trùng và Ma. <short pause> Nhưng thời đó, gần như không có chiêu Côn trùng nào đủ mạnh để dùng.

<short pause> Còn Ma thì sao? Chiêu Ma lẽ ra phải gây gấp đôi sát thương. <short pause> Nhưng một lỗi trong trò chơi khiến chiêu Ma hoàn toàn không có tác dụng lên Siêu linh.

<short pause> Nghĩa là hệ mạnh nhất trò chơi gần như không có điểm yếu thật sự. Trong khi đó, nó lại khắc chế hệ Giác đấu và Độc, rất phổ biến lúc bấy giờ.

<short pause> Hệ Rồng thì có vấn đề ngược lại: cả trò chơi chỉ có một chiêu hệ Rồng, và nó luôn gây đúng bốn mươi điểm sát thương, bất kể hệ nào.

<short pause> Ngay cả sinh vật huyền thoại mạnh nhất phiên bản đầu, Mewtwo, cũng là hệ Siêu linh. Hệ mạnh nhất lại có đại diện mạnh nhất.

<short pause> <laugh> Kaku hồi đó cũng có một đội toàn Siêu linh. Không phải vì Kaku giỏi, mà vì Kaku không biết gì hơn. Giờ nghĩ lại hơi xấu hổ.

<short pause> Những năm đó chưa có mạng internet phổ biến như bây giờ. Người chơi phát hiện lỗi hệ Ma bằng cách tự thử, rồi truyền tai nhau, hoặc đọc trong tạp chí trò chơi.

<short pause> Kết quả là trong các trận đấu giữa người chơi, đội nào cũng có ít nhất một sinh vật Siêu linh. Sự đa dạng mà bảng tương khắc hứa hẹn bị phá vỡ bởi một hệ.

<short pause> Vậy các nhà làm game đã sửa thế nào? Câu trả lời đến sau ba năm.

<short pause> Kaku ghi chú: đây là bài học đầu tiên về thiết kế hệ thống sức mạnh. Một luật hay trên giấy vẫn có thể hỏng nếu thiếu công cụ để dùng nó.
```

**ElevenLabs**

```text
Trên giấy, Siêu linh có hai điểm yếu: Côn trùng và Ma. [pause] Nhưng thời đó, gần như không có chiêu Côn trùng nào đủ mạnh để dùng.

[pause] [curious] Còn Ma thì sao? Chiêu Ma lẽ ra phải gây gấp đôi sát thương. [pause] Nhưng một lỗi trong trò chơi khiến chiêu Ma hoàn toàn không có tác dụng lên Siêu linh.

[pause] Nghĩa là hệ mạnh nhất trò chơi gần như không có điểm yếu thật sự. Trong khi đó, nó lại khắc chế hệ Giác đấu và Độc, rất phổ biến lúc bấy giờ.

[pause] Hệ Rồng thì có vấn đề ngược lại: cả trò chơi chỉ có một chiêu hệ Rồng, và nó luôn gây đúng bốn mươi điểm sát thương, bất kể hệ nào.

[pause] Ngay cả sinh vật huyền thoại mạnh nhất phiên bản đầu, Mewtwo, cũng là hệ Siêu linh. Hệ mạnh nhất lại có đại diện mạnh nhất.

[pause] [chuckles] Kaku hồi đó cũng có một đội toàn Siêu linh. Không phải vì Kaku giỏi, mà vì Kaku không biết gì hơn. Giờ nghĩ lại hơi xấu hổ.

[pause] Những năm đó chưa có mạng internet phổ biến như bây giờ. Người chơi phát hiện lỗi hệ Ma bằng cách tự thử, rồi truyền tai nhau, hoặc đọc trong tạp chí trò chơi.

[pause] Kết quả là trong các trận đấu giữa người chơi, đội nào cũng có ít nhất một sinh vật Siêu linh. Sự đa dạng mà bảng tương khắc hứa hẹn bị phá vỡ bởi một hệ.

[pause] Vậy các nhà làm game đã sửa thế nào? Câu trả lời đến sau ba năm.

[pause] Kaku ghi chú: đây là bài học đầu tiên về thiết kế hệ thống sức mạnh. Một luật hay trên giấy vẫn có thể hỏng nếu thiếu công cụ để dùng nó.
```

### c05 · Thời kỳ 2 (1999): Bóng tối và Thép

Khoảng 102 giây · cảnh s33–s41 · 1326 ký tự

**Gemini**

```text
Cùng với hai hệ mới là những sinh vật mới mang hệ đó, và cả những sinh vật cũ được đổi hệ. Một số sinh vật hệ Điện được thêm hệ Thép, vì chúng vốn trông như làm bằng kim loại.

<short pause> Năm 1999, phiên bản Vàng và Bạc ra mắt với lời giải: hai hệ mới, Bóng tối và Thép. Bảng tăng lên mười bảy hệ.

<short pause> Phát minh thứ nhất: hệ Bóng tối miễn nhiễm hoàn toàn với chiêu Siêu linh. Lần đầu tiên, Siêu linh có một khắc tinh thật sự.

<short pause> Tính ra, Thép chống chịu được mười hệ khác nhau ở thời kỳ này, và miễn nhiễm hoàn toàn với Độc. Không hệ nào có bức tường dày như vậy.

<short pause> Phát minh thứ hai: hệ Thép chống chịu rất nhiều hệ, trong đó có Siêu linh. Nó là bức tường mới của bảng tương khắc.

<short pause> Lỗi hệ Ma cũng được sửa. Chiêu Ma giờ gây gấp đôi sát thương lên Siêu linh đúng như thiết kế ban đầu.

<short pause> Và có thêm một thay đổi lớn: chỉ số Đặc biệt được tách thành hai: tấn công đặc biệt và phòng thủ đặc biệt. Siêu linh từng dùng một chỉ số cho cả công lẫn thủ, giờ thì không.

<short pause> Nhưng hai hệ mới cũng tạo ra những kẻ thống trị mới. Một số sinh vật mang cả hệ Đá và Bóng tối, hay Thép và Côn trùng, trở thành cơn ác mộng mới của các trận đấu. Cân bằng là một cuộc chạy đua không có vạch đích.

<short pause> Kaku thấy cách sửa này rất khéo: không giảm sức mạnh của Siêu linh một cách thô bạo, mà thêm công cụ cho người chơi. Hệ thống được cân bằng bằng cách mở rộng, không phải bằng cách cấm.
```

**ElevenLabs**

```text
Cùng với hai hệ mới là những sinh vật mới mang hệ đó, và cả những sinh vật cũ được đổi hệ. Một số sinh vật hệ Điện được thêm hệ Thép, vì chúng vốn trông như làm bằng kim loại.

[pause] Năm 1999, phiên bản Vàng và Bạc ra mắt với lời giải: hai hệ mới, Bóng tối và Thép. Bảng tăng lên mười bảy hệ.

[pause] Phát minh thứ nhất: hệ Bóng tối miễn nhiễm hoàn toàn với chiêu Siêu linh. Lần đầu tiên, Siêu linh có một khắc tinh thật sự.

[pause] Tính ra, Thép chống chịu được mười hệ khác nhau ở thời kỳ này, và miễn nhiễm hoàn toàn với Độc. Không hệ nào có bức tường dày như vậy.

[pause] Phát minh thứ hai: hệ Thép chống chịu rất nhiều hệ, trong đó có Siêu linh. Nó là bức tường mới của bảng tương khắc.

[pause] Lỗi hệ Ma cũng được sửa. Chiêu Ma giờ gây gấp đôi sát thương lên Siêu linh đúng như thiết kế ban đầu.

[pause] Và có thêm một thay đổi lớn: chỉ số Đặc biệt được tách thành hai: tấn công đặc biệt và phòng thủ đặc biệt. Siêu linh từng dùng một chỉ số cho cả công lẫn thủ, giờ thì không.

[pause] Nhưng hai hệ mới cũng tạo ra những kẻ thống trị mới. Một số sinh vật mang cả hệ Đá và Bóng tối, hay Thép và Côn trùng, trở thành cơn ác mộng mới của các trận đấu. Cân bằng là một cuộc chạy đua không có vạch đích.

[pause] Kaku thấy cách sửa này rất khéo: không giảm sức mạnh của Siêu linh một cách thô bạo, mà thêm công cụ cho người chơi. Hệ thống được cân bằng bằng cách mở rộng, không phải bằng cách cấm.
```

### c06 · Thời kỳ 3 (2006): vật lý và đặc biệt

Khoảng 90 giây · cảnh s42–s49 · 1164 ký tự

**Gemini**

```text
Trước đó một chút, năm 2002, phiên bản Hồng ngọc và Lam ngọc đã thêm một lớp mới: đặc tính. Mỗi sinh vật có một khả năng bị động có thể bẻ cong bảng tương khắc.

<short pause> Ví dụ đặc tính Bay lơ lửng giúp sinh vật miễn nhiễm hoàn toàn chiêu Đất, dù hệ của nó không phải hệ Bay. Bảng tương khắc giờ có ngoại lệ gắn với từng sinh vật.

<short pause> Thời kỳ thứ ba không thêm hệ nào, nhưng thay đổi cách mọi hệ hoạt động. Phát minh của phiên bản Kim cương và Ngọc trai năm 2006 là tách chiêu vật lý và chiêu đặc biệt.

<short pause> Trước đó, một chiêu dùng sức tấn công thường hay tấn công đặc biệt là do hệ của nó quyết định. Mọi chiêu Lửa đều là đặc biệt, mọi chiêu Giác đấu đều là vật lý.

<short pause> Điều này tạo ra những chuyện rất vô lý. Một cú đấm lửa lại tính theo sức mạnh đặc biệt, dù rõ ràng là một cú đấm.

<short pause> Những sinh vật có sức tấn công vật lý cao nhưng mang hệ vốn là đặc biệt, như Lửa hay Nước, cuối cùng cũng có chiêu phù hợp với cơ thể mình.

<short pause> Từ năm 2006, mỗi chiêu tự có loại riêng. Cú đấm lửa thành vật lý, luồng lửa thổi ra thành đặc biệt. Bỗng nhiên rất nhiều sinh vật trước đây vô dụng trở nên đáng dùng.

<short pause> <laugh> Kaku ghi chú: đôi khi thay đổi lớn nhất không phải là thêm thứ mới, mà là sửa cách chia những thứ cũ.
```

**ElevenLabs**

```text
Trước đó một chút, năm 2002, phiên bản Hồng ngọc và Lam ngọc đã thêm một lớp mới: đặc tính. Mỗi sinh vật có một khả năng bị động có thể bẻ cong bảng tương khắc.

[pause] Ví dụ đặc tính Bay lơ lửng giúp sinh vật miễn nhiễm hoàn toàn chiêu Đất, dù hệ của nó không phải hệ Bay. Bảng tương khắc giờ có ngoại lệ gắn với từng sinh vật.

[pause] Thời kỳ thứ ba không thêm hệ nào, nhưng thay đổi cách mọi hệ hoạt động. Phát minh của phiên bản Kim cương và Ngọc trai năm 2006 là tách chiêu vật lý và chiêu đặc biệt.

[pause] Trước đó, một chiêu dùng sức tấn công thường hay tấn công đặc biệt là do hệ của nó quyết định. Mọi chiêu Lửa đều là đặc biệt, mọi chiêu Giác đấu đều là vật lý.

[pause] Điều này tạo ra những chuyện rất vô lý. Một cú đấm lửa lại tính theo sức mạnh đặc biệt, dù rõ ràng là một cú đấm.

[pause] Những sinh vật có sức tấn công vật lý cao nhưng mang hệ vốn là đặc biệt, như Lửa hay Nước, cuối cùng cũng có chiêu phù hợp với cơ thể mình.

[pause] Từ năm 2006, mỗi chiêu tự có loại riêng. Cú đấm lửa thành vật lý, luồng lửa thổi ra thành đặc biệt. Bỗng nhiên rất nhiều sinh vật trước đây vô dụng trở nên đáng dùng.

[pause] [chuckles] Kaku ghi chú: đôi khi thay đổi lớn nhất không phải là thêm thứ mới, mà là sửa cách chia những thứ cũ.
```

### c07 · Thời kỳ 4 (2013): hệ Tiên / Thời kỳ 5 (2022): đổi hệ ngay trong trận

Khoảng 152 giây · cảnh s50–s64 · 1970 ký tự

**Gemini**

```text
Những sinh vật Rồng thời này thường là át chủ bài trong đội: hiếm, mạnh, và gần như ai có cũng mang ra trận. Các giải đấu lớn đầy những đội có hai, ba con Rồng.

<short pause> Sau Siêu linh, tới lượt hệ Rồng thống trị. Tới thời kỳ này, Rồng có nhiều chiêu mạnh, chỉ số cao, và chỉ yếu trước Băng và chính Rồng.

<short pause> Hệ Tiên còn khắc chế Giác đấu và Bóng tối, hai hệ đang rất mạnh lúc đó. Một hệ mới, cùng lúc kiềm chế ba kẻ thống trị.

<short pause> Năm 2013, phiên bản X và Y thêm hệ thứ mười tám: Tiên. Đây là hệ mới đầu tiên sau hơn mười hai năm.

<short pause> Phát minh của hệ Tiên: miễn nhiễm hoàn toàn với chiêu Rồng, và đánh Rồng gấp đôi. Kẻ thống trị lần đầu gặp khắc tinh thật sự.

<short pause> Để Tiên không trở thành hệ quá mạnh tiếp theo, nó yếu trước Độc và Thép. Hai hệ vốn ít được dùng để tấn công bỗng có giá trị hơn.

<short pause> Nhiều sinh vật mang hình dáng dễ thương hay mang yếu tố thần tiên được xếp lại vào hệ mới. Có những sinh vật Siêu linh được thêm hệ Tiên và bỗng trở thành khắc tinh của Rồng.

<short pause> Một số sinh vật cũ còn được đổi hệ sang Tiên. Những sinh vật bao nhiêu năm là hệ Thường bỗng có danh tính mới.

<short pause> Và hệ Thép bị giảm nhẹ: mất khả năng chống chịu chiêu Ma và Bóng tối. Mười hai năm làm bức tường, giờ tường cũng phải có vài cửa sổ.

<short pause> Thời kỳ gần nhất không thêm hệ, nhưng cho phép một điều trước đây không thể: đổi hệ ngay giữa trận đấu. Cơ chế này có tên là Terastal.

<short pause> Về sau còn có một hệ Tera đặc biệt tên là Tinh tú, xuất hiện trong phần mở rộng. Kaku ghi cần kiểm lại cho chi tiết này.

<short pause> Mỗi sinh vật có một hệ Tera riêng. Khi kích hoạt, nó mang hệ đó, bất kể hệ gốc là gì. Một sinh vật hệ Lửa có thể bỗng trở thành hệ Nước.

<short pause> Nghĩa là bảng tương khắc giờ có thêm một lớp đoán ý đối thủ. Bạn không chỉ nhìn hệ trước mặt, mà phải đoán hệ nó sẽ trở thành.

<short pause> Nhưng nhìn theo lịch sử, Terastal vẫn theo đúng nguyên tắc cũ: không bỏ bảng tương khắc, mà thêm công cụ để người chơi xoay chuyển nó.

<short pause> <laugh> Kaku phải nói thật: cơ chế này khiến nhiều người chơi lâu năm vừa thích vừa đau đầu. Ba mươi năm học thuộc bảng, giờ bảng lại biết đổi mặt.
```

**ElevenLabs**

```text
Những sinh vật Rồng thời này thường là át chủ bài trong đội: hiếm, mạnh, và gần như ai có cũng mang ra trận. Các giải đấu lớn đầy những đội có hai, ba con Rồng.

[pause] Sau Siêu linh, tới lượt hệ Rồng thống trị. Tới thời kỳ này, Rồng có nhiều chiêu mạnh, chỉ số cao, và chỉ yếu trước Băng và chính Rồng.

[pause] Hệ Tiên còn khắc chế Giác đấu và Bóng tối, hai hệ đang rất mạnh lúc đó. Một hệ mới, cùng lúc kiềm chế ba kẻ thống trị.

[pause] Năm 2013, phiên bản X và Y thêm hệ thứ mười tám: Tiên. Đây là hệ mới đầu tiên sau hơn mười hai năm.

[pause] Phát minh của hệ Tiên: miễn nhiễm hoàn toàn với chiêu Rồng, và đánh Rồng gấp đôi. Kẻ thống trị lần đầu gặp khắc tinh thật sự.

[pause] Để Tiên không trở thành hệ quá mạnh tiếp theo, nó yếu trước Độc và Thép. Hai hệ vốn ít được dùng để tấn công bỗng có giá trị hơn.

[pause] Nhiều sinh vật mang hình dáng dễ thương hay mang yếu tố thần tiên được xếp lại vào hệ mới. Có những sinh vật Siêu linh được thêm hệ Tiên và bỗng trở thành khắc tinh của Rồng.

[pause] Một số sinh vật cũ còn được đổi hệ sang Tiên. Những sinh vật bao nhiêu năm là hệ Thường bỗng có danh tính mới.

[pause] Và hệ Thép bị giảm nhẹ: mất khả năng chống chịu chiêu Ma và Bóng tối. Mười hai năm làm bức tường, giờ tường cũng phải có vài cửa sổ.

[pause] Thời kỳ gần nhất không thêm hệ, nhưng cho phép một điều trước đây không thể: đổi hệ ngay giữa trận đấu. Cơ chế này có tên là Terastal.

[pause] Về sau còn có một hệ Tera đặc biệt tên là Tinh tú, xuất hiện trong phần mở rộng. Kaku ghi cần kiểm lại cho chi tiết này.

[pause] Mỗi sinh vật có một hệ Tera riêng. Khi kích hoạt, nó mang hệ đó, bất kể hệ gốc là gì. Một sinh vật hệ Lửa có thể bỗng trở thành hệ Nước.

[pause] Nghĩa là bảng tương khắc giờ có thêm một lớp đoán ý đối thủ. Bạn không chỉ nhìn hệ trước mặt, mà phải đoán hệ nó sẽ trở thành.

[pause] Nhưng nhìn theo lịch sử, Terastal vẫn theo đúng nguyên tắc cũ: không bỏ bảng tương khắc, mà thêm công cụ để người chơi xoay chuyển nó.

[pause] [chuckles] Kaku phải nói thật: cơ chế này khiến nhiều người chơi lâu năm vừa thích vừa đau đầu. Ba mươi năm học thuộc bảng, giờ bảng lại biết đổi mặt.
```

### c08 · Anime và trò chơi: hai luật khác nhau / Góc nhìn của Kaku: một hệ thống sống

Khoảng 153 giây · cảnh s65–s77 · 1992 ký tự

**Gemini**

```text
Có cả những trận mà nhân vật chính thắng bằng cách đảo ngược bảng tương khắc: dùng điểm yếu của mình làm điểm mạnh, hoặc dùng địa hình chiến đấu để bù lại bất lợi.

<short pause> Còn trong anime thì sao? Anime Pokémon dùng bảng tương khắc lỏng hơn nhiều. Một sinh vật hệ Điện có thể thắng hệ Đất nhờ ý chí, chiến thuật, hoặc đơn giản vì nó là nhân vật chính.

<short pause> Kaku nghĩ đây là lựa chọn có chủ đích. Trò chơi cần luật chặt để công bằng. Phim thì cần kịch tính, và kịch tính đến từ việc vượt qua lợi thế.

<short pause> Kaku để ý thấy những trận hay nhất trong anime thường là trận mà bảng tương khắc bất lợi cho nhân vật chính. Phim dùng bảng để tạo khó khăn, rồi dùng tình bạn để vượt qua.

<short pause> Nhưng anime vẫn dùng bảng làm nền. Khi nhân vật chính đổi sinh vật đúng hệ để thắng, người xem thấy mình hiểu và cổ vũ theo.

<short pause> Và ba mươi năm qua, cậu bé Satoshi cùng chú chuột điện của mình đã dạy cả một thế hệ thuộc lòng bảng tương khắc mà không cần sách giáo khoa.

<short pause> Hầu hết hệ thống sức mạnh trong anime được viết một lần rồi giữ nguyên. Bảng tương khắc Pokémon thì khác: nó là một hệ thống sống, được sửa đi sửa lại suốt ba mươi năm.

<short pause> Và mỗi thời kỳ đều để lại những hệ từng mạnh rồi yếu, từng bị quên rồi được nhớ lại. Côn trùng từng vô dụng, giờ có nhiều chiêu đáng dùng. Độc từng bị coi thường, giờ là khắc tinh của Tiên.

<short pause> Mỗi lần sửa đều theo một nguyên tắc giống nhau: khi một hệ quá mạnh, không cấm nó, mà thêm khắc tinh. Siêu linh có Bóng tối, Rồng có Tiên.

<short pause> Kaku thấy đây là cách cân bằng rất đáng học, không chỉ trong trò chơi. Khi một thứ trở nên quá áp đảo, đôi khi giải pháp tốt nhất là tạo thêm lựa chọn, chứ không phải cấm đoán.

<short pause> Kaku để một gợi ý: hãy nhìn xem hệ nào xuất hiện nhiều nhất trong các đội thi đấu hiện nay. Lịch sử cho thấy đó thường là ứng viên tiếp theo cần một khắc tinh.

<short pause> <laugh> Kaku thì chỉ mong có một hệ Cú. Mạnh trước Côn trùng, yếu trước… bài kiểm tra buổi sáng.

<short pause> Theo bạn, hệ nào hiện đang quá mạnh và cần một khắc tinh mới? Và nếu được đặt tên hệ thứ mười chín, bạn chọn gì? Kaku đoán sẽ có người đề xuất hệ Ánh sáng.
```

**ElevenLabs**

```text
Có cả những trận mà nhân vật chính thắng bằng cách đảo ngược bảng tương khắc: dùng điểm yếu của mình làm điểm mạnh, hoặc dùng địa hình chiến đấu để bù lại bất lợi.

[pause] [curious] Còn trong anime thì sao? Anime Pokémon dùng bảng tương khắc lỏng hơn nhiều. Một sinh vật hệ Điện có thể thắng hệ Đất nhờ ý chí, chiến thuật, hoặc đơn giản vì nó là nhân vật chính.

[pause] Kaku nghĩ đây là lựa chọn có chủ đích. Trò chơi cần luật chặt để công bằng. Phim thì cần kịch tính, và kịch tính đến từ việc vượt qua lợi thế.

[pause] Kaku để ý thấy những trận hay nhất trong anime thường là trận mà bảng tương khắc bất lợi cho nhân vật chính. Phim dùng bảng để tạo khó khăn, rồi dùng tình bạn để vượt qua.

[pause] Nhưng anime vẫn dùng bảng làm nền. Khi nhân vật chính đổi sinh vật đúng hệ để thắng, người xem thấy mình hiểu và cổ vũ theo.

[pause] Và ba mươi năm qua, cậu bé Satoshi cùng chú chuột điện của mình đã dạy cả một thế hệ thuộc lòng bảng tương khắc mà không cần sách giáo khoa.

[pause] Hầu hết hệ thống sức mạnh trong anime được viết một lần rồi giữ nguyên. Bảng tương khắc Pokémon thì khác: nó là một hệ thống sống, được sửa đi sửa lại suốt ba mươi năm.

[pause] Và mỗi thời kỳ đều để lại những hệ từng mạnh rồi yếu, từng bị quên rồi được nhớ lại. Côn trùng từng vô dụng, giờ có nhiều chiêu đáng dùng. Độc từng bị coi thường, giờ là khắc tinh của Tiên.

[pause] Mỗi lần sửa đều theo một nguyên tắc giống nhau: khi một hệ quá mạnh, không cấm nó, mà thêm khắc tinh. Siêu linh có Bóng tối, Rồng có Tiên.

[pause] Kaku thấy đây là cách cân bằng rất đáng học, không chỉ trong trò chơi. Khi một thứ trở nên quá áp đảo, đôi khi giải pháp tốt nhất là tạo thêm lựa chọn, chứ không phải cấm đoán.

[pause] Kaku để một gợi ý: hãy nhìn xem hệ nào xuất hiện nhiều nhất trong các đội thi đấu hiện nay. Lịch sử cho thấy đó thường là ứng viên tiếp theo cần một khắc tinh.

[pause] [chuckles] Kaku thì chỉ mong có một hệ Cú. Mạnh trước Côn trùng, yếu trước… bài kiểm tra buổi sáng.

[pause] Theo bạn, hệ nào hiện đang quá mạnh và cần một khắc tinh mới? Và nếu được đặt tên hệ thứ mười chín, bạn chọn gì? Kaku đoán sẽ có người đề xuất hệ Ánh sáng.
```

### c09 · Đường thời gian thu gọn / Kết

Khoảng 82 giây · cảnh s78–s86 · 1072 ký tự

**Gemini**

```text
<laugh> Kaku thu gọn ba mươi năm vào một đường thời gian.

<short pause> Năm 1996: mười lăm hệ và ý tưởng bảng tương khắc. Siêu linh thống trị vì lỗi hệ Ma và chiêu Côn trùng quá yếu.

<short pause> Năm 2002: đặc tính, những ngoại lệ gắn với từng sinh vật.

<short pause> Năm 1999: thêm Bóng tối và Thép, sửa lỗi hệ Ma, tách chỉ số Đặc biệt. Năm 2006: tách chiêu vật lý và đặc biệt.

<short pause> Năm 2013: thêm hệ Tiên để khắc chế Rồng. Năm 2022: đổi hệ ngay trong trận. Và năm 2026: Pokémon tròn ba mươi tuổi.

<short pause> Và có lẽ đó là lý do Pokémon sống được ba mươi năm: mỗi lần người chơi tìm ra cách phá, trò chơi lại tìm ra cách cân bằng. Hai bên cùng lớn lên.

<short pause> Từ mười lăm lên mười tám hệ, ba mươi năm của bảng tương khắc là câu chuyện về việc sửa sai, cân bằng và mở rộng. Một hệ thống sức mạnh không cần hoàn hảo ngay từ đầu, miễn là nó biết lắng nghe.

<short pause> Video tiếp theo, Kaku mở một phiên tòa. Bị cáo là Eren Yeager. Kaku sẽ trình bày cáo trạng, lời bào chữa và các nhân chứng, còn phán quyết là của bạn.

<short pause> Nếu bạn lớn lên cùng bảng tương khắc này, hãy đăng ký kênh và chia sẻ video cho người bạn từng đấu với bạn hồi nhỏ. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Kaku thu gọn ba mươi năm vào một đường thời gian.

[pause] Năm 1996: mười lăm hệ và ý tưởng bảng tương khắc. Siêu linh thống trị vì lỗi hệ Ma và chiêu Côn trùng quá yếu.

[pause] Năm 2002: đặc tính, những ngoại lệ gắn với từng sinh vật.

[pause] Năm 1999: thêm Bóng tối và Thép, sửa lỗi hệ Ma, tách chỉ số Đặc biệt. Năm 2006: tách chiêu vật lý và đặc biệt.

[pause] Năm 2013: thêm hệ Tiên để khắc chế Rồng. Năm 2022: đổi hệ ngay trong trận. Và năm 2026: Pokémon tròn ba mươi tuổi.

[pause] Và có lẽ đó là lý do Pokémon sống được ba mươi năm: mỗi lần người chơi tìm ra cách phá, trò chơi lại tìm ra cách cân bằng. Hai bên cùng lớn lên.

[pause] Từ mười lăm lên mười tám hệ, ba mươi năm của bảng tương khắc là câu chuyện về việc sửa sai, cân bằng và mở rộng. Một hệ thống sức mạnh không cần hoàn hảo ngay từ đầu, miễn là nó biết lắng nghe.

[pause] Video tiếp theo, Kaku mở một phiên tòa. Bị cáo là Eren Yeager. Kaku sẽ trình bày cáo trạng, lời bào chữa và các nhân chứng, còn phán quyết là của bạn.

[pause] Nếu bạn lớn lên cùng bảng tương khắc này, hãy đăng ký kênh và chia sẻ video cho người bạn từng đấu với bạn hồi nhỏ. Kaku gấp sổ đây, hẹn gặp lại!
```
