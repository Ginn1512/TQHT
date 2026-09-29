# Bộ prompt · Kimetsu no Yaiba: Phân tích chiến thuật trận Tanjiro vs Rui

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 89 ảnh, 8 đoạn đọc, khoảng 15.4 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (89 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu: tỉ số trước trận

Lời: Cảnh báo: video phân tích chi tiết trận đấu trên núi Natagumo trong Kimetsu no Yaiba mùa một, bao gồm cả kết…

```text
Wide 16:9 landscape cinematic frame. a dark mountain forest at night, fine silver threads glinting between the trees under the moon. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Nếu có nhà cái nào nhận cược trận này, tỉ lệ sẽ chênh lệch tới mức nực cười. Một bên là kiếm sĩ cấp thấp nhất…

```text
Wide 16:9 landscape cinematic frame. a betting board with two silhouettes: a small swordsman and a child-sized figure on a web, odds wildly uneven. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trên giấy tờ, cậu kiếm sĩ gần như không có cửa thắng. Và đúng là cậu không thắng theo cách mà ta nghĩ.

```text
Wide 16:9 landscape cinematic frame. a sword stuck in the ground before a giant web glowing red in the dark. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hôm nay Kaku phân tích trận đấu này như một huấn luyện viên xem lại băng hình. Chia thành sáu hiệp, mỗi hiệp…

```text
Wide 16:9 landscape cinematic frame. the owl mascot with a whistle and clipboard in front of a tactical board with six columns. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ là bảng chiến thuật, và Kaku sẽ vẽ bằng mũi tên, không phải bằng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing arrows and circles on a chalk tactical board. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Bối cảnh: ngọn núi của những sợi tơ

Lời: Kimetsu no Yaiba là manga của Gotouge Koyoharu, được studio ufotable chuyển thể thành anime từ năm 2019. Trận…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside a film reel tied with a simple red ribbon. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Tanjiro, một thiếu niên làm nghề bán than, trở thành kiếm sĩ diệt quỷ sau khi gia đình bị giết và em gái Nezu…

```text
Wide 16:9 landscape cinematic frame. a young swordsman carrying a wooden box on his back walking through a snowy mountain path. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhiệm vụ đưa cậu tới núi Natagumo, nơi một nhóm kiếm sĩ đã mất tích. Ngọn núi đầy tơ nhện, và những người mắc…

```text
Wide 16:9 landscape cinematic frame. a misty mountain slope covered in spider webs, puppet-like silhouettes hanging from threads. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Trên núi có cả một gia đình quỷ nhện: mẹ, cha, anh, chị. Nhưng đó là gia đình giả, bị ép vào vai diễn bởi đứa…

```text
Wide 16:9 landscape cinematic frame. a group of demon silhouettes posed like a family portrait, invisible threads pulling their limbs. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trước khi tới trận chính, Tanjiro và đồng đội đã phải đánh qua mẹ và cha của gia đình đó. Nghĩa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a stamina bar already half empty. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Hồ sơ hai bên

Lời: Hồ sơ bên thứ nhất: Tanjiro. Cấp bậc: thấp nhất trong Sát Quỷ Đoàn, vừa mới vào nghề. Vũ khí: kiếm Nhật Luân.…

```text
Wide 16:9 landscape cinematic frame. a stat card of a young swordsman with a water wave emblem and a low rank badge. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Điểm mạnh: khứu giác cực nhạy, có thể ngửi thấy khe hở trong phòng thủ của đối thủ. Tinh thần không bao giờ b…

```text
Wide 16:9 landscape cinematic frame. a swordsman sniffing the air as faint colored threads of scent reveal a gap in a defense. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Điểm yếu: kinh nghiệm ít, thân thể đã bị thương từ các trận trước, và thanh kiếm chưa đủ sắc để chém vật cứng.

```text
Wide 16:9 landscape cinematic frame. a cracked sword blade and bandaged arm under a dim lantern. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Hồ sơ bên thứ hai: Rui. Cấp bậc: Hạ Huyền Ngũ, thứ năm trong sáu con quỷ Hạ Huyền. Năng lực: điều khiển những…

```text
Wide 16:9 landscape cinematic frame. a stat card of a small pale figure standing on a web, a rank mark glowing in one eye. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Điểm mạnh: tấn công từ xa, bẫy khắp khu rừng, và có thể làm tơ cứng hơn nữa bằng cách truyền máu vào, khiến t…

```text
Wide 16:9 landscape cinematic frame. white threads turning deep red as they harden, slicing through a tree trunk. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Điểm yếu: tự tin thái quá, và một nỗi ám ảnh về gia đình khiến hắn dễ bị cảm xúc chi phối.

```text
Wide 16:9 landscape cinematic frame. a lonely child silhouette sitting on a web, looking at a family portrait with torn edges. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Luật thắng thua

Lời: Trước khi phân tích, cần biết luật của trận đấu. Quỷ trong thế giới này tái tạo cơ thể gần như ngay lập tức.…

```text
Wide 16:9 landscape cinematic frame. a demon silhouette regenerating a severed arm in a swirl of dark energy. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Chỉ có hai cách giết quỷ: cho chúng tiếp xúc với ánh mặt trời, hoặc chém đứt đầu bằng kiếm Nhật Luân, loại ki…

```text
Wide 16:9 landscape cinematic frame. a split image: morning sunlight burning away a shadow, and a glowing blade aimed at a neck. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Trận này diễn ra giữa đêm, bình minh còn rất xa. Vậy Tanjiro chỉ có một mục tiêu duy nhất: cái cổ của Rui.

```text
Wide 16:9 landscape cinematic frame. a tactical board with a single red circle drawn around a neck icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Còn Rui thì chỉ cần giữ Tanjiro ở ngoài tầm kiếm. Một bên cần lao vào, một bên cần giữ khoảng cách. Toàn bộ t…

```text
Wide 16:9 landscape cinematic frame. two range circles on a tactical board, one small around a sword and one very large around a web. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Nhịp thở là vũ khí

Lời: Trước khi vào trận, cần hiểu vì sao cách thở lại quan trọng như vậy trong Kimetsu no Yaiba.

```text
Wide 16:9 landscape cinematic frame. a swordsman meditating by a waterfall, visible breath forming steady swirls. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Kiếm sĩ diệt quỷ được luyện một kỹ thuật thở đặc biệt, giúp đưa thật nhiều không khí vào cơ thể, tăng sức mạn…

```text
Wide 16:9 landscape cinematic frame. a diagram of lungs glowing brighter, muscles and heart highlighted in warm light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Mỗi trường phái hơi thở có phong cách riêng. Hơi thở của Nước uyển chuyển, thích hợp để phản ứng và thay đổi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small family tree diagram of breathing styles pinned to the board. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Nhưng hơi thở cũng là giới hạn. Khi phổi và cơ thể kiệt sức, mọi thế kiếm đều yếu đi. Nên trong trận này, sức…

```text
Wide 16:9 landscape cinematic frame. a stamina meter shaped like lungs, slowly draining as a swordsman pants. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Hãy nhớ điều này, vì bước ngoặt của trận đấu đến chính từ việc Tanjiro thay đổi cách thở.

```text
Wide 16:9 landscape cinematic frame. a single breath of air turning from blue to red in slow motion. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Sơ đồ khoảng cách

Lời: Kaku vẽ ba vòng tròn trên bảng chiến thuật. Vòng trong cùng là tầm kiếm của Tanjiro, chỉ khoảng một cánh tay…

```text
Wide 16:9 landscape cinematic frame. a chalk diagram with a tiny inner circle around a swordsman icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Vòng giữa là tầm tơ của Rui: vài chục mét, bao trùm cả một khoảng rừng. Trong vòng này, tơ có thể tới từ bất…

```text
Wide 16:9 landscape cinematic frame. a larger circle filled with crisscrossing lines around a small central figure. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Vòng ngoài cùng là khu rừng đã giăng bẫy sẵn, nơi Rui kiểm soát mọi lối đi. Tanjiro đang đứng ngay trong lãnh…

```text
Wide 16:9 landscape cinematic frame. an outer ring of the diagram shaded with web patterns and trap marks. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Để thắng, Tanjiro phải đi xuyên qua vòng hai, nơi mỗi bước chân có thể mất một cánh tay. Đây là bài toán của…

```text
Wide 16:9 landscape cinematic frame. an arrow trying to pierce from the outer ring to the center through a dense mesh. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong võ thuật thật, người ta gọi đây là cuộc chiến giữa người đánh xa và người đánh gần. Người…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny spear and a tiny sword, comparing their lengths. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Hiệp 1: thăm dò

Lời: Hiệp một. Mục tiêu của Tanjiro: đánh giá sức mạnh của tơ và tìm đường tiếp cận. Mục tiêu của Rui: dạy cho kẻ…

```text
Wide 16:9 landscape cinematic frame. a swordsman in a ready stance facing a web of threads, both sides studying each other. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Lựa chọn của Tanjiro: dùng các thế của Hơi thở của Nước, vốn uyển chuyển như dòng chảy, để né và cắt tơ trên…

```text
Wide 16:9 landscape cinematic frame. a swordsman flowing through threads with water-like arcs trailing from his blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Kết quả: Tanjiro cắt được tơ thường. Nhưng Rui không vội. Hắn đang quan sát, giống như một người chơi cờ nhườ…

```text
Wide 16:9 landscape cinematic frame. cut threads falling like silver hair as a calm figure watches from above. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Cái giá: Tanjiro tiêu hao sức và để lộ gần hết các thế kiếm của mình. Rui thì chưa dùng tới sức mạnh thật.

```text
Wide 16:9 landscape cinematic frame. a stamina bar dropping for the swordsman while the opponent's bar stays full. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Kaku có một suy luận: giữa một khu rừng phủ kín tơ, khứu giác của Tanjiro khó cho cậu biết sợi nào sắp lao tớ…

```text
Wide 16:9 landscape cinematic frame. a swordsman sniffing the air in confusion as nearly invisible threads approach from behind. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhận xét của Kaku: hiệp này Rui thắng về thông tin. Hắn biết Tanjiro làm được gì, còn Tanjiro chưa biết hắn l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot moving a chess piece while its opponent's pieces remain hidden. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Hiệp 2: thanh kiếm gãy

Lời: Hiệp hai. Rui truyền máu vào tơ. Những sợi tơ chuyển sang màu đỏ, cứng hơn hẳn trước.

```text
Wide 16:9 landscape cinematic frame. white threads flushing red and humming with tension in the moonlight. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Lựa chọn của Tanjiro: vẫn chém thẳng vào tơ để mở đường. Và rồi điều tồi tệ nhất với một kiếm sĩ xảy ra: than…

```text
Wide 16:9 landscape cinematic frame. a sword blade snapping in half against a taut red thread, fragments flying. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Về chiến thuật, đây là khoảnh khắc khủng hoảng. Người đánh gần mất vũ khí đánh gần. Mục tiêu duy nhất, cái cổ…

```text
Wide 16:9 landscape cinematic frame. a tactical board where the inner sword circle is crossed out in red. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Cái giá: không chỉ là thanh kiếm. Tơ bắt đầu cắt vào người Tanjiro. Mỗi giây đứng yên là thêm một vết thương.

```text
Wide 16:9 landscape cinematic frame. a swordsman surrounded by a tightening cage of red threads, small cuts on his arms. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhận xét của Kaku: sai lầm ở đây là chém trực diện vào thứ mình chưa biết độ cứng. Nhưng một kiếm sĩ mới vào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a broken toy sword with a sigh. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Hiệp 3: đòn tâm lý

Lời: Hiệp ba không diễn ra bằng kiếm. Rui chứng kiến Nezuko liều mình che chắn cho anh trai, và nảy ra một ý: hắn…

```text
Wide 16:9 landscape cinematic frame. a small figure on a web reaching out toward a girl shielding her brother. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Đây là chiến thuật tâm lý: chia rẽ hai người, lấy đi điểm tựa tinh thần lớn nhất của Tanjiro.

```text
Wide 16:9 landscape cinematic frame. a thread pulling two silhouettes apart as they reach for each other. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Rui bắt Nezuko, treo cô bé lên bằng tơ, và bắt đầu rút máu của cô. Tanjiro phải chứng kiến tất cả mà không th…

```text
Wide 16:9 landscape cinematic frame. a girl suspended high in a web of threads, a brother on the ground below reaching up. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Lựa chọn của Tanjiro: từ chối mọi thỏa hiệp. Cậu hét lên rằng mối liên kết của hai anh em không phải thứ có t…

```text
Wide 16:9 landscape cinematic frame. a swordsman shouting defiantly with a broken sword in hand, threads all around him. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Cái giá: Tanjiro nổi giận và lao vào, bất chấp nguy hiểm. Về chiến thuật, cơn giận đã giúp cậu tiến vào vòng…

```text
Wide 16:9 landscape cinematic frame. an arrow on the tactical board plunging recklessly into the middle circle. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Hiệp 4: điệu múa của thần lửa

Lời: Hiệp bốn là khoảnh khắc nổi tiếng nhất. Bị dồn vào đường cùng, sắp chết, Tanjiro nhớ lại hình ảnh người cha m…

```text
Wide 16:9 landscape cinematic frame. a man dancing gracefully with a torch in a snowy night, flames tracing circles in the air. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Đó là điệu múa thần lửa, được gia đình cậu múa mỗi dịp năm mới, suốt từ đêm tới sáng, để cầu nguyện với thần…

```text
Wide 16:9 landscape cinematic frame. a family watching a dance under snowfall, the dancer's breath visible as steady clouds. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Lựa chọn của Tanjiro: bỏ Hơi thở của Nước, chuyển sang nhịp thở của điệu múa. Một nhịp thở mà cơ thể cậu chưa…

```text
Wide 16:9 landscape cinematic frame. a swordsman's breath changing from blue water swirls to red flame swirls. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Cùng lúc đó, Nezuko trong cơn mê tỉnh dậy và dùng năng lực máu của mình. Máu của cô bốc cháy, đốt đứt những s…

```text
Wide 16:9 landscape cinematic frame. a girl in the web igniting in pink flame, the fire racing along the threads toward the swordsman's blade. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Đây là sự phối hợp hoàn hảo: nhịp thở mới cho Tanjiro sức mạnh, lửa của Nezuko cho lưỡi kiếm khả năng cắt tơ.…

```text
Wide 16:9 landscape cinematic frame. a tactical board with two arrows, red and pink, merging into one and piercing the center. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Tanjiro vượt qua vòng tơ và chém trúng cổ của Rui. Trong anime, cảnh này được xem là một trong những khoảnh k…

```text
Wide 16:9 landscape cinematic frame. a burning blade slicing through a storm of threads in a spiral of fire, dramatic low angle. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Cái giá: cơ thể Tanjiro hoàn toàn kiệt quệ. Cậu dùng một nhịp thở mà cơ thể chưa quen, và phải trả bằng mọi s…

```text
Wide 16:9 landscape cinematic frame. a swordsman collapsing onto the forest floor, smoke rising from his broken blade. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Hiệp 5: cú lừa

Lời: Nhưng khi Tanjiro ngã xuống, tưởng đã thắng, Rui vẫn đứng đó. Chuyện gì đã xảy ra?

```text
Wide 16:9 landscape cinematic frame. a pale figure standing untouched among falling ash, head intact. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Hóa ra ngay trước khi lưỡi kiếm chạm tới, Rui đã tự cắt đầu mình bằng tơ. Đầu hắn rời ra do chính hắn, không…

```text
Wide 16:9 landscape cinematic frame. a slow-motion diagram showing a thread cutting just ahead of a blade's path. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Về chiến thuật, đây là một cú lừa thông minh. Tanjiro tưởng đã đạt mục tiêu, và buông lỏng đúng lúc nguy hiểm…

```text
Wide 16:9 landscape cinematic frame. a tactical board with a green check mark that turns into a red question mark. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Cái giá của Rui: gần như không có. Hắn chỉ cần nối đầu lại. Còn Tanjiro giờ nằm bất động, không còn sức đứng…

```text
Wide 16:9 landscape cinematic frame. a regenerating neck stitched together by threads, a fallen swordsman in the background. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhận xét của Kaku: bài học lớn nhất của hiệp này là đừng bao giờ ăn mừng trước khi chắc chắn. Với quỷ, chưa t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot stopping itself mid-celebration, confetti frozen in the air. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Hiệp 6: người thứ ba

Lời: Hiệp cuối. Rui chuẩn bị kết liễu Tanjiro bằng đòn tơ mạnh nhất của mình. Đúng lúc đó, một kiếm sĩ khác xuất h…

```text
Wide 16:9 landscape cinematic frame. a calm swordsman in a plain dark cloak stepping between a fallen boy and a web of threads. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Anh dùng một thế kiếm do chính mình tạo ra, gọi là Lặng sóng. Trong phạm vi của thế kiếm này, mọi đòn tấn côn…

```text
Wide 16:9 landscape cinematic frame. a perfectly still water surface around a standing swordsman, threads dissolving as they enter it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Đòn tơ mạnh nhất của Rui, thứ đã suýt giết Tanjiro, tan biến trước một người đứng yên. Rồi đầu của Rui rơi xu…

```text
Wide 16:9 landscape cinematic frame. a single clean arc of light, a thread web collapsing like falling snow. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Về chiến thuật, đây là minh họa khoảng cách giữa người mới vào nghề và một Trụ cột. Không phải vì kỹ thuật kh…

```text
Wide 16:9 landscape cinematic frame. a tactical board with two water wave icons, one small and rough, one large and perfectly smooth. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhận xét của Kaku: nhưng đừng nghĩ Tanjiro thua. Cậu đã làm được điều không ai ngờ: buộc một Hạ Huyền phải dù…

```text
Wide 16:9 landscape cinematic frame. the owl mascot giving a small medal to a sleeping swordsman figurine. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Những trận đấu song song

Lời: Trận của Tanjiro không diễn ra một mình. Trên cùng ngọn núi, cùng lúc, đồng đội của cậu cũng đang chiến đấu v…

```text
Wide 16:9 landscape cinematic frame. a mountain map with several glowing battle markers scattered across it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Một đồng đội nhút nhát nhưng cực nhanh phải đối mặt với con quỷ có độc biến người thành nhện. Người kia, kiếm…

```text
Wide 16:9 landscape cinematic frame. two separate battles: a trembling swordsman facing a spider-like creature, and a wild fighter facing a hulking brute. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Về chiến thuật, việc bị chia cắt là điều tồi tệ. Ba người mới vào nghề, mỗi người một nơi, không ai hỗ trợ đư…

```text
Wide 16:9 landscape cinematic frame. a tactical board with three isolated friendly markers surrounded by red zones. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Đó là lý do Sát Quỷ Đoàn phải cử tới hai Trụ cột. Khi đối thủ là một Hạ Huyền, những kiếm sĩ cấp thấp chỉ có…

```text
Wide 16:9 landscape cinematic frame. two powerful silhouettes running through the forest at night toward the battle markers. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: bài học ở đây rất thực tế. Khi bước vào lãnh thổ của đối thủ, đừng tách nhóm nếu không có kế ho…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding three tiny walkie-talkies, handing them out. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Nếu… thì: ba kịch bản khác · **Kaku** (đính kèm ảnh mẫu)

Lời: Huấn luyện viên nào cũng thích hỏi nếu. Đây là ba kịch bản khác của trận đấu, theo suy luận của Kaku.

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping between three alternate tactical boards. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nếu Tanjiro không chém thẳng vào tơ đỏ ở hiệp hai, thanh kiếm có thể không gãy. Nhưng cậu cũng không biết đượ…

```text
Wide 16:9 landscape cinematic frame. an unbroken sword and a question mark over a still-intact red web. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nếu Nezuko không tỉnh dậy đúng lúc, lưỡi kiếm gãy của Tanjiro gần như chắc chắn không cắt nổi tơ đỏ. Trận đấu…

```text
Wide 16:9 landscape cinematic frame. a broken blade bouncing off a red thread, sparks flying uselessly. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu Trụ cột đến sớm hơn năm phút, Tanjiro có lẽ không bao giờ nhớ lại điệu múa của cha. Và câu chuyện sau này…

```text
Wide 16:9 landscape cinematic frame. a clock showing five minutes earlier, with a faint image of a fire dance fading away. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và một kịch bản vui: nếu Tanjiro giả vờ đồng ý để Rui nhận Nezuko làm em, rồi bất ngờ tấn công? Kaku nghĩ Tan…

```text
Wide 16:9 landscape cinematic frame. a swordsman trying to fake a smile but his face twisting awkwardly, a sweat drop on his forehead. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đôi khi trận thua lại quan trọng hơn trận thắng, vì nó mở ra một cánh cửa mà trận thắng dễ dàng…

```text
Wide 16:9 landscape cinematic frame. a door opening in a dark forest with warm firelight pouring out. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Bài học chiến thuật

Lời: Tổng kết lại, trận đấu này để lại năm bài học chiến thuật.

```text
Wide 16:9 landscape cinematic frame. a tactical board with five numbered chalk notes. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Một: xác định mục tiêu duy nhất. Với quỷ, chỉ có cái cổ. Mọi động tác thừa đều là lãng phí sức lực.

```text
Wide 16:9 landscape cinematic frame. a single red circle on a neck icon, all other targets crossed out. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Hai: thu thập thông tin trước khi dồn sức. Hiệp một và hai cho thấy cái giá của việc tấn công khi chưa biết đ…

```text
Wide 16:9 landscape cinematic frame. a magnifying glass over a red thread, measuring its thickness. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Ba: phối hợp tạo ra thứ mà một người không làm được. Nhịp thở mới cộng với lửa của em gái mới đủ phá được lồn…

```text
Wide 16:9 landscape cinematic frame. two hands, one holding a sword and one wreathed in pink flame, gripping the same hilt. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Bốn: đừng ăn mừng sớm. Năm: độ tinh luyện quan trọng hơn số lượng chiêu thức. Một thế kiếm hoàn hảo đánh bại…

```text
Wide 16:9 landscape cinematic frame. a single perfect ripple on water beside a messy splash. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Góc nhìn của Kaku: gia đình giả và sợi dây thật · **Kaku** (đính kèm ảnh mẫu)

Lời: Bỏ bảng chiến thuật sang một bên, Kaku muốn nói về điều khiến trận đấu này đáng nhớ hơn mọi đường kiếm.

```text
Wide 16:9 landscape cinematic frame. the owl mascot setting down its whistle and sitting quietly by a campfire. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Rui dùng tơ để trói buộc một gia đình giả. Mọi thành viên phải đóng đúng vai, ai sai thì bị trừng phạt. Hắn n…

```text
Wide 16:9 landscape cinematic frame. puppet-like figures connected to a small central figure by taut red threads. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Tanjiro và Nezuko không có sợi dây nào nối với nhau. Nhưng khi anh sắp chết, em gái tỉnh dậy. Khi em bị treo…

```text
Wide 16:9 landscape cinematic frame. a brother and sister back to back in the forest, no threads between them, warm light around them. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Về sau, truyện cho thấy Rui từng là một đứa trẻ ốm yếu. Hắn đã hiểu sai về gia đình từ rất sớm, và trả giá bằ…

```text
Wide 16:9 landscape cinematic frame. a small sick child in a futon looking out a window at his parents in the garden. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Kaku nghĩ đó là lý do trận đấu này được nhớ lâu: nó không chỉ là cuộc chiến giữa kiếm và tơ, mà giữa hai cách…

```text
Wide 16:9 landscape cinematic frame. a single broken red thread drifting down onto the forest floor at dawn. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Kết

Lời: Tóm lại: một kiếm sĩ cấp thấp nhất gặp một Hạ Huyền trong lãnh thổ của hắn. Mất kiếm, mất em gái, suýt mất mạ…

```text
Wide 16:9 landscape cinematic frame. a summary tactical board with six columns, each with a small icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Và dù người kết liễu Rui là một Trụ cột, trận đấu này là lúc Tanjiro thật sự trở thành một kiếm sĩ.

```text
Wide 16:9 landscape cinematic frame. a young swordsman sleeping peacefully under a tree as sunrise breaks over the mountain. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: bạn muốn Kaku phân tích trận đấu nào tiếp theo bằng bảng chiến thuật? Viết tên trận vào phần…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a blank tactical board toward the viewer. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Video tới, Kaku mở lại tập một của một bộ truyện khác, và chỉ cho bạn những chi tiết cài cắm mà tác giả đã gi…

```text
Wide 16:9 landscape cinematic frame. a very first page of a book with tiny hidden symbols glowing in the margins. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh nếu bạn thấy phân tích hữu ích. Huấn luyện viên Kaku thổi còi hết giờ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot blowing a whistle and waving from the sideline of a chalk field. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu: tỉ số trước trận / Bối cảnh: ngọn núi của những sợi tơ

Khoảng 115 giây · cảnh s01–s10 · 1490 ký tự

**Gemini**

```text
Cảnh báo: video phân tích chi tiết trận đấu trên núi Natagumo trong Kimetsu no Yaiba mùa một, bao gồm cả kết quả. Nếu chưa xem, hãy xem trước rồi quay lại nhé.

<short pause> Nếu có nhà cái nào nhận cược trận này, tỉ lệ sẽ chênh lệch tới mức nực cười. Một bên là kiếm sĩ cấp thấp nhất của Sát Quỷ Đoàn. Bên kia là một trong mười hai con quỷ mạnh nhất dưới trướng chúa quỷ.

<short pause> Trên giấy tờ, cậu kiếm sĩ gần như không có cửa thắng. Và đúng là cậu không thắng theo cách mà ta nghĩ.

<short pause> <laugh> Hôm nay Kaku phân tích trận đấu này như một huấn luyện viên xem lại băng hình. Chia thành sáu hiệp, mỗi hiệp ba câu hỏi: mục tiêu là gì, lựa chọn là gì, và cái giá là gì.

<short pause> Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ là bảng chiến thuật, và Kaku sẽ vẽ bằng mũi tên, không phải bằng cảnh phim.

<short pause> Kimetsu no Yaiba là manga của Gotouge Koyoharu, được studio ufotable chuyển thể thành anime từ năm 2019. Trận đấu hôm nay nằm ở cuối mùa một.

<short pause> Tanjiro, một thiếu niên làm nghề bán than, trở thành kiếm sĩ diệt quỷ sau khi gia đình bị giết và em gái Nezuko bị biến thành quỷ. Cô bé vẫn giữ được lý trí và đi cùng anh.

<short pause> Nhiệm vụ đưa cậu tới núi Natagumo, nơi một nhóm kiếm sĩ đã mất tích. Ngọn núi đầy tơ nhện, và những người mắc vào tơ bị điều khiển như con rối.

<short pause> Trên núi có cả một gia đình quỷ nhện: mẹ, cha, anh, chị. <short pause> Nhưng đó là gia đình giả, bị ép vào vai diễn bởi đứa con nhỏ nhất, kẻ mạnh nhất.

<short pause> Kaku ghi chú: trước khi tới trận chính, Tanjiro và đồng đội đã phải đánh qua mẹ và cha của gia đình đó. Nghĩa là cậu bước vào trận này khi đã rất mệt.
```

**ElevenLabs**

```text
Cảnh báo: video phân tích chi tiết trận đấu trên núi Natagumo trong Kimetsu no Yaiba mùa một, bao gồm cả kết quả. Nếu chưa xem, hãy xem trước rồi quay lại nhé.

[pause] Nếu có nhà cái nào nhận cược trận này, tỉ lệ sẽ chênh lệch tới mức nực cười. Một bên là kiếm sĩ cấp thấp nhất của Sát Quỷ Đoàn. Bên kia là một trong mười hai con quỷ mạnh nhất dưới trướng chúa quỷ.

[pause] Trên giấy tờ, cậu kiếm sĩ gần như không có cửa thắng. Và đúng là cậu không thắng theo cách mà ta nghĩ.

[pause] [chuckles] Hôm nay Kaku phân tích trận đấu này như một huấn luyện viên xem lại băng hình. Chia thành sáu hiệp, mỗi hiệp ba câu hỏi: mục tiêu là gì, lựa chọn là gì, và cái giá là gì.

[pause] Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ là bảng chiến thuật, và Kaku sẽ vẽ bằng mũi tên, không phải bằng cảnh phim.

[pause] Kimetsu no Yaiba là manga của Gotouge Koyoharu, được studio ufotable chuyển thể thành anime từ năm 2019. Trận đấu hôm nay nằm ở cuối mùa một.

[pause] Tanjiro, một thiếu niên làm nghề bán than, trở thành kiếm sĩ diệt quỷ sau khi gia đình bị giết và em gái Nezuko bị biến thành quỷ. Cô bé vẫn giữ được lý trí và đi cùng anh.

[pause] Nhiệm vụ đưa cậu tới núi Natagumo, nơi một nhóm kiếm sĩ đã mất tích. Ngọn núi đầy tơ nhện, và những người mắc vào tơ bị điều khiển như con rối.

[pause] Trên núi có cả một gia đình quỷ nhện: mẹ, cha, anh, chị. [pause] Nhưng đó là gia đình giả, bị ép vào vai diễn bởi đứa con nhỏ nhất, kẻ mạnh nhất.

[pause] Kaku ghi chú: trước khi tới trận chính, Tanjiro và đồng đội đã phải đánh qua mẹ và cha của gia đình đó. Nghĩa là cậu bước vào trận này khi đã rất mệt.
```

### c02 · Hồ sơ hai bên / Luật thắng thua / Nhịp thở là vũ khí

Khoảng 151 giây · cảnh s11–s25 · 1959 ký tự

**Gemini**

```text
Hồ sơ bên thứ nhất: Tanjiro. Cấp bậc: thấp nhất trong Sát Quỷ Đoàn, vừa mới vào nghề. Vũ khí: kiếm Nhật Luân. Kỹ thuật: Hơi thở của Nước.

<short pause> Điểm mạnh: khứu giác cực nhạy, có thể ngửi thấy khe hở trong phòng thủ của đối thủ. Tinh thần không bao giờ bỏ cuộc. Và một em gái có năng lực của quỷ đứng về phía mình.

<short pause> Điểm yếu: kinh nghiệm ít, thân thể đã bị thương từ các trận trước, và thanh kiếm chưa đủ sắc để chém vật cứng.

<short pause> Hồ sơ bên thứ hai: Rui. Cấp bậc: Hạ Huyền Ngũ, thứ năm trong sáu con quỷ Hạ Huyền. Năng lực: điều khiển những sợi tơ còn cứng hơn thép.

<short pause> Điểm mạnh: tấn công từ xa, bẫy khắp khu rừng, và có thể làm tơ cứng hơn nữa bằng cách truyền máu vào, khiến tơ chuyển màu đỏ.

<short pause> Điểm yếu: tự tin thái quá, và một nỗi ám ảnh về gia đình khiến hắn dễ bị cảm xúc chi phối.

<short pause> Trước khi phân tích, cần biết luật của trận đấu. Quỷ trong thế giới này tái tạo cơ thể gần như ngay lập tức. Chém tay, tay mọc lại. Chém chân, chân mọc lại.

<short pause> Chỉ có hai cách giết quỷ: cho chúng tiếp xúc với ánh mặt trời, hoặc chém đứt đầu bằng kiếm Nhật Luân, loại kiếm rèn từ quặng hấp thụ ánh mặt trời.

<short pause> Trận này diễn ra giữa đêm, bình minh còn rất xa. Vậy Tanjiro chỉ có một mục tiêu duy nhất: cái cổ của Rui.

<short pause> Còn Rui thì chỉ cần giữ Tanjiro ở ngoài tầm kiếm. Một bên cần lao vào, một bên cần giữ khoảng cách. Toàn bộ trận đấu xoay quanh khoảng cách.

<short pause> Trước khi vào trận, cần hiểu vì sao cách thở lại quan trọng như vậy trong Kimetsu no Yaiba.

<short pause> Kiếm sĩ diệt quỷ được luyện một kỹ thuật thở đặc biệt, giúp đưa thật nhiều không khí vào cơ thể, tăng sức mạnh, tốc độ và sức bền lên vượt mức người thường.

<short pause> Mỗi trường phái hơi thở có phong cách riêng. Hơi thở của Nước uyển chuyển, thích hợp để phản ứng và thay đổi hướng. Kaku đã vẽ cây phả hệ các kiểu hơi thở ở video số năm.

<short pause> Nhưng hơi thở cũng là giới hạn. Khi phổi và cơ thể kiệt sức, mọi thế kiếm đều yếu đi. Nên trong trận này, sức bền cũng là một chiến trường.

<short pause> Hãy nhớ điều này, vì bước ngoặt của trận đấu đến chính từ việc Tanjiro thay đổi cách thở.
```

**ElevenLabs**

```text
Hồ sơ bên thứ nhất: Tanjiro. Cấp bậc: thấp nhất trong Sát Quỷ Đoàn, vừa mới vào nghề. Vũ khí: kiếm Nhật Luân. Kỹ thuật: Hơi thở của Nước.

[pause] Điểm mạnh: khứu giác cực nhạy, có thể ngửi thấy khe hở trong phòng thủ của đối thủ. Tinh thần không bao giờ bỏ cuộc. Và một em gái có năng lực của quỷ đứng về phía mình.

[pause] Điểm yếu: kinh nghiệm ít, thân thể đã bị thương từ các trận trước, và thanh kiếm chưa đủ sắc để chém vật cứng.

[pause] Hồ sơ bên thứ hai: Rui. Cấp bậc: Hạ Huyền Ngũ, thứ năm trong sáu con quỷ Hạ Huyền. Năng lực: điều khiển những sợi tơ còn cứng hơn thép.

[pause] Điểm mạnh: tấn công từ xa, bẫy khắp khu rừng, và có thể làm tơ cứng hơn nữa bằng cách truyền máu vào, khiến tơ chuyển màu đỏ.

[pause] Điểm yếu: tự tin thái quá, và một nỗi ám ảnh về gia đình khiến hắn dễ bị cảm xúc chi phối.

[pause] Trước khi phân tích, cần biết luật của trận đấu. Quỷ trong thế giới này tái tạo cơ thể gần như ngay lập tức. Chém tay, tay mọc lại. Chém chân, chân mọc lại.

[pause] Chỉ có hai cách giết quỷ: cho chúng tiếp xúc với ánh mặt trời, hoặc chém đứt đầu bằng kiếm Nhật Luân, loại kiếm rèn từ quặng hấp thụ ánh mặt trời.

[pause] Trận này diễn ra giữa đêm, bình minh còn rất xa. Vậy Tanjiro chỉ có một mục tiêu duy nhất: cái cổ của Rui.

[pause] Còn Rui thì chỉ cần giữ Tanjiro ở ngoài tầm kiếm. Một bên cần lao vào, một bên cần giữ khoảng cách. Toàn bộ trận đấu xoay quanh khoảng cách.

[pause] Trước khi vào trận, cần hiểu vì sao cách thở lại quan trọng như vậy trong Kimetsu no Yaiba.

[pause] Kiếm sĩ diệt quỷ được luyện một kỹ thuật thở đặc biệt, giúp đưa thật nhiều không khí vào cơ thể, tăng sức mạnh, tốc độ và sức bền lên vượt mức người thường.

[pause] Mỗi trường phái hơi thở có phong cách riêng. Hơi thở của Nước uyển chuyển, thích hợp để phản ứng và thay đổi hướng. Kaku đã vẽ cây phả hệ các kiểu hơi thở ở video số năm.

[pause] Nhưng hơi thở cũng là giới hạn. Khi phổi và cơ thể kiệt sức, mọi thế kiếm đều yếu đi. Nên trong trận này, sức bền cũng là một chiến trường.

[pause] Hãy nhớ điều này, vì bước ngoặt của trận đấu đến chính từ việc Tanjiro thay đổi cách thở.
```

### c03 · Sơ đồ khoảng cách / Hiệp 1: thăm dò

Khoảng 112 giây · cảnh s26–s36 · 1461 ký tự

**Gemini**

```text
Kaku vẽ ba vòng tròn trên bảng chiến thuật. Vòng trong cùng là tầm kiếm của Tanjiro, chỉ khoảng một cánh tay cộng chiều dài lưỡi kiếm.

<short pause> Vòng giữa là tầm tơ của Rui: vài chục mét, bao trùm cả một khoảng rừng. Trong vòng này, tơ có thể tới từ bất kỳ hướng nào.

<short pause> Vòng ngoài cùng là khu rừng đã giăng bẫy sẵn, nơi Rui kiểm soát mọi lối đi. Tanjiro đang đứng ngay trong lãnh thổ của đối thủ.

<short pause> Để thắng, Tanjiro phải đi xuyên qua vòng hai, nơi mỗi bước chân có thể mất một cánh tay. Đây là bài toán của cả trận đấu.

<short pause> <laugh> Kaku ghi chú: trong võ thuật thật, người ta gọi đây là cuộc chiến giữa người đánh xa và người đánh gần. Người đánh gần luôn phải trả giá để vào được tầm.

<short pause> Hiệp một. Mục tiêu của Tanjiro: đánh giá sức mạnh của tơ và tìm đường tiếp cận. Mục tiêu của Rui: dạy cho kẻ xâm nhập biết vị trí của mình.

<short pause> Lựa chọn của Tanjiro: dùng các thế của Hơi thở của Nước, vốn uyển chuyển như dòng chảy, để né và cắt tơ trên đường lao tới.

<short pause> Kết quả: Tanjiro cắt được tơ thường. <short pause> Nhưng Rui không vội. Hắn đang quan sát, giống như một người chơi cờ nhường vài nước đầu.

<short pause> Cái giá: Tanjiro tiêu hao sức và để lộ gần hết các thế kiếm của mình. Rui thì chưa dùng tới sức mạnh thật.

<short pause> Kaku có một suy luận: giữa một khu rừng phủ kín tơ, khứu giác của Tanjiro khó cho cậu biết sợi nào sắp lao tới. Truyện không nói rõ điều này, nhưng nó giải thích vì sao cậu bị động ở hiệp đầu.

<short pause> Nhận xét của Kaku: hiệp này Rui thắng về thông tin. Hắn biết Tanjiro làm được gì, còn Tanjiro chưa biết hắn làm được gì.
```

**ElevenLabs**

```text
Kaku vẽ ba vòng tròn trên bảng chiến thuật. Vòng trong cùng là tầm kiếm của Tanjiro, chỉ khoảng một cánh tay cộng chiều dài lưỡi kiếm.

[pause] Vòng giữa là tầm tơ của Rui: vài chục mét, bao trùm cả một khoảng rừng. Trong vòng này, tơ có thể tới từ bất kỳ hướng nào.

[pause] Vòng ngoài cùng là khu rừng đã giăng bẫy sẵn, nơi Rui kiểm soát mọi lối đi. Tanjiro đang đứng ngay trong lãnh thổ của đối thủ.

[pause] Để thắng, Tanjiro phải đi xuyên qua vòng hai, nơi mỗi bước chân có thể mất một cánh tay. Đây là bài toán của cả trận đấu.

[pause] [chuckles] Kaku ghi chú: trong võ thuật thật, người ta gọi đây là cuộc chiến giữa người đánh xa và người đánh gần. Người đánh gần luôn phải trả giá để vào được tầm.

[pause] Hiệp một. Mục tiêu của Tanjiro: đánh giá sức mạnh của tơ và tìm đường tiếp cận. Mục tiêu của Rui: dạy cho kẻ xâm nhập biết vị trí của mình.

[pause] Lựa chọn của Tanjiro: dùng các thế của Hơi thở của Nước, vốn uyển chuyển như dòng chảy, để né và cắt tơ trên đường lao tới.

[pause] Kết quả: Tanjiro cắt được tơ thường. [pause] Nhưng Rui không vội. Hắn đang quan sát, giống như một người chơi cờ nhường vài nước đầu.

[pause] Cái giá: Tanjiro tiêu hao sức và để lộ gần hết các thế kiếm của mình. Rui thì chưa dùng tới sức mạnh thật.

[pause] Kaku có một suy luận: giữa một khu rừng phủ kín tơ, khứu giác của Tanjiro khó cho cậu biết sợi nào sắp lao tới. Truyện không nói rõ điều này, nhưng nó giải thích vì sao cậu bị động ở hiệp đầu.

[pause] Nhận xét của Kaku: hiệp này Rui thắng về thông tin. Hắn biết Tanjiro làm được gì, còn Tanjiro chưa biết hắn làm được gì.
```

### c04 · Hiệp 2: thanh kiếm gãy / Hiệp 3: đòn tâm lý

Khoảng 95 giây · cảnh s37–s46 · 1238 ký tự

**Gemini**

```text
Hiệp hai. Rui truyền máu vào tơ. Những sợi tơ chuyển sang màu đỏ, cứng hơn hẳn trước.

<short pause> Lựa chọn của Tanjiro: vẫn chém thẳng vào tơ để mở đường. Và rồi điều tồi tệ nhất với một kiếm sĩ xảy ra: thanh kiếm của cậu gãy.

<short pause> Về chiến thuật, đây là khoảnh khắc khủng hoảng. Người đánh gần mất vũ khí đánh gần. Mục tiêu duy nhất, cái cổ, giờ gần như không thể với tới.

<short pause> Cái giá: không chỉ là thanh kiếm. Tơ bắt đầu cắt vào người Tanjiro. Mỗi giây đứng yên là thêm một vết thương.

<short pause> <laugh> Nhận xét của Kaku: sai lầm ở đây là chém trực diện vào thứ mình chưa biết độ cứng. <short pause> Nhưng một kiếm sĩ mới vào nghề không có nhiều lựa chọn khác.

<short pause> Hiệp ba không diễn ra bằng kiếm. Rui chứng kiến Nezuko liều mình che chắn cho anh trai, và nảy ra một ý: hắn muốn cô bé làm em gái của hắn.

<short pause> Đây là chiến thuật tâm lý: chia rẽ hai người, lấy đi điểm tựa tinh thần lớn nhất của Tanjiro.

<short pause> Rui bắt Nezuko, treo cô bé lên bằng tơ, và bắt đầu rút máu của cô. Tanjiro phải chứng kiến tất cả mà không thể lại gần.

<short pause> Lựa chọn của Tanjiro: từ chối mọi thỏa hiệp. Cậu hét lên rằng mối liên kết của hai anh em không phải thứ có thể cướp đi bằng sợ hãi.

<short pause> Cái giá: Tanjiro nổi giận và lao vào, bất chấp nguy hiểm. Về chiến thuật, cơn giận đã giúp cậu tiến vào vòng hai, nhưng cũng khiến cậu mất bình tĩnh.
```

**ElevenLabs**

```text
Hiệp hai. Rui truyền máu vào tơ. Những sợi tơ chuyển sang màu đỏ, cứng hơn hẳn trước.

[pause] Lựa chọn của Tanjiro: vẫn chém thẳng vào tơ để mở đường. Và rồi điều tồi tệ nhất với một kiếm sĩ xảy ra: thanh kiếm của cậu gãy.

[pause] Về chiến thuật, đây là khoảnh khắc khủng hoảng. Người đánh gần mất vũ khí đánh gần. Mục tiêu duy nhất, cái cổ, giờ gần như không thể với tới.

[pause] Cái giá: không chỉ là thanh kiếm. Tơ bắt đầu cắt vào người Tanjiro. Mỗi giây đứng yên là thêm một vết thương.

[pause] [chuckles] Nhận xét của Kaku: sai lầm ở đây là chém trực diện vào thứ mình chưa biết độ cứng. [pause] Nhưng một kiếm sĩ mới vào nghề không có nhiều lựa chọn khác.

[pause] Hiệp ba không diễn ra bằng kiếm. Rui chứng kiến Nezuko liều mình che chắn cho anh trai, và nảy ra một ý: hắn muốn cô bé làm em gái của hắn.

[pause] Đây là chiến thuật tâm lý: chia rẽ hai người, lấy đi điểm tựa tinh thần lớn nhất của Tanjiro.

[pause] Rui bắt Nezuko, treo cô bé lên bằng tơ, và bắt đầu rút máu của cô. Tanjiro phải chứng kiến tất cả mà không thể lại gần.

[pause] Lựa chọn của Tanjiro: từ chối mọi thỏa hiệp. Cậu hét lên rằng mối liên kết của hai anh em không phải thứ có thể cướp đi bằng sợ hãi.

[pause] Cái giá: Tanjiro nổi giận và lao vào, bất chấp nguy hiểm. Về chiến thuật, cơn giận đã giúp cậu tiến vào vòng hai, nhưng cũng khiến cậu mất bình tĩnh.
```

### c05 · Hiệp 4: điệu múa của thần lửa / Hiệp 5: cú lừa

Khoảng 125 giây · cảnh s47–s58 · 1622 ký tự

**Gemini**

```text
Hiệp bốn là khoảnh khắc nổi tiếng nhất. Bị dồn vào đường cùng, sắp chết, Tanjiro nhớ lại hình ảnh người cha múa giữa trời tuyết.

<short pause> Đó là điệu múa thần lửa, được gia đình cậu múa mỗi dịp năm mới, suốt từ đêm tới sáng, để cầu nguyện với thần lửa. Người cha dù yếu ớt vẫn múa được trọn đêm, nhờ cách thở đúng.

<short pause> Lựa chọn của Tanjiro: bỏ Hơi thở của Nước, chuyển sang nhịp thở của điệu múa. Một nhịp thở mà cơ thể cậu chưa từng được huấn luyện để dùng trong chiến đấu.

<short pause> Cùng lúc đó, Nezuko trong cơn mê tỉnh dậy và dùng năng lực máu của mình. Máu của cô bốc cháy, đốt đứt những sợi tơ, và lan lên cả lưỡi kiếm gãy của anh trai.

<short pause> Đây là sự phối hợp hoàn hảo: nhịp thở mới cho Tanjiro sức mạnh, lửa của Nezuko cho lưỡi kiếm khả năng cắt tơ. Không ai trong hai người làm được một mình.

<short pause> Tanjiro vượt qua vòng tơ và chém trúng cổ của Rui. Trong anime, cảnh này được xem là một trong những khoảnh khắc đẹp nhất của cả bộ.

<short pause> Cái giá: cơ thể Tanjiro hoàn toàn kiệt quệ. Cậu dùng một nhịp thở mà cơ thể chưa quen, và phải trả bằng mọi sức lực còn lại.

<short pause> Nhưng khi Tanjiro ngã xuống, tưởng đã thắng, Rui vẫn đứng đó. Chuyện gì đã xảy ra?

<short pause> Hóa ra ngay trước khi lưỡi kiếm chạm tới, Rui đã tự cắt đầu mình bằng tơ. Đầu hắn rời ra do chính hắn, không phải do kiếm Nhật Luân, nên hắn không chết.

<short pause> Về chiến thuật, đây là một cú lừa thông minh. Tanjiro tưởng đã đạt mục tiêu, và buông lỏng đúng lúc nguy hiểm nhất.

<short pause> Cái giá của Rui: gần như không có. Hắn chỉ cần nối đầu lại. Còn Tanjiro giờ nằm bất động, không còn sức đứng dậy.

<short pause> <laugh> Nhận xét của Kaku: bài học lớn nhất của hiệp này là đừng bao giờ ăn mừng trước khi chắc chắn. Với quỷ, chưa thấy tan biến là chưa thắng.
```

**ElevenLabs**

```text
Hiệp bốn là khoảnh khắc nổi tiếng nhất. Bị dồn vào đường cùng, sắp chết, Tanjiro nhớ lại hình ảnh người cha múa giữa trời tuyết.

[pause] Đó là điệu múa thần lửa, được gia đình cậu múa mỗi dịp năm mới, suốt từ đêm tới sáng, để cầu nguyện với thần lửa. Người cha dù yếu ớt vẫn múa được trọn đêm, nhờ cách thở đúng.

[pause] Lựa chọn của Tanjiro: bỏ Hơi thở của Nước, chuyển sang nhịp thở của điệu múa. Một nhịp thở mà cơ thể cậu chưa từng được huấn luyện để dùng trong chiến đấu.

[pause] Cùng lúc đó, Nezuko trong cơn mê tỉnh dậy và dùng năng lực máu của mình. Máu của cô bốc cháy, đốt đứt những sợi tơ, và lan lên cả lưỡi kiếm gãy của anh trai.

[pause] Đây là sự phối hợp hoàn hảo: nhịp thở mới cho Tanjiro sức mạnh, lửa của Nezuko cho lưỡi kiếm khả năng cắt tơ. Không ai trong hai người làm được một mình.

[pause] Tanjiro vượt qua vòng tơ và chém trúng cổ của Rui. Trong anime, cảnh này được xem là một trong những khoảnh khắc đẹp nhất của cả bộ.

[pause] Cái giá: cơ thể Tanjiro hoàn toàn kiệt quệ. Cậu dùng một nhịp thở mà cơ thể chưa quen, và phải trả bằng mọi sức lực còn lại.

[pause] Nhưng khi Tanjiro ngã xuống, tưởng đã thắng, Rui vẫn đứng đó. [curious] Chuyện gì đã xảy ra?

[pause] Hóa ra ngay trước khi lưỡi kiếm chạm tới, Rui đã tự cắt đầu mình bằng tơ. Đầu hắn rời ra do chính hắn, không phải do kiếm Nhật Luân, nên hắn không chết.

[pause] Về chiến thuật, đây là một cú lừa thông minh. Tanjiro tưởng đã đạt mục tiêu, và buông lỏng đúng lúc nguy hiểm nhất.

[pause] Cái giá của Rui: gần như không có. Hắn chỉ cần nối đầu lại. Còn Tanjiro giờ nằm bất động, không còn sức đứng dậy.

[pause] [chuckles] Nhận xét của Kaku: bài học lớn nhất của hiệp này là đừng bao giờ ăn mừng trước khi chắc chắn. Với quỷ, chưa thấy tan biến là chưa thắng.
```

### c06 · Hiệp 6: người thứ ba / Những trận đấu song song

Khoảng 113 giây · cảnh s59–s68 · 1470 ký tự

**Gemini**

```text
Hiệp cuối. Rui chuẩn bị kết liễu Tanjiro bằng đòn tơ mạnh nhất của mình. Đúng lúc đó, một kiếm sĩ khác xuất hiện: một Trụ cột của Sát Quỷ Đoàn, người dùng Hơi thở của Nước.

<short pause> Anh dùng một thế kiếm do chính mình tạo ra, gọi là Lặng sóng. Trong phạm vi của thế kiếm này, mọi đòn tấn công đi vào đều bị vô hiệu hóa, như mặt nước phẳng lặng hoàn toàn.

<short pause> Đòn tơ mạnh nhất của Rui, thứ đã suýt giết Tanjiro, tan biến trước một người đứng yên. Rồi đầu của Rui rơi xuống, lần này là thật.

<short pause> Về chiến thuật, đây là minh họa khoảng cách giữa người mới vào nghề và một Trụ cột. Không phải vì kỹ thuật khác nhau, cả hai đều dùng Hơi thở của Nước, mà vì độ tinh luyện.

<short pause> <laugh> Nhận xét của Kaku: nhưng đừng nghĩ Tanjiro thua. Cậu đã làm được điều không ai ngờ: buộc một Hạ Huyền phải dùng tới cú lừa để sống sót.

<short pause> Trận của Tanjiro không diễn ra một mình. Trên cùng ngọn núi, cùng lúc, đồng đội của cậu cũng đang chiến đấu với những thành viên khác của gia đình quỷ nhện.

<short pause> Một đồng đội nhút nhát nhưng cực nhanh phải đối mặt với con quỷ có độc biến người thành nhện. Người kia, kiếm sĩ đội đầu lợn rừng, đối đầu với con quỷ cha to lớn.

<short pause> Về chiến thuật, việc bị chia cắt là điều tồi tệ. Ba người mới vào nghề, mỗi người một nơi, không ai hỗ trợ được ai.

<short pause> Đó là lý do Sát Quỷ Đoàn phải cử tới hai Trụ cột. Khi đối thủ là một Hạ Huyền, những kiếm sĩ cấp thấp chỉ có thể cầm cự chờ viện binh.

<short pause> Kaku ghi chú: bài học ở đây rất thực tế. Khi bước vào lãnh thổ của đối thủ, đừng tách nhóm nếu không có kế hoạch liên lạc.
```

**ElevenLabs**

```text
Hiệp cuối. Rui chuẩn bị kết liễu Tanjiro bằng đòn tơ mạnh nhất của mình. Đúng lúc đó, một kiếm sĩ khác xuất hiện: một Trụ cột của Sát Quỷ Đoàn, người dùng Hơi thở của Nước.

[pause] Anh dùng một thế kiếm do chính mình tạo ra, gọi là Lặng sóng. Trong phạm vi của thế kiếm này, mọi đòn tấn công đi vào đều bị vô hiệu hóa, như mặt nước phẳng lặng hoàn toàn.

[pause] Đòn tơ mạnh nhất của Rui, thứ đã suýt giết Tanjiro, tan biến trước một người đứng yên. Rồi đầu của Rui rơi xuống, lần này là thật.

[pause] Về chiến thuật, đây là minh họa khoảng cách giữa người mới vào nghề và một Trụ cột. Không phải vì kỹ thuật khác nhau, cả hai đều dùng Hơi thở của Nước, mà vì độ tinh luyện.

[pause] [chuckles] Nhận xét của Kaku: nhưng đừng nghĩ Tanjiro thua. Cậu đã làm được điều không ai ngờ: buộc một Hạ Huyền phải dùng tới cú lừa để sống sót.

[pause] Trận của Tanjiro không diễn ra một mình. Trên cùng ngọn núi, cùng lúc, đồng đội của cậu cũng đang chiến đấu với những thành viên khác của gia đình quỷ nhện.

[pause] Một đồng đội nhút nhát nhưng cực nhanh phải đối mặt với con quỷ có độc biến người thành nhện. Người kia, kiếm sĩ đội đầu lợn rừng, đối đầu với con quỷ cha to lớn.

[pause] Về chiến thuật, việc bị chia cắt là điều tồi tệ. Ba người mới vào nghề, mỗi người một nơi, không ai hỗ trợ được ai.

[pause] Đó là lý do Sát Quỷ Đoàn phải cử tới hai Trụ cột. Khi đối thủ là một Hạ Huyền, những kiếm sĩ cấp thấp chỉ có thể cầm cự chờ viện binh.

[pause] Kaku ghi chú: bài học ở đây rất thực tế. Khi bước vào lãnh thổ của đối thủ, đừng tách nhóm nếu không có kế hoạch liên lạc.
```

### c07 · Nếu… thì: ba kịch bản khác / Bài học chiến thuật

Khoảng 110 giây · cảnh s69–s79 · 1427 ký tự

**Gemini**

```text
Huấn luyện viên nào cũng thích hỏi nếu. <laugh> Đây là ba kịch bản khác của trận đấu, theo suy luận của Kaku.

<short pause> Nếu Tanjiro không chém thẳng vào tơ đỏ ở hiệp hai, thanh kiếm có thể không gãy. <short pause> Nhưng cậu cũng không biết được tơ cứng tới mức nào, và có thể thua theo cách khác.

<short pause> Nếu Nezuko không tỉnh dậy đúng lúc, lưỡi kiếm gãy của Tanjiro gần như chắc chắn không cắt nổi tơ đỏ. Trận đấu đã kết thúc sớm hơn nhiều.

<short pause> Nếu Trụ cột đến sớm hơn năm phút, Tanjiro có lẽ không bao giờ nhớ lại điệu múa của cha. Và câu chuyện sau này sẽ mất đi một trong những bước ngoặt quan trọng nhất.

<short pause> Và một kịch bản vui: nếu Tanjiro giả vờ đồng ý để Rui nhận Nezuko làm em, rồi bất ngờ tấn công? Kaku nghĩ Tanjiro không làm được. Cậu là người không biết nói dối, và truyện cũng cho thấy cậu nói dối rất tệ.

<short pause> Kaku ghi chú: đôi khi trận thua lại quan trọng hơn trận thắng, vì nó mở ra một cánh cửa mà trận thắng dễ dàng không bao giờ mở.

<short pause> Tổng kết lại, trận đấu này để lại năm bài học chiến thuật.

<short pause> Một: xác định mục tiêu duy nhất. Với quỷ, chỉ có cái cổ. Mọi động tác thừa đều là lãng phí sức lực.

<short pause> Hai: thu thập thông tin trước khi dồn sức. Hiệp một và hai cho thấy cái giá của việc tấn công khi chưa biết đối thủ mạnh tới đâu.

<short pause> Ba: phối hợp tạo ra thứ mà một người không làm được. Nhịp thở mới cộng với lửa của em gái mới đủ phá được lồng tơ.

<short pause> Bốn: đừng ăn mừng sớm. Năm: độ tinh luyện quan trọng hơn số lượng chiêu thức. Một thế kiếm hoàn hảo đánh bại mười thế kiếm vội vàng.
```

**ElevenLabs**

```text
Huấn luyện viên nào cũng thích hỏi nếu. [chuckles] Đây là ba kịch bản khác của trận đấu, theo suy luận của Kaku.

[pause] Nếu Tanjiro không chém thẳng vào tơ đỏ ở hiệp hai, thanh kiếm có thể không gãy. [pause] Nhưng cậu cũng không biết được tơ cứng tới mức nào, và có thể thua theo cách khác.

[pause] Nếu Nezuko không tỉnh dậy đúng lúc, lưỡi kiếm gãy của Tanjiro gần như chắc chắn không cắt nổi tơ đỏ. Trận đấu đã kết thúc sớm hơn nhiều.

[pause] Nếu Trụ cột đến sớm hơn năm phút, Tanjiro có lẽ không bao giờ nhớ lại điệu múa của cha. Và câu chuyện sau này sẽ mất đi một trong những bước ngoặt quan trọng nhất.

[pause] [curious] Và một kịch bản vui: nếu Tanjiro giả vờ đồng ý để Rui nhận Nezuko làm em, rồi bất ngờ tấn công? Kaku nghĩ Tanjiro không làm được. Cậu là người không biết nói dối, và truyện cũng cho thấy cậu nói dối rất tệ.

[pause] Kaku ghi chú: đôi khi trận thua lại quan trọng hơn trận thắng, vì nó mở ra một cánh cửa mà trận thắng dễ dàng không bao giờ mở.

[pause] Tổng kết lại, trận đấu này để lại năm bài học chiến thuật.

[pause] Một: xác định mục tiêu duy nhất. Với quỷ, chỉ có cái cổ. Mọi động tác thừa đều là lãng phí sức lực.

[pause] Hai: thu thập thông tin trước khi dồn sức. Hiệp một và hai cho thấy cái giá của việc tấn công khi chưa biết đối thủ mạnh tới đâu.

[pause] Ba: phối hợp tạo ra thứ mà một người không làm được. Nhịp thở mới cộng với lửa của em gái mới đủ phá được lồng tơ.

[pause] Bốn: đừng ăn mừng sớm. Năm: độ tinh luyện quan trọng hơn số lượng chiêu thức. Một thế kiếm hoàn hảo đánh bại mười thế kiếm vội vàng.
```

### c08 · Góc nhìn của Kaku: gia đình giả và sợi dây thật / Kết

Khoảng 101 giây · cảnh s80–s89 · 1313 ký tự

**Gemini**

```text
<laugh> Bỏ bảng chiến thuật sang một bên, Kaku muốn nói về điều khiến trận đấu này đáng nhớ hơn mọi đường kiếm.

<short pause> Rui dùng tơ để trói buộc một gia đình giả. Mọi thành viên phải đóng đúng vai, ai sai thì bị trừng phạt. Hắn nghĩ sợi dây trói càng chặt thì gia đình càng bền.

<short pause> Tanjiro và Nezuko không có sợi dây nào nối với nhau. <short pause> Nhưng khi anh sắp chết, em gái tỉnh dậy. Khi em bị treo lên, anh không bỏ cuộc.

<short pause> Về sau, truyện cho thấy Rui từng là một đứa trẻ ốm yếu. Hắn đã hiểu sai về gia đình từ rất sớm, và trả giá bằng cả cuộc đời mình.

<short pause> Kaku nghĩ đó là lý do trận đấu này được nhớ lâu: nó không chỉ là cuộc chiến giữa kiếm và tơ, mà giữa hai cách hiểu về gia đình.

<short pause> Tóm lại: một kiếm sĩ cấp thấp nhất gặp một Hạ Huyền trong lãnh thổ của hắn. Mất kiếm, mất em gái, suýt mất mạng, nhưng nhờ điệu múa của cha và lửa của em, cậu chạm tới được cổ của đối thủ.

<short pause> Và dù người kết liễu Rui là một Trụ cột, trận đấu này là lúc Tanjiro thật sự trở thành một kiếm sĩ.

<short pause> Câu hỏi cho bạn: bạn muốn Kaku phân tích trận đấu nào tiếp theo bằng bảng chiến thuật? Viết tên trận vào phần bình luận nhé.

<short pause> Video tới, Kaku mở lại tập một của một bộ truyện khác, và chỉ cho bạn những chi tiết cài cắm mà tác giả đã giấu từ những trang đầu tiên: Attack on Titan.

<short pause> Đăng ký kênh nếu bạn thấy phân tích hữu ích. Huấn luyện viên Kaku thổi còi hết giờ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Bỏ bảng chiến thuật sang một bên, Kaku muốn nói về điều khiến trận đấu này đáng nhớ hơn mọi đường kiếm.

[pause] Rui dùng tơ để trói buộc một gia đình giả. Mọi thành viên phải đóng đúng vai, ai sai thì bị trừng phạt. Hắn nghĩ sợi dây trói càng chặt thì gia đình càng bền.

[pause] Tanjiro và Nezuko không có sợi dây nào nối với nhau. [pause] Nhưng khi anh sắp chết, em gái tỉnh dậy. Khi em bị treo lên, anh không bỏ cuộc.

[pause] Về sau, truyện cho thấy Rui từng là một đứa trẻ ốm yếu. Hắn đã hiểu sai về gia đình từ rất sớm, và trả giá bằng cả cuộc đời mình.

[pause] Kaku nghĩ đó là lý do trận đấu này được nhớ lâu: nó không chỉ là cuộc chiến giữa kiếm và tơ, mà giữa hai cách hiểu về gia đình.

[pause] Tóm lại: một kiếm sĩ cấp thấp nhất gặp một Hạ Huyền trong lãnh thổ của hắn. Mất kiếm, mất em gái, suýt mất mạng, nhưng nhờ điệu múa của cha và lửa của em, cậu chạm tới được cổ của đối thủ.

[pause] Và dù người kết liễu Rui là một Trụ cột, trận đấu này là lúc Tanjiro thật sự trở thành một kiếm sĩ.

[pause] [curious] Câu hỏi cho bạn: bạn muốn Kaku phân tích trận đấu nào tiếp theo bằng bảng chiến thuật? Viết tên trận vào phần bình luận nhé.

[pause] Video tới, Kaku mở lại tập một của một bộ truyện khác, và chỉ cho bạn những chi tiết cài cắm mà tác giả đã giấu từ những trang đầu tiên: Attack on Titan.

[pause] Đăng ký kênh nếu bạn thấy phân tích hữu ích. Huấn luyện viên Kaku thổi còi hết giờ đây, hẹn gặp lại!
```
