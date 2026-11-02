#!/usr/bin/env python3
"""
check-kb.py — cek konsistensi hitungan di progress/evaluation.md.

Yang dicek (aturan dari .claude/skills/quiz/SKILL.md langkah 6 & docs/cara-kerja.md):
  1. Tabel "Per grammar tag" (dua jalur MCQ & Prod):
     - urutan ✓✗ tiap jalur maksimal 10;
     - angka n/m cocok dengan jumlah ✓ dan panjang urutan;
     - persen = round(n/m) (dibulatkan ke atas di .5);
     - status jalur sesuai ambang (< 3 ⚪ · < 60% 🔴 · 60–79% 🟡 · ≥ 80% 🟢);
     - All-time: MCQ + Prod = total, persen total benar;
     - status tag mengikuti aturan dua jalur.
  2. Tabel skill / error / unit (satu jalur): Accuracy = Correct/Total dan statusnya.

Tidak mengubah file apa pun. Exit 0 = semua cocok, exit 1 = ada yang tidak cocok.
Pakai:  python3 scripts/check-kb.py [path/ke/evaluation.md]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / "progress" / "evaluation.md"

STATUS = ("⚪", "🔴", "🟡", "🟢")
WORST_ORDER = {"🔴": 0, "🟡": 1, "🟢": 2}


def pct(c, t):
    """Persen dibulatkan, .5 ke atas (bukan banker's rounding)."""
    return int(c * 100 / t + 0.5) if t else 0


def status_of(c, t):
    if t < 3:
        return "⚪"
    p = c * 100 / t  # ambang pakai nilai asli, bukan yang dibulatkan
    if p < 60:
        return "🔴"
    if p < 80:
        return "🟡"
    return "🟢"


def first_status(text):
    hits = [(text.find(s), s) for s in STATUS if s in text]
    return min(hits)[1] if hits else None


def tag_status(mcq, prod):
    """Aturan dua jalur. mcq/prod = status jalur (⚪/🔴/🟡/🟢)."""
    if mcq == "🟢" and prod == "🟢":
        return "🟢"
    data = [s for s in (mcq, prod) if s != "⚪"]
    if not data:
        return "⚪"
    if data == ["🟢"]:  # satu jalur 🟢, jalur lain ⚪ → belum terbukti
        return "🟡"
    return min(data, key=WORST_ORDER.get)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def sections(text):
    """{judul '## ...': [baris tabel data]}"""
    out, cur = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            out[cur] = []
        elif cur and line.startswith("|") and not re.match(r"^\|\s*-", line):
            out[cur].append(line)
    for k in out:
        out[k] = out[k][1:]  # buang header
    return out


LANE_RE = re.compile(r"`([✓✗]*)`\s*(\d+)/(\d+)\s*\((\d+)%\)\s*(⚪|🔴|🟡|🟢)")
ALLTIME_RE = re.compile(r"(\d+)/(\d+)\s*·\s*(\d+)/(\d+)\s*·\s*(\d+)/(\d+)\s*\((\d+)%\)")


def check_lane(tag, name, cell, errs):
    m = LANE_RE.search(cell)
    if not m:
        # jalur tanpa data boleh ditulis tanpa urutan, asal statusnya ⚪
        st = first_status(cell)
        if st != "⚪":
            errs.append(f"{tag} {name}: format jalur tidak terbaca: {cell!r}")
            return None
        return "⚪"
    seq, n, m_, p, st = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)
    ok_n, size = seq.count("✓"), len(seq)
    if size > 10:
        errs.append(f"{tag} {name}: urutan {size} item (maks 10)")
    if n != ok_n or m_ != size:
        errs.append(f"{tag} {name}: tertulis {n}/{m_}, urutan berisi {ok_n}/{size}")
    if p != pct(ok_n, size):
        errs.append(f"{tag} {name}: tertulis {p}%, seharusnya {pct(ok_n, size)}%")
    want = status_of(ok_n, size)
    if st != want:
        errs.append(f"{tag} {name}: status {st}, seharusnya {want} ({ok_n}/{size})")
    return want


def check_grammar(rows, errs):
    for line in rows:
        c = cells(line)
        if len(c) < 5:
            continue
        tag = c[0].strip("`")
        mcq = check_lane(tag, "MCQ", c[1], errs)
        prod = check_lane(tag, "Prod", c[2], errs)

        a = ALLTIME_RE.search(c[3])
        if not a:
            errs.append(f"{tag} All-time: format tidak terbaca: {c[3]!r}")
        else:
            mc, mt, pc, pt, tc, tt, tp = map(int, a.groups())
            if (mc + pc, mt + pt) != (tc, tt):
                errs.append(f"{tag} All-time: {mc}/{mt} + {pc}/{pt} ≠ total {tc}/{tt}")
            if tp != pct(tc, tt):
                errs.append(f"{tag} All-time: tertulis {tp}%, seharusnya {pct(tc, tt)}%")
            if mc > mt or pc > pt:
                errs.append(f"{tag} All-time: benar lebih besar dari total")

        if mcq and prod:
            want = tag_status(mcq, prod)
            got = first_status(c[4])
            if got != want:
                errs.append(f"{tag} Status: {got}, seharusnya {want} (MCQ {mcq} · Prod {prod})")


def check_single(section, rows, errs):
    for line in rows:
        c = cells(line)
        if len(c) < 5 or not c[1].isdigit() or not c[2].isdigit():
            continue  # baris placeholder
        tag = c[0].strip("`")
        corr, tot = int(c[1]), int(c[2])
        if corr > tot:
            errs.append(f"[{section}] {tag}: Correct {corr} > Total {tot}")
        pm = re.search(r"(\d+)%", c[3])
        if not pm or int(pm.group(1)) != pct(corr, tot):
            errs.append(f"[{section}] {tag}: Accuracy {c[3]!r}, seharusnya {pct(corr, tot)}%")
        want, got = status_of(corr, tot), first_status(c[4])
        if got != want:
            errs.append(f"[{section}] {tag}: status {got}, seharusnya {want} ({corr}/{tot})")


def check_text(text):
    """Logika murni (tanpa I/O): isi evaluation.md → (daftar masalah, jumlah baris dicek)."""
    secs = sections(text)
    errs = []

    grammar = [k for k in secs if k.startswith("Per grammar tag")]
    if not grammar:
        errs.append("Bagian '## Per grammar tag' tidak ditemukan")
    for k in grammar:
        check_grammar(secs[k], errs)
    n_rows = sum(len(secs[k]) for k in grammar)

    for k in ("Per skill tag", "Per error type", "Per unit"):
        if k in secs:
            check_single(k, secs[k], errs)
            n_rows += len(secs[k])
        else:
            errs.append(f"Bagian '## {k}' tidak ditemukan")
    return errs, n_rows


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    errs, n_rows = check_text(path.read_text(encoding="utf-8"))
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    if errs:
        print(f"❌ {rel}: {len(errs)} masalah")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    print(f"✅ {rel}: {n_rows} baris dicek, semua hitungan cocok")


if __name__ == "__main__":
    main()
