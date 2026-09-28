# Lộ trình kênh anime AI

> Bản chính của lộ trình. Bản xem trên điện thoại: https://claude.ai/code/artifact/52493995-899b-4a48-a7b4-440e38690e4f
> Khi cập nhật file này, cập nhật cả trang đó.
> Cập nhật lần cuối: 2026-09-28.

## Mục tiêu và quyết định đã chốt

Một kênh YouTube tiếng Việt phân tích anime, làm video bằng AI, đủ điều kiện kiếm tiền (YPP) trong khoảng 12 tháng.

- **Định dạng:** video phân tích/giải thích anime dài 10–15 phút; Shorts làm sau.
- **Hình ảnh:** tranh AI tự vẽ + chữ + sơ đồ. Không dùng cảnh phim, trang manga hay art chính thức.
- **Ngôn ngữ:** video 1–3 chỉ tiếng Việt → thêm Anh + Bồ Đào Nha (Brazil) → thêm Hindi + Trung phồn thể.
- **Ngân sách:** 1.000.000đ/tháng (khoảng 38 USD) cho ảnh và giọng đọc; tiền gói Claude trả riêng.
- **Kênh mẫu:** @quinquinreview, @canalmangaq, @hashiranosekai, @meoluoilongtieng, @mikoreview-f6t.

## Trạng thái

- [x] 30 skill ECC trong repo
- [x] Công cụ Python (`tools/`), 47 test đạt
- [x] Skill `/yt-analyzer` và `/yt-studio`
- [x] Clip demo dựng thử
- [x] `channel/profile.md` bản sơ bộ (từ tìm kiếm web, chưa có lời thoại video)
- [ ] Cài `TRANSCRIPT_API_KEY`, `GEMINI_API_KEY`, mở kết nối `transcriptapi.com` — xem [hướng dẫn có hình](https://claude.ai/artifact/CLeMBD8BXXfBLhcVfbzT6S)
- [ ] Phân tích 5 kênh mẫu bằng dữ liệu thật, chốt profile
- [ ] Video 1–3 (tiếng Việt)
- [ ] Thêm bản lồng tiếng Anh + Bồ Đào Nha
- [ ] Thêm Hindi + Trung, Shorts
- [ ] YPP: 1.000 người đăng ký + 4.000 giờ xem

## Lộ trình

| Giai đoạn | Thời gian | Việc chính |
|---|---|---|
| Cài đặt và phân tích | Tuần 1 | Cài 2 key, phân tích 5 kênh mẫu, chốt hồ sơ kênh |
| 3 video thử | Tuần 2–4 | Chỉ tiếng Việt; đo chi phí và thời gian thật |
| Nhịp đều + lồng tiếng | Tháng 2 | 2 video/tuần; thêm Anh, Bồ Đào Nha; đọc số liệu hằng tuần |
| Mở rộng | Tháng 3 | Thêm Hindi, Trung phồn thể; cắt Shorts từ video dài |
| Tăng trưởng tới YPP | Tháng 4–12 | 1.000 người đăng ký + 4.000 giờ xem |

Chỉ tăng tần suất và thêm ngôn ngữ khi video trước đạt chất lượng và chi phí dưới 3 USD/video.

## Ngân sách mỗi video (12 phút)

| Khoản | Đơn giá (USD) | Mỗi video (USD) |
|---|---|---|
| Ảnh AI (khoảng 50 ảnh) | 0,034/ảnh | khoảng 1,7 |
| Giọng đọc tiếng Việt | 0,009/phút | khoảng 0,1 |
| Mỗi bản lồng tiếng thêm | 0,009/phút | khoảng 0,1 |
| TranscriptAPI | 100 credit miễn phí | 0 |

Giá lấy từ nguồn thứ ba tháng 9/2026; giá giọng đọc được báo sẽ tăng gấp đôi từ 01/01/2027.

## Rủi ro

| Rủi ro | Cách phòng |
|---|---|
| Không được bật kiếm tiền (nội dung "không chân thực") | 3 bước duyệt, góc nhìn riêng, không lặp khuôn mẫu |
| Bản quyền anime | Chỉ hình AI tự vẽ |
| AI bịa thông tin | Mọi thông tin có nguồn trong `brief.md` |
| Vượt ngân sách | Ước tính trước mỗi video, cảnh báo 35 USD trên Google |
| Ngách kênh AI đông | Linh vật riêng, góc "giải mã hệ thống sức mạnh" |

## Lệnh cần gõ (trong phiên mới, sau khi có key)

1. `/yt-analyzer @quinquinreview @canalmangaq @hashiranosekai @meoluoilongtieng @mikoreview-f6t` — khoảng 50 credit.
2. `/yt-studio` — video 1, khoảng 2 USD, có bước chờ duyệt.
