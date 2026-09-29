---
name: kaku-canon-ledger
description: Lập và kiểm sổ khẳng định về anime (channel/canon-ledger.md) từ bảng "Sự thật dùng trong kịch bản" của mọi brief.md — mở trang nguồn, ghi link đã kiểm vào brief, sửa kịch bản khi sai, và chặn bước làm giọng khi video còn khẳng định chưa kiểm. Dùng khi người dùng muốn kiểm nguồn, fact-check một video hay một bộ anime, trước khi làm giọng video nào, hoặc khi hỏi còn bao nhiêu chi tiết "cần kiểm lại".
---

# kaku-canon-ledger: mỗi khẳng định một nguồn đã mở

`brief.md` là nguồn gốc. `channel/canon-ledger.md` được tạo tự động bằng `python -m tools.canon build` và **không sửa tay**.

Các mức của từng dòng:

| Mức | Nghĩa | Tính là |
|---|---|---|
| `da-kiem` | có "đã kiểm YYYY-MM-DD" | đã kiểm |
| `co-nguon` | có link, không kèm lời dè dặt | đã kiểm |
| `y-kien` | ý kiến, trò chơi của kênh, hoặc lý thuyết đã gắn nhãn trong kịch bản | không cần nguồn |
| `chua-mo` | chỉ thấy trong kết quả tìm kiếm, chưa mở trang | **chưa kiểm** |
| `can-kiem` | có chữ "cần kiểm lại" hoặc "cần thêm nguồn" | **chưa kiểm** |
| `khong-ro` | không có link, không có nhãn | **chưa kiểm** |

## 0. Xem hiện trạng

```bash
python -m tools.canon build                       # cập nhật sổ, in dòng tóm tắt
python -m tools.canon check videos/<thư-mục>       # các dòng chưa kiểm của một video (mã 1 nếu còn)
```

- Kiểm **một video**: dùng trước bước làm giọng của video đó.
- Kiểm **một bộ**: dùng mục "Chưa kiểm, gom theo bộ" trong sổ. Cùng một chi tiết thường xuất hiện ở nhiều video của cùng bộ (One Piece có 6 video, Naruto 5).

## 1. Kiểm từng dòng

1. **Mở trang nguồn** bằng WebFetch. Đoạn trích trong kết quả tìm kiếm không được tính.
   - Nên dùng: wiki của bộ (Fandom), Wikipedia, trang tin anime uy tín (Anime News Network, Crunchyroll News), trang chính thức.
   - Nếu trang bị chặn, thử nguồn khác. Không có nguồn nào mở được thì ghi rõ và để dòng ở mức chưa kiểm.
2. **Dòng gộp nhiều chi tiết**, ví dụ "tên kỹ năng, tỉ lệ lục giác, lời Wing…": tách thành nhiều dòng trong bảng của `brief.md` trước, mỗi dòng một khẳng định. Sau đó kiểm từng dòng.
3. **Khớp với nguồn:**
   ```bash
   python -m tools.canon resolve videos/<thư-mục> <số dòng> --source "[Tên trang](https://…)"
   ```
   Lệnh ghi link và ngày kiểm vào đúng dòng, cho cả bảng 2 cột lẫn 3 cột.
4. **Sai so với nguồn:**
   - Sửa lời thoại cảnh liên quan trong `scenes.json`, và sửa `script.vi.md` cho khớp.
   - Sửa chữ của dòng trong `brief.md`, rồi `resolve`.
   - Chạy `python -m tools.prompt_pack videos/<thư-mục>` và `python -m tools.plan_check`, vì độ dài vẫn phải từ 15 phút.
   - Báo người dùng **từng câu đã đổi**: id cảnh, câu cũ, câu mới, nguồn.
5. **Không tìm được nguồn:** chọn một trong ba cách, và báo người dùng đã chọn cách nào:
   - đổi câu trong kịch bản thành không khẳng định ("nhiều fan cho rằng…") và gắn nhãn LÝ THUYẾT, rồi ghi ô tình trạng là "Lý thuyết, gắn nhãn trong kịch bản";
   - bỏ chi tiết khỏi kịch bản;
   - giữ nguyên ở mức chưa kiểm.
6. Mâu thuẫn giữa hai video cùng bộ: sửa cả hai, theo nguồn.

**Không bao giờ** đánh dấu đã kiểm khi chưa mở trang. **Không bao giờ** tự đổi một sự thật sang ý kiến chỉ để qua cửa kiểm.

## 2. Kết thúc

```bash
python -m tools.canon build
python -m tools.canon check videos/<thư-mục>    # phải báo "Làm giọng được"
pytest tools/tests/test_canon.py                 # có bài kiểm sổ khớp các brief.md
```

- Commit `brief.md`, `channel/canon-ledger.md`, và `scenes.json` / `script.vi.md` / `prompts.vi.md` nếu có sửa. Rồi push.
- Báo lại:
  - số dòng đã kiểm;
  - các câu kịch bản đã đổi;
  - số dòng còn lại của video;
  - số dòng còn lại của cả kênh (dòng tóm tắt của `build`).

## Luật nối với các skill khác

- `/yt-studio` mục 5: **chỉ làm giọng khi `canon check` của video đó đạt**. Nếu người dùng muốn làm trước, nói rõ rủi ro phải làm lại giọng các cảnh bị sửa, và chỉ làm khi họ đồng ý.
- `/kaku-release-review`: mục "Nguồn (canon)" là LỖI nếu còn dòng chưa kiểm.
- Kịch bản mới do `/yt-studio` hoặc công cụ dựng cảnh tạo ra phải ghi ô tình trạng theo đúng các mức ở trên, để sổ đọc được.
