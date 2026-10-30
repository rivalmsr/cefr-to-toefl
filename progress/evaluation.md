# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Updated 2026-10-30 after `/quiz` #2 (Unit 1,
12 items, 11/12); earlier: `/quiz` #1 (2026-10-29, 10/12), `/quiz-t` #1 (2026-10-29, 2/4).
Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `A2-present-simple` | 8 | 11 | 73% | 🟡 (MCQ 4/4 on 2026-10-30; earlier: *my cousins goes*, *they brings*, *my parent drinks* for "orang tua") |
| `A2-present-perfect` | 7 | 8 | 88% | 🟢 (MCQ incl. negatives / How long all correct; production slip earlier: *I have this coat for 3 years* → **have had**) |
| `SK-vocab` | 8 | 8 | 100% | 🟢 |
| `SK-reading` | 7 | 8 | 88% | 🟢 (missed main idea: picked a detail-based topic) |
| `SK-collocation` | 1 | 1 | — | ⚪ |
| `SK-paraphrase` | 2 | 2 | — | ⚪ |
| `SK-writing` | 2 | 5 | 40% | 🔴 (A2 sample: verb-form, dropped subjects, articles; translate 2/4) |

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-agreement` | 9 | 13 | 69% | 🟡 (MCQ now solid; production still the risk: *my parent drinks*) |
| `ERR-tense` | 7 | 10 | 70% | 🟡 (production: present simple instead of present perfect — *I have this coat for 3 years*) |
| `ERR-wordorder` | 3 | 3 | 100% | 🟢 |
| `ERR-prep` | 2 | 2 | — | ⚪ (for/since) |
| `ERR-wordchoice` | 1 | 1 | — | ⚪ (do the housework) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 23 | 28 | 82% | 🟢 |

---

## Weak areas (priority for next questions)

1. 🔴 **Writing accuracy** (`SK-writing` 40%) — verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *Saturday*, sentence-initial
   *My/I*); translate: *~~my parent drinks~~* → **My parents drink**.
2. 🔴 **First conditional** (from diagnostic) — present simple in the *if*-clause (*If it rains,
   we will stay*). No unit yet → not testable; future tag e.g. `B1-first-conditional`.
3. 🟡 **`A2-present-simple` — subject–verb agreement** (73%, `ERR-agreement` 69%) — MCQ 4/4 on
   2026-10-30 (*my grandparents cook*, *Do your brothers…?*, *Daniel doesn't drink*), but earlier
   errors *~~My cousins goes~~*, *~~they brings~~*, *~~my parent drinks~~* → keep checking,
   especially in production (`/quiz-t`).

**Strengths (de-prioritize):** `A2-present-perfect` 🟢 (MCQ; still watch *have had* in
production), `SK-vocab` 🟢, `SK-reading` 🟢, `ERR-wordorder` 🟢 — pull richer B1/B2 material
for vocab/reading.
