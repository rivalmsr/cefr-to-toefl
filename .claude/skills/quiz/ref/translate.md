# /quiz — Mode terjemahan (dibaca HANYA saat `translate` / `/quiz-t`)

> Alur umum (muat state, cakupan, rekam) tetap di `quiz/SKILL.md`; file ini = penyajian,
> penyusunan & penilaian mode translate. Alias singkat: **`/quiz-t`** (skill `quiz-t` = jalur
> ringkas ke file ini).

Varian **produksi aktif**: user menulis sendiri terjemahan English dari kalimat Indonesia (bukan
pilih ganda). Klik pilihan ganda tak menangkap kelemahan **menyusun sendiri** — tense, agreement,
urutan kata, articles. Produksi bebas memaksa user merangkai kalimat utuh sendiri.

**Cakupan & bobot:** sama seperti `/quiz` (tag 🔴/🟡 di `evaluation.md` didahulukan, unit terbaru,
Weak areas). Default **4 soal** (produksi berat; boleh `unit X` / `N`).

## Penyajian (beda dari mode pilihan ganda)

- **1 soal = 1 panel** AskUserQuestion terpisah, berurutan.
- Input jawaban = opsi **"Other"** (kolom ketik). AskUserQuestion **wajib ≥2 opsi** → sediakan 2
  opsi bantu tetap: **💡 Minta petunjuk grammar** + **⏭️ Lewati soal ini**. Placeholder kotak Other
  tak bisa diganti → taruh instruksi "tulis jawaban di kotak Other" di **teks pertanyaan**.
  - 💡 dipilih → beri 1 petunjuk singkat (arah, bukan jawaban; mis. *"Keadaannya mulai di masa
    lalu dan masih berlangsung."*), lalu tampilkan ulang panel soal yang sama. Catat di Notes.
  - ⏭️ dipilih → soal dihitung **salah** (tanpa jawaban), kunci diberikan di akhir.
- Soal juga tampil besar di chat (`#` heading = kalimat Indonesia) sebelum panelnya.
- Kalimat sumber = Bahasa Indonesia; **jangan bocorkan struktur English-nya**.

## Instruksi & kosakata bantu (WAJIB)

Tujuannya membiasakan **menyusun kalimat sendiri**; bantuan dikurangi seiring mahir.

- **Instruksi sejelas mungkin:** tiap soal menyebut **konteks** (siapa bicara ke siapa / situasi)
  dan **waktu** kejadian.
- **⚠️ Bahasa Indonesia tidak punya tense → prompt WAJIB mengunci waktu.** Kalimat seperti
  *"Saya tinggal di Bandung"* bisa jadi *I live / I lived / I have lived*. Kunci lewat:
  - kata waktu eksplisit (*setiap hari, kemarin, sejak 2020, selama tiga tahun, sekarang*), atau
  - catatan konteks di kurung (*(sampai sekarang masih tinggal di sana)*).
  Tense yang **tidak** dikunci prompt **tidak boleh** dinilai salah.
- **Pertahankan konteks, pertajam TUJUAN:** tambah **1 baris tujuan** = pesan apa yang harus
  tersampaikan, ditulis sebagai **maksud komunikasi**, bukan nama grammar. Contoh:
  - 「Saya sudah tinggal di Bandung selama lima tahun.」 → `🎯 Tujuan: memberi tahu sudah BERAPA
    LAMA kamu tinggal di sana — dan kamu masih tinggal di sana sekarang.`
  - 「Kakak saya bekerja di bank, tapi dia tidak suka pekerjaannya.」 → `🎯 Tujuan: menjelaskan
    pekerjaan TETAP kakakmu (kebiasaan/fakta, bukan hanya hari ini) dan perasaannya.`
  - Tujuan **selalu ditampilkan di semua level** (kejelasan ≠ bantuan).
  - Hindari istilah teknis di instruksi (*present perfect, third person, auxiliary*) → kata sehari-hari.
- **Susunan panel:**
  ```
  Soal N/M — Terjemahkan ke English (tulis jawaban di kotak Other).
  (<konteks>. <waktu>.) Label: «<fungsi>»        ← label hanya di level penuh
  「<kalimat Indonesia>」
  🎯 Tujuan: <pesan yang harus tersampaikan>
  Kosakata bantu: <word (arti)> · …
  ```
- **Kosakata bantu = HANYA kata yang benar-benar muncul di kunci** — tanpa kata pengecoh. Urut
  sesuai kemunculan di kalimat Indonesia.
- **Bentuk:** kata kerja **bentuk dasar** (*live, work, go*), kata benda **tunggal** (*brother,
  year*). Konjugasi (*lives, lived, has lived*), jamak (*years*), dan articles tetap tugas user.
- **Kata grammar titik uji TIDAK diberikan** (*have/has, for/since, do/does, don't/doesn't,
  will, a/an/the*…) — itulah yang dilatih.
- **Level bantuan per tag sasaran** (dari status tag di `evaluation.md`):

  | Level | Status tag | Kosakata bantu | Label fungsi («durasi», «kebiasaan», «larangan»…) |
  |---|---|---|---|
  | `penuh` | ⚪ / 🔴 / 🟡 | semua kata isi di kunci | ditampilkan |
  | `sebagian` | 🟢 | hanya kata di atas level aktif (mis. B1+ saat level A2) + nama | tidak |
  | `minimal` | 🟢 ≥ 90% & Total ≥ 10 | hanya nama & kata di atas level aktif | tidak |

  Konteks, waktu, & tujuan **selalu** ada di semua level.
- Mode ujian tetap: kumpulkan **semua** jawaban dulu, koreksi & analisis **di akhir**.
- **Jangan** tampilkan kandidat terjemahan sebagai opsi (jadi pilih ganda). Kontras kandidat hanya
  dipakai **saat koreksi**.

## Penyusunan kalimat sumber (WAJIB — cek sebelum soal dipakai)

- **Grammar hanya dari unit in-scope** (`lessons/`); kosakata ≤ level aktif +1; boleh pakai kata
  lemah Anki (anchor `progress/anki-weak-items.md`) sebagai kata isi bila wajar.
- **Kunci SEMUA tense yang akan dinilai** — termasuk klausa kedua. Contoh cacat: *"Dia bilang
  dia capek"* → *She said she was tired* / *She says she is tired* dua-duanya sah bila waktu tak
  dikunci. **Fix:** *"Tadi pagi dia bilang..."* atau jangan nilai tense itu.
- **Subjek jelas tunggal/jamak** (hindari *keluarga saya, tim kami, semua orang* kecuali memang
  titik ujinya) — bahasa Indonesia tak menandai jamak.
- **1 soal produksi = 1 titik uji.** Jangan borong dua skill tak berkaitan dalam satu soal.
  Contoh cacat: *"Adik saya sudah belajar bahasa Inggris sejak SMP di sekolah yang terkenal"* →
  menguji present perfect + *since* **dan** articles/word order frasa *a famous school*. Bila salah
  di frasa sekolah, tag present perfect ikut kena. **Fix:** isolasi → *"Adik saya sudah belajar
  bahasa Inggris sejak SMP."*

## Penilaian (BERBASIS TITIK UJI — bukan kesempurnaan total)

1. Tiap soal punya **1 titik uji** (mis. *have/has + V3 + for/since*). ✅/❌ ditentukan oleh
   **titik itu**, bukan seluruh kalimat sempurna.
2. **Toleransi variasi sah:** kontraksi (*I've / I have*), sinonim yang tepat makna (*job / work*
   bila tak diuji), urutan keterangan waktu yang sah (*Every day I… / I… every day*), British vs
   American spelling (*favourite / favorite*), present perfect continuous bila sama sah
   (*have been living* untuk durasi) — **tidak** menggagalkan.
3. **Pisahkan slip dari kelemahan:** typo, huruf besar, article/preposisi **di luar** titik uji →
   **dicatat & dikoreksi**, tapi **tak** membuat ❌. Slip yang ADA di titik uji → ❌.
4. **Atribusi tag:** soal **benar** → +1 Correct & +1 Total untuk **semua** tag sasaran; soal
   **salah** → +1 Total **hanya untuk tag yang gagal**, supaya sub-skill yang sudah benar tak
   ikut dihukum. Error-type (`ERR-tense`, `ERR-agreement`, …) mengikuti titik yang gagal.
   `SK-writing` +1 Total per soal, +1 Correct bila soal ✅.
5. Koreksi di pesan akhir: tabel soal salah (`# · tag · jawabanmu · kunci`) + 1 baris fix tiap
   soal + slip minor sebagai catatan (bukan penyebab ❌).

## Penanda mode (WAJIB)

Baris `progress/history.md` untuk sesi ini: kolom Scope diawali **`QUIZ [translate]`** (mis.
`QUIZ [translate] (Unit 1)`), supaya sesi produksi bisa dipisahkan dari sesi pilihan ganda dengan
`grep "\[translate\]"`. Angka tetap masuk tabel tag yang sama di `evaluation.md`.
