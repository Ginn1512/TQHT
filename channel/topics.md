# Danh sách chủ đề (78 video)

Chấm điểm từ 1 đến 5 cho mỗi tiêu chí. Làm trước những chủ đề có tổng điểm cao.

- **Nhu cầu:** mọi người có đang tìm kiếm hoặc bàn luận chủ đề này không? Bộ đang phát năm 2026 được cộng điểm (xem `channel/references/nghien-cuu-nganh-2026.md`).
- **Bằng chứng:** các kênh mẫu từng có video vượt trội về chủ đề tương tự chưa? (`?` = chờ `/yt-analyzer` có key)
- **Góc nhìn:** mình có góc riêng để nói không?
- **Dễ minh họa:** vẽ được bằng tranh AI và sơ đồ mà không cần art chính thức không?

Tổng tạm tính trên 3 tiêu chí (tối đa 15), chưa có Bằng chứng.

**Dạng video:** mã A–U trong `channel/formats.md`. Luật: không có 2 video liền nhau cùng dạng, và mỗi dạng tối đa 2 lần trong 30 video. Kiểm tra bằng `python -m tools.plan_check`.

**Lịch đăng (đổi ngày 30/09/2026):**

- **3 video dài mỗi ngày**, cách nhau 8 giờ: 06:00, 14:00, 22:00 (giờ Việt Nam). Video n đăng ngày 06/10 + ⌊(n−1)/3⌋.
- 78 video đăng từ 06/10 đến 31/10/2026. Video 79 trở đi đăng từ 01/11; `/yt-research` và viết kịch bản đợt mới bắt đầu ngay.
- **Mỗi ngày 1 Short lúc 18:00**, cắt từ video 06:00 của cùng ngày (`tools/shorts.py`): 26 Short từ 06/10 đến 31/10.
- **Xét lại nhịp ngày 25/10**, dựa trên CTR, tỉ lệ giữ chân, cảnh báo chính sách và số giờ làm của người. Có cảnh báo chính sách thì giảm ngay về 1 video/ngày.
- Mục tiêu đủ điều kiện YPP, tính từ 06/10/2026 (xem `docs/lo-trinh.md`).
- **Hạn chót 31/01/2027:** đủ 1.000 người đăng ký + 4.000 giờ xem thì nộp đơn YPP ngay. Từ 01/02/2027 kênh mới cần 8.000 giờ xem.
- Các video gắn mùa anime 2027 (40–42, 47, 59, 64, 75–78) đăng sớm trong tháng 10, lời thoại đã sửa theo kiểu "chuẩn bị trước mùa mới".
- Ảnh qua API, trần 2,5 USD/video. Trần tháng 200 USD, ghi trong `channel/costs.md`.
- Ngày đăng có thể lùi nếu không kịp làm; thứ tự video phải giữ nguyên để luật dạng video vẫn đạt. Lùi lịch thì chỉ sửa cột "Ngày đăng", "Giờ" và Notion, không đổi tên thư mục.

| # | Ngày đăng | Giờ | Chủ đề | Anime | Dạng | Nhu cầu | Bằng chứng | Góc nhìn | Dễ minh họa | Tổng | Thư mục | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-06 | 06:00 | Nen hoạt động thế nào? 6 hệ và luật "giao ước" | Hunter x Hunter | A · Giải thích hệ thống | 5 | ? | 5 | 5 | 15 | `videos/2026-10-06-nen-hunter-x-hunter/` | Kịch bản xong — chờ kiểm nguồn |
| 2 | 2026-10-06 | 14:00 | Bành trướng lãnh địa: luật và cách phá | Jujutsu Kaisen | B · Luật chơi và cách phá | 5 | ? | 4 | 4 | 13 | `videos/2026-10-06-lanh-dia-jujutsu-kaisen/` | Kịch bản xong — chờ kiểm nguồn |
| 3 | 2026-10-06 | 22:00 | Ma thuật Frieren, vì sao Zoltraak thành phổ thông | Frieren | C · Lịch sử / tiến hóa | 4 | ? | 5 | 3 | 12 | `videos/2026-10-06-ma-thuat-frieren/` | Kịch bản xong — chờ kiểm nguồn |
| 4 | 2026-10-07 | 06:00 | 3 loại Haki và Haki bá vương "phủ" | One Piece | A · Giải thích hệ thống | 5 | ? | 4 | 5 | 14 | `videos/2026-10-07-haki-one-piece/` | Kịch bản xong — chờ kiểm nguồn |
| 5 | 2026-10-07 | 14:00 | Cây phả hệ các kiểu Hơi thở | Kimetsu no Yaiba | D · Cây phả hệ | 4 | ? | 4 | 4 | 12 | `videos/2026-10-07-cay-pha-he-hoi-tho-kimetsu/` | Kịch bản xong — chờ kiểm nguồn |
| 6 | 2026-10-07 | 22:00 | Hồ sơ trái ác quỷ, thức tỉnh | One Piece | E · Hồ sơ bách khoa | 5 | ? | 4 | 4 | 13 | `videos/2026-10-07-trai-ac-quy-one-piece/` | Kịch bản xong — chờ kiểm nguồn |
| 7 | 2026-10-08 | 06:00 | Hệ thống cấp bậc thợ săn và cổng | Solo Leveling | F · Bảng chỉ số kiểu game | 4 | ? | 4 | 5 | 13 | `videos/2026-10-08-cap-bac-tho-san-solo-leveling/` | Kịch bản xong — chờ kiểm nguồn |
| 8 | 2026-10-08 | 14:00 | Sharingan tiến hóa và cái giá | Naruto | G · Bậc thang tiến hóa | 4 | ? | 3 | 4 | 11 | `videos/2026-10-08-sharingan-tien-hoa-naruto/` | Kịch bản xong — chờ kiểm nguồn |
| 9 | 2026-10-08 | 22:00 | Ác quỷ và nỗi sợ | Chainsaw Man | B · Luật chơi và cách phá | 4 | ? | 4 | 3 | 11 | `videos/2026-10-08-ac-quy-noi-so-chainsaw-man/` | Kịch bản xong — chờ kiểm nguồn |
| 10 | 2026-10-09 | 06:00 | Chakra vs Nen vs Chú lực | Naruto / HxH / JJK | I · So sánh chéo có chấm điểm | 4 | ? | 5 | 4 | 13 | `videos/2026-10-09-chakra-nen-chu-luc-so-sanh/` | Kịch bản xong — chờ kiểm nguồn |
| 11 | 2026-10-09 | 14:00 | Các dạng Super Saiyan theo sức mạnh và cái giá | Dragon Ball | J · Xếp hạng có tiêu chí | 4 | ? | 3 | 4 | 11 | `videos/2026-10-09-xep-hang-super-saiyan/` | Kịch bản xong — chờ kiểm nguồn |
| 12 | 2026-10-09 | 22:00 | Nhập môn: ma thuật được vẽ ra | Witch Hat Atelier (hot xuân 2026) | Q · Nhập môn | 4 | ? | 5 | 5 | 14 | `videos/2026-10-09-nhap-mon-witch-hat-atelier/` | Kịch bản xong — chờ kiểm nguồn |
| 13 | 2026-10-10 | 06:00 | "Xoay" và tỉ lệ vàng: khoa học có thật không? | JoJo: Steel Ball Run (đang phát) | P · Khoa học trong anime | 4 | ? | 5 | 4 | 13 | `videos/2026-10-10-khoa-hoc-xoay-steel-ball-run/` | Kịch bản xong — chờ kiểm nguồn |
| 14 | 2026-10-10 | 14:00 | Hồ sơ grimoire 3, 4, 5 lá và phản ma thuật | Black Clover (mùa 2 đang phát) | E · Hồ sơ bách khoa | 5 | ? | 4 | 4 | 13 | `videos/2026-10-10-ho-so-grimoire-black-clover/` | Kịch bản xong — chờ kiểm nguồn |
| 15 | 2026-10-10 | 22:00 | 10 hiểu lầm phổ biến | Jujutsu Kaisen | K · Gỡ hiểu lầm | 5 | ? | 4 | 4 | 13 | `videos/2026-10-10-10-hieu-lam-jujutsu-kaisen/` | Kịch bản xong — chờ kiểm nguồn |
| 16 | 2026-10-11 | 06:00 | Nếu bạn sống trong thế giới yêu quái + người ngoài hành tinh | Dandadan | L · Thử nghiệm "nếu… thì" | 4 | ? | 5 | 4 | 13 | `videos/2026-10-11-neu-ban-song-trong-dandadan/` | Kịch bản xong — chờ kiểm nguồn |
| 17 | 2026-10-11 | 14:00 | Bảng chỉ số: tỉ lệ giải phóng sức mạnh và chỉ số quái thú | Kaiju No. 8 | F · Bảng chỉ số kiểu game | 4 | ? | 4 | 5 | 13 | `videos/2026-10-11-bang-chi-so-kaiju-no-8/` | Kịch bản xong — chờ kiểm nguồn |
| 18 | 2026-10-11 | 22:00 | Từ Shikai đến Bankai | Bleach (2 tập cuối phát 19/10 và 26/10) | G · Bậc thang tiến hóa | 4 | ? | 4 | 4 | 12 | `videos/2026-10-11-shikai-bankai-bleach/` | Kịch bản xong — chờ kiểm nguồn |
| 19 | 2026-10-12 | 06:00 | Dòng thời gian 800 năm và Thế kỷ trống | One Piece | O · Dòng thời gian | 5 | ? | 4 | 4 | 13 | `videos/2026-10-12-dong-thoi-gian-800-nam-one-piece/` | Kịch bản xong — chờ kiểm nguồn |
| 20 | 2026-10-12 | 14:00 | Bí ẩn Lục địa Đen (lý thuyết có gắn nhãn) | Hunter x Hunter | N · Điều tra bí ẩn | 4 | ? | 4 | 4 | 12 | `videos/2026-10-12-bi-an-luc-dia-den-hunter-x-hunter/` | Kịch bản xong — chờ kiểm nguồn |
| 21 | 2026-10-12 | 22:00 | Phân tích chiến thuật trận Tanjiro vs Rui | Kimetsu no Yaiba | M · Phân tích trận đấu | 4 | ? | 4 | 3 | 11 | `videos/2026-10-12-phan-tich-tran-tanjiro-rui/` | Kịch bản xong — chờ kiểm nguồn |
| 22 | 2026-10-13 | 06:00 | Những chi tiết cài cắm từ tập 1 | Attack on Titan | R · Cài cắm và chi tiết ẩn | 5 | ? | 4 | 3 | 12 | `videos/2026-10-13-cai-cam-attack-on-titan/` | Kịch bản xong — chờ kiểm nguồn |
| 23 | 2026-10-13 | 14:00 | 10 hiểu lầm phổ biến | Naruto | K · Gỡ hiểu lầm | 5 | ? | 4 | 4 | 13 | `videos/2026-10-13-10-hieu-lam-naruto/` | Kịch bản xong — chờ kiểm nguồn |
| 24 | 2026-10-13 | 22:00 | Nếu bạn tập trong Phòng Thời Gian Tinh Thần | Dragon Ball | L · Thử nghiệm "nếu… thì" | 4 | ? | 5 | 5 | 14 | `videos/2026-10-13-phong-thoi-gian-tinh-than-dragon-ball/` | Kịch bản xong — chờ kiểm nguồn |
| 25 | 2026-10-14 | 06:00 | Dòng thời gian 1.000 năm từ thời Heian | Jujutsu Kaisen | O · Dòng thời gian | 4 | ? | 4 | 4 | 12 | `videos/2026-10-14-dong-thoi-gian-jujutsu-kaisen/` | Kịch bản xong — chờ kiểm nguồn |
| 26 | 2026-10-14 | 14:00 | Khoa học thật đằng sau các phát minh của Senku | Dr. Stone (mùa cuối 2026) | P · Khoa học trong anime | 4 | ? | 5 | 5 | 14 | `videos/2026-10-14-khoa-hoc-that-dr-stone/` | Kịch bản xong — chờ kiểm nguồn |
| 27 | 2026-10-14 | 22:00 | Nhập môn: hậu cung, thuốc và độc | Dược sư tự sự (mùa 3 đang phát) | Q · Nhập môn | 5 | ? | 4 | 4 | 13 | `videos/2026-10-14-nhap-mon-duoc-su-tu-su/` | Kịch bản xong — chờ kiểm nguồn |
| 28 | 2026-10-15 | 06:00 | Lịch sử từ Hamon đến Stand | JoJo | C · Lịch sử / tiến hóa | 4 | ? | 4 | 4 | 12 | `videos/2026-10-15-lich-su-hamon-stand-jojo/` | Kịch bản xong — chờ kiểm nguồn |
| 29 | 2026-10-15 | 14:00 | Cây phả hệ Otsutsuki, Uchiha, Senju, Uzumaki | Naruto | D · Cây phả hệ | 4 | ? | 3 | 4 | 11 | `videos/2026-10-15-cay-pha-he-naruto/` | Kịch bản xong — chờ kiểm nguồn |
| 30 | 2026-10-15 | 22:00 | Ma thuật Frieren vs Black Clover vs Witch Hat Atelier | Frieren / Black Clover / Witch Hat Atelier | I · So sánh chéo có chấm điểm | 4 | ? | 5 | 4 | 13 | `videos/2026-10-15-so-sanh-ma-thuat-3-the-gioi/` | Kịch bản xong — chờ kiểm nguồn |
| 31 | 2026-10-16 | 06:00 | Vô hạ hạn nói gì về con người Gojo | Jujutsu Kaisen | H · Chân dung qua sức mạnh | 5 | ? | 5 | 4 | 14 | `videos/2026-10-16-vo-ha-han-gojo/` | Kịch bản xong — chờ kiểm nguồn |
| 32 | 2026-10-16 | 14:00 | Luật du hành thời gian 12 năm và cách "phá" tương lai | Tokyo Revengers (mùa 4 đang phát) | B · Luật chơi và cách phá | 4 | ? | 5 | 4 | 13 | `videos/2026-10-16-luat-du-hanh-tokyo-revengers/` | Kịch bản xong — chờ kiểm nguồn |
| 33 | 2026-10-16 | 22:00 | Xếp hạng các vị thần | Dragon Ball (DBS: Beerus đang phát) | J · Xếp hạng có tiêu chí | 5 | ? | 4 | 4 | 13 | `videos/2026-10-16-xep-hang-cac-vi-than-dragon-ball/` | Kịch bản xong — chờ kiểm nguồn |
| 34 | 2026-10-17 | 06:00 | Cấy ghép cơ thể và chứng "loạn thần máy" | Cyberpunk: Edgerunners (mùa 2 ra 20/10) | A · Giải thích hệ thống | 4 | ? | 5 | 5 | 14 | `videos/2026-10-17-cay-ghep-edgerunners/` | Kịch bản xong — chờ kiểm nguồn |
| 35 | 2026-10-17 | 14:00 | Truyền thuyết Momotaro thật và cách bộ truyện lật ngược nó | Tougen Anki (arc mới tháng 10/2026) | S · Nguồn gốc ngoài đời thật | 4 | ? | 5 | 5 | 14 | `videos/2026-10-17-momotaro-that-tougen-anki/` | Kịch bản xong — chờ kiểm nguồn |
| 36 | 2026-10-17 | 22:00 | Phân tích trận Ichigo vs Byakuya | Bleach | M · Phân tích trận đấu | 4 | ? | 4 | 4 | 12 | `videos/2026-10-17-tran-ichigo-byakuya/` | Kịch bản xong — chờ kiểm nguồn |
| 37 | 2026-10-18 | 06:00 | Hồ sơ 4 loại Kagune | Tokyo Ghoul | E · Hồ sơ bách khoa | 4 | ? | 4 | 4 | 12 | `videos/2026-10-18-ho-so-kagune-tokyo-ghoul/` | Kịch bản xong — chờ kiểm nguồn |
| 38 | 2026-10-18 | 14:00 | Lịch sử các hệ, từ 15 lên 18 | Pokémon | C · Lịch sử / tiến hóa | 5 | ? | 4 | 4 | 13 | `videos/2026-10-18-lich-su-cac-he-pokemon/` | Kịch bản xong — chờ kiểm nguồn |
| 39 | 2026-10-18 | 22:00 | Phiên tòa: Eren Yeager | Attack on Titan | U · Phiên tòa nhân vật | 5 | ? | 5 | 4 | 14 | `videos/2026-10-18-phien-toa-eren/` | Kịch bản xong — chờ kiểm nguồn |
| 40 | 2026-10-19 | 06:00 | Ôn tập trước mùa 2 | Sakamoto Days (mùa 2 tháng 1) | T · Ôn tập trước mùa mới | 4 | ? | 4 | 4 | 12 | `videos/2026-10-19-on-tap-sakamoto-days/` | Kịch bản xong — chờ kiểm nguồn |
| 41 | 2026-10-19 | 14:00 | Bảng chỉ số kiểu game | Shangri-La Frontier (mùa 3 tháng 1) | F · Bảng chỉ số kiểu game | 4 | ? | 5 | 5 | 14 | `videos/2026-10-19-bang-chi-so-shangri-la-frontier/` | Kịch bản xong — chờ kiểm nguồn |
| 42 | 2026-10-19 | 22:00 | Ôn tập trước mùa 3 | Mashle (mùa 3 tháng 1) | T · Ôn tập trước mùa mới | 4 | ? | 4 | 4 | 12 | `videos/2026-10-19-on-tap-mashle/` | Kịch bản xong — chờ kiểm nguồn |
| 43 | 2026-10-20 | 06:00 | Rimuru tiến hóa từ slime đến Ma vương | Tensura | G · Bậc thang tiến hóa | 4 | ? | 4 | 5 | 13 | `videos/2026-10-20-rimuru-tien-hoa-tensura/` | Kịch bản xong — chờ kiểm nguồn |
| 44 | 2026-10-20 | 14:00 | Cây phả hệ One For All, 9 người kế thừa | My Hero Academia | D · Cây phả hệ | 4 | ? | 4 | 4 | 12 | `videos/2026-10-20-cay-pha-he-one-for-all/` | Kịch bản xong — chờ kiểm nguồn |
| 45 | 2026-10-20 | 22:00 | APTX 4869 và đồ của tiến sĩ Agasa: khoa học thật tới đâu | Thám tử lừng danh Conan | P · Khoa học trong anime | 5 | ? | 5 | 4 | 14 | `videos/2026-10-20-khoa-hoc-conan/` | Kịch bản xong — chờ kiểm nguồn |
| 46 | 2026-10-21 | 06:00 | Luật chơi Tử Diệt Hồi Du và cách phá | Jujutsu Kaisen | B · Luật chơi và cách phá | 5 | ? | 4 | 4 | 13 | `videos/2026-10-21-luat-tu-diet-hoi-du/` | Kịch bản xong — chờ kiểm nguồn |
| 47 | 2026-10-21 | 14:00 | Nếu bạn dự kỳ thi sát thủ JCC | Sakamoto Days (mùa 2 tháng 1/2027) | L · Thử nghiệm "nếu… thì" | 4 | ? | 5 | 4 | 13 | `videos/2026-10-21-neu-ban-thi-jcc-sakamoto-days/` | Kịch bản xong — chờ kiểm nguồn |
| 48 | 2026-10-21 | 22:00 | Nhập môn Jinki (bảo khí) | Gachiakuta | Q · Nhập môn | 4 | ? | 4 | 5 | 13 | `videos/2026-10-21-nhap-mon-gachiakuta/` | Kịch bản xong — chờ kiểm nguồn |
| 49 | 2026-10-22 | 06:00 | Du hành thời gian: luật nào chặt nhất | Tokyo Revengers / Steins;Gate / Re:Zero | I · So sánh chéo có chấm điểm | 4 | ? | 5 | 4 | 13 | `videos/2026-10-22-so-sanh-du-hanh-thoi-gian/` | Kịch bản xong — chờ kiểm nguồn |
| 50 | 2026-10-22 | 14:00 | Dòng thời gian 1.000 năm, từ Muzan tới Tanjiro | Kimetsu no Yaiba | O · Dòng thời gian | 5 | ? | 4 | 4 | 13 | `videos/2026-10-22-dong-thoi-gian-kimetsu/` | Kịch bản xong — chờ kiểm nguồn |
| 51 | 2026-10-22 | 22:00 | Giả kim thuật và luật trao đổi ngang giá | Fullmetal Alchemist | A · Giải thích hệ thống | 5 | ? | 4 | 5 | 14 | `videos/2026-10-22-gia-kim-thuat-fullmetal/` | Kịch bản xong — chờ kiểm nguồn |
| 52 | 2026-10-23 | 06:00 | Tần Thủy Hoàng và Lý Tín thật | Kingdom | S · Nguồn gốc ngoài đời thật | 4 | ? | 5 | 4 | 13 | `videos/2026-10-23-tan-thuy-hoang-that-kingdom/` | Kịch bản xong — chờ kiểm nguồn |
| 53 | 2026-10-23 | 14:00 | Bí ẩn Ác quỷ Cưa máy (lý thuyết có gắn nhãn) | Chainsaw Man | N · Điều tra bí ẩn | 4 | ? | 4 | 4 | 12 | `videos/2026-10-23-bi-an-ac-quy-cua-may/` | Kịch bản xong — chờ kiểm nguồn |
| 54 | 2026-10-23 | 22:00 | Từ 1% đến 100%: sức mạnh là cảm xúc | Mob Psycho 100 | H · Chân dung qua sức mạnh | 4 | ? | 5 | 4 | 13 | `videos/2026-10-23-mob-psycho-100-phan-tram/` | Kịch bản xong — chờ kiểm nguồn |
| 55 | 2026-10-24 | 06:00 | 10 hiểu lầm phổ biến | One Piece | K · Gỡ hiểu lầm | 5 | ? | 4 | 4 | 13 | `videos/2026-10-24-10-hieu-lam-one-piece/` | Kịch bản xong — chờ kiểm nguồn |
| 56 | 2026-10-24 | 14:00 | Hồ sơ quái vật (và ăn được không) | Dungeon Meshi | E · Hồ sơ bách khoa | 4 | ? | 5 | 5 | 14 | `videos/2026-10-24-ho-so-quai-vat-dungeon-meshi/` | Kịch bản xong — chờ kiểm nguồn |
| 57 | 2026-10-24 | 22:00 | Phân tích trận Naruto vs Pain | Naruto | M · Phân tích trận đấu | 5 | ? | 4 | 4 | 13 | `videos/2026-10-24-tran-naruto-pain/` | Kịch bản xong — chờ kiểm nguồn |
| 58 | 2026-10-25 | 06:00 | Phiên tòa: Lelouch | Code Geass | U · Phiên tòa nhân vật | 4 | ? | 5 | 4 | 13 | `videos/2026-10-25-phien-toa-lelouch/` | Kịch bản xong — chờ kiểm nguồn |
| 59 | 2026-10-25 | 14:00 | Chi tiết cài cắm trong 50 chương đầu | One Piece (bản làm lại tháng 2) | R · Cài cắm và chi tiết ẩn | 5 | ? | 4 | 4 | 13 | `videos/2026-10-25-cai-cam-50-chuong-one-piece/` | Kịch bản xong — chờ kiểm nguồn |
| 60 | 2026-10-25 | 22:00 | Bảng xếp hạng anh hùng và cấp thảm họa | One Punch Man | F · Bảng chỉ số kiểu game | 4 | ? | 4 | 5 | 13 | `videos/2026-10-25-xep-hang-anh-hung-one-punch-man/` | Kịch bản xong — chờ kiểm nguồn |
| 61 | 2026-10-26 | 06:00 | Lịch sử luật bài, từ Fusion đến Link | Yu-Gi-Oh! | C · Lịch sử / tiến hóa | 4 | ? | 5 | 4 | 13 | `videos/2026-10-26-lich-su-luat-bai-yu-gi-oh/` | Kịch bản xong — chờ kiểm nguồn |
| 62 | 2026-10-26 | 14:00 | Các dạng Ác ma hợp thể của Asta | Black Clover (mùa 2 đang phát) | G · Bậc thang tiến hóa | 4 | ? | 4 | 4 | 12 | `videos/2026-10-26-ac-ma-hop-the-asta/` | Kịch bản xong — chờ kiểm nguồn |
| 63 | 2026-10-26 | 22:00 | Luật của cuốn sổ và cách phá | Death Note | B · Luật chơi và cách phá | 5 | ? | 5 | 4 | 14 | `videos/2026-10-26-luat-death-note/` | Kịch bản xong — chờ kiểm nguồn |
| 64 | 2026-10-27 | 06:00 | Bảo bối nào làm được ngoài đời thật | Doraemon (phim mới 05/03) | P · Khoa học trong anime | 5 | ? | 5 | 5 | 15 | `videos/2026-10-27-khoa-hoc-doraemon/` | Kịch bản xong — chờ kiểm nguồn |
| 65 | 2026-10-27 | 14:00 | Cây phả hệ Joestar và dấu ngôi sao | JoJo | D · Cây phả hệ | 4 | ? | 4 | 4 | 12 | `videos/2026-10-27-cay-pha-he-joestar/` | Kịch bản xong — chờ kiểm nguồn |
| 66 | 2026-10-27 | 22:00 | Người Viking thật và Thorfinn thật | Vinland Saga | S · Nguồn gốc ngoài đời thật | 4 | ? | 5 | 5 | 14 | `videos/2026-10-27-viking-that-vinland-saga/` | Kịch bản xong — chờ kiểm nguồn |
| 67 | 2026-10-28 | 06:00 | "Tao" (Đạo) hoạt động thế nào | Hell's Paradise | A · Giải thích hệ thống | 4 | ? | 4 | 4 | 12 | `videos/2026-10-28-tao-hells-paradise/` | Kịch bản xong — chờ kiểm nguồn |
| 68 | 2026-10-28 | 14:00 | Nếu bạn là đứa trẻ ở Grace Field | Miền đất hứa | L · Thử nghiệm "nếu… thì" | 4 | ? | 5 | 4 | 13 | `videos/2026-10-28-neu-ban-o-grace-field/` | Kịch bản xong — chờ kiểm nguồn |
| 69 | 2026-10-28 | 22:00 | Dòng thời gian 2.000 năm | Attack on Titan | O · Dòng thời gian | 5 | ? | 4 | 4 | 13 | `videos/2026-10-28-dong-thoi-gian-attack-on-titan/` | Kịch bản xong — chờ kiểm nguồn |
| 70 | 2026-10-29 | 06:00 | Chi tiết cài cắm về Himmel | Frieren | R · Cài cắm và chi tiết ẩn | 5 | ? | 5 | 4 | 14 | `videos/2026-10-29-cai-cam-himmel-frieren/` | Kịch bản xong — chờ kiểm nguồn |
| 71 | 2026-10-29 | 14:00 | Hồ sơ 9 Vĩ thú | Naruto | E · Hồ sơ bách khoa | 5 | ? | 4 | 5 | 14 | `videos/2026-10-29-ho-so-vi-thu-naruto/` | Kịch bản xong — chờ kiểm nguồn |
| 72 | 2026-10-29 | 22:00 | 10 hiểu lầm phổ biến | Dragon Ball | K · Gỡ hiểu lầm | 5 | ? | 4 | 4 | 13 | `videos/2026-10-29-10-hieu-lam-dragon-ball/` | Kịch bản xong — chờ kiểm nguồn |
| 73 | 2026-10-30 | 06:00 | Từ Gear 2 đến Gear 5 | One Piece | G · Bậc thang tiến hóa | 5 | ? | 4 | 5 | 14 | `videos/2026-10-30-gear-2-den-gear-5/` | Kịch bản xong — chờ kiểm nguồn |
| 74 | 2026-10-30 | 14:00 | Phân tích trận Netero vs Meruem | Hunter x Hunter | M · Phân tích trận đấu | 5 | ? | 5 | 4 | 14 | `videos/2026-10-30-tran-netero-meruem/` | Kịch bản xong — chờ kiểm nguồn |
| 75 | 2026-10-30 | 22:00 | Xếp hạng "vũ khí" của các tiền đạo | Blue Lock (mùa 3 xuân 2027) | J · Xếp hạng có tiêu chí | 4 | ? | 4 | 4 | 12 | `videos/2026-10-30-xep-hang-vu-khi-blue-lock/` | Kịch bản xong — chờ kiểm nguồn |
| 76 | 2026-10-31 | 06:00 | Nhập môn thế giới yêu đao | Kagurabachi (ra mắt tháng 4/2027) | Q · Nhập môn | 5 | ? | 4 | 5 | 14 | `videos/2026-10-31-nhap-mon-kagurabachi/` | Kịch bản xong — chờ kiểm nguồn |
| 77 | 2026-10-31 | 14:00 | Bí ẩn thân thế Jinshi (lý thuyết có gắn nhãn) | Dược sư tự sự (phần 2 tháng 4/2027) | N · Điều tra bí ẩn | 5 | ? | 4 | 4 | 13 | `videos/2026-10-31-bi-an-than-the-jinshi/` | Kịch bản xong — chờ kiểm nguồn |
| 78 | 2026-10-31 | 22:00 | Ba hệ kiếm thuật: Hơi thở vs kiếm Haki vs yêu đao | Kimetsu / One Piece / Kagurabachi | I · So sánh chéo có chấm điểm | 4 | ? | 5 | 4 | 13 | `videos/2026-10-31-ba-he-kiem-thuat/` | Kịch bản xong — chờ kiểm nguồn |

Chi phí và chi tiết từng video: xem `docs/ke-hoach-noi-dung.md`.

**Ý tưởng dự trữ** (chưa xếp lịch):

- bí ẩn cổng trong Solo Leveling;
- Daemons of the Shadow Realm nhập môn, khi có đủ nguồn;
- Jujutsu Kaisen: ôn tập trước mùa 4 (dạng T), khi có ngày phát chính thức;
- Frieren: ôn tập trước arc Vùng đất Hoàng kim (dạng T, dự kiến tháng 10/2027);
- Phiên tòa: Light Yagami hoặc Itachi (dạng U);
- Dandadan mùa 3, Chainsaw Man arc Sát thủ (khi có lịch phát);
- Thám tử lừng danh Conan: dòng thời gian Tổ chức Áo đen (dạng O).
