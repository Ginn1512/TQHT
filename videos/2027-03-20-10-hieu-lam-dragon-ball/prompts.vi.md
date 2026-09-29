# Bộ prompt · Dragon Ball: 10 hiểu lầm mà nhiều người tin suốt ba mươi năm

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 82 ảnh, 8 đoạn đọc, khoảng 15.1 phút giọng.
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

Lời: Cảnh báo spoiler: video này nói về toàn bộ Dragon Ball, Dragon Ball Z và một phần Dragon Ball Super. Với một…

```text
Wide 16:9 landscape cinematic frame. an old orange crystal ball with small red stars inside resting on a stack of worn comic books beside a spoiler card, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Goku là người Trái Đất. Kamehameha là chiêu của Goku. Ngọc rồng ước được mọi điều. Nếu bạn gật đầu với cả ba…

```text
Wide 16:9 landscape cinematic frame. three handwritten notes pinned to a wall, each with a large red X drawn over it, close-up, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Dragon Ball là bộ truyện đã theo nhiều thế hệ người Việt, từ những cuốn truyện mỏng mua ở sạp báo tới những b…

```text
Wide 16:9 landscape cinematic frame. a small newsstand with rows of thin colorful comic books clipped on strings, wide shot, warm nostalgic afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku gỡ mười hiểu lầm về Dragon Ball. Mỗi hiểu lầm: người ta tin gì, truy…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny martial arts uniform, crossing out items on a checklist with a determined look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Và đúng dịp này, Dragon Ball Super đang được phát lại với phần Thần Hủy Diệt Beerus. Rất nhiều người đang qua…

```text
Wide 16:9 landscape cinematic frame. a TV screen glowing in a cozy living room with a small cat-like silhouette on the screen, wide shot, warm evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Dragon Ball là manga của Toriyama Akira, bắt đầu năm 1984. Ông mất ngày một tháng ba năm 2024, để lại một tro…

```text
Wide 16:9 landscape cinematic frame. a quiet drawing desk with a pen resting beside a blank page and a single flower in a small vase, close-up, soft respectful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Hiểu lầm 1: Goku là người Trái Đất

Lời: Nhiều người mới xem, nhất là chỉ xem phần đầu, nghĩ Goku là một cậu bé người Trái Đất có sức khỏe phi thường…

```text
Wide 16:9 landscape cinematic frame. a small boy with a monkey-like tail sitting on a rock in a mountain forest, back view, wide shot, warm morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Thật ra, Goku là người Saiyan, một chủng tộc chiến binh từ hành tinh khác. Tên thật của cậu là Kakarot. Cậu đ…

```text
Wide 16:9 landscape cinematic frame. a small round space pod crashed in a crater in a forest at dawn, close-up, dramatic soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Theo truyện, cậu được gửi tới để chinh phục Trái Đất. Nhưng một cú ngã vào đầu khi còn nhỏ khiến cậu quên nhi…

```text
Wide 16:9 landscape cinematic frame. an elderly man lifting a small baby from a crashed pod in a forest, medium shot, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Và lúc đó, Goku đã là một người cha. Sự thật về nguồn gốc không làm cậu thay đổi. Cậu vẫn chọn Trái Đất là qu…

```text
Wide 16:9 landscape cinematic frame. a father holding a small child's hand on a hillside overlooking a peaceful valley, back view, wide shot, warm sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Vì sao dễ hiểu nhầm? Vì sự thật này được tiết lộ khá muộn, khi Raditz, anh trai của Goku, xuất hiện ở đầu Dra…

```text
Wide 16:9 landscape cinematic frame. a dark figure descending from the sky over a green field, casting a long shadow, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Và cái đuôi khỉ của Goku, thứ tưởng chỉ để trông dễ thương, hóa ra là manh mối từ đầu: người Saiyan có đuôi,…

```text
Wide 16:9 landscape cinematic frame. a full moon glowing over a quiet forest with a giant ape-like shadow cast on the trees below, wide shot, eerie silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Kaku thấy đây là một trong những bước ngoặt hay nhất: nhân vật chính ta đã quen hơn trăm chương hóa ra thuộc…

```text
Wide 16:9 landscape cinematic frame. a small boy standing between a green Earth landscape and a distant red planet in the sky, symbolic wide shot, contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Hiểu lầm 2: Kamehameha là chiêu của Goku

Lời: Kamehameha, chiêu thức nổi tiếng nhất Dragon Ball. Ai cũng gắn nó với Goku, như thể Goku phát minh ra nó.

```text
Wide 16:9 landscape cinematic frame. two cupped hands drawn back at the hip with a bright blue light gathering between them, close-up, glowing blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Quy lão tên thật là Muten Roshi, sống trên một hòn đảo nhỏ với căn nhà màu hồng. Ông là người dạy võ cho cả G…

```text
Wide 16:9 landscape cinematic frame. a small pink house on a tiny tropical island surrounded by turquoise sea, wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Thật ra, người sáng tạo ra Kamehameha là Quy lão tiên sinh, Muten Roshi, thầy của Goku. Ông nói mình mất năm…

```text
Wide 16:9 landscape cinematic frame. an elderly martial arts master with a turtle shell on his back standing on a small tropical island, back view, wide shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Và Goku, lần đầu nhìn thấy, bắt chước được ngay, dù ở mức nhỏ. Ông già Quy lão sốc tới mức không nói nên lời.

```text
Wide 16:9 landscape cinematic frame. a small blast of blue light shooting from a child's hands and hitting a parked car, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Nhiều người khác trong truyện cũng dùng Kamehameha: Krillin, Yamcha, Gohan, cả Cell. Nó là chiêu của trường p…

```text
Wide 16:9 landscape cinematic frame. several silhouettes of different fighters each striking the same hand pose side by side, wide shot, bright blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Vì sao dễ hiểu nhầm? Vì Goku dùng chiêu này nhiều nhất, và dùng mạnh nhất. Người sáng tạo thì dần lui về làm…

```text
Wide 16:9 landscape cinematic frame. an old master sitting on a beach chair reading a magazine while a young fighter trains in the background, humorous wide shot, sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Tên Kamehameha cũng có một gốc thú vị: nó giống tên một vị vua Hawaii có thật, Kamehameha đệ nhất.

```text
Wide 16:9 landscape cinematic frame. a tropical island coastline with palm trees and a distant volcanic mountain under a bright sky, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Hiểu lầm 3: Ngọc rồng ước được mọi điều

Lời: Gom đủ bảy viên ngọc rồng, gọi rồng thần, và ước bất cứ điều gì. Đó là điều mà ai cũng nhớ.

```text
Wide 16:9 landscape cinematic frame. seven small orange crystal balls glowing in a circle on the ground under a darkening sky, overhead shot, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Thật ra, rồng thần có giới hạn. Sức mạnh của rồng không vượt quá sức mạnh của người tạo ra nó. Nên rồng không…

```text
Wide 16:9 landscape cinematic frame. a giant serpentine dragon silhouette coiled in a stormy sky, shaking its head slowly, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Rồng thần Trái Đất cũng không thể hồi sinh một người đã được hồi sinh một lần trước đó, và không hồi sinh ngư…

```text
Wide 16:9 landscape cinematic frame. a list of rules on an old parchment scroll with several lines crossed out, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Sau mỗi lần ước, ngọc rồng hóa thành đá và bay tán loạn khắp thế giới trong một năm. Muốn ước lần nữa, phải đ…

```text
Wide 16:9 landscape cinematic frame. seven grey stones scattering into the sky in different directions from a clearing, wide shot, dramatic evening light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Và mỗi bộ ngọc rồng khác nhau có luật khác nhau. Ngọc rồng Namek có thể thực hiện ba điều ước, và luật hồi si…

```text
Wide 16:9 landscape cinematic frame. two sets of crystal balls side by side, one small set and one larger set, on a rocky alien landscape, wide shot, green sky light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Có những điều ước nổi tiếng không liên quan tới sức mạnh: như lần đầu tiên, một điều ước bị cướp mất bởi một…

```text
Wide 16:9 landscape cinematic frame. a giant dragon silhouette in the sky looking puzzled as a small piece of cloth floats down from above, humorous wide shot, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Vì sao dễ hiểu nhầm? Vì những luật này được thêm dần qua từng arc, thường đúng lúc câu chuyện cần một giới hạ…

```text
Wide 16:9 landscape cinematic frame. a rulebook with sticky notes added at different pages over time, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: nhờ những giới hạn này, cái chết trong Dragon Ball vẫn có sức nặng, dù ngọc rồng có thể hồi sinh n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny crystal ball up to the light, examining it carefully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Hiểu lầm 4: Goku luôn thắng

Lời: Nhiều người nghĩ Goku luôn là người thắng trận quyết định.

```text
Wide 16:9 landscape cinematic frame. a victory podium with a single fighter standing on the top step, crowd cheering, wide shot, bright stadium light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Thật ra, Goku thua khá nhiều. Ở hai giải Thiên hạ đệ nhất võ đạo hội đầu tiên, cậu đều về nhì. Lần đầu thua c…

```text
Wide 16:9 landscape cinematic frame. a tournament ring with a young fighter sitting on the ground laughing while another fighter stands victorious, medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và trong arc Cell, người đánh bại Cell không phải Goku, mà là con trai cậu, Gohan. Goku chủ động rút lui để G…

```text
Wide 16:9 landscape cinematic frame. a young fighter standing in a ruined arena facing a towering silhouette while an older fighter watches from the side, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Kaku nghĩ chính những trận thua mới làm Goku hấp dẫn. Cậu không phải người được sinh ra để thắng, mà là người…

```text
Wide 16:9 landscape cinematic frame. a young fighter bowing respectfully to an opponent after a lost match in a tournament ring, medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Vì sao dễ hiểu nhầm? Vì Goku luôn là trung tâm của áp phích, trò chơi, và ký ức của người xem. Nhưng truyện t…

```text
Wide 16:9 landscape cinematic frame. a large poster on a wall featuring one fighter in the center with several smaller figures around the edges, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34 · Hiểu lầm 5: dạng cuối của Frieza là dạng mạnh nhất được tạo ra

Lời: Frieza biến hình nhiều lần trên Namek. Nhiều người nghĩ mỗi lần biến là Frieza tạo ra một cơ thể mạnh hơn.

```text
Wide 16:9 landscape cinematic frame. a sequence of four shadowy alien silhouettes of different shapes lined up from left to right, symbolic wide shot, dramatic purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Thật ra, dạng cuối cùng mà ta thấy trên Namek mới là cơ thể gốc của Frieza. Những dạng trước là các lớp để kì…

```text
Wide 16:9 landscape cinematic frame. a sleek small silhouette standing calmly in a stormy alien landscape as shed outer shells lie around it, dramatic low-angle shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Nghĩa là mỗi lần biến hình, Frieza không trở nên lớn hơn, mà là cởi bỏ lớp kìm hãm. Thứ đáng sợ nhất lại là h…

```text
Wide 16:9 landscape cinematic frame. a heavy set of armor pieces falling away from a small figure revealing a glowing core, symbolic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Và về sau, trong Dragon Ball Super, Frieza còn luyện tập và có thêm những dạng mới. Nhưng dạng gốc vẫn là chì…

```text
Wide 16:9 landscape cinematic frame. a small calm silhouette standing in a training field with a faint golden aura, wide shot, cold dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Vì sao dễ hiểu nhầm? Vì trong phần lớn truyện tranh, biến hình thường có nghĩa là thêm sức mạnh. Frieza làm n…

```text
Wide 16:9 landscape cinematic frame. a comparison drawing: a figure growing larger with arrows on one side, and a figure shrinking and glowing brighter on the other, parchment close-up, amber ink. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39 · Hiểu lầm 6: người Namek là nam

Lời: Piccolo, Kami, Nail, Dende. Tất cả người Namek trông giống nam giới. Nhiều người mặc định họ là một chủng tộc…

```text
Wide 16:9 landscape cinematic frame. a group of tall green-skinned silhouettes with antennae standing on a hill under a green sky, wide shot, soft alien light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Thật ra, người Namek không có giới tính. Họ sinh sản vô tính, bằng cách nhả ra một quả trứng từ miệng.

```text
Wide 16:9 landscape cinematic frame. a large white egg resting on soft moss on an alien planet with blue grass, close-up, gentle green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Đó là lý do Piccolo, dù nói chuyện như một người đàn ông, lại là người chăm sóc Gohan như một người cha lẫn n…

```text
Wide 16:9 landscape cinematic frame. a tall green silhouette carrying a small child on its shoulders through a quiet forest, back view, wide shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Người Namek còn có thể hợp thể với nhau, khi hai người Namek hòa làm một để mạnh hơn. Piccolo từng hợp thể vớ…

```text
Wide 16:9 landscape cinematic frame. two tall green silhouettes merging into one in a burst of soft light, symbolic wide shot, alien green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Vì sao dễ hiểu nhầm? Vì trong bản dịch và giọng lồng tiếng, người Namek thường được gọi bằng đại từ nam. Và D…

```text
Wide 16:9 landscape cinematic frame. a dubbing studio microphone in front of a script page with a highlighted pronoun, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Hiểu lầm 7: Dragon Ball Z là một truyện khác

Lời: Nhiều người nghĩ Dragon Ball và Dragon Ball Z là hai bộ truyện khác nhau, của hai giai đoạn khác nhau.

```text
Wide 16:9 landscape cinematic frame. two separate manga volumes placed apart on a shelf with a gap between them, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Thật ra, manga gốc ở Nhật chỉ có một tên: Dragon Ball. Chữ Z là tên của bộ anime chuyển thể phần sau của truy…

```text
Wide 16:9 landscape cinematic frame. a single continuous manga series spine with a small letter Z sticker added halfway along it, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Sau đó còn có Dragon Ball GT, một phần chỉ có ở anime, và Dragon Ball Super, có cả manga lẫn anime. Rồi năm 2…

```text
Wide 16:9 landscape cinematic frame. a branching timeline drawn on parchment with several labeled branches spreading from a single trunk, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Ở một số nước, phần sau của manga cũng được in với tên Dragon Ball Z để khớp với anime. Vì vậy sự phân chia c…

```text
Wide 16:9 landscape cinematic frame. a stack of foreign-edition comic books with different cover designs, close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: chữ Z được Toriyama chọn đơn giản vì nó là chữ cái cuối cùng, như một lời hứa rằng đây là phần cuố…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up a large letter Z sign and then looking sheepish as more pages appear behind it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Hiểu lầm 8: Vegeta chỉ là đối thủ

Lời: Vegeta, hoàng tử Saiyan. Nhiều người chỉ nhớ anh như đối thủ kiêu ngạo của Goku, luôn thua một bước.

```text
Wide 16:9 landscape cinematic frame. a proud silhouette with arms crossed standing on a rocky cliff, looking away from another figure in the distance, wide shot, dramatic sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Thật ra, Vegeta có một trong những hành trình thay đổi lớn nhất truyện: từ kẻ xâm lược tàn nhẫn thành người c…

```text
Wide 16:9 landscape cinematic frame. a man in a training suit teaching a small child to throw a punch in a backyard, medium shot, warm afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Và câu nói nổi tiếng của Vegeta về việc sức mạnh của Goku vượt quá chín nghìn, trong bản lồng tiếng tiếng Anh…

```text
Wide 16:9 landscape cinematic frame. an old scouter-like device display showing a large number with a crack across the screen, humorous close-up, green glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Trong arc Buu, Vegeta chấp nhận hy sinh bản thân để bảo vệ gia đình, và cuối cùng thừa nhận Goku mạnh hơn mìn…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing in a vast barren landscape with glowing energy around him, arms outstretched protectively, wide shot, dramatic golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Trong Dragon Ball Super, Vegeta còn có những khoảnh khắc làm cha rất dễ thương. Một người từng phá hủy các hà…

```text
Wide 16:9 landscape cinematic frame. a proud man holding a small child's hand walking through a sunny park, back view, wide shot, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Vì sao dễ hiểu nhầm? Vì câu nói và vẻ kiêu ngạo của Vegeta quá nổi bật. Người ta nhớ câu nói, mà quên hành tr…

```text
Wide 16:9 landscape cinematic frame. a speech bubble with an exclamation point floating above a crowd of meme-like doodles, humorous close-up, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Hiểu lầm 9: Goku chiến đấu vì công lý

Lời: Goku là anh hùng, nên chắc hẳn cậu chiến đấu vì công lý, vì bảo vệ Trái Đất.

```text
Wide 16:9 landscape cinematic frame. a heroic silhouette standing on a mountain peak with the sun behind him, low-angle shot, dramatic heroic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Thật ra, động lực lớn nhất của Goku là được đấu với người mạnh. Cậu vui khi gặp đối thủ khó, và nhiều lần còn…

```text
Wide 16:9 landscape cinematic frame. a fighter grinning widely while facing a much larger opponent in a ruined arena, medium shot, bright energetic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Chichi, vợ Goku, thường than phiền rằng chồng mình chỉ nghĩ tới đánh nhau. Qua cô, bộ truyện cũng tự chế giễu…

```text
Wide 16:9 landscape cinematic frame. a woman with hands on her hips scolding a sheepish fighter in a cozy kitchen, humorous medium shot, warm homely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Có lần Goku cho Frieza hay Cell cơ hội hồi phục để trận đấu công bằng hơn, khiến bạn bè cậu bực mình. Cậu bảo…

```text
Wide 16:9 landscape cinematic frame. a small glowing bean being tossed through the air toward an injured opponent in a battlefield, dynamic close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Vì sao dễ hiểu nhầm? Vì kết quả là như nhau: Goku luôn bảo vệ Trái Đất. Nhưng lý do thì không phải kiểu anh h…

```text
Wide 16:9 landscape cinematic frame. a comparison drawing: a caped hero silhouette on one side and a grinning martial artist silhouette on the other, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · Hiểu lầm 10, lớn nhất: Dragon Ball ban đầu là truyện đánh nhau

Lời: Và đây là hiểu lầm lớn nhất. Nhiều người chỉ biết Dragon Ball qua những trận đánh nổ tung hành tinh, và nghĩ…

```text
Wide 16:9 landscape cinematic frame. a planet exploding in space with streaks of energy in the foreground, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Thật ra, Dragon Ball bắt đầu là một câu chuyện phiêu lưu hài hước, lấy cảm hứng từ Tây Du Ký. Goku, với cái đ…

```text
Wide 16:9 landscape cinematic frame. a small boy with a monkey tail riding a golden cloud over mountains while holding a long staff, wide shot, bright adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Bulma là một thiên tài khoa học, người tạo ra máy dò ngọc rồng, và về sau là cỗ máy thời gian. Không có cô, s…

```text
Wide 16:9 landscape cinematic frame. a young inventor tinkering with a small round radar device on a workbench full of gadgets, close-up, bright workshop light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Phần đầu là chuyến đi tìm ngọc rồng cùng cô gái Bulma, với rất nhiều trò đùa, chuyện kỳ quặc, và những nhân v…

```text
Wide 16:9 landscape cinematic frame. a small group of travelers on a winding desert road with a quirky capsule car, humorous wide shot, warm sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Người Việt rất quen với Tây Du Ký, nên nếu đọc lại những chương đầu, bạn sẽ thấy rất nhiều chỗ nháy mắt: cây…

```text
Wide 16:9 landscape cinematic frame. an old illustrated book of an ancient pilgrimage legend lying open beside a modern comic, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nếu bạn chưa từng đọc phần đầu, Kaku khuyên thử đọc lại hai, ba tập đầu tiên. Bạn sẽ gặp một Goku rất khác: n…

```text
Wide 16:9 landscape cinematic frame. a small stack of the first few comic volumes placed on a bedside table with a lamp on, close-up, cozy warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Vì sao dễ hiểu nhầm? Vì phần đánh nhau quá nổi tiếng, và anime Z được phát rộng rãi hơn. Nhiều người chưa bao…

```text
Wide 16:9 landscape cinematic frame. a bookshelf where the later volumes are worn from reading while the first volumes remain untouched, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là bài học lớn nhất: Dragon Ball không mạnh vì những trận đánh, mà vì tinh thần phiêu lưu và ti…

```text
Wide 16:9 landscape cinematic frame. the owl mascot riding a tiny golden cloud with a joyful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · Ba hiểu lầm nhỏ tặng thêm

Lời: Trước khi tổng kết, Kaku tặng thêm ba hiểu lầm nhỏ, vui hơn và ít ai để ý.

```text
Wide 16:9 landscape cinematic frame. a small gift box tied with an orange ribbon on a stack of comics, close-up, cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Hiểu lầm nhỏ một: tóc vàng của Super Saiyan được chọn vì trông ngầu. Toriyama từng chia sẻ một lý do rất đời:…

```text
Wide 16:9 landscape cinematic frame. a manga page in progress with some hair areas left blank white while an ink bottle sits nearby, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Hiểu lầm nhỏ hai: Krillin không có mũi là do vẽ thiếu. Không, Toriyama cố ý vẽ vậy, và nhân vật trong truyện…

```text
Wide 16:9 landscape cinematic frame. a small doodle of a smiling face with no nose drawn on a sketchbook page with an arrow and a laughing note, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hiểu lầm nhỏ ba: Goku biết bay từ đầu. Không, lúc nhỏ Goku phải cưỡi đám mây bay. Cậu chỉ học cách tự bay khi…

```text
Wide 16:9 landscape cinematic frame. a small boy clinging happily to a golden cloud flying low over a green valley, wide shot, bright playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy những chi tiết nhỏ này cho thấy Toriyama là một họa sĩ rất thực tế, và rất hài hước. Ông vẽ để vui,…

```text
Wide 16:9 landscape cinematic frame. the owl mascot laughing while holding up a small sketch of a cloud. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Bảng tổng kết

Lời: Tổng kết mười hiểu lầm. Goku là người Saiyan tên Kakarot. Kamehameha là của Quy lão. Ngọc rồng có giới hạn. G…

```text
Wide 16:9 landscape cinematic frame. a checklist on parchment with the first five items checked in green ink, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Người Namek không có giới tính. Dragon Ball Z là tên anime, không phải truyện khác. Vegeta có hành trình trưở…

```text
Wide 16:9 landscape cinematic frame. the completed checklist with all ten items checked and a gold star beside the last, close-up, warm triumphant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Cộng thêm ba hiểu lầm nhỏ: tóc vàng để đỡ tô mực, Krillin cố ý không có mũi, và Goku lúc nhỏ phải cưỡi mây.

```text
Wide 16:9 landscape cinematic frame. three small bonus items added to the bottom of the checklist in a different ink, close-up, amber and orange ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Bạn đã từng tin hiểu lầm nào? Viết vào bình luận, và nếu bạn biết thêm hiểu lầm khác, Kaku sẽ gom lại cho một…

```text
Wide 16:9 landscape cinematic frame. a comment card drawn on parchment with a tiny crystal ball doodle and a question mark, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · Lời cảm ơn Toriyama

Lời: Trước khi kết thúc, Kaku muốn dành vài giây cho Toriyama Akira. Ông không chỉ vẽ Dragon Ball, mà còn thiết kế…

```text
Wide 16:9 landscape cinematic frame. a drawing desk with scattered sketches of whimsical vehicles and creatures, a pen resting across them, close-up, warm respectful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Phong cách của ông, những cỗ máy tròn tròn, những nhân vật vừa ngầu vừa ngộ nghĩnh, đã ảnh hưởng tới rất nhiề…

```text
Wide 16:9 landscape cinematic frame. a row of manga volumes from different artists on a shelf with a small older volume placed at the start, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Toriyama từng nói, đại ý, rằng ông chỉ muốn vẽ những thứ làm người đọc vui. Có lẽ đó là lý do Dragon Ball vẫn…

```text
Wide 16:9 landscape cinematic frame. a small smiling doodle drawn in the corner of a manga page beside a signature-like squiggle, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Kaku mong rằng lần tới bạn mở lại Dragon Ball, bạn sẽ bắt đầu từ trang đầu tiên, nơi một cậu bé có đuôi khỉ g…

```text
Wide 16:9 landscape cinematic frame. the first page of an old comic book being opened by a pair of hands, warm golden light spilling out, close-up, nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Kết

Lời: Video tiếp theo, Kaku leo một bậc thang khác: One Piece, từ Gear 2 tới Gear 5, mỗi nấc là một cách Luffy vượt…

```text
Wide 16:9 landscape cinematic frame. a staircase of glowing steps rising into the clouds with a small hat resting on the lowest step, wide shot, adventurous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video này giúp bạn nhìn Dragon Ball khác đi một chút, hãy đăng ký kênh. Và nếu có ai hỏi Goku là người ở…

```text
Wide 16:9 landscape cinematic frame. the owl mascot waving goodbye from atop a small golden cloud drifting across the sky. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 78 giây · cảnh s01–s06 · 1014 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói về toàn bộ Dragon Ball, Dragon Ball Z và một phần Dragon Ball Super. Với một bộ truyện gần bốn mươi năm tuổi, Kaku tin phần lớn các bạn đã biết, nhưng vẫn nhắc cho chắc.

<short pause> Goku là người Trái Đất. Kamehameha là chiêu của Goku. Ngọc rồng ước được mọi điều. Nếu bạn gật đầu với cả ba câu này, video này dành cho bạn.

<short pause> Dragon Ball là bộ truyện đã theo nhiều thế hệ người Việt, từ những cuốn truyện mỏng mua ở sạp báo tới những buổi chiều xem anime trên tivi. Truyện càng quen, hiểu lầm càng nhiều.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku gỡ mười hiểu lầm về Dragon Ball. Mỗi hiểu lầm: người ta tin gì, truyện nói gì, và vì sao dễ hiểu nhầm. Hiểu lầm lớn nhất để dành tới cuối.

<short pause> Và đúng dịp này, Dragon Ball Super đang được phát lại với phần Thần Hủy Diệt Beerus. Rất nhiều người đang quay lại với Goku, và đây là lúc tốt để làm mới trí nhớ.

<short pause> Dragon Ball là manga của Toriyama Akira, bắt đầu năm 1984. Ông mất ngày một tháng ba năm 2024, để lại một trong những di sản lớn nhất của manga thế giới.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói về toàn bộ Dragon Ball, Dragon Ball Z và một phần Dragon Ball Super. Với một bộ truyện gần bốn mươi năm tuổi, Kaku tin phần lớn các bạn đã biết, nhưng vẫn nhắc cho chắc.

[pause] Goku là người Trái Đất. Kamehameha là chiêu của Goku. Ngọc rồng ước được mọi điều. Nếu bạn gật đầu với cả ba câu này, video này dành cho bạn.

[pause] Dragon Ball là bộ truyện đã theo nhiều thế hệ người Việt, từ những cuốn truyện mỏng mua ở sạp báo tới những buổi chiều xem anime trên tivi. Truyện càng quen, hiểu lầm càng nhiều.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku gỡ mười hiểu lầm về Dragon Ball. Mỗi hiểu lầm: người ta tin gì, truyện nói gì, và vì sao dễ hiểu nhầm. Hiểu lầm lớn nhất để dành tới cuối.

[pause] Và đúng dịp này, Dragon Ball Super đang được phát lại với phần Thần Hủy Diệt Beerus. Rất nhiều người đang quay lại với Goku, và đây là lúc tốt để làm mới trí nhớ.

[pause] Dragon Ball là manga của Toriyama Akira, bắt đầu năm 1984. Ông mất ngày một tháng ba năm 2024, để lại một trong những di sản lớn nhất của manga thế giới.
```

### c02 · Hiểu lầm 1: Goku là người Trái Đất / Hiểu lầm 2: Kamehameha là chiêu của Goku

Khoảng 147 giây · cảnh s07–s20 · 1907 ký tự

**Gemini**

```text
Nhiều người mới xem, nhất là chỉ xem phần đầu, nghĩ Goku là một cậu bé người Trái Đất có sức khỏe phi thường và một cái đuôi khỉ.

<short pause> Thật ra, Goku là người Saiyan, một chủng tộc chiến binh từ hành tinh khác. Tên thật của cậu là Kakarot. Cậu được gửi tới Trái Đất khi còn là em bé.

<short pause> Theo truyện, cậu được gửi tới để chinh phục Trái Đất. <short pause> Nhưng một cú ngã vào đầu khi còn nhỏ khiến cậu quên nhiệm vụ, và trở thành một đứa trẻ hiền lành.

<short pause> Và lúc đó, Goku đã là một người cha. Sự thật về nguồn gốc không làm cậu thay đổi. Cậu vẫn chọn Trái Đất là quê hương.

<short pause> Vì sao dễ hiểu nhầm? Vì sự thật này được tiết lộ khá muộn, khi Raditz, anh trai của Goku, xuất hiện ở đầu Dragon Ball Z. Phần Dragon Ball đầu tiên không nói gì về nó.

<short pause> Và cái đuôi khỉ của Goku, thứ tưởng chỉ để trông dễ thương, hóa ra là manh mối từ đầu: người Saiyan có đuôi, và biến thành khỉ đột khổng lồ khi nhìn trăng tròn.

<short pause> Kaku thấy đây là một trong những bước ngoặt hay nhất: nhân vật chính ta đã quen hơn trăm chương hóa ra thuộc về một chủng tộc chinh phạt, nhưng chọn sống như một người Trái Đất.

<short pause> Kamehameha, chiêu thức nổi tiếng nhất Dragon Ball. Ai cũng gắn nó với Goku, như thể Goku phát minh ra nó.

<short pause> Quy lão tên thật là Muten Roshi, sống trên một hòn đảo nhỏ với căn nhà màu hồng. Ông là người dạy võ cho cả Goku lẫn Krillin khi còn nhỏ.

<short pause> Thật ra, người sáng tạo ra Kamehameha là Quy lão tiên sinh, Muten Roshi, thầy của Goku. Ông nói mình mất năm mươi năm để hoàn thiện nó.

<short pause> Và Goku, lần đầu nhìn thấy, bắt chước được ngay, dù ở mức nhỏ. Ông già Quy lão sốc tới mức không nói nên lời.

<short pause> Nhiều người khác trong truyện cũng dùng Kamehameha: Krillin, Yamcha, Gohan, cả Cell. Nó là chiêu của trường phái Quy lão, không phải của riêng ai.

<short pause> Vì sao dễ hiểu nhầm? Vì Goku dùng chiêu này nhiều nhất, và dùng mạnh nhất. Người sáng tạo thì dần lui về làm một ông già vui tính.

<short pause> Tên Kamehameha cũng có một gốc thú vị: nó giống tên một vị vua Hawaii có thật, Kamehameha đệ nhất.
```

**ElevenLabs**

```text
Nhiều người mới xem, nhất là chỉ xem phần đầu, nghĩ Goku là một cậu bé người Trái Đất có sức khỏe phi thường và một cái đuôi khỉ.

[pause] Thật ra, Goku là người Saiyan, một chủng tộc chiến binh từ hành tinh khác. Tên thật của cậu là Kakarot. Cậu được gửi tới Trái Đất khi còn là em bé.

[pause] Theo truyện, cậu được gửi tới để chinh phục Trái Đất. [pause] Nhưng một cú ngã vào đầu khi còn nhỏ khiến cậu quên nhiệm vụ, và trở thành một đứa trẻ hiền lành.

[pause] Và lúc đó, Goku đã là một người cha. Sự thật về nguồn gốc không làm cậu thay đổi. Cậu vẫn chọn Trái Đất là quê hương.

[pause] [curious] Vì sao dễ hiểu nhầm? Vì sự thật này được tiết lộ khá muộn, khi Raditz, anh trai của Goku, xuất hiện ở đầu Dragon Ball Z. Phần Dragon Ball đầu tiên không nói gì về nó.

[pause] Và cái đuôi khỉ của Goku, thứ tưởng chỉ để trông dễ thương, hóa ra là manh mối từ đầu: người Saiyan có đuôi, và biến thành khỉ đột khổng lồ khi nhìn trăng tròn.

[pause] Kaku thấy đây là một trong những bước ngoặt hay nhất: nhân vật chính ta đã quen hơn trăm chương hóa ra thuộc về một chủng tộc chinh phạt, nhưng chọn sống như một người Trái Đất.

[pause] Kamehameha, chiêu thức nổi tiếng nhất Dragon Ball. Ai cũng gắn nó với Goku, như thể Goku phát minh ra nó.

[pause] Quy lão tên thật là Muten Roshi, sống trên một hòn đảo nhỏ với căn nhà màu hồng. Ông là người dạy võ cho cả Goku lẫn Krillin khi còn nhỏ.

[pause] Thật ra, người sáng tạo ra Kamehameha là Quy lão tiên sinh, Muten Roshi, thầy của Goku. Ông nói mình mất năm mươi năm để hoàn thiện nó.

[pause] Và Goku, lần đầu nhìn thấy, bắt chước được ngay, dù ở mức nhỏ. Ông già Quy lão sốc tới mức không nói nên lời.

[pause] Nhiều người khác trong truyện cũng dùng Kamehameha: Krillin, Yamcha, Gohan, cả Cell. Nó là chiêu của trường phái Quy lão, không phải của riêng ai.

[pause] Vì sao dễ hiểu nhầm? Vì Goku dùng chiêu này nhiều nhất, và dùng mạnh nhất. Người sáng tạo thì dần lui về làm một ông già vui tính.

[pause] Tên Kamehameha cũng có một gốc thú vị: nó giống tên một vị vua Hawaii có thật, Kamehameha đệ nhất.
```

### c03 · Hiểu lầm 3: Ngọc rồng ước được mọi điều / Hiểu lầm 4: Goku luôn thắng

Khoảng 136 giây · cảnh s21–s33 · 1764 ký tự

**Gemini**

```text
Gom đủ bảy viên ngọc rồng, gọi rồng thần, và ước bất cứ điều gì. Đó là điều mà ai cũng nhớ.

<short pause> Thật ra, rồng thần có giới hạn. Sức mạnh của rồng không vượt quá sức mạnh của người tạo ra nó. Nên rồng không thể giết một kẻ mạnh hơn người tạo ra ngọc rồng.

<short pause> Rồng thần Trái Đất cũng không thể hồi sinh một người đã được hồi sinh một lần trước đó, và không hồi sinh người chết vì tuổi già hay bệnh tật tự nhiên.

<short pause> Sau mỗi lần ước, ngọc rồng hóa thành đá và bay tán loạn khắp thế giới trong một năm. Muốn ước lần nữa, phải đi tìm lại từ đầu. Đó là lý do mỗi điều ước đều quý.

<short pause> Và mỗi bộ ngọc rồng khác nhau có luật khác nhau. Ngọc rồng Namek có thể thực hiện ba điều ước, và luật hồi sinh cũng khác.

<short pause> Có những điều ước nổi tiếng không liên quan tới sức mạnh: như lần đầu tiên, một điều ước bị cướp mất bởi một yêu cầu rất đời thường, một chiếc quần lót. Dragon Ball ngay từ đầu đã không nghiêm túc lắm.

<short pause> Vì sao dễ hiểu nhầm? Vì những luật này được thêm dần qua từng arc, thường đúng lúc câu chuyện cần một giới hạn.

<short pause> <laugh> Kaku để ý: nhờ những giới hạn này, cái chết trong Dragon Ball vẫn có sức nặng, dù ngọc rồng có thể hồi sinh người.

<short pause> Nhiều người nghĩ Goku luôn là người thắng trận quyết định.

<short pause> Thật ra, Goku thua khá nhiều. Ở hai giải Thiên hạ đệ nhất võ đạo hội đầu tiên, cậu đều về nhì. Lần đầu thua chính thầy mình đang cải trang, lần hai thua Thiên Tân Hán.

<short pause> Và trong arc Cell, người đánh bại Cell không phải Goku, mà là con trai cậu, Gohan. Goku chủ động rút lui để Gohan ra sân.

<short pause> Kaku nghĩ chính những trận thua mới làm Goku hấp dẫn. Cậu không phải người được sinh ra để thắng, mà là người không ngừng muốn giỏi hơn sau mỗi lần thua.

<short pause> Vì sao dễ hiểu nhầm? Vì Goku luôn là trung tâm của áp phích, trò chơi, và ký ức của người xem. <short pause> Nhưng truyện thường để người khác thắng những trận quan trọng.
```

**ElevenLabs**

```text
Gom đủ bảy viên ngọc rồng, gọi rồng thần, và ước bất cứ điều gì. Đó là điều mà ai cũng nhớ.

[pause] Thật ra, rồng thần có giới hạn. Sức mạnh của rồng không vượt quá sức mạnh của người tạo ra nó. Nên rồng không thể giết một kẻ mạnh hơn người tạo ra ngọc rồng.

[pause] Rồng thần Trái Đất cũng không thể hồi sinh một người đã được hồi sinh một lần trước đó, và không hồi sinh người chết vì tuổi già hay bệnh tật tự nhiên.

[pause] Sau mỗi lần ước, ngọc rồng hóa thành đá và bay tán loạn khắp thế giới trong một năm. Muốn ước lần nữa, phải đi tìm lại từ đầu. Đó là lý do mỗi điều ước đều quý.

[pause] Và mỗi bộ ngọc rồng khác nhau có luật khác nhau. Ngọc rồng Namek có thể thực hiện ba điều ước, và luật hồi sinh cũng khác.

[pause] Có những điều ước nổi tiếng không liên quan tới sức mạnh: như lần đầu tiên, một điều ước bị cướp mất bởi một yêu cầu rất đời thường, một chiếc quần lót. Dragon Ball ngay từ đầu đã không nghiêm túc lắm.

[pause] [curious] Vì sao dễ hiểu nhầm? Vì những luật này được thêm dần qua từng arc, thường đúng lúc câu chuyện cần một giới hạn.

[pause] [chuckles] Kaku để ý: nhờ những giới hạn này, cái chết trong Dragon Ball vẫn có sức nặng, dù ngọc rồng có thể hồi sinh người.

[pause] Nhiều người nghĩ Goku luôn là người thắng trận quyết định.

[pause] Thật ra, Goku thua khá nhiều. Ở hai giải Thiên hạ đệ nhất võ đạo hội đầu tiên, cậu đều về nhì. Lần đầu thua chính thầy mình đang cải trang, lần hai thua Thiên Tân Hán.

[pause] Và trong arc Cell, người đánh bại Cell không phải Goku, mà là con trai cậu, Gohan. Goku chủ động rút lui để Gohan ra sân.

[pause] Kaku nghĩ chính những trận thua mới làm Goku hấp dẫn. Cậu không phải người được sinh ra để thắng, mà là người không ngừng muốn giỏi hơn sau mỗi lần thua.

[pause] Vì sao dễ hiểu nhầm? Vì Goku luôn là trung tâm của áp phích, trò chơi, và ký ức của người xem. [pause] Nhưng truyện thường để người khác thắng những trận quan trọng.
```

### c04 · Hiểu lầm 5: dạng cuối của Frieza là dạng mạnh nhất được tạo ra / Hiểu lầm 6: người Namek là nam

Khoảng 103 giây · cảnh s34–s43 · 1337 ký tự

**Gemini**

```text
Frieza biến hình nhiều lần trên Namek. Nhiều người nghĩ mỗi lần biến là Frieza tạo ra một cơ thể mạnh hơn.

<short pause> Thật ra, dạng cuối cùng mà ta thấy trên Namek mới là cơ thể gốc của Frieza. Những dạng trước là các lớp để kìm nén sức mạnh, vì sức mạnh gốc của hắn quá lớn để kiểm soát thường ngày.

<short pause> Nghĩa là mỗi lần biến hình, Frieza không trở nên lớn hơn, mà là cởi bỏ lớp kìm hãm. Thứ đáng sợ nhất lại là hình dạng nhỏ gọn nhất.

<short pause> Và về sau, trong Dragon Ball Super, Frieza còn luyện tập và có thêm những dạng mới. <short pause> Nhưng dạng gốc vẫn là chìa khóa để hiểu tính cách hắn: luôn kìm nén, luôn tính toán.

<short pause> Vì sao dễ hiểu nhầm? Vì trong phần lớn truyện tranh, biến hình thường có nghĩa là thêm sức mạnh. Frieza làm ngược lại.

<short pause> Piccolo, Kami, Nail, Dende. Tất cả người Namek trông giống nam giới. Nhiều người mặc định họ là một chủng tộc toàn nam.

<short pause> Thật ra, người Namek không có giới tính. Họ sinh sản vô tính, bằng cách nhả ra một quả trứng từ miệng.

<short pause> Đó là lý do Piccolo, dù nói chuyện như một người đàn ông, lại là người chăm sóc Gohan như một người cha lẫn người mẹ.

<short pause> Người Namek còn có thể hợp thể với nhau, khi hai người Namek hòa làm một để mạnh hơn. Piccolo từng hợp thể với Nail và với Kami.

<short pause> Vì sao dễ hiểu nhầm? Vì trong bản dịch và giọng lồng tiếng, người Namek thường được gọi bằng đại từ nam. Và Dragon Ball không bao giờ dừng lại để giải thích dài dòng.
```

**ElevenLabs**

```text
Frieza biến hình nhiều lần trên Namek. Nhiều người nghĩ mỗi lần biến là Frieza tạo ra một cơ thể mạnh hơn.

[pause] Thật ra, dạng cuối cùng mà ta thấy trên Namek mới là cơ thể gốc của Frieza. Những dạng trước là các lớp để kìm nén sức mạnh, vì sức mạnh gốc của hắn quá lớn để kiểm soát thường ngày.

[pause] Nghĩa là mỗi lần biến hình, Frieza không trở nên lớn hơn, mà là cởi bỏ lớp kìm hãm. Thứ đáng sợ nhất lại là hình dạng nhỏ gọn nhất.

[pause] Và về sau, trong Dragon Ball Super, Frieza còn luyện tập và có thêm những dạng mới. [pause] Nhưng dạng gốc vẫn là chìa khóa để hiểu tính cách hắn: luôn kìm nén, luôn tính toán.

[pause] [curious] Vì sao dễ hiểu nhầm? Vì trong phần lớn truyện tranh, biến hình thường có nghĩa là thêm sức mạnh. Frieza làm ngược lại.

[pause] Piccolo, Kami, Nail, Dende. Tất cả người Namek trông giống nam giới. Nhiều người mặc định họ là một chủng tộc toàn nam.

[pause] Thật ra, người Namek không có giới tính. Họ sinh sản vô tính, bằng cách nhả ra một quả trứng từ miệng.

[pause] Đó là lý do Piccolo, dù nói chuyện như một người đàn ông, lại là người chăm sóc Gohan như một người cha lẫn người mẹ.

[pause] Người Namek còn có thể hợp thể với nhau, khi hai người Namek hòa làm một để mạnh hơn. Piccolo từng hợp thể với Nail và với Kami.

[pause] Vì sao dễ hiểu nhầm? Vì trong bản dịch và giọng lồng tiếng, người Namek thường được gọi bằng đại từ nam. Và Dragon Ball không bao giờ dừng lại để giải thích dài dòng.
```

### c05 · Hiểu lầm 7: Dragon Ball Z là một truyện khác / Hiểu lầm 8: Vegeta chỉ là đối thủ

Khoảng 124 giây · cảnh s44–s54 · 1608 ký tự

**Gemini**

```text
Nhiều người nghĩ Dragon Ball và Dragon Ball Z là hai bộ truyện khác nhau, của hai giai đoạn khác nhau.

<short pause> Thật ra, manga gốc ở Nhật chỉ có một tên: Dragon Ball. Chữ Z là tên của bộ anime chuyển thể phần sau của truyện, kể từ khi Goku trưởng thành và Raditz xuất hiện.

<short pause> Sau đó còn có Dragon Ball GT, một phần chỉ có ở anime, và Dragon Ball Super, có cả manga lẫn anime. Rồi năm 2024 là Dragon Ball Daima. Dòng thời gian ngày càng nhiều nhánh.

<short pause> Ở một số nước, phần sau của manga cũng được in với tên Dragon Ball Z để khớp với anime. Vì vậy sự phân chia càng thêm rõ trong trí nhớ người đọc.

<short pause> <laugh> Kaku để ý: chữ Z được Toriyama chọn đơn giản vì nó là chữ cái cuối cùng, như một lời hứa rằng đây là phần cuối. Rồi sau đó, câu chuyện vẫn tiếp tục thêm nhiều năm.

<short pause> Vegeta, hoàng tử Saiyan. Nhiều người chỉ nhớ anh như đối thủ kiêu ngạo của Goku, luôn thua một bước.

<short pause> Thật ra, Vegeta có một trong những hành trình thay đổi lớn nhất truyện: từ kẻ xâm lược tàn nhẫn thành người chồng, người cha, và người bảo vệ Trái Đất.

<short pause> Và câu nói nổi tiếng của Vegeta về việc sức mạnh của Goku vượt quá chín nghìn, trong bản lồng tiếng tiếng Anh, đã trở thành một trong những câu đùa lan truyền nhất trên mạng, dù trong bản gốc con số khác.

<short pause> Trong arc Buu, Vegeta chấp nhận hy sinh bản thân để bảo vệ gia đình, và cuối cùng thừa nhận Goku mạnh hơn mình. Đó là một khoảnh khắc trưởng thành rất lớn.

<short pause> Trong Dragon Ball Super, Vegeta còn có những khoảnh khắc làm cha rất dễ thương. Một người từng phá hủy các hành tinh, giờ dắt con gái đi chơi.

<short pause> Vì sao dễ hiểu nhầm? Vì câu nói và vẻ kiêu ngạo của Vegeta quá nổi bật. Người ta nhớ câu nói, mà quên hành trình.
```

**ElevenLabs**

```text
Nhiều người nghĩ Dragon Ball và Dragon Ball Z là hai bộ truyện khác nhau, của hai giai đoạn khác nhau.

[pause] Thật ra, manga gốc ở Nhật chỉ có một tên: Dragon Ball. Chữ Z là tên của bộ anime chuyển thể phần sau của truyện, kể từ khi Goku trưởng thành và Raditz xuất hiện.

[pause] Sau đó còn có Dragon Ball GT, một phần chỉ có ở anime, và Dragon Ball Super, có cả manga lẫn anime. Rồi năm 2024 là Dragon Ball Daima. Dòng thời gian ngày càng nhiều nhánh.

[pause] Ở một số nước, phần sau của manga cũng được in với tên Dragon Ball Z để khớp với anime. Vì vậy sự phân chia càng thêm rõ trong trí nhớ người đọc.

[pause] [chuckles] Kaku để ý: chữ Z được Toriyama chọn đơn giản vì nó là chữ cái cuối cùng, như một lời hứa rằng đây là phần cuối. Rồi sau đó, câu chuyện vẫn tiếp tục thêm nhiều năm.

[pause] Vegeta, hoàng tử Saiyan. Nhiều người chỉ nhớ anh như đối thủ kiêu ngạo của Goku, luôn thua một bước.

[pause] Thật ra, Vegeta có một trong những hành trình thay đổi lớn nhất truyện: từ kẻ xâm lược tàn nhẫn thành người chồng, người cha, và người bảo vệ Trái Đất.

[pause] Và câu nói nổi tiếng của Vegeta về việc sức mạnh của Goku vượt quá chín nghìn, trong bản lồng tiếng tiếng Anh, đã trở thành một trong những câu đùa lan truyền nhất trên mạng, dù trong bản gốc con số khác.

[pause] Trong arc Buu, Vegeta chấp nhận hy sinh bản thân để bảo vệ gia đình, và cuối cùng thừa nhận Goku mạnh hơn mình. Đó là một khoảnh khắc trưởng thành rất lớn.

[pause] Trong Dragon Ball Super, Vegeta còn có những khoảnh khắc làm cha rất dễ thương. Một người từng phá hủy các hành tinh, giờ dắt con gái đi chơi.

[pause] [curious] Vì sao dễ hiểu nhầm? Vì câu nói và vẻ kiêu ngạo của Vegeta quá nổi bật. Người ta nhớ câu nói, mà quên hành trình.
```

### c06 · Hiểu lầm 9: Goku chiến đấu vì công lý / Hiểu lầm 10, lớn nhất: Dragon Ball ban đầu là truyện đánh nhau

Khoảng 153 giây · cảnh s55–s67 · 1994 ký tự

**Gemini**

```text
Goku là anh hùng, nên chắc hẳn cậu chiến đấu vì công lý, vì bảo vệ Trái Đất.

<short pause> Thật ra, động lực lớn nhất của Goku là được đấu với người mạnh. Cậu vui khi gặp đối thủ khó, và nhiều lần còn tha cho kẻ thù để sau này được đấu lại.

<short pause> Chichi, vợ Goku, thường than phiền rằng chồng mình chỉ nghĩ tới đánh nhau. Qua cô, bộ truyện cũng tự chế giễu chính nhân vật chính của mình.

<short pause> Có lần Goku cho Frieza hay Cell cơ hội hồi phục để trận đấu công bằng hơn, khiến bạn bè cậu bực mình. Cậu bảo vệ Trái Đất, nhưng không phải vì cậu coi mình là anh hùng.

<short pause> Vì sao dễ hiểu nhầm? Vì kết quả là như nhau: Goku luôn bảo vệ Trái Đất. <short pause> Nhưng lý do thì không phải kiểu anh hùng truyền thống. Chính điều đó làm Goku khác biệt.

<short pause> Và đây là hiểu lầm lớn nhất. Nhiều người chỉ biết Dragon Ball qua những trận đánh nổ tung hành tinh, và nghĩ ngay từ đầu nó đã là truyện đánh nhau.

<short pause> Thật ra, Dragon Ball bắt đầu là một câu chuyện phiêu lưu hài hước, lấy cảm hứng từ Tây Du Ký. Goku, với cái đuôi khỉ, cây gậy như ý và đám mây bay, là một phiên bản của Tôn Ngộ Không.

<short pause> Bulma là một thiên tài khoa học, người tạo ra máy dò ngọc rồng, và về sau là cỗ máy thời gian. Không có cô, sẽ không có hành trình nào bắt đầu.

<short pause> Phần đầu là chuyến đi tìm ngọc rồng cùng cô gái Bulma, với rất nhiều trò đùa, chuyện kỳ quặc, và những nhân vật vui nhộn. Các giải đấu võ thuật được thêm vào sau.

<short pause> Người Việt rất quen với Tây Du Ký, nên nếu đọc lại những chương đầu, bạn sẽ thấy rất nhiều chỗ nháy mắt: cây gậy dài ra theo ý muốn, đám mây chỉ người tốt bụng mới ngồi được, và một chuyến đi về phía tây.

<short pause> Nếu bạn chưa từng đọc phần đầu, Kaku khuyên thử đọc lại hai, ba tập đầu tiên. Bạn sẽ gặp một Goku rất khác: ngây thơ, hài hước, và chưa biết mình sẽ trở thành huyền thoại.

<short pause> Vì sao dễ hiểu nhầm? Vì phần đánh nhau quá nổi tiếng, và anime Z được phát rộng rãi hơn. Nhiều người chưa bao giờ đọc những chương đầu.

<short pause> <laugh> Kaku nghĩ đây là bài học lớn nhất: Dragon Ball không mạnh vì những trận đánh, mà vì tinh thần phiêu lưu và tiếng cười mà Toriyama đặt vào từ trang đầu tiên.
```

**ElevenLabs**

```text
Goku là anh hùng, nên chắc hẳn cậu chiến đấu vì công lý, vì bảo vệ Trái Đất.

[pause] Thật ra, động lực lớn nhất của Goku là được đấu với người mạnh. Cậu vui khi gặp đối thủ khó, và nhiều lần còn tha cho kẻ thù để sau này được đấu lại.

[pause] Chichi, vợ Goku, thường than phiền rằng chồng mình chỉ nghĩ tới đánh nhau. Qua cô, bộ truyện cũng tự chế giễu chính nhân vật chính của mình.

[pause] Có lần Goku cho Frieza hay Cell cơ hội hồi phục để trận đấu công bằng hơn, khiến bạn bè cậu bực mình. Cậu bảo vệ Trái Đất, nhưng không phải vì cậu coi mình là anh hùng.

[pause] [curious] Vì sao dễ hiểu nhầm? Vì kết quả là như nhau: Goku luôn bảo vệ Trái Đất. [pause] Nhưng lý do thì không phải kiểu anh hùng truyền thống. Chính điều đó làm Goku khác biệt.

[pause] Và đây là hiểu lầm lớn nhất. Nhiều người chỉ biết Dragon Ball qua những trận đánh nổ tung hành tinh, và nghĩ ngay từ đầu nó đã là truyện đánh nhau.

[pause] Thật ra, Dragon Ball bắt đầu là một câu chuyện phiêu lưu hài hước, lấy cảm hứng từ Tây Du Ký. Goku, với cái đuôi khỉ, cây gậy như ý và đám mây bay, là một phiên bản của Tôn Ngộ Không.

[pause] Bulma là một thiên tài khoa học, người tạo ra máy dò ngọc rồng, và về sau là cỗ máy thời gian. Không có cô, sẽ không có hành trình nào bắt đầu.

[pause] Phần đầu là chuyến đi tìm ngọc rồng cùng cô gái Bulma, với rất nhiều trò đùa, chuyện kỳ quặc, và những nhân vật vui nhộn. Các giải đấu võ thuật được thêm vào sau.

[pause] Người Việt rất quen với Tây Du Ký, nên nếu đọc lại những chương đầu, bạn sẽ thấy rất nhiều chỗ nháy mắt: cây gậy dài ra theo ý muốn, đám mây chỉ người tốt bụng mới ngồi được, và một chuyến đi về phía tây.

[pause] Nếu bạn chưa từng đọc phần đầu, Kaku khuyên thử đọc lại hai, ba tập đầu tiên. Bạn sẽ gặp một Goku rất khác: ngây thơ, hài hước, và chưa biết mình sẽ trở thành huyền thoại.

[pause] Vì sao dễ hiểu nhầm? Vì phần đánh nhau quá nổi tiếng, và anime Z được phát rộng rãi hơn. Nhiều người chưa bao giờ đọc những chương đầu.

[pause] [chuckles] Kaku nghĩ đây là bài học lớn nhất: Dragon Ball không mạnh vì những trận đánh, mà vì tinh thần phiêu lưu và tiếng cười mà Toriyama đặt vào từ trang đầu tiên.
```

### c07 · Ba hiểu lầm nhỏ tặng thêm / Bảng tổng kết / Lời cảm ơn Toriyama

Khoảng 143 giây · cảnh s68–s80 · 1863 ký tự

**Gemini**

```text
Trước khi tổng kết, Kaku tặng thêm ba hiểu lầm nhỏ, vui hơn và ít ai để ý.

<short pause> Hiểu lầm nhỏ một: tóc vàng của Super Saiyan được chọn vì trông ngầu. Toriyama từng chia sẻ một lý do rất đời: tóc để trắng trên bản in đen trắng thì trợ lý không phải tô mực đen, đỡ tốn công.

<short pause> Hiểu lầm nhỏ hai: Krillin không có mũi là do vẽ thiếu. Không, Toriyama cố ý vẽ vậy, và nhân vật trong truyện cũng từng đùa về chuyện đó.

<short pause> Hiểu lầm nhỏ ba: Goku biết bay từ đầu. Không, lúc nhỏ Goku phải cưỡi đám mây bay. Cậu chỉ học cách tự bay khi đã lớn và luyện tập nhiều hơn.

<short pause> <laugh> Kaku thấy những chi tiết nhỏ này cho thấy Toriyama là một họa sĩ rất thực tế, và rất hài hước. Ông vẽ để vui, và điều đó thấm vào từng trang.

<short pause> Tổng kết mười hiểu lầm. Goku là người Saiyan tên Kakarot. Kamehameha là của Quy lão. Ngọc rồng có giới hạn. Goku thua nhiều hơn bạn nghĩ. Dạng cuối của Frieza là dạng gốc.

<short pause> Người Namek không có giới tính. Dragon Ball Z là tên anime, không phải truyện khác. Vegeta có hành trình trưởng thành lớn. Goku chiến đấu vì thích đấu. Và Dragon Ball bắt đầu từ Tây Du Ký.

<short pause> Cộng thêm ba hiểu lầm nhỏ: tóc vàng để đỡ tô mực, Krillin cố ý không có mũi, và Goku lúc nhỏ phải cưỡi mây.

<short pause> Bạn đã từng tin hiểu lầm nào? Viết vào bình luận, và nếu bạn biết thêm hiểu lầm khác, Kaku sẽ gom lại cho một phần hai.

<short pause> Trước khi kết thúc, Kaku muốn dành vài giây cho Toriyama Akira. Ông không chỉ vẽ Dragon Ball, mà còn thiết kế nhân vật cho những trò chơi mà nhiều thế hệ đã lớn lên cùng.

<short pause> Phong cách của ông, những cỗ máy tròn tròn, những nhân vật vừa ngầu vừa ngộ nghĩnh, đã ảnh hưởng tới rất nhiều họa sĩ manga sau này.

<short pause> Toriyama từng nói, đại ý, rằng ông chỉ muốn vẽ những thứ làm người đọc vui. Có lẽ đó là lý do Dragon Ball vẫn làm chúng ta vui, gần bốn mươi năm sau.

<short pause> Kaku mong rằng lần tới bạn mở lại Dragon Ball, bạn sẽ bắt đầu từ trang đầu tiên, nơi một cậu bé có đuôi khỉ gặp một cô gái đang đi tìm ngọc rồng.
```

**ElevenLabs**

```text
Trước khi tổng kết, Kaku tặng thêm ba hiểu lầm nhỏ, vui hơn và ít ai để ý.

[pause] Hiểu lầm nhỏ một: tóc vàng của Super Saiyan được chọn vì trông ngầu. Toriyama từng chia sẻ một lý do rất đời: tóc để trắng trên bản in đen trắng thì trợ lý không phải tô mực đen, đỡ tốn công.

[pause] Hiểu lầm nhỏ hai: Krillin không có mũi là do vẽ thiếu. Không, Toriyama cố ý vẽ vậy, và nhân vật trong truyện cũng từng đùa về chuyện đó.

[pause] Hiểu lầm nhỏ ba: Goku biết bay từ đầu. Không, lúc nhỏ Goku phải cưỡi đám mây bay. Cậu chỉ học cách tự bay khi đã lớn và luyện tập nhiều hơn.

[pause] [chuckles] Kaku thấy những chi tiết nhỏ này cho thấy Toriyama là một họa sĩ rất thực tế, và rất hài hước. Ông vẽ để vui, và điều đó thấm vào từng trang.

[pause] Tổng kết mười hiểu lầm. Goku là người Saiyan tên Kakarot. Kamehameha là của Quy lão. Ngọc rồng có giới hạn. Goku thua nhiều hơn bạn nghĩ. Dạng cuối của Frieza là dạng gốc.

[pause] Người Namek không có giới tính. Dragon Ball Z là tên anime, không phải truyện khác. Vegeta có hành trình trưởng thành lớn. Goku chiến đấu vì thích đấu. Và Dragon Ball bắt đầu từ Tây Du Ký.

[pause] Cộng thêm ba hiểu lầm nhỏ: tóc vàng để đỡ tô mực, Krillin cố ý không có mũi, và Goku lúc nhỏ phải cưỡi mây.

[pause] [curious] Bạn đã từng tin hiểu lầm nào? Viết vào bình luận, và nếu bạn biết thêm hiểu lầm khác, Kaku sẽ gom lại cho một phần hai.

[pause] Trước khi kết thúc, Kaku muốn dành vài giây cho Toriyama Akira. Ông không chỉ vẽ Dragon Ball, mà còn thiết kế nhân vật cho những trò chơi mà nhiều thế hệ đã lớn lên cùng.

[pause] Phong cách của ông, những cỗ máy tròn tròn, những nhân vật vừa ngầu vừa ngộ nghĩnh, đã ảnh hưởng tới rất nhiều họa sĩ manga sau này.

[pause] Toriyama từng nói, đại ý, rằng ông chỉ muốn vẽ những thứ làm người đọc vui. Có lẽ đó là lý do Dragon Ball vẫn làm chúng ta vui, gần bốn mươi năm sau.

[pause] Kaku mong rằng lần tới bạn mở lại Dragon Ball, bạn sẽ bắt đầu từ trang đầu tiên, nơi một cậu bé có đuôi khỉ gặp một cô gái đang đi tìm ngọc rồng.
```

### c08 · Kết

Khoảng 23 giây · cảnh s81–s82 · 300 ký tự

**Gemini**

```text
Video tiếp theo, Kaku leo một bậc thang khác: One Piece, từ Gear 2 tới Gear 5, mỗi nấc là một cách Luffy vượt giới hạn cơ thể mình.

<short pause> Nếu video này giúp bạn nhìn Dragon Ball khác đi một chút, hãy đăng ký kênh. Và nếu có ai hỏi Goku là người ở đâu, bạn biết trả lời rồi đấy. <laugh> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Video tiếp theo, Kaku leo một bậc thang khác: One Piece, từ Gear 2 tới Gear 5, mỗi nấc là một cách Luffy vượt giới hạn cơ thể mình.

[pause] Nếu video này giúp bạn nhìn Dragon Ball khác đi một chút, hãy đăng ký kênh. Và nếu có ai hỏi Goku là người ở đâu, bạn biết trả lời rồi đấy. [chuckles] Kaku gấp sổ đây, hẹn gặp lại!
```
