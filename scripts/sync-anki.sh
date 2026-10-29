#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# sync-anki.sh
# Regenerasi progress/anki-weak-items.md dari collection Anki desktop.
#
# Sumber = collection.anki2 (SQLite) milik Anki desktop. Menarik SINYAL KESULITAN
# empiris (lapses + tag `leech` + gagal 30 hari terakhir) untuk deck "Oxford 3000"
# (sekarang "Oxford 3000 A1"; level berikutnya ikut terbaca otomatis, mis.
# "Oxford 3000 A2" atau "Oxford 3000::A2"), lalu menuliskannya sebagai daftar item
# lemah bertingkat. Dipakai /quiz & /toefl untuk memilih kosakata yang benar-benar
# sering dilupakan.
#
# File output = TURUNAN, jangan diedit tangan. Jalankan ulang tiap kali mau refresh.
#
# Pakai:  bash scripts/sync-anki.sh [weak] [path/ke/collection.anki2]
# Env:    ANKI_COLLECTION=... (override lokasi collection)
# ---------------------------------------------------------------------------
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$PROJECT_ROOT/progress/anki-weak-items.md"

# --- Argumen: target (hanya `weak` untuk saat ini) + path collection opsional ---
COL="${ANKI_COLLECTION:-}"
for arg in "$@"; do
  case "$arg" in
    weak|all) ;;
    *.anki2) COL="$arg" ;;
    *) echo "ERROR: target tidak dikenal: $arg (pakai: weak | all)" >&2; exit 1 ;;
  esac
done

# --- Lokasi collection (default macOS; ambil profil pertama yang punya collection) ---
if [ -z "$COL" ]; then
  for c in "$HOME/Library/Application Support/Anki2/"*/collection.anki2; do
    [ -f "$c" ] && COL="$c" && break
  done
fi
if [ -z "${COL:-}" ] || [ ! -f "$COL" ]; then
  echo "❌ weak: collection.anki2 tidak ditemukan." >&2
  echo "   Set ANKI_COLLECTION=... atau beri path .anki2 sebagai argumen." >&2
  exit 1
fi

# --- Umur collection (peringatan bila > 24 jam: mungkin belum Sync) ---
AGE_H=$(( ( $(date +%s) - $(stat -f %m "$COL") ) / 3600 ))
if [ "$AGE_H" -gt 24 ]; then
  echo "⚠️  collection.anki2 terakhir berubah ${AGE_H} jam lalu — sudah buka Anki desktop & Sync?"
fi

# --- Salin dulu (hindari lock kalau Anki terbuka), query read-only ---
TMP="$(mktemp -t anki-col.XXXXXX).anki2"
trap 'rm -f "$TMP" "$TMP.out"' EXIT
cp "$COL" "$TMP"

python3 -I - "$TMP" "$TMP.out" <<'PY'
import datetime, re, sqlite3, sys, time

db, out = sys.argv[1], sys.argv[2]
con = sqlite3.connect(db)
US = chr(31)  # pemisah field Anki (juga pemisah level deck di kolom name)

# Kolom deck name memakai collation `unicase` → cocokkan di Python, bukan di SQL.
decks = []  # (did, level)
for did, name in con.execute("SELECT id, name FROM decks"):
    full = name.replace(US, "::")
    if "Oxford 3000" not in full:
        continue
    m = re.search(r"\b([ABC][12])\b", full)
    if m:
        decks.append((did, m.group(1)))
decks.sort(key=lambda d: d[1])
if not decks:
    sys.exit("❌ weak: deck 'Oxford 3000 <level>' tidak ditemukan di collection.")

CUT_30D = int((time.time() - 30 * 86400) * 1000)  # revlog.id = epoch ms

def clean(s):
    s = re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()
    return re.sub(r"(?<=[a-z])\d+$", "", s)  # "lie1" → "lie" (penanda homonim)

def tier(lapses, leech):
    if leech or lapses >= 8:
        return "🔴"
    if lapses >= 5:
        return "🟡"
    if lapses >= 3:
        return "⚪"
    return None

items, stats = [], {}
for did, level in decks:
    q = """SELECT c.id, n.flds, n.tags, c.lapses, c.type FROM cards c
           JOIN notes n ON n.id = c.nid WHERE c.did = ?"""
    total = seen = 0
    for cid, flds, tags, lapses, ctype in con.execute(q, (did,)):
        total += 1
        seen += ctype != 0
        f = flds.split(US)
        leech = " leech " in f" {tags or ''} "
        t = tier(lapses or 0, leech)
        if not t:
            continue
        fail30 = con.execute(
            "SELECT count(*) FROM revlog WHERE cid = ? AND ease = 1 AND id > ?",
            (cid, CUT_30D)).fetchone()[0]
        items.append((t, lapses or 0, leech, clean(f[0]),
                      clean(f[1]) if len(f) > 1 else "", level, fail30))
    stats[level] = (total, seen)

items.sort(key=lambda r: (-r[1], -r[6], r[3]))

def count(sym):
    return sum(1 for r in items if r[0] == sym)

def mark(leech):
    return " 🩸" if leech else ""

# Deck masih muda (lapses jarang ≥ 8) → selama 🔴 masih < 5, anchor diisi item teratas
# (🟡/⚪, urut lapses) sampai 10 item supaya /quiz tetap punya bias. Otomatis menyempit
# ke 🔴 saja begitu 🔴 ≥ 5.
crit = [r for r in items if r[0] == "🔴"]
fallback = len(crit) < 5
anchor = items[:10] if fallback else crit

today = datetime.date.today().isoformat()
L = []
w = L.append
w("# Item Lemah Anki — Oxford 3000")
w("")
w("> ⚙️ **FILE AUTO-GENERATED — jangan edit tangan.** Regenerasi dari collection Anki desktop")
w("> dengan `bash scripts/sync-anki.sh` (atau `/sync-anki`). Sinyal = `lapses` (berapa kali kartu")
w("> \"gagal\"/lupa) + tag `leech` Anki (🩸 = kartu bermasalah kronis) + gagal 30 hari terakhir.")
w("> Ini **pelengkap** `evaluation.md` (kelemahan per GRAMMAR/SKILL): file ini kelemahan per KATA.")
w("")
w("Dipakai `/quiz` (dan `/toefl` untuk soal vocab) untuk memilih **kata pengisi soal** yang")
w("benar-benar sering dilupakan — **di dalam** grammar/skill yang sedang dilatih. Bukan drill")
w("hafalan arti (itu tugas Anki), tapi memaksa kata sulit ini muncul dalam kalimat.")
w("")
w("Tingkat: **🔴** = `leech` atau `lapses ≥ 8` · **🟡** = `lapses 5–7` · **⚪** = `lapses 3–4`.")
w("**🩸** = bertag `leech`. Kolom **30h** = berapa kali gagal (Again) dalam 30 hari terakhir.")
w("")
w("> Ringkasan cepat (anchor — baca ini saja saat quiz): PRIORITAS TINGGI")
w(">")
w("> **Oxford 3000:** " + (", ".join(
    f"{r[3]}{' ' + r[0] if fallback else ''}{mark(r[2])}" for r in anchor) or "—"))
if fallback:
    w(">")
    w("> _🔴 masih < 5 (deck muda) → anchor sementara = 10 kata teratas (🟡/⚪ ikut); kembali ke 🔴 saja begitu 🔴 ≥ 5._")
w("")
w(f"Total ditandai: 🔴{count('🔴')} · 🟡{count('🟡')} · ⚪{count('⚪')}")
w("")
w("Progres deck: " + " · ".join(
    f"**{lv}** {s}/{t} kartu sudah direview" for lv, (t, s) in stats.items()))
w("")
w("## Kosakata lemah — Oxford 3000")
w("")
w("| | Word | Arti | CEFR | lapses | 30h |")
w("|---|------|------|:----:|:------:|:---:|")
for t, lp, lc, front, back, lv, f30 in items:
    w(f"| {t}{mark(lc)} | {front} | {back} | {lv} | {lp} | {f30} |")
w("")
w("---")
w(f"_Auto-generated {today} oleh `scripts/sync-anki.sh` dari `collection.anki2`._")

open(out, "w").write("\n".join(L) + "\n")
print(f"Oxford 3000: 🔴{count('🔴')} 🟡{count('🟡')} ⚪{count('⚪')}  |  " + "  ".join(
    f"{lv}: {s}/{t} direview" for lv, (t, s) in stats.items()))
PY

# --- Tulis output & laporkan apakah datanya berubah (abaikan baris footer tanggal) ---
strip_footer() { grep -v '^_Auto-generated' "$1" 2>/dev/null || true; }
echo ""
echo "## Ringkasan /sync-anki"
if [ -f "$OUT" ] && [ "$(strip_footer "$OUT")" = "$(strip_footer "$TMP.out")" ]; then
  echo "✅ weak — ℹ️ No data updated (sudah up-to-date)"
else
  cp "$TMP.out" "$OUT"
  echo "✅ weak — 📝 Berubah: progress/anki-weak-items.md"
fi
