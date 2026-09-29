# Danh mục dạng video

Mỗi video chọn **một** dạng. Mỗi dạng có khung riêng, gồm cách mở đầu, chương đặc thù và cách kết, để các video xem liền nhau không giống nhau. YouTube coi "cùng khung kịch bản, chỉ thay danh từ" là nội dung lặp lại (chính sách 13/7/2026, xem `channel/references/nghien-cuu-nganh-2026.md`).

## Luật

1. Không có 2 video liền nhau cùng dạng.
2. Trong mỗi 30 video liên tiếp, một dạng xuất hiện tối đa 2 lần.
3. Phần chung của mọi video:
   - câu đầu cảnh báo spoiler;
   - Kaku chào bằng câu "Mở sổ ra nào!";
   - một chương góc nhìn riêng (tên chương đổi theo dạng, không phải lúc nào cũng là "Góc nhìn của Kaku");
   - lời thoại dài ≥ 15,3 phút.
4. Câu kết và lời mời xem video kế tiếp phải khác nhau giữa các video. Chỉ giữ dấu hiệu của Kaku, không giữ nguyên câu.
5. Kiểm tra tự động: `python -m tools.plan_check` (đọc `channel/topics.md` và độ dài từng video).

## Các dạng

| Mã | Dạng | Mở đầu | Chương đặc thù | Cách kết | Thumbnail |
|---|---|---|---|---|---|
| A | Giải thích hệ thống | Một câu hỏi "hoạt động thế nào?" | Luật nền → các nhánh → luật nâng cao → hiểu lầm | Sơ đồ tổng kết một hình | Sơ đồ + Kaku chỉ tay |
| B | Luật chơi và cách phá | Một tình huống "nếu gặp cái này thì làm sao?" | Luật → 3–5 cách phá → cái giá của mỗi cách | Bảng "luật / cách phá" | Chữ "CÁCH PHÁ" + ổ khóa |
| C | Lịch sử / tiến hóa của một thứ | Hình ảnh "ngày xưa" đối lập "bây giờ" | Các thời kỳ theo thứ tự, mỗi thời kỳ có một "phát minh" | Đường thời gian thu gọn | Hai nửa cũ/mới |
| D | Cây phả hệ | Gốc cây hoặc tổ tiên chung | Gốc → nhánh → nhánh con → nhánh bị mất | Cây hoàn chỉnh một hình | Cây phát sáng |
| E | Hồ sơ bách khoa | "Hồ sơ số…" mở ra | Mục từ theo nhóm, mỗi mục cùng thứ tự: tên, loại, điểm mạnh, điểm yếu | Mục lục hồ sơ | Tấm thẻ hồ sơ |
| F | Bảng chỉ số kiểu game | Thẻ chỉ số của một "nhân vật game" | Giải thích từng chỉ số → xếp hạng → giới hạn của con số | Thẻ chỉ số của người xem (trò chơi) | Thanh chỉ số, số % |
| G | Bậc thang tiến hóa | Nấc thang đầu tiên | Từng nấc: điều kiện, sức mạnh, cái giá | Toàn bộ bậc thang | Bậc thang sáng dần |
| H | Chân dung một nhân vật qua sức mạnh | Một khoảnh khắc định nghĩa nhân vật | Sức mạnh phản ánh tính cách thế nào | Một câu tổng kết về con người | Bóng nhân vật + chữ |
| I | So sánh chéo có chấm điểm | Đặt 2–3 hệ lên cùng một bàn | Tiêu chí → chấm từng tiêu chí → tổng | Bảng điểm cuối cùng | Chia 3 ô |
| J | Xếp hạng có tiêu chí | Công bố tiêu chí trước | Từ hạng thấp lên hạng cao | Bảng xếp hạng + mời người xem xếp lại | Bảng xếp hạng |
| K | Gỡ hiểu lầm | Một câu "ai cũng tin" bị gạch chéo | Mỗi hiểu lầm: người ta tin gì → truyện nói gì → vì sao dễ hiểu nhầm | Hiểu lầm lớn nhất, để dành tới cuối | Dấu X đỏ |
| L | Thử nghiệm "nếu… thì" | "Giả sử bạn tỉnh dậy trong thế giới đó" | Người xem đi qua từng bước, mỗi bước là một lựa chọn | Người xem sống sót được bao lâu, hoặc mạnh tới đâu | Người xem (bóng) giữa thế giới |
| M | Phân tích trận đấu | Tỉ số trước trận: ai được đánh giá cao hơn | Từng hiệp: mục tiêu, lựa chọn, cái giá; sơ đồ chiến thuật | Bài học chiến thuật | Hai bóng đối đầu + mũi tên |
| N | Điều tra bí ẩn | Một câu hỏi truyện chưa trả lời | Manh mối (có thật) → giả thuyết (gắn nhãn lý thuyết) → phản biện | Câu hỏi mở cho người xem | Kính lúp + dấu hỏi |
| O | Dòng thời gian thế giới | Một năm cụ thể, một sự kiện | Theo thứ tự thời gian, có mốc năm hoặc thời đại | Dòng thời gian toàn bộ | Dải thời gian |
| P | Khoa học trong anime | "Trong đời thật, điều này có thể không?" | Chi tiết trong truyện → nguyên lý khoa học thật → chỗ truyện "phóng tay" | Điểm "độ thật" | Công thức + tranh |
| Q | Nhập môn cho người mới | "Nếu bạn chưa xem, đây là 15 phút bạn cần" | Thế giới → nhân vật chính → cách sức mạnh vận hành → vì sao nên xem; spoiler thấp | Lộ trình xem (từ đâu, bao nhiêu tập) | Cánh cửa mở |
| R | Cài cắm và chi tiết ẩn | "Câu trả lời đã có từ tập đầu tiên" | Mỗi chi tiết: lần đầu xuất hiện → ý nghĩa về sau | Chi tiết cài cắm hay nhất | Hai khung "trước/sau" |
| S | Nguồn gốc ngoài đời thật | "Câu chuyện này có thật hơn bạn nghĩ" | Chi tiết trong truyện → nguồn gốc thật (lịch sử, truyền thuyết) → chỗ tác giả thay đổi và vì sao | Bản đồ "thật / hư cấu" | Nửa tranh cổ, nửa tranh anime |
| T | Ôn tập trước mùa mới | "Mùa mới ra mắt sau N ngày, đây là 15 phút bạn cần nhớ" | Tình hình hiện tại → luật sức mạnh cần nhớ → các nút thắt còn mở | 3 điều nên để ý ở mùa mới | Lịch đếm ngược |
| U | Phiên tòa nhân vật | "Bị cáo: …" | Cáo trạng → lời bào chữa → nhân chứng (chi tiết có thật) → luận điểm cuối của hai bên | Người xem là bồi thẩm, bình chọn trong bình luận; Kaku không tuyên án | Cán cân + búa |

## Ghi chú theo dạng

- **M (phân tích trận đấu):** kể bằng sơ đồ chiến thuật và tranh tự vẽ; không dựng lại khung hình của anime.
- **N (bí ẩn) và R (cài cắm):** manh mối phải là chi tiết có thật trong truyện, ghi nguồn chương hoặc tập trong `brief.md`. Giả thuyết luôn nói rõ "đây là lý thuyết".
- **P (khoa học):** không đưa công thức hay cách làm có thể gây nguy hiểm, như chế thuốc súng, chất độc hay thuốc. Chỉ nói nguyên lý chung. Có câu "đây không phải hướng dẫn".
- **Q (nhập môn):** spoiler thấp nhất; chỉ nói tới khoảng tập 3–5 của mùa 1.
- **S (nguồn gốc ngoài đời thật):** mọi sự thật lịch sử, truyền thuyết hay văn hóa phải có nguồn trong `brief.md`. Nói rõ chỗ nào là hư cấu của tác giả. Không vẽ lại chân dung người thật theo ảnh; dùng bóng người và đồ vật thời đó.
- **T (ôn tập trước mùa mới):** spoiler tới hết mùa anime trước, không đụng tới phần manga mà mùa mới sẽ chiếu. Ghi ngày phát trong `brief.md` và kiểm lại ngay trước khi đăng.
- **U (phiên tòa nhân vật):** Kaku chỉ trình bày lập luận của cả hai bên, không tuyên án và không cổ vũ bạo lực. Nhân chứng là chi tiết có thật, ghi tập hoặc chương trong `brief.md`. Kết bằng lời mời người xem bình chọn.
