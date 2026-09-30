# Bộ prompt · Yu-Gi-Oh!: Lịch sử luật bài từ Fusion tới Link — bạn rời game ở thời kỳ nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 7 đoạn đọc, khoảng 15.0 phút giọng.
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

Lời: Nếu bạn lớn lên ở Việt Nam những năm 2000, rất có thể bạn từng có một xấp bài Yu-Gi-Oh!, mua ở cổng trường, v…

```text
Wide 16:9 landscape cinematic frame. a small stack of worn trading cards held together with a rubber band on a classroom desk, close-up, nostalgic warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Và luật thì mỗi nhóm bạn một kiểu. Có nhóm cho gọi quái vật mạnh không cần hiến tế. Có nhóm tính bài bẫy là ă…

```text
Wide 16:9 landscape cinematic frame. two children arguing over a card with a third child holding a crumpled handwritten rules sheet, humorous top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Ngày đó, luật chơi rất đơn giản: đặt quái vật, tấn công, trừ điểm. Mạnh nhất là con rồng mắt xanh.

```text
Wide 16:9 landscape cinematic frame. two children kneeling on a tiled floor with cards laid out between them, top-down shot, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Còn bây giờ? Một lượt đi có thể kéo dài mười phút, triệu hồi hàng chục quái vật, với những cái tên như Synchr…

```text
Wide 16:9 landscape cinematic frame. a modern game mat crowded with many cards in complex zones and a bewildered hand hovering above, top-down shot, cool bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Hôm nay Kaku kể lịch sử luật bài Yu-Gi-Oh!, từ năm 1999 tới nay. Mỗi thời kỳ có một phát minh, và mỗi phát mi…

```text
Wide 16:9 landscape cinematic frame. a split image: an old rubber-banded card stack on the left, a modern organized deck box on the right, symmetrical composition, contrasting warm and cool light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku kể chuyện ngày xưa và bây giờ. Cuối video là một đường thời gian thu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot shuffling a tiny deck of cards with a nostalgic smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Kaku nói trước: video này nói về luật chơi và lịch sử, không phải hướng dẫn cờ bạc hay mua bán bài. Và Kaku k…

```text
Wide 16:9 landscape cinematic frame. a row of blank trading card outlines drawn on paper, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Gốc rễ: truyện tranh của Takahashi Kazuki

Lời: Yu-Gi-Oh! bắt đầu là manga của tác giả Takahashi Kazuki, đăng trên Weekly Shonen Jump từ năm 1996 tới 2004.

```text
Wide 16:9 landscape cinematic frame. a vintage manga magazine lying open on a desk with a game board sketch beside it, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Cái tên Yu-Gi-Oh! trong tiếng Nhật có nghĩa là Vua trò chơi. Và nhân vật chính Yugi là một cậu bé nhút nhát,…

```text
Wide 16:9 landscape cinematic frame. an old golden puzzle box resting on a school desk beside a stack of board games, close-up, warm mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Ban đầu, truyện nói về nhiều loại trò chơi khác nhau: xúc xắc, bài, cờ. Trò chơi bài Duel Monsters chỉ là một…

```text
Wide 16:9 landscape cinematic frame. a table covered with dice, a small board game, and a few scattered cards, top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Nhưng độc giả thích trò chơi bài nhất. Truyện dần tập trung vào nó, và công ty Konami biến trò chơi trong tru…

```text
Wide 16:9 landscape cinematic frame. a fictional card from a sketchbook turning into a printed card on a factory line, symbolic split image, warm to cool light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Takahashi Kazuki mất năm 2022. Người ta tìm thấy ông ở vùng biển Okinawa, và sau đó biết rằng ông đã lao xuốn…

```text
Wide 16:9 landscape cinematic frame. a calm ocean at sunset with a single card-shaped paper boat floating on the water, wide shot, gentle golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Thời kỳ 1: 1999, luật nền

Lời: Tháng hai năm 1999, Konami ra mắt bộ bài đầu tiên ở Nhật. Luật chơi chính thức được giới thiệu một tháng sau…

```text
Wide 16:9 landscape cinematic frame. a small unopened booster pack and a thin folded rulebook on a wooden table, close-up, warm vintage light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Luật nền rất gọn: mỗi người bắt đầu với tám nghìn điểm sinh mệnh. Mỗi lượt, bạn được triệu hồi thường một quá…

```text
Wide 16:9 landscape cinematic frame. a scoreboard showing the number eight thousand beside two monster card outlines, one being sacrificed for a bigger one, infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và khi hai người cùng kích hoạt hiệu ứng, trò chơi có một cơ chế gọi là chuỗi: hiệu ứng sau cùng được giải qu…

```text
Wide 16:9 landscape cinematic frame. a chain of small linked rings laid across a game mat, the last ring glowing brightest, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Chi tiết thú vị: trong anime thời đầu, nhiều trận chỉ dùng bốn nghìn điểm sinh mệnh để trận đấu ngắn gọn trên…

```text
Wide 16:9 landscape cinematic frame. two scoreboards side by side, one showing four thousand and one showing eight thousand, with a small TV icon above the first, infographic style, bright light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Ngoài quái vật còn có bài phép và bài bẫy. Phép dùng ngay, bẫy đặt úp chờ đối thủ mắc vào.

```text
Wide 16:9 landscape cinematic frame. a face-down card on a table with a tiny mousetrap doodle beside it, humorous close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Và ngay từ đầu đã có hai cách triệu hồi đặc biệt. Kaku gọi đây là hai phát minh đầu tiên.

```text
Wide 16:9 landscape cinematic frame. two special card outlines glowing faintly on a table, one with a swirl symbol and one with a flame symbol, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Phát minh một: Dung hợp, Fusion. Dùng một lá bài phép đặc biệt để trộn hai hay nhiều quái vật thành một quái…

```text
Wide 16:9 landscape cinematic frame. two card outlines merging into a single larger card with swirling light between them, dynamic close-up, vibrant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Phát minh hai: Nghi lễ, Ritual. Dùng một lá bài nghi lễ và hiến tế quái vật có tổng cấp đủ lớn để gọi một quá…

```text
Wide 16:9 landscape cinematic frame. a card outline placed on a small stone altar with candles and offerings arranged around it, close-up, warm ceremonial light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Quái vật Dung hợp nằm trong một khu riêng, ngoài bộ bài chính. Khu này về sau được gọi là Extra Deck, và nó s…

```text
Wide 16:9 landscape cinematic frame. a small separate card box set beside a main deck on a game mat, labeled with a simple plus sign, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kaku để ý: ở thời kỳ này, một trận đấu thường kéo dài nhiều lượt. Người ta đánh qua lại, tính toán từng lá. Đ…

```text
Wide 16:9 landscape cinematic frame. two children laughing and slapping cards down on a floor, top-down shot, warm golden nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Những lá bài huyền thoại của tuổi thơ

Lời: Trước khi sang thời kỳ tiếp theo, Kaku ghé qua những lá bài mà gần như ai chơi hồi đó cũng biết tên.

```text
Wide 16:9 landscape cinematic frame. a small wooden treasure box lined with velvet holding a few blank card outlines, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Rồng trắng mắt xanh, lá bài của Kaiba, với ba nghìn điểm tấn công, con số khổng lồ ở thời đó. Có một lá trong…

```text
Wide 16:9 landscape cinematic frame. a glowing white dragon silhouette rising above a schoolyard at dusk, wide shot, majestic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Pháp sư bóng tối, lá bài của Yugi, biểu tượng của lòng tin giữa người chơi và quái vật của mình.

```text
Wide 16:9 landscape cinematic frame. a mysterious robed silhouette holding a staff under a starry night sky, wide shot, soft purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Và Exodia, bộ năm mảnh. Ai gom đủ năm mảnh trên tay là thắng ngay lập tức, bất kể điểm sinh mệnh. Đó là giấc…

```text
Wide 16:9 landscape cinematic frame. five blank card outlines arranged in the shape of a figure with a chained silhouette glowing behind them, close-up, golden dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Kaku để ý: những lá bài tuổi thơ mạnh vì những con số lớn. Còn bài hiện đại mạnh vì hiệu ứng. Đó là thay đổi…

```text
Wide 16:9 landscape cinematic frame. two card outlines side by side, one with a huge number and one covered in small text, close-up, contrasting warm and cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Thời kỳ 2: những năm 2000, bùng nổ toàn cầu

Lời: Anime Yu-Gi-Oh! Duel Monsters phát năm 2000 và lan ra toàn thế giới. Năm 2002, bản tiếng Anh của trò chơi bài…

```text
Wide 16:9 landscape cinematic frame. a globe on a desk with small card icons pinned across many countries, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Tiếp theo là Yu-Gi-Oh! GX, với nhân vật chính dùng bài Dung hợp. Thời kỳ này, Fusion là cách triệu hồi được y…

```text
Wide 16:9 landscape cinematic frame. a school-like academy building on an island with students carrying card decks, wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Danh sách này được cập nhật định kỳ. Mỗi lần công bố, cộng đồng lại xôn xao: lá nào bị cấm, lá nào được thả.…

```text
Wide 16:9 landscape cinematic frame. a crowd of people gathered around a notice board reading a newly posted list, back view, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Luật cũng dần phải thêm những điều chỉnh: danh sách bài cấm và bài hạn chế, vì có những lá quá mạnh làm mất c…

```text
Wide 16:9 landscape cinematic frame. a list of blank card outlines with some crossed out in red and some marked with a limit number, close-up, office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Năm 2009 và 2011, sách Kỷ lục Guinness công nhận Yu-Gi-Oh! là trò chơi bài bán chạy nhất thế giới, với hơn ha…

```text
Wide 16:9 landscape cinematic frame. a large trophy beside a towering stack of cards reaching up out of frame, low-angle shot, bright celebratory light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Ở Việt Nam thời đó, nhiều người không biết có luật chính thức. Bài mua ở cổng trường thường là bài in lại, và…

```text
Wide 16:9 landscape cinematic frame. a small roadside stall near a school gate with colorful card packs hanging on strings, wide shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy thời kỳ này là đỉnh cao của tuổi thơ nhiều người. Và cũng là lúc nhiều người rời game, vì lớn lên,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving goodbye to a small group of children walking away with their card decks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Thời kỳ 3: 2008, Synchro

Lời: Năm 2008, cùng với anime Yu-Gi-Oh! 5D's, một phát minh mới ra đời: triệu hồi Đồng bộ, Synchro.

```text
Wide 16:9 landscape cinematic frame. a motorcycle road at night with glowing speed lines and a card outline floating above it, wide shot, cool neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Luật Synchro: lấy một quái vật đặc biệt gọi là Tuner, cộng với một hay nhiều quái vật khác. Nếu tổng cấp sao…

```text
Wide 16:9 landscape cinematic frame. a simple math equation drawn with card outlines: a small card plus two cards equals a larger card, with star counts beside each, infographic style. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Anime 5D's còn thêm một ý tưởng rất nhớ: đấu bài trên mô tô, gọi là Turbo Duel. Luật trong anime có riêng một…

```text
Wide 16:9 landscape cinematic frame. two motorcycles racing side by side on a highway at night with glowing card outlines floating beside them, dynamic wide shot, neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nghe như phép cộng. Và đúng là phép cộng. Nhưng nó thay đổi mọi thứ: không cần lá phép đặc biệt nào, chỉ cần…

```text
Wide 16:9 landscape cinematic frame. a small abacus beside a stack of cards on a game mat, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Lần đầu tiên, Extra Deck trở thành nơi chứa những quái vật mạnh mà ai cũng có thể gọi ra thường xuyên. Tốc độ…

```text
Wide 16:9 landscape cinematic frame. an opened card box with many glowing card outlines rising out of it, close-up, bright magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku để ý: Synchro là phát minh đầu tiên biến việc đếm số thành trung tâm của trò chơi. Người chơi bắt đầu ng…

```text
Wide 16:9 landscape cinematic frame. a notebook page filled with star-level calculations and small card doodles, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Thời kỳ 4: 2011, Xyz

Lời: Tháng ba năm 2011, cùng anime Yu-Gi-Oh! Zexal, lại một phát minh nữa: triệu hồi Xyz, đọc là ích-xít.

```text
Wide 16:9 landscape cinematic frame. a starry night sky with a card outline hovering and small orbs circling it, wide shot, cool cosmic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Luật Xyz: lấy hai hay nhiều quái vật có cùng cấp, chồng chúng lên nhau. Quái vật Xyz không có cấp, mà có hạng.

```text
Wide 16:9 landscape cinematic frame. two identical card outlines being stacked beneath a larger card, with small glowing orbs circling the stack, dynamic close-up, blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Những quái vật bên dưới trở thành nguyên liệu. Quái vật Xyz có thể gỡ nguyên liệu ra để dùng hiệu ứng. Nguyên…

```text
Wide 16:9 landscape cinematic frame. a card with small glowing tokens orbiting it, one token breaking away and fading, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Có những quái vật Xyz còn có thể được chồng lên chính một quái vật Xyz khác, tạo thành dạng mạnh hơn. Trò chơ…

```text
Wide 16:9 landscape cinematic frame. a tall stack of card outlines layered on top of each other with orbs circling each layer, close-up, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nếu Synchro là phép cộng, Xyz là phép so sánh: không cần cộng, chỉ cần giống nhau. Hai hệ thống sống song son…

```text
Wide 16:9 landscape cinematic frame. a side-by-side diagram: a plus sign under one set of cards and an equals sign under another, infographic style, bright light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Và mỗi lần có phát minh mới, trò chơi lại nhanh hơn. Số quái vật được gọi ra mỗi lượt tăng lên liên tục.

```text
Wide 16:9 landscape cinematic frame. a speedometer needle climbing higher beside a stack of cards, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Thời kỳ 5: 2014, Pendulum

Lời: Năm 2014, với anime Yu-Gi-Oh! Arc-V, đến lượt triệu hồi Con lắc, Pendulum.

```text
Wide 16:9 landscape cinematic frame. a large pendulum swinging slowly in a grand hall with card outlines hovering at each end, wide shot, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Quái vật Pendulum lai giữa quái vật và bài phép. Đặt hai lá vào hai ô đặc biệt, gọi là thang Con lắc, mỗi lá…

```text
Wide 16:9 landscape cinematic frame. two card outlines placed on either side of a game mat with numbers glowing above them, forming a scale, top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Mọi quái vật có cấp nằm giữa hai con số đó đều có thể được triệu hồi cùng một lúc. Không phải một con, mà cả…

```text
Wide 16:9 landscape cinematic frame. many card outlines swinging down together from a glowing arc between two pillars, dynamic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nghĩa là một lá Pendulum vừa là quái vật, vừa có thể làm cột mốc cho thang Con lắc. Một lá bài làm hai việc.…

```text
Wide 16:9 landscape cinematic frame. a single card outline split diagonally into two halves of different colors, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Và điều đặc biệt: quái vật Pendulum bị đánh bại không vào mộ bài, mà quay về Extra Deck, sẵn sàng được gọi lạ…

```text
Wide 16:9 landscape cinematic frame. a card outline floating back up into an open card box instead of falling into a pit, symbolic close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Có người chơi gọi thời kỳ này là thời kỳ mọi thứ đều quá nhanh. Có trận kết thúc ngay ở lượt đầu tiên, khi ng…

```text
Wide 16:9 landscape cinematic frame. a game mat fully covered in card outlines on one side while the other side is completely empty, top-down shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy Pendulum là phát minh táo bạo nhất. Nó cho phép số lượng quái vật trên sân tăng vọt, và cũng làm ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot balancing on a swinging pendulum, wobbling nervously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Thời kỳ 6: 2017, Link và luật mới

Lời: Năm 2017, với anime Yu-Gi-Oh! VRAINS, xuất hiện triệu hồi Liên kết, Link, cùng một thay đổi lớn về luật sân đ…

```text
Wide 16:9 landscape cinematic frame. a futuristic digital grid floor with glowing arrows pointing in different directions, wide shot, cool cyber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Luật mới thêm hai ô ở giữa sân, gọi là vùng quái vật Extra. Và từ đó, mỗi người chỉ được gọi một quái vật từ…

```text
Wide 16:9 landscape cinematic frame. a game mat diagram with two new zones glowing in the center and arrows pointing from them, top-down infographic, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Quái vật Link không có cấp, không có điểm phòng thủ. Thay vào đó, nó có những mũi tên. Mũi tên chỉ vào đâu, ô…

```text
Wide 16:9 landscape cinematic frame. a card outline with glowing arrows on its edges pointing outward toward empty zones, close-up, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Luật này là một cú phanh gấp. Nó giới hạn số quái vật Extra Deck mỗi người có thể dùng, để hãm tốc độ mà Sync…

```text
Wide 16:9 landscape cinematic frame. a brake lever being pulled beside a speeding card deck, humorous symbolic close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Cộng đồng tranh cãi rất nhiều. Pendulum bị ảnh hưởng nặng nhất. Và vài năm sau, luật được nới ra một phần, ch…

```text
Wide 16:9 landscape cinematic frame. a rulebook page with one paragraph crossed out and a revised paragraph written beside it in a different ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Với người chơi mới, Link lại có một lợi ích: nó biến vị trí đặt quái vật thành một câu đố hình học. Ai thích…

```text
Wide 16:9 landscape cinematic frame. a grid of squares with arrows forming a neat puzzle pattern, top-down infographic, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Kaku để ý: đây là lần đầu tiên trong lịch sử game, một phát minh mới không làm trò chơi nhanh hơn, mà cố làm…

```text
Wide 16:9 landscape cinematic frame. a speedometer needle dropping back slightly with a small relieved face doodled beside it, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Sau Link: nhánh rẽ Rush Duel

Lời: Từ năm 2020, Konami còn tạo ra một nhánh rẽ: Rush Duel, một kiểu chơi đơn giản và nhanh hơn, gắn với anime Yu…

```text
Wide 16:9 landscape cinematic frame. a smaller, simpler game mat beside a complex one on a table, top-down shot, bright friendly light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Trong Rush Duel, mỗi lượt bạn được rút bài cho tới khi đủ năm lá trên tay, và được triệu hồi thường không giớ…

```text
Wide 16:9 landscape cinematic frame. a child's hand holding exactly five blank card outlines fanned out, close-up, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Rush Duel quay về tinh thần ngày xưa: ít luật, dễ hiểu, dành cho người mới. Nó như một lời mời những người đã…

```text
Wide 16:9 landscape cinematic frame. an open door with warm light spilling out onto a small card table, symbolic wide shot, inviting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và năm 2022, trò chơi điện tử Yu-Gi-Oh! Master Duel ra đời, cho phép chơi bản đầy đủ trên điện thoại và máy t…

```text
Wide 16:9 landscape cinematic frame. a phone and a laptop side by side each showing a card game interface, close-up, cool screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Mỗi thời kỳ, một nhân vật chính

Lời: Có một chi tiết vui mà nhiều người không để ý: gần như mỗi bộ anime Yu-Gi-Oh! mới đều có một nhân vật chính m…

```text
Wide 16:9 landscape cinematic frame. a row of small hero silhouettes standing on a timeline, each holding a different glowing card, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Yugi với bài truyền thống. Judai của GX với Fusion. Yusei của 5D's với Synchro, đấu bài trên mô tô. Yuma của…

```text
Wide 16:9 landscape cinematic frame. four small panels on parchment each with a tiny icon: a puzzle piece, a swirl, a motorcycle, a star, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Yuya của Arc-V với Pendulum. Yusaku của VRAINS với Link. Và hãy để ý: tên của họ đều bắt đầu bằng âm Yu.

```text
Wide 16:9 landscape cinematic frame. a list of names on parchment with the first two letters of each name circled in red ink, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhờ vậy, mỗi thế hệ người xem có một nhân vật chính của riêng mình, và một cơ chế gắn với tuổi thơ của họ. Hỏ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny card up to a line of different-aged silhouettes and guessing their ages. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Vì sao luật cứ thay đổi?

Lời: Nhìn lại, vì sao Yu-Gi-Oh! liên tục thêm phát minh mới? Kaku thấy có ba lý do.

```text
Wide 16:9 landscape cinematic frame. a notebook page with three numbered lines and a small card doodle, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Một: mỗi bộ anime mới cần một cơ chế mới để câu chuyện có điểm nhấn, và để bán bộ bài mới.

```text
Wide 16:9 landscape cinematic frame. a TV screen and a booster pack side by side connected by a dotted line, infographic style, bright light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hai: người chơi lâu năm cần cái mới để không chán. Một trò chơi hai mươi lăm năm tuổi phải liên tục làm mình…

```text
Wide 16:9 landscape cinematic frame. an old wooden chest opened to reveal new shiny items inside, symbolic close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Ba: cân bằng. Mỗi phát minh làm lệch cán cân, và luật sau phải sửa lại cán cân đó. Link chính là ví dụ rõ nhấ…

```text
Wide 16:9 landscape cinematic frame. a balance scale being adjusted by a small hand, one side holding a speed icon and the other a brake icon, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và mỗi thời kỳ đều có người yêu và người ghét. Có người nói game mất đi sự đơn giản. Có người nói game chưa b…

```text
Wide 16:9 landscape cinematic frame. two groups of silhouettes sitting at separate tables, one with a simple mat and one with a complex mat, both laughing, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ lịch sử Yu-Gi-Oh! giống lịch sử của nhiều công nghệ: mỗi phát minh giải quyết một vấn đề, và tạo ra…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a wrench in one wing and a new problem card in the other, looking amused. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Người chơi cũ nên quay lại thế nào?

Lời: Nếu bạn rời game ở thời kỳ Fusion và muốn quay lại, đây là gợi ý của Kaku. Bước một: học Synchro và Xyz trước…

```text
Wide 16:9 landscape cinematic frame. a small step ladder with the first two steps labeled with plus and equals symbols, close-up, bright friendly light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bước hai: học Link, vì nó quyết định cách bạn đặt quái vật trên sân. Bước ba mới là Pendulum, cơ chế phức tạp…

```text
Wide 16:9 landscape cinematic frame. the same ladder with the next two steps labeled with an arrow and a pendulum icon, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và đừng ngại hỏi. Cộng đồng người chơi Yu-Gi-Oh! ở Việt Nam, trên mạng lẫn ở các cửa hàng bài, thường rất sẵn…

```text
Wide 16:9 landscape cinematic frame. a friendly gathering at a small card shop with players helping each other at long tables, wide shot, warm welcoming light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Hoặc bạn có thể thử Rush Duel trước, để làm quen lại với nhịp chơi, rồi mới sang bản đầy đủ.

```text
Wide 16:9 landscape cinematic frame. a small practice mat beside a full-size mat with a friendly arrow pointing from one to the other, top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và quan trọng nhất: tìm một người bạn để chơi cùng. Yu-Gi-Oh! vui nhất không phải khi thắng, mà khi hai người…

```text
Wide 16:9 landscape cinematic frame. two adults sitting across from each other at a café table playing cards and laughing, medium shot, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Đường thời gian thu gọn

Lời: Và đây là đường thời gian thu gọn. 1999: luật nền, Fusion và Ritual. 2002: bản tiếng Anh ra thế giới.

```text
Wide 16:9 landscape cinematic frame. a horizontal timeline on parchment with the first two markers illuminated, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: 2008: Synchro, phép cộng. 2011: Xyz, phép so sánh. 2014: Pendulum, triệu hồi cả đàn.

```text
Wide 16:9 landscape cinematic frame. the middle section of the timeline with three glowing markers, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: 2017: Link và vùng quái vật Extra, cú phanh gấp. 2020: Rush Duel, lối vào cho người mới. 2022: Master Duel, t…

```text
Wide 16:9 landscape cinematic frame. the final section of the timeline with three more markers and a small phone icon at the end, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Bạn đã rời game ở thời kỳ nào? Và bạn nhớ nhất lá bài nào của tuổi thơ? Viết vào bình luận nhé, Kaku rất muốn…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny blank card doodle and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Kết

Lời: Từ một trò chơi trong truyện tranh, Yu-Gi-Oh! trở thành trò chơi bài bán chạy nhất thế giới, và liên tục thay…

```text
Wide 16:9 landscape cinematic frame. a hand drawing a single card from a deck in slow motion, soft glow around the card's edge, extreme close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tiếp theo, Kaku quay về một bộ đang phát sóng: Black Clover, và các dạng Ác ma hợp thể của Asta, từ lần…

```text
Wide 16:9 landscape cinematic frame. a worn grimoire with a torn black cover resting beside a large rough sword, close-up, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này gợi lại tuổi thơ của bạn, hãy đăng ký kênh, và gửi video cho người bạn từng đấu bài với bạn ở c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a single card face-down on a table and waving goodbye with a wink. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Gốc rễ: truyện tranh của Takahashi Kazuki

Khoảng 138 giây · cảnh s01–s12 · 1791 ký tự

**Gemini**

```text
Nếu bạn lớn lên ở Việt Nam những năm 2000, rất có thể bạn từng có một xấp bài Yu-Gi-Oh!, mua ở cổng trường, và đấu với bạn bè trên nền gạch lớp học.

<short pause> Và luật thì mỗi nhóm bạn một kiểu. Có nhóm cho gọi quái vật mạnh không cần hiến tế. Có nhóm tính bài bẫy là ăn gian. Mỗi trận đấu kèm theo một cuộc tranh cãi về luật.

<short pause> Ngày đó, luật chơi rất đơn giản: đặt quái vật, tấn công, trừ điểm. Mạnh nhất là con rồng mắt xanh.

<short pause> Còn bây giờ? Một lượt đi có thể kéo dài mười phút, triệu hồi hàng chục quái vật, với những cái tên như Synchro, Xyz, Pendulum, Link. Nhiều người chơi cũ quay lại và không hiểu gì nữa.

<short pause> Hôm nay Kaku kể lịch sử luật bài Yu-Gi-Oh!, từ năm 1999 tới nay. Mỗi thời kỳ có một phát minh, và mỗi phát minh thay đổi cả cách chơi.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku kể chuyện ngày xưa và bây giờ. Cuối video là một đường thời gian thu gọn, để bạn biết mình đã rời game ở thời kỳ nào.

<short pause> Kaku nói trước: video này nói về luật chơi và lịch sử, không phải hướng dẫn cờ bạc hay mua bán bài. Và Kaku không dùng hình bài chính thức. Mọi lá bài trong video đều là hình minh họa trống.

<short pause> Yu-Gi-Oh! bắt đầu là manga của tác giả Takahashi Kazuki, đăng trên Weekly Shonen Jump từ năm 1996 tới 2004.

<short pause> Cái tên Yu-Gi-Oh! trong tiếng Nhật có nghĩa là Vua trò chơi. Và nhân vật chính Yugi là một cậu bé nhút nhát, được một linh hồn cổ đại trong món đồ chơi xếp hình giúp đỡ.

<short pause> Ban đầu, truyện nói về nhiều loại trò chơi khác nhau: xúc xắc, bài, cờ. Trò chơi bài Duel Monsters chỉ là một trong số đó.

<short pause> Nhưng độc giả thích trò chơi bài nhất. Truyện dần tập trung vào nó, và công ty Konami biến trò chơi trong truyện thành trò chơi thật.

<short pause> Takahashi Kazuki mất năm 2022. Người ta tìm thấy ông ở vùng biển Okinawa, và sau đó biết rằng ông đã lao xuống biển để cứu những người gặp nạn. Kaku muốn dành một phút để nhớ tới ông.
```

**ElevenLabs**

```text
Nếu bạn lớn lên ở Việt Nam những năm 2000, rất có thể bạn từng có một xấp bài Yu-Gi-Oh!, mua ở cổng trường, và đấu với bạn bè trên nền gạch lớp học.

[pause] Và luật thì mỗi nhóm bạn một kiểu. Có nhóm cho gọi quái vật mạnh không cần hiến tế. Có nhóm tính bài bẫy là ăn gian. Mỗi trận đấu kèm theo một cuộc tranh cãi về luật.

[pause] Ngày đó, luật chơi rất đơn giản: đặt quái vật, tấn công, trừ điểm. Mạnh nhất là con rồng mắt xanh.

[pause] [curious] Còn bây giờ? Một lượt đi có thể kéo dài mười phút, triệu hồi hàng chục quái vật, với những cái tên như Synchro, Xyz, Pendulum, Link. Nhiều người chơi cũ quay lại và không hiểu gì nữa.

[pause] Hôm nay Kaku kể lịch sử luật bài Yu-Gi-Oh!, từ năm 1999 tới nay. Mỗi thời kỳ có một phát minh, và mỗi phát minh thay đổi cả cách chơi.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku kể chuyện ngày xưa và bây giờ. Cuối video là một đường thời gian thu gọn, để bạn biết mình đã rời game ở thời kỳ nào.

[pause] Kaku nói trước: video này nói về luật chơi và lịch sử, không phải hướng dẫn cờ bạc hay mua bán bài. Và Kaku không dùng hình bài chính thức. Mọi lá bài trong video đều là hình minh họa trống.

[pause] Yu-Gi-Oh! bắt đầu là manga của tác giả Takahashi Kazuki, đăng trên Weekly Shonen Jump từ năm 1996 tới 2004.

[pause] Cái tên Yu-Gi-Oh! trong tiếng Nhật có nghĩa là Vua trò chơi. Và nhân vật chính Yugi là một cậu bé nhút nhát, được một linh hồn cổ đại trong món đồ chơi xếp hình giúp đỡ.

[pause] Ban đầu, truyện nói về nhiều loại trò chơi khác nhau: xúc xắc, bài, cờ. Trò chơi bài Duel Monsters chỉ là một trong số đó.

[pause] Nhưng độc giả thích trò chơi bài nhất. Truyện dần tập trung vào nó, và công ty Konami biến trò chơi trong truyện thành trò chơi thật.

[pause] Takahashi Kazuki mất năm 2022. Người ta tìm thấy ông ở vùng biển Okinawa, và sau đó biết rằng ông đã lao xuống biển để cứu những người gặp nạn. Kaku muốn dành một phút để nhớ tới ông.
```

### c02 · Thời kỳ 1: 1999, luật nền / Những lá bài huyền thoại của tuổi thơ

Khoảng 153 giây · cảnh s13–s27 · 1985 ký tự

**Gemini**

```text
Tháng hai năm 1999, Konami ra mắt bộ bài đầu tiên ở Nhật. Luật chơi chính thức được giới thiệu một tháng sau đó.

<short pause> Luật nền rất gọn: mỗi người bắt đầu với tám nghìn điểm sinh mệnh. Mỗi lượt, bạn được triệu hồi thường một quái vật. Quái vật mạnh hơn cần hiến tế quái vật yếu hơn.

<short pause> Và khi hai người cùng kích hoạt hiệu ứng, trò chơi có một cơ chế gọi là chuỗi: hiệu ứng sau cùng được giải quyết trước. Khái niệm nhỏ này là nền móng cho mọi sự phức tạp về sau.

<short pause> Chi tiết thú vị: trong anime thời đầu, nhiều trận chỉ dùng bốn nghìn điểm sinh mệnh để trận đấu ngắn gọn trên màn hình. Nhiều đứa trẻ ngoài đời chơi theo anime thay vì theo luật chính thức.

<short pause> Ngoài quái vật còn có bài phép và bài bẫy. Phép dùng ngay, bẫy đặt úp chờ đối thủ mắc vào.

<short pause> Và ngay từ đầu đã có hai cách triệu hồi đặc biệt. Kaku gọi đây là hai phát minh đầu tiên.

<short pause> Phát minh một: Dung hợp, Fusion. Dùng một lá bài phép đặc biệt để trộn hai hay nhiều quái vật thành một quái vật mạnh hơn.

<short pause> Phát minh hai: Nghi lễ, Ritual. Dùng một lá bài nghi lễ và hiến tế quái vật có tổng cấp đủ lớn để gọi một quái vật đặc biệt.

<short pause> Quái vật Dung hợp nằm trong một khu riêng, ngoài bộ bài chính. Khu này về sau được gọi là Extra Deck, và nó sẽ trở thành trung tâm của mọi thay đổi sau này.

<short pause> Kaku để ý: ở thời kỳ này, một trận đấu thường kéo dài nhiều lượt. Người ta đánh qua lại, tính toán từng lá. Đó là cảm giác nhiều người nhớ về tuổi thơ.

<short pause> Trước khi sang thời kỳ tiếp theo, Kaku ghé qua những lá bài mà gần như ai chơi hồi đó cũng biết tên.

<short pause> Rồng trắng mắt xanh, lá bài của Kaiba, với ba nghìn điểm tấn công, con số khổng lồ ở thời đó. Có một lá trong tay là cả lớp phải nể.

<short pause> Pháp sư bóng tối, lá bài của Yugi, biểu tượng của lòng tin giữa người chơi và quái vật của mình.

<short pause> Và Exodia, bộ năm mảnh. Ai gom đủ năm mảnh trên tay là thắng ngay lập tức, bất kể điểm sinh mệnh. Đó là giấc mơ của mọi đứa trẻ cầm bài.

<short pause> Kaku để ý: những lá bài tuổi thơ mạnh vì những con số lớn. Còn bài hiện đại mạnh vì hiệu ứng. Đó là thay đổi lớn nhất mà người chơi cũ cần làm quen.
```

**ElevenLabs**

```text
Tháng hai năm 1999, Konami ra mắt bộ bài đầu tiên ở Nhật. Luật chơi chính thức được giới thiệu một tháng sau đó.

[pause] Luật nền rất gọn: mỗi người bắt đầu với tám nghìn điểm sinh mệnh. Mỗi lượt, bạn được triệu hồi thường một quái vật. Quái vật mạnh hơn cần hiến tế quái vật yếu hơn.

[pause] Và khi hai người cùng kích hoạt hiệu ứng, trò chơi có một cơ chế gọi là chuỗi: hiệu ứng sau cùng được giải quyết trước. Khái niệm nhỏ này là nền móng cho mọi sự phức tạp về sau.

[pause] Chi tiết thú vị: trong anime thời đầu, nhiều trận chỉ dùng bốn nghìn điểm sinh mệnh để trận đấu ngắn gọn trên màn hình. Nhiều đứa trẻ ngoài đời chơi theo anime thay vì theo luật chính thức.

[pause] Ngoài quái vật còn có bài phép và bài bẫy. Phép dùng ngay, bẫy đặt úp chờ đối thủ mắc vào.

[pause] Và ngay từ đầu đã có hai cách triệu hồi đặc biệt. Kaku gọi đây là hai phát minh đầu tiên.

[pause] Phát minh một: Dung hợp, Fusion. Dùng một lá bài phép đặc biệt để trộn hai hay nhiều quái vật thành một quái vật mạnh hơn.

[pause] Phát minh hai: Nghi lễ, Ritual. Dùng một lá bài nghi lễ và hiến tế quái vật có tổng cấp đủ lớn để gọi một quái vật đặc biệt.

[pause] Quái vật Dung hợp nằm trong một khu riêng, ngoài bộ bài chính. Khu này về sau được gọi là Extra Deck, và nó sẽ trở thành trung tâm của mọi thay đổi sau này.

[pause] Kaku để ý: ở thời kỳ này, một trận đấu thường kéo dài nhiều lượt. Người ta đánh qua lại, tính toán từng lá. Đó là cảm giác nhiều người nhớ về tuổi thơ.

[pause] Trước khi sang thời kỳ tiếp theo, Kaku ghé qua những lá bài mà gần như ai chơi hồi đó cũng biết tên.

[pause] Rồng trắng mắt xanh, lá bài của Kaiba, với ba nghìn điểm tấn công, con số khổng lồ ở thời đó. Có một lá trong tay là cả lớp phải nể.

[pause] Pháp sư bóng tối, lá bài của Yugi, biểu tượng của lòng tin giữa người chơi và quái vật của mình.

[pause] Và Exodia, bộ năm mảnh. Ai gom đủ năm mảnh trên tay là thắng ngay lập tức, bất kể điểm sinh mệnh. Đó là giấc mơ của mọi đứa trẻ cầm bài.

[pause] Kaku để ý: những lá bài tuổi thơ mạnh vì những con số lớn. Còn bài hiện đại mạnh vì hiệu ứng. Đó là thay đổi lớn nhất mà người chơi cũ cần làm quen.
```

### c03 · Thời kỳ 2: những năm 2000, bùng nổ toàn cầu / Thời kỳ 3: 2008, Synchro

Khoảng 141 giây · cảnh s28–s40 · 1837 ký tự

**Gemini**

```text
Anime Yu-Gi-Oh! Duel Monsters phát năm 2000 và lan ra toàn thế giới. Năm 2002, bản tiếng Anh của trò chơi bài ra mắt ở Bắc Mỹ.

<short pause> Tiếp theo là Yu-Gi-Oh! GX, với nhân vật chính dùng bài Dung hợp. Thời kỳ này, Fusion là cách triệu hồi được yêu thích nhất.

<short pause> Danh sách này được cập nhật định kỳ. Mỗi lần công bố, cộng đồng lại xôn xao: lá nào bị cấm, lá nào được thả. Nó giống như bản tin thời sự của người chơi bài.

<short pause> Luật cũng dần phải thêm những điều chỉnh: danh sách bài cấm và bài hạn chế, vì có những lá quá mạnh làm mất cân bằng.

<short pause> Năm 2009 và 2011, sách Kỷ lục Guinness công nhận Yu-Gi-Oh! là trò chơi bài bán chạy nhất thế giới, với hơn hai mươi lăm tỉ lá bài tính tới tháng ba năm 2011.

<short pause> Ở Việt Nam thời đó, nhiều người không biết có luật chính thức. Bài mua ở cổng trường thường là bài in lại, và luật được truyền miệng từ anh chị trong xóm.

<short pause> <laugh> Kaku thấy thời kỳ này là đỉnh cao của tuổi thơ nhiều người. Và cũng là lúc nhiều người rời game, vì lớn lên, đi học, đi làm. <short pause> Nhưng game thì tiếp tục thay đổi.

<short pause> Năm 2008, cùng với anime Yu-Gi-Oh! 5D's, một phát minh mới ra đời: triệu hồi Đồng bộ, Synchro.

<short pause> Luật Synchro: lấy một quái vật đặc biệt gọi là Tuner, cộng với một hay nhiều quái vật khác. Nếu tổng cấp sao bằng đúng cấp của quái vật Synchro, bạn gọi nó ra từ Extra Deck.

<short pause> Anime 5D's còn thêm một ý tưởng rất nhớ: đấu bài trên mô tô, gọi là Turbo Duel. Luật trong anime có riêng một loại bài phép tốc độ. Ngoài đời không dùng, nhưng người xem nhớ mãi.

<short pause> Nghe như phép cộng. Và đúng là phép cộng. <short pause> Nhưng nó thay đổi mọi thứ: không cần lá phép đặc biệt nào, chỉ cần có đủ quái vật trên sân.

<short pause> Lần đầu tiên, Extra Deck trở thành nơi chứa những quái vật mạnh mà ai cũng có thể gọi ra thường xuyên. Tốc độ trò chơi tăng hẳn.

<short pause> Kaku để ý: Synchro là phát minh đầu tiên biến việc đếm số thành trung tâm của trò chơi. Người chơi bắt đầu nghĩ bằng các phép tính cấp sao.
```

**ElevenLabs**

```text
Anime Yu-Gi-Oh! Duel Monsters phát năm 2000 và lan ra toàn thế giới. Năm 2002, bản tiếng Anh của trò chơi bài ra mắt ở Bắc Mỹ.

[pause] Tiếp theo là Yu-Gi-Oh! GX, với nhân vật chính dùng bài Dung hợp. Thời kỳ này, Fusion là cách triệu hồi được yêu thích nhất.

[pause] Danh sách này được cập nhật định kỳ. Mỗi lần công bố, cộng đồng lại xôn xao: lá nào bị cấm, lá nào được thả. Nó giống như bản tin thời sự của người chơi bài.

[pause] Luật cũng dần phải thêm những điều chỉnh: danh sách bài cấm và bài hạn chế, vì có những lá quá mạnh làm mất cân bằng.

[pause] Năm 2009 và 2011, sách Kỷ lục Guinness công nhận Yu-Gi-Oh! là trò chơi bài bán chạy nhất thế giới, với hơn hai mươi lăm tỉ lá bài tính tới tháng ba năm 2011.

[pause] Ở Việt Nam thời đó, nhiều người không biết có luật chính thức. Bài mua ở cổng trường thường là bài in lại, và luật được truyền miệng từ anh chị trong xóm.

[pause] [chuckles] Kaku thấy thời kỳ này là đỉnh cao của tuổi thơ nhiều người. Và cũng là lúc nhiều người rời game, vì lớn lên, đi học, đi làm. [pause] Nhưng game thì tiếp tục thay đổi.

[pause] Năm 2008, cùng với anime Yu-Gi-Oh! 5D's, một phát minh mới ra đời: triệu hồi Đồng bộ, Synchro.

[pause] Luật Synchro: lấy một quái vật đặc biệt gọi là Tuner, cộng với một hay nhiều quái vật khác. Nếu tổng cấp sao bằng đúng cấp của quái vật Synchro, bạn gọi nó ra từ Extra Deck.

[pause] Anime 5D's còn thêm một ý tưởng rất nhớ: đấu bài trên mô tô, gọi là Turbo Duel. Luật trong anime có riêng một loại bài phép tốc độ. Ngoài đời không dùng, nhưng người xem nhớ mãi.

[pause] Nghe như phép cộng. Và đúng là phép cộng. [pause] Nhưng nó thay đổi mọi thứ: không cần lá phép đặc biệt nào, chỉ cần có đủ quái vật trên sân.

[pause] Lần đầu tiên, Extra Deck trở thành nơi chứa những quái vật mạnh mà ai cũng có thể gọi ra thường xuyên. Tốc độ trò chơi tăng hẳn.

[pause] Kaku để ý: Synchro là phát minh đầu tiên biến việc đếm số thành trung tâm của trò chơi. Người chơi bắt đầu nghĩ bằng các phép tính cấp sao.
```

### c04 · Thời kỳ 4: 2011, Xyz / Thời kỳ 5: 2014, Pendulum

Khoảng 129 giây · cảnh s41–s53 · 1678 ký tự

**Gemini**

```text
Tháng ba năm 2011, cùng anime Yu-Gi-Oh! Zexal, lại một phát minh nữa: triệu hồi Xyz, đọc là ích-xít.

<short pause> Luật Xyz: lấy hai hay nhiều quái vật có cùng cấp, chồng chúng lên nhau. Quái vật Xyz không có cấp, mà có hạng.

<short pause> Những quái vật bên dưới trở thành nguyên liệu. Quái vật Xyz có thể gỡ nguyên liệu ra để dùng hiệu ứng. Nguyên liệu giống như đạn dược.

<short pause> Có những quái vật Xyz còn có thể được chồng lên chính một quái vật Xyz khác, tạo thành dạng mạnh hơn. Trò chơi bắt đầu có những chuỗi triệu hồi dài như công thức.

<short pause> Nếu Synchro là phép cộng, Xyz là phép so sánh: không cần cộng, chỉ cần giống nhau. Hai hệ thống sống song song, và người chơi có thêm lựa chọn.

<short pause> Và mỗi lần có phát minh mới, trò chơi lại nhanh hơn. Số quái vật được gọi ra mỗi lượt tăng lên liên tục.

<short pause> Năm 2014, với anime Yu-Gi-Oh! Arc-V, đến lượt triệu hồi Con lắc, Pendulum.

<short pause> Quái vật Pendulum lai giữa quái vật và bài phép. Đặt hai lá vào hai ô đặc biệt, gọi là thang Con lắc, mỗi lá có một con số.

<short pause> Mọi quái vật có cấp nằm giữa hai con số đó đều có thể được triệu hồi cùng một lúc. Không phải một con, mà cả một đàn.

<short pause> Nghĩa là một lá Pendulum vừa là quái vật, vừa có thể làm cột mốc cho thang Con lắc. Một lá bài làm hai việc. Đây là lần đầu tiên loại bài bị xóa nhòa ranh giới như vậy.

<short pause> Và điều đặc biệt: quái vật Pendulum bị đánh bại không vào mộ bài, mà quay về Extra Deck, sẵn sàng được gọi lại lượt sau.

<short pause> Có người chơi gọi thời kỳ này là thời kỳ mọi thứ đều quá nhanh. Có trận kết thúc ngay ở lượt đầu tiên, khi người đi trước dựng một sân đấu mà đối thủ không thể vượt qua.

<short pause> <laugh> Kaku thấy Pendulum là phát minh táo bạo nhất. Nó cho phép số lượng quái vật trên sân tăng vọt, và cũng làm cho việc cân bằng trò chơi khó hơn bao giờ hết.
```

**ElevenLabs**

```text
Tháng ba năm 2011, cùng anime Yu-Gi-Oh! Zexal, lại một phát minh nữa: triệu hồi Xyz, đọc là ích-xít.

[pause] Luật Xyz: lấy hai hay nhiều quái vật có cùng cấp, chồng chúng lên nhau. Quái vật Xyz không có cấp, mà có hạng.

[pause] Những quái vật bên dưới trở thành nguyên liệu. Quái vật Xyz có thể gỡ nguyên liệu ra để dùng hiệu ứng. Nguyên liệu giống như đạn dược.

[pause] Có những quái vật Xyz còn có thể được chồng lên chính một quái vật Xyz khác, tạo thành dạng mạnh hơn. Trò chơi bắt đầu có những chuỗi triệu hồi dài như công thức.

[pause] Nếu Synchro là phép cộng, Xyz là phép so sánh: không cần cộng, chỉ cần giống nhau. Hai hệ thống sống song song, và người chơi có thêm lựa chọn.

[pause] Và mỗi lần có phát minh mới, trò chơi lại nhanh hơn. Số quái vật được gọi ra mỗi lượt tăng lên liên tục.

[pause] Năm 2014, với anime Yu-Gi-Oh! Arc-V, đến lượt triệu hồi Con lắc, Pendulum.

[pause] Quái vật Pendulum lai giữa quái vật và bài phép. Đặt hai lá vào hai ô đặc biệt, gọi là thang Con lắc, mỗi lá có một con số.

[pause] Mọi quái vật có cấp nằm giữa hai con số đó đều có thể được triệu hồi cùng một lúc. Không phải một con, mà cả một đàn.

[pause] Nghĩa là một lá Pendulum vừa là quái vật, vừa có thể làm cột mốc cho thang Con lắc. Một lá bài làm hai việc. Đây là lần đầu tiên loại bài bị xóa nhòa ranh giới như vậy.

[pause] Và điều đặc biệt: quái vật Pendulum bị đánh bại không vào mộ bài, mà quay về Extra Deck, sẵn sàng được gọi lại lượt sau.

[pause] Có người chơi gọi thời kỳ này là thời kỳ mọi thứ đều quá nhanh. Có trận kết thúc ngay ở lượt đầu tiên, khi người đi trước dựng một sân đấu mà đối thủ không thể vượt qua.

[pause] [chuckles] Kaku thấy Pendulum là phát minh táo bạo nhất. Nó cho phép số lượng quái vật trên sân tăng vọt, và cũng làm cho việc cân bằng trò chơi khó hơn bao giờ hết.
```

### c05 · Thời kỳ 6: 2017, Link và luật mới / Sau Link: nhánh rẽ Rush Duel

Khoảng 123 giây · cảnh s54–s64 · 1595 ký tự

**Gemini**

```text
Năm 2017, với anime Yu-Gi-Oh! VRAINS, xuất hiện triệu hồi Liên kết, Link, cùng một thay đổi lớn về luật sân đấu.

<short pause> Luật mới thêm hai ô ở giữa sân, gọi là vùng quái vật Extra. Và từ đó, mỗi người chỉ được gọi một quái vật từ Extra Deck vào vùng giữa đó, trừ khi có quái vật Link chỉ đường.

<short pause> Quái vật Link không có cấp, không có điểm phòng thủ. Thay vào đó, nó có những mũi tên. Mũi tên chỉ vào đâu, ô đó được phép nhận quái vật từ Extra Deck.

<short pause> Luật này là một cú phanh gấp. Nó giới hạn số quái vật Extra Deck mỗi người có thể dùng, để hãm tốc độ mà Synchro, Xyz và Pendulum đã đẩy lên.

<short pause> Cộng đồng tranh cãi rất nhiều. Pendulum bị ảnh hưởng nặng nhất. Và vài năm sau, luật được nới ra một phần, cho phép gọi Fusion, Synchro và Xyz ra sân chính mà không cần mũi tên.

<short pause> Với người chơi mới, Link lại có một lợi ích: nó biến vị trí đặt quái vật thành một câu đố hình học. Ai thích xếp hình sẽ thích Link.

<short pause> Kaku để ý: đây là lần đầu tiên trong lịch sử game, một phát minh mới không làm trò chơi nhanh hơn, mà cố làm nó chậm lại.

<short pause> Từ năm 2020, Konami còn tạo ra một nhánh rẽ: Rush Duel, một kiểu chơi đơn giản và nhanh hơn, gắn với anime Yu-Gi-Oh! Sevens.

<short pause> Trong Rush Duel, mỗi lượt bạn được rút bài cho tới khi đủ năm lá trên tay, và được triệu hồi thường không giới hạn. Nghe thì lạ, nhưng nó làm trò chơi nhanh và vui cho trẻ em.

<short pause> Rush Duel quay về tinh thần ngày xưa: ít luật, dễ hiểu, dành cho người mới. Nó như một lời mời những người đã rời game quay trở lại.

<short pause> Và năm 2022, trò chơi điện tử Yu-Gi-Oh! Master Duel ra đời, cho phép chơi bản đầy đủ trên điện thoại và máy tính. Nhiều người Việt quay lại game nhờ bản này.
```

**ElevenLabs**

```text
Năm 2017, với anime Yu-Gi-Oh! VRAINS, xuất hiện triệu hồi Liên kết, Link, cùng một thay đổi lớn về luật sân đấu.

[pause] Luật mới thêm hai ô ở giữa sân, gọi là vùng quái vật Extra. Và từ đó, mỗi người chỉ được gọi một quái vật từ Extra Deck vào vùng giữa đó, trừ khi có quái vật Link chỉ đường.

[pause] Quái vật Link không có cấp, không có điểm phòng thủ. Thay vào đó, nó có những mũi tên. Mũi tên chỉ vào đâu, ô đó được phép nhận quái vật từ Extra Deck.

[pause] Luật này là một cú phanh gấp. Nó giới hạn số quái vật Extra Deck mỗi người có thể dùng, để hãm tốc độ mà Synchro, Xyz và Pendulum đã đẩy lên.

[pause] Cộng đồng tranh cãi rất nhiều. Pendulum bị ảnh hưởng nặng nhất. Và vài năm sau, luật được nới ra một phần, cho phép gọi Fusion, Synchro và Xyz ra sân chính mà không cần mũi tên.

[pause] Với người chơi mới, Link lại có một lợi ích: nó biến vị trí đặt quái vật thành một câu đố hình học. Ai thích xếp hình sẽ thích Link.

[pause] Kaku để ý: đây là lần đầu tiên trong lịch sử game, một phát minh mới không làm trò chơi nhanh hơn, mà cố làm nó chậm lại.

[pause] Từ năm 2020, Konami còn tạo ra một nhánh rẽ: Rush Duel, một kiểu chơi đơn giản và nhanh hơn, gắn với anime Yu-Gi-Oh! Sevens.

[pause] Trong Rush Duel, mỗi lượt bạn được rút bài cho tới khi đủ năm lá trên tay, và được triệu hồi thường không giới hạn. Nghe thì lạ, nhưng nó làm trò chơi nhanh và vui cho trẻ em.

[pause] Rush Duel quay về tinh thần ngày xưa: ít luật, dễ hiểu, dành cho người mới. Nó như một lời mời những người đã rời game quay trở lại.

[pause] Và năm 2022, trò chơi điện tử Yu-Gi-Oh! Master Duel ra đời, cho phép chơi bản đầy đủ trên điện thoại và máy tính. Nhiều người Việt quay lại game nhờ bản này.
```

### c06 · Mỗi thời kỳ, một nhân vật chính / Vì sao luật cứ thay đổi? / Người chơi cũ nên quay lại thế nào?

Khoảng 144 giây · cảnh s65–s79 · 1877 ký tự

**Gemini**

```text
Có một chi tiết vui mà nhiều người không để ý: gần như mỗi bộ anime Yu-Gi-Oh! mới đều có một nhân vật chính mới, gắn với một cơ chế mới.

<short pause> Yugi với bài truyền thống. Judai của GX với Fusion. Yusei của 5D's với Synchro, đấu bài trên mô tô. Yuma của Zexal với Xyz.

<short pause> Yuya của Arc-V với Pendulum. Yusaku của VRAINS với Link. Và hãy để ý: tên của họ đều bắt đầu bằng âm Yu.

<short pause> Nhờ vậy, mỗi thế hệ người xem có một nhân vật chính của riêng mình, và một cơ chế gắn với tuổi thơ của họ. Hỏi một người chơi thích anime nào, bạn sẽ đoán được họ bao nhiêu tuổi.

<short pause> Nhìn lại, vì sao Yu-Gi-Oh! liên tục thêm phát minh mới? Kaku thấy có ba lý do.

<short pause> Một: mỗi bộ anime mới cần một cơ chế mới để câu chuyện có điểm nhấn, và để bán bộ bài mới.

<short pause> Hai: người chơi lâu năm cần cái mới để không chán. Một trò chơi hai mươi lăm năm tuổi phải liên tục làm mình mới.

<short pause> Ba: cân bằng. Mỗi phát minh làm lệch cán cân, và luật sau phải sửa lại cán cân đó. Link chính là ví dụ rõ nhất.

<short pause> Và mỗi thời kỳ đều có người yêu và người ghét. Có người nói game mất đi sự đơn giản. Có người nói game chưa bao giờ hay như bây giờ. Cả hai đều đúng, theo cách của mình.

<short pause> <laugh> Kaku nghĩ lịch sử Yu-Gi-Oh! giống lịch sử của nhiều công nghệ: mỗi phát minh giải quyết một vấn đề, và tạo ra một vấn đề mới.

<short pause> Nếu bạn rời game ở thời kỳ Fusion và muốn quay lại, đây là gợi ý của Kaku. Bước một: học Synchro và Xyz trước, vì chúng dễ hiểu nhất.

<short pause> Bước hai: học Link, vì nó quyết định cách bạn đặt quái vật trên sân. Bước ba mới là Pendulum, cơ chế phức tạp nhất.

<short pause> Và đừng ngại hỏi. Cộng đồng người chơi Yu-Gi-Oh! ở Việt Nam, trên mạng lẫn ở các cửa hàng bài, thường rất sẵn lòng hướng dẫn người mới và người quay lại.

<short pause> Hoặc bạn có thể thử Rush Duel trước, để làm quen lại với nhịp chơi, rồi mới sang bản đầy đủ.

<short pause> Và quan trọng nhất: tìm một người bạn để chơi cùng. Yu-Gi-Oh! vui nhất không phải khi thắng, mà khi hai người ngồi đối diện nhau, như ngày xưa ở cổng trường.
```

**ElevenLabs**

```text
Có một chi tiết vui mà nhiều người không để ý: gần như mỗi bộ anime Yu-Gi-Oh! mới đều có một nhân vật chính mới, gắn với một cơ chế mới.

[pause] Yugi với bài truyền thống. Judai của GX với Fusion. Yusei của 5D's với Synchro, đấu bài trên mô tô. Yuma của Zexal với Xyz.

[pause] Yuya của Arc-V với Pendulum. Yusaku của VRAINS với Link. Và hãy để ý: tên của họ đều bắt đầu bằng âm Yu.

[pause] Nhờ vậy, mỗi thế hệ người xem có một nhân vật chính của riêng mình, và một cơ chế gắn với tuổi thơ của họ. Hỏi một người chơi thích anime nào, bạn sẽ đoán được họ bao nhiêu tuổi.

[pause] Nhìn lại, vì sao Yu-Gi-Oh! [curious] liên tục thêm phát minh mới? Kaku thấy có ba lý do.

[pause] Một: mỗi bộ anime mới cần một cơ chế mới để câu chuyện có điểm nhấn, và để bán bộ bài mới.

[pause] Hai: người chơi lâu năm cần cái mới để không chán. Một trò chơi hai mươi lăm năm tuổi phải liên tục làm mình mới.

[pause] Ba: cân bằng. Mỗi phát minh làm lệch cán cân, và luật sau phải sửa lại cán cân đó. Link chính là ví dụ rõ nhất.

[pause] Và mỗi thời kỳ đều có người yêu và người ghét. Có người nói game mất đi sự đơn giản. Có người nói game chưa bao giờ hay như bây giờ. Cả hai đều đúng, theo cách của mình.

[pause] [chuckles] Kaku nghĩ lịch sử Yu-Gi-Oh! giống lịch sử của nhiều công nghệ: mỗi phát minh giải quyết một vấn đề, và tạo ra một vấn đề mới.

[pause] Nếu bạn rời game ở thời kỳ Fusion và muốn quay lại, đây là gợi ý của Kaku. Bước một: học Synchro và Xyz trước, vì chúng dễ hiểu nhất.

[pause] Bước hai: học Link, vì nó quyết định cách bạn đặt quái vật trên sân. Bước ba mới là Pendulum, cơ chế phức tạp nhất.

[pause] Và đừng ngại hỏi. Cộng đồng người chơi Yu-Gi-Oh! ở Việt Nam, trên mạng lẫn ở các cửa hàng bài, thường rất sẵn lòng hướng dẫn người mới và người quay lại.

[pause] Hoặc bạn có thể thử Rush Duel trước, để làm quen lại với nhịp chơi, rồi mới sang bản đầy đủ.

[pause] Và quan trọng nhất: tìm một người bạn để chơi cùng. Yu-Gi-Oh! vui nhất không phải khi thắng, mà khi hai người ngồi đối diện nhau, như ngày xưa ở cổng trường.
```

### c07 · Đường thời gian thu gọn / Kết

Khoảng 71 giây · cảnh s80–s86 · 923 ký tự

**Gemini**

```text
Và đây là đường thời gian thu gọn. 1999: luật nền, Fusion và Ritual. 2002: bản tiếng Anh ra thế giới.

<short pause> 2008: Synchro, phép cộng. 2011: Xyz, phép so sánh. 2014: Pendulum, triệu hồi cả đàn.

<short pause> 2017: Link và vùng quái vật Extra, cú phanh gấp. 2020: Rush Duel, lối vào cho người mới. 2022: Master Duel, trò chơi bài trên điện thoại.

<short pause> Bạn đã rời game ở thời kỳ nào? Và bạn nhớ nhất lá bài nào của tuổi thơ? Viết vào bình luận nhé, Kaku rất muốn biết.

<short pause> Từ một trò chơi trong truyện tranh, Yu-Gi-Oh! trở thành trò chơi bài bán chạy nhất thế giới, và liên tục thay đổi suốt hơn hai mươi lăm năm. <short pause> Nhưng cảm giác rút một lá bài và hy vọng thì vẫn như ngày xưa.

<short pause> Video tiếp theo, Kaku quay về một bộ đang phát sóng: Black Clover, và các dạng Ác ma hợp thể của Asta, từ lần đầu tới dạng mạnh nhất.

<short pause> Nếu video này gợi lại tuổi thơ của bạn, hãy đăng ký kênh, và gửi video cho người bạn từng đấu bài với bạn ở cổng trường. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và đây là đường thời gian thu gọn. 1999: luật nền, Fusion và Ritual. 2002: bản tiếng Anh ra thế giới.

[pause] 2008: Synchro, phép cộng. 2011: Xyz, phép so sánh. 2014: Pendulum, triệu hồi cả đàn.

[pause] 2017: Link và vùng quái vật Extra, cú phanh gấp. 2020: Rush Duel, lối vào cho người mới. 2022: Master Duel, trò chơi bài trên điện thoại.

[pause] [curious] Bạn đã rời game ở thời kỳ nào? Và bạn nhớ nhất lá bài nào của tuổi thơ? Viết vào bình luận nhé, Kaku rất muốn biết.

[pause] Từ một trò chơi trong truyện tranh, Yu-Gi-Oh! trở thành trò chơi bài bán chạy nhất thế giới, và liên tục thay đổi suốt hơn hai mươi lăm năm. [pause] Nhưng cảm giác rút một lá bài và hy vọng thì vẫn như ngày xưa.

[pause] Video tiếp theo, Kaku quay về một bộ đang phát sóng: Black Clover, và các dạng Ác ma hợp thể của Asta, từ lần đầu tới dạng mạnh nhất.

[pause] Nếu video này gợi lại tuổi thơ của bạn, hãy đăng ký kênh, và gửi video cho người bạn từng đấu bài với bạn ở cổng trường. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
