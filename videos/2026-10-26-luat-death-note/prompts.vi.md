# Bộ prompt · Death Note: Luật của cuốn sổ và những cách phá luật

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 7 đoạn đọc, khoảng 15.0 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (83 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói về toàn bộ Death Note, kể cả cái kết. Nếu bạn chưa xem, hãy lưu video lại. Đâ…

```text
Wide 16:9 landscape cinematic frame. a plain black notebook lying closed on a school desk beside a spoiler warning card, close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một cuốn sổ đen rơi từ trên trời xuống sân trường. Trên bìa ghi hai chữ. Và bên trong là một danh sách luật l…

```text
Wide 16:9 landscape cinematic frame. a black notebook falling through the air toward an empty schoolyard under a grey sky, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Luật đầu tiên: người bị ghi tên vào sổ sẽ chết. Chỉ vậy thôi. Nhưng từ một luật đơn giản đó, Death Note xây n…

```text
Wide 16:9 landscape cinematic frame. an open notebook with a single blank line and a pen resting on it, extreme close-up, cold stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Vì cuốn sổ không chỉ có một luật. Nó có rất nhiều luật, và người thắng không phải người mạnh nhất, mà là ngườ…

```text
Wide 16:9 landscape cinematic frame. a thick rulebook with many small bookmarks sticking out of its pages, close-up, cool dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở cuốn sổ đáng sợ nhất anime: luật của nó, những cách các nhân vật…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding its own notebook tightly and glancing nervously at a black notebook on the table. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Kaku nói rõ: đây là truyện hư cấu. Video phân tích luật chơi và chiến thuật trong truyện, không cổ vũ bạo lực…

```text
Wide 16:9 landscape cinematic frame. a small notice card with a simple scale icon pinned beside a closed notebook, close-up, soft neutral light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Bối cảnh: Death Note là gì?

Lời: Death Note là manga của Ohba Tsugumi viết truyện và Obata Takeshi vẽ, đăng từ tháng mười hai năm 2003 tới thá…

```text
Wide 16:9 landscape cinematic frame. a neat stack of twelve manga volumes beside a vintage TV on a desk, close-up, cool nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Nhân vật chính là Yagami Light, một học sinh xuất sắc. Cậu nhặt được cuốn sổ, thử nghiệm nó, và phát hiện nó…

```text
Wide 16:9 landscape cinematic frame. a young student sitting alone at a desk at night, a notebook open in front of him and a single desk lamp on, back view, dramatic cold light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Light quyết định dùng cuốn sổ để trừng phạt tội phạm, và tạo ra một thế giới mới không còn cái ác. Người ta g…

```text
Wide 16:9 landscape cinematic frame. a city skyline at night with a single glowing window in a tall residential building, wide shot, ominous blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Cuốn sổ thuộc về Ryuk, một thần chết thấy thế giới thần chết quá nhàm chán nên cố tình thả sổ xuống nhân gian…

```text
Wide 16:9 landscape cinematic frame. a tall shadowy winged silhouette perched on a rooftop at dusk, watching the city below, wide shot, eerie orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Đối thủ của Light là L, thám tử bí ẩn giỏi nhất thế giới, không ai biết mặt, không ai biết tên thật. Và trong…

```text
Wide 16:9 landscape cinematic frame. a single letter printed in an old gothic font on a plain white screen in a dark room, close-up, cold stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Kaku để ý: Death Note là trận đấu giữa hai người đều thông minh, và cả hai đều đọc cùng một cuốn luật. Ai đọc…

```text
Wide 16:9 landscape cinematic frame. two chess players' hands hovering over the same board from opposite sides, close-up, dramatic split light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Luật 1: tên và khuôn mặt

Lời: Luật đầu tiên đầy đủ: người bị ghi tên sẽ chết. Nhưng người viết phải nghĩ tới khuôn mặt của người đó khi viế…

```text
Wide 16:9 landscape cinematic frame. a notebook page with a name line and a small sketch of a face beside it, parchment close-up, cold ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Nghĩa là để giết ai, Light cần hai thứ: tên thật và khuôn mặt. Và đây chính là điểm yếu mà L khai thác: giấu…

```text
Wide 16:9 landscape cinematic frame. a portrait frame with a blank face and a nameplate covered by a strip of tape, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Cách phá của phía L: không bao giờ xuất hiện trước công chúng, dùng bí danh, và nói chuyện qua một màn hình c…

```text
Wide 16:9 landscape cinematic frame. a laptop in a dark hotel room showing a single letter on screen with a voice distortion graphic, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Sau này, L còn dùng cả còng tay để tự khóa mình với Light suốt nhiều tuần, để theo dõi từng hành động. Để bảo…

```text
Wide 16:9 landscape cinematic frame. a pair of handcuffs linking two chairs placed side by side in an investigation room, close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Cái giá của cách phá này: L phải sống ẩn dật hoàn toàn. Không bạn bè, không đời sống bình thường, không thể t…

```text
Wide 16:9 landscape cinematic frame. an empty hotel suite with drawn curtains and room service trays stacked by the door, wide shot, lonely dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Luật 2: bốn mươi giây và sáu phút bốn mươi giây

Lời: Nghe thì chỉ là thủ tục, nhưng những con số này cho thấy tác giả thiết kế cuốn sổ như một bộ luật thật, có th…

```text
Wide 16:9 landscape cinematic frame. a legal document with many small numbered clauses and footnotes under a magnifying glass, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Luật hai: nếu ghi nguyên nhân cái chết trong vòng bốn mươi giây sau khi viết tên, nó sẽ xảy ra. Nếu không ghi…

```text
Wide 16:9 landscape cinematic frame. a stopwatch showing forty seconds placed on an open notebook, close-up, tense cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Luật ba: sau khi ghi nguyên nhân, người viết có thêm sáu phút bốn mươi giây để ghi chi tiết hoàn cảnh.

```text
Wide 16:9 landscape cinematic frame. a second stopwatch showing six minutes and forty seconds beside the first, close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và luật bốn: người viết có thể điều khiển hành động của nạn nhân trước khi chết, trong giới hạn khoảng hai mư…

```text
Wide 16:9 landscape cinematic frame. a calendar with twenty-three days marked in a row and a small figure walking along them, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Nghe như những con số khô khan. Nhưng chính luật điều khiển hành động là vũ khí mạnh nhất của Light.

```text
Wide 16:9 landscape cinematic frame. a puppet on strings sitting motionless on a desk under a lamp, symbolic close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Cách phá 1: thí nghiệm bằng hành động

Lời: Light dùng luật điều khiển hành động để thí nghiệm, rồi để gửi thông điệp. Cậu khiến một số tội phạm trong tù…

```text
Wide 16:9 landscape cinematic frame. several handwritten letters laid out on a table with the first letters of each line circled in red, close-up, cold forensic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Câu đó, đại ý: L, ông có biết thần chết chỉ ăn táo không? Đó là một lời trêu chọc, nhưng cũng là một lần Ligh…

```text
Wide 16:9 landscape cinematic frame. a single red apple placed on a stack of case files, close-up, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Vì qua đó, L suy ra Kira có thể điều khiển hành động của nạn nhân trước khi chết. Mỗi thí nghiệm của Light cũ…

```text
Wide 16:9 landscape cinematic frame. a detective's notebook with a hypothesis written and underlined twice, close-up, cold lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Light từng giết một nhóm đặc vụ đang theo dõi mình bằng một kế hoạch điều khiển hành động phức tạp. Nhưng cũn…

```text
Wide 16:9 landscape cinematic frame. a subway platform at night with empty benches and a single dropped envelope on the ground, wide shot, cold eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Cái giá: kiêu ngạo. Light thích thể hiện, và mỗi lần thể hiện là một lần để lại dấu vết.

```text
Wide 16:9 landscape cinematic frame. a single footprint left in fresh snow leading toward a door, close-up, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · Nước cờ của L

Lời: Giờ tới phía bên kia bàn cờ. L cũng không đọc luật, vì L không có cuốn sổ. L phải đoán luật từ những gì Kira…

```text
Wide 16:9 landscape cinematic frame. a detective's evidence board with pinned photos, timelines and question marks connected by string, close-up, cold lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Nước cờ đầu tiên của L: cho một người đóng thế xuất hiện trên truyền hình, tự xưng là L, thách thức Kira. Kir…

```text
Wide 16:9 landscape cinematic frame. a television studio with a single chair under harsh spotlights and a live broadcast sign lit up, wide shot, tense cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nhưng chương trình chỉ được phát ở một khu vực. Nhờ đó, L biết Kira đang ở vùng Kanto, Nhật Bản, và biết Kira…

```text
Wide 16:9 landscape cinematic frame. a map of a country with a single region shaded and circled in red ink, parchment close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Cách này cho thấy L phá luật kiểu khác: không lách luật, mà dùng hành động của Kira để vẽ lại luật. Mỗi vụ gi…

```text
Wide 16:9 landscape cinematic frame. a detective's hand writing a new rule on a blank page based on a stack of case files, close-up, cold lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Và L còn làm một điều không ai ngờ: tự giới thiệu mình là L với chính Light, người L nghi ngờ nhất. Một nước…

```text
Wide 16:9 landscape cinematic frame. two figures standing at the edge of a university stage during a ceremony, one leaning slightly toward the other, medium shot, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Cách phá 2: mảnh giấy xé ra

Lời: Một luật khác: một mảnh giấy xé ra từ cuốn sổ vẫn có hiệu lực y hệt cuốn sổ. Chỉ cần viết tên lên mảnh đó.

```text
Wide 16:9 landscape cinematic frame. a small torn piece of black paper lying on a wooden desk beside a pen, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Light lợi dụng điều này để giấu những mảnh giấy khắp nơi. Nổi tiếng nhất là một mảnh giấu trong đồng hồ đeo t…

```text
Wide 16:9 landscape cinematic frame. a wristwatch with a tiny hidden compartment slightly open revealing a folded scrap of paper, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Nhờ vậy, Light có thể giết người ngay cả khi bị theo dõi, ngay cả khi không cầm cuốn sổ. Cách phá này biến cu…

```text
Wide 16:9 landscape cinematic frame. a security camera mounted in the corner of a room pointing at a desk where a hand discreetly holds a pen, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Light còn giấu cuốn sổ trong ngăn kéo có đáy giả, gài một cơ chế tự đốt nếu có người mở sai cách. Một cuốn sổ…

```text
Wide 16:9 landscape cinematic frame. a desk drawer with a false bottom partially lifted revealing a hidden compartment and small wires, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Cái giá: Light không bao giờ có thể buông cuốn sổ ra, dù chỉ trong tâm trí. Cậu phải luôn tính toán, luôn đề…

```text
Wide 16:9 landscape cinematic frame. a young man lying awake in bed at night staring at the ceiling, wide shot, cold lonely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Luật 3: quyền sở hữu và ký ức

Lời: Luật tiếp theo, rất quan trọng: người chạm vào cuốn sổ sẽ nhìn thấy thần chết. Và nếu người sở hữu từ bỏ quyề…

```text
Wide 16:9 landscape cinematic frame. a hand releasing a notebook that falls away, with faint memory fragments drifting off like dust, symbolic close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nghe như một bất lợi. Nhưng Light biến nó thành cách phá luật táo bạo nhất trong truyện.

```text
Wide 16:9 landscape cinematic frame. a chess piece being deliberately sacrificed on a board, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Cách phá 3: tự quên mình là Kira

Lời: Khi bị L nghi ngờ, Light tự nguyện bị giam giữ. Rồi cậu từ bỏ quyền sở hữu cuốn sổ, và quên sạch mọi thứ. Lig…

```text
Wide 16:9 landscape cinematic frame. a young man sitting calmly in a bare holding cell under constant camera surveillance, wide shot, cold white light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: L giam Light nhiều tuần, theo dõi từng phút. Nhưng người L theo dõi là một Light vô tội. Không có gì để phát…

```text
Wide 16:9 landscape cinematic frame. a wall of surveillance monitors showing the same quiet cell from multiple angles, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Trong lúc đó, cuốn sổ được chuyển cho một người khác, và các vụ giết người tiếp tục. Light được thả, và thậm…

```text
Wide 16:9 landscape cinematic frame. two figures sitting side by side in front of computer screens in a dark investigation room, back view, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Và rồi, theo kế hoạch Light đã sắp đặt từ trước khi quên, cậu chạm lại vào cuốn sổ, và toàn bộ ký ức ùa về.

```text
Wide 16:9 landscape cinematic frame. a hand touching a black notebook as a burst of light and scattered images flood outward, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Cái giá: Light đánh cược tất cả vào một kế hoạch mà chính cậu không nhớ. Nếu có một mắt xích sai, cậu sẽ mất…

```text
Wide 16:9 landscape cinematic frame. a long line of dominoes standing in a dark room with one slightly out of alignment, close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Và Light khi mất trí nhớ là một người hoàn toàn khác: chính trực, tận tâm, muốn bắt Kira thật lòng. Nhiều ngư…

```text
Wide 16:9 landscape cinematic frame. a young man working late at a desk with case files, a genuine determined expression, medium shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy đây là nước cờ đỉnh cao nhất của Light. Và cũng đáng sợ nhất: một người sẵn sàng xóa chính mình để…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a chess board with wide eyes, feathers slightly ruffled. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Cách phá 4: luật giả

Lời: Nhưng nước cờ của Light chưa dừng ở đó. Cậu nhờ Ryuk viết thêm hai luật giả vào cuốn sổ.

```text
Wide 16:9 landscape cinematic frame. a notebook's rule page with two new lines written in slightly different ink, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Luật giả một: nếu người dùng không viết tên ai trong mười ba ngày liên tiếp, người dùng sẽ chết. Luật giả hai…

```text
Wide 16:9 landscape cinematic frame. two rule lines on a page circled in red with a large question mark stamp beside them, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Mục đích: Light đã bị giam hơn năm mươi ngày mà không chết, nên theo luật giả, cậu không thể là Kira. Và khôn…

```text
Wide 16:9 landscape cinematic frame. a calendar with more than fifty days crossed out beside a small cleared stamp, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Đây là cách phá tinh vi nhất: không phá luật thật, mà viết thêm luật giả để người khác tin. Luật trở thành mộ…

```text
Wide 16:9 landscape cinematic frame. a forged document being placed on top of a real one, close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Cái giá: luật giả có thể bị lật. Và cuối cùng, chính việc kiểm tra luật giả là một trong những mắt xích dẫn t…

```text
Wide 16:9 landscape cinematic frame. a thread being pulled from a woven cloth, starting to unravel it, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Cuốn sổ thứ hai

Lời: Một chi tiết nhiều người quên: Ryuk có hai cuốn sổ. Hắn đã lừa vua thần chết để có thêm một cuốn, rồi thả một…

```text
Wide 16:9 landscape cinematic frame. two identical black notebooks, one falling from the sky and one resting on a stone ledge in a grey desolate realm, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Và rồi xuất hiện một Kira thứ hai, với một cuốn sổ khác, của một thần chết khác. Đó là Misa, cùng thần chết R…

```text
Wide 16:9 landscape cinematic frame. a second notebook lying on a vanity table beside a small mirror, close-up, dramatic cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Hai cuốn sổ nghĩa là luật chơi thay đổi. Light có thể chuyển sổ qua lại, giấu sổ ở nhiều nơi, và dùng người k…

```text
Wide 16:9 landscape cinematic frame. two notebooks being passed between two hands across a table, close-up, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: mỗi lần số cuốn sổ tăng, trận đấu trí càng khó đoán. Ở arc cuối, số người biết về cuốn sổ nhiều tớ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at several identical notebooks on a table, trying to tell them apart. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Luật 4: mắt thần chết

Lời: Luật đáng sợ nhất: con người có thể đổi một nửa tuổi thọ còn lại để có đôi mắt thần chết. Với đôi mắt đó, chỉ…

```text
Wide 16:9 landscape cinematic frame. an eye in extreme close-up with faint glowing text reflected in the iris, dramatic red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Đôi mắt này phá được tấm khiên của L: không cần biết tên, chỉ cần nhìn thấy mặt.

```text
Wide 16:9 landscape cinematic frame. a crowd of faces with faint floating names above each head, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Light từ chối đổi mắt, vì cậu muốn sống lâu để cai trị thế giới mới. Nhưng Misa, người ngưỡng mộ Kira, đã đổi…

```text
Wide 16:9 landscape cinematic frame. a young woman with a determined expression looking into a mirror, a faint red glow in her eyes, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cái giá: Misa mất ba phần tư tuổi thọ còn lại, vì Light. Đây là một trong những cái giá đau lòng nhất truyện,…

```text
Wide 16:9 landscape cinematic frame. an hourglass with only a thin stream of sand left falling, close-up, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Luật 5: thần chết cũng có luật

Lời: Thần chết cũng bị ràng buộc bởi luật. Luật quan trọng nhất: nếu một thần chết dùng sổ để giết ai đó nhằm kéo…

```text
Wide 16:9 landscape cinematic frame. a tall winged silhouette crumbling into sand in a desolate landscape, wide shot, somber grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Rem, thần chết đi theo Misa, yêu thương Misa. Light hiểu luật này, và cố ý dồn Rem vào thế phải chọn: để L ph…

```text
Wide 16:9 landscape cinematic frame. a chess board where a single large piece is cornered by several smaller pieces, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Rem chọn cứu Misa. L chết. Rem cũng tan thành cát bụi. Light thắng mà không cần tự tay viết một chữ nào.

```text
Wide 16:9 landscape cinematic frame. a single empty chair in front of a wall of monitors in a dark room, wide shot, quiet somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: L có linh cảm trước. Trong một cảnh mưa nổi tiếng, L nói với Light rằng mình nghe thấy tiếng chuông, và lau c…

```text
Wide 16:9 landscape cinematic frame. two figures standing on a rooftop in heavy rain, one gazing up at the sky, wide shot, melancholy grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Kaku thấy đây là cách phá luật lạnh lùng nhất: không phá luật, mà dùng chính luật để buộc người khác hy sinh.…

```text
Wide 16:9 landscape cinematic frame. a pair of hands carefully arranging dominoes so that they will fall toward a distant target, close-up, cold calculating light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Cách phá cuối: đổi cuốn sổ

Lời: Near và Mello là hai mặt của L: một người điềm tĩnh, logic, ngồi xếp đồ chơi khi suy nghĩ; một người liều lĩn…

```text
Wide 16:9 landscape cinematic frame. two contrasting workspaces side by side: one neat with puzzle pieces on a white floor, one chaotic with maps and a motorcycle helmet, wide shot, split cool and warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Sau L, những người kế nhiệm là Near và Mello. Họ hiểu một điều: đánh Kira bằng luật thì Kira luôn đi trước mộ…

```text
Wide 16:9 landscape cinematic frame. a set of toy figures and puzzle pieces spread across a white floor with a single notebook among them, top-down shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Trong trận cuối, người giúp việc cho Kira là Mikami mang theo cuốn sổ. Nhóm của Near đã bí mật thay nó bằng m…

```text
Wide 16:9 landscape cinematic frame. two identical black notebooks side by side on a table, one with a tiny hidden mark on its corner, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Khi Mikami viết tên tất cả mọi người trong phòng, không ai chết. Và tên duy nhất không được viết trên trang đ…

```text
Wide 16:9 landscape cinematic frame. a notebook page filled with names in hurried handwriting with one conspicuous blank space, extreme close-up, cold stark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Cuối cùng, Light, người phá mọi luật, bị đánh bại bằng một cách không liên quan tới luật: một cuốn sổ giả. Mộ…

```text
Wide 16:9 landscape cinematic frame. a simple paper decoy on a table under a spotlight, close-up, ironic dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Và theo đúng lời Ryuk nói từ đầu truyện, khi mọi thứ kết thúc, Ryuk là người viết tên Light vào cuốn sổ của m…

```text
Wide 16:9 landscape cinematic frame. a lone winged silhouette sitting on a high rooftop at sunset, writing in a notebook, wide shot, bittersweet orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Kaku để ý: ngay từ đầu, Ryuk đã nói với Light rằng người dùng sổ sẽ không có kết cục tốt. Luật đó không được…

```text
Wide 16:9 landscape cinematic frame. an old handwritten note tucked into the back cover of a black notebook, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · Bảng luật và cách phá

Lời: Tổng kết. Luật tên và khuôn mặt: bị phá bằng đôi mắt thần chết, và được chống bằng cách giấu tên. Luật điều k…

```text
Wide 16:9 landscape cinematic frame. a two-column chart on parchment with rules on the left and methods on the right, first two rows filled, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Luật mảnh giấy: giấu trong đồng hồ. Luật quyền sở hữu: tự quên mình là Kira. Luật giả: tự minh oan.

```text
Wide 16:9 landscape cinematic frame. the chart with three more rows filled with small doodles of a watch, a fading brain and a forged page, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Luật thần chết: dồn Rem vào lựa chọn. Và cách phá cuối cùng, không qua luật nào: một cuốn sổ giả.

```text
Wide 16:9 landscape cinematic frame. the chart completed with a final row and a small gold star beside the fake notebook entry, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nếu phải chọn một cách phá hay nhất, Kaku chọn cuốn sổ giả. Vì nó nhắc rằng một kế hoạch hoàn hảo tới đâu cũn…

```text
Wide 16:9 landscape cinematic frame. a single loose link in a long metal chain, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Và cột cái giá: kiêu ngạo, không bao giờ được nghỉ ngơi, đánh cược cả bản thân, tuổi thọ của Misa, sự hy sinh…

```text
Wide 16:9 landscape cinematic frame. a long column of small price tags hanging from a single thread on the chart, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Góc nhìn của Kaku

Lời: Death Note hay vì nó biến một năng lực siêu nhiên thành một bài toán logic. Nhưng Kaku nghĩ nó hay hơn nữa vì…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a notebook on one side and a gavel on the other, close-up, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Light bắt đầu với ý định trừng phạt kẻ ác. Nhưng để bảo vệ quyền làm điều đó, cậu giết cả những người vô tội…

```text
Wide 16:9 landscape cinematic frame. a figure's shadow on a wall slowly growing larger and darker than the figure itself, symbolic close-up, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Trò chơi nhỏ: nếu bạn là L, bạn sẽ làm gì đầu tiên để tìm Kira? Và nếu bạn là Kira, bạn sẽ phạm sai lầm đầu t…

```text
Wide 16:9 landscape cinematic frame. two blank index cards side by side on a desk, one marked with a letter and one with a notebook doodle, close-up, cold lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và câu hỏi dành cho bạn: có ai xứng đáng được nắm trong tay quyền quyết định sống chết của người khác không?…

```text
Wide 16:9 landscape cinematic frame. the owl mascot slowly closing a black notebook and pushing it away across the table. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Bạn thích nước cờ nào nhất trong Death Note? Mảnh giấy trong đồng hồ, tự quên mình là Kira, hay cuốn sổ giả c…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with tiny doodles of a watch, a brain and a notebook, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku chuyển sang một cuốn sổ vui hơn nhiều: Doraemon, và câu hỏi bảo bối nào có thể làm được…

```text
Wide 16:9 landscape cinematic frame. a round blue-and-white pocket-like pouch doodle beside a science notebook, close-up, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những video mổ xẻ luật chơi như thế này, hãy đăng ký kênh. Và nếu một ngày nhặt được cuốn sổ đe…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving goodbye while stepping carefully around a black notebook on the ground. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Bối cảnh: Death Note là gì?

Khoảng 142 giây · cảnh s01–s12 · 1849 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói về toàn bộ Death Note, kể cả cái kết. Nếu bạn chưa xem, hãy lưu video lại. Đây là một trong những bộ anime nên xem ít nhất một lần.

<short pause> Một cuốn sổ đen rơi từ trên trời xuống sân trường. Trên bìa ghi hai chữ. Và bên trong là một danh sách luật lệ, viết bằng tiếng Anh, giống như hướng dẫn sử dụng.

<short pause> Luật đầu tiên: người bị ghi tên vào sổ sẽ chết. Chỉ vậy thôi. <short pause> Nhưng từ một luật đơn giản đó, Death Note xây nên một trong những cuộc đấu trí nổi tiếng nhất lịch sử anime.

<short pause> Vì cuốn sổ không chỉ có một luật. Nó có rất nhiều luật, và người thắng không phải người mạnh nhất, mà là người hiểu luật và tìm ra kẽ hở giỏi nhất.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở cuốn sổ đáng sợ nhất anime: luật của nó, những cách các nhân vật đã phá luật, và cái giá của mỗi cách. Cuối video là bảng luật và cách phá.

<short pause> Kaku nói rõ: đây là truyện hư cấu. Video phân tích luật chơi và chiến thuật trong truyện, không cổ vũ bạo lực, và không mô tả chi tiết cái chết.

<short pause> Death Note là manga của Ohba Tsugumi viết truyện và Obata Takeshi vẽ, đăng từ tháng mười hai năm 2003 tới tháng năm năm 2006, gồm một trăm lẻ tám chương. Anime do Madhouse làm, phát năm 2006.

<short pause> Nhân vật chính là Yagami Light, một học sinh xuất sắc. Cậu nhặt được cuốn sổ, thử nghiệm nó, và phát hiện nó hoạt động thật.

<short pause> Light quyết định dùng cuốn sổ để trừng phạt tội phạm, và tạo ra một thế giới mới không còn cái ác. Người ta gọi cậu là Kira.

<short pause> Cuốn sổ thuộc về Ryuk, một thần chết thấy thế giới thần chết quá nhàm chán nên cố tình thả sổ xuống nhân gian để xem chuyện gì xảy ra.

<short pause> Đối thủ của Light là L, thám tử bí ẩn giỏi nhất thế giới, không ai biết mặt, không ai biết tên thật. Và trong một thế giới mà biết tên là giết được, không có tên chính là tấm khiên.

<short pause> Kaku để ý: Death Note là trận đấu giữa hai người đều thông minh, và cả hai đều đọc cùng một cuốn luật. Ai đọc kỹ hơn thì thắng.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói về toàn bộ Death Note, kể cả cái kết. Nếu bạn chưa xem, hãy lưu video lại. Đây là một trong những bộ anime nên xem ít nhất một lần.

[pause] Một cuốn sổ đen rơi từ trên trời xuống sân trường. Trên bìa ghi hai chữ. Và bên trong là một danh sách luật lệ, viết bằng tiếng Anh, giống như hướng dẫn sử dụng.

[pause] Luật đầu tiên: người bị ghi tên vào sổ sẽ chết. Chỉ vậy thôi. [pause] Nhưng từ một luật đơn giản đó, Death Note xây nên một trong những cuộc đấu trí nổi tiếng nhất lịch sử anime.

[pause] Vì cuốn sổ không chỉ có một luật. Nó có rất nhiều luật, và người thắng không phải người mạnh nhất, mà là người hiểu luật và tìm ra kẽ hở giỏi nhất.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở cuốn sổ đáng sợ nhất anime: luật của nó, những cách các nhân vật đã phá luật, và cái giá của mỗi cách. Cuối video là bảng luật và cách phá.

[pause] Kaku nói rõ: đây là truyện hư cấu. Video phân tích luật chơi và chiến thuật trong truyện, không cổ vũ bạo lực, và không mô tả chi tiết cái chết.

[pause] Death Note là manga của Ohba Tsugumi viết truyện và Obata Takeshi vẽ, đăng từ tháng mười hai năm 2003 tới tháng năm năm 2006, gồm một trăm lẻ tám chương. Anime do Madhouse làm, phát năm 2006.

[pause] Nhân vật chính là Yagami Light, một học sinh xuất sắc. Cậu nhặt được cuốn sổ, thử nghiệm nó, và phát hiện nó hoạt động thật.

[pause] Light quyết định dùng cuốn sổ để trừng phạt tội phạm, và tạo ra một thế giới mới không còn cái ác. Người ta gọi cậu là Kira.

[pause] Cuốn sổ thuộc về Ryuk, một thần chết thấy thế giới thần chết quá nhàm chán nên cố tình thả sổ xuống nhân gian để xem chuyện gì xảy ra.

[pause] Đối thủ của Light là L, thám tử bí ẩn giỏi nhất thế giới, không ai biết mặt, không ai biết tên thật. Và trong một thế giới mà biết tên là giết được, không có tên chính là tấm khiên.

[pause] Kaku để ý: Death Note là trận đấu giữa hai người đều thông minh, và cả hai đều đọc cùng một cuốn luật. Ai đọc kỹ hơn thì thắng.
```

### c02 · Luật 1: tên và khuôn mặt / Luật 2: bốn mươi giây và sáu phút bốn mươi giây

Khoảng 105 giây · cảnh s13–s22 · 1370 ký tự

**Gemini**

```text
Luật đầu tiên đầy đủ: người bị ghi tên sẽ chết. <short pause> Nhưng người viết phải nghĩ tới khuôn mặt của người đó khi viết. Vì vậy những người trùng tên không bị ảnh hưởng.

<short pause> Nghĩa là để giết ai, Light cần hai thứ: tên thật và khuôn mặt. Và đây chính là điểm yếu mà L khai thác: giấu cả hai.

<short pause> Cách phá của phía L: không bao giờ xuất hiện trước công chúng, dùng bí danh, và nói chuyện qua một màn hình chỉ có một chữ cái.

<short pause> Sau này, L còn dùng cả còng tay để tự khóa mình với Light suốt nhiều tuần, để theo dõi từng hành động. Để bảo vệ tên thật, L chấp nhận không còn một giây riêng tư.

<short pause> Cái giá của cách phá này: L phải sống ẩn dật hoàn toàn. Không bạn bè, không đời sống bình thường, không thể tin ai.

<short pause> Nghe thì chỉ là thủ tục, nhưng những con số này cho thấy tác giả thiết kế cuốn sổ như một bộ luật thật, có thời hạn, có điều kiện, có ngoại lệ. Và luật càng chi tiết thì kẽ hở càng nhiều.

<short pause> Luật hai: nếu ghi nguyên nhân cái chết trong vòng bốn mươi giây sau khi viết tên, nó sẽ xảy ra. Nếu không ghi, người đó chết vì đau tim.

<short pause> Luật ba: sau khi ghi nguyên nhân, người viết có thêm sáu phút bốn mươi giây để ghi chi tiết hoàn cảnh.

<short pause> Và luật bốn: người viết có thể điều khiển hành động của nạn nhân trước khi chết, trong giới hạn khoảng hai mươi ba ngày, và chỉ những việc người đó có thể làm được.

<short pause> Nghe như những con số khô khan. <short pause> Nhưng chính luật điều khiển hành động là vũ khí mạnh nhất của Light.
```

**ElevenLabs**

```text
Luật đầu tiên đầy đủ: người bị ghi tên sẽ chết. [pause] Nhưng người viết phải nghĩ tới khuôn mặt của người đó khi viết. Vì vậy những người trùng tên không bị ảnh hưởng.

[pause] Nghĩa là để giết ai, Light cần hai thứ: tên thật và khuôn mặt. Và đây chính là điểm yếu mà L khai thác: giấu cả hai.

[pause] Cách phá của phía L: không bao giờ xuất hiện trước công chúng, dùng bí danh, và nói chuyện qua một màn hình chỉ có một chữ cái.

[pause] Sau này, L còn dùng cả còng tay để tự khóa mình với Light suốt nhiều tuần, để theo dõi từng hành động. Để bảo vệ tên thật, L chấp nhận không còn một giây riêng tư.

[pause] Cái giá của cách phá này: L phải sống ẩn dật hoàn toàn. Không bạn bè, không đời sống bình thường, không thể tin ai.

[pause] Nghe thì chỉ là thủ tục, nhưng những con số này cho thấy tác giả thiết kế cuốn sổ như một bộ luật thật, có thời hạn, có điều kiện, có ngoại lệ. Và luật càng chi tiết thì kẽ hở càng nhiều.

[pause] Luật hai: nếu ghi nguyên nhân cái chết trong vòng bốn mươi giây sau khi viết tên, nó sẽ xảy ra. Nếu không ghi, người đó chết vì đau tim.

[pause] Luật ba: sau khi ghi nguyên nhân, người viết có thêm sáu phút bốn mươi giây để ghi chi tiết hoàn cảnh.

[pause] Và luật bốn: người viết có thể điều khiển hành động của nạn nhân trước khi chết, trong giới hạn khoảng hai mươi ba ngày, và chỉ những việc người đó có thể làm được.

[pause] Nghe như những con số khô khan. [pause] Nhưng chính luật điều khiển hành động là vũ khí mạnh nhất của Light.
```

### c03 · Cách phá 1: thí nghiệm bằng hành động / Nước cờ của L

Khoảng 106 giây · cảnh s23–s32 · 1382 ký tự

**Gemini**

```text
Light dùng luật điều khiển hành động để thí nghiệm, rồi để gửi thông điệp. Cậu khiến một số tội phạm trong tù viết những lá thư trước khi chết. Ghép chữ đầu lại, thành một câu gửi cho L.

<short pause> Câu đó, đại ý: L, ông có biết thần chết chỉ ăn táo không? Đó là một lời trêu chọc, nhưng cũng là một lần Light để lộ quá nhiều.

<short pause> Vì qua đó, L suy ra Kira có thể điều khiển hành động của nạn nhân trước khi chết. Mỗi thí nghiệm của Light cũng là một manh mối cho L.

<short pause> Light từng giết một nhóm đặc vụ đang theo dõi mình bằng một kế hoạch điều khiển hành động phức tạp. <short pause> Nhưng cũng chính vụ đó khiến L thu hẹp danh sách nghi phạm.

<short pause> Cái giá: kiêu ngạo. Light thích thể hiện, và mỗi lần thể hiện là một lần để lại dấu vết.

<short pause> Giờ tới phía bên kia bàn cờ. L cũng không đọc luật, vì L không có cuốn sổ. L phải đoán luật từ những gì Kira làm.

<short pause> Nước cờ đầu tiên của L: cho một người đóng thế xuất hiện trên truyền hình, tự xưng là L, thách thức Kira. Kira giết người đó ngay lập tức.

<short pause> Nhưng chương trình chỉ được phát ở một khu vực. Nhờ đó, L biết Kira đang ở vùng Kanto, Nhật Bản, và biết Kira cần nhìn thấy mặt để giết.

<short pause> Cách này cho thấy L phá luật kiểu khác: không lách luật, mà dùng hành động của Kira để vẽ lại luật. Mỗi vụ giết người là một dữ kiện.

<short pause> Và L còn làm một điều không ai ngờ: tự giới thiệu mình là L với chính Light, người L nghi ngờ nhất. Một nước cờ đặt chính mạng mình lên bàn để thử phản ứng của đối thủ.
```

**ElevenLabs**

```text
Light dùng luật điều khiển hành động để thí nghiệm, rồi để gửi thông điệp. Cậu khiến một số tội phạm trong tù viết những lá thư trước khi chết. Ghép chữ đầu lại, thành một câu gửi cho L.

[pause] [curious] Câu đó, đại ý: L, ông có biết thần chết chỉ ăn táo không? Đó là một lời trêu chọc, nhưng cũng là một lần Light để lộ quá nhiều.

[pause] Vì qua đó, L suy ra Kira có thể điều khiển hành động của nạn nhân trước khi chết. Mỗi thí nghiệm của Light cũng là một manh mối cho L.

[pause] Light từng giết một nhóm đặc vụ đang theo dõi mình bằng một kế hoạch điều khiển hành động phức tạp. [pause] Nhưng cũng chính vụ đó khiến L thu hẹp danh sách nghi phạm.

[pause] Cái giá: kiêu ngạo. Light thích thể hiện, và mỗi lần thể hiện là một lần để lại dấu vết.

[pause] Giờ tới phía bên kia bàn cờ. L cũng không đọc luật, vì L không có cuốn sổ. L phải đoán luật từ những gì Kira làm.

[pause] Nước cờ đầu tiên của L: cho một người đóng thế xuất hiện trên truyền hình, tự xưng là L, thách thức Kira. Kira giết người đó ngay lập tức.

[pause] Nhưng chương trình chỉ được phát ở một khu vực. Nhờ đó, L biết Kira đang ở vùng Kanto, Nhật Bản, và biết Kira cần nhìn thấy mặt để giết.

[pause] Cách này cho thấy L phá luật kiểu khác: không lách luật, mà dùng hành động của Kira để vẽ lại luật. Mỗi vụ giết người là một dữ kiện.

[pause] Và L còn làm một điều không ai ngờ: tự giới thiệu mình là L với chính Light, người L nghi ngờ nhất. Một nước cờ đặt chính mạng mình lên bàn để thử phản ứng của đối thủ.
```

### c04 · Cách phá 2: mảnh giấy xé ra / Luật 3: quyền sở hữu và ký ức / Cách phá 3: tự quên mình là Kira

Khoảng 145 giây · cảnh s33–s46 · 1886 ký tự

**Gemini**

```text
Một luật khác: một mảnh giấy xé ra từ cuốn sổ vẫn có hiệu lực y hệt cuốn sổ. Chỉ cần viết tên lên mảnh đó.

<short pause> Light lợi dụng điều này để giấu những mảnh giấy khắp nơi. Nổi tiếng nhất là một mảnh giấu trong đồng hồ đeo tay, có ngăn bí mật mở ra khi kéo núm vặn đúng cách.

<short pause> Nhờ vậy, Light có thể giết người ngay cả khi bị theo dõi, ngay cả khi không cầm cuốn sổ. Cách phá này biến cuốn sổ thành một vũ khí có thể mang theo mọi lúc.

<short pause> Light còn giấu cuốn sổ trong ngăn kéo có đáy giả, gài một cơ chế tự đốt nếu có người mở sai cách. Một cuốn sổ, và một hệ thống bảo vệ như két sắt.

<short pause> Cái giá: Light không bao giờ có thể buông cuốn sổ ra, dù chỉ trong tâm trí. Cậu phải luôn tính toán, luôn đề phòng. Cuộc sống bình thường biến mất.

<short pause> Luật tiếp theo, rất quan trọng: người chạm vào cuốn sổ sẽ nhìn thấy thần chết. Và nếu người sở hữu từ bỏ quyền sở hữu, họ sẽ mất toàn bộ ký ức liên quan tới cuốn sổ.

<short pause> Nghe như một bất lợi. <short pause> Nhưng Light biến nó thành cách phá luật táo bạo nhất trong truyện.

<short pause> Khi bị L nghi ngờ, Light tự nguyện bị giam giữ. Rồi cậu từ bỏ quyền sở hữu cuốn sổ, và quên sạch mọi thứ. Light lúc đó thật sự tin mình không phải Kira.

<short pause> L giam Light nhiều tuần, theo dõi từng phút. <short pause> Nhưng người L theo dõi là một Light vô tội. Không có gì để phát hiện.

<short pause> Trong lúc đó, cuốn sổ được chuyển cho một người khác, và các vụ giết người tiếp tục. Light được thả, và thậm chí cùng L điều tra Kira mới.

<short pause> Và rồi, theo kế hoạch Light đã sắp đặt từ trước khi quên, cậu chạm lại vào cuốn sổ, và toàn bộ ký ức ùa về.

<short pause> Cái giá: Light đánh cược tất cả vào một kế hoạch mà chính cậu không nhớ. Nếu có một mắt xích sai, cậu sẽ mất cuốn sổ mãi mãi.

<short pause> Và Light khi mất trí nhớ là một người hoàn toàn khác: chính trực, tận tâm, muốn bắt Kira thật lòng. Nhiều người xem nói đó là Light mà họ ước cậu đã có thể trở thành.

<short pause> <laugh> Kaku thấy đây là nước cờ đỉnh cao nhất của Light. Và cũng đáng sợ nhất: một người sẵn sàng xóa chính mình để thắng.
```

**ElevenLabs**

```text
Một luật khác: một mảnh giấy xé ra từ cuốn sổ vẫn có hiệu lực y hệt cuốn sổ. Chỉ cần viết tên lên mảnh đó.

[pause] Light lợi dụng điều này để giấu những mảnh giấy khắp nơi. Nổi tiếng nhất là một mảnh giấu trong đồng hồ đeo tay, có ngăn bí mật mở ra khi kéo núm vặn đúng cách.

[pause] Nhờ vậy, Light có thể giết người ngay cả khi bị theo dõi, ngay cả khi không cầm cuốn sổ. Cách phá này biến cuốn sổ thành một vũ khí có thể mang theo mọi lúc.

[pause] Light còn giấu cuốn sổ trong ngăn kéo có đáy giả, gài một cơ chế tự đốt nếu có người mở sai cách. Một cuốn sổ, và một hệ thống bảo vệ như két sắt.

[pause] Cái giá: Light không bao giờ có thể buông cuốn sổ ra, dù chỉ trong tâm trí. Cậu phải luôn tính toán, luôn đề phòng. Cuộc sống bình thường biến mất.

[pause] Luật tiếp theo, rất quan trọng: người chạm vào cuốn sổ sẽ nhìn thấy thần chết. Và nếu người sở hữu từ bỏ quyền sở hữu, họ sẽ mất toàn bộ ký ức liên quan tới cuốn sổ.

[pause] Nghe như một bất lợi. [pause] Nhưng Light biến nó thành cách phá luật táo bạo nhất trong truyện.

[pause] Khi bị L nghi ngờ, Light tự nguyện bị giam giữ. Rồi cậu từ bỏ quyền sở hữu cuốn sổ, và quên sạch mọi thứ. Light lúc đó thật sự tin mình không phải Kira.

[pause] L giam Light nhiều tuần, theo dõi từng phút. [pause] Nhưng người L theo dõi là một Light vô tội. Không có gì để phát hiện.

[pause] Trong lúc đó, cuốn sổ được chuyển cho một người khác, và các vụ giết người tiếp tục. Light được thả, và thậm chí cùng L điều tra Kira mới.

[pause] Và rồi, theo kế hoạch Light đã sắp đặt từ trước khi quên, cậu chạm lại vào cuốn sổ, và toàn bộ ký ức ùa về.

[pause] Cái giá: Light đánh cược tất cả vào một kế hoạch mà chính cậu không nhớ. Nếu có một mắt xích sai, cậu sẽ mất cuốn sổ mãi mãi.

[pause] Và Light khi mất trí nhớ là một người hoàn toàn khác: chính trực, tận tâm, muốn bắt Kira thật lòng. Nhiều người xem nói đó là Light mà họ ước cậu đã có thể trở thành.

[pause] [chuckles] Kaku thấy đây là nước cờ đỉnh cao nhất của Light. Và cũng đáng sợ nhất: một người sẵn sàng xóa chính mình để thắng.
```

### c05 · Cách phá 4: luật giả / Cuốn sổ thứ hai / Luật 4: mắt thần chết

Khoảng 132 giây · cảnh s47–s59 · 1710 ký tự

**Gemini**

```text
Nhưng nước cờ của Light chưa dừng ở đó. Cậu nhờ Ryuk viết thêm hai luật giả vào cuốn sổ.

<short pause> Luật giả một: nếu người dùng không viết tên ai trong mười ba ngày liên tiếp, người dùng sẽ chết. Luật giả hai: nếu cuốn sổ bị phá hủy, mọi người đã chạm vào nó sẽ chết.

<short pause> Mục đích: Light đã bị giam hơn năm mươi ngày mà không chết, nên theo luật giả, cậu không thể là Kira. Và không ai dám phá cuốn sổ để thử.

<short pause> Đây là cách phá tinh vi nhất: không phá luật thật, mà viết thêm luật giả để người khác tin. Luật trở thành một công cụ nói dối.

<short pause> Cái giá: luật giả có thể bị lật. Và cuối cùng, chính việc kiểm tra luật giả là một trong những mắt xích dẫn tới sự thật.

<short pause> Một chi tiết nhiều người quên: Ryuk có hai cuốn sổ. Hắn đã lừa vua thần chết để có thêm một cuốn, rồi thả một cuốn xuống nhân gian.

<short pause> Và rồi xuất hiện một Kira thứ hai, với một cuốn sổ khác, của một thần chết khác. Đó là Misa, cùng thần chết Rem.

<short pause> Hai cuốn sổ nghĩa là luật chơi thay đổi. Light có thể chuyển sổ qua lại, giấu sổ ở nhiều nơi, và dùng người khác làm cánh tay của mình.

<short pause> <laugh> Kaku để ý: mỗi lần số cuốn sổ tăng, trận đấu trí càng khó đoán. Ở arc cuối, số người biết về cuốn sổ nhiều tới mức ai cũng có thể là quân cờ của ai.

<short pause> Luật đáng sợ nhất: con người có thể đổi một nửa tuổi thọ còn lại để có đôi mắt thần chết. Với đôi mắt đó, chỉ cần nhìn mặt là thấy tên thật và tuổi thọ của bất kỳ ai.

<short pause> Đôi mắt này phá được tấm khiên của L: không cần biết tên, chỉ cần nhìn thấy mặt.

<short pause> Light từ chối đổi mắt, vì cậu muốn sống lâu để cai trị thế giới mới. <short pause> Nhưng Misa, người ngưỡng mộ Kira, đã đổi. Và đổi tới hai lần.

<short pause> Cái giá: Misa mất ba phần tư tuổi thọ còn lại, vì Light. Đây là một trong những cái giá đau lòng nhất truyện, và nó cho thấy Light sẵn sàng dùng người khác làm công cụ.
```

**ElevenLabs**

```text
Nhưng nước cờ của Light chưa dừng ở đó. Cậu nhờ Ryuk viết thêm hai luật giả vào cuốn sổ.

[pause] Luật giả một: nếu người dùng không viết tên ai trong mười ba ngày liên tiếp, người dùng sẽ chết. Luật giả hai: nếu cuốn sổ bị phá hủy, mọi người đã chạm vào nó sẽ chết.

[pause] Mục đích: Light đã bị giam hơn năm mươi ngày mà không chết, nên theo luật giả, cậu không thể là Kira. Và không ai dám phá cuốn sổ để thử.

[pause] Đây là cách phá tinh vi nhất: không phá luật thật, mà viết thêm luật giả để người khác tin. Luật trở thành một công cụ nói dối.

[pause] Cái giá: luật giả có thể bị lật. Và cuối cùng, chính việc kiểm tra luật giả là một trong những mắt xích dẫn tới sự thật.

[pause] Một chi tiết nhiều người quên: Ryuk có hai cuốn sổ. Hắn đã lừa vua thần chết để có thêm một cuốn, rồi thả một cuốn xuống nhân gian.

[pause] Và rồi xuất hiện một Kira thứ hai, với một cuốn sổ khác, của một thần chết khác. Đó là Misa, cùng thần chết Rem.

[pause] Hai cuốn sổ nghĩa là luật chơi thay đổi. Light có thể chuyển sổ qua lại, giấu sổ ở nhiều nơi, và dùng người khác làm cánh tay của mình.

[pause] [chuckles] Kaku để ý: mỗi lần số cuốn sổ tăng, trận đấu trí càng khó đoán. Ở arc cuối, số người biết về cuốn sổ nhiều tới mức ai cũng có thể là quân cờ của ai.

[pause] Luật đáng sợ nhất: con người có thể đổi một nửa tuổi thọ còn lại để có đôi mắt thần chết. Với đôi mắt đó, chỉ cần nhìn mặt là thấy tên thật và tuổi thọ của bất kỳ ai.

[pause] Đôi mắt này phá được tấm khiên của L: không cần biết tên, chỉ cần nhìn thấy mặt.

[pause] Light từ chối đổi mắt, vì cậu muốn sống lâu để cai trị thế giới mới. [pause] Nhưng Misa, người ngưỡng mộ Kira, đã đổi. Và đổi tới hai lần.

[pause] Cái giá: Misa mất ba phần tư tuổi thọ còn lại, vì Light. Đây là một trong những cái giá đau lòng nhất truyện, và nó cho thấy Light sẵn sàng dùng người khác làm công cụ.
```

### c06 · Luật 5: thần chết cũng có luật / Cách phá cuối: đổi cuốn sổ

Khoảng 134 giây · cảnh s60–s71 · 1737 ký tự

**Gemini**

```text
Thần chết cũng bị ràng buộc bởi luật. Luật quan trọng nhất: nếu một thần chết dùng sổ để giết ai đó nhằm kéo dài sự sống của người mình yêu, thần chết đó sẽ chết.

<short pause> Rem, thần chết đi theo Misa, yêu thương Misa. Light hiểu luật này, và cố ý dồn Rem vào thế phải chọn: để L phát hiện Misa, hoặc giết L và chết.

<short pause> Rem chọn cứu Misa. L chết. Rem cũng tan thành cát bụi. Light thắng mà không cần tự tay viết một chữ nào.

<short pause> L có linh cảm trước. Trong một cảnh mưa nổi tiếng, L nói với Light rằng mình nghe thấy tiếng chuông, và lau chân cho Light như một lời từ biệt không nói thành lời.

<short pause> Kaku thấy đây là cách phá luật lạnh lùng nhất: không phá luật, mà dùng chính luật để buộc người khác hy sinh. Và nó cũng là khoảnh khắc Light trở nên đáng sợ nhất.

<short pause> Near và Mello là hai mặt của L: một người điềm tĩnh, logic, ngồi xếp đồ chơi khi suy nghĩ; một người liều lĩnh, sẵn sàng làm mọi cách. Cuối cùng, họ cần nhau để thắng.

<short pause> Sau L, những người kế nhiệm là Near và Mello. Họ hiểu một điều: đánh Kira bằng luật thì Kira luôn đi trước một bước. Vậy phải đánh vào chính cuốn sổ.

<short pause> Trong trận cuối, người giúp việc cho Kira là Mikami mang theo cuốn sổ. Nhóm của Near đã bí mật thay nó bằng một cuốn sổ giả, trông giống hệt.

<short pause> Khi Mikami viết tên tất cả mọi người trong phòng, không ai chết. Và tên duy nhất không được viết trên trang đó là Yagami Light.

<short pause> Cuối cùng, Light, người phá mọi luật, bị đánh bại bằng một cách không liên quan tới luật: một cuốn sổ giả. Một mánh khóe đơn giản nhất lại hạ kẻ tinh vi nhất.

<short pause> Và theo đúng lời Ryuk nói từ đầu truyện, khi mọi thứ kết thúc, Ryuk là người viết tên Light vào cuốn sổ của mình.

<short pause> Kaku để ý: ngay từ đầu, Ryuk đã nói với Light rằng người dùng sổ sẽ không có kết cục tốt. Luật đó không được viết trong sổ, nhưng nó đúng tới cuối.
```

**ElevenLabs**

```text
Thần chết cũng bị ràng buộc bởi luật. Luật quan trọng nhất: nếu một thần chết dùng sổ để giết ai đó nhằm kéo dài sự sống của người mình yêu, thần chết đó sẽ chết.

[pause] Rem, thần chết đi theo Misa, yêu thương Misa. Light hiểu luật này, và cố ý dồn Rem vào thế phải chọn: để L phát hiện Misa, hoặc giết L và chết.

[pause] Rem chọn cứu Misa. L chết. Rem cũng tan thành cát bụi. Light thắng mà không cần tự tay viết một chữ nào.

[pause] L có linh cảm trước. Trong một cảnh mưa nổi tiếng, L nói với Light rằng mình nghe thấy tiếng chuông, và lau chân cho Light như một lời từ biệt không nói thành lời.

[pause] Kaku thấy đây là cách phá luật lạnh lùng nhất: không phá luật, mà dùng chính luật để buộc người khác hy sinh. Và nó cũng là khoảnh khắc Light trở nên đáng sợ nhất.

[pause] Near và Mello là hai mặt của L: một người điềm tĩnh, logic, ngồi xếp đồ chơi khi suy nghĩ; một người liều lĩnh, sẵn sàng làm mọi cách. Cuối cùng, họ cần nhau để thắng.

[pause] Sau L, những người kế nhiệm là Near và Mello. Họ hiểu một điều: đánh Kira bằng luật thì Kira luôn đi trước một bước. Vậy phải đánh vào chính cuốn sổ.

[pause] Trong trận cuối, người giúp việc cho Kira là Mikami mang theo cuốn sổ. Nhóm của Near đã bí mật thay nó bằng một cuốn sổ giả, trông giống hệt.

[pause] Khi Mikami viết tên tất cả mọi người trong phòng, không ai chết. Và tên duy nhất không được viết trên trang đó là Yagami Light.

[pause] Cuối cùng, Light, người phá mọi luật, bị đánh bại bằng một cách không liên quan tới luật: một cuốn sổ giả. Một mánh khóe đơn giản nhất lại hạ kẻ tinh vi nhất.

[pause] Và theo đúng lời Ryuk nói từ đầu truyện, khi mọi thứ kết thúc, Ryuk là người viết tên Light vào cuốn sổ của mình.

[pause] Kaku để ý: ngay từ đầu, Ryuk đã nói với Light rằng người dùng sổ sẽ không có kết cục tốt. Luật đó không được viết trong sổ, nhưng nó đúng tới cuối.
```

### c07 · Bảng luật và cách phá / Góc nhìn của Kaku / Kết

Khoảng 136 giây · cảnh s72–s83 · 1762 ký tự

**Gemini**

```text
Tổng kết. Luật tên và khuôn mặt: bị phá bằng đôi mắt thần chết, và được chống bằng cách giấu tên. Luật điều khiển hành động: dùng để thí nghiệm và gửi thông điệp.

<short pause> Luật mảnh giấy: giấu trong đồng hồ. Luật quyền sở hữu: tự quên mình là Kira. Luật giả: tự minh oan.

<short pause> Luật thần chết: dồn Rem vào lựa chọn. Và cách phá cuối cùng, không qua luật nào: một cuốn sổ giả.

<short pause> Nếu phải chọn một cách phá hay nhất, Kaku chọn cuốn sổ giả. Vì nó nhắc rằng một kế hoạch hoàn hảo tới đâu cũng thua một mắt xích con người mà mình không tính tới.

<short pause> Và cột cái giá: kiêu ngạo, không bao giờ được nghỉ ngơi, đánh cược cả bản thân, tuổi thọ của Misa, sự hy sinh của Rem, và cuối cùng là chính Light.

<short pause> Death Note hay vì nó biến một năng lực siêu nhiên thành một bài toán logic. <short pause> Nhưng Kaku nghĩ nó hay hơn nữa vì câu hỏi đạo đức phía sau.

<short pause> Light bắt đầu với ý định trừng phạt kẻ ác. <short pause> Nhưng để bảo vệ quyền làm điều đó, cậu giết cả những người vô tội đứng trên đường mình. Kẻ muốn làm thần công lý trở thành kẻ giết người.

<short pause> Trò chơi nhỏ: nếu bạn là L, bạn sẽ làm gì đầu tiên để tìm Kira? Và nếu bạn là Kira, bạn sẽ phạm sai lầm đầu tiên ở đâu? Viết cả hai câu trả lời, Kaku sẽ đọc.

<short pause> Và câu hỏi dành cho bạn: có ai xứng đáng được nắm trong tay quyền quyết định sống chết của người khác không? <laugh> Kaku nghĩ câu trả lời của bộ truyện rất rõ.

<short pause> Bạn thích nước cờ nào nhất trong Death Note? Mảnh giấy trong đồng hồ, tự quên mình là Kira, hay cuốn sổ giả của Near? Viết vào bình luận nhé.

<short pause> Video tiếp theo, Kaku chuyển sang một cuốn sổ vui hơn nhiều: Doraemon, và câu hỏi bảo bối nào có thể làm được ngoài đời thật, trước khi phim Doraemon mới ra rạp.

<short pause> Nếu bạn thích những video mổ xẻ luật chơi như thế này, hãy đăng ký kênh. Và nếu một ngày nhặt được cuốn sổ đen nào, hãy để nó yên dưới đất. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tổng kết. Luật tên và khuôn mặt: bị phá bằng đôi mắt thần chết, và được chống bằng cách giấu tên. Luật điều khiển hành động: dùng để thí nghiệm và gửi thông điệp.

[pause] Luật mảnh giấy: giấu trong đồng hồ. Luật quyền sở hữu: tự quên mình là Kira. Luật giả: tự minh oan.

[pause] Luật thần chết: dồn Rem vào lựa chọn. Và cách phá cuối cùng, không qua luật nào: một cuốn sổ giả.

[pause] Nếu phải chọn một cách phá hay nhất, Kaku chọn cuốn sổ giả. Vì nó nhắc rằng một kế hoạch hoàn hảo tới đâu cũng thua một mắt xích con người mà mình không tính tới.

[pause] Và cột cái giá: kiêu ngạo, không bao giờ được nghỉ ngơi, đánh cược cả bản thân, tuổi thọ của Misa, sự hy sinh của Rem, và cuối cùng là chính Light.

[pause] Death Note hay vì nó biến một năng lực siêu nhiên thành một bài toán logic. [pause] Nhưng Kaku nghĩ nó hay hơn nữa vì câu hỏi đạo đức phía sau.

[pause] Light bắt đầu với ý định trừng phạt kẻ ác. [pause] Nhưng để bảo vệ quyền làm điều đó, cậu giết cả những người vô tội đứng trên đường mình. Kẻ muốn làm thần công lý trở thành kẻ giết người.

[pause] [curious] Trò chơi nhỏ: nếu bạn là L, bạn sẽ làm gì đầu tiên để tìm Kira? Và nếu bạn là Kira, bạn sẽ phạm sai lầm đầu tiên ở đâu? Viết cả hai câu trả lời, Kaku sẽ đọc.

[pause] Và câu hỏi dành cho bạn: có ai xứng đáng được nắm trong tay quyền quyết định sống chết của người khác không? [chuckles] Kaku nghĩ câu trả lời của bộ truyện rất rõ.

[pause] Bạn thích nước cờ nào nhất trong Death Note? Mảnh giấy trong đồng hồ, tự quên mình là Kira, hay cuốn sổ giả của Near? Viết vào bình luận nhé.

[pause] Video tiếp theo, Kaku chuyển sang một cuốn sổ vui hơn nhiều: Doraemon, và câu hỏi bảo bối nào có thể làm được ngoài đời thật, trước khi phim Doraemon mới ra rạp.

[pause] Nếu bạn thích những video mổ xẻ luật chơi như thế này, hãy đăng ký kênh. Và nếu một ngày nhặt được cuốn sổ đen nào, hãy để nó yên dưới đất. Kaku gấp sổ đây, hẹn gặp lại!
```
