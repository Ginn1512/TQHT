# Bộ prompt · Du hành thời gian: Tokyo Revengers vs Steins;Gate vs Re:Zero — luật nào chặt nhất?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 89 ảnh, 9 đoạn đọc, khoảng 16.9 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (89 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết anime mùa ba Tokyo Revengers, phần lớn Steins;Gate mùa một, và Re:Zer…

```text
Wide 16:9 landscape cinematic frame. three closed books stacked on a desk, each tied with a ribbon and a small clock charm, a warning sign card leaning against them, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Ba người trẻ tuổi, ba thế giới, và cùng một năng lực: quay ngược thời gian để sửa một bi kịch. Một người chỉ…

```text
Wide 16:9 landscape cinematic frame. three glowing symbols on a dark table: two clasped hands, a flip phone with a glowing screen, and a cracked hourglass, overhead shot, dramatic amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nghe thì giống nhau, nhưng luật chơi của ba cỗ máy thời gian này khác nhau rất xa. Có cỗ máy được giải thích…

```text
Wide 16:9 landscape cinematic frame. three different mechanical clocks with exposed gears, one labeled with precise numbers, one blank, one shrouded in shadow, still life, warm light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Câu hỏi hôm nay: trong Tokyo Revengers, Steins;Gate và Re:Zero, luật du hành thời gian của bộ nào chặt chẽ nh…

```text
Wide 16:9 landscape cinematic frame. a balance scale on a desk with three small clocks waiting to be weighed, close-up, soft spotlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku làm trọng tài cho ba nhà du hành thời gian, chấm điểm theo năm tiêu…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny referee whistle, standing behind a table with three clocks, gesturing like a host. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Kaku nói trước: điểm số là ý kiến của Kaku, dựa trên những gì truyện thể hiện. Bạn hoàn toàn có thể chấm khác…

```text
Wide 16:9 landscape cinematic frame. a scorecard on parchment with three empty columns and a pencil resting on top, close-up, warm amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · Ba nhà du hành trong một phút

Lời: Đấu thủ số một: Hanagaki Takemichi của Tokyo Revengers. Một thanh niên hai mươi sáu tuổi, sống một cuộc đời n…

```text
Wide 16:9 landscape cinematic frame. a tired young man in a small cluttered apartment staring at a TV news report, back view, dim evening light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Bị đẩy xuống đường ray tàu, Takemichi bỗng tỉnh dậy ở đúng mười hai năm trước, trong cơ thể của chính mình th…

```text
Wide 16:9 landscape cinematic frame. a train platform with a blurred train rushing past, a single figure falling toward the tracks, motion blur, dramatic cold light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Đấu thủ số hai: Okabe Rintaro của Steins;Gate. Một sinh viên tự xưng là nhà khoa học điên, cùng bạn bè mở một…

```text
Wide 16:9 landscape cinematic frame. a cramped makeshift laboratory above a shop, cluttered with wires, gadgets and a whiteboard of scribbles, wide shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Nhóm của Okabe vô tình phát hiện ra rằng chiếc điện thoại nối với lò vi sóng có thể gửi tin nhắn về quá khứ.…

```text
Wide 16:9 landscape cinematic frame. a microwave oven wired to a flip phone on a cluttered workbench, sparks and a faint glow inside, close-up, eerie green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Đấu thủ số ba: Natsuki Subaru của Re:Zero. Một thanh niên đang đi mua đồ ở cửa hàng tiện lợi thì bị đưa sang…

```text
Wide 16:9 landscape cinematic frame. a young man holding a plastic convenience store bag standing bewildered in a medieval fantasy marketplace, wide shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Năng lực duy nhất của Subaru được gọi là Hồi sinh từ cái chết. Mỗi khi chết, cậu quay về một thời điểm trước…

```text
Wide 16:9 landscape cinematic frame. an hourglass lying on its side with sand flowing backward into the upper chamber, dark background, close-up, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13 · **Kaku** (đính kèm ảnh mẫu)

Lời: Ba người, ba cách quay lại. Kaku đặt họ lên cùng một bàn. Nhưng trước khi chấm, trọng tài phải công bố luật c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot placing three small clocks on a round table and tapping a rulebook with its wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14 · Luật chấm điểm của trọng tài

Lời: Tiêu chí một: Luật có rõ không. Người xem có hiểu được cỗ máy hoạt động thế nào, bắt đầu từ đâu, quay về bao…

```text
Wide 16:9 landscape cinematic frame. a clean rulebook page with a numbered list and a small magnifying glass icon, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Tiêu chí hai: Có nhất quán không. Khi luật đã được đặt ra, câu chuyện có giữ đúng luật tới cuối, hay có những…

```text
Wide 16:9 landscape cinematic frame. a long chain of linked metal rings on a table, one ring slightly cracked, extreme close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Tiêu chí ba: Cái giá. Mỗi lần quay lại, nhân vật phải trả gì: đau đớn, ký ức, sự cô đơn, hay mất đi người khá…

```text
Wide 16:9 landscape cinematic frame. a small brass price tag hanging from an old clock, dramatic side light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Tiêu chí bốn: Chống lạm dụng. Nhân vật có thể dùng năng lực để gian lận mọi thứ không, hay luật đủ chặt để gi…

```text
Wide 16:9 landscape cinematic frame. a padlock fastened around a pocket watch on a velvet cloth, close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Tiêu chí năm: Sức nặng cảm xúc. Luật chơi có khiến ta đau cùng nhân vật không, hay chỉ là một công cụ để đẩy…

```text
Wide 16:9 landscape cinematic frame. a single tear drop falling onto a clock face, extreme close-up, soft blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Mỗi tiêu chí mười điểm, tổng năm mươi. Và Kaku nhắc lại: đây là chấm độ chặt của luật du hành, không phải chấ…

```text
Wide 16:9 landscape cinematic frame. a scoreboard drawn on parchment with five rows and three columns, the maximum 50 written at the bottom, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20 · Vòng 1: Luật có rõ không?

Lời: Tokyo Revengers trước. Luật khá đơn giản: Takemichi bắt tay với Naoto, em trai của Hina, và cậu được đưa về đ…

```text
Wide 16:9 landscape cinematic frame. two hands clasping firmly with a soft glow of light around the grip, a calendar with two years circled in the background, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Thời gian ở quá khứ vẫn chạy song song. Nếu Takemichi ở quá khứ một tuần, thì khi về hiện tại cũng đã trôi qu…

```text
Wide 16:9 landscape cinematic frame. two parallel timelines drawn on parchment with matching tick marks, one labeled past and one labeled present, amber ink. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22

Lời: Luật này dễ hiểu, dễ nhớ. Nhưng có một câu hỏi truyện không trả lời ngay: vì sao lại là mười hai năm, và vì s…

```text
Wide 16:9 landscape cinematic frame. a large question mark drawn over a calendar with the number twelve circled, parchment close-up, amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Steins;Gate thì chi tiết tới mức gần như sách giáo khoa. Có hai cách: D-mail là gửi tin nhắn ngắn về quá khứ,…

```text
Wide 16:9 landscape cinematic frame. a notebook page split in two: on the left a small envelope flying back along a timeline, on the right a glowing brain flying back along a timeline, diagram, amber ink. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Máy Time Leap đọc cấu trúc não, chuyển ký ức thành dữ liệu, rồi gửi về quá khứ bằng chính công nghệ D-mail. V…

```text
Wide 16:9 landscape cinematic frame. a headset connected by cables to a small machine, a digital display showing the number 48, close-up, eerie green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Vì sao là bốn mươi tám giờ? Truyện giải thích: não người thay đổi theo thời gian. Nhảy xa hơn thì ký ức mới k…

```text
Wide 16:9 landscape cinematic frame. a translucent brain diagram with a glowing puzzle piece that does not fit its slot, medical-style illustration, cool light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Re:Zero thì ngược lại. Luật cốt lõi rất rõ: chết thì quay về. Nhưng điểm quay về ở đâu thì Subaru không được…

```text
Wide 16:9 landscape cinematic frame. a game-style save point icon glowing on a dark path, with footprints leading past it into fog, wide shot, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Điểm quay về thay đổi theo những thời khắc quan trọng của câu chuyện, và người ta cho rằng có một ý chí nào đ…

```text
Wide 16:9 landscape cinematic frame. a glowing save icon moving along a path by itself while a small figure chases it, whimsical wide shot, dusk light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Điểm vòng một: Steins;Gate chín, vì mọi thứ đều có con số và lý do. Tokyo Revengers bảy, luật dễ hiểu nhưng t…

```text
Wide 16:9 landscape cinematic frame. a scoreboard on parchment with round one filled in: nine, seven, six, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Vòng 2: Có nhất quán không?

Lời: Steins;Gate có một khái niệm rất đẹp: đường thế giới. Mỗi thay đổi trong quá khứ đẩy thế giới sang một đường…

```text
Wide 16:9 landscape cinematic frame. a web of glowing parallel lines stretching into darkness, each labeled with a small decimal number, abstract wide shot, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Nhiều đường thế giới gom lại thành một nhóm gọi là trường hút. Trong cùng một trường hút, có những sự kiện lu…

```text
Wide 16:9 landscape cinematic frame. many thin glowing lines converging into a single bright knot before spreading apart again, abstract diagram, cool light. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và đây là chỗ Steins;Gate tàn nhẫn nhất. Okabe cố cứu một người bạn thân, nhưng dù quay lại bao nhiêu lần, cô…

```text
Wide 16:9 landscape cinematic frame. a wall calendar with the same date circled again and again in red ink across many overlapping pages, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Luật này không bao giờ bị phá một cách dễ dãi. Muốn thoát khỏi điểm hội tụ, Okabe phải trả đúng cái giá mà lu…

```text
Wide 16:9 landscape cinematic frame. a heavy iron gate with an intricate lock, a single key hovering in front of it, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Tokyo Revengers thì gặp nhiều tranh luận hơn. Người xem hay hỏi: nếu Naoto nhớ được mọi thứ vì được kể lại, v…

```text
Wide 16:9 landscape cinematic frame. a cork board covered in photos connected by red string, with several question marks pinned among them, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Công bằng mà nói, Tokyo Revengers là truyện về băng nhóm và tình bạn. Cỗ máy thời gian là công cụ, không phải…

```text
Wide 16:9 landscape cinematic frame. a group of young friends sitting on motorbikes at night under a street lamp, back view, warm nostalgic light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Re:Zero giấu luật đi, nhưng không phá luật. Mỗi khi Subaru hiểu thêm một điều về năng lực, điều đó được giữ đ…

```text
Wide 16:9 landscape cinematic frame. a notebook with a handwritten list of rules growing longer page by page, each rule checked off, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rất thích cách Re:Zero để người xem học luật cùng nhân vật. Ta không được đưa sách hướng dẫn, ta phải tự…

```text
Wide 16:9 landscape cinematic frame. the owl mascot flipping through a blank instruction manual and scribbling notes in it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Điểm vòng hai: Steins;Gate mười, Re:Zero tám, Tokyo Revengers sáu. Sau hai vòng: Steins;Gate mười chín, Re:Ze…

```text
Wide 16:9 landscape cinematic frame. the scoreboard updated with round two: ten, eight, six, and running totals, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38 · Vòng 3: Cái giá

Lời: Giờ tới câu hỏi Kaku thích nhất: mỗi lần quay lại, người du hành phải trả gì?

```text
Wide 16:9 landscape cinematic frame. an old merchant's scale with a clock on one side and a heart-shaped stone on the other, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Takemichi phải chiến đấu trong quá khứ với cơ thể của một học sinh yếu ớt. Cậu bị đánh rất nhiều. Và mỗi lần…

```text
Wide 16:9 landscape cinematic frame. a bruised teenage fist clenched on the ground of an alley, rain puddles around, extreme close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Cái giá lớn nhất là cô đơn. Takemichi mang ký ức của những dòng thời gian mà không ai khác nhớ. Người duy nhấ…

```text
Wide 16:9 landscape cinematic frame. a lone young man sitting at a bus stop at night surrounded by blurred passing crowds, wide shot, lonely blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41

Lời: Okabe có một năng lực riêng gọi là Reading Steiner: khi thế giới đổi sang đường khác, chỉ cậu nhớ đường cũ. N…

```text
Wide 16:9 landscape cinematic frame. a young man standing still in a crowded street while everyone else blurs and shifts around him, long exposure effect, eerie light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Để thoát khỏi điểm hội tụ, Okabe phải xóa từng tin nhắn đã gửi về quá khứ. Mà mỗi tin nhắn đó là điều ước của…

```text
Wide 16:9 landscape cinematic frame. a row of glowing text messages on a phone screen being deleted one by one, each fading into ash, close-up, sad blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Subaru thì trả giá bằng chính cơ thể. Cậu phải thật sự chết, cảm nhận đau đớn, rồi tỉnh lại như chưa có gì. M…

```text
Wide 16:9 landscape cinematic frame. a young man waking up with a sharp gasp in a sunlit street, hand clutching his chest, medium shot, harsh contrasting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Và có một luật khiến cái giá đó nặng gấp đôi: Subaru không thể kể cho bất kỳ ai về năng lực. Hễ cậu định nói,…

```text
Wide 16:9 landscape cinematic frame. a frozen moment where falling leaves hang mid-air, a shadowy hand reaching toward a softly glowing heart, symbolic dark illustration, cold light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Nghĩa là Subaru phải chịu đựng tất cả một mình, và bị người khác hiểu lầm vì những hành động mà họ không thể…

```text
Wide 16:9 landscape cinematic frame. a young man standing alone in a doorway while a group of people look at him with confusion and distrust, medium shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Điểm vòng ba: Re:Zero mười, vì không cái giá nào đau hơn. Steins;Gate chín. Tokyo Revengers bảy. Sau ba vòng:…

```text
Wide 16:9 landscape cinematic frame. the scoreboard updated with round three: ten, nine, seven, and running totals twenty-eight, twenty-four, twenty, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · Vòng 4: Chống lạm dụng

Lời: Một năng lực du hành thời gian tốt phải có giới hạn. Nếu không, nhân vật chỉ cần quay lại mãi cho tới khi mọi…

```text
Wide 16:9 landscape cinematic frame. a video game controller with a glowing rewind button crossed out in red, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48

Lời: Takemichi không chọn được thời điểm. Luôn là mười hai năm. Cậu cũng cần Naoto ở cả hai đầu. Nếu Naoto không c…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing in an empty station, holding out a hand that no one takes, wide shot, lonely light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Okabe bị giới hạn bởi bốn mươi tám giờ, bởi chiếc máy có thể hỏng, và bởi một tổ chức bí ẩn luôn theo dõi. Mỗ…

```text
Wide 16:9 landscape cinematic frame. a small machine sparking and smoking on a workbench, a digital countdown clock on the wall behind, close-up, tense green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Subaru bị giới hạn theo cách đáng sợ nhất. Cậu không chọn được điểm lưu. Nếu điểm lưu rơi vào một tình huống…

```text
Wide 16:9 landscape cinematic frame. a looping path drawn as a closed circle in the dark, a small figure walking it again and again, overhead shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Cậu cũng không được chia sẻ thông tin. Biết tương lai mà không được nói ra, Subaru phải tìm cách thuyết phục…

```text
Wide 16:9 landscape cinematic frame. a young man with his mouth covered by a shadowy ribbon, eyes pleading, close-up, dramatic dark light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku thấy cả ba đều khá chặt ở vòng này. Nhưng Steins;Gate và Re:Zero có thêm lớp khóa: một bên là luật vật l…

```text
Wide 16:9 landscape cinematic frame. the owl mascot examining three padlocks on a table with a magnifying glass, one lock has a double chain. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Điểm vòng bốn: Steins;Gate chín, Re:Zero chín, Tokyo Revengers tám. Sau bốn vòng: Steins;Gate ba mươi bảy, Re…

```text
Wide 16:9 landscape cinematic frame. the scoreboard updated with round four: nine, nine, eight, and running totals, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54 · Vòng 5: Sức nặng cảm xúc

Lời: Vòng cuối không đo luật mà đo trái tim: luật chơi có khiến ta đau cùng nhân vật không.

```text
Wide 16:9 landscape cinematic frame. a clock with a heartbeat line drawn across its face, close-up, soft warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Takemichi được gọi là anh hùng hay khóc. Cậu không mạnh, không thông minh, nhưng không bao giờ bỏ cuộc. Mỗi l…

```text
Wide 16:9 landscape cinematic frame. a young man with tear-streaked face standing up again in a rain-soaked alley, fists clenched, low-angle shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Okabe bắt đầu truyện với vai diễn nhà khoa học điên, cười lớn, nói những câu kỳ quặc. Càng quay lại nhiều lần…

```text
Wide 16:9 landscape cinematic frame. a cracked theatrical mask lying on a lab floor beside a coffee cup, close-up, cold morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Những tập giữa Steins;Gate, khi Okabe nhảy lại cùng một ngày hết lần này tới lần khác, được nhiều người xem n…

```text
Wide 16:9 landscape cinematic frame. a sequence of identical clock faces receding into the distance like a tunnel, a small figure walking through, surreal wide shot, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Subaru thì có lẽ là nhân vật được xem suy sụp rõ nhất trong ba người. Có những lúc cậu muốn bỏ cuộc, và Re:Ze…

```text
Wide 16:9 landscape cinematic frame. a young man sitting on stone steps at night, head in hands, a distant warm light glowing behind him, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Cảnh một người bạn nói với Subaru rằng hãy bắt đầu lại từ số không, cùng nhau, là một trong những cảnh nổi ti…

```text
Wide 16:9 landscape cinematic frame. two silhouettes sitting side by side on a hill under a vast starry sky, one leaning on the other's shoulder, wide shot, gentle blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Điểm vòng năm: Steins;Gate mười, Re:Zero mười, Tokyo Revengers tám. Hai bộ đầu hòa nhau ở vòng này, vì cả hai…

```text
Wide 16:9 landscape cinematic frame. the scoreboard updated with round five: ten, ten, eight, parchment close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61 · Thử thách phụ: cứu chiếc bánh sinh nhật

Lời: Trước khi công bố kết quả, Kaku cho ba nhà du hành một thử thách vui. Ba giờ chiều nay, bạn làm rơi chiếc bán…

```text
Wide 16:9 landscape cinematic frame. a birthday cake upside down on a kitchen floor, frosting splattered, a sad candle lying beside it, close-up, bright kitchen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Takemichi: bắt tay Naoto, và thế là cậu về mười hai năm trước. Chiếc bánh còn chưa được làm. Cậu phải chờ mườ…

```text
Wide 16:9 landscape cinematic frame. a young man looking at a calendar in dismay with twelve years of pages flipping by, humorous medium shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Okabe: gửi một D-mail về trưa nay: nhớ cầm bánh bằng hai tay. Chiếc bánh được cứu. Nhưng đường thế giới lệch…

```text
Wide 16:9 landscape cinematic frame. a flip phone showing a short glowing message, beside a perfectly intact cake on a table, while the shop sign outside the window has changed, close-up, eerie green light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Subaru: cậu không chọn được lúc quay lại, và Kaku không bao giờ khuyên ai liều mạng vì một chiếc bánh. Subaru…

```text
Wide 16:9 landscape cinematic frame. a young man cheerfully mopping a kitchen floor while holding a new cake box under one arm, humorous medium shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kết quả thử thách phụ: Steins;Gate thắng. Và đây chính là lý do Kaku nói luật của Steins;Gate chặt nhất: nó c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot holding a slice of cake on a plate, looking smug, a tiny trophy beside it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Kết quả chung cuộc

Lời: Và đây là bảng điểm chung cuộc. Tokyo Revengers: bảy, sáu, bảy, tám, tám. Tổng ba mươi sáu trên năm mươi.

```text
Wide 16:9 landscape cinematic frame. a large scoreboard on parchment with the first column fully filled and the total 36 circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Re:Zero: sáu, tám, mười, chín, mười. Tổng bốn mươi ba trên năm mươi.

```text
Wide 16:9 landscape cinematic frame. the scoreboard with the second column totaled at 43 circled, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Steins;Gate: chín, mười, chín, chín, mười. Tổng bốn mươi bảy trên năm mươi. Người chiến thắng về độ chặt của…

```text
Wide 16:9 landscape cinematic frame. the scoreboard with the third column totaled at 47 circled and a small gold star beside it, amber ink close-up, warm triumphant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Steins;Gate thắng vì nó xem du hành thời gian là khoa học: có con số, có giới hạn, có hậu quả. Mọi bi kịch đề…

```text
Wide 16:9 landscape cinematic frame. a precise engineering blueprint of a time machine pinned to a wall with measurements and notes, close-up, cool light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Re:Zero đứng thứ hai vì nó xem du hành thời gian là lời nguyền: luật giấu kín, cái giá tàn nhẫn, và cô đơn tu…

```text
Wide 16:9 landscape cinematic frame. a dark ornate hourglass wrapped in thorny vines on a stone pedestal, close-up, ominous purple light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Tokyo Revengers đứng thứ ba, nhưng Kaku muốn nói rõ: đây không phải bộ kém. Nó xem du hành thời gian là một c…

```text
Wide 16:9 landscape cinematic frame. two hands shaking over a table with old photos of friends scattered around, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Nếu bạn muốn một câu đố logic, hãy xem Steins;Gate. Nếu bạn muốn một hành trình đau đớn, hãy xem Re:Zero. Nếu…

```text
Wide 16:9 landscape cinematic frame. three doors side by side, one with a gear symbol, one with a thorn symbol, one with a handshake symbol, wide shot, inviting warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73 · Giải thưởng phụ

Lời: Kaku trao thêm ba giải phụ. Giải Luật dễ hiểu nhất: Tokyo Revengers. Một cái bắt tay, mười hai năm, ai cũng n…

```text
Wide 16:9 landscape cinematic frame. a small ribbon award pinned beside a drawing of two clasped hands, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Giải Cái giá đau nhất: Re:Zero. Không bộ nào bắt nhân vật chính trả giá bằng chính mình nhiều như vậy.

```text
Wide 16:9 landscape cinematic frame. a ribbon award beside a cracked hourglass, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75

Lời: Giải Gắn với đời thật nhất: Steins;Gate. Truyện lấy cảm hứng từ John Titor, một người từng đăng bài trên mạng…

```text
Wide 16:9 landscape cinematic frame. an old CRT computer monitor showing a dim internet forum page, a small clock icon in the corner, close-up, nostalgic green glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Trong truyện còn có một chiếc máy tính cổ tên là IBN 5100, lấy cảm hứng từ máy IBM 5100 có thật, ra đời năm 1…

```text
Wide 16:9 landscape cinematic frame. a vintage portable computer with a tiny screen and a chunky keyboard on a wooden desk, close-up, warm retro light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku cũng tặng một giải cho chính mình: Trọng tài chấm điểm công bằng nhất. Không ai phản đối đâu nhỉ?

```text
Wide 16:9 landscape cinematic frame. the owl mascot pinning a tiny ribbon onto its own chest with a proud expression. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78 · Một bí mật hậu trường

Lời: Có một chi tiết thú vị: anime Steins;Gate năm 2011 và anime Re:Zero năm 2016 đều do cùng một studio thực hiện…

```text
Wide 16:9 landscape cinematic frame. two anime production storyboards side by side on a studio desk with the same fox-shaped logo stamp in the corner, close-up, warm studio light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Nhiều người xem nhận ra hai bộ có không khí giống nhau: nhịp chậm lúc đầu, rồi đột ngột trở nên nặng nề, và n…

```text
Wide 16:9 landscape cinematic frame. two film reels intertwined on a table, one labeled with a gear and one with a thorn, close-up, moody light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Nếu bạn đã xem một trong hai bộ và thích, bộ còn lại gần như chắc chắn hợp với bạn.

```text
Wide 16:9 landscape cinematic frame. a bookshelf with two volumes placed side by side, a small sticky note connecting them with an arrow, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Nếu bạn có một lần quay lại

Lời: Giờ tới lượt bạn. Nếu được chọn một trong ba năng lực, bạn chọn cái nào?

```text
Wide 16:9 landscape cinematic frame. three glowing cards on a table: a handshake, a phone, an hourglass, a hand hovering over them deciding, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Bắt tay để về đúng mười hai năm trước, sửa những gì bạn tiếc nuối từ thời đi học. Hoặc gửi tin nhắn về hai ng…

```text
Wide 16:9 landscape cinematic frame. a comparison chart on parchment with two columns of small doodles: a school building and a flip phone, amber ink close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Hoặc quay về mỗi khi thất bại, không giới hạn số lần, nhưng không bao giờ được kể cho ai biết bạn đã trải qua…

```text
Wide 16:9 landscape cinematic frame. a lonely figure doodled inside a looping arrow on parchment, a small lock drawn over its mouth, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn tin nhắn, vì Kaku chỉ cần sửa câu nói sai trong video trước. Viết lựa chọn của bạn vào bình luận, k…

```text
Wide 16:9 landscape cinematic frame. the owl mascot typing on a tiny flip phone with a sheepish look. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85

Lời: Và nếu bạn không đồng ý với bảng điểm, hãy viết bảng điểm của bạn. Kaku sẽ đọc hết và làm một video trả lời n…

```text
Wide 16:9 landscape cinematic frame. a comment box drawn on parchment with several different scoreboards scribbled inside, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86 · Kết

Lời: Ba nhà du hành, ba cỗ máy, và cùng một bài học: quay lại quá khứ không làm mọi thứ dễ hơn. Nó chỉ cho bạn thê…

```text
Wide 16:9 landscape cinematic frame. three silhouettes standing on three separate timelines that converge toward a single bright horizon, wide shot, bittersweet dawn light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87

Lời: Có lẽ vì vậy mà cả ba bộ đều kết luận giống nhau: điều cứu nhân vật không phải cỗ máy, mà là những người đã ở…

```text
Wide 16:9 landscape cinematic frame. several hands placed on top of one another over an old clock, close-up, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88

Lời: Video tiếp theo, Kaku mở dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ khi Muzan trở thành quỷ tới ng…

```text
Wide 16:9 landscape cinematic frame. a long scroll unrolling across a table with ink marks for centuries, a small blade icon at the far end, close-up, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích xem Kaku làm trọng tài, hãy đăng ký kênh. Không cần quay ngược thời gian, chỉ cần một cái bấm.…

```text
Wide 16:9 landscape cinematic frame. the owl mascot blowing its referee whistle and waving goodbye beside the finished scoreboard. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 77 giây · cảnh s01–s06 · 996 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết anime mùa ba Tokyo Revengers, phần lớn Steins;Gate mùa một, và Re:Zero mùa một. Kaku giữ kín cái kết của Steins;Gate. Nếu bạn chưa xem, hãy lưu video lại.

<short pause> Ba người trẻ tuổi, ba thế giới, và cùng một năng lực: quay ngược thời gian để sửa một bi kịch. Một người chỉ cần bắt tay. Một người gửi tin nhắn. Còn người thứ ba phải chết.

<short pause> Nghe thì giống nhau, nhưng luật chơi của ba cỗ máy thời gian này khác nhau rất xa. Có cỗ máy được giải thích tới từng con số. Có cỗ máy mà chính nhân vật cũng không hiểu.

<short pause> Câu hỏi hôm nay: trong Tokyo Revengers, Steins;Gate và Re:Zero, luật du hành thời gian của bộ nào chặt chẽ nhất? Và chặt chẽ có phải là hay nhất không?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku làm trọng tài cho ba nhà du hành thời gian, chấm điểm theo năm tiêu chí, và cuối video là bảng điểm chung cuộc.

<short pause> Kaku nói trước: điểm số là ý kiến của Kaku, dựa trên những gì truyện thể hiện. Bạn hoàn toàn có thể chấm khác, và phần bình luận chính là chỗ để tranh luận.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết anime mùa ba Tokyo Revengers, phần lớn Steins;Gate mùa một, và Re:Zero mùa một. Kaku giữ kín cái kết của Steins;Gate. Nếu bạn chưa xem, hãy lưu video lại.

[pause] Ba người trẻ tuổi, ba thế giới, và cùng một năng lực: quay ngược thời gian để sửa một bi kịch. Một người chỉ cần bắt tay. Một người gửi tin nhắn. Còn người thứ ba phải chết.

[pause] Nghe thì giống nhau, nhưng luật chơi của ba cỗ máy thời gian này khác nhau rất xa. Có cỗ máy được giải thích tới từng con số. Có cỗ máy mà chính nhân vật cũng không hiểu.

[pause] [curious] Câu hỏi hôm nay: trong Tokyo Revengers, Steins;Gate và Re:Zero, luật du hành thời gian của bộ nào chặt chẽ nhất? Và chặt chẽ có phải là hay nhất không?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku làm trọng tài cho ba nhà du hành thời gian, chấm điểm theo năm tiêu chí, và cuối video là bảng điểm chung cuộc.

[pause] Kaku nói trước: điểm số là ý kiến của Kaku, dựa trên những gì truyện thể hiện. Bạn hoàn toàn có thể chấm khác, và phần bình luận chính là chỗ để tranh luận.
```

### c02 · Ba nhà du hành trong một phút / Luật chấm điểm của trọng tài

Khoảng 142 giây · cảnh s07–s19 · 1850 ký tự

**Gemini**

```text
Đấu thủ số một: Hanagaki Takemichi của Tokyo Revengers. Một thanh niên hai mươi sáu tuổi, sống một cuộc đời nhạt nhòa, cho tới khi biết tin người yêu cũ thời trung học là Hina đã chết.

<short pause> Bị đẩy xuống đường ray tàu, Takemichi bỗng tỉnh dậy ở đúng mười hai năm trước, trong cơ thể của chính mình thời học sinh. Và cậu quyết định cứu Hina.

<short pause> Đấu thủ số hai: Okabe Rintaro của Steins;Gate. Một sinh viên tự xưng là nhà khoa học điên, cùng bạn bè mở một phòng thí nghiệm nhỏ trên tầng hai một cửa hàng ở Akihabara.

<short pause> Nhóm của Okabe vô tình phát hiện ra rằng chiếc điện thoại nối với lò vi sóng có thể gửi tin nhắn về quá khứ. Một phát minh tình cờ, và mọi thứ bắt đầu từ đó.

<short pause> Đấu thủ số ba: Natsuki Subaru của Re:Zero. Một thanh niên đang đi mua đồ ở cửa hàng tiện lợi thì bị đưa sang một thế giới kỳ ảo, không có sức mạnh, không có phép thuật.

<short pause> Năng lực duy nhất của Subaru được gọi là Hồi sinh từ cái chết. Mỗi khi chết, cậu quay về một thời điểm trước đó, và chỉ mình cậu còn nhớ những gì đã xảy ra.

<short pause> Ba người, ba cách quay lại. <laugh> Kaku đặt họ lên cùng một bàn. <short pause> Nhưng trước khi chấm, trọng tài phải công bố luật chấm điểm.

<short pause> Tiêu chí một: Luật có rõ không. Người xem có hiểu được cỗ máy hoạt động thế nào, bắt đầu từ đâu, quay về bao xa, và cần điều kiện gì không.

<short pause> Tiêu chí hai: Có nhất quán không. Khi luật đã được đặt ra, câu chuyện có giữ đúng luật tới cuối, hay có những chỗ tự mâu thuẫn.

<short pause> Tiêu chí ba: Cái giá. Mỗi lần quay lại, nhân vật phải trả gì: đau đớn, ký ức, sự cô đơn, hay mất đi người khác.

<short pause> Tiêu chí bốn: Chống lạm dụng. Nhân vật có thể dùng năng lực để gian lận mọi thứ không, hay luật đủ chặt để giữ căng thẳng.

<short pause> Tiêu chí năm: Sức nặng cảm xúc. Luật chơi có khiến ta đau cùng nhân vật không, hay chỉ là một công cụ để đẩy cốt truyện.

<short pause> Mỗi tiêu chí mười điểm, tổng năm mươi. Và Kaku nhắc lại: đây là chấm độ chặt của luật du hành, không phải chấm toàn bộ bộ truyện.
```

**ElevenLabs**

```text
Đấu thủ số một: Hanagaki Takemichi của Tokyo Revengers. Một thanh niên hai mươi sáu tuổi, sống một cuộc đời nhạt nhòa, cho tới khi biết tin người yêu cũ thời trung học là Hina đã chết.

[pause] Bị đẩy xuống đường ray tàu, Takemichi bỗng tỉnh dậy ở đúng mười hai năm trước, trong cơ thể của chính mình thời học sinh. Và cậu quyết định cứu Hina.

[pause] Đấu thủ số hai: Okabe Rintaro của Steins;Gate. Một sinh viên tự xưng là nhà khoa học điên, cùng bạn bè mở một phòng thí nghiệm nhỏ trên tầng hai một cửa hàng ở Akihabara.

[pause] Nhóm của Okabe vô tình phát hiện ra rằng chiếc điện thoại nối với lò vi sóng có thể gửi tin nhắn về quá khứ. Một phát minh tình cờ, và mọi thứ bắt đầu từ đó.

[pause] Đấu thủ số ba: Natsuki Subaru của Re:Zero. Một thanh niên đang đi mua đồ ở cửa hàng tiện lợi thì bị đưa sang một thế giới kỳ ảo, không có sức mạnh, không có phép thuật.

[pause] Năng lực duy nhất của Subaru được gọi là Hồi sinh từ cái chết. Mỗi khi chết, cậu quay về một thời điểm trước đó, và chỉ mình cậu còn nhớ những gì đã xảy ra.

[pause] Ba người, ba cách quay lại. [chuckles] Kaku đặt họ lên cùng một bàn. [pause] Nhưng trước khi chấm, trọng tài phải công bố luật chấm điểm.

[pause] Tiêu chí một: Luật có rõ không. Người xem có hiểu được cỗ máy hoạt động thế nào, bắt đầu từ đâu, quay về bao xa, và cần điều kiện gì không.

[pause] Tiêu chí hai: Có nhất quán không. Khi luật đã được đặt ra, câu chuyện có giữ đúng luật tới cuối, hay có những chỗ tự mâu thuẫn.

[pause] Tiêu chí ba: Cái giá. Mỗi lần quay lại, nhân vật phải trả gì: đau đớn, ký ức, sự cô đơn, hay mất đi người khác.

[pause] Tiêu chí bốn: Chống lạm dụng. Nhân vật có thể dùng năng lực để gian lận mọi thứ không, hay luật đủ chặt để giữ căng thẳng.

[pause] Tiêu chí năm: Sức nặng cảm xúc. Luật chơi có khiến ta đau cùng nhân vật không, hay chỉ là một công cụ để đẩy cốt truyện.

[pause] Mỗi tiêu chí mười điểm, tổng năm mươi. Và Kaku nhắc lại: đây là chấm độ chặt của luật du hành, không phải chấm toàn bộ bộ truyện.
```

### c03 · Vòng 1: Luật có rõ không?

Khoảng 110 giây · cảnh s20–s28 · 1435 ký tự

**Gemini**

```text
Tokyo Revengers trước. Luật khá đơn giản: Takemichi bắt tay với Naoto, em trai của Hina, và cậu được đưa về đúng mười hai năm trước. Muốn quay về hiện tại, cậu lại bắt tay Naoto ở quá khứ.

<short pause> Thời gian ở quá khứ vẫn chạy song song. Nếu Takemichi ở quá khứ một tuần, thì khi về hiện tại cũng đã trôi qua một tuần.

<short pause> Luật này dễ hiểu, dễ nhớ. <short pause> Nhưng có một câu hỏi truyện không trả lời ngay: vì sao lại là mười hai năm, và vì sao lại là Takemichi. Đó là bí ẩn để dành cho sau này.

<short pause> Steins;Gate thì chi tiết tới mức gần như sách giáo khoa. Có hai cách: D-mail là gửi tin nhắn ngắn về quá khứ, và Time Leap là gửi ký ức của chính mình về quá khứ.

<short pause> Máy Time Leap đọc cấu trúc não, chuyển ký ức thành dữ liệu, rồi gửi về quá khứ bằng chính công nghệ D-mail. Và giới hạn là bốn mươi tám giờ.

<short pause> Vì sao là bốn mươi tám giờ? Truyện giải thích: não người thay đổi theo thời gian. Nhảy xa hơn thì ký ức mới không khớp với bộ não cũ, và có thể gây tổn thương nghiêm trọng.

<short pause> Re:Zero thì ngược lại. Luật cốt lõi rất rõ: chết thì quay về. <short pause> Nhưng điểm quay về ở đâu thì Subaru không được chọn, và cũng không biết trước.

<short pause> Điểm quay về thay đổi theo những thời khắc quan trọng của câu chuyện, và người ta cho rằng có một ý chí nào đó quyết định. Với Subaru, nó giống như một trò chơi không cho xem nút lưu.

<short pause> Điểm vòng một: Steins;Gate chín, vì mọi thứ đều có con số và lý do. Tokyo Revengers bảy, luật dễ hiểu nhưng thiếu lời giải thích. Re:Zero sáu, vì điểm lưu là một ẩn số.
```

**ElevenLabs**

```text
Tokyo Revengers trước. Luật khá đơn giản: Takemichi bắt tay với Naoto, em trai của Hina, và cậu được đưa về đúng mười hai năm trước. Muốn quay về hiện tại, cậu lại bắt tay Naoto ở quá khứ.

[pause] Thời gian ở quá khứ vẫn chạy song song. Nếu Takemichi ở quá khứ một tuần, thì khi về hiện tại cũng đã trôi qua một tuần.

[pause] Luật này dễ hiểu, dễ nhớ. [pause] Nhưng có một câu hỏi truyện không trả lời ngay: vì sao lại là mười hai năm, và vì sao lại là Takemichi. Đó là bí ẩn để dành cho sau này.

[pause] Steins;Gate thì chi tiết tới mức gần như sách giáo khoa. Có hai cách: D-mail là gửi tin nhắn ngắn về quá khứ, và Time Leap là gửi ký ức của chính mình về quá khứ.

[pause] Máy Time Leap đọc cấu trúc não, chuyển ký ức thành dữ liệu, rồi gửi về quá khứ bằng chính công nghệ D-mail. Và giới hạn là bốn mươi tám giờ.

[pause] [curious] Vì sao là bốn mươi tám giờ? Truyện giải thích: não người thay đổi theo thời gian. Nhảy xa hơn thì ký ức mới không khớp với bộ não cũ, và có thể gây tổn thương nghiêm trọng.

[pause] Re:Zero thì ngược lại. Luật cốt lõi rất rõ: chết thì quay về. [pause] Nhưng điểm quay về ở đâu thì Subaru không được chọn, và cũng không biết trước.

[pause] Điểm quay về thay đổi theo những thời khắc quan trọng của câu chuyện, và người ta cho rằng có một ý chí nào đó quyết định. Với Subaru, nó giống như một trò chơi không cho xem nút lưu.

[pause] Điểm vòng một: Steins;Gate chín, vì mọi thứ đều có con số và lý do. Tokyo Revengers bảy, luật dễ hiểu nhưng thiếu lời giải thích. Re:Zero sáu, vì điểm lưu là một ẩn số.
```

### c04 · Vòng 2: Có nhất quán không?

Khoảng 110 giây · cảnh s29–s37 · 1425 ký tự

**Gemini**

```text
Steins;Gate có một khái niệm rất đẹp: đường thế giới. Mỗi thay đổi trong quá khứ đẩy thế giới sang một đường khác, với một con số gọi là độ lệch.

<short pause> Nhiều đường thế giới gom lại thành một nhóm gọi là trường hút. Trong cùng một trường hút, có những sự kiện luôn xảy ra dù bạn làm gì. Truyện gọi đó là điểm hội tụ.

<short pause> Và đây là chỗ Steins;Gate tàn nhẫn nhất. Okabe cố cứu một người bạn thân, nhưng dù quay lại bao nhiêu lần, cô ấy vẫn chết vào đúng khoảng thời gian đó, chỉ bằng một cách khác.

<short pause> Luật này không bao giờ bị phá một cách dễ dãi. Muốn thoát khỏi điểm hội tụ, Okabe phải trả đúng cái giá mà luật yêu cầu. Kaku thấy đây là sự nhất quán hiếm có.

<short pause> Tokyo Revengers thì gặp nhiều tranh luận hơn. Người xem hay hỏi: nếu Naoto nhớ được mọi thứ vì được kể lại, vậy những người khác thì sao? Và vì sao một số thay đổi nhỏ lại tạo ra tương lai khác hẳn?

<short pause> Công bằng mà nói, Tokyo Revengers là truyện về băng nhóm và tình bạn. Cỗ máy thời gian là công cụ, không phải chủ đề chính, nên tác giả không cần giải thích từng chi tiết.

<short pause> Re:Zero giấu luật đi, nhưng không phá luật. Mỗi khi Subaru hiểu thêm một điều về năng lực, điều đó được giữ đúng ở những lần sau.

<short pause> <laugh> Kaku rất thích cách Re:Zero để người xem học luật cùng nhân vật. Ta không được đưa sách hướng dẫn, ta phải tự rút ra từ những lần thất bại.

<short pause> Điểm vòng hai: Steins;Gate mười, Re:Zero tám, Tokyo Revengers sáu. Sau hai vòng: Steins;Gate mười chín, Re:Zero mười bốn, Tokyo Revengers mười ba.
```

**ElevenLabs**

```text
Steins;Gate có một khái niệm rất đẹp: đường thế giới. Mỗi thay đổi trong quá khứ đẩy thế giới sang một đường khác, với một con số gọi là độ lệch.

[pause] Nhiều đường thế giới gom lại thành một nhóm gọi là trường hút. Trong cùng một trường hút, có những sự kiện luôn xảy ra dù bạn làm gì. Truyện gọi đó là điểm hội tụ.

[pause] Và đây là chỗ Steins;Gate tàn nhẫn nhất. Okabe cố cứu một người bạn thân, nhưng dù quay lại bao nhiêu lần, cô ấy vẫn chết vào đúng khoảng thời gian đó, chỉ bằng một cách khác.

[pause] Luật này không bao giờ bị phá một cách dễ dãi. Muốn thoát khỏi điểm hội tụ, Okabe phải trả đúng cái giá mà luật yêu cầu. Kaku thấy đây là sự nhất quán hiếm có.

[pause] Tokyo Revengers thì gặp nhiều tranh luận hơn. [curious] Người xem hay hỏi: nếu Naoto nhớ được mọi thứ vì được kể lại, vậy những người khác thì sao? Và vì sao một số thay đổi nhỏ lại tạo ra tương lai khác hẳn?

[pause] Công bằng mà nói, Tokyo Revengers là truyện về băng nhóm và tình bạn. Cỗ máy thời gian là công cụ, không phải chủ đề chính, nên tác giả không cần giải thích từng chi tiết.

[pause] Re:Zero giấu luật đi, nhưng không phá luật. Mỗi khi Subaru hiểu thêm một điều về năng lực, điều đó được giữ đúng ở những lần sau.

[pause] [chuckles] Kaku rất thích cách Re:Zero để người xem học luật cùng nhân vật. Ta không được đưa sách hướng dẫn, ta phải tự rút ra từ những lần thất bại.

[pause] Điểm vòng hai: Steins;Gate mười, Re:Zero tám, Tokyo Revengers sáu. Sau hai vòng: Steins;Gate mười chín, Re:Zero mười bốn, Tokyo Revengers mười ba.
```

### c05 · Vòng 3: Cái giá

Khoảng 105 giây · cảnh s38–s46 · 1363 ký tự

**Gemini**

```text
Giờ tới câu hỏi Kaku thích nhất: mỗi lần quay lại, người du hành phải trả gì?

<short pause> Takemichi phải chiến đấu trong quá khứ với cơ thể của một học sinh yếu ớt. Cậu bị đánh rất nhiều. Và mỗi lần về hiện tại, cậu có thể thấy một bi kịch mới thay cho bi kịch cũ.

<short pause> Cái giá lớn nhất là cô đơn. Takemichi mang ký ức của những dòng thời gian mà không ai khác nhớ. Người duy nhất cậu có thể tâm sự là Naoto.

<short pause> Okabe có một năng lực riêng gọi là Reading Steiner: khi thế giới đổi sang đường khác, chỉ cậu nhớ đường cũ. Nghe thì như lợi thế, nhưng thật ra là một lời nguyền.

<short pause> Để thoát khỏi điểm hội tụ, Okabe phải xóa từng tin nhắn đã gửi về quá khứ. Mà mỗi tin nhắn đó là điều ước của một người bạn. Cứu một người, cậu phải lấy lại hạnh phúc của những người khác.

<short pause> Subaru thì trả giá bằng chính cơ thể. Cậu phải thật sự chết, cảm nhận đau đớn, rồi tỉnh lại như chưa có gì. Mỗi lần như vậy để lại vết thương trong tâm trí.

<short pause> Và có một luật khiến cái giá đó nặng gấp đôi: Subaru không thể kể cho bất kỳ ai về năng lực. Hễ cậu định nói, thời gian dừng lại, và một bàn tay đen siết lấy trái tim cậu.

<short pause> Nghĩa là Subaru phải chịu đựng tất cả một mình, và bị người khác hiểu lầm vì những hành động mà họ không thể hiểu.

<short pause> Điểm vòng ba: Re:Zero mười, vì không cái giá nào đau hơn. Steins;Gate chín. Tokyo Revengers bảy. Sau ba vòng: Steins;Gate hai mươi tám, Re:Zero hai mươi bốn, Tokyo Revengers hai mươi.
```

**ElevenLabs**

```text
[curious] Giờ tới câu hỏi Kaku thích nhất: mỗi lần quay lại, người du hành phải trả gì?

[pause] Takemichi phải chiến đấu trong quá khứ với cơ thể của một học sinh yếu ớt. Cậu bị đánh rất nhiều. Và mỗi lần về hiện tại, cậu có thể thấy một bi kịch mới thay cho bi kịch cũ.

[pause] Cái giá lớn nhất là cô đơn. Takemichi mang ký ức của những dòng thời gian mà không ai khác nhớ. Người duy nhất cậu có thể tâm sự là Naoto.

[pause] Okabe có một năng lực riêng gọi là Reading Steiner: khi thế giới đổi sang đường khác, chỉ cậu nhớ đường cũ. Nghe thì như lợi thế, nhưng thật ra là một lời nguyền.

[pause] Để thoát khỏi điểm hội tụ, Okabe phải xóa từng tin nhắn đã gửi về quá khứ. Mà mỗi tin nhắn đó là điều ước của một người bạn. Cứu một người, cậu phải lấy lại hạnh phúc của những người khác.

[pause] Subaru thì trả giá bằng chính cơ thể. Cậu phải thật sự chết, cảm nhận đau đớn, rồi tỉnh lại như chưa có gì. Mỗi lần như vậy để lại vết thương trong tâm trí.

[pause] Và có một luật khiến cái giá đó nặng gấp đôi: Subaru không thể kể cho bất kỳ ai về năng lực. Hễ cậu định nói, thời gian dừng lại, và một bàn tay đen siết lấy trái tim cậu.

[pause] Nghĩa là Subaru phải chịu đựng tất cả một mình, và bị người khác hiểu lầm vì những hành động mà họ không thể hiểu.

[pause] Điểm vòng ba: Re:Zero mười, vì không cái giá nào đau hơn. Steins;Gate chín. Tokyo Revengers bảy. Sau ba vòng: Steins;Gate hai mươi tám, Re:Zero hai mươi bốn, Tokyo Revengers hai mươi.
```

### c06 · Vòng 4: Chống lạm dụng

Khoảng 81 giây · cảnh s47–s53 · 1056 ký tự

**Gemini**

```text
Một năng lực du hành thời gian tốt phải có giới hạn. Nếu không, nhân vật chỉ cần quay lại mãi cho tới khi mọi thứ hoàn hảo, và câu chuyện mất hết căng thẳng.

<short pause> Takemichi không chọn được thời điểm. Luôn là mười hai năm. Cậu cũng cần Naoto ở cả hai đầu. Nếu Naoto không có mặt, cậu mắc kẹt.

<short pause> Okabe bị giới hạn bởi bốn mươi tám giờ, bởi chiếc máy có thể hỏng, và bởi một tổ chức bí ẩn luôn theo dõi. Mỗi lần nhảy còn phải chạy đua với thời gian thật.

<short pause> Subaru bị giới hạn theo cách đáng sợ nhất. Cậu không chọn được điểm lưu. Nếu điểm lưu rơi vào một tình huống không lối thoát, cậu có thể bị kẹt trong vòng lặp.

<short pause> Cậu cũng không được chia sẻ thông tin. Biết tương lai mà không được nói ra, Subaru phải tìm cách thuyết phục người khác bằng những lý do mà cậu không thể giải thích.

<short pause> <laugh> Kaku thấy cả ba đều khá chặt ở vòng này. <short pause> Nhưng Steins;Gate và Re:Zero có thêm lớp khóa: một bên là luật vật lý, một bên là lời nguyền.

<short pause> Điểm vòng bốn: Steins;Gate chín, Re:Zero chín, Tokyo Revengers tám. Sau bốn vòng: Steins;Gate ba mươi bảy, Re:Zero ba mươi ba, Tokyo Revengers hai mươi tám.
```

**ElevenLabs**

```text
Một năng lực du hành thời gian tốt phải có giới hạn. Nếu không, nhân vật chỉ cần quay lại mãi cho tới khi mọi thứ hoàn hảo, và câu chuyện mất hết căng thẳng.

[pause] Takemichi không chọn được thời điểm. Luôn là mười hai năm. Cậu cũng cần Naoto ở cả hai đầu. Nếu Naoto không có mặt, cậu mắc kẹt.

[pause] Okabe bị giới hạn bởi bốn mươi tám giờ, bởi chiếc máy có thể hỏng, và bởi một tổ chức bí ẩn luôn theo dõi. Mỗi lần nhảy còn phải chạy đua với thời gian thật.

[pause] Subaru bị giới hạn theo cách đáng sợ nhất. Cậu không chọn được điểm lưu. Nếu điểm lưu rơi vào một tình huống không lối thoát, cậu có thể bị kẹt trong vòng lặp.

[pause] Cậu cũng không được chia sẻ thông tin. Biết tương lai mà không được nói ra, Subaru phải tìm cách thuyết phục người khác bằng những lý do mà cậu không thể giải thích.

[pause] [chuckles] Kaku thấy cả ba đều khá chặt ở vòng này. [pause] Nhưng Steins;Gate và Re:Zero có thêm lớp khóa: một bên là luật vật lý, một bên là lời nguyền.

[pause] Điểm vòng bốn: Steins;Gate chín, Re:Zero chín, Tokyo Revengers tám. Sau bốn vòng: Steins;Gate ba mươi bảy, Re:Zero ba mươi ba, Tokyo Revengers hai mươi tám.
```

### c07 · Vòng 5: Sức nặng cảm xúc / Thử thách phụ: cứu chiếc bánh sinh nhật

Khoảng 143 giây · cảnh s54–s65 · 1858 ký tự

**Gemini**

```text
Vòng cuối không đo luật mà đo trái tim: luật chơi có khiến ta đau cùng nhân vật không.

<short pause> Takemichi được gọi là anh hùng hay khóc. Cậu không mạnh, không thông minh, nhưng không bao giờ bỏ cuộc. Mỗi lần quay lại là một lần cậu chọn đứng dậy.

<short pause> Okabe bắt đầu truyện với vai diễn nhà khoa học điên, cười lớn, nói những câu kỳ quặc. Càng quay lại nhiều lần, lớp vỏ đó càng vỡ, và ta thấy một người trẻ kiệt sức.

<short pause> Những tập giữa Steins;Gate, khi Okabe nhảy lại cùng một ngày hết lần này tới lần khác, được nhiều người xem nhớ mãi. Không có cảnh đánh nhau, chỉ có một người không chịu buông tay.

<short pause> Subaru thì có lẽ là nhân vật được xem suy sụp rõ nhất trong ba người. Có những lúc cậu muốn bỏ cuộc, và Re:Zero không né tránh những khoảnh khắc đó.

<short pause> Cảnh một người bạn nói với Subaru rằng hãy bắt đầu lại từ số không, cùng nhau, là một trong những cảnh nổi tiếng nhất của isekai hiện đại. Nó cho thấy cái giá của năng lực chỉ được chữa lành bằng người khác.

<short pause> Điểm vòng năm: Steins;Gate mười, Re:Zero mười, Tokyo Revengers tám. Hai bộ đầu hòa nhau ở vòng này, vì cả hai đều khiến người xem đau thật sự.

<short pause> Trước khi công bố kết quả, Kaku cho ba nhà du hành một thử thách vui. Ba giờ chiều nay, bạn làm rơi chiếc bánh sinh nhật xuống sàn. Ai cứu được chiếc bánh?

<short pause> Takemichi: bắt tay Naoto, và thế là cậu về mười hai năm trước. Chiếc bánh còn chưa được làm. Cậu phải chờ mười hai năm. Thất bại.

<short pause> Okabe: gửi một D-mail về trưa nay: nhớ cầm bánh bằng hai tay. Chiếc bánh được cứu. <short pause> Nhưng đường thế giới lệch đi một chút, và có khi tiệm bánh quen giờ đã biến mất.

<short pause> Subaru: cậu không chọn được lúc quay lại, và Kaku không bao giờ khuyên ai liều mạng vì một chiếc bánh. Subaru chỉ còn cách mua bánh mới. <short pause> Nhưng cậu sẽ là người lau sàn nhanh nhất.

<short pause> Kết quả thử thách phụ: Steins;Gate thắng. <laugh> Và đây chính là lý do Kaku nói luật của Steins;Gate chặt nhất: nó cho kết quả rõ ràng, và cả tác dụng phụ rõ ràng.
```

**ElevenLabs**

```text
Vòng cuối không đo luật mà đo trái tim: luật chơi có khiến ta đau cùng nhân vật không.

[pause] Takemichi được gọi là anh hùng hay khóc. Cậu không mạnh, không thông minh, nhưng không bao giờ bỏ cuộc. Mỗi lần quay lại là một lần cậu chọn đứng dậy.

[pause] Okabe bắt đầu truyện với vai diễn nhà khoa học điên, cười lớn, nói những câu kỳ quặc. Càng quay lại nhiều lần, lớp vỏ đó càng vỡ, và ta thấy một người trẻ kiệt sức.

[pause] Những tập giữa Steins;Gate, khi Okabe nhảy lại cùng một ngày hết lần này tới lần khác, được nhiều người xem nhớ mãi. Không có cảnh đánh nhau, chỉ có một người không chịu buông tay.

[pause] Subaru thì có lẽ là nhân vật được xem suy sụp rõ nhất trong ba người. Có những lúc cậu muốn bỏ cuộc, và Re:Zero không né tránh những khoảnh khắc đó.

[pause] Cảnh một người bạn nói với Subaru rằng hãy bắt đầu lại từ số không, cùng nhau, là một trong những cảnh nổi tiếng nhất của isekai hiện đại. Nó cho thấy cái giá của năng lực chỉ được chữa lành bằng người khác.

[pause] Điểm vòng năm: Steins;Gate mười, Re:Zero mười, Tokyo Revengers tám. Hai bộ đầu hòa nhau ở vòng này, vì cả hai đều khiến người xem đau thật sự.

[pause] Trước khi công bố kết quả, Kaku cho ba nhà du hành một thử thách vui. Ba giờ chiều nay, bạn làm rơi chiếc bánh sinh nhật xuống sàn. [curious] Ai cứu được chiếc bánh?

[pause] Takemichi: bắt tay Naoto, và thế là cậu về mười hai năm trước. Chiếc bánh còn chưa được làm. Cậu phải chờ mười hai năm. Thất bại.

[pause] Okabe: gửi một D-mail về trưa nay: nhớ cầm bánh bằng hai tay. Chiếc bánh được cứu. [pause] Nhưng đường thế giới lệch đi một chút, và có khi tiệm bánh quen giờ đã biến mất.

[pause] Subaru: cậu không chọn được lúc quay lại, và Kaku không bao giờ khuyên ai liều mạng vì một chiếc bánh. Subaru chỉ còn cách mua bánh mới. [pause] Nhưng cậu sẽ là người lau sàn nhanh nhất.

[pause] Kết quả thử thách phụ: Steins;Gate thắng. [chuckles] Và đây chính là lý do Kaku nói luật của Steins;Gate chặt nhất: nó cho kết quả rõ ràng, và cả tác dụng phụ rõ ràng.
```

### c08 · Kết quả chung cuộc / Giải thưởng phụ

Khoảng 128 giây · cảnh s66–s77 · 1667 ký tự

**Gemini**

```text
Và đây là bảng điểm chung cuộc. Tokyo Revengers: bảy, sáu, bảy, tám, tám. Tổng ba mươi sáu trên năm mươi.

<short pause> Re:Zero: sáu, tám, mười, chín, mười. Tổng bốn mươi ba trên năm mươi.

<short pause> Steins;Gate: chín, mười, chín, chín, mười. Tổng bốn mươi bảy trên năm mươi. Người chiến thắng về độ chặt của luật du hành thời gian.

<short pause> Steins;Gate thắng vì nó xem du hành thời gian là khoa học: có con số, có giới hạn, có hậu quả. Mọi bi kịch đều đến từ chính luật mà truyện đặt ra từ đầu.

<short pause> Re:Zero đứng thứ hai vì nó xem du hành thời gian là lời nguyền: luật giấu kín, cái giá tàn nhẫn, và cô đơn tuyệt đối.

<short pause> Tokyo Revengers đứng thứ ba, nhưng Kaku muốn nói rõ: đây không phải bộ kém. Nó xem du hành thời gian là một cơ hội thứ hai, và điều nó quan tâm là tình bạn, không phải vật lý.

<short pause> Nếu bạn muốn một câu đố logic, hãy xem Steins;Gate. Nếu bạn muốn một hành trình đau đớn, hãy xem Re:Zero. Nếu bạn muốn một câu chuyện về lòng trung thành, hãy xem Tokyo Revengers.

<short pause> Kaku trao thêm ba giải phụ. Giải Luật dễ hiểu nhất: Tokyo Revengers. Một cái bắt tay, mười hai năm, ai cũng nhớ được sau năm phút xem.

<short pause> Giải Cái giá đau nhất: Re:Zero. Không bộ nào bắt nhân vật chính trả giá bằng chính mình nhiều như vậy.

<short pause> Giải Gắn với đời thật nhất: Steins;Gate. Truyện lấy cảm hứng từ John Titor, một người từng đăng bài trên mạng khoảng năm 2000, tự xưng là người du hành từ năm 2036. Đó là một truyền thuyết internet, không phải sự thật.

<short pause> Trong truyện còn có một chiếc máy tính cổ tên là IBN 5100, lấy cảm hứng từ máy IBM 5100 có thật, ra đời năm 1975. Kaku thích những chi tiết như vậy vì nó làm câu chuyện đáng tin hơn.

<short pause> <laugh> Kaku cũng tặng một giải cho chính mình: Trọng tài chấm điểm công bằng nhất. Không ai phản đối đâu nhỉ?
```

**ElevenLabs**

```text
Và đây là bảng điểm chung cuộc. Tokyo Revengers: bảy, sáu, bảy, tám, tám. Tổng ba mươi sáu trên năm mươi.

[pause] Re:Zero: sáu, tám, mười, chín, mười. Tổng bốn mươi ba trên năm mươi.

[pause] Steins;Gate: chín, mười, chín, chín, mười. Tổng bốn mươi bảy trên năm mươi. Người chiến thắng về độ chặt của luật du hành thời gian.

[pause] Steins;Gate thắng vì nó xem du hành thời gian là khoa học: có con số, có giới hạn, có hậu quả. Mọi bi kịch đều đến từ chính luật mà truyện đặt ra từ đầu.

[pause] Re:Zero đứng thứ hai vì nó xem du hành thời gian là lời nguyền: luật giấu kín, cái giá tàn nhẫn, và cô đơn tuyệt đối.

[pause] Tokyo Revengers đứng thứ ba, nhưng Kaku muốn nói rõ: đây không phải bộ kém. Nó xem du hành thời gian là một cơ hội thứ hai, và điều nó quan tâm là tình bạn, không phải vật lý.

[pause] Nếu bạn muốn một câu đố logic, hãy xem Steins;Gate. Nếu bạn muốn một hành trình đau đớn, hãy xem Re:Zero. Nếu bạn muốn một câu chuyện về lòng trung thành, hãy xem Tokyo Revengers.

[pause] Kaku trao thêm ba giải phụ. Giải Luật dễ hiểu nhất: Tokyo Revengers. Một cái bắt tay, mười hai năm, ai cũng nhớ được sau năm phút xem.

[pause] Giải Cái giá đau nhất: Re:Zero. Không bộ nào bắt nhân vật chính trả giá bằng chính mình nhiều như vậy.

[pause] Giải Gắn với đời thật nhất: Steins;Gate. Truyện lấy cảm hứng từ John Titor, một người từng đăng bài trên mạng khoảng năm 2000, tự xưng là người du hành từ năm 2036. Đó là một truyền thuyết internet, không phải sự thật.

[pause] Trong truyện còn có một chiếc máy tính cổ tên là IBN 5100, lấy cảm hứng từ máy IBM 5100 có thật, ra đời năm 1975. Kaku thích những chi tiết như vậy vì nó làm câu chuyện đáng tin hơn.

[pause] [chuckles] Kaku cũng tặng một giải cho chính mình: Trọng tài chấm điểm công bằng nhất. [curious] Không ai phản đối đâu nhỉ?
```

### c09 · Một bí mật hậu trường / Nếu bạn có một lần quay lại / Kết

Khoảng 116 giây · cảnh s78–s89 · 1506 ký tự

**Gemini**

```text
Có một chi tiết thú vị: anime Steins;Gate năm 2011 và anime Re:Zero năm 2016 đều do cùng một studio thực hiện, là White Fox.

<short pause> Nhiều người xem nhận ra hai bộ có không khí giống nhau: nhịp chậm lúc đầu, rồi đột ngột trở nên nặng nề, và những cảnh vòng lặp đầy ám ảnh.

<short pause> Nếu bạn đã xem một trong hai bộ và thích, bộ còn lại gần như chắc chắn hợp với bạn.

<short pause> Giờ tới lượt bạn. Nếu được chọn một trong ba năng lực, bạn chọn cái nào?

<short pause> Bắt tay để về đúng mười hai năm trước, sửa những gì bạn tiếc nuối từ thời đi học. Hoặc gửi tin nhắn về hai ngày trước, sửa một sai lầm nhỏ nhưng chấp nhận thế giới đổi khác.

<short pause> Hoặc quay về mỗi khi thất bại, không giới hạn số lần, nhưng không bao giờ được kể cho ai biết bạn đã trải qua những gì.

<short pause> <laugh> Kaku chọn tin nhắn, vì Kaku chỉ cần sửa câu nói sai trong video trước. Viết lựa chọn của bạn vào bình luận, kèm lý do.

<short pause> Và nếu bạn không đồng ý với bảng điểm, hãy viết bảng điểm của bạn. Kaku sẽ đọc hết và làm một video trả lời những bảng điểm khác biệt nhất.

<short pause> Ba nhà du hành, ba cỗ máy, và cùng một bài học: quay lại quá khứ không làm mọi thứ dễ hơn. Nó chỉ cho bạn thêm một lần để chọn lại, và thêm một lần để đau.

<short pause> Có lẽ vì vậy mà cả ba bộ đều kết luận giống nhau: điều cứu nhân vật không phải cỗ máy, mà là những người đã ở bên họ.

<short pause> Video tiếp theo, Kaku mở dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ khi Muzan trở thành quỷ tới ngày Tanjiro cầm kiếm.

<short pause> Nếu bạn thích xem Kaku làm trọng tài, hãy đăng ký kênh. Không cần quay ngược thời gian, chỉ cần một cái bấm. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Có một chi tiết thú vị: anime Steins;Gate năm 2011 và anime Re:Zero năm 2016 đều do cùng một studio thực hiện, là White Fox.

[pause] Nhiều người xem nhận ra hai bộ có không khí giống nhau: nhịp chậm lúc đầu, rồi đột ngột trở nên nặng nề, và những cảnh vòng lặp đầy ám ảnh.

[pause] Nếu bạn đã xem một trong hai bộ và thích, bộ còn lại gần như chắc chắn hợp với bạn.

[pause] Giờ tới lượt bạn. [curious] Nếu được chọn một trong ba năng lực, bạn chọn cái nào?

[pause] Bắt tay để về đúng mười hai năm trước, sửa những gì bạn tiếc nuối từ thời đi học. Hoặc gửi tin nhắn về hai ngày trước, sửa một sai lầm nhỏ nhưng chấp nhận thế giới đổi khác.

[pause] Hoặc quay về mỗi khi thất bại, không giới hạn số lần, nhưng không bao giờ được kể cho ai biết bạn đã trải qua những gì.

[pause] [chuckles] Kaku chọn tin nhắn, vì Kaku chỉ cần sửa câu nói sai trong video trước. Viết lựa chọn của bạn vào bình luận, kèm lý do.

[pause] Và nếu bạn không đồng ý với bảng điểm, hãy viết bảng điểm của bạn. Kaku sẽ đọc hết và làm một video trả lời những bảng điểm khác biệt nhất.

[pause] Ba nhà du hành, ba cỗ máy, và cùng một bài học: quay lại quá khứ không làm mọi thứ dễ hơn. Nó chỉ cho bạn thêm một lần để chọn lại, và thêm một lần để đau.

[pause] Có lẽ vì vậy mà cả ba bộ đều kết luận giống nhau: điều cứu nhân vật không phải cỗ máy, mà là những người đã ở bên họ.

[pause] Video tiếp theo, Kaku mở dòng thời gian một nghìn năm của Kimetsu no Yaiba, từ khi Muzan trở thành quỷ tới ngày Tanjiro cầm kiếm.

[pause] Nếu bạn thích xem Kaku làm trọng tài, hãy đăng ký kênh. Không cần quay ngược thời gian, chỉ cần một cái bấm. Kaku gấp sổ đây, hẹn gặp lại!
```
