# Bộ prompt · Kingdom: Tần Thủy Hoàng và Lý Tín ngoài đời thật là ai?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 77 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (77 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Câu chuyện này có thật hơn bạn nghĩ. Một cậu bé mồ côi, lớn lên như một người hầu, mơ trở thành đại tướng quâ…

```text
Wide 16:9 landscape cinematic frame. an ancient bamboo scroll partially unrolled on a dark wooden table, a single name brushed in ink highlighted by a beam of light, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Và vị vua trẻ mà cậu phò tá sau này sẽ trở thành một trong những người nổi tiếng nhất lịch sử Trung Hoa: Tần…

```text
Wide 16:9 landscape cinematic frame. an imposing ancient palace gate at dawn with rows of banners fluttering in the wind, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nói về spoiler: với Kingdom, spoiler lớn nhất đã có trong sách lịch sử từ hơn hai nghìn năm trước. Nước Tần s…

```text
Wide 16:9 landscape cinematic frame. a history textbook lying open next to a stack of manga volumes, a small spoiler warning card between them, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Câu hỏi hôm nay: trong Kingdom, bao nhiêu là thật, bao nhiêu là hư cấu? Doanh Chính và Lý Tín ngoài đời là ng…

```text
Wide 16:9 landscape cinematic frame. a large parchment divided into two columns, one side marked with a brush stroke and the other with a question mark, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Kaku nói trước một nguyên tắc: Kaku sẽ không vẽ chân dung người thật. Vì không ai biết chính xác họ trông thế…

```text
Wide 16:9 landscape cinematic frame. a museum display case with ancient bronze artifacts and a small placard, soft spotlight, medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở một cuốn sử thật, đặt cạnh Kingdom, và cuối video là bản đồ thật…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny reading glasses opening a large ancient bamboo scroll with great care. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Kingdom là gì?

Lời: Kingdom là manga của tác giả Hara Yasuhisa, đăng trên tạp chí Weekly Young Jump từ tháng một năm 2006. Tới th…

```text
Wide 16:9 landscape cinematic frame. a tall stack of thick manga volumes towering on a bookstore table with a small sign, close-up, warm store light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Truyện có anime nhiều mùa, mùa sáu phát từ tháng mười năm 2025, và cả loạt phim người đóng ở Nhật rất thành c…

```text
Wide 16:9 landscape cinematic frame. a movie theater marquee glowing at night with an empty ticket booth below, wide shot, warm neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Bối cảnh là thời Chiến Quốc ở Trung Hoa, khoảng thế kỷ thứ ba trước Công nguyên. Bảy nước lớn đánh nhau suốt…

```text
Wide 16:9 landscape cinematic frame. an old hand-drawn map of ancient China divided into seven colored regions, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Truyện theo hai nhân vật: Lý Tín, cậu bé muốn thành đại tướng, và Doanh Chính, vị vua trẻ nước Tần muốn chấm…

```text
Wide 16:9 landscape cinematic frame. two small silhouettes standing on a hill overlooking a vast plain, one holding a sword and one holding a scroll, wide shot, dramatic sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Thời Chiến Quốc thật

Lời: Thời Chiến Quốc thật kéo dài khoảng hai trăm năm mươi năm, từ thế kỷ thứ năm tới năm hai trăm hai mươi mốt tr…

```text
Wide 16:9 landscape cinematic frame. a long timeline scroll with many small crossed-sword marks spaced along it, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Bảy nước lớn là Tần, Triệu, Hàn, Ngụy, Sở, Yên và Tề. Tần ở phía tây, từng bị các nước khác xem là vùng biên,…

```text
Wide 16:9 landscape cinematic frame. a map of seven ancient states with the western region shaded darker and slightly isolated by mountains, parchment close-up, amber and red ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhưng Tần mạnh lên nhờ cải cách của Thương Ưởng khoảng một trăm năm trước thời Doanh Chính: luật lệ nghiêm kh…

```text
Wide 16:9 landscape cinematic frame. an ancient stone tablet engraved with columns of rules beside a bronze tally token, close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Chi tiết cuối cùng này rất quan trọng với Kingdom. Ở nước Tần thật, một người lính thường có thể thăng tiến n…

```text
Wide 16:9 landscape cinematic frame. a simple soldier's helmet placed on a step at the bottom of a tall staircase leading to a general's banner, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Kingdom không phát minh ra giấc mơ đổi đời bằng chiến công. Nó lấy từ chính luật lệ nước Tần.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at an old rulebook with a small helmet doodle on the margin. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Doanh Chính trong truyện và ngoài đời

Lời: Doanh Chính thật sinh năm hai trăm năm mươi chín trước Công nguyên ở Hàm Đan, kinh đô nước Triệu, nơi cha ông…

```text
Wide 16:9 landscape cinematic frame. an ancient walled city at dusk with narrow streets and a lone child's silhouette at a gate, wide shot, cold dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Thời đó, các nước thường gửi con cháu hoàng tộc sang nước khác làm con tin để bảo đảm hòa ước. Khi hai nước t…

```text
Wide 16:9 landscape cinematic frame. an ornate sealed treaty scroll lying beside a small child's shoe on a stone floor, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Kingdom khắc họa tuổi thơ khốn khổ của ông ở nước Triệu, bị người Triệu thù ghét. Phần này có gốc thật: ông l…

```text
Wide 16:9 landscape cinematic frame. a small child hiding in the shadow of a stone wall while hostile silhouettes pass by, medium shot, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Năm hai trăm bốn mươi bảy trước Công nguyên, Doanh Chính lên ngôi vua Tần khi mới khoảng mười ba tuổi. Quyền…

```text
Wide 16:9 landscape cinematic frame. an oversized throne in a vast hall with a small figure seated on it, a tall shadow standing beside the throne, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Lã Bất Vi vốn là một thương nhân giàu có. Ông đầu tư vào cha của Doanh Chính khi người cha còn là con tin, và…

```text
Wide 16:9 landscape cinematic frame. a merchant's abacus and a stack of ancient coins beside a small royal seal on a lacquered table, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Sử ký của Tư Mã Thiên còn chép một lời đồn: Lã Bất Vi mới là cha ruột của Doanh Chính. Nhiều nhà sử học hiện…

```text
Wide 16:9 landscape cinematic frame. an ancient scroll with a passage circled and a small question mark stamp beside it, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Năm hai trăm ba mươi tám trước Công nguyên, khi Doanh Chính làm lễ trưởng thành, Lao Ái, một kẻ thân cận của…

```text
Wide 16:9 landscape cinematic frame. a palace courtyard at night with torches and scattered banners after a clash, wide shot, dramatic firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Còn nhân vật người đóng thế giống hệt nhà vua ở đầu truyện, người bạn thân của Lý Tín, là hoàn toàn hư cấu. T…

```text
Wide 16:9 landscape cinematic frame. two identical silhouettes facing each other like a mirror reflection, one fading, symbolic close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Và lý tưởng thống nhất để chấm dứt chiến tranh, như Doanh Chính trong truyện thường nói, là cách tác giả diễn…

```text
Wide 16:9 landscape cinematic frame. a young ruler's silhouette standing on a palace balcony overlooking a war-torn land at sunset, back view, wide shot, somber golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Lý Tín trong truyện và ngoài đời

Lời: Giờ tới Lý Tín. Trong truyện, cậu là trẻ mồ côi chiến tranh, lớn lên làm người hầu, và luyện kiếm mỗi ngày vớ…

```text
Wide 16:9 landscape cinematic frame. a young boy swinging a wooden stick like a sword alone in a dusty village yard at dawn, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Ngoài đời, sử sách gần như không ghi gì về tuổi thơ của Lý Tín. Không có dòng nào nói ông là trẻ mồ côi hay n…

```text
Wide 16:9 landscape cinematic frame. a mostly empty bamboo scroll with only a few lines of ink near the end, parchment close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và chính khoảng trống này là món quà cho tác giả. Không có ghi chép thì có thể sáng tạo. Hara Yasuhisa đã cho…

```text
Wide 16:9 landscape cinematic frame. a blank page with a brush poised above it, a single drop of ink about to fall, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Lý Tín thật được sử sách nhắc tới như một vị tướng trẻ dũng mãnh. Ông từng dẫn quân truy đuổi thái tử Đan nướ…

```text
Wide 16:9 landscape cinematic frame. a small cavalry unit riding hard across a frozen river under a pale sky, wide shot, cold winter light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Rồi tới trận nổi tiếng nhất. Năm hai trăm hai mươi lăm trước Công nguyên, Doanh Chính hỏi các tướng cần bao n…

```text
Wide 16:9 landscape cinematic frame. a war council scene with generals' silhouettes around a large map table, one elderly figure raising six fingers, medium shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Lý Tín trẻ tuổi nói: hai mươi vạn là đủ. Nhà vua chọn Lý Tín.

```text
Wide 16:9 landscape cinematic frame. a younger silhouette at the map table raising two fingers confidently while the elderly figure turns away, medium shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và Hạng Yên là ai? Ông là ông nội của Hạng Vũ, Tây Sở Bá Vương, người mà người Việt biết qua câu chuyện Hán S…

```text
Wide 16:9 landscape cinematic frame. an old family tree scroll with a line connecting a general's name to a famous grandson's name marked with a small crown, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Kết quả: quân Sở do tướng Hạng Yên chỉ huy đánh úp quân Tần, và Lý Tín thua lớn. Nhà vua phải đích thân tới m…

```text
Wide 16:9 landscape cinematic frame. a battlefield at dusk with scattered banners and broken chariot wheels in tall grass, wide shot, somber red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy thú vị: Kingdom không giấu thất bại này. Truyện biết trước rằng nhân vật chính sẽ có một trận thua…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a history book in one wing and a manga volume in the other, looking back and forth nervously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Sau trận thua, Lý Tín vẫn tiếp tục cầm quân. Sử sách ghi ông cùng Vương Bí, con trai Vương Tiễn, tham gia nhữ…

```text
Wide 16:9 landscape cinematic frame. two riders side by side on a hill looking toward a distant coastline, back view, wide shot, bright morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và một chi tiết đẹp: theo Sử ký, danh tướng Lý Quảng của nhà Hán, người được gọi là Phi tướng quân, là hậu du…

```text
Wide 16:9 landscape cinematic frame. an ancient family genealogy scroll with a line of names connected by ink, a small bow and arrow drawn beside the last name, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Những người có thật khác

Lời: Kingdom có rất nhiều nhân vật có thật. Vương Tiễn là một trong những danh tướng lớn nhất nước Tần, người cuối…

```text
Wide 16:9 landscape cinematic frame. a massive army camp stretching to the horizon with countless tents and banners, wide shot, hazy morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Sử ký kể một chuyện rất đời: trước khi xuất quân, Vương Tiễn liên tục xin nhà vua ruộng đất, nhà cửa. Ông giả…

```text
Wide 16:9 landscape cinematic frame. a scroll listing fields and houses held beside a general's helmet, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Lý Mục, danh tướng nước Triệu, là đối thủ đáng sợ nhất của Tần, từng đánh bại quân Tần nhiều lần. Nhưng năm h…

```text
Wide 16:9 landscape cinematic frame. a lone general's banner lying fallen in the rain outside a city gate, close-up, somber grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kẻ gièm pha là Quách Khai, một cận thần nước Triệu đã nhận hối lộ của Tần. Không thắng được trên chiến trường…

```text
Wide 16:9 landscape cinematic frame. a small pouch of coins passed secretly between two hands in a dark palace corridor, extreme close-up, shadowy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kinh Kha, người mà người Việt biết qua rất nhiều phim, là thích khách do thái tử Đan nước Yên cử đi ám sát Do…

```text
Wide 16:9 landscape cinematic frame. a rolled map on a lacquered tray with the glint of a hidden blade at its core, extreme close-up, tense candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Dương Đoan Hòa là một cái tên có thật trong Sử ký, một tướng Tần từng đánh vào đất Triệu. Trong Kingdom, tác…

```text
Wide 16:9 landscape cinematic frame. a mountain fortress on a rocky peak with tribal banners, wide shot, dramatic misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Hoàn Nghĩ cũng là một tướng Tần có thật. Ông từng thắng nhiều trận, rồi thua đậm trước Lý Mục, và sau đó biến…

```text
Wide 16:9 landscape cinematic frame. a Qin war banner half buried in mud on an empty battlefield, close-up, grey overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Một số nhà sử học cho rằng ông có thể đã trốn sang nước Yên và đổi tên thành Phàn Ô Kỳ, người mà Kinh Kha man…

```text
Wide 16:9 landscape cinematic frame. a figure in a traveling cloak walking away from a border gate at dusk, a signpost pointing two directions, wide shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Mông Vũ và Mông Điềm cũng là cha con tướng Tần có thật. Mông Điềm sau này nổi tiếng vì đánh người Hung Nô ở p…

```text
Wide 16:9 landscape cinematic frame. a long earthen wall winding over northern hills under a pale sky, wide shot, cold windy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Những gì hoàn toàn hư cấu

Lời: Giờ tới phía hư cấu. Người đóng thế giống nhà vua, như Kaku đã nói, là hư cấu. Cô gái đeo mặt nạ trong nhóm c…

```text
Wide 16:9 landscape cinematic frame. a simple ceremonial bird-shaped mask lying on a stone step, close-up, soft mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Phần lớn đội quân riêng của Lý Tín và các đồng đội trong truyện là nhân vật sáng tạo. Sử sách thời đó chỉ ghi…

```text
Wide 16:9 landscape cinematic frame. a vast crowd of anonymous soldiers' silhouettes marching, only a few banners with names visible, wide shot, dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Những võ tướng một mình chém cả trăm người, những cú nhảy bay qua cả hàng quân, là phong cách manga. Chiến tr…

```text
Wide 16:9 landscape cinematic frame. an ancient crossbow and a bundle of bronze arrowheads laid on a wooden table beside a formation diagram, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku nhắc thêm: nước Tần thật có nỏ rất mạnh và các bộ phận vũ khí được chuẩn hóa để dễ thay thế. Đó mới là l…

```text
Wide 16:9 landscape cinematic frame. a row of identical bronze crossbow trigger mechanisms lined up neatly on a workbench, close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Và thời gian trong truyện được nén lại hoặc kéo dài theo nhịp kể chuyện. Có trận sử sách chỉ ghi một dòng, nh…

```text
Wide 16:9 landscape cinematic frame. a single line of brushed text on bamboo stretched out into a long illustrated scroll of battle scenes, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Tác giả thay đổi và vì sao

Lời: Vậy vì sao tác giả thay đổi? Kaku thấy có bốn lý do.

```text
Wide 16:9 landscape cinematic frame. a notebook page titled with four numbered empty lines, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Một: lấp khoảng trống. Nơi sử sách im lặng, như tuổi thơ Lý Tín, truyện có quyền sáng tạo mà không nói sai lị…

```text
Wide 16:9 landscape cinematic frame. a crumbling ancient wall with gaps being filled by fresh bricks of a different color, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Hai: tạo nhân vật để người đọc đồng cảm. Một cậu bé mồ côi đi lên dễ khiến ta cổ vũ hơn một vị tướng xuất thâ…

```text
Wide 16:9 landscape cinematic frame. a small figure climbing a tall rocky cliff toward a banner at the top, low-angle shot, inspiring light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Ba: diễn giải lại một nhân vật gây tranh cãi. Tần Thủy Hoàng thường bị nhớ tới như một bạo chúa. Kingdom cho…

```text
Wide 16:9 landscape cinematic frame. a two-sided bronze mirror, one side dark and cracked, the other polished and bright, close-up, dramatic split light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Bốn: phục vụ thể loại. Kingdom là manga hành động dành cho người lớn. Những trận đánh cần kịch tính, nên nó p…

```text
Wide 16:9 landscape cinematic frame. a dramatic ink splash of a charging horse on rice paper, dynamic close-up, energetic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Mẹo nhỏ của Kaku: nếu bạn tò mò, hãy đọc Kingdom cùng một bản tóm tắt thời Chiến Quốc. Mỗi khi truyện nhắc tớ…

```text
Wide 16:9 landscape cinematic frame. a manga volume and a slim history book open side by side on a desk, a pencil and sticky notes marking pages, close-up, cozy lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là cách làm truyện lịch sử rất khéo: giữ đúng các cột mốc lớn, và sáng tạo ở giữa. Người đọc bi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing small flags on a map at fixed points and drawing a winding path between them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Phần lịch sử truyện chưa tới

Lời: Năm hai trăm hai mươi mốt trước Công nguyên, nước Tần diệt nước Tề, nước cuối cùng. Doanh Chính thống nhất th…

```text
Wide 16:9 landscape cinematic frame. a vast unified map of ancient China with all seven regions merging into one color, parchment close-up, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Trước đó, Tần diệt sáu nước trong khoảng mười năm: Hàn, rồi Triệu, Ngụy, Sở, Yên, và cuối cùng là Tề. Kingdom…

```text
Wide 16:9 landscape cinematic frame. a map with six regions being crossed out one by one in red ink, each with a small date marker, parchment close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Ông chuẩn hóa chữ viết, tiền tệ, đo lường, và cả khoảng cách giữa hai bánh xe để xe đi được trên mọi con đườn…

```text
Wide 16:9 landscape cinematic frame. a flat lay of ancient round bronze coins with square holes, a bamboo measuring rod and a set of weights, overhead shot, warm museum light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nhưng ông cũng nổi tiếng vì những chính sách hà khắc: đốt sách, lao dịch nặng nề, và luật lệ tàn nhẫn.

```text
Wide 16:9 landscape cinematic frame. a pile of burning bamboo scrolls in a courtyard with smoke rising into a grey sky, wide shot, somber orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Năm hai trăm mười trước Công nguyên, ông mất trong một chuyến tuần du. Nhà Tần sụp đổ chỉ vài năm sau đó, tổn…

```text
Wide 16:9 landscape cinematic frame. an ornate carriage traveling along an empty road under a dark sky, wide shot, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Năm 1974, những người nông dân đào giếng gần Tây An tình cờ tìm thấy mảnh gốm. Đó là đội quân đất nung trong…

```text
Wide 16:9 landscape cinematic frame. rows of ancient terracotta soldier statues standing in an excavation pit, wide shot, soft museum light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Mỗi tượng có khuôn mặt hơi khác nhau. Kaku luôn tự hỏi: trong tám nghìn gương mặt đó, có ai là những người lí…

```text
Wide 16:9 landscape cinematic frame. extreme close-up of the weathered face of a terracotta statue, soft dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Bạo chúa hay minh quân?

Lời: Phần lớn những gì ta biết về Tần Thủy Hoàng đến từ Sử ký của Tư Mã Thiên, viết dưới thời nhà Hán, khoảng một…

```text
Wide 16:9 landscape cinematic frame. an ancient historian's writing desk with brushes, an ink stone and stacks of bamboo slips, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nhà Hán lên thay nhà Tần, nên có lý do để kể nhà Tần như một triều đại tàn bạo. Nhiều nhà sử học hiện đại đã…

```text
Wide 16:9 landscape cinematic frame. a balance scale with bamboo slips on one side and a bronze coin on the other, close-up, neutral light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Kingdom chọn kể câu chuyện của một Doanh Chính trẻ, trước khi thành hoàng đế. Nó không trả lời ông là bạo chú…

```text
Wide 16:9 landscape cinematic frame. a young ruler's silhouette standing at a fork in a road at dawn, one path bright and one path dark, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku cũng làm vậy. Bạn nghĩ sao: Tần Thủy Hoàng là bạo chúa hay minh quân? Hay cả hai? Viết vào bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up two small signs, one with a crown and one with a chain, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Góc nhìn từ Việt Nam

Lời: Có một chi tiết nối lịch sử này với Việt Nam. Sau khi thống nhất, nhà Tần đem quân xuống phương Nam, vùng mà…

```text
Wide 16:9 landscape cinematic frame. an old map showing armies' arrows moving south toward a lush green region with rivers and mountains, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Triệu Đà, người sau này lập nước Nam Việt, vốn là một viên tướng nhà Tần tham gia cuộc chinh phạt đó. Người V…

```text
Wide 16:9 landscape cinematic frame. a quiet southern river landscape with misty mountains and a small ancient fortress, wide shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nghĩa là thế giới của Kingdom không xa lạ như ta nghĩ. Nó là một phần câu chuyện lớn mà lịch sử Việt Nam cũng…

```text
Wide 16:9 landscape cinematic frame. two old maps laid over each other, one of ancient China and one of ancient Vietnam, their edges overlapping, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Bản đồ thật và hư cấu

Lời: Và đây là bản đồ thật và hư cấu trong một hình. Cột thật: Doanh Chính, Lã Bất Vi, loạn Lao Ái, Vương Tiễn, Lý…

```text
Wide 16:9 landscape cinematic frame. a two-column chart on parchment with the left column filled with small seal-stamp icons, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Cột có tên thật nhưng thay đổi: Dương Đoan Hòa thành nữ vương miền núi, tuổi thơ mồ côi của Lý Tín, và lý tưở…

```text
Wide 16:9 landscape cinematic frame. the middle of the chart with half-filled circle icons beside a few entries, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Cột hư cấu: người đóng thế, cô gái đeo mặt nạ, phần lớn đồng đội của Lý Tín, và những võ tướng một người địch…

```text
Wide 16:9 landscape cinematic frame. the right column of the chart with dotted circle icons, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Cột giả thuyết: Lã Bất Vi là cha ruột, và Hoàn Nghĩ là Phàn Ô Kỳ. Sử sách chưa trả lời, nên Kaku để chúng ở m…

```text
Wide 16:9 landscape cinematic frame. a small note pinned at the edge of the chart with two question marks, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Kết

Lời: Kingdom là câu chuyện về một cậu bé không có tên trong sử sách thời thơ ấu, nhưng có tên ở những trang quan t…

```text
Wide 16:9 landscape cinematic frame. a bamboo scroll with the blank early section now filled with delicate illustrations, leading into the historical text, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Video tiếp theo, Kaku mở một hồ sơ bí ẩn: Chainsaw Man, và câu hỏi vì sao cả thế giới ác quỷ lại sợ một con q…

```text
Wide 16:9 landscape cinematic frame. a magnifying glass lying on a case file with a small chainsaw doodle on the cover, close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video đặt truyện cạnh lịch sử thật, hãy đăng ký kênh. Lần sau bạn đọc Kingdom, bạn sẽ biế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the bamboo scroll and bowing politely. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Kingdom là gì?

Khoảng 116 giây · cảnh s01–s10 · 1513 ký tự

**Gemini**

```text
Câu chuyện này có thật hơn bạn nghĩ. Một cậu bé mồ côi, lớn lên như một người hầu, mơ trở thành đại tướng quân thiên hạ. Nghe như truyện tranh. <short pause> Nhưng tên của cậu thật sự có trong sử sách.

<short pause> Và vị vua trẻ mà cậu phò tá sau này sẽ trở thành một trong những người nổi tiếng nhất lịch sử Trung Hoa: Tần Thủy Hoàng.

<short pause> Nói về spoiler: với Kingdom, spoiler lớn nhất đã có trong sách lịch sử từ hơn hai nghìn năm trước. Nước Tần sẽ thống nhất thiên hạ. <short pause> Nhưng Kaku sẽ không nói trước các trận chưa lên anime.

<short pause> Câu hỏi hôm nay: trong Kingdom, bao nhiêu là thật, bao nhiêu là hư cấu? Doanh Chính và Lý Tín ngoài đời là người thế nào? Và tác giả đã thay đổi những gì, vì sao?

<short pause> Kaku nói trước một nguyên tắc: Kaku sẽ không vẽ chân dung người thật. Vì không ai biết chính xác họ trông thế nào. Kaku dùng cổ vật, bản đồ và những bóng người.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở một cuốn sử thật, đặt cạnh Kingdom, và cuối video là bản đồ thật và hư cấu trong một hình.

<short pause> Kingdom là manga của tác giả Hara Yasuhisa, đăng trên tạp chí Weekly Young Jump từ tháng một năm 2006. Tới tháng một năm 2026, truyện đã vượt một trăm hai mươi triệu bản.

<short pause> Truyện có anime nhiều mùa, mùa sáu phát từ tháng mười năm 2025, và cả loạt phim người đóng ở Nhật rất thành công.

<short pause> Bối cảnh là thời Chiến Quốc ở Trung Hoa, khoảng thế kỷ thứ ba trước Công nguyên. Bảy nước lớn đánh nhau suốt hàng trăm năm.

<short pause> Truyện theo hai nhân vật: Lý Tín, cậu bé muốn thành đại tướng, và Doanh Chính, vị vua trẻ nước Tần muốn chấm dứt chiến tranh bằng cách thống nhất cả bảy nước.
```

**ElevenLabs**

```text
Câu chuyện này có thật hơn bạn nghĩ. Một cậu bé mồ côi, lớn lên như một người hầu, mơ trở thành đại tướng quân thiên hạ. Nghe như truyện tranh. [pause] Nhưng tên của cậu thật sự có trong sử sách.

[pause] Và vị vua trẻ mà cậu phò tá sau này sẽ trở thành một trong những người nổi tiếng nhất lịch sử Trung Hoa: Tần Thủy Hoàng.

[pause] Nói về spoiler: với Kingdom, spoiler lớn nhất đã có trong sách lịch sử từ hơn hai nghìn năm trước. Nước Tần sẽ thống nhất thiên hạ. [pause] Nhưng Kaku sẽ không nói trước các trận chưa lên anime.

[pause] [curious] Câu hỏi hôm nay: trong Kingdom, bao nhiêu là thật, bao nhiêu là hư cấu? Doanh Chính và Lý Tín ngoài đời là người thế nào? Và tác giả đã thay đổi những gì, vì sao?

[pause] Kaku nói trước một nguyên tắc: Kaku sẽ không vẽ chân dung người thật. Vì không ai biết chính xác họ trông thế nào. Kaku dùng cổ vật, bản đồ và những bóng người.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở một cuốn sử thật, đặt cạnh Kingdom, và cuối video là bản đồ thật và hư cấu trong một hình.

[pause] Kingdom là manga của tác giả Hara Yasuhisa, đăng trên tạp chí Weekly Young Jump từ tháng một năm 2006. Tới tháng một năm 2026, truyện đã vượt một trăm hai mươi triệu bản.

[pause] Truyện có anime nhiều mùa, mùa sáu phát từ tháng mười năm 2025, và cả loạt phim người đóng ở Nhật rất thành công.

[pause] Bối cảnh là thời Chiến Quốc ở Trung Hoa, khoảng thế kỷ thứ ba trước Công nguyên. Bảy nước lớn đánh nhau suốt hàng trăm năm.

[pause] Truyện theo hai nhân vật: Lý Tín, cậu bé muốn thành đại tướng, và Doanh Chính, vị vua trẻ nước Tần muốn chấm dứt chiến tranh bằng cách thống nhất cả bảy nước.
```

### c02 · Thời Chiến Quốc thật

Khoảng 56 giây · cảnh s11–s15 · 722 ký tự

**Gemini**

```text
Thời Chiến Quốc thật kéo dài khoảng hai trăm năm mươi năm, từ thế kỷ thứ năm tới năm hai trăm hai mươi mốt trước Công nguyên.

<short pause> Bảy nước lớn là Tần, Triệu, Hàn, Ngụy, Sở, Yên và Tề. Tần ở phía tây, từng bị các nước khác xem là vùng biên, nửa văn minh.

<short pause> Nhưng Tần mạnh lên nhờ cải cách của Thương Ưởng khoảng một trăm năm trước thời Doanh Chính: luật lệ nghiêm khắc, thưởng phạt rõ ràng, và lên chức theo chiến công chứ không theo dòng dõi.

<short pause> Chi tiết cuối cùng này rất quan trọng với Kingdom. Ở nước Tần thật, một người lính thường có thể thăng tiến nhờ chiến công. Đó là nền móng để một cậu bé như Lý Tín có thể mơ làm tướng.

<short pause> <laugh> Kaku để ý: Kingdom không phát minh ra giấc mơ đổi đời bằng chiến công. Nó lấy từ chính luật lệ nước Tần.
```

**ElevenLabs**

```text
Thời Chiến Quốc thật kéo dài khoảng hai trăm năm mươi năm, từ thế kỷ thứ năm tới năm hai trăm hai mươi mốt trước Công nguyên.

[pause] Bảy nước lớn là Tần, Triệu, Hàn, Ngụy, Sở, Yên và Tề. Tần ở phía tây, từng bị các nước khác xem là vùng biên, nửa văn minh.

[pause] Nhưng Tần mạnh lên nhờ cải cách của Thương Ưởng khoảng một trăm năm trước thời Doanh Chính: luật lệ nghiêm khắc, thưởng phạt rõ ràng, và lên chức theo chiến công chứ không theo dòng dõi.

[pause] Chi tiết cuối cùng này rất quan trọng với Kingdom. Ở nước Tần thật, một người lính thường có thể thăng tiến nhờ chiến công. Đó là nền móng để một cậu bé như Lý Tín có thể mơ làm tướng.

[pause] [chuckles] Kaku để ý: Kingdom không phát minh ra giấc mơ đổi đời bằng chiến công. Nó lấy từ chính luật lệ nước Tần.
```

### c03 · Doanh Chính trong truyện và ngoài đời

Khoảng 114 giây · cảnh s16–s24 · 1476 ký tự

**Gemini**

```text
Doanh Chính thật sinh năm hai trăm năm mươi chín trước Công nguyên ở Hàm Đan, kinh đô nước Triệu, nơi cha ông đang làm con tin.

<short pause> Thời đó, các nước thường gửi con cháu hoàng tộc sang nước khác làm con tin để bảo đảm hòa ước. Khi hai nước trở mặt, con tin là người đầu tiên gặp nguy hiểm.

<short pause> Kingdom khắc họa tuổi thơ khốn khổ của ông ở nước Triệu, bị người Triệu thù ghét. Phần này có gốc thật: ông lớn lên ở đất địch, trong thân phận con của con tin.

<short pause> Năm hai trăm bốn mươi bảy trước Công nguyên, Doanh Chính lên ngôi vua Tần khi mới khoảng mười ba tuổi. Quyền lực thật lúc đó nằm trong tay thừa tướng Lã Bất Vi.

<short pause> Lã Bất Vi vốn là một thương nhân giàu có. Ông đầu tư vào cha của Doanh Chính khi người cha còn là con tin, và giúp ông ta lên ngôi. Một thương vụ đổi lấy cả một đất nước.

<short pause> Sử ký của Tư Mã Thiên còn chép một lời đồn: Lã Bất Vi mới là cha ruột của Doanh Chính. Nhiều nhà sử học hiện đại nghi ngờ lời đồn này. Kaku ghi nó là lời đồn, không phải sự thật.

<short pause> Năm hai trăm ba mươi tám trước Công nguyên, khi Doanh Chính làm lễ trưởng thành, Lao Ái, một kẻ thân cận của thái hậu, nổi loạn. Doanh Chính dẹp loạn, rồi dần lấy lại quyền từ Lã Bất Vi.

<short pause> Còn nhân vật người đóng thế giống hệt nhà vua ở đầu truyện, người bạn thân của Lý Tín, là hoàn toàn hư cấu. Tác giả cần một cách để hai nhân vật chính gặp nhau.

<short pause> Và lý tưởng thống nhất để chấm dứt chiến tranh, như Doanh Chính trong truyện thường nói, là cách tác giả diễn giải. Sử sách ghi lại việc ông làm, nhưng không ghi lại ông nghĩ gì.
```

**ElevenLabs**

```text
Doanh Chính thật sinh năm hai trăm năm mươi chín trước Công nguyên ở Hàm Đan, kinh đô nước Triệu, nơi cha ông đang làm con tin.

[pause] Thời đó, các nước thường gửi con cháu hoàng tộc sang nước khác làm con tin để bảo đảm hòa ước. Khi hai nước trở mặt, con tin là người đầu tiên gặp nguy hiểm.

[pause] Kingdom khắc họa tuổi thơ khốn khổ của ông ở nước Triệu, bị người Triệu thù ghét. Phần này có gốc thật: ông lớn lên ở đất địch, trong thân phận con của con tin.

[pause] Năm hai trăm bốn mươi bảy trước Công nguyên, Doanh Chính lên ngôi vua Tần khi mới khoảng mười ba tuổi. Quyền lực thật lúc đó nằm trong tay thừa tướng Lã Bất Vi.

[pause] Lã Bất Vi vốn là một thương nhân giàu có. Ông đầu tư vào cha của Doanh Chính khi người cha còn là con tin, và giúp ông ta lên ngôi. Một thương vụ đổi lấy cả một đất nước.

[pause] Sử ký của Tư Mã Thiên còn chép một lời đồn: Lã Bất Vi mới là cha ruột của Doanh Chính. Nhiều nhà sử học hiện đại nghi ngờ lời đồn này. Kaku ghi nó là lời đồn, không phải sự thật.

[pause] Năm hai trăm ba mươi tám trước Công nguyên, khi Doanh Chính làm lễ trưởng thành, Lao Ái, một kẻ thân cận của thái hậu, nổi loạn. Doanh Chính dẹp loạn, rồi dần lấy lại quyền từ Lã Bất Vi.

[pause] Còn nhân vật người đóng thế giống hệt nhà vua ở đầu truyện, người bạn thân của Lý Tín, là hoàn toàn hư cấu. Tác giả cần một cách để hai nhân vật chính gặp nhau.

[pause] Và lý tưởng thống nhất để chấm dứt chiến tranh, như Doanh Chính trong truyện thường nói, là cách tác giả diễn giải. Sử sách ghi lại việc ông làm, nhưng không ghi lại ông nghĩ gì.
```

### c04 · Lý Tín trong truyện và ngoài đời

Khoảng 134 giây · cảnh s25–s35 · 1739 ký tự

**Gemini**

```text
Giờ tới Lý Tín. Trong truyện, cậu là trẻ mồ côi chiến tranh, lớn lên làm người hầu, và luyện kiếm mỗi ngày với giấc mơ thành đại tướng quân thiên hạ.

<short pause> Ngoài đời, sử sách gần như không ghi gì về tuổi thơ của Lý Tín. Không có dòng nào nói ông là trẻ mồ côi hay người hầu. Ông xuất hiện trong sử khi đã là một vị tướng.

<short pause> Và chính khoảng trống này là món quà cho tác giả. Không có ghi chép thì có thể sáng tạo. Hara Yasuhisa đã cho Lý Tín một câu chuyện đi lên từ con số không.

<short pause> Lý Tín thật được sử sách nhắc tới như một vị tướng trẻ dũng mãnh. Ông từng dẫn quân truy đuổi thái tử Đan nước Yên, người đứng sau vụ ám sát Doanh Chính.

<short pause> Rồi tới trận nổi tiếng nhất. Năm hai trăm hai mươi lăm trước Công nguyên, Doanh Chính hỏi các tướng cần bao nhiêu quân để đánh nước Sở. Lão tướng Vương Tiễn nói sáu mươi vạn.

<short pause> Lý Tín trẻ tuổi nói: hai mươi vạn là đủ. Nhà vua chọn Lý Tín.

<short pause> Và Hạng Yên là ai? Ông là ông nội của Hạng Vũ, Tây Sở Bá Vương, người mà người Việt biết qua câu chuyện Hán Sở tranh hùng. Người đánh bại Lý Tín là ông nội của đối thủ lớn nhất của nhà Hán sau này.

<short pause> Kết quả: quân Sở do tướng Hạng Yên chỉ huy đánh úp quân Tần, và Lý Tín thua lớn. Nhà vua phải đích thân tới mời Vương Tiễn trở lại cầm quân.

<short pause> <laugh> Kaku thấy thú vị: Kingdom không giấu thất bại này. Truyện biết trước rằng nhân vật chính sẽ có một trận thua lớn trong sử sách, và cả người đọc Nhật lẫn Trung đều chờ xem tác giả xử lý thế nào.

<short pause> Sau trận thua, Lý Tín vẫn tiếp tục cầm quân. Sử sách ghi ông cùng Vương Bí, con trai Vương Tiễn, tham gia những chiến dịch cuối cùng của quá trình thống nhất.

<short pause> Và một chi tiết đẹp: theo Sử ký, danh tướng Lý Quảng của nhà Hán, người được gọi là Phi tướng quân, là hậu duệ bốn đời của Lý Tín. Giấc mơ đại tướng quân có lẽ đã được truyền lại trong gia đình.
```

**ElevenLabs**

```text
Giờ tới Lý Tín. Trong truyện, cậu là trẻ mồ côi chiến tranh, lớn lên làm người hầu, và luyện kiếm mỗi ngày với giấc mơ thành đại tướng quân thiên hạ.

[pause] Ngoài đời, sử sách gần như không ghi gì về tuổi thơ của Lý Tín. Không có dòng nào nói ông là trẻ mồ côi hay người hầu. Ông xuất hiện trong sử khi đã là một vị tướng.

[pause] Và chính khoảng trống này là món quà cho tác giả. Không có ghi chép thì có thể sáng tạo. Hara Yasuhisa đã cho Lý Tín một câu chuyện đi lên từ con số không.

[pause] Lý Tín thật được sử sách nhắc tới như một vị tướng trẻ dũng mãnh. Ông từng dẫn quân truy đuổi thái tử Đan nước Yên, người đứng sau vụ ám sát Doanh Chính.

[pause] Rồi tới trận nổi tiếng nhất. Năm hai trăm hai mươi lăm trước Công nguyên, Doanh Chính hỏi các tướng cần bao nhiêu quân để đánh nước Sở. Lão tướng Vương Tiễn nói sáu mươi vạn.

[pause] Lý Tín trẻ tuổi nói: hai mươi vạn là đủ. Nhà vua chọn Lý Tín.

[pause] [curious] Và Hạng Yên là ai? Ông là ông nội của Hạng Vũ, Tây Sở Bá Vương, người mà người Việt biết qua câu chuyện Hán Sở tranh hùng. Người đánh bại Lý Tín là ông nội của đối thủ lớn nhất của nhà Hán sau này.

[pause] Kết quả: quân Sở do tướng Hạng Yên chỉ huy đánh úp quân Tần, và Lý Tín thua lớn. Nhà vua phải đích thân tới mời Vương Tiễn trở lại cầm quân.

[pause] [chuckles] Kaku thấy thú vị: Kingdom không giấu thất bại này. Truyện biết trước rằng nhân vật chính sẽ có một trận thua lớn trong sử sách, và cả người đọc Nhật lẫn Trung đều chờ xem tác giả xử lý thế nào.

[pause] Sau trận thua, Lý Tín vẫn tiếp tục cầm quân. Sử sách ghi ông cùng Vương Bí, con trai Vương Tiễn, tham gia những chiến dịch cuối cùng của quá trình thống nhất.

[pause] Và một chi tiết đẹp: theo Sử ký, danh tướng Lý Quảng của nhà Hán, người được gọi là Phi tướng quân, là hậu duệ bốn đời của Lý Tín. Giấc mơ đại tướng quân có lẽ đã được truyền lại trong gia đình.
```

### c05 · Những người có thật khác

Khoảng 119 giây · cảnh s36–s44 · 1547 ký tự

**Gemini**

```text
Kingdom có rất nhiều nhân vật có thật. Vương Tiễn là một trong những danh tướng lớn nhất nước Tần, người cuối cùng chinh phục nước Sở với sáu mươi vạn quân như ông đã nói.

<short pause> Sử ký kể một chuyện rất đời: trước khi xuất quân, Vương Tiễn liên tục xin nhà vua ruộng đất, nhà cửa. Ông giải thích: để nhà vua yên tâm rằng ông chỉ ham của cải, không ham quyền.

<short pause> Lý Mục, danh tướng nước Triệu, là đối thủ đáng sợ nhất của Tần, từng đánh bại quân Tần nhiều lần. <short pause> Nhưng năm hai trăm hai mươi chín trước Công nguyên, ông bị gièm pha là muốn làm phản và bị xử tử.

<short pause> Kẻ gièm pha là Quách Khai, một cận thần nước Triệu đã nhận hối lộ của Tần. Không thắng được trên chiến trường, Tần thắng bằng lời nói trong triều đình địch.

<short pause> Kinh Kha, người mà người Việt biết qua rất nhiều phim, là thích khách do thái tử Đan nước Yên cử đi ám sát Doanh Chính năm hai trăm hai mươi bảy trước Công nguyên, với con dao giấu trong một tấm bản đồ.

<short pause> Dương Đoan Hòa là một cái tên có thật trong Sử ký, một tướng Tần từng đánh vào đất Triệu. Trong Kingdom, tác giả biến nhân vật này thành nữ vương của các bộ tộc miền núi.

<short pause> Hoàn Nghĩ cũng là một tướng Tần có thật. Ông từng thắng nhiều trận, rồi thua đậm trước Lý Mục, và sau đó biến mất khỏi sử sách nước Tần.

<short pause> Một số nhà sử học cho rằng ông có thể đã trốn sang nước Yên và đổi tên thành Phàn Ô Kỳ, người mà Kinh Kha mang đầu tới gặp Doanh Chính để được tiếp kiến. Đây là giả thuyết, chưa có kết luận.

<short pause> Mông Vũ và Mông Điềm cũng là cha con tướng Tần có thật. Mông Điềm sau này nổi tiếng vì đánh người Hung Nô ở phương Bắc và nối các đoạn trường thành.
```

**ElevenLabs**

```text
Kingdom có rất nhiều nhân vật có thật. Vương Tiễn là một trong những danh tướng lớn nhất nước Tần, người cuối cùng chinh phục nước Sở với sáu mươi vạn quân như ông đã nói.

[pause] Sử ký kể một chuyện rất đời: trước khi xuất quân, Vương Tiễn liên tục xin nhà vua ruộng đất, nhà cửa. Ông giải thích: để nhà vua yên tâm rằng ông chỉ ham của cải, không ham quyền.

[pause] Lý Mục, danh tướng nước Triệu, là đối thủ đáng sợ nhất của Tần, từng đánh bại quân Tần nhiều lần. [pause] Nhưng năm hai trăm hai mươi chín trước Công nguyên, ông bị gièm pha là muốn làm phản và bị xử tử.

[pause] Kẻ gièm pha là Quách Khai, một cận thần nước Triệu đã nhận hối lộ của Tần. Không thắng được trên chiến trường, Tần thắng bằng lời nói trong triều đình địch.

[pause] Kinh Kha, người mà người Việt biết qua rất nhiều phim, là thích khách do thái tử Đan nước Yên cử đi ám sát Doanh Chính năm hai trăm hai mươi bảy trước Công nguyên, với con dao giấu trong một tấm bản đồ.

[pause] Dương Đoan Hòa là một cái tên có thật trong Sử ký, một tướng Tần từng đánh vào đất Triệu. Trong Kingdom, tác giả biến nhân vật này thành nữ vương của các bộ tộc miền núi.

[pause] Hoàn Nghĩ cũng là một tướng Tần có thật. Ông từng thắng nhiều trận, rồi thua đậm trước Lý Mục, và sau đó biến mất khỏi sử sách nước Tần.

[pause] Một số nhà sử học cho rằng ông có thể đã trốn sang nước Yên và đổi tên thành Phàn Ô Kỳ, người mà Kinh Kha mang đầu tới gặp Doanh Chính để được tiếp kiến. Đây là giả thuyết, chưa có kết luận.

[pause] Mông Vũ và Mông Điềm cũng là cha con tướng Tần có thật. Mông Điềm sau này nổi tiếng vì đánh người Hung Nô ở phương Bắc và nối các đoạn trường thành.
```

### c06 · Những gì hoàn toàn hư cấu / Tác giả thay đổi và vì sao

Khoảng 132 giây · cảnh s45–s56 · 1717 ký tự

**Gemini**

```text
Giờ tới phía hư cấu. Người đóng thế giống nhà vua, như Kaku đã nói, là hư cấu. Cô gái đeo mặt nạ trong nhóm của Lý Tín cũng không có trong sử.

<short pause> Phần lớn đội quân riêng của Lý Tín và các đồng đội trong truyện là nhân vật sáng tạo. Sử sách thời đó chỉ ghi tên các tướng lớn, gần như không ghi tên lính.

<short pause> Những võ tướng một mình chém cả trăm người, những cú nhảy bay qua cả hàng quân, là phong cách manga. Chiến tranh thời đó chủ yếu dựa vào đội hình, cung nỏ và hậu cần.

<short pause> Kaku nhắc thêm: nước Tần thật có nỏ rất mạnh và các bộ phận vũ khí được chuẩn hóa để dễ thay thế. Đó mới là lợi thế thật, dù trên trang truyện không hấp dẫn bằng một nhát kiếm.

<short pause> Và thời gian trong truyện được nén lại hoặc kéo dài theo nhịp kể chuyện. Có trận sử sách chỉ ghi một dòng, nhưng truyện dành cả chục tập.

<short pause> Vậy vì sao tác giả thay đổi? Kaku thấy có bốn lý do.

<short pause> Một: lấp khoảng trống. Nơi sử sách im lặng, như tuổi thơ Lý Tín, truyện có quyền sáng tạo mà không nói sai lịch sử.

<short pause> Hai: tạo nhân vật để người đọc đồng cảm. Một cậu bé mồ côi đi lên dễ khiến ta cổ vũ hơn một vị tướng xuất thân quý tộc.

<short pause> Ba: diễn giải lại một nhân vật gây tranh cãi. Tần Thủy Hoàng thường bị nhớ tới như một bạo chúa. Kingdom cho ông một lý tưởng, để người đọc tự hỏi: liệu ông có đáng bị nhớ như vậy?

<short pause> Bốn: phục vụ thể loại. Kingdom là manga hành động dành cho người lớn. Những trận đánh cần kịch tính, nên nó phóng đại sức mạnh cá nhân.

<short pause> Mẹo nhỏ của Kaku: nếu bạn tò mò, hãy đọc Kingdom cùng một bản tóm tắt thời Chiến Quốc. Mỗi khi truyện nhắc tới một cái tên, bạn tra thử xem người đó có thật không. Rất nhiều bất ngờ đang chờ.

<short pause> <laugh> Kaku nghĩ đây là cách làm truyện lịch sử rất khéo: giữ đúng các cột mốc lớn, và sáng tạo ở giữa. Người đọc biết đích đến, nhưng không biết đường đi.
```

**ElevenLabs**

```text
Giờ tới phía hư cấu. Người đóng thế giống nhà vua, như Kaku đã nói, là hư cấu. Cô gái đeo mặt nạ trong nhóm của Lý Tín cũng không có trong sử.

[pause] Phần lớn đội quân riêng của Lý Tín và các đồng đội trong truyện là nhân vật sáng tạo. Sử sách thời đó chỉ ghi tên các tướng lớn, gần như không ghi tên lính.

[pause] Những võ tướng một mình chém cả trăm người, những cú nhảy bay qua cả hàng quân, là phong cách manga. Chiến tranh thời đó chủ yếu dựa vào đội hình, cung nỏ và hậu cần.

[pause] Kaku nhắc thêm: nước Tần thật có nỏ rất mạnh và các bộ phận vũ khí được chuẩn hóa để dễ thay thế. Đó mới là lợi thế thật, dù trên trang truyện không hấp dẫn bằng một nhát kiếm.

[pause] Và thời gian trong truyện được nén lại hoặc kéo dài theo nhịp kể chuyện. Có trận sử sách chỉ ghi một dòng, nhưng truyện dành cả chục tập.

[pause] [curious] Vậy vì sao tác giả thay đổi? Kaku thấy có bốn lý do.

[pause] Một: lấp khoảng trống. Nơi sử sách im lặng, như tuổi thơ Lý Tín, truyện có quyền sáng tạo mà không nói sai lịch sử.

[pause] Hai: tạo nhân vật để người đọc đồng cảm. Một cậu bé mồ côi đi lên dễ khiến ta cổ vũ hơn một vị tướng xuất thân quý tộc.

[pause] Ba: diễn giải lại một nhân vật gây tranh cãi. Tần Thủy Hoàng thường bị nhớ tới như một bạo chúa. Kingdom cho ông một lý tưởng, để người đọc tự hỏi: liệu ông có đáng bị nhớ như vậy?

[pause] Bốn: phục vụ thể loại. Kingdom là manga hành động dành cho người lớn. Những trận đánh cần kịch tính, nên nó phóng đại sức mạnh cá nhân.

[pause] Mẹo nhỏ của Kaku: nếu bạn tò mò, hãy đọc Kingdom cùng một bản tóm tắt thời Chiến Quốc. Mỗi khi truyện nhắc tới một cái tên, bạn tra thử xem người đó có thật không. Rất nhiều bất ngờ đang chờ.

[pause] [chuckles] Kaku nghĩ đây là cách làm truyện lịch sử rất khéo: giữ đúng các cột mốc lớn, và sáng tạo ở giữa. Người đọc biết đích đến, nhưng không biết đường đi.
```

### c07 · Phần lịch sử truyện chưa tới / Bạo chúa hay minh quân?

Khoảng 127 giây · cảnh s57–s67 · 1645 ký tự

**Gemini**

```text
Năm hai trăm hai mươi mốt trước Công nguyên, nước Tần diệt nước Tề, nước cuối cùng. Doanh Chính thống nhất thiên hạ và tự xưng là Thủy Hoàng Đế, hoàng đế đầu tiên.

<short pause> Trước đó, Tần diệt sáu nước trong khoảng mười năm: Hàn, rồi Triệu, Ngụy, Sở, Yên, và cuối cùng là Tề. Kingdom hiện vẫn đang kể những năm đầu của cuộc chinh phạt đó.

<short pause> Ông chuẩn hóa chữ viết, tiền tệ, đo lường, và cả khoảng cách giữa hai bánh xe để xe đi được trên mọi con đường. Những cải cách đó ảnh hưởng tới Trung Hoa suốt hai nghìn năm.

<short pause> Nhưng ông cũng nổi tiếng vì những chính sách hà khắc: đốt sách, lao dịch nặng nề, và luật lệ tàn nhẫn.

<short pause> Năm hai trăm mười trước Công nguyên, ông mất trong một chuyến tuần du. Nhà Tần sụp đổ chỉ vài năm sau đó, tổng cộng tồn tại khoảng mười lăm năm.

<short pause> Năm 1974, những người nông dân đào giếng gần Tây An tình cờ tìm thấy mảnh gốm. Đó là đội quân đất nung trong khu lăng mộ của ông, với hơn tám nghìn tượng lính theo ước tính.

<short pause> Mỗi tượng có khuôn mặt hơi khác nhau. Kaku luôn tự hỏi: trong tám nghìn gương mặt đó, có ai là những người lính vô danh mà sử sách không ghi tên không?

<short pause> Phần lớn những gì ta biết về Tần Thủy Hoàng đến từ Sử ký của Tư Mã Thiên, viết dưới thời nhà Hán, khoảng một thế kỷ sau khi nhà Tần sụp đổ.

<short pause> Nhà Hán lên thay nhà Tần, nên có lý do để kể nhà Tần như một triều đại tàn bạo. Nhiều nhà sử học hiện đại đã đánh giá lại, công nhận cả những đóng góp lẫn tội ác của ông.

<short pause> Kingdom chọn kể câu chuyện của một Doanh Chính trẻ, trước khi thành hoàng đế. Nó không trả lời ông là bạo chúa hay minh quân. Nó để người đọc tự quyết định.

<short pause> <laugh> Kaku cũng làm vậy. Bạn nghĩ sao: Tần Thủy Hoàng là bạo chúa hay minh quân? Hay cả hai? Viết vào bình luận nhé.
```

**ElevenLabs**

```text
Năm hai trăm hai mươi mốt trước Công nguyên, nước Tần diệt nước Tề, nước cuối cùng. Doanh Chính thống nhất thiên hạ và tự xưng là Thủy Hoàng Đế, hoàng đế đầu tiên.

[pause] Trước đó, Tần diệt sáu nước trong khoảng mười năm: Hàn, rồi Triệu, Ngụy, Sở, Yên, và cuối cùng là Tề. Kingdom hiện vẫn đang kể những năm đầu của cuộc chinh phạt đó.

[pause] Ông chuẩn hóa chữ viết, tiền tệ, đo lường, và cả khoảng cách giữa hai bánh xe để xe đi được trên mọi con đường. Những cải cách đó ảnh hưởng tới Trung Hoa suốt hai nghìn năm.

[pause] Nhưng ông cũng nổi tiếng vì những chính sách hà khắc: đốt sách, lao dịch nặng nề, và luật lệ tàn nhẫn.

[pause] Năm hai trăm mười trước Công nguyên, ông mất trong một chuyến tuần du. Nhà Tần sụp đổ chỉ vài năm sau đó, tổng cộng tồn tại khoảng mười lăm năm.

[pause] Năm 1974, những người nông dân đào giếng gần Tây An tình cờ tìm thấy mảnh gốm. Đó là đội quân đất nung trong khu lăng mộ của ông, với hơn tám nghìn tượng lính theo ước tính.

[pause] Mỗi tượng có khuôn mặt hơi khác nhau. [curious] Kaku luôn tự hỏi: trong tám nghìn gương mặt đó, có ai là những người lính vô danh mà sử sách không ghi tên không?

[pause] Phần lớn những gì ta biết về Tần Thủy Hoàng đến từ Sử ký của Tư Mã Thiên, viết dưới thời nhà Hán, khoảng một thế kỷ sau khi nhà Tần sụp đổ.

[pause] Nhà Hán lên thay nhà Tần, nên có lý do để kể nhà Tần như một triều đại tàn bạo. Nhiều nhà sử học hiện đại đã đánh giá lại, công nhận cả những đóng góp lẫn tội ác của ông.

[pause] Kingdom chọn kể câu chuyện của một Doanh Chính trẻ, trước khi thành hoàng đế. Nó không trả lời ông là bạo chúa hay minh quân. Nó để người đọc tự quyết định.

[pause] [chuckles] Kaku cũng làm vậy. Bạn nghĩ sao: Tần Thủy Hoàng là bạo chúa hay minh quân? Hay cả hai? Viết vào bình luận nhé.
```

### c08 · Góc nhìn từ Việt Nam / Bản đồ thật và hư cấu / Kết

Khoảng 112 giây · cảnh s68–s77 · 1458 ký tự

**Gemini**

```text
Có một chi tiết nối lịch sử này với Việt Nam. Sau khi thống nhất, nhà Tần đem quân xuống phương Nam, vùng mà sử sách gọi là đất Bách Việt.

<short pause> Triệu Đà, người sau này lập nước Nam Việt, vốn là một viên tướng nhà Tần tham gia cuộc chinh phạt đó. Người Việt học về ông trong sách sử, và vẫn tranh luận về vai trò của ông tới nay.

<short pause> Nghĩa là thế giới của Kingdom không xa lạ như ta nghĩ. Nó là một phần câu chuyện lớn mà lịch sử Việt Nam cũng có mặt.

<short pause> Và đây là bản đồ thật và hư cấu trong một hình. Cột thật: Doanh Chính, Lã Bất Vi, loạn Lao Ái, Vương Tiễn, Lý Mục, Kinh Kha, trận thua Hạng Yên, và Lý Tín.

<short pause> Cột có tên thật nhưng thay đổi: Dương Đoan Hòa thành nữ vương miền núi, tuổi thơ mồ côi của Lý Tín, và lý tưởng của Doanh Chính.

<short pause> Cột hư cấu: người đóng thế, cô gái đeo mặt nạ, phần lớn đồng đội của Lý Tín, và những võ tướng một người địch trăm.

<short pause> Cột giả thuyết: Lã Bất Vi là cha ruột, và Hoàn Nghĩ là Phàn Ô Kỳ. Sử sách chưa trả lời, nên Kaku để chúng ở mép giấy.

<short pause> Kingdom là câu chuyện về một cậu bé không có tên trong sử sách thời thơ ấu, nhưng có tên ở những trang quan trọng nhất. Tác giả chỉ viết thêm phần mà lịch sử bỏ trống.

<short pause> Video tiếp theo, Kaku mở một hồ sơ bí ẩn: Chainsaw Man, và câu hỏi vì sao cả thế giới ác quỷ lại sợ một con quỷ cưa máy. Có lý thuyết, và Kaku sẽ gắn nhãn rõ ràng.

<short pause> Nếu bạn thích những video đặt truyện cạnh lịch sử thật, hãy đăng ký kênh. Lần sau bạn đọc Kingdom, bạn sẽ biết trang nào là sử, trang nào là mơ. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Có một chi tiết nối lịch sử này với Việt Nam. Sau khi thống nhất, nhà Tần đem quân xuống phương Nam, vùng mà sử sách gọi là đất Bách Việt.

[pause] Triệu Đà, người sau này lập nước Nam Việt, vốn là một viên tướng nhà Tần tham gia cuộc chinh phạt đó. Người Việt học về ông trong sách sử, và vẫn tranh luận về vai trò của ông tới nay.

[pause] Nghĩa là thế giới của Kingdom không xa lạ như ta nghĩ. Nó là một phần câu chuyện lớn mà lịch sử Việt Nam cũng có mặt.

[pause] Và đây là bản đồ thật và hư cấu trong một hình. Cột thật: Doanh Chính, Lã Bất Vi, loạn Lao Ái, Vương Tiễn, Lý Mục, Kinh Kha, trận thua Hạng Yên, và Lý Tín.

[pause] Cột có tên thật nhưng thay đổi: Dương Đoan Hòa thành nữ vương miền núi, tuổi thơ mồ côi của Lý Tín, và lý tưởng của Doanh Chính.

[pause] Cột hư cấu: người đóng thế, cô gái đeo mặt nạ, phần lớn đồng đội của Lý Tín, và những võ tướng một người địch trăm.

[pause] Cột giả thuyết: Lã Bất Vi là cha ruột, và Hoàn Nghĩ là Phàn Ô Kỳ. Sử sách chưa trả lời, nên Kaku để chúng ở mép giấy.

[pause] Kingdom là câu chuyện về một cậu bé không có tên trong sử sách thời thơ ấu, nhưng có tên ở những trang quan trọng nhất. Tác giả chỉ viết thêm phần mà lịch sử bỏ trống.

[pause] Video tiếp theo, Kaku mở một hồ sơ bí ẩn: Chainsaw Man, và câu hỏi vì sao cả thế giới ác quỷ lại sợ một con quỷ cưa máy. Có lý thuyết, và Kaku sẽ gắn nhãn rõ ràng.

[pause] Nếu bạn thích những video đặt truyện cạnh lịch sử thật, hãy đăng ký kênh. Lần sau bạn đọc Kingdom, bạn sẽ biết trang nào là sử, trang nào là mơ. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
