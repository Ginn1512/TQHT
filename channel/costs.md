# Sổ chi phí

Ngân sách: **200 USD/tháng** từ tháng 10/2026, chỉ dùng cho ảnh và giọng đọc (`tools/config.py`: `MONTHLY_BUDGET_USD`).

- 30/09/2026: người dùng chọn 3 video/ngày và làm ảnh qua API, nâng trần từ 38 USD (1.000.000đ) lên 200 USD.
- Trần mỗi video: 2,5 USD.
- Tháng 10 (78 video) ước tính 220–236 USD nếu mọi cảnh là ảnh AI, khoảng 195 USD khi 20–30% cảnh thay bằng thẻ vẽ bằng code. Có thể vượt trần khoảng 20–36 USD nếu công cụ thẻ chưa xong.
- Vẫn báo ước tính (`python -m tools.costs estimate`) và chờ người dùng đồng ý trước mỗi lần gọi API tốn tiền.
`tools/costs.py record` tự thêm dòng vào bảng dưới đây sau mỗi video.

| Tháng | Video | Ảnh | Giây giọng đọc | Chi phí (USD) |
|-------|-------|-----|----------------|---------------|
