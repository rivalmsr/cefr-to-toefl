---
name: toefl
description: Simulasi (mock) TOEFL iBT format 2026 berbasis teks — Reading (Complete the Words, Daily Life, Academic Passage), Listening via transkrip (Choose a Response, Conversation, Announcement, Academic Talk), Writing (Build a Sentence, Email, Academic Discussion), Speaking (Interview, jawaban diketik). Nilai jawaban, lalu perbarui tracker per subtype (progress/toefl-evaluation.md) + baris TOEFL di history.md. Pakai saat user menjalankan /toefl atau minta simulasi/mock/latihan TOEFL.
---

# Skill: /toefl — Mock TOEFL iBT 2026 (berbasis teks)

Jalankan **simulasi TOEFL iBT format 2026** (task resmi ETS), nilai jawaban, pelihara tracker
**per subtype** (`progress/toefl-evaluation.md`). Beda dari `/quiz` (harian, per grammar):
**JANGAN sentuh `evaluation.md` atau skill `/quiz`** — `/toefl` hanya menulis `toefl-evaluation.md`
+ baris `TOEFL` di `history.md`.

| File | Kapan dibaca |
|---|---|
| `reference/toefl-2026-spec.md` | **WAJIB, utuh** — struktur resmi, rincian task, tabel band ↔ CEFR |
| `reference/toefl-templates.md` | bila sesi memuat task free-text (`RD-words`, `WR-*`, `SP-interview`) — format, cara nilai, rubrik |

**Section & subtype:** Reading = `RD-words` · `RD-daily` · `RD-academic` · Listening (transkrip) =
`LS-response` · `LS-conversation` · `LS-announcement` · `LS-talk` · Writing = `WR-build` ·
`WR-email` · `WR-discussion` · Speaking = `SP-interview`. *Listen and Repeat* di luar cakupan.

## Prinsip inti (WAJIB)

1. **Setara ujian asli = `reference/toefl-2026-spec.md`.** Jangan pakai format lama (Integrated
   Writing, Independent Speaking, skor 0–30) dari ingatan model.
2. **Level materi = target ujian, bukan unit.** TOEFL tidak dibatasi `lessons/`: teks & soal
   memakai English akademik/kampus yang wajar. Mulai dari level **B1** (atau level section di
   tracker bila sudah ada), lalu adaptif (langkah 4). Kosakata akademik dari
   `reference/academic-vocabulary.md` / AWL; boleh di atas pool bila konteks menjelaskan.
3. **Bias LUNAK:** kata lemah Anki (anchor `progress/anki-weak-items.md`) boleh muncul di teks;
   grammar lemah dari `evaluation.md` (**read-only**) boleh jadi target `WR-build` / koreksi
   writing. Jangan memaksa.
4. **Tag hanya dari `reference/quiz-taxonomy.md`** (section TOEFL). **Jangan mengarang skor** —
   angka dihitung eksplisit; **jangan** mengonversi persentase ke band 1–6 seolah resmi.
5. **Bahasa:** semua soal, teks, transkrip dalam **English**; instruksi singkat, pembahasan, dan
   hasil dalam **Bahasa Indonesia yang mudah dipahami**.

**Hemat token:** baca `toefl-evaluation.md` + section TOEFL `quiz-taxonomy.md` +
`toefl-2026-spec.md` utuh; `toefl-templates.md` hanya bila perlu; (opsional) Weak areas
`evaluation.md` + anchor `anki-weak-items.md`. **Jangan** baca unit, `oxford-vocabulary.md` utuh.

## Parsing argumen

`/toefl [full | reading | listening | writing | speaking | review] [N]`

| Mode | Reading | Listening | Writing | Speaking | Total · waktu |
|---|---|---|---|---|---|
| `/toefl` = mock harian | words 1 set (10) · daily 2 · academic 3 | response 3 · conversation 2 · announcement 1 · talk 2 | build 3 | — | 16 MCQ/build + 1 set words · ±25 menit |
| `full` (mingguan) | words 2 set (20) · daily 5 · academic 6 | response 8 · conversation 4 · announcement 3 · talk 5 | build 6 · email 1 · discussion 1 | interview 4 | ±90 menit |
| `reading` | words 1 set · daily 3 · academic 5 | — | — | — | ±18 menit |
| `listening` | — | response 4 · conversation 3 · announcement 2 · talk 3 | — | — | ±15 menit |
| `writing` | — | — | build 5 · email 1 · discussion 1 | — | ±23 menit |
| `speaking` | — | — | — | interview 4 | ±8 menit |

- **1 set `RD-words`** = 1 paragraf dengan 10 kata terpotong (dihitung 10 item).
- `review` → hanya subtype 🔴/🟡 di tracker, 12 item (atau `N`). Tracker kosong → beri tahu user,
  jalankan mock harian. `N` hanya untuk `review`.
- Mock harian sengaja **tanpa** Email/Discussion/Interview (task panjang) supaya sesi tetap
  ringan → sarankan `writing` / `speaking` bergiliran di hari lain.

## Langkah eksekusi

### 1. Muat state
- Baca `progress/toefl-evaluation.md`, section TOEFL `quiz-taxonomy.md`, `toefl-2026-spec.md`.
- (Opsional) `Grep` Weak areas `progress/evaluation.md` + anchor `progress/anki-weak-items.md`.
- Cek `progress/history.md` (baris `TOEFL` terakhir) → **rotasi tema**: jangan ulang topik teks
  akademik/percakapan dari 3 sesi terakhir (variasikan bidang: biologi, sejarah, psikologi,
  teknik, ekonomi, seni, geologi, …; dan situasi kampus: perpustakaan, asrama, registrasi, lab, …).

### 2. Buat soal (format per subtype: bagian "Ringkasan subtype" di bawah)
Tiap soal: kunci, penjelasan singkat, `subtype` + (MCQ R/L) focus tag.
- **GERBANG kunci tunggal (WAJIB):** cek **tiap opsi** terhadap teks/transkrip — hanya satu yang
  didukung teks; distraktor = salah detail / kebalikan / tidak disebut / terlalu luas-sempit.
  Jawaban kunci **tidak boleh** bisa ditebak tanpa membaca teks.
- `RD-words` & `WR-build`: verifikasi satu jawaban tunggal (lihat `toefl-templates.md`).
- **Acak posisi kunci MCQ** — model tidak memilih letak kunci sendiri:
  `python3 -I -c "import random; print([random.randint(1,4) for _ in range(<jumlah MCQ>)])"`

### 3. Sajikan — MODE UJIAN (jawab semua dulu; kunci & pembahasan baru di akhir)
- Urutan section seperti ujian asli: **Reading → Listening → Writing → Speaking**. Header tiap
  section + waktu: `## Section 1 · Reading · ⏱️ 10 menit`. Instruksi resmi singkat (English)
  sekali per task, mis. `> Fill in the missing letters in the paragraph.`
- **Waktu:** jalankan `date +%s` tepat sebelum soal pertama dan setelah jawaban terakhir tiap
  section → catat menit terpakai vs batas (catatan saja, tidak menghentikan ujian).
- **Teks/transkrip** tampil sekali di chat (blockquote `>`; percakapan 1 pembicara per baris
  `**Woman:** …`). Transkrip Listening diberi label `🎧 Transcript`. Lalu soal-soalnya.
- Tiap soal MCQ di chat:
  ```
  ---

  # What is the main purpose of the announcement?

  **Soal 7 · Listening · Announcement (LS-announcement)**

  - **1.** …
  - **2.** …
  - **3.** …
  - **4.** …
  ```
  Lalu panel **AskUserQuestion ≤4 soal/panel**, urut nomor, **tidak mencampur dua teks dalam satu
  panel bila bisa**. `question` = pertanyaan + (soal berteks) ringkasan teks singkat berawalan
  `【Text】` cukup untuk menjawab tanpa scroll; `options` = 4 opsi persis urutan di chat.
- **Free-text** (`RD-words`, `WR-build`, `WR-email`, `WR-discussion`, `SP-interview`): tampilkan
  prompt sebagai `#` heading + instruksi format; minta user mengetik **semua jawaban task itu
  dalam satu pesan** (bernomor: `1. information 2. ...`). Untuk `SP-interview`: tampilkan
  pertanyaan **satu per satu** (seperti wawancara, tanpa persiapan), user menjawab tiap pertanyaan.
- **Hint fading `description`** (per subtype dari tracker): 🔴/🟡/⚪ → hint netral singkat
  (arti kata sulit dalam opsi, bahasa Indonesia); menuju 🟢 → lebih tipis; 🟢 → kosong (gaya
  ujian). Simetris di semua opsi; jangan bocorkan jawaban.
- **Adaptif (Reading & Listening, mode `full`/`reading`/`listening`):** soal dibagi 2 modul.
  Modul 1 di level awal; Modul 2 naik satu langkah (B1→B2, B2→C1) bila Modul 1 ≥ 75% benar, turun
  satu langkah bila < 50%. Nilai Modul 1 diam-diam (jangan tampilkan kunci). Mock harian: tanpa modul.

### 4. Nilai
- MCQ: jawaban vs kunci. `RD-words`: 1 poin per kata (ejaan persis). `WR-build`: 1 poin per kalimat.
- `WR-email`, `WR-discussion`, `SP-interview`: skor rubrik 0–5 dari `toefl-templates.md` (+ 1 alasan).
- Soal **rancu** (≥2 opsi terbukti sah) → hitung benar, catat. **Slip** (salah klik yang diakui
  user) → skor tetap salah, sebut di Notes.

### 5. Rekam (WAJIB, sebelum pesan hasil)
**`progress/toefl-evaluation.md`** — hitung eksplisit (lama + sesi = baru):
- **Reading / Listening / Writing-build (benar/salah):** per subtype `Correct` += benar, `Total` +=
  item; Accuracy = Correct/Total; Status: Total < 3 → ⚪ · < 60% 🔴 · 60–79% 🟡 · ≥ 80% 🟢.
  Hapus baris placeholder `_(empty)_` saat baris pertama ditambah.
- **Rubrik (email/discussion/interview):** `Avg score` = (avg lama × attempts lama + jumlah skor
  sesi) ÷ attempts baru (1 desimal). Status: attempts < 3 → ⚪ · avg < 3 🔴 · 3–3.9 🟡 · ≥ 4 🟢.
- **Weak types:** urutkan 🔴 lalu 🟡 (terendah di atas) + 1 baris pola kesalahan nyata.
- Ganti baris `_No data yet — run /toefl._` dengan `_Updated YYYY-MM-DD._`.

**`progress/history.md`** — tambah baris **paling atas** tabel:
`| YYYY-MM-DD | TOEFL <mode> | <N> | R <a>/<b> · L <c>/<d> · W <…> · S <…> | <1 kalimat: subtype terlemah + catatan waktu> |`

**Jangan** menyentuh `progress/evaluation.md`.

### 6. Hasil — RINGKAS (= pesan akhir)
- Skor per section + waktu vs batas (mis. `Reading 12/15 · 9/10 menit · Listening 6/8 · 7/6 menit
  (lewat)`), rubrik bila ada (`Email 3/5`).
- Sekali catatan: *persentase ≠ band resmi 1–6 (TOEFL asli adaptif & dinilai ETS); Listening di
  sini via transkrip sehingga cenderung lebih mudah. Target band per CEFR: `toefl-2026-spec.md` §3.*
- **Tabel soal SALAH saja** (`# · subtype · jawabanmu · kunci`) · 1 baris pembahasan per soal salah
  (kutip bagian teks/transkrip yang jadi bukti).
- Task free-text: skor + alasan + 1–3 koreksi terpenting (+ model answer singkat bila skor ≤ 3).
- 1 baris subtype terlemah · 1 baris saran: `→ /quiz <tag grammar>` bila kesalahan writing cocok
  dengan tag di taxonomy.

## Ringkasan subtype

**Reading**
- **`RD-words`** — paragraf akademik ±70–90 kata, kalimat pertama utuh, 10 kata terpotong
  separuh akhir (`inform_ _ _ _ _`). Kata umum (Oxford 3000/AWL 1–3), konteks mengunci 1 kata.
- **`RD-daily`** — teks sehari-hari 60–150 kata (email, pengumuman kampus, menu, jadwal, chat,
  iklan) → set 2–3 MCQ: tujuan teks, detail, inference ringan. Detail (jam, harga, tanggal)
  dihitung ulang; tiap distraktor salah karena satu detail jelas.
- **`RD-academic`** — teks akademik ±150–200 kata, 1 topik, 2–3 paragraf → MCQ campur focus:
  `RD-mainidea`, `RD-detail`, `RD-inference`, `RD-vocab` (kata AWL dalam konteks), `RD-paraphrase`.

**Listening (transkrip)**
- **`LS-response`** — 1 kalimat pembicara (pertanyaan/pernyataan sehari-hari) → pilih respons
  paling wajar. Distraktor: mengulang kata yang sama tapi tak nyambung, salah tense/orang, jawaban
  untuk pertanyaan lain. Hindari jawaban yang sah tapi "tidak langsung" sebagai distraktor.
- **`LS-conversation`** — percakapan 2 orang, 6–10 giliran (kampus/sehari-hari) → 2 MCQ
  (`LS-gist`, `LS-detail`, `LS-function`: kenapa pembicara bilang X / sikapnya).
- **`LS-announcement`** — pengumuman 80–120 kata (perubahan jadwal, acara, aturan) → 1–2 MCQ.
- **`LS-talk`** — kuliah pendek 150–200 kata, gaya lisan (*"So, today we're going to look at…"*) →
  2 MCQ (main idea + detail/fungsi contoh).

**Writing**
- **`WR-build`** — konteks 1 kalimat + rangka kalimat jawaban + 5–7 potongan acak → user mengetik
  kalimat utuh. Uji word order: pertanyaan tak langsung, posisi adverb, relative clause, passive.
- **`WR-email`** — situasi + penerima + 3 poin wajib; ±7 menit; rubrik 0–5.
- **`WR-discussion`** — pertanyaan dosen + 2 pendapat mahasiswa; ≥100 kata; ±10 menit; rubrik 0–5.

**Speaking**
- **`SP-interview`** — 4 pertanyaan berurutan (pribadi → pendapat umum), user mengetik ±70–110 kata
  per jawaban; rubrik 0–5 (isi & bahasa; pelafalan tidak dinilai).

## Gaya
Nada ramah dan santai; penjelasan singkat dalam Bahasa Indonesia. Nama pembicara bervariasi
(hindari selalu *John/Mary*). Jangan lebih dari jumlah item mode yang dipilih.
