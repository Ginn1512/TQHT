# Bộ prompt · Mob Psycho 100: Từ 1% đến 100% — khi sức mạnh là cảm xúc

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 8 đoạn đọc, khoảng 15.0 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói tới hết anime Mob Psycho 100, cả ba mùa, cũng là hết câu chuyện gốc. Nếu bạn…

```text
Wide 16:9 landscape cinematic frame. a cozy living room decorated for the lunar new year with a small TV and a closed notebook on the table, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Chúc mừng năm mới! Năm mới người ta hay chúc nhau sức khỏe, tiền tài, may mắn. Hôm nay Kaku muốn nói về một t…

```text
Wide 16:9 landscape cinematic frame. red lucky envelopes and a plate of candied fruit on a wooden table beside a small handwritten card, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Hãy tưởng tượng một cậu bé mười bốn tuổi có sức mạnh siêu nhiên mạnh nhất thế giới. Cậu có thể bẻ cong kim lo…

```text
Wide 16:9 landscape cinematic frame. a quiet schoolboy silhouette standing in an empty street while bent street signs and floating pebbles hover around him, wide shot, eerie calm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Vậy mà điều cậu muốn nhất lại là chạy nhanh hơn một chút, nói chuyện tự nhiên hơn một chút, và được cô bạn cù…

```text
Wide 16:9 landscape cinematic frame. a thin boy panting at the end of a running track, hands on his knees, a distant group of students chatting, wide shot, soft late afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Cậu tên là Kageyama Shigeo, biệt danh Mob. Và bộ truyện của cậu có một con số rất lạ ở ngay trong tên: một tr…

```text
Wide 16:9 landscape cinematic frame. a large number one hundred painted in bold brush strokes on white paper with a tiny percent sign beside it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay, ngày đầu năm, Kaku vẽ chân dung một cậu bé qua sức mạnh của cậu. Cuối vi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny festive scarf, holding a paintbrush over a blank portrait canvas. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Ai là Mob?

Lời: Mob Psycho 100 là truyện của ONE, cũng là tác giả One Punch Man. Truyện bắt đầu đăng trên mạng từ tháng tư nă…

```text
Wide 16:9 landscape cinematic frame. a laptop showing a simple hand-drawn webcomic page beside a stack of anime DVD cases, close-up, cozy desk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Biệt danh Mob nghĩa là nhân vật quần chúng, kiểu người đứng ở phía sau trong mọi bức ảnh lớp. Và đó đúng là S…

```text
Wide 16:9 landscape cinematic frame. a class photo with many smiling students and one quiet boy half hidden at the edge of the back row, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Nhưng Mob là người có năng lực siêu nhiên mạnh nhất trong truyện. Những người khác cũng có năng lực, nhưng kh…

```text
Wide 16:9 landscape cinematic frame. a small figure standing in front of an enormous swirling vortex of energy that towers over a city skyline, wide shot, dramatic purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Trong nhà, Mob là một người anh hiền lành. Ở trường, cậu là học sinh chẳng ai để ý. Chỉ khi gặp những linh hồ…

```text
Wide 16:9 landscape cinematic frame. a boy quietly washing dishes at a family kitchen sink while a faint glow flickers around his fingertips unnoticed, medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Cậu làm thêm cho một văn phòng tư vấn tâm linh, dưới quyền một người đàn ông tên Reigen Arataka, tự xưng là n…

```text
Wide 16:9 landscape cinematic frame. a small shabby office with a hand-painted sign on the door, a cheap desk and a single potted plant, wide shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Điều buồn cười là Reigen không có chút năng lực siêu nhiên nào. Và Mob làm việc cho ông với mức lương rất thấ…

```text
Wide 16:9 landscape cinematic frame. a tiny paper envelope with a few coins on a desk, a small handwritten receipt beside it, extreme close-up, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Mob còn tự tham gia câu lạc bộ Cải thiện Cơ thể, toàn những anh chàng cơ bắp. Cậu muốn tự mạnh lên, không nhờ…

```text
Wide 16:9 landscape cinematic frame. a group of muscular students jogging in formation past a school gate at sunrise, a skinny boy trailing behind them, wide shot, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy chỉ riêng những chi tiết này đã đủ vẽ nên một người: có sức mạnh lớn nhất, nhưng chọn con đường khó…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sketching a small figure climbing a steep hill while an easy elevator stands unused beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Chiếc đồng hồ cảm xúc

Lời: Giờ tới chi tiết đặc biệt nhất của bộ truyện: con số phần trăm. Trên màn hình thỉnh thoảng hiện một bộ đếm, t…

```text
Wide 16:9 landscape cinematic frame. a glowing percentage counter floating in dark space, the numbers rising from single digits, close-up, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Bộ đếm này đo cảm xúc bị dồn nén của Mob. Mỗi lần cậu bị trêu chọc, bị ép, bị tổn thương mà không nói ra, con…

```text
Wide 16:9 landscape cinematic frame. a glass jar slowly filling with swirling colored smoke on a school desk, close-up, soft ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Khi chạm một trăm phần trăm, cảm xúc bùng nổ. Và sức mạnh siêu nhiên của Mob bùng nổ theo, gắn với đúng cảm x…

```text
Wide 16:9 landscape cinematic frame. the glass jar cracking with light and colored smoke bursting outward, dynamic close-up, explosive bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Anime còn cho người xem thấy bộ đếm ngay trên màn hình. Mỗi lần con số hiện lên, người xem tự đếm theo, và hồ…

```text
Wide 16:9 landscape cinematic frame. a TV screen in a dark room showing a glowing percentage number, silhouettes of viewers leaning forward on a couch, wide shot, tense cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nghĩa là trong Mob Psycho 100, sức mạnh không đo bằng cấp độ hay chiêu thức. Nó đo bằng cảm xúc. Sức mạnh lớn…

```text
Wide 16:9 landscape cinematic frame. a comparison drawn on parchment: a ladder of levels crossed out, replaced by a heart with a percentage meter inside, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Đây là một ẩn dụ rất đẹp cho tuổi dậy thì. Ai cũng từng có lúc dồn nén quá lâu, rồi một ngày bùng lên vì một…

```text
Wide 16:9 landscape cinematic frame. a teenager sitting alone on a staircase with headphones on, a crumpled test paper beside him, medium shot, moody evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kaku để ý: bộ đếm không bao giờ đo năng lực của Mob. Nó chỉ đo khoảng cách giữa cái Mob cảm thấy và cái Mob d…

```text
Wide 16:9 landscape cinematic frame. two parallel lines drawn on a notebook page with a widening gap between them labeled with a small heart icon, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và câu hỏi lớn của truyện là: liệu Mob có thể sống mà không cần chạm tới một trăm phần trăm? Liệu cậu có thể…

```text
Wide 16:9 landscape cinematic frame. a percentage meter frozen at a calm low number with a small sprout growing beside it, symbolic close-up, gentle morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Vì sao Mob kìm nén?

Lời: Vì sao một cậu bé lại khóa chặt cảm xúc như vậy? Câu trả lời nằm ở tuổi thơ.

```text
Wide 16:9 landscape cinematic frame. an old family photo album lying open on a table with a faded childhood picture, close-up, soft nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Khi còn nhỏ, có lần Mob mất kiểm soát sức mạnh, và vô tình làm em trai Ritsu bị thương. Từ đó, cậu sợ chính m…

```text
Wide 16:9 landscape cinematic frame. a small child staring at his own trembling hands in a dim room, a toy lying broken on the floor, close-up, cold melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Mob tự đặt ra cho mình một luật: không dùng sức mạnh để làm hại người khác, và không để cảm xúc điều khiển mì…

```text
Wide 16:9 landscape cinematic frame. a small handwritten rule card pinned above a child's desk, slightly faded with age, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nghe thì trưởng thành. Nhưng cách cậu làm là tắt hết cảm xúc. Không vui quá, không buồn quá, không giận quá.…

```text
Wide 16:9 landscape cinematic frame. a volume knob turned all the way down on an old radio while a faint glow builds inside the speaker, extreme close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là chỗ bộ truyện rất thật. Nhiều người lớn lên cũng tin rằng kìm nén là mạnh mẽ. Nhưng cảm xúc…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tightly sealed lunchbox that is bulging and about to pop open, looking worried. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Và Mob cũng tin một điều khác nữa: năng lực siêu nhiên không làm cậu đặc biệt hơn ai. Nó chỉ là một khả năng,…

```text
Wide 16:9 landscape cinematic frame. a row of small icons on parchment: a running shoe, a book, a paintbrush, and a floating spoon, all the same size, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Những kiểu 100%

Lời: Điều thú vị nhất: mỗi lần chạm một trăm phần trăm, Mob bùng nổ theo một cảm xúc khác nhau. Và sức mạnh mang m…

```text
Wide 16:9 landscape cinematic frame. a row of several glass jars each filled with a different colored glowing smoke, still life, dramatic light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Có lúc là tức giận, khi cậu thấy người khác bị làm hại. Sức mạnh khi đó dữ dội, muốn phá hủy mọi thứ trước mặ…

```text
Wide 16:9 landscape cinematic frame. a jar of swirling crimson smoke with small cracks spreading through the glass, dramatic close-up, harsh red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Có lúc là buồn bã. Sức mạnh khi đó không tấn công, mà lan ra như một làn sóng nặng nề, khiến mọi thứ xung qua…

```text
Wide 16:9 landscape cinematic frame. a jar of slow heavy deep blue smoke sinking downward, close-up, melancholy blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Có lúc là lòng dũng cảm, hay lòng biết ơn. Sức mạnh khi đó sáng và ấm, dùng để bảo vệ chứ không để phá hủy.

```text
Wide 16:9 landscape cinematic frame. a jar of bright golden smoke glowing warmly and lighting up the table around it, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nghĩa là sức mạnh của Mob không tốt, không xấu. Nó chỉ khuếch đại cái đang có trong tim cậu. Giống như một ch…

```text
Wide 16:9 landscape cinematic frame. an old loudspeaker on a pole with different colored sound waves coming out of it, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Đây là lý do Kaku chọn Mob cho video Tết. Truyện nói rằng điều quan trọng không phải là bạn mạnh cỡ nào, mà l…

```text
Wide 16:9 landscape cinematic frame. a small heart-shaped lantern glowing among festive red decorations, close-up, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Kaku rất thích cách anime thể hiện những khoảnh khắc này: màu sắc, nét vẽ, cả phong cách hình thay đổi theo t…

```text
Wide 16:9 landscape cinematic frame. an animator's desk with several sketches of swirling energy in different art styles pinned side by side, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · ???%: phần bị giấu kín

Lời: Nhưng có một trạng thái đáng sợ hơn một trăm phần trăm. Bộ đếm không hiện số, chỉ hiện ba dấu hỏi.

```text
Wide 16:9 landscape cinematic frame. a glowing counter display showing three question marks instead of numbers, flickering in darkness, extreme close-up, eerie white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Trạng thái này thường xuất hiện khi Mob bất tỉnh. Cậu không còn tỉnh táo, và sức mạnh tự hành động, mạnh hơn…

```text
Wide 16:9 landscape cinematic frame. a boy lying unconscious on the ground while a huge swirl of white energy rises above him, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nhiều người xem hiểu ???% là phần sâu nhất của Mob: tất cả những cảm xúc cậu đã khóa lại suốt nhiều năm, giờ…

```text
Wide 16:9 landscape cinematic frame. a locked wooden chest at the bottom of a dark basement with light leaking out from the seams, close-up, eerie glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Trong mùa cuối, phần bị giấu kín đó mất kiểm soát, và trở thành mối nguy lớn nhất của câu chuyện. Không có kẻ…

```text
Wide 16:9 landscape cinematic frame. a colossal swirling storm of white energy rising over a city at night, tiny figures looking up from rooftops, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku thấy đây là một ý tưởng rất dũng cảm của tác giả. Trận cuối không phải là đánh bại một phản diện, mà là…

```text
Wide 16:9 landscape cinematic frame. a boy standing in front of a mirror that reflects a glowing version of himself, symbolic medium shot, soft dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Người thầy không có năng lực: Reigen

Lời: Giờ tới nhân vật quan trọng thứ hai trong chân dung của Mob: Reigen. Một người lừa đảo, không có năng lực, nó…

```text
Wide 16:9 landscape cinematic frame. a man in a plain suit confidently pointing at a whiteboard covered in scribbled diagrams in a cheap office, medium shot, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nhưng Reigen dạy Mob những điều không siêu năng lực nào dạy được: cách đối xử với người khác, cách nhìn một v…

```text
Wide 16:9 landscape cinematic frame. a man and a boy sitting side by side on a park bench eating street food, the man gesturing as he talks, medium shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Reigen từng nói với Mob, đại ý: gặp chuyện mình không thích thì bỏ chạy cũng được. Với một cậu bé luôn cố chị…

```text
Wide 16:9 landscape cinematic frame. an open door at the end of a dark hallway with warm light spilling through, symbolic wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Reigen cũng không bao giờ coi Mob là vũ khí. Với ông, Mob là một đứa trẻ. Ông muốn Mob có bạn bè, có câu lạc…

```text
Wide 16:9 landscape cinematic frame. a man ruffling a boy's hair outside a school gate as other students walk by, medium shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Và mối quan hệ này đi theo cả hai chiều. Mob thấy Reigen nói dối, nhưng cũng thấy Reigen thật lòng. Có lúc Mo…

```text
Wide 16:9 landscape cinematic frame. a boy walking away down a street as a man watches from a doorway, both glancing back, wide shot, bittersweet dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ Reigen là một trong những người thầy hay nhất trong anime. Ông không mạnh, không hoàn hảo, nhưng ôn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small trophy labeled with a heart and handing it to an empty office chair. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Ritsu: người em muốn có năng lực

Lời: Một nhân vật nữa giúp ta hiểu Mob: em trai Ritsu. Ritsu là học sinh giỏi, được thầy cô quý, là hội viên hội h…

```text
Wide 16:9 landscape cinematic frame. a neat student desk with stacks of perfect test papers and a student council badge, close-up, clean bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Nhưng Ritsu lại ghen tị với anh. Cậu muốn có năng lực siêu nhiên như Mob, vì trong mắt cậu, đó là thứ duy nhấ…

```text
Wide 16:9 landscape cinematic frame. a younger boy watching through a doorway as a floating spoon hovers above his older brother's hand, medium shot, wistful evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Khi Ritsu thức tỉnh năng lực, cậu vui, nhưng cũng bắt đầu đi sai đường. Năng lực không làm Ritsu hạnh phúc hơ…

```text
Wide 16:9 landscape cinematic frame. a boy staring at his own glowing hands in a dark room with a conflicted expression, close-up, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Hai anh em là hai mặt của một câu hỏi: người có năng lực muốn bình thường, người bình thường muốn có năng lực…

```text
Wide 16:9 landscape cinematic frame. two brothers sitting back to back on the floor of a shared bedroom, one holding a textbook and one holding a floating pebble, wide shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Dimple: linh hồn đồng hành

Lời: Còn một người bạn đồng hành rất lạ: một linh hồn tên Dimple. Ban đầu Dimple muốn chiếm cơ thể Mob để trở thàn…

```text
Wide 16:9 landscape cinematic frame. a small mischievous wisp of green light floating over a boy's shoulder in a quiet street, medium shot, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Thay vì biến mất, Dimple ở lại bên Mob, nói là để chờ cơ hội. Nhưng dần dần, linh hồn này trở thành một người…

```text
Wide 16:9 landscape cinematic frame. a boy walking home from school with a tiny floating light bobbing beside him, back view, wide shot, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: từ kẻ muốn lợi dụng sức mạnh của Mob, Dimple trở thành một trong những người hiểu Mob nhất. Một lầ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sharing a small snack with a tiny floating wisp of light, both looking content. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Những người có sức mạnh và lạc lối

Lời: Để hiểu Mob, hãy nhìn những người có năng lực khác trong truyện. Nhiều người trong số họ tin rằng năng lực kh…

```text
Wide 16:9 landscape cinematic frame. a small group of silhouettes standing on a raised stage above a crowd, arms raised arrogantly, wide shot, harsh spotlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Có một cậu học sinh tên Teru, người dùng năng lực để làm trùm trường. Khi gặp Mob, cậu thua, và lần đầu tiên…

```text
Wide 16:9 landscape cinematic frame. a proud boy's silhouette on a school rooftop, his shadow shrinking as the sun sets, wide shot, dramatic dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Có cả một tổ chức gồm những người có năng lực muốn thống trị thế giới. Họ tin người có năng lực phải đứng trê…

```text
Wide 16:9 landscape cinematic frame. a sinister corporate tower at night with glowing windows and a large symbol on its top floor, wide shot, cold ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Mob thì ngược lại. Cậu mạnh nhất, nhưng tin rằng năng lực chỉ là một đặc điểm, như chiều cao hay màu tóc. Cậu…

```text
Wide 16:9 landscape cinematic frame. a boy standing at ground level among ordinary people on a busy crosswalk, blending in, wide shot, bright everyday light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Chính niềm tin đó khiến Mob thay đổi được nhiều người. Cậu không đánh bại họ bằng sức mạnh, mà bằng cách cho…

```text
Wide 16:9 landscape cinematic frame. several hands reaching out to help a fallen figure stand up in an empty schoolyard, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Câu lạc bộ Cải thiện Cơ thể

Lời: Có một nhóm nhân vật Kaku rất thích: câu lạc bộ Cải thiện Cơ thể. Những anh chàng to cao, cơ bắp, nhìn thì đá…

```text
Wide 16:9 landscape cinematic frame. a group of large muscular students cheering loudly on the side of a running track, wide shot, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Mob là thành viên yếu nhất. Chạy chậm nhất, hụt hơi nhanh nhất. Nhưng không ai chê cậu. Họ chờ cậu, cổ vũ cậu…

```text
Wide 16:9 landscape cinematic frame. a skinny boy struggling to finish a lap while a line of big students waits at the finish line clapping, wide shot, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Điều thú vị là các anh chàng này không có năng lực siêu nhiên nào. Nhưng với Mob, họ là những người đầu tiên…

```text
Wide 16:9 landscape cinematic frame. a group of students sharing drinks and laughing on a school bench after practice, medium shot, golden hour light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và trong trận cuối, khi Mob mất kiểm soát, họ cũng có mặt. Không phải để chiến đấu, mà để nói với cậu rằng họ…

```text
Wide 16:9 landscape cinematic frame. a line of big silhouettes standing firmly together against a swirling storm of light, wide shot, determined warm backlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Có một câu nói của đội trưởng câu lạc bộ mà nhiều người nhớ, đại ý: cơ thể không lừa dối ai. Mỗi bước chạy th…

```text
Wide 16:9 landscape cinematic frame. a worn training notebook open to a page with a running log and small checkmarks, close-up, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Kaku nghĩ đây là thông điệp giản dị nhất của truyện: đôi khi người giúp bạn nhiều nhất không phải người mạnh…

```text
Wide 16:9 landscape cinematic frame. a pair of running shoes placed side by side with a much bigger pair on a locker room bench, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Cái kết: một trăm phần trăm chính mình

Lời: Tới mùa cuối, Mob quyết định làm một việc rất bình thường mà rất khó: nói ra tình cảm với cô bạn thời thơ ấu,…

```text
Wide 16:9 landscape cinematic frame. a boy holding a small handwritten letter standing at a school gate in the evening, nervous posture, medium shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nỗi sợ bị từ chối khiến bộ đếm tăng vọt, và phần bị giấu kín của Mob bùng nổ thành một cơn bão khổng lồ phủ l…

```text
Wide 16:9 landscape cinematic frame. a gigantic swirling storm of white energy engulfing a city skyline at night, tiny lights flickering below, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Những người quanh Mob lần lượt tới: em trai, thầy Reigen, bạn bè, cả những người từng là đối thủ. Họ không tớ…

```text
Wide 16:9 landscape cinematic frame. many small figures walking toward the center of a storm, each holding a small lantern, wide shot, warm lights against cold storm. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Và Mob gặp chính mình, phần cảm xúc cậu đã giấu suốt bao năm. Cậu không tiêu diệt nó. Cậu chấp nhận nó, như m…

```text
Wide 16:9 landscape cinematic frame. a boy embracing a glowing reflection of himself in the eye of a calming storm, symbolic wide shot, soft radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Cậu vẫn đi gặp Tsubomi. Lời tỏ tình không được đáp lại như cậu mong. Nhưng cậu không bùng nổ. Cậu buồn, và cậ…

```text
Wide 16:9 landscape cinematic frame. a boy walking home alone under streetlights with a small calm smile despite teary eyes, wide shot, gentle evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hãy so sánh với mùa một: một cậu bé giấu mọi cảm xúc sau gương mặt không biểu cảm. Tới mùa cuối, cậu khóc, cậ…

```text
Wide 16:9 landscape cinematic frame. two small portrait sketches side by side on parchment, one with a blank expression and one with a tearful smile, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Kaku thấy đây là cái kết đẹp nhất có thể. Mob không thắng tình yêu, nhưng thắng được nỗi sợ cảm xúc của chính…

```text
Wide 16:9 landscape cinematic frame. a percentage counter gently fading away into warm morning light, symbolic close-up, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và thầy Reigen có mặt ở đó, như mọi lần, để mời Mob đi ăn. Một cái kết nhỏ, bình thường, đúng như điều Mob mo…

```text
Wide 16:9 landscape cinematic frame. a man and a boy sitting at a small ramen stall at night, steam rising from two bowls, wide shot, warm cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Bài học cho năm mới

Lời: Vậy Mob Psycho 100 muốn nói gì với chúng ta, trong ngày đầu năm?

```text
Wide 16:9 landscape cinematic frame. a small notebook open to a blank page titled with a new year's date, a pen beside it, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Một: cảm xúc không phải là điểm yếu. Giận, buồn, sợ, vui, tất cả đều là một phần của bạn. Khóa chúng lại khôn…

```text
Wide 16:9 landscape cinematic frame. a set of colorful paper lanterns hanging in a row, each a different color, wide shot, warm festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Hai: năng lực, tài năng, hay bất cứ điều gì bạn giỏi, không làm bạn cao hơn người khác. Nó chỉ là một phần củ…

```text
Wide 16:9 landscape cinematic frame. a small trophy placed on the same shelf as a teacup and a houseplant, all equally sized, still life, soft light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Ba: hãy tìm những người như Reigen và câu lạc bộ cơ bắp. Những người không cần bạn mạnh, chỉ cần bạn là chính…

```text
Wide 16:9 landscape cinematic frame. a family and friends gathered around a festive table sharing food and laughing, wide shot, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bốn: đừng so sánh mình với người khác theo kiểu ai có năng lực hơn. Mob và Ritsu, mỗi người đều có giá trị ri…

```text
Wide 16:9 landscape cinematic frame. two different potted plants of different heights growing side by side on a windowsill, both blooming, still life, soft morning light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đề nghị một thử thách nhỏ cho năm mới: hãy nói ra một cảm xúc bạn đã giữ quá lâu. Một lời cảm ơn, một lờ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot handing a small red envelope with a heart drawn on it toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Chân dung trong một câu

Lời: Và giờ, Kaku tóm cả con người Mob trong đúng một câu, như đã hứa ở đầu video.

```text
Wide 16:9 landscape cinematic frame. a finished portrait canvas turned away from the viewer on an easel, a paintbrush resting on the ledge, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Mob không phải người mạnh nhất học cách kiểm soát sức mạnh. Mob là người học cách không cần sức mạnh để được…

```text
Wide 16:9 landscape cinematic frame. a quiet boy standing in an ordinary sunny street, arms relaxed, a calm smile, no glowing effects around him, wide shot, bright gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Nếu năm nay bạn chỉ xem một bộ anime cùng gia đình, Kaku gợi ý Mob Psycho 100. Nó hài hước, nó đẹp, và nó để…

```text
Wide 16:9 landscape cinematic frame. a family sitting together on a couch under a blanket watching TV with snacks and tea, back view, wide shot, cozy festive light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku gỡ mười hiểu lầm phổ biến nhất về One Piece, đúng lúc bản làm lại chuẩn bị ra mắt. Có h…

```text
Wide 16:9 landscape cinematic frame. a small straw-colored treasure map with ten red X marks drawn across it, close-up, warm adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chúc bạn một năm mới thật nhiều cảm xúc tốt, và đủ can đảm để nói ra cả những cảm xúc khó. Đăng ký kênh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing deeply with a festive scarf and holding a small lantern. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 70 giây · cảnh s01–s06 · 910 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime Mob Psycho 100, cả ba mùa, cũng là hết câu chuyện gốc. Nếu bạn định xem trong kỳ nghỉ Tết, hãy lưu video lại, xem xong rồi quay lại với Kaku.

<short pause> Chúc mừng năm mới! Năm mới người ta hay chúc nhau sức khỏe, tiền tài, may mắn. Hôm nay Kaku muốn nói về một thứ ít ai chúc nhau: được sống thật với cảm xúc của mình.

<short pause> Hãy tưởng tượng một cậu bé mười bốn tuổi có sức mạnh siêu nhiên mạnh nhất thế giới. Cậu có thể bẻ cong kim loại, bay lên trời, đánh tan cả những linh hồn ác độc nhất.

<short pause> Vậy mà điều cậu muốn nhất lại là chạy nhanh hơn một chút, nói chuyện tự nhiên hơn một chút, và được cô bạn cùng lớp để ý.

<short pause> Cậu tên là Kageyama Shigeo, biệt danh Mob. Và bộ truyện của cậu có một con số rất lạ ở ngay trong tên: một trăm.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay, ngày đầu năm, Kaku vẽ chân dung một cậu bé qua sức mạnh của cậu. Cuối video, Kaku tóm cả con người Mob trong đúng một câu.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime Mob Psycho 100, cả ba mùa, cũng là hết câu chuyện gốc. Nếu bạn định xem trong kỳ nghỉ Tết, hãy lưu video lại, xem xong rồi quay lại với Kaku.

[pause] Chúc mừng năm mới! Năm mới người ta hay chúc nhau sức khỏe, tiền tài, may mắn. Hôm nay Kaku muốn nói về một thứ ít ai chúc nhau: được sống thật với cảm xúc của mình.

[pause] Hãy tưởng tượng một cậu bé mười bốn tuổi có sức mạnh siêu nhiên mạnh nhất thế giới. Cậu có thể bẻ cong kim loại, bay lên trời, đánh tan cả những linh hồn ác độc nhất.

[pause] Vậy mà điều cậu muốn nhất lại là chạy nhanh hơn một chút, nói chuyện tự nhiên hơn một chút, và được cô bạn cùng lớp để ý.

[pause] Cậu tên là Kageyama Shigeo, biệt danh Mob. Và bộ truyện của cậu có một con số rất lạ ở ngay trong tên: một trăm.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay, ngày đầu năm, Kaku vẽ chân dung một cậu bé qua sức mạnh của cậu. Cuối video, Kaku tóm cả con người Mob trong đúng một câu.
```

### c02 · Ai là Mob?

Khoảng 96 giây · cảnh s07–s14 · 1250 ký tự

**Gemini**

```text
Mob Psycho 100 là truyện của ONE, cũng là tác giả One Punch Man. Truyện bắt đầu đăng trên mạng từ tháng tư năm 2012, và studio Bones làm anime ba mùa: 2016, 2019 và 2022.

<short pause> Biệt danh Mob nghĩa là nhân vật quần chúng, kiểu người đứng ở phía sau trong mọi bức ảnh lớp. Và đó đúng là Shigeo: ít nói, ít biểu cảm, học bình thường, thể thao kém.

<short pause> Nhưng Mob là người có năng lực siêu nhiên mạnh nhất trong truyện. Những người khác cũng có năng lực, nhưng không ai đến gần được sức mạnh của cậu.

<short pause> Trong nhà, Mob là một người anh hiền lành. Ở trường, cậu là học sinh chẳng ai để ý. Chỉ khi gặp những linh hồn ác, người ta mới thấy sức mạnh thật của cậu, và cậu cũng không muốn ai thấy.

<short pause> Cậu làm thêm cho một văn phòng tư vấn tâm linh, dưới quyền một người đàn ông tên Reigen Arataka, tự xưng là nhà ngoại cảm vĩ đại nhất thế kỷ hai mươi mốt.

<short pause> Điều buồn cười là Reigen không có chút năng lực siêu nhiên nào. Và Mob làm việc cho ông với mức lương rất thấp. <short pause> Nhưng như Kaku sẽ kể, đó là quyết định đúng nhất đời cậu.

<short pause> Mob còn tự tham gia câu lạc bộ Cải thiện Cơ thể, toàn những anh chàng cơ bắp. Cậu muốn tự mạnh lên, không nhờ tới năng lực.

<short pause> <laugh> Kaku thấy chỉ riêng những chi tiết này đã đủ vẽ nên một người: có sức mạnh lớn nhất, nhưng chọn con đường khó nhất để trở nên tốt hơn.
```

**ElevenLabs**

```text
Mob Psycho 100 là truyện của ONE, cũng là tác giả One Punch Man. Truyện bắt đầu đăng trên mạng từ tháng tư năm 2012, và studio Bones làm anime ba mùa: 2016, 2019 và 2022.

[pause] Biệt danh Mob nghĩa là nhân vật quần chúng, kiểu người đứng ở phía sau trong mọi bức ảnh lớp. Và đó đúng là Shigeo: ít nói, ít biểu cảm, học bình thường, thể thao kém.

[pause] Nhưng Mob là người có năng lực siêu nhiên mạnh nhất trong truyện. Những người khác cũng có năng lực, nhưng không ai đến gần được sức mạnh của cậu.

[pause] Trong nhà, Mob là một người anh hiền lành. Ở trường, cậu là học sinh chẳng ai để ý. Chỉ khi gặp những linh hồn ác, người ta mới thấy sức mạnh thật của cậu, và cậu cũng không muốn ai thấy.

[pause] Cậu làm thêm cho một văn phòng tư vấn tâm linh, dưới quyền một người đàn ông tên Reigen Arataka, tự xưng là nhà ngoại cảm vĩ đại nhất thế kỷ hai mươi mốt.

[pause] Điều buồn cười là Reigen không có chút năng lực siêu nhiên nào. Và Mob làm việc cho ông với mức lương rất thấp. [pause] Nhưng như Kaku sẽ kể, đó là quyết định đúng nhất đời cậu.

[pause] Mob còn tự tham gia câu lạc bộ Cải thiện Cơ thể, toàn những anh chàng cơ bắp. Cậu muốn tự mạnh lên, không nhờ tới năng lực.

[pause] [chuckles] Kaku thấy chỉ riêng những chi tiết này đã đủ vẽ nên một người: có sức mạnh lớn nhất, nhưng chọn con đường khó nhất để trở nên tốt hơn.
```

### c03 · Chiếc đồng hồ cảm xúc / Vì sao Mob kìm nén?

Khoảng 142 giây · cảnh s15–s28 · 1845 ký tự

**Gemini**

```text
Giờ tới chi tiết đặc biệt nhất của bộ truyện: con số phần trăm. Trên màn hình thỉnh thoảng hiện một bộ đếm, từ vài phần trăm tăng dần lên.

<short pause> Bộ đếm này đo cảm xúc bị dồn nén của Mob. Mỗi lần cậu bị trêu chọc, bị ép, bị tổn thương mà không nói ra, con số lại tăng lên.

<short pause> Khi chạm một trăm phần trăm, cảm xúc bùng nổ. Và sức mạnh siêu nhiên của Mob bùng nổ theo, gắn với đúng cảm xúc đó.

<short pause> Anime còn cho người xem thấy bộ đếm ngay trên màn hình. Mỗi lần con số hiện lên, người xem tự đếm theo, và hồi hộp chờ xem điều gì sẽ khiến nó chạm một trăm.

<short pause> Nghĩa là trong Mob Psycho 100, sức mạnh không đo bằng cấp độ hay chiêu thức. Nó đo bằng cảm xúc. Sức mạnh lớn nhất xuất hiện khi cậu không còn kìm nén được nữa.

<short pause> Đây là một ẩn dụ rất đẹp cho tuổi dậy thì. Ai cũng từng có lúc dồn nén quá lâu, rồi một ngày bùng lên vì một chuyện rất nhỏ.

<short pause> Kaku để ý: bộ đếm không bao giờ đo năng lực của Mob. Nó chỉ đo khoảng cách giữa cái Mob cảm thấy và cái Mob dám thể hiện.

<short pause> Và câu hỏi lớn của truyện là: liệu Mob có thể sống mà không cần chạm tới một trăm phần trăm? Liệu cậu có thể nói ra cảm xúc trước khi nó bùng nổ?

<short pause> Vì sao một cậu bé lại khóa chặt cảm xúc như vậy? Câu trả lời nằm ở tuổi thơ.

<short pause> Khi còn nhỏ, có lần Mob mất kiểm soát sức mạnh, và vô tình làm em trai Ritsu bị thương. Từ đó, cậu sợ chính mình.

<short pause> Mob tự đặt ra cho mình một luật: không dùng sức mạnh để làm hại người khác, và không để cảm xúc điều khiển mình.

<short pause> Nghe thì trưởng thành. <short pause> Nhưng cách cậu làm là tắt hết cảm xúc. Không vui quá, không buồn quá, không giận quá. Và đó chính là lý do bộ đếm cứ âm thầm tăng lên.

<short pause> <laugh> Kaku thấy đây là chỗ bộ truyện rất thật. Nhiều người lớn lên cũng tin rằng kìm nén là mạnh mẽ. <short pause> Nhưng cảm xúc bị khóa không biến mất. Nó chỉ chờ ngày bùng ra.

<short pause> Và Mob cũng tin một điều khác nữa: năng lực siêu nhiên không làm cậu đặc biệt hơn ai. Nó chỉ là một khả năng, giống như chạy nhanh hay học giỏi.
```

**ElevenLabs**

```text
Giờ tới chi tiết đặc biệt nhất của bộ truyện: con số phần trăm. Trên màn hình thỉnh thoảng hiện một bộ đếm, từ vài phần trăm tăng dần lên.

[pause] Bộ đếm này đo cảm xúc bị dồn nén của Mob. Mỗi lần cậu bị trêu chọc, bị ép, bị tổn thương mà không nói ra, con số lại tăng lên.

[pause] Khi chạm một trăm phần trăm, cảm xúc bùng nổ. Và sức mạnh siêu nhiên của Mob bùng nổ theo, gắn với đúng cảm xúc đó.

[pause] Anime còn cho người xem thấy bộ đếm ngay trên màn hình. Mỗi lần con số hiện lên, người xem tự đếm theo, và hồi hộp chờ xem điều gì sẽ khiến nó chạm một trăm.

[pause] Nghĩa là trong Mob Psycho 100, sức mạnh không đo bằng cấp độ hay chiêu thức. Nó đo bằng cảm xúc. Sức mạnh lớn nhất xuất hiện khi cậu không còn kìm nén được nữa.

[pause] Đây là một ẩn dụ rất đẹp cho tuổi dậy thì. Ai cũng từng có lúc dồn nén quá lâu, rồi một ngày bùng lên vì một chuyện rất nhỏ.

[pause] Kaku để ý: bộ đếm không bao giờ đo năng lực của Mob. Nó chỉ đo khoảng cách giữa cái Mob cảm thấy và cái Mob dám thể hiện.

[pause] [curious] Và câu hỏi lớn của truyện là: liệu Mob có thể sống mà không cần chạm tới một trăm phần trăm? Liệu cậu có thể nói ra cảm xúc trước khi nó bùng nổ?

[pause] Vì sao một cậu bé lại khóa chặt cảm xúc như vậy? Câu trả lời nằm ở tuổi thơ.

[pause] Khi còn nhỏ, có lần Mob mất kiểm soát sức mạnh, và vô tình làm em trai Ritsu bị thương. Từ đó, cậu sợ chính mình.

[pause] Mob tự đặt ra cho mình một luật: không dùng sức mạnh để làm hại người khác, và không để cảm xúc điều khiển mình.

[pause] Nghe thì trưởng thành. [pause] Nhưng cách cậu làm là tắt hết cảm xúc. Không vui quá, không buồn quá, không giận quá. Và đó chính là lý do bộ đếm cứ âm thầm tăng lên.

[pause] [chuckles] Kaku thấy đây là chỗ bộ truyện rất thật. Nhiều người lớn lên cũng tin rằng kìm nén là mạnh mẽ. [pause] Nhưng cảm xúc bị khóa không biến mất. Nó chỉ chờ ngày bùng ra.

[pause] Và Mob cũng tin một điều khác nữa: năng lực siêu nhiên không làm cậu đặc biệt hơn ai. Nó chỉ là một khả năng, giống như chạy nhanh hay học giỏi.
```

### c04 · Những kiểu 100% / ???%: phần bị giấu kín

Khoảng 124 giây · cảnh s29–s40 · 1610 ký tự

**Gemini**

```text
Điều thú vị nhất: mỗi lần chạm một trăm phần trăm, Mob bùng nổ theo một cảm xúc khác nhau. Và sức mạnh mang màu của cảm xúc đó.

<short pause> Có lúc là tức giận, khi cậu thấy người khác bị làm hại. Sức mạnh khi đó dữ dội, muốn phá hủy mọi thứ trước mặt.

<short pause> Có lúc là buồn bã. Sức mạnh khi đó không tấn công, mà lan ra như một làn sóng nặng nề, khiến mọi thứ xung quanh chìm xuống.

<short pause> Có lúc là lòng dũng cảm, hay lòng biết ơn. Sức mạnh khi đó sáng và ấm, dùng để bảo vệ chứ không để phá hủy.

<short pause> Nghĩa là sức mạnh của Mob không tốt, không xấu. Nó chỉ khuếch đại cái đang có trong tim cậu. Giống như một chiếc loa: bạn nói gì, nó phát to lên cái đó.

<short pause> Đây là lý do Kaku chọn Mob cho video Tết. Truyện nói rằng điều quan trọng không phải là bạn mạnh cỡ nào, mà là trong tim bạn đang có gì.

<short pause> Kaku rất thích cách anime thể hiện những khoảnh khắc này: màu sắc, nét vẽ, cả phong cách hình thay đổi theo từng cảm xúc. Bạn không cần nghe lời thoại cũng biết Mob đang cảm thấy gì.

<short pause> Nhưng có một trạng thái đáng sợ hơn một trăm phần trăm. Bộ đếm không hiện số, chỉ hiện ba dấu hỏi.

<short pause> Trạng thái này thường xuất hiện khi Mob bất tỉnh. Cậu không còn tỉnh táo, và sức mạnh tự hành động, mạnh hơn và khó kiểm soát hơn mọi lần.

<short pause> Nhiều người xem hiểu ???% là phần sâu nhất của Mob: tất cả những cảm xúc cậu đã khóa lại suốt nhiều năm, giờ có hình dạng riêng.

<short pause> Trong mùa cuối, phần bị giấu kín đó mất kiểm soát, và trở thành mối nguy lớn nhất của câu chuyện. Không có kẻ thù nào mạnh hơn chính cảm xúc bị dồn nén của Mob.

<short pause> Kaku thấy đây là một ý tưởng rất dũng cảm của tác giả. Trận cuối không phải là đánh bại một phản diện, mà là một cậu bé học cách gặp lại chính mình.
```

**ElevenLabs**

```text
Điều thú vị nhất: mỗi lần chạm một trăm phần trăm, Mob bùng nổ theo một cảm xúc khác nhau. Và sức mạnh mang màu của cảm xúc đó.

[pause] Có lúc là tức giận, khi cậu thấy người khác bị làm hại. Sức mạnh khi đó dữ dội, muốn phá hủy mọi thứ trước mặt.

[pause] Có lúc là buồn bã. Sức mạnh khi đó không tấn công, mà lan ra như một làn sóng nặng nề, khiến mọi thứ xung quanh chìm xuống.

[pause] Có lúc là lòng dũng cảm, hay lòng biết ơn. Sức mạnh khi đó sáng và ấm, dùng để bảo vệ chứ không để phá hủy.

[pause] Nghĩa là sức mạnh của Mob không tốt, không xấu. Nó chỉ khuếch đại cái đang có trong tim cậu. Giống như một chiếc loa: bạn nói gì, nó phát to lên cái đó.

[pause] Đây là lý do Kaku chọn Mob cho video Tết. Truyện nói rằng điều quan trọng không phải là bạn mạnh cỡ nào, mà là trong tim bạn đang có gì.

[pause] Kaku rất thích cách anime thể hiện những khoảnh khắc này: màu sắc, nét vẽ, cả phong cách hình thay đổi theo từng cảm xúc. Bạn không cần nghe lời thoại cũng biết Mob đang cảm thấy gì.

[pause] Nhưng có một trạng thái đáng sợ hơn một trăm phần trăm. Bộ đếm không hiện số, chỉ hiện ba dấu hỏi.

[pause] Trạng thái này thường xuất hiện khi Mob bất tỉnh. Cậu không còn tỉnh táo, và sức mạnh tự hành động, mạnh hơn và khó kiểm soát hơn mọi lần.

[pause] Nhiều người xem hiểu ???% là phần sâu nhất của Mob: tất cả những cảm xúc cậu đã khóa lại suốt nhiều năm, giờ có hình dạng riêng.

[pause] Trong mùa cuối, phần bị giấu kín đó mất kiểm soát, và trở thành mối nguy lớn nhất của câu chuyện. Không có kẻ thù nào mạnh hơn chính cảm xúc bị dồn nén của Mob.

[pause] Kaku thấy đây là một ý tưởng rất dũng cảm của tác giả. Trận cuối không phải là đánh bại một phản diện, mà là một cậu bé học cách gặp lại chính mình.
```

### c05 · Người thầy không có năng lực: Reigen / Ritsu: người em muốn có năng lực

Khoảng 117 giây · cảnh s41–s50 · 1519 ký tự

**Gemini**

```text
Giờ tới nhân vật quan trọng thứ hai trong chân dung của Mob: Reigen. Một người lừa đảo, không có năng lực, nói dối rất giỏi.

<short pause> Nhưng Reigen dạy Mob những điều không siêu năng lực nào dạy được: cách đối xử với người khác, cách nhìn một vấn đề từ nhiều phía, và cách xin lỗi.

<short pause> Reigen từng nói với Mob, đại ý: gặp chuyện mình không thích thì bỏ chạy cũng được. Với một cậu bé luôn cố chịu đựng, đó là lời cho phép quan trọng nhất.

<short pause> Reigen cũng không bao giờ coi Mob là vũ khí. Với ông, Mob là một đứa trẻ. Ông muốn Mob có bạn bè, có câu lạc bộ, có cuộc sống bình thường.

<short pause> Và mối quan hệ này đi theo cả hai chiều. Mob thấy Reigen nói dối, nhưng cũng thấy Reigen thật lòng. Có lúc Mob phải tự quyết định rời khỏi cái bóng của thầy.

<short pause> <laugh> Kaku nghĩ Reigen là một trong những người thầy hay nhất trong anime. Ông không mạnh, không hoàn hảo, nhưng ông giúp học trò trở thành người tốt hơn chính mình.

<short pause> Một nhân vật nữa giúp ta hiểu Mob: em trai Ritsu. Ritsu là học sinh giỏi, được thầy cô quý, là hội viên hội học sinh. Nhìn từ ngoài, Ritsu mới là người thành công trong nhà.

<short pause> Nhưng Ritsu lại ghen tị với anh. Cậu muốn có năng lực siêu nhiên như Mob, vì trong mắt cậu, đó là thứ duy nhất anh có mà mình không có.

<short pause> Khi Ritsu thức tỉnh năng lực, cậu vui, nhưng cũng bắt đầu đi sai đường. Năng lực không làm Ritsu hạnh phúc hơn. Nó chỉ làm cậu hiểu anh mình phải gánh nặng thế nào.

<short pause> Hai anh em là hai mặt của một câu hỏi: người có năng lực muốn bình thường, người bình thường muốn có năng lực. Và cả hai đều học được rằng giá trị của mình không nằm ở đó.
```

**ElevenLabs**

```text
Giờ tới nhân vật quan trọng thứ hai trong chân dung của Mob: Reigen. Một người lừa đảo, không có năng lực, nói dối rất giỏi.

[pause] Nhưng Reigen dạy Mob những điều không siêu năng lực nào dạy được: cách đối xử với người khác, cách nhìn một vấn đề từ nhiều phía, và cách xin lỗi.

[pause] Reigen từng nói với Mob, đại ý: gặp chuyện mình không thích thì bỏ chạy cũng được. Với một cậu bé luôn cố chịu đựng, đó là lời cho phép quan trọng nhất.

[pause] Reigen cũng không bao giờ coi Mob là vũ khí. Với ông, Mob là một đứa trẻ. Ông muốn Mob có bạn bè, có câu lạc bộ, có cuộc sống bình thường.

[pause] Và mối quan hệ này đi theo cả hai chiều. Mob thấy Reigen nói dối, nhưng cũng thấy Reigen thật lòng. Có lúc Mob phải tự quyết định rời khỏi cái bóng của thầy.

[pause] [chuckles] Kaku nghĩ Reigen là một trong những người thầy hay nhất trong anime. Ông không mạnh, không hoàn hảo, nhưng ông giúp học trò trở thành người tốt hơn chính mình.

[pause] Một nhân vật nữa giúp ta hiểu Mob: em trai Ritsu. Ritsu là học sinh giỏi, được thầy cô quý, là hội viên hội học sinh. Nhìn từ ngoài, Ritsu mới là người thành công trong nhà.

[pause] Nhưng Ritsu lại ghen tị với anh. Cậu muốn có năng lực siêu nhiên như Mob, vì trong mắt cậu, đó là thứ duy nhất anh có mà mình không có.

[pause] Khi Ritsu thức tỉnh năng lực, cậu vui, nhưng cũng bắt đầu đi sai đường. Năng lực không làm Ritsu hạnh phúc hơn. Nó chỉ làm cậu hiểu anh mình phải gánh nặng thế nào.

[pause] Hai anh em là hai mặt của một câu hỏi: người có năng lực muốn bình thường, người bình thường muốn có năng lực. Và cả hai đều học được rằng giá trị của mình không nằm ở đó.
```

### c06 · Dimple: linh hồn đồng hành / Những người có sức mạnh và lạc lối

Khoảng 94 giây · cảnh s51–s58 · 1227 ký tự

**Gemini**

```text
Còn một người bạn đồng hành rất lạ: một linh hồn tên Dimple. Ban đầu Dimple muốn chiếm cơ thể Mob để trở thành thần, nhưng thất bại và bị Mob đánh bại.

<short pause> Thay vì biến mất, Dimple ở lại bên Mob, nói là để chờ cơ hội. <short pause> Nhưng dần dần, linh hồn này trở thành một người bạn, người hay trêu chọc nhưng luôn có mặt.

<short pause> <laugh> Kaku để ý: từ kẻ muốn lợi dụng sức mạnh của Mob, Dimple trở thành một trong những người hiểu Mob nhất. Một lần nữa, truyện cho thấy người ta gắn bó với Mob vì con người cậu, không phải vì năng lực.

<short pause> Để hiểu Mob, hãy nhìn những người có năng lực khác trong truyện. Nhiều người trong số họ tin rằng năng lực khiến họ đặc biệt, cao hơn người thường.

<short pause> Có một cậu học sinh tên Teru, người dùng năng lực để làm trùm trường. Khi gặp Mob, cậu thua, và lần đầu tiên nhận ra năng lực không làm mình trở thành người tốt hơn.

<short pause> Có cả một tổ chức gồm những người có năng lực muốn thống trị thế giới. Họ tin người có năng lực phải đứng trên người thường.

<short pause> Mob thì ngược lại. Cậu mạnh nhất, nhưng tin rằng năng lực chỉ là một đặc điểm, như chiều cao hay màu tóc. Cậu không muốn đứng trên ai cả.

<short pause> Chính niềm tin đó khiến Mob thay đổi được nhiều người. Cậu không đánh bại họ bằng sức mạnh, mà bằng cách cho họ thấy họ không cần sức mạnh để có giá trị.
```

**ElevenLabs**

```text
Còn một người bạn đồng hành rất lạ: một linh hồn tên Dimple. Ban đầu Dimple muốn chiếm cơ thể Mob để trở thành thần, nhưng thất bại và bị Mob đánh bại.

[pause] Thay vì biến mất, Dimple ở lại bên Mob, nói là để chờ cơ hội. [pause] Nhưng dần dần, linh hồn này trở thành một người bạn, người hay trêu chọc nhưng luôn có mặt.

[pause] [chuckles] Kaku để ý: từ kẻ muốn lợi dụng sức mạnh của Mob, Dimple trở thành một trong những người hiểu Mob nhất. Một lần nữa, truyện cho thấy người ta gắn bó với Mob vì con người cậu, không phải vì năng lực.

[pause] Để hiểu Mob, hãy nhìn những người có năng lực khác trong truyện. Nhiều người trong số họ tin rằng năng lực khiến họ đặc biệt, cao hơn người thường.

[pause] Có một cậu học sinh tên Teru, người dùng năng lực để làm trùm trường. Khi gặp Mob, cậu thua, và lần đầu tiên nhận ra năng lực không làm mình trở thành người tốt hơn.

[pause] Có cả một tổ chức gồm những người có năng lực muốn thống trị thế giới. Họ tin người có năng lực phải đứng trên người thường.

[pause] Mob thì ngược lại. Cậu mạnh nhất, nhưng tin rằng năng lực chỉ là một đặc điểm, như chiều cao hay màu tóc. Cậu không muốn đứng trên ai cả.

[pause] Chính niềm tin đó khiến Mob thay đổi được nhiều người. Cậu không đánh bại họ bằng sức mạnh, mà bằng cách cho họ thấy họ không cần sức mạnh để có giá trị.
```

### c07 · Câu lạc bộ Cải thiện Cơ thể / Cái kết: một trăm phần trăm chính mình

Khoảng 151 giây · cảnh s59–s72 · 1962 ký tự

**Gemini**

```text
Có một nhóm nhân vật Kaku rất thích: câu lạc bộ Cải thiện Cơ thể. Những anh chàng to cao, cơ bắp, nhìn thì đáng sợ, nhưng hóa ra rất tử tế.

<short pause> Mob là thành viên yếu nhất. Chạy chậm nhất, hụt hơi nhanh nhất. <short pause> Nhưng không ai chê cậu. Họ chờ cậu, cổ vũ cậu, và tôn trọng việc cậu cố gắng.

<short pause> Điều thú vị là các anh chàng này không có năng lực siêu nhiên nào. <short pause> Nhưng với Mob, họ là những người đầu tiên chấp nhận cậu như một người bình thường.

<short pause> Và trong trận cuối, khi Mob mất kiểm soát, họ cũng có mặt. Không phải để chiến đấu, mà để nói với cậu rằng họ vẫn ở đây.

<short pause> Có một câu nói của đội trưởng câu lạc bộ mà nhiều người nhớ, đại ý: cơ thể không lừa dối ai. Mỗi bước chạy thêm là một bước thật, không có phép màu nào thay được.

<short pause> Kaku nghĩ đây là thông điệp giản dị nhất của truyện: đôi khi người giúp bạn nhiều nhất không phải người mạnh nhất, mà là người không bỏ bạn lại phía sau.

<short pause> Tới mùa cuối, Mob quyết định làm một việc rất bình thường mà rất khó: nói ra tình cảm với cô bạn thời thơ ấu, Tsubomi.

<short pause> Nỗi sợ bị từ chối khiến bộ đếm tăng vọt, và phần bị giấu kín của Mob bùng nổ thành một cơn bão khổng lồ phủ lên cả thành phố.

<short pause> Những người quanh Mob lần lượt tới: em trai, thầy Reigen, bạn bè, cả những người từng là đối thủ. Họ không tới để đánh bại cơn bão. Họ tới để gọi Mob trở về.

<short pause> Và Mob gặp chính mình, phần cảm xúc cậu đã giấu suốt bao năm. Cậu không tiêu diệt nó. Cậu chấp nhận nó, như một phần của mình.

<short pause> Cậu vẫn đi gặp Tsubomi. Lời tỏ tình không được đáp lại như cậu mong. <short pause> Nhưng cậu không bùng nổ. Cậu buồn, và cậu để mình buồn.

<short pause> Hãy so sánh với mùa một: một cậu bé giấu mọi cảm xúc sau gương mặt không biểu cảm. Tới mùa cuối, cậu khóc, cậu cười, cậu nói ra. Đó là sự trưởng thành lớn nhất trong truyện.

<short pause> Kaku thấy đây là cái kết đẹp nhất có thể. Mob không thắng tình yêu, nhưng thắng được nỗi sợ cảm xúc của chính mình. Bộ đếm không cần chạm một trăm nữa.

<short pause> Và thầy Reigen có mặt ở đó, như mọi lần, để mời Mob đi ăn. Một cái kết nhỏ, bình thường, đúng như điều Mob mong muốn từ đầu.
```

**ElevenLabs**

```text
Có một nhóm nhân vật Kaku rất thích: câu lạc bộ Cải thiện Cơ thể. Những anh chàng to cao, cơ bắp, nhìn thì đáng sợ, nhưng hóa ra rất tử tế.

[pause] Mob là thành viên yếu nhất. Chạy chậm nhất, hụt hơi nhanh nhất. [pause] Nhưng không ai chê cậu. Họ chờ cậu, cổ vũ cậu, và tôn trọng việc cậu cố gắng.

[pause] Điều thú vị là các anh chàng này không có năng lực siêu nhiên nào. [pause] Nhưng với Mob, họ là những người đầu tiên chấp nhận cậu như một người bình thường.

[pause] Và trong trận cuối, khi Mob mất kiểm soát, họ cũng có mặt. Không phải để chiến đấu, mà để nói với cậu rằng họ vẫn ở đây.

[pause] Có một câu nói của đội trưởng câu lạc bộ mà nhiều người nhớ, đại ý: cơ thể không lừa dối ai. Mỗi bước chạy thêm là một bước thật, không có phép màu nào thay được.

[pause] Kaku nghĩ đây là thông điệp giản dị nhất của truyện: đôi khi người giúp bạn nhiều nhất không phải người mạnh nhất, mà là người không bỏ bạn lại phía sau.

[pause] Tới mùa cuối, Mob quyết định làm một việc rất bình thường mà rất khó: nói ra tình cảm với cô bạn thời thơ ấu, Tsubomi.

[pause] Nỗi sợ bị từ chối khiến bộ đếm tăng vọt, và phần bị giấu kín của Mob bùng nổ thành một cơn bão khổng lồ phủ lên cả thành phố.

[pause] Những người quanh Mob lần lượt tới: em trai, thầy Reigen, bạn bè, cả những người từng là đối thủ. Họ không tới để đánh bại cơn bão. Họ tới để gọi Mob trở về.

[pause] Và Mob gặp chính mình, phần cảm xúc cậu đã giấu suốt bao năm. Cậu không tiêu diệt nó. Cậu chấp nhận nó, như một phần của mình.

[pause] Cậu vẫn đi gặp Tsubomi. Lời tỏ tình không được đáp lại như cậu mong. [pause] Nhưng cậu không bùng nổ. Cậu buồn, và cậu để mình buồn.

[pause] Hãy so sánh với mùa một: một cậu bé giấu mọi cảm xúc sau gương mặt không biểu cảm. Tới mùa cuối, cậu khóc, cậu cười, cậu nói ra. Đó là sự trưởng thành lớn nhất trong truyện.

[pause] Kaku thấy đây là cái kết đẹp nhất có thể. Mob không thắng tình yêu, nhưng thắng được nỗi sợ cảm xúc của chính mình. Bộ đếm không cần chạm một trăm nữa.

[pause] Và thầy Reigen có mặt ở đó, như mọi lần, để mời Mob đi ăn. Một cái kết nhỏ, bình thường, đúng như điều Mob mong muốn từ đầu.
```

### c08 · Bài học cho năm mới / Chân dung trong một câu / Kết

Khoảng 106 giây · cảnh s73–s83 · 1384 ký tự

**Gemini**

```text
Vậy Mob Psycho 100 muốn nói gì với chúng ta, trong ngày đầu năm?

<short pause> Một: cảm xúc không phải là điểm yếu. Giận, buồn, sợ, vui, tất cả đều là một phần của bạn. Khóa chúng lại không làm bạn mạnh hơn.

<short pause> Hai: năng lực, tài năng, hay bất cứ điều gì bạn giỏi, không làm bạn cao hơn người khác. Nó chỉ là một phần của bạn.

<short pause> Ba: hãy tìm những người như Reigen và câu lạc bộ cơ bắp. Những người không cần bạn mạnh, chỉ cần bạn là chính mình.

<short pause> Bốn: đừng so sánh mình với người khác theo kiểu ai có năng lực hơn. Mob và Ritsu, mỗi người đều có giá trị riêng, không ai hơn ai.

<short pause> <laugh> Kaku đề nghị một thử thách nhỏ cho năm mới: hãy nói ra một cảm xúc bạn đã giữ quá lâu. Một lời cảm ơn, một lời xin lỗi, hay một lời thương. Trước khi bộ đếm chạm một trăm.

<short pause> Và giờ, Kaku tóm cả con người Mob trong đúng một câu, như đã hứa ở đầu video.

<short pause> Mob không phải người mạnh nhất học cách kiểm soát sức mạnh. Mob là người học cách không cần sức mạnh để được là chính mình.

<short pause> Nếu năm nay bạn chỉ xem một bộ anime cùng gia đình, Kaku gợi ý Mob Psycho 100. Nó hài hước, nó đẹp, và nó để lại trong bạn một điều ấm áp.

<short pause> Video tiếp theo, Kaku gỡ mười hiểu lầm phổ biến nhất về One Piece, đúng lúc bản làm lại chuẩn bị ra mắt. Có hiểu lầm mà chính fan lâu năm cũng tin.

<short pause> Kaku chúc bạn một năm mới thật nhiều cảm xúc tốt, và đủ can đảm để nói ra cả những cảm xúc khó. Đăng ký kênh để Kaku đồng hành với bạn cả năm nhé. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Vậy Mob Psycho 100 muốn nói gì với chúng ta, trong ngày đầu năm?

[pause] Một: cảm xúc không phải là điểm yếu. Giận, buồn, sợ, vui, tất cả đều là một phần của bạn. Khóa chúng lại không làm bạn mạnh hơn.

[pause] Hai: năng lực, tài năng, hay bất cứ điều gì bạn giỏi, không làm bạn cao hơn người khác. Nó chỉ là một phần của bạn.

[pause] Ba: hãy tìm những người như Reigen và câu lạc bộ cơ bắp. Những người không cần bạn mạnh, chỉ cần bạn là chính mình.

[pause] Bốn: đừng so sánh mình với người khác theo kiểu ai có năng lực hơn. Mob và Ritsu, mỗi người đều có giá trị riêng, không ai hơn ai.

[pause] [chuckles] Kaku đề nghị một thử thách nhỏ cho năm mới: hãy nói ra một cảm xúc bạn đã giữ quá lâu. Một lời cảm ơn, một lời xin lỗi, hay một lời thương. Trước khi bộ đếm chạm một trăm.

[pause] Và giờ, Kaku tóm cả con người Mob trong đúng một câu, như đã hứa ở đầu video.

[pause] Mob không phải người mạnh nhất học cách kiểm soát sức mạnh. Mob là người học cách không cần sức mạnh để được là chính mình.

[pause] Nếu năm nay bạn chỉ xem một bộ anime cùng gia đình, Kaku gợi ý Mob Psycho 100. Nó hài hước, nó đẹp, và nó để lại trong bạn một điều ấm áp.

[pause] Video tiếp theo, Kaku gỡ mười hiểu lầm phổ biến nhất về One Piece, đúng lúc bản làm lại chuẩn bị ra mắt. Có hiểu lầm mà chính fan lâu năm cũng tin.

[pause] Kaku chúc bạn một năm mới thật nhiều cảm xúc tốt, và đủ can đảm để nói ra cả những cảm xúc khó. Đăng ký kênh để Kaku đồng hành với bạn cả năm nhé. Kaku gấp sổ đây, hẹn gặp lại!
```
