---
name: yt-research
description: Nghiên cứu ngách anime trước mỗi đợt kịch bản. Tìm anime đang hot theo mùa, xem các kênh giải thích/review anime khác đang làm dạng video gì, xác minh hệ thống sức mạnh của bộ sắp làm, rồi ghi 3 điều học được vào nhật ký. Dùng khi người dùng muốn chọn chủ đề mới, lên lịch nội dung, hoặc trước khi /yt-studio viết kịch bản cho bộ chưa từng làm.
---

# yt-research: luôn nghiên cứu trước khi viết

Mục tiêu: kênh luôn học từ các kênh khác mà **không sao chép**. Kịch bản chỉ dùng `channel/profile.md` và `channel/references/nhat-ky-hoc-hoi.md`, không dùng lời thoại của kênh khác.

## 1. Anime đang hot (WebSearch)

- Tìm theo mùa hiện tại và mùa tới: `anime <mùa> <năm> most anticipated`, `anime <mùa> <năm> ranking`, và lịch phát của các bộ lớn.
- Với mỗi bộ, ghi vào `channel/references/nghien-cuu-nganh-<năm>.md`: tên, ngày phát, số tập, nơi phát, nguồn.
- Bộ nào đang phát trong 1–3 tháng tới thì cộng điểm "Nhu cầu" trong `channel/topics.md`.

## 2. Kênh tham khảo

- Có `TRANSCRIPT_API_KEY`:
  - chạy `python -m tools.yt_research outliers @handle` cho 5 kênh mẫu và 2–3 kênh giải thích anime khác;
  - chỉ ghi **tiêu đề, dạng video và hệ số vượt trội**, không chép lời thoại.
- Chưa có key: WebSearch tên kênh cùng các từ "anime explained", "power system", "video essay"; ghi dạng video họ làm.
- Ghi mỗi kênh một dòng: tên, quy mô, dạng video đáng học, nguồn.

## 3. Xác minh hệ thống sức mạnh của bộ sắp làm

- Tìm 2 nguồn độc lập cho mỗi luật hoặc con số sẽ đưa vào kịch bản.
- Trang nào bị chặn (fandom, wiki…) thì dùng đoạn trích trong kết quả tìm kiếm và ghi "cần kiểm lại".
- Chỗ chưa chắc thì chọn góc "nhập môn" hoặc "lý thuyết có gắn nhãn" thay vì khẳng định.

## 4. Chính sách YouTube

- Tìm `YouTube inauthentic content policy <năm>` và `YouTube monetization policy update <tháng> <năm>`.
- Có thay đổi thì cập nhật mục "Chính sách" trong file nghiên cứu, và sửa `channel/formats.md` nếu cần.

## 5. Ghi 3 điều học được

Thêm một mục mới lên đầu `channel/references/nhat-ky-hoc-hoi.md`:

```markdown
## <YYYY-MM-DD>: trước đợt <tên đợt>

1. **<điều học được>** (<kênh hoặc nguồn>). **Áp dụng:** <thay đổi cụ thể cho kịch bản, dạng video hoặc thumbnail>.
2. …
3. …
```

Mỗi điều phải dẫn tới **một thay đổi cụ thể** (một dạng video mới, một cách mở đầu, một kiểu thumbnail), không ghi chung chung.

## 6. Chọn dạng video

- Mỗi chủ đề mới gắn một mã dạng trong `channel/formats.md`.
- Chạy `python -m tools.plan_check`: không có 2 video liền nhau cùng dạng, mỗi dạng tối đa 2 lần trong 30 video.
- Báo người dùng danh sách chủ đề và dạng video, chờ duyệt rồi mới viết kịch bản.
