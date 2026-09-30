# Bộ prompt · Jujutsu Kaisen: Luật chơi Tử Diệt Hồi Du và 4 cách phá

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 9 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo: video có spoiler Jujutsu Kaisen tới anime mùa ba, phần đầu của arc Tử Diệt Hồi Du. Kaku không nói n…

```text
Wide 16:9 landscape cinematic frame. a darkened city skyline at night with faint glowing barrier domes over several districts, a closed notebook on a rooftop ledge, wide establishing shot, eerie violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Giả sử một sáng thức dậy, bạn phát hiện mình có năng lực lạ. Chưa kịp vui, một sinh vật nhỏ xuất hiện và đọc…

```text
Wide 16:9 landscape cinematic frame. a startled young person in pajamas facing a small floating golden creature reading from a scroll in a sunlit bedroom, medium shot, uneasy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trò chơi diễn ra trong những khu vực bị kết giới bao quanh khắp nước Nhật. Muốn ghi điểm, người chơi phải lấy…

```text
Wide 16:9 landscape cinematic frame. a map of Japan with ten glowing dome shapes scattered across it, clean parchment diagram, crimson and navy ink. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đó là Tử Diệt Hồi Du, trò chơi sinh tử do phản diện Kenjaku tạo ra. Và nó có một bộ luật được viết cực kỳ chặ…

```text
Wide 16:9 landscape cinematic frame. a thick rulebook bound in dark leather with a lock on its cover, lying on a stone altar, close-up, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Trò chơi sinh tử là một thể loại quen thuộc: từ tiểu thuyết Battle Royale năm 1999 của Nhật, tới loạt phim Hà…

```text
Wide 16:9 landscape cinematic frame. a stack of thriller novels and a TV remote on a table, a small game board with a skull icon beside them, close-up, dim dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Tử Diệt Hồi Du khác ở chỗ: luật của nó không đơn giản. Nó giống một bộ luật thật, có điều khoản, có ngoại lệ,…

```text
Wide 16:9 landscape cinematic frame. an ornate legal code book with numbered articles and footnotes, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đọc từng luật của Tử Diệt Hồi Du như một luật sư đọc hợp đồng, rồi c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny reading glasses, holding a long contract scroll with a red pen. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Cuối video là bảng luật và cách phá trong một hình. Nhắc lại: Kaku chỉ nói về những gì đã lên anime.

```text
Wide 16:9 landscape cinematic frame. a two-column table sketched on parchment with a lock icon on the left and a key icon on the right, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · Bối cảnh: vì sao có trò chơi này

Lời: Sau sự kiện Shibuya, Gojo bị phong ấn, và Kenjaku, kẻ đã sống hơn một nghìn năm bằng cách chiếm thân xác ngườ…

```text
Wide 16:9 landscape cinematic frame. a sealed cube resting in a dark empty room, and a shadowy robed figure standing in a distant doorway, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Vì vậy trong trò chơi có ba kiểu người chơi: thuật sư hiện đại như Itadori, người thường vừa thức tỉnh và hoả…

```text
Wide 16:9 landscape cinematic frame. three groups of silhouettes standing apart in a ruined city: young sorcerers, frightened ordinary people, and imposing ancient warriors, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Hãy tưởng tượng một nhân viên văn phòng bình thường bị đặt chung sân chơi với một chiến binh từ nghìn năm trư…

```text
Wide 16:9 landscape cinematic frame. an office worker in a suit clutching a briefcase, facing a towering ancient warrior silhouette in an empty street, low-angle shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Hắn đánh thức năng lực tiềm ẩn ở rất nhiều người bình thường, và đưa những thuật sư cổ đại tái sinh vào thân…

```text
Wide 16:9 landscape cinematic frame. a crowd of ordinary people in a city square with faint glowing marks appearing on some of them, ancient warrior silhouettes superimposed faintly, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Mục đích của trò chơi không phải để tìm người thắng. Nó là để tạo ra thật nhiều chú lực và những trận đấu, ph…

```text
Wide 16:9 landscape cinematic frame. a large glowing funnel collecting streams of violet energy from many small domes, symbolic diagram, cold light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Các khu kết giới có luật riêng về ra vào: bước vào thì dễ, nhưng rời đi thì gần như không thể nếu không có cá…

```text
Wide 16:9 landscape cinematic frame. a shimmering dome wall with arrows pointing easily inward and a single arrow blocked trying to exit, parchment diagram, violet ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và người quản lý trò chơi là những sinh vật nhỏ màu vàng tên Kogane. Chúng đi theo mỗi người chơi, đọc điểm,…

```text
Wide 16:9 landscape cinematic frame. a small round golden creature floating beside a player's shoulder, displaying a tiny glowing scoreboard, close-up, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Kogane nói chuyện rất vui vẻ, như một người dẫn chương trình trò chơi truyền hình. Đó là điều k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring nervously at a tiny golden creature holding a game show microphone. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Luật 1, 2 và 3: không thể đứng ngoài

Lời: Luật một: ai đã thức tỉnh năng lực phải tuyên bố tham gia tại một khu kết giới trong vòng mười chín ngày.

```text
Wide 16:9 landscape cinematic frame. a large calendar with nineteen days boxed in red and a countdown clock beside it, close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Luật hai: ai vi phạm luật một sẽ bị tước năng lực. Nghe thì nhẹ, nhưng tước năng lực trong trò chơi này đồng…

```text
Wide 16:9 landscape cinematic frame. a glowing cursed mark fading from a person's hand as they collapse, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Luật ba: người thường bước vào khu kết giới cũng trở thành người chơi. Nghĩa là không ai được làm khán giả an…

```text
Wide 16:9 landscape cinematic frame. an ordinary pedestrian stepping through a shimmering barrier wall and a small golden creature instantly appearing beside them, medium shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Có một chi tiết Kaku thấy rất khôn: luật một cho mười chín ngày để quyết định. Đủ dài để người ta hiểu chuyện…

```text
Wide 16:9 landscape cinematic frame. a calendar with nineteen days where the first days show confusion and the last days show panic, parchment storyboard, amber and crimson ink. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và việc phải tuyên bố tham gia cũng có ý nghĩa: giống như ký vào một hợp đồng. Trong thế giới chú thuật, lời…

```text
Wide 16:9 landscape cinematic frame. a hand signing a glowing contract with a quill, the ink turning into faint light, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Ba luật đầu tiên có chung một mục đích: không để ai đứng ngoài. Người có năng lực buộc phải vào, người không…

```text
Wide 16:9 landscape cinematic frame. a funnel diagram on parchment with arrows from all directions flowing into a single dome, no arrows flowing out, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mà là người thường lỡ bước vào, chắc sẽ hỏi Kogane có mục bỏ qua hướng dẫn không. Chắc chắn là không.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing hopefully at a tiny skip button while a golden creature shakes its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Kaku gọi đây là luật giăng lưới. Một trò chơi mà ngay cả việc từ chối chơi cũng là một nước đi thua.

```text
Wide 16:9 landscape cinematic frame. a vast net stretched over a city at night with small lights caught inside it, wide shot, cold violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Luật 4 và 5: bảng điểm của sự sống

Lời: Luật bốn: người chơi ghi điểm bằng cách lấy mạng người chơi khác.

```text
Wide 16:9 landscape cinematic frame. a stark scoreboard icon on parchment with a single up arrow, crimson ink, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Từ thông thường trong luật năm rất đáng chú ý. Nó gợi ý rằng quản trò có thể định giá khác trong những trường…

```text
Wide 16:9 landscape cinematic frame. a single word highlighted with a magnifying glass on a printed rule, extreme close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Luật năm: thông thường, mạng một thuật sư là năm điểm, mạng một người không phải thuật sư là một điểm.

```text
Wide 16:9 landscape cinematic frame. two small token stacks on a scale, one with five tokens labeled with a spark icon, one with a single token labeled with a plain person icon, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Theo lý thuyết trò chơi, luật bốn và năm tạo ra một tình huống giống thế lưỡng nan của người tù: nếu ai cũng…

```text
Wide 16:9 landscape cinematic frame. two figures in separate glowing cells each looking at a button, a question mark between them, parchment diagram, cold light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và trò chơi được thiết kế để niềm tin sụp đổ: người chơi không biết ai là người thường vừa thức tỉnh, ai là t…

```text
Wide 16:9 landscape cinematic frame. a crowd of identical ordinary-looking silhouettes where one shadow on the ground reveals an ancient warrior's shape, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Kaku nghĩ luật này tàn nhẫn nhất, vì nó định giá con người. Một người thường chỉ bằng một phần năm một thuật…

```text
Wide 16:9 landscape cinematic frame. a price tag hanging from a small paper figure, extreme close-up, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Nói cách khác, luật chỉ định giá mạng người, không bắt ai phải chọn mạng của người vô tội. Lựa chọn đó thuộc…

```text
Wide 16:9 landscape cinematic frame. a fork in a path on parchment, one side marked with a small shield, the other with a cracked icon, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nhưng luật năm cũng tạo ra một lựa chọn cho người tốt: nếu phải ghi điểm, hãy săn những thuật sư cổ đại đang…

```text
Wide 16:9 landscape cinematic frame. a young sorcerer silhouette confronting a menacing ancient warrior silhouette in a ruined street, protecting civilians behind him, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Luật 6 và 7: chiếc chìa khóa

Lời: Luật sáu là luật quan trọng nhất: người chơi có thể dùng một trăm điểm để thương lượng với quản trò, thêm một…

```text
Wide 16:9 landscape cinematic frame. a golden key made of glowing points hovering above an open rulebook, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nhưng thế nào là ảnh hưởng quá lớn? Luật không định nghĩa. Người quyết định là quản trò. Vì vậy thêm luật khô…

```text
Wide 16:9 landscape cinematic frame. a player and a small golden creature sitting across a tiny negotiation table with documents spread between them, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Một luật mới càng nhỏ, càng cụ thể thì càng dễ được chấp nhận. Muốn thay đổi lớn, phải chia thành nhiều luật…

```text
Wide 16:9 landscape cinematic frame. a large boulder broken down into many small pebbles along a path, symbolic illustration, parchment style. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Luật bảy: quản trò phải chấp nhận luật mới, trừ khi nó ảnh hưởng quá lớn và lâu dài tới trò chơi.

```text
Wide 16:9 landscape cinematic frame. a small golden creature nodding solemnly while holding a stamp over a document, humorous close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Có thể chính Kenjaku cố ý để lại lỗ hổng này. Một trò chơi có hy vọng thì người chơi sẽ chiến đấu hăng hơn, t…

```text
Wide 16:9 landscape cinematic frame. a small lantern glowing at the end of a long dark maze, a shadowy figure watching from above the walls, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Đây chính là lỗ hổng mà cả trò chơi được thiết kế để có. Nó cho người chơi hy vọng rằng họ có thể thay đổi lu…

```text
Wide 16:9 landscape cinematic frame. a small keyhole glowing in the side of a massive dark wall, extreme close-up, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhưng giới hạn của luật bảy rất khôn khéo: không được thay đổi quá lớn. Bạn không thể thêm một luật kiểu kết…

```text
Wide 16:9 landscape cinematic frame. a staircase of tiny steps carved into a steep cliff, a small figure starting to climb, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: luật sáu và bảy biến trò chơi sinh tử thành một trò chơi pháp lý. Người thắng không phải người…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drafting a clause on parchment with great concentration, a tiny golden key beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Luật 8: đồng hồ không bao giờ dừng

Lời: Luật tám: nếu điểm của một người chơi không thay đổi trong mười chín ngày, người đó sẽ bị tước năng lực.

```text
Wide 16:9 landscape cinematic frame. a large clock face with its hands moving and a small figure standing still beneath it, symbolic wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Kết hợp với luật bốn, luật tám nghĩa là mỗi người chơi phải lấy ít nhất một mạng người mỗi mười chín ngày để…

```text
Wide 16:9 landscape cinematic frame. a circular arrow diagram with a skull icon and a clock icon endlessly chasing each other, parchment style, crimson ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Luật này chặn cách chơi an toàn nhất: trốn đi và không làm gì. Ai cũng buộc phải chiến đấu, và phải chiến đấu…

```text
Wide 16:9 landscape cinematic frame. a hiding place under a staircase with a small countdown timer glowing beside a crouching figure, medium shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kaku để ý: không có luật nào nói về người thắng cuộc. Trò chơi không có vạch đích. Đó là dấu hiệu rõ nhất rằn…

```text
Wide 16:9 landscape cinematic frame. an empty finish line ribbon lying on the ground in an abandoned stadium, wide shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Kết hợp luật một và luật tám, bạn sẽ thấy trò chơi được thiết kế như một cái máy ép: nó đẩy tất cả người chơi…

```text
Wide 16:9 landscape cinematic frame. a mechanical press slowly closing on a crowd of small figures, symbolic parchment illustration, crimson ink. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Cách phá 1: thêm luật để thoát

Lời: Giờ tới phần phá luật. Mục tiêu của phe Itadori và Fushiguro rất rõ: dùng chính luật sáu để thêm những luật g…

```text
Wide 16:9 landscape cinematic frame. two young sorcerer silhouettes studying a large rulebook together on a rooftop at dusk, back view, warm light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng luật đó phải được viết khéo. Nếu nó cho phép tất cả rời đi ngay, quản trò sẽ từ chối vì ảnh hưởng quá l…

```text
Wide 16:9 landscape cinematic frame. two hands carefully editing a draft rule with many crossed-out words, extreme close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ý tưởng đầu tiên: thêm một luật cho phép người chơi rời khỏi trò chơi. Nếu được chấp nhận, người thường bị kẹ…

```text
Wide 16:9 landscape cinematic frame. a small door appearing in a glowing barrier wall with ordinary people walking out, wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Kaku để ý: gần như nhân vật nào trong arc này cũng có một người thân để cứu. Tác giả biến một trò chơi lạnh l…

```text
Wide 16:9 landscape cinematic frame. many small photographs pinned inside a glowing dome map, each showing a different family, parchment illustration, warm light. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Fushiguro có một lý do cá nhân: em gái của cậu, Tsumiki, cũng bị cuốn vào trò chơi. Với cậu, đây không chỉ là…

```text
Wide 16:9 landscape cinematic frame. a young man standing alone in the rain looking at an old photograph of a smiling girl, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Cái giá: muốn có một trăm điểm, vẫn phải hạ gục những người chơi khác. Người tốt cũng phải tham gia trò chơi…

```text
Wide 16:9 landscape cinematic frame. a clean white glove stained at the fingertips with dark ink, extreme close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Cách phá 2: gom điểm vào một người

Lời: Một trăm điểm là con số rất lớn. Nếu mỗi người tự kiếm, họ sẽ mất rất lâu. Vì vậy một ý tưởng khác là cho phé…

```text
Wide 16:9 landscape cinematic frame. several small glowing point tokens flowing from multiple hands into one player's palm, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nghĩa là một người không cần tự tay lấy đủ một trăm mạng. Cả nhóm cùng chia gánh nặng, rồi dồn cho người đáng…

```text
Wide 16:9 landscape cinematic frame. a group of hands placing glowing tokens into a single small chest held by one person, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nếu chuyển được điểm, cả nhóm có thể dồn điểm cho một người đủ một trăm, để người đó thêm luật mới cho tất cả.

```text
Wide 16:9 landscape cinematic frame. a diagram showing many small circles connected by arrows to one larger circle labeled 100, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Kaku thấy đây là cách phá thông minh nhất: biến một trò chơi được thiết kế để người chơi giết nhau thành một…

```text
Wide 16:9 landscape cinematic frame. two players shaking hands inside a glowing barrier while a small golden creature looks puzzled, humorous medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Cái giá: phải tin tưởng người khác trong một trò chơi mà ai cũng có thể là kẻ thù. Và luật chuyển điểm cũng c…

```text
Wide 16:9 landscape cinematic frame. a handshake where one hand is hiding a small blade behind the back, close-up, tense cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Cách phá 3: săn đúng người

Lời: Cách phá thứ ba không cần thêm luật: chọn kỹ đối thủ. Thay vì săn người thường một điểm, hãy đối đầu những th…

```text
Wide 16:9 landscape cinematic frame. a young sorcerer silhouette standing between a frightened crowd and an approaching ancient warrior, protective stance, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Và có một điểm tinh tế: thuật sư cổ đại thường mạnh vì họ đã quen với chiến tranh và cái chết. Người hiện đại…

```text
Wide 16:9 landscape cinematic frame. a group of young sorcerers coordinating an attack on a large ancient warrior using a tactical plan sketched in the air, dynamic wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cách này vừa ghi điểm, vừa bảo vệ người vô tội. Nhưng nó cũng nguy hiểm nhất, vì những thuật sư cổ đại thường…

```text
Wide 16:9 landscape cinematic frame. a massive intimidating figure towering over a smaller sorcerer in a ruined plaza, low-angle shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: đây là cách mà các nhân vật chính chọn gần như trong mọi trận. Họ biến luật tàn nhẫn nhất, luật nă…

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling rule five on the rulebook and drawing a small shield icon beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Cái giá: mỗi trận đấu với thuật sư cổ đại có thể là trận cuối cùng.

```text
Wide 16:9 landscape cinematic frame. a cracked mask lying in the rubble of a ruined street, extreme close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Cách phá 4: đánh vào người tạo luật

Lời: Cách phá lớn nhất là không phá luật, mà phá người tạo ra luật. Nếu Kenjaku bị ngăn lại, trò chơi sẽ mất lý do…

```text
Wide 16:9 landscape cinematic frame. a hand reaching toward a shadowy puppeteer silhouette above a stage full of small figures on strings, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Kaku nhớ lại video về Gojo: một thế giới dựa vào một người mạnh nhất thì rất mong manh. Arc này chính là lúc…

```text
Wide 16:9 landscape cinematic frame. a group of young silhouettes holding up a cracked stone pillar together, wide shot, dramatic dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và cũng có một mục tiêu song song: giải phóng Gojo khỏi phong ấn. Người mạnh nhất nếu trở lại sẽ thay đổi hoà…

```text
Wide 16:9 landscape cinematic frame. a sealed cube glowing faintly in a dark room with a small crack of light on its surface, close-up, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Cái giá: cả hai mục tiêu đều cần thời gian, trong khi luật tám không cho ai thời gian. Mỗi ngày trôi qua là t…

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand pouring onto a map of glowing domes, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Kaku dừng ở đây. Những gì xảy ra tiếp theo, bạn sẽ thấy ở phần sau của anime.

```text
Wide 16:9 landscape cinematic frame. a notebook closing with a bookmark sticking out at a page marked with a question mark, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Bảng luật và cách phá

Lời: Kaku gom lại thành một bảng. Luật một, hai, ba: không ai đứng ngoài. Cách phá: không có, chỉ có thể bước vào…

```text
Wide 16:9 landscape cinematic frame. a two-column table on parchment, the first row with a net icon on the left and a closed door icon on the right, amber ink. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Luật bốn, năm: điểm là mạng người. Cách phá: săn đúng người, những kẻ đang gây hại. Cái giá: đối thủ mạnh hơn…

```text
Wide 16:9 landscape cinematic frame. the second row with a scoreboard icon and a shield icon, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Một dòng nhỏ Kaku viết thêm dưới bảng: mọi cách phá đều dùng luật của chính trò chơi. Không ai thoát ra bằng…

```text
Wide 16:9 landscape cinematic frame. a footnote line written at the bottom of the table with a small key and book icon, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Luật sáu, bảy: một trăm điểm đổi một luật. Cách phá: thêm luật cho phép rời trò chơi, chuyển điểm để dồn cho…

```text
Wide 16:9 landscape cinematic frame. the third row with a key icon and a handshake icon, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Luật tám: không được đứng yên. Cách phá lớn nhất: nhắm vào người viết luật, và đưa người mạnh nhất trở lại. C…

```text
Wide 16:9 landscape cinematic frame. the final row with a clock icon and a broken chain icon, glowing slightly, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Góc nhìn của Kaku: một trò chơi dạy người chơi viết luật

Lời: Nếu so với Trò chơi con mực, nơi người chơi chỉ có thể bỏ phiếu dừng trò chơi, thì Tử Diệt Hồi Du cho người c…

```text
Wide 16:9 landscape cinematic frame. a comparison sketch of a simple ballot box and a complex rulebook with a key, side by side on parchment, amber ink. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải thừa nhận: đọc bộ luật này giống như làm bài tập môn luật. Nhưng đây là bài tập mà sai một điều kho…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sweating over a thick legal exam paper with a red timer beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Kaku thấy Tử Diệt Hồi Du là một trong những trò chơi sinh tử được thiết kế thông minh nhất trong anime. Không…

```text
Wide 16:9 landscape cinematic frame. a large rulebook with many handwritten amendments in different inks, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và chính điều đó biến các nhân vật chính từ nạn nhân thành người viết lại câu chuyện. Họ không thắng bằng các…

```text
Wide 16:9 landscape cinematic frame. a young sorcerer rewriting a line in a giant rulebook with a glowing brush, low-angle shot, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn có một trăm điểm, bạn sẽ thêm luật gì vào Tử Diệt Hồi Du? Nhớ luật bảy: không được quá lớn. Viết luật…

```text
Wide 16:9 landscape cinematic frame. a blank rule card and a pen on a desk with a small golden creature waiting beside it, top-down shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Kết

Lời: Và đó là một thông điệp rất đẹp của Jujutsu Kaisen: khi luật bất công, đừng chỉ tìm cách sống sót trong đó. H…

```text
Wide 16:9 landscape cinematic frame. a hand holding a pen correcting a line on a large public notice board in a city square, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Tử Diệt Hồi Du bắt đầu như một trò chơi để người ta giết nhau. Nhưng với những người như Itadori và Fushiguro…

```text
Wide 16:9 landscape cinematic frame. two young sorcerers standing on a rooftop at dawn looking at the glowing barrier domes across the city, back view, wide shot, determined light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku đưa bạn vào một kỳ thi khác, cũng sinh tử nhưng vui hơn nhiều: nếu bạn dự kỳ thi sát th…

```text
Wide 16:9 landscape cinematic frame. an exam hall with desks, a countdown clock and hidden traps, a nervous candidate holding a pencil, wide shot, tense but playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích đọc luật như đọc hợp đồng cùng Kaku, hãy đăng ký kênh để không bỏ lỡ những bộ luật tiếp theo. K…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the contract scroll and tipping its tiny reading glasses goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 98 giây · cảnh s01–s08 · 1272 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới anime mùa ba, phần đầu của arc Tử Diệt Hồi Du. Kaku không nói những gì chưa lên anime.

<short pause> Giả sử một sáng thức dậy, bạn phát hiện mình có năng lực lạ. Chưa kịp vui, một sinh vật nhỏ xuất hiện và đọc cho bạn nghe luật chơi: trong mười chín ngày, hãy tham gia một trò chơi, hoặc mất năng lực, tức là mất mạng.

<short pause> Trò chơi diễn ra trong những khu vực bị kết giới bao quanh khắp nước Nhật. Muốn ghi điểm, người chơi phải lấy mạng người chơi khác.

<short pause> Đó là Tử Diệt Hồi Du, trò chơi sinh tử do phản diện Kenjaku tạo ra. Và nó có một bộ luật được viết cực kỳ chặt, chặt tới mức cách duy nhất để thoát là tìm lỗ hổng trong chính bộ luật.

<short pause> Trò chơi sinh tử là một thể loại quen thuộc: từ tiểu thuyết Battle Royale năm 1999 của Nhật, tới loạt phim Hàn Quốc Trò chơi con mực năm 2021. Điểm chung là luật chơi đơn giản mà tàn nhẫn.

<short pause> Tử Diệt Hồi Du khác ở chỗ: luật của nó không đơn giản. Nó giống một bộ luật thật, có điều khoản, có ngoại lệ, và có cả quy trình sửa đổi.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đọc từng luật của Tử Diệt Hồi Du như một luật sư đọc hợp đồng, rồi chỉ ra những cách các nhân vật đã dùng để phá luật, và cái giá của mỗi cách.

<short pause> Cuối video là bảng luật và cách phá trong một hình. Nhắc lại: Kaku chỉ nói về những gì đã lên anime.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới anime mùa ba, phần đầu của arc Tử Diệt Hồi Du. Kaku không nói những gì chưa lên anime.

[pause] Giả sử một sáng thức dậy, bạn phát hiện mình có năng lực lạ. Chưa kịp vui, một sinh vật nhỏ xuất hiện và đọc cho bạn nghe luật chơi: trong mười chín ngày, hãy tham gia một trò chơi, hoặc mất năng lực, tức là mất mạng.

[pause] Trò chơi diễn ra trong những khu vực bị kết giới bao quanh khắp nước Nhật. Muốn ghi điểm, người chơi phải lấy mạng người chơi khác.

[pause] Đó là Tử Diệt Hồi Du, trò chơi sinh tử do phản diện Kenjaku tạo ra. Và nó có một bộ luật được viết cực kỳ chặt, chặt tới mức cách duy nhất để thoát là tìm lỗ hổng trong chính bộ luật.

[pause] Trò chơi sinh tử là một thể loại quen thuộc: từ tiểu thuyết Battle Royale năm 1999 của Nhật, tới loạt phim Hàn Quốc Trò chơi con mực năm 2021. Điểm chung là luật chơi đơn giản mà tàn nhẫn.

[pause] Tử Diệt Hồi Du khác ở chỗ: luật của nó không đơn giản. Nó giống một bộ luật thật, có điều khoản, có ngoại lệ, và có cả quy trình sửa đổi.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đọc từng luật của Tử Diệt Hồi Du như một luật sư đọc hợp đồng, rồi chỉ ra những cách các nhân vật đã dùng để phá luật, và cái giá của mỗi cách.

[pause] Cuối video là bảng luật và cách phá trong một hình. Nhắc lại: Kaku chỉ nói về những gì đã lên anime.
```

### c02 · Bối cảnh: vì sao có trò chơi này

Khoảng 102 giây · cảnh s09–s16 · 1321 ký tự

**Gemini**

```text
Sau sự kiện Shibuya, Gojo bị phong ấn, và Kenjaku, kẻ đã sống hơn một nghìn năm bằng cách chiếm thân xác người khác, bắt đầu kế hoạch lớn nhất của mình.

<short pause> Vì vậy trong trò chơi có ba kiểu người chơi: thuật sư hiện đại như Itadori, người thường vừa thức tỉnh và hoảng loạn, và những thuật sư cổ đại tái sinh, mạnh và không có chút đạo đức hiện đại nào.

<short pause> Hãy tưởng tượng một nhân viên văn phòng bình thường bị đặt chung sân chơi với một chiến binh từ nghìn năm trước. Đó là sự bất công được cài sẵn trong trò chơi.

<short pause> Hắn đánh thức năng lực tiềm ẩn ở rất nhiều người bình thường, và đưa những thuật sư cổ đại tái sinh vào thân xác người hiện đại. Rồi hắn nhốt tất cả vào các kết giới.

<short pause> Mục đích của trò chơi không phải để tìm người thắng. Nó là để tạo ra thật nhiều chú lực và những trận đấu, phục vụ kế hoạch bí ẩn của hắn. Kaku sẽ không đi sâu vào mục đích đó để tránh spoiler.

<short pause> Các khu kết giới có luật riêng về ra vào: bước vào thì dễ, nhưng rời đi thì gần như không thể nếu không có cách đặc biệt. Kết giới là bức tường, còn luật là ổ khóa.

<short pause> Và người quản lý trò chơi là những sinh vật nhỏ màu vàng tên Kogane. Chúng đi theo mỗi người chơi, đọc điểm, thông báo luật mới, và không thể bị mua chuộc.

<short pause> <laugh> Kaku ghi chú: Kogane nói chuyện rất vui vẻ, như một người dẫn chương trình trò chơi truyền hình. Đó là điều khiến trò chơi càng đáng sợ.
```

**ElevenLabs**

```text
Sau sự kiện Shibuya, Gojo bị phong ấn, và Kenjaku, kẻ đã sống hơn một nghìn năm bằng cách chiếm thân xác người khác, bắt đầu kế hoạch lớn nhất của mình.

[pause] Vì vậy trong trò chơi có ba kiểu người chơi: thuật sư hiện đại như Itadori, người thường vừa thức tỉnh và hoảng loạn, và những thuật sư cổ đại tái sinh, mạnh và không có chút đạo đức hiện đại nào.

[pause] Hãy tưởng tượng một nhân viên văn phòng bình thường bị đặt chung sân chơi với một chiến binh từ nghìn năm trước. Đó là sự bất công được cài sẵn trong trò chơi.

[pause] Hắn đánh thức năng lực tiềm ẩn ở rất nhiều người bình thường, và đưa những thuật sư cổ đại tái sinh vào thân xác người hiện đại. Rồi hắn nhốt tất cả vào các kết giới.

[pause] Mục đích của trò chơi không phải để tìm người thắng. Nó là để tạo ra thật nhiều chú lực và những trận đấu, phục vụ kế hoạch bí ẩn của hắn. Kaku sẽ không đi sâu vào mục đích đó để tránh spoiler.

[pause] Các khu kết giới có luật riêng về ra vào: bước vào thì dễ, nhưng rời đi thì gần như không thể nếu không có cách đặc biệt. Kết giới là bức tường, còn luật là ổ khóa.

[pause] Và người quản lý trò chơi là những sinh vật nhỏ màu vàng tên Kogane. Chúng đi theo mỗi người chơi, đọc điểm, thông báo luật mới, và không thể bị mua chuộc.

[pause] [chuckles] Kaku ghi chú: Kogane nói chuyện rất vui vẻ, như một người dẫn chương trình trò chơi truyền hình. Đó là điều khiến trò chơi càng đáng sợ.
```

### c03 · Luật 1, 2 và 3: không thể đứng ngoài

Khoảng 78 giây · cảnh s17–s24 · 1018 ký tự

**Gemini**

```text
Luật một: ai đã thức tỉnh năng lực phải tuyên bố tham gia tại một khu kết giới trong vòng mười chín ngày.

<short pause> Luật hai: ai vi phạm luật một sẽ bị tước năng lực. Nghe thì nhẹ, nhưng tước năng lực trong trò chơi này đồng nghĩa với cái chết.

<short pause> Luật ba: người thường bước vào khu kết giới cũng trở thành người chơi. Nghĩa là không ai được làm khán giả an toàn.

<short pause> Có một chi tiết Kaku thấy rất khôn: luật một cho mười chín ngày để quyết định. Đủ dài để người ta hiểu chuyện gì đang xảy ra, nhưng đủ ngắn để không ai kịp tìm cách trốn.

<short pause> Và việc phải tuyên bố tham gia cũng có ý nghĩa: giống như ký vào một hợp đồng. Trong thế giới chú thuật, lời thề và giao ước có sức mạnh thật sự.

<short pause> Ba luật đầu tiên có chung một mục đích: không để ai đứng ngoài. Người có năng lực buộc phải vào, người không có năng lực mà lỡ vào cũng không thể ra.

<short pause> <laugh> Kaku mà là người thường lỡ bước vào, chắc sẽ hỏi Kogane có mục bỏ qua hướng dẫn không. Chắc chắn là không.

<short pause> Kaku gọi đây là luật giăng lưới. Một trò chơi mà ngay cả việc từ chối chơi cũng là một nước đi thua.
```

**ElevenLabs**

```text
Luật một: ai đã thức tỉnh năng lực phải tuyên bố tham gia tại một khu kết giới trong vòng mười chín ngày.

[pause] Luật hai: ai vi phạm luật một sẽ bị tước năng lực. Nghe thì nhẹ, nhưng tước năng lực trong trò chơi này đồng nghĩa với cái chết.

[pause] Luật ba: người thường bước vào khu kết giới cũng trở thành người chơi. Nghĩa là không ai được làm khán giả an toàn.

[pause] Có một chi tiết Kaku thấy rất khôn: luật một cho mười chín ngày để quyết định. Đủ dài để người ta hiểu chuyện gì đang xảy ra, nhưng đủ ngắn để không ai kịp tìm cách trốn.

[pause] Và việc phải tuyên bố tham gia cũng có ý nghĩa: giống như ký vào một hợp đồng. Trong thế giới chú thuật, lời thề và giao ước có sức mạnh thật sự.

[pause] Ba luật đầu tiên có chung một mục đích: không để ai đứng ngoài. Người có năng lực buộc phải vào, người không có năng lực mà lỡ vào cũng không thể ra.

[pause] [chuckles] Kaku mà là người thường lỡ bước vào, chắc sẽ hỏi Kogane có mục bỏ qua hướng dẫn không. Chắc chắn là không.

[pause] Kaku gọi đây là luật giăng lưới. Một trò chơi mà ngay cả việc từ chối chơi cũng là một nước đi thua.
```

### c04 · Luật 4 và 5: bảng điểm của sự sống

Khoảng 87 giây · cảnh s25–s32 · 1127 ký tự

**Gemini**

```text
Luật bốn: người chơi ghi điểm bằng cách lấy mạng người chơi khác.

<short pause> Từ thông thường trong luật năm rất đáng chú ý. Nó gợi ý rằng quản trò có thể định giá khác trong những trường hợp đặc biệt. Một từ nhỏ mở ra cả một vùng mập mờ.

<short pause> Luật năm: thông thường, mạng một thuật sư là năm điểm, mạng một người không phải thuật sư là một điểm.

<short pause> Theo lý thuyết trò chơi, luật bốn và năm tạo ra một tình huống giống thế lưỡng nan của người tù: nếu ai cũng tin nhau thì tất cả an toàn hơn, nhưng mỗi người lại có động cơ ra tay trước.

<short pause> Và trò chơi được thiết kế để niềm tin sụp đổ: người chơi không biết ai là người thường vừa thức tỉnh, ai là thuật sư cổ đại đội lốt người hiện đại.

<short pause> Kaku nghĩ luật này tàn nhẫn nhất, vì nó định giá con người. Một người thường chỉ bằng một phần năm một thuật sư. Và những kẻ muốn ghi điểm nhanh sẽ săn những người yếu nhất.

<short pause> Nói cách khác, luật chỉ định giá mạng người, không bắt ai phải chọn mạng của người vô tội. Lựa chọn đó thuộc về người chơi.

<short pause> Nhưng luật năm cũng tạo ra một lựa chọn cho người tốt: nếu phải ghi điểm, hãy săn những thuật sư cổ đại đang tàn sát người khác, vì họ đáng năm điểm và đang gây nguy hiểm.
```

**ElevenLabs**

```text
Luật bốn: người chơi ghi điểm bằng cách lấy mạng người chơi khác.

[pause] Từ thông thường trong luật năm rất đáng chú ý. Nó gợi ý rằng quản trò có thể định giá khác trong những trường hợp đặc biệt. Một từ nhỏ mở ra cả một vùng mập mờ.

[pause] Luật năm: thông thường, mạng một thuật sư là năm điểm, mạng một người không phải thuật sư là một điểm.

[pause] Theo lý thuyết trò chơi, luật bốn và năm tạo ra một tình huống giống thế lưỡng nan của người tù: nếu ai cũng tin nhau thì tất cả an toàn hơn, nhưng mỗi người lại có động cơ ra tay trước.

[pause] Và trò chơi được thiết kế để niềm tin sụp đổ: người chơi không biết ai là người thường vừa thức tỉnh, ai là thuật sư cổ đại đội lốt người hiện đại.

[pause] Kaku nghĩ luật này tàn nhẫn nhất, vì nó định giá con người. Một người thường chỉ bằng một phần năm một thuật sư. Và những kẻ muốn ghi điểm nhanh sẽ săn những người yếu nhất.

[pause] Nói cách khác, luật chỉ định giá mạng người, không bắt ai phải chọn mạng của người vô tội. Lựa chọn đó thuộc về người chơi.

[pause] Nhưng luật năm cũng tạo ra một lựa chọn cho người tốt: nếu phải ghi điểm, hãy săn những thuật sư cổ đại đang tàn sát người khác, vì họ đáng năm điểm và đang gây nguy hiểm.
```

### c05 · Luật 6 và 7: chiếc chìa khóa / Luật 8: đồng hồ không bao giờ dừng

Khoảng 143 giây · cảnh s33–s45 · 1855 ký tự

**Gemini**

```text
Luật sáu là luật quan trọng nhất: người chơi có thể dùng một trăm điểm để thương lượng với quản trò, thêm một luật mới vào trò chơi.

<short pause> Nhưng thế nào là ảnh hưởng quá lớn? Luật không định nghĩa. Người quyết định là quản trò. Vì vậy thêm luật không chỉ là có điểm, mà còn là nghệ thuật thương lượng.

<short pause> Một luật mới càng nhỏ, càng cụ thể thì càng dễ được chấp nhận. Muốn thay đổi lớn, phải chia thành nhiều luật nhỏ, và mỗi luật cần một trăm điểm.

<short pause> Luật bảy: quản trò phải chấp nhận luật mới, trừ khi nó ảnh hưởng quá lớn và lâu dài tới trò chơi.

<short pause> Có thể chính Kenjaku cố ý để lại lỗ hổng này. Một trò chơi có hy vọng thì người chơi sẽ chiến đấu hăng hơn, tạo ra nhiều chú lực hơn. Hy vọng cũng là một phần của cái bẫy.

<short pause> Đây chính là lỗ hổng mà cả trò chơi được thiết kế để có. Nó cho người chơi hy vọng rằng họ có thể thay đổi luật từ bên trong.

<short pause> Nhưng giới hạn của luật bảy rất khôn khéo: không được thay đổi quá lớn. Bạn không thể thêm một luật kiểu kết thúc trò chơi ngay lập tức. Bạn phải đi từng bước nhỏ.

<short pause> <laugh> Kaku ghi chú: luật sáu và bảy biến trò chơi sinh tử thành một trò chơi pháp lý. Người thắng không phải người mạnh nhất, mà là người viết được luật hay nhất.

<short pause> Luật tám: nếu điểm của một người chơi không thay đổi trong mười chín ngày, người đó sẽ bị tước năng lực.

<short pause> Kết hợp với luật bốn, luật tám nghĩa là mỗi người chơi phải lấy ít nhất một mạng người mỗi mười chín ngày để tồn tại. Nếu không có lỗ hổng nào, đây là một vòng lặp không có lối thoát.

<short pause> Luật này chặn cách chơi an toàn nhất: trốn đi và không làm gì. Ai cũng buộc phải chiến đấu, và phải chiến đấu liên tục.

<short pause> Kaku để ý: không có luật nào nói về người thắng cuộc. Trò chơi không có vạch đích. Đó là dấu hiệu rõ nhất rằng nó không được tạo ra để có người thắng.

<short pause> Kết hợp luật một và luật tám, bạn sẽ thấy trò chơi được thiết kế như một cái máy ép: nó đẩy tất cả người chơi vào nhau, và không bao giờ cho họ nghỉ.
```

**ElevenLabs**

```text
Luật sáu là luật quan trọng nhất: người chơi có thể dùng một trăm điểm để thương lượng với quản trò, thêm một luật mới vào trò chơi.

[pause] [curious] Nhưng thế nào là ảnh hưởng quá lớn? Luật không định nghĩa. Người quyết định là quản trò. Vì vậy thêm luật không chỉ là có điểm, mà còn là nghệ thuật thương lượng.

[pause] Một luật mới càng nhỏ, càng cụ thể thì càng dễ được chấp nhận. Muốn thay đổi lớn, phải chia thành nhiều luật nhỏ, và mỗi luật cần một trăm điểm.

[pause] Luật bảy: quản trò phải chấp nhận luật mới, trừ khi nó ảnh hưởng quá lớn và lâu dài tới trò chơi.

[pause] Có thể chính Kenjaku cố ý để lại lỗ hổng này. Một trò chơi có hy vọng thì người chơi sẽ chiến đấu hăng hơn, tạo ra nhiều chú lực hơn. Hy vọng cũng là một phần của cái bẫy.

[pause] Đây chính là lỗ hổng mà cả trò chơi được thiết kế để có. Nó cho người chơi hy vọng rằng họ có thể thay đổi luật từ bên trong.

[pause] Nhưng giới hạn của luật bảy rất khôn khéo: không được thay đổi quá lớn. Bạn không thể thêm một luật kiểu kết thúc trò chơi ngay lập tức. Bạn phải đi từng bước nhỏ.

[pause] [chuckles] Kaku ghi chú: luật sáu và bảy biến trò chơi sinh tử thành một trò chơi pháp lý. Người thắng không phải người mạnh nhất, mà là người viết được luật hay nhất.

[pause] Luật tám: nếu điểm của một người chơi không thay đổi trong mười chín ngày, người đó sẽ bị tước năng lực.

[pause] Kết hợp với luật bốn, luật tám nghĩa là mỗi người chơi phải lấy ít nhất một mạng người mỗi mười chín ngày để tồn tại. Nếu không có lỗ hổng nào, đây là một vòng lặp không có lối thoát.

[pause] Luật này chặn cách chơi an toàn nhất: trốn đi và không làm gì. Ai cũng buộc phải chiến đấu, và phải chiến đấu liên tục.

[pause] Kaku để ý: không có luật nào nói về người thắng cuộc. Trò chơi không có vạch đích. Đó là dấu hiệu rõ nhất rằng nó không được tạo ra để có người thắng.

[pause] Kết hợp luật một và luật tám, bạn sẽ thấy trò chơi được thiết kế như một cái máy ép: nó đẩy tất cả người chơi vào nhau, và không bao giờ cho họ nghỉ.
```

### c06 · Cách phá 1: thêm luật để thoát / Cách phá 2: gom điểm vào một người

Khoảng 122 giây · cảnh s46–s56 · 1590 ký tự

**Gemini**

```text
Giờ tới phần phá luật. Mục tiêu của phe Itadori và Fushiguro rất rõ: dùng chính luật sáu để thêm những luật giúp người chơi thoát ra.

<short pause> Nhưng luật đó phải được viết khéo. Nếu nó cho phép tất cả rời đi ngay, quản trò sẽ từ chối vì ảnh hưởng quá lớn. Phải viết sao cho đủ nhỏ để được chấp nhận, nhưng đủ lớn để cứu người.

<short pause> Ý tưởng đầu tiên: thêm một luật cho phép người chơi rời khỏi trò chơi. Nếu được chấp nhận, người thường bị kẹt trong kết giới có thể thoát ra mà không phải giết ai.

<short pause> Kaku để ý: gần như nhân vật nào trong arc này cũng có một người thân để cứu. Tác giả biến một trò chơi lạnh lùng thành hàng chục câu chuyện gia đình nhỏ.

<short pause> Fushiguro có một lý do cá nhân: em gái của cậu, Tsumiki, cũng bị cuốn vào trò chơi. Với cậu, đây không chỉ là chiến thuật, mà là cuộc chạy đua để cứu người thân.

<short pause> Cái giá: muốn có một trăm điểm, vẫn phải hạ gục những người chơi khác. Người tốt cũng phải tham gia trò chơi bẩn để có quyền sửa nó.

<short pause> Một trăm điểm là con số rất lớn. Nếu mỗi người tự kiếm, họ sẽ mất rất lâu. Vì vậy một ý tưởng khác là cho phép chuyển điểm giữa những người chơi.

<short pause> Nghĩa là một người không cần tự tay lấy đủ một trăm mạng. Cả nhóm cùng chia gánh nặng, rồi dồn cho người đáng tin nhất để thương lượng.

<short pause> Nếu chuyển được điểm, cả nhóm có thể dồn điểm cho một người đủ một trăm, để người đó thêm luật mới cho tất cả.

<short pause> Kaku thấy đây là cách phá thông minh nhất: biến một trò chơi được thiết kế để người chơi giết nhau thành một trò chơi mà người chơi hợp tác.

<short pause> Cái giá: phải tin tưởng người khác trong một trò chơi mà ai cũng có thể là kẻ thù. Và luật chuyển điểm cũng có thể bị kẻ xấu lợi dụng.
```

**ElevenLabs**

```text
Giờ tới phần phá luật. Mục tiêu của phe Itadori và Fushiguro rất rõ: dùng chính luật sáu để thêm những luật giúp người chơi thoát ra.

[pause] Nhưng luật đó phải được viết khéo. Nếu nó cho phép tất cả rời đi ngay, quản trò sẽ từ chối vì ảnh hưởng quá lớn. Phải viết sao cho đủ nhỏ để được chấp nhận, nhưng đủ lớn để cứu người.

[pause] Ý tưởng đầu tiên: thêm một luật cho phép người chơi rời khỏi trò chơi. Nếu được chấp nhận, người thường bị kẹt trong kết giới có thể thoát ra mà không phải giết ai.

[pause] Kaku để ý: gần như nhân vật nào trong arc này cũng có một người thân để cứu. Tác giả biến một trò chơi lạnh lùng thành hàng chục câu chuyện gia đình nhỏ.

[pause] Fushiguro có một lý do cá nhân: em gái của cậu, Tsumiki, cũng bị cuốn vào trò chơi. Với cậu, đây không chỉ là chiến thuật, mà là cuộc chạy đua để cứu người thân.

[pause] Cái giá: muốn có một trăm điểm, vẫn phải hạ gục những người chơi khác. Người tốt cũng phải tham gia trò chơi bẩn để có quyền sửa nó.

[pause] Một trăm điểm là con số rất lớn. Nếu mỗi người tự kiếm, họ sẽ mất rất lâu. Vì vậy một ý tưởng khác là cho phép chuyển điểm giữa những người chơi.

[pause] Nghĩa là một người không cần tự tay lấy đủ một trăm mạng. Cả nhóm cùng chia gánh nặng, rồi dồn cho người đáng tin nhất để thương lượng.

[pause] Nếu chuyển được điểm, cả nhóm có thể dồn điểm cho một người đủ một trăm, để người đó thêm luật mới cho tất cả.

[pause] Kaku thấy đây là cách phá thông minh nhất: biến một trò chơi được thiết kế để người chơi giết nhau thành một trò chơi mà người chơi hợp tác.

[pause] Cái giá: phải tin tưởng người khác trong một trò chơi mà ai cũng có thể là kẻ thù. Và luật chuyển điểm cũng có thể bị kẻ xấu lợi dụng.
```

### c07 · Cách phá 3: săn đúng người / Cách phá 4: đánh vào người tạo luật

Khoảng 100 giây · cảnh s57–s66 · 1297 ký tự

**Gemini**

```text
Cách phá thứ ba không cần thêm luật: chọn kỹ đối thủ. Thay vì săn người thường một điểm, hãy đối đầu những thuật sư cổ đại đang gây hại, mỗi người năm điểm.

<short pause> Và có một điểm tinh tế: thuật sư cổ đại thường mạnh vì họ đã quen với chiến tranh và cái chết. Người hiện đại phải thắng họ bằng sự sáng tạo, hiểu biết luật chơi và tinh thần đồng đội.

<short pause> Cách này vừa ghi điểm, vừa bảo vệ người vô tội. <short pause> Nhưng nó cũng nguy hiểm nhất, vì những thuật sư cổ đại thường mạnh hơn rất nhiều.

<short pause> <laugh> Kaku để ý: đây là cách mà các nhân vật chính chọn gần như trong mọi trận. Họ biến luật tàn nhẫn nhất, luật năm, thành cơ hội để làm điều đúng.

<short pause> Cái giá: mỗi trận đấu với thuật sư cổ đại có thể là trận cuối cùng.

<short pause> Cách phá lớn nhất là không phá luật, mà phá người tạo ra luật. Nếu Kenjaku bị ngăn lại, trò chơi sẽ mất lý do tồn tại.

<short pause> Kaku nhớ lại video về Gojo: một thế giới dựa vào một người mạnh nhất thì rất mong manh. Arc này chính là lúc thế giới phải học cách chiến đấu khi không có người đó.

<short pause> Và cũng có một mục tiêu song song: giải phóng Gojo khỏi phong ấn. Người mạnh nhất nếu trở lại sẽ thay đổi hoàn toàn cán cân.

<short pause> Cái giá: cả hai mục tiêu đều cần thời gian, trong khi luật tám không cho ai thời gian. Mỗi ngày trôi qua là thêm người chơi bị cuốn vào.

<short pause> Kaku dừng ở đây. Những gì xảy ra tiếp theo, bạn sẽ thấy ở phần sau của anime.
```

**ElevenLabs**

```text
Cách phá thứ ba không cần thêm luật: chọn kỹ đối thủ. Thay vì săn người thường một điểm, hãy đối đầu những thuật sư cổ đại đang gây hại, mỗi người năm điểm.

[pause] Và có một điểm tinh tế: thuật sư cổ đại thường mạnh vì họ đã quen với chiến tranh và cái chết. Người hiện đại phải thắng họ bằng sự sáng tạo, hiểu biết luật chơi và tinh thần đồng đội.

[pause] Cách này vừa ghi điểm, vừa bảo vệ người vô tội. [pause] Nhưng nó cũng nguy hiểm nhất, vì những thuật sư cổ đại thường mạnh hơn rất nhiều.

[pause] [chuckles] Kaku để ý: đây là cách mà các nhân vật chính chọn gần như trong mọi trận. Họ biến luật tàn nhẫn nhất, luật năm, thành cơ hội để làm điều đúng.

[pause] Cái giá: mỗi trận đấu với thuật sư cổ đại có thể là trận cuối cùng.

[pause] Cách phá lớn nhất là không phá luật, mà phá người tạo ra luật. Nếu Kenjaku bị ngăn lại, trò chơi sẽ mất lý do tồn tại.

[pause] Kaku nhớ lại video về Gojo: một thế giới dựa vào một người mạnh nhất thì rất mong manh. Arc này chính là lúc thế giới phải học cách chiến đấu khi không có người đó.

[pause] Và cũng có một mục tiêu song song: giải phóng Gojo khỏi phong ấn. Người mạnh nhất nếu trở lại sẽ thay đổi hoàn toàn cán cân.

[pause] Cái giá: cả hai mục tiêu đều cần thời gian, trong khi luật tám không cho ai thời gian. Mỗi ngày trôi qua là thêm người chơi bị cuốn vào.

[pause] Kaku dừng ở đây. Những gì xảy ra tiếp theo, bạn sẽ thấy ở phần sau của anime.
```

### c08 · Bảng luật và cách phá / Góc nhìn của Kaku: một trò chơi dạy người chơi viết luật

Khoảng 118 giây · cảnh s67–s76 · 1539 ký tự

**Gemini**

```text
Kaku gom lại thành một bảng. Luật một, hai, ba: không ai đứng ngoài. Cách phá: không có, chỉ có thể bước vào với mục tiêu rõ ràng.

<short pause> Luật bốn, năm: điểm là mạng người. Cách phá: săn đúng người, những kẻ đang gây hại. Cái giá: đối thủ mạnh hơn nhiều.

<short pause> Một dòng nhỏ Kaku viết thêm dưới bảng: mọi cách phá đều dùng luật của chính trò chơi. Không ai thoát ra bằng cách phớt lờ luật. Họ thoát ra bằng cách hiểu luật hơn người viết.

<short pause> Luật sáu, bảy: một trăm điểm đổi một luật. Cách phá: thêm luật cho phép rời trò chơi, chuyển điểm để dồn cho một người. Cái giá: vẫn phải chiến đấu và phải tin nhau.

<short pause> Luật tám: không được đứng yên. Cách phá lớn nhất: nhắm vào người viết luật, và đưa người mạnh nhất trở lại. Cái giá: thời gian không chờ ai.

<short pause> Nếu so với Trò chơi con mực, nơi người chơi chỉ có thể bỏ phiếu dừng trò chơi, thì Tử Diệt Hồi Du cho người chơi nhiều công cụ hơn, nhưng cũng đòi hỏi họ phải trả giá nhiều hơn.

<short pause> <laugh> Kaku phải thừa nhận: đọc bộ luật này giống như làm bài tập môn luật. <short pause> Nhưng đây là bài tập mà sai một điều khoản là mất mạng.

<short pause> Kaku thấy Tử Diệt Hồi Du là một trong những trò chơi sinh tử được thiết kế thông minh nhất trong anime. Không phải vì nó tàn nhẫn, mà vì nó cho phép người chơi sửa luật.

<short pause> Và chính điều đó biến các nhân vật chính từ nạn nhân thành người viết lại câu chuyện. Họ không thắng bằng cách giết nhiều hơn, mà bằng cách thay đổi những gì được coi là thắng.

<short pause> Nếu bạn có một trăm điểm, bạn sẽ thêm luật gì vào Tử Diệt Hồi Du? Nhớ luật bảy: không được quá lớn. Viết luật của bạn vào bình luận, Kaku sẽ chọn luật khôn ngoan nhất.
```

**ElevenLabs**

```text
Kaku gom lại thành một bảng. Luật một, hai, ba: không ai đứng ngoài. Cách phá: không có, chỉ có thể bước vào với mục tiêu rõ ràng.

[pause] Luật bốn, năm: điểm là mạng người. Cách phá: săn đúng người, những kẻ đang gây hại. Cái giá: đối thủ mạnh hơn nhiều.

[pause] Một dòng nhỏ Kaku viết thêm dưới bảng: mọi cách phá đều dùng luật của chính trò chơi. Không ai thoát ra bằng cách phớt lờ luật. Họ thoát ra bằng cách hiểu luật hơn người viết.

[pause] Luật sáu, bảy: một trăm điểm đổi một luật. Cách phá: thêm luật cho phép rời trò chơi, chuyển điểm để dồn cho một người. Cái giá: vẫn phải chiến đấu và phải tin nhau.

[pause] Luật tám: không được đứng yên. Cách phá lớn nhất: nhắm vào người viết luật, và đưa người mạnh nhất trở lại. Cái giá: thời gian không chờ ai.

[pause] Nếu so với Trò chơi con mực, nơi người chơi chỉ có thể bỏ phiếu dừng trò chơi, thì Tử Diệt Hồi Du cho người chơi nhiều công cụ hơn, nhưng cũng đòi hỏi họ phải trả giá nhiều hơn.

[pause] [chuckles] Kaku phải thừa nhận: đọc bộ luật này giống như làm bài tập môn luật. [pause] Nhưng đây là bài tập mà sai một điều khoản là mất mạng.

[pause] Kaku thấy Tử Diệt Hồi Du là một trong những trò chơi sinh tử được thiết kế thông minh nhất trong anime. Không phải vì nó tàn nhẫn, mà vì nó cho phép người chơi sửa luật.

[pause] Và chính điều đó biến các nhân vật chính từ nạn nhân thành người viết lại câu chuyện. Họ không thắng bằng cách giết nhiều hơn, mà bằng cách thay đổi những gì được coi là thắng.

[pause] [curious] Nếu bạn có một trăm điểm, bạn sẽ thêm luật gì vào Tử Diệt Hồi Du? Nhớ luật bảy: không được quá lớn. Viết luật của bạn vào bình luận, Kaku sẽ chọn luật khôn ngoan nhất.
```

### c09 · Kết

Khoảng 46 giây · cảnh s77–s80 · 592 ký tự

**Gemini**

```text
Và đó là một thông điệp rất đẹp của Jujutsu Kaisen: khi luật bất công, đừng chỉ tìm cách sống sót trong đó. Hãy tìm cách sửa nó.

<short pause> Tử Diệt Hồi Du bắt đầu như một trò chơi để người ta giết nhau. <short pause> Nhưng với những người như Itadori và Fushiguro, nó trở thành cuộc chiến để giành lại quyền viết luật.

<short pause> Video tiếp theo, Kaku đưa bạn vào một kỳ thi khác, cũng sinh tử nhưng vui hơn nhiều: nếu bạn dự kỳ thi sát thủ JCC của Sakamoto Days, bạn sẽ sống sót tới vòng nào?

<short pause> <laugh> Nếu bạn thích đọc luật như đọc hợp đồng cùng Kaku, hãy đăng ký kênh để không bỏ lỡ những bộ luật tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và đó là một thông điệp rất đẹp của Jujutsu Kaisen: khi luật bất công, đừng chỉ tìm cách sống sót trong đó. Hãy tìm cách sửa nó.

[pause] Tử Diệt Hồi Du bắt đầu như một trò chơi để người ta giết nhau. [pause] Nhưng với những người như Itadori và Fushiguro, nó trở thành cuộc chiến để giành lại quyền viết luật.

[pause] [curious] Video tiếp theo, Kaku đưa bạn vào một kỳ thi khác, cũng sinh tử nhưng vui hơn nhiều: nếu bạn dự kỳ thi sát thủ JCC của Sakamoto Days, bạn sẽ sống sót tới vòng nào?

[pause] [chuckles] Nếu bạn thích đọc luật như đọc hợp đồng cùng Kaku, hãy đăng ký kênh để không bỏ lỡ những bộ luật tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```
