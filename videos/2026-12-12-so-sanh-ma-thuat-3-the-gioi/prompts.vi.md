# Bộ prompt · Frieren vs Black Clover vs Witch Hat Atelier: Hệ phép thuật nào hay nhất?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 92 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (92 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler nhẹ của Frieren tới kỳ thi pháp sư hạng nhất, Black Clover tới hết anime mùa một,…

```text
Wide 16:9 landscape cinematic frame. three different magic books lying side by side on a round wooden table under warm lamplight. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một ngọn nến chưa thắp đặt giữa bàn. Ba pháp sư từ ba thế giới khác nhau ngồi quanh nó. Nhiệm vụ rất đơn giản…

```text
Wide 16:9 landscape cinematic frame. an unlit candle in the center of a table, three shadowy mage silhouettes seated around it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Một người sẽ vẽ. Một người sẽ mở sách. Một người sẽ nhắm mắt tưởng tượng. Ba cách làm đó nói lên toàn bộ sự k…

```text
Wide 16:9 landscape cinematic frame. three hands: one holding a pen over paper, one opening a grimoire, one resting calmly with eyes closed. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay là video số ba mươi của kênh, và Kaku tổ chức một giải đấu nhỏ: năm vòng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot as a referee with a tiny whistle, a scoreboard with three columns behind it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Ba đấu thủ: ma thuật của Frieren, ma thuật của Black Clover, và ma thuật của Witch Hat Atelier. Cuối video có…

```text
Wide 16:9 landscape cinematic frame. three banners hanging in a small arena: one with a flower, one with a clover, one with a pointed hat. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Ba đấu thủ trong một phút

Lời: Trước khi thi, giới thiệu nhanh ba đấu thủ. Đấu thủ thứ nhất: Frieren. Phép thuật dựa trên ma lực và trí tưởn…

```text
Wide 16:9 landscape cinematic frame. a calm elf-like mage with a staff standing in a field of flowers, a spell forming from pure imagination. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Trong thế giới đó, phép thuật là một ngành nghiên cứu. Có những phép tấn công mạnh, và cũng có hàng nghìn phé…

```text
Wide 16:9 landscape cinematic frame. a library of old grimoires, some thick with battle spells, others thin with everyday charms. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Đấu thủ thứ hai: Black Clover. Gần như ai cũng có ma lực. Năm mười lăm tuổi, mỗi người nhận một cuốn grimoire…

```text
Wide 16:9 landscape cinematic frame. a teenager receiving a floating grimoire in a tall tower, elemental symbols circling around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Đấu thủ thứ ba: Witch Hat Atelier. Phép thuật được vẽ ra bằng một loại mực đặc biệt, theo hình tròn ba lớp: k…

```text
Wide 16:9 landscape cinematic frame. a glowing three-layer circle drawn in ink on a wooden floor, a pen and ink bottle beside it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một hệ dựa vào đầu óc, một hệ dựa vào cuốn sách, một hệ dựa vào ngòi bút. Giờ thì bắt đầu thi t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot blowing its whistle as three small banners flutter. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Luật chấm điểm của trọng tài · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi vào vòng một, trọng tài Kaku công bố luật chấm điểm, để không ai nói Kaku thiên vị.

```text
Wide 16:9 landscape cinematic frame. the owl mascot standing at a podium with a tiny gavel and a rulebook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Mỗi vòng là một thử thách cụ thể, chấm từ một tới mười điểm cho mỗi hệ. Năm vòng cộng lại, tối đa năm mươi đi…

```text
Wide 16:9 landscape cinematic frame. a scoreboard with five rows and a maximum of 50 written at the bottom. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Kaku chấm hệ thống phép thuật, không chấm nhân vật mạnh nhất. Một hệ có thể có nhân vật rất mạnh, nhưng luật…

```text
Wide 16:9 landscape cinematic frame. two scales: one weighing a powerful character, one weighing a rulebook, the second one highlighted. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và Kaku chỉ dùng những gì đã có trong phần truyện mà ba video riêng của kênh đã giới thiệu, để không spoiler…

```text
Wide 16:9 landscape cinematic frame. three small notebooks labeled with video numbers stacked beside the scoreboard. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Sức mạnh nằm ở đâu?

Lời: Có một khác biệt nền tảng giữa ba hệ mà Kaku muốn chỉ ra trước: sức mạnh nằm ở đâu?

```text
Wide 16:9 landscape cinematic frame. three glowing spheres labeled with icons: a person, a book, and an ink bottle. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Ở Frieren, sức mạnh nằm trong chính pháp sư: lượng ma lực tích lũy qua nhiều năm và khả năng tưởng tượng. Ngư…

```text
Wide 16:9 landscape cinematic frame. a calm mage with a faint aura that grows brighter as years pass behind her. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Ở Black Clover, sức mạnh nằm ở cả người lẫn cuốn sách: ma lực bẩm sinh quyết định nhiều thứ, và grimoire khuế…

```text
Wide 16:9 landscape cinematic frame. a noble with a bright aura and a commoner with a faint one, each holding a grimoire. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Còn ở Witch Hat Atelier, sức mạnh nằm phần lớn trong mực và hình vẽ. Người vẽ cần kỹ năng và kiến thức, nhưng…

```text
Wide 16:9 landscape cinematic frame. an ordinary hand drawing a powerful glowing circle with a simple pen. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: khác biệt này sẽ ảnh hưởng tới gần như mọi vòng thi phía sau. Hãy để ý nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling the ink bottle sphere on a chalkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Vòng 1: Thắp ngọn nến

Lời: Vòng một chấm hai điều: ai dùng được phép, và luật có rõ ràng không. Thử thách là thắp ngọn nến.

```text
Wide 16:9 landscape cinematic frame. the unlit candle in the center of the table, a small scorecard beside it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Pháp sư Witch Hat Atelier vẽ một ký hiệu lửa, thêm một dấu cường độ nhỏ, khép vòng tròn. Ngọn lửa nhỏ bùng lê…

```text
Wide 16:9 landscape cinematic frame. a small ink circle glowing under the candle as a neat little flame appears on the wick. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và ai học cách vẽ cũng làm được, kể cả một cô bé con nhà thợ may. Vấn đề duy nhất là kiến thức đó bị giữ bí m…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 9 under a pointed hat icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Pháp sư Frieren chọn một phép lửa mình đã học, hình dung ngọn lửa thật rõ, rồi thi triển. Ngọn nến sáng lên.…

```text
Wide 16:9 landscape cinematic frame. a calm mage pointing a staff at the candle, a soft flame appearing as if imagined into being. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Và muốn thành pháp sư thì phải học lâu năm, có thầy, có tài năng về ma lực. Kaku chấm bảy điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 7 under a flower icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Pháp sư Black Clover thì phụ thuộc vào may mắn. Nếu thuộc tính của bạn là lửa, bạn thắp ngọn nến trong một nố…

```text
Wide 16:9 landscape cinematic frame. a fire-attribute mage lighting the candle instantly while a water-attribute mage shrugs with a dripping hand. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Thật ra ở Black Clover, người không đúng thuộc tính vẫn có thể nhờ đồ vật phép hay nhờ đồng đội. Nhưng tự mìn…

```text
Wide 16:9 landscape cinematic frame. a mage handing a small glowing lantern to a friend who cannot make fire. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Luật thuộc tính rất rõ, nhưng có nhiều ngoại lệ và nhiều phép hiếm khó đoán. Kaku chấm sáu điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 6 under a clover icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Vòng 2: Học một phép mới

Lời: Vòng hai chấm khả năng sáng tạo: một pháp sư có thể học hoặc tạo ra phép mới dễ đến đâu?

```text
Wide 16:9 landscape cinematic frame. a blank page in a spellbook with a question mark drawn in the center. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Witch Hat Atelier gần như là hệ sáng tạo nhất Kaku từng thấy. Phép là sự kết hợp của ký hiệu và dấu. Chỉ cần…

```text
Wide 16:9 landscape cinematic frame. puzzle-like pieces of glowing symbols being rearranged into a brand-new circle. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nhân vật chính của bộ này còn dùng góc nhìn của người ngoài để nghĩ ra những cách vẽ mà phù thủy lâu năm khôn…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 10 under a pointed hat icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Frieren cũng rất mạnh ở vòng này. Phép thuật được nghiên cứu, phân tích và cải tiến qua nhiều thế hệ. Một phé…

```text
Wide 16:9 landscape cinematic frame. scholars analyzing a dark spell diagram, then the same diagram appearing in a textbook. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Và Frieren thì sưu tầm cả những phép nhỏ bé, như phép làm hoa nở hay phép lau sạch một bức tượng. Kaku chấm t…

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 under a flower icon, a small field of blooming flowers beside it. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Frieren còn có một chi tiết Kaku rất thích: phép thuật mà người đời cho là vô dụng hôm nay có thể trở thành c…

```text
Wide 16:9 landscape cinematic frame. a dusty spellbook with a small bookmark glowing on a page of a seemingly useless charm. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Black Clover thì phép mới thường tự xuất hiện trong grimoire khi người dùng trưởng thành, hoặc được khai phá…

```text
Wide 16:9 landscape cinematic frame. a grimoire page lighting up with a new spell as its owner stands up from defeat. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Kaku chấm bảy điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 7 under a clover icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Vòng 3: Cái giá

Lời: Vòng ba chấm cái giá: hệ thống nào khiến phép thuật có hậu quả rõ ràng nhất? Kaku cho điểm cao cho hệ nào có…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a glowing spell on one side and a dark shadow on the other. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Witch Hat Atelier có cái giá rất rõ: vẽ sai một nét là thảm họa. Người thường thấy cách vẽ phép thì bị xóa ký…

```text
Wide 16:9 landscape cinematic frame. a cracked crystal room and a figure with memories drifting away as light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Kaku chấm tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 under a pointed hat icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Frieren có cái giá kiểu khác: thời gian. Phép thuật mạnh cần hàng trăm năm luyện tập, và một pháp sư sống lâu…

```text
Wide 16:9 landscape cinematic frame. an ageless mage standing at a grave on a hill, seasons changing rapidly around her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Ngoài ra còn có những cái giá chiến thuật, như giấu ma lực suốt cả đời để đánh lừa kẻ thù. Kaku chấm tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 under a flower icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Và phép thuật mạnh tới đâu cũng không cứu được người đã mất. Truyện nhắc lại điều đó nhiều lần, rất nhẹ nhàng…

```text
Wide 16:9 landscape cinematic frame. a mage standing quietly beside a memorial stone with a small bouquet, wind in the grass. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Black Clover có cái giá chủ yếu là ma lực và thể lực. Phần đáng sợ nhất là những sức mạnh đến từ ác quỷ, luôn…

```text
Wide 16:9 landscape cinematic frame. a warrior with a black wing collapsing, then standing back up bandaged a few scenes later. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Kaku chấm bảy điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 7 under a clover icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Vòng 4: Trận chiến

Lời: Vòng bốn là vòng mà nhiều người chờ nhất: hệ nào tạo ra những trận đánh mãn nhãn nhất?

```text
Wide 16:9 landscape cinematic frame. a stormy arena with three glowing circles of light on the ground. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Black Clover thắng rõ ràng ở vòng này. Mỗi người một thuộc tính, mỗi hội hiệp sĩ một phong cách, và phản ma t…

```text
Wide 16:9 landscape cinematic frame. a spectacular clash of fire, water, wind and black anti-magic energy in a ruined city. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Kaku chấm mười điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 10 under a clover icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Frieren có những trận đánh ít phô trương hơn, nhưng rất thông minh: đọc ma lực đối thủ, giấu sức mạnh thật, v…

```text
Wide 16:9 landscape cinematic frame. a quiet mage standing calmly as a single precise beam of light ends a duel. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Kaku chấm tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 under a flower icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Trận đánh ở Frieren còn có một yếu tố riêng: đọc lượng ma lực của đối thủ để đánh giá sức mạnh. Và vì có ngườ…

```text
Wide 16:9 landscape cinematic frame. a mage squinting at an opponent's faint aura while a hidden immense power lurks beneath it. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Witch Hat Atelier thì không được làm ra để đánh nhau. Có những pha nguy hiểm và căng thẳng, nhưng phép thuật…

```text
Wide 16:9 landscape cinematic frame. an apprentice drawing a floating circle to rescue someone falling from a cliff. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Kaku chấm năm điểm. Không phải vì yếu, mà vì trận chiến không phải mục đích của nó.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 5 under a pointed hat icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Vòng 5: Ý nghĩa

Lời: Vòng cuối chấm điều Kaku coi trọng nhất: hệ thống phép thuật giúp câu chuyện nói được điều gì sâu sắc?

```text
Wide 16:9 landscape cinematic frame. a single glowing feather quill resting on an open book in soft light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Frieren dùng phép thuật để nói về thời gian và ký ức. Một pháp sư sống hàng nghìn năm học cách trân trọng nhữ…

```text
Wide 16:9 landscape cinematic frame. an ageless mage casting a small spell that makes a field of flowers bloom, a memory of old friends in the petals. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kaku chấm mười điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 10 under a flower icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Witch Hat Atelier dùng phép thuật để nói về kiến thức, quyền lực và đạo đức: ai được phép biết, và biết rồi t…

```text
Wide 16:9 landscape cinematic frame. a young apprentice holding a pen before a giant locked door of knowledge. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Kaku chấm chín điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 9 under a pointed hat icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Và phép thuật trong bộ này rất gần với nghệ thuật. Mỗi vòng tròn giống một bức tranh, và người vẽ đặt cả tâm…

```text
Wide 16:9 landscape cinematic frame. a gallery wall of framed glowing magic circles, each one unique like a painting. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Black Clover dùng phép thuật để nói về định kiến và nỗ lực: một thế giới xếp hạng con người theo ma lực, và m…

```text
Wide 16:9 landscape cinematic frame. a boy with no aura standing tall among glowing nobles, sword planted in the ground. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Kaku chấm tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scorecard showing 8 under a clover icon. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Thử thách phụ: dạy phép cho một đứa trẻ

Lời: Trước khi công bố kết quả, một thử thách phụ không tính điểm: nếu một đứa trẻ muốn học phép, nó sẽ đi con đườ…

```text
Wide 16:9 landscape cinematic frame. a curious child standing at a crossroads with three signposts. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Ở Witch Hat Atelier, đứa trẻ phải được một phù thủy nhận làm học trò và sống trong xưởng vẽ của thầy, học từn…

```text
Wide 16:9 landscape cinematic frame. a cozy atelier where a child copies circles from a teacher's sketchbook. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Ở Black Clover, đứa trẻ chờ tới năm mười lăm tuổi để nhận grimoire, rồi thi vào các hội hiệp sĩ ma pháp. Tài…

```text
Wide 16:9 landscape cinematic frame. a line of teenagers waiting outside a tall tower on grimoire day. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Ở Frieren, đứa trẻ cần một người thầy, và con đường có thể kéo dài hàng chục năm. Truyện cho thấy những sợi d…

```text
Wide 16:9 landscape cinematic frame. three silhouettes in a line across time, each teaching the next under the same tree. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cả ba thế giới đều đồng ý ở một điều: phép thuật không học một mình được. Luôn cần một người đi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding the hand of a smaller owl, walking along a path. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Kết quả chung cuộc

Lời: Giờ cộng điểm. Black Clover: sáu, bảy, bảy, mười, tám. Tổng cộng ba mươi tám điểm.

```text
Wide 16:9 landscape cinematic frame. a scoreboard filling in the clover column with a final total of 38. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Frieren: bảy, tám, tám, tám, mười. Tổng cộng bốn mươi mốt điểm.

```text
Wide 16:9 landscape cinematic frame. the flower column filling in with a total of 41. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Witch Hat Atelier: chín, mười, tám, năm, chín. Tổng cộng cũng là bốn mươi mốt điểm.

```text
Wide 16:9 landscape cinematic frame. the pointed hat column filling in with a total of 41, matching the flower column. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Hòa! Frieren và Witch Hat Atelier bằng điểm nhau ở vị trí số một. Và Kaku quyết định không phá thế hòa, vì tr…

```text
Wide 16:9 landscape cinematic frame. two banners side by side at the top of a podium, a blank tiebreaker card between them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: điểm số hoàn toàn là ý kiến của Kaku. Nếu bạn thích xem đánh nhau, Black Clover có thể là số một c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a sign saying opinion, with a small smile. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Giải thưởng phụ

Lời: Ngoài bảng tổng, Kaku trao vài giải thưởng phụ, giống lễ trao giải thật.

```text
Wide 16:9 landscape cinematic frame. three small trophies on a velvet cloth, each with a ribbon. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Giải hệ thống dễ đoán nhất: Witch Hat Atelier, vì bạn có thể tự vẽ ra kết quả trước khi phép được dùng.

```text
Wide 16:9 landscape cinematic frame. a trophy with a pointed hat engraving and a small circle diagram. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Giải trận đánh đã mắt nhất: Black Clover. Giải phép thuật khiến Kaku khóc nhiều nhất: phép làm hoa nở của Fri…

```text
Wide 16:9 landscape cinematic frame. two trophies: one with a clover engraving, one with a tiny flower bouquet tied to it. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và giải đặc biệt: hệ phép thuật Kaku muốn được sống trong đó nhất. Kaku chọn Witch Hat Atelier, vì Kaku thích…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a pen very carefully over a glowing circle, sweating. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Bạn hợp với thế giới nào?

Lời: Một trò vui nhỏ: dựa trên tính cách, bạn hợp với thế giới phép thuật nào nhất?

```text
Wide 16:9 landscape cinematic frame. three doors side by side, each with a small emblem: flower, clover, pointed hat. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nếu bạn kiên nhẫn, thích quan sát, thích những điều nhỏ bé và không vội vàng, thế giới của Frieren có lẽ là c…

```text
Wide 16:9 landscape cinematic frame. a quiet figure sitting in a meadow collecting small flowers into a book. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu bạn nhiều năng lượng, thích thử thách và càng bị coi thường càng muốn chứng minh bản thân, Black Clover đ…

```text
Wide 16:9 landscape cinematic frame. an energetic figure training at dawn, shouting with determination. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Nếu bạn thích vẽ, thích tự tay làm ra mọi thứ và luôn tò mò vì sao mọi thứ hoạt động, bạn sẽ hạnh phúc trong…

```text
Wide 16:9 landscape cinematic frame. a figure sketching intricate diagrams at a desk covered in ink bottles and notes. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Viết thế giới bạn chọn vào phần bình luận. Kaku sẽ đếm, và biết đâu đó chính là cách phá thế hòa.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tally board with three columns of marks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Nếu ba thế giới gặp nhau

Lời: Trước khi kết, một trò chơi tưởng tượng. Nhắc rõ: đây hoàn toàn là giả thuyết vui của Kaku, không có trong tr…

```text
Wide 16:9 landscape cinematic frame. three portals opening into one shared field, a THEORY stamp in the corner. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Nếu một vòng tròn phép của Witch Hat Atelier gặp phản ma thuật của Black Clover? Theo luật của phản ma thuật,…

```text
Wide 16:9 landscape cinematic frame. a black blade slicing through a glowing ink circle, the ink scattering like smoke. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Nếu một pháp sư của Frieren, người giấu ma lực suốt cả đời, gặp những hiệp sĩ Black Clover quen cảm nhận ma l…

```text
Wide 16:9 landscape cinematic frame. a mage with almost no visible aura standing calmly as confident knights approach, unaware. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Và nếu cô bé học trò của Witch Hat Atelier được đọc những cuốn sách phép kỳ lạ mà Frieren sưu tầm? Kaku nghĩ…

```text
Wide 16:9 landscape cinematic frame. a young apprentice surrounded by floating old grimoires, sketching excitedly. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Bạn nghĩ sao? Viết kịch bản gặp gỡ của bạn vào phần bình luận nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding three small portals like cards, grinning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Video số 30: Kaku nhìn lại · **Kaku** (đính kèm ảnh mẫu)

Lời: Đây là video thứ ba mươi của kênh. Kaku muốn dành một phút nhìn lại.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a stack of thirty small notebooks, looking back. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Ba mươi video, từ Nen trong Hunter x Hunter tới phép thuật hôm nay. Có video giải thích, có video xếp hạng, c…

```text
Wide 16:9 landscape cinematic frame. a long shelf of thirty notebooks, each with a different small symbol on its spine. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Điều Kaku học được nhiều nhất là thế này: một hệ thống sức mạnh hay không phải vì nó mạnh nhất, mà vì nó giúp…

```text
Wide 16:9 landscape cinematic frame. a single glowing thread connecting many small symbols into one picture of a human silhouette. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Cảm ơn bạn đã xem, bình luận và gợi ý chủ đề. Nhiều video trên kênh ra đời từ chính câu hỏi của người xem.

```text
Wide 16:9 landscape cinematic frame. a warm wall covered in comment cards and small thank-you notes. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Và cuốn sổ của Kaku vẫn còn rất nhiều trang trắng.

```text
Wide 16:9 landscape cinematic frame. a notebook open to a fresh blank page, a pen resting on it, morning light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Kết

Lời: Tóm lại: Frieren là phép thuật của tưởng tượng và thời gian. Black Clover là phép thuật của thuộc tính và nỗ…

```text
Wide 16:9 landscape cinematic frame. three magic books glowing side by side, each with a small symbol: flower, clover, pointed hat. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Kết quả: Frieren và Witch Hat Atelier hòa bốn mươi mốt điểm, Black Clover ba mươi tám điểm, nhưng đứng đầu ở…

```text
Wide 16:9 landscape cinematic frame. a final scoreboard with two tied columns and one slightly lower column with a battle trophy. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi quan trọng nhất: bạn sẽ phá thế hòa thế nào? Frieren hay Witch Hat Atelier? Hay bạn nghĩ Black Clover…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a ballot box and three small voting cards. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hãy đăng ký kênh để đi cùng Kaku tới những video tiếp theo. Kaku thổi tắt ngọn nến đây. Hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently blowing out the candle on the table, a thin trail of smoke rising. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Ba đấu thủ trong một phút

Khoảng 127 giây · cảnh s01–s10 · 1648 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler nhẹ của Frieren tới kỳ thi pháp sư hạng nhất, Black Clover tới hết anime mùa một, và Witch Hat Atelier ở mức nhập môn. Kaku đã có ba video riêng cho ba bộ này, số ba, số mười bốn và số mười hai.

<short pause> Một ngọn nến chưa thắp đặt giữa bàn. Ba pháp sư từ ba thế giới khác nhau ngồi quanh nó. Nhiệm vụ rất đơn giản: thắp ngọn nến bằng phép thuật.

<short pause> Một người sẽ vẽ. Một người sẽ mở sách. Một người sẽ nhắm mắt tưởng tượng. Ba cách làm đó nói lên toàn bộ sự khác nhau giữa ba hệ thống phép thuật.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay là video số ba mươi của kênh, và Kaku tổ chức một giải đấu nhỏ: năm vòng thử thách, mỗi vòng chấm từ một tới mười điểm.

<short pause> Ba đấu thủ: ma thuật của Frieren, ma thuật của Black Clover, và ma thuật của Witch Hat Atelier. Cuối video có kết quả, và có thể không như bạn đoán đâu.

<short pause> Trước khi thi, giới thiệu nhanh ba đấu thủ. Đấu thủ thứ nhất: Frieren. Phép thuật dựa trên ma lực và trí tưởng tượng. Muốn dùng một phép, pháp sư phải hình dung được nó thật rõ ràng.

<short pause> Trong thế giới đó, phép thuật là một ngành nghiên cứu. Có những phép tấn công mạnh, và cũng có hàng nghìn phép nhỏ bé cho đời sống thường ngày.

<short pause> Đấu thủ thứ hai: Black Clover. Gần như ai cũng có ma lực. Năm mười lăm tuổi, mỗi người nhận một cuốn grimoire, và mỗi người chỉ có một thuộc tính phép như lửa, nước hay gió.

<short pause> Đấu thủ thứ ba: Witch Hat Atelier. Phép thuật được vẽ ra bằng một loại mực đặc biệt, theo hình tròn ba lớp: ký hiệu trung tâm, các dấu điều khiển, và vòng tròn khép kín. Ai biết cách vẽ đều dùng được, nên nó bị giữ bí mật.

<short pause> Kaku ghi chú: một hệ dựa vào đầu óc, một hệ dựa vào cuốn sách, một hệ dựa vào ngòi bút. Giờ thì bắt đầu thi thôi!
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler nhẹ của Frieren tới kỳ thi pháp sư hạng nhất, Black Clover tới hết anime mùa một, và Witch Hat Atelier ở mức nhập môn. Kaku đã có ba video riêng cho ba bộ này, số ba, số mười bốn và số mười hai.

[pause] Một ngọn nến chưa thắp đặt giữa bàn. Ba pháp sư từ ba thế giới khác nhau ngồi quanh nó. Nhiệm vụ rất đơn giản: thắp ngọn nến bằng phép thuật.

[pause] Một người sẽ vẽ. Một người sẽ mở sách. Một người sẽ nhắm mắt tưởng tượng. Ba cách làm đó nói lên toàn bộ sự khác nhau giữa ba hệ thống phép thuật.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay là video số ba mươi của kênh, và Kaku tổ chức một giải đấu nhỏ: năm vòng thử thách, mỗi vòng chấm từ một tới mười điểm.

[pause] Ba đấu thủ: ma thuật của Frieren, ma thuật của Black Clover, và ma thuật của Witch Hat Atelier. Cuối video có kết quả, và có thể không như bạn đoán đâu.

[pause] Trước khi thi, giới thiệu nhanh ba đấu thủ. Đấu thủ thứ nhất: Frieren. Phép thuật dựa trên ma lực và trí tưởng tượng. Muốn dùng một phép, pháp sư phải hình dung được nó thật rõ ràng.

[pause] Trong thế giới đó, phép thuật là một ngành nghiên cứu. Có những phép tấn công mạnh, và cũng có hàng nghìn phép nhỏ bé cho đời sống thường ngày.

[pause] Đấu thủ thứ hai: Black Clover. Gần như ai cũng có ma lực. Năm mười lăm tuổi, mỗi người nhận một cuốn grimoire, và mỗi người chỉ có một thuộc tính phép như lửa, nước hay gió.

[pause] Đấu thủ thứ ba: Witch Hat Atelier. Phép thuật được vẽ ra bằng một loại mực đặc biệt, theo hình tròn ba lớp: ký hiệu trung tâm, các dấu điều khiển, và vòng tròn khép kín. Ai biết cách vẽ đều dùng được, nên nó bị giữ bí mật.

[pause] Kaku ghi chú: một hệ dựa vào đầu óc, một hệ dựa vào cuốn sách, một hệ dựa vào ngòi bút. Giờ thì bắt đầu thi thôi!
```

### c02 · Luật chấm điểm của trọng tài / Sức mạnh nằm ở đâu?

Khoảng 87 giây · cảnh s11–s19 · 1132 ký tự

**Gemini**

```text
<laugh> Trước khi vào vòng một, trọng tài Kaku công bố luật chấm điểm, để không ai nói Kaku thiên vị.

<short pause> Mỗi vòng là một thử thách cụ thể, chấm từ một tới mười điểm cho mỗi hệ. Năm vòng cộng lại, tối đa năm mươi điểm.

<short pause> Kaku chấm hệ thống phép thuật, không chấm nhân vật mạnh nhất. Một hệ có thể có nhân vật rất mạnh, nhưng luật lại lỏng lẻo, và ngược lại.

<short pause> Và Kaku chỉ dùng những gì đã có trong phần truyện mà ba video riêng của kênh đã giới thiệu, để không spoiler thêm.

<short pause> Có một khác biệt nền tảng giữa ba hệ mà Kaku muốn chỉ ra trước: sức mạnh nằm ở đâu?

<short pause> Ở Frieren, sức mạnh nằm trong chính pháp sư: lượng ma lực tích lũy qua nhiều năm và khả năng tưởng tượng. Người luyện càng lâu càng mạnh, và có thể giấu nó đi.

<short pause> Ở Black Clover, sức mạnh nằm ở cả người lẫn cuốn sách: ma lực bẩm sinh quyết định nhiều thứ, và grimoire khuếch đại nó. Quý tộc thường sinh ra đã có nhiều ma lực hơn.

<short pause> Còn ở Witch Hat Atelier, sức mạnh nằm phần lớn trong mực và hình vẽ. Người vẽ cần kỹ năng và kiến thức, nhưng không cần sinh ra đã mạnh. Đây là lý do nó nguy hiểm nếu lọt ra ngoài.

<short pause> Kaku ghi chú: khác biệt này sẽ ảnh hưởng tới gần như mọi vòng thi phía sau. Hãy để ý nhé.
```

**ElevenLabs**

```text
[chuckles] Trước khi vào vòng một, trọng tài Kaku công bố luật chấm điểm, để không ai nói Kaku thiên vị.

[pause] Mỗi vòng là một thử thách cụ thể, chấm từ một tới mười điểm cho mỗi hệ. Năm vòng cộng lại, tối đa năm mươi điểm.

[pause] Kaku chấm hệ thống phép thuật, không chấm nhân vật mạnh nhất. Một hệ có thể có nhân vật rất mạnh, nhưng luật lại lỏng lẻo, và ngược lại.

[pause] Và Kaku chỉ dùng những gì đã có trong phần truyện mà ba video riêng của kênh đã giới thiệu, để không spoiler thêm.

[pause] [curious] Có một khác biệt nền tảng giữa ba hệ mà Kaku muốn chỉ ra trước: sức mạnh nằm ở đâu?

[pause] Ở Frieren, sức mạnh nằm trong chính pháp sư: lượng ma lực tích lũy qua nhiều năm và khả năng tưởng tượng. Người luyện càng lâu càng mạnh, và có thể giấu nó đi.

[pause] Ở Black Clover, sức mạnh nằm ở cả người lẫn cuốn sách: ma lực bẩm sinh quyết định nhiều thứ, và grimoire khuếch đại nó. Quý tộc thường sinh ra đã có nhiều ma lực hơn.

[pause] Còn ở Witch Hat Atelier, sức mạnh nằm phần lớn trong mực và hình vẽ. Người vẽ cần kỹ năng và kiến thức, nhưng không cần sinh ra đã mạnh. Đây là lý do nó nguy hiểm nếu lọt ra ngoài.

[pause] Kaku ghi chú: khác biệt này sẽ ảnh hưởng tới gần như mọi vòng thi phía sau. Hãy để ý nhé.
```

### c03 · Vòng 1: Thắp ngọn nến

Khoảng 85 giây · cảnh s20–s27 · 1108 ký tự

**Gemini**

```text
Vòng một chấm hai điều: ai dùng được phép, và luật có rõ ràng không. Thử thách là thắp ngọn nến.

<short pause> Pháp sư Witch Hat Atelier vẽ một ký hiệu lửa, thêm một dấu cường độ nhỏ, khép vòng tròn. Ngọn lửa nhỏ bùng lên đúng như dự tính. Luật rõ tới mức bạn có thể đoán trước kết quả.

<short pause> Và ai học cách vẽ cũng làm được, kể cả một cô bé con nhà thợ may. Vấn đề duy nhất là kiến thức đó bị giữ bí mật. Kaku chấm chín điểm.

<short pause> Pháp sư Frieren chọn một phép lửa mình đã học, hình dung ngọn lửa thật rõ, rồi thi triển. Ngọn nến sáng lên. <short pause> Nhưng luật của hệ này mềm hơn: cùng một phép, người tưởng tượng giỏi hơn sẽ dùng tốt hơn.

<short pause> Và muốn thành pháp sư thì phải học lâu năm, có thầy, có tài năng về ma lực. Kaku chấm bảy điểm.

<short pause> Pháp sư Black Clover thì phụ thuộc vào may mắn. Nếu thuộc tính của bạn là lửa, bạn thắp ngọn nến trong một nốt nhạc. Nếu thuộc tính là nước hay gió, bạn sẽ phải đi mượn bật lửa.

<short pause> Thật ra ở Black Clover, người không đúng thuộc tính vẫn có thể nhờ đồ vật phép hay nhờ đồng đội. <short pause> Nhưng tự mình làm thì gần như không được.

<short pause> Luật thuộc tính rất rõ, nhưng có nhiều ngoại lệ và nhiều phép hiếm khó đoán. Kaku chấm sáu điểm.
```

**ElevenLabs**

```text
Vòng một chấm hai điều: ai dùng được phép, và luật có rõ ràng không. Thử thách là thắp ngọn nến.

[pause] Pháp sư Witch Hat Atelier vẽ một ký hiệu lửa, thêm một dấu cường độ nhỏ, khép vòng tròn. Ngọn lửa nhỏ bùng lên đúng như dự tính. Luật rõ tới mức bạn có thể đoán trước kết quả.

[pause] Và ai học cách vẽ cũng làm được, kể cả một cô bé con nhà thợ may. Vấn đề duy nhất là kiến thức đó bị giữ bí mật. Kaku chấm chín điểm.

[pause] Pháp sư Frieren chọn một phép lửa mình đã học, hình dung ngọn lửa thật rõ, rồi thi triển. Ngọn nến sáng lên. [pause] Nhưng luật của hệ này mềm hơn: cùng một phép, người tưởng tượng giỏi hơn sẽ dùng tốt hơn.

[pause] Và muốn thành pháp sư thì phải học lâu năm, có thầy, có tài năng về ma lực. Kaku chấm bảy điểm.

[pause] Pháp sư Black Clover thì phụ thuộc vào may mắn. Nếu thuộc tính của bạn là lửa, bạn thắp ngọn nến trong một nốt nhạc. Nếu thuộc tính là nước hay gió, bạn sẽ phải đi mượn bật lửa.

[pause] Thật ra ở Black Clover, người không đúng thuộc tính vẫn có thể nhờ đồ vật phép hay nhờ đồng đội. [pause] Nhưng tự mình làm thì gần như không được.

[pause] Luật thuộc tính rất rõ, nhưng có nhiều ngoại lệ và nhiều phép hiếm khó đoán. Kaku chấm sáu điểm.
```

### c04 · Vòng 2: Học một phép mới

Khoảng 85 giây · cảnh s28–s35 · 1106 ký tự

**Gemini**

```text
Vòng hai chấm khả năng sáng tạo: một pháp sư có thể học hoặc tạo ra phép mới dễ đến đâu?

<short pause> Witch Hat Atelier gần như là hệ sáng tạo nhất Kaku từng thấy. Phép là sự kết hợp của ký hiệu và dấu. Chỉ cần sắp xếp lại, bạn có một phép hoàn toàn mới, như lắp ráp đồ chơi xếp hình.

<short pause> Nhân vật chính của bộ này còn dùng góc nhìn của người ngoài để nghĩ ra những cách vẽ mà phù thủy lâu năm không nghĩ tới. Kaku chấm mười điểm.

<short pause> Frieren cũng rất mạnh ở vòng này. Phép thuật được nghiên cứu, phân tích và cải tiến qua nhiều thế hệ. Một phép giết người đáng sợ của ma tộc, sau vài chục năm bị phân tích, đã thành phép tấn công phổ thông.

<short pause> Và Frieren thì sưu tầm cả những phép nhỏ bé, như phép làm hoa nở hay phép lau sạch một bức tượng. Kaku chấm tám điểm.

<short pause> Frieren còn có một chi tiết Kaku rất thích: phép thuật mà người đời cho là vô dụng hôm nay có thể trở thành chìa khóa ngày mai. Không có kiến thức nào hoàn toàn thừa.

<short pause> Black Clover thì phép mới thường tự xuất hiện trong grimoire khi người dùng trưởng thành, hoặc được khai phá trong những trận chiến sinh tử. Sáng tạo có, nhưng nằm trong khuôn thuộc tính.

<short pause> Kaku chấm bảy điểm.
```

**ElevenLabs**

```text
[curious] Vòng hai chấm khả năng sáng tạo: một pháp sư có thể học hoặc tạo ra phép mới dễ đến đâu?

[pause] Witch Hat Atelier gần như là hệ sáng tạo nhất Kaku từng thấy. Phép là sự kết hợp của ký hiệu và dấu. Chỉ cần sắp xếp lại, bạn có một phép hoàn toàn mới, như lắp ráp đồ chơi xếp hình.

[pause] Nhân vật chính của bộ này còn dùng góc nhìn của người ngoài để nghĩ ra những cách vẽ mà phù thủy lâu năm không nghĩ tới. Kaku chấm mười điểm.

[pause] Frieren cũng rất mạnh ở vòng này. Phép thuật được nghiên cứu, phân tích và cải tiến qua nhiều thế hệ. Một phép giết người đáng sợ của ma tộc, sau vài chục năm bị phân tích, đã thành phép tấn công phổ thông.

[pause] Và Frieren thì sưu tầm cả những phép nhỏ bé, như phép làm hoa nở hay phép lau sạch một bức tượng. Kaku chấm tám điểm.

[pause] Frieren còn có một chi tiết Kaku rất thích: phép thuật mà người đời cho là vô dụng hôm nay có thể trở thành chìa khóa ngày mai. Không có kiến thức nào hoàn toàn thừa.

[pause] Black Clover thì phép mới thường tự xuất hiện trong grimoire khi người dùng trưởng thành, hoặc được khai phá trong những trận chiến sinh tử. Sáng tạo có, nhưng nằm trong khuôn thuộc tính.

[pause] Kaku chấm bảy điểm.
```

### c05 · Vòng 3: Cái giá / Vòng 4: Trận chiến

Khoảng 142 giây · cảnh s36–s51 · 1848 ký tự

**Gemini**

```text
Vòng ba chấm cái giá: hệ thống nào khiến phép thuật có hậu quả rõ ràng nhất? Kaku cho điểm cao cho hệ nào có cái giá khiến câu chuyện căng thẳng hơn.

<short pause> Witch Hat Atelier có cái giá rất rõ: vẽ sai một nét là thảm họa. Người thường thấy cách vẽ phép thì bị xóa ký ức. Và phép cấm có thể gây ra những hậu quả không đảo ngược được.

<short pause> Kaku chấm tám điểm.

<short pause> Frieren có cái giá kiểu khác: thời gian. Phép thuật mạnh cần hàng trăm năm luyện tập, và một pháp sư sống lâu sẽ nhìn những người mình yêu thương già đi rồi mất.

<short pause> Ngoài ra còn có những cái giá chiến thuật, như giấu ma lực suốt cả đời để đánh lừa kẻ thù. Kaku chấm tám điểm.

<short pause> Và phép thuật mạnh tới đâu cũng không cứu được người đã mất. Truyện nhắc lại điều đó nhiều lần, rất nhẹ nhàng mà đau lòng.

<short pause> Black Clover có cái giá chủ yếu là ma lực và thể lực. Phần đáng sợ nhất là những sức mạnh đến từ ác quỷ, luôn có nguy cơ nuốt chửng người dùng. <short pause> Nhưng phần lớn thời gian, nhân vật hồi phục khá nhanh.

<short pause> Kaku chấm bảy điểm.

<short pause> Vòng bốn là vòng mà nhiều người chờ nhất: hệ nào tạo ra những trận đánh mãn nhãn nhất?

<short pause> Black Clover thắng rõ ràng ở vòng này. Mỗi người một thuộc tính, mỗi hội hiệp sĩ một phong cách, và phản ma thuật xóa phép giữa trận. Trận đánh luôn ồn ào, nhiều màu và dồn dập.

<short pause> Kaku chấm mười điểm.

<short pause> Frieren có những trận đánh ít phô trương hơn, nhưng rất thông minh: đọc ma lực đối thủ, giấu sức mạnh thật, và kết thúc chỉ bằng một đòn đúng lúc.

<short pause> Kaku chấm tám điểm.

<short pause> Trận đánh ở Frieren còn có một yếu tố riêng: đọc lượng ma lực của đối thủ để đánh giá sức mạnh. Và vì có người giấu ma lực, việc đánh giá sai có thể phải trả giá bằng mạng sống.

<short pause> Witch Hat Atelier thì không được làm ra để đánh nhau. Có những pha nguy hiểm và căng thẳng, nhưng phép thuật chủ yếu được dùng để cứu người, giải quyết vấn đề và tạo ra những điều đẹp đẽ.

<short pause> Kaku chấm năm điểm. Không phải vì yếu, mà vì trận chiến không phải mục đích của nó.
```

**ElevenLabs**

```text
[curious] Vòng ba chấm cái giá: hệ thống nào khiến phép thuật có hậu quả rõ ràng nhất? Kaku cho điểm cao cho hệ nào có cái giá khiến câu chuyện căng thẳng hơn.

[pause] Witch Hat Atelier có cái giá rất rõ: vẽ sai một nét là thảm họa. Người thường thấy cách vẽ phép thì bị xóa ký ức. Và phép cấm có thể gây ra những hậu quả không đảo ngược được.

[pause] Kaku chấm tám điểm.

[pause] Frieren có cái giá kiểu khác: thời gian. Phép thuật mạnh cần hàng trăm năm luyện tập, và một pháp sư sống lâu sẽ nhìn những người mình yêu thương già đi rồi mất.

[pause] Ngoài ra còn có những cái giá chiến thuật, như giấu ma lực suốt cả đời để đánh lừa kẻ thù. Kaku chấm tám điểm.

[pause] Và phép thuật mạnh tới đâu cũng không cứu được người đã mất. Truyện nhắc lại điều đó nhiều lần, rất nhẹ nhàng mà đau lòng.

[pause] Black Clover có cái giá chủ yếu là ma lực và thể lực. Phần đáng sợ nhất là những sức mạnh đến từ ác quỷ, luôn có nguy cơ nuốt chửng người dùng. [pause] Nhưng phần lớn thời gian, nhân vật hồi phục khá nhanh.

[pause] Kaku chấm bảy điểm.

[pause] Vòng bốn là vòng mà nhiều người chờ nhất: hệ nào tạo ra những trận đánh mãn nhãn nhất?

[pause] Black Clover thắng rõ ràng ở vòng này. Mỗi người một thuộc tính, mỗi hội hiệp sĩ một phong cách, và phản ma thuật xóa phép giữa trận. Trận đánh luôn ồn ào, nhiều màu và dồn dập.

[pause] Kaku chấm mười điểm.

[pause] Frieren có những trận đánh ít phô trương hơn, nhưng rất thông minh: đọc ma lực đối thủ, giấu sức mạnh thật, và kết thúc chỉ bằng một đòn đúng lúc.

[pause] Kaku chấm tám điểm.

[pause] Trận đánh ở Frieren còn có một yếu tố riêng: đọc lượng ma lực của đối thủ để đánh giá sức mạnh. Và vì có người giấu ma lực, việc đánh giá sai có thể phải trả giá bằng mạng sống.

[pause] Witch Hat Atelier thì không được làm ra để đánh nhau. Có những pha nguy hiểm và căng thẳng, nhưng phép thuật chủ yếu được dùng để cứu người, giải quyết vấn đề và tạo ra những điều đẹp đẽ.

[pause] Kaku chấm năm điểm. Không phải vì yếu, mà vì trận chiến không phải mục đích của nó.
```

### c06 · Vòng 5: Ý nghĩa / Thử thách phụ: dạy phép cho một đứa trẻ

Khoảng 119 giây · cảnh s52–s64 · 1553 ký tự

**Gemini**

```text
Vòng cuối chấm điều Kaku coi trọng nhất: hệ thống phép thuật giúp câu chuyện nói được điều gì sâu sắc?

<short pause> Frieren dùng phép thuật để nói về thời gian và ký ức. Một pháp sư sống hàng nghìn năm học cách trân trọng những khoảnh khắc ngắn ngủi với con người. Những phép vô dụng lại chứa những kỷ niệm quý nhất.

<short pause> Kaku chấm mười điểm.

<short pause> Witch Hat Atelier dùng phép thuật để nói về kiến thức, quyền lực và đạo đức: ai được phép biết, và biết rồi thì phải chịu trách nhiệm thế nào.

<short pause> Kaku chấm chín điểm.

<short pause> Và phép thuật trong bộ này rất gần với nghệ thuật. Mỗi vòng tròn giống một bức tranh, và người vẽ đặt cả tâm hồn mình vào đó.

<short pause> Black Clover dùng phép thuật để nói về định kiến và nỗ lực: một thế giới xếp hạng con người theo ma lực, và một cậu bé không có ma lực vẫn không bỏ cuộc.

<short pause> Kaku chấm tám điểm.

<short pause> Trước khi công bố kết quả, một thử thách phụ không tính điểm: nếu một đứa trẻ muốn học phép, nó sẽ đi con đường nào ở mỗi thế giới?

<short pause> Ở Witch Hat Atelier, đứa trẻ phải được một phù thủy nhận làm học trò và sống trong xưởng vẽ của thầy, học từng ký hiệu, từng nét vẽ, như học một nghề thủ công.

<short pause> Ở Black Clover, đứa trẻ chờ tới năm mười lăm tuổi để nhận grimoire, rồi thi vào các hội hiệp sĩ ma pháp. Tài năng bẩm sinh và cuốn sách nhận được quyết định rất nhiều.

<short pause> Ở Frieren, đứa trẻ cần một người thầy, và con đường có thể kéo dài hàng chục năm. Truyện cho thấy những sợi dây thầy trò nối qua nhiều thế hệ, từ thầy của Frieren tới Frieren, rồi tới học trò của cô.

<short pause> <laugh> Kaku ghi chú: cả ba thế giới đều đồng ý ở một điều: phép thuật không học một mình được. Luôn cần một người đi trước.
```

**ElevenLabs**

```text
[curious] Vòng cuối chấm điều Kaku coi trọng nhất: hệ thống phép thuật giúp câu chuyện nói được điều gì sâu sắc?

[pause] Frieren dùng phép thuật để nói về thời gian và ký ức. Một pháp sư sống hàng nghìn năm học cách trân trọng những khoảnh khắc ngắn ngủi với con người. Những phép vô dụng lại chứa những kỷ niệm quý nhất.

[pause] Kaku chấm mười điểm.

[pause] Witch Hat Atelier dùng phép thuật để nói về kiến thức, quyền lực và đạo đức: ai được phép biết, và biết rồi thì phải chịu trách nhiệm thế nào.

[pause] Kaku chấm chín điểm.

[pause] Và phép thuật trong bộ này rất gần với nghệ thuật. Mỗi vòng tròn giống một bức tranh, và người vẽ đặt cả tâm hồn mình vào đó.

[pause] Black Clover dùng phép thuật để nói về định kiến và nỗ lực: một thế giới xếp hạng con người theo ma lực, và một cậu bé không có ma lực vẫn không bỏ cuộc.

[pause] Kaku chấm tám điểm.

[pause] Trước khi công bố kết quả, một thử thách phụ không tính điểm: nếu một đứa trẻ muốn học phép, nó sẽ đi con đường nào ở mỗi thế giới?

[pause] Ở Witch Hat Atelier, đứa trẻ phải được một phù thủy nhận làm học trò và sống trong xưởng vẽ của thầy, học từng ký hiệu, từng nét vẽ, như học một nghề thủ công.

[pause] Ở Black Clover, đứa trẻ chờ tới năm mười lăm tuổi để nhận grimoire, rồi thi vào các hội hiệp sĩ ma pháp. Tài năng bẩm sinh và cuốn sách nhận được quyết định rất nhiều.

[pause] Ở Frieren, đứa trẻ cần một người thầy, và con đường có thể kéo dài hàng chục năm. Truyện cho thấy những sợi dây thầy trò nối qua nhiều thế hệ, từ thầy của Frieren tới Frieren, rồi tới học trò của cô.

[pause] [chuckles] Kaku ghi chú: cả ba thế giới đều đồng ý ở một điều: phép thuật không học một mình được. Luôn cần một người đi trước.
```

### c07 · Kết quả chung cuộc / Giải thưởng phụ / Bạn hợp với thế giới nào?

Khoảng 120 giây · cảnh s65–s78 · 1557 ký tự

**Gemini**

```text
Giờ cộng điểm. Black Clover: sáu, bảy, bảy, mười, tám. Tổng cộng ba mươi tám điểm.

<short pause> Frieren: bảy, tám, tám, tám, mười. Tổng cộng bốn mươi mốt điểm.

<short pause> Witch Hat Atelier: chín, mười, tám, năm, chín. Tổng cộng cũng là bốn mươi mốt điểm.

<short pause> Hòa! Frieren và Witch Hat Atelier bằng điểm nhau ở vị trí số một. Và Kaku quyết định không phá thế hòa, vì trận chung kết này cần một trọng tài công bằng hơn Kaku: chính là bạn.

<short pause> <laugh> Kaku nhắc: điểm số hoàn toàn là ý kiến của Kaku. Nếu bạn thích xem đánh nhau, Black Clover có thể là số một của bạn. Không có hệ thống nào sai cả.

<short pause> Ngoài bảng tổng, Kaku trao vài giải thưởng phụ, giống lễ trao giải thật.

<short pause> Giải hệ thống dễ đoán nhất: Witch Hat Atelier, vì bạn có thể tự vẽ ra kết quả trước khi phép được dùng.

<short pause> Giải trận đánh đã mắt nhất: Black Clover. Giải phép thuật khiến Kaku khóc nhiều nhất: phép làm hoa nở của Frieren.

<short pause> Và giải đặc biệt: hệ phép thuật Kaku muốn được sống trong đó nhất. Kaku chọn Witch Hat Atelier, vì Kaku thích vẽ. <short pause> Nhưng Kaku sẽ rất cẩn thận để không vẽ sai nét nào.

<short pause> Một trò vui nhỏ: dựa trên tính cách, bạn hợp với thế giới phép thuật nào nhất?

<short pause> Nếu bạn kiên nhẫn, thích quan sát, thích những điều nhỏ bé và không vội vàng, thế giới của Frieren có lẽ là của bạn.

<short pause> Nếu bạn nhiều năng lượng, thích thử thách và càng bị coi thường càng muốn chứng minh bản thân, Black Clover đang gọi bạn.

<short pause> Nếu bạn thích vẽ, thích tự tay làm ra mọi thứ và luôn tò mò vì sao mọi thứ hoạt động, bạn sẽ hạnh phúc trong xưởng vẽ của Witch Hat Atelier.

<short pause> Viết thế giới bạn chọn vào phần bình luận. Kaku sẽ đếm, và biết đâu đó chính là cách phá thế hòa.
```

**ElevenLabs**

```text
Giờ cộng điểm. Black Clover: sáu, bảy, bảy, mười, tám. Tổng cộng ba mươi tám điểm.

[pause] Frieren: bảy, tám, tám, tám, mười. Tổng cộng bốn mươi mốt điểm.

[pause] Witch Hat Atelier: chín, mười, tám, năm, chín. Tổng cộng cũng là bốn mươi mốt điểm.

[pause] Hòa! Frieren và Witch Hat Atelier bằng điểm nhau ở vị trí số một. Và Kaku quyết định không phá thế hòa, vì trận chung kết này cần một trọng tài công bằng hơn Kaku: chính là bạn.

[pause] [chuckles] Kaku nhắc: điểm số hoàn toàn là ý kiến của Kaku. Nếu bạn thích xem đánh nhau, Black Clover có thể là số một của bạn. Không có hệ thống nào sai cả.

[pause] Ngoài bảng tổng, Kaku trao vài giải thưởng phụ, giống lễ trao giải thật.

[pause] Giải hệ thống dễ đoán nhất: Witch Hat Atelier, vì bạn có thể tự vẽ ra kết quả trước khi phép được dùng.

[pause] Giải trận đánh đã mắt nhất: Black Clover. Giải phép thuật khiến Kaku khóc nhiều nhất: phép làm hoa nở của Frieren.

[pause] Và giải đặc biệt: hệ phép thuật Kaku muốn được sống trong đó nhất. Kaku chọn Witch Hat Atelier, vì Kaku thích vẽ. [pause] Nhưng Kaku sẽ rất cẩn thận để không vẽ sai nét nào.

[pause] [curious] Một trò vui nhỏ: dựa trên tính cách, bạn hợp với thế giới phép thuật nào nhất?

[pause] Nếu bạn kiên nhẫn, thích quan sát, thích những điều nhỏ bé và không vội vàng, thế giới của Frieren có lẽ là của bạn.

[pause] Nếu bạn nhiều năng lượng, thích thử thách và càng bị coi thường càng muốn chứng minh bản thân, Black Clover đang gọi bạn.

[pause] Nếu bạn thích vẽ, thích tự tay làm ra mọi thứ và luôn tò mò vì sao mọi thứ hoạt động, bạn sẽ hạnh phúc trong xưởng vẽ của Witch Hat Atelier.

[pause] Viết thế giới bạn chọn vào phần bình luận. Kaku sẽ đếm, và biết đâu đó chính là cách phá thế hòa.
```

### c08 · Nếu ba thế giới gặp nhau / Video số 30: Kaku nhìn lại / Kết

Khoảng 143 giây · cảnh s79–s92 · 1856 ký tự

**Gemini**

```text
Trước khi kết, một trò chơi tưởng tượng. Nhắc rõ: đây hoàn toàn là giả thuyết vui của Kaku, không có trong truyện nào cả.

<short pause> Nếu một vòng tròn phép của Witch Hat Atelier gặp phản ma thuật của Black Clover? Theo luật của phản ma thuật, vòng tròn đó có lẽ sẽ tan biến ngay khi bị chém. Kẻ vẽ phép sẽ phải vẽ ở nơi lưỡi kiếm không với tới.

<short pause> Nếu một pháp sư của Frieren, người giấu ma lực suốt cả đời, gặp những hiệp sĩ Black Clover quen cảm nhận ma lực đối thủ? Có lẽ họ sẽ đánh giá thấp cô, và đó sẽ là sai lầm cuối cùng của họ.

<short pause> Và nếu cô bé học trò của Witch Hat Atelier được đọc những cuốn sách phép kỳ lạ mà Frieren sưu tầm? Kaku nghĩ cô sẽ vẽ ra những phép mà chưa thế giới nào từng thấy.

<short pause> Bạn nghĩ sao? Viết kịch bản gặp gỡ của bạn vào phần bình luận nhé.

<short pause> Đây là video thứ ba mươi của kênh. <laugh> Kaku muốn dành một phút nhìn lại.

<short pause> Ba mươi video, từ Nen trong Hunter x Hunter tới phép thuật hôm nay. Có video giải thích, có video xếp hạng, có video điều tra, có video đưa bạn vào thế giới đó để tự lựa chọn.

<short pause> Điều Kaku học được nhiều nhất là thế này: một hệ thống sức mạnh hay không phải vì nó mạnh nhất, mà vì nó giúp câu chuyện nói được điều gì đó về con người.

<short pause> Cảm ơn bạn đã xem, bình luận và gợi ý chủ đề. Nhiều video trên kênh ra đời từ chính câu hỏi của người xem.

<short pause> Và cuốn sổ của Kaku vẫn còn rất nhiều trang trắng.

<short pause> Tóm lại: Frieren là phép thuật của tưởng tượng và thời gian. Black Clover là phép thuật của thuộc tính và nỗ lực. Witch Hat Atelier là phép thuật của ngòi bút và bí mật.

<short pause> Kết quả: Frieren và Witch Hat Atelier hòa bốn mươi mốt điểm, Black Clover ba mươi tám điểm, nhưng đứng đầu ở vòng trận chiến.

<short pause> Câu hỏi quan trọng nhất: bạn sẽ phá thế hòa thế nào? Frieren hay Witch Hat Atelier? Hay bạn nghĩ Black Clover mới là số một? Bình chọn trong phần bình luận nhé.

<short pause> Hãy đăng ký kênh để đi cùng Kaku tới những video tiếp theo. Kaku thổi tắt ngọn nến đây. Hẹn gặp lại!
```

**ElevenLabs**

```text
Trước khi kết, một trò chơi tưởng tượng. Nhắc rõ: đây hoàn toàn là giả thuyết vui của Kaku, không có trong truyện nào cả.

[pause] [curious] Nếu một vòng tròn phép của Witch Hat Atelier gặp phản ma thuật của Black Clover? Theo luật của phản ma thuật, vòng tròn đó có lẽ sẽ tan biến ngay khi bị chém. Kẻ vẽ phép sẽ phải vẽ ở nơi lưỡi kiếm không với tới.

[pause] Nếu một pháp sư của Frieren, người giấu ma lực suốt cả đời, gặp những hiệp sĩ Black Clover quen cảm nhận ma lực đối thủ? Có lẽ họ sẽ đánh giá thấp cô, và đó sẽ là sai lầm cuối cùng của họ.

[pause] Và nếu cô bé học trò của Witch Hat Atelier được đọc những cuốn sách phép kỳ lạ mà Frieren sưu tầm? Kaku nghĩ cô sẽ vẽ ra những phép mà chưa thế giới nào từng thấy.

[pause] Bạn nghĩ sao? Viết kịch bản gặp gỡ của bạn vào phần bình luận nhé.

[pause] Đây là video thứ ba mươi của kênh. [chuckles] Kaku muốn dành một phút nhìn lại.

[pause] Ba mươi video, từ Nen trong Hunter x Hunter tới phép thuật hôm nay. Có video giải thích, có video xếp hạng, có video điều tra, có video đưa bạn vào thế giới đó để tự lựa chọn.

[pause] Điều Kaku học được nhiều nhất là thế này: một hệ thống sức mạnh hay không phải vì nó mạnh nhất, mà vì nó giúp câu chuyện nói được điều gì đó về con người.

[pause] Cảm ơn bạn đã xem, bình luận và gợi ý chủ đề. Nhiều video trên kênh ra đời từ chính câu hỏi của người xem.

[pause] Và cuốn sổ của Kaku vẫn còn rất nhiều trang trắng.

[pause] Tóm lại: Frieren là phép thuật của tưởng tượng và thời gian. Black Clover là phép thuật của thuộc tính và nỗ lực. Witch Hat Atelier là phép thuật của ngòi bút và bí mật.

[pause] Kết quả: Frieren và Witch Hat Atelier hòa bốn mươi mốt điểm, Black Clover ba mươi tám điểm, nhưng đứng đầu ở vòng trận chiến.

[pause] Câu hỏi quan trọng nhất: bạn sẽ phá thế hòa thế nào? Frieren hay Witch Hat Atelier? Hay bạn nghĩ Black Clover mới là số một? Bình chọn trong phần bình luận nhé.

[pause] Hãy đăng ký kênh để đi cùng Kaku tới những video tiếp theo. Kaku thổi tắt ngọn nến đây. Hẹn gặp lại!
```
