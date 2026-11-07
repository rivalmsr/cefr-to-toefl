---
name: quiz-v
description: Latihan HAFALAN bentuk kata kerja tidak beraturan: soal memberi V1 + arti (dipilih model sesuai level user, kata harian dulu, dirotasi) → user ketik V2, V3 (satu jenis soal saja), dari reference/irregular-verbs.md (Oxford 3000 A1–A2, dikelompokkan per pola bunyi). Default 8 soal (2 panel × 4). Adaptif per kata (5 percobaan terakhir) dan per pola. Rekam di progress/verb-evaluation.md + baris VERB di history.md; TIDAK menyentuh evaluation.md. Pakai saat user menjalankan /quiz-v atau minta latihan/hafalan verb 1 2 3, irregular verbs, V2 V3.
---

# Skill: /quiz-v — Hafalan bentuk kata kerja (V1 · V2 · V3)

**Tujuan:** hafal bentuk V2 · V3 kata kerja tidak beraturan lewat **mengingat sendiri**
(*retrieval practice*). **Model** memilih kata kerjanya (sesuai level user, kata yang sering dipakai
sehari-hari dulu, dirotasi) dan menulis **V1 + arti** di soal; user **hanya mengetik V2, V3**.
Pilihan ganda tidak dipakai, karena hanya melatih mengenali. **Satu jenis soal saja**, tidak
dicampur dengan soal kalimat (permintaan user 2026-11-02).

- **Berdiri sendiri** (seperti `/kanji` di proyek Jepang). Hanya menulis
  `progress/verb-evaluation.md` + baris `VERB` di `progress/history.md`. **Jangan** tulis
  `evaluation.md`.
- **Sumber kata = `reference/irregular-verbs.md` saja.** Jangan pakai kata kerja di luar file itu.
- **Hafalan bentuk saja, tanpa soal kalimat.** Pemakaian di kalimat dilatih di `/quiz` ·
  `/quiz-t`: V2 = past simple (Unit 2), V3 setelah *have/has* (Unit 1).
- **Jangan mengarang skor:** hitung eksplisit dari angka lama + hasil sesi.
- Instruksi, pembahasan, dan hasil dalam **Bahasa Indonesia yang mudah dipahami**. Kata kerja
  dalam **English**.

> **Hemat tool call:** gabung bacaan independen dalam satu perintah. Jangan pakai `echo =====`
> sebagai pemisah (zsh).

## Argumen

`/quiz-v [a1 | a2] [pola <P…>] [N]`
- Tanpa argumen → adaptif, **8 soal**. Pool = kata dengan CEFR ≤ level aktif user
  (`progress/diagnostic.md`, sekarang **A2**); kata **Harian** (langkah 2) dulu, lalu sisa A1,
  lalu sisa A2.
- `a1` / `a2` → batasi level. `pola P4c` (atau `pola P2a,P2b`) → hanya pola itu.
- `N` → jumlah soal (kelipatan 4 disarankan, maks 12).

## Langkah

### 1. Muat state (satu perintah)
`cat progress/verb-evaluation.md reference/irregular-verbs.md; head -12 progress/history.md; grep -m1 -A1 'CEFR level estimate' progress/diagnostic.md`

### 2. Pilih kata (urut prioritas, tanpa duplikat)
1. **Redrill** — kata ✗ di sesi `/quiz-v` terakhir (baris `VERB` teratas di `history.md`), maks 3.
2. **Lemah** — kata 🔴 lalu 🟡 di `verb-evaluation.md` (akurasi terendah dulu).
3. **Prioritas** — tabel "Prioritas (dari kesalahan nyata)" di `irregular-verbs.md`, bila belum
   pernah diuji.
4. **Baru (rotasi)** — kata yang belum pernah diuji, **paling sering dipakai sehari-hari dulu**:
   daftar **Harian** di bawah (urut dari kiri), lalu sisa A1, lalu sisa A2 (≤ level aktif). Campur
   pola (jangan satu pola per sesi). Rotasi: setelah semua kata pernah diuji, ambil yang paling
   lama tidak diuji.
5. **Pemeliharaan** — 1–2 kata 🟢 yang paling lama tidak diuji.

Isi sampai N. Kalau pool habis, ambil dari langkah 5.

**Harian** (kata kerja tidak beraturan paling umum dalam percakapan sehari-hari; urutan pilihan
pedagogis untuk rotasi, **bukan** level CEFR — level tetap dari `irregular-verbs.md`):
*be, have, do, go, get, make, say, see, come, take, know, think, give, eat, drink, buy, tell,
find, feel, sleep, write, read, meet, put, leave, pay, sit, speak, wake, wear, bring, send,
begin, lose, understand, hear, keep, run, spend, stand*

### 3. Jenis soal (hanya satu)
**V1 + arti → ketik V2, V3.** Soal menulis V1 dan arti dari kolom `Arti` di `irregular-verbs.md`;
user mengetik **V2, V3** saja. Tidak ada soal kalimat, tidak dicampur.

### 4. Sajikan (mode ujian: kumpulkan SEMUA jawaban dulu, koreksi di akhir)
- **4 soal per panel** AskUserQuestion (aturan 3 `CLAUDE.md`: ≤ 4/panel). Jawaban diketik di
  **Other**. Tiap soal punya 2 opsi tetap: **💡 Petunjuk pola** dan **⏭️ Lewati**. Tulis
  "ketik jawaban di kotak Other" di teks pertanyaan.
- Sebelum panel, tulis soalnya juga di chat sebagai `#` heading.
- **Format teks soal:**
  `Soal n/N — wear (memakai baju). Ketik V2, V3 di kotak Other (contoh format: went, gone).`
- **Header panel** (≤ 12 karakter): `Soal n`.
- **Jangan bocorkan pola** di soal (jangan urutkan soal per pola; acak urutannya).
- 💡 dipilih → beri **1 petunjuk pola** tanpa jawaban (mis. *"Polanya mirip drink → drank → drunk."*),
  tampilkan ulang soal itu. Soal itu tetap dinilai **✗** (belum ingat sendiri) dan ini
  **disebut di petunjuknya**.
- ⏭️ dipilih → ✗, kunci diberikan di akhir.

### 5. Nilai
- **✓ hanya bila V2 dan V3 keduanya benar**, termasuk ejaan (*writen* ✗). Huruf besar
  diabaikan. Pemisah koma atau spasi sama-sama diterima.
- Dua bentuk sah di referensi (*learned/learnt*, *got/gotten*) → keduanya ✓. *be* → harus
  menyebut *was* **dan** *were* (+ *been*).
- Satu soal = **satu percobaan** untuk kata itu.

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
