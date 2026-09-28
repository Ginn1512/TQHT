# CLAUDE.md

## Ngôn ngữ

- Luôn trả lời người dùng bằng **tiếng Việt**: giải thích, kế hoạch, tóm tắt, câu hỏi.
- Giữ nguyên tiếng gốc cho code, tên biến/hàm, lệnh terminal và thông báo lỗi.

## Cách làm việc: Suy nghĩ → Kế hoạch → Chiến lược → Thực hiện

Với mọi yêu cầu, trước khi bắt tay vào làm:

1. **Phân tích**: nêu rõ mục tiêu, bối cảnh và các ràng buộc. Nếu yêu cầu mơ hồ ở điểm ảnh hưởng tới kết quả thì hỏi lại.
2. **Kế hoạch**: chia công việc thành các bước cụ thể, có thứ tự.
3. **Chiến lược**: chọn hướng tiếp cận, nêu lý do và rủi ro chính. Nếu có nhiều phương án, đề xuất một phương án thay vì liệt kê dàn trải.

Sau đó mới thực hiện, rồi kết thúc bằng:

- **Kết quả**: đã làm gì, đã kiểm chứng ra sao (hoặc chưa kiểm chứng được gì).
- **Bước tiếp theo**: việc nên làm tiếp, nếu có.

## Skills

- `.claude/skills/` chứa 30 skill chọn lọc từ [ECC](https://github.com/affaan-m/ECC) (giấy phép MIT, xem `third_party/ecc/LICENSE`), liệt kê trong `third_party/ecc/keep.txt`. Phiên bản đang dùng ghi trong `third_party/ecc/SOURCE`.
- Không sửa trực tiếp các skill ECC: lần đồng bộ sau sẽ ghi đè. Muốn tùy biến thì tạo skill mới với tên khác.
- Cập nhật từ upstream: `scripts/sync-ecc-skills.sh` (hoặc `scripts/sync-ecc-skills.sh <tag>` để chọn phiên bản). Thêm/bớt skill: sửa `keep.txt` rồi chạy lại script.
- Skill riêng của dự án (tên bắt đầu bằng `yt-`) không nằm trong ECC, được sửa trực tiếp.

## Dự án: kênh YouTube phân tích anime

Kênh tiếng Việt, video phân tích/giải thích anime dài 15–20 phút (tối thiểu 15 phút), hình AI tự vẽ, lồng tiếng thêm theo lộ trình ghi trong `channel/profile.md`.

Lộ trình và trạng thái: `docs/lo-trinh.md` (khi đổi, cập nhật cả trang xem trên điện thoại https://claude.ai/code/artifact/52493995-899b-4a48-a7b4-440e38690e4f).

### Cấu trúc

- `channel/profile.md`: hồ sơ kênh, nguồn sự thật duy nhất về giọng văn, cấu trúc, phong cách hình và danh sách CẤM.
- `channel/references/<handle>.md`: phân tích từng kênh mẫu.
- `channel/topics.md`: danh sách chủ đề đã chấm điểm, kèm dạng video và ngày đăng.
- `channel/formats.md`: danh mục dạng video (A–R) và khung của từng dạng.
- `channel/references/nghien-cuu-nganh-<năm>.md` và `nhat-ky-hoc-hoi.md`: nghiên cứu ngách và 3 điều học được mỗi đợt.
- `channel/costs.md`: sổ chi phí.
- `videos/<YYYY-MM-DD>-<slug>/`: mỗi video một thư mục gồm `brief.md`, `script.vi.md`, `scenes.json`, `metadata.<lang>.md`, `cost.json`. Hai thư mục `assets/` và `render/` bị gitignore.
- `tools/`: công cụ Python (TranscriptAPI, Gemini TTS/ảnh, ffmpeg). Cài bằng `pip install -r tools/requirements.txt`, chạy test bằng `pytest tools/tests`.

### Quy trình

1. `/yt-analyzer`: phân tích kênh mẫu, cập nhật `channel/profile.md`.
2. `/yt-research`: **luôn chạy trước mỗi đợt kịch bản** (hoặc khi nhật ký học hỏi đã quá 2 tuần). Tìm anime hot, xem các kênh anime khác làm gì, ghi 3 điều học được.
3. `/yt-studio`: từ chủ đề đến video MP4 hoàn chỉnh và gói thông tin đăng tải.
4. `/yt-seedance` (tuỳ chọn): tối đa 6 clip Seedance 2.5 × 5 giây cho cảnh "đinh"; mặc định làm thủ công trên app Dreamina/CapCut.

### Quy tắc cứng

- **Không dùng cảnh phim, ảnh chụp màn hình, trang manga hay art chính thức.** Chỉ dùng hình AI tự tạo, chữ và sơ đồ.
- Mọi thông tin thật trong kịch bản phải có nguồn, ghi trong `brief.md`.
- Khi viết kịch bản, không nạp transcript của kênh mẫu; chỉ dùng `channel/profile.md` và `nhat-ky-hoc-hoi.md`.
- Mỗi video theo một dạng trong `channel/formats.md`: không có 2 video liền nhau cùng dạng, mỗi dạng tối đa 2 lần trong 30 video. Kiểm tra bằng `python -m tools.plan_check`.
- **Trước mỗi lần gọi API tốn tiền** (tạo ảnh, giọng đọc): báo ước tính chi phí bằng `python -m tools.costs estimate` và chờ người dùng đồng ý.
- Key API chỉ đọc từ biến môi trường `TRANSCRIPT_API_KEY` và `GEMINI_API_KEY`. Không bao giờ yêu cầu người dùng dán key vào chat.
- Video MP4 gửi cho người dùng bằng SendUserFile, không commit lên git.
