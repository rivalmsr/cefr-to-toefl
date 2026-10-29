---
name: lesson
description: Baca materi unit dari lessons/ langsung di chat (read-only) — tampilkan daftar unit, daftar bagian satu unit, atau isi satu bagian APA ADANYA (verbatim, tidak diringkas). Tidak ada soal, tidak menulis file apa pun. Pakai saat user menjalankan /lesson atau minta "tampilkan/baca materi/unit/Point X/Reading/Vocabulary" di chat.
---

# Skill: /lesson — Baca Materi Unit di Chat

Alternatif membaca unit tanpa Obsidian. **Read-only:** tidak menulis `progress/`, tidak
memberi soal, tidak mengubah unit. Isi ditampilkan **verbatim** dari `lessons/unit-XX.md`
(source of truth) — **jangan diringkas, diparafrasa, atau ditambah**.

## Argumen

| Perintah | Aksi |
|---|---|
| `/lesson` | Daftar unit yang ada (nomor, judul, CEFR) + daftar bagian unit terbaru |
| `/lesson <n>` | Daftar bagian unit `n` (Quick summary + heading `##`/`###`) |
| `/lesson <n> <bagian>` | Tampilkan isi satu bagian unit `n`, verbatim |
| `/lesson <n> all` | Tampilkan seluruh unit (konfirmasi dulu bila > ~200 baris) |
| `/lesson next` | Bagian sesudah yang terakhir ditampilkan di sesi ini |

`<bagian>` dicocokkan longgar ke heading (tanpa beda huruf besar/kecil):
`1` / `p1` / `point 1` → `### Point 1 …`, `vocab` → `## Vocabulary …`, `reading`,
`phrases` / `speaking` / `writing` → `## Speaking / Writing phrases`, `toefl` → `## TOEFL link`,
`grammar` → seluruh `## Grammar` (semua Point), `summary` → blok Quick summary di atas.
Kalau ambigu / tidak cocok → tampilkan daftar bagian dan minta pilih.

## Langkah

1. **Peta heading (hemat token)** — satu command:
   `ls lessons/; grep -n "^#" lessons/unit-<nn>.md; wc -l lessons/unit-<nn>.md`
   (`<nn>` = nomor 2 digit, mis. `01`).
2. **Ambil rentang baris** bagian yang diminta: dari baris heading-nya sampai sebelum heading
   berikutnya yang levelnya sama atau lebih tinggi. Baca dengan `sed -n '<a>,<b>p'` (atau Read
   dengan offset/limit) — **hanya rentang itu**, bukan seluruh file.
3. **Tampilkan** isinya di chat sebagai markdown (jangan di dalam code block, supaya
   bold/italic/tabel ter-render). Buang garis pemisah `---` di ujung rentang.
4. **Tutup** dengan satu baris navigasi, mis.:
   `Bagian lain: summary · p1 · p2 · vocab · reading · phrases · toefl — atau /lesson next`

## Aturan

- **Verbatim.** Penjelasan tambahan hanya bila user bertanya, dan dipisah jelas di bawah
  materi (bahasa Indonesia mudah, contoh tetap English).
- **Jangan menjalankan soal/cek pemahaman** kecuali user minta → arahkan ke `/quiz` atau
  `/quiz-t`.
- Unit yang belum ditulis → bilang belum ada (lihat tabel *Written units* di `README.md`),
  jangan mengarang materi.
- Bila bagian sangat panjang (> ~80 baris), tampilkan per sub-bagian dan tawarkan lanjut.
