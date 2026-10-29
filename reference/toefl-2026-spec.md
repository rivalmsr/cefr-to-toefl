# TOEFL iBT 2026 — Spesifikasi Resmi (acuan `/toefl`)

Format TOEFL iBT **berubah sejak 21 Januari 2026**. File ini = acuan setara ujian asli untuk skill
`/toefl` (seperti `jlpt-n5-spec.md` di proyek Jepang). Jangan pakai format lama (Integrated
Writing, Independent Speaking, skor 0–30 per section) dari ingatan model.

> Sumber: **ETS** — halaman *Test Content* ([in.ets.org](https://www.in.ets.org/toefl/test-takers/ibt/about/content.html)),
> *Upcoming updates Jan 2026* ([in.ets.org](https://www.in.ets.org/toefl/test-takers/ibt/upcoming-updates-jan-2026.html)),
> dan laporan ETS *A banded score scale for the TOEFL iBT test* (April 2026,
> `reference/sources/ets-toefl-score-scale-update-2026.pdf`, Table 6–7).
> Baris bertanda † = dari situs persiapan pihak ketiga (belum dikonfirmasi ETS).

## 1. Struktur tes (ETS)

| Section | Task type (nama resmi) | Item | Waktu dasar |
|---|---|---|---|
| Reading | Complete the Words · Read in Daily Life · Read an Academic Passage | 50 | ±30 menit |
| Listening | Listen and Choose a Response · Listen to a Conversation · Listen to an Announcement · Listen to an Academic Talk | 47 | ±29 menit |
| Writing | Build a Sentence · Write an Email · Write for an Academic Discussion | 12 | ±23 menit |
| Speaking | Listen and Repeat · Take an Interview | 11 | ±8 menit |

- Waktu tidak termasuk instruksi; ETS menyarankan alokasi ±2 jam. Tanpa jeda terjadwal.
- Tes **adaptif** ("as the test adapts, test time and items may vary"). † Adaptif per modul hanya
  di Reading & Listening: Modul 1 sama untuk semua, Modul 2 lebih mudah/sulit sesuai hasil Modul 1.

## 2. Rincian task (†, situs persiapan — cocok dengan nama resmi ETS)

| Task | Yang dikerjakan | Jumlah ± |
|---|---|---|
| **Complete the Words** | Paragraf akademik pendek; 10 kata terpotong (separuh huruf akhir hilang) → lengkapi hurufnya | ±30 kata (3 paragraf) |
| **Read in Daily Life** | Teks sehari-hari (email, pengumuman, menu, jadwal, chat) → MCQ | 5–15 (set 2–3 soal) |
| **Read an Academic Passage** | Teks akademik ≤ ±200 kata → MCQ (main idea, detail, inference, vocab) | 5–15 |
| **Listen and Choose a Response** | Dengar 1 kalimat → pilih respons paling tepat | 15–19 |
| **Listen to a Conversation** | Percakapan pendek (kampus/sehari-hari) → MCQ | ±10 |
| **Listen to an Announcement** | Pengumuman kampus → MCQ | 6–10 |
| **Listen to an Academic Talk** | Kuliah pendek → MCQ | 8–16 |
| **Build a Sentence** | Susun kata-kata acak jadi 1 kalimat benar (dalam konteks dialog pendek) | 10 |
| **Write an Email** | Tulis email untuk situasi tertentu (3 poin wajib), ±7 menit | 1 |
| **Write for an Academic Discussion** | Tanggapi pertanyaan dosen + 2 pendapat mahasiswa, ±10 menit, ≥100 kata | 1 |
| **Listen and Repeat** | Dengar kalimat → ulangi persis (kalimat tidak ditampilkan) | 7 |
| **Take an Interview** | 4 pertanyaan wawancara, jawab ±45 detik tanpa waktu persiapan | 4 |

## 3. Skor (ETS)

- Tiap section **1–6** (kenaikan 0,5). **Overall = rata-rata 4 section**, dibulatkan ke 0,5
  terdekat (contoh ETS: 5,125 → 5).
- Selama transisi (Jan 2026 – Jan 2028) skor **0–120** yang setara juga dicantumkan.

### Band ↔ CEFR (ETS Table 7 — sama untuk semua section & overall)
| CEFR | Band |
|---|---|
| C2 | 6 |
| C1 | 5 – 5.5 |
| B2 | 4 – 4.5 |
| B1 | 3 – 3.5 |
| A2 | 2 – 2.5 |
| A1 | 1 – 1.5 |

### Band ↔ skor lama 0–30 / 0–120 (ETS Table 6)
| Band | Reading | Listening | Writing | Speaking | Total 0–120 |
|---|---|---|---|---|---|
| 6 | 29–30 | 28–30 | 29–30 | 28–30 | 114+ |
| 5.5 | 27–28 | 26–27 | 27–28 | 27 | 107+ |
| 5 | 24–26 | 22–25 | 24–26 | 25–26 | 95+ |
| 4.5 | 22–23 | 20–21 | 21–23 | 23–24 | 86+ |
| 4 | 18–21 | 17–19 | 17–20 | 20–22 | 72+ |
| 3.5 | 12–17 | 13–16 | 15–16 | 18–19 | 58+ |
| 3 | 6–11 | 9–12 | 13–14 | 16–17 | 44+ |
| 2.5 | 4–5 | 6–8 | 11–12 | 13–15 | 34+ |
| 2 | 3 | 4–5 | 7–10 | 10–12 | 24+ |
| 1.5 | 2 | 2–3 | 3–6 | 5–9 | 12+ |
| 1 | 0–1 | 0–1 | 0–2 | 0–4 | 0+ |

> **Target:** syarat Institute of Science Tokyo ditentukan **per program/graduate school** (tidak
> ada angka minimum tunggal) — cek guideline program tujuan. Sebagai patokan umum, program
> berbahasa Inggris biasanya meminta setara **B2 (band 4–4.5, ±72–94 skala lama)** atau lebih.

## 4. Adaptasi teks di KB ini (bukan ujian asli)

| Task | Versi `/toefl` | Catatan |
|---|---|---|
| Listening (semua) | **Transkrip** ditampilkan | Membaca ≠ mendengar → hasil Listening cenderung lebih tinggi dari aslinya |
| Listen and Repeat | **Di luar cakupan** | Tanpa audio tidak bisa diuji jujur |
| Take an Interview | User **mengetik** jawaban (±70–110 kata ≈ 45 detik bicara) | Dinilai isi & bahasa; pelafalan/kelancaran tidak terukur |
| Complete the Words, Build a Sentence | User mengetik jawaban (free-text) | Dinilai persis (ejaan / urutan) |
