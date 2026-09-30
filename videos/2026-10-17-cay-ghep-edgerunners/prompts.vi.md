# Bộ prompt · Cyberpunk Edgerunners: Cấy ghép cơ thể và loạn thần máy hoạt động thế nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (80 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Cyberpunk: Edgerunners mùa một. Mùa hai lên Netflix ngày 20 tháng 10 năm 2026, nên…

```text
Wide 16:9 landscape cinematic frame. a rainy neon-lit alley at night, a closed notebook resting on a wet crate under a flickering sign, wide establishing shot, magenta and cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy tưởng tượng một thành phố nơi bạn có thể mua một cánh tay mạnh như máy xúc, một đôi mắt nhìn xuyên đêm, h…

```text
Wide 16:9 landscape cinematic frame. a futuristic clinic display window showing mechanical arms, glowing artificial eyes and small chips on velvet stands, wide shot, cold neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Chỉ cần đủ tiền. Và chỉ cần bạn chấp nhận một cái giá không ghi trên hóa đơn: một phần con người của bạn.

```text
Wide 16:9 landscape cinematic frame. a receipt printing out of a machine with the last line smeared and unreadable, extreme close-up, harsh fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đó là Night City trong Cyberpunk: Edgerunners, nơi người ta gọi những bộ phận máy móc gắn vào cơ thể là chrom…

```text
Wide 16:9 landscape cinematic frame. a crowded futuristic street where many pedestrians have subtle glowing mechanical parts, one figure in the center with too many glowing seams, wide shot, rain and neon. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Night City là thành phố của các tập đoàn khổng lồ và những băng đảng đường phố. Người giàu sống trên những tò…

```text
Wide 16:9 landscape cinematic frame. a vertical city composition: gleaming corporate towers above the clouds, crowded dark streets and markets far below, wide shot, neon and fog. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình giải thích hệ thống cấy ghép trong Edgerunners hoạt động thế nào: lu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny visor, opening its notebook on a workbench full of small mechanical parts, warm lamp light. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Và cuối video, Kaku sẽ tách bạch phần nào có thật ngoài đời, phần nào là hư cấu. Vì chuyện gắn máy vào người…

```text
Wide 16:9 landscape cinematic frame. a split image: a futuristic glowing arm on the left, a simple modern prosthetic hand on the right, symmetrical composition, soft light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Luật nền: chrome là gì

Lời: Trong Edgerunners, chrome là mọi bộ phận nhân tạo gắn vào cơ thể: tay chân, mắt, da, hệ thần kinh, cả những c…

```text
Wide 16:9 landscape cinematic frame. an anatomical diagram of a human silhouette with glowing highlighted zones for arms, eyes, spine and brain, parchment and neon hybrid style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Người lắp chrome gọi là bác sĩ chợ đen, hay ripperdoc. Có người làm trong phòng khám sạch sẽ, có người làm tr…

```text
Wide 16:9 landscape cinematic frame. a cramped underground clinic with a reclining chair, hanging cables and old surgical tools under a single swinging lamp, wide shot, green-tinted light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Chrome còn là thời trang. Có người gắn hình xăm phát sáng dưới da, có người thay màu mắt theo tâm trạng. Tron…

```text
Wide 16:9 landscape cinematic frame. young people in a night market showing off glowing subdermal tattoos and color-shifting artificial eyes, medium shot, playful neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Và cũng giống điện thoại, đồ tốt thì đắt, đồ rẻ thì dễ hỏng, còn đồ lậu thì không ai bảo hành.

```text
Wide 16:9 landscape cinematic frame. a shady street stall selling used implants in plastic bins with handwritten price tags, close-up, flickering neon. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Ở Night City, chrome không phải xa xỉ. Nó là công cụ để sống. Người bảo vệ cần tay khỏe, người lái xe cần mắt…

```text
Wide 16:9 landscape cinematic frame. a montage of three silhouettes at work: a guard lifting a heavy door, a driver with glowing eyes, a mercenary crouching, triptych composition, neon light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Luật nền thứ nhất vì vậy rất đơn giản: chrome cho bạn thêm năng lực, và năng lực càng mạnh thì càng đắt, về c…

```text
Wide 16:9 landscape cinematic frame. a price tag hanging from a mechanical arm, the numbers glowing and rising, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku đã thử nghĩ xem mình nên lắp gì. Kết luận: cặp kính của Kaku đã là chrome duy nhất Kaku cần. Và nó cũng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adjusting its oversized round glasses in a mirror, the glasses slightly crooked. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Nhánh 1: phản xạ và tốc độ

Lời: Nhánh chrome nổi tiếng nhất trong Edgerunners là bộ tăng tốc phản xạ, trong phim gọi là Sandevistan. Nó gắn d…

```text
Wide 16:9 landscape cinematic frame. a sleek glowing implant running along a spine seen from behind, a faint trail of light behind the silhouette, close-up, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Khi kích hoạt, người dùng di chuyển và phản ứng nhanh tới mức cả thế giới xung quanh như đứng im. Viên đạn lơ…

```text
Wide 16:9 landscape cinematic frame. raindrops and a bullet frozen in midair on a neon street, a blurred figure moving between them leaving a rainbow afterimage trail, dynamic wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Lần đầu dùng nó, David đang ở trường, trước mặt những kẻ bắt nạt từng coi thường cậu. Trong vài giây, cậu làm…

```text
Wide 16:9 landscape cinematic frame. a school hallway where a group of students stand frozen in shock while a teenager appears behind them in a blur of light, wide shot, cold fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thật: nếu Kaku có Sandevistan, Kaku chỉ dùng để kịp chuyến xe buýt buổi sáng. Và chắc vẫn trễ,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sprinting comically toward a departing bus with glasses flying off its face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nhân vật chính David có được một bộ tăng tốc loại quân sự, loại dành cho binh lính chứ không dành cho một cậu…

```text
Wide 16:9 landscape cinematic frame. a teenager lying on a clinic chair looking at a military-grade implant case opened beside him, close-up, harsh green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Cái giá của nhánh này là cơ thể và bộ não phải chịu tải khổng lồ. Dùng lâu sẽ đau, chảy máu mũi, choáng váng.…

```text
Wide 16:9 landscape cinematic frame. a teenager kneeling in the rain, one hand on the ground, a trail of fading afterimages behind him, medium shot, cold neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Nhánh 2: vũ khí trong cơ thể

Lời: Nhánh thứ hai là biến chính cơ thể thành vũ khí. Có lưỡi dao gập giấu trong cẳng tay, có cánh tay cơ khí đấm…

```text
Wide 16:9 landscape cinematic frame. three mechanical forearms displayed side by side: one with folding blades, one bulky and armored, one with a thin glowing wire coiled at the wrist, close-up, product lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Maine, thủ lĩnh nhóm đánh thuê mà David gia nhập, có đôi tay cơ khí to và khỏe tới mức lật được cả chiếc xe.…

```text
Wide 16:9 landscape cinematic frame. a huge muscular mercenary silhouette with heavy mechanical arms flipping a car on a highway overpass, dynamic low-angle shot, orange sodium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Người cầm súng còn có thể bị tước vũ khí. Người mà cánh tay chính là vũ khí thì không. Ở Night City, điều đó…

```text
Wide 16:9 landscape cinematic frame. a dropped pistol sliding across wet pavement, beside it a mechanical fist clenching, close-up, dramatic rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Nhưng mỗi món vũ khí gắn vào người là một phần cơ thể bị thay thế. Bạn không chỉ thêm vào. Bạn phải bỏ đi một…

```text
Wide 16:9 landscape cinematic frame. a surgical tray holding a small bandaged natural hand silhouette beside a gleaming mechanical replacement, top-down shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Nhánh 3: giác quan và mạng

Lời: Nhánh thứ ba ít ồn ào hơn: mắt quang học zoom xa, phân tích đối thủ, nhìn trong bóng tối. Tai nghe được những…

```text
Wide 16:9 landscape cinematic frame. an extreme close-up of an artificial eye with a glowing iris ring and faint targeting overlays reflected in it, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Và có cả những người lặn thẳng vào mạng máy tính bằng não: netrunner. Họ cắm dây vào cổ, nằm im, và tâm trí đ…

```text
Wide 16:9 landscape cinematic frame. a figure lying still in a bathtub of ice with cables running from the back of the neck, a vast glowing digital ocean visible above like a dream, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Thành phố còn có một thứ gọi là braindance: những đoạn ghi lại toàn bộ cảm giác của một người, để người khác…

```text
Wide 16:9 landscape cinematic frame. a figure wearing a sleek headset lying on a bed, surrounded by translucent floating memories of another person's life, medium shot, soft violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nghe thì như phim ảnh, nhưng nó cho thấy trong thế giới này, ngay cả cảm xúc cũng có thể được thu âm, mua bán…

```text
Wide 16:9 landscape cinematic frame. a market shelf lined with small glowing memory chips labeled only with emotion icons, close-up, cold neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Lucy, người con gái David gặp, là một netrunner tài năng. Cô mơ được lên Mặt Trăng, nơi xa nhất khỏi thành ph…

```text
Wide 16:9 landscape cinematic frame. a lone figure sitting on a rooftop at night looking at a huge bright moon above the neon skyline, back view, soft silver light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Cái giá của nhánh này nằm ngay trong đầu. Bị hệ thống phòng thủ phản công, bộ não của netrunner có thể bị chá…

```text
Wide 16:9 landscape cinematic frame. a cracked visor glowing red with error symbols, sparks flickering near a neck port, extreme close-up, harsh red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Nhánh 4: gần như toàn bộ là máy

Lời: Ở cực đoan nhất là những người đã thay gần hết cơ thể. Kẻ đáng sợ nhất Edgerunners, Adam Smasher, gần như chỉ…

```text
Wide 16:9 landscape cinematic frame. a towering heavily armored cyborg silhouette standing in smoke, glowing red optics, dwarfing the ruined vehicles around it, low-angle wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Mỗi lần hắn xuất hiện, bầu không khí trong phim thay đổi hẳn. Không có nét biểu cảm, không có sự do dự, chỉ c…

```text
Wide 16:9 landscape cinematic frame. a pair of glowing red optics in total darkness, rain streaks reflecting their light, extreme close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Hắn không bị loạn thần máy theo cách mọi người thường thấy. Đây là một chi tiết khiến fan tranh luận nhiều: c…

```text
Wide 16:9 landscape cinematic frame. a single small human heart symbol glowing faintly inside a massive mechanical chest diagram, close-up, cold red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là lý thuyết của người xem, truyện không nói rõ. Nhưng nó gợi ra một câu hỏi rất đáng sợ về…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a sticky note with a question mark stuck on the chest diagram, looking uneasy. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Luật nâng cao: cơ thể đào thải

Lời: Giờ đến phần quan trọng nhất: vì sao chrome lại có cái giá? Lớp đầu tiên là sinh học. Cơ thể coi bộ phận lạ l…

```text
Wide 16:9 landscape cinematic frame. a microscopic view of cells surrounding a small metallic fragment, glowing defensive shapes clustering around it, stylized diagram, amber and cyan. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Bác sĩ chợ đen của David nhiều lần cảnh báo. Mỗi món mới lắp vào là một gánh nặng mới, và liều thuốc cứ thế t…

```text
Wide 16:9 landscape cinematic frame. an old ripperdoc silhouette shaking his head while holding an x-ray image full of implants against a light box, medium shot, green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Kaku để ý thấy phim dùng những chi tiết rất đời thường để kể chuyện này: một vỉ thuốc rỗng, một cái rùng mình…

```text
Wide 16:9 landscape cinematic frame. a single drop of blood falling onto a sink next to an empty blister pack, extreme close-up, cold bathroom light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Để chrome không bị đào thải, người dùng phải uống thuốc ức chế miễn dịch thường xuyên. David cũng phải dùng t…

```text
Wide 16:9 landscape cinematic frame. a small pill organizer box with every compartment filled, beside a glass of water on a cluttered desk, close-up, cold neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhưng thuốc chỉ làm chậm vấn đề, không xóa nó. Mỗi món chrome mới là thêm một cuộc chiến nhỏ bên trong cơ thể.

```text
Wide 16:9 landscape cinematic frame. a tug of war rope between a mechanical hand and a human hand, frayed in the middle, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Luật nâng cao: chi phí nhân tính

Lời: Lớp thứ hai là tâm lý, và nó có nguồn gốc rất thú vị. Thế giới Cyberpunk bắt đầu từ một trò chơi nhập vai trê…

```text
Wide 16:9 landscape cinematic frame. a tabletop scene with dice, character sheets and a small cardboard city map under a warm lamp, top-down shot, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Trong luật của trò chơi, mỗi nhân vật có chỉ số đồng cảm, tức khả năng kết nối cảm xúc với người khác. Chỉ số…

```text
Wide 16:9 landscape cinematic frame. a character sheet with a single highlighted stat bar labeled with a heart icon, being filled with small tally marks, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Mỗi món chrome có một chi phí nhân tính. Lắp càng nhiều, điểm nhân tính càng giảm. Khi điểm về dưới không, nh…

```text
Wide 16:9 landscape cinematic frame. a heart icon bar draining segment by segment as small mechanical part icons are added beside it, diagram style, cyan and red. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Edgerunners lấy bối cảnh cùng thế giới với trò chơi điện tử Cyberpunk 2077, khoảng một năm trước câu chuyện t…

```text
Wide 16:9 landscape cinematic frame. a game controller resting on a desk in front of a monitor showing a neon skyline, close-up, cozy dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kaku rất thích luật này. Nó biến một ý tưởng triết học thành một con số. Và nó nói rằng thứ bị mất không phải…

```text
Wide 16:9 landscape cinematic frame. a hand-drawn chart on parchment with two curves crossing: power rising, empathy falling, amber ink, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Loạn thần máy trông như thế nào

Lời: Trong Edgerunners, loạn thần máy hiện ra dần dần. Đầu tiên là những thoáng ảo giác, những hình ảnh nhiễu sóng…

```text
Wide 16:9 landscape cinematic frame. a figure in a dark room seeing glitching distorted shapes in the corners of the vision, a warped overlay effect, medium shot, magenta and cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Rồi là mất kiểm soát cảm xúc: giận dữ vô cớ, không phân biệt được bạn và thù. Maine, người đội trưởng từng dì…

```text
Wide 16:9 landscape cinematic frame. a large armored figure clutching his head in a burning street, allies backing away in fear, wide shot, red emergency light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Điều trớ trêu là chính những người săn loạn thần máy cũng mang rất nhiều chrome. Thành phố chống lại hậu quả…

```text
Wide 16:9 landscape cinematic frame. an armored enforcer silhouette with glowing implants standing over a fallen cyborg, both looking nearly identical, medium shot, harsh searchlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ở giai đoạn cuối, người đó trở thành mối nguy cho tất cả. Thành phố có một đơn vị cảnh sát đặc biệt chuyên xử…

```text
Wide 16:9 landscape cinematic frame. a squad of heavily armored silhouettes with a flying transport vehicle landing behind them in a smoky street, low-angle wide shot, harsh searchlights. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Với Maine, những dấu hiệu đầu tiên xuất hiện từ khá sớm, và người xung quanh nhìn thấy. Nhưng trong một nghề…

```text
Wide 16:9 landscape cinematic frame. a crew of mercenaries in a van exchanging worried glances while their leader stares blankly out the window, medium shot, dim interior light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Điều đáng sợ nhất: nạn nhân không phải người xấu. Họ chỉ là người đã thay quá nhiều thứ để sống sót, và không…

```text
Wide 16:9 landscape cinematic frame. a broken mirror reflecting a face half human half machine, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Ngoại lệ: cơ thể đặc biệt

Lời: Trong phim, David được bác sĩ nói là có sức chịu chrome cao bất thường. Cậu gắn được những thứ mà người khác…

```text
Wide 16:9 landscape cinematic frame. a teenager standing calmly while multiple implants glow along his arms and spine, doctors watching in disbelief behind glass, medium shot, clinical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Và sức chịu cao còn tạo ra một cái bẫy: chính vì cậu làm được, người khác bắt đầu trông đợi cậu làm nhiều hơn…

```text
Wide 16:9 landscape cinematic frame. a teenager standing in front of a wall of glowing job offers and requests, each one heavier than the last, medium shot, neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nhưng cao bất thường không có nghĩa là vô hạn. Luật vẫn là luật: mỗi lần thêm chrome, cậu tiến gần hơn tới gi…

```text
Wide 16:9 landscape cinematic frame. a tall glass slowly filling with glowing liquid, the waterline approaching the brim, extreme close-up, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kaku sẽ không kể chi tiết cái kết của mùa một cho những ai chưa xem. Chỉ nói rằng luật chi phí nhân tính khôn…

```text
Wide 16:9 landscape cinematic frame. a door slowly closing on a neon-lit room, a faint moon visible through a window inside, medium shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Ba hiểu lầm thường gặp

Lời: Hiểu lầm thứ nhất: càng nhiều chrome càng mạnh. Sai. Mỗi người có một giới hạn chịu đựng khác nhau, và vượt g…

```text
Wide 16:9 landscape cinematic frame. a scale with stacked mechanical parts tipping over dangerously, a red warning glow, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Cách phim thể hiện rất rõ: khi nhân vật bị loạn thần, chrome của họ thường còn chạy mạnh hơn bao giờ hết. Cái…

```text
Wide 16:9 landscape cinematic frame. a mechanical arm glowing at full power while the person attached to it looks lost and frightened, close-up, split warm and cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Hiểu lầm thứ hai: loạn thần máy là do máy bị hỏng. Không phải. Chrome có thể hoạt động hoàn hảo, thứ bị hỏng…

```text
Wide 16:9 landscape cinematic frame. a perfectly polished working mechanical arm next to a cracked glass sculpture of a human head, still life composition, cold light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Nếu có một liều thuốc chữa thật sự, Night City đã không cần tới một đội cảnh sát chuyên đi săn người loạn thầ…

```text
Wide 16:9 landscape cinematic frame. a lonely pharmacy counter with a closed sign under heavy rain, an armored transport flying overhead, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hiểu lầm thứ ba: có thuốc là chữa được. Thuốc ức chế chỉ giúp cơ thể không đào thải và làm chậm triệu chứng.…

```text
Wide 16:9 landscape cinematic frame. an empty pill bottle lying on its side in a puddle reflecting neon signs, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Thật và hư cấu

Lời: Giờ tới phần Kaku hứa từ đầu. Ngoài đời thật, con người đã gắn máy vào cơ thể từ lâu: máy tạo nhịp tim, ốc ta…

```text
Wide 16:9 landscape cinematic frame. a modern prosthetic hand, a small pacemaker and a cochlear implant displayed on a clean white table, still life, soft daylight. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Tay giả hiện đại còn bắt đầu có cảm giác: cảm biến ở đầu ngón gửi tín hiệu ngược lại cho dây thần kinh, để ng…

```text
Wide 16:9 landscape cinematic frame. a prosthetic fingertip gently holding a ripe strawberry without crushing it, thin sensor lines glowing faintly, extreme close-up, soft daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: những tiến bộ này giúp con người lấy lại những gì đã mất, chứ không phải để thành siêu nhân. Và…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny white coat, holding a clipboard beside a clean modern clinic sign. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Các nhóm nghiên cứu cũng đang thử nghiệm giao diện não máy tính, giúp người bị liệt điều khiển con trỏ máy tí…

```text
Wide 16:9 landscape cinematic frame. a person in a wheelchair looking at a screen with a cursor moving, a thin sensor cap on the head, medium shot, calm lab light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Phản ứng của cơ thể với vật lạ và thuốc ức chế miễn dịch sau ghép tạng cũng là chuyện có thật trong y học.

```text
Wide 16:9 landscape cinematic frame. a stylized medical diagram of a body outline with a highlighted transplanted organ and small shield icons, clean infographic style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Còn loạn thần máy thì hoàn toàn là hư cấu. Không có nghiên cứu nào cho thấy gắn thiết bị y tế làm người ta mấ…

```text
Wide 16:9 landscape cinematic frame. a large stamp reading fiction pressed onto a comic-style illustration of a glitching figure, close-up, playful lighting. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Góc nhìn của Kaku: vì sao phải thay mình để sống

Lời: Kaku nghĩ luật chi phí nhân tính thật ra là một câu chuyện về áp lực. Ở Night City, nếu bạn không nâng cấp, b…

```text
Wide 16:9 landscape cinematic frame. a person running on an endless treadmill made of city streets, other runners with glowing implants overtaking them, wide shot, neon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Mẹ David từng mơ con mình vào học ở học viện của tập đoàn lớn nhất thành phố và leo lên tới đỉnh tòa tháp. Cậ…

```text
Wide 16:9 landscape cinematic frame. a mother and a young boy looking up at a gigantic corporate tower from a crowded street, back view, the tower's lights reflecting in their eyes, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: David không gắn chrome vì ham sức mạnh. Cậu gắn vì muốn thực hiện giấc mơ của mẹ, muốn bảo vệ người mình thươ…

```text
Wide 16:9 landscape cinematic frame. a teenager looking at an old photograph of his mother under a flickering light, a new implant glowing on his arm, close-up, warm and cold contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Lucy muốn lên Mặt Trăng để thoát khỏi thành phố. David muốn leo lên tòa tháp để chinh phục thành phố. Hai giấ…

```text
Wide 16:9 landscape cinematic frame. two arrows drawn on a map, one pointing up toward a moon, the other pointing up a tall tower, diverging, parchment and neon hybrid style. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và đó là bi kịch: những lý do rất con người lại dẫn cậu tới chỗ mất dần phần con người.

```text
Wide 16:9 landscape cinematic frame. a silhouette walking toward a bright moon while leaving mechanical footprints behind, wide shot, bittersweet silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Mùa hai có một nhân vật chính từng là huyền thoại nhưng giờ phải sống không có chrome. Kaku rất tò mò: sau mù…

```text
Wide 16:9 landscape cinematic frame. an aging mercenary silhouette with bare human arms sitting in a quiet diner at night, a box of old implants on the seat beside him, medium shot, warm neon. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Sơ đồ tổng kết

Lời: Kaku gom lại thành một sơ đồ. Ở trên là bốn nhánh chrome: phản xạ, vũ khí, giác quan và mạng, và thay gần như…

```text
Wide 16:9 landscape cinematic frame. a clean diagram with four branches spreading from a human silhouette: a speed icon, a blade icon, an eye icon and a full robot icon, parchment and neon style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và bên cạnh là một mũi tên nhỏ chỉ về phía áp lực của thành phố: thứ khiến người ta cứ phải gắn thêm dù đã bi…

```text
Wide 16:9 landscape cinematic frame. a small arrow labeled with a city skyline icon pushing against the diagram from the side, parchment style, amber ink. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Ở giữa là hai lớp cái giá: cơ thể đào thải, phải dùng thuốc; và chi phí nhân tính, làm giảm khả năng đồng cảm.

```text
Wide 16:9 landscape cinematic frame. the same diagram with two warning layers drawn beneath the branches: a shield icon and a fading heart icon, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Ở dưới cùng là điểm cuối nếu vượt giới hạn: loạn thần máy. Và một dòng nhỏ Kaku viết thêm: mỗi người có giới…

```text
Wide 16:9 landscape cinematic frame. the bottom of the diagram with a red warning symbol and a small handwritten note beside it, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu sống ở Night City, bạn sẽ gắn món chrome nào, và dừng lại ở đâu? Kaku đoán nhiều bạn sẽ chọn đôi mắt nhìn…

```text
Wide 16:9 landscape cinematic frame. a shop catalog page with several implant options and empty checkboxes, a pen resting on it, top-down shot, neon glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Kết

Lời: Mùa hai có mười tập. Khi xem xong, hãy thử đối chiếu với sơ đồ hôm nay xem luật chơi có thay đổi gì không. Nh…

```text
Wide 16:9 landscape cinematic frame. a streaming remote lying on a couch next to the notebook diagram, cozy neon-lit apartment, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Edgerunners dùng một hệ thống nghe rất khoa học viễn tưởng để kể một câu chuyện rất cũ: cái giá của việc cố t…

```text
Wide 16:9 landscape cinematic frame. a lone figure on a rooftop reaching toward the moon while the neon city glows below, wide shot, silver moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku đi từ tương lai về quá khứ xa xưa: truyền thuyết cậu bé quả đào Momotaro, và vì sao Tou…

```text
Wide 16:9 landscape cinematic frame. an ancient Japanese storybook opened to an illustration of a giant peach floating down a river, close-up, warm parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video vừa giải thích vừa tách bạch thật và hư cấu, hãy đăng ký kênh để đi cùng Kaku. Kaku…

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off its tiny visor, closing the notebook and waving goodbye under a neon sign. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 88 giây · cảnh s01–s07 · 1139 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Cyberpunk: Edgerunners mùa một. Mùa hai lên Netflix ngày 20 tháng 10 năm 2026, nên Kaku chỉ nhắc tiền đề, không kể nội dung.

<short pause> Hãy tưởng tượng một thành phố nơi bạn có thể mua một cánh tay mạnh như máy xúc, một đôi mắt nhìn xuyên đêm, hay một con chip làm thời gian quanh bạn như chậm lại.

<short pause> Chỉ cần đủ tiền. Và chỉ cần bạn chấp nhận một cái giá không ghi trên hóa đơn: một phần con người của bạn.

<short pause> Đó là Night City trong Cyberpunk: Edgerunners, nơi người ta gọi những bộ phận máy móc gắn vào cơ thể là chrome. Và khi gắn quá nhiều, người ta có thể rơi vào một trạng thái đáng sợ gọi là loạn thần máy.

<short pause> Night City là thành phố của các tập đoàn khổng lồ và những băng đảng đường phố. Người giàu sống trên những tòa tháp chọc trời, người nghèo sống bên dưới, và ai cũng tìm cách để không bị giẫm lên.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình giải thích hệ thống cấy ghép trong Edgerunners hoạt động thế nào: luật nền, các loại chrome, cái giá, và vì sao loạn thần máy xảy ra.

<short pause> Và cuối video, Kaku sẽ tách bạch phần nào có thật ngoài đời, phần nào là hư cấu. Vì chuyện gắn máy vào người nghe thì xa, nhưng không xa như bạn nghĩ.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Cyberpunk: Edgerunners mùa một. Mùa hai lên Netflix ngày 20 tháng 10 năm 2026, nên Kaku chỉ nhắc tiền đề, không kể nội dung.

[pause] Hãy tưởng tượng một thành phố nơi bạn có thể mua một cánh tay mạnh như máy xúc, một đôi mắt nhìn xuyên đêm, hay một con chip làm thời gian quanh bạn như chậm lại.

[pause] Chỉ cần đủ tiền. Và chỉ cần bạn chấp nhận một cái giá không ghi trên hóa đơn: một phần con người của bạn.

[pause] Đó là Night City trong Cyberpunk: Edgerunners, nơi người ta gọi những bộ phận máy móc gắn vào cơ thể là chrome. Và khi gắn quá nhiều, người ta có thể rơi vào một trạng thái đáng sợ gọi là loạn thần máy.

[pause] Night City là thành phố của các tập đoàn khổng lồ và những băng đảng đường phố. Người giàu sống trên những tòa tháp chọc trời, người nghèo sống bên dưới, và ai cũng tìm cách để không bị giẫm lên.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình giải thích hệ thống cấy ghép trong Edgerunners hoạt động thế nào: luật nền, các loại chrome, cái giá, và vì sao loạn thần máy xảy ra.

[pause] Và cuối video, Kaku sẽ tách bạch phần nào có thật ngoài đời, phần nào là hư cấu. Vì chuyện gắn máy vào người nghe thì xa, nhưng không xa như bạn nghĩ.
```

### c02 · Luật nền: chrome là gì / Nhánh 1: phản xạ và tốc độ

Khoảng 143 giây · cảnh s08–s20 · 1854 ký tự

**Gemini**

```text
Trong Edgerunners, chrome là mọi bộ phận nhân tạo gắn vào cơ thể: tay chân, mắt, da, hệ thần kinh, cả những con chip cắm thẳng vào não.

<short pause> Người lắp chrome gọi là bác sĩ chợ đen, hay ripperdoc. Có người làm trong phòng khám sạch sẽ, có người làm trong một góc hầm chật chội với dụng cụ cũ.

<short pause> Chrome còn là thời trang. Có người gắn hình xăm phát sáng dưới da, có người thay màu mắt theo tâm trạng. Trong thành phố này, cơ thể là thứ để nâng cấp giống như chiếc điện thoại.

<short pause> Và cũng giống điện thoại, đồ tốt thì đắt, đồ rẻ thì dễ hỏng, còn đồ lậu thì không ai bảo hành.

<short pause> Ở Night City, chrome không phải xa xỉ. Nó là công cụ để sống. Người bảo vệ cần tay khỏe, người lái xe cần mắt tốt, người đánh thuê cần phản xạ nhanh hơn đối thủ.

<short pause> Luật nền thứ nhất vì vậy rất đơn giản: chrome cho bạn thêm năng lực, và năng lực càng mạnh thì càng đắt, về cả tiền bạc lẫn cơ thể.

<short pause> <laugh> Kaku đã thử nghĩ xem mình nên lắp gì. Kết luận: cặp kính của Kaku đã là chrome duy nhất Kaku cần. Và nó cũng hay bị lệch.

<short pause> Nhánh chrome nổi tiếng nhất trong Edgerunners là bộ tăng tốc phản xạ, trong phim gọi là Sandevistan. Nó gắn dọc sống lưng.

<short pause> Khi kích hoạt, người dùng di chuyển và phản ứng nhanh tới mức cả thế giới xung quanh như đứng im. Viên đạn lơ lửng, giọt mưa treo giữa không trung.

<short pause> Lần đầu dùng nó, David đang ở trường, trước mặt những kẻ bắt nạt từng coi thường cậu. Trong vài giây, cậu làm được điều mà cả lớp không kịp nhìn thấy.

<short pause> Kaku phải nói thật: nếu Kaku có Sandevistan, Kaku chỉ dùng để kịp chuyến xe buýt buổi sáng. Và chắc vẫn trễ, vì còn bận chọn kính.

<short pause> Nhân vật chính David có được một bộ tăng tốc loại quân sự, loại dành cho binh lính chứ không dành cho một cậu học sinh. Đó là điểm khởi đầu của mọi chuyện.

<short pause> Cái giá của nhánh này là cơ thể và bộ não phải chịu tải khổng lồ. Dùng lâu sẽ đau, chảy máu mũi, choáng váng. Cơ thể người không được thiết kế để sống nhanh gấp nhiều lần như vậy.
```

**ElevenLabs**

```text
Trong Edgerunners, chrome là mọi bộ phận nhân tạo gắn vào cơ thể: tay chân, mắt, da, hệ thần kinh, cả những con chip cắm thẳng vào não.

[pause] Người lắp chrome gọi là bác sĩ chợ đen, hay ripperdoc. Có người làm trong phòng khám sạch sẽ, có người làm trong một góc hầm chật chội với dụng cụ cũ.

[pause] Chrome còn là thời trang. Có người gắn hình xăm phát sáng dưới da, có người thay màu mắt theo tâm trạng. Trong thành phố này, cơ thể là thứ để nâng cấp giống như chiếc điện thoại.

[pause] Và cũng giống điện thoại, đồ tốt thì đắt, đồ rẻ thì dễ hỏng, còn đồ lậu thì không ai bảo hành.

[pause] Ở Night City, chrome không phải xa xỉ. Nó là công cụ để sống. Người bảo vệ cần tay khỏe, người lái xe cần mắt tốt, người đánh thuê cần phản xạ nhanh hơn đối thủ.

[pause] Luật nền thứ nhất vì vậy rất đơn giản: chrome cho bạn thêm năng lực, và năng lực càng mạnh thì càng đắt, về cả tiền bạc lẫn cơ thể.

[pause] [chuckles] Kaku đã thử nghĩ xem mình nên lắp gì. Kết luận: cặp kính của Kaku đã là chrome duy nhất Kaku cần. Và nó cũng hay bị lệch.

[pause] Nhánh chrome nổi tiếng nhất trong Edgerunners là bộ tăng tốc phản xạ, trong phim gọi là Sandevistan. Nó gắn dọc sống lưng.

[pause] Khi kích hoạt, người dùng di chuyển và phản ứng nhanh tới mức cả thế giới xung quanh như đứng im. Viên đạn lơ lửng, giọt mưa treo giữa không trung.

[pause] Lần đầu dùng nó, David đang ở trường, trước mặt những kẻ bắt nạt từng coi thường cậu. Trong vài giây, cậu làm được điều mà cả lớp không kịp nhìn thấy.

[pause] Kaku phải nói thật: nếu Kaku có Sandevistan, Kaku chỉ dùng để kịp chuyến xe buýt buổi sáng. Và chắc vẫn trễ, vì còn bận chọn kính.

[pause] Nhân vật chính David có được một bộ tăng tốc loại quân sự, loại dành cho binh lính chứ không dành cho một cậu học sinh. Đó là điểm khởi đầu của mọi chuyện.

[pause] Cái giá của nhánh này là cơ thể và bộ não phải chịu tải khổng lồ. Dùng lâu sẽ đau, chảy máu mũi, choáng váng. Cơ thể người không được thiết kế để sống nhanh gấp nhiều lần như vậy.
```

### c03 · Nhánh 2: vũ khí trong cơ thể / Nhánh 3: giác quan và mạng

Khoảng 113 giây · cảnh s21–s30 · 1469 ký tự

**Gemini**

```text
Nhánh thứ hai là biến chính cơ thể thành vũ khí. Có lưỡi dao gập giấu trong cẳng tay, có cánh tay cơ khí đấm vỡ cả khối bê tông, có sợi dây siêu mảnh cắt được kim loại.

<short pause> Maine, thủ lĩnh nhóm đánh thuê mà David gia nhập, có đôi tay cơ khí to và khỏe tới mức lật được cả chiếc xe. Anh là hình mẫu của người đã sống bằng chrome rất nhiều năm.

<short pause> Người cầm súng còn có thể bị tước vũ khí. Người mà cánh tay chính là vũ khí thì không. Ở Night City, điều đó có thể là ranh giới giữa sống và chết.

<short pause> Nhưng mỗi món vũ khí gắn vào người là một phần cơ thể bị thay thế. Bạn không chỉ thêm vào. Bạn phải bỏ đi một thứ gì đó vốn là của mình.

<short pause> Nhánh thứ ba ít ồn ào hơn: mắt quang học zoom xa, phân tích đối thủ, nhìn trong bóng tối. Tai nghe được những âm thanh người thường không nghe.

<short pause> Và có cả những người lặn thẳng vào mạng máy tính bằng não: netrunner. Họ cắm dây vào cổ, nằm im, và tâm trí đi vào mạng để đột nhập hệ thống.

<short pause> Thành phố còn có một thứ gọi là braindance: những đoạn ghi lại toàn bộ cảm giác của một người, để người khác cắm vào và sống lại trải nghiệm đó như thật.

<short pause> Nghe thì như phim ảnh, nhưng nó cho thấy trong thế giới này, ngay cả cảm xúc cũng có thể được thu âm, mua bán và lạm dụng.

<short pause> Lucy, người con gái David gặp, là một netrunner tài năng. Cô mơ được lên Mặt Trăng, nơi xa nhất khỏi thành phố này.

<short pause> Cái giá của nhánh này nằm ngay trong đầu. Bị hệ thống phòng thủ phản công, bộ não của netrunner có thể bị cháy theo đúng nghĩa đen. Mạng trong Edgerunners không phải trò chơi.
```

**ElevenLabs**

```text
Nhánh thứ hai là biến chính cơ thể thành vũ khí. Có lưỡi dao gập giấu trong cẳng tay, có cánh tay cơ khí đấm vỡ cả khối bê tông, có sợi dây siêu mảnh cắt được kim loại.

[pause] Maine, thủ lĩnh nhóm đánh thuê mà David gia nhập, có đôi tay cơ khí to và khỏe tới mức lật được cả chiếc xe. Anh là hình mẫu của người đã sống bằng chrome rất nhiều năm.

[pause] Người cầm súng còn có thể bị tước vũ khí. Người mà cánh tay chính là vũ khí thì không. Ở Night City, điều đó có thể là ranh giới giữa sống và chết.

[pause] Nhưng mỗi món vũ khí gắn vào người là một phần cơ thể bị thay thế. Bạn không chỉ thêm vào. Bạn phải bỏ đi một thứ gì đó vốn là của mình.

[pause] Nhánh thứ ba ít ồn ào hơn: mắt quang học zoom xa, phân tích đối thủ, nhìn trong bóng tối. Tai nghe được những âm thanh người thường không nghe.

[pause] Và có cả những người lặn thẳng vào mạng máy tính bằng não: netrunner. Họ cắm dây vào cổ, nằm im, và tâm trí đi vào mạng để đột nhập hệ thống.

[pause] Thành phố còn có một thứ gọi là braindance: những đoạn ghi lại toàn bộ cảm giác của một người, để người khác cắm vào và sống lại trải nghiệm đó như thật.

[pause] Nghe thì như phim ảnh, nhưng nó cho thấy trong thế giới này, ngay cả cảm xúc cũng có thể được thu âm, mua bán và lạm dụng.

[pause] Lucy, người con gái David gặp, là một netrunner tài năng. Cô mơ được lên Mặt Trăng, nơi xa nhất khỏi thành phố này.

[pause] Cái giá của nhánh này nằm ngay trong đầu. Bị hệ thống phòng thủ phản công, bộ não của netrunner có thể bị cháy theo đúng nghĩa đen. Mạng trong Edgerunners không phải trò chơi.
```

### c04 · Nhánh 4: gần như toàn bộ là máy / Luật nâng cao: cơ thể đào thải

Khoảng 101 giây · cảnh s31–s39 · 1317 ký tự

**Gemini**

```text
Ở cực đoan nhất là những người đã thay gần hết cơ thể. Kẻ đáng sợ nhất Edgerunners, Adam Smasher, gần như chỉ còn là một cỗ máy chiến tranh với chút ít phần người sót lại.

<short pause> Mỗi lần hắn xuất hiện, bầu không khí trong phim thay đổi hẳn. Không có nét biểu cảm, không có sự do dự, chỉ có hiệu quả.

<short pause> Hắn không bị loạn thần máy theo cách mọi người thường thấy. Đây là một chi tiết khiến fan tranh luận nhiều: có phải vì hắn đã không còn đủ phần người để mà mất nữa?

<short pause> <laugh> Kaku ghi chú: đây là lý thuyết của người xem, truyện không nói rõ. <short pause> Nhưng nó gợi ra một câu hỏi rất đáng sợ về luật chơi của thế giới này.

<short pause> Giờ đến phần quan trọng nhất: vì sao chrome lại có cái giá? Lớp đầu tiên là sinh học. Cơ thể coi bộ phận lạ là kẻ xâm nhập và tìm cách chống lại nó.

<short pause> Bác sĩ chợ đen của David nhiều lần cảnh báo. Mỗi món mới lắp vào là một gánh nặng mới, và liều thuốc cứ thế tăng lên.

<short pause> Kaku để ý thấy phim dùng những chi tiết rất đời thường để kể chuyện này: một vỉ thuốc rỗng, một cái rùng mình, một lần chảy máu mũi. Không cần giải thích dài dòng, người xem vẫn thấy cơ thể đang kêu cứu.

<short pause> Để chrome không bị đào thải, người dùng phải uống thuốc ức chế miễn dịch thường xuyên. David cũng phải dùng thuốc như vậy, và liều ngày càng nhiều.

<short pause> Nhưng thuốc chỉ làm chậm vấn đề, không xóa nó. Mỗi món chrome mới là thêm một cuộc chiến nhỏ bên trong cơ thể.
```

**ElevenLabs**

```text
Ở cực đoan nhất là những người đã thay gần hết cơ thể. Kẻ đáng sợ nhất Edgerunners, Adam Smasher, gần như chỉ còn là một cỗ máy chiến tranh với chút ít phần người sót lại.

[pause] Mỗi lần hắn xuất hiện, bầu không khí trong phim thay đổi hẳn. Không có nét biểu cảm, không có sự do dự, chỉ có hiệu quả.

[pause] Hắn không bị loạn thần máy theo cách mọi người thường thấy. [curious] Đây là một chi tiết khiến fan tranh luận nhiều: có phải vì hắn đã không còn đủ phần người để mà mất nữa?

[pause] [chuckles] Kaku ghi chú: đây là lý thuyết của người xem, truyện không nói rõ. [pause] Nhưng nó gợi ra một câu hỏi rất đáng sợ về luật chơi của thế giới này.

[pause] Giờ đến phần quan trọng nhất: vì sao chrome lại có cái giá? Lớp đầu tiên là sinh học. Cơ thể coi bộ phận lạ là kẻ xâm nhập và tìm cách chống lại nó.

[pause] Bác sĩ chợ đen của David nhiều lần cảnh báo. Mỗi món mới lắp vào là một gánh nặng mới, và liều thuốc cứ thế tăng lên.

[pause] Kaku để ý thấy phim dùng những chi tiết rất đời thường để kể chuyện này: một vỉ thuốc rỗng, một cái rùng mình, một lần chảy máu mũi. Không cần giải thích dài dòng, người xem vẫn thấy cơ thể đang kêu cứu.

[pause] Để chrome không bị đào thải, người dùng phải uống thuốc ức chế miễn dịch thường xuyên. David cũng phải dùng thuốc như vậy, và liều ngày càng nhiều.

[pause] Nhưng thuốc chỉ làm chậm vấn đề, không xóa nó. Mỗi món chrome mới là thêm một cuộc chiến nhỏ bên trong cơ thể.
```

### c05 · Luật nâng cao: chi phí nhân tính / Loạn thần máy trông như thế nào

Khoảng 132 giây · cảnh s40–s50 · 1713 ký tự

**Gemini**

```text
Lớp thứ hai là tâm lý, và nó có nguồn gốc rất thú vị. Thế giới Cyberpunk bắt đầu từ một trò chơi nhập vai trên bàn của tác giả Mike Pondsmith, ra đời từ cuối những năm tám mươi.

<short pause> Trong luật của trò chơi, mỗi nhân vật có chỉ số đồng cảm, tức khả năng kết nối cảm xúc với người khác. Chỉ số này quy ra điểm nhân tính.

<short pause> Mỗi món chrome có một chi phí nhân tính. Lắp càng nhiều, điểm nhân tính càng giảm. Khi điểm về dưới không, nhân vật rơi vào loạn thần máy, và người chơi mất quyền điều khiển nhân vật đó.

<short pause> Edgerunners lấy bối cảnh cùng thế giới với trò chơi điện tử Cyberpunk 2077, khoảng một năm trước câu chuyện trong game. Loạn thần máy cũng là chủ đề của nhiều nhiệm vụ trong game đó.

<short pause> Kaku rất thích luật này. Nó biến một ý tưởng triết học thành một con số. Và nó nói rằng thứ bị mất không phải là sức khỏe, mà là khả năng thấy người khác là người.

<short pause> Trong Edgerunners, loạn thần máy hiện ra dần dần. Đầu tiên là những thoáng ảo giác, những hình ảnh nhiễu sóng, những giọng nói không có thật.

<short pause> Rồi là mất kiểm soát cảm xúc: giận dữ vô cớ, không phân biệt được bạn và thù. Maine, người đội trưởng từng dìu dắt David, là ví dụ đau lòng nhất.

<short pause> Điều trớ trêu là chính những người săn loạn thần máy cũng mang rất nhiều chrome. Thành phố chống lại hậu quả của chrome bằng… thêm chrome.

<short pause> Ở giai đoạn cuối, người đó trở thành mối nguy cho tất cả. Thành phố có một đơn vị cảnh sát đặc biệt chuyên xử lý những người như vậy, gọi là MaxTac.

<short pause> Với Maine, những dấu hiệu đầu tiên xuất hiện từ khá sớm, và người xung quanh nhìn thấy. <short pause> Nhưng trong một nghề mà dừng lại đồng nghĩa với chết đói, ai dám bảo anh dừng?

<short pause> Điều đáng sợ nhất: nạn nhân không phải người xấu. Họ chỉ là người đã thay quá nhiều thứ để sống sót, và không còn nhận ra mình nữa.
```

**ElevenLabs**

```text
Lớp thứ hai là tâm lý, và nó có nguồn gốc rất thú vị. Thế giới Cyberpunk bắt đầu từ một trò chơi nhập vai trên bàn của tác giả Mike Pondsmith, ra đời từ cuối những năm tám mươi.

[pause] Trong luật của trò chơi, mỗi nhân vật có chỉ số đồng cảm, tức khả năng kết nối cảm xúc với người khác. Chỉ số này quy ra điểm nhân tính.

[pause] Mỗi món chrome có một chi phí nhân tính. Lắp càng nhiều, điểm nhân tính càng giảm. Khi điểm về dưới không, nhân vật rơi vào loạn thần máy, và người chơi mất quyền điều khiển nhân vật đó.

[pause] Edgerunners lấy bối cảnh cùng thế giới với trò chơi điện tử Cyberpunk 2077, khoảng một năm trước câu chuyện trong game. Loạn thần máy cũng là chủ đề của nhiều nhiệm vụ trong game đó.

[pause] Kaku rất thích luật này. Nó biến một ý tưởng triết học thành một con số. Và nó nói rằng thứ bị mất không phải là sức khỏe, mà là khả năng thấy người khác là người.

[pause] Trong Edgerunners, loạn thần máy hiện ra dần dần. Đầu tiên là những thoáng ảo giác, những hình ảnh nhiễu sóng, những giọng nói không có thật.

[pause] Rồi là mất kiểm soát cảm xúc: giận dữ vô cớ, không phân biệt được bạn và thù. Maine, người đội trưởng từng dìu dắt David, là ví dụ đau lòng nhất.

[pause] Điều trớ trêu là chính những người săn loạn thần máy cũng mang rất nhiều chrome. Thành phố chống lại hậu quả của chrome bằng… thêm chrome.

[pause] Ở giai đoạn cuối, người đó trở thành mối nguy cho tất cả. Thành phố có một đơn vị cảnh sát đặc biệt chuyên xử lý những người như vậy, gọi là MaxTac.

[pause] Với Maine, những dấu hiệu đầu tiên xuất hiện từ khá sớm, và người xung quanh nhìn thấy. [pause] [curious] Nhưng trong một nghề mà dừng lại đồng nghĩa với chết đói, ai dám bảo anh dừng?

[pause] Điều đáng sợ nhất: nạn nhân không phải người xấu. Họ chỉ là người đã thay quá nhiều thứ để sống sót, và không còn nhận ra mình nữa.
```

### c06 · Ngoại lệ: cơ thể đặc biệt / Ba hiểu lầm thường gặp

Khoảng 96 giây · cảnh s51–s59 · 1247 ký tự

**Gemini**

```text
Trong phim, David được bác sĩ nói là có sức chịu chrome cao bất thường. Cậu gắn được những thứ mà người khác gắn vào đã phát điên.

<short pause> Và sức chịu cao còn tạo ra một cái bẫy: chính vì cậu làm được, người khác bắt đầu trông đợi cậu làm nhiều hơn nữa.

<short pause> Nhưng cao bất thường không có nghĩa là vô hạn. Luật vẫn là luật: mỗi lần thêm chrome, cậu tiến gần hơn tới giới hạn của chính mình.

<short pause> Kaku sẽ không kể chi tiết cái kết của mùa một cho những ai chưa xem. Chỉ nói rằng luật chi phí nhân tính không có ngoại lệ thật sự nào cả.

<short pause> Hiểu lầm thứ nhất: càng nhiều chrome càng mạnh. Sai. Mỗi người có một giới hạn chịu đựng khác nhau, và vượt giới hạn thì sức mạnh trở thành mối nguy.

<short pause> Cách phim thể hiện rất rõ: khi nhân vật bị loạn thần, chrome của họ thường còn chạy mạnh hơn bao giờ hết. Cái hỏng không nằm ở máy.

<short pause> Hiểu lầm thứ hai: loạn thần máy là do máy bị hỏng. Không phải. Chrome có thể hoạt động hoàn hảo, thứ bị hỏng là tâm trí và sự gắn kết của con người.

<short pause> Nếu có một liều thuốc chữa thật sự, Night City đã không cần tới một đội cảnh sát chuyên đi săn người loạn thần. Chính sự tồn tại của đội đó đã là câu trả lời.

<short pause> Hiểu lầm thứ ba: có thuốc là chữa được. Thuốc ức chế chỉ giúp cơ thể không đào thải và làm chậm triệu chứng. Nó không trả lại phần nhân tính đã mất.
```

**ElevenLabs**

```text
Trong phim, David được bác sĩ nói là có sức chịu chrome cao bất thường. Cậu gắn được những thứ mà người khác gắn vào đã phát điên.

[pause] Và sức chịu cao còn tạo ra một cái bẫy: chính vì cậu làm được, người khác bắt đầu trông đợi cậu làm nhiều hơn nữa.

[pause] Nhưng cao bất thường không có nghĩa là vô hạn. Luật vẫn là luật: mỗi lần thêm chrome, cậu tiến gần hơn tới giới hạn của chính mình.

[pause] Kaku sẽ không kể chi tiết cái kết của mùa một cho những ai chưa xem. Chỉ nói rằng luật chi phí nhân tính không có ngoại lệ thật sự nào cả.

[pause] Hiểu lầm thứ nhất: càng nhiều chrome càng mạnh. Sai. Mỗi người có một giới hạn chịu đựng khác nhau, và vượt giới hạn thì sức mạnh trở thành mối nguy.

[pause] Cách phim thể hiện rất rõ: khi nhân vật bị loạn thần, chrome của họ thường còn chạy mạnh hơn bao giờ hết. Cái hỏng không nằm ở máy.

[pause] Hiểu lầm thứ hai: loạn thần máy là do máy bị hỏng. Không phải. Chrome có thể hoạt động hoàn hảo, thứ bị hỏng là tâm trí và sự gắn kết của con người.

[pause] Nếu có một liều thuốc chữa thật sự, Night City đã không cần tới một đội cảnh sát chuyên đi săn người loạn thần. Chính sự tồn tại của đội đó đã là câu trả lời.

[pause] Hiểu lầm thứ ba: có thuốc là chữa được. Thuốc ức chế chỉ giúp cơ thể không đào thải và làm chậm triệu chứng. Nó không trả lại phần nhân tính đã mất.
```

### c07 · Thật và hư cấu / Góc nhìn của Kaku: vì sao phải thay mình để sống

Khoảng 142 giây · cảnh s60–s71 · 1849 ký tự

**Gemini**

```text
Giờ tới phần Kaku hứa từ đầu. Ngoài đời thật, con người đã gắn máy vào cơ thể từ lâu: máy tạo nhịp tim, ốc tai điện tử, tay chân giả điều khiển bằng tín hiệu cơ bắp.

<short pause> Tay giả hiện đại còn bắt đầu có cảm giác: cảm biến ở đầu ngón gửi tín hiệu ngược lại cho dây thần kinh, để người dùng biết mình đang cầm vật mềm hay cứng.

<short pause> <laugh> Kaku ghi chú: những tiến bộ này giúp con người lấy lại những gì đã mất, chứ không phải để thành siêu nhân. Và nó do bác sĩ thật làm, không phải bác sĩ trong hầm tối.

<short pause> Các nhóm nghiên cứu cũng đang thử nghiệm giao diện não máy tính, giúp người bị liệt điều khiển con trỏ máy tính bằng suy nghĩ.

<short pause> Phản ứng của cơ thể với vật lạ và thuốc ức chế miễn dịch sau ghép tạng cũng là chuyện có thật trong y học.

<short pause> Còn loạn thần máy thì hoàn toàn là hư cấu. Không có nghiên cứu nào cho thấy gắn thiết bị y tế làm người ta mất khả năng đồng cảm. Đây là nội dung giải trí, không phải lời khuyên y tế.

<short pause> Kaku nghĩ luật chi phí nhân tính thật ra là một câu chuyện về áp lực. Ở Night City, nếu bạn không nâng cấp, bạn bị bỏ lại. Nếu bạn nâng cấp quá mức, bạn mất chính mình.

<short pause> Mẹ David từng mơ con mình vào học ở học viện của tập đoàn lớn nhất thành phố và leo lên tới đỉnh tòa tháp. Cậu đã đi tới đỉnh tháp theo một cách rất khác với những gì bà mong.

<short pause> David không gắn chrome vì ham sức mạnh. Cậu gắn vì muốn thực hiện giấc mơ của mẹ, muốn bảo vệ người mình thương, muốn trở thành người mà thành phố không thể nghiền nát.

<short pause> Lucy muốn lên Mặt Trăng để thoát khỏi thành phố. David muốn leo lên tòa tháp để chinh phục thành phố. Hai giấc mơ đi ngược hướng nhau, và Kaku nghĩ đó là chỗ phim đau nhất.

<short pause> Và đó là bi kịch: những lý do rất con người lại dẫn cậu tới chỗ mất dần phần con người.

<short pause> Mùa hai có một nhân vật chính từng là huyền thoại nhưng giờ phải sống không có chrome. Kaku rất tò mò: sau mùa một, liệu câu trả lời của bộ phim có phải là quay về với cơ thể thật?
```

**ElevenLabs**

```text
Giờ tới phần Kaku hứa từ đầu. Ngoài đời thật, con người đã gắn máy vào cơ thể từ lâu: máy tạo nhịp tim, ốc tai điện tử, tay chân giả điều khiển bằng tín hiệu cơ bắp.

[pause] Tay giả hiện đại còn bắt đầu có cảm giác: cảm biến ở đầu ngón gửi tín hiệu ngược lại cho dây thần kinh, để người dùng biết mình đang cầm vật mềm hay cứng.

[pause] [chuckles] Kaku ghi chú: những tiến bộ này giúp con người lấy lại những gì đã mất, chứ không phải để thành siêu nhân. Và nó do bác sĩ thật làm, không phải bác sĩ trong hầm tối.

[pause] Các nhóm nghiên cứu cũng đang thử nghiệm giao diện não máy tính, giúp người bị liệt điều khiển con trỏ máy tính bằng suy nghĩ.

[pause] Phản ứng của cơ thể với vật lạ và thuốc ức chế miễn dịch sau ghép tạng cũng là chuyện có thật trong y học.

[pause] Còn loạn thần máy thì hoàn toàn là hư cấu. Không có nghiên cứu nào cho thấy gắn thiết bị y tế làm người ta mất khả năng đồng cảm. Đây là nội dung giải trí, không phải lời khuyên y tế.

[pause] Kaku nghĩ luật chi phí nhân tính thật ra là một câu chuyện về áp lực. Ở Night City, nếu bạn không nâng cấp, bạn bị bỏ lại. Nếu bạn nâng cấp quá mức, bạn mất chính mình.

[pause] Mẹ David từng mơ con mình vào học ở học viện của tập đoàn lớn nhất thành phố và leo lên tới đỉnh tòa tháp. Cậu đã đi tới đỉnh tháp theo một cách rất khác với những gì bà mong.

[pause] David không gắn chrome vì ham sức mạnh. Cậu gắn vì muốn thực hiện giấc mơ của mẹ, muốn bảo vệ người mình thương, muốn trở thành người mà thành phố không thể nghiền nát.

[pause] Lucy muốn lên Mặt Trăng để thoát khỏi thành phố. David muốn leo lên tòa tháp để chinh phục thành phố. Hai giấc mơ đi ngược hướng nhau, và Kaku nghĩ đó là chỗ phim đau nhất.

[pause] Và đó là bi kịch: những lý do rất con người lại dẫn cậu tới chỗ mất dần phần con người.

[pause] Mùa hai có một nhân vật chính từng là huyền thoại nhưng giờ phải sống không có chrome. [curious] Kaku rất tò mò: sau mùa một, liệu câu trả lời của bộ phim có phải là quay về với cơ thể thật?
```

### c08 · Sơ đồ tổng kết / Kết

Khoảng 95 giây · cảnh s72–s80 · 1233 ký tự

**Gemini**

```text
Kaku gom lại thành một sơ đồ. Ở trên là bốn nhánh chrome: phản xạ, vũ khí, giác quan và mạng, và thay gần như toàn thân.

<short pause> Và bên cạnh là một mũi tên nhỏ chỉ về phía áp lực của thành phố: thứ khiến người ta cứ phải gắn thêm dù đã biết cái giá.

<short pause> Ở giữa là hai lớp cái giá: cơ thể đào thải, phải dùng thuốc; và chi phí nhân tính, làm giảm khả năng đồng cảm.

<short pause> Ở dưới cùng là điểm cuối nếu vượt giới hạn: loạn thần máy. Và một dòng nhỏ Kaku viết thêm: mỗi người có giới hạn khác nhau, nhưng ai cũng có giới hạn.

<short pause> Nếu sống ở Night City, bạn sẽ gắn món chrome nào, và dừng lại ở đâu? Kaku đoán nhiều bạn sẽ chọn đôi mắt nhìn xuyên đêm. Viết lựa chọn của bạn vào bình luận nhé.

<short pause> Mùa hai có mười tập. Khi xem xong, hãy thử đối chiếu với sơ đồ hôm nay xem luật chơi có thay đổi gì không. Nhớ đánh dấu spoiler khi bình luận nhé.

<short pause> Edgerunners dùng một hệ thống nghe rất khoa học viễn tưởng để kể một câu chuyện rất cũ: cái giá của việc cố trở thành người khác.

<short pause> Video tiếp theo, Kaku đi từ tương lai về quá khứ xa xưa: truyền thuyết cậu bé quả đào Momotaro, và vì sao Tougen Anki lại biến người anh hùng ấy thành kẻ săn đuổi.

<short pause> <laugh> Nếu bạn thích những video vừa giải thích vừa tách bạch thật và hư cấu, hãy đăng ký kênh để đi cùng Kaku. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Kaku gom lại thành một sơ đồ. Ở trên là bốn nhánh chrome: phản xạ, vũ khí, giác quan và mạng, và thay gần như toàn thân.

[pause] Và bên cạnh là một mũi tên nhỏ chỉ về phía áp lực của thành phố: thứ khiến người ta cứ phải gắn thêm dù đã biết cái giá.

[pause] Ở giữa là hai lớp cái giá: cơ thể đào thải, phải dùng thuốc; và chi phí nhân tính, làm giảm khả năng đồng cảm.

[pause] Ở dưới cùng là điểm cuối nếu vượt giới hạn: loạn thần máy. Và một dòng nhỏ Kaku viết thêm: mỗi người có giới hạn khác nhau, nhưng ai cũng có giới hạn.

[pause] [curious] Nếu sống ở Night City, bạn sẽ gắn món chrome nào, và dừng lại ở đâu? Kaku đoán nhiều bạn sẽ chọn đôi mắt nhìn xuyên đêm. Viết lựa chọn của bạn vào bình luận nhé.

[pause] Mùa hai có mười tập. Khi xem xong, hãy thử đối chiếu với sơ đồ hôm nay xem luật chơi có thay đổi gì không. Nhớ đánh dấu spoiler khi bình luận nhé.

[pause] Edgerunners dùng một hệ thống nghe rất khoa học viễn tưởng để kể một câu chuyện rất cũ: cái giá của việc cố trở thành người khác.

[pause] Video tiếp theo, Kaku đi từ tương lai về quá khứ xa xưa: truyền thuyết cậu bé quả đào Momotaro, và vì sao Tougen Anki lại biến người anh hùng ấy thành kẻ săn đuổi.

[pause] [chuckles] Nếu bạn thích những video vừa giải thích vừa tách bạch thật và hư cấu, hãy đăng ký kênh để đi cùng Kaku. Kaku gấp sổ đây, hẹn gặp lại!
```
