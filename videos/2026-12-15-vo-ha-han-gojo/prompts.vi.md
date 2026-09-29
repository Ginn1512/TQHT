# Bộ prompt · Jujutsu Kaisen: Vô hạ hạn nói gì về con người Gojo?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 81 ảnh, 10 đoạn đọc, khoảng 16.0 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (81 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya trong anime mùa hai, và nhắc ngắn tình trạng củ…

```text
Wide 16:9 landscape cinematic frame. a quiet dark shrine at night, a single paper lantern glowing above a closed notebook on a stone step, wide establishing shot, cool moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Một thiếu niên mười bảy tuổi nằm giữa vũng máu. Cổ họng bị cắt, trán bị đâm xuyên. Kẻ tấn công đã quay lưng b…

```text
Wide 16:9 landscape cinematic frame. a ruined temple courtyard at dusk, a fallen teenage figure seen from far away, long shadows, a lone assassin silhouette walking away, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Vài phút sau, cậu đứng dậy. Vết thương đã lành. Cậu mỉm cười, và nói một câu mà người Việt mình nghe rất quen…

```text
Wide 16:9 landscape cinematic frame. a teenage silhouette rising slowly among floating dust, a calm smile barely visible, warm golden light breaking through clouds behind him, low-angle shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Trên trời dưới đất, chỉ có ta là tôn quý. Câu nói gắn với truyền thuyết Đức Phật lúc đản sinh. Nhưng khi thiế…

```text
Wide 16:9 landscape cinematic frame. an ancient temple mural of a lotus blooming under a single beam of light, close-up, soft amber candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay mình không giải thích thêm một chiêu thức nữa. Mình muốn dùng chính sức m…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a large notebook on a desk, a glowing infinity symbol hovering above the page, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Vô hạ hạn, Lục nhãn, Vô hạn, Xanh, Đỏ, Tím và lãnh địa Vô Lượng Không Xứ. Mỗi thứ là một mảnh chân dung. Ghép…

```text
Wide 16:9 landscape cinematic frame. seven small glowing cards laid out in a circle on a dark wooden table, each with a different abstract symbol, top-down shot, amber highlights. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Vô hạ hạn trong ba phút

Lời: Trước khi đọc tính cách, ta cần hiểu luật. Thuật thức gia truyền của nhà Gojo tên là Vô hạ hạn. Nó đưa khái n…

```text
Wide 16:9 landscape cinematic frame. an old family scroll unrolling to reveal an elegant diagram of nested circles shrinking toward a center point, close-up, parchment texture. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Tác giả Akutami từng lấy ví dụ bằng một nghịch lý rất cổ: Achilles và con rùa của nhà triết học Hy Lạp Zeno.

```text
Wide 16:9 landscape cinematic frame. a stylized ancient greek vase painting of a runner chasing a small tortoise, side view, warm terracotta and amber tones. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Achilles chạy nhanh hơn con rùa rất nhiều. Nhưng muốn đuổi kịp, anh phải tới chỗ con rùa vừa đứng. Tới nơi th…

```text
Wide 16:9 landscape cinematic frame. a sequence of footprints getting closer and closer to a tortoise, each gap half the previous one, diagram style on parchment, top-down shot. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Trong đời thật, Achilles vẫn vượt qua con rùa, vì tổng của vô số khoảng cách ngày càng nhỏ vẫn là một con số…

```text
Wide 16:9 landscape cinematic frame. a glowing number line with infinitely many tiny ticks crowding toward a point that is never reached, diagram style on a dark slate, amber lines. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Vì vậy khi đòn đánh lao tới Gojo, nó chậm dần, chậm dần, rồi gần như đứng yên cách anh một khoảng rất nhỏ. Nó…

```text
Wide 16:9 landscape cinematic frame. a fist frozen a hair's breadth away from a calm figure, ripples of distorted air between them, extreme close-up, cold blue rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Hồi còn trẻ, Gojo phải tự bật Vô hạn khi cần. Sau lần thức tỉnh, anh để nó chạy gần như liên tục, và dùng Phả…

```text
Wide 16:9 landscape cinematic frame. a figure walking through a busy street while a faint shimmering outline always surrounds him, glowing threads repairing themselves inside a translucent head silhouette, medium shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nghĩa là trong phần lớn thời gian, thế giới không bao giờ thật sự chạm vào anh. Kể cả những điều nhỏ nhặt như…

```text
Wide 16:9 landscape cinematic frame. autumn leaves blowing toward a standing figure and curving around him without touching, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú luật thứ nhất: Vô hạn không phải tấm khiên. Nó là khoảng cách. Hãy nhớ chữ khoảng cách này, vì l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing the word distance on a chalkboard and underlining it twice. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Lục nhãn: đứa trẻ sinh ra đã khác

Lời: Vô hạ hạn không phải của riêng Gojo. Cả dòng họ đều có thể thừa hưởng nó. Nhưng tính toán vô hạn ở cấp độ ngu…

```text
Wide 16:9 landscape cinematic frame. a family tree of faded silhouettes, most of them dim, only one small figure at the bottom glowing brightly, parchment diagram, amber light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Thứ làm nên khác biệt là Lục nhãn, một đôi mắt đặc biệt hiếm. Nó cho phép nhìn thấy chú lực chi tiết tới mức…

```text
Wide 16:9 landscape cinematic frame. an extreme close-up of an eye reflecting a fine web of glowing threads, abstract and stylized, cool blue and amber highlights. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Người mang cả Vô hạ hạn lẫn Lục nhãn đã hàng trăm năm mới xuất hiện một lần. Trong truyện, người ta nói sự ra…

```text
Wide 16:9 landscape cinematic frame. a large balance scale in an ancient hall tipping sharply as a tiny glowing cradle is placed on one side, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Hãy tưởng tượng bạn là đứa trẻ đó. Từ khi còn chưa biết đi, đã có người muốn giết bạn chỉ vì bạn tồn tại. Đã…

```text
Wide 16:9 landscape cinematic frame. a small child silhouette standing in a vast empty hall, rows of bowing adults on one side and shadowy figures with knives on the other, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Không ai đối xử với bạn như một đứa trẻ bình thường. Bạn là vũ khí, là biểu tượng, là mục tiêu. Kaku nghĩ đây…

```text
Wide 16:9 landscape cinematic frame. a lonely child sitting on a high throne-like chair too big for him, looking out a window at other children playing far away, medium shot, warm window light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku từng đọc hết thư viện, nhưng chưa thấy cuốn nào dạy cách làm một đứa trẻ bình thường khi cả thế giới coi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot searching through tall bookshelves and finding an empty slot with a tiny label, shrugging. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Và đôi mắt nhìn thấy mọi thứ đó cũng có một cái giá nhỏ: nó quá tải thông tin. Gojo thường che mắt lại khi kh…

```text
Wide 16:9 landscape cinematic frame. a figure resting in a dim room with a cloth over his eyes, soft muted light, a teacup steaming beside him, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Vô hạn: bức tường mà không ai chạm tới

Lời: Giờ quay lại chữ khoảng cách. Khi bật Vô hạn, không gì chạm được vào Gojo: nắm đấm, lưỡi dao, mưa, bụi, cả nh…

```text
Wide 16:9 landscape cinematic frame. raindrops hovering in midair around a calm standing figure, forming a perfect invisible bubble, medium shot, cold blue night light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Anh có thể chọn cho thứ gì đi qua. Nhưng trong trạng thái mặc định, thế giới luôn cách anh một khoảng rất nhỏ…

```text
Wide 16:9 landscape cinematic frame. a hand reaching toward a shoulder but stopping just short, a faint shimmering boundary between them, extreme close-up, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Kaku thấy đây là hình ảnh đẹp và buồn nhất của nhân vật này. Người mạnh nhất cũng là người không ai chạm tới…

```text
Wide 16:9 landscape cinematic frame. a crowded city crossing where everyone walks in pairs and groups while one tall figure walks alone inside a faint bubble, wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Có một câu Gojo nói về người bạn thân Geto Suguru: hai người là mạnh nhất. Chữ hai người rất quan trọng. Suốt…

```text
Wide 16:9 landscape cinematic frame. two teenage silhouettes sitting side by side on a rooftop at sunset, sharing a bottle of soda, back view, warm golden light. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Năm đó, hai cậu học sinh nhận một nhiệm vụ: bảo vệ Amanai Riko, cô gái được chọn làm Tinh Tương Thể, người sẽ…

```text
Wide 16:9 landscape cinematic frame. two teenage bodyguard silhouettes walking on either side of a schoolgirl silhouette along a seaside road, summer light, wide shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Hai người mạnh nhất, một nhiệm vụ tưởng như dễ. Họ thậm chí còn đưa cô gái đi chơi biển ở Okinawa, để cô có v…

```text
Wide 16:9 landscape cinematic frame. a bright tropical beach, three small silhouettes playing at the water's edge, an aquarium building in the distance, wide shot, cheerful afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nhưng họ đã thất bại. Một sát thủ không có chút chú lực nào, Fushiguro Toji, đã vượt qua cả hai. Và cô gái họ…

```text
Wide 16:9 landscape cinematic frame. a vast underground hall with the roots of a colossal ancient tree, a dropped school bag on the stone floor, close-up, somber cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Sau biến cố với cô gái Amanai Riko và trận đấu với Fushiguro Toji, Gojo thức tỉnh và vượt lên. Từ đó, anh khô…

```text
Wide 16:9 landscape cinematic frame. the same rooftop, now one silhouette standing far ahead in bright light while the other sits in shadow, wide shot, split lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Và khi khoảng cách sức mạnh quá lớn, khoảng cách giữa hai con người cũng lớn theo. Geto rời đi theo con đường…

```text
Wide 16:9 landscape cinematic frame. two paths splitting at a crossroads in the rain, one figure walking away under a dark umbrella, the other standing still, wide shot, grey-blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku gấp nhẹ một góc sổ ở đây. Nếu bạn thấy thương Gojo hơn một chút, đó là đúng ý tác giả rồi đấy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot folding the corner of a notebook page with a small sigh, a tiny drawing of two stick figures on the page. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Xanh và Đỏ: hút lại và đẩy ra

Lời: Từ trạng thái trung tính Vô hạn, Gojo có hai cách dùng thuật thức theo hai hướng ngược nhau.

```text
Wide 16:9 landscape cinematic frame. a split diagram on a dark chalkboard: arrows converging inward on the left in blue, arrows bursting outward on the right in red. clean side-by-side panel composition, each part equally balanced. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Xanh là hướng hút. Dùng chú lực thông thường, anh tạo ra một điểm kéo mọi thứ xung quanh về phía nó, như một…

```text
Wide 16:9 landscape cinematic frame. a small glowing blue sphere pulling trees, rocks and debris toward it in a spiral, wide shot, deep blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Đỏ là hướng đẩy. Muốn dùng nó, anh phải đảo ngược chú lực bằng Phản chuyển thuật thức. Kết quả là một lực đẩy…

```text
Wide 16:9 landscape cinematic frame. a small crimson sphere exploding outward, a shockwave throwing debris away in all directions, dynamic low-angle shot, red and amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Trước trận đấu với Toji, Gojo chưa dùng được Đỏ một cách hoàn chỉnh. Chỉ khi bị dồn tới cửa tử, anh mới nắm đ…

```text
Wide 16:9 landscape cinematic frame. a wounded figure on the ground with a faint red glow spreading from his chest, cracks of light closing over the wounds, close-up, dramatic chiaroscuro. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Kaku đọc hai lực này như hai mặt của Gojo. Một mặt, anh kéo người khác về phía mình: nhận nuôi Megumi, gom cá…

```text
Wide 16:9 landscape cinematic frame. a young teacher silhouette with three students gathered close around him under a big tree, warm afternoon light, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Khi Itadori Yuji bị kết án tử chỉ vì nuốt ngón tay của Sukuna, Gojo là người đứng ra xin hoãn án. Anh dạy cậu…

```text
Wide 16:9 landscape cinematic frame. a teenage boy sitting on a couch watching movies while holding a stuffed toy bear with a stern face, a teacher silhouette laughing in the doorway, medium shot, cozy warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nghe thì buồn cười, nhưng đó là cách anh bảo vệ học trò khỏi chính cái hệ thống muốn loại bỏ họ.

```text
Wide 16:9 landscape cinematic frame. a teacher silhouette standing between a group of students and a row of looming shadows, back view, dramatic rim light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Mặt còn lại, anh đẩy mọi người ra xa bằng sự đùa cợt. Anh trêu chọc, anh đến trễ, anh nói những câu nghe rất…

```text
Wide 16:9 landscape cinematic frame. a playful figure juggling sweets while older officials in dark suits glare at him, comedic framing, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Kaku nghĩ sự đùa cợt ấy là một lớp vỏ. Khi bạn mạnh tới mức một câu nói nghiêm túc cũng làm người khác sợ, th…

```text
Wide 16:9 landscape cinematic frame. a smiling paper mask lying on a desk beside a serious handwritten letter, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Hút lại và đẩy ra, gần gũi và xa cách. Cả hai cùng tồn tại trong một người. Đó là mảnh chân dung thứ ba.

```text
Wide 16:9 landscape cinematic frame. a hand-drawn yin-yang style diagram made of a blue swirl and a red swirl on parchment, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Tím: khi hai mặt hợp làm một

Lời: Nếu Xanh và Đỏ là hai mặt, thì điều gì xảy ra khi Gojo cho chúng va vào nhau?

```text
Wide 16:9 landscape cinematic frame. two small spheres, one blue and one red, drifting toward each other in darkness, extreme close-up, glowing edges. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Đó là Hư thức: Tím. Hai lực trái ngược hợp lại tạo ra thứ mà truyện gọi là khối lượng ảo. Nó quét qua và xóa…

```text
Wide 16:9 landscape cinematic frame. a massive violet beam carving a clean straight trench through a forest and a hill, wide shot from above, violet and amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Lần đầu Gojo dùng Tím là ngay trong trận tái đấu với Toji. Người vừa đánh gục anh vài phút trước giờ không th…

```text
Wide 16:9 landscape cinematic frame. two silhouettes facing each other across a wrecked courtyard, one surrounded by a faint violet glow, the other gripping a long weapon, wide shot, tense dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Chiêu này là kỹ thuật bí truyền mà ngay cả trong nhà Gojo cũng chỉ vài người biết. Và Gojo dùng được nó sau k…

```text
Wide 16:9 landscape cinematic frame. an old family scroll with a single forbidden seal glowing violet in its center, close-up, candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Kaku thấy chi tiết này rất đẹp. Tím chỉ xuất hiện khi Gojo không còn chối bỏ một nửa nào của mình. Không còn…

```text
Wide 16:9 landscape cinematic frame. a calm young man standing in a field of flattened grass, light violet glow around his hands, peaceful expression hidden in shadow, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Nhưng khi hai mặt hợp làm một, nó cũng mang sức hủy diệt lớn nhất. Người trở nên trọn vẹn nhất cũng là người…

```text
Wide 16:9 landscape cinematic frame. a crater shaped like a perfect half sphere in the middle of a city at night, faint violet smoke rising, wide aerial shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải nói thêm: con số chính xác về sức công phá, hay việc Tím mạnh tới đâu so với các chiêu khác, thì fa…

```text
Wide 16:9 landscape cinematic frame. the owl mascot with a magnifying glass over a small violet crater drawn in the notebook, raising one wing to say wait. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49 · Vô Lượng Không Xứ: biết tất cả, nhưng không làm được gì

Lời: Mảnh cuối cùng là lãnh địa của Gojo: Vô Lượng Không Xứ. Bành trướng lãnh địa là khi thuật sư dựng nên một khô…

```text
Wide 16:9 landscape cinematic frame. a vast starry void unfolding around a small shrine-like platform, galaxies and light streams everywhere, wide establishing shot, cosmic violet and amber. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Bên trong lãnh địa này, nạn nhân bị dội vào vô tận thông tin. Họ nhận thức được mọi thứ, cảm nhận được mọi th…

```text
Wide 16:9 landscape cinematic frame. a figure frozen mid-step, eyes wide, surrounded by millions of floating fragments of images and symbols, close-up, overwhelming light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Ngay ở mùa một, Gojo từng kéo một chú linh cấp đặc biệt vào lãnh địa này, và để Yuji đi cùng để tận mắt thấy.…

```text
Wide 16:9 landscape cinematic frame. a volcanic-headed monster silhouette frozen inside a starry void, a teacher silhouette calmly holding a student's collar beside him, wide shot, cosmic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Ở Shibuya, Gojo mở lãnh địa chỉ trong khoảng hai phần mười giây, và hàng trăm người thường bị kẹt bên trong đ…

```text
Wide 16:9 landscape cinematic frame. a crowded subway platform frozen in a flash of cosmic light, people standing motionless, a single figure in the center, wide shot, cold white and violet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Kaku thấy lãnh địa này như một tấm gương của chính Gojo. Người sinh ra với Lục nhãn nhìn thấy mọi thứ, hiểu m…

```text
Wide 16:9 landscape cinematic frame. a figure standing before a giant mirror that reflects an endless starry void instead of his face, medium shot, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Anh thấy rõ thế giới chú thuật mục ruỗng thế nào: những lão già bảo thủ, những luật lệ hi sinh người trẻ. Như…

```text
Wide 16:9 landscape cinematic frame. an old council chamber with elders behind paper screens, their shadows long and crooked, a lone young figure standing in front of them, wide shot, dim amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Nếu anh dùng sức mạnh để lật đổ tất cả, anh sẽ thành một bạo chúa. Nếu không làm gì, mọi thứ vẫn y như cũ. Đó…

```text
Wide 16:9 landscape cinematic frame. a crossroads drawn on parchment: one path leading to a crumbling throne, the other to an unchanged gray city, top-down shot, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · Lựa chọn của người mạnh nhất

Lời: Vậy Gojo chọn con đường nào? Anh chọn con đường thứ ba, và đây là điều Kaku thích nhất ở nhân vật này: anh tr…

```text
Wide 16:9 landscape cinematic frame. a simple classroom at a mountain school, sunlight through tall windows, an empty teacher's desk with a stack of notebooks, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Trong truyện, Gojo nói ước mơ của anh là thay đổi thế giới chú thuật bằng cách nuôi dạy những thuật sư trẻ mạ…

```text
Wide 16:9 landscape cinematic frame. a teacher silhouette pointing at a chalkboard covered in diagrams while three students lean forward with interest, medium shot, bright morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Hãy đọc lại câu đó bằng những mảnh chân dung ta vừa ghép. Một người lớn lên không có ai ngang hàng. Một người…

```text
Wide 16:9 landscape cinematic frame. three puzzle pieces clicking together on a wooden desk: a lonely child, two friends on a rooftop, a teacher with students, top-down shot, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Không phải để có quân lính. Mà để không bao giờ phải là người duy nhất nữa. Mục tiêu thật của kẻ mạnh nhất có…

```text
Wide 16:9 landscape cinematic frame. a single tall silhouette on a hill at dawn, with several smaller silhouettes climbing up to stand beside him, wide shot, warm golden sunrise. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Và anh đã có những học trò như thế: Okkotsu Yuta, người mà chính Gojo nói có thể vượt qua mình, rồi Fushiguro…

```text
Wide 16:9 landscape cinematic frame. four student silhouettes standing in a row on a school ground at sunset, each with a different faint aura color, back view, warm light. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Chi tiết thú vị: Megumi chính là con trai của Toji, kẻ từng suýt giết Gojo. Gojo nhận nuôi cậu bé đó. Kaku ng…

```text
Wide 16:9 landscape cinematic frame. a young man silhouette holding the hand of a small boy walking along a quiet street, long evening shadows, wide shot, gentle amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku phải công bằng: đây là cách mình đọc nhân vật, dựa trên lời thoại và hành động trong truyện. Bạn hoàn to…

```text
Wide 16:9 landscape cinematic frame. the owl mascot adjusting its glasses beside a sticky note that reads just my reading, playful expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63 · Shibuya: khi bức tường có kẽ hở

Lời: Arc Shibuya là nơi kẻ thù hiểu Gojo nhất ra tay. Không ai thắng được anh bằng sức mạnh, nên họ nhắm vào con n…

```text
Wide 16:9 landscape cinematic frame. a busy city intersection at night on Halloween, crowds in costumes, neon lights and a sense of dread, wide establishing shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Chúng dồn hàng trăm người thường vào ga tàu điện ngầm rồi thả chú linh vào giữa. Gojo không thể tung chiêu lớ…

```text
Wide 16:9 landscape cinematic frame. a packed underground station, frightened civilians everywhere, a lone figure in the middle holding back his power, wide shot, harsh fluorescent light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Một mình anh chiến đấu với nhiều chú linh cấp đặc biệt, vừa đánh vừa tính xem mỗi người thường đang đứng ở đâ…

```text
Wide 16:9 landscape cinematic frame. a figure moving between monsters while tiny glowing dots mark every civilian around him like a map, top-down diagram style, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Kẻ đứng sau dùng thân xác của Geto Suguru, người bạn ngang hàng năm xưa. Chỉ trong một khoảnh khắc Gojo chững…

```text
Wide 16:9 landscape cinematic frame. a strange cube-shaped relic unfolding in a subway station, its surfaces covered in eyes drawn as abstract symbols, close-up, eerie green-amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Hãy nghĩ lại luật đầu tiên: Vô hạn là khoảng cách mà không gì vượt qua được. Nhưng thứ duy nhất vượt qua được…

```text
Wide 16:9 landscape cinematic frame. an old faded photograph of two teenage friends laughing, lying on a cold station floor next to a glowing boundary line, close-up, soft warm light against cold surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kaku nghĩ đây là lời nhắc cay đắng nhất của tác giả: sức mạnh bảo vệ Gojo khỏi mọi thứ, trừ chính trái tim củ…

```text
Wide 16:9 landscape cinematic frame. an invisible bubble around a figure with a single crack forming where a small heart symbol glows, extreme close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Tới mùa ba anime, Gojo vẫn bị phong ấn, và thế giới chú thuật rơi vào hỗn loạn ngay khi thiếu vắng anh. Chuyệ…

```text
Wide 16:9 landscape cinematic frame. a sealed cube resting alone on a stone altar in an empty dark hall, a city in chaos visible through a distant window, wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nhưng sự hỗn loạn đó cũng nói lên một điều: một người mạnh nhất gánh cả thế giới thì thế giới ấy rất mong man…

```text
Wide 16:9 landscape cinematic frame. a giant stone pillar holding up a whole city on a mountain, one crack running through it, wide shot, stormy sky. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Góc nhìn của Kaku: sức mạnh như một tấm gương · **Kaku** (đính kèm ảnh mẫu)

Lời: Trước khi gấp sổ, Kaku muốn đặt tất cả các mảnh lên cùng một trang.

```text
Wide 16:9 landscape cinematic frame. the owl mascot laying out seven glowing cards in a neat row across a big notebook, top-down shot. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Lục nhãn: một đứa trẻ sinh ra đã không có ai ngang hàng. Vô hạn: một khoảng cách mà không ai chạm tới được.

```text
Wide 16:9 landscape cinematic frame. two glowing cards: an eye symbol and a nested circle symbol, close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Xanh và Đỏ: kéo người khác lại gần rồi đẩy họ ra xa. Tím: khi chấp nhận trọn vẹn bản thân, anh cũng trở thành…

```text
Wide 16:9 landscape cinematic frame. three glowing cards: a blue spiral, a red burst, and a violet beam, close-up, rich colors. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Vô Lượng Không Xứ: thấy mọi thứ nhưng không thể một mình thay đổi mọi thứ. Và con đường anh chọn: dạy học, để…

```text
Wide 16:9 landscape cinematic frame. a glowing card showing a starry void, next to a final card showing a small classroom, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Và mảnh Shibuya: thứ duy nhất vượt qua được bức tường vô hạn lại là một ký ức về tình bạn.

```text
Wide 16:9 landscape cinematic frame. a glowing card showing a faded photograph of two friends, placed slightly apart from the others, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Nhiều hệ thống sức mạnh trong anime chỉ để đánh nhau cho đẹp. Còn ở đây, mỗi chiêu thức lại như một câu văn m…

```text
Wide 16:9 landscape cinematic frame. a notebook page where diagrams of techniques slowly turn into a handwritten character portrait, close-up, amber ink glowing. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Bạn thấy mảnh chân dung nào đúng nhất với Gojo? Hay bạn có một mảnh thứ tám mà Kaku bỏ sót? Viết vào phần bìn…

```text
Wide 16:9 landscape cinematic frame. an empty eighth card with a question mark placed at the end of the row, close-up, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Kết

Lời: Nếu phải tóm Gojo trong một câu, Kaku sẽ viết thế này: người mạnh nhất thế giới, và cũng là người khao khát n…

```text
Wide 16:9 landscape cinematic frame. a lone figure on a rooftop at night looking at the city, then the camera reveals several small silhouettes climbing the stairs to join him, wide shot, warm city glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Thiên thượng thiên hạ, duy ngã độc tôn. Câu nói ấy nghe thì kiêu ngạo. Nhưng khi đã hiểu cả chân dung, Kaku l…

```text
Wide 16:9 landscape cinematic frame. the lotus mural again, now with a small lonely figure standing beneath it, medium shot, soft candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Video tiếp theo, Kaku chuyển sang một kiểu sức mạnh hoàn toàn khác: không phải đánh nhau, mà là quay ngược th…

```text
Wide 16:9 landscape cinematic frame. a vintage wall clock with its hands spinning backwards over a dim alley, close-up, amber streetlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu video giúp bạn nhìn Gojo theo một cách mới, hãy đăng ký kênh để cùng Kaku mở những cuốn sổ tiếp theo. Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing its notebook with a tiny infinity symbol on the cover and waving goodbye, warm lamplight. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 79 giây · cảnh s01–s06 · 1022 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya trong anime mùa hai, và nhắc ngắn tình trạng của Gojo ở mùa ba. Không có spoiler phần manga chưa chiếu.

<short pause> Một thiếu niên mười bảy tuổi nằm giữa vũng máu. Cổ họng bị cắt, trán bị đâm xuyên. Kẻ tấn công đã quay lưng bỏ đi, chắc chắn rằng cậu đã chết.

<short pause> Vài phút sau, cậu đứng dậy. Vết thương đã lành. Cậu mỉm cười, và nói một câu mà người Việt mình nghe rất quen: Thiên thượng thiên hạ, duy ngã độc tôn.

<short pause> Trên trời dưới đất, chỉ có ta là tôn quý. Câu nói gắn với truyền thuyết Đức Phật lúc đản sinh. <short pause> Nhưng khi thiếu niên ấy nói ra, nó nghe giống một lời tự giới thiệu hơn là một lời khoe khoang.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay mình không giải thích thêm một chiêu thức nữa. Mình muốn dùng chính sức mạnh của Gojo Satoru để trả lời một câu hỏi khác: anh ấy là người như thế nào?

<short pause> Vô hạ hạn, Lục nhãn, Vô hạn, Xanh, Đỏ, Tím và lãnh địa Vô Lượng Không Xứ. Mỗi thứ là một mảnh chân dung. Ghép lại, ta sẽ thấy một con người rất khác với hình ảnh kẻ mạnh nhất luôn cười cợt.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Jujutsu Kaisen tới hết arc Shibuya trong anime mùa hai, và nhắc ngắn tình trạng của Gojo ở mùa ba. Không có spoiler phần manga chưa chiếu.

[pause] Một thiếu niên mười bảy tuổi nằm giữa vũng máu. Cổ họng bị cắt, trán bị đâm xuyên. Kẻ tấn công đã quay lưng bỏ đi, chắc chắn rằng cậu đã chết.

[pause] Vài phút sau, cậu đứng dậy. Vết thương đã lành. Cậu mỉm cười, và nói một câu mà người Việt mình nghe rất quen: Thiên thượng thiên hạ, duy ngã độc tôn.

[pause] Trên trời dưới đất, chỉ có ta là tôn quý. Câu nói gắn với truyền thuyết Đức Phật lúc đản sinh. [pause] Nhưng khi thiếu niên ấy nói ra, nó nghe giống một lời tự giới thiệu hơn là một lời khoe khoang.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay mình không giải thích thêm một chiêu thức nữa. [curious] Mình muốn dùng chính sức mạnh của Gojo Satoru để trả lời một câu hỏi khác: anh ấy là người như thế nào?

[pause] Vô hạ hạn, Lục nhãn, Vô hạn, Xanh, Đỏ, Tím và lãnh địa Vô Lượng Không Xứ. Mỗi thứ là một mảnh chân dung. Ghép lại, ta sẽ thấy một con người rất khác với hình ảnh kẻ mạnh nhất luôn cười cợt.
```

### c02 · Vô hạ hạn trong ba phút

Khoảng 100 giây · cảnh s07–s14 · 1303 ký tự

**Gemini**

```text
Trước khi đọc tính cách, ta cần hiểu luật. Thuật thức gia truyền của nhà Gojo tên là Vô hạ hạn. Nó đưa khái niệm vô hạn, thứ vốn chỉ có trong toán học, ra thế giới thật.

<short pause> Tác giả Akutami từng lấy ví dụ bằng một nghịch lý rất cổ: Achilles và con rùa của nhà triết học Hy Lạp Zeno.

<short pause> Achilles chạy nhanh hơn con rùa rất nhiều. <short pause> Nhưng muốn đuổi kịp, anh phải tới chỗ con rùa vừa đứng. Tới nơi thì con rùa đã nhích thêm một chút. Anh lại phải tới chỗ đó, và cứ thế mãi.

<short pause> Trong đời thật, Achilles vẫn vượt qua con rùa, vì tổng của vô số khoảng cách ngày càng nhỏ vẫn là một con số hữu hạn. <short pause> Nhưng thuật thức của Gojo làm điều ngược lại: nó khiến khoảng cách đó thật sự không bao giờ về không.

<short pause> Vì vậy khi đòn đánh lao tới Gojo, nó chậm dần, chậm dần, rồi gần như đứng yên cách anh một khoảng rất nhỏ. Nó không bị chặn lại. Nó chỉ không bao giờ tới nơi.

<short pause> Hồi còn trẻ, Gojo phải tự bật Vô hạn khi cần. Sau lần thức tỉnh, anh để nó chạy gần như liên tục, và dùng Phản chuyển thuật thức để hồi phục bộ não không bị quá tải.

<short pause> Nghĩa là trong phần lớn thời gian, thế giới không bao giờ thật sự chạm vào anh. Kể cả những điều nhỏ nhặt như một cái vỗ vai hay một cơn gió.

<short pause> <laugh> Kaku ghi chú luật thứ nhất: Vô hạn không phải tấm khiên. Nó là khoảng cách. Hãy nhớ chữ khoảng cách này, vì lát nữa nó sẽ quay lại theo một nghĩa buồn hơn nhiều.
```

**ElevenLabs**

```text
Trước khi đọc tính cách, ta cần hiểu luật. Thuật thức gia truyền của nhà Gojo tên là Vô hạ hạn. Nó đưa khái niệm vô hạn, thứ vốn chỉ có trong toán học, ra thế giới thật.

[pause] Tác giả Akutami từng lấy ví dụ bằng một nghịch lý rất cổ: Achilles và con rùa của nhà triết học Hy Lạp Zeno.

[pause] Achilles chạy nhanh hơn con rùa rất nhiều. [pause] Nhưng muốn đuổi kịp, anh phải tới chỗ con rùa vừa đứng. Tới nơi thì con rùa đã nhích thêm một chút. Anh lại phải tới chỗ đó, và cứ thế mãi.

[pause] Trong đời thật, Achilles vẫn vượt qua con rùa, vì tổng của vô số khoảng cách ngày càng nhỏ vẫn là một con số hữu hạn. [pause] Nhưng thuật thức của Gojo làm điều ngược lại: nó khiến khoảng cách đó thật sự không bao giờ về không.

[pause] Vì vậy khi đòn đánh lao tới Gojo, nó chậm dần, chậm dần, rồi gần như đứng yên cách anh một khoảng rất nhỏ. Nó không bị chặn lại. Nó chỉ không bao giờ tới nơi.

[pause] Hồi còn trẻ, Gojo phải tự bật Vô hạn khi cần. Sau lần thức tỉnh, anh để nó chạy gần như liên tục, và dùng Phản chuyển thuật thức để hồi phục bộ não không bị quá tải.

[pause] Nghĩa là trong phần lớn thời gian, thế giới không bao giờ thật sự chạm vào anh. Kể cả những điều nhỏ nhặt như một cái vỗ vai hay một cơn gió.

[pause] [chuckles] Kaku ghi chú luật thứ nhất: Vô hạn không phải tấm khiên. Nó là khoảng cách. Hãy nhớ chữ khoảng cách này, vì lát nữa nó sẽ quay lại theo một nghĩa buồn hơn nhiều.
```

### c03 · Lục nhãn: đứa trẻ sinh ra đã khác

Khoảng 88 giây · cảnh s15–s21 · 1150 ký tự

**Gemini**

```text
Vô hạ hạn không phải của riêng Gojo. Cả dòng họ đều có thể thừa hưởng nó. <short pause> Nhưng tính toán vô hạn ở cấp độ nguyên tử thì bộ óc người thường sẽ quá tải.

<short pause> Thứ làm nên khác biệt là Lục nhãn, một đôi mắt đặc biệt hiếm. Nó cho phép nhìn thấy chú lực chi tiết tới mức gần như không lãng phí một chút năng lượng nào.

<short pause> Người mang cả Vô hạ hạn lẫn Lục nhãn đã hàng trăm năm mới xuất hiện một lần. Trong truyện, người ta nói sự ra đời của cậu bé Gojo đã làm thay đổi cán cân của cả thế giới chú thuật.

<short pause> Hãy tưởng tượng bạn là đứa trẻ đó. Từ khi còn chưa biết đi, đã có người muốn giết bạn chỉ vì bạn tồn tại. Đã có người cúi đầu trước bạn chỉ vì bạn tồn tại.

<short pause> Không ai đối xử với bạn như một đứa trẻ bình thường. Bạn là vũ khí, là biểu tượng, là mục tiêu. Kaku nghĩ đây là mảnh chân dung đầu tiên: Gojo lớn lên mà không có ai ngang hàng.

<short pause> <laugh> Kaku từng đọc hết thư viện, nhưng chưa thấy cuốn nào dạy cách làm một đứa trẻ bình thường khi cả thế giới coi mình là cán cân. Chắc là cuốn đó chưa ai viết.

<short pause> Và đôi mắt nhìn thấy mọi thứ đó cũng có một cái giá nhỏ: nó quá tải thông tin. Gojo thường che mắt lại khi không cần dùng hết khả năng, giống như ta đeo kính râm dưới nắng gắt.
```

**ElevenLabs**

```text
Vô hạ hạn không phải của riêng Gojo. Cả dòng họ đều có thể thừa hưởng nó. [pause] Nhưng tính toán vô hạn ở cấp độ nguyên tử thì bộ óc người thường sẽ quá tải.

[pause] Thứ làm nên khác biệt là Lục nhãn, một đôi mắt đặc biệt hiếm. Nó cho phép nhìn thấy chú lực chi tiết tới mức gần như không lãng phí một chút năng lượng nào.

[pause] Người mang cả Vô hạ hạn lẫn Lục nhãn đã hàng trăm năm mới xuất hiện một lần. Trong truyện, người ta nói sự ra đời của cậu bé Gojo đã làm thay đổi cán cân của cả thế giới chú thuật.

[pause] Hãy tưởng tượng bạn là đứa trẻ đó. Từ khi còn chưa biết đi, đã có người muốn giết bạn chỉ vì bạn tồn tại. Đã có người cúi đầu trước bạn chỉ vì bạn tồn tại.

[pause] Không ai đối xử với bạn như một đứa trẻ bình thường. Bạn là vũ khí, là biểu tượng, là mục tiêu. Kaku nghĩ đây là mảnh chân dung đầu tiên: Gojo lớn lên mà không có ai ngang hàng.

[pause] [chuckles] Kaku từng đọc hết thư viện, nhưng chưa thấy cuốn nào dạy cách làm một đứa trẻ bình thường khi cả thế giới coi mình là cán cân. Chắc là cuốn đó chưa ai viết.

[pause] Và đôi mắt nhìn thấy mọi thứ đó cũng có một cái giá nhỏ: nó quá tải thông tin. Gojo thường che mắt lại khi không cần dùng hết khả năng, giống như ta đeo kính râm dưới nắng gắt.
```

### c04 · Vô hạn: bức tường mà không ai chạm tới

Khoảng 122 giây · cảnh s22–s31 · 1591 ký tự

**Gemini**

```text
Giờ quay lại chữ khoảng cách. Khi bật Vô hạn, không gì chạm được vào Gojo: nắm đấm, lưỡi dao, mưa, bụi, cả những thứ anh không để ý tới.

<short pause> Anh có thể chọn cho thứ gì đi qua. <short pause> Nhưng trong trạng thái mặc định, thế giới luôn cách anh một khoảng rất nhỏ mà không bao giờ vượt qua được.

<short pause> Kaku thấy đây là hình ảnh đẹp và buồn nhất của nhân vật này. Người mạnh nhất cũng là người không ai chạm tới được, theo cả nghĩa đen lẫn nghĩa bóng.

<short pause> Có một câu Gojo nói về người bạn thân Geto Suguru: hai người là mạnh nhất. Chữ hai người rất quan trọng. Suốt tuổi trẻ, Geto là người duy nhất đứng ngang hàng, người duy nhất đi được bên trong khoảng cách ấy.

<short pause> Năm đó, hai cậu học sinh nhận một nhiệm vụ: bảo vệ Amanai Riko, cô gái được chọn làm Tinh Tương Thể, người sẽ hợp nhất với Thiên Nguyên để giữ cho kết giới của cả nước Nhật ổn định.

<short pause> Hai người mạnh nhất, một nhiệm vụ tưởng như dễ. Họ thậm chí còn đưa cô gái đi chơi biển ở Okinawa, để cô có vài ngày sống như một thiếu nữ bình thường.

<short pause> Nhưng họ đã thất bại. Một sát thủ không có chút chú lực nào, Fushiguro Toji, đã vượt qua cả hai. Và cô gái họ bảo vệ không trở về.

<short pause> Sau biến cố với cô gái Amanai Riko và trận đấu với Fushiguro Toji, Gojo thức tỉnh và vượt lên. Từ đó, anh không còn là một trong hai người mạnh nhất nữa. Anh chỉ còn là người mạnh nhất.

<short pause> Và khi khoảng cách sức mạnh quá lớn, khoảng cách giữa hai con người cũng lớn theo. Geto rời đi theo con đường của riêng mình. Mảnh chân dung thứ hai: Gojo mất người bạn ngang hàng duy nhất đúng lúc anh mạnh nhất.

<short pause> <laugh> Kaku gấp nhẹ một góc sổ ở đây. Nếu bạn thấy thương Gojo hơn một chút, đó là đúng ý tác giả rồi đấy.
```

**ElevenLabs**

```text
Giờ quay lại chữ khoảng cách. Khi bật Vô hạn, không gì chạm được vào Gojo: nắm đấm, lưỡi dao, mưa, bụi, cả những thứ anh không để ý tới.

[pause] Anh có thể chọn cho thứ gì đi qua. [pause] Nhưng trong trạng thái mặc định, thế giới luôn cách anh một khoảng rất nhỏ mà không bao giờ vượt qua được.

[pause] Kaku thấy đây là hình ảnh đẹp và buồn nhất của nhân vật này. Người mạnh nhất cũng là người không ai chạm tới được, theo cả nghĩa đen lẫn nghĩa bóng.

[pause] Có một câu Gojo nói về người bạn thân Geto Suguru: hai người là mạnh nhất. Chữ hai người rất quan trọng. Suốt tuổi trẻ, Geto là người duy nhất đứng ngang hàng, người duy nhất đi được bên trong khoảng cách ấy.

[pause] Năm đó, hai cậu học sinh nhận một nhiệm vụ: bảo vệ Amanai Riko, cô gái được chọn làm Tinh Tương Thể, người sẽ hợp nhất với Thiên Nguyên để giữ cho kết giới của cả nước Nhật ổn định.

[pause] Hai người mạnh nhất, một nhiệm vụ tưởng như dễ. Họ thậm chí còn đưa cô gái đi chơi biển ở Okinawa, để cô có vài ngày sống như một thiếu nữ bình thường.

[pause] Nhưng họ đã thất bại. Một sát thủ không có chút chú lực nào, Fushiguro Toji, đã vượt qua cả hai. Và cô gái họ bảo vệ không trở về.

[pause] Sau biến cố với cô gái Amanai Riko và trận đấu với Fushiguro Toji, Gojo thức tỉnh và vượt lên. Từ đó, anh không còn là một trong hai người mạnh nhất nữa. Anh chỉ còn là người mạnh nhất.

[pause] Và khi khoảng cách sức mạnh quá lớn, khoảng cách giữa hai con người cũng lớn theo. Geto rời đi theo con đường của riêng mình. Mảnh chân dung thứ hai: Gojo mất người bạn ngang hàng duy nhất đúng lúc anh mạnh nhất.

[pause] [chuckles] Kaku gấp nhẹ một góc sổ ở đây. Nếu bạn thấy thương Gojo hơn một chút, đó là đúng ý tác giả rồi đấy.
```

### c05 · Xanh và Đỏ: hút lại và đẩy ra

Khoảng 111 giây · cảnh s32–s41 · 1447 ký tự

**Gemini**

```text
Từ trạng thái trung tính Vô hạn, Gojo có hai cách dùng thuật thức theo hai hướng ngược nhau.

<short pause> Xanh là hướng hút. Dùng chú lực thông thường, anh tạo ra một điểm kéo mọi thứ xung quanh về phía nó, như một hố nhỏ nuốt chửng cây cối, đá và cả kẻ thù.

<short pause> Đỏ là hướng đẩy. Muốn dùng nó, anh phải đảo ngược chú lực bằng Phản chuyển thuật thức. Kết quả là một lực đẩy cực mạnh hất tung mọi thứ ra xa.

<short pause> Trước trận đấu với Toji, Gojo chưa dùng được Đỏ một cách hoàn chỉnh. Chỉ khi bị dồn tới cửa tử, anh mới nắm được Phản chuyển thuật thức. Vừa để chữa lành, vừa để mở khóa nửa còn lại của sức mạnh.

<short pause> Kaku đọc hai lực này như hai mặt của Gojo. Một mặt, anh kéo người khác về phía mình: nhận nuôi Megumi, gom các học trò lại, bảo vệ họ như một người anh.

<short pause> Khi Itadori Yuji bị kết án tử chỉ vì nuốt ngón tay của Sukuna, Gojo là người đứng ra xin hoãn án. Anh dạy cậu kiểm soát chú lực bằng cách ôm một con gấu bông phải giữ bình tĩnh suốt cả ngày.

<short pause> Nghe thì buồn cười, nhưng đó là cách anh bảo vệ học trò khỏi chính cái hệ thống muốn loại bỏ họ.

<short pause> Mặt còn lại, anh đẩy mọi người ra xa bằng sự đùa cợt. Anh trêu chọc, anh đến trễ, anh nói những câu nghe rất vô trách nhiệm. Ít ai được thấy anh nghiêm túc thật sự.

<short pause> Kaku nghĩ sự đùa cợt ấy là một lớp vỏ. Khi bạn mạnh tới mức một câu nói nghiêm túc cũng làm người khác sợ, thì đùa là cách dễ nhất để người ta dám đứng gần bạn.

<short pause> Hút lại và đẩy ra, gần gũi và xa cách. Cả hai cùng tồn tại trong một người. Đó là mảnh chân dung thứ ba.
```

**ElevenLabs**

```text
Từ trạng thái trung tính Vô hạn, Gojo có hai cách dùng thuật thức theo hai hướng ngược nhau.

[pause] Xanh là hướng hút. Dùng chú lực thông thường, anh tạo ra một điểm kéo mọi thứ xung quanh về phía nó, như một hố nhỏ nuốt chửng cây cối, đá và cả kẻ thù.

[pause] Đỏ là hướng đẩy. Muốn dùng nó, anh phải đảo ngược chú lực bằng Phản chuyển thuật thức. Kết quả là một lực đẩy cực mạnh hất tung mọi thứ ra xa.

[pause] Trước trận đấu với Toji, Gojo chưa dùng được Đỏ một cách hoàn chỉnh. Chỉ khi bị dồn tới cửa tử, anh mới nắm được Phản chuyển thuật thức. Vừa để chữa lành, vừa để mở khóa nửa còn lại của sức mạnh.

[pause] Kaku đọc hai lực này như hai mặt của Gojo. Một mặt, anh kéo người khác về phía mình: nhận nuôi Megumi, gom các học trò lại, bảo vệ họ như một người anh.

[pause] Khi Itadori Yuji bị kết án tử chỉ vì nuốt ngón tay của Sukuna, Gojo là người đứng ra xin hoãn án. Anh dạy cậu kiểm soát chú lực bằng cách ôm một con gấu bông phải giữ bình tĩnh suốt cả ngày.

[pause] Nghe thì buồn cười, nhưng đó là cách anh bảo vệ học trò khỏi chính cái hệ thống muốn loại bỏ họ.

[pause] Mặt còn lại, anh đẩy mọi người ra xa bằng sự đùa cợt. Anh trêu chọc, anh đến trễ, anh nói những câu nghe rất vô trách nhiệm. Ít ai được thấy anh nghiêm túc thật sự.

[pause] Kaku nghĩ sự đùa cợt ấy là một lớp vỏ. Khi bạn mạnh tới mức một câu nói nghiêm túc cũng làm người khác sợ, thì đùa là cách dễ nhất để người ta dám đứng gần bạn.

[pause] Hút lại và đẩy ra, gần gũi và xa cách. Cả hai cùng tồn tại trong một người. Đó là mảnh chân dung thứ ba.
```

### c06 · Tím: khi hai mặt hợp làm một

Khoảng 77 giây · cảnh s42–s48 · 1006 ký tự

**Gemini**

```text
Nếu Xanh và Đỏ là hai mặt, thì điều gì xảy ra khi Gojo cho chúng va vào nhau?

<short pause> Đó là Hư thức: Tím. Hai lực trái ngược hợp lại tạo ra thứ mà truyện gọi là khối lượng ảo. Nó quét qua và xóa sạch những gì nằm trên đường đi.

<short pause> Lần đầu Gojo dùng Tím là ngay trong trận tái đấu với Toji. Người vừa đánh gục anh vài phút trước giờ không thể chạm được vào anh nữa.

<short pause> Chiêu này là kỹ thuật bí truyền mà ngay cả trong nhà Gojo cũng chỉ vài người biết. Và Gojo dùng được nó sau khi thức tỉnh, đúng lúc anh chấp nhận mình là ai.

<short pause> Kaku thấy chi tiết này rất đẹp. Tím chỉ xuất hiện khi Gojo không còn chối bỏ một nửa nào của mình. Không còn là cậu thiếu niên gồng mình, cũng không còn là người phải chứng minh.

<short pause> Nhưng khi hai mặt hợp làm một, nó cũng mang sức hủy diệt lớn nhất. Người trở nên trọn vẹn nhất cũng là người nguy hiểm nhất. Mảnh chân dung thứ tư.

<short pause> <laugh> Kaku phải nói thêm: con số chính xác về sức công phá, hay việc Tím mạnh tới đâu so với các chiêu khác, thì fan vẫn còn tranh luận. Mình chỉ dùng những gì truyện thể hiện rõ.
```

**ElevenLabs**

```text
[curious] Nếu Xanh và Đỏ là hai mặt, thì điều gì xảy ra khi Gojo cho chúng va vào nhau?

[pause] Đó là Hư thức: Tím. Hai lực trái ngược hợp lại tạo ra thứ mà truyện gọi là khối lượng ảo. Nó quét qua và xóa sạch những gì nằm trên đường đi.

[pause] Lần đầu Gojo dùng Tím là ngay trong trận tái đấu với Toji. Người vừa đánh gục anh vài phút trước giờ không thể chạm được vào anh nữa.

[pause] Chiêu này là kỹ thuật bí truyền mà ngay cả trong nhà Gojo cũng chỉ vài người biết. Và Gojo dùng được nó sau khi thức tỉnh, đúng lúc anh chấp nhận mình là ai.

[pause] Kaku thấy chi tiết này rất đẹp. Tím chỉ xuất hiện khi Gojo không còn chối bỏ một nửa nào của mình. Không còn là cậu thiếu niên gồng mình, cũng không còn là người phải chứng minh.

[pause] Nhưng khi hai mặt hợp làm một, nó cũng mang sức hủy diệt lớn nhất. Người trở nên trọn vẹn nhất cũng là người nguy hiểm nhất. Mảnh chân dung thứ tư.

[pause] [chuckles] Kaku phải nói thêm: con số chính xác về sức công phá, hay việc Tím mạnh tới đâu so với các chiêu khác, thì fan vẫn còn tranh luận. Mình chỉ dùng những gì truyện thể hiện rõ.
```

### c07 · Vô Lượng Không Xứ: biết tất cả, nhưng không làm được gì

Khoảng 89 giây · cảnh s49–s55 · 1159 ký tự

**Gemini**

```text
Mảnh cuối cùng là lãnh địa của Gojo: Vô Lượng Không Xứ. Bành trướng lãnh địa là khi thuật sư dựng nên một không gian riêng, nơi đòn đánh của mình chắc chắn trúng đích.

<short pause> Bên trong lãnh địa này, nạn nhân bị dội vào vô tận thông tin. Họ nhận thức được mọi thứ, cảm nhận được mọi thứ, nhưng không thể hành động gì cả.

<short pause> Ngay ở mùa một, Gojo từng kéo một chú linh cấp đặc biệt vào lãnh địa này, và để Yuji đi cùng để tận mắt thấy. Chỉ cần vài giây, kẻ thù đã đứng im như một bức tượng.

<short pause> Ở Shibuya, Gojo mở lãnh địa chỉ trong khoảng hai phần mười giây, và hàng trăm người thường bị kẹt bên trong đều sống sót. Một chi tiết cho thấy anh kiểm soát nó tốt tới mức nào.

<short pause> Kaku thấy lãnh địa này như một tấm gương của chính Gojo. Người sinh ra với Lục nhãn nhìn thấy mọi thứ, hiểu mọi thứ. <short pause> Nhưng hiểu hết thì chưa chắc đã thay đổi được gì.

<short pause> Anh thấy rõ thế giới chú thuật mục ruỗng thế nào: những lão già bảo thủ, những luật lệ hi sinh người trẻ. <short pause> Nhưng một mình anh, dù mạnh nhất, cũng không thể sửa nó bằng sức mạnh.

<short pause> Nếu anh dùng sức mạnh để lật đổ tất cả, anh sẽ thành một bạo chúa. Nếu không làm gì, mọi thứ vẫn y như cũ. Đó là cái bẫy của người mạnh nhất. Mảnh chân dung thứ năm.
```

**ElevenLabs**

```text
Mảnh cuối cùng là lãnh địa của Gojo: Vô Lượng Không Xứ. Bành trướng lãnh địa là khi thuật sư dựng nên một không gian riêng, nơi đòn đánh của mình chắc chắn trúng đích.

[pause] Bên trong lãnh địa này, nạn nhân bị dội vào vô tận thông tin. Họ nhận thức được mọi thứ, cảm nhận được mọi thứ, nhưng không thể hành động gì cả.

[pause] Ngay ở mùa một, Gojo từng kéo một chú linh cấp đặc biệt vào lãnh địa này, và để Yuji đi cùng để tận mắt thấy. Chỉ cần vài giây, kẻ thù đã đứng im như một bức tượng.

[pause] Ở Shibuya, Gojo mở lãnh địa chỉ trong khoảng hai phần mười giây, và hàng trăm người thường bị kẹt bên trong đều sống sót. Một chi tiết cho thấy anh kiểm soát nó tốt tới mức nào.

[pause] Kaku thấy lãnh địa này như một tấm gương của chính Gojo. Người sinh ra với Lục nhãn nhìn thấy mọi thứ, hiểu mọi thứ. [pause] Nhưng hiểu hết thì chưa chắc đã thay đổi được gì.

[pause] Anh thấy rõ thế giới chú thuật mục ruỗng thế nào: những lão già bảo thủ, những luật lệ hi sinh người trẻ. [pause] Nhưng một mình anh, dù mạnh nhất, cũng không thể sửa nó bằng sức mạnh.

[pause] Nếu anh dùng sức mạnh để lật đổ tất cả, anh sẽ thành một bạo chúa. Nếu không làm gì, mọi thứ vẫn y như cũ. Đó là cái bẫy của người mạnh nhất. Mảnh chân dung thứ năm.
```

### c08 · Lựa chọn của người mạnh nhất

Khoảng 85 giây · cảnh s56–s62 · 1101 ký tự

**Gemini**

```text
Vậy Gojo chọn con đường nào? Anh chọn con đường thứ ba, và đây là điều Kaku thích nhất ở nhân vật này: anh trở thành thầy giáo.

<short pause> Trong truyện, Gojo nói ước mơ của anh là thay đổi thế giới chú thuật bằng cách nuôi dạy những thuật sư trẻ mạnh mẽ, những người có thể đứng ngang hàng với anh.

<short pause> Hãy đọc lại câu đó bằng những mảnh chân dung ta vừa ghép. Một người lớn lên không có ai ngang hàng. Một người mất đi người bạn ngang hàng duy nhất. Và bây giờ anh muốn tự tay tạo ra những người ngang hàng.

<short pause> Không phải để có quân lính. Mà để không bao giờ phải là người duy nhất nữa. Mục tiêu thật của kẻ mạnh nhất có lẽ là không còn là kẻ mạnh nhất.

<short pause> Và anh đã có những học trò như thế: Okkotsu Yuta, người mà chính Gojo nói có thể vượt qua mình, rồi Fushiguro Megumi, Itadori Yuji, Kugisaki Nobara.

<short pause> Chi tiết thú vị: Megumi chính là con trai của Toji, kẻ từng suýt giết Gojo. Gojo nhận nuôi cậu bé đó. Kaku nghĩ không phải ai cũng làm được điều này.

<short pause> <laugh> Kaku phải công bằng: đây là cách mình đọc nhân vật, dựa trên lời thoại và hành động trong truyện. Bạn hoàn toàn có thể đọc khác, ví dụ Gojo chỉ đơn giản là thích làm thầy.
```

**ElevenLabs**

```text
[curious] Vậy Gojo chọn con đường nào? Anh chọn con đường thứ ba, và đây là điều Kaku thích nhất ở nhân vật này: anh trở thành thầy giáo.

[pause] Trong truyện, Gojo nói ước mơ của anh là thay đổi thế giới chú thuật bằng cách nuôi dạy những thuật sư trẻ mạnh mẽ, những người có thể đứng ngang hàng với anh.

[pause] Hãy đọc lại câu đó bằng những mảnh chân dung ta vừa ghép. Một người lớn lên không có ai ngang hàng. Một người mất đi người bạn ngang hàng duy nhất. Và bây giờ anh muốn tự tay tạo ra những người ngang hàng.

[pause] Không phải để có quân lính. Mà để không bao giờ phải là người duy nhất nữa. Mục tiêu thật của kẻ mạnh nhất có lẽ là không còn là kẻ mạnh nhất.

[pause] Và anh đã có những học trò như thế: Okkotsu Yuta, người mà chính Gojo nói có thể vượt qua mình, rồi Fushiguro Megumi, Itadori Yuji, Kugisaki Nobara.

[pause] Chi tiết thú vị: Megumi chính là con trai của Toji, kẻ từng suýt giết Gojo. Gojo nhận nuôi cậu bé đó. Kaku nghĩ không phải ai cũng làm được điều này.

[pause] [chuckles] Kaku phải công bằng: đây là cách mình đọc nhân vật, dựa trên lời thoại và hành động trong truyện. Bạn hoàn toàn có thể đọc khác, ví dụ Gojo chỉ đơn giản là thích làm thầy.
```

### c09 · Shibuya: khi bức tường có kẽ hở

Khoảng 97 giây · cảnh s63–s70 · 1263 ký tự

**Gemini**

```text
Arc Shibuya là nơi kẻ thù hiểu Gojo nhất ra tay. Không ai thắng được anh bằng sức mạnh, nên họ nhắm vào con người bên trong.

<short pause> Chúng dồn hàng trăm người thường vào ga tàu điện ngầm rồi thả chú linh vào giữa. Gojo không thể tung chiêu lớn, vì mỗi đòn mạnh đều có thể giết chết những người vô tội xung quanh.

<short pause> Một mình anh chiến đấu với nhiều chú linh cấp đặc biệt, vừa đánh vừa tính xem mỗi người thường đang đứng ở đâu. Sức mạnh lớn nhất lúc này lại trở thành gánh nặng lớn nhất.

<short pause> Kẻ đứng sau dùng thân xác của Geto Suguru, người bạn ngang hàng năm xưa. Chỉ trong một khoảnh khắc Gojo chững lại vì ký ức, chiếc hộp Ngục Môn Cương đã khóa được anh.

<short pause> Hãy nghĩ lại luật đầu tiên: Vô hạn là khoảng cách mà không gì vượt qua được. <short pause> Nhưng thứ duy nhất vượt qua được khoảng cách ấy lại là một ký ức về tình bạn.

<short pause> Kaku nghĩ đây là lời nhắc cay đắng nhất của tác giả: sức mạnh bảo vệ Gojo khỏi mọi thứ, trừ chính trái tim của anh.

<short pause> Tới mùa ba anime, Gojo vẫn bị phong ấn, và thế giới chú thuật rơi vào hỗn loạn ngay khi thiếu vắng anh. Chuyện gì xảy ra tiếp theo, mình để dành cho phần anime sau, không spoiler ở đây.

<short pause> Nhưng sự hỗn loạn đó cũng nói lên một điều: một người mạnh nhất gánh cả thế giới thì thế giới ấy rất mong manh. Và đó chính là điều Gojo muốn thay đổi bằng việc dạy học.
```

**ElevenLabs**

```text
Arc Shibuya là nơi kẻ thù hiểu Gojo nhất ra tay. Không ai thắng được anh bằng sức mạnh, nên họ nhắm vào con người bên trong.

[pause] Chúng dồn hàng trăm người thường vào ga tàu điện ngầm rồi thả chú linh vào giữa. Gojo không thể tung chiêu lớn, vì mỗi đòn mạnh đều có thể giết chết những người vô tội xung quanh.

[pause] Một mình anh chiến đấu với nhiều chú linh cấp đặc biệt, vừa đánh vừa tính xem mỗi người thường đang đứng ở đâu. Sức mạnh lớn nhất lúc này lại trở thành gánh nặng lớn nhất.

[pause] Kẻ đứng sau dùng thân xác của Geto Suguru, người bạn ngang hàng năm xưa. Chỉ trong một khoảnh khắc Gojo chững lại vì ký ức, chiếc hộp Ngục Môn Cương đã khóa được anh.

[pause] Hãy nghĩ lại luật đầu tiên: Vô hạn là khoảng cách mà không gì vượt qua được. [pause] Nhưng thứ duy nhất vượt qua được khoảng cách ấy lại là một ký ức về tình bạn.

[pause] Kaku nghĩ đây là lời nhắc cay đắng nhất của tác giả: sức mạnh bảo vệ Gojo khỏi mọi thứ, trừ chính trái tim của anh.

[pause] Tới mùa ba anime, Gojo vẫn bị phong ấn, và thế giới chú thuật rơi vào hỗn loạn ngay khi thiếu vắng anh. Chuyện gì xảy ra tiếp theo, mình để dành cho phần anime sau, không spoiler ở đây.

[pause] Nhưng sự hỗn loạn đó cũng nói lên một điều: một người mạnh nhất gánh cả thế giới thì thế giới ấy rất mong manh. Và đó chính là điều Gojo muốn thay đổi bằng việc dạy học.
```

### c10 · Góc nhìn của Kaku: sức mạnh như một tấm gương / Kết

Khoảng 112 giây · cảnh s71–s81 · 1459 ký tự

**Gemini**

```text
<laugh> Trước khi gấp sổ, Kaku muốn đặt tất cả các mảnh lên cùng một trang.

<short pause> Lục nhãn: một đứa trẻ sinh ra đã không có ai ngang hàng. Vô hạn: một khoảng cách mà không ai chạm tới được.

<short pause> Xanh và Đỏ: kéo người khác lại gần rồi đẩy họ ra xa. Tím: khi chấp nhận trọn vẹn bản thân, anh cũng trở thành người nguy hiểm nhất.

<short pause> Vô Lượng Không Xứ: thấy mọi thứ nhưng không thể một mình thay đổi mọi thứ. Và con đường anh chọn: dạy học, để có những người ngang hàng.

<short pause> Và mảnh Shibuya: thứ duy nhất vượt qua được bức tường vô hạn lại là một ký ức về tình bạn.

<short pause> Nhiều hệ thống sức mạnh trong anime chỉ để đánh nhau cho đẹp. Còn ở đây, mỗi chiêu thức lại như một câu văn mô tả con người sử dụng nó. Kaku nghĩ đó là lý do Gojo được yêu thích tới vậy.

<short pause> Bạn thấy mảnh chân dung nào đúng nhất với Gojo? Hay bạn có một mảnh thứ tám mà Kaku bỏ sót? Viết vào phần bình luận nhé, mình đọc hết.

<short pause> Nếu phải tóm Gojo trong một câu, Kaku sẽ viết thế này: người mạnh nhất thế giới, và cũng là người khao khát nhất được không phải đứng một mình.

<short pause> Thiên thượng thiên hạ, duy ngã độc tôn. Câu nói ấy nghe thì kiêu ngạo. <short pause> Nhưng khi đã hiểu cả chân dung, Kaku lại nghe thấy trong đó một nỗi cô đơn rất lớn.

<short pause> Video tiếp theo, Kaku chuyển sang một kiểu sức mạnh hoàn toàn khác: không phải đánh nhau, mà là quay ngược thời gian mười hai năm để sửa sai. Luật của nó chặt hơn bạn nghĩ đấy.

<short pause> Nếu video giúp bạn nhìn Gojo theo một cách mới, hãy đăng ký kênh để cùng Kaku mở những cuốn sổ tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
[chuckles] Trước khi gấp sổ, Kaku muốn đặt tất cả các mảnh lên cùng một trang.

[pause] Lục nhãn: một đứa trẻ sinh ra đã không có ai ngang hàng. Vô hạn: một khoảng cách mà không ai chạm tới được.

[pause] Xanh và Đỏ: kéo người khác lại gần rồi đẩy họ ra xa. Tím: khi chấp nhận trọn vẹn bản thân, anh cũng trở thành người nguy hiểm nhất.

[pause] Vô Lượng Không Xứ: thấy mọi thứ nhưng không thể một mình thay đổi mọi thứ. Và con đường anh chọn: dạy học, để có những người ngang hàng.

[pause] Và mảnh Shibuya: thứ duy nhất vượt qua được bức tường vô hạn lại là một ký ức về tình bạn.

[pause] Nhiều hệ thống sức mạnh trong anime chỉ để đánh nhau cho đẹp. Còn ở đây, mỗi chiêu thức lại như một câu văn mô tả con người sử dụng nó. Kaku nghĩ đó là lý do Gojo được yêu thích tới vậy.

[pause] [curious] Bạn thấy mảnh chân dung nào đúng nhất với Gojo? Hay bạn có một mảnh thứ tám mà Kaku bỏ sót? Viết vào phần bình luận nhé, mình đọc hết.

[pause] Nếu phải tóm Gojo trong một câu, Kaku sẽ viết thế này: người mạnh nhất thế giới, và cũng là người khao khát nhất được không phải đứng một mình.

[pause] Thiên thượng thiên hạ, duy ngã độc tôn. Câu nói ấy nghe thì kiêu ngạo. [pause] Nhưng khi đã hiểu cả chân dung, Kaku lại nghe thấy trong đó một nỗi cô đơn rất lớn.

[pause] Video tiếp theo, Kaku chuyển sang một kiểu sức mạnh hoàn toàn khác: không phải đánh nhau, mà là quay ngược thời gian mười hai năm để sửa sai. Luật của nó chặt hơn bạn nghĩ đấy.

[pause] Nếu video giúp bạn nhìn Gojo theo một cách mới, hãy đăng ký kênh để cùng Kaku mở những cuốn sổ tiếp theo. Kaku gấp sổ đây, hẹn gặp lại!
```
