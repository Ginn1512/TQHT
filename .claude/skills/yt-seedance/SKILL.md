---
name: yt-seedance
description: Thiết kế và xuất prompt Seedance 2.5 (ảnh → video) cho vài cảnh "đinh" của một video kênh anime, rồi ghép clip vào video dựng bằng tools.assemble. Dùng khi người dùng muốn thêm chuyển động thật/clip AI, nhắc tới Seedance, Dreamina, CapCut AI video hay "làm video bằng AI video".
---

# yt-seedance: clip Seedance cho cảnh "đinh"

Seedance 2.5 đắt: khoảng 0,23 USD/giây (Replicate, 720p) đến 0,47 USD/giây (fal). Làm cả video 15–20 phút bằng Seedance tốn 200–450 USD, vượt xa ngân sách 38 USD/tháng. Quy tắc của kênh:

- **Tối đa 6 clip × 5 giây mỗi video** (khoảng 30 giây, khoảng 7 USD qua API). Phần còn lại vẫn là ảnh + chuyển động nhẹ.
- Ưu tiên làm thủ công trên app **Dreamina / CapCut** (điện thoại) bằng credit của gói; chỉ dùng API khi người dùng đồng ý chi phí.
- Chạy `python -m tools.costs estimate` và chờ người dùng duyệt trước khi tạo clip qua API.

## 1. Chọn cảnh "đinh"

Chọn tối đa 6 cảnh mà chuyển động làm tăng cảm xúc hoặc làm rõ ý:
- câu mở đầu (0–30 giây) và khoảnh khắc cao trào của câu chuyện;
- linh vật chào lúc mở đầu (tạo nhận diện kênh);
- lần đầu một sơ đồ quan trọng xuất hiện (ví dụ hình lục giác quay);
- một thí nghiệm/hiện tượng dễ thấy bằng chuyển động (nước tràn, xích quấn).

Không chọn cảnh chỉ để giải thích bằng chữ; ảnh tĩnh làm việc đó tốt hơn và rẻ hơn.

## 2. Viết `video_prompt` trong `scenes.json`

Thêm vào cảnh: `"video_prompt": "..."`, `"clip_seconds": 5` (4–10). `video_prompt` chỉ mô tả **chuyển động và máy quay**, vì bố cục đã có trong ảnh tham chiếu:
- một hành động chính + điểm kết (ví dụ: "the seal cracks, a chain unwinds and wraps the frame");
- một kiểu máy quay: slow push-in / dolly-in / orbit / pull back / static macro;
- chi tiết không khí: embers, dust, particles, rain;
- nhân vật người: "no face shown" hoặc dáng từ phía sau, để không giống nhân vật có bản quyền.

`tools/seedance.py` tự ghép thêm phong cách, linh vật và câu chặn (không chữ, không logo, không lời thoại, không nhân vật có sẵn).

## 3. Xuất prompt và làm clip

```bash
python -m tools.images videos/<thư-mục>        # ảnh tham chiếu (khung đầu) cho từng cảnh
python -m tools.seedance videos/<thư-mục>      # → seedance.md
```

Gửi `seedance.md` và các ảnh `assets/images/<id>.png` của cảnh "đinh" cho người dùng (SendUserFile). Trên app: chọn ảnh → video, tải ảnh làm khung đầu, dán prompt, 16:9, đúng số giây, tắt âm thanh. Người dùng gửi lại clip; lưu thành `videos/<thư-mục>/assets/clips/<id>.mp4`.

## 4. Ghép vào video

```bash
python -m tools.assemble videos/<thư-mục>
```

Cảnh có clip sẽ dùng clip (tự lặp/cắt cho đủ độ dài giọng đọc, bỏ tiếng gốc, vẫn phủ chữ trên màn hình). Xem 2–3 khung hình ở các cảnh clip để kiểm tra chỗ nối.

## Khi nào dùng API

Khi đã có key và tên miền được phép (ví dụ Replicate hoặc BytePlus ModelArk), có thể thêm công cụ gọi API. Trước đó phải: báo chi phí thật, người dùng đồng ý, và thêm key vào biến môi trường (không bao giờ nhận key qua chat).
