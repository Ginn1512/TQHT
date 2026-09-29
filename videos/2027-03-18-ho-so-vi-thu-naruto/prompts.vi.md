# Bộ prompt · Naruto: Hồ sơ 9 Vĩ thú — tên, sức mạnh và nhân trụ lực

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 91 ảnh, 7 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (91 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo spoiler: video này nói tới hết Naruto Shippuden, kể cả nguồn gốc của Vĩ thú trong Đại chiến ninja lầ…

```text
Wide 16:9 landscape cinematic frame. a thick case file with nine colored tabs sticking out, resting on a wooden desk beside a spoiler card, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Hồ sơ số chín. Loài: cáo khổng lồ. Số đuôi: chín. Sức mạnh: đủ để san phẳng một ngôi làng. Nhân trụ lực hiện…

```text
Wide 16:9 landscape cinematic frame. an official-looking dossier card with a large paw print and nine tally marks, stamped with a red seal, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Trong thế giới Naruto có chín sinh vật khổng lồ, mỗi con mang một lượng chakra khổng lồ, gọi là Vĩ thú. Người…

```text
Wide 16:9 landscape cinematic frame. nine enormous animal silhouettes standing on distant mountains under a dramatic sky, wide shot, epic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng ít ai hỏi: Vĩ thú muốn gì? Chúng có tên không? Và vì sao chúng ghét con người?

```text
Wide 16:9 landscape cinematic frame. a single large eye glowing in the darkness of a cave, close-up, mysterious light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku mở chín hồ sơ Vĩ thú. Mỗi hồ sơ có năm dòng: tên, hình dạng, sức mạn…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing tiny reading glasses flipping open the first of nine folders. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06 · Nguồn gốc: Thập Vĩ

Lời: Trước khi có chín Vĩ thú, chỉ có một sinh vật: Thập Vĩ, con quái vật mười đuôi, gắn với một cây thần cổ xưa.

```text
Wide 16:9 landscape cinematic frame. a colossal ten-tailed silhouette looming over an ancient barren landscape with a giant tree in the distance, wide shot, ominous red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07

Lời: Lục Đạo Tiên Nhân, Otsutsuki Hagoromo, đánh bại Thập Vĩ và phong ấn nó vào chính cơ thể mình. Ông trở thành n…

```text
Wide 16:9 landscape cinematic frame. a robed sage silhouette standing calmly as swirling energy is drawn into his body, symbolic wide shot, radiant light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Trước khi chết, ông chia chakra của Thập Vĩ thành chín phần, tạo ra chín Vĩ thú. Và ông đặt cho mỗi con một c…

```text
Wide 16:9 landscape cinematic frame. a single large flame splitting into nine smaller flames floating in a circle, symbolic close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09

Lời: Hagoromo coi chúng như con của mình. Ông nói với chúng rằng một ngày nào đó sẽ có người hiểu chúng. Lời hứa đ…

```text
Wide 16:9 landscape cinematic frame. an old sage sitting on a rock surrounded by nine small animal silhouettes listening to him, wide shot, gentle sunset light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Kaku để ý: con người trong truyện gần như không ai biết Vĩ thú có tên. Họ gọi chúng bằng số đuôi, như gọi một…

```text
Wide 16:9 landscape cinematic frame. a row of labels with numbers one to nine stuck over crossed-out names, close-up, cold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11 · Luật: nhân trụ lực và cân bằng quyền lực

Lời: Về sau, Hashirama, Hokage đệ nhất, bắt giữ nhiều Vĩ thú và chia chúng cho các làng ninja lớn để giữ cân bằng…

```text
Wide 16:9 landscape cinematic frame. a large map with five village symbols and small beast icons distributed among them, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Để kiểm soát Vĩ thú, các làng phong ấn chúng vào cơ thể con người. Người đó gọi là nhân trụ lực.

```text
Wide 16:9 landscape cinematic frame. a glowing seal pattern drawn on a stone floor with a small figure standing at its center, overhead shot, mystical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Nhân trụ lực có thể mượn chakra của Vĩ thú. Nhưng họ thường bị cả làng sợ hãi, xa lánh, như thể chính họ là c…

```text
Wide 16:9 landscape cinematic frame. a lonely child sitting on a swing in an empty playground at dusk while other children walk away, wide shot, melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Và nếu Vĩ thú bị rút ra khỏi cơ thể, nhân trụ lực thường không sống sót. Đó là lý do tổ chức Akatsuki săn lùn…

```text
Wide 16:9 landscape cinematic frame. a black cloak with a red cloud pattern hanging in a dark cave entrance, close-up, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15 · Sức mạnh chung của Vĩ thú

Lời: Trước khi mở từng hồ sơ, Kaku ghi những sức mạnh mà Vĩ thú nào cũng có. Một: lượng chakra khổng lồ, càng nhiề…

```text
Wide 16:9 landscape cinematic frame. a row of nine glowing orbs of increasing size on a dark table, close-up, dramatic warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Hai: Vĩ thú ngọc, một khối cầu chakra nén cực mạnh, bắn ra có thể phá hủy cả một vùng rộng lớn.

```text
Wide 16:9 landscape cinematic frame. a dense sphere of dark energy with swirling light at its core hovering in the air above a landscape, dramatic close-up, intense light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17

Lời: Ba: nhân trụ lực có thể biến hình theo nhiều cấp: mọc một vài đuôi bằng chakra, khoác áo chakra, rồi hóa thàn…

```text
Wide 16:9 landscape cinematic frame. three silhouette sketches side by side showing a figure with a faint aura, a figure with energy tails, and a giant beast shape, parchment close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18

Lời: Và người kiểm soát được Vĩ thú hoàn toàn, hợp tác thay vì bị chiếm lấy, được gọi là nhân trụ lực hoàn hảo. Rấ…

```text
Wide 16:9 landscape cinematic frame. a figure standing calmly with a massive gentle shadow behind them, both looking in the same direction, symbolic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19 · Những nhân trụ lực trước Naruto

Lời: Naruto không phải nhân trụ lực đầu tiên của Cửu Vĩ. Người đầu tiên là Uzumaki Mito, vợ của Hokage đệ nhất Has…

```text
Wide 16:9 landscape cinematic frame. an elegant woman's silhouette standing in a traditional garden with a faint seal pattern glowing on the ground, wide shot, soft historical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Người thứ hai là Uzumaki Kushina, mẹ của Naruto. Tộc Uzumaki có sinh lực và chakra đặc biệt mạnh, nên thích h…

```text
Wide 16:9 landscape cinematic frame. a woman with a gentle smile holding a newborn wrapped in a blanket, medium shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Đêm Naruto chào đời, Cửu Vĩ bị giải phóng khỏi Kushina và tấn công làng. Cha mẹ Naruto hy sinh để phong ấn nó…

```text
Wide 16:9 landscape cinematic frame. a night sky over a village glowing orange with a colossal silhouette in the distance, two small figures standing protectively over a cradle, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: ba đời nhân trụ lực Cửu Vĩ đều là tộc Uzumaki. Cửu Vĩ gần như là một phần lịch sử gia đình của Nar…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at a small family tree with three names circled and a fox doodle beside them. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23 · Hồ sơ 1: Shukaku, Nhất Vĩ

Lời: Hồ sơ số một: Shukaku, Nhất Vĩ. Hình dạng: một con lửng chó khổng lồ, thân làm bằng cát, có hoa văn trên ngườ…

```text
Wide 16:9 landscape cinematic frame. a giant raccoon-dog shaped silhouette formed from swirling desert sand, low-angle shot, harsh sunlight. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Sức mạnh: điều khiển cát, và phong ấn phép thuật. Tính cách: hung hăng, ồn ào, thích gây sự.

```text
Wide 16:9 landscape cinematic frame. a massive wave of sand rising from the desert and curling like a hand, dynamic wide shot, golden dusty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25

Lời: Cha của Gaara, Kazekage, đã cố tình phong ấn Shukaku vào con mình trước khi sinh, để tạo ra vũ khí cho làng.…

```text
Wide 16:9 landscape cinematic frame. a lonely child standing in a desert courtyard while adults watch coldly from a balcony above, wide shot, harsh bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Nhân trụ lực: Gaara, làng Cát. Gaara từng là một đứa trẻ cô độc, không ngủ được vì sợ Shukaku chiếm lấy cơ th…

```text
Wide 16:9 landscape cinematic frame. a small boy sitting alone on a rooftop at night staring at a full moon over a desert village, back view, wide shot, cold blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Sau khi gặp Naruto, Gaara thay đổi và trở thành Kazekage. Nhất Vĩ là con Vĩ thú đầu tiên cho thấy nhân trụ lự…

```text
Wide 16:9 landscape cinematic frame. a young leader standing on a balcony above a desert village as crowds cheer below, wide shot, warm sunrise light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Mức nguy hiểm: trung bình. Mức bị hiểu lầm: rất cao.

```text
Wide 16:9 landscape cinematic frame. a small dossier stamp with a medium danger rating beside a heart icon, close-up, amber ink. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29 · Hồ sơ 2: Matatabi, Nhị Vĩ

Lời: Hồ sơ số hai: Matatabi, Nhị Vĩ. Hình dạng: một con mèo khổng lồ phủ ngọn lửa xanh.

```text
Wide 16:9 landscape cinematic frame. a giant cat silhouette wreathed in flickering blue flames on a dark hilltop, low-angle shot, eerie blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Trong văn hóa Nhật, mèo có hai đuôi gợi tới yêu quái mèo trong truyện dân gian. Matatabi cũng là tên một loài…

```text
Wide 16:9 landscape cinematic frame. an old Japanese folk tale illustration of a mysterious two-tailed cat sitting under a lantern, parchment close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Sức mạnh: lửa xanh, và sự nhanh nhẹn của loài mèo. Tính cách: điềm tĩnh, lịch sự hơn nhiều Vĩ thú khác.

```text
Wide 16:9 landscape cinematic frame. a trail of blue fire streaking across a rocky landscape at night, dynamic wide shot, cool blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32

Lời: Nhân trụ lực: Yugito Nii, làng Mây. Cô là một trong những nhân trụ lực kiểm soát Vĩ thú tốt nhất, nhưng vẫn b…

```text
Wide 16:9 landscape cinematic frame. a lone figure standing in a moonlit clearing with faint blue flames around her feet, medium shot, cool dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33

Lời: Anime và các phần phụ sau này có kể thêm về vài nhân trụ lực này, nhưng phần lớn chỉ là những lát cắt ngắn. N…

```text
Wide 16:9 landscape cinematic frame. a small row of name tags pinned to a board, some with short notes and some blank, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Kaku để ý: nhiều nhân trụ lực như Yugito chỉ xuất hiện rất ít trong truyện. Họ là những câu chuyện chưa được…

```text
Wide 16:9 landscape cinematic frame. a half-written notebook page with a faded name at the top and mostly empty lines, close-up, soft melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35 · Hồ sơ 3: Isobu, Tam Vĩ

Lời: Hồ sơ số ba: Isobu, Tam Vĩ. Hình dạng: một con rùa khổng lồ với lớp vỏ gai nhọn như san hô.

```text
Wide 16:9 landscape cinematic frame. a giant turtle silhouette with a spiked coral-like shell emerging from a misty lake, wide shot, cool grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Rùa là biểu tượng của sự phòng thủ và tuổi thọ. Isobu không muốn đánh nhau, nó chỉ muốn được để yên dưới đáy…

```text
Wide 16:9 landscape cinematic frame. a large turtle shell resting peacefully at the bottom of a clear lake with fish swimming around it, close-up, calm teal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Sức mạnh: phòng thủ cực mạnh, và tạo sương mù, san hô. Tính cách: nhút nhát, không thích đánh nhau.

```text
Wide 16:9 landscape cinematic frame. coral spikes growing rapidly out of dark water under heavy fog, close-up, eerie teal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Nhân trụ lực: Yagura, Mizukage của làng Sương mù, từng bị thao túng. Và trong quá khứ, Tam Vĩ còn từng bị pho…

```text
Wide 16:9 landscape cinematic frame. a misty village of stilted houses over water with a single boat drifting, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Kaku ghi thêm: Tam Vĩ là Vĩ thú bị bắt dễ dàng nhất trong cuộc săn của Akatsuki, vì lúc đó nó không có nhân t…

```text
Wide 16:9 landscape cinematic frame. a quiet lake with ripples spreading from a disturbance at its center under a grey sky, wide shot, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Tam Vĩ là Vĩ thú từng không có nhân trụ lực trong một thời gian, sống tự do trong hồ. Một hồ sơ nhiều khoảng…

```text
Wide 16:9 landscape cinematic frame. a calm lake at dawn with a large shadow faintly visible beneath the surface, wide shot, soft pale light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Hồ sơ 4 và 5: Son Goku và Kokuo

Lời: Hồ sơ số bốn: Son Goku, Tứ Vĩ. Hình dạng: một con khỉ đột khổng lồ. Sức mạnh: dung nham. Tên của nó lấy cảm h…

```text
Wide 16:9 landscape cinematic frame. a giant ape silhouette standing among glowing lava flows on a volcanic mountain, low-angle shot, fiery red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Roshi là một ninja lớn tuổi, đã kiểm soát được Vĩ thú của mình khá tốt. Nhưng ông vẫn không thoát được Akatsu…

```text
Wide 16:9 landscape cinematic frame. an elderly warrior standing alone on a volcanic ridge with steam rising around him, wide shot, dramatic red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Nhân trụ lực: Roshi, làng Đá. Son Goku tự hào, không thích bị gọi là Tứ Vĩ, và luôn muốn được gọi đúng tên.

```text
Wide 16:9 landscape cinematic frame. a proud nameplate carved into a volcanic rock, close-up, warm lava glow. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Hồ sơ số năm: Kokuo, Ngũ Vĩ. Hình dạng: lai giữa ngựa và cá heo, có sừng. Sức mạnh: hơi nước nóng.

```text
Wide 16:9 landscape cinematic frame. a giant horse-like silhouette with dolphin features and horns surrounded by billowing steam, wide shot, misty warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Han mặc một bộ giáp đặc biệt để kiềm chế hơi nước phát ra từ cơ thể. Một ví dụ cho thấy sống cùng Vĩ thú khôn…

```text
Wide 16:9 landscape cinematic frame. a heavy suit of armor with small vents releasing steam standing in a quiet workshop, close-up, warm misty light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhân trụ lực: Han, cũng của làng Đá. Kokuo điềm tĩnh, ít nói, và là một trong những Vĩ thú lịch sự nhất.

```text
Wide 16:9 landscape cinematic frame. a lone armored figure walking through a steam-filled canyon, back view, wide shot, soft diffused light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: làng Đá giữ tới hai Vĩ thú. Sự phân chia của Hashirama không đồng đều, và điều đó cũng là mầm mống…

```text
Wide 16:9 landscape cinematic frame. the owl mascot looking at an unbalanced scale with two small tokens on one side and one on the other. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Hồ sơ 6 và 7: Saiken và Chomei

Lời: Hồ sơ số sáu: Saiken, Lục Vĩ. Hình dạng: một con sên khổng lồ màu trắng. Sức mạnh: chất lỏng ăn mòn và bong b…

```text
Wide 16:9 landscape cinematic frame. a giant pale slug-like silhouette surrounded by floating bubbles in a humid swamp, wide shot, soft eerie light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Utakata từng có một người thầy muốn rút Vĩ thú ra khỏi cậu, và cậu bỏ làng ra đi. Nhiều nhân trụ lực mang nhữ…

```text
Wide 16:9 landscape cinematic frame. a lone figure walking away from a misty village along a narrow road, back view, wide shot, cold grey light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Nhân trụ lực: Utakata, người từng thuộc làng Sương mù, sống như một ninja lưu lạc. Saiken được mô tả là hiền…

```text
Wide 16:9 landscape cinematic frame. a lone figure blowing soap bubbles on a quiet riverbank at dusk, medium shot, gentle melancholy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Hồ sơ số bảy: Chomei, Thất Vĩ. Hình dạng: một con côn trùng khổng lồ có cánh, giống bọ cánh cứng. Sức mạnh: b…

```text
Wide 16:9 landscape cinematic frame. a giant winged beetle-like silhouette flying above a waterfall, glittering dust trailing from its wings, wide shot, bright magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52

Lời: Fu là một cô gái vui vẻ, muốn có thật nhiều bạn. Trong những phần phụ, cô được cho thấy luôn cố làm quen với…

```text
Wide 16:9 landscape cinematic frame. a cheerful girl waving at a group of children who hesitate at a distance, medium shot, bright bittersweet light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53

Lời: Nhân trụ lực: Fu, làng Thác nước. Chomei là Vĩ thú lạc quan, vui vẻ, và thích chuyện may mắn.

```text
Wide 16:9 landscape cinematic frame. a small village built around a massive waterfall with rainbows in the spray, wide shot, bright cheerful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Bảy Vĩ thú đầu tiên đều lần lượt bị Akatsuki bắt. Tới giữa Shippuden, chỉ còn hai: Bát Vĩ và Cửu Vĩ.

```text
Wide 16:9 landscape cinematic frame. seven of nine candles extinguished in a row, only two still burning at the end, close-up, somber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55 · Cuộc săn của Akatsuki

Lời: Akatsuki đi săn từng nhân trụ lực theo cặp. Mỗi cặp một mục tiêu. Họ bắt được Gaara ngay tại làng Cát, và lần…

```text
Wide 16:9 landscape cinematic frame. two cloaked silhouettes walking across a desert toward a distant village at dawn, back view, wide shot, ominous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Sau khi bắt, họ dùng một bức tượng khổng lồ để rút Vĩ thú ra khỏi nhân trụ lực. Quá trình kéo dài nhiều ngày,…

```text
Wide 16:9 landscape cinematic frame. a colossal stone statue with its hands raised in a dark cavern, faint glowing shapes surrounding it, low-angle shot, ominous dim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Gaara là trường hợp hiếm: cậu được hồi sinh nhờ sự hy sinh của bà Chiyo, một người làng Cát. Naruto chứng kiế…

```text
Wide 16:9 landscape cinematic frame. an elderly woman's hands glowing softly as she kneels beside a still figure on the grass, close-up, warm gentle light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Kaku để ý: Akatsuki coi Vĩ thú là tài nguyên. Các làng cũng vậy. Trong suốt cuộc săn, gần như không ai hỏi Vĩ…

```text
Wide 16:9 landscape cinematic frame. a ledger listing nine items with checkmarks beside seven of them, close-up, cold office light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59 · Hồ sơ 8: Gyuki, Bát Vĩ

Lời: Hồ sơ số tám: Gyuki, Bát Vĩ. Hình dạng: đầu bò, thân có tám xúc tu như bạch tuộc.

```text
Wide 16:9 landscape cinematic frame. a giant silhouette with a bull's head and eight octopus-like tentacles rising from the sea, low-angle shot, dramatic stormy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Sức mạnh: sức mạnh thể chất khủng khiếp, mực, và xúc tu có thể tái tạo. Tính cách: nghiêm túc, trầm tĩnh.

```text
Wide 16:9 landscape cinematic frame. a spray of dark ink spreading across the ocean surface, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Bee từng bị làng mình sợ hãi như mọi nhân trụ lực khác. Nhưng anh trai nuôi của Bee, Raikage, luôn đứng về ph…

```text
Wide 16:9 landscape cinematic frame. two brothers standing side by side on a cliff overlooking a mountain village, one arm resting on the other's shoulder, back view, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62

Lời: Nhân trụ lực: Killer Bee, làng Mây, em nuôi của Raikage. Bee là nhân trụ lực đầu tiên trong truyện sống hòa t…

```text
Wide 16:9 landscape cinematic frame. a large muscular figure sitting cross-legged on a rocky island shore, casually writing in a small notebook, medium shot, bright sunny light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Bee từng giả vờ bị bắt bằng cách để lại một xúc tu của Gyuki thay cho mình, rồi trốn đi nghỉ. Đó là cách một…

```text
Wide 16:9 landscape cinematic frame. a single large tentacle lying on a rocky beach while a figure's footprints lead away toward the sea, humorous wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Bee và Gyuki là bạn thật sự. Họ nói chuyện, đùa nhau, và chiến đấu như một đội. Bee còn thích làm thơ, dù thơ…

```text
Wide 16:9 landscape cinematic frame. a notebook page filled with scribbled rhymes and small doodles, close-up, playful warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Chính Bee là người dạy Naruto cách kiểm soát Cửu Vĩ. Hồ sơ số tám là hồ sơ quan trọng nhất cho cái kết của hồ…

```text
Wide 16:9 landscape cinematic frame. an older figure and a younger figure meditating side by side beside a waterfall, medium shot, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66 · Hồ sơ 9: Kurama, Cửu Vĩ

Lời: Hồ sơ số chín: Kurama, Cửu Vĩ. Hình dạng: một con cáo khổng lồ với chín đuôi. Sức mạnh: lượng chakra lớn nhất…

```text
Wide 16:9 landscape cinematic frame. a colossal fox silhouette with nine flowing tails standing on a mountain ridge at night, low-angle shot, fierce orange light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Và mắt Sharingan có thể điều khiển Vĩ thú. Đó là lý do Kurama căm ghét cả tộc Uchiha, và những ai muốn dùng n…

```text
Wide 16:9 landscape cinematic frame. a glowing red eye reflected in a giant animal's eye in extreme close-up, dramatic crimson light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kurama từng bị Madara điều khiển để tấn công làng Lá, và bị phong ấn nhiều lần. Nó căm ghét con người, vì chỉ…

```text
Wide 16:9 landscape cinematic frame. a massive dark silhouette looming over a village at night with fire on the horizon, wide shot, dramatic red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Người trong làng không được phép nói về Cửu Vĩ với trẻ con. Vì vậy những đứa trẻ khác không biết vì sao cha m…

```text
Wide 16:9 landscape cinematic frame. a group of parents pulling their children away from a small boy near a swing, wide shot, cold afternoon light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70

Lời: Nhân trụ lực: Naruto, được phong ấn ngay từ ngày sinh. Và cậu bị cả làng xa lánh vì con quái vật bên trong.

```text
Wide 16:9 landscape cinematic frame. a small child standing alone at the edge of a crowded festival, looking at families laughing together, wide shot, lonely warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71

Lời: Có lần Kurama cho Naruto mượn sức chỉ vì không muốn chết theo cậu. Mối quan hệ của hai người lúc đó là một th…

```text
Wide 16:9 landscape cinematic frame. two hands reaching toward each other across a cage's bars but not touching, symbolic close-up, cold red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Suốt nhiều năm, Naruto và Kurama là kẻ thù. Naruto mượn sức Kurama khi giận dữ, và Kurama chờ cơ hội chiếm lấ…

```text
Wide 16:9 landscape cinematic frame. a small figure standing before a massive cage with glowing eyes behind the bars, symbolic wide shot, eerie red light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Nhưng trong Đại chiến ninja lần thứ tư, Naruto làm điều chưa ai làm: cậu hỏi tên của Kurama, và muốn làm bạn…

```text
Wide 16:9 landscape cinematic frame. a small hand and a giant clawed paw pressing their fists together in a glowing space, symbolic close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku để ý: hành động quan trọng nhất trong cả hồ sơ này không phải một đòn đánh. Nó là việc gọi một con quái…

```text
Wide 16:9 landscape cinematic frame. the owl mascot carefully writing a name on a blank label and sticking it onto a folder. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · Chín Vĩ thú cùng nhau

Lời: Trong Đại chiến ninja lần thứ tư, Akatsuki gom đủ Vĩ thú để hồi sinh Thập Vĩ. Chín con bị buộc phải hợp lại t…

```text
Wide 16:9 landscape cinematic frame. nine glowing streams of energy spiraling together into one enormous dark shape in the sky, wide shot, apocalyptic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76

Lời: Và Naruto, qua Kurama, nói chuyện được với tất cả Vĩ thú. Cậu biết tên từng con, và chúng lần đầu tiên thấy m…

```text
Wide 16:9 landscape cinematic frame. a small figure standing in a vast glowing space surrounded by nine large gentle animal silhouettes, wide shot, warm ethereal light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Và các Vĩ thú còn truyền cho Naruto một phần chakra của mình. Từ chín sinh vật bị chia cắt, chúng lại gặp nha…

```text
Wide 16:9 landscape cinematic frame. nine small glowing lights gently flowing into a single figure's open palm, symbolic close-up, warm golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Đó chính là người mà Lục Đạo Tiên Nhân đã hứa với chúng gần một nghìn năm trước: người sẽ hiểu chúng.

```text
Wide 16:9 landscape cinematic frame. an old sage's silhouette faintly visible in the sky smiling down at a small figure below, symbolic wide shot, radiant golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Và Kurama ở lại với Naruto, không phải vì bị giam, mà vì muốn thế. Đó là lần đầu tiên trong gần một nghìn năm…

```text
Wide 16:9 landscape cinematic frame. a large fox silhouette resting its head gently beside a young man sitting on a cliff at sunrise, wide shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80

Lời: Sau chiến tranh, các Vĩ thú được giải thoát. Nhiều con chọn sống tự do, không còn bị giam trong ai.

```text
Wide 16:9 landscape cinematic frame. several large animal silhouettes wandering freely across open meadows and mountains at sunrise, wide shot, peaceful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s81 · Mục lục hồ sơ

Lời: Mục lục hồ sơ Vĩ thú. Một: Shukaku, lửng chó cát, Gaara, làng Cát. Hai: Matatabi, mèo lửa xanh, Yugito, làng…

```text
Wide 16:9 landscape cinematic frame. an index page with small animal doodles and names listed beside each number, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s82

Lời: Bốn: Son Goku, khỉ dung nham, Roshi, làng Đá. Năm: Kokuo, ngựa cá heo hơi nước, Han, làng Đá. Sáu: Saiken, sê…

```text
Wide 16:9 landscape cinematic frame. the middle section of the index page with more doodles, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s83

Lời: Bảy: Chomei, côn trùng có cánh, Fu, làng Thác nước. Tám: Gyuki, bò bạch tuộc, Killer Bee, làng Mây. Chín: Kur…

```text
Wide 16:9 landscape cinematic frame. the final section of the index page with a large fox doodle at the bottom and a small star beside it, amber ink close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s84

Lời: Và ghi chú cuối trang: tất cả đều có tên, do Lục Đạo Tiên Nhân đặt. Và tất cả đều từng là một phần của cùng m…

```text
Wide 16:9 landscape cinematic frame. a small handwritten note at the bottom of the index page with a single circle connecting nine dots, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s85 · Trò chơi: Vĩ thú nào hợp với bạn?

Lời: Giờ tới trò chơi. Nếu bạn là nhân trụ lực, bạn muốn mang Vĩ thú nào?

```text
Wide 16:9 landscape cinematic frame. nine small cards laid face down on a table, each with a different tail count on its back, close-up, warm playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s86

Lời: Nếu bạn thích sự bình yên, có lẽ là Saiken hoặc Kokuo. Nếu bạn thích phiêu lưu, là Chomei. Nếu bạn muốn mạnh…

```text
Wide 16:9 landscape cinematic frame. a few cards turned over showing small doodles of a slug, a winged beetle, a fox and an octopus, close-up, playful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s87 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku chọn Isobu, con rùa nhút nhát. Vì Kaku cũng thích trốn trong vỏ khi phải thuyết trình. Còn bạn? Viết vào…

```text
Wide 16:9 landscape cinematic frame. the owl mascot hiding shyly behind a tiny turtle shell prop. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s88 · Kết

Lời: Nhìn lại, câu chuyện của Vĩ thú và câu chuyện của nhân trụ lực giống hệt nhau: cả hai đều bị xa lánh vì thứ m…

```text
Wide 16:9 landscape cinematic frame. a small figure and a large animal silhouette sitting back to back on a hill under a starry sky, wide shot, gentle blue light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s89

Lời: Vĩ thú là những sinh vật bị con người giam giữ vì sợ hãi. Và câu chuyện của chúng chỉ thay đổi khi có một ngư…

```text
Wide 16:9 landscape cinematic frame. a large gentle animal silhouette resting its head beside a small figure sitting on a grassy hill at sunset, wide shot, warm tender light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s90

Lời: Video tiếp theo, Kaku gỡ mười hiểu lầm về Dragon Ball, từ sức mạnh của các Super Saiyan tới những điều nhiều…

```text
Wide 16:9 landscape cinematic frame. an orange crystal ball with stars inside resting on a stack of old comics, close-up, warm nostalgic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s91 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn thích những hồ sơ như thế này, hãy đăng ký kênh. Và lần tới gặp một người bị mọi người sợ hãi, hãy th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing the thick case file and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

### c01 · Mở đầu / Nguồn gốc: Thập Vĩ / Luật: nhân trụ lực và cân bằng quyền lực

Khoảng 137 giây · cảnh s01–s14 · 1785 ký tự

**Gemini**

```text
Cảnh báo spoiler: video này nói tới hết Naruto Shippuden, kể cả nguồn gốc của Vĩ thú trong Đại chiến ninja lần thứ tư.

<short pause> Hồ sơ số chín. Loài: cáo khổng lồ. Số đuôi: chín. Sức mạnh: đủ để san phẳng một ngôi làng. Nhân trụ lực hiện tại: một cậu bé tóc vàng từng bị cả làng xa lánh.

<short pause> Trong thế giới Naruto có chín sinh vật khổng lồ, mỗi con mang một lượng chakra khổng lồ, gọi là Vĩ thú. Người ta sợ chúng, giam chúng, và dùng chúng làm vũ khí.

<short pause> Nhưng ít ai hỏi: Vĩ thú muốn gì? Chúng có tên không? Và vì sao chúng ghét con người?

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku mở chín hồ sơ Vĩ thú. Mỗi hồ sơ có năm dòng: tên, hình dạng, sức mạnh, nhân trụ lực, và làng giữ nó. Cuối video là mục lục đầy đủ.

<short pause> Trước khi có chín Vĩ thú, chỉ có một sinh vật: Thập Vĩ, con quái vật mười đuôi, gắn với một cây thần cổ xưa.

<short pause> Lục Đạo Tiên Nhân, Otsutsuki Hagoromo, đánh bại Thập Vĩ và phong ấn nó vào chính cơ thể mình. Ông trở thành nhân trụ lực đầu tiên.

<short pause> Trước khi chết, ông chia chakra của Thập Vĩ thành chín phần, tạo ra chín Vĩ thú. Và ông đặt cho mỗi con một cái tên.

<short pause> Hagoromo coi chúng như con của mình. Ông nói với chúng rằng một ngày nào đó sẽ có người hiểu chúng. Lời hứa đó phải chờ gần một nghìn năm.

<short pause> Kaku để ý: con người trong truyện gần như không ai biết Vĩ thú có tên. Họ gọi chúng bằng số đuôi, như gọi một món vũ khí. Chính điều đó cho thấy vấn đề.

<short pause> Về sau, Hashirama, Hokage đệ nhất, bắt giữ nhiều Vĩ thú và chia chúng cho các làng ninja lớn để giữ cân bằng quyền lực.

<short pause> Để kiểm soát Vĩ thú, các làng phong ấn chúng vào cơ thể con người. Người đó gọi là nhân trụ lực.

<short pause> Nhân trụ lực có thể mượn chakra của Vĩ thú. <short pause> Nhưng họ thường bị cả làng sợ hãi, xa lánh, như thể chính họ là con quái vật.

<short pause> Và nếu Vĩ thú bị rút ra khỏi cơ thể, nhân trụ lực thường không sống sót. Đó là lý do tổ chức Akatsuki săn lùng họ.
```

**ElevenLabs**

```text
Cảnh báo spoiler: video này nói tới hết Naruto Shippuden, kể cả nguồn gốc của Vĩ thú trong Đại chiến ninja lần thứ tư.

[pause] Hồ sơ số chín. Loài: cáo khổng lồ. Số đuôi: chín. Sức mạnh: đủ để san phẳng một ngôi làng. Nhân trụ lực hiện tại: một cậu bé tóc vàng từng bị cả làng xa lánh.

[pause] Trong thế giới Naruto có chín sinh vật khổng lồ, mỗi con mang một lượng chakra khổng lồ, gọi là Vĩ thú. Người ta sợ chúng, giam chúng, và dùng chúng làm vũ khí.

[pause] [curious] Nhưng ít ai hỏi: Vĩ thú muốn gì? Chúng có tên không? Và vì sao chúng ghét con người?

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku mở chín hồ sơ Vĩ thú. Mỗi hồ sơ có năm dòng: tên, hình dạng, sức mạnh, nhân trụ lực, và làng giữ nó. Cuối video là mục lục đầy đủ.

[pause] Trước khi có chín Vĩ thú, chỉ có một sinh vật: Thập Vĩ, con quái vật mười đuôi, gắn với một cây thần cổ xưa.

[pause] Lục Đạo Tiên Nhân, Otsutsuki Hagoromo, đánh bại Thập Vĩ và phong ấn nó vào chính cơ thể mình. Ông trở thành nhân trụ lực đầu tiên.

[pause] Trước khi chết, ông chia chakra của Thập Vĩ thành chín phần, tạo ra chín Vĩ thú. Và ông đặt cho mỗi con một cái tên.

[pause] Hagoromo coi chúng như con của mình. Ông nói với chúng rằng một ngày nào đó sẽ có người hiểu chúng. Lời hứa đó phải chờ gần một nghìn năm.

[pause] Kaku để ý: con người trong truyện gần như không ai biết Vĩ thú có tên. Họ gọi chúng bằng số đuôi, như gọi một món vũ khí. Chính điều đó cho thấy vấn đề.

[pause] Về sau, Hashirama, Hokage đệ nhất, bắt giữ nhiều Vĩ thú và chia chúng cho các làng ninja lớn để giữ cân bằng quyền lực.

[pause] Để kiểm soát Vĩ thú, các làng phong ấn chúng vào cơ thể con người. Người đó gọi là nhân trụ lực.

[pause] Nhân trụ lực có thể mượn chakra của Vĩ thú. [pause] Nhưng họ thường bị cả làng sợ hãi, xa lánh, như thể chính họ là con quái vật.

[pause] Và nếu Vĩ thú bị rút ra khỏi cơ thể, nhân trụ lực thường không sống sót. Đó là lý do tổ chức Akatsuki săn lùng họ.
```

### c02 · Sức mạnh chung của Vĩ thú / Những nhân trụ lực trước Naruto / Hồ sơ 1: Shukaku, Nhất Vĩ

Khoảng 130 giây · cảnh s15–s28 · 1688 ký tự

**Gemini**

```text
Trước khi mở từng hồ sơ, Kaku ghi những sức mạnh mà Vĩ thú nào cũng có. Một: lượng chakra khổng lồ, càng nhiều đuôi thì thường càng nhiều chakra.

<short pause> Hai: Vĩ thú ngọc, một khối cầu chakra nén cực mạnh, bắn ra có thể phá hủy cả một vùng rộng lớn.

<short pause> Ba: nhân trụ lực có thể biến hình theo nhiều cấp: mọc một vài đuôi bằng chakra, khoác áo chakra, rồi hóa thành toàn bộ Vĩ thú. Càng lên cao, càng khó kiểm soát.

<short pause> Và người kiểm soát được Vĩ thú hoàn toàn, hợp tác thay vì bị chiếm lấy, được gọi là nhân trụ lực hoàn hảo. Rất ít người làm được.

<short pause> Naruto không phải nhân trụ lực đầu tiên của Cửu Vĩ. Người đầu tiên là Uzumaki Mito, vợ của Hokage đệ nhất Hashirama.

<short pause> Người thứ hai là Uzumaki Kushina, mẹ của Naruto. Tộc Uzumaki có sinh lực và chakra đặc biệt mạnh, nên thích hợp để giữ Cửu Vĩ.

<short pause> Đêm Naruto chào đời, Cửu Vĩ bị giải phóng khỏi Kushina và tấn công làng. Cha mẹ Naruto hy sinh để phong ấn nó vào chính con trai mình.

<short pause> <laugh> Kaku để ý: ba đời nhân trụ lực Cửu Vĩ đều là tộc Uzumaki. Cửu Vĩ gần như là một phần lịch sử gia đình của Naruto.

<short pause> Hồ sơ số một: Shukaku, Nhất Vĩ. Hình dạng: một con lửng chó khổng lồ, thân làm bằng cát, có hoa văn trên người.

<short pause> Sức mạnh: điều khiển cát, và phong ấn phép thuật. Tính cách: hung hăng, ồn ào, thích gây sự.

<short pause> Cha của Gaara, Kazekage, đã cố tình phong ấn Shukaku vào con mình trước khi sinh, để tạo ra vũ khí cho làng. Gaara lớn lên tin rằng không ai yêu mình.

<short pause> Nhân trụ lực: Gaara, làng Cát. Gaara từng là một đứa trẻ cô độc, không ngủ được vì sợ Shukaku chiếm lấy cơ thể mình khi ngủ.

<short pause> Sau khi gặp Naruto, Gaara thay đổi và trở thành Kazekage. Nhất Vĩ là con Vĩ thú đầu tiên cho thấy nhân trụ lực có thể được làng mình yêu quý.

<short pause> Mức nguy hiểm: trung bình. Mức bị hiểu lầm: rất cao.
```

**ElevenLabs**

```text
Trước khi mở từng hồ sơ, Kaku ghi những sức mạnh mà Vĩ thú nào cũng có. Một: lượng chakra khổng lồ, càng nhiều đuôi thì thường càng nhiều chakra.

[pause] Hai: Vĩ thú ngọc, một khối cầu chakra nén cực mạnh, bắn ra có thể phá hủy cả một vùng rộng lớn.

[pause] Ba: nhân trụ lực có thể biến hình theo nhiều cấp: mọc một vài đuôi bằng chakra, khoác áo chakra, rồi hóa thành toàn bộ Vĩ thú. Càng lên cao, càng khó kiểm soát.

[pause] Và người kiểm soát được Vĩ thú hoàn toàn, hợp tác thay vì bị chiếm lấy, được gọi là nhân trụ lực hoàn hảo. Rất ít người làm được.

[pause] Naruto không phải nhân trụ lực đầu tiên của Cửu Vĩ. Người đầu tiên là Uzumaki Mito, vợ của Hokage đệ nhất Hashirama.

[pause] Người thứ hai là Uzumaki Kushina, mẹ của Naruto. Tộc Uzumaki có sinh lực và chakra đặc biệt mạnh, nên thích hợp để giữ Cửu Vĩ.

[pause] Đêm Naruto chào đời, Cửu Vĩ bị giải phóng khỏi Kushina và tấn công làng. Cha mẹ Naruto hy sinh để phong ấn nó vào chính con trai mình.

[pause] [chuckles] Kaku để ý: ba đời nhân trụ lực Cửu Vĩ đều là tộc Uzumaki. Cửu Vĩ gần như là một phần lịch sử gia đình của Naruto.

[pause] Hồ sơ số một: Shukaku, Nhất Vĩ. Hình dạng: một con lửng chó khổng lồ, thân làm bằng cát, có hoa văn trên người.

[pause] Sức mạnh: điều khiển cát, và phong ấn phép thuật. Tính cách: hung hăng, ồn ào, thích gây sự.

[pause] Cha của Gaara, Kazekage, đã cố tình phong ấn Shukaku vào con mình trước khi sinh, để tạo ra vũ khí cho làng. Gaara lớn lên tin rằng không ai yêu mình.

[pause] Nhân trụ lực: Gaara, làng Cát. Gaara từng là một đứa trẻ cô độc, không ngủ được vì sợ Shukaku chiếm lấy cơ thể mình khi ngủ.

[pause] Sau khi gặp Naruto, Gaara thay đổi và trở thành Kazekage. Nhất Vĩ là con Vĩ thú đầu tiên cho thấy nhân trụ lực có thể được làng mình yêu quý.

[pause] Mức nguy hiểm: trung bình. Mức bị hiểu lầm: rất cao.
```

### c03 · Hồ sơ 2: Matatabi, Nhị Vĩ / Hồ sơ 3: Isobu, Tam Vĩ

Khoảng 115 giây · cảnh s29–s40 · 1493 ký tự

**Gemini**

```text
Hồ sơ số hai: Matatabi, Nhị Vĩ. Hình dạng: một con mèo khổng lồ phủ ngọn lửa xanh.

<short pause> Trong văn hóa Nhật, mèo có hai đuôi gợi tới yêu quái mèo trong truyện dân gian. Matatabi cũng là tên một loài cây mà mèo rất thích.

<short pause> Sức mạnh: lửa xanh, và sự nhanh nhẹn của loài mèo. Tính cách: điềm tĩnh, lịch sự hơn nhiều Vĩ thú khác.

<short pause> Nhân trụ lực: Yugito Nii, làng Mây. Cô là một trong những nhân trụ lực kiểm soát Vĩ thú tốt nhất, nhưng vẫn bị Akatsuki bắt.

<short pause> Anime và các phần phụ sau này có kể thêm về vài nhân trụ lực này, nhưng phần lớn chỉ là những lát cắt ngắn. Người đọc thường nhớ họ qua tên, hơn là qua câu chuyện.

<short pause> Kaku để ý: nhiều nhân trụ lực như Yugito chỉ xuất hiện rất ít trong truyện. Họ là những câu chuyện chưa được kể, bị cuốn đi trong cuộc săn của Akatsuki.

<short pause> Hồ sơ số ba: Isobu, Tam Vĩ. Hình dạng: một con rùa khổng lồ với lớp vỏ gai nhọn như san hô.

<short pause> Rùa là biểu tượng của sự phòng thủ và tuổi thọ. Isobu không muốn đánh nhau, nó chỉ muốn được để yên dưới đáy hồ.

<short pause> Sức mạnh: phòng thủ cực mạnh, và tạo sương mù, san hô. Tính cách: nhút nhát, không thích đánh nhau.

<short pause> Nhân trụ lực: Yagura, Mizukage của làng Sương mù, từng bị thao túng. Và trong quá khứ, Tam Vĩ còn từng bị phong ấn vào một cô gái tên Rin, người đồng đội của Kakashi, trong một kế hoạch đen tối.

<short pause> Kaku ghi thêm: Tam Vĩ là Vĩ thú bị bắt dễ dàng nhất trong cuộc săn của Akatsuki, vì lúc đó nó không có nhân trụ lực nào bảo vệ.

<short pause> Tam Vĩ là Vĩ thú từng không có nhân trụ lực trong một thời gian, sống tự do trong hồ. Một hồ sơ nhiều khoảng trống.
```

**ElevenLabs**

```text
Hồ sơ số hai: Matatabi, Nhị Vĩ. Hình dạng: một con mèo khổng lồ phủ ngọn lửa xanh.

[pause] Trong văn hóa Nhật, mèo có hai đuôi gợi tới yêu quái mèo trong truyện dân gian. Matatabi cũng là tên một loài cây mà mèo rất thích.

[pause] Sức mạnh: lửa xanh, và sự nhanh nhẹn của loài mèo. Tính cách: điềm tĩnh, lịch sự hơn nhiều Vĩ thú khác.

[pause] Nhân trụ lực: Yugito Nii, làng Mây. Cô là một trong những nhân trụ lực kiểm soát Vĩ thú tốt nhất, nhưng vẫn bị Akatsuki bắt.

[pause] Anime và các phần phụ sau này có kể thêm về vài nhân trụ lực này, nhưng phần lớn chỉ là những lát cắt ngắn. Người đọc thường nhớ họ qua tên, hơn là qua câu chuyện.

[pause] Kaku để ý: nhiều nhân trụ lực như Yugito chỉ xuất hiện rất ít trong truyện. Họ là những câu chuyện chưa được kể, bị cuốn đi trong cuộc săn của Akatsuki.

[pause] Hồ sơ số ba: Isobu, Tam Vĩ. Hình dạng: một con rùa khổng lồ với lớp vỏ gai nhọn như san hô.

[pause] Rùa là biểu tượng của sự phòng thủ và tuổi thọ. Isobu không muốn đánh nhau, nó chỉ muốn được để yên dưới đáy hồ.

[pause] Sức mạnh: phòng thủ cực mạnh, và tạo sương mù, san hô. Tính cách: nhút nhát, không thích đánh nhau.

[pause] Nhân trụ lực: Yagura, Mizukage của làng Sương mù, từng bị thao túng. Và trong quá khứ, Tam Vĩ còn từng bị phong ấn vào một cô gái tên Rin, người đồng đội của Kakashi, trong một kế hoạch đen tối.

[pause] Kaku ghi thêm: Tam Vĩ là Vĩ thú bị bắt dễ dàng nhất trong cuộc săn của Akatsuki, vì lúc đó nó không có nhân trụ lực nào bảo vệ.

[pause] Tam Vĩ là Vĩ thú từng không có nhân trụ lực trong một thời gian, sống tự do trong hồ. Một hồ sơ nhiều khoảng trống.
```

### c04 · Hồ sơ 4 và 5: Son Goku và Kokuo / Hồ sơ 6 và 7: Saiken và Chomei

Khoảng 136 giây · cảnh s41–s54 · 1769 ký tự

**Gemini**

```text
Hồ sơ số bốn: Son Goku, Tứ Vĩ. Hình dạng: một con khỉ đột khổng lồ. Sức mạnh: dung nham. Tên của nó lấy cảm hứng từ Tôn Ngộ Không trong Tây Du Ký.

<short pause> Roshi là một ninja lớn tuổi, đã kiểm soát được Vĩ thú của mình khá tốt. <short pause> Nhưng ông vẫn không thoát được Akatsuki. Không ai an toàn trong cuộc săn đó.

<short pause> Nhân trụ lực: Roshi, làng Đá. Son Goku tự hào, không thích bị gọi là Tứ Vĩ, và luôn muốn được gọi đúng tên.

<short pause> Hồ sơ số năm: Kokuo, Ngũ Vĩ. Hình dạng: lai giữa ngựa và cá heo, có sừng. Sức mạnh: hơi nước nóng.

<short pause> Han mặc một bộ giáp đặc biệt để kiềm chế hơi nước phát ra từ cơ thể. Một ví dụ cho thấy sống cùng Vĩ thú không chỉ khó về tinh thần, mà cả về cơ thể.

<short pause> Nhân trụ lực: Han, cũng của làng Đá. Kokuo điềm tĩnh, ít nói, và là một trong những Vĩ thú lịch sự nhất.

<short pause> <laugh> Kaku để ý: làng Đá giữ tới hai Vĩ thú. Sự phân chia của Hashirama không đồng đều, và điều đó cũng là mầm mống của những căng thẳng giữa các làng.

<short pause> Hồ sơ số sáu: Saiken, Lục Vĩ. Hình dạng: một con sên khổng lồ màu trắng. Sức mạnh: chất lỏng ăn mòn và bong bóng.

<short pause> Utakata từng có một người thầy muốn rút Vĩ thú ra khỏi cậu, và cậu bỏ làng ra đi. Nhiều nhân trụ lực mang những vết thương như vậy từ chính người thân của mình.

<short pause> Nhân trụ lực: Utakata, người từng thuộc làng Sương mù, sống như một ninja lưu lạc. Saiken được mô tả là hiền lành.

<short pause> Hồ sơ số bảy: Chomei, Thất Vĩ. Hình dạng: một con côn trùng khổng lồ có cánh, giống bọ cánh cứng. Sức mạnh: bay, và phấn trên cánh làm lóa mắt kẻ thù.

<short pause> Fu là một cô gái vui vẻ, muốn có thật nhiều bạn. Trong những phần phụ, cô được cho thấy luôn cố làm quen với người khác, dù bị làng mình e dè.

<short pause> Nhân trụ lực: Fu, làng Thác nước. Chomei là Vĩ thú lạc quan, vui vẻ, và thích chuyện may mắn.

<short pause> Bảy Vĩ thú đầu tiên đều lần lượt bị Akatsuki bắt. Tới giữa Shippuden, chỉ còn hai: Bát Vĩ và Cửu Vĩ.
```

**ElevenLabs**

```text
Hồ sơ số bốn: Son Goku, Tứ Vĩ. Hình dạng: một con khỉ đột khổng lồ. Sức mạnh: dung nham. Tên của nó lấy cảm hứng từ Tôn Ngộ Không trong Tây Du Ký.

[pause] Roshi là một ninja lớn tuổi, đã kiểm soát được Vĩ thú của mình khá tốt. [pause] Nhưng ông vẫn không thoát được Akatsuki. Không ai an toàn trong cuộc săn đó.

[pause] Nhân trụ lực: Roshi, làng Đá. Son Goku tự hào, không thích bị gọi là Tứ Vĩ, và luôn muốn được gọi đúng tên.

[pause] Hồ sơ số năm: Kokuo, Ngũ Vĩ. Hình dạng: lai giữa ngựa và cá heo, có sừng. Sức mạnh: hơi nước nóng.

[pause] Han mặc một bộ giáp đặc biệt để kiềm chế hơi nước phát ra từ cơ thể. Một ví dụ cho thấy sống cùng Vĩ thú không chỉ khó về tinh thần, mà cả về cơ thể.

[pause] Nhân trụ lực: Han, cũng của làng Đá. Kokuo điềm tĩnh, ít nói, và là một trong những Vĩ thú lịch sự nhất.

[pause] [chuckles] Kaku để ý: làng Đá giữ tới hai Vĩ thú. Sự phân chia của Hashirama không đồng đều, và điều đó cũng là mầm mống của những căng thẳng giữa các làng.

[pause] Hồ sơ số sáu: Saiken, Lục Vĩ. Hình dạng: một con sên khổng lồ màu trắng. Sức mạnh: chất lỏng ăn mòn và bong bóng.

[pause] Utakata từng có một người thầy muốn rút Vĩ thú ra khỏi cậu, và cậu bỏ làng ra đi. Nhiều nhân trụ lực mang những vết thương như vậy từ chính người thân của mình.

[pause] Nhân trụ lực: Utakata, người từng thuộc làng Sương mù, sống như một ninja lưu lạc. Saiken được mô tả là hiền lành.

[pause] Hồ sơ số bảy: Chomei, Thất Vĩ. Hình dạng: một con côn trùng khổng lồ có cánh, giống bọ cánh cứng. Sức mạnh: bay, và phấn trên cánh làm lóa mắt kẻ thù.

[pause] Fu là một cô gái vui vẻ, muốn có thật nhiều bạn. Trong những phần phụ, cô được cho thấy luôn cố làm quen với người khác, dù bị làng mình e dè.

[pause] Nhân trụ lực: Fu, làng Thác nước. Chomei là Vĩ thú lạc quan, vui vẻ, và thích chuyện may mắn.

[pause] Bảy Vĩ thú đầu tiên đều lần lượt bị Akatsuki bắt. Tới giữa Shippuden, chỉ còn hai: Bát Vĩ và Cửu Vĩ.
```

### c05 · Cuộc săn của Akatsuki / Hồ sơ 8: Gyuki, Bát Vĩ

Khoảng 113 giây · cảnh s55–s65 · 1466 ký tự

**Gemini**

```text
Akatsuki đi săn từng nhân trụ lực theo cặp. Mỗi cặp một mục tiêu. Họ bắt được Gaara ngay tại làng Cát, và lần lượt bắt những người khác.

<short pause> Sau khi bắt, họ dùng một bức tượng khổng lồ để rút Vĩ thú ra khỏi nhân trụ lực. Quá trình kéo dài nhiều ngày, và nhân trụ lực hầu như không sống sót.

<short pause> Gaara là trường hợp hiếm: cậu được hồi sinh nhờ sự hy sinh của bà Chiyo, một người làng Cát. Naruto chứng kiến điều đó, và nó ảnh hưởng tới cách cậu nhìn về nhân trụ lực.

<short pause> Kaku để ý: Akatsuki coi Vĩ thú là tài nguyên. Các làng cũng vậy. Trong suốt cuộc săn, gần như không ai hỏi Vĩ thú muốn gì.

<short pause> Hồ sơ số tám: Gyuki, Bát Vĩ. Hình dạng: đầu bò, thân có tám xúc tu như bạch tuộc.

<short pause> Sức mạnh: sức mạnh thể chất khủng khiếp, mực, và xúc tu có thể tái tạo. Tính cách: nghiêm túc, trầm tĩnh.

<short pause> Bee từng bị làng mình sợ hãi như mọi nhân trụ lực khác. <short pause> Nhưng anh trai nuôi của Bee, Raikage, luôn đứng về phía em. Có một người tin mình, mọi thứ đã khác.

<short pause> Nhân trụ lực: Killer Bee, làng Mây, em nuôi của Raikage. Bee là nhân trụ lực đầu tiên trong truyện sống hòa thuận hoàn toàn với Vĩ thú của mình.

<short pause> Bee từng giả vờ bị bắt bằng cách để lại một xúc tu của Gyuki thay cho mình, rồi trốn đi nghỉ. Đó là cách một nhân trụ lực hoàn hảo đùa với cả Akatsuki.

<short pause> Bee và Gyuki là bạn thật sự. Họ nói chuyện, đùa nhau, và chiến đấu như một đội. Bee còn thích làm thơ, dù thơ của Bee không hay lắm.

<short pause> Chính Bee là người dạy Naruto cách kiểm soát Cửu Vĩ. Hồ sơ số tám là hồ sơ quan trọng nhất cho cái kết của hồ sơ số chín.
```

**ElevenLabs**

```text
Akatsuki đi săn từng nhân trụ lực theo cặp. Mỗi cặp một mục tiêu. Họ bắt được Gaara ngay tại làng Cát, và lần lượt bắt những người khác.

[pause] Sau khi bắt, họ dùng một bức tượng khổng lồ để rút Vĩ thú ra khỏi nhân trụ lực. Quá trình kéo dài nhiều ngày, và nhân trụ lực hầu như không sống sót.

[pause] Gaara là trường hợp hiếm: cậu được hồi sinh nhờ sự hy sinh của bà Chiyo, một người làng Cát. Naruto chứng kiến điều đó, và nó ảnh hưởng tới cách cậu nhìn về nhân trụ lực.

[pause] Kaku để ý: Akatsuki coi Vĩ thú là tài nguyên. Các làng cũng vậy. Trong suốt cuộc săn, gần như không ai hỏi Vĩ thú muốn gì.

[pause] Hồ sơ số tám: Gyuki, Bát Vĩ. Hình dạng: đầu bò, thân có tám xúc tu như bạch tuộc.

[pause] Sức mạnh: sức mạnh thể chất khủng khiếp, mực, và xúc tu có thể tái tạo. Tính cách: nghiêm túc, trầm tĩnh.

[pause] Bee từng bị làng mình sợ hãi như mọi nhân trụ lực khác. [pause] Nhưng anh trai nuôi của Bee, Raikage, luôn đứng về phía em. Có một người tin mình, mọi thứ đã khác.

[pause] Nhân trụ lực: Killer Bee, làng Mây, em nuôi của Raikage. Bee là nhân trụ lực đầu tiên trong truyện sống hòa thuận hoàn toàn với Vĩ thú của mình.

[pause] Bee từng giả vờ bị bắt bằng cách để lại một xúc tu của Gyuki thay cho mình, rồi trốn đi nghỉ. Đó là cách một nhân trụ lực hoàn hảo đùa với cả Akatsuki.

[pause] Bee và Gyuki là bạn thật sự. Họ nói chuyện, đùa nhau, và chiến đấu như một đội. Bee còn thích làm thơ, dù thơ của Bee không hay lắm.

[pause] Chính Bee là người dạy Naruto cách kiểm soát Cửu Vĩ. Hồ sơ số tám là hồ sơ quan trọng nhất cho cái kết của hồ sơ số chín.
```

### c06 · Hồ sơ 9: Kurama, Cửu Vĩ / Chín Vĩ thú cùng nhau

Khoảng 154 giây · cảnh s66–s80 · 1999 ký tự

**Gemini**

```text
Hồ sơ số chín: Kurama, Cửu Vĩ. Hình dạng: một con cáo khổng lồ với chín đuôi. Sức mạnh: lượng chakra lớn nhất trong chín Vĩ thú.

<short pause> Và mắt Sharingan có thể điều khiển Vĩ thú. Đó là lý do Kurama căm ghét cả tộc Uchiha, và những ai muốn dùng nó làm vũ khí.

<short pause> Kurama từng bị Madara điều khiển để tấn công làng Lá, và bị phong ấn nhiều lần. Nó căm ghét con người, vì chỉ thấy con người dùng nó làm vũ khí.

<short pause> Người trong làng không được phép nói về Cửu Vĩ với trẻ con. Vì vậy những đứa trẻ khác không biết vì sao cha mẹ chúng lại tránh xa Naruto. Chúng chỉ bắt chước.

<short pause> Nhân trụ lực: Naruto, được phong ấn ngay từ ngày sinh. Và cậu bị cả làng xa lánh vì con quái vật bên trong.

<short pause> Có lần Kurama cho Naruto mượn sức chỉ vì không muốn chết theo cậu. Mối quan hệ của hai người lúc đó là một thỏa thuận lạnh lùng, không phải tình bạn.

<short pause> Suốt nhiều năm, Naruto và Kurama là kẻ thù. Naruto mượn sức Kurama khi giận dữ, và Kurama chờ cơ hội chiếm lấy cơ thể cậu.

<short pause> Nhưng trong Đại chiến ninja lần thứ tư, Naruto làm điều chưa ai làm: cậu hỏi tên của Kurama, và muốn làm bạn với nó. Từ kẻ thù, hai người trở thành đồng đội.

<short pause> <laugh> Kaku để ý: hành động quan trọng nhất trong cả hồ sơ này không phải một đòn đánh. Nó là việc gọi một con quái vật bằng tên của nó.

<short pause> Trong Đại chiến ninja lần thứ tư, Akatsuki gom đủ Vĩ thú để hồi sinh Thập Vĩ. Chín con bị buộc phải hợp lại thành con quái vật ban đầu.

<short pause> Và Naruto, qua Kurama, nói chuyện được với tất cả Vĩ thú. Cậu biết tên từng con, và chúng lần đầu tiên thấy một con người không muốn dùng chúng.

<short pause> Và các Vĩ thú còn truyền cho Naruto một phần chakra của mình. Từ chín sinh vật bị chia cắt, chúng lại gặp nhau, lần này bằng sự tin tưởng thay vì bằng xiềng xích.

<short pause> Đó chính là người mà Lục Đạo Tiên Nhân đã hứa với chúng gần một nghìn năm trước: người sẽ hiểu chúng.

<short pause> Và Kurama ở lại với Naruto, không phải vì bị giam, mà vì muốn thế. Đó là lần đầu tiên trong gần một nghìn năm một Vĩ thú chọn ở bên con người.

<short pause> Sau chiến tranh, các Vĩ thú được giải thoát. Nhiều con chọn sống tự do, không còn bị giam trong ai.
```

**ElevenLabs**

```text
Hồ sơ số chín: Kurama, Cửu Vĩ. Hình dạng: một con cáo khổng lồ với chín đuôi. Sức mạnh: lượng chakra lớn nhất trong chín Vĩ thú.

[pause] Và mắt Sharingan có thể điều khiển Vĩ thú. Đó là lý do Kurama căm ghét cả tộc Uchiha, và những ai muốn dùng nó làm vũ khí.

[pause] Kurama từng bị Madara điều khiển để tấn công làng Lá, và bị phong ấn nhiều lần. Nó căm ghét con người, vì chỉ thấy con người dùng nó làm vũ khí.

[pause] Người trong làng không được phép nói về Cửu Vĩ với trẻ con. Vì vậy những đứa trẻ khác không biết vì sao cha mẹ chúng lại tránh xa Naruto. Chúng chỉ bắt chước.

[pause] Nhân trụ lực: Naruto, được phong ấn ngay từ ngày sinh. Và cậu bị cả làng xa lánh vì con quái vật bên trong.

[pause] Có lần Kurama cho Naruto mượn sức chỉ vì không muốn chết theo cậu. Mối quan hệ của hai người lúc đó là một thỏa thuận lạnh lùng, không phải tình bạn.

[pause] Suốt nhiều năm, Naruto và Kurama là kẻ thù. Naruto mượn sức Kurama khi giận dữ, và Kurama chờ cơ hội chiếm lấy cơ thể cậu.

[pause] Nhưng trong Đại chiến ninja lần thứ tư, Naruto làm điều chưa ai làm: cậu hỏi tên của Kurama, và muốn làm bạn với nó. Từ kẻ thù, hai người trở thành đồng đội.

[pause] [chuckles] Kaku để ý: hành động quan trọng nhất trong cả hồ sơ này không phải một đòn đánh. Nó là việc gọi một con quái vật bằng tên của nó.

[pause] Trong Đại chiến ninja lần thứ tư, Akatsuki gom đủ Vĩ thú để hồi sinh Thập Vĩ. Chín con bị buộc phải hợp lại thành con quái vật ban đầu.

[pause] Và Naruto, qua Kurama, nói chuyện được với tất cả Vĩ thú. Cậu biết tên từng con, và chúng lần đầu tiên thấy một con người không muốn dùng chúng.

[pause] Và các Vĩ thú còn truyền cho Naruto một phần chakra của mình. Từ chín sinh vật bị chia cắt, chúng lại gặp nhau, lần này bằng sự tin tưởng thay vì bằng xiềng xích.

[pause] Đó chính là người mà Lục Đạo Tiên Nhân đã hứa với chúng gần một nghìn năm trước: người sẽ hiểu chúng.

[pause] Và Kurama ở lại với Naruto, không phải vì bị giam, mà vì muốn thế. Đó là lần đầu tiên trong gần một nghìn năm một Vĩ thú chọn ở bên con người.

[pause] Sau chiến tranh, các Vĩ thú được giải thoát. Nhiều con chọn sống tự do, không còn bị giam trong ai.
```

### c07 · Mục lục hồ sơ / Trò chơi: Vĩ thú nào hợp với bạn? / Kết

Khoảng 120 giây · cảnh s81–s91 · 1558 ký tự

**Gemini**

```text
Mục lục hồ sơ Vĩ thú. Một: Shukaku, lửng chó cát, Gaara, làng Cát. Hai: Matatabi, mèo lửa xanh, Yugito, làng Mây. Ba: Isobu, rùa san hô, Yagura, làng Sương mù.

<short pause> Bốn: Son Goku, khỉ dung nham, Roshi, làng Đá. Năm: Kokuo, ngựa cá heo hơi nước, Han, làng Đá. Sáu: Saiken, sên bong bóng, Utakata, làng Sương mù.

<short pause> Bảy: Chomei, côn trùng có cánh, Fu, làng Thác nước. Tám: Gyuki, bò bạch tuộc, Killer Bee, làng Mây. Chín: Kurama, cáo chín đuôi, Naruto, làng Lá.

<short pause> Và ghi chú cuối trang: tất cả đều có tên, do Lục Đạo Tiên Nhân đặt. Và tất cả đều từng là một phần của cùng một sinh vật.

<short pause> Giờ tới trò chơi. Nếu bạn là nhân trụ lực, bạn muốn mang Vĩ thú nào?

<short pause> Nếu bạn thích sự bình yên, có lẽ là Saiken hoặc Kokuo. Nếu bạn thích phiêu lưu, là Chomei. Nếu bạn muốn mạnh nhất, là Kurama. Và nếu bạn muốn một người bạn biết làm thơ dở, là Gyuki.

<short pause> <laugh> Kaku chọn Isobu, con rùa nhút nhát. Vì Kaku cũng thích trốn trong vỏ khi phải thuyết trình. Còn bạn? Viết vào bình luận nhé.

<short pause> Nhìn lại, câu chuyện của Vĩ thú và câu chuyện của nhân trụ lực giống hệt nhau: cả hai đều bị xa lánh vì thứ mà họ không chọn. Và cả hai chỉ được giải thoát khi tìm thấy nhau.

<short pause> Vĩ thú là những sinh vật bị con người giam giữ vì sợ hãi. Và câu chuyện của chúng chỉ thay đổi khi có một người đủ kiên nhẫn để hỏi tên chúng.

<short pause> Video tiếp theo, Kaku gỡ mười hiểu lầm về Dragon Ball, từ sức mạnh của các Super Saiyan tới những điều nhiều người tin sai suốt ba mươi năm.

<short pause> Nếu bạn thích những hồ sơ như thế này, hãy đăng ký kênh. Và lần tới gặp một người bị mọi người sợ hãi, hãy thử hỏi tên họ trước. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Mục lục hồ sơ Vĩ thú. Một: Shukaku, lửng chó cát, Gaara, làng Cát. Hai: Matatabi, mèo lửa xanh, Yugito, làng Mây. Ba: Isobu, rùa san hô, Yagura, làng Sương mù.

[pause] Bốn: Son Goku, khỉ dung nham, Roshi, làng Đá. Năm: Kokuo, ngựa cá heo hơi nước, Han, làng Đá. Sáu: Saiken, sên bong bóng, Utakata, làng Sương mù.

[pause] Bảy: Chomei, côn trùng có cánh, Fu, làng Thác nước. Tám: Gyuki, bò bạch tuộc, Killer Bee, làng Mây. Chín: Kurama, cáo chín đuôi, Naruto, làng Lá.

[pause] Và ghi chú cuối trang: tất cả đều có tên, do Lục Đạo Tiên Nhân đặt. Và tất cả đều từng là một phần của cùng một sinh vật.

[pause] Giờ tới trò chơi. [curious] Nếu bạn là nhân trụ lực, bạn muốn mang Vĩ thú nào?

[pause] Nếu bạn thích sự bình yên, có lẽ là Saiken hoặc Kokuo. Nếu bạn thích phiêu lưu, là Chomei. Nếu bạn muốn mạnh nhất, là Kurama. Và nếu bạn muốn một người bạn biết làm thơ dở, là Gyuki.

[pause] [chuckles] Kaku chọn Isobu, con rùa nhút nhát. Vì Kaku cũng thích trốn trong vỏ khi phải thuyết trình. Còn bạn? Viết vào bình luận nhé.

[pause] Nhìn lại, câu chuyện của Vĩ thú và câu chuyện của nhân trụ lực giống hệt nhau: cả hai đều bị xa lánh vì thứ mà họ không chọn. Và cả hai chỉ được giải thoát khi tìm thấy nhau.

[pause] Vĩ thú là những sinh vật bị con người giam giữ vì sợ hãi. Và câu chuyện của chúng chỉ thay đổi khi có một người đủ kiên nhẫn để hỏi tên chúng.

[pause] Video tiếp theo, Kaku gỡ mười hiểu lầm về Dragon Ball, từ sức mạnh của các Super Saiyan tới những điều nhiều người tin sai suốt ba mươi năm.

[pause] Nếu bạn thích những hồ sơ như thế này, hãy đăng ký kênh. Và lần tới gặp một người bị mọi người sợ hãi, hãy thử hỏi tên họ trước. Kaku gấp sổ đây, hẹn gặp lại!
```
