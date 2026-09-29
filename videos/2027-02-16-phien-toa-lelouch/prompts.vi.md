# Bộ prompt · Phiên tòa: Lelouch vi Britannia — anh hùng hay kẻ ác?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 84 ảnh, 9 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (84 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Khai mạc phiên tòa

Lời: Cảnh báo: video này có spoiler toàn bộ Code Geass, cả mùa một, mùa hai, và cái kết. Nếu bạn chưa xem hết, hãy…

```text
Wide 16:9 landscape cinematic frame. a closed case file with a red spoiler seal resting on a courtroom desk beside a wooden gavel, close-up, warm dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Bị cáo: Lelouch vi Britannia, còn được biết với cái tên Zero. Tội danh: giết người, gây chiến tranh, thao tún…

```text
Wide 16:9 landscape cinematic frame. an empty defendant's chair in a grand courtroom under a single spotlight, a black chess king piece placed on the seat, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng cũng chính người này đã chấm dứt một đế chế xâm lược, giải phóng nhiều quốc gia, và kết thúc chiến tran…

```text
Wide 16:9 landscape cinematic frame. a chess board where a single black king piece lies toppled while all the other pieces stand peacefully together, close-up, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Người anh hùng hay kẻ ác? Kẻ giải phóng hay kẻ độc tài? Đó là câu hỏi mà người xem Code Geass đã tranh luận g…

```text
Wide 16:9 landscape cinematic frame. a balance scale on a judge's bench with a white chess piece on one side and a black chess piece on the other, perfectly level, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku lại làm thư ký tòa: đọc cáo trạng, ghi lời bào chữa, gọi nhân chứng.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny clerk's collar sitting at a small desk with a quill and a thick ledger. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Và như mọi phiên tòa của kênh, Kaku không tuyên án. Bạn là bồi thẩm. Cuối video, Kaku mời bạn bỏ phiếu.

```text
Wide 16:9 landscape cinematic frame. a wooden ballot box with a slot on top placed on a courtroom railing, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Một lưu ý: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh cho bạo lực ngoài…

```text
Wide 16:9 landscape cinematic frame. a small notice card pinned to the courtroom door with a simple scale icon, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Hồ sơ bị cáo

Lời: Code Geass là anime gốc của studio Sunrise, mùa một phát năm 2006, mùa hai năm 2008. Đạo diễn là Taniguchi Go…

```text
Wide 16:9 landscape cinematic frame. a stack of old anime DVD cases beside a chessboard on a wooden shelf, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Bối cảnh là một thế giới giả tưởng, nơi đế quốc Britannia hùng mạnh xâm chiếm nhiều quốc gia. Nhật Bản bị chi…

```text
Wide 16:9 landscape cinematic frame. a map of the world with large regions painted in a single imperial color and one island nation stamped with a number, parchment close-up, cold red ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Lelouch là một hoàng tử Britannia. Khi còn nhỏ, mẹ cậu bị ám sát ngay trong cung điện. Em gái Nunnally bị mất…

```text
Wide 16:9 landscape cinematic frame. a grand palace staircase with scattered flower petals and a small overturned wheelchair at the bottom, wide shot, cold melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Khi Lelouch chất vấn cha mình, hoàng đế, về cái chết của mẹ, ông gửi cả hai anh em sang Nhật làm con tin chín…

```text
Wide 16:9 landscape cinematic frame. a small boy standing defiantly before a towering throne in a vast hall, the throne's occupant in shadow, wide shot, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Lelouch lớn lên dưới tên giả Lelouch Lamperouge, một học sinh thông minh, giỏi cờ vua, sống ẩn mình ở Khu vực…

```text
Wide 16:9 landscape cinematic frame. a chessboard mid-game on a school desk by a window with sunlight falling across it, close-up, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Cậu có hai mục tiêu: tìm ra kẻ đã giết mẹ, và tạo ra một thế giới hiền hòa để em gái được sống yên ổn. Và để…

```text
Wide 16:9 landscape cinematic frame. a young figure standing on a rooftop at dusk looking over a city divided between gleaming towers and ruined districts, back view, wide shot, dramatic sunset. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Bạn thân nhất của Lelouch từ thuở nhỏ là Suzaku, một người Nhật. Hai người sẽ gặp lại nhau ở hai phía đối lập…

```text
Wide 16:9 landscape cinematic frame. two small wooden toy soldiers of different colors facing each other on a table, close-up, soft nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Vũ khí của bị cáo: Geass

Lời: Tất cả thay đổi khi Lelouch gặp một cô gái bí ẩn, C.C., và nhận được một năng lực gọi là Geass.

```text
Wide 16:9 landscape cinematic frame. a mysterious silhouette of a young woman standing in a dark warehouse beside a glowing capsule, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: C.C. trao Geass cho Lelouch qua một bản khế ước: đổi lại, cậu phải thực hiện một điều ước của cô trong tương…

```text
Wide 16:9 landscape cinematic frame. an old parchment contract with a wax seal and a single blank line awaiting a signature, close-up, dim mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Geass của Lelouch là mệnh lệnh tuyệt đối. Chỉ cần nhìn vào mắt ai đó, cậu có thể ra một lệnh, và người đó sẽ…

```text
Wide 16:9 landscape cinematic frame. a glowing eye reflected in another person's eye in extreme close-up, a faint beam of light connecting them, dramatic red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhưng có giới hạn: mỗi người chỉ bị ra lệnh được một lần, và phải có giao tiếp bằng mắt. Lelouch biến giới hạ…

```text
Wide 16:9 landscape cinematic frame. a chess board with a few pieces marked with small crossed-out eye symbols, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Lelouch có một câu nói nổi tiếng, đại ý: nếu quân vua không tự di chuyển, cấp dưới sẽ không đi theo. Cậu luôn…

```text
Wide 16:9 landscape cinematic frame. a black king piece stepping forward ahead of its pawns on a chess board, close-up, dramatic side light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Và cậu tạo ra một danh tính mới: Zero, người đeo mặt nạ, thủ lĩnh của Hiệp sĩ Đen, tổ chức kháng chiến chống…

```text
Wide 16:9 landscape cinematic frame. a long black cloak hanging on a coat stand in a dark room beside a chess king piece on a table, close-up, dramatic shadow light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: Geass không cho Lelouch sức mạnh thể chất. Nó chỉ cho cậu khả năng điều khiển người khác. Nên mọi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a marionette control bar with strings dangling, looking at it with discomfort. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Cáo trạng

Lời: Thư ký tòa đọc cáo trạng. Tội một: giết người. Ngay từ đầu, Lelouch dùng Geass để giết nhiều binh lính, và tự…

```text
Wide 16:9 landscape cinematic frame. an official indictment scroll unrolled on the bench with the first charge underlined in red ink, close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Tội hai: gây thương vong cho dân thường. Trong trận núi Narita, Lelouch cho gây một trận lở đất để tiêu diệt…

```text
Wide 16:9 landscape cinematic frame. a massive landslide pouring down a mountainside toward a small town in the valley below, wide shot, ominous grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Một trong những người chết là cha của Shirley, người bạn cùng lớp đang thầm yêu Lelouch.

```text
Wide 16:9 landscape cinematic frame. a single umbrella lying in the mud on an empty mountain road after rain, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Tội ba, nặng nhất: thảm kịch Khu Đặc khu hành chính. Công chúa Euphemia đề nghị lập một khu vực để người Nhật…

```text
Wide 16:9 landscape cinematic frame. a large open-air stadium decorated with flags and flowers, crowds gathering in hope, wide shot, bright hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Một câu nói đùa của Lelouch trở thành mệnh lệnh tuyệt đối. Euphemia, người hiền lành nhất Britannia, ra lệnh…

```text
Wide 16:9 landscape cinematic frame. the same stadium now empty with fallen flags and scattered flowers under a darkened sky, wide shot, somber grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Sau đó, Lelouch tự tay kết liễu Euphemia, và dùng chính thảm kịch này để kêu gọi người Nhật nổi dậy trong cuộ…

```text
Wide 16:9 landscape cinematic frame. a single white flower lying on a stone floor with a dark cloak's hem passing by, close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Tội bổ sung: bỏ rơi đồng đội. Giữa cuộc Phản loạn Đen, khi em gái bị bắt cóc, Lelouch rời chiến trường để đi…

```text
Wide 16:9 landscape cinematic frame. a battlefield map with many unit markers left alone while a single marker moves far away off the map's edge, parchment close-up, red ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Tội bốn: thao túng ý chí người khác. Lelouch từng ra lệnh cho Suzaku phải sống. Mệnh lệnh đó về sau buộc Suza…

```text
Wide 16:9 landscape cinematic frame. a bright flash of light blooming over a distant city skyline at night, silhouettes watching from a hill, wide shot, blinding white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Tội năm: độc tài. Ở cuối truyện, Lelouch lên ngôi hoàng đế Britannia, bắt giữ lãnh đạo các nước, và tự biến m…

```text
Wide 16:9 landscape cinematic frame. a towering throne on a high platform above a vast crowd of kneeling silhouettes, wide shot, cold imperial light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Lời bào chữa

Lời: Giờ tới luật sư bào chữa. Luận điểm một: bối cảnh. Britannia là một đế chế xâm lược, chia con người thành ngư…

```text
Wide 16:9 landscape cinematic frame. a torn identity card with a name crossed out and replaced by a number, extreme close-up, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Luận điểm hai: động cơ. Lelouch không chiến đấu vì quyền lực hay tiền bạc. Cậu chiến đấu để em gái có một thế…

```text
Wide 16:9 landscape cinematic frame. a small handwritten note on a desk reading a wish for a gentle world, with a pressed flower beside it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Luận điểm ba: thảm kịch Đặc khu là tai nạn. Geass của Lelouch mất kiểm soát, không tắt được nữa. Cậu chưa bao…

```text
Wide 16:9 landscape cinematic frame. a young figure covering one eye with a trembling hand in a dark corridor, medium shot, harsh red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Lelouch cũng từng nói một câu mà chính cậu sống theo tới cuối, đại ý: chỉ những ai sẵn sàng bị bắn mới có quy…

```text
Wide 16:9 landscape cinematic frame. a single chess king piece placed in the line of fire among pawns on a board, symbolic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Luận điểm bốn: cái giá cá nhân. Lelouch mất gần như mọi người thân: người bạn thân, người yêu thầm, đồng đội,…

```text
Wide 16:9 landscape cinematic frame. an empty student council room with chairs pushed back and a forgotten scarf on a table, wide shot, lonely afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Luận điểm năm, mạnh nhất: kế hoạch Zero Requiem. Lelouch cố ý trở thành bạo chúa để cả thế giới căm ghét mình…

```text
Wide 16:9 landscape cinematic frame. a long parade route lined with crowds, an ornate carriage at the center, and a lone masked figure leaping toward it, wide shot, dramatic bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Khi bạo chúa chết, mọi hận thù trên thế giới chết theo. Các quốc gia đoàn kết lại, chiến tranh chấm dứt. Lelo…

```text
Wide 16:9 landscape cinematic frame. a sunrise over a city where people from different nations stand together in a square, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Luật sư bào chữa hỏi bồi thẩm: một người chấp nhận chết như một kẻ ác để thế giới có hòa bình, liệu có thể bị…

```text
Wide 16:9 landscape cinematic frame. a toppled black king piece resting in the palm of an open hand, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Nhân chứng 1: Suzaku

Lời: Nhân chứng thứ nhất: Kururugi Suzaku, người bạn thân nhất và cũng là đối thủ lớn nhất của bị cáo.

```text
Wide 16:9 landscape cinematic frame. a witness stand with a folded white knight's cape draped over the railing, close-up, soft courtroom light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Suzaku tin rằng phải thay đổi hệ thống từ bên trong, bằng những cách đúng đắn. Anh gia nhập quân đội Britanni…

```text
Wide 16:9 landscape cinematic frame. a lone soldier standing at attention in a line of foreign uniforms, looking straight ahead, medium shot, cold disciplined light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Anh từng nói, đại ý: kết quả đạt được bằng cách sai trái thì không có ý nghĩa. Đây là luận điểm mạnh nhất của…

```text
Wide 16:9 landscape cinematic frame. a crossed-out shortcut path on a map beside a longer honest road drawn in careful ink, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Suzaku căm ghét Lelouch vì cái chết của Euphemia, người anh yêu quý. Nhưng cuối cùng, chính Suzaku lại là ngư…

```text
Wide 16:9 landscape cinematic frame. two silhouettes sitting back to back on a rooftop at night, not looking at each other, wide shot, cold moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và Suzaku cũng mang một bí mật: khi còn nhỏ, anh đã giết chính cha mình, thủ tướng Nhật, để ngăn một cuộc khá…

```text
Wide 16:9 landscape cinematic frame. a small child's silhouette standing alone in a traditional house at night, a sliding door half open, wide shot, heavy somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Lời khai của Suzaku vì vậy rất phức tạp. Anh vừa là người buộc tội, vừa là đồng phạm. Và cái giá của anh: phả…

```text
Wide 16:9 landscape cinematic frame. a plain mask resting on a table beside a folded letter, close-up, somber quiet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi nhận: lời khai của Suzaku không ủng hộ hẳn bên nào. Nhưng nó cho thấy Lelouch không hành động một mì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing carefully in a ledger with two columns, pausing thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Nhân chứng 2: Shirley

Lời: Nhân chứng thứ hai: Shirley Fenette, bạn cùng lớp, người yêu Lelouch.

```text
Wide 16:9 landscape cinematic frame. a school bag with a small charm hanging from it resting on the witness stand, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Cha của Shirley chết trong trận lở đất Narita do Zero gây ra. Khi biết Lelouch chính là Zero, cô đứng giữa ha…

```text
Wide 16:9 landscape cinematic frame. a girl sitting alone on a bench in the rain holding a closed umbrella, medium shot, grey melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Và Shirley chọn tha thứ. Cô nói rằng dù Lelouch có là ai, cô vẫn sẽ yêu cậu. Rồi cô mất đi, và Lelouch không…

```text
Wide 16:9 landscape cinematic frame. a single paper crane resting on a windowsill in the early morning light, close-up, gentle bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Lời khai của Shirley là một lời tha thứ từ chính nạn nhân. Phía bào chữa sẽ dùng nó. Phía buộc tội sẽ hỏi: mộ…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a paper crane on one side and an umbrella on the other, close-up, soft dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Kaku nghĩ đây là nhân chứng đau lòng nhất. Cô không bảo vệ việc Lelouch làm. Cô chỉ nói rằng con người Lelouc…

```text
Wide 16:9 landscape cinematic frame. a small pressed flower tucked into the pages of a closed school notebook, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Nhân chứng 3: Kallen

Lời: Nhân chứng thứ ba: Kallen Kozuki, phi công giỏi nhất của Hiệp sĩ Đen, người đi theo Zero từ ngày đầu.

```text
Wide 16:9 landscape cinematic frame. a pilot's helmet resting on the witness stand beside a pair of worn gloves, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Kallen tin vào Zero như tin vào một lá cờ. Nhưng khi Hiệp sĩ Đen phát hiện ra Zero dùng Geass và từng lừa dối…

```text
Wide 16:9 landscape cinematic frame. a group of silhouettes turning their backs on a lone figure standing in a dark hangar, wide shot, cold harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Kallen hỏi Lelouch: cậu có thật lòng với tôi không? Và Lelouch, để bảo vệ cô, chọn không trả lời thật.

```text
Wide 16:9 landscape cinematic frame. two silhouettes standing a few steps apart in an empty hangar, one reaching out and one turning away, medium shot, dim cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Lời khai của Kallen cho thấy một tội khác mà cáo trạng chưa ghi: lừa dối những người tin mình. Lelouch dùng n…

```text
Wide 16:9 landscape cinematic frame. a chess piece being moved by a hand while other pieces watch, symbolic close-up, cold amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Kaku để ý: Kallen là một trong số ít người mà Lelouch không bao giờ dùng Geass lên để ép theo mình. Cô đi the…

```text
Wide 16:9 landscape cinematic frame. a pilot's glove resting on a railing beside a small badge, close-up, warm steady light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Nhưng Kallen cũng là người hiểu Lelouch sâu nhất ở cuối truyện. Cô nhận ra kế hoạch của cậu, và không ngăn cả…

```text
Wide 16:9 landscape cinematic frame. a figure standing alone at a window watching a distant parade, a single tear on her cheek, back view, soft light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Nhân chứng 4: Nunnally

Lời: Nhân chứng cuối cùng: Nunnally, em gái của Lelouch, người mà mọi việc cậu làm đều hướng về.

```text
Wide 16:9 landscape cinematic frame. an empty wheelchair positioned on the witness stand with a folded blanket on its seat, close-up, soft gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Nunnally lớn lên trong vòng tay che chở của anh. Nhưng cô không muốn một thế giới được xây bằng máu vì mình.…

```text
Wide 16:9 landscape cinematic frame. a small pair of hands folding a paper crane carefully in a sunlit room, close-up, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Khi biết anh mình là Zero, cô đau đớn. Khi anh trở thành hoàng đế độc tài, cô đứng ở phía chống lại anh.

```text
Wide 16:9 landscape cinematic frame. two chess pieces of different colors placed on opposite ends of a chess board, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Và ở giây phút cuối, khi chạm vào tay anh, Nunnally nhìn thấy sự thật về Zero Requiem. Cô khóc và nói: anh ơi…

```text
Wide 16:9 landscape cinematic frame. a small hand holding a larger hand that is slowly slipping away, extreme close-up, soft tearful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Và cô cũng là người duy nhất trong truyện dám đứng trước anh mình, ở phía đối lập, để nói rằng anh sai. Tình…

```text
Wide 16:9 landscape cinematic frame. two figures facing each other across a wide empty hall, one seated and one standing, wide shot, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Lời khai của Nunnally không trả lời Lelouch có tội hay không. Nó trả lời một câu hỏi khác: Lelouch có yêu thư…

```text
Wide 16:9 landscape cinematic frame. a paper crane resting on a gravestone with fresh flowers beside it, close-up, gentle morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là cảnh khiến nhiều người xem nhớ mãi. Không có tiếng nổ, không có trận đánh. Chỉ có một người…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quietly closing the ledger and placing its quill down, eyes lowered. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Luận điểm cuối của công tố

Lời: Phía buộc tội tổng kết. Một: Lelouch đã giết, trực tiếp và gián tiếp, rất nhiều người, trong đó có dân thường…

```text
Wide 16:9 landscape cinematic frame. a long list of names written on parchment fading into the distance, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Hai: cậu điều khiển ý chí người khác, tước đi quyền tự quyết định, thứ cơ bản nhất của con người.

```text
Wide 16:9 landscape cinematic frame. a set of marionette strings hanging from above over an empty stage, close-up, cold dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Ba: một kết thúc tốt đẹp không biện minh được cho mọi phương tiện. Nếu chấp nhận điều đó, bất kỳ ai cũng có t…

```text
Wide 16:9 landscape cinematic frame. a long road paved with dark stones leading toward a bright horizon, symbolic wide shot, uneasy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Phía buộc tội còn nhấn mạnh: Zero Requiem là quyết định của hai người, nhưng số phận của cả thế giới bị đặt v…

```text
Wide 16:9 landscape cinematic frame. a globe on a desk with two small chess pieces placed on top of it, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Và bốn: Lelouch tự chọn cái chết, nhưng những người đã chết vì cậu thì không được chọn.

```text
Wide 16:9 landscape cinematic frame. a row of empty chairs in a quiet memorial hall with candles on each seat, wide shot, solemn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Luận điểm cuối của bào chữa

Lời: Phía bào chữa tổng kết. Một: Lelouch sinh ra trong một thế giới đã bạo lực từ trước. Cậu không tạo ra chiến t…

```text
Wide 16:9 landscape cinematic frame. a child's toy lying in the rubble of a bombed town, close-up, grey somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hai: những tội nặng nhất có yếu tố tai nạn. Cậu không muốn thảm kịch Đặc khu xảy ra.

```text
Wide 16:9 landscape cinematic frame. a shattered pocket watch lying on a stone floor, its hands frozen, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Ba: cậu không nhận lấy bất cứ lợi ích nào. Cậu kết thúc bằng cách tự trừng phạt mình, trước cả khi có tòa án…

```text
Wide 16:9 landscape cinematic frame. an empty throne with a crown resting on the floor beside it, wide shot, quiet melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và năm: sau cái chết của Lelouch, Suzaku tiếp tục làm Zero để bảo vệ hòa bình, còn Nunnally trở thành người d…

```text
Wide 16:9 landscape cinematic frame. a gentle figure in a sunlit hall surrounded by representatives of many nations, a masked guardian standing quietly behind, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và bốn: thế giới sau cái chết của Lelouch là một thế giới hòa bình hơn. Chính những người từng bị áp bức được…

```text
Wide 16:9 landscape cinematic frame. children from different backgrounds playing together in a peaceful park at sunset, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Góc nhìn của Kaku

Lời: Kaku không tuyên án, nhưng Kaku muốn chỉ ra câu hỏi thật sự của Code Geass: mục đích có biện minh cho phương…

```text
Wide 16:9 landscape cinematic frame. a notebook page with two words written at each end of a long arrow, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Lelouch trả lời là có, và cậu trả giá bằng cả mạng sống. Suzaku trả lời là không, nhưng cuối cùng cũng đồng h…

```text
Wide 16:9 landscape cinematic frame. two paths merging into one on a hillside at dusk, back view of two figures walking together, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Câu hỏi này cũng là một câu hỏi triết học rất cũ ngoài đời: có nên hy sinh một số người để cứu nhiều người hơ…

```text
Wide 16:9 landscape cinematic frame. an old philosophy book open to a page with a simple diagram of a forked railway track, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Kaku nghĩ Code Geass hay chính vì nó không để Lelouch hoàn toàn vô tội, cũng không để cậu hoàn toàn đáng ghét…

```text
Wide 16:9 landscape cinematic frame. a chess piece that is half white and half black standing alone on a board, close-up, dramatic split light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Bồi thẩm bỏ phiếu

Lời: Giờ tới lượt bạn. Có ba lựa chọn. Một: có tội. Những gì Lelouch làm không thể biện minh, dù kết quả là gì.

```text
Wide 16:9 landscape cinematic frame. a ballot paper with three checkboxes and the first one highlighted, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Hai: vô tội. Trong hoàn cảnh đó, Lelouch đã làm điều cần làm, và tự trả giá bằng mạng sống.

```text
Wide 16:9 landscape cinematic frame. the same ballot with the second checkbox highlighted, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Ba: có tội, nhưng được khoan hồng. Lelouch phạm tội, nhưng động cơ và sự hy sinh của cậu cần được tính tới.

```text
Wide 16:9 landscape cinematic frame. the same ballot with the third checkbox highlighted, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Viết số một, hai hay ba vào bình luận, kèm một câu lý do. Kaku sẽ tổng hợp kết quả phiên tòa ở một video sau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding the ballot box out toward the viewer with an encouraging nod. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · Kết

Lời: Lelouch bắt đầu câu chuyện bằng một lời thề phá hủy thế giới, và kết thúc bằng việc để thế giới phá hủy mình.…

```text
Wide 16:9 landscape cinematic frame. a chess board at sunset with the black king lying down and all other pieces standing in a circle around it, close-up, golden bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Video tiếp theo, Kaku quay về biển Đông, đúng lúc bản làm lại One Piece ra mắt: những chi tiết cài cắm trong…

```text
Wide 16:9 landscape cinematic frame. an old wide-brimmed hat resting on a small wooden boat at a quiet harbor at dawn, close-up, fresh morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những phiên tòa như thế này, hãy đăng ký kênh, và cho Kaku biết bị cáo tiếp theo bạn muốn đưa r…

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping a tiny gavel once on the bench and bowing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Khai mạc phiên tòa

Khoảng 80 giây · cảnh s01–s07 · 1036 ký tự

**Gemini**

```text
Cảnh báo: video này có spoiler toàn bộ Code Geass, cả mùa một, mùa hai, và cái kết. Nếu bạn chưa xem hết, hãy lưu video lại. Cái kết của Code Geass là một trong những cái kết đáng xem nhất lịch sử anime.

<short pause> Bị cáo: Lelouch vi Britannia, còn được biết với cái tên Zero. Tội danh: giết người, gây chiến tranh, thao túng ý chí người khác, và tự lập làm hoàng đế độc tài của cả thế giới.

<short pause> Nhưng cũng chính người này đã chấm dứt một đế chế xâm lược, giải phóng nhiều quốc gia, và kết thúc chiến tranh trên toàn thế giới. Bằng cái chết của chính mình.

<short pause> Người anh hùng hay kẻ ác? Kẻ giải phóng hay kẻ độc tài? Đó là câu hỏi mà người xem Code Geass đã tranh luận gần hai mươi năm.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku lại làm thư ký tòa: đọc cáo trạng, ghi lời bào chữa, gọi nhân chứng. Mọi nhân chứng là chi tiết có thật trong phim.

<short pause> Và như mọi phiên tòa của kênh, Kaku không tuyên án. Bạn là bồi thẩm. Cuối video, Kaku mời bạn bỏ phiếu.

<short pause> Một lưu ý: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh cho bạo lực ngoài đời.
```

**ElevenLabs**

```text
Cảnh báo: video này có spoiler toàn bộ Code Geass, cả mùa một, mùa hai, và cái kết. Nếu bạn chưa xem hết, hãy lưu video lại. Cái kết của Code Geass là một trong những cái kết đáng xem nhất lịch sử anime.

[pause] Bị cáo: Lelouch vi Britannia, còn được biết với cái tên Zero. Tội danh: giết người, gây chiến tranh, thao túng ý chí người khác, và tự lập làm hoàng đế độc tài của cả thế giới.

[pause] Nhưng cũng chính người này đã chấm dứt một đế chế xâm lược, giải phóng nhiều quốc gia, và kết thúc chiến tranh trên toàn thế giới. Bằng cái chết của chính mình.

[pause] [curious] Người anh hùng hay kẻ ác? Kẻ giải phóng hay kẻ độc tài? Đó là câu hỏi mà người xem Code Geass đã tranh luận gần hai mươi năm.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku lại làm thư ký tòa: đọc cáo trạng, ghi lời bào chữa, gọi nhân chứng. Mọi nhân chứng là chi tiết có thật trong phim.

[pause] Và như mọi phiên tòa của kênh, Kaku không tuyên án. Bạn là bồi thẩm. Cuối video, Kaku mời bạn bỏ phiếu.

[pause] Một lưu ý: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh cho bạo lực ngoài đời.
```

### c02 · Hồ sơ bị cáo

Khoảng 78 giây · cảnh s08–s14 · 1008 ký tự

**Gemini**

```text
Code Geass là anime gốc của studio Sunrise, mùa một phát năm 2006, mùa hai năm 2008. Đạo diễn là Taniguchi Goro, kịch bản của Okouchi Ichiro.

<short pause> Bối cảnh là một thế giới giả tưởng, nơi đế quốc Britannia hùng mạnh xâm chiếm nhiều quốc gia. Nhật Bản bị chiếm, đổi tên thành Khu vực 11, người Nhật bị gọi là Eleven.

<short pause> Lelouch là một hoàng tử Britannia. Khi còn nhỏ, mẹ cậu bị ám sát ngay trong cung điện. Em gái Nunnally bị mất thị lực và không thể đi lại.

<short pause> Khi Lelouch chất vấn cha mình, hoàng đế, về cái chết của mẹ, ông gửi cả hai anh em sang Nhật làm con tin chính trị. Không lâu sau, Britannia tấn công chính nước Nhật.

<short pause> Lelouch lớn lên dưới tên giả Lelouch Lamperouge, một học sinh thông minh, giỏi cờ vua, sống ẩn mình ở Khu vực 11 cùng em gái.

<short pause> Cậu có hai mục tiêu: tìm ra kẻ đã giết mẹ, và tạo ra một thế giới hiền hòa để em gái được sống yên ổn. Và để làm được, cậu cần phá hủy Britannia.

<short pause> Bạn thân nhất của Lelouch từ thuở nhỏ là Suzaku, một người Nhật. Hai người sẽ gặp lại nhau ở hai phía đối lập của chiến tranh.
```

**ElevenLabs**

```text
Code Geass là anime gốc của studio Sunrise, mùa một phát năm 2006, mùa hai năm 2008. Đạo diễn là Taniguchi Goro, kịch bản của Okouchi Ichiro.

[pause] Bối cảnh là một thế giới giả tưởng, nơi đế quốc Britannia hùng mạnh xâm chiếm nhiều quốc gia. Nhật Bản bị chiếm, đổi tên thành Khu vực 11, người Nhật bị gọi là Eleven.

[pause] Lelouch là một hoàng tử Britannia. Khi còn nhỏ, mẹ cậu bị ám sát ngay trong cung điện. Em gái Nunnally bị mất thị lực và không thể đi lại.

[pause] Khi Lelouch chất vấn cha mình, hoàng đế, về cái chết của mẹ, ông gửi cả hai anh em sang Nhật làm con tin chính trị. Không lâu sau, Britannia tấn công chính nước Nhật.

[pause] Lelouch lớn lên dưới tên giả Lelouch Lamperouge, một học sinh thông minh, giỏi cờ vua, sống ẩn mình ở Khu vực 11 cùng em gái.

[pause] Cậu có hai mục tiêu: tìm ra kẻ đã giết mẹ, và tạo ra một thế giới hiền hòa để em gái được sống yên ổn. Và để làm được, cậu cần phá hủy Britannia.

[pause] Bạn thân nhất của Lelouch từ thuở nhỏ là Suzaku, một người Nhật. Hai người sẽ gặp lại nhau ở hai phía đối lập của chiến tranh.
```

### c03 · Vũ khí của bị cáo: Geass

Khoảng 78 giây · cảnh s15–s21 · 1016 ký tự

**Gemini**

```text
Tất cả thay đổi khi Lelouch gặp một cô gái bí ẩn, C.C., và nhận được một năng lực gọi là Geass.

<short pause> C.C. trao Geass cho Lelouch qua một bản khế ước: đổi lại, cậu phải thực hiện một điều ước của cô trong tương lai. Điều ước đó là gì, bộ phim giữ bí mật tới gần cuối.

<short pause> Geass của Lelouch là mệnh lệnh tuyệt đối. Chỉ cần nhìn vào mắt ai đó, cậu có thể ra một lệnh, và người đó sẽ làm theo, không thể cưỡng lại.

<short pause> Nhưng có giới hạn: mỗi người chỉ bị ra lệnh được một lần, và phải có giao tiếp bằng mắt. Lelouch biến giới hạn này thành một trò chơi chiến lược.

<short pause> Lelouch có một câu nói nổi tiếng, đại ý: nếu quân vua không tự di chuyển, cấp dưới sẽ không đi theo. Cậu luôn tự đứng ở tuyến đầu kế hoạch của mình.

<short pause> Và cậu tạo ra một danh tính mới: Zero, người đeo mặt nạ, thủ lĩnh của Hiệp sĩ Đen, tổ chức kháng chiến chống lại Britannia.

<short pause> <laugh> Kaku để ý: Geass không cho Lelouch sức mạnh thể chất. Nó chỉ cho cậu khả năng điều khiển người khác. Nên mọi tội trong cáo trạng đều liên quan tới một câu hỏi: cậu có quyền điều khiển người khác không?
```

**ElevenLabs**

```text
Tất cả thay đổi khi Lelouch gặp một cô gái bí ẩn, C.C., và nhận được một năng lực gọi là Geass.

[pause] C.C. trao Geass cho Lelouch qua một bản khế ước: đổi lại, cậu phải thực hiện một điều ước của cô trong tương lai. Điều ước đó là gì, bộ phim giữ bí mật tới gần cuối.

[pause] Geass của Lelouch là mệnh lệnh tuyệt đối. Chỉ cần nhìn vào mắt ai đó, cậu có thể ra một lệnh, và người đó sẽ làm theo, không thể cưỡng lại.

[pause] Nhưng có giới hạn: mỗi người chỉ bị ra lệnh được một lần, và phải có giao tiếp bằng mắt. Lelouch biến giới hạn này thành một trò chơi chiến lược.

[pause] Lelouch có một câu nói nổi tiếng, đại ý: nếu quân vua không tự di chuyển, cấp dưới sẽ không đi theo. Cậu luôn tự đứng ở tuyến đầu kế hoạch của mình.

[pause] Và cậu tạo ra một danh tính mới: Zero, người đeo mặt nạ, thủ lĩnh của Hiệp sĩ Đen, tổ chức kháng chiến chống lại Britannia.

[pause] [chuckles] Kaku để ý: Geass không cho Lelouch sức mạnh thể chất. Nó chỉ cho cậu khả năng điều khiển người khác. [curious] Nên mọi tội trong cáo trạng đều liên quan tới một câu hỏi: cậu có quyền điều khiển người khác không?
```

### c04 · Cáo trạng

Khoảng 109 giây · cảnh s22–s30 · 1423 ký tự

**Gemini**

```text
Thư ký tòa đọc cáo trạng. Tội một: giết người. Ngay từ đầu, Lelouch dùng Geass để giết nhiều binh lính, và tự tay giết anh cùng cha khác mẹ, hoàng tử Clovis, người cai quản Khu vực 11.

<short pause> Tội hai: gây thương vong cho dân thường. Trong trận núi Narita, Lelouch cho gây một trận lở đất để tiêu diệt quân Britannia. Trận lở đất cũng cướp đi mạng sống của nhiều người không liên quan.

<short pause> Một trong những người chết là cha của Shirley, người bạn cùng lớp đang thầm yêu Lelouch.

<short pause> Tội ba, nặng nhất: thảm kịch Khu Đặc khu hành chính. Công chúa Euphemia đề nghị lập một khu vực để người Nhật được sống tự do. Lelouch đồng ý. <short pause> Nhưng Geass của cậu mất kiểm soát.

<short pause> Một câu nói đùa của Lelouch trở thành mệnh lệnh tuyệt đối. Euphemia, người hiền lành nhất Britannia, ra lệnh tàn sát chính những người Nhật cô muốn bảo vệ. Kaku không mô tả thêm.

<short pause> Sau đó, Lelouch tự tay kết liễu Euphemia, và dùng chính thảm kịch này để kêu gọi người Nhật nổi dậy trong cuộc Phản loạn Đen.

<short pause> Tội bổ sung: bỏ rơi đồng đội. Giữa cuộc Phản loạn Đen, khi em gái bị bắt cóc, Lelouch rời chiến trường để đi cứu Nunnally. Hiệp sĩ Đen mất chỉ huy và thất bại.

<short pause> Tội bốn: thao túng ý chí người khác. Lelouch từng ra lệnh cho Suzaku phải sống. Mệnh lệnh đó về sau buộc Suzaku phóng một vũ khí hủy diệt xuống thủ đô, gây thương vong cực lớn.

<short pause> Tội năm: độc tài. Ở cuối truyện, Lelouch lên ngôi hoàng đế Britannia, bắt giữ lãnh đạo các nước, và tự biến mình thành bạo chúa của cả thế giới.
```

**ElevenLabs**

```text
Thư ký tòa đọc cáo trạng. Tội một: giết người. Ngay từ đầu, Lelouch dùng Geass để giết nhiều binh lính, và tự tay giết anh cùng cha khác mẹ, hoàng tử Clovis, người cai quản Khu vực 11.

[pause] Tội hai: gây thương vong cho dân thường. Trong trận núi Narita, Lelouch cho gây một trận lở đất để tiêu diệt quân Britannia. Trận lở đất cũng cướp đi mạng sống của nhiều người không liên quan.

[pause] Một trong những người chết là cha của Shirley, người bạn cùng lớp đang thầm yêu Lelouch.

[pause] Tội ba, nặng nhất: thảm kịch Khu Đặc khu hành chính. Công chúa Euphemia đề nghị lập một khu vực để người Nhật được sống tự do. Lelouch đồng ý. [pause] Nhưng Geass của cậu mất kiểm soát.

[pause] Một câu nói đùa của Lelouch trở thành mệnh lệnh tuyệt đối. Euphemia, người hiền lành nhất Britannia, ra lệnh tàn sát chính những người Nhật cô muốn bảo vệ. Kaku không mô tả thêm.

[pause] Sau đó, Lelouch tự tay kết liễu Euphemia, và dùng chính thảm kịch này để kêu gọi người Nhật nổi dậy trong cuộc Phản loạn Đen.

[pause] Tội bổ sung: bỏ rơi đồng đội. Giữa cuộc Phản loạn Đen, khi em gái bị bắt cóc, Lelouch rời chiến trường để đi cứu Nunnally. Hiệp sĩ Đen mất chỉ huy và thất bại.

[pause] Tội bốn: thao túng ý chí người khác. Lelouch từng ra lệnh cho Suzaku phải sống. Mệnh lệnh đó về sau buộc Suzaku phóng một vũ khí hủy diệt xuống thủ đô, gây thương vong cực lớn.

[pause] Tội năm: độc tài. Ở cuối truyện, Lelouch lên ngôi hoàng đế Britannia, bắt giữ lãnh đạo các nước, và tự biến mình thành bạo chúa của cả thế giới.
```

### c05 · Lời bào chữa

Khoảng 100 giây · cảnh s31–s38 · 1301 ký tự

**Gemini**

```text
Giờ tới luật sư bào chữa. Luận điểm một: bối cảnh. Britannia là một đế chế xâm lược, chia con người thành người Britannia và người số. Người Nhật bị tước cả tên gọi.

<short pause> Luận điểm hai: động cơ. Lelouch không chiến đấu vì quyền lực hay tiền bạc. Cậu chiến đấu để em gái có một thế giới hiền hòa, và để người bị áp bức được tự do.

<short pause> Luận điểm ba: thảm kịch Đặc khu là tai nạn. Geass của Lelouch mất kiểm soát, không tắt được nữa. Cậu chưa bao giờ muốn Euphemia làm điều đó, và cậu đau đớn vì nó.

<short pause> Lelouch cũng từng nói một câu mà chính cậu sống theo tới cuối, đại ý: chỉ những ai sẵn sàng bị bắn mới có quyền bắn. Cậu không bao giờ đứng ngoài cái giá mà mình đặt ra cho người khác.

<short pause> Luận điểm bốn: cái giá cá nhân. Lelouch mất gần như mọi người thân: người bạn thân, người yêu thầm, đồng đội, thậm chí cả tình yêu của em gái trong một thời gian.

<short pause> Luận điểm năm, mạnh nhất: kế hoạch Zero Requiem. Lelouch cố ý trở thành bạo chúa để cả thế giới căm ghét mình. Rồi cậu để Suzaku, trong vai Zero, giết mình trước mặt mọi người.

<short pause> Khi bạo chúa chết, mọi hận thù trên thế giới chết theo. Các quốc gia đoàn kết lại, chiến tranh chấm dứt. Lelouch mang theo mọi tội lỗi, để thế giới được bắt đầu lại.

<short pause> Luật sư bào chữa hỏi bồi thẩm: một người chấp nhận chết như một kẻ ác để thế giới có hòa bình, liệu có thể bị coi là kẻ ác không?
```

**ElevenLabs**

```text
Giờ tới luật sư bào chữa. Luận điểm một: bối cảnh. Britannia là một đế chế xâm lược, chia con người thành người Britannia và người số. Người Nhật bị tước cả tên gọi.

[pause] Luận điểm hai: động cơ. Lelouch không chiến đấu vì quyền lực hay tiền bạc. Cậu chiến đấu để em gái có một thế giới hiền hòa, và để người bị áp bức được tự do.

[pause] Luận điểm ba: thảm kịch Đặc khu là tai nạn. Geass của Lelouch mất kiểm soát, không tắt được nữa. Cậu chưa bao giờ muốn Euphemia làm điều đó, và cậu đau đớn vì nó.

[pause] Lelouch cũng từng nói một câu mà chính cậu sống theo tới cuối, đại ý: chỉ những ai sẵn sàng bị bắn mới có quyền bắn. Cậu không bao giờ đứng ngoài cái giá mà mình đặt ra cho người khác.

[pause] Luận điểm bốn: cái giá cá nhân. Lelouch mất gần như mọi người thân: người bạn thân, người yêu thầm, đồng đội, thậm chí cả tình yêu của em gái trong một thời gian.

[pause] Luận điểm năm, mạnh nhất: kế hoạch Zero Requiem. Lelouch cố ý trở thành bạo chúa để cả thế giới căm ghét mình. Rồi cậu để Suzaku, trong vai Zero, giết mình trước mặt mọi người.

[pause] Khi bạo chúa chết, mọi hận thù trên thế giới chết theo. Các quốc gia đoàn kết lại, chiến tranh chấm dứt. Lelouch mang theo mọi tội lỗi, để thế giới được bắt đầu lại.

[pause] [curious] Luật sư bào chữa hỏi bồi thẩm: một người chấp nhận chết như một kẻ ác để thế giới có hòa bình, liệu có thể bị coi là kẻ ác không?
```

### c06 · Nhân chứng 1: Suzaku / Nhân chứng 2: Shirley

Khoảng 127 giây · cảnh s39–s50 · 1652 ký tự

**Gemini**

```text
Nhân chứng thứ nhất: Kururugi Suzaku, người bạn thân nhất và cũng là đối thủ lớn nhất của bị cáo.

<short pause> Suzaku tin rằng phải thay đổi hệ thống từ bên trong, bằng những cách đúng đắn. Anh gia nhập quân đội Britannia, dù là người Nhật, và phản đối mọi cách làm của Zero.

<short pause> Anh từng nói, đại ý: kết quả đạt được bằng cách sai trái thì không có ý nghĩa. Đây là luận điểm mạnh nhất của phía buộc tội.

<short pause> Suzaku căm ghét Lelouch vì cái chết của Euphemia, người anh yêu quý. <short pause> Nhưng cuối cùng, chính Suzaku lại là người cùng Lelouch thực hiện Zero Requiem.

<short pause> Và Suzaku cũng mang một bí mật: khi còn nhỏ, anh đã giết chính cha mình, thủ tướng Nhật, để ngăn một cuộc kháng chiến vô vọng. Anh cũng từng dùng cách sai để đạt kết quả mình tin là đúng.

<short pause> Lời khai của Suzaku vì vậy rất phức tạp. Anh vừa là người buộc tội, vừa là đồng phạm. Và cái giá của anh: phải sống tiếp dưới mặt nạ Zero, không bao giờ được là chính mình.

<short pause> <laugh> Kaku ghi nhận: lời khai của Suzaku không ủng hộ hẳn bên nào. <short pause> Nhưng nó cho thấy Lelouch không hành động một mình trong phần cuối.

<short pause> Nhân chứng thứ hai: Shirley Fenette, bạn cùng lớp, người yêu Lelouch.

<short pause> Cha của Shirley chết trong trận lở đất Narita do Zero gây ra. Khi biết Lelouch chính là Zero, cô đứng giữa hai cảm xúc: đau khổ vì cha, và tình cảm với Lelouch.

<short pause> Và Shirley chọn tha thứ. Cô nói rằng dù Lelouch có là ai, cô vẫn sẽ yêu cậu. Rồi cô mất đi, và Lelouch không thể cứu cô.

<short pause> Lời khai của Shirley là một lời tha thứ từ chính nạn nhân. Phía bào chữa sẽ dùng nó. Phía buộc tội sẽ hỏi: một người tha thứ có xóa được tội không?

<short pause> Kaku nghĩ đây là nhân chứng đau lòng nhất. Cô không bảo vệ việc Lelouch làm. Cô chỉ nói rằng con người Lelouch vẫn đáng được yêu thương.
```

**ElevenLabs**

```text
Nhân chứng thứ nhất: Kururugi Suzaku, người bạn thân nhất và cũng là đối thủ lớn nhất của bị cáo.

[pause] Suzaku tin rằng phải thay đổi hệ thống từ bên trong, bằng những cách đúng đắn. Anh gia nhập quân đội Britannia, dù là người Nhật, và phản đối mọi cách làm của Zero.

[pause] Anh từng nói, đại ý: kết quả đạt được bằng cách sai trái thì không có ý nghĩa. Đây là luận điểm mạnh nhất của phía buộc tội.

[pause] Suzaku căm ghét Lelouch vì cái chết của Euphemia, người anh yêu quý. [pause] Nhưng cuối cùng, chính Suzaku lại là người cùng Lelouch thực hiện Zero Requiem.

[pause] Và Suzaku cũng mang một bí mật: khi còn nhỏ, anh đã giết chính cha mình, thủ tướng Nhật, để ngăn một cuộc kháng chiến vô vọng. Anh cũng từng dùng cách sai để đạt kết quả mình tin là đúng.

[pause] Lời khai của Suzaku vì vậy rất phức tạp. Anh vừa là người buộc tội, vừa là đồng phạm. Và cái giá của anh: phải sống tiếp dưới mặt nạ Zero, không bao giờ được là chính mình.

[pause] [chuckles] Kaku ghi nhận: lời khai của Suzaku không ủng hộ hẳn bên nào. [pause] Nhưng nó cho thấy Lelouch không hành động một mình trong phần cuối.

[pause] Nhân chứng thứ hai: Shirley Fenette, bạn cùng lớp, người yêu Lelouch.

[pause] Cha của Shirley chết trong trận lở đất Narita do Zero gây ra. Khi biết Lelouch chính là Zero, cô đứng giữa hai cảm xúc: đau khổ vì cha, và tình cảm với Lelouch.

[pause] Và Shirley chọn tha thứ. Cô nói rằng dù Lelouch có là ai, cô vẫn sẽ yêu cậu. Rồi cô mất đi, và Lelouch không thể cứu cô.

[pause] Lời khai của Shirley là một lời tha thứ từ chính nạn nhân. Phía bào chữa sẽ dùng nó. [curious] Phía buộc tội sẽ hỏi: một người tha thứ có xóa được tội không?

[pause] Kaku nghĩ đây là nhân chứng đau lòng nhất. Cô không bảo vệ việc Lelouch làm. Cô chỉ nói rằng con người Lelouch vẫn đáng được yêu thương.
```

### c07 · Nhân chứng 3: Kallen / Nhân chứng 4: Nunnally

Khoảng 128 giây · cảnh s51–s63 · 1658 ký tự

**Gemini**

```text
Nhân chứng thứ ba: Kallen Kozuki, phi công giỏi nhất của Hiệp sĩ Đen, người đi theo Zero từ ngày đầu.

<short pause> Kallen tin vào Zero như tin vào một lá cờ. <short pause> Nhưng khi Hiệp sĩ Đen phát hiện ra Zero dùng Geass và từng lừa dối họ, cả tổ chức quay lưng với Lelouch.

<short pause> Kallen hỏi Lelouch: cậu có thật lòng với tôi không? Và Lelouch, để bảo vệ cô, chọn không trả lời thật.

<short pause> Lời khai của Kallen cho thấy một tội khác mà cáo trạng chưa ghi: lừa dối những người tin mình. Lelouch dùng niềm tin của người khác như những quân cờ.

<short pause> Kaku để ý: Kallen là một trong số ít người mà Lelouch không bao giờ dùng Geass lên để ép theo mình. Cô đi theo Zero bằng ý chí của chính mình.

<short pause> Nhưng Kallen cũng là người hiểu Lelouch sâu nhất ở cuối truyện. Cô nhận ra kế hoạch của cậu, và không ngăn cản.

<short pause> Nhân chứng cuối cùng: Nunnally, em gái của Lelouch, người mà mọi việc cậu làm đều hướng về.

<short pause> Nunnally lớn lên trong vòng tay che chở của anh. <short pause> Nhưng cô không muốn một thế giới được xây bằng máu vì mình. Cô muốn thay đổi thế giới bằng cách hiền hòa.

<short pause> Khi biết anh mình là Zero, cô đau đớn. Khi anh trở thành hoàng đế độc tài, cô đứng ở phía chống lại anh.

<short pause> Và ở giây phút cuối, khi chạm vào tay anh, Nunnally nhìn thấy sự thật về Zero Requiem. Cô khóc và nói: anh ơi, em yêu anh.

<short pause> Và cô cũng là người duy nhất trong truyện dám đứng trước anh mình, ở phía đối lập, để nói rằng anh sai. Tình yêu của cô không phải là sự đồng ý.

<short pause> Lời khai của Nunnally không trả lời Lelouch có tội hay không. Nó trả lời một câu hỏi khác: Lelouch có yêu thương thật không. Và câu trả lời là có.

<short pause> <laugh> Kaku thấy đây là cảnh khiến nhiều người xem nhớ mãi. Không có tiếng nổ, không có trận đánh. Chỉ có một người em hiểu ra mọi thứ khi đã quá muộn.
```

**ElevenLabs**

```text
Nhân chứng thứ ba: Kallen Kozuki, phi công giỏi nhất của Hiệp sĩ Đen, người đi theo Zero từ ngày đầu.

[pause] Kallen tin vào Zero như tin vào một lá cờ. [pause] Nhưng khi Hiệp sĩ Đen phát hiện ra Zero dùng Geass và từng lừa dối họ, cả tổ chức quay lưng với Lelouch.

[pause] [curious] Kallen hỏi Lelouch: cậu có thật lòng với tôi không? Và Lelouch, để bảo vệ cô, chọn không trả lời thật.

[pause] Lời khai của Kallen cho thấy một tội khác mà cáo trạng chưa ghi: lừa dối những người tin mình. Lelouch dùng niềm tin của người khác như những quân cờ.

[pause] Kaku để ý: Kallen là một trong số ít người mà Lelouch không bao giờ dùng Geass lên để ép theo mình. Cô đi theo Zero bằng ý chí của chính mình.

[pause] Nhưng Kallen cũng là người hiểu Lelouch sâu nhất ở cuối truyện. Cô nhận ra kế hoạch của cậu, và không ngăn cản.

[pause] Nhân chứng cuối cùng: Nunnally, em gái của Lelouch, người mà mọi việc cậu làm đều hướng về.

[pause] Nunnally lớn lên trong vòng tay che chở của anh. [pause] Nhưng cô không muốn một thế giới được xây bằng máu vì mình. Cô muốn thay đổi thế giới bằng cách hiền hòa.

[pause] Khi biết anh mình là Zero, cô đau đớn. Khi anh trở thành hoàng đế độc tài, cô đứng ở phía chống lại anh.

[pause] Và ở giây phút cuối, khi chạm vào tay anh, Nunnally nhìn thấy sự thật về Zero Requiem. Cô khóc và nói: anh ơi, em yêu anh.

[pause] Và cô cũng là người duy nhất trong truyện dám đứng trước anh mình, ở phía đối lập, để nói rằng anh sai. Tình yêu của cô không phải là sự đồng ý.

[pause] Lời khai của Nunnally không trả lời Lelouch có tội hay không. Nó trả lời một câu hỏi khác: Lelouch có yêu thương thật không. Và câu trả lời là có.

[pause] [chuckles] Kaku thấy đây là cảnh khiến nhiều người xem nhớ mãi. Không có tiếng nổ, không có trận đánh. Chỉ có một người em hiểu ra mọi thứ khi đã quá muộn.
```

### c08 · Luận điểm cuối của công tố / Luận điểm cuối của bào chữa / Góc nhìn của Kaku

Khoảng 144 giây · cảnh s64–s77 · 1868 ký tự

**Gemini**

```text
Phía buộc tội tổng kết. Một: Lelouch đã giết, trực tiếp và gián tiếp, rất nhiều người, trong đó có dân thường vô tội.

<short pause> Hai: cậu điều khiển ý chí người khác, tước đi quyền tự quyết định, thứ cơ bản nhất của con người.

<short pause> Ba: một kết thúc tốt đẹp không biện minh được cho mọi phương tiện. Nếu chấp nhận điều đó, bất kỳ ai cũng có thể làm điều ác và nói rằng đó là vì hòa bình.

<short pause> Phía buộc tội còn nhấn mạnh: Zero Requiem là quyết định của hai người, nhưng số phận của cả thế giới bị đặt vào kế hoạch đó mà không ai được hỏi ý kiến.

<short pause> Và bốn: Lelouch tự chọn cái chết, nhưng những người đã chết vì cậu thì không được chọn.

<short pause> Phía bào chữa tổng kết. Một: Lelouch sinh ra trong một thế giới đã bạo lực từ trước. Cậu không tạo ra chiến tranh, cậu tìm cách chấm dứt nó.

<short pause> Hai: những tội nặng nhất có yếu tố tai nạn. Cậu không muốn thảm kịch Đặc khu xảy ra.

<short pause> Ba: cậu không nhận lấy bất cứ lợi ích nào. Cậu kết thúc bằng cách tự trừng phạt mình, trước cả khi có tòa án nào.

<short pause> Và năm: sau cái chết của Lelouch, Suzaku tiếp tục làm Zero để bảo vệ hòa bình, còn Nunnally trở thành người dẫn dắt Britannia theo cách hiền hòa. Đúng như mong ước ban đầu của Lelouch.

<short pause> Và bốn: thế giới sau cái chết của Lelouch là một thế giới hòa bình hơn. Chính những người từng bị áp bức được sống tự do.

<short pause> Kaku không tuyên án, nhưng Kaku muốn chỉ ra câu hỏi thật sự của Code Geass: mục đích có biện minh cho phương tiện không?

<short pause> Lelouch trả lời là có, và cậu trả giá bằng cả mạng sống. Suzaku trả lời là không, nhưng cuối cùng cũng đồng hành với Lelouch. Bộ phim không cho ta một câu trả lời dễ dàng.

<short pause> Câu hỏi này cũng là một câu hỏi triết học rất cũ ngoài đời: có nên hy sinh một số người để cứu nhiều người hơn không? Người ta đã tranh luận về nó hàng trăm năm mà chưa có câu trả lời chung.

<short pause> Kaku nghĩ Code Geass hay chính vì nó không để Lelouch hoàn toàn vô tội, cũng không để cậu hoàn toàn đáng ghét. Nó bắt ta phải tự suy nghĩ.
```

**ElevenLabs**

```text
Phía buộc tội tổng kết. Một: Lelouch đã giết, trực tiếp và gián tiếp, rất nhiều người, trong đó có dân thường vô tội.

[pause] Hai: cậu điều khiển ý chí người khác, tước đi quyền tự quyết định, thứ cơ bản nhất của con người.

[pause] Ba: một kết thúc tốt đẹp không biện minh được cho mọi phương tiện. Nếu chấp nhận điều đó, bất kỳ ai cũng có thể làm điều ác và nói rằng đó là vì hòa bình.

[pause] Phía buộc tội còn nhấn mạnh: Zero Requiem là quyết định của hai người, nhưng số phận của cả thế giới bị đặt vào kế hoạch đó mà không ai được hỏi ý kiến.

[pause] Và bốn: Lelouch tự chọn cái chết, nhưng những người đã chết vì cậu thì không được chọn.

[pause] Phía bào chữa tổng kết. Một: Lelouch sinh ra trong một thế giới đã bạo lực từ trước. Cậu không tạo ra chiến tranh, cậu tìm cách chấm dứt nó.

[pause] Hai: những tội nặng nhất có yếu tố tai nạn. Cậu không muốn thảm kịch Đặc khu xảy ra.

[pause] Ba: cậu không nhận lấy bất cứ lợi ích nào. Cậu kết thúc bằng cách tự trừng phạt mình, trước cả khi có tòa án nào.

[pause] Và năm: sau cái chết của Lelouch, Suzaku tiếp tục làm Zero để bảo vệ hòa bình, còn Nunnally trở thành người dẫn dắt Britannia theo cách hiền hòa. Đúng như mong ước ban đầu của Lelouch.

[pause] Và bốn: thế giới sau cái chết của Lelouch là một thế giới hòa bình hơn. Chính những người từng bị áp bức được sống tự do.

[pause] [curious] Kaku không tuyên án, nhưng Kaku muốn chỉ ra câu hỏi thật sự của Code Geass: mục đích có biện minh cho phương tiện không?

[pause] Lelouch trả lời là có, và cậu trả giá bằng cả mạng sống. Suzaku trả lời là không, nhưng cuối cùng cũng đồng hành với Lelouch. Bộ phim không cho ta một câu trả lời dễ dàng.

[pause] Câu hỏi này cũng là một câu hỏi triết học rất cũ ngoài đời: có nên hy sinh một số người để cứu nhiều người hơn không? Người ta đã tranh luận về nó hàng trăm năm mà chưa có câu trả lời chung.

[pause] Kaku nghĩ Code Geass hay chính vì nó không để Lelouch hoàn toàn vô tội, cũng không để cậu hoàn toàn đáng ghét. Nó bắt ta phải tự suy nghĩ.
```

### c09 · Bồi thẩm bỏ phiếu / Kết

Khoảng 70 giây · cảnh s78–s84 · 913 ký tự

**Gemini**

```text
Giờ tới lượt bạn. Có ba lựa chọn. Một: có tội. Những gì Lelouch làm không thể biện minh, dù kết quả là gì.

<short pause> Hai: vô tội. Trong hoàn cảnh đó, Lelouch đã làm điều cần làm, và tự trả giá bằng mạng sống.

<short pause> Ba: có tội, nhưng được khoan hồng. Lelouch phạm tội, nhưng động cơ và sự hy sinh của cậu cần được tính tới.

<short pause> Viết số một, hai hay ba vào bình luận, kèm một câu lý do. <laugh> Kaku sẽ tổng hợp kết quả phiên tòa ở một video sau.

<short pause> Lelouch bắt đầu câu chuyện bằng một lời thề phá hủy thế giới, và kết thúc bằng việc để thế giới phá hủy mình. Giữa hai điều đó là một câu hỏi mà mỗi người xem tự trả lời.

<short pause> Video tiếp theo, Kaku quay về biển Đông, đúng lúc bản làm lại One Piece ra mắt: những chi tiết cài cắm trong năm mươi chương đầu mà chỉ người đọc lại mới thấy.

<short pause> Nếu bạn thích những phiên tòa như thế này, hãy đăng ký kênh, và cho Kaku biết bị cáo tiếp theo bạn muốn đưa ra tòa là ai. Phiên tòa tạm hoãn. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ tới lượt bạn. Có ba lựa chọn. Một: có tội. Những gì Lelouch làm không thể biện minh, dù kết quả là gì.

[pause] Hai: vô tội. Trong hoàn cảnh đó, Lelouch đã làm điều cần làm, và tự trả giá bằng mạng sống.

[pause] Ba: có tội, nhưng được khoan hồng. Lelouch phạm tội, nhưng động cơ và sự hy sinh của cậu cần được tính tới.

[pause] Viết số một, hai hay ba vào bình luận, kèm một câu lý do. [chuckles] Kaku sẽ tổng hợp kết quả phiên tòa ở một video sau.

[pause] Lelouch bắt đầu câu chuyện bằng một lời thề phá hủy thế giới, và kết thúc bằng việc để thế giới phá hủy mình. Giữa hai điều đó là một câu hỏi mà mỗi người xem tự trả lời.

[pause] Video tiếp theo, Kaku quay về biển Đông, đúng lúc bản làm lại One Piece ra mắt: những chi tiết cài cắm trong năm mươi chương đầu mà chỉ người đọc lại mới thấy.

[pause] Nếu bạn thích những phiên tòa như thế này, hãy đăng ký kênh, và cho Kaku biết bị cáo tiếp theo bạn muốn đưa ra tòa là ai. Phiên tòa tạm hoãn. Kaku gấp sổ đây, hẹn gặp lại!
```
