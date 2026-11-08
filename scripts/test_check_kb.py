#!/usr/bin/env python3
"""Tes untuk scripts/check-kb.py (stdlib saja, tanpa pytest).
Jalankan: python3 scripts/test_check_kb.py
Cara menulis tes: .claude/skills/writing-good-tests/SKILL.md
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("check_kb", HERE / "check-kb.py")
ck = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ck)

# --- Fixture bernama -------------------------------------------------------

HEADER = """## Per grammar tag (MCQ vs production, last 10)
| Tag | MCQ last 10 | Prod last 10 | All-time (MCQ · Prod · total) | Status |
|-----|-------------|--------------|-------------------------------|--------|
{grammar}

## Per skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
{skill}

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-x` | 4 | 5 | 80% | 🟢 |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 4 | 5 | 80% | 🟢 |
"""

GOOD_GRAMMAR = ("| `A2-x` | `✓✓✓✓✗` 4/5 (80%) 🟢 | `✓✓✓✗✓` 4/5 (80%) 🟢 "
                "| 4/5 · 4/5 · 8/10 (80%) | 🟢 (catatan) |")
GOOD_SKILL = "| `SK-vocab` | 13 | 13 | 100% | 🟢 |"


def _eval(grammar=GOOD_GRAMMAR, skill=GOOD_SKILL):
    return HEADER.format(grammar=grammar, skill=skill)


def _errors(**kw):
    errs, _ = ck.check_text(_eval(**kw))
    return errs


# --- pct & status_of: ambang --------------------------------------------------

def test_pct_rounds_half_up():
    assert ck.pct(1, 8) == 13     # 12.5 → 13 (bukan banker's rounding 12)
    assert ck.pct(3, 8) == 38     # 37.5 → 38


def test_pct_zero_total_is_zero():
    assert ck.pct(0, 0) == 0


def test_status_below_three_attempts_is_grey():
    assert ck.status_of(2, 2) == "⚪"


def test_status_thresholds_at_boundaries():
    assert ck.status_of(5, 9) == "🔴"    # 55.6%
    assert ck.status_of(6, 10) == "🟡"   # 60% = batas bawah 🟡
    assert ck.status_of(8, 10) == "🟢"   # 80% = batas 🟢


def test_status_uses_raw_percent_not_rounded():
    # 79.5% dibulatkan jadi 80%, tapi belum mencapai ambang 🟢
    assert ck.status_of(159, 200) == "🟡"


# --- tag_status: aturan dua jalur ------------------------------------------------

def test_tag_green_only_when_both_lanes_green():
    assert ck.tag_status("🟢", "🟢") == "🟢"


def test_tag_takes_worst_lane():
    assert ck.tag_status("🟢", "🟡") == "🟡"
    assert ck.tag_status("🟡", "🔴") == "🔴"


def test_tag_green_plus_grey_is_yellow():
    assert ck.tag_status("🟢", "⚪") == "🟡"


def test_tag_red_plus_grey_stays_red():
    assert ck.tag_status("⚪", "🔴") == "🔴"


def test_tag_both_grey_is_grey():
    assert ck.tag_status("⚪", "⚪") == "⚪"


# --- check_text: tracker yang benar -------------------------------------------

def test_consistent_tracker_has_no_errors():
    errs, n_rows = ck.check_text(_eval())
    assert n_rows == 4           # prakondisi: baris benar-benar terbaca
    assert errs == []


def test_lane_without_data_written_as_grey_is_accepted():
    row = "| `A2-x` | — ⚪ | — ⚪ | 0/0 · 0/0 · 0/0 (0%) | ⚪ |"
    assert _errors(grammar=row) == []


# --- check_text: tiap jenis kesalahan terdeteksi ---------------------------------

def test_detects_lane_longer_than_ten():
    row = GOOD_GRAMMAR.replace("`✓✓✓✓✗` 4/5 (80%)", "`✓✓✓✓✓✓✓✓✓✓✓` 11/11 (100%)")
    assert any("maks 10" in e for e in _errors(grammar=row))


def test_detects_count_not_matching_sequence():
    row = GOOD_GRAMMAR.replace("`✓✓✓✓✗` 4/5", "`✓✓✓✓✗` 5/5")
    assert any("urutan berisi 4/5" in e for e in _errors(grammar=row))


def test_detects_wrong_lane_percent():
    row = GOOD_GRAMMAR.replace("4/5 (80%) 🟢 | `✓✓✓✗✓`", "4/5 (75%) 🟢 | `✓✓✓✗✓`")
    assert any("seharusnya 80%" in e for e in _errors(grammar=row))


def test_detects_wrong_lane_status():
    row = GOOD_GRAMMAR.replace("`✓✓✓✗✓` 4/5 (80%) 🟢", "`✓✓✓✗✓` 4/5 (80%) 🟡")
    assert any("Prod: status 🟡, seharusnya 🟢" in e for e in _errors(grammar=row))


def test_detects_alltime_total_not_summing():
    row = GOOD_GRAMMAR.replace("8/10 (80%)", "9/10 (90%)")
    assert any("≠ total" in e for e in _errors(grammar=row))


def test_detects_tag_status_breaking_two_lane_rule():
    row = GOOD_GRAMMAR.replace("| 🟢 (catatan) |", "| 🟡 (catatan) |")
    assert any("Status: 🟡, seharusnya 🟢" in e for e in _errors(grammar=row))


def test_detects_wrong_single_lane_accuracy():
    row = "| `SK-vocab` | 13 | 14 | 100% | 🟢 |"
    assert any("seharusnya 93%" in e for e in _errors(skill=row))


def test_detects_missing_section():
    errs, _ = ck.check_text(_eval().replace("## Per unit", "## Something else"))
    assert any("Per unit" in e for e in errs)


# --- Integrasi: file nyata ----------------------------------------------------------

def test_real_evaluation_md_is_consistent():
    """Tracker nyata harus lolos. Kalau merah: hitungan sesi terakhir salah, atau
    format tabel berubah (perbarui check-kb.py)."""
    text = (HERE.parent / "progress" / "evaluation.md").read_text(encoding="utf-8")
    errs, n_rows = ck.check_text(text)
    assert n_rows > 0, "tidak ada baris yang terbaca"
    assert errs == [], "\n".join(errs)


# --- verb-evaluation.md (/quiz-v) -----------------------------------------------------

VERB_HEADER = """## Per pattern
| Pattern | Correct | Total | Accuracy | Status |
|---------|---------|-------|----------|--------|
| P4c | 3 | 4 | 75% | 🟡 |

## Per verb (last 5)
| Verb | V2 · V3 | Last 5 | All-time | Status |
|------|---------|--------|----------|--------|
{verb}
"""

GOOD_VERB = "| `wear` | wore · worn | `✗✓✓✓` 3/4 (75%) 🟡 | 3/4 | 🟡 (*weared* 2026-11-02) |"


def _verb_errors(verb=GOOD_VERB):
    errs, _ = ck.check_verb_text(VERB_HEADER.format(verb=verb))
    return errs


def test_verb_consistent_tracker_has_no_errors():
    errs, n_rows = ck.check_verb_text(VERB_HEADER.format(verb=GOOD_VERB))
    assert n_rows == 2           # prakondisi: 1 pola + 1 kata terbaca
    assert errs == []


def test_verb_placeholder_row_is_skipped():
    assert _verb_errors(verb="| _(none yet)_ | | | | |") == []


def test_verb_detects_window_longer_than_five():
    row = GOOD_VERB.replace("`✗✓✓✓` 3/4 (75%) 🟡 | 3/4", "`✗✓✓✓✓✓` 5/6 (83%) 🟢 | 5/6")
    assert any("maks 5" in e for e in _verb_errors(verb=row))


def test_verb_detects_wrong_status():
    row = GOOD_VERB.replace("| 🟡 (*weared*", "| 🟢 (*weared*")
    assert any("Status: 🟢, seharusnya 🟡" in e for e in _verb_errors(verb=row))


def test_verb_detects_alltime_smaller_than_window():
    row = GOOD_VERB.replace("| 3/4 |", "| 2/3 |")
    assert any("lebih kecil dari isi urutan" in e for e in _verb_errors(verb=row))


def test_check_any_routes_verb_tracker_to_verb_checker():
    errs, n_rows = ck.check_any(VERB_HEADER.format(verb=GOOD_VERB))
    assert (errs, n_rows) == ([], 2)


def test_real_verb_evaluation_md_is_consistent():
    path = HERE.parent / "progress" / "verb-evaluation.md"
    errs, n_rows = ck.check_verb_text(path.read_text(encoding="utf-8"))
    assert n_rows > 0, "tidak ada baris yang terbaca"
    assert errs == [], "\n".join(errs)


# --- toefl-evaluation.md (/toefl) ----------------------------------------------------

TOEFL_HEADER = """## Section level (adaptive between sessions)
| Section | Level | Sessions at this level | Note |
|---------|-------|------------------------|------|
| Reading | {level} | 80% | |

## Reading / Listening / Build a Sentence (correct/incorrect)
| Subtype | Tag | Correct | Total | Accuracy | Status |
|---------|-----|---------|-------|----------|--------|
{single}

## Writing / Speaking (rubric 0–5)
| Subtype | Tag | Avg score | Attempts | Status |
|---------|-----|-----------|----------|--------|
{rubric}
"""

GOOD_TOEFL_SINGLE = "| RD-academic | Read an Academic Passage | 2 | 3 | 67% | 🟡 |"
GOOD_TOEFL_RUBRIC = "| WR-email | Write an Email | 3.5 | 4 | 🟡 |"


def _toefl(level="B1", single=GOOD_TOEFL_SINGLE, rubric=GOOD_TOEFL_RUBRIC):
    return TOEFL_HEADER.format(level=level, single=single, rubric=rubric)


def _toefl_errors(**kw):
    errs, _ = ck.check_toefl_text(_toefl(**kw))
    return errs


def test_toefl_consistent_tracker_has_no_errors():
    errs, n_rows = ck.check_toefl_text(_toefl())
    assert n_rows == 3           # prakondisi: level + 1 subtype + 1 rubrik terbaca
    assert errs == []


def test_toefl_placeholder_rows_are_skipped():
    errs, n_rows = ck.check_toefl_text(
        _toefl(single="| _(empty)_ | | | | | |", rubric="| _(empty)_ | | | | |"))
    assert (errs, n_rows) == ([], 1)


def test_toefl_detects_wrong_accuracy_with_task_name_column():
    row = GOOD_TOEFL_SINGLE.replace("67%", "70%")
    assert any("seharusnya 67%" in e for e in _toefl_errors(single=row))


def test_toefl_detects_wrong_subtype_status():
    row = GOOD_TOEFL_SINGLE.replace("🟡", "🟢")
    assert any("status 🟢, seharusnya 🟡" in e for e in _toefl_errors(single=row))


def test_toefl_rubric_status_boundaries():
    assert ck.rubric_status(5.0, 2) == "⚪"   # < 3 attempts
    assert ck.rubric_status(2.9, 3) == "🔴"
    assert ck.rubric_status(3.0, 3) == "🟡"   # 3 = batas bawah 🟡
    assert ck.rubric_status(4.0, 3) == "🟢"   # 4 = batas 🟢


def test_toefl_detects_wrong_rubric_status():
    row = GOOD_TOEFL_RUBRIC.replace("| 🟡 |", "| 🟢 |")
    assert any("status 🟢, seharusnya 🟡" in e for e in _toefl_errors(rubric=row))


def test_toefl_detects_rubric_avg_above_five():
    row = GOOD_TOEFL_RUBRIC.replace("3.5", "5.5")
    assert any("di luar 0–5" in e for e in _toefl_errors(rubric=row))


def test_toefl_detects_unknown_level():
    assert any("bukan salah satu" in e for e in _toefl_errors(level="B3"))


def test_toefl_detects_missing_level_section():
    errs, _ = ck.check_toefl_text(_toefl().replace("## Section level", "## Something"))
    assert any("Section level" in e for e in errs)


def test_check_any_routes_toefl_tracker_to_toefl_checker():
    errs, n_rows = ck.check_any(_toefl())
    assert (errs, n_rows) == ([], 3)


def test_real_toefl_evaluation_md_is_consistent():
    path = HERE.parent / "progress" / "toefl-evaluation.md"
    errs, n_rows = ck.check_toefl_text(path.read_text(encoding="utf-8"))
    assert n_rows > 0, "tidak ada baris yang terbaca"
    assert errs == [], "\n".join(errs)


# --- Runner ---------------------------------------------------------------------------

def run():
    """Jalankan SEMUA test_* (urut alfabetis), kumpulkan semua kegagalan, lapor di akhir."""
    import traceback
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failures = []
    for t in tests:
        try:
            t()
            print(f"  ok    {t.__name__}")
        except Exception:  # noqa: BLE001 — runner harus menangkap semua
            print(f"  FAIL  {t.__name__}")
            failures.append((t.__name__, traceback.format_exc()))
    if failures:
        print(f"\n❌ {len(failures)}/{len(tests)} test GAGAL:")
        for name, tb in failures:
            print(f"\n─── {name} ───\n{tb.rstrip()}")
        return len(failures)
    print(f"\n✅ {len(tests)} test lulus")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(1 if run() else 0)
