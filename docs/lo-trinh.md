# Lộ trình kênh anime AI

> Bản chính của lộ trình. Bản xem trên điện thoại: https://claude.ai/code/artifact/52493995-899b-4a48-a7b4-440e38690e4f
> Khi cập nhật file này, cập nhật cả trang đó.
> Cập nhật lần cuối: 2026-09-30 (mục tiêu YPP trong 1–3 tháng, làm tay trước; Xưởng Kaku; Shorts; 78 kịch bản; hạn chót YPP 31/01/2027; tự động hóa bằng agent bắt đầu ngay, P0–P3).

## Mục tiêu và quyết định đã chốt

**Mục tiêu:** một kênh YouTube tiếng Việt phân tích anime, làm video bằng AI, đủ điều kiện kiếm tiền (YPP) trong 1–3 tháng.

- **Cách làm:**
  - **Làm tay trước** để chi phí gần 0: ảnh bằng Gemini app (gói Gemini Plus), giọng bằng Google AI Studio hoặc ElevenLabs, dùng prompt soạn sẵn.
  - **Tự động hóa bằng agent Claude Code, bắt đầu ngay:** 2 làn (chữ trên cloud, media trên PC), 7 agent, người giữ 2 cổng (merge kịch bản, tự tải lên). Xem `docs/tu-dong-hoa-agent.md`.
- **Định dạng:**
  - 3 video dài 15–20 phút mỗi tuần (thứ Ba, thứ Năm, thứ Bảy);
  - 1 Short mỗi ngày, cắt từ video dài.
- **Hình ảnh:** tranh AI tự vẽ theo phong cách "Sổ tay Kaku", cộng chữ và sơ đồ. Không dùng cảnh phim, trang manga hay art chính thức.
- **Ngôn ngữ:** tiếng Việt trước. Chỉ thêm lồng tiếng Anh và Bồ Đào Nha sau khi được bật kiếm tiền và bản tiếng Việt đã ổn định.
- **Ngân sách:** trần 1.000.000đ/tháng (khoảng 38 USD). Khi làm tay thì gần như 0 USD; tiền gói Claude và Gemini Plus trả riêng.
- **Kênh mẫu:** @quinquinreview, @canalmangaq, @hashiranosekai, @meoluoilongtieng, @mikoreview-f6t.

### Điều kiện YPP và con số cần đạt

- **Đường video dài:** 1.000 người đăng ký + 4.000 giờ xem công khai trong 12 tháng.
  - Trong 90 ngày, 4.000 giờ tương đương khoảng 45 giờ/ngày, tức khoảng 450 lượt xem mỗi ngày nếu mỗi lượt xem trung bình 6 phút.
- **Đường Shorts:** 1.000 người đăng ký + 10 triệu lượt xem Shorts trong 90 ngày.
- **Mốc sớm (YPP mở rộng):** 500 người đăng ký + 3 video công khai trong 90 ngày + 3.000 giờ xem (hoặc 3 triệu lượt xem Shorts). Mốc này mở hội viên và Super Thanks, **chưa có tiền quảng cáo**. Việt Nam nằm trong danh sách được áp dụng; kiểm tra trong YouTube Studio → Kiếm tiền.
- **Nói thẳng:** 1–3 tháng là mục tiêu tham vọng. Nhiều kênh mới mất 6–12 tháng. Muốn kịp thì cần 1–2 video "nổ", nên kế hoạch có mốc kiểm tra để đổi hướng sớm.
- Sau khi nộp đơn, YouTube thường xét duyệt trong khoảng 1 tháng.
- **Hạn chót thật: 31/01/2027.** YouTube công bố ngày 10/8/2026: từ **01/02/2027**, kênh mới nộp đơn cần 1.000 người đăng ký + **8.000 giờ xem** trong 365 ngày (gấp đôi hiện nay), hoặc **20 triệu** lượt xem Shorts trong 90 ngày.
  - Nộp đơn **trước 01/02/2027** thì được xét theo mức cũ (4.000 giờ hoặc 10 triệu lượt xem Shorts).
  - Mốc YPP mở rộng (500 người đăng ký + 3.000 giờ xem) giữ nguyên.
  - Vì vậy, chủ đề tháng 1/2027 (video 39–51) được dồn vào các bộ có nhu cầu cao nhất.
  - Nguồn: [YouTube Blog](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/), [vidIQ](https://vidiq.com/blog/post/youtube-partner-program-changes-2027/), [9to5Google](https://9to5google.com/2026/08/10/youtube-premium-lite-expansion-monetization-changes/), [tbreak](https://tbreak.com/youtube-partner-program-8000-watch-hours/). Chi tiết: `channel/references/nghien-cuu-nganh-2026.md`.

## Trạng thái

- [x] 30 skill ECC trong repo
- [x] Công cụ Python (`tools/`), 117 test đạt
- [x] Skill `/yt-analyzer`, `/yt-research`, `/yt-studio`, `/yt-seedance`
- [x] `channel/profile.md` bản sơ bộ, nghiên cứu ngách 2026, nhật ký học hỏi
- [x] 21 dạng video (`channel/formats.md`, thêm S, T, U), 78 chủ đề (`channel/topics.md`)
- [x] Kịch bản video 1–30, mỗi video 15,3–16,2 phút, dùng 17 dạng khác nhau
- [x] Kịch bản video 31–78 (15/12/2026 → 03/04/2027), mỗi video 15,3–17,5 phút; tổng 78 kịch bản dùng 21 dạng, đạt `plan_check`
- [x] Lịch 90 ngày: video 1–30 đăng từ 06/10 đến 12/12/2026, 3 video/tuần; video 31–78 tiếp tục cùng nhịp tới 03/04/2027
- [x] Phong cách hình "Sổ tay Kaku" và khuôn prompt ảnh 6 lớp (cả 6.713 cảnh của 78 video đều có cỡ cảnh và ánh sáng)
- [x] Bộ prompt làm tay cho cả 78 video (`videos/*/prompts.vi.md`): ảnh, cộng giọng bản Gemini và bản ElevenLabs
- [x] Trang "Xưởng Kaku" cho video 1 (Ảnh / Giọng / Kiểm tra): https://claude.ai/artifact/JZThW5cMae5U9pbrvRsYSr
- [x] Công cụ nhập giọng làm tay (tự cắt thành từng cảnh) và công cụ cắt Short dọc
- [x] Lộ trình tự động hóa Notion + n8n (`docs/tu-dong-hoa.md`), nay đã được thay
- [x] Chiến lược tự động hóa bằng agent (`docs/tu-dong-hoa-agent.md`), trang điện thoại: https://claude.ai/code/artifact/7608e62b-19ff-4147-bce4-b6a2a4e15cae
- [x] Notion "Cú Kaku anime" (riêng tư): https://app.notion.com/p/3ea4a1a7ca3f81ca962ece826fd086f6
  - bảng Video dài (78 video, có Kanban theo trạng thái và lịch đăng);
  - bảng Shorts;
  - bảng Chỉ số tuần (tự tính % tới điều kiện YPP);
  - trang Lộ trình tự động hóa n8n.
- [ ] Chọn giọng Kaku (thử 3 giọng) và tạo ảnh mẫu Kaku
- [ ] Video 1: làm ảnh và giọng trên trang Xưởng → dựng → đăng 06/10
- [ ] Cài `TRANSCRIPT_API_KEY`, mở kết nối `transcriptapi.com` → phân tích 5 kênh mẫu bằng dữ liệu thật, chốt profile ([hướng dẫn](https://claude.ai/artifact/CLeMBD8BXXfBLhcVfbzT6S))
- [ ] Kiểm lại nguồn trong `brief.md` trước khi làm giọng mỗi video
- [ ] Video 2–78 theo lịch (video 31–78 đã có kịch bản, trạng thái "chờ kiểm nguồn")
- [ ] **Trước 31/01/2027:** nộp đơn YPP ngay khi đủ 1.000 người đăng ký + 4.000 giờ xem (hoặc 10 triệu lượt xem Shorts)
- [ ] YPP: 1.000 người đăng ký + 4.000 giờ xem (hoặc 10 triệu lượt xem Shorts)
- [ ] P0 tự động hóa (tới 15/10): xây nền, chạy thử 2 video (`docs/tu-dong-hoa-agent.md` mục 9)
- [ ] P1 (16/10–30/11): lên Max 20x, bật làn chữ trước, rồi làn media; người vẫn tự tải lên
- [ ] P2 (12/2026–01/2027): số liệu và bình luận bằng agent; tải lên qua API nếu kiểm định đạt
- [ ] P3 (sau YPP): lồng tiếng Anh + Bồ Đào Nha, thử nghiệm A/B

## Lộ trình 90 ngày (ngày 0 = 06/10/2026)

| Giai đoạn | Thời gian | Việc chính |
|---|---|---|
| Chuẩn bị | 29/09–05/10 | Chọn giọng Kaku, tạo ảnh mẫu Kaku, làm ảnh và giọng video 1–2; bắt đầu P0 tự động hóa (xây nền) |
| Tháng 1 | 06/10–05/11 | Video 1–14, 1 Short/ngày; đo thời gian làm tay thật; tối ưu thumbnail theo CTR; P0 xong 15/10 (chạy thử 2 video), từ 16/10 P1 bật làn chữ |
| Tháng 2 | 06/11–05/12 | Video 15–27; làm thêm theo chủ đề thắng; bật YPP mở rộng khi đủ 500 người đăng ký; P1 bật làn media |
| Tháng 3 | 06/12–04/01/2027 | Video 28–39; đạt 1.000 người đăng ký + 4.000 giờ xem rồi nộp đơn YPP; P2: số liệu, bình luận |
| Quý 2 | 05/01–03/04/2027 | Video 40–78; nộp đơn YPP trước hạn chót 31/01/2027; chuẩn bị mùa anime tháng 4 (Kagurabachi, Blue Lock mùa 3, Dược sư tự sự mùa 3 phần 2) |
| Sau YPP | từ 02/2027 | P3: lồng tiếng Anh + Bồ Đào Nha, thử nghiệm A/B |

### Mốc kiểm tra

| Mốc | Mục tiêu |
|---|---|
| Ngày 30 (05/11) | 14 video, khoảng 30 Short; từ 200 người đăng ký, từ 800 giờ xem; CTR từ 5%, tỉ lệ giữ chân từ 35% |
| Ngày 60 (05/12) | Từ 500 người đăng ký, từ 2.500 giờ xem |
| Ngày 90 (04/01/2027) | 1.000 người đăng ký + 4.000 giờ xem (hoặc 10 triệu lượt xem Shorts) |
| **Trước 31/01/2027** | **Nộp đơn nếu đủ.** Từ 01/02/2027 kênh mới cần 8.000 giờ xem (hoặc 20 triệu lượt xem Shorts) |

**Luật đổi hướng:** nếu tới ngày 30 chưa đạt 50% mục tiêu:

- chuyển sang các bộ đang hot nhất;
- làm lại thumbnail và tiêu đề của những video có CTR thấp;
- cắt Short từ những đoạn có tỉ lệ giữ chân cao nhất;
- **không tăng số lượng video.** Đăng dày hơn mức một người làm được là dấu hiệu YouTube dùng để đánh giá nội dung "không chân thực".

### Mỗi tuần làm tay khoảng 10–12 giờ

| Việc | Mỗi lần | Mỗi tuần |
|---|---|---|
| Ảnh một video (khoảng 90–104 ảnh trên Gemini app) | 1,5–2 giờ | 4,5–6 giờ |
| Giọng một video (7–9 đoạn đọc) | 30–45 phút | 1,5–2,5 giờ |
| Duyệt video, đăng, trả lời bình luận | 30 phút | 1,5 giờ |
| Duyệt và đăng Short | 10 phút | khoảng 1 giờ |

Khi tự động hóa chạy đủ 2 làn (P1–P2), phần của người còn khoảng 3,3 giờ/tuần, gom vào 2 buổi thứ Hai và thứ Năm (`docs/tu-dong-hoa-agent.md` mục 5).

## Ngân sách mỗi video (15–20 phút)

| Khoản | Làm tay (mặc định) | Qua API (từ P1, khi đã duyệt hạn mức tháng) |
|---|---|---|
| Ảnh (khoảng 90–110 ảnh) | 0, có trong gói Gemini Plus | tối đa 2,5 USD (0,034/ảnh; 20–30% cảnh thay bằng thẻ vẽ bằng code) |
| Giọng tiếng Việt | 0, AI Studio miễn phí hoặc gói ElevenLabs của bạn | 0 với VoiceStudio trên PC; khoảng 0,15–0,2 USD nếu dùng Gemini |
| Short (3 cái mỗi video) | 0, cắt từ video dài | 0 |
| TranscriptAPI | 100 credit miễn phí | 0 |
| Clip Seedance 2.5 (tuỳ chọn, 6 × 5 giây) | 0 nếu dùng credit app Dreamina/CapCut | khoảng 6,9 USD |

Giá lấy từ nguồn thứ ba tháng 9/2026. Giá giọng đọc qua API được báo sẽ tăng gấp đôi từ 01/01/2027.

## Rủi ro

| Rủi ro | Cách phòng |
|---|---|
| Không được bật kiếm tiền (nội dung "không chân thực") | 17 dạng video, góc nhìn riêng, có nguồn; 2 cửa duyệt người; nhịp đăng một người làm được |
| Không kịp 1–3 tháng | Mốc kiểm tra ngày 30/60; Short mỗi ngày; đổi chủ đề, không tăng số lượng |
| Bản quyền anime | Chỉ hình AI tự vẽ; `prompt_check` chặn tên và chi tiết đặc trưng |
| AI bịa thông tin | Mọi thông tin có nguồn trong `brief.md` |
| Kiệt sức vì làm tay | Trang Xưởng chia việc thành từng bước nhỏ; làm dần được; lịch có thể lùi |
| Công cụ làm tay đổi cách dùng hoặc hết lượt | Bộ prompt không phụ thuộc công cụ (Gemini, ElevenLabs, bản thường) |

## Lệnh thường dùng

1. `/yt-studio` cho video tiếp theo: Claude tạo trang Xưởng, bạn làm ảnh + giọng, rồi Claude nhập, dựng, làm 3 Short.
2. `/yt-research`: trước mỗi đợt kịch bản mới (đợt tiếp theo: video 79 trở đi).
3. `/yt-analyzer @quinquinreview @canalmangaq @hashiranosekai @meoluoilongtieng @mikoreview-f6t`: khi đã có `TRANSCRIPT_API_KEY` (khoảng 50 credit).
