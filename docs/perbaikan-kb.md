# Log Perbaikan KB (Improvement Log)

> Catatan **perbaikan sistem / knowledge** KB ini — bukan progres belajar (itu di
> `progress/`). Tiap entri: **Problem** (apa yang salah/kurang) → **Fix** (perbaikannya)
> → **Tanggal** + file terdampak. Entri terbaru **di atas**.
>
> Tujuan: supaya tiap keputusan desain & perbaikan aturan punya jejak "kenapa" — biar
> tak berulang & mudah ditinjau. Ini melengkapi `docs/cara-kerja.md` (peta cara kerja)
> dan `git log` (riwayat commit mentah).

## Kategori (WAJIB di tiap entri)
Tiap perbaikan diberi **1 kategori primer** (boleh + 1 sekunder bila benar-benar lintas,
pisah dengan ` · `). Dipakai untuk filter di Obsidian (search `Kategori: skill`).

| Kategori | Cakupan |
|---|---|
| `pembelajaran` | validitas & desain soal, pedagogi, isi unit — distraktor rancu, kunci tunggal, kebocoran jawaban, level CEFR materi, cakupan grammar |
| `skill` | perilaku/tampilan skill `/diagnostic`·`/quiz`·`/quiz-t`·`/toefl`·`/sync-anki` — format panel, mode, alias, aturan rekam |
| `data` | sumber & integrasi data — sync Anki, referensi resmi (Oxford, CEFR, ETS), tag taxonomy, tracker |
| `docs` | dokumentasi & peta proses |

## Cara menambah entri (untuk sesi berikutnya)
Setiap kali sebuah **aturan / logika / skill / referensi diperbaiki** (bukan sekadar tambah
materi atau update skor), tambahkan satu blok di paling atas daftar di bawah, format:

```
### YYYY-MM-DD — <judul singkat>
- **Kategori:** <pembelajaran|skill|data|docs> (opsional ` · <sekunder>`)
- **Problem:** <apa yang salah / kurang, sertakan contoh konkret bila ada>
- **Fix:** <apa yang diubah>
- **File:** <file yang tersentuh>
```

---

### 2026-10-29 — CLAUDE.md dirampingkan; konvensi unit diekstrak
- **Kategori:** docs
- **Problem:** `CLAUDE.md` (dimuat tiap sesi) 123 baris dan banyak duplikat: pohon file lengkap
  (juga di README), deskripsi skill panjang (juga di SKILL.md), konvensi unit (hanya perlu saat
  menulis unit) → boros token tiap sesi.
- **Fix:** `CLAUDE.md` jadi hub ±50 baris (project, peta dokumen, tabel skill, 8 aturan inti).
  Konvensi unit + "perbedaan dari proyek Jepang" + aturan cek referensi resmi → `docs/konvensi-unit.md`.
  Pohon file detail → `README.md` (Folder map). Aturan baru eksplisit: **referensi resmi di atas
  ingatan model** (Core rule 2) dan tips batch tool call (dari Minna).
- **File:** `CLAUDE.md`, `docs/konvensi-unit.md`, `README.md`

### 2026-10-29 — Log perbaikan + peta cara kerja (mengikuti proyek Minna)
- **Kategori:** docs
- **Problem:** Perbaikan aturan/skill hanya tercatat di `git log` dan chat; alasan di balik
  keputusan (mis. kenapa tag TOEFL lama dihapus) tidak tersimpan di repo. Belum ada penjelasan
  alur KB untuk manusia.
- **Fix:** Tambah `docs/perbaikan-kb.md` (file ini, entri hari ini di-backfill) +
  `docs/cara-kerja.md` (alur & diagram Mermaid); aturan wajib "Log perbaikan" di Core rules
  `CLAUDE.md`.
- **File:** `docs/perbaikan-kb.md`, `docs/cara-kerja.md`, `CLAUDE.md`, `README.md`

### 2026-10-29 — Unit 1: tag CEFR vocab & TOEFL link disesuaikan dengan referensi resmi
- **Kategori:** pembelajaran · data
- **Problem:** Tag CEFR di tabel Vocabulary Unit 1 ditulis dari ingatan, berbeda dari PDF Oxford
  resmi: *routine/relax/prepare* tertulis A2 (resmi **A1**), *schedule* B1 (resmi **A2**),
  *spare time* A2 (*spare* = **B2**, Oxford 5000), *commute/chore* B1 (padahal **tidak ada** di
  Oxford 3000/5000). Bagian TOEFL link masih menyebut Speaking Task 1 (Independent) & Writing
  (Independent) yang sudah tidak ada sejak TOEFL 2026.
- **Fix:** Kolom CEFR diperbaiki sesuai PDF Oxford; baris di `oxford-vocabulary.md` dipindah ke
  tabel level yang benar + tabel baru **Di luar Oxford 3000/5000** (CEFR `—`) + aturan "cek level
  di PDF resmi" di header. TOEFL link ditulis ulang ke task 2026 (Take an Interview, Write an
  Email/Academic Discussion, Build a Sentence); isi lama dipindah, tidak dibuang. Grammar
  dicek ke Core Inventory (present simple A1, present perfect A2) → sudah sesuai, tidak diubah.
- **File:** `lessons/unit-01.md`, `reference/oxford-vocabulary.md`

### 2026-10-29 — /quiz-t: alias mode translate + wajib kunci waktu di prompt
- **Kategori:** skill · pembelajaran
- **Problem:** Mode `translate` di `/quiz` hanya 1 baris aturan; tidak ada panduan penyajian,
  penyusunan, dan penilaian. Risiko khusus English: **Bahasa Indonesia tidak punya tense** —
  *"Saya tinggal di Bandung"* sah sebagai *I live / I lived / I have lived* → kunci rancu.
- **Fix:** Tambah `quiz/ref/translate.md` (1 soal/panel, input via Other + 💡/⏭️, 🎯 Tujuan,
  kosakata bantu bentuk dasar, level bantuan per status tag, 1 titik uji/soal, atribusi tag,
  toleransi variasi sah) dengan aturan **waktu wajib dikunci di prompt** dan **subjek jelas
  tunggal/jamak**; skill alias `/quiz-t`; `/quiz` merujuk ke ref ini.
- **File:** `.claude/skills/quiz-t/SKILL.md`, `.claude/skills/quiz/ref/translate.md`,
  `.claude/skills/quiz/SKILL.md`, `CLAUDE.md`, `README.md`

### 2026-10-29 — /toefl: pindah ke format TOEFL iBT 2026
- **Kategori:** skill · data
- **Problem:** Folder `.claude/skills/toefl/` kosong (SKILL.md tidak pernah ada). Taxonomy &
  templates memakai format lama (Integrated/Independent Writing, Speaking Task 1–4, skor 0–30),
  padahal TOEFL iBT berubah sejak **21 Januari 2026** (task baru, skala band 1–6).
- **Fix:** Tambah `reference/toefl-2026-spec.md` (struktur resmi ETS + tabel band ↔ CEFR & ↔
  0–120 dari laporan ETS April 2026). Tag TOEFL lama `SP-independent`, `SP-integrated`,
  `WR-integrated`, `WR-independent` **dihapus** (tracker masih kosong, tak ada data hilang) →
  diganti 11 tag task 2026; focus tag `RD-*`/`LS-*` dipertahankan. `toefl-templates.md` ditulis
  ulang (rubrik internal 0–5 Email/Discussion/Interview). Skill `/toefl` ditulis mengikuti pola
  `/jlpt` (mode harian/full/per section/review, kunci tunggal, posisi kunci diacak, persentase ≠
  band resmi). *Listen and Repeat* di luar cakupan (butuh audio).
- **File:** `.claude/skills/toefl/SKILL.md`, `reference/toefl-2026-spec.md`,
  `reference/quiz-taxonomy.md`, `reference/toefl-templates.md`, `progress/toefl-evaluation.md`,
  `reference/official-sources.md`, `CLAUDE.md`, `README.md`

### 2026-10-29 — /quiz: SKILL.md ditulis (sebelumnya folder kosong)
- **Kategori:** skill
- **Problem:** `.claude/skills/practice/` kosong — skill latihan harian terdokumentasi di
  `CLAUDE.md` tapi tidak bisa dijalankan.
- **Fix:** Tulis `quiz/SKILL.md` mengikuti `/quiz` Minna, tanpa engine: skor dihitung eksplisit
  oleh model (aturan hitung per tabel tracker), posisi kunci diacak via 1 perintah Python (model
  tak memilih letak kunci), daftar jebakan khas English (present perfect vs continuous, subjek
  ambigu, varian British/American).
- **File:** `.claude/skills/quiz/SKILL.md`

### 2026-10-29 — /sync-anki: kata lemah Oxford 3000 dari Anki
- **Kategori:** data · skill
- **Problem:** Tidak ada sinyal kata yang sering dilupakan di Anki → `/quiz` memilih kata
  pengisi soal tanpa data empiris.
- **Fix:** `scripts/sync-anki.sh` membaca salinan `collection.anki2` (deck `Oxford 3000 <level>`),
  tier 🔴/🟡/⚪ dari lapses + leech + kolom gagal 30 hari → `progress/anki-weak-items.md`
  (AUTO-GENERATED). Deck masih muda → selama 🔴 < 5, anchor diisi 10 kata teratas. Bias LUNAK di
  `/quiz` & `/toefl`.
- **File:** `scripts/sync-anki.sh`, `.claude/skills/sync-anki/SKILL.md`,
  `progress/anki-weak-items.md`, `CLAUDE.md`, `README.md`

### 2026-10-29 — Rename /practice → /quiz
- **Kategori:** skill
- **Problem:** Nama skill berbeda dari proyek Jepang (`/quiz`) → membingungkan saat berpindah proyek.
- **Fix:** Folder & semua rujukan diganti (`/practice` → `/quiz`, label history `PRACTICE` → `QUIZ`).
- **File:** `CLAUDE.md`, `README.md`, `progress/*.md`, `reference/*.md`,
  `.claude/skills/diagnostic/SKILL.md`

### 2026-10-29 — Indeks sumber resmi A1–C1
- **Kategori:** data
- **Problem:** Materi & level CEFR ditulis dari ingatan model, tanpa acuan dokumen resmi.
- **Fix:** `reference/official-sources.md` (CEFR Companion Volume, Core Inventory, Oxford 3000/5000
  by CEFR, Cambridge A2/B1 lists, AWL, ETS). PDF yang bisa diunduh disimpan di
  `reference/sources/` (**gitignored** — hak cipta penerbit).
- **File:** `reference/official-sources.md`, `.gitignore`, `CLAUDE.md`
