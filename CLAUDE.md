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

- `.claude/skills/` chứa 292 skills lấy từ [ECC](https://github.com/affaan-m/ECC) (giấy phép MIT, xem `third_party/ecc/LICENSE`). Phiên bản đang dùng ghi trong `third_party/ecc/SOURCE`.
- Không sửa trực tiếp các skill ECC: lần đồng bộ sau sẽ ghi đè. Muốn tùy biến thì tạo skill mới với tên khác.
- Cập nhật từ upstream: `scripts/sync-ecc-skills.sh` (hoặc `scripts/sync-ecc-skills.sh <tag>` để chọn phiên bản).
