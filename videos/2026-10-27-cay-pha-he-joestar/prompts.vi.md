# Bộ prompt · JoJo: Cây phả hệ Joestar và bí mật của dấu ngôi sao

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 8 đoạn đọc, khoảng 15.0 phút giọng.
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

Lời: Cảnh báo spoiler: video này đi qua sáu phần đầu của JoJo, kể cả cái kết của phần sáu, và nhắc sơ qua phần bảy…

```text
Wide 16:9 landscape cinematic frame. an ornate old family album closed on a wooden table beside a spoiler warning card, close-up, warm vintage light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Năm 1888, ở nước Anh, một chàng trai quý tộc tên Jonathan Joestar chiến đấu với người anh nuôi của mình. Hơn…

```text
Wide 16:9 landscape cinematic frame. a Victorian English mansion at dusk on the left and a modern prison fence under a Florida sky on the right, split composition, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Giữa hai người đó là năm thế hệ, một mối thù truyền kiếp, và một dấu hiệu nhỏ hình ngôi sao mà mọi người tron…

```text
Wide 16:9 landscape cinematic frame. a large family tree painted on an old wall with small golden stars glowing beside several names, wide shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: JoJo là bộ truyện của Araki Hirohiko, bắt đầu năm 1987 và vẫn tiếp tục tới hôm nay. Mỗi phần có một nhân vật…

```text
Wide 16:9 landscape cinematic frame. a long shelf of manga volumes arranged by colored spine sections, close-up, warm bookstore light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ Joestar: gốc rễ, các nhánh, những nhánh con bất ngờ, v…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a large rolled-up family tree scroll with both wings, looking excited. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Và vì phần bảy, Steel Ball Run, đang lên anime trên Netflix, video này cũng là bản đồ để bạn hiểu vì sao phần…

```text
Wide 16:9 landscape cinematic frame. a vast desert racetrack stretching to the horizon at sunrise with a few distant horse riders, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Cách đọc cây phả hệ

Lời: Trước khi vẽ, ba quy tắc đọc. Một: mỗi phần của JoJo có một nhân vật chính, gọi là một JoJo, và phần lớn là n…

```text
Wide 16:9 landscape cinematic frame. a numbered list on parchment with three small icons: a portrait frame, a star, and a branching line, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Hai: biệt danh JoJo đến từ cách chơi chữ trên tên. Ví dụ Jonathan Joestar thành Jo cộng Jo. Có những JoJo man…

```text
Wide 16:9 landscape cinematic frame. two syllables written in large brush strokes on paper, combined with a small plus sign, close-up, playful amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Ba: hầu hết người trong dòng họ có một vết hình ngôi sao ở sau vai trái, gần gáy. Đó là chìa khóa để nhận ra…

```text
Wide 16:9 landscape cinematic frame. a small gold star symbol drawn on an anatomical outline of a shoulder on parchment, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: trong JoJo, dòng máu quan trọng hơn cái họ. Và như ta sẽ thấy, có cả một người mang dấu ngôi sao n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot squinting at a family tree through a magnifying glass, puzzled. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Gốc: Jonathan Joestar, phần một

Lời: Gốc của cây là George Joestar đệ nhất, một quý tộc Anh. Ông nhận nuôi một cậu bé tên Dio Brando, vì tin rằng…

```text
Wide 16:9 landscape cinematic frame. a grand English manor house with a horse carriage arriving at the gate on a grey afternoon, wide shot, Victorian light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Con trai ruột của ông là Jonathan, một chàng trai tốt bụng, lịch thiệp. Dio thì mang tham vọng chiếm đoạt cả…

```text
Wide 16:9 landscape cinematic frame. two young men's silhouettes standing on opposite sides of a long dining table in a candlelit hall, wide shot, tense warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Jonathan học Hamon từ một người thầy tên Zeppeli. Nguyên lý: kiểm soát hơi thở để tạo ra năng lượng giống ánh…

```text
Wide 16:9 landscape cinematic frame. a figure breathing deeply on a hilltop at sunrise with faint golden ripples of energy around him, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Dio dùng một chiếc mặt nạ đá cổ để biến thành ma cà rồng. Jonathan học một kỹ thuật thở gọi là Hamon, sức mạn…

```text
Wide 16:9 landscape cinematic frame. an ancient carved stone mask resting on a velvet cloth in a dim study, close-up, ominous warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Trận cuối diễn ra trên một con tàu. Jonathan chết, nhưng mang theo cả Dio xuống đáy biển. Hay ít nhất là mọi…

```text
Wide 16:9 landscape cinematic frame. a large ship burning on a dark ocean at night, flames reflecting on the waves, wide shot, dramatic orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Và đây là chi tiết quyết định cả cây phả hệ: vợ Jonathan, Erina, sống sót, đang mang thai. Cô trốn thoát tron…

```text
Wide 16:9 landscape cinematic frame. a wooden coffin drifting on calm sea at dawn with a small bundle of cloth visible inside, wide shot, soft pale light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nếu Erina không sống sót, cây phả hệ đã kết thúc ngay ở gốc. Mọi JoJo về sau đều nợ mạng sống của mình cho ch…

```text
Wide 16:9 landscape cinematic frame. a single seed floating on water beside a drifting wooden box, symbolic close-up, hopeful dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Nhánh 1: George đệ nhị và Joseph, phần hai

Lời: Đứa con Erina mang trong bụng là George Joestar đệ nhị. Và bé gái được cứu cùng chiếc quan tài lớn lên thành…

```text
Wide 16:9 landscape cinematic frame. an old sepia photograph of a young man and a young woman standing together in a garden, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: George đệ nhị và Elizabeth yêu nhau và cưới nhau. Họ có một con trai: Joseph Joestar.

```text
Wide 16:9 landscape cinematic frame. a baby's cradle beside a window in an English house with soft sunlight falling across it, close-up, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng George đệ nhị bị một kẻ thuộc phe Dio sát hại. Elizabeth phải rời đi để trả thù và lẩn trốn, và Joseph…

```text
Wide 16:9 landscape cinematic frame. an elderly woman holding the hand of a small boy while walking along a seaside path, back view, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Kẻ thù của phần hai không phải Dio, mà là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá. Cây phả hệ Joestar…

```text
Wide 16:9 landscape cinematic frame. ancient stone pillars in a ruined Roman temple with strange carvings, wide shot, mysterious golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Năm 1938, Joseph, một chàng trai ranh mãnh, hay đoán trước câu nói của đối thủ, trở thành JoJo thứ hai. Cậu h…

```text
Wide 16:9 landscape cinematic frame. a young man grinning confidently while pointing at an opponent on a cliffside at sunset, medium shot, warm dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Kaku để ý: đây là nhánh đầu tiên cho thấy cây phả hệ JoJo đầy những bí mật gia đình. Người thầy hóa ra là mẹ.…

```text
Wide 16:9 landscape cinematic frame. a locket opened to reveal a small portrait inside, extreme close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Sau phần hai, Joseph cưới Suzi Q, cô bạn người Ý của mẹ mình. Họ có một con gái, Holly.

```text
Wide 16:9 landscape cinematic frame. a small wedding photo in an ornate frame on a mantelpiece, close-up, warm soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Nhánh 2: Holly và Jotaro, phần ba

Lời: Holly Joestar cưới một nhạc công người Nhật, Kujo Sadao, và chuyển tới Nhật. Con trai họ là Kujo Jotaro, JoJo…

```text
Wide 16:9 landscape cinematic frame. a traditional Japanese house with a jazz record player on the veranda, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Năm 1987, gần một trăm năm sau con tàu cháy, Dio trở lại. Hắn không chết dưới đáy biển. Hắn đã lấy cơ thể của…

```text
Wide 16:9 landscape cinematic frame. a coffin rising from the dark seabed surrounded by bubbles, low-angle shot, ominous green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Và vì Dio mang cơ thể của Jonathan, dòng máu Joestar trong hắn đánh thức một sức mạnh mới ở cả dòng họ: Stand…

```text
Wide 16:9 landscape cinematic frame. a ghostly translucent figure rising behind a seated silhouette, symbolic medium shot, dramatic purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Mỗi thành viên trong dòng họ có một Stand khác nhau, phản ánh con người họ. Joseph có Stand dạng dây leo gai,…

```text
Wide 16:9 landscape cinematic frame. two contrasting ghostly shapes side by side, one made of thorny vines and one a powerful humanoid silhouette, symbolic close-up, purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Holly không đủ sức chịu Stand của mình, và ngã bệnh nặng. Jotaro, Joseph và những người bạn lên đường tới Ai…

```text
Wide 16:9 landscape cinematic frame. a small group of travelers walking across a desert toward distant pyramids at sunset, back view, wide shot, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Điều thú vị: các Joestar có thể cảm nhận Dio qua dòng máu chung, vì hắn đang mang cơ thể tổ tiên họ. Cây phả…

```text
Wide 16:9 landscape cinematic frame. several points of light on a map connected by thin glowing threads converging on one dark point, parchment close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Phần ba khép lại khi Jotaro đánh bại Dio. Cơ thể của Jonathan, sau một trăm năm, cuối cùng cũng được yên nghỉ.

```text
Wide 16:9 landscape cinematic frame. a sunrise over a desert city with a quiet empty street, wide shot, peaceful warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Những người phụ nữ giữ gốc cây

Lời: Trước khi sang nhánh tiếp theo, Kaku muốn dừng lại ở những người thường bị bỏ quên trên cây phả hệ JoJo: nhữn…

```text
Wide 16:9 landscape cinematic frame. a row of old portraits of women in different eras hanging on a wall of a family hall, wide shot, warm respectful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Erina cứu cả dòng họ bằng cách sống sót trên biển. Lisa Lisa giấu thân phận để bảo vệ con trai. Erina lại nuô…

```text
Wide 16:9 landscape cinematic frame. an elderly woman's hands knitting beside a window with a child's small jacket on her lap, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Holly chịu đựng Stand của mình trong im lặng, mỉm cười để con trai không lo. Tomoko nuôi Josuke một mình suốt…

```text
Wide 16:9 landscape cinematic frame. a mother smiling gently while hiding a tired expression in a sunlit kitchen, medium shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: các JoJo là người chiến đấu, nhưng chính những người phụ nữ này là người giữ cho cây không bị bật…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing a small flower beside a row of old portraits with a respectful bow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Nhánh con bất ngờ: Josuke, phần bốn

Lời: Năm 1999, ở thị trấn Morioh, Nhật Bản, cây phả hệ mọc thêm một nhánh không ai biết: Higashikata Josuke.

```text
Wide 16:9 landscape cinematic frame. a peaceful Japanese suburban town with a small train station and houses on a hillside, wide shot, bright summer light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Josuke là con ngoài giá thú của Joseph Joestar, với một phụ nữ Nhật tên Tomoko, từ nhiều năm trước. Joseph ch…

```text
Wide 16:9 landscape cinematic frame. a letter in an old envelope resting on a table beside a faded photograph, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Điều khiến fan cười nhiều nhất: Josuke là chú của Jotaro, dù trẻ hơn Jotaro nhiều tuổi. Một thiếu niên mười s…

```text
Wide 16:9 landscape cinematic frame. two silhouettes side by side, a tall adult and a shorter teen, with a family tree arrow pointing from the teen down to the adult, humorous infographic, bright light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Phần bốn cũng là phần ít có mối thù Dio nhất. Nó là câu chuyện về một thị trấn nhỏ và những bí ẩn đời thường.…

```text
Wide 16:9 landscape cinematic frame. a quiet small-town street with a café, a school and a cat sleeping on a wall, wide shot, lazy summer light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Josuke có Stand chữa lành và sửa chữa mọi thứ, trừ chính bản thân mình. Một nhánh con mang năng lực phục hồi,…

```text
Wide 16:9 landscape cinematic frame. a broken vase reassembling itself piece by piece in midair, dynamic close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Kaku để ý: nhánh Josuke cho thấy cây phả hệ JoJo không hoàn hảo. Có những bí mật, những lỗi lầm, nhưng cuối c…

```text
Wide 16:9 landscape cinematic frame. an elderly man and a teenager standing awkwardly side by side at a train station, then shaking hands, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Nhánh lạc: Giorno, phần năm

Lời: Năm 2001, ở Ý, một chàng trai mười lăm tuổi tên Giorno Giovanna mơ trở thành trùm băng đảng để làm sạch thành…

```text
Wide 16:9 landscape cinematic frame. a sunny Italian coastal city with narrow streets and laundry lines between buildings, wide shot, bright Mediterranean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Giorno có dấu ngôi sao trên vai. Nhưng cậu là con của Dio. Làm sao con của kẻ thù lại mang dấu hiệu của dòng…

```text
Wide 16:9 landscape cinematic frame. a question mark drawn beside a small gold star on a family tree branch that curves in from outside, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Câu trả lời: Giorno được sinh ra khi Dio đang dùng cơ thể của Jonathan. Về mặt di truyền, Giorno mang dòng má…

```text
Wide 16:9 landscape cinematic frame. two different colored threads twisting together into a single rope, extreme close-up, symbolic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Trong phần năm, Giorno gần như không gặp gia đình Joestar nào. Cậu tự đi con đường của mình, và chỉ người đọc…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing on a rooftop overlooking a city while a faint golden thread trails behind him into the distance, wide shot, warm dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Và thú vị hơn nữa: Giorno thừa hưởng từ Jonathan sự tử tế và lòng chính trực, từ Dio sự quyết đoán và tham vọ…

```text
Wide 16:9 landscape cinematic frame. a young sapling growing from the crack between two different stones, close-up, hopeful golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Giorno cũng có những người thầy và đồng đội tạo nên cậu, như băng nhóm của Bucciarati. Một lần nữa, gia đình…

```text
Wide 16:9 landscape cinematic frame. a small group of silhouettes walking together down a sunny Italian street, back view, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là nhánh đẹp nhất của cây. Mối thù bắt đầu từ Jonathan và Dio, cuối cùng sinh ra một người thừa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot carefully watering a small sapling growing between two rocks. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Nhánh bóng tối: những người con khác của Dio

Lời: Giorno không phải con duy nhất của Dio. Ở phần sáu, xuất hiện thêm ba người con trai khác, cũng mang dấu ngôi…

```text
Wide 16:9 landscape cinematic frame. three separate lonely silhouettes standing in different American landscapes, triptych composition, muted light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nếu Giorno chọn con đường ánh sáng, thì ba người này bị kéo vào phe bóng tối, như những quân cờ của một kẻ th…

```text
Wide 16:9 landscape cinematic frame. chess pieces on a board being pulled toward a dark square by unseen strings, close-up, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Kaku xếp họ vào nhánh bóng tối của cây: cùng một dòng máu, nhưng hoàn cảnh sống khác, lựa chọn khác, và số ph…

```text
Wide 16:9 landscape cinematic frame. a family tree drawing with one branch shaded dark and drooping, parchment close-up, amber and grey ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Ngọn cây: Jolyne, phần sáu

Lời: Năm 2011, ở Florida, Kujo Jolyne, con gái của Jotaro, bị vu oan và đưa vào tù. Cô trở thành JoJo thứ sáu, và…

```text
Wide 16:9 landscape cinematic frame. a prison yard under a hot Florida sky with a tall fence and a single figure standing defiantly, wide shot, harsh bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Kẻ đứng sau là một người từng là bạn thân của Dio, mang theo di sản và kế hoạch của hắn. Hơn một trăm hai mươ…

```text
Wide 16:9 landscape cinematic frame. an old diary with worn pages lying on a desk in a dim prison chapel, close-up, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Mối quan hệ cha con giữa Jotaro và Jolyne là trung tâm cảm xúc của phần sáu. Jotaro là người cha vắng mặt, nh…

```text
Wide 16:9 landscape cinematic frame. a father's large hand reaching toward a daughter's hand across a prison visiting table, close-up, emotional warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Jolyne có Stand biến cơ thể thành sợi chỉ. Kaku thấy đây là một biểu tượng đẹp: sợi chỉ nối các thế hệ của gi…

```text
Wide 16:9 landscape cinematic frame. a single glowing thread weaving through a family tree drawing connecting all the stars, close-up, warm magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Và cái kết của phần sáu, Kaku chỉ nói ngắn: nó thay đổi cả vũ trụ của JoJo. Cây phả hệ mà ta vừa vẽ, theo một…

```text
Wide 16:9 landscape cinematic frame. a massive tree silhouette slowly dissolving into light particles against a sunrise, wide shot, bittersweet radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Đó là lý do khi phần bảy bắt đầu, người đọc gặp một thế giới mới, với những người mang tên quen thuộc nhưng k…

```text
Wide 16:9 landscape cinematic frame. a fresh sapling growing in an empty field under a new sky, close-up, clean morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Gia đình không chỉ là dòng máu

Lời: Cây phả hệ JoJo còn có những nhánh không cùng dòng máu, nhưng gắn bó như người nhà.

```text
Wide 16:9 landscape cinematic frame. a family tree drawing with extra branches drawn in a different ink color reaching in from the sides, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Speedwagon, người bạn của Jonathan từ phần một, lập ra một quỹ mang tên mình. Quỹ Speedwagon hỗ trợ dòng họ J…

```text
Wide 16:9 landscape cinematic frame. an old foundation building with a brass nameplate on its door and a vintage car parked outside, wide shot, warm period light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Dòng họ Zeppeli cũng song hành: Will A. Zeppeli dạy Hamon cho Jonathan, và cháu ông, Caesar, trở thành người…

```text
Wide 16:9 landscape cinematic frame. two old portraits of mentors side by side in oval frames on a wall, close-up, nostalgic sepia light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Và những người bạn đồng hành của Jotaro trên đường tới Ai Cập, nhiều người không trở về. Họ không mang dấu ng…

```text
Wide 16:9 landscape cinematic frame. a small campfire in the desert at night with several empty spots around it and one lone figure sitting, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Kaku thấy đây là thông điệp đẹp của JoJo: gia đình là những người sẵn sàng đi cùng bạn qua bóng tối, dù có cù…

```text
Wide 16:9 landscape cinematic frame. several hands of different ages and skin tones stacked together over a map, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Cây đối xứng: dòng họ Brando

Lời: Bên cạnh cây Joestar là một cây đối xứng: dòng họ Brando. Cha của Dio là một kẻ nghiện rượu tàn nhẫn, và Dio…

```text
Wide 16:9 landscape cinematic frame. a dark shabby London alley at night with a single dim gas lamp, wide shot, cold grim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Hai cây mọc cạnh nhau: một bên được nuôi bằng lòng tốt, một bên bằng tham vọng. Và hai cây quấn vào nhau khi…

```text
Wide 16:9 landscape cinematic frame. two trees with intertwined trunks, one with bright leaves and one with dark leaves, symbolic wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Kết quả của sự quấn vào nhau đó là Giorno, và cả những người con ở nhánh bóng tối. Một cây phả hệ không thể v…

```text
Wide 16:9 landscape cinematic frame. a single branch growing from where two different trunks fuse together, close-up, warm and dark mixed light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Vũ trụ mới: phần bảy, tám và chín

Lời: Phần bảy, Steel Ball Run, diễn ra ở nước Mỹ năm 1890, với một cuộc đua ngựa xuyên lục địa. Nhân vật chính là…

```text
Wide 16:9 landscape cinematic frame. horse riders racing across a wide desert with dust trails at sunrise, wide shot, golden adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Phần bảy được chuyển thể anime bởi David Production, phát trên Netflix từ tháng ba năm 2026, và phần hai của…

```text
Wide 16:9 landscape cinematic frame. a streaming screen glowing in a dark room with a desert landscape on it, close-up, cool screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Phần tám, JoJolion, lấy bối cảnh một thị trấn Morioh khác, với một Josuke khác. Và phần chín, The JOJOLands,…

```text
Wide 16:9 landscape cinematic frame. a tropical Hawaiian coastline with palm trees and a small town in the distance, wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Kaku gọi đây là cây phả hệ thứ hai: cùng những cái tên, cùng tinh thần, nhưng mọc ở một khu vườn khác. Muốn h…

```text
Wide 16:9 landscape cinematic frame. two separate family trees drawn side by side on parchment, similar in shape but with different leaves, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Bí mật của dấu ngôi sao

Lời: Quay lại dấu ngôi sao. Vì sao nó quan trọng tới vậy?

```text
Wide 16:9 landscape cinematic frame. a small gold star drawn on parchment with rays of light around it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Một: nó giúp nhận ra người nhà, như với Josuke và Giorno. Hai: nó là dấu hiệu của một dòng máu mà định mệnh l…

```text
Wide 16:9 landscape cinematic frame. a star stamp being pressed onto several different portraits in a row, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Có một thói quen thú vị của các Joestar: họ thường có những câu cửa miệng rất riêng, được fan nhớ mãi và bắt…

```text
Wide 16:9 landscape cinematic frame. a speech bubble card pinned to a family tree beside a small star, close-up, playful warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và ba, theo cách Kaku hiểu: nó là một lời nhắc rằng mỗi JoJo không chiến đấu một mình. Họ mang theo tinh thần…

```text
Wide 16:9 landscape cinematic frame. a row of faded silhouettes standing behind a young figure with small stars glowing on their shoulders, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Trong JoJo, điều này có tên: tinh thần hoàng kim. Sự dũng cảm và lòng tốt được truyền từ thế hệ này sang thế…

```text
Wide 16:9 landscape cinematic frame. a golden flame being passed from one candle to another along a row of candles, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Toàn bộ cây phả hệ

Lời: Và đây là cả cây trong một hình. Gốc: George đệ nhất và Jonathan, phần một, 1888. Erina sống sót trong quan t…

```text
Wide 16:9 landscape cinematic frame. a family tree on parchment with the root section illuminated and a small coffin icon beside it, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nhánh một: George đệ nhị và Lisa Lisa, sinh Joseph, phần hai, 1938. Joseph và Suzi Q, sinh Holly. Holly và Ku…

```text
Wide 16:9 landscape cinematic frame. the trunk of the family tree with several names and small stars illuminated, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và những nhánh ngoài dòng máu nhưng là gia đình: Speedwagon, dòng họ Zeppeli, và những người bạn đồng hành kh…

```text
Wide 16:9 landscape cinematic frame. extra branches drawn in a different ink color reaching into the tree from its sides, amber and green ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nhánh con: Joseph và Tomoko, sinh Josuke, phần bốn, 1999. Nhánh lạc: Dio trong cơ thể Jonathan, sinh Giorno,…

```text
Wide 16:9 landscape cinematic frame. the side branches of the tree with one bright branch and one shaded branch, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Ngọn cây: Jotaro sinh Jolyne, phần sáu, 2011. Và bên cạnh, một cây thứ hai bắt đầu mọc: Johnny, Josuke của Jo…

```text
Wide 16:9 landscape cinematic frame. the complete family tree with a small second sapling drawn beside it, wide overhead shot, radiant warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · Kết

Lời: Bạn thích JoJo nào nhất? Và bạn có để ý chi tiết gia đình nào khiến bạn bất ngờ nhất: mẹ là thầy, chú trẻ hơn…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny family tree doodle and a small star, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo, Kaku mở một cuốn sử khác: Vinland Saga, người Viking thật, và nhân vật Thorfinn có thật tron…

```text
Wide 16:9 landscape cinematic frame. a longship with a square sail on a misty northern sea under a grey sky, wide shot, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem Kaku vẽ cây phả hệ, hãy đăng ký kênh. Mỗi video là một chiếc lá mới trên cây của kênh. Kaku…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hanging a small leaf-shaped card on a tiny tree and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc cây phả hệ

Khoảng 122 giây · cảnh s01–s10 · 1587 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này đi qua sáu phần đầu của JoJo, kể cả cái kết của phần sáu, và nhắc sơ qua phần bảy, tám, chín. Nếu bạn đang xem dở, hãy lưu video lại.

<short pause> Năm 1888, ở nước Anh, một chàng trai quý tộc tên Jonathan Joestar chiến đấu với người anh nuôi của mình. Hơn một trăm năm sau, ở Florida, một cô gái trong tù chiến đấu với cùng một bóng ma của quá khứ.

<short pause> Giữa hai người đó là năm thế hệ, một mối thù truyền kiếp, và một dấu hiệu nhỏ hình ngôi sao mà mọi người trong dòng họ đều mang trên vai.

<short pause> JoJo là bộ truyện của Araki Hirohiko, bắt đầu năm 1987 và vẫn tiếp tục tới hôm nay. Mỗi phần có một nhân vật chính mới, và gần như ai cũng có biệt danh JoJo.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ Joestar: gốc rễ, các nhánh, những nhánh con bất ngờ, và cả những nhánh đã mất. Cuối video là cả cây trong một hình.

<short pause> Và vì phần bảy, Steel Ball Run, đang lên anime trên Netflix, video này cũng là bản đồ để bạn hiểu vì sao phần bảy lại có một dòng họ Joestar hoàn toàn khác.

<short pause> Trước khi vẽ, ba quy tắc đọc. Một: mỗi phần của JoJo có một nhân vật chính, gọi là một JoJo, và phần lớn là người nhà Joestar.

<short pause> Hai: biệt danh JoJo đến từ cách chơi chữ trên tên. Ví dụ Jonathan Joestar thành Jo cộng Jo. Có những JoJo mang họ khác, nhưng vẫn cùng dòng máu.

<short pause> Ba: hầu hết người trong dòng họ có một vết hình ngôi sao ở sau vai trái, gần gáy. Đó là chìa khóa để nhận ra ai là người nhà, kể cả khi họ không mang họ Joestar.

<short pause> Kaku để ý: trong JoJo, dòng máu quan trọng hơn cái họ. Và như ta sẽ thấy, có cả một người mang dấu ngôi sao nhưng không phải con của người nhà Joestar theo cách thông thường.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này đi qua sáu phần đầu của JoJo, kể cả cái kết của phần sáu, và nhắc sơ qua phần bảy, tám, chín. Nếu bạn đang xem dở, hãy lưu video lại.

[pause] Năm 1888, ở nước Anh, một chàng trai quý tộc tên Jonathan Joestar chiến đấu với người anh nuôi của mình. Hơn một trăm năm sau, ở Florida, một cô gái trong tù chiến đấu với cùng một bóng ma của quá khứ.

[pause] Giữa hai người đó là năm thế hệ, một mối thù truyền kiếp, và một dấu hiệu nhỏ hình ngôi sao mà mọi người trong dòng họ đều mang trên vai.

[pause] JoJo là bộ truyện của Araki Hirohiko, bắt đầu năm 1987 và vẫn tiếp tục tới hôm nay. Mỗi phần có một nhân vật chính mới, và gần như ai cũng có biệt danh JoJo.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ Joestar: gốc rễ, các nhánh, những nhánh con bất ngờ, và cả những nhánh đã mất. Cuối video là cả cây trong một hình.

[pause] Và vì phần bảy, Steel Ball Run, đang lên anime trên Netflix, video này cũng là bản đồ để bạn hiểu vì sao phần bảy lại có một dòng họ Joestar hoàn toàn khác.

[pause] Trước khi vẽ, ba quy tắc đọc. Một: mỗi phần của JoJo có một nhân vật chính, gọi là một JoJo, và phần lớn là người nhà Joestar.

[pause] Hai: biệt danh JoJo đến từ cách chơi chữ trên tên. Ví dụ Jonathan Joestar thành Jo cộng Jo. Có những JoJo mang họ khác, nhưng vẫn cùng dòng máu.

[pause] Ba: hầu hết người trong dòng họ có một vết hình ngôi sao ở sau vai trái, gần gáy. Đó là chìa khóa để nhận ra ai là người nhà, kể cả khi họ không mang họ Joestar.

[pause] Kaku để ý: trong JoJo, dòng máu quan trọng hơn cái họ. Và như ta sẽ thấy, có cả một người mang dấu ngôi sao nhưng không phải con của người nhà Joestar theo cách thông thường.
```

### c02 · Gốc: Jonathan Joestar, phần một

Khoảng 81 giây · cảnh s11–s17 · 1053 ký tự

**Gemini**

```text
Gốc của cây là George Joestar đệ nhất, một quý tộc Anh. Ông nhận nuôi một cậu bé tên Dio Brando, vì tin rằng cha cậu từng cứu mạng mình.

<short pause> Con trai ruột của ông là Jonathan, một chàng trai tốt bụng, lịch thiệp. Dio thì mang tham vọng chiếm đoạt cả gia sản nhà Joestar.

<short pause> Jonathan học Hamon từ một người thầy tên Zeppeli. Nguyên lý: kiểm soát hơi thở để tạo ra năng lượng giống ánh mặt trời, thứ duy nhất ma cà rồng sợ. Kaku đã kể kỹ trong video lịch sử Hamon và Stand.

<short pause> Dio dùng một chiếc mặt nạ đá cổ để biến thành ma cà rồng. Jonathan học một kỹ thuật thở gọi là Hamon, sức mạnh của mặt trời, để chống lại hắn.

<short pause> Trận cuối diễn ra trên một con tàu. Jonathan chết, nhưng mang theo cả Dio xuống đáy biển. Hay ít nhất là mọi người tin như vậy.

<short pause> Và đây là chi tiết quyết định cả cây phả hệ: vợ Jonathan, Erina, sống sót, đang mang thai. Cô trốn thoát trong một chiếc quan tài trôi trên biển, cùng một bé gái được cứu từ con tàu.

<short pause> Nếu Erina không sống sót, cây phả hệ đã kết thúc ngay ở gốc. Mọi JoJo về sau đều nợ mạng sống của mình cho chiếc quan tài trôi trên biển đó.
```

**ElevenLabs**

```text
Gốc của cây là George Joestar đệ nhất, một quý tộc Anh. Ông nhận nuôi một cậu bé tên Dio Brando, vì tin rằng cha cậu từng cứu mạng mình.

[pause] Con trai ruột của ông là Jonathan, một chàng trai tốt bụng, lịch thiệp. Dio thì mang tham vọng chiếm đoạt cả gia sản nhà Joestar.

[pause] Jonathan học Hamon từ một người thầy tên Zeppeli. Nguyên lý: kiểm soát hơi thở để tạo ra năng lượng giống ánh mặt trời, thứ duy nhất ma cà rồng sợ. Kaku đã kể kỹ trong video lịch sử Hamon và Stand.

[pause] Dio dùng một chiếc mặt nạ đá cổ để biến thành ma cà rồng. Jonathan học một kỹ thuật thở gọi là Hamon, sức mạnh của mặt trời, để chống lại hắn.

[pause] Trận cuối diễn ra trên một con tàu. Jonathan chết, nhưng mang theo cả Dio xuống đáy biển. Hay ít nhất là mọi người tin như vậy.

[pause] Và đây là chi tiết quyết định cả cây phả hệ: vợ Jonathan, Erina, sống sót, đang mang thai. Cô trốn thoát trong một chiếc quan tài trôi trên biển, cùng một bé gái được cứu từ con tàu.

[pause] Nếu Erina không sống sót, cây phả hệ đã kết thúc ngay ở gốc. Mọi JoJo về sau đều nợ mạng sống của mình cho chiếc quan tài trôi trên biển đó.
```

### c03 · Nhánh 1: George đệ nhị và Joseph, phần hai / Nhánh 2: Holly và Jotaro, phần ba

Khoảng 149 giây · cảnh s18–s31 · 1932 ký tự

**Gemini**

```text
Đứa con Erina mang trong bụng là George Joestar đệ nhị. Và bé gái được cứu cùng chiếc quan tài lớn lên thành Elizabeth, về sau được biết tới với tên Lisa Lisa.

<short pause> George đệ nhị và Elizabeth yêu nhau và cưới nhau. Họ có một con trai: Joseph Joestar.

<short pause> Nhưng George đệ nhị bị một kẻ thuộc phe Dio sát hại. Elizabeth phải rời đi để trả thù và lẩn trốn, và Joseph được bà nội Erina nuôi lớn.

<short pause> Kẻ thù của phần hai không phải Dio, mà là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá. Cây phả hệ Joestar bắt đầu bị kéo vào một lịch sử còn xa hơn cả mối thù với Dio.

<short pause> Năm 1938, Joseph, một chàng trai ranh mãnh, hay đoán trước câu nói của đối thủ, trở thành JoJo thứ hai. Cậu học Hamon từ chính mẹ mình, Lisa Lisa, mà ban đầu không biết đó là mẹ.

<short pause> Kaku để ý: đây là nhánh đầu tiên cho thấy cây phả hệ JoJo đầy những bí mật gia đình. Người thầy hóa ra là mẹ. Và đó mới chỉ là bắt đầu.

<short pause> Sau phần hai, Joseph cưới Suzi Q, cô bạn người Ý của mẹ mình. Họ có một con gái, Holly.

<short pause> Holly Joestar cưới một nhạc công người Nhật, Kujo Sadao, và chuyển tới Nhật. Con trai họ là Kujo Jotaro, JoJo thứ ba.

<short pause> Năm 1987, gần một trăm năm sau con tàu cháy, Dio trở lại. Hắn không chết dưới đáy biển. Hắn đã lấy cơ thể của Jonathan làm cơ thể mình.

<short pause> Và vì Dio mang cơ thể của Jonathan, dòng máu Joestar trong hắn đánh thức một sức mạnh mới ở cả dòng họ: Stand, hiện thân của tinh thần.

<short pause> Mỗi thành viên trong dòng họ có một Stand khác nhau, phản ánh con người họ. Joseph có Stand dạng dây leo gai, hợp với tính ranh mãnh. Jotaro có Stand cực mạnh và chính xác, hợp với tính điềm tĩnh.

<short pause> Holly không đủ sức chịu Stand của mình, và ngã bệnh nặng. Jotaro, Joseph và những người bạn lên đường tới Ai Cập để tìm Dio, cứu Holly.

<short pause> Điều thú vị: các Joestar có thể cảm nhận Dio qua dòng máu chung, vì hắn đang mang cơ thể tổ tiên họ. Cây phả hệ trở thành một mạng lưới liên kết thật sự.

<short pause> Phần ba khép lại khi Jotaro đánh bại Dio. Cơ thể của Jonathan, sau một trăm năm, cuối cùng cũng được yên nghỉ.
```

**ElevenLabs**

```text
Đứa con Erina mang trong bụng là George Joestar đệ nhị. Và bé gái được cứu cùng chiếc quan tài lớn lên thành Elizabeth, về sau được biết tới với tên Lisa Lisa.

[pause] George đệ nhị và Elizabeth yêu nhau và cưới nhau. Họ có một con trai: Joseph Joestar.

[pause] Nhưng George đệ nhị bị một kẻ thuộc phe Dio sát hại. Elizabeth phải rời đi để trả thù và lẩn trốn, và Joseph được bà nội Erina nuôi lớn.

[pause] Kẻ thù của phần hai không phải Dio, mà là những sinh vật cổ đại đã tạo ra chiếc mặt nạ đá. Cây phả hệ Joestar bắt đầu bị kéo vào một lịch sử còn xa hơn cả mối thù với Dio.

[pause] Năm 1938, Joseph, một chàng trai ranh mãnh, hay đoán trước câu nói của đối thủ, trở thành JoJo thứ hai. Cậu học Hamon từ chính mẹ mình, Lisa Lisa, mà ban đầu không biết đó là mẹ.

[pause] Kaku để ý: đây là nhánh đầu tiên cho thấy cây phả hệ JoJo đầy những bí mật gia đình. Người thầy hóa ra là mẹ. Và đó mới chỉ là bắt đầu.

[pause] Sau phần hai, Joseph cưới Suzi Q, cô bạn người Ý của mẹ mình. Họ có một con gái, Holly.

[pause] Holly Joestar cưới một nhạc công người Nhật, Kujo Sadao, và chuyển tới Nhật. Con trai họ là Kujo Jotaro, JoJo thứ ba.

[pause] Năm 1987, gần một trăm năm sau con tàu cháy, Dio trở lại. Hắn không chết dưới đáy biển. Hắn đã lấy cơ thể của Jonathan làm cơ thể mình.

[pause] Và vì Dio mang cơ thể của Jonathan, dòng máu Joestar trong hắn đánh thức một sức mạnh mới ở cả dòng họ: Stand, hiện thân của tinh thần.

[pause] Mỗi thành viên trong dòng họ có một Stand khác nhau, phản ánh con người họ. Joseph có Stand dạng dây leo gai, hợp với tính ranh mãnh. Jotaro có Stand cực mạnh và chính xác, hợp với tính điềm tĩnh.

[pause] Holly không đủ sức chịu Stand của mình, và ngã bệnh nặng. Jotaro, Joseph và những người bạn lên đường tới Ai Cập để tìm Dio, cứu Holly.

[pause] Điều thú vị: các Joestar có thể cảm nhận Dio qua dòng máu chung, vì hắn đang mang cơ thể tổ tiên họ. Cây phả hệ trở thành một mạng lưới liên kết thật sự.

[pause] Phần ba khép lại khi Jotaro đánh bại Dio. Cơ thể của Jonathan, sau một trăm năm, cuối cùng cũng được yên nghỉ.
```

### c04 · Những người phụ nữ giữ gốc cây / Nhánh con bất ngờ: Josuke, phần bốn

Khoảng 107 giây · cảnh s32–s41 · 1397 ký tự

**Gemini**

```text
Trước khi sang nhánh tiếp theo, Kaku muốn dừng lại ở những người thường bị bỏ quên trên cây phả hệ JoJo: những người phụ nữ.

<short pause> Erina cứu cả dòng họ bằng cách sống sót trên biển. Lisa Lisa giấu thân phận để bảo vệ con trai. Erina lại nuôi lớn cháu nội khi cha mẹ cậu không thể.

<short pause> Holly chịu đựng Stand của mình trong im lặng, mỉm cười để con trai không lo. Tomoko nuôi Josuke một mình suốt mười sáu năm.

<short pause> <laugh> Kaku để ý: các JoJo là người chiến đấu, nhưng chính những người phụ nữ này là người giữ cho cây không bị bật gốc. Không có họ, sẽ không có JoJo nào tiếp theo.

<short pause> Năm 1999, ở thị trấn Morioh, Nhật Bản, cây phả hệ mọc thêm một nhánh không ai biết: Higashikata Josuke.

<short pause> Josuke là con ngoài giá thú của Joseph Joestar, với một phụ nữ Nhật tên Tomoko, từ nhiều năm trước. Joseph chưa từng biết về đứa con này.

<short pause> Điều khiến fan cười nhiều nhất: Josuke là chú của Jotaro, dù trẻ hơn Jotaro nhiều tuổi. Một thiếu niên mười sáu tuổi là chú của một người đàn ông hai mươi tám tuổi.

<short pause> Phần bốn cũng là phần ít có mối thù Dio nhất. Nó là câu chuyện về một thị trấn nhỏ và những bí ẩn đời thường. Cây phả hệ được nghỉ ngơi một chút.

<short pause> Josuke có Stand chữa lành và sửa chữa mọi thứ, trừ chính bản thân mình. Một nhánh con mang năng lực phục hồi, như để hàn gắn những vết nứt của gia đình.

<short pause> Kaku để ý: nhánh Josuke cho thấy cây phả hệ JoJo không hoàn hảo. Có những bí mật, những lỗi lầm, nhưng cuối cùng người nhà vẫn chấp nhận nhau.
```

**ElevenLabs**

```text
Trước khi sang nhánh tiếp theo, Kaku muốn dừng lại ở những người thường bị bỏ quên trên cây phả hệ JoJo: những người phụ nữ.

[pause] Erina cứu cả dòng họ bằng cách sống sót trên biển. Lisa Lisa giấu thân phận để bảo vệ con trai. Erina lại nuôi lớn cháu nội khi cha mẹ cậu không thể.

[pause] Holly chịu đựng Stand của mình trong im lặng, mỉm cười để con trai không lo. Tomoko nuôi Josuke một mình suốt mười sáu năm.

[pause] [chuckles] Kaku để ý: các JoJo là người chiến đấu, nhưng chính những người phụ nữ này là người giữ cho cây không bị bật gốc. Không có họ, sẽ không có JoJo nào tiếp theo.

[pause] Năm 1999, ở thị trấn Morioh, Nhật Bản, cây phả hệ mọc thêm một nhánh không ai biết: Higashikata Josuke.

[pause] Josuke là con ngoài giá thú của Joseph Joestar, với một phụ nữ Nhật tên Tomoko, từ nhiều năm trước. Joseph chưa từng biết về đứa con này.

[pause] Điều khiến fan cười nhiều nhất: Josuke là chú của Jotaro, dù trẻ hơn Jotaro nhiều tuổi. Một thiếu niên mười sáu tuổi là chú của một người đàn ông hai mươi tám tuổi.

[pause] Phần bốn cũng là phần ít có mối thù Dio nhất. Nó là câu chuyện về một thị trấn nhỏ và những bí ẩn đời thường. Cây phả hệ được nghỉ ngơi một chút.

[pause] Josuke có Stand chữa lành và sửa chữa mọi thứ, trừ chính bản thân mình. Một nhánh con mang năng lực phục hồi, như để hàn gắn những vết nứt của gia đình.

[pause] Kaku để ý: nhánh Josuke cho thấy cây phả hệ JoJo không hoàn hảo. Có những bí mật, những lỗi lầm, nhưng cuối cùng người nhà vẫn chấp nhận nhau.
```

### c05 · Nhánh lạc: Giorno, phần năm / Nhánh bóng tối: những người con khác của Dio

Khoảng 104 giây · cảnh s42–s51 · 1346 ký tự

**Gemini**

```text
Năm 2001, ở Ý, một chàng trai mười lăm tuổi tên Giorno Giovanna mơ trở thành trùm băng đảng để làm sạch thành phố của mình.

<short pause> Giorno có dấu ngôi sao trên vai. <short pause> Nhưng cậu là con của Dio. Làm sao con của kẻ thù lại mang dấu hiệu của dòng họ Joestar?

<short pause> Câu trả lời: Giorno được sinh ra khi Dio đang dùng cơ thể của Jonathan. Về mặt di truyền, Giorno mang dòng máu của cả Dio lẫn Jonathan.

<short pause> Trong phần năm, Giorno gần như không gặp gia đình Joestar nào. Cậu tự đi con đường của mình, và chỉ người đọc mới thấy sợi dây nối cậu với cây phả hệ.

<short pause> Và thú vị hơn nữa: Giorno thừa hưởng từ Jonathan sự tử tế và lòng chính trực, từ Dio sự quyết đoán và tham vọng. Cậu là nhánh cây mọc lên từ chính mối thù.

<short pause> Giorno cũng có những người thầy và đồng đội tạo nên cậu, như băng nhóm của Bucciarati. Một lần nữa, gia đình được tạo nên bởi những người chọn đi cùng nhau.

<short pause> <laugh> Kaku thấy đây là nhánh đẹp nhất của cây. Mối thù bắt đầu từ Jonathan và Dio, cuối cùng sinh ra một người thừa hưởng điều tốt của cả hai.

<short pause> Giorno không phải con duy nhất của Dio. Ở phần sáu, xuất hiện thêm ba người con trai khác, cũng mang dấu ngôi sao, sống ở Mỹ.

<short pause> Nếu Giorno chọn con đường ánh sáng, thì ba người này bị kéo vào phe bóng tối, như những quân cờ của một kẻ thừa kế ý chí của Dio.

<short pause> Kaku xếp họ vào nhánh bóng tối của cây: cùng một dòng máu, nhưng hoàn cảnh sống khác, lựa chọn khác, và số phận khác.
```

**ElevenLabs**

```text
Năm 2001, ở Ý, một chàng trai mười lăm tuổi tên Giorno Giovanna mơ trở thành trùm băng đảng để làm sạch thành phố của mình.

[pause] Giorno có dấu ngôi sao trên vai. [pause] Nhưng cậu là con của Dio. [curious] Làm sao con của kẻ thù lại mang dấu hiệu của dòng họ Joestar?

[pause] Câu trả lời: Giorno được sinh ra khi Dio đang dùng cơ thể của Jonathan. Về mặt di truyền, Giorno mang dòng máu của cả Dio lẫn Jonathan.

[pause] Trong phần năm, Giorno gần như không gặp gia đình Joestar nào. Cậu tự đi con đường của mình, và chỉ người đọc mới thấy sợi dây nối cậu với cây phả hệ.

[pause] Và thú vị hơn nữa: Giorno thừa hưởng từ Jonathan sự tử tế và lòng chính trực, từ Dio sự quyết đoán và tham vọng. Cậu là nhánh cây mọc lên từ chính mối thù.

[pause] Giorno cũng có những người thầy và đồng đội tạo nên cậu, như băng nhóm của Bucciarati. Một lần nữa, gia đình được tạo nên bởi những người chọn đi cùng nhau.

[pause] [chuckles] Kaku thấy đây là nhánh đẹp nhất của cây. Mối thù bắt đầu từ Jonathan và Dio, cuối cùng sinh ra một người thừa hưởng điều tốt của cả hai.

[pause] Giorno không phải con duy nhất của Dio. Ở phần sáu, xuất hiện thêm ba người con trai khác, cũng mang dấu ngôi sao, sống ở Mỹ.

[pause] Nếu Giorno chọn con đường ánh sáng, thì ba người này bị kéo vào phe bóng tối, như những quân cờ của một kẻ thừa kế ý chí của Dio.

[pause] Kaku xếp họ vào nhánh bóng tối của cây: cùng một dòng máu, nhưng hoàn cảnh sống khác, lựa chọn khác, và số phận khác.
```

### c06 · Ngọn cây: Jolyne, phần sáu / Gia đình không chỉ là dòng máu / Cây đối xứng: dòng họ Brando

Khoảng 149 giây · cảnh s52–s65 · 1931 ký tự

**Gemini**

```text
Năm 2011, ở Florida, Kujo Jolyne, con gái của Jotaro, bị vu oan và đưa vào tù. Cô trở thành JoJo thứ sáu, và là JoJo nữ đầu tiên.

<short pause> Kẻ đứng sau là một người từng là bạn thân của Dio, mang theo di sản và kế hoạch của hắn. Hơn một trăm hai mươi năm sau con tàu cháy, mối thù vẫn chưa kết thúc.

<short pause> Mối quan hệ cha con giữa Jotaro và Jolyne là trung tâm cảm xúc của phần sáu. Jotaro là người cha vắng mặt, nhưng cuối cùng lại là người liều mạng vì con gái.

<short pause> Jolyne có Stand biến cơ thể thành sợi chỉ. Kaku thấy đây là một biểu tượng đẹp: sợi chỉ nối các thế hệ của gia đình lại với nhau.

<short pause> Và cái kết của phần sáu, Kaku chỉ nói ngắn: nó thay đổi cả vũ trụ của JoJo. Cây phả hệ mà ta vừa vẽ, theo một nghĩa nào đó, đi tới điểm cuối.

<short pause> Đó là lý do khi phần bảy bắt đầu, người đọc gặp một thế giới mới, với những người mang tên quen thuộc nhưng không phải cùng một người.

<short pause> Cây phả hệ JoJo còn có những nhánh không cùng dòng máu, nhưng gắn bó như người nhà.

<short pause> Speedwagon, người bạn của Jonathan từ phần một, lập ra một quỹ mang tên mình. Quỹ Speedwagon hỗ trợ dòng họ Joestar qua rất nhiều thế hệ, tới tận phần sáu.

<short pause> Dòng họ Zeppeli cũng song hành: Will A. Zeppeli dạy Hamon cho Jonathan, và cháu ông, Caesar, trở thành người bạn thân nhất của Joseph ở phần hai.

<short pause> Và những người bạn đồng hành của Jotaro trên đường tới Ai Cập, nhiều người không trở về. Họ không mang dấu ngôi sao, nhưng mang tinh thần giống hệt.

<short pause> Kaku thấy đây là thông điệp đẹp của JoJo: gia đình là những người sẵn sàng đi cùng bạn qua bóng tối, dù có cùng dòng máu hay không.

<short pause> Bên cạnh cây Joestar là một cây đối xứng: dòng họ Brando. Cha của Dio là một kẻ nghiện rượu tàn nhẫn, và Dio lớn lên trong nghèo khổ, thù hận.

<short pause> Hai cây mọc cạnh nhau: một bên được nuôi bằng lòng tốt, một bên bằng tham vọng. Và hai cây quấn vào nhau khi Dio lấy cơ thể của Jonathan.

<short pause> Kết quả của sự quấn vào nhau đó là Giorno, và cả những người con ở nhánh bóng tối. Một cây phả hệ không thể vẽ riêng mà không vẽ luôn kẻ thù.
```

**ElevenLabs**

```text
Năm 2011, ở Florida, Kujo Jolyne, con gái của Jotaro, bị vu oan và đưa vào tù. Cô trở thành JoJo thứ sáu, và là JoJo nữ đầu tiên.

[pause] Kẻ đứng sau là một người từng là bạn thân của Dio, mang theo di sản và kế hoạch của hắn. Hơn một trăm hai mươi năm sau con tàu cháy, mối thù vẫn chưa kết thúc.

[pause] Mối quan hệ cha con giữa Jotaro và Jolyne là trung tâm cảm xúc của phần sáu. Jotaro là người cha vắng mặt, nhưng cuối cùng lại là người liều mạng vì con gái.

[pause] Jolyne có Stand biến cơ thể thành sợi chỉ. Kaku thấy đây là một biểu tượng đẹp: sợi chỉ nối các thế hệ của gia đình lại với nhau.

[pause] Và cái kết của phần sáu, Kaku chỉ nói ngắn: nó thay đổi cả vũ trụ của JoJo. Cây phả hệ mà ta vừa vẽ, theo một nghĩa nào đó, đi tới điểm cuối.

[pause] Đó là lý do khi phần bảy bắt đầu, người đọc gặp một thế giới mới, với những người mang tên quen thuộc nhưng không phải cùng một người.

[pause] Cây phả hệ JoJo còn có những nhánh không cùng dòng máu, nhưng gắn bó như người nhà.

[pause] Speedwagon, người bạn của Jonathan từ phần một, lập ra một quỹ mang tên mình. Quỹ Speedwagon hỗ trợ dòng họ Joestar qua rất nhiều thế hệ, tới tận phần sáu.

[pause] Dòng họ Zeppeli cũng song hành: Will A. Zeppeli dạy Hamon cho Jonathan, và cháu ông, Caesar, trở thành người bạn thân nhất của Joseph ở phần hai.

[pause] Và những người bạn đồng hành của Jotaro trên đường tới Ai Cập, nhiều người không trở về. Họ không mang dấu ngôi sao, nhưng mang tinh thần giống hệt.

[pause] Kaku thấy đây là thông điệp đẹp của JoJo: gia đình là những người sẵn sàng đi cùng bạn qua bóng tối, dù có cùng dòng máu hay không.

[pause] Bên cạnh cây Joestar là một cây đối xứng: dòng họ Brando. Cha của Dio là một kẻ nghiện rượu tàn nhẫn, và Dio lớn lên trong nghèo khổ, thù hận.

[pause] Hai cây mọc cạnh nhau: một bên được nuôi bằng lòng tốt, một bên bằng tham vọng. Và hai cây quấn vào nhau khi Dio lấy cơ thể của Jonathan.

[pause] Kết quả của sự quấn vào nhau đó là Giorno, và cả những người con ở nhánh bóng tối. Một cây phả hệ không thể vẽ riêng mà không vẽ luôn kẻ thù.
```

### c07 · Vũ trụ mới: phần bảy, tám và chín / Bí mật của dấu ngôi sao / Toàn bộ cây phả hệ

Khoảng 152 giây · cảnh s66–s79 · 1973 ký tự

**Gemini**

```text
Phần bảy, Steel Ball Run, diễn ra ở nước Mỹ năm 1890, với một cuộc đua ngựa xuyên lục địa. Nhân vật chính là Johnny Joestar, một người khác hoàn toàn với các Joestar trước.

<short pause> Phần bảy được chuyển thể anime bởi David Production, phát trên Netflix từ tháng ba năm 2026, và phần hai của anime ra từ tháng chín năm 2026.

<short pause> Phần tám, JoJolion, lấy bối cảnh một thị trấn Morioh khác, với một Josuke khác. Và phần chín, The JOJOLands, theo Jodio Joestar, một thiếu niên ở Hawaii, vẫn đang được đăng.

<short pause> Kaku gọi đây là cây phả hệ thứ hai: cùng những cái tên, cùng tinh thần, nhưng mọc ở một khu vườn khác. Muốn hiểu nó, Kaku sẽ cần một video riêng.

<short pause> Quay lại dấu ngôi sao. Vì sao nó quan trọng tới vậy?

<short pause> Một: nó giúp nhận ra người nhà, như với Josuke và Giorno. Hai: nó là dấu hiệu của một dòng máu mà định mệnh luôn kéo vào cuộc chiến với Dio.

<short pause> Có một thói quen thú vị của các Joestar: họ thường có những câu cửa miệng rất riêng, được fan nhớ mãi và bắt chước khắp nơi. Kaku để bạn tự nhớ lại câu của JoJo mà bạn thích nhất.

<short pause> Và ba, theo cách Kaku hiểu: nó là một lời nhắc rằng mỗi JoJo không chiến đấu một mình. Họ mang theo tinh thần của những người đi trước.

<short pause> Trong JoJo, điều này có tên: tinh thần hoàng kim. Sự dũng cảm và lòng tốt được truyền từ thế hệ này sang thế hệ khác.

<short pause> Và đây là cả cây trong một hình. Gốc: George đệ nhất và Jonathan, phần một, 1888. Erina sống sót trong quan tài, mang thai George đệ nhị, cùng bé Elizabeth.

<short pause> Nhánh một: George đệ nhị và Lisa Lisa, sinh Joseph, phần hai, 1938. Joseph và Suzi Q, sinh Holly. Holly và Kujo Sadao, sinh Jotaro, phần ba, 1987.

<short pause> Và những nhánh ngoài dòng máu nhưng là gia đình: Speedwagon, dòng họ Zeppeli, và những người bạn đồng hành không mang dấu ngôi sao.

<short pause> Nhánh con: Joseph và Tomoko, sinh Josuke, phần bốn, 1999. Nhánh lạc: Dio trong cơ thể Jonathan, sinh Giorno, phần năm, 2001, cùng ba người con ở nhánh bóng tối.

<short pause> Ngọn cây: Jotaro sinh Jolyne, phần sáu, 2011. Và bên cạnh, một cây thứ hai bắt đầu mọc: Johnny, Josuke của JoJolion, và Jodio.
```

**ElevenLabs**

```text
Phần bảy, Steel Ball Run, diễn ra ở nước Mỹ năm 1890, với một cuộc đua ngựa xuyên lục địa. Nhân vật chính là Johnny Joestar, một người khác hoàn toàn với các Joestar trước.

[pause] Phần bảy được chuyển thể anime bởi David Production, phát trên Netflix từ tháng ba năm 2026, và phần hai của anime ra từ tháng chín năm 2026.

[pause] Phần tám, JoJolion, lấy bối cảnh một thị trấn Morioh khác, với một Josuke khác. Và phần chín, The JOJOLands, theo Jodio Joestar, một thiếu niên ở Hawaii, vẫn đang được đăng.

[pause] Kaku gọi đây là cây phả hệ thứ hai: cùng những cái tên, cùng tinh thần, nhưng mọc ở một khu vườn khác. Muốn hiểu nó, Kaku sẽ cần một video riêng.

[pause] Quay lại dấu ngôi sao. [curious] Vì sao nó quan trọng tới vậy?

[pause] Một: nó giúp nhận ra người nhà, như với Josuke và Giorno. Hai: nó là dấu hiệu của một dòng máu mà định mệnh luôn kéo vào cuộc chiến với Dio.

[pause] Có một thói quen thú vị của các Joestar: họ thường có những câu cửa miệng rất riêng, được fan nhớ mãi và bắt chước khắp nơi. Kaku để bạn tự nhớ lại câu của JoJo mà bạn thích nhất.

[pause] Và ba, theo cách Kaku hiểu: nó là một lời nhắc rằng mỗi JoJo không chiến đấu một mình. Họ mang theo tinh thần của những người đi trước.

[pause] Trong JoJo, điều này có tên: tinh thần hoàng kim. Sự dũng cảm và lòng tốt được truyền từ thế hệ này sang thế hệ khác.

[pause] Và đây là cả cây trong một hình. Gốc: George đệ nhất và Jonathan, phần một, 1888. Erina sống sót trong quan tài, mang thai George đệ nhị, cùng bé Elizabeth.

[pause] Nhánh một: George đệ nhị và Lisa Lisa, sinh Joseph, phần hai, 1938. Joseph và Suzi Q, sinh Holly. Holly và Kujo Sadao, sinh Jotaro, phần ba, 1987.

[pause] Và những nhánh ngoài dòng máu nhưng là gia đình: Speedwagon, dòng họ Zeppeli, và những người bạn đồng hành không mang dấu ngôi sao.

[pause] Nhánh con: Joseph và Tomoko, sinh Josuke, phần bốn, 1999. Nhánh lạc: Dio trong cơ thể Jonathan, sinh Giorno, phần năm, 2001, cùng ba người con ở nhánh bóng tối.

[pause] Ngọn cây: Jotaro sinh Jolyne, phần sáu, 2011. Và bên cạnh, một cây thứ hai bắt đầu mọc: Johnny, Josuke của JoJolion, và Jodio.
```

### c08 · Kết

Khoảng 34 giây · cảnh s80–s82 · 437 ký tự

**Gemini**

```text
Bạn thích JoJo nào nhất? Và bạn có để ý chi tiết gia đình nào khiến bạn bất ngờ nhất: mẹ là thầy, chú trẻ hơn cháu, hay con của kẻ thù mang dấu ngôi sao? Viết vào bình luận nhé.

<short pause> Video tiếp theo, Kaku mở một cuốn sử khác: Vinland Saga, người Viking thật, và nhân vật Thorfinn có thật trong sử thi Iceland.

<short pause> <laugh> Nếu bạn thích xem Kaku vẽ cây phả hệ, hãy đăng ký kênh. Mỗi video là một chiếc lá mới trên cây của kênh. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Bạn thích JoJo nào nhất? Và bạn có để ý chi tiết gia đình nào khiến bạn bất ngờ nhất: mẹ là thầy, chú trẻ hơn cháu, hay con của kẻ thù mang dấu ngôi sao? Viết vào bình luận nhé.

[pause] Video tiếp theo, Kaku mở một cuốn sử khác: Vinland Saga, người Viking thật, và nhân vật Thorfinn có thật trong sử thi Iceland.

[pause] [chuckles] Nếu bạn thích xem Kaku vẽ cây phả hệ, hãy đăng ký kênh. Mỗi video là một chiếc lá mới trên cây của kênh. Kaku gấp sổ đây, hẹn gặp lại!
```
