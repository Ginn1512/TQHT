# Bộ prompt · My Hero Academia: Cây phả hệ One For All — 9 người kế thừa và một nhánh bị mất

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 11 đoạn đọc, khoảng 16.2 phút giọng.
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

Lời: Cảnh báo: video có spoiler toàn bộ My Hero Academia, bao gồm cả cái kết của manga và mùa anime cuối cùng. Nếu…

```text
Wide 16:9 landscape cinematic frame. a quiet hero academy rooftop at sunset with a closed notebook resting on the railing, wide establishing shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Có một sức mạnh không sinh ra cùng ai cả. Nó được trao tay, từ người này sang người khác, qua chín thế hệ. Mỗ…

```text
Wide 16:9 landscape cinematic frame. a single glowing flame being passed from hand to hand across a long line of silhouettes stretching into the past, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Sức mạnh đó tên là One For All. Và cây phả hệ của nó không phải cây phả hệ theo huyết thống, mà là cây phả hệ…

```text
Wide 16:9 landscape cinematic frame. a glowing tree whose branches are made of light and whose leaves are small human silhouettes, wide shot, magical warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng cây nào cũng có rễ, và rễ của One For All mọc lên từ một cuộc chiến giữa hai anh em ruột.

```text
Wide 16:9 landscape cinematic frame. the roots of a glowing tree splitting into two twisted directions deep underground, one bright and one dark, cross-section illustration. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: My Hero Academia là manga của tác giả Horikoshi Kohei, đăng trên Shonen Jump từ năm 2014 tới 2024. Anime chạy…

```text
Wide 16:9 landscape cinematic frame. a long row of manga volumes on a shelf ending with a final volume, a small hero figurine beside it, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ One For All: từ gốc, qua chín nhánh, tới những nhánh b…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a large blank parchment and dipping a quill into ink, ready to draw a tree. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Và Kaku sẽ chỉ ra một điều mà nhiều người không để ý: cây phả hệ này giao nhau với một cây phả hệ khác theo c…

```text
Wide 16:9 landscape cinematic frame. two tree diagrams on parchment with one branch from each crossing over the other, a small red mark at the intersection, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08 · Gốc cây: hai anh em

Lời: Ngày xưa, khi siêu năng lực, hay còn gọi là quirk, bắt đầu xuất hiện ở loài người, xã hội rơi vào hỗn loạn. T…

```text
Wide 16:9 landscape cinematic frame. a chaotic city in an early era of superpowers, fires and strange lights in the streets, a calm dark figure watching from a rooftop, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Hắn không chỉ mạnh. Hắn có sức hút, biết thao túng, và thu phục những người bị xã hội bỏ rơi. Trong thời loạn…

```text
Wide 16:9 landscape cinematic frame. a charismatic dark figure standing on a stage in a shadowy hall, many lost people gathered at his feet looking up, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Hắn được gọi là All For One, và hắn trở thành kẻ thống trị thế giới ngầm. Hắn có một người em trai, Yoichi, m…

```text
Wide 16:9 landscape cinematic frame. two brothers silhouettes, one tall and imposing in a dark suit, one small and frail beside him, back view, dim cold light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: All For One ép em trai nhận một năng lực đặc biệt: năng lực tích trữ sức mạnh. Hắn nghĩ mình đang cho em một…

```text
Wide 16:9 landscape cinematic frame. a large hand pressing a small glowing orb into a frail young man's chest, dramatic close-up, cold and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Năng lực truyền đi của Yoichi nhỏ tới mức không ai, kể cả chính ông, biết tới nó. Nó chỉ lộ ra khi được trộn…

```text
Wide 16:9 landscape cinematic frame. a tiny, almost invisible spark hidden inside a frail palm, only glowing when a second light approaches, extreme close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhưng thật ra Yoichi có một năng lực ẩn: năng lực truyền đi. Hai năng lực hòa vào nhau, tạo thành một thứ hoà…

```text
Wide 16:9 landscape cinematic frame. two small streams of light, one gathering and one flowing outward, merging into a single spiraling flame, close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Đó là hạt giống của One For All. Và ngay từ đầu, nó được tạo ra để chống lại chính người đã vô tình tạo ra nó.

```text
Wide 16:9 landscape cinematic frame. a single glowing seed planted in dark soil beneath the shadow of a looming figure, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: gốc của cây này là một câu chuyện gia đình. Một người anh muốn sở hữu tất cả, và một người em c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing two names on opposite sides of a page, one surrounded by grabbing arrows and one by giving arrows. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Luật của cây

Lời: Trước khi đi qua các nhánh, cần biết luật của cây. Luật một: sức mạnh được truyền bằng cách người nhận hấp th…

```text
Wide 16:9 landscape cinematic frame. a single strand of hair glowing faintly in an open palm, extreme close-up, soft golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Luật hai: mỗi thế hệ, sức mạnh tích trữ thêm và lớn dần. Người sau luôn nhận được nhiều hơn người trước.

```text
Wide 16:9 landscape cinematic frame. a series of glowing vessels in a row, each one filled higher than the last, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Những bóng hình này không phải hồn ma. Chúng là dấu vết ý chí được lưu lại cùng sức mạnh, và mỗi người còn gi…

```text
Wide 16:9 landscape cinematic frame. a circle of translucent silhouettes seated around a glowing flame in a misty space, each with a different posture, wide shot, ethereal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Luật ba: những người cũ để lại một phần ý thức bên trong, gọi là bóng hình. Họ có thể xuất hiện, nói chuyện,…

```text
Wide 16:9 landscape cinematic frame. a young man standing in a misty inner space surrounded by faint translucent silhouettes of past holders, wide shot, ethereal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng để dùng được năng lực của người cũ, Deku phải được họ chấp nhận, và cơ thể phải đủ mạnh. Mỗi năng lực m…

```text
Wide 16:9 landscape cinematic frame. a young man straining as a new dark tendril power bursts uncontrolled from his arm, dramatic close-up, harsh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Luật bốn, được hé lộ khá muộn: năng lực riêng của những người cũ cũng được giữ lại bên trong, và người kế thừ…

```text
Wide 16:9 landscape cinematic frame. several small glowing icons orbiting a single flame: a whip, a floating feather, a smoke puff, an eye, a gear, parchment illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Và có một luật ngầm đáng sợ hơn: sức mạnh quá lớn có thể làm người giữ nó chết sớm, nhất là những người vốn đ…

```text
Wide 16:9 landscape cinematic frame. an hourglass with sand running faster than normal beside a glowing flame, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Nhánh 1 tới 3: những người đầu tiên

Lời: Nhánh một: Yoichi Shigaraki, người đầu tiên. Ông không đủ sức đánh bại anh trai, nên ông truyền sức mạnh đi,…

```text
Wide 16:9 landscape cinematic frame. a frail young man handing a small glowing flame to another person in a dark alley, both looking over their shoulders, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Người thứ hai trở thành người dẫn dắt các bóng hình, người nói chuyện nhiều nhất với Deku. Ông từng là một ng…

```text
Wide 16:9 landscape cinematic frame. a bold young silhouette standing at the front of a group of faint figures, arms crossed, facing a young hero, medium shot, misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nhánh hai: người sử dụng thứ hai, có năng lực tăng giảm tốc độ, như sang số của một cỗ máy.

```text
Wide 16:9 landscape cinematic frame. a figure with gear-shaped light patterns spinning around their legs as they accelerate, dynamic shot, amber light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nhánh ba: người sử dụng thứ ba, có năng lực tích động năng rồi giải phóng một lúc để tăng tốc. Cả ba người đầ…

```text
Wide 16:9 landscape cinematic frame. a figure crouched like a coiled spring releasing a burst of stored energy, dynamic close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Yoichi, người đầu tiên, về sau là bóng hình đặc biệt nhất. Ông thường xuất hiện ở những khoảnh khắc quan trọn…

```text
Wide 16:9 landscape cinematic frame. a frail faint figure standing slightly apart from the other silhouettes, looking at a young hero with gentle eyes, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Và cả ba đều không thắng được All For One. Họ chỉ có thể sống sót đủ lâu để truyền sức mạnh đi. Mỗi lần trao…

```text
Wide 16:9 landscape cinematic frame. a relay baton made of light passed from a falling runner to the next in a dark stadium, dramatic wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Kaku để ý: những nhánh đầu tiên của cây gần như không có tên trong truyện một thời gian dài. Họ là những ngườ…

```text
Wide 16:9 landscape cinematic frame. three faded silhouettes on an old photograph with their faces blurred, close-up, sepia light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Nhánh 4 tới 6: những người đứng giữa

Lời: Nhánh bốn: Shinomori Hikage, năng lực cảm nhận nguy hiểm. Ông già đi rất nhanh, và mất khi còn khá trẻ.

```text
Wide 16:9 landscape cinematic frame. a gaunt figure with prematurely grey hair sitting alone, faint warning pulses radiating around his head, medium shot, dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Banjo là người ồn ào và nhiệt huyết nhất trong các bóng hình. Năng lực roi đen của ông là năng lực đầu tiên D…

```text
Wide 16:9 landscape cinematic frame. a burly cheerful silhouette laughing loudly among quieter faint figures, dark tendrils flickering at his hands, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nhánh năm: Banjo Daigoro, năng lực roi đen, những sợi năng lượng đen có thể quấn, kéo, trói.

```text
Wide 16:9 landscape cinematic frame. dark energy tendrils whipping out from a burly figure's arms and wrapping around a steel beam, dynamic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Nghe thì khói có vẻ không mạnh bằng roi hay bay. Nhưng trong chiến đấu, che mắt kẻ thù đôi khi quyết định sốn…

```text
Wide 16:9 landscape cinematic frame. a young hero using a dark smoke cloud to shield injured civilians while escaping, wide shot, tense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nhánh sáu: En, năng lực tạo khói, giúp ẩn nấp và gây rối. Ông cũng là người đã chiến đấu và hi sinh trước All…

```text
Wide 16:9 landscape cinematic frame. a figure disappearing into a thick cloud of dark smoke in a ruined alley, wide shot, eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Cảm nhận nguy hiểm của Shinomori về sau trở thành một trong những năng lực Deku dùng nhiều nhất, như một hệ t…

```text
Wide 16:9 landscape cinematic frame. a faint warning pulse radiating around a young hero's head as a hidden attack approaches from behind, dynamic close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Ba nhánh này có điểm chung: đều đối đầu trực tiếp với All For One hoặc thuộc hạ của hắn, và đều không sống lâ…

```text
Wide 16:9 landscape cinematic frame. a tree trunk with three carved notches near its middle, rain running down the bark, close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thật: sau này khi Deku đánh thức năng lực của họ, Kaku mới hiểu vì sao tác giả để các nhánh giữ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot fitting three small puzzle pieces into a larger picture, nodding thoughtfully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Nhánh 7: Nana Shimura

Lời: Nhánh bảy: Shimura Nana, năng lực bay lơ lửng. Bà là một anh hùng chuyên nghiệp mạnh mẽ, vui tính, và là ngườ…

```text
Wide 16:9 landscape cinematic frame. a confident woman in a hero cape floating calmly above a city skyline at sunset, low-angle shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nana dạy Toshinori một điều quan trọng hơn mọi kỹ thuật: hãy luôn mỉm cười. Anh hùng mỉm cười để người khác b…

```text
Wide 16:9 landscape cinematic frame. a woman and a young man both grinning widely on a rooftop, the city behind them, medium shot, bright warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Nụ cười nổi tiếng của All Might, thứ mà cả thế giới nhớ tới, thật ra là bài học của người thầy. Cây phả hệ nà…

```text
Wide 16:9 landscape cinematic frame. a small smile drawn on a notebook page passed between two hands, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Bà nhìn thấy ở một cậu thanh niên không có năng lực, Yagi Toshinori, điều mà người khác không thấy: một trái…

```text
Wide 16:9 landscape cinematic frame. a woman placing her hand on the shoulder of a thin young man looking at a city from a rooftop, back view, soft evening light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Để bảo vệ gia đình, bà đã gửi con trai mình đi, cắt đứt liên lạc, để All For One không thể dùng đứa bé làm co…

```text
Wide 16:9 landscape cinematic frame. a small child being handed to a foster family at a doorway, a woman walking away in the rain without looking back, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Người bạn thân của bà, một anh hùng già tên Gran Torino, sau đó tiếp tục huấn luyện Toshinori, và nhiều năm s…

```text
Wide 16:9 landscape cinematic frame. a short elderly hero in a cape bouncing energetically off walls while a young student struggles to keep up, humorous dynamic shot, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và rồi bà hi sinh trong trận chiến với All For One. Lựa chọn gửi con đi, tưởng là để bảo vệ, về sau lại trở t…

```text
Wide 16:9 landscape cinematic frame. a torn hero cape caught on a broken railing, blowing in the wind, extreme close-up, grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45 · Nhánh 8: All Might

Lời: Nhánh tám: Yagi Toshinori, All Might. Người đầu tiên trong cây không có năng lực riêng nào, và cũng là người…

```text
Wide 16:9 landscape cinematic frame. a towering muscular hero silhouette standing in front of a crowd with arms raised, sunlight behind him, low-angle shot, heroic golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Vì không có năng lực riêng, cơ thể ông không phải gánh hai sức mạnh cùng lúc. Nhiều người cho rằng đó là lý d…

```text
Wide 16:9 landscape cinematic frame. a single empty vessel receiving a large flame without any other contents, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng khi hết sức, All Might trở lại dáng vẻ gầy gò, ho ra máu. Thế giới không biết. Chỉ vài người thân cận b…

```text
Wide 16:9 landscape cinematic frame. a thin gaunt man sitting alone in a dim room, a giant hero poster of himself on the wall behind him, medium shot, melancholic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ông trở thành Biểu tượng Hòa bình, người mà sự có mặt thôi cũng khiến tội phạm chùn tay. Và ông đã đánh bại A…

```text
Wide 16:9 landscape cinematic frame. a hero silhouette standing victorious in a destroyed city, one hand clutching his side, dust settling, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Ở trận chiến Kamino, All Might dùng chút lửa cuối cùng để đánh bại All For One lần nữa. Rồi ông chỉ tay vào ố…

```text
Wide 16:9 landscape cinematic frame. a gaunt hero pointing forward toward the viewer in a smoky destroyed city, flashes of news cameras around, dramatic low-angle shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Vết thương khiến thời gian ông ở dạng anh hùng ngày càng ngắn lại. Ông cần người kế nhiệm, và ông tìm thấy ng…

```text
Wide 16:9 landscape cinematic frame. a skinny boy running toward danger with his backpack flying, while adult heroes hesitate in the background, dynamic wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · Nhánh 9: Midoriya Izuku

Lời: Từ nhỏ Deku đã bị bác sĩ nói là không có năng lực, và bị bạn bè coi thường. Nhưng cậu có một thói quen: ghi c…

```text
Wide 16:9 landscape cinematic frame. a stack of worn notebooks filled with hero sketches and notes on a child's desk, one slightly burnt at the edges, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói: Kaku rất có cảm tình với một nhân vật chính mê ghi chép. Nếu Deku có kênh YouTube, chắc là đối…

```text
Wide 16:9 landscape cinematic frame. the owl mascot comparing its own notebook with a similar notebook, nodding with respect. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nhánh chín: Midoriya Izuku, Deku. Cậu nuốt sợi tóc của All Might và nhận One For All. Sức mạnh quá lớn, lần đ…

```text
Wide 16:9 landscape cinematic frame. a boy holding his injured arm after a massive punch that cleared the clouds above him, wide shot, dramatic sky. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Cậu còn đổi cách chiến đấu: chuyển từ đấm sang đá, để tay không bị hỏng thêm. Mỗi lần thích nghi là một lần c…

```text
Wide 16:9 landscape cinematic frame. a young hero switching from a punch to a powerful kick in midair, glowing lines around his legs, dynamic shot, bright light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Cậu học cách dùng từng phần trăm sức mạnh: năm phần trăm, tám phần trăm, hai mươi phần trăm, để cơ thể không…

```text
Wide 16:9 landscape cinematic frame. a glowing percentage gauge drawn beside a young fighter, the needle carefully held at a low value, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Rồi những bóng hình người cũ bắt đầu thức tỉnh. Deku lần lượt dùng được roi đen, khói, bay lơ lửng, cảm nhận…

```text
Wide 16:9 landscape cinematic frame. a young hero surrounded by faint silhouettes of past holders, each lending a different glowing power to him, wide shot, epic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Deku là người cuối cùng của cây. Theo truyện, cậu là nhánh được chọn để kết thúc cuộc chiến bắt đầu từ hai an…

```text
Wide 16:9 landscape cinematic frame. the top of a glowing tree with a single bright leaf at its tip, wide shot, dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Nhánh bị mất: dòng họ Shimura

Lời: Giờ tới nhánh bi kịch nhất. Con trai của Nana Shimura lớn lên không biết mẹ mình là ai, và căm ghét anh hùng…

```text
Wide 16:9 landscape cinematic frame. a stern man standing in a dim living room with his back to a small boy, a hero poster torn on the wall, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cậu bé từng mơ làm anh hùng, như bà mình. Nhưng không ai tới cứu cậu vào đêm hôm đó. Đó là vết thương lớn nhấ…

```text
Wide 16:9 landscape cinematic frame. a small boy walking alone along a busy street at night, adults passing by without looking down at him, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Cháu của Nana, cậu bé Shimura Tenko, lớn lên trong một gia đình cấm nhắc tới anh hùng. Một ngày, năng lực phâ…

```text
Wide 16:9 landscape cinematic frame. a small boy standing alone in a ruined garden at night, crumbling dust drifting from his hands, wide shot, eerie cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Deku về sau hiểu ra rằng mình muốn cứu cả Shigaraki, không chỉ đánh bại hắn. Nhánh cây bị mất cuối cùng cũng…

```text
Wide 16:9 landscape cinematic frame. a young hero reaching out his hand toward a figure surrounded by crumbling dust, dramatic close-up, contrasting warm and cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: All For One tìm tới cậu bé, nuôi dạy, đổi tên cậu thành Shigaraki Tomura, và biến cậu thành kẻ thù lớn nhất c…

```text
Wide 16:9 landscape cinematic frame. a tall dark figure placing a hand on the head of a small lost boy on a rainy street, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Hãy nhìn cái tên: Shigaraki là họ của chính Yoichi, người đầu tiên của One For All. All For One lấy họ của em…

```text
Wide 16:9 landscape cinematic frame. two family trees on parchment crossing branches, the name tags at the intersection glowing red, close-up, crimson and amber ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Kaku thấy đây là chi tiết tàn nhẫn nhất của cả bộ truyện: người giữ ngọn lửa hi sinh gia đình để bảo vệ nó, v…

```text
Wide 16:9 landscape cinematic frame. a small candle flame beside a dark hand reaching toward it from the shadows, extreme close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Nhánh đối nghịch: All For One

Lời: Hắn kéo dài tuổi thọ, thay đổi cơ thể, và thậm chí tìm cách trở lại qua người khác. Một kẻ không chịu buông t…

```text
Wide 16:9 landscape cinematic frame. a clenched dark fist gripping many glowing threads next to an open hand releasing a single light, split composition, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Và ở phía đối diện của cây là All For One: kẻ sống qua nhiều thế hệ, lấy năng lực của vô số người, và luôn mu…

```text
Wide 16:9 landscape cinematic frame. a dark tree with twisted branches mirroring the glowing tree, a looming figure at its roots, split composition, cold and warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Kaku để ý: Yoichi và All For One đều là những nhân vật được nhắc tới từ đầu, nhưng mãi tới cuối truyện ta mới…

```text
Wide 16:9 landscape cinematic frame. an old photograph of two young brothers smiling together, faded and torn down the middle, close-up, sepia light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Hai sức mạnh đối lập hoàn toàn: một bên lấy mọi thứ cho một người, một bên trao một thứ cho mọi người sau. Tê…

```text
Wide 16:9 landscape cinematic frame. two symbols side by side on parchment: many arrows pointing into one point, and one point sending arrows outward, amber ink. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Và câu chuyện của cả chín thế hệ, rốt cuộc, là cuộc cãi nhau chưa dứt giữa hai anh em ruột.

```text
Wide 16:9 landscape cinematic frame. two small brothers' silhouettes sitting on opposite ends of a long bench under a single streetlight, back view, melancholic light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Cái kết của cây

Lời: Trong trận chiến cuối cùng, Deku dùng toàn bộ sức mạnh của cả cây phả hệ. Và sau đó, One For All dần tắt tron…

```text
Wide 16:9 landscape cinematic frame. a young hero standing in a devastated field at dawn as golden embers slowly drift away from his body, wide shot, bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Nhiều năm sau, All Might, người không còn năng lực, và Deku, người đã mất năng lực, đều vẫn được gọi là anh h…

```text
Wide 16:9 landscape cinematic frame. an older man and a young teacher standing side by side watching students train in a sunny yard, back view, warm hopeful light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Deku không còn sức mạnh. Nhưng truyện cho thấy cậu vẫn là anh hùng: trở thành giáo viên, rồi được bạn bè giúp…

```text
Wide 16:9 landscape cinematic frame. a young teacher standing in front of a class of eager students, a hero suit hanging in a display case behind him, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy cái kết này khép lại cây phả hệ rất đẹp: sức mạnh được trao qua chín đời để kết thúc một cuộc chiến…

```text
Wide 16:9 landscape cinematic frame. the owl mascot gently closing a book with a glowing tree on its cover, a small ember floating up from it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Cây hoàn chỉnh

Lời: Kaku vẽ lại toàn bộ cây. Gốc: hai anh em, All For One và Yoichi. Thân cây: năng lực tích trữ và truyền đi hòa…

```text
Wide 16:9 landscape cinematic frame. a complete glowing tree drawing on parchment with two roots labeled by small icons, close-up, amber ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và bên cạnh cây là những người không ở trong cây nhưng giữ cho nó sống: Gran Torino, mẹ của Deku, những người…

```text
Wide 16:9 landscape cinematic frame. small supporting figures standing around the base of the glowing tree, holding it steady with ropes of light, parchment illustration. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Chín nhánh: Yoichi, sang số, tích động năng, cảm nhận nguy hiểm, roi đen, khói, bay lơ lửng, All Might, và De…

```text
Wide 16:9 landscape cinematic frame. nine glowing branches each tipped with a small icon, arranged from bottom to top, parchment illustration. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Một nhánh bị mất: dòng họ Shimura, bị cây đối nghịch cướp đi và biến thành Shigaraki Tomura. Và ngọn cây: ý c…

```text
Wide 16:9 landscape cinematic frame. a dark broken branch hanging off the side of the tree, and a small light rising from the treetop into the sky, close-up, dramatic contrast. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Nếu được chọn một người trong chín nhánh để kể riêng một video, bạn chọn ai? Kaku nghiêng về Nana Shimura. Vi…

```text
Wide 16:9 landscape cinematic frame. nine small portrait frames on a wall with one empty frame and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Kết

Lời: Kaku mong bạn cũng có một người để truyền lại điều gì đó: một kỹ năng, một thói quen tốt, hay chỉ là một nụ c…

```text
Wide 16:9 landscape cinematic frame. two hands, one old and one young, holding a small glowing notebook together, extreme close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Cây phả hệ One For All không nối với nhau bằng máu, mà bằng lựa chọn. Mỗi người chọn trao đi, và nhờ vậy, ngọ…

```text
Wide 16:9 landscape cinematic frame. a long line of hands passing a small flame toward a bright horizon, wide shot, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Video tiếp theo, Kaku mở phòng thí nghiệm của tiến sĩ Agasa trong Thám tử lừng danh Conan: viên thuốc teo nhỏ…

```text
Wide 16:9 landscape cinematic frame. a cluttered home laboratory with strange gadgets, a small pill bottle under a desk lamp, wide shot, warm yellow light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những cây phả hệ như thế này, hãy đăng ký kênh để Kaku vẽ thêm nhiều cây nữa. Kaku gấp sổ đây,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up the parchment tree and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 77 giây · cảnh s01–s07 · 1005 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler toàn bộ My Hero Academia, bao gồm cả cái kết của manga và mùa anime cuối cùng. Nếu bạn chưa xem hết, hãy lưu video lại.

<short pause> Có một sức mạnh không sinh ra cùng ai cả. Nó được trao tay, từ người này sang người khác, qua chín thế hệ. Mỗi người nhận nó đều để lại một phần của mình bên trong.

<short pause> Sức mạnh đó tên là One For All. Và cây phả hệ của nó không phải cây phả hệ theo huyết thống, mà là cây phả hệ của những người được chọn.

<short pause> Nhưng cây nào cũng có rễ, và rễ của One For All mọc lên từ một cuộc chiến giữa hai anh em ruột.

<short pause> My Hero Academia là manga của tác giả Horikoshi Kohei, đăng trên Shonen Jump từ năm 2014 tới 2024. Anime chạy suốt gần mười năm, và mùa cuối cùng khép lại vào năm 2025.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ One For All: từ gốc, qua chín nhánh, tới những nhánh bị mất và những nhánh tối. Cuối video là cả cây trong một hình.

<short pause> Và Kaku sẽ chỉ ra một điều mà nhiều người không để ý: cây phả hệ này giao nhau với một cây phả hệ khác theo cách rất bi kịch.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler toàn bộ My Hero Academia, bao gồm cả cái kết của manga và mùa anime cuối cùng. Nếu bạn chưa xem hết, hãy lưu video lại.

[pause] Có một sức mạnh không sinh ra cùng ai cả. Nó được trao tay, từ người này sang người khác, qua chín thế hệ. Mỗi người nhận nó đều để lại một phần của mình bên trong.

[pause] Sức mạnh đó tên là One For All. Và cây phả hệ của nó không phải cây phả hệ theo huyết thống, mà là cây phả hệ của những người được chọn.

[pause] Nhưng cây nào cũng có rễ, và rễ của One For All mọc lên từ một cuộc chiến giữa hai anh em ruột.

[pause] My Hero Academia là manga của tác giả Horikoshi Kohei, đăng trên Shonen Jump từ năm 2014 tới 2024. Anime chạy suốt gần mười năm, và mùa cuối cùng khép lại vào năm 2025.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku vẽ cây phả hệ One For All: từ gốc, qua chín nhánh, tới những nhánh bị mất và những nhánh tối. Cuối video là cả cây trong một hình.

[pause] Và Kaku sẽ chỉ ra một điều mà nhiều người không để ý: cây phả hệ này giao nhau với một cây phả hệ khác theo cách rất bi kịch.
```

### c02 · Gốc cây: hai anh em

Khoảng 99 giây · cảnh s08–s15 · 1287 ký tự

**Gemini**

```text
Ngày xưa, khi siêu năng lực, hay còn gọi là quirk, bắt đầu xuất hiện ở loài người, xã hội rơi vào hỗn loạn. Trong thời loạn đó có một người đàn ông có năng lực cướp và trao năng lực của người khác.

<short pause> Hắn không chỉ mạnh. Hắn có sức hút, biết thao túng, và thu phục những người bị xã hội bỏ rơi. Trong thời loạn, hắn giống một vị vua bóng tối.

<short pause> Hắn được gọi là All For One, và hắn trở thành kẻ thống trị thế giới ngầm. Hắn có một người em trai, Yoichi, một người nhỏ bé, yếu ớt, và bị coi là không có năng lực.

<short pause> All For One ép em trai nhận một năng lực đặc biệt: năng lực tích trữ sức mạnh. Hắn nghĩ mình đang cho em một món quà, hoặc đang kiểm soát em.

<short pause> Năng lực truyền đi của Yoichi nhỏ tới mức không ai, kể cả chính ông, biết tới nó. Nó chỉ lộ ra khi được trộn với năng lực tích trữ. Một năng lực vô dụng hóa ra lại là chìa khóa.

<short pause> Nhưng thật ra Yoichi có một năng lực ẩn: năng lực truyền đi. Hai năng lực hòa vào nhau, tạo thành một thứ hoàn toàn mới: một sức mạnh có thể tích trữ và truyền từ người này sang người khác.

<short pause> Đó là hạt giống của One For All. Và ngay từ đầu, nó được tạo ra để chống lại chính người đã vô tình tạo ra nó.

<short pause> <laugh> Kaku ghi chú: gốc của cây này là một câu chuyện gia đình. Một người anh muốn sở hữu tất cả, và một người em chọn trao lại tất cả. Tên của hai sức mạnh nói lên điều đó.
```

**ElevenLabs**

```text
Ngày xưa, khi siêu năng lực, hay còn gọi là quirk, bắt đầu xuất hiện ở loài người, xã hội rơi vào hỗn loạn. Trong thời loạn đó có một người đàn ông có năng lực cướp và trao năng lực của người khác.

[pause] Hắn không chỉ mạnh. Hắn có sức hút, biết thao túng, và thu phục những người bị xã hội bỏ rơi. Trong thời loạn, hắn giống một vị vua bóng tối.

[pause] Hắn được gọi là All For One, và hắn trở thành kẻ thống trị thế giới ngầm. Hắn có một người em trai, Yoichi, một người nhỏ bé, yếu ớt, và bị coi là không có năng lực.

[pause] All For One ép em trai nhận một năng lực đặc biệt: năng lực tích trữ sức mạnh. Hắn nghĩ mình đang cho em một món quà, hoặc đang kiểm soát em.

[pause] Năng lực truyền đi của Yoichi nhỏ tới mức không ai, kể cả chính ông, biết tới nó. Nó chỉ lộ ra khi được trộn với năng lực tích trữ. Một năng lực vô dụng hóa ra lại là chìa khóa.

[pause] Nhưng thật ra Yoichi có một năng lực ẩn: năng lực truyền đi. Hai năng lực hòa vào nhau, tạo thành một thứ hoàn toàn mới: một sức mạnh có thể tích trữ và truyền từ người này sang người khác.

[pause] Đó là hạt giống của One For All. Và ngay từ đầu, nó được tạo ra để chống lại chính người đã vô tình tạo ra nó.

[pause] [chuckles] Kaku ghi chú: gốc của cây này là một câu chuyện gia đình. Một người anh muốn sở hữu tất cả, và một người em chọn trao lại tất cả. Tên của hai sức mạnh nói lên điều đó.
```

### c03 · Luật của cây

Khoảng 83 giây · cảnh s16–s22 · 1077 ký tự

**Gemini**

```text
Trước khi đi qua các nhánh, cần biết luật của cây. Luật một: sức mạnh được truyền bằng cách người nhận hấp thụ ADN của người trao, ví dụ nuốt một sợi tóc.

<short pause> Luật hai: mỗi thế hệ, sức mạnh tích trữ thêm và lớn dần. Người sau luôn nhận được nhiều hơn người trước.

<short pause> Những bóng hình này không phải hồn ma. Chúng là dấu vết ý chí được lưu lại cùng sức mạnh, và mỗi người còn giữ tính cách riêng: có người ít nói, có người nóng nảy, có người rất vui tính.

<short pause> Luật ba: những người cũ để lại một phần ý thức bên trong, gọi là bóng hình. Họ có thể xuất hiện, nói chuyện, và dẫn dắt người đang giữ sức mạnh.

<short pause> Nhưng để dùng được năng lực của người cũ, Deku phải được họ chấp nhận, và cơ thể phải đủ mạnh. Mỗi năng lực mới đến vào đúng lúc cậu cần nó nhất, và cũng khiến cậu kiệt sức hơn.

<short pause> Luật bốn, được hé lộ khá muộn: năng lực riêng của những người cũ cũng được giữ lại bên trong, và người kế thừa có thể dần đánh thức chúng.

<short pause> Và có một luật ngầm đáng sợ hơn: sức mạnh quá lớn có thể làm người giữ nó chết sớm, nhất là những người vốn đã có năng lực riêng. Kaku gắn nhãn cần kiểm lại cho chi tiết này.
```

**ElevenLabs**

```text
Trước khi đi qua các nhánh, cần biết luật của cây. Luật một: sức mạnh được truyền bằng cách người nhận hấp thụ ADN của người trao, ví dụ nuốt một sợi tóc.

[pause] Luật hai: mỗi thế hệ, sức mạnh tích trữ thêm và lớn dần. Người sau luôn nhận được nhiều hơn người trước.

[pause] Những bóng hình này không phải hồn ma. Chúng là dấu vết ý chí được lưu lại cùng sức mạnh, và mỗi người còn giữ tính cách riêng: có người ít nói, có người nóng nảy, có người rất vui tính.

[pause] Luật ba: những người cũ để lại một phần ý thức bên trong, gọi là bóng hình. Họ có thể xuất hiện, nói chuyện, và dẫn dắt người đang giữ sức mạnh.

[pause] Nhưng để dùng được năng lực của người cũ, Deku phải được họ chấp nhận, và cơ thể phải đủ mạnh. Mỗi năng lực mới đến vào đúng lúc cậu cần nó nhất, và cũng khiến cậu kiệt sức hơn.

[pause] Luật bốn, được hé lộ khá muộn: năng lực riêng của những người cũ cũng được giữ lại bên trong, và người kế thừa có thể dần đánh thức chúng.

[pause] Và có một luật ngầm đáng sợ hơn: sức mạnh quá lớn có thể làm người giữ nó chết sớm, nhất là những người vốn đã có năng lực riêng. Kaku gắn nhãn cần kiểm lại cho chi tiết này.
```

### c04 · Nhánh 1 tới 3: những người đầu tiên

Khoảng 83 giây · cảnh s23–s29 · 1078 ký tự

**Gemini**

```text
Nhánh một: Yoichi Shigaraki, người đầu tiên. Ông không đủ sức đánh bại anh trai, nên ông truyền sức mạnh đi, gửi gắm hy vọng vào người sau.

<short pause> Người thứ hai trở thành người dẫn dắt các bóng hình, người nói chuyện nhiều nhất với Deku. Ông từng là một người trẻ nổi loạn chống lại All For One từ những ngày đầu.

<short pause> Nhánh hai: người sử dụng thứ hai, có năng lực tăng giảm tốc độ, như sang số của một cỗ máy.

<short pause> Nhánh ba: người sử dụng thứ ba, có năng lực tích động năng rồi giải phóng một lúc để tăng tốc. Cả ba người đầu đều sống trong thời kỳ All For One còn ở đỉnh cao.

<short pause> Yoichi, người đầu tiên, về sau là bóng hình đặc biệt nhất. Ông thường xuất hiện ở những khoảnh khắc quan trọng, nhìn người em cuối cùng của cây phả hệ bằng ánh mắt vừa buồn vừa hy vọng.

<short pause> Và cả ba đều không thắng được All For One. Họ chỉ có thể sống sót đủ lâu để truyền sức mạnh đi. Mỗi lần trao tay là một lần thua, nhưng cũng là một lần hy vọng được giữ lại.

<short pause> Kaku để ý: những nhánh đầu tiên của cây gần như không có tên trong truyện một thời gian dài. Họ là những người hùng vô danh, và bộ truyện mất rất lâu mới kể về họ.
```

**ElevenLabs**

```text
Nhánh một: Yoichi Shigaraki, người đầu tiên. Ông không đủ sức đánh bại anh trai, nên ông truyền sức mạnh đi, gửi gắm hy vọng vào người sau.

[pause] Người thứ hai trở thành người dẫn dắt các bóng hình, người nói chuyện nhiều nhất với Deku. Ông từng là một người trẻ nổi loạn chống lại All For One từ những ngày đầu.

[pause] Nhánh hai: người sử dụng thứ hai, có năng lực tăng giảm tốc độ, như sang số của một cỗ máy.

[pause] Nhánh ba: người sử dụng thứ ba, có năng lực tích động năng rồi giải phóng một lúc để tăng tốc. Cả ba người đầu đều sống trong thời kỳ All For One còn ở đỉnh cao.

[pause] Yoichi, người đầu tiên, về sau là bóng hình đặc biệt nhất. Ông thường xuất hiện ở những khoảnh khắc quan trọng, nhìn người em cuối cùng của cây phả hệ bằng ánh mắt vừa buồn vừa hy vọng.

[pause] Và cả ba đều không thắng được All For One. Họ chỉ có thể sống sót đủ lâu để truyền sức mạnh đi. Mỗi lần trao tay là một lần thua, nhưng cũng là một lần hy vọng được giữ lại.

[pause] Kaku để ý: những nhánh đầu tiên của cây gần như không có tên trong truyện một thời gian dài. Họ là những người hùng vô danh, và bộ truyện mất rất lâu mới kể về họ.
```

### c05 · Nhánh 4 tới 6: những người đứng giữa

Khoảng 87 giây · cảnh s30–s37 · 1133 ký tự

**Gemini**

```text
Nhánh bốn: Shinomori Hikage, năng lực cảm nhận nguy hiểm. Ông già đi rất nhanh, và mất khi còn khá trẻ.

<short pause> Banjo là người ồn ào và nhiệt huyết nhất trong các bóng hình. Năng lực roi đen của ông là năng lực đầu tiên Deku đánh thức, và cũng khó điều khiển nhất lúc ban đầu.

<short pause> Nhánh năm: Banjo Daigoro, năng lực roi đen, những sợi năng lượng đen có thể quấn, kéo, trói.

<short pause> Nghe thì khói có vẻ không mạnh bằng roi hay bay. <short pause> Nhưng trong chiến đấu, che mắt kẻ thù đôi khi quyết định sống chết. Cây phả hệ này cần cả những năng lực không hào nhoáng.

<short pause> Nhánh sáu: En, năng lực tạo khói, giúp ẩn nấp và gây rối. Ông cũng là người đã chiến đấu và hi sinh trước All For One.

<short pause> Cảm nhận nguy hiểm của Shinomori về sau trở thành một trong những năng lực Deku dùng nhiều nhất, như một hệ thống cảnh báo sớm gắn trong đầu.

<short pause> Ba nhánh này có điểm chung: đều đối đầu trực tiếp với All For One hoặc thuộc hạ của hắn, và đều không sống lâu. Cây One For All lớn lên trên những mất mát.

<short pause> <laugh> Kaku phải nói thật: sau này khi Deku đánh thức năng lực của họ, Kaku mới hiểu vì sao tác giả để các nhánh giữa này có năng lực rất khác nhau. Mỗi người là một mảnh ghép cho người cuối cùng.
```

**ElevenLabs**

```text
Nhánh bốn: Shinomori Hikage, năng lực cảm nhận nguy hiểm. Ông già đi rất nhanh, và mất khi còn khá trẻ.

[pause] Banjo là người ồn ào và nhiệt huyết nhất trong các bóng hình. Năng lực roi đen của ông là năng lực đầu tiên Deku đánh thức, và cũng khó điều khiển nhất lúc ban đầu.

[pause] Nhánh năm: Banjo Daigoro, năng lực roi đen, những sợi năng lượng đen có thể quấn, kéo, trói.

[pause] Nghe thì khói có vẻ không mạnh bằng roi hay bay. [pause] Nhưng trong chiến đấu, che mắt kẻ thù đôi khi quyết định sống chết. Cây phả hệ này cần cả những năng lực không hào nhoáng.

[pause] Nhánh sáu: En, năng lực tạo khói, giúp ẩn nấp và gây rối. Ông cũng là người đã chiến đấu và hi sinh trước All For One.

[pause] Cảm nhận nguy hiểm của Shinomori về sau trở thành một trong những năng lực Deku dùng nhiều nhất, như một hệ thống cảnh báo sớm gắn trong đầu.

[pause] Ba nhánh này có điểm chung: đều đối đầu trực tiếp với All For One hoặc thuộc hạ của hắn, và đều không sống lâu. Cây One For All lớn lên trên những mất mát.

[pause] [chuckles] Kaku phải nói thật: sau này khi Deku đánh thức năng lực của họ, Kaku mới hiểu vì sao tác giả để các nhánh giữa này có năng lực rất khác nhau. Mỗi người là một mảnh ghép cho người cuối cùng.
```

### c06 · Nhánh 7: Nana Shimura

Khoảng 77 giây · cảnh s38–s44 · 1006 ký tự

**Gemini**

```text
Nhánh bảy: Shimura Nana, năng lực bay lơ lửng. Bà là một anh hùng chuyên nghiệp mạnh mẽ, vui tính, và là người thầy của All Might.

<short pause> Nana dạy Toshinori một điều quan trọng hơn mọi kỹ thuật: hãy luôn mỉm cười. Anh hùng mỉm cười để người khác bớt sợ, và để chính mình không gục ngã.

<short pause> Nụ cười nổi tiếng của All Might, thứ mà cả thế giới nhớ tới, thật ra là bài học của người thầy. Cây phả hệ này truyền cả sức mạnh lẫn nụ cười.

<short pause> Bà nhìn thấy ở một cậu thanh niên không có năng lực, Yagi Toshinori, điều mà người khác không thấy: một trái tim sẵn sàng cứu người bằng mọi giá.

<short pause> Để bảo vệ gia đình, bà đã gửi con trai mình đi, cắt đứt liên lạc, để All For One không thể dùng đứa bé làm con tin.

<short pause> Người bạn thân của bà, một anh hùng già tên Gran Torino, sau đó tiếp tục huấn luyện Toshinori, và nhiều năm sau còn huấn luyện cả Deku. Những người không giữ ngọn lửa cũng góp phần bảo vệ nó.

<short pause> Và rồi bà hi sinh trong trận chiến với All For One. Lựa chọn gửi con đi, tưởng là để bảo vệ, về sau lại trở thành một nhánh cây rất tối.
```

**ElevenLabs**

```text
Nhánh bảy: Shimura Nana, năng lực bay lơ lửng. Bà là một anh hùng chuyên nghiệp mạnh mẽ, vui tính, và là người thầy của All Might.

[pause] Nana dạy Toshinori một điều quan trọng hơn mọi kỹ thuật: hãy luôn mỉm cười. Anh hùng mỉm cười để người khác bớt sợ, và để chính mình không gục ngã.

[pause] Nụ cười nổi tiếng của All Might, thứ mà cả thế giới nhớ tới, thật ra là bài học của người thầy. Cây phả hệ này truyền cả sức mạnh lẫn nụ cười.

[pause] Bà nhìn thấy ở một cậu thanh niên không có năng lực, Yagi Toshinori, điều mà người khác không thấy: một trái tim sẵn sàng cứu người bằng mọi giá.

[pause] Để bảo vệ gia đình, bà đã gửi con trai mình đi, cắt đứt liên lạc, để All For One không thể dùng đứa bé làm con tin.

[pause] Người bạn thân của bà, một anh hùng già tên Gran Torino, sau đó tiếp tục huấn luyện Toshinori, và nhiều năm sau còn huấn luyện cả Deku. Những người không giữ ngọn lửa cũng góp phần bảo vệ nó.

[pause] Và rồi bà hi sinh trong trận chiến với All For One. Lựa chọn gửi con đi, tưởng là để bảo vệ, về sau lại trở thành một nhánh cây rất tối.
```

### c07 · Nhánh 8: All Might

Khoảng 83 giây · cảnh s45–s50 · 1079 ký tự

**Gemini**

```text
Nhánh tám: Yagi Toshinori, All Might. Người đầu tiên trong cây không có năng lực riêng nào, và cũng là người mạnh nhất tới lúc đó.

<short pause> Vì không có năng lực riêng, cơ thể ông không phải gánh hai sức mạnh cùng lúc. Nhiều người cho rằng đó là lý do ông dùng One For All mạnh mẽ và lâu dài tới vậy. Kaku gắn nhãn đây là cách giải thích của truyện, cần kiểm lại.

<short pause> Nhưng khi hết sức, All Might trở lại dáng vẻ gầy gò, ho ra máu. Thế giới không biết. Chỉ vài người thân cận biết Biểu tượng Hòa bình đang cạn dần.

<short pause> Ông trở thành Biểu tượng Hòa bình, người mà sự có mặt thôi cũng khiến tội phạm chùn tay. Và ông đã đánh bại All For One lần đầu, nhưng phải trả giá bằng một vết thương không bao giờ lành.

<short pause> Ở trận chiến Kamino, All Might dùng chút lửa cuối cùng để đánh bại All For One lần nữa. Rồi ông chỉ tay vào ống kính và nói với cả thế giới: tiếp theo là cậu. Người xem hiểu câu đó dành cho Deku.

<short pause> Vết thương khiến thời gian ông ở dạng anh hùng ngày càng ngắn lại. Ông cần người kế nhiệm, và ông tìm thấy người đó ở một cậu bé không có năng lực, lao vào cứu bạn khi mọi anh hùng khác còn đứng yên.
```

**ElevenLabs**

```text
Nhánh tám: Yagi Toshinori, All Might. Người đầu tiên trong cây không có năng lực riêng nào, và cũng là người mạnh nhất tới lúc đó.

[pause] Vì không có năng lực riêng, cơ thể ông không phải gánh hai sức mạnh cùng lúc. Nhiều người cho rằng đó là lý do ông dùng One For All mạnh mẽ và lâu dài tới vậy. Kaku gắn nhãn đây là cách giải thích của truyện, cần kiểm lại.

[pause] Nhưng khi hết sức, All Might trở lại dáng vẻ gầy gò, ho ra máu. Thế giới không biết. Chỉ vài người thân cận biết Biểu tượng Hòa bình đang cạn dần.

[pause] Ông trở thành Biểu tượng Hòa bình, người mà sự có mặt thôi cũng khiến tội phạm chùn tay. Và ông đã đánh bại All For One lần đầu, nhưng phải trả giá bằng một vết thương không bao giờ lành.

[pause] Ở trận chiến Kamino, All Might dùng chút lửa cuối cùng để đánh bại All For One lần nữa. Rồi ông chỉ tay vào ống kính và nói với cả thế giới: tiếp theo là cậu. Người xem hiểu câu đó dành cho Deku.

[pause] Vết thương khiến thời gian ông ở dạng anh hùng ngày càng ngắn lại. Ông cần người kế nhiệm, và ông tìm thấy người đó ở một cậu bé không có năng lực, lao vào cứu bạn khi mọi anh hùng khác còn đứng yên.
```

### c08 · Nhánh 9: Midoriya Izuku

Khoảng 82 giây · cảnh s51–s57 · 1063 ký tự

**Gemini**

```text
Từ nhỏ Deku đã bị bác sĩ nói là không có năng lực, và bị bạn bè coi thường. <short pause> Nhưng cậu có một thói quen: ghi chép tỉ mỉ về năng lực của mọi anh hùng vào những cuốn sổ.

<short pause> <laugh> Kaku phải nói: Kaku rất có cảm tình với một nhân vật chính mê ghi chép. Nếu Deku có kênh YouTube, chắc là đối thủ đáng gờm nhất của Kaku.

<short pause> Nhánh chín: Midoriya Izuku, Deku. Cậu nuốt sợi tóc của All Might và nhận One For All. Sức mạnh quá lớn, lần đầu dùng là xương tay gãy.

<short pause> Cậu còn đổi cách chiến đấu: chuyển từ đấm sang đá, để tay không bị hỏng thêm. Mỗi lần thích nghi là một lần cậu hiểu cơ thể mình rõ hơn.

<short pause> Cậu học cách dùng từng phần trăm sức mạnh: năm phần trăm, tám phần trăm, hai mươi phần trăm, để cơ thể không vỡ. Giống như học lái một chiếc xe quá mạnh so với tay lái của mình.

<short pause> Rồi những bóng hình người cũ bắt đầu thức tỉnh. Deku lần lượt dùng được roi đen, khói, bay lơ lửng, cảm nhận nguy hiểm, và những năng lực khác. Cả cây phả hệ cùng chiến đấu trong một người.

<short pause> Deku là người cuối cùng của cây. Theo truyện, cậu là nhánh được chọn để kết thúc cuộc chiến bắt đầu từ hai anh em ở gốc cây.
```

**ElevenLabs**

```text
Từ nhỏ Deku đã bị bác sĩ nói là không có năng lực, và bị bạn bè coi thường. [pause] Nhưng cậu có một thói quen: ghi chép tỉ mỉ về năng lực của mọi anh hùng vào những cuốn sổ.

[pause] [chuckles] Kaku phải nói: Kaku rất có cảm tình với một nhân vật chính mê ghi chép. Nếu Deku có kênh YouTube, chắc là đối thủ đáng gờm nhất của Kaku.

[pause] Nhánh chín: Midoriya Izuku, Deku. Cậu nuốt sợi tóc của All Might và nhận One For All. Sức mạnh quá lớn, lần đầu dùng là xương tay gãy.

[pause] Cậu còn đổi cách chiến đấu: chuyển từ đấm sang đá, để tay không bị hỏng thêm. Mỗi lần thích nghi là một lần cậu hiểu cơ thể mình rõ hơn.

[pause] Cậu học cách dùng từng phần trăm sức mạnh: năm phần trăm, tám phần trăm, hai mươi phần trăm, để cơ thể không vỡ. Giống như học lái một chiếc xe quá mạnh so với tay lái của mình.

[pause] Rồi những bóng hình người cũ bắt đầu thức tỉnh. Deku lần lượt dùng được roi đen, khói, bay lơ lửng, cảm nhận nguy hiểm, và những năng lực khác. Cả cây phả hệ cùng chiến đấu trong một người.

[pause] Deku là người cuối cùng của cây. Theo truyện, cậu là nhánh được chọn để kết thúc cuộc chiến bắt đầu từ hai anh em ở gốc cây.
```

### c09 · Nhánh bị mất: dòng họ Shimura / Nhánh đối nghịch: All For One

Khoảng 145 giây · cảnh s58–s69 · 1886 ký tự

**Gemini**

```text
Giờ tới nhánh bi kịch nhất. Con trai của Nana Shimura lớn lên không biết mẹ mình là ai, và căm ghét anh hùng vì nghĩ mẹ đã bỏ rơi mình.

<short pause> Cậu bé từng mơ làm anh hùng, như bà mình. <short pause> Nhưng không ai tới cứu cậu vào đêm hôm đó. Đó là vết thương lớn nhất của Shigaraki, và là câu hỏi mà bộ truyện đặt ra cho chính các anh hùng.

<short pause> Cháu của Nana, cậu bé Shimura Tenko, lớn lên trong một gia đình cấm nhắc tới anh hùng. Một ngày, năng lực phân rã của cậu thức tỉnh, và gây ra một thảm kịch cho chính gia đình mình.

<short pause> Deku về sau hiểu ra rằng mình muốn cứu cả Shigaraki, không chỉ đánh bại hắn. Nhánh cây bị mất cuối cùng cũng có người muốn đưa nó về.

<short pause> All For One tìm tới cậu bé, nuôi dạy, đổi tên cậu thành Shigaraki Tomura, và biến cậu thành kẻ thù lớn nhất của các anh hùng.

<short pause> Hãy nhìn cái tên: Shigaraki là họ của chính Yoichi, người đầu tiên của One For All. All For One lấy họ của em trai mình đặt cho cháu của người giữ One For All thứ bảy. Hai cây phả hệ giao nhau ngay ở đây.

<short pause> Kaku thấy đây là chi tiết tàn nhẫn nhất của cả bộ truyện: người giữ ngọn lửa hi sinh gia đình để bảo vệ nó, và kẻ thù dùng chính gia đình đó để dập tắt ngọn lửa.

<short pause> Hắn kéo dài tuổi thọ, thay đổi cơ thể, và thậm chí tìm cách trở lại qua người khác. Một kẻ không chịu buông tay bất cứ thứ gì, trái ngược với một cây phả hệ sống nhờ việc buông tay.

<short pause> Và ở phía đối diện của cây là All For One: kẻ sống qua nhiều thế hệ, lấy năng lực của vô số người, và luôn muốn lấy lại thứ mà em trai đã trao đi.

<short pause> Kaku để ý: Yoichi và All For One đều là những nhân vật được nhắc tới từ đầu, nhưng mãi tới cuối truyện ta mới hiểu cuộc chiến của cả thế giới bắt nguồn từ mối quan hệ của họ.

<short pause> Hai sức mạnh đối lập hoàn toàn: một bên lấy mọi thứ cho một người, một bên trao một thứ cho mọi người sau. Tên của chúng đã nói lên tất cả: tất cả vì một, và một vì tất cả.

<short pause> Và câu chuyện của cả chín thế hệ, rốt cuộc, là cuộc cãi nhau chưa dứt giữa hai anh em ruột.
```

**ElevenLabs**

```text
Giờ tới nhánh bi kịch nhất. Con trai của Nana Shimura lớn lên không biết mẹ mình là ai, và căm ghét anh hùng vì nghĩ mẹ đã bỏ rơi mình.

[pause] Cậu bé từng mơ làm anh hùng, như bà mình. [pause] Nhưng không ai tới cứu cậu vào đêm hôm đó. Đó là vết thương lớn nhất của Shigaraki, và là câu hỏi mà bộ truyện đặt ra cho chính các anh hùng.

[pause] Cháu của Nana, cậu bé Shimura Tenko, lớn lên trong một gia đình cấm nhắc tới anh hùng. Một ngày, năng lực phân rã của cậu thức tỉnh, và gây ra một thảm kịch cho chính gia đình mình.

[pause] Deku về sau hiểu ra rằng mình muốn cứu cả Shigaraki, không chỉ đánh bại hắn. Nhánh cây bị mất cuối cùng cũng có người muốn đưa nó về.

[pause] All For One tìm tới cậu bé, nuôi dạy, đổi tên cậu thành Shigaraki Tomura, và biến cậu thành kẻ thù lớn nhất của các anh hùng.

[pause] Hãy nhìn cái tên: Shigaraki là họ của chính Yoichi, người đầu tiên của One For All. All For One lấy họ của em trai mình đặt cho cháu của người giữ One For All thứ bảy. Hai cây phả hệ giao nhau ngay ở đây.

[pause] Kaku thấy đây là chi tiết tàn nhẫn nhất của cả bộ truyện: người giữ ngọn lửa hi sinh gia đình để bảo vệ nó, và kẻ thù dùng chính gia đình đó để dập tắt ngọn lửa.

[pause] Hắn kéo dài tuổi thọ, thay đổi cơ thể, và thậm chí tìm cách trở lại qua người khác. Một kẻ không chịu buông tay bất cứ thứ gì, trái ngược với một cây phả hệ sống nhờ việc buông tay.

[pause] Và ở phía đối diện của cây là All For One: kẻ sống qua nhiều thế hệ, lấy năng lực của vô số người, và luôn muốn lấy lại thứ mà em trai đã trao đi.

[pause] Kaku để ý: Yoichi và All For One đều là những nhân vật được nhắc tới từ đầu, nhưng mãi tới cuối truyện ta mới hiểu cuộc chiến của cả thế giới bắt nguồn từ mối quan hệ của họ.

[pause] Hai sức mạnh đối lập hoàn toàn: một bên lấy mọi thứ cho một người, một bên trao một thứ cho mọi người sau. Tên của chúng đã nói lên tất cả: tất cả vì một, và một vì tất cả.

[pause] Và câu chuyện của cả chín thế hệ, rốt cuộc, là cuộc cãi nhau chưa dứt giữa hai anh em ruột.
```

### c10 · Cái kết của cây / Cây hoàn chỉnh

Khoảng 108 giây · cảnh s70–s78 · 1400 ký tự

**Gemini**

```text
Trong trận chiến cuối cùng, Deku dùng toàn bộ sức mạnh của cả cây phả hệ. Và sau đó, One For All dần tắt trong người cậu.

<short pause> Nhiều năm sau, All Might, người không còn năng lực, và Deku, người đã mất năng lực, đều vẫn được gọi là anh hùng. Bộ truyện kết thúc bằng câu trả lời cho câu hỏi đầu tiên: người không có năng lực có thể trở thành anh hùng không?

<short pause> Deku không còn sức mạnh. <short pause> Nhưng truyện cho thấy cậu vẫn là anh hùng: trở thành giáo viên, rồi được bạn bè giúp đỡ để có thể tiếp tục chiến đấu bằng một bộ trang phục đặc biệt.

<short pause> <laugh> Kaku thấy cái kết này khép lại cây phả hệ rất đẹp: sức mạnh được trao qua chín đời để kết thúc một cuộc chiến. Khi cuộc chiến kết thúc, sức mạnh cũng không cần nữa. Chỉ còn ý chí được trao lại.

<short pause> Kaku vẽ lại toàn bộ cây. Gốc: hai anh em, All For One và Yoichi. Thân cây: năng lực tích trữ và truyền đi hòa làm một.

<short pause> Và bên cạnh cây là những người không ở trong cây nhưng giữ cho nó sống: Gran Torino, mẹ của Deku, những người bạn cùng lớp đã đứng cạnh cậu tới cuối cùng.

<short pause> Chín nhánh: Yoichi, sang số, tích động năng, cảm nhận nguy hiểm, roi đen, khói, bay lơ lửng, All Might, và Deku.

<short pause> Một nhánh bị mất: dòng họ Shimura, bị cây đối nghịch cướp đi và biến thành Shigaraki Tomura. Và ngọn cây: ý chí được truyền lại, sau khi sức mạnh đã tắt.

<short pause> Nếu được chọn một người trong chín nhánh để kể riêng một video, bạn chọn ai? Kaku nghiêng về Nana Shimura. Viết lựa chọn của bạn vào bình luận nhé.
```

**ElevenLabs**

```text
Trong trận chiến cuối cùng, Deku dùng toàn bộ sức mạnh của cả cây phả hệ. Và sau đó, One For All dần tắt trong người cậu.

[pause] Nhiều năm sau, All Might, người không còn năng lực, và Deku, người đã mất năng lực, đều vẫn được gọi là anh hùng. [curious] Bộ truyện kết thúc bằng câu trả lời cho câu hỏi đầu tiên: người không có năng lực có thể trở thành anh hùng không?

[pause] Deku không còn sức mạnh. [pause] Nhưng truyện cho thấy cậu vẫn là anh hùng: trở thành giáo viên, rồi được bạn bè giúp đỡ để có thể tiếp tục chiến đấu bằng một bộ trang phục đặc biệt.

[pause] [chuckles] Kaku thấy cái kết này khép lại cây phả hệ rất đẹp: sức mạnh được trao qua chín đời để kết thúc một cuộc chiến. Khi cuộc chiến kết thúc, sức mạnh cũng không cần nữa. Chỉ còn ý chí được trao lại.

[pause] Kaku vẽ lại toàn bộ cây. Gốc: hai anh em, All For One và Yoichi. Thân cây: năng lực tích trữ và truyền đi hòa làm một.

[pause] Và bên cạnh cây là những người không ở trong cây nhưng giữ cho nó sống: Gran Torino, mẹ của Deku, những người bạn cùng lớp đã đứng cạnh cậu tới cuối cùng.

[pause] Chín nhánh: Yoichi, sang số, tích động năng, cảm nhận nguy hiểm, roi đen, khói, bay lơ lửng, All Might, và Deku.

[pause] Một nhánh bị mất: dòng họ Shimura, bị cây đối nghịch cướp đi và biến thành Shigaraki Tomura. Và ngọn cây: ý chí được truyền lại, sau khi sức mạnh đã tắt.

[pause] Nếu được chọn một người trong chín nhánh để kể riêng một video, bạn chọn ai? Kaku nghiêng về Nana Shimura. Viết lựa chọn của bạn vào bình luận nhé.
```

### c11 · Kết

Khoảng 47 giây · cảnh s79–s82 · 605 ký tự

**Gemini**

```text
Kaku mong bạn cũng có một người để truyền lại điều gì đó: một kỹ năng, một thói quen tốt, hay chỉ là một nụ cười như Nana đã truyền cho All Might.

<short pause> Cây phả hệ One For All không nối với nhau bằng máu, mà bằng lựa chọn. Mỗi người chọn trao đi, và nhờ vậy, ngọn lửa đi được tới người cuối cùng.

<short pause> Video tiếp theo, Kaku mở phòng thí nghiệm của tiến sĩ Agasa trong Thám tử lừng danh Conan: viên thuốc teo nhỏ và những món đồ phát minh. Khoa học thật tới đâu? Và tất nhiên, không phải hướng dẫn.

<short pause> <laugh> Nếu bạn thích những cây phả hệ như thế này, hãy đăng ký kênh để Kaku vẽ thêm nhiều cây nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Kaku mong bạn cũng có một người để truyền lại điều gì đó: một kỹ năng, một thói quen tốt, hay chỉ là một nụ cười như Nana đã truyền cho All Might.

[pause] Cây phả hệ One For All không nối với nhau bằng máu, mà bằng lựa chọn. Mỗi người chọn trao đi, và nhờ vậy, ngọn lửa đi được tới người cuối cùng.

[pause] Video tiếp theo, Kaku mở phòng thí nghiệm của tiến sĩ Agasa trong Thám tử lừng danh Conan: viên thuốc teo nhỏ và những món đồ phát minh. [curious] Khoa học thật tới đâu? Và tất nhiên, không phải hướng dẫn.

[pause] [chuckles] Nếu bạn thích những cây phả hệ như thế này, hãy đăng ký kênh để Kaku vẽ thêm nhiều cây nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
