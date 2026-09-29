# Bộ prompt · Black Clover: Bậc thang sức mạnh của Asta — từ không có gì tới Ác ma hợp thể

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 8 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo spoiler: video này đi tới hết arc Vương quốc Spade trong manga, tức phần mà anime mùa hai đang kể, v…

```text
Wide 16:9 landscape cinematic frame. a battered old spellbook with a torn dark cover lying on a stone floor beside a spoiler warning card, close-up, dramatic dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một cậu bé sinh ra trong một thế giới mà ai cũng có phép thuật, trừ cậu. Không một chút ma lực nào. Cậu chỉ c…

```text
Wide 16:9 landscape cinematic frame. a small boy doing push-ups alone in a village square while other children float objects around him with magic, wide shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhiều năm sau, cậu bay trên đôi cánh đen, mang sừng, cầm những thanh kiếm cắt đứt mọi phép thuật, và đứng nga…

```text
Wide 16:9 landscape cinematic frame. a lone silhouette with large dark wings hovering above a battlefield, holding a massive rough blade, low-angle shot, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Giữa hai hình ảnh đó là một bậc thang dài. Hôm nay Kaku leo từng nấc: điều kiện để mở, sức mạnh có được, và c…

```text
Wide 16:9 landscape cinematic frame. a long stone staircase spiraling upward into dark clouds with faint glowing steps, wide shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay là bậc thang sức mạnh của Asta, từ cậu bé không có phép thuật tới Ác ma h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot at the bottom of a tall staircase, stretching its wings as if preparing to climb. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Black Clover là manga của Tabata Yuki, bắt đầu đăng năm 2015. Anime mùa một có một trăm bảy mươi tập, do stud…

```text
Wide 16:9 landscape cinematic frame. a tall stack of manga volumes beside a TV remote and a small four-leaf clover charm on a shelf, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Nấc 0: không có gì

Lời: Nấc đầu tiên là không có gì. Asta là trẻ mồ côi, lớn lên ở nhà thờ làng Hage cùng Yuno, cậu bé cũng mồ côi, đ…

```text
Wide 16:9 landscape cinematic frame. two small baby baskets left on the steps of a village church under a snowy sky, wide shot, soft cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Yuno có tài năng phép thuật hiếm có. Asta thì không có gì. Nhưng Asta vẫn tuyên bố, trước mặt mọi người, rằng…

```text
Wide 16:9 landscape cinematic frame. a small boy shouting with his fist raised at the top of a hill while other villagers watch in disbelief, wide shot, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Người trong làng cười cậu. Những đứa trẻ khác bay lượn, đốt lửa, gọi gió. Còn Asta, mỗi sáng, chỉ chạy quanh…

```text
Wide 16:9 landscape cinematic frame. a boy running along a dirt road at dawn with a wooden sword strapped to his back while children float playfully above, wide shot, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Không có ma lực, Asta làm điều duy nhất cậu làm được: tập thể lực. Chạy, hít đất, vung kiếm gỗ, mỗi ngày, suố…

```text
Wide 16:9 landscape cinematic frame. a worn wooden sword leaning against a tree beside a patch of trampled grass from endless training, close-up, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Và có một chi tiết nhỏ: Asta từng tỏ tình với sơ Lily ở nhà thờ gần như mỗi ngày, và bị từ chối mỗi ngày. Kiê…

```text
Wide 16:9 landscape cinematic frame. a small boy kneeling dramatically with a handful of wildflowers in front of a church door, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Điều kiện của nấc này: không có. Sức mạnh: chỉ có cơ thể. Cái giá: bị cả thế giới coi thường.

```text
Wide 16:9 landscape cinematic frame. a small index card on parchment with three lines: condition, power, cost, each filled with a simple doodle, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Black Clover xây Asta như một người bị loại khỏi hệ thống. Và mọi nấc thang sau đó đều là cách cậu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up at a closed gate with a small ladder leaning against the wall beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Nấc 1: grimoire năm lá và thanh kiếm đầu tiên

Lời: Năm mười lăm tuổi, mọi đứa trẻ nhận một cuốn sách phép gọi là grimoire. Asta không nhận được gì, cho tới khi…

```text
Wide 16:9 landscape cinematic frame. a tattered dark spellbook flying through a moonlit window toward a sleeping boy, wide shot, eerie blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Cuốn sách có hình cỏ năm lá, loại cực hiếm, được đồn là nơi ác ma trú ngụ. Và từ trong đó, Asta rút ra một th…

```text
Wide 16:9 landscape cinematic frame. a huge rusty broadsword being drawn out of an open book in a burst of dark particles, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Thanh kiếm có một năng lực duy nhất: phản ma thuật. Nó cắt đứt, vô hiệu hóa mọi phép thuật chạm vào nó.

```text
Wide 16:9 landscape cinematic frame. a blade slicing through a glowing magical projectile, the energy scattering into dark dust, dynamic close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Điều kiện: được grimoire chọn, và đủ sức vung một thanh kiếm nặng. Đây là lúc nhiều năm tập thể lực được đền…

```text
Wide 16:9 landscape cinematic frame. a pair of calloused hands gripping a heavy sword hilt tightly, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Asta gia nhập Hắc Bò, hội hiệp sĩ bị coi là tệ nhất vương quốc, vì chỉ đội trưởng Yami chịu nhận cậu. Một ngư…

```text
Wide 16:9 landscape cinematic frame. a rundown castle-like hideout with a crooked flag and a lively crowd of misfits in the courtyard, wide shot, warm chaotic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Sức mạnh: vô hiệu phép của đối thủ. Cái giá: Asta vẫn không có phép thuật để bay, để chữa thương, hay tấn côn…

```text
Wide 16:9 landscape cinematic frame. a lone figure charging head-on across a field toward a hail of magical attacks, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Kaku để ý: thanh kiếm đầu tiên của Asta không đẹp, không sắc. Nó gỉ sét và thô kệch, giống hệt chủ của nó lúc…

```text
Wide 16:9 landscape cinematic frame. a rusty, chipped blade resting beside a polished ornate magic staff on a table, contrasting still life, dramatic light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Sau đó, Asta có thêm những thanh kiếm khác: một thanh có thể hấp thụ phép thuật rồi phóng ra, và những thanh…

```text
Wide 16:9 landscape cinematic frame. several different swords with rough dark blades arranged on a wooden rack, still life, dramatic side light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Nấc 2: Khí và đôi tay bị nguyền

Lời: Ở đền dưới đáy biển, Asta đối đầu Vetto, một thành viên của tổ chức Mắt Mặt trời Đêm. Hắn nghiền nát và nguyề…

```text
Wide 16:9 landscape cinematic frame. a pair of heavily bandaged arms resting on a stone table with dark cracks spreading beneath the bandages, close-up, cold eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Cũng trong trận đó, Asta học được một kỹ năng mới từ đội trưởng Yami: Khí, khả năng cảm nhận luồng sống của đ…

```text
Wide 16:9 landscape cinematic frame. a figure with closed eyes standing still while faint lines of energy flow around approaching shadows, symbolic medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Yami từng nói với Asta, đại ý: hãy vượt qua giới hạn của mình, ngay tại đây, ngay bây giờ. Câu nói trở thành…

```text
Wide 16:9 landscape cinematic frame. a large calloused hand resting on a younger figure's shoulder at the edge of a battlefield, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Khí là kỹ năng hoàn hảo cho Asta. Người không có ma lực không cảm nhận được phép, nhưng vẫn cảm nhận được sự…

```text
Wide 16:9 landscape cinematic frame. a blindfolded swordsman deflecting an arrow with a calm expression in a misty forest, dynamic close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Cả Hắc Bò, và cả những người từng coi thường Asta, đi tìm cách chữa cho cậu. Lần đầu tiên, cậu bé không có gì…

```text
Wide 16:9 landscape cinematic frame. several different silhouettes walking together along a forest path carrying an injured companion on a stretcher, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Nhưng lời nguyền khiến không phép chữa thương nào tác dụng được. Asta suýt mất đôi tay mãi mãi, tức là mất lu…

```text
Wide 16:9 landscape cinematic frame. a sword lying on the floor just out of reach of a limp bandaged hand, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nữ hoàng phù thủy ở Rừng Phù thủy dùng phép máu để chữa cho Asta. Đổi lại, nhóm Asta phải bảo vệ khu rừng. Đô…

```text
Wide 16:9 landscape cinematic frame. a mysterious dark forest with glowing flowers and a large tree throne at its heart, wide shot, magical crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Điều kiện của nấc này: suýt mất tất cả. Sức mạnh: Khí, và đôi tay được chữa. Cái giá: một món nợ với phù thủy…

```text
Wide 16:9 landscape cinematic frame. a small index card with three filled lines and a tiny drawing of a bandaged hand, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Nấc 3: Dạng Đen lần đầu

Lời: Ở chương chín mươi bảy, trong trận đấu với Ladros, một chuyện lạ xảy ra. Phản ma thuật từ grimoire trào ra, b…

```text
Wide 16:9 landscape cinematic frame. a right arm suddenly engulfed in swirling black energy, dynamic close-up, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Một chiếc cánh đen mọc ra từ vai phải. Một chiếc sừng nhỏ, mắt phải chuyển đỏ. Asta nhanh và mạnh hơn hẳn. Ng…

```text
Wide 16:9 landscape cinematic frame. a silhouette with a single black wing sprouting from one shoulder and a small horn on one side of the head, dramatic low-angle shot, dark red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nguồn gốc sức mạnh này: con ác ma sống trong grimoire năm lá. Asta đang mượn sức của nó, dù chưa biết nó là a…

```text
Wide 16:9 landscape cinematic frame. a shadowy horned figure faintly visible inside the pages of an open book, symbolic close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Điều kiện: cơ thể Asta chịu được phản ma thuật tràn ra. Sức mạnh: tốc độ và sức phá hủy tăng vọt, có thể cắt…

```text
Wide 16:9 landscape cinematic frame. a figure dashing through a massive magical barrier and splitting it in two, dynamic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Có lúc Asta suýt bị Dạng Đen chiếm lấy, như thể ác ma bên trong muốn giành quyền điều khiển. Cậu phải dùng hế…

```text
Wide 16:9 landscape cinematic frame. a figure clutching his own arm as black energy crawls further up his shoulder, a determined grimace, dramatic close-up, dark red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Cái giá: chỉ giữ được trong thời gian ngắn, và cơ thể kiệt sức sau đó. Asta chưa kiểm soát được, nó giống như…

```text
Wide 16:9 landscape cinematic frame. a figure collapsing to one knee with black energy fading from his arm, close-up, exhausted grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Người trong vương quốc bắt đầu sợ Asta, vì sức mạnh của ác ma. Cậu bé từng bị coi thường vì không có gì, giờ…

```text
Wide 16:9 landscape cinematic frame. a crowd of townspeople stepping back warily from a lone figure standing in a square, wide shot, cold uneasy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: nấc này rất đáng sợ về mặt ý nghĩa. Lần đầu tiên, sức mạnh của Asta không đến từ tập luyện, mà từ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a notebook close to its chest while a small shadow looms behind it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Nấc 4: Dạng Đen hoàn chỉnh

Lời: Qua nhiều trận, Asta dần mở rộng Dạng Đen. Từ một cánh tay, tới cả hai tay, rồi toàn thân được bao phủ.

```text
Wide 16:9 landscape cinematic frame. three silhouette sketches side by side on parchment showing black energy spreading from one arm to the whole body, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Ở arc Vương quốc Spade, Asta được Nacht, phó đội trưởng bí ẩn của Hắc Bò, huấn luyện. Nacht cũng là người man…

```text
Wide 16:9 landscape cinematic frame. a figure in a dark coat standing in deep shadows of a stone corridor, watching a younger figure train, wide shot, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Bản thân Nacht có tới bốn ác ma, mỗi con như một người bạn. Cách anh sống cùng ác ma của mình chính là hình m…

```text
Wide 16:9 landscape cinematic frame. four small horned shadows sitting around a figure in a dim room like companions, symbolic wide shot, warm dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nacht dạy Asta rằng sức mạnh của ác ma không thể chỉ mượn. Muốn dùng hết, phải có một mối quan hệ thật với ác…

```text
Wide 16:9 landscape cinematic frame. two shadows facing each other across a candlelit table, one human and one horned, symbolic medium shot, warm dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Điều kiện: luyện tập thời gian dài, và kiểm soát được cảm xúc. Sức mạnh: giữ Dạng Đen lâu hơn, dùng các đòn m…

```text
Wide 16:9 landscape cinematic frame. a small index card with three filled lines and a doodle of a black wing, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Có lúc Asta bị bắt giam và suýt bị xử vì mang sức mạnh ác ma. Chính các đồng đội và người thầy đã đứng ra bảo…

```text
Wide 16:9 landscape cinematic frame. a heavy iron cell door slightly ajar with warm light spilling in from the corridor, close-up, hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và rồi câu hỏi lớn xuất hiện: con ác ma trong grimoire của Asta là ai? Và nó muốn gì từ cậu?

```text
Wide 16:9 landscape cinematic frame. a closed dark book with a faint pair of red eyes glowing through the cover, close-up, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Người song hành: Yuno

Lời: Muốn hiểu bậc thang của Asta, phải nhìn người leo song song với cậu: Yuno, người anh em cùng lớn lên ở nhà th…

```text
Wide 16:9 landscape cinematic frame. two parallel staircases side by side rising into the clouds, one plain stone and one with glowing wind swirls, wide shot, dramatic sky light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Yuno nhận grimoire bốn lá, loại hiếm, và được tinh linh gió chọn. Mọi thứ Asta phải giành lấy bằng mồ hôi thì…

```text
Wide 16:9 landscape cinematic frame. a gentle swirl of wind lifting leaves around a calm young figure holding an open book, medium shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng Yuno cũng không đứng yên. Cậu luyện tập không ngừng, vì biết rằng Asta sẽ không bao giờ ngừng. Hai ngườ…

```text
Wide 16:9 landscape cinematic frame. two silhouettes training on opposite hilltops at dawn, each glancing toward the other, wide shot, golden morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku để ý: mỗi lần Asta lên một nấc, Yuno cũng lên một nấc. Họ không đua để thắng nhau, mà đua để giữ lời hứa…

```text
Wide 16:9 landscape cinematic frame. two small hands pressing their fists together in front of a village church, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Và ở arc Spade, Yuno cũng khám phá ra thân phận thật của mình, gắn với chính vương quốc đang bị ác ma chiếm g…

```text
Wide 16:9 landscape cinematic frame. an old royal crest partially hidden under dust on a frozen castle wall, close-up, cold mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Bí mật của Liebe

Lời: Con ác ma tên là Liebe. Và câu chuyện của nó là một trong những bất ngờ cảm động nhất Black Clover.

```text
Wide 16:9 landscape cinematic frame. an old photograph-like sketch of a small horned creature sitting beside a gentle woman in a field, sepia tone, soft warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Liebe là một ác ma bị các ác ma khác bắt nạt, vì nó không có phép thuật. Giống hệt Asta. Nó trốn khỏi địa ngụ…

```text
Wide 16:9 landscape cinematic frame. a small horned creature cowering alone in a dark crevice while larger shadows loom above, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ở đó, Liebe được một người phụ nữ tên Richita nhận nuôi và chăm sóc như con. Và Richita chính là mẹ ruột của…

```text
Wide 16:9 landscape cinematic frame. a woman gently holding a small horned creature in her arms under a tree at sunset, medium shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và điều đau lòng nhất: Asta bị bỏ lại ở nhà thờ khi còn bé không phải vì bị bỏ rơi. Mẹ cậu mất đi khả năng nu…

```text
Wide 16:9 landscape cinematic frame. a mother's silhouette leaving a small basket at a church door in the snow, looking back one last time, wide shot, soft cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Richita mất khi bảo vệ Liebe khỏi một ác ma khác. Liebe mang hận, và muốn dùng cơ thể Asta để trả thù. Đó là…

```text
Wide 16:9 landscape cinematic frame. a single flower lying on a hillside grave under a grey sky, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Liebe từng muốn chiếm cơ thể Asta. Asta từng đánh nhau với Liebe. Nhưng cả hai nhận ra kẻ thù thật sự là nhữn…

```text
Wide 16:9 landscape cinematic frame. two figures standing back to back facing a towering dark shadow, wide shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Khi biết sự thật, Asta không ghét Liebe. Cậu coi Liebe như anh em, vì cả hai đều được cùng một người mẹ yêu t…

```text
Wide 16:9 landscape cinematic frame. two silhouettes of different shapes standing side by side on a hill looking at the sunset, back view, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là cú lật tuyệt vời. Sức mạnh mạnh nhất của Asta hóa ra đến từ tình mẹ, qua một ác ma.

```text
Wide 16:9 landscape cinematic frame. the owl mascot quietly wiping a tear with the corner of its wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Nấc 5: Ác ma hợp thể

Lời: Sau khi hiểu nhau, Asta và Liebe lập một khế ước ngang hàng. Không ai lợi dụng ai. Từ đó mở ra nấc cao nhất t…

```text
Wide 16:9 landscape cinematic frame. two hands, one human and one clawed, clasping each other firmly with light swirling around them, extreme close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Trong Ác ma hợp thể, Asta mang những đặc điểm của Liebe: đôi cánh lớn, mắt dọc, chiếc đuôi dài, và sức mạnh p…

```text
Wide 16:9 landscape cinematic frame. a silhouette with large dark wings, a long pointed tail and glowing slit eyes hovering in a stormy sky, dramatic low-angle wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Liebe cũng có thể tự chiến đấu bên cạnh Asta. Hai kẻ từng bị cả thế giới xem thường, giờ đứng cạnh nhau như m…

```text
Wide 16:9 landscape cinematic frame. two silhouettes of different shapes standing side by side facing an oncoming storm, wide shot, dramatic heroic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Khác với Dạng Đen, đây không còn là mượn sức. Asta và Liebe cùng chiến đấu trong một cơ thể, như hai người cù…

```text
Wide 16:9 landscape cinematic frame. two silhouettes merging into one shape with two distinct glows at its center, symbolic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Điều kiện: một mối quan hệ thật sự với ác ma, và một nghi thức ràng buộc ác ma. Sức mạnh: đủ để đối đầu với n…

```text
Wide 16:9 landscape cinematic frame. a vast dark castle floating above a frozen kingdom with a small winged figure flying toward it, wide shot, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Và trong trận cuối của arc Spade, Asta dùng Ác ma hợp thể để chiến đấu cùng các đồng đội chống lại những ác m…

```text
Wide 16:9 landscape cinematic frame. a winged silhouette flying alongside several other glowing figures toward a massive dark castle, wide shot, heroic dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Cái giá: gánh nặng rất lớn lên cơ thể, và mọi thứ phụ thuộc vào sự tin tưởng giữa hai người. Nếu niềm tin vỡ,…

```text
Wide 16:9 landscape cinematic frame. a delicate glass bridge connecting two cliffs with a small crack forming in its center, symbolic wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Trong manga còn có một nấc Ác ma hợp thể mạnh hơn nữa về sau, với thêm sừng, thêm sức mạnh. Kaku không kể chi…

```text
Wide 16:9 landscape cinematic frame. a partially open door with faint horned shadows visible through the gap, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Vùng spoiler arc cuối: Zetten

Lời: Từ đây là spoiler arc cuối của manga, chưa lên anime. Nếu bạn muốn chờ, hãy tua tới chương Toàn bộ bậc thang.

```text
Wide 16:9 landscape cinematic frame. a red warning sign painted on a wooden gate across a mountain path, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Khoảng một năm sau arc Spade, Asta thua trong trận với Lucius, kẻ thù cuối cùng. Cậu bị đưa tới Vùng đất Mặt…

```text
Wide 16:9 landscape cinematic frame. a traditional eastern village with wooden houses and cherry trees at the foot of a mountain, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Ở đó, Asta học một kỹ thuật tên Zetten từ Ichika, em gái Yami: biến Khí thành một điểm năng lượng cực nhỏ, rồ…

```text
Wide 16:9 landscape cinematic frame. a single point of light concentrated on the tip of a blade, about to burst, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Ở Vùng đất Mặt Trời, Asta còn học cách chiến đấu bằng kiếm theo phong cách mới, cùng những kiếm sĩ bản địa. M…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman practicing slow sword forms beneath cherry blossoms beside an old shrine, wide shot, soft pink light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và thú vị nhất: Zetten không cần phép thuật. Nó quay về gốc rễ của Asta: cơ thể, luyện tập, và Khí. Nấc cao n…

```text
Wide 16:9 landscape cinematic frame. a worn wooden practice sword lying beside a gleaming real sword on a dojo floor, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Arc cuối vẫn đang được kể trong manga. Kaku sẽ không nói trước kết quả.

```text
Wide 16:9 landscape cinematic frame. an unfinished staircase with its final steps still being built, wide shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Toàn bộ bậc thang

Lời: Và đây là toàn bộ bậc thang của Asta. Nấc không: không có gì, chỉ có cơ thể. Nấc một: grimoire năm lá và kiếm…

```text
Wide 16:9 landscape cinematic frame. a tall staircase drawn on parchment with the first two steps labeled with small icons of a fist and a sword, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nấc hai: Khí và đôi tay được chữa. Nấc ba: Dạng Đen lần đầu. Nấc bốn: Dạng Đen hoàn chỉnh cùng Nacht.

```text
Wide 16:9 landscape cinematic frame. the middle steps of the staircase with icons of an eye, a single wing, and full wings, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Nấc năm: Ác ma hợp thể cùng Liebe. Và nấc cuối, trong arc cuối: Zetten, quay về gốc rễ.

```text
Wide 16:9 landscape cinematic frame. the top steps of the staircase with icons of two clasped hands and a single point of light, amber ink close-up, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và mỗi nấc cũng có một cái giá: bị coi thường, suýt mất đôi tay, bị nghi ngờ, bị ác ma chiếm lấy, và gánh cả…

```text
Wide 16:9 landscape cinematic frame. a staircase where each step has a small price tag hanging from its edge, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nhìn cả bậc thang, Kaku thấy một điều: mỗi nấc sức mạnh của Asta đều đến từ một mối quan hệ. Yami dạy Khí. Nữ…

```text
Wide 16:9 landscape cinematic frame. a staircase where each step has a different small silhouette standing beside it offering a hand up, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku

Lời: Black Clover thường bị nói là một bộ shounen truyền thống: nhân vật chính hét to, không bỏ cuộc. Đúng vậy. Nh…

```text
Wide 16:9 landscape cinematic frame. a small figure shouting with fists raised on a hilltop at sunrise, wide shot, bright inspiring light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu bạn đang cảm thấy mình không có tài năng gì đặc biệt, Asta là lời nhắc: không có ma lực vẫn có thể leo, c…

```text
Wide 16:9 landscape cinematic frame. a pair of worn running shoes at the bottom of a long staircase at sunrise, close-up, hopeful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Người không có gì không leo lên một mình. Cậu leo lên nhờ những người, và cả những ác ma, chịu đưa tay ra cho…

```text
Wide 16:9 landscape cinematic frame. a hand reaching down from above to pull a small figure up onto a ledge, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và cậu cũng đưa tay ra cho người khác, kể cả cho một ác ma bị cả địa ngục bắt nạt. Kaku nghĩ đó mới là phép t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot extending a wing to help a small shadowy creature climb onto a step. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Bạn thích nấc nào nhất trên bậc thang của Asta? Và nếu có một ác ma trong grimoire của bạn, bạn muốn nó là ai…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny staircase and a small horned doodle, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku mở một cuốn sổ đáng sợ: Death Note. Luật của cuốn sổ, và những cách mà các nhân vật đã…

```text
Wide 16:9 landscape cinematic frame. a plain black notebook lying on a desk beside an apple, close-up, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này tiếp thêm cho bạn chút động lực, hãy đăng ký kênh. Không có phép thuật cũng không sao, chỉ cần…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing proudly at the top of a small staircase and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nấc 0: không có gì

Khoảng 146 giây · cảnh s01–s13 · 1901 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này đi tới hết arc Vương quốc Spade trong manga, tức phần mà anime mùa hai đang kể, và có một chương riêng cho arc cuối, Kaku sẽ báo trước.

<short pause> Một cậu bé sinh ra trong một thế giới mà ai cũng có phép thuật, trừ cậu. Không một chút ma lực nào. Cậu chỉ có hai bàn tay, một giọng hét rất to, và một giấc mơ trở thành Ma pháp vương.

<short pause> Nhiều năm sau, cậu bay trên đôi cánh đen, mang sừng, cầm những thanh kiếm cắt đứt mọi phép thuật, và đứng ngang hàng với những ác ma mạnh nhất.

<short pause> Giữa hai hình ảnh đó là một bậc thang dài. Hôm nay Kaku leo từng nấc: điều kiện để mở, sức mạnh có được, và cái giá phải trả.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay là bậc thang sức mạnh của Asta, từ cậu bé không có phép thuật tới Ác ma hợp thể. Cuối video là toàn bộ bậc thang trong một hình.

<short pause> Black Clover là manga của Tabata Yuki, bắt đầu đăng năm 2015. Anime mùa một có một trăm bảy mươi tập, do studio Pierrot làm, và mùa hai đang phát, kể arc Vương quốc Spade.

<short pause> Nấc đầu tiên là không có gì. Asta là trẻ mồ côi, lớn lên ở nhà thờ làng Hage cùng Yuno, cậu bé cũng mồ côi, được nhặt về cùng ngày.

<short pause> Yuno có tài năng phép thuật hiếm có. Asta thì không có gì. <short pause> Nhưng Asta vẫn tuyên bố, trước mặt mọi người, rằng cậu sẽ trở thành Ma pháp vương.

<short pause> Người trong làng cười cậu. Những đứa trẻ khác bay lượn, đốt lửa, gọi gió. Còn Asta, mỗi sáng, chỉ chạy quanh làng với một thanh kiếm gỗ trên lưng.

<short pause> Không có ma lực, Asta làm điều duy nhất cậu làm được: tập thể lực. Chạy, hít đất, vung kiếm gỗ, mỗi ngày, suốt nhiều năm.

<short pause> Và có một chi tiết nhỏ: Asta từng tỏ tình với sơ Lily ở nhà thờ gần như mỗi ngày, và bị từ chối mỗi ngày. Kiên trì là tính cách của cậu, trong cả luyện tập lẫn tình cảm.

<short pause> Điều kiện của nấc này: không có. Sức mạnh: chỉ có cơ thể. Cái giá: bị cả thế giới coi thường.

<short pause> Kaku để ý: Black Clover xây Asta như một người bị loại khỏi hệ thống. Và mọi nấc thang sau đó đều là cách cậu leo lên mà không cần hệ thống cho phép.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này đi tới hết arc Vương quốc Spade trong manga, tức phần mà anime mùa hai đang kể, và có một chương riêng cho arc cuối, Kaku sẽ báo trước.

[pause] Một cậu bé sinh ra trong một thế giới mà ai cũng có phép thuật, trừ cậu. Không một chút ma lực nào. Cậu chỉ có hai bàn tay, một giọng hét rất to, và một giấc mơ trở thành Ma pháp vương.

[pause] Nhiều năm sau, cậu bay trên đôi cánh đen, mang sừng, cầm những thanh kiếm cắt đứt mọi phép thuật, và đứng ngang hàng với những ác ma mạnh nhất.

[pause] Giữa hai hình ảnh đó là một bậc thang dài. Hôm nay Kaku leo từng nấc: điều kiện để mở, sức mạnh có được, và cái giá phải trả.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay là bậc thang sức mạnh của Asta, từ cậu bé không có phép thuật tới Ác ma hợp thể. Cuối video là toàn bộ bậc thang trong một hình.

[pause] Black Clover là manga của Tabata Yuki, bắt đầu đăng năm 2015. Anime mùa một có một trăm bảy mươi tập, do studio Pierrot làm, và mùa hai đang phát, kể arc Vương quốc Spade.

[pause] Nấc đầu tiên là không có gì. Asta là trẻ mồ côi, lớn lên ở nhà thờ làng Hage cùng Yuno, cậu bé cũng mồ côi, được nhặt về cùng ngày.

[pause] Yuno có tài năng phép thuật hiếm có. Asta thì không có gì. [pause] Nhưng Asta vẫn tuyên bố, trước mặt mọi người, rằng cậu sẽ trở thành Ma pháp vương.

[pause] Người trong làng cười cậu. Những đứa trẻ khác bay lượn, đốt lửa, gọi gió. Còn Asta, mỗi sáng, chỉ chạy quanh làng với một thanh kiếm gỗ trên lưng.

[pause] Không có ma lực, Asta làm điều duy nhất cậu làm được: tập thể lực. Chạy, hít đất, vung kiếm gỗ, mỗi ngày, suốt nhiều năm.

[pause] Và có một chi tiết nhỏ: Asta từng tỏ tình với sơ Lily ở nhà thờ gần như mỗi ngày, và bị từ chối mỗi ngày. Kiên trì là tính cách của cậu, trong cả luyện tập lẫn tình cảm.

[pause] Điều kiện của nấc này: không có. Sức mạnh: chỉ có cơ thể. Cái giá: bị cả thế giới coi thường.

[pause] Kaku để ý: Black Clover xây Asta như một người bị loại khỏi hệ thống. Và mọi nấc thang sau đó đều là cách cậu leo lên mà không cần hệ thống cho phép.
```

### c02 · Nấc 1: grimoire năm lá và thanh kiếm đầu tiên

Khoảng 93 giây · cảnh s14–s21 · 1210 ký tự

**Gemini**

```text
Năm mười lăm tuổi, mọi đứa trẻ nhận một cuốn sách phép gọi là grimoire. Asta không nhận được gì, cho tới khi một cuốn sách cũ nát, bìa đen, tự bay tới tìm cậu.

<short pause> Cuốn sách có hình cỏ năm lá, loại cực hiếm, được đồn là nơi ác ma trú ngụ. Và từ trong đó, Asta rút ra một thanh kiếm khổng lồ, gỉ sét.

<short pause> Thanh kiếm có một năng lực duy nhất: phản ma thuật. Nó cắt đứt, vô hiệu hóa mọi phép thuật chạm vào nó.

<short pause> Điều kiện: được grimoire chọn, và đủ sức vung một thanh kiếm nặng. Đây là lúc nhiều năm tập thể lực được đền đáp. Người không có sức sẽ không nhấc nổi thanh kiếm.

<short pause> Asta gia nhập Hắc Bò, hội hiệp sĩ bị coi là tệ nhất vương quốc, vì chỉ đội trưởng Yami chịu nhận cậu. Một người bị loại, gia nhập đội của những người bị loại.

<short pause> Sức mạnh: vô hiệu phép của đối thủ. Cái giá: Asta vẫn không có phép thuật để bay, để chữa thương, hay tấn công từ xa. Cậu phải lao vào cận chiến trong mọi trận.

<short pause> Kaku để ý: thanh kiếm đầu tiên của Asta không đẹp, không sắc. Nó gỉ sét và thô kệch, giống hệt chủ của nó lúc đó. <short pause> Nhưng nó làm được việc mà không phép thuật nào làm được.

<short pause> Sau đó, Asta có thêm những thanh kiếm khác: một thanh có thể hấp thụ phép thuật rồi phóng ra, và những thanh khác về sau. Kaku đã kể kỹ trong video hồ sơ grimoire.
```

**ElevenLabs**

```text
Năm mười lăm tuổi, mọi đứa trẻ nhận một cuốn sách phép gọi là grimoire. Asta không nhận được gì, cho tới khi một cuốn sách cũ nát, bìa đen, tự bay tới tìm cậu.

[pause] Cuốn sách có hình cỏ năm lá, loại cực hiếm, được đồn là nơi ác ma trú ngụ. Và từ trong đó, Asta rút ra một thanh kiếm khổng lồ, gỉ sét.

[pause] Thanh kiếm có một năng lực duy nhất: phản ma thuật. Nó cắt đứt, vô hiệu hóa mọi phép thuật chạm vào nó.

[pause] Điều kiện: được grimoire chọn, và đủ sức vung một thanh kiếm nặng. Đây là lúc nhiều năm tập thể lực được đền đáp. Người không có sức sẽ không nhấc nổi thanh kiếm.

[pause] Asta gia nhập Hắc Bò, hội hiệp sĩ bị coi là tệ nhất vương quốc, vì chỉ đội trưởng Yami chịu nhận cậu. Một người bị loại, gia nhập đội của những người bị loại.

[pause] Sức mạnh: vô hiệu phép của đối thủ. Cái giá: Asta vẫn không có phép thuật để bay, để chữa thương, hay tấn công từ xa. Cậu phải lao vào cận chiến trong mọi trận.

[pause] Kaku để ý: thanh kiếm đầu tiên của Asta không đẹp, không sắc. Nó gỉ sét và thô kệch, giống hệt chủ của nó lúc đó. [pause] Nhưng nó làm được việc mà không phép thuật nào làm được.

[pause] Sau đó, Asta có thêm những thanh kiếm khác: một thanh có thể hấp thụ phép thuật rồi phóng ra, và những thanh khác về sau. Kaku đã kể kỹ trong video hồ sơ grimoire.
```

### c03 · Nấc 2: Khí và đôi tay bị nguyền

Khoảng 86 giây · cảnh s22–s29 · 1121 ký tự

**Gemini**

```text
Ở đền dưới đáy biển, Asta đối đầu Vetto, một thành viên của tổ chức Mắt Mặt trời Đêm. Hắn nghiền nát và nguyền rủa cả hai cánh tay của Asta.

<short pause> Cũng trong trận đó, Asta học được một kỹ năng mới từ đội trưởng Yami: Khí, khả năng cảm nhận luồng sống của đối thủ để đoán đòn tấn công.

<short pause> Yami từng nói với Asta, đại ý: hãy vượt qua giới hạn của mình, ngay tại đây, ngay bây giờ. Câu nói trở thành châm ngôn của cả Hắc Bò.

<short pause> Khí là kỹ năng hoàn hảo cho Asta. Người không có ma lực không cảm nhận được phép, nhưng vẫn cảm nhận được sự sống. Cậu biến điểm yếu thành điểm mạnh.

<short pause> Cả Hắc Bò, và cả những người từng coi thường Asta, đi tìm cách chữa cho cậu. Lần đầu tiên, cậu bé không có gì được nhiều người cùng nâng lên.

<short pause> Nhưng lời nguyền khiến không phép chữa thương nào tác dụng được. Asta suýt mất đôi tay mãi mãi, tức là mất luôn khả năng cầm kiếm.

<short pause> Nữ hoàng phù thủy ở Rừng Phù thủy dùng phép máu để chữa cho Asta. Đổi lại, nhóm Asta phải bảo vệ khu rừng. Đôi tay lành lại, và mạnh hơn trước.

<short pause> Điều kiện của nấc này: suýt mất tất cả. Sức mạnh: Khí, và đôi tay được chữa. Cái giá: một món nợ với phù thủy, và nỗi sợ mất đi thứ duy nhất cậu có.
```

**ElevenLabs**

```text
Ở đền dưới đáy biển, Asta đối đầu Vetto, một thành viên của tổ chức Mắt Mặt trời Đêm. Hắn nghiền nát và nguyền rủa cả hai cánh tay của Asta.

[pause] Cũng trong trận đó, Asta học được một kỹ năng mới từ đội trưởng Yami: Khí, khả năng cảm nhận luồng sống của đối thủ để đoán đòn tấn công.

[pause] Yami từng nói với Asta, đại ý: hãy vượt qua giới hạn của mình, ngay tại đây, ngay bây giờ. Câu nói trở thành châm ngôn của cả Hắc Bò.

[pause] Khí là kỹ năng hoàn hảo cho Asta. Người không có ma lực không cảm nhận được phép, nhưng vẫn cảm nhận được sự sống. Cậu biến điểm yếu thành điểm mạnh.

[pause] Cả Hắc Bò, và cả những người từng coi thường Asta, đi tìm cách chữa cho cậu. Lần đầu tiên, cậu bé không có gì được nhiều người cùng nâng lên.

[pause] Nhưng lời nguyền khiến không phép chữa thương nào tác dụng được. Asta suýt mất đôi tay mãi mãi, tức là mất luôn khả năng cầm kiếm.

[pause] Nữ hoàng phù thủy ở Rừng Phù thủy dùng phép máu để chữa cho Asta. Đổi lại, nhóm Asta phải bảo vệ khu rừng. Đôi tay lành lại, và mạnh hơn trước.

[pause] Điều kiện của nấc này: suýt mất tất cả. Sức mạnh: Khí, và đôi tay được chữa. Cái giá: một món nợ với phù thủy, và nỗi sợ mất đi thứ duy nhất cậu có.
```

### c04 · Nấc 3: Dạng Đen lần đầu

Khoảng 85 giây · cảnh s30–s37 · 1105 ký tự

**Gemini**

```text
Ở chương chín mươi bảy, trong trận đấu với Ladros, một chuyện lạ xảy ra. Phản ma thuật từ grimoire trào ra, bao phủ cánh tay phải của Asta.

<short pause> Một chiếc cánh đen mọc ra từ vai phải. Một chiếc sừng nhỏ, mắt phải chuyển đỏ. Asta nhanh và mạnh hơn hẳn. Người ta gọi đây là Asta Đen.

<short pause> Nguồn gốc sức mạnh này: con ác ma sống trong grimoire năm lá. Asta đang mượn sức của nó, dù chưa biết nó là ai.

<short pause> Điều kiện: cơ thể Asta chịu được phản ma thuật tràn ra. Sức mạnh: tốc độ và sức phá hủy tăng vọt, có thể cắt cả những phép thuật lớn.

<short pause> Có lúc Asta suýt bị Dạng Đen chiếm lấy, như thể ác ma bên trong muốn giành quyền điều khiển. Cậu phải dùng hết ý chí để giữ lại chính mình.

<short pause> Cái giá: chỉ giữ được trong thời gian ngắn, và cơ thể kiệt sức sau đó. Asta chưa kiểm soát được, nó giống như mượn một thứ quá lớn so với mình.

<short pause> Người trong vương quốc bắt đầu sợ Asta, vì sức mạnh của ác ma. Cậu bé từng bị coi thường vì không có gì, giờ bị nghi ngờ vì có quá nhiều.

<short pause> <laugh> Kaku để ý: nấc này rất đáng sợ về mặt ý nghĩa. Lần đầu tiên, sức mạnh của Asta không đến từ tập luyện, mà từ một thứ ác ma. Và cậu phải học cách không để nó nuốt mình.
```

**ElevenLabs**

```text
Ở chương chín mươi bảy, trong trận đấu với Ladros, một chuyện lạ xảy ra. Phản ma thuật từ grimoire trào ra, bao phủ cánh tay phải của Asta.

[pause] Một chiếc cánh đen mọc ra từ vai phải. Một chiếc sừng nhỏ, mắt phải chuyển đỏ. Asta nhanh và mạnh hơn hẳn. Người ta gọi đây là Asta Đen.

[pause] Nguồn gốc sức mạnh này: con ác ma sống trong grimoire năm lá. Asta đang mượn sức của nó, dù chưa biết nó là ai.

[pause] Điều kiện: cơ thể Asta chịu được phản ma thuật tràn ra. Sức mạnh: tốc độ và sức phá hủy tăng vọt, có thể cắt cả những phép thuật lớn.

[pause] Có lúc Asta suýt bị Dạng Đen chiếm lấy, như thể ác ma bên trong muốn giành quyền điều khiển. Cậu phải dùng hết ý chí để giữ lại chính mình.

[pause] Cái giá: chỉ giữ được trong thời gian ngắn, và cơ thể kiệt sức sau đó. Asta chưa kiểm soát được, nó giống như mượn một thứ quá lớn so với mình.

[pause] Người trong vương quốc bắt đầu sợ Asta, vì sức mạnh của ác ma. Cậu bé từng bị coi thường vì không có gì, giờ bị nghi ngờ vì có quá nhiều.

[pause] [chuckles] Kaku để ý: nấc này rất đáng sợ về mặt ý nghĩa. Lần đầu tiên, sức mạnh của Asta không đến từ tập luyện, mà từ một thứ ác ma. Và cậu phải học cách không để nó nuốt mình.
```

### c05 · Nấc 4: Dạng Đen hoàn chỉnh / Người song hành: Yuno

Khoảng 128 giây · cảnh s38–s49 · 1664 ký tự

**Gemini**

```text
Qua nhiều trận, Asta dần mở rộng Dạng Đen. Từ một cánh tay, tới cả hai tay, rồi toàn thân được bao phủ.

<short pause> Ở arc Vương quốc Spade, Asta được Nacht, phó đội trưởng bí ẩn của Hắc Bò, huấn luyện. Nacht cũng là người mang ác ma, và biết cách sống cùng chúng.

<short pause> Bản thân Nacht có tới bốn ác ma, mỗi con như một người bạn. Cách anh sống cùng ác ma của mình chính là hình mẫu cho Asta.

<short pause> Nacht dạy Asta rằng sức mạnh của ác ma không thể chỉ mượn. Muốn dùng hết, phải có một mối quan hệ thật với ác ma của mình.

<short pause> Điều kiện: luyện tập thời gian dài, và kiểm soát được cảm xúc. Sức mạnh: giữ Dạng Đen lâu hơn, dùng các đòn mạnh hơn. Cái giá: vẫn phụ thuộc vào một ác ma mà cậu chưa hiểu.

<short pause> Có lúc Asta bị bắt giam và suýt bị xử vì mang sức mạnh ác ma. Chính các đồng đội và người thầy đã đứng ra bảo vệ cậu. Nấc thang này không chỉ thử thách cơ thể, mà thử thách cả niềm tin của người khác vào cậu.

<short pause> Và rồi câu hỏi lớn xuất hiện: con ác ma trong grimoire của Asta là ai? Và nó muốn gì từ cậu?

<short pause> Muốn hiểu bậc thang của Asta, phải nhìn người leo song song với cậu: Yuno, người anh em cùng lớn lên ở nhà thờ.

<short pause> Yuno nhận grimoire bốn lá, loại hiếm, và được tinh linh gió chọn. Mọi thứ Asta phải giành lấy bằng mồ hôi thì Yuno dường như có sẵn.

<short pause> Nhưng Yuno cũng không đứng yên. Cậu luyện tập không ngừng, vì biết rằng Asta sẽ không bao giờ ngừng. Hai người là động lực của nhau.

<short pause> Kaku để ý: mỗi lần Asta lên một nấc, Yuno cũng lên một nấc. Họ không đua để thắng nhau, mà đua để giữ lời hứa cùng nhau từ thời thơ ấu: ai sẽ trở thành Ma pháp vương.

<short pause> Và ở arc Spade, Yuno cũng khám phá ra thân phận thật của mình, gắn với chính vương quốc đang bị ác ma chiếm giữ. Hai con đường mồ côi, hai bí mật về gia đình.
```

**ElevenLabs**

```text
Qua nhiều trận, Asta dần mở rộng Dạng Đen. Từ một cánh tay, tới cả hai tay, rồi toàn thân được bao phủ.

[pause] Ở arc Vương quốc Spade, Asta được Nacht, phó đội trưởng bí ẩn của Hắc Bò, huấn luyện. Nacht cũng là người mang ác ma, và biết cách sống cùng chúng.

[pause] Bản thân Nacht có tới bốn ác ma, mỗi con như một người bạn. Cách anh sống cùng ác ma của mình chính là hình mẫu cho Asta.

[pause] Nacht dạy Asta rằng sức mạnh của ác ma không thể chỉ mượn. Muốn dùng hết, phải có một mối quan hệ thật với ác ma của mình.

[pause] Điều kiện: luyện tập thời gian dài, và kiểm soát được cảm xúc. Sức mạnh: giữ Dạng Đen lâu hơn, dùng các đòn mạnh hơn. Cái giá: vẫn phụ thuộc vào một ác ma mà cậu chưa hiểu.

[pause] Có lúc Asta bị bắt giam và suýt bị xử vì mang sức mạnh ác ma. Chính các đồng đội và người thầy đã đứng ra bảo vệ cậu. Nấc thang này không chỉ thử thách cơ thể, mà thử thách cả niềm tin của người khác vào cậu.

[pause] [curious] Và rồi câu hỏi lớn xuất hiện: con ác ma trong grimoire của Asta là ai? Và nó muốn gì từ cậu?

[pause] Muốn hiểu bậc thang của Asta, phải nhìn người leo song song với cậu: Yuno, người anh em cùng lớn lên ở nhà thờ.

[pause] Yuno nhận grimoire bốn lá, loại hiếm, và được tinh linh gió chọn. Mọi thứ Asta phải giành lấy bằng mồ hôi thì Yuno dường như có sẵn.

[pause] Nhưng Yuno cũng không đứng yên. Cậu luyện tập không ngừng, vì biết rằng Asta sẽ không bao giờ ngừng. Hai người là động lực của nhau.

[pause] Kaku để ý: mỗi lần Asta lên một nấc, Yuno cũng lên một nấc. Họ không đua để thắng nhau, mà đua để giữ lời hứa cùng nhau từ thời thơ ấu: ai sẽ trở thành Ma pháp vương.

[pause] Và ở arc Spade, Yuno cũng khám phá ra thân phận thật của mình, gắn với chính vương quốc đang bị ác ma chiếm giữ. Hai con đường mồ côi, hai bí mật về gia đình.
```

### c06 · Bí mật của Liebe

Khoảng 83 giây · cảnh s50–s57 · 1083 ký tự

**Gemini**

```text
Con ác ma tên là Liebe. Và câu chuyện của nó là một trong những bất ngờ cảm động nhất Black Clover.

<short pause> Liebe là một ác ma bị các ác ma khác bắt nạt, vì nó không có phép thuật. Giống hệt Asta. Nó trốn khỏi địa ngục và tới thế giới con người.

<short pause> Ở đó, Liebe được một người phụ nữ tên Richita nhận nuôi và chăm sóc như con. Và Richita chính là mẹ ruột của Asta.

<short pause> Và điều đau lòng nhất: Asta bị bỏ lại ở nhà thờ khi còn bé không phải vì bị bỏ rơi. Mẹ cậu mất đi khả năng nuôi con vì một năng lực đặc biệt của chính bà. Bà đã yêu con theo cách duy nhất có thể.

<short pause> Richita mất khi bảo vệ Liebe khỏi một ác ma khác. Liebe mang hận, và muốn dùng cơ thể Asta để trả thù. Đó là lý do nó ở trong grimoire.

<short pause> Liebe từng muốn chiếm cơ thể Asta. Asta từng đánh nhau với Liebe. <short pause> Nhưng cả hai nhận ra kẻ thù thật sự là những ác ma đã giết người mẹ của họ.

<short pause> Khi biết sự thật, Asta không ghét Liebe. Cậu coi Liebe như anh em, vì cả hai đều được cùng một người mẹ yêu thương. Hai kẻ không có phép thuật, cùng một gia đình.

<short pause> <laugh> Kaku thấy đây là cú lật tuyệt vời. Sức mạnh mạnh nhất của Asta hóa ra đến từ tình mẹ, qua một ác ma.
```

**ElevenLabs**

```text
Con ác ma tên là Liebe. Và câu chuyện của nó là một trong những bất ngờ cảm động nhất Black Clover.

[pause] Liebe là một ác ma bị các ác ma khác bắt nạt, vì nó không có phép thuật. Giống hệt Asta. Nó trốn khỏi địa ngục và tới thế giới con người.

[pause] Ở đó, Liebe được một người phụ nữ tên Richita nhận nuôi và chăm sóc như con. Và Richita chính là mẹ ruột của Asta.

[pause] Và điều đau lòng nhất: Asta bị bỏ lại ở nhà thờ khi còn bé không phải vì bị bỏ rơi. Mẹ cậu mất đi khả năng nuôi con vì một năng lực đặc biệt của chính bà. Bà đã yêu con theo cách duy nhất có thể.

[pause] Richita mất khi bảo vệ Liebe khỏi một ác ma khác. Liebe mang hận, và muốn dùng cơ thể Asta để trả thù. Đó là lý do nó ở trong grimoire.

[pause] Liebe từng muốn chiếm cơ thể Asta. Asta từng đánh nhau với Liebe. [pause] Nhưng cả hai nhận ra kẻ thù thật sự là những ác ma đã giết người mẹ của họ.

[pause] Khi biết sự thật, Asta không ghét Liebe. Cậu coi Liebe như anh em, vì cả hai đều được cùng một người mẹ yêu thương. Hai kẻ không có phép thuật, cùng một gia đình.

[pause] [chuckles] Kaku thấy đây là cú lật tuyệt vời. Sức mạnh mạnh nhất của Asta hóa ra đến từ tình mẹ, qua một ác ma.
```

### c07 · Nấc 5: Ác ma hợp thể / Vùng spoiler arc cuối: Zetten

Khoảng 149 giây · cảnh s58–s71 · 1933 ký tự

**Gemini**

```text
Sau khi hiểu nhau, Asta và Liebe lập một khế ước ngang hàng. Không ai lợi dụng ai. Từ đó mở ra nấc cao nhất trong arc Spade: Ác ma hợp thể.

<short pause> Trong Ác ma hợp thể, Asta mang những đặc điểm của Liebe: đôi cánh lớn, mắt dọc, chiếc đuôi dài, và sức mạnh phản ma thuật hoàn toàn.

<short pause> Liebe cũng có thể tự chiến đấu bên cạnh Asta. Hai kẻ từng bị cả thế giới xem thường, giờ đứng cạnh nhau như một đội.

<short pause> Khác với Dạng Đen, đây không còn là mượn sức. Asta và Liebe cùng chiến đấu trong một cơ thể, như hai người cùng lái một con tàu.

<short pause> Điều kiện: một mối quan hệ thật sự với ác ma, và một nghi thức ràng buộc ác ma. Sức mạnh: đủ để đối đầu với những ác ma cấp cao nhất đang chiếm giữ Vương quốc Spade.

<short pause> Và trong trận cuối của arc Spade, Asta dùng Ác ma hợp thể để chiến đấu cùng các đồng đội chống lại những ác ma cấp cao nhất. Đây là lần đầu tiên cậu thật sự đứng ngang hàng với những người mạnh nhất.

<short pause> Cái giá: gánh nặng rất lớn lên cơ thể, và mọi thứ phụ thuộc vào sự tin tưởng giữa hai người. Nếu niềm tin vỡ, sức mạnh cũng vỡ.

<short pause> Trong manga còn có một nấc Ác ma hợp thể mạnh hơn nữa về sau, với thêm sừng, thêm sức mạnh. Kaku không kể chi tiết để bạn tự khám phá.

<short pause> Từ đây là spoiler arc cuối của manga, chưa lên anime. Nếu bạn muốn chờ, hãy tua tới chương Toàn bộ bậc thang.

<short pause> Khoảng một năm sau arc Spade, Asta thua trong trận với Lucius, kẻ thù cuối cùng. Cậu bị đưa tới Vùng đất Mặt Trời, quê hương của đội trưởng Yami.

<short pause> Ở đó, Asta học một kỹ thuật tên Zetten từ Ichika, em gái Yami: biến Khí thành một điểm năng lượng cực nhỏ, rồi bùng nổ trong một nhát chém duy nhất.

<short pause> Ở Vùng đất Mặt Trời, Asta còn học cách chiến đấu bằng kiếm theo phong cách mới, cùng những kiếm sĩ bản địa. Một cậu bé từ làng Hage đi nửa vòng thế giới để quay về với chính mình.

<short pause> Và thú vị nhất: Zetten không cần phép thuật. Nó quay về gốc rễ của Asta: cơ thể, luyện tập, và Khí. Nấc cao nhất lại giống nấc đầu tiên nhất.

<short pause> Arc cuối vẫn đang được kể trong manga. Kaku sẽ không nói trước kết quả.
```

**ElevenLabs**

```text
Sau khi hiểu nhau, Asta và Liebe lập một khế ước ngang hàng. Không ai lợi dụng ai. Từ đó mở ra nấc cao nhất trong arc Spade: Ác ma hợp thể.

[pause] Trong Ác ma hợp thể, Asta mang những đặc điểm của Liebe: đôi cánh lớn, mắt dọc, chiếc đuôi dài, và sức mạnh phản ma thuật hoàn toàn.

[pause] Liebe cũng có thể tự chiến đấu bên cạnh Asta. Hai kẻ từng bị cả thế giới xem thường, giờ đứng cạnh nhau như một đội.

[pause] Khác với Dạng Đen, đây không còn là mượn sức. Asta và Liebe cùng chiến đấu trong một cơ thể, như hai người cùng lái một con tàu.

[pause] Điều kiện: một mối quan hệ thật sự với ác ma, và một nghi thức ràng buộc ác ma. Sức mạnh: đủ để đối đầu với những ác ma cấp cao nhất đang chiếm giữ Vương quốc Spade.

[pause] Và trong trận cuối của arc Spade, Asta dùng Ác ma hợp thể để chiến đấu cùng các đồng đội chống lại những ác ma cấp cao nhất. Đây là lần đầu tiên cậu thật sự đứng ngang hàng với những người mạnh nhất.

[pause] Cái giá: gánh nặng rất lớn lên cơ thể, và mọi thứ phụ thuộc vào sự tin tưởng giữa hai người. Nếu niềm tin vỡ, sức mạnh cũng vỡ.

[pause] Trong manga còn có một nấc Ác ma hợp thể mạnh hơn nữa về sau, với thêm sừng, thêm sức mạnh. Kaku không kể chi tiết để bạn tự khám phá.

[pause] Từ đây là spoiler arc cuối của manga, chưa lên anime. Nếu bạn muốn chờ, hãy tua tới chương Toàn bộ bậc thang.

[pause] Khoảng một năm sau arc Spade, Asta thua trong trận với Lucius, kẻ thù cuối cùng. Cậu bị đưa tới Vùng đất Mặt Trời, quê hương của đội trưởng Yami.

[pause] Ở đó, Asta học một kỹ thuật tên Zetten từ Ichika, em gái Yami: biến Khí thành một điểm năng lượng cực nhỏ, rồi bùng nổ trong một nhát chém duy nhất.

[pause] Ở Vùng đất Mặt Trời, Asta còn học cách chiến đấu bằng kiếm theo phong cách mới, cùng những kiếm sĩ bản địa. Một cậu bé từ làng Hage đi nửa vòng thế giới để quay về với chính mình.

[pause] Và thú vị nhất: Zetten không cần phép thuật. Nó quay về gốc rễ của Asta: cơ thể, luyện tập, và Khí. Nấc cao nhất lại giống nấc đầu tiên nhất.

[pause] Arc cuối vẫn đang được kể trong manga. Kaku sẽ không nói trước kết quả.
```

### c08 · Toàn bộ bậc thang / Góc nhìn của Kaku / Kết

Khoảng 127 giây · cảnh s72–s83 · 1647 ký tự

**Gemini**

```text
Và đây là toàn bộ bậc thang của Asta. Nấc không: không có gì, chỉ có cơ thể. Nấc một: grimoire năm lá và kiếm phản ma thuật.

<short pause> Nấc hai: Khí và đôi tay được chữa. Nấc ba: Dạng Đen lần đầu. Nấc bốn: Dạng Đen hoàn chỉnh cùng Nacht.

<short pause> Nấc năm: Ác ma hợp thể cùng Liebe. Và nấc cuối, trong arc cuối: Zetten, quay về gốc rễ.

<short pause> Và mỗi nấc cũng có một cái giá: bị coi thường, suýt mất đôi tay, bị nghi ngờ, bị ác ma chiếm lấy, và gánh cả niềm tin của một người anh em. Không nấc nào miễn phí.

<short pause> Nhìn cả bậc thang, Kaku thấy một điều: mỗi nấc sức mạnh của Asta đều đến từ một mối quan hệ. Yami dạy Khí. Nữ hoàng phù thủy chữa tay. Nacht huấn luyện. Liebe là anh em. Ichika dạy Zetten.

<short pause> Black Clover thường bị nói là một bộ shounen truyền thống: nhân vật chính hét to, không bỏ cuộc. Đúng vậy. <short pause> Nhưng bậc thang của Asta có một thông điệp sâu hơn.

<short pause> Nếu bạn đang cảm thấy mình không có tài năng gì đặc biệt, Asta là lời nhắc: không có ma lực vẫn có thể leo, chỉ cần không dừng lại, và không ngại nắm lấy bàn tay người khác.

<short pause> Người không có gì không leo lên một mình. Cậu leo lên nhờ những người, và cả những ác ma, chịu đưa tay ra cho cậu.

<short pause> Và cậu cũng đưa tay ra cho người khác, kể cả cho một ác ma bị cả địa ngục bắt nạt. <laugh> Kaku nghĩ đó mới là phép thuật thật sự của Asta.

<short pause> Bạn thích nấc nào nhất trên bậc thang của Asta? Và nếu có một ác ma trong grimoire của bạn, bạn muốn nó là ai? Viết vào bình luận nhé.

<short pause> Video tiếp theo, Kaku mở một cuốn sổ đáng sợ: Death Note. Luật của cuốn sổ, và những cách mà các nhân vật đã phá luật.

<short pause> Nếu video này tiếp thêm cho bạn chút động lực, hãy đăng ký kênh. Không có phép thuật cũng không sao, chỉ cần leo từng nấc một. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và đây là toàn bộ bậc thang của Asta. Nấc không: không có gì, chỉ có cơ thể. Nấc một: grimoire năm lá và kiếm phản ma thuật.

[pause] Nấc hai: Khí và đôi tay được chữa. Nấc ba: Dạng Đen lần đầu. Nấc bốn: Dạng Đen hoàn chỉnh cùng Nacht.

[pause] Nấc năm: Ác ma hợp thể cùng Liebe. Và nấc cuối, trong arc cuối: Zetten, quay về gốc rễ.

[pause] Và mỗi nấc cũng có một cái giá: bị coi thường, suýt mất đôi tay, bị nghi ngờ, bị ác ma chiếm lấy, và gánh cả niềm tin của một người anh em. Không nấc nào miễn phí.

[pause] Nhìn cả bậc thang, Kaku thấy một điều: mỗi nấc sức mạnh của Asta đều đến từ một mối quan hệ. Yami dạy Khí. Nữ hoàng phù thủy chữa tay. Nacht huấn luyện. Liebe là anh em. Ichika dạy Zetten.

[pause] Black Clover thường bị nói là một bộ shounen truyền thống: nhân vật chính hét to, không bỏ cuộc. Đúng vậy. [pause] Nhưng bậc thang của Asta có một thông điệp sâu hơn.

[pause] Nếu bạn đang cảm thấy mình không có tài năng gì đặc biệt, Asta là lời nhắc: không có ma lực vẫn có thể leo, chỉ cần không dừng lại, và không ngại nắm lấy bàn tay người khác.

[pause] Người không có gì không leo lên một mình. Cậu leo lên nhờ những người, và cả những ác ma, chịu đưa tay ra cho cậu.

[pause] Và cậu cũng đưa tay ra cho người khác, kể cả cho một ác ma bị cả địa ngục bắt nạt. [chuckles] Kaku nghĩ đó mới là phép thuật thật sự của Asta.

[pause] [curious] Bạn thích nấc nào nhất trên bậc thang của Asta? Và nếu có một ác ma trong grimoire của bạn, bạn muốn nó là ai? Viết vào bình luận nhé.

[pause] Video tiếp theo, Kaku mở một cuốn sổ đáng sợ: Death Note. Luật của cuốn sổ, và những cách mà các nhân vật đã phá luật.

[pause] Nếu video này tiếp thêm cho bạn chút động lực, hãy đăng ký kênh. Không có phép thuật cũng không sao, chỉ cần leo từng nấc một. Kaku gấp sổ đây, hẹn gặp lại!
```
