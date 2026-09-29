# Bộ prompt · Chainsaw Man: Luật ác quỷ và nỗi sợ hoạt động thế nào?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 98 ảnh, 7 đoạn đọc, khoảng 15.0 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (98 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Chainsaw Man đến hết phần một của manga, nhiều hơn phần anime đã chiếu. Nếu chỉ xe…

```text
Wide 16:9 landscape cinematic frame. a dark city alley at night with a single flickering streetlight and a chain lying on the ground. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Trong thế giới Chainsaw Man, có những con quỷ yếu tới mức một đứa trẻ cũng đánh thắng. Và có những con quỷ mạ…

```text
Wide 16:9 landscape cinematic frame. a split image: a tiny harmless creature on a sidewalk and a massive shadow looming over an entire city. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Điều gì tạo ra sự khác biệt đó? Không phải tuổi tác, không phải luyện tập. Mà là việc con người sợ chúng tới…

```text
Wide 16:9 landscape cinematic frame. a crowd of human silhouettes whose shadows stretch and merge into a giant monstrous shape. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Đây là một trong những hệ thống sức mạnh độc đáo nhất anime: sức mạnh của quỷ được quyết định bởi nỗi sợ của…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a frightened human face that becomes a devil's silhouette. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình sẽ giải mã luật ác quỷ: chúng sinh ra thế nào, khế ước là gì, và vì…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a notebook nervously, looking over its shoulder at a shadow. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · **Kaku** (đính kèm ảnh mẫu)

Lời: Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, thứ đáng sợ nhất không phải con quỷ, mà là nỗi sợ trong…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a small candle in a dark room, calm but alert. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Quỷ sinh ra từ đâu?

Lời: Luật đầu tiên: mỗi con quỷ mang tên một khái niệm hoặc sự vật mà con người sợ. Có quỷ bóng tối, quỷ súng, quỷ…

```text
Wide 16:9 landscape cinematic frame. a gallery of abstract devil silhouettes each shaped like a concept: darkness, a gun, a flame, a tomato. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Chúng sinh ra từ nỗi sợ tập thể của loài người về khái niệm đó. Thứ gì tồn tại trong nỗi sợ của con người, th…

```text
Wide 16:9 landscape cinematic frame. countless small shadows rising from human silhouettes and gathering into a single creature. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Luật thứ hai: con người càng sợ khái niệm nào, con quỷ mang tên khái niệm đó càng mạnh.

```text
Wide 16:9 landscape cinematic frame. a bar chart made of shadows, one tiny bar and one enormous bar towering over a city. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Vì vậy quỷ cà chua thì yếu, vì ít ai thật sự sợ cà chua. Còn quỷ súng thì cực mạnh, vì súng là nỗi sợ của hàn…

```text
Wide 16:9 landscape cinematic frame. a small comical tomato-like creature next to a colossal shadow made of gun barrels. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Điều này có nghĩa là sức mạnh của quỷ thay đổi theo thời đại. Một nỗi sợ xưa cũ bị lãng quên, con quỷ đó cũng…

```text
Wide 16:9 landscape cinematic frame. an old faded poster peeling off a wall while a new glowing poster replaces it. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là một hệ thống sức mạnh mà người xem góp phần tạo ra. Chính nỗi sợ của xã hội là nguồn năn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a crowd whose shadows feed into a glowing core. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · Địa ngục và vòng luân hồi

Lời: Luật thứ ba: quỷ không thật sự chết. Khi bị giết trên trái đất, chúng tái sinh ở địa ngục. Khi chết ở địa ngụ…

```text
Wide 16:9 landscape cinematic frame. a circular diagram with Earth on one side and a dark hellscape on the other, arrows looping between. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Khi tái sinh, quỷ thường mất ký ức và phải bắt đầu lại, nhưng khái niệm mà nó đại diện vẫn còn đó.

```text
Wide 16:9 landscape cinematic frame. a devil silhouette dissolving into smoke and reforming in a strange landscape with blank eyes. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Vì vậy thợ săn quỷ không bao giờ thật sự tiêu diệt được một nỗi sợ. Họ chỉ đẩy nó sang phía bên kia, và nó sẽ…

```text
Wide 16:9 landscape cinematic frame. a hunter watching a defeated devil fade, while a new shadow appears on the distant horizon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Địa ngục trong truyện là một nơi kỳ lạ, nơi những con quỷ mạnh nhất chưa từng chết lần nào vẫn đang tồn tại.…

```text
Wide 16:9 landscape cinematic frame. a surreal hellscape with endless doors floating in a pale sky and colossal shapes beyond them. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ví von: đánh bại quỷ giống tắt một bóng đèn. Đèn tắt ở phòng này, nhưng sẽ sáng lại ở một phòng khác.

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping a light switch as a bulb goes dark here and lights up in another room. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Nỗi sợ nguyên thủy

Lời: Có một nhóm quỷ đặc biệt được gọi là nỗi sợ nguyên thủy. Chúng đại diện cho những nỗi sợ sâu nhất, có từ thuở…

```text
Wide 16:9 landscape cinematic frame. ancient colossal shadows standing in a void, each shaped like a primal concept. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Đó là những thứ như bóng tối, sự rơi, cái chết, những nỗi sợ không cần ai dạy, đứa trẻ nào cũng có.

```text
Wide 16:9 landscape cinematic frame. a small child silhouette looking up at a vast darkness above them, clutching a blanket. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Những con quỷ này mạnh tới mức ngay cả thợ săn quỷ giỏi nhất cũng gần như bất lực. Truyện mô tả chúng như thi…

```text
Wide 16:9 landscape cinematic frame. a team of hunters standing frozen as a wall of absolute darkness swallows the street. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Điều thú vị: chúng chưa từng bị giết, nên chưa từng tái sinh. Chúng là những ký ức cổ xưa nhất của nỗi sợ loà…

```text
Wide 16:9 landscape cinematic frame. an ancient hourglass with sand that has never run out, glowing faintly in darkness. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rùng mình: nếu sức mạnh đến từ nỗi sợ, thì nỗi sợ có từ lâu nhất sẽ là thứ mạnh nhất. Logic rất đơn giản…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding behind a book with only its glasses visible. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Những con quỷ tiêu biểu

Lời: Để luật nỗi sợ dễ hình dung hơn, hãy xem vài con quỷ tiêu biểu và cách sức mạnh của chúng khớp với nỗi sợ của…

```text
Wide 16:9 landscape cinematic frame. a bestiary page with several shadowy devil silhouettes sketched in ink. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Quỷ súng là ví dụ khủng khiếp nhất. Trong truyện, nó từng xuất hiện và giết hơn một triệu người chỉ trong vài…

```text
Wide 16:9 landscape cinematic frame. a city skyline under a sky filled with countless tiny glinting projectiles, people scattering. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Sau sự kiện đó, súng bị kiểm soát gắt gao ở nhiều nơi. Điều này càng khiến con người sợ súng hơn, và vòng lặp…

```text
Wide 16:9 landscape cinematic frame. a government office with stacks of confiscated weapons and worried officials. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Quỷ tương lai lập khế ước để cho người dùng nhìn thấy vài giây tương lai. Nó sống trong mắt người ký, và thíc…

```text
Wide 16:9 landscape cinematic frame. a shadowy figure peering out from inside a human eye socket, faint future images around. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Quỷ cáo là con quỷ được nhiều thợ săn dùng, triệu hồi bằng một thế tay. Nhưng nó kén người, không phải ai nó…

```text
Wide 16:9 landscape cinematic frame. a giant fox head emerging from a shadowy portal to bite down on a monster, a hunter forming a hand sign. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Quỷ nguyền rủa cho phép giết đối thủ sau vài nhát đâm, nhưng người dùng trả bằng một phần tuổi thọ rất lớn. M…

```text
Wide 16:9 landscape cinematic frame. a nail-like blade glowing with a curse mark, a hunter's lifeline shrinking beside it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Mỗi con quỷ này cho thấy cùng một luật: năng lực của quỷ gắn với nỗi sợ mà nó đại diện, và cái giá luôn đi kè…

```text
Wide 16:9 landscape cinematic frame. a row of contracts pinned to a wall, each with a different shadow and a price tag. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30 · Khế ước: con người mượn sức quỷ

Lời: Con người yếu hơn quỷ rất nhiều. Vậy họ chiến đấu bằng cách nào? Câu trả lời là khế ước.

```text
Wide 16:9 landscape cinematic frame. a human hand shaking a clawed shadowy hand over a glowing contract on a table. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Thợ săn quỷ có thể lập khế ước với một con quỷ để mượn sức mạnh của nó. Đổi lại, họ phải trả một cái giá.

```text
Wide 16:9 landscape cinematic frame. a scale with a burst of devil power on one side and a small glowing human piece on the other. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Cái giá có thể là một phần cơ thể, một phần tuổi thọ, hay một thứ gì đó quý giá khác. Quỷ càng mạnh, cái giá…

```text
Wide 16:9 landscape cinematic frame. three price tags hanging on a chain: an eye icon, an hourglass, a heart. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Có người đưa một con mắt để đổi lấy khả năng nhìn thấy tương lai gần. Có người trả bằng nhiều năm tuổi thọ để…

```text
Wide 16:9 landscape cinematic frame. a hunter with an eyepatch seeing faint future images, another with a shortening glowing lifeline. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Khế ước nghe giống giao ước trong Nen mà mình từng giải thích. Nhưng ở đây, bạn không tự đặt luật. Bạn thương…

```text
Wide 16:9 landscape cinematic frame. a tense negotiation table with a human on one side and a grinning shadow on the other. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Và quỷ không phải lúc nào cũng giữ lời theo cách con người mong muốn. Một khế ước sai có thể lấy đi nhiều hơn…

```text
Wide 16:9 landscape cinematic frame. a contract with small print glowing ominously at the bottom of the page. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu có ngày bạn định ký khế ước với quỷ, hãy đọc kỹ điều khoản. Đó là lời khuyên hữu ích cả ngo…

```text
Wide 16:9 landscape cinematic frame. the owl mascot squinting at tiny text on a contract with a magnifying glass. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Thợ săn quỷ công an

Lời: Trong truyện, săn quỷ là một nghề chính thức. Có thợ săn tư nhân, và có Thợ săn quỷ công an, một tổ chức của…

```text
Wide 16:9 landscape cinematic frame. a group of devil hunters in dark suits and ties standing beside a police car at night. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Thợ săn quỷ công an nhận nhiệm vụ nguy hiểm nhất, và họ thường dùng khế ước với những con quỷ mạnh để có sức…

```text
Wide 16:9 landscape cinematic frame. hunters in suits drawing swords and summoning shadowy allies in a ruined street. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nghề này có tỉ lệ tử vong cực cao. Truyện liên tục cho thấy những thợ săn chết sớm, thậm chí chết một cách độ…

```text
Wide 16:9 landscape cinematic frame. a row of empty desks in a small office with flowers placed on them. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Điều đó làm thế giới Chainsaw Man có cảm giác rất lạnh lùng: không ai an toàn, kể cả những nhân vật tưởng như…

```text
Wide 16:9 landscape cinematic frame. a lone hunter smoking on a rooftop at dawn, looking at the city with tired eyes. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Cách con người đánh bại quỷ mạnh hơn mình

Lời: Nếu quỷ mạnh hơn người nhiều như vậy, làm sao thợ săn vẫn thắng được? Truyện cho thấy vài chiến thuật lặp lại.

```text
Wide 16:9 landscape cinematic frame. a small team of hunters planning around a map in a dim room, a giant shadow drawn on the map. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chiến thuật một: dùng quỷ đánh quỷ. Khế ước cho phép con người đưa một con quỷ mạnh ra đối đầu với con quỷ kh…

```text
Wide 16:9 landscape cinematic frame. a summoned shadowy beast clashing with another devil while a hunter stands behind it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Chiến thuật hai: làm việc theo đội. Mỗi người mang một khế ước khác nhau, bù trừ điểm yếu cho nhau.

```text
Wide 16:9 landscape cinematic frame. four hunters in suits covering different angles in a narrow street, each with a different shadow ally. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Chiến thuật ba: lợi dụng điểm yếu của nỗi sợ. Quỷ gắn với một khái niệm, nên hiểu khái niệm đó là hiểu cách đ…

```text
Wide 16:9 landscape cinematic frame. a hunter shining a bright lamp at a devil made of darkness, the devil shrinking back. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Chiến thuật bốn, đen tối nhất: chấp nhận trả giá cực đắt, bằng tuổi thọ hay một phần cơ thể, cho một đòn quyế…

```text
Wide 16:9 landscape cinematic frame. a hunter kneeling after a final strike, an hourglass beside them nearly empty. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhận xét: trong Chainsaw Man, chiến thắng hiếm khi sạch sẽ. Ai thắng cũng phải mất một thứ gì đó.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a bandaged wing, looking tired but relieved. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Ma nhân và người lai quỷ

Lời: Ngoài quỷ và con người, truyện còn có hai dạng lai rất quan trọng: ma nhân và người lai quỷ.

```text
Wide 16:9 landscape cinematic frame. two silhouettes side by side: one with horns and a playful stance, one with a strange weapon growing from the head. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ma nhân là quỷ chiếm lấy xác người chết. Chúng yếu hơn quỷ thật, và thường có đặc điểm lạ trên đầu như sừng.

```text
Wide 16:9 landscape cinematic frame. a mischievous horned figure silhouette sitting cross-legged on a sofa, snacks around her. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Power, cô gái ma nhân máu nổi tiếng, là ví dụ tiêu biểu: vừa nguy hiểm, vừa trẻ con, vừa đáng yêu theo một cá…

```text
Wide 16:9 landscape cinematic frame. a horned girl silhouette laughing wildly while holding a weapon shaped from blood, chaotic energy. dynamic low-angle shot, sense of overwhelming power. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Người lai quỷ thì khác: họ là con người có thể biến thành quỷ, thường bằng một hành động kích hoạt cụ thể.

```text
Wide 16:9 landscape cinematic frame. a figure pulling a cord on their chest as sparks and machinery begin to emerge. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Denji là người lai với quỷ cưa máy. Anh kéo sợi dây trên ngực, và cưa máy mọc ra từ đầu và tay.

```text
Wide 16:9 landscape cinematic frame. a hooded silhouette wielding two roaring saw blades of light in a dark alley. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Người lai có một lợi thế lớn: họ hồi phục khi uống máu. Điều đó giúp họ trụ được những vết thương mà người th…

```text
Wide 16:9 landscape cinematic frame. a wounded hybrid figure drinking from a small vial, wounds closing with a faint glow. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Người lai khác: kiếm và bom

Lời: Denji không phải người lai duy nhất. Truyện còn có những người lai khác, mỗi người mang một loại vũ khí làm n…

```text
Wide 16:9 landscape cinematic frame. two silhouettes: one with blades emerging from arms and head, one with a pin on their neck. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Có người lai với quỷ kiếm, rút một chốt để biến tay và đầu thành những lưỡi kiếm sắc lẻm.

```text
Wide 16:9 landscape cinematic frame. a figure pulling a small pin as sword blades burst from their arms, dark train station. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Có người lai với quỷ bom, kéo chốt trên cổ để biến cơ thể thành vũ khí nổ, với sức phá hủy đáng sợ.

```text
Wide 16:9 landscape cinematic frame. a silhouette in a rainy night pulling a pin at the neck, explosions blossoming behind her like flowers. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Những người lai này cho thấy vũ khí hiện đại là một trong những nỗi sợ lớn nhất của con người thời nay. Và tr…

```text
Wide 16:9 landscape cinematic frame. a gallery of modern weapon shadows cast by ordinary-looking people. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: tên và dạng của người lai luôn gợi ý điểm mạnh và cách họ chiến đấu. Đọc tên là đoán được luật…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a tiny pin and a tiny chain, comparing them curiously. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58 · Con quỷ cưa máy: vì sao đặc biệt?

Lời: Và giờ tới bí ẩn lớn nhất phần một: vì sao con quỷ cưa máy lại được những thế lực mạnh nhất săn lùng?

```text
Wide 16:9 landscape cinematic frame. a mysterious hooded silhouette with glowing saw blades against a blood-red moon, shadows watching from rooftops. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Nhìn qua, cưa máy không phải nỗi sợ quá lớn. Nhưng truyện tiết lộ con quỷ cưa máy có một năng lực không con q…

```text
Wide 16:9 landscape cinematic frame. a small ordinary chainsaw on a workbench casting an enormous ominous shadow on the wall. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Khi nó ăn một con quỷ, khái niệm mà con quỷ đó đại diện sẽ bị xóa khỏi thế giới. Không chỉ con quỷ biến mất,…

```text
Wide 16:9 landscape cinematic frame. a history book whose pages are being erased blank one by one as a shadow feeds. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Truyện gợi ý rằng đã có những thứ từng tồn tại, nhưng giờ không ai nhớ, vì con quỷ của chúng đã bị ăn.

```text
Wide 16:9 landscape cinematic frame. empty frames on a museum wall with small plaques describing nothing. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Vì thế, trong địa ngục, những con quỷ sợ con quỷ cưa máy. Nó được gọi là anh hùng của địa ngục, thứ đáng sợ v…

```text
Wide 16:9 landscape cinematic frame. countless devil silhouettes fleeing in a pale hellscape as a single hooded figure with glowing saw blades approaches. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là nghịch lý thú vị. Trong một thế giới quỷ mạnh nhờ nỗi sợ, con quỷ mạnh nhất lại là thứ m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a circle with an arrow pointing back at itself on a chalkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · Quỷ kiểm soát và giấc mơ về một thế giới không có nỗi sợ

Lời: Phần một của truyện xoay quanh một nhân vật bí ẩn đứng sau mọi chuyện, được tiết lộ là quỷ kiểm soát.

```text
Wide 16:9 landscape cinematic frame. a calm figure silhouette with ringed eyes standing at a window, a leash of shadows in her hand. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Nỗi sợ về sự kiểm soát, bị người khác điều khiển, là một nỗi sợ rất sâu của con người. Và con quỷ này mạnh tư…

```text
Wide 16:9 landscape cinematic frame. puppet strings reaching down from the sky to many human silhouettes in a city square. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Mục tiêu của nó là dùng năng lực của con quỷ cưa máy để xóa đi những nỗi sợ, và tạo ra một thế giới mà nó cho…

```text
Wide 16:9 landscape cinematic frame. a pristine but lifeless city with no shadows, everything perfectly still. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Câu hỏi truyện đặt ra rất đáng suy nghĩ: một thế giới không có nỗi sợ, nhưng bị một kẻ kiểm soát, có thật sự…

```text
Wide 16:9 landscape cinematic frame. a perfect glass dome over a city, a single figure outside looking in with doubt. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nghĩ đây là lý do Chainsaw Man được yêu thích: đằng sau những cảnh máu me là câu hỏi về tự do, lựa chọn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a bench eating a simple piece of bread happily. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Denji và giấc mơ bình thường

Lời: Có một điều khiến Chainsaw Man khác các bộ shounen khác: nhân vật chính không mơ làm vua hay mạnh nhất thế gi…

```text
Wide 16:9 landscape cinematic frame. a young man eating a simple slice of bread with jam at a tiny table, soft morning light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Denji lớn lên trong nợ nần và đói khát. Giấc mơ của anh chỉ là được ăn bánh mì với mứt, được ngủ trên giường…

```text
Wide 16:9 landscape cinematic frame. a shabby shack at night with a thin blanket and an empty plate, then a warm apartment with a full plate. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Chính giấc mơ nhỏ bé đó làm anh trở thành một nhân vật đặc biệt. Trong một thế giới đầy nỗi sợ, anh chiến đấu…

```text
Wide 16:9 landscape cinematic frame. a hooded silhouette with glowing saw blades standing protectively in front of a small warm window with light inside. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Và đó cũng là đối trọng hoàn hảo với tham vọng kiểm soát của những kẻ mạnh: một người chỉ muốn tự do sống cuộ…

```text
Wide 16:9 landscape cinematic frame. two figures facing each other: one holding puppet strings, one holding a simple bread roll. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích điều này. Đôi khi, mục tiêu đáng chiến đấu nhất không phải thứ vĩ đại, mà là một bữa sáng yên…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sharing a piece of bread with a small bird on a windowsill. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Thử nghiệm: bạn sẽ ký khế ước với quỷ nào?

Lời: Giờ tới trò chơi đen tối nhưng thú vị: nếu là thợ săn quỷ, bạn sẽ ký khế ước với loại quỷ nào?

```text
Wide 16:9 landscape cinematic frame. three glowing contracts floating in the dark, each with a different shadowy signature. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Lựa chọn an toàn: một con quỷ yếu với cái giá nhỏ. Bạn không mạnh lên nhiều, nhưng cũng không mất nhiều.

```text
Wide 16:9 landscape cinematic frame. a small cute shadow creature holding a tiny contract, asking for a snack as payment. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Lựa chọn mạo hiểm: một con quỷ mạnh với cái giá là tuổi thọ. Bạn trở thành thợ săn đáng gờm, nhưng mỗi trận c…

```text
Wide 16:9 landscape cinematic frame. a figure with a glowing weapon, an hourglass on their back draining quickly. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Lựa chọn thông minh: một con quỷ có năng lực đặc biệt như nhìn thấy tương lai, dù giá đắt, vì thông tin thườn…

```text
Wide 16:9 landscape cinematic frame. a hunter with one eye covered, faint images of the next few seconds floating before them. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thì chọn không ký gì cả, về nhà ăn bánh mì với mứt. Trong thế giới này, sống bình thường đã là một chiến…

```text
Wide 16:9 landscape cinematic frame. the owl mascot happily eating bread with jam at a small kitchen table. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79 · Những hiểu lầm về ác quỷ

Lời: Cùng gỡ vài hiểu lầm hay gặp về luật ác quỷ trong Chainsaw Man.

```text
Wide 16:9 landscape cinematic frame. a notice board with four pinned cards with red question marks. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Hiểu lầm một: quỷ trông càng đáng sợ thì càng mạnh. Không đúng, sức mạnh tùy vào mức độ con người sợ khái niệ…

```text
Wide 16:9 landscape cinematic frame. a terrifying-looking but weak creature next to a plain-looking but powerful figure. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Hiểu lầm hai: giết quỷ là hết quỷ. Như mình nói, chúng tái sinh giữa địa ngục và trái đất.

```text
Wide 16:9 landscape cinematic frame. a looping arrow between two worlds with a devil icon. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Hiểu lầm ba: khế ước luôn là thiệt cho con người. Có những khế ước thông minh, nơi con người trả giá nhỏ mà n…

```text
Wide 16:9 landscape cinematic frame. a clever human smiling across a table from a grumbling devil holding a tiny payment. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hiểu lầm bốn: Denji mạnh vì cưa máy sắc. Sức mạnh thật của anh nằm ở năng lực độc nhất của con quỷ cưa máy, v…

```text
Wide 16:9 landscape cinematic frame. a battered hooded figure with glowing saw blades standing up again in the rain, determined. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Góc nhìn của Kaku: nỗi sợ như một hệ thống · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn lại toàn bộ, vì sao hệ thống nỗi sợ của Chainsaw Man lại hay đến vậy?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting in a dim room with a single lamp, reflecting. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Lý do một: nó gắn sức mạnh với thế giới thật. Súng, bệnh tật, chiến tranh đều là nỗi sợ có thật, và truyện bi…

```text
Wide 16:9 landscape cinematic frame. real-world fear symbols drawn as abstract shadows: a gun barrel, a virus shape, a crumbling building. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Lý do hai: nó có luật rõ ràng mà vẫn khó đoán. Ai cũng hiểu sợ nhiều thì mạnh, nhưng không ai biết trước con…

```text
Wide 16:9 landscape cinematic frame. a deck of face-down cards each with a shadow leaking from the edges. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Lý do ba: nó phản chiếu xã hội. Mỗi thời đại có nỗi sợ riêng, và những con quỷ mạnh nhất cho thấy xã hội đang…

```text
Wide 16:9 landscape cinematic frame. a mirror reflecting a modern city skyline full of looming shadows. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: So với các hệ thống mình đã giải thích, Chainsaw Man là hệ thống duy nhất mà sức mạnh không nằm trong nhân vậ…

```text
Wide 16:9 landscape cinematic frame. a hexagon, a lung icon, a red eye, and a crowd of human silhouettes whose shadows form a devil. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Nỗi sợ ngoài đời thật

Lời: Trước khi tổng kết, thử áp luật của Chainsaw Man vào thế giới thật một chút. Nếu nỗi sợ tạo ra quỷ, thì quỷ n…

```text
Wide 16:9 landscape cinematic frame. a modern city at night with faint shadows rising from glowing phone screens and news tickers. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Có thể là nỗi sợ bệnh tật, nỗi sợ thất nghiệp, nỗi sợ bị bỏ lại phía sau. Những nỗi sợ này không có hình dạng…

```text
Wide 16:9 landscape cinematic frame. a crowd of silhouettes each carrying a small shadow on their back, walking through a busy street. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91

Lời: Bài học nhẹ nhàng mà truyện gợi ra: nỗi sợ càng được nuôi lớn thì càng mạnh. Hiểu nó, gọi tên nó, là cách đầu…

```text
Wide 16:9 landscape cinematic frame. a person shining a small flashlight at a large shadow, which shrinks into a small harmless shape. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s92 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku không phải chuyên gia tâm lý, nhưng Kaku biết một điều: kể nỗi sợ cho người mình tin tưởng thường giúp n…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting next to a small friend on a bench under a streetlight, talking quietly. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s93 · Tóm tắt

Lời: Tóm lại: quỷ sinh ra từ nỗi sợ của con người, và con người càng sợ thì quỷ càng mạnh.

```text
Wide 16:9 landscape cinematic frame. a summary diagram: human fear flowing into a growing devil silhouette. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s94

Lời: Quỷ tái sinh giữa địa ngục và trái đất. Con người chiến đấu bằng khế ước, trả giá bằng cơ thể hoặc tuổi thọ.

```text
Wide 16:9 landscape cinematic frame. a looping arrow between two worlds next to a contract with a price tag. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s95

Lời: Và con quỷ cưa máy đặc biệt vì khi ăn quỷ, nó xóa cả khái niệm đó khỏi thế giới.

```text
Wide 16:9 landscape cinematic frame. an eraser wiping a word off an old book page, leaving a blank space. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s96 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nỗi sợ nào của bạn, nếu thành quỷ, sẽ mạnh nhất? Viết xuống phần bình luận nhé, nhưng đừng s…

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking out from under a blanket with a flashlight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s97 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ so sánh Chakra, Nen và Chú lực: hệ thống nào chặt chẽ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at three glowing symbols arranged in a triangle. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s98 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp sổ đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a glowing notebook and waving goodbye under a single streetlight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Quỷ sinh ra từ đâu?

Khoảng 116 giây · cảnh s01–s12 · 1514 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Chainsaw Man đến hết phần một của manga, nhiều hơn phần anime đã chiếu. Nếu chỉ xem anime, bạn cân nhắc nhé.

<short pause> Trong thế giới Chainsaw Man, có những con quỷ yếu tới mức một đứa trẻ cũng đánh thắng. Và có những con quỷ mạnh tới mức giết hàng nghìn người trong vài giây.

<short pause> Điều gì tạo ra sự khác biệt đó? Không phải tuổi tác, không phải luyện tập. Mà là việc con người sợ chúng tới mức nào.

<short pause> Đây là một trong những hệ thống sức mạnh độc đáo nhất anime: sức mạnh của quỷ được quyết định bởi nỗi sợ của chính chúng ta.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình sẽ giải mã luật ác quỷ: chúng sinh ra thế nào, khế ước là gì, và vì sao con quỷ cưa máy lại đặc biệt đến vậy.

<short pause> Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, thứ đáng sợ nhất không phải con quỷ, mà là nỗi sợ trong đầu con người.

<short pause> Luật đầu tiên: mỗi con quỷ mang tên một khái niệm hoặc sự vật mà con người sợ. Có quỷ bóng tối, quỷ súng, quỷ lửa, quỷ cà chua.

<short pause> Chúng sinh ra từ nỗi sợ tập thể của loài người về khái niệm đó. Thứ gì tồn tại trong nỗi sợ của con người, thứ đó có thể thành quỷ.

<short pause> Luật thứ hai: con người càng sợ khái niệm nào, con quỷ mang tên khái niệm đó càng mạnh.

<short pause> Vì vậy quỷ cà chua thì yếu, vì ít ai thật sự sợ cà chua. Còn quỷ súng thì cực mạnh, vì súng là nỗi sợ của hàng tỉ người.

<short pause> Điều này có nghĩa là sức mạnh của quỷ thay đổi theo thời đại. Một nỗi sợ xưa cũ bị lãng quên, con quỷ đó cũng yếu đi.

<short pause> Kaku ghi chú: đây là một hệ thống sức mạnh mà người xem góp phần tạo ra. Chính nỗi sợ của xã hội là nguồn năng lượng của quỷ.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Chainsaw Man đến hết phần một của manga, nhiều hơn phần anime đã chiếu. Nếu chỉ xem anime, bạn cân nhắc nhé.

[pause] Trong thế giới Chainsaw Man, có những con quỷ yếu tới mức một đứa trẻ cũng đánh thắng. Và có những con quỷ mạnh tới mức giết hàng nghìn người trong vài giây.

[pause] [curious] Điều gì tạo ra sự khác biệt đó? Không phải tuổi tác, không phải luyện tập. Mà là việc con người sợ chúng tới mức nào.

[pause] Đây là một trong những hệ thống sức mạnh độc đáo nhất anime: sức mạnh của quỷ được quyết định bởi nỗi sợ của chính chúng ta.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình sẽ giải mã luật ác quỷ: chúng sinh ra thế nào, khế ước là gì, và vì sao con quỷ cưa máy lại đặc biệt đến vậy.

[pause] Xem hết video, bạn sẽ hiểu vì sao trong thế giới này, thứ đáng sợ nhất không phải con quỷ, mà là nỗi sợ trong đầu con người.

[pause] Luật đầu tiên: mỗi con quỷ mang tên một khái niệm hoặc sự vật mà con người sợ. Có quỷ bóng tối, quỷ súng, quỷ lửa, quỷ cà chua.

[pause] Chúng sinh ra từ nỗi sợ tập thể của loài người về khái niệm đó. Thứ gì tồn tại trong nỗi sợ của con người, thứ đó có thể thành quỷ.

[pause] Luật thứ hai: con người càng sợ khái niệm nào, con quỷ mang tên khái niệm đó càng mạnh.

[pause] Vì vậy quỷ cà chua thì yếu, vì ít ai thật sự sợ cà chua. Còn quỷ súng thì cực mạnh, vì súng là nỗi sợ của hàng tỉ người.

[pause] Điều này có nghĩa là sức mạnh của quỷ thay đổi theo thời đại. Một nỗi sợ xưa cũ bị lãng quên, con quỷ đó cũng yếu đi.

[pause] Kaku ghi chú: đây là một hệ thống sức mạnh mà người xem góp phần tạo ra. Chính nỗi sợ của xã hội là nguồn năng lượng của quỷ.
```

### c02 · Địa ngục và vòng luân hồi / Nỗi sợ nguyên thủy

Khoảng 93 giây · cảnh s13–s22 · 1205 ký tự

**Gemini**

```text
Luật thứ ba: quỷ không thật sự chết. Khi bị giết trên trái đất, chúng tái sinh ở địa ngục. Khi chết ở địa ngục, chúng tái sinh trên trái đất.

<short pause> Khi tái sinh, quỷ thường mất ký ức và phải bắt đầu lại, nhưng khái niệm mà nó đại diện vẫn còn đó.

<short pause> Vì vậy thợ săn quỷ không bao giờ thật sự tiêu diệt được một nỗi sợ. Họ chỉ đẩy nó sang phía bên kia, và nó sẽ quay lại.

<short pause> Địa ngục trong truyện là một nơi kỳ lạ, nơi những con quỷ mạnh nhất chưa từng chết lần nào vẫn đang tồn tại. Đó là những nỗi sợ nguyên thủy.

<short pause> <laugh> Kaku ví von: đánh bại quỷ giống tắt một bóng đèn. Đèn tắt ở phòng này, nhưng sẽ sáng lại ở một phòng khác.

<short pause> Có một nhóm quỷ đặc biệt được gọi là nỗi sợ nguyên thủy. Chúng đại diện cho những nỗi sợ sâu nhất, có từ thuở con người mới xuất hiện.

<short pause> Đó là những thứ như bóng tối, sự rơi, cái chết, những nỗi sợ không cần ai dạy, đứa trẻ nào cũng có.

<short pause> Những con quỷ này mạnh tới mức ngay cả thợ săn quỷ giỏi nhất cũng gần như bất lực. Truyện mô tả chúng như thiên tai hơn là kẻ thù.

<short pause> Điều thú vị: chúng chưa từng bị giết, nên chưa từng tái sinh. Chúng là những ký ức cổ xưa nhất của nỗi sợ loài người.

<short pause> Kaku rùng mình: nếu sức mạnh đến từ nỗi sợ, thì nỗi sợ có từ lâu nhất sẽ là thứ mạnh nhất. Logic rất đơn giản mà đáng sợ.
```

**ElevenLabs**

```text
Luật thứ ba: quỷ không thật sự chết. Khi bị giết trên trái đất, chúng tái sinh ở địa ngục. Khi chết ở địa ngục, chúng tái sinh trên trái đất.

[pause] Khi tái sinh, quỷ thường mất ký ức và phải bắt đầu lại, nhưng khái niệm mà nó đại diện vẫn còn đó.

[pause] Vì vậy thợ săn quỷ không bao giờ thật sự tiêu diệt được một nỗi sợ. Họ chỉ đẩy nó sang phía bên kia, và nó sẽ quay lại.

[pause] Địa ngục trong truyện là một nơi kỳ lạ, nơi những con quỷ mạnh nhất chưa từng chết lần nào vẫn đang tồn tại. Đó là những nỗi sợ nguyên thủy.

[pause] [chuckles] Kaku ví von: đánh bại quỷ giống tắt một bóng đèn. Đèn tắt ở phòng này, nhưng sẽ sáng lại ở một phòng khác.

[pause] Có một nhóm quỷ đặc biệt được gọi là nỗi sợ nguyên thủy. Chúng đại diện cho những nỗi sợ sâu nhất, có từ thuở con người mới xuất hiện.

[pause] Đó là những thứ như bóng tối, sự rơi, cái chết, những nỗi sợ không cần ai dạy, đứa trẻ nào cũng có.

[pause] Những con quỷ này mạnh tới mức ngay cả thợ săn quỷ giỏi nhất cũng gần như bất lực. Truyện mô tả chúng như thiên tai hơn là kẻ thù.

[pause] Điều thú vị: chúng chưa từng bị giết, nên chưa từng tái sinh. Chúng là những ký ức cổ xưa nhất của nỗi sợ loài người.

[pause] Kaku rùng mình: nếu sức mạnh đến từ nỗi sợ, thì nỗi sợ có từ lâu nhất sẽ là thứ mạnh nhất. Logic rất đơn giản mà đáng sợ.
```

### c03 · Những con quỷ tiêu biểu / Khế ước: con người mượn sức quỷ

Khoảng 136 giây · cảnh s23–s36 · 1772 ký tự

**Gemini**

```text
Để luật nỗi sợ dễ hình dung hơn, hãy xem vài con quỷ tiêu biểu và cách sức mạnh của chúng khớp với nỗi sợ của con người.

<short pause> Quỷ súng là ví dụ khủng khiếp nhất. Trong truyện, nó từng xuất hiện và giết hơn một triệu người chỉ trong vài phút, vì súng là nỗi sợ của cả thế giới.

<short pause> Sau sự kiện đó, súng bị kiểm soát gắt gao ở nhiều nơi. Điều này càng khiến con người sợ súng hơn, và vòng lặp nỗi sợ tiếp tục.

<short pause> Quỷ tương lai lập khế ước để cho người dùng nhìn thấy vài giây tương lai. Nó sống trong mắt người ký, và thích nói về tương lai theo cách đầy bí ẩn.

<short pause> Quỷ cáo là con quỷ được nhiều thợ săn dùng, triệu hồi bằng một thế tay. <short pause> Nhưng nó kén người, không phải ai nó cũng chịu giúp.

<short pause> Quỷ nguyền rủa cho phép giết đối thủ sau vài nhát đâm, nhưng người dùng trả bằng một phần tuổi thọ rất lớn. Mạnh nhưng cực đắt.

<short pause> Mỗi con quỷ này cho thấy cùng một luật: năng lực của quỷ gắn với nỗi sợ mà nó đại diện, và cái giá luôn đi kèm.

<short pause> Con người yếu hơn quỷ rất nhiều. Vậy họ chiến đấu bằng cách nào? Câu trả lời là khế ước.

<short pause> Thợ săn quỷ có thể lập khế ước với một con quỷ để mượn sức mạnh của nó. Đổi lại, họ phải trả một cái giá.

<short pause> Cái giá có thể là một phần cơ thể, một phần tuổi thọ, hay một thứ gì đó quý giá khác. Quỷ càng mạnh, cái giá càng đắt.

<short pause> Có người đưa một con mắt để đổi lấy khả năng nhìn thấy tương lai gần. Có người trả bằng nhiều năm tuổi thọ để dùng một lời nguyền chết người.

<short pause> Khế ước nghe giống giao ước trong Nen mà mình từng giải thích. <short pause> Nhưng ở đây, bạn không tự đặt luật. Bạn thương lượng với một sinh vật muốn lấy nhiều nhất có thể.

<short pause> Và quỷ không phải lúc nào cũng giữ lời theo cách con người mong muốn. Một khế ước sai có thể lấy đi nhiều hơn những gì bạn tưởng.

<short pause> <laugh> Kaku ghi chú: nếu có ngày bạn định ký khế ước với quỷ, hãy đọc kỹ điều khoản. Đó là lời khuyên hữu ích cả ngoài đời thật nữa.
```

**ElevenLabs**

```text
Để luật nỗi sợ dễ hình dung hơn, hãy xem vài con quỷ tiêu biểu và cách sức mạnh của chúng khớp với nỗi sợ của con người.

[pause] Quỷ súng là ví dụ khủng khiếp nhất. Trong truyện, nó từng xuất hiện và giết hơn một triệu người chỉ trong vài phút, vì súng là nỗi sợ của cả thế giới.

[pause] Sau sự kiện đó, súng bị kiểm soát gắt gao ở nhiều nơi. Điều này càng khiến con người sợ súng hơn, và vòng lặp nỗi sợ tiếp tục.

[pause] Quỷ tương lai lập khế ước để cho người dùng nhìn thấy vài giây tương lai. Nó sống trong mắt người ký, và thích nói về tương lai theo cách đầy bí ẩn.

[pause] Quỷ cáo là con quỷ được nhiều thợ săn dùng, triệu hồi bằng một thế tay. [pause] Nhưng nó kén người, không phải ai nó cũng chịu giúp.

[pause] Quỷ nguyền rủa cho phép giết đối thủ sau vài nhát đâm, nhưng người dùng trả bằng một phần tuổi thọ rất lớn. Mạnh nhưng cực đắt.

[pause] Mỗi con quỷ này cho thấy cùng một luật: năng lực của quỷ gắn với nỗi sợ mà nó đại diện, và cái giá luôn đi kèm.

[pause] Con người yếu hơn quỷ rất nhiều. [curious] Vậy họ chiến đấu bằng cách nào? Câu trả lời là khế ước.

[pause] Thợ săn quỷ có thể lập khế ước với một con quỷ để mượn sức mạnh của nó. Đổi lại, họ phải trả một cái giá.

[pause] Cái giá có thể là một phần cơ thể, một phần tuổi thọ, hay một thứ gì đó quý giá khác. Quỷ càng mạnh, cái giá càng đắt.

[pause] Có người đưa một con mắt để đổi lấy khả năng nhìn thấy tương lai gần. Có người trả bằng nhiều năm tuổi thọ để dùng một lời nguyền chết người.

[pause] Khế ước nghe giống giao ước trong Nen mà mình từng giải thích. [pause] Nhưng ở đây, bạn không tự đặt luật. Bạn thương lượng với một sinh vật muốn lấy nhiều nhất có thể.

[pause] Và quỷ không phải lúc nào cũng giữ lời theo cách con người mong muốn. Một khế ước sai có thể lấy đi nhiều hơn những gì bạn tưởng.

[pause] [chuckles] Kaku ghi chú: nếu có ngày bạn định ký khế ước với quỷ, hãy đọc kỹ điều khoản. Đó là lời khuyên hữu ích cả ngoài đời thật nữa.
```

### c04 · Thợ săn quỷ công an / Cách con người đánh bại quỷ mạnh hơn mình / Ma nhân và người lai quỷ

Khoảng 139 giây · cảnh s37–s52 · 1803 ký tự

**Gemini**

```text
Trong truyện, săn quỷ là một nghề chính thức. Có thợ săn tư nhân, và có Thợ săn quỷ công an, một tổ chức của nhà nước.

<short pause> Thợ săn quỷ công an nhận nhiệm vụ nguy hiểm nhất, và họ thường dùng khế ước với những con quỷ mạnh để có sức đối đầu.

<short pause> Nghề này có tỉ lệ tử vong cực cao. Truyện liên tục cho thấy những thợ săn chết sớm, thậm chí chết một cách đột ngột không ai ngờ.

<short pause> Điều đó làm thế giới Chainsaw Man có cảm giác rất lạnh lùng: không ai an toàn, kể cả những nhân vật tưởng như sẽ sống tới cuối.

<short pause> Nếu quỷ mạnh hơn người nhiều như vậy, làm sao thợ săn vẫn thắng được? Truyện cho thấy vài chiến thuật lặp lại.

<short pause> Chiến thuật một: dùng quỷ đánh quỷ. Khế ước cho phép con người đưa một con quỷ mạnh ra đối đầu với con quỷ khác.

<short pause> Chiến thuật hai: làm việc theo đội. Mỗi người mang một khế ước khác nhau, bù trừ điểm yếu cho nhau.

<short pause> Chiến thuật ba: lợi dụng điểm yếu của nỗi sợ. Quỷ gắn với một khái niệm, nên hiểu khái niệm đó là hiểu cách đánh bại nó.

<short pause> Chiến thuật bốn, đen tối nhất: chấp nhận trả giá cực đắt, bằng tuổi thọ hay một phần cơ thể, cho một đòn quyết định.

<short pause> <laugh> Kaku nhận xét: trong Chainsaw Man, chiến thắng hiếm khi sạch sẽ. Ai thắng cũng phải mất một thứ gì đó.

<short pause> Ngoài quỷ và con người, truyện còn có hai dạng lai rất quan trọng: ma nhân và người lai quỷ.

<short pause> Ma nhân là quỷ chiếm lấy xác người chết. Chúng yếu hơn quỷ thật, và thường có đặc điểm lạ trên đầu như sừng.

<short pause> Power, cô gái ma nhân máu nổi tiếng, là ví dụ tiêu biểu: vừa nguy hiểm, vừa trẻ con, vừa đáng yêu theo một cách rất hỗn loạn.

<short pause> Người lai quỷ thì khác: họ là con người có thể biến thành quỷ, thường bằng một hành động kích hoạt cụ thể.

<short pause> Denji là người lai với quỷ cưa máy. Anh kéo sợi dây trên ngực, và cưa máy mọc ra từ đầu và tay.

<short pause> Người lai có một lợi thế lớn: họ hồi phục khi uống máu. Điều đó giúp họ trụ được những vết thương mà người thường sẽ chết ngay.
```

**ElevenLabs**

```text
Trong truyện, săn quỷ là một nghề chính thức. Có thợ săn tư nhân, và có Thợ săn quỷ công an, một tổ chức của nhà nước.

[pause] Thợ săn quỷ công an nhận nhiệm vụ nguy hiểm nhất, và họ thường dùng khế ước với những con quỷ mạnh để có sức đối đầu.

[pause] Nghề này có tỉ lệ tử vong cực cao. Truyện liên tục cho thấy những thợ săn chết sớm, thậm chí chết một cách đột ngột không ai ngờ.

[pause] Điều đó làm thế giới Chainsaw Man có cảm giác rất lạnh lùng: không ai an toàn, kể cả những nhân vật tưởng như sẽ sống tới cuối.

[pause] [curious] Nếu quỷ mạnh hơn người nhiều như vậy, làm sao thợ săn vẫn thắng được? Truyện cho thấy vài chiến thuật lặp lại.

[pause] Chiến thuật một: dùng quỷ đánh quỷ. Khế ước cho phép con người đưa một con quỷ mạnh ra đối đầu với con quỷ khác.

[pause] Chiến thuật hai: làm việc theo đội. Mỗi người mang một khế ước khác nhau, bù trừ điểm yếu cho nhau.

[pause] Chiến thuật ba: lợi dụng điểm yếu của nỗi sợ. Quỷ gắn với một khái niệm, nên hiểu khái niệm đó là hiểu cách đánh bại nó.

[pause] Chiến thuật bốn, đen tối nhất: chấp nhận trả giá cực đắt, bằng tuổi thọ hay một phần cơ thể, cho một đòn quyết định.

[pause] [chuckles] Kaku nhận xét: trong Chainsaw Man, chiến thắng hiếm khi sạch sẽ. Ai thắng cũng phải mất một thứ gì đó.

[pause] Ngoài quỷ và con người, truyện còn có hai dạng lai rất quan trọng: ma nhân và người lai quỷ.

[pause] Ma nhân là quỷ chiếm lấy xác người chết. Chúng yếu hơn quỷ thật, và thường có đặc điểm lạ trên đầu như sừng.

[pause] Power, cô gái ma nhân máu nổi tiếng, là ví dụ tiêu biểu: vừa nguy hiểm, vừa trẻ con, vừa đáng yêu theo một cách rất hỗn loạn.

[pause] Người lai quỷ thì khác: họ là con người có thể biến thành quỷ, thường bằng một hành động kích hoạt cụ thể.

[pause] Denji là người lai với quỷ cưa máy. Anh kéo sợi dây trên ngực, và cưa máy mọc ra từ đầu và tay.

[pause] Người lai có một lợi thế lớn: họ hồi phục khi uống máu. Điều đó giúp họ trụ được những vết thương mà người thường sẽ chết ngay.
```

### c05 · Người lai khác: kiếm và bom / Con quỷ cưa máy: vì sao đặc biệt? / Quỷ kiểm soát và giấc mơ về một thế giới không có nỗi sợ

Khoảng 148 giây · cảnh s53–s68 · 1923 ký tự

**Gemini**

```text
Denji không phải người lai duy nhất. Truyện còn có những người lai khác, mỗi người mang một loại vũ khí làm nỗi sợ.

<short pause> Có người lai với quỷ kiếm, rút một chốt để biến tay và đầu thành những lưỡi kiếm sắc lẻm.

<short pause> Có người lai với quỷ bom, kéo chốt trên cổ để biến cơ thể thành vũ khí nổ, với sức phá hủy đáng sợ.

<short pause> Những người lai này cho thấy vũ khí hiện đại là một trong những nỗi sợ lớn nhất của con người thời nay. Và truyện biến chúng thành những đối thủ vừa đẹp vừa đáng sợ.

<short pause> <laugh> Kaku ghi chú: tên và dạng của người lai luôn gợi ý điểm mạnh và cách họ chiến đấu. Đọc tên là đoán được luật chơi.

<short pause> Và giờ tới bí ẩn lớn nhất phần một: vì sao con quỷ cưa máy lại được những thế lực mạnh nhất săn lùng?

<short pause> Nhìn qua, cưa máy không phải nỗi sợ quá lớn. <short pause> Nhưng truyện tiết lộ con quỷ cưa máy có một năng lực không con quỷ nào khác có.

<short pause> Khi nó ăn một con quỷ, khái niệm mà con quỷ đó đại diện sẽ bị xóa khỏi thế giới. Không chỉ con quỷ biến mất, mà cả nỗi sợ và ký ức về thứ đó cũng biến mất.

<short pause> Truyện gợi ý rằng đã có những thứ từng tồn tại, nhưng giờ không ai nhớ, vì con quỷ của chúng đã bị ăn.

<short pause> Vì thế, trong địa ngục, những con quỷ sợ con quỷ cưa máy. Nó được gọi là anh hùng của địa ngục, thứ đáng sợ với cả quỷ.

<short pause> Kaku ghi chú: đây là nghịch lý thú vị. Trong một thế giới quỷ mạnh nhờ nỗi sợ, con quỷ mạnh nhất lại là thứ mà chính quỷ sợ hãi.

<short pause> Phần một của truyện xoay quanh một nhân vật bí ẩn đứng sau mọi chuyện, được tiết lộ là quỷ kiểm soát.

<short pause> Nỗi sợ về sự kiểm soát, bị người khác điều khiển, là một nỗi sợ rất sâu của con người. Và con quỷ này mạnh tương xứng.

<short pause> Mục tiêu của nó là dùng năng lực của con quỷ cưa máy để xóa đi những nỗi sợ, và tạo ra một thế giới mà nó cho là tốt đẹp hơn.

<short pause> Câu hỏi truyện đặt ra rất đáng suy nghĩ: một thế giới không có nỗi sợ, nhưng bị một kẻ kiểm soát, có thật sự tốt đẹp không?

<short pause> Kaku nghĩ đây là lý do Chainsaw Man được yêu thích: đằng sau những cảnh máu me là câu hỏi về tự do, lựa chọn và thế nào là hạnh phúc bình thường.
```

**ElevenLabs**

```text
Denji không phải người lai duy nhất. Truyện còn có những người lai khác, mỗi người mang một loại vũ khí làm nỗi sợ.

[pause] Có người lai với quỷ kiếm, rút một chốt để biến tay và đầu thành những lưỡi kiếm sắc lẻm.

[pause] Có người lai với quỷ bom, kéo chốt trên cổ để biến cơ thể thành vũ khí nổ, với sức phá hủy đáng sợ.

[pause] Những người lai này cho thấy vũ khí hiện đại là một trong những nỗi sợ lớn nhất của con người thời nay. Và truyện biến chúng thành những đối thủ vừa đẹp vừa đáng sợ.

[pause] [chuckles] Kaku ghi chú: tên và dạng của người lai luôn gợi ý điểm mạnh và cách họ chiến đấu. Đọc tên là đoán được luật chơi.

[pause] [curious] Và giờ tới bí ẩn lớn nhất phần một: vì sao con quỷ cưa máy lại được những thế lực mạnh nhất săn lùng?

[pause] Nhìn qua, cưa máy không phải nỗi sợ quá lớn. [pause] Nhưng truyện tiết lộ con quỷ cưa máy có một năng lực không con quỷ nào khác có.

[pause] Khi nó ăn một con quỷ, khái niệm mà con quỷ đó đại diện sẽ bị xóa khỏi thế giới. Không chỉ con quỷ biến mất, mà cả nỗi sợ và ký ức về thứ đó cũng biến mất.

[pause] Truyện gợi ý rằng đã có những thứ từng tồn tại, nhưng giờ không ai nhớ, vì con quỷ của chúng đã bị ăn.

[pause] Vì thế, trong địa ngục, những con quỷ sợ con quỷ cưa máy. Nó được gọi là anh hùng của địa ngục, thứ đáng sợ với cả quỷ.

[pause] Kaku ghi chú: đây là nghịch lý thú vị. Trong một thế giới quỷ mạnh nhờ nỗi sợ, con quỷ mạnh nhất lại là thứ mà chính quỷ sợ hãi.

[pause] Phần một của truyện xoay quanh một nhân vật bí ẩn đứng sau mọi chuyện, được tiết lộ là quỷ kiểm soát.

[pause] Nỗi sợ về sự kiểm soát, bị người khác điều khiển, là một nỗi sợ rất sâu của con người. Và con quỷ này mạnh tương xứng.

[pause] Mục tiêu của nó là dùng năng lực của con quỷ cưa máy để xóa đi những nỗi sợ, và tạo ra một thế giới mà nó cho là tốt đẹp hơn.

[pause] Câu hỏi truyện đặt ra rất đáng suy nghĩ: một thế giới không có nỗi sợ, nhưng bị một kẻ kiểm soát, có thật sự tốt đẹp không?

[pause] Kaku nghĩ đây là lý do Chainsaw Man được yêu thích: đằng sau những cảnh máu me là câu hỏi về tự do, lựa chọn và thế nào là hạnh phúc bình thường.
```

### c06 · Denji và giấc mơ bình thường / Thử nghiệm: bạn sẽ ký khế ước với quỷ nào? / Những hiểu lầm về ác quỷ

Khoảng 139 giây · cảnh s69–s83 · 1806 ký tự

**Gemini**

```text
Có một điều khiến Chainsaw Man khác các bộ shounen khác: nhân vật chính không mơ làm vua hay mạnh nhất thế giới.

<short pause> Denji lớn lên trong nợ nần và đói khát. Giấc mơ của anh chỉ là được ăn bánh mì với mứt, được ngủ trên giường ấm, và sống như một người bình thường.

<short pause> Chính giấc mơ nhỏ bé đó làm anh trở thành một nhân vật đặc biệt. Trong một thế giới đầy nỗi sợ, anh chiến đấu vì những điều giản dị.

<short pause> Và đó cũng là đối trọng hoàn hảo với tham vọng kiểm soát của những kẻ mạnh: một người chỉ muốn tự do sống cuộc đời bình thường của mình.

<short pause> <laugh> Kaku rất thích điều này. Đôi khi, mục tiêu đáng chiến đấu nhất không phải thứ vĩ đại, mà là một bữa sáng yên bình.

<short pause> Giờ tới trò chơi đen tối nhưng thú vị: nếu là thợ săn quỷ, bạn sẽ ký khế ước với loại quỷ nào?

<short pause> Lựa chọn an toàn: một con quỷ yếu với cái giá nhỏ. Bạn không mạnh lên nhiều, nhưng cũng không mất nhiều.

<short pause> Lựa chọn mạo hiểm: một con quỷ mạnh với cái giá là tuổi thọ. Bạn trở thành thợ săn đáng gờm, nhưng mỗi trận chiến đều rút ngắn cuộc đời.

<short pause> Lựa chọn thông minh: một con quỷ có năng lực đặc biệt như nhìn thấy tương lai, dù giá đắt, vì thông tin thường quyết định sống còn.

<short pause> Kaku thì chọn không ký gì cả, về nhà ăn bánh mì với mứt. Trong thế giới này, sống bình thường đã là một chiến thắng.

<short pause> Cùng gỡ vài hiểu lầm hay gặp về luật ác quỷ trong Chainsaw Man.

<short pause> Hiểu lầm một: quỷ trông càng đáng sợ thì càng mạnh. Không đúng, sức mạnh tùy vào mức độ con người sợ khái niệm, không phải ngoại hình.

<short pause> Hiểu lầm hai: giết quỷ là hết quỷ. Như mình nói, chúng tái sinh giữa địa ngục và trái đất.

<short pause> Hiểu lầm ba: khế ước luôn là thiệt cho con người. Có những khế ước thông minh, nơi con người trả giá nhỏ mà nhận lợi ích lớn, nhờ biết thương lượng.

<short pause> Hiểu lầm bốn: Denji mạnh vì cưa máy sắc. Sức mạnh thật của anh nằm ở năng lực độc nhất của con quỷ cưa máy, và ở việc anh không bao giờ chịu bỏ cuộc.
```

**ElevenLabs**

```text
Có một điều khiến Chainsaw Man khác các bộ shounen khác: nhân vật chính không mơ làm vua hay mạnh nhất thế giới.

[pause] Denji lớn lên trong nợ nần và đói khát. Giấc mơ của anh chỉ là được ăn bánh mì với mứt, được ngủ trên giường ấm, và sống như một người bình thường.

[pause] Chính giấc mơ nhỏ bé đó làm anh trở thành một nhân vật đặc biệt. Trong một thế giới đầy nỗi sợ, anh chiến đấu vì những điều giản dị.

[pause] Và đó cũng là đối trọng hoàn hảo với tham vọng kiểm soát của những kẻ mạnh: một người chỉ muốn tự do sống cuộc đời bình thường của mình.

[pause] [chuckles] Kaku rất thích điều này. Đôi khi, mục tiêu đáng chiến đấu nhất không phải thứ vĩ đại, mà là một bữa sáng yên bình.

[pause] [curious] Giờ tới trò chơi đen tối nhưng thú vị: nếu là thợ săn quỷ, bạn sẽ ký khế ước với loại quỷ nào?

[pause] Lựa chọn an toàn: một con quỷ yếu với cái giá nhỏ. Bạn không mạnh lên nhiều, nhưng cũng không mất nhiều.

[pause] Lựa chọn mạo hiểm: một con quỷ mạnh với cái giá là tuổi thọ. Bạn trở thành thợ săn đáng gờm, nhưng mỗi trận chiến đều rút ngắn cuộc đời.

[pause] Lựa chọn thông minh: một con quỷ có năng lực đặc biệt như nhìn thấy tương lai, dù giá đắt, vì thông tin thường quyết định sống còn.

[pause] Kaku thì chọn không ký gì cả, về nhà ăn bánh mì với mứt. Trong thế giới này, sống bình thường đã là một chiến thắng.

[pause] Cùng gỡ vài hiểu lầm hay gặp về luật ác quỷ trong Chainsaw Man.

[pause] Hiểu lầm một: quỷ trông càng đáng sợ thì càng mạnh. Không đúng, sức mạnh tùy vào mức độ con người sợ khái niệm, không phải ngoại hình.

[pause] Hiểu lầm hai: giết quỷ là hết quỷ. Như mình nói, chúng tái sinh giữa địa ngục và trái đất.

[pause] Hiểu lầm ba: khế ước luôn là thiệt cho con người. Có những khế ước thông minh, nơi con người trả giá nhỏ mà nhận lợi ích lớn, nhờ biết thương lượng.

[pause] Hiểu lầm bốn: Denji mạnh vì cưa máy sắc. Sức mạnh thật của anh nằm ở năng lực độc nhất của con quỷ cưa máy, và ở việc anh không bao giờ chịu bỏ cuộc.
```

### c07 · Góc nhìn của Kaku: nỗi sợ như một hệ thống / Nỗi sợ ngoài đời thật / Tóm tắt

Khoảng 130 giây · cảnh s84–s98 · 1695 ký tự

**Gemini**

```text
Nhìn lại toàn bộ, vì sao hệ thống nỗi sợ của Chainsaw Man lại hay đến vậy?

<short pause> Lý do một: nó gắn sức mạnh với thế giới thật. Súng, bệnh tật, chiến tranh đều là nỗi sợ có thật, và truyện biến chúng thành quái vật.

<short pause> Lý do hai: nó có luật rõ ràng mà vẫn khó đoán. Ai cũng hiểu sợ nhiều thì mạnh, nhưng không ai biết trước con quỷ tiếp theo là nỗi sợ gì.

<short pause> Lý do ba: nó phản chiếu xã hội. Mỗi thời đại có nỗi sợ riêng, và những con quỷ mạnh nhất cho thấy xã hội đang sợ điều gì.

<short pause> So với các hệ thống mình đã giải thích, Chainsaw Man là hệ thống duy nhất mà sức mạnh không nằm trong nhân vật, mà nằm trong đầu của cả loài người.

<short pause> Trước khi tổng kết, thử áp luật của Chainsaw Man vào thế giới thật một chút. Nếu nỗi sợ tạo ra quỷ, thì quỷ nào sẽ mạnh nhất hôm nay?

<short pause> Có thể là nỗi sợ bệnh tật, nỗi sợ thất nghiệp, nỗi sợ bị bỏ lại phía sau. Những nỗi sợ này không có hình dạng, nhưng rất nhiều người cùng mang.

<short pause> Bài học nhẹ nhàng mà truyện gợi ra: nỗi sợ càng được nuôi lớn thì càng mạnh. Hiểu nó, gọi tên nó, là cách đầu tiên để nó nhỏ lại.

<short pause> <laugh> Kaku không phải chuyên gia tâm lý, nhưng Kaku biết một điều: kể nỗi sợ cho người mình tin tưởng thường giúp nó nhẹ đi rất nhiều.

<short pause> Tóm lại: quỷ sinh ra từ nỗi sợ của con người, và con người càng sợ thì quỷ càng mạnh.

<short pause> Quỷ tái sinh giữa địa ngục và trái đất. Con người chiến đấu bằng khế ước, trả giá bằng cơ thể hoặc tuổi thọ.

<short pause> Và con quỷ cưa máy đặc biệt vì khi ăn quỷ, nó xóa cả khái niệm đó khỏi thế giới.

<short pause> Câu hỏi cho bạn: nỗi sợ nào của bạn, nếu thành quỷ, sẽ mạnh nhất? Viết xuống phần bình luận nhé, nhưng đừng sợ quá kẻo nó mạnh lên đấy.

<short pause> Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ so sánh Chakra, Nen và Chú lực: hệ thống nào chặt chẽ nhất?

<short pause> Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[curious] Nhìn lại toàn bộ, vì sao hệ thống nỗi sợ của Chainsaw Man lại hay đến vậy?

[pause] Lý do một: nó gắn sức mạnh với thế giới thật. Súng, bệnh tật, chiến tranh đều là nỗi sợ có thật, và truyện biến chúng thành quái vật.

[pause] Lý do hai: nó có luật rõ ràng mà vẫn khó đoán. Ai cũng hiểu sợ nhiều thì mạnh, nhưng không ai biết trước con quỷ tiếp theo là nỗi sợ gì.

[pause] Lý do ba: nó phản chiếu xã hội. Mỗi thời đại có nỗi sợ riêng, và những con quỷ mạnh nhất cho thấy xã hội đang sợ điều gì.

[pause] So với các hệ thống mình đã giải thích, Chainsaw Man là hệ thống duy nhất mà sức mạnh không nằm trong nhân vật, mà nằm trong đầu của cả loài người.

[pause] Trước khi tổng kết, thử áp luật của Chainsaw Man vào thế giới thật một chút. Nếu nỗi sợ tạo ra quỷ, thì quỷ nào sẽ mạnh nhất hôm nay?

[pause] Có thể là nỗi sợ bệnh tật, nỗi sợ thất nghiệp, nỗi sợ bị bỏ lại phía sau. Những nỗi sợ này không có hình dạng, nhưng rất nhiều người cùng mang.

[pause] Bài học nhẹ nhàng mà truyện gợi ra: nỗi sợ càng được nuôi lớn thì càng mạnh. Hiểu nó, gọi tên nó, là cách đầu tiên để nó nhỏ lại.

[pause] [chuckles] Kaku không phải chuyên gia tâm lý, nhưng Kaku biết một điều: kể nỗi sợ cho người mình tin tưởng thường giúp nó nhẹ đi rất nhiều.

[pause] Tóm lại: quỷ sinh ra từ nỗi sợ của con người, và con người càng sợ thì quỷ càng mạnh.

[pause] Quỷ tái sinh giữa địa ngục và trái đất. Con người chiến đấu bằng khế ước, trả giá bằng cơ thể hoặc tuổi thọ.

[pause] Và con quỷ cưa máy đặc biệt vì khi ăn quỷ, nó xóa cả khái niệm đó khỏi thế giới.

[pause] Câu hỏi cho bạn: nỗi sợ nào của bạn, nếu thành quỷ, sẽ mạnh nhất? Viết xuống phần bình luận nhé, nhưng đừng sợ quá kẻo nó mạnh lên đấy.

[pause] Nếu video hữu ích, hãy đăng ký kênh. Video sau Kaku sẽ so sánh Chakra, Nen và Chú lực: hệ thống nào chặt chẽ nhất?

[pause] Kaku gấp sổ đây, hẹn gặp lại!
```
