# Bộ prompt · Phiên tòa: Eren Yeager — có tội hay không?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 8 đoạn đọc, khoảng 15.4 phút giọng.
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

### s01 · Khai mạc phiên tòa

Lời: Cảnh báo: video có spoiler toàn bộ Attack on Titan, bao gồm cả cái kết của manga và anime. Nếu bạn chưa xem h…

```text
Wide 16:9 landscape cinematic frame. an empty old courtroom with tall windows, dust in the light beams, a closed notebook resting on the clerk's desk, wide establishing shot, cold daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Bị cáo: Eren Yeager. Tội danh: gây ra Địa minh, cuộc hành quân của những người khổng lồ đã xóa sổ khoảng tám…

```text
Wide 16:9 landscape cinematic frame. a lone empty defendant's chair under a single spotlight in a dark courtroom, a thick case file on the table beside it, dramatic medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Đây là một trong những nhân vật gây tranh cãi nhất lịch sử anime. Có người gọi cậu là quỷ dữ. Có người gọi cậ…

```text
Wide 16:9 landscape cinematic frame. a split crowd in a public gallery, some people raising angry fists, others looking down in sorrow, others confused, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku không phải thẩm phán. Kaku là thư ký tòa: đọc cáo trạng, ghi lời bào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot seated at a clerk's desk with a quill pen and a small stack of case files, serious expression, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Vì sao lại là một phiên tòa? Vì với một nhân vật như Eren, xếp hạng hay giải thích sức mạnh đều không đủ. Câu…

```text
Wide 16:9 landscape cinematic frame. a courthouse facade at dawn with a crowd gathering on the steps, some holding signs, wide shot, cool morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Còn phán quyết? Phán quyết thuộc về bạn. Bạn là bồi thẩm của phiên tòa này, và cuối video Kaku sẽ mời bạn bỏ…

```text
Wide 16:9 landscape cinematic frame. a row of empty jury chairs facing the viewer, each with a small ballot card on the seat, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Một lưu ý trước khi bắt đầu: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh…

```text
Wide 16:9 landscape cinematic frame. a small printed notice pinned on the courtroom door, close-up, neutral light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Hồ sơ bị cáo

Lời: Eren lớn lên trong những bức tường khổng lồ bao quanh một thị trấn nhỏ. Người dân tin rằng bên ngoài chỉ có n…

```text
Wide 16:9 landscape cinematic frame. three gigantic concentric stone walls surrounding a small medieval town seen from high above, wide aerial shot, soft morning mist. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Cậu gia nhập Trinh sát đoàn, đơn vị duy nhất dám ra ngoài tường thành. Với Eren, bầu trời bên ngoài tượng trư…

```text
Wide 16:9 landscape cinematic frame. a squad of riders on horseback charging out through a massive gate into open fields, cloaks with wing emblems fluttering, wide shot, bright sky. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Hình ảnh cánh chim xuất hiện suốt bộ truyện. Eren luôn nhìn lên những con chim bay qua tường và tự hỏi vì sao…

```text
Wide 16:9 landscape cinematic frame. a flock of birds flying over a towering stone wall at sunset, a small boy silhouette looking up from below, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Năm mười tuổi, cậu tận mắt chứng kiến mẹ mình bị một người khổng lồ giết khi bức tường bị phá. Cậu thề sẽ tiê…

```text
Wide 16:9 landscape cinematic frame. a small boy being carried away by an adult, reaching back toward a collapsed house engulfed in dust, wide shot, dramatic grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Về sau, cậu phát hiện mình có thể biến thành người khổng lồ. Rồi phát hiện sự thật lớn hơn: người trên đảo là…

```text
Wide 16:9 landscape cinematic frame. a young man standing at the edge of a wall looking out at a distant sea for the first time, back view, wide shot, bright but uneasy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Bên kia biển, quốc gia Marley nhốt người Eldia trong khu cách ly, buộc họ đeo băng tay đánh dấu, và biến trẻ…

```text
Wide 16:9 landscape cinematic frame. a fenced internment district in a grey city, residents wearing armbands on their sleeves, guards at the gate, wide shot, cold overcast light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và thế giới đã có kế hoạch cho hòn đảo: không phải hòa bình, mà là tiêu diệt. Eren biết điều đó khi chạm vào…

```text
Wide 16:9 landscape cinematic frame. a map of an island with ominous red arrows from warships converging on it, parchment style, crimson ink. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Kaku ghi thêm: bí mật về thế giới bên ngoài nằm trong tầng hầm nhà Eren, nơi cha cậu để lại những cuốn sổ. Mư…

```text
Wide 16:9 landscape cinematic frame. a dusty basement with a single desk and three old notebooks under a beam of light, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Cậu nắm trong tay hai sức mạnh: Người khổng lồ Tiến công, có thể thấy ký ức của cả những người kế thừa trong…

```text
Wide 16:9 landscape cinematic frame. two glowing symbols floating above an open hand: an eye looking forward in time and a crown-like sigil, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi vào hồ sơ: bị cáo không phải là một kẻ sinh ra đã ác. Nhưng hồ sơ không quyết định bản án. Hành động…

```text
Wide 16:9 landscape cinematic frame. the owl mascot stamping a small seal on the defendant's file, thoughtful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Cáo trạng

Lời: Công tố viên xin trình bày. Tội danh thứ nhất: cuộc tấn công ở Liberio. Giữa một lễ hội ở thành phố của Marle…

```text
Wide 16:9 landscape cinematic frame. a festival stage in a crowded city square collapsing as a massive shadow rises behind it, wide shot, chaotic red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Eren còn tấn công ngay khi Marley vừa tuyên chiến với hòn đảo trước toàn thế giới. Công tố nói: đó là trả đũa…

```text
Wide 16:9 landscape cinematic frame. a grand stage with national flags and a speaker at a podium addressing foreign diplomats, a massive shadow looming behind the backdrop, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Mục tiêu là giới lãnh đạo quân sự và các chiến binh khổng lồ của Marley. Nhưng trong cuộc tấn công, rất nhiều…

```text
Wide 16:9 landscape cinematic frame. a scattered festival banner lying in rubble on a quiet street after the attack, extreme close-up, somber grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Trước khi bắt đầu, Eren dùng sức mạnh Thủy tổ nói thẳng vào tâm trí mọi người Eldia: cậu sẽ giẫm nát mọi vùng…

```text
Wide 16:9 landscape cinematic frame. thousands of people in different places all stopping at the same moment and looking up at an empty sky, wide shot, eerie pale light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Tội danh thứ hai, nghiêm trọng nhất: Địa minh. Eren dùng sức mạnh Thủy tổ đánh thức hàng triệu người khổng lồ…

```text
Wide 16:9 landscape cinematic frame. an endless line of colossal silhouettes marching across a plain toward the horizon, dust rising to the sky, wide epic shot, ominous orange light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Theo truyện, khoảng tám mươi phần trăm nhân loại đã chết trước khi Địa minh bị chặn lại. Công tố nhấn mạnh: đ…

```text
Wide 16:9 landscape cinematic frame. a world map on parchment with most of its land shaded dark and only a few small areas left light, top-down shot, crimson and navy ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Zeke, anh trai cùng cha, có một kế hoạch khác: dùng sức mạnh Thủy tổ khiến người Eldia không thể sinh con nữa…

```text
Wide 16:9 landscape cinematic frame. two brothers standing on a vast glowing sandy plain under a starry sky, one reaching out his hand, the other turning away, wide shot, surreal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Tội danh thứ ba: thao túng. Eren giấu kế hoạch với chính những người đồng đội, lợi dụng anh trai Zeke, và đẩy…

```text
Wide 16:9 landscape cinematic frame. a chess board where several pieces are tied by faint strings to a hand above the board, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Tội danh thứ tư gây tranh cãi nhất. Trong chương cuối, truyện hé lộ Eren đã tác động tới quá khứ qua sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a boy looking at a shattered family photograph on the floor, faint glowing threads running from it into the past, close-up, melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Công tố kết luận phần cáo trạng: dù hoàn cảnh ra sao, không có lý do nào biện minh cho việc giết phần lớn nhâ…

```text
Wide 16:9 landscape cinematic frame. a gavel resting firmly on a thick stack of documents, extreme close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Lời bào chữa

Lời: Luật sư bào chữa xin trình bày. Trước hết, hãy nhìn vào hoàn cảnh. Người Eldia bị áp bức suốt hàng chục năm,…

```text
Wide 16:9 landscape cinematic frame. an old generation of armband-wearing families behind a fence looking through the wire at a free city, medium shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Thế giới bên ngoài không chỉ ghét hòn đảo. Họ đang chuẩn bị tấn công nó. Với Eren, nếu không làm gì, những ng…

```text
Wide 16:9 landscape cinematic frame. a fleet of warships gathering on a stormy sea at night, distant island lights on the horizon, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Bào chữa cũng chỉ ra: lựa chọn còn lại mà Eren có là kế hoạch của Zeke, để chính dân tộc mình tự biến mất. Vớ…

```text
Wide 16:9 landscape cinematic frame. an empty cradle in a quiet sunlit room, dust floating in the air, close-up, melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Thứ hai, sức mạnh Tiến công cho Eren thấy ký ức của tương lai. Cậu nói rằng tương lai ấy như đã được định sẵn…

```text
Wide 16:9 landscape cinematic frame. a young man standing on a single narrow path carved into stone with walls on either side stretching into the distance, wide shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Không còn người khổng lồ, người Eldia không còn bị coi là mối đe dọa sinh học. Bào chữa lập luận: đây là điều…

```text
Wide 16:9 landscape cinematic frame. a child with an armband slowly taking it off and letting it fall to the ground, close-up, soft hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Thứ ba, kết quả cuối cùng của câu chuyện: sức mạnh người khổng lồ biến mất vĩnh viễn. Lời nguyền kéo dài hai…

```text
Wide 16:9 landscape cinematic frame. a massive ancient tree of light slowly fading away above a quiet hill, wide shot, soft dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và thứ tư: Eren đã chủ động để chính bạn bè mình chặn cậu lại. Bằng cách trở thành kẻ thù chung, cậu biến nhữ…

```text
Wide 16:9 landscape cinematic frame. a group of young silhouettes standing together on a hill at sunset, facing a distant colossal shadow, wide shot, warm and cold contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Bào chữa kết luận: Eren là sản phẩm của một vòng thù hận mà cậu không tạo ra. Cậu đã chọn một con đường khủng…

```text
Wide 16:9 landscape cinematic frame. a circular path carved into stone with no exits, a lone figure walking along it, top-down shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chép lại mà không bình luận. Việc của thư ký là ghi đủ, không ghi thiên.

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing carefully in a ledger, both columns filling evenly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Nhân chứng 1: Reiner

Lời: Tòa mời nhân chứng thứ nhất: Reiner Braun, chiến binh Marley từng phá bức tường năm Eren mười tuổi.

```text
Wide 16:9 landscape cinematic frame. a tired broad-shouldered man in a military uniform standing in a witness box, hands trembling, medium shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Trước cuộc tấn công Liberio, Eren gặp Reiner trong một tầng hầm. Và Eren nói một câu mà nhiều người nhớ mãi:…

```text
Wide 16:9 landscape cinematic frame. two men sitting across from each other in a dim basement, one leaning forward calmly, the other shaking, medium shot, single lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Ý của Eren: Reiner từng phá tường, giết người trên đảo, vì tin mình đang cứu thế giới khỏi quỷ. Giờ Eren sắp…

```text
Wide 16:9 landscape cinematic frame. two mirrored scenes side by side: a wall collapsing on one island, a city stage collapsing in another country, symmetrical composition, grey and red light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Về sau, chính Reiner cũng chiến đấu để ngăn Địa minh, cùng những người từng là kẻ thù của anh. Một người từng…

```text
Wide 16:9 landscape cinematic frame. a tired soldier standing shoulder to shoulder with former enemies on a hill, facing a distant cloud of dust, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Lời khai này có lợi cho ai? Bào chữa nói nó cho thấy Eren hiểu vòng thù hận. Công tố nói: hiểu mà vẫn làm, th…

```text
Wide 16:9 landscape cinematic frame. a balance scale with the same small object placed first on one side, then the other, parchment illustration, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Nhân chứng 2: Gabi

Lời: Nhân chứng thứ hai: Gabi Braun, cô bé người Eldia ở Marley, được dạy từ nhỏ rằng người trên đảo là quỷ.

```text
Wide 16:9 landscape cinematic frame. a young girl in a soldier's uniform with an armband standing on a crate to see over the witness box, determined face, medium shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Người bạn Falco của Gabi thì từ đầu đã không muốn thù hận. Cậu bé chỉ muốn Gabi được sống. Hai đứa trẻ này là…

```text
Wide 16:9 landscape cinematic frame. two children sitting on a fallen log in a forest, one offering the other a piece of bread, medium shot, soft dappled light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Sau cuộc tấn công, Gabi lên đảo trả thù. Cô gây ra cái chết của Sasha, một người bạn của Eren. Nhưng rồi cô s…

```text
Wide 16:9 landscape cinematic frame. a young girl sitting at a farmhouse dinner table with a family who welcomes her, her expression shifting from anger to confusion, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Công tố dùng nhân chứng này làm bằng chứng quan trọng: vòng thù hận có thể bị phá vỡ bằng sự thấu hiểu, không…

```text
Wide 16:9 landscape cinematic frame. a broken chain on a table next to two small hands clasped together, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi nhận: đây là một trong những cuộc tranh luận hay nhất của phiên tòa. Cả hai bên đều dùng cùng một nh…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking back and forth between two lawyers pointing at the same witness. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Bào chữa phản biện: một cô bé thay đổi không có nghĩa là cả thế giới thay đổi kịp, khi chiến hạm đã ở ngoài k…

```text
Wide 16:9 landscape cinematic frame. a single small candle burning on a windowsill while a massive fleet sails past in the dark sea outside, wide shot, cold and warm contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Nhân chứng 3: Armin

Lời: Nhân chứng thứ ba: Armin Arlert, bạn thân nhất của Eren từ thuở nhỏ, người từng cùng cậu mơ về biển cả bên ng…

```text
Wide 16:9 landscape cinematic frame. two young boys sitting on a stone step reading a book about the ocean together, back view, warm afternoon light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Trong cuộc trò chuyện cuối cùng ở một không gian ngoài thời gian, Eren thừa nhận một điều rất con người: một…

```text
Wide 16:9 landscape cinematic frame. two young men sitting on a sandy beach at the edge of a strange glowing endless space, one looking down, medium shot, surreal soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Armin là người đã chiến đấu để ngăn bạn mình. Nhưng cậu cũng là người duy nhất nghe Eren nói thật lòng, và cậ…

```text
Wide 16:9 landscape cinematic frame. two young men sitting side by side on the sand, one gently resting his head against the other's shoulder, back view, soft glowing light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhưng cậu cũng thừa nhận mình không muốn chết, muốn được sống bên bạn bè. Một thiếu niên sợ hãi đằng sau kẻ g…

```text
Wide 16:9 landscape cinematic frame. a young man crying with his face in his hands, a friend's hand resting on his shoulder, close-up, soft melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Có một chi tiết thú vị cho bồi thẩm: một câu nói của Armin trong cuộc trò chuyện này ở manga từng gây tranh c…

```text
Wide 16:9 landscape cinematic frame. two versions of the same printed page side by side, one line highlighted differently on each, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · **Kaku** (đính kèm ảnh mẫu)

Lời: Lời khai của Armin khó xếp vào bên nào. Nó cho thấy Eren vừa có lựa chọn, vừa bị dằn vặt bởi lựa chọn đó.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a witness statement up to the light, unable to decide which pile to put it in. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Nhân chứng 4: Mikasa

Lời: Nhân chứng cuối cùng: Mikasa Ackerman, người luôn ở bên Eren từ nhỏ.

```text
Wide 16:9 landscape cinematic frame. a young woman in a dark military jacket standing silently in the witness box, eyes lowered, medium shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Chính Mikasa là người kết thúc Địa minh bằng một lựa chọn rất đau đớn: cô ngăn Eren lại bằng chính tay mình.…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing on a vast battlefield at dusk, holding a small bundle wrapped in cloth, a colossal shadow collapsing behind, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Truyện gợi ý rằng Ymir, người khổng lồ đầu tiên, đã bị trói buộc hai nghìn năm bởi một tình yêu dành cho kẻ đ…

```text
Wide 16:9 landscape cinematic frame. a chain wrapped around an ancient tree snapping apart as a young woman lets go of a hand, symbolic composition, soft golden light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chép mà tay hơi run. Trong cả phiên tòa, đây là lời khai khó ghi nhất.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pausing with the quill above the page, a single tear-shaped ink drop on the paper. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Lời khai của Mikasa không bằng lời, mà bằng hành động: cô yêu Eren, và vẫn chọn ngăn cậu lại. Với nhiều người…

```text
Wide 16:9 landscape cinematic frame. a single white flower lying on a stone beneath a large tree on a hill, extreme close-up, gentle warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Nhưng hãy nhớ: truyện cũng cho thấy Eren đã biết trước và chờ đợi lựa chọn ấy. Đến cả khoảnh khắc bị ngăn lại…

```text
Wide 16:9 landscape cinematic frame. a small hourglass with sand running out placed beside a folded letter, close-up, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Luận điểm cuối của công tố

Lời: Công tố tổng kết. Bị cáo đã giết phần lớn nhân loại, trong đó có vô số người vô tội, trẻ em, những người chưa…

```text
Wide 16:9 landscape cinematic frame. a vast empty landscape with silent ruined towns stretching to the horizon, wide shot, grey ash-colored sky. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Công tố cũng lưu ý: nhiều người trong số những người chết không hề cầm vũ khí, không hề biết tới Paradis, và…

```text
Wide 16:9 landscape cinematic frame. a quiet village marketplace far from any war, people buying bread and fruit, unaware of the dust cloud on the horizon, wide shot, warm then ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Bị cáo có những lựa chọn khác. Gabi chứng minh sự thấu hiểu là có thể. Bị cáo thừa nhận một phần trong mình m…

```text
Wide 16:9 landscape cinematic frame. three evidence folders laid on a table with small tags: a broken chain, a confession, a map, top-down shot, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Công tố còn đặt câu hỏi: nếu Eren thấy trước tương lai, thì cậu cũng thấy trước con số. Biết trước mà vẫn làm…

```text
Wide 16:9 landscape cinematic frame. a hand holding a telescope looking at a distant catastrophe, the other hand not reaching for any brake lever, close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Và kế hoạch biến bạn bè thành anh hùng không thay đổi được con số. Không có mục đích nào đủ lớn để biện minh…

```text
Wide 16:9 landscape cinematic frame. a single large number 80 carved into a stone tablet in an empty hall, low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Luận điểm cuối của bào chữa

Lời: Bào chữa tổng kết. Không ai phủ nhận thảm họa. Nhưng bị cáo sinh ra trong một thế giới đã chọn sẵn hòn đảo là…

```text
Wide 16:9 landscape cinematic frame. a small island on a map surrounded by arrows from every direction, parchment illustration, crimson ink. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Bào chữa cũng nhắc: sau Địa minh, những người sống sót trên đảo và ngoài đảo lần đầu tiên phải ngồi lại với n…

```text
Wide 16:9 landscape cinematic frame. a small group of people from different sides sitting together around a campfire in a ruined landscape, medium shot, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Bị cáo thấy một tương lai mà cậu tin là không thể thay đổi. Cậu gánh lấy tội lỗi lớn nhất lịch sử, để kết thú…

```text
Wide 16:9 landscape cinematic frame. a lone figure carrying an enormous stone on his back up a hill while friends watch from a distance, wide shot, heavy dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Bào chữa không xin tòa gọi bị cáo là người tốt. Chỉ xin tòa hiểu rằng câu chuyện này không có lựa chọn nào sạ…

```text
Wide 16:9 landscape cinematic frame. a pair of hands held out palms up, empty, in soft light, extreme close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Góc nhìn của Kaku: vì sao tác giả không tuyên án

Lời: Cái kết của Attack on Titan ra mắt năm 2021 ở manga và năm 2023 ở anime, và tới giờ vẫn chia rẽ người đọc. Có…

```text
Wide 16:9 landscape cinematic frame. a bookstore shelf with the final volume of a long series, two readers standing nearby with opposite expressions, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Kaku có một nhận xét cuối, không phải phán quyết. Tác giả Isayama không đưa ra câu trả lời rõ ràng. Ông để nh…

```text
Wide 16:9 landscape cinematic frame. an unfinished manuscript page on a desk with the last panel left blank, a pen resting beside it, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Tên truyện trong tiếng Nhật có thể hiểu là người khổng lồ tấn công. Nhưng đến cuối, câu hỏi thật sự là: ai mớ…

```text
Wide 16:9 landscape cinematic frame. an old stone gate with its carved inscription half worn away, wind blowing leaves across it, close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và có lẽ đó là chủ đích. Attack on Titan là câu chuyện về việc mỗi bên đều nghĩ mình đang chiến đấu cho tự do…

```text
Wide 16:9 landscape cinematic frame. two armies facing each other across a river, each carrying banners with the same symbol of wings, wide shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thấy khó bỏ phiếu, đó là dấu hiệu bạn đã hiểu câu chuyện. Một phiên tòa dễ dàng thì không cần tới bồi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting quietly with the quill pen put down, looking at the empty jury chairs. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Bồi thẩm bỏ phiếu

Lời: Giờ tới lượt bạn. Phương án A: có tội, không có tình tiết giảm nhẹ.

```text
Wide 16:9 landscape cinematic frame. a ballot card with option A highlighted in crimson ink, close-up, stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Phương án B: có tội, nhưng có tình tiết giảm nhẹ vì hoàn cảnh và mục đích.

```text
Wide 16:9 landscape cinematic frame. a ballot card with option B highlighted in amber ink, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Phương án C: không thể phán xét theo luật thông thường, vì đây là một thế giới không có lựa chọn đúng.

```text
Wide 16:9 landscape cinematic frame. a ballot card with option C highlighted in navy ink, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và nếu bạn chọn khác với số đông, đừng ngại. Một bồi thẩm tốt là người nói ra lý do của mình, không phải ngườ…

```text
Wide 16:9 landscape cinematic frame. a single raised hand in an otherwise still jury box, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Hãy bình luận chữ cái bạn chọn, kèm một câu lý do. Kaku sẽ đếm phiếu và công bố kết quả ở phần ghim bình luận.

```text
Wide 16:9 landscape cinematic frame. a ballot box on the clerk's desk with small paper cards dropping into it, medium shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Kết

Lời: Eren từng mơ được nhìn thấy biển. Cậu đã nhìn thấy nó, và rồi cậu chọn đi qua nó theo cách không ai có thể qu…

```text
Wide 16:9 landscape cinematic frame. a young man standing alone on a beach facing a vast calm sea at sunset, waves reaching his feet, wide shot, bittersweet warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Nếu bạn đã đi cùng Kaku từ video đầu tiên về Nen, cảm ơn bạn rất nhiều. Ba mươi chín cuốn sổ đã mở, và Kaku c…

```text
Wide 16:9 landscape cinematic frame. a tall stack of thirty-nine small notebooks on a desk with a thank-you note on top, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo là một món quà cho fan Sakamoto Days: mười lăm phút ôn tập mọi thứ cần nhớ trước khi mùa hai…

```text
Wide 16:9 landscape cinematic frame. a desk calendar with a small countdown circle drawn on it, close-up, fresh morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích dạng phiên tòa này và muốn Kaku xử thêm nhân vật khác, hãy đăng ký kênh và đề cử bị cáo tiếp th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing the court ledger and bowing politely toward the jury chairs. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 83 giây · cảnh s01–s07 · 1079 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler toàn bộ Attack on Titan, bao gồm cả cái kết của manga và anime. Nếu bạn chưa xem hết, hãy lưu video lại.

<short pause> Bị cáo: Eren Yeager. Tội danh: gây ra Địa minh, cuộc hành quân của những người khổng lồ đã xóa sổ khoảng tám mươi phần trăm nhân loại bên ngoài đảo Paradis.

<short pause> Đây là một trong những nhân vật gây tranh cãi nhất lịch sử anime. Có người gọi cậu là quỷ dữ. Có người gọi cậu là người hi sinh tất cả vì bạn bè. Có người không biết gọi cậu là gì.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku không phải thẩm phán. Kaku là thư ký tòa: đọc cáo trạng, ghi lời bào chữa, gọi nhân chứng. Mọi nhân chứng đều là chi tiết có thật trong truyện.

<short pause> Vì sao lại là một phiên tòa? Vì với một nhân vật như Eren, xếp hạng hay giải thích sức mạnh đều không đủ. Câu hỏi thật sự mà người xem vẫn tranh cãi là: cậu có đáng bị kết tội không?

<short pause> Còn phán quyết? Phán quyết thuộc về bạn. Bạn là bồi thẩm của phiên tòa này, và cuối video Kaku sẽ mời bạn bỏ phiếu.

<short pause> Một lưu ý trước khi bắt đầu: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh cho bạo lực ngoài đời.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler toàn bộ Attack on Titan, bao gồm cả cái kết của manga và anime. Nếu bạn chưa xem hết, hãy lưu video lại.

[pause] Bị cáo: Eren Yeager. Tội danh: gây ra Địa minh, cuộc hành quân của những người khổng lồ đã xóa sổ khoảng tám mươi phần trăm nhân loại bên ngoài đảo Paradis.

[pause] Đây là một trong những nhân vật gây tranh cãi nhất lịch sử anime. Có người gọi cậu là quỷ dữ. Có người gọi cậu là người hi sinh tất cả vì bạn bè. Có người không biết gọi cậu là gì.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku không phải thẩm phán. Kaku là thư ký tòa: đọc cáo trạng, ghi lời bào chữa, gọi nhân chứng. Mọi nhân chứng đều là chi tiết có thật trong truyện.

[pause] [curious] Vì sao lại là một phiên tòa? Vì với một nhân vật như Eren, xếp hạng hay giải thích sức mạnh đều không đủ. Câu hỏi thật sự mà người xem vẫn tranh cãi là: cậu có đáng bị kết tội không?

[pause] Còn phán quyết? Phán quyết thuộc về bạn. Bạn là bồi thẩm của phiên tòa này, và cuối video Kaku sẽ mời bạn bỏ phiếu.

[pause] Một lưu ý trước khi bắt đầu: phiên tòa này là để hiểu một nhân vật hư cấu, không phải để cổ vũ hay biện minh cho bạo lực ngoài đời.
```

### c02 · Hồ sơ bị cáo

Khoảng 118 giây · cảnh s08–s17 · 1532 ký tự

**Gemini**

```text
Eren lớn lên trong những bức tường khổng lồ bao quanh một thị trấn nhỏ. Người dân tin rằng bên ngoài chỉ có những người khổng lồ ăn thịt người.

<short pause> Cậu gia nhập Trinh sát đoàn, đơn vị duy nhất dám ra ngoài tường thành. Với Eren, bầu trời bên ngoài tượng trưng cho một thứ duy nhất: tự do.

<short pause> Hình ảnh cánh chim xuất hiện suốt bộ truyện. Eren luôn nhìn lên những con chim bay qua tường và tự hỏi vì sao con người lại phải sống như gia súc trong chuồng.

<short pause> Năm mười tuổi, cậu tận mắt chứng kiến mẹ mình bị một người khổng lồ giết khi bức tường bị phá. Cậu thề sẽ tiêu diệt toàn bộ bọn chúng.

<short pause> Về sau, cậu phát hiện mình có thể biến thành người khổng lồ. Rồi phát hiện sự thật lớn hơn: người trên đảo là tộc Eldia, và thế giới bên ngoài coi họ là quỷ.

<short pause> Bên kia biển, quốc gia Marley nhốt người Eldia trong khu cách ly, buộc họ đeo băng tay đánh dấu, và biến trẻ em Eldia thành chiến binh khổng lồ.

<short pause> Và thế giới đã có kế hoạch cho hòn đảo: không phải hòa bình, mà là tiêu diệt. Eren biết điều đó khi chạm vào ký ức của những người khổng lồ trước.

<short pause> Kaku ghi thêm: bí mật về thế giới bên ngoài nằm trong tầng hầm nhà Eren, nơi cha cậu để lại những cuốn sổ. Mười một năm đi tìm, cuối cùng câu trả lời là: kẻ thù không phải quái vật, mà là cả thế giới.

<short pause> Cậu nắm trong tay hai sức mạnh: Người khổng lồ Tiến công, có thể thấy ký ức của cả những người kế thừa trong tương lai, và Người khổng lồ Thủy tổ, có thể điều khiển mọi người khổng lồ.

<short pause> <laugh> Kaku ghi vào hồ sơ: bị cáo không phải là một kẻ sinh ra đã ác. <short pause> Nhưng hồ sơ không quyết định bản án. Hành động mới quyết định.
```

**ElevenLabs**

```text
Eren lớn lên trong những bức tường khổng lồ bao quanh một thị trấn nhỏ. Người dân tin rằng bên ngoài chỉ có những người khổng lồ ăn thịt người.

[pause] Cậu gia nhập Trinh sát đoàn, đơn vị duy nhất dám ra ngoài tường thành. Với Eren, bầu trời bên ngoài tượng trưng cho một thứ duy nhất: tự do.

[pause] Hình ảnh cánh chim xuất hiện suốt bộ truyện. Eren luôn nhìn lên những con chim bay qua tường và tự hỏi vì sao con người lại phải sống như gia súc trong chuồng.

[pause] Năm mười tuổi, cậu tận mắt chứng kiến mẹ mình bị một người khổng lồ giết khi bức tường bị phá. Cậu thề sẽ tiêu diệt toàn bộ bọn chúng.

[pause] Về sau, cậu phát hiện mình có thể biến thành người khổng lồ. Rồi phát hiện sự thật lớn hơn: người trên đảo là tộc Eldia, và thế giới bên ngoài coi họ là quỷ.

[pause] Bên kia biển, quốc gia Marley nhốt người Eldia trong khu cách ly, buộc họ đeo băng tay đánh dấu, và biến trẻ em Eldia thành chiến binh khổng lồ.

[pause] Và thế giới đã có kế hoạch cho hòn đảo: không phải hòa bình, mà là tiêu diệt. Eren biết điều đó khi chạm vào ký ức của những người khổng lồ trước.

[pause] Kaku ghi thêm: bí mật về thế giới bên ngoài nằm trong tầng hầm nhà Eren, nơi cha cậu để lại những cuốn sổ. Mười một năm đi tìm, cuối cùng câu trả lời là: kẻ thù không phải quái vật, mà là cả thế giới.

[pause] Cậu nắm trong tay hai sức mạnh: Người khổng lồ Tiến công, có thể thấy ký ức của cả những người kế thừa trong tương lai, và Người khổng lồ Thủy tổ, có thể điều khiển mọi người khổng lồ.

[pause] [chuckles] Kaku ghi vào hồ sơ: bị cáo không phải là một kẻ sinh ra đã ác. [pause] Nhưng hồ sơ không quyết định bản án. Hành động mới quyết định.
```

### c03 · Cáo trạng

Khoảng 128 giây · cảnh s18–s27 · 1665 ký tự

**Gemini**

```text
Công tố viên xin trình bày. Tội danh thứ nhất: cuộc tấn công ở Liberio. Giữa một lễ hội ở thành phố của Marley, Eren biến thành người khổng lồ và tấn công.

<short pause> Eren còn tấn công ngay khi Marley vừa tuyên chiến với hòn đảo trước toàn thế giới. Công tố nói: đó là trả đũa nhắm vào cả một thành phố. Bào chữa sẽ nói: đó là ra tay trước khi bị tiêu diệt.

<short pause> Mục tiêu là giới lãnh đạo quân sự và các chiến binh khổng lồ của Marley. <short pause> Nhưng trong cuộc tấn công, rất nhiều thường dân, kể cả người Eldia trong khu cách ly, đã chết.

<short pause> Trước khi bắt đầu, Eren dùng sức mạnh Thủy tổ nói thẳng vào tâm trí mọi người Eldia: cậu sẽ giẫm nát mọi vùng đất bên ngoài, cho tới khi không còn gì để giẫm.

<short pause> Tội danh thứ hai, nghiêm trọng nhất: Địa minh. Eren dùng sức mạnh Thủy tổ đánh thức hàng triệu người khổng lồ trong tường thành và cho chúng giẫm nát thế giới bên ngoài.

<short pause> Theo truyện, khoảng tám mươi phần trăm nhân loại đã chết trước khi Địa minh bị chặn lại. Công tố nhấn mạnh: đây không phải phòng vệ. Đây là tiêu diệt.

<short pause> Zeke, anh trai cùng cha, có một kế hoạch khác: dùng sức mạnh Thủy tổ khiến người Eldia không thể sinh con nữa, để cả dân tộc biến mất trong hòa bình. Eren giả vờ đồng ý, rồi phản bội kế hoạch đó.

<short pause> Tội danh thứ ba: thao túng. Eren giấu kế hoạch với chính những người đồng đội, lợi dụng anh trai Zeke, và đẩy mọi người vào những lựa chọn mà họ không được biết trước.

<short pause> Tội danh thứ tư gây tranh cãi nhất. Trong chương cuối, truyện hé lộ Eren đã tác động tới quá khứ qua sức mạnh nhìn ký ức, góp phần vào chính những bi kịch trong gia đình mình, kể cả cái chết của mẹ.

<short pause> Công tố kết luận phần cáo trạng: dù hoàn cảnh ra sao, không có lý do nào biện minh cho việc giết phần lớn nhân loại.
```

**ElevenLabs**

```text
Công tố viên xin trình bày. Tội danh thứ nhất: cuộc tấn công ở Liberio. Giữa một lễ hội ở thành phố của Marley, Eren biến thành người khổng lồ và tấn công.

[pause] Eren còn tấn công ngay khi Marley vừa tuyên chiến với hòn đảo trước toàn thế giới. Công tố nói: đó là trả đũa nhắm vào cả một thành phố. Bào chữa sẽ nói: đó là ra tay trước khi bị tiêu diệt.

[pause] Mục tiêu là giới lãnh đạo quân sự và các chiến binh khổng lồ của Marley. [pause] Nhưng trong cuộc tấn công, rất nhiều thường dân, kể cả người Eldia trong khu cách ly, đã chết.

[pause] Trước khi bắt đầu, Eren dùng sức mạnh Thủy tổ nói thẳng vào tâm trí mọi người Eldia: cậu sẽ giẫm nát mọi vùng đất bên ngoài, cho tới khi không còn gì để giẫm.

[pause] Tội danh thứ hai, nghiêm trọng nhất: Địa minh. Eren dùng sức mạnh Thủy tổ đánh thức hàng triệu người khổng lồ trong tường thành và cho chúng giẫm nát thế giới bên ngoài.

[pause] Theo truyện, khoảng tám mươi phần trăm nhân loại đã chết trước khi Địa minh bị chặn lại. Công tố nhấn mạnh: đây không phải phòng vệ. Đây là tiêu diệt.

[pause] Zeke, anh trai cùng cha, có một kế hoạch khác: dùng sức mạnh Thủy tổ khiến người Eldia không thể sinh con nữa, để cả dân tộc biến mất trong hòa bình. Eren giả vờ đồng ý, rồi phản bội kế hoạch đó.

[pause] Tội danh thứ ba: thao túng. Eren giấu kế hoạch với chính những người đồng đội, lợi dụng anh trai Zeke, và đẩy mọi người vào những lựa chọn mà họ không được biết trước.

[pause] Tội danh thứ tư gây tranh cãi nhất. Trong chương cuối, truyện hé lộ Eren đã tác động tới quá khứ qua sức mạnh nhìn ký ức, góp phần vào chính những bi kịch trong gia đình mình, kể cả cái chết của mẹ.

[pause] Công tố kết luận phần cáo trạng: dù hoàn cảnh ra sao, không có lý do nào biện minh cho việc giết phần lớn nhân loại.
```

### c04 · Lời bào chữa

Khoảng 104 giây · cảnh s28–s36 · 1357 ký tự

**Gemini**

```text
Luật sư bào chữa xin trình bày. Trước hết, hãy nhìn vào hoàn cảnh. Người Eldia bị áp bức suốt hàng chục năm, bị coi là quỷ chỉ vì dòng máu.

<short pause> Thế giới bên ngoài không chỉ ghét hòn đảo. Họ đang chuẩn bị tấn công nó. Với Eren, nếu không làm gì, những người cậu yêu thương chắc chắn sẽ chết.

<short pause> Bào chữa cũng chỉ ra: lựa chọn còn lại mà Eren có là kế hoạch của Zeke, để chính dân tộc mình tự biến mất. Với Eren, đó không phải hòa bình mà là đầu hàng.

<short pause> Thứ hai, sức mạnh Tiến công cho Eren thấy ký ức của tương lai. Cậu nói rằng tương lai ấy như đã được định sẵn. Câu hỏi đặt ra là: cậu có thật sự được tự do lựa chọn không?

<short pause> Không còn người khổng lồ, người Eldia không còn bị coi là mối đe dọa sinh học. Bào chữa lập luận: đây là điều mà không một cuộc đàm phán nào trước đó làm được.

<short pause> Thứ ba, kết quả cuối cùng của câu chuyện: sức mạnh người khổng lồ biến mất vĩnh viễn. Lời nguyền kéo dài hai nghìn năm chấm dứt.

<short pause> Và thứ tư: Eren đã chủ động để chính bạn bè mình chặn cậu lại. Bằng cách trở thành kẻ thù chung, cậu biến những người bạn thành anh hùng cứu thế giới, những người mà thế giới sẽ khó lòng căm ghét.

<short pause> Bào chữa kết luận: Eren là sản phẩm của một vòng thù hận mà cậu không tạo ra. Cậu đã chọn một con đường khủng khiếp, nhưng trong một thế giới chỉ cho cậu những con đường khủng khiếp.

<short pause> <laugh> Kaku ghi chép lại mà không bình luận. Việc của thư ký là ghi đủ, không ghi thiên.
```

**ElevenLabs**

```text
Luật sư bào chữa xin trình bày. Trước hết, hãy nhìn vào hoàn cảnh. Người Eldia bị áp bức suốt hàng chục năm, bị coi là quỷ chỉ vì dòng máu.

[pause] Thế giới bên ngoài không chỉ ghét hòn đảo. Họ đang chuẩn bị tấn công nó. Với Eren, nếu không làm gì, những người cậu yêu thương chắc chắn sẽ chết.

[pause] Bào chữa cũng chỉ ra: lựa chọn còn lại mà Eren có là kế hoạch của Zeke, để chính dân tộc mình tự biến mất. Với Eren, đó không phải hòa bình mà là đầu hàng.

[pause] Thứ hai, sức mạnh Tiến công cho Eren thấy ký ức của tương lai. Cậu nói rằng tương lai ấy như đã được định sẵn. [curious] Câu hỏi đặt ra là: cậu có thật sự được tự do lựa chọn không?

[pause] Không còn người khổng lồ, người Eldia không còn bị coi là mối đe dọa sinh học. Bào chữa lập luận: đây là điều mà không một cuộc đàm phán nào trước đó làm được.

[pause] Thứ ba, kết quả cuối cùng của câu chuyện: sức mạnh người khổng lồ biến mất vĩnh viễn. Lời nguyền kéo dài hai nghìn năm chấm dứt.

[pause] Và thứ tư: Eren đã chủ động để chính bạn bè mình chặn cậu lại. Bằng cách trở thành kẻ thù chung, cậu biến những người bạn thành anh hùng cứu thế giới, những người mà thế giới sẽ khó lòng căm ghét.

[pause] Bào chữa kết luận: Eren là sản phẩm của một vòng thù hận mà cậu không tạo ra. Cậu đã chọn một con đường khủng khiếp, nhưng trong một thế giới chỉ cho cậu những con đường khủng khiếp.

[pause] [chuckles] Kaku ghi chép lại mà không bình luận. Việc của thư ký là ghi đủ, không ghi thiên.
```

### c05 · Nhân chứng 1: Reiner / Nhân chứng 2: Gabi

Khoảng 122 giây · cảnh s37–s47 · 1580 ký tự

**Gemini**

```text
Tòa mời nhân chứng thứ nhất: Reiner Braun, chiến binh Marley từng phá bức tường năm Eren mười tuổi.

<short pause> Trước cuộc tấn công Liberio, Eren gặp Reiner trong một tầng hầm. Và Eren nói một câu mà nhiều người nhớ mãi: Tôi cũng giống anh.

<short pause> Ý của Eren: Reiner từng phá tường, giết người trên đảo, vì tin mình đang cứu thế giới khỏi quỷ. Giờ Eren sắp làm điều tương tự với thế giới của Reiner, vì cùng một lý do.

<short pause> Về sau, chính Reiner cũng chiến đấu để ngăn Địa minh, cùng những người từng là kẻ thù của anh. Một người từng phá tường giờ đứng chắn trước bức tường người khổng lồ.

<short pause> Lời khai này có lợi cho ai? Bào chữa nói nó cho thấy Eren hiểu vòng thù hận. Công tố nói: hiểu mà vẫn làm, thì càng đáng trách.

<short pause> Nhân chứng thứ hai: Gabi Braun, cô bé người Eldia ở Marley, được dạy từ nhỏ rằng người trên đảo là quỷ.

<short pause> Người bạn Falco của Gabi thì từ đầu đã không muốn thù hận. Cậu bé chỉ muốn Gabi được sống. Hai đứa trẻ này là hình ảnh ngược lại với Eren và những người bạn của cậu.

<short pause> Sau cuộc tấn công, Gabi lên đảo trả thù. Cô gây ra cái chết của Sasha, một người bạn của Eren. <short pause> Nhưng rồi cô sống giữa những người mà cô từng gọi là quỷ, và nhận ra họ cũng là con người.

<short pause> Công tố dùng nhân chứng này làm bằng chứng quan trọng: vòng thù hận có thể bị phá vỡ bằng sự thấu hiểu, không cần tới việc tiêu diệt. Gabi làm được, sao Eren lại không chọn con đường đó?

<short pause> <laugh> Kaku ghi nhận: đây là một trong những cuộc tranh luận hay nhất của phiên tòa. Cả hai bên đều dùng cùng một nhân chứng, và cả hai đều có lý.

<short pause> Bào chữa phản biện: một cô bé thay đổi không có nghĩa là cả thế giới thay đổi kịp, khi chiến hạm đã ở ngoài khơi.
```

**ElevenLabs**

```text
Tòa mời nhân chứng thứ nhất: Reiner Braun, chiến binh Marley từng phá bức tường năm Eren mười tuổi.

[pause] Trước cuộc tấn công Liberio, Eren gặp Reiner trong một tầng hầm. Và Eren nói một câu mà nhiều người nhớ mãi: Tôi cũng giống anh.

[pause] Ý của Eren: Reiner từng phá tường, giết người trên đảo, vì tin mình đang cứu thế giới khỏi quỷ. Giờ Eren sắp làm điều tương tự với thế giới của Reiner, vì cùng một lý do.

[pause] Về sau, chính Reiner cũng chiến đấu để ngăn Địa minh, cùng những người từng là kẻ thù của anh. Một người từng phá tường giờ đứng chắn trước bức tường người khổng lồ.

[pause] [curious] Lời khai này có lợi cho ai? Bào chữa nói nó cho thấy Eren hiểu vòng thù hận. Công tố nói: hiểu mà vẫn làm, thì càng đáng trách.

[pause] Nhân chứng thứ hai: Gabi Braun, cô bé người Eldia ở Marley, được dạy từ nhỏ rằng người trên đảo là quỷ.

[pause] Người bạn Falco của Gabi thì từ đầu đã không muốn thù hận. Cậu bé chỉ muốn Gabi được sống. Hai đứa trẻ này là hình ảnh ngược lại với Eren và những người bạn của cậu.

[pause] Sau cuộc tấn công, Gabi lên đảo trả thù. Cô gây ra cái chết của Sasha, một người bạn của Eren. [pause] Nhưng rồi cô sống giữa những người mà cô từng gọi là quỷ, và nhận ra họ cũng là con người.

[pause] Công tố dùng nhân chứng này làm bằng chứng quan trọng: vòng thù hận có thể bị phá vỡ bằng sự thấu hiểu, không cần tới việc tiêu diệt. Gabi làm được, sao Eren lại không chọn con đường đó?

[pause] [chuckles] Kaku ghi nhận: đây là một trong những cuộc tranh luận hay nhất của phiên tòa. Cả hai bên đều dùng cùng một nhân chứng, và cả hai đều có lý.

[pause] Bào chữa phản biện: một cô bé thay đổi không có nghĩa là cả thế giới thay đổi kịp, khi chiến hạm đã ở ngoài khơi.
```

### c06 · Nhân chứng 3: Armin / Nhân chứng 4: Mikasa

Khoảng 131 giây · cảnh s48–s59 · 1697 ký tự

**Gemini**

```text
Nhân chứng thứ ba: Armin Arlert, bạn thân nhất của Eren từ thuở nhỏ, người từng cùng cậu mơ về biển cả bên ngoài bức tường.

<short pause> Trong cuộc trò chuyện cuối cùng ở một không gian ngoài thời gian, Eren thừa nhận một điều rất con người: một phần trong cậu đã muốn làm điều đó, muốn san phẳng tất cả.

<short pause> Armin là người đã chiến đấu để ngăn bạn mình. <short pause> Nhưng cậu cũng là người duy nhất nghe Eren nói thật lòng, và cậu không quay lưng lại với bạn trong giây phút cuối.

<short pause> Nhưng cậu cũng thừa nhận mình không muốn chết, muốn được sống bên bạn bè. Một thiếu niên sợ hãi đằng sau kẻ gây ra thảm họa.

<short pause> Có một chi tiết thú vị cho bồi thẩm: một câu nói của Armin trong cuộc trò chuyện này ở manga từng gây tranh cãi dữ dội, và bản anime đã chỉnh lại lời thoại. Kaku ghi cần kiểm lại nguyên văn.

<short pause> Lời khai của Armin khó xếp vào bên nào. Nó cho thấy Eren vừa có lựa chọn, vừa bị dằn vặt bởi lựa chọn đó.

<short pause> Nhân chứng cuối cùng: Mikasa Ackerman, người luôn ở bên Eren từ nhỏ.

<short pause> Chính Mikasa là người kết thúc Địa minh bằng một lựa chọn rất đau đớn: cô ngăn Eren lại bằng chính tay mình. Và theo truyện, lựa chọn đó giải phóng Ymir, người khởi đầu lời nguyền.

<short pause> Truyện gợi ý rằng Ymir, người khổng lồ đầu tiên, đã bị trói buộc hai nghìn năm bởi một tình yêu dành cho kẻ đã đối xử tệ với mình. Mikasa thì khác: cô yêu nhưng vẫn chọn buông tay. Lựa chọn đó cắt đứt sợi xích.

<short pause> <laugh> Kaku ghi chép mà tay hơi run. Trong cả phiên tòa, đây là lời khai khó ghi nhất.

<short pause> Lời khai của Mikasa không bằng lời, mà bằng hành động: cô yêu Eren, và vẫn chọn ngăn cậu lại. Với nhiều người, đó là phán quyết rõ nhất trong truyện.

<short pause> Nhưng hãy nhớ: truyện cũng cho thấy Eren đã biết trước và chờ đợi lựa chọn ấy. Đến cả khoảnh khắc bị ngăn lại cũng nằm trong kế hoạch của cậu.
```

**ElevenLabs**

```text
Nhân chứng thứ ba: Armin Arlert, bạn thân nhất của Eren từ thuở nhỏ, người từng cùng cậu mơ về biển cả bên ngoài bức tường.

[pause] Trong cuộc trò chuyện cuối cùng ở một không gian ngoài thời gian, Eren thừa nhận một điều rất con người: một phần trong cậu đã muốn làm điều đó, muốn san phẳng tất cả.

[pause] Armin là người đã chiến đấu để ngăn bạn mình. [pause] Nhưng cậu cũng là người duy nhất nghe Eren nói thật lòng, và cậu không quay lưng lại với bạn trong giây phút cuối.

[pause] Nhưng cậu cũng thừa nhận mình không muốn chết, muốn được sống bên bạn bè. Một thiếu niên sợ hãi đằng sau kẻ gây ra thảm họa.

[pause] Có một chi tiết thú vị cho bồi thẩm: một câu nói của Armin trong cuộc trò chuyện này ở manga từng gây tranh cãi dữ dội, và bản anime đã chỉnh lại lời thoại. Kaku ghi cần kiểm lại nguyên văn.

[pause] Lời khai của Armin khó xếp vào bên nào. Nó cho thấy Eren vừa có lựa chọn, vừa bị dằn vặt bởi lựa chọn đó.

[pause] Nhân chứng cuối cùng: Mikasa Ackerman, người luôn ở bên Eren từ nhỏ.

[pause] Chính Mikasa là người kết thúc Địa minh bằng một lựa chọn rất đau đớn: cô ngăn Eren lại bằng chính tay mình. Và theo truyện, lựa chọn đó giải phóng Ymir, người khởi đầu lời nguyền.

[pause] Truyện gợi ý rằng Ymir, người khổng lồ đầu tiên, đã bị trói buộc hai nghìn năm bởi một tình yêu dành cho kẻ đã đối xử tệ với mình. Mikasa thì khác: cô yêu nhưng vẫn chọn buông tay. Lựa chọn đó cắt đứt sợi xích.

[pause] [chuckles] Kaku ghi chép mà tay hơi run. Trong cả phiên tòa, đây là lời khai khó ghi nhất.

[pause] Lời khai của Mikasa không bằng lời, mà bằng hành động: cô yêu Eren, và vẫn chọn ngăn cậu lại. Với nhiều người, đó là phán quyết rõ nhất trong truyện.

[pause] Nhưng hãy nhớ: truyện cũng cho thấy Eren đã biết trước và chờ đợi lựa chọn ấy. Đến cả khoảnh khắc bị ngăn lại cũng nằm trong kế hoạch của cậu.
```

### c07 · Luận điểm cuối của công tố / Luận điểm cuối của bào chữa

Khoảng 100 giây · cảnh s60–s68 · 1296 ký tự

**Gemini**

```text
Công tố tổng kết. Bị cáo đã giết phần lớn nhân loại, trong đó có vô số người vô tội, trẻ em, những người chưa từng biết tới hòn đảo.

<short pause> Công tố cũng lưu ý: nhiều người trong số những người chết không hề cầm vũ khí, không hề biết tới Paradis, và không liên quan gì tới quyết định của các chính phủ.

<short pause> Bị cáo có những lựa chọn khác. Gabi chứng minh sự thấu hiểu là có thể. Bị cáo thừa nhận một phần trong mình muốn làm điều đó.

<short pause> Công tố còn đặt câu hỏi: nếu Eren thấy trước tương lai, thì cậu cũng thấy trước con số. Biết trước mà vẫn làm là một lựa chọn, không phải số phận.

<short pause> Và kế hoạch biến bạn bè thành anh hùng không thay đổi được con số. Không có mục đích nào đủ lớn để biện minh cho tám mươi phần trăm.

<short pause> Bào chữa tổng kết. Không ai phủ nhận thảm họa. <short pause> Nhưng bị cáo sinh ra trong một thế giới đã chọn sẵn hòn đảo làm vật hi sinh.

<short pause> Bào chữa cũng nhắc: sau Địa minh, những người sống sót trên đảo và ngoài đảo lần đầu tiên phải ngồi lại với nhau. Một thế giới tan hoang, nhưng không còn sức mạnh nào để thù hận nhắm vào.

<short pause> Bị cáo thấy một tương lai mà cậu tin là không thể thay đổi. Cậu gánh lấy tội lỗi lớn nhất lịch sử, để kết thúc lời nguyền và để bạn bè mình được sống như những người anh hùng.

<short pause> Bào chữa không xin tòa gọi bị cáo là người tốt. Chỉ xin tòa hiểu rằng câu chuyện này không có lựa chọn nào sạch sẽ.
```

**ElevenLabs**

```text
Công tố tổng kết. Bị cáo đã giết phần lớn nhân loại, trong đó có vô số người vô tội, trẻ em, những người chưa từng biết tới hòn đảo.

[pause] Công tố cũng lưu ý: nhiều người trong số những người chết không hề cầm vũ khí, không hề biết tới Paradis, và không liên quan gì tới quyết định của các chính phủ.

[pause] Bị cáo có những lựa chọn khác. Gabi chứng minh sự thấu hiểu là có thể. Bị cáo thừa nhận một phần trong mình muốn làm điều đó.

[pause] Công tố còn đặt câu hỏi: nếu Eren thấy trước tương lai, thì cậu cũng thấy trước con số. Biết trước mà vẫn làm là một lựa chọn, không phải số phận.

[pause] Và kế hoạch biến bạn bè thành anh hùng không thay đổi được con số. Không có mục đích nào đủ lớn để biện minh cho tám mươi phần trăm.

[pause] Bào chữa tổng kết. Không ai phủ nhận thảm họa. [pause] Nhưng bị cáo sinh ra trong một thế giới đã chọn sẵn hòn đảo làm vật hi sinh.

[pause] Bào chữa cũng nhắc: sau Địa minh, những người sống sót trên đảo và ngoài đảo lần đầu tiên phải ngồi lại với nhau. Một thế giới tan hoang, nhưng không còn sức mạnh nào để thù hận nhắm vào.

[pause] Bị cáo thấy một tương lai mà cậu tin là không thể thay đổi. Cậu gánh lấy tội lỗi lớn nhất lịch sử, để kết thúc lời nguyền và để bạn bè mình được sống như những người anh hùng.

[pause] Bào chữa không xin tòa gọi bị cáo là người tốt. Chỉ xin tòa hiểu rằng câu chuyện này không có lựa chọn nào sạch sẽ.
```

### c08 · Góc nhìn của Kaku: vì sao tác giả không tuyên án / Bồi thẩm bỏ phiếu / Kết

Khoảng 136 giây · cảnh s69–s82 · 1763 ký tự

**Gemini**

```text
Cái kết của Attack on Titan ra mắt năm 2021 ở manga và năm 2023 ở anime, và tới giờ vẫn chia rẽ người đọc. Có người thấy trọn vẹn, có người thấy hụt hẫng. Chính sự chia rẽ ấy là lý do phiên tòa này tồn tại.

<short pause> Kaku có một nhận xét cuối, không phải phán quyết. Tác giả Isayama không đưa ra câu trả lời rõ ràng. Ông để nhân vật của mình vừa đáng thương, vừa đáng sợ.

<short pause> Tên truyện trong tiếng Nhật có thể hiểu là người khổng lồ tấn công. <short pause> Nhưng đến cuối, câu hỏi thật sự là: ai mới là người tấn công, và ai là người bị tấn công?

<short pause> Và có lẽ đó là chủ đích. Attack on Titan là câu chuyện về việc mỗi bên đều nghĩ mình đang chiến đấu cho tự do, và đều gọi bên kia là quỷ.

<short pause> Nếu bạn thấy khó bỏ phiếu, đó là dấu hiệu bạn đã hiểu câu chuyện. Một phiên tòa dễ dàng thì không cần tới bồi thẩm.

<short pause> Giờ tới lượt bạn. Phương án A: có tội, không có tình tiết giảm nhẹ.

<short pause> Phương án B: có tội, nhưng có tình tiết giảm nhẹ vì hoàn cảnh và mục đích.

<short pause> Phương án C: không thể phán xét theo luật thông thường, vì đây là một thế giới không có lựa chọn đúng.

<short pause> Và nếu bạn chọn khác với số đông, đừng ngại. Một bồi thẩm tốt là người nói ra lý do của mình, không phải người đoán xem mọi người chọn gì.

<short pause> Hãy bình luận chữ cái bạn chọn, kèm một câu lý do. Kaku sẽ đếm phiếu và công bố kết quả ở phần ghim bình luận.

<short pause> Eren từng mơ được nhìn thấy biển. Cậu đã nhìn thấy nó, và rồi cậu chọn đi qua nó theo cách không ai có thể quên.

<short pause> Nếu bạn đã đi cùng Kaku từ video đầu tiên về Nen, cảm ơn bạn rất nhiều. Ba mươi chín cuốn sổ đã mở, và Kaku còn rất nhiều cuốn nữa.

<short pause> Video tiếp theo là một món quà cho fan Sakamoto Days: mười lăm phút ôn tập mọi thứ cần nhớ trước khi mùa hai lên sóng.

<short pause> <laugh> Nếu bạn thích dạng phiên tòa này và muốn Kaku xử thêm nhân vật khác, hãy đăng ký kênh và đề cử bị cáo tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Cái kết của Attack on Titan ra mắt năm 2021 ở manga và năm 2023 ở anime, và tới giờ vẫn chia rẽ người đọc. Có người thấy trọn vẹn, có người thấy hụt hẫng. Chính sự chia rẽ ấy là lý do phiên tòa này tồn tại.

[pause] Kaku có một nhận xét cuối, không phải phán quyết. Tác giả Isayama không đưa ra câu trả lời rõ ràng. Ông để nhân vật của mình vừa đáng thương, vừa đáng sợ.

[pause] Tên truyện trong tiếng Nhật có thể hiểu là người khổng lồ tấn công. [pause] [curious] Nhưng đến cuối, câu hỏi thật sự là: ai mới là người tấn công, và ai là người bị tấn công?

[pause] Và có lẽ đó là chủ đích. Attack on Titan là câu chuyện về việc mỗi bên đều nghĩ mình đang chiến đấu cho tự do, và đều gọi bên kia là quỷ.

[pause] Nếu bạn thấy khó bỏ phiếu, đó là dấu hiệu bạn đã hiểu câu chuyện. Một phiên tòa dễ dàng thì không cần tới bồi thẩm.

[pause] Giờ tới lượt bạn. Phương án A: có tội, không có tình tiết giảm nhẹ.

[pause] Phương án B: có tội, nhưng có tình tiết giảm nhẹ vì hoàn cảnh và mục đích.

[pause] Phương án C: không thể phán xét theo luật thông thường, vì đây là một thế giới không có lựa chọn đúng.

[pause] Và nếu bạn chọn khác với số đông, đừng ngại. Một bồi thẩm tốt là người nói ra lý do của mình, không phải người đoán xem mọi người chọn gì.

[pause] Hãy bình luận chữ cái bạn chọn, kèm một câu lý do. Kaku sẽ đếm phiếu và công bố kết quả ở phần ghim bình luận.

[pause] Eren từng mơ được nhìn thấy biển. Cậu đã nhìn thấy nó, và rồi cậu chọn đi qua nó theo cách không ai có thể quên.

[pause] Nếu bạn đã đi cùng Kaku từ video đầu tiên về Nen, cảm ơn bạn rất nhiều. Ba mươi chín cuốn sổ đã mở, và Kaku còn rất nhiều cuốn nữa.

[pause] Video tiếp theo là một món quà cho fan Sakamoto Days: mười lăm phút ôn tập mọi thứ cần nhớ trước khi mùa hai lên sóng.

[pause] [chuckles] Nếu bạn thích dạng phiên tòa này và muốn Kaku xử thêm nhân vật khác, hãy đăng ký kênh và đề cử bị cáo tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```
