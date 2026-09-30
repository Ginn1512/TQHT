# Bộ prompt · Naruto: Cây phả hệ Otsutsuki, Uchiha, Senju và Uzumaki

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 90 ảnh, 8 đoạn đọc, khoảng 15.0 phút giọng.
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

Lời: Cảnh báo: video có spoiler toàn bộ Naruto Shippuden, phim The Last, và nhắc nhẹ phần mở đầu của Boruto.

```text
Wide 16:9 landscape cinematic frame. a colossal ancient tree silhouetted against a full moon, roots spreading across a vast land. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hai cậu bé cùng lớp, một người bị cả làng xa lánh, một người là thiên tài của gia tộc danh giá. Họ là bạn, là…

```text
Wide 16:9 landscape cinematic frame. two boys standing back to back on a cliff at sunset, one with a warm smile and one with a cold stare. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nhưng nếu lần ngược lên cây phả hệ, bạn sẽ thấy câu chuyện của họ đã bắt đầu từ hàng nghìn năm trước, từ một…

```text
Wide 16:9 landscape cinematic frame. a glowing fruit hanging from a gigantic tree, a lone figure reaching up toward it. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay cuốn sổ là một tấm giấy thật lớn, và Kaku sẽ vẽ cây phả hệ của thế giới N…

```text
Wide 16:9 landscape cinematic frame. the owl mascot unrolling a huge sheet of paper and holding a brush, a tree sketch beginning. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Bốn cái tên chính hôm nay: Otsutsuki, Uchiha, Senju và Uzumaki. Và cuối video, bạn sẽ thấy gần như mọi nhân v…

```text
Wide 16:9 landscape cinematic frame. four family crests arranged around a tree trunk, connected by glowing lines. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Cách đọc cây của Kaku

Lời: Trước khi vẽ, Kaku quy ước vài ký hiệu để bạn dễ theo dõi.

```text
Wide 16:9 landscape cinematic frame. a legend box drawn in the corner of a large sheet with small symbols. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Đường liền là quan hệ huyết thống. Đường chấm là chuyển thế, khi chakra hay linh hồn của một người được cho l…

```text
Wide 16:9 landscape cinematic frame. a solid line and a dotted line drawn side by side with small labels. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Kaku còn thêm hai loại nhánh đặc biệt: nhánh ghép, khi một phần sức mạnh của gia tộc này được cấy vào người k…

```text
Wide 16:9 landscape cinematic frame. a grafted branch tied with cloth and a broken branch lying on the ground. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cây phả hệ Naruto khá rối, nên nếu bạn thấy chóng mặt, hãy tạm dừng video và nhìn lại sơ đồ nhé.

```text
Wide 16:9 landscape cinematic frame. the owl mascot spinning slightly dizzy in front of a complicated tree diagram. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · Gốc cây: Thần thụ và trái chakra

Lời: Ở tận gốc là một cái cây khổng lồ gọi là Thần thụ. Truyện kể rằng cứ nghìn năm, cây này kết một trái duy nhất…

```text
Wide 16:9 landscape cinematic frame. a gigantic otherworldly tree with roots like mountains, a single glowing fruit at its top. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Thời đó, con người chưa có chakra. Không có nhẫn thuật, không có ninja. Chiến tranh diễn ra bằng gươm giáo và…

```text
Wide 16:9 landscape cinematic frame. an ancient battlefield of ordinary soldiers with spears, a giant tree visible on the horizon. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Rồi một người phụ nữ ăn trái cây đó, và trở thành người đầu tiên có chakra trên thế giới. Từ đây, mọi thứ bắt…

```text
Wide 16:9 landscape cinematic frame. a woman's silhouette holding a glowing fruit, light spreading from her hands. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Về sau, truyện tiết lộ người phụ nữ ấy thuộc một tộc từ ngoài hành tinh, đến Trái Đất để lấy trái của Thần th…

```text
Wide 16:9 landscape cinematic frame. a starry sky with a faint path of light descending toward a single tree on Earth. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và vì chakra bắt nguồn từ một trái cây bị lấy cắp khỏi Thần thụ, nên theo một nghĩa nào đó, mọi ninja đều thừ…

```text
Wide 16:9 landscape cinematic frame. a single glowing seed passed down through many hands across generations. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: vậy nên gốc của cây phả hệ không nằm trên Trái Đất. Nó nằm ở đâu đó giữa các vì sao.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking up at the stars through a small telescope. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · Thân cây: Kaguya

Lời: Người phụ nữ đó tên là Kaguya Otsutsuki. Với sức mạnh của chakra, bà chấm dứt chiến tranh và được tôn thờ như…

```text
Wide 16:9 landscape cinematic frame. a pale ethereal goddess figure standing above kneeling crowds, war banners lowered. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Nhưng quyền lực tuyệt đối dần biến bà thành một người cai trị đáng sợ. Bà coi con người chỉ là thứ để dùng.

```text
Wide 16:9 landscape cinematic frame. a cold figure on a high throne looking down at tiny people in a vast hall. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Bà có hai người con trai, được sinh ra đã mang chakra. Họ là hai nhánh lớn đầu tiên của cây phả hệ.

```text
Wide 16:9 landscape cinematic frame. a tree trunk splitting into two large branches, each glowing with a different color. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Cuối cùng, Kaguya hợp nhất với Thần thụ, trở thành một con quái vật khổng lồ gọi là Thập vĩ. Hai người con ph…

```text
Wide 16:9 landscape cinematic frame. a colossal ten-tailed shadow rising from a giant tree, two small figures standing before it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Họ phong ấn bà vào một khối đá khổng lồ và đưa nó lên bầu trời. Theo truyện, khối đá đó chính là Mặt Trăng.

```text
Wide 16:9 landscape cinematic frame. a giant sphere of rock rising into the night sky, becoming the moon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21 · Hai nhánh lớn: Hagoromo và Hamura

Lời: Người con cả là Hagoromo, sau này được gọi là Lục đạo tiên nhân, người sáng lập ninshu, tiền thân của nhẫn th…

```text
Wide 16:9 landscape cinematic frame. an elderly sage with a staff standing on a hill, lines of light connecting people below. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Hagoromo đã chia chakra của Thập vĩ thành chín vĩ thú mà Kaku nói ở video mười hiểu lầm. Ông là người đặt tên…

```text
Wide 16:9 landscape cinematic frame. an elderly sage surrounded by nine small glowing creatures in a circle. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Người con thứ hai là Hamura. Sau trận chiến, ông cùng một phần dòng tộc chuyển lên Mặt Trăng để canh giữ ngườ…

```text
Wide 16:9 landscape cinematic frame. a calm figure standing on the surface of the moon, looking down at the Earth. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Từ đây, cây phả hệ chia làm hai nửa: nửa của Hagoromo ở lại Trái Đất, nửa của Hamura có một phần ở Mặt Trăng…

```text
Wide 16:9 landscape cinematic frame. a tree diagram with two main branches, one reaching toward a moon drawn at the top. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nhớ nhánh Hamura nhé. Nó ít được nhắc tới, nhưng sẽ gặp lại nhánh Hagoromo ở cuối cây phả hệ th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot tying a small ribbon on one branch as a reminder. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · Nhánh Hamura: Hyuga và Mặt Trăng

Lời: Những người thuộc dòng của Hamura ở lại Trái Đất trở thành tổ tiên của gia tộc Hyuga, những người sở hữu đôi…

```text
Wide 16:9 landscape cinematic frame. a traditional estate with a pale-eyed family crest, calm figures practicing martial arts in the courtyard. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Đôi mắt đó thật ra thừa hưởng từ chính Kaguya. Nên Hyuga là một trong những nhánh gần gốc nhất của cây phả hệ.

```text
Wide 16:9 landscape cinematic frame. a thin glowing line connecting a family crest back to the tree's trunk. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Phần dòng tộc lên Mặt Trăng thì sống ở đó hàng nghìn năm. Phim The Last cho thấy hậu duệ cuối cùng của họ trê…

```text
Wide 16:9 landscape cinematic frame. a lonely palace on the moon surface with empty halls and a single figure. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Trong gia tộc Hyuga còn có một luật khắc nghiệt: chia thành nhà chính và nhà phụ, người nhà phụ bị đóng một d…

```text
Wide 16:9 landscape cinematic frame. two branches of a family seated apart, one with a faint seal mark on their foreheads. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Gia tộc Hyuga còn có một phong cách chiến đấu riêng, dùng đôi mắt để nhìn thấy các điểm huyệt chakra trong cơ…

```text
Wide 16:9 landscape cinematic frame. a martial artist striking precise points on a training dummy covered in a faint network of glowing lines. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một cây phả hệ không chỉ truyền sức mạnh, mà còn truyền cả những luật lệ và nỗi đau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking sadly at a branch with a small chain around it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Hai nhánh của Hagoromo: Indra và Asura

Lời: Quay lại nhánh Hagoromo. Ông có hai người con trai, và cuộc chiến giữa họ là nguồn gốc của mọi xung đột trong…

```text
Wide 16:9 landscape cinematic frame. an elderly sage with two young sons standing on either side of him. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Người anh là Indra, thiên tài bẩm sinh, thừa hưởng đôi mắt và sức mạnh tinh thần của cha. Anh tin rằng sức mạ…

```text
Wide 16:9 landscape cinematic frame. a sharp-eyed young man mastering a technique effortlessly while others watch in awe. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Người em là Asura, không có tài năng nổi bật, nhưng thừa hưởng thể chất và nguồn sống mạnh mẽ. Anh mạnh lên n…

```text
Wide 16:9 landscape cinematic frame. a warm young man working alongside villagers, lifting logs together. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Hagoromo chọn Asura làm người kế thừa. Indra không chấp nhận, và hai anh em trở thành kẻ thù. Mối thù đó kéo…

```text
Wide 16:9 landscape cinematic frame. two brothers turning their backs on each other, a crack running across the ground between them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Từ Indra sinh ra gia tộc Uchiha. Từ Asura sinh ra gia tộc Senju, và cả gia tộc Uzumaki, họ hàng xa của Senju.

```text
Wide 16:9 landscape cinematic frame. the branch splitting again: one side labeled with one crest, the other with two more crests. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là thứ Kaku đã nhắc ở hiểu lầm số mười trong video trước. Giờ bạn thấy nó nằm ở đâu trên câ…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at the fork where two branches separate. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Nhánh Uchiha

Lời: Nhánh Uchiha nổi tiếng với đôi mắt Sharingan, và với một đặc điểm đau lòng: sức mạnh của họ mạnh lên cùng với…

```text
Wide 16:9 landscape cinematic frame. a family crest above a dark estate at night. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Những cái tên lớn nhất của nhánh này gồm Madara, người đồng sáng lập làng Lá rồi trở thành kẻ thù của nó, Ita…

```text
Wide 16:9 landscape cinematic frame. three silhouettes on branches of the same limb: a warrior, a quiet older brother and a young avenger. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku đã phân tích sự tiến hóa của Sharingan và cái giá của nó ở video số tám. Ở đây chỉ cần nhớ: nhánh này ma…

```text
Wide 16:9 landscape cinematic frame. the owl mascot tapping a small red eye diagram pinned to the branch. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nhánh Uchiha gần như bị cắt đứt sau cuộc thảm sát, chỉ còn lại rất ít người sống sót.

```text
Wide 16:9 landscape cinematic frame. a nearly bare branch with only a couple of leaves left, fallen leaves below it. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Gia tộc Uchiha cũng từng là một trong hai trụ cột sáng lập làng Lá cùng Senju. Nhưng sự nghi kỵ giữa hai bên…

```text
Wide 16:9 landscape cinematic frame. two founders shaking hands at a village gate, then a later image of a walled clan district at the edge of the village. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một gia tộc mạnh nhất lại gần như biến mất. Cây phả hệ Naruto đầy những nhánh như vậy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a single fallen leaf carefully. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44 · Nhánh Senju

Lời: Nhánh Senju nổi tiếng với thể chất mạnh mẽ và nguồn chakra dồi dào, cùng khả năng dùng nhiều loại nhẫn thuật.

```text
Wide 16:9 landscape cinematic frame. a family crest of a stylized tree above a large wooden house in a forest. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Người nổi bật nhất là Hashirama, Hokage đệ nhất và người sáng lập làng Lá, cùng với đối thủ kiêm bạn cũ Madar…

```text
Wide 16:9 landscape cinematic frame. two young men sitting by a river skipping stones, a future village drawn faintly behind them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Hashirama có năng lực mộc độn, tạo ra cả một khu rừng bằng chakra. Em trai ông, Tobirama, là Hokage đệ nhị và…

```text
Wide 16:9 landscape cinematic frame. a vast forest sprouting from the ground in seconds, a figure with arms outstretched in the center. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Cháu gái của Hashirama là Tsunade, Hokage đệ ngũ và là một trong những ninja y thuật giỏi nhất.

```text
Wide 16:9 landscape cinematic frame. a strong confident woman healing a wounded ninja with glowing green hands. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Ý tưởng lớn nhất của Hashirama là lập ra một ngôi làng nơi các gia tộc không còn giết nhau. Làng Lá chính là…

```text
Wide 16:9 landscape cinematic frame. several clan banners placed together under one large leaf-shaped symbol at a village gate. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Về sau, nhánh Senju dần hòa vào làng Lá, không còn là một gia tộc riêng biệt mạnh mẽ như trước.

```text
Wide 16:9 landscape cinematic frame. a branch blending into a larger tree labeled with a leaf-shaped symbol. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50 · Nhánh Uzumaki

Lời: Nhánh Uzumaki là họ hàng xa của Senju. Họ nổi tiếng với sinh lực mạnh mẽ, sống lâu, và đặc biệt giỏi thuật ph…

```text
Wide 16:9 landscape cinematic frame. a swirling spiral crest on a banner above a seaside village. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Họ từng có làng riêng, và có quan hệ thân thiết với làng Lá. Vợ của Hokage đệ nhất cũng là người nhà Uzumaki.

```text
Wide 16:9 landscape cinematic frame. a bridge across the sea connecting a spiral-crested village with a leaf-crested village. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Nhờ sinh lực mạnh, người Uzumaki thường được chọn làm nhân trụ lực, người mang vĩ thú trong mình. Mẹ của Naru…

```text
Wide 16:9 landscape cinematic frame. a woman with chains of light protecting a baby wrapped in cloth. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Naruto mang họ của mẹ, Uzumaki, dù cha cậu là Hokage đệ tứ. Nhờ vậy, cậu thuộc về nhánh của Asura qua dòng má…

```text
Wide 16:9 landscape cinematic frame. a family photo sketch: a smiling father, a laughing mother and a baby between them. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Thuật phong ấn của Uzumaki mạnh đến mức ngay cả vĩ thú mạnh nhất cũng có thể bị giam giữ trong một con người.…

```text
Wide 16:9 landscape cinematic frame. intricate glowing seal patterns spiraling across a scroll, a giant shadow contained within them. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nhiều người không để ý, nhưng cái tên Uzumaki mang nghĩa xoáy nước, và biểu tượng xoắn ốc xuất…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a spiral symbol on the back of a vest hanging on a hook. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Chuyển thế: những chiếc lá quay về

Lời: Giờ tới đường chấm trên cây: chuyển thế. Truyện tiết lộ chakra của Indra và Asura không mất đi, mà tái sinh q…

```text
Wide 16:9 landscape cinematic frame. dotted glowing lines looping from old branches to new leaves across generations. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Chakra của Indra tái sinh ở Madara, rồi ở Sasuke. Chakra của Asura tái sinh ở Hashirama, rồi ở Naruto.

```text
Wide 16:9 landscape cinematic frame. two dotted lines: one linking three dark silhouettes, the other linking three warm silhouettes. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Nên mỗi thế hệ, cuộc chiến giữa hai anh em lại lặp lại dưới những cái tên khác: Madara và Hashirama bên bờ sô…

```text
Wide 16:9 landscape cinematic frame. two pairs of rivals fighting at the same waterfall valley in two different eras. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Và vòng lặp đó chỉ kết thúc khi Naruto và Sasuke, sau trận chiến cuối cùng, hiểu và chấp nhận nhau.

```text
Wide 16:9 landscape cinematic frame. two exhausted young men lying side by side on broken rocks, both smiling faintly. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là chỗ cây phả hệ biến thành một câu chuyện. Không chỉ là ai sinh ra ai, mà là thù hận được…

```text
Wide 16:9 landscape cinematic frame. the owl mascot cutting a dark dotted line with small scissors. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Nhánh ghép: tế bào và đôi mắt

Lời: Một đặc điểm kỳ lạ của cây phả hệ Naruto là rất nhiều nhánh ghép: sức mạnh của gia tộc này được cấy vào người…

```text
Wide 16:9 landscape cinematic frame. a gardener grafting a branch onto a different tree, tying it with cloth. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Tế bào của Hashirama được dùng trong nhiều thí nghiệm bí mật, cấy vào những người khác để họ có được một phần…

```text
Wide 16:9 landscape cinematic frame. a dim laboratory with glass tanks and a small sprouting tree growing from a sample dish. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Đôi mắt Sharingan cũng được cấy sang người ngoài tộc Uchiha. Một ninja của làng Lá mang một con mắt như vậy t…

```text
Wide 16:9 landscape cinematic frame. a ninja with one eye hidden in deep shadow, a faint red glow within it. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Có những kẻ còn cố ghép cả sức mạnh của Senju lẫn Uchiha vào một cơ thể, để có được thứ mà Lục đạo tiên nhân…

```text
Wide 16:9 landscape cinematic frame. two different glowing branches forced together onto one trunk, cracks appearing at the joint. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: những nhánh ghép cho thấy một mặt tối của thế giới ninja: sức mạnh bị coi như tài sản, có thể c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot frowning at a jar labeled with a leaf icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Những nhánh bị mất

Lời: Cây phả hệ nào cũng có những nhánh bị gãy. Và trong Naruto, có rất nhiều.

```text
Wide 16:9 landscape cinematic frame. a large tree with several broken branches lying on the ground beneath it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Làng của gia tộc Uzumaki bị hủy diệt trong chiến tranh, vì các làng khác sợ sức mạnh phong ấn của họ. Người U…

```text
Wide 16:9 landscape cinematic frame. a ruined seaside village with a broken spiral banner fluttering in the wind. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Gia tộc Uchiha gần như bị xóa sổ trong một đêm. Và nhánh Hamura trên Mặt Trăng chỉ còn lại một người cuối cùn…

```text
Wide 16:9 landscape cinematic frame. an empty clan district at night and a lonely palace on the moon side by side. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: điều buồn nhất là phần lớn những nhánh này không mất vì thiên tai, mà vì con người sợ nhau. Đây…

```text
Wide 16:9 landscape cinematic frame. the owl mascot planting a small sapling next to a broken branch. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · Hỏi nhanh về họ hàng

Lời: Trước khi nhìn lên ngọn cây, Kaku trả lời nhanh vài câu hỏi về họ hàng mà nhiều người thắc mắc.

```text
Wide 16:9 landscape cinematic frame. a small signboard at the base of the tree with question cards pinned to it. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Hỏi: Tsunade có họ hàng với Naruto không? Đáp: có, dù khá xa. Bà nội của Tsunade là người nhà Uzumaki, vợ của…

```text
Wide 16:9 landscape cinematic frame. two silhouettes, an older woman and a young man, connected by a thin spiral-patterned thread. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Hỏi: Uchiha và Hyuga có liên quan không? Đáp: rất xa, qua Kaguya. Uchiha đi từ Hagoromo, Hyuga đi từ Hamura.…

```text
Wide 16:9 landscape cinematic frame. two eye symbols on distant branches both tracing thin lines back to the trunk. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Hỏi: Uchiha và Senju có phải kẻ thù truyền kiếp? Đáp: đúng, và nguồn gốc là hai anh em Indra và Asura. Nói cá…

```text
Wide 16:9 landscape cinematic frame. two warriors facing off, their shadows forming two brothers holding hands as children. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Hỏi: vì sao Naruto và Sasuke mạnh vượt trội so với bạn cùng lứa? Đáp: một phần vì chuyển thế và dòng máu, như…

```text
Wide 16:9 landscape cinematic frame. two young men training under a waterfall in different styles. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: làng Lá thật ra giống một đại gia đình, chỉ là mọi người không biết mình là họ hàng của nhau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing tiny lines between houses in a village sketch. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Ngọn cây: thế hệ mới

Lời: Và giờ tới phần đẹp nhất của cây phả hệ: ngọn cây, nơi các nhánh tưởng như xa nhau lại gặp lại nhau.

```text
Wide 16:9 landscape cinematic frame. the top of a tall tree where several branches intertwine and bloom with flowers. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Naruto, mang dòng máu Uzumaki thuộc nhánh Asura, kết hôn với Hinata, người nhà Hyuga thuộc nhánh Hamura. Hai…

```text
Wide 16:9 landscape cinematic frame. two branches from opposite sides of the tree curving toward each other and joining. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Con của họ mang trong mình cả hai dòng máu. Truyện Boruto cho thấy chúng thừa hưởng những đôi mắt đặc biệt từ…

```text
Wide 16:9 landscape cinematic frame. two children standing under a blooming branch, one with a faint pale glow in their eyes. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Sasuke, người cuối cùng của nhánh Uchiha, cũng lập gia đình, và con gái của anh mang trong mình Sharingan. Nh…

```text
Wide 16:9 landscape cinematic frame. a nearly bare branch sprouting a single fresh green leaf. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: cây phả hệ bắt đầu bằng một người mẹ và hai người con chống lại nhau. Nó kết thúc, ít nhất là t…

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on the top branch among blossoms, smiling. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Góc nhìn của Kaku: cây và vòng lặp thù hận · **Kaku** (đính kèm ảnh mẫu)

Lời: Nhìn toàn bộ cây phả hệ, Kaku thấy Naruto dùng dòng máu như một cách kể về lịch sử thù hận.

```text
Wide 16:9 landscape cinematic frame. the owl mascot stepping back to look at the whole tree drawing on the wall. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Từ Kaguya tới hai người con, từ Indra tới Asura, từ Madara tới Hashirama, mỗi thế hệ đều thừa hưởng không chỉ…

```text
Wide 16:9 landscape cinematic frame. a long chain of rival pairs drawn along a tree trunk, each pair facing each other. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Nhưng câu trả lời của truyện không phải là dòng máu quyết định tất cả. Naruto phá vỡ vòng lặp không phải vì c…

```text
Wide 16:9 landscape cinematic frame. a young man extending a hand across a chasm toward a rival on the other side. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Kaku nghĩ đó là thông điệp đẹp nhất: ta không chọn được cây mà mình mọc ra, nhưng ta chọn được mình sẽ trổ ra…

```text
Wide 16:9 landscape cinematic frame. a single flower blooming on a branch that grew from a scarred part of the trunk. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Cây hoàn chỉnh

Lời: Tổng kết cây phả hệ. Gốc là Thần thụ và tộc Otsutsuki từ ngoài vũ trụ. Thân là Kaguya, người đầu tiên có chak…

```text
Wide 16:9 landscape cinematic frame. the complete tree diagram with the root and trunk lighting up. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Hai nhánh lớn: Hagoromo ở lại Trái Đất, Hamura với nhánh Hyuga và nhánh trên Mặt Trăng. Từ Hagoromo tách ra I…

```text
Wide 16:9 landscape cinematic frame. the main branches lighting up with their family crests. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Đường chấm là chuyển thế từ Indra, Asura tới Madara, Hashirama, rồi Sasuke, Naruto. Và ở ngọn, các nhánh gặp…

```text
Wide 16:9 landscape cinematic frame. dotted lines glowing across the tree and blossoms appearing at the top. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · **Kaku** (đính kèm ảnh mẫu)

Lời: Câu hỏi cho bạn: nếu được sinh ra trong một gia tộc ninja, bạn muốn thuộc nhánh nào? Uchiha, Senju, Uzumaki h…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding up four small family crests like cards. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · Kết

Lời: Video tới là video số ba mươi, và Kaku sẽ làm một việc đặc biệt: đặt ba thế giới phép thuật lên cùng một bàn…

```text
Wide 16:9 landscape cinematic frame. three different magic books side by side on a table under warm light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Kaku cuộn tấm giấy phả hệ lại đây. Hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot rolling up a large sheet with a tree drawing and waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Cách đọc cây của Kaku / Gốc cây: Thần thụ và trái chakra

Khoảng 148 giây · cảnh s01–s15 · 1928 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler toàn bộ Naruto Shippuden, phim The Last, và nhắc nhẹ phần mở đầu của Boruto.

<short pause> Hai cậu bé cùng lớp, một người bị cả làng xa lánh, một người là thiên tài của gia tộc danh giá. Họ là bạn, là đối thủ, và suýt giết nhau nhiều lần.

<short pause> Nhưng nếu lần ngược lên cây phả hệ, bạn sẽ thấy câu chuyện của họ đã bắt đầu từ hàng nghìn năm trước, từ một cái cây và một trái cây bị cấm.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay cuốn sổ là một tấm giấy thật lớn, và Kaku sẽ vẽ cây phả hệ của thế giới Naruto, từ gốc tới ngọn.

<short pause> Bốn cái tên chính hôm nay: Otsutsuki, Uchiha, Senju và Uzumaki. Và cuối video, bạn sẽ thấy gần như mọi nhân vật quan trọng đều là họ hàng xa của nhau.

<short pause> Trước khi vẽ, Kaku quy ước vài ký hiệu để bạn dễ theo dõi.

<short pause> Đường liền là quan hệ huyết thống. Đường chấm là chuyển thế, khi chakra hay linh hồn của một người được cho là tái sinh ở người khác.

<short pause> Kaku còn thêm hai loại nhánh đặc biệt: nhánh ghép, khi một phần sức mạnh của gia tộc này được cấy vào người khác, và nhánh bị mất, những dòng họ gần như đã biến mất.

<short pause> Kaku ghi chú: cây phả hệ Naruto khá rối, nên nếu bạn thấy chóng mặt, hãy tạm dừng video và nhìn lại sơ đồ nhé.

<short pause> Ở tận gốc là một cái cây khổng lồ gọi là Thần thụ. Truyện kể rằng cứ nghìn năm, cây này kết một trái duy nhất, chứa nguồn năng lượng mà sau này người ta gọi là chakra.

<short pause> Thời đó, con người chưa có chakra. Không có nhẫn thuật, không có ninja. Chiến tranh diễn ra bằng gươm giáo và sức người.

<short pause> Rồi một người phụ nữ ăn trái cây đó, và trở thành người đầu tiên có chakra trên thế giới. Từ đây, mọi thứ bắt đầu.

<short pause> Về sau, truyện tiết lộ người phụ nữ ấy thuộc một tộc từ ngoài hành tinh, đến Trái Đất để lấy trái của Thần thụ. Tộc đó tên là Otsutsuki.

<short pause> Và vì chakra bắt nguồn từ một trái cây bị lấy cắp khỏi Thần thụ, nên theo một nghĩa nào đó, mọi ninja đều thừa hưởng một thứ vốn không thuộc về loài người.

<short pause> Kaku ghi chú: vậy nên gốc của cây phả hệ không nằm trên Trái Đất. Nó nằm ở đâu đó giữa các vì sao.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler toàn bộ Naruto Shippuden, phim The Last, và nhắc nhẹ phần mở đầu của Boruto.

[pause] Hai cậu bé cùng lớp, một người bị cả làng xa lánh, một người là thiên tài của gia tộc danh giá. Họ là bạn, là đối thủ, và suýt giết nhau nhiều lần.

[pause] Nhưng nếu lần ngược lên cây phả hệ, bạn sẽ thấy câu chuyện của họ đã bắt đầu từ hàng nghìn năm trước, từ một cái cây và một trái cây bị cấm.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay cuốn sổ là một tấm giấy thật lớn, và Kaku sẽ vẽ cây phả hệ của thế giới Naruto, từ gốc tới ngọn.

[pause] Bốn cái tên chính hôm nay: Otsutsuki, Uchiha, Senju và Uzumaki. Và cuối video, bạn sẽ thấy gần như mọi nhân vật quan trọng đều là họ hàng xa của nhau.

[pause] Trước khi vẽ, Kaku quy ước vài ký hiệu để bạn dễ theo dõi.

[pause] Đường liền là quan hệ huyết thống. Đường chấm là chuyển thế, khi chakra hay linh hồn của một người được cho là tái sinh ở người khác.

[pause] Kaku còn thêm hai loại nhánh đặc biệt: nhánh ghép, khi một phần sức mạnh của gia tộc này được cấy vào người khác, và nhánh bị mất, những dòng họ gần như đã biến mất.

[pause] Kaku ghi chú: cây phả hệ Naruto khá rối, nên nếu bạn thấy chóng mặt, hãy tạm dừng video và nhìn lại sơ đồ nhé.

[pause] Ở tận gốc là một cái cây khổng lồ gọi là Thần thụ. Truyện kể rằng cứ nghìn năm, cây này kết một trái duy nhất, chứa nguồn năng lượng mà sau này người ta gọi là chakra.

[pause] Thời đó, con người chưa có chakra. Không có nhẫn thuật, không có ninja. Chiến tranh diễn ra bằng gươm giáo và sức người.

[pause] Rồi một người phụ nữ ăn trái cây đó, và trở thành người đầu tiên có chakra trên thế giới. Từ đây, mọi thứ bắt đầu.

[pause] Về sau, truyện tiết lộ người phụ nữ ấy thuộc một tộc từ ngoài hành tinh, đến Trái Đất để lấy trái của Thần thụ. Tộc đó tên là Otsutsuki.

[pause] Và vì chakra bắt nguồn từ một trái cây bị lấy cắp khỏi Thần thụ, nên theo một nghĩa nào đó, mọi ninja đều thừa hưởng một thứ vốn không thuộc về loài người.

[pause] Kaku ghi chú: vậy nên gốc của cây phả hệ không nằm trên Trái Đất. Nó nằm ở đâu đó giữa các vì sao.
```

### c02 · Thân cây: Kaguya / Hai nhánh lớn: Hagoromo và Hamura

Khoảng 96 giây · cảnh s16–s25 · 1254 ký tự

**Gemini**

```text
Người phụ nữ đó tên là Kaguya Otsutsuki. Với sức mạnh của chakra, bà chấm dứt chiến tranh và được tôn thờ như một nữ thần.

<short pause> Nhưng quyền lực tuyệt đối dần biến bà thành một người cai trị đáng sợ. Bà coi con người chỉ là thứ để dùng.

<short pause> Bà có hai người con trai, được sinh ra đã mang chakra. Họ là hai nhánh lớn đầu tiên của cây phả hệ.

<short pause> Cuối cùng, Kaguya hợp nhất với Thần thụ, trở thành một con quái vật khổng lồ gọi là Thập vĩ. Hai người con phải chiến đấu với chính mẹ mình.

<short pause> Họ phong ấn bà vào một khối đá khổng lồ và đưa nó lên bầu trời. Theo truyện, khối đá đó chính là Mặt Trăng.

<short pause> Người con cả là Hagoromo, sau này được gọi là Lục đạo tiên nhân, người sáng lập ninshu, tiền thân của nhẫn thuật. Ông muốn dùng chakra để kết nối con người với nhau.

<short pause> Hagoromo đã chia chakra của Thập vĩ thành chín vĩ thú mà Kaku nói ở video mười hiểu lầm. Ông là người đặt tên cho từng con.

<short pause> Người con thứ hai là Hamura. Sau trận chiến, ông cùng một phần dòng tộc chuyển lên Mặt Trăng để canh giữ người mẹ bị phong ấn.

<short pause> Từ đây, cây phả hệ chia làm hai nửa: nửa của Hagoromo ở lại Trái Đất, nửa của Hamura có một phần ở Mặt Trăng và một phần ở lại Trái Đất.

<short pause> <laugh> Kaku ghi chú: nhớ nhánh Hamura nhé. Nó ít được nhắc tới, nhưng sẽ gặp lại nhánh Hagoromo ở cuối cây phả hệ theo một cách rất đẹp.
```

**ElevenLabs**

```text
Người phụ nữ đó tên là Kaguya Otsutsuki. Với sức mạnh của chakra, bà chấm dứt chiến tranh và được tôn thờ như một nữ thần.

[pause] Nhưng quyền lực tuyệt đối dần biến bà thành một người cai trị đáng sợ. Bà coi con người chỉ là thứ để dùng.

[pause] Bà có hai người con trai, được sinh ra đã mang chakra. Họ là hai nhánh lớn đầu tiên của cây phả hệ.

[pause] Cuối cùng, Kaguya hợp nhất với Thần thụ, trở thành một con quái vật khổng lồ gọi là Thập vĩ. Hai người con phải chiến đấu với chính mẹ mình.

[pause] Họ phong ấn bà vào một khối đá khổng lồ và đưa nó lên bầu trời. Theo truyện, khối đá đó chính là Mặt Trăng.

[pause] Người con cả là Hagoromo, sau này được gọi là Lục đạo tiên nhân, người sáng lập ninshu, tiền thân của nhẫn thuật. Ông muốn dùng chakra để kết nối con người với nhau.

[pause] Hagoromo đã chia chakra của Thập vĩ thành chín vĩ thú mà Kaku nói ở video mười hiểu lầm. Ông là người đặt tên cho từng con.

[pause] Người con thứ hai là Hamura. Sau trận chiến, ông cùng một phần dòng tộc chuyển lên Mặt Trăng để canh giữ người mẹ bị phong ấn.

[pause] Từ đây, cây phả hệ chia làm hai nửa: nửa của Hagoromo ở lại Trái Đất, nửa của Hamura có một phần ở Mặt Trăng và một phần ở lại Trái Đất.

[pause] [chuckles] Kaku ghi chú: nhớ nhánh Hamura nhé. Nó ít được nhắc tới, nhưng sẽ gặp lại nhánh Hagoromo ở cuối cây phả hệ theo một cách rất đẹp.
```

### c03 · Nhánh Hamura: Hyuga và Mặt Trăng / Hai nhánh của Hagoromo: Indra và Asura

Khoảng 122 giây · cảnh s26–s37 · 1581 ký tự

**Gemini**

```text
Những người thuộc dòng của Hamura ở lại Trái Đất trở thành tổ tiên của gia tộc Hyuga, những người sở hữu đôi mắt nhìn xuyên vật thể gọi là Byakugan.

<short pause> Đôi mắt đó thật ra thừa hưởng từ chính Kaguya. Nên Hyuga là một trong những nhánh gần gốc nhất của cây phả hệ.

<short pause> Phần dòng tộc lên Mặt Trăng thì sống ở đó hàng nghìn năm. Phim The Last cho thấy hậu duệ cuối cùng của họ trên Mặt Trăng.

<short pause> Trong gia tộc Hyuga còn có một luật khắc nghiệt: chia thành nhà chính và nhà phụ, người nhà phụ bị đóng một dấu ấn để bảo vệ nhà chính. Đó là nguồn gốc nỗi đau của một nhân vật mà Kaku đã nhắc ở video trước.

<short pause> Gia tộc Hyuga còn có một phong cách chiến đấu riêng, dùng đôi mắt để nhìn thấy các điểm huyệt chakra trong cơ thể đối thủ và đánh thẳng vào đó.

<short pause> <laugh> Kaku ghi chú: một cây phả hệ không chỉ truyền sức mạnh, mà còn truyền cả những luật lệ và nỗi đau.

<short pause> Quay lại nhánh Hagoromo. Ông có hai người con trai, và cuộc chiến giữa họ là nguồn gốc của mọi xung đột trong Naruto.

<short pause> Người anh là Indra, thiên tài bẩm sinh, thừa hưởng đôi mắt và sức mạnh tinh thần của cha. Anh tin rằng sức mạnh là thứ để đạt mục tiêu.

<short pause> Người em là Asura, không có tài năng nổi bật, nhưng thừa hưởng thể chất và nguồn sống mạnh mẽ. Anh mạnh lên nhờ nỗ lực và nhờ những người giúp đỡ mình.

<short pause> Hagoromo chọn Asura làm người kế thừa. Indra không chấp nhận, và hai anh em trở thành kẻ thù. Mối thù đó kéo dài qua hàng trăm năm.

<short pause> Từ Indra sinh ra gia tộc Uchiha. Từ Asura sinh ra gia tộc Senju, và cả gia tộc Uzumaki, họ hàng xa của Senju.

<short pause> Kaku ghi chú: đây là thứ Kaku đã nhắc ở hiểu lầm số mười trong video trước. Giờ bạn thấy nó nằm ở đâu trên cây.
```

**ElevenLabs**

```text
Những người thuộc dòng của Hamura ở lại Trái Đất trở thành tổ tiên của gia tộc Hyuga, những người sở hữu đôi mắt nhìn xuyên vật thể gọi là Byakugan.

[pause] Đôi mắt đó thật ra thừa hưởng từ chính Kaguya. Nên Hyuga là một trong những nhánh gần gốc nhất của cây phả hệ.

[pause] Phần dòng tộc lên Mặt Trăng thì sống ở đó hàng nghìn năm. Phim The Last cho thấy hậu duệ cuối cùng của họ trên Mặt Trăng.

[pause] Trong gia tộc Hyuga còn có một luật khắc nghiệt: chia thành nhà chính và nhà phụ, người nhà phụ bị đóng một dấu ấn để bảo vệ nhà chính. Đó là nguồn gốc nỗi đau của một nhân vật mà Kaku đã nhắc ở video trước.

[pause] Gia tộc Hyuga còn có một phong cách chiến đấu riêng, dùng đôi mắt để nhìn thấy các điểm huyệt chakra trong cơ thể đối thủ và đánh thẳng vào đó.

[pause] [chuckles] Kaku ghi chú: một cây phả hệ không chỉ truyền sức mạnh, mà còn truyền cả những luật lệ và nỗi đau.

[pause] Quay lại nhánh Hagoromo. Ông có hai người con trai, và cuộc chiến giữa họ là nguồn gốc của mọi xung đột trong Naruto.

[pause] Người anh là Indra, thiên tài bẩm sinh, thừa hưởng đôi mắt và sức mạnh tinh thần của cha. Anh tin rằng sức mạnh là thứ để đạt mục tiêu.

[pause] Người em là Asura, không có tài năng nổi bật, nhưng thừa hưởng thể chất và nguồn sống mạnh mẽ. Anh mạnh lên nhờ nỗ lực và nhờ những người giúp đỡ mình.

[pause] Hagoromo chọn Asura làm người kế thừa. Indra không chấp nhận, và hai anh em trở thành kẻ thù. Mối thù đó kéo dài qua hàng trăm năm.

[pause] Từ Indra sinh ra gia tộc Uchiha. Từ Asura sinh ra gia tộc Senju, và cả gia tộc Uzumaki, họ hàng xa của Senju.

[pause] Kaku ghi chú: đây là thứ Kaku đã nhắc ở hiểu lầm số mười trong video trước. Giờ bạn thấy nó nằm ở đâu trên cây.
```

### c04 · Nhánh Uchiha / Nhánh Senju

Khoảng 119 giây · cảnh s38–s49 · 1546 ký tự

**Gemini**

```text
Nhánh Uchiha nổi tiếng với đôi mắt Sharingan, và với một đặc điểm đau lòng: sức mạnh của họ mạnh lên cùng với cảm xúc, đặc biệt là nỗi đau mất mát.

<short pause> Những cái tên lớn nhất của nhánh này gồm Madara, người đồng sáng lập làng Lá rồi trở thành kẻ thù của nó, Itachi, người anh diệt tộc vì nhiệm vụ, và Sasuke, người cuối cùng còn lại.

<short pause> Kaku đã phân tích sự tiến hóa của Sharingan và cái giá của nó ở video số tám. Ở đây chỉ cần nhớ: nhánh này mang trong mình tinh thần của Indra.

<short pause> Nhánh Uchiha gần như bị cắt đứt sau cuộc thảm sát, chỉ còn lại rất ít người sống sót.

<short pause> Gia tộc Uchiha cũng từng là một trong hai trụ cột sáng lập làng Lá cùng Senju. <short pause> Nhưng sự nghi kỵ giữa hai bên kéo dài nhiều thế hệ, dẫn tới việc Uchiha dần bị đẩy ra rìa.

<short pause> <laugh> Kaku ghi chú: một gia tộc mạnh nhất lại gần như biến mất. Cây phả hệ Naruto đầy những nhánh như vậy.

<short pause> Nhánh Senju nổi tiếng với thể chất mạnh mẽ và nguồn chakra dồi dào, cùng khả năng dùng nhiều loại nhẫn thuật.

<short pause> Người nổi bật nhất là Hashirama, Hokage đệ nhất và người sáng lập làng Lá, cùng với đối thủ kiêm bạn cũ Madara.

<short pause> Hashirama có năng lực mộc độn, tạo ra cả một khu rừng bằng chakra. Em trai ông, Tobirama, là Hokage đệ nhị và người sáng tạo nhiều kỹ thuật nổi tiếng.

<short pause> Cháu gái của Hashirama là Tsunade, Hokage đệ ngũ và là một trong những ninja y thuật giỏi nhất.

<short pause> Ý tưởng lớn nhất của Hashirama là lập ra một ngôi làng nơi các gia tộc không còn giết nhau. Làng Lá chính là cách ông cố chấm dứt mối thù từ thời Indra và Asura.

<short pause> Về sau, nhánh Senju dần hòa vào làng Lá, không còn là một gia tộc riêng biệt mạnh mẽ như trước.
```

**ElevenLabs**

```text
Nhánh Uchiha nổi tiếng với đôi mắt Sharingan, và với một đặc điểm đau lòng: sức mạnh của họ mạnh lên cùng với cảm xúc, đặc biệt là nỗi đau mất mát.

[pause] Những cái tên lớn nhất của nhánh này gồm Madara, người đồng sáng lập làng Lá rồi trở thành kẻ thù của nó, Itachi, người anh diệt tộc vì nhiệm vụ, và Sasuke, người cuối cùng còn lại.

[pause] Kaku đã phân tích sự tiến hóa của Sharingan và cái giá của nó ở video số tám. Ở đây chỉ cần nhớ: nhánh này mang trong mình tinh thần của Indra.

[pause] Nhánh Uchiha gần như bị cắt đứt sau cuộc thảm sát, chỉ còn lại rất ít người sống sót.

[pause] Gia tộc Uchiha cũng từng là một trong hai trụ cột sáng lập làng Lá cùng Senju. [pause] Nhưng sự nghi kỵ giữa hai bên kéo dài nhiều thế hệ, dẫn tới việc Uchiha dần bị đẩy ra rìa.

[pause] [chuckles] Kaku ghi chú: một gia tộc mạnh nhất lại gần như biến mất. Cây phả hệ Naruto đầy những nhánh như vậy.

[pause] Nhánh Senju nổi tiếng với thể chất mạnh mẽ và nguồn chakra dồi dào, cùng khả năng dùng nhiều loại nhẫn thuật.

[pause] Người nổi bật nhất là Hashirama, Hokage đệ nhất và người sáng lập làng Lá, cùng với đối thủ kiêm bạn cũ Madara.

[pause] Hashirama có năng lực mộc độn, tạo ra cả một khu rừng bằng chakra. Em trai ông, Tobirama, là Hokage đệ nhị và người sáng tạo nhiều kỹ thuật nổi tiếng.

[pause] Cháu gái của Hashirama là Tsunade, Hokage đệ ngũ và là một trong những ninja y thuật giỏi nhất.

[pause] Ý tưởng lớn nhất của Hashirama là lập ra một ngôi làng nơi các gia tộc không còn giết nhau. Làng Lá chính là cách ông cố chấm dứt mối thù từ thời Indra và Asura.

[pause] Về sau, nhánh Senju dần hòa vào làng Lá, không còn là một gia tộc riêng biệt mạnh mẽ như trước.
```

### c05 · Nhánh Uzumaki / Chuyển thế: những chiếc lá quay về

Khoảng 108 giây · cảnh s50–s60 · 1406 ký tự

**Gemini**

```text
Nhánh Uzumaki là họ hàng xa của Senju. Họ nổi tiếng với sinh lực mạnh mẽ, sống lâu, và đặc biệt giỏi thuật phong ấn.

<short pause> Họ từng có làng riêng, và có quan hệ thân thiết với làng Lá. Vợ của Hokage đệ nhất cũng là người nhà Uzumaki.

<short pause> Nhờ sinh lực mạnh, người Uzumaki thường được chọn làm nhân trụ lực, người mang vĩ thú trong mình. Mẹ của Naruto là một trong số đó.

<short pause> Naruto mang họ của mẹ, Uzumaki, dù cha cậu là Hokage đệ tứ. Nhờ vậy, cậu thuộc về nhánh của Asura qua dòng máu Uzumaki.

<short pause> Thuật phong ấn của Uzumaki mạnh đến mức ngay cả vĩ thú mạnh nhất cũng có thể bị giam giữ trong một con người. Đó vừa là món quà, vừa là gánh nặng của gia tộc.

<short pause> <laugh> Kaku ghi chú: nhiều người không để ý, nhưng cái tên Uzumaki mang nghĩa xoáy nước, và biểu tượng xoắn ốc xuất hiện khắp nơi trong làng Lá.

<short pause> Giờ tới đường chấm trên cây: chuyển thế. Truyện tiết lộ chakra của Indra và Asura không mất đi, mà tái sinh qua nhiều thế hệ.

<short pause> Chakra của Indra tái sinh ở Madara, rồi ở Sasuke. Chakra của Asura tái sinh ở Hashirama, rồi ở Naruto.

<short pause> Nên mỗi thế hệ, cuộc chiến giữa hai anh em lại lặp lại dưới những cái tên khác: Madara và Hashirama bên bờ sông, rồi Sasuke và Naruto ở thung lũng tận cùng.

<short pause> Và vòng lặp đó chỉ kết thúc khi Naruto và Sasuke, sau trận chiến cuối cùng, hiểu và chấp nhận nhau.

<short pause> Kaku ghi chú: đây là chỗ cây phả hệ biến thành một câu chuyện. Không chỉ là ai sinh ra ai, mà là thù hận được truyền lại thế nào, và được cắt đứt thế nào.
```

**ElevenLabs**

```text
Nhánh Uzumaki là họ hàng xa của Senju. Họ nổi tiếng với sinh lực mạnh mẽ, sống lâu, và đặc biệt giỏi thuật phong ấn.

[pause] Họ từng có làng riêng, và có quan hệ thân thiết với làng Lá. Vợ của Hokage đệ nhất cũng là người nhà Uzumaki.

[pause] Nhờ sinh lực mạnh, người Uzumaki thường được chọn làm nhân trụ lực, người mang vĩ thú trong mình. Mẹ của Naruto là một trong số đó.

[pause] Naruto mang họ của mẹ, Uzumaki, dù cha cậu là Hokage đệ tứ. Nhờ vậy, cậu thuộc về nhánh của Asura qua dòng máu Uzumaki.

[pause] Thuật phong ấn của Uzumaki mạnh đến mức ngay cả vĩ thú mạnh nhất cũng có thể bị giam giữ trong một con người. Đó vừa là món quà, vừa là gánh nặng của gia tộc.

[pause] [chuckles] Kaku ghi chú: nhiều người không để ý, nhưng cái tên Uzumaki mang nghĩa xoáy nước, và biểu tượng xoắn ốc xuất hiện khắp nơi trong làng Lá.

[pause] Giờ tới đường chấm trên cây: chuyển thế. Truyện tiết lộ chakra của Indra và Asura không mất đi, mà tái sinh qua nhiều thế hệ.

[pause] Chakra của Indra tái sinh ở Madara, rồi ở Sasuke. Chakra của Asura tái sinh ở Hashirama, rồi ở Naruto.

[pause] Nên mỗi thế hệ, cuộc chiến giữa hai anh em lại lặp lại dưới những cái tên khác: Madara và Hashirama bên bờ sông, rồi Sasuke và Naruto ở thung lũng tận cùng.

[pause] Và vòng lặp đó chỉ kết thúc khi Naruto và Sasuke, sau trận chiến cuối cùng, hiểu và chấp nhận nhau.

[pause] Kaku ghi chú: đây là chỗ cây phả hệ biến thành một câu chuyện. Không chỉ là ai sinh ra ai, mà là thù hận được truyền lại thế nào, và được cắt đứt thế nào.
```

### c06 · Nhánh ghép: tế bào và đôi mắt / Những nhánh bị mất

Khoảng 88 giây · cảnh s61–s69 · 1138 ký tự

**Gemini**

```text
Một đặc điểm kỳ lạ của cây phả hệ Naruto là rất nhiều nhánh ghép: sức mạnh của gia tộc này được cấy vào người của gia tộc khác.

<short pause> Tế bào của Hashirama được dùng trong nhiều thí nghiệm bí mật, cấy vào những người khác để họ có được một phần sức mạnh của ông, kể cả khả năng mộc độn.

<short pause> Đôi mắt Sharingan cũng được cấy sang người ngoài tộc Uchiha. Một ninja của làng Lá mang một con mắt như vậy từ người bạn thân đã hy sinh.

<short pause> Có những kẻ còn cố ghép cả sức mạnh của Senju lẫn Uchiha vào một cơ thể, để có được thứ mà Lục đạo tiên nhân từng có.

<short pause> <laugh> Kaku ghi chú: những nhánh ghép cho thấy một mặt tối của thế giới ninja: sức mạnh bị coi như tài sản, có thể cắt ra và cấy vào.

<short pause> Cây phả hệ nào cũng có những nhánh bị gãy. Và trong Naruto, có rất nhiều.

<short pause> Làng của gia tộc Uzumaki bị hủy diệt trong chiến tranh, vì các làng khác sợ sức mạnh phong ấn của họ. Người Uzumaki còn sống phải tản mát khắp nơi.

<short pause> Gia tộc Uchiha gần như bị xóa sổ trong một đêm. Và nhánh Hamura trên Mặt Trăng chỉ còn lại một người cuối cùng.

<short pause> Kaku ghi chú: điều buồn nhất là phần lớn những nhánh này không mất vì thiên tai, mà vì con người sợ nhau. Đây cũng là chủ đề mà Naruto luôn quay lại.
```

**ElevenLabs**

```text
Một đặc điểm kỳ lạ của cây phả hệ Naruto là rất nhiều nhánh ghép: sức mạnh của gia tộc này được cấy vào người của gia tộc khác.

[pause] Tế bào của Hashirama được dùng trong nhiều thí nghiệm bí mật, cấy vào những người khác để họ có được một phần sức mạnh của ông, kể cả khả năng mộc độn.

[pause] Đôi mắt Sharingan cũng được cấy sang người ngoài tộc Uchiha. Một ninja của làng Lá mang một con mắt như vậy từ người bạn thân đã hy sinh.

[pause] Có những kẻ còn cố ghép cả sức mạnh của Senju lẫn Uchiha vào một cơ thể, để có được thứ mà Lục đạo tiên nhân từng có.

[pause] [chuckles] Kaku ghi chú: những nhánh ghép cho thấy một mặt tối của thế giới ninja: sức mạnh bị coi như tài sản, có thể cắt ra và cấy vào.

[pause] Cây phả hệ nào cũng có những nhánh bị gãy. Và trong Naruto, có rất nhiều.

[pause] Làng của gia tộc Uzumaki bị hủy diệt trong chiến tranh, vì các làng khác sợ sức mạnh phong ấn của họ. Người Uzumaki còn sống phải tản mát khắp nơi.

[pause] Gia tộc Uchiha gần như bị xóa sổ trong một đêm. Và nhánh Hamura trên Mặt Trăng chỉ còn lại một người cuối cùng.

[pause] Kaku ghi chú: điều buồn nhất là phần lớn những nhánh này không mất vì thiên tai, mà vì con người sợ nhau. Đây cũng là chủ đề mà Naruto luôn quay lại.
```

### c07 · Hỏi nhanh về họ hàng / Ngọn cây: thế hệ mới

Khoảng 120 giây · cảnh s70–s80 · 1558 ký tự

**Gemini**

```text
Trước khi nhìn lên ngọn cây, Kaku trả lời nhanh vài câu hỏi về họ hàng mà nhiều người thắc mắc.

<short pause> Hỏi: Tsunade có họ hàng với Naruto không? Đáp: có, dù khá xa. Bà nội của Tsunade là người nhà Uzumaki, vợ của Hokage đệ nhất. Nên Tsunade có dòng máu Uzumaki, giống mẹ của Naruto.

<short pause> Hỏi: Uchiha và Hyuga có liên quan không? Đáp: rất xa, qua Kaguya. Uchiha đi từ Hagoromo, Hyuga đi từ Hamura. Đôi mắt của cả hai đều có gốc từ bà.

<short pause> Hỏi: Uchiha và Senju có phải kẻ thù truyền kiếp? Đáp: đúng, và nguồn gốc là hai anh em Indra và Asura. Nói cách khác, hai gia tộc thù nhau nhất lại là anh em họ xa.

<short pause> Hỏi: vì sao Naruto và Sasuke mạnh vượt trội so với bạn cùng lứa? Đáp: một phần vì chuyển thế và dòng máu, nhưng phần lớn là vì những năm tháng luyện tập và những trận chiến sinh tử.

<short pause> <laugh> Kaku ghi chú: làng Lá thật ra giống một đại gia đình, chỉ là mọi người không biết mình là họ hàng của nhau.

<short pause> Và giờ tới phần đẹp nhất của cây phả hệ: ngọn cây, nơi các nhánh tưởng như xa nhau lại gặp lại nhau.

<short pause> Naruto, mang dòng máu Uzumaki thuộc nhánh Asura, kết hôn với Hinata, người nhà Hyuga thuộc nhánh Hamura. Hai nhánh đã tách nhau từ thời hai người con của Kaguya, giờ nhập lại.

<short pause> Con của họ mang trong mình cả hai dòng máu. Truyện Boruto cho thấy chúng thừa hưởng những đôi mắt đặc biệt từ phía mẹ.

<short pause> Sasuke, người cuối cùng của nhánh Uchiha, cũng lập gia đình, và con gái của anh mang trong mình Sharingan. Nhánh tưởng như đã chết lại đâm chồi.

<short pause> Kaku ghi chú: cây phả hệ bắt đầu bằng một người mẹ và hai người con chống lại nhau. Nó kết thúc, ít nhất là trong Naruto, bằng những gia đình hòa hợp.
```

**ElevenLabs**

```text
Trước khi nhìn lên ngọn cây, Kaku trả lời nhanh vài câu hỏi về họ hàng mà nhiều người thắc mắc.

[pause] [curious] Hỏi: Tsunade có họ hàng với Naruto không? Đáp: có, dù khá xa. Bà nội của Tsunade là người nhà Uzumaki, vợ của Hokage đệ nhất. Nên Tsunade có dòng máu Uzumaki, giống mẹ của Naruto.

[pause] Hỏi: Uchiha và Hyuga có liên quan không? Đáp: rất xa, qua Kaguya. Uchiha đi từ Hagoromo, Hyuga đi từ Hamura. Đôi mắt của cả hai đều có gốc từ bà.

[pause] Hỏi: Uchiha và Senju có phải kẻ thù truyền kiếp? Đáp: đúng, và nguồn gốc là hai anh em Indra và Asura. Nói cách khác, hai gia tộc thù nhau nhất lại là anh em họ xa.

[pause] Hỏi: vì sao Naruto và Sasuke mạnh vượt trội so với bạn cùng lứa? Đáp: một phần vì chuyển thế và dòng máu, nhưng phần lớn là vì những năm tháng luyện tập và những trận chiến sinh tử.

[pause] [chuckles] Kaku ghi chú: làng Lá thật ra giống một đại gia đình, chỉ là mọi người không biết mình là họ hàng của nhau.

[pause] Và giờ tới phần đẹp nhất của cây phả hệ: ngọn cây, nơi các nhánh tưởng như xa nhau lại gặp lại nhau.

[pause] Naruto, mang dòng máu Uzumaki thuộc nhánh Asura, kết hôn với Hinata, người nhà Hyuga thuộc nhánh Hamura. Hai nhánh đã tách nhau từ thời hai người con của Kaguya, giờ nhập lại.

[pause] Con của họ mang trong mình cả hai dòng máu. Truyện Boruto cho thấy chúng thừa hưởng những đôi mắt đặc biệt từ phía mẹ.

[pause] Sasuke, người cuối cùng của nhánh Uchiha, cũng lập gia đình, và con gái của anh mang trong mình Sharingan. Nhánh tưởng như đã chết lại đâm chồi.

[pause] Kaku ghi chú: cây phả hệ bắt đầu bằng một người mẹ và hai người con chống lại nhau. Nó kết thúc, ít nhất là trong Naruto, bằng những gia đình hòa hợp.
```

### c08 · Góc nhìn của Kaku: cây và vòng lặp thù hận / Cây hoàn chỉnh / Kết

Khoảng 98 giây · cảnh s81–s90 · 1271 ký tự

**Gemini**

```text
<laugh> Nhìn toàn bộ cây phả hệ, Kaku thấy Naruto dùng dòng máu như một cách kể về lịch sử thù hận.

<short pause> Từ Kaguya tới hai người con, từ Indra tới Asura, từ Madara tới Hashirama, mỗi thế hệ đều thừa hưởng không chỉ sức mạnh mà cả mối thù.

<short pause> Nhưng câu trả lời của truyện không phải là dòng máu quyết định tất cả. Naruto phá vỡ vòng lặp không phải vì cậu mạnh nhất, mà vì cậu chọn thấu hiểu thay vì trả thù.

<short pause> Kaku nghĩ đó là thông điệp đẹp nhất: ta không chọn được cây mà mình mọc ra, nhưng ta chọn được mình sẽ trổ ra loại hoa nào.

<short pause> Tổng kết cây phả hệ. Gốc là Thần thụ và tộc Otsutsuki từ ngoài vũ trụ. Thân là Kaguya, người đầu tiên có chakra.

<short pause> Hai nhánh lớn: Hagoromo ở lại Trái Đất, Hamura với nhánh Hyuga và nhánh trên Mặt Trăng. Từ Hagoromo tách ra Indra với Uchiha, và Asura với Senju cùng Uzumaki.

<short pause> Đường chấm là chuyển thế từ Indra, Asura tới Madara, Hashirama, rồi Sasuke, Naruto. Và ở ngọn, các nhánh gặp lại nhau trong thế hệ mới.

<short pause> Câu hỏi cho bạn: nếu được sinh ra trong một gia tộc ninja, bạn muốn thuộc nhánh nào? Uchiha, Senju, Uzumaki hay Hyuga?

<short pause> Video tới là video số ba mươi, và Kaku sẽ làm một việc đặc biệt: đặt ba thế giới phép thuật lên cùng một bàn cân: Frieren, Black Clover và Witch Hat Atelier.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. Kaku cuộn tấm giấy phả hệ lại đây. Hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Nhìn toàn bộ cây phả hệ, Kaku thấy Naruto dùng dòng máu như một cách kể về lịch sử thù hận.

[pause] Từ Kaguya tới hai người con, từ Indra tới Asura, từ Madara tới Hashirama, mỗi thế hệ đều thừa hưởng không chỉ sức mạnh mà cả mối thù.

[pause] Nhưng câu trả lời của truyện không phải là dòng máu quyết định tất cả. Naruto phá vỡ vòng lặp không phải vì cậu mạnh nhất, mà vì cậu chọn thấu hiểu thay vì trả thù.

[pause] Kaku nghĩ đó là thông điệp đẹp nhất: ta không chọn được cây mà mình mọc ra, nhưng ta chọn được mình sẽ trổ ra loại hoa nào.

[pause] Tổng kết cây phả hệ. Gốc là Thần thụ và tộc Otsutsuki từ ngoài vũ trụ. Thân là Kaguya, người đầu tiên có chakra.

[pause] Hai nhánh lớn: Hagoromo ở lại Trái Đất, Hamura với nhánh Hyuga và nhánh trên Mặt Trăng. Từ Hagoromo tách ra Indra với Uchiha, và Asura với Senju cùng Uzumaki.

[pause] Đường chấm là chuyển thế từ Indra, Asura tới Madara, Hashirama, rồi Sasuke, Naruto. Và ở ngọn, các nhánh gặp lại nhau trong thế hệ mới.

[pause] [curious] Câu hỏi cho bạn: nếu được sinh ra trong một gia tộc ninja, bạn muốn thuộc nhánh nào? Uchiha, Senju, Uzumaki hay Hyuga?

[pause] Video tới là video số ba mươi, và Kaku sẽ làm một việc đặc biệt: đặt ba thế giới phép thuật lên cùng một bàn cân: Frieren, Black Clover và Witch Hat Atelier.

[pause] Đăng ký kênh để không bỏ lỡ nhé. Kaku cuộn tấm giấy phả hệ lại đây. Hẹn gặp lại!
```
