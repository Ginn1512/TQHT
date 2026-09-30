---
name: kaku-rights-audit
description: Lập và kiểm sổ quyền tài sản của một video kênh Cú Kaku (videos/<thư-mục>/rights.csv theo cột asset_id, filename, type, creator, source_url, license, permission_proof, attribution_required, expiry, notes) bằng python -m tools.rights, dựa trên sổ điều khoản chung channel/rights-registry.json — ảnh Gemini, giọng VoxCPM2/AI Studio/ElevenLabs, font, clip Seedance, nhạc nền. Chặn đăng khi còn dòng UNKNOWN hoặc công cụ chưa kiểm điều khoản. Dùng sau khi nhập ảnh và giọng, khi thêm nhạc hay clip, khi người dùng hỏi "ảnh AI có được kiếm tiền không", hoặc khi cần kiểm điều khoản một công cụ.
---

# kaku-rights-audit: mọi tài sản có nguồn và giấy phép

Theo tài liệu "Policy Safe": không có nguồn hoặc giấy phép rõ ràng thì không được đưa vào bản render cuối. Có giấy phép cũng **không** tự động đủ điều kiện kiếm tiền: nội dung vẫn cần bình luận và giá trị riêng (`/kaku-originality-check`).

Hai tầng:

- **`channel/rights-registry.json`**: sổ điều khoản chung. Mỗi công cụ một mục, kiểm một lần, dùng cho mọi video. Trạng thái:
  - `da-kiem`: đã mở trang điều khoản, có ngày kiểm;
  - `can-kiem`: chưa mở trang hoặc chưa xác nhận dùng thương mại;
  - `UNKNOWN`: không rõ nguồn hay giấy phép;
  - `cam`: không được dùng cho kênh kiếm tiền.
- **`videos/<thư-mục>/rights.csv`**: sổ của từng video. Dòng máy tạo có `permission_proof` = `registry:<khóa>`.

## 0. Xem hiện trạng

```bash
python -m tools.rights registry                      # trạng thái các mục trong sổ chung
python -m tools.rights check videos/<thư-mục>        # mã 1 nếu còn LỖI
```

## 1. Tạo hoặc cập nhật `rights.csv`

```bash
python -m tools.rights build videos/<thư-mục>        # hoặc --all cho mọi video
```

Máy tạo các dòng sau:

- mỗi cảnh một dòng ảnh;
- một dòng cho mỗi clip có trong `assets/clips/`;
- mỗi ngôn ngữ một dòng giọng;
- một dòng font;
- một dòng thumbnail.

Công cụ được đọc từ `cost.json`:

| Trong `cost.json` | Công cụ ghi vào sổ |
|---|---|
| `images` | `gemini-image-api` |
| `images_app` | `gemini-image-app` |
| `tts_local_seconds` | engine VoiceStudio (`voxcpm2`) |
| `tts_seconds` | `gemini-tts-api` |
| `tts_app_seconds` + `tts_app_engine` | `ai-studio-tts` hoặc `elevenlabs` |

- Chưa làm ảnh hay giọng thì máy ghi theo kế hoạch (ảnh API, VoxCPM2) và ghi chú "dự kiến". **Chạy lại `build` sau khi nhập ảnh và giọng.**
- Giọng làm tay phải nhập bằng `app_audio import --engine gemini|elevenlabs`. Thiếu thì dòng giọng là UNKNOWN.
- Chạy lại `build` sẽ giữ:
  - dòng người tự thêm;
  - dòng có `permission_proof` không bắt đầu bằng `registry:`;
  - ô `expiry` và `notes` người đã điền.

## 2. Thêm tay những gì máy không biết

Mở `rights.csv` và thêm một dòng cho mỗi tài sản sau:

- **Nhạc nền** (`assemble --music` không ghi lại): `asset_id` = `music`, `type` = `music`. Ghi tên tác giả, link đúng bài, loại giấy phép, và `attribution_required` = `yes` nếu bài bắt buộc ghi công. Ô `permission_proof` ghi nơi lấy, ví dụ "Thư viện âm thanh YouTube, bài X".
- **Ảnh không do AI tạo**, ví dụ sơ đồ tự vẽ tay: sửa dòng của cảnh đó. `creator` là người vẽ, `license` = "Tác phẩm của kênh", `permission_proof` ghi nơi lưu file gốc.
- **Tài sản của bên thứ ba**: theo luật kênh là **không dùng** (cảnh phim, ảnh chụp, trang manga, art chính thức). Nếu vẫn có thì phải có giấy phép bằng văn bản, ghi vào `permission_proof`, `expiry` nếu có.

## 3. Kiểm điều khoản một công cụ (đổi `can-kiem` → `da-kiem`)

1. Mở trang điều khoản bằng WebFetch. Đoạn trích trong kết quả tìm kiếm không được tính.
2. Tìm câu trả lời cho 4 câu hỏi:
   - Được dùng đầu ra cho mục đích thương mại (video kiếm tiền) không?
   - Ai sở hữu đầu ra?
   - Có bắt buộc ghi công hay gắn nhãn không?
   - Có giới hạn theo gói tài khoản không (miễn phí hay trả phí)?
3. Nếu đạt: sửa mục trong `channel/rights-registry.json`:
   - `status` = `da-kiem`;
   - `checked` = ngày hôm nay;
   - `notes` = câu trả lời ngắn cho 4 câu hỏi, kèm link;
   - `attribution_required` = `yes` hoặc `no`.
4. Nếu không đạt: `status` = `cam`, ghi lý do, và báo người dùng đổi công cụ.
5. Trang bị chặn trong phiên cloud: để nguyên `can-kiem`. Nhờ người dùng mở trang trên điện thoại hoặc PC rồi dán **nội dung điều khoản** (không phải key) vào chat, hoặc tự xác nhận.

**Không bao giờ** đánh `da-kiem` khi chưa đọc điều khoản. **Không bao giờ** bịa link.

## 4. Kết thúc

```bash
python -m tools.rights check videos/<thư-mục>        # phải báo "Mọi tài sản đã có nguồn…"
pytest tools/tests/test_rights.py
```

- Commit `rights.csv` (và `channel/rights-registry.json` nếu có sửa), rồi push.
- Báo lại:
  - các công cụ còn `can-kiem`;
  - các dòng còn UNKNOWN;
  - các dòng bắt buộc ghi công, và đã ghi trong mô tả chưa.

## Luật nối với các skill khác

- `/kaku-originality-check`: tiêu chí `hinh-co-quyen` lấy điểm từ đây. 2 điểm khi mọi mục đã kiểm, 1 khi còn `can-kiem`, 0 khi có UNKNOWN hoặc mục bị cấm.
- `/kaku-release-review`: mục "Quyền tài sản" là LỖI khi còn dòng UNKNOWN hoặc mục chưa `da-kiem`.
- `/yt-seedance`: clip đặt vào `assets/clips/` thì chạy lại `build`.
