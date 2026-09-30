# Bộ prompt · Fullmetal Alchemist: Giả kim thuật và luật trao đổi ngang giá hoạt động thế nào

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 79 ảnh, 7 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (79 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết Fullmetal Alchemist Brotherhood, kể cả bí mật lớn nhất về nguồn năng…

```text
Wide 16:9 landscape cinematic frame. a closed leather-bound alchemy book with a brass clasp on a wooden desk, a warning card tucked under it, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Con người không thể có được thứ gì mà không trả lại một thứ khác. Muốn có, phải mất đi một thứ có giá trị tươ…

```text
Wide 16:9 landscape cinematic frame. an antique brass balance scale perfectly level, one pan holding a small pile of sand and the other a small glass vial, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Hai anh em nhà Elric tin vào câu đó. Và vì tin, họ nghĩ rằng nếu đưa đủ nguyên liệu, họ có thể mang người mẹ…

```text
Wide 16:9 landscape cinematic frame. two small boys sitting side by side on a wooden floor surrounded by open books and scribbled notes, back view, soft candlelight. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Họ đã sai. Người anh mất một chân. Người em mất toàn bộ cơ thể. Để giữ linh hồn em lại, người anh đánh đổi th…

```text
Wide 16:9 landscape cinematic frame. a chalk circle on a dark basement floor with scattered books and a single overturned candle, no people, wide shot, cold eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Câu hỏi hôm nay: giả kim thuật trong Fullmetal Alchemist hoạt động thế nào? Luật trao đổi ngang giá có thật s…

```text
Wide 16:9 landscape cinematic frame. a notebook page with three handwritten question marks beside a drawn circle diagram, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở một cuốn sổ giả kim: từ luật nền, qua các nhánh, tới những luật c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a chalk circle on a small blackboard with great concentration. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Giả kim thuật là gì?

Lời: Fullmetal Alchemist là manga của Arakawa Hiromu, đăng từ năm 2001 tới 2010. Truyện có hai bản anime do studio…

```text
Wide 16:9 landscape cinematic frame. a stack of manga volumes beside two DVD cases on a shelf, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Trong thế giới của truyện, giả kim thuật không phải phép thuật. Nó là một ngành khoa học: hiểu cấu tạo của vậ…

```text
Wide 16:9 landscape cinematic frame. a laboratory table with glass flasks, mineral samples and a notebook of formulas, medium shot, warm scholarly light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Nhà giả kim giỏi phải học rất nhiều: hóa học, vật lý, sinh học, và cả toán. Ở tuổi mười hai, Edward đã là một…

```text
Wide 16:9 landscape cinematic frame. a young teenager asleep on a pile of thick open books in a library at night, close-up, soft lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Ngoài đời thật, giả kim thuật cũng từng tồn tại, từ châu Âu, thế giới Ả Rập tới Trung Hoa. Người ta tìm cách…

```text
Wide 16:9 landscape cinematic frame. an old medieval alchemist's workshop with a furnace, retorts and dusty manuscripts, wide shot, warm firelight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Arakawa đã lấy rất nhiều biểu tượng từ giả kim thuật thật, rồi xây một hệ thống có luật rõ ràng. Kaku sẽ chỉ…

```text
Wide 16:9 landscape cinematic frame. an old illuminated manuscript page with alchemical symbols in the margins, extreme close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · Luật nền: trao đổi ngang giá

Lời: Luật nền của mọi phép giả kim là trao đổi ngang giá. Không thể tạo ra thứ gì từ hư không. Muốn có một thứ, ph…

```text
Wide 16:9 landscape cinematic frame. two cupped hands holding a small pile of iron filings that is slowly reshaping into a tiny iron key, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Luật này chia làm hai phần. Phần một: bảo toàn khối lượng. Một ký sắt chỉ có thể biến thành một ký thứ gì đó,…

```text
Wide 16:9 landscape cinematic frame. a kitchen scale with a block of iron on one side and an iron statue on the other, both showing the same weight, close-up, clean light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nghe quen không? Ngoài đời, nhà hóa học Lavoisier đã nêu định luật bảo toàn khối lượng vào cuối thế kỷ mười t…

```text
Wide 16:9 landscape cinematic frame. an eighteenth-century chemistry laboratory with a large precise balance and sealed glass vessels, wide shot, warm period light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Phần hai: vật chất chỉ biến đổi thành thứ có cùng bản chất. Gỗ có thể thành một cái bàn gỗ, nhưng không thể t…

```text
Wide 16:9 landscape cinematic frame. a wooden chair on one side transforming into a wooden table, while a crossed-out steel sword floats nearby, diagram-style illustration, warm light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Vì vậy nhà giả kim luôn phải tính toán: mình có bao nhiêu nguyên liệu, thành phần là gì, và thứ mình muốn làm…

```text
Wide 16:9 landscape cinematic frame. a notebook page covered with neat calculations and small sketches of materials, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích chỗ này. Nó khiến giả kim thuật giống như nấu ăn: không có bột thì không có bánh, và bạn không…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny chef hat holding a bag of flour in one wing and a handful of sand in the other, looking puzzled. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Và luật ngang giá không chỉ là một định luật khoa học trong truyện. Nó là triết lý sống của hai anh em: muốn…

```text
Wide 16:9 landscape cinematic frame. two brothers walking side by side down a long dusty road toward the horizon, back view, wide shot, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Ba bước: hiểu, phân giải, tái tạo

Lời: Mỗi phép giả kim đi qua ba bước. Bước một: hiểu. Nhà giả kim phải biết chính xác vật mình đang chạm vào được…

```text
Wide 16:9 landscape cinematic frame. a magnifying glass held over a rough stone revealing its crystalline structure, extreme close-up, clean bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Bước hai: phân giải. Vật chất bị tách ra thành những thành phần cơ bản.

```text
Wide 16:9 landscape cinematic frame. a ceramic cup breaking apart into a swirling cloud of fine particles in mid-air, dynamic close-up, glowing blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Bước ba: tái tạo. Những thành phần đó được ghép lại thành hình dạng mới mà nhà giả kim muốn.

```text
Wide 16:9 landscape cinematic frame. a cloud of particles reassembling into a delicate ceramic bird in mid-air, dynamic close-up, glowing blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Nếu bước một sai, mọi thứ sau đó đều sai. Đó là lý do tại sao một nhà giả kim không thể biến đổi thứ mình khô…

```text
Wide 16:9 landscape cinematic frame. a failed transmutation result: a lopsided cracked lump of metal on a workbench, close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Và cũng vì vậy mà người mạnh nhất không phải người có nhiều năng lượng nhất, mà là người hiểu vật chất sâu nh…

```text
Wide 16:9 landscape cinematic frame. a tall stack of books glowing faintly with a small spark of light rising from the top, symbolic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Ba bước này nghe đơn giản, nhưng Kaku thấy nó là chìa khóa của cả bộ truyện. Mọi luật cấm, mọi bi kịch, đều x…

```text
Wide 16:9 landscape cinematic frame. three numbered stepping stones across a stream, the first stone cracked, close-up, soft daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Vòng tròn chuyển hóa

Lời: Để kích hoạt, nhà giả kim vẽ một vòng tròn chuyển hóa. Vòng tròn tượng trưng cho dòng năng lượng tuần hoàn. C…

```text
Wide 16:9 landscape cinematic frame. a precise chalk transmutation circle on a stone floor with geometric symbols inside, overhead shot, soft glowing blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Mỗi nhà giả kim có vòng tròn riêng, phù hợp với chuyên môn của mình. Có người khắc vòng tròn lên găng tay, lê…

```text
Wide 16:9 landscape cinematic frame. a row of different small objects on a table each engraved with a different circle design: a ring, a metal plate, a leather strap, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Ví dụ, Hỏa thuật sư Roy Mustang dùng găng tay có vòng tròn và vật liệu tạo tia lửa. Anh búng tay tạo tia lửa,…

```text
Wide 16:9 landscape cinematic frame. a hand snapping fingers with a tiny spark leaping into the air, extreme close-up, bright orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Kaku thích năng lực này vì nó rất gần với hóa học thật: lửa cần nhiên liệu, oxy và nhiệt. Và nó cũng có điểm…

```text
Wide 16:9 landscape cinematic frame. a fire triangle diagram drawn on parchment with fuel, oxygen and heat at each corner, raindrops smudging the corner, close-up, amber ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Nhưng Edward thì không cần vẽ. Cậu chỉ cần chắp hai tay lại. Hai bàn tay khép thành một vòng tròn, và cơ thể…

```text
Wide 16:9 landscape cinematic frame. two hands pressed together with a bright ring of light forming around them, extreme close-up, dramatic blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Vì sao Edward làm được vậy? Câu trả lời nằm ở luật cấm lớn nhất. Kaku sẽ kể ngay sau đây.

```text
Wide 16:9 landscape cinematic frame. a large closed stone door with intricate carvings standing alone in white emptiness, wide shot, eerie soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · Các nhánh giả kim

Lời: Ở đất nước Amestris, những nhà giả kim giỏi nhất được quân đội tuyển làm nhà giả kim quốc gia. Mỗi người có m…

```text
Wide 16:9 landscape cinematic frame. a row of silver pocket watches laid out on a velvet cloth, each engraved with a different symbol, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Có người chuyên về lửa. Có người chuyên về đá và đất, dùng nắm đấm để biến đổi. Có người chuyên về vụ nổ. Và…

```text
Wide 16:9 landscape cinematic frame. four small icons drawn on parchment in a row: a flame, a fist on stone, an explosion, and a steel bar, amber ink close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Được làm nhà giả kim quốc gia nghĩa là có tiền nghiên cứu và đặc quyền. Nhưng cũng có nghĩa là thành vũ khí c…

```text
Wide 16:9 landscape cinematic frame. a small silver pocket watch attached to a heavy chain leash, symbolic close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Rồi có một nhánh hoàn toàn khác, đến từ đất nước Xing ở phương Đông, gọi là Luyện đan thuật. Nó tập trung vào…

```text
Wide 16:9 landscape cinematic frame. an eastern-style apothecary with rows of small wooden drawers, jade tools and hanging herbs, wide shot, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Luyện đan thuật dựa trên khái niệm Long mạch: dòng năng lượng sống chảy trong lòng đất, từ núi cao xuống đồng…

```text
Wide 16:9 landscape cinematic frame. a landscape map showing glowing veins of energy flowing from mountains through rivers and plains, painted in ink-wash style, wide shot, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Điểm mạnh riêng của Luyện đan thuật: có thể biến đổi từ xa, bằng cách cắm những con dao nhỏ quanh mục tiêu th…

```text
Wide 16:9 landscape cinematic frame. five small throwing knives stuck into the ground in a pentagon shape with faint glowing lines connecting them, overhead shot, soft green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Hai nhánh, hai cách nhìn. Amestris xem giả kim là công cụ, là vũ khí. Xing xem nó là cách chữa lành. Sự khác…

```text
Wide 16:9 landscape cinematic frame. a split illustration: a military factory with smokestacks on one side, a peaceful mountain temple on the other, symmetrical composition, contrasting light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Luật cấm: biến đổi con người

Lời: Nhà giả kim quốc gia có những luật phải giữ, và có một điều cấm mà mọi nhà giả kim đều biết: không được biến…

```text
Wide 16:9 landscape cinematic frame. a heavy stone tablet with carved rules and one line struck through with a deep red mark, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Vì sao? Vì không ai tính được giá trị của một con người. Nước, than, vôi, sắt, phốt pho... có thể mua được hế…

```text
Wide 16:9 landscape cinematic frame. a table with neatly labeled jars of basic elements and an empty jar labeled with a question mark in the middle, still life, cold light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Hai anh em Elric đã thử. Kết quả: không phải mẹ họ trở lại. Và họ mất đi những thứ không bao giờ lấy lại được…

```text
Wide 16:9 landscape cinematic frame. a dark empty room with an overturned chair and a chalk circle smudged on the floor, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Người thử biến đổi con người sẽ bị kéo tới trước một cánh cổng khổng lồ và gặp một thực thể gọi là Chân lý. C…

```text
Wide 16:9 landscape cinematic frame. a colossal stone gate standing in an endless white void with a faint featureless silhouette sitting before it, wide shot, stark white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nhưng Chân lý cũng cho họ nhìn thấy một thứ: toàn bộ kiến thức của thế giới trong một khoảnh khắc. Đó là lý d…

```text
Wide 16:9 landscape cinematic frame. a flood of glowing symbols and images pouring through a partly open stone gate, dynamic wide shot, overwhelming bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Một điều đáng sợ: Chân lý nói với Edward rằng nó là thế giới, là vũ trụ, là tất cả, và cũng là chính cậu. Mỗi…

```text
Wide 16:9 landscape cinematic frame. a mirror standing in white emptiness reflecting a faint featureless silhouette with a wide grin, eerie wide shot, cold white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: phí qua cổng luôn liên quan tới điều người đó mong muốn. Người muốn nhìn thấy sự thật thì mất đi đ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a stone gate with a nervous expression, clutching its notebook tightly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Hòn đá triết gia

Lời: Truyền thuyết nói có một thứ có thể phá luật ngang giá: hòn đá triết gia. Có nó, nhà giả kim có thể làm mọi p…

```text
Wide 16:9 landscape cinematic frame. a small glowing red stone resting on a velvet cushion inside a glass dome, extreme close-up, intense crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Ngoài đời thật, hòn đá triết gia cũng là giấc mơ của các nhà giả kim châu Âu: thứ biến kim loại thường thành…

```text
Wide 16:9 landscape cinematic frame. an old European manuscript illustration of a stone emitting rays of light surrounded by alchemical symbols, close-up, warm parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng trong truyện, sự thật về hòn đá rất đen tối. Nó được làm từ linh hồn con người. Rất nhiều linh hồn.

```text
Wide 16:9 landscape cinematic frame. a crimson stone with faint ghostly faces swirling inside it, dark symbolic close-up, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Nghĩa là hòn đá không phá luật ngang giá. Nó chỉ trả giá bằng mạng sống của người khác. Người dùng đá không t…

```text
Wide 16:9 landscape cinematic frame. a balance scale where one pan holds a small crimson stone and the other pan is weighed down by countless tiny faceless silhouettes, symbolic illustration, dark red light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Kaku thấy đây là cú lật tuyệt vời của Arakawa. Giấc mơ không phải trả giá thật ra là cơn ác mộng của người ph…

```text
Wide 16:9 landscape cinematic frame. a golden treasure chest opening to reveal only darkness inside, symbolic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Hai anh em quyết định không dùng hòn đá để lấy lại cơ thể, dù có cơ hội. Vì họ không muốn lấy mạng người khác…

```text
Wide 16:9 landscape cinematic frame. two brothers standing firmly with their backs to a glowing red stone on a pedestal, walking away, wide shot, warm determined light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Bí mật lớn nhất: năng lượng đến từ đâu?

Lời: Giờ tới bí mật lớn nhất. Người Amestris tin rằng giả kim thuật của họ lấy năng lượng từ chuyển động của vỏ tr…

```text
Wide 16:9 landscape cinematic frame. a cross-section illustration of the earth's crust with glowing lines of energy rising toward a small city on the surface, diagram style, warm light. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nhưng những người dùng Luyện đan thuật từ Xing cảm nhận được một điều lạ. Năng lượng dưới Amestris không giốn…

```text
Wide 16:9 landscape cinematic frame. a person kneeling with a palm pressed to the ground, faint ghostly whispers rising from the soil around the hand, eerie close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Sự thật là: có một thực thể gọi là Người cha đã đặt một hòn đá triết gia khổng lồ dưới lòng đất Amestris. Năn…

```text
Wide 16:9 landscape cinematic frame. a vast underground cavern with an enormous glowing red core beneath a sleeping country, cross-section illustration, ominous crimson light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nghĩa là mỗi phép giả kim ở Amestris, dù nhỏ nhất, cũng đang dùng năng lượng từ những linh hồn trong đá. Cả đ…

```text
Wide 16:9 landscape cinematic frame. an ordinary town square with people going about their day while faint red veins glow beneath the cobblestones, wide shot, uneasy warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Và hình dạng của chính đất nước Amestris là một vòng tròn chuyển hóa khổng lồ. Mỗi nơi xảy ra đổ máu trong lị…

```text
Wide 16:9 landscape cinematic frame. an old map of a circular country with a glowing transmutation circle overlaid on its borders, dots marking points along the circle, parchment close-up, amber and red ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Đó là vì sao khi Người cha chặn năng lượng, mọi nhà giả kim Amestris bất lực, nhưng người dùng Luyện đan thuậ…

```text
Wide 16:9 landscape cinematic frame. a split scene: a group of people staring at their unresponsive hands on one side, a single person transmuting with glowing green light on the other, symmetrical composition. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói: đây là một trong những cú bẻ lái hay nhất trong anime. Nó biến một hệ thống khoa học thành một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring wide-eyed at a map with a red circle on it, feathers slightly ruffled. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Những hiểu lầm về giả kim thuật

Lời: Hiểu lầm một: chắp tay là mạnh hơn vẽ vòng tròn. Không hẳn. Chắp tay chỉ nhanh hơn, vì không cần vẽ. Sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a split image: a hand drawing a chalk circle slowly on one side, two hands clapping on the other, with an equal sign between them, diagram style. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hiểu lầm hai: hòn đá triết gia tạo ra thứ từ hư không. Không. Như Kaku vừa nói, nó chỉ là một khối năng lượng…

```text
Wide 16:9 landscape cinematic frame. a crossed-out drawing of a stone creating objects from nothing, beside a drawing of a stone filled with tiny figures, parchment, amber ink. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Hiểu lầm ba: Chân lý là kẻ ác. Chân lý không trừng phạt vì ghét. Nó chỉ thu phí, đúng theo luật. Nó giống một…

```text
Wide 16:9 landscape cinematic frame. a featureless silhouette sitting calmly before a gate, holding out an open palm like a toll collector, eerie wide shot, white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Hiểu lầm bốn, lớn nhất: trao đổi ngang giá là chân lý tuyệt đối của thế giới. Chính bộ truyện đặt câu hỏi cho…

```text
Wide 16:9 landscape cinematic frame. a large balance scale with one pan slowly tipping, a question mark hovering above it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Cái kết: một luật mới

Lời: Ở trận cuối, Alphonse hy sinh linh hồn mình để trả lại cánh tay cho anh. Và để cứu em, Edward phải tìm một th…

```text
Wide 16:9 landscape cinematic frame. an empty suit of old armor sitting quietly in a ruined hall with light falling through a broken ceiling, wide shot, melancholy dust-filled light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Edward chọn đổi chính cánh cổng Chân lý của mình, tức là khả năng dùng giả kim thuật. Suốt đời. Để đổi lấy em…

```text
Wide 16:9 landscape cinematic frame. a young man standing before a colossal stone gate with his hand raised, the gate beginning to crumble into dust, wide shot, radiant white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Chân lý nói rằng đó là câu trả lời đúng. Edward thắng Chân lý không phải bằng cách gian lận luật, mà bằng các…

```text
Wide 16:9 landscape cinematic frame. a young man walking away from a crumbling gate toward a bright doorway, back view, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Ở cuối truyện, hai anh em nói về một luật mới. Không chỉ nhận mười rồi trả mười. Mà nhận mười, thêm một phần…

```text
Wide 16:9 landscape cinematic frame. a notebook page with the numbers ten, plus one, equals eleven written in neat handwriting, a small heart doodle beside it, close-up, warm amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Đó là câu trả lời cho hiểu lầm lớn nhất. Trao đổi ngang giá là luật của giả kim, nhưng không phải luật của lò…

```text
Wide 16:9 landscape cinematic frame. two hands passing a small warm glowing light to a third hand, extreme close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là cái kết đẹp nhất một bộ truyện về hệ thống sức mạnh có thể có. Nhân vật chính mất hết sức mạ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot quietly closing its alchemy notebook and placing a small flower on top of it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Giả kim thuật thật và giả kim thuật trong truyện

Lời: Trước khi tổng kết, vài chi tiết đời thật. Nhà vật lý Isaac Newton, người phát hiện định luật hấp dẫn, đã viế…

```text
Wide 16:9 landscape cinematic frame. an old desk with a candle, a quill and handwritten notes covered in alchemical symbols beside an apple, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Nhà giả kim Paracelsus thế kỷ mười sáu từng viết về việc tạo ra một người nhân tạo nhỏ trong bình, gọi là hom…

```text
Wide 16:9 landscape cinematic frame. a sealed glass flask on an old workbench with a tiny faint shadowy shape inside, close-up, eerie greenish light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Biểu tượng con rắn tự cắn đuôi, gọi là ouroboros, là một biểu tượng giả kim thật, nói về vòng tuần hoàn bất t…

```text
Wide 16:9 landscape cinematic frame. an old manuscript illustration of a serpent biting its own tail forming a circle, close-up, warm parchment light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Kaku nhắc lại: giả kim thuật ngoài đời không biến chì thành vàng được, và các thí nghiệm của các nhà giả kim…

```text
Wide 16:9 landscape cinematic frame. a crossed-out dangerous-looking bubbling flask beside a safety goggles icon, parchment warning card, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Sơ đồ tổng kết một hình

Lời: Và đây là toàn bộ giả kim thuật trong một hình. Ở giữa: luật trao đổi ngang giá, gồm bảo toàn khối lượng và c…

```text
Wide 16:9 landscape cinematic frame. a large circular diagram on parchment with a balance scale at the center, amber ink overhead shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Vòng trong: ba bước hiểu, phân giải, tái tạo, và vòng tròn chuyển hóa. Vòng giữa: các nhánh, từ giả kim Amest…

```text
Wide 16:9 landscape cinematic frame. the circular diagram with inner rings labeled with three steps and two branches, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Vòng ngoài: luật cấm biến đổi con người, cánh cổng Chân lý, và hòn đá triết gia. Và dưới tất cả: bí mật về ng…

```text
Wide 16:9 landscape cinematic frame. the full circular diagram with an outer ring of warnings and a red circle glowing faintly beneath, amber and red ink, overhead shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Cuối cùng, một dòng chữ nhỏ ở mép giấy: nhận mười, trả mười một. Luật không có trong sách giả kim nào, nhưng…

```text
Wide 16:9 landscape cinematic frame. a small handwritten note in the corner of the parchment diagram reading ten and eleven with a tiny heart, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Kết

Lời: Fullmetal Alchemist bắt đầu bằng câu muốn có phải mất đi, và kết thúc bằng câu con người có thể cho nhiều hơn…

```text
Wide 16:9 landscape cinematic frame. two brothers standing on a hill at sunrise looking out over a peaceful town, back view, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Hãy kể cho Kaku nghe: nếu phải trả một phí qua cổng, bạn sẵn sàng đổi gì để lấy lại một điều quan trọng? Và n…

```text
Wide 16:9 landscape cinematic frame. a comment box drawn on parchment with a small gate doodle and the numbers ten and eleven, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Video tiếp theo, Kaku mở một cuốn sử thật: Kingdom, và câu hỏi Tần Thủy Hoàng cùng tướng Lý Tín ngoài đời thậ…

```text
Wide 16:9 landscape cinematic frame. an ancient bamboo scroll unrolled beside a small bronze seal on a dark wooden table, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này giúp bạn hiểu Fullmetal Alchemist sâu hơn, hãy đăng ký kênh. Đó là trao đổi ngang giá: bạn cho…

```text
Wide 16:9 landscape cinematic frame. the owl mascot bowing slightly with one wing on its chest beside a small balance scale. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Giả kim thuật là gì?

Khoảng 135 giây · cảnh s01–s11 · 1760 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết Fullmetal Alchemist Brotherhood, kể cả bí mật lớn nhất về nguồn năng lượng của giả kim thuật và cái kết. Nếu bạn chưa xem, hãy lưu lại.

<short pause> Con người không thể có được thứ gì mà không trả lại một thứ khác. Muốn có, phải mất đi một thứ có giá trị tương đương. Đó là câu mở đầu nổi tiếng của Fullmetal Alchemist.

<short pause> Hai anh em nhà Elric tin vào câu đó. Và vì tin, họ nghĩ rằng nếu đưa đủ nguyên liệu, họ có thể mang người mẹ đã mất trở lại.

<short pause> Họ đã sai. Người anh mất một chân. Người em mất toàn bộ cơ thể. Để giữ linh hồn em lại, người anh đánh đổi thêm một cánh tay.

<short pause> Câu hỏi hôm nay: giả kim thuật trong Fullmetal Alchemist hoạt động thế nào? Luật trao đổi ngang giá có thật sự tuyệt đối không? Và năng lượng của nó đến từ đâu?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở một cuốn sổ giả kim: từ luật nền, qua các nhánh, tới những luật cấm, và cuối video là một sơ đồ tổng kết trong một hình.

<short pause> Fullmetal Alchemist là manga của Arakawa Hiromu, đăng từ năm 2001 tới 2010. Truyện có hai bản anime do studio Bones làm: bản năm 2003 và bản Brotherhood năm 2009, bám sát manga.

<short pause> Trong thế giới của truyện, giả kim thuật không phải phép thuật. Nó là một ngành khoa học: hiểu cấu tạo của vật chất, rồi biến đổi nó thành thứ khác.

<short pause> Nhà giả kim giỏi phải học rất nhiều: hóa học, vật lý, sinh học, và cả toán. Ở tuổi mười hai, Edward đã là một nhà giả kim quốc gia, vì cậu đọc sách nhiều như người khác ăn cơm.

<short pause> Ngoài đời thật, giả kim thuật cũng từng tồn tại, từ châu Âu, thế giới Ả Rập tới Trung Hoa. Người ta tìm cách biến chì thành vàng và tìm thuốc trường sinh. Từ những thí nghiệm đó, ngành hóa học ra đời.

<short pause> Arakawa đã lấy rất nhiều biểu tượng từ giả kim thuật thật, rồi xây một hệ thống có luật rõ ràng. Kaku sẽ chỉ ra những chỗ trùng khớp khi tới.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết Fullmetal Alchemist Brotherhood, kể cả bí mật lớn nhất về nguồn năng lượng của giả kim thuật và cái kết. Nếu bạn chưa xem, hãy lưu lại.

[pause] Con người không thể có được thứ gì mà không trả lại một thứ khác. Muốn có, phải mất đi một thứ có giá trị tương đương. Đó là câu mở đầu nổi tiếng của Fullmetal Alchemist.

[pause] Hai anh em nhà Elric tin vào câu đó. Và vì tin, họ nghĩ rằng nếu đưa đủ nguyên liệu, họ có thể mang người mẹ đã mất trở lại.

[pause] Họ đã sai. Người anh mất một chân. Người em mất toàn bộ cơ thể. Để giữ linh hồn em lại, người anh đánh đổi thêm một cánh tay.

[pause] [curious] Câu hỏi hôm nay: giả kim thuật trong Fullmetal Alchemist hoạt động thế nào? Luật trao đổi ngang giá có thật sự tuyệt đối không? Và năng lượng của nó đến từ đâu?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở một cuốn sổ giả kim: từ luật nền, qua các nhánh, tới những luật cấm, và cuối video là một sơ đồ tổng kết trong một hình.

[pause] Fullmetal Alchemist là manga của Arakawa Hiromu, đăng từ năm 2001 tới 2010. Truyện có hai bản anime do studio Bones làm: bản năm 2003 và bản Brotherhood năm 2009, bám sát manga.

[pause] Trong thế giới của truyện, giả kim thuật không phải phép thuật. Nó là một ngành khoa học: hiểu cấu tạo của vật chất, rồi biến đổi nó thành thứ khác.

[pause] Nhà giả kim giỏi phải học rất nhiều: hóa học, vật lý, sinh học, và cả toán. Ở tuổi mười hai, Edward đã là một nhà giả kim quốc gia, vì cậu đọc sách nhiều như người khác ăn cơm.

[pause] Ngoài đời thật, giả kim thuật cũng từng tồn tại, từ châu Âu, thế giới Ả Rập tới Trung Hoa. Người ta tìm cách biến chì thành vàng và tìm thuốc trường sinh. Từ những thí nghiệm đó, ngành hóa học ra đời.

[pause] Arakawa đã lấy rất nhiều biểu tượng từ giả kim thuật thật, rồi xây một hệ thống có luật rõ ràng. Kaku sẽ chỉ ra những chỗ trùng khớp khi tới.
```

### c02 · Luật nền: trao đổi ngang giá / Ba bước: hiểu, phân giải, tái tạo

Khoảng 134 giây · cảnh s12–s24 · 1743 ký tự

**Gemini**

```text
Luật nền của mọi phép giả kim là trao đổi ngang giá. Không thể tạo ra thứ gì từ hư không. Muốn có một thứ, phải đưa vào một thứ tương đương.

<short pause> Luật này chia làm hai phần. Phần một: bảo toàn khối lượng. Một ký sắt chỉ có thể biến thành một ký thứ gì đó, không hơn không kém.

<short pause> Nghe quen không? Ngoài đời, nhà hóa học Lavoisier đã nêu định luật bảo toàn khối lượng vào cuối thế kỷ mười tám: trong phản ứng hóa học, khối lượng không tự mất đi hay sinh ra.

<short pause> Phần hai: vật chất chỉ biến đổi thành thứ có cùng bản chất. Gỗ có thể thành một cái bàn gỗ, nhưng không thể thành một thanh kiếm thép.

<short pause> Vì vậy nhà giả kim luôn phải tính toán: mình có bao nhiêu nguyên liệu, thành phần là gì, và thứ mình muốn làm cần gì.

<short pause> <laugh> Kaku rất thích chỗ này. Nó khiến giả kim thuật giống như nấu ăn: không có bột thì không có bánh, và bạn không thể làm bánh mì từ cát.

<short pause> Và luật ngang giá không chỉ là một định luật khoa học trong truyện. Nó là triết lý sống của hai anh em: muốn có, phải trả giá. Cả bộ truyện là hành trình thử thách triết lý đó.

<short pause> Mỗi phép giả kim đi qua ba bước. Bước một: hiểu. Nhà giả kim phải biết chính xác vật mình đang chạm vào được cấu tạo từ gì.

<short pause> Bước hai: phân giải. Vật chất bị tách ra thành những thành phần cơ bản.

<short pause> Bước ba: tái tạo. Những thành phần đó được ghép lại thành hình dạng mới mà nhà giả kim muốn.

<short pause> Nếu bước một sai, mọi thứ sau đó đều sai. Đó là lý do tại sao một nhà giả kim không thể biến đổi thứ mình không hiểu.

<short pause> Và cũng vì vậy mà người mạnh nhất không phải người có nhiều năng lượng nhất, mà là người hiểu vật chất sâu nhất. Kiến thức là sức mạnh theo nghĩa đen.

<short pause> Ba bước này nghe đơn giản, nhưng Kaku thấy nó là chìa khóa của cả bộ truyện. Mọi luật cấm, mọi bi kịch, đều xuất phát từ một chỗ: con người muốn làm bước ba khi chưa làm xong bước một.
```

**ElevenLabs**

```text
Luật nền của mọi phép giả kim là trao đổi ngang giá. Không thể tạo ra thứ gì từ hư không. Muốn có một thứ, phải đưa vào một thứ tương đương.

[pause] Luật này chia làm hai phần. Phần một: bảo toàn khối lượng. Một ký sắt chỉ có thể biến thành một ký thứ gì đó, không hơn không kém.

[pause] [curious] Nghe quen không? Ngoài đời, nhà hóa học Lavoisier đã nêu định luật bảo toàn khối lượng vào cuối thế kỷ mười tám: trong phản ứng hóa học, khối lượng không tự mất đi hay sinh ra.

[pause] Phần hai: vật chất chỉ biến đổi thành thứ có cùng bản chất. Gỗ có thể thành một cái bàn gỗ, nhưng không thể thành một thanh kiếm thép.

[pause] Vì vậy nhà giả kim luôn phải tính toán: mình có bao nhiêu nguyên liệu, thành phần là gì, và thứ mình muốn làm cần gì.

[pause] [chuckles] Kaku rất thích chỗ này. Nó khiến giả kim thuật giống như nấu ăn: không có bột thì không có bánh, và bạn không thể làm bánh mì từ cát.

[pause] Và luật ngang giá không chỉ là một định luật khoa học trong truyện. Nó là triết lý sống của hai anh em: muốn có, phải trả giá. Cả bộ truyện là hành trình thử thách triết lý đó.

[pause] Mỗi phép giả kim đi qua ba bước. Bước một: hiểu. Nhà giả kim phải biết chính xác vật mình đang chạm vào được cấu tạo từ gì.

[pause] Bước hai: phân giải. Vật chất bị tách ra thành những thành phần cơ bản.

[pause] Bước ba: tái tạo. Những thành phần đó được ghép lại thành hình dạng mới mà nhà giả kim muốn.

[pause] Nếu bước một sai, mọi thứ sau đó đều sai. Đó là lý do tại sao một nhà giả kim không thể biến đổi thứ mình không hiểu.

[pause] Và cũng vì vậy mà người mạnh nhất không phải người có nhiều năng lượng nhất, mà là người hiểu vật chất sâu nhất. Kiến thức là sức mạnh theo nghĩa đen.

[pause] Ba bước này nghe đơn giản, nhưng Kaku thấy nó là chìa khóa của cả bộ truyện. Mọi luật cấm, mọi bi kịch, đều xuất phát từ một chỗ: con người muốn làm bước ba khi chưa làm xong bước một.
```

### c03 · Vòng tròn chuyển hóa / Các nhánh giả kim

Khoảng 147 giây · cảnh s25–s37 · 1906 ký tự

**Gemini**

```text
Để kích hoạt, nhà giả kim vẽ một vòng tròn chuyển hóa. Vòng tròn tượng trưng cho dòng năng lượng tuần hoàn. Các ký hiệu bên trong cho biết sẽ làm gì với vật chất.

<short pause> Mỗi nhà giả kim có vòng tròn riêng, phù hợp với chuyên môn của mình. Có người khắc vòng tròn lên găng tay, lên áo giáp, thậm chí lên chính da thịt.

<short pause> Ví dụ, Hỏa thuật sư Roy Mustang dùng găng tay có vòng tròn và vật liệu tạo tia lửa. Anh búng tay tạo tia lửa, rồi điều khiển nồng độ khí oxy trong không khí để tạo ra ngọn lửa lớn.

<short pause> Kaku thích năng lực này vì nó rất gần với hóa học thật: lửa cần nhiên liệu, oxy và nhiệt. Và nó cũng có điểm yếu thật: trời mưa, găng ướt, thì không có tia lửa.

<short pause> Nhưng Edward thì không cần vẽ. Cậu chỉ cần chắp hai tay lại. Hai bàn tay khép thành một vòng tròn, và cơ thể cậu chính là vòng tròn chuyển hóa.

<short pause> Vì sao Edward làm được vậy? Câu trả lời nằm ở luật cấm lớn nhất. Kaku sẽ kể ngay sau đây.

<short pause> Ở đất nước Amestris, những nhà giả kim giỏi nhất được quân đội tuyển làm nhà giả kim quốc gia. Mỗi người có một biệt danh theo chuyên môn.

<short pause> Có người chuyên về lửa. Có người chuyên về đá và đất, dùng nắm đấm để biến đổi. Có người chuyên về vụ nổ. Và Edward, biệt danh Giả kim thuật sư Thép, chuyên về kim loại.

<short pause> Được làm nhà giả kim quốc gia nghĩa là có tiền nghiên cứu và đặc quyền. <short pause> Nhưng cũng có nghĩa là thành vũ khí của quân đội. Người dân gọi họ là chó của quân đội.

<short pause> Rồi có một nhánh hoàn toàn khác, đến từ đất nước Xing ở phương Đông, gọi là Luyện đan thuật. Nó tập trung vào y học và chữa bệnh.

<short pause> Luyện đan thuật dựa trên khái niệm Long mạch: dòng năng lượng sống chảy trong lòng đất, từ núi cao xuống đồng bằng, giống như máu chảy trong mạch.

<short pause> Điểm mạnh riêng của Luyện đan thuật: có thể biến đổi từ xa, bằng cách cắm những con dao nhỏ quanh mục tiêu thành một vòng tròn.

<short pause> Hai nhánh, hai cách nhìn. Amestris xem giả kim là công cụ, là vũ khí. Xing xem nó là cách chữa lành. Sự khác biệt đó sẽ trở thành bí mật lớn nhất của truyện.
```

**ElevenLabs**

```text
Để kích hoạt, nhà giả kim vẽ một vòng tròn chuyển hóa. Vòng tròn tượng trưng cho dòng năng lượng tuần hoàn. Các ký hiệu bên trong cho biết sẽ làm gì với vật chất.

[pause] Mỗi nhà giả kim có vòng tròn riêng, phù hợp với chuyên môn của mình. Có người khắc vòng tròn lên găng tay, lên áo giáp, thậm chí lên chính da thịt.

[pause] Ví dụ, Hỏa thuật sư Roy Mustang dùng găng tay có vòng tròn và vật liệu tạo tia lửa. Anh búng tay tạo tia lửa, rồi điều khiển nồng độ khí oxy trong không khí để tạo ra ngọn lửa lớn.

[pause] Kaku thích năng lực này vì nó rất gần với hóa học thật: lửa cần nhiên liệu, oxy và nhiệt. Và nó cũng có điểm yếu thật: trời mưa, găng ướt, thì không có tia lửa.

[pause] Nhưng Edward thì không cần vẽ. Cậu chỉ cần chắp hai tay lại. Hai bàn tay khép thành một vòng tròn, và cơ thể cậu chính là vòng tròn chuyển hóa.

[pause] [curious] Vì sao Edward làm được vậy? Câu trả lời nằm ở luật cấm lớn nhất. Kaku sẽ kể ngay sau đây.

[pause] Ở đất nước Amestris, những nhà giả kim giỏi nhất được quân đội tuyển làm nhà giả kim quốc gia. Mỗi người có một biệt danh theo chuyên môn.

[pause] Có người chuyên về lửa. Có người chuyên về đá và đất, dùng nắm đấm để biến đổi. Có người chuyên về vụ nổ. Và Edward, biệt danh Giả kim thuật sư Thép, chuyên về kim loại.

[pause] Được làm nhà giả kim quốc gia nghĩa là có tiền nghiên cứu và đặc quyền. [pause] Nhưng cũng có nghĩa là thành vũ khí của quân đội. Người dân gọi họ là chó của quân đội.

[pause] Rồi có một nhánh hoàn toàn khác, đến từ đất nước Xing ở phương Đông, gọi là Luyện đan thuật. Nó tập trung vào y học và chữa bệnh.

[pause] Luyện đan thuật dựa trên khái niệm Long mạch: dòng năng lượng sống chảy trong lòng đất, từ núi cao xuống đồng bằng, giống như máu chảy trong mạch.

[pause] Điểm mạnh riêng của Luyện đan thuật: có thể biến đổi từ xa, bằng cách cắm những con dao nhỏ quanh mục tiêu thành một vòng tròn.

[pause] Hai nhánh, hai cách nhìn. Amestris xem giả kim là công cụ, là vũ khí. Xing xem nó là cách chữa lành. Sự khác biệt đó sẽ trở thành bí mật lớn nhất của truyện.
```

### c04 · Luật cấm: biến đổi con người / Hòn đá triết gia

Khoảng 142 giây · cảnh s38–s50 · 1847 ký tự

**Gemini**

```text
Nhà giả kim quốc gia có những luật phải giữ, và có một điều cấm mà mọi nhà giả kim đều biết: không được biến đổi con người.

<short pause> Vì sao? Vì không ai tính được giá trị của một con người. Nước, than, vôi, sắt, phốt pho... có thể mua được hết. <short pause> Nhưng linh hồn thì đổi bằng gì?

<short pause> Hai anh em Elric đã thử. Kết quả: không phải mẹ họ trở lại. Và họ mất đi những thứ không bao giờ lấy lại được bằng giả kim.

<short pause> Người thử biến đổi con người sẽ bị kéo tới trước một cánh cổng khổng lồ và gặp một thực thể gọi là Chân lý. Chân lý lấy đi một phần cơ thể làm phí qua cổng.

<short pause> Nhưng Chân lý cũng cho họ nhìn thấy một thứ: toàn bộ kiến thức của thế giới trong một khoảnh khắc. Đó là lý do Edward không cần vẽ vòng tròn nữa. Cậu đã thấy Chân lý.

<short pause> Một điều đáng sợ: Chân lý nói với Edward rằng nó là thế giới, là vũ trụ, là tất cả, và cũng là chính cậu. Mỗi người gặp Chân lý đều gặp một phiên bản của mình.

<short pause> <laugh> Kaku để ý: phí qua cổng luôn liên quan tới điều người đó mong muốn. Người muốn nhìn thấy sự thật thì mất đi đôi mắt. Người muốn đứng dậy thì mất đi đôi chân. Luật này tàn nhẫn nhưng rất công bằng.

<short pause> Truyền thuyết nói có một thứ có thể phá luật ngang giá: hòn đá triết gia. Có nó, nhà giả kim có thể làm mọi phép mà không cần trả giá.

<short pause> Ngoài đời thật, hòn đá triết gia cũng là giấc mơ của các nhà giả kim châu Âu: thứ biến kim loại thường thành vàng và mang lại sự trường sinh.

<short pause> Nhưng trong truyện, sự thật về hòn đá rất đen tối. Nó được làm từ linh hồn con người. Rất nhiều linh hồn.

<short pause> Nghĩa là hòn đá không phá luật ngang giá. Nó chỉ trả giá bằng mạng sống của người khác. Người dùng đá không trả gì, vì người khác đã trả thay.

<short pause> Kaku thấy đây là cú lật tuyệt vời của Arakawa. Giấc mơ không phải trả giá thật ra là cơn ác mộng của người phải trả giá thay.

<short pause> Hai anh em quyết định không dùng hòn đá để lấy lại cơ thể, dù có cơ hội. Vì họ không muốn lấy mạng người khác để sửa sai lầm của mình.
```

**ElevenLabs**

```text
Nhà giả kim quốc gia có những luật phải giữ, và có một điều cấm mà mọi nhà giả kim đều biết: không được biến đổi con người.

[pause] [curious] Vì sao? Vì không ai tính được giá trị của một con người. Nước, than, vôi, sắt, phốt pho... có thể mua được hết. [pause] Nhưng linh hồn thì đổi bằng gì?

[pause] Hai anh em Elric đã thử. Kết quả: không phải mẹ họ trở lại. Và họ mất đi những thứ không bao giờ lấy lại được bằng giả kim.

[pause] Người thử biến đổi con người sẽ bị kéo tới trước một cánh cổng khổng lồ và gặp một thực thể gọi là Chân lý. Chân lý lấy đi một phần cơ thể làm phí qua cổng.

[pause] Nhưng Chân lý cũng cho họ nhìn thấy một thứ: toàn bộ kiến thức của thế giới trong một khoảnh khắc. Đó là lý do Edward không cần vẽ vòng tròn nữa. Cậu đã thấy Chân lý.

[pause] Một điều đáng sợ: Chân lý nói với Edward rằng nó là thế giới, là vũ trụ, là tất cả, và cũng là chính cậu. Mỗi người gặp Chân lý đều gặp một phiên bản của mình.

[pause] [chuckles] Kaku để ý: phí qua cổng luôn liên quan tới điều người đó mong muốn. Người muốn nhìn thấy sự thật thì mất đi đôi mắt. Người muốn đứng dậy thì mất đi đôi chân. Luật này tàn nhẫn nhưng rất công bằng.

[pause] Truyền thuyết nói có một thứ có thể phá luật ngang giá: hòn đá triết gia. Có nó, nhà giả kim có thể làm mọi phép mà không cần trả giá.

[pause] Ngoài đời thật, hòn đá triết gia cũng là giấc mơ của các nhà giả kim châu Âu: thứ biến kim loại thường thành vàng và mang lại sự trường sinh.

[pause] Nhưng trong truyện, sự thật về hòn đá rất đen tối. Nó được làm từ linh hồn con người. Rất nhiều linh hồn.

[pause] Nghĩa là hòn đá không phá luật ngang giá. Nó chỉ trả giá bằng mạng sống của người khác. Người dùng đá không trả gì, vì người khác đã trả thay.

[pause] Kaku thấy đây là cú lật tuyệt vời của Arakawa. Giấc mơ không phải trả giá thật ra là cơn ác mộng của người phải trả giá thay.

[pause] Hai anh em quyết định không dùng hòn đá để lấy lại cơ thể, dù có cơ hội. Vì họ không muốn lấy mạng người khác để sửa sai lầm của mình.
```

### c05 · Bí mật lớn nhất: năng lượng đến từ đâu? / Những hiểu lầm về giả kim thuật

Khoảng 137 giây · cảnh s51–s61 · 1784 ký tự

**Gemini**

```text
Giờ tới bí mật lớn nhất. Người Amestris tin rằng giả kim thuật của họ lấy năng lượng từ chuyển động của vỏ trái đất, giống như năng lượng từ lòng đất.

<short pause> Nhưng những người dùng Luyện đan thuật từ Xing cảm nhận được một điều lạ. Năng lượng dưới Amestris không giống dòng chảy của đất. Nó giống như tiếng của rất nhiều người.

<short pause> Sự thật là: có một thực thể gọi là Người cha đã đặt một hòn đá triết gia khổng lồ dưới lòng đất Amestris. Năng lượng của nó chặn dòng năng lượng thật, và cung cấp cho mọi nhà giả kim trong nước.

<short pause> Nghĩa là mỗi phép giả kim ở Amestris, dù nhỏ nhất, cũng đang dùng năng lượng từ những linh hồn trong đá. Cả đất nước đang sống nhờ một tội ác mà họ không biết.

<short pause> Và hình dạng của chính đất nước Amestris là một vòng tròn chuyển hóa khổng lồ. Mỗi nơi xảy ra đổ máu trong lịch sử đều nằm trên các điểm của vòng tròn đó.

<short pause> Đó là vì sao khi Người cha chặn năng lượng, mọi nhà giả kim Amestris bất lực, nhưng người dùng Luyện đan thuật thì vẫn làm được. Họ dùng dòng chảy thật của đất, không phải dòng chảy từ đá.

<short pause> <laugh> Kaku phải nói: đây là một trong những cú bẻ lái hay nhất trong anime. Nó biến một hệ thống khoa học thành một câu chuyện chính trị về cái giá của sức mạnh quốc gia.

<short pause> Hiểu lầm một: chắp tay là mạnh hơn vẽ vòng tròn. Không hẳn. Chắp tay chỉ nhanh hơn, vì không cần vẽ. Sức mạnh vẫn phụ thuộc vào kiến thức và nguyên liệu.

<short pause> Hiểu lầm hai: hòn đá triết gia tạo ra thứ từ hư không. Không. Như Kaku vừa nói, nó chỉ là một khối năng lượng được trả trước bằng linh hồn người.

<short pause> Hiểu lầm ba: Chân lý là kẻ ác. Chân lý không trừng phạt vì ghét. Nó chỉ thu phí, đúng theo luật. Nó giống một người gác cổng lạnh lùng hơn là một con quỷ.

<short pause> Hiểu lầm bốn, lớn nhất: trao đổi ngang giá là chân lý tuyệt đối của thế giới. Chính bộ truyện đặt câu hỏi cho điều này. Kaku để dành cho chương tiếp theo.
```

**ElevenLabs**

```text
Giờ tới bí mật lớn nhất. Người Amestris tin rằng giả kim thuật của họ lấy năng lượng từ chuyển động của vỏ trái đất, giống như năng lượng từ lòng đất.

[pause] Nhưng những người dùng Luyện đan thuật từ Xing cảm nhận được một điều lạ. Năng lượng dưới Amestris không giống dòng chảy của đất. Nó giống như tiếng của rất nhiều người.

[pause] Sự thật là: có một thực thể gọi là Người cha đã đặt một hòn đá triết gia khổng lồ dưới lòng đất Amestris. Năng lượng của nó chặn dòng năng lượng thật, và cung cấp cho mọi nhà giả kim trong nước.

[pause] Nghĩa là mỗi phép giả kim ở Amestris, dù nhỏ nhất, cũng đang dùng năng lượng từ những linh hồn trong đá. Cả đất nước đang sống nhờ một tội ác mà họ không biết.

[pause] Và hình dạng của chính đất nước Amestris là một vòng tròn chuyển hóa khổng lồ. Mỗi nơi xảy ra đổ máu trong lịch sử đều nằm trên các điểm của vòng tròn đó.

[pause] Đó là vì sao khi Người cha chặn năng lượng, mọi nhà giả kim Amestris bất lực, nhưng người dùng Luyện đan thuật thì vẫn làm được. Họ dùng dòng chảy thật của đất, không phải dòng chảy từ đá.

[pause] [chuckles] Kaku phải nói: đây là một trong những cú bẻ lái hay nhất trong anime. Nó biến một hệ thống khoa học thành một câu chuyện chính trị về cái giá của sức mạnh quốc gia.

[pause] Hiểu lầm một: chắp tay là mạnh hơn vẽ vòng tròn. Không hẳn. Chắp tay chỉ nhanh hơn, vì không cần vẽ. Sức mạnh vẫn phụ thuộc vào kiến thức và nguyên liệu.

[pause] Hiểu lầm hai: hòn đá triết gia tạo ra thứ từ hư không. Không. Như Kaku vừa nói, nó chỉ là một khối năng lượng được trả trước bằng linh hồn người.

[pause] Hiểu lầm ba: Chân lý là kẻ ác. Chân lý không trừng phạt vì ghét. Nó chỉ thu phí, đúng theo luật. Nó giống một người gác cổng lạnh lùng hơn là một con quỷ.

[pause] Hiểu lầm bốn, lớn nhất: trao đổi ngang giá là chân lý tuyệt đối của thế giới. Chính bộ truyện đặt câu hỏi cho điều này. Kaku để dành cho chương tiếp theo.
```

### c06 · Cái kết: một luật mới / Giả kim thuật thật và giả kim thuật trong truyện

Khoảng 118 giây · cảnh s62–s71 · 1537 ký tự

**Gemini**

```text
Ở trận cuối, Alphonse hy sinh linh hồn mình để trả lại cánh tay cho anh. Và để cứu em, Edward phải tìm một thứ đủ giá trị để đổi.

<short pause> Edward chọn đổi chính cánh cổng Chân lý của mình, tức là khả năng dùng giả kim thuật. Suốt đời. Để đổi lấy em trai.

<short pause> Chân lý nói rằng đó là câu trả lời đúng. Edward thắng Chân lý không phải bằng cách gian lận luật, mà bằng cách hiểu rằng cậu không cần giả kim để là chính mình.

<short pause> Ở cuối truyện, hai anh em nói về một luật mới. Không chỉ nhận mười rồi trả mười. Mà nhận mười, thêm một phần của chính mình, rồi trả lại mười một.

<short pause> Đó là câu trả lời cho hiểu lầm lớn nhất. Trao đổi ngang giá là luật của giả kim, nhưng không phải luật của lòng tốt. Con người có thể cho nhiều hơn những gì họ nhận.

<short pause> <laugh> Kaku nghĩ đây là cái kết đẹp nhất một bộ truyện về hệ thống sức mạnh có thể có. Nhân vật chính mất hết sức mạnh, và câu chuyện nói đó là chiến thắng.

<short pause> Trước khi tổng kết, vài chi tiết đời thật. Nhà vật lý Isaac Newton, người phát hiện định luật hấp dẫn, đã viết rất nhiều ghi chép về giả kim thuật.

<short pause> Nhà giả kim Paracelsus thế kỷ mười sáu từng viết về việc tạo ra một người nhân tạo nhỏ trong bình, gọi là homunculus. Trong truyện, những kẻ thù chính cũng mang tên Homunculus.

<short pause> Biểu tượng con rắn tự cắn đuôi, gọi là ouroboros, là một biểu tượng giả kim thật, nói về vòng tuần hoàn bất tận. Arakawa dùng nó làm dấu hiệu cho các Homunculus.

<short pause> Kaku nhắc lại: giả kim thuật ngoài đời không biến chì thành vàng được, và các thí nghiệm của các nhà giả kim xưa rất nguy hiểm. Video này là để hiểu truyện, không phải hướng dẫn thí nghiệm.
```

**ElevenLabs**

```text
Ở trận cuối, Alphonse hy sinh linh hồn mình để trả lại cánh tay cho anh. Và để cứu em, Edward phải tìm một thứ đủ giá trị để đổi.

[pause] Edward chọn đổi chính cánh cổng Chân lý của mình, tức là khả năng dùng giả kim thuật. Suốt đời. Để đổi lấy em trai.

[pause] Chân lý nói rằng đó là câu trả lời đúng. Edward thắng Chân lý không phải bằng cách gian lận luật, mà bằng cách hiểu rằng cậu không cần giả kim để là chính mình.

[pause] Ở cuối truyện, hai anh em nói về một luật mới. Không chỉ nhận mười rồi trả mười. Mà nhận mười, thêm một phần của chính mình, rồi trả lại mười một.

[pause] Đó là câu trả lời cho hiểu lầm lớn nhất. Trao đổi ngang giá là luật của giả kim, nhưng không phải luật của lòng tốt. Con người có thể cho nhiều hơn những gì họ nhận.

[pause] [chuckles] Kaku nghĩ đây là cái kết đẹp nhất một bộ truyện về hệ thống sức mạnh có thể có. Nhân vật chính mất hết sức mạnh, và câu chuyện nói đó là chiến thắng.

[pause] Trước khi tổng kết, vài chi tiết đời thật. Nhà vật lý Isaac Newton, người phát hiện định luật hấp dẫn, đã viết rất nhiều ghi chép về giả kim thuật.

[pause] Nhà giả kim Paracelsus thế kỷ mười sáu từng viết về việc tạo ra một người nhân tạo nhỏ trong bình, gọi là homunculus. Trong truyện, những kẻ thù chính cũng mang tên Homunculus.

[pause] Biểu tượng con rắn tự cắn đuôi, gọi là ouroboros, là một biểu tượng giả kim thật, nói về vòng tuần hoàn bất tận. Arakawa dùng nó làm dấu hiệu cho các Homunculus.

[pause] Kaku nhắc lại: giả kim thuật ngoài đời không biến chì thành vàng được, và các thí nghiệm của các nhà giả kim xưa rất nguy hiểm. Video này là để hiểu truyện, không phải hướng dẫn thí nghiệm.
```

### c07 · Sơ đồ tổng kết một hình / Kết

Khoảng 93 giây · cảnh s72–s79 · 1214 ký tự

**Gemini**

```text
Và đây là toàn bộ giả kim thuật trong một hình. Ở giữa: luật trao đổi ngang giá, gồm bảo toàn khối lượng và cùng bản chất.

<short pause> Vòng trong: ba bước hiểu, phân giải, tái tạo, và vòng tròn chuyển hóa. Vòng giữa: các nhánh, từ giả kim Amestris tới Luyện đan thuật của Xing.

<short pause> Vòng ngoài: luật cấm biến đổi con người, cánh cổng Chân lý, và hòn đá triết gia. Và dưới tất cả: bí mật về nguồn năng lượng thật của Amestris.

<short pause> Cuối cùng, một dòng chữ nhỏ ở mép giấy: nhận mười, trả mười một. Luật không có trong sách giả kim nào, nhưng là luật quan trọng nhất của truyện.

<short pause> Fullmetal Alchemist bắt đầu bằng câu muốn có phải mất đi, và kết thúc bằng câu con người có thể cho nhiều hơn những gì họ nhận. Giữa hai câu đó là cả một hành trình trưởng thành.

<short pause> Hãy kể cho Kaku nghe: nếu phải trả một phí qua cổng, bạn sẵn sàng đổi gì để lấy lại một điều quan trọng? Và nếu được nhận mười, bạn sẽ thêm phần một của mình vào đâu?

<short pause> Video tiếp theo, Kaku mở một cuốn sử thật: Kingdom, và câu hỏi Tần Thủy Hoàng cùng tướng Lý Tín ngoài đời thật là người thế nào.

<short pause> Nếu video này giúp bạn hiểu Fullmetal Alchemist sâu hơn, hãy đăng ký kênh. <laugh> Đó là trao đổi ngang giá: bạn cho Kaku một cú bấm, Kaku trả bạn thêm nhiều cuốn sổ nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Và đây là toàn bộ giả kim thuật trong một hình. Ở giữa: luật trao đổi ngang giá, gồm bảo toàn khối lượng và cùng bản chất.

[pause] Vòng trong: ba bước hiểu, phân giải, tái tạo, và vòng tròn chuyển hóa. Vòng giữa: các nhánh, từ giả kim Amestris tới Luyện đan thuật của Xing.

[pause] Vòng ngoài: luật cấm biến đổi con người, cánh cổng Chân lý, và hòn đá triết gia. Và dưới tất cả: bí mật về nguồn năng lượng thật của Amestris.

[pause] Cuối cùng, một dòng chữ nhỏ ở mép giấy: nhận mười, trả mười một. Luật không có trong sách giả kim nào, nhưng là luật quan trọng nhất của truyện.

[pause] Fullmetal Alchemist bắt đầu bằng câu muốn có phải mất đi, và kết thúc bằng câu con người có thể cho nhiều hơn những gì họ nhận. Giữa hai câu đó là cả một hành trình trưởng thành.

[pause] [curious] Hãy kể cho Kaku nghe: nếu phải trả một phí qua cổng, bạn sẵn sàng đổi gì để lấy lại một điều quan trọng? Và nếu được nhận mười, bạn sẽ thêm phần một của mình vào đâu?

[pause] Video tiếp theo, Kaku mở một cuốn sử thật: Kingdom, và câu hỏi Tần Thủy Hoàng cùng tướng Lý Tín ngoài đời thật là người thế nào.

[pause] Nếu video này giúp bạn hiểu Fullmetal Alchemist sâu hơn, hãy đăng ký kênh. [chuckles] Đó là trao đổi ngang giá: bạn cho Kaku một cú bấm, Kaku trả bạn thêm nhiều cuốn sổ nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
