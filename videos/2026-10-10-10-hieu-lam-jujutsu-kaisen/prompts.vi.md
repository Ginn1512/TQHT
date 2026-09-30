# Bộ prompt · Jujutsu Kaisen: 10 hiểu lầm mà gần như ai cũng từng tin

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 90 ảnh, 8 đoạn đọc, khoảng 15.0 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (90 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Jujutsu Kaisen tới hết anime mùa hai, arc Shibuya, và một ít đầu arc Trò chơi tử d…

```text
Wide 16:9 landscape cinematic frame. a dark city intersection at night with a faint purple barrier over the skyline. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Câu này bạn chắc chắn đã nghe: Hắc thiểm là tuyệt chiêu mà nhân vật mạnh có thể tung ra bất cứ lúc nào. Nghe…

```text
Wide 16:9 landscape cinematic frame. a sticky note on a wall reading a common belief, with a large red X slowly drawn across it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Sai. Và đó mới chỉ là hiểu lầm đầu tiên trong mười hiểu lầm mà Kaku gom được từ bình luận, diễn đàn và chính…

```text
Wide 16:9 landscape cinematic frame. a wall covered with ten pinned notes, each with a red question mark, a detective lamp shining on them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Với mỗi hiểu lầm, Kaku sẽ trả lời ba câu: người ta tin gì, truyện thực sự nói gì,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a red marker in one wing and an open notebook in the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và như mọi danh sách hay, hiểu lầm lớn nhất, cũng là hiểu lầm Kaku thấy nhiều nhất, được để dành tới cuối.

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding one note behind its back with a mischievous smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Hiểu lầm 1: Hắc thiểm là tuyệt chiêu

Lời: Người ta tin: Hắc thiểm là một đòn đánh đặc biệt, nhân vật mạnh có thể dùng khi cần, giống như tung một chiêu…

```text
Wide 16:9 landscape cinematic frame. a figure winding up a punch with black lightning crackling around the fist. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Truyện nói: Hắc thiểm không phải kỹ thuật, mà là một hiện tượng. Nó xảy ra khi chú lực chạm vào đối thủ chỉ t…

```text
Wide 16:9 landscape cinematic frame. a stopwatch frozen at an impossibly small fraction of a second beside a fist striking. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Khi trùng khớp đúng khoảnh khắc đó, không gian bị bóp méo, tia sét đen lóe lên, và sức mạnh cú đánh tăng vọt.…

```text
Wide 16:9 landscape cinematic frame. a distortion ripple in the air as black lightning bursts from a point of impact. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Không ai tạo ra Hắc thiểm theo ý muốn một cách chắc chắn. Ngay cả những chú thuật sư mạnh nhất cũng chỉ có th…

```text
Wide 16:9 landscape cinematic frame. a dartboard with a single tiny bullseye glowing black, most darts scattered around it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Vì sao dễ nhầm: vì anime thể hiện nó quá ngầu, với tên gọi và hiệu ứng riêng, nên trông giống hệt một chiêu c…

```text
Wide 16:9 landscape cinematic frame. a video game health bar and a flashy special move icon, crossed out. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Chi tiết hay: người từng tạo ra Hắc thiểm được cho là hiểu chú lực ở một tầm khác. Kaku nghĩ nó giống cảm giá…

```text
Wide 16:9 landscape cinematic frame. the owl mascot swinging a tiny bat and hitting a perfect shot, sparkles around it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Hiểu lầm 2: Chú linh là quái vật vô tri

Lời: Người ta tin: chú linh chỉ là quái vật, không có suy nghĩ, chỉ biết tấn công con người.

```text
Wide 16:9 landscape cinematic frame. a grotesque shapeless creature lurking in a dark school hallway. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Truyện nói: chú linh sinh ra từ cảm xúc tiêu cực của con người, như sợ hãi, căm ghét, lo âu. Phần lớn đúng là…

```text
Wide 16:9 landscape cinematic frame. a crowd of people with dark wisps rising from their heads, merging into a shadow above them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Có những chú linh cấp đặc biệt biết nói, biết lập kế hoạch, và còn có triết lý riêng. Một số sinh ra từ nỗi s…

```text
Wide 16:9 landscape cinematic frame. three shadowy intelligent figures standing on a volcano, in a forest and by the sea. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Có chú linh còn tự coi mình là loài người thật sự, vì chúng là cảm xúc thuần khiết của con người mà không có…

```text
Wide 16:9 landscape cinematic frame. a humanoid shadow looking into a mirror that reflects a human crowd. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Vì vậy, trong thế giới này, càng nhiều người cùng sợ một thứ, chú linh sinh ra từ nỗi sợ đó càng mạnh. Nỗi sợ…

```text
Wide 16:9 landscape cinematic frame. a city skyline where countless tiny dark wisps gather into one enormous shadow above the rooftops. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Vì sao dễ nhầm: những tập đầu chỉ cho thấy chú linh yếu, hình thù kỳ dị. Khán giả gắn hình ảnh đó cho mọi chú…

```text
Wide 16:9 landscape cinematic frame. a row of small ugly creatures, then a tall intelligent shadow stepping out from behind them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Hiểu lầm 3: Thuật thức luyện tập mà có

Lời: Người ta tin: nếu chăm chỉ, chú thuật sư có thể học được thuật thức mới, giống học một chiêu mới trong võ thu…

```text
Wide 16:9 landscape cinematic frame. a student bowing in a dojo in front of a scroll of techniques. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Truyện nói: thuật thức bẩm sinh được khắc sẵn trong cơ thể từ khi sinh ra. Người có thì có, người không có th…

```text
Wide 16:9 landscape cinematic frame. a glowing pattern engraved inside a silhouette's body like a circuit, visible from birth. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Luyện tập thay đổi cách dùng: mở rộng thuật thức, dùng ngược lại, hay đẩy tới mức tối đa. Nhưng gốc rễ vẫn là…

```text
Wide 16:9 landscape cinematic frame. a single seed growing into a tree with many branches, each branch labeled with a small icon. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Nhiều gia tộc chú thuật truyền thuật thức theo dòng máu, và coi đó là tài sản quý nhất, đến mức đánh giá con…

```text
Wide 16:9 landscape cinematic frame. an old clan house with family crests, children lined up while elders inspect them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Cũng có những trường hợp đặc biệt trong truyện cho phép dùng thuật thức của người khác, nhưng đó là ngoại lệ…

```text
Wide 16:9 landscape cinematic frame. a rare glowing key hovering over a locked box, surrounded by warning symbols. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì nhân vật mạnh lên rất nhanh trong truyện. Nhưng thứ họ học được là kỹ năng dùng chú lực, k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at two jars: one labeled born and one labeled trained. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · Hiểu lầm 4: Không có thuật thức thì yếu

Lời: Người ta tin: nhân vật chính Yuji ban đầu yếu vì không có thuật thức riêng như các bạn.

```text
Wide 16:9 landscape cinematic frame. a young fighter in a school uniform standing beside classmates with glowing techniques. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Truyện nói: Yuji có thể lực phi thường ngay từ đầu, chạy nhanh, đánh mạnh ở mức khiến chú thuật sư lâu năm cũ…

```text
Wide 16:9 landscape cinematic frame. a teenager throwing a shot put so far it disappears beyond a stadium. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Cậu còn có năng khiếu đặc biệt với Hắc thiểm. Trong một trận đấu, cậu tạo ra bốn Hắc thiểm liên tiếp, cân bằn…

```text
Wide 16:9 landscape cinematic frame. four black lightning flashes in a row lighting up a forest battlefield. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Trong thế giới này, không có thuật thức không đồng nghĩa với yếu. Có cả những nhân vật mạnh khủng khiếp mà hầ…

```text
Wide 16:9 landscape cinematic frame. a silhouette with a heavy weapon standing calmly amid defeated sorcerers. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Vì sao dễ nhầm: vì phần lớn thời lượng tập trung vào thuật thức hào nhoáng, nên thứ sức mạnh thuần túy của cơ…

```text
Wide 16:9 landscape cinematic frame. a spotlight on flashy spell effects while a fighter stands in the shadow beside it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Hiểu lầm 5: Chú lực đảo ngược chữa được mọi thứ

Lời: Người ta tin: ai dùng được chú lực đảo ngược là gần như bất tử, và có thể chữa lành cho bất kỳ ai.

```text
Wide 16:9 landscape cinematic frame. a glowing healing light around a figure, wounds closing instantly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Truyện nói: chú lực đảo ngược được tạo ra bằng cách nhân hai nguồn năng lượng âm với nhau để có năng lượng dư…

```text
Wide 16:9 landscape cinematic frame. a chalkboard showing minus times minus equals plus with glowing energy symbols. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Nó rất khó học. Chỉ một số ít chú thuật sư làm được, và đa số chỉ chữa được cho chính mình.

```text
Wide 16:9 landscape cinematic frame. a single sorcerer glowing with healing light while many others around them cannot. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Chữa cho người khác còn hiếm hơn nữa. Trong trường chú thuật, có một bác sĩ nổi tiếng chính vì làm được điều…

```text
Wide 16:9 landscape cinematic frame. a calm doctor in a white coat in an infirmary, a gentle glow from her hands over a patient. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Và nó không phải phép màu: nó cần chú lực, tốn sức, và không đưa được người đã chết trở lại.

```text
Wide 16:9 landscape cinematic frame. a fading hourglass beside a healing glow that flickers out. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì những nhân vật mạnh nhất dùng nó quá nhẹ nhàng, khiến người xem tưởng ai cũng làm được.

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying to multiply two small dark clouds together, getting only a puff of smoke. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Hiểu lầm 6: Lời thề ràng buộc chỉ có trong trận lớn

Lời: Người ta tin: lời thề ràng buộc là thứ hiếm, chỉ xuất hiện trong những giao kèo lớn và kịch tính.

```text
Wide 16:9 landscape cinematic frame. two figures shaking hands in a storm as glowing chains wrap around their wrists. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Truyện nói: lời thề ràng buộc có mặt ở khắp nơi, kể cả trong những thói quen nhỏ. Tự đặt giới hạn cho mình th…

```text
Wide 16:9 landscape cinematic frame. a daily planner with small glowing chains linking certain entries. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Ví dụ nổi tiếng là chú thuật sư làm việc như nhân viên văn phòng: ông tự giới hạn giờ làm, và khi phải làm th…

```text
Wide 16:9 landscape cinematic frame. a tired office worker loosening his tie as a clock passes six in the evening, his aura intensifying. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Một dạng khác rất phổ biến: tiết lộ thuật thức của mình cho đối thủ. Tự làm mình bất lợi thì thuật thức được…

```text
Wide 16:9 landscape cinematic frame. a fighter explaining their technique with diagrams while their aura grows brighter. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Lời thề cũng có thể được lập giữa hai người. Nhưng phá vỡ lời thề thì sẽ phải chịu hậu quả, và hậu quả đó khô…

```text
Wide 16:9 landscape cinematic frame. two glowing chains linking two hands, one chain snapping with a dark spark. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Vì sao dễ nhầm: vì trong nhiều bộ khác, nhân vật giải thích chiêu thức chỉ để khán giả hiểu. Ở đây, việc giải…

```text
Wide 16:9 landscape cinematic frame. a speech bubble with a small power-up arrow inside it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nên lần sau thấy nhân vật giải thích dài dòng giữa trận, đừng vội chê. Họ đang mạnh lên đấy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot lecturing at a chalkboard while a tiny power meter beside it fills up. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Hiểu lầm 7: Lãnh địa là không thể đỡ

Lời: Người ta tin: đã bị kéo vào lãnh địa là thua, vì mọi đòn trong lãnh địa đều trúng một trăm phần trăm.

```text
Wide 16:9 landscape cinematic frame. a figure trapped inside a dark dome as countless attacks rain down. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Truyện nói: đòn trong lãnh địa được bảo đảm trúng, nhưng vẫn có nhiều cách chống đỡ. Có kỹ thuật tạo một vùng…

```text
Wide 16:9 landscape cinematic frame. a small glowing circle around a figure's feet inside a dark dome, attacks bouncing off it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Cách mạnh nhất là mở lãnh địa của chính mình. Hai lãnh địa va chạm thì bên nào tinh xảo hơn sẽ lấn át bên kia.

```text
Wide 16:9 landscape cinematic frame. two domes of different colors colliding and pushing against each other. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đã giải thích chi tiết luật và các cách phá lãnh địa ở video số hai của kênh. Ở đây chỉ cần nhớ: lãnh đị…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small thumbnail of a dark dome pinned to its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Vì sao dễ nhầm: vì lần đầu xuất hiện, lãnh địa được thể hiện như một đòn kết thúc tuyệt đối, và cảm giác đó ở…

```text
Wide 16:9 landscape cinematic frame. a first-time viewer's silhouette frozen in shock in front of a glowing screen. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Hiểu lầm 8: Người mạnh nhất không thể bị chạm vào

Lời: Người ta tin: người được gọi là mạnh nhất có một lá chắn vô hạn, nên không gì có thể chạm vào anh ta.

```text
Wide 16:9 landscape cinematic frame. a figure standing calmly as punches and blades stop an inch away from his body. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Truyện nói: lá chắn đó dựa trên khái niệm vô hạn trong toán học. Thứ gì tiến lại gần sẽ chậm dần và không bao…

```text
Wide 16:9 landscape cinematic frame. a diagram of an arrow moving half the remaining distance again and again, never reaching a wall. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Nhưng lá chắn vẫn có giới hạn. Trong quá khứ, anh từng bị một người không có chú lực đâm xuyên, nhờ một vũ kh…

```text
Wide 16:9 landscape cinematic frame. a jagged dagger piercing through a shimmering invisible barrier, the barrier cracking. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Sau lần đó, anh tìm cách để lá chắn luôn tự động hoạt động. Nhưng câu chuyện đã chứng minh: không có sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a barrier re-forming around a figure, glowing with new strength after a close call. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Lá chắn cũng tiêu hao chú lực và cần tính toán cực kỳ chính xác. Anh làm được là nhờ đôi mắt đặc biệt giúp nh…

```text
Wide 16:9 landscape cinematic frame. a pair of glowing blue eyes reflecting intricate streams of energy like a circuit map. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Vì sao dễ nhầm: vì anh gần như luôn thắng dễ dàng trong mùa một, khiến người xem nghĩ lá chắn là vô địch. Mùa…

```text
Wide 16:9 landscape cinematic frame. a perfect glass sphere with a single hairline crack catching the light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Hiểu lầm 9: Megumi chỉ là nhân vật phụ

Lời: Người ta tin: Megumi, người bạn trầm tính của Yuji, chỉ là nhân vật phụ yếu hơn, sinh ra để hỗ trợ.

```text
Wide 16:9 landscape cinematic frame. a quiet student making shadow shapes with his hands, standing slightly behind his friends. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Truyện nói: thuật thức của Megumi, Thập chủng ảnh pháp, là một trong những thuật thức nổi tiếng nhất lịch sử…

```text
Wide 16:9 landscape cinematic frame. shadow creatures rising from a dark pool at a boy's feet: a dog, a bird, a toad. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Theo truyện, nhiều thế kỷ trước, người mang thuật thức này từng đấu ngang ngửa với người mang sức mạnh của kẻ…

```text
Wide 16:9 landscape cinematic frame. an ancient battlefield painting of two sorcerers striking each other, a shadow beast and a burst of light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Trong bóng của cậu còn ẩn một thức thần mà chưa ai từng thuần phục, mạnh đến mức triệu hồi nó giống như đặt c…

```text
Wide 16:9 landscape cinematic frame. a massive shadowy silhouette with a wheel above its head looming behind a small figure. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì Megumi hay tự kìm hãm bản thân và chưa dùng hết tiềm năng. Truyện nhiều lần nhắc rằng cậu…

```text
Wide 16:9 landscape cinematic frame. a boy looking at his own shadow, which looms much larger than he is. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Hiểu lầm tặng kèm: cấp bậc · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi tới hiểu lầm lớn nhất, Kaku tặng thêm một hiểu lầm nhỏ về cấp bậc, vì câu hỏi này xuất hiện trong b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling a small gift box out of its scarf, a note inside. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Người ta tin: cấp đặc biệt chỉ mạnh hơn cấp một một chút, giống như bậc tiếp theo trên cùng một cái thang.

```text
Wide 16:9 landscape cinematic frame. a ladder with rungs labeled 4, 3, 2, 1, and a special rung just slightly above. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Truyện nói: chú linh và chú thuật sư đều được xếp từ cấp bốn lên cấp một, rồi tới cấp đặc biệt. Truyện còn so…

```text
Wide 16:9 landscape cinematic frame. a chart pairing curse grades with everyday weapons, from a wooden bat to heavier weapons. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Cấp bốn thì một cây gậy gỗ là đủ. Cấp ba cần tới súng ngắn. Cấp hai cần súng săn. Còn cấp một, ngay cả xe tăn…

```text
Wide 16:9 landscape cinematic frame. four panels: a wooden bat, a handgun, a shotgun, and a tank looking uncertain. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Và cấp đặc biệt thì nằm hẳn ngoài thang đo đó. Truyện nói phải cần tới ném bom rải thảm mới có thể xử lý được.

```text
Wide 16:9 landscape cinematic frame. a giant shadow towering over a city, far beyond the top of a chart. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao dễ nhầm: vì chữ đặc biệt nghe như một bậc nữa trên thang. Thực ra nó giống một thang đo hoàn toàn khác…

```text
Wide 16:9 landscape cinematic frame. the owl mascot counting on the tips of its wing feathers, looking amazed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Hiểu lầm 10: Sukuna là một con quỷ

Lời: Và đây là hiểu lầm lớn nhất. Người ta tin: Sukuna, vua nguyền rủa, là một con quỷ, một chú linh từ thời xa xư…

```text
Wide 16:9 landscape cinematic frame. an ancient scroll painting of a fearsome multi-armed demon with two faces in a burning city. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Truyện nói: Sukuna vốn là một con người, một chú thuật sư sống vào thời Heian, khoảng một nghìn năm trước, kh…

```text
Wide 16:9 landscape cinematic frame. an ancient imperial capital at night with lanterns and silhouettes of robed sorcerers. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Hắn mạnh đến mức các chú thuật sư thời đó hợp sức lại cũng không thể đánh bại. Sau khi chết, hai mươi ngón ta…

```text
Wide 16:9 landscape cinematic frame. twenty withered fingers sealed in wooden boxes with paper talismans, arranged in rows. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Cái tên Sukuna còn mượn từ một nhân vật trong truyền thuyết Nhật Bản cổ, được mô tả là có hai mặt và bốn tay.…

```text
Wide 16:9 landscape cinematic frame. a faded ancient manuscript page with an ink drawing of a two-faced figure. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Vì sao dễ nhầm: vì hắn sống trong cơ thể Yuji như một chú linh, được gọi là vua nguyền rủa, và hành động khôn…

```text
Wide 16:9 landscape cinematic frame. a teenager's reflection in a puddle showing a sinister smiling face instead of his own. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là chi tiết đáng sợ nhất của truyện: con quỷ đáng sợ nhất lịch sử chú thuật hóa ra lại là một c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a mirror where its reflection looks slightly darker. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Trắc nghiệm: đúng hay sai? · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ kiểm tra xem bạn nhớ bao nhiêu. Kaku đọc năm câu, bạn trả lời đúng hay sai trong đầu trước khi Kaku công…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up two paddles, one green and one red. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Câu một: Hắc thiểm xảy ra khi chú lực chạm vào đối thủ gần như cùng lúc với cú đánh. Đáp án: đúng. Khoảng các…

```text
Wide 16:9 landscape cinematic frame. a green check mark next to a fist and a tiny stopwatch. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Câu hai: có thể học thêm một thuật thức mới nếu luyện tập đủ lâu. Đáp án: sai. Thuật thức là bẩm sinh, luyện…

```text
Wide 16:9 landscape cinematic frame. a red X next to a scroll labeled with a new technique. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Câu ba: tiết lộ thuật thức cho đối thủ có thể làm nó mạnh hơn. Đáp án: đúng. Đó là một dạng lời thề ràng buộc.

```text
Wide 16:9 landscape cinematic frame. a green check mark next to a speech bubble with a power-up arrow. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Câu bốn: chú lực đảo ngược có thể hồi sinh người đã chết. Đáp án: sai. Nó chữa thương, nhưng không đưa người…

```text
Wide 16:9 landscape cinematic frame. a red X next to an empty hourglass. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Câu năm: Sukuna sống vào thời Heian. Đáp án: đúng. Khoảng một nghìn năm trước, và khi đó hắn là một con người.

```text
Wide 16:9 landscape cinematic frame. a green check mark next to an ancient lantern-lit capital. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn đúng cả năm câu, chúc mừng, bạn đã sẵn sàng làm chú thuật sư cấp một. Còn nếu sai nhiều, đừng lo, cứ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a small gold badge on a paper certificate. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku: vì sao Jujutsu Kaisen dễ bị hiểu nhầm? · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại mười hiểu lầm, Kaku thấy chúng có ba nguyên nhân chung.

```text
Wide 16:9 landscape cinematic frame. the owl mascot arranging ten notes into three piles on a desk. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Thứ nhất, luật của thế giới được giải thích rải rác, thường giữa những trận đánh rất nhanh. Chỉ cần lơ đãng v…

```text
Wide 16:9 landscape cinematic frame. a fast-moving battle with tiny rule notes flying off in the wind. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Thứ hai, anime quá đẹp. Hiệu ứng hình ảnh mạnh khiến mọi thứ trông như chiêu cuối, dù truyện đang nói về một…

```text
Wide 16:9 landscape cinematic frame. a dazzling explosion of color with a small plain rulebook almost hidden in the corner. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Thứ ba, truyện thích lật ngược kỳ vọng. Người mạnh nhất có vết nứt, nhân vật phụ có tiềm năng khổng lồ, con q…

```text
Wide 16:9 landscape cinematic frame. a playing card flipping over to reveal the opposite image on its back. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Thêm nữa, cộng đồng fan rất đông và bàn luận rất sôi nổi. Một cách hiểu sai được lặp lại đủ nhiều lần trên mạ…

```text
Wide 16:9 landscape cinematic frame. a chain of speech bubbles repeating the same wrong note, growing larger each time. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và Kaku nghĩ đó chính là điểm hay nhất: mỗi lần xem lại, bạn lại hiểu thêm một luật mà lần trước mình đã hiểu…

```text
Wide 16:9 landscape cinematic frame. a stack of rewatched notebooks growing taller, each with more notes. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Bảng tổng hợp

Lời: Tổng hợp nhanh mười hiểu lầm. Một: Hắc thiểm là hiện tượng, không phải chiêu. Hai: chú linh cấp cao thông min…

```text
Wide 16:9 landscape cinematic frame. a summary board with ten rows, the first two lighting up. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Ba: thuật thức là bẩm sinh. Bốn: không có thuật thức vẫn có thể rất mạnh. Năm: chú lực đảo ngược rất hiếm, và…

```text
Wide 16:9 landscape cinematic frame. rows three to five lighting up on the summary board. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Sáu: lời thề ràng buộc có ở khắp nơi. Bảy: lãnh địa có cách chống. Tám: người mạnh nhất vẫn có thể bị chạm và…

```text
Wide 16:9 landscape cinematic frame. rows six to eight lighting up on the summary board. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Chín: Megumi mang một trong những thuật thức nổi tiếng nhất lịch sử. Và mười: Sukuna là con người, không phải…

```text
Wide 16:9 landscape cinematic frame. the final two rows lighting up, the last one glowing red. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: bạn từng tin hiểu lầm nào trong số này? Hoặc còn hiểu lầm nào Kaku chưa nhắc tới? Viết vào p…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a blank sticky note and a red pen toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · Kết

Lời: Video tới sẽ rất khác: Kaku không giải thích, không sửa lỗi, mà mời chính bạn bước vào một thế giới nơi yêu q…

```text
Wide 16:9 landscape cinematic frame. a quiet suburban street at night with a ghostly figure on one side and a UFO light on the other. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Bạn sẽ phải tự đưa ra lựa chọn, và Kaku sẽ tính xem bạn sống sót được bao lâu.

```text
Wide 16:9 landscape cinematic frame. a choose-your-path signpost with two arrows glowing in the dark. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất cây bút đỏ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot capping a red marker and waving in front of a board full of crossed-out notes. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hiểu lầm 1: Hắc thiểm là tuyệt chiêu

Khoảng 117 giây · cảnh s01–s11 · 1517 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết anime mùa hai, arc Shibuya, và một ít đầu arc Trò chơi tử diệt trong mùa ba.

<short pause> Câu này bạn chắc chắn đã nghe: Hắc thiểm là tuyệt chiêu mà nhân vật mạnh có thể tung ra bất cứ lúc nào. Nghe hợp lý, đúng không?

<short pause> Sai. Và đó mới chỉ là hiểu lầm đầu tiên trong mười hiểu lầm mà Kaku gom được từ bình luận, diễn đàn và chính những lần Kaku tự hiểu sai.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Với mỗi hiểu lầm, Kaku sẽ trả lời ba câu: người ta tin gì, truyện thực sự nói gì, và vì sao lại dễ hiểu nhầm đến vậy.

<short pause> Và như mọi danh sách hay, hiểu lầm lớn nhất, cũng là hiểu lầm Kaku thấy nhiều nhất, được để dành tới cuối.

<short pause> Người ta tin: Hắc thiểm là một đòn đánh đặc biệt, nhân vật mạnh có thể dùng khi cần, giống như tung một chiêu cuối.

<short pause> Truyện nói: Hắc thiểm không phải kỹ thuật, mà là một hiện tượng. Nó xảy ra khi chú lực chạm vào đối thủ chỉ trong khoảng một phần triệu giây sau cú đánh vật lý.

<short pause> Khi trùng khớp đúng khoảnh khắc đó, không gian bị bóp méo, tia sét đen lóe lên, và sức mạnh cú đánh tăng vọt. Truyện mô tả nó mạnh hơn đòn thường theo cấp số mũ.

<short pause> Không ai tạo ra Hắc thiểm theo ý muốn một cách chắc chắn. Ngay cả những chú thuật sư mạnh nhất cũng chỉ có thể tăng cơ hội, chứ không bảo đảm.

<short pause> Vì sao dễ nhầm: vì anime thể hiện nó quá ngầu, với tên gọi và hiệu ứng riêng, nên trông giống hệt một chiêu cuối trong game đối kháng.

<short pause> Chi tiết hay: người từng tạo ra Hắc thiểm được cho là hiểu chú lực ở một tầm khác. Kaku nghĩ nó giống cảm giác vào guồng của vận động viên sau một cú đánh hoàn hảo.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết anime mùa hai, arc Shibuya, và một ít đầu arc Trò chơi tử diệt trong mùa ba.

[pause] Câu này bạn chắc chắn đã nghe: Hắc thiểm là tuyệt chiêu mà nhân vật mạnh có thể tung ra bất cứ lúc nào. [curious] Nghe hợp lý, đúng không?

[pause] Sai. Và đó mới chỉ là hiểu lầm đầu tiên trong mười hiểu lầm mà Kaku gom được từ bình luận, diễn đàn và chính những lần Kaku tự hiểu sai.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Với mỗi hiểu lầm, Kaku sẽ trả lời ba câu: người ta tin gì, truyện thực sự nói gì, và vì sao lại dễ hiểu nhầm đến vậy.

[pause] Và như mọi danh sách hay, hiểu lầm lớn nhất, cũng là hiểu lầm Kaku thấy nhiều nhất, được để dành tới cuối.

[pause] Người ta tin: Hắc thiểm là một đòn đánh đặc biệt, nhân vật mạnh có thể dùng khi cần, giống như tung một chiêu cuối.

[pause] Truyện nói: Hắc thiểm không phải kỹ thuật, mà là một hiện tượng. Nó xảy ra khi chú lực chạm vào đối thủ chỉ trong khoảng một phần triệu giây sau cú đánh vật lý.

[pause] Khi trùng khớp đúng khoảnh khắc đó, không gian bị bóp méo, tia sét đen lóe lên, và sức mạnh cú đánh tăng vọt. Truyện mô tả nó mạnh hơn đòn thường theo cấp số mũ.

[pause] Không ai tạo ra Hắc thiểm theo ý muốn một cách chắc chắn. Ngay cả những chú thuật sư mạnh nhất cũng chỉ có thể tăng cơ hội, chứ không bảo đảm.

[pause] Vì sao dễ nhầm: vì anime thể hiện nó quá ngầu, với tên gọi và hiệu ứng riêng, nên trông giống hệt một chiêu cuối trong game đối kháng.

[pause] Chi tiết hay: người từng tạo ra Hắc thiểm được cho là hiểu chú lực ở một tầm khác. Kaku nghĩ nó giống cảm giác vào guồng của vận động viên sau một cú đánh hoàn hảo.
```

### c02 · Hiểu lầm 2: Chú linh là quái vật vô tri / Hiểu lầm 3: Thuật thức luyện tập mà có

Khoảng 129 giây · cảnh s12–s23 · 1676 ký tự

**Gemini**

```text
Người ta tin: chú linh chỉ là quái vật, không có suy nghĩ, chỉ biết tấn công con người.

<short pause> Truyện nói: chú linh sinh ra từ cảm xúc tiêu cực của con người, như sợ hãi, căm ghét, lo âu. Phần lớn đúng là yếu và vô tri, nhưng những chú linh cấp cao thì hoàn toàn khác.

<short pause> Có những chú linh cấp đặc biệt biết nói, biết lập kế hoạch, và còn có triết lý riêng. Một số sinh ra từ nỗi sợ thiên nhiên của loài người, như sợ núi lửa, sợ rừng, sợ biển.

<short pause> Có chú linh còn tự coi mình là loài người thật sự, vì chúng là cảm xúc thuần khiết của con người mà không có lớp vỏ giả tạo.

<short pause> Vì vậy, trong thế giới này, càng nhiều người cùng sợ một thứ, chú linh sinh ra từ nỗi sợ đó càng mạnh. Nỗi sợ tập thể là nguồn sức mạnh đáng sợ nhất.

<short pause> Vì sao dễ nhầm: những tập đầu chỉ cho thấy chú linh yếu, hình thù kỳ dị. Khán giả gắn hình ảnh đó cho mọi chú linh.

<short pause> Người ta tin: nếu chăm chỉ, chú thuật sư có thể học được thuật thức mới, giống học một chiêu mới trong võ thuật.

<short pause> Truyện nói: thuật thức bẩm sinh được khắc sẵn trong cơ thể từ khi sinh ra. Người có thì có, người không có thì không. Không thể tự học thêm một thuật thức khác.

<short pause> Luyện tập thay đổi cách dùng: mở rộng thuật thức, dùng ngược lại, hay đẩy tới mức tối đa. <short pause> Nhưng gốc rễ vẫn là thứ có sẵn từ lúc sinh ra.

<short pause> Nhiều gia tộc chú thuật truyền thuật thức theo dòng máu, và coi đó là tài sản quý nhất, đến mức đánh giá con cái theo thuật thức chúng nhận được.

<short pause> Cũng có những trường hợp đặc biệt trong truyện cho phép dùng thuật thức của người khác, nhưng đó là ngoại lệ hiếm hoi và luôn có một cái giá hay một điều kiện rất riêng.

<short pause> Vì sao dễ nhầm: vì nhân vật mạnh lên rất nhanh trong truyện. <short pause> Nhưng thứ họ học được là kỹ năng dùng chú lực, không phải thuật thức mới.
```

**ElevenLabs**

```text
Người ta tin: chú linh chỉ là quái vật, không có suy nghĩ, chỉ biết tấn công con người.

[pause] Truyện nói: chú linh sinh ra từ cảm xúc tiêu cực của con người, như sợ hãi, căm ghét, lo âu. Phần lớn đúng là yếu và vô tri, nhưng những chú linh cấp cao thì hoàn toàn khác.

[pause] Có những chú linh cấp đặc biệt biết nói, biết lập kế hoạch, và còn có triết lý riêng. Một số sinh ra từ nỗi sợ thiên nhiên của loài người, như sợ núi lửa, sợ rừng, sợ biển.

[pause] Có chú linh còn tự coi mình là loài người thật sự, vì chúng là cảm xúc thuần khiết của con người mà không có lớp vỏ giả tạo.

[pause] Vì vậy, trong thế giới này, càng nhiều người cùng sợ một thứ, chú linh sinh ra từ nỗi sợ đó càng mạnh. Nỗi sợ tập thể là nguồn sức mạnh đáng sợ nhất.

[pause] Vì sao dễ nhầm: những tập đầu chỉ cho thấy chú linh yếu, hình thù kỳ dị. Khán giả gắn hình ảnh đó cho mọi chú linh.

[pause] Người ta tin: nếu chăm chỉ, chú thuật sư có thể học được thuật thức mới, giống học một chiêu mới trong võ thuật.

[pause] Truyện nói: thuật thức bẩm sinh được khắc sẵn trong cơ thể từ khi sinh ra. Người có thì có, người không có thì không. Không thể tự học thêm một thuật thức khác.

[pause] Luyện tập thay đổi cách dùng: mở rộng thuật thức, dùng ngược lại, hay đẩy tới mức tối đa. [pause] Nhưng gốc rễ vẫn là thứ có sẵn từ lúc sinh ra.

[pause] Nhiều gia tộc chú thuật truyền thuật thức theo dòng máu, và coi đó là tài sản quý nhất, đến mức đánh giá con cái theo thuật thức chúng nhận được.

[pause] Cũng có những trường hợp đặc biệt trong truyện cho phép dùng thuật thức của người khác, nhưng đó là ngoại lệ hiếm hoi và luôn có một cái giá hay một điều kiện rất riêng.

[pause] Vì sao dễ nhầm: vì nhân vật mạnh lên rất nhanh trong truyện. [pause] Nhưng thứ họ học được là kỹ năng dùng chú lực, không phải thuật thức mới.
```

### c03 · Hiểu lầm 4: Không có thuật thức thì yếu / Hiểu lầm 5: Chú lực đảo ngược chữa được mọi thứ

Khoảng 98 giây · cảnh s24–s34 · 1275 ký tự

**Gemini**

```text
Người ta tin: nhân vật chính Yuji ban đầu yếu vì không có thuật thức riêng như các bạn.

<short pause> Truyện nói: Yuji có thể lực phi thường ngay từ đầu, chạy nhanh, đánh mạnh ở mức khiến chú thuật sư lâu năm cũng kinh ngạc.

<short pause> Cậu còn có năng khiếu đặc biệt với Hắc thiểm. Trong một trận đấu, cậu tạo ra bốn Hắc thiểm liên tiếp, cân bằng kỷ lục của một chú thuật sư kỳ cựu.

<short pause> Trong thế giới này, không có thuật thức không đồng nghĩa với yếu. Có cả những nhân vật mạnh khủng khiếp mà hầu như không dùng chú lực.

<short pause> Vì sao dễ nhầm: vì phần lớn thời lượng tập trung vào thuật thức hào nhoáng, nên thứ sức mạnh thuần túy của cơ thể dễ bị xem nhẹ.

<short pause> Người ta tin: ai dùng được chú lực đảo ngược là gần như bất tử, và có thể chữa lành cho bất kỳ ai.

<short pause> Truyện nói: chú lực đảo ngược được tạo ra bằng cách nhân hai nguồn năng lượng âm với nhau để có năng lượng dương, giống như âm nhân âm ra dương trong toán học.

<short pause> Nó rất khó học. Chỉ một số ít chú thuật sư làm được, và đa số chỉ chữa được cho chính mình.

<short pause> Chữa cho người khác còn hiếm hơn nữa. Trong trường chú thuật, có một bác sĩ nổi tiếng chính vì làm được điều đó.

<short pause> Và nó không phải phép màu: nó cần chú lực, tốn sức, và không đưa được người đã chết trở lại.

<short pause> Vì sao dễ nhầm: vì những nhân vật mạnh nhất dùng nó quá nhẹ nhàng, khiến người xem tưởng ai cũng làm được.
```

**ElevenLabs**

```text
Người ta tin: nhân vật chính Yuji ban đầu yếu vì không có thuật thức riêng như các bạn.

[pause] Truyện nói: Yuji có thể lực phi thường ngay từ đầu, chạy nhanh, đánh mạnh ở mức khiến chú thuật sư lâu năm cũng kinh ngạc.

[pause] Cậu còn có năng khiếu đặc biệt với Hắc thiểm. Trong một trận đấu, cậu tạo ra bốn Hắc thiểm liên tiếp, cân bằng kỷ lục của một chú thuật sư kỳ cựu.

[pause] Trong thế giới này, không có thuật thức không đồng nghĩa với yếu. Có cả những nhân vật mạnh khủng khiếp mà hầu như không dùng chú lực.

[pause] Vì sao dễ nhầm: vì phần lớn thời lượng tập trung vào thuật thức hào nhoáng, nên thứ sức mạnh thuần túy của cơ thể dễ bị xem nhẹ.

[pause] Người ta tin: ai dùng được chú lực đảo ngược là gần như bất tử, và có thể chữa lành cho bất kỳ ai.

[pause] Truyện nói: chú lực đảo ngược được tạo ra bằng cách nhân hai nguồn năng lượng âm với nhau để có năng lượng dương, giống như âm nhân âm ra dương trong toán học.

[pause] Nó rất khó học. Chỉ một số ít chú thuật sư làm được, và đa số chỉ chữa được cho chính mình.

[pause] Chữa cho người khác còn hiếm hơn nữa. Trong trường chú thuật, có một bác sĩ nổi tiếng chính vì làm được điều đó.

[pause] Và nó không phải phép màu: nó cần chú lực, tốn sức, và không đưa được người đã chết trở lại.

[pause] Vì sao dễ nhầm: vì những nhân vật mạnh nhất dùng nó quá nhẹ nhàng, khiến người xem tưởng ai cũng làm được.
```

### c04 · Hiểu lầm 6: Lời thề ràng buộc chỉ có trong trận lớn / Hiểu lầm 7: Lãnh địa là không thể đỡ

Khoảng 120 giây · cảnh s35–s46 · 1555 ký tự

**Gemini**

```text
Người ta tin: lời thề ràng buộc là thứ hiếm, chỉ xuất hiện trong những giao kèo lớn và kịch tính.

<short pause> Truyện nói: lời thề ràng buộc có mặt ở khắp nơi, kể cả trong những thói quen nhỏ. Tự đặt giới hạn cho mình thì được thưởng thêm sức mạnh.

<short pause> Ví dụ nổi tiếng là chú thuật sư làm việc như nhân viên văn phòng: ông tự giới hạn giờ làm, và khi phải làm thêm giờ, sức mạnh của ông tăng lên.

<short pause> Một dạng khác rất phổ biến: tiết lộ thuật thức của mình cho đối thủ. Tự làm mình bất lợi thì thuật thức được tăng sức mạnh.

<short pause> Lời thề cũng có thể được lập giữa hai người. <short pause> Nhưng phá vỡ lời thề thì sẽ phải chịu hậu quả, và hậu quả đó không phải lúc nào cũng biết trước được.

<short pause> Vì sao dễ nhầm: vì trong nhiều bộ khác, nhân vật giải thích chiêu thức chỉ để khán giả hiểu. Ở đây, việc giải thích là một phần của chiến thuật.

<short pause> <laugh> Kaku ghi chú: nên lần sau thấy nhân vật giải thích dài dòng giữa trận, đừng vội chê. Họ đang mạnh lên đấy.

<short pause> Người ta tin: đã bị kéo vào lãnh địa là thua, vì mọi đòn trong lãnh địa đều trúng một trăm phần trăm.

<short pause> Truyện nói: đòn trong lãnh địa được bảo đảm trúng, nhưng vẫn có nhiều cách chống đỡ. Có kỹ thuật tạo một vùng nhỏ quanh cơ thể để vô hiệu hóa đòn chắc chắn trúng.

<short pause> Cách mạnh nhất là mở lãnh địa của chính mình. Hai lãnh địa va chạm thì bên nào tinh xảo hơn sẽ lấn át bên kia.

<short pause> Kaku đã giải thích chi tiết luật và các cách phá lãnh địa ở video số hai của kênh. Ở đây chỉ cần nhớ: lãnh địa rất mạnh, nhưng không phải chiến thắng tự động.

<short pause> Vì sao dễ nhầm: vì lần đầu xuất hiện, lãnh địa được thể hiện như một đòn kết thúc tuyệt đối, và cảm giác đó ở lại với người xem.
```

**ElevenLabs**

```text
Người ta tin: lời thề ràng buộc là thứ hiếm, chỉ xuất hiện trong những giao kèo lớn và kịch tính.

[pause] Truyện nói: lời thề ràng buộc có mặt ở khắp nơi, kể cả trong những thói quen nhỏ. Tự đặt giới hạn cho mình thì được thưởng thêm sức mạnh.

[pause] Ví dụ nổi tiếng là chú thuật sư làm việc như nhân viên văn phòng: ông tự giới hạn giờ làm, và khi phải làm thêm giờ, sức mạnh của ông tăng lên.

[pause] Một dạng khác rất phổ biến: tiết lộ thuật thức của mình cho đối thủ. Tự làm mình bất lợi thì thuật thức được tăng sức mạnh.

[pause] Lời thề cũng có thể được lập giữa hai người. [pause] Nhưng phá vỡ lời thề thì sẽ phải chịu hậu quả, và hậu quả đó không phải lúc nào cũng biết trước được.

[pause] Vì sao dễ nhầm: vì trong nhiều bộ khác, nhân vật giải thích chiêu thức chỉ để khán giả hiểu. Ở đây, việc giải thích là một phần của chiến thuật.

[pause] [chuckles] Kaku ghi chú: nên lần sau thấy nhân vật giải thích dài dòng giữa trận, đừng vội chê. Họ đang mạnh lên đấy.

[pause] Người ta tin: đã bị kéo vào lãnh địa là thua, vì mọi đòn trong lãnh địa đều trúng một trăm phần trăm.

[pause] Truyện nói: đòn trong lãnh địa được bảo đảm trúng, nhưng vẫn có nhiều cách chống đỡ. Có kỹ thuật tạo một vùng nhỏ quanh cơ thể để vô hiệu hóa đòn chắc chắn trúng.

[pause] Cách mạnh nhất là mở lãnh địa của chính mình. Hai lãnh địa va chạm thì bên nào tinh xảo hơn sẽ lấn át bên kia.

[pause] Kaku đã giải thích chi tiết luật và các cách phá lãnh địa ở video số hai của kênh. Ở đây chỉ cần nhớ: lãnh địa rất mạnh, nhưng không phải chiến thắng tự động.

[pause] Vì sao dễ nhầm: vì lần đầu xuất hiện, lãnh địa được thể hiện như một đòn kết thúc tuyệt đối, và cảm giác đó ở lại với người xem.
```

### c05 · Hiểu lầm 8: Người mạnh nhất không thể bị chạm vào / Hiểu lầm 9: Megumi chỉ là nhân vật phụ

Khoảng 115 giây · cảnh s47–s57 · 1494 ký tự

**Gemini**

```text
Người ta tin: người được gọi là mạnh nhất có một lá chắn vô hạn, nên không gì có thể chạm vào anh ta.

<short pause> Truyện nói: lá chắn đó dựa trên khái niệm vô hạn trong toán học. Thứ gì tiến lại gần sẽ chậm dần và không bao giờ tới nơi, giống như đi mãi một nửa quãng đường còn lại.

<short pause> Nhưng lá chắn vẫn có giới hạn. Trong quá khứ, anh từng bị một người không có chú lực đâm xuyên, nhờ một vũ khí đặc biệt có thể vô hiệu hóa thuật thức.

<short pause> Sau lần đó, anh tìm cách để lá chắn luôn tự động hoạt động. <short pause> Nhưng câu chuyện đã chứng minh: không có sức mạnh nào là tuyệt đối.

<short pause> Lá chắn cũng tiêu hao chú lực và cần tính toán cực kỳ chính xác. Anh làm được là nhờ đôi mắt đặc biệt giúp nhìn thấy dòng chú lực đến từng chi tiết nhỏ.

<short pause> Vì sao dễ nhầm: vì anh gần như luôn thắng dễ dàng trong mùa một, khiến người xem nghĩ lá chắn là vô địch. Mùa hai mới cho thấy vết nứt.

<short pause> Người ta tin: Megumi, người bạn trầm tính của Yuji, chỉ là nhân vật phụ yếu hơn, sinh ra để hỗ trợ.

<short pause> Truyện nói: thuật thức của Megumi, Thập chủng ảnh pháp, là một trong những thuật thức nổi tiếng nhất lịch sử chú thuật. Cậu gọi thức thần từ bóng của mình.

<short pause> Theo truyện, nhiều thế kỷ trước, người mang thuật thức này từng đấu ngang ngửa với người mang sức mạnh của kẻ mạnh nhất hiện tại, và cả hai cùng gục ngã.

<short pause> Trong bóng của cậu còn ẩn một thức thần mà chưa ai từng thuần phục, mạnh đến mức triệu hồi nó giống như đặt cược cả mạng sống.

<short pause> Vì sao dễ nhầm: vì Megumi hay tự kìm hãm bản thân và chưa dùng hết tiềm năng. Truyện nhiều lần nhắc rằng cậu mạnh hơn mình nghĩ.
```

**ElevenLabs**

```text
Người ta tin: người được gọi là mạnh nhất có một lá chắn vô hạn, nên không gì có thể chạm vào anh ta.

[pause] Truyện nói: lá chắn đó dựa trên khái niệm vô hạn trong toán học. Thứ gì tiến lại gần sẽ chậm dần và không bao giờ tới nơi, giống như đi mãi một nửa quãng đường còn lại.

[pause] Nhưng lá chắn vẫn có giới hạn. Trong quá khứ, anh từng bị một người không có chú lực đâm xuyên, nhờ một vũ khí đặc biệt có thể vô hiệu hóa thuật thức.

[pause] Sau lần đó, anh tìm cách để lá chắn luôn tự động hoạt động. [pause] Nhưng câu chuyện đã chứng minh: không có sức mạnh nào là tuyệt đối.

[pause] Lá chắn cũng tiêu hao chú lực và cần tính toán cực kỳ chính xác. Anh làm được là nhờ đôi mắt đặc biệt giúp nhìn thấy dòng chú lực đến từng chi tiết nhỏ.

[pause] Vì sao dễ nhầm: vì anh gần như luôn thắng dễ dàng trong mùa một, khiến người xem nghĩ lá chắn là vô địch. Mùa hai mới cho thấy vết nứt.

[pause] Người ta tin: Megumi, người bạn trầm tính của Yuji, chỉ là nhân vật phụ yếu hơn, sinh ra để hỗ trợ.

[pause] Truyện nói: thuật thức của Megumi, Thập chủng ảnh pháp, là một trong những thuật thức nổi tiếng nhất lịch sử chú thuật. Cậu gọi thức thần từ bóng của mình.

[pause] Theo truyện, nhiều thế kỷ trước, người mang thuật thức này từng đấu ngang ngửa với người mang sức mạnh của kẻ mạnh nhất hiện tại, và cả hai cùng gục ngã.

[pause] Trong bóng của cậu còn ẩn một thức thần mà chưa ai từng thuần phục, mạnh đến mức triệu hồi nó giống như đặt cược cả mạng sống.

[pause] Vì sao dễ nhầm: vì Megumi hay tự kìm hãm bản thân và chưa dùng hết tiềm năng. Truyện nhiều lần nhắc rằng cậu mạnh hơn mình nghĩ.
```

### c06 · Hiểu lầm tặng kèm: cấp bậc / Hiểu lầm 10: Sukuna là một con quỷ

Khoảng 127 giây · cảnh s58–s69 · 1646 ký tự

**Gemini**

```text
<laugh> Trước khi tới hiểu lầm lớn nhất, Kaku tặng thêm một hiểu lầm nhỏ về cấp bậc, vì câu hỏi này xuất hiện trong bình luận rất nhiều.

<short pause> Người ta tin: cấp đặc biệt chỉ mạnh hơn cấp một một chút, giống như bậc tiếp theo trên cùng một cái thang.

<short pause> Truyện nói: chú linh và chú thuật sư đều được xếp từ cấp bốn lên cấp một, rồi tới cấp đặc biệt. Truyện còn so sánh sức mạnh theo vũ khí của người thường để dễ hình dung.

<short pause> Cấp bốn thì một cây gậy gỗ là đủ. Cấp ba cần tới súng ngắn. Cấp hai cần súng săn. Còn cấp một, ngay cả xe tăng cũng chưa chắc đã đủ.

<short pause> Và cấp đặc biệt thì nằm hẳn ngoài thang đo đó. Truyện nói phải cần tới ném bom rải thảm mới có thể xử lý được.

<short pause> Vì sao dễ nhầm: vì chữ đặc biệt nghe như một bậc nữa trên thang. Thực ra nó giống một thang đo hoàn toàn khác. Và số chú thuật sư cấp đặc biệt đếm được trên đầu ngón tay.

<short pause> Và đây là hiểu lầm lớn nhất. Người ta tin: Sukuna, vua nguyền rủa, là một con quỷ, một chú linh từ thời xa xưa.

<short pause> Truyện nói: Sukuna vốn là một con người, một chú thuật sư sống vào thời Heian, khoảng một nghìn năm trước, khi thế giới chú thuật ở thời kỳ hưng thịnh nhất.

<short pause> Hắn mạnh đến mức các chú thuật sư thời đó hợp sức lại cũng không thể đánh bại. Sau khi chết, hai mươi ngón tay của hắn trở thành những chú vật không thể phá hủy.

<short pause> Cái tên Sukuna còn mượn từ một nhân vật trong truyền thuyết Nhật Bản cổ, được mô tả là có hai mặt và bốn tay. Vì thế hình tượng quỷ dữ gắn chặt với hắn.

<short pause> Vì sao dễ nhầm: vì hắn sống trong cơ thể Yuji như một chú linh, được gọi là vua nguyền rủa, và hành động không có chút nhân tính nào.

<short pause> Kaku nghĩ đây là chi tiết đáng sợ nhất của truyện: con quỷ đáng sợ nhất lịch sử chú thuật hóa ra lại là một con người.
```

**ElevenLabs**

```text
[chuckles] Trước khi tới hiểu lầm lớn nhất, Kaku tặng thêm một hiểu lầm nhỏ về cấp bậc, vì câu hỏi này xuất hiện trong bình luận rất nhiều.

[pause] Người ta tin: cấp đặc biệt chỉ mạnh hơn cấp một một chút, giống như bậc tiếp theo trên cùng một cái thang.

[pause] Truyện nói: chú linh và chú thuật sư đều được xếp từ cấp bốn lên cấp một, rồi tới cấp đặc biệt. Truyện còn so sánh sức mạnh theo vũ khí của người thường để dễ hình dung.

[pause] Cấp bốn thì một cây gậy gỗ là đủ. Cấp ba cần tới súng ngắn. Cấp hai cần súng săn. Còn cấp một, ngay cả xe tăng cũng chưa chắc đã đủ.

[pause] Và cấp đặc biệt thì nằm hẳn ngoài thang đo đó. Truyện nói phải cần tới ném bom rải thảm mới có thể xử lý được.

[pause] Vì sao dễ nhầm: vì chữ đặc biệt nghe như một bậc nữa trên thang. Thực ra nó giống một thang đo hoàn toàn khác. Và số chú thuật sư cấp đặc biệt đếm được trên đầu ngón tay.

[pause] Và đây là hiểu lầm lớn nhất. Người ta tin: Sukuna, vua nguyền rủa, là một con quỷ, một chú linh từ thời xa xưa.

[pause] Truyện nói: Sukuna vốn là một con người, một chú thuật sư sống vào thời Heian, khoảng một nghìn năm trước, khi thế giới chú thuật ở thời kỳ hưng thịnh nhất.

[pause] Hắn mạnh đến mức các chú thuật sư thời đó hợp sức lại cũng không thể đánh bại. Sau khi chết, hai mươi ngón tay của hắn trở thành những chú vật không thể phá hủy.

[pause] Cái tên Sukuna còn mượn từ một nhân vật trong truyền thuyết Nhật Bản cổ, được mô tả là có hai mặt và bốn tay. Vì thế hình tượng quỷ dữ gắn chặt với hắn.

[pause] Vì sao dễ nhầm: vì hắn sống trong cơ thể Yuji như một chú linh, được gọi là vua nguyền rủa, và hành động không có chút nhân tính nào.

[pause] Kaku nghĩ đây là chi tiết đáng sợ nhất của truyện: con quỷ đáng sợ nhất lịch sử chú thuật hóa ra lại là một con người.
```

### c07 · Trắc nghiệm: đúng hay sai? / Góc nhìn của Kaku: vì sao Jujutsu Kaisen dễ bị hiểu nhầm?

Khoảng 123 giây · cảnh s70–s82 · 1600 ký tự

**Gemini**

```text
Giờ kiểm tra xem bạn nhớ bao nhiêu. <laugh> Kaku đọc năm câu, bạn trả lời đúng hay sai trong đầu trước khi Kaku công bố nhé.

<short pause> Câu một: Hắc thiểm xảy ra khi chú lực chạm vào đối thủ gần như cùng lúc với cú đánh. Đáp án: đúng. Khoảng cách chỉ khoảng một phần triệu giây.

<short pause> Câu hai: có thể học thêm một thuật thức mới nếu luyện tập đủ lâu. Đáp án: sai. Thuật thức là bẩm sinh, luyện tập chỉ mở rộng cách dùng.

<short pause> Câu ba: tiết lộ thuật thức cho đối thủ có thể làm nó mạnh hơn. Đáp án: đúng. Đó là một dạng lời thề ràng buộc.

<short pause> Câu bốn: chú lực đảo ngược có thể hồi sinh người đã chết. Đáp án: sai. Nó chữa thương, nhưng không đưa người chết trở lại.

<short pause> Câu năm: Sukuna sống vào thời Heian. Đáp án: đúng. Khoảng một nghìn năm trước, và khi đó hắn là một con người.

<short pause> Nếu bạn đúng cả năm câu, chúc mừng, bạn đã sẵn sàng làm chú thuật sư cấp một. Còn nếu sai nhiều, đừng lo, cứ xem lại video này nhé.

<short pause> Nhìn lại mười hiểu lầm, Kaku thấy chúng có ba nguyên nhân chung.

<short pause> Thứ nhất, luật của thế giới được giải thích rải rác, thường giữa những trận đánh rất nhanh. Chỉ cần lơ đãng vài giây là bỏ lỡ một luật quan trọng.

<short pause> Thứ hai, anime quá đẹp. Hiệu ứng hình ảnh mạnh khiến mọi thứ trông như chiêu cuối, dù truyện đang nói về một hiện tượng hay một giới hạn.

<short pause> Thứ ba, truyện thích lật ngược kỳ vọng. Người mạnh nhất có vết nứt, nhân vật phụ có tiềm năng khổng lồ, con quỷ hóa ra là người.

<short pause> Thêm nữa, cộng đồng fan rất đông và bàn luận rất sôi nổi. Một cách hiểu sai được lặp lại đủ nhiều lần trên mạng thì dần dần được coi như sự thật.

<short pause> Và Kaku nghĩ đó chính là điểm hay nhất: mỗi lần xem lại, bạn lại hiểu thêm một luật mà lần trước mình đã hiểu sai.
```

**ElevenLabs**

```text
Giờ kiểm tra xem bạn nhớ bao nhiêu. [chuckles] Kaku đọc năm câu, bạn trả lời đúng hay sai trong đầu trước khi Kaku công bố nhé.

[pause] Câu một: Hắc thiểm xảy ra khi chú lực chạm vào đối thủ gần như cùng lúc với cú đánh. Đáp án: đúng. Khoảng cách chỉ khoảng một phần triệu giây.

[pause] Câu hai: có thể học thêm một thuật thức mới nếu luyện tập đủ lâu. Đáp án: sai. Thuật thức là bẩm sinh, luyện tập chỉ mở rộng cách dùng.

[pause] Câu ba: tiết lộ thuật thức cho đối thủ có thể làm nó mạnh hơn. Đáp án: đúng. Đó là một dạng lời thề ràng buộc.

[pause] Câu bốn: chú lực đảo ngược có thể hồi sinh người đã chết. Đáp án: sai. Nó chữa thương, nhưng không đưa người chết trở lại.

[pause] Câu năm: Sukuna sống vào thời Heian. Đáp án: đúng. Khoảng một nghìn năm trước, và khi đó hắn là một con người.

[pause] Nếu bạn đúng cả năm câu, chúc mừng, bạn đã sẵn sàng làm chú thuật sư cấp một. Còn nếu sai nhiều, đừng lo, cứ xem lại video này nhé.

[pause] Nhìn lại mười hiểu lầm, Kaku thấy chúng có ba nguyên nhân chung.

[pause] Thứ nhất, luật của thế giới được giải thích rải rác, thường giữa những trận đánh rất nhanh. Chỉ cần lơ đãng vài giây là bỏ lỡ một luật quan trọng.

[pause] Thứ hai, anime quá đẹp. Hiệu ứng hình ảnh mạnh khiến mọi thứ trông như chiêu cuối, dù truyện đang nói về một hiện tượng hay một giới hạn.

[pause] Thứ ba, truyện thích lật ngược kỳ vọng. Người mạnh nhất có vết nứt, nhân vật phụ có tiềm năng khổng lồ, con quỷ hóa ra là người.

[pause] Thêm nữa, cộng đồng fan rất đông và bàn luận rất sôi nổi. Một cách hiểu sai được lặp lại đủ nhiều lần trên mạng thì dần dần được coi như sự thật.

[pause] Và Kaku nghĩ đó chính là điểm hay nhất: mỗi lần xem lại, bạn lại hiểu thêm một luật mà lần trước mình đã hiểu sai.
```

### c08 · Bảng tổng hợp / Kết

Khoảng 73 giây · cảnh s83–s90 · 950 ký tự

**Gemini**

```text
Tổng hợp nhanh mười hiểu lầm. Một: Hắc thiểm là hiện tượng, không phải chiêu. Hai: chú linh cấp cao thông minh và có triết lý.

<short pause> Ba: thuật thức là bẩm sinh. Bốn: không có thuật thức vẫn có thể rất mạnh. Năm: chú lực đảo ngược rất hiếm, và chữa cho người khác còn hiếm hơn.

<short pause> Sáu: lời thề ràng buộc có ở khắp nơi. Bảy: lãnh địa có cách chống. Tám: người mạnh nhất vẫn có thể bị chạm vào.

<short pause> Chín: Megumi mang một trong những thuật thức nổi tiếng nhất lịch sử. Và mười: Sukuna là con người, không phải quỷ.

<short pause> Câu hỏi cho bạn: bạn từng tin hiểu lầm nào trong số này? <laugh> Hoặc còn hiểu lầm nào Kaku chưa nhắc tới? Viết vào phần bình luận, biết đâu sẽ có phần hai.

<short pause> Video tới sẽ rất khác: Kaku không giải thích, không sửa lỗi, mà mời chính bạn bước vào một thế giới nơi yêu quái và người ngoài hành tinh cùng tồn tại.

<short pause> Bạn sẽ phải tự đưa ra lựa chọn, và Kaku sẽ tính xem bạn sống sót được bao lâu.

<short pause> Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất cây bút đỏ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tổng hợp nhanh mười hiểu lầm. Một: Hắc thiểm là hiện tượng, không phải chiêu. Hai: chú linh cấp cao thông minh và có triết lý.

[pause] Ba: thuật thức là bẩm sinh. Bốn: không có thuật thức vẫn có thể rất mạnh. Năm: chú lực đảo ngược rất hiếm, và chữa cho người khác còn hiếm hơn.

[pause] Sáu: lời thề ràng buộc có ở khắp nơi. Bảy: lãnh địa có cách chống. Tám: người mạnh nhất vẫn có thể bị chạm vào.

[pause] Chín: Megumi mang một trong những thuật thức nổi tiếng nhất lịch sử. Và mười: Sukuna là con người, không phải quỷ.

[pause] [curious] Câu hỏi cho bạn: bạn từng tin hiểu lầm nào trong số này? [chuckles] Hoặc còn hiểu lầm nào Kaku chưa nhắc tới? Viết vào phần bình luận, biết đâu sẽ có phần hai.

[pause] Video tới sẽ rất khác: Kaku không giải thích, không sửa lỗi, mà mời chính bạn bước vào một thế giới nơi yêu quái và người ngoài hành tinh cùng tồn tại.

[pause] Bạn sẽ phải tự đưa ra lựa chọn, và Kaku sẽ tính xem bạn sống sót được bao lâu.

[pause] Nếu thấy video hữu ích, hãy đăng ký kênh. Kaku cất cây bút đỏ đây, hẹn gặp lại!
```
