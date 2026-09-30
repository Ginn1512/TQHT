---
name: kaku-originality-check
description: Chấm độ nguyên bản của một video kênh Cú Kaku theo 8 tiêu chí (0–2 điểm mỗi tiêu chí, tổng 16) bằng python -m tools.originality — máy chấm câu hỏi/luận điểm, nguồn, bình luận của kênh, quyền hình ảnh và độ trùng với các video khác; Claude chấm ví dụ mới, không paraphrase và giá trị cho người xem, có dẫn chứng. Chặn làm ảnh, giọng và đăng khi dưới 12/16 hoặc kịch bản chỉ đọc lại nguồn. Dùng sau khi viết xong kịch bản, trước khi làm ảnh và giọng, khi người dùng hỏi video có bị xem là "reused" hay "mass-produced" không, hoặc khi rà cả kênh tìm video lặp khuôn.
---

# kaku-originality-check: mỗi video một luận điểm riêng

Dựa trên tài liệu "Policy Safe" (`docs/chinh-sach-noi-dung.md`). Kết quả ghi vào `videos/<thư-mục>/originality.json` và được `release_check` đọc lại.

| Khóa | Tiêu chí | Ai chấm | Cách chấm |
|---|---|---|---|
| `cau-hoi` | Có câu hỏi hoặc luận điểm riêng | máy | 2 nếu `brief.md` có "Câu hỏi video trả lời" và "Luận điểm riêng" (hoặc "Góc nhìn"); 1 nếu chỉ có câu hỏi |
| `nguon` | Có nghiên cứu và nguồn được ghi lại | máy | 2 nếu `canon check` đạt; 1 nếu ít nhất một nửa số dòng có link; 0 nếu dưới một nửa |
| `binh-luan` | Có bình luận hoặc phân tích của kênh | máy | đếm cụm "Kaku ghi chú / nghĩ / đoán / để ý…", "theo mình", "lý thuyết" và chương góc nhìn; 2 khi có từ 5 cụm trở lên và có chương góc nhìn |
| `vi-du-moi` | Có ví dụ hoặc dữ liệu mới | **Claude** | xem mục 2 |
| `hinh-co-quyen` | Hình tự tạo hoặc có giấy phép | máy | điểm của `tools.rights` (xem `/kaku-rights-audit`) |
| `khong-paraphrase` | Không phải bản dịch hay paraphrase gần nguyên bản | **Claude** | xem mục 2 |
| `khac-nhau` | Nội dung cốt lõi khác các video khác | máy | tỉ lệ cụm 5 từ trùng với **một** video khác, đã bỏ câu cửa miệng: dưới 10% được 2 điểm, dưới 25% được 1 điểm |
| `gia-tri` | Người xem nhận được giá trị rõ ràng | **Claude** | xem mục 2 |

Kết luận:

- **đạt**: đủ 8 tiêu chí và tổng từ 12 điểm trở lên.
- **viết lại**: tổng dưới 12. Quay lại nghiên cứu hoặc viết lại kịch bản.
- **từ chối**: `khong-paraphrase` = 0, tức có đoạn chỉ đọc lại bài viết, transcript hay tin tức. Viết lại hẳn đoạn đó.
- **chưa chấm đủ**: Claude chưa chấm 3 tiêu chí của mình.

## 1. Chấm phần máy

```bash
python -m tools.originality check videos/<thư-mục>
```

Lệnh in từng tiêu chí kèm dẫn chứng, ghi `originality.json`, và trả mã 1 khi chưa đạt. Chạy lại bất cứ lúc nào: phần máy được chấm lại, điểm Claude đã chấm được giữ.

Cách nâng điểm máy, mà không làm giả:

| Tiêu chí thấp | Việc làm thật |
|---|---|
| `cau-hoi` = 1 | Thêm dòng `- **Luận điểm riêng:** …` vào `brief.md`. Đây phải là điều kịch bản thật sự lập luận, lấy từ chương góc nhìn của kịch bản, không phải khẩu hiệu. |
| `nguon` ≤ 1 | Làm `/kaku-canon-ledger`: mở trang nguồn, `canon resolve`. |
| `binh-luan` ≤ 1 | Thêm phân tích thật: một chương "Góc nhìn của Kaku", phép so sánh, lập luận có lý do. Không rải cụm "Kaku nghĩ" vào câu không có ý kiến. |
| `hinh-co-quyen` ≤ 1 | Làm `/kaku-rights-audit`. |
| `khac-nhau` ≤ 1 | Xem cặp video trùng trong dẫn chứng; viết lại các đoạn chung, đổi khung theo `channel/formats.md`. |

## 2. Claude chấm 3 tiêu chí

Đọc `script.vi.md` (hoặc lời thoại trong `scenes.json`) và `brief.md`. Chấm theo thang sau, **mỗi điểm phải có dẫn chứng** là id cảnh hoặc câu cụ thể:

| Tiêu chí | 2 điểm | 1 điểm | 0 điểm |
|---|---|---|---|
| `vi-du-moi` | Có ít nhất 2 ví dụ, phép tính, bảng hay thử nghiệm do kênh tự làm (bảng chỉ số, phép so sánh chéo, thử nghiệm "nếu… thì") | Có 1 | Chỉ kể lại nội dung truyện |
| `khong-paraphrase` | Cấu trúc và câu chữ là của kênh; nguồn chỉ dùng để kiểm dữ kiện | Có đoạn bám sát thứ tự hoặc cách diễn đạt của một bài wiki | Có đoạn dịch hoặc viết lại gần nguyên văn một bài viết, transcript hay tin tức |
| `gia-tri` | Người xem trả lời được câu hỏi của video và nhớ được một ý mới | Có thông tin nhưng câu trả lời mờ | Không trả lời câu hỏi đã hứa |

Với `khong-paraphrase`: mở lại 1–2 link nguồn chính trong brief bằng WebFetch (nếu mở được) và so với đoạn kịch bản tương ứng. Nếu không mở được thì ghi rõ trong dẫn chứng.

```bash
python -m tools.originality score videos/<thư-mục> vi-du-moi 2 --evidence "s41–s47: bảng chỉ số tự dựng; s63: phép tính tốc độ"
python -m tools.originality score videos/<thư-mục> khong-paraphrase 2 --evidence "đã so s10–s20 với wiki Nen: cấu trúc và câu khác hẳn"
python -m tools.originality score videos/<thư-mục> gia-tri 2 --evidence "s95: trả lời 'vì sao Gon mất Nen' bằng luật giao ước"
```

**Không bao giờ** cho điểm cao để qua cửa. Điểm thấp là tín hiệu phải sửa kịch bản. Người dùng xác nhận điểm của Claude khi ghi quyết định trong `audit.md` (`/kaku-release-review`).

## 3. Rà cả kênh

```bash
python -m tools.originality scan
```

Lệnh in các cặp video giống nhau nhất và các câu lặp ở nhiều video nhất (đã bỏ câu cửa miệng "Mở sổ ra nào!", "Mình là Kaku.", "Kaku gấp sổ đây, hẹn gặp lại!").

- Câu lặp ở từ 10 video trở lên, thường là lời kêu gọi đăng ký: viết lại cho khác nhau khi sửa các video đó.
- Chạy mỗi đợt kịch bản mới và trước lần xét nhịp đăng (25/10).

## Luật nối với các skill khác

- `/yt-studio` mục 5: **chỉ làm ảnh và giọng khi `originality check` ra "đạt"**.
- `/kaku-release-review`: mục "Độ nguyên bản" là LỖI khi chưa đạt. `audit.md` dùng điểm này để chấm rủi ro "reused" và "inauthentic".
- Commit `originality.json` cùng `brief.md`.
