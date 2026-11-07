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

### 2026-11-08 — Unit 2 (past simple) ditulis: catatan "past simple belum punya unit" diperbarui
- **Kategori:** data · skill
- **Problem:** `reference/irregular-verbs.md` dan `/quiz-v` menyebut *past simple belum punya
  unit* sebagai alasan `/quiz-v` hanya menguji hafalan bentuk. Setelah Unit 2 ditulis, alasan
  itu tidak benar lagi. Unit 2 juga butuh tag grammar baru sebelum `/quiz` boleh memakainya.
- **Fix:** tag `A2-past-be` dan `A2-past-simple` ditambahkan ke taxonomy. Catatan di
  `irregular-verbs.md` dan `/quiz-v` diganti: `/quiz-v` **tetap** hafalan bentuk saja (perilaku
  tidak berubah), sedangkan pemakaian V2 di kalimat dilatih lewat `/quiz` · `/quiz-t` (Unit 2).
  Level dicek di PDF resmi: past simple & *was/were* = Core Inventory A1–A2; 11 kata Unit 2 =
  Oxford 3000 A1–A2, *souvenir* tidak ada di Oxford (CEFR `—`).
- **File:** `lessons/unit-02.md` (baru), `reference/quiz-taxonomy.md`,
  `reference/irregular-verbs.md`, `.claude/skills/quiz-v/SKILL.md`,
  `reference/oxford-vocabulary.md`, `README.md`, `docs/cara-kerja.md`

### 2026-11-07 — Pisah "boleh lanjut" (≥ 70%) dari "tuntas" (≥ 80%) + aturan naik level
- **Kategori:** pembelajaran · skill
- **Problem:** Satu-satunya syarat menulis unit baru adalah unit lama 🎉 tuntas (semua tag ≥ 80%
  di kedua jalur). Akibatnya materi baru tertahan: Unit 1 akurasi 84% tapi tertahan oleh
  `A2-present-perfect` Prod 5/10. Referensi (CEFR, ELP, GSE, ACTFL, Cambridge, KKTP) menunjukkan
  80% wajar untuk "dikuasai", tapi "boleh lanjut / berada di level" umumnya lebih longgar.
- **Fix:** Tiga tingkat: ✅ **boleh lanjut** = semua tag grammar unit ≥ 70% di kedua jalur
  (≥ 8 percobaan/jalur) → unit berikutnya boleh ditulis, tag yang belum 🟢 tetap terbawa lewat
  bobot adaptif; 🎉 **tuntas** = semua 🟢 (aturan lama); ⬆️ **naik level** = ≥ 80% tag level itu
  tuntas. Warna status 🔴/🟡/🟢 tidak diubah. Angka 70% dipilih user. Referensi baru di
  `official-sources.md` bagian 5b.
- **File:** `docs/cara-kerja.md`, `.claude/skills/quiz/SKILL.md`, `.claude/skills/quiz-t/SKILL.md`,
  `reference/official-sources.md`, `progress/evaluation.md` (catatan Unit 1)

### 2026-11-02 — `/quiz-v`: satu jenis soal (V1 + arti → V2, V3), kata harian dirotasi
- **Kategori:** skill · pembelajaran
- **Problem:** Sesi pertama mencampur dua jenis soal (recall *V1 → V2, V3* dan kalimat *I haven't
  ___ (wear)…*); user bingung kenapa dicampur. Kata baru juga diambil satu pola per sesi
  menurut urutan file (P1 dulu: *cost, cut, let*), bukan kata yang paling sering dipakai.
- **Fix:** Soal kalimat (S) dihapus: satu jenis saja, **model** menulis V1 + arti, user mengetik
  **V2, V3**. Kata dipilih model sesuai level aktif user (`diagnostic.md`, A2) dengan daftar
  **Harian** (40 kata kerja paling umum) dulu, pola dicampur, dirotasi (belum diuji → paling lama
  tidak diuji). (Sempat dicoba "arti saja → ketik V1, V2, V3", dibatalkan atas permintaan user.)
  Kolom tracker tidak berubah (`check-kb.py` tetap cocok).
- **File:** `.claude/skills/quiz-v/SKILL.md`, `CLAUDE.md`, `README.md`, `docs/cara-kerja.md`,
  `progress/verb-evaluation.md`, `reference/irregular-verbs.md`

### 2026-11-02 — Skill `/quiz-v`: hafalan bentuk kata kerja tidak beraturan
- **Kategori:** skill · data
- **Problem:** Belum ada latihan khusus V1 · V2 · V3. Bentuk V3 hanya teruji sambil lalu lewat
  `A2-present-perfect`, padahal kesalahan bentuk muncul berulang (*~~weared~~*, *~~have you study~~*).
- **Fix:** (1) `reference/irregular-verbs.md`: 85 kata kerja tidak beraturan (64 A1 + 21 A2),
  level dicek otomatis ke PDF Oxford 3000, dikelompokkan per pola bunyi (P1–P5). (2) Skill
  `/quiz-v` (pola `/kanji` proyek Jepang): jawaban diketik (*retrieval practice*), 8 soal,
  adaptif per kata, V2 hanya hafalan bentuk karena past simple belum punya unit; soal kalimat
  hanya V3 setelah *have/has*. (3) Tracker terpisah `progress/verb-evaluation.md` (per kata 5
  terakhir + per pola); `evaluation.md` tidak disentuh. (4) `check-kb.py` ikut mengecek tracker
  ini (+7 tes, 5 mutasi tertangkap).
- **File:** `reference/irregular-verbs.md`, `.claude/skills/quiz-v/SKILL.md`,
  `progress/verb-evaluation.md`, `progress/history.md` (label `VERB`), `scripts/check-kb.py`,
  `scripts/test_check_kb.py`, `CLAUDE.md`, `README.md`, `docs/cara-kerja.md`, `docs/perbaikan-kb.md`

### 2026-11-02 — Tes untuk `check-kb.py` (filosofi tes proyek Jepang)
- **Kategori:** data · skill
- **Problem:** `check-kb.py` sendiri belum dites. Kalau logikanya salah (mis. ambang atau aturan
  dua jalur), tracker yang salah bisa lolos tanpa ketahuan.
- **Fix:** Mengikuti pola `minna-no-nihongo-i`: logika dipisah jadi fungsi murni `check_text()`,
  lalu ditambah `scripts/test_check_kb.py` (runner stdlib, 21 tes: ambang & batas, aturan dua
  jalur, tiap jenis kesalahan terdeteksi, plus satu tes integrasi ke `evaluation.md` nyata).
  Sudah diuji dengan 5 mutasi, semuanya membuat tes merah. Skill `writing-good-tests` diadaptasi
  versi ringkas. `CLAUDE.md` aturan 9: jalankan cek setelah menulis `evaluation.md`.
  `__pycache__/` masuk `.gitignore`.
- **File:** `scripts/check-kb.py`, `scripts/test_check_kb.py`,
  `.claude/skills/writing-good-tests/SKILL.md`, `CLAUDE.md`, `README.md`, `.gitignore`,
  `docs/perbaikan-kb.md`

### 2026-11-02 — Script cek hitungan `evaluation.md`
- **Kategori:** data
- **Problem:** Semua hitungan di `evaluation.md` (urutan 10 terakhir, n/m, persen, status jalur,
  status tag dua jalur, Accuracy) dikerjakan Claude secara manual, tanpa ada yang memeriksa ulang.
- **Fix:** Tambah `scripts/check-kb.py` (read-only). Script ini mengecek tabel grammar (dua jalur
  + All-time + status tag) dan tabel skill/error/unit. Exit 1 kalau ada yang tidak cocok.
  Pakai: `python3 scripts/check-kb.py`.
- **File:** `scripts/check-kb.py`, `README.md`, `docs/perbaikan-kb.md`

### 2026-11-02 — Catatan koreksi kesalahan berulang + minimum 8 percobaan untuk unit tuntas
- **Kategori:** pembelajaran · skill
- **Problem:** (1) Kesalahan yang sama terus berulang tanpa penjelasan baru di unit. Contoh: *has*
  yang tidak perlu (*~~has always late~~*, *~~Rina has always happy~~*) muncul 4×, dan bentuk
  setelah *have* (*~~do you known~~*, *~~have you study~~*, *~~weared~~*) muncul 4×. Unit 1 belum
  punya catatan untuk dua pola ini. (2) Satu jalur bisa 🟢 hanya dengan 3/3, jadi unit bisa
  dinyatakan tuntas dengan bukti tipis.
- **Fix:** (1) Aturan baru di `konvensi-unit.md`: pola ≥ 3× → blok `⚠️ Koreksi` dengan cara
  penjelasan lain (Guskey 2010). `/quiz` dan `/quiz-t` menawarkannya di pesan akhir. Dua blok
  koreksi ditambahkan di Unit 1 (Point 1 & Point 2). (2) Syarat unit tuntas: semua tag 🟢 **dan**
  ≥ 8 percobaan per jalur (Bloom 1968: kelulusan dibuktikan ulang). Ambang 80% tidak diubah.
- **File:** `lessons/unit-01.md`, `docs/konvensi-unit.md`, `docs/cara-kerja.md`,
  `.claude/skills/quiz/SKILL.md`, `.claude/skills/quiz-t/SKILL.md`, `docs/perbaikan-kb.md`

### 2026-11-02 — Referensi riset untuk ambang 🟢 80% (unit tuntas)
- **Kategori:** data
- **Problem:** Ambang 🟢 ≥ 80% (syarat unit tuntas → tulis unit baru) tidak punya sumber tertulis.
  CEFR, Oxford, dan ETS memang tidak mengatur kapan boleh lanjut materi.
- **Fix:** Tambah bagian 5 di `official-sources.md` berisi sumber riset *mastery learning* yang
  sudah dicek lewat web: Bloom 1968, Slavin 1987 (80–90%), Guskey 2010 (80%), Kulik dkk. 1990,
  D'Albro (90% tidak lebih baik), dan Wilson dkk. 2019 (aturan 85%, dengan catatan batas cakupannya).
  Ambang tidak diubah.
- **File:** `reference/official-sources.md`, `docs/perbaikan-kb.md`

### 2026-11-02 — Status jalur tag grammar dari 10 percobaan terakhir
- **Kategori:** data · skill
- **Problem:** Akurasi per jalur dihitung dari semua riwayat. Kesalahan lama yang sudah diperbaiki
  terus menahan status, apalagi jalur Prod yang cuma ±4 soal/sesi (1 salah butuh ±4–5 benar untuk
  ditebus). Contoh: `A2-present-simple` Prod 16/21 (76%) padahal 3 sesi terakhir 8/9 (89%).
- **Fix:** Tiap jalur (MCQ/Prod) menyimpan urutan `✓/✗` maks 10 percobaan terakhir; status jalur
  dari urutan itu (< 3 ⚪, batas 80% tetap). C/T sepanjang waktu tetap dicatat sebagai info.
  Urutan lama direkonstruksi dari `history.md` (urutan dalam sesi tak diketahui → salah ditaruh
  lebih lama, konservatif). Level `minimal` `/quiz-t` = Prod ≥ 9/10. Efek: `A2-present-simple`
  🟡 → 🟢 (MCQ 8/10, Prod 8/10); `A2-present-perfect` tetap 🟡 (Prod 5/7).
- **File:** `progress/evaluation.md`, `.claude/skills/quiz/SKILL.md`,
  `.claude/skills/quiz/ref/translate.md`, `.claude/skills/quiz-t/SKILL.md`,
  `.claude/skills/diagnostic/SKILL.md`, `docs/cara-kerja.md`

### 2026-11-02 — Tag grammar dilacak dua jalur: pilihan ganda vs produksi
- **Kategori:** data · skill
- **Problem:** Hasil `/quiz` (pilihan ganda, 12 soal) dan `/quiz-t` (terjemahan, 4 soal) masuk ke
  satu angka yang sama per tag. Pilihan ganda lebih mudah (mengenali, bukan menyusun) dan lebih
  banyak soalnya, jadi status tag didominasi pilihan ganda. Contoh: `A2-present-perfect` tampil
  🟢 83% padahal di produksi baru 5/7 (71%).
- **Fix:** Tabel tag grammar di `evaluation.md` dipecah jadi kolom **MCQ** & **Prod** (data lama
  direkonstruksi dari `history.md`: present simple Prod 16/21, present perfect Prod 5/7; sisanya
  MCQ). Tag 🟢 hanya bila **kedua jalur 🟢**; jalur terburuk menentukan status. Hint fading
  `/quiz` pakai status jalur MCQ; level kosakata bantu `/quiz-t` pakai status jalur Prod. Tag
  skill/error/unit tetap satu jalur. Efek: `A2-present-perfect` 🟢 → 🟡, Unit 1 belum tuntas.
- **File:** `progress/evaluation.md`, `.claude/skills/quiz/SKILL.md`,
  `.claude/skills/quiz/ref/translate.md`, `.claude/skills/quiz-t/SKILL.md`,
  `.claude/skills/diagnostic/SKILL.md`, `docs/cara-kerja.md`

### 2026-10-30 — `/quiz` merotasi tema teks reading ala *Minna no Nihongo*
- **Kategori:** pembelajaran · skill
- **Problem:** Tema teks reading dipilih bebas tiap sesi (mis. rutinitas perawat), jadi
  cenderung berulang di sekitar tema unit dan tidak ada urutan situasi yang jelas.
- **Fix:** Tambah daftar 16 tema situasi sehari-hari (perkenalan → kota & lingkungan) di langkah
  2 `/quiz`; tiap sesi pakai tema berikutnya dari `Tema: <n>` terakhir di `history.md`
  (berputar). Baris history QUIZ sekarang mencatat `Tema: <n> <nama>`; sesi 2026-10-30 ditandai
  `Tema: 8 Pekerjaan & kantor` sebagai titik awal.
- **File:** `.claude/skills/quiz/SKILL.md`, `progress/history.md`

### 2026-10-29 — `/quiz` & `/quiz-t` memberi tahu kapan unit tuntas
- **Kategori:** skill
- **Problem:** Aturan pindah unit ("semua tag unit 🟢") hanya ada di `docs/cara-kerja.md`.
  Pesan akhir quiz cuma menampilkan perubahan status tag, jadi user harus menyimpulkan sendiri
  apakah sudah waktunya minta unit berikutnya.
- **Fix:** Pesan akhir `/quiz` (langkah 7) dan `/quiz-t` (langkah 6) kini memuat 1 baris cek
  kelulusan per unit yang diuji. Tag unit diambil dari kolom `Unit` di `quiz-taxonomy.md`. Semua
  🟢 → `🎉 Unit N tuntas → minta "tulis Unit N+1"` + kandidat tema; belum → `Unit N: x/y tag 🟢
  (…)`. Unit baru tetap **tidak** ditulis otomatis.
- **File:** `.claude/skills/quiz/SKILL.md`, `.claude/skills/quiz-t/SKILL.md`, `docs/cara-kerja.md`

### 2026-10-29 — Kosakata bantu `/quiz-t` tidak boleh ada yang terlewat
- **Kategori:** skill · pembelajaran
- **Problem:** Di `/quiz-t` pertama, beberapa kata kunci tidak ada di kosakata bantu: soal 1
  (*every* untuk "setiap"), soal 3 (*on* untuk "pada hari"), dan soal 4 (level `sebagian`) tanpa
  baris kosakata sama sekali (*coat, three, year*). Aturan "semua kata isi" ambigu soal kata
  fungsi non-uji, dan level `sebagian` (hanya kata di atas level aktif) praktis = kosong di A2.
- **Fix:** `penuh` = semua kata di kunci kecuali kata titik uji (termasuk *every, this, my, on*,
  angka) + cek wajib sebelum panel; `sebagian` = semua kata isi (kata fungsi kecil jadi tugas
  user); baris Kosakata bantu selalu ditulis (`—` bila sengaja kosong di `minimal`).
- **File:** `.claude/skills/quiz/ref/translate.md`

### 2026-10-29 — Teks reading wajib ikut di panel `/quiz`
- **Kategori:** skill
- **Problem:** Di `/quiz` pertama, teks reading (Maya) hanya tampil di chat; panel
  AskUserQuestion soal 11–12 berisi pertanyaan saja → panel menutupi chat, user tidak bisa
  membaca teksnya dan harus membatalkan panel.
- **Fix:** Aturan baru di langkah 4: `question` soal reading memuat teks utuh
  (`Reading: "<teks>"` + pertanyaan); semua soal satu teks di panel yang sama. (`/toefl` sudah
  punya aturan setara: ringkasan `【Text】` di panel.)
- **File:** `.claude/skills/quiz/SKILL.md`
- **Lanjutan (hari yang sama):** aturan diterapkan juga ke `/diagnostic` (sebelumnya teks hanya di
  chat) dan `/toefl` (sebelumnya hanya **ringkasan** `【Text】` → kini teks verbatim; teks panjang
  = kutipan paragraf relevan, soal main idea = teks utuh). File: `.claude/skills/diagnostic/SKILL.md`,
  `.claude/skills/toefl/SKILL.md`.

### 2026-10-29 — Skill `/lesson` untuk baca materi di chat
- **Kategori:** skill
- **Problem:** Materi unit hanya bisa dibaca di Obsidian. Saat diminta "lesson" di chat, Claude
  meringkas sendiri lalu langsung memberi soal cek pemahaman — user ingin **membaca materinya**,
  bukan dites.
- **Fix:** Skill baru `/lesson` (read-only): daftar unit/bagian, lalu tampilkan satu bagian
  **verbatim** via rentang baris heading (hemat token). Tanpa soal, tanpa menulis `progress/`.
  Didaftarkan di CLAUDE.md, README, dan cara-kerja.
- **File:** `.claude/skills/lesson/SKILL.md`, `CLAUDE.md`, `README.md`, `docs/cara-kerja.md`

### 2026-10-29 — Tiap poin unit wajib punya Kegunaan/Tujuan
- **Kategori:** pembelajaran · docs
- **Problem:** Di `unit-01`, Point 2 punya baris **Kegunaan** tapi Point 1 tidak; sub-aturan
  (negatif, tanya, adverbs of frequency, for/since) dan bagian Vocabulary/Reading/Phrases/TOEFL
  link juga tidak menjelaskan fungsinya → user hafal bentuk tapi kurang paham konteks pemakaian.
- **Fix:** Tambah `Kegunaan:` di Point 1 + kegunaan tiap sub-aturan Point 1 & 2 (termasuk alasan
  perbandingan dengan present continuous), `Tujuan:` di 4 bagian non-grammar, Quick summary
  menyebut kegunaan present simple. Konvensi unit kini mewajibkan pola ini.
- **File:** `lessons/unit-01.md`, `docs/konvensi-unit.md`

### 2026-10-29 — Rename proyek learn-english → cefr-to-toefl
- **Kategori:** docs
- **Problem:** Nama `learn-english` hanya menyebut bahasa, tidak menggambarkan jalur belajarnya, dan
  tidak sejajar dengan pola proyek Jepang (`learn-japan/minna-no-nihongo-i` = folder bahasa →
  proyek per jalur).
- **Fix:** Folder dipindah ke `~/rdeveloper/personal/learn-english/cefr-to-toefl` (jalur bertahap
  CEFR A1→C1 menuju TOEFL). Judul di README/CLAUDE.md/taxonomy/diagnostic diganti; path relatif ke
  proyek Jepang jadi `../../learn-japan/minna-no-nihongo-i`. Memory Claude Code disalin ke key path
  baru. Repo GitHub di-rename jadi `cefr-to-toefl`.
- **File:** `README.md`, `CLAUDE.md`, `reference/quiz-taxonomy.md`, `.claude/skills/diagnostic/SKILL.md`

### 2026-10-29 — CLAUDE.md dirampingkan; konvensi unit diekstrak
- **Kategori:** docs
- **Problem:** `CLAUDE.md` (dimuat tiap sesi) 123 baris dan banyak duplikat: pohon file lengkap
  (juga di README), deskripsi skill panjang (juga di SKILL.md), konvensi unit (hanya perlu saat
  menulis unit) → boros token tiap sesi.
- **Fix:** `CLAUDE.md` jadi hub ±50 baris (project, peta dokumen, tabel skill, 8 aturan inti).
  Konvensi unit + "perbedaan dari proyek Jepang" + aturan cek referensi resmi → `docs/konvensi-unit.md`.
  Pohon file detail → `README.md` (Folder map). Aturan baru eksplisit: **referensi resmi di atas
  ingatan model** (Core rule 2) dan tips batch tool call (dari Minna).
- **File:** `CLAUDE.md`, `docs/konvensi-unit.md`, `README.md`, `docs/cara-kerja.md` (peta
  komponen, alur baru **1b — Menulis unit**, bagian **Status sekarang**)

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
