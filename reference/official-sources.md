# Official Sources (acuan resmi A1–C1)

Daftar dokumen **resmi** yang dipakai sebagai acuan saat Claude menulis unit di `lessons/` dan
mengisi `reference/`. File PDF yang berhasil diunduh ada di `reference/sources/`. Folder itu
**tidak di-commit** ke git (`.gitignore`), karena dokumennya milik penerbit masing-masing.
Kalau folder itu kosong (misalnya di komputer lain), unduh ulang dari link di bawah.

> Status: ✅ sudah diunduh ke `reference/sources/` · 🔗 link saja (situs menolak unduhan otomatis,
> unduh manual lewat browser kalau perlu)

## 1. Kerangka level CEFR (deskriptor "bisa melakukan apa" per level)
| Dokumen | Penerbit | Dipakai untuk | Status / file |
|---------|----------|---------------|---------------|
| CEFR Companion Volume (2020) | Council of Europe | definisi resmi A1–C2 per skill (reading, listening, speaking, writing, interaksi, mediasi) | 🔗 [rm.coe.int/16809ea0d4](https://rm.coe.int/16809ea0d4) · [halaman resmi](https://www.coe.int/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions) |

## 2. Grammar & fungsi per level
| Dokumen | Penerbit | Dipakai untuk | Status / file |
|---------|----------|---------------|---------------|
| Core Inventory for General English (2011) | British Council & EAQUALS | daftar grammar, fungsi, discourse marker, dan topik per level A1–C1 → acuan roadmap unit | ✅ `core-inventory-general-english-2011.pdf` |
| Core Inventory Posters (update 2018) | British Council & EAQUALS | ringkasan 1 halaman per level dari dokumen di atas | ✅ `core-inventory-posters-2018.pdf` |
| English Grammar Profile | Cambridge (English Profile) | database online: struktur grammar + level CEFR-nya, berdasarkan korpus pelajar | 🔗 [englishprofile.org](https://www.englishprofile.org) |

## 3. Vocabulary per level
| Dokumen | Penerbit | Dipakai untuk | Status / file |
|---------|----------|---------------|---------------|
| Oxford 3000 by CEFR level | Oxford University Press | kata A1–B2 (sama dengan deck Anki kamu) → sumber `oxford-vocabulary.md` | ✅ `oxford-3000-by-cefr.pdf` |
| Oxford 5000 by CEFR level | Oxford University Press | tambahan kata B2–C1 | ✅ `oxford-5000-by-cefr.pdf` |
| A2 Key vocabulary list | Cambridge English | cek silang vocab A2 | ✅ `a2-key-vocabulary-list.pdf` |
| B1 Preliminary vocabulary list | Cambridge English | cek silang vocab B1 | ✅ `b1-preliminary-vocabulary-list.pdf` |
| English Vocabulary Profile | Cambridge (English Profile) | level CEFR per *arti* kata (satu kata bisa A1 di satu arti, B2 di arti lain) | 🔗 [englishprofile.org](https://www.englishprofile.org) |
| Academic Word List — headwords | Victoria University of Wellington (Coxhead, 2000) | 570 word family akademik untuk TOEFL → sumber `academic-vocabulary.md` | ✅ `awl-headwords.pdf` · [sublist 1–10](https://www.wgtn.ac.nz/lals/resources/academicwordlist) |

## 4. TOEFL iBT ↔ CEFR
| Dokumen | Penerbit | Dipakai untuk | Status / file |
|---------|----------|---------------|---------------|
| Mapping TOEFL iBT ke CEFR (RM-15-06, 2015) | ETS | skor minimum per section untuk tiap level (B1–C1) | ✅ `ets-toefl-cefr-mapping-RM-15-06.pdf` |
| A banded score scale for the TOEFL iBT test (April 2026) | ETS | tabel resmi band 1–6 ↔ CEFR & ↔ skor lama 0–120 (Table 6–7) → disalin di `toefl-2026-spec.md` | ✅ `ets-toefl-score-scale-update-2026.pdf` |
| Compare scores (tabel resmi terbaru) | ETS | tabel skor TOEFL ↔ CEFR yang berlaku sekarang | 🔗 [ets.org compare scores](https://www.ets.org/toefl/score-users/ibt/compare-scores.html) |
| TOEFL iBT updates (Januari 2026) | ETS | format baru: skala 1–6 yang selaras CEFR, Reading/Listening adaptif, tes lebih pendek | 🔗 [ets.org upcoming updates](https://www.in.ets.org/toefl/test-takers/ibt/upcoming-updates-jan-2026.html) |

> ⚠️ **Catatan TOEFL 2026:** sejak **21 Januari 2026** TOEFL iBT memakai format baru dengan skala
> **1–6** (selama masa transisi sampai Januari 2028, skala lama 0–120 juga tetap dicantumkan).
> Skill `/toefl` dan `toefl-templates.md` perlu dicek apakah masih memakai format lama.

## 5. Ambang "tuntas" & lanjut ke materi baru (riset pendidikan, bukan standar resmi)
CEFR, Oxford, dan ETS **tidak** mengatur kapan pelajar boleh lanjut ke materi baru. Ambang 🟢
**≥ 80%** (dari 10 percobaan terakhir, kedua jalur) di `docs/cara-kerja.md` berdasar riset
*mastery learning* di bawah ini.

| Sumber | Isi yang relevan | Dipakai untuk | Status / link |
|--------|------------------|---------------|---------------|
| Bloom, B. S. (1968). *Learning for Mastery*. UCLA **Evaluation Comment**, 1(2) | dasar *mastery learning*: siswa lulus tes formatif unit dulu (kalau belum, dapat perbaikan), baru lanjut ke unit berikutnya | konsep "unit tuntas → baru tulis unit baru" | 🔗 [CRESST (UCLA)](https://cresst.org/?p=2412) |
| Slavin, R. E. (1987). *Mastery Learning Reconsidered*. **Review of Educational Research**, 57(2) | ambang mastery yang dipakai *"usually in the range of 80–90% correct"* | rentang wajar ambang 🟢 | 🔗 [PDF (gwern.net)](https://www.gwern.net/doc/psychology/1987-slavin.pdf) |
| Guskey, T. R. (2010). *Lessons of Mastery Learning*. **Educational Leadership**, 68(2), ASCD | target mastery **80% or better**; perbaikan ≠ sekadar mengulang materi yang sama | dasar angka **80%** | 🔗 [ascd.org](https://www.ascd.org/publications/educational-leadership/oct10/vol68/num02/Lessons-of-Mastery-Learning.aspx) |
| Kulik, Kulik & Bangert-Drowns (1990). *Effectiveness of Mastery Learning Programs: A Meta-Analysis*. **Review of Educational Research**, 60(2), 265–299 | 108 studi terkontrol: mastery learning menaikkan nilai ujian; pelajar yang lebih lemah paling diuntungkan | bukti bahwa model "tuntas dulu" efektif | 🔗 [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265) |
| D'Albro (disertasi, Michigan State Univ.) | membandingkan ambang tetap 80%, tetap 90%, dan ambang naik bertahap: **90% tetap** membuat waktu belajar kurang efisien **tanpa** kenaikan hasil | alasan **tidak** menaikkan ambang ke 90% | 🔗 [d.lib.msu.edu](https://d.lib.msu.edu/etd/25195/FULL_TEXT/view) |
| Wilson, Shenhav, Straccia & Cohen (2019). *The Eighty Five Percent Rule for optimal learning*. **Nature Communications**, 10:4646 | belajar paling cepat saat akurasi latihan ±**85%** (error ±15,87%) | soal latihan sebaiknya menantang, jangan terlalu mudah. ⚠️ Diuji pada model jaringan saraf & tugas persepsi sederhana, jadi penerapan ke kelas bahasa hanya ekstrapolasi | 🔗 [PMC6831579](https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579) |

> Ringkasnya: **80%** ada di batas bawah rentang mastery (80–90%). Angka ini cocok untuk proyek
> sekunder yang ringan, apalagi syarat dua jalur (MCQ + Prod) sudah lebih ketat dari model
> standar. Menaikkan ke 90% tidak terbukti menambah hasil (D'Albro).

### 5b. Kerangka bahasa & kurikulum: "dikuasai" vs "boleh lanjut / naik level" (dicek 2026-11-07)
Tidak ada sumber yang memberi satu angka resmi untuk "boleh lanjut ke materi berikutnya". Yang
konsisten: menandai **dikuasai** umumnya ±80%, sedangkan **berada di / lanjut ke** suatu level
lebih longgar (tidak harus menguasai semuanya). Dasar tingkat ✅ boleh lanjut (≥ 70%) · 🎉 tuntas
(≥ 80%) · ⬆️ naik level (≥ 80% tag level tuntas) di `docs/cara-kerja.md`.

| Sumber | Isi yang relevan | Dipakai untuk | Status / link |
|--------|------------------|---------------|---------------|
| Council of Europe, **CEFR** (2001, bab 2.2 & 9.3) + Companion Volume (2020) | penilaian berbasis kriteria *can do*; membedakan *achievement* (menguasai materi kursus) vs *proficiency* (level); ambang *mastery* diserahkan ke penyusun kursus — **tanpa angka persen** | alasan ambang ditentukan KB sendiri | 🔗 [CoE: Assessing CEFR level](https://rm.coe.int/assessing-cefr-level/1680a9178c) · [ECML worksheet](https://www.ecml.at/Portals/1/3MTP/ECEP/training-kit/PageEN/P/WORKSHEET_A_Assessment_traditions.pdf) |
| Council of Europe, **European Language Portfolio** — checklist self-assessment | bisa ≥ **80%** butir *can do* suatu level → "kemungkinan sudah mencapai" level itu (disebut pedoman kasar) | ambang 🎉 tuntas & ⬆️ naik level | 🔗 [rm.coe.int/16804932bf](https://rm.coe.int/16804932bf) · [ELP Swiss, Appendix 2](https://www.readkong.com/page/appendix-2-self-assessment-checklists-from-the-swiss-9391014) — ⚠️ kalimat dibaca lewat versi Swiss/salinan, bukan teks CoE asli |
| Pearson, **Global Scale of English** (GSE Learning Objectives; English Performance Standards) | "berada di" suatu level = ±**50%** peluang berhasil di tugas level itu; berada di level ≠ menguasai semua tujuannya | alasan "boleh lanjut" lebih longgar dari "tuntas" | 🔗 [GSE LO overview](https://www.pearsoncanadaschool.com/content/dam/websites/pearson-canada-school/assets/documents/literacy/gse/gse-learning-objectives-overview.pdf) · [Performance Standards](https://www.pearson.com/content/dam/global-store/global/resources/efficacy/evidence-about-learning/Pearson-Learning-Design-Principles-English-Performance-Standards-summary.pdf) |
| **ACTFL** Proficiency Guidelines 2024 | rating suatu level butuh performa **konsisten** di semua kriteria FACT level itu | alasan syarat **kedua jalur** + minimum 8 percobaan | 🔗 [Guidelines 2024](https://www.isbe.net/Documents/ACTFL-Proficiency-Guidelines-2024.pdf) |
| **Cambridge English** A2 Key | lulus = skor skala **120** (Cambridge English Scale), bukan persen mentah; angka "70%" yang beredar tidak ada di dokumen resmi | catatan: jangan mengutip "Cambridge = 70%" | 🔗 [A2 statement of results](https://www.cambridgeenglish.org/images/664442-a2-statement-of-results-factsheet.pdf) |
| **Kurikulum Merdeka — KKTP** (pengganti KKM) | guru menetapkan kriteria per tujuan pembelajaran; contoh template sekolah: 66–85% = tuntas, < 66% = remedial | dasar angka **70%** (±66% dibulatkan) | 🔗 [modul PMIKM (arsip)](https://archive.org/download/rekap-final-pmikm-sd-22032023/REKAP%20FINAL%20PMIKM%20SD%2022032023.zip/REKAP%20FINAL%20PMIKM%20SD%2022032023%2F014%20Kriteria%20Ketercapaian%20Tujuan%20Pembelajaran%20SUDAH.pdf) · [mysch.id](https://mysch.id/blog/detail/332/kktp-adalah) — ⚠️ template sekolah, **bukan** ketentuan nasional Kemendikbud |

> ⚠️ Angka **70%** adalah **pilihan desain** KB ini (disintesis dari sumber di atas, dipilih user
> 2026-11-07), bukan angka yang tertulis persis di satu sumber.

## Cara pakai (aturan untuk Claude)
- Saat menulis unit baru: cek grammar di **Core Inventory** (level yang sesuai) dan ambil vocab
  dari **Oxford 3000/5000 by CEFR**. Tag CEFR di `oxford-vocabulary.md` harus sama dengan PDF Oxford.
- Vocab akademik: ambil dari **AWL**, mulai dari sublist 1 (kata paling sering).
- Target skor TOEFL: pakai tabel ETS untuk menerjemahkan level CEFR ke skor per section.
