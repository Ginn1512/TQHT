# Bộ prompt · Dragon Ball: Xếp hạng các vị thần từ Thượng Đế tới Toàn Vương

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 8 đoạn đọc, khoảng 15.9 phút giọng.
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

Lời: Cảnh báo: video có spoiler Dragon Ball Super tới hết Giải đấu Sức mạnh. Bản làm lại Dragon Ball Super: Beerus…

```text
Wide 16:9 landscape cinematic frame. a vast starry sky above a quiet mountain peak with a closed notebook resting on a rock, wide establishing shot, deep navy night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong Dragon Ball có một vị thần có thể xóa sổ cả một vũ trụ, với hàng tỉ hành tinh và sự sống, chỉ bằng một…

```text
Wide 16:9 landscape cinematic frame. an entire spiral galaxy dissolving into sparkles of light, a tiny glowing hand silhouette in the foreground, wide cosmic shot, violet and gold light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Và vị thần đó lại cư xử như một đứa trẻ, thích chơi, thích có bạn, và đôi khi chẳng biết mình vừa làm điều kh…

```text
Wide 16:9 landscape cinematic frame. a tiny cute round silhouette sitting on an enormous throne swinging its legs, surrounded by vast emptiness, wide shot, soft surreal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng trước khi lên tới đỉnh, có cả một bậc thang các vị thần: từ vị thần chăm lo cho Trái Đất, tới những vị…

```text
Wide 16:9 landscape cinematic frame. a colossal staircase spiraling up through clouds into space, small glowing thrones placed at different heights, wide low-angle shot, amber and violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình xếp hạng các vị thần trong Dragon Ball, từ thấp lên cao. Và như mọi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at the bottom of a giant cosmic staircase holding a clipboard, looking up with determination. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Bốn tiêu chí chấm điểm

Lời: Tiêu chí thứ nhất là sức mạnh: nếu phải chiến đấu, vị thần này mạnh tới đâu. Tiêu chí thứ hai là quyền hạn: h…

```text
Wide 16:9 landscape cinematic frame. a scorecard on parchment with four empty rows, the first two marked with a fist icon and a crown icon, top-down shot, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Tiêu chí thứ ba là phạm vi: họ trông coi một hành tinh, một góc vũ trụ, cả vũ trụ, hay toàn bộ các vũ trụ.

```text
Wide 16:9 landscape cinematic frame. concentric circles drawn on a chalkboard: a planet, a quadrant, a galaxy, and many galaxies, diagram style, amber chalk. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Tiêu chí thứ tư hơi đặc biệt: sự tự do. Có vị thần mạnh nhưng bị ràng buộc bởi luật lệ hoặc bởi mạng sống của…

```text
Wide 16:9 landscape cinematic frame. a powerful silhouette with faint glowing chains around its wrists, close-up, dramatic rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Vì sao cần bốn tiêu chí? Vì nếu chỉ xếp theo sức mạnh, bảng sẽ rất nhàm chán: ai đánh mạnh hơn thì đứng trên.…

```text
Wide 16:9 landscape cinematic frame. a single tall bar chart labeled with a fist icon looking dull next to a richer four-part chart, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mỗi tiêu chí chấm từ một tới năm điểm, tối đa hai mươi điểm. Kaku chỉ xếp các chức vụ thần, không xếp các nhâ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a scoreboard labeled with a maximum of 20, two small popcorn buckets on empty seats beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Một điều quan trọng trước khi bắt đầu: trong Dragon Ball, thần là một chức vụ. Không phải cứ là thần thì mạnh…

```text
Wide 16:9 landscape cinematic frame. a simple office nameplate with a small halo drawn above it lying on a desk, close-up, soft light, humorous tone. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Hạng 8: Thần Trái Đất

Lời: Bậc thấp nhất là Thần Trái Đất, người ta quen gọi là Thượng Đế. Ông sống trên một cung điện lơ lửng trên trời…

```text
Wide 16:9 landscape cinematic frame. a small white palace floating on a platform high above the clouds, a garden with palm trees, wide shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Thành tựu lớn nhất của chức vụ này là tạo ra bộ Ngọc Rồng của Trái Đất. Bảy viên ngọc, gom đủ thì gọi được rồ…

```text
Wide 16:9 landscape cinematic frame. seven small glowing orange orbs arranged in a circle on a stone floor, each with tiny red stars inside, top-down shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Điểm thú vị là Thần Trái Đất không phải người Trái Đất. Người giữ chức đầu tiên trong truyện và người kế nhiệ…

```text
Wide 16:9 landscape cinematic frame. a calm green-skinned alien elder silhouette with antennae standing at the edge of a sky palace looking down, back view, soft light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và vị Thượng Đế đầu tiên có một bí mật. Để trở thành thần, ông đã tách phần ác trong mình ra ngoài. Phần ác ấ…

```text
Wide 16:9 landscape cinematic frame. a calm elder silhouette with a dark shadow tearing away from his body and taking the shape of a menacing demon, dramatic split lighting, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Hai người vốn là một, nên sinh mạng cũng gắn liền. Nếu Đại Ma Vương chết, Thượng Đế cũng chết theo. Một chức…

```text
Wide 16:9 landscape cinematic frame. two figures, one light and one dark, standing back to back with a single thread connecting them, wide shot, grey dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Chấm điểm: sức mạnh một điểm, vì nhiều chiến binh phàm trần đã vượt xa. Quyền hạn hai điểm. Phạm vi một điểm,…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 1, 2, 1, 2 with a total of 6, pinned on a cloud-shaped board, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Chi tiết cuối cùng này rất quan trọng: nếu người giữ chức chết, ngọc rồng cũng biến thành đá. Kaku ghi chú: đ…

```text
Wide 16:9 landscape cinematic frame. seven orbs turning into plain grey stones one by one, close-up, fading light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Hạng 7: Giới Vương

Lời: Bước lên một bậc là các Giới Vương. Vũ trụ được chia làm bốn phương Bắc, Nam, Đông, Tây, mỗi phương có một Gi…

```text
Wide 16:9 landscape cinematic frame. a galaxy divided into four quadrants by glowing lines, a tiny planet marked in each quadrant, top-down diagram, navy and amber. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Người quen thuộc nhất là Bắc Giới Vương, sống trên một hành tinh nhỏ xíu với trọng lực gấp mười lần Trái Đất,…

```text
Wide 16:9 landscape cinematic frame. a tiny round planet with a single house, a car and a tree, a small monkey and a cricket sitting on the grass, wide shot, whimsical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Ông dạy cho nhân vật chính hai kỹ thuật nổi tiếng nhất: Giới Vương Quyền, nhân sức mạnh lên nhiều lần nhưng h…

```text
Wide 16:9 landscape cinematic frame. a fighter surrounded by a red flaming aura, next to a huge sphere of blue energy held above a raised hand, split composition, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và vị thần này rất thích kể chuyện cười. Muốn làm học trò, bạn phải làm ông cười trước. Kaku đã thử, và ông ấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot telling a joke with a tiny microphone while an audience of one small cricket stares blankly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Và vị Giới Vương này còn là một vị thần đã chết. Khi một kẻ thù định tự hủy để phá nổ Trái Đất, nhân vật chín…

```text
Wide 16:9 landscape cinematic frame. a tiny round planet exploding in a flash of light, a small car and a tree flying away comically, wide cosmic shot. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Từ đó ông đội một vòng hào quang trên đầu, giống như mọi người ở thế giới bên kia. Nhưng ông vẫn tiếp tục dạy…

```text
Wide 16:9 landscape cinematic frame. a small figure with a glowing halo above his head sitting on a new little planet, telling a joke to a cricket, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Chấm điểm: sức mạnh một điểm, quyền hạn hai điểm, phạm vi hai điểm, vì trông coi một phần tư vũ trụ. Tự do bố…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 1, 2, 2, 4 with a total of 9, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Hạng 6: Đại Giới Vương

Lời: Trên bốn Giới Vương là Đại Giới Vương, người quản lý cả bốn. Ông sống ở một hành tinh lớn trong thế giới bên…

```text
Wide 16:9 landscape cinematic frame. a large peaceful planet with grand buildings and training grounds, glowing halos floating above the heads of tiny figures, wide shot, golden afterlife light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Ở đó, người chết vẫn được luyện tập, thậm chí tổ chức cả giải đấu võ thuật của thế giới bên kia.

```text
Wide 16:9 landscape cinematic frame. a tournament arena in the clouds with fighters wearing faint halos, crowds cheering, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nhưng Đại Giới Vương cũng như các Giới Vương: đứng trên người phàm về chức vụ, còn về sức mạnh thì đã bị bỏ x…

```text
Wide 16:9 landscape cinematic frame. a small elderly figure in fancy robes watching a much stronger young fighter train, looking impressed, medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Chấm điểm: sức mạnh một điểm, quyền hạn ba điểm, phạm vi hai điểm. Tự do bốn điểm. Tổng mười điểm, chỉ nhỉnh…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 1, 3, 2, 4 with a total of 10, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Kaku ghi chú: ba bậc đầu tiên này đều là những vị thần trông coi, không phải những vị thần chiến đấu. Từ bậc…

```text
Wide 16:9 landscape cinematic frame. a dividing line drawn across the cosmic staircase, lower steps warm and simple, upper steps glowing and intimidating, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Hạng 5: Giới Vương Thần

Lời: Giới Vương Thần là vị thần sáng tạo. Nhiệm vụ của họ là tạo ra các hành tinh, nuôi dưỡng sự sống, và trông co…

```text
Wide 16:9 landscape cinematic frame. a serene figure holding a small glowing newborn planet in cupped hands, a nebula blooming behind, close-up, soft violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Họ có một bảo vật nổi tiếng: đôi bông tai Potara. Hai người mỗi người đeo một chiếc thì sẽ hợp thể thành một…

```text
Wide 16:9 landscape cinematic frame. a pair of round glowing earrings floating side by side above a velvet cushion, extreme close-up, gold highlights. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nhưng về sức mạnh chiến đấu, Giới Vương Thần của vũ trụ bảy lại khá yếu. Chính nhân vật chính đã vượt xa ông…

```text
Wide 16:9 landscape cinematic frame. a nervous small deity silhouette hiding behind a much larger fighter's shadow, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và đây là luật quan trọng nhất ở bậc này: mạng sống của Giới Vương Thần gắn liền với mạng sống của Thần Hủy D…

```text
Wide 16:9 landscape cinematic frame. two figures standing on opposite sides of a bridge, connected by a single glowing thread tied to their hearts, wide shot, violet and amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Ngày xưa vũ trụ bảy có tới năm Giới Vương Thần. Majin Buu đã tiêu diệt hoặc hấp thụ gần hết. Người còn sống s…

```text
Wide 16:9 landscape cinematic frame. five small thrones in a circle, four of them empty and cracked, one occupied by a lone small figure, wide shot, somber violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Ông sau đó hợp thể vĩnh viễn với người hầu Kibito bằng Potara, nên người ta gọi ông là Kibito Thần một thời g…

```text
Wide 16:9 landscape cinematic frame. two silhouettes merging into one in a swirl of light, a pair of earrings glowing at the center, close-up, soft gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Và có cả một vị Lão Giới Vương Thần, sống từ mười lăm đời trước, bị phong ấn trong một thanh kiếm suốt nhiều…

```text
Wide 16:9 landscape cinematic frame. an ancient ornate sword stuck in a stone on a quiet sacred planet, a tiny old figure emerging from a burst of light, wide shot, mystical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải khen: một vị thần bị nhốt trong kiếm suốt bao đời mà ra ngoài việc đầu tiên vẫn là than phiền về gi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot nodding along as a tiny old figure lectures with a raised finger. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Chấm điểm: sức mạnh hai điểm, quyền hạn bốn điểm, phạm vi bốn điểm, cả một vũ trụ. Tự do chỉ một điểm, vì sin…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 2, 4, 4, 1 with a total of 11, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Hạng 4: Thần Hủy Diệt

Lời: Nếu có sáng tạo thì phải có hủy diệt. Mỗi vũ trụ có một Thần Hủy Diệt, và ở vũ trụ bảy, người đó là Beerus.

```text
Wide 16:9 landscape cinematic frame. a dark silhouette sitting on a giant stone throne, eyes glowing faintly, planets drifting in the background, low-angle shot, violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nhiệm vụ của họ là phá hủy các hành tinh để giữ cân bằng với việc sáng tạo. Chiêu mạnh nhất của họ là Hakai,…

```text
Wide 16:9 landscape cinematic frame. a single raised palm with a violet spark, an object in front of it dissolving into drifting light particles, extreme close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Beerus ngủ hàng chục năm liền. Khi thức dậy, ông có thể phá hủy một hành tinh chỉ vì món ăn không hợp khẩu vị…

```text
Wide 16:9 landscape cinematic frame. a sleepy silhouette yawning inside a massive dark temple, a half-eaten bowl of noodles on a table beside the throne, humorous wide shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Arc này chính là thứ đang được làm lại trong Dragon Ball Super: Beerus, với hình ảnh vẽ lại và cách kể mới. N…

```text
Wide 16:9 landscape cinematic frame. a small television on a desk showing a stylized cosmic battle, a calendar beside it marked with a star, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Beerus còn có một người anh em sinh đôi: Champa, Thần Hủy Diệt của vũ trụ sáu. Hai vũ trụ này cũng là cặp son…

```text
Wide 16:9 landscape cinematic frame. two mirrored silhouettes, one thin and one round, standing back to back in front of two twin galaxies, symmetrical composition, violet light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Hai vị thần này từng tổ chức cả một giải đấu giữa hai vũ trụ chỉ để tranh nhau một hành tinh có đồ ăn ngon. K…

```text
Wide 16:9 landscape cinematic frame. a floating arena between two galaxies, a table of steaming dishes set as the prize on a pedestal, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Mỗi vũ trụ đều có một Thần Hủy Diệt riêng, và sức mạnh của họ không bằng nhau. Nghĩa là Thần Hủy Diệt cũng là…

```text
Wide 16:9 landscape cinematic frame. a row of twelve dark throne silhouettes of different sizes on a cosmic bridge, wide shot, violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Đáng nói là Thần Hủy Diệt không thể tự tiện giết Giới Vương Thần, vì chính họ cũng sẽ chết theo. Hai vị thần…

```text
Wide 16:9 landscape cinematic frame. two chess pieces of equal size facing each other on a board, a thread linking their bases, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Chấm điểm: sức mạnh bốn điểm, quyền hạn bốn điểm, phạm vi bốn điểm. Tự do hai điểm, vì sinh mạng gắn với Giới…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 4, 4, 4, 2 with a total of 14, close-up, violet highlights. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Hạng 3: Thiên sứ

Lời: Nếu bạn nghĩ Thần Hủy Diệt đã ở gần đỉnh thì bậc tiếp theo sẽ làm bạn bất ngờ. Bên cạnh mỗi Thần Hủy Diệt luô…

```text
Wide 16:9 landscape cinematic frame. a tall serene attendant silhouette in flowing robes standing calmly behind a seated dark god, backlit, medium shot, cool silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Thiên sứ của vũ trụ bảy là Whis. Ông lo đồ ăn, đánh thức Beerus, và dạy võ. Nhưng thật ra ông mạnh hơn chính…

```text
Wide 16:9 landscape cinematic frame. a calm attendant effortlessly tapping a furious dark silhouette on the back of the neck, humorous medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Các Thiên sứ làm chủ Bản năng vô cực, trạng thái mà cơ thể tự né và tự phản đòn mà không cần suy nghĩ. Đó cũn…

```text
Wide 16:9 landscape cinematic frame. a figure gracefully dodging dozens of incoming attacks with eyes half closed, silver aura flowing like water, dynamic low-angle shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Whis còn có thể quay ngược thời gian ba phút để sửa một sai lầm. Một năng lực mà Takemichi ở video trước chắc…

```text
Wide 16:9 landscape cinematic frame. a pocket watch with its hands spinning backwards exactly three ticks, extreme close-up, silver and amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Mỗi Thần Hủy Diệt có một Thiên sứ riêng, và các Thiên sứ là anh chị em với nhau. Ví dụ Vados, Thiên sứ của vũ…

```text
Wide 16:9 landscape cinematic frame. a line of serene attendant silhouettes standing side by side in flowing robes, each beside a different small galaxy, wide shot, silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nhưng Thiên sứ có một luật khắt khe: phải giữ trung lập, không được tự ý can thiệp vào chuyện của người phàm.

```text
Wide 16:9 landscape cinematic frame. a glowing boundary line drawn on the ground between a watching attendant and a battle raging beyond it, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Chấm điểm: sức mạnh năm điểm, quyền hạn ba điểm, phạm vi bốn điểm. Tự do hai điểm, vì luật trung lập. Tổng mư…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 5, 3, 4, 2 with a total of 14 and a small tie-break note beside it, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Hạng 2: Đại Thần Quan

Lời: Đứng trên tất cả các Thiên sứ là Đại Thần Quan, cha của các Thiên sứ và là người phụ tá trực tiếp của Toàn Vư…

```text
Wide 16:9 landscape cinematic frame. an elder attendant silhouette standing beside an empty tiny throne in a palace floating in white space, wide shot, soft luminous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Ông là người điều hành Giải đấu Sức mạnh, đọc luật, tuyên bố ai bị loại, và truyền đạt ý muốn của Toàn Vương.

```text
Wide 16:9 landscape cinematic frame. a massive floating arena made of stone platforms in a void, dozens of tiny fighters, a calm figure announcing from a high balcony, wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Truyện gợi ý rằng Đại Thần Quan là một trong những sinh vật mạnh nhất đa vũ trụ. Nhưng ông chưa từng thực sự…

```text
Wide 16:9 landscape cinematic frame. a question mark made of light hovering over a calm elder silhouette, close-up, soft glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Có một chi tiết đáng sợ: khi Giải đấu Sức mạnh kết thúc, các Thiên sứ của những vũ trụ bị xóa vẫn còn đó, bìn…

```text
Wide 16:9 landscape cinematic frame. a few serene attendant silhouettes standing calmly on an empty platform while faded outlines of vanished galaxies float behind them, wide shot, cold white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Chấm điểm: sức mạnh năm điểm, quyền hạn năm điểm, phạm vi năm điểm, toàn bộ các vũ trụ. Tự do ba điểm, vì ông…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 5, 5, 5, 3 with a total of 18, close-up, white glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Hạng 1: Toàn Vương

Lời: Và ở đỉnh cao nhất là Toàn Vương Zeno, vua của mọi thứ. Không có vị thần nào ở trên ông.

```text
Wide 16:9 landscape cinematic frame. a tiny glowing throne at the very top of the cosmic staircase, the entire multiverse spread out below like scattered jewels, wide shot, dazzling light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Theo truyện, ngày xưa có mười tám vũ trụ. Một lần Toàn Vương nổi giận, và sáu vũ trụ biến mất. Giờ chỉ còn mư…

```text
Wide 16:9 landscape cinematic frame. eighteen small glowing orbs in a circle, six of them fading into nothing, top-down diagram, cold white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Trong Giải đấu Sức mạnh, các vũ trụ thua cuộc bị xóa sổ ngay tại chỗ, cùng toàn bộ sự sống bên trong. Chỉ bằn…

```text
Wide 16:9 landscape cinematic frame. a glowing orb representing a universe dissolving into light above the arena, tiny spectators frozen in shock, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và có tới hai Toàn Vương. Trong arc tương lai, nhân vật chính mang Toàn Vương của một dòng thời gian khác về,…

```text
Wide 16:9 landscape cinematic frame. two identical tiny glowing figures holding hands on twin thrones, dozens of gods staring in shock below, humorous wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Toàn Vương còn tặng nhân vật chính một cái nút bấm để gọi mình bất cứ lúc nào. Một cái nút có thể mang tới vị…

```text
Wide 16:9 landscape cinematic frame. a small simple button device resting in an open palm, glowing ominously, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nhưng Toàn Vương lại trông và cư xử như một đứa trẻ. Ông vui khi có bạn chơi. Nhân vật chính đối xử với ông n…

```text
Wide 16:9 landscape cinematic frame. a tiny ruler silhouette happily holding a simple handheld button device, while powerful gods kneel nervously around him, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Chấm điểm: sức mạnh năm điểm, quyền hạn năm, phạm vi năm, và tự do năm. Không ai ra lệnh cho ông. Tổng hai mư…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 5, 5, 5, 5 with a total of 20, glowing brightly, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: vị thần mạnh nhất đa vũ trụ lại là người ít hiểu hậu quả nhất. Có lẽ đó là lời châm biếm nhẹ nh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up nervously at a tiny glowing throne, holding its notebook like a shield. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Bảng xếp hạng cuối cùng

Lời: Giờ ghép lại toàn bộ bảng xếp hạng. Từ dưới lên: Thần Trái Đất sáu điểm, Giới Vương chín điểm, Đại Giới Vương…

```text
Wide 16:9 landscape cinematic frame. the lower half of a cosmic staircase with four glowing plaques showing 6, 9, 10 and 11, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Thần Hủy Diệt mười bốn điểm, Thiên sứ mười bốn điểm nhưng thắng nhờ sức mạnh, Đại Thần Quan mười tám điểm, và…

```text
Wide 16:9 landscape cinematic frame. the upper half of the staircase with four brighter plaques showing 14, 14, 18 and 20, wide shot, violet and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Và các cặp sinh mạng gắn liền xuất hiện ở hai nơi: Thượng Đế với Đại Ma Vương ở dưới đáy, Giới Vương Thần với…

```text
Wide 16:9 landscape cinematic frame. a staircase diagram with two pairs of figures linked by glowing threads at the bottom and middle, the top steps free of threads, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nhìn bảng, bạn sẽ thấy một điều lạ: sức mạnh và quyền hạn không đi cùng nhau. Thiên sứ mạnh hơn Thần Hủy Diệt…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a fist icon on one side and a crown icon on the other, not quite level, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và nhiều người phàm đã mạnh hơn cả những vị thần ở nửa dưới bảng. Nhân vật chính và Vegeta vượt xa Giới Vương…

```text
Wide 16:9 landscape cinematic frame. two mortal warrior silhouettes climbing past the lower thrones of the staircase, the lower gods watching in surprise, wide low-angle shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Góc nhìn của Kaku: thần là chức vụ

Lời: Kaku nghĩ đây là điểm hay nhất của hệ thống thần trong Dragon Ball. Thần không phải là đích đến cuối cùng của…

```text
Wide 16:9 landscape cinematic frame. an office-like celestial hall with desks labeled by small icons: planet, quadrant, universe, multiverse, wide shot, soft light, gently humorous. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Tác giả Toriyama nổi tiếng là người không quá coi trọng việc thiết lập mọi thứ thật chặt chẽ. Nhưng chính vì…

```text
Wide 16:9 landscape cinematic frame. a whimsical sketchbook page full of doodled deity silhouettes with funny expressions, close-up, warm paper light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Có thần sáng tạo, thần hủy diệt, thần trông coi, thần phục vụ. Và giống như mọi công việc, có người làm tốt,…

```text
Wide 16:9 landscape cinematic frame. a row of celestial office desks, one occupant snoring with feet on the desk, another busy with stacks of glowing paperwork, humorous wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Chính vì vậy người phàm mới có thể vươn lên ngang hàng với thần bằng luyện tập. Đó là tinh thần xuyên suốt củ…

```text
Wide 16:9 landscape cinematic frame. a mortal warrior training alone on a mountain at dawn, the cosmic staircase faintly visible in the sky above, wide shot, golden sunrise. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đoán nhiều bạn sẽ muốn đẩy Thiên sứ lên trên Đại Thần Quan, hoặc cho Thần Hủy Diệt nhiều điểm tự do hơn.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding two small plaques, hesitating over where to place them on the staircase. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Bạn có đồng ý với bảng xếp hạng này không? Nếu là bạn, bạn sẽ đổi vị trí của ai, và chấm lại tiêu chí nào? Vi…

```text
Wide 16:9 landscape cinematic frame. a blank ranking chart with eight empty slots and a pencil lying on it, top-down shot, inviting warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Kết

Lời: Từ một vị thần trông coi một hành tinh tới một vị vua có thể xóa cả vũ trụ, bậc thang thần thánh của Dragon B…

```text
Wide 16:9 landscape cinematic frame. the whole cosmic staircase seen from far away, glowing softly, with a tiny figure at the bottom looking up, wide shot, calm starlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Nếu bạn đang xem bản làm lại, hãy để ý cách Beerus lần đầu gặp nhân vật chính. Giờ bạn đã biết ông ấy đứng ở…

```text
Wide 16:9 landscape cinematic frame. a dark god silhouette facing a determined mortal fighter, a serene attendant watching calmly from behind, wide shot, dramatic violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku rời vũ trụ thần thánh để tới một thành phố rất con người: Night City, nơi người ta thay…

```text
Wide 16:9 landscape cinematic frame. a rainy futuristic city skyline glowing with neon signs, a silhouette with a glowing mechanical arm in the foreground, wide shot, magenta and cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích bảng xếp hạng có tiêu chí rõ ràng, hãy đăng ký kênh để không bỏ lỡ bảng tiếp theo. Kaku gấp sổ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing politely at the foot of the cosmic staircase and closing its notebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Bốn tiêu chí chấm điểm

Khoảng 125 giây · cảnh s01–s11 · 1626 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Dragon Ball Super tới hết Giải đấu Sức mạnh. Bản làm lại Dragon Ball Super: Beerus đang phát cũng nằm trong phần này, nên bạn yên tâm xem.

<short pause> Trong Dragon Ball có một vị thần có thể xóa sổ cả một vũ trụ, với hàng tỉ hành tinh và sự sống, chỉ bằng một cái giơ tay.

<short pause> Và vị thần đó lại cư xử như một đứa trẻ, thích chơi, thích có bạn, và đôi khi chẳng biết mình vừa làm điều khủng khiếp tới mức nào.

<short pause> Nhưng trước khi lên tới đỉnh, có cả một bậc thang các vị thần: từ vị thần chăm lo cho Trái Đất, tới những vị thần phá hủy các hành tinh chỉ vì mất ngủ.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình xếp hạng các vị thần trong Dragon Ball, từ thấp lên cao. Và như mọi bảng xếp hạng của kênh, Kaku công bố tiêu chí trước.

<short pause> Tiêu chí thứ nhất là sức mạnh: nếu phải chiến đấu, vị thần này mạnh tới đâu. Tiêu chí thứ hai là quyền hạn: họ được phép quyết định những gì.

<short pause> Tiêu chí thứ ba là phạm vi: họ trông coi một hành tinh, một góc vũ trụ, cả vũ trụ, hay toàn bộ các vũ trụ.

<short pause> Tiêu chí thứ tư hơi đặc biệt: sự tự do. Có vị thần mạnh nhưng bị ràng buộc bởi luật lệ hoặc bởi mạng sống của người khác. Ràng buộc càng ít thì điểm càng cao.

<short pause> Vì sao cần bốn tiêu chí? Vì nếu chỉ xếp theo sức mạnh, bảng sẽ rất nhàm chán: ai đánh mạnh hơn thì đứng trên. Còn thần thì không chỉ để đánh nhau.

<short pause> Mỗi tiêu chí chấm từ một tới năm điểm, tối đa hai mươi điểm. Kaku chỉ xếp các chức vụ thần, không xếp các nhân vật phàm trần đã mạnh lên, nên Goku và Vegeta hôm nay chỉ ngồi xem thôi.

<short pause> Một điều quan trọng trước khi bắt đầu: trong Dragon Ball, thần là một chức vụ. Không phải cứ là thần thì mạnh hơn người phàm. Lát nữa bạn sẽ thấy điều này rõ ràng.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Dragon Ball Super tới hết Giải đấu Sức mạnh. Bản làm lại Dragon Ball Super: Beerus đang phát cũng nằm trong phần này, nên bạn yên tâm xem.

[pause] Trong Dragon Ball có một vị thần có thể xóa sổ cả một vũ trụ, với hàng tỉ hành tinh và sự sống, chỉ bằng một cái giơ tay.

[pause] Và vị thần đó lại cư xử như một đứa trẻ, thích chơi, thích có bạn, và đôi khi chẳng biết mình vừa làm điều khủng khiếp tới mức nào.

[pause] Nhưng trước khi lên tới đỉnh, có cả một bậc thang các vị thần: từ vị thần chăm lo cho Trái Đất, tới những vị thần phá hủy các hành tinh chỉ vì mất ngủ.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình xếp hạng các vị thần trong Dragon Ball, từ thấp lên cao. Và như mọi bảng xếp hạng của kênh, Kaku công bố tiêu chí trước.

[pause] Tiêu chí thứ nhất là sức mạnh: nếu phải chiến đấu, vị thần này mạnh tới đâu. Tiêu chí thứ hai là quyền hạn: họ được phép quyết định những gì.

[pause] Tiêu chí thứ ba là phạm vi: họ trông coi một hành tinh, một góc vũ trụ, cả vũ trụ, hay toàn bộ các vũ trụ.

[pause] Tiêu chí thứ tư hơi đặc biệt: sự tự do. Có vị thần mạnh nhưng bị ràng buộc bởi luật lệ hoặc bởi mạng sống của người khác. Ràng buộc càng ít thì điểm càng cao.

[pause] [curious] Vì sao cần bốn tiêu chí? Vì nếu chỉ xếp theo sức mạnh, bảng sẽ rất nhàm chán: ai đánh mạnh hơn thì đứng trên. Còn thần thì không chỉ để đánh nhau.

[pause] Mỗi tiêu chí chấm từ một tới năm điểm, tối đa hai mươi điểm. Kaku chỉ xếp các chức vụ thần, không xếp các nhân vật phàm trần đã mạnh lên, nên Goku và Vegeta hôm nay chỉ ngồi xem thôi.

[pause] Một điều quan trọng trước khi bắt đầu: trong Dragon Ball, thần là một chức vụ. Không phải cứ là thần thì mạnh hơn người phàm. Lát nữa bạn sẽ thấy điều này rõ ràng.
```

### c02 · Hạng 8: Thần Trái Đất

Khoảng 85 giây · cảnh s12–s18 · 1109 ký tự

**Gemini**

```text
Bậc thấp nhất là Thần Trái Đất, người ta quen gọi là Thượng Đế. Ông sống trên một cung điện lơ lửng trên trời và trông chừng một hành tinh duy nhất.

<short pause> Thành tựu lớn nhất của chức vụ này là tạo ra bộ Ngọc Rồng của Trái Đất. Bảy viên ngọc, gom đủ thì gọi được rồng thần để thực hiện điều ước.

<short pause> Điểm thú vị là Thần Trái Đất không phải người Trái Đất. Người giữ chức đầu tiên trong truyện và người kế nhiệm Dende đều là người Namek.

<short pause> Và vị Thượng Đế đầu tiên có một bí mật. Để trở thành thần, ông đã tách phần ác trong mình ra ngoài. Phần ác ấy trở thành Đại Ma Vương Piccolo.

<short pause> Hai người vốn là một, nên sinh mạng cũng gắn liền. Nếu Đại Ma Vương chết, Thượng Đế cũng chết theo. Một chức vụ thiêng liêng được xây trên một vết nứt rất con người.

<short pause> Chấm điểm: sức mạnh một điểm, vì nhiều chiến binh phàm trần đã vượt xa. Quyền hạn hai điểm. Phạm vi một điểm, chỉ một hành tinh. Tự do hai điểm, vì ngọc rồng gắn liền với mạng sống của người tạo ra chúng.

<short pause> Chi tiết cuối cùng này rất quan trọng: nếu người giữ chức chết, ngọc rồng cũng biến thành đá. Kaku ghi chú: đây là lần đầu tiên ta thấy một vị thần bị trói buộc bởi mạng sống.
```

**ElevenLabs**

```text
Bậc thấp nhất là Thần Trái Đất, người ta quen gọi là Thượng Đế. Ông sống trên một cung điện lơ lửng trên trời và trông chừng một hành tinh duy nhất.

[pause] Thành tựu lớn nhất của chức vụ này là tạo ra bộ Ngọc Rồng của Trái Đất. Bảy viên ngọc, gom đủ thì gọi được rồng thần để thực hiện điều ước.

[pause] Điểm thú vị là Thần Trái Đất không phải người Trái Đất. Người giữ chức đầu tiên trong truyện và người kế nhiệm Dende đều là người Namek.

[pause] Và vị Thượng Đế đầu tiên có một bí mật. Để trở thành thần, ông đã tách phần ác trong mình ra ngoài. Phần ác ấy trở thành Đại Ma Vương Piccolo.

[pause] Hai người vốn là một, nên sinh mạng cũng gắn liền. Nếu Đại Ma Vương chết, Thượng Đế cũng chết theo. Một chức vụ thiêng liêng được xây trên một vết nứt rất con người.

[pause] Chấm điểm: sức mạnh một điểm, vì nhiều chiến binh phàm trần đã vượt xa. Quyền hạn hai điểm. Phạm vi một điểm, chỉ một hành tinh. Tự do hai điểm, vì ngọc rồng gắn liền với mạng sống của người tạo ra chúng.

[pause] Chi tiết cuối cùng này rất quan trọng: nếu người giữ chức chết, ngọc rồng cũng biến thành đá. Kaku ghi chú: đây là lần đầu tiên ta thấy một vị thần bị trói buộc bởi mạng sống.
```

### c03 · Hạng 7: Giới Vương / Hạng 6: Đại Giới Vương

Khoảng 138 giây · cảnh s19–s30 · 1792 ký tự

**Gemini**

```text
Bước lên một bậc là các Giới Vương. Vũ trụ được chia làm bốn phương Bắc, Nam, Đông, Tây, mỗi phương có một Giới Vương trông coi.

<short pause> Người quen thuộc nhất là Bắc Giới Vương, sống trên một hành tinh nhỏ xíu với trọng lực gấp mười lần Trái Đất, cùng một chú khỉ và một con dế.

<short pause> Ông dạy cho nhân vật chính hai kỹ thuật nổi tiếng nhất: Giới Vương Quyền, nhân sức mạnh lên nhiều lần nhưng hành hạ cơ thể, và Genki Dama, gom năng lượng của mọi sinh vật.

<short pause> Và vị thần này rất thích kể chuyện cười. Muốn làm học trò, bạn phải làm ông cười trước. <laugh> Kaku đã thử, và ông ấy chỉ gật đầu lịch sự.

<short pause> Và vị Giới Vương này còn là một vị thần đã chết. Khi một kẻ thù định tự hủy để phá nổ Trái Đất, nhân vật chính dịch chuyển hắn tới hành tinh của Giới Vương. Cả hành tinh nhỏ biến mất.

<short pause> Từ đó ông đội một vòng hào quang trên đầu, giống như mọi người ở thế giới bên kia. <short pause> Nhưng ông vẫn tiếp tục dạy học và kể chuyện cười như chưa có gì xảy ra.

<short pause> Chấm điểm: sức mạnh một điểm, quyền hạn hai điểm, phạm vi hai điểm, vì trông coi một phần tư vũ trụ. Tự do bốn điểm, vì không bị ràng buộc gì đặc biệt. Tổng chín điểm.

<short pause> Trên bốn Giới Vương là Đại Giới Vương, người quản lý cả bốn. Ông sống ở một hành tinh lớn trong thế giới bên kia, nơi những chiến binh xuất sắc đã qua đời được giữ lại thân xác.

<short pause> Ở đó, người chết vẫn được luyện tập, thậm chí tổ chức cả giải đấu võ thuật của thế giới bên kia.

<short pause> Nhưng Đại Giới Vương cũng như các Giới Vương: đứng trên người phàm về chức vụ, còn về sức mạnh thì đã bị bỏ xa. Ở thế giới Dragon Ball, chức vụ không tự làm bạn mạnh lên.

<short pause> Chấm điểm: sức mạnh một điểm, quyền hạn ba điểm, phạm vi hai điểm. Tự do bốn điểm. Tổng mười điểm, chỉ nhỉnh hơn Giới Vương một chút.

<short pause> Kaku ghi chú: ba bậc đầu tiên này đều là những vị thần trông coi, không phải những vị thần chiến đấu. Từ bậc tiếp theo, mọi thứ bắt đầu khác.
```

**ElevenLabs**

```text
Bước lên một bậc là các Giới Vương. Vũ trụ được chia làm bốn phương Bắc, Nam, Đông, Tây, mỗi phương có một Giới Vương trông coi.

[pause] Người quen thuộc nhất là Bắc Giới Vương, sống trên một hành tinh nhỏ xíu với trọng lực gấp mười lần Trái Đất, cùng một chú khỉ và một con dế.

[pause] Ông dạy cho nhân vật chính hai kỹ thuật nổi tiếng nhất: Giới Vương Quyền, nhân sức mạnh lên nhiều lần nhưng hành hạ cơ thể, và Genki Dama, gom năng lượng của mọi sinh vật.

[pause] Và vị thần này rất thích kể chuyện cười. Muốn làm học trò, bạn phải làm ông cười trước. [chuckles] Kaku đã thử, và ông ấy chỉ gật đầu lịch sự.

[pause] Và vị Giới Vương này còn là một vị thần đã chết. Khi một kẻ thù định tự hủy để phá nổ Trái Đất, nhân vật chính dịch chuyển hắn tới hành tinh của Giới Vương. Cả hành tinh nhỏ biến mất.

[pause] Từ đó ông đội một vòng hào quang trên đầu, giống như mọi người ở thế giới bên kia. [pause] Nhưng ông vẫn tiếp tục dạy học và kể chuyện cười như chưa có gì xảy ra.

[pause] Chấm điểm: sức mạnh một điểm, quyền hạn hai điểm, phạm vi hai điểm, vì trông coi một phần tư vũ trụ. Tự do bốn điểm, vì không bị ràng buộc gì đặc biệt. Tổng chín điểm.

[pause] Trên bốn Giới Vương là Đại Giới Vương, người quản lý cả bốn. Ông sống ở một hành tinh lớn trong thế giới bên kia, nơi những chiến binh xuất sắc đã qua đời được giữ lại thân xác.

[pause] Ở đó, người chết vẫn được luyện tập, thậm chí tổ chức cả giải đấu võ thuật của thế giới bên kia.

[pause] Nhưng Đại Giới Vương cũng như các Giới Vương: đứng trên người phàm về chức vụ, còn về sức mạnh thì đã bị bỏ xa. Ở thế giới Dragon Ball, chức vụ không tự làm bạn mạnh lên.

[pause] Chấm điểm: sức mạnh một điểm, quyền hạn ba điểm, phạm vi hai điểm. Tự do bốn điểm. Tổng mười điểm, chỉ nhỉnh hơn Giới Vương một chút.

[pause] Kaku ghi chú: ba bậc đầu tiên này đều là những vị thần trông coi, không phải những vị thần chiến đấu. Từ bậc tiếp theo, mọi thứ bắt đầu khác.
```

### c04 · Hạng 5: Giới Vương Thần

Khoảng 102 giây · cảnh s31–s39 · 1321 ký tự

**Gemini**

```text
Giới Vương Thần là vị thần sáng tạo. Nhiệm vụ của họ là tạo ra các hành tinh, nuôi dưỡng sự sống, và trông coi cả thế giới người sống lẫn thế giới bên kia.

<short pause> Họ có một bảo vật nổi tiếng: đôi bông tai Potara. Hai người mỗi người đeo một chiếc thì sẽ hợp thể thành một chiến binh mạnh hơn nhiều.

<short pause> Nhưng về sức mạnh chiến đấu, Giới Vương Thần của vũ trụ bảy lại khá yếu. Chính nhân vật chính đã vượt xa ông từ thời arc Majin Buu.

<short pause> Và đây là luật quan trọng nhất ở bậc này: mạng sống của Giới Vương Thần gắn liền với mạng sống của Thần Hủy Diệt cùng vũ trụ. Một người chết thì người kia cũng chết theo.

<short pause> Ngày xưa vũ trụ bảy có tới năm Giới Vương Thần. Majin Buu đã tiêu diệt hoặc hấp thụ gần hết. Người còn sống sót là Giới Vương Thần phương Đông.

<short pause> Ông sau đó hợp thể vĩnh viễn với người hầu Kibito bằng Potara, nên người ta gọi ông là Kibito Thần một thời gian.

<short pause> Và có cả một vị Lão Giới Vương Thần, sống từ mười lăm đời trước, bị phong ấn trong một thanh kiếm suốt nhiều thiên niên kỷ. Ông biết cách đánh thức sức mạnh tiềm ẩn của người khác.

<short pause> <laugh> Kaku phải khen: một vị thần bị nhốt trong kiếm suốt bao đời mà ra ngoài việc đầu tiên vẫn là than phiền về giới trẻ. Kaku thấy thân quen lạ lùng.

<short pause> Chấm điểm: sức mạnh hai điểm, quyền hạn bốn điểm, phạm vi bốn điểm, cả một vũ trụ. Tự do chỉ một điểm, vì sinh mạng bị ràng buộc. Tổng mười một điểm.
```

**ElevenLabs**

```text
Giới Vương Thần là vị thần sáng tạo. Nhiệm vụ của họ là tạo ra các hành tinh, nuôi dưỡng sự sống, và trông coi cả thế giới người sống lẫn thế giới bên kia.

[pause] Họ có một bảo vật nổi tiếng: đôi bông tai Potara. Hai người mỗi người đeo một chiếc thì sẽ hợp thể thành một chiến binh mạnh hơn nhiều.

[pause] Nhưng về sức mạnh chiến đấu, Giới Vương Thần của vũ trụ bảy lại khá yếu. Chính nhân vật chính đã vượt xa ông từ thời arc Majin Buu.

[pause] Và đây là luật quan trọng nhất ở bậc này: mạng sống của Giới Vương Thần gắn liền với mạng sống của Thần Hủy Diệt cùng vũ trụ. Một người chết thì người kia cũng chết theo.

[pause] Ngày xưa vũ trụ bảy có tới năm Giới Vương Thần. Majin Buu đã tiêu diệt hoặc hấp thụ gần hết. Người còn sống sót là Giới Vương Thần phương Đông.

[pause] Ông sau đó hợp thể vĩnh viễn với người hầu Kibito bằng Potara, nên người ta gọi ông là Kibito Thần một thời gian.

[pause] Và có cả một vị Lão Giới Vương Thần, sống từ mười lăm đời trước, bị phong ấn trong một thanh kiếm suốt nhiều thiên niên kỷ. Ông biết cách đánh thức sức mạnh tiềm ẩn của người khác.

[pause] [chuckles] Kaku phải khen: một vị thần bị nhốt trong kiếm suốt bao đời mà ra ngoài việc đầu tiên vẫn là than phiền về giới trẻ. Kaku thấy thân quen lạ lùng.

[pause] Chấm điểm: sức mạnh hai điểm, quyền hạn bốn điểm, phạm vi bốn điểm, cả một vũ trụ. Tự do chỉ một điểm, vì sinh mạng bị ràng buộc. Tổng mười một điểm.
```

### c05 · Hạng 4: Thần Hủy Diệt

Khoảng 101 giây · cảnh s40–s48 · 1317 ký tự

**Gemini**

```text
Nếu có sáng tạo thì phải có hủy diệt. Mỗi vũ trụ có một Thần Hủy Diệt, và ở vũ trụ bảy, người đó là Beerus.

<short pause> Nhiệm vụ của họ là phá hủy các hành tinh để giữ cân bằng với việc sáng tạo. Chiêu mạnh nhất của họ là Hakai, xóa một thứ khỏi sự tồn tại.

<short pause> Beerus ngủ hàng chục năm liền. Khi thức dậy, ông có thể phá hủy một hành tinh chỉ vì món ăn không hợp khẩu vị. Và ông đã tìm tới Trái Đất vì một giấc mơ về Thần Saiyan.

<short pause> Arc này chính là thứ đang được làm lại trong Dragon Ball Super: Beerus, với hình ảnh vẽ lại và cách kể mới. Nếu bạn đang xem, bạn đang ở ngay bậc thứ tư của bảng xếp hạng này.

<short pause> Beerus còn có một người anh em sinh đôi: Champa, Thần Hủy Diệt của vũ trụ sáu. Hai vũ trụ này cũng là cặp song sinh.

<short pause> Hai vị thần này từng tổ chức cả một giải đấu giữa hai vũ trụ chỉ để tranh nhau một hành tinh có đồ ăn ngon. Kaku nghĩ nếu cả hai ăn chung thì đỡ tốn công hơn.

<short pause> Mỗi vũ trụ đều có một Thần Hủy Diệt riêng, và sức mạnh của họ không bằng nhau. Nghĩa là Thần Hủy Diệt cũng là một chức vụ, và có người làm tốt hơn người khác.

<short pause> Đáng nói là Thần Hủy Diệt không thể tự tiện giết Giới Vương Thần, vì chính họ cũng sẽ chết theo. Hai vị thần kìm hãm lẫn nhau.

<short pause> Chấm điểm: sức mạnh bốn điểm, quyền hạn bốn điểm, phạm vi bốn điểm. Tự do hai điểm, vì sinh mạng gắn với Giới Vương Thần và vẫn phải nghe lệnh cấp trên. Tổng mười bốn điểm.
```

**ElevenLabs**

```text
Nếu có sáng tạo thì phải có hủy diệt. Mỗi vũ trụ có một Thần Hủy Diệt, và ở vũ trụ bảy, người đó là Beerus.

[pause] Nhiệm vụ của họ là phá hủy các hành tinh để giữ cân bằng với việc sáng tạo. Chiêu mạnh nhất của họ là Hakai, xóa một thứ khỏi sự tồn tại.

[pause] Beerus ngủ hàng chục năm liền. Khi thức dậy, ông có thể phá hủy một hành tinh chỉ vì món ăn không hợp khẩu vị. Và ông đã tìm tới Trái Đất vì một giấc mơ về Thần Saiyan.

[pause] Arc này chính là thứ đang được làm lại trong Dragon Ball Super: Beerus, với hình ảnh vẽ lại và cách kể mới. Nếu bạn đang xem, bạn đang ở ngay bậc thứ tư của bảng xếp hạng này.

[pause] Beerus còn có một người anh em sinh đôi: Champa, Thần Hủy Diệt của vũ trụ sáu. Hai vũ trụ này cũng là cặp song sinh.

[pause] Hai vị thần này từng tổ chức cả một giải đấu giữa hai vũ trụ chỉ để tranh nhau một hành tinh có đồ ăn ngon. Kaku nghĩ nếu cả hai ăn chung thì đỡ tốn công hơn.

[pause] Mỗi vũ trụ đều có một Thần Hủy Diệt riêng, và sức mạnh của họ không bằng nhau. Nghĩa là Thần Hủy Diệt cũng là một chức vụ, và có người làm tốt hơn người khác.

[pause] Đáng nói là Thần Hủy Diệt không thể tự tiện giết Giới Vương Thần, vì chính họ cũng sẽ chết theo. Hai vị thần kìm hãm lẫn nhau.

[pause] Chấm điểm: sức mạnh bốn điểm, quyền hạn bốn điểm, phạm vi bốn điểm. Tự do hai điểm, vì sinh mạng gắn với Giới Vương Thần và vẫn phải nghe lệnh cấp trên. Tổng mười bốn điểm.
```

### c06 · Hạng 3: Thiên sứ / Hạng 2: Đại Thần Quan

Khoảng 137 giây · cảnh s49–s60 · 1785 ký tự

**Gemini**

```text
Nếu bạn nghĩ Thần Hủy Diệt đã ở gần đỉnh thì bậc tiếp theo sẽ làm bạn bất ngờ. Bên cạnh mỗi Thần Hủy Diệt luôn có một Thiên sứ, vừa là người hầu, vừa là thầy dạy, vừa là người trông chừng.

<short pause> Thiên sứ của vũ trụ bảy là Whis. Ông lo đồ ăn, đánh thức Beerus, và dạy võ. <short pause> Nhưng thật ra ông mạnh hơn chính vị thần mà ông phục vụ.

<short pause> Các Thiên sứ làm chủ Bản năng vô cực, trạng thái mà cơ thể tự né và tự phản đòn mà không cần suy nghĩ. Đó cũng là trạng thái nhân vật chính mất rất lâu mới chạm tới.

<short pause> Whis còn có thể quay ngược thời gian ba phút để sửa một sai lầm. Một năng lực mà Takemichi ở video trước chắc sẽ rất ghen tị.

<short pause> Mỗi Thần Hủy Diệt có một Thiên sứ riêng, và các Thiên sứ là anh chị em với nhau. Ví dụ Vados, Thiên sứ của vũ trụ sáu, là chị của Whis.

<short pause> Nhưng Thiên sứ có một luật khắt khe: phải giữ trung lập, không được tự ý can thiệp vào chuyện của người phàm.

<short pause> Chấm điểm: sức mạnh năm điểm, quyền hạn ba điểm, phạm vi bốn điểm. Tự do hai điểm, vì luật trung lập. Tổng mười bốn điểm, bằng với Thần Hủy Diệt, nhưng Kaku xếp Thiên sứ cao hơn vì sức mạnh vượt trội.

<short pause> Đứng trên tất cả các Thiên sứ là Đại Thần Quan, cha của các Thiên sứ và là người phụ tá trực tiếp của Toàn Vương.

<short pause> Ông là người điều hành Giải đấu Sức mạnh, đọc luật, tuyên bố ai bị loại, và truyền đạt ý muốn của Toàn Vương.

<short pause> Truyện gợi ý rằng Đại Thần Quan là một trong những sinh vật mạnh nhất đa vũ trụ. <short pause> Nhưng ông chưa từng thực sự ra tay, nên con số chính xác là điều fan vẫn tranh luận.

<short pause> Có một chi tiết đáng sợ: khi Giải đấu Sức mạnh kết thúc, các Thiên sứ của những vũ trụ bị xóa vẫn còn đó, bình thản như chưa có gì xảy ra. Họ phục vụ trật tự, không phục vụ một vũ trụ cụ thể.

<short pause> Chấm điểm: sức mạnh năm điểm, quyền hạn năm điểm, phạm vi năm điểm, toàn bộ các vũ trụ. Tự do ba điểm, vì ông vẫn phục vụ Toàn Vương. Tổng mười tám điểm.
```

**ElevenLabs**

```text
Nếu bạn nghĩ Thần Hủy Diệt đã ở gần đỉnh thì bậc tiếp theo sẽ làm bạn bất ngờ. Bên cạnh mỗi Thần Hủy Diệt luôn có một Thiên sứ, vừa là người hầu, vừa là thầy dạy, vừa là người trông chừng.

[pause] Thiên sứ của vũ trụ bảy là Whis. Ông lo đồ ăn, đánh thức Beerus, và dạy võ. [pause] Nhưng thật ra ông mạnh hơn chính vị thần mà ông phục vụ.

[pause] Các Thiên sứ làm chủ Bản năng vô cực, trạng thái mà cơ thể tự né và tự phản đòn mà không cần suy nghĩ. Đó cũng là trạng thái nhân vật chính mất rất lâu mới chạm tới.

[pause] Whis còn có thể quay ngược thời gian ba phút để sửa một sai lầm. Một năng lực mà Takemichi ở video trước chắc sẽ rất ghen tị.

[pause] Mỗi Thần Hủy Diệt có một Thiên sứ riêng, và các Thiên sứ là anh chị em với nhau. Ví dụ Vados, Thiên sứ của vũ trụ sáu, là chị của Whis.

[pause] Nhưng Thiên sứ có một luật khắt khe: phải giữ trung lập, không được tự ý can thiệp vào chuyện của người phàm.

[pause] Chấm điểm: sức mạnh năm điểm, quyền hạn ba điểm, phạm vi bốn điểm. Tự do hai điểm, vì luật trung lập. Tổng mười bốn điểm, bằng với Thần Hủy Diệt, nhưng Kaku xếp Thiên sứ cao hơn vì sức mạnh vượt trội.

[pause] Đứng trên tất cả các Thiên sứ là Đại Thần Quan, cha của các Thiên sứ và là người phụ tá trực tiếp của Toàn Vương.

[pause] Ông là người điều hành Giải đấu Sức mạnh, đọc luật, tuyên bố ai bị loại, và truyền đạt ý muốn của Toàn Vương.

[pause] Truyện gợi ý rằng Đại Thần Quan là một trong những sinh vật mạnh nhất đa vũ trụ. [pause] Nhưng ông chưa từng thực sự ra tay, nên con số chính xác là điều fan vẫn tranh luận.

[pause] Có một chi tiết đáng sợ: khi Giải đấu Sức mạnh kết thúc, các Thiên sứ của những vũ trụ bị xóa vẫn còn đó, bình thản như chưa có gì xảy ra. Họ phục vụ trật tự, không phục vụ một vũ trụ cụ thể.

[pause] Chấm điểm: sức mạnh năm điểm, quyền hạn năm điểm, phạm vi năm điểm, toàn bộ các vũ trụ. Tự do ba điểm, vì ông vẫn phục vụ Toàn Vương. Tổng mười tám điểm.
```

### c07 · Hạng 1: Toàn Vương / Bảng xếp hạng cuối cùng

Khoảng 144 giây · cảnh s61–s73 · 1868 ký tự

**Gemini**

```text
Và ở đỉnh cao nhất là Toàn Vương Zeno, vua của mọi thứ. Không có vị thần nào ở trên ông.

<short pause> Theo truyện, ngày xưa có mười tám vũ trụ. Một lần Toàn Vương nổi giận, và sáu vũ trụ biến mất. Giờ chỉ còn mười hai.

<short pause> Trong Giải đấu Sức mạnh, các vũ trụ thua cuộc bị xóa sổ ngay tại chỗ, cùng toàn bộ sự sống bên trong. Chỉ bằng một cái giơ tay.

<short pause> Và có tới hai Toàn Vương. Trong arc tương lai, nhân vật chính mang Toàn Vương của một dòng thời gian khác về, vì nghĩ Toàn Vương hiện tại sẽ vui khi có bạn chơi.

<short pause> Toàn Vương còn tặng nhân vật chính một cái nút bấm để gọi mình bất cứ lúc nào. Một cái nút có thể mang tới vị thần xóa sổ vũ trụ. Kaku mà có thì chắc không dám để trong túi áo.

<short pause> Nhưng Toàn Vương lại trông và cư xử như một đứa trẻ. Ông vui khi có bạn chơi. Nhân vật chính đối xử với ông như một người bạn, và điều đó vừa buồn cười vừa đáng sợ.

<short pause> Chấm điểm: sức mạnh năm điểm, quyền hạn năm, phạm vi năm, và tự do năm. Không ai ra lệnh cho ông. Tổng hai mươi điểm tuyệt đối.

<short pause> <laugh> Kaku ghi chú: vị thần mạnh nhất đa vũ trụ lại là người ít hiểu hậu quả nhất. Có lẽ đó là lời châm biếm nhẹ nhàng của tác giả về quyền lực tuyệt đối.

<short pause> Giờ ghép lại toàn bộ bảng xếp hạng. Từ dưới lên: Thần Trái Đất sáu điểm, Giới Vương chín điểm, Đại Giới Vương mười điểm, Giới Vương Thần mười một điểm.

<short pause> Thần Hủy Diệt mười bốn điểm, Thiên sứ mười bốn điểm nhưng thắng nhờ sức mạnh, Đại Thần Quan mười tám điểm, và Toàn Vương hai mươi điểm.

<short pause> Và các cặp sinh mạng gắn liền xuất hiện ở hai nơi: Thượng Đế với Đại Ma Vương ở dưới đáy, Giới Vương Thần với Thần Hủy Diệt ở giữa. Càng lên cao, các vị thần càng ít bị ràng buộc.

<short pause> Nhìn bảng, bạn sẽ thấy một điều lạ: sức mạnh và quyền hạn không đi cùng nhau. Thiên sứ mạnh hơn Thần Hủy Diệt nhưng lại phục vụ họ.

<short pause> Và nhiều người phàm đã mạnh hơn cả những vị thần ở nửa dưới bảng. Nhân vật chính và Vegeta vượt xa Giới Vương Thần từ lâu, và đã từng chạm tay tới sức mạnh của thần.
```

**ElevenLabs**

```text
Và ở đỉnh cao nhất là Toàn Vương Zeno, vua của mọi thứ. Không có vị thần nào ở trên ông.

[pause] Theo truyện, ngày xưa có mười tám vũ trụ. Một lần Toàn Vương nổi giận, và sáu vũ trụ biến mất. Giờ chỉ còn mười hai.

[pause] Trong Giải đấu Sức mạnh, các vũ trụ thua cuộc bị xóa sổ ngay tại chỗ, cùng toàn bộ sự sống bên trong. Chỉ bằng một cái giơ tay.

[pause] Và có tới hai Toàn Vương. Trong arc tương lai, nhân vật chính mang Toàn Vương của một dòng thời gian khác về, vì nghĩ Toàn Vương hiện tại sẽ vui khi có bạn chơi.

[pause] Toàn Vương còn tặng nhân vật chính một cái nút bấm để gọi mình bất cứ lúc nào. Một cái nút có thể mang tới vị thần xóa sổ vũ trụ. Kaku mà có thì chắc không dám để trong túi áo.

[pause] Nhưng Toàn Vương lại trông và cư xử như một đứa trẻ. Ông vui khi có bạn chơi. Nhân vật chính đối xử với ông như một người bạn, và điều đó vừa buồn cười vừa đáng sợ.

[pause] Chấm điểm: sức mạnh năm điểm, quyền hạn năm, phạm vi năm, và tự do năm. Không ai ra lệnh cho ông. Tổng hai mươi điểm tuyệt đối.

[pause] [chuckles] Kaku ghi chú: vị thần mạnh nhất đa vũ trụ lại là người ít hiểu hậu quả nhất. Có lẽ đó là lời châm biếm nhẹ nhàng của tác giả về quyền lực tuyệt đối.

[pause] Giờ ghép lại toàn bộ bảng xếp hạng. Từ dưới lên: Thần Trái Đất sáu điểm, Giới Vương chín điểm, Đại Giới Vương mười điểm, Giới Vương Thần mười một điểm.

[pause] Thần Hủy Diệt mười bốn điểm, Thiên sứ mười bốn điểm nhưng thắng nhờ sức mạnh, Đại Thần Quan mười tám điểm, và Toàn Vương hai mươi điểm.

[pause] Và các cặp sinh mạng gắn liền xuất hiện ở hai nơi: Thượng Đế với Đại Ma Vương ở dưới đáy, Giới Vương Thần với Thần Hủy Diệt ở giữa. Càng lên cao, các vị thần càng ít bị ràng buộc.

[pause] Nhìn bảng, bạn sẽ thấy một điều lạ: sức mạnh và quyền hạn không đi cùng nhau. Thiên sứ mạnh hơn Thần Hủy Diệt nhưng lại phục vụ họ.

[pause] Và nhiều người phàm đã mạnh hơn cả những vị thần ở nửa dưới bảng. Nhân vật chính và Vegeta vượt xa Giới Vương Thần từ lâu, và đã từng chạm tay tới sức mạnh của thần.
```

### c08 · Góc nhìn của Kaku: thần là chức vụ / Kết

Khoảng 123 giây · cảnh s74–s83 · 1599 ký tự

**Gemini**

```text
Kaku nghĩ đây là điểm hay nhất của hệ thống thần trong Dragon Ball. Thần không phải là đích đến cuối cùng của sức mạnh. Thần là một công việc.

<short pause> Tác giả Toriyama nổi tiếng là người không quá coi trọng việc thiết lập mọi thứ thật chặt chẽ. <short pause> Nhưng chính vì vậy, các vị thần của ông mới có tính cách: lười, háu ăn, trẻ con, hay giận dỗi.

<short pause> Có thần sáng tạo, thần hủy diệt, thần trông coi, thần phục vụ. Và giống như mọi công việc, có người làm tốt, có người lười, có người ngủ gật suốt nhiều năm.

<short pause> Chính vì vậy người phàm mới có thể vươn lên ngang hàng với thần bằng luyện tập. Đó là tinh thần xuyên suốt của Dragon Ball: không ai sinh ra đã ở trên đỉnh, ngoại trừ một người thích chơi.

<short pause> <laugh> Kaku đoán nhiều bạn sẽ muốn đẩy Thiên sứ lên trên Đại Thần Quan, hoặc cho Thần Hủy Diệt nhiều điểm tự do hơn. Cứ tranh luận thoải mái, miễn là có lý do.

<short pause> Bạn có đồng ý với bảng xếp hạng này không? Nếu là bạn, bạn sẽ đổi vị trí của ai, và chấm lại tiêu chí nào? Viết bảng của bạn vào bình luận nhé.

<short pause> Từ một vị thần trông coi một hành tinh tới một vị vua có thể xóa cả vũ trụ, bậc thang thần thánh của Dragon Ball cho ta thấy một điều: quyền lực càng lớn thì càng cần người biết giữ nó.

<short pause> Nếu bạn đang xem bản làm lại, hãy để ý cách Beerus lần đầu gặp nhân vật chính. Giờ bạn đã biết ông ấy đứng ở bậc nào, và ai đang đứng ngay phía sau ông.

<short pause> Video tiếp theo, Kaku rời vũ trụ thần thánh để tới một thành phố rất con người: Night City, nơi người ta thay tay chân bằng máy móc và phải trả giá bằng chính tâm trí.

<short pause> Nếu bạn thích bảng xếp hạng có tiêu chí rõ ràng, hãy đăng ký kênh để không bỏ lỡ bảng tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Kaku nghĩ đây là điểm hay nhất của hệ thống thần trong Dragon Ball. Thần không phải là đích đến cuối cùng của sức mạnh. Thần là một công việc.

[pause] Tác giả Toriyama nổi tiếng là người không quá coi trọng việc thiết lập mọi thứ thật chặt chẽ. [pause] Nhưng chính vì vậy, các vị thần của ông mới có tính cách: lười, háu ăn, trẻ con, hay giận dỗi.

[pause] Có thần sáng tạo, thần hủy diệt, thần trông coi, thần phục vụ. Và giống như mọi công việc, có người làm tốt, có người lười, có người ngủ gật suốt nhiều năm.

[pause] Chính vì vậy người phàm mới có thể vươn lên ngang hàng với thần bằng luyện tập. Đó là tinh thần xuyên suốt của Dragon Ball: không ai sinh ra đã ở trên đỉnh, ngoại trừ một người thích chơi.

[pause] [chuckles] Kaku đoán nhiều bạn sẽ muốn đẩy Thiên sứ lên trên Đại Thần Quan, hoặc cho Thần Hủy Diệt nhiều điểm tự do hơn. Cứ tranh luận thoải mái, miễn là có lý do.

[pause] [curious] Bạn có đồng ý với bảng xếp hạng này không? Nếu là bạn, bạn sẽ đổi vị trí của ai, và chấm lại tiêu chí nào? Viết bảng của bạn vào bình luận nhé.

[pause] Từ một vị thần trông coi một hành tinh tới một vị vua có thể xóa cả vũ trụ, bậc thang thần thánh của Dragon Ball cho ta thấy một điều: quyền lực càng lớn thì càng cần người biết giữ nó.

[pause] Nếu bạn đang xem bản làm lại, hãy để ý cách Beerus lần đầu gặp nhân vật chính. Giờ bạn đã biết ông ấy đứng ở bậc nào, và ai đang đứng ngay phía sau ông.

[pause] Video tiếp theo, Kaku rời vũ trụ thần thánh để tới một thành phố rất con người: Night City, nơi người ta thay tay chân bằng máy móc và phải trả giá bằng chính tâm trí.

[pause] Nếu bạn thích bảng xếp hạng có tiêu chí rõ ràng, hãy đăng ký kênh để không bỏ lỡ bảng tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```
