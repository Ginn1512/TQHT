# Bộ prompt · Tokyo Revengers: Luật du hành thời gian 12 năm và 5 cách "phá" tương lai

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 83 ảnh, 8 đoạn đọc, khoảng 15.8 phút giọng.
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

Lời: Cảnh báo: video có spoiler Tokyo Revengers tới hết anime mùa ba, arc Tenjiku. Mùa bốn đang phát, nên Kaku sẽ…

```text
Wide 16:9 landscape cinematic frame. a rainy city street at night with a single street lamp lighting a closed notebook on a bench, wide establishing shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Giả sử bạn hai mươi sáu tuổi, sống một mình trong căn phòng nhỏ, làm công việc bán thời gian mà ông chủ còn n…

```text
Wide 16:9 landscape cinematic frame. a tiny cluttered apartment at night, a young man sitting on the floor staring at a phone screen glowing in the dark, medium shot, cold screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Hôm sau, có người đẩy bạn xuống đường ray. Tiếng còi tàu. Bạn nhắm mắt. Và khi mở mắt ra, bạn đang đứng ở sân…

```text
Wide 16:9 landscape cinematic frame. a train headlight rushing toward the viewer on a station platform, motion blur, then a sunny middle school courtyard fading in, dramatic split composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Bạn sẽ làm gì? Đó là câu hỏi mà Hanagaki Takemichi phải trả lời trong Tokyo Revengers. Và câu trả lời phụ thu…

```text
Wide 16:9 landscape cinematic frame. a teenage delinquent silhouette with messy hair standing alone in an empty school hallway, looking at his own hands, medium shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Anime có rất nhiều bộ du hành thời gian. Nhưng hầu hết cho nhân vật chính một cỗ máy muốn đi đâu thì đi. Toky…

```text
Wide 16:9 landscape cinematic frame. a shelf of old sci-fi books with glowing clock covers, one simple book without a clock standing out, close-up, warm library light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình lập bảng luật của khả năng du hành thời gian trong Tokyo Revengers:…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a long scroll titled with a clock symbol on a wooden desk, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Và mỗi cách phá luật đều có một cái giá. Cuối video sẽ có bảng tổng kết một hình để bạn lưu lại.

```text
Wide 16:9 landscape cinematic frame. a simple two-column table drawn on parchment with a lock icon on one side and a key icon on the other, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Luật số 1: đúng mười hai năm

Lời: Luật đầu tiên rất đơn giản mà cũng rất khắt khe. Takemichi luôn quay về đúng mười hai năm trước, tính tới từn…

```text
Wide 16:9 landscape cinematic frame. a large calendar with pages flipping backwards from 2017 to 2005, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Takemichi tỉnh dậy trong thân thể của chính mình năm mười bốn tuổi, nhưng mang theo trí nhớ của người hai mươ…

```text
Wide 16:9 landscape cinematic frame. a teenager staring at his reflection in a school restroom mirror, the reflection showing a tired adult face, close-up, cool fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Anh phải đi học, về nhà, gặp lại bạn bè cũ như chưa có chuyện gì. Nghe thì như một kỳ nghỉ, nhưng thật ra là…

```text
Wide 16:9 landscape cinematic frame. a teenager walking home past old shop signs from the 2000s, flip phone in hand, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Anh không thể chọn quay về năm năm trước hay hai mươi năm trước. Không thể chọn một buổi sáng cụ thể để sửa m…

```text
Wide 16:9 landscape cinematic frame. a dial on an old machine that has only one fixed marking, the needle locked in place, extreme close-up, brass and amber tones. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Và thời gian ở quá khứ vẫn chạy tiếp. Nếu Takemichi ở quá khứ ba ngày rồi trở về, lần sau anh sẽ tới quá khứ…

```text
Wide 16:9 landscape cinematic frame. two parallel timelines drawn on a chalkboard, each moving forward in sync with arrows, a small figure jumping between them, diagram style, amber chalk. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Kaku gọi đây là luật một lần. Mỗi khoảnh khắc trong quá khứ, Takemichi chỉ có đúng một cơ hội. Bỏ lỡ là mất l…

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand falling in only one direction, a tiny figure running beside it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku mà có khả năng này thì chắc chỉ dùng để quay về đọc lại mấy cuốn sách hay trong thư viện. Nhưng luật một…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a book whose pages turn only forward, looking annoyed at the stuck page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Nghe thì khó chịu, nhưng chính luật này làm truyện căng thẳng. Nếu được làm lại vô hạn lần như trò chơi điện…

```text
Wide 16:9 landscape cinematic frame. a retro game screen with a big continue button crossed out in red ink, close-up, playful lighting. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Luật số 2: cái bắt tay

Lời: Luật thứ hai là cách kích hoạt. Takemichi không dùng máy móc hay phép thuật. Anh chỉ cần bắt tay một người: T…

```text
Wide 16:9 landscape cinematic frame. two hands meeting in a firm handshake, a faint ripple of light spreading from the grip, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Ở hiện tại, bắt tay Naoto người lớn thì Takemichi về quá khứ. Ở quá khứ, bắt tay Naoto còn là cậu bé thì anh…

```text
Wide 16:9 landscape cinematic frame. split frame: an adult detective shaking hands with a young man on the left, a small boy shaking hands with a teenager on the right, symmetrical composition, soft light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nghĩa là Naoto vừa là cửa đi, vừa là cửa về. Nếu Naoto chết ở tương lai, hoặc không bao giờ gặp lại Takemichi…

```text
Wide 16:9 landscape cinematic frame. an ornate door with a handshake-shaped keyhole slowly closing in a dark corridor, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Nếu Takemichi bắt tay một người khác thì sao? Không có gì xảy ra. Cỗ máy chỉ nhận đúng một người, không có bả…

```text
Wide 16:9 landscape cinematic frame. a teenager shaking hands with a classmate while nothing happens, a small crossed-out spark icon floating above, medium shot, ordinary daylight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Lần đầu tiên nghe chuyện, Naoto người lớn không tin. Anh là cảnh sát, anh tin vào bằng chứng. Nhưng Takemichi…

```text
Wide 16:9 landscape cinematic frame. a skeptical detective with arms crossed facing a nervous young man in a small office, a faded old memory glowing between them, medium shot, desk lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Chi tiết thú vị: trong dòng thời gian gốc, chính Naoto cũng đã chết cùng chị gái. Lần nhảy đầu tiên, Takemich…

```text
Wide 16:9 landscape cinematic frame. a small boy listening seriously to a teenager under a streetlamp, then a grown detective silhouette standing in a police office, before-and-after composition, warm light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thật: truyện giải thích nguồn gốc của khả năng này ở phần sau, nên hôm nay mình dừng ở luật chơ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pressing a finger to its beak with a small sealed envelope beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Luật số 3: chỉ một người nhớ

Lời: Luật thứ ba: mỗi lần Takemichi thay đổi quá khứ, tương lai được viết lại. Nhưng chỉ Takemichi mang theo ký ức…

```text
Wide 16:9 landscape cinematic frame. a stack of transparent pages each showing a slightly different city, one figure standing at the edge holding all of them, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Có những lần Takemichi trở về và thấy chính mình đang sống một cuộc đời hoàn toàn khác: một vị trí khác, nhữn…

```text
Wide 16:9 landscape cinematic frame. a young man waking up in an unfamiliar expensive apartment, confused, looking at framed photos he does not recognize, medium shot, cold morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Anh phải đoán xem ở dòng thời gian này mình là ai, mình đã làm gì, trước khi để lộ rằng mình không nhớ. Giống…

```text
Wide 16:9 landscape cinematic frame. an actor standing on a dark stage holding a blank script, a spotlight on him, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Naoto biết bí mật vì Takemichi kể cho anh. Còn tất cả những người khác sống như thể dòng thời gian mới là dòn…

```text
Wide 16:9 landscape cinematic frame. a crowd walking normally through a street while ghostly outlines of other versions of the same street flicker around one person, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Hãy thử nghĩ cảm giác đó. Bạn nhớ một người bạn đã chết, nhưng ở dòng thời gian mới họ vẫn sống. Hoặc ngược l…

```text
Wide 16:9 landscape cinematic frame. a young man standing between two photographs, one showing a friend smiling, the other showing an empty chair, medium shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Kaku gọi đây là luật cô đơn. Người du hành thời gian luôn là người duy nhất phải mang hết những phiên bản đau…

```text
Wide 16:9 landscape cinematic frame. a figure carrying a heavy backpack stuffed with torn calendar pages walking up a long staircase, wide shot, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Luật số 4: hiệu ứng cánh bướm

Lời: Luật thứ tư không được viết ra, nhưng nó hiện diện trong từng arc: một thay đổi nhỏ ở quá khứ có thể tạo ra t…

```text
Wide 16:9 landscape cinematic frame. a small butterfly flapping its wings over a map of Tokyo, faint storm clouds forming on the far edge, top-down shot, amber and navy tones. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Takemichi cứu được Draken trong trận ngày ba tháng tám. Tương lai đổi khác thật. Nhưng băng Tokyo Manji vẫn b…

```text
Wide 16:9 landscape cinematic frame. a summer festival at night with lanterns, then the same street years later lit by cold neon and dark cars, before-and-after composition. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Vấn đề là Takemichi chỉ nhìn thấy tương lai sau khi đã quay về. Anh không có cách nào thử trước một lựa chọn,…

```text
Wide 16:9 landscape cinematic frame. a young man standing before a closed door marked with a clock, the other side hidden, medium shot, dim corridor light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Anh sửa được một nút thắt, thì một nút thắt khác mọc ra ở chỗ khác. Giống như bịt một lỗ rò trên chiếc thuyền…

```text
Wide 16:9 landscape cinematic frame. a leaky wooden boat where plugging one hole makes water spurt from another, humorous close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Và có những chuyện anh không thay đổi được dù cố tới đâu. Trong arc Halloween đẫm máu, Baji Keisuke vẫn ra đi.

```text
Wide 16:9 landscape cinematic frame. a lone motorcycle parked in an empty lot under heavy rain, a single bent headlight glowing, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và những bi kịch dường như có quán tính. Như một quả bóng đang lăn xuống dốc: đẩy nó chệch hướng một chút thì…

```text
Wide 16:9 landscape cinematic frame. a heavy ball rolling down a steep hill with a small figure pushing it slightly off course, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: tương lai trong Tokyo Revengers không phải một con đường thẳng. Nó giống một mạng nhện, và mỗi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a spiderweb diagram with names replaced by small dots, looking puzzled. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · Bảng luật trước khi phá

Lời: Tóm lại, trước khi xem Takemichi phá luật thế nào, đây là bốn luật.

```text
Wide 16:9 landscape cinematic frame. four sealed envelopes laid in a row on a desk, each marked with a single numeral, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Một: luôn đúng mười hai năm, không tua lại. Hai: cửa đi và cửa về là cái bắt tay với Naoto. Ba: chỉ Takemichi…

```text
Wide 16:9 landscape cinematic frame. a neat handwritten list with four icons: a calendar, a handshake, a single eye, and a butterfly, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nếu so với các bộ khác, đây giống như được phát một thanh kiếm gỗ trong khi đối thủ cầm súng. Vậy phá luật th…

```text
Wide 16:9 landscape cinematic frame. a wooden practice sword leaning against a wall next to a scary shadow of a much larger weapon, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhìn bảng này, bạn sẽ thấy đây là một khả năng rất yếu. Không chọn được thời điểm, không làm lại được, phụ th…

```text
Wide 16:9 landscape cinematic frame. a small figure standing in front of a giant locked gate, looking up determined, wide low-angle shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40 · Cách phá 1: biến tương lai thành bộ nhớ

Lời: Cách phá đầu tiên là dùng tương lai như một cuốn sổ ghi chép. Takemichi không chọn được thời điểm, nhưng anh…

```text
Wide 16:9 landscape cinematic frame. a notebook with dates circled in red ink and small drawings of events, lying on a school desk, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Ở hiện tại, Naoto là cảnh sát. Anh tra hồ sơ, tìm ai đã chết, ai là thủ lĩnh, vụ việc bắt đầu từ đâu. Rồi Tak…

```text
Wide 16:9 landscape cinematic frame. a detective's desk covered in case files, photos pinned to a corkboard with red strings, a young man leaning over it, medium shot, desk lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Nhờ vậy Takemichi biết ngày ba tháng tám là ngày Draken bị đâm trong một trận ẩu đả. Anh có mặt ở đó từ trước…

```text
Wide 16:9 landscape cinematic frame. a summer festival shrine at night with a torn paper lantern on the ground, a teenager kneeling beside an injured friend in the rain, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Naoto cũng phải trả giá: điều tra những băng nhóm tội phạm nguy hiểm khi chính mình là mục tiêu. Có những dòn…

```text
Wide 16:9 landscape cinematic frame. a detective walking quickly through a dark parking garage, looking over his shoulder, wide shot, harsh overhead light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Hai người biến cỗ máy thời gian thành một đội điều tra: một người ở tương lai tìm manh mối, một người ở quá k…

```text
Wide 16:9 landscape cinematic frame. a diagram of two figures connected by a glowing line through a clock, one holding a magnifying glass, the other running, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Cái giá: thông tin luôn đến trễ. Hồ sơ cảnh sát chỉ ghi kết quả, không ghi lý do. Takemichi thường biết ai sẽ…

```text
Wide 16:9 landscape cinematic frame. a case file with most lines blacked out except a date and a name, extreme close-up, cold desk lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Cách phá 2: đi từ bên trong

Lời: Cách phá thứ hai là thay đổi chính mình. Takemichi mười bốn tuổi yếu, nhút nhát, đánh nhau toàn thua. Thay vì…

```text
Wide 16:9 landscape cinematic frame. a small teenage figure standing at the gates of a rough motorcycle gang meeting under a highway overpass, dozens of bikes parked around, wide shot, orange night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Anh làm quen với Mikey, thủ lĩnh Tokyo Manji, và Draken, phó thủ lĩnh. Anh đứng lên trong những lúc mà người…

```text
Wide 16:9 landscape cinematic frame. a group of teenagers sitting on a riverbank at sunset, one small figure being accepted into the circle, back view, golden light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Anh học cách nói chuyện với những người mà anh từng sợ. Anh hiểu vì sao họ đánh nhau, họ trung thành với ai,…

```text
Wide 16:9 landscape cinematic frame. a nervous teenager sitting with older tough-looking teens at a ramen stall late at night, everyone laughing, medium shot, warm steam and light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Lý do rất đơn giản: đứng ngoài thì chỉ nhìn được hậu quả. Đứng trong thì mới chạm được vào quyết định.

```text
Wide 16:9 landscape cinematic frame. a clock mechanism seen from the inside, a tiny figure standing among the gears, wide shot, warm brass light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Cái giá: thân xác của Takemichi chịu đòn thật, đau thật. Và càng gắn bó với mọi người, mỗi lần mất một ai đó…

```text
Wide 16:9 landscape cinematic frame. a bruised teenage fist wrapped in torn bandages resting on a knee, close-up, dim evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải khen tác giả một câu: Takemichi có lẽ là nhân vật chính khóc nhiều nhất trong các bộ shounen mà Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tally counter with a huge number and tissues piled around it, comic expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Cách phá 3: tìm gốc rễ

Lời: Cách phá thứ ba là thôi đuổi theo từng bi kịch, mà đi tìm gốc rễ. Qua nhiều lần nhảy, một cái tên cứ xuất hiệ…

```text
Wide 16:9 landscape cinematic frame. a tangled root system beneath a dark tree, all roots leading to one small glowing point, cross-section diagram style, amber light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Ở dòng thời gian này, Kisaki là quân sư của Tokyo Manji. Ở dòng thời gian khác, hắn vẫn đứng gần quyền lực. C…

```text
Wide 16:9 landscape cinematic frame. a chess board where one dark piece keeps reappearing next to the king in several ghostly overlapping positions, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Nhìn vào luật, nghi ngờ này có cơ sở: một người hai mươi sáu tuổi trong thân xác thiếu niên thì dĩ nhiên sẽ t…

```text
Wide 16:9 landscape cinematic frame. a young man in glasses calmly moving pieces on a board several turns ahead, reflected in a dark window, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Takemichi và Naoto từng nghi ngờ Kisaki cũng là người du hành thời gian. Kaku sẽ không nói nghi ngờ đó đúng h…

```text
Wide 16:9 landscape cinematic frame. two figures studying a board with a question mark drawn over a silhouette, medium shot, warm desk lamp light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Ở arc Tenjiku, người em gái của Mikey là Emma trở thành nạn nhân. Một mất mát mà Takemichi không kịp ngăn, và…

```text
Wide 16:9 landscape cinematic frame. a fallen hair ribbon lying on wet asphalt beside a motorcycle wheel, extreme close-up, cold rain light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Cái giá: một kẻ thù thông minh thì cũng thích nghi. Mỗi lần gốc rễ bị cắt ở chỗ này, nó lại mọc ra ở chỗ khác…

```text
Wide 16:9 landscape cinematic frame. a weed growing back through a crack in concrete after being cut, time-lapse style, close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Cách phá 4: thay đổi con người, không chỉ sự kiện

Lời: Cách phá thứ tư là cách Kaku thấy tinh tế nhất. Takemichi dần hiểu rằng cứu một người khỏi một sự kiện là chư…

```text
Wide 16:9 landscape cinematic frame. a hand gently placing a small lit candle inside a dark hollow tree trunk, close-up, warm glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Mikey mạnh nhất, được mọi người tôn thờ, nhưng mỗi lần mất một người thân, cậu lại tối đi một chút. Ở tương l…

```text
Wide 16:9 landscape cinematic frame. a young gang leader sitting alone on a motorcycle at the edge of a pier at night, city lights far away, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Draken từng nói với Takemichi rằng Mikey cần có người bên cạnh. Mikey mạnh tới mức không ai nghĩ cậu cần được…

```text
Wide 16:9 landscape cinematic frame. a tall teenager placing a hand on a shorter friend's shoulder, both looking at a smaller figure sitting alone ahead, back view, sunset light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Vì vậy mục tiêu thật của Takemichi dần chuyển từ cứu Hina sang cứu cả Mikey. Không phải khỏi kẻ thù, mà khỏi…

```text
Wide 16:9 landscape cinematic frame. two teenagers sitting back to back on a rooftop, one reaching his hand back toward the other without looking, medium shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Cái giá: đây là cách khó nhất, vì con người không thay đổi bằng một cú đấm hay một thông tin mật. Và luật một…

```text
Wide 16:9 landscape cinematic frame. a fragile glass heart resting on a narrow bridge above a dark river, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Cách phá 5: niềm tin

Lời: Cách phá cuối cùng không nằm trong luật nào cả. Takemichi không mạnh, không thông minh bằng Kisaki. Thứ anh c…

```text
Wide 16:9 landscape cinematic frame. a small figure standing up again in the rain after falling, a group of silhouettes behind him slowly standing too, wide shot, dramatic backlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Có một biệt danh người ta dành cho anh: anh hùng hay khóc. Nghe như trêu, nhưng trong thế giới đó, dám khóc m…

```text
Wide 16:9 landscape cinematic frame. a teenager with a bruised face wiping tears while standing firm in front of a crowd, medium shot, warm dramatic backlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nhiều người trong băng bắt đầu đi theo anh không phải vì anh đánh thắng, mà vì anh đứng dậy. Chifuyu, người b…

```text
Wide 16:9 landscape cinematic frame. two teenage friends fist-bumping in front of a convenience store at night, warm neon light, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và nhìn lại, cả bốn cách phá trước đều cần người khác: Naoto để điều tra, cả băng để thay đổi từ bên trong, b…

```text
Wide 16:9 landscape cinematic frame. a web diagram connecting a central figure to several allies with glowing lines, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku thấy đây là cách truyện trả lời câu hỏi lớn: một khả năng yếu tới vậy thì làm sao thắng được số phận? Bằ…

```text
Wide 16:9 landscape cinematic frame. many small hands stacked on top of each other in a circle, top-down shot, warm lantern light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Cái giá: niềm tin là thứ dễ vỡ nhất. Nếu Takemichi thất bại, không chỉ anh mất tất cả, mà cả những người đã t…

```text
Wide 16:9 landscape cinematic frame. a paper chain of linked figures with one link starting to tear, close-up, soft candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Bảng tổng kết · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ ghép tất cả vào một bảng. Cột trái là luật, cột phải là cách phá và cái giá.

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a large two-column chart onto a corkboard, satisfied expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Luật đúng mười hai năm, không tua lại: phá bằng cách biến tương lai thành cuốn sổ ghi chép. Cái giá là thông…

```text
Wide 16:9 landscape cinematic frame. row one of a chart with a calendar icon and a notebook icon, parchment close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Luật bắt tay với Naoto: biến một cánh cửa thành một cộng sự. Cái giá là mọi thứ phụ thuộc vào an toàn của Nao…

```text
Wide 16:9 landscape cinematic frame. row two with a handshake icon and a detective badge icon, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Luật một người nhớ và hiệu ứng cánh bướm: phá bằng cách vào trong băng và tìm gốc rễ. Cái giá là đau thật và…

```text
Wide 16:9 landscape cinematic frame. row three with an eye icon, a butterfly icon and a tree root icon, parchment close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Và thứ phá được mọi luật: thay đổi con người, bằng niềm tin. Cái giá là nó dễ vỡ nhất.

```text
Wide 16:9 landscape cinematic frame. the final row with a candle icon and a paper chain icon, glowing slightly brighter than the rest, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Góc nhìn của Kaku: vì sao luật yếu lại hay

Lời: Trong một video sắp tới, Kaku sẽ đặt Tokyo Revengers lên bàn so sánh với hai bộ du hành thời gian nổi tiếng k…

```text
Wide 16:9 landscape cinematic frame. three different clocks placed side by side on a round table under a spotlight, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Nhiều bộ du hành thời gian cho nhân vật chính một khả năng gần như vô địch. Tokyo Revengers thì ngược lại: kh…

```text
Wide 16:9 landscape cinematic frame. a comparison sketch: a giant glowing time machine on one side, a simple handshake on the other, parchment diagram, amber ink. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nếu Takemichi có thể quay lại bất cứ lúc nào, ta sẽ không cần anh can đảm. Chính vì anh chỉ có một cơ hội, mỗ…

```text
Wide 16:9 landscape cinematic frame. a single match being struck in the dark, its tiny flame lighting a determined face, extreme close-up, warm flame light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Kaku nghĩ đó chính là điểm hay. Khi cỗ máy thời gian không đủ để thắng, nhân vật buộc phải dùng những thứ khô…

```text
Wide 16:9 landscape cinematic frame. a teenager standing in front of a huge crowd of rival gang members, fists clenched, wide low-angle shot, sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu bạn có khả năng của Takemichi, bạn sẽ quay về năm nào của mình, và sửa điều gì? Kaku tò mò lắm, viết vào…

```text
Wide 16:9 landscape cinematic frame. a young person looking at an old childhood photo under a desk lamp, close-up, nostalgic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Kết

Lời: Tokyo Revengers không thật sự kể về một cỗ máy thời gian. Nó kể về một người bình thường quyết định rằng quá…

```text
Wide 16:9 landscape cinematic frame. a young man walking toward the camera on an empty street at dawn, the city waking up behind him, wide shot, warm sunrise. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Takemichi không có siêu năng lực chiến đấu, không có trí tuệ thiên tài. Anh chỉ có một cái bắt tay, và quyết…

```text
Wide 16:9 landscape cinematic frame. two hands clasped tightly in the rain, extreme close-up, soft warm light breaking through the grey. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Mùa bốn đang phát, và luật chơi sẽ còn thay đổi theo những cách mà Kaku chưa được phép kể. Xem xong mùa bốn,…

```text
Wide 16:9 landscape cinematic frame. a calendar page marked with a small star on the current week beside a remote control, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Video tiếp theo, Kaku leo lên tận đỉnh vũ trụ Dragon Ball để xếp hạng các vị thần, từ Kaioshin tới người mà n…

```text
Wide 16:9 landscape cinematic frame. a tall cosmic staircase rising into a starry sky with glowing thrones at different heights, wide shot, violet and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích kiểu video lập bảng luật như thế này, hãy đăng ký kênh để Kaku lập thêm nhiều bảng nữa. Kaku gấ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing its notebook and giving a small handshake to the viewer with one wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 87 giây · cảnh s01–s07 · 1132 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Tokyo Revengers tới hết anime mùa ba, arc Tenjiku. Mùa bốn đang phát, nên Kaku sẽ không nói gì về những chuyện xảy ra trong đó.

<short pause> Giả sử bạn hai mươi sáu tuổi, sống một mình trong căn phòng nhỏ, làm công việc bán thời gian mà ông chủ còn nhỏ tuổi hơn bạn. Rồi một buổi tối, bạn đọc được tin người bạn gái đầu tiên đã chết.

<short pause> Hôm sau, có người đẩy bạn xuống đường ray. Tiếng còi tàu. Bạn nhắm mắt. Và khi mở mắt ra, bạn đang đứng ở sân trường cấp hai, mười hai năm về trước.

<short pause> Bạn sẽ làm gì? Đó là câu hỏi mà Hanagaki Takemichi phải trả lời trong Tokyo Revengers. Và câu trả lời phụ thuộc hoàn toàn vào luật chơi của cỗ máy thời gian kỳ lạ này.

<short pause> Anime có rất nhiều bộ du hành thời gian. <short pause> Nhưng hầu hết cho nhân vật chính một cỗ máy muốn đi đâu thì đi. Tokyo Revengers thì khác: cỗ máy này gần như không cho Takemichi chọn gì cả.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình lập bảng luật của khả năng du hành thời gian trong Tokyo Revengers: nó hoạt động thế nào, giới hạn ở đâu, và những cách mà Takemichi đã dùng để phá luật.

<short pause> Và mỗi cách phá luật đều có một cái giá. Cuối video sẽ có bảng tổng kết một hình để bạn lưu lại.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Tokyo Revengers tới hết anime mùa ba, arc Tenjiku. Mùa bốn đang phát, nên Kaku sẽ không nói gì về những chuyện xảy ra trong đó.

[pause] Giả sử bạn hai mươi sáu tuổi, sống một mình trong căn phòng nhỏ, làm công việc bán thời gian mà ông chủ còn nhỏ tuổi hơn bạn. Rồi một buổi tối, bạn đọc được tin người bạn gái đầu tiên đã chết.

[pause] Hôm sau, có người đẩy bạn xuống đường ray. Tiếng còi tàu. Bạn nhắm mắt. Và khi mở mắt ra, bạn đang đứng ở sân trường cấp hai, mười hai năm về trước.

[pause] [curious] Bạn sẽ làm gì? Đó là câu hỏi mà Hanagaki Takemichi phải trả lời trong Tokyo Revengers. Và câu trả lời phụ thuộc hoàn toàn vào luật chơi của cỗ máy thời gian kỳ lạ này.

[pause] Anime có rất nhiều bộ du hành thời gian. [pause] Nhưng hầu hết cho nhân vật chính một cỗ máy muốn đi đâu thì đi. Tokyo Revengers thì khác: cỗ máy này gần như không cho Takemichi chọn gì cả.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình lập bảng luật của khả năng du hành thời gian trong Tokyo Revengers: nó hoạt động thế nào, giới hạn ở đâu, và những cách mà Takemichi đã dùng để phá luật.

[pause] Và mỗi cách phá luật đều có một cái giá. Cuối video sẽ có bảng tổng kết một hình để bạn lưu lại.
```

### c02 · Luật số 1: đúng mười hai năm

Khoảng 96 giây · cảnh s08–s15 · 1245 ký tự

**Gemini**

```text
Luật đầu tiên rất đơn giản mà cũng rất khắt khe. Takemichi luôn quay về đúng mười hai năm trước, tính tới từng ngày. Năm 2017 thành năm 2005.

<short pause> Takemichi tỉnh dậy trong thân thể của chính mình năm mười bốn tuổi, nhưng mang theo trí nhớ của người hai mươi sáu tuổi. Người khác thấy một cậu học sinh cấp hai. Bên trong là một người lớn đang hoảng loạn.

<short pause> Anh phải đi học, về nhà, gặp lại bạn bè cũ như chưa có chuyện gì. Nghe thì như một kỳ nghỉ, nhưng thật ra là một nhiệm vụ không có bản hướng dẫn.

<short pause> Anh không thể chọn quay về năm năm trước hay hai mươi năm trước. Không thể chọn một buổi sáng cụ thể để sửa một lỗi cụ thể. Cỗ máy chỉ có một con số: mười hai.

<short pause> Và thời gian ở quá khứ vẫn chạy tiếp. Nếu Takemichi ở quá khứ ba ngày rồi trở về, lần sau anh sẽ tới quá khứ muộn hơn ba ngày. Không có nút tua lại.

<short pause> Kaku gọi đây là luật một lần. Mỗi khoảnh khắc trong quá khứ, Takemichi chỉ có đúng một cơ hội. Bỏ lỡ là mất luôn.

<short pause> <laugh> Kaku mà có khả năng này thì chắc chỉ dùng để quay về đọc lại mấy cuốn sách hay trong thư viện. <short pause> Nhưng luật một lần nghĩa là đọc xong một trang là không lật lại được. Thôi, Kaku xin kiếu.

<short pause> Nghe thì khó chịu, nhưng chính luật này làm truyện căng thẳng. Nếu được làm lại vô hạn lần như trò chơi điện tử, thì không cảnh nào còn đáng sợ nữa.
```

**ElevenLabs**

```text
Luật đầu tiên rất đơn giản mà cũng rất khắt khe. Takemichi luôn quay về đúng mười hai năm trước, tính tới từng ngày. Năm 2017 thành năm 2005.

[pause] Takemichi tỉnh dậy trong thân thể của chính mình năm mười bốn tuổi, nhưng mang theo trí nhớ của người hai mươi sáu tuổi. Người khác thấy một cậu học sinh cấp hai. Bên trong là một người lớn đang hoảng loạn.

[pause] Anh phải đi học, về nhà, gặp lại bạn bè cũ như chưa có chuyện gì. Nghe thì như một kỳ nghỉ, nhưng thật ra là một nhiệm vụ không có bản hướng dẫn.

[pause] Anh không thể chọn quay về năm năm trước hay hai mươi năm trước. Không thể chọn một buổi sáng cụ thể để sửa một lỗi cụ thể. Cỗ máy chỉ có một con số: mười hai.

[pause] Và thời gian ở quá khứ vẫn chạy tiếp. Nếu Takemichi ở quá khứ ba ngày rồi trở về, lần sau anh sẽ tới quá khứ muộn hơn ba ngày. Không có nút tua lại.

[pause] Kaku gọi đây là luật một lần. Mỗi khoảnh khắc trong quá khứ, Takemichi chỉ có đúng một cơ hội. Bỏ lỡ là mất luôn.

[pause] [chuckles] Kaku mà có khả năng này thì chắc chỉ dùng để quay về đọc lại mấy cuốn sách hay trong thư viện. [pause] Nhưng luật một lần nghĩa là đọc xong một trang là không lật lại được. Thôi, Kaku xin kiếu.

[pause] Nghe thì khó chịu, nhưng chính luật này làm truyện căng thẳng. Nếu được làm lại vô hạn lần như trò chơi điện tử, thì không cảnh nào còn đáng sợ nữa.
```

### c03 · Luật số 2: cái bắt tay

Khoảng 87 giây · cảnh s16–s22 · 1137 ký tự

**Gemini**

```text
Luật thứ hai là cách kích hoạt. Takemichi không dùng máy móc hay phép thuật. Anh chỉ cần bắt tay một người: Tachibana Naoto, em trai của bạn gái cũ.

<short pause> Ở hiện tại, bắt tay Naoto người lớn thì Takemichi về quá khứ. Ở quá khứ, bắt tay Naoto còn là cậu bé thì anh trở về hiện tại.

<short pause> Nghĩa là Naoto vừa là cửa đi, vừa là cửa về. Nếu Naoto chết ở tương lai, hoặc không bao giờ gặp lại Takemichi, cánh cửa đóng lại.

<short pause> Nếu Takemichi bắt tay một người khác thì sao? Không có gì xảy ra. Cỗ máy chỉ nhận đúng một người, không có bản sao, không có người thay thế.

<short pause> Lần đầu tiên nghe chuyện, Naoto người lớn không tin. Anh là cảnh sát, anh tin vào bằng chứng. <short pause> Nhưng Takemichi biết những điều mà chỉ người ở quá khứ mới biết, và Naoto nhớ lại lời dặn năm xưa của cậu thiếu niên kỳ lạ đó.

<short pause> Chi tiết thú vị: trong dòng thời gian gốc, chính Naoto cũng đã chết cùng chị gái. Lần nhảy đầu tiên, Takemichi dặn cậu bé Naoto bảo vệ chị. Nhờ câu dặn đó, Naoto sống, lớn lên thành cảnh sát, và trở thành cộng sự.

<short pause> <laugh> Kaku phải nói thật: truyện giải thích nguồn gốc của khả năng này ở phần sau, nên hôm nay mình dừng ở luật chơi thôi. Ai đã đọc manga thì giữ bí mật giúp Kaku nhé.
```

**ElevenLabs**

```text
Luật thứ hai là cách kích hoạt. Takemichi không dùng máy móc hay phép thuật. Anh chỉ cần bắt tay một người: Tachibana Naoto, em trai của bạn gái cũ.

[pause] Ở hiện tại, bắt tay Naoto người lớn thì Takemichi về quá khứ. Ở quá khứ, bắt tay Naoto còn là cậu bé thì anh trở về hiện tại.

[pause] Nghĩa là Naoto vừa là cửa đi, vừa là cửa về. Nếu Naoto chết ở tương lai, hoặc không bao giờ gặp lại Takemichi, cánh cửa đóng lại.

[pause] [curious] Nếu Takemichi bắt tay một người khác thì sao? Không có gì xảy ra. Cỗ máy chỉ nhận đúng một người, không có bản sao, không có người thay thế.

[pause] Lần đầu tiên nghe chuyện, Naoto người lớn không tin. Anh là cảnh sát, anh tin vào bằng chứng. [pause] Nhưng Takemichi biết những điều mà chỉ người ở quá khứ mới biết, và Naoto nhớ lại lời dặn năm xưa của cậu thiếu niên kỳ lạ đó.

[pause] Chi tiết thú vị: trong dòng thời gian gốc, chính Naoto cũng đã chết cùng chị gái. Lần nhảy đầu tiên, Takemichi dặn cậu bé Naoto bảo vệ chị. Nhờ câu dặn đó, Naoto sống, lớn lên thành cảnh sát, và trở thành cộng sự.

[pause] [chuckles] Kaku phải nói thật: truyện giải thích nguồn gốc của khả năng này ở phần sau, nên hôm nay mình dừng ở luật chơi thôi. Ai đã đọc manga thì giữ bí mật giúp Kaku nhé.
```

### c04 · Luật số 3: chỉ một người nhớ / Luật số 4: hiệu ứng cánh bướm

Khoảng 144 giây · cảnh s23–s35 · 1872 ký tự

**Gemini**

```text
Luật thứ ba: mỗi lần Takemichi thay đổi quá khứ, tương lai được viết lại. <short pause> Nhưng chỉ Takemichi mang theo ký ức về những phiên bản cũ.

<short pause> Có những lần Takemichi trở về và thấy chính mình đang sống một cuộc đời hoàn toàn khác: một vị trí khác, những người xung quanh khác, những ký ức mà anh không hề có.

<short pause> Anh phải đoán xem ở dòng thời gian này mình là ai, mình đã làm gì, trước khi để lộ rằng mình không nhớ. Giống như vào vai một nhân vật mà không được đọc kịch bản.

<short pause> Naoto biết bí mật vì Takemichi kể cho anh. Còn tất cả những người khác sống như thể dòng thời gian mới là dòng thời gian duy nhất từng có.

<short pause> Hãy thử nghĩ cảm giác đó. Bạn nhớ một người bạn đã chết, nhưng ở dòng thời gian mới họ vẫn sống. Hoặc ngược lại: bạn cứu được người này, rồi phát hiện người khác lại chết thay.

<short pause> Kaku gọi đây là luật cô đơn. Người du hành thời gian luôn là người duy nhất phải mang hết những phiên bản đau lòng.

<short pause> Luật thứ tư không được viết ra, nhưng nó hiện diện trong từng arc: một thay đổi nhỏ ở quá khứ có thể tạo ra thay đổi rất lớn ở tương lai, và thường là theo cách không ai lường trước.

<short pause> Takemichi cứu được Draken trong trận ngày ba tháng tám. Tương lai đổi khác thật. <short pause> Nhưng băng Tokyo Manji vẫn biến thành một tổ chức tội phạm, và Hina vẫn chết.

<short pause> Vấn đề là Takemichi chỉ nhìn thấy tương lai sau khi đã quay về. Anh không có cách nào thử trước một lựa chọn, xem kết quả, rồi chọn lại.

<short pause> Anh sửa được một nút thắt, thì một nút thắt khác mọc ra ở chỗ khác. Giống như bịt một lỗ rò trên chiếc thuyền cũ.

<short pause> Và có những chuyện anh không thay đổi được dù cố tới đâu. Trong arc Halloween đẫm máu, Baji Keisuke vẫn ra đi.

<short pause> Và những bi kịch dường như có quán tính. Như một quả bóng đang lăn xuống dốc: đẩy nó chệch hướng một chút thì được, nhưng làm nó dừng hẳn thì rất khó.

<short pause> <laugh> Kaku ghi chú: tương lai trong Tokyo Revengers không phải một con đường thẳng. Nó giống một mạng nhện, và mỗi sợi đều kéo theo sợi khác.
```

**ElevenLabs**

```text
Luật thứ ba: mỗi lần Takemichi thay đổi quá khứ, tương lai được viết lại. [pause] Nhưng chỉ Takemichi mang theo ký ức về những phiên bản cũ.

[pause] Có những lần Takemichi trở về và thấy chính mình đang sống một cuộc đời hoàn toàn khác: một vị trí khác, những người xung quanh khác, những ký ức mà anh không hề có.

[pause] Anh phải đoán xem ở dòng thời gian này mình là ai, mình đã làm gì, trước khi để lộ rằng mình không nhớ. Giống như vào vai một nhân vật mà không được đọc kịch bản.

[pause] Naoto biết bí mật vì Takemichi kể cho anh. Còn tất cả những người khác sống như thể dòng thời gian mới là dòng thời gian duy nhất từng có.

[pause] Hãy thử nghĩ cảm giác đó. Bạn nhớ một người bạn đã chết, nhưng ở dòng thời gian mới họ vẫn sống. Hoặc ngược lại: bạn cứu được người này, rồi phát hiện người khác lại chết thay.

[pause] Kaku gọi đây là luật cô đơn. Người du hành thời gian luôn là người duy nhất phải mang hết những phiên bản đau lòng.

[pause] Luật thứ tư không được viết ra, nhưng nó hiện diện trong từng arc: một thay đổi nhỏ ở quá khứ có thể tạo ra thay đổi rất lớn ở tương lai, và thường là theo cách không ai lường trước.

[pause] Takemichi cứu được Draken trong trận ngày ba tháng tám. Tương lai đổi khác thật. [pause] Nhưng băng Tokyo Manji vẫn biến thành một tổ chức tội phạm, và Hina vẫn chết.

[pause] Vấn đề là Takemichi chỉ nhìn thấy tương lai sau khi đã quay về. Anh không có cách nào thử trước một lựa chọn, xem kết quả, rồi chọn lại.

[pause] Anh sửa được một nút thắt, thì một nút thắt khác mọc ra ở chỗ khác. Giống như bịt một lỗ rò trên chiếc thuyền cũ.

[pause] Và có những chuyện anh không thay đổi được dù cố tới đâu. Trong arc Halloween đẫm máu, Baji Keisuke vẫn ra đi.

[pause] Và những bi kịch dường như có quán tính. Như một quả bóng đang lăn xuống dốc: đẩy nó chệch hướng một chút thì được, nhưng làm nó dừng hẳn thì rất khó.

[pause] [chuckles] Kaku ghi chú: tương lai trong Tokyo Revengers không phải một con đường thẳng. Nó giống một mạng nhện, và mỗi sợi đều kéo theo sợi khác.
```

### c05 · Bảng luật trước khi phá / Cách phá 1: biến tương lai thành bộ nhớ

Khoảng 110 giây · cảnh s36–s45 · 1430 ký tự

**Gemini**

```text
Tóm lại, trước khi xem Takemichi phá luật thế nào, đây là bốn luật.

<short pause> Một: luôn đúng mười hai năm, không tua lại. Hai: cửa đi và cửa về là cái bắt tay với Naoto. Ba: chỉ Takemichi nhớ các dòng thời gian cũ. Bốn: sửa một chỗ có thể làm hỏng chỗ khác.

<short pause> Nếu so với các bộ khác, đây giống như được phát một thanh kiếm gỗ trong khi đối thủ cầm súng. Vậy phá luật thế nào? Có năm cách.

<short pause> Nhìn bảng này, bạn sẽ thấy đây là một khả năng rất yếu. Không chọn được thời điểm, không làm lại được, phụ thuộc vào một người khác. Vậy mà Takemichi vẫn tìm ra cách.

<short pause> Cách phá đầu tiên là dùng tương lai như một cuốn sổ ghi chép. Takemichi không chọn được thời điểm, nhưng anh biết trước những ngày quan trọng sẽ xảy ra chuyện gì.

<short pause> Ở hiện tại, Naoto là cảnh sát. Anh tra hồ sơ, tìm ai đã chết, ai là thủ lĩnh, vụ việc bắt đầu từ đâu. Rồi Takemichi mang thông tin đó về quá khứ.

<short pause> Nhờ vậy Takemichi biết ngày ba tháng tám là ngày Draken bị đâm trong một trận ẩu đả. Anh có mặt ở đó từ trước, và lần đầu tiên thật sự đổi được một cái chết.

<short pause> Naoto cũng phải trả giá: điều tra những băng nhóm tội phạm nguy hiểm khi chính mình là mục tiêu. Có những dòng thời gian cả hai suýt không sống sót.

<short pause> Hai người biến cỗ máy thời gian thành một đội điều tra: một người ở tương lai tìm manh mối, một người ở quá khứ hành động.

<short pause> Cái giá: thông tin luôn đến trễ. Hồ sơ cảnh sát chỉ ghi kết quả, không ghi lý do. Takemichi thường biết ai sẽ chết, nhưng không biết ai sẽ ra tay và vì sao.
```

**ElevenLabs**

```text
Tóm lại, trước khi xem Takemichi phá luật thế nào, đây là bốn luật.

[pause] Một: luôn đúng mười hai năm, không tua lại. Hai: cửa đi và cửa về là cái bắt tay với Naoto. Ba: chỉ Takemichi nhớ các dòng thời gian cũ. Bốn: sửa một chỗ có thể làm hỏng chỗ khác.

[pause] Nếu so với các bộ khác, đây giống như được phát một thanh kiếm gỗ trong khi đối thủ cầm súng. [curious] Vậy phá luật thế nào? Có năm cách.

[pause] Nhìn bảng này, bạn sẽ thấy đây là một khả năng rất yếu. Không chọn được thời điểm, không làm lại được, phụ thuộc vào một người khác. Vậy mà Takemichi vẫn tìm ra cách.

[pause] Cách phá đầu tiên là dùng tương lai như một cuốn sổ ghi chép. Takemichi không chọn được thời điểm, nhưng anh biết trước những ngày quan trọng sẽ xảy ra chuyện gì.

[pause] Ở hiện tại, Naoto là cảnh sát. Anh tra hồ sơ, tìm ai đã chết, ai là thủ lĩnh, vụ việc bắt đầu từ đâu. Rồi Takemichi mang thông tin đó về quá khứ.

[pause] Nhờ vậy Takemichi biết ngày ba tháng tám là ngày Draken bị đâm trong một trận ẩu đả. Anh có mặt ở đó từ trước, và lần đầu tiên thật sự đổi được một cái chết.

[pause] Naoto cũng phải trả giá: điều tra những băng nhóm tội phạm nguy hiểm khi chính mình là mục tiêu. Có những dòng thời gian cả hai suýt không sống sót.

[pause] Hai người biến cỗ máy thời gian thành một đội điều tra: một người ở tương lai tìm manh mối, một người ở quá khứ hành động.

[pause] Cái giá: thông tin luôn đến trễ. Hồ sơ cảnh sát chỉ ghi kết quả, không ghi lý do. Takemichi thường biết ai sẽ chết, nhưng không biết ai sẽ ra tay và vì sao.
```

### c06 · Cách phá 2: đi từ bên trong / Cách phá 3: tìm gốc rễ

Khoảng 142 giây · cảnh s46–s57 · 1846 ký tự

**Gemini**

```text
Cách phá thứ hai là thay đổi chính mình. Takemichi mười bốn tuổi yếu, nhút nhát, đánh nhau toàn thua. Thay vì tránh băng đảng, anh chọn bước vào nó.

<short pause> Anh làm quen với Mikey, thủ lĩnh Tokyo Manji, và Draken, phó thủ lĩnh. Anh đứng lên trong những lúc mà người khác bỏ chạy. Dần dần, anh trở thành đội trưởng đội một.

<short pause> Anh học cách nói chuyện với những người mà anh từng sợ. Anh hiểu vì sao họ đánh nhau, họ trung thành với ai, họ sợ mất điều gì.

<short pause> Lý do rất đơn giản: đứng ngoài thì chỉ nhìn được hậu quả. Đứng trong thì mới chạm được vào quyết định.

<short pause> Cái giá: thân xác của Takemichi chịu đòn thật, đau thật. Và càng gắn bó với mọi người, mỗi lần mất một ai đó càng đau hơn.

<short pause> <laugh> Kaku phải khen tác giả một câu: Takemichi có lẽ là nhân vật chính khóc nhiều nhất trong các bộ shounen mà Kaku biết. <short pause> Nhưng anh chưa bao giờ bỏ cuộc. Kaku đã đếm thử số lần anh khóc, rồi bỏ cuộc trước anh.

<short pause> Cách phá thứ ba là thôi đuổi theo từng bi kịch, mà đi tìm gốc rễ. Qua nhiều lần nhảy, một cái tên cứ xuất hiện đằng sau mọi chuyện: Kisaki Tetta.

<short pause> Ở dòng thời gian này, Kisaki là quân sư của Tokyo Manji. Ở dòng thời gian khác, hắn vẫn đứng gần quyền lực. Có vẻ như dù Takemichi đổi gì, hắn cũng tìm được đường lên.

<short pause> Nhìn vào luật, nghi ngờ này có cơ sở: một người hai mươi sáu tuổi trong thân xác thiếu niên thì dĩ nhiên sẽ thông minh bất thường. Kisaki thì luôn tính trước người khác vài bước.

<short pause> Takemichi và Naoto từng nghi ngờ Kisaki cũng là người du hành thời gian. Kaku sẽ không nói nghi ngờ đó đúng hay sai. <short pause> Nhưng đây là một bước suy luận rất hợp lý theo luật đã biết.

<short pause> Ở arc Tenjiku, người em gái của Mikey là Emma trở thành nạn nhân. Một mất mát mà Takemichi không kịp ngăn, và nó đẩy Mikey tới gần bóng tối hơn bao giờ hết.

<short pause> Cái giá: một kẻ thù thông minh thì cũng thích nghi. Mỗi lần gốc rễ bị cắt ở chỗ này, nó lại mọc ra ở chỗ khác, kéo theo những bi kịch mới, như arc Tenjiku.
```

**ElevenLabs**

```text
Cách phá thứ hai là thay đổi chính mình. Takemichi mười bốn tuổi yếu, nhút nhát, đánh nhau toàn thua. Thay vì tránh băng đảng, anh chọn bước vào nó.

[pause] Anh làm quen với Mikey, thủ lĩnh Tokyo Manji, và Draken, phó thủ lĩnh. Anh đứng lên trong những lúc mà người khác bỏ chạy. Dần dần, anh trở thành đội trưởng đội một.

[pause] Anh học cách nói chuyện với những người mà anh từng sợ. Anh hiểu vì sao họ đánh nhau, họ trung thành với ai, họ sợ mất điều gì.

[pause] Lý do rất đơn giản: đứng ngoài thì chỉ nhìn được hậu quả. Đứng trong thì mới chạm được vào quyết định.

[pause] Cái giá: thân xác của Takemichi chịu đòn thật, đau thật. Và càng gắn bó với mọi người, mỗi lần mất một ai đó càng đau hơn.

[pause] [chuckles] Kaku phải khen tác giả một câu: Takemichi có lẽ là nhân vật chính khóc nhiều nhất trong các bộ shounen mà Kaku biết. [pause] Nhưng anh chưa bao giờ bỏ cuộc. Kaku đã đếm thử số lần anh khóc, rồi bỏ cuộc trước anh.

[pause] Cách phá thứ ba là thôi đuổi theo từng bi kịch, mà đi tìm gốc rễ. Qua nhiều lần nhảy, một cái tên cứ xuất hiện đằng sau mọi chuyện: Kisaki Tetta.

[pause] Ở dòng thời gian này, Kisaki là quân sư của Tokyo Manji. Ở dòng thời gian khác, hắn vẫn đứng gần quyền lực. Có vẻ như dù Takemichi đổi gì, hắn cũng tìm được đường lên.

[pause] Nhìn vào luật, nghi ngờ này có cơ sở: một người hai mươi sáu tuổi trong thân xác thiếu niên thì dĩ nhiên sẽ thông minh bất thường. Kisaki thì luôn tính trước người khác vài bước.

[pause] Takemichi và Naoto từng nghi ngờ Kisaki cũng là người du hành thời gian. Kaku sẽ không nói nghi ngờ đó đúng hay sai. [pause] Nhưng đây là một bước suy luận rất hợp lý theo luật đã biết.

[pause] Ở arc Tenjiku, người em gái của Mikey là Emma trở thành nạn nhân. Một mất mát mà Takemichi không kịp ngăn, và nó đẩy Mikey tới gần bóng tối hơn bao giờ hết.

[pause] Cái giá: một kẻ thù thông minh thì cũng thích nghi. Mỗi lần gốc rễ bị cắt ở chỗ này, nó lại mọc ra ở chỗ khác, kéo theo những bi kịch mới, như arc Tenjiku.
```

### c07 · Cách phá 4: thay đổi con người, không chỉ sự kiện / Cách phá 5: niềm tin

Khoảng 128 giây · cảnh s58–s68 · 1661 ký tự

**Gemini**

```text
Cách phá thứ tư là cách Kaku thấy tinh tế nhất. Takemichi dần hiểu rằng cứu một người khỏi một sự kiện là chưa đủ. Anh phải thay đổi điều bên trong những con người ấy.

<short pause> Mikey mạnh nhất, được mọi người tôn thờ, nhưng mỗi lần mất một người thân, cậu lại tối đi một chút. Ở tương lai, Mikey luôn là người đứng cuối cùng một mình.

<short pause> Draken từng nói với Takemichi rằng Mikey cần có người bên cạnh. Mikey mạnh tới mức không ai nghĩ cậu cần được bảo vệ. Kaku thấy điểm này giống Gojo ở video trước một cách lạ lùng.

<short pause> Vì vậy mục tiêu thật của Takemichi dần chuyển từ cứu Hina sang cứu cả Mikey. Không phải khỏi kẻ thù, mà khỏi sự cô độc và bóng tối trong chính cậu.

<short pause> Cái giá: đây là cách khó nhất, vì con người không thay đổi bằng một cú đấm hay một thông tin mật. Và luật một lần vẫn còn đó: sai một bước là mất mãi.

<short pause> Cách phá cuối cùng không nằm trong luật nào cả. Takemichi không mạnh, không thông minh bằng Kisaki. Thứ anh có là việc không bao giờ bỏ rơi ai.

<short pause> Có một biệt danh người ta dành cho anh: anh hùng hay khóc. Nghe như trêu, nhưng trong thế giới đó, dám khóc mà vẫn đứng dậy lại là điều hiếm nhất.

<short pause> Nhiều người trong băng bắt đầu đi theo anh không phải vì anh đánh thắng, mà vì anh đứng dậy. Chifuyu, người bạn thân nhất, chọn tin anh khi chẳng ai tin.

<short pause> Và nhìn lại, cả bốn cách phá trước đều cần người khác: Naoto để điều tra, cả băng để thay đổi từ bên trong, bạn bè để tìm ra gốc rễ, và Mikey để có ai đó cần được cứu.

<short pause> Kaku thấy đây là cách truyện trả lời câu hỏi lớn: một khả năng yếu tới vậy thì làm sao thắng được số phận? Bằng cách không làm một mình.

<short pause> Cái giá: niềm tin là thứ dễ vỡ nhất. Nếu Takemichi thất bại, không chỉ anh mất tất cả, mà cả những người đã tin anh.
```

**ElevenLabs**

```text
Cách phá thứ tư là cách Kaku thấy tinh tế nhất. Takemichi dần hiểu rằng cứu một người khỏi một sự kiện là chưa đủ. Anh phải thay đổi điều bên trong những con người ấy.

[pause] Mikey mạnh nhất, được mọi người tôn thờ, nhưng mỗi lần mất một người thân, cậu lại tối đi một chút. Ở tương lai, Mikey luôn là người đứng cuối cùng một mình.

[pause] Draken từng nói với Takemichi rằng Mikey cần có người bên cạnh. Mikey mạnh tới mức không ai nghĩ cậu cần được bảo vệ. Kaku thấy điểm này giống Gojo ở video trước một cách lạ lùng.

[pause] Vì vậy mục tiêu thật của Takemichi dần chuyển từ cứu Hina sang cứu cả Mikey. Không phải khỏi kẻ thù, mà khỏi sự cô độc và bóng tối trong chính cậu.

[pause] Cái giá: đây là cách khó nhất, vì con người không thay đổi bằng một cú đấm hay một thông tin mật. Và luật một lần vẫn còn đó: sai một bước là mất mãi.

[pause] Cách phá cuối cùng không nằm trong luật nào cả. Takemichi không mạnh, không thông minh bằng Kisaki. Thứ anh có là việc không bao giờ bỏ rơi ai.

[pause] Có một biệt danh người ta dành cho anh: anh hùng hay khóc. Nghe như trêu, nhưng trong thế giới đó, dám khóc mà vẫn đứng dậy lại là điều hiếm nhất.

[pause] Nhiều người trong băng bắt đầu đi theo anh không phải vì anh đánh thắng, mà vì anh đứng dậy. Chifuyu, người bạn thân nhất, chọn tin anh khi chẳng ai tin.

[pause] Và nhìn lại, cả bốn cách phá trước đều cần người khác: Naoto để điều tra, cả băng để thay đổi từ bên trong, bạn bè để tìm ra gốc rễ, và Mikey để có ai đó cần được cứu.

[pause] [curious] Kaku thấy đây là cách truyện trả lời câu hỏi lớn: một khả năng yếu tới vậy thì làm sao thắng được số phận? Bằng cách không làm một mình.

[pause] Cái giá: niềm tin là thứ dễ vỡ nhất. Nếu Takemichi thất bại, không chỉ anh mất tất cả, mà cả những người đã tin anh.
```

### c08 · Bảng tổng kết / Góc nhìn của Kaku: vì sao luật yếu lại hay / Kết

Khoảng 151 giây · cảnh s69–s83 · 1967 ký tự

**Gemini**

```text
Giờ ghép tất cả vào một bảng. Cột trái là luật, cột phải là cách phá và cái giá.

<short pause> Luật đúng mười hai năm, không tua lại: phá bằng cách biến tương lai thành cuốn sổ ghi chép. Cái giá là thông tin luôn trễ.

<short pause> Luật bắt tay với Naoto: biến một cánh cửa thành một cộng sự. Cái giá là mọi thứ phụ thuộc vào an toàn của Naoto.

<short pause> Luật một người nhớ và hiệu ứng cánh bướm: phá bằng cách vào trong băng và tìm gốc rễ. Cái giá là đau thật và kẻ thù cũng thích nghi.

<short pause> Và thứ phá được mọi luật: thay đổi con người, bằng niềm tin. Cái giá là nó dễ vỡ nhất.

<short pause> Trong một video sắp tới, Kaku sẽ đặt Tokyo Revengers lên bàn so sánh với hai bộ du hành thời gian nổi tiếng khác, để xem luật của bộ nào chặt chẽ nhất.

<short pause> Nhiều bộ du hành thời gian cho nhân vật chính một khả năng gần như vô địch. Tokyo Revengers thì ngược lại: khả năng yếu, luật khắt khe, và nhân vật chính còn yếu hơn.

<short pause> Nếu Takemichi có thể quay lại bất cứ lúc nào, ta sẽ không cần anh can đảm. Chính vì anh chỉ có một cơ hội, mỗi lựa chọn của anh mới đáng giá.

<short pause> Kaku nghĩ đó chính là điểm hay. Khi cỗ máy thời gian không đủ để thắng, nhân vật buộc phải dùng những thứ không phải phép màu: can đảm, bạn bè, và sự kiên trì.

<short pause> Nếu bạn có khả năng của Takemichi, bạn sẽ quay về năm nào của mình, và sửa điều gì? Kaku tò mò lắm, viết vào bình luận nhé.

<short pause> Tokyo Revengers không thật sự kể về một cỗ máy thời gian. Nó kể về một người bình thường quyết định rằng quá khứ vẫn còn đáng để cứu.

<short pause> Takemichi không có siêu năng lực chiến đấu, không có trí tuệ thiên tài. Anh chỉ có một cái bắt tay, và quyết định không buông tay ai.

<short pause> Mùa bốn đang phát, và luật chơi sẽ còn thay đổi theo những cách mà Kaku chưa được phép kể. Xem xong mùa bốn, quay lại đây đối chiếu bảng luật này nhé.

<short pause> Video tiếp theo, Kaku leo lên tận đỉnh vũ trụ Dragon Ball để xếp hạng các vị thần, từ Kaioshin tới người mà ngay cả Thần Hủy Diệt cũng phải cúi đầu.

<short pause> <laugh> Nếu bạn thích kiểu video lập bảng luật như thế này, hãy đăng ký kênh để Kaku lập thêm nhiều bảng nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ ghép tất cả vào một bảng. Cột trái là luật, cột phải là cách phá và cái giá.

[pause] Luật đúng mười hai năm, không tua lại: phá bằng cách biến tương lai thành cuốn sổ ghi chép. Cái giá là thông tin luôn trễ.

[pause] Luật bắt tay với Naoto: biến một cánh cửa thành một cộng sự. Cái giá là mọi thứ phụ thuộc vào an toàn của Naoto.

[pause] Luật một người nhớ và hiệu ứng cánh bướm: phá bằng cách vào trong băng và tìm gốc rễ. Cái giá là đau thật và kẻ thù cũng thích nghi.

[pause] Và thứ phá được mọi luật: thay đổi con người, bằng niềm tin. Cái giá là nó dễ vỡ nhất.

[pause] Trong một video sắp tới, Kaku sẽ đặt Tokyo Revengers lên bàn so sánh với hai bộ du hành thời gian nổi tiếng khác, để xem luật của bộ nào chặt chẽ nhất.

[pause] Nhiều bộ du hành thời gian cho nhân vật chính một khả năng gần như vô địch. Tokyo Revengers thì ngược lại: khả năng yếu, luật khắt khe, và nhân vật chính còn yếu hơn.

[pause] Nếu Takemichi có thể quay lại bất cứ lúc nào, ta sẽ không cần anh can đảm. Chính vì anh chỉ có một cơ hội, mỗi lựa chọn của anh mới đáng giá.

[pause] Kaku nghĩ đó chính là điểm hay. Khi cỗ máy thời gian không đủ để thắng, nhân vật buộc phải dùng những thứ không phải phép màu: can đảm, bạn bè, và sự kiên trì.

[pause] [curious] Nếu bạn có khả năng của Takemichi, bạn sẽ quay về năm nào của mình, và sửa điều gì? Kaku tò mò lắm, viết vào bình luận nhé.

[pause] Tokyo Revengers không thật sự kể về một cỗ máy thời gian. Nó kể về một người bình thường quyết định rằng quá khứ vẫn còn đáng để cứu.

[pause] Takemichi không có siêu năng lực chiến đấu, không có trí tuệ thiên tài. Anh chỉ có một cái bắt tay, và quyết định không buông tay ai.

[pause] Mùa bốn đang phát, và luật chơi sẽ còn thay đổi theo những cách mà Kaku chưa được phép kể. Xem xong mùa bốn, quay lại đây đối chiếu bảng luật này nhé.

[pause] Video tiếp theo, Kaku leo lên tận đỉnh vũ trụ Dragon Ball để xếp hạng các vị thần, từ Kaioshin tới người mà ngay cả Thần Hủy Diệt cũng phải cúi đầu.

[pause] [chuckles] Nếu bạn thích kiểu video lập bảng luật như thế này, hãy đăng ký kênh để Kaku lập thêm nhiều bảng nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
