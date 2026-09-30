# Bộ prompt · Sakamoto Days: Ôn tập mọi thứ cần nhớ trước mùa 2

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 10 đoạn đọc, khoảng 15.3 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (82 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Sakamoto Days tới hết anime mùa một, tập hai mươi hai. Kaku không nói gì về phần m…

```text
Wide 16:9 landscape cinematic frame. a small neighborhood convenience store at night with its lights still on, a closed notebook resting on the counter, wide establishing shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Mùa hai của Sakamoto Days lên sóng vào tháng một năm 2027. Nếu bạn xem mùa một từ năm ngoái và đã quên gần hế…

```text
Wide 16:9 landscape cinematic frame. a desk calendar showing January with a small countdown circle drawn around a date, a remote control beside it, close-up, fresh morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Kaku sẽ nhắc lại: mùa một đã xảy ra những gì, luật sức mạnh nào cần nhớ, các phe đang đứng ở đâu, và những nú…

```text
Wide 16:9 landscape cinematic frame. four index cards laid out on a table: a store icon, a rulebook icon, a chessboard icon and a knot icon, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Và cuối video là ba điều Kaku nghĩ bạn nên để ý khi xem mùa mới. Không spoiler, chỉ là gợi ý để xem hay hơn.

```text
Wide 16:9 landscape cinematic frame. a small magnifying glass resting on a notebook page with three empty bullet points, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Sakamoto Days là manga của tác giả Suzuki Yuto, đăng trên tạp chí Shonen Jump từ năm 2020. Anime mùa một lên…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a laptop showing a streaming menu, close-up, cozy evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku làm gia sư ôn thi cho bạn trước kỳ thi… à nhầm, trước mùa mới.

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny tutor's cap standing before a chalkboard with a big number two drawn on it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Mùa một trong ba phút

Lời: Sakamoto Taro từng là sát thủ huyền thoại, người mạnh nhất giới sát thủ. Kẻ thù sợ ông, đồng nghiệp nể ông.

```text
Wide 16:9 landscape cinematic frame. a sleek legendary assassin silhouette in a dark suit standing on a rooftop at night, city lights below, low-angle shot, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Tập đầu tiên mở ra khi một sát thủ trẻ được cử tới để thuyết phục, hoặc giết, Sakamoto. Người đó chính là Shi…

```text
Wide 16:9 landscape cinematic frame. a young man in a dark jacket lying defeated on a store floor while a round shopkeeper offers him an apron, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Cả nhà Sakamoto sống bình thường tới mức buồn cười: vợ chồng lo cửa hàng, con gái Hana đi mẫu giáo, và thỉnh…

```text
Wide 16:9 landscape cinematic frame. a little girl with a kindergarten backpack waving goodbye at the store door while a masked intruder hides behind a shelf in the background, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Rồi ông gặp một cô gái làm thu ngân ở cửa hàng tiện lợi, yêu cô, và giải nghệ. Ông cưới cô, có một cô con gái…

```text
Wide 16:9 landscape cinematic frame. a large round cheerful shopkeeper silhouette behind a small store counter, a smiling wife and a little daughter beside him, medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Tiền thưởng cho đầu Sakamoto lớn tới mức sát thủ khắp nơi đổ về thị trấn nhỏ. Có tập, cửa hàng tiện lợi biến…

```text
Wide 16:9 landscape cinematic frame. a small town street filled with suspicious figures in disguises all converging on a tiny convenience store, wide shot, comedic tension. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Nhưng quá khứ không để ông yên. Những sát thủ cũ lần lượt tìm tới, và rồi cả thế giới ngầm treo thưởng cho cá…

```text
Wide 16:9 landscape cinematic frame. a wanted poster with a large reward number pinned on a dark alley wall among many others, close-up, harsh streetlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Kẻ đứng sau lệnh treo thưởng là một người bí ẩn có biệt danh là Slur, hay X. Hắn muốn thay đổi toàn bộ trật t…

```text
Wide 16:9 landscape cinematic frame. a mysterious figure in a long coat standing in the shadows of a tunnel, face obscured, a single large letter X scratched on the wall behind, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Sakamoto thì có một quy tắc tuyệt đối: không giết người. Ông đã hứa với vợ như vậy. Nên mọi trận đấu của ông…

```text
Wide 16:9 landscape cinematic frame. a large hand gently holding a small wedding ring, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Arc tử tù đáng nhớ vì những kẻ thù rất quái dị: mỗi tên tử tù vượt ngục có một phong cách giết người riêng, v…

```text
Wide 16:9 landscape cinematic frame. a row of shadowy escaped prisoner silhouettes in torn uniforms standing in front of a broken prison gate, wide shot, cold floodlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Arc kỳ thi JCC thì giống một bộ phim sinh tồn: thí sinh phải vượt qua những bài thi chết người để được vào họ…

```text
Wide 16:9 landscape cinematic frame. a large exam hall with candidates at desks, a countdown clock on the wall and hidden traps glowing faintly under the floor, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Mùa một có ba arc lớn. Arc đầu giới thiệu cửa hàng và những người bạn. Arc giữa là cuộc đối đầu với nhóm tử t…

```text
Wide 16:9 landscape cinematic frame. three small book spines on a shelf with icons: a store, a prison cell, and a school gate, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Tập cuối khép lại kỳ thi, và mở ra một hướng đi mới: nhóm của Sakamoto sẽ phải thâm nhập vào chính học viện J…

```text
Wide 16:9 landscape cinematic frame. a grand academy gate at dusk with a small group of silhouettes approaching it, wide shot, dramatic orange sky. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Luật 1: Sakamoto gầy và Sakamoto béo

Lời: Giờ đến phần quan trọng nhất: các luật sức mạnh. Luật thứ nhất nghe buồn cười nhưng rất thật trong truyện: hì…

```text
Wide 16:9 landscape cinematic frame. a split illustration: a round cheerful shopkeeper on the left, a slim sharp assassin on the right, same outfit, symmetrical composition, warm and cold light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Khi chiến đấu hết sức, ông đốt năng lượng nhanh tới mức gầy đi ngay trong trận, trở lại dáng vẻ thời còn là s…

```text
Wide 16:9 landscape cinematic frame. a sequence of three silhouettes showing a round figure gradually becoming slim during a fight, then round again after, parchment diagram, amber ink. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Trong truyện, dáng gầy của Sakamoto còn là một tín hiệu cho đối thủ. Những ai từng biết ông thời còn là sát t…

```text
Wide 16:9 landscape cinematic frame. a frightened opponent staring at a slim silhouette emerging from steam, close-up on the opponent's wide eyes, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Có những trận Sakamoto chỉ gầy đi một nửa, hoặc gầy đi trong vài giây rồi lại béo. Tác giả dùng hình dáng như…

```text
Wide 16:9 landscape cinematic frame. a humorous health-bar style diagram drawn as a belly outline shrinking and growing, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Nhưng đừng để dáng béo đánh lừa. Ngay cả khi tròn nhất, Sakamoto vẫn nhanh hơn và mạnh hơn gần như mọi đối th…

```text
Wide 16:9 landscape cinematic frame. a round shopkeeper effortlessly dodging a thrown knife while carrying groceries, humorous dynamic shot, bright daylight. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Nhưng hãy nhớ: béo trở lại cũng là một phần của luật. Sau mỗi trận đấu, Sakamoto trở về làm một ông bố, một ô…

```text
Wide 16:9 landscape cinematic frame. a round shopkeeper eating dinner happily with his family at a small table, medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây có lẽ là hệ thống sức mạnh duy nhất trong anime mà chỉ số cân nặng là một thanh sức mạnh. K…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a pastry in one wing and flexing a tiny bicep with the other, comic expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Luật 2: mọi thứ đều là vũ khí

Lời: Ông còn dùng được những thứ mà người khác không nghĩ tới: một cái móc áo, một chiếc đũa, một thanh kẹo. Với S…

```text
Wide 16:9 landscape cinematic frame. a hand holding a single chopstick poised precisely like a fencing sword, extreme close-up, dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Luật thứ hai là phong cách của cả bộ truyện: bất cứ vật gì cũng có thể thành vũ khí. Sakamoto đánh bằng thìa,…

```text
Wide 16:9 landscape cinematic frame. a collection of everyday items laid out like a weapons rack: a spoon, a ballpoint pen, a plastic bag, a shopping cart, still life, dramatic lighting. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Điều này không chỉ để vui. Vì không được giết người, Sakamoto cần những cách đánh gục đối thủ mà không gây ch…

```text
Wide 16:9 landscape cinematic frame. a shopkeeper disarming an attacker using only a rolled-up newspaper, dynamic medium shot, warm store light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và đối thủ cũng biết điều đó. Có những sát thủ cố gắng dọn sạch không gian trước khi đấu, để Sakamoto không c…

```text
Wide 16:9 landscape cinematic frame. an empty white room with a lone attacker looking confused as a round figure calmly holds a single paperclip, humorous medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thử áp dụng luật này ở nhà và phát hiện ra mình chỉ biết dùng cuốn sổ làm vũ khí. Có lẽ vì vậy Kaku chỉ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot swinging its notebook clumsily like a sword, papers flying out. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Mỗi trận đấu vì vậy giống như một câu đố: trong không gian này có những đồ vật gì, và dùng chúng thế nào cho…

```text
Wide 16:9 landscape cinematic frame. a top-down diagram of a convenience store aisle with items circled and arrows showing a fight route, parchment style, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Và đó cũng là lý do các cảnh đánh trong Sakamoto Days thường đi kèm rất nhiều tiếng cười. Căng thẳng và hài h…

```text
Wide 16:9 landscape cinematic frame. a chaotic fight in a supermarket with flying cereal boxes and a startled cat on a shelf, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Luật 3: Shin đọc được suy nghĩ

Lời: Giữa Shin và Sakamoto còn có một kiểu giao tiếp đặc biệt: Sakamoto chỉ cần nghĩ, Shin sẽ hiểu. Trong nhiều tr…

```text
Wide 16:9 landscape cinematic frame. two figures in a store fighting back to back, faint lines of thought connecting their heads, dynamic medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Người trợ thủ đầu tiên của Sakamoto là Asakura Shin, một sát thủ trẻ có khả năng đọc suy nghĩ của người khác.…

```text
Wide 16:9 landscape cinematic frame. a young man in a store apron with a faint ring of light around his head, overlapping speech-bubble shapes floating near him, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Nghĩa là đối thủ giỏi nhất với Shin là người không suy nghĩ, hoặc người suy nghĩ quá nhiều thứ cùng lúc. Có k…

```text
Wide 16:9 landscape cinematic frame. a young man clutching his head as dozens of chaotic thought bubbles swirl around an opponent, humorous close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Trong chiến đấu, đọc suy nghĩ giúp Shin biết trước đối thủ định làm gì. Nhưng nó có giới hạn: phạm vi gần, và…

```text
Wide 16:9 landscape cinematic frame. a diagram showing a small circle of range around a figure, with one attacker inside labeled with a thought icon and one attacker outside, parchment style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Và đọc suy nghĩ cũng có mặt trái: Shin nghe cả những điều người khác không muốn nói ra. Nhiều tình huống hài…

```text
Wide 16:9 landscape cinematic frame. a young man wincing with embarrassment while a smiling customer's thought bubble shows something awkward, humorous close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Ở kỳ thi JCC, Shin không có Sakamoto bên cạnh. Lần đầu tiên, cậu phải tự đưa ra quyết định và bảo vệ người kh…

```text
Wide 16:9 landscape cinematic frame. a young man standing alone in front of a group of frightened candidates, facing a looming examiner silhouette, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Suốt mùa một, Shin mạnh lên rất nhiều, và ở kỳ thi JCC, cậu gần như là nhân vật chính thứ hai. Hãy nhớ rằng k…

```text
Wide 16:9 landscape cinematic frame. a young man standing confidently in an exam hall among rival candidates, faint light rings expanding around his head, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Luật 4: những người bạn

Lời: Lu mang theo một món nợ quá khứ: gia đình cô bị cuốn vào những cuộc thanh toán trong giới ngầm, và Sakamoto l…

```text
Wide 16:9 landscape cinematic frame. a young woman sitting on the store's back steps at night looking at an old family photo, a warm light from the doorway behind her, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Lu Shaotang là cô gái đến từ một gia đình mafia Trung Quốc. Cô dùng võ thuật, và có một kiểu quyền rất đặc bi…

```text
Wide 16:9 landscape cinematic frame. a young woman in a qipao-inspired outfit striking a kung fu stance in an alley, a small empty cup rolling at her feet, dynamic medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chú vẹt của Heisuke không chỉ là thú cưng. Nó là người bạn duy nhất của anh trong nhiều năm, và có những lúc…

```text
Wide 16:9 landscape cinematic frame. a colorful parrot flying boldly toward a masked villain while a young sniper shouts behind it, dynamic wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Heisuke là một tay bắn tỉa vụng về nhưng tốt bụng, đi cùng một chú vẹt. Anh từng là kẻ thù, rồi trở thành ngư…

```text
Wide 16:9 landscape cinematic frame. a lanky young man holding a long rifle awkwardly, a colorful parrot perched on his shoulder, medium shot, soft daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và có vợ Sakamoto, Aoi. Cô không phải sát thủ, nhưng là người đặt luật cho cả nhà: không giết người, không là…

```text
Wide 16:9 landscape cinematic frame. a calm woman standing behind a store counter with her arms crossed and a gentle but firm smile, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Aoi còn là lý do khiến cửa hàng trở thành một gia đình thay vì một băng nhóm. Ai vào làm cũng phải tuân theo…

```text
Wide 16:9 landscape cinematic frame. a handwritten list of house rules pinned beside the store's staff room door, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: trong một bộ truyện về sát thủ, người đáng sợ nhất với nhân vật chính lại là người vợ không cầm vũ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding behind a stack of cans, peeking nervously at a calm woman with crossed arms. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Các phe phái

Lời: Giờ tới bản đồ các phe. Phe thứ nhất: cửa hàng Sakamoto, gồm Sakamoto, Shin, Lu, Heisuke và những người bạn.…

```text
Wide 16:9 landscape cinematic frame. a simple faction map on parchment with a small store icon at the center surrounded by friendly figure icons, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Order có những gương mặt rất khác nhau: một người điềm tĩnh và cực nhanh, một cô gái trẻ thanh lịch với lưỡi…

```text
Wide 16:9 landscape cinematic frame. three elite silhouettes standing apart in a rainy plaza: a calm man in a suit, a graceful young woman with a long saw, an old swordsman with a cane, wide shot, cold elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Luật của Hội rất rõ: giới sát thủ có trật tự, có đẳng cấp, và ai phá trật tự sẽ bị Order xử lý. Việc cả giới…

```text
Wide 16:9 landscape cinematic frame. an ornate rulebook lying open on a marble desk with a crack running through the page, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Phe thứ hai: Hội Sát thủ và JCC. Đứng đầu là một nhóm sát thủ mạnh nhất gọi là Order, đội cảnh sát của giới s…

```text
Wide 16:9 landscape cinematic frame. an ornate hall with a circle of elite silhouettes seated around a round table, a crest on the wall, wide shot, cold elegant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Trong Order có Nagumo, bạn học cũ thời JCC của Sakamoto, bậc thầy cải trang, lúc nào cũng cười. Không ai chắc…

```text
Wide 16:9 landscape cinematic frame. a smiling tall figure holding several different masks fanned out like playing cards, medium shot, playful but ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Điều đáng sợ ở Slur không phải sức mạnh, mà là hắn có tầm nhìn. Hắn không chỉ muốn giết Sakamoto. Hắn muốn th…

```text
Wide 16:9 landscape cinematic frame. a figure standing on a high ledge looking down at a sprawling city map drawn on the ground below, back view, ominous dusk light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Phe thứ ba: Slur và những kẻ đi theo hắn. Hắn thuê tử tù, gây hỗn loạn, và muốn phá vỡ trật tự của Hội.

```text
Wide 16:9 landscape cinematic frame. a dark tunnel with several menacing silhouettes gathered behind a figure in a long coat, wide shot, eerie green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Và giữa các phe là những nhân vật chưa rõ lập trường, trong đó có hai học viên trẻ ở JCC là Toramaru và Mafuy…

```text
Wide 16:9 landscape cinematic frame. two young students standing at a crossroads in an academy courtyard, a shadow looming over them from above, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Kaku ghi chú: trong Sakamoto Days, ranh giới giữa bạn và thù thay đổi rất nhanh. Nhiều kẻ thù của mùa một giờ…

```text
Wide 16:9 landscape cinematic frame. a faction map with several arrows redrawn from the enemy side to the friendly side, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Nút thắt 1: Slur là ai?

Lời: Có những lúc Slur dường như nói chuyện với chính mình, như thể trong hắn có hai giọng nói. Kaku ghi đây là mộ…

```text
Wide 16:9 landscape cinematic frame. a cracked mirror in a dark tunnel reflecting two slightly different silhouettes of the same figure, close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Nút thắt lớn nhất: Slur thật sự là ai, và vì sao hắn nhắm vào Sakamoto? Mùa một để lại vài manh mối, nhưng ch…

```text
Wide 16:9 landscape cinematic frame. a corkboard with a blurry figure photo in the center and red strings connecting to question marks, medium shot, desk lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Và hắn chọn đúng thời điểm Sakamoto đã giải nghệ, tăng cân, có gia đình để ra tay. Một kẻ hiểu rằng điểm yếu…

```text
Wide 16:9 landscape cinematic frame. a shadow falling across a family photo on a store counter at night, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hắn dường như biết rất rõ về Sakamoto và về JCC. Và hắn nói về việc xây dựng một trật tự mới cho giới sát thủ…

```text
Wide 16:9 landscape cinematic frame. an old academy yearbook lying open with one photo scratched out, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku không spoiler. Nhưng nếu bạn để ý những chi tiết về quá khứ JCC trong mùa hai, bạn sẽ đoán được nhiều đi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot zipping its beak shut with a tiny zipper, holding a sealed envelope. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Nút thắt 2: quá khứ của Sakamoto

Lời: Mùa một chỉ hé lộ những mảnh nhỏ: Sakamoto từng học ở JCC, từng là thành viên Order, và từng có những người b…

```text
Wide 16:9 landscape cinematic frame. three school lockers side by side, one with a store keychain, one with a smiling mask, one scratched with an X, close-up, dim hallway light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nút thắt thứ hai: quá khứ của chính Sakamoto. Ông đã trở thành sát thủ mạnh nhất thế nào, ai là thầy, ai là b…

```text
Wide 16:9 landscape cinematic frame. an old photograph of three young students in academy uniforms standing together, faces obscured by sunlight glare, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đoán arc quá khứ sẽ thay đổi cách bạn nhìn nhiều nhân vật, kể cả những người bạn tưởng đã hiểu rõ. Đây l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rewinding an old videotape with a pencil, looking eager. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Theo thông tin về mùa hai, anime sẽ đi vào arc quá khứ của Sakamoto. Đây là phần nhiều fan manga đánh giá rất…

```text
Wide 16:9 landscape cinematic frame. a flashback-style scene of a young slim assassin silhouette standing in the rain in an academy courtyard, medium shot, muted colors. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Hãy nhớ lại mối quan hệ giữa Sakamoto và Nagumo ở mùa một. Họ trêu nhau như bạn cũ, nhưng cũng từng chĩa vũ k…

```text
Wide 16:9 landscape cinematic frame. two men standing back to back in a quiet street, one round and one tall, both smiling slightly, medium shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Nút thắt 3: quy tắc không giết người

Lời: Nút thắt thứ ba không nằm trong cốt truyện, mà nằm trong luật chơi: quy tắc không giết người sẽ còn đứng vững…

```text
Wide 16:9 landscape cinematic frame. a small promise note taped to the inside of a store's cash register, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Và quy tắc này còn áp dụng cho cả những người ở cửa hàng. Shin, Lu, Heisuke đều phải chiến đấu theo cách của…

```text
Wide 16:9 landscape cinematic frame. three young fighters standing guard in front of a small store at night, each holding a non-lethal improvised weapon, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kẻ thù ngày càng mạnh, và nhiều kẻ không ngần ngại giết người. Mỗi trận, Sakamoto phải thắng với một tay bị t…

```text
Wide 16:9 landscape cinematic frame. a heavyweight fighter with one arm tied behind his back facing several armed opponents, dramatic low-angle shot, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Kaku nghĩ nếu có một ngày quy tắc này bị phá, đó sẽ là khoảnh khắc lớn nhất của cả bộ truyện. Còn trước ngày…

```text
Wide 16:9 landscape cinematic frame. a small ring glowing softly on a store counter while a storm rages outside the window, close-up, warm light against cold. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Đây là nguồn căng thẳng thú vị nhất của bộ truyện: không phải Sakamoto có thắng không, mà là ông có thắng đượ…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a small ring on one side and a heavy sword on the other, perfectly level, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Ba điều nên để ý ở mùa mới · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ là ba điều Kaku gợi ý bạn để ý khi xem mùa hai.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up three fingers in front of a big television screen. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Học viện JCC là một nơi đầy đồ vật lạ: phòng thí nghiệm, thư viện, phòng tập, căng tin. Kaku đoán mùa hai sẽ…

```text
Wide 16:9 landscape cinematic frame. a wide academy corridor lined with labs, a library and a cafeteria, strange objects visible through each doorway, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Một: để ý những đồ vật trong khung hình. Trong mỗi trận đấu, gần như món đồ nào xuất hiện cũng sẽ được dùng.…

```text
Wide 16:9 landscape cinematic frame. a cluttered classroom desk with a stapler, a ruler and a lunch box circled in amber ink, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hai: để ý cân nặng của Sakamoto. Mỗi lần ông gầy đi là một tín hiệu: trận đấu đã nghiêm trọng tới mức ông khô…

```text
Wide 16:9 landscape cinematic frame. a simple gauge drawn on parchment from round to slim with the needle moving toward slim, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Ba: để ý những gì Shin nghe được mà không nói ra. Khả năng đọc suy nghĩ của cậu thường là cách truyện giấu ma…

```text
Wide 16:9 landscape cinematic frame. a young man with a knowing expression standing in a crowd, faint thought bubbles around other people, one bubble glowing brighter, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nhất là khi mùa hai đưa Sakamoto rời xa cửa hàng. Mỗi lần ông nhớ tới nhà là một lần ta hiểu vì sao ông chiến…

```text
Wide 16:9 landscape cinematic frame. a round man looking at a small drawing made by a child taped inside his jacket, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và một điều bonus: đừng bỏ qua những cảnh gia đình. Trong Sakamoto Days, những bữa cơm ở nhà chính là lý do c…

```text
Wide 16:9 landscape cinematic frame. a small family dinner table with three bowls of rice and a warm lamp, a round father laughing, medium shot, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Kết

Lời: Sakamoto Days là một bộ truyện về một người đàn ông mạnh nhất thế giới, người chỉ muốn được về nhà ăn tối đún…

```text
Wide 16:9 landscape cinematic frame. a round shopkeeper walking home at sunset carrying grocery bags, a cat following him, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và nếu bạn chưa xem mùa một, video này cũng là bản tóm tắt đủ để bắt đầu. Nhưng Kaku vẫn khuyên xem mùa một,…

```text
Wide 16:9 landscape cinematic frame. a person settling onto a couch with a blanket and a bowl of snacks, a remote in hand, medium shot, cozy evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Xem xong vài tập đầu mùa hai, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không. Và nếu bạn đã đọc manga,…

```text
Wide 16:9 landscape cinematic frame. a comment section drawn on parchment with small spoiler tags on some lines, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo, Kaku bước vào một thế giới game thực tế ảo: Shangri-La Frontier. Kaku sẽ đọc bảng chỉ số của…

```text
Wide 16:9 landscape cinematic frame. a glowing game status window floating in a fantasy forest, stats bars and icons visible, wide shot, vibrant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video ôn tập này giúp bạn sẵn sàng cho mùa mới, hãy đăng ký kênh để Kaku ôn thêm các bộ khác trước khi ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off its tutor cap and waving goodbye beside the chalkboard with the big number two. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 60 giây · cảnh s01–s06 · 782 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Sakamoto Days tới hết anime mùa một, tập hai mươi hai. Kaku không nói gì về phần manga mà mùa hai sẽ chiếu.

<short pause> Mùa hai của Sakamoto Days lên sóng vào tháng một năm 2027. Nếu bạn xem mùa một từ năm ngoái và đã quên gần hết, đây là mười lăm phút bạn cần.

<short pause> Kaku sẽ nhắc lại: mùa một đã xảy ra những gì, luật sức mạnh nào cần nhớ, các phe đang đứng ở đâu, và những nút thắt còn mở.

<short pause> Và cuối video là ba điều Kaku nghĩ bạn nên để ý khi xem mùa mới. Không spoiler, chỉ là gợi ý để xem hay hơn.

<short pause> Sakamoto Days là manga của tác giả Suzuki Yuto, đăng trên tạp chí Shonen Jump từ năm 2020. Anime mùa một lên Netflix năm 2025, chia làm hai phần, tổng cộng hai mươi hai tập.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku làm gia sư ôn thi cho bạn trước kỳ thi… à nhầm, trước mùa mới.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Sakamoto Days tới hết anime mùa một, tập hai mươi hai. Kaku không nói gì về phần manga mà mùa hai sẽ chiếu.

[pause] Mùa hai của Sakamoto Days lên sóng vào tháng một năm 2027. Nếu bạn xem mùa một từ năm ngoái và đã quên gần hết, đây là mười lăm phút bạn cần.

[pause] Kaku sẽ nhắc lại: mùa một đã xảy ra những gì, luật sức mạnh nào cần nhớ, các phe đang đứng ở đâu, và những nút thắt còn mở.

[pause] Và cuối video là ba điều Kaku nghĩ bạn nên để ý khi xem mùa mới. Không spoiler, chỉ là gợi ý để xem hay hơn.

[pause] Sakamoto Days là manga của tác giả Suzuki Yuto, đăng trên tạp chí Shonen Jump từ năm 2020. Anime mùa một lên Netflix năm 2025, chia làm hai phần, tổng cộng hai mươi hai tập.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku làm gia sư ôn thi cho bạn trước kỳ thi… à nhầm, trước mùa mới.
```

### c02 · Mùa một trong ba phút

Khoảng 136 giây · cảnh s07–s18 · 1772 ký tự

**Gemini**

```text
Sakamoto Taro từng là sát thủ huyền thoại, người mạnh nhất giới sát thủ. Kẻ thù sợ ông, đồng nghiệp nể ông.

<short pause> Tập đầu tiên mở ra khi một sát thủ trẻ được cử tới để thuyết phục, hoặc giết, Sakamoto. Người đó chính là Shin. Kết quả là cậu bị đánh bại, rồi được nhận vào làm ở cửa hàng.

<short pause> Cả nhà Sakamoto sống bình thường tới mức buồn cười: vợ chồng lo cửa hàng, con gái Hana đi mẫu giáo, và thỉnh thoảng có một sát thủ đột nhập giữa giờ bán hàng.

<short pause> Rồi ông gặp một cô gái làm thu ngân ở cửa hàng tiện lợi, yêu cô, và giải nghệ. Ông cưới cô, có một cô con gái, mở một cửa hàng tạp hóa nhỏ, và tăng cân. Rất nhiều cân.

<short pause> Tiền thưởng cho đầu Sakamoto lớn tới mức sát thủ khắp nơi đổ về thị trấn nhỏ. Có tập, cửa hàng tiện lợi biến thành chiến trường chỉ trong vài phút.

<short pause> Nhưng quá khứ không để ông yên. Những sát thủ cũ lần lượt tìm tới, và rồi cả thế giới ngầm treo thưởng cho cái đầu của ông.

<short pause> Kẻ đứng sau lệnh treo thưởng là một người bí ẩn có biệt danh là Slur, hay X. Hắn muốn thay đổi toàn bộ trật tự của giới sát thủ.

<short pause> Sakamoto thì có một quy tắc tuyệt đối: không giết người. Ông đã hứa với vợ như vậy. Nên mọi trận đấu của ông đều phải thắng mà không lấy mạng ai.

<short pause> Arc tử tù đáng nhớ vì những kẻ thù rất quái dị: mỗi tên tử tù vượt ngục có một phong cách giết người riêng, và Slur thả chúng ra để săn Sakamoto.

<short pause> Arc kỳ thi JCC thì giống một bộ phim sinh tồn: thí sinh phải vượt qua những bài thi chết người để được vào học viện sát thủ danh giá nhất.

<short pause> Mùa một có ba arc lớn. Arc đầu giới thiệu cửa hàng và những người bạn. Arc giữa là cuộc đối đầu với nhóm tử tù vượt ngục do Slur thuê. Arc cuối là kỳ thi chuyển trường vào JCC, học viện đào tạo sát thủ.

<short pause> Tập cuối khép lại kỳ thi, và mở ra một hướng đi mới: nhóm của Sakamoto sẽ phải thâm nhập vào chính học viện JCC. Đó là nơi mùa hai bắt đầu.
```

**ElevenLabs**

```text
Sakamoto Taro từng là sát thủ huyền thoại, người mạnh nhất giới sát thủ. Kẻ thù sợ ông, đồng nghiệp nể ông.

[pause] Tập đầu tiên mở ra khi một sát thủ trẻ được cử tới để thuyết phục, hoặc giết, Sakamoto. Người đó chính là Shin. Kết quả là cậu bị đánh bại, rồi được nhận vào làm ở cửa hàng.

[pause] Cả nhà Sakamoto sống bình thường tới mức buồn cười: vợ chồng lo cửa hàng, con gái Hana đi mẫu giáo, và thỉnh thoảng có một sát thủ đột nhập giữa giờ bán hàng.

[pause] Rồi ông gặp một cô gái làm thu ngân ở cửa hàng tiện lợi, yêu cô, và giải nghệ. Ông cưới cô, có một cô con gái, mở một cửa hàng tạp hóa nhỏ, và tăng cân. Rất nhiều cân.

[pause] Tiền thưởng cho đầu Sakamoto lớn tới mức sát thủ khắp nơi đổ về thị trấn nhỏ. Có tập, cửa hàng tiện lợi biến thành chiến trường chỉ trong vài phút.

[pause] Nhưng quá khứ không để ông yên. Những sát thủ cũ lần lượt tìm tới, và rồi cả thế giới ngầm treo thưởng cho cái đầu của ông.

[pause] Kẻ đứng sau lệnh treo thưởng là một người bí ẩn có biệt danh là Slur, hay X. Hắn muốn thay đổi toàn bộ trật tự của giới sát thủ.

[pause] Sakamoto thì có một quy tắc tuyệt đối: không giết người. Ông đã hứa với vợ như vậy. Nên mọi trận đấu của ông đều phải thắng mà không lấy mạng ai.

[pause] Arc tử tù đáng nhớ vì những kẻ thù rất quái dị: mỗi tên tử tù vượt ngục có một phong cách giết người riêng, và Slur thả chúng ra để săn Sakamoto.

[pause] Arc kỳ thi JCC thì giống một bộ phim sinh tồn: thí sinh phải vượt qua những bài thi chết người để được vào học viện sát thủ danh giá nhất.

[pause] Mùa một có ba arc lớn. Arc đầu giới thiệu cửa hàng và những người bạn. Arc giữa là cuộc đối đầu với nhóm tử tù vượt ngục do Slur thuê. Arc cuối là kỳ thi chuyển trường vào JCC, học viện đào tạo sát thủ.

[pause] Tập cuối khép lại kỳ thi, và mở ra một hướng đi mới: nhóm của Sakamoto sẽ phải thâm nhập vào chính học viện JCC. Đó là nơi mùa hai bắt đầu.
```

### c03 · Luật 1: Sakamoto gầy và Sakamoto béo

Khoảng 86 giây · cảnh s19–s25 · 1123 ký tự

**Gemini**

```text
Giờ đến phần quan trọng nhất: các luật sức mạnh. Luật thứ nhất nghe buồn cười nhưng rất thật trong truyện: hình dáng của Sakamoto thay đổi theo mức độ nghiêm túc.

<short pause> Khi chiến đấu hết sức, ông đốt năng lượng nhanh tới mức gầy đi ngay trong trận, trở lại dáng vẻ thời còn là sát thủ. Khi trận kết thúc, ông lại tròn trịa như cũ.

<short pause> Trong truyện, dáng gầy của Sakamoto còn là một tín hiệu cho đối thủ. Những ai từng biết ông thời còn là sát thủ đều hiểu: nếu ông gầy đi, họ đã gặp rắc rối lớn.

<short pause> Có những trận Sakamoto chỉ gầy đi một nửa, hoặc gầy đi trong vài giây rồi lại béo. Tác giả dùng hình dáng như một thanh máu mà người xem nhìn thấy được.

<short pause> Nhưng đừng để dáng béo đánh lừa. Ngay cả khi tròn nhất, Sakamoto vẫn nhanh hơn và mạnh hơn gần như mọi đối thủ. Dáng béo chỉ có nghĩa là ông chưa cần nghiêm túc.

<short pause> Nhưng hãy nhớ: béo trở lại cũng là một phần của luật. Sau mỗi trận đấu, Sakamoto trở về làm một ông bố, một ông chủ cửa hàng. Cân nặng của ông là cân nặng của cuộc sống bình yên.

<short pause> <laugh> Kaku ghi chú: đây có lẽ là hệ thống sức mạnh duy nhất trong anime mà chỉ số cân nặng là một thanh sức mạnh. Kaku cũng mong ăn bánh xong thì mạnh lên.
```

**ElevenLabs**

```text
Giờ đến phần quan trọng nhất: các luật sức mạnh. Luật thứ nhất nghe buồn cười nhưng rất thật trong truyện: hình dáng của Sakamoto thay đổi theo mức độ nghiêm túc.

[pause] Khi chiến đấu hết sức, ông đốt năng lượng nhanh tới mức gầy đi ngay trong trận, trở lại dáng vẻ thời còn là sát thủ. Khi trận kết thúc, ông lại tròn trịa như cũ.

[pause] Trong truyện, dáng gầy của Sakamoto còn là một tín hiệu cho đối thủ. Những ai từng biết ông thời còn là sát thủ đều hiểu: nếu ông gầy đi, họ đã gặp rắc rối lớn.

[pause] Có những trận Sakamoto chỉ gầy đi một nửa, hoặc gầy đi trong vài giây rồi lại béo. Tác giả dùng hình dáng như một thanh máu mà người xem nhìn thấy được.

[pause] Nhưng đừng để dáng béo đánh lừa. Ngay cả khi tròn nhất, Sakamoto vẫn nhanh hơn và mạnh hơn gần như mọi đối thủ. Dáng béo chỉ có nghĩa là ông chưa cần nghiêm túc.

[pause] Nhưng hãy nhớ: béo trở lại cũng là một phần của luật. Sau mỗi trận đấu, Sakamoto trở về làm một ông bố, một ông chủ cửa hàng. Cân nặng của ông là cân nặng của cuộc sống bình yên.

[pause] [chuckles] Kaku ghi chú: đây có lẽ là hệ thống sức mạnh duy nhất trong anime mà chỉ số cân nặng là một thanh sức mạnh. Kaku cũng mong ăn bánh xong thì mạnh lên.
```

### c04 · Luật 2: mọi thứ đều là vũ khí

Khoảng 79 giây · cảnh s26–s32 · 1032 ký tự

**Gemini**

```text
Ông còn dùng được những thứ mà người khác không nghĩ tới: một cái móc áo, một chiếc đũa, một thanh kẹo. Với Sakamoto, món đồ không quan trọng bằng cách dùng nó.

<short pause> Luật thứ hai là phong cách của cả bộ truyện: bất cứ vật gì cũng có thể thành vũ khí. Sakamoto đánh bằng thìa, bút bi, túi nhựa, cả chiếc xe đẩy hàng trong siêu thị.

<short pause> Điều này không chỉ để vui. Vì không được giết người, Sakamoto cần những cách đánh gục đối thủ mà không gây chết người. Đồ vật hàng ngày cho ông sự kiểm soát đó.

<short pause> Và đối thủ cũng biết điều đó. Có những sát thủ cố gắng dọn sạch không gian trước khi đấu, để Sakamoto không có gì trong tay. Kết quả thường là… họ vẫn thua.

<short pause> <laugh> Kaku thử áp dụng luật này ở nhà và phát hiện ra mình chỉ biết dùng cuốn sổ làm vũ khí. Có lẽ vì vậy Kaku chỉ làm thư ký.

<short pause> Mỗi trận đấu vì vậy giống như một câu đố: trong không gian này có những đồ vật gì, và dùng chúng thế nào cho thông minh nhất?

<short pause> Và đó cũng là lý do các cảnh đánh trong Sakamoto Days thường đi kèm rất nhiều tiếng cười. Căng thẳng và hài hước cùng tồn tại trong một khung hình.
```

**ElevenLabs**

```text
Ông còn dùng được những thứ mà người khác không nghĩ tới: một cái móc áo, một chiếc đũa, một thanh kẹo. Với Sakamoto, món đồ không quan trọng bằng cách dùng nó.

[pause] Luật thứ hai là phong cách của cả bộ truyện: bất cứ vật gì cũng có thể thành vũ khí. Sakamoto đánh bằng thìa, bút bi, túi nhựa, cả chiếc xe đẩy hàng trong siêu thị.

[pause] Điều này không chỉ để vui. Vì không được giết người, Sakamoto cần những cách đánh gục đối thủ mà không gây chết người. Đồ vật hàng ngày cho ông sự kiểm soát đó.

[pause] Và đối thủ cũng biết điều đó. Có những sát thủ cố gắng dọn sạch không gian trước khi đấu, để Sakamoto không có gì trong tay. Kết quả thường là… họ vẫn thua.

[pause] [chuckles] Kaku thử áp dụng luật này ở nhà và phát hiện ra mình chỉ biết dùng cuốn sổ làm vũ khí. Có lẽ vì vậy Kaku chỉ làm thư ký.

[pause] [curious] Mỗi trận đấu vì vậy giống như một câu đố: trong không gian này có những đồ vật gì, và dùng chúng thế nào cho thông minh nhất?

[pause] Và đó cũng là lý do các cảnh đánh trong Sakamoto Days thường đi kèm rất nhiều tiếng cười. Căng thẳng và hài hước cùng tồn tại trong một khung hình.
```

### c05 · Luật 3: Shin đọc được suy nghĩ

Khoảng 85 giây · cảnh s33–s39 · 1104 ký tự

**Gemini**

```text
Giữa Shin và Sakamoto còn có một kiểu giao tiếp đặc biệt: Sakamoto chỉ cần nghĩ, Shin sẽ hiểu. Trong nhiều trận, hai người phối hợp mà không cần nói một lời.

<short pause> Người trợ thủ đầu tiên của Sakamoto là Asakura Shin, một sát thủ trẻ có khả năng đọc suy nghĩ của người khác. Khả năng này đến từ một thí nghiệm mà cậu từng bị đưa vào.

<short pause> Nghĩa là đối thủ giỏi nhất với Shin là người không suy nghĩ, hoặc người suy nghĩ quá nhiều thứ cùng lúc. Có kẻ thù cố tình nghĩ lung tung để làm nhiễu cậu.

<short pause> Trong chiến đấu, đọc suy nghĩ giúp Shin biết trước đối thủ định làm gì. <short pause> Nhưng nó có giới hạn: phạm vi gần, và nếu đối thủ hành động theo bản năng, không kịp nghĩ, Shin sẽ không đọc trước được.

<short pause> Và đọc suy nghĩ cũng có mặt trái: Shin nghe cả những điều người khác không muốn nói ra. Nhiều tình huống hài nhất của bộ truyện đến từ chuyện này.

<short pause> Ở kỳ thi JCC, Shin không có Sakamoto bên cạnh. Lần đầu tiên, cậu phải tự đưa ra quyết định và bảo vệ người khác bằng chính khả năng của mình.

<short pause> Suốt mùa một, Shin mạnh lên rất nhiều, và ở kỳ thi JCC, cậu gần như là nhân vật chính thứ hai. Hãy nhớ rằng khả năng của cậu vẫn đang phát triển.
```

**ElevenLabs**

```text
Giữa Shin và Sakamoto còn có một kiểu giao tiếp đặc biệt: Sakamoto chỉ cần nghĩ, Shin sẽ hiểu. Trong nhiều trận, hai người phối hợp mà không cần nói một lời.

[pause] Người trợ thủ đầu tiên của Sakamoto là Asakura Shin, một sát thủ trẻ có khả năng đọc suy nghĩ của người khác. Khả năng này đến từ một thí nghiệm mà cậu từng bị đưa vào.

[pause] Nghĩa là đối thủ giỏi nhất với Shin là người không suy nghĩ, hoặc người suy nghĩ quá nhiều thứ cùng lúc. Có kẻ thù cố tình nghĩ lung tung để làm nhiễu cậu.

[pause] Trong chiến đấu, đọc suy nghĩ giúp Shin biết trước đối thủ định làm gì. [pause] Nhưng nó có giới hạn: phạm vi gần, và nếu đối thủ hành động theo bản năng, không kịp nghĩ, Shin sẽ không đọc trước được.

[pause] Và đọc suy nghĩ cũng có mặt trái: Shin nghe cả những điều người khác không muốn nói ra. Nhiều tình huống hài nhất của bộ truyện đến từ chuyện này.

[pause] Ở kỳ thi JCC, Shin không có Sakamoto bên cạnh. Lần đầu tiên, cậu phải tự đưa ra quyết định và bảo vệ người khác bằng chính khả năng của mình.

[pause] Suốt mùa một, Shin mạnh lên rất nhiều, và ở kỳ thi JCC, cậu gần như là nhân vật chính thứ hai. Hãy nhớ rằng khả năng của cậu vẫn đang phát triển.
```

### c06 · Luật 4: những người bạn

Khoảng 76 giây · cảnh s40–s46 · 983 ký tự

**Gemini**

```text
Lu mang theo một món nợ quá khứ: gia đình cô bị cuốn vào những cuộc thanh toán trong giới ngầm, và Sakamoto là người đã che chở cho cô.

<short pause> Lu Shaotang là cô gái đến từ một gia đình mafia Trung Quốc. Cô dùng võ thuật, và có một kiểu quyền rất đặc biệt khi say. Kaku sẽ không khuyến khích bạn thử.

<short pause> Chú vẹt của Heisuke không chỉ là thú cưng. Nó là người bạn duy nhất của anh trong nhiều năm, và có những lúc chính chú vẹt quyết định số phận trận đấu.

<short pause> Heisuke là một tay bắn tỉa vụng về nhưng tốt bụng, đi cùng một chú vẹt. Anh từng là kẻ thù, rồi trở thành người của cửa hàng.

<short pause> Và có vợ Sakamoto, Aoi. Cô không phải sát thủ, nhưng là người đặt luật cho cả nhà: không giết người, không làm điều gì khiến gia đình gặp nguy hiểm.

<short pause> Aoi còn là lý do khiến cửa hàng trở thành một gia đình thay vì một băng nhóm. Ai vào làm cũng phải tuân theo luật nhà, kể cả những sát thủ từng là kẻ thù.

<short pause> <laugh> Kaku để ý: trong một bộ truyện về sát thủ, người đáng sợ nhất với nhân vật chính lại là người vợ không cầm vũ khí.
```

**ElevenLabs**

```text
Lu mang theo một món nợ quá khứ: gia đình cô bị cuốn vào những cuộc thanh toán trong giới ngầm, và Sakamoto là người đã che chở cho cô.

[pause] Lu Shaotang là cô gái đến từ một gia đình mafia Trung Quốc. Cô dùng võ thuật, và có một kiểu quyền rất đặc biệt khi say. Kaku sẽ không khuyến khích bạn thử.

[pause] Chú vẹt của Heisuke không chỉ là thú cưng. Nó là người bạn duy nhất của anh trong nhiều năm, và có những lúc chính chú vẹt quyết định số phận trận đấu.

[pause] Heisuke là một tay bắn tỉa vụng về nhưng tốt bụng, đi cùng một chú vẹt. Anh từng là kẻ thù, rồi trở thành người của cửa hàng.

[pause] Và có vợ Sakamoto, Aoi. Cô không phải sát thủ, nhưng là người đặt luật cho cả nhà: không giết người, không làm điều gì khiến gia đình gặp nguy hiểm.

[pause] Aoi còn là lý do khiến cửa hàng trở thành một gia đình thay vì một băng nhóm. Ai vào làm cũng phải tuân theo luật nhà, kể cả những sát thủ từng là kẻ thù.

[pause] [chuckles] Kaku để ý: trong một bộ truyện về sát thủ, người đáng sợ nhất với nhân vật chính lại là người vợ không cầm vũ khí.
```

### c07 · Các phe phái

Khoảng 105 giây · cảnh s47–s55 · 1368 ký tự

**Gemini**

```text
Giờ tới bản đồ các phe. Phe thứ nhất: cửa hàng Sakamoto, gồm Sakamoto, Shin, Lu, Heisuke và những người bạn. Mục tiêu: sống yên ổn và bảo vệ gia đình.

<short pause> Order có những gương mặt rất khác nhau: một người điềm tĩnh và cực nhanh, một cô gái trẻ thanh lịch với lưỡi cưa, và một ông lão kiếm sĩ huyền thoại mà ngay cả Order cũng kiêng dè.

<short pause> Luật của Hội rất rõ: giới sát thủ có trật tự, có đẳng cấp, và ai phá trật tự sẽ bị Order xử lý. Việc cả giới treo thưởng cho Sakamoto khiến trật tự ấy bắt đầu lung lay.

<short pause> Phe thứ hai: Hội Sát thủ và JCC. Đứng đầu là một nhóm sát thủ mạnh nhất gọi là Order, đội cảnh sát của giới sát thủ, chuyên xử lý những kẻ gây rối.

<short pause> Trong Order có Nagumo, bạn học cũ thời JCC của Sakamoto, bậc thầy cải trang, lúc nào cũng cười. Không ai chắc anh ta đứng về phía nào.

<short pause> Điều đáng sợ ở Slur không phải sức mạnh, mà là hắn có tầm nhìn. Hắn không chỉ muốn giết Sakamoto. Hắn muốn thay đổi cả thế giới sát thủ, và sẵn sàng hi sinh bất kỳ ai cho mục tiêu đó.

<short pause> Phe thứ ba: Slur và những kẻ đi theo hắn. Hắn thuê tử tù, gây hỗn loạn, và muốn phá vỡ trật tự của Hội.

<short pause> Và giữa các phe là những nhân vật chưa rõ lập trường, trong đó có hai học viên trẻ ở JCC là Toramaru và Mafuyu, những người mà ở cuối mùa một bị Slur để mắt tới.

<short pause> Kaku ghi chú: trong Sakamoto Days, ranh giới giữa bạn và thù thay đổi rất nhanh. Nhiều kẻ thù của mùa một giờ đang đứng cùng phe với Sakamoto.
```

**ElevenLabs**

```text
Giờ tới bản đồ các phe. Phe thứ nhất: cửa hàng Sakamoto, gồm Sakamoto, Shin, Lu, Heisuke và những người bạn. Mục tiêu: sống yên ổn và bảo vệ gia đình.

[pause] Order có những gương mặt rất khác nhau: một người điềm tĩnh và cực nhanh, một cô gái trẻ thanh lịch với lưỡi cưa, và một ông lão kiếm sĩ huyền thoại mà ngay cả Order cũng kiêng dè.

[pause] Luật của Hội rất rõ: giới sát thủ có trật tự, có đẳng cấp, và ai phá trật tự sẽ bị Order xử lý. Việc cả giới treo thưởng cho Sakamoto khiến trật tự ấy bắt đầu lung lay.

[pause] Phe thứ hai: Hội Sát thủ và JCC. Đứng đầu là một nhóm sát thủ mạnh nhất gọi là Order, đội cảnh sát của giới sát thủ, chuyên xử lý những kẻ gây rối.

[pause] Trong Order có Nagumo, bạn học cũ thời JCC của Sakamoto, bậc thầy cải trang, lúc nào cũng cười. Không ai chắc anh ta đứng về phía nào.

[pause] Điều đáng sợ ở Slur không phải sức mạnh, mà là hắn có tầm nhìn. Hắn không chỉ muốn giết Sakamoto. Hắn muốn thay đổi cả thế giới sát thủ, và sẵn sàng hi sinh bất kỳ ai cho mục tiêu đó.

[pause] Phe thứ ba: Slur và những kẻ đi theo hắn. Hắn thuê tử tù, gây hỗn loạn, và muốn phá vỡ trật tự của Hội.

[pause] Và giữa các phe là những nhân vật chưa rõ lập trường, trong đó có hai học viên trẻ ở JCC là Toramaru và Mafuyu, những người mà ở cuối mùa một bị Slur để mắt tới.

[pause] Kaku ghi chú: trong Sakamoto Days, ranh giới giữa bạn và thù thay đổi rất nhanh. Nhiều kẻ thù của mùa một giờ đang đứng cùng phe với Sakamoto.
```

### c08 · Nút thắt 1: Slur là ai? / Nút thắt 2: quá khứ của Sakamoto

Khoảng 114 giây · cảnh s56–s65 · 1488 ký tự

**Gemini**

```text
Có những lúc Slur dường như nói chuyện với chính mình, như thể trong hắn có hai giọng nói. Kaku ghi đây là một chi tiết đáng để ý, không giải thích thêm.

<short pause> Nút thắt lớn nhất: Slur thật sự là ai, và vì sao hắn nhắm vào Sakamoto? Mùa một để lại vài manh mối, nhưng chưa có câu trả lời.

<short pause> Và hắn chọn đúng thời điểm Sakamoto đã giải nghệ, tăng cân, có gia đình để ra tay. Một kẻ hiểu rằng điểm yếu lớn nhất của người mạnh nhất chính là những người ông yêu thương.

<short pause> Hắn dường như biết rất rõ về Sakamoto và về JCC. Và hắn nói về việc xây dựng một trật tự mới cho giới sát thủ, như thể hắn từng là người trong cuộc.

<short pause> <laugh> Kaku không spoiler. <short pause> Nhưng nếu bạn để ý những chi tiết về quá khứ JCC trong mùa hai, bạn sẽ đoán được nhiều điều.

<short pause> Mùa một chỉ hé lộ những mảnh nhỏ: Sakamoto từng học ở JCC, từng là thành viên Order, và từng có những người bạn cùng khóa mà giờ đi theo những con đường rất khác nhau.

<short pause> Nút thắt thứ hai: quá khứ của chính Sakamoto. Ông đã trở thành sát thủ mạnh nhất thế nào, ai là thầy, ai là bạn, và điều gì khiến ông sẵn sàng bỏ tất cả để giải nghệ?

<short pause> Kaku đoán arc quá khứ sẽ thay đổi cách bạn nhìn nhiều nhân vật, kể cả những người bạn tưởng đã hiểu rõ. Đây là lý do nên xem lại mùa một trước khi xem mùa hai.

<short pause> Theo thông tin về mùa hai, anime sẽ đi vào arc quá khứ của Sakamoto. Đây là phần nhiều fan manga đánh giá rất cao.

<short pause> Hãy nhớ lại mối quan hệ giữa Sakamoto và Nagumo ở mùa một. Họ trêu nhau như bạn cũ, nhưng cũng từng chĩa vũ khí vào nhau. Điều đó sẽ có ý nghĩa hơn khi quá khứ được kể.
```

**ElevenLabs**

```text
Có những lúc Slur dường như nói chuyện với chính mình, như thể trong hắn có hai giọng nói. Kaku ghi đây là một chi tiết đáng để ý, không giải thích thêm.

[pause] [curious] Nút thắt lớn nhất: Slur thật sự là ai, và vì sao hắn nhắm vào Sakamoto? Mùa một để lại vài manh mối, nhưng chưa có câu trả lời.

[pause] Và hắn chọn đúng thời điểm Sakamoto đã giải nghệ, tăng cân, có gia đình để ra tay. Một kẻ hiểu rằng điểm yếu lớn nhất của người mạnh nhất chính là những người ông yêu thương.

[pause] Hắn dường như biết rất rõ về Sakamoto và về JCC. Và hắn nói về việc xây dựng một trật tự mới cho giới sát thủ, như thể hắn từng là người trong cuộc.

[pause] [chuckles] Kaku không spoiler. [pause] Nhưng nếu bạn để ý những chi tiết về quá khứ JCC trong mùa hai, bạn sẽ đoán được nhiều điều.

[pause] Mùa một chỉ hé lộ những mảnh nhỏ: Sakamoto từng học ở JCC, từng là thành viên Order, và từng có những người bạn cùng khóa mà giờ đi theo những con đường rất khác nhau.

[pause] Nút thắt thứ hai: quá khứ của chính Sakamoto. Ông đã trở thành sát thủ mạnh nhất thế nào, ai là thầy, ai là bạn, và điều gì khiến ông sẵn sàng bỏ tất cả để giải nghệ?

[pause] Kaku đoán arc quá khứ sẽ thay đổi cách bạn nhìn nhiều nhân vật, kể cả những người bạn tưởng đã hiểu rõ. Đây là lý do nên xem lại mùa một trước khi xem mùa hai.

[pause] Theo thông tin về mùa hai, anime sẽ đi vào arc quá khứ của Sakamoto. Đây là phần nhiều fan manga đánh giá rất cao.

[pause] Hãy nhớ lại mối quan hệ giữa Sakamoto và Nagumo ở mùa một. Họ trêu nhau như bạn cũ, nhưng cũng từng chĩa vũ khí vào nhau. Điều đó sẽ có ý nghĩa hơn khi quá khứ được kể.
```

### c09 · Nút thắt 3: quy tắc không giết người / Ba điều nên để ý ở mùa mới

Khoảng 120 giây · cảnh s66–s77 · 1559 ký tự

**Gemini**

```text
Nút thắt thứ ba không nằm trong cốt truyện, mà nằm trong luật chơi: quy tắc không giết người sẽ còn đứng vững bao lâu?

<short pause> Và quy tắc này còn áp dụng cho cả những người ở cửa hàng. Shin, Lu, Heisuke đều phải chiến đấu theo cách của Sakamoto, dù đối thủ của họ không hề nương tay.

<short pause> Kẻ thù ngày càng mạnh, và nhiều kẻ không ngần ngại giết người. Mỗi trận, Sakamoto phải thắng với một tay bị trói sau lưng.

<short pause> Kaku nghĩ nếu có một ngày quy tắc này bị phá, đó sẽ là khoảnh khắc lớn nhất của cả bộ truyện. Còn trước ngày đó, mỗi trận thắng đều là một lần lời hứa được giữ.

<short pause> Đây là nguồn căng thẳng thú vị nhất của bộ truyện: không phải Sakamoto có thắng không, mà là ông có thắng được mà vẫn giữ lời hứa không.

<short pause> <laugh> Giờ là ba điều Kaku gợi ý bạn để ý khi xem mùa hai.

<short pause> Học viện JCC là một nơi đầy đồ vật lạ: phòng thí nghiệm, thư viện, phòng tập, căng tin. Kaku đoán mùa hai sẽ có những món vũ khí bất ngờ nhất từ trước tới nay.

<short pause> Một: để ý những đồ vật trong khung hình. Trong mỗi trận đấu, gần như món đồ nào xuất hiện cũng sẽ được dùng. Thử đoán trước xem món nào sẽ thành vũ khí.

<short pause> Hai: để ý cân nặng của Sakamoto. Mỗi lần ông gầy đi là một tín hiệu: trận đấu đã nghiêm trọng tới mức ông không thể đùa nữa.

<short pause> Ba: để ý những gì Shin nghe được mà không nói ra. Khả năng đọc suy nghĩ của cậu thường là cách truyện giấu manh mối ngay trước mắt người xem.

<short pause> Nhất là khi mùa hai đưa Sakamoto rời xa cửa hàng. Mỗi lần ông nhớ tới nhà là một lần ta hiểu vì sao ông chiến đấu.

<short pause> Và một điều bonus: đừng bỏ qua những cảnh gia đình. Trong Sakamoto Days, những bữa cơm ở nhà chính là lý do cho mọi trận đánh.
```

**ElevenLabs**

```text
[curious] Nút thắt thứ ba không nằm trong cốt truyện, mà nằm trong luật chơi: quy tắc không giết người sẽ còn đứng vững bao lâu?

[pause] Và quy tắc này còn áp dụng cho cả những người ở cửa hàng. Shin, Lu, Heisuke đều phải chiến đấu theo cách của Sakamoto, dù đối thủ của họ không hề nương tay.

[pause] Kẻ thù ngày càng mạnh, và nhiều kẻ không ngần ngại giết người. Mỗi trận, Sakamoto phải thắng với một tay bị trói sau lưng.

[pause] Kaku nghĩ nếu có một ngày quy tắc này bị phá, đó sẽ là khoảnh khắc lớn nhất của cả bộ truyện. Còn trước ngày đó, mỗi trận thắng đều là một lần lời hứa được giữ.

[pause] Đây là nguồn căng thẳng thú vị nhất của bộ truyện: không phải Sakamoto có thắng không, mà là ông có thắng được mà vẫn giữ lời hứa không.

[pause] [chuckles] Giờ là ba điều Kaku gợi ý bạn để ý khi xem mùa hai.

[pause] Học viện JCC là một nơi đầy đồ vật lạ: phòng thí nghiệm, thư viện, phòng tập, căng tin. Kaku đoán mùa hai sẽ có những món vũ khí bất ngờ nhất từ trước tới nay.

[pause] Một: để ý những đồ vật trong khung hình. Trong mỗi trận đấu, gần như món đồ nào xuất hiện cũng sẽ được dùng. Thử đoán trước xem món nào sẽ thành vũ khí.

[pause] Hai: để ý cân nặng của Sakamoto. Mỗi lần ông gầy đi là một tín hiệu: trận đấu đã nghiêm trọng tới mức ông không thể đùa nữa.

[pause] Ba: để ý những gì Shin nghe được mà không nói ra. Khả năng đọc suy nghĩ của cậu thường là cách truyện giấu manh mối ngay trước mắt người xem.

[pause] Nhất là khi mùa hai đưa Sakamoto rời xa cửa hàng. Mỗi lần ông nhớ tới nhà là một lần ta hiểu vì sao ông chiến đấu.

[pause] Và một điều bonus: đừng bỏ qua những cảnh gia đình. Trong Sakamoto Days, những bữa cơm ở nhà chính là lý do cho mọi trận đánh.
```

### c10 · Kết

Khoảng 60 giây · cảnh s78–s82 · 775 ký tự

**Gemini**

```text
Sakamoto Days là một bộ truyện về một người đàn ông mạnh nhất thế giới, người chỉ muốn được về nhà ăn tối đúng giờ. Và vì vậy mà mọi trận đấu của ông đều đáng xem.

<short pause> Và nếu bạn chưa xem mùa một, video này cũng là bản tóm tắt đủ để bắt đầu. <short pause> Nhưng Kaku vẫn khuyên xem mùa một, vì những trận đánh bằng đồ vật khó kể lại bằng lời.

<short pause> Xem xong vài tập đầu mùa hai, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không. Và nếu bạn đã đọc manga, nhớ đánh dấu spoiler khi bình luận nhé.

<short pause> Video tiếp theo, Kaku bước vào một thế giới game thực tế ảo: Shangri-La Frontier. Kaku sẽ đọc bảng chỉ số của người chơi như đọc một nhân vật game thật.

<short pause> <laugh> Nếu video ôn tập này giúp bạn sẵn sàng cho mùa mới, hãy đăng ký kênh để Kaku ôn thêm các bộ khác trước khi chúng trở lại. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Sakamoto Days là một bộ truyện về một người đàn ông mạnh nhất thế giới, người chỉ muốn được về nhà ăn tối đúng giờ. Và vì vậy mà mọi trận đấu của ông đều đáng xem.

[pause] Và nếu bạn chưa xem mùa một, video này cũng là bản tóm tắt đủ để bắt đầu. [pause] Nhưng Kaku vẫn khuyên xem mùa một, vì những trận đánh bằng đồ vật khó kể lại bằng lời.

[pause] Xem xong vài tập đầu mùa hai, hãy quay lại đây xem ba điều Kaku gợi ý có đúng không. Và nếu bạn đã đọc manga, nhớ đánh dấu spoiler khi bình luận nhé.

[pause] Video tiếp theo, Kaku bước vào một thế giới game thực tế ảo: Shangri-La Frontier. Kaku sẽ đọc bảng chỉ số của người chơi như đọc một nhân vật game thật.

[pause] [chuckles] Nếu video ôn tập này giúp bạn sẵn sàng cho mùa mới, hãy đăng ký kênh để Kaku ôn thêm các bộ khác trước khi chúng trở lại. Kaku gấp sổ đây, hẹn gặp lại!
```
