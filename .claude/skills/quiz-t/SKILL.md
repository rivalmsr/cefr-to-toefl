---
name: quiz-t
description: Alias singkat untuk /quiz translate — sesi TERJEMAHAN PRODUKSI (Indonesia→English, tulis-bebas) dari unit di lessons/. User menyusun kalimat English sendiri (bukan pilihan ganda), 1 soal/panel, default 4 soal. Perbarui evaluation.md + history.md seperti /quiz. Pakai saat user menjalankan /quiz-t (atau /quiz translate).
---

# Skill: /quiz-t — Mode terjemahan produksi

`/quiz-t` **= `/quiz translate`** (aturan sama, tidak ada mekanisme baru). File ini = **jalur
ringkas** yang sudah memuat bagian `quiz/SKILL.md` yang relevan → **jangan baca
`quiz/SKILL.md`**; satu-satunya bacaan skill tambahan = `quiz/ref/translate.md` (penyajian,
penyusunan, penilaian).

> **Hemat tool call:** gabung bacaan independen dalam satu perintah (`cat a b; head …`).
> **Jangan** pakai `echo =====` sebagai pemisah — di zsh kata berawalan `=` dianggap nama perintah.

## Prinsip (dari `/quiz`)

- **Grammar hanya dari `lessons/unit-XX.md` yang sudah ditulis**; tag hanya dari
  `reference/quiz-taxonomy.md`; kosakata ≤ level aktif +1 (`oxford-vocabulary.md`).
- **Bias LUNAK** ke kata lemah Anki (anchor `progress/anki-weak-items.md`) sebagai kata isi.
- **Jangan mengarang skor** — hitung eksplisit dari angka lama + hasil sesi.
- Soal (kalimat sumber) dalam **Bahasa Indonesia**, kunci dalam **English**; instruksi,
  pembahasan, dan hasil dalam **Bahasa Indonesia yang mudah dipahami**.

## Parsing argumen

`/quiz-t [unit X | unit X-Y] [N]` — tanpa argumen → adaptif, **default 4 soal**; `unit X[-Y]` →
batasi unit; `N` → override jumlah soal sesi itu.

## Langkah

1. **Satu** perintah muat state:
   `cat .claude/skills/quiz/ref/translate.md progress/evaluation.md; head -25 progress/anki-weak-items.md; ls lessons/`
2. **Pilih tag sasaran:** tag grammar 🔴/🟡 dulu (Weak areas `evaluation.md`), lalu ⚪, lalu unit
   terbaru. Tentukan **level bantuan** per tag (tabel di `translate.md`).
3. Bila perlu detail poin grammar / kosakata: **satu** perintah, mis.
   `head -25 lessons/unit-01.md; grep -n "<tag1>\|<tag2>" reference/quiz-taxonomy.md; grep -n -i "<kata1>\|<kata2>" reference/oxford-vocabulary.md`.
4. Susun & sajikan soal persis `translate.md`: 1 soal/panel AskUserQuestion, input via Other, 2 opsi
   bantu (💡 petunjuk / ⏭️ lewati), **waktu dikunci di prompt** (Bahasa Indonesia tak punya tense),
   🎯 tujuan, kosakata bantu bentuk dasar, 1 titik uji/soal. Kumpulkan **semua** jawaban dulu.
5. **Nilai** per titik uji (toleransi variasi sah, slip di luar titik uji = catatan) → **rekam**
   seperti `/quiz` langkah 6:
   - `progress/evaluation.md`: per tag (atribusi: benar → semua tag sasaran; salah → hanya tag
     yang gagal), per error type, per unit, `SK-writing`, Weak areas, baris "Updated".
   - `progress/history.md`: baris paling atas, Scope **`QUIZ [translate] (<cakupan>)`**.
6. **Pesan akhir RINGKAS:** skor 1 baris · tabel soal SALAH saja (`# · tag · jawabanmu · kunci`) ·
   1 baris fix per soal salah + slip di luar titik uji sebagai catatan · 1 baris area terlemah /
   perubahan status · tawarkan pembahasan lebih dalam bila user mau.
