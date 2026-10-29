# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Numbers below are initial attempts; `/quiz`
will add to them. Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `SK-vocab` | 5 | 5 | 100% | 🟢 |
| `SK-reading` | 4 | 4 | 100% | 🟢 |
| `SK-writing` | 0 | 1 | — | ⚪ (A2 sample: verb-form, dropped subjects, articles) |

_(No `<level>-<slug>` grammar tags yet — units not written. Grammar weaknesses recorded in
Weak areas below; add tags to `reference/quiz-taxonomy.md` when the A2 unit is created.)_

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-tense` | 0 | 2 | 0% | ⚪ (present perfect for/since; 1st-conditional if-clause) |
| `ERR-agreement` | 0 | 1 | 0% | ⚪ (they + base verb, no -s) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| _(none — no units in scope yet)_ | | | | |

---

## Weak areas (priority for next questions)
Detected at placement (grammar tags to be created with the A2 unit):

1. 🔴 **Subject–verb agreement** — present simple, plural subject takes the base verb (*they go*,
   not *they goes*). → future tag e.g. `A2-present-simple`.
2. 🔴 **Present perfect for/since** — past action continuing to now (*I have lived here for three
   years*). Confused with present continuous. → future tag e.g. `A2-present-perfect`.
3. 🔴 **First conditional** — present simple in the *if*-clause (*If it rains, we will stay*), not
   *will* in both clauses. → future tag e.g. `B1-first-conditional`.
4. 🟡 **Writing accuracy** (`SK-writing`) — verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *At the end of the day*).

**Strengths (de-prioritize):** `SK-vocab` 🟢, `SK-reading` 🟢 — pull richer B1/B2 material here.
