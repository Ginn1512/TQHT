# Bộ prompt · Shangri-La Frontier: Đọc bảng chỉ số — vì sao Sunraku chỉ có 6 điểm thể chất?

> Tạo tự động từ `scenes.json` và `channel/giong-kaku.json` bằng `python -m tools.prompt_pack`. **Không sửa tay**: sửa `scenes.json` rồi chạy lại lệnh.
> Cách làm từng bước: `docs/huong-dan-lam-tay.md`.

- 80 ảnh, 9 đoạn đọc, khoảng 15.1 phút giọng.
- Ảnh: dán prompt vào Gemini app (tạo hình ảnh), tải ảnh gốc về, đặt tên theo số cảnh (`s01.png`…).
- Giọng: dán ghi chú đạo diễn một lần, rồi dán từng đoạn; tải file về, đặt tên theo số đoạn (`c01.wav`…).

## 1. Ảnh mẫu Kaku (một lần cho cả kênh)

Tạo 1 lần, lưu lại, rồi đính kèm làm ảnh tham chiếu cho mọi cảnh có đánh dấu **Kaku**.

```text
Wide 16:9 landscape cinematic frame. Character model sheet of the channel mascot on a plain warm parchment background: front view, three-quarter view and side view, full body, identical proportions and colors in every view: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. Even soft studio lighting. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

## 2. Ảnh (80 cảnh)

Negative prompt, chỉ dùng cho model có ô riêng (Gemini không cần):

```text
text, letters, caption, logo, watermark, signature, photorealistic, photo, 3D render, blurry, low resolution, extra fingers, deformed hands, distorted face, cropped head, existing anime characters, official art, screenshot
```

### s01 · Mở đầu

Lời: Cảnh báo: video có spoiler Shangri-La Frontier tới hết anime mùa hai. Mùa ba ra mắt tháng một này, và Kaku kh…

```text
Wide 16:9 landscape cinematic frame. a glowing virtual reality headset resting on a desk beside a closed notebook, soft blue screen light in a dark room, wide establishing shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s02

Lời: Đây là thẻ chỉ số của một người chơi. Sức bền khá. Sức mạnh vừa phải. Nhanh nhẹn rất cao. May mắn rất cao. Cò…

```text
Wide 16:9 landscape cinematic frame. a floating fantasy game status window with glowing bars, one bar almost empty, close-up, vibrant cyan and amber light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s03

Lời: Nếu bạn chơi game nhập vai, bạn sẽ nói ngay: đây là một bản xây dựng nhân vật tồi tệ. Chỉ cần một cú đánh là…

```text
Wide 16:9 landscape cinematic frame. a fragile paper doll standing in front of a giant monster silhouette in a dark forest, humorous wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s04

Lời: Nhưng chủ nhân của thẻ chỉ số này đã sống sót trước những con quái vật mạnh nhất trò chơi, những thứ mà cả ng…

```text
Wide 16:9 landscape cinematic frame. a lone agile player silhouette leaping over a colossal monster's claw in a moonlit forest, dynamic wide shot, silver light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s05

Lời: Shangri-La Frontier bắt đầu là một tiểu thuyết đăng trên mạng, rồi thành manga và anime. Anime mùa một ra mắt…

```text
Wide 16:9 landscape cinematic frame. a web novel page glowing on a phone screen next to a manga volume and a TV remote, close-up, cozy light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s06

Lời: Và vì câu chuyện diễn ra trong một trò chơi, bảng chỉ số không phải thứ người xem phải đoán. Nó hiện ngay trê…

```text
Wide 16:9 landscape cinematic frame. a floating game interface overlay on a fantasy landscape, clearly readable bars and icons, wide shot, bright cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s07 · **Kaku** (đính kèm ảnh mẫu)

Lời: Mở sổ ra nào! Mình là Kaku. Hôm nay Kaku đọc bảng chỉ số của Shangri-La Frontier như đọc một nhân vật game th…

```text
Wide 16:9 landscape cinematic frame. the owl mascot wearing a tiny VR headset, pointing at a floating status window with a wing. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s08

Lời: Cuối video, Kaku có một trò chơi nhỏ: bạn sẽ tự lập thẻ chỉ số cho chính mình.

```text
Wide 16:9 landscape cinematic frame. a blank character sheet with empty stat bars and a pencil lying on it, top-down shot, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s09 · Thế giới game Shangri-La Frontier

Lời: Shangri-La Frontier là tên một trò chơi thực tế ảo toàn phần trong truyện. Người chơi đeo thiết bị, nằm xuống…

```text
Wide 16:9 landscape cinematic frame. a teenager lying on a bed wearing a sleek headset, a vast fantasy landscape unfolding above him like a dream, wide shot, soft blue and gold light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s10

Lời: Đây là trò chơi hot nhất trong thế giới của truyện, với hàng chục triệu người chơi. Thế giới rộng lớn, có cốt…

```text
Wide 16:9 landscape cinematic frame. a sprawling fantasy city with thousands of tiny adventurers in the streets, airships in the sky, wide aerial shot, bright golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s11

Lời: Game rác là những trò chơi mà người khác bỏ cuộc sau vài phút: điều khiển lỗi, va chạm vô lý, trùm đánh gục n…

```text
Wide 16:9 landscape cinematic frame. a frustrated gamer silhouette throwing a controller on a couch while another calmly keeps playing a chaotic glitchy game, split composition, humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s12

Lời: Nhân vật chính Hizutome Rakuro có một sở thích lạ: anh là thợ săn game rác. Anh chuyên chơi những trò chơi lỗ…

```text
Wide 16:9 landscape cinematic frame. a shelf full of cracked and weird-looking game cases with warning stickers, a satisfied player sitting in front of it, medium shot, dim room light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s13

Lời: Ngoài đời, Rakuro là một học sinh cấp ba bình thường. Không ai trong lớp biết rằng cậu là một trong những ngư…

```text
Wide 16:9 landscape cinematic frame. a high school classroom where a quiet student sits by the window, a faint glowing game icon reflected in his eyes, medium shot, daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s14

Lời: Sau khi phá đảo một trò chơi rác tới mức không còn gì để chơi, anh quyết định thử một game tử tế: Shangri-La…

```text
Wide 16:9 landscape cinematic frame. a player's hand choosing a character name on a glowing menu, the letters forming in light, close-up, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s15

Lời: Và chính những kỹ năng học được từ game rác, như né đòn trong hệ thống va chạm lỗi, hay đoán nhịp của những c…

```text
Wide 16:9 landscape cinematic frame. a split image: a pixelated glitchy game scene on the left, a sleek fantasy battle on the right, the same dodge motion in both, symmetrical composition. clean side-by-side panel composition, each part equally balanced. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s16

Lời: Luật số không này sẽ quay lại ở cuối video. Hãy nhớ nó khi Kaku đọc từng chỉ số.

```text
Wide 16:9 landscape cinematic frame. a small bookmark with the number zero placed between notebook pages, close-up, warm lamplight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s17 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú luật số không của video: trong Shangri-La Frontier, người chơi có hai loại sức mạnh. Chỉ số của…

```text
Wide 16:9 landscape cinematic frame. the owl mascot drawing two columns on a chalkboard labeled with a stat bar icon and a hand icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s18 · Chỉ số 1: sinh lực, ma lực và sức bền

Lời: Như nhiều game nhập vai, mỗi lần lên cấp, người chơi nhận một số điểm để tự chia vào các chỉ số. Mỗi lựa chọn…

```text
Wide 16:9 landscape cinematic frame. a level-up notification glowing above a character's head, a handful of floating points waiting to be assigned, close-up, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s19

Lời: Mở thẻ chỉ số ra. Ba thanh đầu tiên quen thuộc với mọi game thủ: sinh lực, về không là chết; ma lực, để dùng…

```text
Wide 16:9 landscape cinematic frame. three glowing horizontal bars in red, blue and green floating in the air, clean game interface style, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s20

Lời: Sức bền là thanh quan trọng hơn người ta nghĩ. Chạy, nhảy, né, tấn công đều tốn sức bền. Hết sức bền, nhân vậ…

```text
Wide 16:9 landscape cinematic frame. an adventurer bent over panting in the middle of a battlefield, a green bar flashing empty above his head, medium shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s21

Lời: Nhiều người chơi mới bỏ qua sức bền vì nó không làm con số sát thương to lên. Rồi họ ngạc nhiên khi nhân vật…

```text
Wide 16:9 landscape cinematic frame. a new player's character frozen mid-battle, panting, as a large boss swings toward it, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s22 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ngoài đời cũng có chỉ số sức bền rất thấp. Leo ba tầng cầu thang là thanh xanh đã nhấp nháy.

```text
Wide 16:9 landscape cinematic frame. the owl mascot panting at the top of a short staircase with a tiny green bar flashing above its head. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s23

Lời: Với một lối chơi dựa vào né tránh như Sunraku, sức bền chính là thời gian sống. Không né được nữa là không cò…

```text
Wide 16:9 landscape cinematic frame. a stopwatch overlaid on a green stamina bar that is draining, parchment diagram style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s24

Lời: Sunraku đầu tư khá nhiều vào sức bền, vì anh biết mình sẽ chạy và né suốt trận. Đây là lựa chọn đầu tiên cho…

```text
Wide 16:9 landscape cinematic frame. a player allocating glowing points into a green bar on a floating menu, satisfied expression reflected in the screen, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s25 · Chỉ số 2: sức mạnh và thể chất

Lời: Tiếp theo là sức mạnh, quyết định lực tấn công vật lý, và thể chất, quyết định khả năng chịu đòn.

```text
Wide 16:9 landscape cinematic frame. two stat icons, a fist and a shield, floating side by side above a character silhouette, clean interface style, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s26

Lời: Trong nhiều game trực tuyến, đó là lời khuyên chuẩn: chết là mất thời gian, mất vật phẩm. Cẩn thận là cách ch…

```text
Wide 16:9 landscape cinematic frame. a respawn point glowing in a town square with several annoyed adventurers reappearing, wide shot, bright light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s27

Lời: Hầu hết người chơi mới đều cân bằng hai chỉ số này, hoặc dồn vào thể chất cho an toàn. Chịu được đòn thì có t…

```text
Wide 16:9 landscape cinematic frame. a heavily armored knight silhouette calmly taking a hit from a monster, barely moving, medium shot, bright daylight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s28

Lời: Nhưng anh có lý do: những điểm không cho vào thể chất có thể dồn vào những chỉ số giúp anh không bao giờ bị đ…

```text
Wide 16:9 landscape cinematic frame. a diagram showing a big impact zone on the ground and a small figure already standing just outside it, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s29

Lời: Sunraku thì gần như bỏ trống thể chất: chỉ sáu điểm. Anh chấp nhận rằng bất kỳ đòn nào trúng cũng có thể giết…

```text
Wide 16:9 landscape cinematic frame. a stat bar labeled with a shield icon showing only a tiny sliver of fill, glowing warning red, extreme close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s30

Lời: Thêm vào đó là thói quen đội một chiếc mặt nạ kỳ quặc và ăn mặc gần như không có gì. Người chơi khác nhìn anh…

```text
Wide 16:9 landscape cinematic frame. a crowd of armored players staring and whispering at a lightly dressed masked stranger walking through a fantasy market, wide shot, humorous light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s31

Lời: Và mọi chuyện còn tệ hơn: anh bị trúng một lời nguyền khiến phần thân và chân không mặc được giáp. Nên hình ả…

```text
Wide 16:9 landscape cinematic frame. a lightly equipped adventurer silhouette standing bravely before a gigantic monster, armor slots on a floating menu crossed out in red, wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s32 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku nhìn bảng này và nghĩ: nếu Kaku chơi kiểu này, Kaku sẽ chết trước khi kịp mở bản đồ.

```text
Wide 16:9 landscape cinematic frame. the owl mascot peeking out from behind a very thick shield, holding a map it hasn't opened yet. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s33 · Chỉ số 3: nhanh nhẹn, khéo léo, kỹ thuật

Lời: Trong một thế giới thực tế ảo toàn phần, nhanh nhẹn không chỉ là con số. Người chơi cảm nhận tốc độ bằng chín…

```text
Wide 16:9 landscape cinematic frame. a first-person view of sprinting through a forest with trees rushing past, wind lines, dynamic shot, bright light. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s34

Lời: Nhóm chỉ số thứ ba là nơi Sunraku dồn phần lớn điểm. Nhanh nhẹn quyết định tốc độ di chuyển và phản ứng.

```text
Wide 16:9 landscape cinematic frame. a blurred adventurer darting between falling rocks in a canyon, speed lines trailing behind, dynamic wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s35

Lời: Khéo léo quyết định độ chính xác, còn kỹ thuật ảnh hưởng tới việc dùng kỹ năng, chiêu thức cho hiệu quả.

```text
Wide 16:9 landscape cinematic frame. a precise dagger strike hitting a tiny glowing weak point on a monster's armor, extreme close-up, amber highlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s36

Lời: Anh còn học được cách đọc hoạt ảnh của quái vật: nhìn cách chúng lấy đà là biết đòn sẽ rơi vào đâu. Kỹ năng n…

```text
Wide 16:9 landscape cinematic frame. a sequence of three frames showing a monster winding up, a small figure reading it, then dodging perfectly, parchment storyboard style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s37

Lời: Kaku để ý: đây là thứ mà nhiều game thủ ngoài đời cũng làm. Anime chỉ đẩy nó lên cực hạn.

```text
Wide 16:9 landscape cinematic frame. a real gamer leaning forward intently in front of a monitor, reflections of a boss animation in his glasses, close-up, blue screen light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s38

Lời: Với Sunraku, tốc độ là giáp. Nếu không bị đánh trúng, thể chất thấp cũng không sao. Đây là triết lý của các b…

```text
Wide 16:9 landscape cinematic frame. a diagram on parchment showing a large monster swing arc with a small figure stepping just outside it, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s39

Lời: Nhưng tốc độ trong game chỉ có ý nghĩa nếu người chơi phản xạ kịp. Chỉ số cho nhân vật khả năng chạy nhanh, c…

```text
Wide 16:9 landscape cinematic frame. a player's real hands gripping nothing in the dark, a faint reflection of a fast in-game dodge in his visor, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s40

Lời: Ở đây ta thấy rõ luật số không: nhanh nhẹn cao chỉ là tiềm năng. Kỹ năng của Rakuro ngoài đời thật mới biến t…

```text
Wide 16:9 landscape cinematic frame. two connected gears labeled with a stat icon and a human hand icon, turning together, parchment illustration, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s41 · Chỉ số 4: may mắn

Lời: Nhiều người chơi coi may mắn là chỉ số vô dụng, vì nó không hiện ra ngay trong mỗi đòn. Sunraku thì hiểu rằng…

```text
Wide 16:9 landscape cinematic frame. a tally board of golden critical hit marks accumulating over a long battle timeline, parchment diagram, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s42

Lời: Chỉ số cuối cùng mà Sunraku đầu tư mạnh là may mắn. Trong game, may mắn làm tăng tỉ lệ đòn chí mạng và cơ hội…

```text
Wide 16:9 landscape cinematic frame. a glowing four-leaf clover icon floating above a treasure chest that spills rare items, close-up, golden light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s43

Lời: Anh còn chọn nghề Lữ khách, một nghề có sức phòng thủ kém nhưng được thưởng thêm điểm may mắn. Mọi lựa chọn đ…

```text
Wide 16:9 landscape cinematic frame. a wanderer silhouette with a light travel cloak and a walking staff on a winding road, a lucky star glowing above, wide shot, soft light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s44

Lời: Vũ khí của anh thường là những thanh kiếm ngắn, nhẹ, đánh nhanh. Chúng không mạnh bằng kiếm lớn, nhưng hợp vớ…

```text
Wide 16:9 landscape cinematic frame. two short light blades crossed on a wooden table beside a small pouch of potions, close-up, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s45

Lời: Đòn chí mạng quan trọng với Sunraku vì anh không có sức mạnh để đánh lâu. Anh cần mỗi đòn trúng đều gây thiệt…

```text
Wide 16:9 landscape cinematic frame. a single precise strike causing a burst of golden critical sparks on a giant monster, dynamic close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s46

Lời: Nhưng may mắn trong Shangri-La Frontier còn có một ý nghĩa lớn hơn con số: gặp đúng người, đúng lúc. Và cú ma…

```text
Wide 16:9 landscape cinematic frame. a small elegantly dressed rabbit character bowing politely in a moonlit alley, medium shot, soft magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s47

Lời: Đó là Emul, một cô thỏ thuộc tộc thỏ Vorpal, người mở ra cho Sunraku một kịch bản độc nhất mà không người chơ…

```text
Wide 16:9 landscape cinematic frame. a small rabbit character opening a glowing magical door in the middle of a forest, light spilling out, wide shot, enchanting light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s48 · Bản xây dựng của Sunraku

Lời: Giờ ghép lại bản xây dựng của Sunraku. Sức bền cao để chạy lâu. Nhanh nhẹn và khéo léo cao để né và đánh trún…

```text
Wide 16:9 landscape cinematic frame. a radar chart with sharp spikes on speed, dexterity, luck and stamina and a tiny dent on vitality, parchment style, amber ink. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s49

Lời: Và bản xây dựng này thay đổi dần theo thời gian. Khi gặp những thử thách mới, Sunraku sẵn sàng điều chỉnh, đổ…

```text
Wide 16:9 landscape cinematic frame. a character sheet with several versions layered on top of each other, some stats crossed out and rewritten, close-up, amber ink. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s50

Lời: Trong ngôn ngữ game thủ, đây là một bản xây dựng pháo thủy tinh: sát thương cao, tốc độ cao, nhưng vỡ ngay kh…

```text
Wide 16:9 landscape cinematic frame. a delicate glass cannon firing a bright shot, cracks already visible on its barrel, humorous still life, bright light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s51

Lời: Nhưng nó không phải một lựa chọn liều lĩnh. Nó là lựa chọn của người biết chính xác điểm mạnh của mình: phản…

```text
Wide 16:9 landscape cinematic frame. a player surrounded by floating memories of weird glitchy game bosses, each one dodged, medium shot, cyan light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s52 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku rút ra bài học đầu tiên: bảng chỉ số tốt nhất không phải bảng cân bằng nhất, mà là bảng hợp với người ch…

```text
Wide 16:9 landscape cinematic frame. the owl mascot writing a bold line in its notebook and underlining it twice. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s53 · Xếp hạng: điều gì quyết định thắng thua?

Lời: Theo đúng khung của dạng video này, Kaku xếp hạng những thứ quyết định thắng thua trong Shangri-La Frontier,…

```text
Wide 16:9 landscape cinematic frame. a podium with four steps and empty placards, spotlight on it, wide shot, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s54

Lời: Hạng tư: chỉ số. Quan trọng, nhưng ai chơi lâu cũng có chỉ số cao. Nó là nền, không phải lợi thế.

```text
Wide 16:9 landscape cinematic frame. a placard with a stat bar icon placed on the lowest step of the podium, close-up. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s55

Lời: Nhưng cũng phải công bằng: một số vũ khí đặc biệt, có được nhờ nhiệm vụ độc nhất, đã giúp Sunraku rất nhiều.…

```text
Wide 16:9 landscape cinematic frame. a unique glowing blade resting on an altar inside a hidden rabbit village, close-up, magical light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s56

Lời: Hạng ba: trang bị. Vũ khí và giáp mạnh thay đổi được nhiều thứ. Nhưng Sunraku bị nguyền không mặc được giáp,…

```text
Wide 16:9 landscape cinematic frame. a placard with a sword and armor icon on the third step, a small curse mark stamped beside it, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s57

Lời: Arthur Pencilgon, bạn cũ của Rakuro, là bậc thầy về thông tin và mưu kế. Cô nổi tiếng là kẻ chuyên hạ gục ngư…

```text
Wide 16:9 landscape cinematic frame. an elegant player silhouette with a sly smile sitting on a throne of stacked scrolls in a dim tavern, medium shot, warm candlelight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s58

Lời: Hạng nhì: thông tin. Trong một thế giới rộng lớn, biết một bí mật như cách vào làng thỏ, hay điều kiện để đán…

```text
Wide 16:9 landscape cinematic frame. a placard with a scroll and key icon on the second step, glowing faintly, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s59

Lời: Hạng nhất: kỹ năng của con người thật. Phản xạ, bình tĩnh, khả năng đọc nhịp đối thủ. Thứ mà Rakuro mang từ n…

```text
Wide 16:9 landscape cinematic frame. a placard with a human hand icon on the top step bathed in golden light, close-up. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s60

Lời: Ba người Sunraku, Pencilgon và Oikatzo khi hợp lại là một đội đáng sợ: một người né giỏi, một người mưu mẹo,…

```text
Wide 16:9 landscape cinematic frame. three player silhouettes standing back to back on a hill: a light masked figure, a scheming figure, a composed pro gamer, wide shot, dramatic sunset. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s61

Lời: Bạn của Rakuro, Oikatzo, là một game thủ chuyên nghiệp ngoài đời, và bản thân điều đó đã nói lên tất cả: tron…

```text
Wide 16:9 landscape cinematic frame. a focused professional gamer silhouette in a tournament booth with headphones, audience lights in the background, medium shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s62 · Giới hạn của những con số

Lời: Nhưng bảng chỉ số cũng có giới hạn. Giới hạn thứ nhất: quái vật độc nhất. Trò chơi có những con trùm đặc biệt…

```text
Wide 16:9 landscape cinematic frame. a colossal ghostly armored warrior rising from a misty graveyard under a full moon, a tiny adventurer facing it, wide epic shot. medium shot, expressive body language, strong readable silhouette. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s63

Lời: Hai mươi phút có thể không dài khi bạn xem phim. Nhưng thử tưởng tượng hai mươi phút liên tục né đòn của một…

```text
Wide 16:9 landscape cinematic frame. a close-up of a focused player's eyes reflecting countless sword slashes, sweat on the brow, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s64

Lời: Trận đấu với Wethermon, hiệp sĩ canh mộ, là ví dụ rõ nhất. Người chơi phải sống sót hai mươi phút trước khi t…

```text
Wide 16:9 landscape cinematic frame. an hourglass with twenty minutes marked on it placed in front of a massive ghostly knight, symbolic composition, silver light. close-up detail shot with shallow depth of field. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s65

Lời: Giới hạn thứ hai: những lời nguyền và hiệu ứng đặc biệt. Lời nguyền của Lycagon, con sói săn đêm, không chỉ c…

```text
Wide 16:9 landscape cinematic frame. a glowing crescent-shaped curse mark on an adventurer's back, small monsters fleeing in the background, medium shot, eerie moonlight. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s66

Lời: Ở mùa hai, người chơi còn phải hợp sức trong những trận đánh tập thể với quái vật khổng lồ. Khi đó, khả năng…

```text
Wide 16:9 landscape cinematic frame. a large group of adventurers coordinating an attack on a colossal sea creature at night, commanders signaling from rocks, wide epic shot. wide establishing shot with deep perspective. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s67

Lời: Một hiệu ứng vừa là điểm yếu, vừa là lợi thế. Bảng chỉ số không thể đánh giá nó bằng một con số cộng hay trừ.

```text
Wide 16:9 landscape cinematic frame. a coin spinning in the air showing a curse mark on one side and a key on the other, close-up, dramatic light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s68

Lời: Kaku rất thích chi tiết này: người chơi mạnh nhất lại có bạn thân là một con thỏ. Và tình bạn đó mở ra cả một…

```text
Wide 16:9 landscape cinematic frame. a masked player and a small elegantly dressed rabbit sitting together on a hill watching shooting stars, back view, soft night light. cinematic medium-wide shot, rule-of-thirds composition. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s69

Lời: Giới hạn thứ ba: các nhân vật trong game như có linh hồn. Emul và tộc thỏ Vorpal có tính cách, cảm xúc, ký ức…

```text
Wide 16:9 landscape cinematic frame. a cozy rabbit village with tiny houses and lanterns at night, a player sitting and laughing with rabbit characters around a fire, wide shot, warm light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s70 · **Kaku** (đính kèm ảnh mẫu)

Lời: Kaku ghi chú: Shangri-La Frontier dùng bảng chỉ số để nói rằng những thứ quan trọng nhất trong trò chơi, cũng…

```text
Wide 16:9 landscape cinematic frame. the owl mascot closing a floating status window and looking at a small rabbit waving at it. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s71 · Trò chơi: thẻ chỉ số của bạn

Lời: Giờ tới lượt bạn. Kaku cho bạn ba mươi điểm để chia vào sáu chỉ số: sinh lực, sức bền, sức mạnh, thể chất, nh…

```text
Wide 16:9 landscape cinematic frame. a blank character sheet with six empty stat bars and a small pile of thirty glowing tokens beside it, top-down shot. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s72

Lời: Một gợi ý nhỏ: đừng chia đều. Hãy thử làm như Sunraku, chọn một hai điểm mạnh thật rõ và chấp nhận một điểm y…

```text
Wide 16:9 landscape cinematic frame. a lopsided character sheet with two very tall bars and one tiny bar, a small star sticker on it, close-up. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s73

Lời: Bạn là kiểu người chịu đòn giỏi và kiên trì? Dồn vào thể chất. Bạn phản xạ nhanh? Dồn vào nhanh nhẹn. Bạn hay…

```text
Wide 16:9 landscape cinematic frame. three small sketches: a sturdy person, a quick person dodging a ball, a person holding a winning lottery ticket, parchment style. medium shot, expressive body language, strong readable silhouette. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s74

Lời: Và chọn một nghề cho mình: chiến binh, pháp sư, lữ khách, hay một nghề bạn tự nghĩ ra. Viết thẻ chỉ số của bạ…

```text
Wide 16:9 landscape cinematic frame. a row of four job class icons: a sword, a staff, a walking stick and a question mark, clean interface style. clean centered composition with the diagram as the clear focal point, flat front view, generous negative space. diagram lines glowing softly in white and amber, deep navy surroundings. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s75 · **Kaku** (đính kèm ảnh mẫu)

Lời: Thẻ của Kaku đây: may mắn hai điểm, thể chất hai điểm, và hai mươi sáu điểm vào… đọc sách. Chỉ số này không c…

```text
Wide 16:9 landscape cinematic frame. the owl mascot proudly showing a character sheet with one huge bar labeled with a book icon. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s76 · Kết

Lời: Và đó cũng là một lời nhắn cho người xem: đừng để con số định nghĩa bạn. Chỉ số của bạn ngoài đời có thể thấp…

```text
Wide 16:9 landscape cinematic frame. a person walking up a mountain path at sunrise with a small floating stat card behind them fading away, wide shot, warm hopeful light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s77

Lời: Shangri-La Frontier cho ta một bảng chỉ số rất chi tiết, rồi dành cả câu chuyện để chứng minh rằng con người…

```text
Wide 16:9 landscape cinematic frame. a player taking off a VR headset at dawn, smiling tiredly, the fantasy world fading from his eyes, close-up, soft morning light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s78

Lời: Mùa ba lên sóng trong tháng một. Xem xong, hãy thử để ý xem Sunraku có thay đổi bản xây dựng của mình không,…

```text
Wide 16:9 landscape cinematic frame. a calendar page for January with a small game controller doodle on a date, close-up, fresh light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s79

Lời: Video tiếp theo, Kaku tiếp tục ôn tập trước mùa mới, lần này là Mashle: thế giới nơi phép thuật quyết định đị…

```text
Wide 16:9 landscape cinematic frame. a magic academy courtyard with students casting sparkles from wands while one muscular boy lifts a huge stone pillar, humorous wide shot. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
```

### s80 · **Kaku** (đính kèm ảnh mẫu)

Lời: Nếu bạn là game thủ và thích kiểu phân tích này, hãy đăng ký kênh để Kaku đọc thêm nhiều bảng chỉ số nữa. Kak…

```text
Wide 16:9 landscape cinematic frame. the owl mascot taking off its tiny VR headset and waving goodbye. The channel mascot: a small round owl scholar mascot with fluffy brown-and-cream feathers, oversized round golden glasses, a red knitted scarf, holding a rolled parchment scroll, big expressive amber eyes, chibi proportions, original character design. medium shot at eye level, the mascot in sharp focus in the foreground. moody cinematic lighting, warm amber key light, cool navy shadows, soft rim light. Signature "Kaku field notebook" look: modern anime illustration, cel-shaded with clean confident line art, faint hand-inked sketch marks and a subtle warm parchment grain toward the edges of the frame, palette of deep navy shadows, warm amber-gold highlights and a single small crimson accent, strong rim light, painterly atmospheric depth, original characters only. No text, no letters, no logos, no watermark, no signature. Original character designs only, not resembling any existing anime or manga character.
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

Khoảng 87 giây · cảnh s01–s08 · 1134 ký tự

**Gemini**

```text
Cảnh báo: video có spoiler Shangri-La Frontier tới hết anime mùa hai. Mùa ba ra mắt tháng một này, và Kaku không nói gì về nội dung của nó.

<short pause> Đây là thẻ chỉ số của một người chơi. Sức bền khá. Sức mạnh vừa phải. Nhanh nhẹn rất cao. May mắn rất cao. Còn thể chất? Sáu điểm. Mỏng như một tờ giấy.

<short pause> Nếu bạn chơi game nhập vai, bạn sẽ nói ngay: đây là một bản xây dựng nhân vật tồi tệ. Chỉ cần một cú đánh là chết.

<short pause> Nhưng chủ nhân của thẻ chỉ số này đã sống sót trước những con quái vật mạnh nhất trò chơi, những thứ mà cả nghìn người chơi khác chưa từng chạm tới.

<short pause> Shangri-La Frontier bắt đầu là một tiểu thuyết đăng trên mạng, rồi thành manga và anime. Anime mùa một ra mắt năm 2023, mùa hai tiếp nối ngay sau đó.

<short pause> Và vì câu chuyện diễn ra trong một trò chơi, bảng chỉ số không phải thứ người xem phải đoán. Nó hiện ngay trên màn hình, như khi chính bạn đang chơi.

<short pause> Mở sổ ra nào! <laugh> Mình là Kaku. Hôm nay Kaku đọc bảng chỉ số của Shangri-La Frontier như đọc một nhân vật game thật: từng chỉ số làm gì, vì sao Sunraku xây nhân vật như vậy, và giới hạn của những con số ở đâu.

<short pause> Cuối video, Kaku có một trò chơi nhỏ: bạn sẽ tự lập thẻ chỉ số cho chính mình.
```

**ElevenLabs**

```text
Cảnh báo: video có spoiler Shangri-La Frontier tới hết anime mùa hai. Mùa ba ra mắt tháng một này, và Kaku không nói gì về nội dung của nó.

[pause] Đây là thẻ chỉ số của một người chơi. Sức bền khá. Sức mạnh vừa phải. Nhanh nhẹn rất cao. May mắn rất cao. [curious] Còn thể chất? Sáu điểm. Mỏng như một tờ giấy.

[pause] Nếu bạn chơi game nhập vai, bạn sẽ nói ngay: đây là một bản xây dựng nhân vật tồi tệ. Chỉ cần một cú đánh là chết.

[pause] Nhưng chủ nhân của thẻ chỉ số này đã sống sót trước những con quái vật mạnh nhất trò chơi, những thứ mà cả nghìn người chơi khác chưa từng chạm tới.

[pause] Shangri-La Frontier bắt đầu là một tiểu thuyết đăng trên mạng, rồi thành manga và anime. Anime mùa một ra mắt năm 2023, mùa hai tiếp nối ngay sau đó.

[pause] Và vì câu chuyện diễn ra trong một trò chơi, bảng chỉ số không phải thứ người xem phải đoán. Nó hiện ngay trên màn hình, như khi chính bạn đang chơi.

[pause] Mở sổ ra nào! [chuckles] Mình là Kaku. Hôm nay Kaku đọc bảng chỉ số của Shangri-La Frontier như đọc một nhân vật game thật: từng chỉ số làm gì, vì sao Sunraku xây nhân vật như vậy, và giới hạn của những con số ở đâu.

[pause] Cuối video, Kaku có một trò chơi nhỏ: bạn sẽ tự lập thẻ chỉ số cho chính mình.
```

### c02 · Thế giới game Shangri-La Frontier

Khoảng 108 giây · cảnh s09–s17 · 1403 ký tự

**Gemini**

```text
Shangri-La Frontier là tên một trò chơi thực tế ảo toàn phần trong truyện. Người chơi đeo thiết bị, nằm xuống, và cả năm giác quan đi vào thế giới game.

<short pause> Đây là trò chơi hot nhất trong thế giới của truyện, với hàng chục triệu người chơi. Thế giới rộng lớn, có cốt truyện riêng, và những nhân vật không phải người chơi thông minh tới mức như người thật.

<short pause> Game rác là những trò chơi mà người khác bỏ cuộc sau vài phút: điều khiển lỗi, va chạm vô lý, trùm đánh gục người chơi chỉ trong một đòn. Với Rakuro, chúng là những bài kiểm tra phản xạ.

<short pause> Nhân vật chính Hizutome Rakuro có một sở thích lạ: anh là thợ săn game rác. Anh chuyên chơi những trò chơi lỗi, khó chịu, thiết kế tệ, và phá đảo chúng.

<short pause> Ngoài đời, Rakuro là một học sinh cấp ba bình thường. Không ai trong lớp biết rằng cậu là một trong những người chơi đáng gờm nhất của trò chơi đình đám nhất.

<short pause> Sau khi phá đảo một trò chơi rác tới mức không còn gì để chơi, anh quyết định thử một game tử tế: Shangri-La Frontier. Tên nhân vật của anh là Sunraku.

<short pause> Và chính những kỹ năng học được từ game rác, như né đòn trong hệ thống va chạm lỗi, hay đoán nhịp của những con trùm vô lý, trở thành vũ khí mạnh nhất của anh.

<short pause> Luật số không này sẽ quay lại ở cuối video. Hãy nhớ nó khi Kaku đọc từng chỉ số.

<short pause> <laugh> Kaku ghi chú luật số không của video: trong Shangri-La Frontier, người chơi có hai loại sức mạnh. Chỉ số của nhân vật, và kỹ năng thật của con người ngồi sau nhân vật.
```

**ElevenLabs**

```text
Shangri-La Frontier là tên một trò chơi thực tế ảo toàn phần trong truyện. Người chơi đeo thiết bị, nằm xuống, và cả năm giác quan đi vào thế giới game.

[pause] Đây là trò chơi hot nhất trong thế giới của truyện, với hàng chục triệu người chơi. Thế giới rộng lớn, có cốt truyện riêng, và những nhân vật không phải người chơi thông minh tới mức như người thật.

[pause] Game rác là những trò chơi mà người khác bỏ cuộc sau vài phút: điều khiển lỗi, va chạm vô lý, trùm đánh gục người chơi chỉ trong một đòn. Với Rakuro, chúng là những bài kiểm tra phản xạ.

[pause] Nhân vật chính Hizutome Rakuro có một sở thích lạ: anh là thợ săn game rác. Anh chuyên chơi những trò chơi lỗi, khó chịu, thiết kế tệ, và phá đảo chúng.

[pause] Ngoài đời, Rakuro là một học sinh cấp ba bình thường. Không ai trong lớp biết rằng cậu là một trong những người chơi đáng gờm nhất của trò chơi đình đám nhất.

[pause] Sau khi phá đảo một trò chơi rác tới mức không còn gì để chơi, anh quyết định thử một game tử tế: Shangri-La Frontier. Tên nhân vật của anh là Sunraku.

[pause] Và chính những kỹ năng học được từ game rác, như né đòn trong hệ thống va chạm lỗi, hay đoán nhịp của những con trùm vô lý, trở thành vũ khí mạnh nhất của anh.

[pause] Luật số không này sẽ quay lại ở cuối video. Hãy nhớ nó khi Kaku đọc từng chỉ số.

[pause] [chuckles] Kaku ghi chú luật số không của video: trong Shangri-La Frontier, người chơi có hai loại sức mạnh. Chỉ số của nhân vật, và kỹ năng thật của con người ngồi sau nhân vật.
```

### c03 · Chỉ số 1: sinh lực, ma lực và sức bền

Khoảng 73 giây · cảnh s18–s24 · 953 ký tự

**Gemini**

```text
Như nhiều game nhập vai, mỗi lần lên cấp, người chơi nhận một số điểm để tự chia vào các chỉ số. Mỗi lựa chọn chia điểm là một lời tuyên bố về cách mình muốn chơi.

<short pause> Mở thẻ chỉ số ra. Ba thanh đầu tiên quen thuộc với mọi game thủ: sinh lực, về không là chết; ma lực, để dùng phép và kỹ năng; và sức bền.

<short pause> Sức bền là thanh quan trọng hơn người ta nghĩ. Chạy, nhảy, né, tấn công đều tốn sức bền. Hết sức bền, nhân vật đứng thở hồng hộc giữa trận.

<short pause> Nhiều người chơi mới bỏ qua sức bền vì nó không làm con số sát thương to lên. Rồi họ ngạc nhiên khi nhân vật đứng thở dốc đúng lúc con trùm vung đòn.

<short pause> <laugh> Kaku ngoài đời cũng có chỉ số sức bền rất thấp. Leo ba tầng cầu thang là thanh xanh đã nhấp nháy.

<short pause> Với một lối chơi dựa vào né tránh như Sunraku, sức bền chính là thời gian sống. Không né được nữa là không còn gì để bảo vệ.

<short pause> Sunraku đầu tư khá nhiều vào sức bền, vì anh biết mình sẽ chạy và né suốt trận. Đây là lựa chọn đầu tiên cho thấy anh hiểu rõ lối chơi của mình.
```

**ElevenLabs**

```text
Như nhiều game nhập vai, mỗi lần lên cấp, người chơi nhận một số điểm để tự chia vào các chỉ số. Mỗi lựa chọn chia điểm là một lời tuyên bố về cách mình muốn chơi.

[pause] Mở thẻ chỉ số ra. Ba thanh đầu tiên quen thuộc với mọi game thủ: sinh lực, về không là chết; ma lực, để dùng phép và kỹ năng; và sức bền.

[pause] Sức bền là thanh quan trọng hơn người ta nghĩ. Chạy, nhảy, né, tấn công đều tốn sức bền. Hết sức bền, nhân vật đứng thở hồng hộc giữa trận.

[pause] Nhiều người chơi mới bỏ qua sức bền vì nó không làm con số sát thương to lên. Rồi họ ngạc nhiên khi nhân vật đứng thở dốc đúng lúc con trùm vung đòn.

[pause] [chuckles] Kaku ngoài đời cũng có chỉ số sức bền rất thấp. Leo ba tầng cầu thang là thanh xanh đã nhấp nháy.

[pause] Với một lối chơi dựa vào né tránh như Sunraku, sức bền chính là thời gian sống. Không né được nữa là không còn gì để bảo vệ.

[pause] Sunraku đầu tư khá nhiều vào sức bền, vì anh biết mình sẽ chạy và né suốt trận. Đây là lựa chọn đầu tiên cho thấy anh hiểu rõ lối chơi của mình.
```

### c04 · Chỉ số 2: sức mạnh và thể chất

Khoảng 86 giây · cảnh s25–s32 · 1117 ký tự

**Gemini**

```text
Tiếp theo là sức mạnh, quyết định lực tấn công vật lý, và thể chất, quyết định khả năng chịu đòn.

<short pause> Trong nhiều game trực tuyến, đó là lời khuyên chuẩn: chết là mất thời gian, mất vật phẩm. Cẩn thận là cách chơi an toàn nhất.

<short pause> Hầu hết người chơi mới đều cân bằng hai chỉ số này, hoặc dồn vào thể chất cho an toàn. Chịu được đòn thì có thêm thời gian để sửa sai.

<short pause> Nhưng anh có lý do: những điểm không cho vào thể chất có thể dồn vào những chỉ số giúp anh không bao giờ bị đánh trúng. Với anh, phòng thủ tốt nhất là không có mặt ở chỗ đòn đánh rơi xuống.

<short pause> Sunraku thì gần như bỏ trống thể chất: chỉ sáu điểm. Anh chấp nhận rằng bất kỳ đòn nào trúng cũng có thể giết mình.

<short pause> Thêm vào đó là thói quen đội một chiếc mặt nạ kỳ quặc và ăn mặc gần như không có gì. Người chơi khác nhìn anh như một kẻ lập dị, cho tới khi thấy anh chiến đấu.

<short pause> Và mọi chuyện còn tệ hơn: anh bị trúng một lời nguyền khiến phần thân và chân không mặc được giáp. Nên hình ảnh quen thuộc của Sunraku là một người chơi gần như không có giáp giữa những con quái vật khổng lồ.

<short pause> <laugh> Kaku nhìn bảng này và nghĩ: nếu Kaku chơi kiểu này, Kaku sẽ chết trước khi kịp mở bản đồ.
```

**ElevenLabs**

```text
Tiếp theo là sức mạnh, quyết định lực tấn công vật lý, và thể chất, quyết định khả năng chịu đòn.

[pause] Trong nhiều game trực tuyến, đó là lời khuyên chuẩn: chết là mất thời gian, mất vật phẩm. Cẩn thận là cách chơi an toàn nhất.

[pause] Hầu hết người chơi mới đều cân bằng hai chỉ số này, hoặc dồn vào thể chất cho an toàn. Chịu được đòn thì có thêm thời gian để sửa sai.

[pause] Nhưng anh có lý do: những điểm không cho vào thể chất có thể dồn vào những chỉ số giúp anh không bao giờ bị đánh trúng. Với anh, phòng thủ tốt nhất là không có mặt ở chỗ đòn đánh rơi xuống.

[pause] Sunraku thì gần như bỏ trống thể chất: chỉ sáu điểm. Anh chấp nhận rằng bất kỳ đòn nào trúng cũng có thể giết mình.

[pause] Thêm vào đó là thói quen đội một chiếc mặt nạ kỳ quặc và ăn mặc gần như không có gì. Người chơi khác nhìn anh như một kẻ lập dị, cho tới khi thấy anh chiến đấu.

[pause] Và mọi chuyện còn tệ hơn: anh bị trúng một lời nguyền khiến phần thân và chân không mặc được giáp. Nên hình ảnh quen thuộc của Sunraku là một người chơi gần như không có giáp giữa những con quái vật khổng lồ.

[pause] [chuckles] Kaku nhìn bảng này và nghĩ: nếu Kaku chơi kiểu này, Kaku sẽ chết trước khi kịp mở bản đồ.
```

### c05 · Chỉ số 3: nhanh nhẹn, khéo léo, kỹ thuật

Khoảng 80 giây · cảnh s33–s40 · 1036 ký tự

**Gemini**

```text
Trong một thế giới thực tế ảo toàn phần, nhanh nhẹn không chỉ là con số. Người chơi cảm nhận tốc độ bằng chính cơ thể mình, như đang chạy thật.

<short pause> Nhóm chỉ số thứ ba là nơi Sunraku dồn phần lớn điểm. Nhanh nhẹn quyết định tốc độ di chuyển và phản ứng.

<short pause> Khéo léo quyết định độ chính xác, còn kỹ thuật ảnh hưởng tới việc dùng kỹ năng, chiêu thức cho hiệu quả.

<short pause> Anh còn học được cách đọc hoạt ảnh của quái vật: nhìn cách chúng lấy đà là biết đòn sẽ rơi vào đâu. Kỹ năng này anh luyện từ những trùm vô lý trong game rác.

<short pause> Kaku để ý: đây là thứ mà nhiều game thủ ngoài đời cũng làm. Anime chỉ đẩy nó lên cực hạn.

<short pause> Với Sunraku, tốc độ là giáp. Nếu không bị đánh trúng, thể chất thấp cũng không sao. Đây là triết lý của các bản xây dựng né tránh trong game nhập vai.

<short pause> Nhưng tốc độ trong game chỉ có ý nghĩa nếu người chơi phản xạ kịp. Chỉ số cho nhân vật khả năng chạy nhanh, còn con người ngồi sau phải biết chạy về đâu.

<short pause> Ở đây ta thấy rõ luật số không: nhanh nhẹn cao chỉ là tiềm năng. Kỹ năng của Rakuro ngoài đời thật mới biến tiềm năng đó thành sống sót.
```

**ElevenLabs**

```text
Trong một thế giới thực tế ảo toàn phần, nhanh nhẹn không chỉ là con số. Người chơi cảm nhận tốc độ bằng chính cơ thể mình, như đang chạy thật.

[pause] Nhóm chỉ số thứ ba là nơi Sunraku dồn phần lớn điểm. Nhanh nhẹn quyết định tốc độ di chuyển và phản ứng.

[pause] Khéo léo quyết định độ chính xác, còn kỹ thuật ảnh hưởng tới việc dùng kỹ năng, chiêu thức cho hiệu quả.

[pause] Anh còn học được cách đọc hoạt ảnh của quái vật: nhìn cách chúng lấy đà là biết đòn sẽ rơi vào đâu. Kỹ năng này anh luyện từ những trùm vô lý trong game rác.

[pause] Kaku để ý: đây là thứ mà nhiều game thủ ngoài đời cũng làm. Anime chỉ đẩy nó lên cực hạn.

[pause] Với Sunraku, tốc độ là giáp. Nếu không bị đánh trúng, thể chất thấp cũng không sao. Đây là triết lý của các bản xây dựng né tránh trong game nhập vai.

[pause] Nhưng tốc độ trong game chỉ có ý nghĩa nếu người chơi phản xạ kịp. Chỉ số cho nhân vật khả năng chạy nhanh, còn con người ngồi sau phải biết chạy về đâu.

[pause] Ở đây ta thấy rõ luật số không: nhanh nhẹn cao chỉ là tiềm năng. Kỹ năng của Rakuro ngoài đời thật mới biến tiềm năng đó thành sống sót.
```

### c06 · Chỉ số 4: may mắn / Bản xây dựng của Sunraku

Khoảng 138 giây · cảnh s41–s52 · 1797 ký tự

**Gemini**

```text
Nhiều người chơi coi may mắn là chỉ số vô dụng, vì nó không hiện ra ngay trong mỗi đòn. Sunraku thì hiểu rằng trong một trận dài, những lần chí mạng cộng dồn lại sẽ tạo khác biệt lớn.

<short pause> Chỉ số cuối cùng mà Sunraku đầu tư mạnh là may mắn. Trong game, may mắn làm tăng tỉ lệ đòn chí mạng và cơ hội nhận vật phẩm hiếm.

<short pause> Anh còn chọn nghề Lữ khách, một nghề có sức phòng thủ kém nhưng được thưởng thêm điểm may mắn. Mọi lựa chọn đều nhất quán: bỏ thủ, lấy công và cơ hội.

<short pause> Vũ khí của anh thường là những thanh kiếm ngắn, nhẹ, đánh nhanh. Chúng không mạnh bằng kiếm lớn, nhưng hợp với cách đánh chớp nhoáng rồi rút lui.

<short pause> Đòn chí mạng quan trọng với Sunraku vì anh không có sức mạnh để đánh lâu. Anh cần mỗi đòn trúng đều gây thiệt hại lớn nhất có thể, rồi né đi.

<short pause> Nhưng may mắn trong Shangri-La Frontier còn có một ý nghĩa lớn hơn con số: gặp đúng người, đúng lúc. Và cú may mắn lớn nhất của Sunraku đến từ một con thỏ.

<short pause> Đó là Emul, một cô thỏ thuộc tộc thỏ Vorpal, người mở ra cho Sunraku một kịch bản độc nhất mà không người chơi nào khác có. Không có chỉ số nào ghi được điều đó.

<short pause> Giờ ghép lại bản xây dựng của Sunraku. Sức bền cao để chạy lâu. Nhanh nhẹn và khéo léo cao để né và đánh trúng. May mắn cao để chí mạng. Thể chất gần như bằng không.

<short pause> Và bản xây dựng này thay đổi dần theo thời gian. Khi gặp những thử thách mới, Sunraku sẵn sàng điều chỉnh, đổi nghề, đổi vũ khí. Không có bảng chỉ số nào là mãi mãi.

<short pause> Trong ngôn ngữ game thủ, đây là một bản xây dựng pháo thủy tinh: sát thương cao, tốc độ cao, nhưng vỡ ngay khi bị chạm vào.

<short pause> Nhưng nó không phải một lựa chọn liều lĩnh. Nó là lựa chọn của người biết chính xác điểm mạnh của mình: phản xạ và kinh nghiệm né đòn từ hàng trăm trò chơi tệ hại.

<short pause> <laugh> Kaku rút ra bài học đầu tiên: bảng chỉ số tốt nhất không phải bảng cân bằng nhất, mà là bảng hợp với người chơi nhất.
```

**ElevenLabs**

```text
Nhiều người chơi coi may mắn là chỉ số vô dụng, vì nó không hiện ra ngay trong mỗi đòn. Sunraku thì hiểu rằng trong một trận dài, những lần chí mạng cộng dồn lại sẽ tạo khác biệt lớn.

[pause] Chỉ số cuối cùng mà Sunraku đầu tư mạnh là may mắn. Trong game, may mắn làm tăng tỉ lệ đòn chí mạng và cơ hội nhận vật phẩm hiếm.

[pause] Anh còn chọn nghề Lữ khách, một nghề có sức phòng thủ kém nhưng được thưởng thêm điểm may mắn. Mọi lựa chọn đều nhất quán: bỏ thủ, lấy công và cơ hội.

[pause] Vũ khí của anh thường là những thanh kiếm ngắn, nhẹ, đánh nhanh. Chúng không mạnh bằng kiếm lớn, nhưng hợp với cách đánh chớp nhoáng rồi rút lui.

[pause] Đòn chí mạng quan trọng với Sunraku vì anh không có sức mạnh để đánh lâu. Anh cần mỗi đòn trúng đều gây thiệt hại lớn nhất có thể, rồi né đi.

[pause] Nhưng may mắn trong Shangri-La Frontier còn có một ý nghĩa lớn hơn con số: gặp đúng người, đúng lúc. Và cú may mắn lớn nhất của Sunraku đến từ một con thỏ.

[pause] Đó là Emul, một cô thỏ thuộc tộc thỏ Vorpal, người mở ra cho Sunraku một kịch bản độc nhất mà không người chơi nào khác có. Không có chỉ số nào ghi được điều đó.

[pause] Giờ ghép lại bản xây dựng của Sunraku. Sức bền cao để chạy lâu. Nhanh nhẹn và khéo léo cao để né và đánh trúng. May mắn cao để chí mạng. Thể chất gần như bằng không.

[pause] Và bản xây dựng này thay đổi dần theo thời gian. Khi gặp những thử thách mới, Sunraku sẵn sàng điều chỉnh, đổi nghề, đổi vũ khí. Không có bảng chỉ số nào là mãi mãi.

[pause] Trong ngôn ngữ game thủ, đây là một bản xây dựng pháo thủy tinh: sát thương cao, tốc độ cao, nhưng vỡ ngay khi bị chạm vào.

[pause] Nhưng nó không phải một lựa chọn liều lĩnh. Nó là lựa chọn của người biết chính xác điểm mạnh của mình: phản xạ và kinh nghiệm né đòn từ hàng trăm trò chơi tệ hại.

[pause] [chuckles] Kaku rút ra bài học đầu tiên: bảng chỉ số tốt nhất không phải bảng cân bằng nhất, mà là bảng hợp với người chơi nhất.
```

### c07 · Xếp hạng: điều gì quyết định thắng thua?

Khoảng 106 giây · cảnh s53–s61 · 1375 ký tự

**Gemini**

```text
Theo đúng khung của dạng video này, Kaku xếp hạng những thứ quyết định thắng thua trong Shangri-La Frontier, từ ít quan trọng tới quan trọng nhất.

<short pause> Hạng tư: chỉ số. Quan trọng, nhưng ai chơi lâu cũng có chỉ số cao. Nó là nền, không phải lợi thế.

<short pause> Nhưng cũng phải công bằng: một số vũ khí đặc biệt, có được nhờ nhiệm vụ độc nhất, đã giúp Sunraku rất nhiều. Trang bị không quyết định tất cả, nhưng trang bị đúng lúc thì rất có giá.

<short pause> Hạng ba: trang bị. Vũ khí và giáp mạnh thay đổi được nhiều thứ. <short pause> Nhưng Sunraku bị nguyền không mặc được giáp, mà vẫn đi xa hơn người khác.

<short pause> Arthur Pencilgon, bạn cũ của Rakuro, là bậc thầy về thông tin và mưu kế. Cô nổi tiếng là kẻ chuyên hạ gục người chơi khác, và luôn biết nhiều hơn những gì mình nói.

<short pause> Hạng nhì: thông tin. Trong một thế giới rộng lớn, biết một bí mật như cách vào làng thỏ, hay điều kiện để đánh một con trùm, có giá trị hơn mọi món đồ.

<short pause> Hạng nhất: kỹ năng của con người thật. Phản xạ, bình tĩnh, khả năng đọc nhịp đối thủ. Thứ mà Rakuro mang từ ngoài đời vào game.

<short pause> Ba người Sunraku, Pencilgon và Oikatzo khi hợp lại là một đội đáng sợ: một người né giỏi, một người mưu mẹo, một người có kỹ năng chuyên nghiệp. Mỗi người mạnh ở một hạng khác nhau trên bảng xếp hạng này.

<short pause> Bạn của Rakuro, Oikatzo, là một game thủ chuyên nghiệp ngoài đời, và bản thân điều đó đã nói lên tất cả: trong trò chơi này, thứ mạnh nhất không hiện trên bảng chỉ số.
```

**ElevenLabs**

```text
Theo đúng khung của dạng video này, Kaku xếp hạng những thứ quyết định thắng thua trong Shangri-La Frontier, từ ít quan trọng tới quan trọng nhất.

[pause] Hạng tư: chỉ số. Quan trọng, nhưng ai chơi lâu cũng có chỉ số cao. Nó là nền, không phải lợi thế.

[pause] Nhưng cũng phải công bằng: một số vũ khí đặc biệt, có được nhờ nhiệm vụ độc nhất, đã giúp Sunraku rất nhiều. Trang bị không quyết định tất cả, nhưng trang bị đúng lúc thì rất có giá.

[pause] Hạng ba: trang bị. Vũ khí và giáp mạnh thay đổi được nhiều thứ. [pause] Nhưng Sunraku bị nguyền không mặc được giáp, mà vẫn đi xa hơn người khác.

[pause] Arthur Pencilgon, bạn cũ của Rakuro, là bậc thầy về thông tin và mưu kế. Cô nổi tiếng là kẻ chuyên hạ gục người chơi khác, và luôn biết nhiều hơn những gì mình nói.

[pause] Hạng nhì: thông tin. Trong một thế giới rộng lớn, biết một bí mật như cách vào làng thỏ, hay điều kiện để đánh một con trùm, có giá trị hơn mọi món đồ.

[pause] Hạng nhất: kỹ năng của con người thật. Phản xạ, bình tĩnh, khả năng đọc nhịp đối thủ. Thứ mà Rakuro mang từ ngoài đời vào game.

[pause] Ba người Sunraku, Pencilgon và Oikatzo khi hợp lại là một đội đáng sợ: một người né giỏi, một người mưu mẹo, một người có kỹ năng chuyên nghiệp. Mỗi người mạnh ở một hạng khác nhau trên bảng xếp hạng này.

[pause] Bạn của Rakuro, Oikatzo, là một game thủ chuyên nghiệp ngoài đời, và bản thân điều đó đã nói lên tất cả: trong trò chơi này, thứ mạnh nhất không hiện trên bảng chỉ số.
```

### c08 · Giới hạn của những con số

Khoảng 116 giây · cảnh s62–s70 · 1506 ký tự

**Gemini**

```text
Nhưng bảng chỉ số cũng có giới hạn. Giới hạn thứ nhất: quái vật độc nhất. Trò chơi có những con trùm đặc biệt mạnh tới mức chỉ số bình thường gần như vô nghĩa.

<short pause> Hai mươi phút có thể không dài khi bạn xem phim. <short pause> Nhưng thử tưởng tượng hai mươi phút liên tục né đòn của một con trùm, không được sai một lần. Đó là thử thách của tinh thần, không phải của chỉ số.

<short pause> Trận đấu với Wethermon, hiệp sĩ canh mộ, là ví dụ rõ nhất. Người chơi phải sống sót hai mươi phút trước khi thật sự có thể phản công. Chỉ số không giúp được, chỉ có sự kiên nhẫn.

<short pause> Giới hạn thứ hai: những lời nguyền và hiệu ứng đặc biệt. Lời nguyền của Lycagon, con sói săn đêm, không chỉ cấm mặc giáp. Nó còn khiến quái vật yếu hơn bỏ chạy, và mở ra những câu thoại mới với các nhân vật.

<short pause> Ở mùa hai, người chơi còn phải hợp sức trong những trận đánh tập thể với quái vật khổng lồ. Khi đó, khả năng phối hợp và chỉ huy quan trọng không kém gì chỉ số cá nhân.

<short pause> Một hiệu ứng vừa là điểm yếu, vừa là lợi thế. Bảng chỉ số không thể đánh giá nó bằng một con số cộng hay trừ.

<short pause> Kaku rất thích chi tiết này: người chơi mạnh nhất lại có bạn thân là một con thỏ. Và tình bạn đó mở ra cả một chuỗi nhiệm vụ mà cả máy chủ không ai biết tới.

<short pause> Giới hạn thứ ba: các nhân vật trong game như có linh hồn. Emul và tộc thỏ Vorpal có tính cách, cảm xúc, ký ức. Quan hệ với họ mở ra những thứ mà không chỉ số nào tính được.

<short pause> <laugh> Kaku ghi chú: Shangri-La Frontier dùng bảng chỉ số để nói rằng những thứ quan trọng nhất trong trò chơi, cũng như ngoài đời, thường không hiện lên thành con số.
```

**ElevenLabs**

```text
Nhưng bảng chỉ số cũng có giới hạn. Giới hạn thứ nhất: quái vật độc nhất. Trò chơi có những con trùm đặc biệt mạnh tới mức chỉ số bình thường gần như vô nghĩa.

[pause] Hai mươi phút có thể không dài khi bạn xem phim. [pause] Nhưng thử tưởng tượng hai mươi phút liên tục né đòn của một con trùm, không được sai một lần. Đó là thử thách của tinh thần, không phải của chỉ số.

[pause] Trận đấu với Wethermon, hiệp sĩ canh mộ, là ví dụ rõ nhất. Người chơi phải sống sót hai mươi phút trước khi thật sự có thể phản công. Chỉ số không giúp được, chỉ có sự kiên nhẫn.

[pause] Giới hạn thứ hai: những lời nguyền và hiệu ứng đặc biệt. Lời nguyền của Lycagon, con sói săn đêm, không chỉ cấm mặc giáp. Nó còn khiến quái vật yếu hơn bỏ chạy, và mở ra những câu thoại mới với các nhân vật.

[pause] Ở mùa hai, người chơi còn phải hợp sức trong những trận đánh tập thể với quái vật khổng lồ. Khi đó, khả năng phối hợp và chỉ huy quan trọng không kém gì chỉ số cá nhân.

[pause] Một hiệu ứng vừa là điểm yếu, vừa là lợi thế. Bảng chỉ số không thể đánh giá nó bằng một con số cộng hay trừ.

[pause] Kaku rất thích chi tiết này: người chơi mạnh nhất lại có bạn thân là một con thỏ. Và tình bạn đó mở ra cả một chuỗi nhiệm vụ mà cả máy chủ không ai biết tới.

[pause] Giới hạn thứ ba: các nhân vật trong game như có linh hồn. Emul và tộc thỏ Vorpal có tính cách, cảm xúc, ký ức. Quan hệ với họ mở ra những thứ mà không chỉ số nào tính được.

[pause] [chuckles] Kaku ghi chú: Shangri-La Frontier dùng bảng chỉ số để nói rằng những thứ quan trọng nhất trong trò chơi, cũng như ngoài đời, thường không hiện lên thành con số.
```

### c09 · Trò chơi: thẻ chỉ số của bạn / Kết

Khoảng 113 giây · cảnh s71–s80 · 1473 ký tự

**Gemini**

```text
Giờ tới lượt bạn. Kaku cho bạn ba mươi điểm để chia vào sáu chỉ số: sinh lực, sức bền, sức mạnh, thể chất, nhanh nhẹn, may mắn.

<short pause> Một gợi ý nhỏ: đừng chia đều. Hãy thử làm như Sunraku, chọn một hai điểm mạnh thật rõ và chấp nhận một điểm yếu. Nhân vật như vậy mới có cá tính.

<short pause> Bạn là kiểu người chịu đòn giỏi và kiên trì? Dồn vào thể chất. Bạn phản xạ nhanh? Dồn vào nhanh nhẹn. Bạn hay trúng thưởng? Chắc là may mắn.

<short pause> Và chọn một nghề cho mình: chiến binh, pháp sư, lữ khách, hay một nghề bạn tự nghĩ ra. Viết thẻ chỉ số của bạn vào bình luận, Kaku sẽ ghim thẻ thú vị nhất.

<short pause> <laugh> Thẻ của Kaku đây: may mắn hai điểm, thể chất hai điểm, và hai mươi sáu điểm vào… đọc sách. Chỉ số này không có trong game, nhưng Kaku vẫn thêm vào.

<short pause> Và đó cũng là một lời nhắn cho người xem: đừng để con số định nghĩa bạn. Chỉ số của bạn ngoài đời có thể thấp ở chỗ này, nhưng cách bạn dùng nó mới quyết định bạn đi được bao xa.

<short pause> Shangri-La Frontier cho ta một bảng chỉ số rất chi tiết, rồi dành cả câu chuyện để chứng minh rằng con người sau nhân vật mới là chỉ số quan trọng nhất.

<short pause> Mùa ba lên sóng trong tháng một. Xem xong, hãy thử để ý xem Sunraku có thay đổi bản xây dựng của mình không, và vì sao.

<short pause> Video tiếp theo, Kaku tiếp tục ôn tập trước mùa mới, lần này là Mashle: thế giới nơi phép thuật quyết định địa vị, và một cậu bé không có chút phép thuật nào chỉ dùng… cơ bắp.

<short pause> Nếu bạn là game thủ và thích kiểu phân tích này, hãy đăng ký kênh để Kaku đọc thêm nhiều bảng chỉ số nữa. Kaku gấp sổ đây, hẹn gặp lại!
```

**ElevenLabs**

```text
Giờ tới lượt bạn. Kaku cho bạn ba mươi điểm để chia vào sáu chỉ số: sinh lực, sức bền, sức mạnh, thể chất, nhanh nhẹn, may mắn.

[pause] Một gợi ý nhỏ: đừng chia đều. Hãy thử làm như Sunraku, chọn một hai điểm mạnh thật rõ và chấp nhận một điểm yếu. Nhân vật như vậy mới có cá tính.

[pause] [curious] Bạn là kiểu người chịu đòn giỏi và kiên trì? Dồn vào thể chất. Bạn phản xạ nhanh? Dồn vào nhanh nhẹn. Bạn hay trúng thưởng? Chắc là may mắn.

[pause] Và chọn một nghề cho mình: chiến binh, pháp sư, lữ khách, hay một nghề bạn tự nghĩ ra. Viết thẻ chỉ số của bạn vào bình luận, Kaku sẽ ghim thẻ thú vị nhất.

[pause] [chuckles] Thẻ của Kaku đây: may mắn hai điểm, thể chất hai điểm, và hai mươi sáu điểm vào… đọc sách. Chỉ số này không có trong game, nhưng Kaku vẫn thêm vào.

[pause] Và đó cũng là một lời nhắn cho người xem: đừng để con số định nghĩa bạn. Chỉ số của bạn ngoài đời có thể thấp ở chỗ này, nhưng cách bạn dùng nó mới quyết định bạn đi được bao xa.

[pause] Shangri-La Frontier cho ta một bảng chỉ số rất chi tiết, rồi dành cả câu chuyện để chứng minh rằng con người sau nhân vật mới là chỉ số quan trọng nhất.

[pause] Mùa ba lên sóng trong tháng một. Xem xong, hãy thử để ý xem Sunraku có thay đổi bản xây dựng của mình không, và vì sao.

[pause] Video tiếp theo, Kaku tiếp tục ôn tập trước mùa mới, lần này là Mashle: thế giới nơi phép thuật quyết định địa vị, và một cậu bé không có chút phép thuật nào chỉ dùng… cơ bắp.

[pause] Nếu bạn là game thủ và thích kiểu phân tích này, hãy đăng ký kênh để Kaku đọc thêm nhiều bảng chỉ số nữa. Kaku gấp sổ đây, hẹn gặp lại!
```
