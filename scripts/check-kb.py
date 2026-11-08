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
  progress/toefl-evaluation.md (/toefl, .claude/skills/toefl/SKILL.md langkah 5):
  5. Tabel "Reading / Listening / Build a Sentence": Accuracy = Correct/Total dan statusnya.
  6. Tabel "Writing / Speaking (rubric 0–5)": Avg 0–5 dan status (< 3 attempts ⚪ · < 3 🔴 ·
     3–3.9 🟡 · ≥ 4 🟢).
  7. Tabel "Section level": level hanya A2/B1/B2/C1.
  progress/history.md (/toefl langkah 5, rotasi tema scripts/toefl_themes.py):
  8. Tiap baris TOEFL punya `Tema:` berformat `SUBTYPE=id (topik) · …`, dan tiap id ada di pool
     kanonik reference/toefl-themes.md untuk subtype itu.

Tidak mengubah file apa pun. Exit 0 = semua cocok, exit 1 = ada yang tidak cocok.
Pakai:  python3 scripts/check-kb.py            (cek ketiga tracker + tema TOEFL di history)
        python3 scripts/check-kb.py <file.md>  (jenis tracker dikenali dari isinya)
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import toefl_themes  # noqa: E402 — parser tema dipakai bersama dengan scripts/toefl_themes.py

ROOT = Path(__file__).resolve().parent.parent
DEFAULTS = (ROOT / "progress" / "evaluation.md", ROOT / "progress" / "verb-evaluation.md",
            ROOT / "progress" / "toefl-evaluation.md", ROOT / "progress" / "history.md")
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


def check_single(section, rows, errs, skip=0):
    """Tabel satu jalur: Tag | (kolom tambahan × skip) | Correct | Total | Accuracy | Status."""
    for line in rows:
        c = cells(line)
        tag = c[0].strip("`")
        c = c[:1] + c[1 + skip:]
        if len(c) < 5 or not c[1].isdigit() or not c[2].isdigit():
            continue  # baris placeholder
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


def rubric_status(avg, attempts):
    """/toefl rubrik 0–5: < 3 attempts ⚪ · avg < 3 🔴 · 3–3.9 🟡 · ≥ 4 🟢."""
    if attempts < 3:
        return "⚪"
    if avg < 3:
        return "🔴"
    if avg < 4:
        return "🟡"
    return "🟢"


TOEFL_SINGLE = "Reading / Listening / Build a Sentence"
TOEFL_RUBRIC = "Writing / Speaking"
TOEFL_LEVEL = "Section level"
LEVELS = ("A2", "B1", "B2", "C1")


def _find(secs, prefix):
    return next((k for k in secs if k.startswith(prefix)), None)


def check_toefl_text(text):
    """Logika murni: isi toefl-evaluation.md → (daftar masalah, jumlah baris dicek)."""
    secs = sections(text)
    errs, n_rows = [], 0

    k = _find(secs, TOEFL_SINGLE)
    if k:
        check_single(k, secs[k], errs, skip=1)
        n_rows += sum(1 for line in secs[k] if not cells(line)[0].startswith("_"))
    else:
        errs.append(f"Bagian '## {TOEFL_SINGLE} …' tidak ditemukan")

    k = _find(secs, TOEFL_RUBRIC)
    if k:
        for line in secs[k]:
            c = cells(line)
            if len(c) < 5 or c[0].startswith("_"):
                continue  # baris placeholder _(empty)_
            n_rows += 1
            tag = c[0].strip("`")
            try:
                avg, att = float(c[2]), int(c[3])
            except ValueError:
                errs.append(f"[{k}] {tag}: Avg/Attempts tidak terbaca: {c[2]!r} / {c[3]!r}")
                continue
            if not 0 <= avg <= 5:
                errs.append(f"[{k}] {tag}: Avg {avg} di luar 0–5")
            want, got = rubric_status(avg, att), first_status(c[4])
            if got != want:
                errs.append(f"[{k}] {tag}: status {got}, seharusnya {want} (avg {avg}, {att}×)")
    else:
        errs.append(f"Bagian '## {TOEFL_RUBRIC} …' tidak ditemukan")

    k = _find(secs, TOEFL_LEVEL)
    if k:
        for line in secs[k]:
            c = cells(line)
            if len(c) < 2:
                continue
            n_rows += 1
            if c[1] not in LEVELS:
                errs.append(f"[{k}] {c[0]}: level {c[1]!r} bukan salah satu {'/'.join(LEVELS)}")
    else:
        errs.append(f"Bagian '## {TOEFL_LEVEL}' tidak ditemukan")
    return errs, n_rows


def check_history_text(text, pool=None):
    """Logika murni: isi history.md → (masalah tema TOEFL, jumlah baris TOEFL dicek)."""
    if pool is None:
        pool = toefl_themes.parse_pool(toefl_themes.POOL_PATH.read_text(encoding="utf-8"))
    errs, rows = [], toefl_themes.toefl_rows(text)
    for d, notes in rows:
        part = toefl_themes.tema_part(notes)
        if not part:
            errs.append(f"[history {d}] TOEFL tanpa 'Tema:'")
            continue
        entries, bad = toefl_themes.parse_tema(part)
        for piece in bad:
            errs.append(f"[history {d}] Tema tidak berformat SUBTYPE=id: {piece!r}")
        for sub, tid in entries:
            if sub not in pool:
                errs.append(f"[history {d}] subtype {sub} tidak punya pool tema")
            elif tid not in pool[sub]:
                errs.append(f"[history {d}] tema {sub}={tid} tidak ada di reference/toefl-themes.md")
    return errs, len(rows)


def check_any(text):
    """Pilih pemeriksa dari isi file."""
    if text.startswith("# Session History"):
        return check_history_text(text)
    if "## Per verb" in text:
        return check_verb_text(text)
    if "## " + TOEFL_SINGLE in text:
        return check_toefl_text(text)
    return check_text(text)


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
