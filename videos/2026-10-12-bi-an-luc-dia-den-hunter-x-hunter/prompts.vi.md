# Bộ prompt · Hunter x Hunter: Điều tra bí ẩn Lục địa Đen

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 87 ảnh, 8 đoạn đọc, khoảng 15.2 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (87 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Hunter x Hunter tới arc Chọn chủ tịch trong anime, và phần mở đầu arc Lục địa Đen…

```text
Wide 16:9 landscape cinematic frame. a torn map edge dissolving into total darkness, a compass needle spinning. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hãy mở bản đồ thế giới Hunter x Hunter ra. Những quốc gia, thành phố và khu rừng mà ta đã theo nhân vật chính…

```text
Wide 16:9 landscape cinematic frame. a detailed fantasy world map on parchment with cities, forests and mountains. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Giờ hãy lùi ra xa. Rất xa. Toàn bộ tấm bản đồ đó chỉ là một chấm nhỏ nằm giữa một cái hồ khổng lồ. Và bên ngo…

```text
Wide 16:9 landscape cinematic frame. a zoomed-out view where the entire known map is a tiny island inside a vast lake, surrounded by a dark unexplored landmass. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04 · **Kaku** (đính kèm ảnh mẫu)

Lời: Hôm nay Kaku không giải thích, mà điều tra. Kaku sẽ đặt từng manh mối có thật lên bàn, rồi mới đưa ra giả thu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot in a detective coat laying photographs and notes on a table under a lamp. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku, thám tử hôm nay. Nhắc trước: truyện chưa trả lời câu hỏi lớn này, nên cuối video…

```text
Wide 16:9 landscape cinematic frame. the owl mascot opening a case file stamped UNSOLVED. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Hồ sơ vụ án

Lời: Hunter x Hunter là manga của Togashi Yoshihiro, bắt đầu từ năm 1998. Truyện nổi tiếng với hệ thống Nen chặt c…

```text
Wide 16:9 landscape cinematic frame. a case file with a photo of a manga desk and a calendar with many crossed-out months. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Nếu bạn muốn hiểu Nen trước, Kaku đã có video số một của kênh. Video hôm nay không cần biết Nen, chỉ cần biết…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pointing at a small hexagon diagram pinned to the corner of the case board. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Arc Lục địa Đen bắt đầu ngay sau arc Chọn chủ tịch Hiệp hội Thợ săn. Đây là phần anime năm 2011 chưa làm tới.

```text
Wide 16:9 landscape cinematic frame. a timeline of story arcs with the final one shaded dark and marked with a question mark. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Câu hỏi của vụ án: Lục địa Đen là gì, trong đó có gì, và vì sao cả thế giới loài người phải cấm người đi vào?

```text
Wide 16:9 landscape cinematic frame. three question cards pinned to a corkboard connected by red string. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là vụ án khó nhất mà Kaku từng nhận, vì chính tác giả cũng chưa đóng hồ sơ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot sipping tea nervously beside a towering stack of files. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Manh mối 1: Tấm bản đồ thật

Lời: Manh mối đầu tiên là tấm bản đồ. Truyện tiết lộ rằng toàn bộ thế giới loài người biết đến nằm gọn giữa một cá…

```text
Wide 16:9 landscape cinematic frame. an evidence photo of the lake map with the tiny known world circled in red. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Lục địa Đen bao quanh cái hồ đó, lớn hơn thế giới loài người rất nhiều lần. Những gì nhân vật chính từng khám…

```text
Wide 16:9 landscape cinematic frame. a scale comparison: a tiny island versus an enormous dark continent stretching to the edges of the frame. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Con người không vẽ được bản đồ đầy đủ của Lục địa Đen. Chỉ có những ghi chép rời rạc của rất ít người từng đi…

```text
Wide 16:9 landscape cinematic frame. a blank map with only a few scattered sketches along its edges, marked with small warning symbols. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Điều này khiến ta nhìn lại mọi thứ: những con quái vật, những vùng đất nguy hiểm mà ta từng thấy trong truyện…

```text
Wide 16:9 landscape cinematic frame. a familiar-looking monster standing at the edge of a vast darkness, looking small. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Giữa thế giới loài người và Lục địa Đen còn có những vùng đệm và những con đường được canh giữ. Truyện cho th…

```text
Wide 16:9 landscape cinematic frame. a narrow guarded passage along the lake shore, fog rolling over watchtowers. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: đây là một cú lật bàn cờ. Tất cả những gì bạn tưởng là cả thế giới, hóa ra chỉ là sân sau.

```text
Wide 16:9 landscape cinematic frame. the owl mascot staring at a globe that suddenly grows much larger behind a tiny one. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · Manh mối 2: Những chuyến thám hiểm thất bại

Lời: Manh mối thứ hai: lịch sử các chuyến thám hiểm. Loài người đã từng cố gắng đến Lục địa Đen nhiều lần, và phần…

```text
Wide 16:9 landscape cinematic frame. a wall of faded expedition photographs, most of them marked with black ribbons. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Rất ít người trở về. Và những người trở về đôi khi mang theo những thứ khủng khiếp hơn cả cái chết của những…

```text
Wide 16:9 landscape cinematic frame. a lone battered ship returning to harbor, a strange dark mist trailing behind it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Truyện nhắc tới năm tai họa lớn đã từng được mang về thế giới loài người từ Lục địa Đen. Mỗi tai họa đủ sức g…

```text
Wide 16:9 landscape cinematic frame. five sealed containers in a vault, each with a different ominous glow. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Nhưng cũng có những thứ quý giá được mang về, những báu vật mà con người khao khát, như thuốc chữa bách bệnh…

```text
Wide 16:9 landscape cinematic frame. a small glowing vial and a strange shining fruit on a velvet cushion behind glass. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Đó là lý do con người vẫn muốn đi: hy vọng và tai họa luôn đi cùng nhau. Bạn không thể mang về báu vật mà khô…

```text
Wide 16:9 landscape cinematic frame. a balance scale with a glowing treasure on one side and a dark sealed box on the other. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · Manh mối 3: Hiệp ước cấm

Lời: Manh mối thứ ba: năm quốc gia lớn nhất của thế giới loài người đã ký hiệp ước cấm mọi người tự ý đến Lục địa…

```text
Wide 16:9 landscape cinematic frame. five national flags around a treaty table, a bold stamp marked FORBIDDEN on the document. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Để đi hợp pháp, cần sự cho phép của họ, và phải đi qua những con đường được kiểm soát chặt chẽ.

```text
Wide 16:9 landscape cinematic frame. a guarded gate at the edge of a vast lake, soldiers checking papers. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Hiệp ước này nói lên điều gì? Rằng những người có quyền lực nhất thế giới hiểu rất rõ mức độ nguy hiểm, có th…

```text
Wide 16:9 landscape cinematic frame. officials whispering behind closed doors, a dark map on the table between them. top-down overhead view of the map, slight perspective tilt. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Nhưng cũng có một khả năng khác: họ muốn kiểm soát báu vật. Ai nắm con đường tới Lục địa Đen thì nắm nguồn lợ…

```text
Wide 16:9 landscape cinematic frame. a greedy hand reaching toward a glowing vial through bars. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: hãy để ý manh mối này, vì cuộc thám hiểm hiện tại xảy ra chính vì có người muốn phá hiệp ước.

```text
Wide 16:9 landscape cinematic frame. the owl mascot circling the treaty in red ink. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27 · Manh mối 4: Cuốn sách của một người họ Freecss

Lời: Manh mối thứ tư là một cuốn sách. Truyện nhắc tới một cuốn ghi chép về Lục địa Đen, được viết bởi một nhà thá…

```text
Wide 16:9 landscape cinematic frame. an old leather-bound travel journal with a faded compass on its cover. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Bạn không nghe nhầm đâu: Freecss, cùng họ với nhân vật chính Gon và cha cậu là Ging. Đây là một người trong d…

```text
Wide 16:9 landscape cinematic frame. a family tree sketch with a question mark linking an old explorer to a boy and his father. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Cuốn sách được cho là chia làm nhiều phần, và chỉ một phần được biết tới rộng rãi. Những phần còn lại chưa từ…

```text
Wide 16:9 landscape cinematic frame. a book with only one chapter legible and the rest sealed with wax. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Điều này gợi ý rằng dòng họ Freecss có một mối liên hệ đặc biệt với Lục địa Đen, và có lẽ đó là lý do cha con…

```text
Wide 16:9 landscape cinematic frame. a father and son silhouette standing on a cliff, looking toward the same dark horizon. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: trong một bộ truyện mà nhân vật chính bắt đầu bằng hành trình đi tìm cha, việc tổ tiên của họ l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a magnifying glass over a family crest. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · Manh mối 5: Loài kiến chimera

Lời: Manh mối thứ năm liên quan tới arc đáng sợ nhất anime: kiến chimera. Truyện cho biết loài sinh vật này có ngu…

```text
Wide 16:9 landscape cinematic frame. a massive insect queen silhouette washed ashore on a beach, waves crashing around it. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Hãy nhớ lại arc đó. Chỉ một con kiến chúa trôi dạt vào bờ đã sinh ra một đội quân suýt hủy diệt cả một quốc g…

```text
Wide 16:9 landscape cinematic frame. a ruined kingdom under a dark sky, insect soldiers silhouetted on the horizon. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Và kẻ mạnh nhất sinh ra từ đó đã khiến người mạnh nhất thế giới loài người phải dùng tới vũ khí cuối cùng.

```text
Wide 16:9 landscape cinematic frame. a giant explosion lighting up a desert night, a mushroom-shaped cloud rising. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Giờ hãy đặt điều đó cạnh manh mối số hai: đó mới chỉ là một sinh vật đi lạc, không phải tai họa lớn nhất. Nó…

```text
Wide 16:9 landscape cinematic frame. a small insect figurine placed beside five much larger dark containers. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: nếu thứ trôi dạt ngẫu nhiên đã khủng khiếp như vậy, thì những thứ còn ở trong Lục địa Đen sẽ ra…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pulling its scarf up tightly, shivering. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37 · Manh mối 6: Nanika

Lời: Manh mối thứ sáu nằm ngay trong gia đình sát thủ nổi tiếng nhất truyện. Một người em trong nhà có một năng lự…

```text
Wide 16:9 landscape cinematic frame. a small figure with a dark blank face sitting quietly in a dim room, a glowing aura of wishes around it. dynamic low-angle shot, sense of overwhelming power. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Thực thể đó được gọi là Nanika. Nó thực hiện điều ước, nhưng đòi hỏi những yêu cầu đổi lại, và nếu không đáp…

```text
Wide 16:9 landscape cinematic frame. a set of glowing rule cards floating around a dark figure, one card crumbling into dust. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Khi truyện giới thiệu năm tai họa của Lục địa Đen, một trong số đó được mô tả với hình dạng khiến rất nhiều đ…

```text
Wide 16:9 landscape cinematic frame. a sketch in an old journal of a smoky creature with a blank dark face, next to a similar silhouette. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Giả thuyết phổ biến của fan là năng lực này thật ra là một sinh vật từ Lục địa Đen. Kaku gắn nhãn: đây là lý…

```text
Wide 16:9 landscape cinematic frame. a THEORY stamp pressed onto a file linking two silhouettes with red string. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Nếu đúng, thì Lục địa Đen đã hiện diện trong truyện từ rất lâu trước khi được gọi tên.

```text
Wide 16:9 landscape cinematic frame. a shadow of a vast dark continent falling across a family mansion on a mountain. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42 · Manh mối 7: Cái cây và người cha

Lời: Manh mối thứ bảy đến từ người cha của nhân vật chính. Trong một cuộc trò chuyện hiếm hoi giữa hai cha con, ôn…

```text
Wide 16:9 landscape cinematic frame. a father and son sitting on top of a gigantic tree at sunset, the world far below. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Ông nói ông muốn leo lên một cái cây khổng lồ nằm ở rìa thế giới, gọi là Cây Thế giới, để nhìn thấy những gì…

```text
Wide 16:9 landscape cinematic frame. an impossibly tall tree at the edge of a vast lake, its top vanishing into clouds. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Với một thợ săn đã khám phá gần như mọi thứ trong thế giới loài người, mục tiêu cuối cùng chỉ có thể nằm ở bê…

```text
Wide 16:9 landscape cinematic frame. a lone explorer's silhouette at the foot of the colossal tree, looking up. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Và ông đã tham gia cuộc thám hiểm hiện tại. Có vẻ người cha luôn chạy trước con mình một bước, và bước tiếp t…

```text
Wide 16:9 landscape cinematic frame. footprints leading from a small village toward a great ship at a harbor. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46 · Manh mối 8: Cuộc thám hiểm hiện tại

Lời: Manh mối cuối cùng là cuộc thám hiểm đang diễn ra trong truyện. Nó được khởi xướng bởi con trai của cựu chủ t…

```text
Wide 16:9 landscape cinematic frame. a tall imposing man in a dark coat standing on a dock before a massive ship. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Người này công khai tuyên bố sẽ đến Lục địa Đen, bất chấp hiệp ước. Và thay vì bị ngăn lại, một vương quốc lớ…

```text
Wide 16:9 landscape cinematic frame. a royal fleet flag being raised above an enormous ship, crowds cheering below. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Hiệp hội Thợ săn buộc phải tham gia để giám sát, và cử những thợ săn giỏi nhất lên tàu. Trên con tàu đó còn d…

```text
Wide 16:9 landscape cinematic frame. a gigantic ship at sea with countless lit windows, tension visible through silhouettes behind curtains. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Cho tới những chương mới nhất, con tàu vẫn chưa tới nơi. Nghĩa là ta vẫn chưa thật sự thấy bên trong Lục địa…

```text
Wide 16:9 landscape cinematic frame. a ship's silhouette sailing endlessly toward a dark horizon that never gets closer. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Điều thú vị là cuộc thám hiểm này quy tụ những thợ săn giỏi nhất, những kẻ có tham vọng riêng, và cả những ng…

```text
Wide 16:9 landscape cinematic frame. a cross-section of a ship with many decks, each deck showing different groups plotting in secret. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: một arc tên là Lục địa Đen, mà suốt nhiều năm nhân vật vẫn chưa đặt chân lên đó. Chỉ có Togashi…

```text
Wide 16:9 landscape cinematic frame. the owl mascot laughing helplessly while holding a calendar full of crossed-out years. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · Những lời đồn cần loại khỏi hồ sơ · **Kaku** (đính kèm ảnh mẫu)

Lời: Một thám tử giỏi không chỉ thu thập manh mối, mà còn loại bỏ những lời đồn không có căn cứ. Đây là ba lời đồn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot dropping three crumpled papers into a wastebasket marked RUMORS. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Lời đồn một: Lục địa Đen là nơi Nen được sinh ra. Truyện chưa hề nói như vậy. Nen được giới thiệu là sức mạnh…

```text
Wide 16:9 landscape cinematic frame. a crumpled note with a hexagon doodle crossed out in red. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Lời đồn hai: nhân vật chính chắc chắn sẽ lấy lại Nen ở Lục địa Đen. Đây là mong muốn của rất nhiều fan, nhưng…

```text
Wide 16:9 landscape cinematic frame. a crumpled note with a fishing rod doodle and a question mark. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Lời đồn ba: Hiệp hội Thợ săn biết mọi thứ về Lục địa Đen. Ngược lại, họ tham gia cuộc thám hiểm chủ yếu để ki…

```text
Wide 16:9 landscape cinematic frame. officials in suits looking confused at a mostly blank map on a table. top-down overhead view of the map, slight perspective tilt. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: loại bỏ lời đồn giúp ta thấy rõ hơn cái thật sự còn thiếu. Và cái còn thiếu nhiều hơn ta tưởng.

```text
Wide 16:9 landscape cinematic frame. a cleaner corkboard with fewer but clearer pinned clues. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57 · Giả thuyết A: Nguồn gốc của những sức mạnh lạ · **Kaku** (đính kèm ảnh mẫu)

Lời: Giờ đặt các manh mối cạnh nhau và đưa ra giả thuyết. Nhắc lại lần nữa: phần này là suy luận, không phải sự th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning three large cards labeled A, B and C to the corkboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Giả thuyết A: nhiều sức mạnh kỳ lạ nhất trong thế giới loài người, như kiến chimera hay năng lực thực hiện đi…

```text
Wide 16:9 landscape cinematic frame. red strings connecting an insect queen photo and a dark wish-granting silhouette to a map of the dark continent. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Bằng chứng ủng hộ: kiến chimera được xác nhận là từ Lục địa Đen. Và hình mô tả một tai họa rất giống thực thể…

```text
Wide 16:9 landscape cinematic frame. two evidence photos with green check marks beside them. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Phản biện: truyện chưa khẳng định thực thể đó đến từ Lục địa Đen. Và không phải mọi sức mạnh lạ đều cần một n…

```text
Wide 16:9 landscape cinematic frame. a red counter-argument card pinned over part of the red string. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Giả thuyết B: Dòng họ Freecss

Lời: Giả thuyết B: dòng họ Freecss có một sứ mệnh hoặc một mối liên kết đặc biệt với Lục địa Đen, được truyền qua…

```text
Wide 16:9 landscape cinematic frame. an old explorer, a father and a boy standing in a line, each holding a compass. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Bằng chứng ủng hộ: tổ tiên viết sách về Lục địa Đen, người cha muốn leo Cây Thế giới, và nhân vật chính có tà…

```text
Wide 16:9 landscape cinematic frame. three evidence items on the table: a journal, a tree sketch and a fishing rod. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Phản biện: có thể đó chỉ là tính cách thích phiêu lưu chạy trong dòng máu, không phải sứ mệnh bí ẩn nào cả. V…

```text
Wide 16:9 landscape cinematic frame. a red counter-argument card over a photo of a boy fishing peacefully by a lake. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Kaku thích giả thuyết này nhất, vì nó nối cái kết của hành trình tìm cha với một hành trình mới…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing a line from a small village to the dark continent on a map. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · Giả thuyết C: Năm tai họa là năm khao khát

Lời: Giả thuyết C, táo bạo hơn: năm tai họa không chỉ là quái vật, mà là hình ảnh của những khao khát lớn nhất của…

```text
Wide 16:9 landscape cinematic frame. five sealed containers, each with a faint human silhouette reflected in its glass. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Bằng chứng ủng hộ: mỗi tai họa đi kèm một báu vật mà con người muốn có, như sự sống lâu hay sức mạnh vô hạn.…

```text
Wide 16:9 landscape cinematic frame. a coin spinning in the air, one face bright with a treasure, the other dark with a monster. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Phản biện: đây là cách đọc mang tính biểu tượng, truyện không nói thẳng như vậy. Có thể Togashi chỉ đơn giản…

```text
Wide 16:9 landscape cinematic frame. a red counter-argument card pinned over a symbolic diagram. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: dù đúng hay sai, giả thuyết này giải thích vì sao con người cứ quay lại dù biết nguy hiểm. Vì t…

```text
Wide 16:9 landscape cinematic frame. a crowd at a harbor staring longingly at a dark horizon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69 · Nếu Kaku được lên tàu · **Kaku** (đính kèm ảnh mẫu)

Lời: Thử tưởng tượng Kaku được mời lên con tàu thám hiểm. Dựa trên các manh mối, Kaku sẽ chuẩn bị những gì?

```text
Wide 16:9 landscape cinematic frame. the owl mascot packing a tiny backpack on a dock beside an enormous ship. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Thứ nhất: một người dẫn đường. Theo những gì truyện hé lộ, đi đúng con đường và có người dẫn đường là điều ki…

```text
Wide 16:9 landscape cinematic frame. a hooded guide holding a lantern at the start of a narrow path into darkness. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Thứ hai: đồ bảo hộ chống bệnh và chất độc, vì trong năm tai họa có những thứ lây lan chứ không chỉ tấn công t…

```text
Wide 16:9 landscape cinematic frame. protective masks and sealed suits hanging in a ship's storage room. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Thứ ba: một cuốn sổ thật dày. Vì nếu trở về được, điều quý giá nhất không phải báu vật, mà là ghi chép để ngư…

```text
Wide 16:9 landscape cinematic frame. a thick blank notebook and a pen placed carefully in a waterproof box. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và thứ tư: một vé khứ hồi. Kaku nghiêm túc đấy. Trong lịch sử truyện, đi thì dễ, trở về mới là phần khó nhất.

```text
Wide 16:9 landscape cinematic frame. the owl mascot clutching a return ticket tightly with both wings. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · Bảng manh mối

Lời: Tổng hợp bảng điều tra. Chắc chắn: thế giới loài người chỉ là một phần nhỏ giữa hồ lớn, có hiệp ước cấm, có n…

```text
Wide 16:9 landscape cinematic frame. a corkboard with solid green pins on four evidence photos. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Đã xác nhận nhưng còn mờ: cuốn sách của người họ Freecss, ước mơ leo Cây Thế giới, và cuộc thám hiểm đang diễ…

```text
Wide 16:9 landscape cinematic frame. yellow pins on a journal, a giant tree sketch and a ship photo. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Lý thuyết: nguồn gốc của thực thể thực hiện điều ước, sứ mệnh của dòng họ Freecss, và ý nghĩa biểu tượng của…

```text
Wide 16:9 landscape cinematic frame. red dotted pins on three theory cards connected by string. cinematic medium-wide shot, rule-of-thirds composition. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và câu hỏi lớn nhất vẫn chưa ai trả lời được: bên trong Lục địa Đen thật sự có gì?

```text
Wide 16:9 landscape cinematic frame. a single card in the center of the board with only a large question mark on it. close-up detail shot with shallow depth of field. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Góc nhìn của Kaku: sức hút của một vùng tối · **Kaku** (đính kèm ảnh mẫu)

Lời: Vì sao một bí ẩn chưa có lời giải lại khiến người ta bàn luận suốt nhiều năm như vậy?

```text
Wide 16:9 landscape cinematic frame. the owl mascot sitting on a lighthouse, looking out at a dark sea. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Kaku nghĩ là vì Hunter x Hunter bắt đầu bằng một câu chuyện về khát khao khám phá. Nhân vật chính trở thành t…

```text
Wide 16:9 landscape cinematic frame. a small boy with a fishing rod staring at a ship leaving his island. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Lục địa Đen là phiên bản lớn nhất của khát khao đó: một nơi mà ngay cả những thợ săn giỏi nhất cũng chưa hiểu…

```text
Wide 16:9 landscape cinematic frame. a vast dark landscape with a tiny lantern moving across it. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81

Lời: Và có lẽ Togashi cố tình giữ nó trong bóng tối. Một vùng đất càng ít được nhìn thấy, trí tưởng tượng của ngườ…

```text
Wide 16:9 landscape cinematic frame. a reader's silhouette with a glowing imagination cloud full of creatures above their head. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Nó cũng làm tất cả những trận đánh trước đó có thêm ý nghĩa. Những nhân vật mạnh nhất ta từng thấy có thể chỉ…

```text
Wide 16:9 landscape cinematic frame. a mighty warrior silhouette looking small at the edge of an immense dark landscape. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Kaku thấy cách kể chuyện này rất đáng học: đôi khi điều chưa nói ra lại mạnh hơn điều đã nói.

```text
Wide 16:9 landscape cinematic frame. a closed door with light seeping through the gap underneath. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · Kết: câu hỏi mở

Lời: Tóm lại vụ án: Lục địa Đen bao quanh thế giới loài người, bị cấm đi vào, đã từng gây ra năm tai họa, là nơi s…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a case file stamped STILL OPEN. wide establishing shot with deep perspective. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · **Kaku** (đính kèm ảnh mẫu)

Lời: Và hồ sơ này vẫn chưa đóng. Câu hỏi cho bạn: bạn nghĩ bên trong Lục địa Đen có gì? Hay bạn có giả thuyết D củ…

```text
Wide 16:9 landscape cinematic frame. a blank card labeled D pinned to the corkboard next to A, B and C. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Video tới, Kaku rời phòng điều tra để phân tích từng đường kiếm trong một trận đấu kinh điển: trận chiến trên…

```text
Wide 16:9 landscape cinematic frame. a moonlit forest with fine threads glinting between trees and a sword's glint. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Đăng ký kênh để không bỏ lỡ nhé. Thám tử Kaku treo áo khoác lên đây, hẹn gặp lại!

```text
Wide 16:9 landscape cinematic frame. the owl mascot hanging a tiny detective coat on a hook and waving. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Hồ sơ vụ án

Khoảng 109 giây · cảnh s01–s10 · 1415 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Hunter x Hunter tới arc Chọn chủ tịch trong anime, và phần mở đầu arc Lục địa Đen trong manga, tức những chương chưa từng được làm anime.

<short pause> Hãy mở bản đồ thế giới Hunter x Hunter ra. Những quốc gia, thành phố và khu rừng mà ta đã theo nhân vật chính đi qua suốt bao nhiêu năm.

<short pause> Giờ hãy lùi ra xa. Rất xa. Toàn bộ tấm bản đồ đó chỉ là một chấm nhỏ nằm giữa một cái hồ khổng lồ. Và bên ngoài cái hồ là một thứ chưa ai khám phá hết: Lục địa Đen.

<short pause> <laugh> Hôm nay Kaku không giải thích, mà điều tra. Kaku sẽ đặt từng manh mối có thật lên bàn, rồi mới đưa ra giả thuyết. Và mọi giả thuyết sẽ có phần phản biện.

<short pause> Mở sổ ra nào! Mình là Kaku, thám tử hôm nay. Nhắc trước: truyện chưa trả lời câu hỏi lớn này, nên cuối video sẽ không có đáp án. Chỉ có những suy luận tốt nhất ta có thể làm.

<short pause> Hunter x Hunter là manga của Togashi Yoshihiro, bắt đầu từ năm 1998. Truyện nổi tiếng với hệ thống Nen chặt chẽ, và cũng nổi tiếng với những lần tạm dừng rất dài.

<short pause> Nếu bạn muốn hiểu Nen trước, Kaku đã có video số một của kênh. Video hôm nay không cần biết Nen, chỉ cần biết thế giới này rộng hơn ta tưởng rất nhiều.

<short pause> Arc Lục địa Đen bắt đầu ngay sau arc Chọn chủ tịch Hiệp hội Thợ săn. Đây là phần anime năm 2011 chưa làm tới.

<short pause> Câu hỏi của vụ án: Lục địa Đen là gì, trong đó có gì, và vì sao cả thế giới loài người phải cấm người đi vào?

<short pause> Kaku ghi chú: đây là vụ án khó nhất mà Kaku từng nhận, vì chính tác giả cũng chưa đóng hồ sơ.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Hunter x Hunter tới arc Chọn chủ tịch trong anime, và phần mở đầu arc Lục địa Đen trong manga, tức những chương chưa từng được làm anime.

[pause] Hãy mở bản đồ thế giới Hunter x Hunter ra. Những quốc gia, thành phố và khu rừng mà ta đã theo nhân vật chính đi qua suốt bao nhiêu năm.

[pause] Giờ hãy lùi ra xa. Rất xa. Toàn bộ tấm bản đồ đó chỉ là một chấm nhỏ nằm giữa một cái hồ khổng lồ. Và bên ngoài cái hồ là một thứ chưa ai khám phá hết: Lục địa Đen.

[pause] [chuckles] Hôm nay Kaku không giải thích, mà điều tra. Kaku sẽ đặt từng manh mối có thật lên bàn, rồi mới đưa ra giả thuyết. Và mọi giả thuyết sẽ có phần phản biện.

[pause] Mở sổ ra nào! Mình là Kaku, thám tử hôm nay. Nhắc trước: truyện chưa trả lời câu hỏi lớn này, nên cuối video sẽ không có đáp án. Chỉ có những suy luận tốt nhất ta có thể làm.

[pause] Hunter x Hunter là manga của Togashi Yoshihiro, bắt đầu từ năm 1998. Truyện nổi tiếng với hệ thống Nen chặt chẽ, và cũng nổi tiếng với những lần tạm dừng rất dài.

[pause] Nếu bạn muốn hiểu Nen trước, Kaku đã có video số một của kênh. Video hôm nay không cần biết Nen, chỉ cần biết thế giới này rộng hơn ta tưởng rất nhiều.

[pause] Arc Lục địa Đen bắt đầu ngay sau arc Chọn chủ tịch Hiệp hội Thợ săn. Đây là phần anime năm 2011 chưa làm tới.

[pause] [curious] Câu hỏi của vụ án: Lục địa Đen là gì, trong đó có gì, và vì sao cả thế giới loài người phải cấm người đi vào?

[pause] Kaku ghi chú: đây là vụ án khó nhất mà Kaku từng nhận, vì chính tác giả cũng chưa đóng hồ sơ.
```

### c02 · Manh mối 1: Tấm bản đồ thật / Manh mối 2: Những chuyến thám hiểm thất bại

Khoảng 115 giây · cảnh s11–s21 · 1495 ký tự

**Gemini**

```text
Manh mối đầu tiên là tấm bản đồ. Truyện tiết lộ rằng toàn bộ thế giới loài người biết đến nằm gọn giữa một cái hồ cực lớn.

<short pause> Lục địa Đen bao quanh cái hồ đó, lớn hơn thế giới loài người rất nhiều lần. Những gì nhân vật chính từng khám phá chỉ là một phần rất nhỏ.

<short pause> Con người không vẽ được bản đồ đầy đủ của Lục địa Đen. Chỉ có những ghi chép rời rạc của rất ít người từng đi rồi trở về.

<short pause> Điều này khiến ta nhìn lại mọi thứ: những con quái vật, những vùng đất nguy hiểm mà ta từng thấy trong truyện có thể chỉ là phần rìa ngoài của một thế giới lớn hơn nhiều.

<short pause> Giữa thế giới loài người và Lục địa Đen còn có những vùng đệm và những con đường được canh giữ. Truyện cho thấy việc đi qua đó thôi cũng đã là một thử thách lớn.

<short pause> <laugh> Kaku ghi chú: đây là một cú lật bàn cờ. Tất cả những gì bạn tưởng là cả thế giới, hóa ra chỉ là sân sau.

<short pause> Manh mối thứ hai: lịch sử các chuyến thám hiểm. Loài người đã từng cố gắng đến Lục địa Đen nhiều lần, và phần lớn đều kết thúc bằng thảm họa.

<short pause> Rất ít người trở về. Và những người trở về đôi khi mang theo những thứ khủng khiếp hơn cả cái chết của những người ở lại.

<short pause> Truyện nhắc tới năm tai họa lớn đã từng được mang về thế giới loài người từ Lục địa Đen. Mỗi tai họa đủ sức gây ra thảm cảnh trên diện rộng.

<short pause> Nhưng cũng có những thứ quý giá được mang về, những báu vật mà con người khao khát, như thuốc chữa bách bệnh hay nguồn năng lượng vô tận.

<short pause> Đó là lý do con người vẫn muốn đi: hy vọng và tai họa luôn đi cùng nhau. Bạn không thể mang về báu vật mà không có nguy cơ mang về thảm họa.
```

**ElevenLabs**

```text
Manh mối đầu tiên là tấm bản đồ. Truyện tiết lộ rằng toàn bộ thế giới loài người biết đến nằm gọn giữa một cái hồ cực lớn.

[pause] Lục địa Đen bao quanh cái hồ đó, lớn hơn thế giới loài người rất nhiều lần. Những gì nhân vật chính từng khám phá chỉ là một phần rất nhỏ.

[pause] Con người không vẽ được bản đồ đầy đủ của Lục địa Đen. Chỉ có những ghi chép rời rạc của rất ít người từng đi rồi trở về.

[pause] Điều này khiến ta nhìn lại mọi thứ: những con quái vật, những vùng đất nguy hiểm mà ta từng thấy trong truyện có thể chỉ là phần rìa ngoài của một thế giới lớn hơn nhiều.

[pause] Giữa thế giới loài người và Lục địa Đen còn có những vùng đệm và những con đường được canh giữ. Truyện cho thấy việc đi qua đó thôi cũng đã là một thử thách lớn.

[pause] [chuckles] Kaku ghi chú: đây là một cú lật bàn cờ. Tất cả những gì bạn tưởng là cả thế giới, hóa ra chỉ là sân sau.

[pause] Manh mối thứ hai: lịch sử các chuyến thám hiểm. Loài người đã từng cố gắng đến Lục địa Đen nhiều lần, và phần lớn đều kết thúc bằng thảm họa.

[pause] Rất ít người trở về. Và những người trở về đôi khi mang theo những thứ khủng khiếp hơn cả cái chết của những người ở lại.

[pause] Truyện nhắc tới năm tai họa lớn đã từng được mang về thế giới loài người từ Lục địa Đen. Mỗi tai họa đủ sức gây ra thảm cảnh trên diện rộng.

[pause] Nhưng cũng có những thứ quý giá được mang về, những báu vật mà con người khao khát, như thuốc chữa bách bệnh hay nguồn năng lượng vô tận.

[pause] Đó là lý do con người vẫn muốn đi: hy vọng và tai họa luôn đi cùng nhau. Bạn không thể mang về báu vật mà không có nguy cơ mang về thảm họa.
```

### c03 · Manh mối 3: Hiệp ước cấm / Manh mối 4: Cuốn sách của một người họ Freecss / Manh mối 5: Loài kiến chimera

Khoảng 152 giây · cảnh s22–s36 · 1970 ký tự

**Gemini**

```text
Manh mối thứ ba: năm quốc gia lớn nhất của thế giới loài người đã ký hiệp ước cấm mọi người tự ý đến Lục địa Đen.

<short pause> Để đi hợp pháp, cần sự cho phép của họ, và phải đi qua những con đường được kiểm soát chặt chẽ.

<short pause> Hiệp ước này nói lên điều gì? Rằng những người có quyền lực nhất thế giới hiểu rất rõ mức độ nguy hiểm, có thể rõ hơn họ công bố.

<short pause> Nhưng cũng có một khả năng khác: họ muốn kiểm soát báu vật. Ai nắm con đường tới Lục địa Đen thì nắm nguồn lợi khổng lồ.

<short pause> <laugh> Kaku ghi chú: hãy để ý manh mối này, vì cuộc thám hiểm hiện tại xảy ra chính vì có người muốn phá hiệp ước.

<short pause> Manh mối thứ tư là một cuốn sách. Truyện nhắc tới một cuốn ghi chép về Lục địa Đen, được viết bởi một nhà thám hiểm tên là Don Freecss.

<short pause> Bạn không nghe nhầm đâu: Freecss, cùng họ với nhân vật chính Gon và cha cậu là Ging. Đây là một người trong dòng họ của họ.

<short pause> Cuốn sách được cho là chia làm nhiều phần, và chỉ một phần được biết tới rộng rãi. Những phần còn lại chưa từng công bố.

<short pause> Điều này gợi ý rằng dòng họ Freecss có một mối liên hệ đặc biệt với Lục địa Đen, và có lẽ đó là lý do cha con họ đều có máu thám hiểm đến vậy.

<short pause> Kaku ghi chú: trong một bộ truyện mà nhân vật chính bắt đầu bằng hành trình đi tìm cha, việc tổ tiên của họ là người viết về vùng đất bí ẩn nhất thế giới không thể là ngẫu nhiên.

<short pause> Manh mối thứ năm liên quan tới arc đáng sợ nhất anime: kiến chimera. Truyện cho biết loài sinh vật này có nguồn gốc từ Lục địa Đen.

<short pause> Hãy nhớ lại arc đó. Chỉ một con kiến chúa trôi dạt vào bờ đã sinh ra một đội quân suýt hủy diệt cả một quốc gia và buộc cả Hiệp hội Thợ săn phải dốc toàn lực.

<short pause> Và kẻ mạnh nhất sinh ra từ đó đã khiến người mạnh nhất thế giới loài người phải dùng tới vũ khí cuối cùng.

<short pause> Giờ hãy đặt điều đó cạnh manh mối số hai: đó mới chỉ là một sinh vật đi lạc, không phải tai họa lớn nhất. Nó không nằm trong năm tai họa được ghi chép.

<short pause> Kaku ghi chú: nếu thứ trôi dạt ngẫu nhiên đã khủng khiếp như vậy, thì những thứ còn ở trong Lục địa Đen sẽ ra sao? Đây là manh mối khiến Kaku lạnh sống lưng nhất.
```

**ElevenLabs**

```text
Manh mối thứ ba: năm quốc gia lớn nhất của thế giới loài người đã ký hiệp ước cấm mọi người tự ý đến Lục địa Đen.

[pause] Để đi hợp pháp, cần sự cho phép của họ, và phải đi qua những con đường được kiểm soát chặt chẽ.

[pause] [curious] Hiệp ước này nói lên điều gì? Rằng những người có quyền lực nhất thế giới hiểu rất rõ mức độ nguy hiểm, có thể rõ hơn họ công bố.

[pause] Nhưng cũng có một khả năng khác: họ muốn kiểm soát báu vật. Ai nắm con đường tới Lục địa Đen thì nắm nguồn lợi khổng lồ.

[pause] [chuckles] Kaku ghi chú: hãy để ý manh mối này, vì cuộc thám hiểm hiện tại xảy ra chính vì có người muốn phá hiệp ước.

[pause] Manh mối thứ tư là một cuốn sách. Truyện nhắc tới một cuốn ghi chép về Lục địa Đen, được viết bởi một nhà thám hiểm tên là Don Freecss.

[pause] Bạn không nghe nhầm đâu: Freecss, cùng họ với nhân vật chính Gon và cha cậu là Ging. Đây là một người trong dòng họ của họ.

[pause] Cuốn sách được cho là chia làm nhiều phần, và chỉ một phần được biết tới rộng rãi. Những phần còn lại chưa từng công bố.

[pause] Điều này gợi ý rằng dòng họ Freecss có một mối liên hệ đặc biệt với Lục địa Đen, và có lẽ đó là lý do cha con họ đều có máu thám hiểm đến vậy.

[pause] Kaku ghi chú: trong một bộ truyện mà nhân vật chính bắt đầu bằng hành trình đi tìm cha, việc tổ tiên của họ là người viết về vùng đất bí ẩn nhất thế giới không thể là ngẫu nhiên.

[pause] Manh mối thứ năm liên quan tới arc đáng sợ nhất anime: kiến chimera. Truyện cho biết loài sinh vật này có nguồn gốc từ Lục địa Đen.

[pause] Hãy nhớ lại arc đó. Chỉ một con kiến chúa trôi dạt vào bờ đã sinh ra một đội quân suýt hủy diệt cả một quốc gia và buộc cả Hiệp hội Thợ săn phải dốc toàn lực.

[pause] Và kẻ mạnh nhất sinh ra từ đó đã khiến người mạnh nhất thế giới loài người phải dùng tới vũ khí cuối cùng.

[pause] Giờ hãy đặt điều đó cạnh manh mối số hai: đó mới chỉ là một sinh vật đi lạc, không phải tai họa lớn nhất. Nó không nằm trong năm tai họa được ghi chép.

[pause] Kaku ghi chú: nếu thứ trôi dạt ngẫu nhiên đã khủng khiếp như vậy, thì những thứ còn ở trong Lục địa Đen sẽ ra sao? Đây là manh mối khiến Kaku lạnh sống lưng nhất.
```

### c04 · Manh mối 6: Nanika / Manh mối 7: Cái cây và người cha

Khoảng 93 giây · cảnh s37–s45 · 1207 ký tự

**Gemini**

```text
Manh mối thứ sáu nằm ngay trong gia đình sát thủ nổi tiếng nhất truyện. Một người em trong nhà có một năng lực kỳ lạ: một thực thể có thể thực hiện gần như mọi điều ước.

<short pause> Thực thể đó được gọi là Nanika. Nó thực hiện điều ước, nhưng đòi hỏi những yêu cầu đổi lại, và nếu không đáp ứng đúng luật, cái giá rất khủng khiếp.

<short pause> Khi truyện giới thiệu năm tai họa của Lục địa Đen, một trong số đó được mô tả với hình dạng khiến rất nhiều độc giả liên tưởng ngay tới Nanika.

<short pause> Giả thuyết phổ biến của fan là năng lực này thật ra là một sinh vật từ Lục địa Đen. Kaku gắn nhãn: đây là lý thuyết, dù manh mối khá mạnh.

<short pause> Nếu đúng, thì Lục địa Đen đã hiện diện trong truyện từ rất lâu trước khi được gọi tên.

<short pause> Manh mối thứ bảy đến từ người cha của nhân vật chính. Trong một cuộc trò chuyện hiếm hoi giữa hai cha con, ông nói về điều mình thật sự muốn làm.

<short pause> Ông nói ông muốn leo lên một cái cây khổng lồ nằm ở rìa thế giới, gọi là Cây Thế giới, để nhìn thấy những gì ở bên kia.

<short pause> Với một thợ săn đã khám phá gần như mọi thứ trong thế giới loài người, mục tiêu cuối cùng chỉ có thể nằm ở bên ngoài.

<short pause> Và ông đã tham gia cuộc thám hiểm hiện tại. Có vẻ người cha luôn chạy trước con mình một bước, và bước tiếp theo ấy dẫn thẳng vào Lục địa Đen.
```

**ElevenLabs**

```text
Manh mối thứ sáu nằm ngay trong gia đình sát thủ nổi tiếng nhất truyện. Một người em trong nhà có một năng lực kỳ lạ: một thực thể có thể thực hiện gần như mọi điều ước.

[pause] Thực thể đó được gọi là Nanika. Nó thực hiện điều ước, nhưng đòi hỏi những yêu cầu đổi lại, và nếu không đáp ứng đúng luật, cái giá rất khủng khiếp.

[pause] Khi truyện giới thiệu năm tai họa của Lục địa Đen, một trong số đó được mô tả với hình dạng khiến rất nhiều độc giả liên tưởng ngay tới Nanika.

[pause] Giả thuyết phổ biến của fan là năng lực này thật ra là một sinh vật từ Lục địa Đen. Kaku gắn nhãn: đây là lý thuyết, dù manh mối khá mạnh.

[pause] Nếu đúng, thì Lục địa Đen đã hiện diện trong truyện từ rất lâu trước khi được gọi tên.

[pause] Manh mối thứ bảy đến từ người cha của nhân vật chính. Trong một cuộc trò chuyện hiếm hoi giữa hai cha con, ông nói về điều mình thật sự muốn làm.

[pause] Ông nói ông muốn leo lên một cái cây khổng lồ nằm ở rìa thế giới, gọi là Cây Thế giới, để nhìn thấy những gì ở bên kia.

[pause] Với một thợ săn đã khám phá gần như mọi thứ trong thế giới loài người, mục tiêu cuối cùng chỉ có thể nằm ở bên ngoài.

[pause] Và ông đã tham gia cuộc thám hiểm hiện tại. Có vẻ người cha luôn chạy trước con mình một bước, và bước tiếp theo ấy dẫn thẳng vào Lục địa Đen.
```

### c05 · Manh mối 8: Cuộc thám hiểm hiện tại / Những lời đồn cần loại khỏi hồ sơ

Khoảng 126 giây · cảnh s46–s56 · 1638 ký tự

**Gemini**

```text
Manh mối cuối cùng là cuộc thám hiểm đang diễn ra trong truyện. Nó được khởi xướng bởi con trai của cựu chủ tịch Hiệp hội Thợ săn, người mạnh nhất thế giới loài người.

<short pause> Người này công khai tuyên bố sẽ đến Lục địa Đen, bất chấp hiệp ước. Và thay vì bị ngăn lại, một vương quốc lớn đã đứng ra tài trợ, biến nó thành chuyến đi chính thức.

<short pause> Hiệp hội Thợ săn buộc phải tham gia để giám sát, và cử những thợ săn giỏi nhất lên tàu. Trên con tàu đó còn diễn ra một cuộc tranh giành ngôi vị đầy máu giữa các hoàng tử.

<short pause> Cho tới những chương mới nhất, con tàu vẫn chưa tới nơi. Nghĩa là ta vẫn chưa thật sự thấy bên trong Lục địa Đen.

<short pause> Điều thú vị là cuộc thám hiểm này quy tụ những thợ săn giỏi nhất, những kẻ có tham vọng riêng, và cả những người muốn lợi dụng nó. Con tàu giống một phiên bản thu nhỏ của thế giới loài người.

<short pause> <laugh> Kaku ghi chú: một arc tên là Lục địa Đen, mà suốt nhiều năm nhân vật vẫn chưa đặt chân lên đó. Chỉ có Togashi mới dám làm vậy.

<short pause> Một thám tử giỏi không chỉ thu thập manh mối, mà còn loại bỏ những lời đồn không có căn cứ. Đây là ba lời đồn Kaku thấy rất nhiều trên mạng.

<short pause> Lời đồn một: Lục địa Đen là nơi Nen được sinh ra. Truyện chưa hề nói như vậy. Nen được giới thiệu là sức mạnh sự sống có trong mọi con người.

<short pause> Lời đồn hai: nhân vật chính chắc chắn sẽ lấy lại Nen ở Lục địa Đen. Đây là mong muốn của rất nhiều fan, nhưng hiện chưa có dấu hiệu nào trong truyện.

<short pause> Lời đồn ba: Hiệp hội Thợ săn biết mọi thứ về Lục địa Đen. Ngược lại, họ tham gia cuộc thám hiểm chủ yếu để kiểm soát tình hình, và chính họ cũng mù mờ về nhiều điều.

<short pause> Kaku ghi chú: loại bỏ lời đồn giúp ta thấy rõ hơn cái thật sự còn thiếu. Và cái còn thiếu nhiều hơn ta tưởng.
```

**ElevenLabs**

```text
Manh mối cuối cùng là cuộc thám hiểm đang diễn ra trong truyện. Nó được khởi xướng bởi con trai của cựu chủ tịch Hiệp hội Thợ săn, người mạnh nhất thế giới loài người.

[pause] Người này công khai tuyên bố sẽ đến Lục địa Đen, bất chấp hiệp ước. Và thay vì bị ngăn lại, một vương quốc lớn đã đứng ra tài trợ, biến nó thành chuyến đi chính thức.

[pause] Hiệp hội Thợ săn buộc phải tham gia để giám sát, và cử những thợ săn giỏi nhất lên tàu. Trên con tàu đó còn diễn ra một cuộc tranh giành ngôi vị đầy máu giữa các hoàng tử.

[pause] Cho tới những chương mới nhất, con tàu vẫn chưa tới nơi. Nghĩa là ta vẫn chưa thật sự thấy bên trong Lục địa Đen.

[pause] Điều thú vị là cuộc thám hiểm này quy tụ những thợ săn giỏi nhất, những kẻ có tham vọng riêng, và cả những người muốn lợi dụng nó. Con tàu giống một phiên bản thu nhỏ của thế giới loài người.

[pause] [chuckles] Kaku ghi chú: một arc tên là Lục địa Đen, mà suốt nhiều năm nhân vật vẫn chưa đặt chân lên đó. Chỉ có Togashi mới dám làm vậy.

[pause] Một thám tử giỏi không chỉ thu thập manh mối, mà còn loại bỏ những lời đồn không có căn cứ. Đây là ba lời đồn Kaku thấy rất nhiều trên mạng.

[pause] Lời đồn một: Lục địa Đen là nơi Nen được sinh ra. Truyện chưa hề nói như vậy. Nen được giới thiệu là sức mạnh sự sống có trong mọi con người.

[pause] Lời đồn hai: nhân vật chính chắc chắn sẽ lấy lại Nen ở Lục địa Đen. Đây là mong muốn của rất nhiều fan, nhưng hiện chưa có dấu hiệu nào trong truyện.

[pause] Lời đồn ba: Hiệp hội Thợ săn biết mọi thứ về Lục địa Đen. Ngược lại, họ tham gia cuộc thám hiểm chủ yếu để kiểm soát tình hình, và chính họ cũng mù mờ về nhiều điều.

[pause] Kaku ghi chú: loại bỏ lời đồn giúp ta thấy rõ hơn cái thật sự còn thiếu. Và cái còn thiếu nhiều hơn ta tưởng.
```

### c06 · Giả thuyết A: Nguồn gốc của những sức mạnh lạ / Giả thuyết B: Dòng họ Freecss / Giả thuyết C: Năm tai họa là năm khao khát

Khoảng 131 giây · cảnh s57–s68 · 1698 ký tự

**Gemini**

```text
Giờ đặt các manh mối cạnh nhau và đưa ra giả thuyết. Nhắc lại lần nữa: phần này là suy luận, không phải sự thật của truyện.

<short pause> Giả thuyết A: nhiều sức mạnh kỳ lạ nhất trong thế giới loài người, như kiến chimera hay năng lực thực hiện điều ước, đều có nguồn gốc từ Lục địa Đen.

<short pause> Bằng chứng ủng hộ: kiến chimera được xác nhận là từ Lục địa Đen. Và hình mô tả một tai họa rất giống thực thể trong gia đình sát thủ.

<short pause> Phản biện: truyện chưa khẳng định thực thể đó đến từ Lục địa Đen. Và không phải mọi sức mạnh lạ đều cần một nguồn gốc bên ngoài. Nen là sức mạnh của chính con người.

<short pause> Giả thuyết B: dòng họ Freecss có một sứ mệnh hoặc một mối liên kết đặc biệt với Lục địa Đen, được truyền qua nhiều thế hệ.

<short pause> Bằng chứng ủng hộ: tổ tiên viết sách về Lục địa Đen, người cha muốn leo Cây Thế giới, và nhân vật chính có tài năng thiên bẩm hiếm thấy.

<short pause> Phản biện: có thể đó chỉ là tính cách thích phiêu lưu chạy trong dòng máu, không phải sứ mệnh bí ẩn nào cả. Và nhân vật chính hiện đang không còn dùng được Nen.

<short pause> <laugh> Kaku ghi chú: Kaku thích giả thuyết này nhất, vì nó nối cái kết của hành trình tìm cha với một hành trình mới lớn hơn.

<short pause> Giả thuyết C, táo bạo hơn: năm tai họa không chỉ là quái vật, mà là hình ảnh của những khao khát lớn nhất của con người.

<short pause> Bằng chứng ủng hộ: mỗi tai họa đi kèm một báu vật mà con người muốn có, như sự sống lâu hay sức mạnh vô hạn. Hy vọng và thảm họa như hai mặt của một đồng xu.

<short pause> Phản biện: đây là cách đọc mang tính biểu tượng, truyện không nói thẳng như vậy. Có thể Togashi chỉ đơn giản muốn tạo ra những con quái vật đáng sợ nhất có thể.

<short pause> Kaku ghi chú: dù đúng hay sai, giả thuyết này giải thích vì sao con người cứ quay lại dù biết nguy hiểm. Vì thứ họ tìm kiếm chính là thứ họ khao khát nhất.
```

**ElevenLabs**

```text
Giờ đặt các manh mối cạnh nhau và đưa ra giả thuyết. Nhắc lại lần nữa: phần này là suy luận, không phải sự thật của truyện.

[pause] Giả thuyết A: nhiều sức mạnh kỳ lạ nhất trong thế giới loài người, như kiến chimera hay năng lực thực hiện điều ước, đều có nguồn gốc từ Lục địa Đen.

[pause] Bằng chứng ủng hộ: kiến chimera được xác nhận là từ Lục địa Đen. Và hình mô tả một tai họa rất giống thực thể trong gia đình sát thủ.

[pause] Phản biện: truyện chưa khẳng định thực thể đó đến từ Lục địa Đen. Và không phải mọi sức mạnh lạ đều cần một nguồn gốc bên ngoài. Nen là sức mạnh của chính con người.

[pause] Giả thuyết B: dòng họ Freecss có một sứ mệnh hoặc một mối liên kết đặc biệt với Lục địa Đen, được truyền qua nhiều thế hệ.

[pause] Bằng chứng ủng hộ: tổ tiên viết sách về Lục địa Đen, người cha muốn leo Cây Thế giới, và nhân vật chính có tài năng thiên bẩm hiếm thấy.

[pause] Phản biện: có thể đó chỉ là tính cách thích phiêu lưu chạy trong dòng máu, không phải sứ mệnh bí ẩn nào cả. Và nhân vật chính hiện đang không còn dùng được Nen.

[pause] [chuckles] Kaku ghi chú: Kaku thích giả thuyết này nhất, vì nó nối cái kết của hành trình tìm cha với một hành trình mới lớn hơn.

[pause] Giả thuyết C, táo bạo hơn: năm tai họa không chỉ là quái vật, mà là hình ảnh của những khao khát lớn nhất của con người.

[pause] Bằng chứng ủng hộ: mỗi tai họa đi kèm một báu vật mà con người muốn có, như sự sống lâu hay sức mạnh vô hạn. Hy vọng và thảm họa như hai mặt của một đồng xu.

[pause] Phản biện: đây là cách đọc mang tính biểu tượng, truyện không nói thẳng như vậy. Có thể Togashi chỉ đơn giản muốn tạo ra những con quái vật đáng sợ nhất có thể.

[pause] Kaku ghi chú: dù đúng hay sai, giả thuyết này giải thích vì sao con người cứ quay lại dù biết nguy hiểm. Vì thứ họ tìm kiếm chính là thứ họ khao khát nhất.
```

### c07 · Nếu Kaku được lên tàu / Bảng manh mối / Góc nhìn của Kaku: sức hút của một vùng tối

Khoảng 145 giây · cảnh s69–s83 · 1889 ký tự

**Gemini**

```text
<laugh> Thử tưởng tượng Kaku được mời lên con tàu thám hiểm. Dựa trên các manh mối, Kaku sẽ chuẩn bị những gì?

<short pause> Thứ nhất: một người dẫn đường. Theo những gì truyện hé lộ, đi đúng con đường và có người dẫn đường là điều kiện quan trọng bậc nhất để sống sót.

<short pause> Thứ hai: đồ bảo hộ chống bệnh và chất độc, vì trong năm tai họa có những thứ lây lan chứ không chỉ tấn công trực diện.

<short pause> Thứ ba: một cuốn sổ thật dày. Vì nếu trở về được, điều quý giá nhất không phải báu vật, mà là ghi chép để người sau không phải trả giá như người trước.

<short pause> Và thứ tư: một vé khứ hồi. Kaku nghiêm túc đấy. Trong lịch sử truyện, đi thì dễ, trở về mới là phần khó nhất.

<short pause> Tổng hợp bảng điều tra. Chắc chắn: thế giới loài người chỉ là một phần nhỏ giữa hồ lớn, có hiệp ước cấm, có năm tai họa, và kiến chimera đến từ Lục địa Đen.

<short pause> Đã xác nhận nhưng còn mờ: cuốn sách của người họ Freecss, ước mơ leo Cây Thế giới, và cuộc thám hiểm đang diễn ra.

<short pause> Lý thuyết: nguồn gốc của thực thể thực hiện điều ước, sứ mệnh của dòng họ Freecss, và ý nghĩa biểu tượng của năm tai họa.

<short pause> Và câu hỏi lớn nhất vẫn chưa ai trả lời được: bên trong Lục địa Đen thật sự có gì?

<short pause> Vì sao một bí ẩn chưa có lời giải lại khiến người ta bàn luận suốt nhiều năm như vậy?

<short pause> Kaku nghĩ là vì Hunter x Hunter bắt đầu bằng một câu chuyện về khát khao khám phá. Nhân vật chính trở thành thợ săn để đi tìm cha, người đã bỏ mọi thứ để phiêu lưu.

<short pause> Lục địa Đen là phiên bản lớn nhất của khát khao đó: một nơi mà ngay cả những thợ săn giỏi nhất cũng chưa hiểu hết.

<short pause> Và có lẽ Togashi cố tình giữ nó trong bóng tối. Một vùng đất càng ít được nhìn thấy, trí tưởng tượng của người đọc càng lấp đầy nó bằng những điều kỳ diệu và đáng sợ nhất.

<short pause> Nó cũng làm tất cả những trận đánh trước đó có thêm ý nghĩa. Những nhân vật mạnh nhất ta từng thấy có thể chỉ là người mới bắt đầu trước những gì đang chờ ngoài kia.

<short pause> Kaku thấy cách kể chuyện này rất đáng học: đôi khi điều chưa nói ra lại mạnh hơn điều đã nói.
```

**ElevenLabs**

```text
[chuckles] Thử tưởng tượng Kaku được mời lên con tàu thám hiểm. [curious] Dựa trên các manh mối, Kaku sẽ chuẩn bị những gì?

[pause] Thứ nhất: một người dẫn đường. Theo những gì truyện hé lộ, đi đúng con đường và có người dẫn đường là điều kiện quan trọng bậc nhất để sống sót.

[pause] Thứ hai: đồ bảo hộ chống bệnh và chất độc, vì trong năm tai họa có những thứ lây lan chứ không chỉ tấn công trực diện.

[pause] Thứ ba: một cuốn sổ thật dày. Vì nếu trở về được, điều quý giá nhất không phải báu vật, mà là ghi chép để người sau không phải trả giá như người trước.

[pause] Và thứ tư: một vé khứ hồi. Kaku nghiêm túc đấy. Trong lịch sử truyện, đi thì dễ, trở về mới là phần khó nhất.

[pause] Tổng hợp bảng điều tra. Chắc chắn: thế giới loài người chỉ là một phần nhỏ giữa hồ lớn, có hiệp ước cấm, có năm tai họa, và kiến chimera đến từ Lục địa Đen.

[pause] Đã xác nhận nhưng còn mờ: cuốn sách của người họ Freecss, ước mơ leo Cây Thế giới, và cuộc thám hiểm đang diễn ra.

[pause] Lý thuyết: nguồn gốc của thực thể thực hiện điều ước, sứ mệnh của dòng họ Freecss, và ý nghĩa biểu tượng của năm tai họa.

[pause] Và câu hỏi lớn nhất vẫn chưa ai trả lời được: bên trong Lục địa Đen thật sự có gì?

[pause] Vì sao một bí ẩn chưa có lời giải lại khiến người ta bàn luận suốt nhiều năm như vậy?

[pause] Kaku nghĩ là vì Hunter x Hunter bắt đầu bằng một câu chuyện về khát khao khám phá. Nhân vật chính trở thành thợ săn để đi tìm cha, người đã bỏ mọi thứ để phiêu lưu.

[pause] Lục địa Đen là phiên bản lớn nhất của khát khao đó: một nơi mà ngay cả những thợ săn giỏi nhất cũng chưa hiểu hết.

[pause] Và có lẽ Togashi cố tình giữ nó trong bóng tối. Một vùng đất càng ít được nhìn thấy, trí tưởng tượng của người đọc càng lấp đầy nó bằng những điều kỳ diệu và đáng sợ nhất.

[pause] Nó cũng làm tất cả những trận đánh trước đó có thêm ý nghĩa. Những nhân vật mạnh nhất ta từng thấy có thể chỉ là người mới bắt đầu trước những gì đang chờ ngoài kia.

[pause] Kaku thấy cách kể chuyện này rất đáng học: đôi khi điều chưa nói ra lại mạnh hơn điều đã nói.
```

### c08 · Kết: câu hỏi mở

Khoảng 44 giây · cảnh s84–s87 · 569 ký tự

**Gemini**

```text
Tóm lại vụ án: Lục địa Đen bao quanh thế giới loài người, bị cấm đi vào, đã từng gây ra năm tai họa, là nơi sinh ra loài kiến chimera, và có liên quan tới dòng họ Freecss.

<short pause> Và hồ sơ này vẫn chưa đóng. Câu hỏi cho bạn: bạn nghĩ bên trong Lục địa Đen có gì? Hay bạn có giả thuyết D của riêng mình? <laugh> Viết vào phần bình luận để Kaku thêm vào bảng điều tra nhé.

<short pause> Video tới, Kaku rời phòng điều tra để phân tích từng đường kiếm trong một trận đấu kinh điển: trận chiến trên núi của Kimetsu no Yaiba.

<short pause> Đăng ký kênh để không bỏ lỡ nhé. Thám tử Kaku treo áo khoác lên đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Tóm lại vụ án: Lục địa Đen bao quanh thế giới loài người, bị cấm đi vào, đã từng gây ra năm tai họa, là nơi sinh ra loài kiến chimera, và có liên quan tới dòng họ Freecss.

[pause] Và hồ sơ này vẫn chưa đóng. [curious] Câu hỏi cho bạn: bạn nghĩ bên trong Lục địa Đen có gì? Hay bạn có giả thuyết D của riêng mình? [chuckles] Viết vào phần bình luận để Kaku thêm vào bảng điều tra nhé.

[pause] Video tới, Kaku rời phòng điều tra để phân tích từng đường kiếm trong một trận đấu kinh điển: trận chiến trên núi của Kimetsu no Yaiba.

[pause] Đăng ký kênh để không bỏ lỡ nhé. Thám tử Kaku treo áo khoác lên đây, hẹn gặp lại!
```
