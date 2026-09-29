# Giọng Kaku bằng VoiceStudio (chạy trên PC của bạn)

[VoiceStudio](https://github.com/debpalash/VoiceStudio) là app tạo giọng nói chạy hoàn toàn trên máy tính của bạn. Nó có thiết kế giọng và nhân bản giọng, và mở API ở `http://localhost:3900`.

Nó thay được cho AI Studio và ElevenLabs:

- không tốn tiền, không giới hạn lượt;
- tạo giọng từng cảnh tự động, không phải dán từng đoạn đọc.

Công cụ trong repo: `python -m tools.voicestudio`. Cấu hình nằm trong mục `voicestudio` của `channel/giong-kaku.json`.

> **Lệnh phải chạy trên chính PC đang mở VoiceStudio.** Phiên Claude trên cloud không với tới `localhost` của bạn. Chạy ở đó, lệnh chỉ báo "Không kết nối được".

## Giấy phép: đọc trước khi dùng

| Thành phần | Giấy phép | Dùng cho video kiếm tiền? |
|---|---|---|
| App VoiceStudio | AGPL-3.0 | Dùng app bình thường được. Repo này chỉ gọi API, không chép mã của app. |
| Engine mặc định **OmniVoice** | Trọng số theo **CC-BY-NC 4.0**, tức phi thương mại | **Không.** `tools.voicestudio` từ chối engine này. |
| Engine **VoxCPM2** (OpenBMB) | Apache-2.0 | **Có.** Engine có tiếng Việt, tiếng 48 kHz, thiết kế giọng bằng mô tả. Đây là mặc định của công cụ. |
| Engine khác (CosyVoice, IndexTTS…) | Chưa kiểm | Công cụ chặn. Chỉ dùng sau khi tự đọc giấy phép mô hình, ghi vào file này, rồi chạy với `--license-ok`. |

Lưu ý thêm:

- Kho VoxCPM có một [issue hỏi về giấy phép của dữ liệu huấn luyện](https://github.com/OpenBMB/VoxCPM/issues/238). Nên xem lại trước khi bật kiếm tiền.
- Không nhân bản giọng người thật khi chưa được người đó cho phép. Giọng Kaku là giọng tổng hợp, tạo từ mô tả.

## Bước 1. Cài VoiceStudio trên PC (một lần)

- **Windows:** tải bản cài từ trang [Releases](https://github.com/debpalash/VoiceStudio/releases).
- **Linux:** chạy lệnh cài của tác giả:
  ```bash
  curl -fsSL https://voicestudio.sh/install | sh
  ```
  Lệnh này chạy một script tải từ internet. Nếu muốn, mở link đó ra đọc trước.

Yêu cầu máy:

- Card NVIDIA với driver mới.
- Nên có CUDA 12 trở lên.
- VoxCPM2 cần khoảng 8 GB VRAM. Card ít VRAM hơn vẫn chạy được nhưng chậm.

## Bước 2. Cài engine VoxCPM2

1. Mở app. Trong phần engine/mô hình, cài **VoxCPM2** (tải vài GB, làm một lần).
2. Kiểm tra từ repo (trên PC):
   ```bash
   git clone https://github.com/ginn1512/tqht.git && cd tqht
   pip install -r tools/requirements.txt
   python -m tools.voicestudio check
   ```
   Kết quả phải có dòng `voxcpm2: dùng được cho kênh kiếm tiền`.

## Bước 3. Tạo giọng Kaku (một lần)

1. Đọc thử câu mẫu bằng 3 mô tả giọng (nam giọng Bắc, nam giọng Nam, nữ giọng Bắc):
   ```bash
   python -m tools.voicestudio design
   ```
   Ba file nằm trong `.cache/voicestudio-test/`.
2. Nếu ba file nghe giống nhau hoặc sai giọng, làm bước thiết kế ngay trong app:
   - chọn engine VoxCPM2;
   - dán mô tả giọng từ `channel/giong-kaku.json`;
   - đọc câu mẫu.

   Lý do: lệnh `design` gửi mô tả qua trường `description` của API, và mình chưa thử trên máy thật.
3. Chọn giọng ưng nhất, rồi lưu thành **hồ sơ giọng** (voice profile) trong app:
   - dùng file đã chọn làm giọng mẫu;
   - nhập đúng câu mẫu làm lời của đoạn mẫu;
   - đặt tên "Kaku".

   Tên nút có thể khác tùy phiên bản app.
4. Chạy `python -m tools.voicestudio check` để lấy id hồ sơ.
5. Ghi id vào `channel/giong-kaku.json`:
   ```json
   "voicestudio": { "engine": "voxcpm2", "voice_id": "<id hồ sơ>", ... }
   ```
   Ghi luôn giọng đã chọn vào `chosen`. Commit, hoặc nhắn Claude ghi giúp.
6. Nghe lại: `python -m tools.voicestudio test`.

## Bước 4. Tạo giọng cho một video

```bash
python -m tools.voicestudio run videos/2026-10-06-nen-hunter-x-hunter
```

- Mỗi cảnh thành một file `assets/audio/vi/<scene-id>.wav` (mono, 24 kHz), đúng chỗ `tools.assemble` đọc.
- Cảnh đã có file thì bỏ qua.
- Muốn làm lại vài cảnh: `--only s03,s07 --force`.
- Lần gọi đầu chậm hơn vì app phải nạp mô hình.
- Kết quả được lưu cache: chạy lại cùng lời thoại thì không phải tạo lại.
- Thời lượng giọng ghi vào `cost.json` ở khóa `tts_local_seconds` (0 USD).

## Bước 5. Ghép với ảnh và dựng video

Ảnh (từ Gemini app) và giọng (từ PC) phải nằm chung một chỗ. Thư mục `assets/` không lên git. Chọn một trong hai cách:

- **A. Dựng luôn trên PC** (gọn nhất):
  1. Tải ảnh Gemini về PC.
  2. `python -m tools.app_images import videos/<thư-mục> --from <thư-mục-ảnh>`
  3. `python -m tools.assemble videos/<thư-mục>`
- **B. Gửi giọng cho Claude trên cloud:**
  1. `python -m tools.voicestudio pack videos/<thư-mục>` tạo `render/giong-vi.zip`.
  2. Tải file zip lên Google Drive và gửi link cho Claude.
  3. Claude tải về rồi chạy `python -m tools.voicestudio unpack videos/<thư-mục> --from giong-vi.zip`.

## Tùy chọn: Claude Code trên PC điều khiển VoiceStudio

Nếu bạn chạy Claude Code ngay trên PC:

- Kết nối MCP của VoiceStudio bằng cách thêm vào `.mcp.json` ở máy bạn:
  ```json
  {"mcpServers": {"voicestudio": {"type": "http", "url": "http://localhost:3900/mcp/"}}}
  ```
  Giữ dấu `/` ở cuối URL.
- Skill của tác giả: `npx skills add debpalash/VoiceStudio` (skill `voicestudio`).
- Hai thứ này chỉ cài trên máy bạn, không đưa vào repo:
  - file `.mcp.json` sẽ làm phiên cloud báo lỗi kết nối;
  - skill dùng giấy phép AGPL-3.0.

## Lỗi thường gặp

| Thông báo | Cách xử lý |
|---|---|
| `Không kết nối được VoiceStudio` | Mở app. Nếu đổi cổng, đặt biến môi trường `VOICESTUDIO_URL`. |
| `Engine 'omnivoice' … phi thương mại` | Dùng `voxcpm2` (mặc định). |
| `Chưa có hồ sơ giọng Kaku` | Làm bước 3, ghi `voice_id`. |
| `VoiceStudio trả lỗi 400 …` | Đọc lời nhắn. Thường gặp: engine chưa cài, hoặc id hồ sơ sai (`check` để xem lại). |
| Giọng đọc sai tên riêng | Sửa lời thoại cảnh đó trong `scenes.json` theo kiểu phiên âm, rồi `run --only sNN --force`. |

## Nguồn

- [VoiceStudio: README, giấy phép AGPL-3.0](https://github.com/debpalash/VoiceStudio)
- [Skill voicestudio: API `/v1/audio/speech`, `/v1/audio/voices`](https://github.com/debpalash/VoiceStudio/blob/main/skills/voicestudio/SKILL.md)
- [Trường của request (`model`, `voice`, `language`, `seed`…)](https://github.com/debpalash/VoiceStudio/blob/main/backend/api/routers/openai_compat.py)
- [MCP](https://github.com/debpalash/VoiceStudio/blob/main/docs/mcp.md)
- [Hiệu năng](https://github.com/debpalash/VoiceStudio/blob/main/docs/performance.md)
- [Engine VoxCPM2 (danh sách ngôn ngữ có tiếng Việt)](https://github.com/debpalash/VoiceStudio/blob/main/docs/engines/voxcpm2.md)
- [OmniVoice](https://github.com/k2-fsa/OmniVoice)
- [Trọng số OmniVoice theo CC-BY-NC 4.0 (Hugging Face)](https://huggingface.co/k2-fsa/OmniVoice)
- [VoxCPM2: Apache-2.0](https://github.com/OpenBMB/VoxCPM)
- [VoxCPM2 chạy với khoảng 8 GB VRAM](https://x.com/rohanpaul_ai/status/2043538724047425536)
