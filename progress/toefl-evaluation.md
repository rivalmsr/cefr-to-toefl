# TOEFL iBT Mock Evaluation — Per-Subtype Tracker (/toefl)

Updated automatically by the `/toefl` skill after each session. Tracks accuracy **per subtype**
of each section (Reading/Listening MCQ; Speaking/Writing free-text rubric).

> **Separate from `evaluation.md`.** `/toefl` **may read** `evaluation.md` to bias items toward
> weak patterns, but **only writes** this file + a `TOEFL`-labeled row in `history.md`. **Do not
> touch** `evaluation.md`. Real audio (native listening) is out of scope → use a transcript.

**Status thresholds:** <60% 🔴 · 60–79% 🟡 · ≥80% 🟢 (min 3 attempts; below = ⚪).
For Email / Academic Discussion / Interview: track the **average rubric score** (0–5, internal
rubric in `reference/toefl-templates.md`), status: avg <3 🔴 · 3–3.9 🟡 · ≥4 🟢 (min 3 attempts).
Format = **TOEFL iBT 2026** (subtype tags in `reference/quiz-taxonomy.md`).

_Updated 2026-11-08 · sessions: 1._

---

## Section level (adaptive between sessions)
Level of new material per section. Start B1 (Writing build may drop to A2). Rules in
`.claude/skills/toefl/SKILL.md` step 5: **up** one step after **2 sessions in a row ≥ 80%** at
this level · **down** one step after **1 session < 50%** (≥ 3 items) · range A2–C1. A level change
resets the sequence.

| Section | Level | Sessions at this level (%, newest right) | Note |
|---------|-------|------------------------------------------|------|
| Reading | B1 | 80% | 1 more session ≥ 80% → B2 |
| Listening | B1 | 100% | 1 more session ≥ 80% → B2 |
| Writing (build) | A2 | — | dropped B1 → A2 on 2026-11-08 (1/3 = 33%) |

## Reading / Listening / Build a Sentence (correct/incorrect)
| Subtype | Tag | Correct | Total | Accuracy | Status |
|---------|-----|---------|-------|----------|--------|
| RD-words | Complete the Words | 8 | 10 | 80% | 🟢 |
| RD-daily | Read in Daily Life | 2 | 2 | 100% | ⚪ |
| RD-academic | Read an Academic Passage | 2 | 3 | 67% | 🟡 |
| LS-response | Listen and Choose a Response | 3 | 3 | 100% | 🟢 |
| LS-conversation | Listen to a Conversation | 2 | 2 | 100% | ⚪ |
| LS-announcement | Listen to an Announcement | 1 | 1 | 100% | ⚪ |
| LS-talk | Listen to an Academic Talk | 2 | 2 | 100% | ⚪ |
| WR-build | Build a Sentence | 1 | 3 | 33% | 🔴 |

## Writing / Speaking (rubric 0–5)
| Subtype | Tag | Avg score | Attempts | Status |
|---------|-----|-----------|----------|--------|
| _(empty)_ | | | | |

---

## Weak types (priority for `/toefl review`)
1. 🔴 **WR-build** 33% (1/3) — embedded question & relative clause: time/adverb phrase inserted in the
   middle (*~~what time tomorrow the meeting starts~~* → what time the meeting starts tomorrow;
   *~~the one last week that our professor recommended~~* → the one that our professor recommended last week); spelling *~~meetting~~*.
2. 🟡 **RD-academic** 67% (2/3) — `RD-vocab` miss: *significantly* ≈ noticeably (chose *quickly*).
