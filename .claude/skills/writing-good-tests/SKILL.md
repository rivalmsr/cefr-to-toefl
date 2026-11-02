---
name: writing-good-tests
description: Prinsip menulis & meninjau tes untuk script KB ini (scripts/test_check_kb.py → scripts/check-kb.py). Pakai saat menambah/mengubah tes, mengubah logika check-kb.py, atau menilai apakah sebuah tes ditulis dengan baik. Diadaptasi dari skill yang sama di proyek Jepang (../../learn-japan/minna-no-nihongo-i), versi ringkas.
---

# Menulis tes yang baik (script KB)

Tes yang baik itu **gampang dirawat**, **tahan refactor**, dan **bisa dipercaya**. Tiga hal ini
lebih penting dari angka coverage. Proyek ini proyek sekunder, jadi **tes hanya untuk logika
yang penting** (hitungan skor & status), tidak perlu memaksa coverage.

> **Stack:** Python 3 stdlib, **runner buatan sendiri** (`run()` di akhir file, tanpa pytest).
> Batas eksternal = **filesystem** (`progress/evaluation.md`). Tidak ada UI → hanya **unit test**
> + satu **tes integrasi** ke file nyata.

## Gampang dirawat
- **Nama tes = perilaku**, bukan mekanik: `test_tag_green_plus_grey_is_yellow`, bukan `test_tag_3`.
- **Satu perilaku per tes.** Kalau nama butuh "dan", pecah jadi dua.
- **Kecil** (< ~10 baris). Setup berulang → helper/fixture bernama (`_eval()`, `GOOD_GRAMMAR`).
- Urutan **Arrange → Act → Assert**.

## Tahan refactor (uji perilaku, bukan implementasi)
- Assert pada **kontrak**: daftar masalah dari `check_text()` dan exit code, bukan variabel
  internal. Assert **potongan pesan yang bermakna** (`"maks 10"`), bukan seluruh kalimat.
- Refactor yang tidak mengubah perilaku **tidak boleh** membuat tes merah.

## Bisa dipercaya
- Uji **jalur benar dan batas**: tepat di ambang (60%, 80%), < 3 percobaan, 0/0, jalur tanpa
  data, section hilang.
- **Deterministik:** tanpa acak, tanpa tanggal sekarang.
- **Terisolasi:** fixture dibuat di tes (string), jangan menulis ke `progress/`. Kalau perlu
  file, pakai `tempfile.mkdtemp()` + hapus di `finally`.
- **Pastikan tes BISA gagal.** Assert prakondisi dulu (mis. `n_rows > 0`, supaya tracker
  kosong tidak lulus diam-diam). Setelah menulis tes baru: **rusak sebentar kodenya** di salinan
  scratchpad (mutasi), pastikan tesnya merah. Jalankan mutasi dengan `python3 -I -B`, karena
  cache bytecode bisa membuat hasil mutasi palsu.

## Di repo ini
- **Jalankan:** `python3 scripts/test_check_kb.py` → exit 0 + `✅ N test lulus` = hijau;
  exit 1 + `❌ k/N test GAGAL` + traceback = merah. Runner menjalankan **semua** `test_*`
  (urut alfabetis) dan mengumpulkan semua kegagalan.
- **Pola desain:** logika = **fungsi murni** (`check_text(text)`, `tag_status`, `status_of`,
  `pct`) → tes tebal di situ. `main()` = wrapper tipis untuk I/O → cukup diuji lewat
  `test_real_evaluation_md_is_consistent`.
- **Tes integrasi file nyata merah?** Berarti hitungan sesi terakhir di `evaluation.md` salah
  (perbaiki trackernya), atau format tabel berubah (perbarui `check-kb.py` + tesnya).
- **Aturan skor berubah** (ambang, ukuran jendela, aturan dua jalur) → ubah `check-kb.py` **dan**
  tes batasnya di commit yang sama.
