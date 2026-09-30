# Lộ trình tự động hóa: Notion + n8n

> **Đã được thay bằng `docs/tu-dong-hoa-agent.md` (30/09/2026):** tự động hóa bằng agent Claude Code, bắt đầu ngay, bỏ VPS và n8n. File này giữ lại để tham khảo, nhất là mục "Cấu trúc Notion" ở cuối.
>
> Nguyên tắc cũ: **làm tay tới khi được bật kiếm tiền**, rồi tự động hóa trong 2–3 tuần. Trong lúc làm tay, mọi thứ được chuẩn bị sẵn để sau này chỉ việc "cắm" vào.
> Bảng điều khiển: trang Notion riêng tư "Cú Kaku anime": https://app.notion.com/p/3ea4a1a7ca3f81ca962ece826fd086f6. Cấu trúc ghi ở mục "Cấu trúc Notion" cuối file.

## Nguyên tắc

- **Máy làm phần lặp lại, người giữ 2 cửa duyệt:** duyệt kịch bản, và duyệt video trước khi đăng. Theo chính sách tháng 7/2026, YouTube đánh giá "giá trị gốc" và loại kênh có "nhịp đăng không thể do người làm". Vì vậy không bỏ 2 cửa này, cũng không tăng số video chỉ vì đã tự động.
- **Một nguồn sự thật cho mỗi loại dữ liệu:**
  - repo git: kịch bản, `scenes.json`, prompt, công cụ;
  - Notion: trạng thái, lịch, link, chỉ số.
- **Không khóa vào một nhà cung cấp.** Mỗi bước đọc cùng một bộ prompt (`app_images.export`, `app_audio.export`); đổi công cụ chỉ là đổi "adapter".
- **Key chỉ nằm trong biến môi trường** trên máy chủ, không bao giờ nằm trong repo hay trong workflow xuất ra.

## Giai đoạn 0: bây giờ, 0 USD (chuẩn bị sẵn)

| Việc | Trạng thái |
|---|---|
| Mọi bước sản xuất đều là lệnh CLI trong `tools/` (prompt, nhập ảnh/giọng, dựng, thumbnail, Short) | Xong |
| Bộ prompt không phụ thuộc công cụ: ảnh 6 lớp + negative, giọng cho Gemini/ElevenLabs (`prompts.vi.md`) | Xong |
| Notion: Video dài (78 video), Shorts, Chỉ số tuần; tên trạng thái đúng như workflow sẽ đọc (mục cuối file) | Xong |
| Giọng Kaku: mô tả Voice Design cố định trong `channel/giong-kaku.json`. Khi chọn xong, ghi thêm voice ID (AI Studio hoặc ElevenLabs) | Chờ bạn chọn giọng |
| Ảnh mẫu Kaku lưu trong `channel/brand/kaku-ref.png` (API ảnh dùng làm ảnh tham chiếu) | Chờ video 1 |
| Ghi thời gian làm tay và chi phí thật của mỗi video vào bảng Video dài trên Notion | Bắt đầu từ video 1 |

## Giai đoạn 1: tuần 1 sau khi được bật YPP (hạ tầng)

1. **Máy chủ:** một VPS nhỏ (2 vCPU, 4 GB RAM, khoảng 5–10 USD/tháng) chạy Docker Compose gồm 2 dịch vụ:
   - `n8n` (tự host). n8n Cloud không chạy được lệnh trên máy, và ta cần ffmpeg + Python.
   - `kaku-worker`: chính repo này (Python + ffmpeg), mở một API nội bộ nhỏ `POST /run/<bước>` gọi đúng các lệnh `tools/*`. n8n gọi nó bằng node HTTP Request, nên không cần sửa image của n8n.
2. **Biến môi trường** trên VPS (không commit):
   - `GEMINI_API_KEY`, `ELEVENLABS_API_KEY` (nếu dùng);
   - `TRANSCRIPT_API_KEY`;
   - OAuth của YouTube Data API và YouTube Analytics API (dự án Google Cloud riêng);
   - token Notion integration;
   - token bot Telegram.
3. **Lưu trữ:** thư mục `videos/*/assets` và `render` nằm trên ổ VPS. MP4 xong thì chép lên Google Drive để bạn xem trên điện thoại.
4. **Kiểm tra:** chạy `pytest tools/tests` trong `kaku-worker` và dựng `--demo` một lần.

## Giai đoạn 2: tuần 1–2, bốn workflow

### W1. Sản xuất (Notion → video chờ duyệt)

- **Kích hoạt:** Notion Trigger, khi một dòng "Video dài" chuyển sang **Kịch bản đã duyệt**. Notion hiện chưa có trạng thái này; nó nằm trong bộ trạng thái mới ở `docs/tu-dong-hoa-agent.md` mục 7.
- **Các bước:**
  1. `kaku-worker` chạy `prompt_pack`, rồi `costs estimate`. Nếu chi phí vượt ngân sách tháng thì dừng và báo Telegram.
  2. Ảnh: `images` (API) hoặc chờ ảnh làm tay, tùy cột **Nguồn ảnh**.
  3. Giọng: `tts` (Gemini), hoặc adapter ElevenLabs, hoặc chờ giọng làm tay, tùy cột **Nguồn giọng**.
  4. Dựng video bằng `assemble`, làm thumbnail bằng `thumbnail`, rồi làm 3 Short: `shorts suggest` → `shorts make`.
  5. Chép `video.vi.mp4`, thumbnail và các Short lên Drive.
  6. Cập nhật Notion: trạng thái **Chờ duyệt video**, link Drive, số phút, chi phí.
  7. Gửi Telegram: "Video N đã dựng xong, mời duyệt".
- **Người duyệt:** xem trên điện thoại, rồi đổi trạng thái sang **Duyệt đăng** (hoặc **Sửa**, kèm ghi chú).

### W2. Đăng (Notion → YouTube)

- **Kích hoạt:** trạng thái chuyển sang **Duyệt đăng**.
- **Các bước:**
  1. Node YouTube tải video lên, kèm tiêu đề và mô tả lấy từ `metadata.vi.md`, tag, và "không dành cho trẻ em".
  2. Hẹn giờ đăng theo cột **Ngày đăng**, lúc 19:00.
  3. Đặt thumbnail, tải phụ đề `subs.vi.srt`.
  4. Ghi link YouTube vào Notion, trạng thái **Đã lên lịch**.
  5. Hẹn giờ đăng 3 Short vào 3 ngày kế tiếp.
- **Hạn mức:** với hạn mức YouTube Data API mặc định, mỗi ngày tải lên được khoảng 6 video (kiểm tra lại trên trang Quotas khi làm). Nhịp của kênh là 3 video + 7 Short mỗi tuần, nên đủ.

### W3. Chỉ số (hằng ngày, lúc 8:00)

- YouTube Analytics API → cập nhật cho từng video: lượt xem 48 giờ, CTR, tỉ lệ giữ chân, số người đăng ký tăng.
- Mỗi Chủ nhật thêm một dòng vào **Chỉ số tuần**: tổng người đăng ký, giờ xem 365 ngày, lượt xem Shorts 90 ngày, % tiến độ YPP.
- Gửi cảnh báo Telegram khi CTR 48 giờ dưới 4% (thay thumbnail/tiêu đề) hoặc tỉ lệ giữ chân dưới 30%.

### W4. Nghiên cứu (hằng tuần, sáng thứ Hai)

- Tìm các anime đang hot và video mới của các kênh tham khảo (YouTube Data API, TranscriptAPI).
- Ghi vào cột **Ý tưởng** trong Notion, kèm lượt xem và ngày đăng.
- Claude dùng các ý tưởng này trong đợt `/yt-research` tiếp theo. Kịch bản vẫn viết bằng `/yt-studio` và có người duyệt.

## Giai đoạn 3: tháng 2 sau khi được bật YPP

- Lồng tiếng tự động tiếng Anh và Bồ Đào Nha: dịch `narration` → `tts --lang` → `audio.<lang>.m4a`.
- Phần tải bản âm thanh đa ngôn ngữ và tiêu đề dịch lên YouTube Studio vẫn làm tay, vì API chưa hỗ trợ đủ.
- Chỉ bật khi CTR và tỉ lệ giữ chân của bản tiếng Việt đã ổn định.

## Chuyển từ làm tay sang API mà không soạn lại

| Bước | Làm tay (bây giờ) | API (sau YPP) | Cần thêm |
|---|---|---|---|
| Ảnh | Gemini app, trang Xưởng | `tools.images` (Gemini API); model khác dùng cùng prompt + `NEGATIVE` | Adapter nếu đổi model; `YT_IMAGE_ENGINE` |
| Giọng | AI Studio / ElevenLabs, trang Xưởng | `tools.tts` (Gemini, có sẵn); `tools/tts_elevenlabs.py` (sẽ viết) | Voice ID của giọng Kaku; `YT_TTS_ENGINE`, `ELEVENLABS_API_KEY` |
| Dựng, Short, thumbnail | Claude chạy lệnh | `kaku-worker` chạy cùng lệnh | Không |
| Đăng | Bạn tải lên bằng app YouTube Studio | W2 | OAuth YouTube |
| Chỉ số | Bạn nhập tay mỗi Chủ nhật | W3 | OAuth YouTube Analytics |

Trước khi chọn công cụ giọng cho API: đọc cùng đoạn thử bằng giọng Kaku trên Gemini và ElevenLabs, nghe so sánh, rồi chọn bên rẻ hơn trong những bên đạt chất lượng.

## Chi phí sau khi tự động hóa (ước tính, 12 video/tháng)

| Khoản | Ảnh qua API | Giữ ảnh làm tay |
|---|---|---|
| Ảnh (khoảng 100 ảnh/video × 0,034 USD) | khoảng 41 USD | 0 |
| Giọng Gemini (khoảng 0,14 USD/video) | khoảng 2 USD | khoảng 2 USD |
| VPS | khoảng 5–10 USD | khoảng 5–10 USD |
| **Tổng** | **khoảng 50–55 USD** | **khoảng 7–12 USD** |

- Nếu dùng ElevenLabs thì cộng thêm tiền gói trả theo tháng (kiểm tra bảng giá lúc chọn).
- Chỉ chuyển ảnh sang API khi doanh thu tháng đạt khoảng 2 lần chi phí.

## Mốc hoàn thành

- [ ] Tuần 1: VPS, n8n, `kaku-worker`, đủ biến môi trường; `pytest` đạt trên máy chủ
- [ ] Tuần 2: W1 dựng tự động 1 video thật, người duyệt trên điện thoại
- [ ] Tuần 2: W2 lên lịch đăng thành công 1 video + 3 Short
- [ ] Tuần 3: W3 ghi chỉ số hằng ngày; W4 ghi ý tưởng hằng tuần
- [ ] Tuần 3: tắt các bước làm tay tương ứng trong `yt-studio`, cập nhật `CLAUDE.md`

## Cấu trúc Notion (đã tạo 29/09/2026)

Trang riêng tư **"Cú Kaku anime"**. Trên đầu ghi mục tiêu, mốc kiểm tra và luật đổi hướng (giống `docs/lo-trinh.md`). Bên dưới có 3 cơ sở dữ liệu và 1 trang con.

**1. Video dài** (78 dòng, lấy từ `channel/topics.md` và `docs/ke-hoach-noi-dung.md`)

| Cột | Kiểu | Ghi chú |
|---|---|---|
| Tên | Tiêu đề | Tiêu đề làm việc |
| Số | Số | 1–78 |
| Anime | Chọn nhiều | |
| Dạng | Chọn | A–U |
| Ngày đăng | Ngày | 06:00, 14:00, 22:00 giờ Việt Nam, từ 06/10/2026 |
| Trạng thái | Chọn | Kịch bản xong → Đang làm ảnh → Đang làm giọng → Chờ duyệt video → Duyệt đăng → Đã lên lịch → Đã đăng (thêm "Sửa"). Sẽ đổi sang bộ trạng thái mới ở `docs/tu-dong-hoa-agent.md` mục 7 |
| Nguồn ảnh / Nguồn giọng | Chọn | Làm tay / API |
| Thư mục | Văn bản | `videos/<ngày>-<slug>` |
| Kịch bản | Công thức | `link("Đọc kịch bản", "https://github.com/Ginn1512/TQHT/blob/HEAD/" + prop("Thư mục") + "/script.vi.md")`: luôn là bản mới nhất |
| Link Xưởng, Link Drive, Link YouTube | URL | |
| Số cảnh, Phút, Chi phí USD, Giờ làm tay | Số | |
| Lượt xem 48h, CTR 48h (%), Giữ chân (%), Người đăng ký tăng | Số | W3 tự điền sau này |

Chế độ xem: Kanban theo Trạng thái, Lịch theo Ngày đăng, Bảng đầy đủ.

**Nội dung trang của mỗi video** là bản chép `script.vi.md`, chỉ để đọc (thêm ngày 30/09/2026, đã chép video 1–9):

- Tạo bằng `python -m tools.notion_export videos/<thư-mục>`, dán bằng `notion-update-page` (`replace_content`).
- Đầu trang ghi commit của `script.vi.md` lúc chép và link GitHub. Commit khác `git log -1 -- videos/<thư-mục>/script.vi.md` thì chép lại.
- Chép theo đợt 9 video, sau khi đợt đó kiểm nguồn xong. Trước đó đọc qua cột "Kịch bản".
- Góp ý bằng bình luận trên trang. Không sửa thẳng, vì lần chép sau sẽ ghi đè. Bản gốc là `scenes.json`.

**2. Shorts:** Tên, Video gốc (liên kết tới Video dài), Cảnh (ví dụ `s19–s24`), Ngày đăng, Trạng thái, Lượt xem.

**3. Chỉ số tuần:** Tuần (ngày Chủ nhật), Người đăng ký, Giờ xem 365 ngày, Lượt xem Shorts 90 ngày, Ghi chú. Hai cột công thức:
- % YPP video dài = min(Người đăng ký / 1000, Giờ xem / 4000);
- % YPP Shorts = min(Người đăng ký / 1000, Lượt xem Shorts / 10.000.000).

**4. Trang con "Lộ trình tự động hóa n8n":** các mục tích ở "Mốc hoàn thành" phía trên.
