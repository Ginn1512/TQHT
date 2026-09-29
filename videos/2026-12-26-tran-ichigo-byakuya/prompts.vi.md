# Bộ prompt · Bleach: Phân tích trận Ichigo vs Byakuya theo từng hiệp

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 9 đoạn đọc, khoảng 15.2 phút giọng.
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

Lời: Cảnh báo: video có spoiler Bleach tới hết arc Soul Society, tức khoảng sáu mươi tập đầu của anime. Không có s…

```text
Wide 16:9 landscape cinematic frame. a tall white tower on a hill under a dark stormy sky, a single closed notebook resting on a stone step at its base, wide establishing shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trên đồi Song Cực, hai người cầm kiếm đứng đối diện nhau. Một người là đội trưởng đội sáu, trưởng tộc của một…

```text
Wide 16:9 landscape cinematic frame. an elegant noble swordsman silhouette in a long white captain's coat standing calmly on a hilltop, wind blowing, low-angle shot, cold rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Người kia là một cậu học sinh mười lăm tuổi, vừa học Bankai được đúng ba ngày, trong khi người bình thường mấ…

```text
Wide 16:9 landscape cinematic frame. a teenage swordsman silhouette in a black robe standing opposite, gripping a sword with both hands, determined stance, low-angle shot, warm rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Bối cảnh: Rukia, người đã trao sức mạnh tử thần cho Ichigo, bị kết án tử vì phạm luật. Ichigo cùng bạn bè xôn…

```text
Wide 16:9 landscape cinematic frame. a small group of teenage silhouettes running across rooftops of a vast walled city of white buildings, wide aerial shot, bright dramatic sky. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Nếu phải đặt cược trước trận, Kaku nghĩ gần như ai ở Soul Society cũng sẽ đặt vào vị đội trưởng. Vậy mà người…

```text
Wide 16:9 landscape cinematic frame. a betting board with two columns, one overflowing with coins, the other almost empty, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình phân tích trận Kurosaki Ichigo đối đầu Kuchiki Byakuya theo từng hiệ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a tactical map on a table with two small chess pieces, one white and one black, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Kaku sẽ kể bằng sơ đồ và tranh tự vẽ, không dựng lại cảnh trong anime. Cuối video là ba bài học chiến thuật m…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn tactical diagram with arrows, circles and small sword icons on parchment, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Trước trận: hồ sơ hai đấu thủ

Lời: Đấu thủ thứ nhất, Byakuya. Kiếm của anh tên là Thiên Bản Anh. Khi giải phóng, lưỡi kiếm vỡ thành hàng nghìn m…

```text
Wide 16:9 landscape cinematic frame. a sword blade dissolving into thousands of tiny glowing pink petals that swirl around its hilt, close-up, dramatic cherry blossom light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Gia tộc Kuchiki là một trong những gia tộc quý tộc lớn nhất Soul Society. Byakuya là trưởng tộc, nghĩa là mọi…

```text
Wide 16:9 landscape cinematic frame. a grand traditional estate with white walls and a quiet garden, a lone figure standing on the veranda, wide shot, cool elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Anh còn là bậc thầy Thuấn bộ, kiểu di chuyển nhanh tới mức như biến mất. Anh ít nói, không bao giờ vội vàng,…

```text
Wide 16:9 landscape cinematic frame. a noble figure appearing behind an opponent with only a faint afterimage left where he stood, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Ichigo là một tử thần thay thế: một con người được Rukia trao sức mạnh trong một đêm khẩn cấp. Cậu chưa từng…

```text
Wide 16:9 landscape cinematic frame. a teenager in a black robe standing in his ordinary bedroom at night, looking at his own hands in disbelief, medium shot, moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Đấu thủ thứ hai, Ichigo. Kiếm của cậu tên là Trảm Nguyệt, to và nặng. Cậu mạnh về sức và ý chí, nhưng thiếu k…

```text
Wide 16:9 landscape cinematic frame. a very large broad cleaver-like blade planted in the ground beside a resting teenager, close-up, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Cậu vừa học Bankai bằng một phương pháp đặc biệt trong ba ngày, dưới sự giám sát của Yoruichi. Nghĩa là cậu c…

```text
Wide 16:9 landscape cinematic frame. a teenager training exhausted in a vast underground cavern with rocky cliffs, a cat silhouette sitting on a rock watching, wide shot, dim warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Động cơ của hai người cũng khác nhau. Ichigo tới để cứu Rukia khỏi án tử. Byakuya là anh nuôi của Rukia, nhưn…

```text
Wide 16:9 landscape cinematic frame. a condemned young woman silhouette standing on a tall execution platform, two swordsmen facing each other far below, wide shot, stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Bảng tỉ số trước trận: kinh nghiệm, kỹ thuật và tốc độ nghiêng về Byakuya. Sức bền và ý chí nghiêng về Ichigo…

```text
Wide 16:9 landscape cinematic frame. a scoreboard showing 3 to 2 with small icons for experience, technique, speed on one side and stamina, will on the other, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Hiệp 0: món nợ cũ

Lời: Thật ra đây là lần gặp thứ hai. Lần đầu là ở thế giới người, khi Soul Society tới bắt Rukia. Ichigo lao vào,…

```text
Wide 16:9 landscape cinematic frame. a rainy city street at night, a teenager falling to the wet pavement while a calm swordsman walks away, wide shot, cold streetlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Để lấy lại sức mạnh, Ichigo phải qua một bài huấn luyện nguy hiểm của Urahara: bị trói linh hồn dưới đáy một…

```text
Wide 16:9 landscape cinematic frame. a teenager sitting at the bottom of a deep rocky pit, looking up at a distant circle of light, a broken chain on his chest, wide shot, dim dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Cậu thành công, và lần đầu tiên có được thanh Trảm Nguyệt của chính mình. Tức là thất bại trước Byakuya đã bu…

```text
Wide 16:9 landscape cinematic frame. a teenager climbing out of a pit holding a huge sword, light breaking over the edge, low-angle shot, triumphant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Byakuya không chỉ đánh bại cậu. Anh cắt đứt nguồn linh lực của cậu, khiến cậu mất hết sức mạnh tử thần. Cậu p…

```text
Wide 16:9 landscape cinematic frame. a glowing thread snapping inside a translucent chest silhouette, fading particles drifting away, extreme close-up, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Mục tiêu của Ichigo ở hiệp này rất đơn giản: xông lên. Lựa chọn của cậu: dùng hết sức. Cái giá: suýt mất mạng…

```text
Wide 16:9 landscape cinematic frame. a three-row tactical note card: goal, choice, cost, filled with short handwritten icons, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bài học của hiệp không là ý chí thôi chưa đủ. Chính vì thua trận này, Ichigo mới chịu học hỏi t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a small zero on a scoreboard and circling it with the note lesson learned. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Hiệp 1: tốc độ

Lời: Trận tái đấu trên đồi Song Cực bắt đầu. Byakuya ra đòn bằng Thuấn bộ, như lần trước. Nhưng lần này, Ichigo th…

```text
Wide 16:9 landscape cinematic frame. two blurred figures crossing paths at high speed on a rocky hilltop, sparks where their blades meet, dynamic wide shot, stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Đây là thành quả của những ngày tập với Yoruichi, người được mệnh danh là nữ thần Thuấn bộ. Byakuya không nói…

```text
Wide 16:9 landscape cinematic frame. a close-up of a calm face in shadow with a single eye narrowing slightly, cold rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Với Byakuya, tốc độ luôn là cách giữ khoảng cách: ra đòn rồi biến mất, không bao giờ để đối thủ chạm vào mình…

```text
Wide 16:9 landscape cinematic frame. two figures on a hilltop with a dotted line between them shrinking step by step, parchment diagram overlay, cold light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Sơ đồ hiệp một: Byakuya muốn kết thúc nhanh bằng tốc độ. Ichigo chứng minh cậu không còn là người của lần trư…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram with two arrows running side by side at equal length, a small heart icon next to the black piece, parchment top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mà tập Thuấn bộ ba ngày thì chắc chỉ nhanh hơn được… con rùa trong video Gojo. Mà con rùa đó còn không b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot running in place with a small tortoise calmly walking ahead of it, comic expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Kaku để ý điều này rất hay: trong một trận đấu giữa người mạnh và người yếu hơn, chỉ cần người yếu hơn chứng…

```text
Wide 16:9 landscape cinematic frame. two chess pieces on a board, the smaller one standing firm as a crack appears in the board near the larger one, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Hiệp 2: nghìn cánh hoa

Lời: Byakuya giải phóng Thiên Bản Anh. Hàng nghìn lưỡi dao nhỏ xíu tràn ra như một cơn bão cánh hoa, và gần như kh…

```text
Wide 16:9 landscape cinematic frame. a storm of glowing pink petals flooding across a rocky hilltop toward a lone swordsman, wide dynamic shot, dramatic pink and navy light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Thiên Bản Anh còn có một điểm đáng sợ: Byakuya đứng yên vẫn tấn công được. Anh không cần tới gần, chỉ cần một…

```text
Wide 16:9 landscape cinematic frame. a calm figure standing still with one hand slightly raised while a river of petals bends through the air around him, medium shot, pink and navy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trong khi đó Ichigo chỉ có một cách tấn công: chạy tới và chém. Khoảng cách chính là thứ Byakuya dùng để thắn…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram showing a long distance line between two pieces filled with swirling dots, parchment top-down shot, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Vấn đề của Ichigo là thanh kiếm to của cậu chỉ chặn được một hướng. Còn cánh hoa tấn công từ mọi hướng cùng l…

```text
Wide 16:9 landscape cinematic frame. a diagram showing a single wide shield blocking arrows from the front while dozens of tiny arrows curve around from the sides and back, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Cậu cố chém, cố né, cố xông thẳng vào người điều khiển. Nhưng mỗi lần xông tới, cơn bão lại cắt thêm vài vết…

```text
Wide 16:9 landscape cinematic frame. a wounded teenager pushing forward through a swirling wall of petals, shielding his face with his arm, medium shot, harsh backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Sơ đồ hiệp hai: Byakuya chọn đánh bằng số lượng. Ichigo chọn đánh bằng sức mạnh đơn lẻ. Và số lượng thắng. Hi…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram with hundreds of small dots surrounding a single large dot, the large dot marked with small red cuts, parchment top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Cái giá cho Ichigo: mất máu, và nhận ra rằng cách đánh cũ không dùng được nữa. Muốn thắng, cậu phải đổi cách…

```text
Wide 16:9 landscape cinematic frame. a drop of blood falling onto a rock beside a large sword, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử đếm số cánh hoa trong cảnh này để làm sơ đồ chính xác. Tới cánh thứ ba trăm thì Kaku quyết định làm…

```text
Wide 16:9 landscape cinematic frame. the owl mascot buried under a pile of pink petal sketches, holding up a sign with the word many. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Hiệp 3: Bankai đấu Bankai

Lời: Ichigo giải phóng Bankai. Nhưng khác với mọi người mong đợi, thanh kiếm không to hơn. Nó thu nhỏ lại thành mộ…

```text
Wide 16:9 landscape cinematic frame. a slim black sword with a chain dangling from its hilt held in one hand, dark energy swirling faintly around it, close-up, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Đây là Bankai tên Thiên Tỏa Trảm Nguyệt. Toàn bộ sức mạnh được nén vào một lưỡi kiếm nhỏ, để Ichigo di chuyển…

```text
Wide 16:9 landscape cinematic frame. a diagram of a large sword shape being compressed into a thin line with arrows pointing inward, a speed trail behind it, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Byakuya thậm chí tỏ ra khó chịu. Một kẻ vừa học Bankai ba ngày dám đứng ngang hàng với anh, ở cùng cấp độ sức…

```text
Wide 16:9 landscape cinematic frame. a close-up of a noble swordsman's hand tightening on a sword hilt, a single petal trembling in the air, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Byakuya đáp trả bằng Bankai của mình. Những thanh kiếm khổng lồ mọc lên từ mặt đất, rồi vỡ ra thành hàng trăm…

```text
Wide 16:9 landscape cinematic frame. rows of giant blades rising out of the ground in a vast dark space, dissolving into an ocean of glowing petals, wide shot, pink and black light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nhiều người nghĩ Bankai càng to càng mạnh. Trận này chứng minh điều ngược lại: không phải kích thước, mà là c…

```text
Wide 16:9 landscape cinematic frame. a giant empty suit of armor next to a small nimble fighter, the fighter clearly faster, humorous comparison illustration, parchment style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Đây là cuộc đối đầu thú vị nhất về chiến thuật: một bên nén tất cả vào một điểm, một bên trải tất cả ra khắp…

```text
Wide 16:9 landscape cinematic frame. a split diagram: one tiny concentrated star on the left, a vast diffuse cloud on the right, parchment top-down shot, amber and pink ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Ichigo còn giải thích cho Byakuya rằng Bankai của cậu không to, vì nó dồn hết sức mạnh vào tốc độ. Một lời gi…

```text
Wide 16:9 landscape cinematic frame. a teenager holding a slim black sword up between himself and his opponent as if showing it, dramatic low-angle shot, dark swirling light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Với tốc độ mới, Ichigo không cần chặn cánh hoa nữa. Cậu né, chém xuyên qua khe hở, và lần đầu tiên chạm được…

```text
Wide 16:9 landscape cinematic frame. a black blur slicing a clean path through a wall of petals, a thin cut appearing on a white sleeve, dynamic close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Sơ đồ hiệp ba: Byakuya chọn phủ kín không gian. Ichigo chọn tốc độ để đi xuyên qua khe hở. Hiệp này nghiêng v…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram with a fast line weaving through gaps in a cloud of dots, a small score of 2 to 1 written in the corner, parchment top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Cái giá cho Ichigo: tốc độ cực cao đòi hỏi cơ thể rất nhiều. Cậu học Bankai trong ba ngày, nên chưa biết giới…

```text
Wide 16:9 landscape cinematic frame. a teenager's hand trembling as it grips a slim black sword, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Hiệp 4: kẻ thù bên trong

Lời: Rồi tới khoảnh khắc mà người xem lần đầu không hiểu chuyện gì xảy ra. Giữa trận, một nửa khuôn mặt Ichigo bị…

```text
Wide 16:9 landscape cinematic frame. a close-up of a face half covered by a cracked white bone-like mask, the visible eye glowing, dark energy bursting around, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Thứ sức mạnh ấy không giống của tử thần. Nó thô bạo, không có kỹ thuật, chỉ muốn phá hủy. Và nó không nghe lờ…

```text
Wide 16:9 landscape cinematic frame. a shadowy twin silhouette of the teenager with white glowing eyes grinning in a dark reflection on a broken sword blade, extreme close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Đó là Hollow ẩn trong cậu, một thực thể muốn chiếm lấy cơ thể. Trong vài giây, sức mạnh của Ichigo tăng vọt,…

```text
Wide 16:9 landscape cinematic frame. a dark figure bursting forward with wild energy, the calm opponent stepping back for the first time, wide shot, black and red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Nhưng Ichigo tự đập vỡ chiếc mặt nạ. Cậu không muốn thắng bằng thứ sức mạnh không phải của mình.

```text
Wide 16:9 landscape cinematic frame. a hand gripping and shattering a white mask into fragments, extreme close-up, fragments flying, dramatic backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Sơ đồ hiệp bốn: Ichigo có một lựa chọn dễ để thắng nhanh, và cậu từ chối nó. Về điểm số, hiệp này hòa. Về con…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram with two paths from the black piece: a short glowing red path crossed out, a longer honest path highlighted, parchment top-down shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Kaku thấy đây là một chi tiết kể chuyện rất khéo: cùng một trận đấu, Ichigo phải đánh hai kẻ thù cùng lúc, mộ…

```text
Wide 16:9 landscape cinematic frame. a split diagram with one arrow pointing outward toward an opponent and another arrow pointing inward toward a small shadow inside the chest, parchment style. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Cái giá: cậu đã dùng rất nhiều sức lực để kìm Hollow lại, trong khi trận đấu còn chưa kết thúc.

```text
Wide 16:9 landscape cinematic frame. a nearly empty glowing energy bar drawn on parchment beside a small black sword icon, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thêm: Hollow của Ichigo là một bí ẩn lớn mà Bleach giải thích dần ở những arc sau. Hôm nay Kaku…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quickly covering a page of its notebook with a white paper mask sticker, looking mischievous. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Hiệp 5: hình thái thật của Thiên Bản Anh

Lời: Lần đầu tiên, Byakuya dùng tới hình thái mà anh dành riêng cho kẻ thù anh thề tự tay giết. Những cánh hoa tụ…

```text
Wide 16:9 landscape cinematic frame. a vast circle of a thousand floating swords arranged in four rotating rings around two small figures, top-down wide shot, pink and silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Hình thái này yêu cầu Byakuya tự cầm kiếm lao vào. Người đã quen chiến đấu từ xa giờ phải bước vào tầm đánh c…

```text
Wide 16:9 landscape cinematic frame. a noble swordsman stepping forward into close range with a single glowing sword in hand, medium shot, tense dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Đây là một lựa chọn chiến thuật rất đáng chú ý. Byakuya từ bỏ lợi thế tấn công từ xa bằng cơn bão cánh hoa, đ…

```text
Wide 16:9 landscape cinematic frame. a diagram showing a wide cloud of dots collapsing into a ring of sharp swords around a center, parchment style, amber and pink ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Anh còn gom cánh hoa thành một đôi cánh trắng sau lưng, dồn tất cả vào một đòn cuối.

```text
Wide 16:9 landscape cinematic frame. a noble swordsman silhouette with glowing white feathered wings made of light petals unfolding behind him, low-angle shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Với một người luôn giữ khoảng cách với mọi người như Byakuya, việc tự bước lại gần một đối thủ có lẽ là thay…

```text
Wide 16:9 landscape cinematic frame. two figures standing close within a quiet circle of floating swords, the space between them small for the first time, close-up, warm light breaking through. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Kaku đọc lựa chọn này như một sự thừa nhận: Byakuya cuối cùng coi Ichigo là đối thủ ngang hàng, đáng để anh đ…

```text
Wide 16:9 landscape cinematic frame. two swordsmen standing inside the ring of blades, now facing each other as equals, wide shot, balanced dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Kaku để ý: nếu nhìn trận đấu từ trên cao, sơ đồ hiệp năm giống hệt sơ đồ hiệp ba, chỉ là hai quân cờ đã đổi c…

```text
Wide 16:9 landscape cinematic frame. two nearly identical tactical diagrams side by side, the black and white pieces swapped in the second, parchment top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Sơ đồ hiệp năm: Byakuya chọn dồn toàn lực vào một điểm, giống cách Ichigo làm với Bankai. Hai người giờ chơi…

```text
Wide 16:9 landscape cinematic frame. a tactical diagram with two concentrated stars facing each other at close range, parchment top-down shot, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Hiệp 6: đòn cuối

Lời: Hai người lao vào nhau. Nguyệt Nha Thiên Xung màu đen của Ichigo va vào đòn cánh trắng của Byakuya.

```text
Wide 16:9 landscape cinematic frame. a black crescent wave of energy colliding with a white wave of light petals in the center of a stormy hill, wide dynamic shot, black and white light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Khi khói tan, cả hai vẫn đứng. Nhưng thanh kiếm của Byakuya đã gãy, và người lùi bước là anh.

```text
Wide 16:9 landscape cinematic frame. a broken sword blade lying on cracked stone, smoke clearing around two standing silhouettes, medium shot, soft grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và chỉ ít lâu sau, khi một đội trưởng phản bội tấn công Rukia, chính Byakuya lấy thân mình đỡ đòn cho cô. Ngư…

```text
Wide 16:9 landscape cinematic frame. a wounded noble figure standing in front of a young woman, shielding her with his body as a long blade strikes, dramatic medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Byakuya nói rằng anh đã thua, và thanh kiếm của anh không còn muốn chém Ichigo nữa. Kaku thấy đây là cách thu…

```text
Wide 16:9 landscape cinematic frame. a noble figure turning away with his long coat torn, walking slowly into the mist, back view, melancholic light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nhưng hãy nhớ: Ichigo cũng đã ở sát giới hạn. Sau trận, cậu gần như không thể cử động. Trận này không có ngườ…

```text
Wide 16:9 landscape cinematic frame. a teenager kneeling on one knee, leaning on a slim black sword to stay upright, exhausted, medium shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku chấm như vậy vì điểm số chỉ đo từng hiệp. Nếu chấm cả trận, có lẽ phải thêm một cột cho thứ không đo đượ…

```text
Wide 16:9 landscape cinematic frame. a scoreboard with an extra blank column labeled with a question mark added by hand, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Tỉ số chung cuộc theo sơ đồ của Kaku: ba – hai cho Ichigo, sau khi bị dẫn trước. Một cuộc lội ngược dòng thật…

```text
Wide 16:9 landscape cinematic frame. a scoreboard updated to 3 to 2 in favor of the black piece, confetti of petals falling, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Sau trận: lý do của Byakuya

Lời: Sau trận, Bleach mới cho ta biết vì sao Byakuya lạnh lùng tới vậy. Rukia là em gái của người vợ quá cố của an…

```text
Wide 16:9 landscape cinematic frame. an old family portrait of a gentle woman placed on a small altar with a single candle, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hisana từng bỏ rơi em gái khi còn nhỏ vì hoàn cảnh, và day dứt suốt phần đời còn lại. Trước khi mất, cô nhờ B…

```text
Wide 16:9 landscape cinematic frame. a young woman lying weakly in a bed by a window, holding the hand of a man sitting beside her, soft evening light, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Anh đã hứa với vợ sẽ bảo vệ Rukia. Nhưng anh cũng đã thề trước cha mẹ mình sẽ không bao giờ phá luật nữa, sau…

```text
Wide 16:9 landscape cinematic frame. a man standing between two glowing vows written on scrolls, one tied with a ribbon, one sealed with a family crest, medium shot, conflicted light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Hai lời thề kéo anh về hai phía. Anh chọn luật, và chờ một người đủ mạnh tới phá vỡ nó thay anh. Kaku nghĩ tr…

```text
Wide 16:9 landscape cinematic frame. a chain stretched between two anchors with a figure in the middle, one link cracking, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Sau khi mọi chuyện kết thúc, Byakuya kể cho Rukia sự thật về chị gái cô, và nói lời xin lỗi. Với một người nh…

```text
Wide 16:9 landscape cinematic frame. a man and a young woman standing on a quiet veranda at dusk, cherry petals drifting between them, back view, gentle warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Và vì vậy, nếu nhìn lại toàn trận, đối thủ thật của Ichigo không chỉ là thanh kiếm nghìn cánh hoa, mà là bức…

```text
Wide 16:9 landscape cinematic frame. a tall stone wall with carved rules cracking down the middle, a small figure with a sword standing before it, wide shot, dawn light breaking through. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Ba bài học chiến thuật

Lời: Nhưng trước ba bài học trong trận, có một bài học từ hiệp số không: thua một trận không phải là hết. Ichigo t…

```text
Wide 16:9 landscape cinematic frame. a crumpled losing scorecard pinned beside a winning one on a corkboard, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Giờ tới ba bài học. Bài một: khi đối thủ đánh bằng số lượng, đừng cố chặn tất cả. Hãy đủ nhanh để đi xuyên qu…

```text
Wide 16:9 landscape cinematic frame. a small fast arrow slipping through a gap in a wall of many small dots, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bài hai: nén sức mạnh vào một điểm thường hiệu quả hơn trải đều khắp nơi. Ichigo dùng nó ngay từ Bankai, còn…

```text
Wide 16:9 landscape cinematic frame. a diagram comparing a focused beam hitting a target and a diffuse spray missing, parchment style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Bài ba: đừng dùng lối tắt mà bạn không kiểm soát được. Chiếc mặt nạ Hollow có thể giúp Ichigo thắng nhanh, nh…

```text
Wide 16:9 landscape cinematic frame. a shortcut path on a map leading to a cliff edge, the long path winding safely around, parchment top-down shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và một bài học không nằm trên sơ đồ: người có lý do để chiến đấu rõ ràng hơn thường đứng được lâu hơn. Ichigo…

```text
Wide 16:9 landscape cinematic frame. a single clear arrow next to a tangled knot of two arrows pulling in opposite directions, parchment diagram, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Kaku có một mẹo nhỏ: lần sau xem lại trận này, hãy tắt tiếng và chỉ nhìn khoảng cách giữa hai người. Bạn sẽ t…

```text
Wide 16:9 landscape cinematic frame. a tiny remote control with a muted speaker icon resting on the tactical map, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Bạn có nghĩ Byakuya thua vì kém hơn, hay vì trong thâm tâm anh không muốn thắng? Kaku rất muốn nghe ý kiến củ…

```text
Wide 16:9 landscape cinematic frame. a single cherry blossom petal resting on a closed sword sheath, extreme close-up, soft pink light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Ichigo đối đầu Byakuya là một trận mà Kaku tin rằng ai xem Bleach cũng nhớ. Không chỉ vì những đòn đẹp mắt, m…

```text
Wide 16:9 landscape cinematic frame. two silhouettes standing on a hilltop at dawn after a battle, cherry petals drifting in the wind, wide shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tiếp theo, Kaku mở một cuốn hồ sơ đáng sợ hơn: bốn loại vũ khí sinh học mọc ra từ cơ thể của ngạ quỷ tr…

```text
Wide 16:9 landscape cinematic frame. an old filing cabinet in a dark office with one drawer slightly open and a red glow coming from inside, medium shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem trận đấu được mổ xẻ như một ván cờ, hãy đăng ký kênh để không bỏ lỡ trận tiếp theo. Kaku gấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot folding the tactical map and bowing like a referee after a match. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 80 giây · cảnh s01–s07 · 1040 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Bleach tới hết arc Soul Society, tức khoảng sáu mươi tập đầu của anime. Không có spoiler phần sau.

<short pause> Trên đồi Song Cực, hai người cầm kiếm đứng đối diện nhau. Một người là đội trưởng đội sáu, trưởng tộc của một gia tộc quý tộc bậc nhất, đã luyện kiếm hàng trăm năm.

<short pause> Người kia là một cậu học sinh mười lăm tuổi, vừa học Bankai được đúng ba ngày, trong khi người bình thường mất ít nhất mười năm.

<short pause> Bối cảnh: Rukia, người đã trao sức mạnh tử thần cho Ichigo, bị kết án tử vì phạm luật. Ichigo cùng bạn bè xông vào Soul Society để cứu cô, vượt qua từng đội trưởng một.

<short pause> Nếu phải đặt cược trước trận, Kaku nghĩ gần như ai ở Soul Society cũng sẽ đặt vào vị đội trưởng. Vậy mà người thắng lại là cậu học sinh.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình phân tích trận Kurosaki Ichigo đối đầu Kuchiki Byakuya theo từng hiệp: mỗi người muốn gì, chọn gì, và trả giá gì.

<short pause> Kaku sẽ kể bằng sơ đồ và tranh tự vẽ, không dựng lại cảnh trong anime. Cuối video là ba bài học chiến thuật mà bạn có thể áp dụng cho… bất cứ trận đấu nào trong đời.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Bleach tới hết arc Soul Society, tức khoảng sáu mươi tập đầu của anime. Không có spoiler phần sau.

[pause] Trên đồi Song Cực, hai người cầm kiếm đứng đối diện nhau. Một người là đội trưởng đội sáu, trưởng tộc của một gia tộc quý tộc bậc nhất, đã luyện kiếm hàng trăm năm.

[pause] Người kia là một cậu học sinh mười lăm tuổi, vừa học Bankai được đúng ba ngày, trong khi người bình thường mất ít nhất mười năm.

[pause] Bối cảnh: Rukia, người đã trao sức mạnh tử thần cho Ichigo, bị kết án tử vì phạm luật. Ichigo cùng bạn bè xông vào Soul Society để cứu cô, vượt qua từng đội trưởng một.

[pause] Nếu phải đặt cược trước trận, Kaku nghĩ gần như ai ở Soul Society cũng sẽ đặt vào vị đội trưởng. Vậy mà người thắng lại là cậu học sinh.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình phân tích trận Kurosaki Ichigo đối đầu Kuchiki Byakuya theo từng hiệp: mỗi người muốn gì, chọn gì, và trả giá gì.

[pause] Kaku sẽ kể bằng sơ đồ và tranh tự vẽ, không dựng lại cảnh trong anime. Cuối video là ba bài học chiến thuật mà bạn có thể áp dụng cho… bất cứ trận đấu nào trong đời.
```

### c02 · Trước trận: hồ sơ hai đấu thủ

Khoảng 95 giây · cảnh s08–s15 · 1237 ký tự

**Gemini**

```text
Đấu thủ thứ nhất, Byakuya. Kiếm của anh tên là Thiên Bản Anh. Khi giải phóng, lưỡi kiếm vỡ thành hàng nghìn mảnh nhỏ như cánh hoa anh đào, và mỗi cánh hoa là một lưỡi dao.

<short pause> Gia tộc Kuchiki là một trong những gia tộc quý tộc lớn nhất Soul Society. Byakuya là trưởng tộc, nghĩa là mọi hành động của anh đều là tấm gương cho cả dòng họ.

<short pause> Anh còn là bậc thầy Thuấn bộ, kiểu di chuyển nhanh tới mức như biến mất. Anh ít nói, không bao giờ vội vàng, và chưa từng để lộ cảm xúc.

<short pause> Ichigo là một tử thần thay thế: một con người được Rukia trao sức mạnh trong một đêm khẩn cấp. Cậu chưa từng học ở học viện tử thần, chưa từng được ai dạy bài bản.

<short pause> Đấu thủ thứ hai, Ichigo. Kiếm của cậu tên là Trảm Nguyệt, to và nặng. Cậu mạnh về sức và ý chí, nhưng thiếu kinh nghiệm và kỹ thuật.

<short pause> Cậu vừa học Bankai bằng một phương pháp đặc biệt trong ba ngày, dưới sự giám sát của Yoruichi. Nghĩa là cậu có sức mạnh, nhưng chưa có thời gian làm quen với nó.

<short pause> Động cơ của hai người cũng khác nhau. Ichigo tới để cứu Rukia khỏi án tử. Byakuya là anh nuôi của Rukia, nhưng anh đứng về phía luật lệ và sẽ không để ai ngăn bản án.

<short pause> Bảng tỉ số trước trận: kinh nghiệm, kỹ thuật và tốc độ nghiêng về Byakuya. Sức bền và ý chí nghiêng về Ichigo. Kaku chấm tỉ số ba – hai cho Byakuya.
```

**ElevenLabs**

```text
Đấu thủ thứ nhất, Byakuya. Kiếm của anh tên là Thiên Bản Anh. Khi giải phóng, lưỡi kiếm vỡ thành hàng nghìn mảnh nhỏ như cánh hoa anh đào, và mỗi cánh hoa là một lưỡi dao.

[pause] Gia tộc Kuchiki là một trong những gia tộc quý tộc lớn nhất Soul Society. Byakuya là trưởng tộc, nghĩa là mọi hành động của anh đều là tấm gương cho cả dòng họ.

[pause] Anh còn là bậc thầy Thuấn bộ, kiểu di chuyển nhanh tới mức như biến mất. Anh ít nói, không bao giờ vội vàng, và chưa từng để lộ cảm xúc.

[pause] Ichigo là một tử thần thay thế: một con người được Rukia trao sức mạnh trong một đêm khẩn cấp. Cậu chưa từng học ở học viện tử thần, chưa từng được ai dạy bài bản.

[pause] Đấu thủ thứ hai, Ichigo. Kiếm của cậu tên là Trảm Nguyệt, to và nặng. Cậu mạnh về sức và ý chí, nhưng thiếu kinh nghiệm và kỹ thuật.

[pause] Cậu vừa học Bankai bằng một phương pháp đặc biệt trong ba ngày, dưới sự giám sát của Yoruichi. Nghĩa là cậu có sức mạnh, nhưng chưa có thời gian làm quen với nó.

[pause] Động cơ của hai người cũng khác nhau. Ichigo tới để cứu Rukia khỏi án tử. Byakuya là anh nuôi của Rukia, nhưng anh đứng về phía luật lệ và sẽ không để ai ngăn bản án.

[pause] Bảng tỉ số trước trận: kinh nghiệm, kỹ thuật và tốc độ nghiêng về Byakuya. Sức bền và ý chí nghiêng về Ichigo. Kaku chấm tỉ số ba – hai cho Byakuya.
```

### c03 · Hiệp 0: món nợ cũ / Hiệp 1: tốc độ

Khoảng 134 giây · cảnh s16–s27 · 1747 ký tự

**Gemini**

```text
Thật ra đây là lần gặp thứ hai. Lần đầu là ở thế giới người, khi Soul Society tới bắt Rukia. Ichigo lao vào, và bị Byakuya hạ gục trong nháy mắt.

<short pause> Để lấy lại sức mạnh, Ichigo phải qua một bài huấn luyện nguy hiểm của Urahara: bị trói linh hồn dưới đáy một cái hố sâu, và phải tự thức tỉnh trước khi biến thành Hollow.

<short pause> Cậu thành công, và lần đầu tiên có được thanh Trảm Nguyệt của chính mình. Tức là thất bại trước Byakuya đã buộc cậu phải trở thành một tử thần thật sự.

<short pause> Byakuya không chỉ đánh bại cậu. Anh cắt đứt nguồn linh lực của cậu, khiến cậu mất hết sức mạnh tử thần. Cậu phải đi tìm lại chúng từ đầu.

<short pause> Mục tiêu của Ichigo ở hiệp này rất đơn giản: xông lên. Lựa chọn của cậu: dùng hết sức. Cái giá: suýt mất mạng, và mất Rukia vào tay Soul Society.

<short pause> <laugh> Kaku ghi chú: bài học của hiệp không là ý chí thôi chưa đủ. Chính vì thua trận này, Ichigo mới chịu học hỏi thật sự.

<short pause> Trận tái đấu trên đồi Song Cực bắt đầu. Byakuya ra đòn bằng Thuấn bộ, như lần trước. <short pause> Nhưng lần này, Ichigo theo kịp.

<short pause> Đây là thành quả của những ngày tập với Yoruichi, người được mệnh danh là nữ thần Thuấn bộ. Byakuya không nói gì, nhưng đây là lần đầu anh phải thật sự chú ý.

<short pause> Với Byakuya, tốc độ luôn là cách giữ khoảng cách: ra đòn rồi biến mất, không bao giờ để đối thủ chạm vào mình. Khi Ichigo theo kịp, khoảng cách ấy bắt đầu co lại.

<short pause> Sơ đồ hiệp một: Byakuya muốn kết thúc nhanh bằng tốc độ. Ichigo chứng minh cậu không còn là người của lần trước. Kết quả: hòa. <short pause> Nhưng về tâm lý, Ichigo thắng.

<short pause> Kaku mà tập Thuấn bộ ba ngày thì chắc chỉ nhanh hơn được… con rùa trong video Gojo. Mà con rùa đó còn không bị đuổi kịp.

<short pause> Kaku để ý điều này rất hay: trong một trận đấu giữa người mạnh và người yếu hơn, chỉ cần người yếu hơn chứng minh được một lần rằng mình không dễ bị hạ, trận đấu đã khác.
```

**ElevenLabs**

```text
Thật ra đây là lần gặp thứ hai. Lần đầu là ở thế giới người, khi Soul Society tới bắt Rukia. Ichigo lao vào, và bị Byakuya hạ gục trong nháy mắt.

[pause] Để lấy lại sức mạnh, Ichigo phải qua một bài huấn luyện nguy hiểm của Urahara: bị trói linh hồn dưới đáy một cái hố sâu, và phải tự thức tỉnh trước khi biến thành Hollow.

[pause] Cậu thành công, và lần đầu tiên có được thanh Trảm Nguyệt của chính mình. Tức là thất bại trước Byakuya đã buộc cậu phải trở thành một tử thần thật sự.

[pause] Byakuya không chỉ đánh bại cậu. Anh cắt đứt nguồn linh lực của cậu, khiến cậu mất hết sức mạnh tử thần. Cậu phải đi tìm lại chúng từ đầu.

[pause] Mục tiêu của Ichigo ở hiệp này rất đơn giản: xông lên. Lựa chọn của cậu: dùng hết sức. Cái giá: suýt mất mạng, và mất Rukia vào tay Soul Society.

[pause] [chuckles] Kaku ghi chú: bài học của hiệp không là ý chí thôi chưa đủ. Chính vì thua trận này, Ichigo mới chịu học hỏi thật sự.

[pause] Trận tái đấu trên đồi Song Cực bắt đầu. Byakuya ra đòn bằng Thuấn bộ, như lần trước. [pause] Nhưng lần này, Ichigo theo kịp.

[pause] Đây là thành quả của những ngày tập với Yoruichi, người được mệnh danh là nữ thần Thuấn bộ. Byakuya không nói gì, nhưng đây là lần đầu anh phải thật sự chú ý.

[pause] Với Byakuya, tốc độ luôn là cách giữ khoảng cách: ra đòn rồi biến mất, không bao giờ để đối thủ chạm vào mình. Khi Ichigo theo kịp, khoảng cách ấy bắt đầu co lại.

[pause] Sơ đồ hiệp một: Byakuya muốn kết thúc nhanh bằng tốc độ. Ichigo chứng minh cậu không còn là người của lần trước. Kết quả: hòa. [pause] Nhưng về tâm lý, Ichigo thắng.

[pause] Kaku mà tập Thuấn bộ ba ngày thì chắc chỉ nhanh hơn được… con rùa trong video Gojo. Mà con rùa đó còn không bị đuổi kịp.

[pause] Kaku để ý điều này rất hay: trong một trận đấu giữa người mạnh và người yếu hơn, chỉ cần người yếu hơn chứng minh được một lần rằng mình không dễ bị hạ, trận đấu đã khác.
```

### c04 · Hiệp 2: nghìn cánh hoa

Khoảng 78 giây · cảnh s28–s35 · 1013 ký tự

**Gemini**

```text
Byakuya giải phóng Thiên Bản Anh. Hàng nghìn lưỡi dao nhỏ xíu tràn ra như một cơn bão cánh hoa, và gần như không thể nhìn thấy từng lưỡi.

<short pause> Thiên Bản Anh còn có một điểm đáng sợ: Byakuya đứng yên vẫn tấn công được. Anh không cần tới gần, chỉ cần một cái vẫy tay là cơn bão đổi hướng.

<short pause> Trong khi đó Ichigo chỉ có một cách tấn công: chạy tới và chém. Khoảng cách chính là thứ Byakuya dùng để thắng hiệp này.

<short pause> Vấn đề của Ichigo là thanh kiếm to của cậu chỉ chặn được một hướng. Còn cánh hoa tấn công từ mọi hướng cùng lúc.

<short pause> Cậu cố chém, cố né, cố xông thẳng vào người điều khiển. <short pause> Nhưng mỗi lần xông tới, cơn bão lại cắt thêm vài vết trên người cậu.

<short pause> Sơ đồ hiệp hai: Byakuya chọn đánh bằng số lượng. Ichigo chọn đánh bằng sức mạnh đơn lẻ. Và số lượng thắng. Hiệp hai thuộc về Byakuya.

<short pause> Cái giá cho Ichigo: mất máu, và nhận ra rằng cách đánh cũ không dùng được nữa. Muốn thắng, cậu phải đổi cách chơi.

<short pause> <laugh> Kaku thử đếm số cánh hoa trong cảnh này để làm sơ đồ chính xác. Tới cánh thứ ba trăm thì Kaku quyết định làm tròn thành rất nhiều.
```

**ElevenLabs**

```text
Byakuya giải phóng Thiên Bản Anh. Hàng nghìn lưỡi dao nhỏ xíu tràn ra như một cơn bão cánh hoa, và gần như không thể nhìn thấy từng lưỡi.

[pause] Thiên Bản Anh còn có một điểm đáng sợ: Byakuya đứng yên vẫn tấn công được. Anh không cần tới gần, chỉ cần một cái vẫy tay là cơn bão đổi hướng.

[pause] Trong khi đó Ichigo chỉ có một cách tấn công: chạy tới và chém. Khoảng cách chính là thứ Byakuya dùng để thắng hiệp này.

[pause] Vấn đề của Ichigo là thanh kiếm to của cậu chỉ chặn được một hướng. Còn cánh hoa tấn công từ mọi hướng cùng lúc.

[pause] Cậu cố chém, cố né, cố xông thẳng vào người điều khiển. [pause] Nhưng mỗi lần xông tới, cơn bão lại cắt thêm vài vết trên người cậu.

[pause] Sơ đồ hiệp hai: Byakuya chọn đánh bằng số lượng. Ichigo chọn đánh bằng sức mạnh đơn lẻ. Và số lượng thắng. Hiệp hai thuộc về Byakuya.

[pause] Cái giá cho Ichigo: mất máu, và nhận ra rằng cách đánh cũ không dùng được nữa. Muốn thắng, cậu phải đổi cách chơi.

[pause] [chuckles] Kaku thử đếm số cánh hoa trong cảnh này để làm sơ đồ chính xác. Tới cánh thứ ba trăm thì Kaku quyết định làm tròn thành rất nhiều.
```

### c05 · Hiệp 3: Bankai đấu Bankai

Khoảng 110 giây · cảnh s36–s45 · 1434 ký tự

**Gemini**

```text
Ichigo giải phóng Bankai. <short pause> Nhưng khác với mọi người mong đợi, thanh kiếm không to hơn. Nó thu nhỏ lại thành một thanh kiếm đen mảnh, gọn như một thanh kiếm bình thường.

<short pause> Đây là Bankai tên Thiên Tỏa Trảm Nguyệt. Toàn bộ sức mạnh được nén vào một lưỡi kiếm nhỏ, để Ichigo di chuyển và ra đòn ở tốc độ cực cao.

<short pause> Byakuya thậm chí tỏ ra khó chịu. Một kẻ vừa học Bankai ba ngày dám đứng ngang hàng với anh, ở cùng cấp độ sức mạnh mà anh mất hàng trăm năm để đạt tới.

<short pause> Byakuya đáp trả bằng Bankai của mình. Những thanh kiếm khổng lồ mọc lên từ mặt đất, rồi vỡ ra thành hàng trăm triệu cánh hoa. Cơn bão lần này lớn gấp bội.

<short pause> Nhiều người nghĩ Bankai càng to càng mạnh. Trận này chứng minh điều ngược lại: không phải kích thước, mà là cách sức mạnh phù hợp với người dùng.

<short pause> Đây là cuộc đối đầu thú vị nhất về chiến thuật: một bên nén tất cả vào một điểm, một bên trải tất cả ra khắp không gian.

<short pause> Ichigo còn giải thích cho Byakuya rằng Bankai của cậu không to, vì nó dồn hết sức mạnh vào tốc độ. Một lời giải thích mà ngay cả khán giả lúc đó cũng cần.

<short pause> Với tốc độ mới, Ichigo không cần chặn cánh hoa nữa. Cậu né, chém xuyên qua khe hở, và lần đầu tiên chạm được kiếm vào Byakuya.

<short pause> Sơ đồ hiệp ba: Byakuya chọn phủ kín không gian. Ichigo chọn tốc độ để đi xuyên qua khe hở. Hiệp này nghiêng về Ichigo, và tỉ số giờ là hai – một.

<short pause> Cái giá cho Ichigo: tốc độ cực cao đòi hỏi cơ thể rất nhiều. Cậu học Bankai trong ba ngày, nên chưa biết giới hạn của chính mình ở đâu.
```

**ElevenLabs**

```text
Ichigo giải phóng Bankai. [pause] Nhưng khác với mọi người mong đợi, thanh kiếm không to hơn. Nó thu nhỏ lại thành một thanh kiếm đen mảnh, gọn như một thanh kiếm bình thường.

[pause] Đây là Bankai tên Thiên Tỏa Trảm Nguyệt. Toàn bộ sức mạnh được nén vào một lưỡi kiếm nhỏ, để Ichigo di chuyển và ra đòn ở tốc độ cực cao.

[pause] Byakuya thậm chí tỏ ra khó chịu. Một kẻ vừa học Bankai ba ngày dám đứng ngang hàng với anh, ở cùng cấp độ sức mạnh mà anh mất hàng trăm năm để đạt tới.

[pause] Byakuya đáp trả bằng Bankai của mình. Những thanh kiếm khổng lồ mọc lên từ mặt đất, rồi vỡ ra thành hàng trăm triệu cánh hoa. Cơn bão lần này lớn gấp bội.

[pause] Nhiều người nghĩ Bankai càng to càng mạnh. Trận này chứng minh điều ngược lại: không phải kích thước, mà là cách sức mạnh phù hợp với người dùng.

[pause] Đây là cuộc đối đầu thú vị nhất về chiến thuật: một bên nén tất cả vào một điểm, một bên trải tất cả ra khắp không gian.

[pause] Ichigo còn giải thích cho Byakuya rằng Bankai của cậu không to, vì nó dồn hết sức mạnh vào tốc độ. Một lời giải thích mà ngay cả khán giả lúc đó cũng cần.

[pause] Với tốc độ mới, Ichigo không cần chặn cánh hoa nữa. Cậu né, chém xuyên qua khe hở, và lần đầu tiên chạm được kiếm vào Byakuya.

[pause] Sơ đồ hiệp ba: Byakuya chọn phủ kín không gian. Ichigo chọn tốc độ để đi xuyên qua khe hở. Hiệp này nghiêng về Ichigo, và tỉ số giờ là hai – một.

[pause] Cái giá cho Ichigo: tốc độ cực cao đòi hỏi cơ thể rất nhiều. Cậu học Bankai trong ba ngày, nên chưa biết giới hạn của chính mình ở đâu.
```

### c06 · Hiệp 4: kẻ thù bên trong

Khoảng 79 giây · cảnh s46–s53 · 1025 ký tự

**Gemini**

```text
Rồi tới khoảnh khắc mà người xem lần đầu không hiểu chuyện gì xảy ra. Giữa trận, một nửa khuôn mặt Ichigo bị phủ bởi một chiếc mặt nạ trắng, và giọng cậu đổi khác.

<short pause> Thứ sức mạnh ấy không giống của tử thần. Nó thô bạo, không có kỹ thuật, chỉ muốn phá hủy. Và nó không nghe lời Ichigo.

<short pause> Đó là Hollow ẩn trong cậu, một thực thể muốn chiếm lấy cơ thể. Trong vài giây, sức mạnh của Ichigo tăng vọt, đủ khiến Byakuya bất ngờ.

<short pause> Nhưng Ichigo tự đập vỡ chiếc mặt nạ. Cậu không muốn thắng bằng thứ sức mạnh không phải của mình.

<short pause> Sơ đồ hiệp bốn: Ichigo có một lựa chọn dễ để thắng nhanh, và cậu từ chối nó. Về điểm số, hiệp này hòa. Về con người, đây là hiệp quan trọng nhất.

<short pause> Kaku thấy đây là một chi tiết kể chuyện rất khéo: cùng một trận đấu, Ichigo phải đánh hai kẻ thù cùng lúc, một bên ngoài, một bên trong.

<short pause> Cái giá: cậu đã dùng rất nhiều sức lực để kìm Hollow lại, trong khi trận đấu còn chưa kết thúc.

<short pause> <laugh> Kaku phải nói thêm: Hollow của Ichigo là một bí ẩn lớn mà Bleach giải thích dần ở những arc sau. Hôm nay Kaku dừng ở đây để không spoiler.
```

**ElevenLabs**

```text
Rồi tới khoảnh khắc mà người xem lần đầu không hiểu chuyện gì xảy ra. Giữa trận, một nửa khuôn mặt Ichigo bị phủ bởi một chiếc mặt nạ trắng, và giọng cậu đổi khác.

[pause] Thứ sức mạnh ấy không giống của tử thần. Nó thô bạo, không có kỹ thuật, chỉ muốn phá hủy. Và nó không nghe lời Ichigo.

[pause] Đó là Hollow ẩn trong cậu, một thực thể muốn chiếm lấy cơ thể. Trong vài giây, sức mạnh của Ichigo tăng vọt, đủ khiến Byakuya bất ngờ.

[pause] Nhưng Ichigo tự đập vỡ chiếc mặt nạ. Cậu không muốn thắng bằng thứ sức mạnh không phải của mình.

[pause] Sơ đồ hiệp bốn: Ichigo có một lựa chọn dễ để thắng nhanh, và cậu từ chối nó. Về điểm số, hiệp này hòa. Về con người, đây là hiệp quan trọng nhất.

[pause] Kaku thấy đây là một chi tiết kể chuyện rất khéo: cùng một trận đấu, Ichigo phải đánh hai kẻ thù cùng lúc, một bên ngoài, một bên trong.

[pause] Cái giá: cậu đã dùng rất nhiều sức lực để kìm Hollow lại, trong khi trận đấu còn chưa kết thúc.

[pause] [chuckles] Kaku phải nói thêm: Hollow của Ichigo là một bí ẩn lớn mà Bleach giải thích dần ở những arc sau. Hôm nay Kaku dừng ở đây để không spoiler.
```

### c07 · Hiệp 5: hình thái thật của Thiên Bản Anh

Khoảng 84 giây · cảnh s54–s61 · 1098 ký tự

**Gemini**

```text
Lần đầu tiên, Byakuya dùng tới hình thái mà anh dành riêng cho kẻ thù anh thề tự tay giết. Những cánh hoa tụ lại thành hàng nghìn thanh kiếm lơ lửng xếp thành bốn vòng quanh hai người.

<short pause> Hình thái này yêu cầu Byakuya tự cầm kiếm lao vào. Người đã quen chiến đấu từ xa giờ phải bước vào tầm đánh của đối thủ.

<short pause> Đây là một lựa chọn chiến thuật rất đáng chú ý. Byakuya từ bỏ lợi thế tấn công từ xa bằng cơn bão cánh hoa, để đổi lấy sức sát thương tập trung trong tay mình.

<short pause> Anh còn gom cánh hoa thành một đôi cánh trắng sau lưng, dồn tất cả vào một đòn cuối.

<short pause> Với một người luôn giữ khoảng cách với mọi người như Byakuya, việc tự bước lại gần một đối thủ có lẽ là thay đổi lớn hơn bất kỳ chiêu thức nào.

<short pause> Kaku đọc lựa chọn này như một sự thừa nhận: Byakuya cuối cùng coi Ichigo là đối thủ ngang hàng, đáng để anh đích thân ra tay.

<short pause> Kaku để ý: nếu nhìn trận đấu từ trên cao, sơ đồ hiệp năm giống hệt sơ đồ hiệp ba, chỉ là hai quân cờ đã đổi chỗ cho nhau.

<short pause> Sơ đồ hiệp năm: Byakuya chọn dồn toàn lực vào một điểm, giống cách Ichigo làm với Bankai. Hai người giờ chơi cùng một kiểu. Và khi cùng kiểu, ý chí sẽ quyết định.
```

**ElevenLabs**

```text
Lần đầu tiên, Byakuya dùng tới hình thái mà anh dành riêng cho kẻ thù anh thề tự tay giết. Những cánh hoa tụ lại thành hàng nghìn thanh kiếm lơ lửng xếp thành bốn vòng quanh hai người.

[pause] Hình thái này yêu cầu Byakuya tự cầm kiếm lao vào. Người đã quen chiến đấu từ xa giờ phải bước vào tầm đánh của đối thủ.

[pause] Đây là một lựa chọn chiến thuật rất đáng chú ý. Byakuya từ bỏ lợi thế tấn công từ xa bằng cơn bão cánh hoa, để đổi lấy sức sát thương tập trung trong tay mình.

[pause] Anh còn gom cánh hoa thành một đôi cánh trắng sau lưng, dồn tất cả vào một đòn cuối.

[pause] Với một người luôn giữ khoảng cách với mọi người như Byakuya, việc tự bước lại gần một đối thủ có lẽ là thay đổi lớn hơn bất kỳ chiêu thức nào.

[pause] Kaku đọc lựa chọn này như một sự thừa nhận: Byakuya cuối cùng coi Ichigo là đối thủ ngang hàng, đáng để anh đích thân ra tay.

[pause] Kaku để ý: nếu nhìn trận đấu từ trên cao, sơ đồ hiệp năm giống hệt sơ đồ hiệp ba, chỉ là hai quân cờ đã đổi chỗ cho nhau.

[pause] Sơ đồ hiệp năm: Byakuya chọn dồn toàn lực vào một điểm, giống cách Ichigo làm với Bankai. Hai người giờ chơi cùng một kiểu. Và khi cùng kiểu, ý chí sẽ quyết định.
```

### c08 · Hiệp 6: đòn cuối / Sau trận: lý do của Byakuya

Khoảng 137 giây · cảnh s62–s74 · 1780 ký tự

**Gemini**

```text
Hai người lao vào nhau. Nguyệt Nha Thiên Xung màu đen của Ichigo va vào đòn cánh trắng của Byakuya.

<short pause> Khi khói tan, cả hai vẫn đứng. <short pause> Nhưng thanh kiếm của Byakuya đã gãy, và người lùi bước là anh.

<short pause> Và chỉ ít lâu sau, khi một đội trưởng phản bội tấn công Rukia, chính Byakuya lấy thân mình đỡ đòn cho cô. Người đứng về phía luật lệ cuối cùng đã chọn giữ lời hứa với vợ.

<short pause> Byakuya nói rằng anh đã thua, và thanh kiếm của anh không còn muốn chém Ichigo nữa. Kaku thấy đây là cách thua đẹp nhất trong Bleach.

<short pause> Nhưng hãy nhớ: Ichigo cũng đã ở sát giới hạn. Sau trận, cậu gần như không thể cử động. Trận này không có người thắng tuyệt đối, chỉ có người đứng được lâu hơn một chút.

<short pause> Kaku chấm như vậy vì điểm số chỉ đo từng hiệp. Nếu chấm cả trận, có lẽ phải thêm một cột cho thứ không đo được: người nào dám đổi cách chơi khi đang thua.

<short pause> Tỉ số chung cuộc theo sơ đồ của Kaku: ba – hai cho Ichigo, sau khi bị dẫn trước. Một cuộc lội ngược dòng thật sự.

<short pause> Sau trận, Bleach mới cho ta biết vì sao Byakuya lạnh lùng tới vậy. Rukia là em gái của người vợ quá cố của anh, Hisana.

<short pause> Hisana từng bỏ rơi em gái khi còn nhỏ vì hoàn cảnh, và day dứt suốt phần đời còn lại. Trước khi mất, cô nhờ Byakuya tìm và bảo vệ Rukia.

<short pause> Anh đã hứa với vợ sẽ bảo vệ Rukia. <short pause> Nhưng anh cũng đã thề trước cha mẹ mình sẽ không bao giờ phá luật nữa, sau khi đã phá luật một lần để cưới Hisana.

<short pause> Hai lời thề kéo anh về hai phía. Anh chọn luật, và chờ một người đủ mạnh tới phá vỡ nó thay anh. Kaku nghĩ trong thâm tâm, Byakuya đã chờ Ichigo thắng.

<short pause> Sau khi mọi chuyện kết thúc, Byakuya kể cho Rukia sự thật về chị gái cô, và nói lời xin lỗi. Với một người như anh, đó có lẽ là việc khó hơn cả trận đấu.

<short pause> Và vì vậy, nếu nhìn lại toàn trận, đối thủ thật của Ichigo không chỉ là thanh kiếm nghìn cánh hoa, mà là bức tường luật lệ trong lòng Byakuya.
```

**ElevenLabs**

```text
Hai người lao vào nhau. Nguyệt Nha Thiên Xung màu đen của Ichigo va vào đòn cánh trắng của Byakuya.

[pause] Khi khói tan, cả hai vẫn đứng. [pause] Nhưng thanh kiếm của Byakuya đã gãy, và người lùi bước là anh.

[pause] Và chỉ ít lâu sau, khi một đội trưởng phản bội tấn công Rukia, chính Byakuya lấy thân mình đỡ đòn cho cô. Người đứng về phía luật lệ cuối cùng đã chọn giữ lời hứa với vợ.

[pause] Byakuya nói rằng anh đã thua, và thanh kiếm của anh không còn muốn chém Ichigo nữa. Kaku thấy đây là cách thua đẹp nhất trong Bleach.

[pause] Nhưng hãy nhớ: Ichigo cũng đã ở sát giới hạn. Sau trận, cậu gần như không thể cử động. Trận này không có người thắng tuyệt đối, chỉ có người đứng được lâu hơn một chút.

[pause] Kaku chấm như vậy vì điểm số chỉ đo từng hiệp. Nếu chấm cả trận, có lẽ phải thêm một cột cho thứ không đo được: người nào dám đổi cách chơi khi đang thua.

[pause] Tỉ số chung cuộc theo sơ đồ của Kaku: ba – hai cho Ichigo, sau khi bị dẫn trước. Một cuộc lội ngược dòng thật sự.

[pause] Sau trận, Bleach mới cho ta biết vì sao Byakuya lạnh lùng tới vậy. Rukia là em gái của người vợ quá cố của anh, Hisana.

[pause] Hisana từng bỏ rơi em gái khi còn nhỏ vì hoàn cảnh, và day dứt suốt phần đời còn lại. Trước khi mất, cô nhờ Byakuya tìm và bảo vệ Rukia.

[pause] Anh đã hứa với vợ sẽ bảo vệ Rukia. [pause] Nhưng anh cũng đã thề trước cha mẹ mình sẽ không bao giờ phá luật nữa, sau khi đã phá luật một lần để cưới Hisana.

[pause] Hai lời thề kéo anh về hai phía. Anh chọn luật, và chờ một người đủ mạnh tới phá vỡ nó thay anh. Kaku nghĩ trong thâm tâm, Byakuya đã chờ Ichigo thắng.

[pause] Sau khi mọi chuyện kết thúc, Byakuya kể cho Rukia sự thật về chị gái cô, và nói lời xin lỗi. Với một người như anh, đó có lẽ là việc khó hơn cả trận đấu.

[pause] Và vì vậy, nếu nhìn lại toàn trận, đối thủ thật của Ichigo không chỉ là thanh kiếm nghìn cánh hoa, mà là bức tường luật lệ trong lòng Byakuya.
```

### c09 · Ba bài học chiến thuật / Kết

Khoảng 113 giây · cảnh s75–s84 · 1475 ký tự

**Gemini**

```text
Nhưng trước ba bài học trong trận, có một bài học từ hiệp số không: thua một trận không phải là hết. Ichigo thắng lần này chính vì lần trước đã thua quá đau.

<short pause> Giờ tới ba bài học. Bài một: khi đối thủ đánh bằng số lượng, đừng cố chặn tất cả. Hãy đủ nhanh để đi xuyên qua khe hở.

<short pause> Bài hai: nén sức mạnh vào một điểm thường hiệu quả hơn trải đều khắp nơi. Ichigo dùng nó ngay từ Bankai, còn Byakuya chỉ dùng ở hiệp cuối.

<short pause> Bài ba: đừng dùng lối tắt mà bạn không kiểm soát được. Chiếc mặt nạ Hollow có thể giúp Ichigo thắng nhanh, nhưng cái giá có thể là mất chính mình.

<short pause> Và một bài học không nằm trên sơ đồ: người có lý do để chiến đấu rõ ràng hơn thường đứng được lâu hơn. Ichigo biết mình muốn gì. Byakuya thì bị kẹt giữa hai điều mình muốn.

<short pause> Kaku có một mẹo nhỏ: lần sau xem lại trận này, hãy tắt tiếng và chỉ nhìn khoảng cách giữa hai người. Bạn sẽ thấy cả câu chuyện nằm ở đó.

<short pause> Bạn có nghĩ Byakuya thua vì kém hơn, hay vì trong thâm tâm anh không muốn thắng? Kaku rất muốn nghe ý kiến của bạn trong phần bình luận.

<short pause> Ichigo đối đầu Byakuya là một trận mà Kaku tin rằng ai xem Bleach cũng nhớ. Không chỉ vì những đòn đẹp mắt, mà vì mỗi lựa chọn trong trận đều nói lên con người của người chọn nó.

<short pause> Video tiếp theo, Kaku mở một cuốn hồ sơ đáng sợ hơn: bốn loại vũ khí sinh học mọc ra từ cơ thể của ngạ quỷ trong Tokyo Ghoul. Mỗi loại một điểm mạnh, một điểm yếu.

<short pause> Nếu bạn thích xem trận đấu được mổ xẻ như một ván cờ, hãy đăng ký kênh để không bỏ lỡ trận tiếp theo. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Nhưng trước ba bài học trong trận, có một bài học từ hiệp số không: thua một trận không phải là hết. Ichigo thắng lần này chính vì lần trước đã thua quá đau.

[pause] Giờ tới ba bài học. Bài một: khi đối thủ đánh bằng số lượng, đừng cố chặn tất cả. Hãy đủ nhanh để đi xuyên qua khe hở.

[pause] Bài hai: nén sức mạnh vào một điểm thường hiệu quả hơn trải đều khắp nơi. Ichigo dùng nó ngay từ Bankai, còn Byakuya chỉ dùng ở hiệp cuối.

[pause] Bài ba: đừng dùng lối tắt mà bạn không kiểm soát được. Chiếc mặt nạ Hollow có thể giúp Ichigo thắng nhanh, nhưng cái giá có thể là mất chính mình.

[pause] Và một bài học không nằm trên sơ đồ: người có lý do để chiến đấu rõ ràng hơn thường đứng được lâu hơn. Ichigo biết mình muốn gì. Byakuya thì bị kẹt giữa hai điều mình muốn.

[pause] Kaku có một mẹo nhỏ: lần sau xem lại trận này, hãy tắt tiếng và chỉ nhìn khoảng cách giữa hai người. Bạn sẽ thấy cả câu chuyện nằm ở đó.

[pause] [curious] Bạn có nghĩ Byakuya thua vì kém hơn, hay vì trong thâm tâm anh không muốn thắng? Kaku rất muốn nghe ý kiến của bạn trong phần bình luận.

[pause] Ichigo đối đầu Byakuya là một trận mà Kaku tin rằng ai xem Bleach cũng nhớ. Không chỉ vì những đòn đẹp mắt, mà vì mỗi lựa chọn trong trận đều nói lên con người của người chọn nó.

[pause] Video tiếp theo, Kaku mở một cuốn hồ sơ đáng sợ hơn: bốn loại vũ khí sinh học mọc ra từ cơ thể của ngạ quỷ trong Tokyo Ghoul. Mỗi loại một điểm mạnh, một điểm yếu.

[pause] Nếu bạn thích xem trận đấu được mổ xẻ như một ván cờ, hãy đăng ký kênh để không bỏ lỡ trận tiếp theo. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
