---
name: sync-anki
description: Refresh progress/anki-weak-items.md (kata Oxford 3000 yang sering dilupakan di Anki — lapses, leech, gagal 30 hari) lewat satu script (scripts/sync-anki.sh). Dipakai /quiz & /toefl untuk bias pemilihan kosakata. Tampilkan ringkasan, tawarkan commit. Pakai saat user menjalankan /sync-anki atau minta "update/refresh/sync anki (weak items)".
---

# Skill: /sync-anki — Refresh Item Lemah Anki

Data Anki di-update lewat **satu script**: `scripts/sync-anki.sh`.

| Target | File output | Dipakai | Sumber |
|---|---|---|---|
| `weak` (default) | `progress/anki-weak-items.md` | `/quiz` (kata pengisi soal) · `/toefl` (soal vocab) | `collection.anki2` (Anki desktop) — semua deck bernama `Oxford 3000 <level>` / `Oxford 3000::<level>` (sekarang hanya `Oxford 3000 A1`; A2, B1, … ikut terbaca otomatis) |

Output **AUTO-GENERATED — jangan edit tangan.**

## Argumen

| Perintah | Aksi |
|---|---|
| `/sync-anki` · `/sync-anki weak` | Refresh item lemah (satu-satunya target saat ini) |

## ⚠️ Prasyarat

Script membaca **`collection.anki2` desktop**. Review di **iPhone** baru turun ke desktop
setelah **buka Anki desktop → Sync** (sync dari iPhone saja tidak meng-update file desktop).

**Sebelum menjalankan, tanya dulu:** "Sudah buka Anki desktop & Sync?" Belum → minta Sync dulu,
jangan lanjut. Script mencetak `⚠️` bila collection berumur > 24 jam — sebutkan ke user kalau muncul.

## Langkah eksekusi

1. Konfirmasi prasyarat Sync desktop.
2. Jalankan **satu** perintah:
   ```
   bash scripts/sync-anki.sh
   ```
3. Baca **"Ringkasan /sync-anki"** di akhir output, lalu beri notifikasi singkat:
   - Angka ringkas (mis. `Oxford 3000: 🔴1 🟡3 ⚪19 | A1: 525/929 direview`) + 3–5 kata teratas
     dari anchor.
   - `📝 Berubah` → **✅ Sukses updated**. **Tawarkan commit**:
     `chore(progress): sync Anki — 🔴<a> 🟡<b> ⚪<c>`. Jangan commit tanpa izin.
   - `ℹ️ No data updated` → sudah up-to-date, tak perlu commit.
   - Ada `❌` (exit ≠ 0) → laporkan pesan error **apa adanya**.

## Cara skill lain memakai hasilnya

- `/quiz` & `/toefl` membaca **anchor** file ini saja (baris "Ringkasan cepat").
- **Bias LUNAK**: saat memilih kata pengisi soal untuk grammar/skill yang sedang diuji, utamakan
  kata dari anchor bila cocok secara alami. Bukan pengganti tag lemah di `evaluation.md`, dan
  fallback ke kata lain bila janggal. Tetap pakai level CEFR yang sesuai.
- Item lemah Anki **tidak** dicatat sebagai skor di `evaluation.md` (tracker itu per
  grammar/skill, bukan per kata).

## Tingkat

🔴 = `leech` atau `lapses ≥ 8` · 🟡 = `lapses 5–7` · ⚪ = `lapses 3–4`. Selama 🔴 < 5 (deck masih
muda), anchor diisi 10 kata teratas (🟡/⚪ ikut). Anchor otomatis menyempit ke 🔴 saja begitu 🔴 ≥ 5.

## Catatan

- Error umum: `collection.anki2` tak ketemu → sarankan
  `ANKI_COLLECTION=/path/collection.anki2 bash scripts/sync-anki.sh`. **Jangan** karang datanya.
- Deck tak ketemu → nama deck di Anki harus memuat `Oxford 3000` + level (`A1`, `A2`, …).
- Script hanya **membaca** salinan collection (aman walau Anki sedang terbuka).
