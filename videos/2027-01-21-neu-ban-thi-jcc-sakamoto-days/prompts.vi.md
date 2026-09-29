# Bộ prompt · Sakamoto Days: Nếu bạn dự kỳ thi sát thủ JCC, bạn sống sót tới vòng nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 86 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
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

Lời: Video có spoiler nhẹ Sakamoto Days mùa một. Và đây là một kịch bản giả định của Kaku, lấy cảm hứng từ arc thi…

```text
Wide 16:9 landscape cinematic frame. a sealed envelope with a wax seal lying on a doormat in the morning light, wide establishing shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Giả sử một sáng thức dậy, bạn thấy một lá thư dưới cửa. Trong đó chỉ có một dòng: bạn đã được mời dự kỳ thi c…

```text
Wide 16:9 landscape cinematic frame. a hand opening an elegant black envelope revealing a single card with an academy crest, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Bạn có đúng một ngày để chuẩn bị. Bạn có thể ngủ thật sớm, xem lại vài tập Sakamoto Days để học hỏi, hoặc… ho…

```text
Wide 16:9 landscape cinematic frame. a person pacing nervously in a small bedroom at night, then watching a show on a laptop, then finally asleep, three small panels, humorous storyboard. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Bạn không phải sát thủ. Bạn chỉ là một người bình thường, có lẽ hơi giỏi thể thao, hoặc hơi giỏi toán. Nhưng…

```text
Wide 16:9 landscape cinematic frame. an ordinary young person sitting on a bed staring at the letter with wide eyes, a school bag and a game controller nearby, medium shot, morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Trong Sakamoto Days, JCC là nơi đào tạo những sát thủ giỏi nhất, và chính Sakamoto từng học ở đó. Mùa một có…

```text
Wide 16:9 landscape cinematic frame. a grand academy building with dark towers behind tall iron gates, a line of nervous candidates waiting outside, wide shot, dramatic dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku dẫn bạn đi qua kỳ thi JCC từng vòng một. Ở mỗi vòng, bạn phải chọn.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny exam proctor's armband, holding a clipboard and a whistle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Hãy lấy một tờ giấy và ghi lại lựa chọn của mình ở mỗi vòng. Cuối video, Kaku sẽ tính điểm sống sót cho bạn.

```text
Wide 16:9 landscape cinematic frame. a blank scorecard with five empty rows and a pencil, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Luật chấm điểm của Kaku

Lời: Bạn bắt đầu với mười điểm sống sót. Mỗi lựa chọn có thể cộng hoặc trừ điểm. Về không là bị loại, và trong kỳ…

```text
Wide 16:9 landscape cinematic frame. a large glowing number ten on a scoreboard with small plus and minus signs floating around it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ba nguyên tắc này sẽ quay lại ở mọi vòng. Nếu bạn phân vân, hãy tự hỏi: Sakamoto sẽ làm gì? Câu trả lời thườn…

```text
Wide 16:9 landscape cinematic frame. a small sticky note on a mirror reading a simple question with a round smiling face doodle, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Kaku chấm theo ba nguyên tắc rút ra từ Sakamoto Days. Một: quan sát quan trọng hơn sức mạnh. Hai: mọi đồ vật…

```text
Wide 16:9 landscape cinematic frame. three small signs pinned on a board: an eye icon, a spoon icon and a crossed-out knife icon, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và một luật phụ: nếu bạn làm Kaku bật cười ở một lựa chọn nào đó, Kaku không cộng điểm đâu, nhưng Kaku sẽ nhớ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot trying hard to keep a straight face while holding a scorecard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Nhớ nhé: trong thế giới Sakamoto Days, những người mạnh nhất thường là những người bình tĩnh nhất, và buồn cư…

```text
Wide 16:9 landscape cinematic frame. a relaxed round shopkeeper silhouette sipping tea calmly in the middle of a chaotic scene, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Vòng 0: chọn vũ khí

Lời: Trước khi vào trường thi, giám thị cho bạn chọn một món mang theo. Có ba lựa chọn trên bàn.

```text
Wide 16:9 landscape cinematic frame. a table with three items under spotlights: a sleek knife in a sheath, a compact handgun in a case, and a simple canvas shopping bag with groceries, still life, dramatic light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Lựa chọn A: một con dao chuyên nghiệp. Trông nguy hiểm, nhưng bạn chưa từng dùng dao ngoài việc gọt táo.

```text
Wide 16:9 landscape cinematic frame. a professional knife resting on a folded cloth beside a single peeled apple, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Lựa chọn B: một khẩu súng. Mạnh, nhưng bạn chưa bắn bao giờ, và tiếng súng sẽ thu hút mọi thí sinh khác về ph…

```text
Wide 16:9 landscape cinematic frame. a compact handgun case with a warning sticker, a map of a building with many red arrows pointing to one spot, parchment overlay, tense light. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Giám thị nhìn bạn một lúc lâu khi bạn chọn túi đồ đi chợ. Bạn không biết đó là ánh mắt thương hại hay ánh mắt…

```text
Wide 16:9 landscape cinematic frame. a stern proctor raising one eyebrow at a candidate holding a shopping bag, humorous close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Lựa chọn C: một túi đồ đi chợ, gồm ô, băng keo, một chai nước và một gói bánh. Trông vô dụng.

```text
Wide 16:9 landscape cinematic frame. an ordinary shopping bag with an umbrella handle, a roll of tape and a water bottle peeking out, close-up, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nếu bạn chọn A hoặc B, trừ một điểm: vũ khí bạn không biết dùng còn nguy hiểm cho chính bạn hơn cho đối thủ.…

```text
Wide 16:9 landscape cinematic frame. a round shopkeeper silhouette giving an approving thumbs up from behind a store counter, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Kaku giải thích: trong Sakamoto Days, những đồ vật tầm thường lại linh hoạt nhất. Ô là khiên, là gậy, là móc.…

```text
Wide 16:9 landscape cinematic frame. an umbrella shielding against flying debris, tape wrapped around a door handle, a snack being eaten, three small panels, parchment storyboard. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Vòng 1: tòa nhà bẫy

Lời: Bạn nhìn quanh sảnh. Có hai mươi thí sinh khác, ai cũng trông nguy hiểm hơn bạn. Một người đang mài dao, một…

```text
Wide 16:9 landscape cinematic frame. a crowded lobby of diverse intimidating candidates, one sharpening a blade, one shadowboxing, one calmly eating instant noodles, wide shot, humorous tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Vòng một: bạn bị đưa vào một tòa nhà năm tầng. Nhiệm vụ: lên tới sân thượng trong ba mươi phút. Trong tòa nhà…

```text
Wide 16:9 landscape cinematic frame. a tall abandoned office building at dusk with a helicopter pad on the roof, a countdown of thirty minutes projected on its wall, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Bạn đứng ở sảnh. Trước mặt có thang máy, cầu thang bộ, và một ống thông gió mở toang.

```text
Wide 16:9 landscape cinematic frame. a dim lobby with an elevator with flickering lights, a stairwell door, and an open ventilation duct, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Lựa chọn A: đi thang máy cho nhanh. Lựa chọn B: đi cầu thang bộ, chậm nhưng nhìn thấy mọi thứ. Lựa chọn C: ch…

```text
Wide 16:9 landscape cinematic frame. three labeled arrows drawn on a building cross-section diagram pointing to the elevator shaft, the stairs, and the ventilation duct, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Kaku ghi chú thêm: trong phim hành động, thang máy luôn là nơi xảy ra chuyện. Nếu bạn xem đủ nhiều phim, bạn…

```text
Wide 16:9 landscape cinematic frame. a movie poster collage of dramatic elevator scenes pinned on a corkboard, close-up, humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nếu bạn chọn thang máy: trừ ba điểm. Trong một kỳ thi sát thủ, thang máy là cái hộp kín mà ai cũng biết bạn s…

```text
Wide 16:9 landscape cinematic frame. a stuck elevator with flickering lights and a small figure climbing out through the ceiling hatch, humorous tense close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nếu bạn chọn cầu thang bộ: cộng một điểm. Chậm hơn, nhưng bạn nhìn thấy dây bẫy căng ngang bậc thứ ba tầng ha…

```text
Wide 16:9 landscape cinematic frame. a thin nearly invisible tripwire stretched across a stair step, a shoe stopping just before it, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Trên đường bò qua ống thông gió, bạn còn nghe được hai thí sinh khác thì thầm kế hoạch phục kích ở tầng bốn.…

```text
Wide 16:9 landscape cinematic frame. a person inside a ventilation duct listening through a grate to two shadowy figures whispering below, close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nếu bạn chọn ống thông gió: cộng hai điểm, nhưng mất thêm năm phút vì bạn bị kẹt ở một khúc quanh. May là có…

```text
Wide 16:9 landscape cinematic frame. a person squeezed inside a narrow ventilation duct eating a snack while stuck at a bend, humorous close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và nếu bạn tự hỏi người ăn mì là ai: trong Sakamoto Days, người bình tĩnh nhất phòng thường là người nguy hiể…

```text
Wide 16:9 landscape cinematic frame. a calm candidate slurping noodles while everyone else gives them a wide berth, close-up, humorous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong arc JCC thật, những thí sinh sống sót thường không phải người nhanh nhất, mà là người nhì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peering through a magnifying glass at a tiny tripwire on a diagram. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Vòng phụ: kiểm tra quan sát

Lời: Giữa cầu thang tầng hai, một giám thị chặn bạn lại. Bà ta nói: trước khi đi tiếp, trả lời ba câu hỏi về căn p…

```text
Wide 16:9 landscape cinematic frame. a strict proctor with a clipboard blocking a stairwell landing, a candidate stopping in surprise, medium shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Kaku sẽ cho bạn xem căn phòng đó trong năm giây. Hãy nhìn thật kỹ. Nếu cần, bạn có thể tạm dừng video.

```text
Wide 16:9 landscape cinematic frame. a small office room with a clock on the wall showing ten past three, two doors, a potted plant, a red umbrella in a stand and three chairs, wide shot, even light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Câu một: căn phòng có mấy cửa ra vào? Câu hai: đồng hồ trên tường chỉ mấy giờ? Câu ba: trong phòng có bao nhi…

```text
Wide 16:9 landscape cinematic frame. three question cards laid on a desk with numbers one two three, a pencil beside them, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Đáp án: hai cửa, ba giờ mười phút, và ba chiếc ghế. Mỗi câu đúng, cộng một điểm vào tờ giấy của bạn.

```text
Wide 16:9 landscape cinematic frame. an answer sheet with three check marks in amber ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Nếu bạn trả lời đúng cả ba, Kaku rất ấn tượng. Trong thế giới sát thủ, người để ý số lối thoát và thời gian l…

```text
Wide 16:9 landscape cinematic frame. a candidate glancing at exits and a wall clock while walking calmly through a room, medium shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thì nhớ được chiếc ô, còn đồng hồ và ghế thì quên sạch. Có lẽ vì Kaku chỉ để ý những thứ có thể làm vũ k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly pointing at a red umbrella while ignoring a clock and chairs behind it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Vòng 2: gặp thí sinh khác

Lời: Hành lang tầng ba im lặng một cách đáng ngờ. Những vết trầy trên tường cho thấy đã có một trận đánh ở đây vài…

```text
Wide 16:9 landscape cinematic frame. a long quiet corridor with fresh scratch marks on the walls and a fallen fire extinguisher, wide shot, cold eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Tầng ba. Bạn gặp một thí sinh khác, đang bị thương ở chân và ngồi dựa tường. Người đó nhìn bạn, không nói gì.

```text
Wide 16:9 landscape cinematic frame. an injured candidate sitting against a corridor wall holding their ankle, looking up at the viewer warily, medium shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Lựa chọn A: tấn công để loại một đối thủ. Lựa chọn B: bỏ qua, đi tiếp. Lựa chọn C: dùng băng keo trong túi để…

```text
Wide 16:9 landscape cinematic frame. three small icons on a card: a fist, a walking arrow, and a roll of tape with a heart, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Bài học ở đây: trong một kỳ thi sát thủ, thứ trông yếu nhất có thể là cái bẫy. Người giỏi quan sát sẽ để ý rằ…

```text
Wide 16:9 landscape cinematic frame. a close-up of spotless shoes of a supposedly injured person on a dusty floor, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nếu bạn tấn công: trừ ba điểm. Hóa ra người đó giả vờ bị thương để dụ những kẻ hiếu chiến. Bạn bị phản đòn, v…

```text
Wide 16:9 landscape cinematic frame. a supposedly injured candidate suddenly springing up and flipping an attacker onto the floor, dynamic humorous shot. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nếu bạn bỏ qua: không cộng không trừ. An toàn, nhưng bạn mất một cơ hội.

```text
Wide 16:9 landscape cinematic frame. a person walking away down a corridor while the injured candidate watches silently, wide shot, neutral light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và bạn còn nhận ra người đó chính là người đã giả vờ bị thương để thử lòng mọi người. Họ nói: bạn là người đầ…

```text
Wide 16:9 landscape cinematic frame. the candidate smiling warmly and standing up easily, revealing no injury at all, the other candidate laughing in surprise, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Nếu bạn giúp: cộng ba điểm. Người đó hóa ra rất giỏi đọc bản đồ tòa nhà và chỉ cho bạn lối tắt lên sân thượng…

```text
Wide 16:9 landscape cinematic frame. two candidates walking together, one leaning on the other's shoulder, the second pointing at a building map on the wall, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Kaku giải thích: đây chính là tinh thần của cửa hàng Sakamoto. Shin, Lu, Heisuke đều từng là người lạ, thậm c…

```text
Wide 16:9 landscape cinematic frame. a small store counter with several mismatched mugs lined up, each with a different doodle, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Vòng 3: bài kiểm tra của giám khảo

Lời: Gió trên sân thượng rất mạnh. Bạn còn ba mươi giây trong tổng thời gian, và toàn thân mỏi nhừ sau năm tầng lầ…

```text
Wide 16:9 landscape cinematic frame. a windswept rooftop at sunset with loose papers flying, a tired candidate catching their breath, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Bạn lên tới sân thượng. Nhưng chưa xong. Một giám khảo đứng chờ, một sát thủ chuyên nghiệp mặc vest, mỉm cười…

```text
Wide 16:9 landscape cinematic frame. a calm smiling examiner in a sharp suit standing on a windy rooftop at sunset, city skyline behind, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku đoán nhiều bạn sẽ muốn dùng khẩu súng ở đây, nếu đã chọn nó ở vòng không. Nhưng giám khảo đã tính trước:…

```text
Wide 16:9 landscape cinematic frame. an empty handgun case lying on the rooftop floor, the examiner calmly holding up a single finger as a warning, medium shot, sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Giám khảo nhanh hơn bạn rất nhiều. Lao vào trực diện thì chắc chắn thất bại.

```text
Wide 16:9 landscape cinematic frame. a blurred figure effortlessly sidestepping a lunging candidate, dynamic wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Lựa chọn A: lao vào liên tục cho tới khi hết sức. Lựa chọn B: đứng yên quan sát cách giám khảo di chuyển. Lựa…

```text
Wide 16:9 landscape cinematic frame. a tactical sketch on parchment showing three approaches: repeated arrows, a watching eye, and an umbrella with a thrown bottle, amber ink. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nếu bạn lao vào: trừ hai điểm, bạn kiệt sức sau hai mươi giây.

```text
Wide 16:9 landscape cinematic frame. a candidate on their knees panting on the rooftop while the examiner stands calmly, medium shot, humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nếu bạn quan sát rồi mới dùng ô và chai nước, Kaku cho phép bạn cộng cả hai điểm. Quan sát trước, hành động s…

```text
Wide 16:9 landscape cinematic frame. a simple formula drawn on parchment: an eye icon plus an umbrella icon equals a star, amber ink. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nếu bạn quan sát: cộng một điểm. Bạn nhận ra giám khảo luôn né sang trái. Nhưng biết thì biết, bạn vẫn chưa đ…

```text
Wide 16:9 landscape cinematic frame. a close-up of a candidate's focused eyes tracking a pattern of movement drawn as arrows, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nếu bạn dùng ô và chai nước: cộng bốn điểm. Giám khảo quay đầu theo tiếng động đúng một khoảnh khắc, và đầu n…

```text
Wide 16:9 landscape cinematic frame. an open umbrella blocking view, a water bottle flying to the side, and a fingertip just touching a suit sleeve, dynamic close-up, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: giám khảo không đánh giá bạn mạnh cỡ nào. Họ đánh giá bạn có biết dùng những gì mình có hay khô…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a small umbrella icon with a star next to it on the scorecard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Biến cố: kẻ lạ đột nhập

Lời: Giám khảo lập tức thay đổi nét mặt. Nụ cười biến mất. Lần đầu tiên bạn thấy một sát thủ chuyên nghiệp nghiêm…

```text
Wide 16:9 landscape cinematic frame. a close-up of the examiner's face turning cold and focused under flashing red alarm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Ngay lúc đó, còi báo động vang lên. Một nhóm kẻ lạ mặt đột nhập kỳ thi. Kaku lấy cảm hứng từ việc arc JCC tro…

```text
Wide 16:9 landscape cinematic frame. red alarm lights flashing across the rooftop as shadowy figures appear on the stairwell door, wide shot, tense red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Lựa chọn A: chạy trốn một mình. Lựa chọn B: đuổi theo kẻ lạ để lập công. Lựa chọn C: đưa người bạn bị thương…

```text
Wide 16:9 landscape cinematic frame. three choice cards fanned out: a running figure, a chasing figure, and two figures helping each other, parchment illustration. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Nếu bạn chạy một mình: trừ hai điểm. Bạn thoát, nhưng giám khảo ghi nhận bạn bỏ lại đồng đội.

```text
Wide 16:9 landscape cinematic frame. an examiner writing a note on a clipboard while watching a lone figure run away in the distance, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Trong Sakamoto Days, những thí sinh liều lĩnh thường được cứu bởi người khác. Nhưng trong kịch bản của Kaku,…

```text
Wide 16:9 landscape cinematic frame. an empty stairwell with a single abandoned grocery bag on a step, eerie quiet light, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Nếu bạn đuổi theo: trừ ba điểm. Kẻ lạ là sát thủ thật, và bạn chỉ là thí sinh. Dũng cảm nhưng liều lĩnh.

```text
Wide 16:9 landscape cinematic frame. a candidate chasing into a dark stairwell toward looming silhouettes, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Biết nhờ người đúng lúc không phải là yếu. Ngay cả Sakamoto, người mạnh nhất, cũng dựa vào Shin, Lu, Heisuke…

```text
Wide 16:9 landscape cinematic frame. a small team of silhouettes standing together in front of a convenience store at night, warm light spilling from the doorway, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Nếu bạn đưa bạn xuống và báo giám khảo: cộng ba điểm. Bạn biết giới hạn của mình, và biết lúc nào nên nhường…

```text
Wide 16:9 landscape cinematic frame. two candidates reaching a safe checkpoint where a calm examiner nods and steps past them toward danger, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Kết quả: bạn sống sót tới đâu?

Lời: Nhớ cộng cả ba câu hỏi ở vòng phụ, và lượt cộng thêm nếu bạn quan sát trước khi dùng ô ở vòng ba.

```text
Wide 16:9 landscape cinematic frame. a scorecard with a small bonus star drawn next to the third round row, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Giờ cộng điểm của bạn. Nhớ, bạn bắt đầu với mười điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard with numbers being tallied by a pencil, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Dưới năm điểm: bạn bị loại ở vòng một hoặc hai. Đừng buồn, bạn vẫn có thể về làm nhân viên cửa hàng tiện lợi.…

```text
Wide 16:9 landscape cinematic frame. a person in a convenience store apron stocking shelves, looking relieved, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Và nếu bạn bị loại, đừng buồn: nhiều nhân vật mạnh trong truyện cũng từng trượt kỳ thi đầu tiên của mình.

```text
Wide 16:9 landscape cinematic frame. a crumpled exam result slip being smoothed flat on a desk by a determined hand, close-up, soft hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Từ năm tới mười bốn điểm: bạn vào được vòng ba nhưng chưa đỗ. Giám khảo ghi tên bạn vào danh sách đáng chú ý.

```text
Wide 16:9 landscape cinematic frame. an examiner's notebook with a name circled in amber ink among many others, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Từ mười lăm tới hai mươi hai điểm: bạn đỗ JCC. Chúc mừng, và cũng chia buồn, vì học viện này còn đáng sợ hơn…

```text
Wide 16:9 landscape cinematic frame. a candidate receiving an academy badge from an examiner at the gate at dawn, wide shot, bright but ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Từ hai mươi ba điểm trở lên: bạn chọn gần như hoàn hảo. Một thành viên Order đã để mắt tới bạn. Và ở cuối con…

```text
Wide 16:9 landscape cinematic frame. an elite silhouette watching from a distant rooftop, and at street level a round shopkeeper smiling from his store doorway, split composition, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Điểm tối đa trong kịch bản này là hai mươi tám. Nếu bạn đạt được, hãy khoe trong bình luận. Kaku muốn biết có…

```text
Wide 16:9 landscape cinematic frame. a golden trophy with a small umbrella engraved on it on a pedestal, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Nếu là nhân vật trong truyện

Lời: Nếu Shin dự kỳ thi này, cậu sẽ đọc được suy nghĩ của giám khảo và biết trước họ né sang đâu. Vòng ba với Shin…

```text
Wide 16:9 landscape cinematic frame. a young man with faint light rings around his head smirking at an examiner whose thoughts float as chaotic doodles, humorous medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nếu là Lu, cô sẽ đánh thẳng từ tầng một lên sân thượng, lạc đường hai lần, và vẫn tới nơi đúng giờ nhờ may mắ…

```text
Wide 16:9 landscape cinematic frame. a young woman in a martial arts stance bursting through a door on the wrong floor, humorous dynamic shot, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Còn nếu là Nagumo, người bạn cũ hay cười của Sakamoto, thì chắc anh ta sẽ cải trang thành giám khảo, và chẳng…

```text
Wide 16:9 landscape cinematic frame. two identical smiling examiners standing side by side on a rooftop, one winking at the viewer, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nếu là Heisuke, anh sẽ ngắm từ tòa nhà đối diện, và chú vẹt của anh sẽ là thí sinh đầu tiên chạm vào giám khả…

```text
Wide 16:9 landscape cinematic frame. a colorful parrot landing on an examiner's shoulder on a rooftop while a sniper silhouette cheers from a distant window, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu là Sakamoto, ông sẽ đi cầu thang bộ, giúp người bị thương, chạm vào giám khảo bằng một cây bút bi, và về…

```text
Wide 16:9 landscape cinematic frame. a round shopkeeper walking home at dusk carrying a grocery bag, a ballpoint pen tucked behind his ear, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và nếu là Kaku, Kaku sẽ chọn túi đồ đi chợ, đi cầu thang bộ, giúp người bị thương, rồi… bị kẹt ở vòng ba vì k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot flapping helplessly while an examiner gently holds it at arm's length. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Góc nhìn của Kaku: kỳ thi dạy gì

Lời: Và không lựa chọn điểm cao nào đòi hỏi bạn phải mạnh. Chúng chỉ đòi hỏi bạn bình tĩnh, để ý, và tử tế. Kaku n…

```text
Wide 16:9 landscape cinematic frame. a calm person sitting on a bench observing a busy street, a small umbrella leaning beside them, wide shot, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Nhìn lại kịch bản, những lựa chọn được điểm cao đều giống nhau: quan sát trước khi hành động, dùng những gì m…

```text
Wide 16:9 landscape cinematic frame. three glowing icons on parchment: an eye, an umbrella and two clasped hands, arranged in a triangle, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Đó cũng là lý do Sakamoto Days được yêu thích: một bộ truyện về sát thủ, nhưng nhân vật chính mạnh nhất lại l…

```text
Wide 16:9 landscape cinematic frame. a family of three silhouettes walking hand in hand along a riverside at sunset, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Nhưng những nguyên tắc thì dùng được ngoài đời: quan sát kỹ, dùng những gì mình có, và giúp người bên cạnh. C…

```text
Wide 16:9 landscape cinematic frame. a student at a desk in a quiet exam hall, calmly reading the question twice before writing, close-up, soft daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Kaku nhắc lại: đây là một kịch bản giả định để vui. Ngoài đời, không có trường sát thủ nào, và bạo lực không…

```text
Wide 16:9 landscape cinematic frame. a small note pinned to the scorecard reading just for fun, with a smiley face, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · Kết

Lời: Nếu nhiều bạn thích kiểu video này, Kaku sẽ soạn thêm những kỳ thi khác: thi thợ săn Hunter, thi vào học viện…

```text
Wide 16:9 landscape cinematic frame. three envelopes with different crests fanned out on a desk: a hunter emblem, a magic wand emblem and a pirate flag, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Bạn được bao nhiêu điểm? Và bạn chọn gì ở vòng không? Kaku đoán phần lớn mọi người sẽ chọn khẩu súng, cho tới…

```text
Wide 16:9 landscape cinematic frame. a comment box drawn on parchment filled with small score numbers and umbrella doodles, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Video tiếp theo, Kaku mở cửa nhập môn cho một bộ anime đặc biệt: Gachiakuta, nơi rác thải của người giàu trở…

```text
Wide 16:9 landscape cinematic frame. a towering mountain of discarded objects under a grey sky, a lone figure standing on top holding a glowing piece of junk, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích kiểu video tự chọn đường đi như thế này, hãy đăng ký kênh để Kaku soạn thêm nhiều kỳ thi nữa. K…

```text
Wide 16:9 landscape cinematic frame. the owl mascot blowing its tiny whistle to end the exam and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Luật chấm điểm của Kaku

Khoảng 145 giây · cảnh s01–s12 · 1884 ký tự

**Gemini**

```text
Video có spoiler nhẹ Sakamoto Days mùa một. Và đây là một kịch bản giả định của Kaku, lấy cảm hứng từ arc thi JCC, không phải nội dung chính thức. Nghề sát thủ là hư cấu, và video không cổ vũ bạo lực.

<short pause> Giả sử một sáng thức dậy, bạn thấy một lá thư dưới cửa. Trong đó chỉ có một dòng: bạn đã được mời dự kỳ thi chuyển trường vào JCC, học viện đào tạo sát thủ danh giá nhất.

<short pause> Bạn có đúng một ngày để chuẩn bị. Bạn có thể ngủ thật sớm, xem lại vài tập Sakamoto Days để học hỏi, hoặc… hoảng loạn. Kaku khuyên chọn cả ba theo thứ tự ngược lại.

<short pause> Bạn không phải sát thủ. Bạn chỉ là một người bình thường, có lẽ hơi giỏi thể thao, hoặc hơi giỏi toán. <short pause> Nhưng lá thư không cho phép từ chối.

<short pause> Trong Sakamoto Days, JCC là nơi đào tạo những sát thủ giỏi nhất, và chính Sakamoto từng học ở đó. Mùa một có cả một arc về kỳ thi chuyển trường, nơi Shin phải vượt qua những bài thi chết người.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku dẫn bạn đi qua kỳ thi JCC từng vòng một. Ở mỗi vòng, bạn phải chọn. Và lựa chọn của bạn quyết định bạn sống sót tới đâu.

<short pause> Hãy lấy một tờ giấy và ghi lại lựa chọn của mình ở mỗi vòng. Cuối video, Kaku sẽ tính điểm sống sót cho bạn.

<short pause> Bạn bắt đầu với mười điểm sống sót. Mỗi lựa chọn có thể cộng hoặc trừ điểm. Về không là bị loại, và trong kỳ thi này, bị loại không có nghĩa là về nhà đâu.

<short pause> Ba nguyên tắc này sẽ quay lại ở mọi vòng. Nếu bạn phân vân, hãy tự hỏi: Sakamoto sẽ làm gì? Câu trả lời thường là làm điều đơn giản nhất, bình tĩnh nhất, và không làm ai bị thương.

<short pause> Kaku chấm theo ba nguyên tắc rút ra từ Sakamoto Days. Một: quan sát quan trọng hơn sức mạnh. Hai: mọi đồ vật đều có thể là công cụ. Ba: người không cần giết ai mới là người mạnh nhất.

<short pause> Và một luật phụ: nếu bạn làm Kaku bật cười ở một lựa chọn nào đó, Kaku không cộng điểm đâu, nhưng Kaku sẽ nhớ bạn.

<short pause> Nhớ nhé: trong thế giới Sakamoto Days, những người mạnh nhất thường là những người bình tĩnh nhất, và buồn cười nhất.
```

**ElevenLabs**

```text
Video có spoiler nhẹ Sakamoto Days mùa một. Và đây là một kịch bản giả định của Kaku, lấy cảm hứng từ arc thi JCC, không phải nội dung chính thức. Nghề sát thủ là hư cấu, và video không cổ vũ bạo lực.

[pause] Giả sử một sáng thức dậy, bạn thấy một lá thư dưới cửa. Trong đó chỉ có một dòng: bạn đã được mời dự kỳ thi chuyển trường vào JCC, học viện đào tạo sát thủ danh giá nhất.

[pause] Bạn có đúng một ngày để chuẩn bị. Bạn có thể ngủ thật sớm, xem lại vài tập Sakamoto Days để học hỏi, hoặc… hoảng loạn. Kaku khuyên chọn cả ba theo thứ tự ngược lại.

[pause] Bạn không phải sát thủ. Bạn chỉ là một người bình thường, có lẽ hơi giỏi thể thao, hoặc hơi giỏi toán. [pause] Nhưng lá thư không cho phép từ chối.

[pause] Trong Sakamoto Days, JCC là nơi đào tạo những sát thủ giỏi nhất, và chính Sakamoto từng học ở đó. Mùa một có cả một arc về kỳ thi chuyển trường, nơi Shin phải vượt qua những bài thi chết người.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku dẫn bạn đi qua kỳ thi JCC từng vòng một. Ở mỗi vòng, bạn phải chọn. Và lựa chọn của bạn quyết định bạn sống sót tới đâu.

[pause] Hãy lấy một tờ giấy và ghi lại lựa chọn của mình ở mỗi vòng. Cuối video, Kaku sẽ tính điểm sống sót cho bạn.

[pause] Bạn bắt đầu với mười điểm sống sót. Mỗi lựa chọn có thể cộng hoặc trừ điểm. Về không là bị loại, và trong kỳ thi này, bị loại không có nghĩa là về nhà đâu.

[pause] Ba nguyên tắc này sẽ quay lại ở mọi vòng. [curious] Nếu bạn phân vân, hãy tự hỏi: Sakamoto sẽ làm gì? Câu trả lời thường là làm điều đơn giản nhất, bình tĩnh nhất, và không làm ai bị thương.

[pause] Kaku chấm theo ba nguyên tắc rút ra từ Sakamoto Days. Một: quan sát quan trọng hơn sức mạnh. Hai: mọi đồ vật đều có thể là công cụ. Ba: người không cần giết ai mới là người mạnh nhất.

[pause] Và một luật phụ: nếu bạn làm Kaku bật cười ở một lựa chọn nào đó, Kaku không cộng điểm đâu, nhưng Kaku sẽ nhớ bạn.

[pause] Nhớ nhé: trong thế giới Sakamoto Days, những người mạnh nhất thường là những người bình tĩnh nhất, và buồn cười nhất.
```

### c02 · Vòng 0: chọn vũ khí

Khoảng 67 giây · cảnh s13–s19 · 876 ký tự

**Gemini**

```text
Trước khi vào trường thi, giám thị cho bạn chọn một món mang theo. Có ba lựa chọn trên bàn.

<short pause> Lựa chọn A: một con dao chuyên nghiệp. Trông nguy hiểm, nhưng bạn chưa từng dùng dao ngoài việc gọt táo.

<short pause> Lựa chọn B: một khẩu súng. Mạnh, nhưng bạn chưa bắn bao giờ, và tiếng súng sẽ thu hút mọi thí sinh khác về phía bạn.

<short pause> Giám thị nhìn bạn một lúc lâu khi bạn chọn túi đồ đi chợ. Bạn không biết đó là ánh mắt thương hại hay ánh mắt tôn trọng.

<short pause> Lựa chọn C: một túi đồ đi chợ, gồm ô, băng keo, một chai nước và một gói bánh. Trông vô dụng.

<short pause> Nếu bạn chọn A hoặc B, trừ một điểm: vũ khí bạn không biết dùng còn nguy hiểm cho chính bạn hơn cho đối thủ. Nếu bạn chọn C, cộng hai điểm. Sakamoto sẽ gật đầu hài lòng với bạn.

<short pause> Kaku giải thích: trong Sakamoto Days, những đồ vật tầm thường lại linh hoạt nhất. Ô là khiên, là gậy, là móc. Băng keo trói được người. Và gói bánh giúp bạn không đói khi thi.
```

**ElevenLabs**

```text
Trước khi vào trường thi, giám thị cho bạn chọn một món mang theo. Có ba lựa chọn trên bàn.

[pause] Lựa chọn A: một con dao chuyên nghiệp. Trông nguy hiểm, nhưng bạn chưa từng dùng dao ngoài việc gọt táo.

[pause] Lựa chọn B: một khẩu súng. Mạnh, nhưng bạn chưa bắn bao giờ, và tiếng súng sẽ thu hút mọi thí sinh khác về phía bạn.

[pause] Giám thị nhìn bạn một lúc lâu khi bạn chọn túi đồ đi chợ. Bạn không biết đó là ánh mắt thương hại hay ánh mắt tôn trọng.

[pause] Lựa chọn C: một túi đồ đi chợ, gồm ô, băng keo, một chai nước và một gói bánh. Trông vô dụng.

[pause] Nếu bạn chọn A hoặc B, trừ một điểm: vũ khí bạn không biết dùng còn nguy hiểm cho chính bạn hơn cho đối thủ. Nếu bạn chọn C, cộng hai điểm. Sakamoto sẽ gật đầu hài lòng với bạn.

[pause] Kaku giải thích: trong Sakamoto Days, những đồ vật tầm thường lại linh hoạt nhất. Ô là khiên, là gậy, là móc. Băng keo trói được người. Và gói bánh giúp bạn không đói khi thi.
```

### c03 · Vòng 1: tòa nhà bẫy

Khoảng 120 giây · cảnh s20–s30 · 1560 ký tự

**Gemini**

```text
Bạn nhìn quanh sảnh. Có hai mươi thí sinh khác, ai cũng trông nguy hiểm hơn bạn. Một người đang mài dao, một người đang tập võ, một người đang… ăn mì.

<short pause> Vòng một: bạn bị đưa vào một tòa nhà năm tầng. Nhiệm vụ: lên tới sân thượng trong ba mươi phút. Trong tòa nhà có bẫy, và có những thí sinh khác.

<short pause> Bạn đứng ở sảnh. Trước mặt có thang máy, cầu thang bộ, và một ống thông gió mở toang.

<short pause> Lựa chọn A: đi thang máy cho nhanh. Lựa chọn B: đi cầu thang bộ, chậm nhưng nhìn thấy mọi thứ. Lựa chọn C: chui ống thông gió, không ai ngờ tới.

<short pause> Kaku ghi chú thêm: trong phim hành động, thang máy luôn là nơi xảy ra chuyện. Nếu bạn xem đủ nhiều phim, bạn sẽ biết tránh nó như tránh một cái bẫy lộ liễu.

<short pause> Nếu bạn chọn thang máy: trừ ba điểm. Trong một kỳ thi sát thủ, thang máy là cái hộp kín mà ai cũng biết bạn sẽ bước vào. Đèn tắt giữa chừng và bạn phải trèo ra qua nắp trần.

<short pause> Nếu bạn chọn cầu thang bộ: cộng một điểm. Chậm hơn, nhưng bạn nhìn thấy dây bẫy căng ngang bậc thứ ba tầng hai. Quan sát đã cứu bạn.

<short pause> Trên đường bò qua ống thông gió, bạn còn nghe được hai thí sinh khác thì thầm kế hoạch phục kích ở tầng bốn. Thông tin miễn phí, nhưng đổi lại là đầu gối đau nhức.

<short pause> Nếu bạn chọn ống thông gió: cộng hai điểm, nhưng mất thêm năm phút vì bạn bị kẹt ở một khúc quanh. May là có gói bánh để giữ bình tĩnh.

<short pause> Và nếu bạn tự hỏi người ăn mì là ai: trong Sakamoto Days, người bình tĩnh nhất phòng thường là người nguy hiểm nhất. Hãy tránh xa người đó.

<short pause> <laugh> Kaku ghi chú: trong arc JCC thật, những thí sinh sống sót thường không phải người nhanh nhất, mà là người nhìn ra cái bẫy trước người khác.
```

**ElevenLabs**

```text
Bạn nhìn quanh sảnh. Có hai mươi thí sinh khác, ai cũng trông nguy hiểm hơn bạn. Một người đang mài dao, một người đang tập võ, một người đang… ăn mì.

[pause] Vòng một: bạn bị đưa vào một tòa nhà năm tầng. Nhiệm vụ: lên tới sân thượng trong ba mươi phút. Trong tòa nhà có bẫy, và có những thí sinh khác.

[pause] Bạn đứng ở sảnh. Trước mặt có thang máy, cầu thang bộ, và một ống thông gió mở toang.

[pause] Lựa chọn A: đi thang máy cho nhanh. Lựa chọn B: đi cầu thang bộ, chậm nhưng nhìn thấy mọi thứ. Lựa chọn C: chui ống thông gió, không ai ngờ tới.

[pause] Kaku ghi chú thêm: trong phim hành động, thang máy luôn là nơi xảy ra chuyện. Nếu bạn xem đủ nhiều phim, bạn sẽ biết tránh nó như tránh một cái bẫy lộ liễu.

[pause] Nếu bạn chọn thang máy: trừ ba điểm. Trong một kỳ thi sát thủ, thang máy là cái hộp kín mà ai cũng biết bạn sẽ bước vào. Đèn tắt giữa chừng và bạn phải trèo ra qua nắp trần.

[pause] Nếu bạn chọn cầu thang bộ: cộng một điểm. Chậm hơn, nhưng bạn nhìn thấy dây bẫy căng ngang bậc thứ ba tầng hai. Quan sát đã cứu bạn.

[pause] Trên đường bò qua ống thông gió, bạn còn nghe được hai thí sinh khác thì thầm kế hoạch phục kích ở tầng bốn. Thông tin miễn phí, nhưng đổi lại là đầu gối đau nhức.

[pause] Nếu bạn chọn ống thông gió: cộng hai điểm, nhưng mất thêm năm phút vì bạn bị kẹt ở một khúc quanh. May là có gói bánh để giữ bình tĩnh.

[pause] Và nếu bạn tự hỏi người ăn mì là ai: trong Sakamoto Days, người bình tĩnh nhất phòng thường là người nguy hiểm nhất. Hãy tránh xa người đó.

[pause] [chuckles] Kaku ghi chú: trong arc JCC thật, những thí sinh sống sót thường không phải người nhanh nhất, mà là người nhìn ra cái bẫy trước người khác.
```

### c04 · Vòng phụ: kiểm tra quan sát / Vòng 2: gặp thí sinh khác

Khoảng 151 giây · cảnh s31–s45 · 1957 ký tự

**Gemini**

```text
Giữa cầu thang tầng hai, một giám thị chặn bạn lại. Bà ta nói: trước khi đi tiếp, trả lời ba câu hỏi về căn phòng bạn vừa đi qua. Mỗi câu đúng cộng một điểm.

<short pause> Kaku sẽ cho bạn xem căn phòng đó trong năm giây. Hãy nhìn thật kỹ. Nếu cần, bạn có thể tạm dừng video.

<short pause> Câu một: căn phòng có mấy cửa ra vào? Câu hai: đồng hồ trên tường chỉ mấy giờ? Câu ba: trong phòng có bao nhiêu chiếc ghế?

<short pause> Đáp án: hai cửa, ba giờ mười phút, và ba chiếc ghế. Mỗi câu đúng, cộng một điểm vào tờ giấy của bạn.

<short pause> Nếu bạn trả lời đúng cả ba, Kaku rất ấn tượng. Trong thế giới sát thủ, người để ý số lối thoát và thời gian là người sống sót lâu nhất.

<short pause> <laugh> Kaku thì nhớ được chiếc ô, còn đồng hồ và ghế thì quên sạch. Có lẽ vì Kaku chỉ để ý những thứ có thể làm vũ khí.

<short pause> Hành lang tầng ba im lặng một cách đáng ngờ. Những vết trầy trên tường cho thấy đã có một trận đánh ở đây vài phút trước.

<short pause> Tầng ba. Bạn gặp một thí sinh khác, đang bị thương ở chân và ngồi dựa tường. Người đó nhìn bạn, không nói gì.

<short pause> Lựa chọn A: tấn công để loại một đối thủ. Lựa chọn B: bỏ qua, đi tiếp. Lựa chọn C: dùng băng keo trong túi để băng chân cho người đó, rồi đi cùng.

<short pause> Bài học ở đây: trong một kỳ thi sát thủ, thứ trông yếu nhất có thể là cái bẫy. Người giỏi quan sát sẽ để ý rằng giày của người đó không hề dính bụi, như thể chưa từng chạy.

<short pause> Nếu bạn tấn công: trừ ba điểm. <short pause> Hóa ra người đó giả vờ bị thương để dụ những kẻ hiếu chiến. Bạn bị phản đòn, và bị đánh dấu là người chơi nguy hiểm.

<short pause> Nếu bạn bỏ qua: không cộng không trừ. An toàn, nhưng bạn mất một cơ hội.

<short pause> Và bạn còn nhận ra người đó chính là người đã giả vờ bị thương để thử lòng mọi người. Họ nói: bạn là người đầu tiên dừng lại giúp. Đôi khi bài thi thật không nằm ở đề thi.

<short pause> Nếu bạn giúp: cộng ba điểm. Người đó hóa ra rất giỏi đọc bản đồ tòa nhà và chỉ cho bạn lối tắt lên sân thượng. Và bạn vừa có một đồng minh.

<short pause> Kaku giải thích: đây chính là tinh thần của cửa hàng Sakamoto. Shin, Lu, Heisuke đều từng là người lạ, thậm chí là kẻ thù, trước khi trở thành đồng đội.
```

**ElevenLabs**

```text
Giữa cầu thang tầng hai, một giám thị chặn bạn lại. Bà ta nói: trước khi đi tiếp, trả lời ba câu hỏi về căn phòng bạn vừa đi qua. Mỗi câu đúng cộng một điểm.

[pause] Kaku sẽ cho bạn xem căn phòng đó trong năm giây. Hãy nhìn thật kỹ. Nếu cần, bạn có thể tạm dừng video.

[pause] [curious] Câu một: căn phòng có mấy cửa ra vào? Câu hai: đồng hồ trên tường chỉ mấy giờ? Câu ba: trong phòng có bao nhiêu chiếc ghế?

[pause] Đáp án: hai cửa, ba giờ mười phút, và ba chiếc ghế. Mỗi câu đúng, cộng một điểm vào tờ giấy của bạn.

[pause] Nếu bạn trả lời đúng cả ba, Kaku rất ấn tượng. Trong thế giới sát thủ, người để ý số lối thoát và thời gian là người sống sót lâu nhất.

[pause] [chuckles] Kaku thì nhớ được chiếc ô, còn đồng hồ và ghế thì quên sạch. Có lẽ vì Kaku chỉ để ý những thứ có thể làm vũ khí.

[pause] Hành lang tầng ba im lặng một cách đáng ngờ. Những vết trầy trên tường cho thấy đã có một trận đánh ở đây vài phút trước.

[pause] Tầng ba. Bạn gặp một thí sinh khác, đang bị thương ở chân và ngồi dựa tường. Người đó nhìn bạn, không nói gì.

[pause] Lựa chọn A: tấn công để loại một đối thủ. Lựa chọn B: bỏ qua, đi tiếp. Lựa chọn C: dùng băng keo trong túi để băng chân cho người đó, rồi đi cùng.

[pause] Bài học ở đây: trong một kỳ thi sát thủ, thứ trông yếu nhất có thể là cái bẫy. Người giỏi quan sát sẽ để ý rằng giày của người đó không hề dính bụi, như thể chưa từng chạy.

[pause] Nếu bạn tấn công: trừ ba điểm. [pause] Hóa ra người đó giả vờ bị thương để dụ những kẻ hiếu chiến. Bạn bị phản đòn, và bị đánh dấu là người chơi nguy hiểm.

[pause] Nếu bạn bỏ qua: không cộng không trừ. An toàn, nhưng bạn mất một cơ hội.

[pause] Và bạn còn nhận ra người đó chính là người đã giả vờ bị thương để thử lòng mọi người. Họ nói: bạn là người đầu tiên dừng lại giúp. Đôi khi bài thi thật không nằm ở đề thi.

[pause] Nếu bạn giúp: cộng ba điểm. Người đó hóa ra rất giỏi đọc bản đồ tòa nhà và chỉ cho bạn lối tắt lên sân thượng. Và bạn vừa có một đồng minh.

[pause] Kaku giải thích: đây chính là tinh thần của cửa hàng Sakamoto. Shin, Lu, Heisuke đều từng là người lạ, thậm chí là kẻ thù, trước khi trở thành đồng đội.
```

### c05 · Vòng 3: bài kiểm tra của giám khảo

Khoảng 104 giây · cảnh s46–s55 · 1356 ký tự

**Gemini**

```text
Gió trên sân thượng rất mạnh. Bạn còn ba mươi giây trong tổng thời gian, và toàn thân mỏi nhừ sau năm tầng lầu.

<short pause> Bạn lên tới sân thượng. <short pause> Nhưng chưa xong. Một giám khảo đứng chờ, một sát thủ chuyên nghiệp mặc vest, mỉm cười, và nói: vòng cuối, hãy chạm vào tôi trong sáu mươi giây.

<short pause> Kaku đoán nhiều bạn sẽ muốn dùng khẩu súng ở đây, nếu đã chọn nó ở vòng không. <short pause> Nhưng giám khảo đã tính trước: bắn trượt một phát là mất lượt, và bạn vẫn phải chạm vào họ.

<short pause> Giám khảo nhanh hơn bạn rất nhiều. Lao vào trực diện thì chắc chắn thất bại.

<short pause> Lựa chọn A: lao vào liên tục cho tới khi hết sức. Lựa chọn B: đứng yên quan sát cách giám khảo di chuyển. Lựa chọn C: mở ô che tầm nhìn, rồi ném chai nước sang hướng khác để đánh lạc hướng.

<short pause> Nếu bạn lao vào: trừ hai điểm, bạn kiệt sức sau hai mươi giây.

<short pause> Nếu bạn quan sát rồi mới dùng ô và chai nước, Kaku cho phép bạn cộng cả hai điểm. Quan sát trước, hành động sau, đó là công thức của người sống sót.

<short pause> Nếu bạn quan sát: cộng một điểm. Bạn nhận ra giám khảo luôn né sang trái. <short pause> Nhưng biết thì biết, bạn vẫn chưa đủ nhanh.

<short pause> Nếu bạn dùng ô và chai nước: cộng bốn điểm. Giám khảo quay đầu theo tiếng động đúng một khoảnh khắc, và đầu ngón tay bạn chạm được vào tay áo vest. Giám khảo bật cười.

<short pause> <laugh> Kaku ghi chú: giám khảo không đánh giá bạn mạnh cỡ nào. Họ đánh giá bạn có biết dùng những gì mình có hay không. Đó chính là cách Sakamoto chiến đấu.
```

**ElevenLabs**

```text
Gió trên sân thượng rất mạnh. Bạn còn ba mươi giây trong tổng thời gian, và toàn thân mỏi nhừ sau năm tầng lầu.

[pause] Bạn lên tới sân thượng. [pause] Nhưng chưa xong. Một giám khảo đứng chờ, một sát thủ chuyên nghiệp mặc vest, mỉm cười, và nói: vòng cuối, hãy chạm vào tôi trong sáu mươi giây.

[pause] Kaku đoán nhiều bạn sẽ muốn dùng khẩu súng ở đây, nếu đã chọn nó ở vòng không. [pause] Nhưng giám khảo đã tính trước: bắn trượt một phát là mất lượt, và bạn vẫn phải chạm vào họ.

[pause] Giám khảo nhanh hơn bạn rất nhiều. Lao vào trực diện thì chắc chắn thất bại.

[pause] Lựa chọn A: lao vào liên tục cho tới khi hết sức. Lựa chọn B: đứng yên quan sát cách giám khảo di chuyển. Lựa chọn C: mở ô che tầm nhìn, rồi ném chai nước sang hướng khác để đánh lạc hướng.

[pause] Nếu bạn lao vào: trừ hai điểm, bạn kiệt sức sau hai mươi giây.

[pause] Nếu bạn quan sát rồi mới dùng ô và chai nước, Kaku cho phép bạn cộng cả hai điểm. Quan sát trước, hành động sau, đó là công thức của người sống sót.

[pause] Nếu bạn quan sát: cộng một điểm. Bạn nhận ra giám khảo luôn né sang trái. [pause] Nhưng biết thì biết, bạn vẫn chưa đủ nhanh.

[pause] Nếu bạn dùng ô và chai nước: cộng bốn điểm. Giám khảo quay đầu theo tiếng động đúng một khoảnh khắc, và đầu ngón tay bạn chạm được vào tay áo vest. Giám khảo bật cười.

[pause] [chuckles] Kaku ghi chú: giám khảo không đánh giá bạn mạnh cỡ nào. Họ đánh giá bạn có biết dùng những gì mình có hay không. Đó chính là cách Sakamoto chiến đấu.
```

### c06 · Biến cố: kẻ lạ đột nhập

Khoảng 81 giây · cảnh s56–s63 · 1058 ký tự

**Gemini**

```text
Giám khảo lập tức thay đổi nét mặt. Nụ cười biến mất. Lần đầu tiên bạn thấy một sát thủ chuyên nghiệp nghiêm túc thật sự.

<short pause> Ngay lúc đó, còi báo động vang lên. Một nhóm kẻ lạ mặt đột nhập kỳ thi. Kaku lấy cảm hứng từ việc arc JCC trong truyện cũng bị phe của Slur để mắt tới.

<short pause> Lựa chọn A: chạy trốn một mình. Lựa chọn B: đuổi theo kẻ lạ để lập công. Lựa chọn C: đưa người bạn bị thương xuống nơi an toàn và báo cho giám khảo.

<short pause> Nếu bạn chạy một mình: trừ hai điểm. Bạn thoát, nhưng giám khảo ghi nhận bạn bỏ lại đồng đội.

<short pause> Trong Sakamoto Days, những thí sinh liều lĩnh thường được cứu bởi người khác. <short pause> Nhưng trong kịch bản của Kaku, không có Sakamoto nào đứng chờ ở cầu thang cả.

<short pause> Nếu bạn đuổi theo: trừ ba điểm. Kẻ lạ là sát thủ thật, và bạn chỉ là thí sinh. Dũng cảm nhưng liều lĩnh.

<short pause> Biết nhờ người đúng lúc không phải là yếu. Ngay cả Sakamoto, người mạnh nhất, cũng dựa vào Shin, Lu, Heisuke và vợ mình. Một đội mạnh hơn một người.

<short pause> Nếu bạn đưa bạn xuống và báo giám khảo: cộng ba điểm. Bạn biết giới hạn của mình, và biết lúc nào nên nhường việc cho người chuyên nghiệp.
```

**ElevenLabs**

```text
Giám khảo lập tức thay đổi nét mặt. Nụ cười biến mất. Lần đầu tiên bạn thấy một sát thủ chuyên nghiệp nghiêm túc thật sự.

[pause] Ngay lúc đó, còi báo động vang lên. Một nhóm kẻ lạ mặt đột nhập kỳ thi. Kaku lấy cảm hứng từ việc arc JCC trong truyện cũng bị phe của Slur để mắt tới.

[pause] Lựa chọn A: chạy trốn một mình. Lựa chọn B: đuổi theo kẻ lạ để lập công. Lựa chọn C: đưa người bạn bị thương xuống nơi an toàn và báo cho giám khảo.

[pause] Nếu bạn chạy một mình: trừ hai điểm. Bạn thoát, nhưng giám khảo ghi nhận bạn bỏ lại đồng đội.

[pause] Trong Sakamoto Days, những thí sinh liều lĩnh thường được cứu bởi người khác. [pause] Nhưng trong kịch bản của Kaku, không có Sakamoto nào đứng chờ ở cầu thang cả.

[pause] Nếu bạn đuổi theo: trừ ba điểm. Kẻ lạ là sát thủ thật, và bạn chỉ là thí sinh. Dũng cảm nhưng liều lĩnh.

[pause] Biết nhờ người đúng lúc không phải là yếu. Ngay cả Sakamoto, người mạnh nhất, cũng dựa vào Shin, Lu, Heisuke và vợ mình. Một đội mạnh hơn một người.

[pause] Nếu bạn đưa bạn xuống và báo giám khảo: cộng ba điểm. Bạn biết giới hạn của mình, và biết lúc nào nên nhường việc cho người chuyên nghiệp.
```

### c07 · Kết quả: bạn sống sót tới đâu? / Nếu là nhân vật trong truyện

Khoảng 139 giây · cảnh s64–s77 · 1808 ký tự

**Gemini**

```text
Nhớ cộng cả ba câu hỏi ở vòng phụ, và lượt cộng thêm nếu bạn quan sát trước khi dùng ô ở vòng ba.

<short pause> Giờ cộng điểm của bạn. Nhớ, bạn bắt đầu với mười điểm.

<short pause> Dưới năm điểm: bạn bị loại ở vòng một hoặc hai. Đừng buồn, bạn vẫn có thể về làm nhân viên cửa hàng tiện lợi. Ở thế giới này, đó là nghề an toàn nhất… trừ khi bạn làm ở cửa hàng Sakamoto.

<short pause> Và nếu bạn bị loại, đừng buồn: nhiều nhân vật mạnh trong truyện cũng từng trượt kỳ thi đầu tiên của mình.

<short pause> Từ năm tới mười bốn điểm: bạn vào được vòng ba nhưng chưa đỗ. Giám khảo ghi tên bạn vào danh sách đáng chú ý.

<short pause> Từ mười lăm tới hai mươi hai điểm: bạn đỗ JCC. Chúc mừng, và cũng chia buồn, vì học viện này còn đáng sợ hơn kỳ thi.

<short pause> Từ hai mươi ba điểm trở lên: bạn chọn gần như hoàn hảo. Một thành viên Order đã để mắt tới bạn. Và ở cuối con phố, một ông chủ cửa hàng tròn trịa đang mỉm cười.

<short pause> Điểm tối đa trong kịch bản này là hai mươi tám. Nếu bạn đạt được, hãy khoe trong bình luận. Kaku muốn biết có bao nhiêu người đạt điểm tối đa ngay lần đầu.

<short pause> Nếu Shin dự kỳ thi này, cậu sẽ đọc được suy nghĩ của giám khảo và biết trước họ né sang đâu. Vòng ba với Shin sẽ dễ hơn nhiều, trừ khi giám khảo cố tình nghĩ lung tung.

<short pause> Nếu là Lu, cô sẽ đánh thẳng từ tầng một lên sân thượng, lạc đường hai lần, và vẫn tới nơi đúng giờ nhờ may mắn.

<short pause> Còn nếu là Nagumo, người bạn cũ hay cười của Sakamoto, thì chắc anh ta sẽ cải trang thành giám khảo, và chẳng ai biết anh ta có đi thi thật hay không.

<short pause> Nếu là Heisuke, anh sẽ ngắm từ tòa nhà đối diện, và chú vẹt của anh sẽ là thí sinh đầu tiên chạm vào giám khảo.

<short pause> Nếu là Sakamoto, ông sẽ đi cầu thang bộ, giúp người bị thương, chạm vào giám khảo bằng một cây bút bi, và về nhà kịp nấu cơm tối.

<short pause> <laugh> Và nếu là Kaku, Kaku sẽ chọn túi đồ đi chợ, đi cầu thang bộ, giúp người bị thương, rồi… bị kẹt ở vòng ba vì không chạm được ai. Kaku biết giới hạn của mình.
```

**ElevenLabs**

```text
Nhớ cộng cả ba câu hỏi ở vòng phụ, và lượt cộng thêm nếu bạn quan sát trước khi dùng ô ở vòng ba.

[pause] Giờ cộng điểm của bạn. Nhớ, bạn bắt đầu với mười điểm.

[pause] Dưới năm điểm: bạn bị loại ở vòng một hoặc hai. Đừng buồn, bạn vẫn có thể về làm nhân viên cửa hàng tiện lợi. Ở thế giới này, đó là nghề an toàn nhất… trừ khi bạn làm ở cửa hàng Sakamoto.

[pause] Và nếu bạn bị loại, đừng buồn: nhiều nhân vật mạnh trong truyện cũng từng trượt kỳ thi đầu tiên của mình.

[pause] Từ năm tới mười bốn điểm: bạn vào được vòng ba nhưng chưa đỗ. Giám khảo ghi tên bạn vào danh sách đáng chú ý.

[pause] Từ mười lăm tới hai mươi hai điểm: bạn đỗ JCC. Chúc mừng, và cũng chia buồn, vì học viện này còn đáng sợ hơn kỳ thi.

[pause] Từ hai mươi ba điểm trở lên: bạn chọn gần như hoàn hảo. Một thành viên Order đã để mắt tới bạn. Và ở cuối con phố, một ông chủ cửa hàng tròn trịa đang mỉm cười.

[pause] Điểm tối đa trong kịch bản này là hai mươi tám. Nếu bạn đạt được, hãy khoe trong bình luận. Kaku muốn biết có bao nhiêu người đạt điểm tối đa ngay lần đầu.

[pause] Nếu Shin dự kỳ thi này, cậu sẽ đọc được suy nghĩ của giám khảo và biết trước họ né sang đâu. Vòng ba với Shin sẽ dễ hơn nhiều, trừ khi giám khảo cố tình nghĩ lung tung.

[pause] Nếu là Lu, cô sẽ đánh thẳng từ tầng một lên sân thượng, lạc đường hai lần, và vẫn tới nơi đúng giờ nhờ may mắn.

[pause] Còn nếu là Nagumo, người bạn cũ hay cười của Sakamoto, thì chắc anh ta sẽ cải trang thành giám khảo, và chẳng ai biết anh ta có đi thi thật hay không.

[pause] Nếu là Heisuke, anh sẽ ngắm từ tòa nhà đối diện, và chú vẹt của anh sẽ là thí sinh đầu tiên chạm vào giám khảo.

[pause] Nếu là Sakamoto, ông sẽ đi cầu thang bộ, giúp người bị thương, chạm vào giám khảo bằng một cây bút bi, và về nhà kịp nấu cơm tối.

[pause] [chuckles] Và nếu là Kaku, Kaku sẽ chọn túi đồ đi chợ, đi cầu thang bộ, giúp người bị thương, rồi… bị kẹt ở vòng ba vì không chạm được ai. Kaku biết giới hạn của mình.
```

### c08 · Góc nhìn của Kaku: kỳ thi dạy gì / Kết

Khoảng 102 giây · cảnh s78–s86 · 1321 ký tự

**Gemini**

```text
Và không lựa chọn điểm cao nào đòi hỏi bạn phải mạnh. Chúng chỉ đòi hỏi bạn bình tĩnh, để ý, và tử tế. Kaku nghĩ đó là tin tốt cho tất cả chúng ta.

<short pause> Nhìn lại kịch bản, những lựa chọn được điểm cao đều giống nhau: quan sát trước khi hành động, dùng những gì mình có, và không bỏ rơi người khác.

<short pause> Đó cũng là lý do Sakamoto Days được yêu thích: một bộ truyện về sát thủ, nhưng nhân vật chính mạnh nhất lại là người không giết ai, và coi trọng gia đình hơn mọi thứ.

<short pause> Nhưng những nguyên tắc thì dùng được ngoài đời: quan sát kỹ, dùng những gì mình có, và giúp người bên cạnh. Chúng giúp bạn qua kỳ thi thật, kể cả kỳ thi cuối kỳ.

<short pause> Kaku nhắc lại: đây là một kịch bản giả định để vui. Ngoài đời, không có trường sát thủ nào, và bạo lực không phải thứ để đùa.

<short pause> Nếu nhiều bạn thích kiểu video này, Kaku sẽ soạn thêm những kỳ thi khác: thi thợ săn Hunter, thi vào học viện phép thuật, hay thi làm hải tặc. Bình chọn trong bình luận nhé.

<short pause> Bạn được bao nhiêu điểm? Và bạn chọn gì ở vòng không? Kaku đoán phần lớn mọi người sẽ chọn khẩu súng, cho tới khi nghe giải thích.

<short pause> Video tiếp theo, Kaku mở cửa nhập môn cho một bộ anime đặc biệt: Gachiakuta, nơi rác thải của người giàu trở thành vũ khí của người nghèo.

<short pause> <laugh> Nếu bạn thích kiểu video tự chọn đường đi như thế này, hãy đăng ký kênh để Kaku soạn thêm nhiều kỳ thi nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và không lựa chọn điểm cao nào đòi hỏi bạn phải mạnh. Chúng chỉ đòi hỏi bạn bình tĩnh, để ý, và tử tế. Kaku nghĩ đó là tin tốt cho tất cả chúng ta.

[pause] Nhìn lại kịch bản, những lựa chọn được điểm cao đều giống nhau: quan sát trước khi hành động, dùng những gì mình có, và không bỏ rơi người khác.

[pause] Đó cũng là lý do Sakamoto Days được yêu thích: một bộ truyện về sát thủ, nhưng nhân vật chính mạnh nhất lại là người không giết ai, và coi trọng gia đình hơn mọi thứ.

[pause] Nhưng những nguyên tắc thì dùng được ngoài đời: quan sát kỹ, dùng những gì mình có, và giúp người bên cạnh. Chúng giúp bạn qua kỳ thi thật, kể cả kỳ thi cuối kỳ.

[pause] Kaku nhắc lại: đây là một kịch bản giả định để vui. Ngoài đời, không có trường sát thủ nào, và bạo lực không phải thứ để đùa.

[pause] Nếu nhiều bạn thích kiểu video này, Kaku sẽ soạn thêm những kỳ thi khác: thi thợ săn Hunter, thi vào học viện phép thuật, hay thi làm hải tặc. Bình chọn trong bình luận nhé.

[pause] [curious] Bạn được bao nhiêu điểm? Và bạn chọn gì ở vòng không? Kaku đoán phần lớn mọi người sẽ chọn khẩu súng, cho tới khi nghe giải thích.

[pause] Video tiếp theo, Kaku mở cửa nhập môn cho một bộ anime đặc biệt: Gachiakuta, nơi rác thải của người giàu trở thành vũ khí của người nghèo.

[pause] [chuckles] Nếu bạn thích kiểu video tự chọn đường đi như thế này, hãy đăng ký kênh để Kaku soạn thêm nhiều kỳ thi nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
