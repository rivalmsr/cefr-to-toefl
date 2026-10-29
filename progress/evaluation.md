# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Updated 2026-10-29 after `/quiz` #1 (Unit 1,
12 items, 10/12). Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `A2-present-simple` | 2 | 4 | 50% | 🔴 (agreement with plural subject: *my cousins goes*, *they brings*) |
| `A2-present-perfect` | 3 | 3 | 100% | 🟢 |
| `SK-vocab` | 7 | 7 | 100% | 🟢 |
| `SK-reading` | 6 | 6 | 100% | 🟢 |
| `SK-paraphrase` | 1 | 1 | — | ⚪ |
| `SK-writing` | 0 | 1 | — | ⚪ (A2 sample: verb-form, dropped subjects, articles) |

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-agreement` | 2 | 5 | 40% | 🔴 (plural subject + -s: *my cousins goes*, *they brings*) |
| `ERR-tense` | 3 | 5 | 60% | 🟡 (diagnostic misses; present perfect now correct 3/3) |
| `ERR-prep` | 1 | 1 | — | ⚪ (for/since) |
| `ERR-wordorder` | 1 | 1 | — | ⚪ (adverb of frequency position) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 10 | 12 | 83% | 🟢 |

---

## Weak areas (priority for next questions)

1. 🔴 **`A2-present-simple` — subject–verb agreement** (50%, `ERR-agreement` 40%) — plural
   subject takes the base verb. Quiz errors: *~~My cousins goes~~ to the gym* → **go**; missed
   *~~they brings~~ her some cake* in error identification → **bring**. Negatives/word order were
   correct.
2. 🔴 **First conditional** (from diagnostic) — present simple in the *if*-clause (*If it rains,
   we will stay*). No unit yet → not testable; future tag e.g. `B1-first-conditional`.
3. 🟡 **Writing accuracy** (`SK-writing`) — verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *At the end of the day*).

**Strengths (de-prioritize):** `SK-vocab` 🟢, `SK-reading` 🟢, `A2-present-perfect` 🟢 (3/3 —
small sample, keep 1 maintenance item) — pull richer B1/B2 material for vocab/reading.
