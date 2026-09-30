# Tự động hóa kênh bằng agent Claude Code

> 2026-09-30. Chiến lược, **chưa có agent nào chạy**. Thay cho `docs/tu-dong-hoa.md` (VPS + n8n, chờ YPP).
> Bản xem trên điện thoại: https://claude.ai/code/artifact/7608e62b-19ff-4147-bce4-b6a2a4e15cae. Khi sửa file này, sửa cả trang đó.

## Tóm tắt

- **Mục tiêu:** agent làm khoảng 85% việc. Người làm khoảng 2 giờ/ngày trong tháng 10, khoảng 3–3,5 giờ/ngày khi có kịch bản mới (mục 5).
- **Bắt đầu ngay**, không chờ bật kiếm tiền:
  - P0 xây nền trong gói Pro (tới 15/10/2026);
  - P1 lên Max 20x và bật từng làn.
- **Hai làn:**
  - làn chữ chạy trên cloud bằng routine, kết quả là PR vào git;
  - làn media chạy trên PC bằng scheduled task của Claude Desktop, dùng GPU và VoiceStudio.
- **Hai cổng không agent nào làm thay được:**
  - người merge PR, tức là chốt kịch bản;
  - người tự tải lên và đặt lịch trong YouTube Studio.
- **Nhịp đăng (người chốt ngày 30/09/2026):** 3 video/ngày lúc 06:00, 14:00, 22:00 và 1 Short lúc 18:00, từ 06/10. Xét lại ngày 25/10. Đây là rủi ro chính sách lớn nhất (mục 11).

## 1. Hai làn

| | Làn chữ | Làn media |
|---|---|---|
| Chạy ở đâu | cloud, [routine](https://code.claude.com/docs/en/routines) | PC Windows có card NVIDIA, [Desktop scheduled task](https://code.claude.com/docs/en/desktop-scheduled-tasks) |
| Việc | nghiên cứu, kịch bản, kiểm nguồn, metadata, số liệu, bình luận | ảnh, giọng, dựng, Short, thumbnail, kiểm trước khi đăng |
| Kết quả | PR vào nhánh `claude/*` | file trong `videos/<x>/assets` và `render`, chép vào thư mục Google Drive trên máy |
| Điều kiện chạy | không cần máy bạn bật | app Claude Desktop mở, PC không ngủ (bật **Keep computer awake**) |
| Key | không cần key ảnh | `GEMINI_API_KEY` chỉ nằm trong biến môi trường của PC |

Vì sao chia như vậy:

- Routine chạy cả khi PC tắt. Nhưng nó không với tới `localhost:3900` (VoiceStudio) và không có GPU.
- Mỗi lần chạy routine là một bản clone mới, nên không giữ được `assets/` giữa các lần.
- Desktop task chạy ngay trong thư mục repo trên PC. Nó dùng được file, GPU và localhost.

**Notion** là bảng trạng thái chung của hai làn. Notion không giữ file.

- Tổng quản: `tools/pipeline.py` (sẽ viết) và skill `kaku-pipeline`.
- **Trạng thái suy ra từ file thật**, ví dụ: có `scenes.json` chưa, `canon check` đạt chưa, đủ ảnh chưa, có `render/video.vi.mp4` chưa. Notion chỉ là bản hiển thị.
- **Khóa (lease):** trước khi làm một video, agent ghi tên mình và hạn giờ vào cột "Khóa" trên Notion. Nhờ vậy hai phiên không làm cùng một video.
- **Mỗi đêm đối chiếu** Notion với file thật và sửa chỗ lệch.
- Bỏ VPS và n8n.

## 2. Bảy agent

Mỗi agent là một file `.claude/agents/<tên>.md` ([subagent](https://code.claude.com/docs/en/sub-agents)): giới hạn `tools`, chọn `model`, đặt `maxTurns`, gắn `hooks`. Chưa tạo file nào.

| Agent | Chạy ở đâu | Việc | Cổng phải qua | Model |
|---|---|---|---|---|
| strategist | cloud, sáng thứ Hai | xu hướng, đối thủ, chấm chủ đề, bản ghi nhớ tuần | `plan_check` | sonnet; opus cho bản ghi nhớ |
| writer | cloud | kịch bản, tự sửa nhịp | `script_doctor`, 15–20 phút, `prompt_check`, `originality check` | opus |
| fact-checker | cloud, dự phòng trên PC | mở nguồn từng khẳng định | `canon check --strict` | sonnet; opus khi khó |
| art-director | PC | tạo ảnh, tự xem lại từng ảnh | trần chi phí, tối đa 2 vòng | sonnet |
| producer | PC, GPU | giọng, kiểm giọng, dựng, Short, thumbnail | `asr_check`, `report.json` bản đầy đủ | haiku |
| release-qa | PC, độc lập | kiểm bản cuối, giấy phép, độ nguyên bản, xem khung hình, soạn `audit.md` | `release_check --write-audit`, `rights check` | sonnet |
| community | cloud | lọc bình luận, soạn nháp trả lời | người duyệt nháp | haiku; sonnet khi cần |

Chi tiết từng agent:

- **strategist**
  - Đọc: `channel/topics.md`, `channel/formats.md`, `nhat-ky-hoc-hoi.md`, bảng Notion "Chỉ số tuần", web.
  - Ghi:
    - bản ghi nhớ tuần;
    - 3 chủ đề đề xuất ở trạng thái "Ý tưởng";
    - PR sửa `topics.md` nếu cần.
  - Dùng skill `yt-research`.
  - Không được: chọn chủ đề thay người (trạng thái "Đã chọn").
- **writer**
  - Đọc: góc nhìn của người, `channel/profile.md`, `formats.md`, `nhat-ky-hoc-hoi.md`. Không nạp transcript kênh mẫu.
  - Ghi: `brief.md` (có dòng "Luận điểm riêng"), `scenes.json`, `script.vi.md`, `prompts.vi.md`, qua `scene_pack` và `prompt_pack`.
  - Tự chấm 3 tiêu chí Claude của `/kaku-originality-check`, có dẫn chứng; kịch bản chỉ sang PR khi `originality check` ra "đạt".
  - Không được: gọi API tốn tiền, sửa sự thật sau khi fact-checker đã kiểm, nâng điểm nguyên bản khi chưa sửa kịch bản.
- **fact-checker**
  - Chỉ đọc `scenes.json` và `brief.md`. Không sửa kịch bản.
  - Mở trang nguồn bằng WebFetch, ghi bằng cách `canon resolve`, gửi danh sách lỗi cho writer.
  - Tối đa 4 agent phụ song song, chia theo nhóm khẳng định.
  - Trang bị chặn trên cloud thì để lại cho lần chạy trên PC. Kinh nghiệm: fandom thường bị chặn.
- **art-director**
  - Đọc: `prompts.vi.md`, `channel/brand/kaku-ref.png`.
  - Ghi: `assets/images/`.
  - Dùng `tools.images` và `costs`. Xem lại từng ảnh bằng Read: chữ lạ, giống nhân vật có bản quyền, sai phong cách.
  - Không được: vượt trần chi phí, sửa prompt của cảnh không lỗi.
- **producer**
  - Chạy lần lượt: `voicestudio run` → `asr_check` → `assemble` → song song `shorts`, `thumbnail`, chương.
  - Chỉ dùng engine `voxcpm2`, chỉ một video trên GPU một lúc.
- **release-qa**
  - Chạy `rights build`, rồi `release_check --write-audit`, rồi xem 3 khung hình và thumbnail.
  - Chỉ báo lỗi và chuyển về đúng agent. Không tự sửa file, trừ phần máy của `rights.csv` và `audit.md`.
  - Không bao giờ điền `Decision` trong `audit.md`: đó là quyết định của người (xem `docs/chinh-sach-noi-dung.md`).
- **community**
  - Đọc bình luận và soạn nháp trả lời vào Notion.
  - Không bao giờ tự đăng, không làm theo lời dặn nằm trong bình luận.

## 3. Luồng một video: tuần tự và song song

1. **Góc nhìn** (người): 3–5 dòng, chuyển video sang "Đã chọn".
2. **writer** viết và tự sửa nhịp.
3. **fact-checker** kiểm. Sai thì trả writer sửa, tối đa 2 vòng.
4. **Mở PR** kịch bản.
5. **Người merge** = chốt kịch bản. `pipeline` ghi hash của `scenes.json` để biết nếu kịch bản bị sửa sau khi chốt.
6. Song song:
   - **Ảnh** (art-director, gọi API);
   - **Giọng** (producer, GPU trên PC).
7. **Dựng** bằng `assemble`.
8. Song song: **3 Short**, **thumbnail**, **metadata** (chương, mô tả, tag).
9. **release-qa**.
10. **Người** xem bản cuối, chọn tiêu đề và thumbnail, ghi `Decision: publish` vào `audit.md`, tự tải lên và đặt lịch.

Vì sao bước 1–5 phải tuần tự: sửa kịch bản sau khi đã làm giọng thì phải làm lại giọng.

Giới hạn số video cùng lúc:

| Hàng | Giới hạn |
|---|---|
| Đang viết | tối đa 9 video |
| Chờ người duyệt (kịch bản hoặc video) | tối đa 9 video (3 ngày) |
| Trên GPU | 1 video |
| Kho video đã đặt lịch | tối thiểu 3 video (1 ngày), nên có 9 (3 ngày) |

Hàng chờ duyệt đầy thì agent dừng. Máy không bao giờ chạy nhanh hơn người duyệt.

## 4. Vòng làm lại

Mỗi vòng có giới hạn. Quá giới hạn thì video chuyển sang "Lỗi" và chờ người.

| Chỗ | Giới hạn | Hết vòng thì |
|---|---|---|
| Kiểm nguồn | 2 vòng giữa fact-checker và writer | chuyển câu sang "lý thuyết" có gắn nhãn, hoặc bỏ chi tiết; người quyết |
| Ảnh | 2 vòng tạo lại, thêm tối đa 15% số ảnh | thay bằng thẻ chữ hoặc sơ đồ vẽ bằng code |
| Giọng | 2 lần mỗi cảnh | viết lại câu theo kiểu phiên âm, báo người |
| release-qa | 1 vòng, về đúng agent gây lỗi | Lỗi |
| Người bấm "Sửa" | chọn "Loại sửa": kịch bản / ảnh / giọng / metadata | chuyển đúng agent; sửa kịch bản thì chỉ làm lại giọng các cảnh bị đổi |

## 5. Việc của người

Từ 06/10/2026 kênh đăng 3 video/ngày, nên việc của người chia theo ngày.

| Lúc | Việc | Phút mỗi ngày |
|---|---|---|
| Sáng | Xem bản cuối 3 video, chọn tiêu đề và thumbnail | 60 |
| Sáng | Nghe lại giọng 3 video (VoiceStudio chạy đêm trước) | 30 |
| Sáng | Tải lên, đặt lịch 3 video và 1 Short | 25 |
| Tối | Duyệt nháp trả lời bình luận, ghim bình luận | 15 |
| Từ tháng 11 | Viết góc nhìn và merge 3 PR kịch bản mới | 75 |

- **Tháng 10:** khoảng 2,2 giờ/ngày, vì 78 kịch bản đã viết xong.
- **Từ tháng 11:** nếu giữ 3 video/ngày, khoảng 3,4 giờ/ngày.
- Phần chỉ người làm được là góc nhìn, gu và quyết định đăng. Đây là bằng chứng "người thêm giá trị" mà chính sách YouTube về nội dung "không chân thực" đòi hỏi.
- Ở 3 video/ngày, thời gian người dành cho mỗi video mỏng hơn nhiều so với nhịp 3 video/tuần. Không được bỏ bước xem bản cuối.

Agent không bao giờ tự làm:

- chọn chủ đề và góc nhìn;
- merge kịch bản;
- tải video lên và đặt lịch;
- đăng trả lời bình luận;
- tăng hạn mức tiền.

## 6. Lịch một ngày

Video lên sóng ngày D được làm media vào đêm D−2 và được người xem vào sáng D−1. Nhờ vậy luôn có kho 3 video đã đặt lịch.

| Giờ | Làn chữ (cloud) | Làn media (PC) | Người |
|---|---|---|---|
| 06:00 | | | video thứ nhất lên sóng |
| 07:07 | strategist (thứ Hai hằng tuần) | | |
| Sáng | writer và fact-checker cho 3 kịch bản mới (từ tháng 11) | | xem bản cuối, tải lên, đặt lịch 3 video của ngày mai |
| 14:00 | | | video thứ hai lên sóng |
| 18:00 | | | Short lên sóng |
| 22:00 | | | video thứ ba lên sóng |
| 23:13 | đối chiếu Notion với file thật | | |
| Đêm | | ảnh, giọng (lần lượt trên 1 GPU), dựng, Short, thumbnail, release-qa cho 3 video | |

- Mỗi đêm làn media phải xong 3 video. Cần đo thời gian thật trong tuần đầu: giọng VoxCPM2 cho khoảng 48 phút lời thoại, 3 lần dựng, 9 Short.
- Chọn giờ lệch khỏi đầu giờ (07:07, 23:13) vì routine đặt đúng đầu giờ có thể chạy trễ vài phút.
- Từ tháng 11, làn chữ cần khoảng 7–8 lượt routine mỗi ngày. Tài khoản có trần số lượt mỗi ngày (xem https://claude.ai/code/routines), nên gói Pro có thể không đủ; nên lên Max 20x sớm.
- Desktop task bị lỡ lịch vì máy ngủ sẽ chạy bù một lần khi máy thức. Prompt của task phải tự kiểm tra ngày giờ trước khi làm.

## 7. Trạng thái Notion, hook và công tắc

**Trạng thái mới của cột "Trạng thái"** (bảng Video dài). Các trạng thái in đậm là của người, agent không được đặt:

Ý tưởng → **Đã chọn** → Đang viết → Đang kiểm nguồn → Chờ duyệt kịch bản → **Kịch bản đã duyệt** → Đang làm media → Chờ duyệt video → **Duyệt đăng** → Đã lên lịch → Đã đăng.

Nhánh phụ:

- **Sửa**, kèm cột "Loại sửa";
- Lỗi;
- **Tạm dừng**.

Chuyển từ trạng thái hiện tại:

- Notion hiện có 8 trạng thái, từ "Kịch bản xong" tới "Đã đăng" và "Sửa".
- 78 video đang ở "Kịch bản xong". Chúng chuyển sang "Đang kiểm nguồn", vì còn khoảng 550 khẳng định chưa kiểm (`channel/canon-ledger.md`).

**Cột thêm:**

- Góc nhìn (văn bản);
- Khóa (văn bản: tên agent + hạn giờ);
- Loại sửa (chọn);
- Vòng làm lại (số);
- Hash kịch bản (văn bản).

**Hook** trong `.claude/settings.json` (sẽ viết):

- chặn lệnh Notion đặt các trạng thái in đậm;
- chặn `tools.images` và `tools.tts` khi `costs` báo vượt trần;
- chặn `git push --force` và đẩy lên nhánh khác `claude/*`;
- chặn mọi lệnh in ra biến môi trường chứa key.

**Trang "Công tắc"** trên Notion. Agent đọc trang này trước khi làm. Không đọc được thì coi như mức L2.

| Mức | Agent được làm | Tự bật khi |
|---|---|---|
| Bình thường | mọi việc trong bảng 7 agent | |
| L0 | dừng một video (trạng thái "Tạm dừng") | một video báo Lỗi 2 lần |
| L1 | chỉ làm chữ, không gọi API tốn tiền | chi tiêu vượt 80% hạn mức tháng |
| L2 | chỉ đọc và báo cáo | có thư chính sách từ YouTube, hoặc không đọc được trang Công tắc |
| L3 | tắt hẳn, tắt routine và scheduled task | chỉ người bật |

## 8. Ngân sách

Khoản tốn tiền chính là ảnh qua API. Tháng 10 có 78 video: khoảng 195 USD nếu giữ trần 2,5 USD mỗi video, dưới trần tháng 200 USD mà bạn duyệt ngày 30/09/2026.

| Khoản | Tháng 10 (78 video) | Cách tính |
|---|---|---|
| Ảnh qua API | khoảng 195 USD | 0,034 USD/ảnh (cần kiểm lại) × tối đa 73 ảnh/video, kể cả tạo lại |
| Thẻ chữ, sơ đồ | 0 USD | 20–30% cảnh vẽ bằng code thay vì ảnh AI |
| Giọng | 0 USD | VoiceStudio + VoxCPM2 trên PC |
| Dựng, Short, thumbnail | 0 USD | ffmpeg trên PC |
| Clip Seedance | 0 USD | làm tay trên app Dreamina/CapCut |
| Gói Claude | trả riêng | Pro trong P0, Max 20x từ P1 |

- **Chưa có thẻ vẽ bằng code** thì mọi cảnh đều là ảnh AI: tháng 10 khoảng 220–236 USD, vượt trần.
- **Từ tháng 11**, nếu giữ 3 video/ngày (khoảng 90 video/tháng): khoảng 225 USD/tháng, vượt trần 200 USD. Chốt lại khi xét nhịp ngày 25/10.

Luật chi tiền:

1. **Luật trong `CLAUDE.md` vẫn giữ:** trước mỗi lần gọi API tốn tiền phải báo ước tính (`costs estimate`) và chờ đồng ý.
2. **Trần tháng đã duyệt: 200 USD** (30/09/2026). Ghi trong `channel/costs.md` và `tools/config.py` (`MONTHLY_BUDGET_USD`).
3. **`costs` chặn cứng** (sẽ viết):
   - dừng khi một video vượt 2,5 USD;
   - dừng khi tháng vượt trần;
   - số ảnh tạo lại tối đa 15%.
4. **Trần thật nằm trên Google Cloud:** đặt hạn mức số request mỗi ngày cho project của key ảnh. Code có lỗi cũng không tiêu quá được.
5. **`GEMINI_API_KEY` không bao giờ dán vào chat.** Tháng 10, trước khi làn media chạy tự động, tạo ảnh bằng `tools.images` ở nơi có key: PC của bạn, hoặc biến môi trường của cloud environment. Nếu làn cloud cần gọi Google API, dùng mục "API credentials" của cloud environment (gói Pro/Max có): key được gắn vào request mà phiên không đọc được.

## 9. Lộ trình

Mỗi giai đoạn chỉ bắt đầu khi qua cổng trước nó.

| Giai đoạn | Thời gian | Gói | Việc chính | Cổng để qua |
|---|---|---|---|---|
| P0 · Xây nền | 30/09 → 15/10/2026 | Pro, ~0 USD | công cụ và agent (danh sách dưới), chạy thử 2 video | 2 video chạy thử qua release-qa ngay lần đầu |
| P1 · Bật từng làn | 16/10 → 30/11/2026 | Max 20x | bật làn chữ trước 2 tuần, rồi làn media; người vẫn tự tải lên; đo giờ người mỗi tuần | đạt 6 chỉ số ở mục 10 trong 4 tuần liền |
| P2 · Số liệu | 12/2026 → 01/2027 | Max 20x | community; strategist đọc CTR và giữ chân; tải lên qua API nếu kiểm định đạt | được bật YPP (nộp đơn trước 31/01/2027) |
| P3 · Sau YPP | từ 02/2027 | | lồng tiếng Anh và Bồ Đào Nha, thử nghiệm A/B | |

**Việc của P0, theo thứ tự:**

Công cụ:

- [ ] `tools/scene_pack.py`: đưa công cụ dựng cảnh (`mk2.py`, `ins.py`) vào repo, có test. Làm đầu tiên vì bản duy nhất đang nằm trong thư mục tạm của phiên cloud.
- [ ] `canon check --strict`:
  - chỉ tính dòng có "đã kiểm YYYY-MM-DD";
  - mỗi dòng một khẳng định;
  - lưu bằng chứng (link + đoạn trích + ngày).
- [ ] `tools/script_doctor.py`: báo cáo nhịp, so sánh trước và sau khi sửa (xem `docs/nghien-cuu-skill-kaku.md`).
- [ ] `tools/asr_check.py`: nghe lại giọng bằng nhận dạng giọng nói, so với lời thoại. Chưa biết VoiceStudio có endpoint nhận dạng không; nếu không thì dùng một mô hình chạy trên PC (cần kiểm lại).
- [ ] `costs` chặn cứng.
- [x] `tools/rights.py` với `videos/<x>/rights.csv` và `channel/rights-registry.json`; `tools/originality.py`; `release_check --write-audit` (30/09/2026, xem `docs/chinh-sach-noi-dung.md`).

Agent và điều phối:

- [ ] Tách `yt-studio` thành các skill theo bước, tên bắt đầu bằng `kaku-`: viết, media, phát hành.
- [ ] `tools/pipeline.py` và skill `kaku-pipeline`:
  - `status`: trạng thái suy từ file;
  - `next --lane chu|media`: chọn việc tiếp theo theo giới hạn số video;
  - `lease`: giữ và nhả khóa;
  - `reconcile`: đối chiếu với Notion.
- [ ] 7 file `.claude/agents/*.md` và các hook ở mục 7.
- [ ] Notion: trạng thái mới, cột mới, trang Công tắc.
- [ ] Tạo routine và Desktop task nhưng để **tắt**; thử từng cái bằng **Run now**.

Việc với YouTube:

- [ ] Nộp đơn kiểm định YouTube Data API sớm, vì xét duyệt lâu (cần kiểm lại thời gian).

Việc của bạn:

- chọn giọng Kaku trên VoiceStudio;
- tạo ảnh mẫu Kaku;
- cài Claude Desktop và Google Drive cho máy tính trên PC;
- duyệt hạn mức tháng;
- merge 2 kịch bản chạy thử.

**Không thay đổi suốt lộ trình:**

- nhịp đăng do người chốt: từ 06/10 là 3 video/ngày, xét lại ngày 25/10, tự ngắt về 1 video/ngày khi có dấu hiệu (`docs/lo-trinh.md`, Luật đổi hướng);
- giữ hạn chót nộp YPP 31/01/2027;
- quy trình làm tay (trang Xưởng Kaku, YouTube Studio) luôn chạy được.

## 10. Chỉ số thành công và quay về làm tay

Xét sau mỗi 4 tuần liền:

| Chỉ số | Mục tiêu |
|---|---|
| Thời gian của người | ≤ 2,5 giờ/ngày trong tháng 10; ≤ 3,5 giờ/ngày khi có kịch bản mới |
| Video lên đúng lịch | ≥ 95% |
| Qua release-qa ngay lần đầu | ≥ 80% |
| Khẳng định có bằng chứng trước khi làm giọng | 100% |
| CTR và giữ chân so với trung vị video làm tay | không kém quá 10% |
| Cảnh báo chính sách | 0 |

Tự ngắt:

- chi tiêu vượt 80% hạn mức → L1;
- có thư chính sách từ YouTube → L2;
- 6 video liền kém hơn mục tiêu CTR hoặc giữ chân → quay về làm tay cho làn bị nghi.

## 11. Rủi ro

| Rủi ro | Cách phòng |
|---|---|
| Bị coi là nội dung "không chân thực" | **Rủi ro lớn nhất từ 30/09:** 3 video/ngày là đúng kiểu nhịp đăng YouTube dùng để nhận diện nội dung làm hàng loạt. Xét lại ngày 25/10; tự ngắt về 1 video/ngày khi có dấu hiệu; góc nhìn do người viết; người xem từng video; không tự đăng |
| Agent bịa nguồn | fact-checker độc lập, không sửa kịch bản; `canon --strict`; chỉ tính trang đã mở |
| Prompt injection từ trang web, bình luận hoặc API `/fire` | nội dung ngoài chỉ là dữ liệu; community không đăng; routine không bật trigger API cho việc ghi; `/fire` vốn gắn nhãn nội dung gửi vào là không tin cậy |
| Lộ key | key ảnh chỉ ở PC; hook chặn in biến môi trường; không commit `.env` |
| Chi vượt | `costs` chặn cứng; hạn mức request trên Google Cloud; mức L1 |
| PC tắt hoặc ngủ | Keep computer awake; chạy bù một lần; kho 3 video đã đặt lịch |
| Notion lệch với file | file thật là nguồn đúng; đối chiếu mỗi đêm |
| Hết lượt routine hoặc hết hạn mức gói | gộp việc vào ít lượt chạy; lên Max 20x từ P1; kho video đệm |
| Video tải lên qua API bị khóa riêng tư khi project chưa kiểm định | người tự tải lên cho tới khi kiểm định đạt |
| Mất công cụ dựng cảnh | việc đầu tiên của P0 |
| Giấy phép giọng | chỉ `voxcpm2` (Apache-2.0); `rights check` chặn engine phi thương mại |
| Điều khoản ảnh Gemini chưa kiểm | `rights check` chặn mọi video dùng ảnh API cho tới khi mục `gemini-image-api` là `da-kiem`; người mở trang điều khoản trước 06/10 |
| Bị xem là nội dung hàng loạt (inauthentic) | `originality` từ 12/16, `plan_check`, `originality scan` mỗi đợt; `audit.md` ghi rủi ro high khi đăng hơn 1 video/ngày; xét nhịp 25/10 |

## 12. Nguồn

**Đã mở trang và đối chiếu (30/09/2026):**

- [Routines](https://code.claude.com/docs/en/routines):
  - lịch cách nhau tối thiểu 1 giờ; kích hoạt bằng API `/fire` hoặc sự kiện GitHub;
  - chạy không hỏi quyền; mỗi lần clone repo mới; đẩy lên nhánh `claude/`;
  - trần số lượt chạy mỗi ngày;
  - nội dung gửi qua `/fire` được bọc nhãn không tin cậy.
- [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks):
  - chạy trên máy khi app mở và máy thức;
  - tối thiểu 1 phút;
  - quyền đặt riêng cho từng task;
  - lỡ lịch thì chạy bù một lần.
- [Subagents](https://code.claude.com/docs/en/sub-agents): các trường frontmatter `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `hooks`, `memory`, `isolation`; mặc định 20 agent chạy song song, lồng tối đa 3 tầng.
- [Cloud environments](https://code.claude.com/docs/en/cloud-environments):
  - danh sách mạng mặc định có `*.googleapis.com`;
  - "API credentials" (Pro/Max): key được gắn vào request, phiên không thấy key;
  - giữa các phiên chỉ giữ ảnh chụp ổ đĩa của setup script.

**Chưa mở được trong phiên này (mạng chặn), cần kiểm lại:**

- YouTube Data API: [videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) và [kiểm định](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits):
  - video tải lên từ project chưa kiểm định bị khóa riêng tư;
  - hạn mức tải lên.
- Chính sách "inauthentic content" ([Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/)), và việc YouTube loại 16 kênh khỏi chương trình kiếm tiền ([Tech Times](https://www.techtimes.com/articles/320629/20260715/youtube-wiped-35m-subscribers-over-ai-slop-now-its-judging-your-taste.htm)).
- [Giá ảnh Gemini và giảm giá khi chạy batch](https://ai.google.dev/gemini-api/docs/pricing).
- VoiceStudio có endpoint nhận dạng giọng nói hay không: chưa thử trên máy thật.
