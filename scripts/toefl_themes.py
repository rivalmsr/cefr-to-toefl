#!/usr/bin/env python3
"""
toefl_themes.py — pilih tema teks /toefl secara LRU (bukan oleh model).

Pool kanonik  : reference/toefl-themes.md (tabel `Subtype | Tema`).
Riwayat       : semua baris `| TOEFL` di progress/history.md, bagian
                `Tema: RD-words=biologi-hewan (lebah) · RD-daily=fasilitas-olahraga (…) · …`.
Aturan pilih  : per subtype, tema yang BELUM PERNAH dipakai dulu, lalu yang paling lama tidak
                dipakai. Seri (mis. semua belum pernah) diacak dengan seed = tanggal hari ini
                (stabil kalau dijalankan ulang di hari yang sama). Dalam satu sesi tidak ada ID yang sama di dua subtype
                (mis. `geologi` tidak muncul di RD-academic dan LS-talk sekaligus).

Tidak mengubah file apa pun.
Pakai:  python3 scripts/toefl_themes.py [harian|full|reading|listening|writing|speaking]
        (default harian; mode `review` → pakai `full` lalu ambil subtype yang dites saja)
"""
import random
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POOL_PATH = ROOT / "reference" / "toefl-themes.md"
HISTORY_PATH = ROOT / "progress" / "history.md"

# Jumlah TEKS (bukan soal) per subtype per mode — turunan tabel mode di .claude/skills/toefl/SKILL.md.
MODES = {
    "harian": {"RD-words": 1, "RD-daily": 1, "RD-academic": 1,
               "LS-conversation": 1, "LS-announcement": 1, "LS-talk": 1},
    "full": {"RD-words": 2, "RD-daily": 2, "RD-academic": 2,
             "LS-conversation": 2, "LS-announcement": 2, "LS-talk": 2,
             "WR-email": 1, "WR-discussion": 1, "SP-interview": 1},
    "reading": {"RD-words": 1, "RD-daily": 1, "RD-academic": 2},
    "listening": {"LS-conversation": 2, "LS-announcement": 1, "LS-talk": 2},
    "writing": {"WR-email": 1, "WR-discussion": 1},
    "speaking": {"SP-interview": 1},
}

SUBTYPE_RE = re.compile(r"^[A-Z]{2}-[a-z]+$")
ENTRY_RE = re.compile(r"^([A-Z]{2}-[a-z]+)=([a-z0-9]+(?:-[a-z0-9]+)*)(?:\s*\(.*\))?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_pool(text):
    """Isi toefl-themes.md → {subtype: [id, …]} (urutan pool dipertahankan)."""
    pool = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 2:
            continue
        sub = c[0].strip("`")
        if SUBTYPE_RE.match(sub):
            pool[sub] = re.findall(r"`([a-z0-9-]+)`", c[1])
    return pool


def tema_part(notes):
    """Teks setelah 'Tema:' di kolom Notes (tanpa titik penutup), atau None."""
    i = notes.find("Tema:")
    if i < 0:
        return None
    return notes[i + len("Tema:"):].strip().rstrip(".").strip()


def parse_tema(part):
    """'RD-words=geologi (gua) · …' → ([(subtype, id)], [potongan yang tidak terbaca])."""
    entries, bad = [], []
    for piece in (p.strip() for p in part.split("·")):
        if not piece:
            continue
        m = ENTRY_RE.match(piece)
        if m:
            entries.append((m.group(1), m.group(2)))
        else:
            bad.append(piece)
    return entries, bad


def toefl_rows(history_text):
    """Baris TOEFL di history.md → [(tanggal, kolom Notes)]."""
    rows = []
    for line in history_text.splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 5 and DATE_RE.match(c[0]) and c[1].startswith("TOEFL"):
            rows.append((c[0], c[-1]))
    return rows


def last_used(history_text):
    """{(subtype, id): tanggal terakhir dipakai} dari semua baris TOEFL."""
    used = {}
    for date, notes in toefl_rows(history_text):
        part = tema_part(notes)
        if part is None:
            continue
        for key in parse_tema(part)[0]:
            if date > used.get(key, ""):
                used[key] = date
    return used


def pick(pool, used, counts, rng=None):
    """{subtype: n} → {subtype: [(id, tanggal terakhir atau None)]} secara LRU, tanpa ID ganda.
    rng = random.Random untuk mengacak yang seri; None → seri ikut urutan pool (deterministik)."""
    taken, out = set(), {}
    for sub, n in counts.items():
        cands = list(pool.get(sub, []))
        if rng:
            rng.shuffle(cands)
        # ID yang sudah dipakai subtype lain sesi ini paling belakang (cadangan bila pool habis);
        # lalu belum pernah ("" < tanggal apa pun), lalu paling lama; sort stabil → seri tetap
        cands.sort(key=lambda t: (t in taken, used.get((sub, t), "")))
        out[sub] = [(t, used.get((sub, t))) for t in cands[:n]]
        taken.update(t for t, _ in out[sub])
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "harian"
    if mode not in MODES:
        print(f"Mode tidak dikenal: {mode!r}. Pilih: {', '.join(MODES)}")
        sys.exit(2)
    pool = parse_pool(POOL_PATH.read_text(encoding="utf-8"))
    hist = HISTORY_PATH.read_text(encoding="utf-8")
    picks = pick(pool, last_used(hist), MODES[mode], random.Random(date.today().isoformat()))
    print(f"Tema /toefl {mode} (LRU dari {len(toefl_rows(hist))} sesi TOEFL) — pakai persis:")
    for sub, items in picks.items():
        desc = ", ".join(f"{t} ({d or 'belum pernah'})" for t, d in items)
        print(f"  {sub}: {desc}")
    line = " · ".join(f"{sub}={t} (<topik>)" for sub, items in picks.items() for t, _ in items)
    print(f"\nTulis di history:  Tema: {line}.")


if __name__ == "__main__":
    main()
