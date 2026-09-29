# Bộ prompt · Miền đất hứa: Nếu bạn là đứa trẻ ở Grace Field, bạn có thoát được không?

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

Lời: Cảnh báo spoiler: video này nói về bí mật lớn nhất của Miền đất hứa ngay từ đầu, và đi tới hết cuộc đào thoát…

```text
Wide 16:9 landscape cinematic frame. a closed storybook with a white picket fence drawn on its cover lying on a wooden table beside a spoiler card, close-up, deceptively warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Giả sử bạn tỉnh dậy trong một trại mồ côi tuyệt đẹp. Có đồng cỏ xanh, rừng cây, đồ ăn ngon, và một người mẹ h…

```text
Wide 16:9 landscape cinematic frame. a beautiful white orphanage building surrounded by green meadows and a forest under a clear sky, wide shot, warm idyllic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Bạn có ba mươi tám anh chị em. Mỗi ngày học, chơi, làm bài kiểm tra. Không ai phải đói, không ai bị đánh. Chỉ…

```text
Wide 16:9 landscape cinematic frame. a group of children in plain white clothes running across a grassy field toward a distant tree line, wide shot, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và thỉnh thoảng, một đứa trẻ được nhận nuôi. Nó vui vẻ chào mọi người, đi ra cổng, và không bao giờ viết thư…

```text
Wide 16:9 landscape cinematic frame. a small child waving goodbye at a large closed gate at dusk, back view, wide shot, bittersweet warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay bạn là một đứa trẻ ở Grace Field. Kaku sẽ đưa bạn qua mười lựa chọn. Mỗi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small scorecard with ten empty boxes and a pencil, looking serious. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Miền đất hứa là manga của Shirai Kaiu viết truyện và Demizu Posuka vẽ, đăng trên Weekly Shonen Jump từ năm 20…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a small wooden toy house on a shelf, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Ba bộ óc của Grace Field

Lời: Trước khi chọn, hãy làm quen ba người sẽ dẫn đường cho bạn. Emma: nhanh nhẹn, lạc quan, học giỏi nhưng quan t…

```text
Wide 16:9 landscape cinematic frame. a cheerful girl running across a meadow while holding the hand of a smaller child, wide shot, bright warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Norman: điềm tĩnh, giỏi chiến thuật nhất nhà, luôn tính trước vài bước. Cậu là người lên kế hoạch.

```text
Wide 16:9 landscape cinematic frame. a calm boy sitting under a tree with a chess board, studying the pieces carefully, medium shot, soft dappled light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ray: trầm lặng, mê đọc sách, lạnh lùng và thực tế. Cậu là người biết nhiều nhất, và giấu nhiều nhất.

```text
Wide 16:9 landscape cinematic frame. a quiet boy reading a thick book alone in a corner of a library, lamplight on his face, medium shot, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Ba người, ba cách nghĩ: trái tim, chiến thuật, và sự thật lạnh lùng. Mỗi lựa chọn trong video này là một cuộc…

```text
Wide 16:9 landscape cinematic frame. three chairs arranged in a triangle around a small table with a map on it, overhead shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: bạn không cần giống ai trong ba người. Nhưng để thoát, nhóm cần cả ba.

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing three small puzzle pieces together to form a complete key shape. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Lựa chọn 1: bài kiểm tra mỗi ngày

Lời: Mỗi sáng, các con phải làm một bài kiểm tra khó: toán, logic, trí nhớ. Người mẹ khen những con được điểm cao.…

```text
Wide 16:9 landscape cinematic frame. a classroom with rows of simple desks and test papers, children concentrating in silence, wide shot, bright morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Phương án A: học chăm, cố đạt điểm cao nhất. Phương án B: làm vừa phải, không nổi bật.

```text
Wide 16:9 landscape cinematic frame. two paths drawn on parchment: one leading to a trophy, one leading to a quiet ordinary house, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nhưng có một nghịch lý: điểm càng cao, bạn càng là món hàng có giá trị hơn. Học giỏi vừa là cách để được giữ…

```text
Wide 16:9 landscape cinematic frame. a gold trophy sitting inside a birdcage on a shelf, symbolic close-up, cold elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Câu trả lời đúng là A, dù bạn chưa biết vì sao. Ba đứa trẻ giỏi nhất nhà, Emma, Norman và Ray, luôn đạt điểm…

```text
Wide 16:9 landscape cinematic frame. three test papers with perfect scores pinned side by side on a corkboard, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Về sau bạn sẽ hiểu: bài kiểm tra không chỉ để học. Nó là cách đo xem bộ não của bạn phát triển tới đâu. Bộ nã…

```text
Wide 16:9 landscape cinematic frame. a measuring scale with a small brain icon on one side and a coin on the other, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Điểm sống sót nếu chọn A: một. Và thêm một điều: bộ não của bạn chính là vũ khí duy nhất để thoát khỏi nơi nà…

```text
Wide 16:9 landscape cinematic frame. a scorecard with the first box checked in green ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Lựa chọn 2: đêm tiễn bạn

Lời: Một đêm, Conny, cô bé sáu tuổi, được nhận nuôi. Cô vui vẻ ra đi, nhưng bỏ quên con thỏ bông mà cô không bao g…

```text
Wide 16:9 landscape cinematic frame. a small worn stuffed rabbit lying alone on a wooden floor near a door at night, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Bạn có mang con thỏ bông ra cổng để trả lại, dù luật cấm tới gần cánh cổng không?

```text
Wide 16:9 landscape cinematic frame. a child's hand hesitating before a large closed gate at night holding a small stuffed rabbit, close-up, tense moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Emma và Norman đã làm vậy. Và họ phát hiện ra sự thật: không có ai nhận nuôi cả. Ngoài cổng là những sinh vật…

```text
Wide 16:9 landscape cinematic frame. two small shadows hiding behind a truck at night, peering toward giant shadowy figures in the distance, wide shot, ominous cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Hãy tưởng tượng cảm giác của Emma và Norman đêm đó: mọi kỷ niệm đẹp trong mười một năm, mọi bữa ăn, mọi cái ô…

```text
Wide 16:9 landscape cinematic frame. a wall of cheerful children's drawings in a dim hallway at night, one drawing slightly crumpled, close-up, cold moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kaku không mô tả thêm. Chỉ cần biết: trại mồ côi là một trang trại. Người mẹ là người chăn nuôi. Và các con l…

```text
Wide 16:9 landscape cinematic frame. a beautiful orphanage building reflected in a puddle where the reflection shows a cold industrial farm, symbolic close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Đi hay không đi? Nếu không đi, bạn sẽ sống trong ảo tưởng cho tới ngày tới lượt mình. Nếu đi, bạn biết sự thậ…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the second box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Lựa chọn 3: nói hay giữ bí mật

Lời: Giờ bạn biết sự thật. Bạn sẽ nói cho các em nhỏ biết ngay, hay giữ bí mật?

```text
Wide 16:9 landscape cinematic frame. a group of small children laughing and playing tag in a sunny field while an older child watches from a distance with a worried face, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Và các em nhỏ có thể vô tình nói ra. Một câu hỏi ngây thơ trong bữa tối cũng đủ để người mẹ biết có chuyện gì…

```text
Wide 16:9 landscape cinematic frame. a small child raising a hand at a crowded dinner table to ask something, other children turning to look, medium shot, warm tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nếu nói ngay, các em sẽ hoảng sợ, khóc, và người mẹ sẽ phát hiện ngay lập tức. Kế hoạch sẽ sụp đổ trước khi b…

```text
Wide 16:9 landscape cinematic frame. a crowd of crying children around a tall calm silhouette in a doorway, symbolic wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Emma, Norman và Ray chọn giữ bí mật, chỉ nói với vài người đủ lớn và đáng tin. Họ giả vờ như không biết gì, v…

```text
Wide 16:9 landscape cinematic frame. three children whispering together under a large tree at dusk, heads close, medium shot, secretive warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Điểm cho lựa chọn giữ bí mật: một. Nhưng Kaku muốn bạn để ý cái giá: phải cười mỗi ngày với người mà bạn biết…

```text
Wide 16:9 landscape cinematic frame. a child's smiling face reflected in a window while their real expression behind the glass looks frightened, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Lựa chọn 4: người mẹ biết gì?

Lời: Người mẹ, Isabella, dường như luôn biết các con ở đâu. Bạn sẽ đoán cô biết bằng cách nào?

```text
Wide 16:9 landscape cinematic frame. a tall calm woman's silhouette standing at the top of a staircase watching children below, low-angle shot, cold elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Người mẹ cũng không bao giờ vội. Cô biết các con có ý định trốn, nhưng cô chơi một ván cờ dài: quan sát, đợi,…

```text
Wide 16:9 landscape cinematic frame. a tall calm silhouette slowly moving a chess piece on a board in a dim room, close-up, cold elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Câu trả lời trong truyện: mỗi đứa trẻ đều mang một thiết bị theo dõi được cấy vào người từ khi còn nhỏ. Người…

```text
Wide 16:9 landscape cinematic frame. a small pocket-watch-like device lying open on a desk with tiny glowing dots on its screen, close-up, eerie blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Và các con còn mang một con số ở cổ, được đánh dấu từ khi còn nhỏ. Mỗi đứa trẻ là một mã số.

```text
Wide 16:9 landscape cinematic frame. a ledger with rows of numbers written neatly in ink with no names beside them, extreme close-up, cold office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nhóm Emma phải tìm ra thiết bị đó nằm ở đâu, và làm sao vô hiệu hóa nó mà không bị phát hiện. Nếu không, trốn…

```text
Wide 16:9 landscape cinematic frame. a child examining a small diagram of a human outline with several question marks drawn around it, close-up, lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Điểm cho việc nghi ngờ và đi tìm thiết bị: một. Trong một nhà tù được thiết kế tốt, việc đầu tiên là tìm ra c…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the fourth box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Luật của trang trại

Lời: Để trốn khỏi một hệ thống, phải hiểu nó. Grace Field không phải trang trại duy nhất. Nó là một trang trại cao…

```text
Wide 16:9 landscape cinematic frame. a map with several small farm icons scattered across it, one of them marked with a gold star, parchment close-up, cold amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Vì sao phải chăm sóc tốt tới vậy? Vì bộ não được nuôi dưỡng tốt là thứ có giá nhất. Bài kiểm tra mỗi ngày, bữ…

```text
Wide 16:9 landscape cinematic frame. a perfectly arranged dinner table with healthy meals and flowers, filmed through a cold glass window, symbolic wide shot, eerie warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Và người mẹ không phải kẻ đến từ bên ngoài. Người mẹ từng là một đứa trẻ ở trang trại. Được chọn, được huấn l…

```text
Wide 16:9 landscape cinematic frame. an old uniform hanging in a closet beside a child's small white shirt, close-up, melancholy dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Cái tên Miền đất hứa cũng liên quan tới một lời hứa cổ xưa giữa con người và những sinh vật ngoài cổng. Phần…

```text
Wide 16:9 landscape cinematic frame. an ancient sealed scroll with two different handprints pressed into wax at its bottom, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Hiểu hệ thống giúp bạn thấy điểm yếu của nó: mọi thứ dựa vào niềm tin rằng trẻ em không biết gì. Khi các con…

```text
Wide 16:9 landscape cinematic frame. a hairline crack spreading across a perfect porcelain plate, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Lựa chọn 5: tin ai?

Lời: Rồi xuất hiện một người lớn thứ hai: Sơ Krone, được gửi tới để giúp mẹ. Sơ có vẻ thù địch với mẹ, và muốn lật…

```text
Wide 16:9 landscape cinematic frame. a second tall silhouette arriving at the orphanage gate with a suitcase, looking up at the building, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Bạn có hợp tác với Sơ Krone không? Kẻ thù của kẻ thù có phải là bạn?

```text
Wide 16:9 landscape cinematic frame. two chess pieces of different colors side by side, both facing a third piece, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nhóm Emma chọn lợi dụng Sơ Krone một cách cẩn thận, trao đổi thông tin nhưng không tin hẳn. Sơ đưa cho họ vài…

```text
Wide 16:9 landscape cinematic frame. a small folded note being passed secretly under a table, extreme close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và có một câu hỏi khó hơn nữa: trong chính nhóm của bạn, ai là người đáng tin? Ray, người thông minh nhất, hó…

```text
Wide 16:9 landscape cinematic frame. a child standing in shadow at the end of a hallway while two others look toward him with surprise, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Ray đã đổi thông tin lấy những món đồ từ người mẹ, và từng món đều được cậu dùng cho kế hoạch trốn chạy. Một…

```text
Wide 16:9 landscape cinematic frame. a small hidden collection of objects in a secret box: an old camera, a few books, a coil of wire, close-up, secretive warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhưng Ray làm gián điệp để có cơ hội cứu các bạn. Cậu chơi một ván cờ hai mặt từ nhiều năm trước. Tin người k…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the fifth box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Lựa chọn 6: đưa ai đi?

Lời: Đây là lựa chọn khó nhất. Kế hoạch trốn thoát có thể chỉ đưa được vài người lớn tuổi. Những em nhỏ bốn, năm t…

```text
Wide 16:9 landscape cinematic frame. a group of very small children holding hands in a line across a field, wide shot, tender warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Phương án A: chỉ những người đủ lớn, đủ nhanh. Tỉ lệ thành công cao hơn. Phương án B: đưa tất cả đi, không bỏ…

```text
Wide 16:9 landscape cinematic frame. two diagrams on parchment: a small fast group running and a large slow group walking together, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Hãy tự hỏi thật lòng: nếu bạn là người mười một tuổi, biết rằng mỗi phút chậm trễ có thể khiến tất cả bị bắt,…

```text
Wide 16:9 landscape cinematic frame. an older child kneeling to tie the shoelace of a tiny child at the edge of a dark forest, close-up, tender tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Ray muốn phương án A. Norman thì tính toán thận trọng. Nhưng Emma kiên quyết: không bỏ lại ai. Và chính lựa c…

```text
Wide 16:9 landscape cinematic frame. a determined girl standing in front of a group of younger children with arms outstretched protectively, medium shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói: về logic thuần túy, phương án A an toàn hơn. Nhưng Miền đất hứa không chấm điểm bằng logic thu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two scorecards, one marked logic and one marked heart, and slowly raising the second. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Kaku cho phương án B: hai điểm. Vì truyện cho thấy những em nhỏ cũng có thể làm được rất nhiều, nếu được tin…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the sixth box checked twice in bright ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Lựa chọn 7: huấn luyện các em

Lời: Họ còn phải tính tới cả những em bé chưa biết đi, và những em mới bốn tuổi. Kế hoạch trở thành một bài toán h…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn chart on paper pairing older children's names with younger ones, with arrows and small doodles, close-up, lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Muốn đưa tất cả đi, phải chuẩn bị cho tất cả. Nhóm Emma biến những trò chơi hằng ngày thành bài huấn luyện: t…

```text
Wide 16:9 landscape cinematic frame. children playing tag across a meadow with an older child timing them with a stopwatch, wide shot, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Họ dạy các em nhớ đường, làm theo tín hiệu, và giữ bình tĩnh. Người mẹ nhìn thấy các con chơi, nhưng không th…

```text
Wide 16:9 landscape cinematic frame. a watchful tall silhouette at a window looking down on children playing in formation below, wide shot, deceptive warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Kaku rất thích chi tiết này. Nó giống như ngoài đời: một nhóm mạnh không phải vì có một người giỏi, mà vì ai…

```text
Wide 16:9 landscape cinematic frame. a row of small shoes of different sizes lined up neatly by a door, close-up, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Điểm cho việc huấn luyện: một. Kế hoạch tốt tới đâu cũng vô ích nếu những người thực hiện nó không sẵn sàng.

```text
Wide 16:9 landscape cinematic frame. the scorecard with the seventh box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Lựa chọn 8: bức tường và vách đá

Lời: Bạn nghĩ lối thoát là cánh cổng? Không. Cổng được canh gác. Nhóm Emma khám phá ra khu rừng kết thúc bằng một…

```text
Wide 16:9 landscape cinematic frame. a towering stone wall at the edge of a forest with a sheer cliff drop visible beyond it, wide shot, dramatic evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Để vượt qua, họ phải chuẩn bị dây, tính toán độ cao, và tìm cách đưa cả những em nhỏ nhất qua vực.

```text
Wide 16:9 landscape cinematic frame. a coil of homemade rope made from knotted bedsheets hidden inside a hollow tree, close-up, secretive dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Họ học cách nhận biết giới hạn tầm phát hiện của thiết bị, và chọn đúng thời điểm để hành động. Mỗi chi tiết…

```text
Wide 16:9 landscape cinematic frame. a small hand-drawn map of the forest with concentric circles marking distances from the house, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Và họ cũng phải đối mặt với thiết bị theo dõi. Emma quyết định tự tay xử lý thiết bị trong tai mình. Một cái…

```text
Wide 16:9 landscape cinematic frame. a girl sitting alone by a window at night pressing a cloth to one ear, eyes determined, medium shot, cold moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Điểm cho việc tìm đúng lối thoát: một. Lối ra hiển nhiên thường là lối ra được canh gác kỹ nhất.

```text
Wide 16:9 landscape cinematic frame. the scorecard with the eighth box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Lựa chọn 9: khi kế hoạch đổ vỡ

Lời: Rồi mọi thứ đổ vỡ. Norman, người lên kế hoạch giỏi nhất, bị đưa đi trước ngày trốn thoát. Anh chấp nhận ra đi…

```text
Wide 16:9 landscape cinematic frame. a boy walking calmly toward a large gate at dusk, turning back once to wave, back view, wide shot, heartbreaking warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Trước khi đi, Norman để lại những gì cậu biết cho Emma và Ray. Một kế hoạch tốt không phụ thuộc vào một người…

```text
Wide 16:9 landscape cinematic frame. a folded note tucked inside a book on a shelf, with a tiny drawing of a key on it, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Bạn sẽ làm gì khi mất người quan trọng nhất trong kế hoạch? Bỏ cuộc, hay tiếp tục?

```text
Wide 16:9 landscape cinematic frame. an empty chair at a small table where three cups of tea are set, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Emma và Ray tiếp tục. Ray thậm chí định hy sinh chính mình trong một kế hoạch đốt cháy căn nhà để che giấu cu…

```text
Wide 16:9 landscape cinematic frame. a large house glowing with orange light against a night sky, small figures running toward the forest, wide shot, dramatic firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Điểm cho việc tiếp tục khi kế hoạch đổ vỡ: một. Không kế hoạch nào đi đúng như dự tính. Người sống sót là ngư…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the ninth box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · Lựa chọn 10: đêm trốn thoát

Lời: Đêm trốn thoát. Mười lăm đứa trẻ từ năm tuổi trở lên vượt qua bức tường. Những em còn quá nhỏ ở lại, với lời…

```text
Wide 16:9 landscape cinematic frame. a line of small figures crossing a rope over a dark chasm under the moonlight, wide shot, tense silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Và người mẹ Isabella, người đã nuôi và bán bao nhiêu đứa trẻ, đứng nhìn các con biến mất vào màn đêm. Cô thua…

```text
Wide 16:9 landscape cinematic frame. a lone woman's silhouette standing at the edge of a cliff at dawn looking out over a vast forest, back view, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Vì vậy Isabella không hẳn là một phản diện thuần túy. Cô là kết quả của chính hệ thống ấy: một đứa trẻ đã chọ…

```text
Wide 16:9 landscape cinematic frame. a woman's hand gently touching a child's old drawing pinned to a wall, close-up, bittersweet dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Kaku để ý: Isabella cũng từng là một đứa trẻ ở Grace Field. Cô từng chọn con đường sống sót bằng cách trở thà…

```text
Wide 16:9 landscape cinematic frame. an old photograph of a young girl standing in the same meadow, faded sepia tone, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Điểm cho việc cùng nhau vượt qua: một. Bạn đã ra khỏi Grace Field. Nhưng thế giới bên ngoài còn nguy hiểm hơn…

```text
Wide 16:9 landscape cinematic frame. the scorecard with the tenth box checked, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Bạn sống sót bao lâu?

Lời: Tổng kết điểm. Tối đa mười một điểm. Nếu bạn được từ chín tới mười một: bạn giống nhóm Emma. Bạn thoát được,…

```text
Wide 16:9 landscape cinematic frame. a scorecard with a high total circled and a small open gate drawn beside it, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Từ năm tới tám: bạn có thể thoát, nhưng sẽ phải trả giá, có thể là bỏ lại ai đó, hoặc bị phát hiện giữa chừng.

```text
Wide 16:9 landscape cinematic frame. a scorecard with a middle total circled and a half-open gate drawn beside it, close-up, cautious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Dưới năm: bạn ở lại Grace Field, sống những ngày hạnh phúc trong ảo tưởng, cho tới ngày tới lượt mình. Kaku s…

```text
Wide 16:9 landscape cinematic frame. a scorecard with a low total circled and a closed gate drawn beside it, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và thêm một câu hỏi: nếu bạn là Emma, Norman hay Ray, bạn sẽ là ai? Kaku đoán Kaku là Ray, vì Kaku cũng thích…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up three small name cards and hesitating between them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Viết điểm của bạn vào bình luận nhé. Và cho Kaku biết lựa chọn nào khó nhất với bạn.

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny gate and a pencil, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku

Lời: Miền đất hứa là một câu chuyện kinh dị, nhưng Kaku nghĩ nó thật ra là câu chuyện về giáo dục và tự do.

```text
Wide 16:9 landscape cinematic frame. a child reading a book under a tree with the light forming a doorway shape behind them, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Và những em nhỏ ở lại không bị bỏ rơi. Lời hứa quay lại đón các em trở thành động lực cho cả những phần sau c…

```text
Wide 16:9 landscape cinematic frame. a small handwritten promise note tucked under a pillow in an empty children's bedroom, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Trường học tốt nhất trong truyện lại là một trang trại. Và những đứa trẻ thoát ra nhờ chính những gì trang tr…

```text
Wide 16:9 landscape cinematic frame. a classroom blackboard covered in escape route diagrams drawn in chalk, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Câu hỏi của truyện dành cho mỗi người: nếu phát hiện thế giới mình sống không như vẻ ngoài, bạn sẽ im lặng để…

```text
Wide 16:9 landscape cinematic frame. a small figure standing at an open gate looking out at a vast unknown forest at dawn, back view, wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Miền đất hứa bắt đầu bằng một ngôi nhà hạnh phúc và kết thúc mùa một bằng những đứa trẻ chạy vào bóng tối. Nh…

```text
Wide 16:9 landscape cinematic frame. children's silhouettes running into a dark forest with the first light of dawn breaking through the trees ahead, wide shot, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku trải một dòng thời gian dài hai nghìn năm: Attack on Titan, từ Ymir đầu tiên tới những…

```text
Wide 16:9 landscape cinematic frame. an extremely long scroll unrolled across a stone floor with ink marks spanning its length, overhead shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video đặt bạn vào trong thế giới anime, hãy đăng ký kênh. Và nếu một ngày ai đó hứa cho b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking cautiously through a gap in a large gate, then waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Ba bộ óc của Grace Field

Khoảng 123 giây · cảnh s01–s11 · 1595 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói về bí mật lớn nhất của Miền đất hứa ngay từ đầu, và đi tới hết cuộc đào thoát khỏi Grace Field, tức anime mùa một. Nếu bạn chưa xem, hãy lưu lại. Tập một của bộ này rất đáng để xem mà không biết gì.

<short pause> Giả sử bạn tỉnh dậy trong một trại mồ côi tuyệt đẹp. Có đồng cỏ xanh, rừng cây, đồ ăn ngon, và một người mẹ hiền lành yêu thương tất cả các con.

<short pause> Bạn có ba mươi tám anh chị em. Mỗi ngày học, chơi, làm bài kiểm tra. Không ai phải đói, không ai bị đánh. Chỉ có hai luật: không được đi quá khu rừng, và không được tới gần cánh cổng.

<short pause> Và thỉnh thoảng, một đứa trẻ được nhận nuôi. Nó vui vẻ chào mọi người, đi ra cổng, và không bao giờ viết thư về.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay bạn là một đứa trẻ ở Grace Field. Kaku sẽ đưa bạn qua mười lựa chọn. Mỗi lựa chọn đúng là một điểm sống sót. Cuối video, bạn biết mình có thoát được hay không.

<short pause> Miền đất hứa là manga của Shirai Kaiu viết truyện và Demizu Posuka vẽ, đăng trên Weekly Shonen Jump từ năm 2016 tới 2020. Anime mùa một do CloverWorks làm năm 2019.

<short pause> Trước khi chọn, hãy làm quen ba người sẽ dẫn đường cho bạn. Emma: nhanh nhẹn, lạc quan, học giỏi nhưng quan trọng hơn, cô không bao giờ bỏ ai lại.

<short pause> Norman: điềm tĩnh, giỏi chiến thuật nhất nhà, luôn tính trước vài bước. Cậu là người lên kế hoạch.

<short pause> Ray: trầm lặng, mê đọc sách, lạnh lùng và thực tế. Cậu là người biết nhiều nhất, và giấu nhiều nhất.

<short pause> Ba người, ba cách nghĩ: trái tim, chiến thuật, và sự thật lạnh lùng. Mỗi lựa chọn trong video này là một cuộc tranh luận giữa ba cách nghĩ đó.

<short pause> Kaku để ý: bạn không cần giống ai trong ba người. <short pause> Nhưng để thoát, nhóm cần cả ba.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói về bí mật lớn nhất của Miền đất hứa ngay từ đầu, và đi tới hết cuộc đào thoát khỏi Grace Field, tức anime mùa một. Nếu bạn chưa xem, hãy lưu lại. Tập một của bộ này rất đáng để xem mà không biết gì.

[pause] Giả sử bạn tỉnh dậy trong một trại mồ côi tuyệt đẹp. Có đồng cỏ xanh, rừng cây, đồ ăn ngon, và một người mẹ hiền lành yêu thương tất cả các con.

[pause] Bạn có ba mươi tám anh chị em. Mỗi ngày học, chơi, làm bài kiểm tra. Không ai phải đói, không ai bị đánh. Chỉ có hai luật: không được đi quá khu rừng, và không được tới gần cánh cổng.

[pause] Và thỉnh thoảng, một đứa trẻ được nhận nuôi. Nó vui vẻ chào mọi người, đi ra cổng, và không bao giờ viết thư về.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay bạn là một đứa trẻ ở Grace Field. Kaku sẽ đưa bạn qua mười lựa chọn. Mỗi lựa chọn đúng là một điểm sống sót. Cuối video, bạn biết mình có thoát được hay không.

[pause] Miền đất hứa là manga của Shirai Kaiu viết truyện và Demizu Posuka vẽ, đăng trên Weekly Shonen Jump từ năm 2016 tới 2020. Anime mùa một do CloverWorks làm năm 2019.

[pause] Trước khi chọn, hãy làm quen ba người sẽ dẫn đường cho bạn. Emma: nhanh nhẹn, lạc quan, học giỏi nhưng quan trọng hơn, cô không bao giờ bỏ ai lại.

[pause] Norman: điềm tĩnh, giỏi chiến thuật nhất nhà, luôn tính trước vài bước. Cậu là người lên kế hoạch.

[pause] Ray: trầm lặng, mê đọc sách, lạnh lùng và thực tế. Cậu là người biết nhiều nhất, và giấu nhiều nhất.

[pause] Ba người, ba cách nghĩ: trái tim, chiến thuật, và sự thật lạnh lùng. Mỗi lựa chọn trong video này là một cuộc tranh luận giữa ba cách nghĩ đó.

[pause] Kaku để ý: bạn không cần giống ai trong ba người. [pause] Nhưng để thoát, nhóm cần cả ba.
```

### c02 · Lựa chọn 1: bài kiểm tra mỗi ngày / Lựa chọn 2: đêm tiễn bạn

Khoảng 128 giây · cảnh s12–s23 · 1658 ký tự

**Gemini**

```text
Mỗi sáng, các con phải làm một bài kiểm tra khó: toán, logic, trí nhớ. Người mẹ khen những con được điểm cao. Bạn sẽ làm thế nào?

<short pause> Phương án A: học chăm, cố đạt điểm cao nhất. Phương án B: làm vừa phải, không nổi bật.

<short pause> Nhưng có một nghịch lý: điểm càng cao, bạn càng là món hàng có giá trị hơn. Học giỏi vừa là cách để được giữ lại lâu hơn, vừa khiến bạn trở thành mục tiêu quý giá hơn.

<short pause> Câu trả lời đúng là A, dù bạn chưa biết vì sao. Ba đứa trẻ giỏi nhất nhà, Emma, Norman và Ray, luôn đạt điểm tối đa. Và điểm cao giúp chúng được giữ lại lâu hơn.

<short pause> Về sau bạn sẽ hiểu: bài kiểm tra không chỉ để học. Nó là cách đo xem bộ não của bạn phát triển tới đâu. Bộ não càng tốt, bạn càng có giá trị.

<short pause> Điểm sống sót nếu chọn A: một. Và thêm một điều: bộ não của bạn chính là vũ khí duy nhất để thoát khỏi nơi này.

<short pause> Một đêm, Conny, cô bé sáu tuổi, được nhận nuôi. Cô vui vẻ ra đi, nhưng bỏ quên con thỏ bông mà cô không bao giờ rời tay.

<short pause> Bạn có mang con thỏ bông ra cổng để trả lại, dù luật cấm tới gần cánh cổng không?

<short pause> Emma và Norman đã làm vậy. Và họ phát hiện ra sự thật: không có ai nhận nuôi cả. Ngoài cổng là những sinh vật không phải người, và trẻ em ở Grace Field được nuôi làm thức ăn cho chúng.

<short pause> Hãy tưởng tượng cảm giác của Emma và Norman đêm đó: mọi kỷ niệm đẹp trong mười một năm, mọi bữa ăn, mọi cái ôm của người mẹ, bỗng mang một ý nghĩa khác.

<short pause> Kaku không mô tả thêm. Chỉ cần biết: trại mồ côi là một trang trại. Người mẹ là người chăn nuôi. Và các con là sản phẩm.

<short pause> Đi hay không đi? Nếu không đi, bạn sẽ sống trong ảo tưởng cho tới ngày tới lượt mình. Nếu đi, bạn biết sự thật nhưng bắt đầu gặp nguy hiểm. Điểm cho lựa chọn đi: một. Không biết sự thật thì không thể thoát.
```

**ElevenLabs**

```text
Mỗi sáng, các con phải làm một bài kiểm tra khó: toán, logic, trí nhớ. Người mẹ khen những con được điểm cao. [curious] Bạn sẽ làm thế nào?

[pause] Phương án A: học chăm, cố đạt điểm cao nhất. Phương án B: làm vừa phải, không nổi bật.

[pause] Nhưng có một nghịch lý: điểm càng cao, bạn càng là món hàng có giá trị hơn. Học giỏi vừa là cách để được giữ lại lâu hơn, vừa khiến bạn trở thành mục tiêu quý giá hơn.

[pause] Câu trả lời đúng là A, dù bạn chưa biết vì sao. Ba đứa trẻ giỏi nhất nhà, Emma, Norman và Ray, luôn đạt điểm tối đa. Và điểm cao giúp chúng được giữ lại lâu hơn.

[pause] Về sau bạn sẽ hiểu: bài kiểm tra không chỉ để học. Nó là cách đo xem bộ não của bạn phát triển tới đâu. Bộ não càng tốt, bạn càng có giá trị.

[pause] Điểm sống sót nếu chọn A: một. Và thêm một điều: bộ não của bạn chính là vũ khí duy nhất để thoát khỏi nơi này.

[pause] Một đêm, Conny, cô bé sáu tuổi, được nhận nuôi. Cô vui vẻ ra đi, nhưng bỏ quên con thỏ bông mà cô không bao giờ rời tay.

[pause] Bạn có mang con thỏ bông ra cổng để trả lại, dù luật cấm tới gần cánh cổng không?

[pause] Emma và Norman đã làm vậy. Và họ phát hiện ra sự thật: không có ai nhận nuôi cả. Ngoài cổng là những sinh vật không phải người, và trẻ em ở Grace Field được nuôi làm thức ăn cho chúng.

[pause] Hãy tưởng tượng cảm giác của Emma và Norman đêm đó: mọi kỷ niệm đẹp trong mười một năm, mọi bữa ăn, mọi cái ôm của người mẹ, bỗng mang một ý nghĩa khác.

[pause] Kaku không mô tả thêm. Chỉ cần biết: trại mồ côi là một trang trại. Người mẹ là người chăn nuôi. Và các con là sản phẩm.

[pause] Đi hay không đi? Nếu không đi, bạn sẽ sống trong ảo tưởng cho tới ngày tới lượt mình. Nếu đi, bạn biết sự thật nhưng bắt đầu gặp nguy hiểm. Điểm cho lựa chọn đi: một. Không biết sự thật thì không thể thoát.
```

### c03 · Lựa chọn 3: nói hay giữ bí mật / Lựa chọn 4: người mẹ biết gì?

Khoảng 109 giây · cảnh s24–s34 · 1417 ký tự

**Gemini**

```text
Giờ bạn biết sự thật. Bạn sẽ nói cho các em nhỏ biết ngay, hay giữ bí mật?

<short pause> Và các em nhỏ có thể vô tình nói ra. Một câu hỏi ngây thơ trong bữa tối cũng đủ để người mẹ biết có chuyện gì đó. Giữ bí mật cũng là để bảo vệ các em.

<short pause> Nếu nói ngay, các em sẽ hoảng sợ, khóc, và người mẹ sẽ phát hiện ngay lập tức. Kế hoạch sẽ sụp đổ trước khi bắt đầu.

<short pause> Emma, Norman và Ray chọn giữ bí mật, chỉ nói với vài người đủ lớn và đáng tin. Họ giả vờ như không biết gì, và âm thầm lên kế hoạch.

<short pause> Điểm cho lựa chọn giữ bí mật: một. <short pause> Nhưng Kaku muốn bạn để ý cái giá: phải cười mỗi ngày với người mà bạn biết là kẻ nuôi mình để bán.

<short pause> Người mẹ, Isabella, dường như luôn biết các con ở đâu. Bạn sẽ đoán cô biết bằng cách nào?

<short pause> Người mẹ cũng không bao giờ vội. Cô biết các con có ý định trốn, nhưng cô chơi một ván cờ dài: quan sát, đợi, và phá kế hoạch đúng lúc. Người mẹ là đối thủ đáng sợ nhất, vì cô cũng rất thông minh.

<short pause> Câu trả lời trong truyện: mỗi đứa trẻ đều mang một thiết bị theo dõi được cấy vào người từ khi còn nhỏ. Người mẹ chỉ cần nhìn vào một thiết bị là biết các con ở đâu.

<short pause> Và các con còn mang một con số ở cổ, được đánh dấu từ khi còn nhỏ. Mỗi đứa trẻ là một mã số.

<short pause> Nhóm Emma phải tìm ra thiết bị đó nằm ở đâu, và làm sao vô hiệu hóa nó mà không bị phát hiện. Nếu không, trốn chạy là vô ích.

<short pause> Điểm cho việc nghi ngờ và đi tìm thiết bị: một. Trong một nhà tù được thiết kế tốt, việc đầu tiên là tìm ra cai ngục nhìn thấy bạn bằng cách nào.
```

**ElevenLabs**

```text
Giờ bạn biết sự thật. [curious] Bạn sẽ nói cho các em nhỏ biết ngay, hay giữ bí mật?

[pause] Và các em nhỏ có thể vô tình nói ra. Một câu hỏi ngây thơ trong bữa tối cũng đủ để người mẹ biết có chuyện gì đó. Giữ bí mật cũng là để bảo vệ các em.

[pause] Nếu nói ngay, các em sẽ hoảng sợ, khóc, và người mẹ sẽ phát hiện ngay lập tức. Kế hoạch sẽ sụp đổ trước khi bắt đầu.

[pause] Emma, Norman và Ray chọn giữ bí mật, chỉ nói với vài người đủ lớn và đáng tin. Họ giả vờ như không biết gì, và âm thầm lên kế hoạch.

[pause] Điểm cho lựa chọn giữ bí mật: một. [pause] Nhưng Kaku muốn bạn để ý cái giá: phải cười mỗi ngày với người mà bạn biết là kẻ nuôi mình để bán.

[pause] Người mẹ, Isabella, dường như luôn biết các con ở đâu. Bạn sẽ đoán cô biết bằng cách nào?

[pause] Người mẹ cũng không bao giờ vội. Cô biết các con có ý định trốn, nhưng cô chơi một ván cờ dài: quan sát, đợi, và phá kế hoạch đúng lúc. Người mẹ là đối thủ đáng sợ nhất, vì cô cũng rất thông minh.

[pause] Câu trả lời trong truyện: mỗi đứa trẻ đều mang một thiết bị theo dõi được cấy vào người từ khi còn nhỏ. Người mẹ chỉ cần nhìn vào một thiết bị là biết các con ở đâu.

[pause] Và các con còn mang một con số ở cổ, được đánh dấu từ khi còn nhỏ. Mỗi đứa trẻ là một mã số.

[pause] Nhóm Emma phải tìm ra thiết bị đó nằm ở đâu, và làm sao vô hiệu hóa nó mà không bị phát hiện. Nếu không, trốn chạy là vô ích.

[pause] Điểm cho việc nghi ngờ và đi tìm thiết bị: một. Trong một nhà tù được thiết kế tốt, việc đầu tiên là tìm ra cai ngục nhìn thấy bạn bằng cách nào.
```

### c04 · Luật của trang trại / Lựa chọn 5: tin ai?

Khoảng 130 giây · cảnh s35–s45 · 1691 ký tự

**Gemini**

```text
Để trốn khỏi một hệ thống, phải hiểu nó. Grace Field không phải trang trại duy nhất. Nó là một trang trại cao cấp, nơi trẻ em được nuôi với sự chăm sóc tốt nhất.

<short pause> Vì sao phải chăm sóc tốt tới vậy? Vì bộ não được nuôi dưỡng tốt là thứ có giá nhất. Bài kiểm tra mỗi ngày, bữa ăn ngon, tình yêu của người mẹ, tất cả đều là một phần của quy trình.

<short pause> Và người mẹ không phải kẻ đến từ bên ngoài. Người mẹ từng là một đứa trẻ ở trang trại. Được chọn, được huấn luyện, và trở thành người chăn nuôi để được sống.

<short pause> Cái tên Miền đất hứa cũng liên quan tới một lời hứa cổ xưa giữa con người và những sinh vật ngoài cổng. Phần đó thuộc về những mùa sau, Kaku sẽ không nói thêm.

<short pause> Hiểu hệ thống giúp bạn thấy điểm yếu của nó: mọi thứ dựa vào niềm tin rằng trẻ em không biết gì. Khi các con biết, hệ thống bắt đầu nứt.

<short pause> Rồi xuất hiện một người lớn thứ hai: Sơ Krone, được gửi tới để giúp mẹ. Sơ có vẻ thù địch với mẹ, và muốn lật đổ mẹ để thay chỗ.

<short pause> Bạn có hợp tác với Sơ Krone không? Kẻ thù của kẻ thù có phải là bạn?

<short pause> Nhóm Emma chọn lợi dụng Sơ Krone một cách cẩn thận, trao đổi thông tin nhưng không tin hẳn. Sơ đưa cho họ vài manh mối quan trọng, trước khi bị chính hệ thống loại bỏ.

<short pause> Và có một câu hỏi khó hơn nữa: trong chính nhóm của bạn, ai là người đáng tin? Ray, người thông minh nhất, hóa ra đã biết sự thật từ lâu, và đã làm gián điệp cho mẹ.

<short pause> Ray đã đổi thông tin lấy những món đồ từ người mẹ, và từng món đều được cậu dùng cho kế hoạch trốn chạy. Một chiếc máy ảnh, những cuốn sách, những mảnh ghép nhỏ cho một bức tranh lớn.

<short pause> Nhưng Ray làm gián điệp để có cơ hội cứu các bạn. Cậu chơi một ván cờ hai mặt từ nhiều năm trước. Tin người không có nghĩa là tin mù quáng. Điểm cho lựa chọn hợp tác nhưng cảnh giác: một.
```

**ElevenLabs**

```text
Để trốn khỏi một hệ thống, phải hiểu nó. Grace Field không phải trang trại duy nhất. Nó là một trang trại cao cấp, nơi trẻ em được nuôi với sự chăm sóc tốt nhất.

[pause] [curious] Vì sao phải chăm sóc tốt tới vậy? Vì bộ não được nuôi dưỡng tốt là thứ có giá nhất. Bài kiểm tra mỗi ngày, bữa ăn ngon, tình yêu của người mẹ, tất cả đều là một phần của quy trình.

[pause] Và người mẹ không phải kẻ đến từ bên ngoài. Người mẹ từng là một đứa trẻ ở trang trại. Được chọn, được huấn luyện, và trở thành người chăn nuôi để được sống.

[pause] Cái tên Miền đất hứa cũng liên quan tới một lời hứa cổ xưa giữa con người và những sinh vật ngoài cổng. Phần đó thuộc về những mùa sau, Kaku sẽ không nói thêm.

[pause] Hiểu hệ thống giúp bạn thấy điểm yếu của nó: mọi thứ dựa vào niềm tin rằng trẻ em không biết gì. Khi các con biết, hệ thống bắt đầu nứt.

[pause] Rồi xuất hiện một người lớn thứ hai: Sơ Krone, được gửi tới để giúp mẹ. Sơ có vẻ thù địch với mẹ, và muốn lật đổ mẹ để thay chỗ.

[pause] Bạn có hợp tác với Sơ Krone không? Kẻ thù của kẻ thù có phải là bạn?

[pause] Nhóm Emma chọn lợi dụng Sơ Krone một cách cẩn thận, trao đổi thông tin nhưng không tin hẳn. Sơ đưa cho họ vài manh mối quan trọng, trước khi bị chính hệ thống loại bỏ.

[pause] Và có một câu hỏi khó hơn nữa: trong chính nhóm của bạn, ai là người đáng tin? Ray, người thông minh nhất, hóa ra đã biết sự thật từ lâu, và đã làm gián điệp cho mẹ.

[pause] Ray đã đổi thông tin lấy những món đồ từ người mẹ, và từng món đều được cậu dùng cho kế hoạch trốn chạy. Một chiếc máy ảnh, những cuốn sách, những mảnh ghép nhỏ cho một bức tranh lớn.

[pause] Nhưng Ray làm gián điệp để có cơ hội cứu các bạn. Cậu chơi một ván cờ hai mặt từ nhiều năm trước. Tin người không có nghĩa là tin mù quáng. Điểm cho lựa chọn hợp tác nhưng cảnh giác: một.
```

### c05 · Lựa chọn 6: đưa ai đi? / Lựa chọn 7: huấn luyện các em

Khoảng 120 giây · cảnh s46–s56 · 1558 ký tự

**Gemini**

```text
Đây là lựa chọn khó nhất. Kế hoạch trốn thoát có thể chỉ đưa được vài người lớn tuổi. Những em nhỏ bốn, năm tuổi sẽ làm chậm cả nhóm. Bạn sẽ đưa ai đi?

<short pause> Phương án A: chỉ những người đủ lớn, đủ nhanh. Tỉ lệ thành công cao hơn. Phương án B: đưa tất cả đi, không bỏ ai lại.

<short pause> Hãy tự hỏi thật lòng: nếu bạn là người mười một tuổi, biết rằng mỗi phút chậm trễ có thể khiến tất cả bị bắt, bạn có dám mang theo một em bé bốn tuổi không?

<short pause> Ray muốn phương án A. Norman thì tính toán thận trọng. <short pause> Nhưng Emma kiên quyết: không bỏ lại ai. Và chính lựa chọn của Emma định hình cả câu chuyện.

<short pause> <laugh> Kaku phải nói: về logic thuần túy, phương án A an toàn hơn. <short pause> Nhưng Miền đất hứa không chấm điểm bằng logic thuần túy. Truyện chấm điểm bằng việc bạn vẫn là người sau khi thoát ra.

<short pause> Kaku cho phương án B: hai điểm. Vì truyện cho thấy những em nhỏ cũng có thể làm được rất nhiều, nếu được tin tưởng và dạy dỗ.

<short pause> Họ còn phải tính tới cả những em bé chưa biết đi, và những em mới bốn tuổi. Kế hoạch trở thành một bài toán hậu cần: ai bế ai, ai dẫn ai, ai đi trước, ai đi sau.

<short pause> Muốn đưa tất cả đi, phải chuẩn bị cho tất cả. Nhóm Emma biến những trò chơi hằng ngày thành bài huấn luyện: trốn tìm để học ẩn nấp, đuổi bắt để học chạy nhanh.

<short pause> Họ dạy các em nhớ đường, làm theo tín hiệu, và giữ bình tĩnh. Người mẹ nhìn thấy các con chơi, nhưng không thấy các con đang tập.

<short pause> Kaku rất thích chi tiết này. Nó giống như ngoài đời: một nhóm mạnh không phải vì có một người giỏi, mà vì ai cũng được chuẩn bị.

<short pause> Điểm cho việc huấn luyện: một. Kế hoạch tốt tới đâu cũng vô ích nếu những người thực hiện nó không sẵn sàng.
```

**ElevenLabs**

```text
Đây là lựa chọn khó nhất. Kế hoạch trốn thoát có thể chỉ đưa được vài người lớn tuổi. Những em nhỏ bốn, năm tuổi sẽ làm chậm cả nhóm. [curious] Bạn sẽ đưa ai đi?

[pause] Phương án A: chỉ những người đủ lớn, đủ nhanh. Tỉ lệ thành công cao hơn. Phương án B: đưa tất cả đi, không bỏ ai lại.

[pause] Hãy tự hỏi thật lòng: nếu bạn là người mười một tuổi, biết rằng mỗi phút chậm trễ có thể khiến tất cả bị bắt, bạn có dám mang theo một em bé bốn tuổi không?

[pause] Ray muốn phương án A. Norman thì tính toán thận trọng. [pause] Nhưng Emma kiên quyết: không bỏ lại ai. Và chính lựa chọn của Emma định hình cả câu chuyện.

[pause] [chuckles] Kaku phải nói: về logic thuần túy, phương án A an toàn hơn. [pause] Nhưng Miền đất hứa không chấm điểm bằng logic thuần túy. Truyện chấm điểm bằng việc bạn vẫn là người sau khi thoát ra.

[pause] Kaku cho phương án B: hai điểm. Vì truyện cho thấy những em nhỏ cũng có thể làm được rất nhiều, nếu được tin tưởng và dạy dỗ.

[pause] Họ còn phải tính tới cả những em bé chưa biết đi, và những em mới bốn tuổi. Kế hoạch trở thành một bài toán hậu cần: ai bế ai, ai dẫn ai, ai đi trước, ai đi sau.

[pause] Muốn đưa tất cả đi, phải chuẩn bị cho tất cả. Nhóm Emma biến những trò chơi hằng ngày thành bài huấn luyện: trốn tìm để học ẩn nấp, đuổi bắt để học chạy nhanh.

[pause] Họ dạy các em nhớ đường, làm theo tín hiệu, và giữ bình tĩnh. Người mẹ nhìn thấy các con chơi, nhưng không thấy các con đang tập.

[pause] Kaku rất thích chi tiết này. Nó giống như ngoài đời: một nhóm mạnh không phải vì có một người giỏi, mà vì ai cũng được chuẩn bị.

[pause] Điểm cho việc huấn luyện: một. Kế hoạch tốt tới đâu cũng vô ích nếu những người thực hiện nó không sẵn sàng.
```

### c06 · Lựa chọn 8: bức tường và vách đá / Lựa chọn 9: khi kế hoạch đổ vỡ

Khoảng 106 giây · cảnh s57–s66 · 1372 ký tự

**Gemini**

```text
Bạn nghĩ lối thoát là cánh cổng? Không. Cổng được canh gác. Nhóm Emma khám phá ra khu rừng kết thúc bằng một bức tường cao, và sau bức tường là một vách đá.

<short pause> Để vượt qua, họ phải chuẩn bị dây, tính toán độ cao, và tìm cách đưa cả những em nhỏ nhất qua vực.

<short pause> Họ học cách nhận biết giới hạn tầm phát hiện của thiết bị, và chọn đúng thời điểm để hành động. Mỗi chi tiết nhỏ đều có thể quyết định sống hay chết.

<short pause> Và họ cũng phải đối mặt với thiết bị theo dõi. Emma quyết định tự tay xử lý thiết bị trong tai mình. Một cái giá bằng đau đớn, để đổi lấy tự do.

<short pause> Điểm cho việc tìm đúng lối thoát: một. Lối ra hiển nhiên thường là lối ra được canh gác kỹ nhất.

<short pause> Rồi mọi thứ đổ vỡ. Norman, người lên kế hoạch giỏi nhất, bị đưa đi trước ngày trốn thoát. Anh chấp nhận ra đi để không làm lộ kế hoạch của các bạn.

<short pause> Trước khi đi, Norman để lại những gì cậu biết cho Emma và Ray. Một kế hoạch tốt không phụ thuộc vào một người duy nhất. Nó phải được chia sẻ, để tiếp tục kể cả khi người lên kế hoạch không còn.

<short pause> Bạn sẽ làm gì khi mất người quan trọng nhất trong kế hoạch? Bỏ cuộc, hay tiếp tục?

<short pause> Emma và Ray tiếp tục. Ray thậm chí định hy sinh chính mình trong một kế hoạch đốt cháy căn nhà để che giấu cuộc trốn chạy. Và Emma, một lần nữa, không chịu bỏ lại ai, kể cả Ray.

<short pause> Điểm cho việc tiếp tục khi kế hoạch đổ vỡ: một. Không kế hoạch nào đi đúng như dự tính. Người sống sót là người biết đổi kế hoạch.
```

**ElevenLabs**

```text
[curious] Bạn nghĩ lối thoát là cánh cổng? Không. Cổng được canh gác. Nhóm Emma khám phá ra khu rừng kết thúc bằng một bức tường cao, và sau bức tường là một vách đá.

[pause] Để vượt qua, họ phải chuẩn bị dây, tính toán độ cao, và tìm cách đưa cả những em nhỏ nhất qua vực.

[pause] Họ học cách nhận biết giới hạn tầm phát hiện của thiết bị, và chọn đúng thời điểm để hành động. Mỗi chi tiết nhỏ đều có thể quyết định sống hay chết.

[pause] Và họ cũng phải đối mặt với thiết bị theo dõi. Emma quyết định tự tay xử lý thiết bị trong tai mình. Một cái giá bằng đau đớn, để đổi lấy tự do.

[pause] Điểm cho việc tìm đúng lối thoát: một. Lối ra hiển nhiên thường là lối ra được canh gác kỹ nhất.

[pause] Rồi mọi thứ đổ vỡ. Norman, người lên kế hoạch giỏi nhất, bị đưa đi trước ngày trốn thoát. Anh chấp nhận ra đi để không làm lộ kế hoạch của các bạn.

[pause] Trước khi đi, Norman để lại những gì cậu biết cho Emma và Ray. Một kế hoạch tốt không phụ thuộc vào một người duy nhất. Nó phải được chia sẻ, để tiếp tục kể cả khi người lên kế hoạch không còn.

[pause] Bạn sẽ làm gì khi mất người quan trọng nhất trong kế hoạch? Bỏ cuộc, hay tiếp tục?

[pause] Emma và Ray tiếp tục. Ray thậm chí định hy sinh chính mình trong một kế hoạch đốt cháy căn nhà để che giấu cuộc trốn chạy. Và Emma, một lần nữa, không chịu bỏ lại ai, kể cả Ray.

[pause] Điểm cho việc tiếp tục khi kế hoạch đổ vỡ: một. Không kế hoạch nào đi đúng như dự tính. Người sống sót là người biết đổi kế hoạch.
```

### c07 · Lựa chọn 10: đêm trốn thoát / Bạn sống sót bao lâu? / Góc nhìn của Kaku

Khoảng 146 giây · cảnh s67–s80 · 1896 ký tự

**Gemini**

```text
Đêm trốn thoát. Mười lăm đứa trẻ từ năm tuổi trở lên vượt qua bức tường. Những em còn quá nhỏ ở lại, với lời hứa sẽ quay lại đón.

<short pause> Và người mẹ Isabella, người đã nuôi và bán bao nhiêu đứa trẻ, đứng nhìn các con biến mất vào màn đêm. Cô thua, và lần đầu tiên, cô thật lòng chúc các con may mắn.

<short pause> Vì vậy Isabella không hẳn là một phản diện thuần túy. Cô là kết quả của chính hệ thống ấy: một đứa trẻ đã chọn sống sót bằng cách chấp nhận luật chơi. Truyện để người xem tự cảm nhận về cô.

<short pause> Kaku để ý: Isabella cũng từng là một đứa trẻ ở Grace Field. Cô từng chọn con đường sống sót bằng cách trở thành người chăn nuôi. Emma chọn con đường ngược lại.

<short pause> Điểm cho việc cùng nhau vượt qua: một. Bạn đã ra khỏi Grace Field. <short pause> Nhưng thế giới bên ngoài còn nguy hiểm hơn nhiều.

<short pause> Tổng kết điểm. Tối đa mười một điểm. Nếu bạn được từ chín tới mười một: bạn giống nhóm Emma. Bạn thoát được, và giữ được con người mình.

<short pause> Từ năm tới tám: bạn có thể thoát, nhưng sẽ phải trả giá, có thể là bỏ lại ai đó, hoặc bị phát hiện giữa chừng.

<short pause> Dưới năm: bạn ở lại Grace Field, sống những ngày hạnh phúc trong ảo tưởng, cho tới ngày tới lượt mình. Kaku sẽ không nói thêm.

<short pause> Và thêm một câu hỏi: nếu bạn là Emma, Norman hay Ray, bạn sẽ là ai? <laugh> Kaku đoán Kaku là Ray, vì Kaku cũng thích đọc sách một mình. <short pause> Nhưng Kaku muốn trở thành Emma.

<short pause> Viết điểm của bạn vào bình luận nhé. Và cho Kaku biết lựa chọn nào khó nhất với bạn.

<short pause> Miền đất hứa là một câu chuyện kinh dị, nhưng Kaku nghĩ nó thật ra là câu chuyện về giáo dục và tự do.

<short pause> Và những em nhỏ ở lại không bị bỏ rơi. Lời hứa quay lại đón các em trở thành động lực cho cả những phần sau của câu chuyện.

<short pause> Trường học tốt nhất trong truyện lại là một trang trại. Và những đứa trẻ thoát ra nhờ chính những gì trang trại dạy chúng: suy nghĩ, tính toán, và tin nhau.

<short pause> Câu hỏi của truyện dành cho mỗi người: nếu phát hiện thế giới mình sống không như vẻ ngoài, bạn sẽ im lặng để được yên ổn, hay dũng cảm bước ra?
```

**ElevenLabs**

```text
Đêm trốn thoát. Mười lăm đứa trẻ từ năm tuổi trở lên vượt qua bức tường. Những em còn quá nhỏ ở lại, với lời hứa sẽ quay lại đón.

[pause] Và người mẹ Isabella, người đã nuôi và bán bao nhiêu đứa trẻ, đứng nhìn các con biến mất vào màn đêm. Cô thua, và lần đầu tiên, cô thật lòng chúc các con may mắn.

[pause] Vì vậy Isabella không hẳn là một phản diện thuần túy. Cô là kết quả của chính hệ thống ấy: một đứa trẻ đã chọn sống sót bằng cách chấp nhận luật chơi. Truyện để người xem tự cảm nhận về cô.

[pause] Kaku để ý: Isabella cũng từng là một đứa trẻ ở Grace Field. Cô từng chọn con đường sống sót bằng cách trở thành người chăn nuôi. Emma chọn con đường ngược lại.

[pause] Điểm cho việc cùng nhau vượt qua: một. Bạn đã ra khỏi Grace Field. [pause] Nhưng thế giới bên ngoài còn nguy hiểm hơn nhiều.

[pause] Tổng kết điểm. Tối đa mười một điểm. Nếu bạn được từ chín tới mười một: bạn giống nhóm Emma. Bạn thoát được, và giữ được con người mình.

[pause] Từ năm tới tám: bạn có thể thoát, nhưng sẽ phải trả giá, có thể là bỏ lại ai đó, hoặc bị phát hiện giữa chừng.

[pause] Dưới năm: bạn ở lại Grace Field, sống những ngày hạnh phúc trong ảo tưởng, cho tới ngày tới lượt mình. Kaku sẽ không nói thêm.

[pause] [curious] Và thêm một câu hỏi: nếu bạn là Emma, Norman hay Ray, bạn sẽ là ai? [chuckles] Kaku đoán Kaku là Ray, vì Kaku cũng thích đọc sách một mình. [pause] Nhưng Kaku muốn trở thành Emma.

[pause] Viết điểm của bạn vào bình luận nhé. Và cho Kaku biết lựa chọn nào khó nhất với bạn.

[pause] Miền đất hứa là một câu chuyện kinh dị, nhưng Kaku nghĩ nó thật ra là câu chuyện về giáo dục và tự do.

[pause] Và những em nhỏ ở lại không bị bỏ rơi. Lời hứa quay lại đón các em trở thành động lực cho cả những phần sau của câu chuyện.

[pause] Trường học tốt nhất trong truyện lại là một trang trại. Và những đứa trẻ thoát ra nhờ chính những gì trang trại dạy chúng: suy nghĩ, tính toán, và tin nhau.

[pause] Câu hỏi của truyện dành cho mỗi người: nếu phát hiện thế giới mình sống không như vẻ ngoài, bạn sẽ im lặng để được yên ổn, hay dũng cảm bước ra?
```

### c08 · Kết

Khoảng 40 giây · cảnh s81–s83 · 523 ký tự

**Gemini**

```text
Miền đất hứa bắt đầu bằng một ngôi nhà hạnh phúc và kết thúc mùa một bằng những đứa trẻ chạy vào bóng tối. <short pause> Nhưng đó là bóng tối mà chúng tự chọn, và vì thế nó mang tên tự do.

<short pause> Video tiếp theo, Kaku trải một dòng thời gian dài hai nghìn năm: Attack on Titan, từ Ymir đầu tiên tới những bức tường, và cuộc chiến cuối cùng.

<short pause> Nếu bạn thích những video đặt bạn vào trong thế giới anime, hãy đăng ký kênh. Và nếu một ngày ai đó hứa cho bạn một thiên đường không có luật lệ, hãy kiểm tra cánh cổng trước. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Miền đất hứa bắt đầu bằng một ngôi nhà hạnh phúc và kết thúc mùa một bằng những đứa trẻ chạy vào bóng tối. [pause] Nhưng đó là bóng tối mà chúng tự chọn, và vì thế nó mang tên tự do.

[pause] Video tiếp theo, Kaku trải một dòng thời gian dài hai nghìn năm: Attack on Titan, từ Ymir đầu tiên tới những bức tường, và cuộc chiến cuối cùng.

[pause] Nếu bạn thích những video đặt bạn vào trong thế giới anime, hãy đăng ký kênh. Và nếu một ngày ai đó hứa cho bạn một thiên đường không có luật lệ, hãy kiểm tra cánh cổng trước. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
