# Bộ prompt · Ba hệ kiếm thuật: Hơi thở vs kiếm Haki vs yêu đao — chấm 5 tiêu chí, hệ nào thắng?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 90 ảnh, 7 đoạn đọc, khoảng 14.9 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói tới cái kết của Kimetsu no Yaiba, arc Wano của One Piece, và các chương giữa…

```text
Wide 16:9 landscape cinematic frame. three sheathed swords lying side by side on a wooden table beside a spoiler warning card, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Ba bộ truyện, ba cách cầm kiếm. Một bên học cách thở. Một bên rèn ý chí. Một bên cầm một thanh kiếm tự nó đã…

```text
Wide 16:9 landscape cinematic frame. three swords floating above a long table, one wreathed in swirling breath-like wind, one coated in glossy black, one with ghostly goldfish shapes, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Kaku không so ai mạnh hơn ai. Kaku so hệ thống: học thế nào, mạnh tới đâu, và phải trả giá bao nhiêu.

```text
Wide 16:9 landscape cinematic frame. a notebook page split into three columns with a small sword doodle at the top of each, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đặt Hơi thở của Kimetsu no Yaiba, kiếm Haki của One Piece, và yêu đa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot in a judge's robe sitting behind a long table with three small swords laid out before it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và nếu bạn vừa xem video nhập môn Kagurabachi của Kaku, đây là lúc thanh kiếm thứ bảy bước vào một trận so tà…

```text
Wide 16:9 landscape cinematic frame. a lone sword on a stand being carried into a grand hall where two other swords already rest, wide shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Kiếm thuật Nhật ngoài đời thật

Lời: Trước khi vào ba hệ hư cấu, Kaku kể một chút về kiếm thuật Nhật ngoài đời thật. Cả ba bộ truyện đều mượn khôn…

```text
Wide 16:9 landscape cinematic frame. a quiet traditional dojo with wooden floors and practice swords on a wall rack, wide shot, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Ở Nhật có những trường phái kiếm thuật cổ, được truyền từ thầy sang trò qua nhiều thế kỷ. Mỗi trường phái có…

```text
Wide 16:9 landscape cinematic frame. an old scroll unrolled on a wooden floor showing simple stick-figure sword stances in ink, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Một ví dụ nổi tiếng là trường phái hai kiếm gắn với kiếm sĩ Miyamoto Musashi ở thế kỷ mười bảy. Cầm hai kiếm…

```text
Wide 16:9 landscape cinematic frame. two wooden practice swords crossed on a stand in front of a faded ink landscape painting, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ngày nay, môn phổ biến nhất là kendo, đánh bằng kiếm tre và mặc giáp bảo hộ. Và trong kendo, hơi thở và tiếng…

```text
Wide 16:9 landscape cinematic frame. a practitioner in protective armor raising a bamboo sword in a bright gymnasium, medium shot, clean daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: đây là giới thiệu văn hóa, không phải hướng dẫn. Muốn học kiếm, hãy tìm một võ đường có thầy dạy đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing politely at the entrance of a small dojo. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Hồ sơ hệ 1: Hơi thở

Lời: Hệ thứ nhất: Hơi thở trong Kimetsu no Yaiba. Kiếm sĩ học cách thở theo một nhịp đặc biệt, gọi là Toàn Tập Tru…

```text
Wide 16:9 landscape cinematic frame. a figure standing in a misty forest breathing out a visible swirl of air, close-up, cool dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Mọi Hơi thở đều bắt nguồn từ một hơi thở đầu tiên: Hơi thở Mặt Trời, do một kiếm sĩ huyền thoại tạo ra từ nhi…

```text
Wide 16:9 landscape cinematic frame. a radiant sun rising behind a lone sword planted in a hilltop, wide shot, brilliant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Từ đó chia ra năm hơi thở chính: Nước, Lửa, Sấm, Gió, Đá. Rồi từ năm nhánh chính lại mọc ra những nhánh nhỏ n…

```text
Wide 16:9 landscape cinematic frame. a tree diagram drawn on parchment with one sun root, five thick branches and many smaller twigs with elemental icons, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Kiếm cũng đặc biệt: kiếm Nichirin rèn từ loại quặng hấp thụ ánh mặt trời, và đổi màu theo người cầm nó lần đầ…

```text
Wide 16:9 landscape cinematic frame. a plain steel blade slowly changing color along its edge as a hand grips the hilt, extreme close-up, glowing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và đỉnh cao của hệ này là Ấn, một dấu hiệu xuất hiện trên cơ thể khi kiếm sĩ vượt giới hạn, giúp sức mạnh tăn…

```text
Wide 16:9 landscape cinematic frame. a faint glowing mark appearing on a figure's forehead in a dark forest, extreme close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Còn có Thường Trung, tức giữ nhịp Toàn Tập Trung cả khi ngủ. Kiếm sĩ giỏi luyện tới mức cơ thể tự thở đúng cá…

```text
Wide 16:9 landscape cinematic frame. a figure sleeping peacefully on a futon with a faint steady swirl of breath rising above them, close-up, soft night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Hơi thở là hệ dân chủ nhất. Không cần sinh ra đặc biệt, chỉ cần luyện đủ khổ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot doing breathing exercises with its wings raised, cheeks puffed. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Hồ sơ hệ 2: kiếm Haki

Lời: Hệ thứ hai: kiếm Haki trong One Piece. Haki là sức mạnh của ý chí, có ba loại: vũ trang, quan sát, và bá vươn…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols on parchment, a shield, an eye and a crown, arranged in a triangle, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Kiếm sĩ phủ Haki vũ trang lên lưỡi kiếm, làm thanh kiếm cứng hơn, sắc hơn, và chém được cả những thứ bình thư…

```text
Wide 16:9 landscape cinematic frame. a katana blade slowly darkening to a glossy black sheen from hilt to tip, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Kiếm trong One Piece cũng có hạng. Có mười hai thanh tối thượng, hai mươi mốt thanh đại danh đao, và năm mươi…

```text
Wide 16:9 landscape cinematic frame. a long ranked display rack of swords with small grade plaques beneath each, some plaques more ornate than others, wide shot, museum light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Ở Wano, có một thanh kiếm hút Haki của người cầm nó. Kiếm sĩ phải kiểm soát được nó, nếu không sẽ bị vắt kiệt…

```text
Wide 16:9 landscape cinematic frame. a sword pulling wisps of dark energy out of a straining arm, dramatic close-up, ominous purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và đỉnh cao của hệ này là phủ Haki bá vương lên lưỡi kiếm. Chỉ những kiếm sĩ mạnh nhất thế giới mới làm được.

```text
Wide 16:9 landscape cinematic frame. a blade crackling with black and red lightning as it clashes against another blade in a storm, dramatic close-up, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Haki quan sát cũng quan trọng với kiếm sĩ: nó giúp cảm nhận đối thủ, nhìn trước đòn đánh, và ở mức cao nhất,…

```text
Wide 16:9 landscape cinematic frame. a blindfolded swordsman calmly parrying a blade in a bamboo grove, dynamic close-up, dappled green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: kiếm Haki là hệ đặt ý chí lên trên hết. Thanh kiếm tốt giúp bạn, nhưng thứ quyết định là người cầm…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a wooden sword with a determined frown. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Hồ sơ hệ 3: yêu đao

Lời: Hệ thứ ba: yêu đao trong Kagurabachi. Sức mạnh nằm trong chính thanh kiếm, do người thợ rèn Rokuhira Kunishig…

```text
Wide 16:9 landscape cinematic frame. a katana resting on a blacksmith's anvil with faint glowing patterns moving under the steel, close-up, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Có sáu thanh yêu đao, những vũ khí đã kết thúc Chiến tranh Seitei. Về sau có thêm thanh thứ bảy, Enten, rèn g…

```text
Wide 16:9 landscape cinematic frame. six katanas on a long rack and a seventh on a separate stand, wide shot, solemn dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Luật quan trọng nhất là hợp đồng trọn đời. Khi một người trở thành chủ của yêu đao, chỉ người đó dùng được kỹ…

```text
Wide 16:9 landscape cinematic frame. a hand placing a palm on a sword's blade as a thin glowing thread binds wrist and hilt together, extreme close-up, mystical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Và cái giá: người ký hợp đồng mất vĩnh viễn thuật riêng của mình. Không có kiếm trong tay, họ gần như không c…

```text
Wide 16:9 landscape cinematic frame. an empty open hand beside an empty sword stand in a dark room, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Một người có thể ký hợp đồng với nhiều yêu đao. Nhưng mỗi thanh kiếm, tại một thời điểm, chỉ nghe lời một chủ…

```text
Wide 16:9 landscape cinematic frame. two swords on a rack with glowing threads leading to a single hand, symbolic close-up, mystical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: yêu đao là hệ ngược với Hơi thở. Không cần luyện nửa đời, nhưng số người được cầm thì đếm trên đầu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot counting on its wing feathers with a surprised look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Ba người thầy

Lời: Có một điểm chung thú vị: cả ba hệ đều được truyền qua một người thầy, và người thầy ấy quyết định rất nhiều…

```text
Wide 16:9 landscape cinematic frame. three pairs of hands, one old and one young in each, resting on three different sword hilts, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Trong Kimetsu, Tanjiro học Hơi thở Nước từ một người thầy đeo mặt nạ trên núi, với những bài tập tưởng như bấ…

```text
Wide 16:9 landscape cinematic frame. a young figure standing before a huge boulder on a misty mountain with a sword in hand, wide shot, cold mist light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Trong One Piece, Zoro dành hai năm học kiếm từ chính kiếm sĩ mạnh nhất thế giới, người từng là mục tiêu mà cậ…

```text
Wide 16:9 landscape cinematic frame. two silhouettes crossing swords in the courtyard of a ruined castle under a grey sky, wide shot, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Còn trong Kagurabachi, người thầy đầu tiên của Chihiro không dạy cậu đánh kiếm, mà dạy cậu rèn kiếm. Hiểu tha…

```text
Wide 16:9 landscape cinematic frame. an older blacksmith guiding a teenager's hands on a hammer over a glowing blade, close-up, warm ember light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ba người thầy phản ánh đúng ba hệ. Hơi thở dạy kỷ luật. Haki dạy bạn đối mặt với người mạnh hơn. Y…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing three tiny hats stacked on its head, looking thoughtful. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Năm tiêu chí

Lời: Năm tiêu chí của Kaku. Một: độ phổ cập, tức bao nhiêu người có thể học được. Hai: sức mạnh đỉnh cao, tức hệ n…

```text
Wide 16:9 landscape cinematic frame. a scorecard on parchment with five rows, the first two labeled with a crowd icon and a mountain peak icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Ba: độ đa dạng, tức có bao nhiêu phong cách khác nhau. Bốn: cái giá, và ở tiêu chí này, cái giá càng nhẹ thì…

```text
Wide 16:9 landscape cinematic frame. the next rows of the scorecard labeled with a branching icon and a scale icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Năm: sợi dây giữa người và kiếm, tức hệ này kể câu chuyện về mối quan hệ giữa kiếm sĩ và thanh kiếm sâu tới đ…

```text
Wide 16:9 landscape cinematic frame. the last row of the scorecard labeled with a hand holding a sword hilt icon, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mỗi tiêu chí từ một tới năm, tổng tối đa hai mươi lăm. Và như mọi bảng điểm của Kaku, đây là đánh giá của Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sharpening a pencil beside a blank scorecard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Tiêu chí 1: độ phổ cập

Lời: Hơi thở: ai cũng có thể học, nếu luyện đủ khổ và có thầy giỏi. Nhiều kiếm sĩ bình thường trong Đội diệt quỷ đ…

```text
Wide 16:9 landscape cinematic frame. a row of ordinary trainees practicing breathing forms together in a mountain dojo yard, wide shot, crisp morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Kiếm Haki: theo truyện, mọi sinh vật đều có tiềm năng Haki, nhưng đánh thức được nó rất khó, và Haki bá vương…

```text
Wide 16:9 landscape cinematic frame. a single figure among a crowd with a faint glow around them, symbolic wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Yêu đao: chỉ có bảy thanh, mỗi thanh một người chủ tại một thời điểm. Một điểm.

```text
Wide 16:9 landscape cinematic frame. seven small sword icons on parchment with seven single stick figures beside them, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Ở điểm này, Hơi thở giống một trường võ, Haki giống một tài năng cần khai mở, còn yêu đao giống một báu vật q…

```text
Wide 16:9 landscape cinematic frame. three small icons on parchment, a dojo gate, a seed sprouting and a treasure chest, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Kaku để ý: hệ phổ cập nhất tạo ra một đội quân. Hệ hiếm nhất tạo ra những con người trở thành mục tiêu săn đu…

```text
Wide 16:9 landscape cinematic frame. a crowd of trainee silhouettes on one side and a lone hunted figure on the other, split composition, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Tiêu chí 2: sức mạnh đỉnh cao

Lời: Hơi thở: ở đỉnh cao, người dùng Hơi thở Mặt Trời có thể đứng ngang, thậm chí áp đảo cả Vua Quỷ. Nhưng đó là t…

```text
Wide 16:9 landscape cinematic frame. a lone swordsman silhouette standing before a looming dark figure under a crimson moon, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Kiếm Haki: ở đỉnh cao, kiếm sĩ mạnh nhất có thể chém đôi những thứ khổng lồ, và đối đầu những kẻ mạnh nhất th…

```text
Wide 16:9 landscape cinematic frame. a single sword slash splitting a massive iceberg in half across a stormy sea, dramatic wide shot, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Yêu đao: sáu thanh kiếm đủ để kết thúc cả một cuộc chiến tranh. Về sức tàn phá, đây là hệ đáng sợ nhất. Năm đ…

```text
Wide 16:9 landscape cinematic frame. an old war painting on a folding screen with six points of blinding light over a battlefield, close-up, aged dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: hai hệ cùng năm điểm, nhưng khác nhau ở chỗ: đỉnh cao của Haki là của một người, còn đỉnh cao của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a small figurine and a small sword side by side on a pedestal, comparing them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Tiêu chí 3: độ đa dạng

Lời: Hơi thở: hàng chục nhánh, mỗi nhánh nhiều thế kiếm, mỗi thế mang hình ảnh riêng, từ sóng nước tới hoa đào, từ…

```text
Wide 16:9 landscape cinematic frame. a fan of sword arcs drawn in different elemental styles, water waves, flames, lightning and crescent moons, parchment illustration style, vivid light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Kiếm Haki: mỗi kiếm sĩ tự tạo phong cách riêng, như một kiếm, hai kiếm, hay ba kiếm cùng lúc. Nhưng Haki bản…

```text
Wide 16:9 landscape cinematic frame. a sword stand holding one, two and three sword arrangements side by side, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Yêu đao: mỗi thanh có một năng lực hoàn toàn khác nhau. Chỉ riêng Enten đã có ba kỹ thuật cá vàng. Nhưng tổng…

```text
Wide 16:9 landscape cinematic frame. seven distinct sword silhouettes each with a different small glowing symbol above it, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kaku để ý: Hơi thở thắng ở tiêu chí này vì nó là một hệ thống mở. Người sau có thể tạo ra nhánh mới từ nhánh…

```text
Wide 16:9 landscape cinematic frame. a tree diagram with a fresh new twig being drawn at the end of a branch, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Tiêu chí 4: cái giá

Lời: Hơi thở: cái giá nặng nhất là Ấn. Theo truyện, những người thức tỉnh Ấn sẽ không sống quá tuổi hai mươi lăm,…

```text
Wide 16:9 landscape cinematic frame. a single candle burning very bright but very short on a wooden table, symbolic close-up, intense warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Kiếm Haki: cái giá là kiệt sức, và với một vài thanh kiếm đặc biệt, bị hút cạn Haki. Nặng, nhưng hồi phục đượ…

```text
Wide 16:9 landscape cinematic frame. an exhausted swordsman sitting against a rock after battle, breathing heavily but alive, medium shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Yêu đao: mất vĩnh viễn thuật riêng, không có kiếm là không có gì, và luôn bị săn đuổi. Còn chưa kể cái giá đạ…

```text
Wide 16:9 landscape cinematic frame. a lone figure clutching a sword while shadows close in from every alley, wide shot, tense cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: hai hệ mạnh bùng nổ nhất đều có cái giá đắt nhất. Chỉ kiếm Haki là cho bạn mạnh lên mà vẫn còn đườ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot balancing a heavy scale with a nervous face. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Tiêu chí 5: người và kiếm

Lời: Hơi thở: thanh kiếm đổi màu theo người cầm, và các thợ rèn gắn bó với kiếm sĩ của mình. Nhưng sức mạnh vẫn nằ…

```text
Wide 16:9 landscape cinematic frame. a swordsmith in a mask handing a newly colored blade to a young swordsman, medium shot, warm workshop light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Kiếm Haki: trong One Piece, kiếm có tính cách, có lời nguyền, có lịch sử. Một kiếm sĩ có thể mang theo lời hứ…

```text
Wide 16:9 landscape cinematic frame. a white-hilted katana resting on a grave marker under cherry blossoms, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Yêu đao: hợp đồng trọn đời nghĩa là người và kiếm gắn với nhau tới chết. Và với Chihiro, thanh kiếm còn là di…

```text
Wide 16:9 landscape cinematic frame. a sword and an old blacksmith's hammer resting side by side on a workbench, extreme close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ở tiêu chí này, hai hệ có thanh kiếm biết nói chuyện, theo nghĩa bóng, đều đạt điểm tối đa.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny sword up to its ear as if listening to it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Bảng điểm cuối cùng

Lời: Bảng điểm cuối cùng. Hơi thở: bốn, bốn, năm, hai, bốn. Tổng mười chín điểm.

```text
Wide 16:9 landscape cinematic frame. a scoreboard on parchment with the first column filled with numbers and nineteen circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Kiếm Haki: ba, năm, bốn, bốn, năm. Tổng hai mươi mốt điểm.

```text
Wide 16:9 landscape cinematic frame. the second column of the scoreboard filled with twenty-one circled in gold, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Yêu đao: một, năm, bốn, hai, năm. Tổng mười bảy điểm.

```text
Wide 16:9 landscape cinematic frame. the third column of the scoreboard filled with seventeen circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Khoảng cách giữa ba hệ không lớn: chỉ bốn điểm từ hạng nhất tới hạng ba. Chỉ cần đổi một tiêu chí, thứ hạng c…

```text
Wide 16:9 landscape cinematic frame. three bars on a chart with very similar heights, a finger poised to move one, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Người thắng theo bảng của Kaku: kiếm Haki của One Piece, với hai mươi mốt điểm. Không phải vì nó mạnh nhất ở…

```text
Wide 16:9 landscape cinematic frame. a small gold ribbon pinned onto a black-coated sword on a stand, close-up, warm triumphant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Điểm yếu chí mạng của từng hệ

Lời: Mỗi hệ đều có một điểm yếu chí mạng. Hơi thở dựa vào phổi và thể lực. Khi kiếm sĩ bị thương nặng hay kiệt sức…

```text
Wide 16:9 landscape cinematic frame. a figure kneeling with a hand on their chest in a dark forest as their visible breath falters, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kiếm Haki dựa vào ý chí. Khi Haki cạn, kiếm sĩ trở lại thành người thường cầm một thanh kiếm tốt.

```text
Wide 16:9 landscape cinematic frame. a blade whose black coating flakes away like ash, extreme close-up, fading dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Yêu đao dựa vào chính thanh kiếm. Mất kiếm, người ký hợp đồng mất gần như tất cả, vì thuật riêng của họ đã kh…

```text
Wide 16:9 landscape cinematic frame. a sword being knocked from a hand and spinning away through the air in slow motion, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nói cách khác: muốn thắng người dùng Hơi thở, hãy kéo dài trận đấu. Muốn thắng người dùng Haki, hãy làm họ ng…

```text
Wide 16:9 landscape cinematic frame. a three-column strategy note on parchment with an hourglass, a cracked heart and an open grabbing hand, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: chính điểm yếu làm các trận đấu trong ba bộ truyện hay. Nhân vật mạnh nhất cũng phải chiến đấu qua…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a small crack on a shield with a knowing nod. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Nếu đổi trọng số thì sao?

Lời: Nhưng bảng điểm phụ thuộc vào thứ bạn coi trọng. Nếu chỉ tính sức mạnh đỉnh cao, kiếm Haki và yêu đao hòa nha…

```text
Wide 16:9 landscape cinematic frame. a balance scale perfectly level with a black sword on one side and a goldfish-glow sword on the other, symbolic close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu bạn coi trọng việc ai cũng học được, Hơi thở thắng xa. Đó là hệ của những người bình thường muốn bảo vệ n…

```text
Wide 16:9 landscape cinematic frame. a crowd of ordinary silhouettes holding practice swords together at sunrise, wide shot, hopeful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và nếu bạn coi trọng câu chuyện giữa người và kiếm, yêu đao đứng ngang kiếm Haki. Mỗi hệ đều thắng ở một câu…

```text
Wide 16:9 landscape cinematic frame. three swords on a table each lit by its own separate spotlight, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Trận giả tưởng: ba kiếm sĩ trên cùng một sân

Lời: Giờ là phần giả tưởng vui. Tưởng tượng ba kiếm sĩ bình thường, mỗi người đại diện cho một hệ, gặp nhau trên c…

```text
Wide 16:9 landscape cinematic frame. three faceless swordsman silhouettes standing at three points of a triangle on an empty field at dusk, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Người dùng Hơi thở có tốc độ và sự bền bỉ. Anh ta sẽ cố kéo trận đấu dài ra, dùng các thế kiếm liên hoàn.

```text
Wide 16:9 landscape cinematic frame. a swordsman silhouette dashing in a blur trailing water-like arcs, dynamic wide shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Người dùng Haki có Haki quan sát. Anh ta nhìn thấy trước đòn đánh, nên tốc độ của Hơi thở bớt đáng sợ.

```text
Wide 16:9 landscape cinematic frame. a calm swordsman silhouette with eyes closed sidestepping a blurred slash, dynamic close-up, focused light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Còn người cầm yêu đao có một năng lực mà hai người kia chưa từng thấy. Trận đầu tiên, yếu tố bất ngờ có thể q…

```text
Wide 16:9 landscape cinematic frame. a sword releasing an unexpected burst of ghostly shapes toward two surprised silhouettes, dramatic wide shot, eerie glowing light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Kết quả giả tưởng của Kaku: như oẳn tù tì. Haki khắc Hơi thở, yêu đao khắc Haki ở lần gặp đầu, và Hơi thở khắ…

```text
Wide 16:9 landscape cinematic frame. a rock paper scissors style triangle diagram with three sword icons and arrows between them, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhắc: đây chỉ là giả tưởng, không có trong truyện nào. Bạn nghĩ vòng tròn ấy nên xoay theo chiều nào?

```text
Wide 16:9 landscape cinematic frame. the owl mascot spinning a small paper wheel with three sword icons on it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Góc nhìn của Kaku · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ ba hệ kiếm thuật là ba câu trả lời cho một câu hỏi: sức mạnh đến từ đâu?

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a big question mark in the center of a page with three arrows pointing to it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Kimetsu nói: sức mạnh đến từ cơ thể và sự kiên trì. One Piece nói: sức mạnh đến từ ý chí. Kagurabachi nói: sứ…

```text
Wide 16:9 landscape cinematic frame. three small pedestals holding a lung diagram, a flame and a blacksmith's hammer, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Ba câu trả lời ấy không loại trừ nhau. Một kiếm sĩ giỏi có lẽ cần cả ba: cơ thể được rèn luyện, một ý chí vữn…

```text
Wide 16:9 landscape cinematic frame. three intertwined ribbons tied around a single sword hilt, extreme close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Và có lẽ vì vậy mà cả ba bộ truyện đều có một điểm chung: nhân vật chính cầm kiếm không phải để mạnh hơn, mà…

```text
Wide 16:9 landscape cinematic frame. three silhouettes with swords standing back to back, each shielding a smaller figure behind them, wide shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Nếu được chọn một hệ

Lời: Câu hỏi cuối: nếu được sống trong một trong ba thế giới và học một hệ, bạn chọn hệ nào?

```text
Wide 16:9 landscape cinematic frame. three doors side by side in a misty hall, each with a different sword emblem carved on it, wide shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Chọn Hơi thở, bạn sẽ phải luyện rất khổ, và sống trong thế giới đầy quỷ dữ. Chọn Haki, bạn cần một ý chí thép…

```text
Wide 16:9 landscape cinematic frame. a mountain training path on one side and a small ship on a stormy sea on the other, split composition, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Chọn yêu đao, bạn phải từ bỏ mọi thứ khác, và trở thành mục tiêu của cả thế giới ngầm.

```text
Wide 16:9 landscape cinematic frame. a lone figure holding a sword under a single streetlight while many eyes glow from the dark around them, wide shot, tense cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn Hơi thở, vì Kaku thở rất giỏi. Ít nhất là khi ngủ. Bạn thì sao?

```text
Wide 16:9 landscape cinematic frame. the owl mascot asleep at its desk, breathing peacefully with little puffs of air. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · Kết

Lời: Một hơi thở, một ý chí, một thanh kiếm có phép. Ba hệ kiếm thuật, ba cách trả lời. Và bảng điểm của Kaku chỉ…

```text
Wide 16:9 landscape cinematic frame. three swords laid in a triangle on a wooden table at sunset, top-down shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Video tiếp theo, Kaku muốn bạn chọn: hai hệ sức mạnh nào bạn muốn Kaku đặt lên cùng một bàn? Hãy bình luận cặ…

```text
Wide 16:9 landscape cinematic frame. a blank matchup card with two empty slots and a versus symbol pinned on a corkboard, close-up, warm lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những bảng điểm có luật rõ ràng, hãy đăng ký kênh. Và lần tới cầm một vật quan trọng với mình,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing with a tiny wooden sword held flat in both wings, then waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Kiếm thuật Nhật ngoài đời thật

Khoảng 117 giây · cảnh s01–s10 · 1525 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới cái kết của Kimetsu no Yaiba, arc Wano của One Piece, và các chương giữa của Kagurabachi. Nếu bạn chưa xem tới đó, hãy lưu video lại cho sau này.

<short pause> Ba bộ truyện, ba cách cầm kiếm. Một bên học cách thở. Một bên rèn ý chí. Một bên cầm một thanh kiếm tự nó đã có phép. Nếu đặt ba hệ ấy lên cùng một bàn, hệ nào thắng?

<short pause> Kaku không so ai mạnh hơn ai. Kaku so hệ thống: học thế nào, mạnh tới đâu, và phải trả giá bao nhiêu.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đặt Hơi thở của Kimetsu no Yaiba, kiếm Haki của One Piece, và yêu đao của Kagurabachi lên cùng một bàn. Năm tiêu chí, chấm từ một tới năm, và cuối video là bảng điểm cuối cùng.

<short pause> Và nếu bạn vừa xem video nhập môn Kagurabachi của Kaku, đây là lúc thanh kiếm thứ bảy bước vào một trận so tài với hai hệ lớn nhất của anime.

<short pause> Trước khi vào ba hệ hư cấu, Kaku kể một chút về kiếm thuật Nhật ngoài đời thật. Cả ba bộ truyện đều mượn không ít từ đây.

<short pause> Ở Nhật có những trường phái kiếm thuật cổ, được truyền từ thầy sang trò qua nhiều thế kỷ. Mỗi trường phái có những bài quyền riêng, như một ngôn ngữ riêng của thanh kiếm.

<short pause> Một ví dụ nổi tiếng là trường phái hai kiếm gắn với kiếm sĩ Miyamoto Musashi ở thế kỷ mười bảy. Cầm hai kiếm cùng lúc, nghe như truyện tranh, nhưng là chuyện có thật.

<short pause> Ngày nay, môn phổ biến nhất là kendo, đánh bằng kiếm tre và mặc giáp bảo hộ. Và trong kendo, hơi thở và tiếng hô cũng là một phần của đòn đánh.

<short pause> Kaku nhắc: đây là giới thiệu văn hóa, không phải hướng dẫn. Muốn học kiếm, hãy tìm một võ đường có thầy dạy đàng hoàng.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới cái kết của Kimetsu no Yaiba, arc Wano của One Piece, và các chương giữa của Kagurabachi. Nếu bạn chưa xem tới đó, hãy lưu video lại cho sau này.

[pause] Ba bộ truyện, ba cách cầm kiếm. Một bên học cách thở. Một bên rèn ý chí. Một bên cầm một thanh kiếm tự nó đã có phép. [curious] Nếu đặt ba hệ ấy lên cùng một bàn, hệ nào thắng?

[pause] Kaku không so ai mạnh hơn ai. Kaku so hệ thống: học thế nào, mạnh tới đâu, và phải trả giá bao nhiêu.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đặt Hơi thở của Kimetsu no Yaiba, kiếm Haki của One Piece, và yêu đao của Kagurabachi lên cùng một bàn. Năm tiêu chí, chấm từ một tới năm, và cuối video là bảng điểm cuối cùng.

[pause] Và nếu bạn vừa xem video nhập môn Kagurabachi của Kaku, đây là lúc thanh kiếm thứ bảy bước vào một trận so tài với hai hệ lớn nhất của anime.

[pause] Trước khi vào ba hệ hư cấu, Kaku kể một chút về kiếm thuật Nhật ngoài đời thật. Cả ba bộ truyện đều mượn không ít từ đây.

[pause] Ở Nhật có những trường phái kiếm thuật cổ, được truyền từ thầy sang trò qua nhiều thế kỷ. Mỗi trường phái có những bài quyền riêng, như một ngôn ngữ riêng của thanh kiếm.

[pause] Một ví dụ nổi tiếng là trường phái hai kiếm gắn với kiếm sĩ Miyamoto Musashi ở thế kỷ mười bảy. Cầm hai kiếm cùng lúc, nghe như truyện tranh, nhưng là chuyện có thật.

[pause] Ngày nay, môn phổ biến nhất là kendo, đánh bằng kiếm tre và mặc giáp bảo hộ. Và trong kendo, hơi thở và tiếng hô cũng là một phần của đòn đánh.

[pause] Kaku nhắc: đây là giới thiệu văn hóa, không phải hướng dẫn. Muốn học kiếm, hãy tìm một võ đường có thầy dạy đàng hoàng.
```

### c02 · Hồ sơ hệ 1: Hơi thở / Hồ sơ hệ 2: kiếm Haki

Khoảng 138 giây · cảnh s11–s24 · 1791 ký tự

**Gemini**

```text
Hệ thứ nhất: Hơi thở trong Kimetsu no Yaiba. Kiếm sĩ học cách thở theo một nhịp đặc biệt, gọi là Toàn Tập Trung, để đẩy cơ thể vượt giới hạn con người.

<short pause> Mọi Hơi thở đều bắt nguồn từ một hơi thở đầu tiên: Hơi thở Mặt Trời, do một kiếm sĩ huyền thoại tạo ra từ nhiều thế kỷ trước.

<short pause> Từ đó chia ra năm hơi thở chính: Nước, Lửa, Sấm, Gió, Đá. Rồi từ năm nhánh chính lại mọc ra những nhánh nhỏ như Sương, Rắn, Hoa, Côn trùng, Âm thanh.

<short pause> Kiếm cũng đặc biệt: kiếm Nichirin rèn từ loại quặng hấp thụ ánh mặt trời, và đổi màu theo người cầm nó lần đầu.

<short pause> Và đỉnh cao của hệ này là Ấn, một dấu hiệu xuất hiện trên cơ thể khi kiếm sĩ vượt giới hạn, giúp sức mạnh tăng vọt.

<short pause> Còn có Thường Trung, tức giữ nhịp Toàn Tập Trung cả khi ngủ. Kiếm sĩ giỏi luyện tới mức cơ thể tự thở đúng cách suốt hai mươi bốn giờ mỗi ngày.

<short pause> <laugh> Kaku để ý: Hơi thở là hệ dân chủ nhất. Không cần sinh ra đặc biệt, chỉ cần luyện đủ khổ.

<short pause> Hệ thứ hai: kiếm Haki trong One Piece. Haki là sức mạnh của ý chí, có ba loại: vũ trang, quan sát, và bá vương.

<short pause> Kiếm sĩ phủ Haki vũ trang lên lưỡi kiếm, làm thanh kiếm cứng hơn, sắc hơn, và chém được cả những thứ bình thường không chém nổi.

<short pause> Kiếm trong One Piece cũng có hạng. Có mười hai thanh tối thượng, hai mươi mốt thanh đại danh đao, và năm mươi thanh lương danh đao. Có những thanh còn bị cho là mang lời nguyền.

<short pause> Ở Wano, có một thanh kiếm hút Haki của người cầm nó. Kiếm sĩ phải kiểm soát được nó, nếu không sẽ bị vắt kiệt sức.

<short pause> Và đỉnh cao của hệ này là phủ Haki bá vương lên lưỡi kiếm. Chỉ những kiếm sĩ mạnh nhất thế giới mới làm được.

<short pause> Haki quan sát cũng quan trọng với kiếm sĩ: nó giúp cảm nhận đối thủ, nhìn trước đòn đánh, và ở mức cao nhất, thấy trước một chút tương lai.

<short pause> Kaku để ý: kiếm Haki là hệ đặt ý chí lên trên hết. Thanh kiếm tốt giúp bạn, nhưng thứ quyết định là người cầm kiếm tin vào điều gì.
```

**ElevenLabs**

```text
Hệ thứ nhất: Hơi thở trong Kimetsu no Yaiba. Kiếm sĩ học cách thở theo một nhịp đặc biệt, gọi là Toàn Tập Trung, để đẩy cơ thể vượt giới hạn con người.

[pause] Mọi Hơi thở đều bắt nguồn từ một hơi thở đầu tiên: Hơi thở Mặt Trời, do một kiếm sĩ huyền thoại tạo ra từ nhiều thế kỷ trước.

[pause] Từ đó chia ra năm hơi thở chính: Nước, Lửa, Sấm, Gió, Đá. Rồi từ năm nhánh chính lại mọc ra những nhánh nhỏ như Sương, Rắn, Hoa, Côn trùng, Âm thanh.

[pause] Kiếm cũng đặc biệt: kiếm Nichirin rèn từ loại quặng hấp thụ ánh mặt trời, và đổi màu theo người cầm nó lần đầu.

[pause] Và đỉnh cao của hệ này là Ấn, một dấu hiệu xuất hiện trên cơ thể khi kiếm sĩ vượt giới hạn, giúp sức mạnh tăng vọt.

[pause] Còn có Thường Trung, tức giữ nhịp Toàn Tập Trung cả khi ngủ. Kiếm sĩ giỏi luyện tới mức cơ thể tự thở đúng cách suốt hai mươi bốn giờ mỗi ngày.

[pause] [chuckles] Kaku để ý: Hơi thở là hệ dân chủ nhất. Không cần sinh ra đặc biệt, chỉ cần luyện đủ khổ.

[pause] Hệ thứ hai: kiếm Haki trong One Piece. Haki là sức mạnh của ý chí, có ba loại: vũ trang, quan sát, và bá vương.

[pause] Kiếm sĩ phủ Haki vũ trang lên lưỡi kiếm, làm thanh kiếm cứng hơn, sắc hơn, và chém được cả những thứ bình thường không chém nổi.

[pause] Kiếm trong One Piece cũng có hạng. Có mười hai thanh tối thượng, hai mươi mốt thanh đại danh đao, và năm mươi thanh lương danh đao. Có những thanh còn bị cho là mang lời nguyền.

[pause] Ở Wano, có một thanh kiếm hút Haki của người cầm nó. Kiếm sĩ phải kiểm soát được nó, nếu không sẽ bị vắt kiệt sức.

[pause] Và đỉnh cao của hệ này là phủ Haki bá vương lên lưỡi kiếm. Chỉ những kiếm sĩ mạnh nhất thế giới mới làm được.

[pause] Haki quan sát cũng quan trọng với kiếm sĩ: nó giúp cảm nhận đối thủ, nhìn trước đòn đánh, và ở mức cao nhất, thấy trước một chút tương lai.

[pause] Kaku để ý: kiếm Haki là hệ đặt ý chí lên trên hết. Thanh kiếm tốt giúp bạn, nhưng thứ quyết định là người cầm kiếm tin vào điều gì.
```

### c03 · Hồ sơ hệ 3: yêu đao / Ba người thầy / Năm tiêu chí

Khoảng 150 giây · cảnh s25–s39 · 1956 ký tự

**Gemini**

```text
Hệ thứ ba: yêu đao trong Kagurabachi. Sức mạnh nằm trong chính thanh kiếm, do người thợ rèn Rokuhira Kunishige tạo ra.

<short pause> Có sáu thanh yêu đao, những vũ khí đã kết thúc Chiến tranh Seitei. Về sau có thêm thanh thứ bảy, Enten, rèn gần mười lăm năm sau chiến tranh.

<short pause> Luật quan trọng nhất là hợp đồng trọn đời. Khi một người trở thành chủ của yêu đao, chỉ người đó dùng được kỹ thuật của nó, cho tới khi họ chết.

<short pause> Và cái giá: người ký hợp đồng mất vĩnh viễn thuật riêng của mình. Không có kiếm trong tay, họ gần như không còn gì để chiến đấu.

<short pause> Một người có thể ký hợp đồng với nhiều yêu đao. <short pause> Nhưng mỗi thanh kiếm, tại một thời điểm, chỉ nghe lời một chủ nhân.

<short pause> <laugh> Kaku để ý: yêu đao là hệ ngược với Hơi thở. Không cần luyện nửa đời, nhưng số người được cầm thì đếm trên đầu ngón tay.

<short pause> Có một điểm chung thú vị: cả ba hệ đều được truyền qua một người thầy, và người thầy ấy quyết định rất nhiều về người học trò.

<short pause> Trong Kimetsu, Tanjiro học Hơi thở Nước từ một người thầy đeo mặt nạ trên núi, với những bài tập tưởng như bất khả thi, như chém đôi một tảng đá.

<short pause> Trong One Piece, Zoro dành hai năm học kiếm từ chính kiếm sĩ mạnh nhất thế giới, người từng là mục tiêu mà cậu muốn vượt qua.

<short pause> Còn trong Kagurabachi, người thầy đầu tiên của Chihiro không dạy cậu đánh kiếm, mà dạy cậu rèn kiếm. Hiểu thanh kiếm từ bên trong, trước khi dùng nó.

<short pause> Kaku để ý: ba người thầy phản ánh đúng ba hệ. Hơi thở dạy kỷ luật. Haki dạy bạn đối mặt với người mạnh hơn. Yêu đao dạy bạn hiểu thứ mình cầm trong tay.

<short pause> Năm tiêu chí của Kaku. Một: độ phổ cập, tức bao nhiêu người có thể học được. Hai: sức mạnh đỉnh cao, tức hệ này đi xa tới đâu.

<short pause> Ba: độ đa dạng, tức có bao nhiêu phong cách khác nhau. Bốn: cái giá, và ở tiêu chí này, cái giá càng nhẹ thì điểm càng cao.

<short pause> Năm: sợi dây giữa người và kiếm, tức hệ này kể câu chuyện về mối quan hệ giữa kiếm sĩ và thanh kiếm sâu tới đâu.

<short pause> Mỗi tiêu chí từ một tới năm, tổng tối đa hai mươi lăm. Và như mọi bảng điểm của Kaku, đây là đánh giá của Kaku. Bạn cứ chấm khác nhé.
```

**ElevenLabs**

```text
Hệ thứ ba: yêu đao trong Kagurabachi. Sức mạnh nằm trong chính thanh kiếm, do người thợ rèn Rokuhira Kunishige tạo ra.

[pause] Có sáu thanh yêu đao, những vũ khí đã kết thúc Chiến tranh Seitei. Về sau có thêm thanh thứ bảy, Enten, rèn gần mười lăm năm sau chiến tranh.

[pause] Luật quan trọng nhất là hợp đồng trọn đời. Khi một người trở thành chủ của yêu đao, chỉ người đó dùng được kỹ thuật của nó, cho tới khi họ chết.

[pause] Và cái giá: người ký hợp đồng mất vĩnh viễn thuật riêng của mình. Không có kiếm trong tay, họ gần như không còn gì để chiến đấu.

[pause] Một người có thể ký hợp đồng với nhiều yêu đao. [pause] Nhưng mỗi thanh kiếm, tại một thời điểm, chỉ nghe lời một chủ nhân.

[pause] [chuckles] Kaku để ý: yêu đao là hệ ngược với Hơi thở. Không cần luyện nửa đời, nhưng số người được cầm thì đếm trên đầu ngón tay.

[pause] Có một điểm chung thú vị: cả ba hệ đều được truyền qua một người thầy, và người thầy ấy quyết định rất nhiều về người học trò.

[pause] Trong Kimetsu, Tanjiro học Hơi thở Nước từ một người thầy đeo mặt nạ trên núi, với những bài tập tưởng như bất khả thi, như chém đôi một tảng đá.

[pause] Trong One Piece, Zoro dành hai năm học kiếm từ chính kiếm sĩ mạnh nhất thế giới, người từng là mục tiêu mà cậu muốn vượt qua.

[pause] Còn trong Kagurabachi, người thầy đầu tiên của Chihiro không dạy cậu đánh kiếm, mà dạy cậu rèn kiếm. Hiểu thanh kiếm từ bên trong, trước khi dùng nó.

[pause] Kaku để ý: ba người thầy phản ánh đúng ba hệ. Hơi thở dạy kỷ luật. Haki dạy bạn đối mặt với người mạnh hơn. Yêu đao dạy bạn hiểu thứ mình cầm trong tay.

[pause] Năm tiêu chí của Kaku. Một: độ phổ cập, tức bao nhiêu người có thể học được. Hai: sức mạnh đỉnh cao, tức hệ này đi xa tới đâu.

[pause] Ba: độ đa dạng, tức có bao nhiêu phong cách khác nhau. Bốn: cái giá, và ở tiêu chí này, cái giá càng nhẹ thì điểm càng cao.

[pause] Năm: sợi dây giữa người và kiếm, tức hệ này kể câu chuyện về mối quan hệ giữa kiếm sĩ và thanh kiếm sâu tới đâu.

[pause] Mỗi tiêu chí từ một tới năm, tổng tối đa hai mươi lăm. Và như mọi bảng điểm của Kaku, đây là đánh giá của Kaku. Bạn cứ chấm khác nhé.
```

### c04 · Tiêu chí 1: độ phổ cập / Tiêu chí 2: sức mạnh đỉnh cao / Tiêu chí 3: độ đa dạng

Khoảng 129 giây · cảnh s40–s52 · 1682 ký tự

**Gemini**

```text
Hơi thở: ai cũng có thể học, nếu luyện đủ khổ và có thầy giỏi. Nhiều kiếm sĩ bình thường trong Đội diệt quỷ đều dùng Hơi thở. Bốn điểm.

<short pause> Kiếm Haki: theo truyện, mọi sinh vật đều có tiềm năng Haki, nhưng đánh thức được nó rất khó, và Haki bá vương thì chỉ một số ít người sinh ra đã có. Ba điểm.

<short pause> Yêu đao: chỉ có bảy thanh, mỗi thanh một người chủ tại một thời điểm. Một điểm.

<short pause> Ở điểm này, Hơi thở giống một trường võ, Haki giống một tài năng cần khai mở, còn yêu đao giống một báu vật quốc gia.

<short pause> Kaku để ý: hệ phổ cập nhất tạo ra một đội quân. Hệ hiếm nhất tạo ra những con người trở thành mục tiêu săn đuổi.

<short pause> Hơi thở: ở đỉnh cao, người dùng Hơi thở Mặt Trời có thể đứng ngang, thậm chí áp đảo cả Vua Quỷ. <short pause> Nhưng đó là trường hợp gần như duy nhất trong lịch sử truyện. Bốn điểm.

<short pause> Kiếm Haki: ở đỉnh cao, kiếm sĩ mạnh nhất có thể chém đôi những thứ khổng lồ, và đối đầu những kẻ mạnh nhất thế giới. Năm điểm.

<short pause> Yêu đao: sáu thanh kiếm đủ để kết thúc cả một cuộc chiến tranh. Về sức tàn phá, đây là hệ đáng sợ nhất. Năm điểm.

<short pause> <laugh> Kaku để ý: hai hệ cùng năm điểm, nhưng khác nhau ở chỗ: đỉnh cao của Haki là của một người, còn đỉnh cao của yêu đao là của một vũ khí.

<short pause> Hơi thở: hàng chục nhánh, mỗi nhánh nhiều thế kiếm, mỗi thế mang hình ảnh riêng, từ sóng nước tới hoa đào, từ sấm sét tới trăng khuyết. Năm điểm.

<short pause> Kiếm Haki: mỗi kiếm sĩ tự tạo phong cách riêng, như một kiếm, hai kiếm, hay ba kiếm cùng lúc. <short pause> Nhưng Haki bản thân nó chỉ có ba loại. Bốn điểm.

<short pause> Yêu đao: mỗi thanh có một năng lực hoàn toàn khác nhau. Chỉ riêng Enten đã có ba kỹ thuật cá vàng. <short pause> Nhưng tổng cộng chỉ có bảy thanh. Bốn điểm.

<short pause> Kaku để ý: Hơi thở thắng ở tiêu chí này vì nó là một hệ thống mở. Người sau có thể tạo ra nhánh mới từ nhánh cũ.
```

**ElevenLabs**

```text
Hơi thở: ai cũng có thể học, nếu luyện đủ khổ và có thầy giỏi. Nhiều kiếm sĩ bình thường trong Đội diệt quỷ đều dùng Hơi thở. Bốn điểm.

[pause] Kiếm Haki: theo truyện, mọi sinh vật đều có tiềm năng Haki, nhưng đánh thức được nó rất khó, và Haki bá vương thì chỉ một số ít người sinh ra đã có. Ba điểm.

[pause] Yêu đao: chỉ có bảy thanh, mỗi thanh một người chủ tại một thời điểm. Một điểm.

[pause] Ở điểm này, Hơi thở giống một trường võ, Haki giống một tài năng cần khai mở, còn yêu đao giống một báu vật quốc gia.

[pause] Kaku để ý: hệ phổ cập nhất tạo ra một đội quân. Hệ hiếm nhất tạo ra những con người trở thành mục tiêu săn đuổi.

[pause] Hơi thở: ở đỉnh cao, người dùng Hơi thở Mặt Trời có thể đứng ngang, thậm chí áp đảo cả Vua Quỷ. [pause] Nhưng đó là trường hợp gần như duy nhất trong lịch sử truyện. Bốn điểm.

[pause] Kiếm Haki: ở đỉnh cao, kiếm sĩ mạnh nhất có thể chém đôi những thứ khổng lồ, và đối đầu những kẻ mạnh nhất thế giới. Năm điểm.

[pause] Yêu đao: sáu thanh kiếm đủ để kết thúc cả một cuộc chiến tranh. Về sức tàn phá, đây là hệ đáng sợ nhất. Năm điểm.

[pause] [chuckles] Kaku để ý: hai hệ cùng năm điểm, nhưng khác nhau ở chỗ: đỉnh cao của Haki là của một người, còn đỉnh cao của yêu đao là của một vũ khí.

[pause] Hơi thở: hàng chục nhánh, mỗi nhánh nhiều thế kiếm, mỗi thế mang hình ảnh riêng, từ sóng nước tới hoa đào, từ sấm sét tới trăng khuyết. Năm điểm.

[pause] Kiếm Haki: mỗi kiếm sĩ tự tạo phong cách riêng, như một kiếm, hai kiếm, hay ba kiếm cùng lúc. [pause] Nhưng Haki bản thân nó chỉ có ba loại. Bốn điểm.

[pause] Yêu đao: mỗi thanh có một năng lực hoàn toàn khác nhau. Chỉ riêng Enten đã có ba kỹ thuật cá vàng. [pause] Nhưng tổng cộng chỉ có bảy thanh. Bốn điểm.

[pause] Kaku để ý: Hơi thở thắng ở tiêu chí này vì nó là một hệ thống mở. Người sau có thể tạo ra nhánh mới từ nhánh cũ.
```

### c05 · Tiêu chí 4: cái giá / Tiêu chí 5: người và kiếm / Bảng điểm cuối cùng

Khoảng 122 giây · cảnh s53–s65 · 1587 ký tự

**Gemini**

```text
Hơi thở: cái giá nặng nhất là Ấn. Theo truyện, những người thức tỉnh Ấn sẽ không sống quá tuổi hai mươi lăm, trừ một ngoại lệ duy nhất. Hai điểm.

<short pause> Kiếm Haki: cái giá là kiệt sức, và với một vài thanh kiếm đặc biệt, bị hút cạn Haki. Nặng, nhưng hồi phục được. Bốn điểm.

<short pause> Yêu đao: mất vĩnh viễn thuật riêng, không có kiếm là không có gì, và luôn bị săn đuổi. Còn chưa kể cái giá đạo đức của việc cầm một vũ khí chiến tranh. Hai điểm.

<short pause> <laugh> Kaku để ý: hai hệ mạnh bùng nổ nhất đều có cái giá đắt nhất. Chỉ kiếm Haki là cho bạn mạnh lên mà vẫn còn đường lùi.

<short pause> Hơi thở: thanh kiếm đổi màu theo người cầm, và các thợ rèn gắn bó với kiếm sĩ của mình. <short pause> Nhưng sức mạnh vẫn nằm trong cơ thể, không nằm trong kiếm. Bốn điểm.

<short pause> Kiếm Haki: trong One Piece, kiếm có tính cách, có lời nguyền, có lịch sử. Một kiếm sĩ có thể mang theo lời hứa với một người bạn đã khuất trong chính thanh kiếm của mình. Năm điểm.

<short pause> Yêu đao: hợp đồng trọn đời nghĩa là người và kiếm gắn với nhau tới chết. Và với Chihiro, thanh kiếm còn là di sản của người cha. Năm điểm.

<short pause> Kaku để ý: ở tiêu chí này, hai hệ có thanh kiếm biết nói chuyện, theo nghĩa bóng, đều đạt điểm tối đa.

<short pause> Bảng điểm cuối cùng. Hơi thở: bốn, bốn, năm, hai, bốn. Tổng mười chín điểm.

<short pause> Kiếm Haki: ba, năm, bốn, bốn, năm. Tổng hai mươi mốt điểm.

<short pause> Yêu đao: một, năm, bốn, hai, năm. Tổng mười bảy điểm.

<short pause> Khoảng cách giữa ba hệ không lớn: chỉ bốn điểm từ hạng nhất tới hạng ba. Chỉ cần đổi một tiêu chí, thứ hạng có thể đảo ngược.

<short pause> Người thắng theo bảng của Kaku: kiếm Haki của One Piece, với hai mươi mốt điểm. Không phải vì nó mạnh nhất ở mọi mặt, mà vì nó không có điểm yếu nào quá sâu.
```

**ElevenLabs**

```text
Hơi thở: cái giá nặng nhất là Ấn. Theo truyện, những người thức tỉnh Ấn sẽ không sống quá tuổi hai mươi lăm, trừ một ngoại lệ duy nhất. Hai điểm.

[pause] Kiếm Haki: cái giá là kiệt sức, và với một vài thanh kiếm đặc biệt, bị hút cạn Haki. Nặng, nhưng hồi phục được. Bốn điểm.

[pause] Yêu đao: mất vĩnh viễn thuật riêng, không có kiếm là không có gì, và luôn bị săn đuổi. Còn chưa kể cái giá đạo đức của việc cầm một vũ khí chiến tranh. Hai điểm.

[pause] [chuckles] Kaku để ý: hai hệ mạnh bùng nổ nhất đều có cái giá đắt nhất. Chỉ kiếm Haki là cho bạn mạnh lên mà vẫn còn đường lùi.

[pause] Hơi thở: thanh kiếm đổi màu theo người cầm, và các thợ rèn gắn bó với kiếm sĩ của mình. [pause] Nhưng sức mạnh vẫn nằm trong cơ thể, không nằm trong kiếm. Bốn điểm.

[pause] Kiếm Haki: trong One Piece, kiếm có tính cách, có lời nguyền, có lịch sử. Một kiếm sĩ có thể mang theo lời hứa với một người bạn đã khuất trong chính thanh kiếm của mình. Năm điểm.

[pause] Yêu đao: hợp đồng trọn đời nghĩa là người và kiếm gắn với nhau tới chết. Và với Chihiro, thanh kiếm còn là di sản của người cha. Năm điểm.

[pause] Kaku để ý: ở tiêu chí này, hai hệ có thanh kiếm biết nói chuyện, theo nghĩa bóng, đều đạt điểm tối đa.

[pause] Bảng điểm cuối cùng. Hơi thở: bốn, bốn, năm, hai, bốn. Tổng mười chín điểm.

[pause] Kiếm Haki: ba, năm, bốn, bốn, năm. Tổng hai mươi mốt điểm.

[pause] Yêu đao: một, năm, bốn, hai, năm. Tổng mười bảy điểm.

[pause] Khoảng cách giữa ba hệ không lớn: chỉ bốn điểm từ hạng nhất tới hạng ba. Chỉ cần đổi một tiêu chí, thứ hạng có thể đảo ngược.

[pause] Người thắng theo bảng của Kaku: kiếm Haki của One Piece, với hai mươi mốt điểm. Không phải vì nó mạnh nhất ở mọi mặt, mà vì nó không có điểm yếu nào quá sâu.
```

### c06 · Điểm yếu chí mạng của từng hệ / Nếu đổi trọng số thì sao? / Trận giả tưởng: ba kiếm sĩ trên cùng một sân

Khoảng 135 giây · cảnh s66–s79 · 1758 ký tự

**Gemini**

```text
Mỗi hệ đều có một điểm yếu chí mạng. Hơi thở dựa vào phổi và thể lực. Khi kiếm sĩ bị thương nặng hay kiệt sức, nhịp thở vỡ, và sức mạnh sụp theo.

<short pause> Kiếm Haki dựa vào ý chí. Khi Haki cạn, kiếm sĩ trở lại thành người thường cầm một thanh kiếm tốt.

<short pause> Yêu đao dựa vào chính thanh kiếm. Mất kiếm, người ký hợp đồng mất gần như tất cả, vì thuật riêng của họ đã không còn.

<short pause> Nói cách khác: muốn thắng người dùng Hơi thở, hãy kéo dài trận đấu. Muốn thắng người dùng Haki, hãy làm họ nghi ngờ bản thân. Muốn thắng người cầm yêu đao, hãy cướp kiếm.

<short pause> <laugh> Kaku để ý: chính điểm yếu làm các trận đấu trong ba bộ truyện hay. Nhân vật mạnh nhất cũng phải chiến đấu quanh điểm yếu của mình.

<short pause> Nhưng bảng điểm phụ thuộc vào thứ bạn coi trọng. Nếu chỉ tính sức mạnh đỉnh cao, kiếm Haki và yêu đao hòa nhau.

<short pause> Nếu bạn coi trọng việc ai cũng học được, Hơi thở thắng xa. Đó là hệ của những người bình thường muốn bảo vệ người khác.

<short pause> Và nếu bạn coi trọng câu chuyện giữa người và kiếm, yêu đao đứng ngang kiếm Haki. Mỗi hệ đều thắng ở một câu hỏi khác nhau.

<short pause> Giờ là phần giả tưởng vui. Tưởng tượng ba kiếm sĩ bình thường, mỗi người đại diện cho một hệ, gặp nhau trên cùng một sân. Không ai là nhân vật chính.

<short pause> Người dùng Hơi thở có tốc độ và sự bền bỉ. Anh ta sẽ cố kéo trận đấu dài ra, dùng các thế kiếm liên hoàn.

<short pause> Người dùng Haki có Haki quan sát. Anh ta nhìn thấy trước đòn đánh, nên tốc độ của Hơi thở bớt đáng sợ.

<short pause> Còn người cầm yêu đao có một năng lực mà hai người kia chưa từng thấy. Trận đầu tiên, yếu tố bất ngờ có thể quyết định tất cả.

<short pause> Kết quả giả tưởng của Kaku: như oẳn tù tì. Haki khắc Hơi thở, yêu đao khắc Haki ở lần gặp đầu, và Hơi thở khắc yêu đao nếu kéo được trận đấu dài để cướp kiếm.

<short pause> Kaku nhắc: đây chỉ là giả tưởng, không có trong truyện nào. Bạn nghĩ vòng tròn ấy nên xoay theo chiều nào?
```

**ElevenLabs**

```text
Mỗi hệ đều có một điểm yếu chí mạng. Hơi thở dựa vào phổi và thể lực. Khi kiếm sĩ bị thương nặng hay kiệt sức, nhịp thở vỡ, và sức mạnh sụp theo.

[pause] Kiếm Haki dựa vào ý chí. Khi Haki cạn, kiếm sĩ trở lại thành người thường cầm một thanh kiếm tốt.

[pause] Yêu đao dựa vào chính thanh kiếm. Mất kiếm, người ký hợp đồng mất gần như tất cả, vì thuật riêng của họ đã không còn.

[pause] Nói cách khác: muốn thắng người dùng Hơi thở, hãy kéo dài trận đấu. Muốn thắng người dùng Haki, hãy làm họ nghi ngờ bản thân. Muốn thắng người cầm yêu đao, hãy cướp kiếm.

[pause] [chuckles] Kaku để ý: chính điểm yếu làm các trận đấu trong ba bộ truyện hay. Nhân vật mạnh nhất cũng phải chiến đấu quanh điểm yếu của mình.

[pause] Nhưng bảng điểm phụ thuộc vào thứ bạn coi trọng. Nếu chỉ tính sức mạnh đỉnh cao, kiếm Haki và yêu đao hòa nhau.

[pause] Nếu bạn coi trọng việc ai cũng học được, Hơi thở thắng xa. Đó là hệ của những người bình thường muốn bảo vệ người khác.

[pause] Và nếu bạn coi trọng câu chuyện giữa người và kiếm, yêu đao đứng ngang kiếm Haki. Mỗi hệ đều thắng ở một câu hỏi khác nhau.

[pause] Giờ là phần giả tưởng vui. Tưởng tượng ba kiếm sĩ bình thường, mỗi người đại diện cho một hệ, gặp nhau trên cùng một sân. Không ai là nhân vật chính.

[pause] Người dùng Hơi thở có tốc độ và sự bền bỉ. Anh ta sẽ cố kéo trận đấu dài ra, dùng các thế kiếm liên hoàn.

[pause] Người dùng Haki có Haki quan sát. Anh ta nhìn thấy trước đòn đánh, nên tốc độ của Hơi thở bớt đáng sợ.

[pause] Còn người cầm yêu đao có một năng lực mà hai người kia chưa từng thấy. Trận đầu tiên, yếu tố bất ngờ có thể quyết định tất cả.

[pause] Kết quả giả tưởng của Kaku: như oẳn tù tì. Haki khắc Hơi thở, yêu đao khắc Haki ở lần gặp đầu, và Hơi thở khắc yêu đao nếu kéo được trận đấu dài để cướp kiếm.

[pause] Kaku nhắc: đây chỉ là giả tưởng, không có trong truyện nào. [curious] Bạn nghĩ vòng tròn ấy nên xoay theo chiều nào?
```

### c07 · Góc nhìn của Kaku / Nếu được chọn một hệ / Kết

Khoảng 106 giây · cảnh s80–s90 · 1384 ký tự

**Gemini**

```text
<laugh> Kaku nghĩ ba hệ kiếm thuật là ba câu trả lời cho một câu hỏi: sức mạnh đến từ đâu?

<short pause> Kimetsu nói: sức mạnh đến từ cơ thể và sự kiên trì. One Piece nói: sức mạnh đến từ ý chí. Kagurabachi nói: sức mạnh có thể được rèn ra, nhưng ai cầm nó thì phải chịu trách nhiệm với nó.

<short pause> Ba câu trả lời ấy không loại trừ nhau. Một kiếm sĩ giỏi có lẽ cần cả ba: cơ thể được rèn luyện, một ý chí vững, và ý thức về thứ mình cầm trong tay.

<short pause> Và có lẽ vì vậy mà cả ba bộ truyện đều có một điểm chung: nhân vật chính cầm kiếm không phải để mạnh hơn, mà để bảo vệ ai đó.

<short pause> Câu hỏi cuối: nếu được sống trong một trong ba thế giới và học một hệ, bạn chọn hệ nào?

<short pause> Chọn Hơi thở, bạn sẽ phải luyện rất khổ, và sống trong thế giới đầy quỷ dữ. Chọn Haki, bạn cần một ý chí thép và một chuyến ra khơi đầy nguy hiểm.

<short pause> Chọn yêu đao, bạn phải từ bỏ mọi thứ khác, và trở thành mục tiêu của cả thế giới ngầm.

<short pause> Kaku chọn Hơi thở, vì Kaku thở rất giỏi. Ít nhất là khi ngủ. Bạn thì sao?

<short pause> Một hơi thở, một ý chí, một thanh kiếm có phép. Ba hệ kiếm thuật, ba cách trả lời. Và bảng điểm của Kaku chỉ là một trong vô số cách chấm.

<short pause> Video tiếp theo, Kaku muốn bạn chọn: hai hệ sức mạnh nào bạn muốn Kaku đặt lên cùng một bàn? Hãy bình luận cặp đấu bạn muốn xem nhất.

<short pause> Nếu bạn thích những bảng điểm có luật rõ ràng, hãy đăng ký kênh. Và lần tới cầm một vật quan trọng với mình, hãy nghĩ xem sợi dây giữa bạn và nó là gì. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Kaku nghĩ ba hệ kiếm thuật là ba câu trả lời cho một câu hỏi: sức mạnh đến từ đâu?

[pause] Kimetsu nói: sức mạnh đến từ cơ thể và sự kiên trì. One Piece nói: sức mạnh đến từ ý chí. Kagurabachi nói: sức mạnh có thể được rèn ra, nhưng ai cầm nó thì phải chịu trách nhiệm với nó.

[pause] Ba câu trả lời ấy không loại trừ nhau. Một kiếm sĩ giỏi có lẽ cần cả ba: cơ thể được rèn luyện, một ý chí vững, và ý thức về thứ mình cầm trong tay.

[pause] Và có lẽ vì vậy mà cả ba bộ truyện đều có một điểm chung: nhân vật chính cầm kiếm không phải để mạnh hơn, mà để bảo vệ ai đó.

[pause] [curious] Câu hỏi cuối: nếu được sống trong một trong ba thế giới và học một hệ, bạn chọn hệ nào?

[pause] Chọn Hơi thở, bạn sẽ phải luyện rất khổ, và sống trong thế giới đầy quỷ dữ. Chọn Haki, bạn cần một ý chí thép và một chuyến ra khơi đầy nguy hiểm.

[pause] Chọn yêu đao, bạn phải từ bỏ mọi thứ khác, và trở thành mục tiêu của cả thế giới ngầm.

[pause] Kaku chọn Hơi thở, vì Kaku thở rất giỏi. Ít nhất là khi ngủ. Bạn thì sao?

[pause] Một hơi thở, một ý chí, một thanh kiếm có phép. Ba hệ kiếm thuật, ba cách trả lời. Và bảng điểm của Kaku chỉ là một trong vô số cách chấm.

[pause] Video tiếp theo, Kaku muốn bạn chọn: hai hệ sức mạnh nào bạn muốn Kaku đặt lên cùng một bàn? Hãy bình luận cặp đấu bạn muốn xem nhất.

[pause] Nếu bạn thích những bảng điểm có luật rõ ràng, hãy đăng ký kênh. Và lần tới cầm một vật quan trọng với mình, hãy nghĩ xem sợi dây giữa bạn và nó là gì. Kaku gấp sổ đây, hẹn gặp lại!
```
