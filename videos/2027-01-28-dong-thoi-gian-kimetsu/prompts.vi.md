# Bộ prompt · Kimetsu no Yaiba: Dòng thời gian 1.000 năm, từ Muzan tới Tanjiro

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 9 đoạn đọc, khoảng 15.7 phút giọng.
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

Lời: Cảnh báo spoiler: video này đi tới hết manga Kimetsu no Yaiba, kể cả trận cuối. Kaku sẽ báo trước khi vào vùn…

```text
Wide 16:9 landscape cinematic frame. a closed scroll tied with a red cord lying on a wooden table beside a warning card, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Khoảng một nghìn năm trước, ở kinh đô Nhật Bản thời Heian, có một chàng trai quý tộc mắc bệnh nặng. Thầy thuố…

```text
Wide 16:9 landscape cinematic frame. an ancient Japanese aristocratic residence at night with paper lanterns, a sickly young man lying on a futon behind a translucent screen, wide shot, dim warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Một vị thầy thuốc tận tâm thử cho cậu một loại thuốc mới. Và từ liều thuốc đó, con quỷ đầu tiên ra đời.

```text
Wide 16:9 landscape cinematic frame. a small ceramic medicine bowl with a faint blue glow on a lacquered tray, extreme close-up, eerie candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Một nghìn năm sau, một cậu bé bán than ở vùng núi trở về nhà, và thấy gia đình mình đã bị tấn công. Giữa hai…

```text
Wide 16:9 landscape cinematic frame. a small mountain cottage in snow at dawn with a lone set of footprints leading toward its open door, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Câu hỏi hôm nay: điều gì đã xảy ra trong một nghìn năm đó? Con quỷ đầu tiên đã làm gì, Đội diệt quỷ ra đời th…

```text
Wide 16:9 landscape cinematic frame. a long horizontal scroll partially unrolled showing ink marks spaced across the centuries, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku trải dài dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ đêm t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a long scroll across a table with both wings, looking excited. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Cách đọc dòng thời gian

Lời: Trước hết, một điều cần biết: Kimetsu no Yaiba hiếm khi cho con số năm chính xác. Mốc chắc chắn nhất là thời…

```text
Wide 16:9 landscape cinematic frame. a vintage Japanese calendar page from the early twentieth century pinned to a wall, close-up, warm sepia light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Những mốc khác được tính ngược từ đó: khoảng một nghìn năm trước là thời Heian, khoảng bốn trăm năm trước là…

```text
Wide 16:9 landscape cinematic frame. a ruler laid over a timeline scroll with two earlier points marked approximately, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Kaku sẽ đánh dấu mỗi mốc bằng ba mức. Chắc chắn: truyện nói rõ. Suy ra: tính từ các chi tiết. Lý thuyết: fan…

```text
Wide 16:9 landscape cinematic frame. three small colored stamps on parchment: a solid circle, a half circle, and a dotted circle, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và vì đây là dòng thời gian, Kaku sẽ nói nhiều về những người không xuất hiện trực tiếp trong phần lớn truyện…

```text
Wide 16:9 landscape cinematic frame. a row of faded silhouettes standing behind a young figure in the foreground, symbolic wide shot, soft mist. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Thời Heian, khoảng 1.000 năm trước: con quỷ đầu tiên

Lời: Chàng trai quý tộc đó chính là Kibutsuji Muzan. Vị thầy thuốc cho Muzan dùng một phương thuốc thử nghiệm, tro…

```text
Wide 16:9 landscape cinematic frame. a single blue spider lily flower glowing softly in a dark garden, extreme close-up, cool moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Thuốc dường như không có tác dụng ngay. Muzan nóng giận, cho rằng mình bị lừa, và giết chết vị thầy thuốc trư…

```text
Wide 16:9 landscape cinematic frame. an overturned medicine tray and scattered herbs on a wooden floor, a shadow retreating through a doorway, dramatic low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Rồi Muzan nhận ra: cậu không chết nữa. Cơ thể mạnh hơn, lành lại mọi vết thương. Nhưng cậu không thể bước ra…

```text
Wide 16:9 landscape cinematic frame. a pale hand reaching toward a sliver of sunlight on the floor and pulling back sharply, extreme close-up, harsh contrast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Vì thầy thuốc đã chết, công thức cũng mất theo. Muzan không biết làm sao để hoàn thiện phương thuốc và vượt q…

```text
Wide 16:9 landscape cinematic frame. a torn page of an old medical notebook with half its text missing, drifting in the wind, close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Từ đó, Muzan dành một nghìn năm để tìm hoa bỉ ngạn xanh. Và một nghìn năm không tìm thấy. Cuối video, Kaku sẽ…

```text
Wide 16:9 landscape cinematic frame. a figure in shadow walking through endless fields of red spider lilies searching, wide shot, eerie dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Để tìm hoa và tìm cách vượt mặt trời, Muzan bắt đầu tạo ra những con quỷ khác bằng cách truyền máu của mình.…

```text
Wide 16:9 landscape cinematic frame. a single drop of dark liquid falling into a shallow bowl and spreading into branching veins, extreme close-up, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Máu càng nhiều thì quỷ càng mạnh, nhưng cũng càng bị Muzan kiểm soát chặt. Muzan có thể nghe, thấy qua quỷ củ…

```text
Wide 16:9 landscape cinematic frame. a spider web of thin red threads connecting many small shadowy figures to a central dark point, abstract diagram, ominous light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: mọi bi kịch trong truyện đều bắt đầu từ một khoảnh khắc thiếu kiên nhẫn. Nếu Muzan chờ thêm một ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at an hourglass with a worried expression, one wing on its forehead. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Gia tộc bị nguyền rủa

Lời: Muzan có họ hàng. Gia tộc Ubuyashiki cùng dòng máu với cậu. Và theo truyện, vì dòng máu này sinh ra con quỷ đ…

```text
Wide 16:9 landscape cinematic frame. an old family tree painted on a folding screen with one branch burned black, close-up, somber candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Những người con trai trong gia tộc sinh ra đã yếu ớt, và thường không sống được lâu. Một vị thầy tu nói với h…

```text
Wide 16:9 landscape cinematic frame. an elderly priest speaking to a kneeling family inside a temple hall, incense smoke rising, medium shot, dim golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kaku ghi mức suy ra: truyện không nói năm chính xác Đội diệt quỷ thành lập, nhưng cho thấy gia tộc Ubuyashiki…

```text
Wide 16:9 landscape cinematic frame. a row of ancestral memorial tablets on a shelf, each slightly different in age, close-up, soft candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Những kiếm sĩ đầu tiên chưa có hơi thở. Họ chỉ có lòng can đảm và những thanh kiếm đặc biệt, rèn từ quặng hấp…

```text
Wide 16:9 landscape cinematic frame. a blacksmith forging a blade from glowing ore in a mountain forge, sparks flying, medium shot, fiery light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Kiếm Nhật Luân và ánh mặt trời là hai thứ duy nhất có thể giết quỷ bằng cách chém đầu hoặc thiêu đốt. Trong n…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman standing at the edge of a dark forest at night, holding a faintly glowing blade, back view, cold moonlight. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Hình ảnh lời nguyền của gia tộc này rất quan trọng. Nó biến cuộc chiến diệt quỷ thành một món nợ gia đình kéo…

```text
Wide 16:9 landscape cinematic frame. a heavy iron chain stretching across a long scroll of centuries, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Thời Chiến Quốc, khoảng 400 năm trước: người mang mặt trời

Lời: Nhảy tới khoảng bốn trăm năm trước, thời Chiến Quốc. Một cậu bé tên Tsugikuni Yoriichi ra đời, với một dấu vế…

```text
Wide 16:9 landscape cinematic frame. a quiet samurai-era village at dawn with a small child standing alone in a field, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Yoriichi có một người anh song sinh, Michikatsu. Người anh luôn sống trong cái bóng của em, và nỗi ghen tị đó…

```text
Wide 16:9 landscape cinematic frame. two small shadows cast side by side on a wall, one noticeably longer, symbolic close-up, late afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Yoriichi là người đầu tiên dùng Hơi thở, cụ thể là Hơi thở Mặt Trời. Anh dạy lại cho các kiếm sĩ, và từ đó si…

```text
Wide 16:9 landscape cinematic frame. a glowing sun symbol at the center of a parchment diagram with five branches spreading outward, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Cũng thời đó, nhiều kiếm sĩ đánh thức được một dấu ấn trên cơ thể, giúp họ mạnh vượt bậc. Nhưng cái giá rất n…

```text
Wide 16:9 landscape cinematic frame. a candle burning very brightly and melting quickly on a stand, extreme close-up, intense warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Và rồi Yoriichi gặp Muzan. Đây là lần duy nhất trong một nghìn năm, Muzan cảm thấy sợ hãi thật sự.

```text
Wide 16:9 landscape cinematic frame. a lone swordsman standing calmly under a full moon facing a tall shadowy figure across a field, wide shot, cold silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Yoriichi gần như giết được Muzan. Để sống sót, Muzan phải tự nổ tung thành khoảng một nghìn tám trăm mảnh và…

```text
Wide 16:9 landscape cinematic frame. an explosion of dark fragments scattering into the night sky like a flock of shadows, wide shot, dramatic moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Trong đêm đó, một con quỷ nữ tên Tamayo, người vốn phục vụ Muzan, được giải thoát khỏi sự kiểm soát. Yoriichi…

```text
Wide 16:9 landscape cinematic frame. a woman kneeling in a moonlit field with tears in her eyes, a broken red thread falling from her wrist, medium shot, soft silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nhưng thất bại đó có giá. Muzan trốn thoát, và người anh Michikatsu lại trở thành quỷ. Yoriichi bị trục xuất…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman walking away down a long mountain road, his back to the viewer, wide shot, melancholy dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Michikatsu trở thành Kokushibo, một trong những con quỷ mạnh nhất. Hai anh em song sinh, một người là mặt trờ…

```text
Wide 16:9 landscape cinematic frame. a sun and a crescent moon painted side by side on a torn paper screen, the tear running between them, close-up, split warm and cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Ngọn lửa âm thầm: gia đình bán than

Lời: Trước khi rời đi, Yoriichi gặp một gia đình bán than họ Kamado. Anh kể cho họ nghe câu chuyện của mình, và ch…

```text
Wide 16:9 landscape cinematic frame. a humble charcoal-burner's hut in a snowy mountain forest with warm light spilling from the door, wide shot, cozy winter light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Gia đình Kamado không phải kiếm sĩ. Nhưng họ biến những động tác đó thành một điệu múa cầu thần, gọi là Hinok…

```text
Wide 16:9 landscape cinematic frame. a dancer holding a flaming torch performing in the snow at night, trails of fire drawn in the air, wide shot, warm firelight against cold night. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Họ cũng giữ một món đồ Yoriichi để lại, và truyền qua nhiều thế hệ. Họ không biết mình đang giữ gì. Họ chỉ hứ…

```text
Wide 16:9 landscape cinematic frame. a small wooden keepsake box being handed from an old pair of hands to a young pair of hands, extreme close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là chi tiết đẹp nhất trong cả dòng thời gian. Kiếm thuật mạnh nhất lịch sử không nằm trong võ đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting by a warm hearth holding a tiny torch, looking touched. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Sau Yoriichi, Muzan truy lùng những người dùng Hơi thở Mặt Trời. Kiếm thuật này gần như biến mất khỏi Đội diệ…

```text
Wide 16:9 landscape cinematic frame. a burned scroll with sun symbols lying in ashes, while far away on a mountain a tiny flame still burns, split composition, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Những thế kỷ tích lũy

Lời: Từ thời Chiến Quốc tới thời Đại Chính là khoảng ba, bốn trăm năm. Truyện kể rất ít về giai đoạn này, nên Kaku…

```text
Wide 16:9 landscape cinematic frame. a mostly blank section of a long timeline scroll with only a few faint ink marks, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Muzan lập ra nhóm Thập Nhị Quỷ Nguyệt, mười hai con quỷ mạnh nhất, chia làm sáu Thượng Huyền và sáu Hạ Huyền.

```text
Wide 16:9 landscape cinematic frame. twelve small eerie paper lanterns arranged in two rows of six in a dark hall, wide shot, ominous red glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Các Hạ Huyền thay đổi liên tục. Nhưng sáu Thượng Huyền thì giữ nguyên suốt khoảng một trăm mười ba năm. Không…

```text
Wide 16:9 landscape cinematic frame. six tall stone pillars standing unbroken in mist, with many small fallen stones around their base, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Tamayo thì dùng những thế kỷ đó để nghiên cứu y học. Bà tự thay đổi cơ thể để thoát hẳn khỏi Muzan, và cần rấ…

```text
Wide 16:9 landscape cinematic frame. a quiet hidden study filled with bottles, dried herbs and handwritten notes, a single lamp burning, wide shot, warm scholarly light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và Muzan học cách ẩn mình. Hắn sống giữa con người, đổi tên, đổi vẻ ngoài, thậm chí có cả một gia đình giả để…

```text
Wide 16:9 landscape cinematic frame. a crowded early twentieth century street with a single figure blending into the crowd, face hidden by shadow, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kaku để ý: trong suốt những thế kỷ này, quỷ có thời gian, còn con người thì có sự kế thừa. Quỷ sống lâu hơn,…

```text
Wide 16:9 landscape cinematic frame. a single ancient tree standing alone beside a row of young saplings growing in a line, wide shot, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Thời Đại Chính: Tanjiro

Lời: Thời Đại Chính. Kamado Tanjiro, con trai cả của gia đình bán than, đi xuống thị trấn bán than. Khi trở về, cả…

```text
Wide 16:9 landscape cinematic frame. a young boy carrying a basket of charcoal on his back walking up a snowy mountain path, wide shot, cold morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Kiếm sĩ Tomioka Giyu gặp hai anh em, nhận ra Nezuko khác những con quỷ khác, và gửi Tanjiro tới thầy Urokodak…

```text
Wide 16:9 landscape cinematic frame. a calm swordsman standing in the snow looking down at a kneeling boy shielding someone behind him, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Sau khoảng hai năm luyện tập, Tanjiro vượt qua Kỳ tuyển chọn cuối cùng và gia nhập Đội diệt quỷ. Cậu bắt đầu…

```text
Wide 16:9 landscape cinematic frame. a boy splitting a huge boulder with a single sword strike in a misty forest clearing, dramatic medium shot, soft grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ở Asakusa, Tanjiro lần đầu thấy Muzan, đang sống như một người đàn ông bình thường giữa phố. Cũng tại đây, cậ…

```text
Wide 16:9 landscape cinematic frame. a bustling early twentieth century city street at night with electric lights and a crowd, wide shot, warm bustling light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Rồi tới núi Natagumo, nơi Tanjiro lần đầu dùng điệu múa của cha thành kiếm thuật. Trận với Rui là nơi Hinokam…

```text
Wide 16:9 landscape cinematic frame. a burst of fire trails in the shape of a spiral drawn across a dark forest at night, wide shot, warm firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Chuyến tàu Vô Tận, nơi Viêm Trụ Rengoku chiến đấu với Thượng Huyền Tam và hy sinh khi trời sắp sáng.

```text
Wide 16:9 landscape cinematic frame. a steam train stopped on a track at dawn, smoke drifting across a field, wide shot, bittersweet early light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Phố Đèn Đỏ: Âm Trụ Uzui cùng Tanjiro và các bạn hạ được Thượng Huyền Lục. Đây là lần đầu tiên sau một trăm mư…

```text
Wide 16:9 landscape cinematic frame. one of six tall stone pillars cracking and crumbling while the others remain, wide shot, dramatic dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Làng Thợ Rèn: Nezuko vượt qua được ánh mặt trời. Muzan lập tức đổi mục tiêu: không cần tìm hoa nữa, hắn chỉ c…

```text
Wide 16:9 landscape cinematic frame. a small silhouette standing in bright sunlight on a hillside at dawn, arms spread, wide shot, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Tính từ đêm Heian tới đây là khoảng một nghìn năm. Lần đầu tiên, Muzan có trong tầm tay thứ hắn tìm kiếm. Và…

```text
Wide 16:9 landscape cinematic frame. the long timeline scroll almost fully unrolled with a bright mark near the end, parchment close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Vùng spoiler cuối truyện

Lời: Từ đây là spoiler phần cuối manga, chưa có trong anime truyền hình. Nếu bạn muốn chờ phim, hãy tua tới chương…

```text
Wide 16:9 landscape cinematic frame. a red warning sign painted on a wooden gate across a mountain path, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Sau Làng Thợ Rèn, các Trụ cột mở một đợt huấn luyện chung để nhiều kiếm sĩ đánh thức dấu ấn. Họ biết mình đan…

```text
Wide 16:9 landscape cinematic frame. a group of swordsmen training together in a mountain clearing at sunrise, wide shot, determined warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Thủ lĩnh Ubuyashiki Kagaya, người mang lời nguyền của gia tộc, đón Muzan tới nhà mình. Ông chấp nhận hy sinh…

```text
Wide 16:9 landscape cinematic frame. a traditional Japanese mansion at night with a single lantern at the gate, calm and still, wide shot, somber blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Muzan kéo toàn bộ Đội diệt quỷ vào Vô Hạn Thành, một pháo đài mê cung của quỷ. Anime đang chuyển thể phần này…

```text
Wide 16:9 landscape cinematic frame. an impossible maze of floating wooden corridors and staircases twisting in every direction, surreal wide shot, eerie amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Trong Vô Hạn Thành, Kokushibo đối mặt với những kiếm sĩ mang hơi thở. Bốn trăm năm sau, người anh song sinh v…

```text
Wide 16:9 landscape cinematic frame. a lone crescent moon reflected in a still pool inside a vast dark hall, wide shot, cold silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Trận cuối diễn ra ngoài phố, khi các kiếm sĩ cố giữ Muzan lại cho tới lúc mặt trời mọc. Chiến thuật không phả…

```text
Wide 16:9 landscape cinematic frame. a city skyline at the edge of night with the first sliver of dawn light on the horizon, wide shot, tense cold-to-warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Nhờ thuốc của Tamayo làm Muzan suy yếu, và nhờ nhiều người hy sinh, mặt trời cuối cùng cũng mọc. Muzan bị ánh…

```text
Wide 16:9 landscape cinematic frame. sunlight flooding over rooftops at dawn, scattering dark mist into the air, wide shot, radiant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Kaku để ý: Muzan bị đánh bại không phải bởi một người mạnh nhất, mà bởi những người thường truyền cho nhau su…

```text
Wide 16:9 landscape cinematic frame. many hands passing a single torch forward in a long line toward the sunrise, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Epilogue: thời hiện đại

Lời: Chương cuối của manga nhảy tới thời hiện đại, ở Tokyo. Ta thấy những người mang dáng dấp của các nhân vật cũ…

```text
Wide 16:9 landscape cinematic frame. a modern Tokyo street crossing on a sunny day with ordinary people walking, wide shot, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Và câu hỏi một nghìn năm cuối cùng được trả lời. Hoa bỉ ngạn xanh chỉ nở hai, ba ngày mỗi năm, và chỉ nở vào…

```text
Wide 16:9 landscape cinematic frame. a patch of blue spider lilies blooming in bright daylight in a quiet mountain clearing, close-up, radiant sunlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Một con quỷ không thể ra ánh sáng thì làm sao tìm được một bông hoa chỉ nở dưới ánh sáng? Muzan đã tìm sai cá…

```text
Wide 16:9 landscape cinematic frame. a shadow standing at the edge of a sunlit field, unable to step forward, while blue flowers bloom just out of reach, wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Trong phần epilogue, một nhà thực vật học ở thời hiện đại xác nhận điều này. Với người đọc, đó là lời chào cu…

```text
Wide 16:9 landscape cinematic frame. a botanist in a modern lab examining a single blue flower under a lamp, notes spread on the desk, close-up, clean bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Lý thuyết: những câu hỏi còn mở

Lời: Giờ tới phần lý thuyết. Kaku nhắc lại: đây là suy đoán của người hâm mộ, truyện chưa xác nhận.

```text
Wide 16:9 landscape cinematic frame. a notebook page stamped with the word THEORY in dotted outline, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Lý thuyết một: nếu Muzan kiên nhẫn chờ, thuốc của vị thầy thuốc có thể đã chữa khỏi bệnh cho cậu mà không biế…

```text
Wide 16:9 landscape cinematic frame. a medicine bowl with a small sprout growing out of it, symbolic still life, soft hopeful light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Lý thuyết hai: vì sao các Thượng Huyền không đổi suốt một trăm mười ba năm? Có người cho rằng sau Yoriichi, M…

```text
Wide 16:9 landscape cinematic frame. six stone pillars shrouded in thick fog, a single cautious shadow lurking behind them, wide shot, ominous grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Lý thuyết ba: gia đình Kamado có được Yoriichi chọn vì một lý do sâu xa hơn tình cờ? Truyện chỉ cho thấy đó l…

```text
Wide 16:9 landscape cinematic frame. two paths crossing in a snowy forest, one set of footprints meeting another, overhead shot, soft winter light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Độ chắc chắn của từng mốc

Lời: Tổng kết độ chắc chắn. Chắc chắn: Muzan hóa quỷ thời Heian vì thuốc có hoa bỉ ngạn xanh. Yoriichi gần giết Mu…

```text
Wide 16:9 landscape cinematic frame. a checklist on parchment with three items marked by solid circles, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Suy ra: năm thành lập Đội diệt quỷ, con số chính xác bao nhiêu năm giữa Yoriichi và Tanjiro, và tuổi chính xá…

```text
Wide 16:9 landscape cinematic frame. the same checklist with three items marked by half circles, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Lý thuyết: Muzan có thể được chữa khỏi hay không, và vì sao gia đình Kamado được chọn. Nếu bạn có bằng chứng…

```text
Wide 16:9 landscape cinematic frame. the same checklist with two items marked by dotted circles and a small question mark, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Toàn bộ dòng thời gian

Lời: Và đây là toàn bộ dòng thời gian trong một hình. Khoảng một nghìn năm trước: Muzan hóa quỷ, gia tộc Ubuyashik…

```text
Wide 16:9 landscape cinematic frame. a long timeline scroll with the first section illuminated showing a flower and a family crest icon, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Khoảng bốn trăm năm trước: Yoriichi, Hơi thở Mặt Trời, Muzan nổ thành một nghìn tám trăm mảnh, Tamayo tự do,…

```text
Wide 16:9 landscape cinematic frame. the middle section of the timeline scroll illuminated with sun, moon and torch icons, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Khoảng ba, bốn trăm năm im lặng: Thập Nhị Quỷ Nguyệt, một trăm mười ba năm Thượng Huyền không đổi.

```text
Wide 16:9 landscape cinematic frame. a quiet mostly empty section of the scroll with six small pillar icons, parchment close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Thời Đại Chính: Tanjiro, Nezuko vượt mặt trời, Vô Hạn Thành và bình minh cuối cùng. Rồi thời hiện đại: không…

```text
Wide 16:9 landscape cinematic frame. the full timeline scroll unrolled with the final section glowing brightly with a sunrise icon and a blue flower, wide overhead shot, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku: thời gian của quỷ và của người

Lời: Kaku nghĩ dòng thời gian này nói một điều rất rõ. Quỷ có thời gian vô hạn, nhưng chỉ sống cho bản thân. Con n…

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand flowing into many small cups held by different hands, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Muzan tìm cách sống mãi. Yoriichi và gia đình Kamado thì tìm cách để điều quan trọng sống mãi. Và phe thứ hai…

```text
Wide 16:9 landscape cinematic frame. a single torch flame being lit from another torch in a dark room, extreme close-up, warm firelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku muốn hỏi bạn: trong gia đình bạn, có điều gì được truyền lại qua nhiều thế hệ không? Một món ăn, một câu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding an old family recipe card with both wings, looking curious. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Kết

Lời: Một nghìn năm, bắt đầu bằng một liều thuốc chưa uống hết, và kết thúc bằng một buổi bình minh mà rất nhiều ng…

```text
Wide 16:9 landscape cinematic frame. a medicine bowl in the foreground and a sunrise over mountains in the background, symbolic composition, golden light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo, Kaku mở một cuốn sổ về giả kim thuật: Fullmetal Alchemist, luật trao đổi ngang giá, và vì sa…

```text
Wide 16:9 landscape cinematic frame. an alchemy circle drawn in chalk on a stone floor with a balance scale at its center, close-up, warm mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu dòng thời gian này giúp bạn hiểu Kimetsu rõ hơn, hãy đăng ký kênh và bật chuông, để không bỏ lỡ khi Kaku…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling the long scroll back up and waving goodbye with one wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc dòng thời gian

Khoảng 114 giây · cảnh s01–s10 · 1477 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này đi tới hết manga Kimetsu no Yaiba, kể cả trận cuối. Kaku sẽ báo trước khi vào vùng spoiler cuối truyện, để người chỉ xem anime có thể dừng lại.

<short pause> Khoảng một nghìn năm trước, ở kinh đô Nhật Bản thời Heian, có một chàng trai quý tộc mắc bệnh nặng. Thầy thuốc nói cậu khó sống qua tuổi hai mươi.

<short pause> Một vị thầy thuốc tận tâm thử cho cậu một loại thuốc mới. Và từ liều thuốc đó, con quỷ đầu tiên ra đời.

<short pause> Một nghìn năm sau, một cậu bé bán than ở vùng núi trở về nhà, và thấy gia đình mình đã bị tấn công. Giữa hai sự kiện đó là cả một nghìn năm lịch sử.

<short pause> Câu hỏi hôm nay: điều gì đã xảy ra trong một nghìn năm đó? Con quỷ đầu tiên đã làm gì, Đội diệt quỷ ra đời thế nào, và vì sao một gia đình bán than lại là chìa khóa của tất cả?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku trải dài dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ đêm thời Heian tới buổi bình minh cuối cùng.

<short pause> Trước hết, một điều cần biết: Kimetsu no Yaiba hiếm khi cho con số năm chính xác. Mốc chắc chắn nhất là thời Đại Chính, tức khoảng từ năm 1912 tới 1926, khi câu chuyện của Tanjiro diễn ra.

<short pause> Những mốc khác được tính ngược từ đó: khoảng một nghìn năm trước là thời Heian, khoảng bốn trăm năm trước là thời Chiến Quốc.

<short pause> Kaku sẽ đánh dấu mỗi mốc bằng ba mức. Chắc chắn: truyện nói rõ. Suy ra: tính từ các chi tiết. Lý thuyết: fan đoán, truyện chưa xác nhận.

<short pause> Và vì đây là dòng thời gian, Kaku sẽ nói nhiều về những người không xuất hiện trực tiếp trong phần lớn truyện, nhưng quyết định mọi thứ.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này đi tới hết manga Kimetsu no Yaiba, kể cả trận cuối. Kaku sẽ báo trước khi vào vùng spoiler cuối truyện, để người chỉ xem anime có thể dừng lại.

[pause] Khoảng một nghìn năm trước, ở kinh đô Nhật Bản thời Heian, có một chàng trai quý tộc mắc bệnh nặng. Thầy thuốc nói cậu khó sống qua tuổi hai mươi.

[pause] Một vị thầy thuốc tận tâm thử cho cậu một loại thuốc mới. Và từ liều thuốc đó, con quỷ đầu tiên ra đời.

[pause] Một nghìn năm sau, một cậu bé bán than ở vùng núi trở về nhà, và thấy gia đình mình đã bị tấn công. Giữa hai sự kiện đó là cả một nghìn năm lịch sử.

[pause] [curious] Câu hỏi hôm nay: điều gì đã xảy ra trong một nghìn năm đó? Con quỷ đầu tiên đã làm gì, Đội diệt quỷ ra đời thế nào, và vì sao một gia đình bán than lại là chìa khóa của tất cả?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku trải dài dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ đêm thời Heian tới buổi bình minh cuối cùng.

[pause] Trước hết, một điều cần biết: Kimetsu no Yaiba hiếm khi cho con số năm chính xác. Mốc chắc chắn nhất là thời Đại Chính, tức khoảng từ năm 1912 tới 1926, khi câu chuyện của Tanjiro diễn ra.

[pause] Những mốc khác được tính ngược từ đó: khoảng một nghìn năm trước là thời Heian, khoảng bốn trăm năm trước là thời Chiến Quốc.

[pause] Kaku sẽ đánh dấu mỗi mốc bằng ba mức. Chắc chắn: truyện nói rõ. Suy ra: tính từ các chi tiết. Lý thuyết: fan đoán, truyện chưa xác nhận.

[pause] Và vì đây là dòng thời gian, Kaku sẽ nói nhiều về những người không xuất hiện trực tiếp trong phần lớn truyện, nhưng quyết định mọi thứ.
```

### c02 · Thời Heian, khoảng 1.000 năm trước: con quỷ đầu tiên

Khoảng 88 giây · cảnh s11–s18 · 1141 ký tự

**Gemini**

```text
Chàng trai quý tộc đó chính là Kibutsuji Muzan. Vị thầy thuốc cho Muzan dùng một phương thuốc thử nghiệm, trong đó có một thành phần bí ẩn: hoa bỉ ngạn xanh.

<short pause> Thuốc dường như không có tác dụng ngay. Muzan nóng giận, cho rằng mình bị lừa, và giết chết vị thầy thuốc trước khi quá trình điều trị hoàn tất.

<short pause> Rồi Muzan nhận ra: cậu không chết nữa. Cơ thể mạnh hơn, lành lại mọi vết thương. <short pause> Nhưng cậu không thể bước ra ánh mặt trời, và cậu thèm ăn thịt người.

<short pause> Vì thầy thuốc đã chết, công thức cũng mất theo. Muzan không biết làm sao để hoàn thiện phương thuốc và vượt qua ánh mặt trời.

<short pause> Từ đó, Muzan dành một nghìn năm để tìm hoa bỉ ngạn xanh. Và một nghìn năm không tìm thấy. Cuối video, Kaku sẽ kể vì sao.

<short pause> Để tìm hoa và tìm cách vượt mặt trời, Muzan bắt đầu tạo ra những con quỷ khác bằng cách truyền máu của mình. Mọi con quỷ trong truyện đều có máu Muzan.

<short pause> Máu càng nhiều thì quỷ càng mạnh, nhưng cũng càng bị Muzan kiểm soát chặt. Muzan có thể nghe, thấy qua quỷ của mình, và giết chúng chỉ bằng một ý nghĩ.

<short pause> <laugh> Kaku để ý: mọi bi kịch trong truyện đều bắt đầu từ một khoảnh khắc thiếu kiên nhẫn. Nếu Muzan chờ thêm một chút, có lẽ cả nghìn năm sau đã khác.
```

**ElevenLabs**

```text
Chàng trai quý tộc đó chính là Kibutsuji Muzan. Vị thầy thuốc cho Muzan dùng một phương thuốc thử nghiệm, trong đó có một thành phần bí ẩn: hoa bỉ ngạn xanh.

[pause] Thuốc dường như không có tác dụng ngay. Muzan nóng giận, cho rằng mình bị lừa, và giết chết vị thầy thuốc trước khi quá trình điều trị hoàn tất.

[pause] Rồi Muzan nhận ra: cậu không chết nữa. Cơ thể mạnh hơn, lành lại mọi vết thương. [pause] Nhưng cậu không thể bước ra ánh mặt trời, và cậu thèm ăn thịt người.

[pause] Vì thầy thuốc đã chết, công thức cũng mất theo. Muzan không biết làm sao để hoàn thiện phương thuốc và vượt qua ánh mặt trời.

[pause] Từ đó, Muzan dành một nghìn năm để tìm hoa bỉ ngạn xanh. Và một nghìn năm không tìm thấy. Cuối video, Kaku sẽ kể vì sao.

[pause] Để tìm hoa và tìm cách vượt mặt trời, Muzan bắt đầu tạo ra những con quỷ khác bằng cách truyền máu của mình. Mọi con quỷ trong truyện đều có máu Muzan.

[pause] Máu càng nhiều thì quỷ càng mạnh, nhưng cũng càng bị Muzan kiểm soát chặt. Muzan có thể nghe, thấy qua quỷ của mình, và giết chúng chỉ bằng một ý nghĩ.

[pause] [chuckles] Kaku để ý: mọi bi kịch trong truyện đều bắt đầu từ một khoảnh khắc thiếu kiên nhẫn. Nếu Muzan chờ thêm một chút, có lẽ cả nghìn năm sau đã khác.
```

### c03 · Gia tộc bị nguyền rủa

Khoảng 70 giây · cảnh s19–s24 · 916 ký tự

**Gemini**

```text
Muzan có họ hàng. Gia tộc Ubuyashiki cùng dòng máu với cậu. Và theo truyện, vì dòng máu này sinh ra con quỷ đầu tiên, cả gia tộc bị nguyền rủa.

<short pause> Những người con trai trong gia tộc sinh ra đã yếu ớt, và thường không sống được lâu. Một vị thầy tu nói với họ rằng, muốn phá lời nguyền, họ phải diệt con quỷ xuất thân từ dòng máu mình.

<short pause> Kaku ghi mức suy ra: truyện không nói năm chính xác Đội diệt quỷ thành lập, nhưng cho thấy gia tộc Ubuyashiki dẫn dắt Đội qua nhiều thế hệ.

<short pause> Những kiếm sĩ đầu tiên chưa có hơi thở. Họ chỉ có lòng can đảm và những thanh kiếm đặc biệt, rèn từ quặng hấp thụ ánh mặt trời, gọi là kiếm Nhật Luân.

<short pause> Kiếm Nhật Luân và ánh mặt trời là hai thứ duy nhất có thể giết quỷ bằng cách chém đầu hoặc thiêu đốt. Trong nhiều thế kỷ, con người chiến đấu với vũ khí đó mà vẫn yếu thế.

<short pause> Hình ảnh lời nguyền của gia tộc này rất quan trọng. Nó biến cuộc chiến diệt quỷ thành một món nợ gia đình kéo dài cả nghìn năm.
```

**ElevenLabs**

```text
Muzan có họ hàng. Gia tộc Ubuyashiki cùng dòng máu với cậu. Và theo truyện, vì dòng máu này sinh ra con quỷ đầu tiên, cả gia tộc bị nguyền rủa.

[pause] Những người con trai trong gia tộc sinh ra đã yếu ớt, và thường không sống được lâu. Một vị thầy tu nói với họ rằng, muốn phá lời nguyền, họ phải diệt con quỷ xuất thân từ dòng máu mình.

[pause] Kaku ghi mức suy ra: truyện không nói năm chính xác Đội diệt quỷ thành lập, nhưng cho thấy gia tộc Ubuyashiki dẫn dắt Đội qua nhiều thế hệ.

[pause] Những kiếm sĩ đầu tiên chưa có hơi thở. Họ chỉ có lòng can đảm và những thanh kiếm đặc biệt, rèn từ quặng hấp thụ ánh mặt trời, gọi là kiếm Nhật Luân.

[pause] Kiếm Nhật Luân và ánh mặt trời là hai thứ duy nhất có thể giết quỷ bằng cách chém đầu hoặc thiêu đốt. Trong nhiều thế kỷ, con người chiến đấu với vũ khí đó mà vẫn yếu thế.

[pause] Hình ảnh lời nguyền của gia tộc này rất quan trọng. Nó biến cuộc chiến diệt quỷ thành một món nợ gia đình kéo dài cả nghìn năm.
```

### c04 · Thời Chiến Quốc, khoảng 400 năm trước: người mang mặt trời

Khoảng 102 giây · cảnh s25–s33 · 1328 ký tự

**Gemini**

```text
Nhảy tới khoảng bốn trăm năm trước, thời Chiến Quốc. Một cậu bé tên Tsugikuni Yoriichi ra đời, với một dấu vết bẩm sinh và tài năng kiếm thuật như trời ban.

<short pause> Yoriichi có một người anh song sinh, Michikatsu. Người anh luôn sống trong cái bóng của em, và nỗi ghen tị đó sẽ trở thành một bi kịch.

<short pause> Yoriichi là người đầu tiên dùng Hơi thở, cụ thể là Hơi thở Mặt Trời. Anh dạy lại cho các kiếm sĩ, và từ đó sinh ra năm nhánh hơi thở chính. Video cây phả hệ hơi thở của Kaku đã nói kỹ phần này.

<short pause> Cũng thời đó, nhiều kiếm sĩ đánh thức được một dấu ấn trên cơ thể, giúp họ mạnh vượt bậc. <short pause> Nhưng cái giá rất nặng: người có dấu ấn thường không sống quá hai mươi lăm tuổi.

<short pause> Và rồi Yoriichi gặp Muzan. Đây là lần duy nhất trong một nghìn năm, Muzan cảm thấy sợ hãi thật sự.

<short pause> Yoriichi gần như giết được Muzan. Để sống sót, Muzan phải tự nổ tung thành khoảng một nghìn tám trăm mảnh và chạy trốn theo mọi hướng.

<short pause> Trong đêm đó, một con quỷ nữ tên Tamayo, người vốn phục vụ Muzan, được giải thoát khỏi sự kiểm soát. Yoriichi tha cho bà. Bà sẽ trở thành một mảnh ghép quan trọng bốn trăm năm sau.

<short pause> Nhưng thất bại đó có giá. Muzan trốn thoát, và người anh Michikatsu lại trở thành quỷ. Yoriichi bị trục xuất khỏi Đội diệt quỷ.

<short pause> Michikatsu trở thành Kokushibo, một trong những con quỷ mạnh nhất. Hai anh em song sinh, một người là mặt trời, một người là mặt trăng.
```

**ElevenLabs**

```text
Nhảy tới khoảng bốn trăm năm trước, thời Chiến Quốc. Một cậu bé tên Tsugikuni Yoriichi ra đời, với một dấu vết bẩm sinh và tài năng kiếm thuật như trời ban.

[pause] Yoriichi có một người anh song sinh, Michikatsu. Người anh luôn sống trong cái bóng của em, và nỗi ghen tị đó sẽ trở thành một bi kịch.

[pause] Yoriichi là người đầu tiên dùng Hơi thở, cụ thể là Hơi thở Mặt Trời. Anh dạy lại cho các kiếm sĩ, và từ đó sinh ra năm nhánh hơi thở chính. Video cây phả hệ hơi thở của Kaku đã nói kỹ phần này.

[pause] Cũng thời đó, nhiều kiếm sĩ đánh thức được một dấu ấn trên cơ thể, giúp họ mạnh vượt bậc. [pause] Nhưng cái giá rất nặng: người có dấu ấn thường không sống quá hai mươi lăm tuổi.

[pause] Và rồi Yoriichi gặp Muzan. Đây là lần duy nhất trong một nghìn năm, Muzan cảm thấy sợ hãi thật sự.

[pause] Yoriichi gần như giết được Muzan. Để sống sót, Muzan phải tự nổ tung thành khoảng một nghìn tám trăm mảnh và chạy trốn theo mọi hướng.

[pause] Trong đêm đó, một con quỷ nữ tên Tamayo, người vốn phục vụ Muzan, được giải thoát khỏi sự kiểm soát. Yoriichi tha cho bà. Bà sẽ trở thành một mảnh ghép quan trọng bốn trăm năm sau.

[pause] Nhưng thất bại đó có giá. Muzan trốn thoát, và người anh Michikatsu lại trở thành quỷ. Yoriichi bị trục xuất khỏi Đội diệt quỷ.

[pause] Michikatsu trở thành Kokushibo, một trong những con quỷ mạnh nhất. Hai anh em song sinh, một người là mặt trời, một người là mặt trăng.
```

### c05 · Ngọn lửa âm thầm: gia đình bán than / Những thế kỷ tích lũy

Khoảng 122 giây · cảnh s34–s44 · 1588 ký tự

**Gemini**

```text
Trước khi rời đi, Yoriichi gặp một gia đình bán than họ Kamado. Anh kể cho họ nghe câu chuyện của mình, và cho họ xem kiếm thuật mặt trời.

<short pause> Gia đình Kamado không phải kiếm sĩ. <short pause> Nhưng họ biến những động tác đó thành một điệu múa cầu thần, gọi là Hinokami Kagura, múa mỗi năm vào đầu năm mới.

<short pause> Họ cũng giữ một món đồ Yoriichi để lại, và truyền qua nhiều thế hệ. Họ không biết mình đang giữ gì. Họ chỉ hứa sẽ không để nó thất truyền.

<short pause> <laugh> Kaku thấy đây là chi tiết đẹp nhất trong cả dòng thời gian. Kiếm thuật mạnh nhất lịch sử không nằm trong võ đường nào, mà được giữ bởi một gia đình bình thường, dưới dạng một điệu múa.

<short pause> Sau Yoriichi, Muzan truy lùng những người dùng Hơi thở Mặt Trời. Kiếm thuật này gần như biến mất khỏi Đội diệt quỷ. <short pause> Nhưng nó vẫn sống, trong một điệu múa trên núi.

<short pause> Từ thời Chiến Quốc tới thời Đại Chính là khoảng ba, bốn trăm năm. Truyện kể rất ít về giai đoạn này, nên Kaku ghép lại từ những chi tiết rải rác.

<short pause> Muzan lập ra nhóm Thập Nhị Quỷ Nguyệt, mười hai con quỷ mạnh nhất, chia làm sáu Thượng Huyền và sáu Hạ Huyền.

<short pause> Các Hạ Huyền thay đổi liên tục. <short pause> Nhưng sáu Thượng Huyền thì giữ nguyên suốt khoảng một trăm mười ba năm. Không kiếm sĩ nào hạ được một Thượng Huyền trong thời gian đó.

<short pause> Tamayo thì dùng những thế kỷ đó để nghiên cứu y học. Bà tự thay đổi cơ thể để thoát hẳn khỏi Muzan, và cần rất ít máu người để sống.

<short pause> Và Muzan học cách ẩn mình. Hắn sống giữa con người, đổi tên, đổi vẻ ngoài, thậm chí có cả một gia đình giả để che giấu.

<short pause> Kaku để ý: trong suốt những thế kỷ này, quỷ có thời gian, còn con người thì có sự kế thừa. Quỷ sống lâu hơn, nhưng con người truyền lại cho nhau.
```

**ElevenLabs**

```text
Trước khi rời đi, Yoriichi gặp một gia đình bán than họ Kamado. Anh kể cho họ nghe câu chuyện của mình, và cho họ xem kiếm thuật mặt trời.

[pause] Gia đình Kamado không phải kiếm sĩ. [pause] Nhưng họ biến những động tác đó thành một điệu múa cầu thần, gọi là Hinokami Kagura, múa mỗi năm vào đầu năm mới.

[pause] Họ cũng giữ một món đồ Yoriichi để lại, và truyền qua nhiều thế hệ. Họ không biết mình đang giữ gì. Họ chỉ hứa sẽ không để nó thất truyền.

[pause] [chuckles] Kaku thấy đây là chi tiết đẹp nhất trong cả dòng thời gian. Kiếm thuật mạnh nhất lịch sử không nằm trong võ đường nào, mà được giữ bởi một gia đình bình thường, dưới dạng một điệu múa.

[pause] Sau Yoriichi, Muzan truy lùng những người dùng Hơi thở Mặt Trời. Kiếm thuật này gần như biến mất khỏi Đội diệt quỷ. [pause] Nhưng nó vẫn sống, trong một điệu múa trên núi.

[pause] Từ thời Chiến Quốc tới thời Đại Chính là khoảng ba, bốn trăm năm. Truyện kể rất ít về giai đoạn này, nên Kaku ghép lại từ những chi tiết rải rác.

[pause] Muzan lập ra nhóm Thập Nhị Quỷ Nguyệt, mười hai con quỷ mạnh nhất, chia làm sáu Thượng Huyền và sáu Hạ Huyền.

[pause] Các Hạ Huyền thay đổi liên tục. [pause] Nhưng sáu Thượng Huyền thì giữ nguyên suốt khoảng một trăm mười ba năm. Không kiếm sĩ nào hạ được một Thượng Huyền trong thời gian đó.

[pause] Tamayo thì dùng những thế kỷ đó để nghiên cứu y học. Bà tự thay đổi cơ thể để thoát hẳn khỏi Muzan, và cần rất ít máu người để sống.

[pause] Và Muzan học cách ẩn mình. Hắn sống giữa con người, đổi tên, đổi vẻ ngoài, thậm chí có cả một gia đình giả để che giấu.

[pause] Kaku để ý: trong suốt những thế kỷ này, quỷ có thời gian, còn con người thì có sự kế thừa. Quỷ sống lâu hơn, nhưng con người truyền lại cho nhau.
```

### c06 · Thời Đại Chính: Tanjiro

Khoảng 104 giây · cảnh s45–s53 · 1347 ký tự

**Gemini**

```text
Thời Đại Chính. Kamado Tanjiro, con trai cả của gia đình bán than, đi xuống thị trấn bán than. Khi trở về, cả gia đình đã bị Muzan tấn công. Chỉ em gái Nezuko còn sống, nhưng đã hóa quỷ.

<short pause> Kiếm sĩ Tomioka Giyu gặp hai anh em, nhận ra Nezuko khác những con quỷ khác, và gửi Tanjiro tới thầy Urokodaki.

<short pause> Sau khoảng hai năm luyện tập, Tanjiro vượt qua Kỳ tuyển chọn cuối cùng và gia nhập Đội diệt quỷ. Cậu bắt đầu hành trình tìm cách biến em gái trở lại làm người.

<short pause> Ở Asakusa, Tanjiro lần đầu thấy Muzan, đang sống như một người đàn ông bình thường giữa phố. Cũng tại đây, cậu gặp Tamayo. Bốn trăm năm sau đêm Yoriichi, hai mảnh ghép cuối cùng gặp nhau.

<short pause> Rồi tới núi Natagumo, nơi Tanjiro lần đầu dùng điệu múa của cha thành kiếm thuật. Trận với Rui là nơi Hinokami Kagura thức tỉnh. Kaku đã phân tích trận này trong một video riêng.

<short pause> Chuyến tàu Vô Tận, nơi Viêm Trụ Rengoku chiến đấu với Thượng Huyền Tam và hy sinh khi trời sắp sáng.

<short pause> Phố Đèn Đỏ: Âm Trụ Uzui cùng Tanjiro và các bạn hạ được Thượng Huyền Lục. Đây là lần đầu tiên sau một trăm mười ba năm một Thượng Huyền bị tiêu diệt.

<short pause> Làng Thợ Rèn: Nezuko vượt qua được ánh mặt trời. Muzan lập tức đổi mục tiêu: không cần tìm hoa nữa, hắn chỉ cần bắt Nezuko.

<short pause> Tính từ đêm Heian tới đây là khoảng một nghìn năm. Lần đầu tiên, Muzan có trong tầm tay thứ hắn tìm kiếm. Và lần đầu tiên, Đội diệt quỷ có cơ hội thật sự.
```

**ElevenLabs**

```text
Thời Đại Chính. Kamado Tanjiro, con trai cả của gia đình bán than, đi xuống thị trấn bán than. Khi trở về, cả gia đình đã bị Muzan tấn công. Chỉ em gái Nezuko còn sống, nhưng đã hóa quỷ.

[pause] Kiếm sĩ Tomioka Giyu gặp hai anh em, nhận ra Nezuko khác những con quỷ khác, và gửi Tanjiro tới thầy Urokodaki.

[pause] Sau khoảng hai năm luyện tập, Tanjiro vượt qua Kỳ tuyển chọn cuối cùng và gia nhập Đội diệt quỷ. Cậu bắt đầu hành trình tìm cách biến em gái trở lại làm người.

[pause] Ở Asakusa, Tanjiro lần đầu thấy Muzan, đang sống như một người đàn ông bình thường giữa phố. Cũng tại đây, cậu gặp Tamayo. Bốn trăm năm sau đêm Yoriichi, hai mảnh ghép cuối cùng gặp nhau.

[pause] Rồi tới núi Natagumo, nơi Tanjiro lần đầu dùng điệu múa của cha thành kiếm thuật. Trận với Rui là nơi Hinokami Kagura thức tỉnh. Kaku đã phân tích trận này trong một video riêng.

[pause] Chuyến tàu Vô Tận, nơi Viêm Trụ Rengoku chiến đấu với Thượng Huyền Tam và hy sinh khi trời sắp sáng.

[pause] Phố Đèn Đỏ: Âm Trụ Uzui cùng Tanjiro và các bạn hạ được Thượng Huyền Lục. Đây là lần đầu tiên sau một trăm mười ba năm một Thượng Huyền bị tiêu diệt.

[pause] Làng Thợ Rèn: Nezuko vượt qua được ánh mặt trời. Muzan lập tức đổi mục tiêu: không cần tìm hoa nữa, hắn chỉ cần bắt Nezuko.

[pause] Tính từ đêm Heian tới đây là khoảng một nghìn năm. Lần đầu tiên, Muzan có trong tầm tay thứ hắn tìm kiếm. Và lần đầu tiên, Đội diệt quỷ có cơ hội thật sự.
```

### c07 · Vùng spoiler cuối truyện / Epilogue: thời hiện đại

Khoảng 142 giây · cảnh s54–s65 · 1843 ký tự

**Gemini**

```text
Từ đây là spoiler phần cuối manga, chưa có trong anime truyền hình. Nếu bạn muốn chờ phim, hãy tua tới chương Lý thuyết.

<short pause> Sau Làng Thợ Rèn, các Trụ cột mở một đợt huấn luyện chung để nhiều kiếm sĩ đánh thức dấu ấn. Họ biết mình đang chuẩn bị cho trận cuối cùng.

<short pause> Thủ lĩnh Ubuyashiki Kagaya, người mang lời nguyền của gia tộc, đón Muzan tới nhà mình. Ông chấp nhận hy sinh để mở màn trận chiến. Một nghìn năm nợ gia tộc được trả bằng chính mạng sống.

<short pause> Muzan kéo toàn bộ Đội diệt quỷ vào Vô Hạn Thành, một pháo đài mê cung của quỷ. Anime đang chuyển thể phần này thành bộ ba phim điện ảnh.

<short pause> Trong Vô Hạn Thành, Kokushibo đối mặt với những kiếm sĩ mang hơi thở. Bốn trăm năm sau, người anh song sinh vẫn chưa thoát khỏi cái bóng của em.

<short pause> Trận cuối diễn ra ngoài phố, khi các kiếm sĩ cố giữ Muzan lại cho tới lúc mặt trời mọc. Chiến thuật không phải chém chết, mà là trụ vững đủ lâu.

<short pause> Nhờ thuốc của Tamayo làm Muzan suy yếu, và nhờ nhiều người hy sinh, mặt trời cuối cùng cũng mọc. Muzan bị ánh sáng thiêu đốt. Một nghìn năm kết thúc trong một buổi sáng.

<short pause> Kaku để ý: Muzan bị đánh bại không phải bởi một người mạnh nhất, mà bởi những người thường truyền cho nhau suốt một nghìn năm. Đúng như điều Yoriichi từng tin.

<short pause> Chương cuối của manga nhảy tới thời hiện đại, ở Tokyo. Ta thấy những người mang dáng dấp của các nhân vật cũ đang sống một cuộc sống bình thường, không còn quỷ.

<short pause> Và câu hỏi một nghìn năm cuối cùng được trả lời. Hoa bỉ ngạn xanh chỉ nở hai, ba ngày mỗi năm, và chỉ nở vào ban ngày.

<short pause> Một con quỷ không thể ra ánh sáng thì làm sao tìm được một bông hoa chỉ nở dưới ánh sáng? Muzan đã tìm sai cách ngay từ đầu. Kaku thấy đây là một cú châm biếm tuyệt vời của tác giả.

<short pause> Trong phần epilogue, một nhà thực vật học ở thời hiện đại xác nhận điều này. Với người đọc, đó là lời chào cuối của câu chuyện: bông hoa luôn ở đó, chỉ là không dành cho kẻ trốn ánh sáng.
```

**ElevenLabs**

```text
Từ đây là spoiler phần cuối manga, chưa có trong anime truyền hình. Nếu bạn muốn chờ phim, hãy tua tới chương Lý thuyết.

[pause] Sau Làng Thợ Rèn, các Trụ cột mở một đợt huấn luyện chung để nhiều kiếm sĩ đánh thức dấu ấn. Họ biết mình đang chuẩn bị cho trận cuối cùng.

[pause] Thủ lĩnh Ubuyashiki Kagaya, người mang lời nguyền của gia tộc, đón Muzan tới nhà mình. Ông chấp nhận hy sinh để mở màn trận chiến. Một nghìn năm nợ gia tộc được trả bằng chính mạng sống.

[pause] Muzan kéo toàn bộ Đội diệt quỷ vào Vô Hạn Thành, một pháo đài mê cung của quỷ. Anime đang chuyển thể phần này thành bộ ba phim điện ảnh.

[pause] Trong Vô Hạn Thành, Kokushibo đối mặt với những kiếm sĩ mang hơi thở. Bốn trăm năm sau, người anh song sinh vẫn chưa thoát khỏi cái bóng của em.

[pause] Trận cuối diễn ra ngoài phố, khi các kiếm sĩ cố giữ Muzan lại cho tới lúc mặt trời mọc. Chiến thuật không phải chém chết, mà là trụ vững đủ lâu.

[pause] Nhờ thuốc của Tamayo làm Muzan suy yếu, và nhờ nhiều người hy sinh, mặt trời cuối cùng cũng mọc. Muzan bị ánh sáng thiêu đốt. Một nghìn năm kết thúc trong một buổi sáng.

[pause] Kaku để ý: Muzan bị đánh bại không phải bởi một người mạnh nhất, mà bởi những người thường truyền cho nhau suốt một nghìn năm. Đúng như điều Yoriichi từng tin.

[pause] Chương cuối của manga nhảy tới thời hiện đại, ở Tokyo. Ta thấy những người mang dáng dấp của các nhân vật cũ đang sống một cuộc sống bình thường, không còn quỷ.

[pause] Và câu hỏi một nghìn năm cuối cùng được trả lời. Hoa bỉ ngạn xanh chỉ nở hai, ba ngày mỗi năm, và chỉ nở vào ban ngày.

[pause] [curious] Một con quỷ không thể ra ánh sáng thì làm sao tìm được một bông hoa chỉ nở dưới ánh sáng? Muzan đã tìm sai cách ngay từ đầu. Kaku thấy đây là một cú châm biếm tuyệt vời của tác giả.

[pause] Trong phần epilogue, một nhà thực vật học ở thời hiện đại xác nhận điều này. Với người đọc, đó là lời chào cuối của câu chuyện: bông hoa luôn ở đó, chỉ là không dành cho kẻ trốn ánh sáng.
```

### c08 · Lý thuyết: những câu hỏi còn mở / Độ chắc chắn của từng mốc / Toàn bộ dòng thời gian

Khoảng 127 giây · cảnh s66–s76 · 1650 ký tự

**Gemini**

```text
Giờ tới phần lý thuyết. Kaku nhắc lại: đây là suy đoán của người hâm mộ, truyện chưa xác nhận.

<short pause> Lý thuyết một: nếu Muzan kiên nhẫn chờ, thuốc của vị thầy thuốc có thể đã chữa khỏi bệnh cho cậu mà không biến cậu thành quỷ. Nhiều chi tiết gợi ý như vậy, nhưng truyện không nói thẳng.

<short pause> Lý thuyết hai: vì sao các Thượng Huyền không đổi suốt một trăm mười ba năm? Có người cho rằng sau Yoriichi, Muzan quá sợ nên chỉ giữ những con quỷ mạnh nhất và tránh xung đột lớn với Đội.

<short pause> Lý thuyết ba: gia đình Kamado có được Yoriichi chọn vì một lý do sâu xa hơn tình cờ? Truyện chỉ cho thấy đó là một cuộc gặp gỡ. Kaku thích tin rằng đó là tình cờ, vì như vậy câu chuyện đẹp hơn.

<short pause> Tổng kết độ chắc chắn. Chắc chắn: Muzan hóa quỷ thời Heian vì thuốc có hoa bỉ ngạn xanh. Yoriichi gần giết Muzan thời Chiến Quốc. Câu chuyện chính diễn ra thời Đại Chính.

<short pause> Suy ra: năm thành lập Đội diệt quỷ, con số chính xác bao nhiêu năm giữa Yoriichi và Tanjiro, và tuổi chính xác của các Thượng Huyền.

<short pause> Lý thuyết: Muzan có thể được chữa khỏi hay không, và vì sao gia đình Kamado được chọn. Nếu bạn có bằng chứng khác, hãy viết vào bình luận.

<short pause> Và đây là toàn bộ dòng thời gian trong một hình. Khoảng một nghìn năm trước: Muzan hóa quỷ, gia tộc Ubuyashiki bị nguyền.

<short pause> Khoảng bốn trăm năm trước: Yoriichi, Hơi thở Mặt Trời, Muzan nổ thành một nghìn tám trăm mảnh, Tamayo tự do, Kokushibo ra đời, và điệu múa được trao cho gia đình Kamado.

<short pause> Khoảng ba, bốn trăm năm im lặng: Thập Nhị Quỷ Nguyệt, một trăm mười ba năm Thượng Huyền không đổi.

<short pause> Thời Đại Chính: Tanjiro, Nezuko vượt mặt trời, Vô Hạn Thành và bình minh cuối cùng. Rồi thời hiện đại: không còn quỷ, và hoa bỉ ngạn xanh vẫn nở dưới ánh mặt trời.
```

**ElevenLabs**

```text
Giờ tới phần lý thuyết. Kaku nhắc lại: đây là suy đoán của người hâm mộ, truyện chưa xác nhận.

[pause] Lý thuyết một: nếu Muzan kiên nhẫn chờ, thuốc của vị thầy thuốc có thể đã chữa khỏi bệnh cho cậu mà không biến cậu thành quỷ. Nhiều chi tiết gợi ý như vậy, nhưng truyện không nói thẳng.

[pause] [curious] Lý thuyết hai: vì sao các Thượng Huyền không đổi suốt một trăm mười ba năm? Có người cho rằng sau Yoriichi, Muzan quá sợ nên chỉ giữ những con quỷ mạnh nhất và tránh xung đột lớn với Đội.

[pause] Lý thuyết ba: gia đình Kamado có được Yoriichi chọn vì một lý do sâu xa hơn tình cờ? Truyện chỉ cho thấy đó là một cuộc gặp gỡ. Kaku thích tin rằng đó là tình cờ, vì như vậy câu chuyện đẹp hơn.

[pause] Tổng kết độ chắc chắn. Chắc chắn: Muzan hóa quỷ thời Heian vì thuốc có hoa bỉ ngạn xanh. Yoriichi gần giết Muzan thời Chiến Quốc. Câu chuyện chính diễn ra thời Đại Chính.

[pause] Suy ra: năm thành lập Đội diệt quỷ, con số chính xác bao nhiêu năm giữa Yoriichi và Tanjiro, và tuổi chính xác của các Thượng Huyền.

[pause] Lý thuyết: Muzan có thể được chữa khỏi hay không, và vì sao gia đình Kamado được chọn. Nếu bạn có bằng chứng khác, hãy viết vào bình luận.

[pause] Và đây là toàn bộ dòng thời gian trong một hình. Khoảng một nghìn năm trước: Muzan hóa quỷ, gia tộc Ubuyashiki bị nguyền.

[pause] Khoảng bốn trăm năm trước: Yoriichi, Hơi thở Mặt Trời, Muzan nổ thành một nghìn tám trăm mảnh, Tamayo tự do, Kokushibo ra đời, và điệu múa được trao cho gia đình Kamado.

[pause] Khoảng ba, bốn trăm năm im lặng: Thập Nhị Quỷ Nguyệt, một trăm mười ba năm Thượng Huyền không đổi.

[pause] Thời Đại Chính: Tanjiro, Nezuko vượt mặt trời, Vô Hạn Thành và bình minh cuối cùng. Rồi thời hiện đại: không còn quỷ, và hoa bỉ ngạn xanh vẫn nở dưới ánh mặt trời.
```

### c09 · Góc nhìn của Kaku: thời gian của quỷ và của người / Kết

Khoảng 70 giây · cảnh s77–s82 · 915 ký tự

**Gemini**

```text
Kaku nghĩ dòng thời gian này nói một điều rất rõ. Quỷ có thời gian vô hạn, nhưng chỉ sống cho bản thân. Con người có thời gian ngắn ngủi, nhưng biết truyền lại cho người sau.

<short pause> Muzan tìm cách sống mãi. Yoriichi và gia đình Kamado thì tìm cách để điều quan trọng sống mãi. Và phe thứ hai đã thắng.

<short pause> <laugh> Kaku muốn hỏi bạn: trong gia đình bạn, có điều gì được truyền lại qua nhiều thế hệ không? Một món ăn, một câu chuyện, một nghề? Kể cho Kaku nghe trong bình luận nhé.

<short pause> Một nghìn năm, bắt đầu bằng một liều thuốc chưa uống hết, và kết thúc bằng một buổi bình minh mà rất nhiều người đã chờ.

<short pause> Video tiếp theo, Kaku mở một cuốn sổ về giả kim thuật: Fullmetal Alchemist, luật trao đổi ngang giá, và vì sao muốn có gì thì phải mất đi thứ tương đương.

<short pause> Nếu dòng thời gian này giúp bạn hiểu Kimetsu rõ hơn, hãy đăng ký kênh và bật chuông, để không bỏ lỡ khi Kaku tiếp tục trải những cuộn sổ dài như thế này. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Kaku nghĩ dòng thời gian này nói một điều rất rõ. Quỷ có thời gian vô hạn, nhưng chỉ sống cho bản thân. Con người có thời gian ngắn ngủi, nhưng biết truyền lại cho người sau.

[pause] Muzan tìm cách sống mãi. Yoriichi và gia đình Kamado thì tìm cách để điều quan trọng sống mãi. Và phe thứ hai đã thắng.

[pause] [chuckles] Kaku muốn hỏi bạn: trong gia đình bạn, có điều gì được truyền lại qua nhiều thế hệ không? [curious] Một món ăn, một câu chuyện, một nghề? Kể cho Kaku nghe trong bình luận nhé.

[pause] Một nghìn năm, bắt đầu bằng một liều thuốc chưa uống hết, và kết thúc bằng một buổi bình minh mà rất nhiều người đã chờ.

[pause] Video tiếp theo, Kaku mở một cuốn sổ về giả kim thuật: Fullmetal Alchemist, luật trao đổi ngang giá, và vì sao muốn có gì thì phải mất đi thứ tương đương.

[pause] Nếu dòng thời gian này giúp bạn hiểu Kimetsu rõ hơn, hãy đăng ký kênh và bật chuông, để không bỏ lỡ khi Kaku tiếp tục trải những cuộn sổ dài như thế này. Kaku gấp sổ đây, hẹn gặp lại!
```
