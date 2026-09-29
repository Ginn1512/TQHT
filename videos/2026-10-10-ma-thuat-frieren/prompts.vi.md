# Bộ prompt · Frieren: Ma thuật hoạt động thế nào? Vì sao Zoltraak thành phép phổ thông

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 96 ảnh, 9 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (96 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Frieren đến hết arc thi pháp sư hạng nhất. Nếu bạn chưa xem tới đó, hãy lưu video…

```text
Wide 16:9 landscape cinematic frame. an old wooden desk with a closed spellbook and a sprig of blue flowers under candlelight. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Có một phép thuật từng giết vô số pháp sư và chiến binh loài người. Nó được gọi là ma pháp giết người, và từn…

```text
Wide 16:9 landscape cinematic frame. a beam of dark violet light piercing through a shattered shield in a burning battlefield, silhouettes falling. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Tám mươi năm sau, chính phép thuật đó được dạy cho người mới học như một đòn tấn công cơ bản nhất. Chuyện gì…

```text
Wide 16:9 landscape cinematic frame. a peaceful classroom in a stone tower, young apprentice silhouettes practicing small violet beams at targets. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Câu trả lời cho thấy điều đặc biệt nhất của Frieren: ma thuật ở đây không đứng yên. Nó có lịch sử, được nghiê…

```text
Wide 16:9 landscape cinematic frame. an ancient library timeline mural showing spells evolving across centuries, soft light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã ma thuật trong Frieren: nó vận hành thế nào, vì sao ma lự…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a glowing notebook, tiny blue flowers blooming from the pages. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao một pháp sư tưởng như yếu có thể là người đáng sợ nhất trên chiến trường.

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking over a large book with a mysterious smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Ma thuật là gì trong Frieren?

Lời: Trong Frieren, ma thuật dùng ma lực, một dạng năng lượng mà mỗi pháp sư mang trong người. Lượng ma lực nhiều…

```text
Wide 16:9 landscape cinematic frame. a mage silhouette with a soft glowing aura, energy gauge floating beside them. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhưng ma lực chỉ là nhiên liệu. Điều quyết định một phép thuật có thành hay không là khả năng hình dung của n…

```text
Wide 16:9 landscape cinematic frame. a mage closing their eyes, a clear glowing image of a flower forming in their mind above their head. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Truyện nhiều lần nhấn mạnh: ma thuật là thế giới của trí tưởng tượng. Thứ bạn không thể hình dung rõ ràng thì…

```text
Wide 16:9 landscape cinematic frame. a blurry half-formed spell dissolving in the air next to a sharp fully formed one. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Đây là lý do có những phép rất khó với con người. Không phải vì thiếu ma lực, mà vì con người không thể tưởng…

```text
Wide 16:9 landscape cinematic frame. a mage staring at a complex floating diagram with a puzzled expression, question marks around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Phép bay là ví dụ nổi tiếng. Con người dùng được nó, nhưng không ai giải thích được hoàn toàn cơ chế, vì nó v…

```text
Wide 16:9 landscape cinematic frame. several mage silhouettes floating calmly above clouds, one scholar below taking notes. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong Frieren, trí tưởng tượng là giới hạn thật sự. Ma lực nhiều mà tưởng tượng nghèo thì cũng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting in a tiny toy car with an empty fuel can beside it, shrugging. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Ma pháp giết người: câu chuyện của Zoltraak

Lời: Giờ quay lại phép thuật ở phần mở đầu. Nó có tên Zoltraak, được tạo ra bởi một ma tộc tên Qual.

```text
Wide 16:9 landscape cinematic frame. a tall horned demon silhouette in a ruined castle hall raising a hand crackling with violet light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Zoltraak là phép đầu tiên xuyên thủng được lớp phòng thủ bằng ma lực của con người. Trước nó, pháp sư loài ng…

```text
Wide 16:9 landscape cinematic frame. a violet beam piercing cleanly through a glowing protective barrier held by a human mage. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Kết quả rất khủng khiếp. Trong thời gian đó, phần lớn pháp sư và mạo hiểm giả bị giết đều chết bởi Zoltraak.

```text
Wide 16:9 landscape cinematic frame. a field of broken staffs and fallen banners under a grey sky, somber mood. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Rồi Frieren cùng tổ đội của Himmel đã phong ấn Qual. Ông ta bị khóa lại, còn phép thuật của ông ta ở lại với…

```text
Wide 16:9 landscape cinematic frame. a sealing circle of light closing around the demon silhouette, four hero silhouettes standing in the distance. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và đây là điều thú vị nhất: trong gần tám mươi năm Qual bị phong ấn, loài người đã mổ xẻ Zoltraak.

```text
Wide 16:9 landscape cinematic frame. scholars in a candlelit room dissecting a floating glowing spell diagram with quills and notes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Họ phân tích nó, hiểu nó, đưa nó vào giáo trình. Zoltraak trở thành thứ gọi là ma pháp tấn công thông thường,…

```text
Wide 16:9 landscape cinematic frame. a stack of textbooks with a violet beam icon on the cover, apprentices reading them. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Cùng lúc đó, phép phòng thủ cũng được phát triển để chặn đúng loại tấn công này. Mối đe dọa lớn nhất đã trở t…

```text
Wide 16:9 landscape cinematic frame. a transparent hexagonal shield easily deflecting a violet beam, apprentice smiling. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Khi Qual được giải phong ấn, ông ta dùng Zoltraak như xưa và phát hiện nó không còn là vũ khí tất thắng. Thế…

```text
Wide 16:9 landscape cinematic frame. the demon silhouette looking stunned as his violet beam splashes harmlessly against a simple shield. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Đây là một trong những ý tưởng hay nhất của Frieren: sức mạnh không đứng yên. Thứ mạnh nhất hôm nay có thể là…

```text
Wide 16:9 landscape cinematic frame. an hourglass with glowing sand, one side showing a terrifying beam, the other side a textbook. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ví von: giống như một loại virus nguy hiểm, và nhân loại đã nghiên cứu ra vắc-xin. Virus vẫn còn đó, như…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny lab coat holding a glowing shield-shaped vial. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Ma tộc: kẻ thù biết nói

Lời: Muốn hiểu vì sao ma thuật của con người phải tiến hóa nhanh, cần hiểu kẻ thù của họ: ma tộc.

```text
Wide 16:9 landscape cinematic frame. a horned humanoid silhouette standing at the edge of a village at dusk, smiling politely. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Ma tộc trông giống người, nói tiếng người, thậm chí gọi tên cha mẹ. Nhưng theo Frieren, chúng học ngôn ngữ ch…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette speaking gently to a frightened villager, a shadow of claws behind its back. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Truyện miêu tả ma tộc không có khái niệm gia đình hay lòng thương theo cách con người hiểu. Những lời xin tha…

```text
Wide 16:9 landscape cinematic frame. a demon kneeling and pleading while its shadow on the wall is smiling with sharp teeth. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Đây là lý do Frieren thẳng tay với ma tộc, điều khiến nhiều người lúc đầu thấy cô lạnh lùng. Cô đã thấy quá n…

```text
Wide 16:9 landscape cinematic frame. an elf mage standing firm in the rain before a pleading demon, staff raised. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Với ma tộc, ma thuật là bản năng và niềm tự hào. Mỗi ma tộc thường dành cả đời để hoàn thiện một phép duy nhấ…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette alone in a tower practicing the same glowing spell over centuries, candles melting. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Điều đó làm phép của chúng rất mạnh, nhưng cũng rất dễ bị con người nghiên cứu. Một phép duy nhất, dùng mãi,…

```text
Wide 16:9 landscape cinematic frame. scholars circling a single floating spell diagram, taking notes from all angles. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và đó chính là số phận của Zoltraak. Ma tộc sống lâu, nhưng con người học nhanh hơn.

```text
Wide 16:9 landscape cinematic frame. a long-lived demon silhouette frozen in place while a crowd of human mages walks past it into the future. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Ma lực là thước đo, và cũng là cái bẫy

Lời: Trong thế giới Frieren, cả pháp sư lẫn ma tộc đều cảm nhận được ma lực của người khác. Và với ma tộc, ma lực…

```text
Wide 16:9 landscape cinematic frame. two figures sensing each other's glowing aura from across a misty field. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Ma tộc coi ma lực như thước đo địa vị và sức mạnh. Chúng tự hào khoe ma lực của mình, và đánh giá đối thủ qua…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette with a huge flaring aura looking down on a small human with a faint aura. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Frieren biết điều đó, nên suốt hơn một nghìn năm, cô luôn đè nén ma lực của mình xuống, để trông yếu hơn thực…

```text
Wide 16:9 landscape cinematic frame. an elf mage silhouette walking calmly with a tiny aura, while a huge hidden glow is visible only as a faint shadow. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Kỹ năng này được dạy bởi thầy của cô, Flamme. Bà dạy Frieren giấu ma lực cả khi ăn, khi ngủ, trong mọi khoảnh…

```text
Wide 16:9 landscape cinematic frame. an older woman mage silhouette teaching a young elf in a flower field at sunset. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Mục đích rất rõ ràng: để lừa ma tộc. Một ma tộc nhìn thấy ma lực yếu ớt sẽ khinh thường, và sự khinh thường đ…

```text
Wide 16:9 landscape cinematic frame. a demon smirking at a small aura, unaware of a giant shadow of power behind it. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Trận đấu nổi tiếng nhất cho thấy điều này là trận với Aura, ma tộc sở hữu cán cân phục tùng.

```text
Wide 16:9 landscape cinematic frame. an ornate golden balance scale floating between two figures on a battlefield. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Cán cân này so ma lực của hai bên. Bên nào ít hơn sẽ bị bên kia điều khiển hoàn toàn. Aura tự tin vì ma lực c…

```text
Wide 16:9 landscape cinematic frame. the scale tipping toward the demon side as a large violet aura pours in. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Nhưng khi Frieren thả lỏng ma lực thật của mình, cán cân nghiêng hẳn về phía cô. Aura bị chính phép thuật của…

```text
Wide 16:9 landscape cinematic frame. the scale slamming down on the elf's side as an enormous calm glow rises, the demon's face in shock. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Bài học ở đây: trong Frieren, thông tin là vũ khí. Người để lộ ma lực thật là người đã cho đối thủ biết mình…

```text
Wide 16:9 landscape cinematic frame. a playing card being flipped face up to reveal a glowing crown symbol. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mỉm cười: người mạnh nhất phòng thường không phải người ồn ào nhất. Đôi khi là người ngồi yên uống trà ở…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sipping tea calmly in a corner while a loud aura flares in the background. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Kỹ năng đè nén ma lực có giá gì?

Lời: Đè nén ma lực nghe như chỉ có lợi, nhưng nó có cái giá. Khi luôn giấu sức mạnh, bạn phải chịu bị coi thường,…

```text
Wide 16:9 landscape cinematic frame. an elf mage being ignored by a proud crowd of mages in a grand hall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nhiều pháp sư trong truyện không tin một người trông yếu như Frieren lại là pháp sư huyền thoại. Với cô, điều…

```text
Wide 16:9 landscape cinematic frame. whispering silhouettes pointing at a calm elf reading a book, she ignores them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Kỹ năng này cũng rất khó. Chỉ cần dao động một chút khi chiến đấu, ma lực thật có thể lộ ra. Nó đòi hỏi kỷ lu…

```text
Wide 16:9 landscape cinematic frame. a steady flame in a glass lantern inside a strong wind, barely flickering. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Học trò của Frieren, Fern, cũng học được kỹ năng này và làm tốt tới mức ngay cả Frieren cũng khó nhận ra dao…

```text
Wide 16:9 landscape cinematic frame. a young mage silhouette with perfectly still faint aura, an elf squinting at her with curiosity. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Nhưng có người nhìn xuyên được lớp ngụy trang đó: Serie, một pháp sư tiên tộc cổ xưa, được coi là gần với thầ…

```text
Wide 16:9 landscape cinematic frame. an ancient elf mage silhouette seated on a high throne, eyes glowing as they see through illusions. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Điều này cho thấy không có kỹ năng nào là tuyệt đối. Luôn có ai đó già hơn, tinh hơn, và nhìn thấy thứ bạn gi…

```text
Wide 16:9 landscape cinematic frame. a chain of silhouettes each looking over the shoulder of the one before, into the distance. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Phép của pháp sư và phép của nữ thần

Lời: Trong Frieren còn có một nhánh phép thuật khác hẳn: phép của nữ thần, được dùng bởi các tu sĩ.

```text
Wide 16:9 landscape cinematic frame. a priest silhouette holding an open holy scripture glowing with soft golden light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Phép nữ thần đến từ kinh thánh. Tu sĩ dùng nó để chữa thương, giải độc, xua tà. Đây là thứ pháp sư thường khô…

```text
Wide 16:9 landscape cinematic frame. golden light mending a wound on a traveler's arm while a priest reads from a book. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Điều thú vị là ngay cả tu sĩ cũng không hiểu hết vì sao phép nữ thần hoạt động. Họ tin, và niềm tin đó là một…

```text
Wide 16:9 landscape cinematic frame. a priest kneeling in an empty chapel, light falling through a stained glass window without images. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Tổ đội anh hùng năm xưa có một tu sĩ, và tổ đội mới của Frieren cũng cần một người như vậy. Trong thế giới nà…

```text
Wide 16:9 landscape cinematic frame. a group of four traveler silhouettes around a campfire, one wearing priest robes tending to another. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Hai nhánh phép này bổ sung cho nhau: pháp sư dựa vào hình dung và nghiên cứu, tu sĩ dựa vào kinh thánh và niề…

```text
Wide 16:9 landscape cinematic frame. a split image: a mage with a glowing diagram on the left, a priest with a glowing scripture on the right. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một tổ đội cân bằng luôn cần cả người phá và người chữa. Đó cũng là bài học cho mọi đội nhóm ng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny bandage and a tiny staff, one in each wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Kỳ thi pháp sư hạng nhất

Lời: Một arc lớn của Frieren là kỳ thi pháp sư hạng nhất. Đây là nơi hệ thống ma thuật được thể hiện đa dạng nhất.

```text
Wide 16:9 landscape cinematic frame. a grand exam hall with floating banners and many mage silhouettes gathered. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Kỳ thi do Serie đứng sau. Người đỗ không chỉ có danh hiệu, mà còn được Serie ban cho một phép thuật mà họ mon…

```text
Wide 16:9 landscape cinematic frame. an ancient mage extending a glowing orb of light to a kneeling candidate. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Điều thú vị là mỗi người chọn một kiểu phép khác nhau, và lựa chọn đó nói lên con người họ. Có người chọn phé…

```text
Wide 16:9 landscape cinematic frame. a shelf of glowing spell orbs, each with a different small icon: a sword, a flower, a broom, a shield. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Kỳ thi cũng cho thấy trong Frieren, phép thuật không chỉ là tấn công. Có phép trói, phép tạo ảo ảnh, phép sao…

```text
Wide 16:9 landscape cinematic frame. a montage of spells: glowing ropes, illusion mirrors, and a shadow duplicate stepping out of a portal. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Một phần nổi bật là mê cung với những bản sao của chính các thí sinh. Muốn vượt qua, bạn phải thắng được chín…

```text
Wide 16:9 landscape cinematic frame. a mage facing an identical shadowy copy of themselves in a stone labyrinth. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: kỳ thi là một cách rất khéo để giới thiệu hàng loạt kiểu phép thuật mà không cần giải thích kh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding an exam paper with a gold star, proud expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Những phép thuật vô dụng mà Frieren sưu tầm

Lời: Và giờ tới chi tiết mà fan yêu nhất: Frieren thích sưu tầm những phép thuật kỳ lạ, nghe thì vô dụng.

```text
Wide 16:9 landscape cinematic frame. an elf mage happily opening an old grimoire at a market stall full of dusty books. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Có phép làm sạch gỉ trên tượng đồng, phép làm hoa nở, phép tìm đồ bị mất. Cô có thể đi cả chặng đường dài chỉ…

```text
Wide 16:9 landscape cinematic frame. a small montage: a bronze statue sparkling clean, a field of flowers blooming, a lost ring glowing under leaves. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Phép làm hoa nở có ý nghĩa đặc biệt. Đó là phép mà thầy Flamme thích, và là phép gắn với những ký ức của Frie…

```text
Wide 16:9 landscape cinematic frame. a meadow bursting into blue and white flowers under a golden sunset, a single figure standing in it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nhìn qua thì đây chỉ là sở thích, nhưng nó nói lên triết lý của cả bộ truyện: phép thuật không chỉ để chiến đ…

```text
Wide 16:9 landscape cinematic frame. a gentle scene of travelers smiling at a small magic sparkle over a village fountain. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và đôi khi, chính những phép thuật tưởng vô dụng lại cứu cả tổ đội trong một tình huống bất ngờ.

```text
Wide 16:9 landscape cinematic frame. a small glowing trick spell opening a sealed door while companions look surprised. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Vì sao Frieren mạnh?

Lời: Tổng hợp lại, Frieren mạnh không chỉ vì ma lực lớn. Cô mạnh vì bốn thứ cộng lại với nhau qua hơn một nghìn nă…

```text
Wide 16:9 landscape cinematic frame. four glowing pillars forming a foundation under a small calm elf figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Thứ nhất là thời gian. Là tiên tộc, cô có hơn một nghìn năm để tích lũy ma lực và kinh nghiệm. Không con ngườ…

```text
Wide 16:9 landscape cinematic frame. an hourglass the size of a tower with an elf walking beside it through changing seasons. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Thứ hai là sự kiên nhẫn trong việc giấu ma lực. Cô biến sự coi thường của kẻ thù thành vũ khí.

```text
Wide 16:9 landscape cinematic frame. a tiny aura concealing a vast glowing shadow, demons laughing without noticing. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Thứ ba là kinh nghiệm chiến đấu với ma tộc. Cô hiểu cách chúng nghĩ, và biết chúng sẽ phạm sai lầm ở đâu.

```text
Wide 16:9 landscape cinematic frame. a strategist silhouette studying a map full of demon markers by lamplight. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Thứ tư là sự tò mò. Việc sưu tầm đủ loại phép khiến cô có câu trả lời cho những tình huống mà pháp sư khác kh…

```text
Wide 16:9 landscape cinematic frame. a bookshelf overflowing with oddly shaped grimoires, a lantern glowing on top. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Nhưng chính Frieren cũng không bất khả chiến bại. Truyện cho thấy có những người vẫn vượt trội cô, và cô biết…

```text
Wide 16:9 landscape cinematic frame. an elf mage looking up at a much taller silhouette standing on a mountain peak. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Flamme và Serie: hai triết lý về ma thuật

Lời: Đứng sau lịch sử ma thuật của con người trong truyện là hai cái tên: Flamme và Serie.

```text
Wide 16:9 landscape cinematic frame. two elegant mage silhouettes facing each other across an ancient hall, one human, one elf. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Flamme được xem là người đặt nền móng cho ma thuật của loài người. Bà là thầy của Frieren, và từng là học trò…

```text
Wide 16:9 landscape cinematic frame. an older human mage silhouette writing in a large book as students gather around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Theo truyện, Flamme mơ về một thời đại mà ma thuật trở nên bình thường, ai cũng có thể học. Và thời đại đó cu…

```text
Wide 16:9 landscape cinematic frame. a sunny town square where ordinary people use small spells to light lamps and carry water. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Serie thì khác. Bà là pháp sư tiên tộc cổ xưa, gần như biết mọi phép thuật, và nhìn ma thuật chủ yếu qua lăng…

```text
Wide 16:9 landscape cinematic frame. an ancient elf mage on a throne surrounded by countless floating grimoires. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Hai triết lý này tạo nên sự đối lập thú vị: ma thuật để chiến đấu, hay ma thuật để sống. Frieren đứng đâu đó…

```text
Wide 16:9 landscape cinematic frame. a road splitting in two directions, one toward a battlefield, one toward a flower field, an elf standing at the fork. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là lý do Frieren sưu tầm phép vô dụng: cô mang theo giấc mơ của Flamme, dù bản thân là một chiế…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a sword in one wing and a flower in the other, balancing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Thử nghiệm: nếu bạn là một pháp sư

Lời: Thử tưởng tượng bạn là pháp sư mới học trong thế giới Frieren. Dựa trên những gì truyện kể, bạn nên học theo…

```text
Wide 16:9 landscape cinematic frame. a young apprentice silhouette standing at the entrance of a huge magic library. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bước một: học điều khiển và cảm nhận ma lực. Không cảm nhận được ma lực của người khác thì bạn không đánh giá…

```text
Wide 16:9 landscape cinematic frame. an apprentice meditating with eyes closed, faint auras of distant figures appearing around them. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bước hai: học phép phòng thủ. Trong thời đại Zoltraak đã phổ thông, không biết phòng thủ là cách nhanh nhất đ…

```text
Wide 16:9 landscape cinematic frame. an apprentice raising a hexagonal shield against a training beam. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Bước ba: học Zoltraak, phép tấn công cơ bản mà ai cũng dùng. Fern là ví dụ cho thấy chỉ cần dùng phép cơ bản…

```text
Wide 16:9 landscape cinematic frame. a young mage firing a rapid volley of violet beams with perfect precision. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Bước bốn: học đè nén ma lực. Đây là kỹ năng khó nhất, cần rèn luyện nhiều năm, nhưng giá trị thì vô cùng lớn.

```text
Wide 16:9 landscape cinematic frame. an apprentice practicing in daily life, carrying water buckets with a perfectly still faint aura. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Và bước năm, không bắt buộc nhưng đáng làm: học vài phép vô dụng. Vì bạn không bao giờ biết khi nào chúng trở…

```text
Wide 16:9 landscape cinematic frame. an apprentice grinning at a tiny sparkle spell that makes a flower bloom on a windowsill. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Ma thuật và Himmel

Lời: Cuối cùng, không thể nói về ma thuật trong Frieren mà bỏ qua Himmel, người anh hùng không phải là pháp sư.

```text
Wide 16:9 landscape cinematic frame. a heroic swordsman silhouette seen from behind, looking at a sunset over a field. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Himmel không dùng ma thuật, nhưng anh luôn trân trọng những phép thuật nhỏ của Frieren, kể cả những phép chẳn…

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette smiling as a small magic sparkle blooms in an elf's hand. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Nhiều năm sau khi Himmel mất, Frieren mới hiểu những khoảnh khắc đó quan trọng thế nào. Hành trình của cô cũn…

```text
Wide 16:9 landscape cinematic frame. an elf walking alone along a long road lined with flower fields, carrying a small bouquet. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Đây là điều làm Frieren khác mọi bộ fantasy khác: hệ thống ma thuật không chỉ để giải thích ai mạnh hơn, mà c…

```text
Wide 16:9 landscape cinematic frame. a spellbook open to a page where a pressed flower lies between glowing lines of text. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Góc nhìn của Kaku: hệ thống ma thuật như khoa học · **Kaku** (đính kèm ảnh mẫu)

Lời: Điều khiến mình thích Frieren nhất là cách truyện coi ma thuật như một ngành khoa học có lịch sử.

```text
Wide 16:9 landscape cinematic frame. a museum hall with display cases of glowing ancient spells, labeled with timelines. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Phép thuật được phát minh, bị phân tích, được cải tiến, rồi trở nên lỗi thời. Giống như vũ khí và công nghệ n…

```text
Wide 16:9 landscape cinematic frame. a timeline from a primitive bow to a modern rifle drawn in glowing magical style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Điều này làm thế giới có chiều sâu. Mạnh không chỉ nhờ tài năng, mà còn nhờ biết kiến thức mới nhất.

```text
Wide 16:9 landscape cinematic frame. a young mage reading the newest edition of a spellbook while an old mage uses an outdated scroll. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Nó cũng giải thích vì sao ma tộc sống hàng trăm năm nhưng không phải lúc nào cũng mạnh hơn con người: con ngư…

```text
Wide 16:9 landscape cinematic frame. a relay race of human mages passing a glowing torch through generations. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: So với Nen hay Chú lực mà mình đã giải thích, ma thuật của Frieren nhẹ nhàng hơn, nhưng có một thứ đặc biệt:…

```text
Wide 16:9 landscape cinematic frame. three symbols side by side: a hexagon, a dark dome, and an old spellbook with a clock. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Và vì thế, mỗi trận đấu trong Frieren không chỉ là ai mạnh hơn, mà là ai hiểu phép thuật của thời đại mình rõ…

```text
Wide 16:9 landscape cinematic frame. two mages facing each other, one holding an ancient scroll, one holding a modern book. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · Tóm tắt

Lời: Tóm lại: ma thuật trong Frieren cần ma lực và trí tưởng tượng. Thứ không hình dung được thì không làm được.

```text
Wide 16:9 landscape cinematic frame. a summary diagram: a glowing energy orb plus a thought bubble equals a spell. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92

Lời: Zoltraak cho thấy phép thuật tiến hóa: từ ma pháp giết người thành bài học vỡ lòng chỉ sau tám mươi năm.

```text
Wide 16:9 landscape cinematic frame. a violet beam transforming into a textbook page over a timeline arrow. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93

Lời: Và ma lực là thước đo, nhưng cũng là cái bẫy. Người giấu được sức mạnh thật mới là người đáng sợ nhất.

```text
Wide 16:9 landscape cinematic frame. a small faint aura casting an enormous shadow on a wall. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được Serie ban cho một phép thuật, bạn sẽ chọn phép gì? Mạnh hay đời thường? Viết xuống…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a glowing orb, looking at the viewer with curiosity. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã Haki trong One Piece, sức mạnh của ý chí.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing fist wrapped in black energy. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye in a warm library at night. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Ma thuật là gì trong Frieren?

Khoảng 123 giây · cảnh s01–s12 · 1595 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Frieren đến hết arc thi pháp sư hạng nhất. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Có một phép thuật từng giết vô số pháp sư và chiến binh loài người. Nó được gọi là ma pháp giết người, và từng là nỗi khiếp sợ của cả lục địa.

<short pause> Tám mươi năm sau, chính phép thuật đó được dạy cho người mới học như một đòn tấn công cơ bản nhất. Chuyện gì đã xảy ra?

<short pause> Câu trả lời cho thấy điều đặc biệt nhất của Frieren: ma thuật ở đây không đứng yên. Nó có lịch sử, được nghiên cứu, và tiến hóa như khoa học.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã ma thuật trong Frieren: nó vận hành thế nào, vì sao ma lực là tất cả, và vì sao Frieren mạnh.

<short pause> Xem hết video, bạn sẽ hiểu vì sao một pháp sư tưởng như yếu có thể là người đáng sợ nhất trên chiến trường.

<short pause> Trong Frieren, ma thuật dùng ma lực, một dạng năng lượng mà mỗi pháp sư mang trong người. Lượng ma lực nhiều hay ít khác nhau rất lớn giữa từng người.

<short pause> Nhưng ma lực chỉ là nhiên liệu. Điều quyết định một phép thuật có thành hay không là khả năng hình dung của người dùng.

<short pause> Truyện nhiều lần nhấn mạnh: ma thuật là thế giới của trí tưởng tượng. Thứ bạn không thể hình dung rõ ràng thì bạn không thể biến nó thành phép.

<short pause> Đây là lý do có những phép rất khó với con người. Không phải vì thiếu ma lực, mà vì con người không thể tưởng tượng ra cách nó hoạt động.

<short pause> Phép bay là ví dụ nổi tiếng. Con người dùng được nó, nhưng không ai giải thích được hoàn toàn cơ chế, vì nó vốn có nguồn gốc từ ma tộc.

<short pause> Kaku ghi chú: trong Frieren, trí tưởng tượng là giới hạn thật sự. Ma lực nhiều mà tưởng tượng nghèo thì cũng chỉ như có xăng mà không có xe.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Frieren đến hết arc thi pháp sư hạng nhất. Nếu bạn chưa xem tới đó, hãy lưu video lại nhé.

[pause] Có một phép thuật từng giết vô số pháp sư và chiến binh loài người. Nó được gọi là ma pháp giết người, và từng là nỗi khiếp sợ của cả lục địa.

[pause] Tám mươi năm sau, chính phép thuật đó được dạy cho người mới học như một đòn tấn công cơ bản nhất. [curious] Chuyện gì đã xảy ra?

[pause] Câu trả lời cho thấy điều đặc biệt nhất của Frieren: ma thuật ở đây không đứng yên. Nó có lịch sử, được nghiên cứu, và tiến hóa như khoa học.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã ma thuật trong Frieren: nó vận hành thế nào, vì sao ma lực là tất cả, và vì sao Frieren mạnh.

[pause] Xem hết video, bạn sẽ hiểu vì sao một pháp sư tưởng như yếu có thể là người đáng sợ nhất trên chiến trường.

[pause] Trong Frieren, ma thuật dùng ma lực, một dạng năng lượng mà mỗi pháp sư mang trong người. Lượng ma lực nhiều hay ít khác nhau rất lớn giữa từng người.

[pause] Nhưng ma lực chỉ là nhiên liệu. Điều quyết định một phép thuật có thành hay không là khả năng hình dung của người dùng.

[pause] Truyện nhiều lần nhấn mạnh: ma thuật là thế giới của trí tưởng tượng. Thứ bạn không thể hình dung rõ ràng thì bạn không thể biến nó thành phép.

[pause] Đây là lý do có những phép rất khó với con người. Không phải vì thiếu ma lực, mà vì con người không thể tưởng tượng ra cách nó hoạt động.

[pause] Phép bay là ví dụ nổi tiếng. Con người dùng được nó, nhưng không ai giải thích được hoàn toàn cơ chế, vì nó vốn có nguồn gốc từ ma tộc.

[pause] Kaku ghi chú: trong Frieren, trí tưởng tượng là giới hạn thật sự. Ma lực nhiều mà tưởng tượng nghèo thì cũng chỉ như có xăng mà không có xe.
```

### c02 · Ma pháp giết người: câu chuyện của Zoltraak

Khoảng 97 giây · cảnh s13–s22 · 1265 ký tự

**Gemini**

```text
Giờ quay lại phép thuật ở phần mở đầu. Nó có tên Zoltraak, được tạo ra bởi một ma tộc tên Qual.

<short pause> Zoltraak là phép đầu tiên xuyên thủng được lớp phòng thủ bằng ma lực của con người. Trước nó, pháp sư loài người còn tự tin đỡ được phép của ma tộc.

<short pause> Kết quả rất khủng khiếp. Trong thời gian đó, phần lớn pháp sư và mạo hiểm giả bị giết đều chết bởi Zoltraak.

<short pause> Rồi Frieren cùng tổ đội của Himmel đã phong ấn Qual. Ông ta bị khóa lại, còn phép thuật của ông ta ở lại với thế giới.

<short pause> Và đây là điều thú vị nhất: trong gần tám mươi năm Qual bị phong ấn, loài người đã mổ xẻ Zoltraak.

<short pause> Họ phân tích nó, hiểu nó, đưa nó vào giáo trình. Zoltraak trở thành thứ gọi là ma pháp tấn công thông thường, phép ai học pháp thuật cũng biết.

<short pause> Cùng lúc đó, phép phòng thủ cũng được phát triển để chặn đúng loại tấn công này. Mối đe dọa lớn nhất đã trở thành bài học vỡ lòng.

<short pause> Khi Qual được giải phong ấn, ông ta dùng Zoltraak như xưa và phát hiện nó không còn là vũ khí tất thắng. Thế giới đã đi trước ông ta tám mươi năm.

<short pause> Đây là một trong những ý tưởng hay nhất của Frieren: sức mạnh không đứng yên. Thứ mạnh nhất hôm nay có thể là kiến thức phổ thông ngày mai.

<short pause> <laugh> Kaku ví von: giống như một loại virus nguy hiểm, và nhân loại đã nghiên cứu ra vắc-xin. Virus vẫn còn đó, nhưng không còn đáng sợ như trước.
```

**ElevenLabs**

```text
Giờ quay lại phép thuật ở phần mở đầu. Nó có tên Zoltraak, được tạo ra bởi một ma tộc tên Qual.

[pause] Zoltraak là phép đầu tiên xuyên thủng được lớp phòng thủ bằng ma lực của con người. Trước nó, pháp sư loài người còn tự tin đỡ được phép của ma tộc.

[pause] Kết quả rất khủng khiếp. Trong thời gian đó, phần lớn pháp sư và mạo hiểm giả bị giết đều chết bởi Zoltraak.

[pause] Rồi Frieren cùng tổ đội của Himmel đã phong ấn Qual. Ông ta bị khóa lại, còn phép thuật của ông ta ở lại với thế giới.

[pause] Và đây là điều thú vị nhất: trong gần tám mươi năm Qual bị phong ấn, loài người đã mổ xẻ Zoltraak.

[pause] Họ phân tích nó, hiểu nó, đưa nó vào giáo trình. Zoltraak trở thành thứ gọi là ma pháp tấn công thông thường, phép ai học pháp thuật cũng biết.

[pause] Cùng lúc đó, phép phòng thủ cũng được phát triển để chặn đúng loại tấn công này. Mối đe dọa lớn nhất đã trở thành bài học vỡ lòng.

[pause] Khi Qual được giải phong ấn, ông ta dùng Zoltraak như xưa và phát hiện nó không còn là vũ khí tất thắng. Thế giới đã đi trước ông ta tám mươi năm.

[pause] Đây là một trong những ý tưởng hay nhất của Frieren: sức mạnh không đứng yên. Thứ mạnh nhất hôm nay có thể là kiến thức phổ thông ngày mai.

[pause] [chuckles] Kaku ví von: giống như một loại virus nguy hiểm, và nhân loại đã nghiên cứu ra vắc-xin. Virus vẫn còn đó, nhưng không còn đáng sợ như trước.
```

### c03 · Ma tộc: kẻ thù biết nói

Khoảng 64 giây · cảnh s23–s29 · 832 ký tự

**Gemini**

```text
Muốn hiểu vì sao ma thuật của con người phải tiến hóa nhanh, cần hiểu kẻ thù của họ: ma tộc.

<short pause> Ma tộc trông giống người, nói tiếng người, thậm chí gọi tên cha mẹ. <short pause> Nhưng theo Frieren, chúng học ngôn ngữ chỉ để lừa con người.

<short pause> Truyện miêu tả ma tộc không có khái niệm gia đình hay lòng thương theo cách con người hiểu. Những lời xin tha của chúng thường chỉ là mồi nhử.

<short pause> Đây là lý do Frieren thẳng tay với ma tộc, điều khiến nhiều người lúc đầu thấy cô lạnh lùng. Cô đã thấy quá nhiều người chết vì tin lời chúng.

<short pause> Với ma tộc, ma thuật là bản năng và niềm tự hào. Mỗi ma tộc thường dành cả đời để hoàn thiện một phép duy nhất.

<short pause> Điều đó làm phép của chúng rất mạnh, nhưng cũng rất dễ bị con người nghiên cứu. Một phép duy nhất, dùng mãi, sẽ có ngày bị hiểu thấu.

<short pause> Và đó chính là số phận của Zoltraak. Ma tộc sống lâu, nhưng con người học nhanh hơn.
```

**ElevenLabs**

```text
Muốn hiểu vì sao ma thuật của con người phải tiến hóa nhanh, cần hiểu kẻ thù của họ: ma tộc.

[pause] Ma tộc trông giống người, nói tiếng người, thậm chí gọi tên cha mẹ. [pause] Nhưng theo Frieren, chúng học ngôn ngữ chỉ để lừa con người.

[pause] Truyện miêu tả ma tộc không có khái niệm gia đình hay lòng thương theo cách con người hiểu. Những lời xin tha của chúng thường chỉ là mồi nhử.

[pause] Đây là lý do Frieren thẳng tay với ma tộc, điều khiến nhiều người lúc đầu thấy cô lạnh lùng. Cô đã thấy quá nhiều người chết vì tin lời chúng.

[pause] Với ma tộc, ma thuật là bản năng và niềm tự hào. Mỗi ma tộc thường dành cả đời để hoàn thiện một phép duy nhất.

[pause] Điều đó làm phép của chúng rất mạnh, nhưng cũng rất dễ bị con người nghiên cứu. Một phép duy nhất, dùng mãi, sẽ có ngày bị hiểu thấu.

[pause] Và đó chính là số phận của Zoltraak. Ma tộc sống lâu, nhưng con người học nhanh hơn.
```

### c04 · Ma lực là thước đo, và cũng là cái bẫy

Khoảng 95 giây · cảnh s30–s39 · 1241 ký tự

**Gemini**

```text
Trong thế giới Frieren, cả pháp sư lẫn ma tộc đều cảm nhận được ma lực của người khác. Và với ma tộc, ma lực gần như là tất cả.

<short pause> Ma tộc coi ma lực như thước đo địa vị và sức mạnh. Chúng tự hào khoe ma lực của mình, và đánh giá đối thủ qua lượng ma lực tỏa ra.

<short pause> Frieren biết điều đó, nên suốt hơn một nghìn năm, cô luôn đè nén ma lực của mình xuống, để trông yếu hơn thực tế rất nhiều.

<short pause> Kỹ năng này được dạy bởi thầy của cô, Flamme. Bà dạy Frieren giấu ma lực cả khi ăn, khi ngủ, trong mọi khoảnh khắc của cuộc đời.

<short pause> Mục đích rất rõ ràng: để lừa ma tộc. Một ma tộc nhìn thấy ma lực yếu ớt sẽ khinh thường, và sự khinh thường đó là điểm yếu chết người.

<short pause> Trận đấu nổi tiếng nhất cho thấy điều này là trận với Aura, ma tộc sở hữu cán cân phục tùng.

<short pause> Cán cân này so ma lực của hai bên. Bên nào ít hơn sẽ bị bên kia điều khiển hoàn toàn. Aura tự tin vì ma lực của cô ta đã tích lũy hơn năm trăm năm.

<short pause> Nhưng khi Frieren thả lỏng ma lực thật của mình, cán cân nghiêng hẳn về phía cô. Aura bị chính phép thuật của mình phản lại.

<short pause> Bài học ở đây: trong Frieren, thông tin là vũ khí. Người để lộ ma lực thật là người đã cho đối thủ biết mình mạnh tới đâu.

<short pause> <laugh> Kaku mỉm cười: người mạnh nhất phòng thường không phải người ồn ào nhất. Đôi khi là người ngồi yên uống trà ở góc.
```

**ElevenLabs**

```text
Trong thế giới Frieren, cả pháp sư lẫn ma tộc đều cảm nhận được ma lực của người khác. Và với ma tộc, ma lực gần như là tất cả.

[pause] Ma tộc coi ma lực như thước đo địa vị và sức mạnh. Chúng tự hào khoe ma lực của mình, và đánh giá đối thủ qua lượng ma lực tỏa ra.

[pause] Frieren biết điều đó, nên suốt hơn một nghìn năm, cô luôn đè nén ma lực của mình xuống, để trông yếu hơn thực tế rất nhiều.

[pause] Kỹ năng này được dạy bởi thầy của cô, Flamme. Bà dạy Frieren giấu ma lực cả khi ăn, khi ngủ, trong mọi khoảnh khắc của cuộc đời.

[pause] Mục đích rất rõ ràng: để lừa ma tộc. Một ma tộc nhìn thấy ma lực yếu ớt sẽ khinh thường, và sự khinh thường đó là điểm yếu chết người.

[pause] Trận đấu nổi tiếng nhất cho thấy điều này là trận với Aura, ma tộc sở hữu cán cân phục tùng.

[pause] Cán cân này so ma lực của hai bên. Bên nào ít hơn sẽ bị bên kia điều khiển hoàn toàn. Aura tự tin vì ma lực của cô ta đã tích lũy hơn năm trăm năm.

[pause] Nhưng khi Frieren thả lỏng ma lực thật của mình, cán cân nghiêng hẳn về phía cô. Aura bị chính phép thuật của mình phản lại.

[pause] Bài học ở đây: trong Frieren, thông tin là vũ khí. Người để lộ ma lực thật là người đã cho đối thủ biết mình mạnh tới đâu.

[pause] [chuckles] Kaku mỉm cười: người mạnh nhất phòng thường không phải người ồn ào nhất. Đôi khi là người ngồi yên uống trà ở góc.
```

### c05 · Kỹ năng đè nén ma lực có giá gì? / Phép của pháp sư và phép của nữ thần

Khoảng 115 giây · cảnh s40–s51 · 1493 ký tự

**Gemini**

```text
Đè nén ma lực nghe như chỉ có lợi, nhưng nó có cái giá. Khi luôn giấu sức mạnh, bạn phải chịu bị coi thường, bị đánh giá thấp suốt nhiều năm.

<short pause> Nhiều pháp sư trong truyện không tin một người trông yếu như Frieren lại là pháp sư huyền thoại. Với cô, điều đó không quan trọng.

<short pause> Kỹ năng này cũng rất khó. Chỉ cần dao động một chút khi chiến đấu, ma lực thật có thể lộ ra. Nó đòi hỏi kỷ luật tuyệt đối trong thời gian dài.

<short pause> Học trò của Frieren, Fern, cũng học được kỹ năng này và làm tốt tới mức ngay cả Frieren cũng khó nhận ra dao động ma lực của cô.

<short pause> Nhưng có người nhìn xuyên được lớp ngụy trang đó: Serie, một pháp sư tiên tộc cổ xưa, được coi là gần với thần thoại.

<short pause> Điều này cho thấy không có kỹ năng nào là tuyệt đối. Luôn có ai đó già hơn, tinh hơn, và nhìn thấy thứ bạn giấu.

<short pause> Trong Frieren còn có một nhánh phép thuật khác hẳn: phép của nữ thần, được dùng bởi các tu sĩ.

<short pause> Phép nữ thần đến từ kinh thánh. Tu sĩ dùng nó để chữa thương, giải độc, xua tà. Đây là thứ pháp sư thường không làm được.

<short pause> Điều thú vị là ngay cả tu sĩ cũng không hiểu hết vì sao phép nữ thần hoạt động. Họ tin, và niềm tin đó là một phần của phép.

<short pause> Tổ đội anh hùng năm xưa có một tu sĩ, và tổ đội mới của Frieren cũng cần một người như vậy. Trong thế giới này, chữa lành quan trọng không kém tấn công.

<short pause> Hai nhánh phép này bổ sung cho nhau: pháp sư dựa vào hình dung và nghiên cứu, tu sĩ dựa vào kinh thánh và niềm tin.

<short pause> <laugh> Kaku ghi chú: một tổ đội cân bằng luôn cần cả người phá và người chữa. Đó cũng là bài học cho mọi đội nhóm ngoài đời.
```

**ElevenLabs**

```text
Đè nén ma lực nghe như chỉ có lợi, nhưng nó có cái giá. Khi luôn giấu sức mạnh, bạn phải chịu bị coi thường, bị đánh giá thấp suốt nhiều năm.

[pause] Nhiều pháp sư trong truyện không tin một người trông yếu như Frieren lại là pháp sư huyền thoại. Với cô, điều đó không quan trọng.

[pause] Kỹ năng này cũng rất khó. Chỉ cần dao động một chút khi chiến đấu, ma lực thật có thể lộ ra. Nó đòi hỏi kỷ luật tuyệt đối trong thời gian dài.

[pause] Học trò của Frieren, Fern, cũng học được kỹ năng này và làm tốt tới mức ngay cả Frieren cũng khó nhận ra dao động ma lực của cô.

[pause] Nhưng có người nhìn xuyên được lớp ngụy trang đó: Serie, một pháp sư tiên tộc cổ xưa, được coi là gần với thần thoại.

[pause] Điều này cho thấy không có kỹ năng nào là tuyệt đối. Luôn có ai đó già hơn, tinh hơn, và nhìn thấy thứ bạn giấu.

[pause] Trong Frieren còn có một nhánh phép thuật khác hẳn: phép của nữ thần, được dùng bởi các tu sĩ.

[pause] Phép nữ thần đến từ kinh thánh. Tu sĩ dùng nó để chữa thương, giải độc, xua tà. Đây là thứ pháp sư thường không làm được.

[pause] Điều thú vị là ngay cả tu sĩ cũng không hiểu hết vì sao phép nữ thần hoạt động. Họ tin, và niềm tin đó là một phần của phép.

[pause] Tổ đội anh hùng năm xưa có một tu sĩ, và tổ đội mới của Frieren cũng cần một người như vậy. Trong thế giới này, chữa lành quan trọng không kém tấn công.

[pause] Hai nhánh phép này bổ sung cho nhau: pháp sư dựa vào hình dung và nghiên cứu, tu sĩ dựa vào kinh thánh và niềm tin.

[pause] [chuckles] Kaku ghi chú: một tổ đội cân bằng luôn cần cả người phá và người chữa. Đó cũng là bài học cho mọi đội nhóm ngoài đời.
```

### c06 · Kỳ thi pháp sư hạng nhất / Những phép thuật vô dụng mà Frieren sưu tầm

Khoảng 107 giây · cảnh s52–s62 · 1397 ký tự

**Gemini**

```text
Một arc lớn của Frieren là kỳ thi pháp sư hạng nhất. Đây là nơi hệ thống ma thuật được thể hiện đa dạng nhất.

<short pause> Kỳ thi do Serie đứng sau. Người đỗ không chỉ có danh hiệu, mà còn được Serie ban cho một phép thuật mà họ mong muốn.

<short pause> Điều thú vị là mỗi người chọn một kiểu phép khác nhau, và lựa chọn đó nói lên con người họ. Có người chọn phép mạnh, có người chọn phép rất đời thường.

<short pause> Kỳ thi cũng cho thấy trong Frieren, phép thuật không chỉ là tấn công. Có phép trói, phép tạo ảo ảnh, phép sao chép chính đối thủ.

<short pause> Một phần nổi bật là mê cung với những bản sao của chính các thí sinh. Muốn vượt qua, bạn phải thắng được chính mình, với đầy đủ kỹ năng của mình.

<short pause> <laugh> Kaku nhận xét: kỳ thi là một cách rất khéo để giới thiệu hàng loạt kiểu phép thuật mà không cần giải thích khô khan. Mỗi thí sinh là một bài học.

<short pause> Và giờ tới chi tiết mà fan yêu nhất: Frieren thích sưu tầm những phép thuật kỳ lạ, nghe thì vô dụng.

<short pause> Có phép làm sạch gỉ trên tượng đồng, phép làm hoa nở, phép tìm đồ bị mất. Cô có thể đi cả chặng đường dài chỉ để đổi lấy một phép như vậy.

<short pause> Phép làm hoa nở có ý nghĩa đặc biệt. Đó là phép mà thầy Flamme thích, và là phép gắn với những ký ức của Frieren về Himmel.

<short pause> Nhìn qua thì đây chỉ là sở thích, nhưng nó nói lên triết lý của cả bộ truyện: phép thuật không chỉ để chiến đấu, mà còn để làm cuộc sống đẹp hơn.

<short pause> Và đôi khi, chính những phép thuật tưởng vô dụng lại cứu cả tổ đội trong một tình huống bất ngờ.
```

**ElevenLabs**

```text
Một arc lớn của Frieren là kỳ thi pháp sư hạng nhất. Đây là nơi hệ thống ma thuật được thể hiện đa dạng nhất.

[pause] Kỳ thi do Serie đứng sau. Người đỗ không chỉ có danh hiệu, mà còn được Serie ban cho một phép thuật mà họ mong muốn.

[pause] Điều thú vị là mỗi người chọn một kiểu phép khác nhau, và lựa chọn đó nói lên con người họ. Có người chọn phép mạnh, có người chọn phép rất đời thường.

[pause] Kỳ thi cũng cho thấy trong Frieren, phép thuật không chỉ là tấn công. Có phép trói, phép tạo ảo ảnh, phép sao chép chính đối thủ.

[pause] Một phần nổi bật là mê cung với những bản sao của chính các thí sinh. Muốn vượt qua, bạn phải thắng được chính mình, với đầy đủ kỹ năng của mình.

[pause] [chuckles] Kaku nhận xét: kỳ thi là một cách rất khéo để giới thiệu hàng loạt kiểu phép thuật mà không cần giải thích khô khan. Mỗi thí sinh là một bài học.

[pause] Và giờ tới chi tiết mà fan yêu nhất: Frieren thích sưu tầm những phép thuật kỳ lạ, nghe thì vô dụng.

[pause] Có phép làm sạch gỉ trên tượng đồng, phép làm hoa nở, phép tìm đồ bị mất. Cô có thể đi cả chặng đường dài chỉ để đổi lấy một phép như vậy.

[pause] Phép làm hoa nở có ý nghĩa đặc biệt. Đó là phép mà thầy Flamme thích, và là phép gắn với những ký ức của Frieren về Himmel.

[pause] Nhìn qua thì đây chỉ là sở thích, nhưng nó nói lên triết lý của cả bộ truyện: phép thuật không chỉ để chiến đấu, mà còn để làm cuộc sống đẹp hơn.

[pause] Và đôi khi, chính những phép thuật tưởng vô dụng lại cứu cả tổ đội trong một tình huống bất ngờ.
```

### c07 · Vì sao Frieren mạnh? / Flamme và Serie: hai triết lý về ma thuật

Khoảng 107 giây · cảnh s63–s74 · 1394 ký tự

**Gemini**

```text
Tổng hợp lại, Frieren mạnh không chỉ vì ma lực lớn. Cô mạnh vì bốn thứ cộng lại với nhau qua hơn một nghìn năm.

<short pause> Thứ nhất là thời gian. Là tiên tộc, cô có hơn một nghìn năm để tích lũy ma lực và kinh nghiệm. Không con người nào có được lợi thế đó.

<short pause> Thứ hai là sự kiên nhẫn trong việc giấu ma lực. Cô biến sự coi thường của kẻ thù thành vũ khí.

<short pause> Thứ ba là kinh nghiệm chiến đấu với ma tộc. Cô hiểu cách chúng nghĩ, và biết chúng sẽ phạm sai lầm ở đâu.

<short pause> Thứ tư là sự tò mò. Việc sưu tầm đủ loại phép khiến cô có câu trả lời cho những tình huống mà pháp sư khác không lường trước.

<short pause> Nhưng chính Frieren cũng không bất khả chiến bại. Truyện cho thấy có những người vẫn vượt trội cô, và cô biết điều đó.

<short pause> Đứng sau lịch sử ma thuật của con người trong truyện là hai cái tên: Flamme và Serie.

<short pause> Flamme được xem là người đặt nền móng cho ma thuật của loài người. Bà là thầy của Frieren, và từng là học trò của Serie.

<short pause> Theo truyện, Flamme mơ về một thời đại mà ma thuật trở nên bình thường, ai cũng có thể học. Và thời đại đó cuối cùng đã tới.

<short pause> Serie thì khác. Bà là pháp sư tiên tộc cổ xưa, gần như biết mọi phép thuật, và nhìn ma thuật chủ yếu qua lăng kính sức mạnh và chiến đấu.

<short pause> Hai triết lý này tạo nên sự đối lập thú vị: ma thuật để chiến đấu, hay ma thuật để sống. Frieren đứng đâu đó ở giữa.

<short pause> <laugh> Kaku nghĩ đây là lý do Frieren sưu tầm phép vô dụng: cô mang theo giấc mơ của Flamme, dù bản thân là một chiến binh cực mạnh.
```

**ElevenLabs**

```text
Tổng hợp lại, Frieren mạnh không chỉ vì ma lực lớn. Cô mạnh vì bốn thứ cộng lại với nhau qua hơn một nghìn năm.

[pause] Thứ nhất là thời gian. Là tiên tộc, cô có hơn một nghìn năm để tích lũy ma lực và kinh nghiệm. Không con người nào có được lợi thế đó.

[pause] Thứ hai là sự kiên nhẫn trong việc giấu ma lực. Cô biến sự coi thường của kẻ thù thành vũ khí.

[pause] Thứ ba là kinh nghiệm chiến đấu với ma tộc. Cô hiểu cách chúng nghĩ, và biết chúng sẽ phạm sai lầm ở đâu.

[pause] Thứ tư là sự tò mò. Việc sưu tầm đủ loại phép khiến cô có câu trả lời cho những tình huống mà pháp sư khác không lường trước.

[pause] Nhưng chính Frieren cũng không bất khả chiến bại. Truyện cho thấy có những người vẫn vượt trội cô, và cô biết điều đó.

[pause] Đứng sau lịch sử ma thuật của con người trong truyện là hai cái tên: Flamme và Serie.

[pause] Flamme được xem là người đặt nền móng cho ma thuật của loài người. Bà là thầy của Frieren, và từng là học trò của Serie.

[pause] Theo truyện, Flamme mơ về một thời đại mà ma thuật trở nên bình thường, ai cũng có thể học. Và thời đại đó cuối cùng đã tới.

[pause] Serie thì khác. Bà là pháp sư tiên tộc cổ xưa, gần như biết mọi phép thuật, và nhìn ma thuật chủ yếu qua lăng kính sức mạnh và chiến đấu.

[pause] Hai triết lý này tạo nên sự đối lập thú vị: ma thuật để chiến đấu, hay ma thuật để sống. Frieren đứng đâu đó ở giữa.

[pause] [chuckles] Kaku nghĩ đây là lý do Frieren sưu tầm phép vô dụng: cô mang theo giấc mơ của Flamme, dù bản thân là một chiến binh cực mạnh.
```

### c08 · Thử nghiệm: nếu bạn là một pháp sư / Ma thuật và Himmel / Góc nhìn của Kaku: hệ thống ma thuật như khoa học

Khoảng 153 giây · cảnh s75–s90 · 1994 ký tự

**Gemini**

```text
Thử tưởng tượng bạn là pháp sư mới học trong thế giới Frieren. Dựa trên những gì truyện kể, bạn nên học theo thứ tự nào?

<short pause> Bước một: học điều khiển và cảm nhận ma lực. Không cảm nhận được ma lực của người khác thì bạn không đánh giá được nguy hiểm.

<short pause> Bước hai: học phép phòng thủ. Trong thời đại Zoltraak đã phổ thông, không biết phòng thủ là cách nhanh nhất để thua.

<short pause> Bước ba: học Zoltraak, phép tấn công cơ bản mà ai cũng dùng. Fern là ví dụ cho thấy chỉ cần dùng phép cơ bản cực nhanh và cực chính xác cũng đủ đáng sợ.

<short pause> Bước bốn: học đè nén ma lực. Đây là kỹ năng khó nhất, cần rèn luyện nhiều năm, nhưng giá trị thì vô cùng lớn.

<short pause> Và bước năm, không bắt buộc nhưng đáng làm: học vài phép vô dụng. Vì bạn không bao giờ biết khi nào chúng trở nên hữu ích.

<short pause> Cuối cùng, không thể nói về ma thuật trong Frieren mà bỏ qua Himmel, người anh hùng không phải là pháp sư.

<short pause> Himmel không dùng ma thuật, nhưng anh luôn trân trọng những phép thuật nhỏ của Frieren, kể cả những phép chẳng giúp gì trong chiến đấu.

<short pause> Nhiều năm sau khi Himmel mất, Frieren mới hiểu những khoảnh khắc đó quan trọng thế nào. Hành trình của cô cũng là hành trình tìm hiểu con người.

<short pause> Đây là điều làm Frieren khác mọi bộ fantasy khác: hệ thống ma thuật không chỉ để giải thích ai mạnh hơn, mà còn để kể về thời gian và ký ức.

<short pause> Điều khiến mình thích Frieren nhất là cách truyện coi ma thuật như một ngành khoa học có lịch sử.

<short pause> Phép thuật được phát minh, bị phân tích, được cải tiến, rồi trở nên lỗi thời. Giống như vũ khí và công nghệ ngoài đời thật.

<short pause> Điều này làm thế giới có chiều sâu. Mạnh không chỉ nhờ tài năng, mà còn nhờ biết kiến thức mới nhất.

<short pause> Nó cũng giải thích vì sao ma tộc sống hàng trăm năm nhưng không phải lúc nào cũng mạnh hơn con người: con người học hỏi và truyền lại kiến thức nhanh hơn.

<short pause> So với Nen hay Chú lực mà mình đã giải thích, ma thuật của Frieren nhẹ nhàng hơn, nhưng có một thứ đặc biệt: nó có thời gian, có lịch sử.

<short pause> Và vì thế, mỗi trận đấu trong Frieren không chỉ là ai mạnh hơn, mà là ai hiểu phép thuật của thời đại mình rõ hơn.
```

**ElevenLabs**

```text
Thử tưởng tượng bạn là pháp sư mới học trong thế giới Frieren. [curious] Dựa trên những gì truyện kể, bạn nên học theo thứ tự nào?

[pause] Bước một: học điều khiển và cảm nhận ma lực. Không cảm nhận được ma lực của người khác thì bạn không đánh giá được nguy hiểm.

[pause] Bước hai: học phép phòng thủ. Trong thời đại Zoltraak đã phổ thông, không biết phòng thủ là cách nhanh nhất để thua.

[pause] Bước ba: học Zoltraak, phép tấn công cơ bản mà ai cũng dùng. Fern là ví dụ cho thấy chỉ cần dùng phép cơ bản cực nhanh và cực chính xác cũng đủ đáng sợ.

[pause] Bước bốn: học đè nén ma lực. Đây là kỹ năng khó nhất, cần rèn luyện nhiều năm, nhưng giá trị thì vô cùng lớn.

[pause] Và bước năm, không bắt buộc nhưng đáng làm: học vài phép vô dụng. Vì bạn không bao giờ biết khi nào chúng trở nên hữu ích.

[pause] Cuối cùng, không thể nói về ma thuật trong Frieren mà bỏ qua Himmel, người anh hùng không phải là pháp sư.

[pause] Himmel không dùng ma thuật, nhưng anh luôn trân trọng những phép thuật nhỏ của Frieren, kể cả những phép chẳng giúp gì trong chiến đấu.

[pause] Nhiều năm sau khi Himmel mất, Frieren mới hiểu những khoảnh khắc đó quan trọng thế nào. Hành trình của cô cũng là hành trình tìm hiểu con người.

[pause] Đây là điều làm Frieren khác mọi bộ fantasy khác: hệ thống ma thuật không chỉ để giải thích ai mạnh hơn, mà còn để kể về thời gian và ký ức.

[pause] Điều khiến mình thích Frieren nhất là cách truyện coi ma thuật như một ngành khoa học có lịch sử.

[pause] Phép thuật được phát minh, bị phân tích, được cải tiến, rồi trở nên lỗi thời. Giống như vũ khí và công nghệ ngoài đời thật.

[pause] Điều này làm thế giới có chiều sâu. Mạnh không chỉ nhờ tài năng, mà còn nhờ biết kiến thức mới nhất.

[pause] Nó cũng giải thích vì sao ma tộc sống hàng trăm năm nhưng không phải lúc nào cũng mạnh hơn con người: con người học hỏi và truyền lại kiến thức nhanh hơn.

[pause] So với Nen hay Chú lực mà mình đã giải thích, ma thuật của Frieren nhẹ nhàng hơn, nhưng có một thứ đặc biệt: nó có thời gian, có lịch sử.

[pause] Và vì thế, mỗi trận đấu trong Frieren không chỉ là ai mạnh hơn, mà là ai hiểu phép thuật của thời đại mình rõ hơn.
```

### c09 · Tóm tắt

Khoảng 44 giây · cảnh s91–s96 · 574 ký tự

**Gemini**

```text
Tóm lại: ma thuật trong Frieren cần ma lực và trí tưởng tượng. Thứ không hình dung được thì không làm được.

<short pause> Zoltraak cho thấy phép thuật tiến hóa: từ ma pháp giết người thành bài học vỡ lòng chỉ sau tám mươi năm.

<short pause> Và ma lực là thước đo, nhưng cũng là cái bẫy. Người giấu được sức mạnh thật mới là người đáng sợ nhất.

<short pause> Câu hỏi cho bạn: nếu được Serie ban cho một phép thuật, bạn sẽ chọn phép gì? Mạnh hay đời thường? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã Haki trong One Piece, sức mạnh của ý chí.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại: ma thuật trong Frieren cần ma lực và trí tưởng tượng. Thứ không hình dung được thì không làm được.

[pause] Zoltraak cho thấy phép thuật tiến hóa: từ ma pháp giết người thành bài học vỡ lòng chỉ sau tám mươi năm.

[pause] Và ma lực là thước đo, nhưng cũng là cái bẫy. Người giấu được sức mạnh thật mới là người đáng sợ nhất.

[pause] [curious] Câu hỏi cho bạn: nếu được Serie ban cho một phép thuật, bạn sẽ chọn phép gì? Mạnh hay đời thường? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã Haki trong One Piece, sức mạnh của ý chí.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
