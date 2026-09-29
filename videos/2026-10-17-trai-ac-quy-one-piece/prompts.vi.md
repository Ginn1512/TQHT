# Bộ prompt · One Piece: Hồ sơ trái ác quỷ — 3 loại, thức tỉnh và bí mật của Luffy

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 94 ảnh, 7 đoạn đọc, khoảng 15.0 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (94 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler One Piece đến hết arc Wano, gồm cả bí mật về trái ác quỷ của Luffy. Nếu chưa xem t…

```text
Wide 16:9 landscape cinematic frame. a mysterious swirled fruit on a velvet cushion inside a dark treasure room, single spotlight. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một quả trái cây vị kinh khủng, ăn một miếng là đổi cả đời. Bạn có thể biến thành lửa, thành cao su, thành rồ…

```text
Wide 16:9 landscape cinematic frame. a hand reaching toward a glowing swirled fruit, reflections of fire, dragons, and gravity waves in its skin. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng cái giá là mãi mãi không bơi được, trong một thế giới mà gần như mọi thứ đều diễn ra trên biển.

```text
Wide 16:9 landscape cinematic frame. a figure sinking helplessly into deep blue ocean, bubbles rising, light fading above. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Hôm nay mình sẽ làm một cuốn hồ sơ bách khoa về trái ác quỷ: phân loại, quy tắc, điểm yếu, thức tỉnh, và nhữn…

```text
Wide 16:9 landscape cinematic frame. an old leather-bound encyclopedia opening to pages filled with fruit illustrations. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ của mình sẽ thành một cuốn bách khoa, và bạn là người đọc đầu tiê…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny archivist cap, opening a thick encyclopedia. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao Luffy thực ra chưa bao giờ ăn trái Cao su, và vì sao đó là bí mật được che…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over a fruit illustration with a hidden label. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Hồ sơ 1: những quy tắc chung

Lời: Trước khi phân loại, hãy ghi lại những quy tắc mà mọi trái ác quỷ đều tuân theo.

```text
Wide 16:9 landscape cinematic frame. a rulebook page with numbered glowing clauses and a fruit seal at the top. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Quy tắc một: ăn trái ác quỷ, người đó nhận năng lực ngay lập tức, nhưng biển cả sẽ từ chối họ. Rơi xuống biển…

```text
Wide 16:9 landscape cinematic frame. a person falling into the sea, energy draining from their body like dissolving light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Không chỉ biển. Nước đọng như bồn tắm hay vũng nước sâu cũng làm họ yếu đi. Nước chảy như mưa thì không sao.

```text
Wide 16:9 landscape cinematic frame. a figure slumping weakly in a bathtub, while another figure stands fine under pouring rain. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Quy tắc hai: mỗi người chỉ ăn được một trái. Ăn trái thứ hai, cơ thể sẽ nổ tung. Đây là điều truyện nói tới l…

```text
Wide 16:9 landscape cinematic frame. two fruits side by side with a large red warning cross between them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Quy tắc ba: khi người dùng chết, năng lực không mất đi. Nó tái sinh vào một trái cây khác ở đâu đó trên thế g…

```text
Wide 16:9 landscape cinematic frame. a glowing essence rising from a fallen figure and drifting across the ocean into a distant ordinary fruit. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Quy tắc bốn: mỗi năng lực là duy nhất. Không bao giờ có hai người cùng lúc sở hữu cùng một trái ác quỷ.

```text
Wide 16:9 landscape cinematic frame. a single glowing fruit in a vast empty vault, no duplicates anywhere. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Và một chi tiết đời thường: trái ác quỷ được miêu tả là có vị cực kỳ tệ. Ai ăn cũng phải nhăn mặt.

```text
Wide 16:9 landscape cinematic frame. a comic-style figure grimacing after one bite of a swirled fruit, sweat drops flying. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: vì năng lực tái sinh và mỗi trái là duy nhất, trái ác quỷ cực kỳ đắt giá. Trong truyện, một trá…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring wide-eyed at a mountain of gold coins beside a single fruit. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Hồ sơ 2: ba loại trái ác quỷ

Lời: Trái ác quỷ được chia làm ba loại chính: Siêu nhân, Động vật và Tự nhiên. Mỗi loại có điểm mạnh và điểm yếu r…

```text
Wide 16:9 landscape cinematic frame. a classification chart with three large cards: a strange body icon, an animal icon, and an elemental icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Siêu nhân là nhóm đông nhất và đa dạng nhất. Nó cho cơ thể một năng lực đặc biệt, tác động lên chính mình hoặ…

```text
Wide 16:9 landscape cinematic frame. a gallery of strange abilities: a stretching arm, a body splitting into pieces, glowing barriers. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Có trái biến cơ thể thành lưỡi dao, có trái tạo ra kết giới, có trái điều khiển linh hồn, có trái làm mọi thứ…

```text
Wide 16:9 landscape cinematic frame. four small vignettes: blades emerging from arms, a shimmering barrier, a ghost-like glow, a floating boulder. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Động vật cho phép biến thành một con vật, hoặc dạng nửa người nửa thú. Người dùng tăng mạnh thể lực và sức bề…

```text
Wide 16:9 landscape cinematic frame. a figure mid-transformation into a large beast, half human, half animal silhouette. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Động vật có hai nhánh đặc biệt: loại cổ đại, biến thành những sinh vật đã tuyệt chủng như khủng long, và loại…

```text
Wide 16:9 landscape cinematic frame. a split image: a giant prehistoric beast on one side, a mythical phoenix-like bird of blue flame on the other. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Tự nhiên là nhóm hiếm nhất. Người dùng biến cơ thể thành một nguyên tố như lửa, băng, sét, cát hay khói, và đ…

```text
Wide 16:9 landscape cinematic frame. a figure dissolving into swirling sand, another into crackling lightning, another into ice. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Điểm mạnh lớn nhất của Tự nhiên: đòn đánh thường xuyên qua người họ. Chém vào lửa thì chỉ chém vào không khí.

```text
Wide 16:9 landscape cinematic frame. a sword passing harmlessly through a figure made of fire, sparks scattering. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku tóm lại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Không loại nào tuyệt đối mạnh nhất,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot arranging three cards on a table like a card game. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Hồ sơ: những năng lực kinh điển

Lời: Một cuốn hồ sơ thì không thể thiếu vài mục tiêu biểu. Dưới đây là những năng lực mà gần như fan One Piece nào…

```text
Wide 16:9 landscape cinematic frame. an encyclopedia spread with eight illustrated fruit cards arranged in a grid. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Ở nhóm Tự nhiên, có trái Lửa biến người dùng thành ngọn lửa sống, có trái Cát hút khô mọi thứ nó chạm vào, có…

```text
Wide 16:9 landscape cinematic frame. three elemental figures side by side: blazing fire, swirling desert sand, crackling lightning. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Có cả trái Băng, đủ sức đóng băng cả một vùng biển, và trái Khói, dùng để bắt giữ thay vì tiêu diệt.

```text
Wide 16:9 landscape cinematic frame. a vast frozen sea with a single figure standing on it, and a figure made of smoke wrapping around a runaway. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Ở nhóm Siêu nhân, trái Phòng mổ cho phép tạo ra một vùng mà người dùng cắt, ghép, hoán đổi mọi thứ bên trong…

```text
Wide 16:9 landscape cinematic frame. a translucent blue dome where objects are sliced and rearranged in mid-air like surgery. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Có trái Chỉ, biến sợi chỉ thành vũ khí sắc bén và cả công cụ điều khiển người khác như con rối.

```text
Wide 16:9 landscape cinematic frame. thin glowing strings slicing through a building and controlling puppet-like silhouettes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Ở nhóm Động vật thần thoại, có trái biến người dùng thành phượng hoàng lửa xanh với khả năng hồi phục mọi vết…

```text
Wide 16:9 landscape cinematic frame. a majestic bird of blue flames spreading its wings over a burning battlefield, wounds healing in its light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và có trái biến người dùng thành rồng phương Đông khổng lồ, bay lượn và phun lửa, được xem là một trong những…

```text
Wide 16:9 landscape cinematic frame. a colossal eastern dragon coiling through storm clouds above a mountain fortress. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: mình cố ý không liệt kê hết, vì One Piece có hàng trăm trái ác quỷ. Nếu bạn muốn một video riên…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting under an endless tower of fruit cards, overwhelmed but smiling. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Hồ sơ 3: điểm yếu

Lời: Mọi trái ác quỷ đều có điểm yếu, ngoài việc không bơi được. Hiểu điểm yếu là cách để kẻ yếu hơn đánh bại kẻ m…

```text
Wide 16:9 landscape cinematic frame. a detective board with a fruit in the center and red strings connecting to several weakness icons. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Điểm yếu lớn nhất là hải lâu thạch, một loại đá phát ra năng lượng giống biển cả. Chạm vào nó, người dùng mất…

```text
Wide 16:9 landscape cinematic frame. a set of blue-grey stone shackles glowing faintly, a figure weakened while wearing them. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Hải quân dùng hải lâu thạch làm còng tay, song sắt nhà tù và cả đáy tàu, để người có năng lực không thể dùng…

```text
Wide 16:9 landscape cinematic frame. a prison cell with bars of blue-grey stone and a ship hull lined with the same stone. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Với người Tự nhiên, điểm yếu thứ hai là Haki vũ trang. Như mình đã giải thích ở video trước, Haki chạm được v…

```text
Wide 16:9 landscape cinematic frame. a black-coated fist striking through smoke and hitting a solid figure hidden inside. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Ngoài ra, mỗi trái còn có điểm yếu riêng theo tính chất. Một người cao su không sợ sét, nhưng lại sợ vật sắc…

```text
Wide 16:9 landscape cinematic frame. a rubbery figure shrugging off a lightning bolt, then flinching from a sharp spear. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Có những người Tự nhiên bị khắc chế bởi nguyên tố khác. Cát sợ nước, vì cát ướt thì không còn hóa được thành…

```text
Wide 16:9 landscape cinematic frame. a figure made of sand becoming heavy and solid when splashed with water. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: chính những điểm yếu này làm trận đấu thú vị. Không có năng lực nào vô địch, chỉ có người biết…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small water bottle and a grain of sand, grinning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Hồ sơ 4: thức tỉnh

Lời: Ở mức cao nhất, người dùng trái ác quỷ có thể đạt tới thức tỉnh, một trạng thái mà năng lực vượt xa bình thườ…

```text
Wide 16:9 landscape cinematic frame. a fruit cracking open to release a burst of light, surrounded by swirling energy. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Với Siêu nhân, thức tỉnh cho phép năng lực tác động lên môi trường xung quanh, không chỉ cơ thể người dùng. M…

```text
Wide 16:9 landscape cinematic frame. a city street transforming into waves of strange material spreading outward from a figure. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Với Động vật, thức tỉnh tăng mạnh sức bền và khả năng hồi phục. Người dùng gần như không biết mệt, nhưng có n…

```text
Wide 16:9 landscape cinematic frame. a beast-form figure with glowing eyes standing up again and again despite heavy wounds. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Với Tự nhiên, truyện chưa nói nhiều về thức tỉnh. Đây là phần mà fan vẫn đang chờ, nên mình sẽ không suy đoán…

```text
Wide 16:9 landscape cinematic frame. a question mark made of swirling elements floating above an elemental figure. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Truyện nhấn mạnh rằng thức tỉnh không phải thời gian mà là sự trưởng thành của người dùng. Khi cơ thể và tinh…

```text
Wide 16:9 landscape cinematic frame. a figure standing at a doorway of light, their shadow growing larger behind them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ví von: thức tỉnh giống như việc bạn chơi một nhạc cụ đủ lâu, tới một ngày bạn không còn đánh từng nốt m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot playing a tiny lute with glowing notes flowing into the air. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Hồ sơ 5: bí mật trái ác quỷ của Luffy

Lời: Và giờ là bí mật lớn nhất. Suốt hơn một nghìn chương, ai cũng nghĩ Luffy ăn trái Cao su, một loại Siêu nhân.

```text
Wide 16:9 landscape cinematic frame. a pirate compass resting on a closed book titled only with a rubber-band icon. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nhưng ở Wano, sự thật được tiết lộ: đó thật ra là một trái Động vật thần thoại, mang hình dạng của Thần Mặt T…

```text
Wide 16:9 landscape cinematic frame. a silhouette with flowing white hair and clouds around him, laughing against a bright sun. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Theo truyện, Chính phủ Thế giới đã đổi tên trái này thành trái Cao su trong nhiều thế kỷ để che giấu nó, vì h…

```text
Wide 16:9 landscape cinematic frame. an old official document with a name crossed out and replaced, stamped with a seal. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Khi thức tỉnh, Luffy vào trạng thái mà fan gọi là Gear 5: cơ thể trở nên tự do như trong hoạt hình, biến mọi…

```text
Wide 16:9 landscape cinematic frame. a cartoonish world where the ground bounces like rubber and a joyful figure laughs freely. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Điều này lý giải một câu hỏi fan đặt ra từ lâu: vì sao một trái Siêu nhân nghe có vẻ bình thường lại được cả…

```text
Wide 16:9 landscape cinematic frame. a group of shadowy officials around a table looking at a single glowing fruit. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: đây là một trong những cú lật lớn nhất của One Piece. Nó biến năng lực của nhân vật chính từ t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot laughing freely with its feathers turning a little white and fluffy. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Hồ sơ 6: trái ác quỷ nhân tạo

Lời: Nếu trái ác quỷ hiếm như vậy, liệu có thể tạo ra chúng không? Truyện cho thấy câu trả lời là có, nhưng với cá…

```text
Wide 16:9 landscape cinematic frame. a laboratory with glass tanks containing glowing artificial fruits, eerie green light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Một loại trái nhân tạo được sản xuất hàng loạt ở Wano, cho người ăn khả năng mang đặc điểm của một con vật, n…

```text
Wide 16:9 landscape cinematic frame. rows of crates filled with artificial fruits in a dark warehouse. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nhưng tỉ lệ thành công rất thấp. Theo truyện, chỉ khoảng một phần mười người ăn nhận được năng lực.

```text
Wide 16:9 landscape cinematic frame. a pie chart with a tiny glowing slice and a large grey remainder. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Những người thất bại không nhận được gì, mà còn mất khả năng thể hiện mọi cảm xúc ngoại trừ tiếng cười. Họ cư…

```text
Wide 16:9 landscape cinematic frame. a crowd of silhouettes forced to smile while tears run down their faces, somber mood. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Đây là một trong những chi tiết buồn nhất của arc Wano. Nó cho thấy sức mạnh nhân tạo không thể thay thế thứ…

```text
Wide 16:9 landscape cinematic frame. a village at dusk with empty laughing masks hanging on a fence. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Hồ sơ 7: Tự nhiên có thật sự mạnh nhất?

Lời: Nhiều fan mới thường nghĩ Tự nhiên là loại mạnh nhất vì không bị đánh trúng. Nhưng thực tế trong truyện phức…

```text
Wide 16:9 landscape cinematic frame. a debate stage with three podiums marked by fruit-type icons. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Ở nửa đầu truyện, Tự nhiên đúng là cực mạnh vì ít ai biết Haki. Nhưng ở Tân Thế Giới, hầu hết cao thủ đều có…

```text
Wide 16:9 landscape cinematic frame. a figure made of smoke confidently dodging, then being struck by a black fist in a harsher sea. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Trong khi đó, nhiều người dùng Siêu nhân và Động vật thần thoại lại chứng minh sức mạnh ngang hoặc hơn, nhờ n…

```text
Wide 16:9 landscape cinematic frame. a mythical creature of blue flames and a figure bending space facing a lightning figure on equal ground. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Kết luận: loại trái không quyết định ai mạnh nhất. Người dùng, Haki, và sự sáng tạo trong cách dùng mới là th…

```text
Wide 16:9 landscape cinematic frame. a scale with a fruit on one side and a brain plus a glowing fist on the other, the second side heavier. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hãy nhìn các trận đấu lớn ở Tân Thế Giới: phần thắng thường thuộc về người đọc được đối thủ, dùng Haki tốt và…

```text
Wide 16:9 landscape cinematic frame. two fighters circling each other on a cliff, reading each other's stance, tension in the air. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Một người Tự nhiên chủ quan có thể thua một kiếm sĩ bình thường biết Haki. Một người Siêu nhân khéo léo có th…

```text
Wide 16:9 landscape cinematic frame. a confident elemental figure caught off guard by a swordsman's black-coated blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Đó cũng là lý do fan tranh cãi không hồi kết về bảng xếp hạng trái ác quỷ. Câu trả lời thật sự luôn là: còn t…

```text
Wide 16:9 landscape cinematic frame. a crowd of fans arguing around a ranking board with fruit icons, some pointing, some laughing. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku bổ sung: có những người không ăn trái nào mà vẫn đứng trên đỉnh thế giới. Trái ác quỷ là lợi thế, không…

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing next to a swordsman silhouette with no fruit, both looking confident. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Thử nghiệm: bạn sẽ chọn trái nào?

Lời: Giờ tới trò chơi yêu thích của fan One Piece: nếu được chọn một trái ác quỷ, bạn sẽ chọn loại nào?

```text
Wide 16:9 landscape cinematic frame. three glowing fruits on pedestals in a dark hall, spotlight on each. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Nếu bạn muốn an toàn và linh hoạt, một trái Siêu nhân hữu dụng trong đời sống, như dịch chuyển hay chữa lành,…

```text
Wide 16:9 landscape cinematic frame. a figure using a gentle glowing ability to heal a wounded bird. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nếu bạn muốn chiến đấu bền bỉ, Động vật, đặc biệt là loại thần thoại, cho bạn thể lực và khả năng hồi phục vư…

```text
Wide 16:9 landscape cinematic frame. a figure transforming into a phoenix-like bird of blue flame, wounds closing instantly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Nếu bạn muốn sức mạnh lớn và bạn sẵn sàng học Haki thật giỏi, Tự nhiên vẫn là lựa chọn đầy uy lực.

```text
Wide 16:9 landscape cinematic frame. a figure turning into a massive lightning storm over the sea. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhưng nhớ nhé: dù chọn gì, bạn sẽ không bao giờ bơi được nữa. Với người sống trên biển, đó là cái giá không n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a floatie ring, nervously standing at the edge of a pier. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Sáng tạo: dùng năng lực theo cách không ai nghĩ tới

Lời: Điểm hay nhất của trái ác quỷ không nằm ở năng lực, mà ở cách người dùng sáng tạo với nó.

```text
Wide 16:9 landscape cinematic frame. a figure sketching many different ideas branching from a single fruit icon on a chalkboard. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Luffy là ví dụ rõ nhất. Từ một cơ thể cao su, cậu nghĩ ra cách bơm máu nhanh hơn, thổi phồng xương, hay nén c…

```text
Wide 16:9 landscape cinematic frame. a rubbery figure inflating one arm to giant size while steam rises from his skin. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Có người dùng năng lực tưởng như yếu để làm nên chuyện lớn. Một năng lực tạo lỗ thủng trên tường hay khiến vậ…

```text
Wide 16:9 landscape cinematic frame. a small figure opening a doorway in a solid prison wall with a glowing hand. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Ngược lại, có người sở hữu năng lực mạnh nhưng dùng một cách đơn điệu, và cuối cùng thua người sáng tạo hơn.

```text
Wide 16:9 landscape cinematic frame. a powerful but predictable attacker being outmaneuvered by a clever smaller fighter. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Đây là thông điệp rất One Piece: sức mạnh thật sự là trí tưởng tượng và sự kiên trì, không phải món quà bạn n…

```text
Wide 16:9 landscape cinematic frame. a pirate compass resting on a notebook filled with drawings of new techniques. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku bổ sung: điều này giống ma thuật trong Frieren mà mình từng giải thích. Nhiều bộ truyện khác nhau đều đề…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small spellbook and a small fruit, one in each wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Nguồn gốc: trái ác quỷ đến từ đâu?

Lời: Một câu hỏi lớn vẫn chưa có lời giải trọn vẹn: trái ác quỷ đến từ đâu?

```text
Wide 16:9 landscape cinematic frame. a mysterious glowing tree on a distant island shrouded in mist, question marks in the sky. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Truyện cho biết người ta gọi nó là trái của quỷ biển, vì ăn vào sẽ bị biển cả nguyền rủa. Nhưng vì sao nó tồn…

```text
Wide 16:9 landscape cinematic frame. an old sailor's sketch of a sea devil holding a fruit, drawn on weathered parchment. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Ở những arc gần đây, một nhà khoa học thiên tài đưa ra giả thuyết rằng trái ác quỷ gắn với ước mơ và khao khá…

```text
Wide 16:9 landscape cinematic frame. a scientist silhouette in a futuristic lab looking at a glowing fruit hologram connected to human silhouettes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nếu giả thuyết đó đúng, nó sẽ khớp với chủ đề lớn của One Piece: ước mơ của con người là thứ không thể ngăn c…

```text
Wide 16:9 landscape cinematic frame. a night sky full of glowing dreams drifting upward from a harbor town. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: phần này là giả thuyết, chưa phải sự thật được xác nhận. Khi truyện tiết lộ thêm, mình sẽ làm vide…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a small sign with a question mark and a clock. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Những hiểu lầm về trái ác quỷ

Lời: Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về trái ác quỷ.

```text
Wide 16:9 landscape cinematic frame. a notice board with four cards pinned, each with a red question mark. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Hiểu lầm một: ăn trái ác quỷ là mạnh ngay. Thực tế, người mới ăn thường chưa biết dùng, và phải luyện rất lâu…

```text
Wide 16:9 landscape cinematic frame. a clumsy figure accidentally stretching into a tangled knot after eating a fruit. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hiểu lầm hai: người dùng trái ác quỷ sợ mọi loại nước. Không đúng, họ chỉ yếu trong nước biển và nước đọng. M…

```text
Wide 16:9 landscape cinematic frame. a figure drinking water from a cup happily while rain falls around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Hiểu lầm ba: Động vật là loại yếu nhất. Những Động vật thần thoại và cổ đại thuộc hàng đáng sợ nhất trong tru…

```text
Wide 16:9 landscape cinematic frame. a colossal ancient beast and a mythical flame bird towering over smaller figures. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hiểu lầm bốn: trái ác quỷ là yếu tố quyết định trận đấu. Như mình đã nói, Haki, kỹ năng và sự sáng tạo thường…

```text
Wide 16:9 landscape cinematic frame. a swordsman with no fruit standing firm against a figure with elemental powers. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Góc nhìn của Kaku: vì sao hệ thống này thành công · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn tổng thể, vì sao hệ thống trái ác quỷ lại thành công đến vậy trong suốt hơn hai mươi lăm năm của One Pie…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of old encyclopedias, looking at a glowing map of the world. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Lý do một: nó gần như vô hạn. Mỗi trái là một năng lực mới, nên tác giả luôn có thể tạo ra đối thủ và đồng độ…

```text
Wide 16:9 landscape cinematic frame. an endless shelf of fruit illustrations stretching into the distance. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Lý do hai: nó có luật chung đơn giản. Ai cũng hiểu: không bơi được, sợ hải lâu thạch, chỉ một trái. Luật đơn…

```text
Wide 16:9 landscape cinematic frame. a short rulebook of three lines glowing on a single page. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Lý do ba: nó gắn với bí ẩn lớn của thế giới. Trái ác quỷ không chỉ là năng lực, mà là mảnh ghép của lịch sử b…

```text
Wide 16:9 landscape cinematic frame. a puzzle with one missing piece shaped like a fruit, over an ancient map. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: So với Nen hay Chú lực, trái ác quỷ ít luật hơn về cách dùng, nhưng bù lại bằng sự sáng tạo và bí ẩn. Đó là m…

```text
Wide 16:9 landscape cinematic frame. a hexagon, a dark dome, and a swirled fruit side by side, each glowing in its own color. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Tóm tắt

Lời: Tóm lại: trái ác quỷ cho năng lực ngay lập tức, nhưng lấy đi khả năng bơi. Mỗi người chỉ ăn một trái, và năng…

```text
Wide 16:9 landscape cinematic frame. a summary card with a fruit, a wave with a cross, and a reincarnation arrow. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Có ba loại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Điểm yếu chung là hải lâu thạch và Hak…

```text
Wide 16:9 landscape cinematic frame. three fruit-type cards in a row with small weakness icons under each. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Thức tỉnh là đỉnh cao, và trái của Luffy thực ra là Động vật thần thoại bị giấu tên suốt nhiều thế kỷ.

```text
Wide 16:9 landscape cinematic frame. a burst of white light and laughter rising above a pirate ship's bow. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được ăn một trái ác quỷ, bạn chọn năng lực gì, và bạn có chấp nhận không bao giờ bơi đượ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a fruit in one wing and a swimming ring in the other, undecided. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ giải mã hệ thống cấp bậc thợ săn trong Solo Leveling.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a glowing blue portal with rank letters around it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a thick encyclopedia and waving goodbye on a moonlit ship deck. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hồ sơ 1: những quy tắc chung

Khoảng 128 giây · cảnh s01–s14 · 1660 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler One Piece đến hết arc Wano, gồm cả bí mật về trái ác quỷ của Luffy. Nếu chưa xem tới đó, hãy lưu video lại nhé.

<short pause> Một quả trái cây vị kinh khủng, ăn một miếng là đổi cả đời. Bạn có thể biến thành lửa, thành cao su, thành rồng, hay điều khiển cả trọng lực.

<short pause> Nhưng cái giá là mãi mãi không bơi được, trong một thế giới mà gần như mọi thứ đều diễn ra trên biển.

<short pause> Hôm nay mình sẽ làm một cuốn hồ sơ bách khoa về trái ác quỷ: phân loại, quy tắc, điểm yếu, thức tỉnh, và những trái nhân tạo.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ của mình sẽ thành một cuốn bách khoa, và bạn là người đọc đầu tiên.

<short pause> Xem hết video, bạn sẽ hiểu vì sao Luffy thực ra chưa bao giờ ăn trái Cao su, và vì sao đó là bí mật được che giấu suốt nhiều thế kỷ.

<short pause> Trước khi phân loại, hãy ghi lại những quy tắc mà mọi trái ác quỷ đều tuân theo.

<short pause> Quy tắc một: ăn trái ác quỷ, người đó nhận năng lực ngay lập tức, nhưng biển cả sẽ từ chối họ. Rơi xuống biển, họ mất sức và chìm.

<short pause> Không chỉ biển. Nước đọng như bồn tắm hay vũng nước sâu cũng làm họ yếu đi. Nước chảy như mưa thì không sao.

<short pause> Quy tắc hai: mỗi người chỉ ăn được một trái. Ăn trái thứ hai, cơ thể sẽ nổ tung. Đây là điều truyện nói tới là một quy tắc chết người.

<short pause> Quy tắc ba: khi người dùng chết, năng lực không mất đi. Nó tái sinh vào một trái cây khác ở đâu đó trên thế giới.

<short pause> Quy tắc bốn: mỗi năng lực là duy nhất. Không bao giờ có hai người cùng lúc sở hữu cùng một trái ác quỷ.

<short pause> Và một chi tiết đời thường: trái ác quỷ được miêu tả là có vị cực kỳ tệ. Ai ăn cũng phải nhăn mặt.

<short pause> Kaku ghi chú: vì năng lực tái sinh và mỗi trái là duy nhất, trái ác quỷ cực kỳ đắt giá. Trong truyện, một trái có thể đáng giá cả trăm triệu Beri.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler One Piece đến hết arc Wano, gồm cả bí mật về trái ác quỷ của Luffy. Nếu chưa xem tới đó, hãy lưu video lại nhé.

[pause] Một quả trái cây vị kinh khủng, ăn một miếng là đổi cả đời. Bạn có thể biến thành lửa, thành cao su, thành rồng, hay điều khiển cả trọng lực.

[pause] Nhưng cái giá là mãi mãi không bơi được, trong một thế giới mà gần như mọi thứ đều diễn ra trên biển.

[pause] Hôm nay mình sẽ làm một cuốn hồ sơ bách khoa về trái ác quỷ: phân loại, quy tắc, điểm yếu, thức tỉnh, và những trái nhân tạo.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ của mình sẽ thành một cuốn bách khoa, và bạn là người đọc đầu tiên.

[pause] Xem hết video, bạn sẽ hiểu vì sao Luffy thực ra chưa bao giờ ăn trái Cao su, và vì sao đó là bí mật được che giấu suốt nhiều thế kỷ.

[pause] Trước khi phân loại, hãy ghi lại những quy tắc mà mọi trái ác quỷ đều tuân theo.

[pause] Quy tắc một: ăn trái ác quỷ, người đó nhận năng lực ngay lập tức, nhưng biển cả sẽ từ chối họ. Rơi xuống biển, họ mất sức và chìm.

[pause] Không chỉ biển. Nước đọng như bồn tắm hay vũng nước sâu cũng làm họ yếu đi. Nước chảy như mưa thì không sao.

[pause] Quy tắc hai: mỗi người chỉ ăn được một trái. Ăn trái thứ hai, cơ thể sẽ nổ tung. Đây là điều truyện nói tới là một quy tắc chết người.

[pause] Quy tắc ba: khi người dùng chết, năng lực không mất đi. Nó tái sinh vào một trái cây khác ở đâu đó trên thế giới.

[pause] Quy tắc bốn: mỗi năng lực là duy nhất. Không bao giờ có hai người cùng lúc sở hữu cùng một trái ác quỷ.

[pause] Và một chi tiết đời thường: trái ác quỷ được miêu tả là có vị cực kỳ tệ. Ai ăn cũng phải nhăn mặt.

[pause] Kaku ghi chú: vì năng lực tái sinh và mỗi trái là duy nhất, trái ác quỷ cực kỳ đắt giá. Trong truyện, một trái có thể đáng giá cả trăm triệu Beri.
```

### c02 · Hồ sơ 2: ba loại trái ác quỷ

Khoảng 79 giây · cảnh s15–s22 · 1024 ký tự

**Gemini**

```text
Trái ác quỷ được chia làm ba loại chính: Siêu nhân, Động vật và Tự nhiên. Mỗi loại có điểm mạnh và điểm yếu riêng.

<short pause> Siêu nhân là nhóm đông nhất và đa dạng nhất. Nó cho cơ thể một năng lực đặc biệt, tác động lên chính mình hoặc thế giới xung quanh.

<short pause> Có trái biến cơ thể thành lưỡi dao, có trái tạo ra kết giới, có trái điều khiển linh hồn, có trái làm mọi thứ chạm vào trở nên nhẹ bẫng.

<short pause> Động vật cho phép biến thành một con vật, hoặc dạng nửa người nửa thú. Người dùng tăng mạnh thể lực và sức bền.

<short pause> Động vật có hai nhánh đặc biệt: loại cổ đại, biến thành những sinh vật đã tuyệt chủng như khủng long, và loại thần thoại, biến thành sinh vật huyền thoại.

<short pause> Tự nhiên là nhóm hiếm nhất. Người dùng biến cơ thể thành một nguyên tố như lửa, băng, sét, cát hay khói, và điều khiển nguyên tố đó.

<short pause> Điểm mạnh lớn nhất của Tự nhiên: đòn đánh thường xuyên qua người họ. Chém vào lửa thì chỉ chém vào không khí.

<short pause> <laugh> Kaku tóm lại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Không loại nào tuyệt đối mạnh nhất, tất cả phụ thuộc người dùng.
```

**ElevenLabs**

```text
Trái ác quỷ được chia làm ba loại chính: Siêu nhân, Động vật và Tự nhiên. Mỗi loại có điểm mạnh và điểm yếu riêng.

[pause] Siêu nhân là nhóm đông nhất và đa dạng nhất. Nó cho cơ thể một năng lực đặc biệt, tác động lên chính mình hoặc thế giới xung quanh.

[pause] Có trái biến cơ thể thành lưỡi dao, có trái tạo ra kết giới, có trái điều khiển linh hồn, có trái làm mọi thứ chạm vào trở nên nhẹ bẫng.

[pause] Động vật cho phép biến thành một con vật, hoặc dạng nửa người nửa thú. Người dùng tăng mạnh thể lực và sức bền.

[pause] Động vật có hai nhánh đặc biệt: loại cổ đại, biến thành những sinh vật đã tuyệt chủng như khủng long, và loại thần thoại, biến thành sinh vật huyền thoại.

[pause] Tự nhiên là nhóm hiếm nhất. Người dùng biến cơ thể thành một nguyên tố như lửa, băng, sét, cát hay khói, và điều khiển nguyên tố đó.

[pause] Điểm mạnh lớn nhất của Tự nhiên: đòn đánh thường xuyên qua người họ. Chém vào lửa thì chỉ chém vào không khí.

[pause] [chuckles] Kaku tóm lại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Không loại nào tuyệt đối mạnh nhất, tất cả phụ thuộc người dùng.
```

### c03 · Hồ sơ: những năng lực kinh điển / Hồ sơ 3: điểm yếu

Khoảng 144 giây · cảnh s23–s37 · 1876 ký tự

**Gemini**

```text
Một cuốn hồ sơ thì không thể thiếu vài mục tiêu biểu. Dưới đây là những năng lực mà gần như fan One Piece nào cũng nhớ.

<short pause> Ở nhóm Tự nhiên, có trái Lửa biến người dùng thành ngọn lửa sống, có trái Cát hút khô mọi thứ nó chạm vào, có trái Sét biến người dùng thành tia chớp.

<short pause> Có cả trái Băng, đủ sức đóng băng cả một vùng biển, và trái Khói, dùng để bắt giữ thay vì tiêu diệt.

<short pause> Ở nhóm Siêu nhân, trái Phòng mổ cho phép tạo ra một vùng mà người dùng cắt, ghép, hoán đổi mọi thứ bên trong như một bác sĩ phẫu thuật.

<short pause> Có trái Chỉ, biến sợi chỉ thành vũ khí sắc bén và cả công cụ điều khiển người khác như con rối.

<short pause> Ở nhóm Động vật thần thoại, có trái biến người dùng thành phượng hoàng lửa xanh với khả năng hồi phục mọi vết thương.

<short pause> Và có trái biến người dùng thành rồng phương Đông khổng lồ, bay lượn và phun lửa, được xem là một trong những sinh vật mạnh nhất.

<short pause> <laugh> Kaku ghi chú: mình cố ý không liệt kê hết, vì One Piece có hàng trăm trái ác quỷ. Nếu bạn muốn một video riêng về các trái mạnh nhất, hãy bình luận nhé.

<short pause> Mọi trái ác quỷ đều có điểm yếu, ngoài việc không bơi được. Hiểu điểm yếu là cách để kẻ yếu hơn đánh bại kẻ mạnh hơn.

<short pause> Điểm yếu lớn nhất là hải lâu thạch, một loại đá phát ra năng lượng giống biển cả. Chạm vào nó, người dùng mất năng lực và kiệt sức.

<short pause> Hải quân dùng hải lâu thạch làm còng tay, song sắt nhà tù và cả đáy tàu, để người có năng lực không thể dùng sức mạnh gần đó.

<short pause> Với người Tự nhiên, điểm yếu thứ hai là Haki vũ trang. Như mình đã giải thích ở video trước, Haki chạm được vào thực thể thật của họ.

<short pause> Ngoài ra, mỗi trái còn có điểm yếu riêng theo tính chất. Một người cao su không sợ sét, nhưng lại sợ vật sắc nhọn hoặc sức nóng.

<short pause> Có những người Tự nhiên bị khắc chế bởi nguyên tố khác. Cát sợ nước, vì cát ướt thì không còn hóa được thành cát bay.

<short pause> Kaku ghi chú: chính những điểm yếu này làm trận đấu thú vị. Không có năng lực nào vô địch, chỉ có người biết tận dụng hay không.
```

**ElevenLabs**

```text
Một cuốn hồ sơ thì không thể thiếu vài mục tiêu biểu. Dưới đây là những năng lực mà gần như fan One Piece nào cũng nhớ.

[pause] Ở nhóm Tự nhiên, có trái Lửa biến người dùng thành ngọn lửa sống, có trái Cát hút khô mọi thứ nó chạm vào, có trái Sét biến người dùng thành tia chớp.

[pause] Có cả trái Băng, đủ sức đóng băng cả một vùng biển, và trái Khói, dùng để bắt giữ thay vì tiêu diệt.

[pause] Ở nhóm Siêu nhân, trái Phòng mổ cho phép tạo ra một vùng mà người dùng cắt, ghép, hoán đổi mọi thứ bên trong như một bác sĩ phẫu thuật.

[pause] Có trái Chỉ, biến sợi chỉ thành vũ khí sắc bén và cả công cụ điều khiển người khác như con rối.

[pause] Ở nhóm Động vật thần thoại, có trái biến người dùng thành phượng hoàng lửa xanh với khả năng hồi phục mọi vết thương.

[pause] Và có trái biến người dùng thành rồng phương Đông khổng lồ, bay lượn và phun lửa, được xem là một trong những sinh vật mạnh nhất.

[pause] [chuckles] Kaku ghi chú: mình cố ý không liệt kê hết, vì One Piece có hàng trăm trái ác quỷ. Nếu bạn muốn một video riêng về các trái mạnh nhất, hãy bình luận nhé.

[pause] Mọi trái ác quỷ đều có điểm yếu, ngoài việc không bơi được. Hiểu điểm yếu là cách để kẻ yếu hơn đánh bại kẻ mạnh hơn.

[pause] Điểm yếu lớn nhất là hải lâu thạch, một loại đá phát ra năng lượng giống biển cả. Chạm vào nó, người dùng mất năng lực và kiệt sức.

[pause] Hải quân dùng hải lâu thạch làm còng tay, song sắt nhà tù và cả đáy tàu, để người có năng lực không thể dùng sức mạnh gần đó.

[pause] Với người Tự nhiên, điểm yếu thứ hai là Haki vũ trang. Như mình đã giải thích ở video trước, Haki chạm được vào thực thể thật của họ.

[pause] Ngoài ra, mỗi trái còn có điểm yếu riêng theo tính chất. Một người cao su không sợ sét, nhưng lại sợ vật sắc nhọn hoặc sức nóng.

[pause] Có những người Tự nhiên bị khắc chế bởi nguyên tố khác. Cát sợ nước, vì cát ướt thì không còn hóa được thành cát bay.

[pause] Kaku ghi chú: chính những điểm yếu này làm trận đấu thú vị. Không có năng lực nào vô địch, chỉ có người biết tận dụng hay không.
```

### c04 · Hồ sơ 4: thức tỉnh / Hồ sơ 5: bí mật trái ác quỷ của Luffy

Khoảng 123 giây · cảnh s38–s49 · 1597 ký tự

**Gemini**

```text
Ở mức cao nhất, người dùng trái ác quỷ có thể đạt tới thức tỉnh, một trạng thái mà năng lực vượt xa bình thường.

<short pause> Với Siêu nhân, thức tỉnh cho phép năng lực tác động lên môi trường xung quanh, không chỉ cơ thể người dùng. Mặt đất, tòa nhà cũng biến đổi theo năng lực.

<short pause> Với Động vật, thức tỉnh tăng mạnh sức bền và khả năng hồi phục. Người dùng gần như không biết mệt, nhưng có nguy cơ mất kiểm soát.

<short pause> Với Tự nhiên, truyện chưa nói nhiều về thức tỉnh. Đây là phần mà fan vẫn đang chờ, nên mình sẽ không suy đoán quá nhiều.

<short pause> Truyện nhấn mạnh rằng thức tỉnh không phải thời gian mà là sự trưởng thành của người dùng. Khi cơ thể và tinh thần theo kịp năng lực, nó sẽ thức tỉnh.

<short pause> <laugh> Kaku ví von: thức tỉnh giống như việc bạn chơi một nhạc cụ đủ lâu, tới một ngày bạn không còn đánh từng nốt mà bắt đầu chơi cả bản nhạc.

<short pause> Và giờ là bí mật lớn nhất. Suốt hơn một nghìn chương, ai cũng nghĩ Luffy ăn trái Cao su, một loại Siêu nhân.

<short pause> Nhưng ở Wano, sự thật được tiết lộ: đó thật ra là một trái Động vật thần thoại, mang hình dạng của Thần Mặt Trời Nika.

<short pause> Theo truyện, Chính phủ Thế giới đã đổi tên trái này thành trái Cao su trong nhiều thế kỷ để che giấu nó, vì họ sợ sức mạnh và ý nghĩa của nó.

<short pause> Khi thức tỉnh, Luffy vào trạng thái mà fan gọi là Gear 5: cơ thể trở nên tự do như trong hoạt hình, biến mọi thứ xung quanh thành cao su theo trí tưởng tượng.

<short pause> Điều này lý giải một câu hỏi fan đặt ra từ lâu: vì sao một trái Siêu nhân nghe có vẻ bình thường lại được cả Chính phủ săn lùng.

<short pause> Kaku nhận xét: đây là một trong những cú lật lớn nhất của One Piece. Nó biến năng lực của nhân vật chính từ trò đùa thành biểu tượng của tự do.
```

**ElevenLabs**

```text
Ở mức cao nhất, người dùng trái ác quỷ có thể đạt tới thức tỉnh, một trạng thái mà năng lực vượt xa bình thường.

[pause] Với Siêu nhân, thức tỉnh cho phép năng lực tác động lên môi trường xung quanh, không chỉ cơ thể người dùng. Mặt đất, tòa nhà cũng biến đổi theo năng lực.

[pause] Với Động vật, thức tỉnh tăng mạnh sức bền và khả năng hồi phục. Người dùng gần như không biết mệt, nhưng có nguy cơ mất kiểm soát.

[pause] Với Tự nhiên, truyện chưa nói nhiều về thức tỉnh. Đây là phần mà fan vẫn đang chờ, nên mình sẽ không suy đoán quá nhiều.

[pause] Truyện nhấn mạnh rằng thức tỉnh không phải thời gian mà là sự trưởng thành của người dùng. Khi cơ thể và tinh thần theo kịp năng lực, nó sẽ thức tỉnh.

[pause] [chuckles] Kaku ví von: thức tỉnh giống như việc bạn chơi một nhạc cụ đủ lâu, tới một ngày bạn không còn đánh từng nốt mà bắt đầu chơi cả bản nhạc.

[pause] Và giờ là bí mật lớn nhất. Suốt hơn một nghìn chương, ai cũng nghĩ Luffy ăn trái Cao su, một loại Siêu nhân.

[pause] Nhưng ở Wano, sự thật được tiết lộ: đó thật ra là một trái Động vật thần thoại, mang hình dạng của Thần Mặt Trời Nika.

[pause] Theo truyện, Chính phủ Thế giới đã đổi tên trái này thành trái Cao su trong nhiều thế kỷ để che giấu nó, vì họ sợ sức mạnh và ý nghĩa của nó.

[pause] Khi thức tỉnh, Luffy vào trạng thái mà fan gọi là Gear 5: cơ thể trở nên tự do như trong hoạt hình, biến mọi thứ xung quanh thành cao su theo trí tưởng tượng.

[pause] Điều này lý giải một câu hỏi fan đặt ra từ lâu: vì sao một trái Siêu nhân nghe có vẻ bình thường lại được cả Chính phủ săn lùng.

[pause] Kaku nhận xét: đây là một trong những cú lật lớn nhất của One Piece. Nó biến năng lực của nhân vật chính từ trò đùa thành biểu tượng của tự do.
```

### c05 · Hồ sơ 6: trái ác quỷ nhân tạo / Hồ sơ 7: Tự nhiên có thật sự mạnh nhất?

Khoảng 133 giây · cảnh s50–s62 · 1731 ký tự

**Gemini**

```text
Nếu trái ác quỷ hiếm như vậy, liệu có thể tạo ra chúng không? Truyện cho thấy câu trả lời là có, nhưng với cái giá khủng khiếp.

<short pause> Một loại trái nhân tạo được sản xuất hàng loạt ở Wano, cho người ăn khả năng mang đặc điểm của một con vật, như có sừng hay chân thú mọc ra.

<short pause> Nhưng tỉ lệ thành công rất thấp. Theo truyện, chỉ khoảng một phần mười người ăn nhận được năng lực.

<short pause> Những người thất bại không nhận được gì, mà còn mất khả năng thể hiện mọi cảm xúc ngoại trừ tiếng cười. Họ cười ngay cả khi đau khổ.

<short pause> Đây là một trong những chi tiết buồn nhất của arc Wano. Nó cho thấy sức mạnh nhân tạo không thể thay thế thứ tự nhiên, và kẻ trả giá luôn là người yếu.

<short pause> Nhiều fan mới thường nghĩ Tự nhiên là loại mạnh nhất vì không bị đánh trúng. <short pause> Nhưng thực tế trong truyện phức tạp hơn nhiều.

<short pause> Ở nửa đầu truyện, Tự nhiên đúng là cực mạnh vì ít ai biết Haki. <short pause> Nhưng ở Tân Thế Giới, hầu hết cao thủ đều có Haki, và lợi thế đó mất đi.

<short pause> Trong khi đó, nhiều người dùng Siêu nhân và Động vật thần thoại lại chứng minh sức mạnh ngang hoặc hơn, nhờ năng lực sáng tạo và thức tỉnh.

<short pause> Kết luận: loại trái không quyết định ai mạnh nhất. Người dùng, Haki, và sự sáng tạo trong cách dùng mới là thứ quyết định.

<short pause> Hãy nhìn các trận đấu lớn ở Tân Thế Giới: phần thắng thường thuộc về người đọc được đối thủ, dùng Haki tốt và biết lúc nào nên tung chiêu mạnh nhất.

<short pause> Một người Tự nhiên chủ quan có thể thua một kiếm sĩ bình thường biết Haki. Một người Siêu nhân khéo léo có thể lật ngược thế trận trước kẻ mạnh gấp nhiều lần.

<short pause> Đó cũng là lý do fan tranh cãi không hồi kết về bảng xếp hạng trái ác quỷ. Câu trả lời thật sự luôn là: còn tùy người dùng.

<short pause> <laugh> Kaku bổ sung: có những người không ăn trái nào mà vẫn đứng trên đỉnh thế giới. Trái ác quỷ là lợi thế, không phải điều kiện bắt buộc.
```

**ElevenLabs**

```text
[curious] Nếu trái ác quỷ hiếm như vậy, liệu có thể tạo ra chúng không? Truyện cho thấy câu trả lời là có, nhưng với cái giá khủng khiếp.

[pause] Một loại trái nhân tạo được sản xuất hàng loạt ở Wano, cho người ăn khả năng mang đặc điểm của một con vật, như có sừng hay chân thú mọc ra.

[pause] Nhưng tỉ lệ thành công rất thấp. Theo truyện, chỉ khoảng một phần mười người ăn nhận được năng lực.

[pause] Những người thất bại không nhận được gì, mà còn mất khả năng thể hiện mọi cảm xúc ngoại trừ tiếng cười. Họ cười ngay cả khi đau khổ.

[pause] Đây là một trong những chi tiết buồn nhất của arc Wano. Nó cho thấy sức mạnh nhân tạo không thể thay thế thứ tự nhiên, và kẻ trả giá luôn là người yếu.

[pause] Nhiều fan mới thường nghĩ Tự nhiên là loại mạnh nhất vì không bị đánh trúng. [pause] Nhưng thực tế trong truyện phức tạp hơn nhiều.

[pause] Ở nửa đầu truyện, Tự nhiên đúng là cực mạnh vì ít ai biết Haki. [pause] Nhưng ở Tân Thế Giới, hầu hết cao thủ đều có Haki, và lợi thế đó mất đi.

[pause] Trong khi đó, nhiều người dùng Siêu nhân và Động vật thần thoại lại chứng minh sức mạnh ngang hoặc hơn, nhờ năng lực sáng tạo và thức tỉnh.

[pause] Kết luận: loại trái không quyết định ai mạnh nhất. Người dùng, Haki, và sự sáng tạo trong cách dùng mới là thứ quyết định.

[pause] Hãy nhìn các trận đấu lớn ở Tân Thế Giới: phần thắng thường thuộc về người đọc được đối thủ, dùng Haki tốt và biết lúc nào nên tung chiêu mạnh nhất.

[pause] Một người Tự nhiên chủ quan có thể thua một kiếm sĩ bình thường biết Haki. Một người Siêu nhân khéo léo có thể lật ngược thế trận trước kẻ mạnh gấp nhiều lần.

[pause] Đó cũng là lý do fan tranh cãi không hồi kết về bảng xếp hạng trái ác quỷ. Câu trả lời thật sự luôn là: còn tùy người dùng.

[pause] [chuckles] Kaku bổ sung: có những người không ăn trái nào mà vẫn đứng trên đỉnh thế giới. Trái ác quỷ là lợi thế, không phải điều kiện bắt buộc.
```

### c06 · Thử nghiệm: bạn sẽ chọn trái nào? / Sáng tạo: dùng năng lực theo cách không ai nghĩ tới / Nguồn gốc: trái ác quỷ đến từ đâu?

Khoảng 150 giây · cảnh s63–s78 · 1947 ký tự

**Gemini**

```text
Giờ tới trò chơi yêu thích của fan One Piece: nếu được chọn một trái ác quỷ, bạn sẽ chọn loại nào?

<short pause> Nếu bạn muốn an toàn và linh hoạt, một trái Siêu nhân hữu dụng trong đời sống, như dịch chuyển hay chữa lành, là lựa chọn khôn ngoan.

<short pause> Nếu bạn muốn chiến đấu bền bỉ, Động vật, đặc biệt là loại thần thoại, cho bạn thể lực và khả năng hồi phục vượt trội.

<short pause> Nếu bạn muốn sức mạnh lớn và bạn sẵn sàng học Haki thật giỏi, Tự nhiên vẫn là lựa chọn đầy uy lực.

<short pause> Nhưng nhớ nhé: dù chọn gì, bạn sẽ không bao giờ bơi được nữa. Với người sống trên biển, đó là cái giá không nhỏ chút nào.

<short pause> Điểm hay nhất của trái ác quỷ không nằm ở năng lực, mà ở cách người dùng sáng tạo với nó.

<short pause> Luffy là ví dụ rõ nhất. Từ một cơ thể cao su, cậu nghĩ ra cách bơm máu nhanh hơn, thổi phồng xương, hay nén cơ bắp để tăng sức mạnh. Mỗi Gear là một ý tưởng mới.

<short pause> Có người dùng năng lực tưởng như yếu để làm nên chuyện lớn. Một năng lực tạo lỗ thủng trên tường hay khiến vật nhẹ đi có thể quyết định cả một cuộc đào thoát.

<short pause> Ngược lại, có người sở hữu năng lực mạnh nhưng dùng một cách đơn điệu, và cuối cùng thua người sáng tạo hơn.

<short pause> Đây là thông điệp rất One Piece: sức mạnh thật sự là trí tưởng tượng và sự kiên trì, không phải món quà bạn nhận được.

<short pause> <laugh> Kaku bổ sung: điều này giống ma thuật trong Frieren mà mình từng giải thích. Nhiều bộ truyện khác nhau đều đề cao trí tưởng tượng như một dạng sức mạnh.

<short pause> Một câu hỏi lớn vẫn chưa có lời giải trọn vẹn: trái ác quỷ đến từ đâu?

<short pause> Truyện cho biết người ta gọi nó là trái của quỷ biển, vì ăn vào sẽ bị biển cả nguyền rủa. <short pause> Nhưng vì sao nó tồn tại thì vẫn là bí ẩn.

<short pause> Ở những arc gần đây, một nhà khoa học thiên tài đưa ra giả thuyết rằng trái ác quỷ gắn với ước mơ và khao khát của con người. Đây vẫn là giả thuyết trong truyện.

<short pause> Nếu giả thuyết đó đúng, nó sẽ khớp với chủ đề lớn của One Piece: ước mơ của con người là thứ không thể ngăn cản.

<short pause> Kaku nhắc: phần này là giả thuyết, chưa phải sự thật được xác nhận. Khi truyện tiết lộ thêm, mình sẽ làm video cập nhật.
```

**ElevenLabs**

```text
[curious] Giờ tới trò chơi yêu thích của fan One Piece: nếu được chọn một trái ác quỷ, bạn sẽ chọn loại nào?

[pause] Nếu bạn muốn an toàn và linh hoạt, một trái Siêu nhân hữu dụng trong đời sống, như dịch chuyển hay chữa lành, là lựa chọn khôn ngoan.

[pause] Nếu bạn muốn chiến đấu bền bỉ, Động vật, đặc biệt là loại thần thoại, cho bạn thể lực và khả năng hồi phục vượt trội.

[pause] Nếu bạn muốn sức mạnh lớn và bạn sẵn sàng học Haki thật giỏi, Tự nhiên vẫn là lựa chọn đầy uy lực.

[pause] Nhưng nhớ nhé: dù chọn gì, bạn sẽ không bao giờ bơi được nữa. Với người sống trên biển, đó là cái giá không nhỏ chút nào.

[pause] Điểm hay nhất của trái ác quỷ không nằm ở năng lực, mà ở cách người dùng sáng tạo với nó.

[pause] Luffy là ví dụ rõ nhất. Từ một cơ thể cao su, cậu nghĩ ra cách bơm máu nhanh hơn, thổi phồng xương, hay nén cơ bắp để tăng sức mạnh. Mỗi Gear là một ý tưởng mới.

[pause] Có người dùng năng lực tưởng như yếu để làm nên chuyện lớn. Một năng lực tạo lỗ thủng trên tường hay khiến vật nhẹ đi có thể quyết định cả một cuộc đào thoát.

[pause] Ngược lại, có người sở hữu năng lực mạnh nhưng dùng một cách đơn điệu, và cuối cùng thua người sáng tạo hơn.

[pause] Đây là thông điệp rất One Piece: sức mạnh thật sự là trí tưởng tượng và sự kiên trì, không phải món quà bạn nhận được.

[pause] [chuckles] Kaku bổ sung: điều này giống ma thuật trong Frieren mà mình từng giải thích. Nhiều bộ truyện khác nhau đều đề cao trí tưởng tượng như một dạng sức mạnh.

[pause] Một câu hỏi lớn vẫn chưa có lời giải trọn vẹn: trái ác quỷ đến từ đâu?

[pause] Truyện cho biết người ta gọi nó là trái của quỷ biển, vì ăn vào sẽ bị biển cả nguyền rủa. [pause] Nhưng vì sao nó tồn tại thì vẫn là bí ẩn.

[pause] Ở những arc gần đây, một nhà khoa học thiên tài đưa ra giả thuyết rằng trái ác quỷ gắn với ước mơ và khao khát của con người. Đây vẫn là giả thuyết trong truyện.

[pause] Nếu giả thuyết đó đúng, nó sẽ khớp với chủ đề lớn của One Piece: ước mơ của con người là thứ không thể ngăn cản.

[pause] Kaku nhắc: phần này là giả thuyết, chưa phải sự thật được xác nhận. Khi truyện tiết lộ thêm, mình sẽ làm video cập nhật.
```

### c07 · Những hiểu lầm về trái ác quỷ / Góc nhìn của Kaku: vì sao hệ thống này thành công / Tóm tắt

Khoảng 142 giây · cảnh s79–s94 · 1846 ký tự

**Gemini**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về trái ác quỷ.

<short pause> Hiểu lầm một: ăn trái ác quỷ là mạnh ngay. Thực tế, người mới ăn thường chưa biết dùng, và phải luyện rất lâu mới kiểm soát được.

<short pause> Hiểu lầm hai: người dùng trái ác quỷ sợ mọi loại nước. Không đúng, họ chỉ yếu trong nước biển và nước đọng. Mưa hay nước uống không ảnh hưởng.

<short pause> Hiểu lầm ba: Động vật là loại yếu nhất. Những Động vật thần thoại và cổ đại thuộc hàng đáng sợ nhất trong truyện.

<short pause> Hiểu lầm bốn: trái ác quỷ là yếu tố quyết định trận đấu. Như mình đã nói, Haki, kỹ năng và sự sáng tạo thường quan trọng hơn.

<short pause> Nhìn tổng thể, vì sao hệ thống trái ác quỷ lại thành công đến vậy trong suốt hơn hai mươi lăm năm của One Piece?

<short pause> Lý do một: nó gần như vô hạn. Mỗi trái là một năng lực mới, nên tác giả luôn có thể tạo ra đối thủ và đồng đội khác biệt.

<short pause> Lý do hai: nó có luật chung đơn giản. Ai cũng hiểu: không bơi được, sợ hải lâu thạch, chỉ một trái. Luật đơn giản giúp người đọc theo kịp.

<short pause> Lý do ba: nó gắn với bí ẩn lớn của thế giới. Trái ác quỷ không chỉ là năng lực, mà là mảnh ghép của lịch sử bị che giấu.

<short pause> So với Nen hay Chú lực, trái ác quỷ ít luật hơn về cách dùng, nhưng bù lại bằng sự sáng tạo và bí ẩn. Đó là màu sắc riêng của One Piece.

<short pause> Tóm lại: trái ác quỷ cho năng lực ngay lập tức, nhưng lấy đi khả năng bơi. Mỗi người chỉ ăn một trái, và năng lực tái sinh khi người dùng chết.

<short pause> Có ba loại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Điểm yếu chung là hải lâu thạch và Haki.

<short pause> Thức tỉnh là đỉnh cao, và trái của Luffy thực ra là Động vật thần thoại bị giấu tên suốt nhiều thế kỷ.

<short pause> Câu hỏi cho bạn: nếu được ăn một trái ác quỷ, bạn chọn năng lực gì, và bạn có chấp nhận không bao giờ bơi được nữa không? Viết xuống phần bình luận nhé.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. <laugh> Video sau Kaku sẽ giải mã hệ thống cấp bậc thợ săn trong Solo Leveling.

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi tổng kết, cùng gỡ vài hiểu lầm phổ biến về trái ác quỷ.

[pause] Hiểu lầm một: ăn trái ác quỷ là mạnh ngay. Thực tế, người mới ăn thường chưa biết dùng, và phải luyện rất lâu mới kiểm soát được.

[pause] Hiểu lầm hai: người dùng trái ác quỷ sợ mọi loại nước. Không đúng, họ chỉ yếu trong nước biển và nước đọng. Mưa hay nước uống không ảnh hưởng.

[pause] Hiểu lầm ba: Động vật là loại yếu nhất. Những Động vật thần thoại và cổ đại thuộc hàng đáng sợ nhất trong truyện.

[pause] Hiểu lầm bốn: trái ác quỷ là yếu tố quyết định trận đấu. Như mình đã nói, Haki, kỹ năng và sự sáng tạo thường quan trọng hơn.

[pause] [curious] Nhìn tổng thể, vì sao hệ thống trái ác quỷ lại thành công đến vậy trong suốt hơn hai mươi lăm năm của One Piece?

[pause] Lý do một: nó gần như vô hạn. Mỗi trái là một năng lực mới, nên tác giả luôn có thể tạo ra đối thủ và đồng đội khác biệt.

[pause] Lý do hai: nó có luật chung đơn giản. Ai cũng hiểu: không bơi được, sợ hải lâu thạch, chỉ một trái. Luật đơn giản giúp người đọc theo kịp.

[pause] Lý do ba: nó gắn với bí ẩn lớn của thế giới. Trái ác quỷ không chỉ là năng lực, mà là mảnh ghép của lịch sử bị che giấu.

[pause] So với Nen hay Chú lực, trái ác quỷ ít luật hơn về cách dùng, nhưng bù lại bằng sự sáng tạo và bí ẩn. Đó là màu sắc riêng của One Piece.

[pause] Tóm lại: trái ác quỷ cho năng lực ngay lập tức, nhưng lấy đi khả năng bơi. Mỗi người chỉ ăn một trái, và năng lực tái sinh khi người dùng chết.

[pause] Có ba loại: Siêu nhân đa dạng, Động vật bền bỉ, Tự nhiên khó chạm vào. Điểm yếu chung là hải lâu thạch và Haki.

[pause] Thức tỉnh là đỉnh cao, và trái của Luffy thực ra là Động vật thần thoại bị giấu tên suốt nhiều thế kỷ.

[pause] Câu hỏi cho bạn: nếu được ăn một trái ác quỷ, bạn chọn năng lực gì, và bạn có chấp nhận không bao giờ bơi được nữa không? Viết xuống phần bình luận nhé.

[pause] Nếu video hữu ích, hãy đăng ký kênh. [chuckles] Video sau Kaku sẽ giải mã hệ thống cấp bậc thợ săn trong Solo Leveling.

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
