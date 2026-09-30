# Chính sách nội dung: video AI nguyên bản, đúng luật YouTube

Tài liệu này đưa bộ "Claude Code YouTube Clone Skills — Policy Safe" (người dùng gửi ngày 30/09/2026) vào quy trình của kênh Cú Kaku.

Trong tài liệu gốc, "clone" chỉ có nghĩa là **học** cấu trúc, quy trình và chủ đề của kênh tham khảo. Không sao chép video, transcript, giọng, khuôn mặt, thương hiệu, logo hay thumbnail của kênh khác.

## 9 nguyên tắc, áp vào kênh anime

| # | Nguyên tắc | Ở kênh Cú Kaku |
|---|---|---|
| 1 | AI hỗ trợ, người chịu trách nhiệm ý tưởng, kiểm chứng, quyền tài sản và quyết định đăng | Người giữ 2 cổng: merge kịch bản và quyết định trong `audit.md` (`Decision: publish`) |
| 2 | Mỗi video có luận điểm, phân tích, ví dụ hoặc dữ liệu riêng | Dòng "Luận điểm riêng" trong `brief.md`, chương "Góc nhìn của Kaku", điểm `originality` từ 12/16 |
| 3 | Không đăng lại video, nhạc, hình của người khác khi chưa có quyền | Không dùng cảnh phim, ảnh chụp màn hình, trang manga, art chính thức; mọi tài sản nằm trong `rights.csv` |
| 4 | Không dùng giọng, khuôn mặt, hình của người thật để khiến người xem tin điều không xảy ra | Giọng Kaku thiết kế bằng mô tả, không clone; dạng S dùng bóng người, không vẽ chân dung theo ảnh |
| 5 | Không làm hàng loạt video gần như giống nhau bằng một khuôn | 21 dạng video (`channel/formats.md`), luật `plan_check`, đo độ trùng bằng `originality scan` |
| 6 | Không bot, không traffic ảo | Danh sách việc tay trong `release_check`, checklist trong `audit.md` |
| 7 | Hình, âm thanh trông như thật do AI tạo thì xem xét khai báo | `release_check` gợi ý tick cho dạng S và prompt có từ chỉ ảnh chân thực |
| 8 | Sức khỏe, pháp lý, tài chính, chính trị: không giả chuyên gia, dùng nguồn chính thức | Kênh anime ít gặp. Dạng P (khoa học) có câu "đây không phải hướng dẫn"; mục "Rủi ro bản quyền/chính sách" trong `brief.md` |
| 9 | Không xác định được nguồn, giấy phép hay độ chính xác thì ghi UNKNOWN và chặn đăng | Dòng UNKNOWN trong `rights.csv`, khẳng định chưa kiểm trong `canon`, tiêu chí chưa chấm trong `originality`: đều là LỖI |

## Tài liệu gốc ánh xạ vào dự án

| Skill trong tài liệu | Ở dự án | Công cụ |
|---|---|---|
| channel-profile | `channel/profile.md`, `/yt-analyzer` | danh sách CẤM (mục 10) |
| topic-research | `/yt-research`, `brief.md`, `/kaku-canon-ledger` | `tools.canon` |
| originality-check | `/kaku-originality-check` | `tools.originality` |
| script-studio | `/yt-studio` mục 2 | danh sách tự kiểm trong skill |
| visual-plan | `scenes.json`, `prompts.vi.md` | `tools.prompt_check`, `tools.prompt_pack` |
| rights-ledger | `/kaku-rights-audit` | `tools.rights`, `rights.csv`, `channel/rights-registry.json` |
| ai-disclosure-check | `/kaku-release-review` mục 1 | `release_check`: "Gợi ý khai báo AI", khối YAML trong `audit.md` |
| youtube-metadata | `/kaku-release-review` mục 1 | `release_check`: tiêu đề câu kéo, link ngoài, tiết lộ tài trợ |
| publish-gate | `/kaku-release-review` | `release_check --write-audit`, `audit.md` |

Tên lệnh `/clone-safe-*` của tài liệu **không dùng**. Skill của dự án phải có tiền tố `kaku-` hoặc `yt-` (xem `CLAUDE.md`).

## Các cổng chặn theo thứ tự làm

| Lúc | Cổng | Lệnh | Chặn khi |
|---|---|---|---|
| Sau kịch bản, trước ảnh và giọng | Độ nguyên bản | `python -m tools.originality check` | dưới 12/16, hoặc có đoạn chỉ đọc lại nguồn |
| Trước giọng | Nguồn | `python -m tools.canon check` | còn khẳng định chưa kiểm |
| Sau khi nhập ảnh và giọng | Quyền tài sản | `python -m tools.rights check` | dòng UNKNOWN, công cụ chưa `da-kiem` hoặc bị cấm, giấy phép hết hạn |
| Trước khi đăng | Cổng đăng | `python -m tools.release_check --write-audit` | còn LỖI, hoặc `audit.md` chưa có `Decision: publish` |

Luôn làm bằng tay trong YouTube Studio (danh sách cuối lệnh `release_check`):

- chọn nhãn "Altered or synthetic content";
- không mua view hay dùng bot;
- tiêu đề và thumbnail không dùng người hay sự kiện không có trong video.

## Ví dụ phù hợp với kênh

- Video "Nen hoạt động thế nào?" có:
  - bảng phần trăm lục giác tự dựng;
  - lập luận riêng "Gon trả giá bằng chính luật giao ước";
  - nguồn wiki đã mở và ghi ngày kiểm;
  - tranh sổ tay tự vẽ bằng AI, không có nhân vật chính thức.
- Video dạng S về Tần Thủy Hoàng dùng bóng người và đồ vật thời đó, nói rõ chỗ nào là hư cấu của tác giả. Metadata ghi "Tick" vì chủ đề là người thật.

## Ví dụ không phù hợp

- Cắt cảnh anime, thêm giọng AI đọc tóm tắt.
- Cho AI đọc lại nguyên văn một bài wiki trên nền ảnh slideshow.
- Làm 30 video "10 sự thật về <tên anime>" cùng một khuôn, chỉ đổi tên bộ.
- Thumbnail có mặt diễn viên lồng tiếng hay tác giả không xuất hiện trong video.
- Lời kêu gọi kiểu "like đủ 1.000 thì Kaku tiết lộ phần 2".
- Bịa lời phỏng vấn tác giả.

## Rủi ro lớn nhất của kênh lúc này

- **Nhịp 3 video/ngày** từ 06/10: cả 78 video dùng chung linh vật, phong cách hình và khung kịch bản. Theo tiêu chí của tài liệu, `audit.md` ghi rủi ro "inauthentic" là **high** cho mọi video đăng hơn 1 video/ngày. Đây là dữ liệu cho lần xét nhịp ngày 25/10 (`docs/lo-trinh.md`).
- **Điều khoản ảnh Gemini chưa kiểm:** mọi video dùng ảnh Gemini API đều bị chặn ở cổng quyền tài sản cho tới khi mục `gemini-image-api` trong `channel/rights-registry.json` được kiểm. Trang điều khoản bị chặn trong phiên cloud, nên người dùng cần mở trang để xác nhận **trước 06/10**.
- **Nguồn:** 33/78 video có dưới một nửa số khẳng định kèm link (đo ngày 30/09/2026). Các video này bị chặn ở tiêu chí `nguon` cho tới khi làm `/kaku-canon-ledger`.

## Nguồn chính sách cần theo dõi

Chưa mở được trong phiên này vì mạng chặn `support.google.com`. **Cần kiểm lại** trước khi bật kiếm tiền và mỗi quý một lần:

- [Chính sách kiếm tiền trên kênh YouTube](https://support.google.com/youtube/answer/1311392?hl=vi): nội dung dùng lại (reused) và nội dung không chân thực (inauthentic). Theo hiểu biết tới giữa năm 2025, YouTube đổi tên mục "repetitious content" thành "inauthentic content" từ tháng 7/2025. Chưa đối chiếu trên trang.
- [Công bố nội dung nhân tạo hoặc đã chỉnh sửa](https://support.google.com/youtube/answer/14328491?hl=vi)
- [Chính sách spam, hành vi lừa đảo và câu kéo](https://support.google.com/youtube/answer/2801973?hl=vi)
- [Sử dụng hợp lý (fair use) trên YouTube](https://support.google.com/youtube/answer/9783148?hl=vi)

Chính sách có thể thay đổi. Trước khi tự động hóa quy mô lớn, cần kiểm lại các trang chính thức và đăng thử có người duyệt.
