# Cara Kerja Knowledge Base — Flow & Logika

> Penjelasan **untuk manusia**: bagaimana KB ini bekerja dari ujung ke ujung. Diagram pakai
> Mermaid (otomatis ter-render di Obsidian). Detail teknis tetap di `CLAUDE.md` &
> `.claude/skills/*/SKILL.md`; dokumen ini peta besarnya.

## Ringkasan satu paragraf

KB ini membantu belajar English menuju **TOEFL iBT** untuk S2 di Institute of Science Tokyo,
dengan latihan **active recall** yang **adaptif** ke titik lemah. Alurnya: `/diagnostic`
menentukan level CEFR awal → Claude menulis **unit** materi di `lessons/` (source of truth) →
kamu membaca unit di Obsidian → tiap hari latihan lewat `/quiz` / `/quiz-t` → hasilnya **dicatat
balik** ke peta kelemahan → sesi berikutnya **otomatis condong** ke yang lemah. Anki (Oxford 3000)
menyumbang **sinyal kata yang sering kamu lupa**, dan `/toefl` mengukur kesiapan ujian dengan
format resmi TOEFL 2026.

> Proyek **sekunder** (fokus utama = Jepang) → semua dirancang **ringan**: sesi pendek, tanpa
> target padat.

## Tujuan

- 🎯 **Lancar berbahasa Inggris** (sehari-hari & akademik).
- 🎯 **Skor TOEFL iBT resmi** sesuai syarat program tujuan (patokan umum B2 = band 4–4.5).

## Peta komponen (siapa memegang apa)

| Komponen | Isi | Siapa menulis |
|---|---|---|
| `lessons/unit-XX.md` | materi per unit (grammar, vocab, reading, frasa, TOEFL link) — **source of truth** | Claude |
| `reference/` | pool vocab (Oxford/AWL), taxonomy tag, spec & rubrik TOEFL, indeks sumber resmi | Claude |
| `reference/sources/` | PDF resmi (Oxford, Core Inventory, ETS, …) — gitignored | unduhan |
| `progress/diagnostic.md` | level CEFR aktif | `/diagnostic` |
| `progress/evaluation.md` | kelemahan per **grammar/skill tag** | `/quiz`, `/quiz-t` |
| `progress/toefl-evaluation.md` | kelemahan per **task TOEFL** | `/toefl` |
| `progress/anki-weak-items.md` | kata Oxford yang sering dilupakan (AUTO-GENERATED) | `/sync-anki` |
| `progress/history.md` | log semua sesi (label `DIAG` / `QUIZ` / `TOEFL`) | semua skill |
| `docs/perbaikan-kb.md` | log perbaikan aturan/skill (Problem → Fix) | Claude |

## Gambaran besar

```mermaid
flowchart LR
    D["/diagnostic<br/>level CEFR"] --> U["Claude menulis unit<br/>lessons/unit-XX.md"]
    U --> R["Kamu membaca unit<br/>(Obsidian)"]
    A["Anki<br/>Oxford 3000"] --> S["/sync-anki"]
    S --> W[("anki-weak-items.md")]
    R --> Q["/quiz · /quiz-t"]
    W -. bias lunak .-> Q
    Q --> E[("evaluation.md")]
    E -. bobot adaptif .-> Q
    E -- "semua tag unit 🟢" --> U
    T["/toefl"] --> TE[("toefl-evaluation.md")]
    E -. read-only .-> T
    W -. bias lunak .-> T
```

## Alur 1 — Placement `/diagnostic` (sekali di awal, boleh diulang)

```mermaid
flowchart TD
    A["16 soal: grammar A1→B2,<br/>vocab, reading, 1 writing"] --> B["Tanpa hint<br/>(ukur jujur)"]
    B --> C["Estimasi level CEFR"]
    C --> D[("diagnostic.md")]
    C --> E[("seed evaluation.md<br/>+ Weak areas")]
    E --> F["Dasar memilih unit pertama"]
```

Hasil 2026-08-23: **A2** (vocab & reading B1–B2 kuat; grammar = fokus).

## Alur 2 — Latihan harian `/quiz` (loop adaptif = jantung sistem)

```mermaid
flowchart TD
    S["Muat state: evaluation.md, taxonomy,<br/>anchor unit, anchor Anki"] --> B["Bobot: 🔴 ±3 soal · 🟡 ±2 ·<br/>⚪ 1–2 · 🟢 0–1"]
    B --> G["Buat 12 soal<br/>(grammar, vocab, collocation,<br/>paraphrase, reading)"]
    G --> K{"Gerbang:<br/>hanya 1 opsi benar?"}
    K -- tidak --> G
    K -- ya --> P["Acak posisi kunci<br/>(python random)"]
    P --> X["Mode ujian: jawab semua<br/>(panel ≤4 soal, hint memudar)"]
    X --> N["Nilai + error type"]
    N --> E[("evaluation.md:<br/>lama + sesi = baru")]
    N --> H[("history.md: baris QUIZ")]
    E --> O["Hasil ringkas:<br/>tabel soal salah saja"]
```

## Alur 2b — `/quiz-t` (terjemahan produksi Indonesia → English)

Sama dengan `/quiz translate`. Bedanya: kamu **mengetik** kalimat English sendiri (bukan klik),
4 soal, 1 soal per panel.

```mermaid
flowchart TD
    A["Pilih tag sasaran 🔴/🟡 → ⚪ → unit terbaru"] --> B["Prompt Indonesia + konteks<br/>+ WAKTU dikunci + 🎯 Tujuan"]
    B --> C["Kosakata bantu bentuk dasar<br/>(berkurang saat tag 🟢)"]
    C --> D["Kamu ketik jawaban<br/>(💡 petunjuk / ⏭️ lewati)"]
    D --> E["Nilai per TITIK UJI<br/>(slip di luar titik uji = catatan)"]
    E --> F[("evaluation.md +<br/>history.md: QUIZ [translate]")]
```

Kenapa waktu wajib dikunci: Bahasa Indonesia tidak punya tense — *"Saya tinggal di Bandung"* bisa
*I live / I lived / I have lived*.

## Alur 3 — Mock ujian `/toefl` (jalur terpisah)

```mermaid
flowchart TD
    A["Spec resmi TOEFL 2026<br/>(toefl-2026-spec.md)"] --> B{"Mode"}
    B -- "harian ±25 mnt" --> C["Reading + Listening (transkrip)<br/>+ Build a Sentence"]
    B -- "writing / speaking" --> D["Email · Academic Discussion ·<br/>Interview (diketik)"]
    B -- "full ±90 mnt" --> E["4 section, Reading/Listening<br/>2 modul adaptif"]
    C --> F["Nilai: MCQ benar/salah ·<br/>free-text rubrik 0–5"]
    D --> F
    E --> F
    F --> G[("toefl-evaluation.md")]
    F --> H[("history.md: baris TOEFL")]
    F -. "TIDAK menyentuh" .-x I[("evaluation.md")]
```

- Persentase di sini **≠ band resmi 1–6** (ujian asli adaptif & dinilai ETS).
- Listening via transkrip → cenderung lebih mudah dari aslinya. *Listen and Repeat* di luar cakupan.

## Alur 4 — Sinyal Anki `/sync-anki`

```mermaid
flowchart LR
    A["Review di iPhone"] --> B["Buka Anki desktop → Sync"]
    B --> C["scripts/sync-anki.sh<br/>(baca salinan collection.anki2)"]
    C --> D["Tier per kata:<br/>🔴 leech / lapses ≥8 · 🟡 5–7 · ⚪ 3–4"]
    D --> E[("anki-weak-items.md<br/>anchor = kata prioritas")]
    E -. "dipakai sebagai kata<br/>pengisi kalimat" .-> F["/quiz · /quiz-t · /toefl"]
```

Anki memilih **kata**, bukan grammar. Kata lemah diselipkan ke soal bila cocok secara alami —
bukan drill arti kata (itu tugas Anki).

## Logika inti: DUA sinyal kelemahan

```mermaid
flowchart LR
    A[("evaluation.md<br/>lemah per GRAMMAR/SKILL")] --> C["Soal yang menguji grammar lemah"]
    B[("anki-weak-items.md<br/>lemah per KATA")] --> D["...dengan kata yang sering dilupakan"]
    C --> E["1 soal = latihan dua kelemahan sekaligus"]
    D --> E
```

## Cara skor & status dihitung (tanpa engine)

Proyek Jepang punya engine `kb.py`; di sini **Claude menghitung eksplisit** dari angka lama +
hasil sesi (tidak boleh mengarang angka).

| Tracker | Rumus | Status |
|---|---|---|
| `evaluation.md` (per tag / error / unit) | Correct += benar, Total += soal; Accuracy = Correct/Total | Total < 3 ⚪ · < 60% 🔴 · 60–79% 🟡 · ≥ 80% 🟢 |
| `toefl-evaluation.md` MCQ & build | sama seperti di atas, per task | sama |
| `toefl-evaluation.md` rubrik | Avg baru = (avg lama × n lama + skor sesi) ÷ n baru | n < 3 ⚪ · < 3 🔴 · 3–3.9 🟡 · ≥ 4 🟢 |

**Hint fading:** hint di opsi jawaban mengikuti status tag — 🔴/🟡/⚪ hint penuh → mendekati 🟢
hint netral → 🟢 tanpa hint (gaya ujian).

## Siklus belajar & ritme yang disarankan

| Kapan | Aktivitas |
|---|---|
| Setiap hari | Anki → (`/sync-anki` bila ada review) → `/quiz` atau `/quiz-t` |
| 1× seminggu | `/toefl` (harian, atau bergantian `writing` / `speaking`) |
| Semua tag satu unit 🟢 | minta Claude menulis unit berikutnya (roadmap di `README.md`) |
| Sesekali (mis. tiap 2–3 bulan) | ulang `/diagnostic` untuk cek kenaikan level |

## Aturan main (selalu berlaku)

- Grammar hanya dari unit yang sudah ditulis; tag hanya dari `reference/quiz-taxonomy.md`.
- Level kata & grammar dicek ke referensi resmi (`reference/official-sources.md`).
- Mode ujian: jawab semua dulu, koreksi di akhir.
- Mengedit unit: jangan buang materi, laporkan tiap perubahan.
- Tiap perbaikan aturan/skill → 1 entri di `docs/perbaikan-kb.md`.

## Glosarium singkat

| Istilah | Arti |
|---|---|
| **CEFR** | skala level bahasa Eropa A1 (pemula) → C2 (mahir) |
| **Anchor** | ringkasan ±20 baris di awal file yang cukup dibaca skill (hemat token) |
| **Tag** | label poin yang diuji (mis. `A2-present-simple`, `RD-academic`) |
| **Lapses** | berapa kali kartu Anki "lupa" (ditekan Again setelah sempat hafal) |
| **Leech 🩸** | kartu Anki yang terlalu sering dilupakan (ditandai otomatis oleh Anki) |
| **Band** | skor TOEFL 2026 per section 1–6 (kenaikan 0,5) |
| **Titik uji** | satu poin grammar yang dinilai dalam soal produksi (`/quiz-t`) |
