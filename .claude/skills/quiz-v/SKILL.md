---
name: quiz-v
description: Latihan HAFALAN bentuk kata kerja tidak beraturan (V1 → V2 · V3), ketik bebas, dari reference/irregular-verbs.md (Oxford 3000 A1–A2, dikelompokkan per pola bunyi). Default 8 soal (2 panel × 4). Adaptif per kata (5 percobaan terakhir) dan per pola. Rekam di progress/verb-evaluation.md + baris VERB di history.md; TIDAK menyentuh evaluation.md. Pakai saat user menjalankan /quiz-v atau minta latihan/hafalan verb 1 2 3, irregular verbs, V2 V3.
---

# Skill: /quiz-v — Hafalan bentuk kata kerja (V1 · V2 · V3)

**Tujuan:** hafal bentuk V2 · V3 kata kerja tidak beraturan lewat **mengingat sendiri**
(*retrieval practice*): user **mengetik** bentuknya, bukan memilih. Pilihan ganda tidak dipakai,
karena hanya melatih mengenali.

- **Berdiri sendiri** (seperti `/kanji` di proyek Jepang). Hanya menulis
  `progress/verb-evaluation.md` + baris `VERB` di `progress/history.md`. **Jangan** tulis
  `evaluation.md`.
- **Sumber kata = `reference/irregular-verbs.md` saja.** Jangan pakai kata kerja di luar file itu.
- **V2 hanya sebagai hafalan bentuk.** Past simple belum punya unit (aturan 1 `CLAUDE.md`), jadi
  **jangan** buat soal kalimat V2 (*yesterday I ___*). Soal kalimat hanya untuk **V3 setelah
  *have/has*** (Unit 1, Point 2).
- **Jangan mengarang skor:** hitung eksplisit dari angka lama + hasil sesi.
- Instruksi, pembahasan, dan hasil dalam **Bahasa Indonesia yang mudah dipahami**. Kata kerja dan
  kalimat soal dalam **English**.

> **Hemat tool call:** gabung bacaan independen dalam satu perintah. Jangan pakai `echo =====`
> sebagai pemisah (zsh).

## Argumen

`/quiz-v [a1 | a2] [pola <P…>] [N]`
- Tanpa argumen → adaptif, **8 soal**, pool **A1** (A2 ikut masuk otomatis bila ≥ 80% kata A1
  sudah pernah diuji **dan** 🟢).
- `a1` / `a2` → batasi level. `pola P4c` (atau `pola P2a,P2b`) → hanya pola itu.
- `N` → jumlah soal (kelipatan 4 disarankan, maks 12).

## Langkah

### 1. Muat state (satu perintah)
`cat progress/verb-evaluation.md reference/irregular-verbs.md; head -12 progress/history.md`

### 2. Pilih kata (urut prioritas, tanpa duplikat)
1. **Redrill** — kata ✗ di sesi `/quiz-v` terakhir (baris `VERB` teratas di `history.md`), maks 3.
2. **Lemah** — kata 🔴 lalu 🟡 di `verb-evaluation.md` (akurasi terendah dulu).
3. **Prioritas** — tabel "Prioritas (dari kesalahan nyata)" di `irregular-verbs.md`, bila belum
   pernah diuji.
4. **Baru** — kata yang belum pernah diuji, **3–4 per sesi dari SATU pola** (pola berikutnya
   menurut urutan file: P1 → P2a → … → P5). Satu pola per sesi, supaya polanya terasa.
5. **Pemeliharaan** — 1–2 kata 🟢 yang paling lama tidak diuji.

Isi sampai N. Kalau pool habis, ambil dari langkah 5.

### 3. Tentukan jenis soal
| Jenis | Isi | Porsi (dari 8) |
|---|---|---|
| **R — Recall** | V1 + arti → ketik **V2, V3** | ±6 |
| **S — V3 di kalimat** | kalimat *have/has + ___ (V1)* → ketik **V3** saja | ±2 |

- Jenis **S** hanya untuk kata yang V3-nya beda dari V2, atau kata prioritas (lebih bermanfaat).
  Kalimatnya pakai konteks Unit 1 (*for/since*, *How long have/has…*), kosakata ≤ A2.
- Kalau ada kesalahan nyata user untuk kata itu, jenis S boleh berupa **perbaikan kalimat**
  (*I haven't ~~weared~~ this coat…* → ketik bentuk yang benar).

### 4. Sajikan (mode ujian: kumpulkan SEMUA jawaban dulu, koreksi di akhir)
- **4 soal per panel** AskUserQuestion (aturan 3 `CLAUDE.md`: ≤ 4/panel). Jawaban diketik di
  **Other**. Tiap soal punya 2 opsi tetap: **💡 Petunjuk pola** dan **⏭️ Lewati**. Tulis
  "ketik jawaban di kotak Other" di teks pertanyaan.
- Sebelum panel, tulis soalnya juga di chat sebagai `#` heading.
- **Format teks soal:**
  - R: `Soal n/N — wear (memakai). Ketik V2, V3 di kotak Other (contoh format: went, gone).`
  - S: `Soal n/N — I haven't ___ (wear) this coat for two weeks. Ketik bentuk yang benar di kotak Other.`
- **Header panel** (≤ 12 karakter): `Soal n`.
- **Jangan bocorkan pola** di soal (jangan urutkan soal per pola; acak urutannya).
- 💡 dipilih → beri **1 petunjuk pola** tanpa jawaban (mis. *"Polanya mirip drink → drank → drunk."*),
  tampilkan ulang soal itu. Soal itu tetap dinilai **✗** (belum ingat sendiri) dan ini
  **disebut di petunjuknya**.
- ⏭️ dipilih → ✗, kunci diberikan di akhir.

### 5. Nilai
- **✓ hanya bila semua bentuk yang diminta benar**, termasuk ejaan (*writen* ✗). Huruf besar
  diabaikan. Pemisah koma atau spasi sama-sama diterima.
- Dua bentuk sah di referensi (*learned/learnt*, *got/gotten*) → keduanya ✓. *be* → harus
  menyebut *was* **dan** *were* (+ *been*).
- Satu soal = **satu percobaan** untuk kata itu (jenis R maupun S).

### 6. Rekam (WAJIB, sebelum pesan hasil)
**`progress/verb-evaluation.md`** (hitung eksplisit: lama + sesi = baru):
- **Per verb:** tambahkan `✓`/`✗` ke urutan kata itu (maks 5, buang dari kiri). Kolom `Last 5` =
  `` `<urutan>` c/m (p%) <status> ``. Kolom `All-time` = `c/t` (ditambah tiap sesi). Status:
  < 3 ⚪ · < 60% 🔴 · 60–79% 🟡 · ≥ 80% 🟢. Kolom `Status` = status yang sama + catatan singkat
  (salah ketik nyata, tanggal). Kata baru → tambah baris. Hapus baris placeholder _(none yet)_.
  Urutkan baris per pola, lalu abjad.
- **Per pattern:** `Correct` += benar, `Total` += soal untuk pola itu; Accuracy = Correct/Total
  (bulatkan, .5 ke atas); status dengan ambang yang sama.
- **Weak verbs:** daftar kata 🔴/🟡 (akurasi terendah di atas) + jawaban salah nyata user.
- Perbarui baris "_Updated …_" di header.
- Lalu jalankan **`python3 scripts/check-kb.py`** (harus ✅, aturan 9 `CLAUDE.md`). ❌ → perbaiki
  tracker dulu sebelum pesan hasil.

**`progress/history.md`** — baris **paling atas** tabel:
`| YYYY-MM-DD | VERB (<pola/level yang diuji>) | <N> | <benar>/<N> (<%>) | ✗ <kata: jawabanmu → kunci>, …; pola baru: <P…> |`

### 7. Hasil — RINGKAS (= pesan akhir)
- Skor 1 baris.
- **Tabel soal SALAH saja** (`# · kata · jawabanmu · kunci`). Semua benar → pujian singkat.
- 1 baris per soal salah: **pola** kata itu + 1 kata lain **dari pola yang sama di
  `irregular-verbs.md`** sebagai jangkar (*wear → wore → worn, polanya sama seperti
  break → broke → broken: V2 pakai o, V3 berakhiran -n/-en*).
- 1 baris progres: `Pool A1: x/64 kata sudah diuji, y 🟢` (+ A2 bila aktif).
- Tawarkan pembahasan lebih dalam bila user mau. **Jangan** cetak ulang seluruh tracker.
