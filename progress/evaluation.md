# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Updated 2026-11-01 after `/quiz` #3 (Unit 1,
12 items, 9/12); earlier: `/quiz-t` #2 (2026-10-30, 4/4), `/quiz` #2 (2026-10-30, 11/12), `/quiz` #1 (2026-10-29, 10/12), `/quiz-t` #1 (2026-10-29, 2/4).
Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `A2-present-simple` | 14 | 18 | 78% | 🟡 (MCQ 3/4 on 2026-11-01: agreement/doesn't/Do all ✅, missed adverb position *~~Priya always is late~~* → *is always late*; translate 3/3 on 2026-10-30: *my two cousins watch*, *doesn't drink*, *Does your sister work*; MCQ 4/4 same day; earlier: *my cousins goes*, *they brings*, *my parent drinks* for "orang tua") |
| `A2-present-perfect` | 10 | 12 | 83% | 🟢 (MCQ 2/3 on 2026-11-01: *has studied since*, *have had this coat* ✅; missed *~~How long do you known~~* → *How long have you known*; production fixed 2026-10-30: *I have had this bike since 2019* ✅; earlier slip *I have this coat for 3 years*) |
| `SK-vocab` | 9 | 9 | 100% | 🟢 |
| `SK-reading` | 9 | 10 | 90% | 🟢 (2/2 on 2026-11-01 incl. main idea & inference; earlier missed main idea: picked a detail-based topic) |
| `SK-collocation` | 1 | 2 | — | ⚪ (*~~take attention~~* → **pay attention**) |
| `SK-paraphrase` | 3 | 3 | 100% | 🟢 |
| `SK-writing` | 6 | 9 | 67% | 🟡 (translate 4/4 on 2026-10-30; still slips: sentence-initial capital, *exciting film* → films; earlier: verb-form, dropped subjects, articles) |

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-agreement` | 15 | 19 | 79% | 🟡 (MCQ 3/3 on 2026-11-01; production 3/3 on 2026-10-30; earlier *my parent drinks*) |
| `ERR-tense` | 11 | 15 | 73% | 🟡 (2026-11-01: *How long do you known* ✗; *have had* now correct in production; earlier *I have this coat for 3 years*) |
| `ERR-wordorder` | 3 | 4 | 75% | 🟡 (*~~always is late~~* → *is always late*: adverb goes after *be*) |
| `ERR-prep` | 3 | 3 | 100% | 🟢 (for/since) |
| `ERR-wordchoice` | 1 | 2 | — | ⚪ (do the housework ✅; *~~take attention~~* → pay attention) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 36 | 44 | 82% | 🟢 |

---

## Weak areas (priority for next questions)

1. 🟡 **Writing accuracy** (`SK-writing` 67%, up from 40% after translate 4/4) — remaining slips:
   capital letter at sentence start (*~~my~~ My*), plural after *exciting* (*~~exciting film~~* →
   **exciting films**); earlier: verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *Saturday*, sentence-initial
   *My/I*); translate: *~~my parent drinks~~* → **My parents drink**.
2. 🔴 **First conditional** (from diagnostic) — present simple in the *if*-clause (*If it rains,
   we will stay*). No unit yet → not testable; future tag e.g. `B1-first-conditional`.
3. 🟡 **`A2-present-simple`** (78%, `ERR-agreement` 79%) — agreement now solid in MCQ (3/3 on
   2026-11-01); new slip = **adverb of frequency with _be_**: *~~Priya always is late~~* →
   **Priya is always late** (`ERR-wordorder` 75%). Earlier: translate 3/3 on 2026-10-30, MCQ 4/4 on
   2026-10-30 (*my grandparents cook*, *Do your brothers…?*, *Daniel doesn't drink*), but earlier
   errors *~~My cousins goes~~*, *~~they brings~~*, *~~my parent drinks~~* → keep checking,
   especially in production (`/quiz-t`).

4. 🟡 **`ERR-tense` — *How long* questions** (73%) — *~~How long do you known~~* → **How long
   have you known** (have/has + past participle in the question too).

**Strengths (de-prioritize):** `A2-present-perfect` 🟢 83% (watch *How long have…?* and *have had*
in production), `SK-vocab` 🟢, `SK-reading` 🟢, `SK-paraphrase` 🟢, `ERR-prep` 🟢 — pull richer B1/B2 material
for vocab/reading.
