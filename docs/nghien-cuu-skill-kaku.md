# Nghiên cứu 7 skill `kaku-` (chưa viết)

> 2026-09-29. Đây là bản đánh giá, **chưa tạo skill nào**.
>
> Tên đã chốt: tiền tố `kaku-`. Script `scripts/sync-ecc-skills.sh` chỉ xóa những tên có trong `third_party/ecc/skills.txt`, và chỉ chép những tên có trong `keep.txt`. Vì vậy thư mục `kaku-*` an toàn.
>
> Khi viết skill, sửa `CLAUDE.md` (mục Skills) thành: "skill riêng của dự án bắt đầu bằng `yt-` hoặc `kaku-`".

## Kết luận nhanh

Cả 7 skill đều đúng chỗ hở thật: chưa có công cụ nào đọc `brief.md`, `metadata.*.md`, nguồn gốc asset hay số liệu sau đăng.

Nên đổi thứ tự so với đề xuất:

1. **`kaku-scene-pack` làm trước tiên.** Công cụ dựng cảnh (`mk2.py`, `ins.py`, `done.py`) đã tạo cả 78 kịch bản, nhưng chỉ nằm trong thư mục tạm của phiên cloud. Container bị thu hồi là mất.
2. **`kaku-canon-ledger` và `kaku-release-review` cần trước ngày 06/10**, là ngày đăng video 1:
   - 78 `brief.md` còn nhiều dòng "cần kiểm lại";
   - chưa có gì kiểm file render, phụ đề và metadata trước khi đăng.
3. **`kaku-rights-audit` gấp hơn dự kiến**, vì vừa thêm VoiceStudio: engine mặc định OmniVoice có trọng số phi thương mại.
4. **`kaku-script-doctor` và `kaku-project-audit`** làm sau.
5. **`kaku-retro`** chờ tới khi đã đăng khoảng 6 video, vì trước đó chưa có số liệu. Có thể gộp vào `yt-research`.

## Từng skill

### 1. `kaku-project-audit`: kiểm kê repo và skill

- **Đã có:**
  - `plan_check`, `prompt_check`, `prompt_pack --check`, `pytest tools/tests`;
  - `keep.txt` và `skills.txt` của ECC;
  - skill ECC có sẵn: `verification-loop`, `security-review`.
- **Còn hở:**
  - Chưa có báo cáo gộp.
  - Không phát hiện được lệnh tốn tiền không có bước `costs estimate` đi trước. Ví dụ `tools.tts`, `tools.images`, Seedance qua API, fal.ai.
  - Không phát hiện lệnh nguy hiểm trong skill: `rm -rf`, `git push --force`, `curl … | sh`. Hướng dẫn VoiceStudio có một lệnh `curl | sh`, đã ghi chú.
  - Không kiểm trùng tên giữa ECC và skill dự án.
  - Không kiểm skill thiếu frontmatter.
- **Đề xuất:** `tools/project_audit.py` in một bảng:
  - skill (nguồn ECC / `yt-` / `kaku-`), `name` có khớp tên thư mục không;
  - lệnh tốn tiền và lệnh nguy hiểm trong từng SKILL.md;
  - biến môi trường cần có;
  - kết quả các lệnh kiểm có sẵn.

  SKILL.md chỉ hướng dẫn đọc bảng và sửa.
- **Công sức:** nhỏ. **Rủi ro:** trùng với `verification-loop`, nên chỉ giữ phần riêng của dự án.

### 2. `kaku-canon-ledger`: sổ khẳng định về anime

- **Đã có:**
  - Bảng "Sự thật dùng trong kịch bản" trong cả 78 `brief.md`, mỗi video khoảng 4–7 dòng.
  - Trạng thái ghi bằng chữ: link nguồn / "cần kiểm lại" / "Ý kiến của kênh".
  - Bảng có 3 kiểu tiêu đề cột khác nhau: `Sự thật | Nguồn / tình trạng` (48 video), `Sự thật | Tình trạng` (29), `Sự thật | Nguồn | Tình trạng` (video 1).
- **Còn hở:**
  - Không công cụ nào đọc `brief.md`.
  - Không biết tổng cộng bao nhiêu khẳng định chưa kiểm.
  - Một bộ xuất hiện nhiều lần (One Piece 6 video, Naruto 5…) nên cùng một chi tiết bị kiểm nhiều lần, và có thể mâu thuẫn giữa các video.
- **Đề xuất:** `tools/canon.py`:
  - `build`: đọc cả 3 kiểu bảng, ghi `channel/canon-ledger.csv` với các cột: id, video, anime, khẳng định, nguồn, mức chắc chắn, người kiểm, ngày;
  - mức chắc chắn gồm: có nguồn đã mở / chỉ có kết quả tìm kiếm / cần kiểm lại / lý thuyết / ý kiến kênh;
  - `check <video>`: dừng bước làm giọng nếu video còn dòng "cần kiểm lại";
  - gộp các khẳng định giống nhau theo anime, để kiểm một lần dùng cho nhiều video.
- **Công sức:** vừa. **Giá trị:** cao nhất ngay lúc này.

### 3. `kaku-script-doctor`: rút gọn, sửa nhịp, báo câu đã đổi

- **Đã có:**
  - `plan_check` kiểm độ dài 15–20 phút.
  - `mk2.py` (chỉ ở thư mục tạm) in số cảnh, số lượt Kaku xuất hiện, số phút, và các cảnh dài hơn 230 ký tự.
- **Còn hở:**
  - Chưa có báo cáo nhịp: phân bố độ dài cảnh, câu quá dài, tỉ lệ cảnh có Kaku, chương quá dài hay quá ngắn.
  - Chưa phát hiện câu mở hoặc câu kết lặp giữa các video.
  - Chưa có nhật ký sửa.
- **Đề xuất:** `tools/script_doctor.py`:
  - `report <video>`: số liệu nhịp và các cảnh cần xem;
  - `diff <video> --against <commit>`: bảng cảnh đổi (id, câu cũ, câu mới, số giây thay đổi).

  SKILL.md đặt luật cứng:
  - không đổi sự thật (khẳng định trong sổ `canon`);
  - giữ tối thiểu 15 phút;
  - mọi câu sửa phải liệt kê lại cho người dùng.
- **Phụ thuộc:** cần công cụ in lại `script.vi.md` từ `scenes.json`, nằm trong skill 4.

### 4. `kaku-scene-pack`: kịch bản đã duyệt thành `scenes.json` và danh sách asset

- **Đã có:**
  - `scenes.parse` kiểm cấu trúc;
  - `prompt_pack`, `seedance`, `costs estimate`.
- **Còn hở (quan trọng):**
  - Công cụ dựng cảnh không nằm trong repo.
  - Chưa có danh sách asset theo trạng thái: ảnh nào có rồi, cảnh nào thiếu giọng, clip nào cần, thumbnail.
- **Đề xuất:**
  - Đưa `mk2.py` và `ins.py` vào `tools/scene_pack.py`: `build <spec>` ghi `scenes.json`, `script.vi.md`, `brief.md`, rồi tự chạy `seedance` và `prompt_pack`.
  - `assets <video>` in bảng asset cho từng cảnh (ảnh / giọng / clip), dựa trên thư mục `assets/`.
  - Thêm test như các công cụ khác.
- **Công sức:** vừa. **Làm trước tiên** vì có nguy cơ mất công cụ.

### 5. `kaku-rights-audit`: nguồn, giấy phép, trạng thái duyệt của hình, nhạc, clip, giọng

- **Đã có:**
  - Luật cấm trong `channel/profile.md` và `prompt-blocklist.txt`;
  - font OFL;
  - `assemble --music` có nhắc "nhạc không bản quyền".
- **Còn hở:**
  - Không ghi asset nào làm bằng công cụ nào, theo điều khoản nào, ai đã duyệt.
  - Có VoiceStudio thì giấy phép engine giọng quan trọng hơn: OmniVoice là CC-BY-NC 4.0, VoxCPM2 là Apache-2.0.
- **Đề xuất:**
  - `videos/<x>/rights.json`, được commit, chỉ chứa thông tin, không chứa file. Các mục:
    - ảnh: công cụ, ngày, đã duyệt chưa;
    - giọng: engine, giấy phép mô hình, nguồn giọng là thiết kế hay nhân bản có đồng ý;
    - nhạc: nguồn, giấy phép, link;
    - clip: công cụ, điều khoản;
    - font.
  - `tools/rights.py check`: báo lỗi khi gặp giấy phép phi thương mại, giấy phép chưa rõ, hoặc asset chưa duyệt.
  - Tự điền phần giọng từ `cost.json` (khóa `tts_local_seconds`, `tts_app_seconds`) và từ `giong-kaku.json`.
- **Cần kiểm thêm:** điều khoản dùng thương mại của ảnh Gemini app và clip Dreamina/CapCut.

### 6. `kaku-release-review`: kiểm trước khi đăng

- **Đã có:**
  - `assemble` ghi `report.json` (độ dài), `subs.vi.srt`, `chapters.txt`;
  - `shorts`; `thumbnail`.
  - Skill `yt-studio` có mô tả `metadata.<lang>.md`, nhưng chưa video nào có file này và chưa công cụ nào kiểm.
- **Còn hở:** không có cửa kiểm cuối.
- **Đề xuất:** `tools/release_check.py <video>` kiểm:
  - **Bản render:** dài 15–20 phút, 1920×1080, 30 fps, có tiếng, độ to khoảng −14 LUFS (đo bằng bộ lọc `ebur128` của ffmpeg).
  - **Phụ đề:** phủ hết video, mỗi dòng không quá dài.
  - **Chương:** mở đầu bằng 00:00, ít nhất 3 chương, mỗi chương từ 10 giây.
  - **Metadata:** tiêu đề tối đa 100 ký tự, mô tả có nguồn và cảnh báo spoiler, tag tối đa 500 ký tự.
  - **Thumbnail:** 1280×720, dưới 2 MB.
  - **Liên kết với skill khác:** `canon check` và `rights check` phải đạt.
  - **Checklist tay:** nhãn nội dung tổng hợp trong YouTube Studio (nếu cần), lịch đăng, ghim bình luận.
- **Công sức:** vừa. **Cần trước 06/10.**

### 7. `kaku-retro`: đọc số liệu sau đăng, đề xuất thử nghiệm

- **Đã có:**
  - Bảng Notion "Video dài" có cột Lượt xem 48h, CTR 48h, Giữ chân, Người đăng ký tăng.
  - Bảng "Chỉ số tuần" có % tới điều kiện YPP.
  - `nhat-ky-hoc-hoi.md` có khuôn "3 điều học được".
  - Skill `yt-research` đã ghi nhật ký.
- **Còn hở:**
  - Chưa có số liệu, vì chưa đăng video nào.
  - Chưa nối YouTube Analytics; hiện nhập số tay vào Notion.
- **Đề xuất:**
  - Mỗi tuần đọc Notion qua connector.
  - So sánh theo dạng, theo bộ, theo độ dài.
  - Đề xuất 1–3 thử nghiệm: thumbnail hay tiêu đề (tính năng "Test & compare" của YouTube), câu mở đầu, dạng video.
  - Ghi vào `nhat-ky-hoc-hoi.md` và Notion; theo dõi hạn chót YPP 31/01/2027.
  - **Nên là một mục trong `yt-research`** cho tới khi có đủ việc để tách riêng.
- **Làm sau khoảng 2 tuần kể từ 06/10.**

## Chỗ trùng và cách gộp

- `canon-ledger` và `rights-audit` cùng là "sổ có trạng thái", nên dùng chung một khuôn file và một kiểu lệnh `check`.
- `release-review` gọi `canon check` và `rights check` như hai cửa bắt buộc.
- `script-doctor` cần phần in `script.vi.md` của `scene-pack`, nên làm `scene-pack` trước.
- `retro` trùng một nửa với `yt-research`, nên gộp trước, tách sau.
- Đồng ý với ghi chú trong đề xuất: **chưa tách** skill giọng, phụ đề, Short, chi phí. Chúng đã có công cụ (`app_audio`, `voicestudio`, `shorts`, `costs`).
