#!/usr/bin/env python3
"""
check-kb.py — cek konsistensi hitungan di tracker progress/.

Yang dicek (aturan dari .claude/skills/quiz/SKILL.md langkah 6 & docs/cara-kerja.md):
  1. Tabel "Per grammar tag" (dua jalur MCQ & Prod):
     - urutan ✓✗ tiap jalur maksimal 10;
     - angka n/m cocok dengan jumlah ✓ dan panjang urutan;
     - persen = round(n/m) (dibulatkan ke atas di .5);
     - status jalur sesuai ambang (< 3 ⚪ · < 60% 🔴 · 60–79% 🟡 · ≥ 80% 🟢);
     - All-time: MCQ + Prod = total, persen total benar;
     - status tag mengikuti aturan dua jalur.
  2. Tabel skill / error / unit (satu jalur): Accuracy = Correct/Total dan statusnya.
  progress/verb-evaluation.md (/quiz-v, .claude/skills/quiz-v/SKILL.md langkah 6):
  3. Tabel "Per verb": urutan ✓✗ maksimal 5, n/m, persen, status; All-time c/t masuk akal.
  4. Tabel "Per pattern" (satu jalur): sama seperti nomor 2.

Tidak mengubah file apa pun. Exit 0 = semua cocok, exit 1 = ada yang tidak cocok.
Pakai:  python3 scripts/check-kb.py            (cek kedua tracker)
        python3 scripts/check-kb.py <file.md>  (jenis tracker dikenali dari isinya)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULTS = (ROOT / "progress" / "evaluation.md", ROOT / "progress" / "verb-evaluation.md")
VERB_WINDOW = 5  # /quiz-v: 5 percobaan terakhir per kata

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


def check_lane(tag, name, cell, errs, max_len=10):
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
    if size > max_len:
        errs.append(f"{tag} {name}: urutan {size} item (maks {max_len})")
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


ALLTIME_SINGLE_RE = re.compile(r"(\d+)/(\d+)")


def check_verb_text(text):
    """Logika murni: isi verb-evaluation.md → (daftar masalah, jumlah baris dicek)."""
    secs = sections(text)
    errs, n_rows = [], 0

    if "Per pattern" in secs:
        check_single("Per pattern", secs["Per pattern"], errs)
        n_rows += len(secs["Per pattern"])
    else:
        errs.append("Bagian '## Per pattern' tidak ditemukan")

    verb = [k for k in secs if k.startswith("Per verb")]
    if not verb:
        errs.append("Bagian '## Per verb' tidak ditemukan")
    for k in verb:
        for line in secs[k]:
            c = cells(line)
            if len(c) < 5 or c[0].startswith("_"):
                continue  # baris placeholder _(none yet)_
            n_rows += 1
            name = c[0].strip("`")
            lane = check_lane(name, "Last 5", c[2], errs, max_len=VERB_WINDOW)
            m = LANE_RE.search(c[2])
            a = ALLTIME_SINGLE_RE.search(c[3])
            if not a:
                errs.append(f"{name} All-time: format tidak terbaca: {c[3]!r}")
            elif m:
                at_c, at_t = int(a.group(1)), int(a.group(2))
                seq = m.group(1)
                if at_c > at_t:
                    errs.append(f"{name} All-time: benar {at_c} > total {at_t}")
                if len(seq) > at_t or seq.count("✓") > at_c:
                    errs.append(f"{name} All-time {at_c}/{at_t} lebih kecil dari isi urutan "
                                f"{seq.count('✓')}/{len(seq)}")
            if lane and first_status(c[4]) != lane:
                errs.append(f"{name} Status: {first_status(c[4])}, seharusnya {lane}")
    return errs, n_rows


def check_any(text):
    """Pilih pemeriksa dari isi file."""
    return check_verb_text(text) if "## Per verb" in text else check_text(text)


def main():
    paths = [Path(a) for a in sys.argv[1:]] or [p for p in DEFAULTS if p.exists()]
    failed = False
    for path in paths:
        errs, n_rows = check_any(path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        if errs:
            failed = True
            print(f"❌ {rel}: {len(errs)} masalah")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"✅ {rel}: {n_rows} baris dicek, semua hitungan cocok")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
