# Konvensi Penulisan Unit

> Cara menulis & menambah unit materi (`lessons/unit-XX.md`). Diekstrak dari `CLAUDE.md` agar hub
> konteks tetap ringkas — detail ini hanya diperlukan saat **menulis atau mengedit** unit, bukan
> tiap sesi. Aturan lintas-sesi tetap di `CLAUDE.md`; peta besar di `docs/cara-kerja.md`.

## Siapa menulis & untuk apa

Berbeda dari proyek Jepang (di sana `lessons/` = catatan user), di sini **user tidak punya
catatan** — mereka hanya belajar **Oxford 3000 tier A1 di Anki (belum selesai)**. Jadi **Claude
menulis semua materi** (bertahap, standar CEFR, arah TOEFL), dan materi di `lessons/` menjadi
**source of truth** untuk semua skill. Karena A1 belum tuntas, unit awal juga **memperkuat
kosakata A1** — jangan anggap A1 sudah dikuasai.

Urutan & tema unit mengikuti roadmap A1→C1 di `README.md`; level awal dari `/diagnostic`.
Proyek sekunder → **satu unit sekali tulis**, jangan borong banyak unit.

## Struktur file unit (konvensi anchor)

Anchor (±20 baris pertama) inilah yang membuat baca-hemat-token valid: skill cukup membaca
judul + Focus + Quick summary tanpa memuat file utuh.

1. **Judul** `# Unit X — <Theme> (CEFR <level>)`
2. Blok **Focus** — tujuan unit dalam 2–4 kalimat (Bahasa Indonesia).
3. Blockquote **`> Quick summary:`** — menyebut **SEMUA** poin unit (wajib lengkap; ini yang
   dibaca skill saat memilih cakupan soal).
4. **Grammar** — tiap poin: **Aturan / Contoh / Catatan**. Penjelasan Bahasa Indonesia, contoh
   kalimat English. Kesalahan nyata user (dari tracker/diagnostic) ditandai ⚠️ di Catatan.
   **Aturan WAJIB dibuka dengan baris `Kegunaan:`** (dipakai untuk situasi apa), dan tiap
   sub-aturan (negatif, tanya, adverb, dsb.) diberi *kegunaan* singkat — bentuk tanpa fungsi
   sulit dipahami konteksnya.
   Bagian non-grammar (Vocabulary, Reading, Phrases, TOEFL link) dibuka dengan 1 baris
   **`Tujuan:`** (kenapa bagian ini ada).
5. **Vocabulary** — batch bertema; kolom `Word · POS · CEFR · Meaning (EN) · Arti (ID) · Example`.
6. **Reading** — teks pendek yang memakai grammar & vocab unit.
7. **Speaking / Writing phrases** — frasa siap pakai.
8. **TOEFL link** — kaitan ke task **TOEFL iBT 2026** (`reference/toefl-2026-spec.md`).

## Cek ke referensi resmi (WAJIB)

- **Level grammar** → poster Core Inventory per level (`reference/sources/core-inventory-posters-2018.pdf`).
  Poin di atas level unit boleh bila diambil dari kesalahan nyata user — sebut alasannya di Focus.
- **Tag CEFR kata** → PDF Oxford 3000/5000 by CEFR (`reference/sources/`). **Jangan dari ingatan.**
  Kata yang tidak ada di Oxford 3000/5000 → CEFR `—` (dan masuk tabel **Di luar Oxford** di
  `oxford-vocabulary.md`).
- **Kata akademik** → AWL (`reference/sources/awl-headwords.pdf`), mulai sublist 1.
- Daftar & link semua sumber: `reference/official-sources.md`.

## Saat menambah unit baru — file yang WAJIB ikut di-update

- `README.md` — tabel **Written units** + status roadmap.
- `reference/quiz-taxonomy.md` — tag grammar baru `<level>-<slug>` (**WAJIB sebelum skill memakainya**).
- `reference/oxford-vocabulary.md` / `academic-vocabulary.md` — batch kata unit di tabel level yang benar.

## Saat mengedit unit yang sudah ada

- **Jangan buang materi** — pindahkan/perbarui, dan **laporkan tiap perubahan** ke user.
- Perubahan karena aturan/referensi (bukan sekadar tambah materi) → 1 entri di `docs/perbaikan-kb.md`.
